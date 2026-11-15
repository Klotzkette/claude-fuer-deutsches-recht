#!/usr/bin/env python3
"""Alte Reviews werden durch Migration weder erfunden noch stillschweigend geheilt."""
import copy
import base64
import json
from pathlib import Path
import runpy
import tempfile
import unittest
from unittest.mock import patch

I = runpy.run_path(str(Path(__file__).with_name("integrate-skill-cap.py")))
E = I["ENGINE"]


class IntegrationTests(unittest.TestCase):
    def test_encoded_revision_restores_exact_bytes_and_rejects_tampering(self):
        before = '# Alttext\n[Beleg](../alter-pfad.md)\n'.encode()
        after = '# Geprüfte Neufassung\n[Beleg](../neuer-pfad.md)\n'.encode()
        edit = {'before_offset': 0, 'after_offset': 0, 'encoding': 'base64',
                'before': base64.b64encode(before).decode(),
                'after': base64.b64encode(after).decode()}
        self.assertEqual(E['restore_original'](after, [edit]), before)
        record = {'path': 'fach.md', 'sha256': E['sha'](after), 'edits': [edit]}
        self.assertEqual(I['apply_record'](before, record), after)
        with self.assertRaises(ValueError):
            E['restore_original'](after + b'X', [{**edit, 'after': base64.b64encode(after + b'Y').decode()}])
        with self.assertRaises(ValueError):
            E['restore_original'](after, [{**edit, 'before': 'invalid!'}])
        with self.assertRaises(ValueError):
            E['restore_original'](after, [{**edit, 'encoding': 'unknown'}])

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name).resolve()
        self.source = "oberordner/fachgebiet"
        self.old = self.source + "/skills/alte-pruefung/SKILL.md"
        self.new = self.source + "/skills/alte-pruefung/FACHINHALT.md"
        before = b"# Fachquelle\n\n[Details](../weitere/SKILL.md)\n"
        after, edits = E["rewrite_document"](before, self.new,
                         {self.source + "/skills/weitere/SKILL.md": self.source + "/skills/weitere/FACHINHALT.md"}, {}, {})
        self.write(self.new, after)
        self.write(self.source + "/skills/weitere/FACHINHALT.md", b"# Weitere\n")
        self.write(self.source + "/skills/neuer-arbeitsweg/SKILL.md", b"# Weg\n\n[Alte Fachquelle](../alte-pruefung/FACHINHALT.md)\n")
        self.record = {"original_path": self.old, "path": self.new, "original_sha256": E["sha"](before), "sha256": E["sha"](after), "edits": edits}
        self.report = {"files": [self.record], "integration_inventory": [],
                       "plugins": [{"name": "fachgebiet", "source": self.source,
                                    "active_skills": ["neuer-arbeitsweg"], "routes": []}],
                       "migrations": [{"plugin": "fachgebiet", "old": "alte-pruefung", "new": "neuer-arbeitsweg", "reference": "../alte-pruefung/FACHINHALT.md"}]}

    def write(self, name, data):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def profile(self, digest=None):
        return {"plugin": "fachgebiet", "reviewed_on": "2026-09-01", "needs_review": True,
                "selection": {"target_skill": "alte-pruefung"},
                "cases": [{"id": "bestehender-fall", "target_skill": "alte-pruefung", "criteria": ["Unverändertes Kriterium"]}],
                "skill_reviews": [{"skill_path": self.old, "sha256": digest or self.record["original_sha256"],
                                   "verdict": "needs_review", "needs_review": True, "reviewed_on": "2026-09-01", "reason": "Alte offene Prüfung"}]}

    def test_exact_hash_rebind_preserves_review_status_and_date(self):
        original = self.profile()
        updated, changes, pending = I["migrate_quality"](original, self.repo, self.report)
        self.assertEqual(pending, [])
        self.assertTrue(changes)
        self.assertEqual(updated["skill_reviews"], [])
        reference = updated["reference_reviews"][0]
        self.assertEqual(reference["skill_path"], self.new)
        self.assertEqual(reference["sha256"], self.record["sha256"])
        self.assertEqual(reference["verdict"], "needs_review")
        self.assertTrue(reference["needs_review"])
        self.assertTrue(updated["needs_review"])
        self.assertEqual(reference["reviewed_on"], "2026-09-01")
        self.assertEqual(updated["cases"][0]["criteria"], original["cases"][0]["criteria"])
        self.assertEqual(updated["cases"][0]["target_skill"], "neuer-arbeitsweg")

    def test_preexisting_stale_binding_is_never_repaired(self):
        original = self.profile("0" * 64)
        updated, _, pending = I["migrate_quality"](original, self.repo, self.report)
        self.assertEqual(len(pending), 1)
        self.assertEqual(updated["reference_reviews"][0]["sha256"], "0" * 64)
        self.assertEqual(updated["reference_reviews"][0]["verdict"], "needs_review")

    def test_additional_content_edit_cannot_be_certified_as_path_update(self):
        path = self.repo / self.new
        path.write_bytes(path.read_bytes() + b"\nNeue Behauptung\n")
        updated, _, pending = I["migrate_quality"](self.profile(), self.repo, self.report)
        self.assertEqual(len(pending), 1)
        self.assertEqual(updated["reference_reviews"][0]["sha256"], self.record["original_sha256"])

    def test_forged_reversible_edits_are_rejected(self):
        report = copy.deepcopy(self.report)
        report["files"][0]["edits"][0]["before"] = "Anderer Inhalt"
        _, _, pending = I["migrate_quality"](self.profile(), self.repo, report)
        self.assertTrue(pending)

    def test_historical_snapshots_are_never_rebound_or_declared_pending(self):
        profile = self.profile()
        history = {"path": self.old, "sha256": self.record["original_sha256"], "verdict": "retained"}
        profile["focus_review"] = {"previous_hashes": [copy.deepcopy(history)]}
        profile["source_followup_2026_10_16"] = {"files": [copy.deepcopy(history)]}
        updated, _, pending = I["migrate_quality"](profile, self.repo, self.report)
        self.assertEqual(updated["focus_review"]["previous_hashes"], [history])
        self.assertEqual(updated["source_followup_2026_10_16"], profile["source_followup_2026_10_16"])
        self.assertEqual(pending, [])

    def focus_profile(self, alias_hash=None):
        path = self.source + "/fachgebiet-hauptproblem.md"
        before = b"# Schwerpunkt\n\n[Vertiefung](skills/alte-pruefung/SKILL.md)\n"
        after, edits = E["rewrite_document"](before, path, {self.old: self.new}, {}, {})
        self.write(path, after)
        record = {"original_path": path, "path": path, "original_sha256": E["sha"](before),
                  "sha256": E["sha"](after), "edits": edits}
        self.report["integration_inventory"].append(record)
        profile = self.profile()
        profile["focus_review"] = {
            "prompt_path": path, "prompt_sha256": record["original_sha256"],
            "sha256": alias_hash or record["original_sha256"],
            "skill_path": self.old, "skill_sha256": self.record["original_sha256"],
            "reviewed_on": "2026-09-01", "method": "desk_review", "needs_review": True,
        }
        return profile, record

    def test_focus_alias_is_bound_to_prompt_and_not_skill(self):
        profile, prompt = self.focus_profile()
        updated, _, pending = I["migrate_quality"](profile, self.repo, self.report)
        focus = updated["focus_review"]
        self.assertEqual(pending, [])
        self.assertEqual(focus["sha256"], prompt["sha256"])
        self.assertEqual(focus["prompt_sha256"], prompt["sha256"])
        self.assertEqual(focus["skill_sha256"], self.record["sha256"])
        self.assertNotEqual(focus["sha256"], focus["skill_sha256"])
        self.assertEqual(focus["skill_path"], self.new)
        self.assertEqual(focus["reviewed_on"], "2026-09-01")
        self.assertTrue(focus["needs_review"])

    def test_stale_focus_alias_is_not_healed_by_valid_named_hashes(self):
        profile, prompt = self.focus_profile(alias_hash="0" * 64)
        updated, _, pending = I["migrate_quality"](profile, self.repo, self.report)
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["path"], prompt["original_path"])
        self.assertEqual(updated["focus_review"]["sha256"], "0" * 64)
        self.assertEqual(updated["focus_review"]["prompt_sha256"], prompt["sha256"])
        self.assertEqual(updated["focus_review"]["skill_sha256"], self.record["sha256"])

    def test_two_hashes_use_original_skill_path_before_it_moves(self):
        profile = self.profile()
        profile["skill_reviews"][0]["skill_sha256"] = self.record["original_sha256"]
        updated, _, pending = I["migrate_quality"](profile, self.repo, self.report)
        self.assertEqual(pending, [])
        review = updated["reference_reviews"][0]
        self.assertEqual(review["sha256"], self.record["sha256"])
        self.assertEqual(review["skill_sha256"], self.record["sha256"])

    def test_historical_chain_reaches_final_route_and_original_reference(self):
        reference = self.source + "/skills/alte-pruefung/references/einzelthema.md"
        self.write(reference, b"# Originale Vertiefung\n")
        existing = [{"plugin": "fachgebiet", "old": "historische-auswahl", "new": "alte-pruefung", "reference": "references/einzelthema.md"}]
        rows = I["flatten_migrations"](existing, self.report, self.repo)
        historical = next(r for r in rows if r["old"] == "historische-auswahl")
        self.assertEqual(historical["new"], "neuer-arbeitsweg")
        self.assertEqual(historical["reference"], "../alte-pruefung/references/einzelthema.md")
        self.assertEqual(len(rows), 2)

    def test_historical_chain_without_reference_retains_intermediate_fachtext(self):
        existing = [{"plugin": "fachgebiet", "old": "historisch", "new": "alte-pruefung"}]
        row = next(r for r in I["flatten_migrations"](existing, self.report, self.repo) if r["old"] == "historisch")
        self.assertEqual(row["reference"], "../alte-pruefung/FACHINHALT.md")

    def test_migration_cycle_missing_reference_and_path_escape_fail(self):
        for existing in ([{"plugin": "fachgebiet", "old": "neuer-arbeitsweg", "new": "alte-pruefung"}],
                         [{"plugin": "fachgebiet", "old": "historisch", "new": "alte-pruefung", "reference": "fehlt.md"}],
                         [{"plugin": "fachgebiet", "old": "historisch", "new": "alte-pruefung", "reference": "../../../../../outside.md"}]):
            with self.assertRaises(ValueError):
                I["flatten_migrations"](existing, self.report, self.repo)

    def test_integration_plan_is_explicit_and_preflights_every_file(self):
        first = self.write("erstes.md", "Änderung eins\n".encode())
        second = self.write("zweites.md", b"Original zwei\n")
        a = I["diff_record"]("erstes.md", first.read_bytes(), "Änderung zwei\n".encode(), "test")
        b = I["diff_record"]("zweites.md", second.read_bytes(), b"Neu zwei\n", "test")
        plan = {"files": [a, b]}
        second.write_bytes(b"Parallel bearbeitet\n")
        with self.assertRaises(ValueError):
            I["apply_plan"](self.repo, plan)
        self.assertEqual(first.read_text(), "Änderung eins\n")
        second.write_bytes(b"Original zwei\n")
        I["apply_plan"](self.repo, plan)
        self.assertEqual(first.read_text(), "Änderung zwei\n")
        self.assertEqual(second.read_bytes(), b"Neu zwei\n")

    def test_legacy_encoded_raw_documents_remain_byte_exact(self):
        path = self.write('beleg.txt', 'Überweisung für Rechnung'.encode('cp1252'))
        with patch.dict(E, {'verify_source_map': lambda *args: []}):
            plan = I['prepare_plan'](self.repo, self.report)
        self.assertEqual(plan['unchanged_non_utf8_documents'][0]['sha256'], E['sha'](path.read_bytes()))
        self.assertFalse(any(row['path']=='beleg.txt' for row in plan['files']))
        path.write_bytes(path.read_bytes() + b' /fachgebiet:alte-pruefung')
        with patch.dict(E, {'verify_source_map': lambda *args: []}):
            with self.assertRaisesRegex(ValueError, 'beleg.txt'):
                I['prepare_plan'](self.repo, self.report)


if __name__ == "__main__":
    unittest.main()
