"""Katalogwachstum darf keine unkontrollierte Routingdichte erlauben."""
import importlib.util
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('runtime', Path(__file__).with_name('validate-runtime-performance.py'))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


class RuntimeBudgets(unittest.TestCase):
    def test_catalog_limit_respects_twenty_actual_skills_per_plugin(self):
        self.assertEqual(R.catalog_limits(287), (5740, 3630000))
        self.assertEqual(R.catalog_limits(1), (20, 3630000))

    def test_growth_preserves_density(self):
        self.assertEqual(R.catalog_limits(574), (11480, 7260000))
        self.assertEqual(R.catalog_limits(293), (5860, 3705888))

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
                          R.MAX_SKILL_LINES, R.MAX_REFERENCE_BYTES), (20, 55000, 500, 96 * 1024))

    def test_consolidated_payroll_route_does_not_reopen_micro_selectors(self):
        name = 'steuerrecht-anwalt-und-berater'
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for slug in R.RUNTIME_ROUTERS.get(name, set()) | {'lohn-personal-steuer-sv-bearbeiten'}:
                skill = root/'skills'/slug/'SKILL.md'
                skill.parent.mkdir(parents=True); skill.write_text('Arbeitsweg')
            self.assertEqual(R.runtime_route_errors(root, name), [])
            stale = root/'skills/lohn-einzelserie/SKILL.md'
            stale.parent.mkdir(); stale.write_text('Überholter Einzelselektor')
            self.assertTrue(R.runtime_route_errors(root, name))
            stale.rename(stale.with_name('FACHINHALT.md'))
            self.assertEqual(R.runtime_route_errors(root, name), [])

    def test_twenty_one_real_skills_fail_even_with_short_descriptions(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            marketplace = root / ".claude-plugin/marketplace.json"
            marketplace.parent.mkdir()
            marketplace.write_text(json.dumps({"plugins": [{"name": "beispiel", "source": "./beispiel"}]}))
            for number in range(21):
                skill = root / f"beispiel/skills/aufgabe-{number}/SKILL.md"
                skill.parent.mkdir(parents=True)
                skill.write_text(f"---\nname: aufgabe-{number}\ndescription: Aufgabe\n---\n\n# Aufgabe\n")
            previous_repo, previous_marketplace = R.REPO, R.MARKETPLACE
            R.REPO, R.MARKETPLACE = root, marketplace
            try:
                output = io.StringIO()
                with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                    self.assertEqual(R.main(), 1)
                self.assertIn("21 Skills überschreiten das Budget von 20", output.getvalue())
                (root / "beispiel/skills/aufgabe-20/SKILL.md").rename(root / "beispiel/skills/aufgabe-20/FACHINHALT.md")
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(R.main(), 0)
                (root / "beispiel/skills/aufgabe-20/FACHINHALT.md").write_text("x" * (R.MAX_REFERENCE_BYTES + 1))
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(R.main(), 1)
            finally:
                R.REPO, R.MARKETPLACE = previous_repo, previous_marketplace


if __name__ == '__main__':
    unittest.main()
