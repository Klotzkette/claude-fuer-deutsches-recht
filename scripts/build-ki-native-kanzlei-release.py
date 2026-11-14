#!/usr/bin/env python3
"""Komponentenrelease nur für die vertiefte KI-native Kanzlei.

Bereits veröffentlichte SI-Fallakten bleiben unter ihren unveränderten URLs.
PDF-Lesefassungen werden getrennt vom installierbaren Plugin ausgeliefert.
"""
import argparse,hashlib,json,zipfile
from pathlib import Path
from ki_kanzlei_release_contract import (VERSION, ACTIVE_SKILL_COUNT, ACTIVE_SKILL_SLUGS, MODULE_COUNT, validate_module_report)
from prompt_profiles import PROMPT_SUFFIXES
ROOT=Path(__file__).resolve().parents[1];PLUGIN=ROOT/'ki-native-kanzlei'

def put(z,data,name):
    info=zipfile.ZipInfo(name,date_time=(2026,10,7,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,data)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--dist',required=True,type=Path);ap.add_argument('--pdf-dir',required=True,type=Path);args=ap.parse_args();args.dist.mkdir(parents=True,exist_ok=True)
    if list(args.dist.iterdir()):raise SystemExit('Dist-Ziel muss leer sein; vorhandene Veröffentlichung nicht überschreiben.')
    sources=[p for p in sorted(PLUGIN.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(PROMPT_SUFFIXES)]
    assert {p.parent.name for p in (PLUGIN/'skills').glob('*/SKILL.md')}==ACTIVE_SKILL_SLUGS
    for portable in (False,True):
        name='ki-native-kanzlei-portable.zip' if portable else 'ki-native-kanzlei.zip';prefix='ki-native-kanzlei/' if portable else ''
        with zipfile.ZipFile(args.dist/name,'w') as z:
            for p in sources:put(z,p.read_bytes(),prefix+p.relative_to(PLUGIN).as_posix())
    report=json.loads((args.pdf_dir/'umfang.json').read_text());rows=validate_module_report(report)
    for r in rows:
        src=ROOT/r['source'];assert hashlib.sha256(src.read_bytes()).hexdigest()==r['source_sha256'],'PDF-Quelle veraltet: '+r['skill']
        assert hashlib.sha256((args.pdf_dir/r['pdf']).read_bytes()).hexdigest()==r['pdf_sha256']
    hand=args.pdf_dir/'ki-native-kanzlei-skills-handbuch.pdf';assert hashlib.sha256(hand.read_bytes()).hexdigest()==report['handbook_sha256'];(args.dist/hand.name).write_bytes(hand.read_bytes())
    with zipfile.ZipFile(args.dist/'ki-native-kanzlei-skills-einzelpdfs.zip','w') as z:
        put(z,f'KI-native Kanzlei\n{MODULE_COUNT} vollständige Fachmodule als A4-PDFs; Fachstand 09.10.2026.\nDas Plugin bündelt sie in {ACTIVE_SKILL_COUNT} aktiven Arbeitswegen einschließlich Hauptskill.\nNeusatz und Strukturprüfung: {report["date"]}; keine neue Volltextprüfung der Rechtsquellen.\nQuellen, Anwendungsgrenzen und Workflow stehen in jedem Fachmodul.\nKeine Testakte und kein installierbares Plugin.\nDie Markdown-Quellen und installierbaren Pakete finden Sie unter:\nhttps://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/ki-native-kanzlei\n'.encode(),'README.txt')
        for r in rows:put(z,(args.pdf_dir/r['pdf']).read_bytes(),r['pdf'])
        put(z,(args.pdf_dir/'umfang.json').read_bytes(),'umfang.json')
    sums=''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(args.dist.iterdir()))
    (args.dist/'checksums-sha256.txt').write_text(sums)
    print(json.dumps({'files':[p.name for p in sorted(args.dist.iterdir())],'active_skills':ACTIVE_SKILL_COUNT,'modules':MODULE_COUNT,'handbook_pages':report['handbook_pages']},ensure_ascii=False))
if __name__=='__main__':main()
