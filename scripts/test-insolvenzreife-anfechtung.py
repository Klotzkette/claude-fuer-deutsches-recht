#!/usr/bin/env python3
"""Unabhängige Beleg-, Varianten- und Paketprüfung der Anfechtungsergänzung.

Die eingefrorenen Bankdaten stammen aus dem veröffentlichten Stand 1.1.0.
Ergänzende Sachverhalte dürfen vorhandene Geldflüsse erläutern, aber keinen
zweiten Geldfluss erzeugen oder die Ausgangssalden heimlich umschreiben.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from email import policy
from email.parser import BytesParser
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from zipfile import ZipFile

from docx import Document
from pypdf import PdfReader
from testakte_zip_common import working_dump_archive_pairs
from testakte_file_filter import include_in_working_dump
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'zahlungsunfaehigkeits-und-ueberschuldungspruefer'
CASES = json.loads((ROOT / 'scripts/data/zu-insolvenzfaelle.json').read_text(encoding='utf-8'))['cases']
BY_PREFIX = {case['prefix']: case for case in CASES}
SELECTION_FILE = ROOT / 'scripts/data/testakten-grundakten-insolvenzreife.json'
BASELINE = {
    'CB': (277, '292865ce8fb19bbf3d3339efeccce9f20c13213b587f1fdb6aebf490d7598d53'),
    'BZ': (267, '08732b917cc043abf0ab7dbbd07aaf6fda627e8cb55dd85d4e69bcf503926413'),
    'PR': (278, 'fb29831049a1feb0bf121bc570d35bdb9e96fbe9a991c8b602b00696e7e6a2a0'),
}
TEMPLATE_MAP = {
    '01_Anfechtungsschreiben.docx': '20_Vorlagen/01_Anfechtungsschreiben.docx',
    '02_Anfechtungsklage.docx': '20_Vorlagen/02_Anfechtungsklage.docx',
}
DIST = None


def canonical_digest(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream, delimiter=';'))


def docx_text(document):
    parts = [paragraph.text for paragraph in document.paragraphs]
    for table in document.tables:
        parts.extend(cell.text for row in table.rows for cell in row.cells)
    for section in document.sections:
        parts.extend(paragraph.text for paragraph in section.header.paragraphs)
        parts.extend(paragraph.text for paragraph in section.footer.paragraphs)
    return '\n'.join(parts)


class AnfechtungTest(unittest.TestCase):
    def test_822_originalbuchungen_und_saldokette_unveraendert(self):
        self.assertEqual(sum(len(case['transactions']) for case in CASES), 822)
        for case in CASES:
            with self.subTest(case=case['slug']):
                expected_count, expected_hash = BASELINE[case['prefix']]
                self.assertEqual(len(case['transactions']), expected_count)
                self.assertEqual(canonical_digest(case['transactions']), expected_hash,
                                 'Geldfluss, Bankzweck oder Saldo gegenüber Version 1.1.0 verändert')
                balance = case['opening_bank_balance_cents']
                ids = set()
                for row in case['transactions']:
                    self.assertNotIn(row['id'], ids)
                    ids.add(row['id'])
                    balance += row['amount_cents']
                    self.assertEqual(balance, row['balance_cents'], row['id'])
                    self.assertEqual(row['date'], row['value_on'])

    def test_zinsaufteilung_ist_ein_einziger_originalgeldfluss(self):
        package = json.loads((ROOT / 'scripts/data/insolvenzreife-anfechtungskomplexe.json').read_text(encoding='utf-8'))['cases']['CB']
        case = BY_PREFIX['CB']
        payment = next(row for row in case['transactions'] if row['id'] == 'CB-CAPEX-01-BK')
        self.assertEqual(package['payment_refs'], [payment['id']])
        self.assertEqual(package['event_date'], payment['date'])
        self.assertEqual(package['amount_cents'], -payment['amount_cents'])
        self.assertEqual(sum(component['amount_cents'] for component in package['components']), -payment['amount_cents'])
        self.assertEqual(len({component['label'] for component in package['components']}), len(package['components']))
        loan = package['loan']
        start = date.fromisoformat(loan['interest_from'])
        end = date.fromisoformat(loan['interest_through'])
        days_30_360 = ((end.year - start.year) * 360 + (end.month - start.month) * 30
                      + min(end.day, 30) - min(start.day, 30))
        self.assertEqual(days_30_360, 120)
        self.assertEqual(loan['interest_days_30_360'], days_30_360)
        interest = (Decimal(loan['principal_cents']) * Decimal(loan['annual_rate_percent'])
                    / 100 * days_30_360 / 360).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        self.assertEqual(loan['interest_cents'], int(interest))
        self.assertEqual(loan['interest_cents'], 480000)
        self.assertEqual(loan['creditor'], payment['counterparty'])
        self.assertFalse(loan['shareholder'], 'Unabhängiger Lieferant darf nicht ohne Beleg zum Gesellschafter werden')
        parts = {component['label']: component['amount_cents'] for component in package['components']}
        self.assertEqual(parts['Darlehenskapital'], loan['principal_cents'])
        self.assertEqual(parts['Darlehenszinsen'], loan['interest_cents'])
        self.assertEqual(parts['Zusatzmaterial netto'] + parts['Umsatzsteuer Zusatzmaterial'], 1200000)
        self.assertEqual(parts['Umsatzsteuer Zusatzmaterial'],
                         int((Decimal(parts['Zusatzmaterial netto']) * Decimal('0.19')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)))
        # Keine Umsatzsteuer auf die Tilgung oder nochmals auf den gesamten Bankbetrag.
        self.assertLess(parts['Umsatzsteuer Zusatzmaterial'], int(Decimal(package['amount_cents']) * Decimal('19') / Decimal('119')))

    def test_verrechnung_ohne_bankzahlung_und_ohne_gegenseitigkeit(self):
        package = json.loads((ROOT / 'scripts/data/insolvenzreife-anfechtungskomplexe.json').read_text(encoding='utf-8'))['cases']['BZ']
        case = BY_PREFIX['BZ']
        entry = package['setoff']
        receivable = next(row for row in case['receivables'] if row['id'] == entry['claim_id'])
        debt = next(row for row in case['obligations'] if row['id'] == entry['counterclaim_id'])
        self.assertEqual(entry['claim_creditor'], case['company'])
        self.assertEqual(entry['claim_debtor'], receivable['debtor'])
        self.assertEqual(entry['counterclaim_creditor'], debt['creditor'])
        self.assertEqual(entry['counterclaim_debtor'], case['company'])
        self.assertNotEqual(entry['claim_debtor'], entry['counterclaim_creditor'])
        self.assertEqual(entry['claim_cents'], receivable['amount_cents'])
        self.assertEqual(entry['counterclaim_cents'], debt['amount_cents'])
        self.assertEqual(package['amount_cents'], receivable['amount_cents'])
        self.assertEqual(entry['bank_amount_cents'], 0)
        self.assertEqual(package['payment_refs'], [])
        self.assertIsNone(receivable['payment_id'])
        self.assertIsNone(debt['payment_id'])
        petition = date.fromisoformat(case['procedure']['petition_on'])
        event = date.fromisoformat(package['event_date'])
        self.assertEqual(entry['petition_on'], petition.isoformat())
        self.assertEqual((petition.year - event.year) * 12 + petition.month - event.month, 2)
        self.assertEqual(event.day, petition.day)
        self.assertGreater(date.fromisoformat(debt['defer_until']), event)
        self.assertGreater(date.fromisoformat(receivable['available_on']), event)
        declaration = next(doc for doc in package['documents'] if doc['id'] == 'BZ-ZK-04')
        self.assertEqual(declaration['date'], event.isoformat())

    def test_vorkasse_ist_separater_vorgang_kein_doppelter_klagebetrag(self):
        package = json.loads((ROOT / 'scripts/data/insolvenzreife-anfechtungskomplexe.json').read_text(encoding='utf-8'))['cases']['PR']
        case = BY_PREFIX['PR']
        payments = {row['id']: row for row in case['transactions']}
        first = payments['PR-FUEL-01-BK']
        second = payments['PR-FUEL-02-BK']
        self.assertEqual(set(package['payment_refs']), {first['id'], second['id']})
        self.assertEqual(package['event_date'], first['date'])
        self.assertEqual(package['amount_cents'], -first['amount_cents'])
        comparison = package['comparison_payment']
        self.assertEqual(comparison['id'], second['id'])
        self.assertEqual(comparison['event_date'], second['date'])
        self.assertEqual(comparison['amount_cents'], -second['amount_cents'])
        self.assertNotEqual(package['amount_cents'], -(first['amount_cents'] + second['amount_cents']))
        self.assertEqual(first['counterparty'], second['counterparty'])
        event = date.fromisoformat(first['date'])
        petition = date.fromisoformat(case['procedure']['petition_on'])
        self.assertEqual((petition - event).days, 21)
        documents = {doc['id']: doc for doc in package['documents']}
        self.assertEqual((event - date.fromisoformat(documents['PR-ZK-03']['date'])).days, 16)
        self.assertLess(date.fromisoformat(documents['PR-ZK-04']['date']), event)
        self.assertEqual(documents['PR-ZK-09']['date'], second['date'])

    def test_vorlagen_sind_ausfuellbar_und_formatiert(self):
        required_roles = ('[Name des Insolvenzantragstellers]', '[Name des Insolvenzverwalters]')
        for filename in TEMPLATE_MAP:
            with self.subTest(template=filename):
                path = PLUGIN / 'vorlagen' / filename
                document = Document(path)
                text = docx_text(document)
                normal = document.styles['Normal']
                self.assertEqual(normal.font.name, 'Times New Roman')
                self.assertEqual(normal.font.size.pt, 11)
                placeholders = set(re.findall(r'\[[^\]\n]{2,160}\]', text))
                self.assertGreaterEqual(len(placeholders), 20)
                self.assertNotIn('Insolvenzanderkonto', text)
                self.assertNotIn('[Kontoinhaber Insolvenzanderkonto]', text)
                for role in required_roles:
                    self.assertIn(role, text)
                for paragraph in document.paragraphs:
                    if paragraph.style.name.startswith('Heading'):
                        self.assertRegex(paragraph.text, r'^\d+(?:\.\d+)*[.)]?\s', paragraph.text)
                self.assertNotRegex(text, r'(?m)^\s*(?:[IVX]+|[A-Z]|[a-z])\)\s')
                # Die Vorlagen bestehen überwiegend aus ausformulierten Absätzen,
                # nicht nur aus Feldnamen und Rechtsgrundlagenüberschriften.
                sentences = [p.text for p in document.paragraphs if len(p.text) > 120 and re.search(r'[.!?]$', p.text)]
                self.assertGreaterEqual(len(sentences), 15)

    def test_vorlagen_ausserhalb_grundakte_und_identische_kopien(self):
        selection = json.loads(SELECTION_FILE.read_text(encoding='utf-8'))
        for case in CASES:
            directory = ROOT / 'testakten' / case['slug']
            with self.subTest(case=case['slug']):
                pairs = working_dump_archive_pairs(directory, include_gesamt_pdf=False)
                names = {name for _, name in pairs}
                for source_name, relative in TEMPLATE_MAP.items():
                    self.assertIn(relative, names)
                    self.assertNotIn(relative, selection[case['slug']])
                    self.assertNotIn('Grundakte/' + relative, names)
                    self.assertEqual(hashlib.sha256((directory / relative).read_bytes()).hexdigest(),
                                     hashlib.sha256((PLUGIN / 'vorlagen' / source_name).read_bytes()).hexdigest(),
                                     f'Veraltete Vorlagenkopie: {case["slug"]}/{relative}')
                intake_names = {name for name in names if name.startswith('Grundakte/')}
                self.assertTrue(any('/09_Zahlungskomplex/' in name for name in intake_names))
                self.assertFalse(any('/20_Vorlagen/' in name or '/10_Verfahren/' in name
                                     or 'gesamt.pdf' in name or 'Nachbesprechung' in name
                                     for name in intake_names))

    def test_vorlagenausnahme_bleibt_eng_und_sperrt_musterloesungen(self):
        content = (PLUGIN / 'vorlagen/01_Anfechtungsschreiben.docx').read_bytes()
        with tempfile.TemporaryDirectory(prefix='insolvenzreife-exportfilter-') as temporary:
            base = Path(temporary)
            for case in CASES:
                case_dir = base / case['slug']
                permitted = case_dir / '20_Vorlagen/01_Anfechtungsschreiben.docx'
                permitted.parent.mkdir(parents=True)
                permitted.write_bytes(content)
                self.assertTrue(include_in_working_dump(permitted, case_dir))
                for relative in ('20_Vorlagen/03_Anfechtungsschreiben.docx',
                                 'Grundakte/20_Vorlagen/01_Anfechtungsschreiben.docx'):
                    excluded = case_dir / relative
                    excluded.parent.mkdir(parents=True, exist_ok=True)
                    excluded.write_bytes(content)
                    self.assertFalse(include_in_working_dump(excluded, case_dir), relative)
            other_case = base / 'andere-testakte'
            other_path = other_case / '20_Vorlagen/01_Anfechtungsschreiben.docx'
            other_path.parent.mkdir(parents=True)
            other_path.write_bytes(content)
            self.assertFalse(include_in_working_dump(other_path, other_case))
            # Auch an einem freigegebenen Pfad erlaubt die Ausnahme nur die
            # Variablenfelder; sie darf den Lösungsfilter nicht abschalten.
            case_dir = base / 'kontaminierte-kopie' / CASES[0]['slug']
            path = case_dir / '20_Vorlagen/01_Anfechtungsschreiben.docx'
            path.parent.mkdir(parents=True)
            document = Document(PLUGIN / 'vorlagen/01_Anfechtungsschreiben.docx')
            document.paragraphs[0].insert_paragraph_before('Musterlösung: Hier stehen die fertig ausgefüllten Ansprüche.')
            document.save(path)
            self.assertFalse(include_in_working_dump(path, case_dir))

    def test_erzeugte_bankzuordnung_enthaelt_nur_originalbuchungen(self):
        configs = json.loads((ROOT / 'scripts/data/insolvenzreife-anfechtungskomplexe.json').read_text(encoding='utf-8'))['cases']
        for case in CASES:
            prefix = case['prefix']
            with self.subTest(case=case['slug']):
                directory = ROOT / 'testakten' / case['slug'] / '09_Zahlungskomplex'
                rows = read_csv(directory / f'{prefix}-ZK-11_Bankzuordnung.csv')
                config = configs[prefix]
                expected_ids = set(config['payment_refs'])
                if config.get('comparison_payment'):
                    expected_ids.add(config['comparison_payment']['id'])
                self.assertEqual({row['id'] for row in rows}, expected_ids)
                self.assertEqual(len(rows), len(expected_ids))
                bank = {row['id']: row for row in case['transactions']}
                for row in rows:
                    for key, value in bank[row['id']].items():
                        self.assertEqual(row[key], str(value), (row['id'], key))
                if prefix == 'BZ':
                    self.assertEqual(len(rows), 1)
                    self.assertGreater(int(rows[0]['amount_cents']), 0)
                    self.assertNotEqual(int(rows[0]['amount_cents']), config['amount_cents'])
                else:
                    self.assertTrue(all(int(row['amount_cents']) < 0 for row in rows))

    def test_belegregister_und_tatsaechliche_belege_stimmen_ueberein(self):
        configs = json.loads((ROOT / 'scripts/data/insolvenzreife-anfechtungskomplexe.json').read_text(encoding='utf-8'))['cases']
        for case in CASES:
            prefix = case['prefix']
            with self.subTest(case=case['slug']):
                directory = ROOT / 'testakten' / case['slug'] / '09_Zahlungskomplex'
                records = read_csv(directory / f'{prefix}-ZK-12_Belegregister.csv')
                originals = {doc['id']: doc for doc in configs[prefix]['documents']}
                self.assertEqual({row['Beleg'] for row in records}, set(originals))
                self.assertEqual(len(records), len(originals))
                for row in records:
                    original = originals[row['Beleg']]
                    path = directory / row['Datei']
                    self.assertTrue(path.is_file(), path.name)
                    self.assertEqual(path.stem, row['Beleg'])
                    self.assertEqual(row['Datum'], original['date'])
                    self.assertEqual(row['Aussteller'], original['issuer'])
                    self.assertEqual(row['Empfaenger'], original['recipient'])
                    if path.suffix == '.pdf':
                        reader = PdfReader(path)
                        text = '\n'.join(page.extract_text() for page in reader.pages)
                        self.assertIn(row['Beleg'], text)
                        self.assertIn(date.fromisoformat(row['Datum']).strftime('%d.%m.%Y'), text)
                        self.assertNotIn(NOTICE_BYTES.decode('utf-8').splitlines()[0], text)
                    elif path.suffix == '.docx':
                        document = Document(path)
                        text = docx_text(document)
                        self.assertIn(row['Beleg'], text)
                        self.assertIn(date.fromisoformat(row['Datum']).strftime('%d.%m.%Y'), text)
                    else:
                        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                        self.assertEqual(message['Subject'], row['Betreff'])

    def test_berichtigte_cottbuser_rechnung_zeigt_nur_einmal_umsatzsteuer(self):
        directory = ROOT / 'testakten' / BY_PREFIX['CB']['slug'] / '09_Zahlungskomplex'
        reader = PdfReader(directory / 'CB-ZK-05.pdf')
        text = '\n'.join(page.extract_text() for page in reader.pages)
        # Eigenständige Nachrechnung aus Brutto-Kaufpreis, Materialpreis und Zins.
        original_gross, capital_gross, material_gross, interest = map(Decimal, ('176800', '160000', '12000', '4800'))
        round_cent = lambda number: number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        original_net = round_cent(original_gross / Decimal('1.19'))
        original_tax = original_gross - original_net
        capital_net = round_cent(capital_gross / Decimal('1.19'))
        material_net = round_cent(material_gross / Decimal('1.19'))
        corrected_net = capital_net + material_net
        corrected_tax = (capital_gross - capital_net) + (material_gross - material_net)
        self.assertEqual(corrected_net + corrected_tax + interest, original_gross)
        for value in (original_net, original_tax, capital_net, capital_gross - capital_net,
                      material_net, material_gross - material_net, corrected_net, corrected_tax,
                      original_tax - corrected_tax, interest):
            formatted = f'{value:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
            self.assertIn(formatted, text, formatted)
        # Die Korrektur muss auf die datierte vorhandene Rechnung zurückführen.
        obligation = next(row for row in BY_PREFIX['CB']['obligations'] if row['id'] == 'CB-CAPEX-01')
        self.assertEqual(obligation['arose_on'], '2025-12-18')
        self.assertIn('18. Dezember 2025', text)
        self.assertIn('CB-CAPEX-01', text)

    def test_zahlungskomplex_mailanhaenge_sind_originale(self):
        for case in CASES:
            directory = ROOT / 'testakten' / case['slug'] / '09_Zahlungskomplex'
            with self.subTest(case=case['slug']):
                paths = list(directory.glob('*'))
                self.assertGreaterEqual(len(paths), 8)
                mail_paths = list(directory.glob('*.eml'))
                self.assertGreaterEqual(len(mail_paths), 1)
                attachments = 0
                for path in mail_paths:
                    message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                    self.assertFalse(message.defects, path.name)
                    for header in ('From', 'To', 'Subject', 'Date'):
                        self.assertIsNotNone(message[header], (path.name, header))
                    for part in message.iter_attachments():
                        payload = part.get_payload(decode=True)
                        self.assertTrue(payload)
                        candidates = list((ROOT / 'testakten' / case['slug']).rglob(part.get_filename()))
                        self.assertTrue(candidates, part.get_filename())
                        self.assertTrue(any(candidate.read_bytes() == payload for candidate in candidates), path.name)
                        attachments += 1
                self.assertGreaterEqual(attachments, 1)

    def test_veroeffentlichung_enthaelt_grundakten_und_vorlagen_getrennt(self):
        if DIST is None:
            self.skipTest('Releasebestand mit --dist zusätzlich prüfen')
        with ZipFile(DIST / 'Insolvenzreife_Drei_Grundakten.zip') as intake_archive:
            self.assertEqual(intake_archive.read(NOTICE_FILENAME), NOTICE_BYTES)
            for case in CASES:
                slug = case['slug']
                directory = ROOT / 'testakten' / slug
                expected_pairs = working_dump_archive_pairs(directory, include_gesamt_pdf=False)
                with ZipFile(DIST / f'testakte-{slug}.zip') as archive:
                    self.assertIsNone(archive.testzip())
                    self.assertEqual(archive.read(NOTICE_FILENAME), NOTICE_BYTES)
                    self.assertEqual(set(archive.namelist()), {NOTICE_FILENAME, *(name for _, name in expected_pairs)})
                    for source, name in expected_pairs:
                        self.assertEqual(archive.read(name), source.read_bytes(), name)
                        if name.startswith('Grundakte/'):
                            self.assertEqual(intake_archive.read(f'{slug}/{name}'), source.read_bytes(), name)
                        else:
                            self.assertNotIn(f'{slug}/{name}', intake_archive.namelist())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--dist', type=Path)
    arguments, remaining = parser.parse_known_args()
    DIST = arguments.dist
    unittest.main(argv=[sys.argv[0], *remaining])
