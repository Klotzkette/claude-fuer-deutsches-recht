#!/usr/bin/env python3
"""Baut und prüft nur die drei Produktionsakten mit den zentralen Pakethelfern."""
import argparse
import hashlib
import importlib.util
import io
import json
import re
import shutil
import zipfile
from pathlib import Path
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES
from testakte_zip_common import working_dump_expected_arcnames

ROOT = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / filename)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def normalized(text):
    return ''.join(re.findall(r'\w+', text.casefold()))


def body_text(reader, case):
    headers = {d['sender'].split('\n')[0] + ' | ' + case['matter']
               for d in case['documents'] if 'sender' in d}
    footer = re.compile(re.escape(case['matter']) + r'\s*\|\s*Seite\s+\d+')
    return '\n'.join(line for page in reader.pages for line in page.extract_text().splitlines()
                     if line.strip() not in headers and not footer.fullmatch(line.strip()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dist', type=Path, required=True)
    args = parser.parse_args()
    args.dist.mkdir(parents=True, exist_ok=True)
    originals = module('production_originals', 'build-testakten-release-zips.py')
    singles = module('production_singles', 'build-testakten-einzelpdf-zips.py')
    readmes = module('production_readmes', 'validate-testakten-readme-downloads.py')
    results = []
    for case in json.loads((ROOT / 'scripts/ki-kanzlei-produktionsfaelle.json').read_text()):
        folder = ROOT / 'testakten' / case['slug']
        errors = []
        readmes.validate_local_readme(folder.name, folder, errors)
        readmes.validate_overview(folder.name, (ROOT / 'testakten/README.md').read_text(), errors)
        assert not errors, errors
        total = folder / 'gesamt-pdf' / (folder.name + '_gesamt.pdf')
        total_text = normalized(body_text(PdfReader(total), case))
        original_zip, _ = originals.build_single(folder, args.dist)
        pdf_zip, count = singles.build_single(folder, args.dist)
        assert count == len(case['documents'])
        with zipfile.ZipFile(original_zip) as archive:
            assert set(archive.namelist()) == set(working_dump_expected_arcnames(folder, include_gesamt_pdf=True))
            assert archive.read('README.txt') == NOTICE_BYTES
            assert all('/' not in n and not n.endswith('.md') for n in archive.namelist())
            for item in case['documents']:
                assert archive.read(item['file']) == (folder / item['file']).read_bytes()
        records = []
        with zipfile.ZipFile(pdf_zip) as archive:
            assert archive.read('README.txt') == NOTICE_BYTES
            assert len(archive.namelist()) == count + 1
            assert all('/' not in n for n in archive.namelist())
            for item in case['documents']:
                name = Path(item['file']).stem + '.pdf'
                reader = PdfReader(io.BytesIO(archive.read(name)))
                text = body_text(reader, case)
                assert 'This test case file' not in text
                assert 'Diese Testakte wurde' not in text
                body = item.get('body', item.get('rows', []))
                if isinstance(body, str):
                    segments = body.splitlines()
                elif 'rows' in item:
                    segments = [str(v) for row in body for v in row]
                else:
                    segments = [line for paragraph in body for line in paragraph.splitlines()]
                for segment in segments:
                    needle = normalized(segment)
                    if not needle:
                        continue
                    assert needle in normalized(text), (name, 'Einzel-PDF-Inhalt fehlt', segment[:60])
                    assert needle in total_text, (name, 'Gesamt-PDF-Inhalt fehlt', segment[:60])
                records.append({'file': item['file'], 'pdf': name, 'pages': len(reader.pages), 'sha256': hashlib.sha256(archive.read(name)).hexdigest()})
        shutil.copyfile(total, args.dist / total.name)
        results.append({'case': folder.name, 'documents': records, 'total_pages': len(PdfReader(total).pages), 'source_to_both_pdf_forms': 'passed', 'flat_archives_and_notices': 'passed'})
    report = ROOT / 'quality/ki-native-kanzlei/produktionsakten-pruefung.json'
    report.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    checksum = args.dist / 'checksums-sha256.txt'
    checksum.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(args.dist.iterdir()) if p.is_file() and p != checksum))
    print(json.dumps({'cases': len(results), 'originals': sum(len(r['documents']) for r in results), 'checks': 'passed'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
