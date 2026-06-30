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

from testakte_einzelpdf_common import expected_arcnames

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

RELEASE_BASE = (
    "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"
)


def section_block(slug: str, pdf_rel: str | None, size_kb: int | None, has_einzelpdf: bool = False) -> str:
    zip_url = f"{RELEASE_BASE}/testakte-{slug}.zip"
    einzel_url = f"{RELEASE_BASE}/testakte-{slug}-einzelpdfs.zip"
    einzel_row = (
        f"\n| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-{slug}-einzelpdfs.zip]({einzel_url}) |"
        if has_einzelpdf
        else ""
    )
    einzel_intro = (
        " Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden."
        if has_einzelpdf
        else ""
    )
    if pdf_rel is not None and size_kb is not None:
        rows = (
            f"| Gesamt-PDF (alles in einer Datei, {size_kb} KB) | PDF | [`{pdf_rel}`]({pdf_rel}) |\n"
            f"| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-{slug}.zip]({zip_url}) |"
            f"{einzel_row}"
        )
        intro = (
            "Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen."
            + einzel_intro
        )
        trailer = "Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten."
    else:
        rows = (
            f"| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-{slug}.zip]({zip_url}) |"
            f"{einzel_row}"
        )
        intro = (
            "Dieses Aktenpaket gibt es als Akten-ZIP zum Direkt-Download. Es enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen."
            + einzel_intro
        )
        trailer = "Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version."
    return f"""{MARKER_BEGIN}
## Akte komplett herunterladen

{intro}

| Was | Format | Quelle |
| --- | --- | --- |
{rows}

{trailer}

{MARKER_END}
"""


H1_RE = re.compile(r"^# .+$", re.MULTILINE)


def inject(readme: Path, slug: str) -> str:
    pdf = readme.parent / "gesamt-pdf" / f"{slug}_gesamt.pdf"
    if pdf.exists():
        size_kb = max(1, round(pdf.stat().st_size / 1024))
        pdf_rel = f"gesamt-pdf/{slug}_gesamt.pdf"
    else:
        size_kb = None
        pdf_rel = None
    has_einzelpdf = bool(expected_arcnames(readme.parent))
    new_section = section_block(slug, pdf_rel, size_kb, has_einzelpdf)
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
        readme.write_text(new_text, encoding="utf-8")
        return "updated"

    # Erstmaliges Einfuegen nach dem ersten H1
    m = H1_RE.search(text)
    if not m:
        # Kein H1 - oben einfuegen
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
    readme.write_text(new_text, encoding="utf-8")
    return "inserted"


def main() -> int:
    if not TESTAKTEN_DIR.exists():
        print(f"Testakten-Verzeichnis nicht gefunden: {TESTAKTEN_DIR}", file=sys.stderr)
        return 1
    stats = {"inserted": 0, "updated": 0, "unchanged": 0, "skip": 0}
    for sub in sorted(TESTAKTEN_DIR.iterdir()):
        if not sub.is_dir():
            continue
        if sub.name in SKIP_DIRS:
            stats["skip"] += 1
            continue
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
        result = inject(readme, sub.name)
        key = result.split()[0] if result.startswith("skip") else result
        if key not in stats:
            key = "skip"
        stats[key] += 1
        print(f"  {result.upper():<9} {sub.name}")
    print(
        f"\nFertig: {stats['inserted']} neu, {stats['updated']} aktualisiert, "
        f"{stats['unchanged']} unveraendert, {stats['skip']} uebersprungen"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
