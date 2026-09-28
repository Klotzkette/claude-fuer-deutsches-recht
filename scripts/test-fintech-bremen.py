#!/usr/bin/env python3
"""Konkrete Beleg-, Betrags- und Exportprüfungen der Bremer Verfahrensakte."""

import argparse
import csv
from decimal import Decimal
from email import policy
from email.parser import BytesParser
import io
import json
from pathlib import Path
import re
import unittest
import zipfile

from docx import Document
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES, pdf_content_errors
from testakte_einzelpdf_common import expected_arcnames
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'fintech-darlehen-vertragsuebernahme-bremen'
CASE = ROOT/'testakten'/SLUG
FIXTURES = ROOT/'scripts/fixtures/fintech-bremen'
ASSETS = None


class FintechCase(unittest.TestCase):
    def test_claim_has_25_pages_and_twelve_exhibits_have_75_pages(self):
        claim = CASE/'01_eingang/01_Klage_20260908.pdf'
        self.assertEqual(len(PdfReader(claim).pages), 25)
        exhibits = [p for p in (CASE/'01_eingang').glob('*.pdf') if re.match(r'\d+_K\d+_', p.name)]
        self.assertEqual(len(exhibits), 12)
        self.assertEqual(sum(len(PdfReader(p).pages) for p in exhibits), 75)

    def test_all_expected_documents_are_present_and_readable(self):
        manifest = json.loads((FIXTURES/'documents.json').read_text())
        for row in manifest:
            with self.subTest(path=row['path']):
                path = CASE/row['path']
                self.assertTrue(path.is_file())
                if path.suffix == '.pdf':
                    reader = PdfReader(path)
                    self.assertEqual(len(reader.pages), row['pages'])
                    self.assertEqual(pdf_content_errors(path.read_bytes()), [])
                    self.assertTrue(all(len(p.extract_text().strip()) > 300 for p in reader.pages))
                else:
                    doc = Document(path)
                    self.assertGreater(sum(len(p.text) for p in doc.paragraphs), 15000)
                    self.assertEqual(doc.core_properties.author, 'Klotzkette')

    def test_bank_export_reconciles_every_running_balance_and_payment(self):
        path = CASE/'03_korrespondenz/30_Buchungsdaten_Geschaeftskonto.csv'
        with path.open(encoding='utf-8-sig', newline='') as handle:
            rows = list(csv.DictReader(handle, delimiter=';'))
        self.assertGreater(len(rows), 180)
        balance = Decimal('84300')
        for row in rows:
            balance += Decimal(row['Betrag EUR'])
            self.assertEqual(balance, Decimal(row['Saldo EUR']))
        payments = [row for row in rows if row['Empfänger'] == 'Vellio Finance GmbH']
        self.assertEqual(len(payments), 19)
        self.assertEqual(sum(Decimal(r['Betrag EUR']) for r in payments), Decimal('-590000'))
        self.assertEqual(sum(Decimal(r['Betrag EUR']) for r in payments if 'Zinsperiode' in r['Verwendungszweck']), Decimal('-90000'))
        self.assertFalse(any(r['Empfänger'] == 'Nexora Frontbank AG' for r in rows))
        april = [r for r in rows if r['Buchungstag'] == '2024-04-15' and r['Empfänger'] == 'Vellio Finance GmbH']
        self.assertEqual(Decimal(april[-1]['Saldo EUR']), Decimal('520900'))

    def test_working_inputs_and_defence_are_separate(self):
        pairs = working_dump_archive_pairs(CASE, include_gesamt_pdf=False)
        names = [name for _, name in pairs]
        self.assertIn('02_klageerwiderung/00_Klageerwiderung_20260928.docx', names)
        self.assertTrue(any(name.endswith('.eml') for name in names))
        self.assertTrue(any(name.endswith('.csv') for name in names))
        self.assertFalse(any(Path(name).suffix in {'.md','.json','.yaml'} for name in names))
        self.assertFalse(any('loesung' in name.casefold() for name in names))
        for path in CASE.rglob('*.eml'):
            mail = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
            for header in ('From','To','Date','Message-ID','Subject'):
                self.assertTrue(mail.get(header), (path.name, header))
            self.assertGreater(len(mail.get_body(preferencelist=('plain',)).get_content()), 250)

    def test_combined_pdf_contains_every_working_document_and_bookmarks(self):
        reader = PdfReader(CASE/'gesamt-pdf'/(SLUG+'_gesamt.pdf'))
        self.assertGreater(len(reader.pages), 150)
        text = '\n'.join(p.extract_text() for p in reader.pages)
        self.assertIn('Klageerwiderung', text)
        self.assertIn('500.000', text)
        self.assertGreaterEqual(len(reader.outline), 3)
        self.assertEqual(pdf_content_errors((CASE/'gesamt-pdf'/(SLUG+'_gesamt.pdf')).read_bytes()), [])

    def test_release_archives_match_sources(self):
        if ASSETS is None:
            self.skipTest('--assets für den zusätzlichen Archivvergleich angeben')
        expected = working_dump_archive_pairs(CASE, include_gesamt_pdf=True)
        with zipfile.ZipFile(ASSETS/('testakte-'+SLUG+'.zip')) as archive:
            self.assertEqual(set(archive.namelist()), {'README.txt', *(name for _,name in expected)})
            self.assertEqual(archive.read('README.txt'), NOTICE_BYTES)
            for path, name in expected:
                self.assertEqual(archive.read(name), path.read_bytes())
        with zipfile.ZipFile(ASSETS/('testakte-'+SLUG+'-einzelpdfs.zip')) as archive:
            self.assertEqual(set(archive.namelist()), {'README.txt', *expected_arcnames(CASE)})
            self.assertEqual(archive.read('README.txt'), NOTICE_BYTES)
            for name in archive.namelist():
                if name.endswith('.pdf'):
                    self.assertTrue(PdfReader(io.BytesIO(archive.read(name))).pages)
                    self.assertEqual(pdf_content_errors(archive.read(name)), [])
            for stem, pages in (('00_Klageerwiderung_20260928', 20), ('01_B1_Transfer_Assumption_Agreement', 12)):
                matches = [name for name in archive.namelist() if Path(name).stem == stem]
                self.assertEqual(len(matches), 1, stem)
                self.assertEqual(len(PdfReader(io.BytesIO(archive.read(matches[0]))).pages), pages)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--assets', type=Path)
    args, remaining = parser.parse_known_args()
    ASSETS = args.assets
    unittest.main(argv=[__file__, *remaining])
