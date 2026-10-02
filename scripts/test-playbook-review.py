#!/usr/bin/env python3
"""Behavioral tests for evidence, version isolation and playbook rule semantics."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("playbook_review", ROOT / "playbook-pruefer/scripts/playbook_review.py")
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)


class PlaybookReview(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        text = "1 Arbeitszeit\nDie Arbeitszeit beträgt 40 Stunden pro Woche. Zehn Überstunden sind abgegolten.\n"
        (self.root / "vertrag.txt").write_text(text)
        self.data = {
            "schema_version": 1, "review_id": "review-1", "document_precedence": "Nur Fassung 2 ist maßgeblich.",
            "documents": [{"id": "V2", "title": "Arbeitsvertrag", "version": "2", "role": "authoritative",
                           "path": "vertrag.txt", "sha256": hashlib.sha256(text.encode()).hexdigest()}],
            "playbook": {"id": "ARBEIT", "version": "1", "approved_by": "Personalabteilung", "approval_reference": "Freigabe E1",
                         "contract_type": "Arbeitsvertrag", "client_side": "Arbeitgeber", "topics": [
                             {"id": "T1", "title": "Arbeitszeit", "required": True, "positions": [
                                 {"id": "S", "type": "starting", "rules": [{"id": "S1", "condition": "Höchstens 40 Wochenstunden"}]},
                                 {"id": "F1", "type": "fallback", "rules": [{"id": "F11", "condition": "Höchstens 42 Wochenstunden"}]},
                                 {"id": "N", "type": "not_acceptable", "match_mode": "any", "rules": [
                                     {"id": "N1", "condition": "Mehr als 42 Wochenstunden"},
                                     {"id": "N2", "condition": "Unbegrenzte Überstundenabgeltung"}]}]}]},
            "topic_observations": {"T1": {"presence": "found", "reasoning": "Die Klausel erfüllt die betrieblichen Grenzen."}},
            "observations": {rid: {"outcome": outcome, "reasoning": "An der vorliegenden Klausel geprüft.", "basis": "quote",
                                    "citations": [{"document_id": "V2", "locator": "Ziffer 1", "locator_verified": True,
                                                   "quote": "Die Arbeitszeit beträgt 40 Stunden pro Woche."}]}
                             for rid, outcome in [("S1", "met"), ("F11", "met"), ("N1", "not_met"), ("N2", "not_met")]}}

    def run_review(self):
        return engine.evaluate(self.data, self.root)

    def unknown(self, rid, status="not_verifiable"):
        self.data["observations"][rid] = {"outcome": status, "reasoning": "Eine notwendige Anlage fehlt.",
                                           "basis": "unresolved", "question": "Bitte legen Sie die bezeichnete Anlage vor."}

    def test_clean_contract_has_zero_redline_matches(self):
        out = self.run_review()
        self.assertEqual(out["topics"][0]["risk"], "none")
        self.assertTrue(out["ready_for_human_decision"])
        red = out["topics"][0]["positions"][2]
        self.assertEqual((red["met"], red["judged"]), (0, 2))
        self.assertEqual(red["rules"][0]["label"], "Not detected")

    def test_one_independent_redline_is_high_without_inverting_count(self):
        self.data["observations"]["N1"]["outcome"] = "met"
        out = self.run_review()
        self.assertEqual(out["topics"][0]["risk"], "high")
        red = out["topics"][0]["positions"][2]
        self.assertEqual((red["met"], red["judged"]), (1, 2))
        self.assertEqual(red["rules"][0]["label"], "Detected")
        self.assertFalse(out["ready_for_human_decision"])

    def test_cumulative_redline_requires_all_conditions(self):
        self.data["playbook"]["topics"][0]["positions"][2]["match_mode"] = "all"
        self.data["observations"]["N1"]["outcome"] = "met"
        self.assertEqual(self.run_review()["topics"][0]["risk"], "none")

    def test_unverifiable_redline_cannot_be_clean(self):
        self.unknown("N2")
        out = self.run_review()
        self.assertEqual(out["topics"][0]["risk"], "not_verifiable")
        red = out["topics"][0]["positions"][2]
        self.assertEqual((red["met"], red["judged"], red["not_verifiable"]), (0, 1, 1))
        self.assertFalse(out["ready_for_human_decision"])

    def test_redline_any_detected_overrides_unknown(self):
        self.unknown("N2")
        self.data["observations"]["N1"]["outcome"] = "met"
        self.assertEqual(self.run_review()["topics"][0]["risk"], "high")

    def test_fallback_and_no_acceptable_position(self):
        self.data["observations"]["S1"]["outcome"] = "not_met"
        self.assertEqual(self.run_review()["topics"][0]["risk"], "medium")
        self.data["observations"]["F11"]["outcome"] = "not_met"
        self.assertEqual(self.run_review()["topics"][0]["risk"], "high")

    def test_unknown_start_cannot_hide_existing_fallback_or_unknown_counter(self):
        self.unknown("S1")
        out = self.run_review()
        self.assertEqual(out["topics"][0]["matched_position"], "F1")
        self.assertEqual(out["topics"][0]["risk"], "medium")
        self.assertFalse(out["ready_for_human_decision"])

    def test_known_unacceptable_contract_stays_high_with_unknown_redline(self):
        self.data["observations"]["S1"]["outcome"] = "not_met"
        self.data["observations"]["F11"]["outcome"] = "not_met"
        self.unknown("N2")
        out = self.run_review()
        self.assertEqual(out["topics"][0]["risk"], "high")
        self.assertTrue(out["topics"][0]["unresolved_rules"])

    def test_pending_rejected_at_final_allowed_in_draft(self):
        self.unknown("S1", "pending")
        with self.assertRaisesRegex(engine.ReviewError, "Pending"):
            self.run_review()
        self.assertFalse(engine.evaluate(self.data, self.root, final=False)["ready_for_human_decision"])

    def test_missing_or_foreign_rule_is_error(self):
        self.data["observations"]["FOREIGN"] = copy.deepcopy(self.data["observations"]["S1"])
        with self.assertRaisesRegex(engine.ReviewError, "Fremde"):
            self.run_review()
        del self.data["observations"]["FOREIGN"]
        del self.data["observations"]["S1"]
        with self.assertRaisesRegex(engine.ReviewError, "fehlt"):
            self.run_review()

    def test_changed_document_or_fabricated_quote_rejected(self):
        self.data["observations"]["S1"]["citations"][0]["quote"] = "Nur 30 Wochenstunden."
        with self.assertRaisesRegex(engine.ReviewError, "Zitat fehlt"):
            self.run_review()
        (self.root / "vertrag.txt").write_text("Andere Fassung")
        with self.assertRaisesRegex(engine.ReviewError, "Quellendatei geändert"):
            self.run_review()

    def test_context_email_or_old_version_cannot_replace_contract(self):
        for role in ("context", "superseded"):
            with self.subTest(role=role):
                self.data["documents"].append({**self.data["documents"][0], "id": "ALT", "role": role})
                self.data["observations"]["S1"]["citations"][0]["document_id"] = "ALT"
                with self.assertRaises(engine.ReviewError):
                    self.run_review()
                self.data["documents"].pop()

    def test_missing_required_topic_keeps_not_found_badge_and_high_risk(self):
        self.data["topic_observations"]["T1"]["presence"] = "not_found"
        for obs in self.data["observations"].values():
            obs.update(basis="absence", citations=[], searched_document_ids=["V2"], search_description="Gesamten Vertrag auf Arbeitszeit und Synonyme geprüft.")
        out = self.run_review()["topics"][0]
        self.assertEqual((out["badge"], out["risk"]), ("Not found", "high"))
        self.data["observations"]["S1"]["searched_document_ids"] = []
        with self.assertRaisesRegex(engine.ReviewError, "Suchumfang"):
            self.run_review()

    def test_scope_exception_requires_prior_authorization_and_is_counted(self):
        self.data["observations"]["N2"] = {"outcome": "excluded", "reasoning": "Keine Mehrarbeit im vereinbarten Mandatsumfang."}
        with self.assertRaisesRegex(engine.ReviewError, "Ausnahmefreigabe"):
            self.run_review()
        self.data["observations"]["N2"]["scope_approval"] = {"by": "Mandantin", "reason": "Separate bereits geprüfte Vereinbarung.", "reference": "Auftrag Ziffer 4"}
        red = self.run_review()["topics"][0]["positions"][2]
        self.assertEqual((red["met"], red["judged"], red["excluded"]), (0, 1, 1))

    def test_all_excluded_is_never_vacuously_satisfied(self):
        self.assertEqual(engine.match(["excluded"], "all"), "unknown")
        self.assertEqual(engine.match(["excluded"], "any"), "unknown")

    def test_invalid_law_overrides_firm_policy_and_is_exported(self):
        self.data["topic_observations"]["T1"]["legal_findings"] = [{
            "status": "confirmed_invalid", "reasoning": "Gesondert belegter Rechtsbefund für den Test.",
            "authority": "Testquelle", "source_url": "https://example.org/test", "pinpoint": "Absatz 1", "checked_on": "2026-10-02",
            "contract_citations": copy.deepcopy(self.data["observations"]["S1"]["citations"])}]
        out = self.run_review()
        self.assertEqual(out["topics"][0]["risk"], "high")
        self.assertIn("https://example.org/test", "\n".join(engine.report_lines(out)))

    def test_duplicate_json_keys_and_paths_fail_closed(self):
        with self.assertRaisesRegex(engine.ReviewError, "Doppelter JSON"):
            json.loads('{"id":1,"id":2}', object_pairs_hook=engine.unique_json)
        for path in ("../vertrag.txt", "/etc/passwd"):
            self.data["documents"][0]["path"] = path
            with self.assertRaises(engine.ReviewError):
                self.run_review()

    def test_unverified_locator_is_not_silently_confirmed(self):
        del self.data["observations"]["S1"]["citations"][0]["locator_verified"]
        with self.assertRaisesRegex(engine.ReviewError, "Fundstellenort|Klauselort"):
            self.run_review()


if __name__ == "__main__":
    unittest.main()
