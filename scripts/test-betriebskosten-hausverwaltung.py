#!/usr/bin/env python3
"""Rechen-, Beleg- und Verpackungsregressionen der Betriebskostenfälle."""

import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from email import policy
from email.parser import BytesParser
from decimal import Decimal

from openpyxl import load_workbook
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("bk_belege", ROOT / "scripts/build-betriebskosten-schoeneberg-belege.py")
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
SUPPLEMENT_SPEC = importlib.util.spec_from_file_location("bk_nachtrag", ROOT / "scripts/build-betriebskosten-belegnachtrag.py")
SUPPLEMENT = importlib.util.module_from_spec(SUPPLEMENT_SPEC)
SUPPLEMENT_SPEC.loader.exec_module(SUPPLEMENT)


class BetriebskostenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        BUILDER.ROOT = Path(cls.temp.name)
        cls.cases = [BUILDER.build(case) for case in BUILDER.CASES]
        SUPPLEMENT.build(BUILDER.ROOT)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_monthly_bills_and_distinct_sources(self):
        for case in self.cases:
            bills = case["belege"]
            self.assertEqual(len([b for b in bills if b["category"] == "Hausservice"]), 12)
            self.assertEqual(len([b for b in bills if b["category"] == "Allgemeinstrom"]), 12)
            self.assertEqual(len({b["number"] for b in bills}), len(bills))
            self.assertEqual(len({b["file"] for b in bills}), len(bills))
            self.assertEqual(sum(b["amount"] for b in bills if b["category"] == "Hausservice"), case["hm"] * 12)

    def test_ground_tax_chain_and_areas(self):
        for case in self.cases:
            self.assertEqual(BUILDER.rounded(case["tax_value"] * .00031 * 4.7), case["tax"])
            self.assertEqual(sum(case["areas"]), case["area"])
            self.assertEqual(case["areas"][int(case["unit"]) - 1], 108)
            path = BUILDER.ROOT / "testakten" / case["slug"] / "belege/Grundsteuer_2025.pdf"
            text = "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
            self.assertIn(BUILDER.money(case["tax"]), text)
            self.assertIn("470 Prozent", text)

    def test_twelve_payments_are_preserved_separately_from_statement(self):
        for case in self.cases:
            self.assertEqual(12 * (case["cold"] + case["heat"]), 3600)
            self.assertEqual(BUILDER.rounded(case["draft_total"] - case["draft_credited"]), case["draft_balance"])
        self.assertEqual(self.cases[0]["draft_credited"], 3300)
        self.assertEqual(self.cases[1]["draft_credited"], 3600)

    def test_csv_columns_and_source_links(self):
        for case in self.cases:
            directory = BUILDER.ROOT / "testakten" / case["slug"]
            for path in directory.rglob("*.csv"):
                with path.open(encoding="utf-8") as stream:
                    rows = list(csv.reader(stream, delimiter=";"))
                self.assertGreaterEqual(len(rows), 5)
                self.assertTrue(all(len(row) == len(rows[0]) for row in rows))
            for bill in case["belege"]:
                self.assertTrue((directory / bill["file"]).is_file())
            with (directory / "zahlenwerk/Flaechen_und_Messwerte_2025.csv").open(encoding="utf-8") as stream:
                headers = next(csv.reader(stream, delimiter=";"))
            self.assertIn("Heizkostenverteiler_Einheiten", headers)
            self.assertNotIn("Heizwärme_kWh", headers)

    def test_substantial_readable_single_documents(self):
        for path in BUILDER.ROOT.rglob("*.pdf"):
            text = "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
            self.assertGreater(len(text), 600, path.name)
            self.assertNotIn(chr(167), text)
            for term in ("Musterlösung", "Lösungsmatrix", "Dozentenhinweis", "Platzhalter", "example.org"):
                self.assertNotIn(term, text, path.name)

    def test_rebuild_is_byte_stable(self):
        before = {p.relative_to(BUILDER.ROOT): hashlib.sha256(p.read_bytes()).hexdigest() for p in BUILDER.ROOT.rglob("*.pdf")}
        for case in BUILDER.CASES:
            BUILDER.build(case)
        SUPPLEMENT.build(BUILDER.ROOT)
        after = {p.relative_to(BUILDER.ROOT): hashlib.sha256(p.read_bytes()).hexdigest() for p in BUILDER.ROOT.rglob("*.pdf")}
        self.assertEqual(before, after)

    def test_workbook_sources_formulas_and_cached_totals(self):
        for case in self.cases:
            path = ROOT / "testakten" / case["slug"] / "zahlenwerk/Verwaltungsbuchhaltung_2025.xlsx"
            values = load_workbook(path, data_only=True, read_only=True)
            formulas = load_workbook(path, data_only=False, read_only=True)
            try:
                self.assertEqual(values.sheetnames, ["Belegeingang", "Mietkonto2025", "Abrechnung_Stand"])
                rows = list(values["Belegeingang"].iter_rows(min_row=8, max_row=7 + len(case["belege"]), values_only=True))
                self.assertEqual(len(rows), len(case["belege"]))
                for row, bill in zip(rows, case["belege"]):
                    self.assertEqual(row[5], bill["number"])
                    self.assertAlmostEqual(row[3], bill["amount"], places=2)
                    self.assertEqual(row[9], bill["file"])
                for cell, expected in (("E28", case["draft_total"]), ("E29", case["draft_credited"]), ("E30", case["draft_balance"])):
                    self.assertAlmostEqual(values["Abrechnung_Stand"][cell].value, expected, places=2)
                self.assertEqual(values["Mietkonto2025"]["F21"].value, 3600)
                self.assertTrue(formulas["Abrechnung_Stand"]["E30"].value.startswith("="))
                for sheet in values:
                    for row in sheet:
                        self.assertTrue(all(cell.data_type != "e" for cell in row), sheet.title)
            finally:
                values.close()
                formulas.close()

    def test_native_correspondence_and_separate_documents(self):
        for case in self.cases:
            directory = ROOT / "testakten" / case["slug"]
            self.assertEqual(len(list((directory / "aktenstuecke").glob("*.docx"))), 6)
            self.assertFalse(list((directory / "aktenstuecke").glob("*.md")))
            messages = list((directory / "korrespondenz").glob("*.eml"))
            self.assertEqual(len(messages), 14)
            for path in messages:
                message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                self.assertFalse(message.defects, path.name)
                for header in ("From", "To", "Subject", "Date", "Message-ID", "MIME-Version"):
                    self.assertTrue(message[header], (path.name, header))
                self.assertGreater(len(message.get_body(preferencelist=("plain",)).get_content()), 900)

    def test_supplement_vat_totals_and_single_document_boundaries(self):
        self.assertEqual(len(SUPPLEMENT.INVOICES), 15)
        supporting = (
            (SUPPLEMENT.A, "SP-L250919-084.pdf"),
            (SUPPLEMENT.A, "FR-250616-084_Uebernahme.pdf"),
            (SUPPLEMENT.B, "SP-L251024-073.pdf"),
            (SUPPLEMENT.B, "KW-71-0820_Montagebericht.pdf"),
        )
        # Frischer Build und gespeicherte Akte müssen unabhängig vollständig sein.
        for base in (BUILDER.ROOT, ROOT):
            for invoice in SUPPLEMENT.INVOICES:
                path = base / "testakten" / invoice["case"] / invoice["file"]
                with self.subTest(base=base, file=invoice["file"]):
                    self.assertEqual(invoice["net"] + invoice["vat"], invoice["gross"])
                    self.assertTrue(path.is_file(), path)
                    pdf = PdfReader(path)
                    self.assertEqual(len(pdf.pages), 1, path.name)
                    text = pdf.pages[0].extract_text()
                    self.assertIn(invoice["number"], text)
                    self.assertIn(SUPPLEMENT.euro(invoice["gross"]), text)
                    self.assertGreater(len(text), 1100)
            for slug, filename in supporting:
                path = base / "testakten" / slug / "belege" / filename
                with self.subTest(base=base, file=filename):
                    self.assertTrue(path.is_file(), path)
                    pdf = PdfReader(path)
                    self.assertEqual(len(pdf.pages), 1, path.name)
                    self.assertGreater(len(pdf.pages[0].extract_text()), 1100)

    def test_ventilation_correction_preserves_original_and_cancellation(self):
        bills = {row["number"]: row for row in SUPPLEMENT.INVOICES}
        first, credit, final = [bills[number] for number in ("KL-250905-073", "KL-G250917-073", "KL-250917-071")]
        self.assertEqual(first["gross"] + credit["gross"], 0)
        self.assertEqual(final["gross"], Decimal("8092.00"))
        self.assertEqual(first["paid"], "")
        self.assertEqual(credit["paid"], "")
        self.assertEqual(final["paid"], "2025-10-01")
        self.assertIn("Gotenstraße 71", final["site"])

    def test_supplement_register_and_payment_scope(self):
        excluded = {"EK-EB84-LP-26-042", "KL-250811-071", "KL-250905-073", "KL-G250917-073"}
        for base in (BUILDER.ROOT, ROOT):
            for slug in (SUPPLEMENT.A, SUPPLEMENT.B):
                directory = base / "testakten" / slug / "zahlenwerk"
                with self.subTest(base=base, case=slug):
                    register = directory / "Belegnachtrag_2025_2026.csv"
                    self.assertTrue(register.is_file(), register)
                    with register.open(encoding="utf-8") as stream:
                        rows = list(csv.DictReader(stream, delimiter=";"))
                    expected = [row for row in SUPPLEMENT.INVOICES if row["case"] == slug]
                    self.assertEqual(len(rows), len(expected))
                    for row, source in zip(rows, expected):
                        self.assertEqual(row["Belegnummer"], source["number"])
                        self.assertEqual(Decimal(row["Brutto_EUR"]), source["gross"])
                        self.assertEqual(row["Datei"], source["file"])
                        self.assertTrue((directory.parent / row["Datei"]).is_file())
                    payment_file = directory / "Zahlungsdetails_Nachtraege.csv"
                    self.assertTrue(payment_file.is_file(), payment_file)
                    with payment_file.open(encoding="utf-8") as stream:
                        payments = list(csv.DictReader(stream, delimiter=";"))
                    expected_numbers = {bill["number"] for bill in expected} - excluded
                    self.assertEqual(len(payments), len(expected_numbers))
                    self.assertEqual({row["Verwendungszweck"] for row in payments}, expected_numbers)
                    for row in payments:
                        source = next(bill for bill in expected if bill["number"] == row["Verwendungszweck"])
                        self.assertEqual(row["Buchungsdatum"], source["paid"])
                        self.assertEqual(Decimal(row["Belastung_EUR"]), source["gross"])

    def test_charging_work_stays_in_2026_and_private_order_is_separate(self):
        bills = {row["number"]: row for row in SUPPLEMENT.INVOICES}
        for number in ("EK-EB84-TG-26-041", "EK-EB84-LP-26-042", "EK-GO73-TG-26-056"):
            self.assertTrue(bills[number]["day"].startswith("2026-"))
            self.assertIn("2026", bills[number]["period"])
        self.assertEqual(bills["EK-EB84-TG-26-041"]["gross"], Decimal("17850.00"))
        self.assertEqual(bills["EK-GO73-TG-26-056"]["gross"], Decimal("12495.00"))
        self.assertIn("Jens Rabe", bills["EK-EB84-LP-26-042"]["recipient"])

    def test_plugin_entry_and_scope(self):
        directory = ROOT / "betriebskosten-hausverwaltung"
        manifest = json.loads((directory / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], directory.name)
        self.assertLessEqual(len(manifest["description"]), 300)
        self.assertEqual(len(list((directory / "skills").glob("*/SKILL.md"))), 10)
        self.assertTrue((directory / "skills/belege-bis-zur-abrechnung/SKILL.md").is_file())
        mini = (directory / f"{directory.name}-schnellstart.md").read_bytes()
        self.assertLess(len(mini), 7500)
        for path in directory.glob("*-*.md"):
            self.assertNotIn("skills/", str(path.parent.relative_to(directory)))


if __name__ == "__main__":
    unittest.main()
