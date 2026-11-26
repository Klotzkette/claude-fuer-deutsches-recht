#!/usr/bin/env python3
"""Erzeugt die Originalunterlagen, Druckfassungen und Fallseiten der Interstate AG."""
import argparse
import csv
import io
import json
import math
import re
from datetime import date, datetime, time
from decimal import Decimal, ROUND_HALF_UP
from email.headerregistry import Address
from email.message import EmailMessage
from email.policy import SMTP
from pathlib import Path
from urllib.parse import quote
from xml.dom.minidom import parseString
from xml.sax.saxutils import escape
from zipfile import ZipFile
from zoneinfo import ZoneInfo

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from akteneingang.ausgabe import archive
from akteneingang.dokumente import add_member, office_bytes, sha, simple
from akteneingang.quellen import safe_member
from interstate_einwendungsbogen import pruefbogen
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/interstate-ag"
OUTPUT = ROOT / "vergaberecht-werkstatt/vergabestelle-behoerden/Interstate AG"
COLLECTION_ZIP = ROOT / "docs/downloads/interstate-ag-nl-west-testakten.zip"
PRUEFBOGEN = "Einwendungen-Pruefbogen.xlsx"
PHASES = ("Grundakte", "Nachreichungen")
ACCENT = "234C5A"
MUTED = "4C6370"
SECTION_HEADING = re.compile(r"(?:§\s*)?\d+(?:\.\d+)*\s+[^\n.!?;:]{2,80}")


def german_date(doc):
    return date.fromisoformat(doc["datum"]).strftime("%d.%m.%Y")


def body(doc):
    return [doc["titel"], f'{german_date(doc)} · {doc["von"]} an {doc["an"]}', *doc["text"]]


def mail_time(doc):
    clock = time.fromisoformat(doc.get("uhrzeit", "09:00"))
    return datetime.combine(date.fromisoformat(doc["datum"]), clock, tzinfo=ZoneInfo("Europe/Berlin"))


def mail_address(doc, key, label):
    address = doc.get(key, simple(doc[label])[:48] + "@fallpost.example")
    return Address(display_name=doc[label], addr_spec=address)


def widths(rows):
    # Long descriptions need more space than dates or reference numbers.
    count = len(rows[0])
    return [max(12, min(55, max(len(str(r[c])) for r in rows) + 2)) for c in range(count)]


def german_number(value, minimum_decimals):
    number = Decimal(str(value)).normalize()
    precision = max(minimum_decimals, -number.as_tuple().exponent)
    return f"{number:,.{precision}f}".translate(str.maketrans(",.", ".,"))


