#!/usr/bin/env python3
"""Paket-, Beleg- und Inhaltsregressionen; kein Ersatz für Modellläufe."""
from pathlib import Path
import csv
import hashlib
import json
import re
import unittest
from datetime import datetime
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from zipfile import ZipFile
from xml.etree import ElementTree as ET

from pypdf import PdfReader
from prompt_limits import mini_within_limits
from prompt_profiles import validate_files
from testakte_file_filter import include_in_working_dump

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'eigenbedarfskuendigungschecker'
PLUGIN = ROOT / SLUG
CASES = ('eigenbedarf-umwandlung-berlin', 'eigenbedarf-haerte-ersatzwohnung-regensburg')

def doc_text(path):
    with ZipFile(path) as archive:
        tree = ET.fromstring(archive.read('word/document.xml'))
    return ' '.join(e.text or '' for e in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))

class Eigenbedarf(unittest.TestCase):
    def test_ten_individual_skills_and_routing(self):
        skills = {p.parent.name:p for p in (PLUGIN/'skills').glob('*/SKILL.md')}
        self.assertEqual(len(skills), 10)
        main = skills['eigenbedarf-pruefen-und-klaeren'].read_text()
        for name, path in skills.items():
            if name != 'eigenbedarf-pruefen-und-klaeren': self.assertIn(f'`{name}`', main)
            self.assertNotRegex(name, r'werkstatt|schnellstart')
            text = path.read_text()
            for n in range(1,7): self.assertRegex(text, rf'(?m)^## {n}\. ')
            self.assertIn('../../references/zitierweise.md', text)
            self.assertIn('Times New Roman 11 pt', text)

    def test_standalone_prompts_and_review_hashes(self):
        data = (PLUGIN/f'{SLUG}-schnellstart.md').read_bytes()
        self.assertTrue(mini_within_limits(SLUG, data))
        self.assertLessEqual(len(data.decode()), 7500)
        self.assertEqual(validate_files(PLUGIN, SLUG, ROOT), [])
        review=json.loads((ROOT/'quality/evals'/f'{SLUG}.json').read_text())
        self.assertEqual(len(review['cases']),10)
        for key,suffix in [('mini_review','schnellstart'),('workshop_review','werkstatt')]:
            content=(PLUGIN/f'{SLUG}-{suffix}.md').read_bytes()
            self.assertEqual(review[key]['sha256'],hashlib.sha256(content).hexdigest())
        self.assertEqual({c['target_skill'] for c in review['cases']},{p.parent.name for p in (PLUGIN/'skills').glob('*/SKILL.md')})

    def test_current_form_and_distinct_legal_questions(self):
        for suffix in ('schnellstart','werkstatt'):
            text=(PLUGIN/f'{SLUG}-{suffix}.md').read_text()
            for anchor in ('VIII ZR 16/26','VIII ZR 237/25','VIII ZR 247/24','VIII ZR 276/23','VIII ZR 232/15'):
                self.assertIn(anchor,text)
            self.assertIn('Textform',text)
            self.assertIn('Schriftform',text)
            self.assertIn('Anbietpflicht',text)
            self.assertIn('Sperrfrist',text)
            self.assertIn('574 Absatz 1 Satz 2',text)
        skill=(PLUGIN/'skills/widerspruch-und-fortsetzung-formulieren/SKILL.md').read_text()
        self.assertIn('aktuell Textform, nicht Schriftform',skill)
        self.assertIn('im ersten Termin',skill)

    def test_native_case_inventory_and_no_answers(self):
        for slug in CASES:
            case=ROOT/'testakten'/slug
            files=[p for p in case.iterdir() if include_in_working_dump(p,case)]
            self.assertEqual(len(files),12,slug)
            self.assertEqual({p.suffix for p in files},{'.docx','.csv','.eml','.txt'})
            for p in files:
                text=doc_text(p) if p.suffix=='.docx' else p.read_text()
                self.assertNotRegex(text,r'(?i)Musterlösung|Lösungsmatrix|Platzhalter|Formathinweis')
                self.assertNotIn('§',text)
                self.assertRegex(text,r'[äöüÄÖÜß]')
                if p.suffix=='.docx': self.assertGreater(len(text),900,p.name)
            pdf=case/'gesamt-pdf'/f'{slug}_gesamt.pdf'
            reader=PdfReader(pdf)
            combined='\n'.join(p.extract_text() or '' for p in reader.pages)
            self.assertNotIn('Diese Testakte wurde',combined)
            self.assertGreater(len(reader.pages),12)
            for p in files:
                self.assertIn(p.name,combined,p.name)

    def test_mail_headers_dates_and_replies(self):
        messages={}
        for slug in CASES:
            for p in (ROOT/'testakten'/slug).glob('*.eml'):
                msg=BytesParser(policy=policy.default).parsebytes(p.read_bytes())
                for field in ('From','To','Date','Subject','Message-ID','MIME-Version'):
                    self.assertTrue(msg[field],f'{p.name}: {field}')
                date=parsedate_to_datetime(msg['Date'])
                self.assertEqual(str(msg['Date']).split(',')[0],date.strftime('%a'))
                self.assertLessEqual(date.date(),datetime(2026,10,1).date())
                self.assertGreater(len(msg.get_body().get_content()),500)
                messages[str(msg['Message-ID'])]=msg
        for msg in messages.values():
            if msg['In-Reply-To']: self.assertIn(str(msg['In-Reply-To']),messages)

    def test_csv_shape_and_amounts(self):
        for slug in CASES:
            for p in (ROOT/'testakten'/slug).glob('*.csv'):
                rows=list(csv.reader(p.read_text(encoding='utf-8').splitlines(),delimiter=';'))
                self.assertGreaterEqual(len(rows),5)
                self.assertTrue(all(len(r)==len(rows[0]) for r in rows))
        p=ROOT/'testakten'/CASES[0]/'10_mietkonto.csv'
        for r in csv.DictReader(p.read_text().splitlines(),delimiter=';'):
            self.assertEqual(Decimal(r['Nettokaltmiete_EUR'])+Decimal(r['Vorauszahlung_EUR']),Decimal(r['Zahlung_EUR']))
        p=ROOT/'testakten'/CASES[1]/'10_haushaltszahlungen.csv'
        rows=list(csv.DictReader(p.read_text().splitlines(),delimiter=';'))
        self.assertEqual(sum(Decimal(r['Einnahme_EUR']) for r in rows),Decimal('2733.60'))
        self.assertEqual(sum(Decimal(r['Ausgabe_EUR']) for r in rows),Decimal('1648.00'))

    def test_case_dates_and_distinct_property_histories(self):
        berlin=ROOT/'testakten'/CASES[0]
        regensburg=ROOT/'testakten'/CASES[1]
        self.assertIn('14. November 2024',doc_text(berlin/'03_vollzugsmitteilung.docx'))
        self.assertIn('22. Juni 2022',doc_text(berlin/'03_vollzugsmitteilung.docx'))
        self.assertIn('ungeteiltes Mehrfamilienhaus',doc_text(regensburg/'12_hausunterlagen.docx'))
        for path in (berlin/'05_kuendigung.docx',regensburg/'03_kuendigung.docx'):
            text=doc_text(path)
            self.assertIn('30. Juni 2027',text)
            self.assertIn('30. April 2027',text)
            self.assertIn('Textform',text)

if __name__ == '__main__': unittest.main()
