#!/usr/bin/env python3
"""Isolierte Regressionen für dezimal gegliederte individuelle Schnellstarts."""

from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "quickstart_usability", ROOT / "scripts/audit-quickstart-usability.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class ReviewedQuickstartTests(unittest.TestCase):
    def audit(self, structure=None, *, text=None, review_error=None):
        if text is None:
            introduction = "Prüfen Sie die vorhandenen Unterlagen und bearbeiten Sie den Auftrag. " * 40
            text = f"# Fachlicher Schnellstart\n\n{introduction}\n\n{structure}\n"
        with tempfile.TemporaryDirectory(prefix="quickstart-audit-") as directory:
            root = Path(directory)
            plugin = root / "fachgebiet"
            plugin.mkdir()
            prompt = plugin / "fachgebiet-schnellstart.md"
            prompt.write_text(text, encoding="utf-8")
            review = root / "quality/evals/fachgebiet.json"
            review.parent.mkdir(parents=True)
            review.write_text("{}", encoding="utf-8")
            output = io.StringIO()
            with (
                patch.object(AUDIT, "REPO", root),
                patch.object(AUDIT, "protected_slugs", return_value=set()),
                patch.object(AUDIT, "plugin_entries", return_value=[("fachgebiet", prompt)]),
                patch.object(AUDIT, "validate_profile", side_effect=review_error) as validate,
                redirect_stdout(output),
            ):
                result = AUDIT.main()
            validate.assert_called_once()
            return result, output.getvalue()

    def assert_valid(self, structure):
        result, output = self.audit(structure)
        self.assertEqual(result, 0, output)

    def assert_invalid(self, structure):
        result, output = self.audit(structure)
        self.assertEqual(result, 1, output)

    def test_consecutive_decimal_paragraphs_are_valid(self):
        self.assert_valid("\n\n".join(f"{number}. Abschnitt: Konkreten Auftrag bearbeiten." for number in range(1, 9)))

    def test_existing_ai_paragraph_prompts_are_valid(self):
        for slug in ("ki-verordnung-konformitaet", "ki-verordnung-register-meldungen"):
            with self.subTest(slug=slug):
                text = (ROOT / slug / f"{slug}-schnellstart.md").read_text(encoding="utf-8")
                result, output = self.audit(text=text)
                self.assertEqual(result, 0, output)

    def test_decimal_h2_headings_remain_valid(self):
        self.assert_valid("## 1. Auftrag\n\nBearbeiten.\n\n## 2. Ergebnis\n\nAusformulieren.")
        self.assert_valid("## 1 Auftrag\n\nBearbeiten.\n\n## 1.1 Belege\n\nLesen.\n\n## 2 Ergebnis\n\nAusformulieren.")

    def test_absent_structure_is_invalid(self):
        self.assert_invalid("Ein weiterer unnummerierter Absatz ohne Abschnittsstruktur.")

    def test_paragraph_numbers_must_start_at_one_without_gaps(self):
        for numbers in ((2, 3), (0, 1), (1, 3), (1, 2, 4)):
            with self.subTest(numbers=numbers):
                self.assert_invalid("\n\n".join(f"{number}. Abschnitt bearbeiten." for number in numbers))

    def test_duplicate_and_unordered_paragraph_numbers_are_invalid(self):
        for numbers in ((1, 2, 2), (1, 3, 2)):
            with self.subTest(numbers=numbers):
                self.assert_invalid("\n\n".join(f"{number}. Abschnitt bearbeiten." for number in numbers))

    def test_nondecimal_sections_cannot_be_skipped(self):
        for invalid in ("A.", "a)", "II.", "1)", "01.", "Arbeitsweise:"):
            with self.subTest(label=invalid):
                self.assert_invalid(f"1. Auftrag bearbeiten.\n\n{invalid} Belege prüfen.\n\n2. Ergebnis ausformulieren.")

    def test_nondecimal_leading_section_cannot_be_skipped(self):
        self.assert_invalid("A. Auftrag bearbeiten.\n\n1. Belege prüfen.\n\n2. Ergebnis ausformulieren.")

    def test_roman_and_alphabetic_structures_are_invalid(self):
        for labels in (("I.", "II."), ("A.", "B."), ("a)", "b)")):
            with self.subTest(labels=labels):
                self.assert_invalid("\n\n".join(f"{label} Abschnitt bearbeiten." for label in labels))

    def test_missing_paragraph_number_is_invalid(self):
        self.assert_invalid("1. Auftrag bearbeiten.\n\nBelege prüfen.\n\n2. Ergebnis ausformulieren.")

    def test_invalid_h2_cannot_use_paragraph_fallback(self):
        for headings in (("Auftrag", "Ergebnis"), ("1. Auftrag", "1. Ergebnis"),
                         ("2. Auftrag", "1. Ergebnis"), ("1. Auftrag", "A. Ergebnis")):
            with self.subTest(headings=headings):
                self.assert_invalid(f"## {headings[0]}\n\n1. Auftrag bearbeiten.\n\n## {headings[1]}\n\n2. Ergebnis ausformulieren.")

    def test_existing_h2_allows_numbered_content(self):
        self.assert_valid("## 1. Auftrag\n\n1. Beleg lesen.\n\n2. Beleg zuordnen.\n\n## 2. Ergebnis\n\nAusformulieren.")

    def test_invalid_individual_review_remains_invalid(self):
        result, output = self.audit("1. Auftrag bearbeiten.\n\n2. Ergebnis ausformulieren.",
                                    review_error=ValueError("Prüfhash stimmt nicht"))
        self.assertEqual(result, 1)
        self.assertIn("ungültige individuelle Prüfung: Prüfhash stimmt nicht", output)


if __name__ == "__main__":
    unittest.main()
