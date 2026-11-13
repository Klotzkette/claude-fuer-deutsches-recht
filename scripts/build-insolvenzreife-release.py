#!/usr/bin/env python3
"""Baut und prüft das Komponentenpaket samt drei vollständigen Originalakten."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
from shutil import copyfile
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter

from prompt_profiles import PROMPT_SUFFIXES
from release_routing import scoped_asset_url, validate_plugin_version
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import expected_arcnames
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
NAME = "zahlungsunfaehigkeits-und-ueberschuldungspruefer"
VERSION = "1.0.0"
TAG = f"{NAME}-v{VERSION}"
PLUGIN = ROOT / NAME
CASES = (
    "insolvenzreife-hubschrauber-prenzlau",
    "insolvenzreife-keramikfabrik-cottbus",
    "insolvenzreife-metallbau-berlin-zehlendorf",
)
BUNDLE = "Insolvenzreife_Drei_Originalakten.zip"
INVENTORY = "release-bestand.json"
CHECKSUMS = "checksums-sha256.txt"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plugin_files():
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    entry = next(item for item in marketplace["plugins"] if item["name"] == NAME)
    validate_plugin_version(entry, marketplace["version"], root=ROOT)
    manifests = ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")
    for name in manifests:
        manifest = json.loads((PLUGIN / name).read_text(encoding="utf-8"))
        if (manifest["name"], manifest["version"], manifest["description"]) != (NAME, VERSION, entry["description"]):
            raise ValueError(f"Manifest weicht vom Marketplace ab: {name}")
    if len(list((PLUGIN / "skills").glob("*/SKILL.md"))) != 11:
        raise ValueError("Zehn Fachskills und ein Hauptskill erforderlich")
    paths = {}
    for path in sorted(PLUGIN.rglob("*")):
        relative = path.relative_to(PLUGIN)
        if path.is_symlink():
            raise ValueError(f"Symbolischer Link im Plugin: {relative}")
        if (path.is_file() and not path.name.endswith(PROMPT_SUFFIXES) and path.name != ".DS_Store"
                and not set(relative.parts) & {"tests", "__pycache__", "node_modules"}):
            paths[relative.as_posix()] = path
    paths["LICENSE"] = ROOT / "LICENSE"
    return paths


def original_name(slug):
    return f"testakte-{slug}.zip"


def single_name(slug):
    return f"testakte-{slug}-einzelpdfs.zip"


def combined_name(slug):
    return f"{slug}_gesamt.pdf"


def combined_pdf(single_zip, target, title):
    writer = PdfWriter()
    writer.add_metadata({"/Title": title, "/Author": "Kanzleiakte"})
    with ZipFile(single_zip) as archive:
        for name in sorted(member for member in archive.namelist() if member.endswith(".pdf")):
            start = len(writer.pages)
            writer.append(PdfReader(io.BytesIO(archive.read(name))), import_outline=False)
            writer.add_outline_item(name, start)
    with target.open("wb") as output:
        writer.write(output)


def asset_names():
    return {
        f"{NAME}.zip", f"{NAME}-portable.zip", f"{NAME}-werkstatt.md", f"{NAME}-schnellstart.md",
        BUNDLE, "Stichtagskontrolle_Nachbesprechung.zip",
        *(file for slug in CASES for file in (original_name(slug), single_name(slug))),
    }


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeverzeichnis muss leer sein")
    dist.mkdir(parents=True, exist_ok=True)
    native = load("build-testakten-release-zips")
    pdf = load("build-testakten-einzelpdf-zips")
    paths = plugin_files()
    for archive_name, prefix in ((f"{NAME}.zip", ""), (f"{NAME}-portable.zip", f"{NAME}/")):
        with ZipFile(dist / archive_name, "x") as archive:
            for name, path in paths.items():
                native.write_file(archive, path, prefix + name)
    for kind in ("werkstatt", "schnellstart"):
        prompt = f"{NAME}-{kind}.md"
        copyfile(PLUGIN / prompt, dist / prompt)
    for slug in CASES:
        case_dir = ROOT / "testakten" / slug
        native.build_single(case_dir, dist)
        single, _ = pdf.build_single(case_dir, dist)
        title = (case_dir / "README.md").read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
        stored = case_dir / "gesamt-pdf" / combined_name(slug)
        stored.parent.mkdir(exist_ok=True)
        combined_pdf(single, stored, title)
    with ZipFile(dist / BUNDLE, "x") as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for slug in CASES:
            name = original_name(slug)
            native.write_file(archive, dist / name, name)
    with ZipFile(dist / "Stichtagskontrolle_Nachbesprechung.zip", "x") as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for path in sorted((ROOT / "quality/insolvenzreife").glob("*")):
            if path.suffix in {".md", ".json"}:
                native.write_file(archive, path, path.name)
    report = inspect(dist)
    (dist / INVENTORY).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dist / CHECKSUMS).write_text("".join(
        f"{digest(path)}  {path.name}\n" for path in sorted(dist.iterdir())
    ), encoding="ascii")
    return report


def inspect(dist):
    native = load("validate-testakten-release-zips")
    pdf = load("validate-testakten-einzelpdf-zips")
    report = {"tag": TAG, "cases": {}}
    for filename, prefix in ((f"{NAME}.zip", ""), (f"{NAME}-portable.zip", f"{NAME}/")):
        paths = plugin_files()
        with ZipFile(dist / filename) as archive:
            assert set(archive.namelist()) == {prefix + name for name in paths}
            assert archive.testzip() is None
            for name, path in paths.items():
                assert archive.read(prefix + name) == path.read_bytes(), name
    for slug in CASES:
        directory = ROOT / "testakten" / slug
        archive_path = dist / original_name(slug)
        pairs = working_dump_archive_pairs(directory, include_gesamt_pdf=False)
        expected = [NOTICE_FILENAME, *(name for _, name in pairs)]
        native.assert_same(slug, expected, native.zip_entries(archive_path, require_notice=True, allow_directories=True))
        with ZipFile(archive_path) as archive:
            assert all(archive.read(name) == source.read_bytes() for source, name in pairs)
        bank = sum(name.startswith("Grundakte/01_Bank/Auszug_") for name in expected)
        procedural = sum(name.startswith("10_Verfahren/") for name in expected)
        assert bank == 24 and procedural >= 4, slug
        singles = dist / single_name(slug)
        expected_pdfs = expected_arcnames(directory)
        pdf.assert_same(slug, [NOTICE_FILENAME, *expected_pdfs],
                        pdf.zip_entries(singles, expected_suffix=".pdf", allow_directories=True))
        combined = directory / "gesamt-pdf" / combined_name(slug)
        with ZipFile(singles) as archive:
            pages = sum(len(PdfReader(io.BytesIO(archive.read(name))).pages) for name in expected_pdfs)
        reader = PdfReader(combined)
        assert len(reader.pages) == pages and len(reader.outline) == len(expected_pdfs)
        report["cases"][slug] = {"originals": len(pairs), "bank_months": bank, "procedure_documents": procedural,
                                 "pdf_pages": pages, "original_sha256": digest(archive_path),
                                 "combined_sha256": digest(combined)}
    for name in (f"{NAME}.zip", f"{NAME}-portable.zip",
                 *(file for slug in CASES for file in (original_name(slug), single_name(slug)))):
        assert scoped_asset_url(name, root=ROOT).endswith(f"/{TAG}/{name}")
    with ZipFile(dist / BUNDLE) as archive:
        assert archive.namelist() == [NOTICE_FILENAME, *(original_name(slug) for slug in CASES)]
        assert archive.read(NOTICE_FILENAME) == NOTICE_BYTES and archive.testzip() is None
        assert all(archive.read(original_name(slug)) == (dist / original_name(slug)).read_bytes() for slug in CASES)
    with ZipFile(dist / "Stichtagskontrolle_Nachbesprechung.zip") as archive:
        assert archive.read(NOTICE_FILENAME) == NOTICE_BYTES and len(archive.namelist()) > 1
        assert archive.testzip() is None
    return report


def verify(dist):
    hashes = dict(line.split("  ", 1)[::-1] for line in (dist / CHECKSUMS).read_text(encoding="ascii").splitlines())
    expected = asset_names() | {INVENTORY}
    if hashes.keys() != expected or {file.name for file in dist.iterdir()} != expected | {CHECKSUMS}:
        raise ValueError("Unerwarteter Releasebestand")
    for name, sha in hashes.items():
        if digest(dist / name) != sha:
            raise ValueError(f"Prüfsummenabweichung: {name}")
    actual = inspect(dist)
    if actual != json.loads((dist / INVENTORY).read_text(encoding="utf-8")):
        raise ValueError("Releaseinventar stimmt nicht")
    return actual


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    print(json.dumps((verify if args.verify else build)(args.dist), ensure_ascii=False, indent=2))
