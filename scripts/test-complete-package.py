#!/usr/bin/env python3
"""Offline-Vertragstests für das vollständige, deduplizierte Releasepaket."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from unittest.mock import patch

import release_asset_common as assets
from testakte_disclaimer import NOTICE_BYTES

SPEC = importlib.util.spec_from_file_location("complete_package", Path(__file__).with_name("build-complete-package.py"))
assert SPEC and SPEC.loader
B = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(B)


class CompletePackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="complete-package-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "source"
        self.dist = Path(self.temporary.name) / "dist"
        self.dist.mkdir()
        (self.root / ".claude-plugin").mkdir(parents=True)
        self.marketplace = json.dumps({"plugins": [{"name": "eins"}, {"name": "zwei"}]}).encode()
        (self.dist / "marketplace.json").write_bytes(self.marketplace)
        (self.root / ".claude-plugin/marketplace.json").write_bytes(self.marketplace)
        for name in B.OVERVIEWS:
            (self.root / name).write_text(f"Übersicht {name}\n", encoding="utf-8")
        for name in ("quality/evals/eins.json", "skills-index/eins.md"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"Inhalt {name}\n", encoding="utf-8")
        (self.root / "quality/.DS_Store").write_bytes(b"nicht ausliefern")
        self.members = {
            "alle-plugins-megazip.zip": {"eins.zip": b"Plugin eins", "zwei.zip": b"Plugin zwei", "marketplace.json": self.marketplace},
            "alle-skills-markdown.zip": {"eins-skills-markdown.zip": b"Skills eins", "zwei-skills-markdown.zip": b"Skills zwei"},
            "alle-testakten.zip": {"README.txt": NOTICE_BYTES, "testakte-zentral.zip": b"Originalformate zentral\x00\xff"},
            "alle-testakten-einzelpdfs.zip": {"README.txt": NOTICE_BYTES, "testakte-zentral-einzelpdfs.zip": b"EinzelPDFs zentral\x00\xff"},
            "alle-pluginlokalen-testakten.zip": {"README.txt": NOTICE_BYTES, "eins-testakte.zip": b"Originalformate lokal\x00\xff"},
            "alle-pluginlokalen-testakten-einzelpdfs.zip": {"README.txt": NOTICE_BYTES, "eins-testakte-einzelpdfs.zip": b"EinzelPDFs lokal\x00\xff"},
        }
        for name in self.members:
            self.write_bundle(name)

    def write_bundle(self, name):
        with zipfile.ZipFile(self.dist / name, "w", zipfile.ZIP_DEFLATED) as archive:
            for member, data in self.members[name].items():
                archive.writestr(member, data)

    def test_complete_inventory_bytes_and_notice_without_duplicate_bundles(self):
        original = {name: (self.dist / name).read_bytes() for name in B.BUNDLES}
        result = B.build(self.dist, self.root)
        self.assertEqual(result.name, "alles-komplettpaket.zip")
        with zipfile.ZipFile(result) as archive:
            expected = {"README.txt": B.PACKAGE_README, "marketplace.json": self.marketplace}
            for name in B.OVERVIEWS:
                expected[f"uebersichten/{name}"] = (self.root / name).read_bytes()
            for name in ("quality/evals/eins.json", "skills-index/eins.md"):
                expected[f"uebersichten/{name}"] = (self.root / name).read_bytes()
            for bundle, directory in B.BUNDLES.items():
                for name, data in self.members[bundle].items():
                    if name.endswith(".zip"):
                        expected[f"{directory}/{name}"] = data
            self.assertEqual(archive.namelist()[0], "README.txt")
            self.assertTrue(archive.read("README.txt").startswith(NOTICE_BYTES))
            self.assertIn("genau einmal", archive.read("README.txt").decode())
            self.assertEqual(set(archive.namelist()), set(expected))
            self.assertEqual(len(archive.namelist()), len(expected))
            for name, data in expected.items():
                self.assertEqual(archive.read(name), data, name)
                if name.endswith(".zip"):
                    self.assertEqual(archive.getinfo(name).compress_type, zipfile.ZIP_STORED)
            self.assertIsNone(archive.testzip())
        for name, data in original.items():
            self.assertEqual((self.dist / name).read_bytes(), data, "Sammeldownload bleibt unverändert")
        first = result.read_bytes()
        self.assertEqual(B.build(self.dist, self.root).read_bytes(), first)

    def test_missing_input_preserves_existing_output(self):
        output = self.dist / B.OUTPUT_NAME
        output.write_bytes(b"bestehende Ausgabe")
        (self.dist / "alle-testakten.zip").unlink()
        with self.assertRaises(FileNotFoundError):
            B.build(self.dist, self.root)
        self.assertEqual(output.read_bytes(), b"bestehende Ausgabe")
        self.assertFalse(output.with_name(f".{output.name}.tmp").exists())

    def test_unknown_content_is_not_silently_omitted(self):
        self.members["alle-skills-markdown.zip"]["zusatz.md"] = "ein neuer eigenständiger Inhalt".encode("utf-8")
        self.write_bundle("alle-skills-markdown.zip")
        with self.assertRaisesRegex(ValueError, "unerwarteter Inhalt"):
            B.build(self.dist, self.root)

    def test_duplicate_output_path_is_rejected(self):
        self.members["alle-pluginlokalen-testakten.zip"]["testakte-zentral.zip"] = b"anderer Inhalt"
        self.write_bundle("alle-pluginlokalen-testakten.zip")
        with self.assertRaisesRegex(ValueError, "Doppeltes Einzelpaket"):
            B.build(self.dist, self.root)

    def test_duplicate_archive_member_is_rejected(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(self.dist / "alle-skills-markdown.zip", "a") as archive:
                archive.writestr("eins-skills-markdown.zip", b"doppelt")
        with self.assertRaisesRegex(ValueError, "doppelte ZIP-Einträge"):
            B.build(self.dist, self.root)

    def test_source_root_must_match_original_release(self):
        (self.root / ".claude-plugin/marketplace.json").write_bytes(b'{"plugins": []}')
        with self.assertRaisesRegex(ValueError, "Quellstand"):
            B.build(self.dist, self.root)

    def test_bundle_marketplace_and_plugin_inventory_must_match(self):
        self.members["alle-plugins-megazip.zip"]["marketplace.json"] = b"fremder Marketplace"
        self.write_bundle("alle-plugins-megazip.zip")
        with self.assertRaisesRegex(ValueError, "abweichende marketplace"):
            B.build(self.dist, self.root)
        self.members["alle-plugins-megazip.zip"]["marketplace.json"] = self.marketplace
        del self.members["alle-plugins-megazip.zip"]["zwei.zip"]
        self.write_bundle("alle-plugins-megazip.zip")
        with self.assertRaisesRegex(ValueError, "Marketplace stimmen nicht"):
            B.build(self.dist, self.root)

    def test_each_marketplace_plugin_keeps_its_skill_bundle(self):
        del self.members["alle-skills-markdown.zip"]["zwei-skills-markdown.zip"]
        self.write_bundle("alle-skills-markdown.zip")
        with self.assertRaisesRegex(ValueError, "Skill-Sammelarchiv und Marketplace"):
            B.build(self.dist, self.root)

    def test_notice_cannot_be_lost(self):
        self.members["alle-testakten.zip"]["README.txt"] = b"anderer Text"
        self.write_bundle("alle-testakten.zip")
        with self.assertRaisesRegex(ValueError, "abweichende README"):
            B.build(self.dist, self.root)

    def test_size_failure_keeps_previous_complete_package(self):
        output = self.dist / B.OUTPUT_NAME
        output.write_bytes(b"bestehende Ausgabe")
        with patch.object(assets, "MAX_RELEASE_ASSET_BYTES", 1):
            with self.assertRaisesRegex(ValueError, "Paketaufteilung korrigieren"):
                B.build(self.dist, self.root)
        self.assertEqual(output.read_bytes(), b"bestehende Ausgabe")
        self.assertFalse(output.with_name(f".{output.name}.tmp").exists())


class ReleaseSizeTests(unittest.TestCase):
    def test_actual_github_boundary_without_hashing_or_allocating_two_gib(self):
        with tempfile.TemporaryDirectory(prefix="release-size-") as tmp:
            dist = Path(tmp)
            large = dist / "zu-gross.zip"
            for size, valid in ((2 ** 31 - 1, True), (2 ** 31, False), (2 ** 31 + 1, False)):
                with large.open("wb") as handle:
                    handle.truncate(size)  # Sparse-Datei: keine 2 GiB schreiben/lesen.
                if valid:
                    assets.check_asset_size(large)
                else:
                    with self.assertRaisesRegex(ValueError, "kleiner.*2 GiB"):
                        assets.check_asset_size(large)
            checksums = dist / "checksums-sha256.txt"
            checksums.write_text("0" * 64 + "  zu-gross.zip\n", encoding="utf-8")
            previous = checksums.read_bytes()
            with patch.object(assets, "sha256_file", side_effect=AssertionError("Größenprüfung muss vor Hashing erfolgen")):
                for action in (assets.release_assets, assets.write_checksums, assets.expected_asset_metadata):
                    with self.assertRaisesRegex(ValueError, "zu-gross.zip"):
                        action(dist)
            self.assertEqual(checksums.read_bytes(), previous)
            self.assertFalse((dist / ".checksums-sha256.txt.tmp").exists())


if __name__ == "__main__":
    unittest.main()
