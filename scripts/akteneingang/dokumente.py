"""Setzt die redaktionellen Belege in ihre Arbeitsformate und in lesbare Druckfassungen."""

from __future__ import annotations

import hashlib
import io
import re
import unicodedata
from datetime import date, datetime, time
from email.headerregistry import Address
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
from zoneinfo import ZoneInfo

import reportlab
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def sha(data):
    return hashlib.sha256(data).hexdigest()


def simple(value):
    value = (
        unicodedata.normalize("NFKD", value.replace("ß", "ss"))
        .encode("ascii", "ignore")
        .decode()
    )
    return re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower() or "post"


def add_member(archive, name, data):
    info = ZipInfo(name, (2000, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    archive.writestr(info, data)


def office_bytes(doc):
    raw, stable = io.BytesIO(), io.BytesIO()
    doc.save(raw)
    with ZipFile(raw) as old, ZipFile(stable, "w") as new:
        for name in old.namelist():
            blob = old.read(name)
            if name == "docProps/core.xml":
                blob = re.sub(
                    rb"(<dcterms:(?:created|modified)\b[^>]*>)[^<]+",
                    rb"\g<1>2000-01-01T00:00:00Z",
                    blob,
                )
            add_member(new, name, blob)
    return stable.getvalue()


def chat_rows(item):
    result = []
    for text in item["text"]:
        who, sep, body = text.partition(":")
        if not sep or not body.strip():
            raise ValueError("Chatnachricht ohne Sprecher oder Nachricht: " + text)
        result.append((who.strip(), body.strip()))
    return result


def chat_image(item, identity):
    font_dir = Path(reportlab.__file__).parent / "fonts"
    regular = ImageFont.truetype(str(font_dir / "Vera.ttf"), 22)
    bold = ImageFont.truetype(str(font_dir / "VeraBd.ttf"), 20)
    small = ImageFont.truetype(str(font_dir / "Vera.ttf"), 17)
    heading = ImageFont.truetype(str(font_dir / "VeraBd.ttf"), 25)
    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))

    def lines(value, font, width):
        parts = []
        for word in value.split():
            if parts and draw.textlength(parts[-1] + " " + word, font=font) <= width:
                parts[-1] += " " + word
            else:
                parts.append(word)
        return parts

    brand = item.get("dienst") or (
        "Signal" if int(sha(identity.encode())[:2], 16) % 2 else "WhatsApp"
    )
    if "signal" in (item["titel"] + " " + item["an"]).lower():
        brand = "Signal"
    elif "whatsapp" in (item["titel"] + " " + item["an"]).lower():
        brand = "WhatsApp"
    signal = brand == "Signal"
    group = lines(item["an"], heading, 575)
    messages = chat_rows(item)
    bubbles = [
        (speaker, lines(speaker, bold, 548), lines(body, regular, 548))
        for speaker, body in messages
    ]
    header = 75 + 30 * len(group)
    height = (
        header
        + 86
        + sum(32 + 25 * len(who) + 31 * len(body) for _, who, body in bubbles)
    )
    img = Image.new("RGB", (700, height), "#eef2f8" if signal else "#ece8df")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 700, header), fill="#314a83" if signal else "#165e53")
    d.text((25, 14), brand, font=small, fill="white")
    for i, line in enumerate(group):
        d.text((28, 46 + i * 30), line, font=heading, fill="white")
    stamp = item.get("datum") or "Gruppennachrichten"
    d.text((350, header + 17), stamp, font=small, fill="#44505b", anchor="mt")
    y = header + 56
    for speaker, who, body in bubbles:
        incoming = speaker != messages[0][0]
        x = 20 if incoming else 86
        h = 19 + 25 * len(who) + 31 * len(body)
        d.rounded_rectangle(
            (x, y, x + 593, y + h),
            13,
            fill="#ffffff" if incoming else ("#dbe5ff" if signal else "#d8efcb"),
        )
        for i, line in enumerate(who):
            d.text((x + 16, y + 7 + i * 25), line, font=bold, fill="#354967")
        for i, line in enumerate(body):
            d.text(
                (x + 16, y + 9 + len(who) * 25 + i * 31),
                line,
                font=regular,
                fill="#1b2229",
            )
        y += h + 13
    data = io.BytesIO()
    img.save(data, format="PNG", optimize=True)
    return data.getvalue()


