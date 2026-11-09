#!/usr/bin/env python3
"""Erzeugt X83/X84 für das Türpaket und prüft sie gegen die offiziellen GAEB-Schemata."""
from __future__ import annotations

import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
from xml.etree import ElementTree as ET
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'scripts/data/projekteinkauf-baubranche-c.json'
SCHEMA_URL = 'https://www.gaeb.de/wp-content/uploads/2021/06/2021-05_Leistungsverzeichnis.zip'
SCHEMA_SHA256 = 'd4f19a79c46119ba6a7bbca1067bc2a26ccadb60d1b5fd8a82725f45b491e203'
VERSION = '3.3'
ISSUE = '2021-05'
PROJECT_ID = 'c7fac11ec8cb4f7fa94aa8a5a3a49572'
BOQ_ID = 'a20129eea8424283b909acb66fb97451'
BOQ_NAME = 'KPF-WB-31'
X83 = '31_Tuerpaket_LV_R1.x83'
BIDS = {
    'A': ('33_A_Emswiek_ET-26-241.x84', '08_Angebot_A_Emswiek.pdf', '14_A_Nachtragsmail.eml'),
    'B': ('35_B_Weserfalz_WF-702.x84', '09_Angebot_B_Weserfalz.pdf', '16_B_Nachweismail.eml'),
    'C': ('37_C_Jadeholm_JH-WB-26.x84', '10_Angebot_C_Jadeholm.pdf', '19_C_Qualitaetsmail.eml'),
    'D': ('39_D_Friesenlint_FL-500.x84', '11_Angebot_D_Friesenlint.pdf', '22_D_Familienmail.eml'),
}
POSITION_TEXTS = {
    'B1': (
        'B1 · Büro- und Besprechungsraumtür',
        'Einflügelig, feuerhemmend und selbstschließend. Das angebotene Türelement muss im '
        'jeweiligen Aufbau ein belegtes Rw von mindestens 32 dB erreichen.',
    ),
    'B2': (
        'B2 · Bürotür mit automatischem Antrieb',
        'Einflügelig, feuerhemmend und selbstschließend. Antrieb einschließlich Befestigung, '
        'Steuerung, Sicherheitseinrichtungen, Tastern, elementseitigen Anschlüssen, Parametrierung '
        'und Inbetriebnahme. Die 40 Türen in W-M und zehn Türen an der Sonderwand W-S '
        '(E4-073 bis E4-082) erfordern je einen Nachweis für das vollständige System.',
    ),
    'F1': (
        'F1 · Tür im Flurabschluss',
        'Feuerhemmend, rauchdicht und selbstschließend. Rauchschutzdichtungen, Bodenausbildung '
        'und zugeordnete Fluchtwegbeschläge sind einzukalkulieren.',
    ),
    'T1': (
        'T1 · Treppenraumzugang',
        'Feuerhemmend, rauchdicht und selbstschließend. Öffnungsrichtung und Verriegelung '
        'der zugeordneten Fluchtwegbeschläge sind anhand der Werkplanung zu bestätigen.',
    ),
    'S1': (
        'S1 · Technikraumabschluss',
        'Feuerbeständig und selbstschließend. Der Nachweis muss die gewählte Systemkonfiguration '
        'mit Zarge, Befestigung und vorgesehenem Wandtyp abdecken.',
    ),
}
BID_SCOPE = {
    'A': (
        'Materialpreisstand ET-26-241. Die Einheitspreise gelten ausschließlich für die '
        'Warenlieferung. Baustellenfracht und Entladung, Montage, B2-Antriebe und W-S-Einbau '
        'sind in diesem Preisstand nicht enthalten. Ergänzungspreise bleiben gesondert.',
        {'B2': 'B2 wird nur als für den Antrieb vorbereitetes Element angeboten. Der Antrieb '
               'und das Einbaudetail W-S sind in diesem Preisstand nicht enthalten.'},
    ),
    'B': (
        'Grundpreisstand WF-702. Fracht, Montage, alle B2-Antriebe und Inbetriebnahme '
        'sowie W-S-Befestigung sind kalkuliert. Der objektbezogene W-S-Nachweis ist im '
        'Erststand angefordert. Wartung, bedingter Paketnachlass und Skonto siehe Schriftangebot.',
        {'B2': 'W-S-Befestigung für zehn B2 kalkuliert. Der Herstellerabgleich ist angefordert.'},
    ),
    'C': (
        'Paketpreisstand JH-WB-26. Einschließlich Fracht, Montage, W-S-Befestigung, '
        'aller 50 B2-Systemantriebe und Inbetriebnahme. Wartung und bedingter Paketnachlass '
        'siehe Schriftangebot. Die angekündigten Nachweise werden gesondert geliefert.',
        {'B2': 'Alle 50 Antriebe einschließlich zehn W-S-Konfigurationen kalkuliert. '
               'Prüfgrundlage und Zuordnung werden gesondert vorgelegt.'},
    ),
    'D': (
        'Paketpreisstand FL-500. Fracht, Montage und Standard-Automatikpaket für 50 B2 '
        'sind kalkuliert. W-S und die S1-Befestigung sind im Erststand offen. Bedingter '
        'Nachlass und Teilservice siehe Schriftangebot.',
        {
            'B2': 'Standard-Automatikpaket einschließlich Inbetriebnahme. Die vorgeschlagene '
                  'Anpassung an W-S ist im Erststand nicht nachgewiesen.',
            'S1': 'Familienvariante mit Selbstschließer kalkuliert. Befestigungsaufbau bleibt offen.',
        },
    ),
}


