#!/usr/bin/env python3
"""Reproduzierbare Offline-Probe. Alle Personen, Freigaben und Belege sind FIKTIV.

Auch mode=live prüft hier nur das lokale Journal. Kein Client, kein Netzwerk,
kein tatsächlicher Versand, keine tatsächliche Authentifizierung oder Signatur.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HELPER = REPO / 'ki-native-kanzlei/scripts/computerlauf.py'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, help='Neues oder leeres Ausgabeverzeichnis')
    args = parser.parse_args()
    out = Path(args.out).resolve()
    if out.exists() and any(out.iterdir()):
        raise SystemExit('Ausgabeverzeichnis ist nicht leer; Demo überschreibt keine vorhandenen Daten.')
    out.mkdir(parents=True, exist_ok=True)
    root = out / 'Kanzlei'
    mandate = root / 'DEMO-1'
    mandate.mkdir(parents=True)
    fixtures = {
        'betreff.txt': 'FIKTIVE OFFLINE-PROBE: Rechnung zur Durchsicht',
        'text.txt': 'FIKTIVE OFFLINE-PROBE. Sehr geehrte Frau Fenchel, anbei die nur zu Testzwecken dargestellte Rechnung.',
        'rechnung.txt': 'FIKTIVE OFFLINE-PROBE. Dies ist keine echte Rechnung und keine Forderung.',
        'freigabe.txt': 'FIKTIVE OFFLINE-PROBE. Ada Ahrens bestätigt im fiktiven Ablauf die jeweils im Prüfprotokoll genannte Fassung. Es gibt keine reale Zustimmung und keinen Transport.',
        'route.txt': 'FIKTIVE OFFLINE-PROBE. Beispielroute: persönliche Handlung der fiktiven Postfachinhaberin Ada Ahrens; keine echte Signatur- oder Rechtsprüfung.',
        'ausgang.txt': 'FIKTIVE OFFLINE-PROBE. Simulierter Ausgangsbeleg, kein tatsächlicher Providerkontakt.',
        'eingang.txt': 'FIKTIVE OFFLINE-PROBE. Simulierter Eingangsbeleg, kein tatsächlicher Eingang und keine Zustellung.'
    }
    for name, content in fixtures.items():
        (mandate / name).write_text(content + '\n', encoding='utf-8')
    transcript = []

    def run(command, value, expected=0):
        number = len(transcript) + 1
        path = out / f'{number:02d}-{command}.json'
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        result = subprocess.run([sys.executable, str(HELPER), '--root', str(root), command, '--input', str(path)], capture_output=True, text=True)
        transcript.append({'step': number, 'command': command, 'input': value, 'expected_exit': expected, 'actual_exit': result.returncode, 'output': json.loads(result.stdout) if result.returncode == 0 else None, 'error': result.stderr.strip()})
        (out / 'protokoll.json').write_text(json.dumps({'hinweis': __doc__, 'schritte': transcript}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        if result.returncode != expected:
            raise AssertionError((command, result.returncode, result.stderr))
        return transcript[-1]['output']

    session = {'session_id': 'DEMO-SIMULATION', 'mode': 'simulation', 'level': 3, 'person': 'Ada Ahrens', 'expires': (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat(), 'permissions_confirmed': True, 'mandates': {'DEMO-1': 'DEMO-1'}, 'apps': [{'app': 'outlook', 'account': 'kanzlei@example.test', 'actions': ['send'], 'transport_domains': ['outlook.example.test'], 'recipient_domains': ['mandant.example.test']}, {'app': 'bea', 'account': 'bea:DEMO-AHRENS', 'actions': ['send', 'eeb'], 'transport_domains': ['bea.example.test'], 'recipient_domains': []}]}
    mail = {'action_id': 'DEMO-MAIL-1', 'app': 'outlook', 'account': 'kanzlei@example.test', 'mandat': 'DEMO-1', 'kind': 'send', 'to': ['mara@mandant.example.test'], 'cc': [], 'bcc': [], 'subject_file': 'betreff.txt', 'body_file': 'text.txt', 'attachments': ['rechnung.txt'], 'transport_domains': ['outlook.example.test'], 'source_ids': [], 'legal_route': 'not_applicable', 'legal_route_confirmed': False, 'legal_route_evidence': None, 'personal_actor': None}

    def prepare(plan):
        run('plan', plan)
        frozen = run('freeze', {'action_id': plan['action_id']})
        consent = 'freigabe-' + plan['action_id'] + '.txt'
        (mandate / consent).write_text('FIKTIVE OFFLINE-PROBE. Keine reale Zustimmung. Die fiktive Ada Ahrens bestätigt ausschließlich Aktion ' + plan['action_id'] + ' mit Manifest-SHA-256 ' + frozen['manifest_sha256'] + '.\n', encoding='utf-8')
        run('approve', {'action_id': plan['action_id'], 'person': 'Ada Ahrens', 'manifest_sha256': frozen['manifest_sha256'], 'confirmation_received': True, 'evidence_file': consent})
        return {'action_id': plan['action_id'], 'manifest_sha256': frozen['manifest_sha256']}

    def outcome(aid, person='Ada Ahrens'):
        return {'action_id': aid, 'status': 'ausgefuehrt', 'person': person, 'evidence_file': 'ausgang.txt', 'provider_id': 'FIKTIV-NICHT-VERBUNDEN-' + aid, 'provider_id_absent_reason': None, 'no_effect_confirmed': False, 'note': 'Nur fiktives Ergebnis der Offline-Zustandsprobe; kein wirklicher Transport.'}

    run('init', session)
    run('start', prepare(mail), expected=2)
    run('stop', {'person': 'Ada Ahrens', 'reason': 'Fiktive Simulation abgeschlossen.'})
    run('init', dict(session, session_id='DEMO-LOKALE-ZUSTANDSPROBE', mode='live'))
    mail['action_id'] = 'DEMO-MAIL-2'
    mail_start = prepare(mail)
    assert run('start', mail_start)['status'] == 'gestartet'
    run('result', outcome(mail['action_id']))
    run('receipt', {'action_id': mail['action_id'], 'person': 'Ada Ahrens', 'receipt_status': 'bestaetigt', 'evidence_file': 'eingang.txt', 'provider_id': 'FIKTIVER-EINGANG-1', 'provider_id_absent_reason': None, 'note': 'Fiktiver Empfangsbeleg; kein echter Server- oder Gerichtseingang.'})
    run('start', mail_start, expected=2)
    bea = dict(mail, action_id='DEMO-BEA-1', app='bea', account='bea:DEMO-AHRENS', to=['bea:DEMO-GERICHT'], transport_domains=['bea.example.test'], legal_route='personal_owner_required', legal_route_confirmed=True, legal_route_evidence='route.txt', personal_actor='Ada Ahrens')
    assert run('start', prepare(bea))['status'] == 'wartet_auf_mensch'
    run('result', outcome(bea['action_id'], person='Bertram Brecht'), expected=2)
    run('result', outcome(bea['action_id']))
    run('stop', {'person': 'Ada Ahrens', 'reason': 'Fiktive Offline-Probe beendet; keine Konten geöffnet.'})
    final = run('status', {})
    assert final['session']['stopped'] is True
    assert final['actions']['DEMO-MAIL-2']['status'] == 'ausgefuehrt'
    assert final['actions']['DEMO-BEA-1']['status'] == 'ausgefuehrt'
    print(json.dumps({'hinweis': 'Ausschließlich Offline-Zustandsprobe; kein Transport, keine echten Personenfreigaben.', 'protokoll': str(out / 'protokoll.json'), 'schritte': len(transcript), 'ergebnis': 'bestanden'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
