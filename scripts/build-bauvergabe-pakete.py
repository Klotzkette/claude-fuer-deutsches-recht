#!/usr/bin/env python3
"""Durchgehende Bauvergabe-Lesefassungen mit fünf Stationen und Seitenregister."""
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
from bauvergabe_falldaten import STAGES, case_by_slug
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import OFFICE_EXTS, render_office_batch


def sources(case):
    # Der gemeinsame Filter darf echte Aktenstücke nicht unbemerkt verlieren.
    # Deshalb ist der Dateibaum mit seinen fünf nativen Formaten der unabhängige
    # Vergleichsbestand; ein Gesamt-PDF gehört nicht erneut in seine eigene Quelle.
    native={p for p in case.rglob('*') if p.is_file()
            and p.suffix.lower() in {'.docx','.pdf','.eml','.csv','.xlsx'}
            and p.relative_to(case).parts[0] in STAGES}
    selected=[p for p,_ in document_arcname_pairs(case)]
    expected_count={'bauvergabe-klinikum-muenster':38,'bauvergabe-wohnhaus-bielefeld':39}[case.name]
    if len(native)!=expected_count:
        raise RuntimeError(f'Nativer Aktenbestand unvollständig: {case.name}: {len(native)} statt {expected_count}.')
    if len(selected)!=len(set(selected)) or set(selected)!=native:
        missing=sorted(p.relative_to(case).as_posix() for p in native-set(selected))
        extra=sorted(p.relative_to(case).as_posix() for p in set(selected)-native)
        raise RuntimeError(f'PDF-Quellenauswahl weicht vom nativen Dateibaum ab: fehlt={missing}; zusätzlich={extra}.')
    return sorted(selected,key=lambda p:p.relative_to(case).as_posix().casefold())


def build_release_pdf(case):
    data=case_by_slug(case.name)
    spec=importlib.util.spec_from_file_location('bauvergabe_pdf_renderer',Path(__file__).with_name('build-testakten-einzelpdf-zips.py'))
    renderer=importlib.util.module_from_spec(spec);spec.loader.exec_module(renderer)
    paths=sources(case)
    office=[p for p in paths if p.suffix.lstrip('.') in OFFICE_EXTS]
    cache=render_office_batch(office)
    if set(cache)!=set(office):raise RuntimeError('Vollständige native Office-Konvertierung erforderlich.')
    docs=[]
    for path in paths:
        content=renderer.render_document_pdf(path,case,cache)
        if not content:raise RuntimeError('Fehlende PDF: '+str(path))
        docs.append((path,PdfReader(io.BytesIO(content))))
    per_page=17
    register_pages=(len(docs)+per_page-1)//per_page
    cursor=register_pages+1;positions=[]
    for path,reader in docs:
        positions.append((path,cursor,len(reader.pages)));cursor+=len(reader.pages)
    pdfmetrics.registerFont(TTFont('BauRegister',str(serif_font_path())))
    pdfmetrics.registerFont(TTFont('BauRegisterBold',str(serif_font_path(True))))
    buffer=io.BytesIO();canvas=Canvas(buffer,pagesize=A4,invariant=1)
    style=ParagraphStyle('BauRegister',fontName='BauRegister',fontSize=10,leading=12)
    for offset in range(0,len(docs),per_page):
        canvas.setFont('BauRegisterBold',15)
        canvas.drawString(42,791,'Bauvergabe · '+data['city'])
        canvas.setFont('BauRegister',11)
        canvas.drawString(42,770,data['owner'])
        canvas.drawString(42,750,data['reference']+' · Dokumentenregister')
        y=719
        for path,start,count in positions[offset:offset+per_page]:
            relative=path.relative_to(case).as_posix()
            para=Paragraph(escape(relative),style);_,height=para.wrap(454,30)
            if height>30:raise ValueError('Registertitel zu lang: '+relative)
            para.drawOn(canvas,42,y-height)
            canvas.setFont('BauRegister',10)
            canvas.drawRightString(552,y-11,str(start) if count==1 else f'{start}–{start+count-1}')
            y-=36
        canvas.setFont('BauRegister',9)
        canvas.drawString(42,45,'Aktenstücke nach Arbeitsstation; Schreiben in Word und PDF sind derselbe Vorgang.')
        canvas.showPage()
    canvas.save();writer=PdfWriter();writer.append(PdfReader(io.BytesIO(buffer.getvalue())))
    writer.add_outline_item('Dokumentenregister',0);stages={}
    for (path,reader),(_,start,_) in zip(docs,positions):
        stage=path.relative_to(case).parts[0]
        if stage not in STAGES:raise ValueError('Unbekannte Arbeitsstation: '+stage)
        writer.append(reader,import_outline=False)
        if stage not in stages:stages[stage]=writer.add_outline_item(stage+' · '+STAGES[stage],start-1)
        writer.add_outline_item(path.name,start-1,parent=stages[stage])
    writer.add_metadata({'/Title':data['title'],'/Author':'Klotzkette','/Subject':data['reference'],'/CreationDate':'D:20261006090000Z','/ModDate':'D:20261006090000Z'})
    target=case/'gesamt-pdf'/f'{case.name}_gesamt.pdf';target.parent.mkdir(exist_ok=True)
    temporary=target.with_suffix('.tmp')
    try:
        writer.write(temporary)
        if len(PdfReader(temporary).pages)!=cursor-1:raise RuntimeError('Seitenregister und Dokumentumfang weichen ab.')
        temporary.replace(target)
    finally:temporary.unlink(missing_ok=True)
    return target
