#!/usr/bin/env python3
"""Regression fuer fehlende H1-Titel der beiden Bauvergabe-Pakete."""

from pathlib import Path
import runpy
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(Path(__file__).with_name("audit-skill-selection.py")))
PLUGINS = ("bauvergabe-unterlagen", "bauvergabe-verfahren")


class BauvergabeSkillSelectionTests(unittest.TestCase):
    def test_all_22_skills_pass_selection_audit_with_distinct_titles(self):
        for plugin in PLUGINS:
            with self.subTest(plugin=plugin):
                report = MODULE["inspect_plugin"](REPO / "bauvergabe" / plugin)
                self.assertEqual(11, report["skills"])
                self.assertEqual([], report["errors"])
                self.assertEqual([], report["same_title_groups"])

    def test_missing_h1_is_still_rejected_for_every_skill(self):
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / "SKILL.md"
            for plugin in PLUGINS:
                for path in sorted((REPO / "bauvergabe" / plugin / "skills").glob("*/SKILL.md")):
                    with self.subTest(skill=path.relative_to(REPO)):
                        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
                        headings = [line for line in lines if line.startswith("# ")]
                        self.assertEqual(1, len(headings))
                        copy.write_text("".join(line for line in lines if line != headings[0]), encoding="utf-8")
                        with self.assertRaises(ValueError):
                            MODULE["skill_metadata"](copy)


if __name__ == "__main__":
    unittest.main()
