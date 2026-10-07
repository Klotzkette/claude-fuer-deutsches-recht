#!/usr/bin/env python3
"""Gezielter Komponentenbuild: nur SI-native Kanzlei und ihre 24 Kurzfälle."""
from pathlib import Path
import sys,json,importlib.util,zipfile,hashlib,io
from testakte_disclaimer import NOTICE_BYTES
from prompt_profiles import PROMPT_SUFFIXES
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];PLUGIN=ROOT/'si-native-kanzlei'
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,ROOT/'scripts'/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

def main():
    dist=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'dist/si-native-kanzlei';dist.mkdir(parents=True,exist_ok=True)
    E=module('si_einzel','build-testakten-einzelpdf-zips.py');G=E.G;Z=module('si_original','build-testakten-release-zips.py')
    cases=json.loads((ROOT/'scripts/si-native-kanzlei-faelle.json').read_text());reports=[]
    for case in cases:
        folder=ROOT/'testakten'/case['slug'];out,count=E.build_single(folder,dist);assert count==10,(case['slug'],count)
        status,info=G.build_gesamt_pdf(folder);assert status=='ok',info
        native,n=Z.build_single(folder,dist)
        total=folder/'gesamt-pdf'/f'{folder.name}_gesamt.pdf'
        reports.append({'slug':folder.name,'originals':10,'individual_pdfs':count,'gesamt_pages':len(PdfReader(total).pages),'native_zip':native.name,'pdf_zip':out.name})
        print(folder.name,flush=True)
    def files():
        return [p for p in sorted(PLUGIN.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(PROMPT_SUFFIXES)]
    for portable in (False,True):
        target=dist/('si-native-kanzlei-portable.zip' if portable else 'si-native-kanzlei.zip')
        with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
            for p in files():
                name=p.relative_to(PLUGIN).as_posix();Z.write_file(z,p,('si-native-kanzlei/' if portable else '')+name)
    with zipfile.ZipFile(dist/'si-native-kanzlei-24-testakten.zip','w') as z:
        Z.write_bytes(z,NOTICE_BYTES,'README.txt')
        for c in cases:
            p=dist/f'testakte-{c["slug"]}.zip';Z.write_file(z,p,p.name)
    hashes=''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(dist.glob('*.zip')))
    (dist/'checksums-sha256.txt').write_text(hashes)
    (ROOT/'quality/si-native-kanzlei/pakete.json').write_text(json.dumps({'cases':reports,'original_files':240,'plugin_skills':16,'release_zip_count':len(list(dist.glob('*.zip')))},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'cases':24,'original_files':240,'zip_assets':len(list(dist.glob('*.zip')))}))
if __name__=='__main__':main()
