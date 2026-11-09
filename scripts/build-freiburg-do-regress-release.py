#!/usr/bin/env python3
"""Baut und prüft die drei Downloadfassungen der Freiburger Regressakte."""
from __future__ import annotations

import argparse
import csv
from email import policy
from email.parser import BytesParser
from io import BytesIO, StringIO
import importlib.util
import json
from pathlib import Path
import shutil
from zipfile import ZipFile

from openpyxl import load_workbook
from pypdf import PdfReader
from testakte_disclaimer import pdf_content_errors

ROOT = Path(__file__).resolve().parents[1]
TAG = 'arbeitsrecht-ceo-fraud-freiburg-v1.0.0'
SLUG = 'arbeitsrecht-ceo-fraud-do-regress-freiburg'
ORIGINAL = f'testakte-{SLUG}.zip'
SINGLES = f'testakte-{SLUG}-einzelpdfs.zip'
COMBINED = f'{SLUG}_gesamt.pdf'
DEBRIEF = 'AF-01_Nachbesprechung.pdf'


def load_script(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), ROOT / 'scripts' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


COMMON = load_script('build-projekteinkauf-baubranche-release')


def verify_payment_matrix(archive):
    journal = archive.read('36_Buchungsjournal_Treasury.csv').decode('utf-8-sig')
    rows = list(csv.reader(StringIO(journal), delimiter=';'))[1:]
    workbook = load_workbook(BytesIO(archive.read('35_Zahlungs_und_Deckungsmatrix.xlsx')),
                             read_only=True, data_only=True)
    try:
        payments = list(workbook['Zahlungen'].iter_rows(min_row=4, max_row=9, values_only=True))
        if [list(map(str, row[:4])) for row in payments[:-1]] != rows or len(rows) != 5:
            raise ValueError('Zahlungsmatrix und Buchungsjournal weichen ab')
        if payments[-1][2:] != (6500000, 1000000, 5500000) or any(
                gross - recovered != balance for _, _, gross, recovered, balance in payments):
            raise ValueError('Überweisungen und Rückflüsse gehen nicht auf')
        coverage = workbook['D&O']
        if coverage['B7'].value != 3130000 or any(coverage[key].value not in (None, '') for key in ('B8', 'B9', 'B10')):
            raise ValueError('Rechenrest oder offene Szenariofelder fehlerhaft')
    finally:
        workbook.close()


def verify(dist):
    expected = {ORIGINAL, SINGLES, COMBINED, DEBRIEF, 'release-bestand.json'}
    if {path.name for path in dist.iterdir()} != expected | {'checksums-sha256.txt'}:
        raise ValueError('Unerwarteter Dateibestand im Release')
    checksums = dict(line.split('  ', 1)[::-1] for line in (dist / 'checksums-sha256.txt').read_text().splitlines())
    if set(checksums) != expected or any(COMMON.checksum(dist / name) != digest for name, digest in checksums.items()):
        raise ValueError('Prüfsummen weichen ab')
    report = json.loads((dist / 'release-bestand.json').read_text())
    if report['tag'] != TAG or set(report['archives']) != {ORIGINAL, SINGLES}:
        raise ValueError('Unerwartetes Inventar')
    for name, records in report['archives'].items():
        if COMMON.inventory(dist / name, case_zip=True) != records:
            raise ValueError('Abweichendes Archivinventar ' + name)
    case = report['case']
    with ZipFile(dist / ORIGINAL) as originals, ZipFile(dist / SINGLES) as singles:
        if (len(originals.namelist()), len(singles.namelist())) != (case['documents'] + 2, case['documents'] + 1):
            raise ValueError('Anzahl der Dokumente stimmt nicht überein')
        contents = originals.read(COMBINED)
        if contents != (dist / COMBINED).read_bytes() or case['combined_sha256'] != checksums[COMBINED]:
            raise ValueError('Lesefassung weicht vom Original-ZIP ab')
        pdf = PdfReader(BytesIO(contents))
        if len(pdf.pages) != case['pages'] or len(pdf.outline) != case['documents']:
            raise ValueError('PDF-Seiten oder PDF-Lesezeichen weichen ab')
        for name in originals.namelist():
            if name.endswith('.eml'):
                message = BytesParser(policy=policy.default).parsebytes(originals.read(name))
                if message.defects:
                    raise ValueError('Fehlerhafte MIME-Nachricht ' + name)
                for part in message.iter_attachments():
                    if part.get_payload(decode=True) != originals.read(part.get_filename()):
                        raise ValueError('Abweichende E-Mail-Anlage ' + name)
        if any('Nachbesprechung' in name for name in originals.namelist()):
            raise ValueError('Moderationsmaterial in der Arbeitsakte')
        verify_payment_matrix(originals)
    print(f"{TAG}: 6 Release-Dateien, {case['documents']} Originale, {case['pages']} Seiten.")


def build(dist, rebuild):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Ein leeres Ausgabeziel ist erforderlich')
    dist.mkdir(parents=True, exist_ok=True)
    case = load_script('build-freiburg-do-regress-akten').load_case()
    native = load_script('build-testakten-release-zips')
    single = load_script('build-testakten-einzelpdf-zips')
    native_check = load_script('validate-testakten-release-zips')
    pdf_check = load_script('validate-testakten-einzelpdf-zips')
    record = COMMON.build_case(case, dist, rebuild, native, single, native_check, pdf_check)
    debrief = ROOT / 'quality' / SLUG / DEBRIEF
    if issues := pdf_content_errors(debrief.read_bytes()):
        raise ValueError(f'{DEBRIEF}: {issues}')
    shutil.copyfile(debrief, dist / DEBRIEF)
    report = {'schema_version': 1, 'tag': TAG, 'case': record,
              'archives': {name: COMMON.inventory(dist / name, case_zip=True) for name in (ORIGINAL, SINGLES)}}
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / 'checksums-sha256.txt').write_text(''.join(
        f'{COMMON.checksum(path)}  {path.name}\n' for path in sorted(dist.iterdir())))
    verify(dist)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--verify-only', action='store_true')
    mode.add_argument('--rebuild-pdfs', action='store_true')
    args = parser.parse_args()
    if args.verify_only:
        verify(args.dist.resolve())
    else:
        build(args.dist.resolve(), args.rebuild_pdfs)
