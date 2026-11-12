#!/usr/bin/env python3
"""Erzeugt native Einkaufsakten mit einem gemeinsamen LV und vier GAEB-Angeboten."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from email import policy
from email.parser import BytesParser
import importlib.util
from io import BytesIO
import json
from pathlib import Path
import re
from zipfile import ZipFile

from bauunternehmer_einkauf_gaeb import amount, build_exchange, exchange_documents, item_total, net_total, verify_exchange


SCRIPTS = Path(__file__).resolve().parent
RUNTIME = Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies'
TENDER = Path('Grundakte/03_Leistungsverzeichnis')
BIDS = Path('Grundakte/04_Angebote')


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def money(value):
    return f'{value:,.2f}'.translate(str.maketrans({',': '.', '.': ','}))


def display(value):
    return str(value).replace('.', ',')


def date(value):
    return datetime.fromisoformat(value).strftime('%d.%m.%Y')


def make_tender(case):
    stem = f"LV_{case['lv_number']}"
    sections = [{'heading': 'Angebotsgrundlagen', 'paragraphs': case['lv_notes']}]
    sections.append({'heading': 'Positionsübersicht', 'table': {
        'headers': ['OZ', 'Leistung', 'Menge', 'Einheit'],
        'rows': [[p['oz'], p['short'], display(p['quantity']), p['unit']] for p in case['positions']],
    }})
    for group, label in case.get('groups', {'': 'Leistungsbeschreibung'}).items():
        positions = [p for p in case['positions'] if p['oz'].partition('.')[0] == group or group == '']
        sections.append({'heading': label, 'paragraphs': [
            f"{p['oz']} {p['short']} ({display(p['quantity'])} {p['unit']}). {p['text']}"
            for p in positions
        ]})
    yield {'filename': str(TENDER / f'{stem}.pdf'), 'title': f"Leistungsverzeichnis {case['lv_number']}",
           'issuer': case['company'], 'date': case['tender_date'], 'sections': sections}
    for offer in case['offers']:
        yield {'filename': str(TENDER / f"Anfrage_{offer['id']}.eml"),
               'from_name': case.get('buyer_name', 'Projekteinkauf Krimpfort'), 'from_email': case['buyer_email'],
               'to_email': offer['email'], 'date': case.get('request_date', case['tender_date'] + 'T09:00:00+01:00'),
               'subject': case.get('request_subject', f"Angebotsanfrage {case['lv_number']}"),
               'paragraphs': [f"Guten Tag {offer['person']},", *case.get('request_paragraphs', [
                   f"Bitte senden Sie uns Ihr Angebot zum beigefügten Leistungsverzeichnis {case['lv_number']} "
                   f"bis {date(case['bid_deadline'])} als X84 und mit einem unterzeichneten Preisblatt.",
                   'Bitte weisen Sie Abweichungen, Vorbehalte, Montagegrenzen und etwaige Zusatzpreise gesondert aus.',
               ]), f"Freundliche Grüße\n{case.get('buyer_name', 'Projekteinkauf Krimpfort')}"],
               'attachments': [str(TENDER / f'{stem}.{extension}') for extension in ('pdf', 'x83')]}


def make_bids(case):
    for offer in case['offers']:
        stem = f"{offer['id']}_{offer['number']}"
        lines = []
        for p in case['positions']:
            unit_price = amount(offer['prices'][p['oz']])
            lines.append([p['oz'], f"{display(p['quantity'])} {p['unit']}", money(unit_price), money(item_total(p, offer))])
        price = {'heading': 'Preisblatt', 'table': {'headers': ['OZ', 'Menge', 'EP netto EUR', 'Gesamt netto EUR'],
                                                   'rows': lines + [['Nettosumme', '', '', money(net_total(case, offer))]]}}
        terms = {'heading': 'Bezugsstand und Bindung', 'paragraphs': [
            f"Grundlage ist das LV {case['lv_number']} vom {date(case['tender_date'])}. "
            f"Die genannten Preise verstehen sich zuzüglich Umsatzsteuer. Wir halten dieses Angebot bis zum "
            f"{date(offer['validity'])} aufrecht. Für die Ausführung gelten die nachstehenden Angaben.",
        ]}
        deviations = [{'heading': 'Anmerkungen zu Positionen', 'paragraphs': [
            f'{oz} {note}' for oz, note in offer['notes'].items()
        ]}] if offer.get('notes') else []
        yield {'filename': str(BIDS / f'{stem}.pdf'), 'title': f"Angebot {offer['number']}", 'issuer': offer['name'],
               'date': offer['date'][:10], 'sections': [terms, price, *deviations, *offer['conditions'], {
                   'heading': 'Rückfragen', 'paragraphs': [f"{offer['person']} · {offer['email']}"]}]}
        yield {'filename': str(BIDS / f'{stem}.eml'), 'subject': offer.get('subject', f"Angebot {offer['number']}"),
               'from_name': offer['person'], 'from_email': offer['email'], 'to_email': case['buyer_email'],
               'date': offer['date'], 'reply_to': str(TENDER / f"Anfrage_{offer['id']}.eml"),
               'paragraphs': offer.get('email_body', [
                   'Guten Tag,', f"anbei senden wir Ihnen Angebot {offer['number']} und den zugehörigen GAEB-Export "
                   f"zum LV {case['lv_number']}. Für Rückfragen erreichen Sie mich unter dieser Adresse.",
                   f"Mit freundlichen Grüßen\n{offer['person']}",
               ]), 'attachments': [str(BIDS / f'{stem}.{extension}') for extension in ('pdf', 'x84')]}


def build(case, output, schema, fonts, node, node_modules, previews):
    if not re.fullmatch(r'bauunternehmer-einkauf-[a-z0-9-]+', case['slug']):
        raise ValueError(f"Ungültiger Aktenname {case['slug']}")
    writer = load_script('build-projekteinkauf-baubranche-akten')
    font_paths = writer.set_fonts(fonts)
    directory = output / 'testakten' / case['slug']
    exchange_paths = build_exchange(case, directory, schema)
    records = [*case['documents'], *make_tender(case), *make_bids(case)]
    names = {r['filename'] for r in records}
    if len(names) != len(records):
        raise ValueError(f"Doppelte Aktenstücknamen in {case['slug']}")
    names.update(path.as_posix() for path in exchange_paths)
    workbooks, emails = [], []
    for record in records:
        relative = Path(record['filename'])
        if relative.is_absolute() or '..' in relative.parts or relative.parts[0] not in {'Grundakte', 'Nachlauf'}:
            raise ValueError(f'Ungültiger Aktenpfad {relative}')
        target = directory / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        match target.suffix:
            case '.pdf':
                writer.write_pdf(target, record, case)
            case '.docx':
                writer.write_docx(target, record, case)
            case '.png':
                writer.write_png(target, record, font_paths)
            case '.csv':
                with target.open('w', newline='', encoding='utf-8') as stream:
                    csv.writer(stream, lineterminator='\n').writerows(writer.rows(record))
            case '.xlsx':
                for sheet in record['sheets']:
                    writer.rows(sheet)
                workbooks.append({'path': str(target), 'caseId': case['id'], 'sheets': record['sheets']})
            case '.eml':
                if relative.parts[0] == 'Grundakte' and any(Path(a).parts[0] != 'Grundakte' for a in record.get('attachments', [])):
                    raise ValueError(f'Anlage aus späterem Aktenstand in {relative}')
                emails.append((target, record, {**case, 'message_domain': 'krimpfort.example'}, directory, names))
            case _:
                raise ValueError(f'Unbekanntes Format {target.name}')
    if workbooks:
        writer.write_workbooks(workbooks, node, node_modules, previews)
    for args in emails:
        writer.write_eml(*args)
    print(f"{case['id']}: {len(names)} Originale, {len(emails)} E-Mails, {len(workbooks)} Arbeitsmappen")


def build_release(case, directory, dist):
    """Baut eine einzelne Akte in drei Fassungen und gleicht ihre Inhalte ab."""
    from pypdf import PdfReader, PdfWriter
    from testakte_disclaimer import NOTICE_FILENAME, pdf_content_errors
    from testakte_einzelpdf_common import document_arcname_pairs
    from testakte_zip_common import working_dump_archive_pairs

    verify_exchange(case, directory)
    documents = [*case['documents'], *make_tender(case), *make_bids(case)]
    expected = {record['filename'] for record in documents}
    expected.update(path.as_posix() for path, _ in exchange_documents(case))
    native_pairs = working_dump_archive_pairs(directory, include_gesamt_pdf=False)
    pdf_pairs = document_arcname_pairs(directory)
    if {name for _, name in native_pairs} != expected:
        raise ValueError(f"{case['id']}: Abweichung im Originalbestand")
    if {source.relative_to(directory).as_posix() for source, _ in pdf_pairs} != expected:
        raise ValueError(f"{case['id']}: Lesefassung umfasst nicht den vollständigen Aktenbestand")

    dist.mkdir(parents=True, exist_ok=True)
    native, count = load_script('build-testakten-release-zips').build_single(directory, dist)
    individual, pdf_count = load_script('build-testakten-einzelpdf-zips').build_single(directory, dist)
    if count != len(expected) + 1 or pdf_count != len(expected):
        raise ValueError(f"{case['id']}: Unvollständiger ZIP-Bestand")
    native_validator = load_script('validate-testakten-release-zips')
    native_validator.assert_same(native.name, [NOTICE_FILENAME, *expected],
                                 native_validator.zip_entries(native, require_notice=True, allow_directories=True))
    pdf_validator = load_script('validate-testakten-einzelpdf-zips')
    pdf_validator.assert_same(individual.name, [NOTICE_FILENAME, *(name for _, name in pdf_pairs)],
                               pdf_validator.zip_entries(individual, expected_suffix='.pdf', allow_directories=True))

    with ZipFile(native) as archive:
        for source, name in native_pairs:
            if archive.read(name) != source.read_bytes():
                raise ValueError(f'Archivdatei stimmt nicht mit Original überein: {name}')
        for record in documents:
            name = record['filename']
            if not name.endswith('.eml'):
                continue
            message = BytesParser(policy=policy.default).parsebytes(archive.read(name))
            attachments = [(part.get_filename(), part.get_payload(decode=True)) for part in message.iter_attachments()]
            source_bytes = [(Path(path).name, archive.read(path)) for path in record.get('attachments', [])]
            if attachments != source_bytes:
                raise ValueError(f'Anlagen stimmen nicht mit Original überein: {name}')

    writer = PdfWriter()
    writer.add_metadata({'/Title': case['title'], '/Author': case['company'], '/Subject': case['project']})
    sections = {}
    with ZipFile(individual) as archive:
        for source, name in pdf_pairs:
            part = Path(name).parts[0]
            start = len(writer.pages)
            pdf = PdfReader(BytesIO(archive.read(name)))
            for page in pdf.pages:
                writer.add_page(page)
            if part not in sections:
                sections[part] = writer.add_outline_item(part, start)
            writer.add_outline_item(source.relative_to(directory).as_posix(), start, parent=sections[part])
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    content = BytesIO()
    writer.write(content)
    data = content.getvalue()
    if problems := pdf_content_errors(data):
        raise ValueError(f"{case['id']}: {problems}")
    combined = directory / 'gesamt-pdf' / f"{case['slug']}_gesamt.pdf"
    combined.parent.mkdir(exist_ok=True)
    temporary = combined.with_suffix('.tmp')
    temporary.write_bytes(data)
    temporary.replace(combined)
    (dist / combined.name).write_bytes(data)
    print(f"{case['id']}: {pdf_count} Originale, {len(writer.pages)} PDF-Seiten, {dist}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='Falldaten unter scripts/data')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--schema-zip', type=Path)
    parser.add_argument('--release-only', type=Path, metavar='DIST',
                        help='Baut ZIPs und Gesamt-PDF aus vorhandenen Originalen im Ausgabeverzeichnis')
    parser.add_argument('--fonts', type=Path, default=Path('/System/Library/Fonts/Supplemental'))
    parser.add_argument('--node', type=Path, default=RUNTIME / 'node/bin/node')
    parser.add_argument('--node-modules', type=Path, default=RUNTIME / 'node/node_modules')
    parser.add_argument('--xlsx-previews', type=Path)
    args = parser.parse_args()
    case = json.loads(args.source.read_text(encoding='utf-8'))
    if args.release_only:
        build_release(case, args.output.resolve() / 'testakten' / case['slug'], args.release_only.resolve())
    else:
        if args.schema_zip is None:
            parser.error('--schema-zip wird für die Originale benötigt')
        build(case, args.output.resolve(), args.schema_zip, args.fonts, args.node, args.node_modules, args.xlsx_previews)
