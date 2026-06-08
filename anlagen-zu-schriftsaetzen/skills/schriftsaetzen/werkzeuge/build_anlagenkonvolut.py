#!/usr/bin/env python3
"""
build_anlagenkonvolut.py
========================

Baut aus einem Anlagen-Ordner ein beA-fertiges Anlagenkonvolut:

* nimmt PDFs (und nach Vorab-Konvertierung DOCX/JPG/PNG) aus einem
  Eingangsordner,
* sortiert sie nach Anlage-Bezeichnung (K-01, K-02, ..., K-10, ...),
* stempelt auf Seite 1 jeder Anlage oben rechts die Anlagenbezeichnung
  (Arial 12 pt) ein,
* hängt alle Einzel-PDFs zu einem Konvolut zusammen,
* setzt PDF-Lesezeichen je Anlage,
* erzeugt zusätzlich ein Anlagenverzeichnis als Markdown und als PDF.

Aufruf
------

    python3 build_anlagenkonvolut.py \\
        --eingang ./anlagen \\
        --ausgang ./konvolut \\
        --praefix K \\
        --schriftsatz "Klage Edelholz GmbH"

Eingangsordner-Konvention
-------------------------

Erwartet werden PDF-Dateien, deren Dateinamen mit dem Praefix beginnen,
gefolgt von einem Bindestrich und der zweistelligen Anlage-Nummer, z. B.:

    Anlage_K-01_Vertrag-vom-2024-03-15.pdf
    Anlage_K-02_Mahnschreiben-erste-Stufe.pdf
    Anlage_K-03a_Email-Geschaeftsfuehrer.pdf
    Anlage_K-03b_Anhang-Lieferschein.pdf

Andere Dateinamen werden mit Warnung ignoriert.

Abhaengigkeiten
---------------

* pypdf  (>= 4.0)        ->  PDF lesen / mergen / Lesezeichen
* reportlab  (>= 4.0)    ->  Stempel + Anlagenverzeichnis-PDF

Beide sind in der Skill-Toolchain bereits vorausgesetzt.

Lizenz / Verantwortung
----------------------

Letztverantwortung fuer Vollstaendigkeit, Reihenfolge, Verschwiegenheit
und Schwaerzungen bleibt beim Anwalt (§ 43a BRAO, § 203 StGB, DSGVO). Dieses Werkzeug
ordnet und stempelt nur — es prueft keine Inhalte.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
except ImportError as exc:  # pragma: no cover
    print("FEHLER: pypdf nicht installiert. Bitte `pip install pypdf`.", file=sys.stderr)
    raise SystemExit(2) from exc

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError as exc:  # pragma: no cover
    print("FEHLER: reportlab nicht installiert. Bitte `pip install reportlab`.", file=sys.stderr)
    raise SystemExit(2) from exc


# ---------------------------------------------------------------------------
# Datenmodell
# ---------------------------------------------------------------------------

ANLAGEN_REGEX = re.compile(
    r"^Anlage_(?P<praefix>[A-Z]{1,3})-(?P<nummer>\d{2})(?P<suffix>[a-z]?)_(?P<beschreibung>.+)\.pdf$",
    re.IGNORECASE,
)


@dataclass
class Anlage:
    pfad: Path
    praefix: str
    nummer: int
    suffix: str
    beschreibung: str

    @property
    def bezeichnung(self) -> str:
        """Stempeltext, z. B. 'Anlage K 7' oder 'Anlage K 7a'."""
        return f"Anlage {self.praefix} {self.nummer}{self.suffix}".rstrip()

    @property
    def sortier_schluessel(self) -> tuple:
        return (self.nummer, self.suffix or "")


def lese_anlagen(eingang: Path, praefix: str) -> List[Anlage]:
    anlagen: List[Anlage] = []
    for pdf in sorted(eingang.iterdir()):
        if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
            continue
        m = ANLAGEN_REGEX.match(pdf.name)
        if not m:
            print(f"WARNUNG: ignoriere '{pdf.name}' (entspricht nicht der Konvention)", file=sys.stderr)
            continue
        if m.group("praefix").upper() != praefix.upper():
            print(f"WARNUNG: '{pdf.name}' hat Praefix {m.group('praefix')}, erwartet wurde {praefix}", file=sys.stderr)
            continue
        anlagen.append(
            Anlage(
                pfad=pdf,
                praefix=m.group("praefix").upper(),
                nummer=int(m.group("nummer")),
                suffix=m.group("suffix").lower(),
                beschreibung=m.group("beschreibung").replace("-", " ").replace("_", " "),
            )
        )
    anlagen.sort(key=lambda a: a.sortier_schluessel)
    return anlagen


# ---------------------------------------------------------------------------
# Stempel
# ---------------------------------------------------------------------------

def stempel_overlay(bezeichnung: str, breite: float, hoehe: float) -> io.BytesIO:
    """Erzeugt ein einseitiges Overlay-PDF mit dem Stempel oben rechts."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(breite, hoehe))
    c.setFont("Helvetica", 12)  # Arial-Aequivalent in reportlab-Basisschriften
    text_breite = c.stringWidth(bezeichnung, "Helvetica", 12)
    x = breite - 1.5 * cm - text_breite
    y = hoehe - 1.5 * cm
    c.drawString(x, y, bezeichnung)
    c.save()
    buf.seek(0)
    return buf


def anlage_stempeln(quelle: Path, ziel: Path, bezeichnung: str) -> None:
    """Schreibt die gestempelte Anlage nach `ziel`."""
    reader = PdfReader(str(quelle))
    writer = PdfWriter()
    for idx, page in enumerate(reader.pages):
        if idx == 0:
            box: RectangleObject = page.mediabox
            breite = float(box.width)
            hoehe = float(box.height)
            overlay = PdfReader(stempel_overlay(bezeichnung, breite, hoehe))
            page.merge_page(overlay.pages[0])
        writer.add_page(page)
    with ziel.open("wb") as fh:
        writer.write(fh)


