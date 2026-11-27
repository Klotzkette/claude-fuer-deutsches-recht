"""Liest Aktenstücke ohne Entpacken in die Akte und hält die Fundstelle am Text."""

from __future__ import annotations

import csv
from datetime import date
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses, parsedate_to_datetime
from io import BytesIO, StringIO
from pathlib import Path
import re
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from openpyxl import load_workbook
from pypdf import PdfReader

from akteneingang.quellen import safe_member


def plain(value):
    return re.sub(r"\s+", " ", str(value)).strip()


def paragraphs(text):
    return [plain(block) for block in re.split(r"\n\s*\n", text.strip()) if plain(block)]


def local_bytes(root, address):
    """Hier sind ausschließlich konkrete Repo-Pfade, optional mit ZIP-Mitglied erlaubt."""
    location, *members = address.split("!")
    path = (root / location).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Quellpfad außerhalb des Repository: {address}")
    data = path.read_bytes()
    for member in members:
        with ZipFile(BytesIO(data)) as archive:
            data = archive.read(safe_member(member))
    return data


def source_name(address):
    return Path(address.split("!")[-1]).name


def local_reference(key, member):
    if key.endswith(".zip"):
        return key + "!" + member
    return key + "/" + member


def words(text):
    return set(re.findall(r"[a-zäöüß]{4,}", text.casefold())) - {
        "bitte", "eine", "einen", "einer", "dass", "sind", "wird", "habe", "haben", "dieser", "unser",
        "diesem", "noch", "oder", "wurde", "kann", "sich", "soll", "welche", "welcher",
        "durch", "sowie", "nach", "unter", "akten", "gibt", "beim", "aber", "wäre", "seine",
    }


def adresse(value):
    return ", ".join(f"{name} <{mail}>" if name else mail
                     for name, mail in getaddresses([str(value)]))


def postabschnitte(body):
    # Einzelne harte Zeilen sind regelmäßig Grüße und Unterschriften. Bei
    # Formaten mit Zeilenumbruch bleiben umbrochene Fließtextzeilen zusammen.
    result = []
    for block in re.split(r"\n\s*\n", body.replace("\r\n", "\n").strip()):
        lines = [s.strip() for s in block.splitlines() if s.strip()]
        if len(lines) > 1 and re.match(r"^(?:Sehr geehrt|Guten |Hallo|Lieb\w+ |Hi |Moin|Servus)", lines[0]) and len(lines[0]) < 90:
            result.append(lines.pop(0))
        last = next((i for i, line in enumerate(lines) if re.match(
            r"^(?:Mit (?:freundlichen|besten)|(?:Beste|Viele|Freundliche|Liebe) (?:Grüße|Grüsse)|Hochachtungsvoll)", line)), len(lines))
        if lines[:last]:
            result.append(plain(" ".join(lines[:last])))
        result.extend(lines[last:])
    return result


def attached_mail(data):
    msg = BytesParser(policy=policy.default).parsebytes(data)
    if not all(msg.get(field) for field in ("from", "to", "subject")):
        return None
    body = msg.get_body(preferencelist=("plain",))
    if not body:
        return None
    try:
        text = body.get_content()
    except (LookupError, UnicodeError):
        return None
    if not isinstance(text, str):
        return None
    sent = ""
    if msg["Date"]:
        try:
            sent = parsedate_to_datetime(str(msg["Date"])).strftime("%d.%m.%Y")
        except (TypeError, ValueError, OverflowError):
            pass
    return {"titel": plain(msg["subject"]), "von": adresse(msg["from"]), "an": adresse(msg["to"]),
            "datum": sent, "text": postabschnitte(text), "typ": "eml"}


