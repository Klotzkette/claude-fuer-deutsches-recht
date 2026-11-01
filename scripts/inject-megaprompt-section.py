#!/usr/bin/env python3
"""Kompatibilitaetsskript fuer alte Megaprompt-README-Bloecke.

Die README-Fuehrung liegt inzwischen bei `inject-direkt-loslegen-section.py`.
Dieses Skript entfernt nur noch alte `megaprompt-und-vorlagen`-Bloecke, damit
ein alter Generatorlauf keine veralteten Mega-/Mini-Hinweise zurueckbringt.
"""

from __future__ import annotations


if __name__ == "__main__":
    from generator_cli import parse_generator_cli

    parse_generator_cli(__doc__)

import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
BEGIN = "<!-- BEGIN megaprompt-und-vorlagen (autogen) -->"
END = "<!-- END megaprompt-und-vorlagen (autogen) -->"


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def process(readme: Path) -> str:
    if not readme.is_file():
        return "SKIPPED"
    text = readme.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        return "UNCHANGED"
    new_text = re.sub(
        r"\n*" + re.escape(BEGIN) + r"[\s\S]*?" + re.escape(END) + r"\n*",
        "\n",
        text,
        count=1,
    )
    readme.write_text(new_text, encoding="utf-8")
    return "UPDATED"


def main() -> int:
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    counts = {"UPDATED": 0, "UNCHANGED": 0, "SKIPPED": 0}
    for plugin in plugins:
        status = process(plugin_dir(plugin) / "README.md")
        counts[status] += 1
    print(
        f"Megaprompt-Altbloecke: {counts['UPDATED']} entfernt, "
        f"{counts['UNCHANGED']} unveraendert, {counts['SKIPPED']} uebersprungen"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
