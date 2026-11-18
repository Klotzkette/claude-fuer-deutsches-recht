#!/usr/bin/env python3
"""Prüft Quellenpaket, eigenständige Prompts und bytegenaue Release-Zuordnung."""
from __future__ import annotations
import argparse
import copy
from contextlib import contextmanager
from datetime import date, datetime
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote
import zipfile
from docx import Document
from openpyxl import load_workbook
from pypdf import PdfReader
import yaml
from quality_lab import validate_profile
from release_routing import validate_plugin_version

ROOT = Path(__file__).resolve().parents[1]
NAME = 'insolvenzanfechtung'
PARENT = 'fachanwalt-insolvenz-sanierungsrecht'
DIST = None
COMPONENT_SCOPE = 'scripts/data/insolvenzanfechtung-pruefumfang.json'
COMPONENT_VERSION = '445.36.2'
COMPONENT_TAG = 'qualitaetsrunde-v445.36.2'
VEEDELWENDE_CASES = (
    'insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln',
    'insolvenzanfechtung-veedelwende-zession-koeln',
)


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT/'scripts'/filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(text):
    return re.sub(r'\s+', ' ', text).strip()


def document_text(path):
    if path.suffix == '.docx':
        return '\n'.join(paragraph.text for paragraph in Document(path).paragraphs)
    if path.suffix == '.pdf':
        return '\n'.join(page.extract_text() or '' for page in PdfReader(path).pages)
    if path.suffix == '.eml':
        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        body = message.get_body(preferencelist=('plain',))
        if body is None:
            raise AssertionError(f'Keine Textfassung in {path}')
        return body.get_content()
    if path.suffix == '.txt':
        return path.read_text(encoding='utf-8')
    if path.suffix == '.xlsx':
        workbook = load_workbook(path, data_only=False, read_only=True)
        try:
            return '\n'.join(
                str(cell.value)
                for sheet in workbook.worksheets
                for row in sheet.iter_rows()
                for cell in row
                if cell.value is not None
            )
        finally:
            workbook.close()
    raise ValueError(f'Kein Textleser für {path}')


def veedelwende_cases():
    cases = json.loads((ROOT/'scripts/data/insolvenzanfechtung-akten.json').read_text(encoding='utf-8'))
    return {case['slug']: case for case in cases if case['slug'] in VEEDELWENDE_CASES}


def case_items(case):
    return {item['name']: item for item in case['files']}


@contextmanager
def historical_component_fixture(source_root=ROOT):
    """Den erhaltenen Komponentenstand prüfen, ohne heutige Produktpins umzudeuten."""
    original_scope = json.loads((source_root/COMPONENT_SCOPE).read_text())
    with tempfile.TemporaryDirectory(prefix='anfechtung-komponentenstand-') as folder:
        root = Path(folder)
        (root/'.claude-plugin').mkdir()
        (root/'scripts').mkdir()
        (root/NAME).mkdir()
        market = {
            'version': COMPONENT_VERSION,
            'plugins': [{'name': NAME, 'version': COMPONENT_VERSION, 'source': f'./{NAME}'}],
        }
        (root/'.claude-plugin/marketplace.json').write_text(json.dumps(market))
        pins = {'schema_version': 1, 'assets': {
            f'{NAME}.zip': COMPONENT_TAG,
            f'{NAME}-portable.zip': COMPONENT_TAG,
        }}
        (root/'scripts/scoped-release-assets.json').write_text(json.dumps(pins))
        for filename in original_scope['plugins'][0]['prompts']:
            shutil.copyfile(source_root/NAME/filename, root/NAME/filename)
        for asset in original_scope['additional_assets']:
            for field in ('source', 'evidence'):
                relative = asset[field]
                target = root/relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source_root/relative, target)
        yield root