def table_rows(item):
    rows = [[s.strip() for s in line.split("|")] for line in item["text"]]
    if (
        len(rows) < 2
        or len(rows[0]) < 2
        or any(len(row) != len(rows[0]) for row in rows)
    ):
        raise ValueError("Unregelmäßige Tabellenstruktur: " + item["titel"])
    return rows


def read_pdf(item):
    out = io.BytesIO()
    kind = item["typ"]
    kind_label = {
        "eml": "E-Mail",
        "chat": "Gruppennachrichten",
        "notiz": "Gesprächs- und Vorgangsnotiz",
        "brief": "Korrespondenz",
        "tabelle": "Tabellenblatt",
    }[kind]
    accent = {
        "eml": "#344d69",
        "chat": "#2f6257",
        "notiz": "#68533d",
        "brief": "#344f65",
        "tabelle": "#295b59",
    }[kind]
    doc = SimpleDocTemplate(
        out,
        pagesize=A4,
        leftMargin=51,
        rightMargin=51,
        topMargin=68,
        bottomMargin=56,
        title=item["titel"],
        author=item["von"],
    )

    def par(s, font="Times-Roman", size=11, leading=15, col="#1d2c36"):
        return Paragraph(
            escape(s).replace("\n", "<br/>"),
            ParagraphStyle(
                "p",
                fontName=font,
                fontSize=size,
                leading=leading,
                textColor=colors.HexColor(col),
            ),
        )

    def furniture(c, _):
        c.saveState()
        c.setFillColor(colors.HexColor(accent))
        c.rect(51, 790, 62, 3, fill=1, stroke=0)
        c.setFont("Helvetica", 9)
        c.drawRightString(543, 788, kind_label)
        c.setStrokeColor(colors.HexColor("#ced4d6"))
        c.line(51, 45, 543, 45)
        c.setFont("Helvetica", 8)
        c.drawRightString(543, 30, f"Blatt {c.getPageNumber()}")
        c.restoreState()

    story = [
        par(item["titel"], "Helvetica-Bold", 18, 22, accent),
        Spacer(1, 14),
        par(item["von"], "Helvetica-Bold", 10, 13),
        par("An " + item["an"], "Helvetica", 10, 13),
    ]
    if item.get("_fachfassung") and kind == "brief":
        story = [
            par(item["von"], "Helvetica-Bold", 16, 20, accent),
            Spacer(1, 30),
            par(item["an"], "Helvetica", 11, 15),
            Spacer(1, 25),
            par(item["titel"], "Times-Bold", 14, 18),
        ]
    if item.get("_antworttitel"):
        story.append(par("Bezug: " + item["_antworttitel"], "Helvetica", 9, 13))
    if item.get("_anlagetitel"):
        story.append(par("Anlage: " + item["_anlagetitel"], "Helvetica", 9, 13))
    if item.get("datum"):
        story.append(
            par(
                date.fromisoformat(item["datum"]).strftime("%d.%m.%Y"),
                "Helvetica",
                9,
                13,
            )
        )
    if kind == "eml" and not item.get("datum"):
        story.append(par("Gespeicherter Entwurf", "Helvetica", 9, 13))
    story.append(Spacer(1, 20))
    if kind == "tabelle":
        table = table_rows(item)
        rows = [
            [
                par(
                    v,
                    "Helvetica-Bold" if i == 0 else "Helvetica",
                    9,
                    12,
                    "#ffffff" if i == 0 else "#263842",
                )
                for v in row
            ]
            for i, row in enumerate(table)
        ]
        tab = Table(
            rows, colWidths=[(A4[0] - 114) / len(rows[0])] * len(rows[0]), repeatRows=1
        )
        tab.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(accent)),
                    (
                        "ROWBACKGROUNDS",
                        (0, 1),
                        (-1, -1),
                        [colors.white, colors.HexColor("#eef3f4")],
                    ),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                ]
            )
        )
        story.append(tab)
    elif kind == "chat":
        # Text bleibt im Ausdruck durchsuchbar, das Original im Arbeits-ZIP ist eine Bilddatei.
        for who, body in chat_rows(item):
            story.extend(
                [
                    par(who, "Helvetica-Bold", 10, 13, accent),
                    par(body, "Helvetica", 11, 15),
                    Spacer(1, 10),
                ]
            )
    else:
        for text in item["text"]:
            story.extend(
                [
                    par(text, "Helvetica" if kind == "eml" else "Times-Roman"),
                    Spacer(1, 9),
                ]
            )
    doc.build(
        story,
        onFirstPage=furniture,
        onLaterPages=furniture,
        canvasmaker=lambda *a, **k: Canvas(*a, **{**k, "invariant": 1}),
    )
    return out.getvalue()


