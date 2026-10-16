#!/usr/bin/env python3
"""Reproduzierbares Komponentenrelease zu EuGH C-70/25 mit sieben Plugins."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, shutil, subprocess, sys, zipfile
from pathlib import Path
from pypdf import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate
from prompt_profiles import PROMPT_SUFFIXES, standalone_kinds

ROOT=Path(__file__).resolve().parents[1]
VERSION='445.35.4'
TAG=f'phishing-v{VERSION}'
PLUGINS=('phishing-vorfall-pruefer','bank-rechtsabteilung','fachanwalt-bank-kapitalmarktrecht','bgb-bt-pruefer','agb-werkstatt','betreuungsrecht','commercial-courts-deutschland')
CASE='phishing-kleinanzeigen-rabenstein-halle'
CASE_ASSETS=(f'testakte-{CASE}.zip',f'testakte-{CASE}-einzelpdfs.zip',f'{CASE}_gesamt.pdf')
SKIP_PARTS={'__pycache__','.git','.venv','node_modules','testakte','testakten'}

def module(filename):
    spec=importlib.util.spec_from_file_location(filename.replace('-','_'),ROOT/'scripts'/filename)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

def prompts():
    paths=[]
    for name in PLUGINS:
        for kind in tuple(dict.fromkeys((*standalone_kinds(name), 'hauptproblem'))):
            source=ROOT/name/f'{name}-{kind}.md'
            if source.is_file():paths.append(source)
    paths.extend(ROOT/'betreuungsrecht'/f'betreuungsrecht-unterlagen-werkstatt.{ext}' for ext in ('md','txt'))
    return paths

def asset_names():
    return {f'{n}{s}.zip' for n in PLUGINS for s in ('','-portable')} | {p.name for p in prompts()} | set(CASE_ASSETS) | {'phishing-vorfall-pruefer-werkstatt.pdf','phishing-vorfall-pruefer-schnellstart.pdf','quellenabgleich.json','checksums-sha256.txt'}

def sources(name):
    directory=ROOT/name;result={}
    for p in sorted(directory.rglob('*')):
        rel=p.relative_to(directory)
        if SKIP_PARTS.intersection(rel.parts) or p.name in {'.DS_Store','CLAUDE.md'} or p.suffix=='.pyc' or p.name.endswith(PROMPT_SUFFIXES):continue
        if p.is_symlink():raise ValueError(f'Symlink nicht zulässig: {p}')
        if p.is_file():result[rel.as_posix()]=p
    for n in ('LICENSE','LICENSE-APACHE','LICENSE-MIT','NOTICE'):
        if n not in result and (ROOT/n).is_file():result[n]=ROOT/n
    return result

def render_prompt(source,target):
    render=module('build-testakte-gesamt-pdf.py')
    directory=Path('/System/Library/Fonts/Supplemental');fonts=('Times New Roman.ttf','Times New Roman Bold.ttf');label='Times New Roman'
    if not all((directory/f).is_file() for f in fonts):
        directory=Path('/usr/share/fonts/truetype/liberation2');fonts=('LiberationSerif-Regular.ttf','LiberationSerif-Bold.ttf');label='Liberation Serif (Ersatz für Times New Roman)'
    for n,f in zip(('Phishing-Regular','Phishing-Bold'),fonts):pdfmetrics.registerFont(TTFont(n,str(directory/f)))
    pdfmetrics.registerFontFamily('Phishing-Regular',normal='Phishing-Regular',bold='Phishing-Bold',italic='Phishing-Regular',boldItalic='Phishing-Bold')
    render.FONT_REG,render.FONT_BOLD='Phishing-Regular','Phishing-Bold'
    for style in (render.s_body,render.s_meta):style.fontName,style.fontSize,style.leading='Phishing-Regular',11,14.3
    for style in (render.s_h1,render.s_h2,render.s_h3):style.fontName='Phishing-Bold';style.keepWithNext=True
    markdown=re.sub(r'\[([^\]]+)\]\((https?://[^ )]+)\)',r'\1 (\2)',source.read_text())
    def footer(canvas,document):
        canvas.setFont('Phishing-Regular',8);canvas.drawString(55,27,f'Phishing-Vorfall-Prüfer {VERSION} | {label} 11 pt');canvas.drawRightString(A4[0]-55,27,str(document.page))
    doc=SimpleDocTemplate(str(target),pagesize=A4,leftMargin=55,rightMargin=55,topMargin=50,bottomMargin=50,invariant=1,title=source.stem,author='Klotzkette',subject=f'{label} 11 pt')
    doc.build(render.md_to_flowables(markdown),onFirstPage=footer,onLaterPages=footer)
    count=len(PdfReader(target).pages)
    if not count:raise ValueError(f'Leere Lesefassung: {target}')
    return {'source':source.relative_to(ROOT).as_posix(),'font':label,'pages':count}

def build(dist,case_assets=None):
    dist.mkdir(parents=True,exist_ok=True)
    if any(dist.iterdir()):raise ValueError('Ausgabeziel muss leer sein.')
    checks=module('validate-release-zips.py');report={'schema_version':1,'tag':TAG,'plugins':{},'prompts':{},'pdfs':{}}
    for name in PLUGINS:
        files=sources(name)
        for rel in ('plugin.json','.claude-plugin/plugin.json','.codex-plugin/plugin.json'):
            if rel in files and json.loads(files[rel].read_text()).get('version')!=VERSION:raise ValueError(f'Manifestversion weicht ab: {name}/{rel}')
        for portable in (False,True):
            target=dist/f'{name}{"-portable" if portable else ""}.zip';prefix=f'{name}/' if portable else ''
            with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED) as archive:
                for rel,p in files.items():
                    info=zipfile.ZipInfo(prefix+rel,(2026,10,16,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;archive.writestr(info,p.read_bytes())
            with zipfile.ZipFile(target) as archive:
                if set(archive.namelist())!={prefix+n for n in files}:raise ValueError('Dateiliste im ZIP weicht ab.')
                for n,p in files.items():
                    if archive.read(prefix+n)!=p.read_bytes():raise ValueError(f'Quellenabweichung {name}/{n}')
        checks.validate_plugin_zip(dist,name,VERSION);checks.validate_skill_sources(dist/f'{name}.zip',ROOT/name);checks.validate_focus_skill(dist/f'{name}.zip',ROOT/name,ROOT/'quality/evals'/f'{name}.json')
        report['plugins'][name]={'version':VERSION,'files':{n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in files.items()}}
    for source in prompts():
        shutil.copyfile(source,dist/source.name);report['prompts'][source.name]=hashlib.sha256(source.read_bytes()).hexdigest()
        if source.name.endswith(('-schnellstart.md','-hauptproblem.md')) and len(source.read_bytes())>7500:raise ValueError(f'Kompaktprompt zu lang: {source}')
    for kind in ('werkstatt','schnellstart'):
        source=ROOT/'phishing-vorfall-pruefer'/f'phishing-vorfall-pruefer-{kind}.md';report['pdfs'][source.with_suffix('.pdf').name]=render_prompt(source,dist/source.with_suffix('.pdf').name)
    if case_assets:
        record=json.loads((ROOT/'quality/phishing-vorfall-pruefer/testakte-pruefung.json').read_text())
        expected={p['file']:p['sha256'] for p in record['packages']['artifacts']}
        for n in CASE_ASSETS:
            source=case_assets/n
            if hashlib.sha256(source.read_bytes()).hexdigest()!=expected[n]:raise ValueError(f'Ungeprüftes Aktenpaket: {n}')
            shutil.copyfile(source,dist/n)
    else:
        subprocess.run([sys.executable,str(ROOT/'scripts/build-phishing-testakte-pakete.py'),'--dist',str(dist),'--individual-dir',str(dist.parent/'phishing-einzelpdfs')],check=True)
    (dist/'quellenabgleich.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (dist/'checksums-sha256.txt').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(dist.iterdir())))
    if {p.name for p in dist.iterdir()}!=asset_names():raise ValueError('Assetliste stimmt nicht.')
    print(json.dumps({'tag':TAG,'assets':len(asset_names()),'dist':str(dist),'pdfs':report['pdfs']},ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--dist',type=Path,required=True);p.add_argument('--case-assets',type=Path);a=p.parse_args();build(a.dist.resolve(),a.case_assets.resolve() if a.case_assets else None)
