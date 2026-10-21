#!/usr/bin/env python3
"""Prüft Originalarchive, MIME-Anlagen, PDF-Abbildungen und Zahlenkontrollen."""
import argparse
from email import policy
from email.parser import BytesParser
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES
from testakte_zip_common import working_dump_expected_arcnames
from testakte_einzelpdf_common import expected_arcnames
ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def validator(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--dist',type=Path,default=Path('/tmp/insolvenzsachbearbeitung-20261021/dist-akten'));ap.add_argument('--repro',type=Path);args=ap.parse_args()
 cases=json.loads((ROOT/'scripts/data/insolvenzsachbearbeitung-betriebsakten.json').read_text());reports=[]
 original_validator=validator('validate-testakten-release-zips');pdf_validator=validator('validate-testakten-einzelpdf-zips')
 controls={'38_Forderungsliste_Arbeitsstand.xlsx':{'F12':23957.33,'F7':5355,'F9':4232.33},'39_Warenbestand_Murr.xlsx':{'D10':25000},'20_Bestands_und_Belegliste.xlsx':{'D10':2380,'D8':952},'20_Gutscheine_und_Bestand.xlsx':{'D10':900,'B10':36,'B15':2500}}
 for c in cases:
  d=ROOT/'testakten'/c['slug'];names={i['name'] for i in c['files']};readme=(d/'README.md').read_text();assert 'reserved-example-contacts' in readme
  for link in ['../../README.md','../../ASSET_INDEX.md','../README.md','../../insolvenzsachbearbeitung/README.md']:assert link in readme
  for marker in ['<!-- BEGIN gesamt-pdf-section (autogen) -->','<!-- END gesamt-pdf-section (autogen) -->']:assert marker in readme
  original_validator.assert_same(c['slug'],working_dump_expected_arcnames(d,include_gesamt_pdf=False),original_validator.zip_entries(args.dist/f"testakte-{c['slug']}.zip",require_notice=True))
  pdf_validator.assert_same(c['slug'],['README.txt',*expected_arcnames(d)],pdf_validator.zip_entries(args.dist/f"testakte-{c['slug']}-einzelpdfs.zip",expected_suffix='.pdf'))
  attachment_count=0;xlsx_count=0
  with zipfile.ZipFile(args.dist/f"testakte-{c['slug']}.zip") as z:
   assert set(z.namelist())==names|{'README.txt'} and z.testzip() is None
   assert z.namelist()[0]=='README.txt' and z.read('README.txt').startswith(NOTICE_BYTES)
   for i in c['files']:
    p=d/i['name'];data=p.read_bytes();assert z.read(p.name)==data
    if p.suffix=='.eml':
     m=BytesParser(policy=policy.default).parsebytes(data);assert not m.defects
     for h in ['From','To','Subject','Date','Message-ID','MIME-Version']:assert m[h]
     attached={a.get_filename():a.get_payload(decode=True) for a in m.iter_attachments()}
     assert attached=={n:(d/n).read_bytes() for n in i.get('attachments',[])};attachment_count+=len(attached)
    if p.suffix=='.xlsx':
     xlsx_count+=1
     with zipfile.ZipFile(p) as x:
      cells=ET.fromstring(x.read('xl/worksheets/sheet1.xml')).findall('.//s:c',NS);by={cell.get('r'):cell for cell in cells}
      for addr,value in controls[p.name].items():
       assert by[addr].find('s:f',NS) is not None
       assert abs(float(by[addr].find('s:v',NS).text)-value)<0.0001,(p,addr)
  page_count=0
  with zipfile.ZipFile(args.dist/f"testakte-{c['slug']}-einzelpdfs.zip") as z:
   assert set(z.namelist())=={Path(n).stem+'.pdf' for n in names}|{'README.txt'}
   assert z.namelist()[0]=='README.txt' and z.read('README.txt').startswith(NOTICE_BYTES)
   for name in z.namelist():
    assert '/' not in name
    if name.endswith('.pdf'):
     r=PdfReader(io.BytesIO(z.read(name)));page_count+=len(r.pages)
     text='\n'.join(p.extract_text() or '' for p in r.pages)
     assert text.strip() and 'Diese Testakte wurde mit KI' not in text and 'This test case file was generated' not in text
  total=args.dist/f"{c['slug']}_gesamt.pdf";r=PdfReader(total);assert len(r.pages)==page_count
  assert total.read_bytes()==(d/'gesamt-pdf'/total.name).read_bytes()
  if args.repro:
   for n in [total.name,f"testakte-{c['slug']}.zip",f"testakte-{c['slug']}-einzelpdfs.zip"]:assert sha(args.dist/n)==sha(args.repro/n),n
  reports.append({'slug':c['slug'],'originals':len(names),'pdf_pages':page_count,'byte_exact_mime_attachments':attachment_count,'xlsx_with_verified_controls':xlsx_count,'shared_zip_and_a4_rules':True,'package_reproducible':bool(args.repro)})
 out=ROOT/'quality/insolvenzsachbearbeitung/akten/betriebsakten-pruefung.json';out.write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n');print(json.dumps(reports,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
