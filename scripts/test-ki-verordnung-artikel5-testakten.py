#!/usr/bin/env python3
"""Prüft sieben native KI-Verordnungs-Testakten, elf Skills und drei Qualitätsprofile."""
from pathlib import Path
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import json, hashlib, re, zipfile, unicodedata
from docx import Document
import pymupdf as fitz
import yaml
root=Path(__file__).resolve().parents[1]; plugin=root/'ki-verordnung-verbotene-praktiken'; qa=root/'quality/ki-verordnung-2026-10-09/artikel5'; errors=[]; results={'case_files':0,'emails':0,'mime_attachments':0,'word_pdf_pairs':0,'word_pdf_pages':0,'skills':0,'skill_words':0,'profiles':0,'cases':0}
manifest=json.loads((qa/'aktenmanifest.json').read_text())
source=json.loads((root/'scripts/data/ki-verordnung-artikel5-testakten.json').read_text())
norm=lambda x:re.sub(r'\s+','',unicodedata.normalize('NFKC',x)).replace('\u00ad','')
for case in manifest:
 results['cases']+=1
 d=root/'testakten'/case['slug']
 assert len(case['files'])==12
 for f in case['files']:
  p=root/f['path']; assert p.exists(); assert len(p.read_bytes())==f['bytes']; assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'];results['case_files']+=1
  if p.suffix=='.eml':
   results['emails']+=1;m=BytesParser(policy=policy.default).parsebytes(p.read_bytes()); assert not m.defects;assert parsedate_to_datetime(m['Date']).date().isoformat()<='2026-10-09';assert m['Subject'] and m['From'] and m['To'] and m['Message-ID'];assert m.get_body(preferencelist=('plain',)).get_content().strip()
   for part in m.walk():assert not part.defects
   for attachment in m.iter_attachments():
    results['mime_attachments']+=1;filename=attachment.get_filename();assert filename;assert attachment.get_payload(decode=True)==(d/filename).read_bytes(),(p,filename)
    expected={'.pdf':'application/pdf','.docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document','.xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}[(d/filename).suffix];assert attachment.get_content_type()==expected
  if p.suffix=='.docx':
   results['word_pdf_pairs']+=1;doc=Document(p);pdf=fitz.open(p.with_suffix('.pdf'));results['word_pdf_pages']+=len(pdf);txt=norm(''.join(page.get_text() for page in pdf))
   for para in doc.paragraphs:
    if para.text.strip():assert norm(para.text) in txt, (str(p),para.text[:100])
   assert doc.styles['Normal'].font.name=='Times New Roman';assert doc.styles['Normal'].font.size.pt==11
   for page in pdf:
    for block in page.get_text('dict')['blocks']:
     for line in block.get('lines',[]):
      for span in line['spans']:
       x0,y0,x1,y1=span['bbox'];assert x0>=0 and y0>=0 and x1<=page.rect.width+0.1 and y1<=page.rect.height+0.1
  if p.suffix in ('.docx','.xlsx'):
   with zipfile.ZipFile(p) as z:assert z.testzip() is None
 warning='Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.'
 assert (d/'README.md').read_text().count(warning)==2
for p in plugin.glob('skills/*/SKILL.md'):
 results['skills']+=1;text=p.read_text();front,body=text.split('---',2)[1:];meta=yaml.safe_load(front);assert set(meta)=={'name','description'};assert len(meta['description'])<=360 and '§' not in meta['description'];assert meta['name']==p.parent.name
 headers=re.findall(r'^## (\d+)\. (.+)$',body,re.M);assert [x[0] for x in headers]==list('123456'),(p,headers)
 for req in ['Times New Roman','11 pt','ausformuliert']:assert req in text,(p,req)
 results['skill_words']+=len(body.split())
for p in plugin.rglob('*.md'):
 for dest in re.findall(r'\]\(([^\)]+)\)',p.read_text()):
  if dest.startswith(('http','mailto:','#')):continue
  assert (p.parent/dest.split('#')[0]).exists(),(p,dest)
assert results['skills']==11
for kind,key in [('schnellstart','mini_review'),('werkstatt','workshop_review'),('hauptproblem','focus_review')]:
 p=plugin/f'ki-verordnung-verbotene-praktiken-{kind}.md';assert p.read_bytes()==p.with_suffix('.txt').read_bytes()
 if kind!='werkstatt':assert p.stat().st_size<=7500
for pname in ['ki-verordnung-verbotene-praktiken','ki-verordnung-register-meldungen','ki-verordnung-konformitaet']:
 profile=json.loads((root/'quality/evals'/f'{pname}.json').read_text());results['profiles']+=1
 for case in profile['cases']:
  assert len(case['criteria'])>=6 and case['request'] and case['deliverables'] and case['source_basis']
  assert (root/pname/'skills'/case['target_skill']/'SKILL.md').exists()
  for f in case['input_files']:assert (root/f).exists()
  for criterion in case['criteria']:assert criterion['id'] and criterion['text'] and criterion['deliverables']
results['status']='passed';(qa/'artefaktpruefung.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n');print(json.dumps(results,ensure_ascii=False))
