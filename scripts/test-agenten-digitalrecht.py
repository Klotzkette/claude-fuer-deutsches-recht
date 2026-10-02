#!/usr/bin/env python3
"""Strukturelle Regressionen; keine simulierten Modell- oder Rechtsprüfungen."""

import importlib.util
from pathlib import Path
import re
import unittest

from quality_lab import load, validate_profile


ROOT = Path(__file__).resolve().parent.parent
SKILLS = {
    "berufsrecht-ki-vertragspruefung": ("subunternehmer-regelung-pruefen",),
    "datenschutzrecht": (
        "avv-rolemix-getrennt-vs-gemeinsam-verantwortlich",
        "datenschutz-loeschpflicht-art-17-und-aufbewahrung",
        "dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo",
    ),
    "fachanwalt-it-recht": ("itr-ki-systeme-vertragsklausel-leitfaden",),
    "ki-governance": ("ki-haftung-und-versicherung", "rollenmodell-use-case-vendor"),
    "ki-verordnung-hochrisiko-pruefer": (
        "betreiberkonzept-bewerbungsauswahl", "hr-zweck-und-systemabgrenzung",
        "rollenwechsel-und-shadow-ai",
    ),
    "ki-verordnung-transparenzpruefer": ("chat-und-telefonhinweise",),
    "ki-vo-ai-act-pruefer": ("automatisierte-entscheidung-dsgvo-art-22",),
    "nis2-cybersecurity-compliance": ("ki-tools-shadow-it",),
}
SPEC = importlib.util.spec_from_file_location(
    "prompt_structure", ROOT / "scripts/audit-prompt-profile-routing.py"
)
STRUCTURE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(STRUCTURE)


def skill(plugin, name):
    return (ROOT / plugin / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


class AgentenDigitalrechtTests(unittest.TestCase):
    def test_profiles_and_individual_cases(self):
        for plugin in SKILLS:
            with self.subTest(plugin=plugin):
                profile = load(ROOT / "quality/evals" / f"{plugin}.json")
                validate_profile(profile, plugin, ROOT / plugin)
                cases = [c for c in profile["cases"] if c["id"] == "agenten-digitalrecht-2026"]
                self.assertEqual(len(cases), 1)
                self.assertIn(cases[0]["target_skill"], SKILLS[plugin])
                self.assertGreaterEqual(len(cases[0]["criteria"]), 3)
                self.assertEqual(cases[0]["input_files"], [])

    def test_prompt_limits_structure_and_portability(self):
        for plugin in SKILLS:
            for kind in ("schnellstart", "werkstatt"):
                with self.subTest(plugin=plugin, kind=kind):
                    text = (ROOT / plugin / f"{plugin}-{kind}.md").read_text(encoding="utf-8")
                    self.assertIn("Agent", text)
                    self.assertEqual(STRUCTURE.individual_workshop_structure_problems(text), [])
                    self.assertNotIn("../../references/", text)
                    if kind == "schnellstart":
                        self.assertLess(len(text.encode("utf-8")), 7500)
                        self.assertLessEqual(len(text), 7500)

    def test_skill_names_and_packaged_references(self):
        for plugin, names in SKILLS.items():
            for name in names:
                with self.subTest(plugin=plugin, skill=name):
                    path = ROOT / plugin / "skills" / name / "SKILL.md"
                    text = path.read_text(encoding="utf-8")
                    self.assertRegex(text, rf"(?m)^name: {re.escape(name)}$")
                    for link in re.findall(r"\]\(([^)]+)\)", text):
                        if "://" in link or link.startswith("#"):
                            continue
                        target = (path.parent / link.split("#")[0]).resolve()
                        self.assertTrue(target.is_relative_to((ROOT / plugin).resolve()), link)
                        self.assertTrue(target.is_file(), link)

    def test_decision_and_erasure_guardrails(self):
        mini = (ROOT / "datenschutzrecht/datenschutzrecht-schnellstart.md").read_text(encoding="utf-8")
        for token in ("Gedächtnis", "Ausgabefilter", "Artikel 22", "Artikel 18"):
            self.assertIn(token, mini)
        decision = skill("ki-vo-ai-act-pruefer", "automatisierte-entscheidung-dsgvo-art-22")
        for token in ("C-634/21", "C-203/22", "keine Ausnahme von Artikel 22", "Geschäftsgeheimnisse"):
            self.assertIn(token, decision)
        erasure = skill("datenschutzrecht", "datenschutz-loeschpflicht-art-17-und-aufbewahrung")
        for token in ("Paragraf 8 Absatz 4 GwG", "Artikel 18 hat eigene Voraussetzungen",
                      "keine automatisch gleichwertige Löschung", "Artikel 12 Absatz 3"):
            self.assertIn(token, erasure)

    def test_contract_and_incident_guardrails(self):
        contract = skill("fachanwalt-it-recht", "itr-ki-systeme-vertragsklausel-leitfaden")
        for token in ("keine rechtsgeschäftliche Vollmacht", "unklarem Vollzug", "Artikel 25 Absatz 4", "Exit"):
            self.assertIn(token, contract)
        incident = skill("nis2-cybersecurity-compliance", "ki-tools-shadow-it")
        for token in ("Paragraf 32", "24 Stunden", "72 Stunden", "11. September 2026",
                      "11. Dezember 2027", "delegierte Aufträge weiterlaufen"):
            self.assertIn(token, incident)
        secrecy = skill("berufsrecht-ki-vertragspruefung", "subunternehmer-regelung-pruefen")
        for token in ("Einwilligung nach Absatz 5", "nicht automatisch genehmigt",
                      "Ein vorheriger Einzelzustimmungsvorbehalt ist nicht"):
            self.assertIn(token, secrecy)


if __name__ == "__main__":
    unittest.main()
