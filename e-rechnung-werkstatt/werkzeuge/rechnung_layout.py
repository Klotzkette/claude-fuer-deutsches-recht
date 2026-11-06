"""Lesbares Rechnungsformular aus demselben bestätigten Datenstand wie das XML.

Die Hausschrift Source Sans Pro wird aus der geprüften Mustang-JAR eingebettet.
Apache FOP erzeugt PDF/A-3; die abschließende Prüfung erfolgt am Hybrid-PDF.
"""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import re
import xml.etree.ElementTree as ET

FO = 'http://www.w3.org/1999/XSL/Format'
ET.register_namespace('fo', FO)
INK = '#20313D'
TEAL = '#14696B'
LIGHT = '#EFF6F5'


def add(parent, name, value=None, **attrs):
    node = ET.SubElement(parent, '{' + FO + '}' + name, {k.replace('_', '-'): str(v) for k, v in attrs.items()})
    if value is not None:
        # Long identifiers may wrap without changing the actual XML data.
        node.text = re.sub(r'\S{31,}', lambda m: '\u200b'.join(m[0][i:i+24] for i in range(0, len(m[0]), 24)), str(value))
    return node


def eur(value):
    return f'{Decimal(value).quantize(Decimal(".01"), rounding=ROUND_HALF_UP):,.2f}'.replace(',', 'x').replace('.', ',').replace('x', '.')


def price(value):
    integral, _, fraction = format(Decimal(value), 'f').partition('.')
    return integral + ',' + fraction.rstrip('0').ljust(2, '0')


def day(value):
    return '.'.join(reversed(value.split('-')))


def block(parent, value=None, **attrs):
    return add(parent, 'block', value, **attrs)


def table(parent, widths, **attrs):
    result = add(parent, 'table', table_layout='fixed', width='100%', **attrs)
    for width in widths:
        add(result, 'table-column', column_width=width)
    return result


def cell(row, value=None, **attrs):
    result = add(row, 'table-cell', **{'padding': '2.3mm', **attrs})
    block(result, value)
    return result


