#!/usr/bin/env python3
"""Verhaltenstests für Honorare, offene Zeiten, Korrekturen und Nebenläufigkeit."""
import importlib.util
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('si_journal', ROOT/'ki-native-kanzlei/scripts/kanzlei.py')
J = importlib.util.module_from_spec(spec); spec.loader.exec_module(J)


class JournalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.folder, self.db = J.connect(self.tmp.name, True); self.addCleanup(self.db.close)
        J.init(self.db, {'matter_id':'T-01', 'client':'Testmandantin', 'subject':'Vertragsprüfung'})

    def terms(self, model='hourly', **kw):
        data = dict(id='HV-1', model=model, scope='Außergerichtliche Prüfung', agreement_ref='Auftrag 01', confirmed=True, rate_eur='240.00', vat_rate=19, cap_eur='200.00', cap_scope='fees_only', estimate_eur='200.00', flat_eur='500.00')
        data.update(kw); J.add_terms(self.db, data); return data

    def time(self, **kw):
        data = dict(id='Z-1', terms_id='HV-1', work_date='2026-10-07', person='Frieda', minutes=75, narrative='Vertragsklauseln geprüft', billable=True, confirmed=True, source='Bestätigung der Anwältin')
        data.update(kw); return J.add_entry(self.db, 'time', data)

    def snap(self):
        return J.snapshot(self.db)

    def test_hourly_amount_and_idempotency(self):
        self.terms(); self.time(); revision=self.snap()['journal_revision']; self.time()
        self.assertEqual(self.snap()['known_gross_eur'], '357.00')
        self.assertEqual(self.snap()['journal_revision'], revision)

    def test_missing_is_not_zero(self):
        self.terms(); self.time(minutes=None, confirmed=False)
        self.assertFalse(self.snap()['complete']); self.assertEqual(self.snap()['phases'][0]['minutes'], 0)
        with self.assertRaises(ValueError): self.time(id='Z-2', minutes=None)

    def test_omitted_pending_fields_export_as_unknown_and_are_idempotent(self):
        self.terms()
        pending = dict(id='Z-pending', terms_id='HV-1', work_date='2026-10-07',
                       person='Frieda', narrative='Dauer des Telefonats erfragen',
                       confirmed=False, source='Noch unvollständige Notiz')
        J.add_entry(self.db, 'time', pending)
        first = self.snap()
        self.assertFalse(first['complete'])
        self.assertIsNone(first['entries'][0]['data']['minutes'])
        self.assertIsNone(first['entries'][0]['data']['billable'])
        J.export(self.folder, first)
        explicit = dict(pending, minutes=None, billable=None)
        J.add_entry(self.db, 'time', explicit)
        self.assertEqual(self.snap()['journal_revision'], first['journal_revision'])
        self.assertIn('Z-pending;HV-1;2026-10-07;Frieda;;',
                      (self.folder/'02_Honorar/zeiten.csv').read_text())
        with self.assertRaises(ValueError):
            J.add_entry(self.db, 'time', dict(pending, id='Z-invalid', confirmed=True))

    def test_true_zero_and_nonbillable_are_valid(self):
        self.terms(); self.time(minutes=0); self.time(id='Z-2', billable=False)
        self.assertTrue(self.snap()['complete']); self.assertEqual(self.snap()['known_net_eur'], '0.00')

    def test_cap_and_estimate_differ(self):
        self.terms('capped'); self.time()
        self.assertEqual(self.snap()['known_net_eur'], '200.00')
        self.terms('estimate', id='HV-2'); self.time(id='Z-2', terms_id='HV-2')
        self.assertEqual(self.snap()['phases'][1]['net_eur'], '300.00')
        self.assertTrue(any('Schätzung überschritten' in s for s in self.snap()['notices']))

    def test_cap_includes_expenses_only_when_agreed(self):
        self.terms('capped', cap_scope='fees_and_expenses'); self.time()
        J.add_entry(self.db,'expense',dict(id='A-1',terms_id='HV-1',date='2026-10-07',net_eur='100.00',description='Eigene steuerpflichtige Nebenleistung',source='Beleg',confirmed=True,tax_classification='own_taxable'))
        self.assertEqual(self.snap()['known_net_eur'], '200.00')

    def test_expenses_above_shared_cap_remain_visible_without_time(self):
        self.terms('capped', cap_scope='fees_and_expenses', cap_eur='100.00')
        J.add_entry(self.db, 'expense', dict(id='A-1', terms_id='HV-1', date='2026-10-07',
                    net_eur='150.00', description='Eigene steuerpflichtige Nebenleistung',
                    source='Beleg', confirmed=True, tax_classification='own_taxable'))
        view = self.snap(); phase = view['phases'][0]
        self.assertEqual(view['known_net_eur'], '100.00')
        self.assertEqual(phase['expenses_value_eur'], '150.00')
        self.assertEqual(phase['expenses_eur'], '100.00')
        self.assertEqual(phase['expenses_above_cap_eur'], '50.00')
        self.assertTrue(any('50.00 EUR Auslagenwert' in n for n in view['notices']))
        J.export(self.folder, view)
        output = (self.folder/'02_Honorar/rechnungsentwurf.md').read_text()
        self.assertIn('150.00 EUR', output)
        self.assertIn('50.00 EUR Auslagenwert', output)

    def test_flat_not_hourly_addition(self):
        self.terms('flat'); self.time()
        self.assertEqual(self.snap()['known_net_eur'],'500.00')

    def test_rvg_requires_separate_calculation(self):
        self.terms('rvg'); self.time()
        self.assertFalse(self.snap()['complete']); self.assertEqual(self.snap()['known_net_eur'], '0.00')
        row=dict(id='R-1',terms_id='HV-1',date='2026-10-07',net_eur='100',description='Gesondert geprüfte Gebühr',source='Berechnung',confirmed=True,legal_reviewed=True)
        J.add_entry(self.db,'manual-fee',row)
        self.assertTrue(self.snap()['complete']); self.assertEqual(self.snap()['known_net_eur'], '100.00')

    def test_unconfirmed_terms_dont_bill(self):
        self.terms(confirmed=False); self.time()
        self.assertEqual(self.snap()['known_net_eur'], '0.00'); self.assertFalse(self.snap()['complete'])

    def test_pending_terms_can_be_completed(self):
        data=self.terms(confirmed=False,rate_eur=None); self.time()
        self.assertEqual(self.snap()['known_net_eur'],'0.00')
        data.update(confirmed=True,rate_eur='240.00'); J.add_terms(self.db,data)
        self.assertEqual(self.snap()['known_net_eur'],'300.00')

    def test_time_without_terms_stays_open(self):
        self.time(terms_id=None)
        view=self.snap(); self.assertFalse(view['complete']); self.assertEqual(view['known_net_eur'],'0.00')
        J.export(self.folder,view)

    def test_revision_cannot_reprice_existing_time(self):
        data=self.terms(); self.time(); data['rate_eur']='450'
        with self.assertRaises(ValueError): J.add_terms(self.db,data)
        self.assertEqual(self.snap()['known_net_eur'],'300.00')

    def test_void_preserves_history_and_new_entry(self):
        self.terms(); self.time(); J.void(self.db,'Z-1','Doppelt erfasste Dauer')
        self.time(id='Z-2',minutes=30)
        self.assertEqual(self.snap()['known_net_eur'],'120.00')
        self.assertEqual(len(self.snap()['entries']),2)
        with self.assertRaises(ValueError): self.time()

    def test_invalid_inputs_fail(self):
        self.terms()
        for minutes in (-1, 1500, 'NaN', 'Infinity', 0.5, True):
            with self.subTest(minutes=minutes), self.assertRaises(ValueError): self.time(minutes=minutes)
        with self.assertRaises(ValueError): self.time(work_date='2026-02-30')
        self.time(minutes=1000)
        with self.assertRaises(ValueError): self.time(id='Z-2',minutes=500)

    def test_payment_is_not_automatically_netted(self):
        self.terms(); self.time()
        J.add_entry(self.db,'payment',dict(id='P-1',date='2026-10-07',gross_eur='100',kind='third_party',reference='Fremdgeld ungeklärt',source='Kontoauszug',confirmed=True))
        self.assertEqual(self.snap()['known_gross_eur'],'357.00'); self.assertEqual(len(self.snap()['payments']),1)
        self.assertFalse(self.snap()['invoice_ready'])

    def test_csv_injection_and_regeneration(self):
        self.terms(); self.time(narrative='=HYPERLINK("https://example.invalid")')
        J.export(self.folder,self.snap())
        csv=(self.folder/'02_Honorar/zeiten.csv').read_text()
        self.assertIn("'=HYPERLINK",csv)
        output=self.folder/'02_Honorar/rechnungsentwurf.md'; output.write_text('Abgebrochener Export')
        J.export(self.folder,self.snap()); self.assertIn('357.00',output.read_text())

    def test_different_matter_is_rejected(self):
        with self.assertRaises(ValueError): J.init(self.db,{'matter_id':'T-2','client':'Andere','subject':'Anderes'})


