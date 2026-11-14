#!/usr/bin/env python3
"""Produktwahl, unveränderte Freigaben und konkrete Aktenkonsistenz prüfen."""
import csv
import importlib.util
import json
import subprocess
import shutil
import sys
import tempfile
import unittest
import zipfile
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from pathlib import Path
from skill_sources import active_owner, fachinhalt_path
from pypdf import PdfReader
from ki_kanzlei_release_contract import PRODUCT_SKILLS

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'ki-native-kanzlei'
def owner(slug):
    return active_owner(PLUGIN, slug)
RUN = PLUGIN / 'scripts/mandatslauf.py'
CASES = json.loads((ROOT / 'scripts/ki-kanzlei-produktionsfaelle.json').read_text())


def module(path):
    spec = importlib.util.spec_from_file_location('production_route', path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class ProductionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.akte = self.temp.name
        self.call('init', '--matter-id', 'K-26-1')

    def tearDown(self):
        self.temp.cleanup()

    def call(self, *args):
        return json.loads(subprocess.check_output([sys.executable, str(RUN), *args, '--akte', self.akte], text=True))

    def test_all_ten_routes_are_real_and_read_only(self):
        routes = module(RUN).PRODUCT_SKILLS
        self.assertEqual(set(routes.values()), PRODUCT_SKILLS)
        file = Path(self.akte) / '00_Mandat/mandatslauf.json'
        before = file.read_bytes()
        for product, skill in routes.items():
            with self.subTest(product=product):
                result = self.call('next', '--produkt', product)
                self.assertEqual(result['next_skill'], owner(skill))
                self.assertEqual(result['next_fachmodul'], skill)
                self.assertEqual(result['next_fachinhalt'], fachinhalt_path(PLUGIN / 'skills' / skill / 'SKILL.md').relative_to(PLUGIN).as_posix())
                self.assertFalse(result['external_action_allowed'])
                self.assertTrue((PLUGIN / 'skills' / owner(skill) / 'SKILL.md').is_file())
                self.assertTrue(fachinhalt_path(PLUGIN / 'skills' / skill / 'SKILL.md').is_file())
        self.assertEqual(before, file.read_bytes())

    def test_packaged_mapping_matches_registry_and_all_original_modules(self):
        from ki_kanzlei_release_contract import ACTIVE_SKILL_SLUGS, MODULE_SLUGS
        runtime = module(RUN)
        mapping = json.loads((PLUGIN / 'scripts/fachmodul-routing.json').read_text())
        self.assertEqual(set(mapping['active_skills']), ACTIVE_SKILL_SLUGS)
        self.assertEqual(set(mapping['modules']), MODULE_SLUGS)
        for slug in MODULE_SLUGS:
            with self.subTest(module=slug):
                target = runtime.route_context(slug)
                self.assertEqual(target['skill'], owner(slug))
                self.assertEqual(target['fachmodul'], slug)
                self.assertEqual(PLUGIN / target['fachinhalt'], fachinhalt_path(PLUGIN / 'skills' / slug / 'SKILL.md'))
        with self.assertRaises(runtime.LaufError):
            runtime.route_context('nicht-vorhandenes-fachmodul')

    def test_runtime_routes_without_repository_and_missing_map_changes_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            isolated = Path(folder) / 'plugin'
            shutil.copytree(PLUGIN, isolated)
            script = isolated / 'scripts/mandatslauf.py'
            matter = Path(folder) / 'mandat'
            subprocess.run([sys.executable, str(script), 'init', '--akte', str(matter), '--matter-id', 'ISOLIERT'], check=True, capture_output=True, cwd=folder)
            state = matter / '00_Mandat/mandatslauf.json'
            before = state.read_bytes()
            command = [sys.executable, str(script), 'next', '--akte', str(matter), '--produkt', 'dokument']
            result = json.loads(subprocess.check_output(command, cwd=folder, text=True))
            self.assertTrue((isolated / 'skills' / result['next_skill'] / 'SKILL.md').is_file())
            self.assertTrue((isolated / result['next_fachinhalt']).is_file())
            self.assertEqual(result['next_fachmodul'], 'dokumente-erstellen-formatieren')
            self.assertFalse(result['external_action_allowed'])
            (isolated / 'scripts/fachmodul-routing.json').unlink()
            failed = subprocess.run(command, cwd=folder, capture_output=True, text=True)
            self.assertEqual(failed.returncode, 2)
            self.assertIn('Fachmodul-Routing nicht verfügbar', failed.stderr)
            self.assertEqual(before, state.read_bytes())

    def test_deadline_gate_takes_priority_over_product(self):
        self.call('gate', '--gate', 'G2', '--aktion', 'oeffnen', '--bezug', 'Gerichtsverfügung')
        result = self.call('next', '--produkt', 'dokument')
        self.assertEqual(result['next_skill'], owner('fristen-berechnen-ueberwachen'))
        self.assertEqual(result['requested_product_skill'], owner('dokumente-erstellen-formatieren'))
        self.assertEqual(result['requested_product_fachmodul'], 'dokumente-erstellen-formatieren')
        self.assertEqual(result['next_fachmodul'], 'fristen-berechnen-ueberwachen')
        self.assertEqual(result['open_gates'], ['G2'])
        self.assertFalse(result['external_action_allowed'])

    def test_no_product_bypasses_dispatch_gate(self):
        self.call('gate', '--gate', 'G3', '--aktion', 'oeffnen', '--bezug', 'Ausgangsentwurf')
        for product in module(RUN).PRODUCT_SKILLS:
            result = self.call('next', '--produkt', product)
            self.assertEqual(result['next_skill'], owner('bea-anlagen-vorbereiten'))
            self.assertFalse(result['external_action_allowed'])

    def test_invalid_route_changes_nothing(self):
        file = Path(self.akte) / '00_Mandat/mandatslauf.json'
        before = file.read_bytes()
        result = subprocess.run([sys.executable, str(RUN), 'next', '--akte', self.akte, '--produkt', 'sofort-senden'], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(before, file.read_bytes())

    def test_new_sources_are_native_complete_and_not_answers(self):
        for case in CASES:
            folder = ROOT / 'testakten' / case['slug']
            self.assertEqual(len(case['documents']), 10)
            for item in case['documents']:
                path = folder / item['file']
                self.assertTrue(path.is_file(), str(path))
                self.assertGreater(path.stat().st_size, 200)
                self.assertNotIn(path.suffix, {'.md', '.json', '.yaml'})
                if path.suffix == '.eml':
                    msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                    for field in ['From', 'To', 'Date', 'Subject', 'Message-ID', 'MIME-Version']:
                        self.assertTrue(msg[field], (path, field))
                    self.assertEqual(msg.get_body(preferencelist=('plain',)).get_content().replace('\r\n', '\n').strip(), item['body'].strip())
                if path.suffix == '.csv':
                    with path.open(newline='') as handle:
                        rows = list(csv.reader(handle, delimiter=';'))
                    self.assertGreaterEqual(len(rows), 5)
                    self.assertEqual(rows, item['rows'])
                    self.assertTrue(all(len(r) == len(rows[0]) for r in rows))
                if path.suffix == '.docx':
                    with zipfile.ZipFile(path) as archive:
                        self.assertIn('word/document.xml', archive.namelist())
                if path.suffix == '.pdf':
                    text = ''.join(p.extract_text() for p in PdfReader(path).pages)
                    self.assertIn(item['title'], text)
                    self.assertNotIn('This test case file', text)

    def test_specific_amounts_and_dates(self):
        rows = CASES[0]['documents'][8]['rows'][1:]
        balance = sum(Decimal(r[2]) - Decimal(r[3]) for r in rows)
        self.assertEqual(balance, Decimal('8090'))
        rows = CASES[2]['documents'][5]['rows'][1:]
        self.assertEqual(sum(Decimal(r[3]) for r in rows), Decimal('-12000'))
        roles = CASES[1]['documents'][7]['rows'][1:]
        self.assertEqual(sum(int(r[2]) for r in roles), 40)
        for case in CASES:
            for item in case['documents']:
                body = item.get('body', '')
                if isinstance(body, list):
                    body = '\n'.join(body)
                self.assertNotIn('§', body)
                for forbidden in ['Lösungsmatrix', 'Musterlösung', 'Arbeitsauftrag für das System']:
                    self.assertNotIn(forbidden, body)


if __name__ == '__main__':
    unittest.main()
