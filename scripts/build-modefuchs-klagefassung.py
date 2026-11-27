#!/usr/bin/env python3
"""Build the editable pleading and check its text against the retained PDF."""

import difflib
import io
import re
from pathlib import Path

import pypdfium2
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import ImageOps
from pypdf import PdfReader
from reportlab.pdfgen.canvas import Canvas

from akteneingang.dokumente import office_bytes
from modefuchs_briefpapier import draw_brand


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "testakten/inkasso-zahlungsklage-modefuchs"
SOURCE = CASE / "originale/23_Klageschrift_InkassoZentrale_25-07-2025.pdf"
OUTPUT = CASE / "30_Klage_Arbeitsfassung_20250725.docx"
FONT = "Times New Roman"
INK = RGBColor.from_string("17394D")
MUTED = RGBColor.from_string("435965")

LETTERHEAD = (
    "InkassoZentrale GmbH",
    "Friedrich-Krause-Ufer 42 · 13353 Berlin · HRB 227771 B · AG Charlottenburg",
    "Geschäftsführer: Dr. Marvin Rüter, Constanze Lehnhardt",
    "Bank: Musterbank Nord AG · IBAN: DE55 2222 5555 0000 9988 12 · BIC: MNORDEHH",
    "Tel.: 030 88 71 22 990 · Fax: 030 88 71 22 991 · kontakt@inkassozentrale-gmbh.de",
)

REQUESTS = (
    "€ 698,00 nebst Zinsen in Höhe von 5 Prozentpunkten über dem jeweiligen Basiszinssatz seit dem 18.04.2025 zu zahlen,",
    "Mahngebühren in Höhe von € 5,50 zu zahlen,",
    "vorgerichtliche Inkassokosten in Höhe von € 83,54 nebst Zinsen in Höhe von 5 Prozentpunkten über dem jeweiligen Basiszinssatz seit Rechtshängigkeit zu zahlen,",
    "Verzugszinsen in Höhe von € 10,80 zu zahlen.",
)

