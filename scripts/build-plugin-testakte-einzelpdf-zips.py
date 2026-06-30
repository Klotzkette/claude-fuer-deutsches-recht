#!/usr/bin/env python3
"""Baut Einzel-PDF-ZIPs fuer pluginlokale testakte-Ordner."""

from __future__ import annotations

import importlib.util
import json
import sys
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
SCRIPTS = REPO / "scripts"


def _load_builder_module():
    path = SCRIPTS / "build-testakten-einzelpdf-zips.py"
    spec = importlib.util.spec_from_file_location("build_testakten_einzelpdf_zips", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


B = _load_builder_module()


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: build-plugin-testakte-einzelpdf-zips.py <output-dir>", file=sys.stderr)
        return 2

    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]

    built: list[Path] = []
    for plugin in plugins:
        name = plugin["name"]
        testakte = plugin_dir(plugin) / "testakte"
        if not testakte.is_dir():
            continue
        out = out_dir / f"{name}-testakte-einzelpdfs.zip"
        with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
            count = B.add_testakte(zipf, testakte)
        if count == 0:
            out.unlink(missing_ok=True)
            raise SystemExit(f"{name}: keine renderbaren Unterlagen in testakte/")
        built.append(out)
        print(f"Baue {out.name}: {count} PDFs")

    combined = out_dir / "alle-pluginlokalen-testakten-einzelpdfs.zip"
    with zipfile.ZipFile(combined, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for path in sorted(built, key=lambda p: p.name):
            zipf.write(path, arcname=path.name)
    print(f"Pluginlokale Einzel-PDF-ZIPs gebaut: {len(built)} Plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
