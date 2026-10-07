#!/usr/bin/env python3
"""Lokales Mandatsjournal und abgeleitete Honorarentwürfe. Python >= 3.10, stdlib.

Keine Netzwerkaufrufe, keine Fristenberechnung, kein Versand, keine Finanzbuchung.
Das SQLite-Journal ist führend; draft erzeugt die lesbaren Ansichten erneut.
"""
import argparse
import csv
import hashlib
import io
import json
import os
import re
import sqlite3
import sys
import tempfile
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

MODELS = {'hourly', 'capped', 'estimate', 'flat', 'rvg'}
LABELS = {'hourly': 'Zeithonorar', 'capped': 'Zeithonorar mit Deckel',
          'estimate': 'Zeithonorar mit unverbindlicher Schätzung',
          'flat': 'Festpreis', 'rvg': 'RVG-Einzelberechnung'}
CENT = Decimal('0.01')


def canonical(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def require_text(data, *keys):
    for key in keys:
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key}: Text fehlt')
        if any(ord(c) < 32 for c in data[key]):
            raise ValueError(f'{key}: Steuerzeichen nicht zulässig')


def valid_id(value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,79}', value):
        raise ValueError('ID: 1 bis 80 Buchstaben/Ziffern/Punkt/Bindestrich/Unterstrich erforderlich')


def number(value, label, *, allow_zero=True):
    if isinstance(value, bool) or value is None:
        raise ValueError(f'{label}: Zahl fehlt')
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f'{label}: ungültige Zahl') from None
    if not result.is_finite() or result < 0 or (not allow_zero and result == 0):
        raise ValueError(f'{label}: nichtnegative endliche Zahl erforderlich')
    return result


def money(value, label):
    amount = number(value, label)
    if amount != amount.quantize(CENT):
        raise ValueError(f'{label}: höchstens zwei Nachkommastellen')
    return amount


def euros(value):
    return str(value.quantize(CENT, rounding=ROUND_HALF_UP))


def confirmed(data):
    if type(data.get('confirmed')) is not bool:
        raise ValueError('confirmed muss ausdrücklich true oder false sein')


def valid_date(data, key):
    require_text(data, key)
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', data[key]):
        raise ValueError(f'{key}: Datum YYYY-MM-DD erforderlich')
    date.fromisoformat(data[key])


def connect(folder, create=False):
    folder = Path(folder).expanduser().resolve()
    db = folder / '00_Mandat' / 'mandatsjournal.sqlite'
    if not create and not db.is_file():
        raise ValueError('Mandat nicht angelegt; zuerst init ausführen')
    if create:
        for name in ('00_Mandat', '01_Bearbeitung', '02_Honorar', '03_beA_Vorbereitung'):
            (folder / name).mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db, timeout=20)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA foreign_keys=ON')
    if create:
        con.executescript('''
        CREATE TABLE IF NOT EXISTS matter (singleton INTEGER PRIMARY KEY CHECK(singleton=1), data TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS terms (id TEXT PRIMARY KEY, data TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS entries (id TEXT PRIMARY KEY, kind TEXT NOT NULL, terms_id TEXT REFERENCES terms(id), data TEXT NOT NULL, void_reason TEXT);
        CREATE TABLE IF NOT EXISTS journal (seq INTEGER PRIMARY KEY AUTOINCREMENT, stamp TEXT NOT NULL, action TEXT NOT NULL, item_id TEXT NOT NULL, payload TEXT NOT NULL);
        ''')
    return folder, con


def event(con, action, item_id, payload):
    con.execute('INSERT INTO journal(stamp,action,item_id,payload) VALUES(?,?,?,?)',
                (datetime.now(timezone.utc).isoformat(), action, item_id, canonical(payload)))


def init(con, data):
    require_text(data, 'matter_id', 'client', 'subject')
    valid_id(data['matter_id'])
    old = con.execute('SELECT data FROM matter WHERE singleton=1').fetchone()
    if old:
        if old['data'] != canonical(data):
            raise ValueError('Dieser Ordner gehört bereits zu einem anderen oder abweichend beschriebenen Mandat')
        return 'Unverändert; Mandat schon vorhanden'
    con.execute('INSERT INTO matter VALUES(1,?)', (canonical(data),))
    event(con, 'init', data['matter_id'], data)
    return 'Mandat angelegt'


