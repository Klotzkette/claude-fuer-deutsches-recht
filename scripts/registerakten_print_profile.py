"""Druckkopien der 22 Registerakten-XLSX: Daten/Formeln bleiben unverändert.

Kein generischer Eingriff in andere Akten. Die expliziten Blattprofile werden
nur beim nativen PDF-Export angewendet, nie in den Originalformat-Downloads.
"""
from __future__ import annotations

import copy
import json
import textwrap
from pathlib import Path
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
REL = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
PROFILES_PATH = Path(__file__).with_name('registerakten_print_profiles.json')
PROFILES = json.loads(PROFILES_PATH.read_text(encoding='utf-8'))['profiles']
PRINT_FONT = 'Liberation Sans'  # Linux-CI: fonts-liberation2; macOS: LibreOffice-bundled.


def profile_for(source: Path) -> dict[str, list[int]] | None:
    return PROFILES.get(f'{source.parent.name}/{source.name}')


def insert_before(parent: ET.Element, child: ET.Element, later: set[str]) -> None:
    index = next((i for i, old in enumerate(parent) if old.tag.rsplit('}', 1)[-1] in later), len(parent))
    parent.insert(index, child)


def visible_text(cell: ET.Element, shared: list[str]) -> str:
    if cell.get('t') == 'inlineStr':
        return ''.join(node.text or '' for node in cell.iter(NS+'t'))
    value = cell.findtext(NS+'v', '')
    if cell.get('t') == 's':
        return shared[int(value)]
    # Zahlen-/Datumsformate nicht umschreiben: nur eine konservative Platzannahme.
    return value if len(value) >= 12 else value.ljust(12)


def required_height(text: str, width: float) -> int:
    # Native Wortumbrüche berücksichtigen, nicht nur Zeichenanzahl teilen.
    # Innenabstände und eine zusätzliche Sicherheitszeile halten Umbrüche frei.
    capacity = max(5, int(width) - 6)
    lines = sum(max(1, len(textwrap.wrap(line, width=capacity, break_long_words=True,
                                        break_on_hyphens=True))) for line in text.split('\n'))
    return 12 * lines + 16


