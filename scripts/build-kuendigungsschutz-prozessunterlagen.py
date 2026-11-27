#!/usr/bin/env python3
"""Erstellt die separat zu öffnenden Betriebsrats- und Prozessunterlagen."""
import io
import json
from importlib import import_module
from datetime import datetime
from pathlib import Path
import tempfile
from zipfile import ZipFile

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor
from pypdf import PdfReader, PdfWriter

from testakte_disclaimer import NOTICE_BYTES
from testakte_office_pdf import render_office_batch

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'arbeitsrecht-kuendigungsschutzklagewerkstatt'
SOURCE = ROOT / 'scripts/data/kuendigungsschutz-prozessunterlagen.json'
FILENAMES = ('01_Anhoerung_Betriebsrat.docx', '02_Antwort_Betriebsrat.docx',
             '03_Klageschrift.docx', '04_Klageerwiderung.docx')


def word(path, document):
    stamp = datetime.fromisoformat(document['date'])
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(2.1), Cm(2)
    section.left_margin, section.right_margin = Cm(2.4), Cm(2.3)
    styles = doc.styles
    normal = styles['Normal']
    normal.font.name, normal.font.size = 'Times New Roman', Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.widow_control = True
    head = doc.add_paragraph()
    run = head.add_run(document['sender'])
    run.bold, run.font.size = True, Pt(11)
    doc.add_paragraph(document['recipient'])
    date = doc.add_paragraph(stamp.strftime('%d.%m.%Y'))
    date.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    title = doc.add_paragraph()
    title.paragraph_format.keep_with_next = True
    run = title.add_run(document['title'])
    run.bold, run.font.size = True, Pt(14)
    for para in document['paragraphs']:
        doc.add_paragraph(para)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    note = footer.add_run(document['title'])
    note.font.size, note.font.color.rgb = Pt(8), RGBColor.from_string('515963')
    properties = doc.core_properties
    properties.title, properties.author = document['title'], document['sender']
    properties.created, properties.modified = stamp, stamp
    doc.save(path)


def build():
    archive_writer = import_module('build-testakten-release-zips').write_bytes
    cases = json.loads(SOURCE.read_text(encoding='utf-8'))
    for slug, case in cases.items():
        with tempfile.TemporaryDirectory(prefix='ks-prozess-') as folder:
            temp = Path(folder)
            native = []
            titles = []
            for name, d in zip(FILENAMES, case['dokumente'], strict=True):
                path = temp / name
                if 'original' in d:
                    path.write_bytes((ROOT / 'testakten' / slug / d['original']).read_bytes())
                else:
                    word(path, d)
                native.append(path)
                titles.append(d.get('title') or name[3:-5].replace('_', ' '))
            rendered = render_office_batch(native)
            pdf = PdfWriter()
            for path, title in zip(native, titles, strict=True):
                start = len(pdf.pages)
                pdf.append(PdfReader(io.BytesIO(rendered[path])), import_outline=False)
                pdf.add_outline_item(title, start)
            buffer = io.BytesIO()
            pdf.write(buffer)
            target = PLUGIN / 'testakte/downloads' / f'testakte-{slug}-prozessunterlagen.zip'
            with ZipFile(target, 'w') as archive:
                archive_writer(archive, NOTICE_BYTES, 'README.txt')
                for path in native:
                    archive_writer(archive, path.read_bytes(), path.name)
                archive_writer(archive, buffer.getvalue(), 'Prozessunterlagen.pdf')
            print(f'{slug}: vier Originale, {len(pdf.pages)} PDF-Seiten', flush=True)


if __name__ == '__main__':
    build()
