#!/usr/bin/env python3
"""Quellen-, Export- und Erhaltungsprüfung; keine automatische juristische Bewertung."""
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from datetime import datetime
from pathlib import Path
import hashlib
import io
import json
import os
import re
import unittest
import zipfile
from docx import Document
from pypdf import PdfReader
from kommunale_alltagsakten_daten import CASES
from testakte_disclaimer import NOTICE_DE, NOTICE_EN, NOTICE_TEXT

ROOT = Path(__file__).resolve().parents[1]
def directory(case):
    return ROOT/'testakten'/case['slug']
def normalized(text):
    return re.sub(r'\s+', '', text).replace('\u00ad', '')

class AlltagsaktenTests(unittest.TestCase):
    def test_eight_small_complete_case_inventories(self):
        self.assertEqual(len(CASES), 8)
        self.assertEqual(len({c['slug'] for c in CASES}), 8)
        for case in CASES:
            expected = {d['file'] for d in case['documents']}
            actual = {p.name for p in directory(case).iterdir() if p.is_file() and p.suffix in {'.docx','.eml','.txt','.xlsx','.pdf'}}
            self.assertEqual(expected, actual, case['slug'])
            self.assertTrue(8 <= len(expected) <= 10, case['slug'])
            self.assertTrue({'.docx','.eml'} <= {Path(n).suffix for n in expected})
            self.assertTrue(4 <= len(case['core']) <= 6)
            self.assertTrue(set(case['core']) <= expected)
            self.assertIn('01_Pruefauftrag.eml', expected)

    def test_native_text_preserved_in_full(self):
        for case in CASES:
            for item in case['documents']:
                path = directory(case)/item['file']
                if path.suffix == '.docx':
                    doc = Document(path)
                    text = '\n'.join(p.text for p in doc.paragraphs)
                    for paragraph in re.split(r'\n\s*\n', item['body']):
                        self.assertIn(paragraph.removeprefix('## '), text, str(path))
                elif path.suffix == '.txt':
                    self.assertIn(item['body'], path.read_text(), str(path))

    def test_mime_dates_and_byte_identical_attachments(self):
        for case in CASES:
            for item in case['documents']:
                if not item['file'].endswith('.eml'):
                    continue
                msg = BytesParser(policy=policy.default).parsebytes((directory(case)/item['file']).read_bytes())
                self.assertFalse(msg.defects)
                for h in ('From','To','Subject','Date','Message-ID'):
                    self.assertTrue(msg[h]); self.assertFalse(msg[h].defects)
                self.assertEqual(parsedate_to_datetime(msg['Date']), datetime.fromisoformat(item['date']))
                self.assertEqual(msg.get_body(preferencelist=('plain',)).get_content().replace('\r\n','\n').strip(), item['body'])
                parts = list(msg.iter_attachments())
                attachments = {p.get_filename(): p.get_payload(decode=True) for p in parts}
                self.assertEqual(len(parts), len(attachments))
                self.assertEqual(set(attachments), set(case['attachments'].get(item['file'], [])))
                for name, data in attachments.items():
                    self.assertEqual(data, (directory(case)/name).read_bytes(), name)

    def test_existing_four_cases_are_byte_identical(self):
        proof = json.loads((ROOT/'quality/kommunale-haftpflicht/alltagsakten-altbestand.json').read_text())
        self.assertEqual(proof['baseline'], 'v445.31.1')
        self.assertEqual(len(proof['sources']), 58)
        for item in proof['sources']:
            path = ROOT/item['path']
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item['sha256'], item['path'])

    def test_readmes_and_complete_pdf_navigation(self):
        for case in CASES:
            readme = (directory(case)/'README.md').read_text()
            for required in (NOTICE_DE, NOTICE_EN, 'reserved-example-contacts', '../../kommunale-haftpflicht/README.md'):
                self.assertIn(required, readme)
            pdf = PdfReader(directory(case)/'gesamt-pdf'/f"{case['slug']}_gesamt.pdf")
            text = '\n'.join(p.extract_text() or '' for p in pdf.pages)
            self.assertNotIn(NOTICE_DE, text); self.assertNotIn(NOTICE_EN, text)
            outlines = {item.title: pdf.get_destination_page_number(item) for item in pdf.outline if not isinstance(item,list)}
            self.assertEqual(set(outlines), {Path(d['file']).stem for d in case['documents']})
            for item in case['documents']:
                start = normalized(pdf.pages[outlines[Path(item['file']).stem]].extract_text() or '')
                self.assertIn(normalized(item['title']), start, item['file'])

    @unittest.skipUnless(os.environ.get('KOMMUNALE_ALLTAG_ZIPS'), 'KOMMUNALE_ALLTAG_ZIPS für Archivprüfung setzen')
    def test_archives_sources_and_full_pdf_text(self):
        base = Path(os.environ['KOMMUNALE_ALLTAG_ZIPS'])
        for case in CASES:
            originals = {d['file'] for d in case['documents']}
            for suffix in ('','-einzelpdfs'):
                with zipfile.ZipFile(base/f"testakte-{case['slug']}{suffix}.zip") as z:
                    self.assertIsNone(z.testzip())
                    names = z.namelist()
                    self.assertEqual(len(names), len(set(names)))
                    self.assertTrue(all('/' not in n for n in names))
                    self.assertTrue(z.read('README.txt').decode().startswith(NOTICE_TEXT))
                    if not suffix:
                        combined = f"{case['slug']}_gesamt.pdf"
                        self.assertEqual(set(names), originals | {'README.txt',combined})
                        for name in originals:
                            self.assertEqual(z.read(name), (directory(case)/name).read_bytes(), name)
                        self.assertEqual(z.read(combined), (directory(case)/'gesamt-pdf'/combined).read_bytes())
                    else:
                        self.assertEqual(set(names), {Path(n).stem+'.pdf' for n in originals} | {'README.txt'})
                        for item in case['documents']:
                            p = PdfReader(io.BytesIO(z.read(Path(item['file']).stem+'.pdf')))
                            text = '\n'.join(page.extract_text() or '' for page in p.pages)
                            self.assertNotIn(NOTICE_DE,text); self.assertNotIn(NOTICE_EN,text)
                            for paragraph in re.split(r'\n\s*\n', item['body']):
                                self.assertIn(normalized(paragraph.removeprefix('## ')), normalized(text), (case['slug'],item['file']))

if __name__ == '__main__':
    unittest.main()
