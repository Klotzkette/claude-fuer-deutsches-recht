#!/usr/bin/env python3
"""Namensvorschläge und Einstiegsschutz am tatsächlichen Registry-Entwurf."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).with_name('prepare-skill-cap-registry.py')
SPEC = importlib.util.spec_from_file_location('skill_registry_preparation', SCRIPT)
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


class ReadableSkillNames(unittest.TestCase):
    def test_subject_and_existing_action_remain_understandable(self):
        self.assertEqual(P.slug('Vertrag prüfen'), 'vertrag-pruefen')
        self.assertEqual(P.slug('Mängel und Gewährleistung'), 'maengel-und-gewaehrleistung-bearbeiten')
        self.assertEqual(P.slug('Arbeitsprodukt ausarbeiten und kontrollieren'),
                         'arbeitsprodukt-ausarbeiten-und-kontrollieren')

    def test_long_name_keeps_whole_words_action_and_full_visible_title(self):
        heading = 'Vertrag und Vollmacht und Eigentum und Forderung und Sicherheiten und Haftung prüfen'
        self.assertGreater(len(heading), 82)
        self.assertEqual(P.title(heading + ': Konkrete Prüfung aus den Unterlagen.'), heading)
        candidate = P.slug(heading)
        self.assertLessEqual(len(candidate), 64)
        self.assertRegex(candidate, r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
        self.assertTrue(candidate.endswith('-pruefen'))
        self.assertNotIn('und-pruefen', candidate)
        self.assertTrue(all(word in P.norm(heading).split() for word in candidate.split('-')))

    def test_generic_empty_and_unshortenable_names_require_editorial_choice(self):
        for heading in ('', '---', 'Workflow 01', 'Modul prüfen', 'skill23', 'Hauptskill bearbeiten'):
            with self.subTest(heading=heading), self.assertRaisesRegex(ValueError, 'redaktionell'):
                P.slug(heading)
        with self.assertRaisesRegex(ValueError, 'ohne Wortabbruch'):
            P.slug('Vertragsübertragungszustimmungsdokumentationsvollständigkeitskontrolle prüfen')


class RegistryPreparation(unittest.TestCase):
    SUBJECTS = ('Vertrag', 'Vollmacht', 'Kündigung', 'Miete', 'Darlehen', 'Erbfolge',
                'Grundstück', 'Vergütung', 'Arbeitszeit', 'Urlaub', 'Haftung', 'Schaden',
                'Versicherung', 'Verjährung', 'Zustellung', 'Beweis', 'Datenschutz',
                'Lizenz', 'Marke', 'Register', 'Kosten')

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.plugin = self.root / 'fachgebiet'
        self.keep = self.root / 'keep.json'
        self.output = self.root / 'output/registry.json'
        self.profile_path = self.root / 'scripts/data/werkstatt-visualisierung-profile.json'
        self.profile_path.parent.mkdir(parents=True)
        self.profile_data = {'schema_version': 1, 'plugins': {'fachgebiet': {
            'entry_skills': ['hauptauftrag'], 'mode': 'prompt', 'theme': 'fachgebiet'}}}
        self.write_profile()
        self.keep_data = {'plugins': [{'name': 'fachgebiet', 'source': './fachgebiet', 'keep': ['hauptauftrag']}]}
        self.write_keep()
        self.skill('hauptauftrag', '# Gesamten Fachauftrag bearbeiten\n')
        self.profile = SimpleNamespace(key='fixture', label='Fachgebiet', stationen=[], pruefraster=[])

    def write_profile(self):
        self.profile_path.write_text(json.dumps(self.profile_data), encoding='utf-8')

    def write_keep(self):
        self.keep.write_text(json.dumps(self.keep_data), encoding='utf-8')

    def skill(self, slug, text):
        path = self.plugin / 'skills' / slug / 'SKILL.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def topics(self, headings):
        rows = []
        for number, heading in enumerate(headings):
            source = f'bestand-{number}'
            self.skill(source, f'# {heading}\n\nUnveränderte vollständige Fachquelle.\n')
            rows.append((heading + ': Aus den vorhandenen Unterlagen prüfen.', '^' + source + '$'))
        return {'fachgebiet': rows}

    def run_generator(self, topics):
        with patch.object(P, 'ROOT', self.root), patch.object(P, 'TOPICS', topics), \
                patch.object(P, 'profile_for', return_value=self.profile), \
                patch.object(sys, 'argv', [str(SCRIPT), '--keep', str(self.keep), '--output', str(self.output)]), \
                contextlib.redirect_stdout(io.StringIO()):
            P.main()

    def assert_failure_preserves_output(self, topics, message):
        self.output.parent.mkdir(parents=True, exist_ok=True)
        self.output.write_bytes(b'Bereits vorhandene Registry\n')
        self.output.with_suffix('.review.json').write_bytes(b'Bereits vorhandener Nachweis\n')
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        with self.assertRaisesRegex(ValueError, message):
            self.run_generator(topics)
        after = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_twenty_routes_plus_preserved_main_pass_and_preserve_all_sources(self):
        topics = self.topics([name + ' prüfen' for name in self.SUBJECTS[:20]])
        before = {p: p.read_bytes() for p in self.plugin.rglob('*') if p.is_file()}
        self.run_generator(topics)
        row = json.loads(self.output.read_text())['plugins'][0]
        self.assertEqual(row['keep'], ['hauptauftrag'])
        self.assertEqual(len(row['keep']) + len(row['routes']), 21)
        self.assertEqual(len({route['slug'] for route in row['routes']}), 20)
        self.assertEqual({member for route in row['routes'] for member in route['members']},
                         {f'bestand-{number}' for number in range(20)})
        self.assertEqual(before, {p: p.read_bytes() for p in self.plugin.rglob('*') if p.is_file()})
        self.assertTrue(self.output.with_suffix('.review.json').is_file())

    def test_twenty_two_actual_skills_rejected_before_any_output_changes(self):
        topics = self.topics([name + ' prüfen' for name in self.SUBJECTS])
        self.assert_failure_preserves_output(topics, '22 aktive Skills überschreiten 21')

    def test_generic_heading_rejected_before_output_changes(self):
        self.assert_failure_preserves_output(self.topics(['Workflow 01']), 'redaktionell')

    def test_existing_skill_name_collision_is_not_hidden_by_numbering(self):
        topics = self.topics(['Vertrag prüfen'])
        self.skill('vertrag-pruefen', '# Bestehende Fachquelle bleibt erhalten\n')
        self.assert_failure_preserves_output(topics, 'kollidiert.*redaktionell')

    def test_normalized_route_collision_requires_distinct_editorial_names(self):
        self.assert_failure_preserves_output(self.topics(['Märkte prüfen', 'Maerkte prüfen']),
                                             'kollidiert.*redaktionell')

    def test_declared_entry_cannot_be_silently_regrouped(self):
        topics = self.topics(['Vertrag prüfen'])
        self.keep_data['plugins'][0]['keep'] = []
        self.write_keep()
        self.assert_failure_preserves_output(topics, 'Einstiegsskills in keep erhalten')

    def test_missing_declared_entry_cannot_be_claimed_as_preserved(self):
        topics = self.topics(['Vertrag prüfen'])
        (self.plugin / 'skills/hauptauftrag/SKILL.md').unlink()
        self.assert_failure_preserves_output(topics, 'Einstiegsskills fehlen als SKILL.md')

    def test_unknown_or_duplicate_entry_profiles_fail_without_writes(self):
        topics = self.topics(['Vertrag prüfen'])
        for entries in ([], ['hauptauftrag', 'hauptauftrag'], ['../fremd']):
            self.profile_data['plugins']['fachgebiet']['entry_skills'] = entries
            self.write_profile()
            with self.subTest(entries=entries):
                self.assert_failure_preserves_output(topics, 'eindeutige Einstiegsskills')
        self.profile_data['plugins'] = {}
        self.write_profile()
        self.assert_failure_preserves_output(topics, 'eindeutige Einstiegsskills')


if __name__ == '__main__':
    unittest.main()
