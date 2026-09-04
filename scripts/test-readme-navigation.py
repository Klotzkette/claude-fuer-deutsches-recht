#!/usr/bin/env python3
"""Regressionen für Verzeichnisse, Downloadwege und Aktenhinweise."""

from __future__ import annotations

import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent


def load_script(filename: str):
    spec = importlib.util.spec_from_file_location(filename, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


NAV = load_script("validate-readme-navigation.py")
CASES = load_script("inject-gesamt-pdf-section.py")


class NavigationTests(unittest.TestCase):
    def test_curated_and_start_guides_use_checked_downloads(self):
        checked = set(NAV.user_facing_download_docs())
        for filename in ("PROMPTLISTE.md", "QUICKSTART.md", "INSTALLATION_EINFACH.md"):
            self.assertIn(ROOT / filename, checked)

    def test_shared_anchor_target_is_read_once(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "README.md").write_text(
                "# Start\n\n[A](guide.md#überblick) · [B](guide.md#überblick-1)\n",
                encoding="utf-8",
            )
            (root / "guide.md").write_text(
                "# Überblick\n\n## Überblick\n", encoding="utf-8"
            )
            with patch.object(NAV, "REPO", root), patch.object(
                NAV, "heading_anchors", wraps=NAV.heading_anchors
            ) as read_anchors:
                errors = []
                self.assertEqual(NAV.validate_markdown_links(errors), (2, 2))
                self.assertEqual(errors, [])
                self.assertEqual(read_anchors.call_count, 1)

    def test_case_format_count_matches_available_downloads(self):
        two = CASES.section_block("akte", "gesamt.pdf", False)
        three = CASES.section_block("akte", "gesamt.pdf", True)
        self.assertIn("zwei Formaten", two)
        self.assertNotIn("Einzel-PDF-ZIP", two)
        self.assertIn("drei Formaten", three)
        self.assertIn("Einzel-PDF-ZIP", three)
        self.assertIn("English:", three)
        self.assertIn("zuletzt veröffentlichten Release", three)

    def test_curated_inventory_and_category_counts(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        plugins = {entry["name"]: entry["source"].removeprefix("./") for entry in market["plugins"]}
        text = (ROOT / "PROMPTLISTE.md").read_text(encoding="utf-8")
        sections = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
        categories = {}
        listed = []
        for heading, body in zip(sections[1::2], sections[2::2]):
            entries = re.findall(r"^- \[([a-z0-9-]+)\]\((https://[^)]+/tree/main/[^)]+)\):", body, re.MULTILINE)
            if not entries:
                continue
            names = [name for name, _ in entries]
            self.assertEqual(names, sorted(names), heading)
            categories[heading] = len(names)
            for name, url in entries:
                self.assertIn(name, plugins)
                self.assertTrue(url.endswith("/tree/main/" + plugins[name]), name)
            listed.extend(names)
        self.assertEqual(list(categories), sorted(categories, key=str.casefold))
        self.assertEqual(len(listed), len(set(listed)))
        counts = re.findall(r"^\| \[([^]]+)\]\(#[^)]+\) \| (\d+) \|$", text, re.MULTILINE)
        self.assertEqual({title: int(count) for title, count in counts}, categories)
        self.assertIn(f"{len(listed)} kuratierte Plugins in {len(categories)} Kategorien", text)
        self.assertIn(f"insgesamt {len(plugins)} Marketplace-Plugins", text)

    def test_no_obsolete_quickstart_skill_in_plugin_readmes(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        for plugin in market["plugins"]:
            text = (ROOT / plugin["source"] / "README.md").read_text(encoding="utf-8")
            self.assertNotIn("inklusive Schnellstart-Skill", text, plugin["name"])


if __name__ == "__main__":
    unittest.main()
