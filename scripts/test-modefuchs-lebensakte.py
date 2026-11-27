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
import subprocess
import sys
import unicodedata
import unittest
import zipfile

from PIL import Image
from lxml import html
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import source_zip_includes_gesamt_pdf, working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'testakten/inkasso-zahlungsklage-modefuchs'
FIXTURES = ROOT / 'scripts/fixtures/modefuchs'
SOURCES = FIXTURES / 'quellbelege'
ASSETS = None


def typeset_text(text):
    return ''.join(unicodedata.normalize('NFC', text).split())


class ModefuchsCase(unittest.TestCase):
    def test_28_archived_source_pdfs_are_preserved(self):
        hashes = json.loads((FIXTURES / 'originale-sha256.json').read_text())
        self.assertEqual(len(hashes), 28)
        self.assertEqual({p.name for p in SOURCES.iterdir()}, set(hashes))
        for name, digest in hashes.items():
            with self.subTest(name=name):
                self.assertEqual(hashlib.sha256((SOURCES / name).read_bytes()).hexdigest(), digest)

    def test_typeset_documents_retain_the_source_text_on_every_page(self):
        source_names = {p.name for p in SOURCES.glob('*.pdf')}
        self.assertEqual({p.name for p in (CASE / 'originale').iterdir()}, source_names)
        # Die benannten Ursprungsdokumente haben unterschiedliche Briefköpfe.
        header_sizes = {'00': 2, '18': 1, '19': 2, '25': 1, '26': 1}
        for name in sorted(source_names):
            source, issued = SOURCES / name, CASE / 'originale' / name
            with self.subTest(dokument=name):
                self.assertNotEqual(source.read_bytes(), issued.read_bytes(), 'Ungestalteter Quellbeleg ausgeliefert')
                before, after = PdfReader(source), PdfReader(issued)
                self.assertEqual(len(before.pages), len(after.pages))
                for number, (original, printed) in enumerate(zip(before.pages, after.pages), 1):
                    with self.subTest(seite=number):
                        lines = original.extract_text().splitlines()
                        head = header_sizes.get(name[:2], 5) if number == 1 else 0
                        body = typeset_text(' '.join(lines[head:]))
                        actual = typeset_text(printed.extract_text())
                        self.assertTrue(body)
                        self.assertEqual(actual.count(body), 1, 'Rumpf fehlt, doppelt oder inhaltlich verändert')
                        remainder = actual.replace(body, '', 1)
                        letterhead = lines[:head] if number == 1 else [before.pages[0].extract_text().splitlines()[0]]
                        # Der historische Kanzleikopf nennt einen nicht verliehenen Fachanwaltstitel.
                        if number == 1 and name[:2] in {'16', '17', '20', '22', '24'}:
                            self.assertEqual(letterhead[1], 'Rechtsanwälte · Fachanwalt für Zivilrecht')
                            letterhead[1] = 'Rechtsanwälte · Zivilrecht'
                        if len(before.pages) > 1:
                            letterhead.append(f'Seite {number} von {len(before.pages)}')
                        for line in letterhead:
                            fragment = typeset_text(line)
                            self.assertIn(fragment, remainder)
                            remainder = remainder.replace(fragment, '', 1)
                        self.assertEqual(remainder, '', 'Zusatztext ohne Entsprechung im Quellbeleg')

    def test_checked_in_documents_match_the_build(self):
        subprocess.run([sys.executable, str(ROOT / 'scripts/modefuchs_belege.py'), '--check'], check=True)

    def test_modefuchs_ist_einmal_der_klagewerkstatt_zugeordnet(self):
        self.assertFalse((ROOT / 'testakten/inkasso-modefuchs-cowork-sonderfall').exists())
        spec = importlib.util.spec_from_file_location('direct', ROOT / 'scripts/inject-direkt-loslegen-section.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        mapping = module.discover_testakten_mapping(marketplace['plugins'])
        cases = mapping['forderungsmanagement-klagewerkstatt']
        self.assertEqual([slug for slug in cases if 'modefuchs' in slug], [CASE.name])
        self.assertIn('fintech-darlehen-vertragsuebernahme-bremen', cases)
        self.assertIn('fintech-darlehen-vertragsuebernahme-bremen', mapping['schriftsatz-versandwerkstatt'])

    def test_native_messages_have_matching_embedded_originals(self):
        records = json.loads((FIXTURES / 'korrespondenz.json').read_text())
        dates = {row['id']: parsedate_to_datetime(row['date']) for row in records}
        working = {path for path, _ in working_dump_archive_pairs(CASE, include_gesamt_pdf=False)}
        self.assertEqual(len(list(CASE.glob('*.eml'))), 11)
        self.assertEqual(sum(len(row['attachments']) for row in records), 16)
        self.assertEqual(sum(row.get('mailer') == 'ShopMailer 7.4' for row in records), 3)
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
                rich = message.get_body(preferencelist=('html',))
                if row.get('mailer') == 'ShopMailer 7.4':
                    self.assertIsNotNone(rich)
                    page = html.document_fromstring(rich.get_content())
                    # Der visuelle Briefkopf wiederholt Absender und Betreff aus dem Umschlag.
                    self.assertEqual(typeset_text(page.body.text_content()),
                                     typeset_text('ModeFuchs' + row['subject'] + body))
                    images = page.xpath('//img/@src')
                    self.assertEqual(len(images), 1)
                    self.assertTrue(images[0].startswith('cid:'))
                    self.assertEqual({link for _, _, link, _ in page.iterlinks()}, set(images))
                    inline = [part for part in message.walk() if part.get_content_disposition() == 'inline']
                    self.assertEqual(len(inline), 1)
                    self.assertEqual(str(inline[0]['Content-ID']), f'<{images[0][4:]}>')
                    self.assertEqual(inline[0].get_content_type(), 'image/png')
                    with Image.open(io.BytesIO(inline[0].get_payload(decode=True))) as image:
                        self.assertEqual(image.format, 'PNG')
                        image.verify()
                else:
                    self.assertIsNone(rich)
                if row.get('reply_to'):
                    self.assertLess(dates[row['reply_to']], dates[row['id']])
                parts = list(message.iter_attachments())
                self.assertEqual(len(parts), len(row['attachments']))
                attachments = {part.get_filename(): part.get_payload(decode=True) for part in parts}
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

    def test_email_bodies_match_archived_printouts(self):
        pairs = {
            'Zahlungserinnerung_20_04.eml': '25_E-Mail_Zahlungserinnerung_ModeFuchs_20-04-2025.pdf',
            'DRINGEND_Rechnung_3098.eml': '26_E-Mail_Zweite_Mahnung_ModeFuchs_04-05-2025.pdf',
            'AW_Zahlungsnachweis_ModeFuchs.eml': '18_E-Mail_Altenhausen_an_RA_Brezelmann_27-06-2025.pdf',
        }
        for mail, pdf in pairs.items():
            with self.subTest(mail=mail):
                message = BytesParser(policy=policy.default).parsebytes((CASE / mail).read_bytes())
                body = message.get_body(preferencelist=('plain',)).get_content()
                printed = '\n'.join(page.extract_text() for page in PdfReader(SOURCES / pdf).pages)
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
        self.assertTrue(all('/' not in name for name in names if not name.startswith('Grundakte/')))
        self.assertIn('Grundakte/originale/01_Bestellbestaetigung_03-04-2025.pdf', names)
        self.assertFalse(any(name.startswith('Grundakte/') and 'klage' in name.lower() for name in names))
        self.assertTrue(all(Path(name).suffix not in {'.md', '.json', '.yaml'} for name in names))
        for term in ('claim_gate', 'anspruchsmatrix', 'klagefreigabe', 'fehleranalyse', 'mahnlauf_modefuchs'):
            self.assertFalse(any(term in name for name in names), term)
        self.assertTrue((CASE / '30_Klage_Arbeitsfassung_20250725.docx').is_file())
        self.assertTrue((CASE / '31_Forderungskonto_Arbeitsstand_20250705.xlsx').is_file())

    def test_aggregate_has_new_documents_without_editorial_answers(self):
        path = CASE / 'gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf'
        pages = [page.extract_text() for page in PdfReader(path).pages]
        text = '\n'.join(pages)
        for name in ('Bildschirmfoto_2025-06-27_1817.png', 'Rechnung_April.eml', '31_Forderungskonto_Arbeitsstand_20250705.xlsx'):
            self.assertIn(name, text)
        for term in ('Erwartetes Testergebnis', 'Anspruchs-Gatekeeper-Output', 'Hauptforderung: ROT', 'Erwartete Antwort'):
            self.assertNotIn(term, text)
        self.assertEqual(pdf_content_errors(path.read_bytes()), [])
        collected = [typeset_text(page) for page in pages]
        for issued in sorted((CASE / 'originale').glob('*.pdf')):
            with self.subTest(dokument=issued.name):
                expected = [typeset_text(page.extract_text()) for page in PdfReader(issued).pages]
                self.assertTrue(any(collected[i:i + len(expected)] == expected for i in range(len(collected))),
                                'Gestaltete Seiten fehlen oder stehen nicht zusammen in der Gesamt-PDF')

    def test_release_archives_have_the_same_working_set(self):
        if ASSETS is None:
            self.skipTest('--assets für den vollständigen Archivvergleich angeben')
        slug = CASE.name
        with zipfile.ZipFile(ASSETS / f'testakte-{slug}.zip') as archive:
            expected = working_dump_archive_pairs(CASE, include_gesamt_pdf=source_zip_includes_gesamt_pdf(CASE))
            self.assertEqual(set(archive.namelist()), {'README.txt', *(name for _, name in expected)})
            self.assertEqual(archive.read('README.txt'), NOTICE_BYTES)
            for path, name in expected:
                self.assertEqual(archive.read(name), path.read_bytes(), name)
        with zipfile.ZipFile(ASSETS / f'testakte-{slug}-einzelpdfs.zip') as archive:
            expected = document_arcname_pairs(CASE)
            self.assertEqual(set(archive.namelist()), {'README.txt', *(name for _, name in expected)})
            self.assertEqual(archive.read('README.txt'), NOTICE_BYTES)
            for name in archive.namelist():
                if name.endswith('.pdf'):
                    self.assertNotIn('/', name)
                    self.assertTrue(PdfReader(io.BytesIO(archive.read(name))).pages)
            for path, name in expected:
                if path.suffix.lower() == '.pdf':
                    self.assertEqual(archive.read(name), path.read_bytes(), name)
            konto = PdfReader(io.BytesIO(archive.read('31_Forderungskonto_Arbeitsstand_20250705.pdf')))
            self.assertEqual(len(konto.pages), 2, 'Pro Tabellenblatt wird eine zusammenhängende Druckseite erwartet')
            ledger, receipts = (page.extract_text() for page in konto.pages)
            for term in ('Forderungskonto', 'Summen und Buchsaldo', 'Verfahrensnotiz', 'Mahnbescheidsantrag'):
                self.assertIn(term, ledger)
            self.assertIn('Zahlungsbelege', receipts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--assets', type=Path)
    arguments, remaining = parser.parse_known_args()
    ASSETS = arguments.assets
    unittest.main(argv=[__file__, *remaining])
