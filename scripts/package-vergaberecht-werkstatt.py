#!/usr/bin/env python3
"""Baut und prüft das getrennte Vergaberecht-Komponentenrelease."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "vergaberecht-werkstatt"


def archive(path, pairs, *, notice=False):
    names = set()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as output:
        if notice:
            item = zipfile.ZipInfo(NOTICE_FILENAME, (2020, 1, 1, 0, 0, 0))
            output.writestr(item, NOTICE_BYTES + b"\n")
            names.add(NOTICE_FILENAME.casefold())
        for source, name in sorted(pairs, key=lambda pair: pair[1]):
            if source.is_symlink() or name.casefold() in names:
                raise ValueError(f"Symlink oder Namenskollision: {source}")
            names.add(name.casefold())
            item = zipfile.ZipInfo(name, (2020, 1, 1, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            with source.open("rb") as src, output.open(item, "w") as dst:
                shutil.copyfileobj(src, dst)


def run(script, *args):
    subprocess.run([sys.executable, str(COMPONENT / "scripts" / script), *map(str, args)],
                   cwd=COMPONENT, check=True, timeout=600)


def build(destination):
    destination = destination.resolve()
    if destination == COMPONENT or COMPONENT in destination.parents:
        raise ValueError("Ausgaben müssen außerhalb der Komponentenkopie liegen.")
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError("Für einen vollständigen, unvermischt prüfbaren Build ein leeres Ziel wählen.")
    meta = json.loads((COMPONENT / "source-import.json").read_text())
    run("build-plugin-release-zips.py", destination)
    run("validate-release-zips.py", destination)
    run("build-testakten-release-zips.py", destination)
    run("validate-testakten-release-zips.py", destination)
    run("build-skills-markdown-bundles.py", destination)
    for name in meta["plugins"]:
        for kind in ("werkstatt", "schnellstart"):
            path = COMPONENT / name / f"{name}-{kind}.md"
            shutil.copyfile(path, destination / path.name)
        shutil.copyfile(COMPONENT / "unified-mini-prompts" / f"{name}.md",
                        destination / f"{name}-unified-mini-prompt.md")
    for path in sorted(COMPONENT.glob("vergaberecht-*prompt-*.md")):
        shutil.copyfile(path, destination / path.name)
    for slug in meta["cases"]:
        path = COMPONENT / "testakten" / slug / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        shutil.copyfile(path, destination / path.name)
    archive(destination / "alle-plugins-megazip.zip",
            [(destination / f"{name}.zip", f"{name}.zip") for name in meta["plugins"]])
    # Nur versionierte und nicht ignorierte Quelldateien, keine Git-Daten oder Build-Reste.
    listing = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "vergaberecht-werkstatt"],
        cwd=ROOT,
    ).decode().split("\0")
    pairs = [(ROOT / relative, relative) for relative in sorted(set(listing)) if relative]
    archive(destination / "alles-komplettpaket.zip", pairs, notice=True)
    shutil.copyfile(COMPONENT / "source-import.json", destination / "source-import.json")
    run("validate-release-zips.py", destination)
    subprocess.run([sys.executable, str(ROOT / "scripts/test-vergaberecht-import.py"),
                    "--dist", str(destination)], cwd=ROOT, check=True, timeout=300)
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(destination.iterdir()) if p.is_file()}
    (destination / "checksums-sha256.txt").write_text(
        "".join(f"{digest}  {name}\n" for name, digest in hashes.items()), encoding="utf-8")
    print(json.dumps({"release": meta["release"], "assets": len(hashes) + 1,
                      "destination": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    build(parser.parse_args().destination)
