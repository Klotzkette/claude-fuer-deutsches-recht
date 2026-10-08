#!/usr/bin/env python3
"""Konten, Quellbelege, Anhänge und Auslieferung der Dreijahresakte prüfen."""
import argparse
from collections import defaultdict
from datetime import date
from email import policy
from email.parser import BytesParser
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest
import zipfile

from openpyxl import load_workbook
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_DE, NOTICE_EN, NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "betreuungsrecht"
SLUG = "betreuung-adelheid-pimpernell-dreijahresabrechnung"
CASE = ROOT / "testakten" / SLUG
DATA = json.loads((ROOT / "scripts/data/betreuung-pimpernell.json").read_text())
DIST = None


def validator(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class UnterlagenTest(unittest.TestCase):
    def test_period_and_unique_records(self):
        rows = DATA["transactions"]
        self.assertGreaterEqual(len(rows), 450)
        self.assertEqual(len(rows), len({r["id"] for r in rows}))
        self.assertEqual(DATA["period_start"], "2023-10-01")
        self.assertEqual(DATA["period_end"], "2026-09-30")
        for row in rows:
            self.assertIs(type(row["amount_cents"]), int)
            self.assertLessEqual(DATA["period_start"], row["date"])
            self.assertLessEqual(row["date"], DATA["period_end"])
            date.fromisoformat(row["date"])
        self.assertEqual(len({r["date"][:7] for r in rows}), 36)

    def test_account_balances_and_internal_transfers(self):
        transfers = defaultdict(list)
        for account in DATA["accounts"]:
            net = sum(r["amount_cents"] for r in DATA["transactions"] if r["account"] == account["id"])
            self.assertEqual(account["opening_cents"] + net, account["closing_balance_cents"])
            statements = list((CASE / "02_Konten").glob(f'{account["id"]}_*.pdf'))
            self.assertEqual(len(statements), 36)
        for row in DATA["transactions"]:
            if row.get("transfer_id"):
                transfers[row["transfer_id"]].append(row)
        self.assertTrue(transfers)
        for key, rows in transfers.items():
            with self.subTest(transfer=key):
                self.assertEqual(len(rows), 2)
                self.assertEqual(len({r["account"] for r in rows}), 2)
                self.assertEqual(sum(r["amount_cents"] for r in rows), 0)

    def test_every_booking_has_actual_bank_source(self):
        text = {}
        for row in DATA["transactions"]:
            source = CASE / row["source_file"]
            self.assertTrue(source.is_file(), row["id"])
            if source not in text:
                text[source] = "\n".join(p.extract_text() or "" for p in PdfReader(source).pages)
            self.assertIn(row["id"], text[source])

    def test_invoice_totals_sources_and_payments(self):
        rows = {r["id"]: r for r in DATA["transactions"]}
        self.assertGreaterEqual(len(DATA["invoices"]), 70)
        for inv in DATA["invoices"]:
            with self.subTest(invoice=inv["id"]):
                self.assertEqual(sum(line[1] for line in inv["lines"]), inv["total_cents"])
                path = CASE / inv["source_file"]
                text = "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
                self.assertIn(inv["id"], text)
                for transaction in inv["transaction_ids"]:
                    self.assertIn(transaction, rows)
                    self.assertGreaterEqual(abs(rows[transaction]["amount_cents"]), inv["total_cents"])

    def test_emails_and_attachment_integrity(self):
        files = list(CASE.rglob("*.eml"))
        self.assertGreaterEqual(len(files), 25)
        available = defaultdict(list)
        for path in CASE.rglob("*"):
            if path.is_file():
                available[path.name].append(path)
        ids, attached = set(), 0
        for path in files:
            msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
            for key in ("From", "To", "Date", "Subject", "Message-ID"):
                self.assertTrue(msg[key], f"{path}: {key}")
            self.assertNotIn(str(msg["Message-ID"]), ids)
            ids.add(str(msg["Message-ID"]))
            self.assertFalse(msg.defects, str(path))
            for part in msg.iter_attachments():
                attached += 1
                name = part.get_filename()
                self.assertTrue(available[name], name)
                payload = part.get_payload(decode=True)
                self.assertTrue(any(p.read_bytes() == payload for p in available[name]), name)
        self.assertGreaterEqual(attached, 6)

    def test_workbooks_and_native_formats(self):
        paths = list(CASE.rglob("*.xlsx")) + [PLUGIN / "templates/unterlagen-abrechnung.xlsx"]
        self.assertGreaterEqual(len(paths), 3)
        for path in paths:
            wb = load_workbook(path, data_only=True)
            for ws in wb:
                for row in ws:
                    for cell in row:
                        self.assertNotEqual(cell.data_type, "e", f"{path.name}/{ws.title}/{cell.coordinate}: {cell.value}")
        self.assertGreaterEqual(len(list(CASE.rglob("*.docx"))), 6)
        self.assertGreaterEqual(len(list(CASE.rglob("*.png"))) + len(list(CASE.rglob("*.jpg"))), 3)

    def test_skill_prompt_and_unchanged_old_cases(self):
        skill = PLUGIN / "skills/unterlagen-auswerten-abrechnung-anschreiben/SKILL.md"
        body = skill.read_text()
        self.assertLessEqual(len(body.splitlines()), 500)
        headings = re.findall(r"^## ([1-6])\. ", body, re.M)
        self.assertEqual(headings, list("123456"))
        for token in ("Times New Roman", "11 pt", "ausformuliert"):
            self.assertIn(token, body)
        md = PLUGIN / "betreuungsrecht-unterlagen-werkstatt.md"
        self.assertEqual(md.read_bytes(), md.with_suffix(".txt").read_bytes())
        self.assertGreater(len(md.read_text().split()), 3000)
        self.assertLessEqual(len((PLUGIN / "betreuungsrecht-schnellstart.md").read_bytes()), 7500)
        for case in ("betreuung-schmalfeld-kontodaten-vertraege", "betreuung-hildegard-sauer"):
            self.assertTrue((ROOT / "testakten" / case / "gesamt-pdf" / f"{case}_gesamt.pdf").is_file())

    def test_version_and_route(self):
        version = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())["version"]
        plugins = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"]
        self.assertEqual(next(p["version"] for p in plugins if p["name"] == "betreuungsrecht"), version)
        routes = json.loads((ROOT / "scripts/scoped-release-assets.json").read_text())["assets"]
        self.assertEqual(routes["betreuungsrecht.zip"], "betreuungsrecht-v" + version)

    def test_release_packages(self):
        if DIST is None:
            self.skipTest("Nur bei Paketprüfung")
        # Dieselben Kernprüfungen wie beim Gesamtrelease, auf diese Komponente
        # begrenzt: kein vorgetäuschtes Sammelpaket aller übrigen Akten.
        originals = validator("validate-testakten-release-zips.py")
        singles = validator("validate-testakten-einzelpdf-zips.py")
        original_path = DIST / f"testakte-{SLUG}.zip"
        single_path = DIST / f"testakte-{SLUG}-einzelpdfs.zip"
        originals.assert_same(original_path.name, originals.expected_entries(CASE),
                              originals.zip_entries(original_path, require_notice=True))
        singles.assert_same(single_path.name, ["README.txt", *singles.expected_arcnames(CASE)],
                            singles.zip_entries(single_path, expected_suffix=".pdf"))
        with zipfile.ZipFile(DIST / "betreuungsrecht.zip") as z:
            self.assertIn("skills/unterlagen-auswerten-abrechnung-anschreiben/SKILL.md", z.namelist())
            self.assertIn("templates/unterlagen-abrechnung.xlsx", z.namelist())
            self.assertFalse(any("-werkstatt." in n or n.startswith("testakten/") for n in z.namelist()))
            for name in z.namelist():
                self.assertEqual(z.read(name), (PLUGIN / name).read_bytes(), name)
        for suffix in ("", "-einzelpdfs"):
            with zipfile.ZipFile(DIST / f"testakte-{SLUG}{suffix}.zip") as z:
                self.assertEqual(z.namelist()[0], "README.txt")
                self.assertTrue(z.read("README.txt").startswith(NOTICE_BYTES))
                self.assertFalse(any("/" in n or n.endswith(".md") for n in z.namelist()))
        sums = (DIST / "checksums-sha256.txt").read_text().splitlines()
        for line in sums:
            digest, name = line.split("  ", 1)
            self.assertEqual(hashlib.sha256((DIST / name).read_bytes()).hexdigest(), digest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path)
    args, rest = parser.parse_known_args()
    DIST = args.dist
    unittest.main(argv=[__file__, *rest])
