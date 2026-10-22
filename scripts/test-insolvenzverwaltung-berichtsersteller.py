#!/usr/bin/env python3
"""Quellen-, Struktur-, Akten- und Releaseprüfungen für den Berichtsersteller."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote
import zipfile
from zoneinfo import ZoneInfo

from docx import Document
from openpyxl import load_workbook
from pypdf import PdfReader
import yaml

from quality_lab import validate_profile
from testakte_disclaimer import NOTICE_BYTES
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import working_dump_archive_pairs


ROOT = Path(__file__).resolve().parents[1]
NAME = "insolvenzverwaltung-berichtsersteller"
VERSION = "1.1.0"
PLUGIN = ROOT / NAME
CASES = (
    "insolvenzverwaltung-mainbogen-laborsoftware-wuerzburg",
    "insolvenzverwaltung-nordlicht-handels-kiel",
    "insolvenzverwaltung-moebelwerk-havelberg-regelverfahren",
    "insolvenzverwaltung-klangbogen-buehnentechnik-bamberg",
)
DIST: Path | None = None


def module(filename: str):
    path = ROOT / "scripts" / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    result = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(result)
    return result


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def docx_text(path: Path) -> str:
    document = Document(path)
    lines = [p.text for p in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            lines.append(" | ".join(cell.text for cell in row.cells))
    return "\n".join(lines)


class BerichtserstellerTest(unittest.TestCase):
    def test_release_font_discovery_covers_ubuntu_and_fontconfig(self):
        builder = module("build-insolvenzverwaltung-berichtsersteller-release.py")
        directories = {directory for directory, _, _ in builder.FONT_CANDIDATES}
        self.assertIn(Path("/usr/share/fonts/truetype/liberation"), directories)
        self.assertIn(Path("/usr/share/fonts/truetype/liberation2"), directories)
        with tempfile.TemporaryDirectory() as temporary:
            regular = Path(temporary) / "LiberationSerif-Regular.ttf"
            bold = Path(temporary) / "LiberationSerif-Bold.ttf"
            regular.touch()
            bold.touch()
            result = subprocess.CompletedProcess(
                args=("fc-match",),
                returncode=0,
                stdout=f"Liberation Serif\tBold\t{bold}\n",
                stderr="",
            )
            with patch.object(builder.shutil, "which", return_value="/usr/bin/fc-match"), patch.object(builder.subprocess, "run", return_value=result):
                self.assertEqual(builder.fontconfig_path("Liberation Serif", "Bold"), bold)

    def test_manifests_marketplace_and_skill_contract(self):
        for relative in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
            manifest = json.loads((PLUGIN / relative).read_text())
            self.assertEqual((manifest["name"], manifest["version"]), (NAME, VERSION))
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = [p for p in market["plugins"] if p["name"] == NAME]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["source"], "./" + NAME)
        self.assertEqual(entries[0]["version"], VERSION)
        skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 11)
        self.assertEqual(sum(path.parent.name == "berichtserstellung-steuern" for path in skills), 1)
        for path in skills:
            text = path.read_text(encoding="utf-8")
            front = yaml.safe_load(text.split("---", 2)[1])
            self.assertEqual(set(front), {"name", "description"})
            self.assertEqual(front["name"], path.parent.name)
            self.assertLessEqual(len(front["description"]), 360)
            self.assertNotIn("§", front["description"])
            self.assertNotIn("im Plugin", front["description"])
            self.assertEqual(re.findall(r"(?m)^## ([1-6])\. ", text), list("123456"))
            self.assertGreaterEqual(len(text.split()), 1000, path)
            for required in ("Times New Roman", "11 pt", "ausformuliert", "Trägt nicht"):
                self.assertIn(required, text)
            for target in re.findall(r"\]\(([^ )]+)", text):
                if target.startswith(("http:", "https:", "#", "mailto:")):
                    continue
                destination = (path.parent / unquote(target.split("#")[0])).resolve()
                self.assertTrue(destination.exists(), f"{path}: {target}")

    def test_prompts_are_independent_bounded_and_reviewed(self):
        workshop = PLUGIN / f"{NAME}-werkstatt.md"
        mini = PLUGIN / f"{NAME}-schnellstart.md"
        self.assertEqual(workshop.read_bytes(), workshop.with_suffix(".txt").read_bytes())
        self.assertEqual(mini.read_bytes(), mini.with_suffix(".txt").read_bytes())
        self.assertLessEqual(mini.stat().st_size, 7500)
        self.assertGreaterEqual(len(workshop.read_text().split()), 4000)
        for text in (workshop.read_text(), mini.read_text()):
            for required in ("Zwischenbericht", "Schlussbericht", "Schlussrechnung", "Schlussverzeichnis", "menschliche Freigabe"):
                self.assertIn(required, text)
        profile = json.loads((ROOT / "quality/evals" / f"{NAME}.json").read_text())
        validate_profile(profile, NAME, PLUGIN)
        self.assertGreaterEqual(len(profile["sources"]), 10)
        self.assertGreaterEqual(len(profile["cases"]), 4)

    def test_sources_are_official_and_decision_limits_are_explicit(self):
        sources = (PLUGIN / "references/rechtsquellen.md").read_text()
        self.assertIn("https://www.gesetze-im-internet.de/inso/__58.html", sources)
        self.assertIn("https://www.gesetze-im-internet.de/inso/__66.html", sources)
        for section in ("IX ZB 19/20", "IX ZR 177/15", "IX ZB 16/14", "IX ZB 35/21", "IX ZB 143/11", "IX ZB 5/24", "IX ZB 13/25", "IX ZB 45/25"):
            self.assertIn(section, sources)
        self.assertGreaterEqual(sources.count("Trägt nicht"), 8)
        self.assertNotRegex(sources, r"(?i)beck-online|juris\.de|münchkomm|nzi\s|zip\s")

    def test_mainbogen_case_reconciles_and_preserves_real_attachments(self):
        directory = ROOT / "testakten" / CASES[0]
        pairs = document_arcname_pairs(directory)
        self.assertGreaterEqual(len(pairs), 37)
        self.assertEqual(Counter(p.suffix.lower() for p, _ in pairs)[".eml"], 6)
        manifest = json.loads((ROOT / "quality" / NAME / "mainbogen-akte.json").read_text())
        for item in manifest["created"]:
            source = directory / item["path"]
            self.assertTrue(source.is_file(), item["path"])
            self.assertEqual(source.stat().st_size, item["size"], item["path"])
            self.assertEqual(sha(source), item["sha256"], item["path"])
        book = load_workbook(directory / "09_Schlussrechnung_und_Kontenabgleich.xlsx", data_only=False)
        try:
            sheet = book["Abstimmung"]
            formulae = {cell.coordinate: cell.value for row in sheet.iter_rows() for cell in row if cell.data_type == "f"}
            self.assertGreaterEqual(len(formulae), 6)
        finally:
            book.close()
        receipts = sum(map(Decimal, ("118450", "356200", "1109600", "286000", "94500", "120000", "58400", "21500", "20000")))
        expenses = sum(map(Decimal, ("602480.30", "354680", "141872.45", "184335.60", "126790.20", "96480.25", "21890", "37320", "4125.60", "73318")))
        self.assertEqual(receipts, Decimal("2184650.00"))
        self.assertEqual(expenses, Decimal("1643292.40"))
        self.assertEqual(receipts - expenses, Decimal("541357.60"))
        self.assertEqual(receipts - expenses - Decimal("115927.60"), Decimal("425430.00"))
        report = docx_text(directory / "08a_Schlussbericht_Referenzfassung.docx")
        for value in ("2.184.650,00 EUR", "1.643.292,40 EUR", "541.357,60 EUR", "425.430,00 EUR", "25,2335 Prozent"):
            self.assertIn(value, report)
        for open_gate in (
            "namentliche Freigabe zur Einreichung",
            "gerichtliche Zustimmung",
            "Auszahlungsvollzug",
        ):
            self.assertIn(open_gate, report)
        self.assertIn("nicht zur Einreichung", report)
        self.assertNotIn("Rechtskraftvermerk", report)
        distribution = load_workbook(directory / "12_Schlussverzeichnis.xlsx", data_only=False)
        try:
            sheet = distribution["Schlussverzeichnis"]
            quota = distribution["Quotenblatt"]
            self.assertIn("Quotenblatt", str(sheet["G13"].value))
            self.assertIn("SUM(G2:G12)", str(sheet["G13"].value))
            self.assertEqual(quota["B9"].value, "=ROUND(B2-B8,2)")
        finally:
            distribution.close()
        for email_path in sorted((directory / "eml").glob("*.eml")):
            message = BytesParser(policy=policy.default).parsebytes(email_path.read_bytes())
            self.assertFalse(message.defects)
            self.assertTrue(str(message["From"]).endswith(".example"))
            self.assertTrue(str(message["To"]).endswith(".example"))
            self.assertTrue(list(message.iter_attachments()), email_path.name)
            for attachment in message.iter_attachments():
                source = directory / attachment.get_filename()
                self.assertTrue(source.is_file())
                self.assertEqual(attachment.get_payload(decode=True), source.read_bytes())
        combined = directory / "gesamt-pdf" / f"{directory.name}_gesamt.pdf"
        reader = PdfReader(combined)
        self.assertGreaterEqual(len(reader.pages), 55)
        combined_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        self.assertNotIn("###", combined_text)
        self.assertNotIn("Rechtskraftvermerk", combined_text)
        self.assertIn("Bestandskraft", combined_text)

    def test_external_template_content_did_not_enter_repository_outputs(self):
        forbidden = ("Berke GmbH", "1542 IN 1600/11", "Bethmann Bank", "Jochen Berke", "M BE 4782")
        targets = list(PLUGIN.rglob("*.md"))
        targets += [p for p in (ROOT / "testakten" / CASES[0]).rglob("*") if p.suffix.lower() in {".md", ".csv", ".eml"}]
        targets += [p for p in (ROOT / "testakten" / CASES[0]).rglob("*.docx")]
        content = []
        for path in targets:
            content.append(docx_text(path) if path.suffix.lower() == ".docx" else path.read_text(encoding="utf-8", errors="ignore"))
        joined = "\n".join(content)
        for value in forbidden:
            self.assertNotIn(value, joined)

    def test_case_readmes_and_expanded_closure_chains(self):
        plugin_readme = (PLUGIN / "README.md").read_text()
        for case in CASES:
            directory = ROOT / "testakten" / case
            self.assertTrue((directory / "README.md").is_file())
            self.assertTrue((directory / "gesamt-pdf" / f"{case}_gesamt.pdf").is_file())
            self.assertIn(case, plugin_readme)
            self.assertGreaterEqual(len(document_arcname_pairs(directory)), 35)
        nordlicht = ROOT / "testakten" / CASES[1]
        for name in ("27_zwischenbericht_nr_14_31-12-2023.docx", "28_schlussrechnung_kontenabstimmung_15-03-2024.xlsx", "29_freigabevermerk_abschluss_18-03-2024.docx", "31_vollzugsprotokoll_schlussverteilung_24-04-2024.docx", "33_nachtragsverteilung_steuerzins_20-10-2024.docx"):
            self.assertTrue((nordlicht / name).is_file(), name)
        self.assertFalse((nordlicht / "Insolvenzakte_Nordlicht_Handels_GmbH.pdf").exists())
        nordlicht_readme = (nordlicht / "README.md").read_text()
        for marker in ("Führende Fassung", "23,627320 %", "nicht mehr Bestandteil"):
            self.assertIn(marker, nordlicht_readme)
        self.assertEqual(len(document_arcname_pairs(nordlicht)), 53)
        self.assertEqual(yaml.safe_load((nordlicht / "rubric.yaml").read_text())["plugin"], NAME)
        havelberg = ROOT / "testakten" / CASES[2]
        expected = ("26_zwischenbericht_31-10-2026.docx", "28_schlussverzeichnis_20-01-2027.docx", "29_freigabevermerk_abschluss_23-01-2027.docx", "31_vollzugsprotokoll_schlussverteilung_12-03-2027.docx", "34_abschlusskontrolle_schlussrechnung_20-01-2027.xlsx")
        for name in expected:
            self.assertTrue((havelberg / name).is_file(), name)
        employees = (havelberg / "06_personalliste_insolvenzgeld.csv").read_text()
        self.assertIn("31,Claudia Stern,Auszubildende Tischlerin", employees)
        self.assertIn("31,Claudia Stern,Auszubildende Tischlerin,Produktion,2024-09-01,800.00,800.00,800.00,nein,2026-05-31,ja,", employees)
        self.assertNotIn("BfA", employees)
        payment_review = (havelberg / "11_15b_zahlungsanalyse.csv").read_text()
        self.assertIn("2026-04-01,Furnier Nord GmbH,18000.00,Ratenplanrate 2", payment_review)
        self.assertIn("am 07.05.2026 schriftlich veranlasst", payment_review)
        self.assertIn("Kein de-minimis-Ausschluss allein wegen der Betragshöhe", payment_review)
        hearing_report = docx_text(havelberg / "bericht_berichtstermin_14092026.docx")
        self.assertIn("33,583266 %", hearing_report)
        self.assertNotIn("18,4 %", hearing_report)
        self.assertNotRegex(hearing_report, r"(?m)^(?:I|II|III|IV|V|VI)\.")
        self.assertEqual(yaml.safe_load((havelberg / "rubric.yaml").read_text())["plugin"], NAME)

    def test_klangbogen_long_term_reports_reconcile(self):
        directory = ROOT / "testakten" / CASES[3]
        report_directory = directory / "zwischenberichte"
        expected_pages = [9, 8, 9, 9, 8, 10, 11, 10, 9, 8, 8, 8, 51, 8, 9, 9, 9, 9, 9, 9, 8, 5]
        expected_dates = [
            date(2016, 5, 28), date(2016, 12, 2), date(2017, 6, 3),
            date(2017, 11, 27), date(2018, 5, 28), date(2018, 12, 7),
            date(2019, 5, 28), date(2019, 11, 25), date(2020, 5, 24),
            date(2020, 11, 20), date(2021, 5, 23), date(2021, 11, 29),
            date(2022, 5, 23), date(2023, 2, 5), date(2023, 11, 5),
            date(2024, 3, 30), date(2024, 5, 28), date(2024, 11, 25),
            date(2025, 5, 18), date(2025, 11, 8), date(2026, 6, 5),
            date(2026, 11, 28),
        ]
        reports = sorted(report_directory.glob("*.pdf"))
        self.assertEqual(len(reports), 22)
        actual_dates: list[date] = []
        actual_pages: list[int] = []
        report_texts: dict[int, str] = {}
        for index, report in enumerate(reports, start=1):
            match = re.fullmatch(r"(\d{2})_zwischenbericht_(\d{4}-\d{2}-\d{2})\.pdf", report.name)
            self.assertIsNotNone(match, report.name)
            assert match is not None
            self.assertEqual(int(match.group(1)), index)
            actual_dates.append(date.fromisoformat(match.group(2)))
            reader = PdfReader(report)
            actual_pages.append(len(reader.pages))
            report_texts[index] = "\n".join(page.extract_text() or "" for page in reader.pages)
        self.assertEqual(actual_dates, expected_dates)
        self.assertEqual(actual_pages, expected_pages)
        self.assertEqual(sum(actual_pages), 233)
        self.assertEqual(actual_pages[12], 51)
        self.assertEqual(actual_pages[21], 5)
        self.assertEqual((actual_dates[-1] - actual_dates[0]).days, 3836)
        opening_date = date(2015, 11, 22)
        self.assertEqual((actual_dates[0] - opening_date).days, 188)
        self.assertTrue((directory / "belege" / "01_eroeffnungsbeschluss_2015-11-22.pdf").is_file())

        # Das Inhaltsverzeichnis bildet in jedem Bericht die tatsaechlichen
        # Abschnitte 1 bis 10 und deren wirkliche Startseiten ab. Bericht 22
        # darf dabei keine Finanzanlage ausweisen, die er nicht enthaelt.
        case_builder = module("build-insolvenzverwaltung-klangbogen-zwischenberichte.py")
        for index, report in enumerate(reports):
            annex_pages = 42 if index == 12 else 0
            financial_pages = 0 if index == 21 else 3
            narrative_pages = expected_pages[index] - 3 - financial_pages - annex_pages
            expected_entries = case_builder.report_toc_entries(index, narrative_pages, annex_pages)
            reader = PdfReader(report)
            toc_lines = [line.strip() for line in (reader.pages[2].extract_text() or "").splitlines() if line.strip()]
            narrative_titles = case_builder.narrative_section_titles(index)
            self.assertEqual([title for title, _ in expected_entries[:10]], list(narrative_titles))
            for title, page_number in expected_entries:
                self.assertIn(title, toc_lines, f"Bericht {index + 1:02d}: {title}")
                position = toc_lines.index(title)
                self.assertLess(position + 1, len(toc_lines), f"Bericht {index + 1:02d}: {title}")
                self.assertEqual(toc_lines[position + 1], str(page_number), f"Bericht {index + 1:02d}: {title}")
            for title, page_number in expected_entries[:10]:
                target_text = " ".join((reader.pages[page_number - 1].extract_text() or "").split())
                self.assertIn(" ".join(title.split()), target_text, f"Bericht {index + 1:02d}: {title}")
            if index == 21:
                self.assertEqual(len(expected_entries), 10)
                self.assertNotIn("Anlage 1:", "\n".join(toc_lines))

        evidence = sorted((directory / "belege").glob("*.pdf"))
        expected_evidence_pages = {
            "01_eroeffnungsbeschluss_2015-11-22.pdf": 2,
            "02_berichtsanordnung_2015-12-15.pdf": 1,
            "03_bankbestaetigung_2026-11-30.pdf": 1,
            "04_steuerbescheid_2026-09-15.pdf": 2,
            "05_vergleich_landbuehne_2021-07-14.pdf": 3,
            "06_prozesskostenabrechnung_2024-09-18.pdf": 2,
            "07_tabellenauszug_2026-11-30.pdf": 3,
            "08_glaeubigerausschuss_stellungnahme_2026-12-02.pdf": 2,
            "09_abschlussreifevermerk_2026-12-05.pdf": 2,
            "10_kontenabstimmung_2026-12-05.pdf": 2,
            "11_aktenvermerk_steuerkonto_2026-10-29.pdf": 1,
            "12_wirtschaftlichkeitspruefung_landbuehne_2021-07-12.pdf": 2,
            "13_glaeubigerausschuss_zustimmung_landbuehne_2021-07-13.pdf": 2,
            "14_glaeubigerausschuss_zustimmung_d-und-o_2024-04-04.pdf": 2,
            "15_vergleich_d-und-o_2024-04-05.pdf": 3,
        }
        self.assertEqual({path.name for path in evidence}, set(expected_evidence_pages))
        self.assertEqual(len(evidence), 15)
        for document in evidence:
            self.assertEqual(len(PdfReader(document).pages), expected_evidence_pages[document.name], document.name)
        self.assertEqual(sum(expected_evidence_pages.values()), 30)

        mail_paths = sorted((directory / "korrespondenz").glob("*.eml"))
        self.assertEqual(len(mail_paths), 8)
        message_ids: set[str] = set()
        observed_offsets: set[int] = set()
        berlin = ZoneInfo("Europe/Berlin")
        for mail_path in mail_paths:
            message = BytesParser(policy=policy.default).parsebytes(mail_path.read_bytes())
            self.assertFalse(message.defects, mail_path.name)
            message_id = str(message["Message-ID"] or "")
            self.assertRegex(message_id, r"^<[^<>@\s]+@[^<>@\s]+>$", mail_path.name)
            self.assertNotIn(message_id, message_ids, mail_path.name)
            message_ids.add(message_id)
            sent = parsedate_to_datetime(str(message["Date"] or ""))
            self.assertIsNotNone(sent.tzinfo, mail_path.name)
            expected_offset = sent.replace(tzinfo=None).replace(tzinfo=berlin).utcoffset()
            self.assertEqual(sent.utcoffset(), expected_offset, mail_path.name)
            offset_seconds = int(sent.utcoffset().total_seconds())
            observed_offsets.add(offset_seconds)
            expected_token = "+0200" if offset_seconds == 7200 else "+0100"
            self.assertTrue(str(message["Date"]).endswith(expected_token), mail_path.name)
            attachments = list(message.iter_attachments())
            self.assertTrue(attachments, mail_path.name)
            for attachment in attachments:
                filename = attachment.get_filename()
                self.assertIsNotNone(filename, mail_path.name)
                matches = [path for path in directory.rglob(str(filename)) if path.is_file()]
                self.assertEqual(len(matches), 1, f"{mail_path.name}: {filename}")
                self.assertEqual(attachment.get_payload(decode=True), matches[0].read_bytes())
        self.assertEqual(observed_offsets, {3600, 7200})

        workbook_path = directory / "rechenwerk" / "95_verfahrensrechnung_und_schlussreife.xlsx"
        with zipfile.ZipFile(workbook_path) as archive:
            workbook_xml = archive.read("xl/workbook.xml").decode("utf-8")
            self.assertEqual(workbook_xml.count("_xlnm.Print_Area"), 6)
            self.assertEqual(workbook_xml.count("_xlnm.Print_Titles"), 5)
            for index in range(1, 7):
                sheet_xml = archive.read(f"xl/worksheets/sheet{index}.xml").decode("utf-8")
                self.assertIn('fitToPage="1"', sheet_xml)
                self.assertIn('orientation="landscape"', sheet_xml)
                self.assertIn('fitToWidth="1"', sheet_xml)
        formula_book = load_workbook(workbook_path, data_only=False)
        try:
            self.assertEqual(formula_book["Berichtsperioden"]["G26"].value, "=D26+E26-F26")
            self.assertEqual(formula_book["Forderungen"]["E30"].value, "=SUM(E5:E29)")
            self.assertEqual(formula_book["Schlussreife"]["B11"].value, "=SUM(B5:B10)")
            self.assertEqual(formula_book["Schlussreife"]["B12"].value, "=Berichtsperioden!G26-B11")
            self.assertEqual(formula_book["Schlussreife"]["B13"].value, "=B12/Forderungen!E30")
        finally:
            formula_book.close()
        value_book = load_workbook(workbook_path, data_only=True)
        try:
            overview = value_book["Übersicht"]
            self.assertAlmostEqual(overview["B8"].value, 538776.34, places=2)
            self.assertAlmostEqual(overview["B9"].value, 1764825.62, places=2)
            self.assertAlmostEqual(overview["B10"].value, 119776.27, places=2)
            self.assertAlmostEqual(overview["B11"].value, 419000.07, places=2)
            self.assertAlmostEqual(overview["B12"].value * 100, 23.741726, places=6)
            self.assertAlmostEqual(value_book["Forderungen"]["D30"].value, 2421820.00, places=2)
            self.assertAlmostEqual(value_book["Forderungen"]["E30"].value, 1764825.62, places=2)
            periods = value_book["Berichtsperioden"]
            self.assertEqual(periods["B5"].value.date(), expected_dates[0])
            self.assertEqual(periods["B26"].value.date(), expected_dates[-1])
            self.assertEqual(periods["C5"].value, 188)
            period_receipts = {
                report_number: Decimal(str(periods.cell(row=report_number + 4, column=5).value))
                for report_number in range(1, 23)
            }
            journal_dates: dict[int, list[date]] = {report_number: [] for report_number in range(1, 23)}
            journal_receipts: dict[int, list[tuple[date, str, Decimal]]] = {
                report_number: [] for report_number in range(1, 23)
            }
            for row in value_book["Kontenjournal"].iter_rows(min_row=5, values_only=True):
                if row[0] is None:
                    continue
                report_number = int(row[2])
                booking_date = row[1]
                self.assertTrue(hasattr(booking_date, "date"), f"Journal Bericht {report_number}: {booking_date!r}")
                journal_dates[report_number].append(booking_date.date())
                if row[3] == "E":
                    journal_receipts[report_number].append(
                        (booking_date.date(), str(row[4]), Decimal(str(row[5])))
                    )
        finally:
            value_book.close()

        # Jeder Bericht mit Kontonachweis muss dieselben vier Buchungstage wie das
        # bearbeitbare Journal ausweisen. Bericht 22 ist bewusst der kurze
        # Schlussreifebericht ohne Finanzanlagen; sein Journal bleibt im Rechenwerk.
        for report_number in range(1, 22):
            bank_pages = [
                page.extract_text() or ""
                for page in PdfReader(reports[report_number - 1]).pages
                if "Kontonachweis zum Berichtsstichtag" in (page.extract_text() or "")
            ]
            self.assertEqual(len(bank_pages), 1, f"Bericht {report_number:02d}")
            printed_dates = [
                date(int(year), int(month), int(day))
                for day, month, year in re.findall(r"\b(\d{2})\.(\d{2})\.(\d{4})\b", bank_pages[0])
            ]
            self.assertEqual(len(printed_dates), 6, f"Bericht {report_number:02d}: {printed_dates}")
            self.assertEqual(len(journal_dates[report_number]), 4, f"Journal Bericht {report_number:02d}")
            self.assertEqual(printed_dates[1:5], journal_dates[report_number], f"Bericht {report_number:02d}")
        self.assertNotIn("Kontonachweis zum Berichtsstichtag", report_texts[22])
        self.assertEqual(len(journal_dates[22]), 4)

        expected_named_receipts = {
            7: [(date(2019, 3, 15), "Kaufpreisvergleich", Decimal("30000.00")), (date(2019, 4, 18), "Theater-Schlussrechnungen", Decimal("1057.39"))],
            9: [(date(2020, 1, 16), "Sachversicherungsleistung", Decimal("28420.00")), (date(2020, 4, 20), "Projektvergleich mit Zinsen", Decimal("20644.69"))],
            11: [(date(2021, 1, 15), "Restdebitoren Theaterprojekte", Decimal("24222.00")), (date(2021, 4, 22), "Weitere Forderungseinzüge", Decimal("11398.59"))],
            12: [(date(2021, 7, 19), "Landbühne-Vergleich", Decimal("35620.59")), (date(2021, 10, 29), "Weitere Forderungseinzüge", Decimal("11097.72"))],
            15: [(date(2023, 4, 12), "Steuererstattung Änderungsbescheid", Decimal("30454.71")), (date(2023, 9, 21), "Erstattung Parallelverfahren", Decimal("16524.00"))],
            19: [(date(2025, 1, 16), "Steuerliche Abschlussgutschrift", Decimal("20709.20")), (date(2025, 4, 17), "Zinsgutschrift", Decimal("9745.51"))],
            22: [(date(2026, 6, 22), "Steuererstattung", Decimal("11698.47")), (date(2026, 10, 28), "Zinsgutschrift", Decimal("5505.16"))],
        }
        for report_number, expected_receipts in expected_named_receipts.items():
            self.assertEqual(journal_receipts[report_number], expected_receipts, f"Journal Bericht {report_number:02d}")

        # Die im September 2024 noch offene Kostenfestsetzung wird in einem
        # spaeteren Berichtsstand ausdrücklich geschlossen, ohne eine nicht
        # erfolgte Zahlung in das Kontenjournal einzustellen.
        for marker in ("1.284,30 EUR", "14.01.2025", "17.01.2025", "18.02.2025", "ohne Zahlung und ohne Kontenbuchung"):
            self.assertIn(marker, report_texts[19])

        # Ein als eingegangen bezeichneter Einzelbetrag darf die gesamten
        # Periodeneinnahmen nicht uebersteigen.
        report_07 = " ".join(report_texts[7].split())
        receipt_mentions: list[Decimal] = []
        for entry in re.finditer(r"\beingegangen\b", report_07, flags=re.IGNORECASE):
            prefix = report_07[max(0, entry.start() - 350):entry.start()]
            amounts = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})\s+EUR", prefix)
            if amounts:
                receipt_mentions.append(Decimal(amounts[-1].replace(".", "").replace(",", ".")))
        self.assertTrue(receipt_mentions, "Bericht 07 bezeichnet keinen bezifferten Eingang")
        self.assertTrue(all(amount <= period_receipts[7] for amount in receipt_mentions), receipt_mentions)
        self.assertNotIn("62.500,00 EUR", report_07)

        # Der D&O-Vergleich ist exakt in den beiden Perioden 17 und 18 gebucht.
        first_rate = Decimal("13141.47")
        second_rate = Decimal("33621.71")
        total_settlement = Decimal("46763.18")
        self.assertEqual(period_receipts[17], first_rate)
        self.assertEqual(period_receipts[18], second_rate)
        self.assertEqual(first_rate + second_rate, total_settlement)
        self.assertIn("46.763,18 EUR", report_texts[16])
        self.assertIn("13.141,47 EUR", report_texts[17])
        self.assertIn("33.621,71 EUR", report_texts[18])
        self.assertNotIn("118.000 EUR", report_texts[16] + report_texts[17] + report_texts[18])
        self.assertNotIn("65.000 EUR", report_texts[16] + report_texts[17] + report_texts[18])

        # Der zeitliche Verlauf des Landbuehne-Vergleichs bleibt stichtagsrein.
        report_11 = " ".join(report_texts[11].split())
        report_12 = " ".join(report_texts[12].split())
        self.assertRegex(report_11, r"(?i)Landbuehne.{0,300}(?:noch\s+offen|ausstehend|noch\s+nicht\s+eingegangen)")
        self.assertNotRegex(report_11, r"(?i)Landbuehne.{0,220}(?:Rate|Zahlung).{0,100}\beingegangen\b")
        self.assertRegex(report_12, r"(?i)Landbuehne.{0,300}(?:Zahlungseingang|\beingegangen\b)")

        # Bericht 20 bildet den vorlaeufigen, Bericht 21 erst den finalen
        # Tabellenstand ab.
        report_20 = " ".join(report_texts[20].split())
        report_21 = " ".join(report_texts[21].split())
        self.assertIn("1.759.910,00 EUR", report_20)
        self.assertRegex(report_20, r"(?i)vorlaeufig")
        self.assertNotIn("1.764.825,62 EUR", report_20)
        self.assertIn("1.764.825,62 EUR", report_21)
        self.assertRegex(report_21, r"(?i)(?:final|endgueltig)")

        # Die offenen Vollzugsgates sperren Aussenhandlungen, beseitigen aber
        # nicht die im letzten Bericht belegte faktische Schlussreife.
        report_22 = " ".join(report_texts[22].split())
        for blocked_step in ("Einreichung", "Verteilung", "Auszahlung", "Aufhebung"):
            self.assertIn(blocked_step, report_22)
        self.assertIn("faktische Schlussreife", report_22)
        self.assertRegex(report_22, r"(?i)faktische\s+Schlussreife.{0,160}(?:unberuehrt|nicht\s+(?:gehindert|beseitigt))")
        self.assertNotIn("oder die Schlussreife", report_22)
        self.assertIn("enthaelt weder eine Periodenrechnung noch einen Kontonachweis als Anlage", report_22)
        self.assertIn("separat gefuehrten Rechenwerk", report_22)
        self.assertIn("Finanzanlagen der Zwischenberichte 01 bis 21", report_22)
        self.assertNotRegex(report_22, r"(?i)(?:Periodenrechnung|Kontonachweis).{0,80}in den Anlagen")

        # Das Sonderkonvolut besteht aus 42 Nachweisseiten. Die zwoelf
        # Forderungsblaetter muessen die Teilpruefung nachvollziehbar machen.
        report_13 = report_texts[13]
        self.assertIn("42 Nachweisseiten", report_13)
        self.assertNotIn("42 Nachmeldungen", report_13)
        claim_pages = [
            page.extract_text() or ""
            for page in PdfReader(reports[12]).pages
            if "Forderungsnachweis " in (page.extract_text() or "")
        ]
        self.assertEqual(len(claim_pages), 12)
        for page_text in claim_pages:
            self.assertIn("Beleg-ID", page_text)
            self.assertRegex(page_text, r"(?i)angemeldet(?:er\s+Betrag)?")
            self.assertRegex(page_text, r"(?i)festgestellt(?:er\s+Teilbetrag)?")
            self.assertRegex(page_text, r"(?i)(?:bestritten|reduziert)(?:er\s+Teilbetrag)?")
            self.assertGreaterEqual(len(re.findall(r"\d{1,3}(?:\.\d{3})*,\d{2}\s+EUR", page_text)), 3)

        report_13_reader = PdfReader(reports[12])

        # Seiten 22 bis 29: acht konkrete Korrespondenznachweise mit allen
        # Mindestmetadaten und einer eindeutigen Tabellenposition.
        correspondence_pages = [page.extract_text() or "" for page in report_13_reader.pages[21:29]]
        self.assertEqual(len(correspondence_pages), 8)
        for offset, page_text in enumerate(correspondence_pages, start=1):
            for marker in ("Absender:", "Empfaenger:", "Datum:", "Tabellenposition", "Anlagen", "naechster Schritt"):
                self.assertIn(marker, page_text, f"Korrespondenznachweis {offset:02d}: {marker}")
            self.assertIn(f"F-{offset:03d}", page_text)
            self.assertRegex(page_text, r"\b\d{2}\.\d{2}\.202[12]\b")

        # Seiten 30 bis 37 verwenden nur die sechs tatsaechlich vorhandenen
        # Spalten des Tabellenblatts Forderungen und weisen Einzelwerte aus.
        control_pages = [page.extract_text() or "" for page in report_13_reader.pages[29:37]]
        self.assertEqual(len(control_pages), 8)
        for offset, page_text in enumerate(control_pages, start=1):
            self.assertIn(f"F-{offset:03d}", page_text)
            self.assertIn("ID, Glaeubiger, Grund, Angemeldet, Festgestellt und Status", page_text)
            normalized_page_text = re.sub(r"\s+", " ", page_text)
            self.assertIn("weder um eine Gruppensumme noch um eine Zwischensumme", normalized_page_text)
            self.assertNotIn("Rang, Sicherungsbezug, Beleg-ID und Widerspruchsgrund", page_text)

        # Seiten 38 bis 43: jeder Prozessnachweis nennt den Stichtag, einen
        # Streitwert, den Kostenstand und den naechsten konkreten Schritt.
        process_pages = [page.extract_text() or "" for page in report_13_reader.pages[37:43]]
        self.assertEqual(len(process_pages), 6)
        for offset, page_text in enumerate(process_pages, start=1):
            for marker in ("Vorgang und Datum", "Stand:", "Streitwert", "Kostenstand", "Naechster Schritt"):
                self.assertIn(marker, page_text, f"Prozessregister {offset:02d}: {marker}")
            self.assertGreaterEqual(len(re.findall(r"\d{1,3}(?:\.\d{3})*,\d{2}\s+EUR", page_text)), 2)

        # Seiten 44 bis 47: Steuerart, Bearbeitungsdatum, Buchungskreis,
        # Steuerkonto und verantwortliche Beratung sind ausformuliert.
        tax_pages = [page.extract_text() or "" for page in report_13_reader.pages[43:47]]
        self.assertEqual(len(tax_pages), 4)
        for offset, page_text in enumerate(tax_pages, start=1):
            for marker in ("Steuerart und Datum", "Bearbeitungsstand:", "Buchungskreis:", "Steuerkonto:", "Verantwortliche Beraterin oder verantwortlicher Berater:", "naechster Schritt"):
                self.assertIn(marker, page_text, f"Steuerkontenblatt {offset:02d}: {marker}")
            self.assertIn("keine eigenen Spalten Buchungskreis oder Steuerkonto", page_text)

        # Seiten 48 bis 51 bilden exakt die vier Journalzeilen des Berichts 13
        # ab. Wertstellung und Gegenkonto bleiben zutreffend Einzelbelegfelder.
        bank_pages = [page.extract_text() or "" for page in report_13_reader.pages[47:51]]
        self.assertEqual(len(bank_pages), 4)
        expected_bank_rows = (
            ("B-0049", "17.12.2021", "Verwertungserloes", "22.191,58 EUR", "451.748,00 EUR"),
            ("B-0050", "08.01.2022", "Rechts- und Gutachterkosten", "9.125,60 EUR", "442.622,40 EUR"),
            ("B-0051", "22.04.2022", "Forderungseinzug", "10.443,09 EUR", "453.065,49 EUR"),
            ("B-0052", "14.05.2022", "Massebuero und Bank", "5.834,40 EUR", "447.231,09 EUR"),
        )
        for page_text, expected in zip(bank_pages, expected_bank_rows):
            normalized_page_text = re.sub(r"\s+", " ", page_text)
            for marker in ("Beleg-ID:", "Buchungstag:", "Wertstellung:", "Gegenkonto:", "Laufender Saldo nach Buchung:"):
                self.assertIn(marker, normalized_page_text)
            for value in expected:
                self.assertIn(value, normalized_page_text)
            self.assertIn("Wertstellung und Gegenkonto stehen nur auf diesem Einzelbeleg", normalized_page_text)
            self.assertIn("nicht als Spalten des Rechenwerks behauptet", normalized_page_text)

        # Externe Belege tragen den Kopf ihrer tatsaechlichen Ausstellerin.
        issuer_checks = {
            "01_eroeffnungsbeschluss_2015-11-22.pdf": ("Amtsgericht Bamberg", "Insolvenzgericht"),
            "02_berichtsanordnung_2015-12-15.pdf": ("Amtsgericht Bamberg", "Insolvenzgericht"),
            "03_bankbestaetigung_2026-11-30.pdf": ("Frankenbogen Bank eG",),
            "04_steuerbescheid_2026-09-15.pdf": ("Finanzamt Bamberg",),
            "05_vergleich_landbuehne_2021-07-14.pdf": ("Vergleichsparteien Klangbogen", "Landbuehne Nord"),
            "08_glaeubigerausschuss_stellungnahme_2026-12-02.pdf": ("Glaeubigerausschuss", "Klangbogen"),
            "13_glaeubigerausschuss_zustimmung_landbuehne_2021-07-13.pdf": ("Glaeubigerausschuss", "Klangbogen"),
            "14_glaeubigerausschuss_zustimmung_d-und-o_2024-04-04.pdf": ("Glaeubigerausschuss", "Klangbogen"),
            "15_vergleich_d-und-o_2024-04-05.pdf": ("Vergleichsparteien Klangbogen", "Bamberger", "Frankenwacht"),
        }
        for filename, issuer_parts in issuer_checks.items():
            first_page = PdfReader(directory / "belege" / filename).pages[0].extract_text() or ""
            first_line = next((line.strip() for line in first_page.splitlines() if line.strip()), "")
            for issuer_part in issuer_parts:
                self.assertIn(issuer_part, first_line, filename)

        def evidence_text(filename: str) -> str:
            return " ".join(
                "\n".join(
                    page.extract_text() or ""
                    for page in PdfReader(directory / "belege" / filename).pages
                ).split()
            )

        # Der Bescheid vom 15.09.2026 bleibt auf seinem damaligen Stand. Erst
        # der spaetere interne Vermerk dokumentiert Postkontrolle und Zinszufluss.
        tax_notice = evidence_text("04_steuerbescheid_2026-09-15.pdf")
        for marker in (
            "22.06.2026",
            "11.698,47 EUR",
            "Rechtsbehelfspruefung laeuft",
            "weder ein Ablauf der Rechtsbehelfsfrist noch Bestandskraft",
        ):
            self.assertIn(marker, tax_notice)
        self.assertNotIn("28.10.2026", tax_notice)
        self.assertNotIn("Rechtsbehelfsfrist ist abgelaufen", tax_notice)
        self.assertNotIn("Bestandskraft ist eingetreten", tax_notice)

        tax_memo = evidence_text("11_aktenvermerk_steuerkonto_2026-10-29.pdf")
        for marker in (
            "22.06.2026",
            "28.10.2026",
            "11.698,47 EUR",
            "5.505,16 EUR",
            "keinen aktenkundigen Rechtsbehelf",
            "amtliche Bestandskraftbescheinigung wird nicht behauptet",
            "Philipp Joens",
        ):
            self.assertIn(marker, tax_memo)

        # Vergleichsschluss, Faelligkeit und Zahlungseingang im
        # Landbuehne-Komplex duerfen nicht in einem Ereignis zusammenfallen.
        landbuehne = evidence_text("05_vergleich_landbuehne_2021-07-14.pdf")
        for marker in (
            "14.07.2021",
            "19.07.2021",
            "35.620,59 EUR",
            "nicht den tatsaechlichen Zahlungseingang",
            "Ob und wann der Betrag eingeht",
            "Dr. Mechthild Karg",
            "Jost Thalhammer",
        ):
            self.assertIn(marker, landbuehne)
        self.assertNotIn("Der Eingang am 19.07.2021 wird", landbuehne)
        landbuehne_economy = evidence_text("12_wirtschaftlichkeitspruefung_landbuehne_2021-07-12.pdf")
        for marker in ("49.870,59 EUR", "18.400,00 EUR", "22.815,88 EUR", "34.370,59 EUR", "Dr. Mechthild Karg"):
            self.assertIn(marker, landbuehne_economy)
        landbuehne_approval = evidence_text("13_glaeubigerausschuss_zustimmung_landbuehne_2021-07-13.pdf")
        for marker in ("35.620,59 EUR", "einstimmig", "vollstaendigem Zahlungseingang", "Kunigunde Woelfel"):
            self.assertIn(marker, landbuehne_approval)

        # Alle internen Kernbelege tragen eine namentliche Zeichnung. Die
        # Prozesskostenabrechnung bleibt strikt auf dem Stand 18.09.2024.
        internal_signatures = {
            "05_vergleich_landbuehne_2021-07-14.pdf": ("Dr. Mechthild Karg", "Jost Thalhammer"),
            "06_prozesskostenabrechnung_2024-09-18.pdf": ("Philipp Joens",),
            "07_tabellenauszug_2026-11-30.pdf": ("Philipp Joens",),
            "09_abschlussreifevermerk_2026-12-05.pdf": ("Dr. Mechthild Karg",),
            "10_kontenabstimmung_2026-12-05.pdf": ("Philipp Joens", "Dr. Mechthild Karg"),
        }
        for filename, signatories in internal_signatures.items():
            text_value = evidence_text(filename)
            self.assertIn("Gezeichnet", text_value, filename)
            for signatory in signatories:
                self.assertIn(signatory, text_value, filename)
        costs = evidence_text("06_prozesskostenabrechnung_2024-09-18.pdf")
        for marker in ("Status am 18.09.2024", "1.284,30 EUR", "noch nicht beschieden"):
            self.assertIn(marker, costs)
        self.assertNotIn("Folgezeitraum", costs)
        closing_readiness = evidence_text("09_abschlussreifevermerk_2026-12-05.pdf")
        for marker in ("1.284,30 EUR", "14.01.2025", "17.01.2025", "18.02.2025", "Mangels Zahlung entstand keine Kontenbuchung", "Vorgang ist abgeschlossen"):
            self.assertIn(marker, closing_readiness)

        # D&O-Vergleich und Ausschussfreigabe muessen dieselbe Gesamtsumme
        # und dieselben beiden Raten ausweisen.
        d_and_o_approval = evidence_text("14_glaeubigerausschuss_zustimmung_d-und-o_2024-04-04.pdf")
        d_and_o_settlement = evidence_text("15_vergleich_d-und-o_2024-04-05.pdf")
        for text_value in (d_and_o_approval, d_and_o_settlement):
            for marker in ("46.763,18 EUR", "13.141,47 EUR", "33.621,71 EUR"):
                self.assertIn(marker, text_value)
        for marker in ("Dr. Mechthild Karg", "Hinnerk Bamberger", "Dr. Ylva Thalhammer"):
            self.assertIn(marker, d_and_o_settlement)

        combined = directory / "gesamt-pdf" / f"{directory.name}_gesamt.pdf"
        reader = PdfReader(combined)
        self.assertEqual(len(reader.pages), 263)
        combined_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        for marker in (
            "Zwischenbericht 01",
            "42 Nachweisseiten",
            "Schlussreife und Uebergabe an den Schlussbericht",
            "538.776,34 EUR",
        ):
            self.assertIn(marker, combined_text)

    def test_release_packages_are_complete_and_byte_exact(self):
        if DIST is None:
            self.skipTest("--dist erforderlich")
        builder = module("build-insolvenzverwaltung-berichtsersteller-release.py")
        self.assertEqual({p.name for p in DIST.iterdir()}, builder.asset_names())
        for plugin_zip, prefix in ((f"{NAME}.zip", ""), (f"{NAME}-portable.zip", NAME + "/")):
            with zipfile.ZipFile(DIST / plugin_zip) as archive:
                self.assertIsNone(archive.testzip())
                self.assertTrue(all(".." not in Path(name).parts for name in archive.namelist()))
                for source in builder.plugin_sources():
                    relative = source.relative_to(PLUGIN).as_posix()
                    self.assertEqual(archive.read(prefix + relative), source.read_bytes())
        for case in CASES:
            directory = ROOT / "testakten" / case
            combined = directory / "gesamt-pdf" / f"{case}_gesamt.pdf"
            self.assertEqual((DIST / combined.name).read_bytes(), combined.read_bytes())
            with zipfile.ZipFile(DIST / f"testakte-{case}.zip") as archive:
                self.assertIsNone(archive.testzip())
                self.assertTrue(archive.read("README.txt").startswith(NOTICE_BYTES))
                expected = working_dump_archive_pairs(directory, include_gesamt_pdf=True)
                for source, arcname in expected:
                    self.assertEqual(archive.read(arcname), source.read_bytes())
            with zipfile.ZipFile(DIST / f"testakte-{case}-einzelpdfs.zip") as archive:
                self.assertIsNone(archive.testzip())
                self.assertTrue(archive.read("README.txt").startswith(NOTICE_BYTES))
                self.assertEqual(len(archive.namelist()), len(document_arcname_pairs(directory)) + 1)
        lines = (DIST / "checksums-sha256.txt").read_text().splitlines()
        self.assertEqual(len(lines), len(builder.asset_names()) - 1)
        for line in lines:
            digest, name = line.split("  ", 1)
            self.assertEqual(sha(DIST / name), digest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path)
    args, remaining = parser.parse_known_args()
    DIST = args.dist.resolve() if args.dist else None
    unittest.main(argv=[__file__, *remaining])
