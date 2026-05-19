#!/usr/bin/env python3
"""Validate plugin release ZIPs before publishing them."""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path


def fail(message: str) -> None:
    print(f"validate-release-zips failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def zip_names(zip_path: Path) -> set[str]:
    try:
        with zipfile.ZipFile(zip_path) as archive:
            return {name.replace("\\", "/") for name in archive.namelist()}
    except zipfile.BadZipFile as exc:
        fail(f"{zip_path}: invalid ZIP: {exc}")


# Cowork-/Marketplace-Upload-Limit. Praxiserprobt liegt die Grenze knapp unter 1 MB;
# alles darüber wird vom Server abgelehnt („Plugin validation failed“ ohne Detail).
# Wir setzen daher einen harten Schwellwert von 950 KB.
MAX_ZIP_BYTES = 950 * 1024


def validate_plugin_zip(dist_dir: Path, plugin_name: str) -> None:
    zip_path = dist_dir / f"{plugin_name}.zip"
    if not zip_path.exists():
        fail(f"{zip_path}: missing plugin ZIP")

    size = zip_path.stat().st_size
    if size > MAX_ZIP_BYTES:
        fail(
            f"{zip_path}: {size} bytes überschreitet Cowork-Uploadgrenze ({MAX_ZIP_BYTES} bytes). "
            "Große Binärdateien (z. B. PDFs) entfernen und durch Online-Verweise ersetzen."
        )

    names = zip_names(zip_path)
    if ".claude-plugin/plugin.json" not in names:
        fail(f"{zip_path}: .claude-plugin/plugin.json must be at ZIP root")
    if f"{plugin_name}/.claude-plugin/plugin.json" in names:
        fail(f"{zip_path}: ZIP is nested under {plugin_name}/; upload ZIPs must be flat")
    if any(name.startswith(f"{plugin_name}/") for name in names):
        fail(f"{zip_path}: contains nested {plugin_name}/ root")
    if "CLAUDE.md" in names:
        fail(f"{zip_path}: root CLAUDE.md must not be shipped; Claude Code treats it as a warning and Cowork upload may reject it")
    if any("__pycache__/" in name or name.endswith(".pyc") for name in names):
        fail(f"{zip_path}: contains Python cache files")

    with zipfile.ZipFile(zip_path) as archive:
        manifest = json.loads(archive.read(".claude-plugin/plugin.json"))
    if manifest.get("name") != plugin_name:
        fail(f"{zip_path}: manifest name {manifest.get('name')!r} does not match {plugin_name!r}")

    if plugin_name == "liquiditaetsplanung":
        generator = "skills/liquiditaetsvorschau-3-6-12-monate/werkzeuge/build_liquiditaetsplan.py"
        if generator not in names:
            fail(f"{zip_path}: missing standalone Liquiditätsplan generator {generator}")


def main() -> None:
    dist_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("dist")
    marketplace_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".claude-plugin/marketplace.json")

    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    plugins = [plugin["name"] for plugin in marketplace["plugins"]]
    for plugin_name in plugins:
        validate_plugin_zip(dist_dir, plugin_name)

    marketplace_zip_copy = dist_dir / "marketplace.json"
    if not marketplace_zip_copy.exists():
        fail(f"{marketplace_zip_copy}: missing marketplace.json release asset")
    json.loads(marketplace_zip_copy.read_text(encoding="utf-8"))

    print(f"validate-release-zips OK ({len(plugins)} plugin ZIPs)")


if __name__ == "__main__":
    main()
