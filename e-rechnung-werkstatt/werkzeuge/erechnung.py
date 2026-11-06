#!/usr/bin/env python3
"""Lokale Rechnungsausgabe aus einem geprüften, belegten Datenstand.

EUR, inländische Parteien, Rechnung 380, Überweisung 58, positive Positionen
mit 7 oder 19 Prozent Umsatzsteuer. Andere Steuer- und Abrechnungsfälle werden
ausdrücklich abgewiesen. Es findet kein Rechnungsversand statt.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rechnung_layout import write_layout

MUSTANG_SHA256 = '42d7868cb68264874a7b8cab4c3587b03b23ccc7cd72373da917f66758bb9736'
BUSINESS_PROCESS = 'urn:fdc:peppol.eu:2017:poacc:billing:01:1.0'
XR_ID = 'urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0'
ZF_ID = 'urn:cen.eu:en16931:2017'
NS = {
    'ubl': 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2',
    'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
    'rsm': 'urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100',
    'ram': 'urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100',
    'udt': 'urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100',
}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)


def fail(message):
    raise ValueError(message)


def input_bytes(path):
    with path.open('rb') as stream:
        result = stream.read(8 * 1024**2 + 1)
    if len(result) > 8 * 1024**2:
        fail('JSON-Eingabe überschreitet 8 MiB')
    return result


def json_parse(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result: fail('Widersprüchliche JSON-Eingabe: doppelter Schlüssel ' + key)
            result[key] = value
        return result
    def constant(value): fail('Ungültige JSON-Konstante ' + value)
    return json.loads(raw.decode('utf-8'), object_pairs_hook=unique, parse_constant=constant)


def json_read(path):
    return json_parse(input_bytes(path))


def text(value, field):
    if not isinstance(value, str) or not value.strip() or len(value) > 4000:
        fail(f'{field}: vollständiger Text bis 4000 Zeichen erforderlich')
    if any(ord(c) < 32 or 0xD800 <= ord(c) <= 0xDFFF for c in value):
        fail(f'{field}: unzulässiges Steuerzeichen')
    return value.strip()


def decimal(value, field, precision=6):
    if not isinstance(value, str) or not re.fullmatch(r'\d+(?:\.\d+)?', value):
        fail(f'{field}: nichtnegative Dezimalzahl als Zeichenkette erforderlich')
    result = Decimal(value)
    if not result.is_finite() or result > Decimal('999999999999') or result.as_tuple().exponent < -precision:
        fail(f'{field}: Zahl oder Genauigkeit nicht unterstützt')
    return result


def money(value):
    return str(value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


def keys(value, allowed, required, name):
    if not isinstance(value, dict) or set(value) - set(allowed) or set(required) - set(value):
        fail(f'{name}: fehlende oder nicht unterstützte Felder; Sonderfälle nicht stillschweigend weglassen')


def validate(data, source_root=None):
    common = ('schema_version', 'reviewed', 'invoice_type', 'currency', 'invoice_number', 'issue_date', 'delivery_date',
              'due_date', 'period_start', 'period_end', 'buyer_reference', 'supplier', 'customer',
              'lines', 'totals', 'sources', 'evidence')
    keys(data, common + ('note',), common, 'Rechnungsdaten')
    if type(data['schema_version']) is not int or data['schema_version'] != 1 or data['reviewed'] is not True:
        fail('schema_version=1 und reviewed=true für den geprüften Arbeitsstand erforderlich')
    if data['invoice_type'] != '380' or data['currency'] != 'EUR':
        fail('Dieser Helfer unterstützt ausschließlich Rechnungen 380 in EUR')
    evidence_fields = set()
    for field in ('invoice_number', 'buyer_reference', 'issue_date', 'delivery_date', 'due_date', 'period_start', 'period_end'):
        text(data[field], field)
        evidence_fields.add(field)
    for field in ('issue_date', 'delivery_date', 'due_date', 'period_start', 'period_end'):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', data[field]):
            fail(f'{field}: Datum im Format YYYY-MM-DD erforderlich')
        date.fromisoformat(data[field])
    if data['due_date'] < data['issue_date'] or data['period_end'] < data['period_start']:
        fail('Unplausible Datumsfolge')
    if not data['period_start'] <= data['delivery_date'] <= data['period_end']:
        fail('Das ausdrücklich bestätigte Liefer-/Leistungsabschlussdatum liegt außerhalb des bestätigten Leistungszeitraums')
    if 'note' in data:
        text(data['note'], 'note')
        evidence_fields.add('note')
    party_fields = ('name', 'street', 'postal_code', 'city', 'country', 'email')
    supplier_fields = party_fields + ('contact', 'phone', 'iban')
    for role in ('supplier', 'customer'):
        fields = supplier_fields if role == 'supplier' else party_fields
        allowed = fields + (('vat_id', 'tax_number') if role == 'supplier' else ())
        p = data[role]
        keys(p, allowed, fields, role)
        for field in p:
            text(p[field], role + '.' + field)
            evidence_fields.add(role + '.' + field)
        if p['country'] != 'DE' or not re.fullmatch(r'\d{5}', p['postal_code']):
            fail('Nur ausdrücklich inländische Parteien mit deutscher Postleitzahl unterstützt')
        if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', p['email']):
            fail(f'{role}.email: elektronische Adresse prüfen')
    seller = data['supplier']
    if not seller.get('vat_id') and not seller.get('tax_number'):
        fail('USt-IdNr. oder betriebliche Steuernummer des Ausstellers erforderlich')
    if seller.get('vat_id') and not re.fullmatch(r'DE\d{9}', seller['vat_id']):
        fail('Deutsche USt-IdNr. prüfen; die Existenz wird hier nicht amtlich bestätigt')
    iban = re.sub(r'\s', '', seller['iban']).upper()
    if not re.fullmatch(r'DE\d{20}', iban):
        fail('Deutsche IBAN erforderlich')
    digits = ''.join(str(ord(c) - 55) if c.isalpha() else c for c in iban[4:] + iban[:4])
    if int(digits) % 97 != 1:
        fail('IBAN-Prüfziffer ungültig')
    if seller['iban'] != iban:
        fail('IBAN im geprüften Arbeitsstand ohne Leerzeichen und in Großbuchstaben angeben')
    if not isinstance(data['lines'], list) or not 1 <= len(data['lines']) <= 1000:
        fail('1 bis 1000 Rechnungspositionen erforderlich')
    groups = defaultdict(lambda: Decimal(0))
    ids = set()
    for index, row in enumerate(data['lines']):
        fields = ('id', 'description', 'quantity', 'unit_code', 'unit_price_net', 'vat_rate')
        keys(row, fields, fields, f'lines.{index}')
        for field in fields:
            text(row[field], f'lines.{index}.{field}')
            evidence_fields.add(f'lines.{index}.{field}')
        if row['id'] in ids:
            fail('Doppelte Positions-ID')
        ids.add(row['id'])
        if row['unit_code'] not in ('C62', 'HUR', 'MIN', 'DAY', 'KGM', 'LTR', 'MTR'):
            fail('Einheit nicht unterstützt; keinen Einheitencode erraten')
        quantity = decimal(row['quantity'], 'quantity')
        price = decimal(row['unit_price_net'], 'unit_price_net')
        rate = decimal(row['vat_rate'], 'vat_rate', precision=0)
        if quantity <= 0 or price <= 0 or rate not in (Decimal(7), Decimal(19)):
            fail('Nur positive Positionen mit geprüftem Steuersatz 7 oder 19 unterstützt')
        groups[rate] += (quantity * price).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    net = sum(groups.values())
    tax = sum((base * rate / 100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP) for rate, base in groups.items())
    calculated = {'net': net, 'tax': tax, 'gross': net + tax, 'payable': net + tax}
    keys(data['totals'], calculated, calculated, 'totals')
    for field, expected in calculated.items():
        value = decimal(data['totals'][field], 'totals.' + field, precision=2)
        if value != expected:
            fail(f'totals.{field}: Belegsumme {value} weicht von berechneten {money(expected)} ab')
        evidence_fields.add('totals.' + field)
    if not isinstance(data['sources'], list) or not data['sources']:
        fail('Quellenverzeichnis erforderlich')
    source_ids = set()
    for source in data['sources']:
        keys(source, ('id', 'file', 'sha256'), ('id', 'file', 'sha256'), 'source')
        for field in source:
            text(source[field], 'source.' + field)
        if source['id'] in source_ids or not re.fullmatch(r'[a-f0-9]{64}', source['sha256']):
            fail('Doppelte Quellen-ID oder ungültiger Quellenhash')
        source_ids.add(source['id'])
        if source_root is not None:
            original = (source_root / source['file']).resolve()
            if not original.is_relative_to(source_root.resolve()) or not original.is_file() or original.stat().st_size > 64 * 1024**2:
                fail('Quelldatei außerhalb des freigegebenen Quellenordners, fehlt oder ist zu groß')
            if sha256(original.read_bytes()).hexdigest() != source['sha256']:
                fail('Quelldatei geändert: ' + source['file'])
    if not isinstance(data['evidence'], list):
        fail('Feldbezogene Belegzuordnung erforderlich')
    covered = set()
    for entry in data['evidence']:
        keys(entry, ('field', 'source_id', 'location'), ('field', 'source_id', 'location'), 'evidence')
        for field in entry:
            text(entry[field], 'evidence.' + field)
        if entry['source_id'] not in source_ids or entry['field'] not in evidence_fields:
            fail('Belegzuordnung enthält eine unbekannte Quelle oder ein unbekanntes Rechnungsfeld')
        covered.add(entry['field'])
    if evidence_fields - covered:
        fail('Belegzuordnung fehlt: ' + ', '.join(sorted(evidence_fields - covered)))
    return groups, calculated


def el(parent, tag, value=None, **attrs):
    prefix, local = tag.split(':')
    item = ET.SubElement(parent, '{' + NS[prefix] + '}' + local, attrs)
    if value is not None:
        item.text = str(value)
    return item


def xml_bytes(root):
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)


def ubl(data):
    groups, totals = validate(data)
    root = ET.Element('{' + NS['ubl'] + '}Invoice')
    b = lambda p, n, v=None, **a: el(p, 'cbc:' + n, v, **a)
    a = lambda p, n: el(p, 'cac:' + n)
    for field, value in [('CustomizationID', XR_ID), ('ProfileID', BUSINESS_PROCESS), ('ID', data['invoice_number']),
                         ('IssueDate', data['issue_date']), ('DueDate', data['due_date']), ('InvoiceTypeCode', '380')]:
        b(root, field, value)
    if data.get('note'):
        b(root, 'Note', data['note'])
    b(root, 'DocumentCurrencyCode', 'EUR')
    b(root, 'BuyerReference', data['buyer_reference'])
    period = a(root, 'InvoicePeriod')
    b(period, 'StartDate', data['period_start']); b(period, 'EndDate', data['period_end'])
    for role, name in (('supplier', 'AccountingSupplierParty'), ('customer', 'AccountingCustomerParty')):
        p = data[role]; party = a(a(root, name), 'Party')
        b(party, 'EndpointID', p['email'], schemeID='EM')
        b(a(party, 'PartyName'), 'Name', p['name'])
        address = a(party, 'PostalAddress')
        for key, tag in [('street', 'StreetName'), ('city', 'CityName'), ('postal_code', 'PostalZone')]:
            b(address, tag, p[key])
        b(a(address, 'Country'), 'IdentificationCode', p['country'])
        if role == 'supplier':
            for field, scheme in [('vat_id', 'VAT'), ('tax_number', 'FC')]:
                if p.get(field):
                    registration = a(party, 'PartyTaxScheme')
                    b(registration, 'CompanyID', p[field]); b(a(registration, 'TaxScheme'), 'ID', scheme)
        b(a(party, 'PartyLegalEntity'), 'RegistrationName', p['name'])
        if role == 'supplier':
            contact = a(party, 'Contact')
            for key, tag in [('contact', 'Name'), ('phone', 'Telephone'), ('email', 'ElectronicMail')]:
                b(contact, tag, p[key])
    b(a(root, 'Delivery'), 'ActualDeliveryDate', data['delivery_date'])
    means = a(root, 'PaymentMeans'); b(means, 'PaymentMeansCode', '58')
    b(means, 'PaymentID', data['invoice_number'])
    b(a(means, 'PayeeFinancialAccount'), 'ID', data['supplier']['iban'])
    b(a(root, 'PaymentTerms'), 'Note', 'Zahlbar bis ' + data['due_date'] + ' ohne Abzug.')
    total = a(root, 'TaxTotal'); b(total, 'TaxAmount', money(totals['tax']), currencyID='EUR')
    for rate, base in sorted(groups.items()):
        sub = a(total, 'TaxSubtotal')
        b(sub, 'TaxableAmount', money(base), currencyID='EUR')
        b(sub, 'TaxAmount', money(base * rate / 100), currencyID='EUR')
        category = a(sub, 'TaxCategory'); b(category, 'ID', 'S'); b(category, 'Percent', str(rate))
        b(a(category, 'TaxScheme'), 'ID', 'VAT')
    total = a(root, 'LegalMonetaryTotal')
    for name, amount in [('LineExtensionAmount', totals['net']), ('TaxExclusiveAmount', totals['net']),
                         ('TaxInclusiveAmount', totals['gross']), ('PayableAmount', totals['payable'])]:
        b(total, name, money(amount), currencyID='EUR')
    for row in data['lines']:
        line = a(root, 'InvoiceLine'); b(line, 'ID', row['id'])
        b(line, 'InvoicedQuantity', row['quantity'], unitCode=row['unit_code'])
        b(line, 'LineExtensionAmount', money(Decimal(row['quantity']) * Decimal(row['unit_price_net'])), currencyID='EUR')
        item = a(line, 'Item'); b(item, 'Name', row['description'])
        category = a(item, 'ClassifiedTaxCategory'); b(category, 'ID', 'S'); b(category, 'Percent', row['vat_rate'])
        b(a(category, 'TaxScheme'), 'ID', 'VAT')
        b(a(line, 'Price'), 'PriceAmount', row['unit_price_net'], currencyID='EUR')
    return xml_bytes(root)


def cii(data):
    groups, totals = validate(data)
    root = ET.Element('{' + NS['rsm'] + '}CrossIndustryInvoice')
    def r(p, tag, value=None, **attrs): return el(p, 'ram:' + tag, value, **attrs)
    def dated(p, tag, value): el(r(p, tag), 'udt:DateTimeString', value.replace('-', ''), format='102')
    context = el(root, 'rsm:ExchangedDocumentContext')
    r(r(context, 'BusinessProcessSpecifiedDocumentContextParameter'), 'ID', BUSINESS_PROCESS)
    r(r(context, 'GuidelineSpecifiedDocumentContextParameter'), 'ID', ZF_ID)
    doc = el(root, 'rsm:ExchangedDocument'); r(doc, 'ID', data['invoice_number']); r(doc, 'TypeCode', '380')
    dated(doc, 'IssueDateTime', data['issue_date'])
    if data.get('note'): r(r(doc, 'IncludedNote'), 'Content', data['note'])
    tx = el(root, 'rsm:SupplyChainTradeTransaction')
    for row in data['lines']:
        line = r(tx, 'IncludedSupplyChainTradeLineItem')
        r(r(line, 'AssociatedDocumentLineDocument'), 'LineID', row['id'])
        r(r(line, 'SpecifiedTradeProduct'), 'Name', row['description'])
        agreement = r(line, 'SpecifiedLineTradeAgreement')
        r(r(agreement, 'NetPriceProductTradePrice'), 'ChargeAmount', row['unit_price_net'])
        r(r(line, 'SpecifiedLineTradeDelivery'), 'BilledQuantity', row['quantity'], unitCode=row['unit_code'])
        settlement = r(line, 'SpecifiedLineTradeSettlement'); tax = r(settlement, 'ApplicableTradeTax')
        r(tax, 'TypeCode', 'VAT'); r(tax, 'CategoryCode', 'S'); r(tax, 'RateApplicablePercent', row['vat_rate'])
        r(r(settlement, 'SpecifiedTradeSettlementLineMonetarySummation'), 'LineTotalAmount',
          money(Decimal(row['quantity']) * Decimal(row['unit_price_net'])))
    agreement = r(tx, 'ApplicableHeaderTradeAgreement'); r(agreement, 'BuyerReference', data['buyer_reference'])
    for role, tag in [('supplier', 'SellerTradeParty'), ('customer', 'BuyerTradeParty')]:
        p = data[role]; party = r(agreement, tag); r(party, 'Name', p['name'])
        if role == 'supplier':
            contact = r(party, 'DefinedTradeContact'); r(contact, 'PersonName', p['contact'])
            r(r(contact, 'TelephoneUniversalCommunication'), 'CompleteNumber', p['phone'])
            r(r(contact, 'EmailURIUniversalCommunication'), 'URIID', p['email'])
        address = r(party, 'PostalTradeAddress')
        for key, tag in [('postal_code', 'PostcodeCode'), ('street', 'LineOne'), ('city', 'CityName'), ('country', 'CountryID')]:
            r(address, tag, p[key])
        r(r(party, 'URIUniversalCommunication'), 'URIID', p['email'], schemeID='EM')
        if role == 'supplier':
            for key, scheme in [('vat_id', 'VA'), ('tax_number', 'FC')]:
                if p.get(key): r(r(party, 'SpecifiedTaxRegistration'), 'ID', p[key], schemeID=scheme)
    delivery = r(tx, 'ApplicableHeaderTradeDelivery')
    # BT-72 is separately confirmed, never inferred from the billing period.
    dated(r(delivery, 'ActualDeliverySupplyChainEvent'), 'OccurrenceDateTime', data['delivery_date'])
    settlement = r(tx, 'ApplicableHeaderTradeSettlement')
    r(settlement, 'PaymentReference', data['invoice_number']); r(settlement, 'InvoiceCurrencyCode', 'EUR')
    means = r(settlement, 'SpecifiedTradeSettlementPaymentMeans'); r(means, 'TypeCode', '58')
    r(r(means, 'PayeePartyCreditorFinancialAccount'), 'IBANID', data['supplier']['iban'])
    for rate, base in sorted(groups.items()):
        tax = r(settlement, 'ApplicableTradeTax'); r(tax, 'CalculatedAmount', money(base * rate / 100))
        r(tax, 'TypeCode', 'VAT'); r(tax, 'BasisAmount', money(base)); r(tax, 'CategoryCode', 'S')
        r(tax, 'RateApplicablePercent', str(rate))
    period = r(settlement, 'BillingSpecifiedPeriod')
    dated(period, 'StartDateTime', data['period_start']); dated(period, 'EndDateTime', data['period_end'])
    terms = r(settlement, 'SpecifiedTradePaymentTerms')
    r(terms, 'Description', 'Zahlbar bis ' + data['due_date'] + ' ohne Abzug.')
    dated(terms, 'DueDateDateTime', data['due_date'])
    total = r(settlement, 'SpecifiedTradeSettlementHeaderMonetarySummation')
    for tag, value in [('LineTotalAmount', totals['net']), ('ChargeTotalAmount', Decimal(0)),
                       ('AllowanceTotalAmount', Decimal(0)), ('TaxBasisTotalAmount', totals['net'])]:
        r(total, tag, money(value))
    r(total, 'TaxTotalAmount', money(totals['tax']), currencyID='EUR')
    r(total, 'GrandTotalAmount', money(totals['gross'])); r(total, 'DuePayableAmount', money(totals['payable']))
    return xml_bytes(root)


def run(command, log, cwd):
    result = subprocess.run([str(v) for v in command], cwd=cwd, stdin=subprocess.DEVNULL,
                            capture_output=True, text=True, timeout=180)
    log.write_text(result.stdout + '\n' + result.stderr, encoding='utf-8')
    if result.returncode:
        fail('Werkzeugprüfung fehlgeschlagen; Prüfprotokoll: ' + str(log))
    return result.stdout


def mustang_report(output, require_pdf=False):
    start = output.find('<?xml')
    if start < 0: fail('Mustang hat keinen maschinenlesbaren Prüfbericht geliefert')
    raw = output[start:].strip()
    if '<!DOCTYPE' in raw.upper() or '<!ENTITY' in raw.upper(): fail('Unerwartete XML-Deklaration im Prüfbericht')
    root = ET.fromstring(raw)
    if root.tag != 'validation' or root.find('summary') is None or root.find('summary').get('status') != 'valid':
        fail('Mustang hat die Rechnung abgewiesen')
    if root.find('xml/summary') is None or root.find('xml/summary').get('status') != 'valid':
        fail('XML-Validierung fehlt oder ist fehlgeschlagen')
    if root.findall('.//error') or root.findall('.//fatal'):
        fail('Prüfbericht enthält Fehler')
    if root.findall('.//warning'):
        fail('Prüfbericht enthält eine Warnung; keine automatische Freigabe')
    for notice in root.findall('.//notice'):
        # Mustang additionally applies XRechnung rules to EN16931 invoices.
        # This single profile notice is expected for a ZUGFeRD EN16931 invoice.
        if '[ID BR-DE-21]' not in ''.join(notice.itertext()):
            fail('Ungeklärter Prüfhinweis; keine automatische Freigabe')
    if require_pdf:
        pdf = root.find('pdf')
        if pdf is None or pdf.find('summary') is None or pdf.find('summary').get('status') != 'valid':
            fail('PDF/A-Validierung fehlt oder ist fehlgeschlagen')
        # PDF/A errors are downgraded by Mustang to warnings. Fail closed even
        # when its overall status remains valid; retain every original message.
        if pdf.findall('.//warning') or root.findall('./messages/warning'):
            fail('PDF/A-Warnung: Hybriddatei wird nicht als konform freigegeben')
        # Mustang 2.26.0 serializes veraPDF's ValidationResult as the direct
        # text of <pdf>, not as an isCompliant XML attribute. Require its whole
        # success record, a PDF/A-3 flavour, positive assertions and no failures.
        compliant = re.fullmatch(r'ValidationResult \[flavour=3[abu], totalAssertions=([1-9]\d*), assertions=\[\], isCompliant=true\]',
                                 (pdf.text or '').strip())
        if not compliant:
            fail('Ein positiver veraPDF-Konformitätsnachweis fehlt')
    return raw


def layout_log_check(path):
    log = path.read_text(encoding='utf-8')
    if re.search(r'\bWARN(?:ING)?\b|\bERROR\b|\bFATAL\b|overflow|glyph[^\n]*not available|font[^\n]*substitut', log, re.I):
        fail('Rechnungsdarstellung hat einen Rendererhinweis; keine automatische Freigabe: ' + str(path))


def kosit_validate(source, home, java, stage):
    jar = home / 'validator-1.6.3-standalone.jar'
    config = home / 'configuration'
    lock = home / 'installation.json'
    if not jar.is_file() or not (config / 'scenarios.xml').is_file() or not lock.is_file():
        fail('Geprüfte KoSIT-Installation fehlt; Einrichtung gemäß Werkzeug-README durchführen')
    installation = json.loads(lock.read_text())
    if installation.get('configuration') != '2026-08-31' or installation.get('validator') != '1.6.3':
        fail('KoSIT-Version stimmt nicht mit dem geprüften Werkzeugstand überein')
    pinned = json.loads(Path(__file__).with_name('runtime-lock.json').read_text())['kosit']['files_sha256']
    if installation.get('files_sha256') != pinned:
        fail('KoSIT-Installationsinventar stimmt nicht mit dem gepinnten amtlichen Bundle überein')
    for relative, digest in pinned.items():
        item = (home / relative).resolve()
        if not item.is_relative_to(home.resolve()) or not item.is_file() or sha256(item.read_bytes()).hexdigest() != digest:
            fail('KoSIT-Installation hat sich geändert')
    if not installation.get('files_sha256') or str(jar.relative_to(home)) not in installation['files_sha256']:
        fail('KoSIT-Installationsinventar fehlt')
    target = stage / 'kosit'; target.mkdir()
    run([java, '-jar', jar, '-s', config / 'scenarios.xml', '-r', config, '-o', target, '-h', source], stage / 'kosit.log', stage)
    report = target / (source.stem + '-report.xml')
    if not report.is_file(): fail('KoSIT-Prüfbericht fehlt')
    root = ET.parse(report).getroot()
    namespace = {'rep': 'http://www.xoev.de/de/validator/varl/1'}
    if root.get('valid') != 'true' or root.find('rep:assessment/rep:accept', namespace) is None:
        fail('KoSIT hat die Rechnung abgewiesen')
    steps = root.findall('.//rep:validationStepResult', namespace)
    if not steps or any(s.get('valid') != 'true' for s in steps): fail('KoSIT-Prüfschritte sind unvollständig oder negativ')


def create(input_path, output, mode, jar, java, kosit_home=None, source_root=None):
    if output.exists(): fail('Ein noch nicht existierendes Ausgabeverzeichnis ist erforderlich')
    original_input = input_bytes(input_path)
    data = json_parse(original_input)
    generator_digest = sha256(Path(__file__).read_bytes()).hexdigest()
    lock_digest = sha256(Path(__file__).with_name('runtime-lock.json').read_bytes()).hexdigest()
    layout_path = Path(__file__).with_name('rechnung_layout.py')
    layout_digest = sha256(layout_path.read_bytes()).hexdigest()
    validate(data, (source_root or input_path.parent).resolve())
    if not jar.is_file() or sha256(jar.read_bytes()).hexdigest() != MUSTANG_SHA256:
        fail('Das geprüfte Mustang-CLI-2.26.0.jar fehlt oder dessen SHA-256 weicht ab')
    if mode in ('both', 'xrechnung') and kosit_home is None:
        fail('Für XRechnung ist die aktuelle KoSIT-Installation erforderlich')
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.' + output.name + '-', dir=output.parent))
    try:
        command = [java, '-jar', jar.resolve(), '--disable-file-logging']
        results = {}
        if mode in ('both', 'xrechnung'):
            invoice = stage / 'XRechnung.xml'; invoice.write_bytes(ubl(data))
            kosit_validate(invoice.resolve(), kosit_home.resolve(), java, stage)
            results['XRechnung.xml'] = {'format': 'UBL 2.1 / XRechnung 3.0.2', 'configuration': '2026-08-31', 'schema_and_schematron_valid': True}
        if mode in ('both', 'zugferd'):
            xml = stage / 'factur-x.xml'; xml.write_bytes(cii(data))
            stdout = run(command + ['--action', 'validate', '--source', xml.resolve()], stage / 'zugferd-xml.log', stage)
            (stage / 'zugferd-xml-pruefung.xml').write_text(mustang_report(stdout), encoding='utf-8')
            view = stage / 'Rechnungsansicht.pdf'
            fo, config = write_layout(data, jar, stage)
            run([java, '-cp', jar.resolve(), 'org.apache.fop.cli.Main', '-c', config.resolve(), '-fo', fo.resolve(),
                 '-pdf', view.resolve(), '-pdfprofile', 'PDF/A-3b', '-nocs'], stage / 'rechnungsansicht.log', stage)
            layout_log_check(stage / 'rechnungsansicht.log')
            if not view.is_file(): fail('Die PDF/A-Rechnungsansicht wurde nicht erzeugt')
            hybrid = stage / 'ZUGFeRD.pdf'
            run(command + ['--action', 'combine', '--source', view.resolve(), '--source-xml', xml.resolve(),
                           '--out', hybrid.resolve(), '--format', 'fx', '--version', '1', '--profile', 'E',
                           '--no-additional-attachments'], stage / 'hybrid-erzeugung.log', stage)
            if not hybrid.is_file(): fail('Die Hybriddatei wurde nicht erzeugt')
            stdout = run(command + ['--action', 'validate', '--source', hybrid.resolve()], stage / 'zugferd-pdf.log', stage)
            (stage / 'zugferd-pdf-pruefung.xml').write_text(mustang_report(stdout, require_pdf=True), encoding='utf-8')
            from pypdf import PdfReader
            with hybrid.open('rb') as stream:
                pdf = PdfReader(stream)
                if set(pdf.attachments) != {'factur-x.xml'} or pdf.attachments.get('factur-x.xml') != [xml.read_bytes()]:
                    fail('Eingebettetes Rechnungs-XML weicht vom geprüften Datenstand ab')
            pdf_report = ET.fromstring((stage / 'zugferd-pdf-pruefung.xml').read_text())
            flavour = re.search(r'flavour=(3[abu])', pdf_report.find('pdf').text).group(1)
            results['ZUGFeRD.pdf'] = {'format': 'ZUGFeRD 2.5.2 / Factur-X 1.09.2 / EN16931', 'pdfa': 'PDF/A-' + flavour,
                                      'schema_and_schematron_valid': True, 'pdfa_valid': True, 'xml_attachment_identical': True}
        (stage / 'Rechnungsdaten.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        if input_bytes(input_path) != original_input or sha256(Path(__file__).read_bytes()).hexdigest() != generator_digest \
                or sha256(Path(__file__).with_name('runtime-lock.json').read_bytes()).hexdigest() != lock_digest \
                or sha256(layout_path.read_bytes()).hexdigest() != layout_digest:
            fail('Eingabestand oder Werkzeugstand hat sich während der Erstellung geändert; erneut prüfen und erzeugen')
        report = {'schema_version': 1, 'state': 'generated_and_validated_not_sent', 'mustang': '2.26.0',
                  'generator_sha256': generator_digest,
                  'input_sha256': sha256(original_input).hexdigest(),
                  'runtime_lock_sha256': lock_digest,
                  'layout_sha256': layout_digest,
                  'sources_byte_checked': True, 'field_evidence_complete': True,
                  'tax_assessment_by_tool': False, 'recipient_portal_acceptance_tested': False,
                  'results': results, 'files_sha256': {p.relative_to(stage).as_posix(): sha256(p.read_bytes()).hexdigest()
                                                       for p in sorted(stage.rglob('*')) if p.is_file()}}
        (stage / 'Pruefbericht.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        stage.rename(output)
        return report
    except Exception as exc:
        # A failed candidate never appears at the requested final destination.
        # Preserve local diagnostics so callers can correct the actual failure.
        (stage / 'FEHLGESCHLAGEN.txt').write_text('NICHT FREIGEGEBEN. ' + str(exc) + '\n', encoding='utf-8')
        raise ValueError(str(exc) + '; lokale Zwischendateien und Protokolle: ' + str(stage)) from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    command = sub.add_parser('create', help='Geprüfte Daten lokal erzeugen und validieren; kein Versand')
    command.add_argument('--input', type=Path, required=True)
    command.add_argument('--out', type=Path, required=True)
    command.add_argument('--format', choices=('both', 'xrechnung', 'zugferd'), default='both')
    command.add_argument('--mustang-jar', type=Path, required=True)
    command.add_argument('--java', default='java')
    command.add_argument('--kosit-home', type=Path)
    command.add_argument('--source-root', type=Path)
    args = parser.parse_args()
    report = create(args.input.resolve(), args.out.absolute(), args.format, args.mustang_jar.resolve(),
                    str(Path(args.java).resolve()) if '/' in args.java else args.java, args.kosit_home, args.source_root)
    print(json.dumps({'directory': str(args.out), 'state': report['state'], 'results': report['results']}, ensure_ascii=False))


if __name__ == '__main__':
    try: main()
    except (ValueError, OSError, KeyError, InvalidOperation, subprocess.SubprocessError, ET.ParseError) as exc:
        print('Fehler: ' + str(exc), file=sys.stderr); sys.exit(2)
