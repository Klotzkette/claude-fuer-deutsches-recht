#!/usr/bin/env python3
"""Prüft ausschließlich native Druckkopien der 22 neuen Registerakten-XLSX.

--native rendert alle Profile und eine um 25% verbreiterte Stresskopie mit
LibreOffice. Es prüft die tatsächlich eingebettete Schriftgröße (>= 8 pt).
"""
from __future__ import annotations
import argparse
import hashlib
import importlib
import json
import re
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

import pdfplumber
from registerakten_print_profile import NS, PROFILES, profile_for, required_height
from testakte_office_pdf import office_binary, prepare_source, render_office_batch

ROOT = Path(__file__).resolve().parents[1]


def tree(node):
    if node is None:return None
    return (node.tag, tuple(sorted(node.attrib.items())), node.text, tuple(tree(child) for child in node))


def payloads(archive):
    """Alle Zellwerte, Typen, Adressen und Formeln; nur Stilindex ist Drucklayout."""
    result = {}
    for name in archive.namelist():
        if name.startswith('xl/worksheets/') and name.endswith('.xml'):
            sheet = ET.fromstring(archive.read(name))
            data=sheet.find(NS+'sheetData')
            for row in data:
                row.attrib.pop('ht',None)
                row.attrib.pop('customHeight',None)
                for cell in row:
                    cell.attrib.pop('s',None)
            result[name]=tree(data)
    return result


def widen_copy(source, target):
    """Strenger Puffer: +25% Spaltenmaß entspricht bis zu 20% Verkleinerung."""
    with zipfile.ZipFile(source) as old, zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as new:
        for info in old.infolist():
            data = old.read(info)
            if info.filename.startswith('xl/worksheets/') and info.filename.endswith('.xml'):
                sheet = ET.fromstring(data)
                for col in sheet.findall(NS+'cols/'+NS+'col'):
                    col.set('width',str(float(col.get('width'))*1.25))
                data = ET.tostring(sheet,encoding='utf-8',xml_declaration=True)
            new.writestr(info,data)


