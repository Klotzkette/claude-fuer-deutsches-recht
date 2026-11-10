#!/usr/bin/env python3
"""Baut drei Ausgaben für ME-36 und prüft Vorschau, Sperrexport und Kontrollmuster."""

import argparse
from hashlib import sha256
import json
from pathlib import Path

from pypdf import PdfReader

from testakte_disclaimer import pdf_content_errors

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'compliance-hameln-auskunft-mit-schwaerzungen'
TITLE = 'Die Auskunft mit den roten Markierungen'
TAG = 'compliance-hameln-auskunft-v1.0.0'
CASE = ROOT / 'testakten' / SLUG
DEBRIEF = ROOT / 'quality/hameln-compliance/nachbesprechung'


def verify_redaction():
    preview = PdfReader(CASE / '09_KI_Pruefansicht.pdf')
    overlay = PdfReader(CASE / '10_Exportkandidat_Sperren.pdf')
    scanned = PdfReader(CASE / '11_Gescannte_Fremdbeilage.pdf')
    clean = PdfReader(DEBRIEF / f'{SLUG}-kontrollmuster.pdf')
    wanted = ('Mara Lindhorst', 'Kundin nicht erreichbar', '22.10.2026', 'Okerquell Prüftechnik GmbH')
    third_party = ('Jonas Evers', '05151 000 0187')
    for source in (preview, overlay):
        extracted = source.pages[0].extract_text()
        if any(token not in extracted for token in (*wanted, *third_party)):
            raise ValueError('Das Prüfbeispiel enthält nicht alle erwarteten Textwerte.')
    scan_page = scanned.pages[0]
    if 'Jonas Evers' in scan_page.extract_text() or not scan_page.images:
        raise ValueError('Das Scanbeispiel muss den Beifang ausschließlich als Bild enthalten.')
    page = clean.pages[0]
    extracted = page.extract_text()
    content = page.get_contents().get_data()
    if any(token not in extracted for token in wanted):
        raise ValueError('Im Kontrollmuster fehlt personenbezogener Auskunftsinhalt.')
    if any(token in extracted or token.encode() in content for token in third_party):
        raise ValueError('Fremddaten sind im Kontrollmuster auslesbar.')
    if clean.attachments or page.images or page.get('/Annots') or clean.root_object.get('/AcroForm'):
        raise ValueError('Unerwartete Objekte im neu erzeugten Kontrollmuster.')
    if pdf_content_errors(DEBRIEF.joinpath(f'{SLUG}-kontrollmuster.pdf').read_bytes()):
        raise ValueError('Unzulässiger Hinweistext im Kontrollmuster.')


def build(dist, rebuild):
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        'hameln_archive_builder', ROOT / 'scripts/build-compliance-hameln-release.py'
    )
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Das Ausgabeziel muss leer sein.')
    dist.mkdir(parents=True, exist_ok=True)
    verify_redaction()
    result = builder.build_case(({'nr': 'ME-36', 'slug': SLUG, 'title': TITLE}, str(dist), rebuild))
    if result['documents'] != 11:
        raise ValueError('ME-36 benötigt genau elf Arbeitsdokumente.')
    assets = {path.name: sha256(path.read_bytes()).hexdigest() for path in sorted(dist.iterdir())}
    report = {'tag': TAG, 'case': result, 'assets': assets}
    inventory = dist / 'release-bestand.json'
    inventory.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assets[inventory.name] = sha256(inventory.read_bytes()).hexdigest()
    (dist / 'checksums-sha256.txt').write_text(
        ''.join(f'{digest}  {name}\n' for name, digest in sorted(assets.items())), encoding='utf-8'
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    parser.add_argument('--rebuild-pdf', action='store_true')
    args = parser.parse_args()
    build(args.dist.resolve(), args.rebuild_pdf)
