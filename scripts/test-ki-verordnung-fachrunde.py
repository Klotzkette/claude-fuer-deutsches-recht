#!/usr/bin/env python3
"""Prüft die Quellen und Pakete der KI-Verordnungs-Fachrunde 445.35.0.

Ohne Argumente: Scope, Profile, amtliche Quellenkopien, native Akten und PDFs.
Mit --dist VERZEICHNIS: zusätzlich vollständige Releaseauswahl, ZIP-Inhalte,
Originalbytes, Einzel-PDF-Zuordnung und sämtliche Prüfsummen. Keine Aussage
über materielle Rechtsrichtigkeit oder eine Live-Ausführung in einem Client.
"""
from __future__ import annotations

import argparse
import contextlib
from collections import Counter
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses, parsedate_to_datetime
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path, PurePosixPath
import re
import unittest
from unittest import mock
import tempfile
import xml.etree.ElementTree as ET
import zipfile

from pypdf import PdfReader
import yaml

import quality_lab
from prompt_profiles import PROMPT_SUFFIXES
from release_routing import plugin_asset_url, case_asset_url, validate_plugin_version
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
VERSION = '445.35.0'
TAG = 'ki-verordnung-v' + VERSION
SCOPE_PATH = ROOT / 'scripts/data/ki-verordnung-release-scope.json'
QUALITY = ROOT / 'quality/ki-verordnung-2026-10-09'
SPECIALISTS = (
    'ki-verordnung-verbotene-praktiken',
    'ki-verordnung-hochrisiko-pruefer',
    'ki-verordnung-register-meldungen',
    'ki-verordnung-konformitaet',
)
DIST = None
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
FORMATS = {'.eml': 4, '.docx': 3, '.pdf': 3, '.xlsx': 1, '.txt': 1}
MIME = {'.pdf': 'application/pdf', '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def load_script(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT / 'scripts' / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FachrundeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scope = read_json(SCOPE_PATH)
        cls.marketplace = read_json(ROOT / '.claude-plugin/marketplace.json')
        cls.entries = {p['name']: p for p in cls.marketplace['plugins']}
        cls.release = load_script('build-ki-verordnung-release.py')

    def assert_pdf(self, data, label):
        self.assertTrue(data.startswith(b'%PDF-'), label)
        self.assertEqual(pdf_content_errors(data), [], label)
        reader = PdfReader(io.BytesIO(data))
        self.assertGreater(len(reader.pages), 0, label)
        self.assertTrue(any((page.extract_text() or '').strip() for page in reader.pages), label)
        return reader

    def assert_safe_zip(self, archive, label):
        names = archive.namelist()
        self.assertEqual(len(names), len(set(names)), f'{label}: doppelte Einträge')
        for name in names:
            path = PurePosixPath(name)
            self.assertFalse(path.is_absolute() or '..' in path.parts or '\\' in name, f'{label}: unsicherer Pfad {name}')
        self.assertIsNone(archive.testzip(), label)

    def test_scope_versions_and_routes(self):
        self.assertEqual(self.scope['version'], VERSION)
        self.assertEqual(len(self.scope['plugins']), 48)
        self.assertEqual(len(set(self.scope['plugins'])), 48)
        self.assertEqual(len(self.scope['cases']), 9)
        self.assertEqual(len(set(self.scope['cases'])), 9)
        self.assertTrue(set(SPECIALISTS) <= set(self.scope['plugins']))
        for slug in self.scope['plugins']:
            with self.subTest(plugin=slug):
                self.assertIn(slug, self.entries)
                entry = self.entries[slug]
                directory = self.release.plugin_directory(slug)
                self.assertEqual(entry['version'], VERSION)
                manifest = read_json(directory / '.claude-plugin/plugin.json')
                self.assertEqual(manifest['name'], slug)
                self.assertEqual(manifest['version'], VERSION)
                codex = directory / '.codex-plugin/plugin.json'
                if codex.exists():
                    self.assertEqual(read_json(codex)['name'], slug)
                    self.assertEqual(read_json(codex)['version'], VERSION)
                validate_plugin_version(entry, self.marketplace['version'], root=ROOT)
                self.assertTrue(plugin_asset_url(slug, root=ROOT).endswith(f'/{TAG}/{slug}.zip'))
        for slug in self.scope['cases']:
            for suffix in ('', '-einzelpdfs'):
                self.assertTrue(case_asset_url(slug, suffix, root=ROOT).endswith(f'/{TAG}/testakte-{slug}{suffix}.zip'))
        # Every documented peripheral correction must be shipped, including legal README corrections.
        for correction in read_json(QUALITY / 'peripherie-korrekturen.json'):
            directory = (ROOT / correction['datei']).parent
            while directory != ROOT:
                manifest = directory / '.claude-plugin/plugin.json'
                if manifest.is_file():
                    self.assertIn(read_json(manifest)['name'], self.scope['plugins'], correction['datei'])
                    break
                directory = directory.parent

    def test_four_specialists_skills_prompts_and_profiles(self):
        for slug in SPECIALISTS:
            with self.subTest(plugin=slug):
                directory = ROOT / slug
                self.assertTrue((directory / '.codex-plugin/plugin.json').is_file())
                skills = sorted((directory / 'skills').glob('*/SKILL.md'))
                self.assertEqual(len(skills), 11)
                for path in skills:
                    text = path.read_text(encoding='utf-8')
                    self.assertTrue(text.startswith('---\n'), path)
                    _, frontmatter, body = text.split('---', 2)
                    meta = yaml.safe_load(frontmatter)
                    self.assertEqual(set(meta), {'name', 'description'}, path)
                    self.assertEqual(meta['name'], path.parent.name)
                    self.assertLessEqual(len(meta['description']), 360, path)
                    self.assertNotIn('§', meta['description'], path)
                    self.assertEqual(re.findall(r'^## (\d+)\.? ', body, re.M), list('123456'), path)
                    for required in ('Times New Roman', '11 pt', 'ausformuliert'):
                        self.assertIn(required.lower(), body.lower(), path)
                for kind in ('werkstatt', 'schnellstart', 'hauptproblem'):
                    md = directory / f'{slug}-{kind}.md'
                    data = md.read_bytes()
                    self.assertTrue(data)
                    self.assertEqual(data, md.with_suffix('.txt').read_bytes(), md)
                    if kind != 'werkstatt':
                        self.assertLessEqual(len(data), 7500, md)
                profile = read_json(ROOT / 'quality/evals' / f'{slug}.json')
                quality_lab.validate_profile(profile, slug, directory, ROOT)
                self.assertEqual(profile['selection']['target_skill'], Path(profile['focus_review']['skill_path']).parent.name)
        # This adjacent workshop was substantively corrected in this round too.
        slug = 'krankenhaus-it-ki'
        quality_lab.validate_profile(read_json(ROOT / 'quality/evals' / f'{slug}.json'), slug, ROOT / slug, ROOT)

    def test_skill_index_generator_uses_individual_component_version(self):
        generator = load_script('generate-skills-md.py')
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / '.claude-plugin').mkdir()
            (root / '.claude-plugin/marketplace.json').write_text(json.dumps({
                'version': '445.33.1',
                'plugins': [{'name': 'normal', 'version': '445.33.1'},
                            {'name': 'komponente', 'version': VERSION}],
            }), encoding='utf-8')
            pages = mock.Mock(return_value='Detailseite\n')
            with mock.patch.multiple(generator, REPO_ROOT=root,
                                     SKILLS_INDEX_DIR=root / 'skills-index',
                                     collect_plugins=mock.Mock(return_value=[('normal', []), ('komponente', [])]),
                                     header=mock.Mock(return_value='Index\n'),
                                     plugin_overview_table=mock.Mock(return_value=''),
                                     plugin_detail_page=pages,
                                     write_detail_index=mock.Mock(return_value='Details\n')):
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(generator.main(), 0)
            self.assertEqual(pages.call_args_list,
                             [mock.call('normal', [], 'v445.33.1'),
                              mock.call('komponente', [], 'v' + VERSION)])
        for slug in self.scope['plugins']:
            text = (ROOT / 'skills-index' / f'{slug}.md').read_text(encoding='utf-8')
            self.assertIn(f'Stand `v{VERSION}`', text, slug)

    def test_official_source_archives(self):
        sources = read_json(QUALITY / 'quellen/quellen.json')
        self.assertEqual(len(sources), 5)
        self.assertEqual(len({s['id'] for s in sources}), 5)
        for source in sources:
            with self.subTest(source=source['id']):
                archive = QUALITY / 'quellen' / source['archiv']
                data = archive.read_bytes()
                if archive.suffix == '.gz':
                    data = gzip.decompress(data)
                    self.assertGreater(len(data), 10000)
                    self.assertRegex(data[:500].lower(), rb'html|doctype')
                else:
                    self.assertTrue(data.startswith(b'%PDF-'))
                self.assertEqual(sha(data), source['sha256'], archive)
                self.assertEqual(source['abgerufen'], '2026-10-09')
                self.assertTrue(source['url'].startswith('https://'))

    def test_nine_cases_native_selection_mime_and_formula_caches(self):
        total_attachments = 0
        for slug in self.scope['cases']:
            with self.subTest(case=slug):
                directory = ROOT / 'testakten' / slug
                raw = {p for p in directory.iterdir() if p.is_file() and re.match(r'^\d{2}_', p.name)}
                selected = {p for p, _ in working_dump_archive_pairs(directory, include_gesamt_pdf=False)}
                self.assertEqual(len(raw), 12, slug)
                self.assertEqual(raw, selected, f'{slug}: Exportfilter verliert Originale')
                self.assertEqual(Counter(p.suffix for p in raw), FORMATS)
                singles = document_arcname_pairs(directory)
                self.assertEqual(len(singles), 12, slug)
                self.assertEqual({p for p, _ in singles}, raw)
                case_attachments = 0
                for path in sorted(raw):
                    if path.suffix == '.eml':
                        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                        for part in message.walk():
                            self.assertEqual(part.defects, [], path)
                        for header in ('From', 'To', 'Subject', 'Date', 'Message-ID'):
                            self.assertTrue(message[header], f'{path}: {header}')
                        self.assertIsNotNone(parsedate_to_datetime(message['Date']).utcoffset(), path)
                        body = message.get_body(preferencelist=('plain',))
                        self.assertIsNotNone(body, path)
                        self.assertTrue(body.get_content().strip(), path)
                        for _, address in getaddresses([str(message['From']), str(message['To'])]):
                            self.assertTrue(address.endswith('.example'), (path, address))
                        for attachment in message.iter_attachments():
                            name = attachment.get_filename()
                            self.assertTrue(name, path)
                            self.assertEqual(Path(name).name, name, path)
                            target = directory / name
                            self.assertIn(target, raw, (path, name))
                            self.assertEqual(attachment.get_content_type(), MIME[target.suffix], (path, name))
                            self.assertEqual(attachment.get_payload(decode=True), target.read_bytes(), (path, name))
                            case_attachments += 1
                    elif path.suffix in ('.docx', '.xlsx'):
                        with zipfile.ZipFile(path) as archive:
                            self.assertIsNone(archive.testzip(), path)
                            if path.suffix == '.xlsx':
                                formulas = 0
                                sheets = [n for n in archive.namelist() if re.fullmatch(r'xl/worksheets/sheet\d+\.xml', n)]
                                self.assertGreaterEqual(len(sheets), 1, path)
                                for sheet in sheets:
                                    xml = ET.fromstring(archive.read(sheet))
                                    for cell in xml.findall('.//s:sheetData/s:row/s:c', NS):
                                        self.assertNotEqual(cell.attrib.get('t'), 'e', (path, sheet, cell.attrib.get('r')))
                                        if cell.find('s:f', NS) is None:
                                            continue
                                        formulas += 1
                                        cached = cell.find('s:v', NS)
                                        self.assertIsNotNone(cached, (path, sheet, cell.attrib.get('r')))
                                        self.assertIsNotNone(cached.text, (path, sheet, cell.attrib.get('r')))
                                        context = (path, sheet, cell.attrib.get('r'))
                                        if cell.attrib.get('t') == 'str':
                                            self.assertNotIn(cached.text, {'#REF!', '#VALUE!', '#DIV/0!', '#NAME?', '#N/A', '#NUM!', '#NULL!'}, context)
                                        elif cell.attrib.get('t') == 'b':
                                            self.assertIn(cached.text, ('0', '1'), context)
                                        else:
                                            self.assertTrue(Decimal(cached.text).is_finite(), context)
                                self.assertGreater(formulas, 0, path)
                    elif path.suffix == '.pdf':
                        self.assert_pdf(path.read_bytes(), str(path.relative_to(ROOT)))
                self.assertGreaterEqual(case_attachments, 2, slug)
                total_attachments += case_attachments
                aggregate = directory / 'gesamt-pdf' / f'{slug}_gesamt.pdf'
                self.assertTrue(aggregate.is_file(), aggregate)
                self.assert_pdf(aggregate.read_bytes(), str(aggregate.relative_to(ROOT)))
        self.assertGreaterEqual(total_attachments, 18)

    def test_eight_handbook_pdfs_and_source_hashes(self):
        records = read_json(QUALITY / 'umfang.json')
        self.assertCountEqual([r['plugin'] for r in records], SPECIALISTS)
        for record in records:
            with self.subTest(plugin=record['plugin']):
                slug = record['plugin']
                self.assertEqual(record['skill_count'], 11)
                self.assertEqual(len(record['skills']), 11)
                for skill in record['skills']:
                    self.assertEqual(sha((ROOT / skill['source']).read_bytes()), skill['source_sha256'], skill['source'])
                handbook = ROOT / 'docs/handbuecher' / f'{slug}-skills-handbuch.pdf'
                self.assertEqual(sha(handbook.read_bytes()), record['handbook_sha256'], handbook)
                reader = self.assert_pdf(handbook.read_bytes(), handbook.name)
                self.assertEqual(len(reader.pages), record['handbook_pages'])
                workshop = record['workshop']
                self.assertEqual(sha((ROOT / workshop['source']).read_bytes()), workshop['source_sha256'], workshop['source'])
                pdf = ROOT / 'docs/handbuecher' / f'{slug}-werkstatt-lesefassung.pdf'
                self.assertEqual(sha(pdf.read_bytes()), workshop['pdf_sha256'], pdf)
                self.assertEqual(len(self.assert_pdf(pdf.read_bytes(), pdf.name).pages), workshop['pages'])

    def test_release_archives_bytes_and_checksums(self):
        if DIST is None:
            self.skipTest('Zusätzliche Paketprüfung mit --dist VERZEICHNIS')
        self.assertTrue(DIST.is_dir(), DIST)
        copies = {SCOPE_PATH.name: SCOPE_PATH}
        expected = {'checksums-sha256.txt', SCOPE_PATH.name}
        for slug in self.scope['plugins']:
            directory = self.release.plugin_directory(slug)
            archive_path = DIST / f'{slug}.zip'
            expected.add(archive_path.name)
            sources = {p.relative_to(directory).as_posix(): p for p in self.release.sources(directory)}
            with self.subTest(plugin_zip=slug), zipfile.ZipFile(archive_path) as archive:
                self.assert_safe_zip(archive, archive_path.name)
                self.assertCountEqual(archive.namelist(), sources)
                self.assertFalse(any(n.endswith(PROMPT_SUFFIXES) for n in archive.namelist()), archive_path.name)
                for name, source in sources.items():
                    self.assertEqual(archive.read(name), source.read_bytes(), (archive_path.name, name))
            for kind in ('werkstatt', 'schnellstart', 'hauptproblem'):
                for ext in ('md', 'txt'):
                    path = directory / f'{slug}-{kind}.{ext}'
                    if path.is_file():
                        copies[path.name] = path
                        expected.add(path.name)
        for slug in self.scope['cases']:
            directory = ROOT / 'testakten' / slug
            aggregate = directory / 'gesamt-pdf' / f'{slug}_gesamt.pdf'
            copies[aggregate.name] = aggregate
            expected.add(aggregate.name)
            originals = working_dump_archive_pairs(directory, include_gesamt_pdf=True)
            singles = document_arcname_pairs(directory)
            self.assertEqual(len(singles), 12, slug)
            for suffix, pairs in (('', originals), ('-einzelpdfs', singles)):
                archive_path = DIST / f'testakte-{slug}{suffix}.zip'
                expected.add(archive_path.name)
                with self.subTest(case_zip=archive_path.name), zipfile.ZipFile(archive_path) as archive:
                    self.assert_safe_zip(archive, archive_path.name)
                    self.assertCountEqual(archive.namelist(), [NOTICE_FILENAME, *(n for _, n in pairs)])
                    self.assertEqual(archive.namelist()[0], NOTICE_FILENAME)
                    self.assertEqual(archive.read(NOTICE_FILENAME), NOTICE_BYTES)
                    for source, name in pairs:
                        data = archive.read(name)
                        if not suffix or source.suffix.lower() == '.pdf':
                            self.assertEqual(data, source.read_bytes(), (archive_path.name, name))
                        if suffix:
                            self.assertTrue(name.lower().endswith('.pdf'))
                            self.assert_pdf(data, f'{archive_path.name}/{name}')
        for slug in SPECIALISTS:
            for suffix in ('skills-handbuch', 'werkstatt-lesefassung'):
                pdf = ROOT / 'docs/handbuecher' / f'{slug}-{suffix}.pdf'
                expected.add(pdf.name)
                copies[pdf.name] = pdf
        self.assertEqual({p.name for p in DIST.iterdir()}, expected, 'Releaseauswahl weicht ab')
        for name, source in copies.items():
            self.assertEqual((DIST / name).read_bytes(), source.read_bytes(), name)
        checksum_names = []
        for line in (DIST / 'checksums-sha256.txt').read_text(encoding='utf-8').splitlines():
            self.assertRegex(line, r'^[a-f0-9]{64}  [^/\\]+$')
            digest, name = line.split('  ', 1)
            checksum_names.append(name)
            self.assertEqual(sha((DIST / name).read_bytes()), digest, name)
        self.assertEqual(len(checksum_names), len(set(checksum_names)), 'Doppelte Prüfsumme')
        self.assertCountEqual(checksum_names, expected - {'checksums-sha256.txt'})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path)
    args, remaining = parser.parse_known_args()
    DIST = args.dist.resolve() if args.dist else None
    unittest.main(argv=[__file__, *remaining])
