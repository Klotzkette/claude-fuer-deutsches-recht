#!/usr/bin/env python3
"""Baut und prüft die Bauunternehmer-Einkaufskomponente mit drei Krimpfort-Akten."""
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
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'bauunternehmer-einkauf'
VERSION = '445.35.15'
TAG = f'{PLUGIN}-v{VERSION}'
SLUG = f'{PLUGIN}-brandschutztueren-krimpfort'
ORIGINAL = f'testakte-{SLUG}.zip'
SINGLES = f'testakte-{SLUG}-einzelpdfs.zip'
COMBINED = f'{SLUG}_gesamt.pdf'
WORKSHOP = 'Bauunternehmer_Einkauf_3_Praxisakten.zip'
COMPARISONS = ('bauunternehmer-einkauf-lueftung.json', 'bauunternehmer-einkauf-altstadt-bordsteine.json')
DEBRIEF = 'BE-01_Nachbesprechung.pdf'
TEMPLATES = {f'{SLUG}.docx', 'Verhandlungsleitfaden.docx', 'Brandschutztueren_Preisspiegel.xlsx'}
PROMPTS = {'werkstatt', 'schnellstart', 'master-prompt'}
HISTORY = '00_LV_Entstehung'


def load_builder():
    path = ROOT / 'scripts/build-projekteinkauf-baubranche-release.py'
    spec = importlib.util.spec_from_file_location('projekteinkauf_release', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COMMON = load_builder()


def comparisons():
    return [json.loads((ROOT / 'scripts/data' / filename).read_text(encoding='utf-8'))
            for filename in COMPARISONS]


def case_names(slug):
    return f'testakte-{slug}.zip', f'testakte-{slug}-einzelpdfs.zip', f'{slug}_gesamt.pdf'


def build(dist):
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
    directory = ROOT / 'testakten' / SLUG
    native.build_single(directory, dist)
    single.build_single(directory, dist)
    shutil.copyfile(directory / 'gesamt-pdf' / COMBINED, dist / COMBINED)
    module = COMMON.load_script('build-bauunternehmer-einkauf-vergleichsakten')
    for case in comparisons():
        module.build_release(case, ROOT / 'testakten' / case['slug'], dist)
    shutil.copyfile(ROOT / 'quality' / PLUGIN / DEBRIEF, dist / DEBRIEF)
    with ZipFile(dist / WORKSHOP, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for slug in (SLUG, *(case['slug'] for case in comparisons())):
            name, _, _ = case_names(slug)
            native.write_file(archive, dist / name, name)
        for name in sorted(TEMPLATES):
            native.write_file(archive, source / 'templates' / name, name)
    report = inspect(dist)
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


def inspect_case(dist, slug):
    original_name, singles_name, combined_name = case_names(slug)
    directory = ROOT / 'testakten' / slug
    pairs = working_dump_archive_pairs(directory, include_gesamt_pdf=False)
    pdf_pairs = document_arcname_pairs(directory)
    combined = (dist / combined_name).read_bytes()
    if combined != (directory / 'gesamt-pdf' / combined_name).read_bytes():
        raise ValueError(f'{slug}: Lesefassung weicht von der Repository-Fassung ab.')
    combined_pdf = PdfReader(BytesIO(combined))
    flat_outline = combined_pdf.outline
    if slug != SLUG:
        flat_outline = [child for section in flat_outline if isinstance(section, list) for child in section]
    originals = {}
    root_names = {}
    attached = set()
    page_starts = []
    pages = 0
    with ZipFile(dist / original_name) as original, ZipFile(dist / singles_name) as singles:
        if set(original.namelist()) != {NOTICE_FILENAME, *(name for _, name in pairs)}:
            raise ValueError(f'{slug}: abweichender Bestand im Originalformat.')
        if set(singles.namelist()) != {NOTICE_FILENAME, *(name for _, name in pdf_pairs)}:
            raise ValueError(f'{slug}: abweichender Bestand der Einzel-PDFs.')
        for source, name in pairs:
            data = original.read(name)
            if data != source.read_bytes():
                raise ValueError(f'{slug}: verändertes Original {name}.')
            root_names[source.relative_to(directory).as_posix()] = name
            originals[PurePosixPath(name).name] = name
            if name.endswith('.eml'):
                message = BytesParser(policy=policy.default).parsebytes(data)
                for part in message.iter_attachments():
                    attachment = part.get_filename()
                    attached.add((name, attachment, part.get_payload(decode=True)))
        x83 = {name for name in originals if name.endswith('.x83')}
        x84 = {name for name in originals if name.endswith('.x84')}
        if len(x83) != 1 or len(x84) != 4:
            raise ValueError(f'{slug}: erwartet sind ein X83 und vier X84.')
        if not (x83 | x84) <= {name for _, name, _ in attached}:
            raise ValueError(f'{slug}: eine GAEB-Datei fehlt im MIME-Schriftverkehr.')
        for name, attachment, payload in attached:
            relative = originals.get(attachment)
            if not relative or original.read(relative) != payload:
                raise ValueError(f'{slug}: {name} enthält eine abweichende Anlage {attachment}.')
            if name.startswith('Grundakte/') and not relative.startswith('Grundakte/'):
                raise ValueError(f'{slug}: Anlage aus späterem Bearbeitungsstand in {name}.')
        if slug == SLUG:
            class OriginalPositions:
                def read(self, name):
                    return original.read(root_names[name])
            verify_mengenbruecke(OriginalPositions(), next(iter(x83)))
        for source, member in pdf_pairs:
            title = source.name if slug == SLUG else source.relative_to(directory).as_posix()
            page_starts.append((title, pages))
            pages += len(PdfReader(BytesIO(singles.read(member))).pages)
    actual = [(item.title, combined_pdf.get_destination_page_number(item)) for item in flat_outline]
    if actual != page_starts or pages != len(combined_pdf.pages):
        raise ValueError(f'{slug}: Lesezeichen oder Seitenzahlen weichen ab.')
    return {'documents': len(pairs), 'intake': sum(name.startswith('Grundakte/') for _, name in pairs),
            'pages': pages, 'combined_sha256': COMMON.checksum(dist / combined_name)}


def inspect(dist):
    case_data = comparisons()
    names = (SLUG, *(case['slug'] for case in case_data))
    native_zips = {case_names(slug)[0] for slug in names}
    zip_names = native_zips | {case_names(slug)[1] for slug in names}
    archives = {
        name: COMMON.inventory(dist / name, case_zip=name != f'{PLUGIN}.zip', allow_directories=name in zip_names)
        for name in sorted({*zip_names, f'{PLUGIN}.zip', WORKSHOP})
    }
    with ZipFile(dist / f'{PLUGIN}.zip') as plugin, ZipFile(dist / WORKSHOP) as workshop:
        if sum(name.endswith('/SKILL.md') for name in plugin.namelist()) != 10:
            raise ValueError('Das Plugin muss zehn Skills enthalten.')
        if set(workshop.namelist()) != {NOTICE_FILENAME, *native_zips, *TEMPLATES}:
            raise ValueError('Workshop-ZIP enthält nicht die drei Akten und die Vorlagen.')
        for name in native_zips:
            if workshop.read(name) != (dist / name).read_bytes():
                raise ValueError('Die Workshop-Akte weicht vom Original ab: ' + name)
        for name in TEMPLATES:
            if plugin.read(f'templates/{name}') != workshop.read(name):
                raise ValueError('Abweichende Vorlage: ' + name)
    module = COMMON.load_script('bauunternehmer_einkauf_gaeb')
    for case in case_data:
        module.verify_exchange(case, ROOT / 'testakten' / case['slug'])
    return {'schema_version': 1, 'tag': TAG, 'version': VERSION,
            'cases': {slug: inspect_case(dist, slug) for slug in names}, 'archives': archives}


def verify(dist):
    slugs = (SLUG, *(case['slug'] for case in comparisons()))
    files = {f'{PLUGIN}.zip', WORKSHOP, DEBRIEF, 'release-bestand.json',
             *(name for slug in slugs for name in case_names(slug)),
             *(f'{PLUGIN}-{mode}.md' for mode in PROMPTS)}
    hashes = dict(line.split('  ', 1)[::-1] for line in (dist / 'checksums-sha256.txt').read_text().splitlines())
    if set(hashes) != files or {path.name for path in dist.iterdir()} != files | {'checksums-sha256.txt'}:
        raise ValueError('Unerwartete Dateien im Release.')
    for name, digest in hashes.items():
        if COMMON.checksum(dist / name) != digest:
            raise ValueError('Prüfsummenabweichung: ' + name)
    report = json.loads((dist / 'release-bestand.json').read_text())
    if inspect(dist) != report:
        raise ValueError('Abweichendes Release-Inventar.')
    for slug, case in report['cases'].items():
        print(f"{slug}: {case['documents']} Originale, {case['intake']} in der Grundakte, {case['pages']} Seiten.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    (verify if args.verify_only else build)(args.dist.resolve())
