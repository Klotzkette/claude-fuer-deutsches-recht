#!/usr/bin/env python3
"""Erzeugt die Hamburger Behälterakte mit zeitlich getrennten Eingängen.

Die Rohdaten und alle Beträge entstehen aus denselben Einzelereignissen. Eine
rechtliche Verteidigung oder abschließende Forderungsberechnung wird nicht
in die Arbeitsakte geschrieben. QA und XLSX-Zwischendaten liegen extern.
"""
from __future__ import annotations

import argparse
import calendar
import csv
from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
from email import policy
from email.message import EmailMessage
import hashlib
import importlib.util
import json
import mimetypes
import os
from pathlib import Path
import subprocess
from xml.sax.saxutils import escape

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from testakte_download_notices import ensure_download_notices

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'forderungsmanagement-baeckerei-behaeltertausch-hamburg'
CASE = ROOT / 'testakten' / SLUG
G = 'Grundakte'
P = '01_Gerichtseingang_2026-11-06'
N = '02_Nachlieferung_2026-11-12_und_13'
BAKERY = 'Backbord Backstube GmbH'
BA = 'Billstraße 137\n20539 Hamburg'
WASTE = 'Elbmarsch Wertstofflogistik GmbH'
WA = 'Andreas-Meyer-Straße 48\n22113 Hamburg'
HOSPITAL = 'Klinikum Alsterbogen Hamburg gGmbH'
HA = 'Alsterdorfer Straße 463\n22337 Hamburg'
LAW = 'VOSSEN & KLINK\nRechtsanwälte Partnerschaft mbB'
LA = 'Herrengraben 36 · 20459 Hamburg\nkanzlei@vossen-klink.example · Telefon 040 5550 2160'
BANK = 'Hanseufer Bank eG'
MONTHS = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September']
H_COUNTS = [22,20,23,22,21,22,23,21,22]
B_COUNTS = [9,8,9,9,8,9,9,9,8]
CREATED = []


def eur(cents):
    return f'{cents / 100:,.2f}'.replace(',', '~').replace('.', ',').replace('~', '.')


def dd(value):
    return date.fromisoformat(value).strftime('%d.%m.%Y')


def register_fonts():
    directory = Path(os.environ.get('HAMBURG_FONT_DIR', '/System/Library/Fonts/Supplemental'))
    for suffix, filename in [('', 'Times New Roman.ttf'), ('B','Times New Roman Bold.ttf'), ('I','Times New Roman Italic.ttf')]:
        source = directory / filename
        if not source.is_file():
            raise RuntimeError('Times New Roman fehlt; HAMBURG_FONT_DIR auf lizenzierte Original-TTFs setzen')
        pdfmetrics.registerFont(TTFont('Hamburg'+suffix, str(source)))
    pdfmetrics.registerFontFamily('Hamburg',normal='Hamburg',bold='HamburgB',italic='HamburgI',boldItalic='HamburgB')


def record(path, title):
    CREATED.append({'path': str(path.relative_to(CASE)), 'title': title})


def styles():
    return {
      'body': ParagraphStyle('body',fontName='Hamburg',fontSize=11,leading=15,spaceAfter=9,textColor=colors.HexColor('#172B35')),
      'title': ParagraphStyle('title',fontName='HamburgB',fontSize=17,leading=21,spaceAfter=17,textColor=colors.HexColor('#172B35')),
      'h': ParagraphStyle('h',fontName='HamburgB',fontSize=12,leading=16,spaceBefore=10,spaceAfter=9,keepWithNext=True),
      'small': ParagraphStyle('small',fontName='Hamburg',fontSize=9,leading=12,spaceAfter=7),
      'tiny': ParagraphStyle('tiny',fontName='Hamburg',fontSize=8,leading=10,spaceAfter=2),
    }


def pdf(name,title,issuer,address,recipient,ref,day,blocks,*,color='#234F65',wide=False,signature=None):
    path = CASE / name; path.parent.mkdir(parents=True,exist_ok=True)
    size = landscape(A4) if wide else A4
    width = size[0]-108
    st = styles()
    p = lambda text,style='body': Paragraph(escape(str(text)).replace('\n','<br/>'),st[style])
    flow = [p(recipient,'small'),Spacer(1,8),p(f'{dd(day)} · {ref}','small'),p(title,'title')]
    for block in blocks:
        if isinstance(block,str): flow.append(p(block))
        elif 'heading' in block: flow.append(p(block['heading'],'h'))
        elif 'page' in block: flow.append(PageBreak())
        else:
            rows = [block['headers'],*block['rows']]
            weights = block.get('widths',[1]*len(rows[0])); total=sum(weights)
            table = Table([[p(v,'tiny' if wide or len(rows[0])>5 else 'small') for v in row] for row in rows],colWidths=[width*w/total for w in weights],repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E7EEF1')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor(color)),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F6F8F8')])]))
            flow.extend([table,Spacer(1,12)])
    if signature: flow.extend([Spacer(1,12),p(signature)])
    def frame(canvas,doc):
        canvas.saveState(); canvas.setFillColor(colors.HexColor(color))
        canvas.rect(0,size[1]-24,size[0],24,fill=1,stroke=0)
        brand=issuer.split('\n')
        canvas.setFont('HamburgB',16); canvas.drawString(54,size[1]-52,brand[0])
        canvas.setFont('Hamburg',9)
        if len(brand)>1: canvas.drawString(54,size[1]-66,brand[1])
        canvas.drawString(54,size[1]-81,address.replace('\n',' · '))
        canvas.setFont('Hamburg',8); canvas.setFillColor(colors.HexColor('#50616B'))
        canvas.drawString(54,35,ref); canvas.drawRightString(size[0]-54,35,f'Seite {doc.page}')
        canvas.restoreState()
    SimpleDocTemplate(str(path),pagesize=size,leftMargin=54,rightMargin=54,topMargin=105,bottomMargin=55,title=title,author=issuer,creator='Klotzkette',invariant=1).build(flow,onFirstPage=frame,onLaterPages=frame)
    record(path,title); return path


def heading(text): return {'heading':text}


def word(name,title,blocks):
    path=CASE/name; path.parent.mkdir(parents=True,exist_ok=True)
    d=Document(); sec=d.sections[0]; sec.page_width=Cm(21); sec.page_height=Cm(29.7)
    sec.left_margin=sec.right_margin=Cm(2.2); sec.top_margin=Cm(2.5);sec.bottom_margin=Cm(2)
    for s in d.styles:
        if s.type==1:
            s.font.name='Times New Roman';s.font.size=Pt(11);s.font.color.rgb=RGBColor.from_string('172B35');s.paragraph_format.space_after=Pt(9);s.paragraph_format.line_spacing=1.15
            fonts=s.element.get_or_add_rPr().get_or_add_rFonts()
            for key in list(fonts.attrib):
                if key.endswith('Theme'):del fonts.attrib[key]
            for key in ('ascii','hAnsi','eastAsia','cs'):fonts.set(qn('w:'+key),'Times New Roman')
            for border in s.element.xpath('./w:pPr/w:pBdr'):border.getparent().remove(border)
    d.styles['Title'].font.size=Pt(17);d.styles['Title'].font.bold=True
    d.styles['Heading 1'].font.size=Pt(12);d.styles['Heading 1'].font.bold=True
    sec.header.paragraphs[0].text='BACKBORD BACKSTUBE\nBillstraße 137 · 20539 Hamburg'
    d.add_paragraph(title,'Title')
    for block in blocks:
        d.add_paragraph(block['heading'],'Heading 1') if isinstance(block,dict) else d.add_paragraph(block)
    f=sec.footer.paragraphs[0];f.text='Backbord Backstube GmbH · Geschäftsführung · Seite '
    field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');f._p.append(field)
    d.core_properties.author=d.core_properties.last_modified_by='Klotzkette';d.core_properties.created=d.core_properties.modified=datetime(2026,11,6,10,0)
    d.save(path);record(path,title)


def mail(name,day,sender,recipient,subject,body,attachments=()):
    msg=EmailMessage(policy=policy.SMTP)
    msg['From']=sender;msg['To']=recipient;msg['Date']=datetime.fromisoformat(day)
    mail_id=hashlib.sha256(name.encode()).hexdigest()[:18]
    msg['Subject']=subject;msg['Message-ID']=f'<{mail_id}@backbord-akten.example>'
    msg.set_content(body)
    for attachment in attachments:
        path=CASE/attachment;mime=mimetypes.guess_type(str(path))[0] or 'application/octet-stream';main,sub=mime.split('/',1)
        msg.add_attachment(path.read_bytes(),maintype=main,subtype=sub,filename=path.name)
    if attachments:msg.set_boundary('=_hamburg_'+mail_id)
    path=CASE/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(msg.as_bytes());record(path,subject)


def csv_out(name,headers,rows):
    path=CASE/name;path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f,delimiter=';');w.writerow(headers);w.writerows(rows)
    record(path,path.stem)


def events():
    rows=[]
    for month in range(1,10):
        workdays=[date(2026,month,day) for day in range(1,calendar.monthrange(2026,month)[1]+1) if date(2026,month,day).weekday()<5]
        for site,count,kg,serial,qr,cust,lat,lon in [
            ('KA-LH',H_COUNTS[month-1],440,'EW-1100-0842','QR-71A9','B1047','53.6107','10.0188'),
            ('BB-HOF',B_COUNTS[month-1],130,'EW-1100-0841','QR-71B0','K2088','53.5408','10.0449')]:
            for i in range(count):
                bakery_days=[date(2026,month,day) for day in range(1,calendar.monthrange(2026,month)[1]+1) if date(2026,month,day).weekday() in (0,3)]
                day=workdays[min(i,len(workdays)-1)] if site=='KA-LH' else bakery_days[i]
                if site=='BB-HOF' and day==date(2026,1,1):day=date(2026,1,2)
                # Net weights vary in paired steps, preserving each month's total.
                weight=kg+([-20,20][i%2] if i<count-(count%2) else 0)
                rows.append({'id':f'EW-{month:02}-{site}-{i+1:02}','date':day.isoformat(),'time':f'{6 if site=="KA-LH" else 8:02}:{12+i%7:02}:00','tour':'H03' if site=='KA-LH' else 'H07','serial':serial,'qr':qr,'billed_customer':cust,'physical_site':site,'kg':weight,'lat':lat,'lon':lon,'driver':'F-17' if site=='KA-LH' else 'F-29'})
    return sorted(rows,key=lambda r:(r['date'],r['time']))


def billing(rows):
    invoices=[]
    for month in range(1,10):
        subset=[r for r in rows if int(r['date'][5:7])==month and r['billed_customer']=='B1047']
        kg=sum(r['kg'] for r in subset); net=12000+4800*len(subset)+kg*Decimal('21.5')
        net=int(net);vat=int((Decimal(net)*Decimal('.19')).quantize(Decimal('1'),rounding=ROUND_HALF_UP));gross=net+vat
        last=date(2026,month,calendar.monthrange(2026,month)[1]);due=last+timedelta(days=14)
        payment=gross if month<3 else 80000
        invoices.append({'month':month,'number':f'EW-26-{month:02}-1047','date':last.isoformat(),'due':due.isoformat(),'lifts':len(subset),'kg':kg,'net':net,'vat':vat,'gross':gross,'paid':payment,'payment_date':f'2026-{month+1:02}-12','open':gross-payment})
    return invoices


