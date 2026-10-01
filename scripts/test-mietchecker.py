#!/usr/bin/env python3
"""Prüft Rechenlogik, Verpackung und Belegkonsistenz; keine Modellbewertung."""
import csv
from decimal import Decimal
import email
from email import policy
import importlib.util
import json
from pathlib import Path
import re
import unittest
from zipfile import ZipFile
from xml.etree import ElementTree as ET

from quality_lab import validate_profile

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "mietchecker"
CASES = [ROOT / "testakten" / name for name in (
    "mietchecker-neuvermietung-berlin", "mietchecker-flaeche-kueche-regensburg")]
spec = importlib.util.spec_from_file_location("mietrechnung", PLUGIN / "scripts/mietrechnung.py")
calc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calc)


def docx_text(path):
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    return " ".join(root.itertext())


class MietcheckerTests(unittest.TestCase):
    def test_berlin_asymmetric_halves(self):
        self.assertEqual(calc.berlin("5.90", "7.30", "9.55", [1, 1, 0, 0, 0]), Decimal("8.20"))
        self.assertEqual(calc.berlin("5.90", "7.30", "9.55", [-1, -1, 0, 0, 0]), Decimal("6.74"))
        self.assertEqual(calc.berlin("5.90", "7.30", "9.55", [1, -1, 0, 0, 0]), Decimal("7.30"))
        self.assertEqual(calc.berlin("5.90", "7.30", "9.55", [1]*5), Decimal("9.55"))
        self.assertEqual(calc.berlin("5.90", "7.30", "9.55", [-1]*5), Decimal("5.90"))

    def test_unknown_is_not_neutral(self):
        for groups in ([None, 0, 0, 0, 0], [True, 0, 0, 0, 0], [2, 0, 0, 0, 0], [0]*4):
            with self.subTest(groups=groups), self.assertRaises(ValueError):
                calc.berlin(5, 7, 10, groups)
        with self.assertRaises(ValueError):
            calc.berlin(8, 7, 10, [0]*5)

    def test_regensburg_addition_and_rounding(self):
        self.assertEqual(calc.regensburg("10.44", [-8, -5, -3]), Decimal("8.77"))
        self.assertEqual(calc.monthly("8.77", 70), Decimal("613.90"))
        # Öffentliches Rechenbeispiel der Stadt: 75 Quadratmeter, Saldo minus drei.
        self.assertEqual(calc.regensburg("10.42", [-13, -5, 2, -2, 4, 8, 3]), Decimal("10.11"))
        self.assertEqual(calc.monthly("10.11", 75), Decimal("758.25"))

    def test_independent_limits(self):
        self.assertEqual(calc.initial_basic_limit(calc.monthly("9.55", 62)), Decimal("651.31"))
        self.assertEqual(calc.increase_ceiling(750, 600, 15), Decimal("690.00"))
        self.assertEqual(calc.increase_ceiling("613.90", 600, 15), Decimal("613.90"))

    def test_reject_invalid_numbers(self):
        for value in ("NaN", "Infinity", "abc", None, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                calc.monthly(value, 70)
        for call in (lambda: calc.monthly(10, 0), lambda: calc.regensburg(10, []),
                     lambda: calc.regensburg(10, [-100]), lambda: calc.increase_ceiling(800, 600, 12)):
            with self.assertRaises(ValueError):
                call()

    def test_exactly_ten_skills_and_internal_routes(self):
        skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 10)
        entry = (PLUGIN / "skills/miete-pruefen-und-klaeren/SKILL.md").read_text()
        descriptions = []
        for path in skills:
            content = path.read_text()
            descriptions.append(re.search(r"(?m)^description: (.+)$", content).group(1))
            for n in range(1, 7):
                self.assertRegex(content, rf"(?m)^## {n}\. ")
            self.assertIn("11 pt", content)
            if path.parent.name != "miete-pruefen-und-klaeren":
                self.assertIn(path.parent.name, entry)
            self.assertNotIn("werkstatt.md", content)
            self.assertNotIn("schnellstart.md", content)
        self.assertEqual(len(set(descriptions)), 10)
        self.assertTrue(all(80 <= len(d) <= 360 for d in descriptions))

    def test_standalone_profiles_and_sources(self):
        data = json.loads((ROOT / "scripts/prompt-profiles.json").read_text())["plugins"]["mietchecker"]
        self.assertTrue(data["hand_curated"])
        self.assertFalse(data["megaprompt"])
        for kind in ("schnellstart", "werkstatt"):
            path = PLUGIN / f"mietchecker-{kind}.md"
            content = path.read_text()
            if kind == "schnellstart":
                self.assertLessEqual(len(path.read_bytes()), 7400)
            else:
                self.assertGreater(len(path.read_bytes()), 12000)
            for anchor in ("VIII ZR 266/14", "VIII ZR 52/18", "VIII ZR 123/20", "VIII ZR 229/22",
                           "Berlin", "Regensburg", "keine Rechtsberatung"):
                self.assertIn(anchor, content)
            self.assertNotIn(chr(167), content)
        profile = json.loads((ROOT / "quality/evals/mietchecker.json").read_text())
        validate_profile(profile, "mietchecker", PLUGIN, ROOT)
        self.assertEqual({p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")},
                         {c["target_skill"] for c in profile["cases"]})

    def test_separate_documents_and_messages(self):
        for case in CASES:
            sources = sorted(p for p in case.iterdir() if re.match(r"\d\d_", p.name))
            self.assertEqual(len(sources), 12)
            self.assertEqual({p.suffix for p in sources}, {".docx", ".eml", ".csv", ".txt"})
            readme = (case / "README.md").read_text()
            for path in sources:
                self.assertIn(path.name, readme)
            self.assertFalse(list(case.glob("[0-9]*.md")))
            ids = set()
            messages = []
            for path in case.glob("*.eml"):
                message = email.message_from_bytes(path.read_bytes(), policy=policy.default)
                for name in ("From", "To", "Date", "Message-ID", "Subject", "Content-Type"):
                    self.assertIsNotNone(message[name])
                self.assertFalse(message.defects)
                ids.add(message["Message-ID"])
                messages.append(message)
            self.assertEqual(len(ids), 3)
            for message in messages:
                if message["In-Reply-To"]:
                    self.assertIn(message["In-Reply-To"], ids)

    def test_mietkonto_sums_and_key_documents(self):
        for case in CASES:
            with (case / "08_mietkonto.csv").open(newline="") as stream:
                rows = list(csv.DictReader(stream, delimiter=";"))
            self.assertGreaterEqual(len(rows), 4)
            for row in rows:
                parts = [Decimal(v) for k, v in row.items() if k.endswith("_EUR") and k != "Gesamt_EUR"]
                self.assertEqual(sum(parts), Decimal(row["Gesamt_EUR"]))
            self.assertIn("620" if "regensburg" in case.name else "980",
                          docx_text(case / ("02_mietanpassung_2024.docx" if "regensburg" in case.name else "01_mietvertrag.docx")))
        contract = docx_text(CASES[1] / "01_mietvertrag.docx")
        self.assertIn("76 Quadratmetern", contract)
        survey = docx_text(CASES[1] / "04_aufmass_2026.docx")
        self.assertIn("70 Quadratmeter", survey)

    def test_relative_references(self):
        for path in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if not target.startswith(("http:", "https:", "#")):
                    self.assertTrue((path.parent / target.split("#", 1)[0]).exists(), (path, target))


if __name__ == "__main__":
    unittest.main()
