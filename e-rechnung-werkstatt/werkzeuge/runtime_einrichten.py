#!/usr/bin/env python3
"""Lädt die versionierten Prüfwerkzeuge ohne Rechnungsdaten herunter.

Einrichtung ist ein ausdrücklich aufgerufener Netzwerkschritt. Die spätere
Rechnungserzeugung und -validierung verwendet die lokalen Dateien.
"""
import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import shutil
import stat
import sys
import tempfile
import urllib.request
from zipfile import ZipFile

LOCK = Path(__file__).with_name('runtime-lock.json')


def download(url, expected):
    if not url.startswith('https://'):
        raise ValueError('Nur HTTPS-Download zugelassen')
    request = urllib.request.Request(url, headers={'User-Agent': 'Klotzkette-E-Rechnungswerkstatt/445.35.6'})
    with urllib.request.urlopen(request, timeout=90) as response:
        result = response.read(70 * 1024**2 + 1)
    if len(result) > 70 * 1024**2 or sha256(result).hexdigest() != expected:
        raise ValueError('Downloadgröße oder SHA-256 weicht vom gepinnten Release ab')
    return result


def extract_configuration(raw, target):
    with ZipFile(BytesIO(raw)) as archive:
        if len(archive.infolist()) > 2000 or sum(i.file_size for i in archive.infolist()) > 64 * 1024**2:
            raise ValueError('Konfigurationsarchiv überschreitet die Größenbegrenzung')
        for entry in archive.infolist():
            member = PurePosixPath(entry.filename)
            if member.is_absolute() or '..' in member.parts or '\\' in entry.filename or stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError('Unsicherer Pfad im Konfigurationsarchiv')
            if entry.is_dir():
                continue
            path = target / member
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(archive.read(entry))


def install(output):
    if output.exists():
        raise ValueError('Ein neues, noch nicht vorhandenes Installationsverzeichnis ist erforderlich')
    lock = json.loads(LOCK.read_text())
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.' + output.name + '-', dir=output.parent))
    try:
        m = lock['mustang']; k = lock['kosit']
        (stage / 'Mustang-CLI-2.26.0.jar').write_bytes(download(m['url'], m['sha256']))
        bundle = download(k['bundle_url'], k['bundle_sha256'])
        # Retain the original official package, including its documentation
        # and licence notices, outside the installable plugin archive.
        (stage / 'xrechnung-3.0.2-bundle-2026-08-31.zip').write_bytes(bundle)
        home = stage / 'kosit'; home.mkdir()
        with ZipFile(BytesIO(bundle)) as archive:
            jar = archive.read('validator-1.6.3-standalone.jar')
            config = archive.read('xrechnung-3.0.2-validator-configuration-2026-08-31.zip')
        if sha256(jar).hexdigest() != k['jar_sha256'] or sha256(config).hexdigest() != k['configuration_sha256']:
            raise ValueError('Innere KoSIT-Komponente weicht vom geprüften Bundle ab')
        (home / 'validator-1.6.3-standalone.jar').write_bytes(jar)
        extract_configuration(config, home / 'configuration')
        actual = {p.relative_to(home).as_posix(): sha256(p.read_bytes()).hexdigest() for p in sorted(home.rglob('*')) if p.is_file()}
        if actual != k['files_sha256']:
            raise ValueError('Extrahierter KoSIT-Bestand ist nicht vollständig identisch')
        (home / 'installation.json').write_text(json.dumps({'validator': '1.6.3', 'configuration': '2026-08-31',
                                                         'files_sha256': actual}, indent=2) + '\n')
        (stage / 'installation.json').write_text(json.dumps({'mustang': m['version'], 'kosit': k['validator'],
                                                            'configuration': k['configuration'],
                                                            'runtime_lock_sha256': sha256(LOCK.read_bytes()).hexdigest()}, indent=2) + '\n')
        stage.rename(output)
    finally:
        if stage.exists(): shutil.rmtree(stage)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = install(args.out.absolute())
        print(json.dumps({'directory': str(result), 'mustang': '2.26.0', 'kosit': '1.6.3', 'configuration': '2026-08-31'}, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        print('Fehler: ' + str(exc), file=sys.stderr); sys.exit(2)
