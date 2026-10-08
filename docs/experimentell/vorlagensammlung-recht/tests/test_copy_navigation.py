"""Die separate Kopie erlaubt eigene Downloads, aber keine Pluginverweise."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('copy_check', ROOT / 'scripts/check-gerichtsleitend.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)
PREFIX = ('https://github.com/Klotzkette/claude-fuer-deutsches-recht/'
          'raw/main/docs/experimentell/vorlagensammlung-recht/')


class Navigation(unittest.TestCase):
    def test_own_existing_file_is_not_plugin_reference(self):
        self.assertEqual(CHECK.ohne_eigene_downloadziele(PREFIX + 'LICENSE-MIT'),
                         'download:LICENSE-MIT')

    def test_missing_file_is_not_exempt(self):
        value = PREFIX + 'nicht-vorhanden.md'
        self.assertEqual(CHECK.ohne_eigene_downloadziele(value), value)

    def test_other_plugin_is_not_exempt(self):
        value = 'https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/ki-native-kanzlei/README.md'
        self.assertEqual(CHECK.ohne_eigene_downloadziele(value), value)

    def test_path_escape_is_not_exempt(self):
        value = PREFIX + '../../../README.md'
        self.assertEqual(CHECK.ohne_eigene_downloadziele(value), value)


if __name__ == '__main__':
    unittest.main()
