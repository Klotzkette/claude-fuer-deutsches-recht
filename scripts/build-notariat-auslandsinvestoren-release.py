#!/usr/bin/env python3
"""Baut den abgegrenzten Notariatsrelease samt beiden Auslandsinvestorenakten."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import io
import json
from pathlib import Path
import shutil
from zipfile import ZipFile

from pypdf import PdfReader
from testakte_disclaimer import NOTICE_FILENAME, notice_text_errors, pdf_content_errors

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'notariat-alltag'
VERSION = '445.35.7'
TAG = 'notariat-v' + VERSION
CASES = ('notariat-berlin-mumbai-gesellschafterliste', 'notariat-berlin-vae-vertretungsnachweis')


def module(script):
    spec = importlib.util.spec_from_file_location('notariat_' + script.replace('-', '_'), ROOT / 'scripts' / script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def inspect_zip(path, *, case=False):
    with ZipFile(path) as archive:
        names = archive.namelist()
        if archive.testzip() is not None or len(names) != len(set(names)):
            raise ValueError('Beschädigtes oder mehrdeutiges Archiv: ' + path.name)
        if case:
            if names[0] != NOTICE_FILENAME or notice_text_errors(archive.read(NOTICE_FILENAME)):
                raise ValueError('Herkunftshinweis fehlt: ' + path.name)
            if any('/' in name or '\\' in name or name.lower().endswith('.md') for name in names):
                raise ValueError('Aktenarchiv ist nicht flach oder enthält Markdown: ' + path.name)
        result = {}
        for name in names:
            data = archive.read(name)
            member = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
            if name.lower().endswith('.pdf'):
                if pdf_content_errors(data):
                    raise ValueError('Hinweistext in Akten-PDF: ' + name)
                member['pages'] = len(PdfReader(io.BytesIO(data)).pages)
                if member['pages'] < 1:
                    raise ValueError('Leeres PDF: ' + name)
            result[name] = member
        return result


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Ein leeres Ausgabeziel ist erforderlich')
    dist.mkdir(parents=True, exist_ok=True)
    package = module('build-compatibility-release.py')
    directory = ROOT / PLUGIN
    files = package.sources(ROOT, directory)
    manifest = json.loads(files['.claude-plugin/plugin.json'].read_text())
    if (manifest['name'], manifest['version']) != (PLUGIN, VERSION):
        raise ValueError('Pluginidentität oder Version weicht ab')
    marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    if next(p['version'] for p in marketplace['plugins'] if p['name'] == PLUGIN) != VERSION:
        raise ValueError('Marketplace-Version weicht ab')
    archive = dist / (PLUGIN + '.zip')
    package.write_zip(archive, files)
    hashes = package.verify_zip(archive, files)
    package.CHECKS.validate_plugin_zip(dist, PLUGIN, VERSION)
    package.CHECKS.validate_skill_sources(archive, directory)
    package.CHECKS.validate_focus_skill(archive, directory, ROOT / 'quality/evals' / (PLUGIN + '.json'))
    for kind in ('werkstatt', 'schnellstart'):
        source = directory / f'{PLUGIN}-{kind}.md'
        shutil.copyfile(source, dist / source.name)
    shutil.copyfile(ROOT / 'testakten/megaprompts' / (PLUGIN + '.md'), dist / (PLUGIN + '-master-prompt.md'))
    for slug in CASES:
        source = ROOT / 'testakten' / slug / 'gesamt-pdf' / (slug + '_gesamt.pdf')
        if not source.is_file() or pdf_content_errors(source.read_bytes()):
            raise ValueError('Geprüfte Gesamt-PDF fehlt: ' + slug)
        shutil.copyfile(source, dist / source.name)
    native = module('build-testakten-release-zips.py')
    separate = module('build-testakten-einzelpdf-zips.py')
    native_checks = module('validate-testakten-release-zips.py')
    separate_checks = module('validate-testakten-einzelpdf-zips.py')
    # Einzelakten-APIs erhalten die unveränderten zentralen Auswahl-, Satz- und
    # Prüfregeln; ein Vollarchiv aller übrigen Akten gehört nicht zu diesem Release.
    for slug in CASES:
        case_dir = ROOT / 'testakten' / slug
        original, _ = native.build_single(case_dir, dist)
        pdfs, _ = separate.build_single(case_dir, dist)
        native_checks.assert_same(original.name, native_checks.expected_entries(case_dir),
            native_checks.zip_entries(original, require_notice=True))
        separate_checks.assert_same(pdfs.name,
            [NOTICE_FILENAME, *separate_checks.expected_arcnames(case_dir)],
            separate_checks.zip_entries(pdfs, expected_suffix='.pdf'))
    members = {p.name: inspect_zip(p, case=p.name.startswith('testakte-'))
               for p in sorted(dist.glob('*.zip'))}
    report = {'schema_version': 1, 'tag': TAG, 'version': VERSION,
              'plugin_members_sha256': hashes, 'archives': members,
              'case_material_sha256': sha256((ROOT / 'scripts/notariat-auslandsinvestoren-material.json').read_bytes()).hexdigest()}
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / 'checksums-sha256.txt').write_text(''.join(
        f'{sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(dist.iterdir())))
    if len(list(dist.iterdir())) != 12:
        raise ValueError('Unerwarteter Release-Umfang')
    print(f'{TAG}: 12 Release-Dateien; alle Archivmitglieder geprüft.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    build(parser.parse_args().dist.resolve())
