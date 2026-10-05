"""Fallbezogene Korrespondenz und drei zusätzliche kommunale Haftpflichtakten."""
from importlib import import_module

FOLDER = 'kommunikation-und-deckung'
MODULES = {
    'kita': 'kommunale_vertiefung_kita',
    'feuerwehr': 'kommunale_vertiefung_feuerwehr',
    'kreisstrasse': 'kommunale_vertiefung_kreisstrasse',
    'verletzung': 'kommunale_vertiefung_verletzung',
}

def cases(groups=None):
    result = sorted([c for group in groups or MODULES for c in import_module(MODULES[group]).CASES], key=lambda c: c['slug'])
    if len(result) != len({c['slug'] for c in result}):
        raise ValueError('Doppelte kommunale Akte')
    return result

def native_names(case):
    names = []
    for item in case['documents']:
        names.append(item['file'])
        if item['kind'] == 'letter':
            from pathlib import Path
            names.append(str(Path(item['file']).with_suffix('.pdf')))
    return names
