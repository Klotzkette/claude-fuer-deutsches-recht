#!/usr/bin/env python3
"""Baut die Geldwäschebeauftragter-Komponente mit drei getrennten Testakten.

Aufruf: python3 scripts/build-geldwaeschebeauftragter-release.py <ausgabeziel>
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import zipfile

from prompt_profiles import PROMPT_SUFFIXES

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "geldwaeschebeauftragter"
VERSION = "445.34.0"
CASES = (
    "aml-unternehmen-werkzeughandel-erfurt",
    "aml-kanzlei-grundstueck-berlin",
    "aml-notariat-kaufpreis-wuerzburg",
)


def module(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace("-", "_"), ROOT / "scripts" / filename
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Builder konnte nicht geladen werden: {filename}")
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def build(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError("Bitte ein leeres Ausgabeziel verwenden.")

    manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if manifest["version"] != VERSION:
        raise ValueError(f"Erwartete Pluginversion: {VERSION}; gefunden: {manifest['version']}")

    copies = [
        PLUGIN / f"geldwaeschebeauftragter-{kind}.{extension}"
        for kind in ("werkstatt", "schnellstart", "hauptproblem")
        for extension in ("md", "txt")
    ]
    copies.extend(
        ROOT / "testakten" / case / "gesamt-pdf" / f"{case}_gesamt.pdf"
        for case in CASES
    )
    copies.extend(
        ROOT / "docs/handbuecher" / name
        for name in (
            "geldwaeschebeauftragter-skills-handbuch.pdf",
            "geldwaeschebeauftragter-werkstatt-lesefassung.pdf",
        )
    )
    for path in copies:
        if not path.is_file() or not path.stat().st_size:
            raise ValueError(f"Releasequelle fehlt oder ist leer: {path.relative_to(ROOT)}")

    originals = module("build-testakten-release-zips.py")
    individual_pdfs = module("build-testakten-einzelpdf-zips.py")
    with zipfile.ZipFile(destination / "geldwaeschebeauftragter.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(PLUGIN.rglob("*")):
            if not path.is_file() or path.is_symlink() or "__pycache__" in path.parts:
                continue
            if path.suffix == ".pyc" or path.name in {".DS_Store", "CLAUDE.md"} or path.name.endswith(PROMPT_SUFFIXES):
                continue
            item = zipfile.ZipInfo(path.relative_to(PLUGIN).as_posix(), (2026, 10, 8, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            archive.writestr(item, path.read_bytes())

    for case in CASES:
        case_directory = ROOT / "testakten" / case
        originals.build_single(case_directory, destination)
        individual_pdfs.build_single(case_directory, destination)
    for path in copies:
        shutil.copyfile(path, destination / path.name)

    expected = {"geldwaeschebeauftragter.zip", *(path.name for path in copies)}
    expected.update(f"testakte-{case}{suffix}.zip" for case in CASES for suffix in ("", "-einzelpdfs"))
    actual = {path.name for path in destination.iterdir() if path.is_file()}
    if actual != expected or len(actual) != 18:
        raise ValueError(f"Unvollständige Release-Assets: {sorted(expected ^ actual)}")
    checksums = "".join(
        f"{hashlib.sha256((destination / name).read_bytes()).hexdigest()}  {name}\n"
        for name in sorted(expected)
    )
    (destination / "checksums-sha256.txt").write_text(checksums, encoding="utf-8")
    print(json.dumps({"version": VERSION, "assets": 19, "destination": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    build(parser.parse_args().destination.resolve())
