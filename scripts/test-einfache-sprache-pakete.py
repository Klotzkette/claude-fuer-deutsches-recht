#!/usr/bin/env python3
"""Struktur, Schutzregeln und Bewertungsfälle; keine simulierten Modellresultate."""
import json
from pathlib import Path
import re
import unittest

from quality_lab import validate_profile

ROOT = Path(__file__).resolve().parent.parent
PACKAGES = {"jura-in-einfacher-sprache": (5, "juristischen-text-uebertragen"),
            "sozialrecht-fuer-laien": (10, "meinen-sozialfall-starten")}


class EinfacheSpracheTests(unittest.TestCase):
    def test_direct_skills_and_routes(self):
        for plugin, (count, entry) in PACKAGES.items():
            paths = sorted((ROOT / plugin / "skills").glob("*/SKILL.md"))
            self.assertEqual(len(paths), count)
            main = (ROOT / plugin / "skills" / entry / "SKILL.md").read_text()
            descriptions = set()
            for path in paths:
                with self.subTest(path=path):
                    text = path.read_text()
                    description = re.search(r"(?m)^description: (.+)$", text).group(1)
                    self.assertTrue(80 <= len(description) <= 360)
                    self.assertNotIn(description, descriptions)
                    descriptions.add(description)
                    for number in range(1, 7):
                        self.assertRegex(text, rf"(?m)^## {number}\. ")
                    self.assertIn("../../references/zitierweise.md", text)
                    self.assertIn("11 pt", text)
                    if path.parent.name != entry:
                        self.assertIn(f"`{path.parent.name}`", main)
                    self.assertNotIn("werkstatt.md", text)
                    self.assertNotIn("schnellstart.md", text)

    def test_standalone_prompts(self):
        profiles = json.loads((ROOT / "scripts/prompt-profiles.json").read_text())["plugins"]
        for plugin in PACKAGES:
            self.assertTrue(profiles[plugin]["hand_curated"])
            self.assertFalse(profiles[plugin]["megaprompt"])
            for kind in ("werkstatt", "schnellstart"):
                data = (ROOT / plugin / f"{plugin}-{kind}.md").read_bytes()
                text = data.decode("utf-8")
                if kind == "schnellstart":
                    self.assertLessEqual(len(data), 7500)
                else:
                    self.assertGreater(len(data), 12000)
                self.assertIn("DIN ISO 24495-1", text)
                self.assertIn("DIN 8581-1", text)
                self.assertIn("keine Rechtsberatung", text)
                self.assertIn("B 4 KG 1/24 R", text)
                self.assertNotIn("§", text)
                for line in text.splitlines():
                    if line.startswith("##"):
                        self.assertRegex(line, r"^#{1,3} \d+\.(?:\d+)? ")

    def test_profiles_cover_every_skill(self):
        for plugin in PACKAGES:
            directory = ROOT / plugin
            profile = json.loads((ROOT / "quality/evals" / f"{plugin}.json").read_text())
            validate_profile(profile, plugin, directory, ROOT)
            self.assertEqual({p.parent.name for p in (directory / "skills").glob("*/SKILL.md")},
                             {c["target_skill"] for c in profile["cases"]})

    def test_references_are_local_and_exist(self):
        for plugin in PACKAGES:
            for path in (ROOT / plugin).rglob("*.md"):
                for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                    if target.startswith(("http://", "https://", "#")):
                        continue
                    self.assertTrue((path.parent / target.split("#", 1)[0]).exists(), (path, target))

    def test_no_private_source_or_norm_attachment(self):
        for plugin in PACKAGES:
            for path in (ROOT / plugin).rglob("*"):
                if not path.is_file():
                    continue
                self.assertNotIn(path.suffix.lower(), {".pdf", ".docx", ".pptx"})
                if path.suffix in {".md", ".json"}:
                    text = path.read_text()
                    self.assertNotIn("remote-attachments", text)
                    self.assertNotIn("Kundennummer", text)

    def test_deadline_and_form_guards(self):
        plugin = "sozialrecht-fuer-laien"
        for kind in ("schnellstart", "werkstatt"):
            text = (ROOT / plugin / f"{plugin}-{kind}.md").read_text()
            for phrase in ("Paragraf 64 SGG", "Paragraf 67 SGG", "Paragraf 84 SGG", "Paragraf 87 SGG",
                           "Paragraf 65a SGG", "Paragraf 37 SGB X", "Rechtsantragstelle",
                           "B 1 KR 9/18 R", "1 BvR 569/05", "B 3 P 5/24 R"):
                self.assertIn(phrase, text)
            self.assertIn("ein Monat", text)
            self.assertIn("drei Monate", text)
            self.assertRegex(text, r"(?i)einfache E-Mail")

    def test_meaning_preservation_in_both_prompts(self):
        plugin = "jura-in-einfacher-sprache"
        for kind in ("schnellstart", "werkstatt"):
            text = (ROOT / plugin / f"{plugin}-{kind}.md").read_text()
            for phrase in ("Zugang", "Versand", "schriftlich", "kann", "muss", "soll", "Leichte Sprache",
                           "Lesefassung", "Paragraf 11 BGG", "Paragraf 19 SGB X"):
                self.assertIn(phrase, text)
            self.assertIn("keine", text)
            self.assertIn("Normkonformität", text)

    def test_repository_disclaimer(self):
        text = (ROOT / "README.md").read_text()
        self.assertIn("keine Rechtsberatung", text)
        self.assertIn("zwingende gesetzliche Haftung bleibt unberührt", text)
        for plugin in PACKAGES:
            self.assertIn(f"./{plugin}/README.md", text)

    def test_reverse_transfer_contract(self):
        plugin = ROOT / "jura-in-einfacher-sprache"
        paths = [plugin / f"jura-in-einfacher-sprache-{kind}.md"
                 for kind in ("schnellstart", "werkstatt")]
        paths.append(plugin / "skills/juristischen-text-uebertragen/SKILL.md")
        for path in paths:
            with self.subTest(path=path):
                text = path.read_text()
                for phrase in ("juristische Standardsprache", "Rückübertragung", "Zusammenfassung",
                               "Wiederherstellung", "Anerkenntnis"):
                    self.assertIn(phrase, text)
        review = (plugin / "skills/bedeutung-und-verstaendlichkeit-pruefen/SKILL.md").read_text()
        self.assertIn("zweimalige Umformulierung beweist keine Bedeutungstreue", review)
        self.assertIn("verfügbaren Ausgangstext", review)

    def test_reverse_transfer_and_numeric_evaluation_cases(self):
        profile = json.loads((ROOT / "quality/evals/jura-in-einfacher-sprache.json").read_text())
        cases = {case["id"]: case for case in profile["cases"]}
        for name in ("rueckuebertragung-ohne-neue-zusage", "fehlendes-original",
                     "zwei-fassungen-kein-vollstaendigkeitsbeweis", "monatlicher-hoechstbetrag"):
            self.assertIn(name, cases)
            self.assertGreaterEqual(len(cases[name]["criteria"]), 3)
        self.assertTrue(any("Standardsprache" in value for value in profile["selection"]["positive"]))


if __name__ == "__main__":
    unittest.main()
