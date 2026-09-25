#!/usr/bin/env python3
"""Offline-Tests gegen den Verlust individueller Arbeitsabläufe.

Dateierhaltung und Generatorgrenzen, keine Bewertung erzeugter Fachantworten.
Alle Schreibversuche erfolgen in temporären Verzeichnissen.
"""

import importlib.util
import io
import json
from contextlib import redirect_stdout
from dataclasses import replace
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import quality_lab as lab
from themen_profile import PROFILE_BY_KEY


SCRIPTS = Path(__file__).resolve().parent


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


G = module("workflow_generator", "generate-werkstatt-und-schnellstart-prompts.py")
R = module("workflow_refiner", "refine-speed-and-elegance.py")
A = module("workflow_routing_audit", "audit-prompt-profile-routing.py")
S = module("workflow_law_sentinels", "validate-current-law-sentinels.py")


class LosslessWorkshopTests(unittest.TestCase):
    def test_long_workshop_keeps_sources_products_and_continuation(self):
        sections = {
            "Musterbausteine": "Die Parteien vereinbaren [konkrete Leistung] zu [Bedingung].",
            "Qualitätskontrolle und Abschluss": "Nach Eingang des Belegs denselben Entwurf fertigstellen.",
            "Leitentscheidungen": "Belegte Entscheidung mit Fundstelle und enger Reichweite.",
            "Pflichtnormen": "Norm, Ausnahme und Übergangsrecht gemeinsam prüfen.",
            "Fachliche Entscheidungslandkarte": "Die Route endet im bestellten Dokument.",
            "Arbeitsweise": "Nur die betroffenen Belegstellen und Berechnungen fortschreiben.",
        }
        text = "# 1. Fachwerkstatt\n\n"
        for i, (heading, body) in enumerate(sections.items(), 1):
            text += f"## {i}. {heading}\n\n" + (body + "\n") * 700 + "\n"
        self.assertGreater(len(text.encode()), 128 * 1024)
        self.assertEqual(G.compact_werkstatt(text), text)
        self.assertEqual(G.compact_werkstatt(G.compact_werkstatt(text)), text)

    def test_oversized_workshop_fails_without_returning_a_truncated_document(self):
        with self.assertRaisesRegex(ValueError, "keine Inhalte gekürzt"):
            G.compact_werkstatt("x" * (G.MAX_WERKSTATT + 1))

    def test_norm_excerpt_keeps_following_exception_and_date(self):
        norm = (
            "BGB Paragraf 312g: Den Anwendungsbereich prüfen. "
            "Eine Ausnahme darf nicht durch den ersten Prüfsatz verdeckt werden. "
            "Den im Fall genannten Stand seit 1. Juli 2026 gesondert einordnen."
        )
        result = G.extract_norm_anchors([{"desc": norm}])
        self.assertEqual(result, [norm.rstrip(".")])

    def test_mini_selects_complete_anchors_instead_of_cutting_exceptions(self):
        anchors = [f"- BGB Paragraf {i}: " + "Sachverhalt und Anwendung prüfen. " * 5 + f"Ausnahme {i} vollständig beachten." for i in range(1, 9)]
        case = "- BGH, Urteil: Rechtsfolge nur nach verifizierter Fundstelle und begrenzter Aussage."
        text = (
            "# 1. Mini\n\n## 3. Kernroute\n\nDen bestellten Entwurf nach neuer Antwort fortschreiben.\n"
            "\n## 6. Anker\n\n" + "\n".join(anchors + [case]) +
            "\n\n## 7. Antwortform\n\nDas vollständige bestellte Dokument liefern.\n"
        )
        with patch.object(G, "MAX_FAST", 1100):
            result = G.compact_schnellstart(text)
        self.assertLessEqual(len(result.encode()), 1100)
        self.assertIn(case, result)
        for line in result.splitlines():
            if line.startswith("- "):
                self.assertIn(line, anchors + [case])
        self.assertIn("Den bestellten Entwurf nach neuer Antwort fortschreiben.", result)
        self.assertIn("Das vollständige bestellte Dokument liefern.", result)

    def test_workshop_keeps_curated_decisions_after_the_fifth(self):
        decisions = tuple(f"Testquelle {i}: Geltungsbereich und Grenze {i}." for i in range(8))
        profile = replace(PROFILE_BY_KEY["arbeits"], entscheidungen=decisions)
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(G, "manifest", return_value={"name": "fachgebiet", "description": "Fachliche Prüfung"}), \
                 patch.object(G, "profile_for", return_value=profile):
                text = G.build_werkstatt(Path(tmp), [])
        for decision in decisions:
            self.assertIn(decision, text)


