#!/usr/bin/env python3
"""Fallbezogene Inhalts-, Container-, Rechen- und Exportprüfungen.

--render-all erzeugt QA-PNGs ausschließlich in einem Tempverzeichnis außerhalb des Repos.
--recalc-test prüft Grenzwerte in einer Wegwerfkopie mit derselben Office-Runtime.
Keine festgeschriebenen privaten Toolpfade; SOFFICE und PATH werden übernommen.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

from docx import Document
from openpyxl import load_workbook
from PIL import Image
from pypdf import PdfReader
import yaml

from testakte_file_filter import include_in_working_dump
from testakte_download_notices import missing_notice_positions
from testakte_office_pdf import render_office_batch, uncached_formula_cells


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("kassel_builder", ROOT / "scripts/build-vertragserstellung-kassel-akte.py")
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
CASE, FILES = BUILDER.CASE, BUILDER.FILES
NOTICE_DE = "Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr."
NOTICE_EN = "This test case file was generated with AI and is an experiment. Use at your own responsibility and risk."


def csv_rows(number):
    with (CASE / FILES[number]).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def euro(value):
    return Decimal(value.replace(",", "."))


def source_text(path):
    if path.suffix == ".pdf":
        return "\n".join(page.extract_text() for page in PdfReader(path).pages)
    if path.suffix == ".docx":
        return "\n".join(p.text for p in Document(path).paragraphs)
    if path.suffix == ".eml":
        msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        return msg.get_body(preferencelist=("plain",)).get_content()
    if path.suffix == ".xlsx":
        wb = load_workbook(path, data_only=True)
        return "\n".join(str(c.value) for sh in wb for row in sh for c in row if c.value is not None)
    if path.suffix == ".png":
        return ""
    return path.read_text(encoding="utf-8")


class CaseTests(unittest.TestCase):
    def test_01_inventory_and_export_boundary(self):
        self.assertFalse((CASE / ".qa").exists())
        self.assertEqual({p.name for p in CASE.iterdir()}, set(FILES.values()) | {"README.md", "rubric.yaml", "gesamt-pdf"})
        exported = {p.name for p in CASE.rglob("*") if include_in_working_dump(p, CASE)}
        self.assertEqual(exported, set(FILES.values()))
        self.assertEqual(Counter(Path(p).suffix for p in exported), {
            ".pdf": 11, ".docx": 2, ".eml": 6, ".csv": 3, ".txt": 2, ".xlsx": 1, ".png": 1})
        for name in FILES.values():
            self.assertGreater((CASE / name).stat().st_size, 500, name)

    def test_02_email_headers_and_real_attachments(self):
        ids = {}
        messages = []
        for path in CASE.glob("*.eml"):
            msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
            for header in ["From", "To", "Date", "Subject", "Message-ID", "MIME-Version", "Content-Type", "Received", "Return-Path"]:
                self.assertTrue(msg[header], f"{path.name}: {header}")
            self.assertFalse(msg.defects, path.name)
            self.assertNotIn(msg["Message-ID"], ids)
            ids[msg["Message-ID"]] = parsedate_to_datetime(msg["Date"])
            self.assertIsNotNone(ids[msg["Message-ID"]].tzinfo)
            body = msg.get_body(preferencelist=("plain",))
            self.assertEqual(body.get_content_charset(), "utf-8")
            self.assertTrue(body["Content-Transfer-Encoding"])
            self.assertIn("Grüßen", body.get_content())
            self.assertGreater(len(body.get_content().split()), 145)
            filenames = []
            for part in msg.iter_attachments():
                filename = part.get_filename()
                filenames.append(filename)
                self.assertIn(filename, FILES.values())
                self.assertEqual(part.get_payload(decode=True), (CASE / filename).read_bytes(), filename)
                self.assertIn(filename, body.get_content())
                dated = re.search(r"2026-\d{2}-\d{2}", filename)
                if dated:
                    self.assertLessEqual(datetime.fromisoformat(dated.group()).date(), ids[msg["Message-ID"]].date())
            self.assertEqual(len(filenames), len(set(filenames)))
            messages.append(msg)
        for msg in messages:
            if msg["In-Reply-To"]:
                self.assertIn(msg["In-Reply-To"], ids)
                self.assertIn(msg["In-Reply-To"], msg["References"])
                self.assertLess(ids[msg["In-Reply-To"]], ids[msg["Message-ID"]])
        self.assertEqual(sum(len(list(m.iter_attachments())) for m in messages), 10)

    def test_03_all_named_source_files_exist(self):
        pattern = r"\b\d{2}_[\w.-]+\.(?:docx|xlsx|pdf|csv|eml|png|txt)\b"
        references = set()
        for name in FILES.values():
            for filename in re.findall(pattern, source_text(CASE / name)):
                self.assertIn(filename, FILES.values(), (name, filename))
                self.assertTrue((CASE / filename).is_file())
                references.add(filename)
        self.assertIn(FILES[17], references)
        self.assertIn(FILES[14], references)
        self.assertIn(FILES[23], references)
        for filename in re.findall(pattern, (CASE / FILES[18]).read_text()):
            self.assertTrue((CASE / filename).is_file())

    def test_04_no_meta_in_evidence(self):
        forbidden = [NOTICE_DE, NOTICE_EN, "Musterlösung", "Lösungsmatrix", "Rechtsgutachten", "Erwartungshorizont",
                     "Testakte", "KI generiert", "Lorem ipsum", "Inhalt folgt", "[Datum", "/Users/", ".example"]
        for name in FILES.values():
            text = source_text(CASE / name)
            for marker in forbidden:
                self.assertNotIn(marker.lower(), text.lower(), (name, marker))

    def test_05_csv_utf8_and_quoting(self):
        for number in (4, 11, 24):
            path = CASE / FILES[number]
            raw = path.read_bytes()
            self.assertIn(b"\r\n", raw)
            text = raw.decode("utf-8")
            self.assertRegex(text, "[äöüÄÖÜß]")
            self.assertGreaterEqual(len(csv_rows(number)), 4)
            rows = list(csv.reader(text.splitlines(), delimiter=";", strict=True))
            self.assertEqual(len({len(r) for r in rows}), 1)
            for line in text.splitlines():
                self.assertTrue(line.startswith('"') and line.endswith('"'))
        self.assertIn('""P-17""', (CASE / FILES[4]).read_text())

    def test_06_shift_times_and_counts(self):
        rows = csv_rows(4)
        self.assertEqual(len(rows), 14)
        self.assertEqual(sum(int(r["Stillstand_min"]) for r in rows), 210)
        self.assertEqual(sum(int(r["Reduziert_min"]) for r in rows), 165)
        for row in rows:
            duration = (datetime.fromisoformat(row["Schichtende"]) - datetime.fromisoformat(row["Schichtbeginn"])).total_seconds() / 60
            self.assertEqual(duration, 480)
            self.assertLessEqual(int(row["Stillstand_min"]) + int(row["Reduziert_min"]), duration)
            self.assertGreater(int(row["Gutbogen"]), 0)
        event = source_text(CASE / FILES[8])
        note = source_text(CASE / FILES[7])
        for time in ["00:40", "00:48", "01:25", "03:25", "04:10", "06:55"]:
            self.assertIn(time, event)
            self.assertIn(time, note)

    def test_07_material_consumption_and_invoices(self):
        material = csv_rows(24)
        for row in material:
            self.assertEqual(euro(row["Menge"]) * euro(row["Einzel_netto_EUR"]), euro(row["Gesamt_netto_EUR"]))
        self.assertEqual(sum(euro(r["Gesamt_netto_EUR"]) for r in material), Decimal("1283"))
        self.assertEqual(sum(euro(r["Gesamt_netto_EUR"]) for r in material if r["Zuordnung"] == "Wartungskontingent"), Decimal("381"))
        parts = sum(euro(r["Gesamt_netto_EUR"]) for r in material if r["Beleg"] == "SR-260912")
        net = 4 * Decimal("112") + Decimal("240") + Decimal("145") + parts
        gross = net + (net * Decimal("0.19")).quantize(Decimal("0.01"))
        self.assertEqual(net, Decimal("1735"))
        self.assertEqual(gross, Decimal("2064.65"))
        invoice = source_text(CASE / FILES[10])
        for amount in ["448,00", "240,00", "145,00", "680,00", "180,00", "42,00", "1.735,00", "329,65", "2.064,65"]:
            self.assertIn(amount, invoice)

    def test_08_payments(self):
        payments = csv_rows(11)
        q3 = sum(euro(r["Betrag_EUR"]) for r in payments if r["Rechnung"] == "WS-260701")
        service = sum(euro(r["Betrag_EUR"]) for r in payments if r["Rechnung"] == "WS-260914")
        self.assertEqual(q3, Decimal("5712"))
        self.assertEqual(service, Decimal("1500"))
        self.assertEqual(Decimal("2064.65") - service, Decimal("564.65"))
        text = source_text(CASE / FILES[21])
        self.assertIn("564,65", text)
        self.assertIn("keine abschließende Kürzung", text)

    def test_09_complete_editable_contracts_and_font(self):
        for number in [16, 20]:
            doc = Document(CASE / FILES[number])
            text = "\n".join(p.text for p in doc.paragraphs)
            self.assertGreater(len(text.split()), 1300)
            self.assertIn("noch nicht unterzeichnet", text)
            self.assertIn("Unterzeichnung steht aus", text)
            self.assertIn("Sehr geehrte Vertragspartner", text)
            headings = [p.text for p in doc.paragraphs if p.style.name == "Heading 1"]
            self.assertEqual([int(h.split()[0]) for h in headings], list(range(1, 16)))
            self.assertEqual(doc.styles["Normal"].font.name, "Times New Roman")
            self.assertEqual(doc.styles["Normal"].font.size.pt, 11)
            self.assertTrue(any("Maren Brückner" in p.text for p in doc.paragraphs[-4:]))
            self.assertTrue(any("Dirk Seidel" in p.text for p in doc.paragraphs[-4:]))
            for i, p in enumerate(doc.paragraphs):
                if p.style.name == "Heading 1":
                    self.assertEqual(doc.paragraphs[i + 1].text, "")

    def test_10_workbook_caches_and_independent_totals(self):
        path = CASE / FILES[22]
        self.assertFalse(uncached_formula_cells(path))
        values = load_workbook(path, data_only=True)
        formulas = load_workbook(path, data_only=False)
        self.assertEqual(values.sheetnames, ["Vergleich", "Ansätze"])
        for ws in formulas:
            for row in ws:
                for cell in row:
                    if cell.data_type == "f":
                        value = values[ws.title][cell.coordinate]
                        self.assertIsInstance(value.value, (int, float), (ws.title, cell.coordinate))
                        self.assertNotEqual(value.data_type, "e")
        checks = {"B6": 32640, "C6": 35520, "D6": 29400, "B9": 37840, "C9": 40720,
                  "D9": 33600, "C11": 48456.8, "D11": 39984, "C12": 7120,
                  "C14": 2960, "C15": 10900, "B18": 0, "C18": 0, "D18": 0,
                  "B19": 34272, "C19": 37296, "D19": 30282}
        for coord, expected in checks.items():
            self.assertAlmostEqual(values["Vergleich"][coord].value, expected, places=2, msg=coord)
        self.assertAlmostEqual(values["Ansätze"]["D24"].value, 564.65, places=2)
        self.assertEqual(values["Ansätze"]["D23"].value, 0)
        self.assertEqual(values["Ansätze"]["B5"].value + values["Ansätze"]["B6"].value, 10900)

    def test_11_pdf_letters_and_last_pages(self):
        for path in CASE.glob("*.pdf"):
            reader = PdfReader(path)
            text = "\n".join(p.extract_text() for p in reader.pages)
            self.assertIn("Sehr geehrte", text, path.name)
            self.assertIn("Bezug:", text, path.name)
            self.assertIn("Mit freundlichen Grüßen", text, path.name)
            self.assertRegex(text, "Fuldabogen Spezialdruck|Werkspur Maschinenservice")
            self.assertGreater(len(reader.pages[-1].extract_text().split()), 110, path.name)
            self.assertNotIn("\ufffd", text)
            for page in reader.pages:
                self.assertAlmostEqual(float(page.mediabox.width), 595.2756, places=1)
                fonts = page["/Resources"].get("/Font", {})
                self.assertTrue(any("TimesNewRoman" in str(font.get_object().get("/BaseFont", ""))
                                    or "LiberationSerif" in str(font.get_object().get("/BaseFont", ""))
                                    for font in fonts.values()), path.name)

    def test_12_readme_warnings_and_inventory(self):
        text = (CASE / "README.md").read_text()
        self.assertGreaterEqual(text.count(NOTICE_DE), 1)
        self.assertEqual(text.count(NOTICE_DE), text.count(NOTICE_EN))
        self.assertFalse(missing_notice_positions(text, case_readme=True))
        self.assertEqual(text.count("<!-- BEGIN gesamt-pdf-section (autogen) -->"), 1)
        self.assertEqual(text.count("<!-- END gesamt-pdf-section (autogen) -->"), 1)
        self.assertIn("26 eigenständige Quellen", text)
        self.assertIn("English:", text)
        self.assertIn("-einzelpdfs.zip", text)
        for name in FILES.values():
            self.assertIn(name, text)

    def test_13_specific_rubric(self):
        rubric = yaml.safe_load((CASE / "rubric.yaml").read_text())
        self.assertEqual(rubric["plugin"], "vertragserstellung")
        ids = [c["id"] for c in rubric["checks"]]
        self.assertEqual(len(ids), len(set(ids)))
        for check in rubric["checks"]:
            if check["check_type"] == "file_exists":
                self.assertTrue((CASE / check["path"]).is_file())
        self.assertFalse(include_in_working_dump(CASE / "rubric.yaml", CASE))

    def test_14_image_container(self):
        with Image.open(CASE / FILES[17]) as im:
            self.assertEqual(im.format, "PNG")
            self.assertGreaterEqual(im.width, 1500)
            self.assertGreaterEqual(im.height, 1000)
            self.assertLess(im.convert("L").getextrema()[0], 60)

    def test_15_combined_pdf(self):
        path = CASE / "gesamt-pdf" / f"{BUILDER.SLUG}_gesamt.pdf"
        self.assertTrue(path.is_file(), "Gesamt-PDF gezielt mit vorhandenem Builder erzeugen")
        reader = PdfReader(path)
        text = "\n".join(p.extract_text() for p in reader.pages)
        self.assertGreater(len(reader.pages), 26)
        for notice in [NOTICE_DE, NOTICE_EN, "Erwartungshorizont", "rubric.yaml"]:
            self.assertNotIn(notice, text)
        for name in FILES.values():
            self.assertIn(name, text)


def render_all():
    qa = Path(tempfile.mkdtemp(prefix="vertragserstellung-kassel-qa-"))
    rendered = render_office_batch([CASE / FILES[n] for n in [16, 20, 22]])
    if len(rendered) != 3:
        raise RuntimeError("Nicht alle Office-Dateien konnten nativ gerendert werden.")
    office = qa / "office"
    office.mkdir(exist_ok=True)
    paths = list(CASE.glob("*.pdf"))
    for source, data in rendered.items():
        target = office / (source.stem + ".pdf")
        target.write_bytes(data)
        paths.append(target)
    renderer = shutil.which("pdftoppm")
    if not renderer:
        raise RuntimeError("Poppler fehlt im PATH.")
    manifest = []
    for path in sorted(paths):
        directory = qa / "pages" / path.stem
        directory.mkdir(parents=True, exist_ok=True)
        subprocess.run([renderer, "-r", "120", "-png", str(path), str(directory / "page")],
                       check=True, stdout=subprocess.DEVNULL, timeout=120)
        pages = list(PdfReader(path).pages)
        manifest.append({"file": path.name, "pages": len(pages),
                         "page_images": [str(p.relative_to(qa)) for p in sorted(directory.glob("page-*.png"))]})
    (qa / "render-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print("Gerendert:", sum(m["pages"] for m in manifest), "Seiten in", len(manifest), "Dokumenten; QA:", qa)


def test_recalculation():
    original = CASE / FILES[22]
    # Jede Mutation startet aus derselben Originalfassung; die Aktenquelle bleibt unberührt.
    cases = [
        ({"B5": 4800, "B6": 4800}, {"C14": 2720, "C9": 37840}),
        ({"B5": 4801, "B6": 4800}, {"C14": 2960, "C9": 40720}),
        ({"B7": 0}, {"C7": 0, "C9": 40320, "D9": 33600}),
        ({"B18": 65}, {"C18": 3125, "D18": 575, "C9": 43845, "D9": 34175}),
    ]
    for changes, expected in cases:
        with tempfile.TemporaryDirectory(prefix="kassel-calc-test-") as temp:
            copy = Path(temp) / "mutation.xlsx"
            BUILDER.make_workbook(copy, changes)
            result = load_workbook(copy, data_only=True)["Vergleich"]
            for coord, value in expected.items():
                actual = result[coord].value
                if abs(actual - value) > 0.005:
                    raise AssertionError((changes, coord, actual, value))
    print("Office-Grenzwerttest: vier Eingabevarianten erfolgreich; Original unverändert")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-all", action="store_true")
    parser.add_argument("--recalc-test", action="store_true")
    args = parser.parse_args()
    if args.render_all:
        render_all()
    if args.recalc_test:
        test_recalculation()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(CaseTests))
    raise SystemExit(not result.wasSuccessful())
