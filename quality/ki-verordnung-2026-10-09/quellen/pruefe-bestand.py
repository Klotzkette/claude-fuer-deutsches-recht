#!/usr/bin/env python3
"""Reproduzierbare Prüfung der am 09.10.2026 bearbeiteten Bestandskomponenten."""
from pathlib import Path
import re,json,hashlib,gzip,importlib.util,subprocess,os,zipfile
root=Path(__file__).resolve().parents[3]; os.chdir(root); failures=[];result={}
spec=importlib.util.spec_from_file_location('mdcheck',root/'scripts/validate-markdown-structure.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
for name in ['ki-vo-ai-act-pruefer','ki-verordnung-transparenzpruefer']:
 base=root/name; skills=list((base/'skills').glob('*/SKILL.md'));desc=[];res={'skills':len(skills),'prompts':{}}
 for p in skills:
  s=p.read_text();front=s.split('---',2)[1];keys=re.findall(r'^([\w-]+):',front,re.M)
  if keys!=['name','description']:failures.append(str(p)+':frontmatter')
  d=re.search(r'^description:\s*(.+)$',front,re.M).group(1);desc.append(d)
  if len(d)>360 or '§' in d or 'im Plugin' in d:failures.append(str(p)+':description')
 if len(set(desc))!=len(desc):failures.append(name+':duplicate description')
 for p in base.rglob('*.md'):
  for problem in m.inspect(p):failures.append(str(p.relative_to(root))+':'+problem)
  s=p.read_text()
  for t in re.findall(r'\]\(([^\s)]+)',s):
   if t.startswith(('http:','https:','mailto:','#')):continue
   t=t.split('#',1)[0]
   if not (p.parent/t).exists():failures.append(str(p.relative_to(root))+':missing '+t)
 profile=json.loads((root/'quality/evals'/f'{name}.json').read_text())
 for suffix,key in [('schnellstart','mini_review'),('werkstatt','workshop_review'),('hauptproblem','focus_review')]:
  p=base/f'{name}-{suffix}.md';b=p.read_bytes()
  if b!=p.with_suffix('.txt').read_bytes():failures.append(name+suffix+':TXT mismatch')
  if suffix!='werkstatt' and len(b)>7500:failures.append(name+suffix+':byte limit')
  k='prompt_sha256' if key=='focus_review' else 'sha256'
  if hashlib.sha256(b).hexdigest()!=profile[key][k]:failures.append(name+suffix+':hash')
  res['prompts'][suffix]={'utf8_bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'md_txt_identisch':True}
 f=profile['focus_review'];p=root/f['skill_path']
 if hashlib.sha256(p.read_bytes()).hexdigest()!=f['skill_sha256']:failures.append(name+':skill hash')
 if json.loads((base/'.claude-plugin/plugin.json').read_text())['version']!='445.35.0':failures.append(name+':version')
 result[name]=res
archives=root/'quality/ki-verordnung-2026-10-09/quellen'
for q in json.loads((archives/'quellen.json').read_text()):
 p=archives/q['archiv'];b=gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes()
 if hashlib.sha256(b).hexdigest()!=q['sha256']:failures.append(q['id']+':archive hash')
result['quellenarchive_hashes']=5
spec=importlib.util.spec_from_file_location('odtcheck',root/'docs/experimentell/vorlagensammlung-recht/scripts/md-to-odt.py');odt=importlib.util.module_from_spec(spec);spec.loader.exec_module(odt)
result['vorlagen']=[]
for relative in ['docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/ki-due-diligence-anforderungsliste-ai-act', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/ki-vo-konformitaetserklaerung-hochrisiko-system', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/ki-systeminventar-due-diligence-ai-act', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/verbotene-ki-praktiken-pruefung-ai-act', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/ki-konformitaet-und-registrierung-due-diligence', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/ki-vo-anbieter-und-betreiberpflichten-checkliste', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/ki-nutzungsrichtlinie-mitarbeitende-unternehmen', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/hochrisiko-ki-einstufung-art-6-ai-act', 'docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/ki-vo-risikomanagementsystem-dokumentation', 'docs/experimentell/vorlagensammlung-recht/arbeitsrecht/betriebsvereinbarung-ki-systeme', 'docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/ki-nutzungsrichtlinie-kanzlei-unternehmen']:
 base=root/relative;md=base/(base.name+'.md')
 try:
  with zipfile.ZipFile(md.with_suffix('.md.zip')) as z: assert z.read(md.name)==md.read_bytes()
  odt.pruefe_generiertes_odt(md.with_suffix('.odt'),landscape=odt.needs_landscape_layout(md.read_text()))
  result['vorlagen'].append({'vorlage':str(md.relative_to(root)),'odt_geprueft':True,'md_zip_identisch':True})
 except Exception as exc: failures.append(str(md.relative_to(root))+':'+str(exc))
import sys
sys.path.insert(0,str(root/'scripts'))
from quality_lab import validate_profile
for name in ['ki-vo-ai-act-pruefer','ki-verordnung-transparenzpruefer']:
 try:validate_profile(json.loads((root/'quality/evals'/f'{name}.json').read_text()),name,root/name,root);result[name]['validate_profile']='OK'
 except Exception as exc:failures.append(name+':validate_profile:'+str(exc))
result['fehler']=failures
Path(__file__).with_name('pruefergebnis-bestand.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(failures))
