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

    def prepare_routed_build(self, plugin_routes, version=R.VERSION):
        manifest = self.plugin / ".claude-plugin/plugin.json"
        manifest.parent.mkdir()
        manifest.write_text(json.dumps({"name": "example", "version": version,
                                        "description": "Prüft einen Vorgang."}))
        market = self.root / ".claude-plugin/marketplace.json"
        market.parent.mkdir()
        market.write_text(json.dumps({"version": R.VERSION, "plugins": [
            {"name": "example", "version": version, "source": "./example"}]}))
        routes = self.root / "scripts/scoped-release-assets.json"
        routes.parent.mkdir()
        routes.write_text(json.dumps({"schema_version": 1, "assets": {
            R.WEBSITE: R.TAG, **plugin_routes}}))
        portable = self.root / "grundstuecksrecherche/app/portable.py"
        portable.parent.mkdir(parents=True)
        portable.write_text(
            "import sys, zipfile\n"
            "with zipfile.ZipFile(sys.argv[1], 'x') as archive:\n"
            "    archive.writestr('index.html', '<html></html>')\n"
            "    archive.writestr('portable-bundle.js', 'window.PORTABLE_BUNDLE={\"case\":null};')\n")
        subprocess.run(["git", "init", "--quiet"], cwd=self.root, check=True, timeout=30)
        subprocess.run(["git", "add", "example"], cwd=self.root, check=True, timeout=30)

    def build_routed_fixture(self):
        check_output = subprocess.check_output

        def output(command, **kwargs):
            if command == ["git", "rev-parse", "HEAD"]:
                return "0" * 40 + "\n"
            return check_output(command, **kwargs)

        dist = self.root / "dist"
        with patch.object(R, "PLUGINS", ("example",)), \
             patch.object(R.subprocess, "check_output", side_effect=output), \
             contextlib.redirect_stdout(io.StringIO()):
            R.build(dist, root=self.root)
        return dist, json.loads((dist / "quellenabgleich.json").read_text())

    def test_same_version_other_component_route_is_built_and_reported(self):
        tag = f"ki-verordnung-v{R.VERSION}"
        self.prepare_routed_build({"example.zip": tag})
        dist, report = self.build_routed_fixture()
        self.assertTrue((dist / "example.zip").is_file())
        self.assertEqual(report["tag"], R.TAG)
        self.assertEqual(report["plugins"]["example"]["route"],
                         R.scoped_asset_url("example.zip", root=self.root))
        self.assertTrue(report["plugins"]["example"]["route"].endswith(f"/{tag}/example.zip"))

    def test_newer_other_component_route_uses_actual_plugin_version(self):
        version = "445.35.2"
        self.prepare_routed_build({"example.zip": f"ki-verordnung-v{version}"}, version=version)
        dist, report = self.build_routed_fixture()
        self.assertEqual(report["tag"], R.TAG)
        self.assertEqual(report["version"], R.VERSION)
        self.assertEqual(report["plugins"]["example"]["version"], version)
        self.assertEqual(report["plugins"]["example"]["route"],
                         R.scoped_asset_url("example.zip", root=self.root))
        with zipfile.ZipFile(dist / "example.zip") as archive:
            self.assertEqual(json.loads(archive.read(".claude-plugin/plugin.json"))["version"], version)

    def test_own_component_route_is_built_and_reported(self):
        self.prepare_routed_build({"example.zip": R.TAG})
        _, report = self.build_routed_fixture()
        self.assertEqual(report["plugins"]["example"]["version"], R.VERSION)
        self.assertEqual(report["plugins"]["example"]["route"],
                         R.scoped_asset_url("example.zip", root=self.root))

    def test_missing_wrong_version_or_invalid_component_route_is_rejected(self):
        self.prepare_routed_build({})
        route_file = self.root / "scripts/scoped-release-assets.json"
        for plugin_routes in ({}, {"other.zip": f"ki-verordnung-v{R.VERSION}"},
                              {"example.zip": "ki-verordnung-v0.0.0"},
                              {"example.zip": f"ki-verordnung-v{R.VERSION}0"},
                              {"example.zip": f"invalid/ki-verordnung-v{R.VERSION}"}):
            with self.subTest(routes=plugin_routes):
                route_file.write_text(json.dumps({"schema_version": 1, "assets": {
                    R.WEBSITE: R.TAG, **plugin_routes}}))
                with self.assertRaises(ValueError):
                    self.build_routed_fixture()
                self.assertFalse((self.root / "dist/example.zip").exists())

    def test_newer_plugin_requires_matching_foreign_component_route(self):
        version = "445.35.2"
        self.prepare_routed_build({}, version=version)
        route_file = self.root / "scripts/scoped-release-assets.json"
        for plugin_routes in ({}, {"example.zip": f"ki-verordnung-v{R.VERSION}"},
                              {"example.zip": f"ki-verordnung-v{version}0"},
                              {"example.zip": f"kompatibilitaet-v{version}"}):
            with self.subTest(routes=plugin_routes):
                route_file.write_text(json.dumps({"schema_version": 1, "assets": {
                    R.WEBSITE: R.TAG, **plugin_routes}}))
                with self.assertRaises(ValueError):
                    self.build_routed_fixture()
                self.assertFalse((self.root / "dist/example.zip").exists())

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
