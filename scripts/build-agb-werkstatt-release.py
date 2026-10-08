#!/usr/bin/env python3
"""Baut ein abgegrenztes AGB-Komponentenrelease mit drei separaten Mandatsakten."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "agb-werkstatt"
NAME = PLUGIN.name
PROMPTS = [f"{NAME}-{kind}.md" for kind in ("werkstatt", "schnellstart", "hauptproblem")]
CASES = tuple(case["slug"] for case in json.loads((ROOT / "scripts/data/agb-werkstatt-akten.json").read_text())["cases"])


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def build_plugin(dist):
    manifests = [json.loads((PLUGIN / p).read_text()) for p in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    if len({(m["name"], m["version"], m["description"]) for m in manifests}) != 1:
        raise ValueError("Manifeste stimmen nicht überein")
    if manifests[0]["name"] != NAME or manifests[0]["version"] != "1.0.0":
        raise ValueError("Unerwartete Komponente")
    if len(list((PLUGIN / "skills").glob("*/SKILL.md"))) != 11:
        raise ValueError("Genau elf Skills erforderlich")
    for filename in PROMPTS[1:]:
        data = (PLUGIN / filename).read_bytes()
        if len(data) > 7500 or len(data.decode("utf-8")) > 7500:
            raise ValueError("Kompaktprompt ist zu lang")
    files = [p for p in sorted(PLUGIN.rglob("*")) if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name not in PROMPTS]
    if any(p.is_symlink() for p in files):
        raise ValueError("Keine symbolischen Links im Paket")
    dist.mkdir(parents=True, exist_ok=True)
    for portable in (False, True):
        target = dist / f"{NAME}{'-portable' if portable else ''}.zip"
        prefix = f"{NAME}/" if portable else ""
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
            for source in files:
                info = zipfile.ZipInfo(prefix + source.relative_to(PLUGIN).as_posix(), (2026, 10, 9, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, source.read_bytes())
    for name in PROMPTS:
        shutil.copyfile(PLUGIN / name, dist / name)


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    build_plugin(dist)
    originals = module("build-testakten-release-zips.py")
    pdfs = module("build-testakten-einzelpdf-zips.py")
    for slug in CASES:
        directory = ROOT / "testakten" / slug
        source = directory / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        if not source.is_file():
            raise ValueError(f"Gesamt-PDF fehlt: {slug}")
        originals.build_single(directory, dist)
        pdfs.build_single(directory, dist)
        shutil.copyfile(source, dist / source.name)
    expected = {f"{NAME}.zip", f"{NAME}-portable.zip", *PROMPTS}
    expected.update(f"{case}_gesamt.pdf" for case in CASES)
    expected.update(f"testakte-{case}{suffix}.zip" for case in CASES for suffix in ("", "-einzelpdfs"))
    if {p.name for p in dist.iterdir()} != expected:
        raise ValueError("Releaseumfang weicht ab")
    for source in dist.glob("*.zip"):
        with zipfile.ZipFile(source) as archive:
            if archive.testzip() is not None:
                raise ValueError(f"Defektes ZIP: {source.name}")
    sums = "".join(f"{hashlib.sha256((dist / name).read_bytes()).hexdigest()}  {name}\n" for name in sorted(expected))
    (dist / "checksums-sha256.txt").write_text(sums, encoding="utf-8")
    print(json.dumps({"version": "1.0.0", "assets": len(expected) + 1, "destination": str(dist)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    build(parser.parse_args().dist)
