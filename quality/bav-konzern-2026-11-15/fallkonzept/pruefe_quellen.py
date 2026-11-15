"""Prüft die redaktionellen Rohdaten unabhängig vom Dokumentrenderer."""
from pathlib import Path
from decimal import Decimal
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[3]
DATA=ROOT/'scripts/data/bav-konzern-faelle'
OUT=Path(__file__).parent

def colnum(s):
 n=0
 for x in s:n=n*26+ord(x)-64
 return n-1

def evaluate(sheet,cell,trail=()):
 if cell in trail:raise ValueError('Formelzyklus '+cell)
 mt=re.fullmatch(r'([A-Z]+)(\d+)',cell);ci=colnum(mt[1]);ri=int(mt[2])-6
 val=sheet['rows'][ri][ci]
 if isinstance(val,(int,float)):return Decimal(str(val))
 if not str(val).startswith('='):raise ValueError((cell,val))
 def ref(match):return str(evaluate(sheet,match[0],trail+(cell,)))
 exp=val[1:]
 def sumrange(mt):
  ca,ra,cb,rb=mt.groups();total=Decimal(0)
  assert ca==cb,'Prüfer unterstützt vertikale SUM-Bereiche'
  for rr in range(int(ra),int(rb)+1):total+=evaluate(sheet,f'{ca}{rr}',trail+(cell,))
  return str(total)
 exp=re.sub(r'SUM\(([A-Z]+)(\d+):([A-Z]+)(\d+)\)',sumrange,exp)
 exp=re.sub(r'[A-Z]+\d+',ref,exp)
 assert re.fullmatch(r'[0-9. +*/()\-]+',exp),exp
 # Nur die bereits auf Zahlen und Grundoperationen reduzierte Formel auswerten.
 import ast
 def ev(n):
  if isinstance(n,ast.Expression):return ev(n.body)
  if isinstance(n,ast.Constant):return Decimal(str(n.value))
  if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -ev(n.operand)
  if isinstance(n,ast.BinOp):
   a,b=ev(n.left),ev(n.right)
   if isinstance(n.op,ast.Add):return a+b
   if isinstance(n.op,ast.Sub):return a-b
   if isinstance(n.op,ast.Mult):return a*b
   if isinstance(n.op,ast.Div):return a/b
  raise ValueError(type(n))
 return ev(ast.parse(exp,mode='eval'))
report=[]
for path in sorted(DATA.glob('*.json')):
 c=json.loads(path.read_text());items=c['documents']+c['workbooks']+c['slides']
 paths=[d['path'] for d in items];ids=[d['id'] for d in items]
 assert 35<=len(items)<=45,(path,len(items))
 assert len(set(paths))==len(paths) and len(set(ids))==len(ids)
 assert all(q.startswith(('Grundakte/','Fortsetzung/')) and '..' not in q.split('/') for q in paths)
 assert all(Path(q).suffix in {'.pdf','.docx','.eml','.png','.pptx','.xlsx','.csv','.txt'} for q in paths)
 for d in c['documents']:
  assert d['body'] and all(isinstance(v,str) and v.strip() for v in d['body'])
  assert all(a in paths for a in d['attachments'])
  assert 'Yamamoto' not in json.dumps(d,ensure_ascii=False)
  if d['kind']=='eml':assert d['from_email'].endswith('.example') and d['to_email'].endswith('.example')
 checks=[]
 for wb in c['workbooks']:
  sheets={s['name']:s for s in wb['sheets']}
  for sh in wb['sheets']:
   assert all(len(row)==len(sh['columns']) for row in sh['rows']),(path,wb['id'],sh['name'])
  for check in wb.get('controls',[]):
   observed=evaluate(sheets[check['sheet']],check['cell']);expected=Decimal(str(check['expected']))
   assert abs(observed-expected)<Decimal('.001'),(path,check,observed)
   checks.append(dict(workbook=wb['path'],sheet=check['sheet'],cell=check['cell'],expected=str(expected),observed=str(observed)))
 slug=c['slug']
 if 'meissner' in slug:
  ords=c['workbooks'][0]['sheets'][0]['rows'];assert sum(x[6] for x in ords)==1682000000
  persons=c['workbooks'][1]['sheets'][0]['rows'];assert len(persons)==48
  assert all(x[4]-x[3]>=18 for x in persons)
  assert all(x[4]<=1999 for x in persons if x[1]=='K-VO-1')
  assert sum(x[5] for x in persons)==3269200
  assert persons[16][7]==408
 if 'carve-out' in slug:
  people=c['workbooks'][0]['sheets'][0]['rows'];assert len(people)==60 and people[48][4]==88000
  ca=next(x for x in c['documents'] if x['id']=='30')['csv']['rows'];assert sum(x[4] for x in ca)==28000000
  assert all(sum(x[1:4])==x[4] for x in ca)
  extra=next(x for x in c['documents'] if x['id']=='34')['csv']['rows'];assert sum(x[1] for x in extra)==3600000 and sum(x[2] for x in extra)==2400000
 if 'rentnergesellschaft' in slug:
  rows=next(x for x in c['documents'] if x['id']=='28')['csv']['rows'];assert len(rows)==48
  assert all(int(x[3][:4])-x[2]>=65 for x in rows if x[1]=='Altersrente')
  assert all(2026-x[2]<65 for x in rows if x[1]=='Anwartschaft')
 if 'pensionskasse' in slug:
  rows=c['workbooks'][0]['sheets'][0]['rows'][:3]
  assert sum(x[2] for x in rows)==300000 and sum(x[4] for x in rows)==282000
  assert sum(x[3] for x in rows)==60000 and sum(x[5] for x in rows)==55000
  de=next(x for x in c['documents'] if x['id']=='29')['csv']['rows'];assert len(de)==42 and de[0][3:7]==[1200,60,1128,40]
 report.append({'slug':slug,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'originals':len(items),'grundakte':sum(p.startswith('Grundakte/') for p in paths),'fortsetzung':sum(p.startswith('Fortsetzung/') for p in paths),'text_words':sum(len(' '.join(d['body']).split()) for d in c['documents']),'formats':sorted({Path(q).suffix for q in paths}),'formula_controls':checks})
(OUT/'datenpruefung.json').write_text(json.dumps({'scope':'Quelldaten und Rechenkontrollen; keine PDF-Sichtprüfung oder rechtliche Vollprüfung','cases':report},ensure_ascii=False,indent=2)+'\n')
print(f'{len(report)} Fälle, {sum(r["originals"] for r in report)} Originaldateien, {sum(len(r["formula_controls"]) for r in report)} unabhängige Formelkontrollen bestanden.')
