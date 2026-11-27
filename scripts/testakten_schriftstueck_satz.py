"""Bearbeitbare Aktenpost und dazugehörige A4-Lesefassung aus demselben Inhalt."""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timezone
from functools import lru_cache
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, CondPageBreak, Frame, HRFlowable, LongTable, PageTemplate,
    Paragraph, Spacer, TableStyle,
)

from testakte_bildzeichen import bildzeichen
from testakte_briefkopf import PALETTE, classify

KINDS = {"brief": "Schreiben", "vermerk": "Aktenvermerk", "protokoll": "Protokoll"}
INK, MUTED, PALE = "202B31", "46565E", "CFD9D9"
WIDTH = 163 * mm
XML_CONTROL = re.compile(r"[\x00-\x08\x0b\x0e-\x1f\ud800-\udfff\ufffe\uffff]")
BASE_CHARS = bytes(range(256)).decode("cp1252", errors="ignore")
EXTRA_CHARS = re.compile("([^" + re.escape(BASE_CHARS) + "]+)")
# Name, Word-Schrift, PDF-Schrift, Größe, Zeilenhöhe, Abstand davor/danach, Folgeabsatz binden.
STYLES = [
    ("Absender", "Arial", "Helvetica-Bold", 17, 20, 0, 1, True),
    ("Einheit", "Arial", "Helvetica", 9, 12, 0, 3, True),
    ("Gattung", "Arial", "Helvetica-Bold", 8, 11, 3, 2, True),
    ("Aktenbezug", "Arial", "Helvetica", 9, 12, 0, 6, True),
    ("Betreff", "Times New Roman", "Times-Bold", 19, 22, 0, 10, True),
    ("Text", "Times New Roman", "Times-Roman", 11, 15, 0, 6, False),
    ("Abschnitt", "Arial", "Helvetica-Bold", 11, 14, 9, 6, True),
    ("Beleg", "Times New Roman", "Times-Bold", 11, 14, 5, 1, True),
    ("Fundstelle", "Arial", "Helvetica", 8.5, 11.5, 0, 4, True),
    ("Feld", "Times New Roman", "Times-Roman", 11, 15, 4, 3, True),
    ("Klein", "Arial", "Helvetica", 8, 11, 0, 0, False),
    ("Spaltenkopf", "Arial", "Helvetica-Bold", 9, 12, 0, 0, False),
    ("Zelle", "Times New Roman", "Times-Roman", 10.5, 13.5, 0, 0, False),
]


def house_color(brief):
    identity = " ".join(filter(None, (brief.get("sender"), brief.get("unit"))))
    typ = classify(identity)
    if typ in {"gericht", "behoerde"}:
        return "38516A"
    if typ == "notariat":
        return "594267"
    if typ == "kanzlei":
        return "713744"
    digest = sha256(identity.casefold().encode()).digest()
    return PALETTE[digest[0] % len(PALETTE)][1]


def style_color(name, accent):
    if name in {"Absender", "Gattung", "Abschnitt", "Spaltenkopf"}:
        return accent
    return MUTED if name in {"Einheit", "Aktenbezug", "Fundstelle", "Klein"} else INK


def clean(text):
    if not isinstance(text, str):
        raise TypeError("Dokumenttext muss eine Zeichenkette sein")
    # PDF-Extrakte können Seitenumbrüche enthalten. Inhalt und Absatzgrenzen bleiben erhalten.
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\f", "\n")
    return unicodedata.normalize("NFC", XML_CONTROL.sub(" ", text)).strip()


def body_blocks(brief):
    """Gemeinsame Reihenfolge für den Word- und den PDF-Satz."""
    if brief.get("recipient"):
        yield "Text", clean(brief["recipient"])
    details = []
    for key, label in (("reference", "Bezug"), ("date", "Datum")):
        if brief.get(key):
            details.append(label + "  " + clean(brief[key]))
    if details:
        yield "Aktenbezug", "     ·     ".join(details)
    if brief.get("case") and brief["case"] != brief["title"]:
        yield "Aktenbezug", clean(brief["case"])
    yield "Betreff", clean(brief["title"])
    if brief.get("intro"):
        yield "Text", clean(brief["intro"])
    number = 0
    for section in brief.get("sections", []):
        if section.get("heading"):
            number += 1
            yield "Abschnitt", f"{number}. {clean(section['heading'])}"
        for value in section.get("paragraphs", []):
            yield "Text", clean(value)
        if section.get("table"):
            yield "Tabelle", section["table"]
    if brief.get("evidence"):
        number += 1
        yield "Abschnitt", f"{number}. Unterlagen und Fundstellen"
        for entry in brief["evidence"]:
            yield "Beleg", clean(entry["title"])
            if entry.get("source"):
                yield "Fundstelle", clean(entry["source"])
            if entry.get("text"):
                yield "Text", clean(entry["text"])
    if brief.get("fields"):
        yield "Abschnitt", f"{number + 1}. Zur Bearbeitung"
        for label in brief["fields"]:
            yield "Feld", clean(label)
            yield "Antwortzeile", ""
    for key in ("closing", "signature"):
        if brief.get(key):
            yield "Text", clean(brief[key])


