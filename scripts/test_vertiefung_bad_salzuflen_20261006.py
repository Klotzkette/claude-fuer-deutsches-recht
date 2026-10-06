#!/usr/bin/env python3
"""Native Ergebnis- und Änderungstests der ergänzten Buchhaltungsakten."""
from pathlib import Path
import io,json,os,re,shutil,zipfile,xml.etree.ElementTree as ET,hashlib
from openpyxl import load_workbook
import test_vertiefung_einbeck_20261006 as common
ROOT=Path(__file__).resolve().parents[1]
CASE=ROOT/'testakten/bauwirtschaft-buchhaltung-bauunternehmen-bad-salzuflen'
QA=Path('/tmp/bauwirtschaft-vertiefung-20261006/bad');QA.mkdir(parents=True,exist_ok=True)
common.QA=QA
RANGES={72:[('Offene Posten','A1:F35'),('Belegweg','A1:C28')],73:[('Stunden','A1:G21'),('Abstimmung','A1:D21')],74:[('Mietansatz','A1:G19'),('Zahlungsweg','A1:F18')],75:[('Zahlvorschlag','A1:F21'),('Konten','A1:D15'),('Belegweg','A1:D15')]}
def language(p):
    out=io.BytesIO()
    with zipfile.ZipFile(p)as z,zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED)as o:
        for info in z.infolist():
            data=z.read(info)
            if info.filename=='docProps/core.xml':
                e=ET.fromstring(data);c=e.find(common.DC+'language')
                if c is None:c=ET.SubElement(e,common.DC+'language')
                c.text='de-DE';data=ET.tostring(e,encoding='utf-8',xml_declaration=True)
            o.writestr(info,data)
    p.write_bytes(out.getvalue())
def check(p,s,c,v):
    actual=common.check_value(p,s,c,v)
    w=load_workbook(p,data_only=True)
    assert not [(s.title,c.coordinate,c.value)for s in w for row in s for c in row if c.data_type=='e'];w.close()
    return dict(file=p.name,sheet=s,cell=c,expected=v,actual=actual)
def main():
    files=sorted(p for p in CASE.glob('*.xlsx')if int(p.name[:2])>=72)
    for p in files:common.patch(p,RANGES[int(p.name[:2])]);language(p)
    maps={p.name:common.formulas(p)for p in files}
    baselines={72:[('Offene Posten','F26',13341),('Offene Posten','F17',571)],73:[('Stunden','G18',25400),('Abstimmung','C15',0)],74:[('Zahlungsweg','E12',571)],75:[('Konten','D8','offen'),('Konten','D9','offen')]}
    out=common.native(files,'basis');checks=[]
    for p in out:
        assert maps[p.name]==common.formulas(p),(p.name,'Formeln verändert')
        for s,c,v in baselines[int(p.name[:2])]:checks.append(check(p,s,c,v))
        shutil.copyfile(p,CASE/p.name);common.patch(CASE/p.name,RANGES[int(p.name[:2])]);language(CASE/p.name)
    tests=[
    (72,[(1,'C17',None)],'Offene Posten','F26','Angabe fehlt'),
    (73,[(1,'C8',None)],'Abstimmung','C15','Angabe fehlt'),
    (73,[(1,'B8','BS26-99')],'Abstimmung','C15','Angabe fehlt'),
    (74,[(1,'C10',None)],'Zahlungsweg','E12','Angabe fehlt'),
    (75,[(1,'B8',None)],'Konten','C8','Kontozuordnung offen'),
    (75,[(1,'B8','999999')],'Konten','C9','Kontozuordnung offen'),
    (72,[(1,'E17',571)],'Offene Posten','F17',500),
    (72,[(1,'D13',0)],'Offene Posten','F13',238),
    (73,[(1,'C8',80)],'Abstimmung','C15',300),
    (73,[(1,'C8',0)],'Stunden','G8',440),
    (74,[(1,'C10',7)],'Zahlungsweg','E9',749.5),
    (75,[(1,'C11','freigegeben'),(1,'D11',571),(1,'E11',0)],'Zahlvorschlag','F11',571),
    (75,[(1,'C11','freigegeben'),(1,'D11',571)],'Zahlvorschlag','F11','offen'),
    (75,[(1,'C11','freigegeben'),(1,'D11',0),(1,'E11',0)],'Zahlvorschlag','F11',0),
    (75,[(1,'C11','freigegeben'),(1,'D11',-1),(1,'E11',0)],'Zahlvorschlag','F11','offen'),
    (75,[(1,'C8','freigegeben'),(1,'D8',2142),(1,'E8',0)],'Konten','D8',77069.8),
    (75,[(1,'C11','freigegeben'),(1,'D11',571),(1,'E11',0)],'Konten','D9','offen'),
    (75,sum(([(1,'C'+str(r),'freigegeben'),(1,'D'+str(r),v),(1,'E'+str(r),0)]for r,v in [(9,4800),(10,3200),(11,571),(12,1428)]),[]),'Konten','D9',28219.8)]
    inputs=[];stage=QA/'probes';stage.mkdir(exist_ok=True)
    for i,(n,changes,s,c,v)in enumerate(tests):
        src=next(p for p in files if int(p.name[:2])==n);p=stage/f'probe-{i:02}.xlsx'
        shutil.copyfile(src,p);common.patch(p,mutation=[dict(sheet=a,cell=b,value=c)for a,b,c in changes]);inputs.append(p)
    probes=[]
    for p,t in zip(common.native(inputs,'mutationen'),tests):probes.append({**check(p,*t[2:]),'changes':t[1]})
    preservation=json.loads((QA/'source-preservation.json').read_text())
    assert all(hashlib.sha256((CASE/n).read_bytes()).hexdigest()==h for n,h in preservation['hashes'].items())
    (QA/'native-pruefung.json').write_text(json.dumps({'baseline':checks,'mutations':probes,'formulas':{k:len(v)for k,v in maps.items()},'historische_originale_unveraendert':len(preservation['hashes'])},ensure_ascii=False,indent=2))
    print(f'{len(checks)} native Ergebnisprüfungen; {len(probes)} Änderungen bestanden.')
if __name__=='__main__':main()
