#!/usr/bin/env python3
"""Fuegt in jede testakten/<name>/README.md prominent ganz oben eine
Akte-komplett-Sektion ein mit zwei Downloads:

1. Gesamt-PDF (im Repo unter gesamt-pdf/<slug>_gesamt.pdf eingecheckt)
2. Akten-ZIP mit allen Einzeldateien (aus dem GitHub-Release,
   stabile URL releases/latest/download/testakte-<slug>.zip).

Idempotent ueber HTML-Marker. Position: direkt nach dem H1, vor allen
weiteren Sektionen (insbesondere vor dem Direkt-Download-Block).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from public_release import RAW_BASE, RELEASE_BASE
from testakte_notices import with_case_warnings

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN_DIR = REPO_ROOT / "testakten"

SKIP_DIRS = {
    "formatvorlagen-paradebeispiele",
    "megaprompts",
}

# Hinweis: Die Marker heißen weiterhin "gesamt-pdf-section", damit bestehende
# READMEs idempotent aktualisiert werden. Der Inhalt der Sektion umfasst aber
# inzwischen sowohl das Gesamt-PDF als auch die Akten-ZIP.
MARKER_BEGIN = "<!-- BEGIN gesamt-pdf-section (autogen) -->"
MARKER_END = "<!-- END gesamt-pdf-section (autogen) -->"



def section_block(
    slug: str,
    pdf_rel: str | None,
    size_kb: int | None,
    previous_slug: str | None,
    next_slug: str | None,
) -> str:
    zip_url = f"{RELEASE_BASE}/testakte-{slug}.zip"
    nav = [
        "[Repo-Start](../../README.md)",
        "[Dateikatalog](../../README.md#dateikatalog)",
        "[Downloads](../../README.md#sofort-downloads)",
        "[Testakten-Übersicht](../README.md)",
        f"[Alle Testakten als ZIP]({RELEASE_BASE}/testakten-vergaberecht-werkstatt.zip)",
    ]
    if previous_slug:
        nav.append(f"[Vorherige Akte](../{previous_slug}/README.md)")
    if next_slug:
        nav.append(f"[Nächste Akte](../{next_slug}/README.md)")
    nav_line = " | ".join(nav)
    if pdf_rel is not None and size_kb is not None:
        pdf_raw = f"{RAW_BASE}/testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf"
        rows = (
            f"| Gesamt-PDF (alles in einer Datei, {size_kb} KB) | [Im Browser öffnen]({pdf_rel}) | "
            f"[`{slug}_gesamt.pdf`]({pdf_raw}) |\n"
            f"| Akten-ZIP (alle Einzeldateien) | [Dateiliste](./) | "
            f"[`testakte-{slug}.zip`]({zip_url}) |"
        )
        rows += (
            f"\n| Einzel-PDF-ZIP | [PDF-Dateien](einzel-pdf/) | "
            f"[`testakte-{slug}-einzelpdfs.zip`]({RELEASE_BASE}/testakte-{slug}-einzelpdfs.zip) |"
            f"\n| Gesamt-PDF als Release-Datei | [Gesamt-PDF]({pdf_rel}) | "
            f"[`{slug}_gesamt.pdf`]({RELEASE_BASE}/{slug}_gesamt.pdf) |"
        )
        intro = (
            "Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. "
            "Das flache Akten-ZIP enthält ohne Unterordner ausschließlich bearbeitbare "
            "Word-/Excel-Dateien sowie Einzel-, Scan- und Original-PDFs; das Gesamt-PDF wird separat angeboten."
        )
        trailer = "Die ZIP-URL ist an den Komponentenstand gebunden. Außer README.txt mit dem Warnhinweis enthält das Arbeits-ZIP keine Textnotizen, Markdown-Quellen oder internen Bewertungsraster."
    else:
        rows = (
            f"| Akten-ZIP (alle Einzeldateien) | [Dateiliste](./) | "
            f"[`testakte-{slug}.zip`]({zip_url}) |"
        )
        intro = (
            "Diese Arbeitsakte gibt es als flaches Akten-ZIP zum Direkt-Download. Es enthält ohne Unterordner ausschließlich DOCX, XLSX und PDF."
        )
        trailer = "Die ZIP-URL ist an den Komponentenstand gebunden. README.txt enthält den Warnhinweis."
    return with_case_warnings(f"""{MARKER_BEGIN}
{nav_line}

