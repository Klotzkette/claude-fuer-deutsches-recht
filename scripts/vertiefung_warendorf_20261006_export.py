#!/usr/bin/env python3
"""Warendorf gezielt mit zentralen Exportern bauen, ohne andere Akten anzufassen."""
from pathlib import Path
import importlib.util,sys,subprocess,os,zipfile,json,io,hashlib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
CASE=ROOT/'testakten/bauwirtschaft-baumanagement-werkhalle-warendorf'
QA=Path('/tmp/bauwirtschaft-vertiefung-20261006/warendorf')
DIST=Path('/tmp/bauwirtschaft-vertiefung-20261006/dist')
os.environ['SOFFICE']='/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/soffice'
POPPLER='/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'

def load(name):
    spec=importlib.util.spec_from_file_location(name.replace('-','_'),ROOT/'scripts'/f'{name}.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    DIST.mkdir(parents=True,exist_ok=True);QA.mkdir(parents=True,exist_ok=True)
    subprocess.run([sys.executable,str(ROOT/'scripts/build-testakte-gesamt-pdf.py'),CASE.name],check=True)
    original=load('build-testakten-release-zips');pdfs=load('build-testakten-einzelpdf-zips')
    first,n=original.build_single(CASE,DIST);second,m=pdfs.build_single(CASE,DIST)
    # Zentralen Einzelarchiv-Validator nutzen; die Sammelarchive gehören dem Root-Release.
    ov=load('validate-testakten-release-zips');pv=load('validate-testakten-einzelpdf-zips')
    a=ov.zip_entries(first,require_notice=True,allow_directories=False)
    ov.assert_same(first.name,ov.expected_entries(CASE),a)
    expected=[pv.NOTICE_FILENAME,*[arc for _,arc in pdfs.document_arcname_pairs(CASE)]]
    b=pv.zip_entries(second,expected_suffix='.pdf',allow_directories=False)
    pv.assert_same(second.name,expected,b)
    pages={};final=QA/'final-pdf';final.mkdir(exist_ok=True)
    with zipfile.ZipFile(second) as z:
        for name in z.namelist():
            if name[:2].isdigit() and int(name[:2])>=31 and name.endswith('.pdf'):
                p=final/name;p.write_bytes(z.read(name));pages[name]=len(PdfReader(p).pages)
                for old in final.glob(p.stem+'-*.png'):old.unlink()
                subprocess.run([POPPLER,'-r','105','-png',str(p),str(final/p.stem)],check=True,capture_output=True)
    total=CASE/'gesamt-pdf'/f'{CASE.name}_gesamt.pdf'
    subprocess.run([POPPLER,'-f','1','-l','2','-r','105','-png',str(total),str(final/'gesamt-titel')],check=True,capture_output=True)
    summary={'Originaldateien':43,'Exceldateien':5,'Neue_Belege':10,'Neue_Arbeitsmappen':3,'Neue_PDF_Seiten':pages,'Gesamt_PDF_Seiten':len(PdfReader(total).pages),'Originalformat_ZIP_Eintraege':n,'Einzel_PDF_Anzahl':m,'ZIP_SHA256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [first,second]}}
    (QA/'exportbericht.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
