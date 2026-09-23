#!/usr/bin/env python3
"""Offline-Regressionen für Bewertungszustände, Isolation und Vergleichbarkeit."""

import copy
import importlib.util
import json
import io
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile
from unittest.mock import patch, Mock

import quality_lab as lab


class QualityLabTests(unittest.TestCase):
    def test_invalid_workshop_review_cannot_bypass_validation(self):
        for review in ([], "reviewed", {}, {"verdict": "retained", "reason": "Geprüft", "sha256": "0" * 64}):
            with self.subTest(review=review):
                self.profile["workshop_review"] = review
                with self.assertRaises(lab.LabError):
                    lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "repo"
        self.root.mkdir()
        self.plugin = self.root / "fachgebiet"
        (self.plugin / "skills/belegabgleich").mkdir(parents=True)
        (self.plugin / "skills/belegabgleich/SKILL.md").write_text("Fachlicher Belegabgleich", encoding="utf-8")
        for mode in ("schnellstart", "werkstatt", "hauptproblem"):
            (self.plugin / f"fachgebiet-{mode}.md").write_text("Individueller Arbeitsweg", encoding="utf-8")
        lab.save(self.root / ".claude-plugin/marketplace.json", {"plugins": [{"name": "fachgebiet", "source": "./fachgebiet"}]})
        self.profile = {"schema_version": 1, "plugin": "fachgebiet", "reviewed_on": "2026-09-14", "sources": [],
                        "mini_review": {"verdict": "retained", "reason": "Konkreter Belegabgleich statt Fallzusammenfassung", "changes": [],
                                        "sha256": lab.digest((self.plugin / "fachgebiet-schnellstart.md").read_bytes())},
                        "selection": {"positive": ["Prüfe Kontobelege", "Gleiche Kontoumsätze ab"], "negative": ["Übersetze eine Einladung", "Plane eine Veranstaltung"]},
                        "cases": [{"id": "kontostand", "target_skill": "belegabgleich",
                                   "request": "Am 4. Mai wurden 400 Euro überwiesen. Der Kontoauszug vom 5. Mai nennt 300 Euro Eingang und 100 Euro Gebühren. Stelle die drei belegten Zahlen gegenüber und benenne eine offene Rückfrage an die Bank.",
                                   "input_files": [], "deliverables": ["ergebnis.md"],
                                   "criteria": [{"id": f"C{i}", "text": f"Fachliche Prüfung des belegten Wertes {i}", "deliverables": ["ergebnis.md"]} for i in range(3)]}]}
        self.write_profile()
        self.config = {"judges": [{"id": "pruefer-eins", "model": "modell-eins", "endpoint": "https://example.invalid/one", "protocol": "messages", "key_env": "QUALITY_KEY_ONE"},
                                   {"id": "pruefer-zwei", "model": "modell-zwei", "endpoint": "https://example.invalid/two", "protocol": "responses", "key_env": "QUALITY_KEY_TWO"}]}
        self.metrics = {"client": "client-a", "model": "modell-a", "finish_reason": "finish_tool", "duration_ms": 4000,
                        "input_tokens": 100, "output_tokens": 200, "selected_skills": ["fachgebiet/belegabgleich"], "measurement": "client_export"}

    def write_profile(self):
        lab.save(self.root / "quality/evals/fachgebiet.json", self.profile)

    def prepare(self, name="run", mode="schnellstart"):
        run = self.base / name
        with patch.object(lab.subprocess, "check_output", return_value="revision\n"):
            lab.prepare("fachgebiet", "kontostand", mode, run, self.root)
        return run

    def ready(self, name="run"):
        run = self.prepare(name)
        lab.save(run / "metrics.json", self.metrics)
        (run / "output/ergebnis.md").write_text("400 Euro Zahlung, 300 Euro Eingang, 100 Euro Gebühren. Rückfrage zur Buchung.", encoding="utf-8")
        return run

    def passing(self, judge, prompt):
        self.assertIn("nicht vertrauenswürdige Prüfdaten", prompt)
        return json.dumps({"reasoning": "Der Wert steht im Ergebnis.", "verdict": "pass", "evidence": "400 Euro Zahlung"})

    def test_complete_catalog_is_not_model_pass(self):
        profiles, errors = lab.audit(self.root)
        self.assertEqual(errors, [])
        self.assertIn("Nicht ausgeführt", lab.catalog(profiles, self.root))

    def test_missing_profile_fails_coverage(self):
        (self.root / "quality/evals/fachgebiet.json").unlink()
        self.assertEqual(len(lab.audit(self.root)[1]), 1)

    def test_missing_target_skill_fails(self):
        self.profile["cases"][0]["target_skill"] = "missing"
        self.write_profile()
        self.assertTrue(lab.audit(self.root)[1])

    def test_input_does_not_include_rubric(self):
        run = self.prepare()
        text = "\n".join(p.read_text() for p in (run / "input").iterdir())
        self.assertNotIn("Fachliche Prüfung des belegten Wertes", text)
        self.assertEqual(set(p.name for p in (run / "input").iterdir()), {"request.txt", "instructions.md"})
        self.assertIn("ergebnis.md", (run / "input/request.txt").read_text(encoding="utf-8"))

    def test_missing_mini_hash_rejected(self):
        del self.profile["mini_review"]["sha256"]
        self.write_profile()
        with self.assertRaisesRegex(lab.LabError, "sha256"):
            lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        self.assertTrue(lab.audit(self.root)[1])
        with self.assertRaises(lab.LabError):
            self.prepare()
        self.assertFalse((self.base / "run").exists())

    def test_invalid_mini_hash_rejected(self):
        for value in (None, 123, [], {}, "", "a" * 63, "a" * 65, "g" * 64, "A" * 64):
            with self.subTest(value=value):
                self.profile["mini_review"]["sha256"] = value
                with self.assertRaisesRegex(lab.LabError, "sha256"):
                    lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def test_mismatched_mini_hash_rejected(self):
        self.profile["mini_review"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(lab.LabError, "verändert"):
            lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def test_optional_workshop_review_pins_the_reviewed_text(self):
        workshop = self.plugin / "fachgebiet-werkstatt.md"
        self.profile["workshop_review"] = {
            "verdict": "revised",
            "reason": "Kompakter, individuell geprüfter Werkstattweg",
            "changes": ["Wiederholte Gerüste entfernt"],
            "sha256": lab.digest(workshop.read_bytes()),
        }
        lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        workshop.write_text("Ungeprüfte Änderung", encoding="utf-8")
        with self.assertRaisesRegex(lab.LabError, "Werkstatt-Prüfung.*verändert"):
            lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def test_changed_mini_rejected_for_new_runs(self):
        (self.plugin / "fachgebiet-schnellstart.md").write_text("Neuer Arbeitsweg", encoding="utf-8")
        with self.assertRaisesRegex(lab.LabError, "verändert"):
            self.prepare()
        self.assertFalse((self.base / "run").exists())

    def add_focus_review(self):
        self.profile["selection"]["target_skill"] = "belegabgleich"
        review = {"reviewed_on": "2026-09-14", "method": "desk_review",
                  "verdict": "retained", "reason": "Belegabgleich bis zum Dokument gelesen",
                  "changes": []}
        for kind, relative in (("prompt", "fachgebiet-hauptproblem.md"),
                               ("skill", "skills/belegabgleich/SKILL.md")):
            path = self.plugin / relative
            review[f"{kind}_path"] = path.relative_to(self.root).as_posix()
            review[f"{kind}_sha256"] = lab.digest(path.read_bytes())
        self.profile["focus_review"] = review
        return review

    def test_optional_focus_review_and_legacy_profile(self):
        lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        self.add_focus_review()
        lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        self.write_profile()
        self.assertEqual(lab.audit(self.root)[1], [])
        self.assertIn("Nicht ausgeführt", lab.catalog(lab.audit(self.root)[0], self.root))

    def add_editorial_review(self):
        self.add_focus_review()
        self.profile["workshop_review"] = {
            **self.profile["mini_review"],
            "sha256": lab.digest((self.plugin / "fachgebiet-werkstatt.md").read_bytes()),
        }
        review = {
            "date": "2026-09-14",
            "files": [f"fachgebiet/fachgebiet-{kind}.md" for kind in
                      ("schnellstart", "werkstatt", "hauptproblem")],
            "opening_change": "Bankgebühr und Zahlung im Einstieg unterscheiden.",
            "norms": ["Paragraf 362 BGB"],
            "decisions": [{"citation": "Quellenbezeichnung für den technischen Test",
                           "url": "https://example.invalid/entscheidung",
                           "application": "Zuordnung des belegten Zahlungseingangs.",
                           "limit": "Keine Feststellung über den konkreten Vertrag."}],
            "remaining_limits": ["Nur technische Prüfung des Datenschemas."],
        }
        self.profile["prompt_editorial_review"] = review
        return review

    def test_editorial_review_covers_all_prompt_variants(self):
        review = self.add_editorial_review()
        lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        for name in review["files"][:]:
            with self.subTest(name=name):
                review["files"].remove(name)
                with self.assertRaises(lab.LabError):
                    lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
                review["files"].append(name)

    def test_editorial_review_cannot_replace_hash_bound_reviews(self):
        self.add_editorial_review()
        for key in ("workshop_review", "focus_review"):
            with self.subTest(key=key):
                original = self.profile.pop(key)
                with self.assertRaises(lab.LabError):
                    lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
                self.profile[key] = original

    def test_editorial_review_rejects_incomplete_or_unsafe_metadata(self):
        valid = copy.deepcopy(self.add_editorial_review())
        for field, values in {
            "date": [None, "9999-01-01", "2026-02-30"],
            "norms": [None, [], [""]],
            "files": [[], ["../external.md"], ["missing.md"]],
            "decisions": [[], [None], [{"citation": "Nur ein Aktenzeichen"}]],
            "opening_change": [None, ""],
        }.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.profile["prompt_editorial_review"] = {**valid, field: value}
                    with self.assertRaises(lab.LabError):
                        lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        for field in ("application", "limit", "url"):
            review = copy.deepcopy(valid)
            review["decisions"][0][field] = ""
            self.profile["prompt_editorial_review"] = review
            with self.assertRaises(lab.LabError):
                lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

        for url in ("http://example.invalid/decision", "https:///decision",
                    "https://user:password@example.invalid/decision", "file:///local/decision"):
            with self.subTest(url=url):
                review = copy.deepcopy(valid)
                review["decisions"][0]["url"] = url
                self.profile["prompt_editorial_review"] = review
                with self.assertRaises(lab.LabError):
                    lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def test_editorial_review_does_not_assert_model_success(self):
        self.add_editorial_review()
        self.write_profile()
        profiles, errors = lab.audit(self.root)
        self.assertEqual(errors, [])
        self.assertIn("Nicht ausgeführt", lab.catalog(profiles, self.root))

    def test_editorial_audit_requires_review_without_changing_legacy_mode(self):
        self.write_profile()
        self.assertEqual(lab.audit(self.root)[1], [])
        profiles, errors = lab.audit(self.root, require_editorial=True)
        self.assertEqual(profiles, {})
        self.assertEqual(errors, ["fachgebiet: Fachbezogene Prompt-Redaktion fehlt"])
        self.add_editorial_review()
        self.write_profile()
        self.assertEqual(lab.audit(self.root, require_editorial=True)[1], [])
        (self.plugin / "fachgebiet-werkstatt.md").write_text("Ungeprüft geändert", encoding="utf-8")
        self.assertTrue(lab.audit(self.root, require_editorial=True)[1])

    def test_focus_review_pins_both_files(self):
        review = self.add_focus_review()
        for kind in ("prompt", "skill"):
            with self.subTest(kind=kind):
                path = self.root / review[f"{kind}_path"]
                original = path.read_bytes()
                path.write_bytes(original + b"\n")
                with self.assertRaisesRegex(lab.LabError, "Schwerpunkt.*verändert"):
                    lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
                path.write_bytes(original)

    def test_workflow_review_requires_individual_modes_and_hashed_editorial_review(self):
        self.add_editorial_review()
        self.write_profile()
        self.assertIn("Workflow-Prüfung fehlt", lab.audit(self.root, require_workflow=True)[1][0])
        review = {"date": "2026-09-23", "method": "desk_review",
                  "opening_modes": ["Zahlung ohne Beleg klären", "Bankunterlagen ohne Auftrag einordnen", "Verlangtes Schreiben beginnen"],
                  "continuation": "Nach Gutschrift den Restbetrag und das Schreiben nachführen.",
                  "enrichment": "Tilgungszuordnung vor dem nächsten Schreiben prüfen.",
                  "limits": "Keine beobachtete Modellausführung."}
        self.profile["prompt_workflow_review"] = review
        self.write_profile()
        self.assertEqual(lab.audit(self.root, require_workflow=True)[1], [])
        for field, invalid in (("method", "live"), ("opening_modes", []), ("date", "2026-02-30"),
                               ("continuation", ""), ("enrichment", ""), ("limits", None)):
            with self.subTest(field=field):
                self.profile["prompt_workflow_review"] = {**review, field: invalid}
                with self.assertRaises(lab.LabError):
                    lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        self.profile["prompt_workflow_review"] = review
        del self.profile["prompt_editorial_review"]
        self.write_profile()
        self.assertTrue(lab.audit(self.root, require_workflow=True)[1])

    def test_focus_review_rejects_invalid_metadata(self):
        valid = copy.deepcopy(self.add_focus_review())
        invalid = {"method": [None, "live", "model_evaluation", []],
                   "reviewed_on": [None, "2026-02-30", "9999-01-01", "20260914"],
                   "reason": [None, " ", []], "verdict": ["pass", "certified", []],
                   "changes": [None, [""]],
                   "prompt_sha256": [None, "A" * 64, "0" * 64],
                   "skill_sha256": [None, "a" * 63, "0" * 64]}
        for field, values in invalid.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.profile["focus_review"] = {**valid, field: value}
                    with self.assertRaises(lab.LabError):
                        lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        for value in (None, [], "reviewed", {}):
            self.profile["focus_review"] = value
            with self.assertRaises(lab.LabError):
                lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def test_focus_review_requires_exact_paths_and_target(self):
        review = self.add_focus_review()
        for kind in ("prompt", "skill"):
            key = f"{kind}_path"
            original = review[key]
            for value in (None, "other/" + original, "./" + original,
                          str(self.root / original), "fachgebiet/../" + original,
                          review["skill_path" if kind == "prompt" else "prompt_path"]):
                with self.subTest(kind=kind, path=value):
                    review[key] = value
                    with self.assertRaises(lab.LabError):
                        lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
            review[key] = original
        del self.profile["selection"]["target_skill"]
        with self.assertRaisesRegex(lab.LabError, "selection.target_skill"):
            lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def test_focus_review_rejects_missing_file_and_external_symlink(self):
        review = self.add_focus_review()
        path = self.root / review["prompt_path"]
        content = path.read_bytes()
        path.unlink()
        with self.assertRaisesRegex(lab.LabError, "Datei fehlt"):
            lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)
        outside = self.base / "outside.md"
        outside.write_bytes(content)
        path.symlink_to(outside)
        with self.assertRaisesRegex(lab.LabError, "Symlink"):
            lab.validate_profile(self.profile, "fachgebiet", self.plugin, self.root)

    def test_malformed_nested_profile_is_reported_by_audit(self):
        edits = (
            lambda p: p.update(mini_review=None),
            lambda p: p["mini_review"].update(verdict=[]),
            lambda p: p.update(selection=[]),
            lambda p: p.update(sources=None),
            lambda p: p.update(sources=[None]),
            lambda p: p.update(sources=[{"url": []}]),
            lambda p: p.update(cases=[None]),
            lambda p: p["cases"][0].update(id=[]),
            lambda p: p["cases"][0].update(target_skill=None),
            lambda p: p["cases"][0].update(criteria=[None, None, None]),
        )
        for index, edit in enumerate(edits):
            with self.subTest(index=index):
                profile = copy.deepcopy(self.profile)
                edit(profile)
                lab.save(self.root / "quality/evals/fachgebiet.json", profile)
                with self.assertRaises(lab.LabError):
                    lab.validate_profile(profile, "fachgebiet", self.plugin, self.root)
                profiles, errors = lab.audit(self.root)
                self.assertEqual(profiles, {})
                self.assertEqual(len(errors), 1)
                self.assertTrue(errors[0].startswith("fachgebiet:"))

    def test_no_result_is_unreviewed(self):
        run = self.prepare()
        result, _, _ = lab.inspect_run(run, self.root)
        self.assertEqual(result["status"], "unreviewed")
        self.assertGreaterEqual(len(result["findings"]), 2)

    def test_clean_question_turn_without_document_is_not_completion(self):
        for reason in lab.CLEAN_ENDS:
            with self.subTest(reason=reason):
                run = self.prepare("question-" + reason)
                lab.save(run / "metrics.json", {**self.metrics, "finish_reason": reason})
                (run / "output/rueckfrage.md").write_text(
                    "Sind die 100 Euro als Gebühr bestätigt oder noch ungeklärt?", encoding="utf-8")
                caller = Mock()
                result = lab.evaluate(run, self.config, root=self.root, caller=caller)
                self.assertEqual(result["status"], "unreviewed")
                caller.assert_not_called()
                self.assertFalse((run / "scores_dual.json").exists())

    def test_preparation_preserves_individual_followup_and_export_rules(self):
        instruction = (
            "# 1. Buchungsabgleich\n\n"
            "Frage bei einer ungeklärten Differenz nach dem Gebührenbeleg. "
            "Wenn die Antwort stattdessen eine Teilzahlung nennt, verlange deren Buchungsdatum. "
            "Übernimm die Nachreichung in den abschließenden Vermerk. "
            "Ohne Export liefere den vollständigen Text hier, keinen erfundenen Dateilink.\n"
        )
        (self.plugin / "fachgebiet-werkstatt.md").write_text(instruction, encoding="utf-8")
        run = self.prepare("followup-instructions", "werkstatt")
        self.assertEqual((run / "input/instructions.md").read_bytes(), instruction.encode("utf-8"))
        actual = (run / "input/request.txt").read_text(encoding="utf-8")
        self.assertTrue(actual.startswith(self.profile["cases"][0]["request"]))
        for criterion in self.profile["cases"][0]["criteria"]:
            self.assertNotIn(criterion["text"], actual)

    def test_recorded_followups_and_revised_document_reach_both_judges(self):
        """Prüft Übergabe und Neubewertung mit Testdoubles, keinen Live-Dialog."""
        case = self.profile["cases"][0]
        case["request"] = (
            "Erstelle ergebnis.md als abschließenden internen Buchungsvermerk. "
            "Beschriebener Vorverlauf: Auf die Nachricht über 400 Euro Überweisung und "
            "300 Euro Gutschrift wurde nach der Differenz gefragt. Antwort: Die Bank hat "
            "100 Euro Gebühren schriftlich bestätigt. Zweite Rückfrage: Gab es eine "
            "Gebührenerstattung oder spätere Gutschrift? Antwort: Nein, der endgültige "
            "Auszug bestätigt weiterhin 300 Euro Gutschrift. Übernimm beide Antworten "
            "in den Vermerk; weitere Unterlagen sind für diesen Zahlenabgleich nicht nötig."
        )
        case["criteria"] = [
            {"id": "C01", "text": "Überweisung von 400 Euro und Gutschrift von 300 Euro werden getrennt dargestellt.", "deliverables": ["ergebnis.md"]},
            {"id": "C02", "text": "Die bestätigten 100 Euro Gebühren erklären die Differenz; eine Erstattung wird nicht erfunden.", "deliverables": ["ergebnis.md"]},
            {"id": "C03", "text": "Beide nachgereichten Antworten werden im abschließenden Vermerk verarbeitet statt erneut erfragt.", "deliverables": ["ergebnis.md"]},
        ]
        self.write_profile()
        run = self.prepare("recorded-followups")
        lab.save(run / "metrics.json", {**self.metrics, "finish_reason": "no_tool_calls"})
        question = "Bitte bestätigen Sie noch einmal, ob die 100 Euro Gebühren sind."
        final = (
            "# 1. Abschließender Buchungsvermerk\n\n"
            "Die Überweisung beträgt 400 Euro. Gutgeschrieben wurden 300 Euro. "
            "Die Bankbestätigung ordnet die Differenz von 100 Euro den Gebühren zu. "
            "Nach der zweiten Auskunft gab es weder eine Erstattung noch eine spätere "
            "Gutschrift. Damit sind 400 Euro abzüglich 100 Euro gleich 300 Euro abgestimmt.\n"
        )
        output = run / "output/ergebnis.md"
        output.write_text(question, encoding="utf-8")
        inspection, _, _ = lab.inspect_run(run, self.root)
        # Lesbarkeit ist nur die Eintrittsbedingung zur fachlichen Bewertung.
        self.assertEqual(inspection["status"], "ready_for_judging")
        self.assertNotIn("all_pass", inspection)

        for expected_output, verdict in ((question, "fail"), (final, "pass")):
            with self.subTest(verdict=verdict):
                output.write_text(expected_output, encoding="utf-8")
                if verdict == "pass":
                    with self.assertRaisesRegex(lab.LabError, "Veralteter Bewertungsstand"):
                        lab.compare([run], self.root)
                seen = []

                def recorded_judge(judge, prompt):
                    payload = json.loads(prompt.split("\n", 1)[1])
                    self.assertEqual(payload["request"], case["request"])
                    self.assertEqual(payload["outputs"], {"ergebnis.md": expected_output})
                    self.assertIn(payload["criterion"], [c["text"] for c in case["criteria"]])
                    seen.append((judge["id"], payload["criterion"]))
                    return json.dumps({"reasoning": "Vorab festgelegtes Testurteil für die technische Zustandsprüfung.",
                                       "verdict": verdict, "evidence": expected_output})

                result = lab.evaluate(run, self.config, root=self.root, caller=recorded_judge)
                self.assertEqual(result["status"], "passed" if verdict == "pass" else "failed")
                self.assertEqual(len(set(seen)), 6)
                self.assertEqual(result["source_verification"], "not_independently_verified")

    def test_all_modes_prepare(self):
        for mode in lab.MODES:
            with self.subTest(mode=mode):
                run = self.prepare(mode, mode)
                self.assertEqual(lab.load(run / "run.json")["mode"], mode)

    def test_existing_run_not_overwritten(self):
        self.prepare()
        with self.assertRaises(lab.LabError):
            self.prepare()

    def test_reserved_input_names_cannot_replace_task(self):
        for name in ("request.txt", "instructions.md"):
            with self.subTest(name=name):
                (self.root / name).write_text("Fremder Inhalt", encoding="utf-8")
                self.profile["cases"][0]["input_files"] = [name]
                self.write_profile()
                with self.assertRaises(lab.LabError):
                    self.prepare()
                self.assertFalse((self.base / "run").exists())

    def test_in_repo_run_rejected(self):
        with self.assertRaises(lab.LabError):
            lab.prepare("fachgebiet", "kontostand", "baseline", self.root / "run", self.root)

    def test_path_and_symlink_escape(self):
        for name in ("../secret", "/secret", "a\\b"):
            with self.subTest(name=name), self.assertRaises(lab.LabError):
                lab.inside(self.root, name)
        (self.root / "escape").symlink_to(self.base)
        with self.assertRaises(lab.LabError):
            lab.inside(self.root, "escape/secret")

    def test_modified_input_rejected(self):
        run = self.ready()
        (run / "input/request.txt").write_text("Andere Aufgabe")
        with self.assertRaises(lab.LabError):
            lab.inspect_run(run, self.root)

    def test_changed_criterion_rejected(self):
        run = self.ready()
        self.profile["cases"][0]["criteria"][0]["text"] = "Andere fachliche Bewertung"
        self.write_profile()
        with self.assertRaises(lab.LabError):
            lab.inspect_run(run, self.root)

    def test_added_input_invalidates_inspection_and_comparison(self):
        for kind in ("file", "directory", "symlink"):
            with self.subTest(kind=kind):
                run = self.ready("added-" + kind)
                lab.evaluate(run, self.config, root=self.root, caller=self.passing)
                extra = run / "input/zusatz"
                if kind == "file":
                    extra.write_text("Nachträgliche Anweisung", encoding="utf-8")
                elif kind == "directory":
                    extra.mkdir()
                    (extra / "anweisung.txt").write_text("Zusatz", encoding="utf-8")
                else:
                    extra.symlink_to(run / "input/request.txt")
                with self.assertRaisesRegex(lab.LabError, "Eingabebestand"):
                    lab.inspect_run(run, self.root)
                with self.assertRaises(lab.LabError):
                    lab.compare([run], self.root)
                caller = Mock(side_effect=self.passing)
                with self.assertRaises(lab.LabError):
                    lab.evaluate(run, self.config, root=self.root, caller=caller)
                caller.assert_not_called()
                self.assertFalse((run / "scores_dual.json").exists())

    def test_metadata_change_does_not_invalidate_fixed_case(self):
        run = self.ready()
        self.profile["mini_review"]["reason"] = "Erneut fachlich geprüft"
        self.write_profile()
        self.assertEqual(lab.inspect_run(run, self.root)[0]["status"], "ready_for_judging")

    def test_historical_run_does_not_depend_on_current_mini(self):
        run = self.ready()
        lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        frozen = lab.inspect_run(run, self.root)[0]["run_fingerprint"]
        mini = self.plugin / "fachgebiet-schnellstart.md"
        mini.write_text("Später überarbeiteter Arbeitsweg", encoding="utf-8")
        self.assertTrue(lab.audit(self.root)[1])
        self.assertEqual(lab.inspect_run(run, self.root)[0]["run_fingerprint"], frozen)
        self.assertEqual(lab.compare([run], self.root)["groups"][0]["strict_pass_rate"], 1)
        self.assertTrue(lab.evaluate(run, self.config, root=self.root, caller=self.passing)["all_pass"])
        self.profile["mini_review"]["sha256"] = lab.digest(mini.read_bytes())
        self.write_profile()
        self.assertEqual(lab.audit(self.root)[1], [])
        self.assertTrue(lab.evaluate(run, self.config, root=self.root, caller=self.passing)["all_pass"])
        self.assertEqual(lab.inspect_run(run, self.root)[0]["run_fingerprint"], frozen)

    def test_aborted_run_cannot_be_judged(self):
        for reason in lab.ENDS - lab.CLEAN_ENDS:
            with self.subTest(reason=reason):
                run = self.ready(reason)
                lab.save(run / "metrics.json", {**self.metrics, "finish_reason": reason})
                result = lab.evaluate(run, self.config, root=self.root, caller=self.passing)
                self.assertEqual(result["status"], "unreviewed")
                self.assertFalse((run / "scores_dual.json").exists())

    def test_two_passes_required(self):
        run = self.ready()
        result = lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        self.assertTrue(result["all_pass"])
        self.assertEqual(result["source_verification"], "not_independently_verified")
        self.assertEqual(len(result["judges"]), 2)

    def test_disagreement_is_not_pass(self):
        def caller(judge, prompt):
            return self.passing(judge, prompt) if judge["id"] == "pruefer-eins" else json.dumps({"reasoning": "Zuordnung nicht ausreichend.", "verdict": "fail", "evidence": "Zuordnung fehlt"})
        result = lab.evaluate(self.ready(), self.config, root=self.root, caller=caller)
        self.assertEqual(result["dual_all_pass_rate"], 0.5)
        self.assertFalse(result["all_pass"])
        self.assertEqual(result["status"], "needs_review")

    def test_unknown_is_not_pass(self):
        caller = lambda *_: json.dumps({"reasoning": "Nicht belegt", "verdict": "unreviewed", "evidence": "Quellennachweis fehlt"})
        result = lab.evaluate(self.ready(), self.config, root=self.root, caller=caller)
        self.assertEqual(result["status"], "unreviewed")

    def test_failed_regrade_removes_stale_aggregate(self):
        run = self.ready()
        lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        def caller(judge, prompt):
            if judge["id"] == "pruefer-zwei":
                raise TimeoutError("secret access token must not appear in the artifact")
            return self.passing(judge, prompt)
        with self.assertRaises(lab.LabError):
            lab.evaluate(run, self.config, root=self.root, caller=caller)
        self.assertFalse((run / "scores_dual.json").exists())
        text = (run / "scores_pruefer-zwei.json").read_text()
        self.assertNotIn("secret access", text)
        self.assertEqual(lab.load(run / "scores_pruefer-eins.json")["status"], "complete")

    def test_missing_file_invalidates_previous_pass(self):
        run = self.ready()
        lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        (run / "output/ergebnis.md").unlink()
        self.assertEqual(lab.evaluate(run, self.config, root=self.root, caller=self.passing)["status"], "unreviewed")
        self.assertFalse((run / "scores_dual.json").exists())

    def test_reserved_judge_id_cannot_leave_positive_aggregate(self):
        for index in (0, 1):
            with self.subTest(index=index):
                run = self.ready("reserved-" + str(index))
                lab.evaluate(run, self.config, root=self.root, caller=self.passing)
                config = copy.deepcopy(self.config)
                config["judges"][index]["id"] = "dual"
                with self.assertRaisesRegex(lab.LabError, "reserviert"):
                    lab.validate_judges(config)
                caller = Mock(side_effect=self.passing)
                with self.assertRaises(lab.LabError):
                    lab.evaluate(run, config, root=self.root, caller=caller)
                caller.assert_not_called()
                self.assertFalse((run / "scores_dual.json").exists())

    def test_remote_requires_explicit_permission(self):
        with self.assertRaises(lab.LabError):
            lab.evaluate(self.ready(), self.config, root=self.root)

    def test_fake_evidence_and_nonboolean_truth_rejected(self):
        for value in ({"reasoning": "Ja", "verdict": "pass", "evidence": "Nicht im Dokument"},
                      {"reasoning": "Ja", "verdict": True, "evidence": "400"},
                      {"reasoning": "Ja", "verdict": "pass", "evidence": ""}):
            with self.subTest(value=value), self.assertRaises(lab.LabError):
                lab.parse_verdict(json.dumps(value), "400")

    def test_duplicate_keys_and_nan_rejected(self):
        for raw in ('{"verdict":"fail","verdict":"pass"}', '{"n":NaN}'):
            with self.assertRaises(lab.LabError):
                lab.decode(raw)

    def test_invalid_judge_config(self):
        for edit in (lambda c: c["judges"].pop(), lambda c: c["judges"][1].update(model="modell-eins"),
                     lambda c: c["judges"][0].update(endpoint="http://example.invalid"),
                     lambda c: c["judges"][0].update(endpoint="https://user:password@example.invalid")):
            c = copy.deepcopy(self.config)
            edit(c)
            with self.assertRaises(lab.LabError):
                lab.validate_judges(c)

    def test_unknown_tokens_not_zero(self):
        run = self.ready()
        lab.save(run / "metrics.json", {**self.metrics, "input_tokens": None, "output_tokens": None})
        lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        result = lab.compare([run], self.root)
        self.assertIsNone(result["groups"][0]["tokens_mean"])

    def test_bad_metrics_rejected(self):
        for value in (-1, float("inf"), True):
            with self.subTest(value=value), self.assertRaises(lab.LabError):
                lab.validate_metrics({**self.metrics, "duration_ms": value})

    def test_modified_output_invalidates_comparison(self):
        run = self.ready()
        lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        (run / "output/ergebnis.md").write_text("Andere Zahlen")
        with self.assertRaises(lab.LabError):
            lab.compare([run], self.root)

    def test_fake_pdf_not_accepted(self):
        path = self.base / "datei.pdf"
        path.write_text("Nur eine umbenannte Textdatei")
        with self.assertRaises(lab.LabError):
            lab.read_artifact(path)

    def test_duplicate_run_and_symlink_alias_rejected(self):
        run = self.ready()
        lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        alias = self.base / "run-alias"
        alias.symlink_to(run, target_is_directory=True)
        for duplicate in (run, alias):
            with self.subTest(duplicate=duplicate), self.assertRaisesRegex(lab.LabError, "mehrfach"):
                lab.compare([run, duplicate], self.root)

    def test_distinct_repetitions_remain_comparable(self):
        runs = [self.ready("repeat-" + str(i)) for i in range(2)]
        for run in runs:
            lab.evaluate(run, self.config, root=self.root, caller=self.passing)
        groups = lab.compare(runs, self.root)["groups"]
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["runs"], 2)

    def test_different_cases_never_share_aggregates(self):
        second = copy.deepcopy(self.profile["cases"][0])
        second["id"] = "gebuehren"
        second["request"] += " Prüfe zusätzlich den Buchungstag."
        self.profile["cases"].append(second)
        self.write_profile()
        for mode in ("plugin", "schnellstart", "baseline"):
            runs = []
            for case in self.profile["cases"]:
                run = self.base / (mode + case["id"])
                with patch.object(lab.subprocess, "check_output", return_value="revision\n"):
                    lab.prepare("fachgebiet", case["id"], mode, run, self.root)
                lab.save(run / "metrics.json", self.metrics)
                (run / "output/ergebnis.md").write_text("400 Euro Zahlung", encoding="utf-8")
                lab.evaluate(run, self.config, root=self.root, caller=self.passing)
                runs.append(run)
            groups = lab.compare(runs, self.root)["groups"]
            self.assertEqual(len(groups), 2, mode)
            self.assertEqual(len({g["case_hash"] for g in groups}), 2)
            self.assertTrue(all(g["runs"] == 1 for g in groups))

    def test_broken_office_artifacts_remain_unreviewed(self):
        from openpyxl import Workbook
        for suffix in ("docx", "xlsx"):
            for damage in ("zip", "xml"):
                with self.subTest(suffix=suffix, damage=damage):
                    name = "ergebnis." + suffix
                    case = self.profile["cases"][0]
                    case["deliverables"] = [name]
                    for criterion in case["criteria"]:
                        criterion["deliverables"] = [name]
                    self.write_profile()
                    run = self.prepare(suffix + damage)
                    lab.save(run / "metrics.json", self.metrics)
                    path = run / "output" / name
                    if damage == "zip":
                        path.write_bytes(b"PK truncated archive")
                    elif suffix == "docx":
                        with ZipFile(path, "w") as archive:
                            archive.writestr("word/document.xml", "<document>")
                    else:
                        buffer = io.BytesIO()
                        book = Workbook()
                        book.active["A1"] = "Zahlung"
                        book.save(buffer)
                        book.close()
                        with ZipFile(buffer) as original, ZipFile(path, "w") as archive:
                            for entry in original.namelist():
                                archive.writestr(entry, b"<worksheet>" if entry == "xl/worksheets/sheet1.xml" else original.read(entry))
                    inspection = lab.inspect_run(run, self.root)[0]
                    self.assertEqual(inspection["status"], "unreviewed")
                    self.assertTrue(any(name in finding for finding in inspection["findings"]))
                    caller = Mock(side_effect=AssertionError("Unreadable output must not be judged"))
                    result = lab.evaluate(run, self.config, root=self.root, caller=caller)
                    self.assertEqual(result["status"], "unreviewed")
                    caller.assert_not_called()

    def test_context_limit_is_checked_while_reading(self):
        with self.assertRaises(lab.LabError):
            lab.bounded_text(iter(["a" * lab.MAX_CONTEXT, "b"]))

    def test_oversized_spreadsheet_dimensions_rejected_before_rows(self):
        sheet = Mock(max_row=1048576, max_column=16384, title="Blatt")
        with self.assertRaises(lab.LabError):
            lab.bounded_text(lab.workbook_text(Mock(worksheets=[sheet])))
        sheet.iter_rows.assert_not_called()

    def test_remote_protocols_require_complete_responses(self):
        answers = {
            "messages": {"stop_reason": "end_turn", "content": [{"type": "text", "text": "answer"}]},
            "responses": {"status": "completed", "output": [{"content": [{"type": "output_text", "text": "answer"}]}]},
            "chat-completions": {"choices": [{"finish_reason": "stop", "message": {"content": "answer"}}]},
        }
        for protocol, answer in answers.items():
            judge = {**self.config["judges"][0], "protocol": protocol}
            opener = Mock()
            opener.open.return_value = io.BytesIO(json.dumps(answer).encode())
            with self.subTest(protocol=protocol), patch.dict(lab.os.environ, {judge["key_env"]: "private-key"}), patch.object(lab, "build_opener", return_value=opener):
                self.assertEqual(lab.remote_judge(judge, "request"), "answer")
                request = opener.open.call_args.args[0]
                self.assertNotIn("private-key", request.data.decode())
                self.assertEqual(opener.open.call_args.kwargs["timeout"], 45)
                self.assertEqual(json.loads(request.data)["model"], judge["model"])

    def test_remote_incomplete_and_empty_responses_never_pass(self):
        for answer in ({"choices": []}, {"choices": [{"finish_reason": "length", "message": {"content": "answer"}}]}, []):
            judge = {**self.config["judges"][0], "protocol": "chat-completions"}
            opener = Mock()
            opener.open.return_value = io.BytesIO(json.dumps(answer).encode())
            with patch.dict(lab.os.environ, {judge["key_env"]: "private-key"}), patch.object(lab, "build_opener", return_value=opener), self.assertRaises(lab.LabError):
                lab.remote_judge(judge, "request")

    def test_remote_timeout_has_finite_retry_budget(self):
        judge = self.config["judges"][0]
        opener = Mock()
        opener.open.side_effect = TimeoutError("private transport details")
        with patch.dict(lab.os.environ, {judge["key_env"]: "private-key"}), patch.object(lab, "build_opener", return_value=opener), patch.object(lab.time, "sleep"), self.assertRaises(lab.LabError):
            lab.remote_judge(judge, "request")
        self.assertEqual(opener.open.call_count, 3)

    def test_credentials_not_forwarded_on_redirect(self):
        with self.assertRaises(lab.LabError):
            lab.NoRedirect().redirect_request(None, None, 302, "", {}, "https://elsewhere.invalid/")

    def test_selection_export_has_no_answer_labels(self):
        result = lab.selection_requests("fachgebiet", self.root)
        self.assertEqual(len(result["requests"]), 4)
        self.assertNotIn("positive", json.dumps(result))

    def test_selection_tracks_false_positive_and_missing_runs(self):
        exported = lab.selection_requests("fachgebiet", self.root)
        result = lab.score_selection({"plugin": "fachgebiet", "client": "client", "model": "model",
                                      "selection_hash": exported["selection_hash"], "observations": [
                                          {"id": next(r["id"] for r in exported["requests"] if r["request"] in self.profile["selection"]["negative"]), "status": "completed", "selected_skills": ["fachgebiet/belegabgleich"]}]}, self.root)
        self.assertEqual(result["counts"]["false_positive"], 1)
        self.assertEqual(result["status"], "unreviewed")
        self.assertEqual(len(result["pending"]), 3)

    def test_selection_all_four_observed(self):
        exported = lab.selection_requests("fachgebiet", self.root)
        observations = [{"id": r["id"], "status": "completed", "selected_skills": ["fachgebiet/belegabgleich"] if r["request"] in self.profile["selection"]["positive"] else []} for r in exported["requests"]]
        result = lab.score_selection({**exported, "client": "client", "model": "model", "observations": observations}, self.root)
        self.assertEqual(result["status"], "passed")

    def test_focus_selection_allows_other_skills_for_adjacent_tasks(self):
        other = self.plugin / "skills/nachbaraufgabe"
        other.mkdir()
        (other / "SKILL.md").write_text("Andere Fachaufgabe", encoding="utf-8")
        self.profile["selection"]["target_skill"] = "belegabgleich"
        self.write_profile()
        exported = lab.selection_requests("fachgebiet", self.root)
        observations = [{"id": r["id"], "status": "completed", "selected_skills": ["fachgebiet/belegabgleich" if r["request"] in self.profile["selection"]["positive"] else "fachgebiet/nachbaraufgabe"]} for r in exported["requests"]]
        result = lab.score_selection({**exported, "client": "client", "model": "model", "observations": observations}, self.root)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["evaluation_kind"], "observed_skill_selection")
        self.assertEqual(result["counts"]["true_negative"], 2)

    def test_completed_selection_requires_observed_skills(self):
        exported = lab.selection_requests("fachgebiet", self.root)
        observations = [{"id": r["id"], "status": "completed", "selected_skills": ["fachgebiet/belegabgleich"]}
                        if r["request"] in self.profile["selection"]["positive"]
                        else {"id": r["id"], "status": "completed"} for r in exported["requests"]]
        with self.assertRaisesRegex(lab.LabError, "Beobachtete Skills"):
            lab.score_selection({**exported, "client": "client", "model": "model", "observations": observations}, self.root)

    def test_legacy_skipped_review_is_not_all_pass(self):
        spec = importlib.util.spec_from_file_location("legacy_eval_test", Path(__file__).with_name("run-eval.py"))
        module = importlib.util.module_from_spec(spec)
        import sys
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        result = module.AktenResult("akte", True, [module.CheckResult("a", "file_exists", "vorhanden", True), module.CheckResult("b", "human_review", "offen", None)])
        self.assertTrue(result.structural_passed)
        self.assertFalse(result.all_passed)


if __name__ == "__main__":
    unittest.main()
