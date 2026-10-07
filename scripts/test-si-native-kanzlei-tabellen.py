#!/usr/bin/env python3
"""Rechenprüfung aller 24 Artifact-Tool-Tabellen mit nativer Neuberechnung."""
from pathlib import Path
import importlib.util,json,os,shutil,hashlib,zipfile,io,xml.etree.ElementTree as ET
from decimal import Decimal,ROUND_HALF_UP
from openpyxl import load_workbook
ROOT=Path(__file__).resolve().parents[1]
QA=Path(os.environ.get('SI_QA','/tmp/si-native-kanzlei-20261007/tabellen'));QA.mkdir(parents=True,exist_ok=True)
os.environ['EINBECK_VERTIEFUNG_QA']=str(QA)
spec=importlib.util.spec_from_file_location('native_helpers',ROOT/'scripts/test_vertiefung_einbeck_20261006.py');H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)
S='Zeiten und Honorar'; ranges=[(S,'$A$1:$H$24')]

def patch(p):
    H.patch(p,ranges)
    out=io.BytesIO()
    with zipfile.ZipFile(p) as z,zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as o:
        for i in z.infolist():
            b=z.read(i)
            if i.filename=='xl/workbook.xml':b=b.replace(b'$7:$7',b'$10:$10')
            o.writestr(i,b)
    p.write_bytes(out.getvalue())

cases=json.loads((ROOT/'scripts/si-native-kanzlei-faelle.json').read_text());inputs=QA/'native-input';inputs.mkdir(exist_ok=True)
paths=[];source_formula={};checks=[]
for c in cases:
    src=ROOT/'testakten'/c['slug']/c['xlsx_filename'];patch(src)
    p=inputs/(c['slug']+'.xlsx');shutil.copyfile(src,p);paths.append(p);source_formula[c['slug']]=H.formulas(src)
outs=H.native(paths,'originale')
for c,p in zip(cases,outs):
    assert H.formulas(p)==source_formula[c['slug']],c['slug']
    w=load_workbook(p,data_only=True);errors=[(s.title,x.coordinate,x.value) for s in w for row in s for x in row if x.data_type=='e'];w.close();assert not errors,errors
    mins=sum(t['minutes'] for t in c['times'] if t['confirmed'] and t['billable'])
    net=sum((Decimal(str(t['minutes']))*Decimal(str(c['rate']))/60).quantize(Decimal('.01'),rounding=ROUND_HALF_UP) for t in c['times'] if t['confirmed'] and t['billable']) if c['fee_model'] in ('hourly','capped','estimate') else Decimal(0)
    expected='Vereinbarung offen' if not c['agreed'] else 'RVG-Berechnung offen' if c['fee_model']=='rvg' else c['flat_fee'] if c['fee_model']=='flat' else float(min(net,Decimal(str(c['cap'])))) if c['fee_model']=='capped' else float(net)
    H.check_value(p,S,'D16',mins);H.check_value(p,S,'G18',expected);H.check_value(p,S,'G19',sum(not t['confirmed'] for t in c['times']))
    target=ROOT/'testakten'/c['slug']/c['xlsx_filename'];shutil.copyfile(p,target);patch(target)
    checks.append({'slug':c['slug'],'minutes':mins,'honorar':expected,'formulas':len(source_formula[c['slug']]),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
probes=[];mutdir=QA/'mutationen';mutdir.mkdir(exist_ok=True)
def probe(c,mut,cell,expected):
    p=mutdir/f'probe-{len(probes):02}.xlsx';shutil.copyfile(ROOT/'testakten'/c['slug']/c['xlsx_filename'],p)
    H.patch(p,mutation=[dict(sheet=1,cell=k,value=v) for k,v in mut.items()]);probes.append((p,c,cell,expected,mut))
for model in ['hourly','capped','estimate','flat','rvg']:
    c=next(c for c in cases if c['fee_model']==model and c['agreed'])
    probe(c,{'C7':'Nein'},'G18','Vereinbarung offen')
    if model in ('hourly','capped','estimate'):
        probe(c,{'C6':None},'G18','Zeitzeile prüfen');probe(c,{'D11':-1},'G18','Zeitzeile prüfen')
        probe(c,{'C6':0},'G18',0)
    if model=='capped':probe(c,{'G6':0},'G18',0)
    if model=='flat':probe(c,{'D11':240},'G18',c['flat_fee'])
    if model=='rvg':probe(c,{'G7':250},'G18',250);probe(c,{'G7':-1},'G18','Betrag prüfen')
    if model=='estimate':probe(c,{'G6':0,'D13':0,'F13':'Ja','E13':'Ja','F14':'Ja'},'C20','Schätzung überschritten: Kosteninformation')
results=[]
for p,(_,c,cell,expected,mut) in zip(H.native([p for p,*_ in probes],'mutationen'),probes):
    value=H.check_value(p,S,cell,expected);assert H.formulas(p)==source_formula[c['slug']]
    results.append({'slug':c['slug'],'mutation':mut,'cell':cell,'expected':expected,'actual':value})
report={'engine':'gebündeltes LibreOffice; Formeln unverändert','authoring':'Artifact Tool','baselines':checks,'mutation_checks':results}
target=ROOT/'quality/si-native-kanzlei/tabellen-pruefung.json';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'xlsx':len(checks),'baseline_checks':len(checks)*3,'mutations':len(results)}))
