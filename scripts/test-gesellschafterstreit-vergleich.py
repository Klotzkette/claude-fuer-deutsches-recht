#!/usr/bin/env python3
"""Prüft Klageanlagen, Vergleichsunterlagen und deren chronologische Trennung."""
from pathlib import Path
from email import policy
from email.parser import BytesParser
import importlib.util
import io
import re
import tempfile
import unittest
from docx import Document
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'gesellschafterstreit-klageerwiderung-berlin'
CASE_DIR = ROOT / 'testakten' / SLUG
SUBDIR = 'Vergleich_2026-10-09'


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT / 'scripts' / filename)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def normalized(text):
    return re.sub(r'\s+', '', text.replace('\u00ad', ''))


class VergleichTest(unittest.TestCase):
    def test_register_keeps_three_chronological_groups(self):
        builder = module('build-gesellschafter-vorfuehrpakete.py')
        with tempfile.TemporaryDirectory() as temp:
            case = Path(temp) / SLUG
            for filename in ['02_Klage_Seidel.docx', 'Nachtrag_2026-10-08/N01_Bericht.docx', SUBDIR + '/V01_Vertrag.docx']:
                path = case / filename
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'fixture')
            names = [path.relative_to(case).as_posix() for path in builder.sources(case)]
            self.assertEqual(names, ['02_Klage_Seidel.docx', 'Nachtrag_2026-10-08/N01_Bericht.docx', SUBDIR + '/V01_Vertrag.docx'])

    def test_new_inventory_and_all_authored_paragraphs(self):
        from gesellschafterstreit_vergleich_daten import CASE
        directory = CASE_DIR / SUBDIR
        expected = {'README.md', 'V00_Klage_mit_Anlagen_K1_bis_K9.pdf'}
        self.assertEqual(len(CASE['docs']), 5)
        self.assertEqual(len(CASE['emails']), 6)
        for item in CASE['docs']:
            path = directory / item['file']
            expected.update([path.name, path.with_suffix('.pdf').name])
            docx = '\n'.join(p.text for p in Document(path).paragraphs)
            pdf = module('test-gesellschafterstreit-update.py').docx_pdf_body_text(path.with_suffix('.pdf').read_bytes())
            for paragraph in re.split(r'\n\s*\n', item['body']):
                paragraph = paragraph.removeprefix('## ')
                self.assertIn(normalized(paragraph), normalized(docx), path.name)
                self.assertIn(normalized(paragraph), normalized(pdf), path.name)
        expected.update(item['file'] for item in CASE['emails'])
        self.assertEqual({p.name for p in directory.iterdir() if p.is_file()}, expected)

    def test_mime_attachments_are_complete_and_current(self):
        from gesellschafterstreit_vergleich_daten import CASE
        for item in CASE['emails']:
            directory = CASE_DIR / SUBDIR
            message = BytesParser(policy=policy.default).parsebytes((directory / item['file']).read_bytes())
            self.assertEqual(message.defects, [])
            for header in ('From','To','Date','Subject','Message-ID'):
                self.assertTrue(message[header], item['file'])
                self.assertFalse(message[header].defects)
            self.assertEqual(message.get_body(preferencelist=('plain',)).get_content().replace('\r\n', '\n').strip(), item['body'].strip())
            parts = list(message.iter_attachments())
            self.assertCountEqual([p.get_filename() for p in parts], item['attachments'])
            for part in parts:
                self.assertEqual(part.get_payload(decode=True), (directory / part.get_filename()).read_bytes())

    def test_claim_packet_contains_each_actual_annex_and_no_later_evidence(self):
        packet = PdfReader(CASE_DIR / SUBDIR / 'V00_Klage_mit_Anlagen_K1_bis_K9.pdf')
        outlines = [item for item in packet.outline if isinstance(item,dict)]
        self.assertEqual(len(outlines), 10)
        marks = [str(item['/Title']).split(' - ')[0] for item in outlines[1:]]
        self.assertEqual(marks, [f'Anlage K{n}' for n in range(1,10)])
        text = '\n'.join(page.extract_text() or '' for page in packet.pages)
        for expected in ('Gottfried Seidel', 'Spreebogen Lichtwerk', 'II ZR 77/16', 'SBS-2026-084'):
            self.assertIn(expected, text)
        self.assertNotIn('N01_Ergaenzung_Brandt', text)
        self.assertNotIn('V01_', text)
        from pypdf import PdfWriter
        claim_only = PdfWriter()
        for page in packet.pages[:packet.get_destination_page_number(outlines[1])]:
            claim_only.add_page(page)
        buffer = io.BytesIO()
        claim_only.write(buffer)
        claim_text = module('test-gesellschafterstreit-update.py').docx_pdf_body_text(buffer.getvalue())
        from vorfuehrakte_gesellschafter_berlin import CASE
        claim = next(d for d in CASE['documents'] if d['file']=='02_Klage_Seidel.docx')
        for paragraph in re.split(r'\n\s*\n', claim['body']):
            self.assertIn(normalized(paragraph.removeprefix('## ')), normalized(claim_text))
        self.assertIn('21.09.2026', (CASE_DIR / '11_Nachrichten_K7.txt').read_text())
        self.assertNotIn('28.09.2026', (CASE_DIR / '11_Nachrichten_K7.txt').read_text())


if __name__ == '__main__':
    unittest.main()
