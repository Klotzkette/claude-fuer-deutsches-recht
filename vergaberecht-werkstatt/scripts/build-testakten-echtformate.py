#!/usr/bin/env python3
"""Erzeugt lebensechte Dateiformate fuer alle Testakten-Aktenstuecke.

Grundregel (verbindlich, siehe CLAUDE.md und testakten/README.md):
Das Repository bewahrt den lebensnahen Datenbestand einer echten Akte mit
Word-Dokumenten, E-Mails, Excel-Anlagen, PDFs, CSV/XML-Rohdaten und Bildern.
Die kuratierten Release-ZIPs sind dagegen flach und enthalten ausschliesslich
DOCX, XLSX und PDF. Markdown und technische Rohformate bleiben als Quellen
und Formatproben im Repository; ihre lesbaren Inhalte werden als Einzel-PDF
oder bearbeitbare Office-Fassung ausgeliefert.

Dieser Generator liest jedes nummerierte Aktenstueck (NN_*.md) und erzeugt
deterministisch daraus:

- eml/NN_*.eml   wenn das Stueck Korrespondenz ist (Schreiben, Bieterfrage,
                 Antwort, Mitteilung, Uebersendung, Ablehnung)
- docx/NN_*.docx sonst (Vermerke, Schriftsaetze, Beschluesse, Protokolle),
                 mit Briefkopf aus dem aktenmeta-Kommentar der Quelle oder
                 aus der Beteiligten-Karte der Akte
- xlsx/NN_*.xlsx zusaetzlich als Anlage, wenn das Stueck tabellenlastig ist
                 (mindestens zwei Markdown-Tabellen oder Matrix/LV/Kosten)

Inhaltstreue: Der Text stammt unveraendert aus derselben Markdown-Quelle,
aus der auch Einzel- und Gesamt-PDF gebaut werden.

Bereits handgefertigte Gegenstuecke (z. B. die eml/docx der IT-SIG-2-Akte)
werden erkannt und nicht doppelt erzeugt.

Aufruf:
  python3 scripts/build-testakten-echtformate.py                 # alle Akten
  python3 scripts/build-testakten-echtformate.py <name1> <name2> # gezielt
Idempotent: ueberschreibt nur selbst erzeugte Zieldateien.
"""
from __future__ import annotations

import argparse
import hashlib
import csv
import re
import sys
from datetime import datetime, timedelta, timezone
from email import policy as email_policy
from email.message import EmailMessage
from email.utils import format_datetime
from functools import lru_cache
from pathlib import Path
from zoneinfo import ZoneInfo

import random
import textwrap
import zipfile
from xml.etree import ElementTree as ET

import docx
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.table import Table as ExcelTable, TableStyleInfo
from openpyxl.utils import get_column_letter
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt as PptPt

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
SKIP_DIRS = {"megaprompts", "formatvorlagen-paradebeispiele"}
FIXED_PACKAGE_DATETIME = datetime(2000, 1, 1)
FIXED_PACKAGE_TIME = (2000, 1, 1, 0, 0, 0)
EML_POLICY = email_policy.SMTP.clone(max_line_length=76, utf8=False)
BERLIN_TZ = ZoneInfo("Europe/Berlin")
FIXED_PDF_TIME = datetime(2000, 1, 1, tzinfo=timezone.utc).utctimetuple()
CORE_PROPERTIES_NS = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DCTERMS_NS = "http://purl.org/dc/terms/"
ET.register_namespace("cp", CORE_PROPERTIES_NS)
ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
ET.register_namespace("dcterms", DCTERMS_NS)
ET.register_namespace("dcmitype", "http://purl.org/dc/dcmitype/")
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

# Geaenderte Quellnamen muessen auch in den abgeleiteten Arbeitsformaten
# nachgezogen werden. Sonst bleiben rechtlich ueberholte Dokumente im
# Downloadpaket, obwohl die Markdown-Quelle bereits korrigiert ist.
RENAMED_SOURCE_STEMS: dict[str, dict[str, str]] = {
    "04-it-beratung-ministerium-musterland": {
        "06_olg_beschwerde_skizze": "06_rechtsmittel_und_kostenvermerk",
    },
    "06-konkurrentenrechtsschutz-rechenzentrum-musterkreis": {
        "12_sofortige_beschwerde_olg": "13_sofortige_beschwerde_olg",
    },
    "it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung": {
        "17_beschluss_vk_bund": "17_beschluss_vk_mv",
        "18_sofortige_beschwerde_olg_duesseldorf": "18_sofortige_beschwerde_olg_rostock",
        "20_de_facto_vergabe_klage": "20_de_facto_vergabe_nachpruefungsantrag",
    },
}

# Nur diese fachlich geprüften Bestandsdateien ersetzen eine ansonsten aus der
# Markdown-Quelle erzeugte Zieldatei. Eine ähnliche XLSX oder ein ähnlich
# benannter anderer Beschluss ist ausdrücklich kein Gegenstück.
HANDCRAFTED_COUNTERPARTS: dict[str, dict[str, tuple[str, ...]]] = {
    "it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung": {
        "06_ausschlussschreiben_vergabestelle": (
            "eml/01_ausschlussschreiben_vergabestelle.eml",
        ),
        "07_ruege_cybershield_160_gwb": (
            "docx/ruege_160_gwb.docx",
        ),
        "09_nachpruefungsantrag_vk_mv": (
            "docx/nachpruefungsantrag_vk.docx",
        ),
        "15_vergleichsvorschlag_vergabestelle": (
            "docx/vergleichsvorschlag_vk.docx",
        ),
    },
}

LEGACY_OFFICE_METADATA = {
    "it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung": {
        "vergleichsvorschlag_vk.docx": {
            "title": "Vergleichsvorschlag der 3. Vergabekammer Mecklenburg-Vorpommern",
            "subject": "Vergleichsvorschlag | Az. 3 VK 4/26",
            "author": "3. Vergabekammer Mecklenburg-Vorpommern",
        },
        "nachpruefungsantrag_vk.docx": {
            "title": "Nachprüfungsantrag CyberShield Defense GmbH",
            "subject": "Nachprüfungsantrag | Az. 3 VK 4/26",
            "author": "Bährens Vergaberecht Rechtsanwaltsgesellschaft mbH",
        },
        "ruege_160_gwb.docx": {
            "title": "Rüge nach § 160 Abs. 3 GWB",
            "subject": "Rügeschreiben | Az. LH-SN-Cyber-SOC-NSV-2026",
            "author": "Bährens Vergaberecht Rechtsanwaltsgesellschaft mbH",
        },
        "eignungsreferenzen_cybershield.xlsx": {
            "title": "Eignungsreferenzen CyberShield Defense GmbH",
            "subject": "Eignungsnachweise | Az. LH-SN-Cyber-SOC-NSV-2026",
            "author": "CyberShield Defense GmbH",
        },
        "bewertungsmatrix_zuschlagskriterien.xlsx": {
            "title": "Bewertungsmatrix der Zuschlagskriterien",
            "subject": "Wertungsmatrix | Az. LH-SN-Cyber-SOC-NSV-2026",
            "author": "Landeshauptstadt Schwerin - SDS Stadtwirtschaftliche Dienstleistungen",
        },
    }
}

# E-Mail-Format fuer Korrespondenz-Stuecke (Dateiname oder Dokumenttyp).
EML_KEYWORDS = (
    "bieterfrage", "antwort", "mail", "uebersendung", "mitteilung",
    "schreiben", "ablehnung", "annahme", "anfrage", "information",
)
# Zusaetzliche Excel-Anlage fuer tabellenlastige Stuecke.
XLSX_KEYWORDS = (
    "matrix", "kalkulation", "kosten", "flaechen", "referenzliste",
    "wertung", "preisblatt", "schaetzung", "lv",
)
# Stuecke, die im Alltag als Scan/Fax hereinkommen: graphisches Bild-PDF
# ohne Textebene (max. zwei je Akte, sonst erstes Stueck als Fallback).
SCAN_KEYWORDS = (
    "ruege", "bekanntmachung", "beschluss", "schreiben", "protokoll",
)
# Ein Stueck je Akte zusaetzlich als Praesentation (Fallback: erstes Stueck).
PPTX_KEYWORDS = (
    "markterkundung", "wertung", "fallvarianten", "analyse", "angebot",
    "strategie", "kalkulation", "sachverhalt", "bedarfsvermerk",
)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def load_font(size: int, *, bold: bool = False, serif: bool = False):
    names = []
    if serif:
        names.extend(["DejaVuSerif-Bold.ttf" if bold else "DejaVuSerif.ttf"])
    names.extend(["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"])
    candidates = [FONT_DIR / name for name in names]
    candidates.extend(
        Path(p)
        for p in (
            "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf" if serif and bold else "",
            "/System/Library/Fonts/Supplemental/Times New Roman.ttf" if serif and not bold else "",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/Library/Fonts/Arial Unicode.ttf",
        )
        if p
    )
    for candidate in candidates:
        if candidate.exists():
            try:
                return ImageFont.truetype(str(candidate), size)
            except OSError:
                continue
    return ImageFont.load_default()

