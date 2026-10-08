#!/usr/bin/env python3
"""Drei Gesellschaftsrechtsakten: Kernbestand vor dem Nachtrag, klare Registerpfade."""
import argparse
import importlib.util
import io
from pathlib import Path
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

from akten_build_runtime import serif_font_path
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import OFFICE_EXTS, render_office_batch

TITLES = {
    'gesellschafterstreit-zink-und-zunder': ('Zink und Zunder - Gesellschafter im Streit', 'Zink und Zunder Metallbau GmbH | Berlin | Auftrag Romy Yilmaz'),
    'gesellschafterstreit-klageerwiderung-berlin': ('Klageerwiderung im Gesellschafterstreit', 'Spreebogen Lichtwerk GmbH | Berlin | 32 O 187/26'),
    'gesellschafterstreit-shareholder-agreement-muenchen': ('Drafting Shareholder Agreement', 'Isarwinkel Gerätebau GmbH | München | Beteiligung Vogl'),
}
ROOT = Path(__file__).resolve().parents[1]
ADDENDUM = 'Nachtrag_2026-10-08'


def sources(case):
    """Originalreihenfolge erhalten; der spätere Nachtrag folgt geschlossen."""
    if case.name not in TITLES:
        raise ValueError('Keine unterstützte Gesellschaftsrechtsakte: ' + case.name)
    return sorted((p for p, _ in document_arcname_pairs(case)), key=lambda p: (
        p.relative_to(case).parts[0] == ADDENDUM,
        p.relative_to(case).as_posix().casefold(),
    ))


def register_layout(paths, case, style):
    """Berechnet variable Zeilenhöhen, bevor die Dokumentseiten feststehen."""
    pages, current, used, previous = [], [], 0, None
    for path in paths:
        relative = path.relative_to(case).as_posix()
        group = 'Nachtrag 08.10.2026' if relative.startswith(ADDENDUM + '/') else 'Kernbestand 02.10.2026'
        paragraph = Paragraph(escape(relative), style)
        _, height = paragraph.wrap(438, 1000)
        row_height = max(29, height + 8)
        group_height = 20 if group != previous else 0
        if used + group_height + row_height > 620 and current:
            pages.append(current)
            current, used, previous = [], 0, None
            group_height = 20
        if group_height + row_height > 620:
            raise ValueError('Registerpfad passt nicht auf eine Seite: ' + relative)
        current.append((path, paragraph, height, row_height, group if group != previous else None))
        used += group_height + row_height
        previous = group
    if current:
        pages.append(current)
    return pages


def build_release_pdf(case):
    title, subtitle = TITLES[case.name]
    spec = importlib.util.spec_from_file_location('vorfuehr_pdf_renderer', Path(__file__).with_name('build-testakten-einzelpdf-zips.py'))
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    paths = sources(case)
    office = [p for p in paths if p.suffix.lstrip('.') in OFFICE_EXTS]
    cache = render_office_batch(office)
    if set(cache) != set(office):
        raise RuntimeError('Layoutgetreue Office-Konvertierung für diese Akten erforderlich.')
    docs = []
    for source in paths:
        data = renderer.render_document_pdf(source, case, cache)
        if not data:
            raise RuntimeError('Fehlende PDF: ' + source.name)
        docs.append((source, PdfReader(io.BytesIO(data))))
    pdfmetrics.registerFont(TTFont('VortragRegister', str(serif_font_path())))
    pdfmetrics.registerFont(TTFont('VortragRegisterBold', str(serif_font_path(True))))
    style = ParagraphStyle('Register', fontName='VortragRegister', fontSize=10, leading=12)
    register = register_layout(paths, case, style)
    register_pages = len(register)
    next_page = register_pages + 1
    positions = []
    for path, reader in docs:
        positions.append((path, next_page, len(reader.pages)))
        next_page += len(reader.pages)
    page_ranges = {path: (start, count) for path, start, count in positions}
    buffer = io.BytesIO()
    canvas = Canvas(buffer, pagesize=A4, invariant=1)
    has_addendum = any(ADDENDUM in p.relative_to(case).parts for p in paths)
    for entries in register:
        canvas.setFont('VortragRegisterBold',16)
        canvas.drawString(48,790,title)
        canvas.setFont('VortragRegister',10)
        canvas.drawString(48,767,subtitle)
        date_label = 'Kernstand 02.10.2026 | Nachtrag 08.10.2026' if has_addendum else 'Aktenstand 02.10.2026'
        canvas.drawString(48,746,date_label + ' | Dokumentenregister')
        y = 713
        for path, para, height, row_height, group in entries:
            if group:
                canvas.setFont('VortragRegisterBold',10)
                canvas.drawString(48,y-11,group)
                y-=20
            start, count = page_ranges[path]
            para.drawOn(canvas,48,y-height)
            canvas.setFont('VortragRegister',10)
            page_label=str(start) if count==1 else f'{start}–{start+count-1}'
            canvas.drawRightString(550,y-11,page_label)
            y-=row_height
        canvas.setFont('VortragRegister',9)
        canvas.drawString(48,45,'Originale und Korrespondenz; keine Auswertung beigefügt.')
        canvas.showPage()
    canvas.save()
    writer=PdfWriter()
    writer.append(PdfReader(io.BytesIO(buffer.getvalue())))
    writer.add_outline_item('Dokumentenregister',0)
    for (source,reader),(_,start,_) in zip(docs,positions):
        writer.append(reader,import_outline=False)
        writer.add_outline_item(source.relative_to(case).as_posix(),start-1)
    pdf_date = 'D:20261009000000Z' if has_addendum else 'D:20261002090000Z'
    writer.add_metadata({'/Title':title,'/Author':'Klotzkette','/Subject':subtitle,'/CreationDate':pdf_date,'/ModDate':pdf_date})
    target=case/'gesamt-pdf'/f'{case.name}_gesamt.pdf'
    target.parent.mkdir(exist_ok=True)
    temporary=target.with_suffix('.tmp')
    try:
        writer.write(temporary)
        if len(PdfReader(temporary).pages)!=next_page-1:
            raise RuntimeError('Seitenregister stimmt nicht mit Dokumentumfang überein.')
        temporary.replace(target)
    finally:
        temporary.unlink(missing_ok=True)
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cases', nargs='*', choices=sorted(TITLES), help='Ohne Auswahl werden nur diese drei Akten gebaut.')
    arguments = parser.parse_args()
    for name in arguments.cases or TITLES:
        print(build_release_pdf(ROOT / 'testakten' / name), flush=True)
