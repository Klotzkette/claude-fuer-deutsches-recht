#!/usr/bin/env python3
"""Erweitert die native Tomasius-Verfahrensakte um die Einkommensteuer-Nachträge."""
from __future__ import annotations

import argparse
import csv
from email import policy
from email.parser import BytesParser
from hashlib import sha256
import importlib.util
from io import BytesIO, StringIO
import json
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

from openpyxl import load_workbook
from testakte_disclaimer import NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
TAG = 'tomasius-steuerakte-v4'
NAME = 'Testakte_Tomasius_2025_Rom_Musikschule_v4.zip'
CASE = ROOT / 'quality/steuerrecht-freiburg/tomasius-solo'
FOLDERS = ('13_Musikschule_Erwerbsstatus', '14_Wohnung_Rom', '15_Einkommensteuer_Arbeitsauftrag')
LEDGER = '14_Wohnung_Rom/11_Objektkonto_LT7_2025'
EXPECTED_FILES = 403
OLD_RELEASE_SHA256 = '3b4fe61d97ebdc717a05d2e8644ba1d3334fc79f7eccf8603623b2c1c6aeb9db'
README_ADDENDUM = """
8 Einkommensteuer-Nachtrag 2025

Ordner 13 enthält ergänzende Tatsachen zur Tätigkeit an der Städtischen Musikschule Freiburg Nord. Die Honorarvereinbarung und die Erklärungen zu § 127 SGB IV stehen weiter in Ordner 00. Gleichen Sie Vertragsabrede und Unterrichtspraxis ab und trennen Sie Erwerbsstatus, Übergangsregelung und steuerliche Folgen.

Ordner 14 enthält die Unterlagen zur Wohnungsvermietung in Rom, darunter einen deutsch-englischen Mietvertrag, Objektbewegungen, Kostenabrechnung und italienische Zahlungsbelege. Die Information zum römischen Fremdgeldkonto stammt aus dem späteren Mandatsnachtrag. Die ursprünglichen Freiburger Kontoauszüge bleiben die Beleggrundlage für das deutsche Konto. Prüfen Sie den Erwerbstitel, die Zurechnung der Miete und den italienischen Erklärungsstand getrennt.

Ordner 15 gibt den Arbeitsauftrag für die Einkommensteuer und die Fundstellen für die eigenständige Bearbeitung vor. Die steuerliche Einordnung und das Ergebnis der Statusprüfung sind offen. Die Aktenstücke zur Umsatzsteuer-Vorauszahlung IV/2025 und zur Klagevorbereitung stehen in den bisherigen Ordnern.
"""


