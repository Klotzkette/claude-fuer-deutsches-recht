#!/usr/bin/env python3
"""Tests für den Mandatslauf-Helfer der KI-nativen Kanzlei."""
import importlib.util, io, json, sys, tempfile, unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('mandatslauf', ROOT / 'ki-native-kanzlei/scripts/mandatslauf.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)


def run(*argv):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = M.main(list(argv))
    return code, out.getvalue(), err.getvalue()


class LaufTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.akte = self.tmp.name
        self.assertEqual(run('init', '--akte', self.akte, '--matter-id', 'M-26-104', '--stufe', '2')[0], 0)
        (Path(self.akte) / '01_Bearbeitung').mkdir(); (Path(self.akte) / '01_Bearbeitung/Klage_v04.docx').write_bytes(b'entwurf')

    def tearDown(self):
        self.tmp.cleanup()

    def state(self):
        return json.loads((Path(self.akte) / '00_Mandat/mandatslauf.json').read_text())

    def test_init_refuses_overwrite(self):
        code, _, err = run('init', '--akte', self.akte, '--matter-id', 'X', '--stufe', '1')
        self.assertEqual(code, 2); self.assertIn('existiert bereits', err)

    def test_init_rejects_bad_level(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(run('init', '--akte', d, '--matter-id', 'X', '--stufe', '4')[0], 2)

    def test_phase_and_side_run(self):
        self.assertEqual(run('phase', '--akte', self.akte, '--phase', 'sacharbeit', '--grund', 'Klage bestellt')[0], 0)
        self.assertEqual(run('phase', '--akte', self.akte, '--phase', 'frist', '--grund', 'Zustellung', '--nebenlauf')[0], 0)
        s = self.state(); self.assertEqual(s['phase'], 'sacharbeit'); self.assertEqual(s['side_runs'], ['frist']); self.assertEqual(s['revision'], 3)

    def test_unknown_phase(self):
        self.assertEqual(run('phase', '--akte', self.akte, '--phase', 'urlaub', '--grund', 'x')[0], 2)

    def test_product_hash_and_replacement(self):
        self.assertEqual(run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 'schriftsaetze-entwerfen')[0], 0)
        first = self.state()['products']['klage']['sha256']
        (Path(self.akte) / '01_Bearbeitung/Klage_v04.docx').write_bytes(b'fassung 2')
        run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 'schriftsaetze-entwerfen', '--zustand', 'geprueft')
        p = self.state()['products']['klage']; self.assertEqual(p['replaces'], first); self.assertEqual(p['state'], 'geprueft')

    def test_product_requires_file_and_relative_path(self):
        self.assertEqual(run('product', '--akte', self.akte, '--id', 'x', '--pfad', '01_Bearbeitung/fehlt.docx', '--skill', 's')[0], 2)
        self.assertEqual(run('product', '--akte', self.akte, '--id', 'x', '--pfad', '../Klage.docx', '--skill', 's')[0], 2)

    def test_release_requires_review_first(self):
        code, _, err = run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 's', '--zustand', 'freigegeben')
        self.assertEqual(code, 2); self.assertIn('geprüfte Fassung', err)

    def test_gate_needs_named_person(self):
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--bezug', 'Klage_v04.docx')
        for who in ('KI', 'Agent Smith', 'System', 'automatisch', 'Claude'):
            self.assertEqual(run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'freigeben', '--person', who, '--bezug', 'Klage_v04.docx')[0], 2, who)
        self.assertEqual(run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'freigeben', '--person', 'RAin Dr. Ahrens', '--bezug', 'Klage_v04.docx')[0], 0)
        g = self.state()['gates']['G3']; self.assertEqual(g['status'], 'freigegeben'); self.assertEqual(g['by'], 'RAin Dr. Ahrens')

    def test_gate_cannot_be_released_unopened(self):
        self.assertEqual(run('gate', '--akte', self.akte, '--gate', 'G4', '--aktion', 'freigeben', '--person', 'RA Brecht', '--bezug', 'R-1')[0], 2)

    def test_gate_reset_after_release(self):
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--bezug', 'v4')
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'freigeben', '--person', 'RA Brecht', '--bezug', 'v4')
        self.assertEqual(run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--bezug', 'v5')[0], 2)
        self.assertEqual(run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'zuruecksetzen', '--bezug', 'v5', '--notiz', 'neue Fassung')[0], 0)
        self.assertEqual(self.state()['gates']['G3']['reset_from'], 'freigegeben')

    def test_next_prefers_open_deadline_gate(self):
        run('phase', '--akte', self.akte, '--phase', 'sacharbeit', '--grund', 'x')
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--bezug', 'v4')
        run('gate', '--akte', self.akte, '--gate', 'G2', '--aktion', 'oeffnen', '--bezug', 'Vermerk')
        _, out, _ = run('next', '--akte', self.akte); r = json.loads(out)
        self.assertEqual(r['next_skill'], 'fristen-berechnen-ueberwachen'); self.assertFalse(r['external_action_allowed']); self.assertEqual(sorted(r['open_gates']), ['G2', 'G3'])

    def test_next_follows_phase_without_gates(self):
        run('phase', '--akte', self.akte, '--phase', 'abrechnung', '--grund', 'x')
        _, out, _ = run('next', '--akte', self.akte); self.assertEqual(json.loads(out)['next_skill'], 'zeiten-erfassen')

    def test_closing_requires_decided_gates(self):
        self.assertEqual(run('phase', '--akte', self.akte, '--phase', 'abschluss', '--grund', 'Ende')[0], 2)
        for g in ('G4', 'G5', 'G8'):
            run('gate', '--akte', self.akte, '--gate', g, '--aktion', 'nicht-erforderlich', '--notiz', 'kein Anlass')
        self.assertEqual(run('phase', '--akte', self.akte, '--phase', 'abschluss', '--grund', 'Ende')[0], 0)

    def test_questions_and_history(self):
        run('question', '--akte', self.akte, '--text', 'Zugang der Kündigung?')
        self.assertEqual(self.state()['open_questions'], ['Zugang der Kündigung?'])
        run('question', '--akte', self.akte, '--text', 'Zugang der Kündigung?', '--erledigt')
        s = self.state(); self.assertEqual(s['open_questions'], []); self.assertEqual(s['history'][-1]['action'], 'question_closed')

    def test_control_characters_rejected(self):
        self.assertEqual(run('phase', '--akte', self.akte, '--phase', 'akte', '--grund', 'a\x00b')[0], 2)


    def test_open_gate_preserves_named_responsible(self):
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--person', 'RAin Ada Ahrens', '--bezug', 'Brief')
        self.assertEqual(self.state()['gates']['G3'].get('responsible'), 'RAin Ada Ahrens')

    def test_gate_routes_to_registered_product_skill(self):
        run('product', '--akte', self.akte, '--id', 'mandantenbrief', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 'mandantenkommunikation')
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--person', 'RAin Ada Ahrens', '--bezug', 'mandantenbrief')
        code, out, _ = run('next', '--akte', self.akte)
        result = json.loads(out)
        self.assertEqual(result['next_skill'], 'mandantenkommunikation')
        self.assertEqual(result.get('next_product'), 'mandantenbrief')
        self.assertEqual(result.get('responsible'), 'RAin Ada Ahrens')

    def test_same_hash_skill_change_updates_routing_and_preserves_gate_decisions(self):
        args = ('product', '--akte', self.akte, '--id', 'mandantenbrief', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--zustand', 'geprueft')
        self.assertEqual(run(*args, '--skill', 'schriftsaetze-entwerfen')[0], 0)
        for gate in ('G3', 'G6'):
            self.assertEqual(run('gate', '--akte', self.akte, '--gate', gate, '--aktion', 'oeffnen', '--person', 'RAin Ada Ahrens', '--bezug', 'mandantenbrief')[0], 0)
        self.assertEqual(run('gate', '--akte', self.akte, '--gate', 'G6', '--aktion', 'freigeben', '--person', 'RAin Ada Ahrens', '--bezug', 'mandantenbrief')[0], 0)
        before = self.state()

        self.assertEqual(run(*args, '--skill', 'mandantenkommunikation')[0], 0)
        code, out, _ = run('next', '--akte', self.akte)
        self.assertEqual(code, 0)
        result = json.loads(out)
        self.assertEqual(result['next_skill'], 'mandantenkommunikation')
        self.assertEqual(result['next_product'], 'mandantenbrief')
        self.assertEqual(result['responsible'], 'RAin Ada Ahrens')
        after = self.state()
        for gate in ('G3', 'G6'):
            self.assertEqual(after['gates'][gate], {**before['gates'][gate], 'skill': 'mandantenkommunikation'})
        self.assertEqual(after['products']['mandantenbrief']['sha256'], before['products']['mandantenbrief']['sha256'])
        self.assertEqual(after['products']['mandantenbrief']['state'], 'geprueft')
        self.assertNotIn('approved_by', after['products']['mandantenbrief'])

    def test_changed_product_cannot_inherit_review(self):
        run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 's', '--zustand', 'geprueft')
        (Path(self.akte) / '01_Bearbeitung/Klage_v04.docx').write_bytes(b'ungepruefte neue Fassung')
        self.assertEqual(run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 's', '--zustand', 'freigegeben')[0], 2)

    def test_product_release_requires_named_person(self):
        run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 's', '--zustand', 'geprueft')
        self.assertEqual(run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 's', '--zustand', 'freigegeben')[0], 2)

    def test_named_product_approval_keeps_exact_reviewed_hash(self):
        args = ('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 's')
        run(*args, '--zustand', 'geprueft')
        digest = self.state()['products']['klage']['sha256']
        self.assertEqual(run(*args, '--zustand', 'freigegeben', '--person', 'RAin Ada Ahrens')[0], 0)
        product = self.state()['products']['klage']
        self.assertEqual(product['approved_by'], 'RAin Ada Ahrens')
        self.assertEqual(product['sha256'], digest)
        (Path(self.akte) / '01_Bearbeitung/Klage_v04.docx').write_bytes(b'andere Fassung')
        code, _, error = run(*args, '--zustand', 'freigegeben', '--person', 'RAin Ada Ahrens')
        self.assertEqual(code, 2)
        self.assertIn('Fassung seit Prüfung verändert', error)

    def test_gate_release_rejects_unregistered_file_change(self):
        run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 'schriftsaetze-entwerfen', '--zustand', 'geprueft')
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--bezug', 'klage')
        (Path(self.akte) / '01_Bearbeitung/Klage_v04.docx').write_bytes(b'andere Fassung')
        self.assertEqual(run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'freigeben', '--person', 'RAin Ada Ahrens', '--bezug', 'klage')[0], 2)

    def test_registered_change_reopens_bound_gate(self):
        run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 'schriftsaetze-entwerfen', '--zustand', 'geprueft')
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'oeffnen', '--bezug', 'klage')
        run('gate', '--akte', self.akte, '--gate', 'G3', '--aktion', 'freigeben', '--person', 'RAin Ada Ahrens', '--bezug', 'klage')
        (Path(self.akte) / '01_Bearbeitung/Klage_v04.docx').write_bytes(b'neue Fassung')
        run('product', '--akte', self.akte, '--id', 'klage', '--pfad', '01_Bearbeitung/Klage_v04.docx', '--skill', 'schriftsaetze-entwerfen')
        self.assertEqual(self.state()['gates']['G3']['status'], 'offen')

    def test_denied_closing_gate_blocks_closure(self):
        for g in ('G4', 'G5'):
            run('gate', '--akte', self.akte, '--gate', g, '--aktion', 'nicht-erforderlich', '--notiz', 'kein Anlass')
        run('gate', '--akte', self.akte, '--gate', 'G8', '--aktion', 'oeffnen', '--bezug', 'Ende')
        run('gate', '--akte', self.akte, '--gate', 'G8', '--aktion', 'ablehnen', '--person', 'RAin Ada Ahrens', '--bezug', 'Ende')
        self.assertEqual(run('phase', '--akte', self.akte, '--phase', 'abschluss', '--grund', 'Ende')[0], 2)


