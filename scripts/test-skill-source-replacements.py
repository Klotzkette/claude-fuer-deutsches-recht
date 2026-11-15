#!/usr/bin/env python3
"""Ersatzregister erlaubt nur vollständige aktuelle Quellen und geprüfte Altbytes."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from skill_source_replacements import validate_replacements


class SourceReplacementTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name).resolve()
        self.write('.claude-plugin/marketplace.json', {'plugins': [{'name': 'fachgebiet', 'source': './fachgebiet'}]})
        self.skill = self.write('fachgebiet/skills/start/SKILL.md', '[Kapitel](../../references/kapitel.md)')
        self.chapter = self.write('fachgebiet/references/kapitel.md', '# Neue fachliche Prüfung')
        self.old = 'fachgebiet/skills/alt/FACHINHALT.md'
        self.new = 'quality/ersatz/legacy/' + self.old
        self.original = self.write(self.new, '# Ursprüngliche Fachquelle')
        content = self.original.read_bytes()
        self.manifest_path = 'quality/ersatz/legacy/mapping.json'
        self.manifest = {'files': [{'old_path': self.old, 'new_path': self.new,
                                    'sha256': hashlib.sha256(content).hexdigest(), 'bytes': len(content)}]}
        self.entry = {'source': 'fachgebiet', 'active_skills': ['start'],
                      'chapters': ['references/kapitel.md'], 'archive_manifest': self.manifest_path}
        self.save()

    def write(self, name, value):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) if not isinstance(value, str) else value)
        return path

    def save(self):
        self.write(self.manifest_path, self.manifest)
        self.write('scripts/data/skill-source-replacements.json', {'schema_version': 1, 'plugins': {'fachgebiet': self.entry}})

    def assert_invalid(self):
        result, errors = validate_replacements(self.repo)
        self.assertEqual(result, {})
        self.assertTrue(errors)

    def test_valid_exact_mapping_and_optional_registry(self):
        result, errors = validate_replacements(self.repo)
        self.assertEqual(errors, [])
        self.assertEqual(result, {'fachgebiet': {self.old: self.original}})
        (self.repo / 'scripts/data/skill-source-replacements.json').unlink()
        self.assertEqual(validate_replacements(self.repo), ({}, []))

    def test_changed_bytes_size_and_hash_fail(self):
        baseline = copy.deepcopy(self.manifest)
        for field, value in [('sha256', '0' * 64), ('bytes', 0), ('bytes', True)]:
            with self.subTest(field=field, value=value):
                self.manifest = copy.deepcopy(baseline)
                self.manifest['files'][0][field] = value
                self.save()
                self.assert_invalid()
        self.manifest = baseline
        self.save()
        self.original.write_text('# Verändert')
        self.assert_invalid()

    def test_extra_or_missing_active_skill_and_wrong_source_fail(self):
        baseline = copy.deepcopy(self.entry)
        for values in [{'active_skills': ['start', 'fehlt']}, {'active_skills': ['start', 'start']},
                       {'source': 'anders'}, {'source': '../fachgebiet'}]:
            with self.subTest(values=values):
                self.entry = {**baseline, **values}
                self.save()
                self.assert_invalid()
        self.entry = baseline
        self.save()
        self.write('fachgebiet/skills/zusatz/SKILL.md', '# Nicht registriert')
        self.assert_invalid()

    def test_missing_or_unreachable_chapter_fails(self):
        self.skill.write_text('# Kein Fachkapitel verknüpft')
        self.assert_invalid()
        self.skill.write_text('[Kapitel](../../references/kapitel.md)')
        self.chapter.unlink()
        self.assert_invalid()

    def test_foreign_original_wrong_structure_and_duplicates_fail(self):
        baseline = copy.deepcopy(self.manifest)
        for field, value in [('old_path', 'anderes-plugin/skills/alt/FACHINHALT.md'),
                             ('new_path', 'quality/ersatz/legacy/anderer-name.md'),
                             ('new_path', '../fremd.md')]:
            with self.subTest(field=field):
                self.manifest = copy.deepcopy(baseline)
                self.manifest['files'][0][field] = value
                self.save()
                self.assert_invalid()
        self.manifest = baseline
        self.manifest['files'].append(copy.deepcopy(baseline['files'][0]))
        self.save()
        self.assert_invalid()

    def test_symlink_or_archive_inside_plugin_fails(self):
        self.original.unlink()
        self.original.symlink_to(self.write('fremd.md', '# Ursprüngliche Fachquelle'))
        self.assert_invalid()
        self.original.unlink()
        self.original.write_text('# Ursprüngliche Fachquelle')
        self.entry['archive_manifest'] = 'fachgebiet/legacy/mapping.json'
        self.write(self.entry['archive_manifest'], self.manifest)
        self.save()
        self.assert_invalid()


if __name__ == '__main__':
    unittest.main()
