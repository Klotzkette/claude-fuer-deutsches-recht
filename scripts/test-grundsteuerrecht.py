#!/usr/bin/env python3
"""Sichert Bescheidabgleich, Dezimalrechnung und das kompakte Grundsteuerpaket."""

from decimal import Decimal
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

import yaml


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "grundsteuerrecht"
CALCULATOR = PLUGIN / "scripts/rechenabgleich.py"
SPEC = importlib.util.spec_from_file_location("grundsteuer_rechnung", CALCULATOR)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
SKILLS = {
    "bescheide-und-fristen-ordnen", "grundstueck-und-flaechen-abgleichen",
    "landesmodell-und-stichtag-bestimmen", "grundsteuerwert-nachrechnen",
    "niedrigeren-grundstueckswert-nachweisen", "messbetrag-und-hebesatz-pruefen",
    "einspruch-und-aenderungsantrag-entwerfen", "zahlung-und-eilrechtsschutz-sichern",
    "klage-und-musterverfahren-einordnen", "folgebescheid-und-mandantenbericht-abschliessen",
}


class RechenabgleichTests(unittest.TestCase):
    def test_original_notice_values_remain_distinct(self):
        result = MODULE.compare({
            "grundsteuerwert_eur": "367900", "messzahl_promille": "0.31",
            "messbetrag_bescheid_eur": "114.05", "messbetrag_jahresbescheid_eur": "114.64",
            "hebesatz_prozent": "470", "jahressteuer_bescheid_eur": "538.80",
        })["rohwerte"]
        expected = {
            "messbetrag_rechnerisch_eur": "114.049",
            "steuer_aus_messbescheid_eur": "536.035",
            "steuer_aus_jahresbescheid_eur": "538.808",
            "messbetrag_uebernahmedifferenz_eur": "0.59",
            "jahressteuer_differenz_zum_rohprodukt_eur": "-0.008",
        }
        self.assertEqual({k: Decimal(v) for k, v in result.items()}, {k: Decimal(v) for k, v in expected.items()})

    def test_threshold_uses_common_value_and_includes_equality(self):
        for assessed, expected in (("279999.99", False), ("280000", True), ("280000.01", True)):
            with self.subTest(value=assessed):
                result = MODULE.compare({"grundsteuerwert_eur": assessed, "gemeiner_wert_eur": "200000"})
                self.assertIs(result["bundesmodell_schwelle"]["rechnerisch_erreicht"], expected)
                self.assertEqual(Decimal(result["bundesmodell_schwelle"]["vergleichswert_eur"]), Decimal("280000"))

    def test_missing_is_not_zero_or_substituted(self):
        result = MODULE.compare({"messbetrag_jahresbescheid_eur": "114.64", "hebesatz_prozent": "470"})
        self.assertNotIn("steuer_aus_messbescheid_eur", result["rohwerte"])
        self.assertEqual(result["fehlende_eingaben"]["steuer_aus_messbescheid_eur"], ["messbetrag_bescheid_eur"])
        self.assertNotIn("bundesmodell_schwelle", result)
        self.assertEqual(MODULE.compare({"messbetrag_bescheid_eur": "0", "hebesatz_prozent": "470"})["rohwerte"]["steuer_aus_messbescheid_eur"], "0")

    def test_invalid_or_ambiguous_numbers_fail(self):
        for value in (None, True, 0.31, 100, "NaN", "Infinity", "1e1000000", "-1", "1,40", "1.400,00", "01", "1." + "0" * 9):
            with self.subTest(value=value), self.assertRaises(ValueError):
                MODULE.compare({"grundsteuerwert_eur": value})
        for data in ({}, [], {"flaeche": "30"}, {"gemeiner_wert_eur": "0"}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                MODULE.compare(data)

    def test_cli_failure_has_no_partial_output(self):
        inputs = ('{"grundsteuerwert_eur":"1","grundsteuerwert_eur":"2"}', '{', '[]', ' ' * 65537)
        for text in inputs:
            result = subprocess.run([sys.executable, str(CALCULATOR), "-"], input=text, text=True, capture_output=True, timeout=5)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
            self.assertIn("abgebrochen", result.stderr)

    def test_cli_example_and_extreme_valid_precision(self):
        data = {"grundsteuerwert_eur": "999999999999999.12345678", "messzahl_promille": "999999999999999.12345678"}
        result = subprocess.run([sys.executable, str(CALCULATOR), "-"], input=json.dumps(data), text=True, capture_output=True, timeout=5, check=True)
        self.assertEqual(json.loads(result.stdout), MODULE.compare(data))
        actual = json.loads(result.stdout)["rohwerte"]["messbetrag_rechnerisch_eur"]
        self.assertEqual(Fraction(actual), Fraction(data["grundsteuerwert_eur"]) ** 2 / 1000)


class PaketTests(unittest.TestCase):
    def test_exactly_ten_independent_skills(self):
        paths = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual({p.parent.name for p in paths}, SKILLS)
        descriptions = []
        for path in paths:
            text = path.read_text(encoding="utf-8")
            metadata = yaml.safe_load(text.split("---", 2)[1])
            self.assertEqual(set(metadata), {"name", "description"})
            self.assertEqual(metadata["name"], path.parent.name)
            self.assertTrue(80 <= len(metadata["description"]) <= 1024)
            self.assertEqual(re.findall(r"^## (\d+)\. ", text, re.M), list("123456"))
            self.assertIn("Times New Roman 11 pt", text)
            self.assertIn("../../references/zitierweise.md", text)
            descriptions.append(metadata["description"])
        self.assertEqual(len(set(descriptions)), 10)

    def test_local_resources_resolve(self):
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                target = (path.parent / link).resolve()
                self.assertTrue(target.is_relative_to(PLUGIN.resolve()))
                self.assertTrue(target.is_file(), (path, link))

    def test_standalone_prompts_and_temporal_guards(self):
        for kind in ("werkstatt", "schnellstart"):
            text = (PLUGIN / f"grundsteuerrecht-{kind}.md").read_text()
            with self.subTest(kind=kind):
                self.assertNotIn("skills/", text)
                for anchor in ("II B 78/23", "II R 3/25", "II R 26/24", "November 2024", "1 BvR 472/26", "1 BvR 551/26", "Paragraf 351 Absatz 2", "Promille", "1,40"):
                    self.assertIn(anchor, text)
                headings = [int(n) for n in re.findall(r"^## (\d+)\. ", text, re.M)]
                self.assertEqual(headings, list(range(1, len(headings) + 1)))
                if kind == "schnellstart":
                    self.assertLess(len(text.encode("utf-8")), 7500)
                else:
                    self.assertLess(len(text.encode("utf-8")), 48 * 1024)

    def test_marketplace_manifest_and_case_navigation(self):
        manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        entries = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"]
        entry = next(item for item in entries if item["name"] == "grundsteuerrecht")
        self.assertEqual(entry["description"], manifest["description"])
        self.assertEqual(entry["version"], manifest["version"])
        slug = "steuer-grundsteuer-wolkenfels-berlin"
        self.assertIn(slug, (PLUGIN / "README.md").read_text())
        row = next(line for line in (ROOT / "testakten/README.md").read_text().splitlines() if line.startswith(f"| [`{slug}/`]"))
        self.assertIn("`grundsteuerrecht`", row)
        self.assertIn("../../grundsteuerrecht/README.md", (ROOT / "testakten" / slug / "README.md").read_text())


if __name__ == "__main__":
    unittest.main()
