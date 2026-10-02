#!/usr/bin/env python3
"""Struktur- und Redaktionsregressionen, keine beobachteten Modellläufe."""

import hashlib
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

from prompt_limits import mini_within_limits
from prompt_profiles import validate_files
from quality_lab import validate_profile

ROOT = Path(__file__).resolve().parents[1]
SLUG = "sektorenvergabe-workflow"
PLUGIN = ROOT / SLUG
MAIN = "sektorenvergabe-steuern"
PREPARATION = (
    "auftrag-und-sektorenbezug-klaeren",
    "reinigungsleistung-und-mengen-bestimmen",
    "eignung-wertung-und-vertrag-gestalten",
    "unterlagen-und-preisblatt-abgleichen",
    "bekanntmachung-und-fristen-vorbereiten",
)
PROCEDURE = (
    "teilnahmeantraege-und-angebote-pruefen",
    "bieterfragen-ruegen-und-aenderungen-bearbeiten",
    "verhandeln-und-angebote-werten",
    "zuschlag-und-stillhaltefrist-sichern",
    "nachpruefung-und-verfahrensfortsetzung-begleiten",
)


def skill(name):
    return (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


class SektorenvergabeWorkflow(unittest.TestCase):
    def test_eleven_direct_skills_with_two_five_step_sections(self):
        actual = {p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, {MAIN, *PREPARATION, *PROCEDURE})
        main = skill(MAIN)
        for name in PREPARATION + PROCEDURE:
            self.assertIn(f"`{name}`", main)
        for name in actual:
            with self.subTest(skill=name):
                content = skill(name)
                self.assertIn(f"name: {name}\n", content)
                for n in range(1, 7):
                    self.assertRegex(content, rf"(?m)^## {n}\. ")
                for term in ("SektVO", "GWB", "EuGH", "https://", "Times New Roman 11 pt", "dezimale Gliederung"):
                    self.assertIn(term, content)
                self.assertNotRegex(name, r"werkstatt|schnellstart")
                self.assertIn("../../references/zitierweise.md", content)

    def test_standalone_prompts_and_editorial_scenarios(self):
        self.assertEqual(validate_files(PLUGIN, SLUG, ROOT), [])
        profile = json.loads((ROOT / "quality/evals" / f"{SLUG}.json").read_text())
        validate_profile(profile, SLUG, PLUGIN, ROOT)
        self.assertEqual({case["target_skill"] for case in profile["cases"]}, {MAIN, *PREPARATION, *PROCEDURE})
        self.assertEqual(profile["prompt_workflow_review"]["method"], "desk_review")
        for kind, key in (("schnellstart", "mini_review"), ("werkstatt", "workshop_review")):
            data = (PLUGIN / f"{SLUG}-{kind}.md").read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), profile[key]["sha256"])
            content = data.decode("utf-8")
            for anchor in ("C-521/18", "C-298/15", "C-368/10", "C-6/15", "C-131/16", "C-54/21"):
                self.assertIn(anchor, content)
            if kind == "schnellstart":
                self.assertTrue(mini_within_limits(SLUG, data))
                self.assertLessEqual(len(data), 7500)
                self.assertLessEqual(len(content), 7500)

    def test_regime_threshold_and_numerical_units(self):
        initial = skill(PREPARATION[0])
        for term in ("100", "102", "432000", "2025/2150", "Option", "Sektorenbezug"):
            self.assertIn(term, initial)
        quantity = skill(PREPARATION[1])
        for term in ("1200", "260", "312000", "Freigabe"):
            self.assertIn(term, quantity)
        self.assertNotRegex(initial, r"Schwellenwert[^\n]*2025/2152")

    def test_changes_trigger_return_paths_not_silent_replacement(self):
        content = skill(PREPARATION[3]) + skill(PROCEDURE[1])
        for term in ("Fristverlängerung", "Änderungsverzeichnis", "Bekanntmachung", "Preisblatt", "Nachprüfungs"):
            self.assertIn(term, content)
        for term in ("zehn", "15", "Zugang", "134", "160"):
            self.assertIn(term, content.lower() if term == "zehn" else content)
        self.assertIn("keine Arbeitsanweisung", skill(MAIN))

    def test_publication_clarification_and_award_are_distinct(self):
        publication = skill(PREPARATION[4])
        for term in ("35 Tage", "30 Tage", "15", "zehn Tage", "technischer Validierung", "TED-Veröffentlichungsbeleg"):
            self.assertIn(term, publication)
        self.assertIn("kein neues konzept", skill(PROCEDURE[0]).lower())
        self.assertIn("Paragraf 54 SektVO", skill(PROCEDURE[2]))
        self.assertIn("keine starre gesetzliche 20-prozent-schwelle", skill(PROCEDURE[2]).lower())

    def test_current_and_historical_remedies_not_conflated(self):
        for name in (MAIN, PROCEDURE[3], PROCEDURE[4]):
            with self.subTest(skill=name):
                content = skill(name)
                self.assertIn("187 Absatz 2", content)
                self.assertIn("01.07.2026", content)
        award = skill(PROCEDURE[3])
        for term in ("15 Kalendertage", "zehn Kalendertage", "Folgetag der Absendung", "tatsächlichen Nachweis"):
            self.assertIn(term, award)
        remedy = skill(PROCEDURE[4])
        for term in ("169", "172", "173", "Bekanntgabe", "nicht aufschiebend", "historische Fassung"):
            self.assertIn(term, remedy)

    def test_relative_links_and_individual_downloads(self):
        for path in PLUGIN.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"\[[^\]]+\]\(\)", str(path))
            self.assertNotIn("§", text)
            for target in re.findall(r"\]\(([^\s)]+)\)", text):
                if "://" not in target and not target.startswith("#"):
                    target = unquote(target.split("#", 1)[0])
                    self.assertTrue((path.parent / target).exists(), f"{path}: {target}")
        readme = (PLUGIN / "README.md").read_text(encoding="utf-8")
        for name in (MAIN,) + PREPARATION + PROCEDURE:
            self.assertIn(f"path={SLUG}/skills/{name}/SKILL.md", readme)
        self.assertIn("English", readme)
        self.assertIn("manuell", readme)
        description = readme.split("Was ist das hier?", 1)[1].split("\n\n", 2)[1]
        self.assertNotRegex(description, r"Verfahrensfuehrung|Ruegen|Nachpruefung")

    def test_marketplace_and_protected_prompt_profile(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = [p for p in marketplace["plugins"] if p["name"] == SLUG]
        self.assertEqual(len(entries), 1)
        manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        for field in ("name", "description", "version"):
            self.assertEqual(entries[0][field], manifest[field])
        profiles = json.loads((ROOT / "scripts/prompt-profiles.json").read_text())
        self.assertTrue(profiles["plugins"][SLUG]["hand_curated"])
        self.assertIn(SLUG, (ROOT / "scripts/handkuratierte-prompts.txt").read_text().splitlines())


if __name__ == "__main__":
    unittest.main()
