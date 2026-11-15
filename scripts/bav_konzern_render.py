"""Native Aktenstücke für die vier bAV-Konzernmandate.

Die Fachdaten liegen getrennt in scripts/data/bav-konzern-faelle.
PDF/Word nutzen echte Times-New-Roman-Dateien. E-Mail-Anlagen werden erst
nach dem nativen Bestand angefügt, niemals als bloßer Anlagenhinweis.
"""
from __future__ import annotations

import csv
import hashlib
import mimetypes
import re
from datetime import datetime, timezone
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak

FIRM = "Kashiwara · Treuenfels Rechtsanwälte Partnerschaft mbB"
FIRM_ADDRESS = "Am Rheinbogen 18\n51373 Leverkusen"
INK = "172C3D"


def register_fonts(directory: Path):
    variants = {"BavTimes": "Times New Roman.ttf", "BavTimes-Bold": "Times New Roman Bold.ttf",
                "BavTimes-Italic": "Times New Roman Italic.ttf", "BavTimes-BoldItalic": "Times New Roman Bold Italic.ttf"}
    for name, filename in variants.items():
        path = directory / filename
        if not path.is_file():
            raise RuntimeError(f"Lizenzierte Times-New-Roman-TTF fehlt: {path}; BAV_FONT_DIR setzen")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily("BavTimes", normal="BavTimes", bold="BavTimes-Bold", italic="BavTimes-Italic", boldItalic="BavTimes-BoldItalic")


def safe_path(base, relative):
    p = Path(relative)
    if p.is_absolute() or ".." in p.parts or not p.parts or p.parts[0] not in {"Grundakte", "Fortsetzung"}:
        raise ValueError(f"Ungültiger Aktenpfad: {relative}")
    target = base / p
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def paras(item):
    body = item.get("body", [])
    return body if isinstance(body, list) else body.split("\n\n")


def sender(item, case):
    value = item.get("sender") or item.get("issuer") or case["client"]
    if isinstance(value, dict):
        return "\n".join(str(value[k]) for k in ("name", "address", "city") if value.get(k))
    return value


def recipient(item):
    value = item.get("recipient", "")
    if isinstance(value, dict):
        return "\n".join(str(value[k]) for k in ("name", "address", "city") if value.get(k))
    return value


def letter_style(item, case):
    issuer = sender(item, case)
    law = "Treuenfels" in issuer or "Kashiwara" in issuer
    if law:
        return {"name": "Kashiwara · Treuenfels", "sub": "RECHTSANWÄLTE PARTNERSCHAFT MBB", "address": FIRM_ADDRESS,
                "contact": "mail@kashiwara-treuenfels.example", "color": "203B50", "footer": "Dr. Kashiwara Harunobu · Dr. Nora Treuenfels   |   Leverkusen"}
    parts = issuer.splitlines()
    if len(parts) == 1 and "," in issuer and re.search(r"\b\d{5}\b", issuer):
        parts = [p.strip() for p in issuer.split(",")]
    palette = ["2E5664", "5E4D41", "3D5B55", "434C70"]
    color = palette[int(hashlib.sha256(parts[0].encode()).hexdigest()[:2], 16) % len(palette)]
    return {"name": parts[0], "sub": item.get("department", "Betriebliche Altersversorgung"),
            "address": " · ".join(parts[1:]), "contact": item.get("from_email", ""), "color": color,
            "footer": item.get("footer", parts[0])}


def masthead_size(name):
    size = 22 if len(name) < 40 else 17
    while pdfmetrics.stringWidth(name, "BavTimes-Bold", size) > 481 and size > 12:
        size -= .5
    if pdfmetrics.stringWidth(name, "BavTimes-Bold", size) > 481:
        raise ValueError(f"Absender benötigt mehrzeiligen Briefkopf: {name}")
    return size


def is_heading(text):
    return bool(re.fullmatch(r"\d+(?:\.\d+)*\.?\s+[^\n]{1,110}", text))


def date_label(value):
    try:
        return datetime.fromisoformat(value).strftime("%d.%m.%Y")
    except ValueError:
        return value


