#!/usr/bin/env python3
"""Baut das GVB-Plugin getrennt von Prompts und der eigenständigen Vergabeakte."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "gvb-reinigungsvergabe"
VERSION = "1.0.0"
PROJECT = ROOT / "weitere-unterlagen/sektorenvergabe-gvb-berlin"
PROMPTS = [f"{NAME}-{kind}.md" for kind in ("werkstatt", "schnellstart")]
CASE_FILES = [f"GVB_Reinigungsvergabe_{suffix}" for suffix in
              ("Gesamt.pdf", "Einzel_PDFs.zip", "Originale.zip")]


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    dist.mkdir(parents=True, exist_ok=True)
    plugin = ROOT / NAME
    manifests = [json.loads((plugin / p).read_text()) for p in
                 ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    if len({(m["name"], m["version"], m["description"]) for m in manifests}) != 1:
        raise ValueError("Manifeste stimmen nicht überein")
    if manifests[0]["version"] != VERSION:
        raise ValueError("Unerwartete Komponentenversion")
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    if len(skills) != 10:
        raise ValueError("Genau zehn Skills erforderlich")
    paths = [plugin / "README.md", plugin / "plugin.json",
             plugin / ".claude-plugin/plugin.json", plugin / ".codex-plugin/plugin.json"]
    paths += sorted(p for directory in ("skills", "references")
                    for p in (plugin / directory).rglob("*") if p.is_file())
    if any(p.is_symlink() or p.suffix in {".pyc", ".zip", ".pdf"} for p in paths):
        raise ValueError("Unerwartete Paketdatei")
    for portable in (False, True):
        prefix = f"{NAME}/" if portable else ""
        with zipfile.ZipFile(dist / f"{NAME}{'-portable' if portable else ''}.zip", "w") as archive:
            for path in paths + [ROOT / "LICENSE"]:
                relative = path.relative_to(plugin).as_posix() if path != ROOT / "LICENSE" else "LICENSE"
                info = zipfile.ZipInfo(prefix + relative, (2026, 10, 10, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
    for name in PROMPTS:
        shutil.copyfile(plugin / name, dist / name)
    for path in skills:
        shutil.copyfile(path, dist / f"{NAME}-{path.parent.name}.md")
    for name in CASE_FILES:
        shutil.copyfile(PROJECT / "downloads" / name, dist / name)
    names = sorted(p.name for p in dist.iterdir())
    if len(names) != 17:
        raise ValueError("Unerwarteter Assetumfang")
    (dist / "checksums-sha256.txt").write_text("".join(
        f"{hashlib.sha256((dist/name).read_bytes()).hexdigest()}  {name}\n" for name in names), encoding="utf-8")
    print(f"{NAME} {VERSION}: 18 getrennt geprüfte Release-Dateien in {dist}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    build(parser.parse_args().dist)
