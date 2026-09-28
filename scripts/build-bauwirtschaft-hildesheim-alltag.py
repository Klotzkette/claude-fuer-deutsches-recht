#!/usr/bin/env python3
"""Alltagskorrespondenz der Hildesheimer Projektakte. Autor: Klotzkette."""
from __future__ import annotations

from datetime import datetime
from email import policy
from email.headerregistry import Address
from email.message import EmailMessage
from email.utils import format_datetime
import hashlib
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo

from bauwirtschaft_hildesheim_lebensakte_common import (
    ROOT, CASE, QUALITY, ACTORS, REF, new_document, save_docx,
)

DATA = ROOT / 'scripts/data'
GROUPS = ('bau', 'menschen', 'kaufmaennisch')
FOLDERS = {
    '08_Bauausfuehrung/05_Alltagskorrespondenz',
    '11_Vermietung/Alltagskorrespondenz',
    '00_Projektsteuerung/Alltagskorrespondenz',
    '10_Rechnungen_und_Buchhaltung/Alltagskorrespondenz',
}


def person(record, role):
    key = record.get(role + '_key')
    if key:
        actor = ACTORS[key]
        return record.get(role + '_name', actor[3]), record.get(role + '_email', actor[2])
    return record[role + '_name'], record[role + '_email']


def address(pair):
    name, email = pair
    if not email.endswith('.example'):
        raise ValueError('Fiktive Projektkontakte brauchen reservierte Adressen: ' + email)
    return Address(display_name=name, addr_spec=email)


def stamp(record):
    return datetime.fromisoformat(record['date']).replace(tzinfo=ZoneInfo('Europe/Berlin'))


def message_id(record):
    return '<sw-hi-alltag-' + record['id'].lower() + '@' + person(record, 'from')[1].split('@')[1] + '>'


def filename(record):
    title = record['title'].translate(str.maketrans({'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue', 'ß': 'ss'}))
    title = re.sub(r'[^A-Za-z0-9]+', '_', title).strip('_')[:72].rstrip('_')
    return f"{record['folder']}/{record['date'][:10]}_{record['id']}_{title}.{record['format']}"


def read_records():
    records = [record for group in GROUPS for record in json.loads((DATA / f'hildesheim-alltag-{group}.json').read_text())]
    records.sort(key=lambda r: (r['date'], r['id']))
    by_id = {}
    paths = set()
    for record in records:
        if record['id'] in by_id or record['folder'] not in FOLDERS or record['format'] not in {'eml', 'docx'}:
            raise ValueError('Ungültiger Vorgang: ' + record['id'])
        for role in ('from', 'to'):
            address(person(record, role))
        stamp(record)
        if not record['paragraphs'] or any(not isinstance(p, str) or not p.strip() for p in record['paragraphs']):
            raise ValueError('Leerer Dokumenttext: ' + record['id'])
        for source in record['references']:
            relative = Path(source)
            if relative.is_absolute() or '..' in relative.parts or not (CASE / relative).is_file():
                raise ValueError('Unbekannter Bestandsbezug: ' + source)
        previous = record.get('reply_to')
        if previous:
            parent = by_id[previous]
            if parent['thread'] != record['thread'] or stamp(parent) >= stamp(record):
                raise ValueError('Antwort gehört nicht zu einem früheren Stand desselben Vorgangs: ' + record['id'])
        target = filename(record)
        if target.casefold() in paths:
            raise ValueError('Doppelter Ausgabepfad: ' + target)
        paths.add(target.casefold())
        by_id[record['id']] = record
    return records, by_id


def make_mail(record, by_id):
    mail = EmailMessage(policy=policy.SMTP)
    mail['From'] = address(person(record, 'from'))
    mail['To'] = address(person(record, 'to'))
    if record.get('cc_keys'):
        mail['Cc'] = tuple(address((ACTORS[key][3], ACTORS[key][2])) for key in record['cc_keys'])
    mail['Date'] = format_datetime(stamp(record))
    mail['Subject'] = REF + ' / ' + record['title']
    mail['Message-ID'] = message_id(record)
    mail['Content-Language'] = 'de-DE'
    chain = []
    previous = record.get('reply_to')
    while previous:
        ancestor = by_id[previous]
        if ancestor['format'] == 'eml':
            chain.insert(0, message_id(ancestor))
        previous = ancestor.get('reply_to')
    if chain:
        mail['In-Reply-To'] = chain[-1]
        mail['References'] = ' '.join(chain)
    mail.set_content('\n\n'.join(record['paragraphs']) + '\n', charset='utf-8')
    target = CASE / filename(record)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(mail.as_bytes())
    return target


def make_word(record):
    document = new_document(record['title'], record['date'])
    document.add_paragraph('Hildesheim, ' + stamp(record).strftime('%d.%m.%Y, %H:%M Uhr'))
    document.add_paragraph('Verfasst von: ' + person(record, 'from')[0])
    document.add_paragraph('Adressiert an: ' + person(record, 'to')[0])
    if record.get('cc_keys'):
        document.add_paragraph('Zur Kenntnis: ' + '; '.join(ACTORS[key][3] for key in record['cc_keys']))
    for paragraph in record['paragraphs']:
        document.add_paragraph(paragraph)
    return save_docx(document, filename(record))


def main():
    records, by_id = read_records()
    manifest = []
    for record in records:
        target = make_mail(record, by_id) if record['format'] == 'eml' else make_word(record)
        manifest.append({
            'id': record['id'], 'thread': record['thread'], 'date': record['date'],
            'source': target.relative_to(CASE).as_posix(),
            'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
            'reply_to': record.get('reply_to'), 'references': record['references'],
        })
    (QUALITY / 'alltag-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(manifest)} neue Originale in {len({r["thread"] for r in records})} zusammenhängenden Vorgängen.')


if __name__ == '__main__':
    main()
