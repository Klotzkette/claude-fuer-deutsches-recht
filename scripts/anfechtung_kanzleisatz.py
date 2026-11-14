"""Kanzleisatz für ausdrücklich profilierte Originalschreiben der Anfechtungsakten."""
from __future__ import annotations

from datetime import datetime
import io
from pathlib import Path
import re
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


def document(path: Path, item: dict) -> None:
    profile = item['letterhead']
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(3.65), Cm(2.05)
    section.left_margin, section.right_margin = Cm(2.5), Cm(2.2)
    section.header_distance, section.footer_distance = Cm(1.15), Cm(1.0)
    for style in doc.styles:
        if style.type != 1:
            continue
        style.font.name, style.font.size = 'Times New Roman', Pt(11)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_after = Pt(7)
        style.paragraph_format.line_spacing = 1.06
        style.paragraph_format.widow_control = True
        fonts = style.element.get_or_add_rPr().get_or_add_rFonts()
        for key in list(fonts.attrib):
            if key.endswith('Theme'):
                del fonts.attrib[key]
        for key in ('ascii', 'hAnsi', 'eastAsia', 'cs'):
            fonts.set(qn('w:' + key), 'Times New Roman')
    for border in doc.styles.element.xpath('.//w:pBdr'):
        border.getparent().remove(border)
    doc.styles['Title'].font.size, doc.styles['Title'].font.bold = Pt(16), True
    for n, size in ((1, 13), (2, 12), (3, 11)):
        style = doc.styles[f'Heading {n}']
        style.font.size, style.font.bold = Pt(size), True
        style.paragraph_format.space_before, style.paragraph_format.space_after = Pt(11), Pt(7)
        style.paragraph_format.keep_with_next = True
    header = section.header.paragraphs[0]
    header.paragraph_format.space_after = Pt(4)
    run = header.add_run(profile['firm'])
    run.bold, run.font.size = True, Pt(19)
    line = section.header.add_paragraph(profile['subtitle'])
    line.paragraph_format.space_after = Pt(4)
    line.runs[0].font.size = Pt(10)
    contact = section.header.add_paragraph(profile['contact'])
    contact.paragraph_format.space_after = Pt(0)
    contact.runs[0].font.size = Pt(8)
    # Kanzleifarbe nur als dezenter Briefbogen-Akzent, nicht als Titelunterstreichung.
    run.font.color.rgb = RGBColor.from_string(profile.get('accent', '243E51'))
    sender = doc.add_paragraph(profile['return_address'])
    sender.paragraph_format.space_after = Pt(7)
    sender.runs[0].font.size = Pt(8)
    recipient = doc.add_paragraph(item['to'])
    recipient.paragraph_format.space_after = Pt(15)
    meta = doc.add_paragraph(f"{item['date']}  |  Unser Zeichen {profile['reference']}")
    meta.runs[0].font.size = Pt(9)
    if item.get('docket'):
        doc.add_paragraph('Gerichtliches Aktenzeichen: ' + item['docket'])
    doc.add_paragraph(item['title'], 'Title')
    for block in item['body'].split('\n\n'):
        match = re.fullmatch(r'(\d+(?:\.\d+)*) ([^\n]{1,110})', block)
        if match:
            level = min(3, match[1].count('.') + 1)
            doc.add_paragraph(block, f'Heading {level}')
        else:
            paragraph = doc.add_paragraph(block)
            if block.startswith('Beweis:'):
                paragraph.paragraph_format.left_indent = Cm(.35)
                paragraph.runs[0].italic = True
    footer = section.footer.paragraphs[0]
    footer.paragraph_format.space_after = Pt(0)
    footer.text = profile['reference'] + '  |  ' + profile['firm'] + '  |  Seite '
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    footer._p.append(field)
    for run in footer.runs:
        run.font.size = Pt(8)
    doc.core_properties.author = doc.core_properties.last_modified_by = profile['firm']
    doc.core_properties.title, doc.core_properties.language = item['title'], 'de-DE'
    doc.core_properties.created = doc.core_properties.modified = datetime.strptime(item['date'], '%d.%m.%Y')
    stream = io.BytesIO()
    doc.save(stream)
    with ZipFile(stream) as source, ZipFile(path, 'w', ZIP_DEFLATED) as target:
        for name in sorted(source.namelist()):
            info = ZipInfo(name, (2026, 11, 14, 8, 0, 0))
            info.compress_type = ZIP_DEFLATED
            target.writestr(info, source.read(name))
