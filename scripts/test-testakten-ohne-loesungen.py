#!/usr/bin/env python3
"""Regressionen für Lösungsschlüssel und zulässige Parteidarstellungen."""

import importlib.util
import hashlib
from pathlib import Path
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ohne_loesungen", SCRIPTS / "validate-testakten-ohne-loesungen.py")
AUDIT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AUDIT)


class SolutionKeyTests(unittest.TestCase):
    def test_review_is_bound_to_exact_source_content(self):
        original_root = AUDIT.ROOT
        try:
            with tempfile.TemporaryDirectory() as tmp:
                AUDIT.ROOT = Path(tmp)
                source = AUDIT.ROOT / "akte.txt"
                source.write_text("Musterlösung wurde nicht herausgegeben.")
                reviewed = {"akte.txt": {"reason": "Angeforderte Unterlage fehlt.", "sha256": hashlib.sha256(source.read_bytes()).hexdigest()}}
                self.assertTrue(AUDIT.reviewed_context(source, reviewed))
                source.write_text(source.read_text()+"\nMusterlösung: Anspruch besteht.")
                self.assertFalse(AUDIT.reviewed_context(source, reviewed))
        finally:
            AUDIT.ROOT = original_root

    def test_explicit_answer_keys(self):
        for marker in ("Lösungsmatrix", "Loesungsmatrix", "Antwortmatrix", "Musterlösung", "Musterloesung", "Lösungsskizze", "Erwartungshorizont", "Prüferhinweis", "Dozentenhinweis"):
            with self.subTest(marker=marker):
                self.assertTrue(AUDIT.problems(Path("auskunft.docx"), marker))

    def test_filename_is_checked_even_without_text_layer(self):
        self.assertTrue(AUDIT.problems(Path("09_loesungsmatrix.pdf"), ""))

    def test_party_positions_are_not_answer_keys(self):
        for text in (
            "Der Beklagte bestreitet die Fälligkeit der Forderung.",
            "Wir halten den Bescheid für rechtswidrig und legen Widerspruch ein.",
            "Das Gericht hat die Klage mit Urteil vom 12. Mai abgewiesen.",
            "Bitte prüfen Sie die offenen Posten. Die Bank hat die Linie nicht verlängert.",
        ):
            self.assertEqual(AUDIT.problems(Path("schreiben.docx"), text), [])

    def test_export_filter_does_not_hide_a_source_from_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("Downloadhinweis", encoding="utf-8")
            (root / "rubric.yaml").write_text("checks: []", encoding="utf-8")
            key = root / "09_musterloesung.txt"
            key.write_text("Musterlösung", encoding="utf-8")
            self.assertEqual(list(AUDIT.source_files(root)), [key])


if __name__ == "__main__":
    unittest.main()
