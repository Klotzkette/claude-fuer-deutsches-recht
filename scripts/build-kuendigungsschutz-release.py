#!/usr/bin/env python3
"""Baut das Kündigungsschutzpaket und seine getrennten Begleitdateien."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "arbeitsrecht-kuendigungsschutzklagewerkstatt"
VERSION = "1.0.0"
STAMP = (2026, 10, 22, 12, 0, 0)


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    plugin = ROOT / NAME
    manifest_paths = [plugin / value for value in (
        "plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    manifests = [json.loads(path.read_text(encoding="utf-8")) for path in manifest_paths]
    identities = {(value["name"], value["version"], value["description"]) for value in manifests}
    if len(identities) != 1 or (manifests[0]["name"], manifests[0]["version"]) != (NAME, VERSION):
        raise ValueError("Manifeste sind nicht synchron")
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    if len(skills) != 11:
        raise ValueError("Zehn Fachskills und ein Hauptskill erforderlich")
    cases = json.loads((ROOT / "scripts/data/kuendigungsschutz-akten.json").read_text(encoding="utf-8"))
    if len(cases) != 3 or len({case["slug"] for case in cases}) != 3:
        raise ValueError("Drei verschiedene Akten erforderlich")
    package_paths = manifest_paths + [plugin / "README.md", plugin / "CHANGELOG.md"] + skills
    package_paths += sorted(path for path in (plugin / "references").rglob("*") if path.is_file())
    if any(path.is_symlink() or not path.is_file() for path in package_paths):
        raise ValueError("Fehlende Datei oder Symlink im Paket")
    dist.mkdir(parents=True, exist_ok=True)
    for portable in (False, True):
        prefix = NAME + "/" if portable else ""
        archive_path = dist / (NAME + ("-portable" if portable else "") + ".zip")
        with zipfile.ZipFile(archive_path, "w") as archive:
            for path in package_paths + [ROOT / "LICENSE"]:
                relative = "LICENSE" if path == ROOT / "LICENSE" else path.relative_to(plugin).as_posix()
                info = zipfile.ZipInfo(prefix + relative, STAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
    for kind in ("werkstatt", "schnellstart", "hauptproblem"):
        path = plugin / (NAME + "-" + kind + ".md")
        shutil.copyfile(path, dist / path.name)
    for path in skills:
        shutil.copyfile(path, dist / (NAME + "-" + path.parent.name + ".md"))
    for case in cases:
        slug = case["slug"]
        pdf = ROOT / "testakten" / slug / "gesamt-pdf" / (slug + "_gesamt.pdf")
        shutil.copyfile(pdf, dist / pdf.name)
        for suffix in ("", "-einzelpdfs"):
            filename = "testakte-" + slug + suffix + ".zip"
            shutil.copyfile(plugin / "testakte/downloads" / filename, dist / filename)
    paths = sorted(dist.iterdir())
    if len(paths) != 25:
        raise ValueError("Abweichender Releaseumfang")
    (dist / "checksums-sha256.txt").write_text("".join(
        hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name + "\n"
        for path in paths), encoding="utf-8")
    print(f"Kündigungsschutzwerkstatt {VERSION}: 26 geprüfte Release-Dateien in {dist}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    build(parser.parse_args().dist)