class BillOfQuantities:
    """Positionspreise für die ausfüllbare Arbeitsmappe und deren Lesefassung."""

    def __init__(self, doc):
        self.rows = doc["tabelle"]
        header = self.rows[0]
        columns = [doc["lv"][key] for key in ("menge", "einheitspreis", "gesamtpreis")]
        if len(set(columns)) != 3 or any(header.count(label) != 1 for label in columns):
            raise ValueError(f'{doc["datei"]}: LV-Spalten sind nicht eindeutig')
        self.quantity, self.price, self.amount = map(header.index, columns)
        self.lot = None
        if "losspalte" in doc["lv"]:
            lot_header = doc["lv"]["losspalte"]
            if header.count(lot_header) != 1 or lot_header in columns:
                raise ValueError(f'{doc["datei"]}: Losspalte ist nicht eindeutig')
            self.lot = header.index(lot_header)
        label_columns = [c for c in range(len(header)) if c not in (self.quantity, self.price, self.amount, self.lot)]
        lengths = widths(self.rows)
        self.label = max(label_columns, key=lengths.__getitem__, default=self.quantity)
        self.amounts = []
        lot_amounts = {}
        for position, row in enumerate(self.rows[1:], 1):
            quantity, price = row[self.quantity], row[self.price]
            if type(quantity) not in (int, float) or not math.isfinite(quantity) or quantity <= 0:
                raise ValueError(f'{doc["datei"]}: ungültige Menge in Position {position}')
            if price is not None and (type(price) not in (int, float) or not math.isfinite(price) or price < 0):
                raise ValueError(f'{doc["datei"]}: ungültiger Einheitspreis in Position {position}')
            if row[self.amount] is not None:
                raise ValueError(f'{doc["datei"]}: Gesamtpreis in Position {position} wird berechnet')
            amount = None
            if price is not None:
                amount = (Decimal(str(quantity)) * Decimal(str(price))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            self.amounts.append(amount)
            if self.lot is not None:
                lot = row[self.lot]
                if not isinstance(lot, str) or not lot.strip():
                    raise ValueError(f'{doc["datei"]}: fehlende Loskennung in Position {position}')
                lot_amounts.setdefault(lot, []).append(amount)
        groups = {None: self.amounts, **lot_amounts}
        self.totals = {lot: sum(amounts, Decimal(0)) if None not in amounts else None
                       for lot, amounts in groups.items()}

    def total_label(self, lot):
        if lot is None:
            return "Summe netto (alle Positionen)" if self.lot is not None else "Summe netto"
        return f"Summe Los {lot} netto"

    def print_rows(self):
        result = [self.rows[0]]
        for source, amount in zip(self.rows[1:], self.amounts, strict=True):
            row = source.copy()
            row[self.quantity] = german_number(row[self.quantity], 0)
            row[self.price] = "" if row[self.price] is None else german_number(row[self.price], 2)
            row[self.amount] = "" if amount is None else german_number(amount, 2)
            result.append(row)
        for lot, value in self.totals.items():
            total = [""] * len(result[0])
            total[self.label] = self.total_label(lot)
            total[self.amount] = "" if value is None else german_number(value, 2)
            if lot is not None:
                total[self.lot] = lot
            result.append(total)
        return result

    def add_formulas(self, sheet, heading):
        first, last = heading + 1, heading + len(self.amounts)
        price_inputs = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True)
        price_inputs.showErrorMessage = True
        price_inputs.error = "Geben Sie einen nichtnegativen Einheitspreis als Zahl ein."
        sheet.add_data_validation(price_inputs)
        price_column = get_column_letter(self.price + 1)
        price_inputs.add(f"{price_column}{first}:{price_column}{last}")
        cache = {}
        for row, amount in enumerate(self.amounts, first):
            quantity = sheet.cell(row, self.quantity + 1).coordinate
            price = sheet.cell(row, self.price + 1)
            price.number_format = '#,##0.00##'
            price.fill = PatternFill("solid", fgColor="DAEFF8")
            line_total = sheet.cell(row, self.amount + 1)
            line_total.value = f'=IF(COUNT({quantity},{price.coordinate})=2,ROUND({quantity}*{price.coordinate},2),"")'
            line_total.number_format = '#,##0.00'
            cache[line_total.coordinate] = amount
        amount_column = get_column_letter(self.amount + 1)
        positions = f"${amount_column}${first}:${amount_column}${last}"
        for row, (lot, value) in enumerate(self.totals.items(), last + 1):
            sheet.cell(row, self.label + 1, self.total_label(lot))
            total = sheet.cell(row, self.amount + 1)
            if lot is None:
                total.value = f'=IF(COUNT({positions})=ROWS({positions}),SUM({positions}),"")'
            else:
                key = sheet.cell(row, self.lot + 1, lot).coordinate
                column = get_column_letter(self.lot + 1)
                matching = f'--(${column}${first}:${column}${last}={key})'
                count = f"SUMPRODUCT({matching})"
                priced = f"SUMPRODUCT({matching},--ISNUMBER({positions}))"
                subtotal = f"SUMPRODUCT({matching},{positions})"
                total.value = f'=IF(AND({count}>0,{priced}={count}),{subtotal},"")'
            total.number_format = '#,##0.00'
            cache[total.coordinate] = value
            for cell in sheet[row]:
                cell.font = Font(name="Calibri", size=10, bold=True, color="FFFFFF" if lot is None else ACCENT)
                cell.fill = PatternFill("solid", fgColor=ACCENT if lot is None else "E1EAEC")
            sheet.row_dimensions[row].height = 24
        return cache


