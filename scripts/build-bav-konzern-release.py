#!/usr/bin/env python3
"""Begrenzter bAV-Release aus unveränderten Originalen und geprüften Lesefassungen.

Die Veröffentlichung rendert keine Office-Dateien neu. Der lokale Aktenbuilder
erzeugt und prüft die Lesefassungen mit den lizenzierten Satzschriften; dieses
Werkzeug bindet jedes veröffentlichte Byte an den freigegebenen Checkout.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import posixpath
from pathlib import Path
import shutil
import subprocess
import tempfile
from zipfile import ZipFile

from pypdf import PdfReader
from release_asset_common import expected_asset_metadata, read_checksums, sha256_file, write_checksums
from release_rate_limits import require_download_budget
from release_routing import scoped_asset_url, validate_plugin_version
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_grundakte import check_intake_member
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "bav-strategie-konzern"
VERSION = "445.36.4"
TAG = f"{PLUGIN}-v{VERSION}"
CASES = (
    "bav-strategie-konzern-meissner-rheinwerk-ag",
    "bav-carve-out-rheinbogen-automation",
    "bav-rentnergesellschaft-rheinhafen-logistik",
    "bav-pensionskasse-niederrhein-verbund",
)
PROMPTS = (f"{PLUGIN}-werkstatt.md", f"{PLUGIN}-schnellstart.md")
BUNDLE = "BAV_Konzern_Vier_Arbeitsakten.zip"
REPORT = "release-bestand.json"
CHECKSUMS = "checksums-sha256.txt"
SCOPE = {"schema_version": 1, "version": VERSION, "tag": TAG,
         "title": "Betriebliche Altersversorgung im Konzern – vier Arbeitsakten",
         "plugins": [{"name": PLUGIN}], "cases": list(CASES)}


def load(filename):
    import importlib.util
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


Q = load("build-skill-quality-release.py")
NATIVE = load("build-testakten-release-zips.py")
checkout_state = Q.checkout_state


def names(slug):
    return f"testakte-{slug}.zip", f"testakte-{slug}-einzelpdfs.zip", f"{slug}_gesamt.pdf"


def expected_names():
    return {f"{PLUGIN}.zip", *PROMPTS, BUNDLE, REPORT, CHECKSUMS,
            *(name for slug in CASES for name in names(slug))}


def validate_scope(scope, root):
    if scope != SCOPE:
        raise ValueError("Nur der vollständige festgelegte bAV-Komponentenbestand ist zulässig")
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    entry = next(row for row in market["plugins"] if row["name"] == PLUGIN)
    validate_plugin_version(entry, market["version"], root=root)
    if entry["version"] != VERSION or (root / entry["source"]).resolve() != root / PLUGIN:
        raise ValueError("Pluginquelle oder Version passt nicht zum Komponentenrelease")
    # Das zentrale Routing verwaltet installierbare Plugins und einzelne Akten-ZIPs.
    # Prompts, Gesamt-PDFs und Sammelpaket werden unter dem festen Komponententag
    # veröffentlicht; sie sind kein Fallback des zentralen Downloadrouters.
    routed = {f"{PLUGIN}.zip", *(name for slug in CASES for name in names(slug)[:2])}
    for name in routed:
        if scoped_asset_url(name, root=root) != f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}/{name}":
            raise ValueError(f"Exakte Komponentenroute fehlt: {name}")


def verified_archive(path, sources, *, notice=False):
    if any(source.is_symlink() or not source.is_file() for source, _ in sources):
        raise ValueError("Archivquellen müssen reguläre Dateien sein")
    expected = {name: source.read_bytes() for source, name in sources}
    if len(expected) != len(sources):
        raise ValueError("Doppelte Quellzuordnung im Archiv")
    if notice:
        expected[NOTICE_FILENAME] = NOTICE_BYTES
    with ZipFile(path) as archive:
        actual = archive.namelist()
        if len(actual) != len(set(actual)) or set(actual) != set(expected):
            raise ValueError(f"Abweichender Archivbestand: {path.name}")
        for name, data in expected.items():
            value = archive.read(name)
            # Der zentrale Builder ergänzt den verbindlichen Hinweis um die Anleitung.
            if name == NOTICE_FILENAME and notice:
                if not value.startswith(NOTICE_BYTES):
                    raise ValueError(f"Pflichthinweis fehlt: {path.name}")
            elif value != data:
                raise ValueError(f"Abweichende Originalbytes: {path.name}/{name}")
            if name.startswith("Grundakte/"):
                check_intake_member(name, value)
        return {name: hashlib.sha256(archive.read(name)).hexdigest() for name in sorted(actual)}


def verify_chapters(files, skills, root):
    registry = json.loads((root / "scripts/data/skill-source-replacements.json").read_text())
    entry = registry["plugins"][PLUGIN]
    chapters = entry["chapters"]
    actual = {name for name in files if name.startswith("references/konzern/") and name.endswith(".md")}
    if len(chapters) != 8 or len(set(chapters)) != 8 or actual != set(chapters):
        raise ValueError("Genau acht deklarierte Fachkapitel erforderlich")
    pending, reachable = list(skills), set()
    while pending:
        name = pending.pop()
        if name in reachable or name not in files:
            continue
        reachable.add(name)
        if files[name].suffix != ".md":
            continue
        for raw in Q.LINK.findall(files[name].read_text()):
            target = raw.partition("#")[0]
            if not target or ":" in target or target.startswith("/"):
                continue
            pending.append(posixpath.normpath(posixpath.join(posixpath.dirname(name), target)))
    if actual - reachable:
        raise ValueError(f"Fachkapitel vom Skill nicht erreichbar: {sorted(actual - reachable)}")
    return {name: sha256_file(files[name]) for name in sorted(actual)}


def case_evidence(dist, slug, root):
    original, singles, combined = names(slug)
    directory = root / "testakten" / slug
    sources = working_dump_archive_pairs(directory, include_gesamt_pdf=False)
    if not sources or any(not name.startswith(("Grundakte/", "Fortsetzung/")) for _, name in sources):
        raise ValueError(f"Grundakte und Fortsetzung müssen ausdrücklich getrennt sein: {slug}")
    hashes = verified_archive(dist / original, sources, notice=True)
    pdf_source = root / PLUGIN / "testakten/downloads" / singles
    if (dist / singles).read_bytes() != pdf_source.read_bytes():
        raise ValueError(f"Ungeprüfte Einzel-PDF-Fassung: {slug}")
    if (dist / combined).read_bytes() != (directory / "gesamt-pdf" / combined).read_bytes():
        raise ValueError(f"Gesamt-PDF weicht vom Checkout ab: {slug}")
    pairs = document_arcname_pairs(directory)
    pages, pdfs = 0, {}
    with ZipFile(dist / singles) as archive:
        members = archive.namelist()
        if (len(members) != len(set(members)) or set(members) != {NOTICE_FILENAME, *(name for _, name in pairs)}
                or not archive.read(NOTICE_FILENAME).startswith(NOTICE_BYTES)):
            raise ValueError(f"Einzel-PDF-Bestand oder Hinweis stimmt nicht: {slug}")
        for source, name in pairs:
            data = archive.read(name)
            reader = PdfReader(io.BytesIO(data))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            if not reader.pages or (not text.strip() and source.suffix.lower() not in {".png", ".jpg", ".jpeg"}):
                raise ValueError(f"Leere/nicht durchsuchbare Lesefassung: {slug}/{name}")
            if source.suffix == ".pdf" and data != source.read_bytes():
                raise ValueError(f"Original-PDF wurde beim Verpacken verändert: {slug}/{name}")
            pages += len(reader.pages)
            pdfs[name] = {"sha256": hashlib.sha256(data).hexdigest(), "pages": len(reader.pages),
                          "text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    reader = PdfReader(dist / combined)
    if len(reader.pages) != pages or not reader.outline:
        raise ValueError(f"Gesamtseiten oder Navigation stimmen nicht: {slug}")
    return {"files": len(sources), "intake": sum(name.startswith("Grundakte/") for _, name in sources),
            "originals": hashes, "pdfs": pdfs, "pages": pages, "combined_sha256": sha256_file(dist / combined)}


def inspect(dist, scope, root):
    validate_scope(scope, root)
    # Die Renderfreigabe bindet jede Lesefassung an ihre konkreten Quelldateien.
    # Ein bloßer Hash der Inventardatei würde veraltete PDF-Exporte nicht erkennen.
    from bav_konzern_verify import verify_inventory
    verify_inventory(root)
    if {p.name for p in dist.iterdir()} - {REPORT, CHECKSUMS} != expected_names() - {REPORT, CHECKSUMS}:
        raise ValueError("Unvollständiger oder überzähliger Komponentenbestand")
    if any(not p.is_file() or p.is_symlink() for p in dist.iterdir()):
        raise ValueError("Release darf keine Verzeichnisse oder Symlinks enthalten")
    files = Q.source_files(root, root / PLUGIN)
    manifests = Q.check_manifests(files, PLUGIN, VERSION)
    skills = Q.verify_reachability(files)
    if len(skills) != 10:
        raise ValueError("Genau zehn auswählbare Skills erforderlich")
    chapters = verify_chapters(files, skills, root)
    plugin_hashes = Q.verify_zip(dist / f"{PLUGIN}.zip", files)
    Q.CHECKS.validate_plugin_zip(dist, PLUGIN, VERSION)
    Q.CHECKS.validate_skill_sources(dist / f"{PLUGIN}.zip", root / PLUGIN)
    Q.CHECKS.validate_focus_skill(dist / f"{PLUGIN}.zip", root / PLUGIN, root / "quality/evals" / f"{PLUGIN}.json")
    for filename in PROMPTS:
        if (dist / filename).read_bytes() != (root / PLUGIN / filename).read_bytes():
            raise ValueError(f"Abweichender Prompt: {filename}")
    cases = {slug: case_evidence(dist, slug, root) for slug in CASES}
    verified_archive(dist / BUNDLE, [(dist / names(slug)[0], names(slug)[0]) for slug in CASES], notice=True)
    return {"schema_version": 1, "tag": TAG, "version": VERSION,
            "plugin": {"skills": skills, "chapters": chapters, "manifests": manifests, "files": plugin_hashes},
            "prompts": {name: sha256_file(dist / name) for name in PROMPTS}, "cases": cases,
            "render_inventory_sha256": sha256_file(root / PLUGIN / "testakten/pruefung/bestand.json")}


def validate_assets(dist, scope=SCOPE, root=ROOT, *, expected_commit=None):
    if {p.name for p in dist.iterdir()} != expected_names():
        raise ValueError("Releasebestand muss exakt 18 Dateien enthalten")
    report = json.loads((dist / REPORT).read_text())
    evidence = inspect(dist, scope, root)
    if {key: value for key, value in report.items() if key != "source_state"} != evidence:
        raise ValueError("Release-Inventar stimmt nicht mit den tatsächlichen Quellen überein")
    if expected_commit and report.get("source_state") != {"commit": expected_commit, "clean": True}:
        raise ValueError("Veröffentlichung verlangt den freigegebenen sauberen Commit")
    checks = read_checksums(dist / CHECKSUMS)
    if set(checks) != expected_names() - {CHECKSUMS}:
        raise ValueError("Prüfsummenbestand ist unvollständig")
    for name, digest in checks.items():
        if sha256_file(dist / name) != digest:
            raise ValueError(f"Abweichende Prüfsumme: {name}")
    return report


def build(dist, scope=SCOPE, root=ROOT, *, expected_commit=None):
    root, dist = root.resolve(), dist.resolve()
    if dist.is_relative_to(root):
        raise ValueError("Releaseziel muss außerhalb des Quellrepositories liegen")
    state = checkout_state(root, expected_commit)
    validate_scope(scope, root)
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError("Releaseziel muss leer sein")
    Q.write_zip(dist / f"{PLUGIN}.zip", Q.source_files(root, root / PLUGIN))
    for filename in PROMPTS:
        shutil.copyfile(root / PLUGIN / filename, dist / filename)
    for slug in CASES:
        _, singles, combined = names(slug)
        directory = root / "testakten" / slug
        NATIVE.build_single(directory, dist)
        shutil.copyfile(root / PLUGIN / "testakten/downloads" / singles, dist / singles)
        shutil.copyfile(directory / "gesamt-pdf" / combined, dist / combined)
    with ZipFile(dist / BUNDLE, "x") as archive:
        NATIVE.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for slug in CASES:
            name = names(slug)[0]
            NATIVE.write_file(archive, dist / name, name)
    report = {**inspect(dist, scope, root), "source_state": state}
    (dist / REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    write_checksums(dist)
    expected_asset_metadata(dist)
    validate_assets(dist, scope, root, expected_commit=expected_commit)
    return report


def verify_download(dist, scope, root, repo, expected_commit):
    validate_assets(dist, scope, root, expected_commit=expected_commit)
    require_download_budget(len(expected_names()))
    with tempfile.TemporaryDirectory(prefix="bav-download-") as folder:
        target = Path(folder)
        subprocess.run(["gh", "release", "download", TAG, "--repo", repo, "--dir", str(target)], check=True, timeout=1800)
        validate_assets(target, scope, root, expected_commit=expected_commit)
        for path in dist.iterdir():
            if sha256_file(path) != sha256_file(target / path.name):
                raise ValueError(f"Download weicht ab: {path.name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--expected-commit")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--verify-download", action="store_true")
    parser.add_argument("--repo", default="Klotzkette/claude-fuer-deutsches-recht")
    args = parser.parse_args()
    if args.verify_download:
        if not args.expected_commit:
            parser.error("Downloadprüfung benötigt --expected-commit")
        verify_download(args.dist, SCOPE, ROOT, args.repo, args.expected_commit)
    elif args.verify:
        validate_assets(args.dist, expected_commit=args.expected_commit)
    else:
        build(args.dist, expected_commit=args.expected_commit)
    print(f"{TAG}: 18 Release-Dateien vollständig geprüft")


if __name__ == "__main__":
    main()
