#!/usr/bin/env python3
"""Gezielte Regressionen für Plugin und native Göttinger Quellenakte."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import re
import tempfile
import unittest
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from pathlib import Path
from zipfile import ZipFile

import yaml
from docx import Document
from pypdf import PdfReader

from quality_lab import validate_profile
from testakte_disclaimer import NOTICE_BYTES, NOTICE_DE, NOTICE_EN, pdf_content_errors
from testakte_file_filter import include_in_working_dump

ROOT = Path(__file__).resolve().parent.parent
SLUG = "enteignung-artikel-14"
PLUGIN = ROOT / SLUG
CASE = ROOT / "testakten/enteignung-verkehrsflaeche-goettingen"
FIXTURE = ROOT / "scripts/fixtures" / SLUG / "case.json"
SKILLS = {
    "eingriff-und-verfahrensstand-einordnen", "enteignungszweck-und-alternativen-pruefen",
    "freihandankauf-und-verhandlungen-fuehren", "grundstueck-rechte-und-beteiligte-klaeren",
    "entschaedigung-und-folgeschaeden-pruefen", "enteignungsverfahren-und-anhoerung-bearbeiten",
    "vorzeitige-besitzeinweisung-pruefen", "enteignungsbeschluss-und-vollzug-pruefen",
    "baulandsachen-und-eilrechtsschutz-bearbeiten",
}


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


BUILDER = module("enteignung_builder", "build-enteignung-artikel-14-case.py")
ZIP_BUILDER = module("enteignung_zip_check", "build-testakten-release-zips.py")
PROMPT_AUDIT = module("enteignung_prompt_check", "audit-prompt-profile-routing.py")


class EnteignungTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = BUILDER.load_case()
        cls.documents = cls.fixture["documents"]
        cls.profile = json.loads((ROOT / "quality/evals" / f"{SLUG}.json").read_text())

    def test_manifest_and_independent_skills(self):
        manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], SLUG)
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertLessEqual(len(manifest["description"]), 300)
        self.assertEqual({p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")}, SKILLS)

    def test_frontmatter_and_specific_workflows(self):
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            text = path.read_text()
            metadata = yaml.safe_load(text.split("---", 2)[1])
            self.assertEqual(set(metadata), {"name", "description"}, path)
            self.assertEqual(metadata["name"], path.parent.name)
            self.assertRegex(metadata["name"], r"^[a-z0-9-]{1,64}$")
            self.assertTrue(80 <= len(metadata["description"]) <= 1024)
            for heading in range(1, 7):
                self.assertRegex(text, rf"(?m)^#{{1,2}} {heading}\. ")
            self.assertIn("../../references/zitierweise.md", text)
            self.assertIn("Times New Roman 11 pt", text)
            self.assertGreater(len(text), 2200, path)

    def test_local_links(self):
        for base in (PLUGIN, CASE):
            for path in base.rglob("*.md"):
                for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                    if "://" not in target:
                        self.assertTrue((path.parent / target.split("#")[0]).exists(), (path, target))

    def test_editorial_profile_and_hashes(self):
        validate_profile(self.profile, SLUG, PLUGIN, ROOT)
        self.assertEqual(self.profile["prompt_workflow_review"]["method"], "desk_review")
        for kind, key in (("schnellstart", "mini_review"), ("werkstatt", "workshop_review")):
            data = (PLUGIN / f"{SLUG}-{kind}.md").read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), self.profile[key]["sha256"])

    def test_prompt_limits_and_decimal_structure(self):
        mini = (PLUGIN / f"{SLUG}-schnellstart.md").read_bytes()
        self.assertLessEqual(len(mini), 7500)
        self.assertLessEqual(len(mini.decode()), 7500)
        for kind in ("schnellstart", "werkstatt"):
            text = (PLUGIN / f"{SLUG}-{kind}.md").read_text()
            self.assertEqual(PROMPT_AUDIT.individual_workshop_structure_problems(text), [])
            for marker in ("Ordner", "104", "112", "113", "117", "Hannover", "224"):
                self.assertIn(marker, text)

    def test_no_unrelated_topic_or_section_symbols(self):
        for path in PLUGIN.rglob("*.md"):
            text = path.read_text()
            self.assertNotIn(chr(167), text, path)
            self.assertNotRegex(text, r"(?i)digital.omnibus|AI Act|KI-Verordnung")

    def test_key_legal_distinctions(self):
        text = (PLUGIN / "references/rechtsgrundlagen.md").read_text()
        for marker in ("keine selbständige Eingriffsgrundlage", "Sätze 3 und 4", "Ausführungsanordnung", "nicht zuständig", "zwei Wochen", "Landgericht Hannover", "243–246", "183"):
            self.assertIn(marker, text)
        rights = (PLUGIN / "skills/grundstueck-rechte-und-beteiligte-klaeren/SKILL.md").read_text()
        self.assertIn("Zugang der Anmeldung", rights)

    def test_evaluation_covers_all_skills_and_workflow(self):
        self.assertEqual({case["target_skill"] for case in self.profile["cases"]}, SKILLS)
        self.assertGreaterEqual(len(self.profile["cases"]), 10)
        for cid in ("leerer-einstieg", "ordner-einstieg", "anhoerung-fortsetzung", "baulandsache-eil"):
            self.assertIn(cid, {case["id"] for case in self.profile["cases"]})
        self.assertGreaterEqual(len(self.profile["sources"]), 25)

    def test_eleven_originals_and_existing_export_filter(self):
        expected = {doc["file"] for doc in self.documents}
        exported = {p.name for p in CASE.iterdir() if include_in_working_dump(p, CASE)}
        self.assertEqual(exported, expected)
        self.assertEqual(len(expected), 11)
        self.assertEqual({Path(name).suffix for name in expected}, {".eml", ".txt", ".pdf", ".docx", ".csv"})

    def test_individual_pdf_pages_and_full_content(self):
        for doc in self.documents:
            if doc["kind"] != "pdf":
                continue
            reader = PdfReader(CASE / doc["file"])
            self.assertEqual(len(reader.pages), len(doc["pages"]), doc["file"])
            for actual, source in zip(reader.pages, doc["pages"]):
                text = " ".join(actual.extract_text().split())
                self.assertIn(source["heading"], text)
                for paragraph in source["paragraphs"]:
                    self.assertIn(" ".join(paragraph.split()), text, doc["file"])
                self.assertGreater(len(text.split()), 180, doc["file"])
            self.assertEqual(pdf_content_errors((CASE / doc["file"]).read_bytes()), [])

    def test_docx_native_text_font_and_no_comments(self):
        path = CASE / "04_Technischer_Vermerk_20260818.docx"
        native = Document(path)
        paragraphs = [p.text for p in native.paragraphs]
        for page in self.documents[3]["pages"]:
            for paragraph in page["paragraphs"]:
                self.assertIn(paragraph, paragraphs)
        self.assertEqual(native.styles["Normal"].font.name, "Times New Roman")
        self.assertEqual(native.styles["Normal"].font.size.pt, 11)
        with ZipFile(path) as archive:
            self.assertNotIn("word/comments.xml", archive.namelist())
        for name in ("Title", "Heading 1", "Normal"):
            fonts = native.styles[name].element.rPr.rFonts
            self.assertFalse(any(key.endswith("Theme") for key in fonts.attrib))

    def test_eml_bodies_and_byte_identical_attachments(self):
        for doc in self.documents:
            if doc["kind"] != "eml":
                continue
            message = BytesParser(policy=policy.default).parsebytes((CASE / doc["file"]).read_bytes())
            self.assertEqual(message.defects, [])
            body = message.get_body(preferencelist=("plain",)).get_content()
            self.assertEqual(body.replace("\r\n", "\n").strip(), "\n\n".join(doc["paragraphs"]))
            attachments = list(message.iter_attachments())
            self.assertEqual([a.get_filename() for a in attachments], doc["attachments"])
            for item in attachments:
                self.assertEqual(item.get_payload(decode=True), (CASE / item.get_filename()).read_bytes())

    def test_csv_all_rows_and_arithmetic(self):
        doc = next(d for d in self.documents if d["kind"] == "csv")
        with (CASE / doc["file"]).open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.reader(stream, delimiter=";"))
        self.assertEqual(rows, [doc["headers"], *doc["rows"]])
        for row in rows[1:]:
            quantity, unit, amount = [Decimal(x.replace(",", ".")) for x in (row[4], row[6], row[7])]
            self.assertEqual(quantity * unit, amount, row[0])
        self.assertEqual(len(rows) - 1, 15)

    def test_area_and_price_facts(self):
        prop = self.fixture["property"]
        self.assertEqual(prop["area_m2"] - prop["permanent_m2"], prop["remaining_m2"])
        self.assertEqual(prop["temporary_m2"], 180)
        self.assertEqual(620 * 85, 52700)
        self.assertEqual(620 * 112, 69440)
        self.assertEqual(620 * 135, 83700)
        self.assertEqual(52700 + 7800, 60500)
        self.assertIn("keine Besitzeinweisung angeordnet", json.dumps(self.documents[-1], ensure_ascii=False))

    def test_source_prose_no_answer_key_or_disclaimer(self):
        text = json.dumps(self.documents, ensure_ascii=False)
        self.assertNotIn(chr(167), text)
        for forbidden in ("Musterlösung", "Lösungsskizze", "Prüferhinweis", NOTICE_DE, NOTICE_EN):
            self.assertNotIn(forbidden, text)
        for email in re.findall(r"[\w.+-]+@[\w.-]+", text):
            self.assertTrue(email.rstrip(".").endswith(".example"), email)

    def test_readmes_and_rubric(self):
        for path in (PLUGIN / "README.md", CASE / "README.md"):
            text = path.read_text()
            self.assertIn(NOTICE_DE, text)
            self.assertIn(NOTICE_EN, text)
        rubric = yaml.safe_load((CASE / "rubric.yaml").read_text())
        self.assertEqual(rubric["plugin"], SLUG)
        self.assertTrue(rubric["checks"])
        for check in rubric["checks"]:
            if check["check_type"] == "file_exists":
                self.assertTrue((CASE / check["path"]).is_file())

    def test_actual_zip_members_and_notice_in_memory_only(self):
        data = io.BytesIO()
        with ZipFile(data, "w") as archive:
            ZIP_BUILDER.add_testakte(archive, CASE)
        with ZipFile(data) as archive:
            self.assertEqual(archive.namelist()[0], "README.txt")
            self.assertEqual(archive.read("README.txt"), NOTICE_BYTES)
            expected = {"README.txt", *(doc["file"] for doc in self.documents)}
            aggregate = CASE / "gesamt-pdf" / f"{CASE.name}_gesamt.pdf"
            if aggregate.is_file():
                expected.add(aggregate.name)
                self.assertEqual(archive.read(aggregate.name), aggregate.read_bytes())
            self.assertEqual(set(archive.namelist()), expected)
            for doc in self.documents:
                self.assertEqual(archive.read(doc["file"]), (CASE / doc["file"]).read_bytes())

    def test_rebuild_is_byte_stable(self):
        with tempfile.TemporaryDirectory(prefix="enteignung-artikel-14-") as temp:
            paths = BUILDER.build(Path(temp) / "first")
            BUILDER.build(Path(temp) / "second")
            for path in paths:
                self.assertEqual(path.read_bytes(), (Path(temp) / "second" / path.name).read_bytes(), path.name)
                original = CASE / path.name
                if path.suffix == ".pdf":
                    # System fonts may differ; text and page boundaries must not.
                    actual = [" ".join(p.extract_text().split()) for p in PdfReader(path).pages]
                    expected = [" ".join(p.extract_text().split()) for p in PdfReader(original).pages]
                    self.assertEqual(actual, expected, path.name)
                elif path.suffix == ".eml":
                    actual = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                    expected = BytesParser(policy=policy.default).parsebytes(original.read_bytes())
                    for header in ("From", "To", "Date", "Subject", "Message-ID"):
                        self.assertEqual(" ".join(str(actual[header]).split()), " ".join(str(expected[header]).split()))
                    self.assertEqual(actual.get_body().get_content(), expected.get_body().get_content())
                    self.assertEqual([p.get_filename() for p in actual.iter_attachments()], [p.get_filename() for p in expected.iter_attachments()])
                    for part in actual.iter_attachments():
                        self.assertEqual(part.get_payload(decode=True), (path.parent / part.get_filename()).read_bytes())
                else:
                    self.assertEqual(path.read_bytes(), original.read_bytes(), path.name)

    def test_fixture_rejects_path_escape_and_unknown_attachment(self):
        for mutation in ("path", "attachment"):
            malformed = json.loads(FIXTURE.read_text())
            if mutation == "path":
                malformed["documents"][0]["file"] = "../outside.eml"
            else:
                malformed["documents"][0]["attachments"].append("missing.pdf")
            with tempfile.TemporaryDirectory(prefix="enteignung-artikel-14-") as temp:
                source = Path(temp) / "case.json"
                source.write_text(json.dumps(malformed))
                with self.assertRaises(ValueError):
                    BUILDER.load_case(source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