# Beteiligten-Karte je Akte: Rolle -> (Organisation, Adresse, Mail-Domain).
# Genutzt als Fallback, wenn ein Aktenstueck keinen aktenmeta-Kommentar hat.
PARTEIEN: dict[str, dict[str, tuple[str, str, str]]] = {
    "01-reinigung-grundschule-musterstadt": {
        "vergabestelle": ("Stadt Musterstadt - Zentrale Vergabestelle",
                          "Rathausplatz 1, 99999 Musterstadt", "stadt-musterstadt.example.de"),
        "bieter": ("Sauber & Klar Gebäudedienste GmbH",
                   "Industrieweg 12, 99999 Musterstadt", "sauber-klar.example.de"),
        "kanzlei": ("Rechtsanwälte Hesse & Partner",
                    "Marktstraße 18, 99999 Musterstadt", "hesse-partner.example.de"),
    },
    "02-laptopbeschaffung-landesamt-musterland": {
        "vergabestelle": ("Landesamt für Digitalisierung Musterland",
                          "Musterallee 10, 99000 Musterstadt", "lad-musterland.example.de"),
        "bieter": ("TechLine Systeme GmbH",
                   "Rechenzentrumstraße 4, 99084 Musterstadt", "techline-systeme.example.de"),
        "kanzlei": ("Kanzlei Dr. Rademacher Vergaberecht",
                    "Behördenring 7, 99084 Musterstadt", "rademacher-vergabe.example.de"),
    },
    "03-bauleistung-stadthalle-musterstadt": {
        "vergabestelle": ("Stadt Musterstadt - Fachbereich Hochbau",
                          "Bauhofstraße 4, 99999 Musterstadt", "hochbau-musterstadt.example.de"),
        "bieter": ("Hochbau Mustermann GmbH",
                   "Industriestraße 50, 88800 Musterhausen", "hochbau-mustermann.example.de"),
        "kanzlei": ("Baurecht und Vergabe Partner mbB",
                    "Theaterplatz 3, 88800 Musterhausen", "bauvergabe-partner.example.de"),
    },
    "04-it-beratung-ministerium-musterland": {
        "vergabestelle": ("Ministerium des Innern Musterland",
                          "Schlossgasse 1, 88888 Musterhausen", "mi-musterland.example.de"),
        "bieter": ("Beratung Mustertal GmbH",
                   "Campusstraße 9, 88770 Mustertal", "beratung-mustertal.example.de"),
        "kanzlei": ("Kanzlei Nordmann IT-Vergabe",
                    "Hafenstraße 22, 88770 Mustertal", "nordmann-itvergabe.example.de"),
    },
    "05-insolvenz-auftragnehmerwechsel-132-gwb": {
        "vergabestelle": ("Stadt Hafenburg - Amt für Digitalisierung",
                          "Hafenallee 12, 21079 Hafenburg", "vergabe.hafenburg.example.de"),
        "konkurrent": ("DataPortus GmbH",
                       "Speicherstraße 8, 20457 Hafenburg", "dataportus.example.de"),
        "erwerber": ("NordSys Betriebserwerber GmbH",
                     "Werftweg 3, 21129 Hafenburg", "betriebserwerber.example.de"),
        "vk": ("Vergabekammer bei der Finanzbehörde Hafenburg",
               "Postfach 30 05 30, 20305 Hafenburg", "vk.hafenburg.example.de"),
        "kanzlei": ("Kanzlei Marten & Kollegen - Vergaberecht",
                    "Alsterufer 21, 20354 Hafenburg", "marten-vergaberecht.example.de"),
    },
    "06-konkurrentenrechtsschutz-rechenzentrum-musterkreis": {
        "vergabestelle": ("Musterkreis IT-Service - Vergabestelle",
                          "Kreishaus 1, 44100 Musterstadt", "musterkreis-it.example.de"),
        "konkurrent": ("Datacenter Westfalen GmbH",
                       "Speicherstraße 14, 44147 Dortmund", "datacenter-westfalen.example.de"),
        "bieter": ("CloudNord AG",
                   "Hafenweg 9, 28195 Bremen", "cloudnord.example.de"),
        "vk": ("Vergabekammer Westfalen",
               "Albrecht-Thaer-Straße 9, 48147 Münster", "vk-westfalen.example.de"),
        "kanzlei": ("Kanzlei Ahlers und Stein - Vergaberecht",
                    "Phoenixseestraße 6, 44263 Dortmund", "ahlers-stein.example.de"),
    },
    "it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung": {
        "vergabestelle": ("Landeshauptstadt Schwerin - SDS Stadtwirtschaftliche Dienstleistungen",
                          "Am Grünen Tal 18, 19063 Schwerin", "sds-schwerin.de"),
        "bieter": ("CyberShield Defense GmbH",
                   "Alexanderstraße 7, 10178 Berlin", "cybershield-defense.de"),
        "kanzlei": ("Bährens Vergaberecht Rechtsanwaltsgesellschaft mbH",
                    "Unter den Linden 48, 10117 Berlin", "baehrens-vergabe.de"),
        "vk": ("3. Vergabekammer Mecklenburg-Vorpommern",
               "Johannes-Stelling-Straße 14, 19053 Schwerin", "wm.mv-regierung.de"),
        "olg": ("Oberlandesgericht Rostock - Vergabesenat",
                "Wallstraße 3, 18055 Rostock", "mv-justiz.de"),
    },
}

# Rollenerkennung aus dem Dateinamen (erste Uebereinstimmung gewinnt).
ROLLEN_MUSTER: tuple[tuple[str, str], ...] = (
    ("beschluss_vk", "vk"), ("beiladungsbeschluss", "vk"),
    ("aufklaerungsanfragen", "vk"), ("protokoll", "vk"),
    ("olg", "kanzlei"), ("klage", "kanzlei"), ("beschwerde", "kanzlei"),
    ("nachpruefungsantrag", "kanzlei"), ("erwiderung", "kanzlei"),
    ("sachverhalt", "kanzlei"), ("fallvarianten", "kanzlei"),
    ("analyse", "kanzlei"), ("kostenrechnung", "kanzlei"),
    ("dataportus", "konkurrent"), ("konkurrentenruege", "konkurrent"),
    ("cybershield", "bieter"), ("ruege", "bieter"),
    ("angebot", "bieter"), ("referenzliste", "bieter"),
    ("vergleichsannahme", "bieter"),
    ("erwerber", "erwerber"), ("fortfuehrung", "erwerber"),
    ("beiladungsantrag", "erwerber"),
    ("vergabestelle", "vergabestelle"), ("bekanntmachung", "vergabestelle"),
    ("vergabeunterlagen", "vergabestelle"), ("eignungsanforderungen", "vergabestelle"),
    ("nichtabhilfe", "vergabestelle"), ("vergleichsvorschlag", "vergabestelle"),
    ("pruefvermerk", "vergabestelle"),
)

DATUM_RE = re.compile(r"\b([0-3]?\d)\.([01]?\d)\.(20\d\d)\b")
TABLE_ROW_RE = re.compile(r"^\s*\|.+\|\s*$")
INLINE_MD_RE = re.compile(r"\*\*(.+?)\*\*")


def parse_aktenmeta(text: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    m = re.match(r"<!--\s*aktenmeta(.*?)-->", text, re.S)
    if not m:
        return meta
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip().lower()] = val.strip()
    return meta


def strip_aktenmeta(text: str) -> str:
    return re.sub(r"^<!--\s*aktenmeta.*?-->\s*", "", text, flags=re.S)


def infer_rolle(stem: str) -> str:
    low = stem.lower()
    for needle, rolle in ROLLEN_MUSTER:
        if needle in low:
            return rolle
    return "vergabestelle"


def partei(akte: str, rolle: str) -> tuple[str, str, str]:
    karte = PARTEIEN.get(akte, {})
    if rolle in karte:
        return karte[rolle]
    if karte:
        return next(iter(karte.values()))
    return ("Vergabestelle", "", "vergabestelle.example.de")


def partei_nach_absender(akte: str, absender: str) -> tuple[str, str, str] | None:
    """Ordnet einen expliziten Absender einer bekannten Aktenpartei zu."""
    def key(value: str) -> str:
        value = value.casefold().replace("ß", "ss")
        return re.sub(r"[^a-z0-9]+", " ", value).strip()

    sender_key = key(absender)
    candidates: list[tuple[int, tuple[str, str, str]]] = []
    ignored = {"gmbh", "ag", "se", "mbh", "rechtsamt", "kanzlei", "vergaberecht"}
    sender_tokens = set(sender_key.split()) - ignored
    for party in PARTEIEN.get(akte, {}).values():
        org_key = key(party[0])
        if org_key in sender_key or sender_key in org_key:
            candidates.append((100 + min(len(org_key), len(sender_key)), party))
            continue
        overlap = sender_tokens & (set(org_key.split()) - ignored)
        if len(overlap) >= 2:
            candidates.append((len(overlap), party))
    if not candidates:
        return None
    return max(candidates, key=lambda item: item[0])[1]


def derive_meta(akte: str, stem: str, text: str) -> dict[str, str]:
    """Fallback-Metadaten, wenn kein aktenmeta-Kommentar existiert."""
    rolle = infer_rolle(stem)
    org, adresse, domain = partei(akte, rolle)
    title_m = re.search(r"^#\s+(.+)$", text, re.M)
    betreff = title_m.group(1).strip() if title_m else stem.replace("_", " ")
    betreff = re.sub(r"^(Aktenstück\s+\d+\s*-\s*|\d\d\s+)", "", betreff)
    datum_m = DATUM_RE.search(text)
    datum = datum_m.group(0) if datum_m else ""
    az_m = re.search(r"\b(VK [0-9][0-9-]*/\d\d|[A-Z]{2,6}-20\d\d[A-Z0-9-]*)\b", text)
    return {
        "absender": org,
        "adresse": adresse,
        "domain": domain,
        "datum": datum,
        "betreff": betreff,
        "aktenzeichen": az_m.group(0) if az_m else "",
        "rolle": rolle,
    }


