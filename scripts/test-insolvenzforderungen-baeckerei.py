#!/usr/bin/env python3
"""Belegbestand und Ausgabeformate der kleinen Münchner Forderungsakte."""

import csv
from datetime import date
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path
import unittest
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from pypdf import PdfReader
from testakte_file_filter import include_in_working_dump

ROOT = Path(__file__).resolve().parents[1]
SLUG = "insolvenzforderungen-pistazienbrezeln-muenchen"
CASE = ROOT / "testakten" / SLUG


def document(name):
    with ZipFile(CASE / name) as archive:
        tree = ET.fromstring(archive.read("word/document.xml"))
    return " ".join(node.text or "" for node in tree.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"))


def table(name):
    with (CASE / name).open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source, delimiter=";"))


def amount(value):
    return Decimal(value.replace(".", "").replace(",", "."))


class BaeckereiAkte(unittest.TestCase):
    def test_five_claims_and_thirty_two_separate_native_documents(self):
        files = [p for p in CASE.iterdir() if include_in_working_dump(p, CASE)]
        self.assertEqual(len(files), 32)
        self.assertEqual(len(list(CASE.glob("*_Anmeldung_*.docx"))), 5)
        self.assertEqual({suffix: sum(p.suffix == suffix for p in files) for suffix in (".docx", ".eml", ".csv", ".xlsx")},
                         {".docx": 22, ".eml": 7, ".csv": 2, ".xlsx": 1})
        readme = (CASE / "README.md").read_text()
        for path in files:
            self.assertTrue(path.name.isascii())
            self.assertIn(path.name, readme)
            if path.suffix == ".docx":
                text = document(path.name)
                self.assertGreater(len(text), 900, path.name)
                self.assertNotRegex(text, r"(?i)Musterlösung|Lösungsmatrix|Platzhalter|Formathinweis|Diese Testakte")
                self.assertNotIn("§", text)
                self.assertRegex(text, "[äöüÄÖÜß]", path.name)

    def test_email_headers_dates_and_native_text(self):
        for path in CASE.glob("*.eml"):
            message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
            for header in ("From", "To", "Date", "Subject", "Message-ID", "MIME-Version"):
                self.assertTrue(message[header], (path.name, header))
            sent = parsedate_to_datetime(message["Date"])
            self.assertLessEqual(sent.date(), date(2026, 8, 28))
            self.assertEqual(str(message["Date"]).split(",")[0], sent.strftime("%a"))
            body = message.get_body().get_content()
            self.assertGreater(len(body), 500)
            self.assertRegex(body, "[äöüÄÖÜß]")

    def test_bank_export_arithmetic(self):
        rows = table("04_Betriebskonto_Auszug_30-06-2026.csv")
        balance = Decimal(0)
        for row in rows:
            balance += amount(row["Haben_EUR"]) - amount(row["Soll_EUR"])
            self.assertEqual(balance, amount(row["Saldo_EUR"]))
        self.assertEqual(balance, Decimal("2365"))
        self.assertEqual(sum(amount(row["Soll_EUR"]) for row in rows if "AM-260511" in row["Buchungstext"]), Decimal("535"))

    def test_csv_shape_and_rental_periods(self):
        for path in CASE.glob("*.csv"):
            with path.open(encoding="utf-8-sig", newline="") as source:
                rows = list(csv.reader(source, delimiter=";"))
            self.assertGreaterEqual(len(rows), 5)
            self.assertTrue(all(len(row) == 6 for row in rows), path.name)
        lease = document("13_Gewerbemietvertrag_15-02-2024.docx")
        for term in ("01.03.2024", "900", "Eine Kaution wird nicht vereinbart", "Hausnummer 14"):
            self.assertIn(term.lower(), lease.lower())
        report = document("02_Fortfuehrungsbericht_28-08-2026.docx")
        self.assertIn("nicht gekündigt", report)
        self.assertIn("Juli und August", report)

    def test_party_invoice_and_procedural_dates(self):
        expected = {
            "05_Anmeldung_Mehl_15-07-2026.docx": ("Auenmühle", "2140", "AM-260511"),
            "08_Anmeldung_Pistazien_17-07-2026.docx": ("Kernspitze", "1070", "KP-260602"),
            "12_Anmeldung_Vermieter_20-07-2026.docx": ("Hofwinkel", "1800", "Juli 2026"),
            "15_Anmeldung_Ofendienst_22-07-2026.docx": ("Wärmekante", "476", "OD-260601"),
            "18_Anmeldung_Webstudio_12-08-2026.docx": ("Fensterfaden", "1190", "FF-260520"),
        }
        for name, terms in expected.items():
            text = document(name)
            for term in terms:
                self.assertIn(term, text, name)
        invoice = document("17_Rechnung_Ofendienst_OD-260601.docx")
        self.assertIn("Brezelgarten Café GmbH", invoice)
        self.assertIn("Backhof 14", invoice)
        opening = document("01_Eroeffnungsbeschluss_01-07-2026.docx")
        for term in ("1500 IN 862/26", "01.07.2026", "00:00", "31.07.2026", "08.09.2026", "10:00", "öffentliche Bekanntmachung"):
            self.assertIn(term, opening)

    def test_combined_pdf_contains_all_inputs_without_warning(self):
        pdf = PdfReader(CASE / "gesamt-pdf" / f"{SLUG}_gesamt.pdf")
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        self.assertNotIn("Diese Testakte wurde", text)
        self.assertNotIn("This test case file", text)
        for path in CASE.iterdir():
            if include_in_working_dump(path, CASE):
                self.assertIn(path.name, text)


if __name__ == "__main__":
    unittest.main()
