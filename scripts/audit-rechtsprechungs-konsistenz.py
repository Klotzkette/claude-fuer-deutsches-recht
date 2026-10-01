#!/usr/bin/env python3
"""Erfasst Fach-Markdown und meldet nur mögliche, manuell aufzulösende Datumswidersprüche.

Aktenzeichenabdeckung ist bewusst heuristisch (keine vollständige ECLI-/Auslandsparser-Sprache).
Treffer außerhalb zentraler Profile sind weder als falsch noch als ungeprüft bewiesen.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,re,os
import argparse
parser=argparse.ArgumentParser(description='Heuristischer Aktenzeichen-/Datumsabgleich; ersetzt keine juristische Quellenprüfung.')
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
R=Path(__file__).resolve().parents[1]
market=json.loads((R/'.claude-plugin/marketplace.json').read_text())['plugins']
docket=re.compile(r'\b(?:[IVX]+a?\s+(?:ZR|ZB|ARZ)|\d+\s+(?:AZR|AZB|ABR|StR|BvR|BvL|BvE)|B\s+\d+\s+[A-Z]{1,4})\s+\d+/\d{2}(?:\s+R\b)?|\b[CT][–-]\s*\d+/\d{2}\b|\b\d+\s+(?:C|B|F|VR)\s+\d+\.\d{2}\b')
date=re.compile(r'\b(\d{1,2})\.(\d{1,2})\.(20\d{2}|19\d{2})\b')
def key(x):return re.sub(r'\s+','',x).replace('–','-')
def dates(x):return sorted({f'{y}-{int(m):02}-{int(d):02}' for d,m,y in date.findall(x)})
def report_context(line, source):
 # Relative Markdown links must remain usable from the report's directory.
 def relocate(match):
  target=match.group(2)
  if re.match(r'\w+://|mailto:|#|/',target):return match.group(0)
  return f'[{match.group(1)}]({os.path.relpath(source.parent/target,args.output.resolve().parent)})'
 return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',relocate,line)
canon=defaultdict(list)
for p in market:
 d=json.loads((R/'quality/evals'/f"{p['name']}.json").read_text())
 for x in d.get('prompt_editorial_review',{}).get('decisions',[]):
  for c in docket.findall(x.get('citation','')):canon[key(c)].append({'plugin':p['name'],'citation':x['citation'],'dates':dates(x['citation']),'url':x.get('url')})
rows=[];conflicts=[];nfiles=0;nhits=0;known=0;unknown=Counter()
for p in market:
 root=R/p['source'].removeprefix('./'); fs=set(root.glob('*-werkstatt.md'))|set(root.glob('*-schnellstart.md'))|set(root.glob('*-hauptproblem.md'))
 for sub in ('skills','references'):
  if (root/sub).exists():fs.update((root/sub).rglob('*.md'))
 hits=[]
 for f in sorted(fs):
  nfiles+=1
  for i,line in enumerate(f.read_text().splitlines(),1):
   found=list(docket.finditer(line))
   for m in found:
    nhits+=1;k=key(m.group());ctx=line[max(0,m.start()-150):m.end()+200];ds=dates(line) if len(found)==1 else dates(ctx)
    if k in canon:
     known+=1;expected={v for x in canon[k] for v in x['dates']}
     # This only flags a possible mismatch. Context may cite another decision/date.
     if len(found)==1 and ds and expected and not (set(ds)&expected):
      conflicts.append({'plugin':p['name'],'path':f.relative_to(R).as_posix(),'line':i,'docket':m.group(),'observed_dates':ds,'profile_dates':sorted(expected),'context':report_context(line,f),'references':canon[k]})
    else:unknown[k]+=1
    hits.append(k)
 rows.append({'plugin':p['name'],'directory':p['source'].removeprefix('./'),'files_scanned':len(fs),'docket_occurrences':len(hits),'unique_detected_dockets':len(set(hits)),'profile_dockets':sorted({k for k,v in canon.items() if any(x['plugin']==p['name'] for x in v)})})
result={'method':'heuristic_full_specialist_markdown_crosscheck_not_legal_verification','plugin_count':len(rows),'files_scanned':nfiles,'docket_occurrences':nhits,'occurrences_with_existing_profile_anchor':known,'unique_dockets_outside_profiles':len(unknown),'possible_date_conflicts':len(conflicts),'plugins':rows,'conflicts':conflicts}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('plugins','conflicts')},ensure_ascii=False))
