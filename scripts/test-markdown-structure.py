"""Bedienüberschriften dürfen keine inhaltlichen Prüfregeln abschalten."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('structure', Path(__file__).with_name('validate-markdown-structure.py'))
subject = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subject)

class StructureTests(unittest.TestCase):
    def inspect(self, text):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder)/'FACHINHALT.md'
            file.write_text(text)
            return subject.inspect(file)

    def test_bare_skill_invocation_is_not_a_promised_source_section(self):
        self.assertEqual(self.inspect('### /arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: anpassen\n\n## Ablauf\n\nText\n'), [])

    def test_real_empty_source_section_still_fails(self):
        for title in ['Quellen', 'Quellen und Updates', 'Rechtsprechung', '/plugin:quellen – Rechtsprechung']:
            self.assertTrue(self.inspect(f'## {title}\n\n## Ablauf\n\nText\n'), title)

    def test_content_and_empty_links_are_still_checked(self):
        self.assertEqual(self.inspect('## Rechtsprechung\n\nGeprüfte Fundstelle.\n'), [])
        self.assertTrue(self.inspect('### /plugin:quellen Thema: fall\n\n[Fehlt]()\n'))

if __name__ == '__main__':
    unittest.main()
