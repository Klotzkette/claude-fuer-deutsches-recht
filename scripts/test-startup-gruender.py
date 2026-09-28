#!/usr/bin/env python3
"""Regressionen für Zeichenbudget, Aktenintegrität und Beteiligungsrechnung.

Diese Tests ersetzen keine juristische oder visuelle Abnahme.
"""
from pathlib import Path
import json
from email import policy
from email.parser import BytesParser
from decimal import Decimal, ROUND_HALF_UP
import subprocess
import unittest
from openpyxl import load_workbook
from prompt_limits import mini_within_limits
from prompt_profiles import validate_files

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'startup-gruender'
CASE = ROOT / 'testakten/startup-gruender-schnittflug-berlin'

class Startup(unittest.TestCase):
    def test_unicode_limit_is_scoped_and_counts_characters(self):
        # 7500 deutsche Zeichen dürfen nicht wegen UTF-8-Mehrbytes gekürzt werden.
        valid = ('ä' * 100 + 'a' * 7400).encode()
        self.assertTrue(mini_within_limits('startup-gruender', valid))
        self.assertFalse(mini_within_limits('anderes-plugin', valid))
        self.assertFalse(mini_within_limits('startup-gruender', valid + b'a'))
        self.assertFalse(mini_within_limits('startup-gruender', b''))
        self.assertFalse(mini_within_limits('startup-gruender', ('ä' * 7500).encode()))
        # JS/Python müssen auch Zeichen außerhalb der BMP gleich zählen.
        astral = ('🚀' * 100 + 'a' * 7400).encode()
        self.assertTrue(mini_within_limits('startup-gruender', astral))
        script = "import {miniWithinLimits as m} from './scripts/prompt-limits.mjs'; console.log(JSON.stringify([m('startup-gruender',Buffer.from('ä'.repeat(100)+'a'.repeat(7400))),m('anderes-plugin',Buffer.from('ä'.repeat(100)+'a'.repeat(7400))),m('startup-gruender',Buffer.from('🚀'.repeat(100)+'a'.repeat(7400))),m('startup-gruender',Buffer.from('a'.repeat(7501)))]))"
        actual=json.loads(subprocess.check_output(['node','--input-type=module','-e',script],cwd=ROOT,text=True))
        self.assertEqual(actual,[True,False,True,False])

    def test_requested_publication(self):
        skills=list((PLUGIN/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills),18)
        self.assertTrue((PLUGIN/'skills/gruendung-begleiten/SKILL.md').is_file())
        data=(PLUGIN/'startup-gruender-schnellstart.md').read_bytes()
        self.assertEqual(len(data.decode()),7500)
        self.assertTrue(mini_within_limits('startup-gruender',data))
        self.assertEqual(validate_files(PLUGIN,'startup-gruender',ROOT),[])

    def test_original_inventory_and_real_attachments(self):
        # Der archivierte Morgenstand bleibt eine eigene, unveränderte Teilakte.
        # Das Gesamtinventar einschließlich Nachreichungen prüft das Ergänzungsskript.
        baseline=json.loads((ROOT/'scripts/data/startup-gruender/morgenstand-originale.json').read_text(encoding='utf-8'))
        originals=[CASE/row['file'] for row in baseline['files']]
        self.assertEqual(len(originals),68)
        self.assertEqual(len({p.name for p in originals}),68)
        self.assertTrue(all(p.is_file() for p in originals))
        self.assertEqual(sum(p.suffix=='.eml' for p in originals),24)
        attachments=[]
        for p in originals:
            if p.suffix!='.eml':continue
            msg=BytesParser(policy=policy.default).parsebytes(p.read_bytes())
            for field in ['From','To','Date','Subject','Message-ID']:
                self.assertTrue(msg[field],f'{p.name}: {field}')
            for part in msg.iter_attachments():
                name=part.get_filename();self.assertTrue(name)
                self.assertEqual(part.get_payload(decode=True),(CASE/name).read_bytes(),f'{p.name}: {name}')
                attachments.append(name)
        self.assertEqual(len(attachments),4)

    def test_finance_receipts_and_voting(self):
        data=json.loads((ROOT/'scripts/data/startup-gruender/finanz.json').read_text())
        receipts=data['receipts'];self.assertEqual(len(receipts),13)
        self.assertEqual(sum(r['gross_cents'] for r in receipts),310923)
        self.assertEqual(sum(r['gross_cents'] for r in receipts if r['paid_date']),239523)
        self.assertEqual(sum(r['gross_cents'] for r in receipts if not r['paid_date']),71400)
        for r in receipts:
            self.assertEqual(r['net_cents']+r['vat_cents'],r['gross_cents'])
            self.assertEqual(int((Decimal(r['net_cents'])*Decimal('0.19')).quantize(Decimal(1),rounding=ROUND_HALF_UP)),r['vat_cents'])
            self.assertTrue((CASE/r['filename']).is_file())
        nominals=[5250,5500,4500,3750,2500,2000,1500]
        self.assertEqual(sum(nominals),25000)
        self.assertEqual(sum(nominals[1:])/sum(nominals),.79)
        self.assertEqual([5250/n*100 for n in [25000,30000,40000,60000]],[21,17.5,13.125,8.75])
        formula_count=0
        for file in CASE.glob('*.xlsx'):
            formulas=load_workbook(file,data_only=False)
            values=load_workbook(file,data_only=True)
            for sheet in formulas:
                for row in sheet:
                    for cell in row:
                        if cell.data_type=='f':
                            formula_count+=1
                            cached=values[sheet.title][cell.coordinate]
                            self.assertIsNotNone(cached.value,f'{file.name}/{sheet.title}/{cell.coordinate}')
                            self.assertNotEqual(cached.data_type,'e')
        self.assertGreater(formula_count,100)

if __name__=='__main__': unittest.main()