class CockpitTests(unittest.TestCase):
    def test_cockpit_orders_by_urgency(self):
        with tempfile.TemporaryDirectory() as root:
            for name, gate in (('M-1', None), ('M-2', 'G3'), ('M-3', 'G2')):
                akte = str(Path(root) / name)
                run('init', '--akte', akte, '--matter-id', name, '--stufe', '2')
                if gate:
                    run('gate', '--akte', akte, '--gate', gate, '--aktion', 'oeffnen', '--bezug', 'x')
            (Path(root) / 'M-4/00_Mandat').mkdir(parents=True)
            (Path(root) / 'M-4/00_Mandat/mandatslauf.json').write_text('kaputt')
            code, out, _ = run('cockpit', '--kanzlei', root)
            self.assertEqual(code, 0)
            rows = json.loads(out)['mandate']
            self.assertEqual([r['akte'] for r in rows], ['M-4', 'M-3', 'M-2', 'M-1'])
            self.assertEqual(rows[1]['next_skill'], 'fristen-berechnen-ueberwachen')
            self.assertFalse(json.loads(out)['external_action_allowed'])

    def test_cockpit_markdown(self):
        with tempfile.TemporaryDirectory() as root:
            run('init', '--akte', str(Path(root) / 'M-9'), '--matter-id', 'M-9', '--stufe', '1')
            code, out, _ = run('cockpit', '--kanzlei', root, '--format', 'md')
            self.assertEqual(code, 0); self.assertIn('| M-9 | eingang | Gates: keine; Fragen: 0 | ki-kanzlei-steuern |', out)

    def test_cockpit_missing_root(self):
        self.assertEqual(run('cockpit', '--kanzlei', '/nicht/vorhanden')[0], 2)


    def test_partial_json_does_not_hide_other_mandates(self):
        with tempfile.TemporaryDirectory() as root:
            run('init', '--akte', str(Path(root) / 'M-1'), '--matter-id', 'M-1', '--stufe', '2')
            broken = Path(root) / 'M-2/00_Mandat/mandatslauf.json'
            broken.parent.mkdir(parents=True)
            broken.write_text('{"schema_version": 1}')
            code, out, _ = run('cockpit', '--kanzlei', root)
            self.assertEqual(code, 0)
            rows = json.loads(out)['mandate']
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['akte'], 'M-2')
            self.assertIn('fehler', rows[0])

    def test_invalid_side_run_does_not_hide_other_mandates_in_markdown(self):
        with tempfile.TemporaryDirectory() as root:
            for name in ('M-1', 'M-2'):
                self.assertEqual(run('init', '--akte', str(Path(root) / name), '--matter-id', name, '--stufe', '2')[0], 0)
            broken = Path(root) / 'M-1/00_Mandat/mandatslauf.json'
            data = json.loads(broken.read_text(encoding='utf-8'))
            for side_run in (None, 42, {}, 'urlaub'):
                with self.subTest(side_run=side_run):
                    data['side_runs'] = [side_run]
                    broken.write_text(json.dumps(data), encoding='utf-8')
                    code, out, _ = run('cockpit', '--kanzlei', root, '--format', 'md')
                    self.assertEqual(code, 0)
                    self.assertIn('| M-1 | Fehler | Mandatslauf nicht lesbar | |', out)
                    self.assertIn('| M-2 | eingang | Gates: keine; Fragen: 0 | ki-kanzlei-steuern |', out)

    def test_markdown_keeps_four_column_limit(self):
        with tempfile.TemporaryDirectory() as root:
            run('init', '--akte', str(Path(root) / 'M-1'), '--matter-id', 'M-1', '--stufe', '2')
            _, out, _ = run('cockpit', '--kanzlei', root, '--format', 'md')
            self.assertLessEqual(len(out.splitlines()[0].split('|')) - 2, 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
