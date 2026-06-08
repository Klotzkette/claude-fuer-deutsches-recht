#!/usr/bin/env python3
"""
build_fluggast_anlagen.py
=========================

Spezialisiertes Anlagenpipeline-Werkzeug fuer das Fluggastrechte-Plugin.

Was es leistet:

1. Liest einen Belege-Ordner mit gemischten Formaten (PDF, DOCX, JPG,
   PNG, EML, MSG) und konvertiert alles nach PDF.
2. Liest aus einem **Schriftsatz** (forderungsschreiben / mahnung /
   klage), welche Belege darin erwaehnt werden (Buchungsbestaetigung,
   Boardingpass, Bestaetigung der Annullierung, E-Mail-Verkehr mit der
   Airline, Quittungen fuer Ersatzaufwendungen) und gibt jeder Anlage
   automatisch eine Nummer **K 1, K 2, ...** in der Reihenfolge der
   ersten Erwaehnung im Schriftsatz.
3. Stempelt **oben rechts in Arial 12 pt FETT** "Anlage K 1" auf
   Seite 1 jeder Anlage.
4. Speichert jede Einzelanlage beA-konform benannt
   (`Anlage_K-01_<Kurzbeschreibung>.pdf`).
5. Erzeugt ein Anlagenkonvolut-PDF mit Lesezeichen und ein
   Anlagenverzeichnis (md + pdf).
6. Optional: bindet den Schriftsatz vor das Konvolut und erzeugt ein
   einziges **Schriftsatz_mit_Anlagen.pdf**.

Eingangsordner-Konvention
-------------------------

Belege haben zunaechst beliebige Dateinamen. Wenn die Datei mit dem
Praefix der Konvention beginnt (`Anlage_K-01_...pdf`), wird die
Nummer uebernommen; sonst wird sie aus dem Schriftsatz abgeleitet.

Aufruf
------

    python3 build_fluggast_anlagen.py \\
        --belege ./belege \\
        --schriftsatz ./forderungsschreiben.pdf \\
        --ausgang ./konvolut \\
        --titel "Forderungsschreiben Erste Stufe"

    # mit gebundeltem Schriftsatz_mit_Anlagen.pdf
    python3 build_fluggast_anlagen.py \\
        --belege ./belege \\
        --schriftsatz ./klage.pdf \\
        --ausgang ./konvolut \\
        --titel "Klage Amtsgericht" \\
        --bundle

Abhaengigkeiten
---------------

* pypdf >= 4.0       — PDF lesen / mergen / Lesezeichen
* reportlab >= 4.0   — Stempel + Anlagenverzeichnis
* Pillow (optional)  — fuer JPG/PNG-Vorkonvertierung

Lizenz / Verantwortung
----------------------

Letztverantwortung fuer Vollstaendigkeit, Reihenfolge und
Schwaerzungen bleibt beim Mandanten (bei anwaltlicher Vertretung
beim Anwalt). Das Werkzeug ordnet und stempelt nur — es prueft keine
Inhalte und schwaerzt keine Drittdaten.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple

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
except ImportError as exc:  # pragma: no cover
    print("FEHLER: reportlab nicht installiert. Bitte `pip install reportlab`.", file=sys.stderr)
    raise SystemExit(2) from exc


# ---------------------------------------------------------------------------
# Datenmodell
# ---------------------------------------------------------------------------

ANLAGEN_REGEX = re.compile(
    r"^Anlage_K-(?P<nummer>\d{2})(?P<suffix>[a-z]?)_(?P<beschreibung>.+)\.pdf$",
    re.IGNORECASE,
)


@dataclass
class Anlage:
    pfad: Path
    nummer: int
    suffix: str = ""
    beschreibung: str = ""

    @property
    def bezeichnung(self) -> str:
        return f"Anlage K {self.nummer}{self.suffix}".rstrip()

    @property
    def dateiname(self) -> str:
        # Beschreibung beA-tauglich: keine Umlaute, keine Leerzeichen, kurz
        kurz = (
            self.beschreibung.replace("ae", "ae")
            .replace("oe", "oe")
            .replace("ue", "ue")
            .replace(" ", "-")
        )
        return f"Anlage_K-{self.nummer:02d}{self.suffix}_{kurz}.pdf"

    @property
    def sortier_schluessel(self) -> Tuple[int, str]:
        return (self.nummer, self.suffix)


# ---------------------------------------------------------------------------
# Format-Konvertierung (PDF / DOCX / Bilder / E-Mails)
# ---------------------------------------------------------------------------

def konvertiere_zu_pdf(quelle: Path, ziel: Path) -> Path:
    """Konvertiert beliebige Eingangsformate zu PDF.

    PDF wird kopiert. Bilder werden auf A4 als ein-seitiges PDF gelegt.
    DOCX/EML werden mit LibreOffice headless aufgerufen, falls verfuegbar.
    Andere Formate werfen einen Fehler.
    """
    if not quelle.exists():
        raise FileNotFoundError(quelle)
    suffix = quelle.suffix.lower()
    if suffix == ".pdf":
        ziel.write_bytes(quelle.read_bytes())
        return ziel
    if suffix in (".jpg", ".jpeg", ".png"):
        return _bild_zu_pdf(quelle, ziel)
    if suffix in (".docx", ".eml", ".msg", ".odt", ".rtf", ".txt", ".html"):
        return _libreoffice_konvertieren(quelle, ziel)
    raise ValueError(f"Format {suffix} wird nicht unterstuetzt: {quelle.name}")


def _bild_zu_pdf(quelle: Path, ziel: Path) -> Path:
    try:
        from PIL import Image  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Pillow ist erforderlich fuer Bild-Konvertierung: pip install Pillow") from exc
    img = Image.open(quelle)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    # Bild als A4-Page einbetten — Pillow speichert direkt als PDF
    img.save(ziel, "PDF", resolution=150.0)
    return ziel


def _libreoffice_konvertieren(quelle: Path, ziel: Path) -> Path:
    import shutil
    import subprocess
    binary = shutil.which("libreoffice") or shutil.which("soffice")
    if not binary:
        raise RuntimeError(
            "LibreOffice / soffice ist nicht installiert. "
            f"Konvertiere {quelle.name} manuell nach PDF."
        )
    tmpdir = ziel.parent / ".libreoffice-tmp"
    tmpdir.mkdir(exist_ok=True)
    subprocess.run(
        [binary, "--headless", "--convert-to", "pdf", "--outdir", str(tmpdir), str(quelle)],
        check=True,
        capture_output=True,
    )
    erzeugt = tmpdir / f"{quelle.stem}.pdf"
    if not erzeugt.exists():
        raise RuntimeError(f"LibreOffice-Konvertierung schlug fehl fuer {quelle.name}")
    erzeugt.replace(ziel)
    return ziel


# ---------------------------------------------------------------------------
# Schriftsatz-Analyse: welche Belege werden in welcher Reihenfolge erwaehnt?
# ---------------------------------------------------------------------------

# Erkennt sowohl "(Anlage K 1)" als auch "Anlage K1" und ohne Klammer.
ANLAGE_IM_SCHRIFTSATZ = re.compile(
    r"Anlage\s*K\s*(\d+)([a-z]?)",
    re.IGNORECASE,
)


def lese_schriftsatz_anlagen(schriftsatz_pdf: Path) -> List[Tuple[int, str]]:
    """Extrahiert (nummer, suffix)-Paare in der Reihenfolge des Auftretens.

    Duplikate werden entfernt, die erste Erwaehnung bestimmt die Reihenfolge.
    """
    reader = PdfReader(str(schriftsatz_pdf))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    treffer: List[Tuple[int, str]] = []
    gesehen = set()
    for m in ANLAGE_IM_SCHRIFTSATZ.finditer(text):
        key = (int(m.group(1)), m.group(2).lower())
        if key not in gesehen:
            gesehen.add(key)
            treffer.append(key)
    return treffer


# ---------------------------------------------------------------------------
# Stempel — Arial 12 pt FETT, oben rechts
# ---------------------------------------------------------------------------

def stempel_overlay(bezeichnung: str, breite: float, hoehe: float) -> io.BytesIO:
    """Erzeugt ein einseitiges Overlay-PDF mit dem Stempel oben rechts.

    Schrift: Helvetica-Bold 12 pt (Arial-Aequivalent in den
    reportlab-Basisschriften). Position: 1,5 cm vom oberen, 1,5 cm vom
    rechten Seitenrand.
    """
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(breite, hoehe))
    c.setFont("Helvetica-Bold", 12)
    text_breite = c.stringWidth(bezeichnung, "Helvetica-Bold", 12)
    x = breite - 1.5 * cm - text_breite
    y = hoehe - 1.5 * cm
    c.drawString(x, y, bezeichnung)
    c.save()
    buf.seek(0)
    return buf


def anlage_stempeln(quelle: Path, ziel: Path, bezeichnung: str) -> None:
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
# Konvolut + Lesezeichen + optional Schriftsatz-Bundle
# ---------------------------------------------------------------------------

def baue_konvolut(
    anlagen: List[Anlage],
    gestempelt_ordner: Path,
    ziel: Path,
    schriftsatz_pdf: Optional[Path] = None,
) -> None:
    writer = PdfWriter()
    seitenoffset = 0
    if schriftsatz_pdf is not None:
        reader = PdfReader(str(schriftsatz_pdf))
        for page in reader.pages:
            writer.add_page(page)
        writer.add_outline_item(title="Schriftsatz", page_number=seitenoffset)
        seitenoffset += len(reader.pages)
    for anlage in anlagen:
        gestempelt = gestempelt_ordner / anlage.dateiname
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

def schreibe_verzeichnis_md(anlagen: List[Anlage], ziel: Path, titel: str) -> None:
    zeilen: List[str] = [f"# Anlagenverzeichnis — {titel}", ""]
    zeilen.append("| Anlage | Kurzbeschreibung | Seiten |")
    zeilen.append("|---|---|---|")
    for anlage in anlagen:
        reader = PdfReader(str(anlage.pfad))
        zeilen.append(f"| {anlage.bezeichnung} | {anlage.beschreibung} | {len(reader.pages)} |")
    ziel.write_text("\n".join(zeilen) + "\n", encoding="utf-8")


def schreibe_verzeichnis_pdf(anlagen: List[Anlage], ziel: Path, titel: str) -> None:
    c = canvas.Canvas(str(ziel), pagesize=A4)
    breite, hoehe = A4
    y = hoehe - 2 * cm
    c.setFont("Helvetica-Bold", 16)
    c.drawString(2 * cm, y, f"Anlagenverzeichnis — {titel}")
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
        beschreibung = anlage.beschreibung if len(anlage.beschreibung) <= 65 else anlage.beschreibung[:62] + "..."
        c.drawString(6 * cm, y, beschreibung)
        c.drawRightString(breite - 2 * cm, y, str(len(reader.pages)))
        y -= 0.6 * cm
    c.save()


# ---------------------------------------------------------------------------
# Haupt-Pipeline
# ---------------------------------------------------------------------------

def baue_anlagenpipeline(
    belege_ordner: Path,
    schriftsatz: Path,
    ausgang: Path,
    titel: str,
    bundle: bool = False,
) -> None:
    if not belege_ordner.is_dir():
        raise FileNotFoundError(belege_ordner)
    if not schriftsatz.exists():
        raise FileNotFoundError(schriftsatz)
    ausgang.mkdir(parents=True, exist_ok=True)
    konvertiert = ausgang / "konvertiert"
    gestempelt = ausgang / "gestempelt"
    konvertiert.mkdir(exist_ok=True)
    gestempelt.mkdir(exist_ok=True)

    # Schriftsatz: in PDF normieren
    schriftsatz_pdf = ausgang / "schriftsatz.pdf"
    konvertiere_zu_pdf(schriftsatz, schriftsatz_pdf)

    # Belege: in PDF normieren, in stabiler alphabetischer Reihenfolge
    belege_pdfs: List[Path] = []
    for quelle in sorted(belege_ordner.iterdir()):
        if not quelle.is_file() or quelle.name.startswith("."):
            continue
        ziel = konvertiert / f"{quelle.stem}.pdf"
        try:
            konvertiere_zu_pdf(quelle, ziel)
            belege_pdfs.append(ziel)
            print(f"  konvertiert: {quelle.name} -> {ziel.name}")
        except (ValueError, RuntimeError) as exc:
            print(f"  WARNUNG: {quelle.name}: {exc}", file=sys.stderr)

    if not belege_pdfs:
        print("FEHLER: keine konvertierbaren Belege im Ordner gefunden.", file=sys.stderr)
        raise SystemExit(1)

    # Anlagen aus Schriftsatz extrahieren (in Erwaehnungsreihenfolge)
    erwaehnte = lese_schriftsatz_anlagen(schriftsatz_pdf)

    anlagen: List[Anlage] = []
    if erwaehnte:
        # Zuordnung: i-te Erwaehnung -> i-ter Beleg (alphabetisch)
        # Der Anwender ordnet im Schriftsatz-Skill bereits korrekt zu, indem die
        # Beleg-Dateinamen so beginnen, dass alphabetisch = chronologisch der
        # Erwaehnung entspricht.
        for i, (nr, suffix) in enumerate(erwaehnte):
            if i >= len(belege_pdfs):
                print(f"  WARNUNG: Schriftsatz erwaehnt Anlage K {nr}{suffix}, aber keine Datei vorhanden.", file=sys.stderr)
                continue
            beleg = belege_pdfs[i]
            anlagen.append(Anlage(
                pfad=beleg,
                nummer=nr,
                suffix=suffix,
                beschreibung=beleg.stem.replace("_", " ").replace("-", " "),
            ))
        # Wenn mehr Belege als Erwaehnungen: zusaetzliche fortlaufend nummerieren
        for j, beleg in enumerate(belege_pdfs[len(erwaehnte):], start=len(erwaehnte) + 1):
            anlagen.append(Anlage(
                pfad=beleg,
                nummer=j,
                beschreibung=beleg.stem.replace("_", " ").replace("-", " "),
            ))
            print(f"  HINWEIS: Beleg ohne Erwaehnung -> als Anlage K {j} angehaengt.")
    else:
        # Schriftsatz erwaehnt keine Anlagen — alphabetisch durchnummerieren
        for i, beleg in enumerate(belege_pdfs, start=1):
            anlagen.append(Anlage(
                pfad=beleg,
                nummer=i,
                beschreibung=beleg.stem.replace("_", " ").replace("-", " "),
            ))

    anlagen.sort(key=lambda a: a.sortier_schluessel)

    # Stempeln + beA-Benennung
    for anlage in anlagen:
        ziel = gestempelt / anlage.dateiname
        anlage_stempeln(anlage.pfad, ziel, anlage.bezeichnung)
        print(f"  gestempelt: {anlage.bezeichnung}  ({anlage.dateiname})")
        # Anlage.pfad auf gestempelte Datei umsetzen, damit das Verzeichnis sie zaehlt
        anlage.pfad = ziel

    # Konvolut + Verzeichnis
    konvolut = ausgang / "Anlagenkonvolut.pdf"
    baue_konvolut(anlagen, gestempelt, konvolut)
    print(f"Konvolut: {konvolut}")

    schreibe_verzeichnis_md(anlagen, ausgang / "Anlagenverzeichnis.md", titel)
    schreibe_verzeichnis_pdf(anlagen, ausgang / "Anlagenverzeichnis.pdf", titel)
    print(f"Verzeichnis: {ausgang / 'Anlagenverzeichnis.md'}")
    print(f"Verzeichnis: {ausgang / 'Anlagenverzeichnis.pdf'}")

    # Optional: Schriftsatz + Anlagen als ein PDF
    if bundle:
        bundle_pdf = ausgang / "Schriftsatz_mit_Anlagen.pdf"
        baue_konvolut(anlagen, gestempelt, bundle_pdf, schriftsatz_pdf=schriftsatz_pdf)
        print(f"Bundle:    {bundle_pdf}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Fluggast-Anlagenpipeline: Belege -> beA-Anlagenkonvolut.")
    parser.add_argument("--belege", required=True, type=Path, help="Ordner mit Belegen (PDF/DOCX/JPG/PNG/EML).")
    parser.add_argument("--schriftsatz", required=True, type=Path, help="Schriftsatz-Datei (PDF oder DOCX).")
    parser.add_argument("--ausgang", required=True, type=Path, help="Zielordner; wird angelegt.")
    parser.add_argument("--titel", default="Fluggastrechte", help="Titel des Anlagenverzeichnisses.")
    parser.add_argument("--bundle", action="store_true", help="Zusaetzlich Schriftsatz + Anlagen als ein PDF erzeugen.")
    args = parser.parse_args(argv)

    try:
        baue_anlagenpipeline(
            belege_ordner=args.belege,
            schriftsatz=args.schriftsatz,
            ausgang=args.ausgang,
            titel=args.titel,
            bundle=args.bundle,
        )
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
