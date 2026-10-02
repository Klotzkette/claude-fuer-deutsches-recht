#!/usr/bin/env python3
"""Baut vier native WEG-Arbeitsakten mit dem gemeinsamen Office-Builder.

--qa-dir ist Pflicht; --only und --render-docx entsprechen dem Bildungsbuilder.
Gesamt-PDFs und Archive werden anschließend durch die zentralen Builder erzeugt.
"""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('weg_native_builder', ROOT / 'scripts/build-berlin-bildungsakten.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
from weg_hausverwaltungsakten_daten import CASES


def readme(case, directory):
    builder.native.readme(case, directory)


if __name__ == '__main__':
    builder.CASES = CASES
    builder.ATTACHMENTS = {case['slug']: case.get('attachments', {}) for case in CASES}
    builder.readme = readme
    builder.main()
