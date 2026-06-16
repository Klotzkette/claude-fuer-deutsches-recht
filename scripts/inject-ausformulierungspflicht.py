#!/usr/bin/env python3
"""Fuegt in jeden SKILL.md, der ein Endprodukt erzeugt, am Ende des
'## Ausgabeformat'-Blocks einen Hinweis auf die in CLAUDE.md verankerte
Ausformulierungspflicht ein. Idempotent ueber HTML-Marker.

Heuristik fuer 'erzeugt ein Endprodukt':
- Skill-Slug oder description enthaelt mindestens eines der Endprodukt-Woerter
  (Vertrag, Vorlage, Klage, Antrag, Schriftsatz, Memo, Bescheid, Anschreiben,
  Mandantenbrief, Vermerk, Stellungnahme, Vereinbarung, NDA, AGB, Kündigung,
  Einspruch, Widerspruch, Gutachten, erstellen, entwerf, formulieren, generator).
- UND der Skill hat einen '## Ausgabeformat'-Block (sonst kein klarer Anker).

Nicht angefasst: testakten/megaprompts/* (Perplexity arbeitet parallel daran).
"""
from __future__ import annotations
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

MARKER_BEGIN = "<!-- BEGIN ausformulierungspflicht (autogen) -->"
MARKER_END = "<!-- END ausformulierungspflicht (autogen) -->"

ENDPRODUKT_RE = re.compile(
    r"(vertrag|vorlage|klage|antrag|schriftsatz|memo|bescheid|anschreiben|"
    r"mandantenbrief|vermerk|stellungnahme|vereinbarung|nda|agb|kuendigung|"
    r"kündigung|einspruch|widerspruch|gutachten|erstell|entwerf|entwurf|"
    r"formulier|generator|aufsetz)",
    re.IGNORECASE,
)

# Heading-Pattern fuer Ausgabeformat-Block
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.MULTILINE)
AUSGABE_RE = re.compile(r"^#{2,6}\s+(Ausgabe|Endprodukt|Output)", re.IGNORECASE)


BLOCK = f"""{MARKER_BEGIN}
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
{MARKER_END}"""


def find_ausgabe_section_end(text: str) -> int | None:
    """Liefert Position direkt nach dem '## Ausgabeformat'-Block."""
    lines = text.split("\n")
    in_block = False
    block_level = 0
    block_start_line = -1
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            if not in_block and AUSGABE_RE.match(line):
                in_block = True
                block_level = level
                block_start_line = i
                continue
            if in_block and level <= block_level:
                # neue Sektion auf gleicher oder hoeherer Ebene -> Block-Ende
                return sum(len(ln) + 1 for ln in lines[:i])
    if in_block:
        # Block reicht bis Dateiende
        return len(text)
    return None


def has_endprodukt_signal(slug: str, description: str) -> bool:
    if ENDPRODUKT_RE.search(slug):
        return True
    if ENDPRODUKT_RE.search(description):
        return True
    return False


def extract_description(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    fm = parts[1]
    m = re.search(r"description:\s*\"?([^\"\n]+)", fm)
    return m.group(1) if m else ""


def process_skill(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return "skip-read"

    if MARKER_BEGIN in text:
        return "already"

    slug = path.parent.name
    desc = extract_description(text)
    if not has_endprodukt_signal(slug, desc):
        return "not-endprodukt"

    insert_at = find_ausgabe_section_end(text)
    if insert_at is None:
        return "no-ausgabe-section"

    # Block einfuegen mit Leerzeilen
    before = text[:insert_at].rstrip()
    after = text[insert_at:]
    new = before + "\n\n" + BLOCK + "\n\n" + after.lstrip()
    path.write_text(new, encoding="utf-8")
    return "added"


SKIP_PARTS = {".git", "node_modules", "__pycache__", "testakten", "docs",
               "scripts", "anlagen-zu-schriftsaetzen-archiv"}


def main() -> None:
    added = already = not_endprodukt = no_section = errors = 0
    for skill_md in REPO.rglob("SKILL.md"):
        if any(part in SKIP_PARTS for part in skill_md.parts):
            continue
        result = process_skill(skill_md)
        if result == "added":
            added += 1
        elif result == "already":
            already += 1
        elif result == "not-endprodukt":
            not_endprodukt += 1
        elif result == "no-ausgabe-section":
            no_section += 1
        else:
            errors += 1

    print(f"added={added} already={already} not-endprodukt={not_endprodukt} "
          f"no-ausgabe-section={no_section} errors={errors}")


if __name__ == "__main__":
    main()
