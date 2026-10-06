#!/usr/bin/env python3
"""Native Rechnung, vollständige Exporte und Seitenvorschau der vertieften Akte."""
from pathlib import Path
import argparse
import importlib.util
import hashlib
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

ROOT=Path(__file__).resolve().parents[1]
SLUG='bauwirtschaft-vergabeverfahren-feuerwehrhaus-northeim'
CASE=ROOT/'testakten'/SLUG
QA=Path('/tmp/bauwirtschaft-vertiefung-20261006/northeim')
OUT=QA.parent/'dist'
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
q=lambda n:f'{{{NS}}}{n}'
PROFILE={'Preisvergleich':('G',37,'12:12'),'Angebotswerte':('G',35,'5:5'),'Kostenaufklärung':('E',29,None),'Gerätewerte':('E',36,None),'Nachweisstand':('D',26,'5:5'),'Termine':('F',30,None),'Unterlagen':('E',28,'5:5')}

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/file)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def settings(file,invalidate=False):
    with zipfile.ZipFile(file) as z:items={i.filename:(i,z.read(i.filename)) for i in z.infolist()}
    wb=ET.fromstring(items['xl/workbook.xml'][1]);defs=wb.find(q('definedNames'))
    if defs is None:
        defs=ET.Element(q('definedNames'));calc=wb.find(q('calcPr'));wb.insert(list(wb).index(calc) if calc is not None else len(wb),defs)
    for old in list(defs):
        if old.get('name') in ('_xlnm.Print_Area','_xlnm.Print_Titles'):defs.remove(old)
    order='sheetPr dimension sheetViews sheetFormatPr cols sheetData sheetCalcPr sheetProtection protectedRanges scenarios autoFilter sortState dataConsolidate customSheetViews mergeCells phoneticPr conditionalFormatting dataValidations hyperlinks printOptions pageMargins pageSetup headerFooter rowBreaks colBreaks customProperties cellWatches ignoredErrors smartTags drawing legacyDrawing legacyDrawingHF picture oleObjects controls webPublishItems tableParts extLst'.split()
    def replace(node,name,new):
        for old in list(node):
            if old.tag==q(name):node.remove(old)
        index=next((i for i,e in enumerate(node) if e.tag.split('}')[-1] in order and order.index(e.tag.split('}')[-1])>order.index(name)),len(node));node.insert(index,new)
    for i,s in enumerate(wb.find(q('sheets'))):
        name=s.get('name');end,row,repeat=PROFILE[name]
        ET.SubElement(defs,q('definedName'),{'name':'_xlnm.Print_Area','localSheetId':str(i)}).text=f"'{name}'!$A$1:${end}${row}"
        if repeat:
            a,b=repeat.split(':');ET.SubElement(defs,q('definedName'),{'name':'_xlnm.Print_Titles','localSheetId':str(i)}).text=f"'{name}'!${a}:${b}"
        key=f'xl/worksheets/sheet{i+1}.xml';node=ET.fromstring(items[key][1])
        if invalidate:
            for c in node.iter(q('c')):
                if c.find(q('f')) is not None:
                    for child in list(c):
                        if child.tag in (q('v'),q('is')):c.remove(child)
                    c.attrib.pop('t',None)
        pr=node.find(q('sheetPr'))
        if pr is None:pr=ET.Element(q('sheetPr'));node.insert(0,pr)
        setup=pr.find(q('pageSetUpPr'))
        if setup is None:setup=ET.SubElement(pr,q('pageSetUpPr'))
        setup.set('fitToPage','1')
        replace(node,'pageMargins',ET.Element(q('pageMargins'),dict(left='0.3',right='0.3',top='0.35',bottom='0.35',header='0.1',footer='0.15')))
        replace(node,'pageSetup',ET.Element(q('pageSetup'),dict(paperSize='9',orientation='landscape',fitToWidth='1',fitToHeight='0')))
        footer=ET.Element(q('headerFooter'));ET.SubElement(footer,q('oddFooter')).text='&LNO-FH26-L430&C'+name+'&RSeite &P';replace(node,'headerFooter',footer)
        if name in ('Kostenaufklärung','Gerätewerte'):
            breaks=ET.Element(q('rowBreaks'),{'count':'1','manualBreakCount':'1'})
            ET.SubElement(breaks,q('brk'),{'id':str(17 if name=='Kostenaufklärung' else 15),'min':'0','max':'16383','man':'1'})
            replace(node,'rowBreaks',breaks)
        items[key]=(items[key][0],ET.tostring(node,encoding='utf-8',xml_declaration=True))
    calc=wb.find(q('calcPr'))
    if calc is None:calc=ET.SubElement(wb,q('calcPr'))
    calc.set('calcMode','auto');calc.set('fullCalcOnLoad','1')
    items['xl/workbook.xml']=(items['xl/workbook.xml'][0],ET.tostring(wb,encoding='utf-8',xml_declaration=True))
    core_key='docProps/core.xml'
    if core_key in items:
        core=ET.fromstring(items[core_key][1])
        for key in ['{http://purl.org/dc/elements/1.1/}creator','{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}lastModifiedBy']:
            node=core.find(key)
            if node is None:node=ET.SubElement(core,key)
            node.text='Klotzkette'
        items[core_key]=(items[core_key][0],ET.tostring(core,encoding='utf-8',xml_declaration=True))
    tmp=file.with_suffix('.xlsx.tmp')
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)as z:
        for info,data in items.values():z.writestr(info,data)
    tmp.replace(file)

