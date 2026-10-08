#!/usr/bin/env python3
"""Baut die Betreuungsrecht-Komponente und die neue Dreijahresakte getrennt."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import zipfile

from prompt_profiles import PROMPT_SUFFIXES

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "betreuungsrecht"
CASE = "betreuung-adelheid-pimpernell-dreijahresabrechnung"


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def build(destination):
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError("Bitte ein leeres Ausgabeziel verwenden.")
    manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
    with zipfile.ZipFile(destination / "betreuungsrecht.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(PLUGIN.rglob("*")):
            if not path.is_file() or path.is_symlink() or "__pycache__" in path.parts:
                continue
            if path.suffix == ".pyc" or path.name in {".DS_Store", "CLAUDE.md"} or path.name.endswith(PROMPT_SUFFIXES):
                continue
            name = path.relative_to(PLUGIN).as_posix()
            item = zipfile.ZipInfo(name, (2026, 10, 8, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            archive.writestr(item, path.read_bytes())
    module("build-testakten-release-zips.py").build_single(ROOT / "testakten" / CASE, destination)
    module("build-testakten-einzelpdf-zips.py").build_single(ROOT / "testakten" / CASE, destination)
    for path in (
        PLUGIN / "betreuungsrecht-unterlagen-werkstatt.md",
        PLUGIN / "betreuungsrecht-unterlagen-werkstatt.txt",
        PLUGIN / "templates/unterlagen-abrechnung.xlsx",
        ROOT / "testakten" / CASE / "gesamt-pdf" / f"{CASE}_gesamt.pdf",
    ):
        shutil.copyfile(path, destination / path.name)
    checksums = "".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in sorted(destination.iterdir()))
    (destination / "checksums-sha256.txt").write_text(checksums, encoding="utf-8")
    print(json.dumps({"version": manifest["version"], "assets": len(list(destination.iterdir())), "destination": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    build(parser.parse_args().destination.resolve())
