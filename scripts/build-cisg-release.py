#!/usr/bin/env python3
"""Baut das eigenständige CISG-Paket; Arbeitsakten und Begleitprompts bleiben separat."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "un-kaufrecht-cisg"
VERSION = "1.0.0"
STAMP = (2026, 10, 18, 12, 0, 0)


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    plugin = ROOT / NAME
    manifests = [plugin / p for p in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    values = [json.loads(p.read_text(encoding="utf-8")) for p in manifests]
    if len({(v["name"], v["version"], v["description"]) for v in values}) != 1:
        raise ValueError("Manifeste weichen ab")
    if (values[0]["name"], values[0]["version"]) != (NAME, VERSION):
        raise ValueError("Falscher Komponentenstand")
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    if len(skills) != 11:
        raise ValueError("Zehn Fachskills und ein Hauptskill erforderlich")
    cases = json.loads((ROOT / "scripts/data/cisg-akten.json").read_text(encoding="utf-8"))
    if len(cases) != 3 or len({case["slug"] for case in cases}) != 3:
        raise ValueError("Drei unterschiedliche Akten erforderlich")
    paths = manifests + [plugin / "README.md"] + skills
    paths += sorted(p for p in (plugin / "references").rglob("*") if p.is_file())
    if any(p.is_symlink() or not p.is_file() for p in paths):
        raise ValueError("Fehlende Datei oder Symlink im Paket")
    dist.mkdir(parents=True, exist_ok=True)
    for portable in (False, True):
        prefix = NAME + "/" if portable else ""
        with zipfile.ZipFile(dist / f"{NAME}{'-portable' if portable else ''}.zip", "w") as archive:
            for path in paths + [ROOT / "LICENSE"]:
                relative = path.relative_to(plugin).as_posix() if path != ROOT / "LICENSE" else "LICENSE"
                info = zipfile.ZipInfo(prefix + relative, STAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
    for kind in ("werkstatt", "schnellstart", "hauptproblem"):
        path = plugin / f"{NAME}-{kind}.md"
        shutil.copyfile(path, dist / path.name)
    for path in skills:
        shutil.copyfile(path, dist / f"{NAME}-{path.parent.name}.md")
    for case in cases:
        slug = case["slug"]
        pdf = ROOT / "testakten" / slug / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        shutil.copyfile(pdf, dist / pdf.name)
        for suffix in ("", "-einzelpdfs"):
            name = f"testakte-{slug}{suffix}.zip"
            shutil.copyfile(plugin / "testakte/downloads" / name, dist / name)
    files = sorted(dist.iterdir())
    if len(files) != 25:
        raise ValueError("Releaseumfang weicht ab")
    (dist / "checksums-sha256.txt").write_text("".join(
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in files), encoding="utf-8")
    print(f"UN-Kaufrecht {VERSION}: 26 Release-Dateien in {dist}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    build(parser.parse_args().dist)
