#!/usr/bin/env python3
"""Ergänzt die Schnittflug-Akte reproduzierbar; erhält sämtliche Morgenstände."""
from __future__ import annotations
import argparse
import csv
from datetime import datetime
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'scripts/data/startup-gruender/kommunikation-ergaenzung.json'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--only', choices=['documents', 'mails', 'all'], default='all')
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    data = json.loads(DATA.read_text(encoding='utf-8'))
    prior = json.loads((DATA.parent / 'kommunikation.json').read_text(encoding='utf-8'))
    spec = importlib.util.spec_from_file_location('schnittflug_source_helper', ROOT / 'scripts/build-startup-gruender-lebensakte.py')
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    folder = args.output_dir or ROOT / 'testakten' / data['case_slug']
    folder.mkdir(parents=True, exist_ok=True)
    names = [r['file'] for key in ['documents', 'mails', 'chats', 'screenshots', 'registers'] for r in data[key]]
    assert len(names) == len(set(names))
    assert all(Path(n).name == n for n in names)
    if args.only in ('documents', 'all'):
        for row in data['documents']:
            helper.save_docx(row, folder)
        for row in data['screenshots']:
            helper.screenshot(row, folder)
        for row in data['chats']:
            text = row['title'] + '\n' + row['date'] + '\n\n'
            text += '\n\n'.join(f'[{day}] {person}: {body}' for day, person, body in row['messages']) + '\n'
            (folder / row['file']).write_text(text, encoding='utf-8')
        for row in data['registers']:
            with (folder / row['file']).open('w', encoding='utf-8-sig', newline='') as stream:
                writer = csv.writer(stream)
                writer.writerow(row['columns'])
                writer.writerows(row['rows'])
    if args.only in ('mails', 'all'):
        records = prior['mails'] + data['mails']
        people = prior['people'] | data['people']
        for index, row in enumerate(data['mails'], len(prior['mails']) + 1):
            if row.get('reply'):
                assert 0 < row['reply'] < index
                assert datetime.fromisoformat(records[row['reply']-1]['date']) <= datetime.fromisoformat(row['date'])
            helper.save_mail(row, index, records, people, folder)
    print(json.dumps({'part': args.only, 'docx': len(data['documents']), 'eml': len(data['mails']), 'chats': len(data['chats']), 'png': len(data['screenshots']), 'csv': len(data['registers'])}))

if __name__ == '__main__':
    main()
