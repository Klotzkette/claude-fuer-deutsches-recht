#!/usr/bin/env python3
"""Prüft Bauwirtschaft, neun Phasenpakete und getrennt ausgelieferte Akten."""

from __future__ import annotations

import importlib.util
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

import yaml

from akten_build_runtime import serif_font_path
from bauwirtschaft_hoai import PHASEN, werkstatt_path
from prompt_limits import MAX_WORKSHOP_BYTES
from readme_decimal_headings import normalize_decimal_headings
from quality_lab import load, marketplace, validate_profile
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_zip_common import working_dump_flat_pairs
from themen_profile import EXACT_PROFILE_KEYS


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = "bauwirtschaft"
PROJECT_CASES = {
    "bauwirtschaft-vergabeverfahren-feuerwehrhaus-northeim",
    "bauwirtschaft-baumanagement-werkhalle-warendorf",
    "bauwirtschaft-hoai-buergerhaus-einbeck",
    "bauwirtschaft-buchhaltung-bauunternehmen-bad-salzuflen",
}
PHASE_CASES = {case for _, _, _, case, _ in PHASEN}
CASES = PROJECT_CASES | PHASE_CASES


def script_module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BauwirtschaftTests(unittest.TestCase):
    def test_case_download_headings_stay_decimal_after_regeneration(self):
        injector = script_module("inject-gesamt-pdf-section")
        for slug in sorted(CASES):
            with self.subTest(case=slug), tempfile.TemporaryDirectory() as temporary:
                text = (ROOT / "testakten" / slug / "README.md").read_text()
                self.assertIn("<!-- decimal-headings -->", text)
                self.assertEqual(normalize_decimal_headings(text), text)
                for line in text.splitlines():
                    if line.startswith("#"):
                        self.assertRegex(line, r"^#{1,6} \d+(?:\.\d+)*\. \D")
                readme = Path(temporary) / "README.md"
                readme.write_text(text)
                injector.inject(readme, slug)
                generated = readme.read_text()
                self.assertRegex(generated, r"## 1\.\d+\. Akte komplett herunterladen")
                self.assertEqual(injector.inject(readme, slug), "unchanged")

    def test_navigation_matches_construction_work_instead_of_generic_law_groups(self):
        navigation = script_module("inject-skills-logic-navigation")
        slugs = navigation.skill_slugs(ROOT / PLUGIN)
        groups = navigation.PLUGIN_GROUPS[PLUGIN]
        self.assertEqual(len(groups), 7)
        assigned = [slug for _, items in groups for slug in items]
        self.assertCountEqual(assigned, slugs)
        block = navigation.build_block(slugs, PLUGIN)
        self.assertIn("Kaufmännische Steuerung", block)
        self.assertNotIn("Fallrouting", block)
        self.assertNotIn("Subsumtion", block)
        for slug in slugs:
            self.assertEqual(block.count(f"path={PLUGIN}/skills/{slug}/SKILL.md"), 1)
        with self.assertRaises(ValueError):
            navigation.build_block(slugs[:-1], PLUGIN)

    def test_pdf_fonts_support_configured_and_linux_paths(self):
        configured = Path("/custom/fonts/Times New Roman.ttf")
        linux = Path("/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf")
        linux_bold = linux.with_name("LiberationSerif-Bold.ttf")
        with patch.dict(os.environ, {"AKTEN_FONT_DIR": "/custom/fonts"}, clear=True):
            with patch.object(Path, "is_file", lambda path: path in {configured, linux, linux_bold}):
                self.assertEqual(serif_font_path(), configured)
                self.assertEqual(serif_font_path(bold=True), linux_bold)
        with patch.dict(os.environ, {}, clear=True):
            with patch.object(Path, "is_file", lambda path: path in {linux, linux_bold}):
                self.assertEqual(serif_font_path(), linux)
                self.assertEqual(serif_font_path(bold=True), linux_bold)
            with patch.object(Path, "is_file", return_value=False):
                with self.assertRaisesRegex(RuntimeError, "PDF-Schrift fehlt"):
                    serif_font_path()

    def test_twenty_nine_independent_skills_with_reviewed_routes(self):
        directory = marketplace()[PLUGIN]
        files = sorted((directory / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(files), 29)
        profile = load(ROOT / "quality/evals/bauwirtschaft.json")
        validate_profile(profile, PLUGIN, directory)
        names = {path.parent.name for path in files}
        self.assertEqual({case["target_skill"] for case in profile["cases"]}, names)
        self.assertIn(profile["selection"]["target_skill"], names)
        descriptions = []
        for path in files:
            with self.subTest(skill=path.parent.name):
                text = path.read_text(encoding="utf-8")
                front = yaml.safe_load(text.split("---", 2)[1])
                self.assertEqual(set(front), {"name", "description"})
                self.assertEqual(front["name"], path.parent.name)
                self.assertGreaterEqual(len(front["description"]), 80)
                self.assertLessEqual(len(front["description"]), 1024)
                self.assertLessEqual(len(text.splitlines()), 500)
                descriptions.append(front["description"])
        self.assertEqual(len(set(descriptions)), 29)
        self.assertEqual(EXACT_PROFILE_KEYS[PLUGIN], PLUGIN)
        reviews = profile["skill_reviews"]
        self.assertEqual(len(reviews), 29)
        self.assertEqual({entry["skill_path"] for entry in reviews}, {str(path.relative_to(ROOT)) for path in files})
        for entry in reviews:
            self.assertEqual(entry["sha256"], hashlib.sha256((ROOT / entry["skill_path"]).read_bytes()).hexdigest())
            self.assertEqual(entry["runtime_status"], "not_run")

    def test_downloads_are_separate_visible_and_protected(self):
        directory = ROOT / PLUGIN
        protected = set((ROOT / "scripts/handkuratierte-prompts.txt").read_text().splitlines())
        self.assertIn(PLUGIN, protected)
        for kind in ("werkstatt", "schnellstart", "hauptproblem"):
            path = directory / f"{PLUGIN}-{kind}.md"
            data = path.read_bytes()
            self.assertGreaterEqual(len(data), 40_000 if kind == "werkstatt" else 3500)
            self.assertLessEqual(len(data), MAX_WORKSHOP_BYTES if kind == "werkstatt" else 7500)
            self.assertLessEqual(len(data.decode("utf-8")), MAX_WORKSHOP_BYTES if kind == "werkstatt" else 7500)
            self.assertNotRegex(data.decode("utf-8"), r"\[[^\]]+\]\(\)")
            link = "download.html?path=" + path.relative_to(ROOT).as_posix()
            self.assertIn(link, (directory / "README.md").read_text())
            self.assertIn(link, (ROOT / "README.md").read_text())
        self.assertFalse((directory / "testakte").exists())
        self.assertFalse((directory / "testakten").exists())
        self.assertEqual(
            (directory / "references/zitierweise.md").read_bytes(),
            (ROOT / "references/zitierweise.md").read_bytes(),
        )

    def test_thirteen_distinct_cases_and_native_documents(self):
        injector = script_module("inject-direkt-loslegen-section")
        entries = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"]
        self.assertEqual(set(injector.discover_testakten_mapping(entries)[PLUGIN]), CASES)
        for slug in sorted(CASES):
            with self.subTest(case=slug):
                directory = ROOT / "testakten" / slug
                sources = working_dump_flat_pairs(directory, include_gesamt_pdf=False)
                minimum = 12 if slug in PHASE_CASES else (35 if "hoai-buergerhaus" in slug else 24)
                self.assertGreaterEqual(len(sources), minimum)
                suffixes = {path.suffix.lower() for path, _ in sources}
                self.assertTrue({".docx", ".eml", ".xlsx", ".csv", ".png", ".pdf"} <= suffixes)
                self.assertNotIn(".md", suffixes)
                self.assertGreaterEqual(sum(path.suffix.lower() == ".png" for path, _ in sources), 1 if slug in PHASE_CASES else 2)
                self.assertTrue((directory / "gesamt-pdf" / f"{slug}_gesamt.pdf").is_file())
                rubric = yaml.safe_load((directory / "rubric.yaml").read_text())
                self.assertEqual(rubric["plugin"], PLUGIN)

    def test_nine_phases_have_independent_workshops_skills_and_labelled_cases(self):
        self.assertEqual([phase for phase, *_ in PHASEN], list(range(1, 10)))
        self.assertEqual(len(PHASE_CASES), 9)
        audit = script_module("audit-prompt-profile-routing")
        registered = set(audit.expected_prompt_files(PLUGIN, ROOT / PLUGIN).values())
        self.assertEqual(len(registered), 11)
        self.assertEqual(registered, set((ROOT / PLUGIN).glob("*-werkstatt.md"))
                         | set((ROOT / PLUGIN).glob("*-schnellstart.md")))
        self.assertNotIn(ROOT / PLUGIN / "bauwirtschaft-hoai-10-werkstatt.md", registered)
        self.assertEqual(len(audit.expected_prompt_files("anderes-plugin", ROOT / "anderes-plugin")), 2)
        overview = (ROOT / "docs/bauwirtschaft-hoai-phasen.md").read_text()
        coverage = (ROOT / "docs/werkstatt-und-schnellstart-coverage.md").read_text()
        refiner = script_module("refine-speed-and-elegance")
        self.assertTrue(refiner.prompt_is_protected(ROOT / PLUGIN))
        profile = load(ROOT / "quality/evals/bauwirtschaft.json")
        reviews = profile["phase_workshop_reviews"]
        self.assertEqual([review["phase"] for review in reviews], list(range(1, 10)))
        sources = []
        for phase, _, skill, case, _ in PHASEN:
            with self.subTest(phase=phase):
                prompt = ROOT / werkstatt_path(phase)
                text = prompt.read_text()
                review = reviews[phase - 1]
                self.assertEqual(review["path"], werkstatt_path(phase))
                self.assertEqual(review["sha256"], hashlib.sha256(prompt.read_bytes()).hexdigest())
                self.assertEqual(review["runtime_status"], "not_run")
                self.assertGreaterEqual(len(text.encode()), 18_000)
                self.assertLessEqual(len(text.encode()), MAX_WORKSHOP_BYTES)
                self.assertIn("download.html?path=" + werkstatt_path(phase), overview)
                self.assertIn("download.html?path=" + werkstatt_path(phase), coverage)
                self.assertIn(skill, overview)
                self.assertIn(case + "/README.md", overview)
                self.assertIn(f"Leistungsphase {phase}", (ROOT / "testakten" / case / "README.md").read_text())
                self.assertIn("anlage_10", text)
                self.assertNotIn("§", text)
                self.assertTrue((ROOT / PLUGIN / "skills" / skill / "SKILL.md").is_file())
                self.assertNotRegex(text, r"\[[^\]]+\]\(\)")
                for line in text.splitlines():
                    if line.startswith("#"):
                        self.assertRegex(line, r"^#{1,6} \d+(?:\.\d+)*\.? ")
                sources.append(text)
        self.assertEqual(len(set(sources)), 9)
        references = (ROOT / PLUGIN / "README.md").read_text()
        self.assertIn("29 Skills", references)
        self.assertIn("bauwirtschaft-hoai-phasen.md", references)

    def test_installed_skills_do_not_depend_on_excluded_workshops(self):
        directory = ROOT / PLUGIN
        for folder in (directory / "skills", directory / "references"):
            for path in folder.rglob("*.md"):
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
                    parsed = urlsplit(target)
                    if parsed.scheme or not parsed.path or parsed.path.startswith("/"):
                        continue
                    with self.subTest(path=str(path.relative_to(ROOT)), target=target):
                        linked = (path.parent / unquote(parsed.path)).resolve()
                        self.assertTrue(linked.is_relative_to(directory))
                        self.assertTrue(linked.is_file())
                        self.assertFalse(linked.name.endswith(("-werkstatt.md", "-schnellstart.md", "-hauptproblem.md")))

    def test_original_archives_are_flat_complete_and_byte_exact(self):
        builder = script_module("build-testakten-release-zips")
        with tempfile.TemporaryDirectory(prefix="bauwirtschaft-zip-") as temporary:
            for slug in sorted(CASES):
                with self.subTest(case=slug):
                    directory = ROOT / "testakten" / slug
                    archive, _ = builder.build_single(directory, Path(temporary))
                    expected = {name: path for path, name in working_dump_flat_pairs(directory, include_gesamt_pdf=True)}
                    with ZipFile(archive) as bundle:
                        self.assertEqual(set(bundle.namelist()), set(expected) | {NOTICE_FILENAME})
                        self.assertTrue(all("/" not in name for name in bundle.namelist()))
                        self.assertEqual(bundle.read(NOTICE_FILENAME), NOTICE_BYTES)
                        self.assertIsNone(bundle.testzip())
                        for name, path in expected.items():
                            self.assertNotIn(path.suffix.lower(), {".md", ".yaml", ".json"})
                            self.assertEqual(bundle.read(name), path.read_bytes())


if __name__ == "__main__":
    unittest.main()
