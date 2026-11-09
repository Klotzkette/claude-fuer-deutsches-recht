#!/usr/bin/env python3
"""Baut und prüft die Bauunternehmer-Einkaufskomponente mit der Krimpfort-Akte."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from decimal import Decimal
from email import policy
from email.parser import BytesParser
import importlib.util
from io import BytesIO, StringIO
import json
from pathlib import Path, PurePosixPath
import shutil
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from openpyxl import load_workbook
from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'bauunternehmer-einkauf'
VERSION = '445.35.14'
TAG = f'{PLUGIN}-v{VERSION}'
SLUG = f'{PLUGIN}-brandschutztueren-krimpfort'
ORIGINAL = f'testakte-{SLUG}.zip'
SINGLES = f'testakte-{SLUG}-einzelpdfs.zip'
COMBINED = f'{SLUG}_gesamt.pdf'
WORKSHOP = 'Bauunternehmer_Einkauf_Brandschutztueren_Workshop.zip'
DEBRIEF = 'BE-01_Nachbesprechung.pdf'
TEMPLATES = {f'{SLUG}.docx', 'Verhandlungsleitfaden.docx', 'Brandschutztueren_Preisspiegel.xlsx'}
PROMPTS = {'werkstatt', 'schnellstart', 'master-prompt'}
STRUCTURED = {ORIGINAL, SINGLES}
HISTORY = '00_LV_Entstehung'


def load_builder():
    path = ROOT / 'scripts/build-projekteinkauf-baubranche-release.py'
    spec = importlib.util.spec_from_file_location('projekteinkauf_release', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COMMON = load_builder()


def build(dist, rebuild):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Das Release-Ausgabeziel muss leer sein.')
    dist.mkdir(parents=True, exist_ok=True)
    source = ROOT / PLUGIN
    package = COMMON.load_script('build-compatibility-release')
    sources = package.sources(ROOT, source)
    plugin_zip = dist / f'{PLUGIN}.zip'
    package.write_zip(plugin_zip, sources)
    package.verify_zip(plugin_zip, sources)
    package.CHECKS.validate_plugin_zip(dist, PLUGIN, VERSION)
    package.CHECKS.validate_skill_sources(plugin_zip, source)
    for mode in sorted(PROMPTS):
        path = (ROOT / f'testakten/megaprompts/{PLUGIN}.md' if mode == 'master-prompt'
                else source / f'{PLUGIN}-{mode}.md')
        shutil.copyfile(path, dist / f'{PLUGIN}-{mode}.md')

    native = COMMON.load_script('build-testakten-release-zips')
    single = COMMON.load_script('build-testakten-einzelpdf-zips')
    native_check = COMMON.load_script('validate-testakten-release-zips')
    pdf_check = COMMON.load_script('validate-testakten-einzelpdf-zips')
    case, _, _ = COMMON.load_script('build-bauunternehmer-einkauf-akten').case_data()
    record = COMMON.build_case(case, dist, rebuild, native, single, native_check, pdf_check)
    shutil.copyfile(ROOT / 'quality' / PLUGIN / DEBRIEF, dist / DEBRIEF)
    with ZipFile(dist / WORKSHOP, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        native.write_file(archive, dist / ORIGINAL, ORIGINAL)
        for name in sorted(TEMPLATES):
            native.write_file(archive, source / 'templates' / name, name)
    report = {
        'schema_version': 1, 'tag': TAG, 'version': VERSION, 'case': record,
        'archives': {path.name: COMMON.inventory(path, case_zip=path != plugin_zip,
                                                 allow_directories=path.name in STRUCTURED)
                     for path in sorted(dist.glob('*.zip'))},
    }
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / 'checksums-sha256.txt').write_text(''.join(
        f'{COMMON.checksum(path)}  {path.name}\n' for path in sorted(dist.iterdir())))
    verify(dist)


def verify_mengenbruecke(original, x83):
    def rows(name):
        return list(csv.DictReader(StringIO(original.read(name).decode('utf-8-sig'))))

    planning = f'{HISTORY}/01_Planung'
    draft = {row['Ebene']: row for row in rows(f'{planning}/P02_Tuerliste_T03_Ebenen.csv')}
    changes = Counter()
    for row in rows(f'{planning}/P07_Tueraenderungen_T03_T04.csv'):
        changes[row['Ebene'], row['Gruppe']] += int(row['Delta St'])
    register = rows('04a_Tuerregister_500.csv')
    if len({row['Tür-ID'] for row in register}) != len(register):
        raise ValueError('Doppelte Tür-ID im finalen Register.')
    final = Counter((row['Ebene'], row['Türtyp']) for row in register)
    lv = ET.fromstring(original.read(x83))
    book = load_workbook(BytesIO(original.read(f'{HISTORY}/03_LV_Freigabe/L02_Mengenueberleitung_R1.xlsx')),
                         data_only=True, read_only=True)
    try:
        sheet = book['Mengenbruecke']
        positions = lv.findall('.//{*}Item')
        if len(positions) != 5:
            raise ValueError('Fünf X83-Positionen erwartet.')
        for row, position in enumerate(positions, 4):
            key = position.attrib['ID'].removeprefix('POS_')
            initial = sum(int(level[key]) for level in draft.values())
            delta = sum(changes[level, key] for level in draft)
            qty = Decimal(position.findtext('{*}Qty'))
            if (any(int(draft[level][key]) + changes[level, key] != final[level, key] for level in draft)
                    or sum(final[level, key] for level in draft) != qty):
                raise ValueError('Mengenüberleitung widerspricht Register oder X83: ' + key)
            expected = (position.attrib['RNoPart'], key, initial, delta, qty, qty, 0)
            if tuple(cell.value for cell in sheet[row][:7]) != expected:
                raise ValueError('Abweichung in der Excel-Mengenüberleitung: ' + key)
        if tuple(cell.value for cell in sheet[9][2:7]) != (498, 2, 500, 500, 0):
            raise ValueError('Summen der Mengenüberleitung weichen ab.')
    finally:
        book.close()
    expected_ws = {f'E4-{index:03d}' for index in range(73, 83)}
    if {row['Tür-ID'] for row in register if row['Wandtyp'] == 'W-S' and row['Türtyp'] == 'B2'} != expected_ws:
        raise ValueError('W-S-Zuordnung im Register weicht ab.')


def verify(dist):
    files = {f'{PLUGIN}.zip', ORIGINAL, SINGLES, COMBINED, WORKSHOP, DEBRIEF, 'release-bestand.json',
             *(f'{PLUGIN}-{mode}.md' for mode in PROMPTS)}
    hashes = dict(line.split('  ', 1)[::-1] for line in (dist / 'checksums-sha256.txt').read_text().splitlines())
    if set(hashes) != files or {path.name for path in dist.iterdir()} != files | {'checksums-sha256.txt'}:
        raise ValueError('Unerwartete Dateien im Release.')
    for name, digest in hashes.items():
        if COMMON.checksum(dist / name) != digest:
            raise ValueError('Prüfsummenabweichung: ' + name)
    report = json.loads((dist / 'release-bestand.json').read_text())
    if (report['tag'], report['version'], set(report['archives'])) != (
            TAG, VERSION, {f'{PLUGIN}.zip', ORIGINAL, SINGLES, WORKSHOP}):
        raise ValueError('Unerwarteter Komponentenstand.')
    for name, entries in report['archives'].items():
        if COMMON.inventory(dist / name, case_zip=name != f'{PLUGIN}.zip',
                            allow_directories=name in STRUCTURED) != entries:
            raise ValueError('Inventarabweichung: ' + name)
    with ZipFile(dist / f'{PLUGIN}.zip') as plugin, ZipFile(dist / WORKSHOP) as workshop:
        if sum(name.endswith('/SKILL.md') for name in plugin.namelist()) != 10:
            raise ValueError('Das Plugin muss zehn Skills enthalten.')
        if set(workshop.namelist()) != {NOTICE_FILENAME, ORIGINAL, *TEMPLATES}:
            raise ValueError('Workshop-ZIP enthält nicht die Akte und die drei Vorlagen.')
        if workshop.read(ORIGINAL) != (dist / ORIGINAL).read_bytes():
            raise ValueError('Die Workshop-Akte weicht vom Original ab.')
        for name in TEMPLATES:
            if plugin.read(f'templates/{name}') != workshop.read(name):
                raise ValueError('Abweichende Vorlage: ' + name)

    case = report['case']
    with ZipFile(dist / ORIGINAL) as original, ZipFile(dist / SINGLES) as singles:
        if (len(original.namelist()), len(singles.namelist())) != (case['documents'] + 2, case['documents'] + 1):
            raise ValueError('Aktenbestand weicht von den beiden ZIP-Fassungen ab.')
        if original.read(COMBINED) != (dist / COMBINED).read_bytes() or case['combined_sha256'] != hashes[COMBINED]:
            raise ValueError('Die Lesefassung weicht vom Originalarchiv ab.')
        x83 = {name for name in original.namelist() if name.endswith('.x83')}
        x84 = {name for name in original.namelist() if name.endswith('.x84')}
        if len(x83) != 1 or len(x84) != 4:
            raise ValueError('Erwartet sind ein X83 und vier X84.')
        verify_mengenbruecke(original, next(iter(x83)))
        combined = PdfReader(BytesIO(original.read(COMBINED)))
        expected_destinations = []
        page = 0
        directory = ROOT / 'testakten' / SLUG
        for source, member in document_arcname_pairs(directory):
            expected_destinations.append((source.name, page))
            page += len(PdfReader(BytesIO(singles.read(member))).pages)
        if (page != len(combined.pages) or [(item.title, combined.get_destination_page_number(item))
                                           for item in combined.outline] != expected_destinations):
            raise ValueError('Lesezeichen führen nicht an die Anfänge der Aktenstücke.')
        attached = set()
        for name in original.namelist():
            if name.endswith('.eml'):
                message = BytesParser(policy=policy.default).parsebytes(original.read(name))
                for part in message.iter_attachments():
                    filename = (PurePosixPath(name).parent / part.get_filename()).as_posix()
                    if part.get_payload(decode=True) != original.read(filename):
                        raise ValueError(f'{name}: abweichende Anlage {filename}')
                    attached.add(filename)
        if not (x83 | x84) <= attached:
            raise ValueError('Eine GAEB-Datei fehlt als Anlage im Originalschriftverkehr.')
        if any('Nachbesprechung' in name for name in original.namelist()):
            raise ValueError('Moderationsmaterial in der Arbeitsakte.')
    print(f"{TAG}: {len(files) + 1} Release-Dateien, {case['documents']} Originale, {case['pages']} Seiten.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--rebuild-pdfs', action='store_true')
    mode.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    if args.verify_only:
        verify(args.dist.resolve())
    else:
        build(args.dist.resolve(), args.rebuild_pdfs)
