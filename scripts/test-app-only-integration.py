#!/usr/bin/env python3
"""App-only-Integration ohne Erzeugung globaler Repository-Artefakte."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import prompt_profiles as publication
import quality_lab

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
SLUG = "grundstuecksrecherche"
ORDINARY = "anderes-plugin"


def module(stem):
    spec = importlib.util.spec_from_file_location(stem.replace("-", "_"), SCRIPTS / f"{stem}.py")
    loaded = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = loaded
    spec.loader.exec_module(loaded)
    return loaded


DIRECT = module("inject-direkt-loslegen-section")
INDEX = module("generate-skills-md")
GENERATOR = module("generate-werkstatt-und-schnellstart-prompts")
MEGA = module("generate-megaprompt")
COVERAGE = module("generate-werkstatt-und-schnellstart-coverage")
NAVIGATION = module("validate-readme-navigation")


class AppOnlyIntegration(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.plugin = self.root / SLUG
        for directory in (".claude-plugin", ".codex-plugin", "skills"):
            shutil.copytree(ROOT / SLUG / directory, self.plugin / directory)
        shutil.copy2(ROOT / SLUG / "README.md", self.plugin / "README.md")
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.entry = next(entry for entry in marketplace["plugins"] if entry["name"] == SLUG)
        ordinary = dict(self.entry, name=ORDINARY, source=f"./{ORDINARY}")
        self.marketplace = dict(marketplace, plugins=[ordinary, self.entry])
        self.market = self.root / ".claude-plugin/marketplace.json"
        self.write(self.market, json.dumps(self.marketplace))
        manifest = json.loads((self.plugin / ".claude-plugin/plugin.json").read_text())
        self.write(self.root / ORDINARY / ".claude-plugin/plugin.json", json.dumps(dict(manifest, name=ORDINARY)))
        self.write(self.root / ORDINARY / "skills/pruefen/SKILL.md",
                   "---\nname: pruefen\ndescription: Prüft ein gewöhnliches Plugin mit weiterhin erforderlichen Begleitprompts und allen bisherigen Dateiprüfungen.\n---\n# Prüfung\n")
        base = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="
        readme = ["# Prüfplugin", DIRECT.BEGIN, f"[Plugin]({DIRECT.RELEASE_BASE}/{ORDINARY}.zip)"]
        for kind in ("werkstatt", "schnellstart"):
            filename = f"{ORDINARY}-{kind}.md"
            self.write(self.root / ORDINARY / filename, "# Prüfung\n\n## 1. Auftrag\n\nPrüfen Sie die Unterlagen.\n")
            readme.append(f"[Download]({base}{ORDINARY}/{filename})")
        self.write(self.root / ORDINARY / "README.md", "\n".join(readme + [DIRECT.END]))
        self.write(self.root / ".github/workflows/release-plugin-zips.yml", "# testakte-*-einzelpdfs.zip\n")

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def validate(self, script="validate-marketplace-import.mjs"):
        return subprocess.run(["node", str(SCRIPTS / script)], cwd=self.root,
                              capture_output=True, text=True, timeout=30)

    def test_explicit_empty_profile_and_unchanged_defaults_match_javascript(self):
        self.assertEqual(publication.standalone_kinds(SLUG), ())
        self.assertTrue(publication.hand_curated(SLUG))
        for kind in (*publication.KINDS, "megaprompt"):
            self.assertFalse(publication.enabled(SLUG, kind))
            self.assertTrue(publication.enabled(ORDINARY, kind))
        script = """import {promptKinds,promptFormats,promptEnabled} from './scripts/prompt-profiles.mjs';
