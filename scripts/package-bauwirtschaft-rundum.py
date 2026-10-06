#!/usr/bin/env python3
"""Baut ausschließlich die zwei Seminarpakete und ihre zehn Arbeitsakten."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import zipfile

from pypdf import PdfReader
from prompt_profiles import PROMPT_SUFFIXES
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "bauwirtschaft-rundum/seminarfaelle.json"


def module(stem):
    spec = importlib.util.spec_from_file_location(stem.replace("-", "_"), ROOT / "scripts" / f"{stem}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def check_flat(archive):
    names = archive.namelist()
    if len(names) != len(set(names)) or any("/" in name or "\\" in name for name in names):
        raise ValueError("Das Aktenarchiv enthält Unterordner oder doppelte Dateinamen.")
    if not names or names[0] != NOTICE_FILENAME or not archive.read(NOTICE_FILENAME).startswith(NOTICE_BYTES):
        raise ValueError("Der zweisprachige Hinweis muss zuerst in README.txt stehen.")
    if any(name.lower().endswith((".md", ".yaml", ".json")) for name in names):
        raise ValueError("Redaktionelle Begleitdateien gehören nicht in die Arbeitsakte.")


def build(destination):
    destination = destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    version = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["version"]
    overall = module("build-testakte-gesamt-pdf")
    individual = module("build-testakten-einzelpdf-zips")
    originals = module("build-testakten-release-zips")
    native_validator = module("validate-testakten-release-zips")
    pdf_validator = module("validate-testakten-einzelpdf-zips")
    plugin_validator = module("validate-release-zips")
    report = {"version": version, "plugins": [], "cases": [], "scope": "Zwei Pakete und zehn Akten; keine bestehenden Sammelarchive neu gebaut."}
    assets = []
    for plugin in catalog["plugins"]:
        name = plugin["name"]
        directory = ROOT / plugin["source"]
        target = destination / f"{name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(directory.rglob("*")):
                if not path.is_file() or path.name.endswith(PROMPT_SUFFIXES) or path.name in {"CLAUDE.md", ".DS_Store"} or "__pycache__" in path.parts:
                    continue
                if path.suffix.lower() in {".pyc", ".pdf", ".docx", ".xlsx", ".zip"}:
                    raise ValueError(f"Unerwartete Binärdatei im Seminar-Plugin: {path}")
                originals.write_file(archive, path, path.relative_to(directory).as_posix())
        plugin_validator.validate_plugin_zip(destination, name, version)
        assets.append(target)
        for kind in ("werkstatt", "schnellstart"):
            path = directory / f"{name}-{kind}.md"
            target = destination / path.name
            shutil.copyfile(path, target)
            assets.append(target)
        report["plugins"].append({"name": name, "skills": len(list((directory / "skills").glob("*/SKILL.md")))})
        for item in plugin["cases"]:
            folder = ROOT / "testakten" / item["slug"]
            status, message = overall.build_gesamt_pdf(folder)
            if status != "ok":
                raise ValueError(message)
            print(message, flush=True)
            separate, count = individual.build_single(folder, destination)
            native, _ = originals.build_single(folder, destination)
            native_validator.assert_same(native.name, native_validator.expected_entries(folder), native_validator.zip_entries(native, require_notice=True))
            pdf_validator.assert_same(separate.name, [NOTICE_FILENAME, *pdf_validator.expected_arcnames(folder)], pdf_validator.zip_entries(separate, expected_suffix=".pdf"))
            pairs = working_dump_archive_pairs(folder, include_gesamt_pdf=False)
            native_paths = [p for p, _ in pairs]
            if len(native_paths) < 10 or len({p.suffix.lower() for p in native_paths}) < 4:
                raise ValueError(f"{folder.name}: Umfang oder Formatvielfalt reicht nicht aus.")
            with zipfile.ZipFile(native) as archive:
                check_flat(archive)
                for path, arcname in pairs:
                    if archive.read(arcname) != path.read_bytes():
                        raise ValueError(f"Original nicht bytegleich: {path}")
            with zipfile.ZipFile(separate) as archive:
                check_flat(archive)
                expected = document_arcname_pairs(folder)
                if set(archive.namelist()) != {NOTICE_FILENAME, *(name for _, name in expected)}:
                    raise ValueError(f"{folder.name}: Einzel-PDF-Bestand stimmt nicht mit den Originalen überein.")
            pdf = folder / "gesamt-pdf" / f"{folder.name}_gesamt.pdf"
            target = destination / pdf.name
            shutil.copyfile(pdf, target)
            assets.extend([native, separate, target])
            report["cases"].append({"slug": folder.name, "originals": len(native_paths), "individual_pdfs": len(expected), "overall_pages": len(PdfReader(pdf).pages), "formats": sorted({p.suffix.lower() for p in native_paths}), "native_files_byte_identical": True})
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(assets)}
    report["assets"] = hashes
    report_file = ROOT / "quality/bauwirtschaft-rundum/pakete.json"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (destination / "checksums-sha256.txt").write_text("".join(f"{digest}  {name}\n" for name, digest in hashes.items()), encoding="utf-8")
    print(json.dumps({"plugins": len(report["plugins"]), "cases": len(report["cases"]), "assets": len(assets), "destination": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    build(args.destination)
