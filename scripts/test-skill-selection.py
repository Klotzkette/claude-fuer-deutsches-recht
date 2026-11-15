#!/usr/bin/env python3
"""Regressionen bei sprechenden Namen und bedarfsgeladenen Fachvertiefungen."""

from pathlib import Path
import hashlib
import json
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

    def test_preserved_sibling_content_must_be_explicitly_linked(self):
        skill = self.skill()
        reference = self.root / "alte-auswahl" / "FACHINHALT.md"
        reference.parent.mkdir()
        reference.write_text("# Vollständiger Fachinhalt\n", encoding="utf-8")
        migration = {**self.migration, "reference": "../alte-auswahl/FACHINHALT.md"}
        self.assertTrue(self.errors(migration))
        self.skill(extra="[Fachinhalt](../alte-auswahl/FACHINHALT.md)")
        self.assertEqual([], self.errors(migration))
        # Die Erweiterung lässt eine einzelne Datei oder eine fremde Bibliothek
        # außerhalb des installierbaren Plugins weiterhin nicht passieren.
        outsider = self.repo / "fremdes-plugin.md"
        outsider.write_text("# Fremd")
        self.skill(extra="[Fremd](../../../fremdes-plugin.md)")
        self.assertTrue(self.errors({**self.migration, "reference": "../../../fremdes-plugin.md"}))

    def test_marketplace_source_resolves_nested_plugins(self):
        self.root = self.repo / "oberordner/fachgebiet/skills"
        self.skill(extra="[Fachinhalt](../alte-auswahl/FACHINHALT.md)")
        reference = self.root / "alte-auswahl/FACHINHALT.md"
        reference.parent.mkdir()
        reference.write_text("# Alt\n")
        marketplace = self.repo / ".claude-plugin/marketplace.json"
        marketplace.parent.mkdir()
        marketplace.write_text(json.dumps({"plugins": [{"name": "fachgebiet", "source": "./oberordner/fachgebiet"}]}))
        self.assertEqual([], self.errors({**self.migration, "reference": "../alte-auswahl/FACHINHALT.md"}))

    def test_sibling_reference_symlink_cannot_escape_plugin(self):
        self.skill(extra="[Fachinhalt](../alte-auswahl/FACHINHALT.md)")
        outsider = self.repo / "fremd.md"
        outsider.write_text("# Fremd")
        reference = self.root / "alte-auswahl/FACHINHALT.md"
        reference.parent.mkdir()
        reference.symlink_to(outsider)
        self.assertTrue(self.errors({**self.migration, "reference": "../alte-auswahl/FACHINHALT.md"}))

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

    def replacement(self):
        self.skill(extra='[Neufassung](../../references/kapitel.md)')
        chapter = self.root.parent / 'references/kapitel.md'
        chapter.parent.mkdir()
        chapter.write_text('# Fachliche Neufassung')
        old = 'fachgebiet/skills/alte-auswahl/FACHINHALT.md'
        new = 'quality/ersatz/legacy/' + old
        archived = self.repo / new
        archived.parent.mkdir(parents=True)
        archived.write_text('# Vollständiger Alttext')
        content = archived.read_bytes()
        manifest = self.repo / 'quality/ersatz/legacy/mapping.json'
        manifest.write_text(json.dumps({'files': [{'old_path': old, 'new_path': new,
                                                 'sha256': hashlib.sha256(content).hexdigest(), 'bytes': len(content)}]}))
        config = self.repo / 'scripts/data/skill-source-replacements.json'
        config.parent.mkdir(parents=True)
        config.write_text(json.dumps({'schema_version': 1, 'plugins': {'fachgebiet': {
            'source': 'fachgebiet', 'active_skills': ['aufgabe-pruefen'],
            'chapters': ['references/kapitel.md'], 'archive_manifest': 'quality/ersatz/legacy/mapping.json'}}}))
        marketplace = self.repo / '.claude-plugin/marketplace.json'
        marketplace.parent.mkdir()
        marketplace.write_text(json.dumps({'plugins': [{'name': 'fachgebiet', 'source': './fachgebiet'}]}))
        return archived, {**self.migration, 'reference': '../alte-auswahl/FACHINHALT.md'}

    def test_explicit_fachlich_replaced_source_accepts_only_exact_verified_archive(self):
        archived, migration = self.replacement()
        self.assertEqual([], self.errors(migration))
        self.assertTrue(self.errors({**migration, 'reference': '../unbekannt/FACHINHALT.md'}))
        archived.write_text('# Falscher Archivtext')
        self.assertTrue(self.errors(migration))

    def test_replacement_does_not_hide_missing_target_or_active_drift(self):
        _, migration = self.replacement()
        self.assertTrue(self.errors({**migration, 'new': 'fehlt'}))
        self.skill('zusaetzlich')
        self.assertTrue(self.errors(migration))


if __name__ == "__main__":
    unittest.main()
