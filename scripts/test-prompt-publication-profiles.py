#!/usr/bin/env python3
"""Regressionsschutz: ein Werkstatt-Prompt, keine still erzeugten Nebenvarianten."""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

import prompt_profiles as publication
import quality_lab as lab

SCRIPTS = Path(__file__).resolve().parent


def module(stem):
    spec = importlib.util.spec_from_file_location(stem.replace('-', '_'), SCRIPTS / f'{stem}.py')
    loaded = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = loaded
    spec.loader.exec_module(loaded)
    return loaded


G = module('generate-werkstatt-und-schnellstart-prompts')
MEGA = module('generate-megaprompt')
REFINE = module('refine-speed-and-elegance')
COVERAGE = module('generate-werkstatt-und-schnellstart-coverage')
QUICK = module('audit-quickstart-usability')
ROUTING = module('audit-prompt-profile-routing')
HYGIENE = module('audit-generated-prompt-hygiene')
PACKAGING = module('validate-prompt-packaging')
RELEASE = module('validate-release-zips')
INDEX = module('generate-skills-md')
DIRECT = module('inject-direkt-loslegen-section')


class PromptPublicationProfiles(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.slug = 'bea-versand'
        self.plugin = self.root / self.slug
        (self.plugin / '.claude-plugin').mkdir(parents=True)
        self.entry = {'name': self.slug, 'source': f'./{self.slug}', 'description': 'Ein Versandvorgang.'}
        (self.plugin / '.claude-plugin/plugin.json').write_text(json.dumps(self.entry))
        (self.plugin / 'skills/bea-anlagen-versand').mkdir(parents=True)
        (self.plugin / 'skills/bea-anlagen-versand/SKILL.md').write_text('Ein einzelner Skill.')
        (self.plugin / 'README.md').write_text('# bea-Versand\n')
        self.prompt = self.plugin / f'{self.slug}-werkstatt.md'
        self.prompt.write_text('# Werkstatt\n\n## 1. Versandauftrag\n\nUnterlagen zuerst lesen.\n')
        publication.sync_text_copies(self.plugin, self.slug)
        (self.root / '.claude-plugin').mkdir()
        self.market = self.root / '.claude-plugin/marketplace.json'
        self.market.write_text(json.dumps({'plugins': [self.entry], 'version': '1.0.0'}))

    def profile(self):
        return {
            'schema_version': 1, 'plugin': self.slug, 'reviewed_on': '2026-09-28',
            'workshop_review': {'verdict': 'retained', 'reason': 'Auftrag, Bearbeitung und Übergabe wurden geprüft.',
                                'changes': [], 'sha256': hashlib.sha256(self.prompt.read_bytes()).hexdigest()},
            'selection': {'positive': ['Anlagen für das Gericht aufbereiten', 'Versandmappe prüfen'],
                          'negative': ['Eine Klage juristisch entwerfen', 'Einen Kaufvertrag schreiben']},
            'sources': [],
            'cases': [{'id': 'anlagenmappe', 'target_skill': 'bea-anlagen-versand',
                       'request': 'Ein bereits fertiggestellter Schriftsatz benennt drei Anlagen. Zwei liegen als PDF und eine als gescanntes Dokument vor. Bereiten Sie daraus eine nachvollziehbare Versandmappe vor und benennen Sie ungelöste Dateifehler.',
                       'input_files': [], 'deliverables': ['pruefung.txt'],
                       'criteria': [{'id': f'c{i}', 'text': f'Fachliches Kriterium {i} am Arbeitsergebnis prüfen.', 'deliverables': ['pruefung.txt']} for i in range(3)]}],
        }

    def test_defaults_and_explicit_profile_match_in_python_and_javascript(self):
        self.assertEqual(publication.standalone_kinds('anderes-plugin'), ('werkstatt', 'schnellstart'))
        self.assertTrue(publication.enabled('anderes-plugin', 'hauptproblem'))
        self.assertTrue(publication.enabled('anderes-plugin', 'megaprompt'))
        self.assertEqual(publication.formats('anderes-plugin'), ('md',))
        script = "import {promptKinds,promptFormats,promptEnabled} from './scripts/prompt-profiles.mjs'; console.log(JSON.stringify(['bea-versand','anderes-plugin'].map(s=>[promptKinds(s),promptFormats(s),promptEnabled(s,'megaprompt'),promptEnabled(s,'hauptproblem')])));"
        actual = json.loads(subprocess.check_output(['node', '--input-type=module', '-e', script], cwd=SCRIPTS.parent, text=True))
        expected = [[list(publication.standalone_kinds(s)), list(publication.formats(s)), publication.enabled(s, 'megaprompt'), publication.enabled(s, 'hauptproblem')] for s in (self.slug, 'anderes-plugin')]
        self.assertEqual(actual, expected)

    def test_generator_preserves_curated_bytes_and_syncs_only_txt_idempotently(self):
        before = self.prompt.read_bytes()
        (self.plugin / f'{self.slug}-werkstatt.txt').unlink()
        with patch.object(G, 'REPO', self.root), patch.object(G, 'plugin_dirs', return_value=[self.plugin]), patch.object(G, 'collect_skill_material', side_effect=AssertionError('Handkuratierten Prompt nicht regenerieren')), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(G.main(), 0)
            self.assertEqual(G.main(), 0)
        self.assertEqual(self.prompt.read_bytes(), before)
        self.assertEqual((self.plugin / f'{self.slug}-werkstatt.txt').read_bytes(), before)
        self.assertEqual({p.name for p in self.plugin.glob('*-*.md')}, {self.prompt.name})
        self.assertIsNone(MEGA.build_megaprompt(self.plugin))
        with patch.object(REFINE, 'REPO', self.root):
            self.assertFalse(REFINE.refine_prompt(self.prompt, 'werkstatt'))

    def test_ordinary_generator_still_writes_both_markdown_prompts(self):
        ordinary = self.root / 'anderes-plugin'
        (ordinary / '.claude-plugin').mkdir(parents=True)
        (ordinary / '.claude-plugin/plugin.json').write_text('{"name":"anderes-plugin"}')
        with patch.object(G, 'REPO', self.root), patch.object(G, 'plugin_dirs', return_value=[ordinary]), patch.object(G, 'collect_skill_material', return_value=[]), patch.object(G, 'build_werkstatt', return_value='Werkstatt\n'), patch.object(G, 'build_schnellstart', return_value='Schnellstart\n'), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(G.main(), 0)
        self.assertEqual((ordinary / 'anderes-plugin-werkstatt.md').read_text(), 'Werkstatt\n')
        self.assertEqual((ordinary / 'anderes-plugin-schnellstart.md').read_text(), 'Schnellstart\n')
        self.assertFalse(list(ordinary.glob('*.txt')))

    def test_prohibited_variants_and_word_pdf_derivatives_are_rejected(self):
        self.assertEqual(publication.validate_files(self.plugin, self.slug, self.root), [])
        for suffix in ('schnellstart.md', 'hauptproblem.md', 'werkstatt.docx', 'werkstatt.pdf'):
            with self.subTest(suffix=suffix):
                path = self.plugin / f'{self.slug}-{suffix}'
                path.write_bytes(b'Unzulassige Nebenvariante')
                self.assertTrue(publication.validate_files(self.plugin, self.slug, self.root))
                path.unlink()
        mega = self.root / 'testakten/megaprompts' / f'{self.slug}.md'
        mega.parent.mkdir(parents=True)
        mega.write_text('Nicht vorgesehen')
        self.assertTrue(publication.validate_files(self.plugin, self.slug, self.root))

    def test_txt_drift_and_missing_workshop_review_fail_quality_validation(self):
        profile = self.profile()
        lab.validate_profile(profile, self.slug, self.plugin, self.root)
        del profile['workshop_review']
        with self.assertRaises(lab.LabError):
            lab.validate_profile(profile, self.slug, self.plugin, self.root)
        profile = self.profile()
        (self.plugin / f'{self.slug}-werkstatt.txt').write_text('Veraltet')
        with self.assertRaisesRegex(lab.LabError, 'byteidentisch'):
            lab.validate_profile(profile, self.slug, self.plugin, self.root)

    def test_editorial_review_needs_only_enabled_workshop_but_all_source_metadata(self):
        profile = self.profile()
        profile['prompt_editorial_review'] = {'date': '2026-09-28', 'opening_change': 'Dateien bestimmen den Versandauftrag.', 'norms': ['§ 130a ZPO'], 'remaining_limits': [], 'files': [f'{self.slug}/{self.prompt.name}'], 'decisions': [{'citation': 'Ein verifizierter Entscheidungsanker', 'application': 'Formkontrolle', 'limit': 'Kein allgemeiner Sachnachweis', 'url': 'https://www.bundesgerichtshof.de/'}]}
        lab.validate_profile(profile, self.slug, self.plugin, self.root)
        profile['mini_review'] = dict(profile['workshop_review'])
        with self.assertRaisesRegex(lab.LabError, 'nicht vorgesehenen Prompt'):
            lab.validate_profile(profile, self.slug, self.plugin, self.root)

    def test_audits_only_discover_published_variants(self):
        self.assertEqual(set(ROUTING.expected_prompt_files(self.slug, self.plugin)), {'werkstatt'})
        with patch.object(QUICK, 'REPO', self.root), patch.object(QUICK, 'MARKETPLACE', self.market):
            self.assertEqual(QUICK.plugin_entries(), [])
        with patch.object(HYGIENE, 'REPO', self.root):
            self.assertEqual(HYGIENE.prompt_files(), [self.prompt])
        with patch.object(COVERAGE, 'REPO', self.root):
            self.assertNotIn('`bea-versand`', '\n'.join(COVERAGE.prompt_table([self.entry], 'schnellstart')))
            workshop = '\n'.join(COVERAGE.prompt_table([self.entry], 'werkstatt'))
            self.assertIn('bea-versand-werkstatt.md', workshop)
            self.assertIn('bea-versand-werkstatt.txt', workshop)

    def test_index_and_readme_offer_both_workshop_files_without_dead_quickstart(self):
        with patch.object(INDEX, 'REPO_ROOT', self.root):
            index = INDEX.plugin_detail_page(self.slug, ['bea-anlagen-versand'], '1.0.0')
        with patch.object(DIRECT, 'REPO', self.root), patch.object(DIRECT, 'testakten_section', return_value=''):
            readme = DIRECT.block(self.entry, self.plugin, [], 1)
        for text in (index, readme):
            self.assertIn('bea-versand-werkstatt.md', text)
            self.assertIn('bea-versand-werkstatt.txt', text)
            self.assertNotIn('bea-versand-schnellstart', text)
            self.assertNotIn('bea-versand-hauptproblem', text)
            self.assertNotIn('einer der beiden', text)
            self.assertNotIn('Spezialserien', text)
            self.assertNotIn('Fachrouter', text)
        self.assertIn('## Werkstatt verwenden', readme)
        self.assertIn('[Werkstatt verwenden](#werkstatt-verwenden)', readme)
        self.assertNotIn('#in-30-sekunden-starten', readme)
        self.assertNotIn('Den Schnellstart', readme)
        self.assertNotIn('Startsatz', readme)
        self.assertNotIn('einen fachbezogenen Erststand', readme)

    def test_packaging_rejects_txt_inside_installable_and_skill_archives(self):
        archive = self.root / 'bea-versand.zip'
        with ZipFile(archive, 'w') as output:
            output.writestr('.claude-plugin/plugin.json', json.dumps({'name': self.slug, 'version': '1.0.0'}))
            output.writestr(f'{self.slug}-werkstatt.txt', self.prompt.read_bytes())
        with ZipFile(archive) as output:
            self.assertEqual(PACKAGING.prompt_entries(output), [f'{self.slug}-werkstatt.txt'])
        with patch.object(RELEASE, 'fail', side_effect=ValueError), self.assertRaises(ValueError):
            RELEASE.validate_plugin_zip(self.root, self.slug, '1.0.0')


if __name__ == '__main__':
    unittest.main()