def extract(data, address):
    suffix = Path(source_name(address)).suffix.lower()
    if suffix == ".eml":
        mail = attached_mail(data)
        return [(s, "Nachrichtentext") for s in mail["text"]] if mail else []
    if suffix == ".docx":
        with ZipFile(BytesIO(data)) as archive:
            body = ET.fromstring(archive.read("word/document.xml"))
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        abschnitte = []
        for i, paragraph in enumerate(body.findall(".//w:p", ns), 1):
            run = []
            for node in paragraph.iter():
                tag = node.tag.rsplit("}", 1)[-1]
                if tag == "t":
                    run.append(node.text or "")
                elif tag in {"br", "tab", "cr"}:
                    run.append(" ")
            abschnitte.append((plain("".join(run)), f"Absatz {i}"))
        return abschnitte
    if suffix == ".pdf":
        result = []
        reader = PdfReader(BytesIO(data), strict=False)
        if not reader.is_encrypted:
            for n, page in enumerate(reader.pages[:3], 1):
                result += [(para, f"Seite {n}") for para in paragraphs(page.extract_text(extraction_mode="layout") or "")]
        return result
    if suffix == ".xlsx":
        result = []
        with BytesIO(data) as source:
            workbook = load_workbook(source, read_only=True, data_only=True)
            try:
                for sheet in workbook.worksheets[:4]:
                    for row in sheet.iter_rows(max_row=45, max_col=10):
                        for cell in row:
                            if isinstance(cell.value, str) and len(cell.value) >= 42:
                                result.append((plain(cell.value), f"{sheet.title}!{cell.coordinate}"))
            finally:
                workbook.close()
        return result
    if suffix in (".txt", ".md", ".csv"):
        if b"\0" in data[:4000]:
            return []
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError:
            return []
        if suffix == ".csv":
            try:
                dialect = csv.Sniffer().sniff(text[:4000], delimiters=",;\t|")
                rows = csv.reader(StringIO(text), dialect)
                head = next(rows)
                return [(" · ".join(f"{h}: {v}" for h, v in zip(head, row) if h and v), f"Datenzeile {n}")
                        for n, row in enumerate(rows, 1) if len(row) == len(head)][:20]
            except (csv.Error, StopIteration):
                return []
        return [(s, f"Textabsatz {i}") for i,s in enumerate(paragraphs(text), 1)]
    return []


def saetze(value):
    # In Akten sind „am 20. und 21. Oktober“, „Nr. 6“, „Dr. Roth“ und
    # Paragraphenzitate häufig. Der Punkt beendet dort keinen Fragesatz.
    return re.split(r"(?<=[!?])\s+|(?<!\d\.)(?<!\s[A-ZÄÖÜ]\.)(?<!Dr\.)(?<!Nr\.)(?<!Abs\.)(?<=\.)\s+(?=[A-ZÄÖÜ„])", value)


def evidence_excerpt(parts, query):
    """Wählt einen vollständigen passenden Originalsatz; ein kurzes Fragment wird nie zum Befund."""
    target = words(query)
    choices = []
    for value, location in parts:
        if not value:
            continue
        units = [value] if len(value) <= 390 else saetze(value)
        for unit in units:
            unit = plain(unit)
            if not 42 <= len(unit) <= 390 or len(words(unit)) < 5:
                continue
            if any(mark in unit for mark in ("http://","https://","<html", "](..", "KI generiert",
                                             "Use at your own", "Erwartete Arbeitsprodukte", "_______________")):
                continue
            if ("@" in unit or re.search(r"\b(?:IBAN|Telefax|Telefonzentrale|USt-IdNr|HRB|Seite \d+ von)\b", unit, re.I)
                    or re.search(r"\b(?:Rechnungsdatum|Datum|Fax|Fon|Telefon):.{0,25}\d+\.$", unit)
                    or re.match(r"^(?:Sehr geehrt|Mit freundlichen|Mit besten|Freundliche Grüße|Bearbeitet von)", unit)
                    or re.search(r"(?:\ufffd|[a-zäöüß][A-ZÄÖÜ][a-zäöü]{3}[^ ]{24,}|={4}|_{4})", unit)):
                continue
            if location.startswith("Seite ") and not unit.endswith((".", "!", "?", "“", "€", "Euro")):
                continue
            if unit.startswith(("#", "|", "{", "[", "<", "-----")):
                continue
            common = target & words(unit)
            finanzbeleg = int(bool(re.search(r"\b(?:netto|brutto|Rechnungsbetrag|Gesamtbetrag|Anzahlung)\b", unit, re.I)))
            score = (len(common), finanzbeleg, sum(len(w) for w in common), int(bool(re.search(r"\d", unit))))
            choices.append((score, unit, location))
    if choices:
        _, quote, where = max(choices, key=lambda x:x[0])
        return quote, where
    return "", ""


def german_date(value):
    if not value:
        return ""
    try:
        return date.fromisoformat(value).strftime("%d.%m.%Y")
    except ValueError:
        return value
