#!/usr/bin/env python3
"""Unabhängige Prüfung fertiger Projektunterlagen und ihrer Release-Archive.

Liest Originale, CSVs, MIME-Anlagen und PDF-Lesezeichen. Importiert keinen
Akten-Generator. Die fachliche Sichtprüfung wird dadurch nicht ersetzt.
"""
from __future__ import annotations
import argparse
from bisect import bisect_left
from collections import Counter, defaultdict
import csv
from datetime import date, datetime, timedelta
from decimal import Decimal as D
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
import unicodedata
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import pdfplumber
from pypdf import PdfReader
from reportlab.pdfgen import canvas
from testakte_disclaimer import NOTICE_BYTES
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import working_dump_archive_pairs, safe_archive_name

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'bauwirtschaft-hildesheim-lebensakte'
CASE = ROOT/'testakten'/SLUG
BASE = ROOT/'testakten/bauwirtschaft-neubau-achtfamilienhaus-hildesheim'
QA = ROOT/'quality/hildesheim-lebensakte'
ASSETS = None
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def csv_rows(path, delimiter=','):
    with path.open(encoding='utf-8-sig', newline='') as source:
        return list(csv.DictReader(source, delimiter=delimiter))


def word_xml(path):
    with ZipFile(path) as archive:
        return ET.fromstring(archive.read('word/document.xml'))


def word_text(path):
    return ' '.join(n.text or '' for n in word_xml(path).findall('.//w:t', NS))


def de_amount(value):
    return D(value.replace('.', '').replace(',', '.'))


def diary_title(day):
    months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August',
              'September', 'Oktober', 'November', 'Dezember']
    return f'Bautagebuch {day.day:02d} {months[day.month-1]} {day.year}'


def destinations(outline):
    for item in outline:
        if isinstance(item, list):
            yield from destinations(item)
        else:
            yield item


class ProjectFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pairs = document_arcname_pairs(CASE)
        cls.by_relative = {p.relative_to(CASE).as_posix(): p for p, _ in cls.pairs}

    def assert_pdf_contents(self, checker, path, pages):
        if path.suffix != '.csv':
            checker.assert_export_contains_original(path, pages)
            return
        raw = path.read_text(encoding='utf-8-sig')
        delimiter = ';' if raw.splitlines()[0].count(';') > raw.splitlines()[0].count(',') else ','
        rows = list(csv.reader(io.StringIO(raw), delimiter=delimiter))
        def compact(value):
            return ''.join(re.findall(r'[^\W_]+', unicodedata.normalize('NFKC', value).casefold()))
        text = unicodedata.normalize('NFKC', '\n'.join(page.extract_text() or '' for page in pages)).casefold()
        text = text.replace('\N{MINUS SIGN}', '-')
        # Auch ein beim Umbruch abgesetztes Vorzeichen gehört zur Zahl.
        text = re.sub(r'(?<!\w)([+-])\s+(?=\d)', r'\1', text)
        positions = [i for i, char in enumerate(text) if char.isalnum()]
        rendered = ''.join(text[i] for i in positions)
        for heading in rows[0]:
            self.assertIn(compact(heading), rendered)
        offset = 0
        for row in rows[1:]:
            for cell in row:
                numeric = unicodedata.normalize('NFKC', cell).strip().replace('\N{MINUS SIGN}', '-')
                if re.fullmatch(r'[+-]?\d+(?:[.,]\d+)*', numeric):
                    # Zahlen nicht alphanumerisch reduzieren: Sonst werden
                    # -89.250,00 und 89.250,00 oder 3,5 und 35 gleichgesetzt.
                    # Leerraum innerhalb einer umbrochenen Zahl bleibt zulässig.
                    pattern = re.compile(r'(?<![\w.,+-])' + r'\s*'.join(map(re.escape, numeric)) + r'(?![\w.,])')
                    match = pattern.search(text, offset)
                    self.assertIsNotNone(match, f'CSV-Zahl fehlt oder ist verändert: {path.name}: {cell}')
                    offset = match.end()
                    continue
                value = compact(cell)
                if not value:
                    continue
                start = bisect_left(positions, offset)
                found = rendered.find(value, start)
                self.assertGreaterEqual(found, start, f'CSV-Zelle fehlt: {path.name}: {cell}')
                offset = positions[found+len(value)-1]+1

    def test_every_original_is_exported_and_baseline_is_byte_identical(self):
        physical = {p for p in CASE.rglob('*') if p.is_file() and p.suffix not in {'.md', '.yaml'}
                    and 'gesamt-pdf' not in p.relative_to(CASE).parts}
        self.assertEqual({p for p, _ in self.pairs}, physical)
        self.assertEqual(len(physical), 410)
        self.assertEqual(Counter(p.suffix for p in physical),
                         {'.docx': 184, '.pdf': 101, '.eml': 84, '.xml': 28,
                          '.csv': 7, '.xlsx': 3, '.png': 2, '.txt': 1})
        mapping = json.loads((QA/'basisdateien.json').read_text())
        self.assertEqual(len(mapping), 198)
        for item in mapping:
            with self.subTest(original=item['source']):
                source, target = BASE/item['source'], CASE/item['target']
                self.assertEqual(target.read_bytes(), source.read_bytes())
                self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(), item['sha256'])

    def test_calendar_and_daily_pages_have_no_gaps(self):
        rows = csv_rows(CASE/'08_Bauausfuehrung/01_Bautagebuch/Bautagebuch_Kalenderregister.csv')
        expected = [date(2027, 12, 1)+timedelta(days=i) for i in range(304)]
        self.assertEqual([r['Datum'] for r in rows], [d.isoformat() for d in expected])
        self.assertEqual([int(r['Tagesblatt']) for r in rows], list(range(1, 305)))
        names = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        months = defaultdict(list)
        for day, row in zip(expected, rows):
            self.assertEqual(row['Wochentag'], names[day.weekday()])
            if day.weekday() >= 5 or row['Feiertag']:
                self.assertEqual(int(row['Produktivpersonal']), 0, day.isoformat())
            months[row['Monatsdatei']].append(day)
        self.assertEqual(len(months), 10)
        for name, days in months.items():
            text = word_text(CASE/'08_Bauausfuehrung/01_Bautagebuch'/name)
            for day in days:
                self.assertIn(diary_title(day), text)
        diary = PdfReader(CASE/'gesamt-pdf'/f'{SLUG}_bautagebuch.pdf')
        self.assertEqual(len(diary.pages), 304)
        for day, page in zip(expected, diary.pages):
            self.assertIn(diary_title(day), ' '.join(page.extract_text().split()))

    def test_detail_lv_matches_all_original_lump_sum_groups(self):
        rows = csv_rows(CASE/'06_Leistungsverzeichnisse/Detail-LV/LV_Kalkulationsregister.csv')
        self.assertEqual(len(rows), 134)
        self.assertEqual(len({r['id'] for r in rows}), 134)
        groups, lots = defaultdict(D), defaultdict(D)
        for row in rows:
            self.assertEqual((D(row['qty'])*D(row['unit_price'])).quantize(D('.01')), D(row['net']))
            groups[row['parent_id']] += D(row['net'])
            lots[row['actor']] += D(row['net'])
        self.assertEqual(len(groups), 26)
        for row in rows:
            self.assertEqual(groups[row['parent_id']], D(row['group_total']))
        self.assertEqual(dict(lots), {'rohbau': D(650000), 'huelle': D(440000), 'hls': D(360000),
                                     'elektro': D(150000), 'ausbau': D(300000), 'aufzug': D(60000),
                                     'aussen': D(120000)})
        self.assertEqual(sum(lots.values()), D(2080000))
        documents = sorted((CASE/'06_Leistungsverzeichnisse/Detail-LV').glob('*.docx'))
        self.assertEqual(len(documents), 7)
        joined = ' '.join(word_text(p) for p in documents)
        for row in rows:
            self.assertIn(row['id'], joined)
            self.assertIn(row['title'], joined)

    def test_actual_invoice_mail_attachments_and_dates(self):
        originals = {p.name: p for p, _ in self.pairs if not p.parent.name == 'Rechnungseingang'}
        invoices = json.loads((ROOT/'quality/hildesheim-achtfamilienhaus/finanzdaten.json').read_text())['invoices']
        expected = {r['id']: r for r in invoices if Path(r['filename']).stem+'_XRechnung.xml' in originals}
        mails = sorted((CASE/'10_Rechnungen_und_Buchhaltung/Rechnungseingang').glob('*.eml'))
        self.assertEqual(len(mails), 28)
        seen = set()
        for path in mails:
            with self.subTest(mail=path.name):
                mail = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                matches = [r for key, r in expected.items() if '/ Rechnung '+key+' /' in mail['Subject']
                           or '/ Rechnungskorrektur '+key+' /' in mail['Subject']]
                self.assertEqual(len(matches), 1)
                invoice = matches[0]; seen.add(invoice['id'])
                stamp = parsedate_to_datetime(mail['Date'])
                self.assertEqual(stamp.date().isoformat(), invoice['date'])
                self.assertIsNotNone(stamp.utcoffset())
                self.assertTrue(mail['From'].addresses[0].addr_spec.endswith('.example'))
                self.assertTrue(mail['To'].addresses[0].addr_spec.endswith('.example'))
                attachments = list(mail.iter_attachments())
                names = {a.get_filename() for a in attachments}
                self.assertEqual(names, {invoice['filename'], Path(invoice['filename']).stem+'_XRechnung.xml'})
                for attachment in attachments:
                    self.assertEqual(attachment.get_payload(decode=True), originals[attachment.get_filename()].read_bytes())
                self.assertIn('denselben Abrechnungsbeleg', mail.get_body(preferencelist=('plain',)).get_content())
        self.assertEqual(seen, set(expected))

    def test_optional_sale_numbers_and_draft_status(self):
        rows = csv_rows(CASE/'13_Option_Bautraegerverkauf/00_Entscheidungsvorbereitung/OP04_Preisansatz_und_Ratenkontrolle.csv', ';')
        self.assertEqual(len(rows), 8)
        self.assertEqual([int(r['Wohnfläche_m2']) for r in rows], [68, 75, 82, 68, 75, 82, 75, 75])
        self.assertEqual(sum(int(r['MEA_Zähler']) for r in rows), 600)
        self.assertEqual({int(r['MEA_Nenner']) for r in rows}, {600})
        self.assertEqual(sum(de_amount(r['Planpreis_EUR']) for r in rows), D(3672000))
        percentages = [D('30'), D('28'), D('12.6'), D('6.3'), D('8.4'), D('11.2'), D('3.5')]
        self.assertEqual(sum(percentages), 100)
        for row in rows:
            self.assertEqual(row['Status'], 'Option_nicht_beschlossen')
            price = de_amount(row['Planpreis_EUR'])
            self.assertEqual(de_amount(row['Sicherheit_5Prozent_EUR']), price*D('.05'))
            self.assertEqual(de_amount(row['Erste_Auszahlung_25Prozent_EUR']), price*D('.25'))
            self.assertEqual([de_amount(row[f'Rate{i}_EUR']) for i in range(1, 8)],
                             [price*p/100 for p in percentages])
        contracts = sorted((CASE/'13_Option_Bautraegerverkauf/01_Vertragsentwuerfe').glob('*.docx'))
        self.assertEqual(len(contracts), 8)
        for contract in contracts:
            self.assertIn('Entwurf', word_text(contract))

    def test_defect_followups_and_templates_are_separate(self):
        rows = csv_rows(CASE/'08_Bauausfuehrung/03_Maengel/Maengelregister.csv')
        self.assertEqual(len(rows), 12)
        self.assertEqual(len({r['id'] for r in rows}), 12)
        documents = [word_text(p) for p in (CASE/'08_Bauausfuehrung/03_Maengel').glob('*.docx')]
        self.assertEqual(len(documents), 24)
        for row in rows:
            self.assertLessEqual(date.fromisoformat(row['opened']), date.fromisoformat(row['closed']))
            self.assertGreaterEqual(sum(row['id'] in text for text in documents), 2)
        forms = sorted((CASE/'12_Wordvorlagen').rglob('*.docx'))
        self.assertEqual(len(forms), 18)
        for path in (CASE/'12_Wordvorlagen/Kaufmaennisch').glob('*.docx'):
            xml = word_xml(path)
            fields = xml.findall('.//w:sdt', NS)
            self.assertGreaterEqual(len(fields), 10)
            self.assertTrue(all(f.find('w:sdtPr/w:tag', NS) is not None for f in fields))

    def test_everyday_correspondence_has_traceable_threads(self):
        prior = json.loads((QA/'alltag-bestand-v445.8.0.json').read_text())['originals']
        self.assertEqual(len(prior), 366)
        for item in prior:
            self.assertEqual(hashlib.sha256(self.by_relative[item['source']].read_bytes()).hexdigest(), item['sha256'])
        rows = json.loads((QA/'alltag-manifest.json').read_text())
        by_id = {row['id']: row for row in rows}
        self.assertEqual(len(rows), 44)
        self.assertEqual(len(by_id), len(rows))
        self.assertEqual(sorted(Counter(row['thread'] for row in rows).values()), [4]*11)
        mails = {}
        for row in rows:
            path = self.by_relative[row['source']]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row['sha256'])
            for reference in row['references']:
                self.assertIn(reference, self.by_relative)
            if row['reply_to']:
                previous = by_id[row['reply_to']]
                self.assertEqual(row['thread'], previous['thread'])
                self.assertLess(datetime.fromisoformat(previous['date']), datetime.fromisoformat(row['date']))
            if path.suffix != '.eml':
                self.assertIn(datetime.fromisoformat(row['date']).strftime('%d.%m.%Y'), word_text(path))
                continue
            mail = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
            mails[row['id']] = mail
            self.assertFalse(mail.defects)
            stamp = parsedate_to_datetime(mail['Date'])
            self.assertIsNotNone(stamp.utcoffset())
            self.assertEqual(stamp.replace(tzinfo=None).isoformat(), row['date'])
            for header in ('From', 'To'):
                self.assertEqual(len(mail[header].addresses), 1)
                self.assertTrue(mail[header].addresses[0].addr_spec.endswith('.example'))
            self.assertEqual(list(mail.iter_attachments()), [])
            self.assertNotIn('X-Attachments', mail)
        self.assertEqual(len({m['Message-ID'] for m in mails.values()}), len(mails))
        for row in rows:
            if row['id'] not in mails:
                continue
            chain = []
            previous = row['reply_to']
            while previous:
                if previous in mails:
                    chain.insert(0, str(mails[previous]['Message-ID']))
                previous = by_id[previous]['reply_to']
            mail = mails[row['id']]
            if chain:
                self.assertEqual(str(mail['In-Reply-To']), chain[-1])
                self.assertEqual(str(mail['References']).split(), chain)
            else:
                self.assertIsNone(mail['In-Reply-To'])
                self.assertIsNone(mail['References'])

    def test_archive_paths_original_bytes_and_pdf_contents(self):
        if ASSETS is None:
            self.skipTest('Mit --assets DIR die fertigen Release-Archive prüfen')
        spec = importlib.util.spec_from_file_location('baseline_regression', ROOT/'scripts/test-bauwirtschaft-hildesheim.py')
        baseline = importlib.util.module_from_spec(spec); spec.loader.exec_module(baseline)
        checker = baseline.HildesheimCase()
        originals = dict((arc, path) for path, arc in working_dump_archive_pairs(CASE, include_gesamt_pdf=True))
        single_names = dict((arc, path) for path, arc in self.pairs)
        for suffix in ('', '-einzelpdfs'):
            with ZipFile(ASSETS/f'testakte-{SLUG}{suffix}.zip') as archive:
                names = archive.namelist()
                self.assertEqual(names[0], 'README.txt')
                self.assertTrue(archive.read('README.txt').startswith(NOTICE_BYTES))
                self.assertEqual(len(names), len({n.casefold() for n in names}))
                self.assertTrue(all(safe_archive_name(n, allow_directories=True) for n in names))
                self.assertIsNone(archive.testzip())
                expected = single_names if suffix else originals
                self.assertEqual(set(names), {'README.txt', *expected})
                for arc, path in expected.items():
                    with self.subTest(archive=suffix, document=arc):
                        if suffix:
                            self.assert_pdf_contents(checker, path, PdfReader(io.BytesIO(archive.read(arc))).pages)
                        else:
                            self.assertEqual(archive.read(arc), path.read_bytes())
        total = PdfReader(CASE/'gesamt-pdf'/f'{SLUG}_gesamt.pdf')
        outline = list(destinations(total.outline))
        documents = [d for d in outline if d.title in self.by_relative]
        self.assertEqual([d.title for d in documents], list(self.by_relative))
        starts = [total.get_destination_page_number(d) for d in documents]+[len(total.pages)]
        self.assertGreater(starts[0], 0)
        self.assertEqual(starts, sorted(set(starts)))
        with pdfplumber.open(CASE/'gesamt-pdf'/f'{SLUG}_gesamt.pdf') as print_view:
            printed = []
            for page in print_view.pages[:starts[0]]:
                for table in page.extract_tables():
                    printed.extend(row for row in table if len(row) == 3 and row[1] and row[1].isdigit())
            self.assertEqual(len(printed), len(documents))
            for i, row in enumerate(printed):
                self.assertEqual(''.join(row[0].split()), ''.join(documents[i].title.split()))
                self.assertEqual(int(row[1]), starts[i]+1)
                self.assertEqual(int(row[2]), starts[i+1]-starts[i])
        for i, entry in enumerate(documents):
            with self.subTest(combined=entry.title):
                self.assert_pdf_contents(checker, self.by_relative[entry.title], total.pages[starts[i]:starts[i+1]])