class CitationSentinelTests(unittest.TestCase):
    def test_arag_name_is_not_part_of_paragraf(self):
        sentinel = next(item for item in S.SENTINELS if item.label.startswith("II ZR 331/00"))
        for text in (
            "II ZR 331/00: Außen-GbR; BGB Paragrafen 705 ff. berücksichtigen.",
            "Paragraf 705 BGB: II ZR 331/00.",
            "II ZR 331/00: Außen-GbR.\nII ZR 175/95: ARAG/Garmenbeck.",
        ):
            with self.subTest(text=text):
                self.assertIsNone(sentinel.pattern.search(text))
        for text in ("II ZR 331/00: ARAG/Garmenbeck", "ARAG-Garmenbeck, II ZR 331/00"):
            with self.subTest(text=text):
                self.assertIsNotNone(sentinel.pattern.search(text))


class WorkflowPreservation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # Der Marketplace-Name muss nicht dem Quellverzeichnis entsprechen.
        self.plugin = self.root / "paket"
        (self.plugin / ".claude-plugin").mkdir(parents=True)
        (self.plugin / ".claude-plugin/plugin.json").write_text(
            json.dumps({"name": "fachgebiet"}), encoding="utf-8")
        (self.plugin / "skills/belegabgleich").mkdir(parents=True)
        (self.plugin / "skills/belegabgleich/SKILL.md").write_text("Belege abgleichen.\n", encoding="utf-8")
        self.paths = {}
        for kind in ("schnellstart", "werkstatt", "hauptproblem"):
            path = self.plugin / f"fachgebiet-{kind}.md"
            text = (
                "# 1. Belegabgleich\n\n"
                "## 1.1. Rückfragen und Verzweigung\n\n"
                "Kläre zuerst, ob die Abweichung eine Gebühr oder eine Teilzahlung ist. "
                "Nach der Antwort fordere den dazu passenden Beleg an. "
                "Übernimm die Bestätigung in die Berechnung und den fertigen Vermerk.\n\n"
                "## 1.2. Schlusskontrolle für Tempo\n\n"
                "Nach Eingang des Buchungsbelegs ersetze die vorläufige Fassung.\n\n"
                "Ohne Export liefere den fertigen Text, keinen erfundenen Dateilink.\n\n"
                + "Unveränderte Belegstellen bleiben zugeordnet.\n" * 60
            )
            path.write_text(text, encoding="utf-8")
            self.paths[kind] = path
        self.before = {kind: path.read_bytes() for kind, path in self.paths.items()}

    def review(self):
        profile = {
            "schema_version": 1, "plugin": "fachgebiet", "reviewed_on": "2026-09-15",
            "sources": [],
            "mini_review": {"verdict": "retained", "reason": "Belege vor Abschluss abgleichen",
                            "changes": [], "sha256": lab.digest(self.before["schnellstart"])},
            "selection": {"positive": ["Kontoeingang abgleichen", "Gebührenbeleg zuordnen"],
                          "negative": ["Einladung übersetzen", "Termin abstimmen"]},
            "cases": [{"id": "kontobeleg", "target_skill": "belegabgleich",
                       "request": "Ein Auftrag über 400 Euro wurde überwiesen. Auf dem Konto wurden 300 Euro gutgeschrieben. Die Bank bestätigt 100 Euro Gebühren. Erstelle einen abschließenden Vermerk aus diesen Angaben.",
                       "input_files": [], "deliverables": ["ergebnis.md"],
                       "criteria": [
                           {"id": "C01", "text": "Zahlung und Gutschrift werden getrennt zugeordnet.", "deliverables": ["ergebnis.md"]},
                           {"id": "C02", "text": "Die Differenz wird mit der bestätigten Gebühr abgeglichen.", "deliverables": ["ergebnis.md"]},
                           {"id": "C03", "text": "Ein abschließender Vermerk statt einer bloßen Fragenliste wird geliefert.", "deliverables": ["ergebnis.md"]},
                       ]}],
        }
        lab.save(self.root / "quality/evals/fachgebiet.json", profile)

    def assert_preserved(self):
        self.assertEqual({kind: path.read_bytes() for kind, path in self.paths.items()}, self.before)

    def test_reviewed_workshop_is_protected_at_direct_write_boundary(self):
        self.review()
        with patch.object(G, "REPO", self.root), patch.object(G, "collect_skill_material") as collect:
            self.assertFalse(G.enrich_protected_werkstatt(self.plugin))
            collect.assert_not_called()
        self.assert_preserved()

    def test_curated_helpers_do_not_insert_new_workflow_rules(self):
        with patch.object(G, "REPO", self.root), patch.object(G, "load_protected", return_value={"fachgebiet"}):
            self.assertFalse(G.enrich_protected_werkstatt(self.plugin))
            self.assertFalse(G.normalize_protected_schnellstart(self.plugin))
        self.assert_preserved()

    def test_curated_main_does_not_enrich_or_normalize(self):
        with patch.object(G, "REPO", self.root), \
             patch.object(G, "plugin_dirs", return_value=[self.plugin]), \
             patch.object(G, "load_protected", return_value={"fachgebiet"}), \
             patch.object(G, "enrich_protected_werkstatt") as enrich, \
             patch.object(G, "normalize_protected_schnellstart") as normalize:
            self.assertEqual(G.main(), 0)
            enrich.assert_not_called()
            normalize.assert_not_called()
        self.assert_preserved()

    def test_stale_review_does_not_fall_back_to_generation(self):
        self.review()
        self.paths["schnellstart"].write_bytes(self.before["schnellstart"] + b"\n")
        with patch.object(G, "REPO", self.root), self.assertRaises(lab.LabError):
            G.enrich_protected_werkstatt(self.plugin)
        self.assertEqual(self.paths["werkstatt"].read_bytes(), self.before["werkstatt"])

    def test_refiner_protects_reviewed_paths_even_when_called_directly(self):
        self.review()
        with patch.object(R, "REPO", self.root):
            for kind in ("werkstatt", "schnellstart"):
                self.assertFalse(R.refine_prompt(self.paths[kind], kind))
        self.assert_preserved()

    def test_refiner_discovery_uses_manifest_name_for_review(self):
        self.review()
        with patch.object(R, "REPO", self.root), patch.object(R, "plugin_dirs", return_value=[self.plugin]):
            self.assertEqual(R.prompt_files("-werkstatt.md"), [])
            self.assertEqual(R.prompt_files("-schnellstart.md"), [])
        self.assert_preserved()

    def test_refiner_protects_curated_paths_without_review_profile(self):
        with patch.object(R, "REPO", self.root), patch.object(R, "hand_curated_slugs", return_value={"fachgebiet"}):
            for kind in ("werkstatt", "schnellstart"):
                self.assertFalse(R.refine_prompt(self.paths[kind], kind))
        self.assert_preserved()

    def test_refiner_does_not_replace_custom_sections_or_insert_defaults(self):
        with patch.object(R, "REPO", self.root):
            for kind in ("werkstatt", "schnellstart"):
                self.assertFalse(R.refine_prompt(self.paths[kind], kind))
                self.assertFalse(R.refine_prompt(self.paths[kind], kind))
        self.assert_preserved()

    def test_refiner_removes_only_exact_obsolete_block(self):
        path = self.paths["schnellstart"]
        before = path.read_text(encoding="utf-8")
        path.write_text(R.SCHNELLSTART_BLOCK + before, encoding="utf-8")
        with patch.object(R, "REPO", self.root):
            self.assertTrue(R.refine_prompt(path, "schnellstart"))
            self.assertEqual(path.read_text(encoding="utf-8"), before)
            self.assertFalse(R.refine_prompt(path, "schnellstart"))

    def test_refiner_rejects_stale_review_without_rewriting(self):
        self.review()
        self.paths["schnellstart"].write_bytes(self.before["schnellstart"] + b"\n")
        with patch.object(R, "REPO", self.root), self.assertRaises(lab.LabError):
            R.refine_prompt(self.paths["werkstatt"], "werkstatt")
        self.assertEqual(self.paths["werkstatt"].read_bytes(), self.before["werkstatt"])

    def test_compaction_never_drops_final_route_step(self):
        text = (
            "# Abgleich\n\n## 3. Kernroute\n\n"
            "1. Buchungen lesen.\n2. Abweichung nachfragen.\n"
            "3. Gebühren- oder Teilzahlungsbeleg anfordern.\n"
            "4. Neue Angaben in die Rechnung übernehmen.\n"
            "5. Den abschließenden Vermerk mit der korrigierten Rechnung ausformulieren.\n"
        )
        with patch.object(G, "MAX_FAST", G.byte_len(text) - 1), self.assertRaises(ValueError):
            G.compact_schnellstart(text)
        with patch.object(G, "MAX_FAST", G.byte_len(text)):
            self.assertEqual(G.compact_schnellstart(text), text)

    def test_compaction_never_drops_requested_product(self):
        text = "# Abgleich\n\nZielprodukt: Ein abschließender, ausformulierter Buchungsvermerk.\n"
        with patch.object(G, "MAX_FAST", G.byte_len(text) - 1), self.assertRaises(ValueError):
            G.compact_schnellstart(text)

    def test_size_failure_does_not_replace_either_existing_prompt(self):
        for kind in ("schnellstart", "werkstatt"):
            with self.subTest(kind=kind), patch.object(G, "REPO", self.root), \
                 patch.object(G, "plugin_dirs", return_value=[self.plugin]), \
                 patch.object(G, "load_protected", return_value=set()), \
                 patch.object(G, "collect_skill_material", return_value=[]), \
                 patch.object(G, "build_schnellstart", return_value="x" * (G.MAX_FAST + 1) if kind == "schnellstart" else "Mini\n"), \
                 patch.object(G, "build_werkstatt", return_value="x" * (G.MAX_WERKSTATT + 1) if kind == "werkstatt" else "Werkstatt\n"):
                self.assertEqual(G.main(), 1)
                self.assert_preserved()

    def routing_audit(self):
        with patch.object(A, "REPO", self.root), \
             patch.object(A, "marketplace_plugins", return_value=[("fachgebiet", self.plugin, "Belegabgleich")]), \
             patch.object(A, "profile_for", return_value=PROFILE_BY_KEY["arbeits"]), \
             patch.object(A, "protected_slugs", return_value=set()), \
             patch.object(A, "source_anchor_problems", return_value=[]), \
             redirect_stdout(io.StringIO()) as output:
            result = A.main()
        return result, output.getvalue()

    def test_routing_audit_accepts_short_individual_workflow_without_twelve_routes(self):
        self.review()
        self.assertLess(len(self.before["werkstatt"]), 12 * 1024)
        result, output = self.routing_audit()
        self.assertEqual(result, 0, output)
        self.assert_preserved()

    def test_routing_audit_still_rejects_stale_review_and_oversized_workshop(self):
        self.review()
        self.paths["schnellstart"].write_bytes(self.before["schnellstart"] + b"\n")
        result, output = self.routing_audit()
        self.assertEqual(result, 1)
        self.assertIn("individuelle Prüfung ungültig", output)
        self.paths["schnellstart"].write_bytes(self.before["schnellstart"])
        self.paths["werkstatt"].write_bytes(self.before["werkstatt"] + b"x" * G.MAX_WERKSTATT)
        result, output = self.routing_audit()
        self.assertEqual(result, 1)
        self.assertIn(f"höchstens {G.MAX_WERKSTATT} Bytes", output)

    def test_workshop_structure_rejects_empty_or_misnumbered_sections(self):
        for text in ("", "# Titel\n", "# Titel\n\n## 1. Auftrag\n\n", 
                     "# Titel\n\n## Auftrag\n\nBelege prüfen.\n",
                     "# Titel\n\n## 2. Abschluss\n\nVermerk.\n\n## 1. Eingang\n\nBelege.\n"):
            with self.subTest(text=text):
                self.assertTrue(A.individual_workshop_structure_problems(text))

    def test_routing_audit_validates_optional_workshop_hash(self):
        self.review()
        path = self.root / "quality/evals/fachgebiet.json"
        profile = json.loads(path.read_text(encoding="utf-8"))
        profile["workshop_review"] = {
            "verdict": "retained", "reason": "Individueller Belegabgleich", "changes": [],
            "sha256": lab.digest(self.before["werkstatt"]),
        }
        lab.save(path, profile)
        result, output = self.routing_audit()
        self.assertEqual(result, 0, output)
        self.paths["werkstatt"].write_bytes(self.before["werkstatt"] + b"\n")
        result, output = self.routing_audit()
        self.assertEqual(result, 1)
        self.assertIn("Werkstatt-Prüfung seit individueller Prüfung verändert", output)


class WorkshopValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        plugin = self.root / "fachgebiet"
        description = "Technisches Testpaket für Belegabgleich und abgeschlossene Dokumente."
        manifest = {"name": "fachgebiet", "version": "1.0.0", "description": description,
                    "author": {"name": "Klotzkette", "email": "39582916+Klotzkette@users.noreply.github.com"}}
        lab.save(plugin / ".claude-plugin/plugin.json", manifest)
        lab.save(self.root / ".claude-plugin/marketplace.json", {
            "version": "1.0.0", "description": description,
            "plugins": [{"name": "fachgebiet", "source": "./fachgebiet", "version": "1.0.0", "description": description}],
        })
        skill = plugin / "skills/belegabgleich/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text('---\nname: belegabgleich\ndescription: "Gleicht Zahlung und Gutschrift anhand bestätigter Gebühren und nachgereichter Kontoauszüge ab."\n---\n\n# Belegabgleich\n\nBelege prüfen.\n', encoding="utf-8")
        download = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=fachgebiet/"
        (plugin / "README.md").write_text(
            "# Testpaket\n\n<!-- BEGIN direkt-loslegen (autogen) -->\n"
            "<!-- END direkt-loslegen (autogen) -->\n"
            "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachgebiet.zip\n"
            + download + "fachgebiet-werkstatt.md\n" + download + "fachgebiet-schnellstart.md\n", encoding="utf-8")
        workflow = self.root / ".github/workflows/release-plugin-zips.yml"
        workflow.parent.mkdir(parents=True)
        workflow.write_text("testakte-*-einzelpdfs.zip\n", encoding="utf-8")
        self.mini = plugin / "fachgebiet-schnellstart.md"
        self.mini.write_text("# Abgleich\n\nBelege prüfen.\n", encoding="utf-8")
        self.workshop = plugin / "fachgebiet-werkstatt.md"
        self.valid = (
            "# 1. Buchungsabgleich\n\n## 1.1. Eingang und Rückfragen\n\n"
            "Lies die Buchungen und kläre die Differenz anhand des Gebührenbelegs.\n\n"
            "## 1.2. Abschluss\n\nÜbernimm die Antwort in den Vermerk. "
            "Ohne Export liefere den vollständigen Text, keinen Dateilink.\n"
        )
        self.workshop.write_text(self.valid, encoding="utf-8")

    def validations(self, success):
        for name in ("validate-marketplace-import.mjs", "audit-release-readiness.mjs"):
            with self.subTest(validator=name):
                result = subprocess.run(["node", str(SCRIPTS / name)], cwd=self.root,
                                        capture_output=True, text=True, timeout=20)
                self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)

    def test_short_structured_workshop_is_not_rejected_for_volume(self):
        self.validations(True)
        self.workshop.write_text(self.valid + "Belegzuordnung beibehalten.\n" * 350, encoding="utf-8")
        self.assertLess(self.workshop.stat().st_size, 12 * 1024)
        self.validations(True)

    def test_empty_title_only_and_empty_sections_are_not_valid_workshops(self):
        for text in ("", "# Titel\n", "# Titel\n\n## 1. Abschluss\n\n", self.valid + "\n# Zweiter Titel\n"):
            with self.subTest(text=text):
                self.workshop.write_text(text, encoding="utf-8")
                self.validations(False)

    def test_workshop_upper_bound_remains(self):
        self.workshop.write_text(self.valid + "x" * G.MAX_WERKSTATT, encoding="utf-8")
        self.validations(False)

    def test_long_standalone_workshop_is_allowed_without_increasing_skill_limits(self):
        self.workshop.write_text(self.valid + "Fachliche Vertiefung.\n" * 16000, encoding="utf-8")
        self.assertGreater(self.workshop.stat().st_size, 48 * 1024)
        self.assertGreater(self.workshop.stat().st_size, 128 * 1024)
        self.assertLess(self.workshop.stat().st_size, G.MAX_WERKSTATT)
        self.validations(True)

    def test_marketplace_workshop_review_keeps_structure_and_hash_checks(self):
        import hashlib
        profile_path = self.root / "quality/evals/fachgebiet.json"
        profile_path.parent.mkdir(parents=True, exist_ok=True)
        for text, valid_hash, expected in (
            (self.valid, True, True),
            (self.valid, False, False),
            ("# Titel\n", True, False),
            (self.valid + "x" * G.MAX_WERKSTATT, True, False),
        ):
            with self.subTest(text_length=len(text), valid_hash=valid_hash):
                self.workshop.write_text(text, encoding="utf-8")
                profile_path.write_text(json.dumps({"workshop_review": {
                    "verdict": "retained", "reason": "Individuell geprüft", "changes": [],
                    "sha256": hashlib.sha256(self.workshop.read_bytes()).hexdigest() if valid_hash else "0" * 64,
                }}), encoding="utf-8")
                result = subprocess.run(["node", str(SCRIPTS / "validate-marketplace-import.mjs")],
                                        cwd=self.root, capture_output=True, text=True, timeout=20)
                self.assertEqual(result.returncode == 0, expected, result.stdout + result.stderr)

    def test_mini_upper_bound_remains(self):
        self.mini.write_bytes(b"x" * 7501)
        self.validations(False)

    def test_release_audit_distinguishes_prompt_size_from_answer_truncation(self):
        document = self.root / "CHANGELOG.md"
        for text, expected in (
            ("Ein eigenständiger Markdown-Prompt mit höchstens 7500 Zeichen.", True),
            ("Ein Hauptproblem-Prompt mit höchstens 7500 Zeichen und Bytes.", True),
            ("Ein separater Markdown-Download mit hoechstens 7500 Zeichen und Bytes.", True),
            ("Ein Schnellstart-Prompt mit höchstens 7500 Zeichen.", True),
            ("Antworte mit höchstens 7500 Zeichen.", False),
            ("Ein Hauptproblem-Prompt verlangt eine Antwort mit höchstens 7500 Zeichen.", False),
            ("Ein Markdown-Prompt mit höchstens 7500 Zeichen. Antworte mit höchstens 7500 Zeichen.", False),
            ("Spar-Alternative: Ein Markdown-Prompt mit höchstens 7500 Zeichen.", False),
        ):
            with self.subTest(text=text):
                document.write_text(text, encoding="utf-8")
                result = subprocess.run(["node", str(SCRIPTS / "audit-release-readiness.mjs")],
                                        cwd=self.root, capture_output=True, text=True, timeout=20)
                self.assertEqual(result.returncode == 0, expected, result.stdout + result.stderr)


