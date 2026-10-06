"""Native Rechenprüfung; Originalautorenschaft bleibt beim Artifact Tool."""
from pathlib import Path
import importlib.util,json,os,shutil,hashlib
from openpyxl import load_workbook
ROOT=Path(__file__).resolve().parents[1]
QA=Path(os.environ.get('KLINIK_QA','/tmp/krankenhaus-it-ki-20261006/tabellen'))
os.environ['EINBECK_VERTIEFUNG_QA']=str(QA)
spec=importlib.util.spec_from_file_location('native_helpers',ROOT/'scripts/test_vertiefung_einbeck_20261006.py')
H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)
CASE=ROOT/'testakten/krankenhaus-it-ki-auenhoehe-thueringen'
reports=json.loads((QA/'tabellen-pruefung.json').read_text())
paths=[];original={}
for r in reports:
    p=CASE/r['file'];H.patch(p,r['ranges']);original[p.name]=H.formulas(p);paths.append(p)
native=H.native(paths,'originale')
checks=[]
for source,recalculated,r in zip(paths,native,reports):
    assert H.formulas(recalculated)==original[source.name],source.name
    wb=load_workbook(recalculated,data_only=True)
    errors=[(s.title,c.coordinate,c.value) for s in wb for row in s for c in row if c.data_type=='e'];wb.close()
    assert not errors,errors
    shutil.copyfile(recalculated,source);H.patch(source,r['ranges'])
    for i,probe in enumerate(r['probes']):
        dest=QA/'mutationen'/f'{source.stem}-{i}.xlsx';dest.parent.mkdir(exist_ok=True)
        shutil.copyfile(source,dest)
        sheet=[n for n,_ in r['ranges']].index(probe['sheet'])+1
        H.patch(dest,mutation=[{'sheet':sheet,'cell':probe['cell'],'value':probe['value']}])
        changed=H.native([dest],f'mutation-{source.stem}-{i}')[0]
        actual=H.check_value(changed,probe['outSheet'],probe['outCell'],probe['expected'])
        checks.append({'file':source.name,**probe,'actual':actual})
        assert H.formulas(changed)==original[source.name]
baseline=[(paths[0],'Vorhaben','E5',3),(paths[1],'Maßnahmen','G5',10),(paths[2],'Nachweise','E5',7),(paths[3],'Pilotkosten','E14',12066.6),(paths[3],'Pilotkosten','E16',15186.6),(paths[3],'Messplan','B17',160),(paths[3],'Messplan','F8','Noch keine Messung')]
for p,s,c,v in baseline:H.check_value(p,s,c,v)
out={'native_engine':'bundled LibreOffice','formula_preservation':True,'baseline_checks':len(baseline),'mutation_checks':checks,'workbooks':[{'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'formulas':len(original[p.name])} for p in paths]}
target=ROOT/'quality/krankenhaus-it-ki/tabellen-pruefung.json';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'baseline_checks':len(baseline),'mutation_checks':len(checks),'files':len(paths)}))
