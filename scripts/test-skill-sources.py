#!/usr/bin/env python3
"""Quellresolver darf verlorene Dateien nicht durch geratene Aliase verdecken."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import skill_sources as subject

class SourceTests(unittest.TestCase):
    def test_existing_original_is_not_redirected(self):
        with tempfile.TemporaryDirectory() as tmp:
            old=Path(tmp)/'SKILL.md';old.write_text('Original')
            self.assertEqual(subject.fachinhalt_path(old),old)

    def test_only_declared_migration_can_resolve(self):
        with tempfile.TemporaryDirectory() as tmp:
            old=Path(tmp)/'SKILL.md';new=Path(tmp)/'FACHINHALT.md';new.write_text('Original')
            with patch.object(subject,'moved_sources',return_value={}):
                with self.assertRaises(FileNotFoundError):subject.fachinhalt_path(old)
            with patch.object(subject,'moved_sources',return_value={old.resolve():new}):
                self.assertEqual(subject.fachinhalt_path(old),new)
                new.unlink()
                with self.assertRaises(FileNotFoundError):subject.fachinhalt_path(old)

    def test_unknown_active_owner_is_not_invented(self):
        with tempfile.TemporaryDirectory() as tmp,patch.object(subject,'registry',return_value=[]):
            with self.assertRaises(FileNotFoundError):subject.active_owner(Path(tmp),'missing')

    def test_declared_owner_must_exist_as_a_real_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            plugin={'source':'.','keep':[], 'routes':[{'slug':'pruefen','members':['vertiefung']}]}
            with patch.object(subject,'ROOT',root),patch.object(subject,'registry',return_value=[plugin]):
                with self.assertRaises(FileNotFoundError):subject.active_owner(root,'vertiefung')
                target=root/'skills/pruefen/SKILL.md';target.parent.mkdir(parents=True);target.write_text('Prüfung')
                self.assertEqual(subject.active_owner(root,'vertiefung'),'pruefen')
                target.rename(target.with_name('FACHINHALT.md'))
                with self.assertRaises(FileNotFoundError):subject.active_owner(root,'vertiefung')

if __name__=='__main__':unittest.main()
