#!/usr/bin/env python3
"""Unabhängige Bestands- und Rechenkontrolle der Einstiegsakte Kleinhausen.

Der Test liest die erzeugten Originaldateien und den nach redaktioneller
Gegenprüfung fixierten Bestand. Er importiert weder Builderdaten noch deren
Erwartungswerte. Ein Bestehen ersetzt keine rechtliche oder visuelle Prüfung.
"""
from collections import Counter
from datetime import date, datetime, timedelta
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import hashlib
import json
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile

from testakte_file_filter import include_in_working_dump


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'testakten' / 'weg-kleinhausen'
AUDIT = ROOT / 'quality/source-audits/weg-kleinhausen-2026-10-02'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
WORD_NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def workbook(path):
    """Lese Zellwerte und Formeln samt numerischen Caches direkt aus OOXML."""
    result = {}
    with zipfile.ZipFile(path) as package:
        shared = []
        if 'xl/sharedStrings.xml' in package.namelist():
            shared = [''.join(node.itertext()) for node in
                      ET.fromstring(package.read('xl/sharedStrings.xml'))]
        book = ET.fromstring(package.read('xl/workbook.xml'))
        relations = ET.fromstring(package.read('xl/_rels/workbook.xml.rels'))
        for sheet in book.find('s:sheets', NS):
            target = next(r.get('Target') for r in relations
                          if r.get('Id') == sheet.get(RID))
            member = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            cells = {}
            for node in ET.fromstring(package.read(member)).findall('.//s:c', NS):
                value = node.find('s:v', NS)
                formula = node.find('s:f', NS)
                kind = node.get('t')
                raw = value.text if value is not None else None
                if kind == 's':
                    parsed = shared[int(raw)]
                elif kind == 'inlineStr':
                    parsed = ''.join(node.find('s:is', NS).itertext())
                elif kind in {'str', 'e'}:
                    parsed = raw
                elif raw is not None:
                    parsed = Decimal(raw)
                else:
                    parsed = None
                cells[node.get('r')] = {'value': parsed,
                                       'formula': formula.text if formula is not None else None,
                                       'type': kind}
            result[sheet.get('name')] = cells
    return result


def native_text(path):
    if path.suffix == '.docx':
        with zipfile.ZipFile(path) as package:
            root = ET.fromstring(package.read('word/document.xml'))
        return '\n'.join(''.join(p.itertext()) for p in root.findall('.//w:p', WORD_NS))
    if path.suffix == '.xlsx':
        return '\n'.join(str(cell['value']) for cells in workbook(path).values()
                         for cell in cells.values() if cell['value'] is not None)
    if path.suffix == '.eml':
        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        body = message.get_body(preferencelist=('plain',))
        return body.get_content() if body else ''
    return path.read_text(encoding='utf-8')


def euro_amount(text, pattern):
    match = re.search(pattern + r' ([\d.]+,\d{2}) EUR', text)
    if not match:
        raise AssertionError(f'Betrag nicht gefunden: {pattern}')
    return Decimal(match.group(1).replace('.', '').replace(',', '.'))


def booking_date(value):
    if isinstance(value, Decimal):
        if value != int(value):
            raise AssertionError(f'Unerwarteter Zeitanteil im Buchungstag: {value}')
        # Die Arbeitsmappe verwendet das normale Excel-Datumssystem 1900.
        return date(1899, 12, 30) + timedelta(days=int(value))
    return datetime.strptime(value, '%d.%m.%Y').date()


def invoice_amounts():
    """Beträge der Rechnungen selbst, unabhängig vom Abrechnungsentwurf."""
    sources = [
        ('09_Wasser_Abwasser.docx', 'insgesamt'),
        ('10_Muellgebuehren.docx', 'Jahresgebühr von'),
        ('11_Gebaeudeversicherung.docx', 'Jahresbeitrag einschließlich Versicherungssteuer beträgt'),
        ('12_Allgemeinstrom.docx', 'Jahresbetrag beträgt'),
        ('13_Treppenhausreinigung.docx', 'Jahresvergütung beträgt'),
        ('14_Tuerreparatur.docx', 'Gesamtbetrag beträgt'),
        ('15_Verwalterhonorar.docx', 'Jahresbetrag beträgt'),
        ('16_Bankentgelte.docx', 'Jahresbelastung beträgt damit'),
    ]
    result = []
    for name, pattern in sources:
        text = native_text(CASE / name)
        reference = re.search(r'\d{2}\.\d{2}\.2025 · ([A-Z]+-2025-\d+)', text)
        if reference is None:
            raise AssertionError(f'Belegnummer fehlt: {name}')
        result.append((name, euro_amount(text, pattern), reference.group(1)))
    return result


