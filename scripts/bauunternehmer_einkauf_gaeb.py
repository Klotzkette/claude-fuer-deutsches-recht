"""GAEB DA XML 3.3 für die vergleichenden Krimpfort-Beschaffungsakten."""
from __future__ import annotations

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from xml.etree import ElementTree as ET


def _load_door_builder():
    path = Path(__file__).with_name('build-bauunternehmer-einkauf-gaeb.py')
    spec = spec_from_file_location('krimpfort_tueren_gaeb', path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_gaeb = _load_door_builder()
SCHEMA_URL = _gaeb.SCHEMA_URL
element, fields, text, address = _gaeb.element, _gaeb.fields, _gaeb.text, _gaeb.address


def amount(value):
    return Decimal(str(value))


def item_total(position, offer):
    quantity = amount(position['quantity'])
    price = amount(offer['prices'][position['oz']])
    return (quantity * price).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def net_total(case, offer):
    return sum(item_total(position, offer) for position in case['positions'])


def _add_item(parent, position, offer):
    oz = position['oz']
    item = element(parent, 'Item', ID='POS_' + oz.replace('.', '_'), RNoPart=oz.rsplit('.', 1)[-1])
    element(item, 'Qty', f"{amount(position['quantity']):.3f}")
    if offer:
        fields(item, UP=f"{amount(offer['prices'][oz]):.3f}", IT=f'{item_total(position, offer):.2f}')
        if note := offer.get('notes', {}).get(oz):
            text(element(item, 'BidComm'), note)
    else:
        element(item, 'QU', position['unit'])
        complete = element(element(item, 'Description'), 'CompleteText')
        text(element(element(complete, 'DetailTxt'), 'Text'), position['text'])
        outline = element(element(complete, 'OutlineText'), 'OutlTxt')
        text(element(outline, 'TextOutlTxt'), position['short'])


def _add_positions(boq, case, offer):
    body = element(boq, 'BoQBody')
    groups = case.get('groups', {})
    if groups:
        for number, label in groups.items():
            category = element(body, 'BoQCtgy', ID=f'TITEL_{number}', RNoPart=number)
            if not offer:
                text(element(category, 'LblTx'), label)
            items = element(element(category, 'BoQBody'), 'Itemlist')
            group_positions = [position for position in case['positions']
                               if position['oz'].startswith(number + '.')]
            for position in group_positions:
                _add_item(items, position, offer)
            if offer:
                total = f'{sum(item_total(position, offer) for position in group_positions):.2f}'
                fields(element(category, 'Totals'), Total=total, TotalNet=total)
    else:
        items = element(body, 'Itemlist')
        for position in case['positions']:
            _add_item(items, position, offer)


def _make_document(case, offer=None):
    phase = '84' if offer else '83'
    root = ET.Element('GAEB', {'xmlns': f'http://www.gaeb.de/GAEB_DA_XML/DA{phase}/{_gaeb.VERSION}'})
    issue_date = offer['date'][:10] if offer else case['tender_date']
    fields(element(root, 'GAEBInfo'), Version=_gaeb.VERSION, VersDate=_gaeb.ISSUE, Date=issue_date,
           ProgSystem='Krimpfort LV-Export', ProgName=f'Leistungsverzeichnis X{phase}')
    info = element(root, 'PrjInfo')
    fields(info, NamePrj=case['lv_number'], PrjID=case['project_id'], LblPrj=case['project'])
    if not offer:
        element(info, 'BidCommPerm', 'Yes')
    award = element(root, 'Award')
    element(award, 'DP', phase)
    award_info = element(award, 'AwardInfo')
    fields(award_info, BoQID=case['boq_id'], Cur='EUR', CurLbl='Euro')
    if offer:
        element(award_info, 'BidDate', issue_date)
        contractor = element(award, 'CTR')
        address(contractor, offer['name'], offer['email'])
        element(contractor, 'AwardNo', case['lv_number'])
        add_text = element(element(contractor, 'AddText'), 'DetailAddText')
        text(add_text, f"Preisstand {offer['number']}. Bindung und Leistungseinschränkungen stehen im Schriftangebot.")
    else:
        deadline = datetime.fromisoformat(case['bid_deadline'])
        fields(award_info, OpenDate=deadline.date().isoformat(), OpenTime=deadline.strftime('%H:%M:%S'))
        owner = element(award, 'OWN')
        address(owner, case['company'], case['buyer_email'])
        element(owner, 'AwardNo', case['lv_number'])
        element(element(award, 'CnstSite'), 'CnstSiteName', case['project'])
        add_text = element(element(award, 'AddText'), 'DetailAddText')
        for paragraph in case['lv_notes']:
            text(add_text, paragraph)

    boq = element(award, 'BoQ', ID='LV_' + case['lv_number'].replace('-', '_'))
    boq_info = element(boq, 'BoQInfo')
    element(boq_info, 'Name', case['lv_number'])
    if not offer:
        fields(boq_info, LblBoQ=case['title'], Date=issue_date, OutlCompl='AllTxt')
    if case.get('groups'):
        fields(element(boq_info, 'BoQBkdn'), Type='BoQLevel', Length=2, Num='Yes')
    fields(element(boq_info, 'BoQBkdn'), Type='Item', Length=4, Num='Yes')
    if offer:
        total = f'{net_total(case, offer):.2f}'
        fields(element(boq_info, 'Totals'), Total=total, TotalNet=total)
    _add_positions(boq, case, offer)
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='utf-8', xml_declaration=True) + b'\n'