class CsvExportMutations(unittest.TestCase):
    def assert_csv_pdf(self, original_amount, rendered_amount, *, wrap_text=False):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary)/'bank.csv'
            source.write_text('Beleg;Betrag;Vermerk\nEL-2028-02;'+original_amount+';Erstattung nach abgeschlossenem Abgleich\n', encoding='utf-8')
            output = io.BytesIO()
            pdf = canvas.Canvas(output)
            lines = ['Beleg Betrag Vermerk', 'EL-2028-02', *rendered_amount.splitlines()]
            lines += (['Erstattung nach', 'abgeschlossenem Abgleich'] if wrap_text
                      else ['Erstattung nach abgeschlossenem Abgleich'])
            for i, line in enumerate(lines):
                pdf.drawString(40, 800-i*18, line)
            pdf.save()
            ProjectFile().assert_pdf_contents(None, source, PdfReader(io.BytesIO(output.getvalue())).pages)

    def test_numeric_mutations_in_real_pdf_are_rejected(self):
        for original, changed in [('-89.250,00', '89.250,00'), ('89.250,00', '-89.250,00'),
                                  ('89.250,00', '- 89.250,00'), ('3,5', '35'), ('12.60', '1260')]:
            with self.subTest(original=original, changed=changed), self.assertRaises(AssertionError):
                self.assert_csv_pdf(original, changed)

    def test_text_and_number_line_breaks_remain_allowed(self):
        self.assert_csv_pdf('-89.250,00', '- 89.250,00', wrap_text=True)
        self.assert_csv_pdf('12.60', '12.\n60', wrap_text=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets', type=Path)
    args, rest = parser.parse_known_args()
    ASSETS = args.assets.resolve() if args.assets else None
    unittest.main(argv=[__file__, *rest], verbosity=2)
