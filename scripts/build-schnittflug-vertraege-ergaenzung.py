#!/usr/bin/env python3
"""Baut nur die neuen Verhandlungsunterlagen 100 bis 111 der Schnittflug-Akte."""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'scripts/data/startup-gruender/vertraege-ergaenzung.json'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    data = json.loads(DATA.read_text(encoding='utf-8'))
    facts = json.loads((ROOT / 'scripts/data/startup-gruender/fallstamm.json').read_text(encoding='utf-8'))
    if data['case_slug'] != facts['case_slug'] or len(facts['founders']) != 7 or sum(x['nominal_eur'] for x in facts['founders']) != 25000:
        raise ValueError('Fallstamm und Ergänzung sind nicht konsistent.')
    folder = args.output_dir or ROOT / 'testakten' / data['case_slug']
    names = [row['file'] for row in data['documents']]
    if len(names) != 12 or len(set(names)) != 12 or any(Path(n).name != n or not n.endswith('.docx') for n in names):
        raise ValueError('Die Ergänzung erfordert zwölf eindeutige DOCX-Dateien.')
    if [n[:3] for n in names] != [str(n) for n in range(100, 112)]:
        raise ValueError('Der Builder darf nur den Bereich 100 bis 111 schreiben.')
    spec = importlib.util.spec_from_file_location('schnittflug_docx', ROOT / 'scripts/build-startup-gruender-lebensakte.py')
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    folder.mkdir(parents=True, exist_ok=True)
    for row in data['documents']:
        helper.save_docx(row, folder)
    print(json.dumps({'docx': len(names), 'output_dir': str(folder)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
