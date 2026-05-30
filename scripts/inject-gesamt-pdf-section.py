#!/usr/bin/env python3
"""Fuegt in jede testakten/<name>/README.md prominent ganz oben eine
Gesamt-PDF-Sektion ein, die auf gesamt-pdf/<name>_gesamt.pdf verlinkt.

Idempotent ueber HTML-Marker. Position: direkt nach dem H1, vor allen
weiteren Sektionen (insbesondere vor dem Direkt-Download-Block).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN_DIR = REPO_ROOT / "testakten"

MARKER_BEGIN = "<!-- BEGIN gesamt-pdf-section (autogen) -->"
MARKER_END = "<!-- END gesamt-pdf-section (autogen) -->"


def section_block(slug: str, pdf_rel: str, size_kb: int) -> str:
    return f"""{MARKER_BEGIN}
## 📕 Gesamt-PDF (alles in einer Datei)

> **Doppelt gemoppelt:** Diese Akte gibt es als ein einziges, durchsuchbares Gesamt-PDF mit allen Aktenstuecken (Schriftsaetze, Tabellen, Anhaenge) hintereinander – ideal zum Lesen oder Ausdrucken.

| Datei | Format | Groesse |
| --- | --- | --- |
| [`{pdf_rel}`]({pdf_rel}) | PDF | {size_kb} KB |

Im Release-ZIP `testakte-{slug}.zip` ist das Gesamt-PDF mit enthalten.

{MARKER_END}
"""


H1_RE = re.compile(r"^# .+$", re.MULTILINE)


def inject(readme: Path, slug: str) -> str:
    pdf = readme.parent / "gesamt-pdf" / f"{slug}_gesamt.pdf"
    if not pdf.exists():
        return "skip (kein Gesamt-PDF)"
    size_kb = max(1, round(pdf.stat().st_size / 1024))
    pdf_rel = f"gesamt-pdf/{slug}_gesamt.pdf"
    new_section = section_block(slug, pdf_rel, size_kb)
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
