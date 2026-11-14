#!/usr/bin/env python3
"""Neun Originalakten mit getrennten Grundakten und überprüfbaren PDF-Lesefassungen."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, pdf_content_errors
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_grundakte import check_intake_member
from testakte_zip_common import safe_archive_name, working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
TAG = 'insolvenz-arbeitsakten-v1.0.0'
CASES = (
    'insolvenzreife-keramikfabrik-cottbus',
    'insolvenzreife-metallbau-berlin-zehlendorf',
    'insolvenzreife-hubschrauber-prenzlau',
    'fintech-darlehen-vertragsuebernahme-bremen',
    'insolvenzanfechtung-blechliebe-bamberg',
    'insolvenzanfechtung-faltenwurf-fuerth',
    'insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln',
    'insolvenzanfechtung-veedelwende-zession-koeln',
    'forderungsmanagement-baeckerei-behaeltertausch-hamburg',
)
BUNDLES = {
    'Insolvenzreife_Drei_Originalakten.zip': CASES[:3],
    'Neun_Arbeitsakten_Originalformate.zip': CASES,
}
INTAKE_BUNDLE = 'Insolvenzreife_Drei_Grundakten.zip'
INVENTORY = 'release-bestand.json'
CHECKSUMS = 'checksums-sha256.txt'


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), ROOT / 'scripts' / (name + '.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def sha(data):
    return hashlib.sha256(data).hexdigest()


def asset_names():
    return {*(f'testakte-{slug}{suffix}.zip' for slug in CASES for suffix in ('', '-einzelpdfs')),
            *(f'{slug}_gesamt.pdf' for slug in CASES), *BUNDLES, INTAKE_BUNDLE, INVENTORY, CHECKSUMS}


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Das Ausgabeverzeichnis muss leer sein.')
    dist.mkdir(parents=True, exist_ok=True)
    native = module('build-testakten-release-zips')
    single = module('build-testakten-einzelpdf-zips')
    for slug in CASES:
        directory = ROOT / 'testakten' / slug
        native.build_single(directory, dist)
        pdf_zip, _ = single.build_single(directory, dist)
        stored = directory / 'gesamt-pdf' / f'{slug}_gesamt.pdf'
        stored.parent.mkdir(exist_ok=True)
        if slug == 'fintech-darlehen-vertragsuebernahme-bremen':
            module('build-fintech-bremen-pakete').build_release_pdf(directory)
        else:
            writer = PdfWriter()
            with ZipFile(pdf_zip) as archive:
                for _, name in document_arcname_pairs(directory):
                    start = len(writer.pages)
                    writer.append(PdfReader(io.BytesIO(archive.read(name))), import_outline=False)
                    writer.add_outline_item(name, start)
            writer.add_metadata({'/Title': directory.joinpath('README.md').read_text().splitlines()[0].removeprefix('# '),
                                 '/Author': 'Klotzkette'})
            with stored.open('wb') as stream:
                writer.write(stream)
        shutil.copyfile(stored, dist / stored.name)
        print(slug, flush=True)
    for name, slugs in BUNDLES.items():
        with ZipFile(dist / name, 'x') as archive:
            native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
            for slug in slugs:
                name = f'testakte-{slug}.zip'
                native.write_file(archive, dist / name, name)
    with ZipFile(dist / INTAKE_BUNDLE, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for slug in CASES[:3]:
            for source, name in working_dump_archive_pairs(ROOT / 'testakten' / slug, include_gesamt_pdf=False):
                if name.startswith('Grundakte/'):
                    native.write_file(archive, source, slug + '/' + name)
    report = inspect(dist, compare_sources=True)
    (dist / INVENTORY).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / CHECKSUMS).write_text(''.join(f'{sha(p.read_bytes())}  {p.name}\n' for p in sorted(dist.iterdir())), encoding='ascii')
    verify(dist, compare_sources=True)
    return report


def checked_zip(path):
    archive = ZipFile(path)
    names = archive.namelist()
    if (not names or names[0] != NOTICE_FILENAME or archive.read(NOTICE_FILENAME) != NOTICE_BYTES
            or len(names) != len(set(n.casefold() for n in names)) or archive.testzip()
            or any(not safe_archive_name(n, allow_directories=True) for n in names)):
        archive.close()
        raise ValueError(f'Archivstruktur oder Pflicht-Hinweis fehlerhaft: {path.name}')
    return archive


def page_text(page):
    return ' '.join((page.extract_text() or '').split())


def combined_order(slug, names):
    if slug != 'fintech-darlehen-vertragsuebernahme-bremen':
        return list(names)
    def key(name):
        path = Path(name)
        rank = 0 if path.name.startswith('00_Gerichtliche') else 1 if path.name.startswith('01_Klage') else 2
        return (path.parts[0], rank, path.name.casefold())
    return sorted(names, key=key)


def inspect(dist, *, compare_sources):
    report = {'tag': TAG, 'cases': {}, 'bundles': {}}
    for slug in CASES:
        directory = ROOT / 'testakten' / slug
        with checked_zip(dist / f'testakte-{slug}.zip') as archive:
            native = {name: archive.read(name) for name in archive.namelist()[1:]}
        if any(name.endswith('.md') or '_gesamt.pdf' in name for name in native):
            raise ValueError(f'Redaktion oder Gesamt-PDF im Originalarchiv: {slug}')
        intake = {name: data for name, data in native.items() if name.startswith('Grundakte/')}
        if not intake:
            raise ValueError(f'Grundakte fehlt: {slug}')
        for name, data in intake.items():
            check_intake_member(name, data)
        if compare_sources:
            expected = {name: source.read_bytes() for source, name in working_dump_archive_pairs(directory, include_gesamt_pdf=False)}
            if native != expected:
                raise ValueError(f'Originale weichen von Quellbestand ab: {slug}')
        pages = 0
        individual = {}
        page_contents = {}
        with checked_zip(dist / f'testakte-{slug}-einzelpdfs.zip') as archive:
            for name in archive.namelist()[1:]:
                data = archive.read(name)
                if not name.endswith('.pdf'):
                    raise ValueError(f'Keine PDF: {name}')
                reader = PdfReader(io.BytesIO(data))
                if not reader.pages or pdf_content_errors(data):
                    raise ValueError(f'PDF leer oder mit Warntext: {slug}/{name}')
                count = len(reader.pages)
                individual[name] = {'sha256': sha(data), 'pages': count}
                page_contents[name] = [page_text(page) for page in reader.pages]
                pages += count
            if compare_sources and set(individual) != {name for _, name in document_arcname_pairs(directory)}:
                raise ValueError(f'Einzel-PDF-Bestand abweichend: {slug}')
        for name, data in native.items():
            if not name.endswith('.pdf'):
                continue
            candidates = (name, name.removeprefix('Grundakte/'))
            matching = [candidate for candidate in dict.fromkeys(candidates) if candidate in individual]
            if not matching:
                # Some intake selections deliberately flatten their original folders.
                matching = [candidate for candidate in individual if Path(candidate).name == Path(name).name]
            if len(matching) != 1 or individual[matching[0]]['sha256'] != sha(data):
                raise ValueError(f'Original-PDF fehlt oder ist nicht bytegleich: {slug}/{name}')
        combined = PdfReader(dist / f'{slug}_gesamt.pdf')
        # Weserfunken hat zusätzlich ein Dokumentenregister, andere Akten nicht.
        register = (len(individual) + 21) // 22 if slug == 'fintech-darlehen-vertragsuebernahme-bremen' else 0
        if len(combined.pages) != pages + register or pdf_content_errors((dist / f'{slug}_gesamt.pdf').read_bytes()):
            raise ValueError(f'Gesamt-PDF stimmt nicht: {slug}')
        expected_pages = [text for name in combined_order(slug, individual) for text in page_contents[name]]
        if [page_text(page) for page in list(combined.pages)[register:]] != expected_pages:
            raise ValueError(f'Gesamt-PDF enthält andere oder falsch geordnete Dokumentseiten: {slug}')
        report['cases'][slug] = {
            'originals': len(native), 'intake_originals': len(intake),
            'formats': dict(sorted(Counter(Path(n).suffix for n in native).items())),
            'pdf_documents': len(individual), 'document_pages': pages, 'register_pages': register,
            'total_pages': len(combined.pages),
            'original_files': {name: sha(data) for name, data in native.items()},
            'pdf_files': individual,
        }
    for name, slugs in BUNDLES.items():
        with checked_zip(dist / name) as archive:
            expected = {f'testakte-{slug}.zip': (dist / f'testakte-{slug}.zip').read_bytes() for slug in slugs}
            if {n: archive.read(n) for n in archive.namelist()[1:]} != expected:
                raise ValueError(f'Sammelpaket stimmt nicht: {name}')
            report['bundles'][name] = len(expected)
    with checked_zip(dist / INTAKE_BUNDLE) as archive:
        expected = {}
        for slug in CASES[:3]:
            with checked_zip(dist / f'testakte-{slug}.zip') as original:
                expected.update({slug + '/' + n: original.read(n) for n in original.namelist() if n.startswith('Grundakte/')})
        if {n: archive.read(n) for n in archive.namelist()[1:]} != expected:
            raise ValueError('Grundakten-Sammelpaket weicht von den Einzelakten ab.')
        report['bundles'][INTAKE_BUNDLE] = len(expected)
    return report


def verify(dist, *, compare_sources=True):
    if {p.name for p in dist.iterdir()} != asset_names():
        raise ValueError('Releasebestand unvollständig oder unerwartete Dateien vorhanden.')
    lines = (dist / CHECKSUMS).read_text(encoding='ascii').splitlines()
    hashes = dict(line.split('  ', 1)[::-1] for line in lines)
    if len(hashes) != len(lines) or set(hashes) != asset_names() - {CHECKSUMS}:
        raise ValueError('Prüfsummenverzeichnis unvollständig.')
    for name, digest in hashes.items():
        if sha((dist / name).read_bytes()) != digest:
            raise ValueError(f'Prüfsumme abweichend: {name}')
    actual = inspect(dist, compare_sources=compare_sources)
    if actual != json.loads((dist / INVENTORY).read_text()):
        raise ValueError('Inventar stimmt nicht mit den tatsächlich enthaltenen Dokumenten überein.')
    return actual


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', required=True, type=Path)
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--offline', action='store_true', help='Heruntergeladene Assets ohne lokalen Quellabgleich prüfen')
    args = parser.parse_args()
    if args.offline and not args.verify:
        parser.error('--offline ist nur zusammen mit --verify zulässig')
    report = verify(args.dist, compare_sources=not args.offline) if args.verify else build(args.dist)
    print(json.dumps({slug: {k: v for k, v in row.items() if k not in {'original_files', 'pdf_files'}}
                      for slug, row in report['cases'].items()}, ensure_ascii=False, indent=2))
