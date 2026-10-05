#!/usr/bin/env python3
"""Prüft vollständige Schriftsätze, reale Belegzuordnung, MIME, PDF und Exportbestand."""
from pathlib import Path
import hashlib,importlib.util,io,json,os,re,sys,unittest,zipfile
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime,getaddresses
from datetime import datetime
from docx import Document
from pypdf import PdfReader
from kommunale_schriftverkehr_daten import cases,FOLDER,filename
from testakte_disclaimer import NOTICE_TEXT,NOTICE_DE,NOTICE_EN
from testakte_zip_common import working_dump_archive_pairs
from testakte_einzelpdf_common import document_arcname_pairs
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('schriftverkehr',ROOT/'scripts/build-kommunale-schriftverkehr.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
norm=lambda s:re.sub(r'\s+','',s).replace('\u00ad','')
def full_pdf_text(reader):
 parts=[]
 for number,page in enumerate(reader.pages,1):
  lines=(page.extract_text() or '').strip().splitlines()
  # Office schreibt das PAGE-Feld je nach Objektfolge vor oder nach dem Text.
  # Den Seitenzähler entfernen, damit fortgesetzte Absätze verglichen werden.
  if lines and lines[0].strip()==str(number):lines.pop(0)
  if lines and lines[-1].strip()==str(number):lines.pop()
  parts.append('\n'.join(lines))
 return '\n'.join(parts)
def directory(c):return ROOT/'testakten'/c['slug']
class SchriftverkehrTest(unittest.TestCase):
 def test_preserves_all_130_existing_native_originals(self):
  snapshot=json.loads((ROOT/'quality/kommunale-haftpflicht/schriftverkehr-altbestand.json').read_text());self.assertEqual(snapshot['baseline'],'v445.31.2');self.assertEqual(len(snapshot['sources']),130)
  for source in snapshot['sources']:self.assertEqual(hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest(),source['sha256'],source['path'])
 def test_each_of_twelve_cases_has_exactly_six_additions(self):
  all_cases=cases();self.assertEqual(len(all_cases),12)
  for c in all_cases:
   docs=c['documents'];self.assertEqual({filename(d) for d in docs},{p.name for p in (directory(c)/FOLDER).iterdir() if p.is_file()});self.assertEqual(len(docs),6)
   for kind,count in [('email',3),('letter',2),('claim',1)]:self.assertEqual(sum(d['kind']==kind for d in docs),count)
 def test_claims_have_complete_text_and_resolvable_exhibits(self):
  for c in cases():
   d=next(d for d in c['documents'] if d['kind']=='claim');doc=Document(directory(c)/FOLDER/filename(d));text='\n'.join(p.text for p in doc.paragraphs);self.assertIn('Anlagenverzeichnis',text);self.assertIn('Entwurf',text)
   for paragraph in re.split(r'\n\s*\n',b.claim_body(c,d)):self.assertIn(norm(paragraph.removeprefix('## ')),norm(text),c['slug'])
   self.assertEqual(doc.styles['Normal'].font.name,'Times New Roman');self.assertEqual(doc.styles['Normal'].font.size.pt,11)
   labels={e['label'] for e in c['exhibits']};self.assertEqual(labels,{f'K{i+1}' for i in range(len(c['exhibits']))});self.assertGreaterEqual(len(labels),4)
   used=set(re.findall(r'\bK\s*(\d+)\b',text));self.assertEqual({'K'+n for n in used},labels,c['slug'])
   for e in c['exhibits']:
    self.assertTrue(b.safe_source(directory(c),e['source']).is_file());self.assertIn(norm(e['source']),norm(text),e['label']);self.assertGreaterEqual(len(re.findall(r'\bK\s*'+e['label'][1:]+r'\b',text)),2,(c['slug'],e['label']))
 def test_mime_headers_body_and_attachments(self):
  ids=set()
  for c in cases():
   for d in c['documents']:
    if d['kind']!='email':continue
    msg=BytesParser(policy=policy.default).parsebytes((directory(c)/FOLDER/d['file']).read_bytes());self.assertFalse(msg.defects)
    for h in ('From','To','Subject','Date','Message-ID'):self.assertTrue(msg[h]);self.assertFalse(msg[h].defects)
    for h,key,fallback in [('From','from','sender'),('To','to','recipient')]:self.assertEqual([(a.display_name,a.addr_spec) for a in msg[h].addresses],getaddresses([d.get(key,d.get(fallback))]))
    self.assertNotIn(str(msg['Message-ID']),ids);ids.add(str(msg['Message-ID']));self.assertEqual(parsedate_to_datetime(msg['Date']),datetime.fromisoformat(d['date']))
    self.assertEqual(msg.get_body(preferencelist=('plain',)).get_content().replace('\r\n','\n').strip(),d['body'].strip())
    expected={}
    for n in c.get('attachments',{}).get(d['file'],[]):
     p=directory(c)/FOLDER/n
     if not p.is_file():p=directory(c)/n
     expected[p.name]=p.read_bytes()
    parts=list(msg.iter_attachments());actual={p.get_filename():p.get_payload(decode=True) for p in parts};self.assertEqual(len(parts),len(actual));self.assertEqual(actual,expected)
 def test_letter_pdfs_preserve_entire_text_without_notice(self):
  for c in cases():
   for d in c['documents']:
    if d['kind']!='letter':continue
    pdf=PdfReader(directory(c)/FOLDER/filename(d));text=full_pdf_text(pdf);self.assertGreater(len(pdf.pages),0)
    for paragraph in re.split(r'\n\s*\n',d['body']):self.assertIn(norm(paragraph.removeprefix('## ')),norm(text),(c['slug'],d['file']))
    self.assertNotIn(NOTICE_DE,text);self.assertNotIn(NOTICE_EN,text)
 def test_full_pdf_navigation_for_every_original(self):
  for c in cases():
   root=directory(c);pdf=PdfReader(root/'gesamt-pdf'/f"{c['slug']}_gesamt.pdf");outlines={item.title:pdf.get_destination_page_number(item) for item in pdf.outline if not isinstance(item,list)};pairs=document_arcname_pairs(root)
   self.assertEqual(set(outlines),{p.relative_to(root).with_suffix('').as_posix() for p,a in pairs})
   for d in c['documents']:
    n=FOLDER+'/'+str(Path(filename(d)).with_suffix(''));page=outlines[n];self.assertIn(norm(d['title']),norm(pdf.pages[page].extract_text() or ''),n)
 @unittest.skipUnless(os.environ.get('KOMMUNALE_SCHRIFTVERKEHR_ZIPS'),'Archive separat bereitstellen')
 def test_both_archive_formats_and_complete_new_pdf_text(self):
  base=Path(os.environ['KOMMUNALE_SCHRIFTVERKEHR_ZIPS'])
  for c in cases():
   root=directory(c);native={a:p for p,a in working_dump_archive_pairs(root,include_gesamt_pdf=True)};pdfs={a:p for p,a in document_arcname_pairs(root)}
   for suffix,expected in [('',native),('-einzelpdfs',pdfs)]:
    with zipfile.ZipFile(base/f"testakte-{c['slug']}{suffix}.zip") as z:
     self.assertIsNone(z.testzip());self.assertEqual(set(z.namelist()),set(expected)|{'README.txt'});self.assertEqual(len(z.namelist()),len(set(z.namelist())));self.assertTrue(all('/' not in n for n in z.namelist()));self.assertTrue(z.read('README.txt').decode().startswith(NOTICE_TEXT))
     for name,p in expected.items():
      if not suffix or p.suffix=='.pdf':self.assertEqual(z.read(name),p.read_bytes(),name)
     if suffix:
      reverse={str(p.relative_to(root)):a for a,p in pdfs.items()}
      for d in c['documents']:
       source=FOLDER+'/'+filename(d);reader=PdfReader(io.BytesIO(z.read(reverse[source])));text=full_pdf_text(reader)
       for para in re.split(r'\n\s*\n',b.claim_body(c,d)):self.assertIn(norm(para.removeprefix('## ')),norm(text),(c['slug'],source))
       if d['kind']=='email':
        for key,fallback in [('from','sender'),('to','recipient')]:
         for display,address in getaddresses([d.get(key,d.get(fallback))]):self.assertIn(norm(address),norm(text),(c['slug'],source,key))
if __name__=='__main__':unittest.main()
