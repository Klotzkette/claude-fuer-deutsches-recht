#!/usr/bin/env python3
"""Prüft die zusammengeführte ModeFuchs-Akte bis zu den herunterladbaren Dateien."""

import argparse
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import unittest
import zipfile

from PIL import Image
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES, pdf_content_errors
from testakte_einzelpdf_common import expected_arcnames
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'testakten/inkasso-zahlungsklage-modefuchs'
FIXTURES = ROOT / 'scripts/fixtures/modefuchs'
ASSETS = None


class ModefuchsCase(unittest.TestCase):
    def test_original_28_pdfs_are_preserved(self):
        hashes = json.loads((FIXTURES / 'originale-sha256.json').read_text())
        self.assertEqual(len(hashes), 28)
        for name, digest in hashes.items():
            with self.subTest(name=name):
                self.assertEqual(hashlib.sha256((CASE / 'originale' / name).read_bytes()).hexdigest(), digest)

    def test_one_case_and_two_forderungsmanagement_assignments(self):
        self.assertFalse((ROOT / 'testakten/inkasso-modefuchs-cowork-sonderfall').exists())
        spec = importlib.util.spec_from_file_location('direct', ROOT / 'scripts/inject-direkt-loslegen-section.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        mapping = module.discover_testakten_mapping(marketplace['plugins'])
        self.assertEqual(mapping['forderungsmanagement-klagewerkstatt'], [
            'fintech-darlehen-vertragsuebernahme-bremen', 'inkasso-zahlungsklage-modefuchs'])
        self.assertIn('fintech-darlehen-vertragsuebernahme-bremen', mapping['schriftsatz-versandwerkstatt'])

    def test_native_messages_have_matching_embedded_originals(self):
        records = json.loads((FIXTURES / 'korrespondenz.json').read_text())
        dates = {row['id']: parsedate_to_datetime(row['date']) for row in records}
        working = {path for path, _ in working_dump_archive_pairs(CASE, include_gesamt_pdf=False)}
        self.assertEqual(len(list(CASE.glob('*.eml'))), 11)
        for row in records:
            with self.subTest(message=row['file']):
                path = CASE / row['file']
                self.assertIn(path, working)
                message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                for header in ('From', 'To', 'Date', 'Subject', 'Message-ID', 'MIME-Version'):
                    self.assertTrue(message.get(header), header)
                self.assertFalse(message.defects)
                self.assertEqual(message['Message-ID'], row['id'])
                self.assertEqual(parsedate_to_datetime(message['Date']), dates[row['id']])
                body = message.get_body(preferencelist=('plain',)).get_content().replace('\r\n', '\n')
                if row.get('quote_message'):
                    original = next(item for item in records if item['id'] == row['quote_message'])
                    self.assertTrue(body.startswith(row['body']))
                    self.assertTrue(body.endswith(original['body']))
                    self.assertIn('-----Ursprüngliche Nachricht-----', body)
                else:
                    self.assertEqual(body, row['body'])
                if row.get('reply_to'):
                    self.assertLess(dates[row['reply_to']], dates[row['id']])
                attachments = {part.get_filename(): part.get_payload(decode=True) for part in message.iter_attachments()}
                display = row.get('attachment_names', {})
                self.assertEqual(set(attachments), {display.get(name, Path(name).name) for name in row['attachments']})
                for name in row['attachments']:
                    self.assertIn(CASE / name, working)
                    self.assertEqual(attachments[display.get(name, Path(name).name)], (CASE / name).read_bytes())

    def test_payment_dates_and_identity_are_consistent(self):
        records = json.loads((FIXTURES / 'korrespondenz.json').read_text())
        payment = next(row for row in records if row['file'].startswith('10_email_'))
        self.assertIn('am 01.07. auf unserem Konto verbucht', payment['body'])
        self.assertIn('weitergeleitete Direktzahlung', payment['body'])
        self.assertIn('IZ-MF-2025-1749', payment['subject'])
        self.assertNotIn('IZ-2025-08841', json.dumps(records, ensure_ascii=False))
        self.assertNotIn('g.von.altenhausen@altenhausen-privat.de', json.dumps(records))

    def test_email_bodies_match_existing_printouts(self):
        pairs = {
            'Zahlungserinnerung_20_04.eml': '25_E-Mail_Zahlungserinnerung_ModeFuchs_20-04-2025.pdf',
            'DRINGEND_Rechnung_3098.eml': '26_E-Mail_Zweite_Mahnung_ModeFuchs_04-05-2025.pdf',
            'AW_Zahlungsnachweis_ModeFuchs.eml': '18_E-Mail_Altenhausen_an_RA_Brezelmann_27-06-2025.pdf',
        }
        for mail, pdf in pairs.items():
            with self.subTest(mail=mail):
                message = BytesParser(policy=policy.default).parsebytes((CASE / mail).read_bytes())
                body = message.get_body(preferencelist=('plain',)).get_content()
                printed = '\n'.join(page.extract_text() for page in PdfReader(CASE / 'originale' / pdf).pages)
                printed = printed[printed.index('Sehr geehrter'):]
                normalize = lambda text: re.sub(r'\s+', ' ', text.replace(chr(167), 'Paragraf')).strip()
                self.assertEqual(normalize(body), normalize(printed))

    def test_scan_copies_and_screen_images_exist(self):
        for name in ('Scan007.pdf', 'Scan_20250610_113247.pdf', 'Dokument1.pdf'):
            reader = PdfReader(CASE / name)
            self.assertEqual(len(reader.pages), 1)
            self.assertFalse(reader.pages[0].extract_text().strip())
            self.assertTrue(reader.pages[0].images)
        for name in ('Bildschirmfoto_2025-06-27_1817.png', 'Bildschirmfoto_Postausgang_20250701.png'):
            with Image.open(CASE / name) as image:
                self.assertEqual(image.size, (1536, 1080))
        self.assertTrue((CASE / 'IMG_2047.jpg').is_file())

    def test_working_documents_exclude_editorial_answers(self):
        pairs = working_dump_archive_pairs(CASE, include_gesamt_pdf=False)
        self.assertEqual(len(pairs), 47)
        names = [name for _, name in pairs]
        self.assertTrue(all('/' not in name for name in names))
        self.assertTrue(all(Path(name).suffix not in {'.md', '.json', '.yaml'} for name in names))
        for term in ('claim_gate', 'anspruchsmatrix', 'klagefreigabe', 'fehleranalyse', 'mahnlauf_modefuchs'):
            self.assertFalse(any(term in name for name in names), term)
        self.assertTrue((CASE / '30_Klage_Arbeitsfassung_20250725.docx').is_file())
        self.assertTrue((CASE / '31_Forderungskonto_Arbeitsstand_20250705.xlsx').is_file())

    def test_aggregate_has_new_documents_without_editorial_answers(self):
        path = CASE / 'gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf'
        text = '\n'.join(page.extract_text() for page in PdfReader(path).pages)
        for name in ('Bildschirmfoto_2025-06-27_1817.png', 'Rechnung_April.eml', '31_Forderungskonto_Arbeitsstand_20250705.xlsx'):
            self.assertIn(name, text)
        for term in ('Erwartetes Testergebnis', 'Anspruchs-Gatekeeper-Output', 'Hauptforderung: ROT', 'Erwartete Antwort'):
            self.assertNotIn(term, text)
        self.assertEqual(pdf_content_errors(path.read_bytes()), [])

    def test_release_archives_have_the_same_working_set(self):
        if ASSETS is None:
            self.skipTest('--assets für den vollständigen Archivvergleich angeben')
        slug = CASE.name
        with zipfile.ZipFile(ASSETS / f'testakte-{slug}.zip') as archive:
            expected = working_dump_archive_pairs(CASE, include_gesamt_pdf=True)
            self.assertEqual(set(archive.namelist()), {'README.txt', *(name for _, name in expected)})
            self.assertEqual(archive.read('README.txt'), NOTICE_BYTES)
            for path, name in expected:
                self.assertEqual(archive.read(name), path.read_bytes(), name)
        with zipfile.ZipFile(ASSETS / f'testakte-{slug}-einzelpdfs.zip') as archive:
            self.assertEqual(set(archive.namelist()), {'README.txt', *expected_arcnames(CASE)})
            self.assertEqual(archive.read('README.txt'), NOTICE_BYTES)
            for name in archive.namelist():
                if name.endswith('.pdf'):
                    self.assertNotIn('/', name)
                    self.assertTrue(PdfReader(io.BytesIO(archive.read(name))).pages)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--assets', type=Path)
    arguments, remaining = parser.parse_known_args()
    ASSETS = arguments.assets
    unittest.main(argv=[__file__, *remaining])
