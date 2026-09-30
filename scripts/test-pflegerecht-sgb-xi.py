#!/usr/bin/env python3
"""Struktur- und Redaktionsregressionen; keine beobachteten Modellläufe."""
import json
from pathlib import Path
import re
import unittest

from quality_lab import validate_profile

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "pflegerecht-sgb-xi"


class PflegerechtTests(unittest.TestCase):
    def test_ten_direct_skills(self):
        paths = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(paths), 10)
        main = (PLUGIN / "skills/pflegefall-bearbeiten/SKILL.md").read_text()
        for path in paths:
            with self.subTest(skill=path.parent.name):
                if path.parent.name != "pflegefall-bearbeiten":
                    self.assertIn(f"`{path.parent.name}`", main)
                text = path.read_text()
                for number in range(1, 7):
                    self.assertRegex(text, rf"(?m)^## {number}\. ")
                self.assertIn("../../references/zitierweise.md", text)
                self.assertIn("11 pt", text)

    def test_standalone_limits_and_decimal_headings(self):
        fast = (PLUGIN / "pflegerecht-sgb-xi-schnellstart.md").read_bytes()
        self.assertLessEqual(len(fast), 7500)
        self.assertLessEqual(len(fast.decode("utf-8")), 7500)
        workshop = (PLUGIN / "pflegerecht-sgb-xi-werkstatt.md").read_bytes()
        self.assertGreater(len(workshop), 25000)
        for path in PLUGIN.glob("*-*.md"):
            for line in path.read_text().splitlines():
                if line.startswith("##"):
                    self.assertRegex(line, r"^#{2,3} \d+\.(?:\d+)? ", path.name)

    def test_profile_has_individual_cases_for_every_skill(self):
        profile = json.loads((ROOT / "quality/evals/pflegerecht-sgb-xi.json").read_text())
        validate_profile(profile, PLUGIN.name, PLUGIN, ROOT)
        self.assertEqual({p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")},
                         {case["target_skill"] for case in profile["cases"]})

    def test_legal_pitfalls_in_both_prompts(self):
        for kind in ("werkstatt", "schnellstart"):
            text = (PLUGIN / f"pflegerecht-sgb-xi-{kind}.md").read_text()
            for anchor in ("B 3 P 5/24 R", "B 3 P 9/23 R", "B 3 P 5/22 R",
                           "3539", "4180", "01.07.2026", "folgenden Kalenderjahres",
                           "halbjährlich", "Paragraf 51 SGG"):
                self.assertIn(anchor, text, (kind, anchor))
            self.assertNotIn("§", text)

    def test_local_references_exist(self):
        for path in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if target.startswith(("https://", "http://", "#")):
                    continue
                self.assertTrue((path.parent / target.split("#", 1)[0]).exists(), (path, target))

    def test_no_prompt_wrappers(self):
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            self.assertNotIn("werkstatt.md", path.read_text())
            self.assertNotIn("schnellstart.md", path.read_text())
        config = json.loads((ROOT / "scripts/prompt-profiles.json").read_text())["plugins"][PLUGIN.name]
        self.assertTrue(config["hand_curated"])
        self.assertFalse(config["megaprompt"])


if __name__ == "__main__":
    unittest.main()
