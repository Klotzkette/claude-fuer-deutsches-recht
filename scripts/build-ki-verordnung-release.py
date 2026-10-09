#!/usr/bin/env python3
"""Baut die KI-Verordnungs-Fachrunde aus dokumentiertem Scope und geprüften Quellen."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,shutil,zipfile
from pathlib import Path
from prompt_profiles import PROMPT_SUFFIXES
ROOT=Path(__file__).resolve().parents[1]
SCOPE=ROOT/'scripts/data/ki-verordnung-release-scope.json'
SPECIALISTS=('ki-verordnung-verbotene-praktiken','ki-verordnung-hochrisiko-pruefer','ki-verordnung-register-meldungen','ki-verordnung-konformitaet')

def module(filename):
    spec=importlib.util.spec_from_file_location(filename.replace('-','_'),ROOT/'scripts'/filename)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

def sources(directory):
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():raise ValueError(f'Symlink nicht paketierbar: {path}')
        if not path.is_file() or '__pycache__' in path.parts or path.suffix=='.pyc' or path.name in {'.DS_Store','CLAUDE.md'} or path.name.endswith(PROMPT_SUFFIXES):continue
        yield path

def plugin_directory(slug):
    marketplace=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
    found=[p for p in marketplace['plugins'] if p['name']==slug]
    if len(found)!=1:raise ValueError(f'Plugin nicht eindeutig: {slug}')
    directory=(ROOT/found[0]['source']).resolve()
    if not directory.is_relative_to(ROOT):raise ValueError('Plugin außerhalb Repository')
    return directory

def build(destination):
    destination.mkdir(parents=True,exist_ok=True)
    if any(destination.iterdir()):raise ValueError('Leeres Ausgabeziel erforderlich')
    scope=json.loads(SCOPE.read_text());version=scope['version'];expected=set()
    def copy(path):
        if not path.is_file() or not path.stat().st_size:raise ValueError(f'Fehlende Quelle {path}')
        if path.name in expected:raise ValueError(f'Doppelter Assetname {path.name}')
        shutil.copyfile(path,destination/path.name);expected.add(path.name)
    for slug in scope['plugins']:
        directory=plugin_directory(slug)
        manifest=json.loads((directory/'.claude-plugin/plugin.json').read_text())
        if manifest['version']!=version:raise ValueError(f'{slug}: Versionsabweichung')
        name=slug+'.zip';expected.add(name)
        with zipfile.ZipFile(destination/name,'w',zipfile.ZIP_DEFLATED) as archive:
            for path in sources(directory):
                item=zipfile.ZipInfo(path.relative_to(directory).as_posix(),(2026,10,9,0,0,0));item.compress_type=zipfile.ZIP_DEFLATED;item.external_attr=0o100644<<16
                archive.writestr(item,path.read_bytes())
        for kind in ('werkstatt','schnellstart','hauptproblem'):
            for suffix in ('md','txt'):
                path=directory/f'{slug}-{kind}.{suffix}'
                if path.exists():copy(path)
    originals=module('build-testakten-release-zips.py');pdfs=module('build-testakten-einzelpdf-zips.py')
    for case in scope['cases']:
        directory=ROOT/'testakten'/case
        originals.build_single(directory,destination);pdfs.build_single(directory,destination)
        expected.update({f'testakte-{case}.zip',f'testakte-{case}-einzelpdfs.zip'})
        copy(directory/'gesamt-pdf'/f'{case}_gesamt.pdf')
    for slug in SPECIALISTS:
        for suffix in ('skills-handbuch','werkstatt-lesefassung'):copy(ROOT/'docs/handbuecher'/f'{slug}-{suffix}.pdf')
    copy(SCOPE)
    actual={p.name for p in destination.iterdir()}
    if actual!=expected:raise ValueError(f'Unerwartete Assets: {actual^expected}')
    checksums=''.join(f'{hashlib.sha256((destination/name).read_bytes()).hexdigest()}  {name}\n' for name in sorted(expected))
    (destination/'checksums-sha256.txt').write_text(checksums)
    print(json.dumps({'version':version,'plugins':len(scope['plugins']),'cases':len(scope['cases']),'assets':len(expected)+1},ensure_ascii=False))
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('destination',type=Path);build(parser.parse_args().destination.resolve())
