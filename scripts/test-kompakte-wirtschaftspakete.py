#!/usr/bin/env python3
"""Prüft die beiden kompakten Praxispakete und ihre getrennten Downloads."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from zipfile import ZipFile

import yaml

from quality_lab import load, marketplace, validate_profile
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_zip_common import working_dump_flat_pairs


ROOT = Path(__file__).resolve().parent.parent
PACKAGES = {
    "vertragserstellung": (
        "vertrag-vom-auftrag-bis-zur-endfassung-erstellen",
        {
            "corporate-contract-law-rahmenlieferung-sensorik-aachen",
            "corporate-contract-law-projektvertrag-automation-augsburg",
            "vertragserstellung-wartungsvertrag-druckerei-kassel",
        },
    ),
    "wirtschaftsanwalt": (
        "unternehmensmandat-bis-zum-dokument-bearbeiten",
        {
            "anwaltschaft-lieferstreit-kaffeeroesterei-leipzig",
            "anwaltschaft-dienstleister-datenzugang-dortmund",
            "wirtschaftsanwalt-gesellschafterkonflikt-handwerk-hannover",
        },
    ),
}


def script_module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CompactPracticeTests(unittest.TestCase):
    def test_exact_ten_skills_and_executable_focus(self):
        entries = marketplace()
        for name, (main, _) in PACKAGES.items():
            with self.subTest(plugin=name):
                directory = entries[name]
                skills = sorted((directory / "skills").glob("*/SKILL.md"))
                self.assertEqual(len(skills), 10)
                profile = load(ROOT / "quality/evals" / f"{name}.json")
                validate_profile(profile, name, directory)
                self.assertEqual(profile["selection"]["target_skill"], main)
                self.assertEqual(profile["cases"][0]["target_skill"], main)
                self.assertEqual({case["target_skill"] for case in profile["cases"]}, {p.parent.name for p in skills})
                for path in skills:
                    text = path.read_text()
                    front = yaml.safe_load(text.split("---", 2)[1])
                    self.assertEqual(set(front), {"name", "description"})
                    self.assertEqual(front["name"], path.parent.name)
                    self.assertGreaterEqual(len(front["description"]), 80)
                    self.assertLessEqual(len(front["description"]), 1024)
                    self.assertRegex(text, r"(?m)^# 1\. [^\n]+$")
                    self.assertIn("zitierweise.md", text)
                self.assertGreater((directory / "skills" / main / "SKILL.md").stat().st_size, 2500)

    def test_standalone_prompts_are_visible_and_protected(self):
        protected = set((ROOT / "scripts/handkuratierte-prompts.txt").read_text().splitlines())
        root_readme = (ROOT / "README.md").read_text()
        for name in PACKAGES:
            self.assertIn(name, protected)
            readme = (ROOT / name / "README.md").read_text()
            self.assertIn("Alle zehn Skills sind im Plugin unmittelbar enthalten.", readme)
            for spelling in ("Geschaefte", "Nachtraege", "Liquiditaetsfragen", "Geschaeftsentscheidungen", "ausfuehrende"):
                self.assertNotIn(spelling, readme)
            for kind in ("werkstatt", "schnellstart", "hauptproblem"):
                relative = f"{name}/{name}-{kind}.md"
                raw = (ROOT / relative).read_bytes()
                self.assertGreater(len(raw), 2500)
                self.assertLessEqual(len(raw), 128 * 1024 if kind == "werkstatt" else 7500)
                self.assertLessEqual(len(raw.decode()), 128 * 1024 if kind == "werkstatt" else 7500)
                self.assertIn("download.html?path=" + relative, readme)
                self.assertIn("download.html?path=" + relative, root_readme)
                self.assertNotRegex(raw.decode(), r"\[[^\]]+\]\(\)")

    def test_previous_packages_and_prompts_remain(self):
        for name, expected in (("anwaltschaft-generell", 10), ("corporate-contract-law", 20)):
            self.assertEqual(len(list((ROOT / name / "skills").glob("*/SKILL.md"))), expected)
            for kind in ("werkstatt", "schnellstart", "hauptproblem"):
                self.assertTrue((ROOT / name / f"{name}-{kind}.md").is_file())

    def test_exact_three_assigned_cases_and_native_sources(self):
        injector = script_module("inject-direkt-loslegen-section")
        entries = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"]
        mapping = injector.discover_testakten_mapping(entries)
        for name, (_, cases) in PACKAGES.items():
            self.assertEqual(set(mapping[name]), cases)
            for slug in cases:
                directory = ROOT / "testakten" / slug
                sources = working_dump_flat_pairs(directory, include_gesamt_pdf=False)
                self.assertGreaterEqual(len(sources), 22)
                suffixes = {path.suffix.lower() for path, _ in sources}
                self.assertTrue({".docx", ".eml", ".xlsx", ".csv", ".png"} <= suffixes)
                if slug.startswith(name + "-"):
                    self.assertIn(".pdf", suffixes)
                self.assertNotIn(".md", suffixes)
                self.assertTrue((directory / "gesamt-pdf" / f"{slug}_gesamt.pdf").is_file())

    def test_original_format_archives_are_flat_complete_and_without_answers(self):
        builder = script_module("build-testakten-release-zips")
        new_cases = [next(slug for slug in cases if slug.startswith(name + "-")) for name, (_, cases) in PACKAGES.items()]
        with tempfile.TemporaryDirectory(prefix="kompakte-akten-") as temporary:
            for slug in new_cases:
                directory = ROOT / "testakten" / slug
                archive, _ = builder.build_single(directory, Path(temporary))
                expected = dict((name, path) for path, name in working_dump_flat_pairs(directory, include_gesamt_pdf=True))
                with ZipFile(archive) as bundle:
                    self.assertEqual(set(bundle.namelist()), set(expected) | {NOTICE_FILENAME})
                    self.assertTrue(all("/" not in name for name in bundle.namelist()))
                    self.assertEqual(bundle.read(NOTICE_FILENAME), NOTICE_BYTES)
                    self.assertIsNone(bundle.testzip())
                    for name, path in expected.items():
                        self.assertNotIn(path.suffix.lower(), {".md", ".yaml"})
                        self.assertEqual(bundle.read(name), path.read_bytes())


if __name__ == "__main__":
    unittest.main()