def build_meta(akte: str, md_path: Path, text: str) -> dict[str, str]:
    meta = parse_aktenmeta(text)
    fallback = derive_meta(akte, md_path.stem, text)
    out = dict(fallback)
    if meta:
        out["absender"] = meta.get("absender", fallback["absender"])
        matched_party = partei_nach_absender(akte, out["absender"])
        out["adresse"] = meta.get(
            "adresse",
            matched_party[1] if matched_party is not None else fallback["adresse"],
        )
        out["domain"] = meta.get(
            "domain",
            matched_party[2] if matched_party is not None else fallback["domain"],
        )
        out["betreff"] = meta.get("betreff", fallback["betreff"])
        out["datum"] = meta.get("datum", fallback["datum"])
        out["aktenzeichen"] = meta.get("aktenzeichen", fallback["aktenzeichen"])
        out["empfaenger"] = meta.get("empfänger", meta.get("empfaenger", ""))
        out["dokumenttyp"] = meta.get("dokumenttyp", "")
    return out


# ---------------------------------------------------------------- Markdown

def parse_blocks(text: str) -> list[tuple[str, object]]:
    """Zerlegt Markdown in (art, inhalt): heading/para/table/list."""
    blocks: list[tuple[str, object]] = []
    lines = strip_aktenmeta(text).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip() in {"---", "***", "___"}:
            i += 1
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            blocks.append(("heading", (level, line.lstrip("# ").strip())))
            i += 1
        elif TABLE_ROW_RE.match(line):
            rows: list[list[str]] = []
            while i < len(lines) and TABLE_ROW_RE.match(lines[i]):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= {"-", ":", " "} for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows))
        elif re.match(r"^\s*([-*]|\d+\.)\s+", line):
            marker = re.match(r"^\s*([-*]|\d+\.)\s+", line).group(1)  # type: ignore[union-attr]
            items: list[str] = []
            while i < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                items.append(re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i]).strip())
                i += 1
            blocks.append(("numbered-list" if marker[0].isdigit() else "list", items))
        else:
            para = [line.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") \
                    and not TABLE_ROW_RE.match(lines[i]) \
                    and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                para.append(lines[i].strip())
                i += 1
            blocks.append(("para", " ".join(para)))
    return blocks


def plain(s: str) -> str:
    s = INLINE_MD_RE.sub(r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return s


def normalize_ooxml(path: Path) -> None:
    """Schreibt OOXML-Pakete mit stabiler Reihenfolge und festen ZIP-Zeiten."""
    with zipfile.ZipFile(path, "r") as source:
        entries = [(item.filename, source.read(item)) for item in source.infolist()]
    temporary = path.with_name(f".{path.name}.deterministic")
    with zipfile.ZipFile(
        temporary,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as target:
        for filename, data in sorted(entries):
            if filename == "docProps/core.xml":
                root = ET.fromstring(data)
                for local_name in ("created", "modified"):
                    node = root.find(f"{{{DCTERMS_NS}}}{local_name}")
                    if node is not None:
                        node.text = "2000-01-01T00:00:00Z"
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            info = zipfile.ZipInfo(filename, FIXED_PACKAGE_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o600 << 16
            target.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    temporary.replace(path)


# ------------------------------------------------------------------- DOCX

def add_runs(par, text: str) -> None:
    pos = 0
    for m in INLINE_MD_RE.finditer(text):
        if m.start() > pos:
            par.add_run(plain(text[pos:m.start()]))
        par.add_run(plain(m.group(1))).bold = True
        pos = m.end()
    if pos < len(text):
        par.add_run(plain(text[pos:]))


DOCX_ACCENT = "01696F"
DOCX_TEXT = RGBColor(31, 31, 31)
DOCX_MUTED = RGBColor(100, 100, 100)
DOCX_LIGHT = "F1F3F3"
DOCX_BORDER = "B8C0C1"


def _set_style_font(style, *, size: float, bold: bool = False, color=None) -> None:
    style.font.name = "Times New Roman"
    style.font.size = Pt(size)
    style.font.bold = bold
    if color is not None:
        style.font.color.rgb = color
    style.element.rPr.rFonts.set(qn("w:ascii"), "Times New Roman")
    style.element.rPr.rFonts.set(qn("w:hAnsi"), "Times New Roman")
    style.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")


def _shade_cell(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shading = tc_pr.find(qn("w:shd"))
    if shading is None:
        shading = OxmlElement("w:shd")
        tc_pr.append(shading)
    shading.set(qn("w:fill"), fill)


def _set_cell_margins(cell, *, top: int = 80, start: int = 100,
                      bottom: int = 80, end: int = 100) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{margin}"))
        if node is None:
            node = OxmlElement(f"w:{margin}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def _set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def _prevent_table_row_split(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    if tr_pr.find(qn("w:cantSplit")) is None:
        tr_pr.append(OxmlElement("w:cantSplit"))


def _add_page_number(paragraph) -> None:
    run = paragraph.add_run()
    run.font.name = "Times New Roman"
    run.font.size = Pt(8)
    run.font.color.rgb = DOCX_MUTED
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instruction = OxmlElement("w:instrText")
    instruction.set(qn("xml:space"), "preserve")
    instruction.text = " PAGE "
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text_node = OxmlElement("w:t")
    text_node.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instruction, separate, text_node, end])


def _set_paragraph_bottom_border(paragraph, color: str = DOCX_BORDER) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = p_pr.find(qn("w:pBdr"))
    if p_bdr is None:
        p_bdr = OxmlElement("w:pBdr")
        p_pr.append(p_bdr)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "5")
    bottom.set(qn("w:color"), color)
    p_bdr.append(bottom)


def _set_table_geometry(table, widths_cm: list[float]) -> None:
    """Setzt tblW, tblGrid und tcW konsistent in DXA."""
    widths_twips = [int(Cm(width).twips) for width in widths_cm]
    tbl_pr = table._tbl.tblPr
    tbl_layout = tbl_pr.find(qn("w:tblLayout"))
    if tbl_layout is None:
        tbl_layout = OxmlElement("w:tblLayout")
        tbl_pr.append(tbl_layout)
    tbl_layout.set(qn("w:type"), "fixed")
    tbl_w = tbl_pr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(sum(widths_twips)))
    tbl_w.set(qn("w:type"), "dxa")

    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for width in widths_twips:
        grid_col = OxmlElement("w:gridCol")
        grid_col.set(qn("w:w"), str(width))
        grid.append(grid_col)

    for row in table.rows:
        for index, cell in enumerate(row.cells[:len(widths_twips)]):
            tc_pr = cell._tc.get_or_add_tcPr()
            tc_w = tc_pr.find(qn("w:tcW"))
            if tc_w is None:
                tc_w = OxmlElement("w:tcW")
                tc_pr.append(tc_w)
            tc_w.set(qn("w:w"), str(widths_twips[index]))
            tc_w.set(qn("w:type"), "dxa")


def _docx_column_widths(rows: list[list[str]], ncols: int) -> list[float]:
    available_cm = 16.0
    weights: list[float] = []
    longest_tokens: list[int] = []
    for ci in range(ncols):
        cells = [plain(row[ci]) for row in rows if ci < len(row)]
        longest = max((len(cell) for cell in cells), default=8)
        longest_token = max(
            (len(token) for cell in cells for token in re.findall(r"\S+", cell)),
            default=8,
        )
        weights.append(max(8.0, min(34.0, longest ** 0.72)))
        longest_tokens.append(longest_token)
    total = sum(weights) or 1.0
    widths = [available_cm * weight / total for weight in weights]
    if ncols <= 5:
        # Deutsche Aktenbegriffe sind oft lang. Eine dynamische Mindestbreite
        # verhindert mitten im Wort getrennte Tabellenkoepfe, ohne A4 zu sprengen.
        minima = [max(1.8, min(3.25, 0.95 + token * 0.075)) for token in longest_tokens]
        minimum_total = sum(minima)
        if minimum_total < available_cm:
            remainder = available_cm - minimum_total
            widths = [
                minimum + remainder * weight / total
                for minimum, weight in zip(minima, weights)
            ]
        else:
            widths = [available_cm * minimum / minimum_total for minimum in minima]
    scale = available_cm / sum(widths)
    return [width * scale for width in widths]


def write_docx(out: Path, meta: dict[str, str], blocks: list[tuple[str, object]]) -> None:
    # Preset: standard_business_brief. A4 und Times New Roman 10.5 sind die
    # bewussten deutschen Aktenstandard-Overrides des Presets.
    d = docx.Document()
    d.core_properties.created = FIXED_PACKAGE_DATETIME
    d.core_properties.modified = FIXED_PACKAGE_DATETIME
    d.core_properties.title = plain(meta["betreff"])
    d.core_properties.subject = (
        f"{meta.get('dokumenttyp') or 'Vergabeakte'} | "
        f"Az. {meta.get('aktenzeichen') or 'ohne Aktenzeichen'}"
    )
    d.core_properties.author = meta["absender"]
    d.core_properties.last_modified_by = meta["absender"]
    d.core_properties.category = "Vergabeakte"
    d.core_properties.keywords = ", ".join(
        value
        for value in (
            "Vergaberecht",
            meta.get("aktenzeichen", ""),
            meta.get("dokumenttyp", ""),
        )
        if value
    )

    normal = d.styles["Normal"]
    _set_style_font(normal, size=10.5, color=DOCX_TEXT)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    normal.paragraph_format.line_spacing = 1.04
    for name, size, color in (
        ("Title", 14, RGBColor(1, 105, 111)),
        ("Heading 1", 12.5, RGBColor(1, 105, 111)),
        ("Heading 2", 11, DOCX_TEXT),
        ("Heading 3", 10.5, DOCX_MUTED),
    ):
        heading = d.styles[name]
        _set_style_font(heading, size=size, bold=True, color=color)
        heading.paragraph_format.keep_with_next = True
        heading.paragraph_format.space_before = Pt(10 if name != "Title" else 0)
        heading.paragraph_format.space_after = Pt(4)
        if name == "Title":
            p_pr = heading.element.get_or_add_pPr()
            inherited_border = p_pr.find(qn("w:pBdr"))
            if inherited_border is not None:
                p_pr.remove(inherited_border)
    for name in ("List Bullet", "List Number"):
        list_style = d.styles[name]
        _set_style_font(list_style, size=10.5, color=DOCX_TEXT)
        list_style.paragraph_format.space_after = Pt(3)

    for section in d.sections:
        section.page_width = Cm(21)
        section.page_height = Cm(29.7)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)
        section.top_margin = Cm(1.8)
        section.bottom_margin = Cm(1.65)
        section.header_distance = Cm(0.75)
        section.footer_distance = Cm(0.75)

        header = section.header.paragraphs[0]
        header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        header.paragraph_format.space_after = Pt(0)
        header_run = header.add_run(meta["absender"])
        if meta.get("aktenzeichen"):
            header_run.add_text(f"  |  {meta['aktenzeichen']}")
        header_run.font.name = "Times New Roman"
        header_run.font.size = Pt(8)
        header_run.font.color.rgb = DOCX_MUTED

        footer = section.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        footer.paragraph_format.space_before = Pt(0)
        footer_run = footer.add_run("Aktenstück")
        if meta.get("aktenzeichen"):
            footer_run.add_text(f"  |  {meta['aktenzeichen']}")
        footer_run.add_text("  |  Seite ")
        footer_run.font.name = "Times New Roman"
        footer_run.font.size = Pt(8)
        footer_run.font.color.rgb = DOCX_MUTED
        _add_page_number(footer)

    masthead = d.add_table(rows=1, cols=2)
    masthead.alignment = WD_TABLE_ALIGNMENT.LEFT
    masthead.autofit = False
    _set_table_geometry(masthead, [9.7, 6.3])
    left, right = masthead.rows[0].cells
    left.width = Cm(9.7)
    right.width = Cm(6.3)
    for cell in (left, right):
        cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        _set_cell_margins(cell, top=0, bottom=100, start=0, end=0)
    left_p = left.paragraphs[0]
    left_p.paragraph_format.space_after = Pt(1)
    org_run = left_p.add_run(meta["absender"])
    org_run.bold = True
    org_run.font.name = "Times New Roman"
    org_run.font.size = Pt(12)
    org_run.font.color.rgb = RGBColor(1, 105, 111)
    if meta.get("adresse"):
        addr = left.add_paragraph(meta["adresse"])
        addr.paragraph_format.space_after = Pt(0)
        for run in addr.runs:
            run.font.size = Pt(9)
            run.font.color.rgb = DOCX_MUTED
    right_p = right.paragraphs[0]
    right_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    right_p.paragraph_format.space_after = Pt(0)
    meta_lines = [f"Datum: {meta['datum']}"]
    if meta.get("aktenzeichen"):
        meta_lines.append(f"Aktenzeichen: {meta['aktenzeichen']}")
    if meta.get("dokumenttyp"):
        meta_lines.append(meta["dokumenttyp"])
    for index, line in enumerate(meta_lines):
        run = right_p.add_run(line)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9)
        run.font.color.rgb = DOCX_MUTED
        if index + 1 < len(meta_lines):
            run.add_break()
    _set_paragraph_bottom_border(left_p, DOCX_ACCENT)
    _set_paragraph_bottom_border(right_p, DOCX_ACCENT)

    if meta.get("empfaenger"):
        sender_line = d.add_paragraph()
        sender_line.paragraph_format.space_before = Pt(10)
        sender_line.paragraph_format.space_after = Pt(2)
        sender_run = sender_line.add_run(
            f"{meta['absender']} · {meta.get('adresse', '')}".strip(" ·")
        )
        sender_run.font.name = "Times New Roman"
        sender_run.font.size = Pt(7.5)
        sender_run.font.color.rgb = DOCX_MUTED
        recipient = d.add_paragraph(meta["empfaenger"])
        recipient.paragraph_format.space_after = Pt(12)
    betreff = d.add_paragraph(style="Title")
    betreff.add_run(plain(meta["betreff"]))

    first_heading = True
    for art, inhalt in blocks:
        if art == "heading":
            level, txt = inhalt  # type: ignore[misc]
            if level == 1 and first_heading:
                first_heading = False
                continue  # Titel steht bereits im Betreff
            p = d.add_paragraph(style=f"Heading {min(3, max(1, level - 1))}")
            p.add_run(plain(txt))
        elif art == "para":
            p = d.add_paragraph()
            add_runs(p, str(inhalt))
        elif art in ("list", "numbered-list"):
            for item in inhalt:  # type: ignore[assignment]
                p = d.add_paragraph(style="List Number" if art == "numbered-list" else "List Bullet")
                add_runs(p, item)
        elif art == "table":
            rows = inhalt  # type: ignore[assignment]
            if not rows:
                continue
            ncols = max(len(r) for r in rows)
            t = d.add_table(rows=len(rows), cols=ncols)
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.LEFT
            t.autofit = False
            widths = _docx_column_widths(rows, ncols)
            _set_table_geometry(t, widths)
            if t.rows:
                _set_repeat_table_header(t.rows[0])
            for table_row in t.rows:
                _prevent_table_row_split(table_row)
            for ri, row in enumerate(rows):
                for ci in range(ncols):
                    cell = t.cell(ri, ci)
                    cell.width = Cm(widths[ci])
                    cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
                    _set_cell_margins(cell, top=60, bottom=60, start=90, end=90)
                    if ri == 0:
                        _shade_cell(cell, DOCX_ACCENT)
                    elif ri % 2 == 0:
                        _shade_cell(cell, DOCX_LIGHT)
                    txt = plain(row[ci]) if ci < len(row) else ""
                    cell.text = ""
                    run = cell.paragraphs[0].add_run(txt)
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(8.5)
                    if ri == 0:
                        run.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)
                    cell.paragraphs[0].paragraph_format.space_after = Pt(0)
                    cell.paragraphs[0].paragraph_format.keep_together = True
            spacer = d.add_paragraph()
            spacer.paragraph_format.space_after = Pt(0)
            spacer.paragraph_format.space_before = Pt(2)

    # Kurze Antrags-, Entscheidungs- und Unterschriftsblöcke dürfen nicht als
    # einzelne Restzeilen auf eine neue Seite fallen. Die Zielmenge bleibt
    # bewusst klein genug, um auf eine normale A4-Seite zu passen.
    tail: list = []
    tail_chars = 0
    for paragraph in reversed(d.paragraphs):
        if not paragraph.text.strip():
            continue
        tail.append(paragraph)
        tail_chars += len(re.sub(r"\s+", "", paragraph.text))
        if len(tail) >= 12 or tail_chars >= 700:
            break
    ordered_tail = list(reversed(tail))
    for paragraph in ordered_tail:
        paragraph.paragraph_format.keep_together = True
    for paragraph in ordered_tail[:-1]:
        paragraph.paragraph_format.keep_with_next = True
    out.parent.mkdir(parents=True, exist_ok=True)
    d.save(out)
    normalize_ooxml(out)


