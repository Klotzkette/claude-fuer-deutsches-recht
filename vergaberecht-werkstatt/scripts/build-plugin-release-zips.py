#!/usr/bin/env python3
"""Baut die drei Marketplace-Plugin-ZIPs reproduzierbar und flach."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path, PurePosixPath

from reproducible_zip import tree_members, write_archive


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"


def excluded(relative: PurePosixPath) -> bool:
    return (
        relative.name == ".DS_Store"
        or "__pycache__" in relative.parts
        or relative.suffix == ".pyc"
        or relative.as_posix() == "CLAUDE.md"
        or (len(relative.parts) == 1 and relative.name.endswith(("-werkstatt.md", "-schnellstart.md")))
        or relative.name == "llm-judge-eval.py"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", nargs="?", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        parser.error("marketplace.json enthaelt keine Plugins")

    for plugin in plugins:
        name = plugin.get("name")
        source_value = plugin.get("source")
        if not isinstance(name, str) or not isinstance(source_value, str):
            parser.error("Marketplace-Eintrag ohne name/source")
        source = (ROOT / source_value).resolve()
        if source.parent != ROOT or source.name != name or not source.is_dir():
            parser.error(f"{name}: ungueltiger Plugin-Pfad {source_value!r}")
        members = tree_members(source, exclude=excluded)
        members += [(ROOT / filename, filename) for filename in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE")]
        count = write_archive(output_dir / f"{name}.zip", members)
        if count == 0:
            parser.error(f"{name}: leeres Plugin")
        print(f"{name}.zip: {count} Dateien")

    shutil.copyfile(MARKETPLACE, output_dir / "marketplace.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
