#!/usr/bin/env python3
"""Entfernt den Disclaimer- und Verwendungs-Block aus bestehenden Megaprompts.

Erwartetes Eingangsmuster ab Zeile 1:

    # Megaprompt: <slug>

    > *Achtung: ...*
    >
    > *Caution: ...*

    **Verwendung:** ...

    ## Zusammensetzung

Zielzustand:

    # Megaprompt: <slug>

    ## Zusammensetzung
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEGAPROMPTS = ROOT / "testakten" / "megaprompts"


def clean(text: str) -> str:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# Megaprompt:"):
        return text
    # Suche das erste "## Zusammensetzung" und ersetze alles dazwischen
    # durch eine einzelne Leerzeile.
    try:
        idx = next(i for i, ln in enumerate(lines) if ln.startswith("## Zusammensetzung"))
    except StopIteration:
        return text
    # Falls bereits sauber (Zeile 1 leer, Zeile 2 == ## Zusammensetzung), nichts tun.
    if idx == 2 and lines[1] == "":
        return text
    head = [lines[0], ""]
    tail = lines[idx:]
    cleaned = "\n".join(head + tail)
    if text.endswith("\n"):
        cleaned += "\n"
    return cleaned


def main() -> int:
    if not MEGAPROMPTS.is_dir():
        print(f"FEHLER: {MEGAPROMPTS} fehlt", file=sys.stderr)
        return 1
    changed = 0
    total = 0
    for p in sorted(MEGAPROMPTS.glob("*.md")):
        total += 1
        original = p.read_text(encoding="utf-8")
        cleaned = clean(original)
        if cleaned != original:
            p.write_text(cleaned, encoding="utf-8")
            changed += 1
    print(f"cleanup-megaprompt-disclaimers: {changed}/{total} Dateien aktualisiert")
    return 0


if __name__ == "__main__":
    sys.exit(main())
