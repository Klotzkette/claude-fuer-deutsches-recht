#!/usr/bin/env python3
"""Erweitert PE-07 um GAEB-Austauschdateien und die Verhandlungsrunde."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'bauunternehmer-einkauf'
CASE = f'{PLUGIN}-brandschutztueren-krimpfort'
CASE_ID = 'BE-01'
DATA = ROOT / 'scripts/data/bauunternehmer-einkauf-korrespondenz.json'
MODERATION = ROOT / 'scripts/data/bauunternehmer-einkauf-moderation.json'


def load_script(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def case_data():
    base = load_script('build-projekteinkauf-baubranche-akten').cases()[-1]
    extra = json.loads(DATA.read_text(encoding='utf-8'))
    exchange = [{'filename': name} for name in (
        '31_Tuerpaket_LV_R1.x83', '33_A_Emswiek_ET-26-241.x84', '35_B_Weserfalz_WF-702.x84',
        '37_C_Jadeholm_JH-WB-26.x84', '39_D_Friesenlint_FL-500.x84',
    )]
    return {
        **base,
        'id': CASE_ID,
        'slug': CASE,
        'title': 'Krimpfort kauft 500 Brandschutztüren',
        'summary': 'Die Krimpfort SE & Co. KG kauft 500 Brandschutztüren für einen fiktiven Bundesbau in Bremen. Vier native GAEB-Angebote, ein gemeinsames X83 und eine mehrstufige Verhandlungsakte verbinden Eignungsprüfung, Preisspiegel, Angebotsbindung und Freigabe.',
        'as_of': '2026-12-04',
        'documents': base['documents'] + exchange + extra['documents'],
    }, base, extra


def build(output, gaeb, fonts):
    writer = load_script('build-projekteinkauf-baubranche-akten')
    writer.set_fonts(fonts)
    case, base, extra = case_data()
    moderation = json.loads(MODERATION.read_text(encoding='utf-8'))
    target = output / 'testakten' / CASE
    target.mkdir(parents=True, exist_ok=True)
    names = {doc['filename']: doc for doc in case['documents']}
    if len(names) != len(case['documents']):
        raise ValueError('Doppelte Dateinamen in der Krimpfort-Akte.')
    for doc in base['documents']:
        name = doc['filename']
        shutil.copyfile(ROOT / 'testakten' / base['slug'] / name, target / name)
    for name in names:
        if Path(name).suffix in {'.x83', '.x84'}:
            shutil.copyfile(gaeb / name, target / name)
    for doc in extra['documents']:
        if Path(doc['filename']).suffix == '.pdf':
            writer.write_pdf(target / doc['filename'], doc, case)
    for doc in extra['documents']:
        path = target / doc['filename']
        if path.suffix == '.eml':
            # Die Originalmails behalten ihre Message-ID. Die neue Runde antwortet
            # in derselben Korrespondenz statt in einer künstlich neuen Kette.
            writer.write_eml(path, doc, {**case, 'id': base['id']}, target, names)
        elif path.suffix != '.pdf':
            raise ValueError('Unerwartetes Format im Schriftverkehr: ' + path.name)
    templates = output / PLUGIN / 'templates'
    templates.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / 'projekteinkauf-baubranche/templates/Brandschutztueren_Preisspiegel.xlsx',
                    templates / 'Brandschutztueren_Preisspiegel.xlsx')
    stationery = {'issuer': case['company'], 'date': case['as_of']}
    base_sections = base['template']['sections']
    sections = [*base_sections[:3], {**base_sections[3], 'page_break_before': True},
                *base_sections[4:-1], *moderation['freigabe_template_sections'],
                {**base_sections[-1], 'page_break_before': True}]
    writer.write_docx(templates / f'{CASE}.docx', {
        **base['template'], **stationery, 'sections': sections,
    }, case)
    writer.write_docx(templates / 'Verhandlungsleitfaden.docx', {
        **moderation['verhandlungs_template'], **stationery,
    }, case)
    target = output / 'quality' / PLUGIN
    target.mkdir(parents=True, exist_ok=True)
    writer.write_pdf(target / 'BE-01_Nachbesprechung.pdf', {
        **moderation['debrief'], 'issuer': 'Schulungsleitung · Bauunternehmer Einkauf', 'date': case['as_of'],
    }, case)
    print(f"{case['id']}: {len(names)} Originale und drei Vorlagen")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--gaeb', type=Path, required=True)
    parser.add_argument('--fonts', type=Path, default=Path('/System/Library/Fonts/Supplemental'))
    args = parser.parse_args()
    build(args.output, args.gaeb, args.fonts)