def _read_exchange(data):
    root = ET.fromstring(data)
    ns = {'': root.tag.split('}')[0][1:]}
    award = root.find('Award', ns)
    boq = award.find('BoQ', ns)
    body = boq.find('BoQBody', ns)
    groups = body.findall('BoQCtgy', ns)

    def positions(parent, prefix=''):
        for item in parent.findall('Itemlist/Item', ns):
            oz = prefix + item.attrib['RNoPart']
            yield (oz, item.attrib['ID'], *(item.findtext(field, namespaces=ns)
                                          for field in ('Qty', 'QU', 'UP', 'IT')))

    if groups:
        rows = [row for group in groups for row in positions(group.find('BoQBody', ns), group.attrib['RNoPart'] + '.')]
    else:
        rows = list(positions(body))
    return (
        award.findtext('AwardInfo/BoQID', namespaces=ns),
        boq.findtext('BoQInfo/Name', namespaces=ns),
        rows,
        boq.findtext('BoQInfo/Totals/TotalNet', namespaces=ns),
    )


def _validate_input(case):
    groups = case.get('groups', {})
    positions = case['positions']
    ordinals = [position['oz'] for position in positions]
    pattern = r'\d{2}\.\d{4}' if groups else r'\d{4}'
    if not ordinals or sorted(set(ordinals)) != ordinals or any(not re.fullmatch(pattern, oz) for oz in ordinals):
        raise ValueError('Positions-OZ müssen numerisch, eindeutig und aufsteigend sein.')
    if groups and list(groups) != sorted({oz.split('.')[0] for oz in ordinals}):
        raise ValueError('LV-Gliederung passt nicht zur Reihenfolge der Positionen.')
    if any(amount(position['quantity']) <= 0 for position in positions):
        raise ValueError('Jede Position braucht eine positive Vergleichsmenge.')
    offer_ids = [offer['id'] for offer in case['offers']]
    if len(set(offer_ids)) != 4 or len(offer_ids) != 4:
        raise ValueError('Erwartet werden vier verschiedene Angebotskennungen.')
    for offer in case['offers']:
        if set(offer['prices']) != set(ordinals) or set(offer.get('notes', {})) - set(ordinals):
            raise ValueError(f"Positionen passen nicht zum LV: {offer['number']}")


def _verify_document(case, data, offer=None):
    boq_id, name, rows, total = _read_exchange(data)
    if (boq_id, name) != (case['boq_id'], case['lv_number']):
        raise ValueError('GAEB-Projektbezug weicht vom Leistungsverzeichnis ab.')
    expected = [
        (position['oz'], 'POS_' + position['oz'].replace('.', '_'),
         f"{amount(position['quantity']):.3f}",
         None if offer else position['unit'],
         f"{amount(offer['prices'][position['oz']]):.3f}" if offer else None,
         f'{item_total(position, offer):.2f}' if offer else None)
        for position in case['positions']
    ]
    if rows != expected or total != (f'{net_total(case, offer):.2f}' if offer else None):
        raise ValueError('GAEB-Positionsdaten oder Nettosumme weichen vom Schriftstand ab.')


def exchange_documents(case):
    documents = [(Path('Grundakte/03_Leistungsverzeichnis') / f"LV_{case['lv_number']}.x83", None)]
    documents.extend((Path('Grundakte/04_Angebote') / f"{offer['id']}_{offer['number']}.x84", offer)
                     for offer in case['offers'])
    return documents


def verify_exchange(case, directory):
    """Vergleicht die vorhandenen GAEB-Dateien mit dem dokumentierten Angebotsstand."""
    _validate_input(case)
    for path, offer in exchange_documents(case):
        _verify_document(case, (directory / path).read_bytes(), offer)


def build_exchange(case, output_directory, schema_zip):
    """Prüft alle fünf Austauschdateien vor Übernahme in die Arbeitsakte."""
    _validate_input(case)
    documents = exchange_documents(case)
    with TemporaryDirectory(prefix='krimpfort-vergleich-gaeb-') as stage:
        temporary = Path(stage)
        for path, offer in documents:
            data = _make_document(case, offer)
            _verify_document(case, data, offer)
            (temporary / path.name).write_bytes(data)
        _gaeb.schema_check(schema_zip, temporary, [path.name for path, _ in documents])
        for path, _ in documents:
            target = output_directory / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((temporary / path.name).read_bytes())
    return [path for path, _ in documents]
