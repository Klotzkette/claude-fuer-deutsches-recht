#!/usr/bin/env python3
"""UBL-XRechnung 3.0.2 aus ausdrücklich gelieferten Rechnungsdaten.

Begrenzter Export: EUR, inländische Parteien, positive Positionen, 19 % USt,
keine Vorschussverrechnung, Rabatte, Gutschriften, Reverse Charge oder Kleinunternehmer.
Eine separate KoSIT-Prüfung ist erforderlich; dieses Skript behauptet keine Validierung.
"""
import argparse
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from decimal import Decimal, ROUND_HALF_UP
from datetime import date

NS={'ubl':'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2',
    'cac':'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'}
for key,value in NS.items(): ET.register_namespace(key,value)


def element(parent, kind, name, value=None, **attrs):
    result=ET.SubElement(parent, '{'+NS[kind]+'}'+name, attrs)
    if value is not None: result.text=str(value)
    return result


def text(data,key):
    value=data.get(key)
    if not isinstance(value,str) or not value.strip() or any(ord(c)<32 for c in value):
        raise ValueError(f'{key}: vollständiger Text erforderlich')
    return value


def numeric(value,label):
    if isinstance(value,bool) or value is None: raise ValueError(f'{label}: Zahl fehlt')
    number=Decimal(str(value))
    if not number.is_finite() or number<0: raise ValueError(f'{label}: nichtnegative Zahl erforderlich')
    return number


def amount(value): return str(value.quantize(Decimal('.01'),rounding=ROUND_HALF_UP))


def valid_iban(value):
    compact=re.sub(r'\s','',value).upper()
    if not re.fullmatch(r'DE\d{20}',compact): raise ValueError('Deutsche IBAN mit22Zeichen erforderlich')
    digits=''.join(str(ord(c)-55) if c.isalpha() else c for c in compact[4:]+compact[:4])
    if int(digits)%97!=1: raise ValueError('IBAN-Prüfziffer ungültig')
    return compact