def contracts():
    pdf(f'{G}/01_Entsorgungsvertrag_2025-12-12.pdf','Entsorgungsvertrag Gewerbeabfall',WASTE,WA,BAKERY+'\n'+BA,'EW-B1047 / Vertrag 2025-118','2025-12-12',[
      heading('1 Vertragsparteien und Betrieb'),
      f'{WASTE}, Andreas-Meyer-Straße 48, 22113 Hamburg, vertreten durch ihre Geschäftsführerin Britta Fleetmann, übernimmt für {BAKERY}, Billstraße 137, 20539 Hamburg, vertreten durch ihre Geschäftsführerin Jette Finkenwerder, die nachstehend bestimmten Entsorgungsleistungen. Leistungsort ist ausschließlich der rückwärtige Betriebshof der Backstube an der Billstraße. Die Kundennummer lautet B1047.',
      'Die Backstube beliefert ihren Laden und vier Verkaufsstellen. Verpackungen aus den Verkaufsstellen werden teilweise zur Backstube zurückgebracht. Der Auftraggeber erklärt, dass im Gewerberestabfall keine gefährlichen Abfälle enthalten sind. Lebensmittelreste und Altbrot werden getrennt gesammelt und sind nicht Gegenstand dieses Vertrags. Ein etwaiger öffentlich-rechtlicher Anschluss- oder Benutzungszwang wird durch diesen Vertrag nicht abgeändert.',
      heading('2 Geschuldete Leistung und Behälter'),
      'Die Auftragnehmerin stellt einen verschließbaren 1.100-Liter-Umleerbehälter bereit. Sie leert den bereitgestellten Behälter montags und donnerstags, befördert den Inhalt zu einer dafür zugelassenen Anlage und führt ihn dort der vereinbarten Verwertung oder Beseitigung zu. Vertragsgegenstand ist nicht allein die Bereitstellung eines Fahrzeugs, sondern die tatsächliche Übernahme und ordnungsgemäße Entsorgung der bereitgestellten Abfälle.',
      'Die Behälternummer und der bei Aufstellung angebrachte elektronische Identifikator werden im Übergabeprotokoll festgehalten. Beide Parteien bewahren dieses Protokoll auf. Die Auftragnehmerin bleibt Eigentümerin des Behälters. Sie beseitigt Verschleiß und ersetzt einen unbrauchbaren Behälter auf eigene Kosten. Änderungen des elektronischen Identifikators dürfen die physische Behälter- und Standortzuordnung nicht verändern.',
      heading('2.1 Bereitstellung und Ausfall'),
      'Der Auftraggeber öffnet an Abholtagen von 07:30 bis 10:30 Uhr den Hofzugang und stellt den Behälter an der markierten Position bereit. Fällt ein Abholtag auf einen Feiertag, teilt die Auftragnehmerin den Ersatztermin spätestens zwei Werktage zuvor per E-Mail mit. Eine erfolglose Anfahrt wird nur dann nach Anlage 1 berechnet, wenn der Zugang schuldhaft versperrt war und die Fahrerin oder der Fahrer die erfolglose Anfahrt mit Zeit, Standort und Foto dokumentiert hat. Eine bloße Scannerzeile genügt hierfür nicht.',
      heading('2.2 Zusätzliche Leerungen'),
      'Zusätzliche Leerungen bedürfen einer Bestellung durch Jette Finkenwerder, Betriebsleiter Cem Kavel oder die Buchhaltung unter buchhaltung@backbord.example. Die Auftragnehmerin bestätigt den Termin per E-Mail. Abgerechnet wird je tatsächlich ausgeführter zusätzlicher Leerung. Eine automatisch erfasste Leistungszeile ersetzt keine Bestellung. Das reguläre Leerungsentgelt bleibt mengenabhängig, auch wenn die Anzahl der Abholtage kalendermonatlich schwankt.',
      heading('3 Preis und Abrechnung'),
      'Es gelten ausschließlich die bei Abschluss beiderseits unterzeichnete Anlage 1 und die Leistungsbeschreibung in diesem Vertrag. Die Preise bleiben bis zum 31. Dezember 2026 unverändert. Ein Energie-, Maut- oder Verwaltungskostenaufschlag ist nicht vereinbart. Sämtliche Entgelte verstehen sich zuzüglich der gesetzlichen Umsatzsteuer. Die Auftragnehmerin rechnet monatlich nachträglich ab und fügt ein Leistungsjournal mit Datum, Behälterkennung, Leerungszahl und Nettogewicht bei.',
      'Das Nettogewicht wird aus der geeichten Fahrzeugwaage als Differenz vor und nach Entleerung ermittelt. Es ist in Kilogramm zu dokumentieren; je Rechnung wird die Summe durch 1.000 geteilt und mit dem Tonnenpreis multipliziert. Es erfolgt keine Aufrundung jeder einzelnen Leerung auf volle Tonnen oder 100 Kilogramm. Die Rechnung ist 14 Kalendertage nach ihrem Zugang per Überweisung zu zahlen. Der Auftragnehmerin wird kein Lastschriftmandat erteilt.',
      heading('4 Beanstandungen und Belege'),
      'Die Parteien teilen erkennbare Abweichungen unverzüglich mit und prüfen sie anhand der Originaldaten. Aus dem Unterlassen einer Beanstandung folgt weder eine Genehmigung nicht ausgeführter Leistungen noch ein Verzicht auf Einwendungen. Bei Streit über die Leistungszuordnung stellt die Auftragnehmerin dem Auftraggeber die ihn betreffenden Tour- und Wiegedaten in lesbarer Form bereit. Daten anderer Kunden werden nur übermittelt, soweit hierfür eine rechtliche Grundlage oder deren Einwilligung vorliegt.',
      heading('5 Haftung und Versicherung'),
      'Jede Partei haftet nach den gesetzlichen Vorschriften für die Verletzung ihrer Pflichten. Die Auftragnehmerin unterhält eine Betriebshaftpflichtversicherung mit einer Deckungssumme von 5 Millionen EUR je Schadenereignis. Eine Haftungsbegrenzung zulasten des Auftraggebers ist mit dieser Angabe nicht vereinbart. Die Auftragnehmerin setzt nur erforderliche und berechtigte Beschäftigte oder beauftragte Transportunternehmen ein und bleibt für die ordnungsgemäße Leistung verantwortlich.',
      heading('6 Laufzeit und Beendigung'),
      'Der Vertrag beginnt am 1. Januar 2026 und endet ohne Kündigung am 31. Dezember 2026. Eine Fortsetzung bedarf einer Vereinbarung. Das Recht zur Kündigung aus wichtigem Grund bleibt bestehen. Bei Zahlungsverzug setzt die Auftragnehmerin vor einer Leistungseinstellung eine angemessene schriftliche Nachfrist und weist auf die beabsichtigte Einstellung hin. Eine Einstellung entbindet nicht von der Rückgabe des Behälters; der Abholtermin ist mit dem Betrieb abzustimmen.',
      heading('7 Datenschutz und Vertragsunterlagen'),
      'Kontaktdaten der verantwortlichen Beschäftigten werden zur Vertragsabwicklung verwendet. Eine Übermittlung von Beschäftigten- oder Kundendaten an fremde Geschäftspartner zu Werbezwecken findet nicht statt. Vertragsänderungen werden in Textform festgehalten, soweit nicht gesetzlich eine strengere Form verlangt wird. Individuelle Abreden haben Vorrang. Bestandteil dieses Vertrags sind Anlage 1 Preisblatt vom 12. Dezember 2025 und das Übergabeprotokoll vom 29. Dezember 2025. Weitere allgemeine Geschäftsbedingungen werden nicht einbezogen.',
      'Hamburg, 12. Dezember 2025\nFür Elbmarsch Wertstofflogistik GmbH: Britta Fleetmann, Geschäftsführerin\nFür Backbord Backstube GmbH: Jette Finkenwerder, Geschäftsführerin',
    ])
    pdf(f'{G}/02_Preisblatt_unterzeichnet.pdf','Anlage 1 Preise und Abrechnung',WASTE,WA,BAKERY+'\n'+BA,'EW-B1047 / Anlage 1','2025-12-12',[
      'Dieses Preisblatt ist Bestandteil des Vertrags EW-B1047/2025-118. Es gilt für die im Vertrag bezeichnete Betriebsstätte und den einen überlassenen Behälter. Alle folgenden Preise sind Nettopreise.',
      {'headers':['Leistung','Einheit','Preis EUR'], 'rows':[['Behältermiete und Grundservice','je Kalendermonat','120,00'],['Tatsächliche Leerung einschließlich Transport','je Leerung','48,00'],['Verwertung oder Beseitigung','je Tonne Nettogewicht','215,00'],['Schuldhaft verursachte vergebliche Anfahrt mit Nachweis','je Ereignis','35,00'],['Reguläre Aufstellung und Rücknahme','einmalig','0,00']], 'widths':[3,2,1]},
      heading('1 Berechnung'),
      'Leerungs- und Gewichtsanteil werden nebeneinander berechnet. Eine zusätzliche Leerung wird nach denselben Einheitspreisen wie die reguläre Leerung vergütet. Für ein nicht genutztes reguläres Abholfenster fällt kein Leerungsentgelt an. Der Grundservice bleibt bei einer vorübergehenden Betriebsunterbrechung geschuldet, solange der Vertrag und die Behältergestellung fortbestehen.',
      heading('2 Rechnungsinhalt'),
      'Die Rechnung weist den Monat, die Anzahl der ausgeführten Leerungen und das Gesamtgewicht aus. Das beigefügte Leistungsjournal ermöglicht die Zuordnung zu den einzelnen Ereignissen. Die gesetzliche Umsatzsteuer von derzeit 19 Prozent wird erst auf den Nettorechnungsbetrag berechnet und auf zwei Dezimalstellen gerundet.',
      'Für die Auftragnehmerin: Britta Fleetmann\nFür die Auftraggeberin: Jette Finkenwerder\nHamburg, 12. Dezember 2025',
    ])
    pdf(f'{G}/03_Behaelteruebergabe_2025-12-29.pdf','Behälterübergabe am Betriebshof',WASTE,WA,BAKERY+'\n'+BA,'Übergabe 1047-01','2025-12-29',[
      'Am 29. Dezember 2025 um 09:20 Uhr wurde der folgende Behälter im rückwärtigen Hof der Backstube aufgestellt. Die eingeprägte Seriennummer wurde bei der Übergabe vom Metallträger am Deckelscharnier abgelesen. Der schwarze Kunststoffbehälter trägt ein blaues Klebeetikett und einen mechanischen Schließzylinder.',
      {'headers':['Merkmal','Feststellung'],'rows':[['Seriennummer','EW-1100-0841'],['Elektronische Kennung auf Etikett','QR-71B0'],['Kundennummer auf Arbeitsauftrag','B1047'],['Standort','Billstraße 137, hinteres Rolltor, links neben Rampe'],['Behälterart','1.100 Liter, Gewerberestabfall'],['Schlüssel','2 Stück, Schlüsselnummer B-41'],['Zustand','Deckel und Rollen funktionsfähig; linker Seitenholm mit weißem Farbfleck']]},
      'Die Auftraggeberin hat den Aufstellort und den Lieferumfang bestätigt. Dieses Protokoll enthält keinen Nachweis späterer Leerungen. Der Fahrer hat den Auftrag auf seinem Handgerät abgeschlossen; die Büroerfassung des Bestands erfolgt durch die Disposition.',
    ],signature='Cem Kavel, Betriebsleiter Backbord Backstube GmbH\nOle Kiehn, Fahrer Elbmarsch Wertstofflogistik GmbH')