def pdf(path, item, case):
    style = letter_style(item, case)
    title = item.get("subject") or item["title"]
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=57, rightMargin=57,
                            topMargin=119, bottomMargin=65, title=title, author=style["name"])
    body = ParagraphStyle("body", fontName="BavTimes", fontSize=11, leading=15.2, spaceAfter=10,
                          textColor=HexColor("#20262C"), allowWidows=0, allowOrphans=0)
    section = ParagraphStyle("section", parent=body, fontName="BavTimes-Bold", spaceBefore=7,
                             spaceAfter=9, keepWithNext=True)
    subject = ParagraphStyle("subject", parent=body, fontName="BavTimes-Bold", fontSize=15,
                             leading=18, spaceBefore=14, spaceAfter=17, keepWithNext=True)
    meta = ParagraphStyle("meta", parent=body, fontSize=9, leading=12, spaceAfter=7)

    def p(t, s):
        return Paragraph(escape(str(t)).replace("\n", "<br/>"), s)

    flow = []
    if recipient(item):
        flow += [p(recipient(item), body), Spacer(1, 8)]
    if item.get("date"):
        flow.append(p(f"{date_label(item['date'])}   |   {item.get('id', '')}", meta))
    flow.append(p(title, subject))
    for paragraph in paras(item):
        flow.append(p(paragraph, section if is_heading(paragraph) else body))
    if item.get("signature"):
        flow += [Spacer(1, 8), p(item["signature"], body)]

    def page(c, d):
        w, h = A4
        c.setFillColor(HexColor("#" + style["color"]))
        c.setFont("BavTimes-Bold", masthead_size(style["name"]))
        c.drawString(57, h - 52, style["name"])
        c.setFont("BavTimes", 8)
        c.drawString(58, h - 68, style["sub"])
        c.setStrokeColor(HexColor("#" + style["color"]))
        c.setLineWidth(.7)
        c.line(57, h - 82, w - 57, h - 82)
        address = " · ".join(style["address"].splitlines())
        c.setFont("BavTimes", 8)
        if pdfmetrics.stringWidth(address, "BavTimes", 8) > w - 114:
            raise ValueError(f"Briefkopfadresse passt nicht: {address}")
        c.drawString(57, h - 97, address)
        c.setFillColor(HexColor("#59646C"))
        c.setFont("BavTimes", 8)
        if pdfmetrics.stringWidth(style["footer"], "BavTimes", 8) > w - 114:
            raise ValueError(f"Fußzeile passt nicht: {style['footer']}")
        c.drawString(57, 43, style["footer"])
        c.drawString(57, 30, style["contact"])
        c.drawRightString(w - 57, 30, f"{item.get('id', '')}   ·   Seite {d.page}")

    def canvas(*a, **kw):
        kw["invariant"] = 1
        return Canvas(*a, **kw)
    doc.build(flow, onFirstPage=page, onLaterPages=page, canvasmaker=canvas)


