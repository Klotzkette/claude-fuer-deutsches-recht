"""Regressionen gegen alte Paketstände und unbeabsichtigte Installationsinhalte."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("compatibility", ROOT / "scripts/build-compatibility-release.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


class CompatibilityRelease(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.plugin = self.root / "example"
        self.skill = self.plugin / "skills/check/SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.skill.write_text("# Fachlicher Quellstand\n", encoding="utf-8")
        self.files = {"skills/check/SKILL.md": self.skill}
        self.archive = self.root / "example.zip"

    def test_deterministic_flat_zip(self):
        R.write_zip(self.archive, self.files)
        second = self.root / "second.zip"
        R.write_zip(second, self.files)
        self.assertEqual(self.archive.read_bytes(), second.read_bytes())
        self.assertEqual(set(R.verify_zip(self.archive, self.files)), set(self.files))
        R.CHECKS.validate_skill_sources(self.archive, self.plugin)

    def test_stale_skill_is_rejected_even_without_version_change(self):
        R.write_zip(self.archive, self.files)
        self.skill.write_text("# Geänderter Quellstand\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            R.verify_zip(self.archive, self.files)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            R.CHECKS.validate_skill_sources(self.archive, self.plugin)

    def test_missing_and_additional_skills_are_rejected(self):
        R.write_zip(self.archive, {})
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            R.CHECKS.validate_skill_sources(self.archive, self.plugin)
        self.archive.unlink()
        R.write_zip(self.archive, {**self.files, "skills/other/SKILL.md": self.skill})
        with self.assertRaises(ValueError):
            R.verify_zip(self.archive, self.files)

    def test_no_prompt_case_or_cache_payload(self):
        for name in ("example-werkstatt.md", "example-schnellstart.txt", "example-hauptproblem.md",
                     "CLAUDE.md", ".DS_Store", "testakte/akten.pdf", "testakten/akten.pdf",
                     "app/__pycache__/data.pyc", ".venv/lib/package.py", "node_modules/dependency.js"):
            self.assertFalse(R.packaged(name), name)
        for name in ("skills/check/SKILL.md", "app/static/vendor/leaflet.js", "references/quellen.md"):
            self.assertTrue(R.packaged(name), name)

    def test_output_directory_cannot_be_overwritten(self):
        R.write_zip(self.archive, self.files)
        with self.assertRaises(ValueError):
            R.build(self.root)

    def test_tracked_sources_include_parent_license_but_not_private_files(self):
        manifest = self.plugin / ".claude-plugin/plugin.json"
        manifest.parent.mkdir()
        manifest.write_text('{}')
        (self.root / "LICENSE").write_text("Lizenz des Pakets\n")
        subprocess.run(["git", "init", "--quiet"], cwd=self.root, check=True, timeout=30)
        subprocess.run(["git", "add", "LICENSE", "example"], cwd=self.root, check=True, timeout=30)
        (self.plugin / "privater-vorgang.json").write_text('{}')
        files = R.sources(self.root, self.plugin)
        self.assertEqual(files["LICENSE"], self.root / "LICENSE")
        self.assertNotIn("privater-vorgang.json", files)
        self.assertIn("skills/check/SKILL.md", files)

    def test_tracked_symlink_is_rejected(self):
        manifest = self.plugin / ".claude-plugin/plugin.json"
        manifest.parent.mkdir()
        manifest.write_text('{}')
        (self.plugin / "link").symlink_to(self.skill)
        subprocess.run(["git", "init", "--quiet"], cwd=self.root, check=True, timeout=30)
        subprocess.run(["git", "add", "example"], cwd=self.root, check=True, timeout=30)
        with self.assertRaises(ValueError):
            R.sources(self.root, self.plugin)

    def test_component_versions_used_instead_of_catalog_version(self):
        market = self.root / ".claude-plugin/marketplace.json"
        market.parent.mkdir()
        market.write_text(json.dumps({"version": "1.0.0", "plugins": [
            {"name": "example", "version": "1.0.1", "source": "./example"}]}))
        dist = self.root / "dist"
        dist.mkdir()
        (dist / "marketplace.json").write_bytes(market.read_bytes())
        with patch.object(sys, "argv", ["validate", str(dist), str(market)]), \
             patch.object(R.CHECKS, "validate_plugin_version") as pin, \
             patch.object(R.CHECKS, "validate_plugin_zip") as validate, \
             patch.object(R.CHECKS, "validate_skill_sources"), \
             patch.object(R.CHECKS, "validate_focus_skill"), contextlib.redirect_stdout(io.StringIO()):
            R.CHECKS.main()
        validate.assert_called_once_with(dist, "example", "1.0.1")
        self.assertEqual(pin.call_args.args[1], "1.0.0")

    def test_foreign_interface_field_is_rejected(self):
        manifest = self.plugin / ".claude-plugin/plugin.json"
        manifest.parent.mkdir()
        data = {"name": "example", "version": "1.0.0", "description": "Prüft einen Vorgang.",
                "interface": {"displayName": "Prüfung"}}
        manifest.write_text(json.dumps(data))
        market = self.root / ".claude-plugin/marketplace.json"
        market.parent.mkdir()
        market.write_text(json.dumps({"name": "examples", "version": "1.0.0", "plugins": [
            {"name": "example", "source": "./example", "version": "1.0.0"}]}))
        result = subprocess.run(["node", str(ROOT / "scripts/validate-plugin-structure.mjs")],
                                cwd=self.root, capture_output=True, text=True, timeout=30)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported manifest key interface", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