def invoices_and_bank(invoices,rows):
    for invoice in invoices:
        m=invoice['month'];month=MONTHS[m-1]; subset=[r for r in rows if r['date'][5:7]==f'{m:02}' and r['billed_customer']=='B1047']
        pdf(f'{G}/Rechnungen/{invoice["number"]}.pdf',f'Rechnung {invoice["number"]}',WASTE,WA,BAKERY+'\n'+BA,invoice['number'],invoice['date'],[
          f'Leistungszeitraum: 1. bis {calendar.monthrange(2026,m)[1]}. {month} 2026. Kundenkonto B1047. Leistungsstelle laut Abrechnungssystem: Billstraße 137, 20539 Hamburg. Elektronischer Behälteridentifikator QR-71A9.',
          {'headers':['Leistung','Menge','Einzelpreis EUR','Netto EUR'],'rows':[['Grundservice und Behälter','1 Monat','120,00','120,00'],['Leerungen',str(invoice['lifts']),'48,00',eur(invoice['lifts']*4800)],['Entsorgung',f'{invoice["kg"]/1000:.3f} t'.replace('.',','),'215,00',eur(invoice['kg']*Decimal('21.5'))],['Nettobetrag','','',eur(invoice['net'])],['Umsatzsteuer 19 %','','',eur(invoice['vat'])],['Rechnungsbetrag','','',eur(invoice['gross'])]],'widths':[2.5,1.2,1.3,1.3]},
          f'Bitte überweisen Sie {eur(invoice["gross"])} EUR bis zum {dd(invoice["due"])} unter Angabe der Rechnungsnummer. Bankverbindung: Hanseufer Bank eG, IBAN DE33 2009 9900 0000 2610 47. Die Rechnung wurde am Rechnungsdatum an buchhaltung@backbord.example versandt.',
          'Leistungsdaten aus der Monatsabrechnung sind auf dem folgenden Blatt aufgeführt. Eine Korrektur wird nach Prüfung durch den Kundenservice gesondert erteilt. Elbmarsch Wertstofflogistik GmbH · Geschäftsführerin Britta Fleetmann · USt-IdNr. DE321654987.',
          {'page':True},heading('1 Leistungsjournal zur Rechnung'),
          {'headers':['Ereignis','Datum','QR-Kennung','Leerungen','Netto kg'],'rows':[[r['id'],dd(r['date']),r['qr'],'1',str(r['kg'])] for r in subset],'widths':[2.2,1.2,1.2,1,1]},
          'Export aus EW Abrechnung 4.2; Auftragskonto B1047; monatlicher Abrechnungslauf. Die Standortanschrift dieses Ausdrucks stammt aus dem Kundenstamm. Geografische Messdaten und eingeprägte Behälternummern sind in diesem Drucklayout nicht enthalten.',
        ])
    balance=3245087
    for invoice in invoices:
        old=balance;balance-=invoice['paid']
        pdf(f'{G}/Bank/Kontoauszug_{invoice["payment_date"][:7]}.pdf','Geschäftskonto Buchungsauszug',BANK,'Steinhöft 7 · 20459 Hamburg',BAKERY+'\n'+BA,f'Konto 00491047 / Auszug {invoice["month"]+1:02}/2026',invoice['payment_date'],[
          'Auszug aus dem vollständigen Geschäftskonto; Auswahl der Buchungen an Elbmarsch Wertstofflogistik GmbH. Weitere Buchungen dieses Monats sind in diesem Abruf nicht enthalten. Der vor und nach der ausgewählten Buchung angezeigte Saldo bezieht sich auf den dargestellten Buchungstag.',
          {'headers':['Buchung / Wert','Zahlungsempfänger und Zweck','Betrag EUR'],'rows':[[dd(invoice['payment_date'])+' / '+dd(invoice['payment_date']),WASTE+'\n'+invoice['number']+' · '+('Zahlung Rechnung' if invoice['month']<3 else 'Abschlag unter Vorbehalt der Rechnungsprüfung'),'-'+eur(invoice['paid'])]],'widths':[1.5,3.5,1.2]},
          f'Saldo unmittelbar davor: {eur(old)} EUR\nSaldo unmittelbar danach: {eur(balance)} EUR\nKonto-IBAN: DE57 2009 9900 0000 4910 47\nEmpfänger-IBAN: DE33 2009 9900 0000 2610 47',
          f'Ausführungsstatus: gebucht. Bankreferenz HB26-{invoice["month"]+1:02}12-1047. Dieser Kontoauszug bestätigt den Zahlungsfluss; er enthält keine Aussage zur Berechtigung der zugrunde liegenden Rechnung.',
        ],color='#2D5650')


def correspondence(invoices):
    total=sum(i['open'] for i in invoices)
    mail(f'{G}/04_Startbestätigung.eml','2025-12-30T14:18:00+01:00','Mara Kroll <service@elbmarsch.example>','Cem Kavel <betrieb@backbord.example>','Start der Entsorgung ab Januar / B1047',
      'Guten Tag Herr Kavel,\n\nder Behälter steht. Ab Januar fährt Sie unsere Billbrook-Tour montags und donnerstags an. Wegen Neujahr ist der erste Termin Freitag, 2. Januar. Die Klinikroute arbeitet auch an Feiertagen; Ihr Hof wird dagegen wie vereinbart nach dem gesondert mitgeteilten Plan bedient. Bitte entsorgen Sie Altbrot weiterhin getrennt. Im Anhang erhalten Sie den vollständigen Vertrag samt Preisblatt und das Protokoll.\n\nMit freundlichen Grüßen\nMara Kroll',
      [f'{G}/01_Entsorgungsvertrag_2025-12-12.pdf',f'{G}/02_Preisblatt_unterzeichnet.pdf',f'{G}/03_Behaelteruebergabe_2025-12-29.pdf'])
    mail(f'{G}/05_Reklamation_Maerz.eml','2026-03-04T10:12:00+01:00','Anne Kopp <buchhaltung@backbord.example>','Mara Kroll <service@elbmarsch.example>','Rechnungen Januar und Februar ungewöhnlich hoch',
      'Guten Tag Frau Kroll,\n\nich habe die zweite Rechnung zunächst im üblichen Freigabelauf eingeplant. Frau Finkenwerder fragt aber inzwischen, weshalb wir auf mehr als 20 Leerungen pro Monat und so viel Gewicht kommen. Wir haben nur einen schwarzen Behälter am hinteren Tor. Die neuen Cateringaufträge und die Rückläufe aus den Läden erklären Mehrabfall, aber nicht ohne Weiteres diese Werte. Herr Kavel sagt, manchmal kämen die Fahrer zu anderen Zeiten. Können Sie uns bitte die Belege schicken?\n\nViele Grüße\nAnne Kopp')
    mail(f'{G}/06_Serviceantwort_Maerz.eml','2026-03-06T16:43:00+01:00','Mara Kroll <service@elbmarsch.example>','Anne Kopp <buchhaltung@backbord.example>','AW: Rechnungen Januar und Februar ungewöhnlich hoch',
      'Guten Tag Frau Kopp,\n\nlaut unserem Kundenportal sind die Leerungen elektronisch erfasst. Die Zuordnung erfolgt über die Kennung am Behälter. Bei mehreren Bereitstellungen in einer Woche können auch mehr als acht Leerungen entstehen. Ich habe die Tourenprüfung an die Disposition weitergegeben. Eine Korrekturfreigabe liegt mir bislang nicht vor. Die Rechnung bleibt zunächst offen beziehungsweise fällig.\n\nFreundliche Grüße\nMara Kroll')
    mail(f'{G}/07_Abschlag_und_Belegbitte.eml','2026-04-10T11:30:00+02:00','Jette Finkenwerder <jette@backbord.example>','Mara Kroll <service@elbmarsch.example>','B1047: Zahlungen ab März und fehlende Leistungsbelege',
      'Sehr geehrte Frau Kroll,\n\nab der Märzrechnung zahlen wir vorläufig monatlich 800 Euro ausdrücklich auf die jeweilige Rechnung. Das ist eine Zahlung unter Vorbehalt, kein Anerkenntnis des Restes. Wir wissen ohne die Belege nicht, was genau stimmt. Bitte übersenden Sie die einzelnen Wiegenachweise, Tourzeiten und Bestellungen für zusätzliche Leerungen. Ich bestreite nicht, dass Sie Müll bei uns abholen. Wir wollen die bei uns ausgeführten Leistungen bezahlen. Wir bestreiten aber Ihre Mengen und die vielen zusätzlichen Abholungen.\n\nMit freundlichen Grüßen\nJette Finkenwerder')
    mail(f'{G}/08_Fahrernotiz_Juni.eml','2026-06-18T09:37:00+02:00','Cem Kavel <betrieb@backbord.example>','Jette Finkenwerder <jette@backbord.example>','Müllabholung heute Morgen',
      'Jette,\n\nheute war der Wagen gegen halb neun hier. Fahrer sagte, seit Jahresanfang sei ein anderes Handgerät im Einsatz. An der Tonne war nach wie vor das alte blaue Schild. Den Zettel hat er nicht dagelassen; unterschrieben habe ich nichts. Ich kann nicht jeden Montag sehen, ob er da ist, weil ich dann oft bei den Verkaufsstellen bin. Donnerstag ist meist Nils hinten im Lager.\n\nCem')
    pdf(f'{G}/09_Mahnung_2026-10-19.pdf','Zahlungsaufforderung zum Kundenkonto B1047',WASTE,WA,BAKERY+'\n'+BA,'Mahnlauf 26-1047-09','2026-10-19',[
      'Sehr geehrte Frau Finkenwerder,',
      f'aus den Rechnungen für Januar bis September 2026 verbleibt nach unseren Büchern ein offener Betrag von {eur(total)} EUR. Die folgende Aufstellung berücksichtigt sämtliche bis zum 15. Oktober 2026 auf diese Rechnungen gebuchten Zahlungen.',
      {'headers':['Rechnung','Brutto EUR','Zahlung EUR','Offen EUR'],'rows':[[i['number'],eur(i['gross']),eur(i['paid']),eur(i['open'])] for i in invoices],'widths':[2,1,1,1]},
      f'Wir fordern Sie auf, den offenen Gesamtbetrag von {eur(total)} EUR bis zum 26. Oktober 2026 auf unser in den Rechnungen genanntes Konto zu überweisen. Die bisherigen Rückfragen wurden an die Disposition gegeben. Aus den derzeit verfügbaren Abrechnungsdaten ergibt sich für uns keine Abweichung. Nach ergebnislosem Fristablauf werden wir die Forderung gerichtlich geltend machen.',
      'Diese Aufforderung berechnet keine Mahnpauschale und keine vorgerichtlichen Rechtsanwaltskosten. Bitte nennen Sie bei weiterer Korrespondenz die Kundennummer B1047.',
    ],signature='Britta Fleetmann\nGeschäftsführerin')
    mail(f'{G}/10_Letzte_Belegbitte.eml','2026-10-21T13:16:00+02:00','Jette Finkenwerder <jette@backbord.example>','Britta Fleetmann <geschaeftsfuehrung@elbmarsch.example>','Ihre Zahlungsaufforderung vom 19. Oktober',
      'Sehr geehrte Frau Fleetmann,\n\nwir erhalten seit März keine Antwort mit den angeforderten Originalbelegen. Die Monatslisten allein erklären uns weder die Menge noch die täglichen Abholungen. Zusätzliche Aufträge aus unserem Haus liegen mir nicht vor. Bitte stellen Sie die gerichtliche Weitergabe zurück, bis Ihre Disposition das aufgeklärt hat. Unsere Zahlungen sind kein Einverständnis mit diesen Mengen. Eine vollständige Zahlung kann ich nicht freigeben.\n\nJette Finkenwerder')
    word(f'{G}/11_Betriebsangaben_2026-11-06.docx','Betriebsangaben für Rechtsanwältin Lene Sieveking',[
      'Jette Finkenwerder · 6. November 2026 · zusammengestellt nach Rücksprache mit Betriebsleiter Cem Kavel und Buchhalterin Anne Kopp',
      heading('1 Unser Betrieb'),
      'Wir backen in der Billstraße an sechs Tagen pro Woche mit 17 Beschäftigten. Vier Verkaufsstellen und ein kleiner Laden an der Backstube werden beliefert. Seit Januar kamen zwei Firmenkunden mit Frühstückslieferungen hinzu. Im Sommer hatten wir sechs Wochen einen größeren Veranstaltungsauftrag. Ein Teil der Transportverpackungen kommt zurück. Altbrot geht zweimal wöchentlich an Nordfeld Futtermittel; die grünen Bioeimer gehören einem anderen Unternehmen. Die Fotos und Tabellen aus dem Betrieb haben wir aufgehoben.',
      heading('2 So lief die Abrechnung'),
      'Anne hat die ersten beiden Rechnungen bezahlt. Sie hat vor der zweiten Zahlung nachgefragt; als die Antwort kam, ging sie von einer Klärung im Folgemonat aus. Ich habe danach die monatlichen 800 Euro angeordnet, damit uns die Entsorgung nicht abgestellt wird. Die Buchhaltung durfte diese Beträge ausdrücklich nur auf die benannte Rechnung zahlen. Wir haben keinen Vergleich und keinen Ratenplan unterschrieben.',
      heading('3 Wer etwas wissen könnte'),
      'Cem kennt die Anlieferung und die Türen zum Hof. Nils Bahrenburg arbeitet donnerstags im Lager und sieht oft den Müllwagen. Er hat sich keine Kennzeichen aufgeschrieben. Anne hat die Buchungsbelege und die Reklamationsmails. Der Fahrer im Juni hat etwas über ein anderes Handgerät gesagt. Seinen Namen kennen wir nicht. Wir haben keine Kamera am Hof und können deshalb nicht nachträglich jede Leerung filmen oder zählen.',
      heading('4 Noch nicht aufgefundene Unterlagen'),
      'Die Schichtnotizen aus dem Sommer liegen möglicherweise bei Nils zu Hause. Der Entsorger hat trotz mehrfacher Bitte keine einzelnen Wiegebelege übersandt. Das Etikett an unserer Tonne möchte ich heute fotografieren lassen. Ein elektronisches Kundenkonto habe ich nur mit dem Büro-PC geöffnet. Die dortige Ansicht zeigt keine Uhrzeiten und keine Fahrtroute.',
      'Jette Finkenwerder',
    ])
    mail(f'{G}/12_Mandatsanfrage.eml','2026-11-06T08:24:00+01:00','Jette Finkenwerder <jette@backbord.example>','Lene Sieveking <lene@sieveking-wulff.example>','Bitte dringend prüfen: Rechnungen der Elbmarsch',
      'Sehr geehrte Frau Sieveking,\n\nwir haben gestern Gerichtspost bekommen. Die Gerichtssachen schicke ich separat, damit Sie den Umschlag und alle Seiten zusammen haben. Hier kommen unsere Geschäftsunterlagen. Die Entsorgung hat stattgefunden, aber mit diesen Mengen kann etwas nicht stimmen. Wir sind keine kleine Kaffeebude, trotzdem wirkt die Forderung völlig aus der Welt. Bitte klären Sie zuerst, welche Unterlagen und Auskünfte Sie von uns brauchen. Ich möchte wissen, welche Rechnungsteile uns überhaupt betreffen, und rechtzeitig auf die Gerichtspost reagieren.\n\nFreundliche Grüße\nJette Finkenwerder', [f'{G}/11_Betriebsangaben_2026-11-06.docx'])


