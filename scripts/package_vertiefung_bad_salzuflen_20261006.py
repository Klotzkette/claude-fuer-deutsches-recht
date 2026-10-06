#!/usr/bin/env python3
"""Vier neue Mappen und ergänzende Belege mit zentralen Exportern verpacken."""
from pathlib import Path
import importlib.util,os,json,zipfile,subprocess,shutil
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
SLUG='bauwirtschaft-buchhaltung-bauunternehmen-bad-salzuflen'
CASE=ROOT/'testakten'/SLUG
QA=Path('/tmp/bauwirtschaft-vertiefung-20261006/bad')
DIST=QA.parent/'dist'
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,ROOT/'scripts'/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def main():
    assert 'codex-primary-runtime/dependencies/bin/override/soffice'in os.environ['SOFFICE']
    DIST.mkdir(exist_ok=True)
    g=module('bad_gesamt','build-testakte-gesamt-pdf.py');e=module('bad_einzel','build-testakten-einzelpdf-zips.py');z=module('bad_zip','build-testakten-release-zips.py')
    status,info=g.build_gesamt_pdf(CASE);assert status=='ok',info;print(info,flush=True)
    singles,count=e.build_single(CASE,DIST);assert count==75,count
    native,n=z.build_single(CASE,DIST);assert n==77,n
    total=CASE/'gesamt-pdf'/f'{SLUG}_gesamt.pdf';shutil.copyfile(total,DIST/total.name)
    dest=QA/'einzel-pdf';dest.mkdir(exist_ok=True);rows=[]
    with zipfile.ZipFile(singles)as arc:
        for name in arc.namelist():
            if not name.endswith('.pdf'):continue
            p=dest/name;p.write_bytes(arc.read(name))
            rows.append(dict(file=name,pages=len(PdfReader(p).pages)))
            if int(name[:2])>=58:
                target=QA/f'pdf-{name[:2]}';target.mkdir(exist_ok=True)
                for old in target.glob('page-*.png'):old.unlink()
                subprocess.run(['pdftoppm','-png','-r','105',str(p),str(target/'page')],check=True,capture_output=True)
    (QA/'paketindex.json').write_text(json.dumps({'originals':75,'individuals':rows,'gesamt_pages':len(PdfReader(total).pages)},ensure_ascii=False,indent=2))
    print(f'{count} Einzel-PDFs, {n} Original-ZIP-Einträge, {len(PdfReader(total).pages)} Gesamtseiten.')
if __name__=='__main__':main()
