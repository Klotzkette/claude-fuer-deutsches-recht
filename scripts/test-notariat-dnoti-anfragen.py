#!/usr/bin/env python3
"""Prüft die tatsächlich gesetzten DNotI-Anfragen und den erhaltenen Aktenbestand."""

from hashlib import sha256
import json
from pathlib import Path
import re
import unicodedata
import unittest

from pypdf import PdfReader
from testakte_disclaimer import pdf_content_errors

ROOT = Path(__file__).resolve().parents[1]
REQUESTS = json.loads((ROOT / 'scripts/data/notariat-dnoti-anfragen.json').read_text())['requests']


def normalized(text):
    return re.sub(r'[\s\-\u00ad\u2011]', '', unicodedata.normalize('NFKC', text))


def body_parts(record):
    yield record['subject']
    introduction = record.get('introduction', [])
    yield from ([introduction] if isinstance(introduction, str) else introduction)
    for section in record['sections']:
        yield section['heading']
        yield from section['paragraphs']
    closing = record['closing']
    yield from ([closing] if isinstance(closing, str) else closing)
    yield from record['attachments']
    yield from (source['label'] for source in record['sources'])


def assert_content(record, text):
    actual = normalized(text)
    for part in body_parts(record):
        if normalized(part) not in actual:
            raise AssertionError('Text fehlt im gesetzten PDF: ' + part[:100])


def continuous_body(record, texts):
    """Entfernt wiederholte Kolumnentitel zwischen geteilten Absätzen."""
    lines = []
    for text in texts:
        for line in text.splitlines():
            if (line.strip() == record['reference']
                    or line.startswith('NOTAR DR. VON TANNRIED-EICHENAU')
                    or '· Notar in Berlin' in line
                    or 'post@notar-tannried.example' in line
                    or re.fullmatch(r'Seite \d+ von \d+', line.strip())):
                continue
            lines.append(line)
    return '\n'.join(lines)


class DNotIAnfragen(unittest.TestCase):
    def test_complete_text_and_page_areas_of_actual_pdfs(self):
        for key, record in REQUESTS.items():
            with self.subTest(case=key):
                path = ROOT / 'testakten' / record['case_slug'] / record['filename']
                reader = PdfReader(path)
                self.assertGreaterEqual(len(reader.pages), 7)
                self.assertLessEqual(len(reader.pages), 12)
                texts = [page.extract_text() or '' for page in reader.pages]
                assert_content(record, continuous_body(record, texts))
                self.assertGreater(len(' '.join(body_parts(record)).split()), 3000)
                first = texts[0]
                for field in ('Deutsches Notarinstitut', 'Gerberstraße 19', '97070 Würzburg',
                              'Lennox Hieronymus von Tannried-Eichenau'):
                    self.assertIn(field, first)
                for n, (page, text) in enumerate(zip(reader.pages, texts), 1):
                    self.assertIn(f'Seite {n} von {len(texts)}', text)
                    self.assertAlmostEqual(float(page.mediabox.width), 595.2756, places=2)
                    self.assertAlmostEqual(float(page.mediabox.height), 841.8898, places=2)
                    fonts = page['/Resources']['/Font'].get_object()
                    self.assertTrue(any('TimesNewRoman' in str(font.get_object().get('/BaseFont'))
                                        for font in fonts.values()))
                self.assertEqual(pdf_content_errors(path.read_bytes()), [])

    def test_source_links_in_actual_pdf_annotations(self):
        for record in REQUESTS.values():
            reader = PdfReader(ROOT / 'testakten' / record['case_slug'] / record['filename'])
            urls = []
            for page in reader.pages:
                for ref in page.get('/Annots', []):
                    action = ref.get_object().get('/A', {})
                    if action.get('/URI'):
                        urls.append(str(action['/URI']))
            self.assertCountEqual(urls, [source['url'] for source in record['sources']])

    def test_missing_or_swapped_case_text_is_rejected(self):
        record = REQUESTS['mumbai']
        with self.assertRaises(AssertionError):
            assert_content(record, 'Nur eine Zusammenfassung des Falls.')
        other = REQUESTS['dubai']
        text = '\n'.join(page.extract_text() or '' for page in PdfReader(
            ROOT / 'testakten' / other['case_slug'] / other['filename']).pages)
        with self.assertRaises(AssertionError):
            assert_content(record, text)

    def test_original_58_documents_are_preserved(self):
        original = json.loads((ROOT / 'quality/notariat-auslandsinvestoren/ursprungsbestand-445.35.7.json').read_text())
        self.assertEqual(len(original), 58)
        for name, digest in original.items():
            self.assertEqual(sha256((ROOT / name).read_bytes()).hexdigest(), digest, name)

    def test_request_is_a_pdf_member_of_its_case(self):
        material = json.loads((ROOT / 'scripts/notariat-auslandsinvestoren-material.json').read_text())
        for case in material['cases']:
            expected = 36 if 'mumbai' in case['slug'] else 34
            self.assertEqual(len(case['docs']), expected)
            record = next(d for d in case['docs'] if d.get('renderer') == 'dnoti')
            request = REQUESTS[record['request_key']]
            self.assertEqual(request['case_slug'], case['slug'])
            self.assertEqual(request['filename'], f"{record['n']:02d}_{record['stem']}.pdf")
            self.assertEqual(record['kind'], 'pdf')
            self.assertFalse((ROOT / 'testakten' / case['slug'] / request['filename']).with_suffix('.docx').exists())


if __name__ == '__main__':
    unittest.main()