def claim(invoices):
    total=sum(i['open'] for i in invoices)
    pdf(f'{P}/01_Klage_2026-10-30.pdf','Klage wegen Entsorgungsvergütung',LAW,LA,'Landgericht Hamburg\nZivilkammer\nSievekingplatz 1\n20355 Hamburg\n\nÜber das besondere elektronische Anwaltspostfach','VK 26/1842-FL','2026-10-30',[
      f'Streitwert: {eur(total)} EUR',
      f'Der {WASTE}, Andreas-Meyer-Straße 48, 22113 Hamburg, vertreten durch die Geschäftsführerin Britta Fleetmann, ebenda,\n- Klägerin -\nProzessbevollmächtigte: Vossen & Klink Rechtsanwälte Partnerschaft mbB, Herrengraben 36, 20459 Hamburg,',
      f'gegen\ndie {BAKERY}, Billstraße 137, 20539 Hamburg, vertreten durch die Geschäftsführerin Jette Finkenwerder, ebenda,\n- Beklagte -',
      'Namens und in Vollmacht der Klägerin erheben wir Klage. Eine gütliche Einigung ist bislang nicht zustande gekommen. Die Klägerin hat die Beklagte unter Berücksichtigung ihrer Teilzahlungen zur Zahlung aufgefordert. Die Beklagte hat weiterhin Zweifel an der Leistungsabrechnung geäußert. Einer Güteverhandlung steht die Klägerin offen gegenüber.',
      heading('1 Anträge'),
      heading('1.1 Zahlung'),
      f'Die Beklagte wird verurteilt, an die Klägerin {eur(total)} EUR nebst Zinsen in Höhe von neun Prozentpunkten über dem jeweiligen Basiszinssatz seit dem 27. Oktober 2026 zu zahlen.',
      heading('1.2 Kosten'),
      'Der Beklagten werden die Kosten des Rechtsstreits auferlegt.',
      heading('1.3 Schriftliches Vorverfahren'),
      'Für den Fall, dass das Gericht das schriftliche Vorverfahren anordnet und die Beklagte ihre Verteidigungsbereitschaft nicht rechtzeitig anzeigt, wird der Erlass eines Versäumnisurteils gemäß § 331 Abs. 3 ZPO beantragt.',
      heading('2 Parteien und Vertragsverhältnis'),
      heading('2.1 Geschäftsbetriebe'),
      'Die Klägerin ist ein privates Entsorgungsunternehmen. Sie erhebt keine öffentlich-rechtlichen Gebühren. Die Beklagte betreibt eine Backstube und beliefert mehrere Verkaufsstellen sowie gewerbliche Abnehmer. Zwischen den Parteien wurde am 12. Dezember 2025 ein individueller Entsorgungsvertrag mit Beginn zum 1. Januar 2026 geschlossen. Vertragsgegenstand ist Gewerberestabfall des Betriebs in der Billstraße. Gefährlicher Abfall und getrennt gesammelte Lebensmittelreste gehören nicht zu diesem Auftrag.',
      'Beweis: Vertrag vom 12. Dezember 2025 nebst Preisblatt und Übergabeprotokoll, Anlagen K1 bis K3.',
      heading('2.2 Vereinbarte Vergütung'),
      'Die Beklagte schuldet monatlich 120,00 EUR netto Grundservice, 48,00 EUR netto für jede tatsächlich ausgeführte Leerung und 215,00 EUR netto je Tonne Nettogewicht. Die Umsatzsteuer tritt hinzu. Zusätzliche Leerungen unterliegen denselben Einheitspreisen; sie sind nach dem Vertrag auf Bestellung auszuführen. Die Abrechnung erfolgt monatlich nachträglich. Die Beklagte erhielt die Rechnungen jeweils elektronisch.',
      heading('3 Erbrachte Leistungen und Rechnungen'),
      heading('3.1 Datengrundlage der Klägerin'),
      'Die Klägerin stützt ihre Abrechnung auf die im System EW Abrechnung 4.2 dem Kundenkonto B1047 zugeordneten Ereignisse. Der zugeordnete elektronische Identifikator lautet QR-71A9. Jede im Journal aufgeführte Zeile enthält ein gesondert erfasstes Leerungsereignis und ein Nettogewicht. Eine pauschale Verdoppelung von Regelterminen wurde nicht vorgenommen.',
      'Die Klägerin geht davon aus, dass die erfassten Ereignisse am vertraglichen Leistungsort der Beklagten angefallen sind. Ihre Disponentin hat die Journale bei der Bearbeitung der Kundenreklamation im Abrechnungssystem abgerufen. Ein zusätzlicher manueller Besuch des Leistungsorts erfolgte nach Auskunft des Kundenservice dabei nicht.',
      'Beweis: Rechnungen Januar bis September 2026 mit Leistungsjournalen, Anlagen K4 bis K12; Zeugnis der Disponentin Mara Kroll, zu laden über die Klägerin.',
      heading('3.2 Mehrmengen und Einwendungen'),
      'Die Beklagte hat auf neue Cateringaufträge, Verpackungsrückläufe und schwankende Abholzeiten hingewiesen. Die Klägerin hält es deshalb für plausibel, dass ein deutlich höherer Entsorgungsbedarf als bei ausschließlichem Ladenbetrieb bestand. Die Monatsjournale weisen die tatsächlich abgerechneten Ereignisse aus. Die Klägerin bestreitet, dass sämtliche oberhalb der üblichen acht oder neun Leerungen liegenden Ereignisse allein aus der Anzahl der Regeltermine als nicht erbracht behandelt werden können.',
      'Die Beklagte verlangte im April einzelne Wiegenachweise, Tourzeiten und Zusatzbestellungen. Der Kundenservice leitete die Anfrage weiter. Schriftliche Einzelbestellungen für jede zusätzliche Leerung sind den für die Klage übergebenen Unterlagen nicht beigefügt. Nach Auffassung der Klägerin lässt dies den Nachweis tatsächlich angeforderter und entgegengenommener Entsorgungen durch weitere Beweismittel unberührt. Die Klägerin behält sich ergänzenden Vortrag nach Rücksprache mit der Disposition vor.',
      heading('3.3 Einzelne Forderungen und Zahlungen'),
      {'headers':['Rechnung','Brutto EUR','Gezahlt EUR','Rest EUR'],'rows':[[i['number'],eur(i['gross']),eur(i['paid']),eur(i['open'])] for i in invoices],'widths':[2,1,1,1]},
      f'Die Rechnungen K4 und K5 sind vollständig beglichen und werden nicht erneut eingeklagt. Auf K6 bis K12 sind je 800,00 EUR eingegangen. Die Summe der verbleibenden Rechnungsreste beträgt {eur(total)} EUR. Jede Zahlung wurde entsprechend der im Verwendungszweck genannten Rechnung zugeordnet. Es werden weder eine doppelte Hauptforderung noch Mahnpauschalen oder vorgerichtliche Anwaltskosten verlangt.',
      'Beweis: Kontoaufstellung und Zahlungsliste mit Bankreferenzen vom 15. Oktober 2026, Anlage K13. Die Zahlungseingänge sind zwischen den Parteien nach dem vorprozessualen Schriftverkehr nicht streitig.',
      heading('4 Rechtliche Begründung'),
      heading('4.1 Vertragsanspruch'),
      'Die Parteien haben die Übernahme und ordnungsgemäße Entsorgung konkreter Abfälle gegen ein nach Leerungen und Gewicht bestimmtes Entgelt vereinbart. Die Klägerin verlangt die Vergütung aus diesem Vertrag in Verbindung mit § 631 Abs. 1 BGB. Soweit die Behältergestellung mietvertragliche Bestandteile aufweist, beruht das vereinbarte Grundentgelt zusätzlich auf der vertraglich übernommenen Bereitstellung. Der Schwerpunkt liegt in der wiederholten Erbringung des vereinbarten Entsorgungserfolgs.',
      'Die Klägerin hat darzulegen und erforderlichenfalls zu beweisen, welche vertragsgemäßen Leistungen sie für die Beklagte erbracht hat. Sie beruft sich auf die vorgelegten elektronischen Journale und das genannte Zeugnis. Die Einwendungen der Beklagten betreffen die tatsächliche Leistungsmenge und ihre Zuordnung. Die Klägerin hält die ihr derzeit vorliegenden Daten für zutreffend; sie leitet aus der bloßen Zahlung der ersten beiden Rechnungen kein umfassendes Anerkenntnis aller späteren Rechnungen ab.',
      heading('4.2 Fälligkeit und Verzugszinsen'),
      'Alle eingeklagten Rechnungen betreffen abgeschlossene Abrechnungsmonate. Die Klägerin hat spätestens mit dem Schreiben vom 19. Oktober 2026 Zahlung bis zum 26. Oktober 2026 verlangt. Diese Mahnung ging der Beklagten spätestens am 21. Oktober 2026 zu, wie ihre Antwort desselben Tages belegt. Die Klägerin beansprucht aus Vereinfachungsgründen Zinsen erst ab dem Folgetag des zuletzt gesetzten Zahlungsziels. Beide Parteien handelten unternehmerisch. Grundlage des Zinsantrags sind §§ 286 Abs. 1, 288 Abs. 2 BGB.',
      'Beweis: Zahlungsaufforderung vom 19. Oktober 2026 und E-Mail der Beklagten vom 21. Oktober 2026, Anlagen K14 und K15.',
      heading('4.3 Zuständigkeit'),
      'Der Sitz der Beklagten liegt in Hamburg; damit ist das angerufene Gericht örtlich nach §§ 12, 17 ZPO zuständig. Die sachliche Zuständigkeit folgt aus dem Streitwert und §§ 23 Nr. 1, 71 Abs. 1 GVG. Die Klägerin erhebt die Klage bei einer allgemeinen Zivilkammer.',
      'Ein förmliches Mediationsverfahren wurde vor Klageerhebung nicht durchgeführt. Gegen eine Entscheidung durch den Einzelrichter bestehen keine Bedenken. Auch einer Videoverhandlung nach § 128a ZPO stehen aus Sicht der Klägerin keine Gründe entgegen.',
      heading('5 Anlagen'),
      'K1 Vertrag vom 12.12.2025; K2 Preisblatt; K3 Übergabeprotokoll; K4 bis K12 die neun Rechnungen Januar bis September mit jeweils nachfolgendem Leistungsjournal; K13 Kontoaufstellung vom 15.10.2026; K14 Mahnung vom 19.10.2026; K15 E-Mail der Beklagten vom 21.10.2026. Die Anlagen werden als separate Dateien mit dieser Klage übermittelt.',
    ],color='#294959',signature='Dr. Arvid Klink\nRechtsanwalt\nEinfach signiert; aus dem besonderen elektronischen Anwaltspostfach des Unterzeichners übermittelt.')
    pdf(f'{P}/02_Verfuegung_2026-11-02.pdf','Verfügung im schriftlichen Vorverfahren','Landgericht Hamburg','Sievekingplatz 1 · 20355 Hamburg',BAKERY+'\nz. Hd. der Geschäftsführerin Jette Finkenwerder\n'+BA,'316 O 287/26','2026-11-02',[
      f'In dem Rechtsstreit {WASTE} gegen {BAKERY} wird das schriftliche Vorverfahren angeordnet.',
      heading('1 Verteidigungsanzeige'),
      'Die Beklagte hat binnen einer Notfrist von zwei Wochen nach Zustellung der Klageschrift durch einen Rechtsanwalt schriftlich anzuzeigen, ob sie sich gegen die Klage verteidigen will. Die Frist ist eine Notfrist und kann nicht verlängert werden. Verspäteter Eingang kann zum Erlass eines Versäumnisurteils führen, wenn die gesetzlichen Voraussetzungen vorliegen.',
      heading('2 Klageerwiderung'),
      'Der Beklagten wird aufgegeben, binnen zwei weiterer Wochen nach Ablauf der Frist zur Verteidigungsanzeige auf die Klage zu erwidern. Sie hat ihre Einwendungen, die betreffenden Tatsachen und Beweismittel anzugeben. Eine Verlängerung dieser weiteren Frist bedarf eines rechtzeitig gestellten und begründeten Antrags; sie ist nicht bereits durch die Antragstellung bewilligt.',
      heading('3 Belehrung'),
      'Vor dem Landgericht besteht Anwaltszwang (§ 78 Abs. 1 ZPO). Eine Erklärung der Geschäftsführerin persönlich ersetzt die erforderliche anwaltliche Verteidigungsanzeige nicht. Bei schuldhafter Fristversäumung können Verteidigungsmittel unter den Voraussetzungen der §§ 282, 296 ZPO zurückgewiesen werden. Bleibt die Verteidigungsanzeige aus, kann auf Antrag der Klägerin ohne mündliche Verhandlung ein Versäumnisurteil ergehen (§ 331 Abs. 3 ZPO).',
      'Bei einer Verurteilung durch Versäumnisurteil hat die Beklagte grundsätzlich die Kosten des Rechtsstreits zu tragen (§ 91 ZPO). Das Versäumnisurteil ist ohne Sicherheitsleistung vorläufig vollstreckbar (§ 708 Nr. 2 ZPO); die Klägerin kann daraus die Zwangsvollstreckung betreiben.',
      'Die Klageschrift vom 30. Oktober 2026 und die Anlagen K1 bis K15 werden zugestellt. Die Geschäftsstelle vermerkt den Zustellungstag aus der zurückkommenden Zustellungsurkunde.',
    ],color='#4A5562',signature='Dr. Jonah von Alvensleben\nRichter am Landgericht\nFür die Richtigkeit der Abschrift: Tiede, Justizbeschäftigte')
    path=CASE/f'{P}/03_Zustellungsumschlag_2026-11-05.pdf'
    c=Canvas(str(path),pagesize=A4,invariant=1);c.setTitle('Zustellungsumschlag 316 O 287/26');c.setAuthor('Landgericht Hamburg')
    c.setFillColor(colors.HexColor('#F3DC79'));c.rect(32,280,531,370,fill=1,stroke=0)
    c.setFillColor(colors.black);c.setFont('HamburgB',15);c.drawString(55,618,'Förmliche Zustellung')
    c.setFont('Hamburg',10);c.drawString(55,590,'Absender: Landgericht Hamburg · Sievekingplatz 1 · 20355 Hamburg')
    c.drawString(55,573,'Geschäftsnummer: 316 O 287/26 · Verfügung vom 02.11.2026')
    c.setFillColor(colors.white);c.rect(65,397,337,137,fill=1,stroke=0);c.setFillColor(colors.black)
    c.setFont('Hamburg',14)
    for i,line in enumerate([BAKERY,'Billstraße 137','20539 Hamburg']):c.drawString(83,501-i*25,line)
    c.setFont('Hamburg',10);c.drawString(55,363,'Zugestellt am:');c.setFont('HamburgI',17);c.drawString(133,360,'05.11.2026, 10:18 Uhr')
    c.setFont('HamburgB',13);c.setFillColor(colors.HexColor('#324B67'));c.drawString(325,319,'EINGANG 05. NOV. 2026')
    c.setFont('Hamburg',10);c.drawString(392,302,'Buchhaltung · AK')
    c.setFillColor(colors.black);c.setFont('Hamburg',9);c.drawString(55,250,'Im Mandatseingang am 06.11.2026 erfasst: Umschlagvorderseite mit Zustelldatum und Eingangsstempel.')
    c.showPage();c.save();record(path,'Zustellungsumschlag 316 O 287/26')
    mail(f'{P}/04_Weiterleitung_Gerichtspost.eml','2026-11-06T08:31:00+01:00','Jette Finkenwerder <jette@backbord.example>','Lene Sieveking <lene@sieveking-wulff.example>','Gerichtspost separat / 316 O 287/26',
      'Sehr geehrte Frau Sieveking,\n\nhier die Klage, Verfügung und der Umschlag. Anne hat die Post gestern um kurz nach zehn bekommen. Ich war bis abends auf einer Messe. Bei uns hat noch niemand dem Gericht geantwortet. Ich habe gestern nur mit dem Kundenservice der Elbmarsch telefoniert. Bitte übernehmen Sie die anwaltliche Bearbeitung.\n\nJette Finkenwerder',
      [f'{P}/01_Klage_2026-10-30.pdf',f'{P}/02_Verfuegung_2026-11-02.pdf',f'{P}/03_Zustellungsumschlag_2026-11-05.pdf'])
    pdf(f'{P}/05_K13_Kontoaufstellung.pdf','K13 Kontoaufstellung B1047',WASTE,WA,'Vossen & Klink Rechtsanwälte Partnerschaft mbB\nHerrengraben 36\n20459 Hamburg','K13 / B1047','2026-10-15',[
      'Die nachstehende Aufstellung zeigt die bis zum 15. Oktober 2026 gebuchten Zahlungseingänge auf die Rechnungen Januar bis September. Die Buchung erfolgte jeweils nach der Rechnungsnummer im Verwendungszweck.',
      {'headers':['Rechnung','Datum Zahlung','Brutto EUR','Zahlung EUR','Rest EUR'],'rows':[[i['number'],dd(i['payment_date']),eur(i['gross']),eur(i['paid']),eur(i['open'])] for i in invoices],'widths':[1.9,1.3,1,1,1]},
      f'Gesamtrechnungsbetrag {eur(sum(i["gross"] for i in invoices))} EUR; Zahlungseingänge {eur(sum(i["paid"] for i in invoices))} EUR; offener Buchsaldo {eur(total)} EUR. Weitere Kostenpositionen sind nicht enthalten.',
      'Bankreferenzen der Zahlungseingänge: HB26-0212-1047, HB26-0312-1047, HB26-0412-1047, HB26-0512-1047, HB26-0612-1047, HB26-0712-1047, HB26-0812-1047, HB26-0912-1047 und HB26-1012-1047.',
    ],signature='Anneke Burmester\nDebitorenbuchhaltung Elbmarsch Wertstofflogistik GmbH')
    pdf(f'{P}/06_Anlagenverzeichnis.pdf','Anlagenverzeichnis zur Klage',LAW,LA,'Landgericht Hamburg\nSievekingplatz 1\n20355 Hamburg','VK 26/1842-FL / 316 O 287/26','2026-10-30',[
      'Die Anlagen werden nachfolgend mit der gerichtlichen Bezeichnung und dem Dateinamen des eingereichten Dokuments aufgeführt. Bereits in der Geschäftsablage vorhandene inhaltsgleiche Dateien werden in der Mandatsablage nur einmal aufbewahrt.',
      {'headers':['Anlage','Dokument und Datei'],'rows':[
        ['K1','Entsorgungsvertrag / 01_Entsorgungsvertrag_2025-12-12.pdf'],
        ['K2','Preisblatt / 02_Preisblatt_unterzeichnet.pdf'],
        ['K3','Übergabe / 03_Behaelteruebergabe_2025-12-29.pdf'],
        *[[f'K{i["month"]+3}',i['number']+'.pdf, einschließlich Leistungsjournal'] for i in invoices],
        ['K13','Kontoaufstellung / 05_K13_Kontoaufstellung.pdf'],
        ['K14','Mahnung / 09_Mahnung_2026-10-19.pdf'],
        ['K15','E-Mail vom 21.10.2026 / 10_Letzte_Belegbitte.eml'],
      ],'widths':[.6,4.4]},
      'Die Klageschrift und dieses Verzeichnis enthalten keine geänderten Fassungen der Vertragsunterlagen oder Rechnungen. Die Klägerin hat zu jeder Monatsrechnung das jeweils zugehörige Journal übermittelt.',
    ],color='#294959')