# -------------------------------------------------------------------- EML

def blocks_to_plaintext(blocks: list[tuple[str, object]]) -> str:
    lines: list[str] = []
    first_heading = True
    for art, inhalt in blocks:
        if art == "heading":
            level, txt = inhalt  # type: ignore[misc]
            if level == 1 and first_heading:
                first_heading = False
                continue
            lines += ["", plain(txt).upper(), ""]
        elif art == "para":
            lines += [plain(str(inhalt)), ""]
        elif art in ("list", "numbered-list"):
            prefix = "-" if art == "list" else None
            for index, item in enumerate(inhalt, start=1):  # type: ignore[union-attr]
                lines.append(f"{prefix or f'{index}.'} {plain(item)}")
            lines.append("")
        elif art == "table":
            for row in inhalt:  # type: ignore[union-attr]
                lines.append(" | ".join(plain(c) for c in row))
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def mail_adresse(name: str, domain: str) -> str:
    kurz = re.sub(r"[^a-z]", "", name.lower().split()[0])[:12] or "post"
    return f"{kurz}@{domain}"


def org_domain(org: str) -> str:
    """Fiktive Maildomain aus dem Organisationsnamen (fuer Akten ohne Karte)."""
    worte = [re.sub(r"[^a-z0-9]", "", w.lower()) for w in org.split()[:3]]
    worte = [w for w in worte if w and w not in {"gmbh", "ag", "der", "die", "das", "und", "fuer", "für"}]
    return ("-".join(worte[:2]) or "partei") + ".example.de"


