#!/usr/bin/env python3
"""Baut Gesamt-PDFs fuer pluginlokale testakte-Ordner.

Zentrale Akten unter testakten/ haben ihren eigenen Builder. Dieses Skript
ergänzt die wenigen Pluginordner mit eingebetteter Akte, damit auch dort neben
dem Rohdaten-ZIP ein lesbares Gesamt-PDF vorhanden ist.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
SCRIPTS = REPO / "scripts"


def _load_gesamt_module():
    path = SCRIPTS / "build-testakte-gesamt-pdf.py"
    spec = importlib.util.spec_from_file_location("build_testakte_gesamt_pdf", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


G = _load_gesamt_module()


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def main() -> int:
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    counts = {"ok": 0, "skip": 0, "error": 0}
    for plugin in plugins:
        testakte = plugin_dir(plugin) / "testakte"
        if not testakte.is_dir():
            continue
        status, info = G.build_gesamt_pdf(testakte)
        counts[status] += 1
        sigil = {"ok": "OK ", "skip": "SK ", "error": "ERR"}[status]
        print(f"  {sigil} {plugin['name']}: {info}")
    print(f"Pluginlokale Gesamt-PDFs: {counts['ok']} OK, {counts['skip']} skip, {counts['error']} Fehler")
    return 1 if counts["error"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
