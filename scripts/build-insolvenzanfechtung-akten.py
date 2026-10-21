#!/usr/bin/env python3
"""Zwei Anfechtungsakten; --package-only verpackt die versionierten Originale."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from email.utils import format_datetime, getaddresses
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import zipfile
import xml.etree.ElementTree as ET

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from xml.sax.saxutils import escape
from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN
from testakte_office_pdf import render_office_batch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'scripts/data/insolvenzanfechtung-akten.json'
TAG = 'insolvenzanfechtung-v1.0.0'
BASE = f'https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}'
SLUGS = {'insolvenzanfechtung-blechliebe-bamberg', 'insolvenzanfechtung-faltenwurf-fuerth'}
STAMP = 'D:20261021080000Z'

def load_basis():
    spec = importlib.util.spec_from_file_location('anfechtung_basis', ROOT / 'scripts/build-untersuchungshaft-akten.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.STAMP = datetime(2026, 10, 21, 8)
    return module

def configure_fonts():
    candidates = [(Path('/System/Library/Fonts/Supplemental'), 'Times New Roman.ttf', 'Times New Roman Bold.ttf', 'Times New Roman'),
                  (Path('/usr/share/fonts/truetype/msttcorefonts'), 'Times_New_Roman.ttf', 'Times_New_Roman_Bold.ttf', 'Times New Roman'),
                  (Path('/usr/share/fonts/truetype/liberation2'), 'LiberationSerif-Regular.ttf', 'LiberationSerif-Bold.ttf', 'Liberation Serif'),
                  (Path('/usr/share/fonts/truetype/liberation'), 'LiberationSerif-Regular.ttf', 'LiberationSerif-Bold.ttf', 'Liberation Serif')]
    for directory, regular, bold, label in candidates:
        if (directory / regular).is_file() and (directory / bold).is_file():
            pdfmetrics.registerFont(TTFont('AkteSerif', str(directory / regular)))
            pdfmetrics.registerFont(TTFont('AkteSerifBold', str(directory / bold)))
            pdfmetrics.registerFontFamily('AkteSerif', normal='AkteSerif', bold='AkteSerifBold')
            return label
    raise RuntimeError('Times New Roman oder Liberation Serif ist erforderlich')

def read_cases():
    cases = json.loads(DATA.read_text())
    if {c['slug'] for c in cases} != SLUGS: raise ValueError('Unerwartete Fallslugs')
    for case in cases:
        if len(case['files']) != 24: raise ValueError('24 Originale je Fall erforderlich')
        names = {f['name'] for f in case['files']}
        if len(names) != 24: raise ValueError('Doppelte Originaldatei')
        for item in case['files']:
            if not re.fullmatch(r'\d{2}_[A-Za-z0-9_]+\.(docx|pdf|xlsx|eml|txt)', item['name']): raise ValueError(item['name'])
            if case['slug'].endswith('faltenwurf-fuerth') and item['name'].startswith(('20_', '21_')):
                for field in ('author', 'to', 'body'):
                    item[field] = item[field].replace('Alina Kessel', 'Minna Eberlein').replace('alina.kessel@fichtelmann.example', 'minna.eberlein@fichtelmann.example').replace('Frau Kessel', 'Frau Eberlein')
            for name in item.get('attachments', []):
                if name not in names: raise ValueError(f'Fehlende Anlage {name}')
    return cases

def pdf_bytes(item, email=False):
    stream = io.BytesIO()
    doc = SimpleDocTemplate(stream, pagesize=A4, leftMargin=58, rightMargin=58, topMargin=48, bottomMargin=45,
                            title=item['title'], author=item['author'].split('\n')[0])
    normal = ParagraphStyle('Text', fontName='AkteSerif', fontSize=11, leading=14, spaceAfter=9)
    meta = ParagraphStyle('Kopf', parent=normal, fontSize=10, leading=13, textColor=HexColor('#333333'), spaceAfter=5)
    title = ParagraphStyle('Titel', parent=normal, fontName='AkteSerifBold', fontSize=14, leading=17, spaceBefore=12, spaceAfter=14)
    out=[]
    for label, value in [('Von' if email else 'Absender',item['author']),('An',item['to']),('Datum',item['date'])]:
        out.append(Paragraph(escape(label+': '+value).replace('\n','<br/>'),meta))
    if item.get('cc'): out.append(Paragraph('Cc: '+escape(item['cc']),meta))
    if item.get('attachments'): out.append(Paragraph('Anlagen: '+escape(', '.join(item['attachments'])),meta))
    out.append(Paragraph(escape(item['title']),title))
    for block in item['body'].split('\n\n'):
        style = title if re.match(r'^\d+(?:\.\d+)* ',block) and '\n' not in block and len(block)<90 else normal
        out.append(Paragraph(escape(block).replace('\n','<br/>'),style))
    def page(canvas, document):
        canvas.saveState();canvas.setFont('AkteSerif',9);canvas.drawRightString(A4[0]-58,28,f'Seite {document.page}');canvas.restoreState()
    def stable_canvas(*args, **kwargs):
        kwargs['invariant']=1
        return Canvas(*args, **kwargs)
    doc.build(out,onFirstPage=page,onLaterPages=page,canvasmaker=stable_canvas)
    return stream.getvalue()

def write_email(path, item, slug):
    mail=EmailMessage(policy=policy.SMTP)
    for key, value in [('From',item['author']),('To',item['to']),('Subject',item['title']),('Date',format_datetime(datetime.fromisoformat(item['date']))),('Message-ID',f'<{slug}-{path.stem}@akten.example>')]: mail[key]=value
    mail['Content-Language']='de-DE'
    if item.get('cc'): mail['Cc']=item['cc']
    if item.get('reply_to'):
        ref=f"<{slug}-{Path(item['reply_to']).stem}@akten.example>";mail['In-Reply-To']=ref;mail['References']=ref
    mail.set_content(item['body'],charset='utf-8')
    for name in item.get('attachments',[]):
        suffix=Path(name).suffix
        subtype={'.pdf':'pdf','.xlsx':'vnd.openxmlformats-officedocument.spreadsheetml.sheet','.docx':'vnd.openxmlformats-officedocument.wordprocessingml.document'}[suffix]
        mail.add_attachment((path.parent/name).read_bytes(),maintype='application',subtype=subtype,filename=name)
    if item.get('attachments'):mail.set_boundary(f'akte-{slug}-{path.stem}')
    path.write_bytes(mail.as_bytes())

def read_text_original(path):
    """Render package-only copies from the committed bytes, never fixture prose."""
    if path.suffix == '.eml':
        mail=BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        body=mail.get_body(preferencelist=('plain',))
        if body is None: raise ValueError(f'Keine Textfassung in {path}')
        return {'author':str(mail['From']), 'to':str(mail['To']), 'date':str(mail['Date']),
                'title':str(mail['Subject']), 'body':body.get_content().rstrip(),
                'attachments':[p.get_filename() for p in mail.iter_attachments()],
                'cc':str(mail['Cc']) if mail['Cc'] else ''}
    parts=path.read_text(encoding='utf-8').split('\n\n',4)
    if len(parts)!=5: raise ValueError(f'Textkopf unvollständig: {path}')
    return dict(zip(('author','to','date','title','body'),parts))

def validate_originals(case, directory):
    for item in case['files']:
        path=directory/item['name']
        if not path.is_file() or not path.stat().st_size:raise ValueError(f'Original fehlt: {path}')
        if path.suffix=='.eml':
            mail=BytesParser(policy=policy.default).parsebytes(path.read_bytes())
            if mail.defects:raise ValueError(f'EML defekt: {path}')
            for h in ['From','To','Date','Subject','Message-ID','MIME-Version']:
                if not mail[h]:raise ValueError(f'Header fehlt: {path}/{h}')
            for _, address in getaddresses([str(mail['From']),str(mail['To'])]):
                if not address.endswith('.example'):raise ValueError(f'Echte Mailadresse: {address}')
            actual={p.get_filename():p.get_payload(decode=True) for p in mail.iter_attachments()}
            expected={name:(directory/name).read_bytes() for name in item.get('attachments',[])}
            if actual!=expected:raise ValueError(f'MIME-Anlagen stimmen nicht: {path}')
        elif path.suffix in ('.docx','.xlsx'):
            with zipfile.ZipFile(path) as z:
                if z.testzip():raise ValueError(f'OOXML beschädigt: {path}')
                if path.suffix=='.xlsx':
                    texts=[z.read(n).decode() for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')]
                    if not any(ET.fromstring(t).find('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}f') is not None for t in texts):raise ValueError(f'Excel ohne Formeln: {path}')
        elif path.suffix=='.pdf':
            if not PdfReader(path).pages:raise ValueError(f'PDF leer: {path}')

def set_xlsx_print(path, item):
    # Artifact Tool authors all cells/formulas. Add the print-only OOXML settings
    # for the deliberately wide accounting schedules before Office rendering.
    ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    with zipfile.ZipFile(path) as z:entries={n:z.read(n) for n in z.namelist()}
    for n,b in list(entries.items()):
        if n.startswith('xl/worksheets/sheet') and n.endswith('.xml'):
            sh=ET.fromstring(b);setup=sh.find(ns+'pageSetup')
            if setup is None:setup=ET.SubElement(sh,ns+'pageSetup')
            setup.set('orientation','landscape');setup.set('paperSize','9');setup.set('fitToWidth','1');setup.set('fitToHeight','0')
            entries[n]=ET.tostring(sh,encoding='utf-8',xml_declaration=True)
    workbook=ET.fromstring(entries['xl/workbook.xml'])
    defined=workbook.find(ns+'definedNames')
    if defined is None:defined=ET.SubElement(workbook,ns+'definedNames')
    for old in list(defined):
        if old.get('name')=='_xlnm.Print_Area':defined.remove(old)
    area=ET.SubElement(defined,ns+'definedName',{'name':'_xlnm.Print_Area','localSheetId':'0'})
    last={'opos':'F$21','payments':'E$24','loans':'E$20','bank':'C$20'}[item['kind']]
    area.text=f"'Abgleich'!$A$1:${last}"
    entries['xl/workbook.xml']=ET.tostring(workbook,encoding='utf-8',xml_declaration=True)
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for n,b in entries.items():z.writestr(n,b)

def build_originals(cases, basis, qa):
    runtime=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies'
    node=runtime/'node/bin/node';packages=runtime/'node/node_modules'
    if not node.is_file():raise RuntimeError('Bundled Node für XLSX-Erstellung fehlt; vorhandene Originale mit --package-only verpacken')
    work=qa/'xlsx-build';work.mkdir(parents=True,exist_ok=True)
    link=work/'node_modules'
    if not link.exists():link.symlink_to(packages,target_is_directory=True)
    script=work/'build-insolvenzanfechtung-xlsx.mjs';shutil.copyfile(ROOT/'scripts/build-insolvenzanfechtung-xlsx.mjs',script)
    subprocess.run([str(node),str(script),str(DATA),str(ROOT),str(qa/'xlsx')],check=True)
    for case in cases:
        directory=ROOT/'testakten'/case['slug'];directory.mkdir(parents=True,exist_ok=True)
        for item in case['files']:
            path=directory/item['name']
            if path.suffix=='.xlsx':set_xlsx_print(path, item)
            elif path.suffix=='.pdf':path.write_bytes(pdf_bytes(item))
            elif path.suffix=='.docx':basis.document(path,item)
            elif path.suffix=='.txt':path.write_text('\n\n'.join(item[k] for k in ['author','to','date','title','body'])+'\n')
        for item in case['files']:
            if item['name'].endswith('.eml'):write_email(directory/item['name'],item,case['slug'])

def package_cases(cases,basis,dist,qa,font_label):
    reports=[]
    for case in cases:
        directory=ROOT/'testakten'/case['slug'];validate_originals(case,directory)
        paths=[directory/x['name'] for x in case['files']]
        cache=render_office_batch(paths)
        missing=[str(p) for p in paths if p.suffix in ('.docx','.xlsx') and p not in cache]
        if missing:raise RuntimeError('Native Office-PDFs fehlen: '+', '.join(missing))
        writer=PdfWriter();originals={'README.txt':NOTICE_BYTES};singles={'README.txt':NOTICE_BYTES};docs=[]
        pdfdir=qa/case['slug']/'einzelpdf';pdfdir.mkdir(parents=True,exist_ok=True)
        for item,path in zip(case['files'],paths):
            if path.suffix=='.pdf':pdf=path.read_bytes()
            elif path in cache:pdf=cache[path]
            elif path.suffix in ('.eml','.txt'):pdf=pdf_bytes(read_text_original(path),path.suffix=='.eml')
            else:raise ValueError(path)
            reader=PdfReader(io.BytesIO(pdf));text='\n'.join(p.extract_text() or '' for p in reader.pages)
            if not text.strip() or 'Diese Testakte wurde mit KI' in text or 'This test case file was generated' in text:raise ValueError(f'PDF leer/Warntext: {path}')
            start=len(writer.pages)
            for page in reader.pages:writer.add_page(page)
            writer.add_outline_item(path.name,start)
            originals[path.name]=path.read_bytes();singles[path.stem+'.pdf']=pdf
            (pdfdir/(path.stem+'.pdf')).write_bytes(pdf)
            docs.append({'file':path.name,'pages':len(reader.pages),'start_page':start+1,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        writer.add_metadata({'/Title':case['title'],'/Author':'Klotzkette','/CreationDate':STAMP,'/ModDate':STAMP})
        total=directory/'gesamt-pdf'/f"{case['slug']}_gesamt.pdf";total.parent.mkdir(exist_ok=True)
        with total.open('wb') as handle:writer.write(handle)
        shutil.copyfile(total,dist/total.name)
        for suffix,entries in [('',originals),('-einzelpdfs',singles)]:
            data=basis.archive_bytes(entries);target=dist/f"testakte-{case['slug']}{suffix}.zip";target.write_bytes(data)
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                if len(z.namelist())!=25 or z.testzip():raise ValueError(f'Paketfehler {target}')
        counts=Counter(p.suffix for p in paths)
        rows='\n'.join(f"| `{d['file']}` | {item['title']} | {d['pages']} |" for item,d in zip(case['files'],docs))
        font_note='Times New Roman, 11 pt.' if font_label=='Times New Roman' else 'PDF-Ersatzschrift: Liberation Serif, 11 pt; Times New Roman war in der Buildumgebung nicht installiert.'
        readme=f"""# 1. {case['title']}

