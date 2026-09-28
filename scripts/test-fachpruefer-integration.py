#!/usr/bin/env python3
"""Prüft die eigenständig installierbaren Fachprüfer und ihre Aktenzuordnung."""

from __future__ import annotations

import json
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
from readme_decimal_headings import normalize_decimal_headings


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = {
    "enteignung-artikel-14": "enteignung-verkehrsflaeche-goettingen",
    "ki-verordnung-hochrisiko-pruefer": "ki-hochrisiko-bewerbungsauswahl-kassel",
    "ki-verordnung-transparenzpruefer": "ki-transparenz-kanzlei-kommunikation-mainz",
    "vergesellschaftung-artikel-15": "vergesellschaftung-energienetz-hessen",
}


def local_links(text: str):
    for token in MarkdownIt().parse(text):
        for child in token.children or []:
            if child.type not in {"link_open", "image"}:
                continue
            target = child.attrGet("href" if child.type == "link_open" else "src")
            if not target:
                continue
            parts = urlsplit(target)
            if not parts.scheme and not parts.netloc and parts.path:
                yield unquote(parts.path)


class FachprueferIntegrationTests(unittest.TestCase):
    def test_case_headings_remain_decimal_after_generation(self):
        for case in PACKAGES.values():
            with self.subTest(case=case):
                text = (ROOT / "testakten" / case / "README.md").read_text(encoding="utf-8")
                self.assertIn("<!-- decimal-headings -->", text)
                self.assertEqual(normalize_decimal_headings(text), text)
                tokens = MarkdownIt().parse(text)
                headings = [tokens[i + 1].content for i, token in enumerate(tokens) if token.type == "heading_open"]
                self.assertEqual(len(headings), 5)
                for title in headings:
                    self.assertRegex(title, r"^\d+(?:\.\d+)*\. ")
                self.assertEqual(headings[1], "1.1. Akte komplett herunterladen")

    def test_marketplace_metadata_matches_installable_manifest(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = {entry["name"]: entry for entry in marketplace["plugins"]}
        for name in PACKAGES:
            with self.subTest(plugin=name):
                manifest = json.loads((ROOT / name / ".claude-plugin/plugin.json").read_text())
                self.assertEqual(entries[name]["source"], f"./{name}")
                for field in ("name", "version", "description", "author"):
                    self.assertEqual(entries[name][field], manifest[field])
                self.assertEqual(manifest["version"], marketplace["version"])
                self.assertEqual(manifest["author"]["email"], "39582916+Klotzkette@users.noreply.github.com")

    def test_runtime_references_survive_installation_without_repository(self):
        for name in PACKAGES:
            directory = (ROOT / name).resolve()
            paths = sorted((directory / "skills").glob("*/SKILL.md"))
            self.assertGreaterEqual(len(paths), 1, name)
            self.assertLessEqual(len(paths), 10, name)
            paths += sorted((directory / "references").rglob("*.md"))
            for path in paths:
                with self.subTest(file=str(path.relative_to(ROOT))):
                    text = path.read_text(encoding="utf-8")
                    self.assertNotIn("§", text)
                    for target in local_links(text):
                        resolved = (path.parent / target).resolve()
                        self.assertTrue(resolved.is_relative_to(directory), f"Referenz verlässt Plugin: {target}")
                        self.assertTrue(resolved.exists(), f"Fehlende Referenz: {target}")

    def test_compact_prompts_and_case_navigation(self):
        central = (ROOT / "testakten/README.md").read_text(encoding="utf-8")
        for name, case in PACKAGES.items():
            with self.subTest(plugin=name):
                directory = ROOT / name
                mini = directory / f"{name}-schnellstart.md"
                self.assertTrue(mini.is_file())
                self.assertLessEqual(len(mini.read_bytes()), 7500)
                self.assertTrue((directory / f"{name}-werkstatt.md").is_file())
                readme = (directory / "README.md").read_text(encoding="utf-8")
                self.assertIn(case, readme)
                self.assertTrue((ROOT / "testakten" / case / "README.md").is_file())
                rows = [line for line in central.splitlines() if line.startswith("|") and f"`{case}/`" in line]
                self.assertEqual(len(rows), 1, case)
                self.assertIn(f"`{name}`", rows[0])


if __name__ == "__main__":
    unittest.main()