def docx(path, item, case):
    style = letter_style(item, case)
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(4.0), Cm(2.3)
    sec.left_margin = sec.right_margin = Cm(2)
    sec.header_distance, sec.footer_distance = Cm(1.3), Cm(1.0)
    for name in ("Normal", "Title", "Heading 1", "Heading 2"):
        s = doc.styles[name]
        s.font.name, s.font.size = "Times New Roman", Pt(11)
        s.font.color.rgb = RGBColor.from_string("20262C")
        for rfonts in s.element.findall('.//' + qn('w:rFonts')):
            for attr in list(rfonts.attrib):
                if 'theme' in attr.lower():
                    del rfonts.attrib[attr]
        for border in s.element.findall('.//' + qn('w:pBdr')):
            border.getparent().remove(border)
    normal = doc.styles["Normal"].paragraph_format
    normal.line_spacing = 1.14
    normal.space_after = Pt(9)
    doc.styles["Title"].font.size = Pt(16)
    doc.styles["Title"].font.bold = True
    doc.styles["Title"].paragraph_format.space_after = Pt(17)
    for name in ("Heading 1", "Heading 2"):
        doc.styles[name].font.bold = True
        doc.styles[name].paragraph_format.space_before = Pt(11)
        doc.styles[name].paragraph_format.space_after = Pt(9)
    h = sec.header.paragraphs[0]
    h.paragraph_format.space_after = Pt(2)
    run = h.add_run(style["name"])
    run.font.name, run.font.size, run.font.bold = "Times New Roman", Pt(masthead_size(style["name"])), True
    run.font.color.rgb = RGBColor.from_string(style["color"])
    for text in (style["sub"], " · ".join(style["address"].splitlines())):
        p = sec.header.add_paragraph(text)
        p.paragraph_format.space_after = Pt(3)
        for r in p.runs:
            r.font.size = Pt(8)
    f = sec.footer.paragraphs[0]
    f.add_run(style["footer"] + "\n" + style["contact"] + "   ·   " + item.get("id", "") + "   ·   Seite ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    f._p.append(field)
    for r in f.runs:
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor.from_string("59646C")
    if recipient(item):
        doc.add_paragraph(recipient(item))
    doc.add_paragraph(f"{date_label(item.get('date', ''))}   |   {item.get('id', '')}")
    doc.add_paragraph(item.get("subject") or item["title"], "Title")
    for paragraph in paras(item):
        p = doc.add_paragraph(paragraph, "Heading 1" if is_heading(paragraph) else "Normal")
        p.paragraph_format.widow_control = True
    if item.get("signature"):
        doc.add_paragraph(item["signature"])
    doc.core_properties.author = style["name"]
    doc.core_properties.title = item["title"]
    doc.core_properties.created = doc.core_properties.modified = datetime(2026, 11, 15, tzinfo=timezone.utc)
    doc.save(path)


def text_file(path, item, case):
    path.write_text("\n\n".join([item["title"], *paras(item)]) + "\n", encoding="utf-8")


def csv_file(path, item, case):
    data = item.get("csv", item)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        w = csv.writer(stream, delimiter=";")
        w.writerow(data.get("columns") or data.get("headers"))
        w.writerows(data["rows"])


def email_file(path, item, case, base):
    msg = EmailMessage(policy=SMTP)
    def addr(value, fallback):
        return value if value and "@" in value else fallback
    msg["From"] = addr(item.get("from_email"), "projekt@" + case.get("domain", case["slug"] + ".example"))
    msg["To"] = addr(item.get("to_email"), "mail@kashiwara-treuenfels.example")
    msg["Subject"] = item.get("subject") or item["title"]
    date = item.get("date", "2026-11-15")
    try:
        dt = datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
    except ValueError:
        dt = datetime.strptime(date, "%d.%m.%Y").replace(tzinfo=timezone.utc)
    msg["Date"] = format_datetime(dt)
    digest = hashlib.sha256((case["slug"] + item["id"]).encode()).hexdigest()[:24]
    msg["Message-ID"] = f"<{digest}@aktenpost.example>"
    msg.set_content("\n\n".join(paras(item)) + ("\n\n" + item["signature"] if item.get("signature") else ""))
    for relative in item.get("attachments", []):
        attach = safe_path(base, relative)
        mime = mimetypes.guess_type(attach.name)[0] or "application/octet-stream"
        main, sub = mime.split("/", 1)
        msg.add_attachment(attach.read_bytes(), maintype=main, subtype=sub, filename=attach.name)
    if msg.is_multipart():
        msg.set_boundary("bav-" + digest)
    path.write_bytes(msg.as_bytes())


def screenshot(path, item, case):
    """Lesbarer rekonstruierter Kommunikationsauszug, keine echte UI behauptet."""
    font_dir = Path("/System/Library/Fonts/Supplemental")
    font = ImageFont.truetype(str(font_dir / "Arial.ttf"), 25)
    bold = ImageFont.truetype(str(font_dir / "Arial Bold.ttf"), 28)
    lines = []
    for p in paras(item):
        lines.extend(textwrap.wrap(p, width=77))
        lines.append("")
    height = max(680, 220 + 36 * len(lines))
    im = Image.new("RGB", (1200, height), "#F4F6F8")
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1200, 110), fill="#283D51")
    size = 28
    while dr.textlength(item["title"], font=bold) > 1110 and size > 20:
        size -= 1
        bold = ImageFont.truetype(str(font_dir / "Arial Bold.ttf"), size)
    if dr.textlength(item["title"], font=bold) > 1110:
        raise ValueError(f"Screenshot-Titel zu lang: {item['title']}")
    dr.text((42, 27), item["title"], font=bold, fill="white")
    dr.text((42, 73), "Kommunikationsauszug · Rekonstruktion aus dem Export", font=font, fill="#D7E3EC")
    dr.text((42, 139), f"{item.get('date', '')}   {sender(item, case).splitlines()[0]}", font=font, fill="#3C5364")
    y = 200
    for line in lines:
        dr.text((42, y), line, font=font, fill="#1D2A35")
        y += 36
    im.save(path)