SECTIONS = (
    ("Aktivlegitimation", (
        ("body", "Die Klägerin ist aufgrund Abtretungserklärung vom 08.06.2025 Inhaberin der streitgegenständlichen Forderung. Die ModeFuchs GmbH, Kaiserplatz 12, 10002 Musterstadt, hat die Forderung aus der Rechnung R-20250406-3098 samt sämtlicher Nebenforderungen an die Klägerin abgetreten."),
        ("evidence", "Beweis: Abtretungserklärung vom 08.06.2025 (Anlage K 1)"),
    )),
    ("Kaufvertrag und Lieferung", (
        ("body", "Der Beklagte bestellte am 03.04.2025 über den Online-Shop der ModeFuchs GmbH unter der Auftragsnummer MF-20250403-1749 folgende Waren:"),
        ("item", "– 1 Stück Cashmere-Mantel „Aurelia“, Größe 52, Preis: € 499,00"),
        ("item", "– 1 Stück Lederhandtasche „Noa“, Modell „Luca“, Preis: € 199,00"),
        ("body", "Der Gesamtkaufpreis beträgt € 698,00. Der Beklagte wählte die Zahlungsart „Kauf auf Rechnung“ mit einer Zahlungsfrist von 14 Tagen nach Rechnungszugang."),
        ("evidence", "Beweis: Bestellbestätigung vom 03.04.2025 (Anlage K 2)"),
        ("body", "Die Waren wurden am 06.04.2025 versandt und am 08.04.2025 an der Anschrift des Beklagten zugestellt. Die ordnungsgemäße Zustellung wurde vom Zustelldienst bestätigt."),
        ("evidence", "Beweis: Versandbestätigung vom 06.04.2025 (Anlage K 3), Zustellbestätigung vom 08.04.2025 (Anlage K 4)"),
    )),
    ("Rechnung und Fälligkeit", (
        ("body", "Die ModeFuchs GmbH stellte am 06.04.2025 die Rechnung R-20250406-3098 über € 698,00 aus. Die Rechnung wurde dem Beklagten zusammen mit der Versandbestätigung per E-Mail übermittelt. Das Fälligkeitsdatum wurde entsprechend der vereinbarten Zahlungsbedingungen auf den 17.04.2025 bestimmt."),
        ("evidence", "Beweis: Rechnung R-20250406-3098 vom 06.04.2025 (Anlage K 5)"),
    )),
    ("Verzug des Beklagten", (
        ("body", "Der Beklagte hat den Kaufpreis trotz Fälligkeit am 17.04.2025 nicht gezahlt. Der Verzug ist gemäß Paragraf 286 Abs. 2 Nr. 1 BGB automatisch eingetreten, da für die Leistung eine Zeit nach dem Kalender bestimmt war. Einer Mahnung bedurfte es daher nicht."),
        ("body", "Gleichwohl wurde der Beklagte mehrfach gemahnt:"),
        ("item", "– Erste Zahlungserinnerung per E-Mail am 20.04.2025"),
        ("item", "– Zweite Mahnung per E-Mail am 04.05.2025"),
        ("item", "– Erste Mahnung per Post am 05.05.2025"),
        ("item", "– Zweite Mahnung per Post am 22.05.2025 mit letzter Frist zum 02.06.2025"),
        ("evidence", "Beweis: Mahnschreiben (Anlagen K 6 bis K 9)"),
    )),
    ("Inkassotätigkeit", (
        ("body", "Nach fruchtlosem Ablauf sämtlicher Zahlungsfristen hat die ModeFuchs GmbH die Forderung am 08.06.2025 an die Klägerin abgetreten. Die Klägerin hat den Beklagten mit Schreiben vom 10.06.2025 und erneut mit Schreiben vom 25.06.2025 außergerichtlich zur Zahlung aufgefordert."),
        ("evidence", "Beweis: Inkassoschreiben vom 10.06.2025 (Anlage K 10), letzte Inkassoaufforderung vom 25.06.2025 (Anlage K 11)"),
    )),
    ("Anspruch auf Verzugszinsen", (
        ("body", "Der Beklagte schuldet gemäß Paragrafen 288 Abs. 1, 286 BGB Verzugszinsen in Höhe von 5 Prozentpunkten über dem jeweiligen Basiszinssatz seit dem 18.04.2025 (Tag nach Eintritt der Fälligkeit). Der Basiszinssatz beträgt zum maßgeblichen Zeitpunkt 3,37 %, sodass sich ein Verzugszinssatz von 8,37 % ergibt. Die bis zum Tag der Klageeinreichung aufgelaufenen Verzugszinsen betragen € 10,80."),
    )),
    ("Anspruch auf Erstattung der Inkassokosten", (
        ("body", "Die Klägerin macht zudem Inkassokosten als Verzugsschaden gemäß Paragrafen 280 Abs. 1, Abs. 2, 286 BGB geltend. Die Erstattungsfähigkeit von Inkassokosten bei berechtigter Forderung und Schuldnerverzug ist in der Rechtsprechung des Bundesgerichtshofs anerkannt (vgl. BGH, Urt. v. 22.10.2019 – VIII ZR 95/18)."),
        ("body", "Die Inkassokosten sind gemäß Paragraf 13e RVG auf die Höhe einer entsprechenden anwaltlichen Geschäftsgebühr gedeckelt. Die hier geltend gemachte 1,3-Geschäftsgebühr nach Nr. 2300 VV RVG bei einem Gegenstandswert von € 698,00 beläuft sich auf € 58,50 zuzüglich Auslagenpauschale (€ 11,70, Nr. 7002 VV RVG) und 19 % USt (€ 13,34), mithin insgesamt € 83,54."),
        ("evidence", "Beweis: Gebührenrechnung der Klägerin vom 10.06.2025 (Anlage K 12)"),
    )),
    ("Mahngebühren", (
        ("body", "Ferner macht die Klägerin Mahngebühren in Höhe von € 5,50 geltend. Diese wurden von der Ursprungsgläubigerin ModeFuchs GmbH im Rahmen der zweiten Mahnung (04.05.2025) berechnet und sind als Verzugsschaden gemäß Paragrafen 280, 286 BGB erstattungsfähig."),
    )),
    ("Zuständigkeit", (
        ("body", "Das Amtsgericht Nürnberg ist sachlich zuständig gemäß Paragrafen 23 Nr. 1, 71 Abs. 1 GVG, da der Streitwert € 5.000,00 nicht übersteigt. Die örtliche Zuständigkeit ergibt sich aus Paragraf 13 ZPO (allgemeiner Gerichtsstand des Beklagten am Wohnsitz Nürnberg)."),
    )),
)

