#!/usr/bin/env python3
"""Prüft optionale Codex-Manifeste durch den echten Marketplace-Validator."""
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / 'scripts/validate-marketplace-import.mjs'
SLUG = 'manifest-testfall'
VERSION = '1.2.3'


class CodexManifestAbgleich(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.plugin = self.root / SLUG
        self.codex = self.plugin / '.codex-plugin/plugin.json'
        self.claude = self.plugin / '.claude-plugin/plugin.json'
        self.node = shutil.which('node')
        self.assertIsNotNone(self.node, 'Node.js ist für den Marketplace-Validator erforderlich.')
        manifest = {'name': SLUG, 'version': VERSION, 'description': 'Prüfplugin für Manifestabgleiche.',
                    'author': {'name': 'Klotzkette', 'email': '39582916+Klotzkette@users.noreply.github.com'}}
        self.schreiben(self.claude, json.dumps(manifest))
        self.schreiben(self.root / '.claude-plugin/marketplace.json', json.dumps({
            'name': 'test-marketplace', 'description': 'Isolierter Marketplace für Regressionstests.',
            'version': VERSION, 'plugins': [{'name': SLUG, 'source': './' + SLUG,
                                           'version': VERSION, 'description': manifest['description']}]}))
        self.schreiben(self.plugin / 'skills/manifest-pruefen/SKILL.md',
                       '---\nname: manifest-pruefen\ndescription: Prüft den Abgleich der Metadaten eines isolierten Testplugins mit seinem Marketplace und seinen Manifesten.\n---\n# Manifest prüfen\n')
        self.schreiben(self.plugin / f'{SLUG}-werkstatt.md', '# Werkstatt\n\n## 1 Prüfung\n\nDen Metadatenbestand prüfen.\n')
        self.schreiben(self.plugin / f'{SLUG}-schnellstart.md', '# Schnellstart\n\nDen Metadatenbestand prüfen.\n')
        base = 'https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path='
        self.schreiben(self.plugin / 'README.md', '\n'.join([
            '# Testplugin', f'**Version:** {VERSION}',
            f'[Werkstatt]({base}{SLUG}/{SLUG}-werkstatt.md)',
            f'[Schnellstart]({base}{SLUG}/{SLUG}-schnellstart.md)']))

    def schreiben(self, file, content):
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding='utf-8')

    def pruefen(self):
        return subprocess.run([self.node, str(VALIDATOR)], cwd=self.root,
                              capture_output=True, text=True, timeout=15)

    def test_codex_manifest_bleibt_optional_und_passende_version_besteht(self):
        result = self.pruefen()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.schreiben(self.codex, json.dumps({'name': SLUG, 'version': VERSION}))
        result = self.pruefen()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_veraltete_version_falscher_name_und_fehlende_felder_scheitern(self):
        faelle = [({'name': SLUG, 'version': '1.2.2'}, 'Version'),
                  ({'name': 'anderes-plugin', 'version': VERSION}, 'name'),
                  ({'name': SLUG}, 'Version'), ({'version': VERSION}, 'name')]
        for manifest, meldung in faelle:
            with self.subTest(manifest=manifest):
                self.schreiben(self.codex, json.dumps(manifest))
                result = self.pruefen()
                self.assertEqual(result.returncode, 1)
                self.assertIn(f'{SLUG}/.codex-plugin/plugin.json: {meldung}', result.stderr)

    def test_abweichung_zum_claude_manifest_wird_gemeldet(self):
        self.schreiben(self.codex, json.dumps({'name': SLUG, 'version': VERSION}))
        claude = json.loads(self.claude.read_text())
        claude['version'] = '1.2.2'
        self.schreiben(self.claude, json.dumps(claude))
        result = self.pruefen()
        self.assertEqual(result.returncode, 1)
        self.assertIn('.codex-plugin/plugin.json: Version', result.stderr)
        self.assertIn('.claude-plugin/plugin.json: Version', result.stderr)

    def test_unlesbares_oder_nicht_objektfoermiges_manifest_scheitert(self):
        for raw in ['{', 'null', '[]', '"kein Manifest"']:
            with self.subTest(raw=raw):
                self.schreiben(self.codex, raw)
                result = self.pruefen()
                self.assertEqual(result.returncode, 1)
                self.assertIn('.codex-plugin/plugin.json:', result.stderr)

    def test_komponentenversion_braucht_exakten_pin_und_identische_manifeste(self):
        version = '1.2.7'
        marketplace_path = self.root / '.claude-plugin/marketplace.json'
        marketplace = json.loads(marketplace_path.read_text())
        marketplace['plugins'][0]['version'] = version
        self.schreiben(marketplace_path, json.dumps(marketplace))
        manifest = json.loads(self.claude.read_text())
        manifest['version'] = version
        self.schreiben(self.claude, json.dumps(manifest))
        self.schreiben(self.codex, json.dumps({'name': SLUG, 'version': version}))
        readme = self.plugin / 'README.md'
        self.schreiben(readme, readme.read_text().replace(VERSION, version))
        config = self.root / 'scripts/scoped-release-assets.json'
        for assets, expected in [
            ({}, 1),
            ({SLUG + '.zip': 'paket-v1.2.6'}, 1),
            ({'anderes-plugin.zip': 'paket-v1.2.7'}, 1),
            ({SLUG + '.zip': 'paket-v1.2.7'}, 0),
        ]:
            with self.subTest(assets=assets):
                self.schreiben(config, json.dumps({'schema_version': 1, 'assets': assets}))
                result = self.pruefen()
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        self.schreiben(self.codex, json.dumps({'name': SLUG, 'version': VERSION}))
        result = self.pruefen()
        self.assertEqual(result.returncode, 1)
        self.assertIn('.codex-plugin/plugin.json: Version', result.stderr)

    def bundle_nachweis(self):
        marketplace_path = self.root / '.claude-plugin/marketplace.json'
        marketplace = json.loads(marketplace_path.read_text())
        marketplace['version'] = '9.0.0'
        self.schreiben(marketplace_path, json.dumps(marketplace))
        asset = SLUG + '.zip'
        tag = 'fachbundle-v1.2.7'
        digest = 'a' * 64
        config_path = self.root / 'scripts/scoped-release-package-versions.json'
        evidence_path = self.root / 'quality/fachbundle/pakete.json'
        config = {'schema_version': 1, 'assets': {asset: {
            'tag': tag, 'version': VERSION, 'sha256': digest,
            'evidence': evidence_path.relative_to(self.root).as_posix()}}}
        evidence = {'version': VERSION, 'release': tag,
                    'plugins': [{'name': SLUG, 'skills': 1}], 'assets': {asset: digest}}
        self.schreiben(self.root / 'scripts/scoped-release-assets.json',
                       json.dumps({'schema_version': 1, 'assets': {asset: tag}}))
        self.schreiben(config_path, json.dumps(config))
        self.schreiben(evidence_path, json.dumps(evidence))
        return config_path, config, evidence_path, evidence

    def test_belegte_bundle_version_erlaubt_nur_registrierte_paketversion(self):
        config_path, config, evidence_path, evidence = self.bundle_nachweis()
        result = self.pruefen()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        # Ein in sich stimmiger Nachweis für eine andere Paketversion genügt nicht.
        config['assets'][SLUG + '.zip']['version'] = '1.2.2'
        evidence['version'] = '1.2.2'
        self.schreiben(config_path, json.dumps(config))
        self.schreiben(evidence_path, json.dumps(evidence))
        result = self.pruefen()
        self.assertEqual(result.returncode, 1)
        self.assertIn(f'Marketplace:{SLUG}: Version', result.stderr)
        self.bundle_nachweis()
        # Auch mit Nachweis müssen die lokalen Manifeste übereinstimmen.
        self.schreiben(self.codex, json.dumps({'name': SLUG, 'version': '1.2.7'}))
        result = self.pruefen()
        self.assertEqual(result.returncode, 1)
        self.assertIn('.codex-plugin/plugin.json: Version', result.stderr)

    def test_bundle_nachweis_abweichungen_bleiben_fehler(self):
        for field, value in [('tag', 'anderes-bundle-v1.2.7'), ('version', '1.2.2'),
                             ('sha256', 'b' * 64), ('sha256', 'kein-hash')]:
            with self.subTest(registrierung=field, wert=value):
                config_path, config, _, _ = self.bundle_nachweis()
                config['assets'][SLUG + '.zip'][field] = value
                self.schreiben(config_path, json.dumps(config))
                result = self.pruefen()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for field, value in [('version', '1.2.2'), ('release', 'anderes-bundle-v1.2.7'),
                             ('assets', {SLUG + '.zip': 'b' * 64}),
                             ('assets', {'anderes-plugin.zip': 'a' * 64}),
                             ('plugins', [{'name': 'anderes-plugin'}]), ('plugins', None)]:
            with self.subTest(nachweis=field, wert=value):
                _, _, evidence_path, evidence = self.bundle_nachweis()
                evidence[field] = value
                self.schreiben(evidence_path, json.dumps(evidence))
                result = self.pruefen()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        config_path, config, _, _ = self.bundle_nachweis()
        config['assets']['anderes-plugin.zip'] = config['assets'].pop(SLUG + '.zip')
        self.schreiben(config_path, json.dumps(config))
        result = self.pruefen()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        config_path, config, _, _ = self.bundle_nachweis()
        self.schreiben(self.root / 'scripts/scoped-release-assets.json', json.dumps({
            'schema_version': 1, 'assets': {SLUG + '.zip': 'anderes-bundle-v1.2.7'}}))
        result = self.pruefen()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_bundle_registrierung_und_nachweispfad_muessen_gueltig_sein(self):
        for value in [None, [], {'schema_version': 2, 'assets': {}},
                      {'schema_version': 1, 'assets': []}]:
            with self.subTest(schema=value):
                config_path, _, _, _ = self.bundle_nachweis()
                self.schreiben(config_path, json.dumps(value))
                result = self.pruefen()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for evidence in ['quality/fachbundle/../fachbundle/pakete.json',
                         'quality/./fachbundle/pakete.json', 'quality//fachbundle/pakete.json',
                         'scripts/../quality/fachbundle/pakete.json',
                         '/quality/fachbundle/pakete.json', 'quality\\fachbundle\\pakete.json',
                         'quality/fachbundle/fehlt.json']:
            with self.subTest(pfad=evidence):
                config_path, config, _, _ = self.bundle_nachweis()
                config['assets'][SLUG + '.zip']['evidence'] = evidence
                self.schreiben(config_path, json.dumps(config))
                result = self.pruefen()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        config_path, config, evidence_path, evidence = self.bundle_nachweis()
        self.schreiben(self.root / 'anderer-nachweis.json', json.dumps(evidence))
        evidence_path.unlink()
        evidence_path.symlink_to(self.root / 'anderer-nachweis.json')
        result = self.pruefen()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
