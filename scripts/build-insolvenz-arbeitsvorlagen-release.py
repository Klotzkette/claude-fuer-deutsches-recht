#!/usr/bin/env python3
"""Ergänzt die veröffentlichten nativen Insolvenz-Testakten um die freigegebenen Arbeitsvorlagen."""
from __future__ import annotations

import argparse
import importlib
import io
import json
import os
import re
import shutil
import subprocess
import tempfile
from collections import Counter
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo

from akteneingang.quellen import Sources, URL, digest
from release_asset_common import read_checksums, sha256_file, write_checksums
from release_rate_limits import require_download_budget
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_zip_common import editable_working_forms, safe_archive_name


ROOT = Path(__file__).resolve().parents[1]
REPO = "Klotzkette/claude-fuer-deutsches-recht"
TAG = "insolvenz-arbeitsvorlagen-v1.0.0"
SCOPE = {"tag": TAG, "version": "1.0.0", "title": "Insolvenz-Testakten mit bearbeitbaren Arbeitsvorlagen"}
SOURCES_FILE = Path("scripts/data/insolvenz-arbeitsvorlagen-quellen.json")
INVENTORY = "release-bestand.json"
CHECKSUMS = "checksums-sha256.txt"
OLD_TAGS = {"grundakten-sammlung-v1.0.0": 20, "insolvenz-arbeitsakten-v1.0.0": 5,
            "grundakten-fachakten-v1.1.0": 25}
FORMS = importlib.import_module("build-insolvenz-arbeitsvorlagen")
PUBLISHER = importlib.import_module("publish-skill-quality-release")


def scope_files(root):
    sources = json.loads((root / SOURCES_FILE).read_bytes())["quellen"]
    cases = [slug for slug, _ in FORMS.case_list(root)]
    names = {prefix + slug + ".zip": slug for slug in cases for prefix in ("testakte-", "lebensakte-")}
    if set(names) != set(sources) or Counter(q["tag"] for q in sources.values()) != OLD_TAGS:
        raise ValueError("Quellregister deckt die beiden veröffentlichten ZIP-Varianten der 25 Akten nicht ab")
    for name, source in sources.items():
        if (set(source) != {"tag", "sha256", "bytes"} or not re.fullmatch("[0-9a-f]{64}", source["sha256"])
                or type(source["bytes"]) is not int or source["bytes"] <= 0
                or name.startswith("lebensakte-") != (source["tag"] == "grundakten-fachakten-v1.1.0")):
            raise ValueError(f"Ungültige Quellbindung: {name}")
    additions = {}
    for slug in cases:
        folder = root / "testakten" / slug
        additions[slug] = {name: path.read_bytes() for path, name in editable_working_forms(folder)}
        specs = json.loads((root / FORMS.SOURCES / "faelle" / f"{slug}.json").read_bytes())
        expected = {FORMS.filename(spec) for spec in (specs if isinstance(specs, list) else [specs])}
        if (not expected or set(additions[slug]) !=
                {f"Arbeitsvorlagen/{name}" for name in expected | {FORMS.GENERAL + ".docx"}}):
            raise ValueError(f"Arbeitsvorlagen fehlen oder sind nicht im freigegebenen Umfang enthalten: {slug}")
    return sources, names, additions


def original_names(archive):
    names = archive.namelist()
    if (not names or names[0] != NOTICE_FILENAME or not archive.read(NOTICE_FILENAME).startswith(NOTICE_BYTES)
            or not any(name.startswith("Grundakte/") for name in names)
            or len(names) != len({n.casefold() for n in names})
            or any(not safe_archive_name(n, allow_directories=True) or
                   n.split("/")[0].casefold() == "arbeitsvorlagen" for n in names)):
        raise ValueError("Quell-ZIP ohne eindeutigen Originalbestand, Grundakte oder zweisprachigen Hinweis")
    return names


def append_forms(original, destination, additions):
    destination.write_bytes(original)
    with ZipFile(destination, "a") as archive:
        original_names(archive)
        for name, content in sorted(additions.items()):
            # Office-Dokumente sind selbst bereits komprimierte ZIPs. Gespeicherte
            # Einträge sind unabhängig von der zlib-Version reproduzierbar.
            info = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_STORED
            info.create_system, info.external_attr = 3, 0o100644 << 16
            archive.writestr(info, content)


def inspect_archive(original, path, additions):
    with ZipFile(io.BytesIO(original)) as old, ZipFile(path) as new:
        names = original_names(old)
        if new.namelist() != names + sorted(additions) or new.comment != old.comment:
            raise ValueError(f"{path.name}: Mitgliederauswahl, Reihenfolge oder ZIP-Kommentar abweichend")
        # Vergleicht auch die ursprünglichen komprimierten Daten und lokalen Header.
        with path.open("rb") as stream:
            if stream.read(old.start_dir) != original[:old.start_dir]:
                raise ValueError(f"{path.name}: Datenbereich der historischen Originaldateien verändert")
        if any(new.read(name) != old.read(name) for name in names):
            raise ValueError(f"{path.name}: ursprüngliches Aktenstück verändert")
        for name, content in additions.items():
            if new.read(name) != content:
                raise ValueError(f"{path.name}: Arbeitsvorlage weicht von der Akte ab: {name}")
    return {"alte_dateien": len(names), "arbeitsvorlagen": {n: digest(b) for n, b in sorted(additions.items())}}


def asset_metadata(path):
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


