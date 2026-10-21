#!/usr/bin/env python3
"""Baut getrennte EU- und US-Plugins, Begleitprompts und vier Aktenpakete."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ("eu-sanktionspruefer", "us-sanktionspruefer")
VERSION = "1.0.0"
STAMP = (2026, 10, 21, 8, 0, 0)


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    cases = json.loads((ROOT / "scripts/data/sanktionen-akten.json").read_text(encoding="utf-8"))
    if len(cases) != 4 or len({case["slug"] for case in cases}) != 4:
        raise ValueError("Vier verschiedene Akten erforderlich")
    dist.mkdir(parents=True, exist_ok=True)
    for name in PLUGINS:
        plugin = ROOT / name
        manifests = [plugin / p for p in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
        values = [json.loads(p.read_text(encoding="utf-8")) for p in manifests]
        if len({(v["name"], v["version"], v["description"]) for v in values}) != 1:
            raise ValueError("Manifeste widersprechen sich")
        if (values[0]["name"], values[0]["version"]) != (name, VERSION):
            raise ValueError("Falscher Komponentenstand")
        skills = sorted((plugin / "skills").glob("*/SKILL.md"))
        if len(skills) != 10:
            raise ValueError("Genau zehn Skills je Plugin erforderlich")
        paths = manifests + [plugin / "README.md"] + skills
        paths += sorted(p for p in (plugin / "references").rglob("*") if p.is_file())
        if any(p.is_symlink() or not p.is_file() for p in paths):
            raise ValueError("Fehlende Datei oder Symlink im Paket")
        for portable in (False, True):
            prefix = name + "/" if portable else ""
            with zipfile.ZipFile(dist / f"{name}{'-portable' if portable else ''}.zip", "w") as archive:
                for path in paths + [ROOT / "LICENSE"]:
                    relative = path.relative_to(plugin).as_posix() if path != ROOT / "LICENSE" else "LICENSE"
                    info = zipfile.ZipInfo(prefix + relative, STAMP)
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, path.read_bytes())
        for kind in ("werkstatt", "schnellstart", "hauptproblem"):
            path = plugin / f"{name}-{kind}.md"
            shutil.copyfile(path, dist / path.name)
        for path in skills:
            shutil.copyfile(path, dist / f"{name}-{path.parent.name}.md")
        own = [case for case in cases if case["plugin"] == name]
        if len(own) != 2:
            raise ValueError("Zwei Akten je Plugin erforderlich")
        for case in own:
            slug = case["slug"]
            pdf = ROOT / "testakten" / slug / "gesamt-pdf" / f"{slug}_gesamt.pdf"
            shutil.copyfile(pdf, dist / pdf.name)
            for suffix in ("", "-einzelpdfs"):
                asset = f"testakte-{slug}{suffix}.zip"
                shutil.copyfile(plugin / "downloads" / asset, dist / asset)
    files = sorted(dist.iterdir())
    if len(files) != 42:
        raise ValueError("Releaseumfang weicht ab")
    (dist / "checksums-sha256.txt").write_text("".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in files), encoding="utf-8")
    print(f"Sanktionsprüfung {VERSION}: 43 geprüfte Release-Dateien in {dist}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    build(parser.parse_args().dist)