def cached_workbook(book, cache):
    # openpyxl writes the formulas. Also supply their current result for PDF
    # importers, previews and spreadsheets opened with data_only=True.
    out = io.BytesIO()
    with ZipFile(io.BytesIO(office_bytes(book))) as source, ZipFile(out, "w") as target:
        for name in source.namelist():
            data = source.read(name)
            if name == "xl/worksheets/sheet1.xml":
                with parseString(data) as xml:
                    for cell in xml.getElementsByTagName("c"):
                        coord = cell.getAttribute("r")
                        if coord in cache:
                            value = cache[coord]
                            if value is None:
                                cell.setAttribute("t", "str")
                            else:
                                cell.getElementsByTagName("v")[0].appendChild(xml.createTextNode(str(value)))
                    data = xml.toxml(encoding="utf-8")
                    # Python 3.12 encoded quotes in XML text nodes. Keep the same bytes in
                    # formula text on 3.13+, where minidom escapes them only in attributes.
                    data = re.sub(rb">([^<]*\"[^<]*)<", lambda match: match[0].replace(b'"', b"&quot;"), data)
            add_member(target, name, data)
    return out.getvalue()


def word(doc, case):
    book = Document()
    book.core_properties.author = doc["von"]
    book.core_properties.title = doc["titel"]
    section = book.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.left_margin, section.right_margin = Cm(2.2), Cm(2.2)
    section.top_margin, section.bottom_margin = Cm(2.5), Cm(2.2)
    normal = book.styles["Normal"]
    normal.font.name, normal.font.size = "Times New Roman", Pt(11)
    normal.paragraph_format.space_after = Pt(8)
    letterhead = section.header.paragraphs[0].add_run(doc["von"])
    letterhead.bold = True
    letterhead.font.color.rgb = RGBColor.from_string(ACCENT)
    section.footer.paragraphs[0].text = case["zeichen"] + "    ·    " + german_date(doc)
    book.add_paragraph("An " + doc["an"] + "\n" + german_date(doc))
    title = book.add_heading(doc["titel"], level=1)
    for run in title.runs:
        run.font.name = "Times New Roman"
        run.font.color.rgb = RGBColor.from_string(ACCENT)
    for text in doc["text"]:
        paragraph = book.add_paragraph()
        run = paragraph.add_run(text)
        if SECTION_HEADING.fullmatch(text):
            run.bold = True
            paragraph.paragraph_format.keep_with_next = True
            paragraph.paragraph_format.space_after = Pt(3)
    rows = doc.get("tabelle", [])
    if rows:
        table = book.add_table(rows=0, cols=len(rows[0]))
        table.style = "Light Shading Accent 1"
        for r in rows:
            for cell, value in zip(table.add_row().cells, r, strict=True):
                cell.text = str(value)
    return office_bytes(book)