class Edition:
    checkout_state = staticmethod(PUBLISHER.B.checkout_state)

    def __init__(self, cache, offline=False):
        self.cache = Path(cache)
        self.offline = offline

    def original(self, name, source):
        path = self.cache / source["tag"] / name
        if path.is_file():
            data = path.read_bytes()
        elif self.offline:
            raise ValueError(f"Verifizierte Quelldatei fehlt im Offline-Cache: {name}")
        else:
            data = Sources().read({"url": URL + source["tag"] + "/" + name,
                                   "size": source["bytes"], "sha256": source["sha256"]})
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temporary:
                temporary.write(data)
            os.replace(temporary.name, path)
        if len(data) != source["bytes"] or digest(data) != source["sha256"]:
            raise ValueError(f"Quelldatei weicht von der veröffentlichten SHA-256 oder Größe ab: {name}")
        return data

    def build(self, dist, root, expected_commit=None):
        state = self.checkout_state(root, expected_commit)
        sources, names, additions = scope_files(root)
        if dist.exists() and any(dist.iterdir()):
            raise ValueError("Das Ausgabeverzeichnis muss leer sein")
        dist.mkdir(parents=True, exist_ok=True)
        assets = {}
        for name, source in sources.items():
            path = dist / name
            original = self.original(name, source)
            forms = additions[names[name]]
            append_forms(original, path, forms)
            assets[name] = {**asset_metadata(path), "quelle": source, **inspect_archive(original, path, forms)}
        collection = dist / FORMS.COLLECTION.name
        shutil.copyfile(root / FORMS.COLLECTION, collection)
        assets[collection.name] = asset_metadata(collection)
        report = {"tag": TAG, "quelle_commit": state["commit"], "quelle_sauber": state["clean"], "assets": assets}
        (dist / INVENTORY).write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                                      encoding="utf-8")
        write_checksums(dist)
        self.validate_assets(dist, SCOPE, root, expected_commit=expected_commit)
        return report

    def validate_assets(self, dist, scope, root, *, expected_commit=None):
        sources, names, additions = scope_files(root)
        report = json.loads((dist / INVENTORY).read_bytes())
        assets = report["assets"]
        expected_assets = set(names) | {FORMS.COLLECTION.name}
        if (scope != SCOPE or report["tag"] != TAG or set(assets) != expected_assets
                or not re.fullmatch("[a-f0-9]{40}", report["quelle_commit"])
                or (expected_commit and (report["quelle_commit"] != expected_commit or report["quelle_sauber"] is not True))
                or {p.name for p in dist.iterdir()} != expected_assets | {INVENTORY, CHECKSUMS}):
            raise ValueError("Unvollständige Ausgabe oder abweichende Freigabe")
        sums = read_checksums(dist / CHECKSUMS)
        if set(sums) != expected_assets | {INVENTORY} or any(sha256_file(dist / n) != h for n, h in sums.items()):
            raise ValueError("Bestand oder Inhalt weicht von den Release-Prüfsummen ab")
        for name, source in sources.items():
            path = dist / name
            detail = inspect_archive(self.original(name, source), path, additions[names[name]])
            if assets[name] != {**asset_metadata(path), "quelle": source, **detail}:
                raise ValueError(f"Bestandsnachweis weicht von Original oder Ergänzungen ab: {name}")
        collection = root / FORMS.COLLECTION
        if (collection.read_bytes() != (dist / collection.name).read_bytes()
                or assets[collection.name] != asset_metadata(collection)):
            raise ValueError("Vorlagensammlung weicht von der freigegebenen Repository-Datei ab")
        return report

    def verify_download(self, dist, scope, root, repo, expected_commit):
        require_download_budget(len(list(dist.iterdir())))
        with tempfile.TemporaryDirectory(prefix="insolvenz-arbeitsvorlagen-download-") as folder:
            target = Path(folder)
            subprocess.run(["gh", "release", "download", TAG, "--repo", repo, "--dir", folder],
                           check=True, timeout=1800)
            self.validate_assets(target, scope, root, expected_commit=expected_commit)
            if any(sha256_file(p) != sha256_file(target / p.name) for p in dist.iterdir()):
                raise ValueError("Download des Release-Entwurfs weicht vom geprüften Bau ab")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True, help="Lokaler Cache der früheren Release-ZIPs.")
    parser.add_argument("--offline", action="store_true", help="Ausschließlich geprüfte Quelldateien im Cache nutzen.")
    parser.add_argument("--expected-commit", help="Vollständiger SHA des freigegebenen sauberen Checkout.")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--publish", action="store_true", help="Nach vollständig geprüfter Ausgabe aus main veröffentlichen.")
    action.add_argument("--verify", action="store_true", help="Die vorhandene Ausgabe vollständig vergleichen.")
    args = parser.parse_args()
    edition = Edition(args.cache, args.offline)
    dist = args.dist.resolve()
    if args.publish and not args.expected_commit:
        parser.error("--publish erfordert --expected-commit")
    if args.verify:
        report = edition.validate_assets(dist, SCOPE, ROOT, expected_commit=args.expected_commit)
    else:
        report = edition.build(dist, ROOT, args.expected_commit)
        if args.publish:
            PUBLISHER.publish(dist, SCOPE, args.expected_commit, REPO, builder=edition)
    print(f"{TAG}: {len(report['assets'])} ZIPs mit vollständigem Bestands- und Prüfsummennachweis.")


if __name__ == "__main__":
    main()
