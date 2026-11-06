#!/usr/bin/env python3
"""Baut Steuerrechts-Plugin und Tomasius-Verfahrensakte aus dem Repositorybestand."""

from __future__ import annotations

import argparse
import csv
from hashlib import sha256
import importlib.util
from io import BytesIO, StringIO
import json
from pathlib import Path, PurePosixPath
import shutil
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from testakte_disclaimer import NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'steuerrecht-anwalt-und-berater'
VERSION = '445.35.5'
TAG = 'steuerrecht-ustva-v' + VERSION
CASE = ROOT / 'quality/steuerrecht-freiburg/tomasius-solo'
BASE_NAME = 'Testakte_Tomasius_Lebenswelt_2025_v2.zip'
BASE_SHA256 = '98374e09994c8dfe3cde62f0c619d425db6cef552a1ce646de4d9a1d83929ffb'
CASE_NAME = 'Testakte_Tomasius_UStVA_Einspruch_2025_v3.zip'


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def case_members():
    source = CASE / BASE_NAME
    if sha256(source.read_bytes()).hexdigest() != BASE_SHA256:
        raise ValueError('Die geprüfte Ausgangsakte stimmt nicht mit dem Quellbestand überein')
    with ZipFile(source) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != 349:
            raise ValueError('Die Ausgangsakte ist beschädigt oder unvollständig')
        members = {name: archive.read(name) for name in archive.namelist()}
    additions = CASE / 'ust-verfahren'
    for path in sorted(additions.rglob('*')):
        if not path.is_file():
            continue
        if path.is_symlink():
            raise ValueError(f'Symlink in der Verfahrensergänzung {path}')
        name = path.relative_to(additions).as_posix()
        if path.name == 'README_Akte.txt':
            name = 'README.txt'
        member = PurePosixPath(name)
        if member.is_absolute() or '..' in member.parts or path.suffix == '.ndjson':
            raise ValueError(f'Unzulässige Archivdatei {name}')
        members[name] = path.read_bytes()
    if not members['README.txt'].startswith(NOTICE_BYTES):
        raise ValueError('Der verbindliche Aktenhinweis fehlt')
    if not any(name.endswith('13_Einspruchsentscheidung.pdf') for name in members):
        raise ValueError('Die Einspruchsentscheidung fehlt')
    if any(PurePosixPath(name).name.lower().startswith(('klageschrift', 'klageentwurf')) for name in members):
        raise ValueError('Die Vorbereitungsakte enthält bereits eine Klageschrift')
    members.pop('Dateibestand.csv')
    output = StringIO(newline='')
    writer = csv.writer(output, delimiter=';')
    writer.writerow(['Datei', 'Bytes', 'SHA256'])
    for name, data in sorted(members.items()):
        writer.writerow([name, len(data), sha256(data).hexdigest()])
    members['Dateibestand.csv'] = b'\xef\xbb\xbf' + output.getvalue().encode('utf-8')
    return members


def write_case(target, members):
    with ZipFile(target, 'x') as archive:
        for name, data in sorted(members.items()):
            entry = ZipInfo(name, (2026, 11, 6, 9, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    with ZipFile(target) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(members):
            raise ValueError('Die fertige Verfahrensakte ist beschädigt')
        for name, data in members.items():
            if archive.read(name) != data:
                raise ValueError(f'Archivinhalt weicht ab {name}')


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Ein leeres Ausgabeziel ist erforderlich')
    dist.mkdir(parents=True, exist_ok=True)
    package = module('build-compatibility-release')
    files = package.sources(ROOT, ROOT / PLUGIN)
    manifest = json.loads(files['.claude-plugin/plugin.json'].read_text())
    if (manifest['name'], manifest['version']) != (PLUGIN, VERSION):
        raise ValueError('Das Pluginmanifest hat eine abweichende Identität')
    plugin_zip = dist / f'{PLUGIN}.zip'
    package.write_zip(plugin_zip, files)
    package.verify_zip(plugin_zip, files)
    package.CHECKS.validate_plugin_zip(dist, PLUGIN, VERSION)
    members = case_members()
    write_case(dist / CASE_NAME, members)
    prompts = {
        f'{PLUGIN}-werkstatt.md': ROOT / PLUGIN / f'{PLUGIN}-werkstatt.md',
        f'{PLUGIN}-schnellstart.md': ROOT / PLUGIN / f'{PLUGIN}-schnellstart.md',
        f'{PLUGIN}-hauptproblem.md': ROOT / PLUGIN / f'{PLUGIN}-hauptproblem.md',
        'UStVA_Werkstatt.md': ROOT / PLUGIN / 'ustva/werkstatt.md',
        'UStVA_Mini.md': ROOT / PLUGIN / 'ustva/mini.md',
        'UStVA_Skill.md': ROOT / PLUGIN / 'skills/umsatzsteuer-voranmeldung-erstellen/SKILL.md',
        f'{PLUGIN}-master-prompt.md': ROOT / 'testakten/megaprompts' / f'{PLUGIN}.md',
    }
    for name, source in prompts.items():
        shutil.copyfile(source, dist / name)
    report = {
        'schema_version': 1, 'tag': TAG, 'version': VERSION,
        'base_archive_sha256': BASE_SHA256, 'case_files': len(members),
        'case_members_sha256': {name: sha256(data).hexdigest() for name, data in sorted(members.items())},
        'plugin_sources_sha256': {name: sha256(path.read_bytes()).hexdigest() for name, path in sorted(files.items())},
    }
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    paths = sorted(dist.iterdir())
    if len(paths) != 10:
        raise ValueError('Der Releaseumfang weicht von zehn Nutzdateien ab')
    (dist / 'checksums-sha256.txt').write_text(''.join(
        f'{sha256(path.read_bytes()).hexdigest()}  {path.name}\n' for path in paths))
    print(f'{VERSION}: 11 Release-Dateien, {len(members)} Akten-Dateien, geprüfte Paket- und Archivquellen.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', required=True, type=Path)
    build(parser.parse_args().dist.resolve())