ATTACHMENTS = (
    "Abtretungserklärung vom 08.06.2025",
    "Bestellbestätigung vom 03.04.2025",
    "Versandbestätigung vom 06.04.2025",
    "Zustellbestätigung vom 08.04.2025",
    "Rechnung R-20250406-3098 vom 06.04.2025",
    "Erste Zahlungserinnerung vom 20.04.2025",
    "Zweite Mahnung (E-Mail) vom 04.05.2025",
    "Erste Mahnung per Post vom 05.05.2025",
    "Zweite Mahnung per Post vom 22.05.2025",
    "Inkassoschreiben vom 10.06.2025",
    "Letzte Inkassoaufforderung vom 25.06.2025",
    "Gebührenrechnung der Klägerin vom 10.06.2025",
)


def configure_styles(doc):
    for border in doc.styles.element.xpath(".//w:pBdr"):
        border.getparent().remove(border)
    for style in doc.styles:
        if style.type not in (1, 2):
            continue
        style.font.name = FONT
        style.font.size = Pt(11)
        style.font.color.rgb = RGBColor(0, 0, 0)
        fonts = style.element.get_or_add_rPr().get_or_add_rFonts()
        for name in ("ascii", "hAnsi", "eastAsia", "cs"):
            fonts.set(qn(f"w:{name}"), FONT)
        for name in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
            fonts.attrib.pop(qn(f"w:{name}"), None)
    normal = doc.styles["Normal"].paragraph_format
    normal.line_spacing = 1.15
    normal.space_after = Pt(6)
    normal.widow_control = True
    for name in ("Title", "Heading 1", "Heading 2"):
        style = doc.styles[name]
        style.font.bold = True
        style.font.italic = False
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.keep_together = True
        style.paragraph_format.space_before = Pt(11)
        style.paragraph_format.space_after = Pt(11)
    for name, size in (("Title", 20), ("Heading 1", 14), ("Heading 2", 11.5)):
        doc.styles[name].font.size = Pt(size)
        doc.styles[name].font.color.rgb = INK
    language = OxmlElement("w:lang")
    language.set(qn("w:val"), "de-DE")
    doc.styles["Normal"].element.get_or_add_rPr().append(language)


def paragraph(doc, text, *, after=6, before=0, keep=False, align=None):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.keep_with_next = keep
    p.paragraph_format.keep_together = True
    if align is not None:
        p.alignment = align
    return p


def heading(doc, text, level, *, new_page=False):
    p = doc.add_paragraph(text, style=f"Heading {level}")
    p.paragraph_format.page_break_before = new_page
    return p


def logo_png():
    pdf = io.BytesIO()
    canvas = Canvas(pdf, pagesize=(248, 48), invariant=1)
    draw_brand(canvas, "inkasso", 4, 3)
    canvas.save()
    with pypdfium2.PdfDocument(pdf.getvalue()) as source:
        page = source[0]
        image = page.render(scale=4).to_pil().convert("RGB")
    bounds = ImageOps.invert(image.convert("L")).getbbox()
    if not bounds:
        raise ValueError("Inkasso-Wortbildmarke ist leer")
    output = io.BytesIO()
    image.crop(bounds).save(output, format="PNG")
    output.seek(0)
    return output


def stationery_text(p, text="", *, size=8, bold=False):
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.1
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.font.color.rgb = MUTED
    run.bold = bold
    return run


def page_number_field(p, instruction):
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), instruction)
    run = stationery_text(p)
    field.append(run._r)
    p._p.append(field)


def rule(p, side):
    edges = OxmlElement("w:pBdr")
    edge = OxmlElement(f"w:{side}")
    for key, value in (("val", "single"), ("sz", "5"), ("color", "397F80"), ("space", "5")):
        edge.set(qn(f"w:{key}"), value)
    edges.append(edge)
    p._p.get_or_add_pPr().append(edges)


