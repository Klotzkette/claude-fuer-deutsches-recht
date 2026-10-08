#!/usr/bin/env python3
"""Regression checks for the complete four-asset Arbeitszeugnis release."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile


SPEC = importlib.util.spec_from_file_location(
    "zeugnis_release", Path(__file__).with_name("build-arbeitszeugnispruefer-release.py")
)
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


class ReleaseAssets(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="zeugnis-release-test-")
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        self.plugin = root / BUILDER.NAME
        self.destination = root / "release"
        self.destination.mkdir()
        (self.plugin / ".claude-plugin").mkdir(parents=True)
        (self.plugin / "references").mkdir()
        (self.plugin / ".claude-plugin/plugin.json").write_text(json.dumps({
            "name": BUILDER.NAME, "version": "1.2.3", "description": "Test fixture"
        }), encoding="utf-8")
        (self.plugin / "references/arbeitszeugnis-handbuch.md").write_text(
            "# Vollständige Testreferenz\n", encoding="utf-8"
        )
        for name in BUILDER.PROMPT_ASSETS:
            (self.plugin / name).write_text(f"# Aktueller Prompt {name}\n", encoding="utf-8")
            shutil.copyfile(self.plugin / name, self.destination / name)
        plugin_patch = patch.object(BUILDER, "PLUGIN", self.plugin)
        plugin_patch.start()
        self.addCleanup(plugin_patch.stop)
        with zipfile.ZipFile(self.destination / f"{BUILDER.NAME}.zip", "w") as archive:
            for path in BUILDER.source_files():
                archive.write(path, path.relative_to(self.plugin).as_posix())
        self.write_checksums()

    def write_checksums(self):
        lines = [
            f"{hashlib.sha256((self.destination / name).read_bytes()).hexdigest()}  {name}\n"
            for name in sorted(BUILDER.PAYLOAD_ASSETS)
        ]
        (self.destination / BUILDER.CHECKSUM_ASSET).write_text("".join(lines), encoding="utf-8")

    def validate(self):
        BUILDER.validate_bundle(self.destination, "1.2.3")

    def test_valid_complete_package(self):
        self.assertIsNone(self.validate())
        self.assertEqual(len(list(self.destination.iterdir())), 4)

    def test_missing_prompt(self):
        for name in BUILDER.PROMPT_ASSETS:
            with self.subTest(name=name):
                path = self.destination / name
                original = path.read_bytes()
                path.unlink()
                with self.assertRaisesRegex(ValueError, "asset inventory differs"):
                    self.validate()
                path.write_bytes(original)

    def test_stale_prompt_even_with_updated_checksum(self):
        for name in BUILDER.PROMPT_ASSETS:
            with self.subTest(name=name):
                path = self.destination / name
                original = path.read_bytes()
                path.write_bytes(b"Stale prompt\n")
                self.write_checksums()
                with self.assertRaisesRegex(ValueError, "Prompt asset differs"):
                    self.validate()
                path.write_bytes(original)
                self.write_checksums()

    def test_missing_checksum_file(self):
        (self.destination / BUILDER.CHECKSUM_ASSET).unlink()
        with self.assertRaisesRegex(ValueError, "asset inventory differs"):
            self.validate()

    def test_incomplete_checksums(self):
        path = self.destination / BUILDER.CHECKSUM_ASSET
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        path.write_text("".join(lines[:-1]), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "checksum inventory is incomplete"):
            self.validate()

    def test_wrong_checksum(self):
        path = self.destination / BUILDER.CHECKSUM_ASSET
        content = path.read_text(encoding="utf-8")
        path.write_text("0" * 64 + content[64:], encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "checksum differs"):
            self.validate()

    def test_duplicate_checksum(self):
        path = self.destination / BUILDER.CHECKSUM_ASSET
        content = path.read_text(encoding="utf-8")
        path.write_text(content + content.splitlines()[0] + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate release checksum"):
            self.validate()

    def test_unexpected_checksum_entry(self):
        path = self.destination / BUILDER.CHECKSUM_ASSET
        content = path.read_text(encoding="utf-8")
        path.write_text(content + "0" * 64 + "  extra.md\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Unexpected.*checksum entry"):
            self.validate()

    def test_malformed_checksum(self):
        (self.destination / BUILDER.CHECKSUM_ASSET).write_text("not a checksum\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Malformed release checksum"):
            self.validate()

    def test_additional_asset(self):
        (self.destination / "extra.md").write_text("unexpected", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "asset inventory differs"):
            self.validate()

    def test_additional_directory(self):
        (self.destination / "extra").mkdir()
        with self.assertRaisesRegex(ValueError, "asset inventory differs"):
            self.validate()

    def test_build_outside_plugin(self):
        destination = self.plugin.parent / "fresh-release"
        with patch.object(sys, "argv", ["builder", str(destination)]), patch.object(
            BUILDER, "checked_manifest", return_value={"version": "1.2.3"}
        ):
            BUILDER.main()
        self.assertEqual({path.name for path in destination.iterdir()}, BUILDER.RELEASE_ASSETS)
        BUILDER.validate_bundle(destination, "1.2.3")

    def test_build_inside_plugin_rejected_before_writing(self):
        for destination in (self.plugin, self.plugin / "generated" / "nested"):
            with self.subTest(destination=destination), patch.object(
                sys, "argv", ["builder", str(destination)]
            ), patch.object(BUILDER, "checked_manifest") as manifest:
                with self.assertRaisesRegex(ValueError, "outside the plugin directory"):
                    BUILDER.main()
                manifest.assert_not_called()
                self.assertFalse((self.plugin / "generated").exists())
                self.assertFalse((self.plugin / f"{BUILDER.NAME}.zip").exists())

    def test_build_via_symlink_into_plugin_rejected(self):
        link = self.plugin.parent / "plugin-link"
        link.symlink_to(self.plugin, target_is_directory=True)
        with patch.object(sys, "argv", ["builder", str(link / "generated")]):
            with self.assertRaisesRegex(ValueError, "outside the plugin directory"):
                BUILDER.main()
        self.assertFalse((self.plugin / "generated").exists())


if __name__ == "__main__":
    unittest.main()