def late_records(rows):
    pdf(f'{N}/01_Bestandskarte_Klinikum_2025-12-29.pdf','Behälterkarte Wirtschaftshof',HOSPITAL,HA,'Technischer Dienst · Haus 4\nLieferhof Nord','KA-AB-2088','2025-12-29',[
      'Die folgende Karte betrifft ausschließlich den nicht gefährlichen Gewerberestabfall aus Verwaltung, Kantine und öffentlichen Bereichen. Medizinische, infektiöse oder spitze Abfälle werden über getrennte verschlossene Systeme mit einem anderen Entsorger abgefahren. Diese Karte enthält keine Patientendaten.',
      {'headers':['Feld','Bestand'],'rows':[['Entsorger','Elbmarsch Wertstofflogistik GmbH'],['Kundenkonto','K2088'],['Seriennummer','EW-1100-0842'],['Etikett','QR-71A9'],['Behälter','1.100 Liter, dunkler Kunststoff, gelber Deckelgriff'],['Leerungsfenster','werktäglich 05:45 bis 07:15 Uhr'],['Aufstellort','Lieferhof Nord, Position N-3'],['Schlüssel','K-42']]},
      'Das Etikett wurde vom Technischen Dienst bei Aufstellung fotografisch dokumentiert. Die eingeprägte Nummer am Scharnier wurde beim Jahreswechsel nochmals kontrolliert. Die Verbindung zum Abrechnungskonto führt die Entsorgerin; das Klinikum kann deren interne Kundendaten nicht ändern.',
    ],signature='Marten Blankenese\nTechnischer Dienst')
    pdf(f'{N}/02_Klinikum_Vertragsgrundlage.pdf','Entsorgungsvertrag Lieferhof Nord',WASTE,WA,HOSPITAL+'\n'+HA,'EW-K2088 / Vertrag 2025-119','2025-12-15',[
      heading('1 Parteien und Abfallstrom'),
      f'{WASTE}, vertreten durch Britta Fleetmann, und {HOSPITAL}, vertreten durch den kaufmännischen Geschäftsführer Dr. Finn Eppendorff, vereinbaren ab dem 1. Januar 2026 die werktägliche Leerung eines 1.100-Liter-Behälters am Lieferhof Nord, Alsterdorfer Straße 463, Hamburg. Erfasst wird ausschließlich der nicht gefährliche Gewerberestabfall aus den Verwaltungs-, Kantinen- und öffentlichen Bereichen. Gefährliche medizinische Abfälle, scharfe oder spitze Gegenstände sowie infektiöser Abfall sind ausgeschlossen.',
      heading('2 Leistung und Kontrolle'),
      'Die Auftragnehmerin stellt einen Behälter und übernimmt die Leerung von Montag bis Freitag zwischen 05:45 und 07:15 Uhr, auch wenn der Tag ein gesetzlicher Feiertag ist. Eine Sonderleerung an Wochenenden ist gesondert zu beauftragen. Der Technische Dienst gewährt Zugang über Tor Nord. Der Behälter und sein QR-Etikett werden bei Übergabe dokumentiert. Die Auftragnehmerin führt die Abfälle ordnungsgemäß einer zugelassenen Anlage zu. Den erfolgten Leistungsvorgang hält sie mit Zeitstempel und Wiegedaten fest.',
      heading('3 Vergütung'),
      'Der monatliche Grundservice kostet 120,00 EUR netto. Für jede tatsächlich ausgeführte Leerung werden 48,00 EUR netto berechnet. Die Behandlung des Abfalls kostet 215,00 EUR netto je Tonne tatsächlichen Nettogewichts. Es erfolgt keine pauschale Gewichtsannahme. Die Umsatzsteuer tritt hinzu. Es bestehen keine weiteren Zuschläge. Die Preise gelten unverändert bis Jahresende. Die Rechnung ist nach Ablauf des Monats mit einem Leistungsjournal vorzulegen und binnen 14 Tagen nach Zugang zu bezahlen.',
      heading('4 Nachweise und Beanstandung'),
      'Die Parteien gleichen monatliche Abweichungen anhand der Originalbelege ab. Eine falsch zugeordnete Kennung wird berichtigt, ohne den unveränderten Originaldatensatz zu löschen. Die Auftragnehmerin legt bei Streit über eine Leerung den betreffenden Tour- und Wiegenachweis vor. Das Klinikum führt keine eigene abrechnungsfähige Fahrzeugwaage. Die Kenntnisnahme einer Rechnung begründet keinen Verzicht auf Einwendungen.',
      heading('5 Laufzeit und Verantwortlichkeit'),
      'Der Vertrag läuft vom 1. Januar bis zum 31. Dezember 2026. Er verlängert sich nicht automatisch. Die Parteien können aus wichtigem Grund nach den gesetzlichen Vorschriften kündigen. Die Auftragnehmerin hält den Behälter instand, haftet nach den gesetzlichen Vorschriften und versichert ihre betrieblichen Risiken. Das Klinikum haftet für schuldhaft falsch eingeworfene ausgeschlossene Abfälle. Weitere Haftungsbeschränkungen werden nicht vereinbart.',
      heading('6 Datenschutz und Abschluss'),
      'Patientenbezogene Informationen dürfen nicht in die Entsorgungsdokumentation aufgenommen werden. Die Parteien verwenden ausschließlich die Kontaktdaten der zuständigen Betriebsmitarbeiter. Änderungen bedürfen der Textform, soweit gesetzlich nichts Strengeres erforderlich ist. Weitere AGB werden nicht einbezogen. Beide Parteien haben eine identische Vertragsausfertigung erhalten.',
      'Hamburg, 15. Dezember 2025\nBritta Fleetmann für Elbmarsch Wertstofflogistik GmbH\nDr. Finn Eppendorff für Klinikum Alsterbogen Hamburg gGmbH',
    ])
    pdf(f'{N}/03_Systemticket_2026-11-12.pdf','Ticket 6841 Zuordnung nach Jahreswechsel','Elbmarsch IT und Disposition',WA,'Britta Fleetmann\nGeschäftsführung Elbmarsch Wertstofflogistik GmbH','EW-SUP-6841','2026-11-12',[
      heading('1 Anlass und Sicherung'),
      'Frau Kroll hat heute die Reklamation B1047 an die IT eskaliert. Bei der Vorprüfung fiel auf, dass die Behälterkennung aus dem Übergabeprotokoll nicht mit der im Abrechnungskonto hinterlegten Kennung übereinstimmt. Die Datenbank wurde um 09:14 Uhr schreibgeschützt exportiert. Vor einer Korrektur wurden die aktive Zuordnungstabelle, das Importjournal vom 2. Januar und der archivierte Bestandsstand vom 31. Dezember gesichert.',
      heading('2 Tatsächliche Einträge'),
      'Das Archiv ordnet QR-71B0 und die Seriennummer EW-1100-0841 dem Kunden B1047 zu. QR-71A9 und EW-1100-0842 gehören dort zu K2088. Die aktive Abrechnungstabelle hat seit dem Import vom 2. Januar 2026 die Kundenwerte vertauscht. In der importierten CSV wurden die Spalten Behälter und Kunde vor dem Sortieren getrennt bearbeitet. Die protokollierte manuelle Änderung erfolgte durch Nutzer DISP-04 um 07:52 Uhr. Daraus lässt sich allein noch nicht feststellen, welche Person welche physische Leerung ausgeführt hat.',
      heading('3 Reichweite und offener Abgleich'),
      'Die Abrechnungsjournale übernehmen den Kundennamen aus der aktiven Tabelle, die Scannerrohdaten dagegen Etikett, eingeprägte Nummer, Zeit und Koordinaten vom Fahrzeug. Die bisher gezogene Stichprobe vom 18. Juni stimmt geografisch mit den beiden Übergabestandorten überein. Vor einer Rechnungskorrektur müssen alle Ereignisse und mögliche Zusatzaufträge geprüft werden. Wir haben bislang keine rückwirkenden Rechnungen, Gutschriften oder Verrechnungen erstellt.',
      'Die Originaldateien des Exports wurden unverändert an die Rechtsabteilung übergeben. Die nachfolgende Übermittlung an die Kanzleien umfasst nur Betriebsdaten der beiden beteiligten Unternehmen. Fahrzeugführer werden mit dienstlichen Kennungen bezeichnet. Personaldaten werden bei Bedarf gesondert und rechtlich geprüft bereitgestellt.',
    ],signature='Lea Tesdorpf\nLeitung IT Anwendungen')
    pdf(f'{N}/04_Fahrerauskunft_2026-11-12.pdf','Schriftliche Auskunft zur Tour H07',WASTE,WA,'Lea Tesdorpf · IT Anwendungen\nAndreas-Meyer-Straße 48\n22113 Hamburg','EW-SUP-6841 / F-29','2026-11-12',[
      'Ich fahre die Billbrook-Tour H07. Die Backstube in der Billstraße habe ich im ersten bis dritten Quartal an den üblichen Tagen angefahren; manchmal verschob sich ein Termin wegen Feiertag oder Fahrzeugausfall. Ich kann aus Erinnerung nicht jede einzelne Fahrt sicher bestätigen. Die Standortdaten auf dem Handgerät wurden automatisch aufgezeichnet. Eine handschriftliche Unterschrift der Kundin brauchten wir bei der regulären Umleerung nicht.',
      'Bei der Backstube ist der Behälter mit dem weißen Farbfleck links. Ich habe das blaue Etikett QR-71B0 gescannt. Den Aufstellort habe ich im Jahr 2026 nicht geändert. Ich fahre nicht die frühe Klinikroute. Ein Behältertausch zwischen den Standorten ist mir nicht bekannt. Ob jemand im Büro die Kundenkennungen geändert hat, kann ich nicht beurteilen.',
      'Im Juni war der Hof einmal mit einem Lieferwagen teilweise verstellt. Ich habe gewartet, bis ich durchfahren konnte, und den Behälter geleert. Eine gesonderte vergebliche Anfahrt habe ich dafür nicht erfasst. Zusätzliche Leerungen außerhalb meines Plans habe ich bei der Backstube nicht telefonisch angenommen. Wenn die Disposition andere Fahrer geschickt hat, weiß ich davon nicht.',
    ],signature='Nils Oevelgönne\nFahrerkennung F-29\nAuskunft gelesen und am 12. November 2026 freigegeben')
    pdf(f'{N}/05_Klinikum_Freigabe_und_Auskunft.pdf','Betriebsdaten zur Entsorgungsabrechnung',HOSPITAL,HA,'Rechtsanwältin Lene Sieveking\nSieveking & Wulff\nNeuer Wall 54\n20354 Hamburg','KA-TD-2026-114','2026-11-13',[
      'Sehr geehrte Frau Sieveking,',
      'mit Einwilligung unserer Geschäftsführung übersenden wir die Behälterkarte, den vollständigen Vertrag, die Rechnungsdaten und die Auszüge aus dem Torbuch für den betroffenen Abfallstrom. Die Unterlagen enthalten keine Patienteninformationen. Bitte verwenden Sie sie nur für die Klärung der betroffenen Entsorgungsabrechnung und die damit zusammenhängende Rechtsverfolgung.',
      'Wir haben uns im Februar intern über die überraschend niedrigen Rechnungen gewundert. Unsere Buchhaltung nahm zunächst an, dass der Entsorger weniger Leerungen berechnet, weil das Gewicht niedrig ist. Die operative Abteilung sah die Rechnungen nicht. Erst Ihre Anfrage hat den Abgleich ausgelöst. Am Standort steht seit Dezember 2025 derselbe Behälter EW-1100-0842 mit QR-71A9. Eine Umstellung auf nur zwei wöchentliche Leerungen wurde nicht beauftragt.',
      'Unsere Abrechnung enthält von Januar bis September überwiegend acht oder neun Leerungen monatlich. Das Torbuch weist für diesen Gewerberestabfall die fast werktägliche Abfahrt aus. Es handelt sich nicht um einen anderen Sonderabfallstrom. Die von uns erhaltenen Rechnungen wurden bezahlt; sie sind bisher weder storniert noch korrigiert worden. Eine Ausgleichszahlung an Ihre Mandantin ist nicht erfolgt.',
    ],signature='Dr. Finn Eppendorff\nKaufmännischer Geschäftsführer')
    pdf(f'{N}/06_Klinikum_Rechnungsjournal.pdf','Rechnungsjournal Kundenkonto K2088',HOSPITAL,HA,'Buchhaltung / Technischer Dienst','Export KA-2026-113','2026-11-13',[
      'Auszug aus den Eingangsrechnungen der Elbmarsch Wertstofflogistik GmbH. Der Auszug betrifft nur den Vertrag für den Gewerberestabfallbehälter im Lieferhof Nord. Alle ausgewiesenen Rechnungen sind als bezahlt gebucht. Belege liegen im Rechnungsarchiv unter der angegebenen Nummer.',
      {'headers':['Monat','Rechnung','QR','Leerungen','kg','Brutto EUR'],'rows':[[MONTHS[m-1],f'EW-26-{m:02}-2088','QR-71B0',str(B_COUNTS[m-1]),str(B_COUNTS[m-1]*130),eur(int((Decimal(12000+B_COUNTS[m-1]*4800)+Decimal(B_COUNTS[m-1]*130)*Decimal('21.5'))*Decimal('1.19')+Decimal('.5')))] for m in range(1,10)],'widths':[1.2,1.9,1.1,.9,.8,1.1]},
      'Der Auszug gibt den gebuchten Rechnungsstand wieder. Die Spalten sind keine Bestätigung, dass die aufgeführten Mengen am Klinikstandort angefallen sind.',
    ])
    # Raw export deliberately keeps the billed customer and the physical event apart.
    headers=['event_id','datum','uhrzeit','tour','seriennummer','qr','abrechnung_kunde','standortcode','netto_kg','breite','laenge','fahrer']
    csv_out(f'{N}/07_Fahrzeugereignisse_2026-01_bis_09.csv',headers,[[r[k] for k in ['id','date','time','tour','serial','qr','billed_customer','physical_site','kg','lat','lon','driver']] for r in rows])
    csv_out(f'{N}/08_Zuordnungshistorie.csv',['zeitpunkt','aktion','qr','seriennummer','kunde_alt','kunde_neu','nutzer','quelle'],[
      ['2025-12-29T09:24:00+01:00','Aufstellung','QR-71B0','EW-1100-0841','','B1047','DISP-02','Uebergabe 1047-01'],
      ['2025-12-29T11:16:00+01:00','Aufstellung','QR-71A9','EW-1100-0842','','K2088','DISP-02','KA-AB-2088'],
      ['2026-01-02T07:52:14+01:00','Import','QR-71B0','EW-1100-0841','B1047','K2088','DISP-04','MIG-2026-001.csv Zeile 147'],
      ['2026-01-02T07:52:14+01:00','Import','QR-71A9','EW-1100-0842','K2088','B1047','DISP-04','MIG-2026-001.csv Zeile 148'],
      ['2026-11-12T09:14:00+01:00','Sicherung','beide','beide','unverändert','unverändert','IT-08','EW-SUP-6841'],
    ])
    csv_out(f'{N}/09_Torjournal_Klinikum.csv',['datum','uhrzeit','tor','fahrzeug','auftrag','seriennummer','bemerkung'],[[r['date'],r['time'],'Nord','HH-EW 431','Gewerberestabfall N-3',r['serial'],'Abfahrt nach Leerung'] for r in rows if r['physical_site']=='KA-LH'])
    mail(f'{N}/10_IT_Antwort_mit_Rohdaten.eml','2026-11-12T14:09:00+01:00','Lea Tesdorpf <it@elbmarsch.example>','Lene Sieveking <lene@sieveking-wulff.example>','EW-SUP-6841 / Datenexport und Zuordnung',
      'Sehr geehrte Frau Sieveking,\n\nim Auftrag unserer Geschäftsführung erhalten Sie den gesicherten Export. Die Übergabeprotokolle passen nicht zu den seit 2. Januar aktiven Kundenkennungen. Wir prüfen deshalb auch die Rechnungen des zweiten betroffenen Kunden. Bitte beachten Sie: Der Export ist der damalige gespeicherte Stand, keine rückwirkend bereinigte Abrechnung. Die Spalte abrechnung_kunde darf nicht allein als Nachweis des physischen Leistungsortes verstanden werden. Die Originale bleiben gesichert. Herr Klink erhält dieselben Daten.\n\nMit freundlichen Grüßen\nLea Tesdorpf',
      [f'{N}/03_Systemticket_2026-11-12.pdf',f'{N}/07_Fahrzeugereignisse_2026-01_bis_09.csv',f'{N}/08_Zuordnungshistorie.csv'])
    mail(f'{N}/11_Mandantin_nach_Foto.eml','2026-11-12T16:51:00+01:00','Jette Finkenwerder <jette@backbord.example>','Lene Sieveking <lene@sieveking-wulff.example>','Das Schild an unserer Tonne / Nachtrag',
      'Liebe Frau Sieveking,\n\nCem hat nachgesehen: Auf der Tonne steht QR-71B0, eingeprägt ist EW-1100-0841. Ich hatte Ihnen beim Telefonat am Freitag QR-71A9 genannt, weil ich die Nummer von der Rechnung vorgelesen habe. Die hatte ich nicht an der Tonne kontrolliert. Das war also keine eigene Beobachtung. Der Behälter ist nach Cems Erinnerung seit Dezember nicht ausgetauscht worden.\n\nBitte berücksichtigen Sie das bei Ihrer Bearbeitung. Wir wissen immer noch nicht, ob in jedem Monat wirklich genau acht oder neun Leerungen bei uns waren. Bitte klären Sie auch, was mit den zwei voll bezahlten Rechnungen und den Abschlägen passiert. Wir haben keine Gutschrift erhalten.\n\nJette')
    mail(f'{N}/12_Klinikum_Unterlagen.eml','2026-11-13T09:22:00+01:00','Marten Blankenese <technik@alsterbogen-klinikum.example>','Lene Sieveking <lene@sieveking-wulff.example>','Freigegebene Betriebsunterlagen / Gewerberestabfall',
      'Sehr geehrte Frau Sieveking,\n\ndie Geschäftsführung hat die Weitergabe ausdrücklich freigegeben. Beigefügt erhalten Sie unsere Karte, den Vertrag, die Freigabe, die gebuchten Rechnungsdaten und das Torjournal. Bitte verwechseln Sie den Gewerberestabfall am Lieferhof Nord nicht mit den medizinischen Abfallströmen; diese laufen völlig getrennt. Das Journal wurde aus dem Schrankenprotokoll und den Einträgen des Pförtners exportiert.\n\nMarten Blankenese',
      [f'{N}/01_Bestandskarte_Klinikum_2025-12-29.pdf',f'{N}/02_Klinikum_Vertragsgrundlage.pdf',f'{N}/05_Klinikum_Freigabe_und_Auskunft.pdf',f'{N}/06_Klinikum_Rechnungsjournal.pdf',f'{N}/09_Torjournal_Klinikum.csv'])
    mail(f'{N}/13_Klaegerkollege_2026-11-13.eml','2026-11-13T12:07:00+01:00','Dr. Arvid Klink <arvid.klink@vossen-klink.example>','Lene Sieveking <lene@sieveking-wulff.example>','Elbmarsch / Backbord, 316 O 287/26',
      'Sehr geehrte Frau Kollegin,\n\nmeine Mandantin hat uns gestern den IT-Befund zugeleitet. Wir prüfen seine Auswirkungen auf den Klagebetrag. Die Zuordnungsfrage muss nun anhand sämtlicher Ereignisse aufgeklärt werden; eine abschließende Abrechnung liegt noch nicht vor. Bitte übersenden Sie Ihre Zahlungsbelege und Ihre Auffassung zu den einzelnen Leistungsmonaten. Die Klage ist bislang nicht zurückgenommen oder reduziert. Einen Verzicht auf Fristen haben wir nicht erklärt und könnten gerichtliche Fristen auch nicht einseitig ändern.\n\nMit kollegialen Grüßen\nDr. Arvid Klink')


