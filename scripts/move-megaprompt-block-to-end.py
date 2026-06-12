#!/usr/bin/env python3
"""Verschiebt den autogenerierten Megaprompt-/Vorlagen-Block in den
Plugin-READMEs ans Dateiende.

Block-Marker:
    <!-- BEGIN megaprompt-und-vorlagen (autogen) -->
    ...
    <!-- END megaprompt-und-vorlagen (autogen) -->

Wenn der Block bereits ganz am Ende steht (keine weiteren Inhalts-Zeilen
danach), bleibt die Datei unveraendert.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BEGIN = "<!-- BEGIN megaprompt-und-vorlagen (autogen) -->"
END = "<!-- END megaprompt-und-vorlagen (autogen) -->"

BLOCK_RE = re.compile(
    r"(?s)\n?" + re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?"
)


def process(readme: Path) -> bool:
    text = readme.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        return False
    m = BLOCK_RE.search(text)
    if not m:
        return False
    block = m.group(0).strip("\n")
    remainder = (text[: m.start()] + text[m.end():]).rstrip() + "\n"
    # Bereits am Ende? -> Pruefen, ob nach dem End-Marker substanzieller Text folgt.
    tail_after_block = text[m.end():].strip()
    if not tail_after_block:
        # Block ist schon am Ende. Trotzdem sicherstellen, dass keine
        # nachgelagerten Leerzeilen-Anomalien bestehen.
        return False
    new_text = remainder + "\n" + block + "\n"
    readme.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    changed = 0
    total = 0
    for readme in sorted(ROOT.glob("*/README.md")):
        # Nur Plugin-READMEs (Ordner mit .claude-plugin/plugin.json)
        plugin_json = readme.parent / ".claude-plugin" / "plugin.json"
        if not plugin_json.is_file():
            continue
        total += 1
        if process(readme):
            changed += 1
    print(f"move-megaprompt-block-to-end: {changed}/{total} READMEs aktualisiert")
    return 0


if __name__ == "__main__":
    sys.exit(main())
