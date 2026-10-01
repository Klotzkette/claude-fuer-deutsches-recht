#!/usr/bin/env python3
"""Prüft Paket, Fallbelege und Bewertungsprofile, nicht Modellverhalten."""
import csv
import email
from email import policy
from email.utils import parsedate_to_datetime
import json
from pathlib import Path
import re
import unittest
from zipfile import ZipFile

from quality_lab import validate_profile

ROOT = Path(__file__).resolve().parent.parent
NAME = "antidiskriminierung-agg"
PLUGIN = ROOT / NAME
CASE = ROOT / "testakten/agg-bewerbung-sprachanforderung-berlin"
ENTRY = "agg-fall-zum-schreiben-fuehren"


class AntidiskriminierungTests(unittest.TestCase):
    def test_ten_direct_skills_and_navigation(self):
        skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 10)
        entry = (PLUGIN / "skills" / ENTRY / "SKILL.md").read_text()
        descriptions = set()
        for path in skills:
            text = path.read_text()
            description = re.search(r"(?m)^description: (.+)$", text).group(1)
            self.assertTrue(80 <= len(description) <= 360, path)
            self.assertNotIn(description, descriptions)
            descriptions.add(description)
            for n in range(1, 7):
                self.assertRegex(text, rf"(?m)^## {n}\. ")
            self.assertIn("11 pt", text)
            self.assertIn("../../references/zitierweise.md", text)
            self.assertNotIn("werkstatt.md", text)
            self.assertNotIn("schnellstart.md", text)
            if path.parent.name != ENTRY:
                self.assertIn(f"`{path.parent.name}`", entry)

    def test_standalone_and_legal_guards(self):
        settings = json.loads((ROOT / "scripts/prompt-profiles.json").read_text())["plugins"][NAME]
        self.assertTrue(settings["hand_curated"])
        self.assertFalse(settings["megaprompt"])
        for kind in ("werkstatt", "schnellstart"):
            data = (PLUGIN / f"{NAME}-{kind}.md").read_bytes()
            if kind == "schnellstart":
                self.assertLessEqual(len(data), 7500)
                self.assertLessEqual(len(data.decode()), 7500)
            else:
                self.assertGreater(len(data), 12000)
            text = data.decode()
            for anchor in ("8 AZR 402/15", "8 AZR 372/16", "8 AZR 21/23", "8 AZR 49/25", "8 AZR 269/24", "I ZR 129/25", "Paragraf 61b", "Paragraf 21 Absatz 5", "Pressemitteilung", "keine Rechtsberatung"):
                self.assertIn(anchor, text)
            self.assertNotIn(chr(167), text)

    def test_evaluation_coverage(self):
        profile = json.loads((ROOT / "quality/evals" / f"{NAME}.json").read_text())
        validate_profile(profile, NAME, PLUGIN, ROOT)
        self.assertEqual({p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")},
                         {case["target_skill"] for case in profile["cases"]})

    def test_fifteen_separate_native_documents(self):
        files = sorted(p for p in CASE.iterdir() if re.match(r"\d\d_", p.name))
        self.assertEqual(len(files), 15)
        self.assertEqual({p.suffix for p in files}, {".docx", ".eml", ".txt", ".csv"})
        readme = (CASE / "README.md").read_text()
        for path in files:
            self.assertIn(path.name, readme)
            self.assertGreater(path.stat().st_size, 500)
        self.assertFalse(list(CASE.glob("[0-9]*.md")))

    def test_mail_headers_references_and_dates(self):
        messages = {}
        dates = []
        for path in sorted(CASE.glob("*.eml")):
            message = email.message_from_bytes(path.read_bytes(), policy=policy.default)
            for field in ("From", "To", "Date", "Message-ID", "Subject", "MIME-Version", "Content-Type"):
                self.assertIsNotNone(message[field], (path, field))
            self.assertFalse(message.defects, path)
            when = parsedate_to_datetime(message["Date"])
            self.assertIsNotNone(when.tzinfo)
            dates.append(when)
            self.assertNotIn(message["Message-ID"], messages)
            messages[message["Message-ID"]] = message
            self.assertIn("KS-26-17", str(message["Subject"]))
        self.assertEqual(dates, sorted(dates))
        for message in messages.values():
            if message["In-Reply-To"]:
                self.assertIn(message["In-Reply-To"], messages)

    def test_csv_and_document_continuity(self):
        with (CASE / "12_portalverlauf.csv").open(newline="") as stream:
            rows = list(csv.reader(stream, delimiter=";"))
        self.assertEqual(len(rows), 9)
        self.assertTrue(all(len(row) == 6 for row in rows))
        self.assertEqual(rows[1][0], "2026-08-26 09:00")
        self.assertEqual(rows[-1][0], "2026-09-22 10:04")
        for filename in ("01_stellenanzeige_2608.docx", "09_stellenanzeige_1509.docx"):
            with ZipFile(CASE / filename) as archive:
                text = archive.read("word/document.xml").decode()
            for common in ("KS-26-17", "3400", "01.11.2026", "Treptower Straße 84"):
                self.assertIn(common, text)

    def test_relative_references_exist(self):
        for path in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if not target.startswith(("http:", "https:", "#")):
                    self.assertTrue((path.parent / target.split("#", 1)[0]).exists(), (path, target))


if __name__ == "__main__":
    unittest.main()
