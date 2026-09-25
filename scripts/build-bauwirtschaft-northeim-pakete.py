#!/usr/bin/env python3
"""Native Office-Rechnung, Versandbelege und fallbezogene Pakete. Autor: Klotzkette."""
from pathlib import Path
import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET
from pypdf import PdfReader, PdfWriter
from PIL import Image, ImageDraw
from office_process import run_office
from testakte_office_pdf import render_office_batch, office_binary
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'bauwirtschaft-vergabeverfahren-feuerwehrhaus-northeim'
CASE = ROOT/'testakten'/SLUG
OUT = Path('/tmp/bauwirtschaft-assets')
QA = OUT/'.northeim-qa'
SOFFICE = office_binary()
POPPLER = os.environ.get('AKTEN_PDFTOPPM') or shutil.which('pdftoppm')

def load(name, file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/file)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def metadata(data, title):
    reader=PdfReader(io.BytesIO(data));writer=PdfWriter()
    writer.append(reader)
    writer.add_metadata({'/Author':'Klotzkette','/Title':title,'/Creator':'Klotzkette','/CreationDate':'D:20260925140000+02\'00\'','/ModDate':'D:20260925140000+02\'00\''})
    out=io.BytesIO();writer.write(out);return out.getvalue()

def xlsx_print_settings(file, invalidate=False):
    ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main';q=lambda n:f'{{{ns}}}{n}'
    with zipfile.ZipFile(file) as z: entries={i.filename:(i,z.read(i.filename)) for i in z.infolist()}
    wb=ET.fromstring(entries['xl/workbook.xml'][1]);sheets=wb.find(q('sheets'))
    defs=wb.find(q('definedNames'))
    if defs is None:
        defs=ET.Element(q('definedNames'));calc=wb.find(q('calcPr'));wb.insert(list(wb).index(calc) if calc is not None else len(wb),defs)
    for old in list(defs):
        if old.get('name') in ('_xlnm.Print_Area','_xlnm.Print_Titles'):defs.remove(old)
    order='sheetPr dimension sheetViews sheetFormatPr cols sheetData sheetCalcPr sheetProtection protectedRanges scenarios autoFilter sortState dataConsolidate customSheetViews mergeCells phoneticPr conditionalFormatting dataValidations hyperlinks printOptions pageMargins pageSetup headerFooter rowBreaks colBreaks customProperties cellWatches ignoredErrors smartTags drawing legacyDrawing legacyDrawingHF picture oleObjects controls webPublishItems tableParts extLst'.split()
    def replace(node, name, new):
        for old in list(node):
            if old.tag==q(name):node.remove(old)
        index=next((i for i,e in enumerate(node) if e.tag.split('}')[-1] in order and order.index(e.tag.split('}')[-1])>order.index(name)),len(node))
        node.insert(index,new)
    for i,s in enumerate(sheets):
        name=s.get('name');end='F' if name=='LV' else 'E'
        ET.SubElement(defs,q('definedName'),{'name':'_xlnm.Print_Area','localSheetId':str(i)}).text=f"'{name}'!$A$1:${end}$31"
        if name=='LV':ET.SubElement(defs,q('definedName'),{'name':'_xlnm.Print_Titles','localSheetId':str(i)}).text="'LV'!$1:$5"
        key=f'xl/worksheets/sheet{i+1}.xml';sheet=ET.fromstring(entries[key][1])
        if invalidate:
            for cell in sheet.iter(q('c')):
                if cell.find(q('f')) is not None:
                    for cached in list(cell):
                        if cached.tag in (q('v'),q('is')):cell.remove(cached)
                    cell.attrib.pop('t',None)
        pr=sheet.find(q('sheetPr'))
        if pr is None:pr=ET.Element(q('sheetPr'));sheet.insert(0,pr)
        setup=pr.find(q('pageSetUpPr'))
        if setup is None:setup=ET.SubElement(pr,q('pageSetUpPr'))
        setup.set('fitToPage','1')
        replace(sheet,'pageMargins',ET.Element(q('pageMargins'),dict(left='0.3',right='0.3',top='0.35',bottom='0.35',header='0.1',footer='0.15')))
        replace(sheet,'pageSetup',ET.Element(q('pageSetup'),dict(paperSize='9',orientation='landscape' if name=='LV' else 'portrait',fitToWidth='1',fitToHeight='0' if name=='LV' else '1')))
        footer=ET.Element(q('headerFooter'));ET.SubElement(footer,q('oddFooter')).text='&LNO-FH26-L430&C'+name+'&RSeite &P'
        replace(sheet,'headerFooter',footer)
        entries[key]=(entries[key][0],ET.tostring(sheet,encoding='utf-8',xml_declaration=True))
    entries['xl/workbook.xml']=(entries['xl/workbook.xml'][0],ET.tostring(wb,encoding='utf-8',xml_declaration=True))
    if 'docProps/core.xml' not in entries:
        core=ET.Element('{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}coreProperties')
        entries['docProps/core.xml']=(zipfile.ZipInfo('docProps/core.xml'),b'')
        types=ET.fromstring(entries['[Content_Types].xml'][1])
        ET.SubElement(types,'{http://schemas.openxmlformats.org/package/2006/content-types}Override',{'PartName':'/docProps/core.xml','ContentType':'application/vnd.openxmlformats-package.core-properties+xml'})
        entries['[Content_Types].xml']=(entries['[Content_Types].xml'][0],ET.tostring(types,encoding='utf-8',xml_declaration=True))
        rels=ET.fromstring(entries['_rels/.rels'][1])
        ET.SubElement(rels,'{http://schemas.openxmlformats.org/package/2006/relationships}Relationship',{'Id':'rIdNortheimCore','Type':'http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties','Target':'docProps/core.xml'})
        entries['_rels/.rels']=(entries['_rels/.rels'][0],ET.tostring(rels,encoding='utf-8',xml_declaration=True))
    else:
        core=ET.fromstring(entries['docProps/core.xml'][1])
    for key in ['{http://purl.org/dc/elements/1.1/}creator','{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}lastModifiedBy']:
        e=core.find(key)
        if e is None:e=ET.SubElement(core,key)
        e.text='Klotzkette'
    entries['docProps/core.xml']=(entries['docProps/core.xml'][0],ET.tostring(core,encoding='utf-8',xml_declaration=True))
    temp=file.with_suffix('.xlsx.tmp')
    with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
        for key,(info,data) in entries.items():z.writestr(info,data)
    temp.replace(file)