def build(data):
    if data.get('schema_version')!=1: raise ValueError('schema_version=1 erforderlich')
    if data.get('document_state') not in ('draft','approved'): raise ValueError('document_state fehlt')
    if data['document_state']=='approved' and data.get('legal_reviewed') is not True:
        raise ValueError('Freigegebener Export setzt legal_reviewed=true voraus')
    if data.get('currency')!='EUR' or numeric(data.get('vat_rate'),'vat_rate')!=19:
        raise ValueError('Exporter unterstützt nur EUR und inländische19%-Standardfälle')
    for key in ('invoice_number','buyer_reference','issue_date','due_date','period_start','period_end'):
        text(data,key)
    for key in ('issue_date','due_date','period_start','period_end'):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',data[key]):raise ValueError(f'{key}: YYYY-MM-DD erforderlich')
        date.fromisoformat(data[key])
    if data['due_date']<data['issue_date'] or data['period_end']<data['period_start']:
        raise ValueError('Datumsfolge prüfen')
    forbidden=('allowances','prepaid_amount','credit_note','reverse_charge')
    if any(key in data for key in forbidden):raise ValueError('Sonderfall nicht unterstützt; keine stillschweigende Auslassung')
    seller=data['supplier'];buyer=data['customer']
    for party in (seller,buyer):
        for key in ('name','street','postal_code','city','country','email'):text(party,key)
        if party['country']!='DE':raise ValueError('Nur ausdrücklich inländische Parteien unterstützt')
        if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',party['email']):raise ValueError('Elektronische Adresse prüfen')
    for key in ('vat_id','contact','phone','iban'):text(seller,key)
    if not re.fullmatch(r'DE\d{9}',seller['vat_id']):raise ValueError('Deutsche USt-ID erforderlich; Prüfung ihrer Echtheit erfolgt separat')
    iban=valid_iban(seller['iban'])
    source=data.get('lines')
    if not isinstance(source,list) or not source:raise ValueError('Rechnungspositionen fehlen')
    lines=[];ids=set()
    for row in source:
        text(row,'id');text(row,'description');text(row,'unit_code')
        if row['id'] in ids:raise ValueError('Doppelte Positions-ID')
        ids.add(row['id'])
        if row['unit_code'] not in ('C62','HUR','MIN','DAY'):raise ValueError('Einheit C62/HUR/MIN/DAY erforderlich')
        quantity=numeric(row.get('quantity'),'quantity');price=numeric(row.get('unit_price_net'),'unit_price_net')
        if quantity<=0:raise ValueError('Menge muss positiv sein')
        if price.as_tuple().exponent < -6 or quantity.as_tuple().exponent < -6:
            raise ValueError('Menge und Einzelpreis: höchstens sechs Nachkommastellen')
        net=(quantity*price).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
        lines.append((row,quantity,price,net))
    total=sum((line[3] for line in lines),Decimal(0));tax=(total*Decimal('.19')).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
    root=ET.Element('{'+NS['ubl']+'}Invoice')
    b=lambda p,n,v=None,**a:element(p,'cbc',n,v,**a)
    a=lambda p,n:element(p,'cac',n)
    b(root,'CustomizationID','urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0')
    b(root,'ProfileID','urn:fdc:peppol.eu:2017:poacc:billing:01:1.0')
    b(root,'ID',data['invoice_number']);b(root,'IssueDate',data['issue_date']);b(root,'DueDate',data['due_date']);b(root,'InvoiceTypeCode','380')
    if data['document_state']=='draft':b(root,'Note','ENTWURF. Nicht versenden. Rechnungsdaten, Fälligkeit und rechtliche Grundlage noch abschließend prüfen.')
    b(root,'DocumentCurrencyCode','EUR');b(root,'BuyerReference',data['buyer_reference'])
    period=a(root,'InvoicePeriod');b(period,'StartDate',data['period_start']);b(period,'EndDate',data['period_end'])
    for name,p in (('AccountingSupplierParty',seller),('AccountingCustomerParty',buyer)):
        party=a(a(root,name),'Party');b(party,'EndpointID',p['email'],schemeID='EM')
        pn=a(party,'PartyName');b(pn,'Name',p['name'])
        address=a(party,'PostalAddress');b(address,'StreetName',p['street']);b(address,'CityName',p['city']);b(address,'PostalZone',p['postal_code']);b(a(address,'Country'),'IdentificationCode',p['country'])
        if name=='AccountingSupplierParty':
            ts=a(party,'PartyTaxScheme');b(ts,'CompanyID',seller['vat_id']);b(a(ts,'TaxScheme'),'ID','VAT')
        b(a(party,'PartyLegalEntity'),'RegistrationName',p['name'])
        if name=='AccountingSupplierParty':
            contact=a(party,'Contact');b(contact,'Name',p['contact']);b(contact,'Telephone',p['phone']);b(contact,'ElectronicMail',p['email'])
    means=a(root,'PaymentMeans');b(means,'PaymentMeansCode','58');b(a(means,'PayeeFinancialAccount'),'ID',iban)
    b(a(root,'PaymentTerms'),'Note','Zahlbar bis '+data['due_date']+' ohne Abzug.')
    tax_total=a(root,'TaxTotal');b(tax_total,'TaxAmount',amount(tax),currencyID='EUR')
    sub=a(tax_total,'TaxSubtotal');b(sub,'TaxableAmount',amount(total),currencyID='EUR');b(sub,'TaxAmount',amount(tax),currencyID='EUR')
    category=a(sub,'TaxCategory');b(category,'ID','S');b(category,'Percent','19');b(a(category,'TaxScheme'),'ID','VAT')
    legal=a(root,'LegalMonetaryTotal')
    for name,value in [('LineExtensionAmount',total),('TaxExclusiveAmount',total),('TaxInclusiveAmount',total+tax),('PayableAmount',total+tax)]:b(legal,name,amount(value),currencyID='EUR')
    for row,quantity,price,net in lines:
        line=a(root,'InvoiceLine');b(line,'ID',row['id']);b(line,'InvoicedQuantity',str(quantity),unitCode=row['unit_code']);b(line,'LineExtensionAmount',amount(net),currencyID='EUR')
        item=a(line,'Item');b(item,'Name',row['description']);ct=a(item,'ClassifiedTaxCategory');b(ct,'ID','S');b(ct,'Percent','19');b(a(ct,'TaxScheme'),'ID','VAT')
        b(a(line,'Price'),'PriceAmount',str(price),currencyID='EUR')
    ET.indent(root,space='  ')
    return ET.tostring(root,encoding='utf-8',xml_declaration=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();payload=json.loads(args.input.read_text(encoding='utf-8'))
    result=build(payload)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    # Existing outputs are immutable; use a new version filename for corrections.
    with args.output.open('xb') as stream:stream.write(result)
    print(json.dumps({'file':str(args.output),'document_state':payload['document_state'],'kosit_validated':False,'next':'KoSIT-Validator mit aktueller XRechnung-Konfiguration ausführen'},ensure_ascii=False))


if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError,ArithmeticError) as exc:
        print(f'Fehler: {exc}',file=sys.stderr);sys.exit(2)
