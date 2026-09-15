#!/usr/bin/env python3
"""Prüft die neuen Schwerpunktpakete, nicht ihre juristische Freigabe."""

from pathlib import Path
import importlib.util
import re
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
from quality_lab import ROOT, load, marketplace, validate_profile


class SchwerpunktCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packages = {name: path for name, path in marketplace().items()
                        if name.startswith("fachanwalt-") or name in {"insolvenzrecht", "steuerrecht-anwalt-und-berater"}}

    def test_every_specialist_has_concrete_skill_and_prompt(self):
        self.assertTrue(self.packages)
        for name, directory in self.packages.items():
            with self.subTest(plugin=name):
                profile = load(ROOT / "quality/evals" / f"{name}.json")
                validate_profile(profile, name, directory)
                target = profile["cases"][0]["target_skill"]
                self.assertEqual(profile["selection"]["target_skill"], target)
                skill = directory / "skills" / target / "SKILL.md"
                self.assertGreater(len(skill.read_bytes()), 2500)
                prompt = directory / f"{name}-hauptproblem.md"
                raw = prompt.read_bytes()
                self.assertGreater(len(raw), 2500)
                self.assertLessEqual(len(raw), 7500)
                self.assertTrue(raw.decode("utf-8").startswith("# "))
                self.assertGreaterEqual(len(profile["sources"]), 1)

    def test_new_skill_relative_dependencies_stay_in_plugin(self):
        parser = MarkdownIt()
        for name, directory in self.packages.items():
            profile = load(ROOT / "quality/evals" / f"{name}.json")
            skill = directory / "skills" / profile["cases"][0]["target_skill"] / "SKILL.md"
            for token in parser.parse(skill.read_text(encoding="utf-8")):
                for child in token.children or []:
                    if child.type != "link_open":
                        continue
                    destination = urlsplit(child.attrGet("href"))
                    if destination.scheme or not destination.path:
                        continue
                    with self.subTest(plugin=name, link=destination.path):
                        path = (skill.parent / unquote(destination.path)).resolve()
                        self.assertTrue(path.is_relative_to(directory.resolve()))
                        self.assertTrue(path.exists())

    def test_local_citation_reference_is_current(self):
        canonical = (ROOT / "references/zitierweise.md").read_bytes()
        for name, directory in self.packages.items():
            with self.subTest(plugin=name):
                self.assertEqual((directory / "references/zitierweise.md").read_bytes(), canonical)

    def test_download_is_visible_in_each_readme(self):
        for name, directory in self.packages.items():
            with self.subTest(plugin=name):
                text = (directory / "README.md").read_text(encoding="utf-8")
                self.assertRegex(text, rf'<a href="[^"]*{re.escape(name)}-hauptproblem\.md" download>')
                self.assertIn("| Schwerpunkt-Prompt (Hauptproblem) |", text)

    def test_markdown_bundle_contains_shared_reference_but_no_prompts(self):
        spec = importlib.util.spec_from_file_location("bundles", ROOT / "scripts/build-skills-markdown-bundles.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temporary:
            for name, directory in self.packages.items():
                with self.subTest(plugin=name):
                    archive, _ = module.build_plugin_bundle(
                        {"name": name, "source": str(directory.relative_to(ROOT))}, ROOT, Path(temporary))
                    with ZipFile(archive) as bundle:
                        self.assertEqual(bundle.read(f"{name}/references/zitierweise.md"),
                                         (directory / "references/zitierweise.md").read_bytes())
                        self.assertFalse(any(p.endswith(("-werkstatt.md", "-schnellstart.md", "-hauptproblem.md"))
                                             for p in bundle.namelist()))

    def test_release_requires_exact_installable_focus_skill(self):
        spec = importlib.util.spec_from_file_location("release_zips", ROOT / "scripts/validate-release-zips.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temporary:
            for name, directory in self.packages.items():
                profile_path = ROOT / "quality/evals" / f"{name}.json"
                target = load(profile_path)["selection"]["target_skill"]
                relative = f"skills/{target}/SKILL.md"
                archive_path = Path(temporary) / f"{name}.zip"
                for state in ("correct", "missing", "changed"):
                    with self.subTest(plugin=name, state=state):
                        with ZipFile(archive_path, "w") as archive:
                            if state != "missing":
                                archive.writestr(relative, (directory / relative).read_bytes()
                                                 if state == "correct" else b"Abweichender Text")
                        if state == "correct":
                            module.validate_focus_skill(archive_path, directory, profile_path)
                        else:
                            with patch.object(module, "fail", side_effect=ValueError), self.assertRaises(ValueError):
                                module.validate_focus_skill(archive_path, directory, profile_path)


if __name__ == "__main__":
    unittest.main()