def write_eml(out: Path, akte: str, meta: dict[str, str],
              blocks: list[tuple[str, object]]) -> None:
    rolle = meta.get("rolle") or infer_rolle(out.stem)
    if akte in PARTEIEN:
        org, _, domain = partei(akte, rolle)
        empf_rolle = "vergabestelle" if rolle != "vergabestelle" else "bieter"
        if empf_rolle not in PARTEIEN[akte]:
            empf_rolle = next((r for r in PARTEIEN[akte] if r != rolle), rolle)
        empf_org, _, empf_domain = partei(akte, empf_rolle)
        empfaenger = meta.get("empfaenger") or empf_org
    else:
        org = meta["absender"]
        domain = org_domain(org)
        empfaenger = meta.get("empfaenger") or "Vergabestelle"
        empf_org = empfaenger
        empf_domain = org_domain(empfaenger)

    try:
        tag, monat, jahr = DATUM_RE.match(meta["datum"]).groups()  # type: ignore[union-attr]
        basis = datetime(int(jahr), int(monat), int(tag), tzinfo=BERLIN_TZ)
    except Exception:
        basis = datetime(2026, 5, 15, tzinfo=BERLIN_TZ)
    sekunden = int(hashlib.sha256(out.name.encode()).hexdigest()[:6], 16) % 28800
    stamp = basis + timedelta(hours=8, seconds=sekunden)

    msg = EmailMessage(policy=EML_POLICY)
    msg["From"] = f'"{meta["absender"]}" <{mail_adresse(org, domain)}>'
    msg["To"] = f'"{empfaenger}" <{mail_adresse(empf_org, empf_domain)}>'
    msg["Subject"] = plain(meta["betreff"])
    msg["Date"] = format_datetime(stamp)
    msg["Message-ID"] = f"<{hashlib.sha256((akte + out.name).encode()).hexdigest()[:20]}@{domain}>"
    if meta.get("aktenzeichen"):
        msg["X-Aktenzeichen"] = meta["aktenzeichen"]
    body = blocks_to_plaintext(blocks)
    gruss = f"\nMit freundlichen Grüßen\n\n{meta['absender']}\n"
    msg.set_content("Sehr geehrte Damen und Herren,\n\n" + body + gruss)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(msg.as_bytes(policy=EML_POLICY))


# ------------------------------------------------------------------- XLSX

def write_xlsx(out: Path, meta: dict[str, str], blocks: list[tuple[str, object]]) -> bool:
    tables = [b for art, b in blocks if art == "table"]
    if not tables:
        return False
    wb = Workbook()
    wb.properties.created = FIXED_PACKAGE_DATETIME
    wb.properties.modified = FIXED_PACKAGE_DATETIME
    wb.properties.title = plain(meta["betreff"])
    wb.properties.subject = (
        f"{meta.get('dokumenttyp') or 'Tabellenanlage'} | "
        f"Az. {meta.get('aktenzeichen') or 'ohne Aktenzeichen'}"
    )
    wb.properties.creator = meta["absender"]
    wb.properties.lastModifiedBy = meta["absender"]
    wb.properties.category = "Vergabeakte"
    wb.properties.keywords = ", ".join(
        value
        for value in (
            "Vergaberecht",
            meta.get("aktenzeichen", ""),
            meta.get("dokumenttyp", ""),
        )
        if value
    )
    wb.properties.description = "Bearbeitbare Tabellenanlage zur Vergabeakte"
    wb.remove(wb.active)
    accent_fill = PatternFill("solid", fgColor="01696F")
    light_fill = PatternFill("solid", fgColor="F1F3F3")
    white_font = Font(name="Times New Roman", size=10, bold=True, color="FFFFFF")
    body_font = Font(name="Times New Roman", size=10, color="1F1F1F")
    thin_side = Side(style="thin", color="B8C0C1")
    cell_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
    for nr, rows in enumerate(tables, start=1):
        ws = wb.create_sheet(title=f"Tabelle {nr}")
        ws.sheet_view.showGridLines = False
        ws.freeze_panes = "A2"
        for ri, row in enumerate(rows, start=1):
            for ci, cell in enumerate(row, start=1):
                c = ws.cell(row=ri, column=ci, value=plain(cell))
                c.font = white_font if ri == 1 else body_font
                c.fill = accent_fill if ri == 1 else (light_fill if ri % 2 else PatternFill())
                c.border = cell_border
                c.alignment = Alignment(
                    horizontal="left",
                    vertical="top",
                    wrap_text=True,
                )
            ws.row_dimensions[ri].height = 30 if ri == 1 else 34
        for ci in range(1, max(len(r) for r in rows) + 1):
            breite = max((len(plain(r[ci - 1])) for r in rows if ci <= len(r)), default=10)
            ws.column_dimensions[get_column_letter(ci)].width = min(46, max(13, breite * 0.82 + 3))
        if rows and len(rows) > 1:
            ref = f"A1:{get_column_letter(max(len(r) for r in rows))}{len(rows)}"
            table = ExcelTable(displayName=f"AktenTabelle_{nr}", ref=ref)
            table.tableStyleInfo = TableStyleInfo(
                name="TableStyleMedium2",
                showFirstColumn=False,
                showLastColumn=False,
                showRowStripes=True,
                showColumnStripes=False,
            )
            ws.add_table(table)
            ws.auto_filter.ref = ref
        ws.print_title_rows = "1:1"
        ws.page_margins.left = 0.35
        ws.page_margins.right = 0.35
        ws.page_margins.top = 0.75
        ws.page_margins.bottom = 0.75
        ws.page_margins.header = 0.25
        ws.page_margins.footer = 0.35
        ws.page_setup.orientation = "landscape" if max(len(r) for r in rows) > 3 else "portrait"
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        kopfkennung = plain(meta.get("aktenzeichen") or meta["betreff"])
        ws.oddHeader.center.text = f"&B{kopfkennung} | Tabelle {nr}"
        ws.oddHeader.center.size = 9
        ws.oddFooter.right.text = "Seite &P von &N"
        ws.oddFooter.right.size = 8
    info = wb.create_sheet(title="Quelle", index=0)
    info.sheet_view.showGridLines = False
    info.freeze_panes = "A3"
    info.sheet_view.zoomScale = 95
    info.sheet_properties.tabColor = "01696F"
    info.merge_cells("A1:D1")
    info["A1"] = plain(meta["betreff"])
    info["A1"].font = Font(name="Times New Roman", size=14, bold=True, color="01696F")
    info["A1"].alignment = Alignment(vertical="center", wrap_text=True)
    info.row_dimensions[1].height = 46
    metadata = [
        ("Absender", meta["absender"]),
        ("Datum", meta["datum"]),
        ("Aktenzeichen", meta.get("aktenzeichen", "")),
        ("Dokumenttyp", meta.get("dokumenttyp", "Tabellenanlage")),
        ("Arbeitsblätter", str(len(tables))),
    ]
    for row_index, (label, value) in enumerate(metadata, start=3):
        info.cell(row=row_index, column=1, value=label)
        info.cell(row=row_index, column=2, value=value)
        info.cell(row=row_index, column=1).font = Font(name="Times New Roman", size=10, bold=True, color="FFFFFF")
        info.cell(row=row_index, column=1).fill = accent_fill
        info.cell(row=row_index, column=2).font = body_font
        for column in (1, 2):
            info.cell(row=row_index, column=column).border = cell_border
            info.cell(row=row_index, column=column).alignment = Alignment(vertical="top", wrap_text=True)
    info.column_dimensions["A"].width = 20
    info.column_dimensions["B"].width = 70
    info.column_dimensions["C"].width = 3
    info.column_dimensions["D"].width = 3
    info.page_setup.paperSize = info.PAPERSIZE_A4
    info.page_setup.fitToWidth = 1
    info.sheet_properties.pageSetUpPr.fitToPage = True
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    normalize_ooxml(out)
    return True


# --------------------------------------------------------------- Scan-PDF

def _scan_lines(meta: dict[str, str], blocks: list[tuple[str, object]], breite: int) -> list[tuple[str, bool]]:
    """Zeilen (text, fett) fuer die Scan-Seiten, hart umgebrochen."""
    lines: list[tuple[str, bool]] = [
        (meta["absender"], True),
        (f"Datum: {meta['datum']}" + (f"   Az: {meta['aktenzeichen']}" if meta.get("aktenzeichen") else ""), False),
        ("", False), (plain(meta["betreff"]), True), ("", False),
    ]
    first_heading = True
    for art, inhalt in blocks:
        if art == "heading":
            level, txt = inhalt  # type: ignore[misc]
            if level == 1 and first_heading:
                first_heading = False
                continue
            lines += [("", False), (plain(txt), True)]
        elif art == "para":
            for w in textwrap.wrap(plain(str(inhalt)), breite) or [""]:
                lines.append((w, False))
            lines.append(("", False))
        elif art in ("list", "numbered-list"):
            for index, item in enumerate(inhalt, start=1):  # type: ignore[union-attr]
                wrapped = textwrap.wrap(plain(item), breite - 3) or [""]
                prefix = "- " if art == "list" else f"{index}. "
                lines.append((prefix + wrapped[0], False))
                lines += [("  " + w, False) for w in wrapped[1:]]
            lines.append(("", False))
        elif art == "table":
            for row in inhalt:  # type: ignore[union-attr]
                for w in textwrap.wrap(" | ".join(plain(c) for c in row), breite) or [""]:
                    lines.append((w, False))
            lines.append(("", False))
    return lines


