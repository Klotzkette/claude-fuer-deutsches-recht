"""Katalogwachstum darf keine unkontrollierte Routingdichte erlauben."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('runtime', Path(__file__).with_name('validate-runtime-performance.py'))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


class RuntimeBudgets(unittest.TestCase):
    def test_original_catalog_limits_are_unchanged(self):
        self.assertEqual(R.catalog_limits(287), (23000, 3630000))

    def test_growth_preserves_density(self):
        self.assertEqual(R.catalog_limits(574), (46000, 7260000))
        self.assertEqual(R.catalog_limits(293), (23480, 3705888))

    def test_growth_of_same_catalog_still_fails(self):
        rows = [dict(name=str(i), skills=0, description_chars=0) for i in range(293)]
        a, b = R.catalog_limits(len(rows))
        rows[0].update(skills=a, description_chars=b)
        self.assertEqual(R.catalog_errors(rows), [])
        rows[0].update(skills=a + 1, description_chars=b + 1)
        self.assertEqual(len(R.catalog_errors(rows)), 2)

    def test_empty_duplicate_and_invalid_counts_fail(self):
        self.assertTrue(R.catalog_errors([]))
        self.assertTrue(R.catalog_errors([dict(name='same'), dict(name='same')]))
        for value in (0, -1, True, '293'):
            with self.assertRaises(ValueError):
                R.catalog_limits(value)

    def test_single_plugin_limits_are_not_scaled(self):
        self.assertEqual((R.MAX_SKILLS_PER_PLUGIN, R.MAX_DESCRIPTION_CHARS_PER_PLUGIN,
                          R.MAX_SKILL_LINES, R.MAX_REFERENCE_BYTES), (320, 55000, 500, 96 * 1024))


if __name__ == '__main__':
    unittest.main()
