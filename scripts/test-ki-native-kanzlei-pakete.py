#!/usr/bin/env python3
"""Validiert neue Komponentenpakete, Originalerhaltung und Downloadhinweise."""
import argparse,hashlib,importlib.util,json,subprocess,sys,zipfile
from pathlib import Path
from io import BytesIO
from ki_kanzlei_release_contract import (VERSION, ACTIVE_SKILL_COUNT, ACTIVE_SKILL_SLUGS, MODULE_COUNT, validate_module_report)
from pypdf import PdfReader
from prompt_profiles import validate_files,PROMPT_SUFFIXES
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('dist',type=Path);ap.add_argument('--pdf-report',type=Path,default=ROOT/'quality/ki-native-kanzlei/umfang.json');ap.add_argument('--output',type=Path,default=ROOT/'quality/ki-native-kanzlei/paket-pruefung.json');args=ap.parse_args();DIST=args.dist
def module(name,file):
 sp=importlib.util.spec_from_file_location(name,ROOT/'scripts'/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
R=module('ki_readme','validate-testakten-readme-downloads.py');P=module('ki_plugin','validate-release-zips.py')
errors=[]
for name in ['README.md','ASSET_INDEX.md','ki-native-kanzlei/README.md','testakten/README.md']:
 R.validate_download_notices(name,(ROOT/name).read_text(),errors,case_readme=False)
cases=json.loads((ROOT/'scripts/si-native-kanzlei-faelle.json').read_text());originals=[]
for c in cases:
 folder=ROOT/'testakten'/c['slug'];R.validate_local_readme(folder.name,folder,errors);R.validate_overview(folder.name,(ROOT/'testakten/README.md').read_text(),errors)
 for p in sorted(folder.iterdir()):
  if p.suffix not in ('.docx','.xlsx','.pdf','.eml'):continue
  rel=p.relative_to(ROOT).as_posix();baseline=subprocess.check_output(['git','rev-parse','si-native-kanzlei-v445.33.3:'+rel],cwd=ROOT,text=True).strip();actual=subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip();assert baseline==actual,rel
  originals.append(rel)
assert len(originals)==240;assert not errors,errors
assert not validate_files(ROOT/'ki-native-kanzlei','ki-native-kanzlei',ROOT)
P.validate_plugin_zip(DIST,'ki-native-kanzlei',VERSION);P.validate_focus_skill(DIST/'ki-native-kanzlei.zip',ROOT/'ki-native-kanzlei',ROOT/'quality/evals/ki-native-kanzlei.json')
with zipfile.ZipFile(DIST/'ki-native-kanzlei.zip') as flat,zipfile.ZipFile(DIST/'ki-native-kanzlei-portable.zip') as portable:
 names=flat.namelist();assert len(set(names))==len(names);assert {Path(n).parent.name for n in names if n.startswith('skills/') and n.endswith('/SKILL.md')}==ACTIVE_SKILL_SLUGS
 expected={p.relative_to(ROOT/'ki-native-kanzlei').as_posix():p for p in (ROOT/'ki-native-kanzlei').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(PROMPT_SUFFIXES)}
 assert set(names)==set(expected);assert set(portable.namelist())=={'ki-native-kanzlei/'+n for n in names}
 for name in names:assert flat.read(name)==portable.read('ki-native-kanzlei/'+name)==expected[name].read_bytes(),name
 for name in ['plugin.json','.claude-plugin/plugin.json','.codex-plugin/plugin.json']:
  d=json.loads(flat.read(name));assert d['name']=='ki-native-kanzlei' and d['version']==VERSION
 assert not any(n.endswith(PROMPT_SUFFIXES) for n in names)
report=json.loads(args.pdf_report.read_text());rows=validate_module_report(report)
hand=DIST/'ki-native-kanzlei-skills-handbuch.pdf';assert len(PdfReader(hand).pages)==report['handbook_pages'];assert hashlib.sha256(hand.read_bytes()).hexdigest()==report['handbook_sha256']
with zipfile.ZipFile(DIST/'ki-native-kanzlei-skills-einzelpdfs.zip') as z:
 notice=z.read('README.txt').decode();assert f'{MODULE_COUNT} vollständige Fachmodule' in notice;assert f'{ACTIVE_SKILL_COUNT} aktiven Arbeitswegen' in notice
 assert json.loads(z.read('umfang.json'))==report
 assert set(z.namelist())=={'README.txt','umfang.json',*(r['pdf'] for r in rows)}
 for r in rows:
  assert len(PdfReader(BytesIO(z.read(r['pdf']))).pages)==r['pages']
  assert hashlib.sha256(z.read(r['pdf'])).hexdigest()==r['pdf_sha256'];assert hashlib.sha256((ROOT/r['source']).read_bytes()).hexdigest()==r['source_sha256']
assets={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(DIST.iterdir())}
declared=dict((line.split('  ',1)[1],line.split('  ',1)[0]) for line in (DIST/'checksums-sha256.txt').read_text().splitlines() if line)
assert declared=={name:digest for name,digest in assets.items() if name!='checksums-sha256.txt'},'Release-Prüfsummen passen nicht zu den Assets'
result={'version':VERSION,'scope':'Lokaler KI-Komponentenbuild geprüft; keine Veröffentlichung behauptet; zentrale Paket-/Downloadprüffunktionen unverändert','active_skills':ACTIVE_SKILL_COUNT,'modules':MODULE_COUNT,'plugin_and_portable_source_identical':True,'prompts_separate':True,'handbook_pages':report['handbook_pages'],'preserved_originals':240,'baseline':'si-native-kanzlei-v445.33.3','original_paths':originals,'assets':assets}
args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('original_paths','assets')},ensure_ascii=False))