def recalc():
    if not SOFFICE:raise RuntimeError('Native Office-Rechnung benötigt SOFFICE oder LibreOffice im PATH.')
    xlsx=list(sorted(CASE.glob('*.xlsx')))
    for f in xlsx:xlsx_print_settings(f,invalidate=True)
    staged=QA/'recalc';staged.mkdir(parents=True,exist_ok=True)
    for f in xlsx:(staged/f.name).unlink(missing_ok=True)
    profile=QA/'recalc-profile'
    cmd=[str(SOFFICE),f'-env:UserInstallation={profile.as_uri()}','--headless','--convert-to','xlsx','--outdir',str(staged),*[str(x) for x in xlsx]]
    result,details=run_office(cmd,timeout=180,env=os.environ.copy())
    if result:raise RuntimeError(details)
    for f in xlsx:
        target=staged/f.name
        if not target.exists():raise RuntimeError('Office-Rechnung fehlt: '+f.name)
        shutil.copyfile(target,f)
        xlsx_print_settings(f)
    (QA/'native-recalc.json').write_text(json.dumps({'engine':str(SOFFICE),'files':[p.name for p in xlsx],'exit':result,'log':details},ensure_ascii=False,indent=2),encoding='utf-8')

def receipts():
    a=load('northeim_author','build-bauwirtschaft-northeim-akte.py')
    attached=['02_bekanntmachung.pdf','03_vergabeunterlagen.docx','04_lv_lueftung.xlsx','06_bieterfrage.eml','07_bieterantwort.eml','08_angebot_leinetal.xlsx','09_eignung_leinetal.pdf','15_portal_bieter.png','18_nachforderung_aufklaerung.docx','19_antwort.docx','20_referenz.pdf','21_geraet.pdf','25_information_leinetal.pdf','27_ruege.eml','28_nichtabhilfe.docx']
    files=['29_nachpruefungsantrag.docx']+attached
    hashes=[f'{n}\nSHA-256: {hashlib.sha256((CASE/n).read_bytes()).hexdigest()}' for n in files]
    a.pdf('30_uebermittlungsbeleg.pdf','Elektronischer Rechtsverkehr | Versandjournal','Übermittlungs- und Eingangsbestätigung','24.09.2026',[[
        ('1 Nachricht','Nachrichtenkennung LT-NO26-NP01. Absender: Leinetal Lufttechnik GmbH, Organisationspostfach, handelnd Lena Winter. Empfänger: Vergabekammer Niedersachsen, besonderes elektronisches Behördenpostfach, Verzeichnisname Vergabekammer Lüneburg. Betreff: Nachprüfungsantrag NO-FH26-L430. Die Datei 29_nachpruefungsantrag.docx enthält die Erklärung der Geschäftsführerin. Fünfzehn weitere Dateien sind als Anlagen beigefügt.'),
        ('2 Zeit- und Transportdaten','Versand gestartet am 24.09.2026 um 11:23:51 Uhr MESZ. Nachricht auf der für den Empfang bestimmten Einrichtung gespeichert am 24.09.2026 um 11:24:08 Uhr MESZ. Empfangsbestätigung abgerufen am 24.09.2026 um 11:24:12 Uhr MESZ. Transportstatus: erfolgreich. Alle 16 Dateien wurden übernommen. Diese Bestätigung belegt die technische Übermittlung; sie trifft keine Entscheidung über den Antrag.'),
        ('3 Dateiverzeichnis und Prüfsummen','Das nachfolgende Verzeichnis gehört zu dieser einen Nachricht. Die Prüfsummen beziehen sich auf die unveränderten übermittelten Dateien, nicht auf spätere Druckfassungen.')],
        [('3.1 Dateiverzeichnis', '\n\n'.join(hashes[:8]))],
        [('3.2 Dateiverzeichnis', '\n\n'.join(hashes[8:]))]])
    rows=[
      ['NO26-BM01','27.07.2026 09:00:00','Bekanntmachung','abgesendet','02'],
      ['NO26-BM01','29.07.2026 08:00:00','Bekanntmachung','veröffentlicht','02'],
      ['NO26-F006','12.08.2026 10:18:00','Bieterfrage Leinetal','eingegangen','06'],
      ['NO26-F007','14.08.2026 14:00:00','Antwort an alle','bereitgestellt und versandt','07'],
      ['NO26-E002','31.08.2026 09:31:40','Angebot Weserklima','gespeichert','10 / 11'],
      ['NO26-E003','31.08.2026 09:48:05','Angebot Harzraum','gespeichert','12 / 13'],
      ['NO26-E001','31.08.2026 09:54:12','Angebot Leinetal','gespeichert','08 / 09'],
      ['NO26-N018','02.09.2026 09:00:00','Nachforderung an Leinetal','abgesendet','18'],
      ['NO26-N018','02.09.2026 09:00:03','Nachforderung an Leinetal','Postfachzustellung','18'],
      ['NO26-A019','09.09.2026 11:41:02','Antwort Leinetal','gespeichert','19 / 20 / 21'],
      ['NO26-I025','14.09.2026 15:00:00','Information Leinetal','elektronisch abgesendet','25'],
      ['NO26-I026','14.09.2026 15:00:00','Information Harzraum','elektronisch abgesendet','26'],
      ['NO26-I025','14.09.2026 15:00:03','Information Leinetal','Postfachzustellung','25'],
      ['NO26-I026','14.09.2026 15:00:04','Information Harzraum','Postfachzustellung','26'],
      ['NO26-R027','16.09.2026 09:20:04','Rüge Leinetal','SMTP angenommen','27'],
      ['NO26-S028','18.09.2026 11:00:00','Nichtabhilfe an Leinetal','versandt und zugestellt','28'],
      ['LT-NO26-NP01','24.09.2026 11:24:08','Nachprüfungsantrag','Empfangseinrichtung gespeichert','29 / 30'],
      ['VK26-OUT031','25.09.2026 09:10:05','Mitteilung an Stadt','Behördenpostfachzustellung','31'],
      ['VK26-OUT031','25.09.2026 09:13:22','Mitteilung an Stadt','abgerufen','31'],
    ]
    with (CASE/'17_versandprotokoll.csv').open('w',encoding='utf-8-sig',newline='') as stream:
        w=csv.writer(stream);w.writerow(['Kennung','Zeit MESZ','Vorgang','Status','Dateinummer']);w.writerows(rows)