def validate_component_scope(scope, root=ROOT):
    """Fester Komponentenstand; spätere Qualitätsrunden sind kein Identitätsbeleg."""
    if scope.get('version') != COMPONENT_VERSION or scope.get('tag') != COMPONENT_TAG:
        raise ValueError('Unbekannter Insolvenzanfechtungs-Komponentenstand')
    plugins = scope.get('plugins')
    if not isinstance(plugins, list) or len(plugins) != 1 or plugins[0].get('name') != NAME:
        raise ValueError('Prüfumfang muss ausschließlich Insolvenzanfechtung enthalten')
    expected_prompts = {f'{NAME}-{kind}.{ext}' for kind in ('werkstatt', 'schnellstart', 'hauptproblem')
                        for ext in ('md', 'txt')}
    if plugins[0].get('variants') != ['native', 'portable'] or set(plugins[0].get('prompts', [])) != expected_prompts:
        raise ValueError('Native und portable Variante sowie sechs Promptdateien erforderlich')
    # Die echte Scopeprüfung kontrolliert exakte historische Pins, Version,
    # vollständige Prompts und das hashgebundene Werkstattpaar in einer isolierten
    # Fixture. Die heutigen Produktrouten dürfen inzwischen weitergezogen sein.
    with historical_component_fixture(root) as fixture:
        entries = module('build-skill-quality-release.py').validate_scope(scope, fixture)
    evidence = json.loads((root/'quality/insolvenzanfechtung/tatbestandswerkstaetten-2026-11-15/umfang.json').read_text())
    if evidence.get('version') != COMPONENT_VERSION or evidence.get('module_count') != 10:
        raise ValueError('Version oder Werkstattumfang passt nicht zum erhaltenen Nachweis')
    release_note = (root/'docs/releases'/f'{COMPONENT_TAG}.md').read_text()
    expected_url = f'https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{COMPONENT_TAG}/{NAME}.zip'
    if expected_url not in release_note:
        raise ValueError('Komponentenidentität fehlt in der zugehörigen Release-Dokumentation')
    return entries[NAME]['version']


