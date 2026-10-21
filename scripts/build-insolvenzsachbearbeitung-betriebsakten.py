#!/usr/bin/env python3
"""Drei Betriebsakten; --package-only verwendet unveränderte Originaldateien."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import zipfile
import xml.etree.ElementTree as ET
from pypdf import PdfReader, PdfWriter
from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN
from testakte_office_pdf import render_office_batch
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'scripts/data/insolvenzsachbearbeitung-betriebsakten.json'
TAG='insolvenzsachbearbeitung-v1.0.0'
BASE=f'https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}'
SLUGS={'insolvenzsachbearbeitung-kaufhaus-katzenbogen-muenchen','insolvenzsachbearbeitung-werkzeugkiste-augsburg','insolvenzsachbearbeitung-cafe-abendrot-regensburg'}
def helper():
 spec=importlib.util.spec_from_file_location('betriebsakten_basis',ROOT/'scripts/build-insolvenzanfechtung-akten.py')
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def cases():
 result=json.loads(DATA.read_text())
 if {c['slug'] for c in result}!=SLUGS:raise ValueError('Unerwartete Fallslugs')
 for c in result:
  n=len(c['files'])
  if ('kaufhaus' in c['slug'] and n<32) or ('kaufhaus' not in c['slug'] and not 20<=n<=24):raise ValueError('Falscher Umfang')
  names={i['name'] for i in c['files']}
  if len(names)!=n:raise ValueError('Doppelte Datei')
  for i in c['files']:
   if not re.fullmatch(r'\d{2}_[A-Za-z0-9_]+\.(pdf|docx|eml|xlsx)',i['name']):raise ValueError(i['name'])
   if any(a not in names for a in i.get('attachments',[])):raise ValueError('Anlage fehlt')
 return result

def archive_bytes(entries):
 """Flaches Archiv mit Hinweis zuerst und festen Metadaten."""
 target=io.BytesIO()
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as archive:
  for name in ['README.txt',*sorted(n for n in entries if n!='README.txt')]:
   info=zipfile.ZipInfo(name,(2026,10,21,8,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   archive.writestr(info,entries[name])
 return target.getvalue()

def print_settings(path,item):
 ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
 with zipfile.ZipFile(path) as z:entries={n:z.read(n) for n in z.namelist()}
 for name,data in list(entries.items()):
  if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
   sh=ET.fromstring(data);setup=sh.find(ns+'pageSetup')
   if setup is None:setup=ET.SubElement(sh,ns+'pageSetup')
   setup.set('orientation','landscape');setup.set('paperSize','9');setup.set('fitToWidth','1');setup.set('fitToHeight','0')
   entries[name]=ET.tostring(sh,encoding='utf-8',xml_declaration=True)
 wb=ET.fromstring(entries['xl/workbook.xml']);defined=wb.find(ns+'definedNames')
 if defined is None:defined=ET.SubElement(wb,ns+'definedNames')
 for old in list(defined):
  if old.get('name')=='_xlnm.Print_Area':defined.remove(old)
 end={'claims':'F$21','inventory':'E$17','ledger':'E$17','cafe':'E$22'}[item['kind']]
 area=ET.SubElement(defined,ns+'definedName',{'name':'_xlnm.Print_Area','localSheetId':'0'});area.text=f"'Arbeitsstand'!$A$1:${end}"
 entries['xl/workbook.xml']=ET.tostring(wb,encoding='utf-8',xml_declaration=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in entries.items():
   info=zipfile.ZipInfo(name,(2026,10,21,8,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data)

def author(cases,b,qa):
 runtime=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies'
 work=qa/'xlsx-build';work.mkdir(parents=True,exist_ok=True)
 link=work/'node_modules'
 if not link.exists():link.symlink_to(runtime/'node/node_modules',target_is_directory=True)
 target=work/'build-insolvenzsachbearbeitung-betriebsakten-xlsx.mjs';shutil.copyfile(ROOT/'scripts'/target.name,target)
 subprocess.run([str(runtime/'node/bin/node'),str(target),str(DATA),str(ROOT),str(qa/'xlsx')],check=True)
 basis=b.load_basis()
 for c in cases:
  directory=ROOT/'testakten'/c['slug'];directory.mkdir(parents=True,exist_ok=True)
  for i in c['files']:
   path=directory/i['name']
   if path.suffix=='.xlsx':print_settings(path,i)
   elif path.suffix=='.pdf':path.write_bytes(b.pdf_bytes(i))
   elif path.suffix=='.docx':basis.document(path,i)
  for i in c['files']:
   if i['name'].endswith('.eml'):b.write_email(directory/i['name'],i,c['slug'])

def package(cases,b,dist,qa,font):
 reports=[];basis=b.load_basis()
 for c in cases:
  directory=ROOT/'testakten'/c['slug'];b.validate_originals(c,directory)
  paths=[directory/i['name'] for i in c['files']]
  hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
  cache=render_office_batch(paths)
  missing=[p.name for p in paths if p.suffix in ('.docx','.xlsx') and p not in cache]
  if missing:raise RuntimeError(f'Native Office-PDFs fehlen: {missing}')
  writer=PdfWriter();originals={'README.txt':NOTICE_BYTES};single={'README.txt':NOTICE_BYTES};docs=[]
  pdfdir=qa/c['slug']/'einzelpdf';pdfdir.mkdir(parents=True,exist_ok=True)
  for i,p in zip(c['files'],paths):
   pdf=p.read_bytes() if p.suffix=='.pdf' else cache[p] if p in cache else b.pdf_bytes(b.read_text_original(p),True)
   reader=PdfReader(io.BytesIO(pdf));txt='\n'.join(page.extract_text() or '' for page in reader.pages)
   if not txt.strip() or 'Diese Testakte wurde mit KI' in txt or 'This test case file was generated' in txt:raise ValueError(f'PDF leer/Warntext {p}')
   start=len(writer.pages)
   for page in reader.pages:writer.add_page(page)
   writer.add_outline_item(p.name,start)
   originals[p.name]=p.read_bytes();single[p.stem+'.pdf']=pdf;(pdfdir/(p.stem+'.pdf')).write_bytes(pdf)
   docs.append({'file':p.name,'pages':len(reader.pages),'start_page':start+1,'sha256':hashes[p.name]})
  writer.add_metadata({'/Title':c['title'],'/Author':'Klotzkette','/CreationDate':'D:20261021080000Z','/ModDate':'D:20261021080000Z'})
  total=directory/'gesamt-pdf'/f"{c['slug']}_gesamt.pdf";total.parent.mkdir(exist_ok=True)
  with total.open('wb') as f:writer.write(f)
  shutil.copyfile(total,dist/total.name)
  for suffix,entries in [('',originals),('-einzelpdfs',single)]:
   data=archive_bytes(entries);target=dist/f"testakte-{c['slug']}{suffix}.zip";target.write_bytes(data)
   with zipfile.ZipFile(io.BytesIO(data)) as z:
    if len(z.namelist())!=len(paths)+1 or z.testzip() or any('/' in n for n in z.namelist()):raise ValueError('Paketfehler')
    if z.namelist()[0]!='README.txt' or not z.read('README.txt').startswith(NOTICE_BYTES):raise ValueError('Hinweis fehlt oder steht nicht zuerst')
  if hashes!={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}:raise ValueError('Originale verändert')
  counts=Counter(p.suffix for p in paths)
  xlsx_label='1 Excel-Arbeitsmappe' if counts['.xlsx']==1 else f"{counts['.xlsx']} Excel-Arbeitsmappen"
  xlsx_sentence='Die Arbeitsmappe enthält' if counts['.xlsx']==1 else 'Die Arbeitsmappen enthalten'
  rows='\n'.join(f"| `{d['file']}` | {i['title']} | {d['pages']} |" for i,d in zip(c['files'],docs))
  readme=f"""# 1. {c['title']}

