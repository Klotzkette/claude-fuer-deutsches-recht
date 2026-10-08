#!/usr/bin/env python3
"""Lokales Aktionsjournal; kein Transport, keine Authentifizierung, kein Geheimnisspeicher.

Python 3.10+, ausschließlich Standardbibliothek. Siehe references/computerlauf-cli.md.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

KINDS = {'send', 'read', 'export', 'eeb'}
MACHINES = re.compile(r'\b(ki|ai|agent|agentin|system|automatisch|bot|modell|claude|codex|gpt)\b', re.I)
BUSY = {'gestartet', 'wartet_auf_mensch', 'unklar', 'ausgefuehrt'}


class LaufError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def text(value, label, limit=400):
    if not isinstance(value, str) or not value.strip() or len(value) > limit or any(ord(c) < 32 for c in value):
        raise LaufError(f'{label}: leer, zu lang oder Steuerzeichen enthalten')
    return value.strip()


def ident(value):
    value = text(value, 'Kennung', 80)
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', value):
        raise LaufError('Kennung: nur Buchstaben, Ziffern, Punkt, Unterstrich und Bindestrich')
    return value


def person(value):
    value = text(value, 'Person', 120)
    if MACHINES.search(value) or len(value.split()) < 2:
        raise LaufError('Eine namentlich bezeichnete menschliche Person ist erforderlich')
    return value


def fields(obj, required, optional=()):
    if not isinstance(obj, dict) or set(obj) - set(required) - set(optional) or set(required) - set(obj):
        raise LaufError('Unbekannte oder fehlende JSON-Felder; Geheimnisse gehören nicht in diese Eingaben')


def strings(value, label, empty=False):
    if not isinstance(value, list) or (not value and not empty):
        raise LaufError(f'{label}: Liste erforderlich')
    result = [text(item, label) for item in value]
    if len(set(result)) != len(result):
        raise LaufError(f'{label}: doppelte Werte')
    return result


def expiry(value):
    try:
        stamp = datetime.fromisoformat(text(value, 'expires'))
        if stamp.tzinfo is None:
            raise ValueError('Zeitzone fehlt')
        return stamp
    except ValueError as exc:
        raise LaufError('expires benötigt Datum, Uhrzeit und Zeitzone im ISO-Format') from exc


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def digest(value):
    return hashlib.sha256(value).hexdigest()


def contained(base, relative, directory=False):
    relative = text(relative, 'Dateipfad', 500)
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts or not rel.parts:
        raise LaufError('Nur relative Pfade innerhalb des Mandats sind zulässig')
    target = base
    for part in rel.parts:
        target = target / part
        if target.is_symlink():
            raise LaufError('Symbolische Links sind für Journal und Belegdateien nicht zulässig')
    if not target.resolve().is_relative_to(base.resolve()):
        raise LaufError('Pfad verlässt das Mandat')
    if not (target.is_dir() if directory else target.is_file()):
        raise LaufError('Mandatsverzeichnis oder Belegdatei fehlt: ' + relative)
    return target


def file_record(base, relative):
    path = contained(base, relative)
    return {'path': relative, 'sha256': digest(path.read_bytes()), 'bytes': path.stat().st_size}


def atomic(path, value):
    fd, name = tempfile.mkstemp(prefix='.computerlauf-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(canonical(value) + b'\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        if hasattr(os, 'O_DIRECTORY'):
            directory_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    finally:
        if os.path.exists(name):
            os.unlink(name)


@contextmanager
def locked(root):
    if not root.is_dir() or root.is_symlink():
        raise LaufError('Kanzleiordner muss als echtes Verzeichnis bestehen')
    folder = root / '.computerlauf'
    if folder.is_symlink():
        raise LaufError('Journal darf kein symbolischer Link sein')
    folder.mkdir(mode=0o700, exist_ok=True)
    path = folder / 'lock'
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise LaufError('Journal ist gesperrt; keinen zweiten Lauf oder automatisches Entsperren starten') from exc
    try:
        with os.fdopen(fd, 'w') as stream:
            stream.write(str(os.getpid()) + '\n')
        yield folder
    finally:
        path.unlink(missing_ok=True)


def load(folder):
    path = folder / 'lauf.json'
    if path.is_symlink():
        raise LaufError('Journal darf kein symbolischer Link sein')
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise LaufError('Journal fehlt oder ist unlesbar; zuerst init ausführen') from exc
    if not isinstance(data, dict) or data.get('schema_version') != 1 or not isinstance(data.get('actions'), dict) or not isinstance(data.get('session'), dict):
        raise LaufError('Unvollständiges oder unbekanntes Journal')
    return data


def journal(folder, state, operation, action_id=None):
    state['history'].append({'at': now(), 'operation': operation, 'action_id': action_id})
    atomic(folder / 'lauf.json', state)


def session_validate(root, value):
    fields(value, {'session_id', 'mode', 'level', 'person', 'expires', 'permissions_confirmed', 'mandates', 'apps'})
    ident(value['session_id']); person(value['person'])
    if value['mode'] not in {'simulation', 'live'} or type(value['level']) is not int or value['level'] not in {2, 3}:
        raise LaufError('Journal benötigt Stufe 2 oder 3 und Modus simulation oder live')
    if value['permissions_confirmed'] is not True or expiry(value['expires']) <= datetime.now(timezone.utc):
        raise LaufError('Tatsächliche Berechtigungen müssen bestätigt sein; Sitzung muss in der Zukunft ablaufen')
    if not isinstance(value['mandates'], dict) or not value['mandates']:
        raise LaufError('Mandatsbereiche fehlen')
    for key, path in value['mandates'].items():
        ident(key); contained(root, path, directory=True)
        if path == '.' or '.computerlauf' in Path(path).parts:
            raise LaufError('Mandatsbereich muss ein eigenes Unterverzeichnis sein')
    if not isinstance(value['apps'], list) or not value['apps']:
        raise LaufError('App- und Kontobereiche fehlen')
    seen = set()
    for scope in value['apps']:
        fields(scope, {'app', 'account', 'actions', 'transport_domains', 'recipient_domains'})
        key = (ident(scope['app']), text(scope['account'], 'Konto'))
        if scope['app'] in {'outlook', 'gmail'} and not re.fullmatch(r'[^\s@<>]+@[^\s@<>]+', scope['account']):
            raise LaufError('Mailkonto muss die konkrete Absenderadresse einschließlich Alias bezeichnen')
        if scope['app'] == 'bea' and not re.fullmatch(r'bea:[A-Za-z0-9._-]+', scope['account']):
            raise LaufError('beA-Konto muss den konkreten Postfach-Identifier bezeichnen')
        if key in seen:
            raise LaufError('App/Konto mehrfach aufgeführt')
        seen.add(key)
        if set(strings(scope['actions'], 'Aktionen')) - KINDS:
            raise LaufError('Unbekannte Aktion')
        for label in ('transport_domains', 'recipient_domains'):
            for domain in strings(scope[label], label, empty=label == 'recipient_domains'):
                if not re.fullmatch(r'[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?', domain) or '.' not in domain:
                    raise LaufError('Domains müssen explizit, kleingeschrieben und ohne Platzhalter angegeben werden')
    return dict(value, stopped=False)


def scope_check(root, session, plan, live=False):
    if session['permissions_confirmed'] is not True:
        raise LaufError('Tatsächliche Berechtigungen sind nicht bestätigt')
    if session['stopped'] or expiry(session['expires']) <= datetime.now(timezone.utc):
        raise LaufError('Sitzung beendet oder abgelaufen; keine neue Aktion zulässig')
    if live and session['mode'] != 'live':
        raise LaufError('Simulation führt keinen wirklichen Start aus')
    if plan['mandat'] not in session['mandates']:
        raise LaufError('Mandat außerhalb des bestätigten Bereichs')
    scope = next((s for s in session['apps'] if s['app'] == plan['app'] and s['account'] == plan['account']), None)
    if not scope or plan['kind'] not in scope['actions'] or not set(plan['transport_domains']).issubset(scope['transport_domains']):
        raise LaufError('App, Konto, Aktion oder Transportdomain außerhalb des bestätigten Bereichs')
    if live and plan['kind'] in {'send', 'eeb'} and session['level'] != 3:
        raise LaufError('Versand und eEB erfordern zusätzlich Freigabestufe 3')
    for address in plan['to'] + plan['cc'] + plan['bcc']:
        if plan['app'] == 'bea':
            if not re.fullmatch(r'bea:[A-Za-z0-9._-]+', address):
                raise LaufError('beA-Empfänger benötigt den belegten Identifier im Format bea:<Identifier>')
        elif not re.fullmatch(r'[^\s@<>]+@[^\s@<>]+', address) or address.rsplit('@', 1)[1].lower() not in scope['recipient_domains']:
            raise LaufError('E-Mail-Empfänger oder Empfängerdomain nicht zugelassen')
    return contained(root, session['mandates'][plan['mandat']], directory=True)


def plan_validate(root, session, value):
    fields(value, {'action_id', 'app', 'account', 'mandat', 'kind', 'to', 'cc', 'bcc', 'subject_file', 'body_file', 'attachments', 'transport_domains', 'source_ids', 'legal_route', 'legal_route_confirmed', 'legal_route_evidence', 'personal_actor'})
    ident(value['action_id']); ident(value['app']); ident(value['mandat']); text(value['account'], 'Konto')
    if value['kind'] not in KINDS:
        raise LaufError('Unbekannte Aktion')
    for key in ('to', 'cc', 'bcc', 'attachments', 'source_ids'):
        strings(value[key], key, empty=True)
    strings(value['transport_domains'], 'Transportdomains')
    if len(set(value['to'] + value['cc'] + value['bcc'])) != len(value['to'] + value['cc'] + value['bcc']):
        raise LaufError('Empfänger doppelt in To/CC/BCC')
    if value['kind'] == 'eeb' and value['app'] != 'bea':
        raise LaufError('eEB ist im Prototyp ausschließlich als persönliche beA-Aktion vorgesehen')
    outgoing = value['kind'] in {'send', 'eeb'}
    if outgoing and (not value['to'] or not value['subject_file'] or not value['body_file']):
        raise LaufError('Versand benötigt Empfänger, Betreffdatei und Textdatei')
    if not outgoing and (not value['source_ids'] or value['to'] or value['cc'] or value['bcc'] or value['subject_file'] or value['body_file'] or value['attachments']):
        raise LaufError('Lesen/Export benötigt konkrete Quellkennungen und keine Versandfelder')
    route = value['legal_route']
    if value['app'] == 'bea' and outgoing:
        if route not in {'qes_verified', 'personal_owner_required'} or value['legal_route_confirmed'] is not True or not value['legal_route_evidence']:
            raise LaufError('beA-Versand benötigt die konkret geprüfte Versandroute mit Beleg')
        if value['kind'] == 'eeb' and route != 'personal_owner_required':
            raise LaufError('Der Prototyp überlässt eEB stets dem benannten Menschen')
    elif route != 'not_applicable' or value['legal_route_confirmed'] is not False or value['legal_route_evidence'] is not None:
        raise LaufError('Versandroute ist nur für beA-Versand oder eEB vorgesehen')
    if route == 'personal_owner_required':
        person(value['personal_actor'])
    elif value['personal_actor'] is not None:
        raise LaufError('personal_actor nur bei einer persönlich auszuführenden Aktion')
    base = scope_check(root, session, value)
    for path in value['attachments'] + [p for p in (value['subject_file'], value['body_file'], value['legal_route_evidence']) if p]:
        file_record(base, path)
    return base


def frozen_manifest(root, session, plan):
    base = plan_validate(root, session, plan)
    files = {role: file_record(base, plan[role]) if plan[role] else None for role in ('subject_file', 'body_file', 'legal_route_evidence')}
    files['attachments'] = [file_record(base, path) for path in plan['attachments']]
    return {'session_id': session['session_id'], 'mandate_path': session['mandates'][plan['mandat']], 'plan': plan, 'files': files}


def verify(root, session, action):
    if action['manifest']['session_id'] != session['session_id']:
        raise LaufError('Aktionsfreigabe gehört zu einer anderen Sitzung')
    current = frozen_manifest(root, session, action['plan'])
    if digest(canonical(current)) != action['manifest_sha256'] or current != action['manifest']:
        raise LaufError('Manifest oder Datei verändert; neue Fassung neu planen und freigeben')


def fingerprint(manifest):
    plan = manifest['plan']
    value = {k: plan[k] for k in ('app', 'account', 'mandat', 'kind', 'to', 'cc', 'bcc', 'source_ids')}
    for key in ('to', 'cc', 'bcc', 'source_ids'):
        value[key] = sorted(value[key])
    value['content'] = {k: r['sha256'] if r else None for k, r in manifest['files'].items() if k in {'subject_file', 'body_file'}}
    value['attachments'] = sorted((Path(r['path']).name, r['sha256']) for r in manifest['files']['attachments'])
    return digest(canonical(value))


def evidence(root, state, action, path):
    base = contained(root, action['manifest']['mandate_path'], directory=True)
    return file_record(base, path)


def provider(value):
    if value['provider_id'] is None:
        text(value['provider_id_absent_reason'], 'Grund für fehlende Providerkennung')
    else:
        text(value['provider_id'], 'Providerkennung')
        if value['provider_id_absent_reason'] is not None:
            raise LaufError('Bei vorhandener Providerkennung bleibt der Fehlgrund null')


def guard_path(folder, action):
    return folder / (action['plan']['action_id'] + '.' + str(len(action['attempts']) + 1) + '.attempt')


def orphan_reservations(folder, state):
    known = {f'{aid}.{number}.attempt' for aid, action in state['actions'].items() for number in range(1, len(action['attempts']) + 1)}
    return sorted(path.name for path in folder.glob('*.attempt') if path.name not in known)


def execute(root, folder, operation, value):
    if operation == 'init':
        session = session_validate(root, value)
        state = load(folder) if (folder / 'lauf.json').exists() else {'schema_version': 1, 'actions': {}, 'history': [], 'previous_sessions': []}
        if 'session' in state:
            old = state['session']
            if not old['stopped'] and expiry(old['expires']) > datetime.now(timezone.utc):
                raise LaufError('Bestehende Sitzung zuerst stoppen')
            if orphan_reservations(folder, state) or any(a['status'] in {'gestartet', 'wartet_auf_mensch', 'unklar'} for a in state['actions'].values()):
                raise LaufError('Offene Ausführungsversuche zuerst mit Belegen klären')
            if session['session_id'] in [s['session_id'] for s in state['previous_sessions']] + [old['session_id']]:
                raise LaufError('Sitzungskennung darf nicht wiederverwendet werden')
            state['previous_sessions'].append(old)
        state['session'] = session
        journal(folder, state, operation)
        return state['session']
    state = load(folder)
    if operation == 'status':
        fields(value, set())
        return state
    if operation == 'stop':
        fields(value, {'person', 'reason'})
        person(value['person']); text(value['reason'], 'Stopgrund')
        state['session'].update(stopped=True, stop_record=dict(value, at=now()))
        journal(folder, state, operation)
        return state['session']
    if operation == 'plan':
        plan_validate(root, state['session'], value)
        aid = value['action_id']
        if aid in state['actions']:
            raise LaufError('Aktionskennung besteht bereits; vorhandene Planung nicht überschreiben')
        action = {'plan': value, 'status': 'entwurf', 'attempts': [], 'approvals': [], 'reconciliations': [], 'receipts': []}
        state['actions'][aid] = action
    else:
        aid = ident(value.get('action_id'))
        if aid not in state['actions']:
            raise LaufError('Unbekannte Aktion')
        action = state['actions'][aid]
        if operation == 'freeze':
            fields(value, {'action_id'})
            if action['status'] != 'entwurf':
                raise LaufError('Nur ein Entwurf kann eingefroren werden')
            action['manifest'] = frozen_manifest(root, state['session'], action['plan'])
            action['manifest_sha256'] = digest(canonical(action['manifest']))
            action['fingerprint'] = fingerprint(action['manifest'])
            action['status'] = 'gefroren'
        elif operation == 'approve':
            fields(value, {'action_id', 'person', 'manifest_sha256', 'confirmation_received', 'evidence_file'})
            person(value['person'])
            if action['status'] != 'gefroren' or value['confirmation_received'] is not True or value['manifest_sha256'] != action['manifest_sha256']:
                raise LaufError('Vorhandene Bestätigung muss das genaue eingefrorene Manifest betreffen')
            verify(root, state['session'], action)
            action['approvals'].append(dict(value, evidence=evidence(root, state, action, value['evidence_file']), at=now()))
            action['status'] = 'freigegeben'
        elif operation == 'start':
            fields(value, {'action_id', 'manifest_sha256'})
            if action['status'] != 'freigegeben' or value['manifest_sha256'] != action.get('manifest_sha256'):
                raise LaufError('Nur unverändert freigegebene, noch nicht ausgeführte Aktionen können starten')
            if orphan_reservations(folder, state):
                raise LaufError('Ein Versuch ist bereits reserviert, aber nicht abschließend journalisiert; zuerst reconcile')
            scope_check(root, state['session'], action['plan'], live=True)
            verify(root, state['session'], action)
            approved = action['approvals'][-1]
            if evidence(root, state, action, approved['evidence_file']) != approved['evidence']:
                raise LaufError('Freigabebeleg wurde nachträglich verändert')
            for other in state['actions'].values():
                if other is not action and other.get('fingerprint') == action['fingerprint'] and other['status'] in BUSY:
                    raise LaufError('Gleicher Inhalt bereits gestartet, ungeklärt oder ausgeführt; kein erneuter Versand')
            guard = guard_path(folder, action)
            try:
                fd = os.open(guard, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            except FileExistsError as exc:
                raise LaufError('Versuch bereits reserviert; Zustand zuerst mit reconcile klären') from exc
            attempt = {'number': len(action['attempts']) + 1, 'at': now(), 'manifest_sha256': action['manifest_sha256']}
            with os.fdopen(fd, 'wb') as stream:
                stream.write(canonical(attempt)); stream.flush(); os.fsync(stream.fileno())
            action['attempts'].append(attempt)
            action['status'] = 'wartet_auf_mensch' if action['plan']['legal_route'] == 'personal_owner_required' else 'gestartet'
            action['execution_actor'] = action['plan']['personal_actor'] if action['status'] == 'wartet_auf_mensch' else 'Host innerhalb seiner tatsächlichen Befugnisse'
        elif operation == 'result':
            fields(value, {'action_id', 'status', 'person', 'evidence_file', 'provider_id', 'provider_id_absent_reason', 'no_effect_confirmed', 'note'})
            person(value['person']); text(value['note'], 'Ergebnisvermerk'); provider(value)
            if action['status'] not in {'gestartet', 'wartet_auf_mensch'} or value['status'] not in {'ausgefuehrt', 'unklar', 'fehlgeschlagen'}:
                raise LaufError('Kein offener Versuch oder unzulässiger Ergebnisstatus')
            if action['status'] == 'wartet_auf_mensch' and value['person'] != action['plan']['personal_actor']:
                raise LaufError('Persönliche beA-Aktion muss durch die benannte Person ausgeführt und bestätigt sein')
            if type(value['no_effect_confirmed']) is not bool or (value['status'] == 'fehlgeschlagen' and value['no_effect_confirmed'] is not True) or (value['status'] != 'fehlgeschlagen' and value['no_effect_confirmed'] is not False):
                raise LaufError('Fehlgeschlagen setzt einen belegten Nichteintritt voraus; sonst unklar dokumentieren')
            action['attempts'][-1]['result'] = dict(value, evidence=evidence(root, state, action, value['evidence_file']), at=now())
            action['status'] = value['status']
        elif operation == 'reconcile':
            fields(value, {'action_id', 'person', 'outcome', 'evidence_file', 'provider_id', 'provider_id_absent_reason', 'note'})
            person(value['person']); text(value['note'], 'Klärungsvermerk'); provider(value)
            orphan = guard_path(folder, action)
            if action['status'] == 'freigegeben' and orphan.exists():
                action['attempts'].append({'number': len(action['attempts']) + 1, 'at': now(), 'recovered_reservation': True})
            elif action['status'] not in {'gestartet', 'wartet_auf_mensch', 'unklar', 'fehlgeschlagen'}:
                raise LaufError('Kein offener oder fehlgeschlagener Versuch zu klären')
            if value['outcome'] not in {'ausgefuehrt', 'nicht_ausgefuehrt'}:
                raise LaufError('Wiederholung erst nach belegter eindeutiger Klärung')
            if value['outcome'] == 'ausgefuehrt' and action['plan']['legal_route'] == 'personal_owner_required' and value['person'] != action['plan']['personal_actor']:
                raise LaufError('Persönliche Ausführung muss die benannte Person bestätigen')
            action['reconciliations'].append(dict(value, evidence=evidence(root, state, action, value['evidence_file']), at=now()))
            action['status'] = 'ausgefuehrt' if value['outcome'] == 'ausgefuehrt' else 'gefroren'
        elif operation == 'receipt':
            fields(value, {'action_id', 'person', 'receipt_status', 'evidence_file', 'provider_id', 'provider_id_absent_reason', 'note'})
            person(value['person']); text(value['note'], 'Empfangsvermerk'); provider(value)
            if action['status'] != 'ausgefuehrt' or value['receipt_status'] not in {'bestaetigt', 'abgelehnt', 'unklar'}:
                raise LaufError('Empfangsprüfung setzt dokumentierte Ausführung voraus')
            action['receipts'].append(dict(value, evidence=evidence(root, state, action, value['evidence_file']), at=now()))
        else:
            raise LaufError('Unbekannter Befehl')
    journal(folder, state, operation, aid)
    return action


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, help='Kanzleiordner; enthält Mandate und das lokale Journal')
    parser.add_argument('command', choices=['init', 'plan', 'freeze', 'approve', 'start', 'result', 'receipt', 'reconcile', 'stop', 'status'])
    parser.add_argument('--input', help='UTF-8-JSON ohne Geheimnisse; status benötigt keine Eingabe')
    args = parser.parse_args(argv)
    try:
        value = json.loads(Path(args.input).read_text(encoding='utf-8')) if args.input else {}
        if not isinstance(value, dict):
            raise LaufError('JSON-Objekt erforderlich')
        with locked(Path(args.root).absolute()) as folder:
            result = execute(Path(args.root).absolute(), folder, args.command, value)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (LaufError, OSError, ValueError, KeyError, TypeError) as exc:
        print('Computerlauf abgebrochen: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
