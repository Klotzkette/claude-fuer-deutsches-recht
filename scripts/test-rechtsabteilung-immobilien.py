#!/usr/bin/env python3
"""Regressionsprüfung der vollständigen, getrennt installierbaren Übernahme."""

import hashlib
import importlib.util
import io
import json
import posixpath
import tempfile
import unittest
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "immo_build", ROOT / "scripts/build-rechtsabteilung-immobilien.py"
)
BUILD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILD)
P, B, PROJECT = BUILD.PLUGIN, BUILD.COMPANION, BUILD.PROJECT


class ImportTests(unittest.TestCase):
    def test_snapshot_is_complete_and_unchanged(self):
        record = json.loads((PROJECT / "herkunft.json").read_text())
        with zipfile.ZipFile(BUILD.SNAPSHOT) as archive:
            files = {
                item.filename: hashlib.sha256(archive.read(item)).hexdigest()
                for item in archive.infolist()
                if not item.is_dir()
            }
        self.assertEqual(len(files), 373)
        self.assertEqual(record["source_files"], files)
        self.assertEqual(
            hashlib.sha256(BUILD.SNAPSHOT.read_bytes()).hexdigest(), BUILD.SOURCE_SHA256
        )

    def test_every_original_skill_and_reference_survives(self):
        with zipfile.ZipFile(BUILD.SNAPSHOT) as archive:
            for old, new, count in (
                ("forderungsmanagement-immobilien", P, 50),
                (B, B, 9),
            ):
                self.assertEqual(
                    len(list((ROOT / new / "skills").glob("*/SKILL.md"))), count
                )
                for item in archive.infolist():
                    if item.is_dir() or not item.filename.startswith(
                        (old + "/skills/", old + "/references/")
                    ):
                        continue
                    relative = item.filename.removeprefix(old + "/")
                    target = ROOT / new / relative
                    self.assertTrue(target.is_file(), relative)
                    if relative == "skills/06-fallziel-renofa-triage/SKILL.md":
                        self.assertIn("wird nicht unterstellt", target.read_text())
                    else:
                        self.assertEqual(
                            target.read_bytes(), archive.read(item), relative
                        )

    def test_plugins_have_consistent_marketplace_identity(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = {row["name"]: row for row in marketplace["plugins"]}
        for name in (P, B):
            manifest = json.loads(
                (ROOT / name / ".claude-plugin/plugin.json").read_text()
            )
            self.assertEqual(manifest["name"], name)
            self.assertEqual(manifest["version"], marketplace["version"])
            self.assertEqual(entries[name]["source"], "./" + name)
            self.assertLessEqual(len(name), 64)
            self.assertLessEqual(len(manifest["description"]), 300)

    def test_flat_case_downloads_are_complete(self):
        provenance = json.loads((PROJECT / "herkunft.json").read_text())
        self.assertEqual(len(provenance["cases"]), 10)
        self.assertEqual(sum(row["documents"] for row in provenance["cases"]), 174)
        for row in provenance["cases"]:
            base = PROJECT / "downloads" / ("testakte-" + row["slug"])
            for suffix, formats in (
                (".zip", {".docx", ".xlsx", ".pdf"}),
                ("-einzel-pdfs.zip", {".pdf"}),
            ):
                with zipfile.ZipFile(str(base) + suffix) as archive:
                    self.assertIsNone(archive.testzip())
                    self.assertEqual(archive.read("README.txt"), NOTICE_BYTES)
                    files = [
                        name for name in archive.namelist() if name != "README.txt"
                    ]
                    self.assertEqual(len(files), row["documents"])
                    self.assertEqual(
                        len({name.casefold() for name in files}), len(files)
                    )
                    for name in files:
                        self.assertEqual(name, Path(name).name)
                        self.assertTrue(name.isascii())
                        self.assertIn(Path(name).suffix, formats)
                        if name.endswith(".pdf"):
                            self.assertGreater(
                                len(PdfReader(io.BytesIO(archive.read(name))).pages), 0
                            )
            self.assertGreater(len(PdfReader(str(base) + "-gesamt.pdf").pages), 0)

    def test_local_markdown_links_and_no_private_dependency(self):
        parser = MarkdownIt("commonmark")
        files = [
            path
            for folder in (ROOT / P, ROOT / B, PROJECT)
            for path in folder.rglob("*.md")
        ]
        for path in files:
            text = path.read_text()
            self.assertNotIn(
                "github.com/Klotzkette/immobilien-forderungsmanagement/releases",
                text,
                str(path),
            )
            for token in parser.parse(text):
                for child in token.children or []:
                    if child.type not in {"link_open", "image"}:
                        continue
                    href = child.attrGet("href") or child.attrGet("src")
                    url = urlsplit(href)
                    if url.scheme or url.netloc or not url.path:
                        continue
                    target = (path.parent / unquote(url.path)).resolve()
                    self.assertTrue(
                        target.is_relative_to(ROOT) and target.exists(),
                        f"{path.relative_to(ROOT)}: {href}",
                    )

    def test_prompts_are_separate_and_within_budget(self):
        mini = (ROOT / P / f"{P}-schnellstart.md").read_bytes()
        self.assertLessEqual(len(mini), 7500)
        self.assertLessEqual(len(mini.decode()), 7500)
        self.assertTrue(mini.decode().startswith("# " + BUILD.TITLE))
        for name in (P, B):
            for path in (ROOT / name / "skills").rglob("*"):
                self.assertNotIn("werkstattprompt", path.name)
                self.assertNotIn("schnellstartprompt", path.name)

    def test_package_keeps_source_archive_out_of_runtime(self):
        with tempfile.TemporaryDirectory() as directory:
            dist = Path(directory)
            BUILD.build_packages(dist)
            for name, count in ((P, 50), (B, 9)):
                with zipfile.ZipFile(dist / f"{name}.zip") as archive:
                    self.assertIn(".claude-plugin/plugin.json", archive.namelist())
                    self.assertEqual(
                        sum(
                            n.startswith("skills/") and n.endswith("/SKILL.md")
                            for n in archive.namelist()
                        ),
                        count,
                    )
                    self.assertFalse(
                        any(
                            n.endswith(("-werkstatt.md", "-schnellstart.md", ".zip"))
                            for n in archive.namelist()
                        )
                    )
                    self.assertFalse(any("testakten/" in n for n in archive.namelist()))
            with zipfile.ZipFile(dist / f"{P}-vollstaendig.zip") as archive:
                self.assertTrue(archive.read("README.txt").startswith(NOTICE_BYTES))
                self.assertEqual(
                    archive.read(f"projekte/{P}/quellstand-v5.27.1.zip"),
                    BUILD.SNAPSHOT.read_bytes(),
                )
                # Offline-Navigation darf keine Dateien aus der übrigen Sammlung benötigen.
                names = set(archive.namelist())
                parser = MarkdownIt("commonmark")
                for name in sorted(names):
                    if not name.endswith(".md"):
                        continue
                    for token in parser.parse(archive.read(name).decode("utf-8")):
                        for child in token.children or []:
                            if child.type not in {"link_open", "image"}:
                                continue
                            href = child.attrGet("href") or child.attrGet("src")
                            url = urlsplit(href)
                            if url.scheme or url.netloc or not url.path:
                                continue
                            target = posixpath.normpath(
                                posixpath.join(
                                    posixpath.dirname(name), unquote(url.path)
                                )
                            )
                            self.assertTrue(
                                target in names
                                or any(n.startswith(target + "/") for n in names),
                                f"Offline-Paket {name}: {href}",
                            )

    def test_export_rejects_nested_input(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = (
                Path(directory) / "source.zip",
                Path(directory) / "target.zip",
            )
            with zipfile.ZipFile(source, "w") as archive:
                archive.writestr("nested/file.pdf", b"invalid")
            with self.assertRaisesRegex(ValueError, "Nicht flacher"):
                BUILD.adapt_case_zip(source, target, pdf_only=True)


if __name__ == "__main__":
    unittest.main()
