#!/usr/bin/env python3
"""Validiert die Release-Artefakte fuer pluginlokale testakte-Ordner."""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"


def fail(message: str) -> None:
    print(f"validate-plugin-testakte-assets failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def check_pdf(path: Path) -> None:
    if not path.is_file():
        fail(f"{path.relative_to(REPO)} fehlt")
    data = path.read_bytes()
    if len(data) < 1024 or not data.startswith(b"%PDF") or b"%%EOF" not in data[-4096:]:
        fail(f"{path.relative_to(REPO)} ist kein plausibles PDF")


def check_zip(path: Path) -> None:
    if not path.is_file() or path.stat().st_size <= 0:
        fail(f"{path}: ZIP fehlt oder ist leer")
    try:
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                fail(f"{path}: defekter ZIP-Eintrag {bad}")
            if not [n for n in archive.namelist() if not n.endswith("/")]:
                fail(f"{path}: ZIP ohne Dateien")
    except zipfile.BadZipFile as exc:
        fail(f"{path}: kein gueltiges ZIP: {exc}")


def main() -> int:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "dist"
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    count = 0
    for plugin in plugins:
        name = plugin["name"]
        directory = plugin_dir(plugin)
        testakte = directory / "testakte"
        if not testakte.is_dir():
            continue
        count += 1
        check_pdf(testakte / "gesamt-pdf" / "testakte_gesamt.pdf")
        check_zip(dist / f"{name}-testakte.zip")
        check_zip(dist / f"{name}-testakte-einzelpdfs.zip")
    check_zip(dist / "alle-pluginlokalen-testakten.zip")
    check_zip(dist / "alle-pluginlokalen-testakten-einzelpdfs.zip")
    print(f"validate-plugin-testakte-assets OK ({count} pluginlokale Testakten)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