class PrintProfileTests(unittest.TestCase):
    def test_exact_scope_matches_requested_twelve_case_modules(self):
        expected=set()
        for name in ('transparenz','handelsregister','grundbuch','marken'):
            for case in importlib.import_module('registerakten_'+name).CASES:
                expected.update(f"{case['slug']}/{doc['file']}" for doc in case['documents'] if doc['file'].endswith('.xlsx'))
        self.assertEqual(len(expected),22)
        self.assertEqual(set(PROFILES),expected)
        self.assertEqual(len({Path(x).parent.name for x in expected}),12)

    def test_originals_cells_formulas_and_other_package_members_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            for relative in PROFILES:
                with self.subTest(source=relative):
                    source=ROOT/'testakten'/relative
                    before=hashlib.sha256(source.read_bytes()).hexdigest()
                    copy=Path(tmp)/'druck.xlsx'
                    prepare_source(source,copy)
                    self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),before)
                    with zipfile.ZipFile(source) as original,zipfile.ZipFile(copy) as printed:
                        self.assertEqual(original.namelist(),printed.namelist())
                        self.assertEqual(payloads(original),payloads(printed))
                        for name in original.namelist():
                            if name in ('xl/styles.xml','xl/workbook.xml') or name.startswith('xl/worksheets/'):
                                continue
                            self.assertEqual(original.read(name),printed.read(name),name)
                        before_styles=ET.fromstring(original.read('xl/styles.xml'))
                        after_styles=ET.fromstring(printed.read('xl/styles.xml'))
                        self.assertEqual(tree(before_styles.find(NS+'numFmts')),tree(after_styles.find(NS+'numFmts')))
                        for font in after_styles.find(NS+'fonts'):
                            self.assertEqual(font.find(NS+'name').get('val'),'Liberation Sans')
                            self.assertEqual(font.find(NS+'sz').get('val'),'10')

    def test_explicit_print_areas_titles_orientation_and_spaced_styles(self):
        with tempfile.TemporaryDirectory() as tmp:
            for relative,profiles in PROFILES.items():
                copy=Path(tmp)/'druck.xlsx';prepare_source(ROOT/'testakten'/relative,copy)
                with zipfile.ZipFile(copy) as archive:
                    book=ET.fromstring(archive.read('xl/workbook.xml'))
                    names=list(book.find(NS+'definedNames'))
                    self.assertEqual(sum(x.get('name')=='_xlnm.Print_Area' for x in names),len(profiles))
                    self.assertEqual(sum(x.get('name')=='_xlnm.Print_Titles' for x in names),len(profiles))
                    for file in payloads(archive):
                        sheet=ET.fromstring(archive.read(file));setup=sheet.find(NS+'pageSetup')
                        columns=sheet.find(NS+'cols')
                        self.assertEqual(setup.get('orientation'),'landscape' if len(columns)>=5 else 'portrait')
                        self.assertEqual(setup.get('fitToHeight'),'0')
                        self.assertEqual(setup.get('fitToWidth'),'1')
                        self.assertTrue(all(float(row.get('ht'))>=34 for row in sheet.find(NS+'sheetData')))
                    styles=ET.fromstring(archive.read('xl/styles.xml')).find(NS+'cellXfs')
                    for file in payloads(archive):
                        for cell in ET.fromstring(archive.read(file)).iter(NS+'c'):
                            align=styles[int(cell.get('s'))].find(NS+'alignment')
                            self.assertEqual(align.get('wrapText'),'1')
                            self.assertEqual(align.get('indent'),'0' if align.get('horizontal')=='center' else '1')

    def test_same_filename_elsewhere_does_not_receive_profile(self):
        relative=next(iter(PROFILES));source=ROOT/'testakten'/relative
        with tempfile.TemporaryDirectory() as tmp:
            other=Path(tmp)/source.name;other.write_bytes(source.read_bytes())
            self.assertIsNone(profile_for(other))
            target=Path(tmp)/'copy.xlsx';prepare_source(other,target)
            with zipfile.ZipFile(other) as before,zipfile.ZipFile(target) as after:
                self.assertEqual(before.read('xl/styles.xml'),after.read('xl/styles.xml'))

    def test_existing_nonprint_defined_names_survive(self):
        relative=next(iter(PROFILES));source=ROOT/'testakten'/relative
        with tempfile.TemporaryDirectory() as tmp:
            copy=Path(tmp)/Path(relative);copy.parent.mkdir(parents=True)
            with zipfile.ZipFile(source) as old,zipfile.ZipFile(copy,'w',zipfile.ZIP_DEFLATED) as new:
                for info in old.infolist():
                    data=old.read(info)
                    if info.filename=='xl/workbook.xml':
                        book=ET.fromstring(data)
                        defined=book.find(NS+'definedNames')
                        if defined is None:
                            defined=ET.Element(NS+'definedNames')
                            calc=book.find(NS+'calcPr')
                            book.insert(list(book).index(calc) if calc is not None else len(book),defined)
                        ET.SubElement(defined,NS+'definedName',name='Unabhaengige_Quelle',hidden='1').text="'Kapital'!$A$2:$C$4"
                        data=ET.tostring(book,encoding='utf-8',xml_declaration=True)
                    new.writestr(info,data)
            printed=Path(tmp)/'druck.xlsx';prepare_source(copy,printed)
            with zipfile.ZipFile(copy) as old,zipfile.ZipFile(printed) as new:
                original=[tree(n) for n in ET.fromstring(old.read('xl/workbook.xml')).find(NS+'definedNames') if n.get('name')=='Unabhaengige_Quelle']
                actual=[tree(n) for n in ET.fromstring(new.read('xl/workbook.xml')).find(NS+'definedNames') if n.get('name')=='Unabhaengige_Quelle']
                self.assertEqual(original,actual)

    def test_print_areas_cover_actual_cell_bounds(self):
        with tempfile.TemporaryDirectory() as tmp:
            for relative in PROFILES:
                printed=Path(tmp)/'druck.xlsx';prepare_source(ROOT/'testakten'/relative,printed)
                with zipfile.ZipFile(printed) as archive:
                    book=ET.fromstring(archive.read('xl/workbook.xml'))
                    names=list(book.find(NS+'definedNames'))
                    for i,sheet in enumerate(book.find(NS+'sheets')):
                        content=ET.fromstring(archive.read(f'xl/worksheets/sheet{i+1}.xml'))
                        addresses=[c.get('r') for c in content.iter(NS+'c')]
                        lastcol=max(re.match('[A-Z]+',x).group() for x in addresses)
                        lastrow=max(int(re.search('[0-9]+',x).group()) for x in addresses)
                        quoted="'"+sheet.get('name').replace("'","''")+"'"
                        actual=next(n.text for n in names if n.get('name')=='_xlnm.Print_Area' and n.get('localSheetId')==str(i))
                        self.assertEqual(actual,f'{quoted}!$A$1:${lastcol}${lastrow}')

    def test_word_wrapping_and_long_german_labels_receive_safe_height(self):
        # Jedes 7-Zeichen-Wort braucht bei Kapazität12 eine eigene Zeile.
        # Eine bloße ceil(Zeichen/Kapazität)-Rechnung ergäbe hier nur zwei.
        self.assertGreaterEqual(required_height('BelegXX DatumXX StatusX',18),52)
        self.assertGreaterEqual(required_height('Gesellschafterbeschlussvorbereitung',16),64)
        self.assertGreaterEqual(required_height('Erste Zeile\nZweite Zeile\nDritte Zeile',22),52)


