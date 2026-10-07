#!/usr/bin/env python3
"""Fuegt in jeden SKILL.md, der ein Endprodukt erzeugt, am Ende des
'## Ausgabeformat'-Blocks einen Hinweis auf die in CLAUDE.md verankerte
Ausformulierungspflicht und den Formatstandard ein. Idempotent ueber
HTML-Marker. Der Blocktext kommt aus hausstil.formatblock; jedes Markerpaar
in jeder Markdown-Datei des Repositorys (auch in References) wird auf diesen
Text gehoben, damit es nur eine Fassung des Blocks gibt. Neu eingefuegt wird
er nur in SKILL.md.

Heuristik fuer 'erzeugt ein Endprodukt':
- Skill-Slug oder description enthaelt mindestens eines der Endprodukt-Woerter
  (Vertrag, Vorlage, Klage, Antrag, Schriftsatz, Memo, Bescheid, Anschreiben,
  Mandantenbrief, Vermerk, Stellungnahme, Vereinbarung, NDA, AGB, Kündigung,
  Einspruch, Widerspruch, Gutachten, erstellen, entwerf, formulieren, generator).
- UND der Skill hat einen '## Ausgabeformat'-Block (sonst kein klarer Anker).

Nicht angefasst: testakten/megaprompts/* (generate-megaprompt.py baut sie aus den
SKILL.md neu) und CHANGELOG.md (Historie wird nicht umgeschrieben).
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hausstil as hs  # noqa: E402

REPO = Path(__file__).resolve().parent.parent

MARKER_BEGIN = hs.MARKER_BEGIN
MARKER_END = hs.MARKER_END
MARKERBLOCK_RE = re.compile(re.escape(MARKER_BEGIN) + r"[\s\S]*?" + re.escape(MARKER_END))

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


BLOCK = hs.formatblock(hs.lade_hausstil())


def find_ausgabe_section_end(text: str) -> int | None:
    """Liefert Position direkt nach dem '## Ausgabeformat'-Block.

    Wichtig: niemals innerhalb eines noch offenen fenced code blocks
    einfuegen. Markdown-Headings (#) gelten nur ausserhalb eines
    fenced code blocks; innerhalb eines ``` ... ``` Blocks sind Zeilen
    mit '#' literaler Inhalt und keine Section-Trenner. Wir tracken
    deshalb den Fence-Zustand und liefern bei einem noch offenen Fence
    die Position **vor** dem oeffnenden Fence statt nach der letzten
    Template-Zeile zurueck.
    """
    lines = text.split("\n")
    in_block = False
    block_level = 0
    in_fence = False
    fence_open_line = -1  # Zeilennummer des oeffnenden Fences im Ausgabeformat-Block
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        # Fence-Toggle: Zeile beginnt mit ``` (ggf. mit Sprache)
        if stripped.startswith("```"):
            if in_block and not in_fence:
                fence_open_line = i
            in_fence = not in_fence
            continue
        if in_fence:
            # Innerhalb fenced code: '#' ist literal, kein Heading
            continue
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            if not in_block and AUSGABE_RE.match(line):
                in_block = True
                block_level = level
                continue
            if in_block and level <= block_level:
                # neue Sektion auf gleicher oder hoeherer Ebene -> Block-Ende
                return sum(len(ln) + 1 for ln in lines[:i])
    if in_block:
        if in_fence and fence_open_line >= 0:
            # Datei endet mitten in einem fenced code block. Marker MUSS
            # vor das oeffnende Fence, sonst landet er als Template-Inhalt.
            return sum(len(ln) + 1 for ln in lines[:fence_open_line])
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


def process_markdown(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return "skip-read"

    if MARKER_BEGIN in text and MARKER_END in text:
        # Jedes Markerpaar der Datei, auch mehrere (References mit vielen Abschnitten).
        new_text = MARKERBLOCK_RE.sub(lambda _treffer: BLOCK, text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            return "updated"
        return "already"

    if path.name != "SKILL.md":
        return "no-marker"

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
               "scripts", "anlagen-zu-schriftsaetzen-archiv", "mutants", "venv", ".venv"}
SKIP_FILES = {"CHANGELOG.md"}


def main() -> None:
    added = updated = already = not_endprodukt = no_section = errors = 0
    for markdown in REPO.rglob("*.md"):
        relativ = markdown.relative_to(REPO)
        if any(part in SKIP_PARTS for part in relativ.parts) or str(relativ) in SKIP_FILES:
            continue
        result = process_markdown(markdown)
        if result == "no-marker":
            continue
        if result == "added":
            added += 1
        elif result == "updated":
            updated += 1
        elif result == "already":
            already += 1
        elif result == "not-endprodukt":
            not_endprodukt += 1
        elif result == "no-ausgabe-section":
            no_section += 1
        else:
            errors += 1

    print(f"added={added} updated={updated} already={already} not-endprodukt={not_endprodukt} "
          f"no-ausgabe-section={no_section} errors={errors}")


if __name__ == "__main__":
    main()
