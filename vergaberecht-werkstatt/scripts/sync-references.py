#!/usr/bin/env python3
"""Synchronisiert gemeinsame Referenzen in alle Marketplace-Plugins."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "references"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
REFERENCE_NAMES = (
    "OUTPUT-FORMAT.md",
    "bundeswehrbeschaffung-bwbbg-2026.md",
    "leitentscheidungen-anker.md",
    "methodik-vergaberecht.md",
    "netto-null-technologien-vergabe-2026.md",
    "praxisrechtsprechung-vk-2016-2026.md",
    "quellenhygiene.md",
    "veroeffentlichungswege.md",
    "zitierweise.md",
    "zuschlag-nicht-nur-preis.md",
)
DEPRECATED_REFERENCE_NAMES = (
    "methodik-buergerliches-recht.md",
)


def plugin_paths() -> list[Path]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    paths: list[Path] = []
    for plugin in data.get("plugins", []):
        source = plugin.get("source")
        if not isinstance(source, str):
            raise ValueError("Marketplace-Eintrag ohne source")
        paths.append((ROOT / source).resolve())
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="nur auf Drift prüfen und keine Dateien schreiben",
    )
    args = parser.parse_args()

    try:
        plugins = plugin_paths()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FEHLER: Marketplace kann nicht gelesen werden: {exc}", file=sys.stderr)
        return 1

    sources = [SOURCE_DIR / name for name in REFERENCE_NAMES]
    missing = [source for source in sources if not source.is_file()]
    if missing:
        for source in missing:
            print(f"FEHLER: gemeinsame Referenz fehlt: {source}", file=sys.stderr)
        return 1

    drift: list[str] = []
    changed = 0
    for plugin in plugins:
        if not plugin.is_dir():
            print(f"FEHLER: Plugin-Verzeichnis fehlt: {plugin}", file=sys.stderr)
            return 1
        target_dir = plugin / "references"
        if not args.check:
            target_dir.mkdir(parents=True, exist_ok=True)
        for name in DEPRECATED_REFERENCE_NAMES:
            target = target_dir / name
            if not target.exists():
                continue
            label = str(target.relative_to(ROOT))
            if args.check:
                drift.append(f"veraltete Referenz entfernen: {label}")
            else:
                target.unlink()
                print(f"remove: {label}")
                changed += 1
        for source in sources:
            target = target_dir / source.name
            same = target.exists() and source.read_bytes() == target.read_bytes()
            if same:
                continue
            label = f"{source.relative_to(ROOT)} -> {target.relative_to(ROOT)}"
            if args.check:
                drift.append(label)
            else:
                shutil.copy2(source, target)
                print(f"sync: {label}")
                changed += 1

    if drift:
        for item in drift:
            print(f"FEHLER: Referenzdrift: {item}", file=sys.stderr)
        print(f"sync-references: {len(drift)} Abweichungen", file=sys.stderr)
        return 1

    if args.check:
        print(
            f"sync-references --check OK ({len(sources)} Referenzen, "
            f"{len(plugins)} Plugins)"
        )
    else:
        print(
            f"sync-references OK ({changed} aktualisiert, "
            f"{len(sources)} Referenzen, {len(plugins)} Plugins)"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
