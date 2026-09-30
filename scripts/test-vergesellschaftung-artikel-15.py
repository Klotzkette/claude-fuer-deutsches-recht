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
        self.assertGreaterEqual(len(PROFILE["cases"]), 5)
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


class BerlinerArgumentationskartenTests(unittest.TestCase):
    """Redaktionelle Textverträge, keine juristische Bewertung von Modellantworten."""

    REFERENCE = "references/berliner-kommissionsbericht.md"
    MINI = f"{SLUG}-schnellstart.md"
    WORKSHOP = f"{SLUG}-werkstatt.md"

    def section(self, relative_path, number):
        source = (PLUGIN / relative_path).read_text(encoding="utf-8")
        # Nur den bezeichneten Abschnitt prüfen, nicht benachbarte Wortvorkommen.
        match = re.search(
            rf"(?ms)^#{{1,6}} {re.escape(number)}\. [^\n]+\n(.*?)(?=^#{{1,6}} |\Z)", source
        )
        self.assertIsNotNone(match, (relative_path, number))
        return compact(match[1])

    def assert_passages(self, relative_path, number, *passages):
        text = self.section(relative_path, number)
        for passage in passages:
            with self.subTest(file=relative_path, section=number, passage=passage):
                self.assertIn(compact(passage), text)

    def test_package_local_reference_is_linked_from_sources_and_skills(self):
        reference = PLUGIN / self.REFERENCE
        self.assertTrue(reference.is_file())
        self.assertEqual(reference.resolve().parent, (PLUGIN / "references").resolve())
        skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertTrue(skills)
        for path in [PLUGIN / "references/vergesellschaftung-quellen.md", *skills]:
            with self.subTest(file=path.relative_to(PLUGIN)):
                links = re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8"))
                links = [link for link in links if "berliner-kommissionsbericht.md" in link]
                self.assertTrue(links, path)
                for link in links:
                    self.assertNotIn("://", link)
                    self.assertEqual((path.parent / link.split("#")[0]).resolve(), reference.resolve())

    def test_report_positions_are_not_presented_as_case_law(self):
        self.assert_passages(self.REFERENCE, "1.1",
                             "Mehrheitsbegründung, Sondervoten und eine ergänzende Stellungnahme",
                             "gedruckten Seiten, nicht die um zwei höheren PDF-Seiten",
                             "Der Bericht ist weder Gesetz noch Gerichtsentscheidung.")
        self.assert_passages(self.REFERENCE, "1.3",
                             "Die tragende Mehrheitslinie wendet einen modifizierten Maßstab an",
                             "Das Sondervotum zur Verhältnismäßigkeit verlangt eine strengere grundrechtliche Gegenprüfung",
                             "Es lehnt Vergesellschaftung nicht schlechthin ab.",
                             "Verwende keine Mehrheitsabstimmung der Kommission als Rechtsbeweis.")
        self.assert_passages(self.WORKSHOP, "7.1",
                             "als Argumentationsmaterial, nicht als gerichtliche Freigabe",
                             "ohne Vergesellschaftung grundsätzlich auszuschließen")
        self.assert_passages(self.MINI, "1.4", "Der Abschlussbericht Juni 2023 ist kein Urteil.",
                             "verbietet Vergesellschaftung aber nicht generell",
                             "Prüfe den Fall unter beiden Maßstäben")
        self.assert_passages("skills/vergesellschaftungsvorhaben-einordnen/SKILL.md", "3.5",
                             "Eine Kommissionsmehrheit entscheidet den Verfassungsstreit nicht.")

    def test_article14_and_housing_hessen_transfer_limits_remain_explicit(self):
        self.assert_passages(self.MINI, "1.2",
                             "Nutzungsordnung nach Artikel 14 Absatz 1 Satz 2 GG",
                             "Güterbeschaffung nach Absatz 3",
                             "gesetzliche Überführung in Gemeinwirtschaft nach Artikel 15")
        self.assert_passages(self.WORKSHOP, "4",
                             "Es ist kein Urteil über ein Vergesellschaftungsgesetz.",
                             "Für konkrete Einzelenteignung nicht den Artikel-15-Workflow als verkürzten Ersatz benutzen.")
        self.assert_passages(self.REFERENCE, "1.4",
                             "3000 Wohnungen ist eine Berliner Gestaltungsfrage, kein allgemeiner Artikel-15-Tatbestand")
        self.assert_passages(self.REFERENCE, "1.6",
                             "Hessische Artikel 39–41 und 45 müssen eigenständig ausgelegt werden.")
        self.assert_passages(self.MINI, "1.4", "Berliner Mietprognosen beweisen keine Netzentgeltwirkung.")
        self.assert_passages("skills/energienetz-und-unionsrecht-abgleichen/SKILL.md", "3.6",
                             "Behauptete Mietsenkungen beweisen keine günstigeren Netzentgelte.")

    def test_compensation_models_keep_counterarguments_in_each_surface(self):
        surfaces = (
            (self.REFERENCE, "1.5", "Das Sondervotum wendet sich insbesondere gegen den Zirkelschluss",
             "Eine finanzielle Obergrenze ist eine streitige rechtliche These"),
            (self.WORKSHOP, "9.1", "Das Sondervotum beanstandet insbesondere die Ableitung der Entschädigung",
             "Keine Prozentquote mitteln und keine feste Untergrenze erfinden."),
            (self.MINI, "1.5", "Mietziele oder Budgets rechtfertigen nicht selbst die Entschädigung.",
             "Hypothetische Schranken müssen zulässig und entschädigungsfrei sein."),
            ("skills/entschaedigung-und-finanzierung-pruefen/SKILL.md", "3.5",
             "Das Sondervotum beanstandet insbesondere die Ableitung der Entschädigung",
             "keine gemittelte Kompromissquote"),
        )
        for path, number, objection, constraint in surfaces:
            with self.subTest(file=path):
                text = self.section(path, number)
                for model in (r"gemeinwirtschaftlich\w* (?:Ertr\w*|Bewirtschaftung)",
                              r"fiskalisch\w*", r"hypothetisch\w*", r"Verkehrswert\w*"):
                    self.assertRegex(text, model)
                self.assert_passages(path, number, objection, constraint)
                self.assertIn("entschädigungsfrei", text)
                self.assertIn("Bestandsschutz", text)
                self.assertIn("nicht umgesetzte", text)
        self.assert_passages(self.REFERENCE, "1.5",
                             "In Rn. 244 argumentiert die Mehrheit hilfsweise",
                             "Das belegt kein eigenständiges Mehrheitslager mit Verkehrswertbindung.",
                             "Die Mehrheit lehnt zusätzliche Beteiligtenstellung allein wegen Anteilwertverlusts ab",
                             "das Sondervotum verlangt Berücksichtigung weitergehender Schäden der Mutterunternehmen")
        self.assert_passages(self.MINI, "1.5", "statt automatischem Vollmarktwert oder Pauschalabschlag")

    def test_framework_act_2026_is_not_yet_in_force_or_a_transfer(self):
        # Fester Quellenstand; weder Tagesdatum noch Netzabfrage steuern den Test.
        surfaces = (
            (self.REFERENCE, "1.1", "ist also am Prüfdatum noch nicht in Kraft",
             "Es vollzieht selbst keine Übertragung"),
            (self.WORKSHOP, "7.3", "Es ist daher noch nicht in Kraft.",
             "Für eine konkrete Übertragung verlangt es ein Anwendungsgesetz."),
            (self.MINI, "1.4", "Noch nicht geltend; kein selbständiger Eigentumsübergang und kein Artikel-14-Gesetz.",
             "Keine Position ungeprüft auf Hessen übertragen."),
            ("skills/landeskompetenz-und-hessenrecht-pruefen/SKILL.md", "3.5",
             "Am 30.09.2026 daher nicht als geltende hessische oder Berliner Übertragungsgrundlage verwenden.",
             "Fassung und Zeitbezug im Vermerk ausdrücklich festhalten."),
        )
        for path, number, status, limit in surfaces:
            with self.subTest(file=path):
                self.assert_passages(path, number, "18.03.2026", "27.03.2026", "30.09.2026", status, limit)
                self.assertRegex(self.section(path, number), r"Paragraf(?:en)? 8[^.]{0,100}erst 24 Monate")

    def test_weg_correction_is_carried_into_skill_workshop_and_mini(self):
        surfaces = (
            (self.REFERENCE, "1.2", "Die verkürzte Einordnung als bloß beschränktes dingliches Recht in Rn. 85 des Berichts nicht übernehmen."),
            (self.WORKSHOP, "7.2", "die abweichende verkürzte Beschreibung des Berichts nicht übernehmen"),
            (self.MINI, "1.2", "nicht bloß ein beschränktes dingliches Recht"),
            ("skills/gegenstaende-und-anteile-abgrenzen/SKILL.md", "3.5", "nicht als bloß beschränktes dingliches Recht"),
        )
        for path, number, correction in surfaces:
            with self.subTest(file=path):
                self.assert_passages(path, number, "Paragraf 1 Absatz 2 WEG", correction)
                self.assertRegex(self.section(path, number), r"Sondereigentum (?:verbunden )?mit Miteigentumsanteil")


if __name__ == "__main__":
    unittest.main(verbosity=2)
