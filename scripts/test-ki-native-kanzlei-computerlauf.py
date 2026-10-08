#!/usr/bin/env python3
"""Fehler- und Durchlauftests des Computerlauf-Prototyps; niemals echte Konten öffnen."""
import copy
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'ki-native-kanzlei/scripts/computerlauf.py'
spec = importlib.util.spec_from_file_location('computerlauf', SCRIPT)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


class ComputerlaufTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.mandate = self.root / 'M-1'
        self.mandate.mkdir()
        for name, content in {'betreff.txt': 'Bitte um Durchsicht', 'text.txt': 'Sehr geehrte Frau Fenchel, anbei der Entwurf.', 'anlage.pdf': 'Fiktive Anlage', 'zustimmung.txt': 'Fiktive dokumentierte Bestätigung von Ada Ahrens.', 'beleg.txt': 'Fiktiver Providerbeleg', 'route.txt': 'Fiktive einzeln geprüfte Versandroute'}.items():
            (self.mandate / name).write_text(content, encoding='utf-8')
        self.session = {'session_id': 'S-1', 'mode': 'live', 'level': 3, 'person': 'Ada Ahrens', 'expires': (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat(), 'permissions_confirmed': True, 'mandates': {'M-1': 'M-1'}, 'apps': [{'app': 'outlook', 'account': 'kanzlei@example.test', 'actions': ['send', 'read', 'export'], 'transport_domains': ['outlook.example.test'], 'recipient_domains': ['mandant.example.test']}, {'app': 'bea', 'account': 'bea:TEST-SAFE-AHRENS', 'actions': ['send', 'read', 'export', 'eeb'], 'transport_domains': ['bea.example.test'], 'recipient_domains': []}]}
        self.plan = {'action_id': 'A-1', 'app': 'outlook', 'account': 'kanzlei@example.test', 'mandat': 'M-1', 'kind': 'send', 'to': ['mara@mandant.example.test'], 'cc': [], 'bcc': [], 'subject_file': 'betreff.txt', 'body_file': 'text.txt', 'attachments': ['anlage.pdf'], 'transport_domains': ['outlook.example.test'], 'source_ids': [], 'legal_route': 'not_applicable', 'legal_route_confirmed': False, 'legal_route_evidence': None, 'personal_actor': None}
        self.call('init', self.session)

    def tearDown(self):
        self.temp.cleanup()

    def call(self, operation, value=None, code=0):
        argv = ['--root', str(self.root), operation]
        if value is not None:
            path = self.root / 'eingabe.json'
            path.write_text(json.dumps(value), encoding='utf-8')
            argv += ['--input', str(path)]
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            actual = M.main(argv)
        self.assertEqual(actual, code, (operation, out.getvalue(), err.getvalue()))
        return json.loads(out.getvalue()) if actual == 0 else err.getvalue()

    def state(self):
        return json.loads((self.root / '.computerlauf/lauf.json').read_text())

    def prepared(self, plan=None):
        plan = plan or self.plan
        self.call('plan', plan)
        action = self.call('freeze', {'action_id': plan['action_id']})
        self.call('approve', {'action_id': plan['action_id'], 'person': 'Ada Ahrens', 'manifest_sha256': action['manifest_sha256'], 'confirmation_received': True, 'evidence_file': 'zustimmung.txt'})
        return {'action_id': plan['action_id'], 'manifest_sha256': action['manifest_sha256']}

    def result(self, status='ausgefuehrt', who='Ada Ahrens'):
        return {'action_id': self.plan['action_id'], 'status': status, 'person': who, 'evidence_file': 'beleg.txt', 'provider_id': 'FIKTIV-4711', 'provider_id_absent_reason': None, 'no_effect_confirmed': status == 'fehlgeschlagen', 'note': 'Nur ein Testbefund; kein tatsächlicher Versand.'}

    def reconciliation(self, outcome='nicht_ausgefuehrt'):
        return {'action_id': self.plan['action_id'], 'person': 'Ada Ahrens', 'outcome': outcome, 'evidence_file': 'beleg.txt', 'provider_id': 'FIKTIV-4711', 'provider_id_absent_reason': None, 'note': 'Ausgang, Providerprotokoll und Gegenseite in der Simulation abgeglichen.'}

    def bea(self, personal=True):
        self.plan.update(app='bea', account='bea:TEST-SAFE-AHRENS', to=['bea:TEST-SAFE-ID'], transport_domains=['bea.example.test'], legal_route='personal_owner_required' if personal else 'qes_verified', legal_route_confirmed=True, legal_route_evidence='route.txt', personal_actor='Ada Ahrens' if personal else None)

    def test_full_flow_separates_execution_and_receipt_and_preserves_sources(self):
        originals = {p.name: p.read_bytes() for p in self.mandate.iterdir()}
        start = self.prepared()
        action = self.call('start', start)
        self.assertEqual(action['status'], 'gestartet')
        self.assertEqual(len(action['attempts']), 1)
        self.assertTrue((self.root / '.computerlauf/A-1.1.attempt').is_file())
        action = self.call('result', self.result())
        self.assertEqual(action['receipts'], [])
        receipt = self.reconciliation()
        del receipt['outcome']
        receipt['receipt_status'] = 'bestaetigt'
        action = self.call('receipt', receipt)
        self.assertEqual(action['status'], 'ausgefuehrt')
        self.assertEqual(action['receipts'][0]['receipt_status'], 'bestaetigt')
        self.assertEqual(originals, {p.name: p.read_bytes() for p in self.mandate.iterdir()})
        self.call('start', start, code=2)

    def test_approval_requires_actual_confirmation_exact_hash_and_named_human(self):
        self.call('plan', self.plan)
        action = self.call('freeze', {'action_id': 'A-1'})
        good = {'action_id': 'A-1', 'person': 'Ada Ahrens', 'manifest_sha256': action['manifest_sha256'], 'confirmation_received': True, 'evidence_file': 'zustimmung.txt'}
        for field, value in [('confirmation_received', False), ('manifest_sha256', '0' * 64), ('person', 'Codex Agent'), ('person', 'Freigabe'), ('evidence_file', 'fehlt.txt')]:
            bad = dict(good, **{field: value})
            self.call('approve', bad, code=2)
        self.assertEqual(self.state()['actions']['A-1']['status'], 'gefroren')

    def test_unapproved_start_and_changed_hash_are_rejected(self):
        self.call('plan', self.plan)
        frozen = self.call('freeze', {'action_id': 'A-1'})
        self.call('start', {'action_id': 'A-1', 'manifest_sha256': frozen['manifest_sha256']}, code=2)

    def test_each_source_change_invalidates_existing_approval(self):
        for filename in ('text.txt', 'betreff.txt', 'anlage.pdf'):
            with self.subTest(filename=filename):
                if self.state()['actions']:
                    self.tearDown(); self.setUp()
                start = self.prepared()
                (self.mandate / filename).write_text('Veränderte Fassung', encoding='utf-8')
                self.assertIn('verändert', self.call('start', start, code=2))
                self.assertEqual(self.state()['actions']['A-1']['attempts'], [])

    def test_changed_approval_evidence_is_rejected(self):
        start = self.prepared()
        (self.mandate / 'zustimmung.txt').write_text('Widerruf', encoding='utf-8')
        self.assertIn('Freigabebeleg', self.call('start', start, code=2))

    def test_bcc_is_frozen_and_recipient_domain_enforced(self):
        self.plan['bcc'] = ['archiv@fremd.example.test']
        self.call('plan', self.plan, code=2)
        self.plan['bcc'] = ['archiv@mandant.example.test']
        start = self.prepared()
        before = self.state()['actions']['A-1']['manifest']['plan']['bcc']
        self.assertEqual(before, ['archiv@mandant.example.test'])
        state = self.state()
        state['actions']['A-1']['plan']['bcc'] = []
        (self.root / '.computerlauf/lauf.json').write_text(json.dumps(state))
        self.call('start', start, code=2)

    def test_scope_rejects_other_accounts_apps_domains_and_mandates(self):
        for key, value in [('app', 'gmail'), ('account', 'anderes@example.test'), ('mandat', 'M-2'), ('transport_domains', ['boese.example.test'])]:
            self.call('plan', dict(self.plan, **{key: value}), code=2)
        self.assertEqual(self.state()['actions'], {})

    def test_path_traversal_absolute_path_and_symlink_are_rejected(self):
        outside = self.root / 'ausserhalb.txt'
        outside.write_text('Nicht Teil des Mandats')
        (self.mandate / 'link.txt').symlink_to(outside)
        for path in ('../ausserhalb.txt', str(outside), 'link.txt'):
            self.call('plan', dict(self.plan, attachments=[path]), code=2)
        self.assertEqual(outside.read_text(), 'Nicht Teil des Mandats')

    def test_secret_fields_are_rejected_in_every_mutating_input_shape(self):
        for secret in ('pin', 'software_token', 'password'):
            self.call('plan', dict(self.plan, **{secret: 'NICHT-ECHT'}), code=2)
        self.call('stop', {'person': 'Ada Ahrens', 'reason': 'Test', 'pin': 'NICHT-ECHT'}, code=2)
        self.assertNotIn('NICHT-ECHT', (self.root / '.computerlauf/lauf.json').read_text())

    def test_simulation_cannot_start_real_action(self):
        state = self.state(); state['session']['mode'] = 'simulation'
        (self.root / '.computerlauf/lauf.json').write_text(json.dumps(state))
        start = self.prepared()
        self.assertIn('Simulation', self.call('start', start, code=2))
        self.assertFalse(list((self.root / '.computerlauf').glob('*.attempt')))

    def test_level_two_cannot_send_but_can_read_exact_message(self):
        state = self.state(); state['session']['level'] = 2
        (self.root / '.computerlauf/lauf.json').write_text(json.dumps(state))
        self.call('start', self.prepared(), code=2)
        read = dict(self.plan, action_id='A-2', kind='read', to=[], subject_file=None, body_file=None, attachments=[], source_ids=['EINGANG-123'])
        self.call('start', self.prepared(read))

    def test_read_requires_selected_source_ids_and_cannot_smuggle_send_fields(self):
        bad = dict(self.plan, kind='read', source_ids=['EINGANG-123'])
        self.call('plan', bad, code=2)
        bad.update(to=[], subject_file=None, body_file=None, attachments=[], source_ids=[])
        self.call('plan', bad, code=2)

    def test_expired_and_stopped_session_cannot_start_but_result_can_be_recorded(self):
        start = self.prepared()
        self.call('start', start)
        self.call('stop', {'person': 'Ada Ahrens', 'reason': 'Computersteuerung angehalten'})
        self.call('plan', dict(self.plan, action_id='A-2'), code=2)
        self.call('result', self.result())
        self.call('start', start, code=2)

    def test_expiry_is_checked_at_start(self):
        start = self.prepared()
        state = self.state()
        state['session']['expires'] = '2020-01-01T00:00:00+00:00'
        (self.root / '.computerlauf/lauf.json').write_text(json.dumps(state))
        self.assertIn('abgelaufen', self.call('start', start, code=2))

    def test_unknown_attempt_blocks_retry_and_new_equivalent_action(self):
        start = self.prepared()
        self.call('start', start)
        self.call('result', self.result('unklar'))
        self.call('start', start, code=2)
        second = self.prepared(dict(self.plan, action_id='A-2'))
        self.assertIn('Gleicher Inhalt', self.call('start', second, code=2))
        self.call('reconcile', self.reconciliation())
        self.call('start', start, code=2)
        action = self.state()['actions']['A-1']
        self.call('approve', {'action_id': 'A-1', 'person': 'Ada Ahrens', 'manifest_sha256': action['manifest_sha256'], 'confirmation_received': True, 'evidence_file': 'zustimmung.txt'})
        action = self.call('start', start)
        self.assertEqual(len(action['attempts']), 2)
        self.assertEqual(action['attempts'][0]['result']['status'], 'unklar')

    def test_failed_transport_is_not_automatically_safe_to_retry(self):
        start = self.prepared(); self.call('start', start)
        result = self.result('fehlgeschlagen'); result['no_effect_confirmed'] = False
        self.call('result', result, code=2)
        self.call('result', self.result('fehlgeschlagen'))
        self.call('start', start, code=2)
        self.call('reconcile', self.reconciliation())
        self.assertEqual(self.state()['actions']['A-1']['status'], 'gefroren')

    def test_missing_provider_id_requires_honest_explanation(self):
        self.call('start', self.prepared())
        result = self.result(); result['provider_id'] = None
        self.call('result', result, code=2)
        result['provider_id_absent_reason'] = 'Testoberfläche stellt keine Kennung bereit.'
        self.call('result', result)

    def test_reconciled_execution_and_negative_receipt_never_enable_resend(self):
        start = self.prepared(); self.call('start', start)
        self.call('result', self.result('unklar'))
        self.call('reconcile', self.reconciliation('ausgefuehrt'))
        receipt = self.reconciliation(); del receipt['outcome']; receipt['receipt_status'] = 'abgelehnt'
        self.call('receipt', receipt)
        self.call('start', start, code=2)
        self.call('reconcile', self.reconciliation(), code=2)

    def test_personal_bea_route_waits_for_named_human(self):
        self.bea()
        action = self.call('start', self.prepared())
        self.assertEqual(action['status'], 'wartet_auf_mensch')
        self.assertEqual(action['execution_actor'], 'Ada Ahrens')
        self.call('result', self.result(who='Bertram Brecht'), code=2)
        self.call('result', self.result())

    def test_bea_route_evidence_change_and_missing_check_are_rejected(self):
        self.bea(False)
        self.plan['legal_route_confirmed'] = False
        self.call('plan', self.plan, code=2)
        self.plan['legal_route_confirmed'] = True
        start = self.prepared()
        (self.mandate / 'route.txt').write_text('Route nicht geklärt', encoding='utf-8')
        self.call('start', start, code=2)

    def test_eeb_always_requires_personal_route_in_this_prototype(self):
        self.bea(False); self.plan['kind'] = 'eeb'
        self.call('plan', self.plan, code=2)
        self.bea(True)
        self.assertEqual(self.call('start', self.prepared())['status'], 'wartet_auf_mensch')

    def test_duplicate_ids_and_completed_duplicate_content_are_blocked(self):
        start = self.prepared()
        self.call('plan', self.plan, code=2)
        self.call('start', start); self.call('result', self.result())
        second = self.prepared(dict(self.plan, action_id='A-2'))
        self.call('start', second, code=2)

    def test_init_does_not_erase_existing_or_unresolved_state(self):
        self.call('init', dict(self.session, session_id='S-2'), code=2)
        self.call('start', self.prepared())
        self.call('stop', {'person': 'Ada Ahrens', 'reason': 'Test'})
        self.call('init', dict(self.session, session_id='S-2'), code=2)
        self.call('result', self.result())
        self.call('init', dict(self.session, session_id='S-2'))
        self.assertIn('A-1', self.state()['actions'])
        self.assertEqual(len(self.state()['previous_sessions']), 1)

    def test_session_input_rejects_permissions_missing_timezone_boolean_level_and_wildcards(self):
        self.call('stop', {'person': 'Ada Ahrens', 'reason': 'Test'})
        for change in ({'permissions_confirmed': False}, {'expires': '2099-01-01T12:00:00'}, {'level': True}):
            self.call('init', dict(self.session, session_id='S-2', **change), code=2)
        bad = copy.deepcopy(self.session); bad['session_id'] = 'S-2'; bad['apps'][0]['transport_domains'] = ['*.example.test']
        self.call('init', bad, code=2)

    def test_journal_lock_prevents_parallel_write_and_is_not_broken(self):
        lock = self.root / '.computerlauf/lock'; lock.write_text('123\n')
        self.assertIn('gesperrt', self.call('plan', self.plan, code=2))
        self.assertTrue(lock.exists())
        lock.unlink()

    def test_parallel_start_records_only_one_attempt(self):
        start = self.prepared()
        path = self.root / 'start.json'; path.write_text(json.dumps(start))
        args = [sys.executable, str(SCRIPT), '--root', str(self.root), 'start', '--input', str(path)]
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: subprocess.run(args, text=True, capture_output=True), range(2)))
        self.assertEqual(sorted(result.returncode for result in results), [0, 2])
        self.assertEqual(len(self.state()['actions']['A-1']['attempts']), 1)

    def test_crash_reservation_cannot_silently_retry_and_can_be_reconciled(self):
        start = self.prepared()
        guard = self.root / '.computerlauf/A-1.1.attempt'
        guard.write_text('{"simulation": "reservation before interrupted state write"}')
        self.assertIn('reserviert', self.call('start', start, code=2))
        self.call('reconcile', self.reconciliation())
        action = self.state()['actions']['A-1']
        self.assertTrue(action['attempts'][0]['recovered_reservation'])
        self.assertEqual(action['status'], 'gefroren')
        self.assertTrue(guard.exists())

    def test_crash_reservation_prevents_starting_new_session(self):
        self.prepared()
        (self.root / '.computerlauf/A-1.1.attempt').write_text('reserviert')
        self.call('stop', {'person': 'Ada Ahrens', 'reason': 'Test'})
        self.call('init', dict(self.session, session_id='S-2'), code=2)

    def test_crash_reservation_blocks_different_action_id(self):
        self.prepared()
        (self.root / '.computerlauf/A-1.1.attempt').write_text('reserviert')
        second = self.prepared(dict(self.plan, action_id='A-2'))
        self.call('start', second, code=2)

    def test_reordered_recipients_and_attachments_do_not_allow_duplicate_send(self):
        (self.mandate / 'anlage2.pdf').write_text('Noch eine fiktive Anlage')
        self.plan['to'].append('emil@mandant.example.test')
        self.plan['attachments'].append('anlage2.pdf')
        self.call('start', self.prepared())
        self.call('result', self.result())
        reordered = dict(self.plan, action_id='A-2', to=list(reversed(self.plan['to'])), attachments=list(reversed(self.plan['attachments'])))
        self.call('start', self.prepared(reordered), code=2)

    def test_eeb_cannot_use_mail_app_to_bypass_personal_route(self):
        state = self.state(); state['session']['apps'][0]['actions'].append('eeb')
        (self.root / '.computerlauf/lauf.json').write_text(json.dumps(state))
        self.call('plan', dict(self.plan, kind='eeb'), code=2)

    def test_changed_internal_route_note_does_not_make_a_new_message(self):
        self.bea(False)
        self.call('start', self.prepared()); self.call('result', self.result())
        (self.mandate / 'route2.txt').write_text('Andere interne Bewertung derselben Nachricht')
        duplicate = dict(self.plan, action_id='A-2', legal_route_evidence='route2.txt')
        self.call('start', self.prepared(duplicate), code=2)

    def test_receipt_after_new_session_uses_original_mandate_directory(self):
        self.call('start', self.prepared()); self.call('result', self.result())
        self.call('stop', {'person': 'Ada Ahrens', 'reason': 'Neue Sitzung'})
        (self.root / 'M-1-neu').mkdir()
        self.call('init', dict(self.session, session_id='S-2', mandates={'M-1': 'M-1-neu'}))
        receipt = self.reconciliation(); del receipt['outcome']; receipt['receipt_status'] = 'bestaetigt'
        self.call('receipt', receipt)

    def test_corrupt_journal_is_not_overwritten(self):
        path = self.root / '.computerlauf/lauf.json'
        path.write_text('[]')
        self.call('status', code=2)
        self.assertEqual(path.read_text(), '[]')

    def test_receipt_before_execution_and_machine_result_are_rejected(self):
        self.call('start', self.prepared())
        receipt = self.reconciliation(); del receipt['outcome']; receipt['receipt_status'] = 'bestaetigt'
        self.call('receipt', receipt, code=2)
        self.call('result', self.result(who='Codex System'), code=2)


if __name__ == '__main__':
    unittest.main()
