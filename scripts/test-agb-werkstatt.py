#!/usr/bin/env python3
"""Struktur-, Paket- und Aktenregressionen; kein modellgestützter Rechtsratstest."""
import csv
from decimal import Decimal
from email import policy
from email.parser import BytesParser
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "agb-werkstatt"
CASES = json.loads((ROOT / "scripts/data/agb-werkstatt-akten.json").read_text())["cases"]
spec = importlib.util.spec_from_file_location("agb_release", ROOT / "scripts/build-agb-werkstatt-release.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class AgbTests(unittest.TestCase):
    def test_download_notices_and_local_file_references(self):
        checks = builder.module("validate-testakten-readme-downloads.py")
        errors = []
        for case in CASES:
            checks.validate_local_readme(case["slug"], ROOT / "testakten" / case["slug"], errors)
        checks.validate_download_notices("agb-werkstatt/README.md", (PLUGIN / "README.md").read_text(), errors)
        self.assertEqual(errors, [])

    def test_original_document_quality(self):
        quality = builder.module("validate-testakten-dokumentqualitaet.py")
        errors = []
        checked = 0
        for case in CASES:
            directory = ROOT / "testakten" / case["slug"]
            for group in ("documents", "emails", "raw"):
                for item in case[group]:
                    path = directory / item["path"]
                    text = quality.export_text(path)
                    checked += 1
                    if quality.has_unexplained_synthetic_contact(text, path):
                        errors.append(f"{path.name}: unerklärte Kontaktdaten")
                    errors.extend(f"{path.name}: {error}" for error in quality.language_prose_errors(text, path))
                    for label, pattern in quality.EXPORT_META_PATTERNS.items():
                        if pattern.search(text):
                            errors.append(f"{path.name}: {label}")
                    if path.suffix in (".pdf", ".docx", ".eml", ".txt"):
                        self.assertGreaterEqual(len(text.strip()), quality.MIN_FORMAL_TEXT, path)
                    if path.suffix == ".eml":
                        errors.extend(quality.eml_quality_errors(path))
                    if path.suffix == ".pdf":
                        self.assertTrue(quality.pdf_is_a4(path), path)
                    self.assertNotIn("§", text, path)
        self.assertEqual(checked, 36)
        self.assertEqual(errors, [])

    def test_eleven_distinct_skills_and_main(self):
        skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 11)
        self.assertTrue((PLUGIN / "skills/agb-hauptproblem-loesen/SKILL.md").is_file())
        for path in skills:
            text = path.read_text()
            for heading in ("## 1 ", "## 2 ", "## 3 ", "## 4 ", "## 5 ", "## 6 "):
                self.assertIn(heading, text, path.name)
            self.assertRegex(text, r"(BGH|EuGH),")
            self.assertIn("Paragraf", text)
            self.assertIn("vollständigen", text)
            self.assertIn("11 pt", text)

    def test_prompts_are_self_contained_and_compact(self):
        for name in builder.PROMPTS:
            text = (PLUGIN / name).read_text()
            self.assertIn("XI ZR 61/23", text)
            self.assertIn("C-472/23", text)
            self.assertIn("356a", text)
            self.assertNotIn("§", text)
            self.assertNotIn("**", text)
            if "werkstatt-werkstatt" not in name:
                self.assertLessEqual(len(text.encode()), 7500)
                self.assertLessEqual(len(text), 7500)

    def test_source_limits_are_explicit(self):
        text = (PLUGIN / "references/rechtsprechung.md").read_text()
        for boundary in ("polnische", "Hauptleistung", "technisch", "keine vollständige"):
            self.assertIn(boundary, text)
        self.assertIn("9. Oktober 2026", text)

    def test_package_reproducible_and_no_prompt_installation(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "one", Path(tmp) / "two"
            builder.build_plugin(first)
            builder.build_plugin(second)
            for path in first.iterdir():
                self.assertEqual(path.read_bytes(), (second / path.name).read_bytes())
            with zipfile.ZipFile(first / "agb-werkstatt.zip") as archive:
                self.assertEqual(len([n for n in archive.namelist() if n.endswith("/SKILL.md")]), 11)
                self.assertIn(".claude-plugin/plugin.json", archive.namelist())
                self.assertFalse(any(n.endswith(tuple(builder.PROMPTS)) for n in archive.namelist()))
                self.assertFalse(any("testakten/" in n for n in archive.namelist()))

    def test_cases_are_complete_and_native(self):
        from docx import Document
        from pypdf import PdfReader
        for case in CASES:
            directory = ROOT / "testakten" / case["slug"]
            paths = [item["path"] for group in ("documents", "emails", "raw") for item in case[group]]
            self.assertEqual(len(paths), 12)
            self.assertEqual(len(paths), len(set(paths)))
            for item in case["documents"]:
                path = directory / item["path"]
                self.assertTrue(path.is_file(), path)
                if path.suffix == ".docx":
                    text = "\n".join(p.text for p in Document(path).paragraphs)
                else:
                    text = "\n".join(p.extract_text() for p in PdfReader(path).pages)
                self.assertGreater(len(text), 700, path)
                self.assertNotIn("Testakte", text)
                self.assertNotIn("Musterlösung", text)
                self.assertNotIn("§", text)
            self.assertTrue((directory / "gesamt-pdf" / f"{case['slug']}_gesamt.pdf").is_file())

    def test_email_headers_and_attachment_bytes(self):
        for case in CASES:
            directory = ROOT / "testakten" / case["slug"]
            docs = {item["id"]: directory / item["path"] for item in case["documents"]}
            for item in case["emails"]:
                message = BytesParser(policy=policy.default).parsebytes((directory / item["path"]).read_bytes())
                for header in ("From", "To", "Date", "Subject", "Message-ID", "MIME-Version"):
                    self.assertTrue(message[header])
                attachments = {p.get_filename(): p.get_payload(decode=True) for p in message.iter_attachments()}
                self.assertEqual(set(attachments), {docs[i].name for i in item["attachments"]})
                for identifier in item["attachments"]:
                    path = docs[identifier]
                    self.assertEqual(attachments[path.name], path.read_bytes())

    def test_csv_rows_and_invoice_totals(self):
        for case in CASES:
            for path in (ROOT / "testakten" / case["slug"]).glob("*.csv"):
                rows = list(csv.reader(io.StringIO(path.read_text()), delimiter=";"))
                self.assertGreaterEqual(len(rows), 5)
                self.assertEqual(len({len(row) for row in rows}), 1)
        D = Decimal
        invoices = [doc for case in CASES for doc in case["documents"] if "table" in doc]
        self.assertEqual(len(invoices), 3)
        for invoice in invoices:
            def amount(value):
                return D(value.removesuffix(" Euro").replace(".", "").replace(",", "."))
            rows = invoice["table"]
            self.assertEqual(rows[-1][0], "Gesamt")
            self.assertEqual(sum(amount(row[-1]) for row in rows[1:-1]), amount(rows[-1][-1]), invoice["id"])
            self.assertIn(rows[-1][-1], "\n".join(invoice["paragraphs"]), invoice["id"])
        self.assertEqual(D("178") + D("35.10") + D("5.90"), D("219"))
        self.assertEqual(sum(map(D, ("150", "45", "75", "28", "12"))), D("310"))
        self.assertEqual(D("64") + D("29"), D("93"))
        self.assertEqual(D("2520") * D("1.07"), D("2696.40"))
        self.assertEqual(D("1348.20") * 2, D("2696.40"))

    def test_archives_flat_and_notices_outside_pdfs(self):
        from pypdf import PdfReader
        originals = builder.module("build-testakten-release-zips.py")
        pdfs = builder.module("build-testakten-einzelpdf-zips.py")
        with tempfile.TemporaryDirectory() as tmp:
            for case in CASES:
                directory = ROOT / "testakten" / case["slug"]
                for make in (originals.build_single, pdfs.build_single):
                    path, count = make(directory, Path(tmp))
                    self.assertGreaterEqual(count, 12)
                    with zipfile.ZipFile(path) as archive:
                        names = archive.namelist()
                        self.assertTrue(all("/" not in name for name in names))
                        self.assertFalse(any(name.lower().endswith(".md") for name in names))
                        notice = archive.read("README.txt").decode()
                        from testakte_disclaimer import NOTICE_TEXT
                        self.assertEqual(notice, NOTICE_TEXT)
                        self.assertIn("This test case file was generated with AI", notice)
                        if "-einzelpdfs" in path.name:
                            self.assertEqual(len([n for n in names if n.endswith(".pdf")]), 12)
                        for name in names:
                            if name.endswith(".pdf"):
                                text = "\n".join(p.extract_text() for p in PdfReader(io.BytesIO(archive.read(name))).pages)
                                self.assertNotIn("Diese Testakte wurde mit KI generiert", text)
                                self.assertNotIn("This test case file was generated with AI", text)


if __name__ == "__main__":
    unittest.main()
