#!/usr/bin/env python3
"""Prüft die Belegkette der ergänzten Insolvenzreife-Grundakten."""
import csv
from email import policy
from email.parser import BytesParser
import hashlib
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

from pypdf import PdfReader
from insolvenzreife_grundakten import BUSINESS, money

ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "scripts/data/zu-insolvenzfaelle.json").read_text())["cases"]
SELECTION = json.loads((ROOT / "scripts/data/testakten-grundakten-insolvenzreife.json").read_text())


class GrundaktenTest(unittest.TestCase):
    def test_rechnungen_mit_originalforderung_und_leistungsfreigabe(self):
        for case in CASES:
            with self.subTest(case=case["slug"]):
                root = ROOT / "testakten" / case["slug"]
                meta = BUSINESS[case["prefix"]]
                obligations = {item["id"]: item for item in case["obligations"]}
                receivables = {item["id"]: item for item in case["receivables"]}
                for reference in meta["invoice_ids"] + meta["customer_ids"]:
                    outgoing = reference in meta["customer_ids"]
                    item = (receivables if outgoing else obligations)[reference]
                    suffix = "_Ausgangsrechnung.pdf" if outgoing else "_Rechnung.pdf"
                    file = root / "04_Originalbelege" / (reference + suffix)
                    text = "\n".join(page.extract_text() for page in PdfReader(file).pages)
                    self.assertIn(reference, text)
                    self.assertIn(money(item["amount_cents"]).replace(" EUR", ""), text)
                    self.assertIn("Umsatzsteuer 19 %", text)
                    self.assertIn("Steuernummer", text)
                    if outgoing:
                        accepted = root / "04_Originalbelege" / (reference + "_Leistungsfreigabe.pdf")
                        txt = "\n".join(page.extract_text() for page in PdfReader(accepted).pages)
                        self.assertIn(money(item["amount_cents"]), txt)

    def test_lohnstapel_ergaenzt_sammelbuchung_ohne_neuen_geldfluss(self):
        for case in CASES:
            with self.subTest(case=case["slug"]):
                prefix = case["prefix"]
                root = ROOT / "testakten" / case["slug"]
                with (root / "02_Buchhaltung" / f"06_{prefix}_Lohnzahlstapel_Mai.csv").open(encoding="utf-8-sig") as stream:
                    rows = list(csv.DictReader(stream, delimiter=";"))
                original = next(item for item in case["obligations"] if item["id"] == prefix + "-LOHN-01")
                self.assertEqual(len(rows), case["staff"])
                self.assertEqual(sum(int(row["Nettoauszahlung_Cent"]) for row in rows), original["amount_cents"])
                self.assertEqual({row["Sammelbuchung"] for row in rows}, {original["payment_id"]})
                self.assertEqual({row["Ausfuehrungstag"] for row in rows}, {original["paid_on"]})

    def test_xml_ist_reiner_export_der_vorhandenen_posten(self):
        for case in CASES:
            with self.subTest(case=case["slug"]):
                prefix = case["prefix"]
                root = ROOT / "testakten" / case["slug"]
                source = {item["id"]: item for item in case["obligations"]}
                xml = ET.parse(root / "02_Buchhaltung" / f"08_{prefix}_Zahlungsausgang_ERP.xml").getroot()
                self.assertEqual(xml.get("format"), "Interner ERP-Export")
                for item in xml.findall("Vorgang"):
                    expected = source[item.get("beleg")]
                    self.assertEqual(int(item.findtext("BetragCent")), expected["amount_cents"])
                    self.assertEqual(item.findtext("Empfaenger"), expected["creditor"])
                    self.assertEqual(item.findtext("FaelligkeitLautStamm"), expected["due_on"])
                    self.assertEqual(item.findtext("Bankreferenz"), expected.get("payment_id") or "")

    def test_mailanhaenge_sind_identische_originalbelege(self):
        for case in CASES:
            with self.subTest(case=case["slug"]):
                root = ROOT / "testakten" / case["slug"]
                path = root / "08_Uebergabe" / (case["prefix"] + "-MAIL-RECH.eml")
                mail = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                attachments = list(mail.iter_attachments())
                self.assertEqual(len(attachments), 2)
                for part in attachments:
                    expected = (root / "04_Originalbelege" / part.get_filename()).read_bytes()
                    self.assertEqual(hashlib.sha256(part.get_payload(decode=True)).hexdigest(), hashlib.sha256(expected).hexdigest())

    def test_grundakte_hat_keine_verfahrensdatei_oder_musterloesung(self):
        for case in CASES:
            with self.subTest(case=case["slug"]):
                root = ROOT / "testakten" / case["slug"]
                selection = SELECTION[case["slug"]]
                self.assertEqual(len(selection), len(set(selection)))
                self.assertGreaterEqual(len(selection), 70)
                for name in selection:
                    self.assertTrue((root / name).is_file(), name)
                    self.assertNotIn("10_Verfahren/", name)
                    self.assertNotIn("gesamt-pdf/", name)
                    self.assertNotIn("control", name.lower())
                    self.assertNotIn("nachbesprechung", name.lower())


if __name__ == "__main__":
    unittest.main()
