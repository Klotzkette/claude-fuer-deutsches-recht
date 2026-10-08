#!/usr/bin/env python3
"""Fuegt in alle SKILL.md, Arbeitsprompts, Kurzprompts,
unified-mini-prompts/*.md und in die Plugin-READMEs einen kurzen,
verbindlichen Output-Format-Block ein.

Skill- und README-Bloecke duerfen auf references/OUTPUT-FORMAT.md
verweisen. Prompt-Bloecke bleiben autark und enthalten die Kernregel direkt
im Prompt-Text, damit sie ohne Repository-Dateien funktionieren.

Idempotent ueber HTML-Marker.
"""
from __future__ import annotations

from pathlib import Path
import re

REPO = Path(__file__).resolve().parent.parent

MARKER_BEGIN = "<!-- BEGIN output-format-block (autogen) -->"
MARKER_END = "<!-- END output-format-block (autogen) -->"

BLOCK_SKILL = """\
{begin}

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

{end}
"""

BLOCK_PROMPT = """\
{begin}

## Output-Format (verbindlich)

Arbeitsprodukte in Times New Roman, 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur kursiv bei Gesetzes- und Aktenzeichenfundstellen. Schriftsätze für VK/OLG mit Zeilenabstand 1,5, sonst 1,15. Anträge dezimal nummerieren. Wertungsmatrix nicht umsortieren; Vorgaben der Plattform, Kammer oder des Gerichts gehen vor.

{end}
"""

BLOCK_README = """\
{begin}

## Output-Format

Alle Skills, Megaprompts und Miniprompts dieses Plugins erzeugen Arbeitsprodukte in Times New Roman, Schriftgrad 11 pt, mit durchgängiger Dezimalgliederung (1, 1.1, 1.1.1, 2, 2.1). Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../references/OUTPUT-FORMAT.md).

{end}
"""

MARKER_RE = re.compile(
    re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END),
    re.DOTALL,
)


def upsert(text: str, block: str, anchor_pattern: re.Pattern | None) -> str:
    """Block einsetzen oder ersetzen.

    anchor_pattern: regex; falls gesetzt und Marker noch nicht vorhanden, wird
    der Block direkt NACH der ersten Anchor-Trefferzeile eingefuegt. Sonst ans
    Ende.
    """
    if MARKER_BEGIN in text and MARKER_END in text:
        return MARKER_RE.sub(block.rstrip(), text)

    if anchor_pattern:
        m = anchor_pattern.search(text)
        if m:
            end = m.end()
            return text[:end] + "\n\n" + block.rstrip() + "\n" + text[end:]

    # Fallback: ans Ende
    sep = "" if text.endswith("\n\n") else ("\n\n" if text.endswith("\n") else "\n\n")
    return text + sep + block.rstrip() + "\n"


def process(path: Path, block_template: str, anchor: re.Pattern | None) -> bool:
    old = path.read_text(encoding="utf-8")
    block = block_template.format(begin=MARKER_BEGIN, end=MARKER_END)
    new = upsert(old, block, anchor)
    if new != old:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0
    scanned = 0

    # Alle SKILL.md in beliebigen Plugins
    h1 = re.compile(r"^# .+$", re.MULTILINE)
    for skill in REPO.rglob("SKILL.md"):
        if ".git" in skill.parts:
            continue
        scanned += 1
        if process(skill, BLOCK_SKILL, h1):
            changed += 1

    # Megaprompts / Miniprompts im Root
    for name in ("vergaberecht-arbeitsprompt-vergabestelle.md", "vergaberecht-arbeitsprompt-bieter.md",
                 "vergaberecht-arbeitsprompt-konkurrenten.md",
                 "vergaberecht-kurzprompt-vergabestelle.md", "vergaberecht-kurzprompt-bieter.md",
                 "vergaberecht-kurzprompt-konkurrenten.md"):
        p = REPO / name
        if p.is_file():
            scanned += 1
            if process(p, BLOCK_PROMPT, h1):
                changed += 1

    # Megaprompts in testakten/megaprompts und konkurrenten-rechtsschutz-Plugin
    testaktenprompts = REPO / "testakten" / "megaprompts"
    if testaktenprompts.is_dir():
        for p in testaktenprompts.glob("*.md"):
            scanned += 1
            if process(p, BLOCK_PROMPT, h1):
                changed += 1

    # Plugin-READMEs (vergabestelle-behoerden/README.md etc.)
    import json
    marketplace = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    for plugin in marketplace.get("plugins", []):
        readme = REPO / plugin["name"] / "README.md"
        if readme.is_file():
            scanned += 1
            if process(readme, BLOCK_README, h1):
                changed += 1

    print(f"Scanned: {scanned}  Changed: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