class LegacyBoundaryTests(unittest.TestCase):
    def test_invalid_utf8_skill_is_not_rewritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            original = (
                ("# Fachskill\n\n" + R.DIREKTSTART_SENTENCE + "\n\n").encode("utf-8")
                + b"Beschadigter Inhalt: \xff\n"
            )
            path.write_bytes(original)
            with self.assertRaises(UnicodeDecodeError):
                R.refine_skill(path)
            self.assertEqual(path.read_bytes(), original)

    def test_quoted_rules_survive_cleanup_and_second_run(self):
        for opening, closing in (("```markdown", "```"), ("~~~~md", "~~~~~"),
                                 ("   ````markdown", "   ````"), ("```", "")):
            for kind, block in (("werkstatt", R.OLD_WERKSTATT_BLOCK),
                                ("schnellstart", R.SCHNELLSTART_BLOCK),
                                ("skill", "\n" + R.DIREKTSTART_SENTENCE + "\n")):
                with self.subTest(opening=opening, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp) / "beispiel.md"
                    quoted = "# Beispiel\n\n" + opening + "\n" + block + closing + "\n"
                    path.write_text(quoted, encoding="utf-8")
                    with patch.object(R, "prompt_is_protected", return_value=False):
                        action = lambda: R.refine_skill(path) if kind == "skill" else R.refine_prompt(path, kind)
                        self.assertFalse(action())
                        self.assertFalse(action())
                    self.assertEqual(path.read_bytes(), quoted.encode("utf-8"))

    def test_cleanup_after_fence_preserves_example_and_subject(self):
        quoted = "# Beispiel\n\n````markdown\n```\n" + R.WERKSTATT_BLOCK + "````\n\n"
        subject = "## 2. Belegabgleich\n\nNach der Antwort die Rechnung berichtigen.\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "werkstatt.md"
            path.write_text(quoted + R.WERKSTATT_BLOCK + "\n" + subject, encoding="utf-8")
            with patch.object(R, "prompt_is_protected", return_value=False):
                self.assertTrue(R.refine_prompt(path, "werkstatt"))
                self.assertFalse(R.refine_prompt(path, "werkstatt"))
            self.assertEqual(path.read_text(encoding="utf-8"), quoted + "\n" + subject)

    def test_adjacent_skill_legacy_paragraphs_removed_in_one_pass(self):
        for count in (1, 2, 3):
            for ending in ("\n\n## 1. Belegabgleich\n\nBelege lesen.\n", ""):
                with self.subTest(count=count, ending=ending), tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp) / "SKILL.md"
                    before = "# Fachskill" + ("\n\n" + R.DIREKTSTART_SENTENCE) * count + ending
                    path.write_text(before, encoding="utf-8")
                    self.assertTrue(R.refine_skill(path))
                    self.assertFalse(R.refine_skill(path))
                    self.assertEqual(path.read_text(encoding="utf-8"), "# Fachskill" + ending)

    def test_legacy_fallback_scopes_pause_and_resumes_dependent_document(self):
        text = G.werkstatt_ergonomy_text(PROFILE_BY_KEY["zeugnis"])
        row = next(line for line in text.splitlines() if "Bewerbungsschluss" in line)
        # Vorlagenvertrag, kein Nachweis tatsächlichen Modellverhaltens.
        self.assertIn("Beendigungsdatum, Funktion oder Zeugnisart ist unklar", row)
        self.assertNotIn("vor Fortsetzung klären", row)
        self.assertIn("nur den davon abhängigen Schritt zurückstellen", row)
        self.assertIn("unabhängige Teile weiterbearbeiten", row)
        self.assertIn("nach der Antwort den betroffenen Teil bis zum bestellten Dokument fortsetzen", row)


if __name__ == "__main__":
    unittest.main()