def add_terms(con, data):
    require_text(data, 'id', 'model', 'scope', 'agreement_ref')
    valid_id(data['id']); confirmed(data)
    if data['model'] not in MODELS:
        raise ValueError('model: hourly, capped, estimate, flat oder rvg erforderlich')
    fields = {'hourly': ['rate_eur'], 'capped': ['rate_eur', 'cap_eur'],
              'estimate': ['rate_eur', 'estimate_eur'], 'flat': ['flat_eur'], 'rvg': []}
    for key in fields[data['model']]:
        if data.get(key) is not None or data['confirmed']:
            money(data.get(key), key)
    if data['model'] == 'capped' and data.get('cap_scope') not in ('fees_only', 'fees_and_expenses'):
        raise ValueError('Deckelumfang fehlt: cap_scope=fees_only oder fees_and_expenses; alle Beträge netto')
    # This local calculator deliberately supports only ordinary domestic 19% VAT.
    # Other tax cases belong to a separately checked calculation, not a silent default.
    if number(data.get('vat_rate'), 'vat_rate') != Decimal('19'):
        raise ValueError('Lokale Rechenhilfe: nur ausdrücklich bestätigte inländische 19%-Umsätze; Sonderfall gesondert berechnen')
    old = con.execute('SELECT data FROM terms WHERE id=?', (data['id'],)).fetchone()
    if old and old['data'] == canonical(data):
        return 'Unverändert; Honorargrundlage schon vorhanden'
    if old:
        if json.loads(old['data'])['confirmed'] and con.execute('SELECT 1 FROM entries WHERE terms_id=? LIMIT 1', (data['id'],)).fetchone():
            raise ValueError('Honorargrundlage bereits verwendet. Keine rückwirkende Umbewertung; neue klar abgegrenzte Phase anlegen')
        con.execute('UPDATE terms SET data=? WHERE id=?', (canonical(data), data['id']))
    else:
        con.execute('INSERT INTO terms VALUES(?,?)', (data['id'], canonical(data)))
    event(con, 'terms', data['id'], data)
    return 'Honorargrundlage gespeichert'


def add_entry(con, kind, data):
    # Missing pending time fields are unknown, not zero. Normalize before the
    # idempotency comparison so omitted and explicit null values are equivalent.
    data = dict(data)
    if kind == 'time':
        data.setdefault('minutes', None)
        data.setdefault('billable', None)
    require_text(data, 'id', 'source'); valid_id(data['id']); confirmed(data)
    tid = None
    if kind != 'payment' and not (kind == 'time' and not data.get('terms_id')):
        require_text(data, 'terms_id'); tid = data['terms_id']
        row = con.execute('SELECT data FROM terms WHERE id=?', (tid,)).fetchone()
        if not row:
            raise ValueError('Unbekannte Honorargrundlage')
        terms = json.loads(row['data'])
    if kind == 'time':
        require_text(data, 'person', 'narrative'); valid_date(data, 'work_date')
        if data.get('billable') is not None and type(data['billable']) is not bool:
            raise ValueError('billable: true, false oder null erforderlich')
        if data.get('minutes') is not None:
            minutes = number(data['minutes'], 'minutes')
            if minutes != int(minutes) or minutes > 1440:
                raise ValueError('minutes: ganze tatsächliche Minuten zwischen 0 und 1440')
        if data['confirmed'] and (data.get('minutes') is None or data.get('billable') is None):
            raise ValueError('Bestätigte Zeit benötigt Dauer und Abrechenbarkeit')
        if data['confirmed']:
            previous = con.execute("SELECT data FROM entries WHERE kind='time' AND void_reason IS NULL").fetchall()
            total = sum(int(json.loads(r['data']).get('minutes') or 0) for r in previous
                        if json.loads(r['data']).get('confirmed') and json.loads(r['data'])['person'] == data['person']
                        and json.loads(r['data'])['work_date'] == data['work_date']
                        and json.loads(r['data'])['id'] != data['id'])
            if total + int(data['minutes']) > 1440:
                raise ValueError('Mehr als 1440 Minuten für dieselbe Person am selben Tag')
    elif kind in ('expense', 'manual-fee'):
        valid_date(data, 'date'); require_text(data, 'description'); money(data.get('net_eur'), 'net_eur')
        if kind == 'manual-fee' and (terms['model'] != 'rvg' or data.get('legal_reviewed') is not True):
            raise ValueError('manual-fee nur für gesondert rechtlich geprüfte RVG-Berechnung')
        if kind == 'expense' and data.get('tax_classification') != 'own_taxable':
            raise ValueError('Auslagenhilfe nur für eigene steuerpflichtige Leistung; tax_classification=own_taxable ausdrücklich bestätigen')
    elif kind == 'payment':
        valid_date(data, 'date'); require_text(data, 'reference', 'kind'); money(data.get('gross_eur'), 'gross_eur')
        if data['kind'] not in ('payment', 'advance', 'third_party'):
            raise ValueError('Zahlungsart payment, advance oder third_party erforderlich')
    else:
        raise ValueError('Unbekannter Buchungstyp')
    old = con.execute('SELECT kind,data,void_reason FROM entries WHERE id=?', (data['id'],)).fetchone()
    if old:
        if old['kind'] == kind and old['data'] == canonical(data) and old['void_reason'] is None:
            return 'Unverändert; identische Buchung schon vorhanden'
        raise ValueError('ID bereits verwendet. Korrektur: alte Buchung mit Begründung stornieren und neue ID verwenden')
    con.execute('INSERT INTO entries(id,kind,terms_id,data) VALUES(?,?,?,?)', (data['id'], kind, tid, canonical(data)))
    event(con, kind, data['id'], data)
    return 'Buchung gespeichert; Entwurf fortgeschrieben'


