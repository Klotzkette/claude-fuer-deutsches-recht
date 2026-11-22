"""Prüft den Abgleich der öffentlichen Skill-Tabellen ohne Schreibzugriff."""
import json
from pathlib import Path
import runpy
import tempfile
import unittest

from skill_overview_text import description

ROOT = Path(__file__).resolve().parents[1]
overview = runpy.run_path(str(ROOT / 'scripts/generate-skills-overview.py'))
ROW = overview['SKILL_ROW']
BEGIN, END = overview['BEGIN'], overview['END']


def row(slug, text, label='MD'):
    return f'| [`{slug}`](skills/{slug}/SKILL.md) | {text} | [{label}](skills/{slug}/SKILL.md) |'


class SkillOverviewTests(unittest.TestCase):
    def test_yaml_quoting_folding_and_table_separator(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / 'SKILL.md'
            for value in ["'Text: mit | Zeichen.'", '>\n  Text: mit\n  | Zeichen.']:
                skill.write_text(f'---\nname: demo\ndescription: {value}\n---\n# Demo\n')
                self.assertEqual(description(skill), r'Text: mit \| Zeichen.')

    def test_only_the_description_changes_even_in_a_curated_section(self):
        original = '\n'.join(['# Fachgebiet', BEGIN, '<details>', '| Skill | Beschreibung | Rohdatei |', '| --- | --- | --- |',
                              row('demo', 'Alt', 'Quelle').replace('[`demo`]', '[Zum Einstieg]'), '</details>', '## Vorlagen', '[Anlage](akte.pdf)', END])
        expected = original.replace(' | Alt | ', ' | Neu | ')
        self.assertEqual(overview['updated_overview'](original, row('demo', 'Neu')), expected)
        self.assertEqual(overview['updated_overview'](expected, row('demo', 'Neu')), expected)

    def test_added_and_removed_skills_preserve_other_material(self):
        original = '\n'.join([BEGIN, 'Der vollständige Katalog enthält 2 Skills.',
                              '| Skill | Beschreibung | Rohdatei |', '| --- | --- | --- |',
                              row('entfernt', 'Alt'), row('behalten', 'Alt', 'Quelle'), '[Anlage](akte.pdf)', END])
        desired = '\n'.join([row('behalten', 'Neu'), row('neu', 'Dazu', 'MD herunterladen / Download MD'),
                             row('dritter', 'Dazu', 'MD herunterladen / Download MD')])
        result = overview['updated_overview'](original, desired)
        self.assertIn('Katalog enthält 3 Skills', result)
        self.assertNotIn('entfernt', result)
        self.assertIn(row('neu', 'Dazu', 'Raw .md'), result)
        self.assertIn(row('behalten', 'Neu', 'Quelle'), result)
        self.assertIn('[Anlage](akte.pdf)', result)

    def test_public_descriptions_match_the_installed_skills(self):
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        for plugin in marketplace['plugins']:
            directory = ROOT / plugin['source']
            skills = sorted((directory / 'skills').glob('*/SKILL.md'))
            readme = directory / 'README.md'
            with self.subTest(readme=plugin['name']):
                text = readme.read_text()
                self.assertEqual(text.count(BEGIN), 1)
                self.assertEqual(text.count(END), 1)
                self.assert_descriptions(text.split(BEGIN)[1].split(END)[0], skills,
                                         vergaberolle=directory.parent.name == 'vergaberecht-werkstatt')
            with self.subTest(index=plugin['name']):
                detail = ROOT / 'skills-index' / (plugin['name'] + '.md')
                self.assert_descriptions(detail.read_text(), skills, limit=280)
            if directory.parent.name == 'vergaberecht-werkstatt':
                with self.subTest(rollenindex=plugin['name']):
                    detail = directory.parent / 'skills-index' / (plugin['name'] + '.md')
                    self.assert_descriptions(detail.read_text(), skills, with_title=True, limit=None, vergaberolle=True)

    def assert_descriptions(self, text, skills, with_title=False, **options):
        rows = list(ROW.finditer(text))
        self.assertCountEqual((m['slug'] for m in rows), (p.parent.name for p in skills))
        actual = {m['slug']: m['description'].partition(' | ')[2] if with_title else m['description'] for m in rows}
        for path in skills:
            expected = description(path, **options)
            self.assertTrue(expected, str(path))
            self.assertEqual(actual[path.parent.name], expected, str(path))


if __name__ == '__main__':
    unittest.main()
