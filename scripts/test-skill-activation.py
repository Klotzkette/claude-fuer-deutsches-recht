#!/usr/bin/env python3
"""Nur deklarierte Quellarchive verschwinden aus der aktiven Skill-Auswahl."""
import json
from pathlib import Path
import runpy
import tempfile
import unittest

MODULE = runpy.run_path(str(Path(__file__).with_name('audit-skill-activation.py')))


class ActivationScopeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name).resolve()
        self.write('.claude-plugin/marketplace.json', json.dumps({'plugins': [
            {'name': 'neu', 'source': './oberordner/neu'}]}))
        self.active = self.write('oberordner/neu/skills/start/SKILL.md', '# Aktiver Skill')
        self.old = self.write('alt/skills/start/SKILL.md', '# Historischer Skill')
        self.write('alt/.claude-plugin/plugin.json', json.dumps({'name': 'alt'}))
        self.row = {'legacy': 'alt', 'canonical': 'neu', 'legacy_status': 'retained_source_archive'}

    def write(self, name, text):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def registry(self, rows=None):
        return self.write('scripts/plugin-consolidations.json', json.dumps({
            'schema_version': 1, 'consolidations': rows if rows is not None else [self.row]}))

    def test_explicit_archive_excluded_but_active_nested_source_retained(self):
        self.registry()
        self.assertEqual(MODULE['skill_files'](self.repo), [self.active])
        self.assertEqual(self.old.read_text(), '# Historischer Skill')

    def test_undeclared_archive_or_unknown_skill_is_error(self):
        with self.assertRaisesRegex(ValueError, 'ohne aktives Plugin'):
            MODULE['skill_files'](self.repo)
        self.registry()
        self.write('unbekannt/skills/start/SKILL.md', '# Unbekannt')
        with self.assertRaisesRegex(ValueError, 'unbekannt'):
            MODULE['skill_files'](self.repo)

    def test_missing_canonical_wrong_status_and_duplicates_fail(self):
        for rows in [[{**self.row, 'canonical': 'fehlt'}],
                     [{**self.row, 'legacy_status': 'ignore'}], [self.row, self.row],
                     [{**self.row, 'legacy': '../alt'}]]:
            with self.subTest(rows=rows):
                self.registry(rows)
                with self.assertRaises(ValueError): MODULE['skill_files'](self.repo)

    def test_wrong_manifest_identity_and_symlink_fail(self):
        self.registry()
        manifest = self.write('alt/.claude-plugin/plugin.json', json.dumps({'name': 'falsch'}))
        with self.assertRaisesRegex(ValueError, 'Manifest'): MODULE['skill_files'](self.repo)
        manifest.unlink()
        manifest.symlink_to(self.write('fremd.json', json.dumps({'name': 'alt'})))
        with self.assertRaisesRegex(ValueError, 'Manifest'): MODULE['skill_files'](self.repo)

    def test_active_legacy_cannot_be_excluded(self):
        self.registry()
        self.write('.claude-plugin/marketplace.json', json.dumps({'plugins': [
            {'name': 'neu', 'source': './oberordner/neu'}, {'name': 'alt', 'source': './alt'}]}))
        with self.assertRaisesRegex(ValueError, 'Quellarchiv'): MODULE['skill_files'](self.repo)


if __name__ == '__main__':
    unittest.main()