def void(con, item_id, reason):
    require_text({'reason': reason}, 'reason')
    row = con.execute('SELECT void_reason FROM entries WHERE id=?', (item_id,)).fetchone()
    if not row:
        raise ValueError('Buchung nicht gefunden')
    if row['void_reason']:
        if row['void_reason'] == reason:
            return 'Unverändert; Buchung bereits storniert'
        raise ValueError('Buchung bereits mit anderer Begründung storniert')
    con.execute('UPDATE entries SET void_reason=? WHERE id=?', (reason, item_id))
    event(con, 'void', item_id, {'reason': reason})
    return 'Buchung storniert; Historie bleibt erhalten'


def snapshot(con):
    matter = con.execute('SELECT data FROM matter WHERE singleton=1').fetchone()
    if not matter:
        raise ValueError('Mandatsstammdaten fehlen')
    data = {'matter': json.loads(matter['data']), 'status': 'Entwurf, keine ausgestellte Rechnung',
            'phases': [], 'payments': [], 'open_items': [], 'entries': [], 'notices': []}
    terms = {r['id']: json.loads(r['data']) for r in con.execute('SELECT * FROM terms ORDER BY id')}
    entries = [dict(r) for r in con.execute('SELECT * FROM entries ORDER BY rowid')]
    for entry in entries:
        entry['data'] = json.loads(entry['data'])
        data['entries'].append(entry)
    net_total = Decimal(0)
    for tid, term in terms.items():
        selected = [r for r in entries if r['terms_id'] == tid and not r['void_reason']]
        amount = Decimal(0); minutes = 0; manual = Decimal(0); expenses = Decimal(0)
        for entry in selected:
            row = entry['data']
            if not row['confirmed']:
                data['open_items'].append(f"{row['id']}: Bestätigung, Zeit oder Abrechenbarkeit offen")
                continue
            if entry['kind'] == 'time' and row['billable']:
                minutes += int(row['minutes'])
                if term['confirmed'] and term['model'] in ('hourly', 'capped', 'estimate'):
                    amount += (Decimal(row['minutes']) * money(term['rate_eur'], 'rate_eur') / 60).quantize(CENT, rounding=ROUND_HALF_UP)
            if entry['kind'] == 'manual-fee':
                manual += money(row['net_eur'], 'net_eur')
            if entry['kind'] == 'expense':
                expenses += money(row['net_eur'], 'net_eur')
        raw = amount
        raw_expenses = expenses
        expenses_above_cap = Decimal(0)
        if not term['confirmed']:
            pass
        elif term['model'] == 'flat':
            amount = money(term['flat_eur'], 'flat_eur')
            data['notices'].append(f'{tid}: Festpreis ist Vereinbarungswert; Leistungsstand und Fälligkeit vor Rechnungsstellung prüfen')
        elif term['model'] == 'capped':
            ceiling = money(term['cap_eur'], 'cap_eur')
            if term['cap_scope'] == 'fees_and_expenses':
                expenses_above_cap = max(expenses - ceiling, Decimal(0))
                expenses = min(expenses, ceiling)
                ceiling -= expenses
                if expenses_above_cap:
                    data['notices'].append(f'{tid}: {euros(expenses_above_cap)} EUR Auslagenwert oberhalb des gemeinsamen Deckels nicht angesetzt; tatsächliche Auslagen bleiben dokumentiert')
            amount = min(amount, ceiling)
            if raw > amount:
                data['notices'].append(f'{tid}: {euros(raw-amount)} EUR Zeitwert oberhalb des Deckels nicht angesetzt')
        elif term['model'] == 'estimate' and amount > money(term['estimate_eur'], 'estimate_eur'):
            data['notices'].append(f'{tid}: Schätzung überschritten; Kosteninformation und weiteren Auftrag klären')
        elif term['model'] == 'rvg':
            amount = manual
            if not any(r['kind'] == 'manual-fee' and r['data']['confirmed'] for r in selected):
                data['open_items'].append(f'{tid}: RVG-Berechnung fehlt; Zeiten ergeben keine RVG-Gebühr')
        if not term['confirmed']:
            data['open_items'].append(f'{tid}: Honorargrundlage nicht bestätigt; Betrag nicht übernommen')
            phase_net = None
        else:
            phase_net = amount + expenses
            net_total += phase_net
        data['phases'].append({'id': tid, 'model': term['model'], 'scope': term['scope'],
                               'minutes': minutes, 'time_value_eur': euros(raw),
                               'fee_eur': euros(amount), 'expenses_eur': euros(expenses),
                               'expenses_value_eur': euros(raw_expenses),
                               'expenses_above_cap_eur': euros(expenses_above_cap),
                               'net_eur': euros(phase_net) if phase_net is not None else None,
                               'agreement_ref': term['agreement_ref']})
    for entry in entries:
        if entry['kind'] == 'payment' and not entry['void_reason']:
            data['payments'].append(entry['data'])
        if entry['kind'] == 'time' and not entry['void_reason'] and entry['terms_id'] is None:
            data['open_items'].append(f"{entry['id']}: Zeit erfasst, Honorarzuordnung offen")
    if not terms:
        data['open_items'].append('Honorargrundlage fehlt')
    if data['payments']:
        data['notices'].append('Zahlungen getrennt erfasst und noch nicht verrechnet; Rechnungszuordnung, Vorschusssteuer und Fremdgeld separat prüfen')
    vat = (net_total * Decimal('0.19')).quantize(CENT, rounding=ROUND_HALF_UP)
    data['known_net_eur'] = euros(net_total)
    data['known_vat_eur'] = euros(vat)
    data['known_gross_eur'] = euros(net_total + vat)
    data['complete'] = not data['open_items']
    data['invoice_ready'] = False
    data['journal_revision'] = con.execute('SELECT COALESCE(MAX(seq),0) FROM journal').fetchone()[0]
    data['notices'].append('Keine automatische Rechnungsnummer, keine Buchung im Hauptbuch, kein Versand. Vorsteuer, Fälligkeit und Gebührenrecht werden hier nicht entschieden.')
    return data


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as stream:
            stream.write(content); stream.flush(); os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def clean_cell(value):
    value = '' if value is None else str(value)
    return "'" + value if value[:1] in ('=', '+', '-', '@', '\t', '\r') else value


