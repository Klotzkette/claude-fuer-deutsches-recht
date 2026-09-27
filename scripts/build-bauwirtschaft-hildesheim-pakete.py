#!/usr/bin/env python3
"""Reproduzierbare Lesefassung und Archive der Hildesheimer Originale."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import zipfile
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib import colors
from xml.sax.saxutils import escape
from bauwirtschaft_hildesheim_common import ROOT, CASE, ASSETS, SLUG, setup_fonts
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_zip_common import working_dump_flat_pairs
from testakte_office_pdf import render_office_batch

QA=ASSETS/'qa'

def module(name,filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/filename)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def sources(case_dir=CASE):
    return sorted((p for p,_ in working_dump_flat_pairs(case_dir,include_gesamt_pdf=False)),key=lambda p:p.name)

def normalize(data,title):
    r=PdfReader(io.BytesIO(data));w=PdfWriter()
    for p in r.pages:w.add_page(p)
    meta={'/Author':'Klotzkette','/Creator':'Klotzkette','/Title':title,'/Producer':'Klotzkette'}
    if r.metadata and r.metadata.get('/Subject'):meta['/Subject']=r.metadata['/Subject']
    w.add_metadata(meta);out=io.BytesIO();w.write(out);return out.getvalue()

def render(*, native_release=False, case_dir=CASE, qa_dir=QA):
    qa_dir.mkdir(parents=True,exist_ok=True);E=module('hildesheim_single','build-testakten-einzelpdf-zips.py')
    renderer=os.environ.get('DOCX_RENDERER')
    if not native_release and not renderer:raise RuntimeError('DOCX_RENDERER muss auf render_docx.py zeigen.')
    paths=sources(case_dir);pending=[]
    if len({p.stem for p in paths}) != len(paths):
        raise RuntimeError('Originale benötigen unterschiedliche Dateistämme für ihre PDF-Fassungen.')
    fingerprints={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    # Im Release-Cache müssen auch Änderungen an Konvertern einen Neubau auslösen.
    pipeline=hashlib.sha256(b''.join((ROOT/'scripts'/name).read_bytes() for name in (
        'build-bauwirtschaft-hildesheim-pakete.py', 'build-testakten-einzelpdf-zips.py',
        'build-testakte-gesamt-pdf.py', 'testakte_office_pdf.py'))).hexdigest()
    for p in paths:
        cache=qa_dir/p.stem;fingerprint=fingerprints[p]
        stale_pipeline=native_release and (not (cache/'pipeline.sha256').exists() or (cache/'pipeline.sha256').read_text()!=pipeline)
        if stale_pipeline or not (cache/'source.sha256').exists() or (cache/'source.sha256').read_text()!=fingerprint or not (cache/(p.stem+'.pdf')).exists():pending.append(p)
    office_paths=[p for p in pending if p.suffix=='.xlsx' or (native_release and p.suffix=='.docx')]
    office=render_office_batch(office_paths)
    if native_release and set(office_paths)-set(office):
        missing=', '.join(p.name for p in office_paths if p not in office)
        raise RuntimeError('Native Office-Konvertierung fehlt; LibreOffice/SOFFICE prüfen: '+missing)
    index=[]
    for p in paths:
        cache=qa_dir/p.stem;cache.mkdir(parents=True,exist_ok=True);pdf=cache/(p.stem+'.pdf')
        if p in pending:
            if p.suffix=='.docx' and not native_release:
                r=subprocess.run([sys.executable,renderer,str(p),'--output_dir',str(cache),'--emit_pdf','--dpi','110'],capture_output=True,text=True)
                (cache/'render.log').write_text(r.stdout+'\n'+r.stderr)
                if r.returncode or not pdf.is_file():raise RuntimeError(f'DOCX-Render fehlgeschlagen: {p.name}; {cache}/render.log')
                data=pdf.read_bytes()
            else:data=E.render_document_pdf(p,case_dir,office)
            if not data:raise RuntimeError('Keine PDF-Ausgabe: '+p.name)
            pdf.write_bytes(normalize(data,p.stem))
            if hashlib.sha256(p.read_bytes()).hexdigest() != fingerprints[p]:
                raise RuntimeError('Original während der Konvertierung geändert: '+p.name)
            (cache/'source.sha256').write_text(fingerprints[p])
            if native_release:(cache/'pipeline.sha256').write_text(pipeline)
        index.append(dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pdf=str(pdf),pages=len(PdfReader(pdf).pages)))
        print(f'{p.name}: {index[-1]["pages"]} Seiten',flush=True)
    (qa_dir/'index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
    return index

def build_aggregate(index, *, case_dir=CASE, qa_dir=QA):
    """Erzeugt nur die geordnete Gesamt-PDF mit einem Lesezeichen je Original."""
    qa_dir.mkdir(parents=True,exist_ok=True)
    setup_fonts()
    body=ParagraphStyle('Body',fontName='Hildesheim',fontSize=10,leading=13,spaceAfter=8)
    title=ParagraphStyle('Title',parent=body,fontName='HildesheimBold',fontSize=17,leading=21,spaceAfter=14)
    small=ParagraphStyle('Small',parent=body,fontSize=8.5,leading=11,spaceAfter=3)
    def p(s,st=body):return Paragraph(escape(s),st)
    # Register ist Bestandteil der Lesefassung, kein Ersatz für die Originale.
    rows=[[p('Datei',small),p('Seiten',small)]]+[[p(d['file'],small),p(str(d['pages']),small)] for d in index]
    table=Table(rows,colWidths=[445,50],repeatRows=1)
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf0')),('LINEBELOW',(0,0),(-1,-1),.2,colors.HexColor('#cbd1d4')),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
    register=qa_dir/'register.pdf'
    SimpleDocTemplate(str(register),pagesize=A4,leftMargin=50,rightMargin=50,topMargin=50,bottomMargin=45,author='Klotzkette',title='Wohnhof Am Steinbogen Hildesheim').build([
      p('Wohnhof Am Steinbogen in Hildesheim',title),
      p('Acht Mietwohnungen · Projekt SW-HI-26-08 · Projektunterlagen Oktober 2026 bis 5. Oktober 2033'),
      p(f'Dokumentenregister mit {len(index)} Originaldateien. Die Dateien sind nach ihrer stabilen Aktennummer angeordnet. Die Originale behalten ihre eigenen Datierungen.'),
      Spacer(1,10),table])
    writer=PdfWriter();writer.append(register,outline_item='Dokumentenregister')
    for d in index:writer.append(d['pdf'],outline_item=d['file'])
    writer.add_metadata({'/Author':'Klotzkette','/Creator':'Klotzkette','/Producer':'Klotzkette','/Title':'Achtfamilienhaus Hildesheim Gesamtakte'})
    total=case_dir/'gesamt-pdf'/f'{SLUG}_gesamt.pdf';total.parent.mkdir(parents=True,exist_ok=True)
    temporary=total.with_name('.'+total.name+'.tmp')
    try:
        with temporary.open('wb') as f:writer.write(f)
        if not PdfReader(temporary).pages:raise RuntimeError('Leere Gesamt-PDF erzeugt.')
        temporary.replace(total)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'{len(index)} Originale; {len(PdfReader(total).pages)} Seiten Gesamt-PDF',flush=True)
    return total

def build_release_pdf(case_dir=CASE):
    """Zentraler Release-Einstieg ohne Skill-Renderer und ohne ZIP-Nebenprodukte."""
    if case_dir.name != SLUG:
        raise ValueError('Dieser Release-Einstieg gilt ausschließlich für '+SLUG)
    qa_dir=ASSETS/'release-qa'
    index=render(native_release=True,case_dir=case_dir,qa_dir=qa_dir)
    return build_aggregate(index,case_dir=case_dir,qa_dir=qa_dir)

def package(index):
    total=build_aggregate(index)
    notice=NOTICE_BYTES+b'\n\n'+(
      'Fiktives Achtfamilienhaus in Hildesheim. Personen, Unternehmen, Grundstück, Planungen und Verwaltungsvorgänge sind erfunden. '
      'Recherche- und Redaktionsstand 27.09.2026; der Projektverlauf 2026 bis 2033 ist simuliert. Bereits verkündete Übergangsregeln werden berücksichtigt; unbekanntes künftiges Recht wird nicht behauptet. '
      'Kontaktadressen mit .example sind reserviert. Die Originale enthalten keine Musterlösung. Autor: Klotzkette.\n').encode()
    with zipfile.ZipFile(ASSETS/f'testakte-{SLUG}.zip','w',zipfile.ZIP_DEFLATED) as z:
        z.writestr(NOTICE_FILENAME,notice)
        for p,name in working_dump_flat_pairs(CASE,include_gesamt_pdf=True):z.write(p,name)
    with zipfile.ZipFile(ASSETS/f'testakte-{SLUG}-einzelpdfs.zip','w',zipfile.ZIP_DEFLATED) as z:
        z.writestr(NOTICE_FILENAME,notice)
        for d in index:z.write(d['pdf'],Path(d['file']).stem+'.pdf')
    return total

def main():
    ap=argparse.ArgumentParser()
    mode=ap.add_mutually_exclusive_group()
    mode.add_argument('--package-only',action='store_true')
    mode.add_argument('--release-pdf-only',action='store_true',help='Native Office-Konvertierung und nur die Gesamt-PDF erzeugen')
    args=ap.parse_args()
    if args.release_pdf_only:
        build_release_pdf()
        return
    index=json.loads((QA/'index.json').read_text()) if args.package_only else render()
    if args.package_only:
        current={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources()}
        assert current=={d['file']:d['sha256'] for d in index},'Originale nach Render geändert'
    package(index)

if __name__=='__main__':main()