def worksheet(doc, case, lv):
    table = doc["tabelle"]
    spec = widths(table)
    book = Workbook()
    book.properties.title, book.properties.creator = doc["titel"], doc["von"]
    sheet = book.active
    sheet.title = "Aufstellung"
    sheet.sheet_view.showGridLines = False
    for ci, width in enumerate(spec, 1):
        sheet.column_dimensions[get_column_letter(ci)].width = width
    for ri, text in enumerate([doc["titel"], f'{case["zeichen"]} · {german_date(doc)}', doc["von"] + " an " + doc["an"], *doc["text"]], 1):
        sheet.merge_cells(start_row=ri, end_row=ri, start_column=1, end_column=len(spec))
        cell = sheet.cell(ri, 1, text)
        cell.font = Font(name="Calibri", size=15 if ri == 1 else 10, bold=ri == 1, color=ACCENT)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        lines = sum(max(1, math.ceil(len(line) / max(12, sum(spec) * .8))) for line in text.splitlines())
        sheet.row_dimensions[ri].height = max(28, 10 + 15 * lines)
    heading = sheet.max_row + 2
    for ri, row in enumerate(table, heading):
        for ci, value in enumerate(row, 1):
            cell = sheet.cell(ri, ci, value)
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            cell.font = Font(name="Calibri", size=10, bold=ri == heading, color="FFFFFF" if ri == heading else "263944")
            cell.fill = PatternFill("solid", fgColor=ACCENT if ri == heading else ("EFF4F5" if ri % 2 else "FFFFFF"))
        sheet.row_dimensions[ri].height = max(24, 7 + 15 * max(math.ceil(len(str(v)) / (w * .8)) for v, w in zip(row, spec)))
    sheet.freeze_panes = f"A{heading + 1}"
    sheet.auto_filter.ref = f"A{heading}:{get_column_letter(len(spec))}{sheet.max_row}"
    cache = lv.add_formulas(sheet, heading) if lv else None
    sheet.print_title_rows = f"{heading}:{heading}"
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    sheet.page_setup.fitToWidth, sheet.page_setup.fitToHeight = 1, 0
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
    sheet.page_setup.orientation = "landscape" if len(spec) >= 4 else "portrait"
    sheet.print_area = sheet.dimensions
    return cached_workbook(book, cache) if lv else office_bytes(book)


def native(doc, case, name, lv):
    ext = Path(name).suffix
    if ext == ".docx":
        return word(doc, case)
    if ext == ".xlsx":
        return worksheet(doc, case, lv)
    if ext == ".csv":
        data = io.StringIO(newline="")
        writer = csv.writer(data, delimiter=";", lineterminator="\r\n")
        # One rectangular UTF-8 table, including its accompanying provenance.
        rows = doc["tabelle"]
        writer.writerow([*rows[0], "Exportvermerk"])
        for i, row in enumerate(rows[1:]):
            writer.writerow([*row, "\n\n".join(body(doc)) if i == 0 else ""])
        return data.getvalue().encode("utf-8-sig")
    text = "\n\n".join(doc["text"])
    if doc.get("tabelle"):
        text += "\n\n" + "\n".join("\t".join(map(str, row)) for row in doc["tabelle"])
    if ext == ".txt":
        return ("\n".join(body(doc)[:2]) + "\n\n" + text + "\n").encode()
    if ext != ".eml":
        raise ValueError(f"Unbekanntes Aktenformat: {name}")
    message = EmailMessage(policy=SMTP)
    for header, key, label in [("From", "absender", "von"), ("To", "empfaenger", "an")]:
        message[header] = mail_address(doc, key, label)
    message["Date"] = mail_time(doc)
    message["Message-ID"] = f'<{sha((case["zeichen"] + "/" + name).encode())[:24]}@fallpost.example>'
    message["Subject"] = doc["titel"]
    message.set_content(text, charset="utf-8")
    return message.as_bytes()


def paragraph(text, font="Times-Roman", size=11, leading=14.5, color="24333B", after=8):
    style = ParagraphStyle("Beleg", fontName=font, fontSize=size, leading=leading,
                           textColor=colors.HexColor("#" + color), spaceAfter=after,
                           allowOrphans=0, allowWidows=0)
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), style)