{c['summary']}

[Startseite](../../README.md) · [Download-Index](../../ASSET_INDEX.md) · [Insolvenzsachbearbeitung](../../insolvenzsachbearbeitung/README.md) · [Testaktenübersicht](../README.md)

## 1.1. Benutzung

Beginnen Sie mit dem Arbeitsauftrag und dem gerichtlichen Beschluss. Ordnen Sie anschließend die Originalunterlagen nach Verfahrensstand, Absender, Adressat, Leistungszeitraum und Belegzusammenhang. Die Akte eignet sich für Posteingang, Sachverhaltsaufklärung, Forderungserfassung und die Vorbereitung einer Entscheidung durch den zuständigen Menschen. Sie enthält keine Musterlösung und keine vorweggenommene Tabellenfeststellung.

Der Bestand umfasst {len(paths)} Originalunterlagen und {len(writer.pages)} PDF-Seiten: {counts['.pdf']} PDF-Belege, {counts['.docx']} Word-Dateien, {counts['.eml']} echte E-Mail-Dateien und {xlsx_label}. Die E-Mail-Anlagen enthalten die tatsächlichen Dateien; sie sind außerdem separat vorhanden. {xlsx_sentence} Eingaben, Formeln und Erläuterungen ihrer Aussagegrenzen. Aktenstand 14.10.2026. Schrift: {font}, 11 pt; Tabellen bleiben als solche formatiert.