def recalc():
    files=sorted(p for p in CASE.glob('*.xlsx') if int(p.name[:2])>=43)
    stage=QA/'recalc';stage.mkdir(parents=True,exist_ok=True)
    for p in files:settings(p,True);(stage/p.name).unlink(missing_ok=True)
    cmd=[office_binary(),f'-env:UserInstallation={(QA/"profile").as_uri()}','--headless','--convert-to','xlsx','--outdir',str(stage),*[str(p)for p in files]]
    code,log=run_office(cmd,timeout=180,env=os.environ.copy());assert code==0,log
    for p in files:
        assert(stage/p.name).exists(),p.name
        shutil.copyfile(stage/p.name,p);settings(p)
    (QA/'native-recalc.json').write_text(json.dumps({'engine':office_binary(),'files':[p.name for p in files],'log':log},ensure_ascii=False,indent=2))
    print('Drei neue Arbeitsmappen nativ neu berechnet.')

def packages():
    e=load('northeim_single','build-testakten-einzelpdf-zips.py');z=load('northeim_zip','build-testakten-release-zips.py')
    originals=sorted(p for p in CASE.iterdir() if p.name[:2].isdigit())
    assert len(originals)==45,len(originals)
    office=render_office_batch([p for p in originals if p.suffix in ('.docx','.xlsx')]);assert len(office)==22,len(office)
    pd=QA/'einzelpdf';pd.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
    total=PdfWriter();manifest=[]
    with zipfile.ZipFile(OUT/f'testakte-{SLUG}-einzelpdfs.zip','w',zipfile.ZIP_DEFLATED)as zipf:
        e.write_pdf(zipf,NOTICE_FILENAME,NOTICE_BYTES)
        for p in originals:
            data=e.render_document_pdf(p,CASE,office);reader=PdfReader(io.BytesIO(data));writer=PdfWriter();writer.append(reader);writer.add_metadata({'/Author':'Klotzkette','/Title':p.stem,'/Creator':'Klotzkette'});buf=io.BytesIO();writer.write(buf);data=buf.getvalue()
            (pd/(p.stem+'.pdf')).write_bytes(data);e.write_pdf(zipf,p.stem+'.pdf',data)
            manifest.append({'file':p.name,'pages':len(reader.pages),'start':len(total.pages)+1,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()});total.append(PdfReader(io.BytesIO(data)),outline_item=p.name)
    total.add_metadata({'/Author':'Klotzkette','/Title':'Vergabeakte Feuerwehrhaus Northeim Los 430','/Creator':'Klotzkette'})
    final=CASE/'gesamt-pdf'/f'{SLUG}_gesamt.pdf';total.write(final);shutil.copyfile(final,OUT/final.name);archive,count=z.build_single(CASE,OUT)
    (QA/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print(json.dumps({'originale':45,'seiten':len(total.pages),'originalzip_dateien':count,'einzelpdfzip_dateien':46},ensure_ascii=False))

def previews():
    renderer=os.environ.get('AKTEN_DOCX_RENDERER');assert renderer,'AKTEN_DOCX_RENDERER setzen.'
    for f in sorted(p for p in CASE.glob('*.docx')if int(p.name[:2])>=33):
        target=QA/'docx-render'/f.stem
        subprocess.run([sys.executable,renderer,str(f),'--output_dir',str(target),'--emit_pdf','--width','1100','--height','1556'],check=True)
    poppler=os.environ.get('AKTEN_PDFTOPPM') or shutil.which('pdftoppm');assert poppler
    for f in sorted((QA/'einzelpdf').glob('*.pdf')):
        if int(f.name[:2])<33:continue
        target=QA/'pages'/f.stem;target.mkdir(parents=True,exist_ok=True)
        for old in target.glob('page-*.png'):old.unlink()
        subprocess.run([poppler,'-r','105','-png',str(f),str(target/'page')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    images=sorted((QA/'pages').glob('*/*.png'))
    for n in range(0,len(images),8):
        canvas=Image.new('RGB',(1800,1500),'#e7e7e7');draw=ImageDraw.Draw(canvas)
        for j,f in enumerate(images[n:n+8]):
            im=Image.open(f);im.thumbnail((440,700));x=(j%4)*450+(450-im.width)//2;y=(j//4)*750+30;canvas.paste(im,(x,y));draw.text(((j%4)*450+4,(j//4)*750+7),f.parent.name[:38]+' '+f.stem,fill='black')
        canvas.save(QA/f'contact-{n//8+1:02}.png')
    print(f'{len(images)} neue PDF-Seiten als Einzelbilder erzeugt.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['recalc','packages','previews','all']);args=parser.parse_args();QA.mkdir(parents=True,exist_ok=True)
    for name,fn in [('recalc',recalc),('packages',packages),('previews',previews)]:
        if args.stage in (name,'all'):fn()