class AnfechtungTest(unittest.TestCase):
    def test_eleven_skills_are_activatable_and_references_resolve(self):
        skills = sorted((ROOT/NAME/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills), 11)
        for path in skills:
            text = path.read_text(encoding='utf-8')
            front = yaml.safe_load(text.split('---', 2)[1])
            self.assertEqual(set(front), {'name', 'description'})
            self.assertEqual(front['name'], path.parent.name)
            self.assertLessEqual(len(front['description']), 360)
            self.assertNotIn('§', front['description'])
            self.assertNotIn('im Plugin', front['description'])
            self.assertEqual(re.findall(r'^## ([1-6])\.', text, re.M), list('123456'))
            for word in ('Times New Roman', '11 pt', 'ausformuliert'):
                self.assertIn(word, text)
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('https:', 'http:', '#', 'mailto:')):
                    continue
                target = unquote(target.split('#')[0])
                self.assertTrue((path.parent/target).resolve().exists(), f'{path}: {target}')

    def test_prompts_are_separate_complete_and_bounded(self):
        builder = module('build-insolvenzanfechtung-release.py')
        for source in builder.prompt_sources():
            self.assertEqual(source.read_bytes(), source.with_suffix('.txt').read_bytes())
            data = source.read_bytes().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
            if 'werkstatt' not in source.name:
                self.assertLessEqual(len(data), 7500, source)
            else:
                self.assertGreater(len(source.read_text().split()), 6000)
            self.assertIn('Trägt nicht', source.read_text())
        profile = json.loads((ROOT/'quality/evals'/f'{NAME}.json').read_text())
        validate_profile(profile, NAME, ROOT/NAME)
        self.assertEqual(len(profile['sources']), 15)
        self.assertTrue(any('KORE313232026' in source['url'] for source in profile['sources']))
        self.assertEqual(len(profile['cases']), 5)

    def test_section_135_and_assignment_anchors_are_present(self):
        skill = (ROOT/NAME/'skills/gesellschafterfinanzierung/SKILL.md').read_text()
        workshop = (ROOT/NAME/f'{NAME}-werkstatt.md').read_text()
        sources = (ROOT/NAME/'references/rechtsquellen.md').read_text()
        for anchor in ('IX ZR 196/13', 'IX ZR 32/12', 'IX ZR 173/23'):
            self.assertIn(anchor, skill)
            self.assertIn(anchor, workshop)
            self.assertIn(anchor, sources)
        self.assertIn('objektive Gläubigerbenachteiligung', skill)
        self.assertIn('keine zeitlich unbegrenzte', sources)
        self.assertIn('Treuhand', workshop)

    def test_veedelwende_case_files_match_the_scoped_data(self):
        cases = veedelwende_cases()
        self.assertEqual(set(cases), set(VEEDELWENDE_CASES))
        original_suffixes = {'.docx', '.pdf', '.xlsx', '.eml', '.txt'}
        for slug, case in cases.items():
            items = case['files']
            self.assertEqual(len(items), 24, slug)
            expected = {item['name'] for item in items}
            self.assertEqual(len(expected), 24, slug)
            directory = ROOT/'testakten'/slug
            actual = {path.name for path in directory.iterdir()
                      if path.is_file() and path.suffix in original_suffixes}
            self.assertEqual(actual, expected, slug)
            for item in items:
                path = directory/item['name']
                self.assertGreater(path.stat().st_size, 0, path)
                if item.get('body'):
                    self.assertIn(compact(item['body']), compact(document_text(path)), path)
                elif path.suffix == '.xlsx':
                    text = document_text(path)
                    self.assertIn(item['title'], text, path)
                    for value in (value for row in item['rows'] for value in row):
                        self.assertIn(str(value), text, path)

    def test_veedelwende_direct_case_keeps_exact_facts_and_clean_complaint(self):
        case = veedelwende_cases()[VEEDELWENDE_CASES[0]]
        items = case_items(case)
        self.assertEqual(
            {name: items[name]['date'] for name in (
                '02_Insolvenzantrag_Eingang.pdf',
                '05_Darlehensvertrag_Haderlein.docx',
                '13_Kontoauszug_Rueckzahlung.pdf',
                '21_Klageschrift.docx',
            )},
            {
                '02_Insolvenzantrag_Eingang.pdf': '03.06.2026',
                '05_Darlehensvertrag_Haderlein.docx': '12.06.2024',
                '13_Kontoauszug_Rueckzahlung.pdf': '04.02.2026',
                '21_Klageschrift.docx': '15.09.2026',
            },
        )
        directory = ROOT/'testakten'/case['slug']
        for filename, facts in {
            '02_Insolvenzantrag_Eingang.pdf': ('3. Juni 2026',),
            '05_Darlehensvertrag_Haderlein.docx': ('150.000,00 EUR',),
            '13_Kontoauszug_Rueckzahlung.pdf': ('150.000,00 EUR', '3. Februar 2026'),
        }.items():
            text = document_text(directory/filename)
            for fact in facts:
                self.assertIn(fact, text, filename)

        complaint = document_text(directory/'21_Klageschrift.docx')
        for fact in ('150.000,00 EUR', '3. Februar 2026', '3. Juni 2026',
                     'IX ZR 196/13', 'IX ZR 44/22', 'Nala Seifert'):
            self.assertIn(fact, complaint)
        self.assertNotRegex(complaint, r'(?i)\bTilda\b|\b40\s*k\b|\b40[.\s]?000(?:,00)?\b')

    def test_veedelwende_assignment_case_exposes_timing_and_litigation_risk(self):
        case = veedelwende_cases()[VEEDELWENDE_CASES[1]]
        items = case_items(case)
        self.assertEqual(items['07_Kauf_Abtretung.docx']['date'], '03.12.2024')
        self.assertEqual(items['08_Kaufpreiszahlung_Quast.pdf']['date'], '06.12.2024')
        self.assertEqual(items['09_Abtretungsanzeige.eml']['date'], '2024-12-07T10:17:00+01:00')
        purchase_date = datetime.strptime(items['08_Kaufpreiszahlung_Quast.pdf']['date'], '%d.%m.%Y').date()
        notice_date = datetime.fromisoformat(items['09_Abtretungsanzeige.eml']['date']).date()
        self.assertEqual((purchase_date, notice_date), (date(2024, 12, 6), date(2024, 12, 7)))
        self.assertLess(purchase_date, notice_date)

        directory = ROOT/'testakten'/case['slug']
        purchase = document_text(directory/'08_Kaufpreiszahlung_Quast.pdf')
        self.assertIn('48.000,00 EUR', purchase)
        self.assertIn('6. Dezember 2024', purchase)
        notice = BytesParser(policy=policy.default).parsebytes(
            (directory/'09_Abtretungsanzeige.eml').read_bytes()
        )
        self.assertEqual(parsedate_to_datetime(str(notice['Date'])).date(), date(2024, 12, 7))
        repayment = document_text(directory/'12_Kontoauszug_Rueckzahlung.pdf')
        for fact in ('96.000,00 EUR', '3. April 2026', '3. Juni 2026'):
            self.assertIn(fact, repayment)

        texts = {
            'Risikomemo': document_text(directory/'21_Risikomemo_BGH.docx'),
            'Klage': document_text(directory/'22_Klageschrift.docx'),
            'Klageerwiderung': document_text(directory/'24_Klageerwiderung.docx'),
        }
        for label, text in texts.items():
            for fact in ('IX ZR 32/12', 'IX ZR 173/23', '18 Monate', '17. April 2026'):
                self.assertIn(fact, text, label)
            self.assertRegex(text, r'(?i)(vier Wochen|vierwöchig|Vierwochenfrist)', label)
        self.assertIn('offen risikobehafteter Versuch', texts['Risikomemo'])
        self.assertIn('Ohne neue Tatsachen', texts['Risikomemo'])
        self.assertIn('erhebliches Klagerisiko', texts['Klage'])
        self.assertIn('mit einer Klageabweisung zu rechnen', texts['Klage'])
        self.assertIn('Die Klage ist abzuweisen', texts['Klageerwiderung'])

    def test_veedelwende_email_attachments_are_byte_exact(self):
        for slug, case in veedelwende_cases().items():
            directory = ROOT/'testakten'/slug
            for item in case['files']:
                if not item.get('attachments'):
                    continue
                message = BytesParser(policy=policy.default).parsebytes(
                    (directory/item['name']).read_bytes()
                )
                attachments = [
                    (part.get_filename(), part.get_payload(decode=True))
                    for part in message.iter_attachments()
                ]
                self.assertEqual([name for name, _ in attachments], item['attachments'], item['name'])
                for name, payload in attachments:
                    self.assertEqual(payload, (directory/name).read_bytes(), f'{item["name"]}: {name}')

    def test_manifests_and_marketplace_agree(self):
        market = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
        for name in (NAME, PARENT):
            entries = [p for p in market['plugins'] if p['name'] == name]
            self.assertEqual(len(entries), 1)
            validate_plugin_version(entries[0], market['version'], root=ROOT)
            version = entries[0]['version']
            if name == NAME:
                if version == COMPONENT_VERSION:
                    scope = json.loads((ROOT/COMPONENT_SCOPE).read_text())
                    self.assertEqual(version, validate_component_scope(scope))
            for relative in (('plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json') if name == NAME else ('.claude-plugin/plugin.json',)):
                manifest = json.loads((ROOT/name/relative).read_text())
                self.assertEqual((manifest['name'], manifest['version']), (name, version))
                self.assertEqual(manifest['description'], entries[0]['description'])

    def test_component_identity_does_not_read_the_latest_quality_bundle(self):
        latest = ROOT/'scripts/data/skill-quality-release-scope.json'
        read_text = Path.read_text

        def independent_read(path, *args, **kwargs):
            if path.resolve() == latest.resolve():
                raise AssertionError('Komponentenprüfung darf keinen wechselnden Latest-Scope lesen')
            return read_text(path, *args, **kwargs)

        with patch.object(Path, 'read_text', independent_read):
            self.test_manifests_and_marketplace_agree()
            scope = json.loads((ROOT/COMPONENT_SCOPE).read_text())
            self.assertEqual(validate_component_scope(scope), COMPONENT_VERSION)

    def test_historical_scope_does_not_read_current_product_routes_or_versions(self):
        forbidden = {
            (ROOT/'scripts/scoped-release-assets.json').resolve(),
            (ROOT/'.claude-plugin/marketplace.json').resolve(),
            (ROOT/'scripts/data/skill-quality-release-scope.json').resolve(),
        }
        read_text = Path.read_text

        def historical_read(path, *args, **kwargs):
            if path.resolve() in forbidden:
                raise AssertionError('Historischer Komponentenstand liest aktuelle Produktrouten')
            return read_text(path, *args, **kwargs)

        scope = json.loads((ROOT/COMPONENT_SCOPE).read_text())
        with patch.object(Path, 'read_text', historical_read):
            self.assertEqual(validate_component_scope(scope), COMPONENT_VERSION)

    def test_historical_fixture_still_checks_exact_routes_and_marketplace_version(self):
        scope = json.loads((ROOT/COMPONENT_SCOPE).read_text())
        builder = module('build-skill-quality-release.py')
        for mutation in ('missing-pin', 'wrong-tag', 'wrong-version'):
            with self.subTest(mutation=mutation), historical_component_fixture() as fixture:
                self.assertEqual(builder.validate_scope(scope, fixture)[NAME]['version'], COMPONENT_VERSION)
                if mutation == 'wrong-version':
                    path = fixture/'.claude-plugin/marketplace.json'
                    market = json.loads(path.read_text())
                    market['version'] = market['plugins'][0]['version'] = '445.36.8'
                    path.write_text(json.dumps(market))
                else:
                    path = fixture/'scripts/scoped-release-assets.json'
                    pins = json.loads(path.read_text())
                    if mutation == 'missing-pin':
                        del pins['assets'][f'{NAME}-portable.zip']
                    else:
                        pins['assets'][f'{NAME}.zip'] = 'qualitaetsrunde-v445.36.8'
                    path.write_text(json.dumps(pins))
                with self.assertRaises(ValueError):
                    builder.validate_scope(scope, fixture)

    def test_component_scope_rejects_wrong_identity_incomplete_assets_and_bad_hash(self):
        valid = json.loads((ROOT/COMPONENT_SCOPE).read_text())
        self.assertEqual(validate_component_scope(valid), COMPONENT_VERSION)
        for change in ('version', 'tag', 'other-plugin', 'portable', 'prompt', 'missing-assets', 'bad-hash'):
            scope = copy.deepcopy(valid)
            if change == 'version':
                scope['version'] = '445.36.5'
                scope['tag'] = 'qualitaetsrunde-v445.36.5'
            elif change == 'tag':
                scope['tag'] = 'fremd-v445.36.2'
            elif change == 'other-plugin':
                scope['plugins'].append({'name': 'bautraegervertrag-pruefer'})
            elif change == 'portable':
                scope['plugins'][0]['variants'] = ['native']
            elif change == 'prompt':
                scope['plugins'][0]['prompts'].pop()
            elif change == 'missing-assets':
                scope.pop('additional_assets')
            else:
                scope['additional_assets'][0]['sha256'] = '0' * 64
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_component_scope(scope)

    def test_release_assets_and_packages_are_byte_exact(self):
        if DIST is None:
            self.skipTest('--dist erforderlich')
        builder = module('build-insolvenzanfechtung-release.py')
        self.assertEqual({p.name for p in DIST.iterdir()}, builder.asset_names())
        lines = (DIST/'checksums-sha256.txt').read_text().splitlines()
        self.assertEqual(len(lines), len(builder.asset_names())-1)
        for line in lines:
            digest, name = line.split('  ', 1)
            self.assertEqual(sha(DIST/name), digest)
        for name in (NAME, PARENT):
            expected = builder.plugin_sources(name)
            for suffix, prefix in (('', ''), ('-portable', name+'/')):
                with zipfile.ZipFile(DIST/(name+suffix+'.zip')) as archive:
                    self.assertIsNone(archive.testzip())
                    self.assertEqual(set(archive.namelist()), {prefix+p for p in expected})
                    for relative, path in expected.items():
                        self.assertEqual(archive.read(prefix+relative), path.read_bytes())
                    for path in archive.namelist():
                        self.assertNotIn('..', Path(path).parts)
                        self.assertFalse(set(Path(path).parts) & {'testakte', 'testakten', 'prompts'})
        record = json.loads((DIST/'quellenabgleich.json').read_text())
        for source in builder.prompt_sources():
            asset = builder.prompt_asset(source)
            self.assertEqual((DIST/asset).read_bytes(), source.read_bytes())
            target = DIST/str(Path(asset).with_suffix('.pdf'))
            result = builder.inspect_pdf(source, target)
            for key, value in result.items():
                self.assertEqual(record['pdfs'][target.name][key], value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path)
    args, remaining = parser.parse_known_args()
    DIST = args.dist.resolve() if args.dist else None
    unittest.main(argv=[__file__, *remaining])
