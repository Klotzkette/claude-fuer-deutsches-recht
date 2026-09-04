#!/usr/bin/env python3
"""Fuegt in jede testakten/<name>/README.md prominent ganz oben eine
Akte-komplett-Sektion mit drei getrennten Downloadfassungen ein:

1. Gesamt-PDF (im Repo unter gesamt-pdf/<slug>_gesamt.pdf eingecheckt)
2. Akten-ZIP mit flachen nativen Originaldateien ohne Markdown.
3. Einzel-PDF-ZIP mit flach abgelegten, getrennten PDFs.

Idempotent ueber HTML-Marker. Position: direkt nach dem H1, vor allen
weiteren Sektionen (insbesondere vor dem Direkt-Download-Block).

Ohne Argumente werden alle Akten bearbeitet. Optional koennen konkrete
Testakten-Namen angegeben werden, um nur deren Downloadsektionen zu erneuern.
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


def section_block(slug: str, pdf_rel: str | None, has_einzelpdf: bool = False) -> str:
    zip_url = f"{RELEASE_BASE}/testakte-{slug}.zip"
    einzel_url = f"{RELEASE_BASE}/testakte-{slug}-einzelpdfs.zip"
    einzel_row = (
        f"\n| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-{slug}-einzelpdfs.zip]({einzel_url}) |"
        if has_einzelpdf
        else ""
    )
    einzel_intro = (
        " Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene."
        if has_einzelpdf
        else ""
    )
    if pdf_rel is not None:
        rows = (
            f"| Gesamt-PDF (alles in einer Datei) | PDF | [`{pdf_rel}`]({pdf_rel}) |\n"
            f"| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-{slug}.zip]({zip_url}) |"
            f"{einzel_row}"
        )
        formats = "drei" if has_einzelpdf else "zwei"
        intro = (
            f"Dieses Aktenpaket gibt es in {formats} Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene."
            + einzel_intro
        )
        trailer = "Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein."
    else:
        rows = (
            f"| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-{slug}.zip]({zip_url}) |"
            f"{einzel_row}"
        )
        intro = (
            "Dieses Aktenpaket gibt es als Akten-ZIP zum Direkt-Download. Es enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs, aber kein Markdown. Sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene."
            + einzel_intro
        )
        trailer = "Die ZIP-Links laden den zuletzt veröffentlichten Release. Der Repository-Stand kann zwischen Releases bereits neuer sein."
    english = "English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown."
    if pdf_rel is not None:
        english += " Choose the combined PDF for reading; it is also included in that ZIP."
    if has_einzelpdf:
        english += " Choose the individual-PDF ZIP to review each document separately."
    english += " These are practice documents, not an installable plugin. ZIP links refer to the latest published release."
    return f"""{MARKER_BEGIN}
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

{intro}

| Was | Format | Quelle |
| --- | --- | --- |
{rows}

{trailer}

{english}

{MARKER_END}
"""


H1_RE = re.compile(r"^# .+$", re.MULTILINE)


def normalize_marker_spacing(text: str) -> str:
    return re.sub(
        r"(^# .+\n)\n+(?=" + re.escape(MARKER_BEGIN) + r")",
        r"\1\n",
        text,
        count=1,
        flags=re.MULTILINE,
    )


def inject(readme: Path, slug: str) -> str:
    pdf = readme.parent / "gesamt-pdf" / f"{slug}_gesamt.pdf"
    if pdf.exists():
        pdf_rel = f"gesamt-pdf/{slug}_gesamt.pdf"
    else:
        pdf_rel = None
    has_einzelpdf = bool(expected_arcnames(readme.parent))
    new_section = section_block(slug, pdf_rel, has_einzelpdf)
    text = readme.read_text(encoding="utf-8")

    # Falls bereits eingefuegt: ersetzen
    pat = re.compile(
        re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n?",
        re.DOTALL,
    )
    if pat.search(text):
        new_text = normalize_marker_spacing(pat.sub(new_section, text, count=1))
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
    new_text = normalize_marker_spacing(new_text)
    readme.write_text(new_text, encoding="utf-8")
    return "inserted"


def main() -> int:
    if not TESTAKTEN_DIR.exists():
        print(f"Testakten-Verzeichnis nicht gefunden: {TESTAKTEN_DIR}", file=sys.stderr)
        return 1
    targets = set(sys.argv[1:])
    known = {sub.name for sub in TESTAKTEN_DIR.iterdir() if sub.is_dir()}
    unknown = sorted(targets - known)
    if unknown:
        print(f"Unbekannte Testakten: {unknown}", file=sys.stderr)
        return 1
    stats = {"inserted": 0, "updated": 0, "unchanged": 0, "skip": 0}
    for sub in sorted(TESTAKTEN_DIR.iterdir()):
        if not sub.is_dir():
            continue
        if targets and sub.name not in targets:
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
