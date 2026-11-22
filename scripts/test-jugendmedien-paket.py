#!/usr/bin/env python3
"""Prüft echte Jugendmedien-Pakete und die Trennung von Grundakte und Fortgang.

Die Prüfungen bauen ausschließlich in temporären Verzeichnissen. Sie prüfen
Dateien, Archivinhalt und Arbeitsmaterial; ein juristischer Modelltest wird
hierdurch nicht behauptet.
"""
from __future__ import annotations

import copy
import csv
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import parse_qs, urlparse
import zipfile

from package_edition import edition_routes
from release_routing import RELEASE_BASE, scoped_asset_url


ROOT = Path(__file__).resolve().parents[1]
NAME = "jugendmedienschutz-und-medienangebote"
PLUGIN = ROOT / NAME
EXPECTED_SKILLS = {
    "medienangebot-pruefen",
    "angebot-und-rollen-einordnen",
    "inhalte-und-altersstufen-pruefen",
    "alterskennzeichnung-und-zugangsschutz",
    "jugendschutzorganisation-aufbauen",
    "chat-und-ugc-moderieren",
    "ki-szenarien-verantworten",
    "datenschutz-und-plattformpflichten",
    "medienpflichten-und-werbung",
    "aufsichtsverfahren-bearbeiten",
}
REFERENCES = {
    "references/amtliche-quellen.md",
    "references/fallpruefung.md",
    "references/zitierweise.md",
    "references/arbeitsoberflaeche-und-visualisierung.md",
}
PROMPT_SNAPSHOTS = {
    f"{NAME}-{kind}.{ext}"
    for kind in ("werkstatt", "schnellstart")
    for ext in ("md", "txt")
}


def load_module(filename: str):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RELEASE = load_module("build-skill-quality-release.py")


def rewrite_archive(path: Path, *, remove: str | None = None, replace: tuple[str, bytes] | None = None) -> None:
    """Manipuliertes Downloadarchiv für eine negative Prüfung erzeugen."""
    replacement = dict([replace]) if replace else {}
    temporary = path.with_suffix(".changed.zip")
    with zipfile.ZipFile(path) as source, zipfile.ZipFile(temporary, "w") as target:
        for info in source.infolist():
            if info.filename != remove:
                target.writestr(info, replacement.get(info.filename, source.read(info.filename)))
    temporary.replace(path)


class JugendmedienPaketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="jugendmedien-paket-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.base = Path(cls.temp.name)
        full_scope = json.loads((ROOT / "scripts/data/skill-quality-release-scope.json").read_text())
        plugin_scope = next(p for p in full_scope["plugins"] if p["name"] == NAME)
        cls.scope = {
            "schema_version": full_scope["schema_version"],
            "version": full_scope["version"],
            "tag": full_scope["tag"],
            "plugins": [copy.deepcopy(plugin_scope)],
        }
        # Echte Arbeitsdateien am aktuellen Commit, aber die beiden Routen der
        # historischen Qualitätsrunde in einer eigenen kleinen Registry.
        cls.package_root = cls.base / "paketquelle"
        subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout",
                        str(ROOT), str(cls.package_root)], check=True)
        shutil.copytree(PLUGIN, cls.package_root / NAME)
        for relative in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE", "README.md", "ASSET_INDEX.md",
                         "SKILLS.md", "testakten/README.md", f"skills-index/{NAME}.md",
                         "docs/grundakten-lebenswelt/README.md", f"quality/evals/{NAME}.json"):
            destination = cls.package_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        market["plugins"] = [entry for entry in market["plugins"] if entry["name"] == NAME]
        planned = edition_routes(ROOT)
        cls.package_routes = {asset: planned[asset] for asset in (f"{NAME}.zip", f"{NAME}-portable.zip")}
        registry = {"schema_version": 1, "assets": {asset: old for asset, (old, _) in cls.package_routes.items()}}
        for relative, data in ((".claude-plugin/marketplace.json", market), ("scripts/scoped-release-assets.json", registry)):
            destination = cls.package_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(json.dumps(data), encoding="utf-8")
        cls.dist = cls.base / "original"
        cls.report = RELEASE.build(cls.dist, cls.scope, cls.package_root)

    def copied_dist(self, name: str) -> Path:
        target = self.base / name
        shutil.copytree(self.dist, target)
        return target

    def expected_sources(self) -> dict[str, Path]:
        # Unabhängig von source_files/package_path: Ein versehentlich erweitertes
        # Ausschlussmuster des Builders darf fehlende Referenzen nicht legitimieren.
        excluded = {".git", ".venv", "node_modules", "__pycache__", "testakte", "testakten"}
        files = {
            p.relative_to(PLUGIN).as_posix(): p
            for p in PLUGIN.rglob("*")
            if p.is_file()
            and not excluded.intersection(p.relative_to(PLUGIN).parts)
            and p.name not in {"CLAUDE.md", ".DS_Store"}
            and p.suffix != ".pyc"
            and p.relative_to(PLUGIN).as_posix() not in PROMPT_SNAPSHOTS
        }
        for filename in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
            if filename not in files and (ROOT / filename).is_file():
                files[filename] = ROOT / filename
        return files

    def test_release_builder_keeps_ten_routes_and_all_local_sources(self):
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        self.assertEqual(self.report["source_state"]["commit"], commit)
        expected = self.expected_sources()
        self.assertTrue(REFERENCES <= set(expected))
        skills = {p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(skills, EXPECTED_SKILLS)
        active = RELEASE.verify_reachability(expected)
        self.assertEqual(set(active), {f"skills/{name}/SKILL.md" for name in EXPECTED_SKILLS})
        self.assertEqual(set(self.report["plugins"][NAME]["skills"]), set(active))

        with zipfile.ZipFile(self.dist / f"{NAME}.zip") as native, zipfile.ZipFile(
            self.dist / f"{NAME}-portable.zip"
        ) as portable:
            self.assertEqual(len(native.namelist()), len(set(native.namelist())))
            self.assertEqual(set(native.namelist()), set(expected))
            self.assertEqual(set(portable.namelist()), {f"{NAME}/{name}" for name in expected})
            for name, source in expected.items():
                with self.subTest(member=name):
                    data = source.read_bytes()
                    if name == "README.md":
                        # All cross-repository paths in this specific source are
                        # explicit blob/main URLs. Check their exact rendering
                        # independently of the packaging helper.
                        prefix = b"https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/"
                        revision = self.report["source_state"]["commit"].encode("ascii")
                        data = data.replace(prefix + b"main/", prefix + revision + b"/")
                    self.assertEqual(native.read(name), data)
                    self.assertEqual(portable.read(f"{NAME}/{name}"), data)
            for manifest in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "plugin.json"):
                data = json.loads(native.read(manifest))
                self.assertEqual((data["name"], data["version"]), (NAME, self.scope["version"]))
            self.assertFalse(any(set(Path(name).parts) & {"testakte", "testakten"} for name in native.namelist()))

    def test_prompt_snapshots_remain_separate_and_byte_exact(self):
        plugin_scope = self.scope["plugins"][0]
        prompts = set(plugin_scope["prompts"])
        preserved = plugin_scope.get("preserved_prompts", {})
        self.assertFalse(prompts & set(preserved))
        self.assertEqual(prompts | set(preserved), PROMPT_SNAPSHOTS)
        self.assertEqual(set(self.report["prompts"]), prompts)
        for filename in PROMPT_SNAPSHOTS:
            with self.subTest(prompt=filename):
                data = (PLUGIN / filename).read_bytes()
                digest = hashlib.sha256(data).hexdigest()
                if filename in preserved:
                    self.assertEqual(preserved[filename], digest)
                    self.assertFalse((self.dist / filename).exists())
                else:
                    self.assertEqual((self.dist / filename).read_bytes(), data)
                    self.assertEqual(self.report["prompts"][filename], digest)
        for kind in ("werkstatt", "schnellstart"):
            self.assertEqual((PLUGIN / f"{NAME}-{kind}.md").read_bytes(), (PLUGIN / f"{NAME}-{kind}.txt").read_bytes())
        self.assertEqual(set(p.name for p in self.dist.iterdir()), prompts | {
            f"{NAME}.zip", f"{NAME}-portable.zip", RELEASE.REPORT, RELEASE.CHECKSUMS,
        })

    def test_all_four_prompt_download_routes_remain_available_in_readme(self):
        # Die bestehende separate Publikation erfolgt über download.html, nicht
        # über das neue Plugin-ZIP. Dies prüft die belegten öffentlichen Routen;
        # eine erfolgreiche Netzabfrage wird damit nicht behauptet.
        links = re.findall(r"\]\(([^)]+)\)", (PLUGIN / "README.md").read_text())
        published_paths = set()
        for target in links:
            url = urlparse(target)
            if (url.scheme, url.netloc, url.path) == (
                "https", "klotzkette.github.io", "/claude-fuer-deutsches-recht/download.html"
            ):
                published_paths.update(parse_qs(url.query).get("path", []))
        self.assertTrue({f"{NAME}/{filename}" for filename in PROMPT_SNAPSHOTS} <= published_paths)

    def test_installer_links_match_the_active_registered_release(self):
        links = re.findall(r"\]\(([^)]+)\)", (PLUGIN / "README.md").read_text())
        tags = set()
        for asset, (previous, successor) in self.package_routes.items():
            self.assertEqual(previous, self.scope["tag"])
            url = scoped_asset_url(asset, root=ROOT)
            self.assertIn(url, {f"{RELEASE_BASE}/download/{tag}/{asset}" for tag in (previous, successor)})
            self.assertEqual({link for link in links if link.endswith("/" + asset)}, {url})
            tags.add(url.rsplit("/", 2)[1])
        self.assertEqual(len(tags), 1, "Natives und portables Paket müssen auf dieselbe Ausgabe zeigen")

    def test_preserved_snapshot_loss_hash_mismatch_and_changed_source_are_rejected(self):
        # Eigene kleine Scope-Fixture: Keine Produktdatei wird manipuliert und
        # aktuelle Paketversionen beeinflussen nicht die vier Prompt-Negativfälle.
        for mutation in ("missing", "hash", "changed-source", "duplicate"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory(dir=self.base) as folder:
                root = Path(folder)
                directory = root / NAME
                directory.mkdir()
                for filename in PROMPT_SNAPSHOTS:
                    shutil.copyfile(PLUGIN / filename, directory / filename)
                (root / ".claude-plugin").mkdir()
                (root / ".claude-plugin/marketplace.json").write_text(json.dumps({
                    "version": self.scope["version"],
                    "plugins": [{"name": NAME, "source": "./" + NAME, "version": self.scope["version"]}],
                }))
                (root / "scripts").mkdir()
                (root / "scripts/scoped-release-assets.json").write_text(json.dumps({
                    "schema_version": 1,
                    "assets": {f"{NAME}{suffix}.zip": self.scope["tag"] for suffix in ("", "-portable")},
                }))
                scope = copy.deepcopy(self.scope)
                row = scope["plugins"][0]
                row["prompts"] = []
                row["preserved_prompts"] = {
                    filename: hashlib.sha256((directory / filename).read_bytes()).hexdigest()
                    for filename in PROMPT_SNAPSHOTS
                }
                RELEASE.validate_scope(scope, root)
                filename = f"{NAME}-werkstatt.md"
                if mutation == "missing":
                    del row["preserved_prompts"][filename]
                    error = "nicht vollständig deklariert"
                elif mutation == "hash":
                    row["preserved_prompts"][filename] = "0" * 64
                    error = "muss neu veröffentlicht werden"
                elif mutation == "changed-source":
                    (directory / filename).write_bytes(b"Ungepruefter neuer Prompt\n")
                    error = "muss neu veröffentlicht werden"
                else:
                    row["prompts"].append(filename)
                    error = "doppelt deklarierter"
                with self.assertRaisesRegex(ValueError, error):
                    RELEASE.validate_scope(scope, root)

    def test_missing_local_source_is_rejected_before_packaging(self):
        files = self.expected_sources()
        del files["references/amtliche-quellen.md"]
        with self.assertRaisesRegex(ValueError, "Paketverweis fehlt"):
            RELEASE.verify_reachability(files)

    def test_missing_native_reference_is_rejected_after_checksum_refresh(self):
        dist = self.copied_dist("missing-reference")
        rewrite_archive(dist / f"{NAME}.zip", remove="references/fallpruefung.md")
        RELEASE.write_checksums(dist)
        with self.assertRaisesRegex(ValueError, "Dateiliste weicht"):
            RELEASE.validate_assets(dist, self.scope, self.package_root)

    def test_portable_skill_loss_is_rejected_after_checksum_refresh(self):
        dist = self.copied_dist("missing-portable-skill")
        rewrite_archive(dist / f"{NAME}-portable.zip", remove=f"{NAME}/skills/chat-und-ugc-moderieren/SKILL.md")
        RELEASE.write_checksums(dist)
        with self.assertRaisesRegex(ValueError, "Dateiliste weicht"):
            RELEASE.validate_assets(dist, self.scope, self.package_root)

    def test_changed_reference_is_rejected_even_with_valid_outer_checksums(self):
        dist = self.copied_dist("changed-reference")
        rewrite_archive(dist / f"{NAME}.zip", replace=("references/amtliche-quellen.md", b"Fremder Quellenstand\n"))
        RELEASE.write_checksums(dist)
        with self.assertRaisesRegex(ValueError, "Inhalt weicht"):
            RELEASE.validate_assets(dist, self.scope, self.package_root)


class JugendmedienGrundakteTests(unittest.TestCase):
    """Prüft die ausgelieferte Akte, ohne im CI lizenzierte Fonts zu ersetzen."""

    @classmethod
    def setUpClass(cls):
        cls.builder = load_module("build-jugendmedien-testakte.py")
        cls.payload = json.loads((ROOT / "scripts/data/jugendmedien-wolkenwerft.json").read_text())
        cls.archive = PLUGIN / "testakte/downloads/testakte-jugendmedien-wolkenwerft-originaldateien.zip"
        cls.folders = {
            "G": "01_Grundakte_ohne_Loesung",
            "N": "02_Nachreichungen",
            "V": "03_Vorlagen",
        }

    def test_fixture_keeps_initial_file_and_later_events_separate(self):
        self.builder.validate_documents(self.payload)
        documents = self.payload["documents"]
        expected_ids = {f"G{i:02d}" for i in range(1, 26)} | {
            f"{prefix}{i:02d}" for prefix in ("N", "V") for i in range(1, 5)
        }
        self.assertEqual({d["id"] for d in documents}, expected_ids)
        self.assertEqual(len(documents), len(expected_ids))
        for document in documents:
            with self.subTest(document=document["id"]):
                self.assertEqual(document["folder"], self.folders[document["id"][0]])
                self.assertEqual(Path(document["filename"]).suffix, "." + document["format"])
                if document["id"].startswith("G"):
                    self.assertLessEqual(document["date"], self.payload["case"]["date"])
        # Die spätere Behördenanhörung gehört ausdrücklich nicht zum Erstzugang.
        hearing = next(d for d in documents if d["id"] == "N03")
        self.assertGreater(hearing["date"], self.payload["case"]["date"])
        self.assertEqual(hearing["folder"], "02_Nachreichungen")

    def test_builder_rejects_later_documents_in_initial_file(self):
        payload = copy.deepcopy(self.payload)
        next(d for d in payload["documents"] if d["id"] == "N03")["folder"] = "01_Grundakte_ohne_Loesung"
        with self.assertRaises(ValueError):
            self.builder.validate_documents(payload)

    def test_builder_rejects_lost_initial_document_and_duplicate_paths(self):
        for mutation in ("missing-document", "wrong-folder", "duplicate-id", "duplicate-path", "path-traversal", "empty-text"):
            with self.subTest(mutation=mutation):
                payload = copy.deepcopy(self.payload)
                first, second = payload["documents"][:2]
                if mutation == "missing-document":
                    payload["documents"].pop(0)
                elif mutation == "wrong-folder":
                    first["folder"] = "02_Nachreichungen"
                elif mutation == "duplicate-id":
                    second["id"] = first["id"]
                elif mutation == "duplicate-path":
                    second["filename"] = first["filename"]
                    second["format"] = first["format"]
                elif mutation == "path-traversal":
                    first["filename"] = "../G01_Auftrag.docx"
                else:
                    first["paragraphs"] = []
                with self.assertRaises(ValueError):
                    self.builder.validate_documents(payload)

    def test_download_contains_all_native_documents_and_only_their_phase(self):
        documents = self.payload["documents"]
        expected = {f'{d["folder"]}/{d["filename"]}' for d in documents}
        expected |= {"README.txt", "03_Vorlagen/V05_Leere_Arbeitsmatrix.xlsx"}
        with zipfile.ZipFile(self.archive) as archive:
            members = archive.namelist()
            self.assertEqual(len(members), len(set(members)))
            self.assertEqual(set(members), expected)
            self.assertEqual(len([n for n in members if n.startswith("01_Grundakte_ohne_Loesung/")]), 25)
            self.assertFalse(any(Path(name).name == self.builder.PDF_NAME for name in members))
            readme = archive.read("README.txt").decode("utf-8-sig")
            self.assertIn("01_Grundakte_ohne_Loesung", readme)
            self.assertIn("02_Nachreichungen", readme)
            self.assertIn("fiktiv", readme.lower())
            for document in documents:
                name = f'{document["folder"]}/{document["filename"]}'
                with self.subTest(member=name):
                    self.assert_native_content(archive.read(name), document)
            from openpyxl import load_workbook
            workbook = load_workbook(io.BytesIO(archive.read("03_Vorlagen/V05_Leere_Arbeitsmatrix.xlsx")))
            self.assertTrue(workbook.sheetnames)
            self.assertFalse(workbook._external_links)
            self.assertGreater(sum(sheet.max_column for sheet in workbook), 1)

    def test_inventory_matches_native_files_and_separate_reading_pdf(self):
        from pypdf import PdfReader
        case = PLUGIN / "testakte"
        inventory = json.loads((case / "bestand.json").read_text())
        self.assertEqual(inventory["source_sha256"], hashlib.sha256((ROOT / inventory["source"]).read_bytes()).hexdigest())
        self.assertEqual(
            (inventory["original_count"], inventory["grundakte_count"], inventory["nachreichungen_count"], inventory["vorlagen_count"]),
            (34, 25, 4, 5),
        )
        paths = {entry["file"] for entry in inventory["originals"]}
        self.assertEqual(len(paths), 34)
        actual = {p.relative_to(case).as_posix() for folder in self.folders.values() for p in (case / folder).rglob("*") if p.is_file()}
        self.assertEqual(paths, actual)
        with zipfile.ZipFile(self.archive) as archive:
            self.assertEqual(paths, set(archive.namelist()) - {"README.txt"})
            for entry in inventory["originals"]:
                with self.subTest(original=entry["file"]):
                    raw = (case / entry["file"]).read_bytes()
                    self.assertEqual(archive.read(entry["file"]), raw)
                    self.assertEqual(len(raw), entry["bytes"])
                    self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])
        self.assertEqual([entry["id"] for entry in inventory["pdfs"]], [d["id"] for d in self.payload["documents"]])
        first_page = 1
        for entry in inventory["pdfs"]:
            with self.subTest(reading_document=entry["id"]):
                path = case / entry["file"]
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), entry["sha256"])
                self.assertEqual(entry["first_page"], first_page)
                self.assertEqual(len(PdfReader(path).pages), entry["pages"])
                first_page += entry["pages"]
        self.assertEqual(inventory["pdf_documents"], 33)
        self.assertEqual(inventory["pages"], first_page - 1)
        self.assertEqual({entry["file"] for entry in inventory["downloads"]}, {
            "downloads/testakte-jugendmedien-wolkenwerft-originaldateien.zip",
            "downloads/testakte-jugendmedien-wolkenwerft-gesamt.pdf",
        })
        for entry in inventory["downloads"]:
            path = case / entry["file"]
            self.assertEqual(path.stat().st_size, entry["bytes"])
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), entry["sha256"])
            if path.suffix == ".pdf":
                self.assertEqual(len(PdfReader(path).pages), inventory["pages"])

    def assert_native_content(self, raw: bytes, document: dict) -> None:
        """Inhalte wirklich parsen: Dateiendungen allein belegen kein Arbeitsformat."""
        kind = document["format"]
        if kind == "csv":
            text = raw.decode("utf-8-sig")
            dialect = csv.Sniffer().sniff(text, delimiters=",;\t")
            parsed = list(csv.reader(io.StringIO(text), dialect))
            self.assertEqual(parsed[0], document["columns"])
            self.assertEqual(parsed[1:], [[str(value) for value in row] for row in document["rows"]])
        elif kind == "json":
            self.assertEqual(json.loads(raw), document["data"])
        elif kind == "txt":
            self.assertEqual(raw.decode("utf-8-sig").strip(), document["nativeText"].strip())
        elif kind == "eml":
            message = BytesParser(policy=policy.default).parsebytes(raw)
            self.assertFalse(message.defects)
            self.assertEqual(str(message["Subject"]), document["subject"])
            self.assertEqual(str(message["Message-ID"]), document["messageId"])
            self.assertIsNotNone(message["Date"])
            self.assertEqual(parsedate_to_datetime(str(message["Date"])).date().isoformat(), document["date"])
            self.assertIsNotNone(message["From"])
            self.assertIsNotNone(message["To"])
            body = message.get_body(preferencelist=("plain",)).get_content()
            for paragraph in document["paragraphs"]:
                self.assertIn(" ".join(paragraph.split()), " ".join(body.split()))
        elif kind == "docx":
            from docx import Document
            parsed = Document(io.BytesIO(raw))
            text = "\n".join(p.text for p in parsed.paragraphs)
            text += "\n" + "\n".join(c.text for t in parsed.tables for r in t.rows for c in r.cells)
            for paragraph in document["paragraphs"]:
                self.assertIn(" ".join(paragraph.split()), " ".join(text.split()))
        elif kind == "pdf":
            from pypdf import PdfReader
            pdf = PdfReader(io.BytesIO(raw))
            self.assertFalse(pdf.is_encrypted)
            self.assertGreater(len(pdf.pages), 0)
            text = "".join(page.extract_text() or "" for page in pdf.pages)
            compact = "".join(text.split()).replace("\u00ad", "")
            for paragraph in document["paragraphs"]:
                self.assertIn("".join(paragraph.split()).replace("\u00ad", ""), compact)
        else:
            self.fail(f"Nicht geprüftes Originalformat: {kind}")

    def test_word_reading_pdfs_embed_the_required_font_and_reject_substitution(self):
        from pypdf import PdfReader, PdfWriter
        from pypdf.generic import NameObject
        case = PLUGIN / "testakte"
        inventory = json.loads((case / "bestand.json").read_text())
        word_ids = {d["id"] for d in self.payload["documents"] if d["format"] == "docx"}
        pdfs = [case / row["file"] for row in inventory["pdfs"] if row["id"] in word_ids]
        self.assertEqual(len(pdfs), len(word_ids))
        for path in pdfs:
            with self.subTest(document=path.name):
                self.assertTrue(self.builder.validate_docx_pdf_fonts(path))
        # Regression for the actual LibreOffice fallback found during production.
        # A readable PDF must fail even when the source DOCX still declares TNR.
        with tempfile.TemporaryDirectory() as folder:
            writer = PdfWriter()
            writer.append(PdfReader(pdfs[0]))
            resource = writer.pages[0]["/Resources"]["/Font"].get_object()
            first = next(iter(resource.values())).get_object()
            first[NameObject("/BaseFont")] = NameObject("/LiberationSerif")
            changed = Path(folder) / "substituted.pdf"
            writer.write(changed)
            with self.assertRaisesRegex(ValueError, "Unexpected font substitution"):
                self.builder.validate_docx_pdf_fonts(changed)


if __name__ == "__main__":
    unittest.main()
