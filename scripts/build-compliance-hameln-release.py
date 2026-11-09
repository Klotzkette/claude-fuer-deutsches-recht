#!/usr/bin/env python3
"""Baut die Hamelner Compliance-Werkstatt einschließlich aller 35 Akten.

Das leere Ausgabeziel schützt bestehende Releases. --rebuild-pdfs erneuert
die Lesefassungen aus denselben gerenderten Einzeldateien wie die ZIPs.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from hashlib import sha256
import importlib.util
from io import BytesIO
import json
from pathlib import Path
import shutil
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, notice_text_errors, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'compliance-abteilung-grosskonzern'
VERSION = '445.35.13'
TAG = PLUGIN + '-v' + VERSION
MATERIAL = ROOT / 'scripts/data/compliance-hameln-vertiefung.json'
FACHVERTIEFUNG = MATERIAL.with_name('compliance-hameln-fachvertiefung.json')
WORKSHOP = 'Hameln_Compliance_35_Testakten_und_Vorlagen.zip'
DEBRIEF = 'Hameln_Compliance_Nachbesprechung_35.zip'


def module(name):
    spec = importlib.util.spec_from_file_location('compliance_' + name.replace('-', '_'), ROOT / 'scripts' / name)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def inspect_archive(path, *, flat=False):
    with ZipFile(path) as archive:
        names = archive.namelist()
        if archive.testzip() or len(names) != len(set(names)):
            raise ValueError('Beschädigtes oder mehrdeutiges ZIP: ' + path.name)
        if flat:
            if names[0] != NOTICE_FILENAME or notice_text_errors(archive.read(NOTICE_FILENAME)):
                raise ValueError('Herkunftshinweis fehlt: ' + path.name)
            if any('/' in n or '\\' in n or n.lower().endswith('.md') for n in names):
                raise ValueError('Unzulässiger Aktenpfad: ' + path.name)
        result = {}
        for name in names:
            data = archive.read(name)
            entry = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
            if name.lower().endswith('.pdf'):
                if pdf_content_errors(data):
                    raise ValueError('Hinweistext in PDF: ' + path.name + '/' + name)
                entry['pages'] = len(PdfReader(BytesIO(data)).pages)
                if not entry['pages']:
                    raise ValueError('Leeres PDF: ' + name)
            result[name] = entry
        return result


def build_case(task):
    case, destination, rebuild = task
    dist = Path(destination)
    directory = ROOT / 'testakten' / case['slug']
    pairs = document_arcname_pairs(directory)
    separate = module('build-testakten-einzelpdf-zips.py')
    native = module('build-testakten-release-zips.py')
    separate_check = module('validate-testakten-einzelpdf-zips.py')
    native_check = module('validate-testakten-release-zips.py')
    individual, _ = separate.build_single(directory, dist)
    separate_check.assert_same(individual.name, [NOTICE_FILENAME, *separate_check.expected_arcnames(directory)],
                              separate_check.zip_entries(individual, expected_suffix='.pdf'))
    writer = PdfWriter()
    writer.add_metadata({'/Title': case['title'], '/Author': 'Merrensteg Elektrosysteme SE',
                         '/Subject': 'Compliance-Arbeitsakte ' + case['nr']})
    with ZipFile(individual) as archive:
        for source, arcname in pairs:
            reader = PdfReader(BytesIO(archive.read(arcname)))
            first_page = len(writer.pages)
            for page in reader.pages:
                writer.add_page(page)
            writer.add_outline_item(source.name, first_page)
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    buffer = BytesIO()
    writer.write(buffer)
    data = buffer.getvalue()
    combined = directory / 'gesamt-pdf' / (case['slug'] + '_gesamt.pdf')
    if rebuild:
        combined.parent.mkdir(exist_ok=True)
        combined.write_bytes(data)
    elif not combined.is_file() or combined.read_bytes() != data:
        raise ValueError('Lesefassung veraltet; --rebuild-pdfs erforderlich: ' + case['slug'])
    if pdf_content_errors(data):
        raise ValueError('Hinweis im Gesamt-PDF: ' + case['slug'])
    shutil.copyfile(combined, dist / combined.name)
    original, _ = native.build_single(directory, dist)
    native_check.assert_same(original.name, native_check.expected_entries(directory),
                             native_check.zip_entries(original, require_notice=True))
    with ZipFile(original) as archive:
        for source, _ in pairs:
            if archive.read(source.name) != source.read_bytes():
                raise ValueError('Verändertes Original im ZIP: ' + source.name)
        if archive.read(combined.name) != data:
            raise ValueError('Abweichende Lesefassung im ZIP: ' + case['slug'])
    result = {'nr': case['nr'], 'slug': case['slug'], 'documents': len(pairs),
              'pages': len(writer.pages), 'combined_sha256': sha256(data).hexdigest(),
              'original': original.name, 'individual': individual.name,
              'source_sha256': {source.name: sha256(source.read_bytes()).hexdigest() for source, _ in pairs}}
    print(case['nr'], case['slug'], len(pairs), len(writer.pages), flush=True)
    return result


def build(dist, *, rebuild=False, jobs=4):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Das Ausgabeziel muss leer sein.')
    dist.mkdir(parents=True, exist_ok=True)
    cases = json.loads(MATERIAL.read_text())['cases']
    if len(cases) != 35 or len({c['slug'] for c in cases}) != 35:
        raise ValueError('35 verschiedene Compliance-Akten sind erforderlich.')
    package = module('build-compatibility-release.py')
    plugin = ROOT / PLUGIN
    for manifest in ('plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json'):
        value = json.loads((plugin / manifest).read_text())
        if (value['name'], value['version']) != (PLUGIN, VERSION):
            raise ValueError('Pluginmanifest weicht ab: ' + manifest)
    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    if next(p['version'] for p in market['plugins'] if p['name'] == PLUGIN) != VERSION:
        raise ValueError('Marketplace-Version weicht ab.')
    files = package.sources(ROOT, plugin)
    archive = dist / (PLUGIN + '.zip')
    package.write_zip(archive, files)
    hashes = package.verify_zip(archive, files)
    package.CHECKS.validate_plugin_zip(dist, PLUGIN, VERSION)
    package.CHECKS.validate_skill_sources(archive, plugin)
    package.CHECKS.validate_focus_skill(archive, plugin, ROOT / 'quality/evals' / (PLUGIN + '.json'))
    for kind in ('werkstatt', 'schnellstart'):
        path = plugin / f'{PLUGIN}-{kind}.md'
        shutil.copyfile(path, dist / path.name)
    shutil.copyfile(ROOT / 'testakten/megaprompts' / (PLUGIN + '.md'), dist / (PLUGIN + '-master-prompt.md'))
    with ProcessPoolExecutor(max_workers=jobs) as executor:
        results = list(executor.map(build_case, ((c, str(dist), rebuild) for c in cases)))
    if sum(c['documents'] for c in results) != 420:
        raise ValueError('338 ursprüngliche und 82 ergänzende Dokumente erwartet.')
    native = module('build-testakten-release-zips.py')
    with ZipFile(dist / WORKSHOP, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for c in cases:
            path = dist / ('testakte-' + c['slug'] + '.zip')
            native.write_file(archive, path, path.name)
            path = plugin / 'templates' / (c['slug'] + '.docx')
            native.write_file(archive, path, path.name)
    with ZipFile(dist / DEBRIEF, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for c in cases:
            paths = list((ROOT / 'quality/hameln-compliance/nachbesprechung').glob(c['slug'] + '-nachbesprechung.pdf'))
            paths += list((ROOT / 'quality/ki-arbeit-reskilling/nachbesprechung').glob(c['slug'] + '-nachbesprechung.pdf'))
            if len(paths) != 1:
                raise ValueError('Nachbesprechung fehlt oder ist mehrdeutig: ' + c['slug'])
            native.write_file(archive, paths[0], paths[0].name)
    members = {p.name: inspect_archive(p, flat=p.name != PLUGIN + '.zip') for p in sorted(dist.glob('*.zip'))}
    report = {'schema_version': 1, 'tag': TAG, 'version': VERSION, 'cases': results,
              'material_sha256': sha256(MATERIAL.read_bytes()).hexdigest(),
              'fachvertiefung_sha256': sha256(FACHVERTIEFUNG.read_bytes()).hexdigest(),
              'plugin_members_sha256': hashes, 'archives': members}
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / 'checksums-sha256.txt').write_text(''.join(f'{sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(dist.iterdir())))
    if len(list(dist.iterdir())) != 113:
        raise ValueError('113 Release-Dateien erwartet.')
    print(f'{TAG}: 35 Akten, {sum(c["documents"] for c in results)} Dokumente, {sum(c["pages"] for c in results)} Seiten; 113 Release-Dateien geprüft.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    parser.add_argument('--rebuild-pdfs', action='store_true')
    parser.add_argument('--jobs', type=int, default=4)
    args = parser.parse_args()
    build(args.dist.resolve(), rebuild=args.rebuild_pdfs, jobs=args.jobs)
