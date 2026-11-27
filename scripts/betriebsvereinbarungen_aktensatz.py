"""Briefkopf, Office-Vorlagen und Lesefassungen der Copilot-Verhandlungsakte."""
import io
import math
from email.message import EmailMessage
from email.policy import SMTP
from pathlib import Path

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle

from akteneingang.belegdaten import SECTION_HEADING, german_date, mail_address, mail_time, paragraph, widths
from akteneingang.dokumente import office_bytes, sha

ACCENT = "234C5A"
MUTED = "4C6370"


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


def worksheet(doc, case):
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
    sheet.print_title_rows = f"{heading}:{heading}"
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    sheet.page_setup.fitToWidth, sheet.page_setup.fitToHeight = 1, 0
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
    sheet.page_setup.orientation = "landscape" if len(spec) >= 4 else "portrait"
    sheet.print_area = sheet.dimensions
    return office_bytes(book)


def native(doc, case, name):
    ext = Path(name).suffix
    if ext == ".docx":
        return word(doc, case)
    if ext == ".xlsx":
        return worksheet(doc, case)
    text = "\n\n".join(doc["text"])
    if doc.get("tabelle"):
        text += "\n\n" + "\n".join("\t".join(map(str, row)) for row in doc["tabelle"])
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


def reading(doc, case, name):
    rows = doc.get("tabelle", [])
    page_size = landscape(A4) if rows and len(rows[0]) >= 4 else A4
    out = io.BytesIO()
    pdf = SimpleDocTemplate(out, pagesize=page_size, leftMargin=48, rightMargin=48,
                            topMargin=56, bottomMargin=47,
                            invariant=1, title=doc["titel"], author=doc["von"])
    kinds = {".docx": "Schriftstück", ".xlsx": "Tabellenblatt", ".csv": "Datenexport", ".eml": "E-Mail"}
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
        else:
            story.append(paragraph(text))
    if rows:
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
        story.extend([Spacer(1, 3), grid])
    pdf.build(story, onFirstPage=furniture, onLaterPages=furniture)
    return out.getvalue()
