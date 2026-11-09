#!/usr/bin/env python3
"""Baut und prüft das Paket für die Schulung zum Projekteinkauf."""
from __future__ import annotations

import argparse
from email import policy
from email.parser import BytesParser
from hashlib import sha256
import importlib.util
from io import BytesIO
import json
from pathlib import Path
import shutil
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'projekteinkauf-baubranche'
VERSION = '445.35.11'
TAG = f'{PLUGIN}-v{VERSION}'
WORKSHOP = 'Projekteinkauf_Baubranche_7_Testakten_und_Vorlagen.zip'
DEBRIEF = 'Projekteinkauf_Baubranche_Nachbesprechung.zip'


def load_script(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), ROOT / 'scripts' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def checksum(path):
    return sha256(path.read_bytes()).hexdigest()


def inventory(archive_path, *, case_zip):
    with ZipFile(archive_path) as archive:
        names = archive.namelist()
        if archive.testzip() or len(names) != len(set(names)):
            raise ValueError('Fehlerhafter Archivbestand: ' + archive_path.name)
        if case_zip and (names[0] != NOTICE_FILENAME or archive.read(NOTICE_FILENAME) != NOTICE_BYTES
                         or any('/' in name or '\\' in name or name.endswith('.md') for name in names)):
            raise ValueError('Hinweis oder flache Archivstruktur fehlerhaft: ' + archive_path.name)
        entries = {}
        for name in names:
            data = archive.read(name)
            record = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
            if name.endswith('.pdf'):
                if issues := pdf_content_errors(data):
                    raise ValueError(f'{archive_path.name}/{name}: {issues}')
                record['pages'] = len(PdfReader(BytesIO(data)).pages)
            entries[name] = record
    return entries


def build_case(case, dist, rebuild, native, single, native_check, pdf_check):
    directory = ROOT / 'testakten' / case['slug']
    pairs = document_arcname_pairs(directory)
    if {path.name for path, _ in pairs} != {doc['filename'] for doc in case['documents']}:
        raise ValueError('Aktenstücke weichen vom kuratierten Bestand ab: ' + case['id'])
    single_zip, _ = single.build_single(directory, dist)
    pdf_check.assert_same(single_zip.name, [NOTICE_FILENAME, *pdf_check.expected_arcnames(directory)],
                          pdf_check.zip_entries(single_zip, expected_suffix='.pdf'))
    writer = PdfWriter()
    writer.add_metadata({'/Title': case['title'], '/Author': case.get('company', 'Limmerbogen Bau GmbH'),
                         '/Subject': f"{case['id']} · {case.get('project', 'Bildungscampus Leineaue')}"})
    with ZipFile(single_zip) as archive:
        for path, name in pairs:
            pdf = PdfReader(BytesIO(archive.read(name)))
            if path.suffix == '.eml':
                message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                attachments = [part.get_filename() for part in message.iter_attachments()]
                text = ''.join(''.join((page.extract_text() or '').split()) for page in pdf.pages)
                if any(not filename or filename not in text for filename in attachments):
                    raise ValueError('Anlage fehlt in der PDF-Lesefassung: ' + path.name)
            writer.add_outline_item(path.name, len(writer.pages))
            for page in pdf.pages:
                writer.add_page(page)
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    combined = directory / 'gesamt-pdf' / (case['slug'] + '_gesamt.pdf')
    buffer = BytesIO()
    writer.write(buffer)
    data = buffer.getvalue()
    if rebuild:
        combined.parent.mkdir(exist_ok=True)
        temporary = combined.with_suffix('.tmp')
        temporary.write_bytes(data)
        temporary.replace(combined)
    elif combined.read_bytes() != data:
        raise ValueError('Lesefassung ist veraltet: ' + case['id'])
    if problems := pdf_content_errors(data):
        raise ValueError(f'{case["id"]}: {problems}')
    shutil.copyfile(combined, dist / combined.name)
    original_zip, _ = native.build_single(directory, dist)
    native_check.assert_same(original_zip.name, native_check.expected_entries(directory),
                             native_check.zip_entries(original_zip, require_notice=True))
    with ZipFile(original_zip) as archive:
        for path, _ in pairs:
            if archive.read(path.name) != path.read_bytes():
                raise ValueError(f'{case["id"]}: verändertes Original {path.name}')
        if archive.read(combined.name) != data:
            raise ValueError('Lesefassung im Originalarchiv weicht ab: ' + case['id'])
    print(f"{case['id']}: {len(pairs)} Dokumente, {len(writer.pages)} Seiten", flush=True)
    return {'id': case['id'], 'slug': case['slug'], 'documents': len(pairs),
            'pages': len(writer.pages), 'combined': combined.name, 'original': original_zip.name,
            'individual': single_zip.name, 'combined_sha256': sha256(data).hexdigest()}