def operational_documents():
    pdf(f'{G}/13_Betriebsablauf_und_Hofplan.pdf','Hof und Abfallwege der Backstube',BAKERY,BA,'Cem Kavel · Betriebsleitung','BB-Betrieb-2026-02','2026-02-02',[
      heading('1 Warenweg'),
      'Die Warenannahme liegt hinter dem Rolltor. Mehlsäcke und trockene Verpackungen werden im Lager getrennt. Rückläufe aus den Verkaufsstellen kommen mit den Lieferfahrzeugen gegen 13 Uhr zurück. Saubere Pappe wird im Presscontainer der Nordkarton gesammelt. Altbrot wird in den grünen Eimern in der Kühlkammer bereitgestellt. Der schwarze 1.100-Liter-Behälter links an der Rampe dient ausschließlich dem verbleibenden Gewerberestabfall.',
      heading('2 Zugang zur Entsorgung'),
      'Das Tor wird an Werktagen um 07:30 Uhr geöffnet. Vorher stehen die Auslieferungsfahrzeuge in der Zufahrt; eine reguläre Müllabholung ist dann nicht möglich. Montag und Donnerstag müssen die zwei Stellplätze vor dem schwarzen Behälter bis 10:30 Uhr frei bleiben. Der Entsorger darf keinen Behälter vom Nachbarbetrieb mitnehmen. Nils oder Cem sehen bei der Leerung nach, soweit sie sich im Hof aufhalten.',
      heading('3 Abfallmengen und Sondertermine'),
      'Die Zahl der hergestellten Brote allein ist kein Gewichtsnachweis für Gewerberestabfall. Saisonware, Rückläufe und Verpackungen unterscheiden sich. Sonderleerungen bestellt nur die Geschäftsführung, Cem oder die Buchhaltung. Wer eine zusätzliche Abholung für erforderlich hält, meldet den vollen Behälter mit Datum im Schichtbuch. Eigene Zettel am Behälter gelten nicht als Bestellung.',
    ],color='#8D573C',signature='Cem Kavel\nBetriebsleiter')
    word(f'{G}/14_Schichtnotizen_Juni.docx','Schichtnotizen Hof und Entsorgung Juni 2026',[
      'Nils Bahrenburg · Lager · Ablage am schwarzen Brett',
      heading('1 Donnerstag 4 Juni'),
      '08:25 Uhr: Müllwagen da. Schwarze Tonne geleert, Fahrer alleine. Grüne Eimer hat Nordfeld erst nachmittags mitgenommen. Cem war bei der Außenstelle. Keine Unterschrift.',
      heading('2 Donnerstag 11 Juni'),
      'Tonne abends vorher voll, aber Deckel zu. Morgens wurde normal abgeholt. Keine zweite Abholung gesehen. Die Verpackung vom Stadtteilfest war überwiegend Pappe und ging in den Presscontainer.',
      heading('3 Donnerstag 18 Juni'),
      'Lieferwagen stand quer, Fahrer wartete kurz. Cem sprach mit ihm über das Handgerät. Gegen 08:35 war die Tonne leer und stand wieder am weißen Strich. Am Schild nichts geändert.',
      heading('4 Donnerstag 25 Juni'),
      'Keine eigene Beobachtung: War von 07:00 bis 11:00 Uhr im Außenlager. Cem sagte später, Tonne sei leer gewesen. Montagseinträge fehlen im Buch, weil ich dann nicht im Hofdienst bin.',
    ])


