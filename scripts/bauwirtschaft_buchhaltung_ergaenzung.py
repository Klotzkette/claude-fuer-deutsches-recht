"""Zusätzlicher, separat abgegrenzter Belegstapel Bad Salzuflen. Autor: Klotzkette."""
from datetime import date, timedelta
from decimal import Decimal


def model():
    # Nr, Beleg, Kreditor, Firma, Projekt, Konto, Menge, Einheit, Einzelpreis, Leistung, RC
    raw = [
        (31,'ST-260902','51001','Steinwerk Leopoldshöhe GmbH','BS26-01','5000',600,'Stück',3,'Kalksandsteine 2 DF, Lieferung ohne Einbau',False),
        (32,'HB-260903','51002','Holzhandel Bega GmbH','BS26-01','5000',80,'m²',30,'Schalungsplatten, Lieferung ohne Montage',False),
        (33,'EL-260904','51003','Elektrohandel Werre GmbH','BS26-02','5000',250,'Meter',3,'Installationsleitung NYM, reine Warenlieferung',False),
        (34,'TB-260905','51004','Trockenbau Vogt GmbH','BS26-01','5010',120,'m²',40,'Fest eingebaute Gipskartonwände, einschließlich Unterkonstruktion',True),
        (35,'SA-260906','51005','Sanitär Ahle GmbH','BS26-02','5010',40,'Stunden',80,'Einbau der Trinkwasserleitungen einschließlich Material',True),
        (36,'MR-260907','51006','Mietpark Rethmar GmbH','BS26-01','5020',6,'Tage',150,'Minibagger ohne Bedienpersonal, 1. bis 6. September',False),
        (37,'GE-260908','51007','Gerüstvermietung Exter GmbH','BS26-01','5020',20,'Tage',55,'Gerüstteile ohne Auf- oder Abbau, 19. August bis 7. September',False),
        (38,'EN-260909','51008','Entsorgung Kalletal GmbH','BS26-02','5030',4,'Tonnen',120,'Abtransport und Entsorgung mineralischen Bauschutts, keine Abbrucharbeiten',False),
        (39,'TP-260910','51009','Planungsbüro Retzer GmbH','BS26-02','5040',15,'Stunden',80,'Ausführungsplanung der Eingangstreppe, keine Bauausführung',False),
        (40,'ST-260911','51001','Steinwerk Leopoldshöhe GmbH','BS26-01','5000',30,'Sack',20,'Dünnbettmörtel, Lieferung ohne Verarbeitung',False),
        (41,'TR-260912','51010','Transport Lemgo GmbH','BS26-01','5050',6,'Stunden',70,'Baustellenanlieferung von Werkzeugen, reine Transportleistung',False),
        (42,'VW-260913','51011','Vermessung Werretal GmbH','BS26-02','5060',10,'Stunden',95,'Aufmaß und Bestandsplan der Ladenfläche, keine Bauausführung',False),
        (43,'MT-260914','51012','Miettechnik Ravensberg GmbH','BS26-02','5020',4,'Tage',60,'Bautrockner ohne Bedienpersonal, 10. bis 13. September',False),
        (44,'DZ-260915','51013','Dachbaustoffe Zander GmbH','BS26-01','5000',330,'Stück',3,'Dachziegel einschließlich Anlieferung, ohne Verlegung',False),
    ]
    invoices=[]
    supplier_numbers={}
    for number,identifier,creditor,supplier,project,account,quantity,unit,price,service,rc in raw:
        supplier_number=supplier_numbers.setdefault(creditor,number)
        net=Decimal(quantity)*Decimal(price)
        tax=Decimal(0) if rc else net*Decimal('.19')
        issued=date(2026,9,number-29)
        invoices.append(dict(number=number,id=identifier,creditor=creditor,supplier=supplier,project=project,
                             account=account,quantity=quantity,unit=unit,price=price,service=service,
                             rc=rc,net=float(net),tax=float(tax),gross=float(net+tax),
                             date=issued.isoformat(),due=(issued+timedelta(days=14)).isoformat(),
                             address=f'Gewerbestraße {supplier_number}, 32105 Bad Salzuflen',
                             tax_number=f'313/5700/{supplier_number}10',
                             file=f'{number:02d}_Rechnung_{identifier.replace("-","_")}.pdf'))
    credits=[dict(number=45,id='HB-G260916',invoice='HB-260903',net=-200,tax=-38,gross=-238,date='2026-09-16',reason='Rücknahme beschädigter Schalungsplatten nach gemeinsam bestätigter Bewertung'),
             dict(number=46,id='VW-G260919',invoice='VW-260913',net=-50,tax=-9.5,gross=-59.5,date='2026-09-19',reason='Vereinbarter Nachlass wegen einer doppelt angesetzten Anfahrt')]
    by_id={i['id']:i for i in invoices}
    for c in credits:
        i=by_id[c['invoice']]
        c.update(creditor=i['creditor'],supplier=i['supplier'],project=i['project'],account=i['account'],rc=False,
                 file=f'{c["number"]:02d}_Rechnungskorrektur_{c["id"].replace("-","_")}.pdf')
    allocations=[['EB-0916A','2026-09-16','ST-260902',2142],['EB-0916A','2026-09-16','ST-260911',714],
                 ['EB-0917','2026-09-17','HB-260903',2618],['EB-0918A','2026-09-18','EL-260904',892.5],
                 ['EB-0918B','2026-09-18','MR-260907',500],['EB-0921A','2026-09-21','GE-260908',1309],
                 ['EB-0921B','2026-09-21','EN-260909',571.2],['EB-0922','2026-09-22','TR-260912',499.8],
                 ['EB-0923','2026-09-23','VW-260913',1071],['EB-0924','2026-09-24','MT-260914',285.6],
                 ['EB-0925','2026-09-25','DZ-260915',1178.1]]
    bank=[]
    for reference,day,identifier,paid in allocations:
        existing=next((r for r in bank if r['reference']==reference),None)
        if existing:
            existing['amount']=round(existing['amount']+paid,2);existing['invoices'].append(identifier)
        else:bank.append(dict(reference=reference,date=day,supplier=by_id[identifier]['supplier'],amount=paid,invoices=[identifier]))
    for i in invoices:
        i['credit']=round(-sum(c['gross'] for c in credits if c['invoice']==i['id']),2)
        i['paid']=round(sum(r[3] for r in allocations if r[2]==i['id']),2)
        i['open']=round(i['gross']-i['credit']-i['paid'],2)
        i['status']='Bauabzug prüfen' if i['rc'] else ('Leistungsfreigabe fehlt' if i['id']=='TP-260910' else ('Restzahlung offen' if i['open'] else 'ausgeglichen'))
    # Jede vorgeschlagene Buchung ist ein ausgeglichener Satz mit expliziten Steuerzeilen.
    ledger=[]
    def line(batch,day,identifier,account,debit,credit,key,project):
        ledger.append([batch,day,identifier,account,round(debit,2),round(credit,2),key,project])
    for i in invoices+credits:
        key='RC19' if i['rc'] else 'V19'
        net,tax,gross=i['net'],i['tax'],i['gross']
        if net>=0:
            line(i['id'],i['date'],i['id'],i['account'],net,0,key,i['project'])
            if tax:line(i['id'],i['date'],i['id'],'1400',tax,0,key,i['project'])
            line(i['id'],i['date'],i['id'],i['creditor'],0,gross,key,i['project'])
        else:
            line(i['id'],i['date'],i['id'],i['creditor'],-gross,0,key,i['project'])
            line(i['id'],i['date'],i['id'],i['account'],0,-net,key,i['project'])
            line(i['id'],i['date'],i['id'],'1400',0,-tax,key,i['project'])
        if i['rc']:
            line(i['id'],i['date'],i['id'],'1401',net*.19,0,key,i['project'])
            line(i['id'],i['date'],i['id'],'1771',0,net*.19,key,i['project'])
    for reference,day,identifier,paid in allocations:
        i=by_id[identifier]
        line(reference,day,identifier,i['creditor'],paid,0,'OHNE',i['project'])
        line(reference,day,identifier,'1201',0,paid,'OHNE',i['project'])
    return dict(invoices=invoices,credits=credits,allocations=allocations,bank=bank,ledger=ledger,opening=50000)