def export(folder, data):
    out = folder / '02_Honorar'
    text = [f"# Rechnungsentwurf – {data['matter']['matter_id']}", '',
            f"Mandantschaft: {data['matter']['client']}", '',
            f"Gegenstand: {data['matter']['subject']}", '',
            f"Journalstand: {data['journal_revision']}. Keine ausgestellte Rechnung.", '',
            '## 1. Bekannter Honorarstand', '']
    for row in data['phases']:
        value = row['net_eur'] if row['net_eur'] is not None else 'offen'
        text.extend([f"{row['id']} – {LABELS[row['model']]}: {row['scope']}. "
                     f"Bestätigte abrechenbare Minuten: {row['minutes']}. Netto: {value} EUR. "
                     f"Belegter Auslagenwert: {row['expenses_value_eur']} EUR; im Entwurf angesetzt: {row['expenses_eur']} EUR. "
                     f"Grundlage: {row['agreement_ref']}.", ''])
    text.extend([f"Bekannter Teilbetrag netto: {data['known_net_eur']} EUR. "
                 f"Umsatzsteuer 19 %: {data['known_vat_eur']} EUR. "
                 f"Bekannter Teilbetrag brutto: {data['known_gross_eur']} EUR.", '',
                 'Offene Positionen verhindern einen vollständigen Rechnungsstand.' if data['open_items'] else 'Erfasste Positionen rechnerisch vollständig; rechtliche Rechnungsprüfung steht aus.', '',
                 '## 2. Offene Angaben', ''])
    text += [item + '\n' for item in data['open_items']] or ['Keine offenen Erfassungsangaben.\n']
    text += ['## 3. Zahlungsnotizen und nächste Prüfung', '']
    text += [f"{p['id']}: {p['gross_eur']} EUR, {p['kind']}, {p['reference']}; Bestätigung: {p['confirmed']}.\n" for p in data['payments']]
    text += [item + '\n' for item in data['notices']]
    buf = io.StringIO(newline=''); writer = csv.writer(buf, delimiter=';')
    writer.writerow(['ID', 'Honorarphase', 'Datum', 'Person', 'Minuten', 'Narrativ', 'Abrechenbar', 'Bestätigt', 'Stornogrund'])
    for entry in data['entries']:
        if entry['kind'] != 'time':
            continue
        row = entry['data']
        writer.writerow([clean_cell(v) for v in [row['id'], row.get('terms_id'), row['work_date'], row['person'], row.get('minutes'), row['narrative'], row.get('billable'), row['confirmed'], entry['void_reason']]])
    atomic_write(out / 'rechnungsentwurf.md', '\n'.join(text).rstrip() + '\n')
    atomic_write(out / 'zeiten.csv', buf.getvalue())
    # JSON is written last; revision identifies a stale earlier view after interruption.
    atomic_write(out / 'rechnungsentwurf.json', json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['init', 'terms', 'time', 'expense', 'payment', 'manual-fee', 'void', 'status', 'draft'])
    parser.add_argument('--akte', required=True)
    parser.add_argument('--data', type=Path)
    parser.add_argument('--id')
    parser.add_argument('--reason')
    args = parser.parse_args(argv)
    data = None
    if args.command in ('init', 'terms', 'time', 'expense', 'payment', 'manual-fee'):
        if not args.data:
            parser.error('--data erforderlich')
        data = json.loads(args.data.read_text(encoding='utf-8'))
        if not isinstance(data, dict):
            raise ValueError('--data benötigt ein JSON-Objekt')
    folder, con = connect(args.akte, create=args.command == 'init')
    try:
        con.execute('BEGIN IMMEDIATE')
        if args.command == 'init':
            message = init(con, data)
        elif args.command == 'terms':
            message = add_terms(con, data)
        elif args.command == 'void':
            message = void(con, args.id, args.reason)
        elif args.command in ('status', 'draft'):
            message = 'Aktueller Journalstand'
        else:
            message = add_entry(con, args.command, data)
        view = snapshot(con)
        # Keep the write lock while producing views, so concurrent writers cannot
        # publish an older snapshot after a newer one. SQLite remains authoritative.
        con.commit()
        con.execute('BEGIN IMMEDIATE')
        view = snapshot(con)
        if args.command != 'status':
            export(folder, view)
        con.commit()
        print(json.dumps({'message': message, 'matter_id': view['matter']['matter_id'],
                          'journal_revision': view['journal_revision'], 'complete': view['complete'],
                          'known_gross_eur': view['known_gross_eur'], 'open_items': view['open_items'],
                          'invoice_ready': False}, ensure_ascii=False))
    finally:
        con.close()


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(f'Fehler: {exc}', file=sys.stderr)
        sys.exit(2)