def screenshots():
    fontdir=Path('/System/Library/Fonts/Supplemental')
    regular=lambda size:ImageFont.truetype(str(fontdir/'Arial.ttf'),size)
    bold=lambda size:ImageFont.truetype(str(fontdir/'Arial Bold.ttf'),size)
    for name,heading_text,lines in [
      (f'{G}/15_Kundenportal_2026-11-06.png','EW Kundenportal | B1047',[
        'BACKBORD BACKSTUBE GMBH','Billstraße 137, 20539 Hamburg','Behälter: QR-71A9','Letzte Rechnung: EW-26-09-1047','Status: an Rechtsabteilung übergeben','Leistungsjournal: Monatsliste verfügbar','Tourdetails: Für Ihren Zugang nicht freigeschaltet','Abruf: 06.11.2026, 09:03 Uhr · Benutzer AKOPP']),
      (f'{N}/14_Disposition_Sicherung_2026-11-12.png','EW Disposition | Historischer Datenstand',[
        'Sicherung 12.11.2026 09:14 | Ticket EW-SUP-6841','QR-71A9 | EW-1100-0842 | Kunde B1047','QR-71B0 | EW-1100-0841 | Kunde K2088','Letzter Import: MIG-2026-001.csv','Importzeit: 02.01.2026 07:52:14','Standortquelle: Kundenstamm, nicht Fahrzeug-GPS','Status: Originalstand gesichert; Korrektur ausstehend','Exportansicht · keine nachträgliche Neuzuordnung']),
    ]:
        im=Image.new('RGB',(1500,1000),'#edf1f3');draw=ImageDraw.Draw(im)
        draw.rectangle((0,0,1500,90),fill='#1f3b4c');draw.text((50,25),heading_text,font=bold(30),fill='white')
        draw.text((60,120),'KUNDEN  /  BEHÄLTER  /  DOKUMENTE',font=regular(21),fill='#536873')
        draw.rounded_rectangle((50,175,1450,900),radius=14,fill='white')
        for index,line in enumerate(lines):draw.text((85,215+index*77),line,font=bold(25) if index==0 else regular(25),fill='#172b35')
        draw.text((60,946),'Bildschirmabzug der in der Akte dokumentierten Fachanwendung',font=regular(18),fill='#596f78')
        path=CASE/name;im.save(path);record(path,heading_text)