class CommandLineTests(unittest.TestCase):
    def test_concurrent_cli_entries_and_regeneration_preserve_one_journal(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            matter = folder/'Mandat mit Leerzeichen'
            script = ROOT/'ki-native-kanzlei/scripts/kanzlei.py'

            def run(command, data=None, label='input'):
                args = [sys.executable, str(script), command, '--akte', str(matter)]
                if data is not None:
                    source = folder/(label+'.json')
                    source.write_text(json.dumps(data), encoding='utf-8')
                    args += ['--data', str(source)]
                result = subprocess.run(args, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            run('init', dict(matter_id='E2E-1', client='Testmandantin', subject='Vertragsprüfung'))
            run('terms', dict(id='HV-1', model='hourly', scope='Prüfung', agreement_ref='Auftrag',
                             confirmed=True, rate_eur='240.00', vat_rate=19))
            rows = [dict(id=f'Z-{i}', terms_id='HV-1', work_date='2026-10-07', person='Frieda',
                         minutes=1, narrative=f'Bestätigte Tätigkeit {i}', billable=True,
                         confirmed=True, source='Nutzerangabe') for i in range(8)]
            with ThreadPoolExecutor(max_workers=8) as workers:
                list(workers.map(lambda pair: run('time', pair[1], f'time-{pair[0]}'), enumerate(rows)))
            status = run('status')
            self.assertEqual(status['journal_revision'], 10)
            self.assertEqual(status['known_gross_eur'], '38.08')
            stored = json.loads((matter/'02_Honorar/rechnungsentwurf.json').read_text())
            self.assertEqual(stored['journal_revision'], 10)
            self.assertEqual(len(stored['entries']), 8)
            repeated = run('time', rows[0], 'repeat')
            self.assertEqual(repeated['journal_revision'], 10)
            for filename in ('rechnungsentwurf.md', 'rechnungsentwurf.json', 'zeiten.csv'):
                (matter/'02_Honorar'/filename).unlink()
            regenerated = run('draft')
            self.assertEqual(regenerated['journal_revision'], 10)
            rebuilt = json.loads((matter/'02_Honorar/rechnungsentwurf.json').read_text())
            self.assertEqual(rebuilt, stored)
            self.assertEqual(len((matter/'02_Honorar/zeiten.csv').read_text().splitlines()), 9)

if __name__ == '__main__':
    unittest.main()
