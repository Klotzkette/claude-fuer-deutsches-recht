#!/usr/bin/env python3
"""Topic-specific structural and native evidence regressions, never a model score."""

import csv
import hashlib
import importlib.util
import json
import re
import unittest
from datetime import date, datetime
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

import yaml
from pypdf import PdfReader

from quality_lab import validate_profile

ROOT = Path(__file__).resolve().parents[1]
SLUG = "vergesellschaftung-artikel-15"
PLUGIN = ROOT / SLUG
CASE = ROOT / "testakten/vergesellschaftung-energienetz-hessen"
FIXTURE = ROOT / f"scripts/fixtures/{SLUG}/case.json"
DATA = json.loads(FIXTURE.read_text(encoding="utf-8"))
PROFILE = json.loads((ROOT / f"quality/evals/{SLUG}.json").read_text(encoding="utf-8"))
W = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def plain(entry):
    if "pages" in entry:
        return "\n".join(p for page in entry["pages"] for p in [page["heading"], *page["paragraphs"]])
    if "rows" in entry:
        return "\n".join(";".join(row) for row in entry["rows"])
    return "\n\n".join(entry["paragraphs"])


def compact(text):
    return " ".join(text.split())


class VergesellschaftungTests(unittest.TestCase):
    def test_manifests_and_skills(self):
        manifests = [json.loads((PLUGIN / folder / "plugin.json").read_text())
                     for folder in (".claude-plugin", ".codex-plugin")]
        self.assertEqual(manifests[0]["version"], manifests[1]["version"])
        for manifest in manifests:
            self.assertEqual(manifest["name"], SLUG)
            self.assertLessEqual(len(manifest["description"]), 300)
            self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 9)
        for path in skills:
            source = path.read_text()
            metadata = yaml.safe_load(source.split("---", 2)[1])
            self.assertEqual(set(metadata), {"name", "description"})
            self.assertEqual(metadata["name"], path.parent.name)
            self.assertRegex(metadata["name"], r"^[a-z0-9-]{1,64}$")
            self.assertTrue(80 <= len(metadata["description"]) <= 1024)
            self.assertGreater(len(source), 3000)
            for number in range(1, 7):
                self.assertIn(f"# {number}.", source)
            self.assertIn("Times New Roman 11 pt", source)
            self.assertIn("../../references/zitierweise.md", source)

    def test_profile_and_editorial_hashes(self):
        validate_profile(PROFILE, SLUG, PLUGIN, ROOT)
        self.assertEqual(len(PROFILE["cases"]), 5)
        for kind, review in (("schnellstart", "mini_review"), ("werkstatt", "workshop_review")):
            raw = (PLUGIN / f"{SLUG}-{kind}.md").read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), PROFILE[review]["sha256"])
            if kind == "schnellstart":
                self.assertLessEqual(len(raw), 7500)
                self.assertLessEqual(len(raw.decode()), 7500)
        self.assertEqual(PROFILE["prompt_workflow_review"]["method"], "desk_review")

    def test_evidence_inventory_and_rubric(self):
        expected = {entry["file"] for entry in DATA["documents"]}
        native = {p.name for p in CASE.iterdir() if p.suffix.lower() in {".pdf", ".docx", ".csv", ".eml", ".txt"}}
        self.assertEqual(len(expected), 11)
        self.assertEqual(native, expected)
        self.assertEqual({e["format"] for e in DATA["documents"]}, {"pdf", "docx", "csv", "eml", "txt"})
        rubric = yaml.safe_load((CASE / "rubric.yaml").read_text())
        self.assertEqual(rubric["plugin"], SLUG)
        self.assertEqual(rubric["checks"][-1]["min"], 11)
        self.assertEqual({p.name for p in CASE.glob("*.md")}, {"README.md"})

    def test_native_text_matches_canonical_source(self):
        for entry in DATA["documents"]:
            path = CASE / entry["file"]
            with self.subTest(file=path.name):
                if entry["format"] == "docx":
                    with ZipFile(path) as package:
                        root = ET.fromstring(package.read("word/document.xml"))
                        paragraphs = ["".join(t.text or "" for t in p.findall(".//w:t", W))
                                      for p in root.findall(".//w:p", W)]
                    native = compact(" ".join(paragraphs))
                    for page in entry["pages"]:
                        self.assertIn(compact(page["heading"]), native)
                        for paragraph in page["paragraphs"]:
                            self.assertIn(compact(paragraph.replace("\n", "")), native)
                elif entry["format"] == "pdf":
                    reader = PdfReader(path)
                    self.assertEqual(len(reader.pages), len(entry["pages"]))
                    for actual, expected in zip(reader.pages, entry["pages"]):
                        native = compact(actual.extract_text())
                        self.assertIn(compact(expected["heading"]), native)
                        for paragraph in expected["paragraphs"]:
                            self.assertIn(compact(paragraph), native)
                        self.assertAlmostEqual(float(actual.mediabox.width), 595.276, places=1)
                elif entry["format"] == "csv":
                    with path.open(encoding="utf-8-sig", newline="") as stream:
                        self.assertEqual(list(csv.reader(stream, delimiter=";")), [entry["columns"], *entry["rows"]])
                elif entry["format"] == "txt":
                    self.assertEqual(path.read_text(), entry["title"] + "\n\n" + plain(entry) + "\n")

    def test_eml_headers_dates_and_bytes(self):
        spec = importlib.util.spec_from_file_location("article15_builder", ROOT / f"scripts/build-{SLUG}-akte.py")
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        for entry in DATA["documents"]:
            if entry["format"] != "eml":
                continue
            raw = (CASE / entry["file"]).read_bytes()
            self.assertEqual(raw, builder.email_bytes(entry))
            message = BytesParser(policy=policy.default).parsebytes(raw)
            self.assertFalse(message.defects)
            self.assertEqual(parsedate_to_datetime(message["Date"]), datetime.fromisoformat(entry["date"]))
            self.assertEqual(str(message["Subject"]), entry["subject"])
            self.assertEqual(message.get_content().replace("\r\n", "\n").rstrip(), plain(entry))
            self.assertEqual(len(list(message.iter_attachments())), 0)
            self.assertNotIn(b"\n", raw.replace(b"\r\n", b""))

    def test_financial_reconciliation_without_value_conflation(self):
        assets = next(e for e in DATA["documents"] if e["file"].startswith("04_"))
        rows = [dict(zip(assets["columns"], row)) for row in assets["rows"]]
        self.assertEqual(sum(Decimal(row["buchwert_eur"]) for row in rows), Decimal("307000000"))
        core = {"N-01", "N-02", "N-03", "N-04", "N-05", "N-09"}
        self.assertEqual(sum(Decimal(r["buchwert_eur"]) for r in rows if r["id"] in core), Decimal("288000000"))
        leased = next(r for r in rows if r["id"] == "N-06")
        self.assertEqual(leased["eigentuemer"], "Leitwerk Systems GmbH")
        self.assertEqual(Decimal(leased["buchwert_eur"]), 0)
        self.assertEqual(next(r for r in rows if r["id"] == "N-08")["land"], "Thüringen")
        finance = next(e for e in DATA["documents"] if e["file"].startswith("08_"))
        values = [dict(zip(finance["columns"], row)) for row in finance["rows"]]
        for group in ("Mittel", "Verwendung"):
            self.assertEqual(sum(Decimal(r["betrag_eur"]) for r in values if r["gruppe"] == group), Decimal("280000000"))
        valuation = {r["position"]: Decimal(r["betrag_eur"]) for r in values if r["gruppe"] == "Bewertung"}
        self.assertEqual(valuation["Finanzverbindlichkeiten"] - valuation["Liquide Mittel"], valuation["Nettoverschuldung"])
        self.assertEqual(valuation["Unternehmensgesamtwert"] - valuation["Nettoverschuldung"], valuation["Eigenkapitalwert"])
        self.assertEqual(sum(s["percent"] for s in DATA["shareholders"]), 100)

    def test_docx_typography(self):
        for path in CASE.glob("*.docx"):
            with ZipFile(path) as package:
                styles = ET.fromstring(package.read("word/styles.xml"))
                for name in ("Normal", "Title", "Heading1"):
                    style = styles.find(f"w:style[@w:styleId='{name}']", W)
                    self.assertIsNotNone(style)
                    fonts = style.find("w:rPr/w:rFonts", W)
                    self.assertEqual(fonts.get(f"{{{W['w']}}}ascii"), "Times New Roman")
                    self.assertFalse(any("theme" in k.lower() for k in fonts.attrib))
                    self.assertIsNone(style.find("w:pPr/w:pBdr", W))
                    self.assertEqual(style.find("w:rPr/w:sz", W).get(f"{{{W['w']}}}val"), "22")

    def test_scope_language_contacts_and_no_answers(self):
        authored = list(PLUGIN.rglob("*.md")) + [FIXTURE]
        for path in authored:
            text = path.read_text()
            self.assertNotIn(chr(167), text)
            self.assertNotIn("Digital Omnibus", text)
        all_evidence = "\n".join(plain(e) for e in DATA["documents"])
        for address in re.findall(r"[\w.+-]+@[\w.-]+", all_evidence):
            self.assertTrue(address.endswith(".example"), address)
        for forbidden in ("Musterlösung", "Erwartungshorizont", "Bewertungskriterien", "generated with AI", "mit KI generiert"):
            self.assertNotIn(forbidden, all_evidence)
        self.assertNotIn("Abschnitt 6 beschriebene Anteilsvariante", all_evidence)
        for entry in DATA["documents"]:
            document_date = (datetime.fromisoformat(entry["date"]).date() if entry["format"] == "eml"
                             else datetime.strptime(entry["date"], "%d.%m.%Y").date()) if "date" in entry else date(2026, 8, 31)
            self.assertLessEqual(document_date, date.fromisoformat(DATA["as_of"]))

    def test_local_markdown_links(self):
        for path in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                self.assertTrue((path.parent / target.split("#")[0]).resolve().exists(), (path, target))


if __name__ == "__main__":
    unittest.main(verbosity=2)
