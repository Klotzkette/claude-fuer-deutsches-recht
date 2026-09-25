#!/usr/bin/env python3
"""Prüft die Berufungsfrist der Pohlmann-Akte in Quellen und Gesamt-PDF.

Maßgeblich: § 517, § 222 Abs. 1 und 2 ZPO sowie §§ 187 Abs. 1,
188 Abs. 2 BGB. Die DOCX-Dateien sind die Quellen der zentralen PDF-/ZIP-
Builder; für diese Bestandsakte existiert kein gesonderter Textgenerator.
"""
from datetime import date, datetime, timedelta
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
SLUG = "zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann"
CASE = ROOT / "testakten" / SLUG
NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    return "\n".join(
        "".join(node.text or "" for node in paragraph.iter(f"{NS}t"))
        for paragraph in root.iter(f"{NS}p")
    )


def normalized(text: str) -> str:
    return " ".join(text.split())


class PohlmannFristenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.judgment = docx_text(CASE / "12-urteil-lg-traunstein-1-o-2188-25.docx")
        cls.appeal = docx_text(CASE / "13-berufungsbegruendung-olg-muenchen.docx")
        service = datetime.strptime(
            re.search(r"Zustellung: (\d{2}\.\d{2}\.\d{4})", cls.judgment)[1],
            "%d.%m.%Y",
        ).date()
        # Die Akte betrifft August: Der entsprechende Septembertag existiert.
        cls.nominal = service.replace(month=service.month + 1)
        cls.deadline = cls.nominal
        while cls.deadline.weekday() >= 5:
            cls.deadline += timedelta(days=1)

    def test_sunday_end_moves_to_monday(self):
        self.assertEqual(self.nominal, date(2027, 9, 5))
        self.assertEqual(self.nominal.weekday(), 6)
        self.assertEqual(self.deadline, date(2027, 9, 6))

    def test_both_sources_use_adjusted_deadline(self):
        expected = self.deadline.strftime("%d.%m.%Y")
        self.assertIn(f"Berufungsfrist: Montag, {expected}", self.judgment)
        self.assertIn(f"Berufungsfrist bis Montag, {expected}", self.appeal)
        for text in (self.judgment, self.appeal):
            self.assertNotRegex(text, r"Berufungsfrist(?: bis|:)\s*05\.09\.2027")
            self.assertIn("§ 222", text)
        self.assertIn("Berufungsbegründungsfrist: 05.10.2027", self.judgment)

    def test_aggregate_matches_both_sources(self):
        pdf = CASE / "gesamt-pdf" / f"{SLUG}_gesamt.pdf"
        text = normalized("\n".join(page.extract_text() or "" for page in PdfReader(pdf).pages))
        expected = self.deadline.strftime("%d.%m.%Y")
        self.assertIn(f"Berufungsfrist: Montag, {expected}", text)
        self.assertIn(f"Berufungsfrist bis Montag, {expected}", text)
        self.assertNotRegex(text, r"Berufungsfrist(?: bis|:)\s*05\.09\.2027")


if __name__ == "__main__":
    unittest.main()
