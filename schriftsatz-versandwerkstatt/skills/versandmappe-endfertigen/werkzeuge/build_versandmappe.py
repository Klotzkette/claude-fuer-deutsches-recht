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
import textwrap
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
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
BILD_ENDUNGEN = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
TEXT_ENDUNGEN = {".txt", ".csv", ".tsv", ".md", ".log"}
HTML_ENDUNGEN = {".htm", ".html"}
EMAIL_ENDUNGEN = {".eml"}
KENNUNG_REGEX = re.compile(r"(?:Anlage\s+)?(?P<praefix>AST|AG|K|B)[ _-]*(?P<nummer>[0-9]{1,3})(?P<suffix>[a-z]?)", re.IGNORECASE)
AKTIVE_PDF_MARKER = (b"/JavaScript", b"/JS", b"/EmbeddedFiles", b"/Launch")
MAX_DATEIEN_PRO_NACHRICHT = 1000
MAX_BYTES_PRO_NACHRICHT = 200_000_000
OFFICE_TIMEOUT = 120


class TextAusHtml(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.teile: list[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.teile.append(data.strip())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if tag.lower() in {"br", "p", "div", "li", "tr", "h1", "h2", "h3"}:
            self.teile.append("\n")

    def text(self) -> str:
        return " ".join(self.teile).replace(" \n ", "\n").replace("\n ", "\n")


@dataclass
class Befund:
    stufe: str
    datei: str
    text: str


@dataclass
class Anlage:
    quelle: Path
    quelle_relativ: str
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
        prefix = f"Anlage_{anlage.nummer:0{stellen}d}{anlage.suffix}_"
    elif profil == "bund":
        prefix = f"{seq}_{label}_"
    else:
        prefix = f"{seq}_{datum}_{label}_"
    max_laenge = 84 if profil == "bund" else 80 if profil == "kanzlei-ascii" else 60
    return begrenze_dateiname(prefix, anlage.beschreibung, max_laenge)


def ausgabe_name_hauptdokument(profil: str, datum: str, praefix: str, dokumentart: str) -> str:
    dokumentart = ascii_segment(dokumentart)
    if profil == "nrw":
        prefix = f"{ascii_segment(praefix)}_"
        return begrenze_dateiname(prefix, dokumentart, 60)
    if profil == "bund":
        return begrenze_dateiname("00_", dokumentart, 84)
    max_laenge = 80 if profil == "kanzlei-ascii" else 60
    return begrenze_dateiname(f"00_{datum}_", dokumentart, max_laenge)


def schreibe_text_pdf(ziel: Path, titel: str, kopf: list[tuple[str, str]], inhalt: str) -> None:
    try:
        "\n".join([titel, inhalt, *(wert for _, wert in kopf)]).encode("cp1252")
    except UnicodeEncodeError as exc:
        raise ValueError("Text enthält Zeichen außerhalb der verfügbaren PDF-Schrift; mit geeigneten Schriften exportieren, nicht durch Fragezeichen ersetzen") from exc
    breite, hoehe = A4
    links = 1.8 * cm
    oben = hoehe - 1.8 * cm
    unten = 1.8 * cm
    c = canvas.Canvas(str(ziel), pagesize=A4)

    def neue_seite(seite: int) -> float:
        if seite > 1:
            c.showPage()
        c.setFont("Helvetica-Bold", 14)
        c.drawString(links, oben, pdf_text(titel)[:95])
        c.setFont("Helvetica", 8)
        c.drawRightString(breite - links, oben, f"Seite {seite}")
        return oben - 0.8 * cm

    seite = 1
    y = neue_seite(seite)
    for name, wert in kopf:
        for index, zeile in enumerate(textwrap.wrap(pdf_text(wert), width=92) or [""]):
            if y < unten:
                seite += 1
                y = neue_seite(seite)
            c.setFont("Helvetica-Bold" if index == 0 else "Helvetica", 9)
            prefix = f"{pdf_text(name)}: " if index == 0 else ""
            c.drawString(links, y, (prefix + zeile)[:118])
            y -= 0.45 * cm
    y -= 0.25 * cm
    c.setFont("Helvetica", 9)
    for rohzeile in inhalt.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        umbruch = textwrap.wrap(pdf_text(rohzeile), width=108, replace_whitespace=False) or [""]
        for zeile in umbruch:
            if y < unten:
                seite += 1
                y = neue_seite(seite)
                c.setFont("Helvetica", 9)
            c.drawString(links, y, zeile[:125])
            y -= 0.42 * cm
    c.save()


def lese_textdatei(quelle: Path) -> str:
    roh = quelle.read_bytes()
    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            text = roh.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:  # pragma: no cover
        text = roh.decode("utf-8", "replace")
    if quelle.suffix.lower() not in {".csv", ".tsv"}:
        return text
    delimiter = "\t" if quelle.suffix.lower() == ".tsv" else ";"
    try:
        dialect = csv.Sniffer().sniff(text[:8192], delimiters=",;\t|")
        delimiter = dialect.delimiter
    except csv.Error:
        pass
    return "\n".join(" | ".join(zelle.strip() for zelle in zeile) for zeile in csv.reader(io.StringIO(text), delimiter=delimiter))


def konvertiere_text(quelle: Path, ziel: Path) -> None:
    schreibe_text_pdf(ziel, quelle.name, [("Quelle", quelle.name)], lese_textdatei(quelle))


def konvertiere_html(quelle: Path, ziel: Path) -> None:
    parser = TextAusHtml()
    parser.feed(lese_textdatei(quelle))
    schreibe_text_pdf(ziel, quelle.name, [("Quelle", quelle.name)], parser.text())


def email_anhaenge(nachricht):
    """Auch Bilder im ausgewählten HTML-/Related-Nachrichtenteil erfassen."""
    direkt = list(nachricht.iter_attachments())
    yield from direkt
    direkte_ids = {id(part) for part in direkt}
    for part in nachricht.iter_parts():
        if id(part) not in direkte_ids and part.is_multipart():
            yield from email_anhaenge(part)


def konvertiere_email(quelle: Path, ziel: Path) -> None:
    nachricht = BytesParser(policy=policy.default).parsebytes(quelle.read_bytes())
    teil = nachricht.get_body(preferencelist=("plain", "html"))
    inhalt = ""
    if teil is not None:
        inhalt = teil.get_content()
        if teil.get_content_subtype() == "html":
            parser = TextAusHtml()
            parser.feed(str(inhalt))
            inhalt = parser.text()
    anhaenge = [part.get_filename() or "[ohne Dateiname]" for part in email_anhaenge(nachricht)]
    kopf = [
        ("Von", str(nachricht.get("From", ""))),
        ("An", str(nachricht.get("To", ""))),
        ("Cc", str(nachricht.get("Cc", ""))),
        ("Datum", str(nachricht.get("Date", ""))),
        ("Betreff", str(nachricht.get("Subject", ""))),
        ("Anhänge", ", ".join(anhaenge) if anhaenge else "keine eingebetteten Anhänge"),
    ]
    schreibe_text_pdf(ziel, "E-Mail", kopf, str(inhalt))


def konvertiere_bild(quelle: Path, ziel: Path) -> None:
    from PIL import Image, ImageOps, ImageSequence

    seiten_breite, seiten_hoehe = A4
    rand = 1.5 * cm
    c = canvas.Canvas(str(ziel), pagesize=A4)
    with Image.open(quelle) as original:
        for frame in ImageSequence.Iterator(original):
            frame = ImageOps.exif_transpose(frame.copy()).convert("RGBA")
            bild = Image.new("RGB", frame.size, "white")
            bild.paste(frame, mask=frame.getchannel("A"))
            breite, hoehe = bild.size
            faktor = min((seiten_breite - 2 * rand) / breite, (seiten_hoehe - 2 * rand) / hoehe)
            zeich_breite, zeich_hoehe = breite * faktor, hoehe * faktor
            c.drawImage(ImageReader(bild), (seiten_breite - zeich_breite) / 2,
                        (seiten_hoehe - zeich_hoehe) / 2, width=zeich_breite,
                        height=zeich_hoehe, preserveAspectRatio=True, mask="auto")
            c.showPage()
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
    if quelle.suffix.lower() in TEXT_ENDUNGEN:
        ziel = ziel_ordner / f"{quelle.stem}.pdf"
        konvertiere_text(quelle, ziel)
        return ziel
    if quelle.suffix.lower() in HTML_ENDUNGEN:
        ziel = ziel_ordner / f"{quelle.stem}.pdf"
        konvertiere_html(quelle, ziel)
        return ziel
    if quelle.suffix.lower() in EMAIL_ENDUNGEN:
        ziel = ziel_ordner / f"{quelle.stem}.pdf"
        konvertiere_email(quelle, ziel)
        return ziel
    raise RuntimeError(f"Dateityp {quelle.suffix or '[ohne Endung]'} wird nicht automatisch konvertiert")


def lese_anlagenplan(pfad: Path, eingang: Path, hauptdokument: Optional[Path]) -> dict[str, dict[str, str]]:
    """Der Plan ordnet Originalpfade zu; ausgelassene Dateien benötigen einen Grund."""
    plan: dict[str, dict[str, str]] = {}
    with pfad.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, delimiter=";")
        felder = ["quelle", "anlage", "beschreibung", "auslassen_grund"]
        if reader.fieldnames != felder:
            raise ValueError("Anlagenplan benötigt genau: quelle;anlage;beschreibung;auslassen_grund")
        for nummer, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Anlagenplan Zeile {nummer}: falsche Spaltenzahl")
            row = {key: value.strip() for key, value in row.items()}
            rel = Path(row["quelle"])
            quelle = eingang / rel
            if not row["quelle"] or rel.is_absolute() or ".." in rel.parts or "\\" in row["quelle"]:
                raise ValueError(f"Anlagenplan Zeile {nummer}: relativen Originalpfad verwenden")
            if (not quelle.resolve().is_relative_to(eingang) or not quelle.is_file()
                    or any((eingang / Path(*rel.parts[:i])).is_symlink() for i in range(1, len(rel.parts) + 1))):
                raise ValueError(f"Anlagenplan Zeile {nummer}: Quelle fehlt oder liegt außerhalb des Eingangs")
            if any(part.startswith(".") for part in rel.parts) or quelle.resolve() == pfad.resolve():
                raise ValueError(f"Anlagenplan Zeile {nummer}: keine verborgene Datei oder den Plan selbst zuordnen")
            if hauptdokument and quelle.resolve() == hauptdokument.resolve():
                raise ValueError("Das Hauptdokument wird separat übergeben, nicht als Anlage zugeordnet")
            key = rel.as_posix()
            if key in plan:
                raise ValueError(f"Anlagenplan: Quelle doppelt zugeordnet: {key}")
            if bool(row["anlage"]) == bool(row["auslassen_grund"]):
                raise ValueError(f"Anlagenplan Zeile {nummer}: entweder Kennung oder Auslassungsgrund angeben")
            if row["anlage"]:
                match = KENNUNG_REGEX.fullmatch(row["anlage"])
                if not match or int(match.group("nummer")) < 1:
                    raise ValueError(f"Anlagenplan Zeile {nummer}: ungültige Anlagenkennung")
                row.update(match.groupdict())
            plan[key] = row
    if not plan:
        raise ValueError("Anlagenplan ist leer")
    return plan


def lese_anlagen(
    eingang: Path,
    praefix: str,
    temp: Path,
    konvertieren: bool,
    hauptdokument: Optional[Path],
    plan: Optional[dict[str, dict[str, str]]] = None,
    plan_pfad: Optional[Path] = None,
) -> tuple[list[Anlage], list[Befund]]:
    anlagen: list[Anlage] = []
    befunde: list[Befund] = []
    haupt_resolved = hauptdokument.resolve() if hauptdokument else None

    for quelle in sorted(eingang.rglob("*"), key=lambda p: p.relative_to(eingang).as_posix().lower()):
        if quelle.is_symlink():
            befunde.append(Befund("STOP", quelle.relative_to(eingang).as_posix(), "Symbolische Verknüpfung nicht verarbeitet; Original ausdrücklich bereitstellen"))
            continue
        if not quelle.is_file():
            continue
        quelle_relativ = quelle.relative_to(eingang)
        if any(part.startswith(".") for part in quelle_relativ.parts):
            continue
        if haupt_resolved and quelle.resolve() == haupt_resolved:
            continue
        if plan_pfad and quelle.resolve() == plan_pfad.resolve():
            continue
        if plan is not None:
            zuordnung = plan.get(quelle_relativ.as_posix())
            if zuordnung is None:
                befunde.append(Befund("STOP", quelle_relativ.as_posix(), "Datei fehlt im Anlagenplan; zuordnen oder begründet auslassen"))
                continue
            if zuordnung["auslassen_grund"]:
                befunde.append(Befund("HINWEIS", quelle_relativ.as_posix(), "Bewusst nicht eingereicht: " + zuordnung["auslassen_grund"]))
                continue
            daten = zuordnung
        else:
            match = ANLAGEN_REGEX.match(quelle.stem)
            if not match:
                befunde.append(Befund("STOP", quelle_relativ.as_posix(), "Keine Anlagenkennung; im Anlagenplan zuordnen oder begründet auslassen"))
                continue
            daten = match.groupdict()
        if daten["praefix"].upper() != praefix.upper() or int(daten["nummer"]) < 1:
            befunde.append(Befund("STOP", quelle_relativ.as_posix(), f"Anlagenkennung passt nicht zum Kreis {praefix.upper()} ab Nummer 1"))
            continue
        try:
            pdf = als_pdf(quelle, temp, konvertieren)
        except Exception as exc:  # noqa: BLE001 - Befund soll vollständig protokolliert werden
            befunde.append(Befund("STOP", quelle_relativ.as_posix(), str(exc)))
            continue
        anlagen.append(
            Anlage(
                quelle=quelle,
                quelle_relativ=quelle_relativ.as_posix(),
                arbeits_pdf=pdf,
                praefix=daten["praefix"].upper(),
                nummer=int(daten["nummer"]),
                suffix=daten["suffix"].lower(),
                beschreibung=(daten["beschreibung"] or quelle.stem).replace("-", " ").replace("_", " "),
                quell_hash=sha256(quelle),
            )
        )

    anlagen.sort(key=lambda a: a.sortier_schluessel)
    quell_hashes = {a.quell_hash for a in anlagen}
    ausgelassen = {sha256(eingang / key): row["auslassen_grund"]
                   for key, row in (plan or {}).items() if row["auslassen_grund"]}
    for anlage in anlagen:
        if anlage.quelle.suffix.lower() != ".eml":
            continue
        nachricht = BytesParser(policy=policy.default).parsebytes(anlage.quelle.read_bytes())
        for part in email_anhaenge(nachricht):
            name = part.get_filename() or "ohne Dateiname"
            payload = part.get_payload(decode=True)
            if part.get_content_disposition() != "attachment":
                befunde.append(Befund("WARNUNG", anlage.quelle_relativ, f"Eingebetteter E-Mail-Inhalt {name}: Textausgabe ersetzt keine visuelle Wiedergabe"))
            digest = hashlib.sha256(payload).hexdigest() if payload is not None else ""
            if digest in ausgelassen:
                befunde.append(Befund("HINWEIS", anlage.quelle_relativ, f"E-Mail-Anhang {name} ausdrücklich ausgeschlossen: {ausgelassen[digest]}"))
            elif digest not in quell_hashes:
                befunde.append(Befund("STOP", anlage.quelle_relativ, f"E-Mail-Anhang {name} ist nicht als eigene unveränderte Anlagenquelle zugeordnet oder begründet ausgeschlossen"))
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
    if any(b.stufe == "STOP" for b in befunde):
        raise RuntimeError("PDF enthält unzulässige aktive oder eingebettete Inhalte; keine Versandausgabe erzeugt")
    fields = reader.get_fields() or {}
    if any(field.get("/FT") == "/Sig" and field.get("/V") for field in fields.values()) or reader.trailer["/Root"].get("/Perms"):
        raise RuntimeError("Signierte oder zertifizierte PDF nicht stempeln; Original erhalten und gesonderte Zuordnung abstimmen")
    # Signaturfelder können in fehlerhaften Dateien nur als Seiten-Widgets vorhanden sein.
    for page in reader.pages:
        for ref in page.get("/Annots", []):
            widget = ref.get_object()
            field = widget
            art, wert = field.get("/FT"), field.get("/V")
            seen = {id(field)}
            while field.get("/Parent"):
                field = field["/Parent"].get_object()
                if id(field) in seen:
                    raise RuntimeError("Zyklische PDF-Feldstruktur; manuell prüfen")
                seen.add(id(field))
                art = art or field.get("/FT")
                wert = wert or field.get("/V")
            if art == "/Sig" and wert:
                raise RuntimeError("PDF mit Signaturfeld nicht verändern; Signaturstatus manuell prüfen")
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
    if any(b.stufe == "STOP" for b in befunde):
        raise RuntimeError("Hauptdokument enthält aktive oder eingebettete Inhalte; keine Versandausgabe erzeugt")
    shutil.copy2(pdf, ziel)
    PdfReader(str(ziel), strict=True)
    return seiten, textzeichen, befunde


def pruefe_nummernfolge(anlagen: list[Anlage]) -> list[Befund]:
    befunde: list[Befund] = []
    gesehen: set[tuple[int, str]] = set()
    for anlage in anlagen:
        key = anlage.sortier_schluessel
        if key in gesehen:
            befunde.append(Befund("STOP", anlage.quelle_relativ, f"Anlagenbezeichnung {anlage.bezeichnung} ist doppelt"))
        gesehen.add(key)
    nummern = sorted({a.nummer for a in anlagen})
    if nummern:
        erwartet = list(range(nummern[0], nummern[-1] + 1))
        fehlend = sorted(set(erwartet) - set(nummern))
        if fehlend:
            befunde.append(Befund("STOP", "Anlagenfolge", f"Nummernlücke: {', '.join(map(str, fehlend))}"))
    hash_quellen: dict[str, list[str]] = {}
    for anlage in anlagen:
        hash_quellen.setdefault(anlage.quell_hash, []).append(anlage.quelle_relativ)
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
                "quelle": a.quelle_relativ,
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
                "quelle": a.quelle_relativ,
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
            zeilen.append(f"| {b.stufe} | {markdown_zelle(b.datei)} | {markdown_zelle(b.text)} |")
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


def personen_schluessel(name: str) -> str:
    text = ascii_segment(name).lower()
    teile = [
        teil
        for teil in text.split("_")
        if teil not in {"rechtsanwalt", "rechtsanwaeltin", "ra", "dr", "prof", "professor"}
    ]
    return "_".join(teile)


def schreibe_freigabevermerk(
    ziel: Path,
    metadaten: dict[str, object],
    haupt_hash: str,
    stop_anzahl: int,
    warn_anzahl: int,
) -> None:
    status = "STOP - nicht freigegeben" if stop_anzahl else "technisch vorbereitet - anwaltliche Freigabe erforderlich"
    zeilen = [
        "# Freigabevermerk Versandmappe",
        "",
        "## 1. Status",
        "",
        f"- Status: {status}",
        f"- Stop-Befunde: {stop_anzahl}",
        f"- Warnungen: {warn_anzahl}",
        "",
        "## 2. Verfahren und Dateien",
        "",
        f"- Gericht: {metadaten['gericht'] or '[offen]'}",
        f"- Aktenzeichen: {metadaten['aktenzeichen'] or '[offen]'}",
        f"- Frist: {metadaten['frist'] or '[offen]'}",
        f"- Hauptdokument: {metadaten['hauptdokument'] or '[fehlt]'}",
        f"- SHA-256 Hauptdokument: {haupt_hash or '[fehlt]'}",
        f"- Dateien insgesamt: {metadaten['dateien']}",
        f"- Gesamtgröße: {metadaten['bytes_gesamt']} Bytes",
        f"- Dateinamensprofil: {metadaten['profil']}",
        "",
        "## 3. Verantwortung und Formroute",
        "",
        f"- Verantwortende Person: {metadaten['verantwortlich'] or '[offen]'}",
        f"- Tatsächlicher Versender: {metadaten['versender'] or '[offen]'}",
        f"- Signaturweg: {metadaten['signaturweg']}",
        f"- Qualifizierte elektronische Signatur manuell geprüft: {'ja' if metadaten['qes_geprueft'] else 'nein oder nicht erforderlich'}",
        f"- Sichtkontrolle aller Ausgabeseiten bestätigt: {'ja' if metadaten['sichtpruefung_bestaetigt'] else 'nein'}",
        "",
        "## 4. Schlussfreigabe",
        "",
        "- [ ] Empfänger und Aktenzeichen im Versanddialog geprüft.",
        "- [ ] Finale Schriftsatzfassung und Anlagenfolge geprüft.",
        "- [ ] Signaturroute durch die verantwortende Person bestätigt.",
        "- [ ] Automatisierte Eingangsbestätigung wird nach Versand geprüft und gespeichert.",
        "",
        "Freigabe durch: [Name, Datum, Uhrzeit]",
    ]
    ziel.write_text("\n".join(zeilen) + "\n", encoding="utf-8")


def schreibe_eingangskontrolle(ziel: Path, metadaten: dict[str, object]) -> None:
    zeilen = [
        "# Eingangskontrolle",
        "",
        "## 1. Versanddaten",
        "",
        f"- Gericht: {metadaten['gericht'] or '[offen]'}",
        f"- Aktenzeichen: {metadaten['aktenzeichen'] or '[offen]'}",
        f"- Frist: {metadaten['frist'] or '[offen]'}",
        f"- Erwartete Dateien: {metadaten['dateien']}",
        f"- Erwartete Gesamtgröße: {metadaten['bytes_gesamt']} Bytes",
        "",
        "## 2. Prüfung nach Versand",
        "",
        "| Teil | Versandzeit | Eingangszeit | Status | Dateien | Empfänger geprüft | Prüfender | Frist erledigt |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
        "| 1 von 1 | offen | offen | offen | offen | nein | offen | nein |",
        "",
        "Die Frist erst nach positiver Prüfung der automatisierten Eingangsbestätigung erledigen.",
    ]
    ziel.write_text("\n".join(zeilen) + "\n", encoding="utf-8")


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Erzeugt eine beA-Versandmappe mit getrennten PDF-Anlagen und Preflight-Bericht.")
    parser.add_argument("--eingang", required=True, type=Path, help="Ordner mit Anlagen")
    parser.add_argument("--ausgang", required=True, type=Path, help="Neuer Zielordner")
    parser.add_argument("--praefix", default="K", help="Nummernkreis K, B, AST oder AG")
    parser.add_argument("--hauptdokument", type=Path, help="Finaler Schriftsatz als PDF oder konvertierbare Office-Datei")
    parser.add_argument("--anlagenplan", type=Path, help="UTF-8-CSV: quelle;anlage;beschreibung;auslassen_grund; Originalnamen bleiben unverändert")
    parser.add_argument("--ohne-anlagen", action="store_true", help="Bestätigter Schriftsatz ohne Anlagen; ersetzt keine Klärung unbekannter Dateien")
    parser.add_argument("--dokumentart", default="Schriftsatz_mit_Antraegen", help="Sprechende Art des Hauptdokuments")
    parser.add_argument("--schriftsatz", help="Abwärtskompatibler Titel für Anlagenverzeichnis")
    parser.add_argument("--profil", choices=["kanzlei-ascii", "gericht-sicher", "berlin", "nrw", "bund"], default="kanzlei-ascii")
    parser.add_argument("--datum", default=date.today().strftime("%Y%m%d"), help="Dokumentdatum als JJJJMMTT")
    parser.add_argument("--gericht", default="", help="Empfängergericht für den Prüfbericht")
    parser.add_argument("--aktenzeichen", default="", help="Gerichtliches Aktenzeichen oder Neueingang")
    parser.add_argument("--frist", default="", help="Frist mit Datum und Uhrzeit für Freigabe und Eingangskontrolle")
    parser.add_argument("--verantwortlich", default="", help="Person, die den Schriftsatz verantwortet")
    parser.add_argument("--versender", default="", help="Person, die den Versand tatsächlich auslöst")
    parser.add_argument("--signaturweg", choices=["offen", "persoenlich-sicher", "qes"], default="offen")
    parser.add_argument("--qes-geprueft", action="store_true", help="Manuelle Prüfung der qualifizierten elektronischen Signatur bestätigen")
    parser.add_argument("--sichtpruefung-bestaetigt", action="store_true", help="Visuelle Prüfung aller erzeugten PDF-Seiten bestätigen")
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
    if (ausgang == eingang or ausgang.is_relative_to(eingang) or eingang.is_relative_to(ausgang)
            or (args.hauptdokument and args.hauptdokument.resolve().is_relative_to(ausgang))
            or (args.anlagenplan and args.anlagenplan.resolve().is_relative_to(ausgang))):
        print("FEHLER: Eingangs-, Ausgangs- und Originalpfade müssen getrennt sein; nichts verändert", file=sys.stderr)
        return 2
    if ausgang.exists() and not ausgang.is_dir():
        print("FEHLER: Ausgabeziel ist kein Verzeichnis", file=sys.stderr)
        return 2
    try:
        plan = lese_anlagenplan(args.anlagenplan, eingang, args.hauptdokument) if args.anlagenplan else None
    except (OSError, ValueError, csv.Error) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
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
    if not args.frist.strip():
        alle_befunde.append(Befund(fehlstufe, "Versanddaten", "Frist mit Datum und Uhrzeit ist nicht angegeben"))
    if not args.verantwortlich.strip():
        alle_befunde.append(Befund("STOP", "Signaturweg", "verantwortende Person ist nicht angegeben"))
    if not args.versender.strip():
        alle_befunde.append(Befund("STOP", "Signaturweg", "tatsächlicher Versender ist nicht angegeben"))
    if args.signaturweg == "offen":
        alle_befunde.append(Befund("STOP", "Signaturweg", "persönlicher sicherer Versand oder qualifizierte elektronische Signatur ist nicht festgelegt"))
    if (
        args.signaturweg == "persoenlich-sicher"
        and args.verantwortlich.strip()
        and args.versender.strip()
        and personen_schluessel(args.verantwortlich) != personen_schluessel(args.versender)
    ):
        alle_befunde.append(Befund("STOP", "Signaturweg", "verantwortende Person und tatsächlicher Versender stimmen beim persönlichen sicheren Versand nicht überein"))
    if args.signaturweg == "qes" and not args.qes_geprueft:
        alle_befunde.append(Befund("STOP", "Signaturweg", "qualifizierte elektronische Signatur ist nicht als manuell geprüft bestätigt"))
    if not args.sichtpruefung_bestaetigt:
        alle_befunde.append(Befund("STOP", "Sichtkontrolle", "visuelle Prüfung aller erzeugten PDF-Seiten ist noch nicht bestätigt"))

    with tempfile.TemporaryDirectory(prefix="bea-produktion-") as tmp:
        temp = Path(tmp)
        anlagen, befunde = lese_anlagen(
            eingang,
            praefix,
            temp,
            not args.keine_konvertierung,
            args.hauptdokument,
            plan,
            args.anlagenplan,
        )
        alle_befunde.extend(befunde)
        alle_befunde.extend(pruefe_nummernfolge(anlagen))
        if not anlagen and not args.ohne_anlagen:
            alle_befunde.append(Befund("STOP", "Anlagen", "keine verarbeitbare Anlage gefunden"))
        if anlagen and args.ohne_anlagen:
            alle_befunde.append(Befund("STOP", "Anlagen", "Anlagen vorhanden, obwohl ein Schriftsatz ohne Anlagen bestätigt wurde"))

        stellen = 3 if len(anlagen) >= 100 else 2
        for index, anlage in enumerate(anlagen, start=1):
            anlage.ausgabe_name = ausgabe_name_anlage(anlage, index, stellen, args.profil, args.datum)
        namen = Counter(a.ausgabe_name.casefold() for a in anlagen)
        kennungen = Counter(a.sortier_schluessel for a in anlagen)
        for anlage in anlagen:
            if kennungen[anlage.sortier_schluessel] > 1 or namen[anlage.ausgabe_name.casefold()] > 1:
                alle_befunde.append(Befund("STOP", anlage.quelle_relativ, "Mehrdeutige Kennung oder kollidierender Versandname; keine Fassung ausgewählt"))
                continue
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
                ziel.unlink(missing_ok=True)
                anlage.befunde.append(Befund("STOP", anlage.quelle_relativ, str(exc)))
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
                (versand / haupt_name).unlink(missing_ok=True)
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
    if len(versand_dateien) >= 950 or bytes_gesamt >= 190_000_000:
        alle_befunde.append(Befund("WARNUNG", "Versandpaket", "Geringe Versandreserve: automatisch erzeugte Nachrichten-, Struktur- und Signaturdateien mitzählen; fertige Nachricht im Versanddialog prüfen"))
    if args.stempel_seiten != "alle":
        alle_befunde.append(Befund("WARNUNG", "Anlagenstempel", "nur die erste Seite wurde gestempelt; Berliner Gerichtshinweis empfiehlt sämtliche Seiten"))

    haupt_hash = sha256(versand / haupt_name) if haupt_name and (versand / haupt_name).is_file() else ""
    metadaten: dict[str, object] = {
        "gericht": args.gericht,
        "aktenzeichen": args.aktenzeichen,
        "frist": args.frist,
        "profil": args.profil,
        "datum": args.datum,
        "praefix": praefix,
        "dokumentart": args.dokumentart,
        "hauptdokument": haupt_name,
        "sha256_hauptdokument": haupt_hash,
        "sha256_hauptquelle": sha256(args.hauptdokument) if args.hauptdokument else "",
        "anlagenplan": str(args.anlagenplan) if args.anlagenplan else "",
        "ohne_anlagen": args.ohne_anlagen,
        "stempel_alle_seiten": args.stempel_seiten == "alle",
        "dateien": len(versand_dateien),
        "bytes_gesamt": bytes_gesamt,
        "verantwortlich": args.verantwortlich,
        "versender": args.versender,
        "signaturweg": args.signaturweg,
        "qes_geprueft": args.qes_geprueft,
        "sichtpruefung_bestaetigt": args.sichtpruefung_bestaetigt,
        "befunde": [b.__dict__ for b in alle_befunde],
        "status": "STOP" if any(b.stufe == "STOP" for b in alle_befunde) else "TECHNISCH_VORBEREITET",
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

    stop_anzahl = sum(1 for b in alle_befunde if b.stufe == "STOP")
    warn_anzahl = sum(1 for b in alle_befunde if b.stufe == "WARNUNG")
    schreibe_freigabevermerk(
        intern / "Freigabevermerk.md",
        metadaten,
        haupt_hash,
        stop_anzahl,
        warn_anzahl,
    )
    schreibe_eingangskontrolle(intern / "Eingangskontrolle.md", metadaten)

    print(f"Versandordner: {versand}")
    print(f"Interne Prüfunterlagen: {intern}")
    print(f"Dateien: {len(versand_dateien)}, Gesamtgröße: {bytes_gesamt} Bytes")
    print(f"Befunde: {stop_anzahl} Stop, {warn_anzahl} Warnung")
    if stop_anzahl and args.strict:
        return 3
    return 0 if not stop_anzahl else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
