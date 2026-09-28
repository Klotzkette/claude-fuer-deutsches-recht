#!/usr/bin/env python3
"""Konkrete Beleg-, Betrags- und Exportprüfungen der Bremer Verfahrensakte."""

import argparse
import csv
import hashlib
import importlib.util
from datetime import date, timedelta
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
from openpyxl import load_workbook
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
    def test_supplement_inventory_is_one_table_and_idempotent(self):
        spec = importlib.util.spec_from_file_location('fintech_builder', ROOT/'scripts/build-fintech-bremen-akte.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        original = '| Datei | Inhalt |\n| --- | --- |\n| alt.pdf | Alt |\n\n\n<!-- END fintech-inventory -->\n'
        rows = [('41.docx', '| [zusatz/41.docx](zusatz/41.docx) | Ergänzung |')]
        updated = builder.supplement_inventory(original, 'zusatz', rows)
        self.assertIn('| alt.pdf | Alt |\n| [zusatz/', updated)
        self.assertEqual(builder.supplement_inventory(updated, 'zusatz', rows), updated)
        with self.assertRaises(ValueError):
            builder.supplement_inventory('Kein Verzeichnis', 'zusatz', rows)

    def test_original_35_files_are_byte_identical(self):
        baseline = json.loads((FIXTURES/'original-sha256.json').read_text())
        self.assertEqual(len(baseline), 35)
        for name, digest in baseline.items():
            with self.subTest(path=name):
                self.assertEqual(hashlib.sha256((CASE/name).read_bytes()).hexdigest(), digest)

    def test_seven_native_supplements_have_no_sidecars_or_duplicate_sources(self):
        data = json.loads((FIXTURES/'supplements.json').read_text())
        folder = CASE/data['folder']
        expected = {item['id']+'.'+ext for key, ext in [('documents','docx'),('workbooks','xlsx'),('emails','eml')]
                    for item in data[key]}
        self.assertEqual(len(expected), 7)
        self.assertEqual({path.name for path in folder.iterdir()}, expected)
        self.assertEqual(len(working_dump_archive_pairs(CASE, include_gesamt_pdf=False)), 42)
        for item in data['documents']:
            document = Document(folder/(item['id']+'.docx'))
            text = '\n'.join(p.text for p in document.paragraphs)
            self.assertGreater(len(text.split()), 500)
            self.assertNotRegex(text, r'§|Musterlösung|Lösungsmatrix|Testakte|\bKI\b')
            self.assertEqual(document.core_properties.author, 'Klotzkette')
            headings = [p.text for p in document.paragraphs if p.style.name == 'Heading 1']
            self.assertEqual(headings, [p['heading'] for p in item['pages']])
        readme = (CASE/'README.md').read_text()
        for name in expected:
            self.assertIn(f'{data["folder"]}/{name}', readme)

    def test_mime_attachments_match_standalone_native_files(self):
        data = json.loads((FIXTURES/'supplements.json').read_text())
        count = 0
        for item in data['emails']:
            folder = CASE/data['folder']
            mail = BytesParser(policy=policy.default).parsebytes((folder/(item['id']+'.eml')).read_bytes())
            self.assertEqual(mail.defects, [])
            self.assertEqual(str(mail['Subject']), item['subject'])
            self.assertEqual(mail['Date'].datetime.isoformat(), item['date'])
            parts = list(mail.iter_attachments())
            self.assertEqual([part.get_filename() for part in parts], item.get('attachments', []))
            self.assertEqual(mail.get('X-Attachments', ''), '; '.join(item.get('attachments', [])))
            for part in parts:
                count += 1
                self.assertEqual(part.get_payload(decode=True), (folder/part.get_filename()).read_bytes())
                self.assertEqual(part.get_content_disposition(), 'attachment')
                self.assertTrue(part.get_content_type().startswith('application/vnd.openxmlformats-officedocument.'))
                self.assertTrue(zipfile.is_zipfile(io.BytesIO(part.get_payload(decode=True))))
        self.assertEqual(count, 3)

    def test_workbook_payment_totals_and_acquisition_are_separate(self):
        folder = CASE/'03_korrespondenz/04_vertiefung'
        path = folder/'42_Zahlungszuordnung_20260713.xlsx'
        cached = load_workbook(path, data_only=True)
        formulas = load_workbook(path, data_only=False)
        self.assertEqual(cached.sheetnames, ['Zahlungen', 'Abschluss', 'Zuordnung'])
        with (CASE/'03_korrespondenz/30_Buchungsdaten_Geschaeftskonto.csv').open(encoding='utf-8-sig', newline='') as handle:
            payments = [row for row in csv.DictReader(handle, delimiter=';') if row['Empfänger'] == 'Vellio Finance GmbH']
        for r, payment in enumerate(payments, 5):
            self.assertEqual(cached['Zahlungen'][f'A{r}'].value.date().isoformat(), payment['Buchungstag'])
            self.assertEqual(cached['Zahlungen'][f'F{r}'].value, -int(payment['Betrag EUR']))
            self.assertEqual(cached['Zahlungen'][f'G{r}'].value, 'Vellio Finance GmbH')
        for address, value in [('D25',90000),('E25',500000),('F25',590000)]:
            self.assertEqual(cached['Zahlungen'][address].value, value)
            self.assertEqual(formulas['Zahlungen'][address].data_type, 'f')
        for address, value in [('B7',590000),('B8',15000),('B9',515000),('B10',505000),('B12',0),('B13',500000)]:
            self.assertEqual(cached['Abschluss'][address].value, value)
        self.assertEqual(formulas['Abschluss']['B7'].value, '=SUM(B5:B6)')
        self.assertIn('außerhalb Journal', cached['Abschluss']['C13'].value)
        for sheet in cached:
            self.assertEqual(sheet.page_setup.orientation, 'landscape')
            self.assertFalse(any(cell.data_type == 'e' for row in sheet for cell in row))

    def test_workbook_bank_rows_and_selected_payables_reconcile(self):
        path = CASE/'03_korrespondenz/04_vertiefung/43_Kontoabgleich_20260611.xlsx'
        cached = load_workbook(path, data_only=True)
        formulas = load_workbook(path, data_only=False)
        with (CASE/'03_korrespondenz/30_Buchungsdaten_Geschaeftskonto.csv').open(encoding='utf-8-sig', newline='') as handle:
            records = list(csv.DictReader(handle, delimiter=';'))
        for sheet_name, month in [('Maerz','2024-03'),('April','2024-04')]:
            selected = [row for row in records if row['Buchungstag'].startswith(month)]
            for r, record in enumerate(selected, 5):
                sheet = cached[sheet_name]
                self.assertEqual(sheet[f'A{r}'].value.date().isoformat(), record['Buchungstag'])
                self.assertEqual(sheet[f'B{r}'].value, record['Empfänger'])
                self.assertEqual(sheet[f'C{r}'].value, record['Verwendungszweck'])
                self.assertEqual(sheet[f'D{r}'].value, int(record['Betrag EUR']))
                self.assertEqual(sheet[f'E{r}'].value, int(record['Saldo EUR']))
                self.assertEqual(sheet[f'F{r}'].value, int(record['Saldo EUR']))
                self.assertEqual(sheet[f'G{r}'].value, 0)
                self.assertEqual(formulas[sheet_name][f'E{r}'].data_type, 'f')
        expected = [421800,573900,568900,431000,1025900,520900,383000,478380,42520]
        self.assertEqual([cached['Stichtage'][f'B{r}'].value for r in range(5,14)], expected)
        k7 = next(d for d in json.loads((FIXTURES/'business-records.json').read_text())['documents'] if '_K7_' in d['id'])
        op = [row for page in k7['pages'] for row in page.get('table',{}).get('rows',[]) if row[2]]
        self.assertEqual(len(op), 12)
        for r, (creditor, invoice_date, due, amount) in enumerate(op, 5):
            self.assertEqual(cached['OffenePosten'][f'A{r}'].value, creditor)
            self.assertEqual(cached['OffenePosten'][f'B{r}'].value, invoice_date.split(' / ')[0])
            self.assertEqual(cached['OffenePosten'][f'D{r}'].value.strftime('%d.%m.%Y'), due)
            self.assertEqual(cached['OffenePosten'][f'E{r}'].value, int(amount.replace('.', '').removesuffix(',00')))
        self.assertEqual(cached['MaiAbgrenzung']['B5'].value, 598600)
        self.assertEqual(cached['MaiAbgrenzung']['B7'].value, 215600)
        self.assertEqual(formulas['MaiAbgrenzung']['B6'].value, '=April!E17')
        self.assertIn('kein neuer Mai-Kontoauszug', cached['MaiAbgrenzung']['C6'].value)
        for sheet in cached:
            self.assertEqual(sheet.page_setup.orientation, 'landscape')
            self.assertFalse(any(cell.data_type == 'e' for row in sheet for cell in row))

    def test_new_evidence_keeps_historical_knowledge_and_procedural_dates_separate(self):
        data = json.loads((FIXTURES/'supplements.json').read_text())
        risk, vellio, kroeger = data['emails']
        self.assertEqual(risk['date'], '2024-04-09T12:05:00+02:00')
        self.assertIn('weder ein vollständiger Liquiditätsstatus', risk['body'])
        self.assertNotRegex(risk['body'], r'478\.380|598\.600|520\.900|2\. Mai|Insolvenzantrag')
        self.assertIn('kein zusätzlicher damaliger Kontoauszug', vellio['body'])
        self.assertIn('nicht abschließend entschieden', vellio['body'])
        self.assertIn('kein Nachweis', kroeger['body'])
        self.assertIn('2. Mai 2024', kroeger['body'])
        self.assertIn('jutta.kroeger@weserfunken.example', kroeger['from'])
        english = json.dumps(data['documents'][0], ensure_ascii=False)
        self.assertIn('12:30', english)
        self.assertIn('12:31', english)
        self.assertIn('EUR 90,000', english)
        self.assertIn('does not replace the Loan Agreement', english)
        postal = json.dumps(data['documents'][1], ensure_ascii=False)
        for fragment in ['15. September 2026', '10:24', '11:02', '08:46', '15. Oktober 2026', '29. Oktober 2026', '14:18:07']:
            self.assertIn(fragment, postal)
        self.assertIn('keine Bestätigung eines Versands der Klageerwiderung', postal)

    def test_foreign_service_has_one_month_notice_and_two_further_weeks(self):
        facts = json.loads((FIXTURES/'case.json').read_text())
        self.assertEqual(facts['service_date'], '2026-09-15')
        notice = date.fromisoformat(facts['defence_notice_deadline'])
        self.assertEqual(notice, date(2026, 10, 15))
        self.assertEqual(date.fromisoformat(facts['defence_deadline']), notice + timedelta(weeks=2))
        text = '\n'.join(p.extract_text() for p in PdfReader(CASE/'01_eingang/00_Gerichtliche_Verfuegung.pdf').pages)
        text = ' '.join(text.split())
        self.assertIn('binnen einem Monat', text)
        self.assertIn('zwei weiteren Wochen', text)
        self.assertIn('ohne Sicherheitsleistung', text)
        self.assertIn('Prozess auch bei sachlich berechtigter Verteidigung verlieren', text)
        defence = '\n'.join(p.text for p in Document(CASE/'02_klageerwiderung/00_Klageerwiderung_20260928.docx').paragraphs)
        self.assertIn('Einzelrichter', defence)
        self.assertIn('Videoverhandlung', defence)

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
        def destinations(items):
            for item in items:
                if isinstance(item, list):
                    yield from destinations(item)
                else:
                    yield item
        bookmarks = {item.title for item in destinations(reader.outline)}
        supplements = json.loads((FIXTURES/'supplements.json').read_text())
        for key in ('documents', 'workbooks', 'emails'):
            for item in supplements[key]:
                self.assertIn(item['id'], bookmarks)
        self.assertEqual(len(bookmarks), 45)
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
            expected_pages = {
                '41_Completion_Confirmation_20221014': 2,
                '42_Zahlungszuordnung_20260713': 3,
                '43_Kontoabgleich_20260611': 5,
                '44_Risikorueckfrage_20240409': 1,
                '45_Vellio_Buchungsanlagen_20260713': 1,
                '46_Kroeger_Kontoabgleich_20260611': 1,
                '47_Posteingang_Fristen_20260922': 2,
            }
            for stem, count in expected_pages.items():
                matches = [name for name in archive.namelist() if Path(name).stem == stem]
                self.assertEqual(len(matches), 1)
                pages = PdfReader(io.BytesIO(archive.read(matches[0]))).pages
                self.assertEqual(len(pages), count, stem)
                self.assertTrue(all(len(page.extract_text()) > 300 for page in pages), stem)
                for page in pages:
                    self.assertNotRegex(page.extract_text(), r'#{3,}|\(-407|#REF!|#VALUE!|#DIV/0!')
                if stem == '43_Kontoabgleich_20260611':
                    text = ' '.join(page.extract_text() for page in pages)
                    self.assertIn('(500.000,00)', text)
                    self.assertIn('(21.300,00)', text)
            supplements = json.loads((FIXTURES/'supplements.json').read_text())
            for mail in supplements['emails']:
                path = supplements['folder']+'/'+mail['id']+'.pdf'
                text = '\n'.join(page.extract_text() for page in PdfReader(io.BytesIO(archive.read(path))).pages)
                for attachment in mail.get('attachments', []):
                    self.assertIn(attachment, re.sub(r'\s+', '', text))
                    self.assertIn('Anlagen', text)
            pages = sum(len(PdfReader(io.BytesIO(archive.read(name))).pages) for name in archive.namelist() if name.endswith('.pdf'))
            self.assertEqual(len(PdfReader(CASE/'gesamt-pdf'/(SLUG+'_gesamt.pdf')).pages), pages+2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--assets', type=Path)
    args, remaining = parser.parse_known_args()
    ASSETS = args.assets
    unittest.main(argv=[__file__, *remaining])