{case['summary']}

[Startseite](../../README.md) · [Download-Index](../../ASSET_INDEX.md) · [Insolvenzanfechtung](../../insolvenzanfechtung/README.md) · [Testaktenübersicht](../README.md)

## 1.1. Benutzung

Beginnen Sie mit dem Mandatsschreiben. Ordnen Sie anschließend Zahlung, Leistung, Sicherheit und damaliges Wissen anhand der beigefügten Unterlagen. Sie können eine erste anwaltliche Antwort, eine Belegmatrix und die weitere Sachverhaltsaufklärung erarbeiten. Die Akte enthält keine fertige Lösung und keine vorgegebene gerichtliche Entscheidung über die Rückforderung.

Der Bestand umfasst 24 Originalunterlagen und {len(writer.pages)} PDF-Seiten: {counts['.docx']} Word-Dateien, {counts['.pdf']} PDF-Belege, {counts['.eml']} E-Mails, {counts['.xlsx']} Excel-Arbeitsmappen und {counts['.txt']} Textdateien. E-Mail-Anlagen enthalten die tatsächlichen Dateien. Die Excel-Arbeitsmappen erläutern Eingaben, Formeln und Reichweite der Zahlen. Aktenstand 21.10.2026. {font_note}

<!-- reserved-example-contacts -->

