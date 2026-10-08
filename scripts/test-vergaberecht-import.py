#!/usr/bin/env python3
"""Prüft Integration, Installationsgrenzen und veröffentlichte Paketverweise."""

import argparse
import json
from pathlib import Path
import re
import unittest
import zipfile

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "vergaberecht-werkstatt"
META = json.loads((COMPONENT / "source-import.json").read_text())
DIST = None


class ImportTests(unittest.TestCase):
    def test_registered_roles(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = {p["name"]: p for p in marketplace["plugins"]}
        total = 0
        for name in META["plugins"]:
            plugin = json.loads((COMPONENT / name / ".claude-plugin/plugin.json").read_text())
            self.assertEqual(entries[name]["source"], f"./vergaberecht-werkstatt/{name}")
            self.assertEqual(plugin["version"], marketplace["version"])
            self.assertEqual(plugin["description"], entries[name]["description"])
            total += len(list((COMPONENT / name / "skills").glob("*/SKILL.md")))
        self.assertEqual(total, 255)

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