<!-- reserved-example-contacts -->

Alle Personen, Unternehmen, Anschriften, Kontakte und Aktenzeichen sind erfunden. Reale Ortsnamen bilden nur den geografischen Rahmen. Kontaktadressen verwenden reservierte .example-Domains.

<!-- BEGIN gesamt-pdf-section (autogen) -->

## 1.2. Downloads

{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF | [Gesamte Akte](gesamt-pdf/{c['slug']}_gesamt.pdf) |
| Einzel-PDF-ZIP | [Jede Unterlage als PDF]({BASE}/testakte-{c['slug']}-einzelpdfs.zip) |
| Akten-ZIP | [Originale als PDF, DOCX, EML und XLSX]({BASE}/testakte-{c['slug']}.zip) |

Die ZIPs sind flach und enthalten jeweils {len(paths)} Unterlagen sowie README.txt mit dem zweisprachigen Hinweis. Markdown-Dateien und das Gesamt-PDF sind nicht Teil des Original-ZIPs. E-Mail-Anlagen werden in der PDF-Lesefassung nicht erneut angehängt, weil sie als einzelne Unterlagen enthalten sind.

<!-- END gesamt-pdf-section (autogen) -->

## 1.3. Unterlagen

| Datei | Gegenstand | Seiten |
| --- | --- | ---: |
{rows}

Komponentenrelease `{TAG}`.
"""
  (directory/'README.md').write_text(readme)
  report={'slug':c['slug'],'documents':len(paths),'pages':len(writer.pages),'formats':dict(counts),'font':font,'originals_unchanged_by_packaging':True,'files':docs}
  reportdir=ROOT/'quality/insolvenzsachbearbeitung/akten';reportdir.mkdir(parents=True,exist_ok=True)
  (reportdir/f"{c['slug']}.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
  reports.append(report);print(f"{c['slug']}: {len(paths)} Originale, {len(writer.pages)} Seiten",flush=True)
 (qa/'akten-checks.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
 return reports

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--package-only',action='store_true');ap.add_argument('--dist',type=Path,default=Path('/tmp/insolvenzsachbearbeitung-20261021/dist-akten'));ap.add_argument('--qa',type=Path,default=Path('/tmp/insolvenzsachbearbeitung-20261021/qa-betriebsakten'));args=ap.parse_args()
 args.dist.mkdir(parents=True,exist_ok=True);args.qa.mkdir(parents=True,exist_ok=True)
 b=helper();font=b.configure_fonts();cs=cases()
 if not args.package_only:author(cs,b,args.qa)
 package(cs,b,args.dist,args.qa,font)
if __name__=='__main__':main()