console.log(JSON.stringify(['grundstuecksrecherche','anderes-plugin'].map(s =>
  [promptKinds(s), promptFormats(s), ['werkstatt','schnellstart','hauptproblem','megaprompt'].map(k => promptEnabled(s,k))])));"""
        actual = json.loads(subprocess.check_output(["node", "--input-type=module", "-e", script], cwd=ROOT, text=True))
        expected = [[list(publication.standalone_kinds(slug)), list(publication.formats(slug)),
                     [publication.enabled(slug, kind) for kind in (*publication.KINDS, "megaprompt")]]
                    for slug in (SLUG, ORDINARY)]
        self.assertEqual(actual, expected)

    def test_empty_standalone_does_not_relax_other_profile_fields(self):
        profile = publication.PROFILES[SLUG]
        config = self.root / "profiles.json"
        for changes in ({}, {"standalone": ["werkstatt"]}):
            self.write(config, json.dumps({"schema_version": 1, "plugins": {SLUG: dict(profile, **changes)}}))
            self.assertIn(SLUG, publication.load_profiles(config))
        for changes in ({"formats": []}, {"formats": ["txt"]}, {"standalone": None},
                        {"standalone": ["unbekannt"]}, {"standalone": ["werkstatt", "werkstatt"]},
                        {"megaprompt": 0}, {"hand_curated": "true"}):
            with self.subTest(changes=changes):
                self.write(config, json.dumps({"schema_version": 1, "plugins": {SLUG: dict(profile, **changes)}}))
                with self.assertRaises(ValueError):
                    publication.load_profiles(config)

    def test_real_app_metadata_passes_both_validators_without_prompts(self):
        for validator in ("validate-marketplace-import.mjs", "audit-release-readiness.mjs"):
            with self.subTest(validator=validator):
                result = self.validate(validator)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_other_plugins_still_require_workshop_and_its_download(self):
        workshop = self.root / ORDINARY / f"{ORDINARY}-werkstatt.md"
        content = workshop.read_bytes()
        workshop.unlink()
        for validator in ("validate-marketplace-import.mjs", "audit-release-readiness.mjs"):
            result = self.validate(validator)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(f"{ORDINARY}: Werkstatt-Markdown fehlt", result.stderr)
            self.assertNotIn(f"{SLUG}: Werkstatt-Markdown fehlt", result.stderr)
        workshop.write_bytes(content)
        readme = self.root / ORDINARY / "README.md"
        self.write(readme, readme.read_text().replace(f"{ORDINARY}-werkstatt.md", "nicht-der-prompt.md"))
        for validator in ("validate-marketplace-import.mjs", "audit-release-readiness.mjs"):
            result = self.validate(validator)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(f"{ORDINARY}/README.md: Werkstatt-Direktdownload fehlt", result.stderr)

    def test_app_omission_does_not_bypass_manifest_skill_or_readme_checks(self):
        for relative, message in (("README.md", "README.md fehlt"),
                                  ("skills", "keine Skills gefunden"),
                                  (".claude-plugin/plugin.json", "JSON kann nicht gelesen werden")):
            with self.subTest(relative=relative):
                source = self.plugin / relative
                backup = self.root / "reserved"
                source.rename(backup)
                try:
                    result = self.validate()
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(message, result.stderr)
                finally:
                    backup.rename(source)

    def test_forbidden_prompt_derivatives_are_still_rejected(self):
        self.assertEqual(publication.validate_files(self.plugin, SLUG, self.root), [])
        for kind in publication.KINDS:
            for ext in publication.FORMATS:
                with self.subTest(kind=kind, ext=ext):
                    path = self.plugin / f"{SLUG}-{kind}.{ext}"
                    self.write(path, "Nicht vorgesehen")
                    self.assertTrue(publication.validate_files(self.plugin, SLUG, self.root))
                    result = self.validate()
                    self.assertIn("Prompt laut Profil nicht vorgesehen", result.stderr)
                    path.unlink()
        path = self.root / "testakten/megaprompts" / f"{SLUG}.md"
        self.write(path, "Nicht vorgesehen")
        self.assertTrue(publication.validate_files(self.plugin, SLUG, self.root))
        self.assertIn("Megaprompt laut Profil nicht vorgesehen", self.validate().stderr)

    def test_generators_skip_empty_profiles_even_without_curated_flag(self):
        before = {p.relative_to(self.plugin): p.read_bytes() for p in self.plugin.rglob("*") if p.is_file()}
        with patch.object(GENERATOR, "plugin_dirs", return_value=[self.plugin]), \
             patch.object(GENERATOR, "hand_curated", return_value=False), \
             patch.object(GENERATOR, "has_individual_review", side_effect=AssertionError("Kein Promptauftrag")), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(GENERATOR.main(), 0)
        self.assertIsNone(MEGA.build_megaprompt(self.plugin))
        publication.sync_text_copies(self.plugin, SLUG)
        after = {p.relative_to(self.plugin): p.read_bytes() for p in self.plugin.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        with patch.object(COVERAGE, "REPO", self.root):
            for kind in ("werkstatt", "schnellstart"):
                table = "\n".join(COVERAGE.prompt_table(self.marketplace["plugins"], kind))
                self.assertNotIn(f"`{SLUG}`", table)
                self.assertIn(f"`{ORDINARY}`", table)

    def test_curated_app_readme_is_preserved_byte_for_byte(self):
        readme = self.plugin / "README.md"
        before = readme.read_bytes()
        with patch.object(DIRECT, "REPO", self.root):
            for _ in range(2):
                self.assertEqual(DIRECT.inject(self.entry, [], 2), "UNCHANGED")
        self.assertEqual(before, readme.read_bytes())

    def test_curated_app_version_sync_changes_only_visible_version(self):
        readme = self.plugin / "README.md"
        before = readme.read_text()
        version = self.entry["version"]
        outdated = before.replace(f"**Version:** `{version}`", "**Version:** `1.0.0`")
        self.assertNotEqual(outdated, before)
        self.write(readme, outdated)
        with patch.object(DIRECT, "REPO", self.root):
            self.assertEqual(DIRECT.inject(self.entry, [], 2), "UPDATED")
            self.assertEqual(DIRECT.inject(self.entry, [], 2), "UNCHANGED")
        self.assertEqual(before, readme.read_text())

    def test_visible_version_forms_preserve_dates_and_other_numbers(self):
        text = "**Version:** `1.0.0`\nVersion 1.0.0 · Rechtsstand 06.10.2026\nDer Entwicklungsstand ist 06.10.2026, Version 1.0.0.\nHistorischer Hinweis auf Version 0.9.0.\n"
        self.assertEqual(DIRECT.sync_visible_version(text, "1.1.0"), text.replace("1.0.0", "1.1.0"))

    def test_missing_app_block_gets_app_only_fallback_idempotently(self):
        readme = self.plugin / "README.md"
        self.write(readme, "# Lokale App\n\nEigene Startanleitung.\n")
        with patch.object(DIRECT, "REPO", self.root):
            self.assertEqual(DIRECT.inject(self.entry, [], 2), "INSERTED")
            self.assertEqual(DIRECT.inject(self.entry, [], 2), "UNCHANGED")
        text = readme.read_text()
        self.assertIn("App verwenden", text)
        self.assertIn("Eigene Startanleitung.", text)
        for word in ("Werkstatt", "Schnellstart", "Testakten", "hauptproblem"):
            self.assertNotIn(word, text)

    def test_skill_indexes_do_not_offer_nonexistent_app_prompts(self):
        skills = [path.parent.name for path in (self.plugin / "skills").glob("*/SKILL.md")]
        with patch.object(INDEX, "REPO_ROOT", self.root):
            detail = INDEX.plugin_detail_page(SLUG, skills, self.marketplace["version"])
            table = INDEX.plugin_overview_table([(SLUG, skills), (ORDINARY, ["pruefen"])])
        for kind in publication.KINDS:
            self.assertNotIn(f"{SLUG}-{kind}", detail + table)
        self.assertIn(f"{ORDINARY}-werkstatt.md", table)
        self.assertIn(f"{ORDINARY}-schnellstart.md", table)
        self.assertNotIn("Testakten", detail)
        self.assertIn("App verwenden", detail)
        for skill in skills:
            self.assertIn(f"{SLUG}/skills/{skill}/SKILL.md", detail)

    def test_app_navigation_needs_no_testakte_but_keeps_other_links(self):
        self.write(self.market, json.dumps(dict(self.marketplace, plugins=[self.entry])))
        skills = [path.parent.name for path in (self.plugin / "skills").glob("*/SKILL.md")]
        with patch.object(INDEX, "REPO_ROOT", self.root):
            detail = INDEX.plugin_detail_page(SLUG, skills, self.marketplace["version"])
        self.write(self.root / f"skills-index/{SLUG}.md", detail)
        self.write(self.root / "ASSET_INDEX.md", f"[README]({SLUG}/README.md) [Skills](skills-index/{SLUG}.md)")
        with patch.object(NAVIGATION, "REPO", self.root), patch.object(NAVIGATION, "MARKETPLACE", self.market):
            errors = []
            NAVIGATION.validate_generated_navigation(errors)
            self.assertEqual(errors, [])
            readme = self.plugin / "README.md"
            self.write(readme, readme.read_text().replace("[Skill-Gesamtübersicht](../SKILLS.md)", ""))
            NAVIGATION.validate_generated_navigation(errors)
            self.assertTrue(any("Navigationsziel fehlt: ../SKILLS.md" in error for error in errors))

    def test_quality_catalog_does_not_require_a_disabled_prompt_review(self):
        profiles = {SLUG: {"cases": []}, ORDINARY: {"cases": [], "mini_review": {"verdict": "retained", "reason": "Prüfung bleibt."}}}
        text = quality_lab.catalog(profiles, self.root)
        self.assertIn("App- und Skill-Prüffälle", text)
        self.assertIn("Prüfung bleibt.", text)

    def test_app_quality_audit_keeps_profile_and_workflow_requirements(self):
        self.write(self.market, json.dumps(dict(self.marketplace, plugins=[self.entry])))
        path = self.root / f"quality/evals/{SLUG}.json"
        profile = json.loads((ROOT / f"quality/evals/{SLUG}.json").read_text())
        self.write(path, json.dumps(profile))
        profiles, errors = quality_lab.audit(self.root, require_editorial=True, require_workflow=True)
        self.assertEqual(errors, [])
        self.assertIn(SLUG, profiles)
        del profile["prompt_workflow_review"]
        self.write(path, json.dumps(profile))
        self.assertIn(f"{SLUG}: Fachbezogene Workflow-Prüfung fehlt",
                      quality_lab.audit(self.root, require_editorial=True, require_workflow=True)[1])
        path.unlink()
        self.assertIn(f"{SLUG}: Individuelles Prüfprofil fehlt",
                      quality_lab.audit(self.root, require_editorial=True, require_workflow=True)[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
