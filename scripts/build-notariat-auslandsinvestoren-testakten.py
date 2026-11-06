#!/usr/bin/env python3
"""Erzeugt die nativen Aktenstücke zweier grenzüberschreitender Notariatsakten.

Die Sachverhalte stehen getrennt in notariat-auslandsinvestoren-material.json.
Gesamt-PDF und ZIPs werden anschließend mit den zentralen Testakten-Buildern
erzeugt. Dieser Builder greift ausschließlich auf seine beiden Aktenordner zu.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
import hashlib
import json
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from PIL import Image, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from akten_build_runtime import screen_font, serif_font_path
from testakte_disclaimer import NOTICE_MARKDOWN


ROOT = Path(__file__).resolve().parents[1]
SLUGS = {
    "notariat-berlin-mumbai-gesellschafterliste",
    "notariat-berlin-vae-vertretungsnachweis",
}
STAMP = datetime(2026, 11, 6, 10, 0, tzinfo=timezone.utc)
ZIP_STAMP = (2026, 11, 6, 10, 0, 0)
PROFILES = {
    "notary": "NOTARIAT · URKUNDEN UND VOLLZUG",
    "lawyer": "RECHTSANWÄLTE · GESELLSCHAFTSRECHT",
    "court": "HANDELSREGISTER · REGISTERABTEILUNG",
    "company": "GESCHÄFTSFÜHRUNG · BETEILIGUNGEN",
    "indian": "CORPORATE RECORDS · MUMBAI, MAHARASHTRA",
    "uae": "CORPORATE RECORDS · UNITED ARAB EMIRATES",
    "neutral": "GESCHÄFTSUNTERLAGEN",
}
MUTED = "62676B"


def stable_ooxml(path: Path) -> None:
    """Normalisiert nur Container-Metadaten; Inhalt bleibt unverändert."""
    for prefix, namespace in {
        "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }.items():
        ET.register_namespace(prefix, namespace)
    with zipfile.ZipFile(path) as archive:
        parts = [(entry.filename, archive.read(entry.filename)) for entry in archive.infolist()]
    temporary = path.with_suffix(path.suffix + ".tmp")
    with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for name, payload in parts:
            if name == "docProps/core.xml":
                core = ET.fromstring(payload)
                for key in ("created", "modified"):
                    node = core.find(f"{{http://purl.org/dc/terms/}}{key}")
                    if node is not None:
                        node.text = STAMP.strftime("%Y-%m-%dT%H:%M:%SZ")
                payload = ET.tostring(core, encoding="utf-8", xml_declaration=True)
            entry = zipfile.ZipInfo(name, ZIP_STAMP)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o600 << 16
            archive.writestr(entry, payload)
    temporary.replace(path)


def paragraphs(text: str):
    for block in re.split(r"\n\s*\n", text.strip()):
        yield block.strip()


def is_heading(block: str) -> bool:
    return bool(re.match(r"^\d+(?:\.\d+)*\.?\s+\S", block)) and "\n" not in block and len(block) < 140


def add_text(paragraph, text: str) -> None:
    for index, line in enumerate(text.splitlines()):
        if index:
            paragraph.add_run().add_break()
        paragraph.add_run(line)


def footer_label(record: dict) -> str:
    label = record.get("reference", record.get("author", "").split("|")[0].strip())
    return label if len(label) <= 72 else label[:69].rstrip() + "…"


def create_docx(path: Path, record: dict, case: dict) -> None:
    document = Document()
    section = document.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(2.1), Cm(2.0)
    section.left_margin, section.right_margin = Cm(2.3), Cm(2.2)
    section.header_distance, section.footer_distance = Cm(0.8), Cm(0.8)
    for name in ("Normal", "Title", "Subtitle", "Heading 1", "Heading 2", "Header", "Footer"):
        style = document.styles[name]
        style.font.name = "Times New Roman"
        style.font.size = Pt(11)
        style.font.color.rgb = RGBColor(0, 0, 0)
        fonts = style.element.get_or_add_rPr().rFonts
        for attribute in list(fonts.attrib):
            if "theme" in attribute.lower():
                del fonts.attrib[attribute]
        for attribute in ("ascii", "hAnsi", "eastAsia", "cs"):
            fonts.set(qn("w:" + attribute), "Times New Roman")
    normal = document.styles["Normal"].paragraph_format
    normal.space_after = Pt(7)
    normal.line_spacing = 1.12
    normal.widow_control = True
    for name in ("Heading 1", "Heading 2"):
        style = document.styles[name]
        style.font.bold = True
        style.font.size = Pt(11.5)
        style.paragraph_format.space_before = Pt(10)
        style.paragraph_format.space_after = Pt(7)
        style.paragraph_format.keep_with_next = True
    header = section.header.paragraphs[0]
    header.paragraph_format.space_after = Pt(0)
    run = header.add_run(PROFILES.get(record.get("profile", "neutral"), PROFILES["neutral"]))
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor.from_string(MUTED)
    letterhead = document.add_paragraph()
    letterhead.paragraph_format.space_after = Pt(3)
    name = record.get("author", "").split("|")[0].strip()
    run = letterhead.add_run(name)
    run.bold = True
    run.font.size = Pt(15)
    remaining = " | ".join(part.strip() for part in record.get("author", "").split("|")[1:])
    if remaining:
        contact = document.add_paragraph(remaining)
        contact.paragraph_format.space_after = Pt(12)
        for run in contact.runs:
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor.from_string(MUTED)
    else:
        letterhead.paragraph_format.space_after = Pt(14)
    recipient = record.get("to", "")
    if recipient:
        p = document.add_paragraph()
        p.paragraph_format.space_after = Pt(9)
        add_text(p, recipient.replace(" | ", "\n"))
    p = document.add_paragraph(record.get("date", case.get("date", "")))
    p.paragraph_format.space_after = Pt(9)
    p.alignment = 2
    p = document.add_paragraph()
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(record["title"])
    r.bold = True
    r.font.size = Pt(12)
    for block in paragraphs(record["text"]):
        p = document.add_paragraph(style="Heading 1" if is_heading(block) else "Normal")
        add_text(p, block)
    footer = section.footer.paragraphs[0]
    footer.alignment = 2
    footer.paragraph_format.space_after = Pt(0)
    footer.add_run(f"{record['n']:02d} · {footer_label(record)}  |  Seite ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    for run in footer.runs:
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor.from_string(MUTED)
    props = document.core_properties
    props.title = record["title"]
    props.author = name
    props.subject = case["title"]
    props.created = props.modified = STAMP
    document.save(path)
    stable_ooxml(path)


def init_pdf_fonts() -> None:
    for key, bold in (("NotariatTNR", False), ("NotariatTNRBold", True)):
        source = serif_font_path(bold=bold)
        # Die Enddokumente verlangen die auf dieser Maschine vorhandene lizenzierte
        # Times New Roman. Eine andere Familie wird nicht unter diesem Namen geladen.
        face = TTFont(key, str(source))
        if "times" not in face.face.name.decode("latin1", errors="replace").lower():
            raise RuntimeError("Times New Roman fehlt; AKTEN_FONT_DIR auf legitim vorhandene TTFs setzen.")
        pdfmetrics.registerFont(face)


def create_pdf(path: Path, record: dict, case: dict) -> None:
    body = ParagraphStyle("Aktenbrief", fontName="NotariatTNR", fontSize=11, leading=14.2, spaceAfter=8)
    heading = ParagraphStyle("Aktenüberschrift", parent=body, fontName="NotariatTNRBold", spaceBefore=9, keepWithNext=True)
    title = ParagraphStyle("Betreff", parent=heading, fontSize=12, leading=15, spaceBefore=0, spaceAfter=14)
    masthead = ParagraphStyle("Absender", parent=heading, fontSize=15, leading=18, spaceAfter=4)
    detail = ParagraphStyle("Detail", parent=body, fontSize=9, leading=12, textColor=colors.HexColor("#62676B"), spaceAfter=14)
    story = [Paragraph(escape(record.get("author", "").split("|")[0].strip()), masthead)]
    remaining = " | ".join(p.strip() for p in record.get("author", "").split("|")[1:])
    if remaining:
        story.append(Paragraph(escape(remaining), detail))
    else:
        story.append(Spacer(1, 10))
    if record.get("to"):
        story.append(Paragraph(escape(record["to"]).replace(" | ", "<br/>"), body))
    right = ParagraphStyle("Datum", parent=body, alignment=2, spaceAfter=11)
    story.append(Paragraph(escape(record.get("date", case.get("date", ""))), right))
    story.append(Paragraph(escape(record["title"]), title))
    for block in paragraphs(record["text"]):
        story.append(Paragraph(escape(block).replace("\n", "<br/>"), heading if is_heading(block) else body))

    def page_style(canvas, document):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor("#62676B"))
        canvas.setFont("NotariatTNR", 8)
        canvas.drawString(65, A4[1] - 32, PROFILES.get(record.get("profile", "neutral"), PROFILES["neutral"]))
        canvas.drawRightString(A4[0] - 62, 28, f"{record['n']:02d} · {footer_label(record)}  |  Seite {document.page}")
        canvas.restoreState()

    document = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=65, rightMargin=62,
                                 topMargin=60, bottomMargin=56, title=record["title"],
                                 author=record.get("author", ""), subject=case["title"],
                                 invariant=1)
    document.build(story, onFirstPage=page_style, onLaterPages=page_style)


def mail_date(value: str) -> datetime:
    for pattern in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, pattern).replace(hour=10, tzinfo=timezone.utc)
        except ValueError:
            pass
    parsed = datetime.fromisoformat(value)
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed


def create_email(path: Path, record: dict, case: dict) -> None:
    message = EmailMessage(policy=SMTP)
    message["Subject"] = record["title"]
    sender = record.get("from_email", record.get("author", "Aktenpost"))
    recipient = record.get("to_email", record.get("to", "Vollzug"))
    message["From"] = sender if "@" in sender else f"{sender.split('|')[0].strip()} <postfach@absender.example>"
    message["To"] = recipient if "@" in recipient else f"{recipient.split('|')[0].strip()} <vollzug@notariat.example>"
    message["Date"] = format_datetime(mail_date(record["date"]))
    seed = hashlib.sha256((case["slug"] + path.name).encode()).hexdigest()[:20]
    message["Message-ID"] = f"<{seed}@postfach.example>"
    message.set_content(record["text"].strip() + "\n", charset="utf-8")
    path.write_bytes(message.as_bytes())


def create_xlsx(path: Path, record: dict, case: dict) -> None:
    book = Workbook()
    book.remove(book.active)
    sheets = record.get("sheets") or [record]
    thin = Side(style="thin", color="D9D9D9")
    for source in sheets:
        sheet = book.create_sheet(source.get("name", "Beteiligung und Vollzug")[:31])
        columns = source.get("columns", [])
        rows = source.get("rows", [])
        count = len(columns) or max((len(row) for row in rows), default=1)
        sheet.append([record["title"]])
        sheet.merge_cells(start_row=1, start_column=1, end_row=1, end_column=count)
        sheet.row_dimensions[1].height = 32
        sheet.cell(1, 1).font = Font(name="Calibri", size=15, bold=True)
        sheet.append([f"Stand {record['date']} | {record['author']}"])
        sheet.merge_cells(start_row=2, start_column=1, end_row=2, end_column=count)
        sheet.row_dimensions[2].height = 30
        sheet.cell(2, 1).font = Font(name="Calibri", size=10, color="62676B")
        sheet.cell(2, 1).alignment = Alignment(wrap_text=True, vertical="center")
        sheet.append([])
        sheet.append(columns)
        for row in rows:
            sheet.append(row)
        for row in sheet.iter_rows(min_row=4, max_row=sheet.max_row, max_col=count):
            for cell in row:
                cell.font = Font(name="Calibri", size=10, bold=cell.row == 4, color="FFFFFF" if cell.row == 4 else "202326")
                cell.fill = PatternFill("solid", fgColor="254958" if cell.row == 4 else ("EFF3F4" if cell.row % 2 == 0 else "FFFFFF"))
                cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
                cell.alignment = Alignment(vertical="center", wrap_text=True)
            sheet.row_dimensions[row[0].row].height = max(32, min(96, 16 * max((len(str(c.value or "")) // 24 + 1 for c in row), default=1)))
        for index in range(1, count + 1):
            letter = sheet.cell(4, index).column_letter
            label = str(columns[index - 1] if index <= len(columns) else "").lower()
            if "gesellschafter" in label or "unternehmen" in label:
                column_width = 43
            elif any(token in label for token in ("anteile", "anzahl", "betrag", "kaufpreis", "beteiligung")):
                column_width = 15
            elif label == "stand":
                column_width = 12
            else:
                column_width = 48 if count < 3 else (35 if count < 5 else 24)
            sheet.column_dimensions[letter].width = column_width
            for cells in sheet.iter_cols(min_col=index, max_col=index, min_row=5, max_row=sheet.max_row):
                for cell in cells:
                    if isinstance(cell.value, (int, float)):
                        cell.number_format = '#,##0.00' if "eur" in label else ('0.00" %"' if "%" in label else '#,##0')
        sheet.freeze_panes = "A5"
        sheet.auto_filter.ref = f"A4:{sheet.cell(sheet.max_row, count).coordinate}"
        sheet.sheet_properties.pageSetUpPr.fitToPage = True
        sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
        sheet.page_setup.orientation = "landscape" if count > 3 else "portrait"
        sheet.page_setup.fitToWidth, sheet.page_setup.fitToHeight = 1, 0
        sheet.print_title_rows = "1:4"
        sheet.print_options.horizontalCentered = True
        sheet.oddFooter.right.text = "Seite &P / &N"
        sheet.print_area = f"A1:{sheet.cell(sheet.max_row, count).coordinate}"
        if record.get("text"):
            sheet.cell(sheet.max_row + 2, 1, record["text"])
            r = sheet.max_row
            sheet.merge_cells(start_row=r, start_column=1, end_row=r, end_column=count)
            sheet.cell(r, 1).alignment = Alignment(wrap_text=True, vertical="center")
            sheet.cell(r, 1).font = Font(name="Calibri", size=10)
            sheet.row_dimensions[r].height = min(120, max(40, len(record["text"]) // 4))
            sheet.print_area = f"A1:{sheet.cell(r, count).coordinate}"
    book.properties.creator = record["author"]
    book.properties.title = record["title"]
    book.properties.created = book.properties.modified = STAMP
    book.save(path)
    stable_ooxml(path)


def create_screen(path: Path, record: dict, case: dict) -> None:
    width = 1500
    small, normal, bold = screen_font(21), screen_font(26), screen_font(30, bold=True)
    measurement = ImageDraw.Draw(Image.new("RGB", (1, 1)))

    def fit_lines(value, font, limit=1396):
        result = []
        current = ""
        for word in value.split():
            candidate = f"{current} {word}".strip()
            if measurement.textlength(candidate, font=font) <= limit:
                current = candidate
                continue
            if current:
                result.append(current)
            # Lange technische Kennungen umbrechen, statt sie am Bildrand zu
            # verlieren. Die Zeichenfolge bleibt in Leserichtung vollständig.
            current = ""
            for character in word:
                if measurement.textlength(current + character, font=font) > limit:
                    result.append(current)
                    current = ""
                current += character
        return result + ([current] if current else [])

    lines = []
    for block in record["text"].splitlines():
        lines.extend(fit_lines(block, normal) or [""])
    title_lines = fit_lines(record["title"], bold)
    height = max(900, 300 + 39 * (len(lines) + len(title_lines)))
    image = Image.new("RGB", (width, height), "#F3F5F7")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, 72), fill="#273743")
    draw.text((36, 22), "AKTENABLAGE  /  GESICHERTE BILDSCHIRMANSICHT", font=small, fill="white")
    draw.rectangle((32, 99, width - 32, 151), fill="white", outline="#D7DDE2", width=1)
    draw.text((51, 113), record.get("screen_url", "Ablageexport · " + record["author"]), font=small, fill="#4D5963")
    y = 183
    for line in title_lines:
        draw.text((52, y), line, font=bold, fill="#1F303A")
        y += 39
    draw.text((52, y + 6), f"Gesichert am {record['date']} · {case.get('office', '')}", font=small, fill="#667078")
    y += 58
    for line in lines:
        draw.text((52, y), line, font=normal, fill="#202D36")
        y += 39
    image.save(path, optimize=True)


def case_readme(case: dict, paths: list[Path], release: str) -> str:
    slug = case["slug"]
    documents = "\n".join(f"- [{path.name}]({path.name})" for path in paths)
    return f"""# {case['title']}