def add_letterhead(section):
    section.different_first_page_header_footer = True
    first = section.first_page_header.paragraphs[0]
    first.style = "Normal"
    first.paragraph_format.space_after = Pt(0)
    shape = first.add_run().add_picture(logo_png(), width=Cm(6.8))
    shape._inline.docPr.set("descr", LETTERHEAD[0])
    rule(first, "bottom")
    address = section.first_page_header.add_paragraph()
    stationery_text(address, LETTERHEAD[1])
    address.paragraph_format.space_before = Pt(6)

    width = section.page_width - section.left_margin - section.right_margin
    follow = section.header.paragraphs[0]
    follow.style = "Normal"
    follow.paragraph_format.tab_stops.add_tab_stop(width, WD_TAB_ALIGNMENT.RIGHT)
    stationery_text(follow, LETTERHEAD[0], size=9, bold=True)
    stationery_text(follow, "\tIZ-MF-2025-1749")
    rule(follow, "bottom")

    legal = section.first_page_footer
    line = legal.paragraphs[0]
    line.style = "Normal"
    rule(line, "top")
    line.paragraph_format.tab_stops.add_tab_stop(width, WD_TAB_ALIGNMENT.RIGHT)
    stationery_text(line, LETTERHEAD[2], size=7.5)
    stationery_text(line, "\t")
    for text in LETTERHEAD[3:]:
        stationery_text(legal.add_paragraph(), text, size=7.5)
    for p in (line, section.footer.paragraphs[0]):
        if p is not line:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        stationery_text(p, "Seite ")
        page_number_field(p, "PAGE")
        stationery_text(p, " von ")
        page_number_field(p, "NUMPAGES")