Alle Personen, Unternehmen, Geschäftsadressen, Aktenzeichen und Kontakte sind erfunden; reale Ortsnamen dienen nur als geografischer Rahmen. Kontaktadressen verwenden reservierte .example-Domains.

<!-- BEGIN gesamt-pdf-section (autogen) -->

## 1.2. Downloads

{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF | [Gesamte Akte](gesamt-pdf/{case['slug']}_gesamt.pdf) |
| Einzel-PDF-ZIP | [Einzelne Dokumente]({BASE}/testakte-{case['slug']}-einzelpdfs.zip) |
| Akten-ZIP | [Word, Excel, PDF, EML und TXT]({BASE}/testakte-{case['slug']}.zip) |

Die ZIPs sind flach und enthalten jeweils 24 Unterlagen sowie README.txt mit dem zweisprachigen Hinweis. Das Original-ZIP enthält keine Markdown-Dateien und kein Gesamt-PDF. Die PDF-Lesefassungen geben jede Originaldatei einmal wieder; eingebettete E-Mail-Anlagen werden dabei nicht doppelt gezählt.

<!-- END gesamt-pdf-section (autogen) -->

## 1.3. Unterlagen

| Datei | Gegenstand | Seiten |
| --- | --- | ---: |
{rows}

Komponentenrelease `{TAG}`.
"""
        (directory/'README.md').write_text(readme)
        report={'slug':case['slug'],'documents':24,'pages':len(writer.pages),'formats':dict(counts),'font':font_label,'files':docs}
        manifest_dir=ROOT/'quality/insolvenzanfechtung/akten';manifest_dir.mkdir(parents=True,exist_ok=True)
        (manifest_dir/f"{case['slug']}.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        (directory/'manifest.json').unlink(missing_ok=True)
        reports.append(report);print(f"{case['slug']}: 24 Originale, {len(writer.pages)} Seiten",flush=True)
    (qa/'akten-checks.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
    return reports

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--package-only',action='store_true');ap.add_argument('--dist',type=Path,default=Path('/tmp/insolvenzanfechtung-20261021/dist-akten'));ap.add_argument('--qa',type=Path,default=Path('/tmp/insolvenzanfechtung-20261021/qa-neue-akten'));args=ap.parse_args()
    args.dist.mkdir(parents=True,exist_ok=True);args.qa.mkdir(parents=True,exist_ok=True)
    cases=read_cases();basis=load_basis();label=configure_fonts()
    if not args.package_only:build_originals(cases,basis,args.qa)
    package_cases(cases,basis,args.dist,args.qa,label)

if __name__=='__main__':main()
