#!/usr/bin/env python3
"""Erzeugt eine kontrollierbare Versandmappe aus Hauptdokument und Anlagen.

Das Werkzeug übernimmt keine rechtliche Freigabe und versendet nichts. Es
konvertiert unterstützte Arbeitsdateien, stempelt Anlagen standardmäßig auf
jeder Seite, erzeugt getrennte Versanddateien und schreibt Prüfberichte.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Iterable, Optional

from office_process import pdf_markers, run_office

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
except ImportError as exc:  # pragma: no cover
    print("FEHLER: pypdf fehlt. Installation: pip install pypdf", file=sys.stderr)
    raise SystemExit(2) from exc

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas
except ImportError as exc:  # pragma: no cover
    print("FEHLER: reportlab fehlt. Installation: pip install reportlab", file=sys.stderr)
    raise SystemExit(2) from exc


ANLAGEN_REGEX = re.compile(
    r"^Anlage[_ -](?P<praefix>[A-Z]{1,3})[_ -]?(?P<nummer>\d{1,3})"
    r"(?P<suffix>[a-z]?)[_ -]+(?P<beschreibung>.+)$",
    re.IGNORECASE,
)
OFFICE_ENDUNGEN = {".doc", ".docx", ".odt", ".rtf", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".odp"}
BILD_ENDUNGEN = {".jpg", ".jpeg", ".png"}
AKTIVE_PDF_MARKER = (b"/JavaScript", b"/JS", b"/EmbeddedFiles", b"/Launch")
MAX_DATEIEN_PRO_NACHRICHT = 1000
MAX_BYTES_PRO_NACHRICHT = 200 * 1024 * 1024
OFFICE_TIMEOUT = 120


@dataclass
class Befund:
    stufe: str
    datei: str
    text: str


@dataclass
class Anlage:
    quelle: Path
    arbeits_pdf: Path
    praefix: str
    nummer: int
    suffix: str
    beschreibung: str
    ausgabe_name: str = ""
    seiten: int = 0
    textzeichen: int = 0
    quell_hash: str = ""
    ausgabe_hash: str = ""
    bytes: int = 0
    befunde: list[Befund] = field(default_factory=list)

    @property
    def bezeichnung(self) -> str:
        return f"Anlage {self.praefix} {self.nummer}{self.suffix}".rstrip()

    @property
    def sortier_schluessel(self) -> tuple[int, str]:
        return (self.nummer, self.suffix or "")


def sha256(pfad: Path) -> str:
    digest = hashlib.sha256()
    with pfad.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def eine_zeile(wert: object) -> str:
    return " ".join(str(wert).replace("\x00", "").split())


def markdown_zelle(wert: object) -> str:
    return eine_zeile(wert).replace("\\", "\\\\").replace("|", "\\|").replace("`", "\\`")


def pdf_text(wert: object) -> str:
    return eine_zeile(wert).encode("cp1252", "replace").decode("cp1252")


def csv_sicher(wert: object) -> object:
    if not isinstance(wert, str):
        return wert
    text = eine_zeile(wert)
    return f"'{text}" if text.startswith(("=", "+", "-", "@")) else text


def ascii_segment(text: str) -> str:
    ersetzungen = str.maketrans(
        {"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue", "ß": "ss"}
    )
    text = text.translate(ersetzungen)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    return re.sub(r"_+", "_", text) or "Dokument"


def begrenze_dateiname(prefix: str, beschreibung: str, max_laenge: int) -> str:
    endung = ".pdf"
    beschreibung = ascii_segment(beschreibung)
    frei = max_laenge - len(prefix) - len(endung)
    if frei < 1:
        raise ValueError(f"Dateinamenspräfix ist länger als das Profil erlaubt: {prefix}")
    beschreibung = beschreibung[:frei].rstrip("_") or "Dokument"
    return f"{prefix}{beschreibung}{endung}"


def ausgabe_name_anlage(
    anlage: Anlage,
    reihenfolge: int,
    stellen: int,
    profil: str,
    datum: str,
) -> str:
    seq = f"{reihenfolge:0{stellen}d}"
    label = f"Anlage{anlage.praefix}{anlage.nummer}{anlage.suffix}"
    if profil == "nrw":
        prefix = f"Anlage_{anlage.nummer:0{stellen}d}_"
    elif profil == "bund":
        prefix = f"{seq}_{label}_"
    else:
        prefix = f"{seq}_{datum}_{label}_"
    max_laenge = 90 if profil == "bund" else 60
    return begrenze_dateiname(prefix, anlage.beschreibung, max_laenge)


def ausgabe_name_hauptdokument(profil: str, datum: str, praefix: str, dokumentart: str) -> str:
    dokumentart = ascii_segment(dokumentart)
    if profil == "nrw":
        prefix = f"{ascii_segment(praefix)}_"
        return begrenze_dateiname(prefix, dokumentart, 60)
    if profil == "bund":
        return begrenze_dateiname("00_", dokumentart, 90)
    return begrenze_dateiname(f"00_{datum}_", dokumentart, 60)


def konvertiere_bild(quelle: Path, ziel: Path) -> None:
    bild = ImageReader(str(quelle))
    breite, hoehe = bild.getSize()
    seiten_breite, seiten_hoehe = A4
    rand = 1.5 * cm
    faktor = min((seiten_breite - 2 * rand) / breite, (seiten_hoehe - 2 * rand) / hoehe)
    zeich_breite = breite * faktor
    zeich_hoehe = hoehe * faktor
    c = canvas.Canvas(str(ziel), pagesize=A4)
    c.drawImage(
        bild,
        (seiten_breite - zeich_breite) / 2,
        (seiten_hoehe - zeich_hoehe) / 2,
        width=zeich_breite,
        height=zeich_hoehe,
        preserveAspectRatio=True,
        mask="auto",
    )
    c.save()


def konvertiere_office(quelle: Path, ziel_ordner: Path) -> Path:
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        raise RuntimeError("LibreOffice ist für die Office-Konvertierung nicht verfügbar")
    ziel_ordner.mkdir(parents=True, exist_ok=True)
    ziel = ziel_ordner / f"{quelle.stem}.pdf"
    with tempfile.TemporaryDirectory(prefix="office-", dir=ziel_ordner) as tmp:
        work = Path(tmp)
        ausgabe = work / "pdf"
        ausgabe.mkdir()
        try:
            code, details = run_office(
                [soffice, f"-env:UserInstallation={(work / 'profile').resolve().as_uri()}",
                 "--headless", "--convert-to", "pdf", "--outdir", str(ausgabe.resolve()), str(quelle.resolve())],
                timeout=OFFICE_TIMEOUT,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(f"Office-Konvertierung nach {OFFICE_TIMEOUT} Sekunden abgebrochen: {quelle.name}") from exc
        erzeugt = ausgabe / ziel.name
        if code != 0 or not erzeugt.is_file() or not erzeugt.stat().st_size:
            raise RuntimeError(f"Office-Konvertierung fehlgeschlagen: {details or 'keine neue PDF erzeugt'}")
        try:
            reader = PdfReader(str(erzeugt))
            if reader.is_encrypted or not reader.pages:
                raise ValueError("verschlüsselte oder leere PDF")
        except Exception as exc:
            raise RuntimeError(f"Office-Ausgabe ist keine nutzbare PDF: {quelle.name}") from exc
        erzeugt.replace(ziel)
    return ziel


def als_pdf(quelle: Path, temp: Path, konvertieren: bool) -> Path:
    if quelle.suffix.lower() == ".pdf":
        return quelle
    if not konvertieren:
        raise RuntimeError("Datei ist keine PDF; Konvertierung wurde ausgeschaltet")
    ziel_ordner = temp / hashlib.sha256(str(quelle).encode("utf-8")).hexdigest()[:12]
    ziel_ordner.mkdir(parents=True, exist_ok=True)
    if quelle.suffix.lower() in BILD_ENDUNGEN:
        ziel = ziel_ordner / f"{quelle.stem}.pdf"
        konvertiere_bild(quelle, ziel)
        return ziel
    if quelle.suffix.lower() in OFFICE_ENDUNGEN:
        return konvertiere_office(quelle, ziel_ordner)
    raise RuntimeError(f"Dateityp {quelle.suffix or '[ohne Endung]'} wird nicht automatisch konvertiert")


def lese_anlagen(
    eingang: Path,
    praefix: str,
    temp: Path,
    konvertieren: bool,
    hauptdokument: Optional[Path],
) -> tuple[list[Anlage], list[Befund]]:
    anlagen: list[Anlage] = []
    befunde: list[Befund] = []
    haupt_resolved = hauptdokument.resolve() if hauptdokument else None

    for quelle in sorted(eingang.iterdir(), key=lambda p: p.name.lower()):
        if not quelle.is_file() or quelle.name.startswith("."):
            continue
        if haupt_resolved and quelle.resolve() == haupt_resolved:
            continue
        match = ANLAGEN_REGEX.match(quelle.stem)
        if not match:
            befunde.append(Befund("HINWEIS", quelle.name, "Dateiname enthält keine erkennbare Anlagenkennung; Datei nicht verarbeitet"))
            continue
        if match.group("praefix").upper() != praefix.upper():
            befunde.append(Befund("STOP", quelle.name, f"Nummernkreis {match.group('praefix').upper()} passt nicht zu {praefix.upper()}"))
            continue
        try:
            pdf = als_pdf(quelle, temp, konvertieren)
        except Exception as exc:  # noqa: BLE001 - Befund soll vollständig protokolliert werden
            befunde.append(Befund("STOP", quelle.name, str(exc)))
            continue
        anlagen.append(
            Anlage(
                quelle=quelle,
                arbeits_pdf=pdf,
                praefix=match.group("praefix").upper(),
                nummer=int(match.group("nummer")),
                suffix=match.group("suffix").lower(),
                beschreibung=match.group("beschreibung").replace("-", " ").replace("_", " "),
                quell_hash=sha256(quelle),
            )
        )

    anlagen.sort(key=lambda a: a.sortier_schluessel)
    return anlagen, befunde


def stempel_overlay(bezeichnung: str, breite: float, hoehe: float) -> io.BytesIO:
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(breite, hoehe))
    schrift = "Helvetica-Bold"
    groesse = 10.5
    c.setFont(schrift, groesse)
    text_breite = c.stringWidth(bezeichnung, schrift, groesse)
    x = max(0.8 * cm, breite - 1.2 * cm - text_breite)
    y = max(0.8 * cm, hoehe - 1.0 * cm)
    c.drawString(x, y, bezeichnung)
    c.save()
    buf.seek(0)
    return buf


def pruefe_pdf(quelle: Path, anzeigename: str) -> tuple[PdfReader, int, int, list[Befund]]:
    befunde: list[Befund] = []
    try:
        marker_funde = pdf_markers(quelle, AKTIVE_PDF_MARKER)
        reader = PdfReader(str(quelle), strict=False)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"PDF kann nicht gelesen werden: {exc}") from exc
    if reader.is_encrypted:
        raise RuntimeError("PDF ist verschlüsselt oder kennwortgeschützt")
    if not reader.pages:
        raise RuntimeError("PDF enthält keine Seiten")
    for marker in AKTIVE_PDF_MARKER:
        if marker in marker_funde:
            befunde.append(Befund("STOP", anzeigename, f"aktiver oder eingebetteter PDF-Inhalt erkannt: {marker.decode('ascii')}"))
    textzeichen = 0
    for seite in reader.pages:
        try:
            textzeichen += len((seite.extract_text() or "").strip())
        except Exception:  # noqa: BLE001
            befunde.append(Befund("WARNUNG", anzeigename, "Textprüfung einer Seite ist fehlgeschlagen"))
    if textzeichen < 20:
        befunde.append(Befund("WARNUNG", anzeigename, "kaum auslesbarer Text; OCR und visuelle Lesbarkeit prüfen"))
    return reader, len(reader.pages), textzeichen, befunde


def anlage_stempeln(quelle: Path, ziel: Path, bezeichnung: str, alle_seiten: bool) -> tuple[int, int, list[Befund]]:
    reader, seiten, textzeichen, befunde = pruefe_pdf(quelle, quelle.name)
    writer = PdfWriter()
    for index, page in enumerate(reader.pages):
        if alle_seiten or index == 0:
            if getattr(page, "rotation", 0) and hasattr(page, "transfer_rotation_to_content"):
                page.transfer_rotation_to_content()
            box: RectangleObject = page.mediabox
            overlay = PdfReader(stempel_overlay(bezeichnung, float(box.width), float(box.height)))
            page.merge_page(overlay.pages[0])
        writer.add_page(page)
    with ziel.open("wb") as fh:
        writer.write(fh)
    PdfReader(str(ziel), strict=True)
    return seiten, textzeichen, befunde


def kopiere_hauptdokument(
    quelle: Path,
    ziel: Path,
    temp: Path,
    konvertieren: bool,
) -> tuple[int, int, list[Befund]]:
    pdf = als_pdf(quelle, temp, konvertieren)
    _, seiten, textzeichen, befunde = pruefe_pdf(pdf, quelle.name)
    shutil.copy2(pdf, ziel)
    PdfReader(str(ziel), strict=True)
    return seiten, textzeichen, befunde


def pruefe_nummernfolge(anlagen: list[Anlage]) -> list[Befund]:
    befunde: list[Befund] = []
    gesehen: set[tuple[int, str]] = set()
    for anlage in anlagen:
        key = anlage.sortier_schluessel
        if key in gesehen:
            befunde.append(Befund("STOP", anlage.quelle.name, f"Anlagenbezeichnung {anlage.bezeichnung} ist doppelt"))
        gesehen.add(key)
    nummern = sorted({a.nummer for a in anlagen})
    if nummern:
        erwartet = list(range(nummern[0], nummern[-1] + 1))
        fehlend = sorted(set(erwartet) - set(nummern))
        if fehlend:
            befunde.append(Befund("STOP", "Anlagenfolge", f"Nummernlücke: {', '.join(map(str, fehlend))}"))
    hash_quellen: dict[str, list[str]] = {}
    for anlage in anlagen:
        hash_quellen.setdefault(anlage.quell_hash, []).append(anlage.quelle.name)
    for namen in hash_quellen.values():
        if len(namen) > 1:
            befunde.append(Befund("WARNUNG", "Duplikatprüfung", f"inhaltsgleiche Quelldateien: {'; '.join(namen)}"))
    return befunde


def baue_pruefkonvolut(anlagen: Iterable[Anlage], versand_ordner: Path, ziel: Path) -> None:
    writer = PdfWriter()
    seitenoffset = 0
    for anlage in anlagen:
        reader = PdfReader(str(versand_ordner / anlage.ausgabe_name))
        for page in reader.pages:
            writer.add_page(page)
        writer.add_outline_item(
            title=f"{anlage.bezeichnung} - {anlage.beschreibung}",
            page_number=seitenoffset,
        )
        seitenoffset += len(reader.pages)
    with ziel.open("wb") as fh:
        writer.write(fh)


def schreibe_anlagenverzeichnis(anlagen: list[Anlage], ziel: Path, schriftsatz: str) -> None:
    zeilen = [
        f"# Anlagenverzeichnis - {eine_zeile(schriftsatz)}",
        "",
        "| Anlage | Kurzbeschreibung | Seiten | Versanddatei |",
        "| --- | --- | --- | --- |",
    ]
    for anlage in anlagen:
        zeilen.append(
            f"| {markdown_zelle(anlage.bezeichnung)} | {markdown_zelle(anlage.beschreibung)} | "
            f"{anlage.seiten} | `{markdown_zelle(anlage.ausgabe_name)}` |"
        )
    ziel.write_text("\n".join(zeilen) + "\n", encoding="utf-8")


def schreibe_anlagenverzeichnis_pdf(anlagen: list[Anlage], ziel: Path, schriftsatz: str) -> None:
    c = canvas.Canvas(str(ziel), pagesize=A4)
    breite, hoehe = A4
    y = hoehe - 2 * cm
    c.setFont("Helvetica-Bold", 15)
    c.drawString(2 * cm, y, "Anlagenverzeichnis")
    y -= 0.7 * cm
    c.setFont("Helvetica", 10)
    c.drawString(2 * cm, y, pdf_text(schriftsatz)[:90])
    y -= 1 * cm
    for anlage in anlagen:
        if y < 2.5 * cm:
            c.showPage()
            y = hoehe - 2 * cm
        c.setFont("Helvetica-Bold", 10)
        c.drawString(2 * cm, y, anlage.bezeichnung)
        c.setFont("Helvetica", 10)
        c.drawString(5 * cm, y, pdf_text(anlage.beschreibung)[:70])
        c.drawRightString(breite - 2 * cm, y, str(anlage.seiten))
        y -= 0.55 * cm
    c.save()


def schreibe_manifest(
    anlagen: list[Anlage],
    csv_ziel: Path,
    json_ziel: Path,
    metadaten: dict[str, object],
) -> None:
    felder = [
        "anlage",
        "quelle",
        "versanddatei",
        "beschreibung",
        "seiten",
        "bytes",
        "sha256_quelle",
        "sha256_versand",
        "textzeichen",
        "status",
    ]
    with csv_ziel.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=felder, delimiter=";")
        writer.writeheader()
        for a in anlagen:
            zeile = {
                "anlage": a.bezeichnung,
                "quelle": a.quelle.name,
                "versanddatei": a.ausgabe_name,
                "beschreibung": a.beschreibung,
                "seiten": a.seiten,
                "bytes": a.bytes,
                "sha256_quelle": a.quell_hash,
                "sha256_versand": a.ausgabe_hash,
                "textzeichen": a.textzeichen,
                "status": (
                    "STOP"
                    if any(b.stufe == "STOP" for b in a.befunde)
                    else "PRUEFEN"
                    if a.befunde
                    else "TECHNISCH_OK"
                ),
            }
            writer.writerow({feld: csv_sicher(wert) for feld, wert in zeile.items()})
    daten = {
        "metadaten": metadaten,
        "anlagen": [
            {
                "anlage": a.bezeichnung,
                "quelle": a.quelle.name,
                "versanddatei": a.ausgabe_name,
                "beschreibung": a.beschreibung,
                "seiten": a.seiten,
                "bytes": a.bytes,
                "sha256_quelle": a.quell_hash,
                "sha256_versand": a.ausgabe_hash,
                "textzeichen": a.textzeichen,
                "befunde": [b.__dict__ for b in a.befunde],
            }
            for a in anlagen
        ],
    }
    json_ziel.write_text(json.dumps(daten, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def schreibe_preflight(
    ziel: Path,
    befunde: list[Befund],
    metadaten: dict[str, object],
    dateien: int,
    bytes_gesamt: int,
) -> None:
    zeilen = [
        "# Preflight-Bericht",
        "",
        "## 1. Versanddaten",
        "",
        f"- Gericht: {markdown_zelle(metadaten['gericht'] or '[nicht angegeben]')}",
        f"- Aktenzeichen: {markdown_zelle(metadaten['aktenzeichen'] or '[Neueingang oder nicht angegeben]')}",
        f"- Profil: {metadaten['profil']}",
        f"- Dateien im Versandordner: {dateien}",
        f"- Gesamtgröße: {bytes_gesamt} Bytes",
        f"- Anlagenstempel: {'jede Seite' if metadaten['stempel_alle_seiten'] else 'nur erste Seite'}",
        "- PDF/A-Status: nicht technisch validiert",
        "",
        "## 2. Befunde",
        "",
    ]
    if befunde:
        zeilen.extend(["| Stufe | Datei | Befund |", "| --- | --- | --- |"])
        for b in befunde:
            zeilen.append(f"| {b.stufe} | {b.datei} | {b.text} |")
    else:
        zeilen.append("Keine maschinell erkannten Stop- oder Warnbefunde. Die anwaltliche Sicht- und Formkontrolle bleibt erforderlich.")
    zeilen.extend(
        [
            "",
            "## 3. Nicht automatisierbare Freigaben",
            "",
            "1. Schriftsatzinhalt, Anträge und Beweisbezüge anwaltlich prüfen.",
            "2. Jede konvertierte oder gestempelte Seite visuell kontrollieren.",
            "3. Signaturweg und persönlichen Versand festlegen.",
            "4. Sicherstellen, dass die Nachricht ausschließlich dieses Verfahren betrifft.",
            "5. Empfänger, Aktenzeichen, Dokumentart und erzeugte Strukturdaten im Versanddialog kontrollieren.",
            "6. Nach Versand die automatisierte gerichtliche Eingangsbestätigung prüfen und sichern.",
        ]
    )
    ziel.write_text("\n".join(zeilen) + "\n", encoding="utf-8")


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Erzeugt eine beA-Versandmappe mit getrennten PDF-Anlagen und Preflight-Bericht.")
    parser.add_argument("--eingang", required=True, type=Path, help="Ordner mit Anlagen")
    parser.add_argument("--ausgang", required=True, type=Path, help="Neuer Zielordner")
    parser.add_argument("--praefix", default="K", help="Nummernkreis K, B, AST oder AG")
    parser.add_argument("--hauptdokument", type=Path, help="Finaler Schriftsatz als PDF oder konvertierbare Office-Datei")
    parser.add_argument("--dokumentart", default="Schriftsatz_mit_Antraegen", help="Sprechende Art des Hauptdokuments")
    parser.add_argument("--schriftsatz", help="Abwärtskompatibler Titel für Anlagenverzeichnis")
    parser.add_argument("--profil", choices=["gericht-sicher", "berlin", "nrw", "bund"], default="gericht-sicher")
    parser.add_argument("--datum", default=date.today().strftime("%Y%m%d"), help="Dokumentdatum als JJJJMMTT")
    parser.add_argument("--gericht", default="", help="Empfängergericht für den Prüfbericht")
    parser.add_argument("--aktenzeichen", default="", help="Gerichtliches Aktenzeichen oder Neueingang")
    parser.add_argument("--stempel-seiten", choices=["alle", "erste"], default="alle")
    parser.add_argument("--keine-konvertierung", action="store_true", help="Nur vorhandene PDFs verarbeiten")
    parser.add_argument("--ueberschreiben", action="store_true", help="Vorhandenen Zielordner vollständig ersetzen")
    parser.add_argument("--strict", action="store_true", help="Bei jedem Stop-Befund mit Fehlerstatus enden")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    eingang = args.eingang.resolve()
    ausgang = args.ausgang.resolve()
    praefix = args.praefix.upper()
    if praefix not in {"K", "B", "AST", "AG"}:
        print("FEHLER: --praefix muss K, B, AST oder AG sein", file=sys.stderr)
        return 2
    try:
        datetime.strptime(args.datum, "%Y%m%d")
    except ValueError:
        print("FEHLER: --datum muss JJJJMMTT entsprechen", file=sys.stderr)
        return 2
    if not eingang.is_dir():
        print(f"FEHLER: Eingangsordner fehlt: {eingang}", file=sys.stderr)
        return 2
    if args.hauptdokument and not args.hauptdokument.is_file():
        print(f"FEHLER: Hauptdokument fehlt: {args.hauptdokument}", file=sys.stderr)
        return 2
    if ausgang.exists() and any(ausgang.iterdir()):
        if not args.ueberschreiben:
            print("FEHLER: Zielordner ist nicht leer; bewusst --ueberschreiben verwenden", file=sys.stderr)
            return 2
        shutil.rmtree(ausgang)

    versand = ausgang / "versandfertig"
    intern = ausgang / "intern"
    versand.mkdir(parents=True, exist_ok=True)
    intern.mkdir(parents=True, exist_ok=True)
    alle_befunde: list[Befund] = []
    fehlstufe = "STOP" if args.strict else "WARNUNG"
    if not args.gericht.strip():
        alle_befunde.append(Befund(fehlstufe, "Versanddaten", "Empfängergericht ist nicht angegeben"))
    if not args.aktenzeichen.strip():
        alle_befunde.append(Befund(fehlstufe, "Versanddaten", "Aktenzeichen oder der Wert Neueingang ist nicht angegeben"))

    with tempfile.TemporaryDirectory(prefix="bea-produktion-") as tmp:
        temp = Path(tmp)
        anlagen, befunde = lese_anlagen(
            eingang,
            praefix,
            temp,
            not args.keine_konvertierung,
            args.hauptdokument,
        )
        alle_befunde.extend(befunde)
        alle_befunde.extend(pruefe_nummernfolge(anlagen))
        if not anlagen:
            alle_befunde.append(Befund("STOP", "Anlagen", "keine verarbeitbare Anlage gefunden"))

        stellen = 3 if len(anlagen) >= 100 else 2
        for index, anlage in enumerate(anlagen, start=1):
            anlage.ausgabe_name = ausgabe_name_anlage(anlage, index, stellen, args.profil, args.datum)
            ziel = versand / anlage.ausgabe_name
            try:
                anlage.seiten, anlage.textzeichen, anlage.befunde = anlage_stempeln(
                    anlage.arbeits_pdf,
                    ziel,
                    anlage.bezeichnung,
                    args.stempel_seiten == "alle",
                )
                anlage.ausgabe_hash = sha256(ziel)
                anlage.bytes = ziel.stat().st_size
            except Exception as exc:  # noqa: BLE001
                anlage.befunde.append(Befund("STOP", anlage.quelle.name, str(exc)))
            alle_befunde.extend(anlage.befunde)

        haupt_name = ""
        if args.hauptdokument:
            haupt_name = ausgabe_name_hauptdokument(args.profil, args.datum, praefix, args.dokumentart)
            try:
                _, _, haupt_befunde = kopiere_hauptdokument(
                    args.hauptdokument,
                    versand / haupt_name,
                    temp,
                    not args.keine_konvertierung,
                )
                alle_befunde.extend(haupt_befunde)
            except Exception as exc:  # noqa: BLE001
                alle_befunde.append(Befund("STOP", args.hauptdokument.name, str(exc)))
        else:
            alle_befunde.append(Befund(fehlstufe, "Hauptdokument", "kein Hauptdokument übergeben; Versandmappe ist nicht vollständig"))

    vorhandene_anlagen = [a for a in anlagen if (versand / a.ausgabe_name).is_file()]
    titel = args.schriftsatz or args.dokumentart
    schreibe_anlagenverzeichnis(vorhandene_anlagen, intern / "Anlagenverzeichnis.md", titel)
    schreibe_anlagenverzeichnis_pdf(vorhandene_anlagen, intern / "Anlagenverzeichnis.pdf", titel)
    if vorhandene_anlagen:
        baue_pruefkonvolut(vorhandene_anlagen, versand, intern / "Anlagenkonvolut_Prueffassung.pdf")

    versand_dateien = sorted(p for p in versand.iterdir() if p.is_file())
    bytes_gesamt = sum(p.stat().st_size for p in versand_dateien)
    if len(versand_dateien) > MAX_DATEIEN_PRO_NACHRICHT:
        alle_befunde.append(Befund("STOP", "Versandpaket", f"mehr als {MAX_DATEIEN_PRO_NACHRICHT} Dateien"))
    if bytes_gesamt > MAX_BYTES_PRO_NACHRICHT:
        alle_befunde.append(Befund("STOP", "Versandpaket", "Gesamtgröße überschreitet 200 MB"))
    if args.stempel_seiten != "alle":
        alle_befunde.append(Befund("WARNUNG", "Anlagenstempel", "nur die erste Seite wurde gestempelt; Berliner Gerichtshinweis empfiehlt sämtliche Seiten"))

    metadaten: dict[str, object] = {
        "gericht": args.gericht,
        "aktenzeichen": args.aktenzeichen,
        "profil": args.profil,
        "datum": args.datum,
        "praefix": praefix,
        "dokumentart": args.dokumentart,
        "hauptdokument": haupt_name,
        "stempel_alle_seiten": args.stempel_seiten == "alle",
        "dateien": len(versand_dateien),
        "bytes_gesamt": bytes_gesamt,
    }
    schreibe_manifest(
        vorhandene_anlagen,
        intern / "Versandmanifest.csv",
        intern / "Versandmanifest.json",
        metadaten,
    )
    schreibe_preflight(
        intern / "Preflight-Bericht.md",
        alle_befunde,
        metadaten,
        len(versand_dateien),
        bytes_gesamt,
    )

    print(f"Versandordner: {versand}")
    print(f"Interne Prüfunterlagen: {intern}")
    print(f"Dateien: {len(versand_dateien)}, Gesamtgröße: {bytes_gesamt} Bytes")
    stop_anzahl = sum(1 for b in alle_befunde if b.stufe == "STOP")
    warn_anzahl = sum(1 for b in alle_befunde if b.stufe == "WARNUNG")
    print(f"Befunde: {stop_anzahl} Stop, {warn_anzahl} Warnung")
    if stop_anzahl and args.strict:
        return 3
    return 0 if not stop_anzahl else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
