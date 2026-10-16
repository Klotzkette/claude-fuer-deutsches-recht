#!/usr/bin/env python3
"""Packt Untersuchungshaft, Zusatzprompts und vier Akten getrennt."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "untersuchungshaft"
VERSION = "1.1.0"
PROMPTS = [f"{NAME}-{kind}.md" for kind in ("werkstatt", "schnellstart")]


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    plugin = ROOT / NAME
    manifests = [json.loads((plugin / p).read_text()) for p in
                 ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    if len({(m["name"], m["version"], m["description"]) for m in manifests}) != 1:
        raise ValueError("Manifeste weichen ab")
    if manifests[0]["name"] != NAME or manifests[0]["version"] != VERSION:
        raise ValueError("Falsche Komponente")
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    if len(skills) != 10:
        raise ValueError("Genau zehn Skills erforderlich")
    paths = [plugin / p for p in ("README.md", "plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    paths += sorted(p for folder in ("skills", "references") for p in (plugin / folder).rglob("*") if p.is_file())
    if any(p.is_symlink() for p in paths):
        raise ValueError("Symlinks im Paket")
    dist.mkdir(parents=True, exist_ok=True)
    for portable in (False, True):
        prefix = NAME + "/" if portable else ""
        with zipfile.ZipFile(dist / f"{NAME}{'-portable' if portable else ''}.zip", "w") as archive:
            for path in paths + [ROOT / "LICENSE"]:
                relative = path.relative_to(plugin).as_posix() if path != ROOT / "LICENSE" else "LICENSE"
                info = zipfile.ZipInfo(prefix + relative, (2026, 10, 16, 8, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
    for name in PROMPTS:
        shutil.copyfile(plugin / name, dist / name)
    for path in skills:
        shutil.copyfile(path, dist / f"{NAME}-{path.parent.name}.md")
    cases = json.loads((ROOT / "scripts/data/untersuchungshaft-akten.json").read_text())
    for case in cases:
        slug = case["slug"]
        pdf = ROOT / "testakten" / slug / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        shutil.copyfile(pdf, dist / pdf.name)
        for suffix in ("", "-einzelpdfs"):
            name = f"testakte-{slug}{suffix}.zip"
            shutil.copyfile(plugin / "testakte/downloads" / name, dist / name)
    files = sorted(dist.iterdir())
    if len(files) != 26:
        raise ValueError("Unvollständiger Releaseumfang")
    (dist / "checksums-sha256.txt").write_text("".join(
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in files), encoding="utf-8")
    print(f"Untersuchungshaft {VERSION}: 27 Release-Dateien in {dist}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    build(parser.parse_args().dist)
