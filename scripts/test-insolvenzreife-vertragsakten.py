#!/usr/bin/env python3
"""Prüft vollständige Vertragsakten gegen bestehende Bank- und Saldenbelege."""
import hashlib
import json
import re
import unittest
from email import policy
from email.parser import BytesParser
from pathlib import Path
from pypdf import PdfReader
from insolvenzreife_vertragsakten import META, FOLDER, loan_documents, funding_documents, operating_documents, accounting_annexes, eur
ROOT=Path(__file__).resolve().parents[1]
CASES=json.loads((ROOT/'scripts/data/zu-insolvenzfaelle.json').read_text())['cases']
SELECT=json.loads((ROOT/'scripts/data/testakten-grundakten-insolvenzreife.json').read_text())

class ContractsTest(unittest.TestCase):
 def test_vollvertraege_sind_grundaktenquellen(self):
  for case in CASES:
   docs=loan_documents(case)+funding_documents(case)+operating_documents(case)+accounting_annexes(case)
   self.assertGreaterEqual(len(docs),11)
   for d in docs:
    with self.subTest(id=d['id']):
     rel=FOLDER+'/'+d['id']+'.pdf';self.assertIn(rel,SELECT[case['slug']])
     pdf=PdfReader(ROOT/'testakten'/case['slug']/rel)
     text='\n'.join(p.extract_text() for p in pdf.pages)
     normalized=' '.join(text.split())
     self.assertIn(d['title'],normalized);self.assertIn(d['issuer'],normalized);self.assertIn(d['address'],normalized)
     self.assertIn(case['company'],text);self.assertNotIn('[Name',text);self.assertNotIn('Musterlösung',text)
     self.assertTrue(all(re.fullmatch(r'\d+(?:\.\d+)* [^\n]+',s['heading']) for s in d['sections']))
     self.assertGreaterEqual(len(text),1100)
     for page in pdf.pages:
      self.assertGreater(len(page.extract_text()),120)
      self.assertAlmostEqual(float(page.mediabox.width),595.2756,places=2)
      fonts=str(page['/Resources'].get('/Font',''))
      self.assertTrue(fonts)
 def test_kapitalplaene_stimmen_ohne_doppelte_schuld(self):
  for case in CASES:
   p=case['prefix'];m=META[p];docs=loan_documents(case)
   plan=next(d for d in docs if d['id']==p+'-V-02')
   def value(s):return round(float(s.replace(' EUR','').replace('.','').replace(',','.'))*100)
   self.assertEqual(sum(value(r[2]) for r in plan['table']['rows']),m['amount']*100)
   self.assertEqual(value(plan['table']['rows'][-1][3]),0)
   self.assertEqual(value(plan['table']['rows'][0][1]),m['amount']*100)
   for row,nextrow in zip(plan['table']['rows'],plan['table']['rows'][1:]):self.assertEqual(row[3],nextrow[1])
   liabilities={x['id']:x['amount_cents'] for v in case['valuations'] for x in v['liabilities']}
   self.assertEqual(liabilities[p+'-DAR-01'],m['amount']*100+(7500000 if p=='PR' else 0))
   self.assertEqual(liabilities[p+'-NR-01'],m['mother_amount']*100)
 def test_monatsanlagen_rekonstruieren_wirkliche_bankzahlungen(self):
  for case in CASES:
   p=case['prefix'];docs=operating_documents(case)+accounting_annexes(case)
   doc=next(d for d in docs if d['id']==p+{'CB':'-V-13','BZ':'-V-11','PR':'-V-14'}[p])
   tx={t['id']:t for t in case['transactions']}
   for row in doc['table']['rows']:
    total=row[-2];self.assertEqual(total,eur(-tx[row[-1]]['amount_cents']/100))
    values=[round(float(x.replace(' EUR','').replace('.','').replace(',','.'))*100) for x in row[1:-2]]
    self.assertEqual(sum(values),-tx[row[-1]]['amount_cents'])
 def test_drei_emailanhaenge_sind_identische_unterschriebene_ausfertigungen(self):
  for case in CASES:
   directory=ROOT/'testakten'/case['slug']
   mail=BytesParser(policy=policy.default).parsebytes((directory/'08_Uebergabe'/(case['prefix']+'-V-91_Vertragsarchiv.eml')).read_bytes())
   attachments=list(mail.iter_attachments());self.assertEqual(len(attachments),3)
   for part in attachments:
    self.assertEqual(part.get_payload(decode=True),(directory/FOLDER/part.get_filename()).read_bytes())
 def test_pruefungsentscheidende_unterschiede_bleiben_sichtbar(self):
  contracts={c['prefix']:'\n'.join(p.extract_text() for f in (ROOT/'testakten'/c['slug']/FOLDER).glob('*.pdf') for p in PdfReader(f).pages) for c in CASES}
  self.assertIn('Durchsetzungssperre',contracts['BZ']);self.assertIn('§ 39 Absatz 1 Nummer 1 bis 5',contracts['BZ'])
  self.assertIn('ausschließlich der Zahlungstermin',contracts['CB'])
  for text in ['545.000,00 EUR','75.000,00 EUR','620.000 EUR','fünf Bankarbeitstagen','3. Mai','Kartenreserve','220.000 EUR','48.000 EUR']:self.assertIn(text,contracts['PR'])

if __name__=='__main__':unittest.main()