## Akte komplett herunterladen

{intro}

| Inhalt | Ansehen | Herunterladen |
| --- | --- | --- |
{rows}

{trailer}

{MARKER_END}
""")


H1_RE = re.compile(r"^# .+$", re.MULTILINE)


def inject(
    readme: Path,
    slug: str,
    previous_slug: str | None,
    next_slug: str | None,
) -> str:
    pdf = readme.parent / "gesamt-pdf" / f"{slug}_gesamt.pdf"
    if pdf.exists():
        size_kb = max(1, round(pdf.stat().st_size / 1024))
        pdf_rel = f"gesamt-pdf/{slug}_gesamt.pdf"
    else:
        size_kb = None
        pdf_rel = None
    new_section = section_block(slug, pdf_rel, size_kb, previous_slug, next_slug)
    text = readme.read_text(encoding="utf-8")

    # Falls bereits eingefuegt: ersetzen
    pat = re.compile(
        re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n?",
        re.DOTALL,
    )
    if pat.search(text):
        new_text = pat.sub(new_section, text, count=1)
        if new_text == text:
            return "unchanged"
        readme.write_text(with_case_warnings(new_text), encoding="utf-8")
        return "updated"

    # Erstmaliges Einfuegen nach dem ersten H1
    m = H1_RE.search(text)
    if not m:
        # Kein H1 - oben einfügen
        new_text = new_section + "\n" + text
    else:
        end = m.end()
        # Falls nach H1 noch eine Leerzeile, dahinter setzen
        rest = text[end:]
        # konsumiere genau eine Leerzeile, falls vorhanden
        if rest.startswith("\n\n"):
            insert_at = end + 2
        elif rest.startswith("\n"):
            insert_at = end + 1
        else:
            insert_at = end
        new_text = text[:insert_at] + "\n" + new_section + "\n" + text[insert_at:]
    readme.write_text(with_case_warnings(new_text), encoding="utf-8")
    return "inserted"


def main() -> int:
    if not TESTAKTEN_DIR.exists():
        print(f"Testakten-Verzeichnis nicht gefunden: {TESTAKTEN_DIR}", file=sys.stderr)
        return 1
    stats = {"inserted": 0, "updated": 0, "unchanged": 0, "skip": 0}
    subdirs = [
        sub
        for sub in sorted(TESTAKTEN_DIR.iterdir())
        if sub.is_dir() and sub.name not in SKIP_DIRS
    ]
    stats["skip"] += sum(
        1
        for sub in TESTAKTEN_DIR.iterdir()
        if sub.is_dir() and sub.name in SKIP_DIRS
    )
    for index, sub in enumerate(subdirs):
        readme = sub / "README.md"
        if not readme.exists():
            # Fallback: erstes 00_*.md oder aktenuebersicht*.md
            candidates = sorted(sub.glob("00_*.md")) + sorted(sub.glob("aktenuebersicht*.md"))
            if candidates:
                readme = candidates[0]
            else:
                print(f"  SKIP  {sub.name}: keine README.md / 00_*.md")
                stats["skip"] += 1
                continue
        previous_slug = subdirs[index - 1].name if index > 0 else None
        next_slug = subdirs[index + 1].name if index + 1 < len(subdirs) else None
        result = inject(readme, sub.name, previous_slug, next_slug)
        key = result.split()[0] if result.startswith("skip") else result
        if key not in stats:
            key = "skip"
        stats[key] += 1
        print(f"  {result.upper():<9} {sub.name}")
    print(
        f"\nFertig: {stats['inserted']} neu, {stats['updated']} aktualisiert, "
        f"{stats['unchanged']} unverändert, {stats['skip']} übersprungen"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