def word_tables(path):
    with zipfile.ZipFile(path) as package:
        document = ET.fromstring(package.read('word/document.xml'))
    return [[[''.join(cell.itertext()) for cell in row.findall('w:tc', WORD_NS)]
             for row in table.findall('w:tr', WORD_NS)]
            for table in document.findall('.//w:tbl', WORD_NS)]


class KleinhausenOriginaleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((AUDIT / 'originalbestand.json').read_text())
        cls.files = [p for p in sorted(CASE.iterdir())
                     if p.is_file() and include_in_working_dump(p, CASE)]
        cls.book = workbook(CASE / '06_Abrechnung_2025_Arbeitsdatei.xlsx')

    def number(self, sheet, cell):
        value = self.book[sheet][cell]['value']
        self.assertIsInstance(value, Decimal, f'{sheet}/{cell}: numerischer Cache fehlt')
        self.assertTrue(value.is_finite(), f'{sheet}/{cell}: unendlicher Wert')
        return value

    def test_gepruefter_originalbestand_bleibt_vollstaendig(self):
        expected = {row['datei']: row for row in self.manifest['originale']}
        self.assertEqual({p.name for p in self.files}, set(expected))
        self.assertEqual(len(expected), self.manifest['anzahl'])
        self.assertEqual(Counter(p.suffix for p in self.files),
                         {'.docx': 23, '.eml': 6, '.xlsx': 1, '.txt': 1})
        for path in self.files:
            with self.subTest(datei=path.name):
                self.assertEqual(sha256(path), expected[path.name]['sha256'])
        for excluded in ('README.md', 'rubric.yaml'):
            self.assertFalse(include_in_working_dump(CASE / excluded, CASE))

    def test_nur_originalformate_und_keine_versteckte_loesung(self):
        self.assertTrue(self.files)
        self.assertTrue(all(p.suffix in {'.docx', '.xlsx', '.eml', '.txt'} for p in self.files))
        forbidden = re.compile(r'musterl[oö]sung|erwartungshorizont|pr[uü]ferhinweis|'
                               r'absichtlich(?:er|e|en)?\s+fehler|eingebaute[nr]?\s+fehler|'
                               r'diese\s+testakte|github-release', re.I)
        for path in self.files:
            with self.subTest(datei=path.name):
                self.assertIsNone(forbidden.search(native_text(path)))
        # Eine einzige einfache Arbeitsmappe mit höchstens drei Blättern.
        books = [p for p in self.files if p.suffix == '.xlsx']
        self.assertEqual(len(books), 1)
        self.assertLessEqual(len(workbook(books[0])), 3)

    def test_emails_enthalten_echte_bytegleiche_anlagen(self):
        attachment_count = 0
        for path in self.files:
            if path.suffix != '.eml':
                continue
            with self.subTest(nachricht=path.name):
                message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                self.assertTrue(message['Subject'])
                self.assertTrue(message['From'])
                self.assertTrue(message['To'])
                self.assertIsNotNone(parsedate_to_datetime(message['Date']).tzinfo)
                self.assertFalse(message.defects)
                body = message.get_body(preferencelist=('plain',))
                self.assertIsNotNone(body)
                parts = list(message.iter_attachments())
                names = [part.get_filename() for part in parts]
                self.assertEqual(len(names), len(set(names)))
                for part in parts:
                    name = part.get_filename()
                    self.assertEqual(Path(name).name, name)
                    self.assertIn(name, {p.name for p in self.files})
                    self.assertEqual(part.get_payload(decode=True), (CASE / name).read_bytes())
                    attachment_count += 1
        self.assertGreater(attachment_count, 0)

    def test_fuenf_eigentuemer_anteile_und_vollstaendige_vorschuesse(self):
        units = [self.book['Vorschuesse'][f'A{row}']['value'] for row in range(2, 7)]
        self.assertEqual(units, [f'WE{unit:02d}' for unit in range(1, 6)])
        shares = []
        for index, unit in enumerate(units, 18):
            path = CASE / f'{index:02d}_Einzelabrechnung_{unit}.docx'
            text = native_text(path)
            share = re.search(r'mit (\d+) von ([\d.]+) Miteigentumsanteilen', text)
            self.assertIsNotNone(share)
            self.assertEqual(int(share.group(2).replace('.', '')), 1000)
            shares.append(int(share.group(1)))
            self.assertIn('Es bestehen keine Vorschussrückstände', text)
        self.assertEqual(shares, [200] * 5)
        self.assertEqual(sum(shares), 1000)
        self.assertIn('Alle Wohnungen werden von ihren Eigentümern selbst genutzt',
                      native_text(CASE / '02_Stammdaten.docx'))
        for row in range(2, 7):
            cost = self.number('Vorschuesse', f'C{row}') * 12
            reserve = self.number('Vorschuesse', f'D{row}') * 12
            self.assertEqual(cost, 1200)
            self.assertEqual(reserve, 300)
            self.assertEqual(self.number('Vorschuesse', f'E{row}'), cost)
            self.assertEqual(self.number('Vorschuesse', f'F{row}'), reserve)
            self.assertEqual(self.number('Vorschuesse', f'G{row}'), cost + reserve)
            self.assertEqual(self.number('Vorschuesse', f'H{row}'), 0)

    def test_jede_bankbewegung_und_unabhaengige_rechenbruecke(self):
        # Anfangsbestand ist kein Jahreseingang; Umbuchung ist keine Ausgabe
        # an einen Lieferanten. Jede gespeicherte Saldoformel wird nachgerechnet.
        bank = self.book['Bankbuch']
        saldo = self.number('Bankbuch', 'C2') - self.number('Bankbuch', 'D2')
        self.assertEqual(saldo, 1000)
        received, outgoing = Counter(), Counter()
        monthly_receipts = Counter()
        closed = {date(2025, 1, 1), date(2025, 4, 18), date(2025, 4, 21),
                  date(2025, 5, 1), date(2025, 12, 25), date(2025, 12, 26)}
        dates = []
        for row in range(3, 119):
            day = booking_date(bank[f'A{row}']['value'])
            dates.append(day)
            self.assertEqual(day.year, 2025)
            self.assertLess(day.weekday(), 5)
            self.assertNotIn(day, closed)
            incoming = self.number('Bankbuch', f'C{row}')
            paid = self.number('Bankbuch', f'D{row}')
            ref = bank[f'F{row}']['value']
            self.assertGreaterEqual(incoming, 0)
            self.assertGreaterEqual(paid, 0)
            self.assertFalse(incoming and paid)
            saldo += incoming - paid
            self.assertEqual(self.number('Bankbuch', f'E{row}'), saldo)
            self.assertGreaterEqual(saldo, 0)
            if incoming:
                self.assertRegex(ref, r'^WE0[1-5]$')
                self.assertEqual(incoming, 125)
                self.assertLessEqual(day.day, 10)
                received[ref] += incoming
                monthly_receipts[(ref, day.month)] += 1
            if paid:
                outgoing[ref] += paid
        self.assertEqual(dates, sorted(dates))
        self.assertEqual(len(monthly_receipts), 5 * 12)
        self.assertEqual(set(monthly_receipts.values()), {1})
        self.assertEqual(dict(received), {f'WE{unit:02d}': 1500 for unit in range(1, 6)})
        bills = {ref: amount for _, amount, ref in invoice_amounts()}
        self.assertEqual(outgoing.pop('RL-2025-01'), 1500)
        self.assertEqual(dict(outgoing), bills)
        actual_cost = sum(bills.values())
        self.assertEqual(actual_cost, 1600 + 600 + 1000 + 240 + 960 + 300 + 900 + 60)
        self.assertEqual(saldo, 1000 + sum(received.values()) - actual_cost - 1500)
        self.assertEqual(saldo, 1340)
        reserve_text = native_text(CASE / '08_Ruecklagenkonto.docx')
        reserve = euro_amount(reserve_text, 'Schlussbestand am 31. Dezember 2025 beträgt')
        self.assertEqual(reserve, 5000 + 1500)
        wealth_text = native_text(CASE / '31_Vermoegensbericht.docx')
        self.assertEqual(euro_amount(wealth_text, 'beiden Bankguthaben betragen zusammen'), saldo + reserve)
        self.assertEqual(saldo + reserve, 7840)
        # Monatsübersicht im Word-Bankbeleg zusätzlich gegen Einzelbuchungen.
        overview = word_tables(CASE / '07_Bank_Jahresuebersicht.docx')[0][1:]
        self.assertEqual(len(overview), 12)
        for month, record in enumerate(overview, 1):
            rows = [r for r in range(3, 119) if dates[r - 3].month == month]
            amount = lambda field: Decimal(field.removesuffix(' EUR').replace('.', '').replace(',', '.'))
            self.assertEqual(amount(record[1]), sum(self.number('Bankbuch', f'C{r}') for r in rows))
            costs = sum(self.number('Bankbuch', f'D{r}') for r in rows if bank[f'F{r}']['value'] != 'RL-2025-01')
            self.assertEqual(amount(record[2]), costs)
            self.assertEqual(amount(record[4]), self.number('Bankbuch', f'E{rows[-1]}'))

    def test_genau_zwei_kleine_abweichungen_im_entwurf(self):
        draft = self.book['Abrechnungsentwurf']
        amount_differences, reference_differences = [], []
        actual_cost = Decimal(0)
        for row, (_, amount, ref) in enumerate(invoice_amounts(), 2):
            actual_cost += amount
            label = draft[f'A{row}']['value']
            shown_amount = self.number('Abrechnungsentwurf', f'B{row}')
            shown_ref = draft[f'C{row}']['value']
            if shown_amount != amount:
                amount_differences.append((label, shown_amount - amount))
            if shown_ref != ref:
                reference_differences.append((label, shown_ref, ref))
            self.assertEqual(self.number('Abrechnungsentwurf', f'D{row}'), shown_amount / 5)
        self.assertEqual(amount_differences, [('Allgemeinstrom', Decimal(20))])
        self.assertEqual(reference_differences, [('Treppenhausreinigung', 'R-2025-71', 'R-2025-17')])
        draft_cost = sum(self.number('Abrechnungsentwurf', f'B{row}') for row in range(2, 10))
        advance = self.number('Vorschuesse', 'E7')
        self.assertEqual(self.number('Abrechnungsentwurf', 'B10'), draft_cost)
        self.assertEqual(self.number('Abrechnungsentwurf', 'B13'), advance - draft_cost)
        self.assertEqual(self.number('Abrechnungsentwurf', 'D13'), (advance - draft_cost) / 5)
        self.assertEqual((advance - actual_cost) / 5, 68)
        self.assertEqual((advance - draft_cost) / 5, 64)
        # Die fünf Briefe und die Beschlussvorlage übernehmen nur die Folge
        # dieses einen Betragsfehlers. Keine bereits korrigierte Lösung ausliefern.
        for path in sorted(CASE.glob('*_Einzelabrechnung_WE*.docx')):
            text = native_text(path)
            self.assertEqual(euro_amount(text, 'Ihr Anteil beträgt'), draft_cost / 5)
            self.assertEqual(euro_amount(text, 'Guthaben von'), (advance - draft_cost) / 5)
        table = word_tables(CASE / '17_Gesamtabrechnung_Entwurf.docx')[0][1:]
        self.assertEqual(len(table), 8)
        for row, cells in enumerate(table, 2):
            self.assertEqual(cells[0], draft[f'A{row}']['value'])
            self.assertEqual(Decimal(cells[1].removesuffix(' EUR').replace('.', '').replace(',', '.')),
                             self.number('Abrechnungsentwurf', f'B{row}'))
            self.assertEqual(cells[2], draft[f'C{row}']['value'])
        proposal = native_text(CASE / '28_Beschlussvorlage_Entwurf.docx')
        self.assertIn('Anpassung der beschlossenen Kostenvorschüsse', proposal)
        self.assertIn('innerhalb von vierzehn Tagen nach der Beschlussfassung', proposal)
        self.assertIn('Beiträge zur Erhaltungsrücklage bleiben unverändert', proposal)
        self.assertEqual(euro_amount(proposal, 'Guthaben von'), (advance - draft_cost) / 5)
        for cells in self.book.values():
            for reference, cell in cells.items():
                self.assertNotEqual(cell['type'], 'e', reference)
                if cell['formula'] is not None:
                    self.assertIsInstance(cell['value'], Decimal, reference)


if __name__ == '__main__':
    unittest.main()