def print_overrides(source: Path, archive: zipfile.ZipFile) -> dict[str, bytes]:
    profiles = profile_for(source)
    if profiles is None:
        return {}
    styles = ET.fromstring(archive.read('xl/styles.xml'))
    fonts = styles.find(NS+'fonts')
    assert fonts is not None
    for font in fonts:
        name = font.find(NS+'name')
        if name is None: name = ET.SubElement(font, NS+'name')
        name.set('val', PRINT_FONT)
        size = font.find(NS+'sz')
        if size is None: size = ET.SubElement(font, NS+'sz')
        size.set('val', '10')
    xfs = styles.find(NS+'cellXfs')
    assert xfs is not None
    original_xfs = list(xfs)
    variants: dict[tuple[int, str], int] = {}

    def cell_style(original: int, horizontal: str) -> int:
        key = (original, horizontal)
        if key not in variants:
            xf = copy.deepcopy(original_xfs[original])
            alignment = xf.find(NS+'alignment')
            if alignment is None: alignment = ET.SubElement(xf, NS+'alignment')
            alignment.set('horizontal', horizontal)
            alignment.set('vertical', 'center')
            alignment.set('wrapText', '1')
            alignment.set('shrinkToFit', '0')
            # Rechts wie links drei Leerzeichen Abstand, ohne Zellwerte zu ändern.
            alignment.set('indent', '0' if horizontal == 'center' else '1')
            xf.set('applyAlignment', '1')
            variants[key] = len(xfs)
            xfs.append(xf)
        return variants[key]

    shared = []
    if 'xl/sharedStrings.xml' in archive.namelist():
        shared = [''.join(n.text or '' for n in item.iter(NS+'t'))
                  for item in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
    workbook = ET.fromstring(archive.read('xl/workbook.xml'))
    relationships = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
    targets = {r.get('Id'): posixpath.normpath('xl/'+r.get('Target', '')).lstrip('/')
               if not r.get('Target', '').startswith('/') else r.get('Target', '').lstrip('/')
               for r in relationships}
    sheets = list(workbook.find(NS+'sheets') or [])
    if {s.get('name') for s in sheets} != set(profiles):
        raise ValueError(f'{source.name}: Druckprofil passt nicht mehr zu den Blättern')
    defined = workbook.find(NS+'definedNames')
    if defined is None:
        defined = ET.Element(NS+'definedNames')
        insert_before(workbook, defined, {'calcPr', 'oleSize', 'customWorkbookViews', 'pivotCaches', 'extLst'})
    result = {}
    for index, descriptor in enumerate(sheets):
        name = descriptor.get('name', '')
        widths = profiles[name]
        sheet_path = targets[descriptor.get(REL+'id')]
        sheet = ET.fromstring(archive.read(sheet_path))
        rows = list(sheet.find(NS+'sheetData') or [])
        cells = [cell for row in rows for cell in row if cell.tag == NS+'c']
        def column(cell):
            value = 0
            for letter in re.match(r'[A-Z]+', cell.get('r', '')).group():
                value = value * 26 + ord(letter) - 64
            return value
        if not cells or max(column(c) for c in cells) != len(widths):
            raise ValueError(f'{source.name}/{name}: Druckprofil passt nicht zur Spaltenzahl')
        columns = sheet.find(NS+'cols')
        if columns is None:
            columns = ET.Element(NS+'cols')
            insert_before(sheet, columns, {'sheetData'})
        columns.clear()
        for n, width in enumerate(widths, 1):
            ET.SubElement(columns, NS+'col', min=str(n), max=str(n), width=str(width), customWidth='1')
        for row in rows:
            heading = row.get('r') == '1'
            height = 40 if heading else 34
            for cell in row:
                if cell.tag != NS+'c': continue
                text = visible_text(cell, shared)
                height = max(height, required_height(text, widths[column(cell)-1]))
                horizontal = 'center' if heading else ('left' if cell.get('t') in ('inlineStr','s','str') else 'right')
                cell.set('s', str(cell_style(int(cell.get('s', '0')), horizontal)))
            row.set('ht', str(height))
            row.set('customHeight', '1')
        setup = sheet.find(NS+'pageSetup')
        if setup is None:
            setup = ET.Element(NS+'pageSetup')
            insert_before(sheet, setup, {'headerFooter','rowBreaks','colBreaks','drawing','legacyDrawing','extLst'})
        setup.attrib.pop('scale', None)
        setup.set('paperSize','9')
        setup.set('orientation', 'landscape' if len(widths) >= 5 else 'portrait')
        setup.set('fitToWidth','1');setup.set('fitToHeight','0')
        margins = sheet.find(NS+'pageMargins')
        if margins is None:
            margins = ET.Element(NS+'pageMargins')
            insert_before(sheet, margins, {'pageSetup','headerFooter','rowBreaks','colBreaks','drawing','extLst'})
        for key in ('left','right','top','bottom'): margins.set(key,'0.4')
        for key in ('header','footer'): margins.set(key,'0.15')
        for old in list(defined):
            if old.get('localSheetId') == str(index) and old.get('name') in ('_xlnm.Print_Area','_xlnm.Print_Titles'):
                defined.remove(old)
        lastcol = re.match(r'[A-Z]+', max(cells, key=column).get('r')).group()
        lastrow = max(int(r.get('r','1')) for r in rows)
        quoted = "'"+name.replace("'","''")+"'"
        ET.SubElement(defined, NS+'definedName', name='_xlnm.Print_Area', localSheetId=str(index)).text = f'{quoted}!$A$1:${lastcol}${lastrow}'
        ET.SubElement(defined, NS+'definedName', name='_xlnm.Print_Titles', localSheetId=str(index)).text = f'{quoted}!$1:$1'
        result[sheet_path] = ET.tostring(sheet, encoding='utf-8', xml_declaration=True)
    xfs.set('count',str(len(xfs)))
    result['xl/styles.xml'] = ET.tostring(styles, encoding='utf-8', xml_declaration=True)
    result['xl/workbook.xml'] = ET.tostring(workbook, encoding='utf-8', xml_declaration=True)
    return result
