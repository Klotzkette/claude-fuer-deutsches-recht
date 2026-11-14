#!/usr/bin/env python3
"""Prüft Integration, Installationsgrenzen und veröffentlichte Paketverweise."""

import argparse
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest
from tempfile import TemporaryDirectory
import zipfile

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from release_routing import validate_plugin_version
from skill_sources import active_owner, original_skill_sources, registry

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "vergaberecht-werkstatt"
META = json.loads((COMPONENT / "source-import.json").read_text())
DIST = None


class ImportTests(unittest.TestCase):
    def test_review_guard_rejects_changed_or_unreviewed_prompt(self):
        spec = importlib.util.spec_from_file_location(
            "nested_public_release", COMPONENT / "scripts/public_release.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        name = "vergabestelle-behoerden"
        original = COMPONENT / name / f"{name}-schnellstart.md"
        review = json.loads((ROOT / "quality/evals" / f"{name}.json").read_text())["mini_review"]
        with TemporaryDirectory() as folder:
            target = Path(folder) / "prompt.md"
            target.write_bytes(original.read_bytes())
            self.assertEqual(module.reviewed_prompt(target, review), original.read_text())
            with self.assertRaises(ValueError):
                module.reviewed_prompt(target, None)
            target.write_bytes(target.read_bytes() + b"\n")
            with self.assertRaises(ValueError):
                module.reviewed_prompt(target, review)

    def test_role_prompt_sources_remain_synchronized(self):
        result = subprocess.run(
            [sys.executable, str(COMPONENT / "scripts/sync-public-entrypoints.py"), "--check"],
            cwd=COMPONENT, capture_output=True, text=True, timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_public_integration_accepts_reviewed_role_prompts(self):
        result = subprocess.run(
            [sys.executable, str(COMPONENT / "scripts/validate-public-integration.py")],
            cwd=COMPONENT, capture_output=True, text=True, timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_registered_roles(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = {p["name"]: p for p in marketplace["plugins"]}
        total_modules = 0
        total_active = 0
        original_counts = {'vergabestelle-behoerden': 122, 'bieter-unternehmen': 113,
                           'konkurrenten-rechtsschutz': 20}
        registered = {(ROOT / p['source']).resolve(): p for p in registry()}
        for name in META["plugins"]:
            plugin = json.loads((COMPONENT / name / ".claude-plugin/plugin.json").read_text())
            self.assertEqual(entries[name]["source"], f"./vergaberecht-werkstatt/{name}")
            self.assertEqual(plugin["version"], entries[name]["version"])
            validate_plugin_version(entries[name], marketplace["version"], root=ROOT)
            self.assertEqual(plugin["description"], entries[name]["description"])
            directory = COMPONENT / name
            active = {p.parent.name for p in (directory / 'skills').glob('*/SKILL.md')}
            modules = original_skill_sources(directory)
            self.assertEqual(len(modules), original_counts[name])
            self.assertLessEqual(len(active), 20)
            self.assertGreater(len(active), 0)
            if record := registered.get(directory.resolve()):
                self.assertEqual(active, set(record['keep']) | {r['slug'] for r in record['routes']})
            else:
                self.assertEqual(active, {p.parent.name for p in modules})
            for source in modules:
                self.assertTrue(source.is_file(), source)
                self.assertIn(active_owner(directory, source.parent.name), active)
            total_modules += len(modules)
            total_active += len(active)
        self.assertEqual(total_modules, 255)
        self.assertEqual(total_active, 36)

    def test_standalones(self):
        for name in META["plugins"]:
            for kind in ("werkstatt", "schnellstart"):
                path = COMPONENT / name / f"{name}-{kind}.md"
                self.assertTrue(path.is_file(), path)
                if kind == "schnellstart":
                    self.assertLessEqual(len(path.read_bytes()), 7500)
                self.assertGreater(len(path.read_text()), 1000)

    def test_no_nested_git_or_symlinks(self):
        for path in COMPONENT.rglob("*"):
            self.assertNotEqual(path.name, ".git")
            self.assertFalse(path.is_symlink(), path)

    def test_license_and_case_inventory(self):
        for name in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
            self.assertTrue((COMPONENT / name).is_file(), name)
        actual = {p.name for p in (COMPONENT / "testakten").iterdir()
                  if p.is_dir() and p.name not in {"megaprompts", "formatvorlagen-paradebeispiele"}}
        self.assertEqual(actual, set(META["cases"]))
        for slug in actual:
            self.assertTrue((COMPONENT / "testakten" / slug / "gesamt-pdf" / f"{slug}_gesamt.pdf").is_file())

    def test_component_tag_does_not_start_global_release(self):
        workflow = (ROOT / ".github/workflows/release-plugin-zips.yml").read_text()
        self.assertIn("- 'v[0-9]*'", workflow)
        self.assertNotIn("- 'v*'", workflow)

    def test_smoke_test_dependencies_installed_before_execution(self):
        workflow = (ROOT / ".github/workflows/vergaberecht-werkstatt.yml").read_text()
        dependency = "sudo apt-get install -y --no-install-recommends ripgrep"
        self.assertIn(dependency, workflow)
        self.assertLess(workflow.index(dependency), workflow.index("python scripts/run-smoke-tests.py --quick"))

    def test_readme_public_links(self):
        for path in COMPONENT.rglob("README.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("github.com/Klotzkette/vergaberecht-werkstatt", text, path)
            self.assertNotIn("raw.githubusercontent.com/Klotzkette/vergaberecht-werkstatt", text, path)
            self.assertNotRegex(text, r"\[[^\]]+\]\(\)")

    def test_plugin_archives(self):
        if DIST is None:
            self.skipTest("Paketprüfung erfolgt beim Release-Build mit --dist.")
        for name in META["plugins"]:
            with zipfile.ZipFile(DIST / f"{name}.zip") as archive:
                names = archive.namelist()
                self.assertIn(".claude-plugin/plugin.json", names)
                self.assertTrue(any(p.startswith("skills/") for p in names))
                self.assertFalse(any("testakten/" in p or p.endswith(("-werkstatt.md", "-schnellstart.md")) for p in names))
                self.assertIsNone(archive.testzip())
                directory = COMPONENT / name
                active = list((directory / 'skills').glob('*/SKILL.md'))
                modules = original_skill_sources(directory)
                source_names = set()
                for source in directory.rglob('*'):
                    if not source.is_file():
                        continue
                    relative = source.relative_to(directory)
                    if (source.name == '.DS_Store' or '__pycache__' in relative.parts
                            or source.suffix == '.pyc' or relative.as_posix() == 'CLAUDE.md'
                            or (len(relative.parts) == 1 and source.name.endswith(('-werkstatt.md', '-schnellstart.md')))
                            or source.name == 'llm-judge-eval.py'):
                        continue
                    source_names.add(relative.as_posix())
                self.assertEqual(set(names), source_names | {'LICENSE', 'LICENSE-APACHE', 'LICENSE-MIT', 'NOTICE'})
                self.assertLessEqual(len(active), 20)
                self.assertEqual({n for n in names if n.startswith('skills/') and n.endswith('/SKILL.md')},
                                 {p.relative_to(directory).as_posix() for p in active})
                for source in set(active) | set(modules):
                    self.assertEqual(archive.read(source.relative_to(directory).as_posix()), source.read_bytes())
                for member in names:
                    if member.endswith('/'):
                        continue
                    source = (COMPONENT if member in {'LICENSE', 'LICENSE-APACHE', 'LICENSE-MIT', 'NOTICE'} else directory) / member
                    self.assertTrue(source.is_file(), member)
                    self.assertEqual(archive.read(member), source.read_bytes(), member)
            with zipfile.ZipFile(DIST / f'{name}-skills-markdown.zip') as archive:
                expected = set(active) | set(modules)
                expected_names = {p.relative_to(COMPONENT).as_posix() for p in expected}
                actual_names = {n for n in archive.namelist() if '/skills/' in n}
                self.assertEqual(actual_names, expected_names)
                for source in expected:
                    self.assertEqual(archive.read(source.relative_to(COMPONENT).as_posix()), source.read_bytes())

    def test_flat_case_archives(self):
        if DIST is None:
            self.skipTest("Paketprüfung erfolgt beim Release-Build mit --dist.")
        for slug in META["cases"]:
            for tail in (".zip", "-einzelpdfs.zip"):
                with zipfile.ZipFile(DIST / f"testakte-{slug}{tail}") as archive:
                    names = archive.namelist()
                    self.assertEqual(names[0], NOTICE_FILENAME)
                    self.assertTrue(archive.read(NOTICE_FILENAME).startswith(NOTICE_BYTES))
                    self.assertEqual(len(names), len({n.casefold() for n in names}))
                    self.assertTrue(all("/" not in n and "\\" not in n for n in names))
                    self.assertFalse(any(n.lower().endswith((".md", ".yaml", ".yml")) for n in names))
                    self.assertGreater(len(names), 2)
                    if tail == "-einzelpdfs.zip":
                        self.assertTrue(all(n == NOTICE_FILENAME or n.endswith(".pdf") for n in names))
                    self.assertIsNone(archive.testzip())

    def test_linked_assets_built(self):
        if DIST is None:
            self.skipTest("Paketprüfung erfolgt beim Release-Build mit --dist.")
        prefix = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/" + META["release"] + "/"
        for path in COMPONENT.rglob("README.md"):
            for name in re.findall(re.escape(prefix) + r"([^\s\)\"<>]+)", path.read_text()):
                if name == "checksums-sha256.txt":
                    continue
                self.assertTrue((DIST / name).is_file(), f"{path}: {name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path)
    args, rest = parser.parse_known_args()
    DIST = args.dist
    unittest.main(argv=[__file__, *rest])
