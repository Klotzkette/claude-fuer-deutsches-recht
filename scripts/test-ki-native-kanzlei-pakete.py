#!/usr/bin/env python3
"""Validiert neue Komponentenpakete, Originalerhaltung und Downloadhinweise."""
import hashlib,importlib.util,json,subprocess,sys,zipfile
from pathlib import Path
from pypdf import PdfReader
from prompt_profiles import validate_files,PROMPT_SUFFIXES
ROOT=Path(__file__).resolve().parents[1]
DIST=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/tmp/ki-native-kanzlei-20261007/dist')
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
P.validate_plugin_zip(DIST,'ki-native-kanzlei','445.33.8');P.validate_focus_skill(DIST/'ki-native-kanzlei.zip',ROOT/'ki-native-kanzlei',ROOT/'quality/evals/ki-native-kanzlei.json')
with zipfile.ZipFile(DIST/'ki-native-kanzlei.zip') as flat,zipfile.ZipFile(DIST/'ki-native-kanzlei-portable.zip') as portable:
 names=flat.namelist();assert len(set(names))==len(names);assert len([n for n in names if n.startswith('skills/') and n.endswith('/SKILL.md')])==18
 expected={p.relative_to(ROOT/'ki-native-kanzlei').as_posix():p for p in (ROOT/'ki-native-kanzlei').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(PROMPT_SUFFIXES)}
 assert set(names)==set(expected);assert set(portable.namelist())=={'ki-native-kanzlei/'+n for n in names}
 for name in names:assert flat.read(name)==portable.read('ki-native-kanzlei/'+name)==expected[name].read_bytes(),name
 for name in ['plugin.json','.claude-plugin/plugin.json','.codex-plugin/plugin.json']:
  d=json.loads(flat.read(name));assert d['name']=='ki-native-kanzlei' and d['version']=='445.33.8'
 assert not any(n.endswith(PROMPT_SUFFIXES) for n in names)
report=json.loads((ROOT/'quality/ki-native-kanzlei/umfang.json').read_text());assert len(report['skills'])==18;assert all(r['pages']>=10 for r in report['skills'])
hand=DIST/'ki-native-kanzlei-skills-handbuch.pdf';assert len(PdfReader(hand).pages)==report['handbook_pages'];assert hashlib.sha256(hand.read_bytes()).hexdigest()==report['handbook_sha256']
with zipfile.ZipFile(DIST/'ki-native-kanzlei-skills-einzelpdfs.zip') as z:
 assert set(z.namelist())=={'README.txt','umfang.json',*(r['pdf'] for r in report['skills'])}
 for r in report['skills']:
  assert hashlib.sha256(z.read(r['pdf'])).hexdigest()==r['pdf_sha256'];assert hashlib.sha256((ROOT/r['source']).read_bytes()).hexdigest()==r['source_sha256']
assets={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(DIST.iterdir())}
result={'scope':'KI-Komponentenrelease; zentrale Paket-/Downloadprüffunktionen unverändert','skills':18,'plugin_and_portable_source_identical':True,'prompts_separate':True,'handbook_pages':report['handbook_pages'],'preserved_originals':240,'baseline':'si-native-kanzlei-v445.33.3','original_paths':originals,'assets':assets}
(ROOT/'quality/ki-native-kanzlei/paket-pruefung.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('original_paths','assets')},ensure_ascii=False))
