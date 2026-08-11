#!/usr/bin/env python3
"""Baut Release-ZIPs fuer pluginlokale testakte-Ordner.

Zentrale Testakten unter testakten/ werden von build-testakten-release-zips.py
verpackt. Dieses Skript ergaenzt die Plugin-Faelle, in denen die Demonstrationsakte
direkt im Pluginordner unter testakte/ liegt, etwa bei den Gerichtsplugins.
"""

from __future__ import annotations

import json
import shutil
import sys
import zipfile
from pathlib import Path

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_zip_common import working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def list_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def write_file(zf: zipfile.ZipFile, path: Path, arcname: str) -> None:
    info = zipfile.ZipInfo(arcname, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    with path.open("rb") as source, zf.open(info, "w") as target:
        shutil.copyfileobj(source, target, length=1024 * 1024)


def write_bytes(zf: zipfile.ZipFile, data: bytes, arcname: str) -> None:
    info = zipfile.ZipInfo(arcname, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zf.writestr(info, data)


def add_dir(zf: zipfile.ZipFile, base: Path) -> None:
    write_bytes(zf, NOTICE_BYTES, NOTICE_FILENAME)
    for path, arcname in working_dump_flat_pairs(base, include_gesamt_pdf=True):
        write_file(zf, path, arcname)


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
        if not working_dump_flat_pairs(testakte, include_gesamt_pdf=False):
            zip_path.unlink(missing_ok=True)
            continue
        temporary = zip_path.with_name(f".{zip_path.name}.tmp")
        try:
            with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as zf:
                add_dir(zf, testakte)
            temporary.replace(zip_path)
        except Exception:
            temporary.unlink(missing_ok=True)
            raise
        built.append((name, zip_path))

    combined = out_dir / "alle-pluginlokalen-testakten.zip"
    combined_tmp = combined.with_name(f".{combined.name}.tmp")
    try:
        with zipfile.ZipFile(combined_tmp, "w", zipfile.ZIP_DEFLATED) as zf:
            for name, zip_path in built:
                write_file(zf, zip_path, zip_path.name)
        combined_tmp.replace(combined)
    except Exception:
        combined_tmp.unlink(missing_ok=True)
        raise

    print(f"Pluginlokale Testakten-Bundles gebaut: {len(built)} Plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
