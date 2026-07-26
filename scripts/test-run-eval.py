#!/usr/bin/env python3
"""Regressionstests für die sicherheits- und schemaharten Rubrikprüfungen."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "run-eval.py"
SPEC = importlib.util.spec_from_file_location("run_eval", SCRIPT)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = R
SPEC.loader.exec_module(R)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="rubrik-test-") as tmp:
        case = Path(tmp)
        (case / "unterlage.txt").write_text("Frist 17.07.2026", encoding="utf-8")
        (case / "daten.json").write_text(
            json.dumps({"akte": {"status": "offen"}}), encoding="utf-8"
        )
        (case / "daten.yaml").write_text(
            "akte:\n  prioritaet: hoch\n", encoding="utf-8"
        )

        require(
            R.run_check(
                case,
                {
                    "id": "text",
                    "check_type": "text_contains",
                    "description": "",
                    "path": "unterlage.txt",
                    "contains": "17.07.2026",
                },
            ).passed
            is True,
            "Textprüfung muss vorhandenen Inhalt finden",
        )
        require(
            R.run_check(
                case,
                {
                    "id": "leer",
                    "check_type": "text_contains",
                    "description": "",
                    "path": "unterlage.txt",
                    "contains": "",
                },
            ).passed
            is False,
            "Leerer Suchtext darf nicht automatisch bestehen",
        )
        require(
            R.run_check(
                case,
                {
                    "id": "json",
                    "check_type": "json_field_equals",
                    "description": "",
                    "path": "daten.json",
                    "field": "akte.status",
                    "equals": "offen",
                },
            ).passed
            is True,
            "JSON-Feldprüfung muss verschachtelte Werte lesen",
        )
        require(
            R.run_check(
                case,
                {
                    "id": "yaml",
                    "check_type": "yaml_field_equals",
                    "description": "",
                    "path": "daten.yaml",
                    "field": "akte.prioritaet",
                    "equals": "hoch",
                },
            ).passed
            is True,
            "YAML-Feldprüfung muss verschachtelte Werte lesen",
        )
        try:
            R.resolve_case_path(case, "../ausbruch.txt")
        except ValueError:
            pass
        else:
            raise AssertionError("Ein Rubrikpfad darf den Testaktenordner nicht verlassen")

        schema_errors = R.rubric_schema_checks(
            {
                "name": "Akte",
                "plugin": "tbd",
                "checks": [
                    {"id": "doppelt", "check_type": "file_exists"},
                    {"id": "doppelt", "check_type": "unbekannt"},
                ],
            }
        )
        require(len(schema_errors) == 3, "Plugin, doppelte ID und unbekannter Typ müssen auffallen")
        legacy_errors = R.rubric_schema_checks(
            {
                "name": "Akte",
                "plugin": next(iter(R.PLUGIN_NAMES)),
                "checks": [
                    {
                        "id": "r03-mindestens-3-aktenstuecke",
                        "check_type": "file_count",
                        "description": "mindestens ein Markdown-Aktenstück",
                        "glob": "*.md",
                        "min": 1,
                    },
                    {
                        "id": "r04-fachspezifischer-check-zu-ergaenzen",
                        "check_type": "human_review",
                        "description": "Fachspezifischer Check ist zu ergänzen",
                    },
                ],
            }
        )
        require(
            len(legacy_errors) == 4,
            "Legacy-IDs, Markdown-Aktenchecks und offene Platzhalter müssen auffallen",
        )
        require(
            "formatvorlagen-paradebeispiele" in R.RUBRIC_EXEMPT_SLUGS
            and "megaprompts" in R.RUBRIC_EXEMPT_SLUGS
            and len(R.RUBRIC_EXEMPT_SLUGS) == 2,
            "nur die beiden Metasammlungen dürfen ohne Rubrik bleiben",
        )

    print("test-run-eval OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
