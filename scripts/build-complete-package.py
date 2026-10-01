#!/usr/bin/env python3
"""Baut das vollständige Downloadpaket ohne doppelte Sammelarchive.

Die bereits validierten Sammelarchive sind das verbindliche Inventar. Ihre
Einzel-ZIPs werden unverändert einmal übernommen; die Sammelarchive selbst
bleiben eigene Release-Downloads. --root erlaubt eine Wiederherstellung mit
gesicherten Release-Artefakten und den Übersichten des ursprünglichen Tags.
"""
from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from pathlib import Path

from release_asset_common import check_asset_size
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_NAME = "alles-komplettpaket.zip"
BUNDLES = {
    "alle-plugins-megazip.zip": "plugins",
    "alle-skills-markdown.zip": "skills-markdown",
    "alle-testakten.zip": "testakten",
    "alle-testakten-einzelpdfs.zip": "testakten",
    "alle-pluginlokalen-testakten.zip": "testakten",
    "alle-pluginlokalen-testakten-einzelpdfs.zip": "testakten",
}
OVERVIEWS = ("README.md", "SKILLS.md", "ASSET_INDEX.md", "SCHWERPUNKTE.md", "QUALITY.md", "CHANGELOG.md")
PACKAGE_README = NOTICE_BYTES + """
KOMPLETTPAKET / INHALT
=====================

plugins/          Installierbare Plugin-Einzelpakete.
skills-markdown/   Skill-Markdown-Einzelpakete je Plugin.
testakten/        Alle zentralen und pluginlokalen Testakten, jeweils als
                  Originalformat-ZIP und als Einzel-PDF-ZIP.
marketplace.json  Marketplace für diese Veröffentlichung.
uebersichten/     Zentrale Übersichten, Qualitätsunterlagen und Skill-Index.

Jedes Einzelpaket ist genau einmal enthalten, mit unverändertem Inhalt.
Die sechs Sammel-ZIPs (alle-*.zip) bleiben als eigenständige Release-Downloads
verfügbar. Sie werden hier nicht zusätzlich eingebettet: Ihr gesamter Inhalt
liegt bereits in den obigen Ordnern; so bleiben die Dateien innerhalb der
GitHub-Größengrenze. Diese README enthält auch den gemeinsamen Aktenhinweis.
Werkstatt- und Schnellstart-Prompts bleiben separate Markdown-Direktdownloads.
""".encode("utf-8")


def zip_info(name: str, *, archive: bool = False) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_STORED if archive else zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def collect_entries(dist: Path, root: Path) -> tuple[list[tuple[Path, str, str]], list[tuple[Path, str]]]:
    """Verweigert unbekannten Zusatzinhalt statt ihn stillschweigend wegzulassen."""
    marketplace = (dist / "marketplace.json").read_bytes()
    if marketplace != (root / ".claude-plugin/marketplace.json").read_bytes():
        raise ValueError("Marketplace weicht vom Quellstand ab; --root muss zum Release-Tag passen")
    plugins = [item["name"] for item in json.loads(marketplace)["plugins"]]
    if not plugins or len(plugins) != len(set(plugins)):
        raise ValueError("Marketplace enthält keine oder doppelte Plugins")
    entries: list[tuple[Path, str, str]] = []
    seen: set[str] = set()
    for bundle_name, destination in BUNDLES.items():
        path = dist / bundle_name
        with zipfile.ZipFile(path) as bundle:
            members = [info for info in bundle.infolist() if not info.is_dir()]
            names = [info.filename for info in members]
            if len(names) != len(set(names)):
                raise ValueError(f"{bundle_name}: doppelte ZIP-Einträge")
            expected_metadata = "marketplace.json" if destination == "plugins" else (
                NOTICE_FILENAME if destination == "testakten" else None
            )
            if expected_metadata:
                expected = marketplace if destination == "plugins" else NOTICE_BYTES
                if bundle.read(expected_metadata) != expected:
                    raise ValueError(f"{bundle_name}: abweichende {expected_metadata}")
            archives = set()
            for info in members:
                name = info.filename
                if name == expected_metadata:
                    continue
                if "/" in name or "\\" in name or not name.endswith(".zip") or name in BUNDLES:
                    raise ValueError(f"{bundle_name}: unerwarteter Inhalt {name!r}")
                arcname = f"{destination}/{name}"
                if arcname in seen:
                    raise ValueError(f"Doppeltes Einzelpaket: {arcname}")
                seen.add(arcname)
                archives.add(name)
                entries.append((path, name, arcname))
            if destination == "plugins" and archives != {f"{name}.zip" for name in plugins}:
                raise ValueError("Plugin-Sammelarchiv und Marketplace stimmen nicht überein")
            if destination == "skills-markdown" and archives != {f"{name}-skills-markdown.zip" for name in plugins}:
                raise ValueError("Skill-Sammelarchiv und Marketplace stimmen nicht überein")
    files = [(dist / "marketplace.json", "marketplace.json")]
    files.extend((root / name, f"uebersichten/{name}") for name in OVERVIEWS)
    for folder in ("quality", "skills-index"):
        directory = root / folder
        if not directory.is_dir():
            raise ValueError(f"Fehlende Übersicht: {directory}")
        files.extend((path, f"uebersichten/{path.relative_to(root).as_posix()}")
                     for path in sorted(directory.rglob("*"))
                     if path.is_file() and path.name != ".DS_Store")
    for path, _ in files:
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Fehlende oder verlinkte Quelldatei: {path}")
    return entries, files


def build(dist: Path, root: Path = ROOT) -> Path:
    entries, files = collect_entries(dist, root)
    output = dist / OUTPUT_NAME
    temporary = output.with_name(f".{output.name}.tmp")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as target:
            target.writestr(zip_info(NOTICE_FILENAME), PACKAGE_README)
            for path, arcname in files:
                with path.open("rb") as source, target.open(zip_info(arcname), "w") as sink:
                    shutil.copyfileobj(source, sink, length=1024 * 1024)
            # Je Sammelarchiv nur einmal öffnen; auch große Einzelpakete streamen.
            for bundle_name in BUNDLES:
                with zipfile.ZipFile(dist / bundle_name) as bundle:
                    for path, name, arcname in entries:
                        if path.name != bundle_name:
                            continue
                        with bundle.open(name) as source, target.open(zip_info(arcname, archive=True), "w") as sink:
                            shutil.copyfileobj(source, sink, length=1024 * 1024)
        check_asset_size(temporary)
        temporary.replace(output)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        output = build(args.dist.resolve(), args.root.resolve())
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as error:
        parser.error(str(error))
    print(f"{output.name}: {output.stat().st_size:,} Bytes; Einzelpakete ohne Sammelarchiv-Doppelkopien")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