def packages():
    e=load('northeim_einzel','build-testakten-einzelpdf-zips.py')
    z=load('northeim_zip','build-testakten-release-zips.py')
    originals=sorted(p for p in CASE.iterdir() if p.name[:2].isdigit() and p.suffix in {'.docx','.pdf','.xlsx','.eml','.csv','.txt','.png'})
    assert len(originals)==32,len(originals)
    pdf_dir=QA/'einzelpdf';pdf_dir.mkdir(exist_ok=True)
    office=render_office_batch([p for p in originals if p.suffix in {'.docx','.xlsx'}])
    required=[p for p in originals if p.suffix in {'.docx','.xlsx'}]
    assert set(office)==set(required),'Native Office-Ausgabe unvollständig'
    writer=PdfWriter();manifest=[]
    archive=OUT/f'testakte-{SLUG}-einzelpdfs.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as zipf:
        e.write_pdf(zipf,NOTICE_FILENAME,NOTICE_BYTES)
        for p in originals:
            data=metadata(e.render_document_pdf(p,CASE,office),p.stem)
            target=pdf_dir/(p.stem+'.pdf');target.write_bytes(data)
            e.write_pdf(zipf,target.name,data)
            reader=PdfReader(io.BytesIO(data));count=len(reader.pages)
            start=len(writer.pages)+1;writer.append(reader,outline_item=p.name)
            manifest.append(dict(file=p.name,pages=count,start=start,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    writer.add_metadata({'/Author':'Klotzkette','/Title':'Vergabeakte Feuerwehrhaus Northeim Los 430','/Creator':'Klotzkette'})
    total_dir=CASE/'gesamt-pdf';total_dir.mkdir(exist_ok=True)
    total=total_dir/f'{SLUG}_gesamt.pdf'
    with total.open('wb') as stream:writer.write(stream)
    shutil.copyfile(total,OUT/total.name)
    archive,count=z.build_single(CASE,OUT)
    (QA/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'originale':len(originals),'gesamtseiten':len(writer.pages),'originalzip_dateien':count,'originalzip':str(archive)},ensure_ascii=False))

