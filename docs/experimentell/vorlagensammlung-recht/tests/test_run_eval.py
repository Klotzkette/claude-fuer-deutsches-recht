from __future__ import annotations

import io
import importlib.util
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
FIXTURE = REPO / "tests" / "testakten" / "eval-harness"

sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("run_eval_under_test", SCRIPTS / "run-eval.py")
if spec is None or spec.loader is None:
    raise RuntimeError("run-eval.py konnte nicht als Testmodul geladen werden")
run_eval = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = run_eval
spec.loader.exec_module(run_eval)

from _vorlagen_dateien import THEMENORDNER  # noqa: E402


class EvalHarnessTest(unittest.TestCase):
    def test_testakte_deckt_alle_checktypen_ab(self) -> None:
        rubric = run_eval.load_yaml(FIXTURE / "rubric-pass.yaml")
        self.assertEqual([], run_eval.validate_rubric(rubric))
        results = [run_eval.run_check(FIXTURE, check) for check in rubric["checks"]]
        self.assertTrue(all(result.passed is not False for result in results))
        self.assertEqual(1, sum(result.passed is None for result in results))
        self.assertEqual(run_eval.SUPPORTED_CHECK_TYPES, {check["check_type"] for check in rubric["checks"]})

    def test_yaml_fallback_versteht_verschachtelte_felder(self) -> None:
        data = run_eval._simple_yaml_mapping(
            "status: aktiv\nprüfung:\n  stufe: 2\n  freigegeben: true\n"
        )
        self.assertEqual(2, run_eval._field_value(data, "prüfung.stufe"))
        self.assertIs(run_eval._MISSING, run_eval._field_value(data, "prüfung.fehlt"))

        rubric = run_eval._simple_rubric_yaml(
            "checks:\n"
            "  - id: typvergleich\n"
            "    check_type: json_field_equals\n"
            "    description: Typen bleiben erhalten\n"
            "    path: daten.json\n"
            "    field: prüfung.freigegeben\n"
            "    equals: true\n"
        )
        self.assertIs(rubric["checks"][0]["equals"], True)

    def test_ungueltiger_regex_wird_als_fehler_gemeldet(self) -> None:
        result = run_eval.run_check(FIXTURE, {
            "id": "kaputter-regex",
            "check_type": "regex_match",
            "description": "Ungültiger Ausdruck",
            "path": "muster.md",
            "pattern": "[",
        })
        self.assertFalse(result.passed)
        self.assertIn("invalid regex", result.detail)

    def test_rubric_schema_blockiert_doppelte_ids_und_unbekannte_typen(self) -> None:
        errors = run_eval.validate_rubric({
            "checks": [
                {
                    "id": "doppelt",
                    "check_type": "file_exists",
                    "description": "Erster Check",
                    "path": "muster.md",
                },
                {
                    "id": "doppelt",
                    "check_type": "nicht-implementiert",
                    "description": "Zweiter Check",
                },
            ],
        })
        self.assertTrue(any("doppelte id" in error for error in errors))
        self.assertTrue(any("unbekannten check_type" in error for error in errors))

    def test_defekte_rubric_bricht_nicht_den_gesamtlauf_ab(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "rubric.yaml").write_text("checks:\n  - id: [\n", encoding="utf-8")
            result = run_eval.evaluate_vorlage("test/defekt", folder)
        self.assertTrue(result.has_rubric)
        self.assertFalse(result.all_passed)
        self.assertEqual("rubric-schema", result.checks[0].rubric_id)

    def test_unbekannter_slug_ist_ein_bedienfehler(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unbekannte Vorlagen-Slugs"):
            run_eval.select_vorlagen(
                [("arbeitsrecht/beispiel", Path("/tmp/beispiel"))],
                ["arbeitsrecht/nicht-vorhanden"],
            )

    def test_fehlende_rubric_und_leerer_bestand_sind_keine_erfolge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            vorlage = Path(tmp) / "ohne-rubric"
            vorlage.mkdir()
            ausgabe = io.StringIO()
            with (
                patch.object(
                    run_eval,
                    "discover_vorlagen",
                    return_value=[("test/ohne-rubric", vorlage)],
                ),
                redirect_stdout(ausgabe),
            ):
                status = run_eval.main([])
        self.assertEqual(1, status)
        self.assertIn("rubric.yaml fehlt", ausgabe.getvalue())

        fehlerausgabe = io.StringIO()
        with (
            patch.object(run_eval, "discover_vorlagen", return_value=[]),
            patch("sys.stderr", fehlerausgabe),
        ):
            status = run_eval.main([])
        self.assertEqual(1, status)
        self.assertIn("Keine Vorlagen entdeckt", fehlerausgabe.getvalue())

    def test_rubric_pfade_bleiben_im_vorlagenordner(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            basis = Path(tmp)
            vorlage = basis / "vorlage"
            vorlage.mkdir()
            geheim = basis / "geheim.txt"
            geheim.write_text("nicht lesen", encoding="utf-8")

            traversal = run_eval.run_check(vorlage, {
                "id": "ausbruch",
                "check_type": "text_contains",
                "description": "Darf den Ordner nicht verlassen",
                "path": "../geheim.txt",
                "contains": "nicht lesen",
            })
            self.assertFalse(traversal.passed)
            self.assertIn("verlässt den Vorlagenordner", traversal.detail)

            link = vorlage / "verknuepfung.txt"
            try:
                link.symlink_to(geheim)
            except OSError:
                self.skipTest("Symbolische Links werden auf diesem System nicht unterstützt")
            verknuepfung = run_eval.run_check(vorlage, {
                "id": "link",
                "check_type": "file_exists",
                "description": "Darf keinen Link verfolgen",
                "path": "verknuepfung.txt",
            })
            self.assertFalse(verknuepfung.passed)
            self.assertIn("symbolischen Link", verknuepfung.detail)

        schemafehler = run_eval.validate_rubric({
            "checks": [{
                "id": "ausbruch",
                "check_type": "file_exists",
                "description": "Unsicherer Pfad",
                "path": "../../etc/passwd",
            }]
        })
        self.assertTrue(any("unsicheren path" in fehler for fehler in schemafehler))

    def test_kanonische_themenliste_deckt_alle_rubrics_ab(self) -> None:
        self.assertEqual(len(THEMENORDNER), len(set(THEMENORDNER)))
        rubric_areas = {
            rubric.parent.parent.name
            for rubric in REPO.glob("*/*/rubric.yaml")
        }
        self.assertEqual(set(THEMENORDNER), rubric_areas)

        discovered = run_eval.discover_vorlagen()
        rubric_count = sum(1 for _ in REPO.glob("*/*/rubric.yaml"))
        self.assertEqual(rubric_count, len(discovered))
        self.assertEqual(
            8,
            sum(slug.startswith("strafvollzugsrecht/") for slug, _ in discovered),
        )

    def test_standardausgabe_zeigt_nur_zusammenfassung_und_fehler(self) -> None:
        bestanden = run_eval.VorlagenResult(
            slug="test/bestanden",
            has_rubric=True,
            checks=[
                run_eval.CheckResult(
                    rubric_id="ok",
                    check_type="file_exists",
                    description="Datei vorhanden",
                    passed=True,
                )
            ],
        )
        fehlgeschlagen = run_eval.VorlagenResult(
            slug="test/fehlgeschlagen",
            has_rubric=True,
            checks=[
                run_eval.CheckResult(
                    rubric_id="inhalt",
                    check_type="text_contains",
                    description="Pflichttext vorhanden",
                    passed=False,
                    detail="Pflichttext fehlt",
                )
            ],
        )
        ausgabe = io.StringIO()
        with (
            patch.object(
                run_eval,
                "discover_vorlagen",
                return_value=[
                    (bestanden.slug, Path("/tmp/bestanden")),
                    (fehlgeschlagen.slug, Path("/tmp/fehlgeschlagen")),
                ],
            ),
            patch.object(
                run_eval,
                "evaluate_vorlage",
                side_effect=[bestanden, fehlgeschlagen],
            ),
            redirect_stdout(ausgabe),
        ):
            status = run_eval.main([])

        self.assertEqual(1, status)
        self.assertIn("Vorlagen: 2", ausgabe.getvalue())
        self.assertNotIn("[PASS] test/bestanden", ausgabe.getvalue())
        self.assertIn("[FAIL] test/fehlgeschlagen", ausgabe.getvalue())
        self.assertIn("Pflichttext fehlt", ausgabe.getvalue())


if __name__ == "__main__":
    unittest.main()