def write_scan_pdf(out: Path, meta: dict[str, str], blocks: list[tuple[str, object]]) -> None:
    """Graphisches Bild-PDF im Scan-Look: Rauschen, leichte Rotation,
    Scannerschatten, keine extrahierbare Textebene."""
    rnd = random.Random(int(hashlib.sha256(out.name.encode()).hexdigest()[:8], 16))
    W, H, RAND = 1240, 1754, 110  # A4 bei 150 dpi
    font = load_font(24, serif=True)
    font_b = load_font(24, bold=True, serif=True)
    zeilenhoehe, breite = 34, 88
    lines = _scan_lines(meta, blocks, breite)
    pro_seite = (H - 2 * RAND - 60) // zeilenhoehe
    seiten: list[Image.Image] = []
    for s in range(0, len(lines), pro_seite):
        img = Image.new("L", (W, H), color=246)
        d = ImageDraw.Draw(img)
        for _ in range(1400):  # Papier-/Scannerrauschen
            x, y = rnd.randrange(W), rnd.randrange(H)
            d.point((x, y), fill=rnd.randrange(190, 235))
        y = RAND
        for text, fett in lines[s:s + pro_seite]:
            if text:
                d.text((RAND, y), text, font=font_b if fett else font, fill=38)
            y += zeilenhoehe
        nr = s // pro_seite + 1
        d.text((W // 2 - 40, H - 70), f"Seite {nr}", font=font, fill=90)
        d.rectangle([0, 0, 6, H], fill=120)  # Scannerschatten am Blattrand
        winkel = rnd.uniform(-0.7, 0.7)
        img = img.rotate(winkel, expand=False, fillcolor=246)
        seiten.append(img.convert("RGB"))
    out.parent.mkdir(parents=True, exist_ok=True)
    seiten[0].save(
        out,
        "PDF",
        resolution=150.0,
        save_all=True,
        append_images=seiten[1:],
        creationDate=FIXED_PDF_TIME,
        modDate=FIXED_PDF_TIME,
        title=plain(meta["betreff"]),
        author=meta["absender"],
        subject=(
            f"{meta.get('dokumenttyp') or 'Scan-Anlage'} | "
            f"Az. {meta.get('aktenzeichen') or 'ohne Aktenzeichen'}"
        ),
        keywords=", ".join(
            value
            for value in (
                "Vergaberecht",
                meta.get("aktenzeichen", ""),
                meta.get("dokumenttyp", ""),
            )
            if value
        ),
        creator=meta["absender"],
    )


# ------------------------------------------------------------------- PPTX

def write_pptx(out: Path, meta: dict[str, str], blocks: list[tuple[str, object]]) -> None:
    prs = Presentation()
    prs.core_properties.created = FIXED_PACKAGE_DATETIME
    prs.core_properties.modified = FIXED_PACKAGE_DATETIME
    prs.core_properties.title = plain(meta["betreff"])
    prs.core_properties.subject = (
        f"{meta.get('dokumenttyp') or 'Vergabeakte'} | "
        f"Az. {meta.get('aktenzeichen') or 'ohne Aktenzeichen'}"
    )
    prs.core_properties.author = meta["absender"]
    prs.core_properties.last_modified_by = meta["absender"]
    prs.core_properties.category = "Vergabeakte"
    prs.core_properties.keywords = ", ".join(
        value
        for value in (
            "Vergaberecht",
            meta.get("aktenzeichen", ""),
            meta.get("dokumenttyp", ""),
        )
        if value
    )
    titel = prs.slides.add_slide(prs.slide_layouts[0])
    titel.shapes.title.text = plain(meta["betreff"])
    titel.placeholders[1].text = f"{meta['absender']}\n{meta['datum']}" + (
        f"\nAz: {meta['aktenzeichen']}" if meta.get("aktenzeichen") else "")

    def neue_folie(ueberschrift: str):
        s = prs.slides.add_slide(prs.slide_layouts[1])
        s.shapes.title.text = ueberschrift
        tf = s.placeholders[1].text_frame
        tf.word_wrap = True
        return s, tf

    folie, tf = None, None
    current_heading = plain(meta["betreff"])
    first_heading = True
    for art, inhalt in blocks:
        if art == "heading":
            level, txt = inhalt  # type: ignore[misc]
            if level == 1 and first_heading:
                first_heading = False
                continue
            current_heading = plain(txt)
            folie, tf = neue_folie(current_heading)
        elif art in ("para", "list", "numbered-list"):
            if tf is None:
                folie, tf = neue_folie(plain(meta["betreff"]))
            items = [str(inhalt)] if art == "para" else list(inhalt)  # type: ignore[arg-type]
            for index, item in enumerate(items, start=1):
                p = tf.paragraphs[0] if (len(tf.paragraphs) == 1 and not tf.paragraphs[0].text) else tf.add_paragraph()
                prefix = f"{index}. " if art == "numbered-list" else ""
                p.text = prefix + plain(item)
                p.level = 1 if art in ("list", "numbered-list") else 0
                for run in p.runs:
                    run.font.size = PptPt(14)
        elif art == "table":
            rows = inhalt  # type: ignore[assignment]
            if not rows:
                continue
            header, body = rows[0], rows[1:]
            chunks = [body[index:index + 12] for index in range(0, len(body), 12)] or [[]]
            for chunk_index, chunk in enumerate(chunks, start=1):
                slide_rows = [header, *chunk]
                s = prs.slides.add_slide(prs.slide_layouts[5])
                suffix = (
                    f" ({chunk_index}/{len(chunks)})" if len(chunks) > 1 else ""
                )
                s.shapes.title.text = current_heading + suffix
                ncols = max(len(r) for r in slide_rows)
                table_height = min(5.35, max(1.0, 0.38 * len(slide_rows)))
                tbl = s.shapes.add_table(
                    len(slide_rows),
                    ncols,
                    Inches(0.4),
                    Inches(1.6),
                    Inches(9.2),
                    Inches(table_height),
                ).table
                for ri, row in enumerate(slide_rows):
                    for ci in range(ncols):
                        cell = tbl.cell(ri, ci)
                        cell.text = plain(row[ci]) if ci < len(row) else ""
                        cell.margin_left = Inches(0.07)
                        cell.margin_right = Inches(0.07)
                        cell.margin_top = Inches(0.04)
                        cell.margin_bottom = Inches(0.04)
                        for paragraph in cell.text_frame.paragraphs:
                            for run in paragraph.runs:
                                run.font.size = PptPt(10.5)
                                run.font.bold = ri == 0
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(out)
    normalize_ooxml(out)


# --------------------------------------------------------------- Aktenbeifang

def _basis_datetime(meta: dict[str, str], offset: int = 0) -> datetime:
    try:
        tag, monat, jahr = DATUM_RE.match(meta["datum"]).groups()  # type: ignore[union-attr]
        basis = datetime(int(jahr), int(monat), int(tag), 9, 12, tzinfo=BERLIN_TZ)
    except Exception:
        basis = datetime(2026, 5, 15, 9, 12, tzinfo=BERLIN_TZ)
    return basis + timedelta(days=offset)


def _akte_titles(stuecke: list[Path]) -> list[str]:
    titles: list[str] = []
    for md in stuecke:
        text = md.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            titles.append(plain(m.group(1)).strip())
    return titles


def _akte_meta(akte: str, stuecke: list[Path]) -> dict[str, str]:
    if stuecke:
        text = stuecke[0].read_text(encoding="utf-8")
        return build_meta(akte, stuecke[0], text)
    org, adresse, domain = partei(akte, "vergabestelle")
    return {
        "absender": org,
        "adresse": adresse,
        "domain": domain,
        "datum": "15.05.2026",
        "betreff": akte.replace("-", " "),
        "aktenzeichen": "",
        "rolle": "vergabestelle",
    }


@lru_cache(maxsize=32)
def _stueck_metadaten_cached(
    akte: str, stuecke: tuple[Path, ...]
) -> tuple[tuple[Path, dict[str, str], str], ...]:
    result = []
    for path in stuecke:
        text = path.read_text(encoding="utf-8")
        meta = build_meta(akte, path, text)
        title_match = re.search(r"^#\s+(.+)$", text, re.M)
        title = plain(title_match.group(1)).strip() if title_match else path.stem.replace("_", " ")
        result.append((path, meta, title))
    return tuple(result)


def _stueck_metadaten(
    akte: str, stuecke: list[Path]
) -> tuple[tuple[Path, dict[str, str], str], ...]:
    return _stueck_metadaten_cached(akte, tuple(stuecke))


def arbeitsdatei_name(path: Path, meta: dict[str, str]) -> str:
    low = f"{path.stem} {meta.get('dokumenttyp', '')}".lower()
    suffix = ".eml" if any(keyword in low for keyword in EML_KEYWORDS) else ".docx"
    return path.stem + suffix


def _letzter_stueckzeitpunkt(akte: str, meta: dict[str, str], stuecke: list[Path]) -> datetime:
    dates = [_basis_datetime(item_meta) for _, item_meta, _ in _stueck_metadaten(akte, stuecke)]
    return max(dates, default=_basis_datetime(meta))


def write_portal_log_csv(out: Path, akte: str, meta: dict[str, str], stuecke: list[Path]) -> None:
    rnd = random.Random(int(hashlib.sha256((akte + "portal").encode()).hexdigest()[:8], 16))
    documents = _stueck_metadaten(akte, stuecke)
    vorgaenge = [
        "Unterlagenpaket geöffnet",
        "Dokument in DMS abgelegt",
        "Frist in Kalender übertragen",
        "Metadaten auf Plattform geprüft",
        "Uploadpaket erneut validiert",
        "Bieterkommunikation exportiert",
        "Aktenvermerk finalisiert",
        "Hashwert für Anlage notiert",
        "PDF-Vorschau erzeugt",
        "Freigabe durch Vier-Augen-Prüfung erfasst",
    ]
    systeme = ["Vergabeplattform", "DMS", "E-Mail-Gateway", "AVA/ERP", "Fristenkalender"]
    nutzer = ["s.mueller", "zv.postfach", "jurist.vergaberecht", "fachamt", "extern.upload"]
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["Zeitstempel", "System", "Nutzer", "Vorgang", "Dokument", "Status", "SHA256", "Bemerkung"])
        records = []
        count = max(10, min(18, len(stuecke) + 7))
        for nr in range(count):
            if documents:
                path, item_meta, titel = documents[nr % len(documents)]
                stamp = _basis_datetime(item_meta, nr // len(documents))
                dokument = arbeitsdatei_name(path, item_meta)
            else:
                stamp = _basis_datetime(meta, nr // 4)
                dokument = f"akte-{nr:02d}.pdf"
                titel = meta["betreff"]
            stamp += timedelta(minutes=17 * (nr % max(1, len(documents))) + rnd.randrange(0, 9))
            digest = hashlib.sha256((akte + dokument + str(nr)).encode()).hexdigest()
            records.append((stamp, [
                stamp.strftime("%Y-%m-%d %H:%M:%S"),
                systeme[nr % len(systeme)],
                nutzer[(nr + rnd.randrange(0, len(nutzer))) % len(nutzer)],
                vorgaenge[nr % len(vorgaenge)],
                dokument,
                "OK" if nr % 5 else "nachbearbeitet",
                digest[:16],
                titel[:72].rstrip(),
            ]))
        for _, row in sorted(records, key=lambda item: (item[0], item[1][4], item[1][6])):
            writer.writerow(row)


def write_loose_notes(out: Path, akte: str, meta: dict[str, str], stuecke: list[Path]) -> None:
    titles = _akte_titles(stuecke)
    basis = _letzter_stueckzeitpunkt(akte, meta, stuecke)
    lines = [
        "Lose Bearbeitungsnotizen",
        f"Akte: {meta.get('aktenzeichen') or akte}",
        f"Stand: {basis.strftime('%d.%m.%Y')} / nicht zur Versendung bestimmt",
        "",
        "Telefon / Flur / Rückruf:",
        f"- {basis.strftime('%d.%m.%Y')} 09:35 Fachamt: Mengenansatz noch einmal gegen Altvertrag prüfen.",
        "- Portal zeigt zwei fast gleich benannte Dateien; nur die zuletzt freigegebene Fassung verwenden.",
        "- Beim Upload darauf achten: Preisblatt und Konzeptanlage getrennt lassen, keine Sammel-PDF.",
        "",
        "Noch offen / klebt am Aktenrand:",
    ]
    for nr, title in enumerate(titles[:6], start=1):
        prefix = "!" if nr in {2, 5} else "-"
        lines.append(f"{prefix} {title[:92]} - Quercheck, ob Anlage im ZIP und im Einzel-PDF identisch ist.")
    lines += [
        "",
        "Schmierzettel:",
        "Frist nicht aus Bauchgefühl rechnen. Eingang, Nichtabhilfe, Stillhaltefrist und Uploadzeit getrennt notieren.",
        "Bei Wertung: erst Mindestanforderungen, dann Preisformel, dann Qualität/Tempo/Servicelevel. Nicht reflexhaft billigstes Angebot nehmen.",
        "Bei Rüge/VK: Originalnachricht, Exportzeit und Plattform-Quittung zusammenhalten.",
    ]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_internal_forward_eml(out: Path, akte: str, meta: dict[str, str], stuecke: list[Path]) -> None:
    rolle = "vergabestelle" if "vergabestelle" in PARTEIEN.get(akte, {}) else (meta.get("rolle") or "vergabestelle")
    org, _, domain = partei(akte, rolle)
    empfaenger = meta.get("absender") or org
    stamp = _letzter_stueckzeitpunkt(akte, meta, stuecke) + timedelta(days=1, hours=10, minutes=23)
    msg = EmailMessage(policy=EML_POLICY)
    msg["From"] = f'"{org} - Poststelle" <poststelle@{domain}>'
    msg["To"] = f'"{empfaenger}" <{mail_adresse(empfaenger, domain)}>'
    msg["Subject"] = f"WG: Aktenstand / Unterlagenpaket - {plain(meta['betreff'])[:90]}"
    msg["Date"] = format_datetime(stamp)
    msg["Message-ID"] = f"<{hashlib.sha256((akte + out.name + 'intern').encode()).hexdigest()[:20]}@{domain}>"
    msg["X-Aktenzeichen"] = meta.get("aktenzeichen", "")
    docs = "\n".join(
        f"- {arbeitsdatei_name(path, item_meta)}"
        for path, item_meta, _ in _stueck_metadaten(akte, stuecke)[:8]
    )
    msg.set_content(
        "Guten Morgen,\n\n"
        "anbei nur zur internen Ablage der aktuelle Stand aus Plattform, DMS und Fachbereich. "
        "Die Dateinamen sind noch nicht vollständig bereinigt; bitte vor Versand nur die freigegebenen Fassungen verwenden.\n\n"
        f"Akte: {meta.get('aktenzeichen') or akte}\n"
        f"Betreff: {plain(meta['betreff'])}\n\n"
        "Zuletzt sichtbare Aktenstücke:\n"
        f"{docs}\n\n"
        "Hinweis: Fristen, Uploadquittungen und Hashwerte bitte zusammen mit der fachlichen Wertung prüfen.\n\n"
        "Viele Grüße\nPoststelle / Vergabeakte\n"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(msg.as_bytes(policy=EML_POLICY))


def write_fristen_skizze_png(out: Path, akte: str, meta: dict[str, str], stuecke: list[Path]) -> None:
    rnd = random.Random(int(hashlib.sha256((akte + "skizze").encode()).hexdigest()[:8], 16))
    W, H = 1400, 900
    img = Image.new("RGB", (W, H), (248, 247, 242))
    d = ImageDraw.Draw(img)
    font = load_font(30)
    font_b = load_font(34, bold=True)
    small = load_font(24)
    for _ in range(1800):
        x, y = rnd.randrange(W), rnd.randrange(H)
        shade = rnd.randrange(218, 244)
        d.point((x, y), fill=(shade, shade, shade))
    d.rectangle([50, 50, W - 50, H - 50], outline=(160, 156, 145), width=3)
    d.text((90, 85), "Fristen / Upload / Belege", font=font_b, fill=(28, 74, 86))
    d.text((90, 130), plain(meta.get("aktenzeichen") or akte)[:90], font=small, fill=(80, 76, 68))
    documents = _stueck_metadaten(akte, stuecke)
    basis = min((_basis_datetime(item_meta) for _, item_meta, _ in documents), default=_basis_datetime(meta))
    csv_events: list[tuple[str, datetime]] = []
    if stuecke:
        for csv_path in sorted(stuecke[0].parent.rglob("*.csv")):
            if csv_path.name == "00_portal_aktivitaetsprotokoll.csv":
                continue
            try:
                with csv_path.open(encoding="utf-8", newline="") as stream:
                    rows = list(csv.reader(stream))
            except (OSError, UnicodeError, csv.Error):
                continue
            for row in rows[1:]:
                if not row:
                    continue
                date_match = None
                for cell in row[1:]:
                    date_match = DATUM_RE.search(cell)
                    if date_match:
                        break
                if not date_match:
                    continue
                day, month, year = date_match.groups()
                csv_events.append(
                    (row[0].lower(), datetime(int(year), int(month), int(day), 9, 12, tzinfo=BERLIN_TZ))
                )

    def event_date(tokens: tuple[str, ...], fallback_days: int) -> datetime:
        recorded = [date for label, date in csv_events if any(token in label for token in tokens)]
        if recorded:
            return min(recorded)
        candidates = [
            _basis_datetime(item_meta)
            for path, item_meta, _ in documents
            if any(token in path.stem.lower() for token in tokens)
        ]
        return min(candidates, default=basis + timedelta(days=fallback_days))

    latest = max((_basis_datetime(item_meta) for _, item_meta, _ in documents), default=basis)
    items = [
        ("Eingang / Kenntnis", basis.strftime("%d.%m.%Y")),
        ("Rüge / Bieterfrage", event_date(("ruege", "bieterfrage"), 3).strftime("%d.%m.%Y")),
        ("Nichtabhilfe / Antwort", event_date(("nichtabhilfe", "antwort"), 8).strftime("%d.%m.%Y")),
        ("VK / Stillhaltefrist", event_date(("nachpruefung", "_134_", "vk_"), 12).strftime("%d.%m.%Y")),
        ("Uploadpaket final", (latest + timedelta(days=1)).strftime("%d.%m.%Y")),
    ]
    y = 210
    colors = [(255, 244, 184), (221, 239, 255), (228, 246, 219), (255, 226, 214), (235, 229, 255)]
    for idx, (label, date) in enumerate(items):
        x = 95 + (idx % 2) * 610
        yy = y + (idx // 2) * 150
        d.rounded_rectangle([x, yy, x + 540, yy + 105], radius=14, fill=colors[idx], outline=(159, 154, 142), width=2)
        d.text((x + 22, yy + 18), label, font=font, fill=(34, 34, 34))
        d.text((x + 22, yy + 58), date, font=font_b, fill=(120, 43, 36))
    notes = [
        "Originaldatei behalten",
        "Quittung + Hash sichern",
        "Begründung in Vergabeakte",
        "Geschäftsgeheimnisse schwärzen",
    ]
    for i, note in enumerate(notes):
        d.text((105, 690 + i * 38), f"- {note}", font=small, fill=(42, 42, 42))
    for _ in range(10):
        x1, y1 = rnd.randrange(80, W - 160), rnd.randrange(180, H - 120)
        d.line([x1, y1, x1 + rnd.randrange(-30, 80), y1 + rnd.randrange(-20, 45)],
               fill=(190, 92, 63), width=2)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)


def write_aktenbeifang(akte_dir: Path, akte: str, stuecke: list[Path]) -> dict[str, int]:
    meta = _akte_meta(akte, stuecke)
    write_portal_log_csv(akte_dir / "daten" / "00_portal_aktivitaetsprotokoll.csv", akte, meta, stuecke)
    write_loose_notes(akte_dir / "notizen" / "00_bearbeitungsnotizen_eingangskorb.txt", akte, meta, stuecke)
    write_internal_forward_eml(akte_dir / "eml" / "00_interne_weiterleitung_aktenstand.eml", akte, meta, stuecke)
    write_fristen_skizze_png(akte_dir / "bilder" / "00_fristen_upload_skizze.png", akte, meta, stuecke)
    return {"csv": 1, "txt": 1, "eml": 1, "png": 1}


# ------------------------------------------------------------------ Steuerung

def migrate_renamed_outputs(akte_dir: Path, akte: str) -> int:
    """Beseitigt abgeleitete Dateien zu inzwischen umbenannten Quellen."""
    migrated = 0
    for old_stem, new_stem in RENAMED_SOURCE_STEMS.get(akte, {}).items():
        for subdir, suffix in (
            ("docx", ".docx"),
            ("eml", ".eml"),
            ("xlsx", ".xlsx"),
            ("scan-pdf", ".pdf"),
            ("pptx", ".pptx"),
        ):
            old_path = akte_dir / subdir / f"{old_stem}{suffix}"
            if not old_path.exists():
                continue
            new_path = akte_dir / subdir / f"{new_stem}{suffix}"
            new_path.parent.mkdir(parents=True, exist_ok=True)
            if new_path.exists():
                old_path.unlink()
            else:
                old_path.replace(new_path)
            migrated += 1

        einzel_dir = akte_dir / "einzel-pdf"
        if einzel_dir.is_dir():
            for old_pdf in einzel_dir.glob("*.pdf"):
                if old_pdf.stem == old_stem or old_pdf.stem.endswith(f"__{old_stem}"):
                    old_pdf.unlink()
                    migrated += 1
    return migrated


def enrich_legacy_office_metadata(akte_dir: Path, akte: str) -> int:
    enriched = 0
    for filename, metadata in LEGACY_OFFICE_METADATA.get(akte, {}).items():
        path = next(
            (
                candidate
                for candidate in (
                    akte_dir / "docx" / filename,
                    akte_dir / "xlsx" / filename,
                )
                if candidate.is_file()
            ),
            None,
        )
        if path is None:
            continue
        if path.suffix == ".docx":
            document = docx.Document(str(path))
            props = document.core_properties
            props.title = metadata["title"]
            props.subject = metadata["subject"]
            props.author = metadata["author"]
            props.last_modified_by = metadata["author"]
            props.category = "Vergabeakte"
            props.keywords = "Vergaberecht, IT-Sicherheitsvergabe, Nachprüfung"
            props.created = FIXED_PACKAGE_DATETIME
            props.modified = FIXED_PACKAGE_DATETIME
            document.save(path)
        else:
            from openpyxl import load_workbook

            workbook = load_workbook(path)
            props = workbook.properties
            props.title = metadata["title"]
            props.subject = metadata["subject"]
            props.creator = metadata["author"]
            props.lastModifiedBy = metadata["author"]
            props.category = "Vergabeakte"
            props.keywords = "Vergaberecht, IT-Sicherheitsvergabe, Wertung"
            props.created = FIXED_PACKAGE_DATETIME
            props.modified = FIXED_PACKAGE_DATETIME
            workbook.save(path)
            workbook.close()
        normalize_ooxml(path)
        enriched += 1
    return enriched

def hat_handgefertigtes_gegenstueck(akte_dir: Path, md_stem: Path) -> bool:
    counterparts = HANDCRAFTED_COUNTERPARTS.get(akte_dir.name, {}).get(
        md_stem.stem,
        (),
    )
    return any((akte_dir / relative).is_file() for relative in counterparts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lebensechte Arbeitsformate aus den Markdown-Quellen erzeugen."
    )
    parser.add_argument(
        "testakten",
        nargs="*",
        metavar="NAME",
        help="Testakten-Verzeichnis; ohne Angabe werden alle Akten gebaut.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Verfügbare Testakten anzeigen und beenden.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    all_dirs = sorted(
        d for d in TESTAKTEN.iterdir()
        if d.is_dir() and d.name not in SKIP_DIRS
    )
    by_name = {d.name: d for d in all_dirs}
    if args.list:
        print("\n".join(by_name))
        return 0
    unknown = sorted(set(args.testakten) - set(by_name))
    if unknown:
        print(
            "FEHLER: unbekannte Testakte(n): " + ", ".join(unknown),
            file=sys.stderr,
        )
        return 2
    targets = [by_name[name] for name in args.testakten] if args.testakten else all_dirs

    erzeugt = {"docx": 0, "eml": 0, "xlsx": 0, "scan": 0, "pptx": 0, "beifang": 0}
    uebersprungen = 0
    migriert = 0
    metadaten_ergaenzt = 0
    for akte_dir in targets:
        akte = akte_dir.name
        migriert += migrate_renamed_outputs(akte_dir, akte)
        stuecke = sorted(akte_dir.glob("[0-9]*.md"))
        erzeugt["beifang"] += sum(write_aktenbeifang(akte_dir, akte, stuecke).values())
        scan_ziele = [m for m in stuecke if any(k in m.stem.lower() for k in SCAN_KEYWORDS)][:2]
        if not scan_ziele and stuecke:
            scan_ziele = stuecke[:1]
        pptx_ziele = [m for m in stuecke if any(k in m.stem.lower() for k in PPTX_KEYWORDS)][:1]
        if not pptx_ziele and stuecke:
            pptx_ziele = stuecke[:1]
        for md in stuecke:
            text = md.read_text(encoding="utf-8")
            meta = build_meta(akte, md, text)
            blocks = parse_blocks(text)
            low = (md.stem + " " + meta.get("dokumenttyp", "")).lower()
            als_eml = any(k in low for k in EML_KEYWORDS)
            ziel_ext = ".eml" if als_eml else ".docx"
            ziel = akte_dir / ("eml" if als_eml else "docx") / (md.stem + ziel_ext)
            if not ziel.exists() and hat_handgefertigtes_gegenstueck(akte_dir, md):
                uebersprungen += 1
            else:
                if als_eml:
                    write_eml(ziel, akte, meta, blocks)
                    erzeugt["eml"] += 1
                else:
                    write_docx(ziel, meta, blocks)
                    erzeugt["docx"] += 1
            n_tables = sum(1 for art, _ in blocks if art == "table")
            if n_tables >= 2 or any(k in low for k in XLSX_KEYWORDS):
                xziel = akte_dir / "xlsx" / (md.stem + ".xlsx")
                if write_xlsx(xziel, meta, blocks):
                    erzeugt["xlsx"] += 1
            if md in scan_ziele:
                write_scan_pdf(akte_dir / "scan-pdf" / (md.stem + ".pdf"), meta, blocks)
                erzeugt["scan"] += 1
            if md in pptx_ziele:
                write_pptx(akte_dir / "pptx" / (md.stem + ".pptx"), meta, blocks)
                erzeugt["pptx"] += 1
        metadaten_ergaenzt += enrich_legacy_office_metadata(akte_dir, akte)
    print(f"build-testakten-echtformate: {erzeugt['docx']} docx, "
          f"{erzeugt['eml']} eml, {erzeugt['xlsx']} xlsx, "
          f"{erzeugt['scan']} scan-pdf, {erzeugt['pptx']} pptx erzeugt, "
          f"{erzeugt['beifang']} Aktenbeifang-Dateien, "
          f"{uebersprungen} handgefertigte Gegenstuecke respektiert, "
          f"{migriert} veraltete Ableitungen migriert, "
          f"{metadaten_ergaenzt} Bestandsdateien mit Metadaten ergänzt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
