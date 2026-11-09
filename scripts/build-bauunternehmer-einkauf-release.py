#!/usr/bin/env python3
"""Baut und prüft die Bauunternehmer-Einkaufskomponente mit der Krimpfort-Akte."""
from __future__ import annotations

import argparse
from email import policy
from email.parser import BytesParser
import importlib.util
import json
from pathlib import Path
import shutil
from zipfile import ZipFile

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'bauunternehmer-einkauf'
VERSION = '445.35.12'
TAG = f'{PLUGIN}-v{VERSION}'
SLUG = f'{PLUGIN}-brandschutztueren-krimpfort'
ORIGINAL = f'testakte-{SLUG}.zip'
SINGLES = f'testakte-{SLUG}-einzelpdfs.zip'
COMBINED = f'{SLUG}_gesamt.pdf'
WORKSHOP = 'Bauunternehmer_Einkauf_Brandschutztueren_Workshop.zip'
DEBRIEF = 'BE-01_Nachbesprechung.pdf'
TEMPLATES = {f'{SLUG}.docx', 'Verhandlungsleitfaden.docx', 'Brandschutztueren_Preisspiegel.xlsx'}
PROMPTS = {'werkstatt', 'schnellstart', 'master-prompt'}


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
        'archives': {path.name: COMMON.inventory(path, case_zip=path != plugin_zip)
                     for path in sorted(dist.glob('*.zip'))},
    }
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / 'checksums-sha256.txt').write_text(''.join(
        f'{COMMON.checksum(path)}  {path.name}\n' for path in sorted(dist.iterdir())))
    verify(dist)


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
        if COMMON.inventory(dist / name, case_zip=name != f'{PLUGIN}.zip') != entries:
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
        attached = set()
        for name in original.namelist():
            if name.endswith('.eml'):
                message = BytesParser(policy=policy.default).parsebytes(original.read(name))
                for part in message.iter_attachments():
                    filename = part.get_filename()
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
