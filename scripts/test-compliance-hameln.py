#!/usr/bin/env python3
"""Prüft Originalerhalt, neue Aktenstücke und optional den fertigen Release."""
from __future__ import annotations

import argparse
import csv
from email import policy
from email.parser import BytesParser
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import unicodedata
import unittest
from zipfile import ZipFile

from docx import Document
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_FILENAME, notice_text_errors, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'compliance-abteilung-grosskonzern'
VERSION = '445.35.13'
TAG = PLUGIN + '-v' + VERSION
DIST = None


def normalize(text):
    return re.sub(r'[\s\-\u00ad]', '', unicodedata.normalize('NFKC', text))


def docx_text(path):
    doc = Document(path)
    parts = [p.text for p in doc.paragraphs]
    parts.extend(cell.text for table in doc.tables for row in table.rows for cell in row.cells)
    return '\n'.join(parts)


def require_parts(parts, text, label):
    actual = normalize(text)
    for part in parts:
        if normalize(part) not in actual:
            raise AssertionError(label + ': Text fehlt: ' + part[:100])


def protocol_parts(record):
    yield from (record[k] for k in ('title', 'scope', 'question', 'preservation', 'followup'))
    yield from record['source_files']
    yield record['table']['titel']
    yield from record['table']['spalten']
    for row in record['table']['zeilen']:
        yield from (str(cell) for cell in row)


def template_parts(record):
    yield record['title']
    for heading, paragraph in record['fields']:
        yield heading
        yield paragraph
    yield record['specific_heading']
    yield record['specific_paragraph']


