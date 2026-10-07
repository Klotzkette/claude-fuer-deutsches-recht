#!/usr/bin/env python3
"""Mandatslauf: Phasen, führende Fassungen und Freigabegates je Mandat. Python >= 3.10, stdlib.

Dokumentiert nur. Kein Versand, keine Kalenderschreibung, keine Buchung, keine automatische Freigabe.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

PHASES = ['eingang', 'annahme', 'akte', 'frist', 'sacharbeit', 'kommunikation',
          'versandvorbereitung', 'abrechnung', 'zahlung', 'abschluss']
PHASE_SKILLS = {
    'eingang': ['ki-kanzlei-steuern'], 'annahme': ['mandatsannahme-interessenkollision'],
    'akte': ['akte-fristen-anlegen'], 'frist': ['fristen-berechnen-ueberwachen'],
    'sacharbeit': ['recht-recherchieren', 'schriftsaetze-entwerfen', 'vertraege-agb-pruefen', 'vertraege-gestalten'],
    'kommunikation': ['mandantenkommunikation'], 'versandvorbereitung': ['bea-anlagen-vorbereiten'],
    'abrechnung': ['zeiten-erfassen', 'honorar-budget-vereinbaren', 'abrechnung-e-rechnung'],
    'zahlung': ['zahlungen-buchhaltung'], 'abschluss': ['mandat-abschliessen'],
}
GATES = {
    'G1': ('Annahme', 'mandatsannahme-interessenkollision'), 'G2': ('Fristeintrag', 'fristen-berechnen-ueberwachen'),
    'G3': ('Versand und Einreichung', 'bea-anlagen-vorbereiten'), 'G4': ('Rechnungsausgabe', 'abrechnung-e-rechnung'),
    'G5': ('Zahlung und Fremdgeld', 'zahlungen-buchhaltung'), 'G6': ('Dienstleister', 'workflow-uebergabe'),
    'G7': ('Meldung', 'geldwaesche-pruefen'), 'G8': ('Abschluss und Löschung', 'mandat-abschliessen'),
}
GATE_STATES = {'offen', 'freigegeben', 'abgelehnt', 'nicht_erforderlich'}
PRODUCT_STATES = {'entwurf', 'geprueft', 'freigegeben'}
MACHINE_WORDS = re.compile(r'\b(ki|ai|agent|agentin|system|automatisch|bot|modell|claude|codex|gpt)\b', re.I)
FILE = Path('00_Mandat') / 'mandatslauf.json'


class LaufError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def clean(value, label, maxlen=400):
    if not isinstance(value, str) or not value.strip():
        raise LaufError(f'{label}: Text fehlt')
    if any(ord(c) < 32 for c in value) or len(value) > maxlen:
        raise LaufError(f'{label}: unzulässige Zeichen oder zu lang')
    return value.strip()


def load(akte):
    path = Path(akte) / FILE
    if not path.is_file():
        raise LaufError('Kein Mandatslauf vorhanden; zuerst init ausführen')
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('schema_version') != 1:
        raise LaufError('Unbekannte Schema-Version')
    return data


def save(akte, data, action, detail):
    data['revision'] = int(data.get('revision', 0)) + 1
    data['updated'] = now()
    data.setdefault('history', []).append({'at': data['updated'], 'revision': data['revision'], 'action': action, 'detail': detail})
    path = Path(akte) / FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix='.mandatslauf-', suffix='.json')
    with os.fdopen(fd, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write('\n')
    os.replace(tmp, path)
    return data


def cmd_init(a):
    path = Path(a.akte) / FILE
    if path.exists():
        raise LaufError('Mandatslauf existiert bereits; vorhandenen Lauf nicht überschreiben')
    if a.stufe not in (0, 1, 2, 3):
        raise LaufError('Freigabestufe muss 0, 1, 2 oder 3 sein')
    data = {'schema_version': 1, 'matter_id': clean(a.matter_id, 'matter_id', 80), 'autonomy_level': a.stufe,
            'phase': 'eingang', 'side_runs': [], 'products': {}, 'gates': {}, 'open_questions': [], 'revision': 0, 'history': []}
    return save(a.akte, data, 'init', f'Freigabestufe {a.stufe}')


def cmd_phase(a):
    data = load(a.akte)
    if a.phase not in PHASES:
        raise LaufError('Unbekannte Phase: ' + a.phase)
    if a.phase == 'abschluss':
        blocking = [g for g in ('G4', 'G5', 'G8') if data['gates'].get(g, {}).get('status') in (None, 'offen')]
        if blocking:
            raise LaufError('Abschluss erst nach Entscheidung über ' + ', '.join(blocking))
    grund = clean(a.grund, 'grund')
    if a.nebenlauf:
        if a.phase not in data['side_runs']:
            data['side_runs'].append(a.phase)
        return save(a.akte, data, 'nebenlauf', f'{a.phase}: {grund}')
    data['phase'] = a.phase
    data['side_runs'] = [p for p in data['side_runs'] if p != a.phase]
    return save(a.akte, data, 'phase', f'{a.phase}: {grund}')


def cmd_product(a):
    data = load(a.akte)
    pid = clean(a.id, 'id', 80)
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', pid):
        raise LaufError('id: nur Buchstaben, Ziffern, Punkt, Bindestrich, Unterstrich')
    if a.zustand not in PRODUCT_STATES:
        raise LaufError('zustand muss entwurf, geprueft oder freigegeben sein')
    skill = clean(a.skill, 'skill', 80)
    rel = clean(a.pfad, 'pfad', 300)
    if Path(rel).is_absolute() or '..' in Path(rel).parts:
        raise LaufError('pfad muss relativ zum Mandatsordner liegen')
    target = Path(a.akte) / rel
    if not target.is_file():
        raise LaufError('Produktdatei nicht vorhanden: ' + rel)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    previous = data['products'].get(pid)
    if a.zustand == 'freigegeben' and not (previous and previous.get('state') in ('geprueft', 'freigegeben')):
        raise LaufError('freigegeben setzt eine zuvor geprüfte Fassung voraus')
    entry = {'path': rel, 'sha256': digest, 'skill': skill, 'state': a.zustand, 'updated': now()}
    if previous and previous.get('sha256') != digest:
        entry['replaces'] = previous['sha256']
    data['products'][pid] = entry
    return save(a.akte, data, 'product', f'{pid} {a.zustand} {rel} {digest[:12]}')


def cmd_gate(a):
    data = load(a.akte)
    if a.gate not in GATES:
        raise LaufError('Unbekanntes Gate: ' + a.gate)
    gate = data['gates'].get(a.gate, {'status': None})
    bezug = clean(a.bezug, 'bezug') if a.bezug else ''
    if a.aktion == 'oeffnen':
        if gate.get('status') == 'freigegeben':
            raise LaufError('Gate bereits freigegeben; für eine neue Fassung zuerst zuruecksetzen')
        gate = {'status': 'offen', 'opened_at': now(), 'reference': bezug, 'skill': GATES[a.gate][1]}
    elif a.aktion in ('freigeben', 'ablehnen'):
        person = clean(a.person or '', 'person', 120)
        if MACHINE_WORDS.search(person):
            raise LaufError('Freigabe nur durch eine namentlich bezeichnete Person')
        if gate.get('status') != 'offen':
            raise LaufError('Gate ist nicht geöffnet')
        if not bezug:
            raise LaufError('bezug (freigegebene Fassung oder Vorgang) fehlt')
        gate = {**gate, 'status': 'freigegeben' if a.aktion == 'freigeben' else 'abgelehnt', 'by': person, 'at': now(),
                'reference': bezug, 'note': clean(a.notiz, 'notiz') if a.notiz else ''}
    elif a.aktion == 'nicht-erforderlich':
        gate = {'status': 'nicht_erforderlich', 'at': now(), 'note': clean(a.notiz or '', 'notiz')}
    elif a.aktion == 'zuruecksetzen':
        gate = {'status': 'offen', 'opened_at': now(), 'reference': bezug, 'skill': GATES[a.gate][1],
                'reset_from': gate.get('status'), 'note': clean(a.notiz or '', 'notiz')}
    else:
        raise LaufError('Unbekannte Aktion')
    data['gates'][a.gate] = gate
    return save(a.akte, data, 'gate', f'{a.gate} {gate["status"]} {gate.get("by", "")}'.strip())


def cmd_question(a):
    data = load(a.akte)
    text = clean(a.text, 'text')
    if a.erledigt:
        data['open_questions'] = [q for q in data['open_questions'] if q != text]
        return save(a.akte, data, 'question_closed', text)
    if text not in data['open_questions']:
        data['open_questions'].append(text)
    return save(a.akte, data, 'question', text)


def recommend(data):
    gates = data['gates']
    if gates.get('G2', {}).get('status') == 'offen':
        return 'fristen-berechnen-ueberwachen', 'Gate G2 offen: Fristeintrag bestätigen lassen, bevor Sacharbeit fortgesetzt wird'
    for g, (label, skill) in GATES.items():
        if gates.get(g, {}).get('status') == 'offen':
            return skill, f'Gate {g} ({label}) wartet auf Freigabe; Produkt dafür bereithalten'
    phase = data['phase']
    skills = PHASE_SKILLS[phase]
    hint = 'Phase ' + phase
    if data['open_questions']:
        hint += '; offene Fragen: ' + '; '.join(data['open_questions'][:3])
    return skills[0], hint


def cmd_status(a):
    data = load(a.akte)
    print(json.dumps({k: data[k] for k in ('matter_id', 'autonomy_level', 'phase', 'side_runs', 'products', 'gates', 'open_questions', 'revision', 'updated')}, ensure_ascii=False, indent=2))


def cmd_next(a):
    data = load(a.akte)
    skill, reason = recommend(data)
    print(json.dumps({'next_skill': skill, 'reason': reason, 'autonomy_level': data['autonomy_level'],
                      'external_action_allowed': False, 'open_gates': [g for g, v in data['gates'].items() if v.get('status') == 'offen']}, ensure_ascii=False, indent=2))


def cockpit(root, max_depth=3):
    """Alle Mandatsläufe unterhalb eines Kanzleiordners einsammeln und nach Dringlichkeit ordnen."""
    root = Path(root)
    if not root.is_dir():
        raise LaufError('Kanzleiordner nicht vorhanden')
    rows = []
    for path in sorted(root.rglob('mandatslauf.json')):
        rel = path.relative_to(root)
        if path.parent.name != '00_Mandat' or len(rel.parts) - 2 > max_depth:
            continue
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
            if data.get('schema_version') != 1:
                raise ValueError('Schema')
        except Exception:
            rows.append({'akte': str(rel.parent.parent), 'fehler': 'Mandatslauf nicht lesbar'})
            continue
        open_gates = sorted(g for g, v in data.get('gates', {}).items() if v.get('status') == 'offen')
        skill, reason = recommend(data)
        rank = 0 if 'G2' in open_gates else 1 if open_gates else 2 if data.get('open_questions') else 3
        rows.append({'akte': str(rel.parent.parent), 'matter_id': data.get('matter_id'), 'phase': data.get('phase'),
                     'side_runs': data.get('side_runs', []), 'autonomy_level': data.get('autonomy_level'),
                     'open_gates': open_gates, 'open_questions': len(data.get('open_questions', [])),
                     'next_skill': skill, 'reason': reason, 'updated': data.get('updated'), 'rank': rank})
    rows.sort(key=lambda r: (r.get('rank', -1), r.get('updated') or ''))
    return rows


def cmd_cockpit(a):
    rows = cockpit(a.kanzlei)
    if a.format == 'md':
        print('| Akte | Phase | Offene Gates | Offene Fragen | Nächster Skill |')
        print('| --- | --- | --- | --- | --- |')
        for r in rows:
            if 'fehler' in r:
                print(f"| {r['akte']} | Fehler | {r['fehler']} | | |")
                continue
            phase = r['phase'] + (' + ' + ', '.join(r['side_runs']) if r['side_runs'] else '')
            print(f"| {r['akte']} | {phase} | {', '.join(r['open_gates']) or 'keine'} | {r['open_questions']} | {r['next_skill']} |")
    else:
        print(json.dumps({'mandate': rows, 'external_action_allowed': False}, ensure_ascii=False, indent=2))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='cmd', required=True)
    def common(p):
        p.add_argument('--akte', required=True)
    p = sub.add_parser('init'); common(p); p.add_argument('--matter-id', required=True); p.add_argument('--stufe', type=int, default=1)
    p = sub.add_parser('phase'); common(p); p.add_argument('--phase', required=True); p.add_argument('--grund', required=True); p.add_argument('--nebenlauf', action='store_true')
    p = sub.add_parser('product'); common(p); p.add_argument('--id', required=True); p.add_argument('--pfad', required=True); p.add_argument('--skill', required=True); p.add_argument('--zustand', default='entwurf')
    p = sub.add_parser('gate'); common(p); p.add_argument('--gate', required=True); p.add_argument('--aktion', required=True, choices=['oeffnen', 'freigeben', 'ablehnen', 'nicht-erforderlich', 'zuruecksetzen']); p.add_argument('--person'); p.add_argument('--bezug'); p.add_argument('--notiz')
    p = sub.add_parser('question'); common(p); p.add_argument('--text', required=True); p.add_argument('--erledigt', action='store_true')
    p = sub.add_parser('status'); common(p)
    p = sub.add_parser('next'); common(p)
    p = sub.add_parser('cockpit'); p.add_argument('--kanzlei', required=True); p.add_argument('--format', choices=['json', 'md'], default='json')
    a = ap.parse_args(argv)
    try:
        handler = {'init': cmd_init, 'phase': cmd_phase, 'product': cmd_product, 'gate': cmd_gate, 'question': cmd_question, 'status': cmd_status, 'next': cmd_next, 'cockpit': cmd_cockpit}[a.cmd]
        result = handler(a)
        if result is not None:
            print(json.dumps({'matter_id': result['matter_id'], 'phase': result['phase'], 'revision': result['revision'], 'open_gates': [g for g, v in result['gates'].items() if v.get('status') == 'offen']}, ensure_ascii=False))
    except LaufError as exc:
        print('FEHLER: ' + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