{case.get('subtitle', '')}

Die Akte richtet sich an Notariatsmitarbeiter, Notare und gesellschaftsrechtlich beratende Rechtsanwälte. Die Unterlagen bilden einen offenen Vollzugsvorgang ab. {case.get('task', '')}

## 1. Bearbeitungsstand und Auftrag

Bearbeitungsstand: {case.get('date', '6. November 2026')}. Zuordnung: [Notariat Alltag](../../notariat-alltag/README.md). Die Berliner Zielgesellschaft besteht bereits. Eine nach Anteilskauf eingereichte Gesellschafterliste, die Wirksamkeit der Anteilsübertragung und ein etwaiger gesonderter Geschäftsführerwechsel sind auseinanderzuhalten. Die bereits eingereichte anwaltliche Eingabe gehört zur Vorgeschichte. Eine abschließende Bewertung und die jetzt zu entwerfende ergänzende Stellungnahme sind nicht vorgegeben.

## 2. Aktenstücke

{documents}

## 3. Formate und Herkunft

{len(paths)} getrennte Unterlagen in nativen Büro-, Nachrichten-, Bild- und PDF-Formaten bilden den Arbeitsordner. Brieftexte sind in Times New Roman 11 pt gesetzt; Bildschirmansichten und Tabellen folgen dem jeweiligen Darstellungsformat. Die Bildschirmansichten sind für den fiktiven Sachverhalt rekonstruierte Ansichten, keine Abrufe realer Registerdaten. Personen, Gesellschaften, Aktenzeichen, Kennungen und Transaktionen sind erfunden. Die fiktiven Daten ersetzen keinen aktuellen amtlichen Länder- oder Registerabruf.