def element(parent, name, value=None, **attrs):
    node = ET.SubElement(parent, name, attrs)
    if value is not None:
        node.text = str(value)
    return node


def fields(parent, **values):
    for name, value in values.items():
        element(parent, name, value)


def text(parent, value):
    element(element(parent, 'p'), 'span', value)


def address(parent, name, email, city=''):
    node = element(parent, 'Address')
    fields(node, Name1=name, Street='', PCode='', City=city, Country='Deutschland', Email=email)


def make_document(case, source, offer=None):
    phase = '84' if offer else '83'
    namespace = f'http://www.gaeb.de/GAEB_DA_XML/DA{phase}/{VERSION}'
    root = ET.Element('GAEB', {'xmlns': namespace})
    docs = {doc['filename']: doc for doc in case['documents']}
    project = case['project'].split(' · ', 1)[0]
    bid = docs[BIDS[offer['id']][1]] if offer else None
    issue_date = bid['date'] if bid else '2026-11-04'
    fields(element(root, 'GAEBInfo'), Version=VERSION, VersDate=ISSUE, Date=issue_date,
           ProgSystem='Krimpfort Schulungsakten-Export 1.0',
           ProgName=f'Leistungsverzeichnis X{phase}')
    info = element(root, 'PrjInfo')
    fields(info, NamePrj=project, PrjID=PROJECT_ID, LblPrj=case['project'])
    if not offer:
        element(info, 'BidCommPerm', 'Yes')
    award = element(root, 'Award')
    element(award, 'DP', phase)
    award_info = element(award, 'AwardInfo')
    fields(award_info, BoQID=BOQ_ID, Cur='EUR', CurLbl='Euro')

    if offer:
        _, pdf, mail = BIDS[offer['id']]
        element(award_info, 'BidDate', issue_date)
        bidder = element(award, 'CTR')
        address(bidder, offer['name'], docs[mail]['from_email'])
        element(bidder, 'AwardNo', BOQ_NAME)
        scope, notes = BID_SCOPE[offer['id']]
        text(element(element(bidder, 'AddText'), 'DetailAddText'),
             f'{scope} Schriftangebot {pdf}.')
    else:
        fields(award_info, OpenDate='2026-11-25', OpenTime='12:00:00')
        purchaser = element(award, 'OWN')
        address(purchaser, case['company'], source['from_email'], 'Oldenburg')
        element(purchaser, 'AwardNo', BOQ_NAME)
        element(element(award, 'CnstSite'), 'CnstSiteName', case['project'])
        text(element(element(award, 'AddText'), 'DetailAddText'),
             'Maßgeblich sind die ergänzenden Anforderungen aus Leistungsverzeichnis, '
             'Türregister und Einbauunterlagen. Abweichende Leistungsgrenzen sowie getrennte '
             'Zusatzpreise, Wartung und bedingte Nachlässe im Schriftangebot ausweisen.')

    boq = element(award, 'BoQ', ID='LV_KPF_WB_31')
    boq_info = element(boq, 'BoQInfo')
    element(boq_info, 'Name', BOQ_NAME)
    if not offer:
        fields(boq_info, LblBoQ='Türpaket Weserbogen', Date=issue_date, OutlCompl='AllTxt')
    fields(element(boq_info, 'BoQBkdn'), Type='Item', Length=4, Num='Yes')
    if offer:
        fields(element(boq_info, 'Totals'), Total=f'{offer["base_total"]:.2f}',
               TotalNet=f'{offer["base_total"]:.2f}')
    items = element(element(boq, 'BoQBody'), 'Itemlist')
    for index, (code, (short, long)) in enumerate(POSITION_TEXTS.items(), 1):
        quantity = case['comparison']['quantities'][code]
        item = element(items, 'Item', ID=f'POS_{code}', RNoPart=f'{index:04d}')
        element(item, 'Qty', f'{quantity:.3f}')
        if offer:
            price = offer['unit_prices'][code]
            fields(item, UP=f'{price:.3f}', IT=f'{quantity * price:.2f}')
            if code in notes:
                text(element(item, 'BidComm'), notes[code])
        else:
            element(item, 'QU', 'St')
            complete = element(element(item, 'Description'), 'CompleteText')
            text(element(element(complete, 'DetailTxt'), 'Text'), long)
            outline = element(element(complete, 'OutlineText'), 'OutlTxt')
            text(element(outline, 'TextOutlTxt'), short)
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='utf-8', xml_declaration=True) + b'\n'


