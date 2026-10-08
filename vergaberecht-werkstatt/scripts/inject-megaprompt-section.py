#!/usr/bin/env python3
"""Fuegt in jede <plugin>/README.md eine kurze Megaprompt-Hinweissektion ein,
sofern ein passender Megaprompt unter testakten/megaprompts/<plugin>.md
existiert und der Block noch nicht vorhanden ist.

Idempotent ueber HTML-Marker. Position: direkt vor dem automatisch erzeugten
Skill-Katalog, damit Schnellzugriff und Werkstattprompt in allen Plugins vor
der langen Dateiliste stehen.
"""
from __future__ import annotations
import re
from pathlib import Path

from public_release import RAW_BASE

REPO = Path(__file__).resolve().parent.parent
MEGA_DIR = REPO / "testakten" / "megaprompts"

BEGIN = "<!-- BEGIN megaprompt-und-vorlagen (autogen) -->"
END = "<!-- END megaprompt-und-vorlagen (autogen) -->"
SKILLS_BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"

def block_for(plugin: str, kb: int) -> str:
    return f"""{BEGIN}
## Ergänzender Werkstatt-Gesamtprompt

Die regulären Plugin-, Arbeits- und Schnellstartdownloads stehen bereits im Schnellzugriff am Seitenanfang. Zusätzlich liegt der ausführliche Werkstatt-Gesamtprompt als einzeln lesbare Markdown-Datei im Repo.

| Datei | Ansehen | Rohdatei |
| --- | --- | --- |
| Werkstatt-Gesamtprompt ({kb} KB) | [`testakten/megaprompts/{plugin}.md`](../testakten/megaprompts/{plugin}.md) | [Raw .md]({RAW_BASE}/testakten/megaprompts/{plugin}.md) |

{END}
"""


def process(plugin_dir: Path) -> str:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return "skip-no-readme"
    mega = MEGA_DIR / f"{plugin_dir.name}.md"
    if not mega.exists():
        return "skip-no-megaprompt"
    text = readme.read_text(encoding="utf-8")
    kb = max(1, mega.stat().st_size // 1024)
    new_block = block_for(plugin_dir.name, kb)
    had_block = BEGIN in text
    without_block = re.sub(
        r"\n?" + re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?",
        "\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    if SKILLS_BEGIN in without_block:
        before, after = without_block.split(SKILLS_BEGIN, 1)
        new_text = (
            before.rstrip()
            + "\n\n"
            + new_block.rstrip()
            + "\n\n"
            + SKILLS_BEGIN
            + after
        )
    else:
        new_text = without_block.rstrip() + "\n\n" + new_block
    # Keep exactly one terminal newline. Repeated injections must not add an
    # empty line that later trips git diff --check.
    new_text = new_text.rstrip() + "\n"
    if new_text == text:
        return "unchanged"
    readme.write_text(new_text, encoding="utf-8")
    return "updated" if had_block else "added"


def main() -> None:
    added = updated = unchanged = skipped = 0
    for p in sorted(REPO.iterdir()):
        if not p.is_dir():
            continue
        if p.name.startswith(".") or p.name.startswith("_"):
            continue
        if p.name in {"scripts", "testakten", "docs", "audits", "node_modules",
                      "recherche", "references", "skills-index", "tests",
                      "anthropic-lessons", "anlagen-zu-schriftsaetzen-archiv"}:
            continue
        result = process(p)
        if result == "added":
            added += 1
            print(f"  added: {p.name}")
        elif result == "updated":
            updated += 1
        elif result == "unchanged":
            unchanged += 1
        else:
            skipped += 1
    print(f"\nadded={added} updated={updated} unchanged={unchanged} skipped={skipped}")


if __name__ == "__main__":
    main()
