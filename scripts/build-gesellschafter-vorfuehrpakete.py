#!/usr/bin/env python3
"""Numerisch geordnete Gesellschaftsrechtsakten mit Dokumentenregister."""
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
    'gesellschafterstreit-klageerwiderung-berlin': ('Klageerwiderung im Gesellschafterstreit', 'Spreebogen Lichtwerk GmbH | Berlin | 32 O 187/26'),
    'gesellschafterstreit-shareholder-agreement-muenchen': ('Drafting Shareholder Agreement', 'Isarwinkel Gerätebau GmbH | München | Beteiligung Vogl'),
}


def sources(case):
    return sorted((p for p, _ in document_arcname_pairs(case)), key=lambda p: p.name.casefold())


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
    rows_per_page = 21
    register_pages = (len(docs) + rows_per_page - 1) // rows_per_page
    next_page = register_pages + 1
    positions = []
    for path, reader in docs:
        positions.append((path, next_page, len(reader.pages)))
        next_page += len(reader.pages)
    pdfmetrics.registerFont(TTFont('VortragRegister', str(serif_font_path())))
    pdfmetrics.registerFont(TTFont('VortragRegisterBold', str(serif_font_path(True))))
    buffer = io.BytesIO()
    canvas = Canvas(buffer, pagesize=A4, invariant=1)
    style = ParagraphStyle('Register', fontName='VortragRegister', fontSize=10, leading=12)
    for offset in range(0,len(docs),rows_per_page):
        canvas.setFont('VortragRegisterBold',16)
        canvas.drawString(48,790,title)
        canvas.setFont('VortragRegister',10)
        canvas.drawString(48,767,subtitle)
        canvas.drawString(48,746,'Aktenstand 02.10.2026 | Dokumentenregister zur Lesefassung')
        y = 713
        for path, start, count in positions[offset:offset+rows_per_page]:
            para=Paragraph(escape(path.name),style)
            _,height=para.wrap(438,27)
            if height>27:
                raise ValueError('Registertitel zu lang: '+path.name)
            para.drawOn(canvas,48,y-height)
            canvas.setFont('VortragRegister',10)
            page_label=str(start) if count==1 else f'{start}–{start+count-1}'
            canvas.drawRightString(550,y-11,page_label)
            y-=29
        canvas.setFont('VortragRegister',9)
        canvas.drawString(48,45,'Originale und Korrespondenz; keine Auswertung beigefügt.')
        canvas.showPage()
    canvas.save()
    writer=PdfWriter()
    writer.append(PdfReader(io.BytesIO(buffer.getvalue())))
    writer.add_outline_item('Dokumentenregister',0)
    for (source,reader),(_,start,_) in zip(docs,positions):
        writer.append(reader,import_outline=False)
        writer.add_outline_item(source.stem,start-1)
    writer.add_metadata({'/Title':title,'/Author':'Klotzkette','/Subject':subtitle,'/CreationDate':'D:20261002090000Z','/ModDate':'D:20261002090000Z'})
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