def workbook_pdf(source):
    """A4-Lesefassung breiter Rohregister ohne unlesbare Ganzblatt-Skalierung.

    Jede Zelle ab der Datenüberschrift erscheint. Die erste Kennspalte wiederholt
    sich bei horizontaler Teilung. Zahlen stammen aus dem gespeicherten Cache,
    dessen Formeln der eigenständige Test zusätzlich nachrechnet.
    """
    from openpyxl import load_workbook
    import io
    from datetime import date
    book = load_workbook(source, data_only=True)
    stream = io.BytesIO()
    width, height = landscape(A4)
    doc = SimpleDocTemplate(stream, pagesize=(width, height), leftMargin=36, rightMargin=36,
                            topMargin=42, bottomMargin=42, title=source.stem, author="Konzerncontrolling")
    cell = ParagraphStyle("cell", fontName="BavTimes", fontSize=9.5, leading=12, spaceAfter=0)
    head = ParagraphStyle("head", parent=cell, fontName="BavTimes-Bold", textColor=HexColor("#FFFFFF"))
    title = ParagraphStyle("title", parent=cell, fontName="BavTimes-Bold", fontSize=16, leading=19, spaceAfter=10)
    note = ParagraphStyle("note", parent=cell, spaceAfter=10, textColor=HexColor("#526473"))
    flow = []
    for sh in book:
        columns = [i for i in range(1, sh.max_column+1) if sh.cell(5, i).value is not None]
        if not columns:
            raise ValueError(f"Datenkopf fehlt: {source} / {sh.title}")
        chunks = [columns] if len(columns) <= 6 else [[columns[0], *columns[i:i+5]] for i in range(1,len(columns),5)]
        for chunk_index, group in enumerate(chunks):
            if flow: flow.append(PageBreak())
            def p(value, style=cell): return Paragraph(escape(str(value)).replace("\n", "<br/>"), style)
            flow.append(p(sh.cell(2,1).value or source.stem, title))
            label = f"{sh.title}"
            if len(chunks)>1: label += f" · Spaltenabschnitt {chunk_index+1} von {len(chunks)} · Kennung in erster Spalte wiederholt"
            flow.append(p(label, note))
            rows = [[p(str(sh.cell(5,j).value).replace("_", " "), head) for j in group]]
            for i in range(6, sh.max_row+1):
                if all(sh.cell(i,j).value is None for j in columns): continue
                row = []
                for j in group:
                    c = sh.cell(i,j); value = c.value
                    if value is None: value = ""
                    elif isinstance(value, (datetime,date)): value=value.strftime("%d.%m.%Y")
                    elif isinstance(value, (float,int)):
                        if "%" in c.number_format: value=f"{100*value:.1f} %".replace(".",",")
                        elif ".00" in c.number_format: value=f"{value:,.2f}".replace(",","_").replace(".",",").replace("_",".")
                        elif int(value)==value: value=str(int(value))
                        else: value=str(value).replace(".",",")
                    row.append(p(value))
                rows.append(row)
            available=width-72
            widths=[available/len(group)]*len(group)
            table=Table(rows,colWidths=widths,repeatRows=1,hAlign="LEFT")
            table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),HexColor("#203B50")),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                                       ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#FFFFFF"),HexColor("#F0F4F6")]),
                                       ("BOTTOMPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),
                                       ("LINEBELOW",(0,0),(-1,0),.5,HexColor("#B6C3CB"))]))
            flow.append(table)
    def footer(c,d):
        c.setFont("BavTimes",8);c.setFillColor(HexColor("#59646C"))
        c.drawString(36,23,source.name);c.drawRightString(width-36,23,f"Seite {d.page}")
    def canvas(*a,**kw): kw["invariant"]=1;return Canvas(*a,**kw)
    doc.build(flow,onFirstPage=footer,onLaterPages=footer,canvasmaker=canvas)
    book.close()
    return stream.getvalue()

