#!/usr/bin/env python3
"""Ordnet die geprüften Hildesheimer Originale in Projektordner. Autor: Klotzkette."""
from __future__ import annotations
import hashlib
import json
import re
import shutil
from bauwirtschaft_hildesheim_lebensakte_common import BASE_CASE, CASE, QUALITY


def directory(number, suffix):
    if number <= 6:
        return '01_Grundlagen_und_Erwerb'
    if number <= 8:
        return '02_Vorplanung'
    if number <= 17:
        return '03_Entwurfsplanung'
    if number <= 22:
        return '04_Genehmigung'
    if number <= 29 or number in (150, 151):
        return '05_Ausfuehrungsplanung'
    if number <= 31:
        return '06_Leistungsverzeichnisse/Bestands-LV'
    if number <= 48:
        return '07_Vergabe_und_Bauvertraege'
    if number in range(63, 69) or number == 153:
        return '09_Abnahme_und_Objektbetreuung'
    if number in (149, 170):
        return '01_Grundlagen_und_Erwerb'
    if number in range(130, 146) or number in range(154, 162):
        return '11_Vermietung'
    if number in range(171, 180):
        return '10_Rechnungen_und_Buchhaltung/Bauabzug'
    if number in range(70, 123):
        if suffix == '.xml':
            return '10_Rechnungen_und_Buchhaltung/XRechnungen'
        if suffix == '.xlsx':
            return '10_Rechnungen_und_Buchhaltung/Arbeitsmappen'
        return '10_Rechnungen_und_Buchhaltung/Belege'
    if number in range(162, 170):
        return '08_Bauausfuehrung/04_Lieferungen_und_Pruefungen/Bestandsnachweise'
    return '08_Bauausfuehrung/Bestandsunterlagen'


def main():
    source_files = sorted(p for p in BASE_CASE.iterdir() if p.is_file() and re.match(r'^\d{3}_', p.name))
    if len(source_files) != 198:
        raise RuntimeError('Der referenzierte Ausgangsbestand muss 198 Originaldateien enthalten.')
    manifest = []
    for source in source_files:
        relative = directory(int(source.name[:3]), source.suffix) + '/' + source.name
        target = CASE / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            raise RuntimeError('Kopierfehler: ' + source.name)
        manifest.append({'source': source.name, 'target': relative, 'sha256': digest})
    QUALITY.mkdir(parents=True, exist_ok=True)
    (QUALITY/'basisdateien.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(manifest)} Originale in {len({str((CASE/r["target"]).parent) for r in manifest})} Projektordnern; Ausgangsdateien unverändert.')


if __name__ == '__main__':
    main()
