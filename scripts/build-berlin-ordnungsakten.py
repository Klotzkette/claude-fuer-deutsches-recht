#!/usr/bin/env python3
"""Native Akten für Berliner Gewerbeaufsicht, Polizei und Versammlungen.

Verwendet denselben geprüften Word-, MIME- und Tabellenbau wie die
Bildungsakten. --qa-dir, --only und --render-docx funktionieren entsprechend.
AKTEN_NODE und AKTEN_NODE_MODULES wählen die gebündelte Office-Laufzeit.
"""
from __future__ import annotations

import importlib
import importlib.util
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "berlin_native_builder", ROOT / "scripts/build-berlin-bildungsakten.py"
)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def readme(case, directory):
    builder.native.readme(case, directory)
    target = directory / "README.md"
    text = target.read_text(encoding="utf-8").replace(
        "Alle Personen und Unternehmen in dieser Akte sind fiktiv.",
        "Alle Personen, Unternehmen, Initiativen und Vorgänge in dieser Akte "
        "sind fiktiv. Reale Berliner Behördennamen dienen der örtlichen und "
        "verfahrensrechtlichen Einordnung; Schreiben, Aktenzeichen und "
        "Kontaktdaten sind erfunden."
    )
    target.write_text(text, encoding="utf-8")
    # Den Downloadblock erzeugt der zentrale Generator nach dem PDF-Bau.
    # Dadurch bleiben Dateinamen, Begleitrelease und Warnhinweise identisch.


if __name__ == "__main__":
    modules = {
        "gewerbe": "berlin_gewerbeakten_daten",
        "asog": "berlin_asogakten_daten",
        "versammlung": "berlin_versammlungsakten_daten",
    }
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--groups", nargs="+", choices=modules, default=list(modules))
    groups, rest = parser.parse_known_args()
    sys.argv = [sys.argv[0], *rest]
    builder.CASES = [
        case for group in groups.groups
        for case in importlib.import_module(modules[group]).CASES
    ]
    builder.ATTACHMENTS = {
        case["slug"]: case.get("attachments", {}) for case in builder.CASES
    }
    builder.readme = readme
    builder.main()
