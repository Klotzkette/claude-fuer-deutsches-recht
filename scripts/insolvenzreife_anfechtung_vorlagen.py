#!/usr/bin/env python3
"""Reproduzierbare Word-Vorlagen aus den gepflegten Markdown-Quellen."""

from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / 'zahlungsunfaehigkeits-und-ueberschuldungspruefer' / 'vorlagen'
TEMPLATE_FILES = ('01_Anfechtungsschreiben.docx', '02_Anfechtungsklage.docx')
FONT = 'Times New Roman'


def _font(run, size=11, bold=False, color='000000'):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), FONT)


def _runs(paragraph, text):
    """Subtle bold placeholders, keeping complete nested bracket text intact."""
    for i, chunk in enumerate(re.split(r'(\[[^\[\]\n]{1,100}\])', text)):
        r = paragraph.add_run(chunk)
        _font(r, bold=(i % 2 == 1))


def _cell(cell, text, header=False):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    tcpr = cell._tc.get_or_add_tcPr()
    margins = OxmlElement('w:tcMar')
    for side in ('top', 'left', 'bottom', 'right'):
        el = OxmlElement('w:' + side)
        el.set(qn('w:w'), '90')
        el.set(qn('w:type'), 'dxa')
        margins.append(el)
    tcpr.append(margins)
    if header:
        shade = OxmlElement('w:shd')
        shade.set(qn('w:fill'), 'DCE5EB')
        tcpr.append(shade)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    _runs(p, text)
    if header:
        for r in p.runs:
            r.bold = True


def _table(doc, rows):
    rows = [r for r in rows if not all(re.fullmatch(r':?-+:?', c.strip()) for c in r)]
    table = doc.add_table(rows=0, cols=len(rows[0]))
    table.autofit = False
    # Column widths distinguish transaction descriptions from dates and amounts.
    widths = {3: [2.0, 6.0, 8.0], 4: [1.9, 7.4, 3.7, 3.0], 5: [1.9, 5.8, 3.3, 2.5, 2.5]}[len(rows[0])]
    for col, width in zip(table.columns, widths):
        col.width = Cm(width)
    borders = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement('w:' + side)
        for k, v in [('val', 'single'), ('sz', '4'), ('color', 'D9D9D9')]:
            el.set(qn('w:' + k), v)
        borders.append(el)
    table._tbl.tblPr.append(borders)
    for n, values in enumerate(rows):
        row = table.add_row()
        pr = row._tr.get_or_add_trPr()
        if n == 0:
            repeat = OxmlElement('w:tblHeader')
            pr.append(repeat)
        no_split = OxmlElement('w:cantSplit')
        pr.append(no_split)
        for cell, val, width in zip(row.cells, values, widths):
            cell.width = Cm(width)
            _cell(cell, val, n == 0)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def _docx(source: Path, output: Path):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Cm(21)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.2)
    sec.bottom_margin = Cm(2.0)
    sec.left_margin = Cm(2.5)
    sec.right_margin = Cm(2.5)
    sec.header_distance = Cm(1.0)
    sec.footer_distance = Cm(1.0)
    normal = doc.styles['Normal']
    normal.font.name = FONT
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.line_spacing = 1.08
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.widow_control = True
    for name, size in [('Title', 17), ('Heading 1', 13), ('Heading 2', 11.5), ('Heading 3', 11)]:
        st = doc.styles[name]
        st.font.name = FONT
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.paragraph_format.space_before = Pt(12 if name != 'Title' else 0)
        st.paragraph_format.space_after = Pt(8)
        st.paragraph_format.keep_with_next = True
        st.paragraph_format.keep_together = True
    header = sec.header.paragraphs[0]
    _font(header.add_run('[Kanzleiname]  ·  Insolvenzverwaltung'), 9)
    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _font(footer.add_run('[Kanzlei-Aktenzeichen]  |  Seite '), 9)
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    footer._p.append(field)
    paragraphs = re.split(r'\n\s*\n', source.read_text(encoding='utf-8').strip())
    for block in paragraphs:
        if block.startswith('|'):
            rows = [[c.strip() for c in line.strip().strip('|').split('|')] for line in block.splitlines()]
            _table(doc, rows)
        elif block.startswith('# '):
            p = doc.add_paragraph(style='Title')
            r = p.add_run(block[2:])
            _font(r, 17, True)
        elif block.startswith('## '):
            p = doc.add_paragraph(style='Heading 1')
            _font(p.add_run(block[3:]), 13, True)
        elif block.startswith('### '):
            p = doc.add_paragraph(style='Heading 2')
            _font(p.add_run(block[4:]), 11.5, True)
        else:
            p = doc.add_paragraph()
            _runs(p, block)
            if block.startswith('[Baustein') or block.startswith('[Nur den zutreffenden'):
                p.paragraph_format.keep_with_next = True
                for r in p.runs:
                    r.italic = True
    props = doc.core_properties
    props.title = paragraphs[0].removeprefix('# ')
    props.subject = 'Ausfüllbare Vorlage für die Arbeit mit Insolvenzunterlagen'
    props.author = 'Klotzkette'
    props.last_modified_by = 'Klotzkette'
    props.created = props.modified = datetime(2026, 11, 13, tzinfo=timezone.utc)
    props.revision = 1
    # Some bundled base templates have a title border. It is not letter stationery.
    for root in (doc.element, doc.styles.element):
        for border in root.xpath('.//w:pBdr'):
            border.getparent().remove(border)
    for p in doc.paragraphs:
        if p.text == 'Mit freundlichen Grüßen':
            p.paragraph_format.keep_with_next = True
    if len(doc.paragraphs) >= 2:
        doc.paragraphs[-2].paragraph_format.keep_with_next = True
    doc.save(output)
    # Stable ZIP timestamps permit content-addressed identical case copies.
    with ZipFile(output) as z:
        data = {name: z.read(name) for name in z.namelist()}
    with ZipFile(output, 'w', ZIP_DEFLATED, compresslevel=9) as z:
        for name in sorted(data):
            info = ZipInfo(name, (2026, 11, 13, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data[name])


def build_templates(output_dir: Path = SOURCE_DIR) -> list[Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    files = []
    for name in TEMPLATE_FILES:
        source = SOURCE_DIR / Path(name).with_suffix('.md')
        target = output_dir / name
        if output_dir.resolve() != SOURCE_DIR.resolve():
            shutil.copy2(source, output_dir / source.name)
        _docx(source, target)
        files.append(target)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=SOURCE_DIR)
    args = parser.parse_args()
    for path in build_templates(args.output):
        print(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)


if __name__ == '__main__':
    main()
