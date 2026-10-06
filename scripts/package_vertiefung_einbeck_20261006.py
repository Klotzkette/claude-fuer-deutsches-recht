#!/usr/bin/env python3
"""Fallbezogene Nutzung der zentralen Paketfunktionen, ohne Sammelarchivänderungen."""
from pathlib import Path
import importlib.util,os,json,zipfile,subprocess,shutil
from pypdf import PdfReader
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;SLUG='bauwirtschaft-hoai-buergerhaus-einbeck'
CASE=ROOT/'testakten'/SLUG;QA=Path(os.environ.get('EINBECK_VERTIEFUNG_QA','/tmp/bauwirtschaft-vertiefung-20261006/einbeck'))
DIST=Path(os.environ.get('EINBECK_VERTIEFUNG_DIST','/tmp/bauwirtschaft-vertiefung-20261006/dist'))
def mod(name,file):
    sp=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def main():
    assert 'codex-primary-runtime/dependencies/bin/override/soffice' in os.environ['SOFFICE']
    DIST.mkdir(parents=True,exist_ok=True)
    g=mod('einbeck_gesamt_erg','build-testakte-gesamt-pdf.py');e=mod('einbeck_einzel_erg','build-testakten-einzelpdf-zips.py');z=mod('einbeck_zip_erg','build-testakten-release-zips.py')
    status,info=g.build_gesamt_pdf(CASE);assert status=='ok',info;print(info,flush=True)
    out,count=e.build_single(CASE,DIST);assert count==55,count;print(out,flush=True)
    native,n=z.build_single(CASE,DIST);assert n==57,n;print(native,flush=True)
    total=CASE/'gesamt-pdf'/f'{SLUG}_gesamt.pdf';shutil.copyfile(total,DIST/total.name)
    singles=QA/'einzel-pdf';singles.mkdir(exist_ok=True);rows=[]
    with zipfile.ZipFile(out) as arc:
        for name in arc.namelist():
            if not name.endswith('.pdf'):continue
            path=singles/name;path.write_bytes(arc.read(name));pages=len(PdfReader(path).pages);rows.append({'file':name,'pages':pages})
            if int(name[:2])>=45:
                target=QA/f'pdf-{name[:2]}';target.mkdir(exist_ok=True)
                for old in target.glob('page-*.png'):old.unlink()
                subprocess.run(['pdftoppm','-png','-r','110',str(path),str(target/'page')],check=True,capture_output=True)
    (QA/'paketindex.json').write_text(json.dumps({'originals':55,'individuals':rows,'gesamt_pages':len(PdfReader(total).pages)},ensure_ascii=False,indent=2))
    print(json.dumps({'native_files':n,'individuals':count,'total_pages':len(PdfReader(total).pages)}))
if __name__=='__main__':main()
