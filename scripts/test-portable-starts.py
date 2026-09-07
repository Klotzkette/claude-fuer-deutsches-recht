#!/usr/bin/env python3
"""Prüft portable Startregeln und ihre Erhaltung bei erneuter Erzeugung.

Diese Tests prüfen Dateien und Generatorverhalten, keine fremde Laufzeitumgebung.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from themen_profile import PROFILE_BY_KEY


REPO = Path(__file__).resolve().parent.parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


G = load("portable_prompt_generator", "generate-werkstatt-und-schnellstart-prompts.py")
R = load("portable_prompt_refiner", "refine-speed-and-elegance.py")


class PortableStarts(unittest.TestCase):
    def test_explicit_request_is_not_replaced_by_default_product(self):
        for key, profile in PROFILE_BY_KEY.items():
            with self.subTest(profile=key):
                lines = G.schnellstart_bedienlogik(profile, [("Fachfrage", "Beleg")], [])
                explicit = next(line for line in lines if line.startswith("- Konkreter Auftrag:"))
                self.assertIn("Das verlangte Arbeitsprodukt sofort", explicit)
                self.assertNotIn("„", explicit)
                self.assertIn(G.PORTABLE_EXECUTION, lines)

    def test_workshop_preview_is_conditional_in_every_family(self):
        for key, profile in PROFILE_BY_KEY.items():
            with self.subTest(profile=key):
                text = "\n".join(G.werkstatt_tempo_block(profile))
                self.assertIn("Ohne konkreten Ausgabeauftrag", text)
                self.assertIn("Bei einem konkreten Auftrag direkt dessen Arbeitsprodukt", text)

    def test_compaction_preserves_late_case_anchor(self):
        norms = [f"- Normanker {index}: Tatbestand und Folge." for index in range(10)]
        case = "- BGH, Urteil: vorhandener Entscheidungsanker mit eingegrenzter Aussage."
        for limit in (7, 8):
            result = G.compact_anchor_lines("\n".join(norms + [case]), limit)
            self.assertEqual(len(result), limit)
            self.assertEqual(result[0], norms[0])
            self.assertEqual(result[-1], case)

    def test_compaction_does_not_invent_or_duplicate_cases(self):
        for lines in ([], ["- Technische Ausgabevorgabe."], ["- BAG, Beschluss: Quellenanker.", "- Norm."]):
            self.assertEqual(G.compact_anchor_lines("\n".join(lines), 8), lines)

    def test_company_abbreviation_is_not_a_case_anchor(self):
        lines = ["- HGB: Gesellschaftsvertrag einer KG prüfen."] * 9
        for court in ("KG", "BPatG", "EuG"):
            case = f"- {court}, Beschluss: eingegrenzter Quellenanker."
            self.assertEqual(G.compact_anchor_lines("\n".join(lines + [case]), 7)[-1], case)

    def test_skill_cleanup_is_exact_and_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            before = "---\nname: pruefung\ndescription: Fachaufgabe.\n---\n\n# Prüfung\n\n## 1. Ablauf\n\nVertrag zuerst lesen.\n"
            path.write_text(before + "\n" + R.DIREKTSTART_SENTENCE + "\n\n## 2. Fachregel\n\nBeleg prüfen.\n", encoding="utf-8")
            self.assertTrue(R.refine_skill(path))
            self.assertEqual(path.read_text(encoding="utf-8"), before + "\n## 2. Fachregel\n\nBeleg prüfen.\n")
            self.assertFalse(R.refine_skill(path))

    def test_unrelated_skill_is_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            before = "# Fachregel\n\nLiefere sieben begründete Alternativen nur auf Auftrag.\n"
            path.write_text(before, encoding="utf-8")
            self.assertFalse(R.refine_skill(path))
            self.assertEqual(path.read_text(encoding="utf-8"), before)

    def test_curated_start_is_idempotent_and_keeps_subject(self):
        with tempfile.TemporaryDirectory() as tmp:
            plugin = Path(tmp)
            (plugin / ".claude-plugin").mkdir()
            (plugin / ".claude-plugin/plugin.json").write_text(json.dumps({"name": "arbeitsrecht", "description": "Arbeitsrecht"}), encoding="utf-8")
            path = plugin / "arbeitsrecht-schnellstart.md"
            subject = "## 1. Auftrag\n\nNur den bereits vorliegenden Vergleich überarbeiten.\n"
            path.write_text("# Arbeitsrecht\n\nBedienregel: bisheriger Einstieg.\n\n" + subject, encoding="utf-8")
            with patch.object(G, "collect_skill_material", return_value=[]):
                self.assertTrue(G.normalize_protected_schnellstart(plugin))
                self.assertFalse(G.normalize_protected_schnellstart(plugin))
            text = path.read_text(encoding="utf-8")
            self.assertEqual(text.count("Bedienregel:"), 1)
            self.assertIn(subject, text)
            self.assertIn(G.PORTABLE_EXECUTION, text)

    def test_every_published_prompt_has_portable_fallbacks(self):
        plugins = json.loads((REPO / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))["plugins"]
        for plugin in plugins:
            root = REPO / plugin["source"]
            skill_names = {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}
            for kind in ("schnellstart", "werkstatt"):
                path = root / f"{plugin['name']}-{kind}.md"
                with self.subTest(path=path.relative_to(REPO)):
                    text = path.read_text(encoding="utf-8")
                    self.assertIn(G.PORTABLE_EXECUTION, text)
                    self.assertNotIn("passende Fachskills laufen intern", text)
                    self.assertNotIn("Passende Fachskills intern als Teilroute nutzen", text)
                    self.assertFalse(skill_names & set(re.findall(r"`([a-z0-9-]+)`", text)), "Eigenständiger Prompt verweist auf installierten Skill")
                    if kind == "schnellstart":
                        self.assertLess(len(text.encode("utf-8")), 7500)
                    else:
                        self.assertIn(G.WORKSHOP_EXECUTION, text)
            for path in (root / "skills").glob("*/SKILL.md"):
                with self.subTest(skill=path.relative_to(REPO)):
                    self.assertNotIn(R.DIREKTSTART_SENTENCE, path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