def write_layout(data, jar, directory):
    """Schreibt ausschließlich lokale FO-/Fontkonfiguration und gibt beide Pfade zurück."""
    root = ET.Element('{' + FO + '}root', {'font-family': 'SourceSansPro', 'font-size': '10.5pt', 'line-height': '1.3', 'color': INK})
    masters = add(root, 'layout-master-set')
    master = add(masters, 'simple-page-master', master_name='invoice', page_width='210mm', page_height='297mm', margin='18mm')
    add(master, 'region-body', margin_bottom='15mm')
    add(master, 'region-after', extent='10mm')
    sequence = add(root, 'page-sequence', master_reference='invoice')
    footer = add(sequence, 'static-content', flow_name='xsl-region-after')
    foot = block(footer, font_size='8pt', color='#5A6870', border_top='0.5pt solid #D6E1E1', padding_top='3mm')
    foot.text = data['invoice_number'] + '  ·  '
    add(foot, 'inline', 'Seite ')
    add(foot, 'page-number')
    add(foot, 'inline', ' / ')
    add(foot, 'page-number-citation-last', ref_id='invoice-end')
    body = add(sequence, 'flow', flow_name='xsl-region-body')
    seller = data['supplier']; buyer = data['customer']
    block(body, seller['name'], font_size='18pt', font_weight='bold', color=TEAL, space_after='2mm')
    block(body, seller['street'] + ' · ' + seller['postal_code'] + ' ' + seller['city'], font_size='9pt', color='#5A6870', border_bottom='2pt solid ' + TEAL, padding_bottom='5mm', space_after='9mm')
    parties = table(body, ['60%', '40%'])
    row = add(add(parties, 'table-body'), 'table-row')
    recipient = add(row, 'table-cell', padding_right='8mm')
    block(recipient, 'RECHNUNGSEMPFÄNGER', font_size='8pt', font_weight='bold', color=TEAL, space_after='2mm')
    for text in (buyer['name'], buyer['street'], buyer['postal_code'] + ' ' + buyer['city'], 'Deutschland'):
        block(recipient, text)
    sender = add(row, 'table-cell')
    block(sender, 'IHR ANSPRECHPARTNER', font_size='8pt', font_weight='bold', color=TEAL, space_after='2mm')
    for text in (seller['contact'], seller['email'], seller['phone']):
        block(sender, text, font_size='9pt')
    block(body, 'Rechnung ' + data['invoice_number'], font_size='20pt', font_weight='bold', space_before='10mm', space_after='3mm')
    block(body, 'Rechnungsdatum: ' + day(data['issue_date']) + ' · Fällig am: ' + day(data['due_date']), font_size='10pt', space_after='1mm')
    block(body, 'Leistungszeitraum: ' + day(data['period_start']) + ' bis ' + day(data['period_end']), font_size='10pt')
    block(body, 'Leistungsdatum: ' + day(data['delivery_date']), font_size='10pt')
    block(body, 'Kundenreferenz: ' + data['buyer_reference'], font_size='10pt', space_after='6mm')
    items = table(body, ['6%', '38%', '9%', '10%', '14%', '8%', '15%'], font_size='9pt')
    header = add(add(items, 'table-header'), 'table-row', background_color=TEAL, color='#FFFFFF', font_weight='bold')
    for index, title in enumerate(('Pos.', 'Leistung', 'Menge', 'Einheit', 'Preis netto', 'USt.', 'Summe netto')):
        cell(header, title, **({'padding': '2.3mm 1.5mm'} if index == 0 else {}))
    rows = add(items, 'table-body')
    groups = {}
    units = {'HUR': 'Std.', 'MIN': 'Min.', 'DAY': 'Tag', 'C62': 'Stück', 'KGM': 'kg', 'LTR': 'Liter', 'MTR': 'Meter'}
    for index, item in enumerate(data['lines']):
        amount = (Decimal(item['quantity']) * Decimal(item['unit_price_net'])).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
        rate = Decimal(item['vat_rate'])
        groups[rate] = groups.get(rate, Decimal(0)) + amount
        row = add(rows, 'table-row', background_color=LIGHT if index % 2 == 0 else '#FFFFFF')
        values = [item['id'], item['description'], item['quantity'].replace('.', ','), units[item['unit_code']], price(item['unit_price_net']), item['vat_rate'] + ' %', eur(amount)]
        for col, value in enumerate(values):
            cell(row, value, text_align='right' if col in (2, 4, 5, 6) else 'left', border_bottom='0.5pt solid #D6E1E1', **({'padding': '2.3mm 1.5mm'} if col == 0 else {}))
    totals = block(body, space_before='5mm', **{'keep-together.within-page': 'always'})
    sums = table(totals, ['65%', '20%', '15%'], font_size='10pt')
    rows = add(sums, 'table-body')
    row = add(rows, 'table-row')
    cell(row, ''); cell(row, 'Nettobetrag'); cell(row, eur(data['totals']['net']), text_align='right')
    for rate, base in sorted(groups.items()):
        row = add(rows, 'table-row')
        cell(row, 'Bemessungsgrundlage ' + eur(base) + ' EUR', color='#5A6870', font_size='9pt', text_align='right')
        cell(row, 'Umsatzsteuer ' + str(rate) + ' %'); cell(row, eur(base * rate / 100), text_align='right')
    row = add(rows, 'table-row', background_color=TEAL, color='#FFFFFF', font_weight='bold')
    cell(row, 'Gesamtbetrag / Zahlbetrag'); cell(row, 'EUR'); cell(row, eur(data['totals']['payable']), text_align='right')
    block(totals, 'Bitte überweisen Sie den Zahlbetrag bis zum ' + day(data['due_date']) + ' ohne Abzug.', space_before='6mm')
    block(totals, 'IBAN: ' + seller['iban'], font_weight='bold', space_before='1mm')
    block(totals, 'Verwendungszweck: ' + data['invoice_number'])
    identifiers = []
    if seller.get('vat_id'): identifiers.append('USt-IdNr.: ' + seller['vat_id'])
    if seller.get('tax_number'): identifiers.append('Steuernummer: ' + seller['tax_number'])
    block(totals, ' · '.join(identifiers), font_size='9pt', color='#5A6870', space_before='5mm')
    if data.get('note'):
        block(totals, data['note'], font_size='9pt', color='#5A6870', space_before='3mm')
    block(body, id='invoice-end')
    fo_path = directory / 'Rechnungsformular.fo'
    fo_path.write_bytes(ET.tostring(root, encoding='utf-8', xml_declaration=True))

    config = ET.Element('fop', version='1.0')
    ET.SubElement(config, 'strict-configuration').text = 'true'
    ET.SubElement(config, 'strict-validation').text = 'true'
    ET.SubElement(config, 'use-cache').text = 'false'
    renderer = ET.SubElement(ET.SubElement(config, 'renderers'), 'renderer', mime='application/pdf')
    fonts = ET.SubElement(renderer, 'fonts')
    resource = 'jar:' + jar.resolve().as_uri() + '!/'
    for suffix, weight in [('Regular', '400'), ('Bold', '700')]:
        font = ET.SubElement(fonts, 'font', {'embed-url': resource + 'fonts/SourceSansPro-' + suffix + '.ttf', 'embedding-mode': 'subset'})
        ET.SubElement(font, 'font-triplet', name='SourceSansPro', style='normal', weight=weight)
    ET.SubElement(renderer, 'output-profile').text = resource + 'AdobeCompat-v2.icc'
    config_path = directory / 'fop-rechnung.xconf'
    config_path.write_bytes(ET.tostring(config, encoding='utf-8', xml_declaration=True))
    return fo_path, config_path