def build(api):
    data=model();c=api.BAD;owner=api.B_OWNER
    for i in data['invoices']:
        issuer=i['supplier']+'\n'+i['address']+'\nSteuernummer '+i['tax_number']
        tax=('Steuerschuldnerschaft des Leistungsempfängers nach Paragraf 13b Absatz 2 Nummer 4 und Absatz 5 UStG. Die Rechnung enthält keinen gesonderten Umsatzsteuerausweis.' if i['rc'] else 'Die Rechnung enthält 19 Prozent Umsatzsteuer. Es wird ausschließlich die beschriebene Lieferung oder Dienstleistung berechnet.')
        body=f'''Wir berechnen für das Projekt {i['project']} die nachstehende Leistung. Leistungsdatum ist der {i['date']}; soweit die Leistungszeile einen Zeitraum nennt, ist dieser maßgeblich. Die projektbezogenen Liefer- und Leistungsnachweise sind im Einkauf hinterlegt. Die Übermittlung dieser Rechnung als PDF wurde mit Ihrer Buchhaltung vereinbart.

{tax}

Der Betrag ist bis {i['due']} ohne Skonto fällig. Bitte geben Sie {i['id']} bei der Überweisung auf das im Lieferantenstamm hinterlegte Konto an. Ein Sicherheitseinbehalt ist für diese Rechnung nicht vereinbart.'''
        api.pdf(c,i['file'],issuer,owner,'Rechnung '+i['id'],i['date'],body,
                [['Leistung','Menge','Preis netto EUR','Netto EUR'],[i['service'],f"{i['quantity']} {i['unit']}",api.euro(i['price']),api.euro(i['net'])],['Umsatzsteuer','','',api.euro(i['tax'])],['Rechnungsbetrag','','',api.euro(i['gross'])]])
    for credit in data['credits']:
        api.pdf(c,credit['file'],credit['supplier']+'\nDebitorenbuchhaltung',owner,'Rechnungskorrektur '+credit['id'],credit['date'],
                f"{credit['reason']}. Wir mindern unsere Rechnung {credit['invoice']} um {api.euro(-credit['net'])} EUR netto und {api.euro(-credit['tax'])} EUR Umsatzsteuer. Der Gesamtbetrag der Minderung beträgt {api.euro(-credit['gross'])} EUR.\n\nBitte verrechnen Sie die Korrektur einmalig mit dieser Rechnung. Es erfolgt keine gesonderte Auszahlung. Dies ist eine Rechnungskorrektur des Lieferanten und keine Abrechnung durch den Leistungsempfänger. Die Zahlungsfrist der ursprünglichen Rechnung bleibt unverändert; ein weiterer Nachlass wurde nicht vereinbart.")
    evidence=[]
    for i in data['invoices']:
        confirmation=('Der Eingang der Planfassung ist dokumentiert; die inhaltliche Prüfung durch Jan Hellwig steht noch aus.' if i['id']=='TP-260910' else 'Menge und beschriebene Lieferung oder Leistung durch die zuständige Bauleitung bestätigt.')
        evidence.append(f"{i['id']} | Projekt {i['project']} | {i['date']}\n{i['quantity']} {i['unit']}: {i['service']}. {confirmation}")
    api.pdf(c,'47_Liefer_und_Leistungsregister.pdf',owner,'Einkauf und Bauleitung','Lieferungen und Leistungen des Ergänzungsstapels','25. September 2026',
            'Auszug der projektbezogenen Eingangsnachweise. Zuständig sind Lea Tönnies für BS26-01 und Jan Hellwig für BS26-02. Die Angaben beziehen sich ausschließlich auf die Rechnungen in diesem Register.\n\n'+'\n\n'.join(evidence),keep_blocks=True)
    api.csvfile(c,'48_Projektkonto_Bank.csv',['Referenz','Valuta','Empfänger','Bezug','Soll_EUR'],[[r['reference'],r['date'],r['supplier'],' / '.join(r['invoices']),api.euro(r['amount'])] for r in data['bank']])
    closing=data['opening']-sum(r['amount'] for r in data['bank'])
    api.pdf(c,'49_Projektkonto_Kontoauszug.pdf','Lippische Gewerbebank eG\nProjektkonto 471109',owner,'Kontoauszug Projektkonto 471109','25. September 2026',
            f"Anfangsbestand am 1. September: {api.euro(data['opening'])} EUR. Dieser Auszug enthält sämtliche zehn Umsätze vom 1. bis 25. September. Das Projektkonto 471109 wird getrennt vom Betriebskonto 471108 geführt. Zwischen beiden Konten gab es in diesem Zeitraum keine Umbuchungen.\n\nSchlussbestand und verfügbares Guthaben: {api.euro(closing)} EUR. Buchungstag und Wertstellung stimmen überein. Es bestehen keine Vormerkungen. Die Rechnungsbezüge entsprechen den vom Auftraggeber angegebenen Verwendungszwecken.",
            [['Referenz','Valuta','Soll EUR']]+[[r['reference'],r['date'],api.euro(r['amount'])] for r in data['bank']])
    api.csvfile(c,'50_Ergaenzungsjournal.csv',['Beleg','Datum','Kreditor','Projekt','Netto_EUR','USt_EUR','Belegbetrag_EUR','Datei'],[[i['id'],i['date'],i['creditor'],i['project'],api.euro(i['net']),api.euro(i['tax']),api.euro(i['gross']),i['file']] for i in data['invoices']+data['credits']])
    api.csvfile(c,'51_Ergaenzungs_OPOS.csv',['Beleg','Kreditor','Fällig','Rechnung_EUR','Korrektur_EUR','Zahlung_EUR','Offen_EUR','Status'],[[i['id'],i['creditor'],i['due'],api.euro(i['gross']),api.euro(i['credit']),api.euro(i['paid']),api.euro(i['open']),i['status']] for i in data['invoices']])
    api.csvfile(c,'52_Buchungsvorschlaege.csv',['Satz','Datum','Beleg','Konto','Soll_EUR','Haben_EUR','Schlüssel','Projekt'],[[*r[:4],api.euro(r[4]),api.euro(r[5]),*r[6:]] for r in data['ledger']])
    accounts=[['1201','Projektkonto 471109'],['1400','Vorsteuer aus Rechnungen 19 Prozent'],['1401','Vorsteuer aus Bauleistungen nach Paragraf 13b'],['1771','Umsatzsteuer aus Bauleistungen nach Paragraf 13b'],['5000','Baumaterial'],['5010','Ausgeführte Baugewerke'],['5020','Geräte- und Gerüstmiete'],['5030','Entsorgung'],['5040','Planung'],['5050','Transport'],['5060','Vermessung']]
    accounts += [[i['creditor'],i['supplier']] for i in data['invoices'] if i['id']!='ST-260911']
    api.csvfile(c,'53_Kontenstamm.csv',['Konto','Bezeichnung'],accounts)
    api.doc(c,'54_Uebergabe_Ergaenzungsstapel.docx',owner,'Nora Brinkmann\nKaufmännische Leitung','Weiterer Belegstapel und Projektkonto','25. September 2026',
            '''1 Umfang und Kontoabgrenzung

Ergänzend zum zuerst übergebenen Stapel erhalten Sie 14 weitere Rechnungen und zwei Rechnungskorrekturen. Keine davon ist in den Dateien 01 bis 30 enthalten. Sie betreffen dieselben beiden Projekte, wurden aber über das getrennte Projektkonto 471109 abgewickelt. Die bisherigen Bankdaten und Kostenaufstellungen bleiben für ihren ausgewählten Stapel richtig. Der zusätzliche Kostenstand darf bei einer Zusammenführung einmal hinzugezählt werden; die Bankbestände sind nach Kontonummer getrennt zu führen.

2 Arbeitsstand der Buchhaltung

Das Eingangsjournal und die OPOS sind der Arbeitsstand des Büros. Datei 52 enthält noch nicht freigegebene Buchungsvorschläge, keine ausgeführten Hauptbuchbuchungen. Jeder Satz besteht aus mehreren Kontenzeilen mit Soll- und Habenbeträgen. Die Konten in Datei 53 und die Schlüssel V19, RC19 und OHNE sind unser fallinterner Übungsstamm; sie sind kein DATEV-Importformat und dürfen nicht ungeprüft in ein anderes System übertragen werden. Steuerbeträge stehen bereits auf eigenen Zeilen. Ein Import darf nicht zusätzlich automatische Steuerbuchungen erzeugen.

3 Zahlungsstand und offene Punkte

Steinwerk erhielt eine Sammelüberweisung für zwei Rechnungen. Die Zuordnung steht in Datei 57. Für den Minibagger wurden erst 500,00 EUR gezahlt; der Rest bleibt offen. Die beiden Rechnungskorrekturen mindern jeweils nur die zugehörige Rechnung. Bei Retzer fehlt die inhaltliche Freigabe der Planfassung. Trockenbau Vogt und Sanitär Ahle sind noch unbezahlt. Für diese beiden Lieferanten fehlen die Freistellungsbescheinigungen und Angaben zu weiteren Jahresleistungen. Vor einer Zahlung müssen Bauabzugsteuer und Zahlungsbetrag gesondert geklärt werden. Die vorhandene USt-1-TG-Bescheinigung von Mertens ersetzt diese Prüfung nicht.

4 Nächster Arbeitsauftrag

Bitte prüfen Sie die Rechnungserfassung gegen die Einzelbelege, stimmen Sie Buchungsvorschläge und OPOS mit dem Projektkonto ab und erstellen Sie die erforderlichen Rückfragen. Dokumentieren Sie bestätigte Änderungen im bestehenden Arbeitsstand mit Belegbezug. Die Buchungs- und Bankfreigabe bleibt bei Nora Brinkmann und Tobias Mertens. Die Excel-Datei enthält den bereits erfassten Arbeitsstand und darf zur Prüfung und Fortschreibung bearbeitet werden.

Tobias Mertens\nGeschäftsführer''')
    api.pdf(c,'56_Steuerliche_Bearbeitungsnotiz.pdf',owner,'Buchhaltungsbüro','Steuerannahmen des Ergänzungsstapels','25. September 2026',
            '''Die beiden Projekte werden ausschließlich für steuerpflichtige Ausgangsleistungen des Unternehmens bearbeitet. Private Verwendung und vorsteuerschädliche steuerfreie Verwendung liegen nach Auskunft der Geschäftsführung nicht vor. Die Lieferanten sind inländische regelbesteuerte Unternehmen. Die Unterlagen dieses Stapels betreffen bereits ausgeführte Leistungen; Anzahlungen sind nicht enthalten.

V19 bezeichnet den Vorschlag zur Erfassung der ausgewiesenen 19 Prozent Vorsteuer nach Paragraf 15 Absatz 1 Satz 1 Nummer 1 UStG. Die Voraussetzungen der ordnungsgemäßen Rechnung sind anhand des konkreten Belegs zu prüfen. RC19 bezeichnet die beiden ausgeführten Bauleistungen TB-260905 und SA-260906: Umsatzsteuer nach Paragraf 13b Absatz 2 Nummer 4 und Absatz 5 UStG und unter den genannten Verwendungsannahmen korrespondierende Vorsteuer nach Paragraf 15 Absatz 1 Satz 1 Nummer 4 UStG. Die in Datei 07 dokumentierte Empfängerbescheinigung lag bei Leistungsausführung vor. Die Steuer wird dem Lieferanten nicht überwiesen. OHNE kennzeichnet den Zahlungsausgleich ohne erneuten Vorsteuerabzug.

Die zwei Rechnungskorrekturen werden mit ihrer Nettominderung und ihrer Vorsteuerberichtigung berücksichtigt. Eine zusätzliche Auszahlung ist nicht vorgesehen. Die Berichtigung richtet sich nach Paragraf 17 Absatz 1 UStG. Fehlende interne Zahlungsfreigabe ist für sich genommen kein Beweis einer nicht ausgeführten Leistung.

Der Bauabzug nach Paragrafen 48 und 48b EStG ist vor Zahlungen an Trockenbau Vogt und Sanitär Ahle gesondert zu prüfen. Die bisherigen Rechnungsbeträge allein erlauben keine Aussage zur voraussichtlichen Jahressumme. Weder eine gültige Freistellung noch das Unterschreiten der Freigrenze ist im neuen Stapel nachgewiesen. Deshalb enthält der Arbeitsstand für diese Rechnungen noch keine Bankbuchung und keinen abschließend berechneten Auszahlungsbetrag.

Diese Arbeitsnotiz ersetzt keine Freigabe einer Steueranmeldung. Bearbeitung: Nora Brinkmann.''')
    api.csvfile(c,'57_Zahlungszuordnung.csv',['Bankreferenz','Valuta','Rechnung','Zugeordnet_EUR'],[[*r[:3],api.euro(r[3])] for r in data['allocations']])
    return data
