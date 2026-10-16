#!/usr/bin/env python3
"""Strukturelle Einstiegsregressionen, keine juristische oder sprachliche Zertifizierung."""

import importlib.util
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "opening_inventory", ROOT / "scripts/audit-prompt-profile-routing.py"
)
INVENTORY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INVENTORY)


def published_prompts(root=ROOT):
    plugins = json.loads((root / ".claude-plugin/marketplace.json").read_text())["plugins"]
    for plugin in plugins:
        for kind, path in INVENTORY.expected_prompt_files(
            plugin["name"], root / plugin["source"]
        ).items():
            if kind == "schnellstart" or kind.startswith("werkstatt"):
                yield path


def opening_paragraph(text):
    """Ignore headings and comments, not tables or lists masquerading as prose."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if paragraph and not paragraph.startswith("#"):
            return paragraph
    return ""


class OpeningRegressionTests(unittest.TestCase):
    def test_inventory_includes_special_workshops(self):
        names = {path.name for path in published_prompts()}
        self.assertIn("betreuungsrecht-unterlagen-werkstatt.md", names)
        for phase in range(1, 10):
            self.assertIn(f"bauwirtschaft-hoai-{phase}-werkstatt.md", names)

    def test_every_opening_has_readable_prose_before_routing(self):
        for path in published_prompts():
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("# "))
                self.assertEqual(len(re.findall(r"^# ", text, re.M)), 1, "Genau ein Dokumenttitel")
                first = opening_paragraph(text)
                self.assertGreaterEqual(len(first), 80, "Kein erläuternder Fachabsatz")
                self.assertLessEqual(len(first), 1400, "Einstiegsabsatz in lesbare Einheiten teilen")
                self.assertFalse(first.startswith(("|", "```", "- ", "Autor:")))

    def test_title_does_not_duplicate_the_first_section_number(self):
        for path in published_prompts():
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                title = re.match(r"# (\d+)\. ", text)
                section = re.search(r"^## (\d+)\. ", text, re.M)
                if title and section:
                    self.assertNotEqual(title[1], section[1], "Dokumenttitel und Hauptabschnitt doppelt nummeriert")

    def test_tables_do_not_replace_the_subject_introduction(self):
        for path in published_prompts():
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                table = re.search(r"(?m)^\|", text)
                if table:
                    before = text[:table.start()]
                    prose = re.sub(r"(?m)^#{1,6} .*$", "", before).strip()
                    self.assertGreaterEqual(len(prose), 180, "Routing vor Erläuterung des Auftrags")

    def test_paragraph_reader_does_not_hide_a_leading_table(self):
        self.assertEqual(opening_paragraph("# Titel\n\n## 1. Auswahl\n\n| Feld | Weg |"), "| Feld | Weg |")

    def test_comment_and_heading_do_not_become_the_intro(self):
        self.assertEqual(opening_paragraph("# Titel\n\n<!-- Hinweis -->\n\n## 1. Auftrag\n\nFachtext."), "Fachtext.")


if __name__ == "__main__":
    unittest.main()
