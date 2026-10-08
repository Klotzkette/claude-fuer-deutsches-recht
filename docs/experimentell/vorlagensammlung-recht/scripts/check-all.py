#!/usr/bin/env python3
"""Führt den vollständigen lokalen Qualitätsgate in CI-Reihenfolge aus.

Standardmodus: Entwicklerlauf mit `run-eval.py --report`, damit
`EVAL_RESULTS.md` aktualisiert wird.

CI-Modus: `--ci` nutzt den JSON-Ausgabepfad der GitHub Action und verändert
den Report nicht.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def checks() -> list[tuple[str, list[str]]]:
    python = sys.executable
    return [
        ("Vorlagen validieren", [python, "scripts/validate-vorlagen.py"]),
        ("Drei-Ordner-Sicht prüfen", [python, "scripts/check-kategorien-index.py"]),
        ("Gerichtsleitende Vorlagen prüfen", [python, "scripts/check-gerichtsleitend.py"]),
        ("Umlaut-Hygiene prüfen", [python, "scripts/check-umlauthygiene.py"]),
        ("ODT-Integrität prüfen", [python, "scripts/check-odt-integrity.py"]),
        ("ODT-Spaltenlayout prüfen", [python, "scripts/check-odt-spaltenlayout.py"]),
        ("Markdown-ZIPs prüfen", [python, "scripts/check-md-zip-integrity.py"]),
        ("Rechtsprechungs-Hygiene prüfen", [python, "scripts/check-rechtsprechungshygiene.py"]),
        ("Gliederung prüfen", [python, "scripts/check-gliederung.py"]),
    ]


def eval_befehle(ci: bool) -> list[tuple[str, list[str]]]:
    python = sys.executable
    eval_befehl = (
        [python, "scripts/run-eval.py", "--json-out", "runs/ci.json", "--label", "ci"]
        if ci
        else [python, "scripts/run-eval.py", "--report"]
    )
    return [
        (
            "Eval-Harness mit Testakten prüfen",
            [python, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        ),
        ("Sämtliche Rubrics bewerten", eval_befehl),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Alle Qualitätschecks dieses Repos ausführen.")
    parser.add_argument("--ci", action="store_true", help="CI-Modus mit JSON-Eval-Ausgabe statt Report.")
    parser.add_argument(
        "--jobs",
        type=int,
        default=4,
        help="Anzahl paralleler, nur lesender Prüfungen; 1 erzwingt den seriellen Lauf.",
    )
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs muss mindestens 1 sein")

    nur_lesend = checks()

    def ausfuehren(pruefung: tuple[str, list[str]]) -> tuple[subprocess.CompletedProcess[str], float]:
        _, cmd = pruefung
        start = time.perf_counter()
        result = subprocess.run(
            cmd,
            cwd=REPO,
            check=False,
            text=True,
            capture_output=True,
        )
        return result, time.perf_counter() - start

    gesamtstart = time.perf_counter()
    with ThreadPoolExecutor(max_workers=min(args.jobs, len(nur_lesend))) as pool:
        ergebnisse = list(pool.map(ausfuehren, nur_lesend))

    for nummer, ((name, _), (result, dauer)) in enumerate(
        zip(nur_lesend, ergebnisse, strict=True),
        start=1,
    ):
        print(f"\n[{nummer}/10] {name} ({dauer:.2f} s)", flush=True)
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        if result.returncode != 0:
            print(f"\nFEHLER: {name} ist mit Code {result.returncode} fehlgeschlagen.", file=sys.stderr)
            return result.returncode

    print("\n[10/10] Eval-Harness testen und Rubrics bewerten", flush=True)
    eval_start = time.perf_counter()
    eval_pruefungen = eval_befehle(args.ci)
    with ThreadPoolExecutor(max_workers=len(eval_pruefungen)) as pool:
        eval_ergebnisse = list(pool.map(ausfuehren, eval_pruefungen))
    for (name, _), (result, _) in zip(eval_pruefungen, eval_ergebnisse, strict=True):
        print(f"  - {name}", flush=True)
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        if result.returncode != 0:
            print(f"\nFEHLER: {name} ist mit Code {result.returncode} fehlgeschlagen.", file=sys.stderr)
            return result.returncode
    dauer = time.perf_counter() - eval_start

    gesamtdauer = time.perf_counter() - gesamtstart
    print(
        f"\ncheck-all OK (10/10 Checks grün; Eval {dauer:.2f} s; gesamt {gesamtdauer:.2f} s)",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