def native_check(output:Path, only:list[str]|None=None):
    if not office_binary():raise RuntimeError('Native Druckprüfung benötigt LibreOffice')
    output.mkdir(parents=True,exist_ok=True)
    selected=[r for r in PROFILES if not only or any(x in r for x in only)]
    sources=[ROOT/'testakten'/r for r in selected]
    hashes={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    normal=render_office_batch(sources)
    if set(normal)!=set(sources):raise AssertionError('Fehlende native PDF-Ausgabe')
    report=[]
    with tempfile.TemporaryDirectory(prefix='register-druckstress-') as tmp:
        stress_sources=[]
        for i,source in enumerate(sources):
            prepared=Path(tmp)/f'prepared-{i}.xlsx';prepare_source(source,prepared)
            stress=Path(tmp)/f'stress-{i}.xlsx';widen_copy(prepared,stress);stress_sources.append(stress)
        stress_results=render_office_batch(stress_sources)
        if set(stress_results)!=set(stress_sources):raise AssertionError('Fehlende Stress-PDF-Ausgabe')
        for source,stress in zip(sources,stress_sources):
            entry={'source':str(source),'source_sha256':hashes[source],'variants':[]}
            for variant,data in [('normal',normal[source]),('columns_125_percent',stress_results[stress])]:
                pdf_path=output/f'{source.parent.name}--{source.stem}--{variant}.pdf';pdf_path.write_bytes(data)
                with pdfplumber.open(pdf_path) as pdf:
                    pages=[]
                    for i,page in enumerate(pdf.pages,1):
                        sizes=[c['size'] for c in page.chars if c['text'].strip()]
                        if not sizes or min(sizes)<7.99:raise AssertionError(f'{pdf_path} Seite{i}: Schrift zu klein {min(sizes) if sizes else "leer"}')
                        pages.append({'page':i,'min_font_pt':round(min(sizes),2),'fonts':sorted({c['fontname'] for c in page.chars}),'size':[page.width,page.height]})
                    entry['variants'].append({'variant':variant,'pdf':str(pdf_path),'sha256':hashlib.sha256(data).hexdigest(),'pages':pages})
            if hashlib.sha256(source.read_bytes()).hexdigest()!=hashes[source]:raise AssertionError('Original geändert')
            report.append(entry)
    (output/'native-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'Native Druckprüfung bestanden: {len(selected)} Originale, normale und +25% Spaltenmaß-Druckkopien')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--native',type=Path,metavar='OUTPUT_DIR')
    parser.add_argument('--only',action='append')
    args=parser.parse_args()
    tests=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(PrintProfileTests))
    if not tests.wasSuccessful():raise SystemExit(1)
    if args.native:native_check(args.native,args.only)