def metadata(qa,invoices,rows):
    qa.mkdir(parents=True,exist_ok=True)
    data={'slug':SLUG,'invoices':invoices,'events':rows,'documents':CREATED,'workbooks':[
      {'path':f'{G}/16_Produktion_und_Ruecklaeufe.xlsx','sheet':'Betriebszahlen','title':'Backbord Backstube · Betriebszahlen Januar bis September 2026','note':'Betriebsbuch; Stückzahlen sind keine gewogenen Restabfallmengen. Angaben Anne Kopp, 6. November 2026.','headers':['Monat','Brote und Brötchen Stück','Catering Aufträge','Altbrot Abgabe kg','Pappe Abgabe kg','Quelle'], 'rows':[[f'2026-{m:02}',[48120,45880,51020,49800,52210,60300,58820,55010,53400][m-1],[12,14,15,13,17,24,25,18,16][m-1],[820,790,860,840,890,1020,980,940,910][m-1],[210,205,230,220,245,310,298,270,260][m-1],f'Produktionsbuch {m:02}/2026'] for m in range(1,10)]},
      {'path':f'{N}/15_Ereignisexport_Disposition.xlsx','sheet':'Ereignisse','title':'Elbmarsch · Fahrzeugereignisse Januar bis September 2026','note':'Unveränderter Export vom 12.11.2026, 09:14. Kundenkonto ist ein Abrechnungsfeld; Standortcode stammt aus der Fahrzeugerfassung.','headers':['Ereignis','Datum','Tour','Behälter','QR','Kundenkonto','Standort','Netto kg'], 'rows':[[r['id'],r['date'],r['tour'],r['serial'],r['qr'],r['billed_customer'],r['physical_site'],r['kg']] for r in rows]},
    ]}
    (qa/'source.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return data


def readme():
    lines=[f'# Backbord Backstube und die Entsorgungsrechnungen aus Hamburg','',
      'Eine Hamburger Backstube erhält eine Zahlungsklage wegen gewerblicher Entsorgung. Die Rechnungen passen aus ihrer Sicht nicht zum Betrieb; der Entsorger beruft sich auf seine elektronischen Leistungsdaten. Verträge, Buchungsbelege, betriebliche Notizen und technische Daten müssen anhand ihres jeweiligen Entstehungszeitpunkts geprüft werden. Zugeordnetes Plugin: `forderungsmanagement-klagewerkstatt`.','',
      'Alle Unternehmen, Personen, Vorgänge und betrieblichen Daten sind erfunden. Kontaktadressen verwenden reservierte `.example`-Domains. <!-- reserved-example-contacts -->','',
      '## 1 Bearbeitungsstände','',
      '`Grundakte` enthält nur die bis zum 6. November 2026 zusammengestellten Geschäftsunterlagen, Rechnungen, Zahlungen und ersten Rückfragen. Sie enthält keine Klage, gerichtliche Entscheidung oder Lösung. Die gesonderte Gerichtseingangsmappe enthält die zugestellte Klage, die Verfügung und den Umschlag. Die E-Mail der Mandantin nennt den tatsächlichen Empfang.','',
      '`02_Nachlieferung_2026-11-12_und_13` wird erst im zweiten Durchgang geöffnet. Sie enthält später eingegangene Betriebsunterlagen und Originalexporte. Frühere Aussagen müssen danach mit den weiteren Belegen abgeglichen werden. Es gibt keine vorformulierte Klageerwiderung, keine rechtliche Musterlösung und keine fertige korrigierte Forderungsabrechnung.','',
      '<!-- BEGIN gesamt-pdf-section (autogen) -->',
      '<!-- END gesamt-pdf-section (autogen) -->','',
      '## 3 Aktenbestand','',
      '| Datei | Inhalt |','|---|---|',
    ]
    for doc in CREATED:
        title=doc['title'].replace('|',r'\|')
        lines.append(f'| [{doc["path"]}]({doc["path"]}) | {title} |')
    for name,title in [(f'{G}/16_Produktion_und_Ruecklaeufe.xlsx','Betriebliche Stückzahlen und Abgaben'),(f'{N}/15_Ereignisexport_Disposition.xlsx','Native Tabelle der gesicherten Fahrzeugereignisse')]:lines.append(f'| [{name}]({name}) | {title} |')
    lines += ['', '## 4 Reproduzierbarkeit','',
      'Die Originale werden mit `scripts/build-hamburg-baeckerei-akte.py --qa-dir <temporäres Verzeichnis>` erzeugt. Der Tabellenbuilder verwendet dieselben Ereignisdaten; die Qualitätsprüfung gleicht Rechnungsbeträge, Teilzahlungen, Ereignisse, Zeitstände und E-Mail-Anhänge ab. Rechtsquellen und Prüfergebnisse stehen außerhalb der Arbeitsakte im Repository.','']
    path=CASE/'README.md'
    path.write_text('\n'.join(lines))
    finalize_readme(path)


def finalize_readme(path):
    """Nur diese README normalisieren; keine Originale oder andere Akten anfassen."""
    spec=importlib.util.spec_from_file_location('hamburg_downloads',ROOT/'scripts/inject-gesamt-pdf-section.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.inject(path,SLUG)
    path.write_text(ensure_download_notices(path.read_text(),case_readme=True))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--qa-dir',type=Path,required=True);parser.add_argument('--skip-xlsx',action='store_true');args=parser.parse_args()
    register_fonts();CASE.mkdir(parents=True,exist_ok=True)
    rows=events();invoices=billing(rows)
    contracts();invoices_and_bank(invoices,rows);correspondence(invoices);claim(invoices);late_records(rows);operational_documents();screenshots()
    metadata(args.qa_dir,invoices,rows)
    if not args.skip_xlsx:
        node=os.environ.get('AKTEN_NODE',str(Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node'))
        subprocess.run([node,str(ROOT/'scripts/build-hamburg-baeckerei-tabellen.mjs'),str(args.qa_dir)],check=True)
    readme()
    manifest={str(p.relative_to(CASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in CASE.rglob('*') if p.is_file() and p.suffix!='.md' and 'gesamt-pdf' not in p.parts}
    (args.qa_dir/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'originals':len(manifest),'events':len(rows),'invoice_total_cents':sum(i['gross'] for i in invoices),'paid_cents':sum(i['paid'] for i in invoices),'claim_cents':sum(i['open'] for i in invoices),'pdf_pages':sum(len(PdfReader(p).pages) for p in CASE.rglob('*.pdf') if 'gesamt-pdf' not in p.parts)},ensure_ascii=False))


if __name__=='__main__':main()