class ComplianceAkten(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads((ROOT / 'scripts/data/compliance-hameln-vertiefung.json').read_text())['cases']
        cls.extensions = json.loads((ROOT / 'scripts/data/compliance-hameln-fachvertiefung.json').read_text())['cases']

    def test_all_338_existing_originals_are_unchanged(self):
        baseline = json.loads((ROOT / 'quality/compliance-vertiefung/ursprungsbestand-445.35.4.json').read_text())
        self.assertEqual(len(baseline), 338)
        for name, digest in baseline.items():
            self.assertEqual(sha256((ROOT / name).read_bytes()).hexdigest(), digest, name)

    def test_previous_408_originals_are_preserved(self):
        previous = json.loads((ROOT / 'quality/compliance-vertiefung/release-bestand.json').read_text())['cases']
        self.assertEqual(sum(len(case['source_sha256']) for case in previous), 408)
        for case in previous:
            directory = ROOT / 'testakten' / case['slug']
            for name, digest in case['source_sha256'].items():
                self.assertEqual(sha256((directory / name).read_bytes()).hexdigest(), digest, name)

    def test_35_cases_have_individual_complete_additions(self):
        self.assertEqual(len(self.cases), 35)
        self.assertEqual({c['nr'] for c in self.cases}, {f'ME-{n:02d}' for n in range(1, 36)})
        self.assertEqual(sum(path.name != '00_Einstieg.pdf' for c in self.cases
                             for path, _ in document_arcname_pairs(ROOT / 'testakten' / c['slug'])), 420)
        bodies = set()
        for case in self.cases:
            directory = ROOT / 'testakten' / case['slug']
            msg = BytesParser(policy=policy.default).parsebytes((directory / '12_Ergaenzende_Stellungnahme.eml').read_bytes())
            self.assertTrue(msg['From'] and msg['To'] and msg['Date'] and msg['Message-ID'], case['slug'])
            self.assertEqual(msg['Subject'], case['nr'] + ' | ' + case['mail']['subject'])
            body = msg.get_body(preferencelist=('plain',)).get_content()
            require_parts(case['mail']['paragraphs'], body, case['slug'])
            self.assertNotIn(body, bodies)
            bodies.add(body)
            protocol = directory / '13_Belegabgleich_und_Sicherungsstand.docx'
            require_parts(protocol_parts(case['protocol']), docx_text(protocol), str(protocol))
            template = ROOT / PLUGIN / 'templates' / (case['slug'] + '.docx')
            require_parts(template_parts(case['template']), docx_text(template), str(template))
            self.assertIn('[', docx_text(template), str(template))
            self.assertEqual(Document(protocol).styles['Normal'].font.name, 'Times New Roman')
            self.assertEqual(Document(template).styles['Normal'].font.size.pt, 11)

    def test_actual_combined_pdfs_contain_both_complete_additions(self):
        for case in self.cases:
            path = ROOT / 'testakten' / case['slug'] / 'gesamt-pdf' / (case['slug'] + '_gesamt.pdf')
            reader = PdfReader(path)
            text = '\n'.join(page.extract_text() or '' for page in reader.pages)
            require_parts(case['mail']['paragraphs'], text, str(path))
            require_parts(protocol_parts(case['protocol']), text, str(path))
            self.assertEqual(pdf_content_errors(path.read_bytes()), [])

    def test_missing_or_swapped_case_is_rejected(self):
        first, second = self.cases[:2]
        with self.assertRaises(AssertionError):
            require_parts(first['mail']['paragraphs'], '\n'.join(second['mail']['paragraphs']), 'Falltausch')
        with self.assertRaises(AssertionError):
            require_parts(first['mail']['paragraphs'], '\n'.join(first['mail']['paragraphs'][:-1]), 'Textverlust')

    def test_four_new_evidence_rounds_in_sources_and_pdfs(self):
        self.assertEqual({case['nr'] for case in self.extensions}, {'ME-22', 'ME-24', 'ME-28', 'ME-35'})
        for case in self.extensions:
            directory = ROOT / 'testakten' / case['slug']
            combined = directory / 'gesamt-pdf' / (case['slug'] + '_gesamt.pdf')
            reader = PdfReader(combined)
            outlines = {entry.title: reader.get_destination_page_number(entry) for entry in reader.outline}
            pdfs = None
            if DIST is not None:
                with ZipFile(DIST / ('testakte-' + case['slug'] + '-einzelpdfs.zip')) as archive:
                    pdfs = {Path(item['filename']).with_suffix('.pdf').name:
                            archive.read(Path(item['filename']).with_suffix('.pdf').name) for item in case['documents']}
            for record in case['documents']:
                path = directory / record['filename']
                if path.suffix == '.eml':
                    msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                    self.assertEqual(msg['Subject'], record['subject'])
                    self.assertTrue(msg['From'] and msg['To'] and msg['Date'] and msg['Message-ID'])
                    self.assertEqual(msg['Date'].datetime.isoformat(), record['date'])
                    if reply := record.get('reply_to'):
                        previous = BytesParser(policy=policy.default).parsebytes((directory / reply).read_bytes())
                        self.assertEqual(msg['In-Reply-To'], previous['Message-ID'])
                    attachments = {part.get_filename(): part.get_payload(decode=True) for part in msg.iter_attachments()}
                    self.assertEqual(attachments, {name: (directory / name).read_bytes() for name in record.get('attachments', [])})
                    parts = record['paragraphs']
                    require_parts(parts, msg.get_body(preferencelist=('plain',)).get_content(), path.name)
                elif path.suffix == '.docx':
                    parts = [record['title']]
                    for section in record['sections']:
                        parts.extend((section['heading'], *section['paragraphs']))
                        if 'table' in section:
                            parts.extend(str(value) for row in [section['table']['headers'], *section['table']['rows']] for value in row)
                    require_parts(parts, docx_text(path), path.name)
                    self.assertEqual(Document(path).styles['Normal'].font.name, 'Times New Roman')
                else:
                    rows = [[str(cell) if cell is not None else '' for cell in row] for row in [record['headers'], *record['rows']]]
                    with path.open(newline='') as stream:
                        self.assertEqual(list(csv.reader(stream)), rows)
                    parts = [cell for row in rows for cell in row]
                start = outlines[path.name]
                end = min((page for page in outlines.values() if page > start), default=len(reader.pages))
                require_parts(parts, '\n'.join(page.extract_text() or '' for page in reader.pages[start:end]), path.name)
                if pdfs is not None:
                    individual = PdfReader(BytesIO(pdfs[path.with_suffix('.pdf').name]))
                    require_parts(parts, '\n'.join(page.extract_text() or '' for page in individual.pages), path.name)
            template = ROOT / PLUGIN / 'templates' / (case['slug'] + '.docx')
            require_parts((part for field in case['template_fields'] for part in field), docx_text(template), template.name)

    def test_complete_release_checksums_and_assets(self):
        if DIST is None:
            self.skipTest('Releaseprüfung mit --dist ausführen')
        files = {p.name: p for p in DIST.iterdir()}
        self.assertEqual(len(files), 113)
        lines = (DIST / 'checksums-sha256.txt').read_text().splitlines()
        recorded = dict(line.split('  ', 1)[::-1] for line in lines)
        self.assertEqual(set(recorded), set(files) - {'checksums-sha256.txt'})
        for name, digest in recorded.items():
            self.assertEqual(sha256(files[name].read_bytes()).hexdigest(), digest, name)
        report = json.loads((DIST / 'release-bestand.json').read_text())
        self.assertEqual((report['version'], report['tag']), (VERSION, TAG))
        self.assertEqual(report['material_sha256'], sha256((ROOT / 'scripts/data/compliance-hameln-vertiefung.json').read_bytes()).hexdigest())
        self.assertEqual(report['fachvertiefung_sha256'], sha256((ROOT / 'scripts/data/compliance-hameln-fachvertiefung.json').read_bytes()).hexdigest())
        for name, members in report['archives'].items():
            with ZipFile(DIST / name) as archive:
                self.assertIsNone(archive.testzip())
                self.assertEqual(set(archive.namelist()), set(members))
                for member, value in members.items():
                    data = archive.read(member)
                    self.assertEqual(sha256(data).hexdigest(), value['sha256'], name + '/' + member)
                    self.assertEqual(len(data), value['bytes'])
                    if member.endswith('.pdf'):
                        self.assertEqual(len(PdfReader(BytesIO(data)).pages), value['pages'])
                        self.assertEqual(pdf_content_errors(data), [])
                if name != PLUGIN + '.zip':
                    self.assertEqual(archive.namelist()[0], NOTICE_FILENAME)
                    self.assertEqual(notice_text_errors(archive.read(NOTICE_FILENAME)), [])
                    self.assertTrue(all('/' not in n and '\\' not in n and not n.endswith('.md') for n in archive.namelist()))

    def test_downloadable_native_and_individual_pdfs_match_sources(self):
        if DIST is None:
            self.skipTest('Releaseprüfung mit --dist ausführen')
        report = json.loads((DIST / 'release-bestand.json').read_text())
        for case in self.cases:
            directory = ROOT / 'testakten' / case['slug']
            pairs = [(path, name) for path, name in document_arcname_pairs(directory)
                     if path.name != '00_Einstieg.pdf']
            item = next(r for r in report['cases'] if r['slug'] == case['slug'])
            self.assertEqual(item['documents'], len(pairs))
            with ZipFile(DIST / item['original']) as original, ZipFile(DIST / item['individual']) as pdfs:
                self.assertEqual(set(pdfs.namelist()), {NOTICE_FILENAME, *[name for _, name in pairs]})
                for source, _ in pairs:
                    self.assertEqual(original.read(source.name), source.read_bytes(), case['slug'] + '/' + source.name)
                combined_name = case['slug'] + '_gesamt.pdf'
                data = original.read(combined_name)
                self.assertEqual(data, (DIST / combined_name).read_bytes())
                combined = PdfReader(BytesIO(data))
                self.assertEqual(len(combined.pages), item['pages'])
                expected_destinations = []
                page = 0
                for source, name in pairs:
                    expected_destinations.append((source.name, page))
                    page += len(PdfReader(BytesIO(pdfs.read(name))).pages)
                self.assertEqual([(entry.title, combined.get_destination_page_number(entry))
                                  for entry in combined.outline], expected_destinations, case['slug'])
                self.assertEqual(page, len(combined.pages))
                require_parts(case['mail']['paragraphs'], '\n'.join(p.extract_text() or '' for p in PdfReader(BytesIO(pdfs.read('12_Ergaenzende_Stellungnahme.pdf'))).pages), case['slug'])
                require_parts(protocol_parts(case['protocol']), '\n'.join(p.extract_text() or '' for p in PdfReader(BytesIO(pdfs.read('13_Belegabgleich_und_Sicherungsstand.pdf'))).pages), case['slug'])
                protocol = PdfReader(BytesIO(pdfs.read('13_Belegabgleich_und_Sicherungsstand.pdf')))
                fonts = {str(font.get_object().get('/BaseFont')) for page in protocol.pages
                         for font in page['/Resources']['/Font'].get_object().values()}
                self.assertTrue(fonts and all('TimesNewRoman' in font for font in fonts), (case['slug'], fonts))
        with ZipFile(DIST / (PLUGIN + '.zip')) as archive:
            for name, digest in report['plugin_members_sha256'].items():
                self.assertEqual(sha256(archive.read(name)).hexdigest(), digest, name)
                if name.startswith(('templates/', 'skills/', 'references/')):
                    self.assertEqual(archive.read(name), (ROOT / PLUGIN / name).read_bytes(), name)
        with ZipFile(DIST / 'Hameln_Compliance_35_Testakten_und_Vorlagen.zip') as archive:
            self.assertEqual(len(archive.namelist()), 71)
            for case in self.cases:
                name = 'testakte-' + case['slug'] + '.zip'
                self.assertEqual(archive.read(name), (DIST / name).read_bytes())
                name = case['slug'] + '.docx'
                self.assertEqual(archive.read(name), (ROOT / PLUGIN / 'templates' / name).read_bytes())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path)
    args, remaining = parser.parse_known_args()
    DIST = args.dist.resolve() if args.dist else None
    unittest.main(argv=[__file__, *remaining])