def table_rows(table):
    header = table["headers"]
    rows = [header, *table["rows"]]
    if not header or any(len(row) != len(header) for row in rows):
        raise ValueError("Jede Tabellenzeile benötigt so viele Zellen wie die Kopfzeile")
    return [[clean(str(cell)) for cell in row] for row in rows]


def zip_bytes(parts):
    target = BytesIO()
    with ZipFile(target, "w", ZIP_DEFLATED) as archive:
        for name, data in sorted(parts.items()):
            info = ZipInfo(name, date_time=(2000, 1, 1, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=ZIP_DEFLATED)
    return target.getvalue()


@lru_cache(maxsize=1)
def blank_docx():
    """Schlanke OPC-Vorlage ohne Vorschaubilder, Themen und unbenutzte Word-Stile."""
    rel = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    pkg_rel = "http://schemas.openxmlformats.org/package/2006/relationships"
    w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    document_type = "application/vnd.openxmlformats-officedocument.wordprocessingml"
    return zip_bytes({
        "[Content_Types].xml": f'<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        f'<Override PartName="/word/document.xml" ContentType="{document_type}.document.main+xml"/>'
        f'<Override PartName="/word/styles.xml" ContentType="{document_type}.styles+xml"/></Types>',
        "_rels/.rels": f'<Relationships xmlns="{pkg_rel}"><Relationship Id="rId1" Type="{rel}/officeDocument" Target="word/document.xml"/></Relationships>',
        "word/_rels/document.xml.rels": f'<Relationships xmlns="{pkg_rel}"><Relationship Id="rId1" Type="{rel}/styles" Target="styles.xml"/></Relationships>',
        "word/document.xml": f'<w:document xmlns:w="{w}" xmlns:r="{rel}"><w:body><w:sectPr/></w:body></w:document>',
        "word/styles.xml": f'<w:styles xmlns:w="{w}"><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style></w:styles>',
    })


def elem(tag, **attrs):
    node = OxmlElement("w:" + tag)
    for key, value in attrs.items():
        node.set(qn("w:" + key), str(value))
    return node


def border(paragraph, color, *, top=False):
    props = paragraph._p.get_or_add_pPr()
    borders = elem("pBdr")
    borders.append(elem("top" if top else "bottom", val="single", sz=5, space=3, color=color))
    props.append(borders)


def short(text, length=80):
    text = " ".join(text.split())
    return text if len(text) <= length else text[:length - 1].rstrip() + "…"


def _docx(brief, blocks, accent, kind, sender):
    doc = Document(BytesIO(blank_docx()))
    for name, family, face, size, leading, before, after, bind in STYLES:
        style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        style.font.name, style.font.size = family, Pt(size)
        style.font.bold = face.endswith("Bold")
        style.font.italic = False
        style.font.color.rgb = RGBColor.from_string(style_color(name, accent))
        fmt = style.paragraph_format
        fmt.line_spacing = Pt(leading)
        fmt.space_before, fmt.space_after = Pt(before), Pt(after)
        fmt.keep_with_next, fmt.widow_control = bind, True
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.left_margin, sec.right_margin = Mm(25), Mm(22)
    sec.top_margin, sec.bottom_margin = Mm(22), Mm(23)
    sec.header_distance, sec.footer_distance = Mm(11), Mm(11)
    sec.different_first_page_header_footer = True
    running = sec.header.paragraphs[0]
    running.style = doc.styles["Klein"]
    running.add_run(short(sender) + "   ·   " + kind)
    border(running, PALE)
    doc.core_properties.title = short(clean(brief["title"]), 255)
    doc.core_properties.author = short(sender, 255)
    doc.core_properties.last_modified_by = short(sender, 255)
    doc.core_properties.modified = datetime(2000, 1, 1, tzinfo=timezone.utc)
    for footer in (sec.footer, sec.first_page_footer):
        p = footer.paragraphs[0]
        p.style = doc.styles["Klein"]
        p.paragraph_format.tab_stops.add_tab_stop(Mm(163), WD_TAB_ALIGNMENT.RIGHT)
        p.add_run(short(brief.get("reference") or brief.get("case") or kind, 52))
        p.add_run("\tSeite ")
        field = elem("fldSimple", instr="PAGE")
        r = elem("r")
        t = elem("t")
        t.text = "1"
        r.append(t)
        field.append(r)
        p._p.append(field)
        border(p, accent, top=True)
    p = doc.add_paragraph(sender, "Absender")
    if brief.get("unit") and brief["unit"] != sender:
        p = doc.add_paragraph(clean(brief["unit"]), "Einheit")
    border(p, accent)
    doc.add_paragraph(kind.upper(), "Gattung")
    for index, (name, value) in enumerate(blocks):
        if name == "Tabelle":
            rows = table_rows(value)
            tab = doc.add_table(rows=0, cols=len(rows[0]))
            tab.alignment = WD_TABLE_ALIGNMENT.CENTER
            tab.autofit = False
            for col in tab.columns:
                col.width = Mm(163 / len(tab.columns))
            for i, row in enumerate(rows):
                tr = tab.add_row()
                if i == 0:
                    tr._tr.get_or_add_trPr().append(elem("tblHeader", val="true"))
                for cell, text in zip(tr.cells, row):
                    cell.width = Mm(163 / len(row))
                    p = cell.paragraphs[0]
                    p.style = doc.styles["Spaltenkopf" if i == 0 else "Zelle"]
                    p.paragraph_format.space_before = p.paragraph_format.space_after = Pt(3)
                    p.add_run(text)
                    if i % 2 == 0:
                        color = "EAF0F1" if i == 0 else "F8FAFA"
                        cell._tc.get_or_add_tcPr().append(elem("shd", fill=color))
                    if i == 0:
                        borders = elem("tcBorders")
                        borders.append(elem("bottom", val="single", sz=6, color=accent))
                        cell._tc.get_or_add_tcPr().append(borders)
        elif name == "Antwortzeile":
            p = doc.add_paragraph("", "Text")
            p.paragraph_format.line_spacing = Pt(11)
            if len(brief.get("fields", [])) <= 3 and index + 1 < len(blocks) and blocks[index + 1][0] == "Feld":
                p.paragraph_format.keep_with_next = True
            border(p, PALE)
        else:
            doc.add_paragraph(value, name)
    buf = BytesIO()
    doc.save(buf)
    with ZipFile(buf) as original:
        return zip_bytes({n: original.read(n) for n in original.namelist()})


@lru_cache(maxsize=1)
def extra_fonts():
    """Die Grundschriften decken westeuropäischen Text ab. Sonderzeichen erhalten ein Unicode-Mapping."""
    paths = [Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
             Path("/Library/Fonts/Arial Unicode.ttf"), Path("C:/Windows/Fonts/arial.ttf"),
             Path("/usr/share/fonts/truetype/noto/NotoSansSymbols2-Regular.ttf")]
    fonts = [TTFont("Akten" + path.stem, str(path)) for path in paths if path.is_file()]
    fonts.append(TTFont("AktenVera", "Vera.ttf"))
    for font in fonts:
        pdfmetrics.registerFont(font)
    return fonts


def pdf_markup(text):
    spans = EXTRA_CHARS.split(text)
    for i, span in enumerate(spans):
        if i % 2 == 0:
            spans[i] = escape(span).replace("\n", "<br/>")
            continue
        parts = []
        for char in span:
            # ReportLab 4.4 bildet Supplementary Planes in TrueType-ToUnicode nicht auf UTF-16-Paare ab.
            if ord(char) > 0xFFFF:
                parts.append(bildzeichen(char))
                continue
            font = next((f for f in extra_fonts() if ord(char) in f.face.charToGlyph), None)
            if font is None:
                parts.append(bildzeichen(char))
            else:
                parts.append(f'<font name="{font.fontName}">{escape(char)}</font>')
        spans[i] = "".join(parts)
    return "".join(spans)


def _pdf(brief, blocks, accent, kind, sender):
    file = BytesIO()
    accent_color = HexColor("#" + accent)
    muted_color = HexColor("#" + MUTED)
    line_color = HexColor("#" + PALE)
    styles = {}
    for name, _, face, size, leading, before, after, bind in STYLES:
        styles[name] = ParagraphStyle(name, fontName=face, fontSize=size, leading=leading,
                                      spaceBefore=before, spaceAfter=after, keepWithNext=bind,
                                      textColor=HexColor("#" + style_color(name, accent)),
                                      splitLongWords=True, allowWidows=0, allowOrphans=0)
    def par(text, style):
        return Paragraph(pdf_markup(text), styles[style])

    def running_text(canvas, text, y):
        label = par(text, "Klein")
        label.wrap(WIDTH, 12)
        label.drawOn(canvas, 25 * mm, y)

    def furniture(c, document):
        c.saveState()
        if document.page > 1:
            running_text(c, short(sender, 45) + "   ·   " + kind, A4[1] - 13 * mm)
            c.setStrokeColor(line_color)
            c.line(25 * mm, A4[1] - 15 * mm, 188 * mm, A4[1] - 15 * mm)
        c.setStrokeColor(accent_color)
        c.line(25 * mm, 18 * mm, 188 * mm, 18 * mm)
        c.setFillColor(muted_color)
        c.setFont("Helvetica", 8)
        running_text(c, short(brief.get("reference") or brief.get("case") or kind, 52), 12 * mm)
        c.drawRightString(188 * mm, 12 * mm, f"Seite {document.page}")
        c.restoreState()

    pdf = BaseDocTemplate(file, pagesize=A4, title=brief["title"], author=sender, subject=kind,
                          invariant=1, pageCompression=1)
    frame = Frame(25 * mm, 23 * mm, WIDTH, A4[1] - 45 * mm, leftPadding=0, rightPadding=0,
                  bottomPadding=0, topPadding=0, id="Satzspiegel")
    pdf.addPageTemplates([PageTemplate(id="Akte", frames=[frame], onPage=furniture)])
    story = [par(sender, "Absender")]
    if brief.get("unit") and brief["unit"] != sender:
        story.append(par(clean(brief["unit"]), "Einheit"))
    story += [HRFlowable(width="100%", thickness=1.4, color=accent_color, spaceAfter=6),
              par(kind.upper(), "Gattung"), Spacer(1, 7)]
    for i, (name, value) in enumerate(blocks):
        if name == "Tabelle":
            rows = table_rows(value)
            tab = LongTable([[par(cell, "Spaltenkopf" if i == 0 else "Zelle") for cell in row]
                             for i, row in enumerate(rows)], colWidths=[WIDTH / len(rows[0])] * len(rows[0]),
                            hAlign="LEFT", repeatRows=1, splitInRow=1)
            tab.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#EAF0F1")),
                ("LINEBELOW", (0, 0), (-1, 0), .7, accent_color),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#FFFFFF"), HexColor("#F8FAFA")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story += [tab, Spacer(1, 7)]
        elif name == "Antwortzeile":
            line = HRFlowable(width="100%", thickness=.45, color=line_color, spaceBefore=10, spaceAfter=6)
            if len(brief.get("fields", [])) <= 3 and i + 1 < len(blocks) and blocks[i + 1][0] == "Feld":
                line.keepWithNext = True
            story.append(line)
        else:
            paragraph = par(value, name)
            if i + 1 < len(blocks) and blocks[i + 1][0] == "Tabelle":
                # Ein großer Tabellenkörper darf den Abschnittstitel nicht auf ein leeres Blatt ziehen.
                paragraph.keepWithNext = False
                story.append(CondPageBreak(28 * mm))
            story.append(paragraph)
    pdf.build(story)
    return file.getvalue()


def render_pair(brief: dict) -> tuple[bytes, bytes]:
    """Erzeugt DOCX und PDF. Titel und Inhalt sind Pflicht; Herkunft und Datierung bleiben quellengebunden."""
    title = clean(brief["title"])
    if not title:
        raise ValueError("Schriftstück benötigt einen Betreff")
    kind = KINDS[brief["kind"]]
    sender = clean(brief.get("sender") or kind)
    blocks = list(body_blocks(brief))
    if not any(name in {"Text", "Tabelle", "Beleg", "Feld"} and value for name, value in blocks):
        raise ValueError(f"Schriftstück ohne Inhalt: {title}")
    accent = house_color(brief)
    return _docx(brief, blocks, accent, kind, sender), _pdf(brief, blocks, accent, kind, sender)
