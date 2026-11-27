#!/usr/bin/env python3
"""Prüft die Insolvenz-Plugins und stellt die Fachbereichspakete aus ihren belegten Quellen her."""

import argparse
from copy import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from urllib.request import Request, urlopen
from zipfile import ZIP_STORED, ZipFile

from package_readme import render_readme
from release_routing import RELEASE_BASE
from testakte_zip_common import safe_archive_name
from werkstatt_edition import previous as before_workshops

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "Fachbereiche/Insolvenzrecht"
RELEASE_TAG = "insolvenz-fachbereich-v445.36.10"


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def inventory():
    entries = json.loads((DIRECTORY / "pakete.json").read_text(encoding="utf-8"))
    readme = (DIRECTORY / "README.md").read_text(encoding="utf-8")
    links = re.findall(r"\]\(([a-z0-9-]+)\.zip(?:\?raw=true)?\)", readme)
    if not entries or sorted(links) != sorted(entries):
        raise ValueError("Paketverzeichnis und ZIP-Links der Fachbereichsseite stimmen nicht überein.")
    plugins = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))["plugins"]
    catalog = {plugin["name"]: plugin for plugin in plugins}
    for name, item in entries.items():
        if (name not in catalog or item["version"] != catalog[name]["version"]
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                or not re.fullmatch(r"[a-z0-9]+[a-z0-9.-]*", item["tag"])
                or not re.fullmatch(r"[a-f0-9]{64}", item["sha256"])
                or not re.fullmatch(r"[a-f0-9]{64}", item["quelle_sha256"])):
            raise ValueError(f"Paketnachweis oder Marketplace-Version ungültig: {name}")
    return entries, {name: ROOT / catalog[name]["source"] for name in entries}


def readmes(directory, names):
    # Die Dokumentations-ZIPs gehören zur fest veröffentlichten Ausgabe 445.36.10.
    def release_source(readme):
        return before_workshops(ROOT, readme.relative_to(ROOT).as_posix(),
                                readme.read_bytes(), plugin=directory.name)

    return {name: render_readme(ROOT, directory, names, None, name=name,
                                release_tag=RELEASE_TAG, read_source=release_source)
            for name in names if PurePosixPath(name).name == "README.md"}


def assemble(original, destination, item, source):
    if digest(original) != item["quelle_sha256"]:
        raise ValueError(f"SHA-256 der veröffentlichten Quelle weicht ab: {original.name}")
    if not item["readme_aus_quellbaum"]:
        shutil.copyfile(original, destination)
        return
    with ZipFile(original) as before:
        texts = readmes(source, before.namelist())
        # ZIP_STORED macht den Nachbau unabhängig von der eingesetzten zlib-Version.
        with ZipFile(destination, "w") as after:
            after.comment = before.comment
            for member in before.infolist():
                data = texts[member.filename] if member.filename in texts else before.read(member)
                after.writestr(copy(member), data, compress_type=ZIP_STORED)
        with ZipFile(destination) as after:
            if (after.namelist() != before.namelist() or after.comment != before.comment
                    or any(after.read(n) != before.read(n) for n in before.namelist() if n not in texts)):
                raise ValueError(f"Fachdateien der Dokumentationsfassung weichen ab: {original.name}")


def verify(directory, entries, sources):
    if {p.name for p in directory.glob("*.zip")} != {name + ".zip" for name in entries}:
        raise ValueError(f"ZIP-Bestand stimmt nicht mit dem Paketverzeichnis überein: {directory}")
    for name, item in entries.items():
        path = directory / f"{name}.zip"
        if path.is_symlink() or not path.is_file() or digest(path) != item["sha256"]:
            raise ValueError(f"Datei oder SHA-256 der Fachbereichsfassung weicht ab: {name}")
        with ZipFile(path) as archive:
            names = archive.namelist()
            if (len(names) != len({n.casefold() for n in names})
                    or any(not safe_archive_name(i.filename.rstrip("/"), allow_directories=True)
                           or stat.S_ISLNK(i.external_attr >> 16) for i in archive.infolist())
                    or ".claude-plugin/plugin.json" not in names or "README.md" not in names
                    or not any(re.fullmatch(r"skills/[^/]+/SKILL\.md", n) for n in names)):
                raise ValueError(f"Paket hat keine installierbare Pluginstruktur: {name}")
            manifest = json.loads(archive.read(".claude-plugin/plugin.json"))
            if manifest.get("name") != name or manifest.get("version") != item["version"]:
                raise ValueError(f"Plugin-Manifest weicht ab: {name}")
            if item["readme_aus_quellbaum"]:
                for filename, content in readmes(sources[name], names).items():
                    if archive.read(filename) != content:
                        raise ValueError(f"README weicht von der ausgelieferten Dokumentation ab: {name}/{filename}")

    subprocess.run([sys.executable, str(ROOT / "scripts/build-insolvenz-fachpakete.py"),
                    "--verify", "--dist", str(directory)], check=True)


def download(destination, cache, entries, sources):
    if destination.exists() or destination.is_symlink():
        raise ValueError(f"Für den Nachbau einen neuen Zielordner angeben: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as temp:
        output = Path(temp) / "Pakete"
        output.mkdir()
        for name, item in entries.items():
            filename = f"{name}.zip"
            if cache:
                original = cache / filename
            else:
                original = Path(temp) / filename
                url = f"{RELEASE_BASE}/download/{item['tag']}/{filename}"
                request = Request(url, headers={"User-Agent": "Fachbereich-Insolvenzrecht"})
                with urlopen(request, timeout=60) as response, original.open("wb") as target:
                    shutil.copyfileobj(response, target)
            assemble(original, output / filename, item, sources[name])
        verify(output, entries, sources)
        output.rename(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", type=Path, metavar="AUSGABEORDNER",
                        help="ZIPs aus dem ausgecheckten Stand und den zugeordneten Releases nachbauen.")
    parser.add_argument("--quellen", type=Path, metavar="ORDNER",
                        help="Für den Nachbau lokal archivierte Original-ZIPs verwenden.")
    args = parser.parse_args()
    if args.quellen and not args.download:
        parser.error("--quellen erfordert --download mit einem neuen Ausgabeordner")
    entries, sources = inventory()
    if args.download:
        download(args.download.absolute(), args.quellen, entries, sources)
    else:
        verify(DIRECTORY, entries, sources)
    print(f"{len(entries)} installierbare Pakete anhand von Prüfsummen und Pluginstruktur bestätigt.")


if __name__ == "__main__":
    main()