def read_positions(data):
    root = ET.fromstring(data)
    namespace = {'g': root.tag.split('}')[0][1:]}
    boq_id = root.findtext('g:Award/g:AwardInfo/g:BoQID', namespaces=namespace)
    lv_number = root.findtext('g:Award/g:BoQ/g:BoQInfo/g:Name', namespaces=namespace)
    rows = []
    for item in root.findall('g:Award/g:BoQ/g:BoQBody/g:Itemlist/g:Item', namespace):
        def read(name):
            return item.findtext('g:' + name, namespaces=namespace)
        rows.append((item.attrib['RNoPart'], item.attrib['ID'], read('Qty'), read('UP'), read('IT')))
    total = root.findtext('g:Award/g:BoQ/g:BoQInfo/g:Totals/g:Total', namespaces=namespace)
    return boq_id, lv_number, rows, total


def verify_content(case, documents):
    by_name = {doc['filename']: doc for doc in case['documents']}
    quantities = case['comparison']['quantities']
    master = read_positions(documents[X83])
    expected_positions = [(f'{i:04d}', f'POS_{code}', f'{quantities[code]:.3f}')
                          for i, code in enumerate(POSITION_TEXTS, 1)]
    if master[:2] != (BOQ_ID, BOQ_NAME) or [r[:3] for r in master[2]] != expected_positions:
        raise ValueError('Das GAEB-LV weicht von der Türliste ab.')
    if sum(quantities.values()) != 500 or master[3] is not None or any(r[3:] != (None, None) for r in master[2]):
        raise ValueError('Das X83 muss alle 500 Türen und keine Preise enthalten.')

    for offer in case['comparison']['offers']:
        filename, pdf, _ = BIDS[offer['id']]
        boq_id, lv_number, items, total = read_positions(documents[filename])
        if (boq_id, lv_number) != master[:2] or [r[:3] for r in items] != expected_positions:
            raise ValueError(f'{filename}: LV-Bezug oder OZ/Menge weicht von X83 ab.')
        actual = [(code, Decimal(qty), Decimal(up), Decimal(it))
                  for (_, identifier, qty, up, it), code in zip(items, POSITION_TEXTS, strict=True)]
        expected = [tuple(row) for row in by_name[pdf]['sections'][0]['table']['rows']]
        if actual != expected or any(qty * up != it for _, qty, up, it in actual):
            raise ValueError(f'{filename}: Einheitspreise oder Positionsbeträge weichen von {pdf} ab.')
        if sum(row[3] for row in actual) != Decimal(total) or Decimal(total) != offer['base_total']:
            raise ValueError(f'{filename}: Nettosumme weicht vom Erstangebot ab.')


def schema_check(schemas, directory, filenames):
    if hashlib.sha256(schemas.read_bytes()).hexdigest() != SCHEMA_SHA256:
        raise ValueError(f'Nicht das erwartete GAEB-Schemapaket. Quelle: {SCHEMA_URL}')
    with TemporaryDirectory(prefix='gaeb-schema-') as scratch, ZipFile(schemas) as archive:
        schema_directory = Path(scratch)
        for phase in ('83', '84', 'Lib'):
            name = f'GAEB_DA_XML_{phase}_{VERSION}_{ISSUE}.xsd'
            (schema_directory / name).write_bytes(archive.read(name))
        for name in filenames:
            phase = Path(name).suffix[-2:]
            schema = schema_directory / f'GAEB_DA_XML_{phase}_{VERSION}_{ISSUE}.xsd'
            subprocess.run(['xmllint', '--nonet', '--noout', '--schema', str(schema),
                            str(directory / name)], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='Verzeichnis der fünf GAEB-Dateien')
    parser.add_argument('--schema-zip', type=Path, required=True, help=f'GAEB-Schemapaket von {SCHEMA_URL}')
    parser.add_argument('--verify-only', action='store_true', help='Vorhandenen Bestand ohne Änderungen prüfen')
    args = parser.parse_args()

    [case] = json.loads(SOURCE.read_text(encoding='utf-8'))['cases']
    [request] = [doc for doc in case['documents'] if doc['filename'] == '07_Anfrage_Tuerpaket.eml']
    documents = {X83: make_document(case, request)}
    for offer in case['comparison']['offers']:
        documents[BIDS[offer['id']][0]] = make_document(case, request, offer)
    verify_content(case, documents)
    if args.verify_only:
        for name, expected in documents.items():
            if (args.output / name).read_bytes() != expected:
                raise ValueError(f'{name}: Inhalt weicht vom reproduzierbaren Export ab.')
        schema_check(args.schema_zip, args.output, documents)
    else:
        with TemporaryDirectory(prefix='krimpfort-gaeb-') as scratch:
            directory = Path(scratch)
            for name, data in documents.items():
                (directory / name).write_bytes(data)
            schema_check(args.schema_zip, directory, documents)
        args.output.mkdir(parents=True, exist_ok=True)
        for name, data in documents.items():
            (args.output / name).write_bytes(data)
    print('GAEB DA XML 3.3 / LV 2021-05: 1 X83, 4 X84, 500 Türen, alle Nettosummen abgeglichen.')


if __name__ == '__main__':
    main()
