#!/usr/bin/env python3
"""Sichert datierte Reformhinweise, lokale Quellen und eigenständige Prompts."""

from pathlib import Path
import importlib.util
import re
import unittest
from quality_lab import load, validate_profile


ROOT = Path(__file__).resolve().parent.parent
PLUGINS = (
    "ki-vo-ai-act-pruefer", "ki-governance", "ki-richtlinie-kanzleien",
    "berufsrecht-ki-vertragspruefung", "datenschutzrecht",
    "datenschutz-sanktionsverfahren-verteidigung", "fachanwalt-it-recht",
    "robotik-recht",
)
REFERENCE = "references/digitaler-omnibus-2026.md"
SPEC = importlib.util.spec_from_file_location("omnibus_structure", ROOT / "scripts/audit-prompt-profile-routing.py")
STRUCTURE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(STRUCTURE)


def optional_skill_link_errors(text):
    """Nur den Linkvertrag prüfen, keine fachliche Eigenständigkeit simulieren."""
    return [paragraph for paragraph in re.split(r"\n\s*\n", text)
            if re.search(r"\]\([^)]*skills/", paragraph)
            and not re.search(r"\boptional\w*\b", paragraph, re.I)]


class OmnibusTests(unittest.TestCase):
    def test_reference_is_packaged_locally_and_identical(self):
        source = (ROOT / REFERENCE).read_bytes()
        for plugin in PLUGINS:
            with self.subTest(plugin=plugin):
                self.assertEqual((ROOT / plugin / REFERENCE).read_bytes(), source)
                readme = (ROOT / plugin / "README.md").read_text()
                self.assertIn("./" + REFERENCE, readme)
                self.assertIn("download.html?path=" + plugin + "/" + REFERENCE, readme)

    def test_manual_prompts_remain_protected(self):
        protected = {
            line.strip() for line in
            (ROOT / "scripts/handkuratierte-prompts.txt").read_text().splitlines()
            if line.strip() and not line.startswith("#")
        }
        self.assertTrue(set(PLUGINS) <= protected)
        for plugin in PLUGINS:
            for kind in ("werkstatt", "schnellstart"):
                with self.subTest(plugin=plugin, kind=kind):
                    text = (ROOT / plugin / f"{plugin}-{kind}.md").read_text()
                    for token in ("2026/1744", "Artikel 4a", "KI-MIG", "Bundesnetzagentur"):
                        self.assertIn(token, text)
                    self.assertIn("2. Dezember 2027", text)
                    self.assertIn("2. August 2028", text)
                    self.assertEqual(optional_skill_link_errors(text), [])
                    self.assertNotIn("../../references/", text)
                    self.assertEqual(STRUCTURE.individual_workshop_structure_problems(text), [])
                    if kind == "schnellstart":
                        self.assertLess(len(text.encode("utf-8")), 7500)
                    else:
                        self.assertLess(len(text.encode("utf-8")), 48 * 1024)

    def test_individual_review_hashes_remain_required(self):
        for plugin in PLUGINS:
            review_path = ROOT / "quality/evals" / f"{plugin}.json"
            if review_path.is_file():
                with self.subTest(plugin=plugin):
                    validate_profile(load(review_path), plugin, ROOT / plugin)

    def test_structural_checks_allow_decimal_variants_but_reject_damage(self):
        for text in (
            "# Titel\n\n## 1. Auftrag\n\nText.\n",
            "# 1. Titel\n\n## 1.1. Auftrag\n\nText.\n\n## 2. Ergebnis\n\nText.\n",
        ):
            self.assertEqual(STRUCTURE.individual_workshop_structure_problems(text), [])
        for text in (
            "# Titel\n\n## A. Auftrag\n\nText.\n",
            "# Titel\n\n## 1. Auftrag\n\nText.\n\n## 1. Ergebnis\n\nText.\n",
            "# Titel\n\n## 1. Auftrag\n\n",
        ):
            self.assertTrue(STRUCTURE.individual_workshop_structure_problems(text))

    def test_skill_links_must_be_explicitly_optional(self):
        self.assertFalse(optional_skill_link_errors("Der optionale [Fokus](skills/fokus/SKILL.md) vertieft die Prüfung."))
        self.assertTrue(optional_skill_link_errors("Lade zuerst den [Fokus](skills/fokus/SKILL.md)."))
        self.assertTrue(optional_skill_link_errors("Optionale Hinweise.\n\nLade den [Fokus](skills/fokus/SKILL.md)."))

    def test_primary_sources_and_proposal_status(self):
        text = (ROOT / REFERENCE).read_text()
        for token in ("2025/0360(COD)", "2025/0130(COD)", "72 Stunden",
                      "96 Stunden", "Artikel 111 Absatz 4", "Artikel 4a",
                      "Paragraf 2 Absatz 1", "Abschnitt B", "noch vor der Ausschussentscheidung"):
            self.assertIn(token, text)
        self.assertIn("eur-lex.europa.eu/eli/reg/2026/1744/oj", text)
        self.assertIn("gesetze-im-internet.de/ki-mig/", text)
        self.assertIn("oeil.europarl.europa.eu", text)

    def test_transparency_roles_are_not_swapped(self):
        path = ROOT / "ki-vo-ai-act-pruefer/skills/begrenztes-risiko-art-50-transparenzpflichten/SKILL.md"
        text = path.read_text()
        for token in ("Absatz 2: Anbieter", "Absatz 3: Betreiber", "Absatz 4: Betreiber",
                      "Artikel 111 Absatz 4", "Betreiberhinweise aus Absatz 4"):
            self.assertIn(token, text)
        self.assertNotIn("Deepfake-Kennzeichnungspflicht (Art. 50 Abs. 2", text)

    def test_conformity_and_machine_routes(self):
        text = (ROOT / "ki-vo-ai-act-pruefer/skills/hochrisiko-konformitaetsbewertung-art-43/SKILL.md").read_text()
        for token in ("Nummern 2 bis 8", "Anhang VI", "Anhang VII", "Abschnitt B",
                      "nicht ausnahmslos eine Drittprüfung"):
            self.assertIn(token, text)
        self.assertNotIn("Modul H", text)
        self.assertNotIn("QMS) nach Anhang IX", text)

    def test_changed_skills_use_local_reference(self):
        for plugin in PLUGINS:
            for path in (ROOT / plugin / "skills").glob("*/SKILL.md"):
                text = path.read_text()
                for link in re.findall(r"\]\(([^)]+digitaler-omnibus-2026\.md)\)", text):
                    target = (path.parent / link).resolve()
                    self.assertTrue(target.is_file(), str(path))
                    self.assertTrue(target.is_relative_to((ROOT / plugin).resolve()), str(path))


if __name__ == "__main__":
    unittest.main()
