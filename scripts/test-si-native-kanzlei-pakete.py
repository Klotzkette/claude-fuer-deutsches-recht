#!/usr/bin/env python3
"""Quellenidentität, zentrale Paketregeln, Promptgrenzen und neue Downloadgruppen."""
from pathlib import Path
import json,zipfile,io,sys,hashlib,importlib.util
from pypdf import PdfReader
from prompt_profiles import validate_files
from testakte_disclaimer import NOTICE_BYTES
from testakte_zip_common import working_dump_archive_pairs
ROOT=Path(__file__).resolve().parents[1]
if not (ROOT/'si-native-kanzlei/.claude-plugin/plugin.json').is_file():
 raise SystemExit('Historische SI-Paketprüfung: im Tag si-native-kanzlei-v445.33.3 ausführen. Aktuell test-ki-native-kanzlei-pakete.py verwenden; dieses prüft auch die Erhaltung aller 240 Originale.')
DIST=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/tmp/si-native-kanzlei-20261007/dist')
def mod(name,file):
 sp=importlib.util.spec_from_file_location(name,ROOT/'scripts'/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
Z=mod('si_validate_native','validate-testakten-release-zips.py');E=mod('si_validate_pdfzip','validate-testakten-einzelpdf-zips.py');G=mod('si_validate_gesamt','validate-testakten-gesamt-pdf.py');R=mod('si_validate_readme','validate-testakten-readme-downloads.py');P=mod('si_validate_plugin','validate-release-zips.py')
cases=json.loads((ROOT/'scripts/si-native-kanzlei-faelle.json').read_text());errors=[];reports=[]
for c in cases:
 folder=ROOT/'testakten'/c['slug'];originals=working_dump_archive_pairs(folder,include_gesamt_pdf=False);assert len(originals)==10
 native=DIST/f'testakte-{folder.name}.zip';single=DIST/f'testakte-{folder.name}-einzelpdfs.zip'
 Z.assert_same(native.name,Z.expected_entries(folder),Z.zip_entries(native,require_notice=True))
 E.assert_same(single.name,['README.txt',*E.expected_arcnames(folder)],E.zip_entries(single,expected_suffix='.pdf'))
 with zipfile.ZipFile(native) as z:
  assert z.namelist()[0]=='README.txt' and z.read('README.txt').startswith(NOTICE_BYTES)
  for source,name in originals:assert z.read(name)==source.read_bytes(),(c['slug'],name)
 with zipfile.ZipFile(single) as z:
  assert len(z.namelist())==11
  for name in z.namelist():
   if name.endswith('.pdf'):assert not G.pdf_content_errors(z.read(name)),(c['slug'],name)
 total=folder/'gesamt-pdf'/f'{folder.name}_gesamt.pdf';assert not G.pdf_content_errors(total.read_bytes())
 R.validate_local_readme(folder.name,folder,errors);R.validate_overview(folder.name,(ROOT/'testakten/README.md').read_text(),errors)
 reports.append({'slug':folder.name,'originals':10,'source_identical':True,'individual_pdfs':10,'gesamt_pages':len(PdfReader(total).pages)})
for name in ['README.md','ASSET_INDEX.md','si-native-kanzlei/README.md','testakten/README.md']:
 R.validate_download_notices(name,(ROOT/name).read_text(),errors,case_readme=False)
assert not errors,errors
assert not validate_files(ROOT/'si-native-kanzlei','si-native-kanzlei',ROOT)
P.validate_plugin_zip(DIST,'si-native-kanzlei','445.33.3');P.validate_focus_skill(DIST/'si-native-kanzlei.zip',ROOT/'si-native-kanzlei',ROOT/'quality/evals/si-native-kanzlei.json')
with zipfile.ZipFile(DIST/'si-native-kanzlei.zip') as flat,zipfile.ZipFile(DIST/'si-native-kanzlei-portable.zip') as portable:
 names=flat.namelist();assert len([n for n in names if n.startswith('skills/') and n.endswith('/SKILL.md')])==16
 for name in names:assert portable.read('si-native-kanzlei/'+name)==flat.read(name)
 for name in ['plugin.json','.claude-plugin/plugin.json','.codex-plugin/plugin.json']:
  d=json.loads(flat.read(name));assert d['name']=='si-native-kanzlei' and d['version']=='445.33.3'
 assert not any(n.endswith(('-werkstatt.md','-werkstatt.txt','-schnellstart.md','-schnellstart.txt','-hauptproblem.md','-hauptproblem.txt')) for n in names)
with zipfile.ZipFile(DIST/'si-native-kanzlei-24-testakten.zip') as z:
 assert z.namelist()[0]=='README.txt' and z.read('README.txt').startswith(NOTICE_BYTES)
 assert len(z.namelist())==25
 for c in cases:
  name=f'testakte-{c["slug"]}.zip';assert z.read(name)==(DIST/name).read_bytes()
assets={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in DIST.glob('*.zip')}
report={'scope':'Nur neues Komponentenrelease; zentrale Prüffunktionen unverändert verwendet','cases':reports,'assets':assets,'plugin_skills':16,'originals':240,'original_source_identity':True,'portable_same_content':True,'standalone_prompts_separate':True,'downloads_and_notices_valid':True}
(ROOT/'quality/si-native-kanzlei/paket-pruefung.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'cases':24,'originals':240,'pdfs':240,'zip_assets':len(assets),'all_checks':'passed'}))
