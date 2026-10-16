#!/usr/bin/env python3
"""Prüft Quellenidentität, Promptgrenzen und den veröffentlichten Aktenumfang."""
import argparse, hashlib, importlib.util, json, re, subprocess, sys, zipfile
from pathlib import Path
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def check(dist=None):
    build=module('build-phishing-release');market=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text());entries={e['name']:e for e in market['plugins']}
    for name in build.PLUGINS:
        assert entries[name]['version']==build.VERSION,name
        profile=json.loads((ROOT/'quality/evals'/f'{name}.json').read_text())
        for kind,key in (('schnellstart','mini_review'),('werkstatt','workshop_review')):
            path=ROOT/name/f'{name}-{kind}.md'
            if path.exists():assert profile[key]['sha256']==hashlib.sha256(path.read_bytes()).hexdigest(),str(path)
    for path in build.prompts():
        if path.name.endswith(('-schnellstart.md','-hauptproblem.md')):
            data=path.read_bytes();assert len(data.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'))<=7500,path.name
    p=ROOT/'betreuungsrecht/betreuungsrecht-unterlagen-werkstatt.md';assert p.read_bytes()==p.with_suffix('.txt').read_bytes()
    subprocess.run([sys.executable,str(ROOT/'scripts/test-phishing-tukowiecka.py')],check=True)
    if dist:
        assert {p.name for p in dist.iterdir()}==build.asset_names(),'Assetliste'
        expected={}
        for line in (dist/'checksums-sha256.txt').read_text().splitlines():
            digest,name=line.split('  ',1);assert name not in expected;expected[name]=digest
            assert hashlib.sha256((dist/name).read_bytes()).hexdigest()==digest,name
        assert set(expected)==build.asset_names()-{'checksums-sha256.txt'}
        for name in build.PLUGINS:
            files=build.sources(name)
            for portable in (False,True):
                prefix=f'{name}/' if portable else ''
                with zipfile.ZipFile(dist/f'{name}{"-portable" if portable else ""}.zip') as archive:
                    assert len(archive.namelist())==len(files)
                    assert set(archive.namelist())=={prefix+n for n in files}
                    for n,p in files.items():assert archive.read(prefix+n)==p.read_bytes(),f'{name}/{n}'
        for p in build.prompts():assert (dist/p.name).read_bytes()==p.read_bytes(),p.name
        case=ROOT/'testakten'/build.CASE
        from testakte_einzelpdf_common import document_arcname_pairs
        from testakte_disclaimer import NOTICE_BYTES
        pairs=document_arcname_pairs(case);assert len(pairs)==28
        with zipfile.ZipFile(dist/build.CASE_ASSETS[0]) as original,zipfile.ZipFile(dist/build.CASE_ASSETS[1]) as individual:
            assert original.read('README.txt').startswith(NOTICE_BYTES)
            assert individual.read('README.txt').startswith(NOTICE_BYTES)
            assert len([n for n in individual.namelist() if n.endswith('.pdf')])==28
            total=0
            import io
            aggregate=PdfReader(dist/build.CASE_ASSETS[2])
            for source,pdfname in pairs:
                assert original.read(source.name)==source.read_bytes()
                for page in PdfReader(io.BytesIO(individual.read(pdfname))).pages:
                    assert page.extract_text()==aggregate.pages[total].extract_text();total+=1
            record=json.loads((ROOT/'quality/phishing-vorfall-pruefer/testakte-pruefung.json').read_text())
            assert total==len(aggregate.pages)==record['packages']['aggregate_pages']
            assert original.read(build.CASE_ASSETS[2])==(dist/build.CASE_ASSETS[2]).read_bytes()
        for name in ('phishing-vorfall-pruefer-werkstatt.pdf','phishing-vorfall-pruefer-schnellstart.pdf'):
            text='\n'.join(p.extract_text() or '' for p in PdfReader(dist/name).pages)
            assert 'C-70/25' in text and 'Tukowiecka' in text and '675u' in text,name
    print('Phishing: Quellen, sieben Komponenten, Promptgrenzen und '+('Releasepakete' if dist else 'Regressionen')+' geprüft.')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--dist',type=Path);a=p.parse_args();check(a.dist.resolve() if a.dist else None)