def build(dist, rebuild):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Das Release-Ausgabeziel muss leer sein.')
    dist.mkdir(parents=True, exist_ok=True)
    source = ROOT / PLUGIN
    package = load_script('build-compatibility-release')
    sources = package.sources(ROOT, source)
    package_zip = dist / (PLUGIN + '.zip')
    package.write_zip(package_zip, sources)
    plugin_hashes = package.verify_zip(package_zip, sources)
    package.CHECKS.validate_plugin_zip(dist, PLUGIN, VERSION)
    package.CHECKS.validate_skill_sources(package_zip, source)
    prompts = {source / f'{PLUGIN}-{mode}.md': f'{PLUGIN}-{mode}.md'
               for mode in ('werkstatt', 'schnellstart')}
    prompts[ROOT / 'testakten/megaprompts' / (PLUGIN + '.md')] = PLUGIN + '-master-prompt.md'
    for path, name in prompts.items():
        shutil.copyfile(path, dist / name)
    native = load_script('build-testakten-release-zips')
    single = load_script('build-testakten-einzelpdf-zips')
    native_check = load_script('validate-testakten-release-zips')
    pdf_check = load_script('validate-testakten-einzelpdf-zips')
    cases = load_script('build-projekteinkauf-baubranche-akten').cases()
    records = [build_case(case, dist, rebuild, native, single, native_check, pdf_check) for case in cases]
    with ZipFile(dist / WORKSHOP, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for record in records:
            native.write_file(archive, dist / record['original'], record['original'])
        for path in sorted((source / 'templates').iterdir()):
            native.write_file(archive, path, path.name)
    with ZipFile(dist / DEBRIEF, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for case in cases:
            path = ROOT / 'quality' / PLUGIN / 'nachbesprechung' / (case['id'] + '_Nachbesprechung.pdf')
            native.write_file(archive, path, path.name)
    report = {'schema_version': 1, 'tag': TAG, 'version': VERSION, 'cases': records,
              'plugin_members_sha256': plugin_hashes,
              'archives': {path.name: inventory(path, case_zip=path != package_zip)
                           for path in sorted(dist.glob('*.zip'))}}
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / 'checksums-sha256.txt').write_text(''.join(f'{checksum(path)}  {path.name}\n'
                                                      for path in sorted(dist.iterdir())))
    verify(dist)


def verify(dist):
    report = json.loads((dist / 'release-bestand.json').read_text())
    layouts = {'445.35.10': (6, 7), VERSION: (7, 9)}
    version = report.get('version')
    if version not in layouts or report['tag'] != f'{PLUGIN}-v{version}':
        raise ValueError('Unerwarteter Komponentenstand.')
    case_count, template_count = layouts[version]
    asset_count = case_count * 3 + 8
    hashes = dict(line.split('  ', 1)[::-1] for line in (dist / 'checksums-sha256.txt').read_text().splitlines())
    if set(hashes) != {path.name for path in dist.iterdir()} - {'checksums-sha256.txt'} or len(hashes) != asset_count - 1:
        raise ValueError(f'Der Release muss genau {asset_count} Dateien enthalten.')
    for name, digest in hashes.items():
        if checksum(dist / name) != digest:
            raise ValueError('Prüfsummenabweichung: ' + name)
    if len(report['cases']) != case_count:
        raise ValueError('Unerwartete Zahl an Testakten im Inventar.')
    for name, members in report['archives'].items():
        if inventory(dist / name, case_zip=name != PLUGIN + '.zip') != members:
            raise ValueError('Inventarabweichung: ' + name)
    with ZipFile(dist / (PLUGIN + '.zip')) as archive:
        names = archive.namelist()
        if sum(name.endswith('/SKILL.md') for name in names) != 9:
            raise ValueError('Das Plugin muss neun Skills enthalten.')
        if any('Nachbesprechung' in name for name in names):
            raise ValueError('Nachbesprechung gehört außerhalb des Plugins.')
    workshop = f'Projekteinkauf_Baubranche_{case_count}_Testakten_und_Vorlagen.zip'
    with ZipFile(dist / workshop) as archive:
        if len(archive.namelist()) != 1 + case_count + template_count:
            raise ValueError(f'Workshop-ZIP muss {case_count} Akten und {template_count} Vorlagen enthalten.')
        for case in report['cases']:
            if sha256(archive.read(case['original'])).hexdigest() != hashes[case['original']]:
                raise ValueError('Abweichende Workshop-Akte: ' + case['id'])
            with ZipFile(dist / case['original']) as original:
                if sha256(original.read(case['combined'])).hexdigest() != hashes[case['combined']]:
                    raise ValueError('Abweichende Lesefassung: ' + case['id'])
                if any('Nachbesprechung' in name for name in original.namelist()):
                    raise ValueError('Moderationsmaterial in der Arbeitsakte: ' + case['id'])
    print(f"{report['tag']}: {asset_count} Dateien, {sum(c['documents'] for c in report['cases'])} Originale, "
          f"{sum(c['pages'] for c in report['cases'])} Seiten.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    parser.add_argument('--rebuild-pdfs', action='store_true')
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    if args.verify_only:
        verify(args.dist.resolve())
    else:
        build(args.dist.resolve(), args.rebuild_pdfs)
