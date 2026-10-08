#!/usr/bin/env python3
"""Verschiebt den Megaprompt-Block vor den automatisch erzeugten Skill-Katalog.

Block-Marker:
    <!-- BEGIN megaprompt-und-vorlagen (autogen) -->
    ...
    <!-- END megaprompt-und-vorlagen (autogen) -->

Der historische Dateiname bleibt erhalten, damit bestehende lokale Abläufe
nicht brechen. Die einheitliche Position vermeidet, dass der Prompt bei einem
Plugin erst nach einer sehr langen Dateiliste erscheint.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BEGIN = "<!-- BEGIN megaprompt-und-vorlagen (autogen) -->"
END = "<!-- END megaprompt-und-vorlagen (autogen) -->"
SKILLS_BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"

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
    if SKILLS_BEGIN not in text:
        return False
    block = m.group(0).strip("\n")
    remainder = text[: m.start()] + text[m.end():]
    before, after = remainder.split(SKILLS_BEGIN, 1)
    new_text = (
        before.rstrip()
        + "\n\n"
        + block
        + "\n\n"
        + SKILLS_BEGIN
        + after
    )
    if not new_text.endswith("\n"):
        new_text += "\n"
    if new_text == text:
        return False
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
