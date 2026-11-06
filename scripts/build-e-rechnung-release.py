#!/usr/bin/env python3
"""Baut das E-Rechnungs-Plugin und seine separat verwendbaren Fachprompts."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import shutil
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from testakte_disclaimer import NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'e-rechnung-werkstatt'
VERSION = '445.35.6'
TAG = 'e-rechnung-v' + VERSION


def package_module():
    spec = importlib.util.spec_from_file_location('e_rechnung_package', ROOT / 'scripts/build-compatibility-release.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def demo_members():
    directory = ROOT / 'quality/e-rechnung/ausgabe'
    report = json.loads((directory / 'Pruefbericht.json').read_text())
    bindings = {
        'generator_sha256': ROOT / PLUGIN / 'werkzeuge/erechnung.py',
        'layout_sha256': ROOT / PLUGIN / 'werkzeuge/rechnung_layout.py',
        'runtime_lock_sha256': ROOT / PLUGIN / 'werkzeuge/runtime-lock.json',
        'input_sha256': ROOT / PLUGIN / 'beispiele/rechnungsdaten.json',
    }
    for name, source in bindings.items():
        if sha256(source.read_bytes()).hexdigest() != report[name]:
            raise ValueError(f'Die geprüfte Beispielausgabe gehört zu einem anderen Quellstand: {name}')
    members = {}
    for source in sorted(directory.rglob('*')):
        if not source.is_file():
            continue
        if source.is_symlink():
            raise ValueError('Symlink im geprüften Beispielbestand')
        members[source.relative_to(directory).as_posix()] = source.read_bytes()
    if set(members) != set(report['files_sha256']) | {'Pruefbericht.json'}:
        raise ValueError('Die geprüfte Beispielausgabe ist unvollständig oder verändert')
    for name, expected in report['files_sha256'].items():
        if sha256(members[name]).hexdigest() != expected:
            raise ValueError(f'Die generierte Beispieldatei wurde verändert: {name}')
    if (report['state'] != 'generated_and_validated_not_sent'
            or not report['results']['ZUGFeRD.pdf']['pdfa_valid']
            or not report['results']['XRechnung.xml']['schema_and_schematron_valid']):
        raise ValueError('Der erfolgreiche ursprüngliche Prüfnachweis fehlt')
    members['rechnungsquelle.txt'] = (ROOT / PLUGIN / 'beispiele/rechnungsquelle.txt').read_bytes()
    members['README.txt'] = NOTICE_BYTES + (
        '\nFiktive Beispielrechnung in zwei Formaten. Keine Zahlung und keinen Versand veranlassen.\n'
        'XRechnung.xml und ZUGFeRD.pdf beschreiben dieselbe Rechnung.\n'
        'Pruefbericht.json und die Originalberichte dokumentieren die tatsächlichen lokalen Prüfungen.\n'
        'Rechnungsdaten.json und rechnungsquelle.txt sind der bestätigte Eingabestand.\n'
        'FO-, Konfigurations- und Logdateien bleiben unveränderte technische Nachweise des Prüflaufs.\n'
    ).encode('utf-8')
    return members


def build(dist):
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Ein leeres Ausgabeziel ist erforderlich')
    dist.mkdir(parents=True, exist_ok=True)
    package = package_module()
    directory = ROOT / PLUGIN
    files = package.sources(ROOT, directory)
    manifest = json.loads(files['.claude-plugin/plugin.json'].read_text())
    if (manifest['name'], manifest['version']) != (PLUGIN, VERSION):
        raise ValueError('Die Pluginidentität oder Version weicht ab')
    archive = dist / (PLUGIN + '.zip')
    package.write_zip(archive, files)
    hashes = package.verify_zip(archive, files)
    package.CHECKS.validate_plugin_zip(dist, PLUGIN, VERSION)
    package.CHECKS.validate_skill_sources(archive, directory)
    package.CHECKS.validate_focus_skill(archive, directory, ROOT / 'quality/evals' / (PLUGIN + '.json'))
    for kind in ('werkstatt', 'schnellstart', 'hauptproblem'):
        source = directory / f'{PLUGIN}-{kind}.md'
        shutil.copyfile(source, dist / source.name)
    shutil.copyfile(ROOT / 'testakten/megaprompts' / (PLUGIN + '.md'), dist / (PLUGIN + '-master-prompt.md'))
    demo = demo_members()
    demo_zip = dist / 'E-Rechnung_Beispielpaket.zip'
    with ZipFile(demo_zip, 'x') as archive:
        for name, data in sorted(demo.items()):
            info = ZipInfo(name, (2026, 11, 6, 9, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with ZipFile(demo_zip) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(demo):
            raise ValueError('Das Beispielpaket ist beschädigt')
        for name, data in demo.items():
            if archive.read(name) != data:
                raise ValueError('Der archivierte Beispielinhalt weicht ab: ' + name)
    report = {'schema_version': 1, 'tag': TAG, 'version': VERSION, 'plugin_members_sha256': hashes,
              'demo_members_sha256': {name: sha256(data).hexdigest() for name, data in sorted(demo.items())}}
    (dist / 'release-bestand.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (dist / 'checksums-sha256.txt').write_text(''.join(
        f'{sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(dist.iterdir())))
    print(f'{TAG}: {len(list(dist.iterdir()))} Release-Dateien, {len(hashes)} geprüfte Paketdateien.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    build(parser.parse_args().dist.resolve())