def reading(doc, case, name, lv):
    rows = lv.print_rows() if lv else doc.get("tabelle", [])
    page_size = landscape(A4) if rows and len(rows[0]) >= 4 else A4
    out = io.BytesIO()
    pdf = SimpleDocTemplate(out, pagesize=page_size, leftMargin=48, rightMargin=48,
                            topMargin=46 if lv else 56, bottomMargin=40 if lv else 47,
                            invariant=1, title=doc["titel"], author=doc["von"])
    kinds = {".docx": "Schriftstück", ".xlsx": "Tabellenblatt", ".csv": "Datenexport", ".eml": "E-Mail", ".txt": "Textauszug"}
    kind = kinds[Path(name).suffix]

    def furniture(canvas, document):
        width, height = page_size
        canvas.setStrokeColor(colors.HexColor("#B7C7CC"))
        canvas.line(48, height-41, width-48, height-41)
        canvas.line(48, 35, width-48, 35)
        canvas.setFillColor(colors.HexColor("#" + MUTED))
        canvas.setFont("Helvetica", 8)
        canvas.drawString(48, height-32, case["zeichen"])
        canvas.drawRightString(width-48, height-32, kind)
        canvas.drawString(48, 23, german_date(doc))
        canvas.drawRightString(width-48, 23, f"Blatt {document.page}")

    sender, recipient = doc["von"], doc["an"]
    sent = ""
    if Path(name).suffix == ".eml":
        sender += f' <{mail_address(doc, "absender", "von").addr_spec}>'
        recipient += f' <{mail_address(doc, "empfaenger", "an").addr_spec}>'
        stamp = mail_time(doc)
        offset = stamp.strftime("%z")
        sent = f'\nGesendet  {german_date(doc)}, {stamp:%H:%M} Uhr (UTC{offset[:3]}:{offset[3:]})'
    story = [
        paragraph(doc["titel"], "Times-Bold", 18, 21, ACCENT, 11),
        paragraph(f"Von  {sender}\nAn    {recipient}{sent}", "Helvetica", 9.2, 13, MUTED, 14),
    ]
    for text in doc["text"]:
        if SECTION_HEADING.fullmatch(text):
            heading = paragraph(text, "Times-Bold", 11, 14.5, ACCENT, 3)
            heading.keepWithNext = True
            story.append(heading)
        elif lv:
            story.append(paragraph(text, size=10.5, leading=13.5, after=5))
        else:
            story.append(paragraph(text))
    if rows:
        if lv:
            # Leave space for service descriptions; item/lot codes need only a few characters.
            weights = [max(7, min(75, max(len(str(row[i])) for row in rows) + 2)) for i in range(len(rows[0]))]
        else:
            weights = widths(rows)
        available = pdf.width - 12
        grid = Table([[paragraph(v, "Helvetica-Bold" if i == 0 else "Helvetica", 9, 11.5,
                                 "FFFFFF" if i == 0 else "24333B", 0) for v in row]
                      for i, row in enumerate(rows)], repeatRows=1, hAlign="LEFT",
                     colWidths=[available*w/sum(weights) for w in weights])
        grid.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#" + ACCENT)),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#EDF3F4")]),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("TOPPADDING",(0,0),(-1,-1),6), ("BOTTOMPADDING",(0,0),(-1,-1),6),
        ]))
        if lv:
            first_total = len(lv.rows)
            grid.setStyle(TableStyle([
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEABOVE", (0, first_total), (-1, first_total), 0.8, colors.HexColor("#" + ACCENT)),
                ("BACKGROUND", (0, first_total), (-1, -1), colors.HexColor("#E1EAEC")),
                ("NOSPLIT", (0, -2), (-1, -1)),
            ]))
        story.extend([Spacer(1, 3), grid])
    pdf.build(story, onFirstPage=furniture, onLaterPages=furniture)
    return out.getvalue()


def filing_pairs(case, slug):
    pairs = case.get("einwendungspruefung")
    if not isinstance(pairs, list) or not pairs:
        raise ValueError(f"{slug}: Einwendung und Gegenbeleg für die Prüfung fehlen")
    documents = {doc["datei"]: doc for doc in case["dokumente"]}
    if len(documents) != len(case["dokumente"]):
        raise ValueError(f"{slug}: Dateinamen für die Einwendungsprüfung nicht eindeutig")
    for pair in pairs:
        filing, evidence = pair["eingabe"], pair["gegenpruefung"]
        if filing == evidence or filing not in documents or evidence not in documents:
            raise ValueError(f"{slug}: Eingabe und Gegenprüfung müssen zwei vorhandene Aktenstücke bezeichnen: {pair}")
        yield documents[filing], documents[evidence]


