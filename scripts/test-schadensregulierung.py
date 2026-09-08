#!/usr/bin/env python3
"""Prüft den kompakten Arbeitsweg und die drei Fassungen der Berliner Akte."""

import csv
from decimal import Decimal
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
import zipfile

from pypdf import PdfReader

from testakte_disclaimer import NOTICE_BYTES, pdf_content_errors
from testakte_einzelpdf_common import expected_arcnames


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "schadensregulierung"
SLUG = "schadensregulierung-ubahn-tuerunfall-berlin"
CASE = ROOT / "testakten" / SLUG
SKILLS = {
    "schadenfall-aufnehmen", "unfallbelege-sichern", "haftungsweg-bestimmen",
    "versicherung-einschalten", "schadenpositionen-pruefen",
    "regress-und-anspruchsuebergang", "regulierung-korrespondieren",
    "vergleich-und-zahlung-abschliessen",
}


def load_builder(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SchadensregulierungTests(unittest.TestCase):
    def test_eight_focused_skills_and_independent_prompts(self):
        paths = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual({path.parent.name for path in paths}, SKILLS)
        for kind in ("werkstatt", "schnellstart"):
            text = (PLUGIN / f"schadensregulierung-{kind}.md").read_text(encoding="utf-8")
            with self.subTest(prompt=kind):
                for anchor in ("HaftPflG", "VVG", "SGB X", "VI ZR 937/20", "VI ZR 168/21"):
                    self.assertIn(anchor, text)
                self.assertNotIn("skills/", text)
                if kind == "schnellstart":
                    self.assertLess(len(text.encode("utf-8")), 7500)
                    self.assertLessEqual(len(text), 7500)

    def test_reported_expenses_are_consistent(self):
        with (CASE / "07_auslagen.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 4)
        self.assertTrue(all(None not in row for row in rows))
        total = sum(Decimal(row["Betrag_EUR"]) for row in rows)
        self.assertEqual(total, Decimal("384.80"))
        self.assertEqual(Decimal(rows[0]["Betrag_EUR"]), Decimal("329.00"))
        self.assertIn("384,80", (CASE / "14_telefonvermerk.txt").read_text(encoding="utf-8"))

    def test_combined_pdf_contains_each_document(self):
        path = CASE / "gesamt-pdf" / f"{SLUG}_gesamt.pdf"
        self.assertEqual(pdf_content_errors(path.read_bytes()), [])
        text = "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)
        for source in CASE.iterdir():
            if source.name[:2].isdigit() and source.is_file():
                with self.subTest(source=source.name):
                    self.assertIn(source.name, text)

    def test_flat_archives_preserve_native_sources_and_separate_pdfs(self):
        expected = set(expected_arcnames(CASE))
        self.assertEqual(len(expected), 15)
        sources = [path for path in CASE.iterdir() if path.is_file() and path.name[:2].isdigit()]
        self.assertEqual(len(sources), 15)
        self.assertEqual({path.suffix for path in sources}, {".docx", ".eml", ".csv", ".txt"})
        for filename in ("build-testakten-release-zips.py", "build-testakten-einzelpdf-zips.py"):
            with self.subTest(builder=filename), tempfile.TemporaryDirectory() as directory:
                path, _ = load_builder(filename).build_single(CASE, Path(directory))
                with zipfile.ZipFile(path) as archive:
                    names = archive.namelist()
                    self.assertEqual(len(names), len(set(names)))
                    self.assertTrue(all("/" not in name and "\\" not in name for name in names))
                    self.assertFalse(any(name.endswith(".md") for name in names))
                    self.assertEqual(archive.read("README.txt"), NOTICE_BYTES)
                    self.assertIsNone(archive.testzip())
                    if "einzelpdf" in filename:
                        self.assertEqual(set(names), expected | {"README.txt"})
                        for name in expected:
                            data = archive.read(name)
                            self.assertEqual(pdf_content_errors(data), [], name)
                            self.assertGreater(len(PdfReader(io.BytesIO(data)).pages), 0, name)
                    else:
                        self.assertEqual(set(names), {source.name for source in sources} | {"README.txt", f"{SLUG}_gesamt.pdf"})
                        self.assertEqual(archive.read(f"{SLUG}_gesamt.pdf"), (CASE / "gesamt-pdf" / f"{SLUG}_gesamt.pdf").read_bytes())
                        for source in sources:
                            self.assertEqual(archive.read(source.name), source.read_bytes(), source.name)

    def test_case_is_reachable_from_plugin_and_index(self):
        for path in (PLUGIN / "README.md", ROOT / "testakten" / "README.md"):
            self.assertIn(SLUG, path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