# ---------------------------------------------------------------------------
# Konvolut + Lesezeichen
# ---------------------------------------------------------------------------

def baue_konvolut(anlagen: List[Anlage], gestempelt_ordner: Path, ziel: Path) -> None:
    writer = PdfWriter()
    seitenoffset = 0
    for anlage in anlagen:
        gestempelt = gestempelt_ordner / anlage.pfad.name
        reader = PdfReader(str(gestempelt))
        for page in reader.pages:
            writer.add_page(page)
        writer.add_outline_item(
            title=f"{anlage.bezeichnung} — {anlage.beschreibung}",
            page_number=seitenoffset,
        )
        seitenoffset += len(reader.pages)
    with ziel.open("wb") as fh:
        writer.write(fh)


# ---------------------------------------------------------------------------
# Anlagenverzeichnis
# ---------------------------------------------------------------------------

def schreibe_verzeichnis_md(anlagen: List[Anlage], ziel: Path, schriftsatz: Optional[str]) -> None:
    zeilen: List[str] = []
    if schriftsatz:
        zeilen.append(f"# Anlagenverzeichnis — {schriftsatz}")
    else:
        zeilen.append("# Anlagenverzeichnis")
    zeilen.append("")
    zeilen.append("| Anlage | Kurzbeschreibung | Seiten |")
    zeilen.append("|---|---|---|")
    for anlage in anlagen:
        reader = PdfReader(str(anlage.pfad))
        zeilen.append(
            f"| {anlage.bezeichnung} | {anlage.beschreibung} | {len(reader.pages)} |"
        )
    ziel.write_text("\n".join(zeilen) + "\n", encoding="utf-8")


def schreibe_verzeichnis_pdf(anlagen: List[Anlage], ziel: Path, schriftsatz: Optional[str]) -> None:
    c = canvas.Canvas(str(ziel), pagesize=A4)
    breite, hoehe = A4
    y = hoehe - 2 * cm
    c.setFont("Helvetica-Bold", 16)
    titel = "Anlagenverzeichnis"
    if schriftsatz:
        titel = f"Anlagenverzeichnis — {schriftsatz}"
    c.drawString(2 * cm, y, titel)
    y -= 1 * cm
    c.setFont("Helvetica-Bold", 11)
    c.drawString(2 * cm, y, "Anlage")
    c.drawString(6 * cm, y, "Kurzbeschreibung")
    c.drawString(17 * cm, y, "Seiten")
    y -= 0.5 * cm
    c.line(2 * cm, y, breite - 2 * cm, y)
    y -= 0.5 * cm
    c.setFont("Helvetica", 11)
    for anlage in anlagen:
        if y < 3 * cm:
            c.showPage()
            c.setFont("Helvetica", 11)
            y = hoehe - 2 * cm
        reader = PdfReader(str(anlage.pfad))
        c.drawString(2 * cm, y, anlage.bezeichnung)
        beschreibung = anlage.beschreibung
        if len(beschreibung) > 65:
            beschreibung = beschreibung[:62] + "..."
        c.drawString(6 * cm, y, beschreibung)
        c.drawRightString(breite - 2 * cm, y, str(len(reader.pages)))
        y -= 0.6 * cm
    c.save()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Baut ein beA-faehiges Anlagenkonvolut.")
    parser.add_argument("--eingang", required=True, type=Path, help="Ordner mit Einzel-Anlagen (PDF).")
    parser.add_argument("--ausgang", required=True, type=Path, help="Zielordner; wird angelegt.")
    parser.add_argument("--praefix", default="K", help="Anlagen-Praefix (K, B, A, AST, AG, NI).")
    parser.add_argument("--schriftsatz", default=None, help="Titel des Schriftsatzes (fuer das Verzeichnis).")
    args = parser.parse_args(argv)

    eingang: Path = args.eingang
    ausgang: Path = args.ausgang
    praefix: str = args.praefix.upper()

    if not eingang.is_dir():
        print(f"FEHLER: Eingangsordner '{eingang}' existiert nicht.", file=sys.stderr)
        return 1

    ausgang.mkdir(parents=True, exist_ok=True)
    gestempelt = ausgang / "gestempelt"
    gestempelt.mkdir(exist_ok=True)

    anlagen = lese_anlagen(eingang, praefix)
    if not anlagen:
        print("FEHLER: Keine Anlagen gefunden, die dem Schema entsprechen.", file=sys.stderr)
        return 1

    print(f"{len(anlagen)} Anlage(n) gefunden, Praefix {praefix}.")
    for anlage in anlagen:
        ziel = gestempelt / anlage.pfad.name
        anlage_stempeln(anlage.pfad, ziel, anlage.bezeichnung)
        print(f"  gestempelt: {anlage.bezeichnung}  ({anlage.pfad.name})")

    konvolut_pdf = ausgang / "Anlagenkonvolut.pdf"
    baue_konvolut(anlagen, gestempelt, konvolut_pdf)
    print(f"Konvolut: {konvolut_pdf}")

    verzeichnis_md = ausgang / "Anlagenverzeichnis.md"
    verzeichnis_pdf = ausgang / "Anlagenverzeichnis.pdf"
    schreibe_verzeichnis_md(anlagen, verzeichnis_md, args.schriftsatz)
    schreibe_verzeichnis_pdf(anlagen, verzeichnis_pdf, args.schriftsatz)
    print(f"Verzeichnis: {verzeichnis_md}")
    print(f"Verzeichnis: {verzeichnis_pdf}")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
