#!/usr/bin/env python3
"""Regressionen bei sprechenden Namen und bedarfsgeladenen Fachvertiefungen."""

from pathlib import Path
import runpy
import tempfile
import unittest


MODULE = runpy.run_path(str(Path(__file__).with_name("audit-skill-selection.py")))


class SkillSelectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.root = self.repo / "fachgebiet" / "skills"
        self.migration = {"plugin": "fachgebiet", "old": "alte-auswahl", "new": "aufgabe-pruefen"}

    def skill(self, slug="aufgabe-pruefen", title="Aufgabe prüfen", extra=""):
        path = self.root / slug / "SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'---\nname: {slug}\ndescription: "Konkrete Prüfung"\n---\n\n# {title}\n\n{extra}', encoding="utf-8")
        return path

    def errors(self, migration=None):
        return MODULE["validate_migrations"](self.repo, [migration or self.migration])

    def test_title_normalization_retains_distinctions(self):
        normalize = MODULE["heading_key"]
        self.assertEqual(normalize("1. Prüfung: Äußerung"), normalize("Prüfung – Äußerung"))
        self.assertNotEqual(normalize("Zulassung"), normalize("Zustellung"))

    def test_replacement_exists_without_old_selection(self):
        self.skill()
        self.assertEqual([], self.errors())

    def test_missing_replacement_is_error(self):
        self.assertTrue(self.errors())

    def test_old_selection_cannot_silently_return(self):
        self.skill()
        self.skill("alte-auswahl")
        self.assertTrue(self.errors())

    def test_conflicting_migration_is_error(self):
        self.skill()
        self.assertTrue(MODULE["validate_migrations"](self.repo, [self.migration, self.migration]))

    def test_reference_must_be_reachable_not_merely_present(self):
        skill = self.skill()
        reference = skill.parent / "references" / "vertiefung.md"
        reference.parent.mkdir()
        reference.write_text("# Vertiefung\n", encoding="utf-8")
        migration = {**self.migration, "reference": "references/vertiefung.md"}
        self.assertTrue(self.errors(migration))
        self.skill(extra="[Vertiefung](./references/vertiefung.md)")
        self.assertEqual([], self.errors(migration))

    def test_reference_cycle_terminates(self):
        skill = self.skill(extra="[Details](./details.md)")
        (skill.parent / "details.md").write_text("[Zurück](./SKILL.md)", encoding="utf-8")
        self.assertFalse(MODULE["reference_reachable"](skill, skill.parent / "missing.md"))

    def test_reference_cannot_escape_plugin(self):
        self.skill()
        self.assertTrue(self.errors({**self.migration, "reference": "../../../../outside.md"}))

    def test_equal_titles_are_only_review_candidates(self):
        self.skill()
        self.skill("zweite-aufgabe")
        report = MODULE["inspect_plugin"](self.root.parent)
        self.assertEqual([], report["errors"])
        self.assertEqual(1, len(report["same_title_groups"]))

    def test_double_namespace_only_repaired_for_existing_target(self):
        correct = MODULE["invocation_corrections"]
        names = {"fachgebiet": {"pruefen", "fachgebiet-original"}}
        text = "/fachgebiet:fachgebiet-pruefen /fachgebiet:fachgebiet-original /fachgebiet:fachgebiet-fehlt"
        self.assertEqual({"/fachgebiet:fachgebiet-pruefen": "/fachgebiet:pruefen"}, correct(text, names))

    def test_existing_longer_name_is_not_truncated(self):
        correct = MODULE["invocation_corrections"]
        self.assertEqual({}, correct("/fachgebiet:fachgebiet-pruefen", {"fachgebiet": {"pruefen", "fachgebiet-pruefen"}}))


if __name__ == "__main__":
    unittest.main()
