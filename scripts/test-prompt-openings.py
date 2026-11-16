#!/usr/bin/env python3
"""Strukturelle Einstiegsregressionen, keine juristische oder sprachliche Zertifizierung."""

import importlib.util
import json
from pathlib import Path
import re
import unittest

from prompt_profiles import enabled


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "opening_inventory", ROOT / "scripts/audit-rechtsprechungs-metadaten.py"
)
INVENTORY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INVENTORY)


def published_prompts():
    _, workflows = INVENTORY.workshop_inventory(include_workflows=True)
    paths = {ROOT / record["path"] for record in workflows if record["kind"] == "Prompt"}
    plugins = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))["plugins"]
    for plugin in plugins:
        slug = plugin["name"]
        for kind in ("schnellstart", "hauptproblem"):
            path = ROOT / plugin["source"] / f"{slug}-{kind}.md"
            if enabled(slug, kind) and (kind == "schnellstart" or path.is_file()):
                paths.add(path)
    return sorted(paths)


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
        self.assertIn("playbook-pruefer-hauptproblem.md", names)
        self.assertIn("130-kongruente-deckung.md", names)
        self.assertIn("139-fristen-und-antragsauswahl.md", names)
        self.assertIn("verbraucherinsolvenz-werkstatt.md", names)
        self.assertIn("verbraucherinsolvenz-schnellstart.md", names)
        self.assertIn("insolvenzanfechtung-schnellstart.md", names)
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
                self.assertNotRegex(first, r"^(?:\||```|- |\d+\. )")
                self.assertNotRegex(
                    first,
                    r"(?i)^(?:\*\*)?(?:Autor:|Voraussetzungen:|Arbeitsumgebung:|Bedienregel:|"
                    r"Wenn du das hier (?:öffnest|oeffnest)\b|Du arbeitest als\b|Nur verfügbare Werkzeuge\b)",
                    "Der fachliche Zweck steht vor Rollenfloskeln und Einrichtung",
                )

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

    def test_active_full_checks_explain_the_subject_before_their_composition(self):
        plugins = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))["plugins"]
        for plugin in plugins:
            slug = plugin["name"]
            path = ROOT / "testakten/megaprompts" / f"{slug}.md"
            if not enabled(slug, "megaprompt") or not path.is_file():
                continue
            with self.subTest(plugin=slug):
                first_section = path.read_text(encoding="utf-8").split("## Zusammensetzung", 1)[0]
                self.assertGreaterEqual(len(opening_paragraph(first_section)), 80)


if __name__ == "__main__":
    unittest.main()