def filing_link(doc):
    title = doc["titel"].replace("|", "\\|")
    path = quote(f'{doc["phase"]}/{doc["datei"]}')
    return f'[{title}]({path}) ({doc["phase"]})'


def make_case(case, slug):
    documents = case["dokumente"]
    if {doc["phase"] for doc in documents} != set(PHASES):
        raise ValueError(f"{slug}: Grundakte und Nachreichungen erforderlich")
    prefix = f"testakte-{slug}"
    native_zip = f"downloads/{prefix}.zip"
    single_zip = f"downloads/{prefix}-einzelpdfs.zip"
    combined_pdf = f"gesamt-pdf/{prefix}_gesamt.pdf"
    originals, singles = {}, {}
    combined = PdfWriter()
    readme = [f'# {case["titel"]}', "", f'**Aktenzeichen {case["zeichen"]}**', "", case["einstieg"], "",
              "## Arbeitsauftrag", "", case["auftrag"], "", "## Downloads", "",
              NOTICE_MARKDOWN, "", "| Gesamtakte | Originalunterlagen | Einzel-PDFs |", "| --- | --- | --- |",
              f"| [Gesamt-PDF mit Lesezeichen]({combined_pdf}) | [Originalformat-ZIP]({native_zip}) | [Einzel-PDF-ZIP]({single_zip}) |"]
    for phase in PHASES:
        readme.extend(["", "## " + phase, "", case["nachreichung"] if phase == "Nachreichungen" else "Beginnen Sie mit diesen Unterlagen.", "",
                       "| Datum | Unterlage | Format |", "| --- | --- | --- |"])
        first_page = len(combined.pages)
        parent = None
        for doc in (d for d in documents if d["phase"] == phase):
            name = safe_member(doc["datei"])
            if "/" in name:
                raise ValueError(f"{slug}: kein einzelner Dateiname: {name}")
            rel = f"{phase}/{name}"
            single = phase + "__" + Path(name).stem + ".pdf"
            if rel in originals or single in singles:
                raise ValueError(f"{slug}: doppelter Dateiname: {rel}")
            rows = doc.get("tabelle", [])
            if rows and (not rows[0] or any(len(r) != len(rows[0]) for r in rows)):
                raise ValueError(f"{rel}: uneinheitliche Spaltenzahl")
            if Path(name).suffix in (".csv", ".xlsx") and len(rows) < 2:
                raise ValueError(f"{rel}: Tabelle ohne Datenzeilen")
            lv = None
            if "lv" in doc:
                if Path(name).suffix != ".xlsx":
                    raise ValueError(f"{rel}: LV-Preisspalten erfordern eine XLSX-Arbeitsmappe")
                lv = BillOfQuantities(doc)
            originals[rel] = native(doc, case, rel, lv)
            singles[single] = reading(doc, case, rel, lv)
            page = len(combined.pages)
            combined.append(PdfReader(io.BytesIO(singles[single])), import_outline=False)
            if parent is None:
                parent = combined.add_outline_item(title=phase, page_number=first_page)
            combined.add_outline_item(title=doc["titel"], page_number=page, parent=parent)
            label = doc["titel"].replace("|", "\\|")
            readme.append(f"| {german_date(doc)} | [{label}]({quote(rel)}) | {Path(name).suffix[1:].upper()} |")

    readme.extend(["", "## Eingaben prüfen", "",
                   "Was beantragt der Absender, was lässt sich anhand der Akte belegen und was bleibt offen? "
                   "Nutzen Sie die Nachreichungen in der zweiten Bearbeitungsrunde. "
                   f"Den [Prüfbogen für Einwendungen](../{PRUEFBOGEN}?raw=true) können Sie für jeden Vorgang ausfüllen.",
                   "", "| Eingabe | Unterlage zur Gegenprüfung |", "| --- | --- |"])
    for filing, evidence in filing_pairs(case, slug):
        readme.append(f"| {filing_link(filing)} | {filing_link(evidence)} |")
    readme.extend(["", "## Quellen", ""])
    readme.extend(f"- [{label}]({target})" for label, target in case["quellen"])
    readme.extend(["", "[Alle Interstate-Akten](../README.md)", ""])
    out = io.BytesIO()
    combined.add_metadata({"/Title": case["titel"], "/Subject": case["zeichen"]})
    combined.write(out)
    combined.close()
    return {**originals, native_zip: archive({NOTICE_FILENAME: NOTICE_BYTES, **originals}),
            single_zip: archive({NOTICE_FILENAME: NOTICE_BYTES, **singles}), combined_pdf: out.getvalue(),
            "README.md": "\n".join(readme).encode()}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--check", action="store_true", help="Dateinamen und Inhalt gegen die JSON-Quellen prüfen")
    args = cli.parse_args()
    sources = sorted(DATA.glob("*.json"))
    if not sources or any(not path.stem.startswith(f"{i:02d}-") for i, path in enumerate(sources, 1)):
        cli.error("JSON-Akten ab 01 ohne Lücken und mit eindeutiger Nummer anlegen.")
    unlisted = {p.name for p in OUTPUT.iterdir() if p.is_dir()} - {p.stem for p in sources}
    if unlisted:
        cli.error(f"Aktenordner ohne zugehörige JSON-Quelle: {sorted(unlisted)}")
    form = pruefbogen()
    collection = {NOTICE_FILENAME: NOTICE_BYTES, PRUEFBOGEN: form}
    guide = ["", "Deutsche Interstate AG · Niederlassung West", "",
             "Wählen Sie einen Fallordner. Bearbeiten Sie zuerst die Grundakte. "
             "Öffnen Sie die Nachreichungen nach der ersten Bearbeitungsrunde. "
             f"Für Ihre Prüfung der Eingaben verwenden Sie {PRUEFBOGEN} auf der obersten Ebene. "
             "Die Gesamt-PDF führt über Lesezeichen zu beiden Phasen. "
             "Das ZIP unter downloads enthält die Druckfassungen der einzelnen Unterlagen."]
    for source in sources:
        folder = OUTPUT / source.stem
        case = json.loads(source.read_text(encoding="utf-8"))
        assets = make_case(case, source.stem)
        guide.extend(["", f'{source.stem} · {case["titel"]}', case["zeichen"], "",
                      case["einstieg"], "", case["auftrag"], "", case["nachreichung"],
                      "", "Eingaben und Unterlagen zur Gegenprüfung"])
        for filing, evidence in filing_pairs(case, source.stem):
            guide.extend([f'  Eingabe: {filing["phase"]}/{filing["datei"]}',
                          f'  Gegenprüfung: {evidence["phase"]}/{evidence["datei"]}'])
        guide.extend(["", "Quellen:"])
        guide.extend(f"{label} · {target}" for label, target in case["quellen"])
        extra = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()} - assets.keys()
        if extra:
            raise ValueError(f"{folder.name}: zusätzliche Dateien im Aktenordner: {sorted(extra)}")
        for rel, data in assets.items():
            if rel.startswith((*PHASES, "gesamt-pdf/")) or rel.endswith("-einzelpdfs.zip"):
                collection[f"{source.stem}/{rel}"] = data
            deliver(folder / rel, data, args.check)
        print(f"{source.stem}: {len(assets) - 4} Aktenstücke")
    collection[NOTICE_FILENAME] += ("\n".join(guide) + "\n").encode("utf-8")
    deliver(OUTPUT / PRUEFBOGEN, form, args.check)
    deliver(COLLECTION_ZIP, archive(collection), args.check)
    print(COLLECTION_ZIP.relative_to(ROOT))


def deliver(path, data, check):
    if path.is_file() and path.read_bytes() == data:
        return
    if check:
        raise ValueError(f"Fehlend oder abweichend: {path.relative_to(ROOT)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


if __name__ == "__main__":
    main()
