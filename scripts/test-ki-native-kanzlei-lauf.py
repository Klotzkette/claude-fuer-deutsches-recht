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


if __name__ == '__main__':
    unittest.main(verbosity=2)