def legacy_builder():
    path = ROOT / 'scripts/build-steuerrecht-ustva-release.py'
    spec = importlib.util.spec_from_file_location('tomasius_ustva', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def working_copy(legacy):
    members = legacy.copy()
    for folder in FOLDERS:
        for path in sorted((CASE / folder).iterdir()):
            if path.is_symlink() or not path.is_file() or path.suffix not in {
                    '.csv', '.docx', '.eml', '.pdf', '.txt', '.xlsx'}:
                raise ValueError('Unzulässige Nachtragsunterlage ' + str(path))
            name = f'{folder}/{path.name}'
            if name in members:
                raise ValueError('Namenskollision im Nachtrag ' + name)
            members[name] = path.read_bytes()
    members['README.txt'] = legacy['README.txt'].rstrip() + ('\n\n' + README_ADDENDUM.lstrip()).encode()
    members.pop('Dateibestand.csv')
    stream = StringIO(newline='')
    writer = csv.writer(stream, delimiter=';')
    writer.writerow(['Datei', 'Bytes', 'SHA256'])
    for name, data in sorted(members.items()):
        writer.writerow([name, len(data), sha256(data).hexdigest()])
    members['Dateibestand.csv'] = stream.getvalue().encode('utf-8-sig')
    return members


def verify_ledger(members):
    csv_rows = list(csv.reader(StringIO(members[f'{LEDGER}.csv'].decode('utf-8-sig')), delimiter=';'))[1:]
    workbook = load_workbook(BytesIO(members[f'{LEDGER}.xlsx']), read_only=True, data_only=True)
    try:
        sheet = workbook['Objektkonto']
        data = list(sheet.iter_rows(min_row=4, values_only=True))
        if [list(map(str, row[:6])) for row in data] != csv_rows:
            raise ValueError('Objektkonto in CSV und XLSX weicht ab')
        money_in = sum(row[3] for row in data)
        money_out = sum(row[4] for row in data)
        if (len(data), sum(row[1].startswith('MIETE-') for row in data), money_in, money_out) != (23, 12, 8160, 2469):
            raise ValueError('Mietzahlungen oder Objektkosten stimmen nicht mit der Abrechnung überein')
        balance = 0
        for row in data:
            balance += row[3] - row[4]
            if row[6] != balance:
                raise ValueError('Fehlerhafter fortlaufender Objektsaldo')
        if tuple(workbook['Arbeitsbogen'][f'B{i}'].value for i in (4, 5, 6)) != (8160, 2469, 5691):
            raise ValueError('Arbeitsbogen stimmt nicht mit dem Objektkonto überein')
    finally:
        workbook.close()


def verify_members(members, legacy):
    if len(members) != EXPECTED_FILES or not members['README.txt'].startswith(NOTICE_BYTES):
        raise ValueError('Aktenumfang oder Aktenhinweis fehlerhaft')
    for name, original in legacy.items():
        if name not in {'README.txt', 'Dateibestand.csv'} and members.get(name) != original:
            raise ValueError('Ursprüngliche Akte verändert ' + name)
    recorded = list(csv.DictReader(StringIO(members['Dateibestand.csv'].decode('utf-8-sig')), delimiter=';'))
    if len(recorded) != len(members) - 1 or {row['Datei'] for row in recorded} != set(members) - {'Dateibestand.csv'}:
        raise ValueError('Dateibestand unvollständig')
    for row in recorded:
        data = members[row['Datei']]
        if int(row['Bytes']) != len(data) or row['SHA256'] != sha256(data).hexdigest():
            raise ValueError('Aktenprüfsumme fehlerhaft ' + row['Datei'])
    for name, data in members.items():
        path = PurePosixPath(name)
        if path.parts[0] in FOLDERS and path.suffix == '.eml':
            mail = BytesParser(policy=policy.default).parsebytes(data)
            for part in mail.iter_attachments():
                filename = part.get_filename()
                if not filename or part.get_payload(decode=True) != members.get(str(path.parent / filename)):
                    raise ValueError('E-Mail-Anlage weicht vom Aktenstück ab ' + name)
    verify_ledger(members)


def check_legacy(archive, legacy):
    if sha256(archive.read_bytes()).hexdigest() != OLD_RELEASE_SHA256:
        raise ValueError('Nicht das veröffentlichte v3-Archiv')
    with ZipFile(archive) as original:
        if set(original.namelist()) != set(legacy) or any(original.read(name) != data for name, data in legacy.items()):
            raise ValueError('Rekonstruktion stimmt nicht mit veröffentlichter v3 überein')


def verify_release(dist, legacy):
    expected = {NAME, 'release-bestand.json', 'checksums-sha256.txt'}
    if {path.name for path in dist.iterdir()} != expected:
        raise ValueError('Unerwartete Release-Dateien')
    checksums = dict(line.split('  ', 1)[::-1] for line in (dist / 'checksums-sha256.txt').read_text().splitlines())
    if set(checksums) != expected - {'checksums-sha256.txt'} or any(
            sha256((dist / name).read_bytes()).hexdigest() != digest for name, digest in checksums.items()):
        raise ValueError('Release-Prüfsummen weichen ab')
    with ZipFile(dist / NAME) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or archive.testzip():
            raise ValueError('Originalarchiv beschädigt')
        members = {name: archive.read(name) for name in names}
    verify_members(members, legacy)
    report = json.loads((dist / 'release-bestand.json').read_text())
    if report != inventory(members, legacy):
        raise ValueError('Release-Inventar weicht vom Archiv ab')
    print(f'{TAG}: {len(members)} Dateien, {len(members) - len(legacy)} Nachtragsunterlagen, geprüft.')


def inventory(members, legacy):
    return {'schema_version': 1, 'tag': TAG, 'base_release_archive_sha256': OLD_RELEASE_SHA256,
            'case_files': len(members), 'additional_files': len(members) - len(legacy),
            'case_members_sha256': {name: sha256(data).hexdigest() for name, data in sorted(members.items())}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', required=True, type=Path)
    parser.add_argument('--verify-only', action='store_true')
    parser.add_argument('--legacy-archive', type=Path, help='Veröffentlichtes v3-Archiv zur unabhängigen Gegenprüfung')
    args = parser.parse_args()
    builder = legacy_builder()
    legacy = builder.case_members()
    if args.legacy_archive:
        check_legacy(args.legacy_archive, legacy)
    dist = args.dist.resolve()
    if not args.verify_only:
        if dist.exists() and any(dist.iterdir()):
            raise ValueError('Ein leeres Ausgabeziel ist erforderlich')
        members = working_copy(legacy)
        verify_members(members, legacy)
        dist.mkdir(parents=True, exist_ok=True)
        builder.write_case(dist / NAME, members)
        (dist / 'release-bestand.json').write_text(json.dumps(inventory(members, legacy), indent=2) + '\n')
        (dist / 'checksums-sha256.txt').write_text(''.join(
            f'{sha256(path.read_bytes()).hexdigest()}  {path.name}\n' for path in sorted(dist.iterdir())))
    verify_release(dist, legacy)


if __name__ == '__main__':
    main()
