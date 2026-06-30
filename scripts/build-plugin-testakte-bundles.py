#!/usr/bin/env python3
"""Baut Release-ZIPs fuer pluginlokale testakte-Ordner.

Zentrale Testakten unter testakten/ werden von build-testakten-release-zips.py
verpackt. Dieses Skript ergaenzt die Plugin-Faelle, in denen die Demonstrationsakte
direkt im Pluginordner unter testakte/ liegt, etwa bei den Gerichtsplugins.
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

from testakte_file_filter import include_in_working_dump


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def list_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def add_dir(zf: zipfile.ZipFile, base: Path, arc_prefix: str) -> None:
    for path in sorted(base.rglob("*")):
        if not include_in_working_dump(path, base, include_gesamt_pdf=True):
            continue
        zf.write(path, arcname=f"{arc_prefix}/{path.relative_to(base).as_posix()}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: build-plugin-testakte-bundles.py <output-dir>", file=sys.stderr)
        return 2
    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    built: list[tuple[str, Path]] = []
    for plugin in list_plugins():
        name = plugin["name"]
        directory = plugin_dir(plugin)
        testakte = directory / "testakte"
        if not testakte.is_dir():
            continue
        zip_path = out_dir / f"{name}-testakte.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            add_dir(zf, testakte, "testakte")
        built.append((name, zip_path))

    combined = out_dir / "alle-pluginlokalen-testakten.zip"
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, zip_path in built:
            zf.write(zip_path, arcname=zip_path.name)

    print(f"Pluginlokale Testakten-Bundles gebaut: {len(built)} Plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