<!-- reserved-example-contacts -->
Kontaktadressen mit der reservierten Endung `.example` sind Bestandteil des erfundenen Sachverhalts und nicht für den Versand bestimmt. Die deutschen und ausländischen Unterlagen sind Arbeitsmaterial und keine echten amtlichen Dokumente.

<!-- BEGIN gesamt-pdf-section (autogen) -->
## 4. Akte herunterladen

Das Akten-ZIP enthält die Originaldateien ohne vorgeschalteten Ordner und ohne Markdown. Das Einzel-PDF-ZIP enthält jede Unterlage als PDF. Beide Archive enthalten auf der Wurzelebene die vorgeschriebene `README.txt`; das Gesamt-PDF dient als gemeinsame Lesefassung.

{NOTICE_MARKDOWN}

| Fassung | Download |
| --- | --- |
| Gesamt-PDF | [Akte am Stück](gesamt-pdf/{slug}_gesamt.pdf) |
| Akten-ZIP | [Originaldateien](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{release}/testakte-{slug}.zip) |
| Einzel-PDF-ZIP | [Alle Unterlagen als PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{release}/testakte-{slug}-einzelpdfs.zip) |
<!-- END gesamt-pdf-section (autogen) -->
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--material", type=Path, default=ROOT / "scripts/notariat-auslandsinvestoren-material.json")
    parser.add_argument("--release", default="notariat-v445.35.7")
    parser.add_argument("--case", choices=sorted(SLUGS), help="Nur die ausgewählte Akte erzeugen.")
    args = parser.parse_args()
    material = json.loads(args.material.read_text(encoding="utf-8"))
    present = {case["slug"] for case in material["cases"]}
    if (not args.case and present != SLUGS) or not present <= SLUGS or (args.case and args.case not in present):
        raise ValueError("Material muss genau die beiden vorgesehenen Akten enthalten.")
    init_pdf_fonts()
    creators = {"docx": create_docx, "pdf": create_pdf, "eml": create_email, "xlsx": create_xlsx, "png": create_screen}
    for case in material["cases"]:
        if args.case and case["slug"] != args.case:
            continue
        target = ROOT / "testakten" / case["slug"]
        target.mkdir(parents=True, exist_ok=True)
        docs = case["docs"]
        if sorted(record["n"] for record in docs) != list(range(1, len(docs) + 1)):
            raise ValueError("Aktenstücknummern müssen eindeutig und lückenlos sein.")
        paths = []
        for record in docs:
            kind, stem = record["kind"], record["stem"]
            if kind not in creators or not re.fullmatch(r"[A-Za-z0-9_-]+", stem):
                raise ValueError(f"Unzulässiger Dateiname oder Typ: {stem}.{kind}")
            path = target / f"{record['n']:02d}_{stem}.{kind}"
            creators[kind](path, record, case)
            paths.append(path)
        (target / "README.md").write_text(case_readme(case, paths, args.release), encoding="utf-8")
        print(f"{case['slug']}: {len(paths)} native Aktenstücke")


if __name__ == "__main__":
    main()
