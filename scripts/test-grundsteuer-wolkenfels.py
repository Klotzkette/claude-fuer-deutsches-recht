#!/usr/bin/env python3
"""Sichert die unveränderten Bescheide und ihre drei Auslieferungsfassungen."""

import hashlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
import zipfile

from pypdf import PdfReader

from testakte_disclaimer import NOTICE_BYTES
from testakte_einzelpdf_common import expected_arcnames


ROOT = Path(__file__).resolve().parent.parent
SLUG = "steuer-grundsteuer-wolkenfels-berlin"
CASE = ROOT / "testakten" / SLUG
ORIGINALS = {
    "01_grundsteuer_2025_mit_messbescheid.pdf": (
        "aca508377658e54ba8b11175d33ac46c50c4832d71f9f0631b3d18edb9ba21ff", 4
    ),
    "02_grundsteuerwert_2022.pdf": (
        "d2d981deae3662bf5ce6f628f93a818b0b5b8c7b5782d5f0ec28438e008a60ed", 3
    ),
}


def load_builder(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WolkenfelsTests(unittest.TestCase):
    def test_supplied_files_are_unchanged(self):
        for filename, (digest, pages) in ORIGINALS.items():
            with self.subTest(file=filename):
                data = (CASE / filename).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), digest)
                self.assertEqual(len(PdfReader(io.BytesIO(data)).pages), pages)

    def test_combined_pdf_preserves_all_original_pages(self):
        combined = PdfReader(CASE / "gesamt-pdf" / f"{SLUG}_gesamt.pdf")
        texts = [page.extract_text() for page in combined.pages]
        for filename in ORIGINALS:
            original = PdfReader(CASE / filename)
            for number, page in enumerate(original.pages, 1):
                with self.subTest(file=filename, page=number):
                    self.assertIn(page.extract_text(), texts)

    def test_archives_preserve_sources_and_stay_flat(self):
        expected = set(expected_arcnames(CASE))
        self.assertEqual(len(expected), 8)
        for builder_name in ("build-testakten-release-zips.py", "build-testakten-einzelpdf-zips.py"):
            with self.subTest(builder=builder_name), tempfile.TemporaryDirectory() as directory:
                builder = load_builder(builder_name)
                archive_path, _ = builder.build_single(CASE, Path(directory))
                validator = load_builder(builder_name.replace("build-", "validate-", 1))
                if "einzelpdf" in builder_name:
                    actual = validator.zip_entries(archive_path, expected_suffix=".pdf")
                    validator.assert_same(SLUG, sorted(expected | {"README.txt"}), actual)
                else:
                    actual = validator.zip_entries(archive_path, require_notice=True)
                    validator.assert_same(SLUG, validator.expected_entries(CASE), actual)
                with zipfile.ZipFile(archive_path) as archive:
                    names = archive.namelist()
                    self.assertEqual(len(names), len(set(names)))
                    self.assertTrue(all("/" not in name and "\\" not in name for name in names))
                    self.assertFalse(any(name.endswith(".md") for name in names))
                    self.assertEqual(archive.read("README.txt"), NOTICE_BYTES)
                    self.assertIsNone(archive.testzip())
                    for filename in ORIGINALS:
                        self.assertEqual(archive.read(filename), (CASE / filename).read_bytes())
                    if "einzelpdf" in builder_name:
                        self.assertEqual(set(names), expected | {"README.txt"})
                    else:
                        for source in CASE.iterdir():
                            if source.suffix in {".eml", ".txt", ".csv"}:
                                self.assertEqual(archive.read(source.name), source.read_bytes())

    def test_both_entry_points_link_to_same_case(self):
        for relative in ("fachanwalt-steuerrecht/README.md", "steuerrecht-anwalt-und-berater/README.md", "testakten/README.md"):
            with self.subTest(readme=relative):
                self.assertIn(SLUG, (ROOT / relative).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
