"""Zusätzlicher Schriftverkehr und ausdrücklich bestellte Klageentwürfe in zwölf Akten."""
from importlib import import_module
MODULES = {'verkehr':'kommunale_schriftverkehr_verkehr', 'amt':'kommunale_schriftverkehr_amt', 'stamm':'kommunale_schriftverkehr_stamm'}
FOLDER = 'schriftverkehr-und-klage'
def cases(groups=None):
    result = sorted([case for name in groups or MODULES for case in import_module(MODULES[name]).CASES], key=lambda c:c['slug'])
    if len({c['slug'] for c in result}) != len(result):
        raise ValueError('Doppelte Akte')
    return result
def filename(item):
    from pathlib import Path
    return str(Path(item['file']).with_suffix('.pdf')) if item['kind']=='letter' else item['file']