def add_attachments(doc):
    table = doc.add_table(rows=0, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Cm(2.7)
    table.columns[1].width = Cm(13.5)
    borders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        border = OxmlElement(f"w:{side}")
        for key, value in (("val", "single"), ("sz", "4"), ("color", "D9D9D9")):
            border.set(qn(f"w:{key}"), value)
        borders.append(border)
    table._tbl.tblPr.append(borders)
    for number, description in enumerate(ATTACHMENTS, 1):
        row = table.add_row()
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        for cell, text, width in zip(
            row.cells, (f"Anlage K {number}", description), (2.7, 13.5)
        ):
            cell.width = Cm(width)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            margins = OxmlElement("w:tcMar")
            for side, value in (("top", "85"), ("bottom", "85"), ("left", "100"), ("right", "100")):
                margin = OxmlElement(f"w:{side}")
                margin.set(qn("w:w"), value)
                margin.set(qn("w:type"), "dxa")
                margins.append(margin)
            cell._tc.get_or_add_tcPr().append(margins)
            if text.startswith("Anlage K "):
                shade = OxmlElement("w:shd")
                shade.set(qn("w:fill"), "E4EEF0")
                cell._tc.get_or_add_tcPr().append(shade)
            p = cell.paragraphs[0]
            run = p.add_run(text)
            if text.startswith("Anlage K "):
                run.bold = True
                run.font.color.rgb = INK
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.keep_together = True
            p.paragraph_format.keep_with_next = number < len(ATTACHMENTS)
    return table


def normalized(text):
    return " ".join(text.replace("§§", "Paragrafen").replace("§", "Paragraf").split())


def verify_content(doc):
    # Only heading/list numbering and spelled-out legal symbols may differ.
    pages = PdfReader(SOURCE).pages
    body = []
    printed = []
    for number, page in enumerate(pages, 1):
        lines = [line.strip() for line in page.extract_text().splitlines()]
        printed.extend(lines)
        if number > 1 and lines[0] == LETTERHEAD[0]:
            lines.pop(0)
        footer = {*LETTERHEAD[1:], f"Seite {number} von {len(pages)}"}
        body.extend(line for line in lines if line not in footer)
    body_start = "Unser Zeichen: IZ-MF-2025-1749"
    if any(line not in printed for line in LETTERHEAD) or body_start not in body:
        raise ValueError("Briefkopf oder Aktenzeichen in der PDF-Klage unvollständig")
    text = "\n".join(body[body.index(body_start):])
    section = doc.sections[0]
    names = section.first_page_header._element.xpath(".//wp:docPr/@descr")
    address = section.first_page_header.paragraphs[1].text
    details = [p.text.split("\t")[0] for p in section.first_page_footer.paragraphs]
    if [*names, address, *details] != list(LETTERHEAD):
        raise ValueError("Geschäftsangaben im Word-Briefpapier unvollständig")
    for old, new in (("I. Anträge", "1 Anträge"), ("II. Sachverhalt", "2 Sachverhalt"), ("III. Anlagenverzeichnis", "3 Anlagenverzeichnis")):
        text = text.replace(old, new)
    for number, (title, _) in enumerate(SECTIONS, 1):
        text = text.replace(f"{number}. {title}", f"2.{number} {title}")
    for number in range(1, len(REQUESTS) + 1):
        text = re.sub(rf"(?m)^{number}\. ", f"1.{number} ", text)
    actual = []
    for block in doc.iter_inner_content():
        if hasattr(block, "rows"):
            actual.extend(cell.text for row in block.rows for cell in row.cells)
        else:
            actual.append(block.text)
    actual_text = "\n".join(actual)
    if "§" in actual_text:
        raise ValueError("Legal symbols must be spelled out")
    expected, actual = normalized(text), normalized(actual_text)
    if expected != actual:
        diff = "\n".join(difflib.unified_diff(expected.split(), actual.split(), fromfile="source", tofile="docx", lineterm=""))
        raise ValueError(f"Content differs from the original PDF:\n{diff}")


def build():
    doc = Document()
    configure_styles(doc)
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(3.25), Cm(2.5)
    section.left_margin, section.right_margin = Cm(2.4), Cm(2.4)
    section.header_distance, section.footer_distance = Cm(1.05), Cm(0.85)
    add_letterhead(section)
    props = doc.core_properties
    props.title = "Klage InkassoZentrale GmbH gegen Gottlieb von Altenhausen"
    props.subject = "Kaufpreisforderung nebst Nebenforderungen"
    props.author = ""
    props.last_modified_by = ""
    props.comments = ""

    p = paragraph(doc, "Unser Zeichen: IZ-MF-2025-1749", after=1, keep=True, align=WD_ALIGN_PARAGRAPH.RIGHT)
    p.runs[0].font.color.rgb = MUTED
    paragraph(doc, "Berlin, den 25.07.2025", after=10, keep=True, align=WD_ALIGN_PARAGRAPH.RIGHT)
    paragraph(doc, "An das\nAmtsgericht Nürnberg\nFlaschenhofstraße 35\n90402 Nürnberg", after=0, keep=True)
    title = doc.add_paragraph("Klage", style="Title")
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph(doc, "der InkassoZentrale GmbH, vertreten durch die Geschäftsführer Dr. Marvin Rüter und Constanze Lehnhardt,\nFriedrich-Krause-Ufer 42, 13353 Berlin,", keep=True)
    paragraph(doc, "– Klägerin –", align=WD_ALIGN_PARAGRAPH.RIGHT, keep=True)
    paragraph(doc, "gegen", align=WD_ALIGN_PARAGRAPH.CENTER, keep=True)
    paragraph(doc, "Herrn Gottlieb von Altenhausen,\nKaiserstraße 47, 90403 Nürnberg,", keep=True)
    paragraph(doc, "– Beklagter –", align=WD_ALIGN_PARAGRAPH.RIGHT, keep=True)
    paragraph(doc, "wegen: Kaufpreisforderung nebst Nebenforderungen\nStreitwert: € 797,84", keep=True)
    heading(doc, "1 Anträge", 1)
    paragraph(doc, "Die Klägerin beantragt,", after=0, keep=True)
    paragraph(doc, "den Beklagten zu verurteilen, an die Klägerin", keep=True)
    for number, text in enumerate(REQUESTS, 1):
        p = paragraph(doc, f"1.{number}\t{text}")
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.first_line_indent = Cm(-0.8)
        p.paragraph_format.tab_stops.add_tab_stop(Cm(0.8))

    heading(doc, "2 Sachverhalt", 1, new_page=True)
    for number, (title, blocks) in enumerate(SECTIONS, 1):
        heading(doc, f"2.{number} {title}", 2, new_page=number == 5)
        for index, (kind, text) in enumerate(blocks):
            next_kind = blocks[index + 1][0] if index + 1 < len(blocks) else None
            p = paragraph(doc, text, keep=next_kind in ("evidence", "item"))
            if kind == "item":
                p.paragraph_format.left_indent = Cm(0.3)
                p.paragraph_format.first_line_indent = Cm(-0.3)
                p.paragraph_format.space_after = Pt(2)
            elif kind == "evidence":
                p.clear()
                p.add_run("Beweis: ").bold = True
                p.add_run(text.removeprefix("Beweis: "))

    heading(doc, "3 Anlagenverzeichnis", 1, new_page=True)
    add_attachments(doc)
    paragraph(doc, "InkassoZentrale GmbH", before=18)
    verify_content(doc)
    OUTPUT.write_bytes(office_bytes(doc))
    verify_content(Document(OUTPUT))
    print(OUTPUT)
    print("Inhalt vollständig gegen das Original geprüft.")


if __name__ == "__main__":
    build()