def previews():
    if not POPPLER:raise RuntimeError('Vorschau benötigt pdftoppm oder AKTEN_PDFTOPPM.')
    render=os.environ.get('AKTEN_DOCX_RENDERER')
    for f in sorted(CASE.glob('*.docx')):
        if not render:continue
        target=QA/'docx-render'/f.stem
        sha=hashlib.sha256(f.read_bytes()).hexdigest()
        marker=target/'source.sha256'
        if marker.exists() and marker.read_text()==sha:continue
        if target.exists():
            for old in target.glob('page-*.png'):old.unlink()
        subprocess.run([sys.executable,str(render),str(f),'--output_dir',str(target),'--emit_pdf','--width','1000','--height','1415'],check=True)
        marker.write_text(sha)
    for f in sorted((QA/'einzelpdf').glob('*.pdf')):
        target=QA/'pages'/f.stem;target.mkdir(parents=True,exist_ok=True)
        for old in target.glob('page-*.png'):old.unlink()
        subprocess.run([str(POPPLER),'-r','96','-png',str(f),str(target/'page')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    # Übersicht für die Seitenauswahl; Einzelbilder bleiben für die Vollansicht erhalten.
    images=sorted((QA/'pages').glob('*/*.png'))
    for n in range(0,len(images),12):
        sheet=Image.new('RGB',(1600,1740),'#e7e7e7');draw=ImageDraw.Draw(sheet)
        for j,file in enumerate(images[n:n+12]):
            image=Image.open(file);image.thumbnail((380,520));x=(j%4)*400+(400-image.width)//2;y=(j//4)*580+30
            sheet.paste(image,(x,y));draw.text(((j%4)*400+6,(j//4)*580+6),file.parent.name[:36]+' '+file.stem,fill='black')
        sheet.save(QA/f'contact-{n//12+1:02}.png')
    print(f'Gerenderte Einzelseiten: {len(images)}')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['recalc','receipts','packages','previews','all'],default='all',nargs='?');args=parser.parse_args()
    QA.mkdir(parents=True,exist_ok=True)
    for name,fn in [('recalc',recalc),('receipts',receipts),('packages',packages),('previews',previews)]:
        if args.stage in ('all',name):fn()
