#!/usr/bin/env python3
"""Struktur, unveränderte Ursprünge, Dokumentzuordnung und Release-Inhalt prüfen."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "gvb-reinigungsvergabe"
PROJECT = ROOT / "weitere-unterlagen/sektorenvergabe-gvb-berlin"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(dist=None):
    baseline = json.loads((PLUGIN / "references/ursprung.json").read_text())
    mappings = baseline["workflows"]
    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    require(len(skills) == len(mappings) == 10, "Zehn Skills und zehn Ursprungsassistenten erforderlich")
    require(len({row["skill"] for row in mappings}) == 10, "Doppelte Zuordnung")
    require(not list(PROJECT.rglob("SKILL.md")), "Separates Projekt wurde zum Plugin umgebaut")
    require(not list(PROJECT.rglob("plugin.json")), "Manifest im separaten Projekt")
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    entries = [p for p in marketplace["plugins"] if p["name"] == PLUGIN.name]
    require(len(entries) == 1 and entries[0]["source"] == "./" + PLUGIN.name, "Marketplace-Eintrag fehlt oder doppelt")
    require(not any(baseline["project"] in str(p.get("source")) for p in marketplace["plugins"]),
            "Separates Projekt darf nicht registriert werden")
    for row in mappings:
        source = PROJECT / "workflows" / row["datei"]
        require(hashlib.sha256(source.read_bytes()).hexdigest() == row["sha256"],
                f"Ursprünglicher Assistent verändert: {source.name}")
        skill = PLUGIN / "skills" / row["skill"] / "SKILL.md"
        text = skill.read_text()
        require(len(text) > 7000, f"Fachlicher Inhalt fehlt: {skill}")
        for number in range(1, 7):
            require(re.search(rf"^## {number}\. ", text, re.M), f"Abschnitt {number} fehlt: {skill}")
        for value in ("RUECKFRAGE", "WEITER:", "FREIGABE:", "EuGH", "SektVO", "Times New Roman", "vollständigen"):
            require(value in text, f"Arbeitsregel fehlt: {skill}/{value}")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if not target.startswith(("https://", "http://", "#")):
                require((skill.parent / target).is_file(), f"Tote Referenz: {skill}/{target}")
    mini = (PLUGIN / f"{PLUGIN.name}-schnellstart.md").read_text()
    require(max(len(mini), len(mini.encode()), len(mini.replace("\n", "\r\n"))) <= 7500,
            "Mini-Prompt überschreitet Grenze")
    require(len((PLUGIN / f"{PLUGIN.name}-werkstatt.md").read_bytes()) > 25000, "Werkstatt nicht ausgearbeitet")
    for readme in (PLUGIN / "README.md", PROJECT / "README.md"):
        text = readme.read_text()
        require("48" in text and "51" in text, "Veralteter Aktenumfang")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if not target.startswith(("https://", "http://", "#")):
                require((readme.parent / target.split("#", 1)[0]).exists(), f"Toter README-Link: {target}")
    subprocess.run([sys.executable, str(PROJECT / "pruefen.py")], check=True, cwd=ROOT)
    if dist:
        spec = importlib.util.spec_from_file_location("builder", ROOT / "scripts/build-gvb-reinigungsvergabe-release.py")
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        expected = {f"{PLUGIN.name}.zip", f"{PLUGIN.name}-portable.zip", "checksums-sha256.txt"}
        expected.update(builder.PROMPTS + builder.CASE_FILES)
        expected.update(f"{PLUGIN.name}-{p.parent.name}.md" for p in skills)
        require({p.name for p in dist.iterdir()} == expected, "Release-Dateien fehlen oder sind unerwartet")
        for portable in (False, True):
            prefix = f"{PLUGIN.name}/" if portable else ""
            with zipfile.ZipFile(dist / f"{PLUGIN.name}{'-portable' if portable else ''}.zip") as archive:
                require(archive.testzip() is None, "Defektes Plugin-ZIP")
                require(len([n for n in archive.namelist() if n.endswith("/SKILL.md")]) == 10, "Skillanzahl im Paket")
                require(not any(n.endswith(tuple(builder.PROMPTS)) for n in archive.namelist()), "Zusatzprompt im Plugin")
                require(not any(n.endswith((".pdf", ".eml", ".docx", ".csv", ".zip")) for n in archive.namelist()),
                        "Akteninhalt im Plugin")
                for name in archive.namelist():
                    relative = name.removeprefix(prefix)
                    path = ROOT / "LICENSE" if relative == "LICENSE" else PLUGIN / relative
                    require(path.is_file() and archive.read(name) == path.read_bytes(), f"Paket weicht ab: {name}")
        for name in builder.CASE_FILES:
            require((dist / name).read_bytes() == (PROJECT / "downloads" / name).read_bytes(), "Veraltete Release-Akte")
        for path in skills:
            require((dist / f"{PLUGIN.name}-{path.parent.name}.md").read_bytes() == path.read_bytes(), "Skilldownload weicht ab")
        for name in builder.PROMPTS:
            require((dist / name).read_bytes() == (PLUGIN / name).read_bytes(), "Promptdownload weicht ab")
        for line in (dist / "checksums-sha256.txt").read_text().splitlines():
            digest, name = line.split("  ", 1)
            require(hashlib.sha256((dist / name).read_bytes()).hexdigest() == digest, "Falsche Release-Prüfsumme")
    print("OK: zehn neue Skills; zehn unveränderte Originalassistenten; getrennte Downloads und Verknüpfungen.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path)
    check(parser.parse_args().dist)
