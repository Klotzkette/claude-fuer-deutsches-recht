#!/usr/bin/env python3
"""Erzeugt die fiktiven Originalbelege; XLSX und zentrale Exporte separat."""
from __future__ import annotations
import argparse, calendar, collections, datetime as dt, hashlib, json, mimetypes, subprocess, sys, tempfile
from zoneinfo import ZoneInfo
from pathlib import Path
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'testakten/betreuung-adelheid-pfister-dreijahresabrechnung'
DATA = ROOT / 'scripts/data/betreuung-pfister.json'
WARN = 'Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.\n\nThis test case file was generated with AI and is an experiment. Use at your own responsibility and risk.'

def money(n):
    return f'{n / 100:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') + ' EUR'

def business(y,m,d):
    v=dt.date(y,m,d)
    while v.weekday()>4: v += dt.timedelta(days=1)
    return v.isoformat()

def canonical():
    contacts = [
      dict(id='adelheid',name='Adelheid Pfister',address='Fliederbogen 17, 13125 Berlin',email='adelheid.pfister@postfach.example',role='Betreute Person; geboren 14.02.1948'),
      dict(id='maja',name='Dr. Maja Winterfeld',address='Betreuungsbüro Winterfeld, Bücherplatz 8, 13187 Berlin',email='maja.winterfeld@betreuungsbuero.example',role='Berufliche Betreuerin seit 01.10.2026'),
      dict(id='ruprecht',name='Ruprecht Pfister',address='Kastanienwinkel 6, 16321 Bernau',email='ruprecht.pfister@postfach.example',role='Sohn'),
      dict(id='juna',name='Juna Özdemir-Pfister',address='Birkengasse 24, 10439 Berlin',email='juna.oezdemir@postfach.example',role='Nichte'),
      dict(id='egon',name='Egon Knusper',address='Helferdienst Knusper, Laternenweg 3, 13125 Berlin',email='egon@knusper-hilfe.example',role='Nachbar; Einkaufs- und Technikhilfe'),
      dict(id='bank',name='Fensterbank Spree eG',address='Kontenservice, Uferbogen 12, 10179 Berlin',email='kontenservice@fensterbank-spree.example',role='Girokonto und Sparkonto'),
      dict(id='pflege',name='Alltagshilfe Mohnblüte GmbH',address='Lerchenhof 9, 13125 Berlin',email='rechnung@mohnbluete.example',role='Haushaltsunterstützung'),
      dict(id='haus',name='Hausverwaltung Lindenblatt KG',address='Mauerseglerweg 7, 13189 Berlin',email='verwaltung@lindenblatt.example',role='Vermietervertretung'),
      dict(id='strom',name='Nordlicht Energie Berlin GmbH',address='Stromgasse 14, 10589 Berlin',email='service@nordlicht-energie.example',role='Stromlieferant'),
      dict(id='telefon',name='Sprechfink Telekom GmbH',address='Antennenring 31, 10707 Berlin',email='service@sprechfink.example',role='Telefon und Internet'),
      dict(id='stream',name='SofaKino Digital GmbH',address='Filmpark 18, 10997 Berlin',email='service@sofakino.example',role='Streamingdienst'),
      dict(id='abo',name='LebensKompass Direkt GmbH',address='Wissenshof 4, 04317 Leipzig',email='kundenservice@lebenskompass.example',role='Digitaler Ratgeberdienst'),
      dict(id='lotto',name='Glücksfenster Service GmbH',address='Losweg 11, 99084 Erfurt',email='service@gluecksfenster.example',role='Teilnahmeservice'),
      dict(id='fenster',name='Holz und Licht Wendel GmbH',address='Tischlerhof 2, 16321 Bernau',email='buero@wendel-fenster.example',role='Fensterreparaturbetrieb'),
      dict(id='sanitaet',name='Sanitätshaus Schwalbe GmbH',address='Weidenplatz 16, 13125 Berlin',email='rechnung@schwalbe-sanitaet.example',role='Hilfsmittel'),
      dict(id='apotheke',name='Apotheke Silberblatt',address='Fliederbogen 2, 13125 Berlin',email='team@silberblatt-apotheke.example',role='Apotheke'),
    ]
    tx=[]
    def add(date,account,amount,party,purpose,receipt=None,transfer=None):
        t=dict(id=f'B{len(tx)+1:04d}',date=date,account_id=account,account=account,amount_cents=amount,party=party,counterparty=party,purpose=purpose,source_file=f'02_Konten/{account}_{date[:7]}.pdf',receipt_ids=[receipt] if receipt else [])
        if transfer: t.update(transfer_group=transfer,transfer_id=transfer)
        tx.append(t);return t['id']
    invoices=[]
    def invoice(id,date,seller,total,subject,lines,transaction_id=None,note=''):
        inv=dict(id=id,date=date,seller=seller,total_cents=total,subject=subject,lines=lines,transaction_ids=[transaction_id] if transaction_id else [],note=note,source_file=f'03_Belege/{id}.pdf')
        invoices.append(inv);return inv
    for i in range(36):
        y,m=2023+(9+i)//12,(9+i)%12+1
        ym=f'{y}-{m:02}'
        pension=190000+6000*(int((y,m)>=(2024,7))+int((y,m)>=(2025,7))+int((y,m)>=(2026,7)))
        add(business(y,m,28),'GIRO',pension,'Rentenstelle Nord','Altersrente '+ym)
        add(business(y,m,28),'GIRO',48500,'Rentenstelle Nord','Hinterbliebenenrente '+ym)
        add(business(y,m,3),'GIRO',-78000 if i<15 else -82000,'Hausverwaltung Lindenblatt KG','Warmmiete Fliederbogen 17 / '+ym)
        add(business(y,m,6),'GIRO',-7200 if i<15 else -7900,'Nordlicht Energie Berlin GmbH','Abschlag Kundennummer NE-48017 / '+ym)
        tel=3999 if i<19 else 4499
        tid=add(business(y,m,8),'GIRO',-tel,'Sprechfink Telekom GmbH','Festnetz und Internet SP-118044 / '+ym,'TEL-'+ym if i>=24 else None)
        if i>=24: invoice('TEL-'+ym,ym+'-02','telefon',tel,'Telefon und Internet '+ym,[('Anschluss und Festnetzflat',2499),('Internetpaket',2000)],tid,'Abrechnung einschließlich Umsatzsteuer. Die abgerechneten Leistungsbestandteile betragen zusammen 44,99 EUR. Die Tarifänderung wurde zum 01.05.2025 eingetragen.')
        rid='MH-'+ym
        tid=add(business(y,m,12),'GIRO',-12650,'Alltagshilfe Mohnblüte GmbH','Haushaltshilfe Rechnung '+rid,rid)
        invoice(rid,ym+'-05','pflege',12650,'Haushaltsunterstützung '+ym,[('Wohnung reinigen und Wäsche versorgen, 3 Stunden',6900),('Einkäufe begleiten, 2,5 Stunden',5750)],tid,'Die Leistungen wurden an den im Leistungszettel vermerkten Besuchstagen erbracht. Rechnung an Frau Pfister; keine Kostenerstattung der Pflegekasse auf dieser Rechnung. Der vereinbarte Gesamtpreis beträgt 23,00 EUR je Stunde.')
        add(business(y,m,14),'GIRO',-(21500+(i*137)%6600),'Frischemarkt Karow','Kartenzahlung Lebensmittel, Belegserie FK '+ym)
        drug=2450+(i*113)%1800
        rid='AP-'+ym if i%3==0 else None
        tid=add(business(y,m,15),'GIRO',-drug,'Apotheke Silberblatt','Zuzahlung und Pflegebedarf '+ym,rid)
        if rid: invoice(rid,ym+'-15','apotheke',drug,'Quittung Zuzahlung und Pflegebedarf',[('Zuzahlungsbelege eingelöst',1000),('Pflegebedarf und Verbrauchsartikel',drug-1000)],tid,'Betrag am Schalter per Girokarte bezahlt. Aus Gründen der Diskretion nennt diese Kundenquittung keine Arzneimittel oder Diagnosen. Die Einzelabgabe ist unter der Belegnummer im Haus dokumentiert.')
        add(business(y,m,18),'GIRO',-20000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03')
        add(business(y,m,20),'GIRO',-4850,'Tierladen Pfötchen','Futter und Streu für Kater Mürbchen')
        add(business(y,m,22),'GIRO',-1299,'SofaKino Digital GmbH','Monatsabo SK-77380 / '+ym)
        add(business(y,m,26),'GIRO',-690,'Fensterbank Spree eG','Kontoführung '+ym)
        if i>=6: add(business(y,m,9),'GIRO',-2990,'Glücksfenster Service GmbH','Teilnahmeservice GF-90335 / '+ym)
        if i>=15: add(business(y,m,11),'GIRO',-6990,'LebensKompass Direkt GmbH','Digitalpaket LK-55771 / '+ym)
        if i>=11:
            rid='EK-'+ym if i>=18 else None
            tid=add(business(y,m,24),'GIRO',-14500,'Egon Knusper','Pauschale Einkauf und Technik '+ym,rid)
            if rid: invoice(rid,ym+'-23','egon',14500,'Nachbarschaftsdienste '+ym,[('Einkaufsfahrten nach Absprache',8500),('Telefon, Gerät und Schriftverkehr',6000)],tid,'In der Pauschale sind vereinbarte Fahrten und die laufende technische Hilfe enthalten. Barauslagen für Einkäufe gehören nicht dazu. Termine wurden im Küchenkalender vermerkt; eine Stundenaufstellung wurde nicht vereinbart. Kein Umsatzsteuerausweis.')
        if m in (3,6,9,12):
            add(business(y,m,19),'GIRO',-1500,'Kirchengemeinde Am Fliederbogen','Gemeindespende')
            tr='U-'+ym
            add(business(y,m,21),'GIRO',-25000,'Adelheid Pfister Sparen','Umbuchung auf eigenes Sparkonto',transfer=tr)
            add(business(y,m,21),'SPAR',25000,'Adelheid Pfister Giro','Umbuchung vom eigenen Girokonto',transfer=tr)
        if m==12: add(f'{y}-12-31','SPAR',9000+(y-2023)*1250,'Fensterbank Spree eG','Habenzinsen Jahresabschluss')
    specials=[
      ('2023-11-09',-7800,'Sanitätshaus Schwalbe GmbH','Eigenanteil Gehstock SS-23119','SS-23119'),
      ('2024-02-13',-45000,'Juna Özdemir-Pfister','Zum Abschluss, Tante Adelheid',None),
      ('2024-03-12',8400,'Nordlicht Energie Berlin GmbH','Guthaben Jahresabrechnung 2023 NE-2023','NE-2023'),
      ('2024-05-16',-420000,'Ruprecht Pfister','Fenster / Rechnung W-24051 vorgestreckt','W-24051'),
      ('2024-06-07',60000,'Ruprecht Pfister','Rest Fenster zurück',None),
      ('2024-06-18',-55000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03',None),
      ('2024-07-10',-18900,'Sanitätshaus Schwalbe GmbH','Eigenanteil Duschsitz SS-24102','SS-24102'),
      ('2024-10-04',-120000,'Ruprecht Pfister','Darlehen Reparatur Transporter',None),
      ('2024-12-12',-32000,'Hausverwaltung Lindenblatt KG','Betriebskostennachzahlung 2023 HV-23','HV-23'),
      ('2025-01-16',-55000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03',None),
      ('2025-03-11',3200,'Nordlicht Energie Berlin GmbH','Guthaben Jahresabrechnung 2024 NE-2024','NE-2024'),
      ('2025-04-15',-45000,'Juna Özdemir-Pfister','Zahnbehandlung vorgestreckt',None),
      ('2025-04-29',45000,'Juna Özdemir-Pfister','Zahnbehandlung erstattet',None),
      ('2025-05-08',-79900,'Technikladen Zinnober GmbH','Tablet ZT-250508','ZT-250508'),
      ('2025-06-17',-55000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03',None),
      ('2025-08-07',-27500,'Egon Knusper','Drucker und Einrichtung, Barvorschuss',None),
      ('2025-09-16',-220000,'Egon Knusper','Dankeschön Unterstützung',None),
      ('2025-10-14',-45000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03',None),
      ('2025-11-06',-6990,'LebensKompass Direkt GmbH','Digitalpaket LK-55771 / Nachbelastung 2025-10',None),
      ('2025-11-21',6990,'LebensKompass Direkt GmbH','Storno doppelte Abbuchung Oktober',None),
      ('2025-12-11',-41000,'Hausverwaltung Lindenblatt KG','Betriebskostennachzahlung 2024 HV-24','HV-24'),
      ('2026-01-13',30000,'Ruprecht Pfister','Teilzahlung Transporter',None),
      ('2026-02-10',-55000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03',None),
      ('2026-03-12',-9300,'Nordlicht Energie Berlin GmbH','Nachzahlung Jahresabrechnung 2025 NE-2025','NE-2025'),
      ('2026-04-09',-35000,'Egon Knusper','Ersatz Handy und Datenumzug',None),
      ('2026-05-14',-120000,'Ruprecht Pfister','nochmal überbrücken, wie besprochen',None),
      ('2026-06-16',-65000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03',None),
      ('2026-07-09',-68000,'Sanitätshaus Schwalbe GmbH','Eigenanteil Rollator SS-26180','SS-26180'),
      ('2026-08-11',-98000,'Egon Knusper','Jahrespaket Hilfe voraus',None),
      ('2026-09-10',-65000,'Geldautomat Karow','Bargeldauszahlung Karte 0441, Terminal KA-03',None),
      ('2026-09-18',-8900,'Glücksfenster Service GmbH','Gebühr Sonderziehung GF-90335',None),
    ]
    special_ids={}
    for d,a,p,u,r in specials: special_ids[u]=add(d,'GIRO',a,p,u,r)
    for d,val in [('2024-05-15',350000),('2025-09-15',250000),('2026-05-13',150000)]:
        tr='U-'+d
        add(d,'SPAR',-val,'Adelheid Pfister Giro','Umbuchung auf eigenes Girokonto',transfer=tr)
        add(d,'GIRO',val,'Adelheid Pfister Sparen','Umbuchung vom eigenen Sparkonto',transfer=tr)
    extra_invoices=[
      ('SS-23119','2023-11-09','sanitaet',7800,'Gehstock Eigenanteil',[('Gehstock mit angepasstem Griff',7800)],'Gehstock persönlich abgeholt. Zahlung per Girokarte. Kundin Adelheid Pfister.'),
      ('W-24051','2024-05-10','fenster',360000,'Reparatur Fenster und Terrassentür',[('Beschläge und Dichtungen',144000),('Arbeitszeit und Anfahrt',216000)],'Auftraggeber: Ruprecht Pfister, Kastanienwinkel 6, 16321 Bernau. Leistungsort: Kastanienwinkel 6. Rechnung am 13.05.2024 durch Herrn Pfister bezahlt. Auf der Kopie steht handschriftlich: Mama übernimmt die Fenster wie besprochen.'),
      ('SS-24102','2024-07-10','sanitaet',18900,'Duschsitz Eigenanteil',[('Duschsitz einschließlich Befestigung',18900)],'Einbau im Bad Fliederbogen 17. Zahlung per Girokarte; Übergabe an Frau Pfister.'),
      ('ZT-250508','2025-05-08','egon',79900,'Belegkopie Tablet ZT-250508',[('Tablet 128 GB',69900),('Schutzhülle und Einrichtung',10000)],'Verkäufer: Technikladen Zinnober GmbH, Bildgasse 21, 13127 Berlin. Rechnungsempfängerin: Adelheid Pfister. Abholung laut Abholschein durch Egon Knusper. Serienende 7K31. Es liegt nur diese vom Helfer übersandte Belegkopie vor.'),
      ('SS-26180','2026-07-09','sanitaet',68000,'Rollator mit Zubehör Eigenanteil',[('Rollator Leichtmodell',59900),('Tasche und Schirmhalter',8100)],'Auslieferung Fliederbogen 17 am 09.07.2026. Anpassung in der Wohnung bestätigt; Kartenzahlung bei Lieferung. Erstattungsantrag ist nicht Gegenstand dieser Rechnung.'),
    ]
    for id,d,s,total,sub,lines,note in extra_invoices:
        tids=[t['id'] for t in tx if id in t['receipt_ids']]
        invoice(id,d,s,total,sub,lines,tids[0] if tids else None,note)
    # Abrechnungen werden getrennt als ausführliche Schreiben erzeugt.
    tx.sort(key=lambda t:(t['date'],t['account_id'],t['id']))
    accounts=[dict(id='GIRO',name='Girokonto Endziffern 0441',opening_balance_cents=430000,opening_cents=430000,account_reference='FS-G-0441'),dict(id='SPAR',name='Sparkonto Endziffern 0987',opening_balance_cents=2800000,opening_cents=2800000,account_reference='FS-S-0987')]
    for acc in accounts:
        acc['closing_balance_cents']=acc['opening_cents']+sum(t['amount_cents'] for t in tx if t['account']==acc['id'])
    notes=[]
    for item,party,amount,freq,note in [
      ('Altersrente','Rentenstelle Nord',208000,'monatlich','Im September steht dieser Betrag im Kontoauszug. Frühere Rentenanpassungen sind noch abzugleichen.'),
      ('Hinterbliebenenrente','Rentenstelle Nord',48500,'monatlich','Getrennte Zahlung neben der Altersrente.'),
      ('Warmmiete','Hausverwaltung Lindenblatt KG',82000,'monatlich','Aktueller Betrag; früher war die Miete niedriger. Nachzahlungen kommen gesondert.'),
      ('Stromabschlag','Nordlicht Energie Berlin GmbH',7900,'monatlich','Die Jahresabrechnungen liegen im Ordner. Guthaben bitte nicht vergessen.'),
      ('Telefon und Internet','Sprechfink Telekom GmbH',4499,'monatlich','Anschluss wird weiter gebraucht. Den Termin der Preiserhöhung weiß Adelheid nicht mehr.'),
      ('Haushaltshilfe','Alltagshilfe Mohnblüte GmbH',12650,'monatlich','Adelheid möchte, dass die Haushaltshilfe weiterkommt.'),
      ('Nachbarschaftshilfe','Egon Knusper',14500,'monatlich','Einkauf dienstags erwünscht; andere Beträge bitte einzeln ansehen.'),
      ('Filme am Freitag','SofaKino Digital GmbH',1299,'monatlich','Soll nach ausdrücklichem Wunsch bleiben.'),
      ('Ratgeber','LebensKompass Direkt GmbH',6990,'monatlich','Adelheid erinnert sich an einen kostenlosen Rentencheck; Bestellung und Nutzung noch unklar.'),
      ('Teilnahmeservice','Glücksfenster Service GmbH',2990,'monatlich','Name sagt Adelheid wenig. Im September kam noch eine andere Abbuchung.'),
      ('Geld für Fenster','Ruprecht Pfister',420000,'einmalig','Überweisung Mai 2024; Rechnung nennt Bernau, 600 Euro kamen zurück.'),
      ('Transporterhilfe','Ruprecht Pfister',120000,'einmalig 2024','Ruprecht nennt 300 Euro Teilzahlung im Januar 2026. Neue Zahlung 2026 gesondert klären.'),
      ('Bargeld in Porzellandose','Adelheid Pfister',None,'Bestand offen','Noch nicht gemeinsam gezählt; Einkaufswünsche im Heft sind keine Ausgabebelege.'),
      ('Futter und Streu','Tierladen Pfötchen',4850,'monatlich','Für Mürbchen. Adelheid möchte die Versorgung beibehalten.'),
    ]: notes.append(dict(item=item,party=party,amount_cents=amount,frequency=freq,note=note,source='01_Uebernahme/2026-10-02_Gespraech_Adelheid.docx; Kontoauszüge und E-Mail-Ordner',author='Dr. Maja Winterfeld nach Gespräch und erster Sichtung am 08.10.2026'))
    return dict(schema_version=1,title='Betreuung Adelheid Pfister',period_start='2023-10-01',period_end='2026-09-30',cutoff='2026-10-08',appointment_date='2026-10-01',currency='EUR',accounts=accounts,transactions=tx,contacts=contacts,invoices=invoices,household_sheet_rows=notes,household_notes=[dict(date='2026-10-02',author='Adelheid Pfister',note='SofaKino soll bleiben; Filme mit Mürbchen gehören zum Freitag. Glücksfenster und LebensKompass sagen mir nichts. Bargeld in der Porzellandose nicht gezählt. Ruprecht wollte mir die Transporterhilfe zurückzahlen.')],contracts=[dict(party='SofaKino Digital GmbH',reference='SK-77380',known='Monatliche Abbuchung; ausdrücklich gewünschte Nutzung'),dict(party='LebensKompass Direkt GmbH',reference='LK-55771',known='Bestellbestätigung, Bildschirmfoto und Beschwerde widersprechen sich; vollständiger Bestellablauf fehlt'),dict(party='Glücksfenster Service GmbH',reference='GF-90335',known='Telefonischer Kontakt behauptet; Aufzeichnung angefordert, noch nicht vorgelegt')])

def correspondence():
    return [
      ('2023-10-12','juna','adelheid','Dein neuer Ordner im Schrank','Liebe Tante Adelheid, ich habe die Kontoauszüge in den blauen Ordner gelegt, jeweils das neueste Blatt vorn. Rentenbriefe sind im Umschlag dahinter. Die Quittungen vom Wochenmarkt kannst Du weiter in der Porzellandose sammeln. Bitte wirf die kleinen Zettel nicht weg; wenn ich im Januar komme, sortieren wir wieder. Das Papierheft ist kein Kassenbuch: Die Beträge darin sind Einkaufswünsche, keine Bestätigung, dass schon bezahlt wurde.\n\nSofaKino läuft wieder auf dem Fernseher. Dein Kennwort bleibt bei Dir. Du wolltest die alten Komödien freitags sehen, deshalb habe ich das normale Monatsabo genommen. Zusätzliche Pakete haben wir nicht bestellt. Ich habe Dir aufgeschrieben, wie Du die große Schrift einstellst. Liebe Grüße, Juna',None),
      ('2024-02-14','adelheid','juna','Zum Abschluss','Meine liebe Juna, die 450 Euro sind für Dich. Du hast die Prüfung bestanden und sollst mit Deinen Freundinnen essen gehen oder Dir eine schöne Reise gönnen. Das ist kein Geld für Einkäufe für mich und Du musst es mir nicht wiedergeben. Schreib mir aber, wie es Dir gefällt. Am Freitag bring bitte nur die Katzentabletten mit; das Geld dafür gebe ich Dir aus der Dose. Ich möchte, dass Du mich weiterhin Tante nennst und nicht Kundin.\n\nDie Überweisung habe ich selbst am Schalter abgegeben. Die Dame hat mir geholfen, den langen Namen richtig zu schreiben. Alles Liebe, Deine Tante Adelheid',None),
      ('2024-03-14','strom','adelheid','Jahresabrechnung Strom 2023','Sehr geehrte Frau Pfister, aus Ihrer Stromabrechnung ergibt sich ein Guthaben von 84,00 EUR. Wir haben es am 12.03.2024 auf das bekannte Girokonto ausgezahlt. Es handelt sich um die Abrechnung des Lieferjahres 2023; die monatlichen Abschläge werden dadurch nicht rückwirkend geändert. Bitte gleichen Sie den Zahlungseingang mit Ihrem Kontoauszug ab.\n\nFalls Herr Knusper künftig Unterlagen für Sie einreichen soll, benötigen wir eine nachvollziehbare Bevollmächtigung. Bisher steht allein Ihre Anschrift in unserem Kundenstamm. Unsere ausführliche Abrechnung finden Sie im Anhang. Freundliche Grüße, Mathilde Finke, Kundenservice','03_Belege/NE-2023.pdf'),
      ('2024-05-09','ruprecht','adelheid','Fensterangebot jetzt da','Hallo Mama, die Fenster in Bernau lassen sich hinten kaum noch schließen. Wendel nimmt 3.600 Euro für Beschläge, Dichtungen, Arbeitszeit und Anfahrt. Ich würde die Rechnung zunächst zahlen und brauche davor etwas Luft auf dem Konto. Du hattest am Sonntag gesagt, Du hilfst mir. Kannst Du mir 4.200 Euro überweisen? Die 600 Euro, die übrig bleiben, schicke ich zurück.\n\nWir sollten aufschreiben, ob Du das zurückhaben willst. Ich habe aus unserem Gespräch verstanden, dass Du die eigentliche Reparatur übernimmst, weil die Enkel dort wohnen. Juna meinte gestern, sie habe Dich anders verstanden. Ich rufe heute Abend an, statt hier etwas festzulegen. Grüße, Ruprecht',None),
      ('2024-05-17','ruprecht','juna','Fenster und Mamas Geld','Hallo Juna, ja, die 4.200 Euro sind bei mir angekommen. Die Rechnung war tatsächlich 3.600 Euro. Mama hat mir am Telefon gesagt, die Fenster seien ihr Geschenk an uns. Du musst daraus kein Familiengericht machen. Die Rechnung ist an mich adressiert, weil es mein Haus ist. Den überschüssigen Betrag überweise ich, sobald meine Bankfreigabe wieder funktioniert.\n\nIch hänge die Rechnung an, damit Du wenigstens siehst, was gemacht wurde. Es wurde nichts in Mamas Mietwohnung ausgetauscht. Ich möchte nicht, dass im Ordner später der falsche Einbauort steht. Wenn Mama eine Rückzahlung verlangt, reden wir darüber. Ruprecht','03_Belege/W-24051.pdf'),
      ('2024-06-08','ruprecht','adelheid','600 Euro zurück','Hallo Mama, die 600 Euro Rest von den Fenstern sind gestern rausgegangen. Die Bank nennt als Verwendungszweck Rest Fenster zurück. Die eigentliche Handwerkerrechnung über 3.600 Euro habe ich bezahlt. Juna hat nach einem Darlehenszettel gefragt. So einen haben wir nicht gemacht.\n\nBitte hebe diese Nachricht mit der Rechnung auf; sonst denkt später jemand, ich hätte die gesamten 4.200 Euro behalten. Wir sehen uns Sonntag zum Kaffee. Ich bringe Dir den neuen Fliegenschutz für die Küche mit. Der ist von mir bezahlt und dafür brauche ich nichts zurück. Dein Ruprecht',None),
      ('2024-09-02','egon','adelheid','Absprachen für die Hilfe','Liebe Frau Pfister, ab September kümmere ich mich regelmäßig um Einkaufsfahrten und die kleinen Probleme mit Telefon und Fernseher. Wir haben 145 Euro im Monat besprochen. Ich lege unseren kurzen Zettel bei. Bezahlen können Sie jeweils nach dem 23. des Monats. Wenn Sie etwas im Laden haben möchten, rechne ich das zusätzlich ab; die Einkaufspreise stecken nicht in meiner Pauschale.\n\nIch bin kein gerichtlich bestellter Betreuer. Wenn ich mich am Telefon als Ihr Betreuer vorgestellt habe, war damit gemeint, dass ich mich kümmere. Ich sollte mich künftig als Nachbarschaftshilfe vorstellen. Für Bankgeschäfte sollen wir immer vorher reden. Herzliche Grüße, Egon Knusper','04_Schriftverkehr/2024-09-02_Abrede_Nachbarschaftshilfe.docx'),
      ('2024-10-05','ruprecht','adelheid','Transporterhilfe','Hallo Mama, danke für die 1.200 Euro. Ohne den Transporter komme ich nicht zu den Baustellen. Diesmal ist es ein Darlehen, das steht außer Frage. Ich rechne mit dem Geld aus zwei offenen Rechnungen im Winter und zahle Dir dann etwas zurück. Einen festen Monat kann ich Dir heute leider nicht zusagen.\n\nIch weiß, dass Du für den Winter genug Geld auf Deinem Konto behalten möchtest. Bitte lass Dir dafür nichts vom Sparbuch wegnehmen. Die Werkstattrechnung bekomme ich erst bei Abholung. Ich schicke sie nach, sobald sie da ist. Dein Ruprecht',None),
      ('2024-12-03','haus','adelheid','Betriebskosten 2023 und Vorauszahlung','Sehr geehrte Frau Pfister, die Betriebskostenabrechnung für 2023 endet mit einer Nachzahlung von 320,00 EUR. Die beigefügte Aufstellung erläutert die angesetzten Kosten und Ihre Vorauszahlungen. Die Nachzahlung ziehen wir am 12.12.2024 ein. Ab Januar 2025 erhöht sich die monatliche Vorauszahlung um 40,00 EUR; die Gesamtmiete beträgt dann 820,00 EUR.\n\nEine Prüfung der Belege ist nach Terminvereinbarung möglich. Für Rückfragen nennen Sie bitte das Mietkonto LB-1702. Schreiben Sie uns, wenn Sie die Rechnung lieber in größerer Schrift benötigen. Mit freundlichen Grüßen, Ottilie Beck, Hausverwaltung Lindenblatt','03_Belege/HV-23.pdf'),
      ('2025-01-06','abo','adelheid','Willkommen bei LebensKompass Digital','Sehr geehrte Frau Pfister, wir bestätigen die Registrierung für unser Digitalpaket unter der Kundennummer LK-55771. Sie erhalten Zugang zu Ratgebern, Musterschreiben und unserer telefonischen Informationslinie. In unserem System ist eine Bestellung vom 03.01.2025 um 18:42 Uhr vermerkt. Die Nutzung kostet monatlich 69,90 EUR. Die nächste Abrechnung erfolgt am 11.01.2025 beziehungsweise am folgenden Bankarbeitstag.\n\nDer Bestätigungslink wurde an egon@knusper-hilfe.example versandt. Bei Fragen antworten Sie bitte unter Angabe der Kundennummer. Die Vertragsunterlagen sind im Kundenbereich hinterlegt. Eine vollständige Kopie des Bestellformulars ist dieser Nachricht nicht beigefügt. Mit freundlichen Grüßen, LebensKompass Direkt GmbH',None),
      ('2025-01-08','egon','juna','Das mit dem Ratgeber','Hallo Juna, Adelheid hatte mich wegen eines kostenlosen Rentenchecks gefragt. Ich habe ihr den Computer aufgestellt und meine E-Mail-Adresse eingegeben, weil ihr Postfach dauernd voll war. Ob sie später den kostenpflichtigen Teil angeklickt hat, weiß ich nicht mehr. Der Bildschirm sah nach einem unverbindlichen Informationsangebot aus. Ich habe noch ein Foto vom Ende des Formulars.\n\nIch bin anschließend einkaufen gegangen. Das Fenster blieb offen. Es kann sein, dass sie danach noch selbst weitergemacht hat. Die Bestätigung kam zu mir, ich habe sie ausgedruckt und auf den Küchentisch gelegt. Egon','05_Bildschirmfotos/01_LebensKompass_Bestellseite.png'),
      ('2025-03-13','strom','adelheid','Guthaben aus 2024 überwiesen','Sehr geehrte Frau Pfister, das Guthaben von 32,00 EUR aus der Jahresabrechnung 2024 wurde am 11.03.2025 überwiesen. Ihr Abschlag beträgt seit Januar 79,00 EUR monatlich. Bitte verrechnen Sie das Guthaben nicht selbst mit dem nächsten Abschlag; dieser wird regulär eingezogen.\n\nDie Abrechnung weist einen höheren Verbrauch aus als im Vorjahr. Für eine Überprüfung des Zählerstands genügt ein lesbares Foto der Anzeige mit Aufnahmedatum. Ihre Abrechnung liegt dieser Nachricht bei. Freundliche Grüße, Mathilde Finke','03_Belege/NE-2024.pdf'),
      ('2025-04-15','juna','adelheid','Zahnarzt Betrag nur kurz vorstrecken','Liebe Tante, danke, dass Du mir die 450 Euro bis zum Eingang meiner Erstattung leihst. Ich zahle sie spätestens Ende April zurück. Das hat mit Deinem Geschenk zu meinem Abschluss im letzten Jahr nichts zu tun. Bitte leg beide Vorgänge nicht in denselben Umschlag; sonst bekommen wir beim Sortieren wieder Streit.\n\nIch habe Dir keinen Einkauf abgerechnet. Die Überweisung ist nur meine kurzfristige Überbrückung. Die Rechnung enthält meine Gesundheitsdaten; ich möchte sie Dir gern zeigen, aber nicht an Egon weiterleiten. Liebe Grüße, Juna',None),
      ('2025-04-30','juna','adelheid','450 Euro wieder bei Dir','Liebe Tante, gestern habe ich Dir die 450 Euro für die vorgestreckte Zahnbehandlung zurückgeschickt. Die Bankbestätigung sagt als Verwendungszweck Zahnbehandlung erstattet. Bitte sieh am Kontoauszug nach, ob der Betrag angekommen ist.\n\nAm Wochenende bringe ich Dir den neuen Kalender. Dein Heft mit den Einkaufsbeträgen liegt bei der Telefonstation. Die Aprilseiten habe ich nicht abfotografiert, weil Egon es gerade mitgenommen hatte. Frag ihn bitte danach, damit die kleinen Kassenzettel nicht verloren gehen. Liebe Grüße, Juna',None),
      ('2025-05-09','egon','adelheid','Tablet geliefert','Liebe Frau Pfister, das neue Tablet steht auf dem Sideboard. Es hat 799 Euro einschließlich Hülle und Einrichtung gekostet; bezahlt wurde direkt im Geschäft von Ihrem Konto. Ich habe es für Sie abgeholt, weil Sie an dem Tag den Termin beim Sanitätshaus hatten. Die Belegkopie liegt bei.\n\nDie letzten vier Zeichen der Seriennummer sind 7K31. Bitte nicht mit dem schwarzen Gerät meines Neffen verwechseln, das ich nur zum Übertragen der Bilder dabei hatte. Die Fotos von Mürbchen sind jetzt auf Ihrem Gerät. Ich habe kein weiteres Abonnement dafür abgeschlossen. Viele Grüße, Egon','03_Belege/ZT-250508.pdf'),
      ('2025-08-08','egon','adelheid','Drucker und Geldbeutel','Liebe Frau Pfister, die 275 Euro für Drucker und Einrichtung sind angekommen. Ich kaufe das Gerät am Wochenende. Wenn es preiswerter wird, bringe ich das Wechselgeld mit. Die Tintenpatronen vom alten Drucker können wir nicht mehr verwenden.\n\nSie hatten mir außerdem den kleinen Geldbeutel für den Markt gegeben. Den habe ich nachmittags auf den Küchentisch gelegt. Ein Kassenzettel vom Obststand fehlt, weil es geregnet hat und er unleserlich geworden ist. Den Betrag weiß ich nicht mehr genau, ungefähr 18 Euro. Das gehört nicht zur Druckerüberweisung. Viele Grüße, Egon',None),
      ('2025-09-18','egon','juna','Deine Nachfrage zu den 2200 Euro','Hallo Juna, Adelheid hat mir 2.200 Euro gegeben, weil ich mich die ganze Zeit kümmere. Sie hat Dankeschön Unterstützung auf die Überweisung geschrieben. Ich habe ihr keine Rechnung über diesen Betrag gestellt. Die monatlichen 145 Euro laufen daneben weiter, das ist unsere Abrede.\n\nDu fragst, ob ich sie gedrängt habe. Das bestreite ich. Sie hat selbst davon angefangen. Eine Zeugin war nicht dabei. Ich habe keine Vollmacht, für sie Geschenke an mich zu unterschreiben. Falls Du meinst, das Geld müsse zurück, sollen wir gemeinsam mit Adelheid reden. Ich will keinen Streit über ihren Kopf hinweg. Egon',None),
      ('2025-11-07','juna','abo','Doppelte Abbuchung Kundennummer LK-55771','Sehr geehrte Damen und Herren, Frau Pfister hat mich gebeten, wegen einer zusätzlichen Abbuchung von 69,90 EUR vom 06.11.2025 nachzufragen. Im Oktober wurde bereits der regelmäßige Monatsbetrag eingezogen. Warum belasten Sie denselben Monat erneut? Bitte erläutern Sie dies und erstatten Sie eine Doppelzahlung.\n\nDiese Nachricht betrifft zunächst die konkrete Doppelbelastung. Frau Pfister kann Ihren Dienst keiner bewussten Bestellung zuordnen. Ich bitte zusätzlich um die Bestellung und die damals angezeigten Vertragsbedingungen. Eine Vollmacht zur Erklärung weiterer rechtsgeschäftlicher Erklärungen füge ich hier nicht bei. Mit freundlichen Grüßen, Juna Özdemir-Pfister',None),
      ('2025-11-22','abo','juna','Korrektur der Nachbelastung','Sehr geehrte Frau Özdemir-Pfister, wir haben die Nachbelastung storniert und am 21.11.2025 69,90 EUR zurückgezahlt. Der doppelte Einzug beruhte auf einer technischen Zuordnung. Die laufenden Monatsbeiträge sind davon unberührt.\n\nFür die Übersendung personenbezogener Vertragsunterlagen benötigen wir eine Legitimation. Bitte lassen Sie uns eine Erklärung unserer Kundin oder einen geeigneten Vertretungsnachweis zukommen. Die Vertragsfrage ist mit der Erstattung der Doppelzahlung nicht beantwortet. Mit freundlichen Grüßen, Paula Kranz, LebensKompass Direkt GmbH',None),
      ('2025-12-04','haus','adelheid','Betriebskosten 2024','Sehr geehrte Frau Pfister, die Betriebskostenabrechnung 2024 ergibt eine Nachzahlung von 410,00 EUR. Wir ziehen den Betrag am 11.12.2025 vom bekannten Konto ein. Die laufende Warmmiete von 820,00 EUR bleibt unverändert.\n\nDie Rechnungen für Hausreinigung und Heizung können Sie bei uns einsehen. Herr Knusper hat telefonisch um eine Übersendung an seine Privatadresse gebeten; wir haben dies zunächst zurückgestellt, weil er in unserem System nicht als Bevollmächtigter erfasst ist. Bitte teilen Sie uns schriftlich mit, an wen Unterlagen gehen sollen. Freundliche Grüße, Ottilie Beck','03_Belege/HV-24.pdf'),
      ('2026-01-14','ruprecht','adelheid','Erste Rate Transporter','Hallo Mama, 300 Euro sind gestern auf Dein Konto gegangen. Das ist eine erste Rate auf die 1.200 Euro vom Oktober 2024. Es sind also noch 900 Euro offen. Die Fenster von damals rechne ich dabei nicht mit ein.\n\nIch weiß, dass das viel länger dauert als versprochen. Ich habe Dir im Winter keine weiteren Raten fest zugesagt, weil ich es nicht halten konnte. Bitte sag mir, wenn Du das Geld jetzt für Dich brauchst. Dann muss ich eine andere Lösung finden. Dein Ruprecht',None),
      ('2026-03-14','strom','adelheid','Jahresabrechnung 2025','Sehr geehrte Frau Pfister, aus der beigefügten Stromabrechnung 2025 ergibt sich eine Nachzahlung von 93,00 EUR. Der Betrag wurde am 12.03.2026 eingezogen. Die monatlichen Abschläge bleiben vorerst bei 79,00 EUR.\n\nBei der letzten Ablesung hat Herr Knusper den Zählerstand telefonisch gemeldet. Unsere Abrechnung enthält den Wert als Kundenablesung. Wenn Sie daran zweifeln, schicken Sie bitte einen aktuellen Stand; eine Schätzung ist in dieser Rechnung nicht angesetzt. Mit freundlichen Grüßen, Mathilde Finke','03_Belege/NE-2025.pdf'),
      ('2026-04-10','egon','adelheid','Handy nach Sturz','Liebe Frau Pfister, ich habe die 350 Euro gesehen und kümmere mich um das Ersatzhandy. Das alte Gerät geht zwar noch an, aber das Glas ist gesplittert. Die Daten sollen erhalten bleiben. Bitte nehmen Sie das alte Telefon nicht auseinander.\n\nDie Rechnung und das Wechselgeld bringe ich mit, sobald alles eingerichtet ist. Es ist kein neues Mobilfunkabonnement nötig, wir setzen Ihre bisherige Karte ein. Ich werde dafür weder Ihren Festnetzvertrag noch das Fernsehabo anfassen. Viele Grüße, Egon',None),
      ('2026-05-15','ruprecht','juna','Noch einmal 1200 Euro','Hallo Juna, Mama hat mir gestern noch einmal 1.200 Euro überwiesen. Es stimmt, dass vom ersten Transporterdarlehen noch 900 Euro offen sind. Ich hatte ihr erklärt, dass mein Auftraggeber nicht zahlt. Sie hat gesagt, ich solle nicht bankrottgehen.\n\nOb sie die neue Summe ebenfalls zurückhaben wollte, haben wir nicht sauber ausgesprochen. Im Verwendungszweck steht nochmal überbrücken, wie besprochen. Daraus kannst Du für Dich lesen, was Du möchtest; ich möchte es mit ihr klären. Ich habe im Augenblick keine Rücklage für eine sofortige Rückzahlung. Ruprecht',None),
      ('2026-06-18','juna','egon','Karte am Dienstag','Hallo Egon, Tante Adelheid konnte mir nicht sagen, wer am Dienstag 650 Euro abgehoben hat. Sie erinnert sich an den normalen Marktbesuch, aber nicht an diesen zusätzlichen Betrag. Du hattest mir geschrieben, Du seist an dem Vormittag in Potsdam gewesen. War die Karte bei ihr oder bei Dir?\n\nIch möchte keine Unterstellung daraus machen. Es ist nur inzwischen schwer, die Barbestände nachzuvollziehen. Bitte bring das Einkaufsheft und die noch vorhandenen Quittungen mit. Ein Foto vom Küchenkalender hilft nur, wenn wir auch wissen, wann es aufgenommen wurde. Juna',None),
      ('2026-08-12','egon','juna','Jahrespaket','Hallo Juna, die 980 Euro vom 11.08. sind für zusätzliche Fahrten und Erreichbarkeit im kommenden Jahr. Die regelmäßige Pauschale sollte bestehen bleiben. Wir hatten darüber auf der Terrasse gesprochen; unterschrieben hat Adelheid nichts. Ich kann jetzt nicht mehr aufschreiben, welche Fahrten wir einzeln gemeint hatten.\n\nDu meinst, die Vorauszahlung passe nicht zu den laufenden Rechnungen. Dann müssen wir abgrenzen, welche Hilfe jeweils gemeint war. Ich habe im Juli an drei Tagen ihre Post sortiert. Ich werde eine Liste machen, brauche dafür aber meinen Kalender. Egon',None),
      ('2026-09-20','lotto','adelheid','Sonderziehung und Kontaktdaten','Sehr geehrte Frau Pfister, die Gebühr von 89,00 EUR betrifft die im September aktivierte Sonderziehung Ihres Teilnahmeservices GF-90335. Nach unserer Notiz wurde die Teilnahme in einem Telefonat am 15.09.2026 bestätigt. Ihre monatliche Servicepauschale von 29,90 EUR läuft getrennt weiter.\n\nDie Kontaktperson ist in unserem System als Herr Knusper, Betreuung, hinterlegt. Eine Tonaufzeichnung fügen wir nicht bei. Bitte richten Sie Rückfragen an unseren Kundenservice. Mit freundlichen Grüßen, Hubert Blank, Glücksfenster Service GmbH',None),
      ('2026-10-02','maja','bank','Betreuungsübernahme und Auszüge','Sehr geehrte Damen und Herren, seit dem 01.10.2026 bin ich für Frau Adelheid Pfister im Aufgabenbereich Vermögenssorge bestellt. Bitte erfassen Sie mich nach Prüfung des beigefügten Nachweises als Ansprechpartnerin und teilen Sie mir mit, welche Konten, Karten und Vollmachten zu Frau Pfister geführt werden.\n\nFür die Bestandsaufnahme benötige ich die Auszüge und Buchungsdaten vom 01.10.2023 bis 30.09.2026. Bitte ändern Sie keine Daueraufträge allein aufgrund dieser Auskunftsanfrage. Zu einzelnen Vorgängen werde ich nach Durchsicht gesondert Stellung nehmen. Mit freundlichen Grüßen, Dr. Maja Winterfeld','01_Uebernahme/2026-10-01_Bestellungsmitteilung.pdf'),
      ('2026-10-05','bank','maja','Auszüge und Buchungsdatei bereitgestellt','Sehr geehrte Frau Dr. Winterfeld, Sie erhalten die Monatsauszüge beider Konten von Oktober 2023 bis September 2026 sowie die angeforderte Buchungsdatei. Der Export enthält gebuchte Umsätze und keine vorgemerkten Zahlungen. Die Auszugsnummern entsprechen den Kalendermonaten. Kontoüberträge erscheinen auf beiden Konten als jeweils eigener Umsatz.\n\nEine Bankvollmacht für Herrn Knusper ist nicht hinterlegt. Ob ihm Frau Pfister eine Karte oder Zugangsdaten tatsächlich überlassen hat, können wir aus den Stammdaten nicht feststellen. Für Einzelheiten zu Abhebungen benötigen wir die konkreten Buchungen. Ein Kartenumsatz belegt nicht, wer die Karte bedient hat. Freundliche Grüße, Dorothea Rabe, Fensterbank Spree eG','06_Tabellen/Bankexport_2023-10_bis_2026-09.xlsx'),
      ('2026-10-06','juna','maja','Kartons und Bilder vom Telefon','Sehr geehrte Frau Dr. Winterfeld, ich bringe Ihnen die beiden Ordner und die Schuhschachtel. Die Kontoauszüge hat die Bank wohl inzwischen direkt geschickt. Mein Telefon enthält noch Bilder der Ratgeberseite und einen Ausschnitt aus der Nachricht von Herrn Knusper. Ich habe sie nicht nachbearbeitet; die Dateien stammen aus unterschiedlichen Jahren.\n\nBitte sprechen Sie auch allein mit meiner Tante. Sie will Ruprecht nicht verklagen und Egon nicht einfach vor die Tür setzen. Trotzdem fragt sie inzwischen selbst, warum so viel Geld abgebucht wird. Ich habe nicht alles gesehen und kann nichts über ihren Willen bei jedem einzelnen Vorgang sagen. Mit freundlichen Grüßen, Juna Özdemir-Pfister','05_Bildschirmfotos/02_Chat_Karte_Juni.png'),
      ('2026-10-07','egon','maja','Unterlagen folgen','Sehr geehrte Frau Dr. Winterfeld, ich habe mich um Frau Pfister gekümmert, aber ich bin nicht gerichtlich zum Betreuer bestellt. Die Gerätebelege suche ich zusammen. Den Drucker habe ich gebraucht gekauft, deshalb habe ich nur eine kurze Quittung. Ich weiß noch nicht, wo sie ist. Das Handy liegt bei mir, weil die Datenübertragung noch nicht fertig ist.\n\nDie 2.200 Euro waren nach meiner Erinnerung ein Geschenk. Die 980 Euro waren für zusätzliche Hilfe vorgesehen. Bitte schreiben Sie mir genau, welche Aufstellung Sie brauchen und bis wann. Frau Pfister hatte mich gestern gebeten, weiter dienstags einzukaufen. Mit freundlichen Grüßen, Egon Knusper','03_Belege/EK-2026-09.pdf'),
      ('2026-10-08','maja','juna','Bestandsaufnahme geht weiter','Sehr geehrte Frau Özdemir-Pfister, vielen Dank für die Unterlagen. Ich ordne derzeit die Kontobewegungen und die vorhandenen Belege. Bitte reichen Sie die Fotos in der ursprünglichen Datei ein, wenn Sie diese noch haben. Erinnerungen und eigene Beobachtungen werde ich getrennt festhalten.\n\nMit Frau Pfister bespreche ich, welche Leistungen sie künftig tatsächlich möchte. Aus einzelnen Zahlungen werde ich ohne weitere Klärung weder eine Berechtigung noch einen Missbrauch ableiten. Bitte teilen Sie mir noch mit, wann Sie die Geldkassette zuletzt gesehen haben und ob Sie einen damaligen Bestand sicher kennen. Mit freundlichen Grüßen, Dr. Maja Winterfeld',None),
    ]

def build(data):
    from reportlab.pdfgen import canvas
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from docx import Document
    from docx.shared import Pt, Mm, RGBColor
    from docx.oxml.ns import qn
    fonts=Path('/System/Library/Fonts/Supplemental')
    fallback=Path('/tmp/kk338/liberation')
    regular=fonts/'Times New Roman.ttf'; bold=fonts/'Times New Roman Bold.ttf'
    if not regular.exists():
        candidates=list(fallback.rglob('LiberationSerif-Regular.ttf'));regular=candidates[0];bold=regular.with_name('LiberationSerif-Bold.ttf')
    pdfmetrics.registerFont(TTFont('CaseSerif',str(regular)));pdfmetrics.registerFont(TTFont('CaseSerifBold',str(bold)))
    pdfmetrics.registerFontFamily('CaseSerif',normal='CaseSerif',bold='CaseSerifBold',italic='CaseSerif',boldItalic='CaseSerifBold')
    style=ParagraphStyle('Body',fontName='CaseSerif',fontSize=11,leading=14,spaceAfter=8)
    title=ParagraphStyle('Title',parent=style,fontName='CaseSerifBold',fontSize=17,leading=20,spaceAfter=15)
    small=ParagraphStyle('Small',parent=style,fontSize=9,leading=11,spaceAfter=3)
    header=ParagraphStyle('Head',parent=style,fontName='CaseSerifBold',spaceBefore=8)
    CASE.mkdir(parents=True,exist_ok=True)
    for p in ['01_Uebernahme','02_Konten','03_Belege','04_Schriftverkehr','05_Bildschirmfotos','06_Tabellen','07_E-Mails']: (CASE/p).mkdir(exist_ok=True)
    cmap={c['id']:c for c in data['contacts']}
    artifacts=[]
    def P(text,st=style): return Paragraph(escape(str(text)).replace('\n','<br/>'),st)
    def pdf(rel,heading,paras,table=None,footer=''):
        path=CASE/rel;path.parent.mkdir(parents=True,exist_ok=True)
        story=[P(heading,title)]
        for s in paras: story.extend([P(s),Spacer(1,3)])
        if table:
            rows=[[P(c,small) for c in row] for row in table]
            widths=([62,263,80,82] if len(rows[0])==4 else [340,147])
            t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e9eef1')),('FONTNAME',(0,0),(-1,0),'CaseSerifBold'),('GRID',(0,0),(-1,-1),.3,colors.HexColor('#c6cbd0')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f6f7f8')])]))
            story.append(t)
        if footer: story.extend([Spacer(1,12),P(footer)])
        def page(c,d):
            c.setFont('CaseSerif',9);c.setFillColor(colors.HexColor('#5b626a'));c.drawString(54,30,path.stem[:85]);c.drawRightString(A4[0]-54,30,str(d.page))
        SimpleDocTemplate(str(path),pagesize=A4,rightMargin=54,leftMargin=54,topMargin=48,bottomMargin=48,title=heading,author='').build(story,onFirstPage=page,onLaterPages=page)
        artifacts.append(rel)
    def word(rel,heading,paras):
        doc=Document();sec=doc.sections[0];sec.page_width=Mm(210);sec.page_height=Mm(297)
        sec.top_margin=sec.bottom_margin=Mm(22);sec.left_margin=sec.right_margin=Mm(25)
        for n in ('Normal','Title','Heading 1','Heading 2'):
            s=doc.styles[n];s.font.name='Times New Roman';s.font.size=Pt(11);s.font.color.rgb=RGBColor(0,0,0);s.element.get_or_add_rPr().rFonts.set(qn('w:ascii'),'Times New Roman');s.element.rPr.rFonts.set(qn('w:hAnsi'),'Times New Roman')
            for key in list(s.element.rPr.rFonts.attrib):
                if key.endswith('Theme') or key.endswith('theme'): del s.element.rPr.rFonts.attrib[key]
            for border in list(s.element.iter(qn('w:pBdr'))): border.getparent().remove(border)
        doc.styles['Normal'].paragraph_format.space_after=Pt(8);doc.styles['Normal'].paragraph_format.line_spacing=1.05
        doc.styles['Title'].font.size=Pt(17);doc.styles['Title'].font.bold=True
        hp=doc.add_paragraph(heading,style='Title');hp.runs[0].font.name='Times New Roman';hp.runs[0].font.color.rgb=RGBColor(0,0,0)
        for border in list(hp._p.iter(qn('w:pBdr'))): border.getparent().remove(border)
        for s in paras: doc.add_paragraph(s)
        doc.core_properties.author='';doc.core_properties.title=heading
        doc.save(CASE/rel);artifacts.append(rel)
    # Zwei vollständige Kontoketten mit getrenntem Anfangs- und Endbestand je Monat.
    for acc in data['accounts']:
        balance=acc['opening_cents']
        for i in range(36):
            y,m=2023+(9+i)//12,(9+i)%12+1;ym=f'{y}-{m:02}'
            tx=[t for t in data['transactions'] if t['account']==acc['id'] and t['date'].startswith(ym)]
            opening=balance;rows=[['Buchung','Empfänger oder Absender und Verwendungszweck','Betrag','Kontostand']]
            for t in tx:
                balance+=t['amount_cents'];rows.append([t['date'][8:10]+'.'+t['date'][5:7]+'.',t['party']+'\n'+t['purpose']+'\nBuchungsreferenz '+t['id'],money(t['amount_cents']),money(balance)])
            if not tx:rows.append(['','Keine gebuchten Umsätze in diesem Monat.','',''])
            pdf(f'02_Konten/{acc["id"]}_{ym}.pdf','Fensterbank Spree eG',[
                'Uferbogen 12, 10179 Berlin | Kontenservice\nAdelheid Pfister, Fliederbogen 17, 13125 Berlin',
                f'Kontoauszug {m:02}/{y} | {acc["name"]} | Kontoreferenz {acc["account_reference"]}\nZeitraum 01.{m:02}.{y} bis {calendar.monthrange(y,m)[1]:02}.{m:02}.{y}',
                f'Anfangsbestand: {money(opening)}. Endbestand: {money(balance)}.'],rows,
                'Die Buchungsreferenz bezeichnet den Umsatz im bereitgestellten Export. Die Anzeige von Karte oder Terminal ist keine Identitätsbestätigung der Person, die eine Karte tatsächlich verwendet hat. Bitte prüfen Sie diesen Auszug und teilen Sie uns konkrete Unstimmigkeiten mit.')
        assert balance==acc['closing_balance_cents']
    for inv in data['invoices']:
        seller=cmap[inv['seller']]; rows=[['Leistung','Gesamtpreis']]+[[name,money(value)] for name,value in inv['lines']]+[['Rechnungsbetrag',money(inv['total_cents'])]]
        assert sum(v for _,v in inv['lines'])==inv['total_cents']
        pdf(inv['source_file'],inv['subject'],[
            seller['name']+'\n'+seller['address']+'\n'+seller['email'] if inv['id']!='ZT-250508' else 'Technikladen Zinnober GmbH\nBildgasse 21, 13127 Berlin\nservice@zinnober-technik.example',
            'An Adelheid Pfister\nFliederbogen 17\n13125 Berlin' if inv['id']!='W-24051' else 'An Ruprecht Pfister\nKastanienwinkel 6\n16321 Bernau',
            'Belegnummer '+inv['id']+' | Belegdatum '+dt.date.fromisoformat(inv['date']).strftime('%d.%m.%Y'),
            inv['note']],rows,'Bitte geben Sie bei Rückfragen die Belegnummer an. Diese Rechnung dokumentiert die abgerechnete Leistung; einen etwaigen Zahlungsnachweis finden Sie im Kontoauszug. Eine bereits erfolgte Kartenzahlung oder Überweisung wird nicht erneut angefordert.')
    # Rechnungskorrekturen und Abrechnungen werden als Originalschreiben geliefert.
    for year,cons,paid,net in [(2023,78000,86400,-8400),(2024,83200,86400,-3200),(2025,104100,94800,9300)]:
        pdf(f'03_Belege/NE-{year}.pdf','Strom Jahresabrechnung '+str(year),[
          'Nordlicht Energie Berlin GmbH | Stromgasse 14, 10589 Berlin\nservice@nordlicht-energie.example',
          'Adelheid Pfister, Fliederbogen 17, 13125 Berlin\nKundennummer NE-48017 | Zähler NL-88144',
          f'Wir rechnen die Stromlieferung vom 01.01.{year} bis 31.12.{year} ab. Die angeführten Abschläge gehören zum gesamten Lieferjahr. Der Saldo wird unabhängig von den laufenden Abschlägen ausgeglichen. Bitte vergleichen Sie die Werte mit Ihren Unterlagen.'],
          [['Abrechnungsbestandteil','Betrag'],['Verbrauch und Grundpreis einschließlich Umsatzsteuer',money(cons)],['Verrechnete Abschläge',money(paid)],['Nachzahlung' if net>0 else 'Guthaben',money(abs(net))]],
          f'Den Betrag von {money(abs(net))} '+('ziehen wir am 12.03.2026 ein.' if year==2025 else f'überweisen wir am {"12.03.2024" if year==2023 else "11.03.2025"}.')+' Eine Verrechnung mit dem nächsten laufenden Abschlag erfolgt nicht.')
    for year,paid,cost,remaining in [(2023,240000,272000,32000),(2024,240000,281000,41000)]:
        pdf(f'03_Belege/HV-{str(year)[2:]}.pdf','Betriebskostenabrechnung '+str(year),[
          'Hausverwaltung Lindenblatt KG | Mauerseglerweg 7, 13189 Berlin\nverwaltung@lindenblatt.example',
          f'Adelheid Pfister | Fliederbogen 17, Wohnung 2 | Mietkonto LB-1702\nAbrechnungszeitraum 01.01.{year} bis 31.12.{year}',
          'Die Abrechnung betrifft die von Ihnen bewohnte Mietwohnung. Die anteiligen Betriebskosten werden mit den im gesamten Kalenderjahr geleisteten Vorauszahlungen verrechnet. Die Grundmiete ist darin nicht enthalten.'],
          [['Position','Ihr Anteil'],['Heizung und Warmwasser',money(162000 if year==2023 else 168000)],['Wasser und Abwasser',money(43000)],['Hausreinigung und Müll',money(47000 if year==2023 else 50000)],['Sonstige vereinbarte Betriebskosten',money(20000)],['Summe Kosten',money(cost)],['Abzüglich Vorauszahlungen',money(paid)],['Nachzahlung',money(remaining)]],
          'Die zugrunde liegenden Belege können nach Vereinbarung in unserem Büro eingesehen werden. Die Nachzahlung wird am '+('12.12.2024' if year==2023 else '11.12.2025')+' eingezogen. '+('Ab 01.01.2025 beträgt die monatliche Gesamtmiete 820,00 EUR.' if year==2023 else 'Die monatliche Gesamtmiete bleibt bei 820,00 EUR.'))
    pdf('01_Uebernahme/2026-10-01_Bestellungsmitteilung.pdf','Betreuung Adelheid Pfister',[
      'Amtsgericht Pankow | Betreuungsgericht\nGeschäftszeichen 17 XVII 184/26\nMitteilung an Frau Dr. Maja Winterfeld vom 01.10.2026',
      'Für Frau Adelheid Pfister, geboren am 14.02.1948, wohnhaft Fliederbogen 17, 13125 Berlin, wurde Frau Dr. Maja Winterfeld mit Wirkung vom 01.10.2026 zur beruflichen Betreuerin bestellt.',
      'Die Aufgabenbereiche umfassen Vermögenssorge, Wohnungsangelegenheiten sowie die Vertretung gegenüber Sozialleistungsträgern und Versicherungen. Ein Einwilligungsvorbehalt wurde nicht angeordnet. Die Bestellung umfasst keine pauschale Entscheidung über sämtliche persönlichen Angelegenheiten.',
      'Der gerichtlichen Bestellung ging eine persönliche Anhörung voraus. Frau Pfister hat Unterstützung bei der Sichtung ihrer finanziellen Unterlagen gewünscht. Sie hat erklärt, dass sie ihre alltäglichen Einkäufe und die Auswahl ihrer Freizeitangebote weiterhin selbst bestimmen möchte.',
      'Bitte nehmen Sie die Vermögensangelegenheiten auf und berichten Sie über den Anfangsbestand zum Übernahmezeitpunkt. Die Prüfung früherer Zahlungen dient zunächst der Bestandsaufnahme. Eine Entscheidung über streitige Rückforderungsansprüche ist mit der Bestellung nicht verbunden.',
      'Für Rückfragen verwenden Sie das Geschäftszeichen. Die Ausfertigung des Betreuerausweises wurde Frau Dr. Winterfeld gesondert ausgehändigt.'])
    docs=[
      ('01_Uebernahme/2026-10-02_Gespraech_Adelheid.docx','Gespräch mit Adelheid Pfister',[
        'Dr. Maja Winterfeld | Gespräch in der Wohnung Fliederbogen 17 am 02.10.2026, 10:00 bis 11:05 Uhr. Frau Pfister war zunächst allein anwesend; Juna Özdemir-Pfister kam erst gegen Ende hinzu.',
        'Frau Pfister möchte wissen, wofür ihr Geld ausgegeben wurde. Sie hat zwei Kontoordner, eine Kiste mit Rechnungen und ihr Telefon gezeigt. Sie sagt, Zahlen am Bildschirm überforderten sie inzwischen. Sie kann benennen, wer ihr bei Einkäufen hilft, und unterscheidet die laufende Miete von den Zahlungen an ihren Sohn.',
        'SofaKino soll ausdrücklich bleiben. Sie sieht freitags alte Filme und möchte dabei keine fremde Entscheidung über ihren Geschmack. Auch das Futter für ihren Kater Mürbchen und die Haushaltshilfe Mohnblüte sind ihr wichtig. LebensKompass und Glücksfenster sagen ihr wenig; sie erinnert sich an einen kostenlosen Rentencheck und mehrere Telefonanrufe.',
        'Zu den Fenstern in Bernau sagt sie zunächst, sie habe Ruprecht helfen wollen. Auf Nachfrage erklärt sie, sie wisse nicht mehr, ob von Zurückzahlen die Rede gewesen sei. Die Transporterhilfe nennt sie dagegen geliehenes Geld. Bei Egons 2.200 Euro erinnert sie sich an ein Dankeschön, sagt aber später, so viel habe sie nicht gemeint. Eine abschließende Festlegung war im Gespräch nicht möglich.',
        'Frau Pfister möchte, dass Egon vorerst weiter dienstags einkauft, solange die Auslagen einzeln festgehalten werden. Sie möchte keine Anzeige allein aufgrund des ersten Gesprächs. Sie ist mit sachlichen schriftlichen Nachfragen einverstanden. Konkrete Vertragsbeendigungen sollen zuvor mit ihr besprochen werden.',
        'In der Porzellandose lagen Kassenzettel und Bargeld. Ein Bestand wurde an diesem Tag nicht gemeinsam gezählt. Rückschlüsse auf frühere Barbestände sind daraus nicht möglich. Für den 09.10.2026 wurde ein weiterer Besuch zur gemeinsamen Zählung und Sichtung der Geräte vereinbart.']),
      ('01_Uebernahme/2026-10-06_Uebergabeprotokoll.docx','Übergabe der Unterlagen',[
        'Dr. Maja Winterfeld und Juna Özdemir-Pfister | Betreuungsbüro Winterfeld, Bücherplatz 8, 13187 Berlin | 06.10.2026, 15:30 Uhr',
        'Juna übergibt einen blauen Ordner mit Giroauszügen, einen grünen Ordner mit Sparauszügen und eine Schuhschachtel mit Rechnungen und Notizen. Die Bank hat die für die Prüfung benötigten Auszüge inzwischen nochmals vollständig bereitgestellt. Mehrere Papierkopien tragen handschriftliche Kreuze; deren Urheber lässt sich nicht sicher bestimmen.',
        'Die Quittungen zu Drucker und Ersatzhandy befinden sich nicht in der Schachtel. Juna berichtet, Egon habe sie angekündigt. Ein Vertragsblatt zur monatlichen Hilfe liegt vor. Eine unterschriebene Vereinbarung zum Jahrespaket über 980 Euro wurde bei der Übergabe nicht gefunden.',
        'Juna übergibt außerdem vier Bildschirmabbildungen. Sie kann den ursprünglichen Bestellvorgang von LebensKompass nicht vollständig rekonstruieren. Der Chat-Ausschnitt zeigt eine Nachricht Egons; der vollständige Verlauf ist auf dem Telefon noch vorhanden und kann auf Nachfrage gesichert werden.',
        'Es werden keine Schlüssel, Bankkarten oder Zugangsdaten im Betreuungsbüro hinterlegt. Frau Pfister behält zunächst ihre Karte. Ob weitere Geräte angemeldet sind, ist durch die Bank beziehungsweise die jeweiligen Anbieter zu klären. Das Protokoll bestätigt die Übergabe, nicht die Richtigkeit aller darin enthaltenen Behauptungen.']),
      ('04_Schriftverkehr/2024-09-02_Abrede_Nachbarschaftshilfe.docx','Vereinbarung über Nachbarschaftshilfe',[
        'Adelheid Pfister, Fliederbogen 17, 13125 Berlin, und Egon Knusper, Laternenweg 3, 13125 Berlin, treffen am 02.09.2024 folgende Abrede.',
        '1 Leistungen',
        'Herr Knusper unterstützt Frau Pfister nach Absprache bei Einkaufsfahrten und bei der Bedienung von Telefon, Fernseher und Computer. Die Hilfe findet gewöhnlich dienstags statt. Herr Knusper übernimmt damit keine gerichtliche Betreuung und entscheidet nicht anstelle von Frau Pfister über ihre persönlichen Angelegenheiten.',
        '2 Vergütung und Auslagen',
        'Frau Pfister zahlt monatlich 145,00 EUR. Darin enthalten sind die vereinbarten Fahrten und die laufende technische Hilfe. Waren, die Herr Knusper für Frau Pfister einkauft, werden gegen Beleg zusätzlich erstattet. Ein Vorschuss wird mit dem Einkauf abgerechnet; übriges Geld wird zurückgegeben.',
        '3 Weitere Aufträge',
        'Über größere Anschaffungen und zusätzliche Aufgaben sprechen die Beteiligten vorher. Ein Jahrespaket und die Entgegennahme von Geschenken werden mit dieser Abrede nicht geregelt. Eine Vollmacht für Bankgeschäfte wird hiermit nicht erteilt.',
        '4 Beendigung',
        'Jede Seite kann die Hilfe zum Ende des laufenden Monats beenden. Offene Auslagen werden danach gegen Beleg abgerechnet. Frau Pfister erhält ihre Unterlagen und gegebenenfalls ausgehändigte Geräte zurück.',
        'Auf der Papierfassung stehen die Namen Adelheid Pfister und Egon Knusper unter dem Text. Die hier übergebene Büroabschrift enthält keine Unterschriftsbilder.']),
      ('04_Schriftverkehr/2026-10-03_Bankanschreiben.docx','Unterlagen zur Vermögensaufnahme',[
        'Dr. Maja Winterfeld\nBetreuungsbüro Winterfeld\nBücherplatz 8\n13187 Berlin\nmaja.winterfeld@betreuungsbuero.example',
        'Fensterbank Spree eG\nKontenservice\nUferbogen 12\n10179 Berlin\nBerlin, 03.10.2026',
        'Sehr geehrte Damen und Herren,',
        'ich ergänze meine E-Mail vom 02.10.2026. Bitte senden Sie mir zu Frau Adelheid Pfister die monatlichen Kontoauszüge für Giro- und Sparkonto vom 01.10.2023 bis 30.09.2026 sowie einen maschinenlesbaren Buchungsexport. Der gerichtlich festgelegte Aufgabenbereich Vermögenssorge ist der bereits übersandten Bestellungsmitteilung zu entnehmen.',
        'Bitte teilen Sie außerdem mit, welche Karten ausgegeben wurden, ob Vollmachten für Dritte bestehen und welche Anschrift für Mitteilungen hinterlegt ist. Ich bitte um eine gesonderte Darstellung offener Entgelte und vorgemerkter Umsätze zum 30.09.2026, damit ich diese von gebuchten Bewegungen unterscheiden kann.',
        'Die Anfrage ist noch keine Beanstandung sämtlicher Abbuchungen und keine Anweisung, laufende Zahlungen einzustellen. Zu einzelnen Vorgängen werde ich nach der Auswertung gezielt nachfragen. Bitte antworten Sie an mein oben genanntes Büro.',
        'Mit freundlichen Grüßen\nDr. Maja Winterfeld\nBerufliche Betreuerin']),
      ('04_Schriftverkehr/2026-10-04_Ruprecht_Stellungnahme.docx','Angaben zu den Zahlungen meiner Mutter',[
        'Ruprecht Pfister\nKastanienwinkel 6\n16321 Bernau\nAn Frau Dr. Maja Winterfeld\nBücherplatz 8\n13187 Berlin\nBernau, 04.10.2026',
        'Sehr geehrte Frau Dr. Winterfeld,',
        'ich möchte Ihnen meine Sicht auf die Zahlungen meiner Mutter mitteilen. Die 4.200 Euro aus Mai 2024 bezogen sich auf die Fenster an meinem Haus. Die Rechnung über 3.600 Euro habe ich Ihnen über Juna überlassen. Die restlichen 600 Euro habe ich zurücküberwiesen. Ich ging davon aus, dass Mutter die Reparatur schenkt. Eine schriftliche Schenkungsvereinbarung haben wir nicht gemacht.',
        'Die 1.200 Euro vom Oktober 2024 waren ein Darlehen für meinen Transporter. Davon habe ich im Januar 2026 300 Euro zurückgezahlt. Die neue Überweisung von 1.200 Euro aus Mai 2026 sollte mir erneut über einen Engpass helfen. Ob und wann ich diesen zweiten Betrag zurückzahlen sollte, haben wir nicht festgelegt. Ich bin bereit, das mit meiner Mutter und Ihnen zu besprechen.',
        'Meine Mutter hat selbst Zugang zu ihrem Konto. Ich besitze weder ihre Karte noch eine Bankvollmacht. Von den zusätzlichen Barabhebungen weiß ich nichts. Ich kann bis zum 20.10.2026 meine eigenen Kontoauszüge zu den genannten Vorgängen zusammenstellen; andere private Umsätze würde ich dabei abdecken.',
        'Mit freundlichen Grüßen\nRuprecht Pfister']),
      ('04_Schriftverkehr/2024-06-11_Notiz_Fenster.docx','Notiz nach dem Familienkaffee',[
        'Juna Özdemir-Pfister | notiert am 11.06.2024 nach dem Besuch bei Tante Adelheid am 09.06.2024',
        'Adelheid sagte, Ruprecht habe das restliche Geld von den Fenstern zurückgeschickt. Ich fragte, ob die 3.600 Euro auch zurückkommen. Sie sagte zuerst: Das sehen wir, wenn es ihm wieder besser geht. Später sagte sie: Für die Enkel tut man eben etwas. Ich habe daraus keine eindeutige Antwort bekommen.',
        'Ruprecht war bei diesem Gespräch nicht im Zimmer. Egon brachte später die Einkäufe, hat unsere Unterhaltung nach meiner Erinnerung aber nicht gehört. Ich schreibe das auf, weil ich nicht in zwei Jahren behaupten möchte, es sicher zu wissen. Die Notiz gibt meine Erinnerung wieder; sie ist keine Erklärung meiner Tante.']),
      ('01_Uebernahme/2026-10-07_Geraete_und_Unterlagen.docx','Geräte und weitere Unterlagen',[
        'Dr. Maja Winterfeld | Zwischenstand nach Telefonaten vom 07.10.2026',
        'Nach Frau Pfisters Angaben steht das Tablet mit der Serienendung 7K31 auf dem Sideboard. Eine eigene Besichtigung steht noch aus. Der Kaufbeleg über 799 Euro liegt in Kopie vor. Ein Drucker wird in der Wohnung benutzt; Kaufpreis und Herkunft sind noch nicht mit einer Quittung belegt.',
        'Herr Knusper bestätigt, dass das im April bezahlte Ersatzhandy noch bei ihm liegt. Er nennt als Grund die nicht abgeschlossene Datenübertragung. Frau Pfister benutzt weiter ihr altes Gerät mit beschädigtem Glas. Sie wünscht, das neue Telefon zu erhalten, möchte die Kontakte aber nicht verlieren.',
        'Das Einkaufsheft wurde bei der Ordnerübergabe nicht vorgelegt. Herr Knusper will in seinem Auto nachsehen. Die Bank hat mitgeteilt, dass für ihn keine Bankvollmacht hinterlegt ist. Daraus ergibt sich noch nicht, ob eine private Vollmacht bestand oder wer bestimmte Zahlungen tatsächlich veranlasst hat.',
        'Am 09.10.2026 sollen die Geräte und vorhandenen Kassenbestände gemeinsam mit Frau Pfister aufgenommen werden. Dies ist ein künftiger Termin; ein Ergebnis liegt zum Bearbeitungsstand 08.10.2026 nicht vor.']),
      ('01_Uebernahme/2026-10-08_Arbeitsauftrag.docx','Auftrag zur Sichtung der Finanzunterlagen',[
        'Dr. Maja Winterfeld | Betreuungsbüro Winterfeld | Bearbeitungsstand 08.10.2026',
        'Bitte untersuchen Sie die Unterlagen für den Zeitraum vom 01.10.2023 bis 30.09.2026. Erstellen Sie eine nachvollziehbare Übersicht der tatsächlichen Einnahmen und Ausgaben sowie eine Überleitung von den Anfangsbeständen zu den Endbeständen beider Konten. Überträge zwischen eigenen Konten dürfen das wirtschaftliche Ergebnis nicht erhöhen oder mindern.',
        'Ordnen Sie jeder Aussage die zugrunde liegende Buchung und, soweit vorhanden, einen Beleg zu. Erfassen Sie Erstattungen, Bargeldabhebungen, Darlehen und mögliche Schenkungen gesondert. Eine Abhebung allein belegt keine bestimmte spätere Verwendung des Geldes. Ermitteln Sie, welche Unterlagen noch fehlen und welche Widersprüche vor einer weiteren Bewertung geklärt werden müssen.',
        'Bereiten Sie eine verständliche Excel-Auswertung und ausformulierte Anschreiben an die jeweils zuständigen Personen oder Unternehmen vor. Die Anschreiben sollen konkrete Beträge, Zeiträume und vorhandene Belege nennen. Prüfen Sie für jedes weitere Vorgehen, welche Erklärung rechtlich und nach dem Wunsch Frau Pfisters passt. Ein pauschales Beenden aller Verträge oder eine strafrechtliche Beschuldigung ist nicht beauftragt.',
        'Die Auswertung soll eine Entscheidung ermöglichen, aber keine ungeprüften Tatsachen als bewiesen behandeln. Schreiben werden zunächst als Entwürfe vorgelegt. Ich entscheide nach dem Gespräch mit Frau Pfister über den Versand und weitere Maßnahmen.']),
    ]
    for rel,heading,paras in docs:word(rel,heading,paras)
    # Bildschirmabbildungen als gerenderte Dokumente, keine echten Anbieteroberflächen.
    screens=[
      ('01_LebensKompass_Bestellseite','lebenskompass.example/rentencheck','03.01.2025 18:41',[
        'LebensKompass | Informationen für Ihren Alltag','Rentencheck starten','Kontakt: egon@knusper-hilfe.example','Name: Adelheid Pfister','Digitalpaket: Ratgeber und telefonische Information','Monatlicher Paketpreis: 69,90 EUR','[x] Ich wünsche den Zugang zum Digitalpaket.','Weiter zu meinen Informationen','Kontakt | Datenschutz | Allgemeine Geschäftsbedingungen']),
      ('02_Chat_Karte_Juni','Nachrichten | Juna und Egon','18.06.2026 19:12',[
        '16.06.2026 08:10 | Egon','Bin heute bis mittags in Potsdam, danach Einkauf.','18.06.2026 18:42 | Juna','Tante weiß nichts von den zusätzlichen 650 Euro.','18.06.2026 18:57 | Egon','Die Karte lag nach dem Markt wieder in der Küchenschublade.','18.06.2026 19:02 | Juna','An welchem Tag? Bitte bring das Heft mit.','18.06.2026 19:09 | Egon','Muss in den Kalender schauen.']),
      ('03_SofaKino_Konto','sofakino.example/konto','02.10.2026 10:34',[
        'SofaKino | Mein Abonnement','Kundennummer SK-77380','Adelheid Pfister','Monatspaket 12,99 EUR','Zusatzpakete: keine','Letzte Wiedergabe: Freitag 25.09.2026','Profil: Adelheid und Mürbchen','Nächste Abbuchung: 22.10.2026','Abonnement verwalten']),
      ('04_LebensKompass_Kontakt','lebenskompass.example/kundenbereich','06.10.2026 17:02',[
        'LebensKompass | Persönliche Daten','Kundennummer LK-55771','Vertragsname: Adelheid Pfister','E-Mail: egon@knusper-hilfe.example','Postanschrift: Fliederbogen 17, 13125 Berlin','Kontoauskünfte: Anmeldung erforderlich','Ihre Nachricht vom 07.11.2025','Doppelabbuchung wurde erstattet.','Bestelldokumente: derzeit nicht abrufbar']),
    ]
    import fitz
    screen_tmp=Path(tempfile.gettempdir())/'betreuung-pfister-screens';screen_tmp.mkdir(parents=True,exist_ok=True)
    for stem,url,when,lines in screens:
        pp=screen_tmp/(stem+'.pdf');c=canvas.Canvas(str(pp),pagesize=(420,650))
        c.setFillColor(colors.HexColor('#edf1f3'));c.rect(0,0,420,650,fill=1,stroke=0)
        c.setFillColor(colors.HexColor('#273b4d'));c.rect(0,592,420,58,fill=1,stroke=0);c.setFillColor(colors.white);c.setFont('Helvetica',10);c.drawString(20,630,when);c.drawString(20,608,url)
        y=565
        for i,line in enumerate(lines):
            st=ParagraphStyle('Screenshot',fontName='CaseSerifBold' if i==0 else 'CaseSerif',fontSize=14 if i==0 else 12,leading=17,textColor=colors.HexColor('#172c3b'))
            p=Paragraph(escape(line),st);w,h=p.wrap(370,600);p.drawOn(c,24,y-h);y-=h+20
        c.save();d=fitz.open(pp);d[0].get_pixmap(matrix=fitz.Matrix(2,2)).save(CASE/'05_Bildschirmfotos'/(stem+'.png'));d.close();artifacts.append('05_Bildschirmfotos/'+stem+'.png')
    missing=[]
    for n,(date,fr,to,subject,body,attachment) in enumerate(correspondence(),1):
        msg=EmailMessage(policy=SMTP);a,b=cmap[fr],cmap[to]
        msg['From']=f'{a["name"]} <{a["email"]}>';msg['To']=f'{b["name"]} <{b["email"]}>';msg['Subject']=subject
        msg['Date']=format_datetime(dt.datetime.fromisoformat(date+'T'+f'{8+n%10:02}:15:00').replace(tzinfo=ZoneInfo('Europe/Berlin')))
        msg['Message-ID']=f'<pfister-{date}-{n:02}@{a["email"].split("@")[1]}>'
        msg.set_content(body+'\n\n'+a['name']+'\n'+a['address']+'\n'+a['email'])
        if attachment:
            path=CASE/attachment
            if path.exists():
                mime=mimetypes.guess_type(path.name)[0] or 'application/octet-stream';major,minor=mime.split('/',1)
                msg.add_attachment(path.read_bytes(),maintype=major,subtype=minor,filename=path.name)
            else:missing.append(attachment)
        rel=f'07_E-Mails/{n:02}_{date}_{fr}-an-{to}.eml';(CASE/rel).write_bytes(msg.as_bytes());artifacts.append(rel)
    # Prüfdaten stehen ausdrücklich außerhalb der Testakte.
    outside=[t for t in data['transactions'] if not t.get('transfer_id')]
    controls=dict(transaction_count=len(data['transactions']),opening_cents=sum(a['opening_cents'] for a in data['accounts']),closing_cents=sum(a['closing_balance_cents'] for a in data['accounts']),external_in_cents=sum(t['amount_cents'] for t in outside if t['amount_cents']>0),external_out_cents=-sum(t['amount_cents'] for t in outside if t['amount_cents']<0),internal_transfer_entries=sum(bool(t.get('transfer_id')) for t in data['transactions']),accounts=data['accounts'],monthly=[],missing_attachments=missing,original_files=len(artifacts))
    for i in range(36):
        y,m=2023+(9+i)//12,(9+i)%12+1;ym=f'{y}-{m:02}';ts=[t for t in outside if t['date'].startswith(ym)]
        controls['monthly'].append(dict(month=ym,in_cents=sum(t['amount_cents'] for t in ts if t['amount_cents']>0),out_cents=-sum(t['amount_cents'] for t in ts if t['amount_cents']<0)))
    assert controls['opening_cents']+controls['external_in_cents']-controls['external_out_cents']==controls['closing_cents']
    (ROOT/'quality/betreuungsrecht/pfister-kontrollwerte.json').write_text(json.dumps(controls,ensure_ascii=False,indent=2)+'\n')
    (CASE/'README.md').write_text('# Testakte Adelheid Pfister\n\n## 1. Auftrag und Bearbeitungsstand\n\nDr. Maja Winterfeld hat am 01.10.2026 die berufliche Betreuung von Adelheid Pfister übernommen. Bearbeitungsstand ist der 08.10.2026. Die Akte enthält drei vollständige Jahre von Kontobewegungen vom 01.10.2023 bis 30.09.2026 und die dazu vorhandenen, unterschiedlich vollständigen Belege.\n\nUntersuchen Sie Einnahmen und Ausgaben, saldieren Sie Giro- und Sparkonto und erstellen Sie eine nachvollziehbare Excel-Auswertung. Ordnen Sie Zahlungen und Belege zu, unterscheiden Sie Kontobewegung und wirtschaftlichen Vorgang und bereiten Sie konkrete Rückfragen und ausformulierte Schreiben vor. Die Wünsche von Frau Pfister, die Grenzen des Aufgabenkreises und noch ungeklärte Tatsachen gehören in die weitere Bearbeitung. Die Akte enthält keine Musterlösung.\n\n## 2. Material\n\n72 monatliche Kontoauszüge bilden beide Konten ohne Monatslücken ab. 584 Buchungen, Rechnungen, Abrechnungen, 32 E-Mails mit ausgewählten Originalanhängen, Word-Schriftverkehr und vier Bildschirmabbildungen ergeben eine zusammenhängende Übernahmeakte. Die Excel-Dateien liegen unter `06_Tabellen`. Wiederkehrende Zahlungen werden durch konkrete Belege ergänzt; bewusst nicht jede Barausgabe ist quittiert. Verwandtenzahlungen, Geräteanschaffungen, Hilfsleistungen und laufende Verträge müssen im Zusammenhang gelesen werden.\n\nDie Monatsauszüge sind die bankseitige Kontenquelle; ein in einer E-Mail erneut beigefügter Beleg ist keine zweite Zahlung. Dateinamen und Buchungsreferenzen erlauben das Wiederauffinden. Abbildungen halten nur den sichtbaren Ausschnitt fest.\n\n## 3. Fiktion und Kontakte\n\nAlle Personen, Unternehmen, Adressen, Kontoreferenzen und Vorgänge dieser Akte sind erfunden. Kontoreferenzen sind keine für Zahlungen verwendbaren IBANs. Bildschirmabbildungen zeigen erfundene Anwendungen. Die reservierten `.example`-Adressen dienen ausschließlich der Akte und sind keine Versandziele.\n\n<!-- reserved-example-contacts -->\n\n## 4. Downloads\n\n'+WARN+'\n\n| Fassung | Download |\n| --- | --- |\n| Gesamt-PDF | [Vollständige Lesefassung](gesamt-pdf/betreuung-adelheid-pfister-dreijahresabrechnung_gesamt.pdf) |\n| Originaldateien | [Akten-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/betreuungsrecht-v445.33.3/testakte-betreuung-adelheid-pfister-dreijahresabrechnung.zip) |\n| Einzel-PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/betreuungsrecht-v445.33.3/testakte-betreuung-adelheid-pfister-dreijahresabrechnung-einzelpdfs.zip) |\n')
    print(json.dumps(dict(files=len(artifacts),missing_attachments=missing,controls=controls['closing_cents']),ensure_ascii=False))

def main():
    p=argparse.ArgumentParser();p.add_argument('--data-only',action='store_true');args=p.parse_args()
    data=canonical();DATA.parent.mkdir(parents=True,exist_ok=True);DATA.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    if args.data_only: print(f'{len(data["transactions"])} Buchungen; {len(data["invoices"])} Rechnungen; {DATA}');return
    build(data)
    subprocess.run([sys.executable, str(ROOT/'scripts/inject-gesamt-pdf-section.py'), CASE.name], check=True)

if __name__ == '__main__': main()