def render(item, identity):
    printed = read_pdf(item)
    kind = item["typ"]
    if kind == "brief":
        return "pdf", printed, printed
    if kind == "chat":
        return "png", chat_image(item, identity), printed
    if kind == "eml":
        m = EmailMessage(policy=SMTP)
        for key, field in [("von", "From"), ("an", "To")]:
            name = item[key]
            m[field] = Address(
                display_name=name, username=simple(name)[:48], domain="fallpost.example"
            )
        if item.get("datum"):
            clock = int(sha(identity.encode())[:8], 16) % 540
            stamp = datetime.combine(
                date.fromisoformat(item["datum"]),
                time(8 + clock // 60, clock % 60),
                ZoneInfo("Europe/Berlin"),
            )
            m["Date"] = format_datetime(stamp)
        else:
            # Ein gespeicherter Entwurf hat noch keinen Versandzeitpunkt.
            m["X-Unsent"] = "1"
        m["Message-ID"] = "<" + sha(identity.encode())[:24] + "@fallpost.example>"
        m["Subject"] = item["titel"]
        m.set_content("\n\n".join(item["text"]), charset="utf-8")
        return "eml", m.as_bytes(), printed
    if kind == "notiz":
        doc = Document()
        doc.core_properties.author = item["von"]
        doc.core_properties.title = item["titel"]
        norm = doc.styles["Normal"]
        norm.font.name = "Times New Roman"
        norm.font.size = Pt(11)
        doc.sections[0].header.paragraphs[0].text = item["von"]
        doc.sections[0].left_margin = Cm(2.5)
        doc.add_heading(item["titel"], 0)
        if item.get("_fachfassung"):
            kopf = doc.sections[0].header.paragraphs[0].runs[0]
            kopf.font.name = "Calibri"
            kopf.font.size = Pt(10)
            kopf.font.color.rgb = RGBColor.from_string("285763")
            doc.sections[0].top_margin = Cm(2.7)
            norm.paragraph_format.space_after = Pt(9)
            norm.paragraph_format.line_spacing = 1.16
            block = doc.add_table(rows=0, cols=2)
            fakten = [("Aufgenommen von", item["von"]), ("Für", item["an"])]
            if item.get("datum"):
                fakten.append(
                    ("Datum", date.fromisoformat(item["datum"]).strftime("%d.%m.%Y"))
                )
            for feld, wert in fakten:
                left, right = block.add_row().cells
                left.width = Cm(4)
                left.paragraphs[0].add_run(feld).italic = True
                right.paragraphs[0].add_run(wert)
            doc.add_paragraph()
        else:
            doc.add_paragraph(
                "Für "
                + item["an"]
                + ("  ·  " + item["datum"] if item.get("datum") else "")
            )
        for line in item["text"]:
            doc.add_paragraph(line)
        return "docx", office_bytes(doc), printed
    wb = Workbook()
    ws = wb.active
    ws.title = "Aufstellung"
    ws.append([item["titel"]])
    ws.append([item["von"], item["an"], item.get("datum")])
    ws.append([])
    rows = table_rows(item)
    ws.append(rows[0])
    numeric = set(item.get("zahlenspalten", []))
    if not numeric <= set(range(1, len(rows[0]) + 1)):
        raise ValueError("Ungültige Zahlenspalte in " + item["titel"])
    for row in rows[1:]:
        values = list(row)
        for column in numeric:
            text = row[column - 1]
            if not re.fullmatch(r"-?\d+(?:,\d+)?", text):
                raise ValueError("Unklarer Zahlenwert in " + item["titel"] + ": " + text)
            values[column - 1] = float(text.replace(",", ".")) if "," in text else int(text)
        ws.append(values)
        for column in numeric:
            if "," in row[column - 1]:
                ws.cell(ws.max_row, column).number_format = "#,##0.00"
    for c in ws[4]:
        c.fill = PatternFill("solid", fgColor="255850")
        c.font = Font(bold=True, color="FFFFFF")
    for i in range(len(rows[0])):
        ws.column_dimensions[get_column_letter(i + 1)].width = min(
            62, max(18, max(len(row[i]) for row in rows) + 2)
        )
    for row in ws.iter_rows(min_row=4):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if cell.data_type == "f":
                cell.data_type = "s"
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A5"
    return "xlsx", office_bytes(wb), printed
