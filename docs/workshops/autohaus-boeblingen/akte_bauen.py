"""Baut die nativen Aktenstücke und die zwei getrennten Kontrollimporte."""
import csv
import json
from pathlib import Path
from datetime import date,timedelta
from falldaten import (FIRMA,HAUS,BANK,STICHTAG,AKTIVA,PASSIVA,KREDITOREN,DEBITOREN,AUTOS,VERKEHR,MONAT_EIN,MONAT_AUS,wochen)
from unterlagen import letter,word,mail,sheet,eur

HERE=Path(__file__).resolve().parent
CASE=HERE.parents[2]/'testakten'/'autohaus-boeblingen'
GF='Eva Mergenthal <e.mergenthal@schoenbuchring.example>'
FI='Jule Kopp <j.kopp@schoenbuchring.example>'
BERATUNG='Büro Nehring <mandate@nehring-beratung.example>'
ADRESSE=FIRMA+' · Frau Eva Mergenthal\n'+HAUS

def konten(g):
    balance=0
    for name,start,end,title in [('B01_Kontoauszug_September_I.pdf',0,8,'Kontoauszug 09/26 · Abschnitt 1'),('B02_Kontoauszug_September_II.pdf',8,13,'Kontoauszug 09/26 · Abschnitt 2')]:
        rows=[['Valuta','Buchungstext','Umsatz EUR','Saldo EUR']]
        if start:rows.append(['18.09.','Saldo aus Abschnitt 1','',eur(balance)])
        for dat,txt,amt in VERKEHR[start:end]:
            balance+=amt;rows.append([date.fromisoformat(dat).strftime('%d.%m.'),txt,eur(amt) if dat!='2026-08-31' else '',eur(balance)])
        letter(g/name,BANK,'Firmenkunden · Betriebskonto BB 4416',ADRESSE,'18.09.2026' if start==0 else '25.09.2026','BB 4416 / 09-26',title,[
            'Auszug des EUR-Geschäftskontos. Der laufende Saldo enthält sämtliche wertgestellten Buchungen des ausgewiesenen Zeitraums. Verfügungsvormerkungen und separierte Teilbeträge erscheinen in der Dispositionsansicht des Firmenportals.'],rows)
    assert balance==50000
    letter(g/'B03_Kassensturz.pdf',FIRMA,'Serviceannahme · Kasse S1', 'Zweitschrift für die Finanzbuchhaltung','25.09.2026','K-2517 / 17:05 Uhr','Tagesabschluss nach letzter Fahrzeugabholung',
      ['Zählung durch Derya Heller im Beisein von Linus Birken. Der Ersatzwagenschlüssel für Herrn Maier lag noch im Geldfach. Er ist im Schlüsselbuch übergeben. Die gezählten Gelder gehören dem Betrieb und sind nach Kassenschluss im Tresor verfügbar. Weitere Barkassen oder private Vorschüsse bestehen nicht.'],
      [['Nominal','Zusammen EUR'],['10 × 100 EUR','1.000,00'],['16 × 50 EUR','800,00'],['8 × 20 EUR','160,00'],['4 × 10 EUR','40,00'],['Kassenbuch S1 / letzter Bon 005731','2.000,00']])
    letter(g/'B04_Kreditbestaetigung.pdf','Kappelbrück Kreditbank AG','Firmenservice · unabhängige Betriebsmittelfinanzierung',ADRESSE,'24.09.2026','KK 870 / Bestätigung','Abruf für laufende Betriebsausgaben',
      ['Der am 1. Juli vereinbarte Betriebsmittelkredit über 8.000 Euro ist bisher unbeansprucht. Die vollständige Kreditprüfung ist abgeschlossen. Die Gesellschaft kann bis zum 31. Dezember 2026 per elektronischem Abruf ohne weitere Bedingungen am selben Bankarbeitstag über den Betrag verfügen. Das Abrufkonto weist am heutigen Abend einen Nullsaldo auf.',
       'Die Linie dient ausschließlich laufenden Aufwendungen. Unsere Bank führt weder Fahrzeugbriefe noch Sicherungsguthaben des Autohauses. Eine darüber hinausgehende Finanzierung ist durch diese Bestätigung nicht zugesagt.','Miriam Erath · Kreditservice'])
def finanzen(g,n):
    cols=['Pos.','Beleg','Geschäftspartner','Leistungsgrund','Fälligkeit','Brutto EUR','Unterlage']
    for name,title,data in [('O01_Lieferkonten.xlsx','Lieferanten und Mietverbindlichkeiten',KREDITOREN),('O02_Kundenkonten.xlsx','Kundenforderungen und offene Beträge',DEBITOREN)]:
        sheet(g/name,title,[('Posten','Export 25.09.2026, 17:40 Uhr · Buchungsgruppe 18. Der Betrag zeigt den offenen Rechnungssaldo vor einem eventuellen Ausgleich.',cols,[8,12,30,31,16,15,30],data)])
    rows=[['Referenz','Fälligkeit','Avisierter Betrag EUR']]
    rows.extend([[r[6]+' / '+r[1],r[4],eur(r[5])] for r in DEBITOREN[:-1]])
    letter(g/'O03_Zahlungsavis.pdf',FIRMA,'Debitorenteam · Freitagsablage','Jule Kopp · Kassenplanung','25.09.2026','DMS Export 906','Bestätigte Zahlungstermine der Kunden',
      ['Die Debitorenbuchhaltung hat die schriftlich bestätigten Werte aus den Rückläufen zum Kontenabgleich zusammengestellt. Alle sieben Leistungen sind abgenommen. Die Zahlungen gehen auf das Betriebskonto BB 4416, ohne Abtretung oder Ablöseauflage. Für die ältere Unfallsache liegt kein Zahlungstermin vor.'],rows)
    word(g/'O04_Abschlussnotiz.docx',FIRMA,'Finanzbuchhaltung','Buchungsschluss für den Termin bei Frau Nehring','Ablage FiBu 25.09.2026 · 18:15 Uhr',[
      ('1. Offener Zahlungslauf','Die zehn Posten der Lieferliste sind eingebucht, angefordert und vollständig offen. Bis heute hat kein Lieferant einem Zahlungsaufschub zugestimmt. Die Geschäftsleitung möchte die alten vier Positionen bei nächster Gelegenheit gemeinsam anweisen. Weitere fällige Altrechnungen oder gesperrte Zahlungsstapel bestehen laut Hauptbuch und dem heute durchgesehenen Postfach nicht.'),
      ('2. Laufende Aufwendungen','Löhne und Beitragsnachweis für September sind mit den Septemberabschlägen und der Schlusszahlung bedient. Die nächste Pacht wird am 22. Oktober, die nächsten Löhne am 23. Oktober und die Rahmenrate für die Fahrzeugfinanzierung nach dem 16. Oktober fällig. Für September ergibt die vorbereitete Umsatzsteueranmeldung wegen der Fahrzeugzugänge einen Vorsteuerüberhang. Eine Erstattung ist im Zahlungskalender nicht angesetzt.'),
      ('3. Finanzierung und weitere Eingänge','Die 50.000 Euro Investitionsdarlehen der Hausbank sind endfällig im Juni 2027. Die nächste Zinsabrechnung erfolgt Ende November. Beim Gesellschafterdarlehen ist im ersten Quartal 2027 die Schlusszahlung vorgesehen. Weitere Konten außer den zwei Bankverbindungen in B01–B04 bestehen nicht. Die Kreditbrücke aus dem Verkaufsgespräch ist im Kalender unberücksichtigt.'),
      ('4. Beleghorizont','Für die ersten drei Wochen hat das Team alle bekannten Fälligkeiten, sicheren Kundenzahlungen und Zahlungsanweisungen einzeln abgeglichen. Für spätere Wochen stehen auch kalkulierte Werkstattumsätze und laufende Kosten im Plan. Der Firmenportal-Ausdruck zeigt heute 50.000 Euro Habensaldo. Die zweite Maske zur Verfügung ist im Ausdruck des Freitagsordners nicht enthalten.')],'Jule Kopp · Leiterin Buchhaltung')
    sheet(g/'F01_Saldenliste.xlsx','Vorläufiger Zwischenabschluss 25. September',[
      ('Vermögen','Bilanzwerte in EUR vor Ergebnisverwendung. Kontengruppe 18 enthält die gesamte Bankforderung einschließlich etwaiger Verfügungsbeschränkungen.',
       ['Konto','Posten','Buchwert EUR'],[16,60,25],[[a,b,c] for a,b,c,_,_ in AKTIVA]+[['','Aktivsumme',('=SUM(C5:C10)',486000)]]),
      ('Kapital','Laufende Geschäfte und Abgrenzungen sind gebucht. Vier offene Garantiefälle mit erwarteten Zahlungen ab Dezember ergeben 20.000 Euro. Eigenkapital ist der Saldoposten.',
       ['Konto','Posten','Buchwert EUR'],[16,60,25],[[a,b,c] for a,b,c,_,_ in PASSIVA]+[['EK','Eigenkapital',31000],['','Passivsumme',('=SUM(C5:C10)',486000)]])])
    word(g/'F02_Darlehen_Mergenthal.docx','Mergenthal Beteiligungsgesellschaft mbH','Beteiligungsverwaltung · Böblingen','Darlehensvereinbarung','Abschrift der unterzeichneten Ausfertigung vom 2. Januar 2024',[
      ('1. Darlehensparteien und Auszahlung','Die Mergenthal Beteiligungsgesellschaft mbH gewährt der Autohaus Schönbuchring GmbH 115.000 Euro für die Umstellung des Gebrauchtwagenlagers. Die Valuta wird in einer Summe auf das Betriebskonto geleistet. Die Auszahlung ist für den 3. Januar 2024 vereinbart.'),
      ('2. Fälligkeit und Vergütung','Das Darlehen ist zinslos. Der Kapitalbetrag wird am 31. März 2027 zurückgezahlt. Änderungen der Fälligkeit bedürfen einer von beiden Gesellschaften unterzeichneten Vereinbarung. Bis zur Fälligkeit kann der Betrag im Betrieb verbleiben.'),
      ('3. Sicherheiten und Zahlungsbedingungen','Es werden keine Sicherheiten bestellt. Die Forderung ist vorbehaltlos aus dem Vermögen der Darlehensnehmerin zu bedienen. Ein Verzicht, eine Zahlungssperre zugunsten vorrangiger Gläubiger oder eine gesonderte Rangvereinbarung werden nicht vereinbart.')],
      'Mara Gehring, Geschäftsführerin der Darlehensgeberin\nEva Mergenthal, Geschäftsführerin der Darlehensnehmerin')
    sheet(g/'V01_Hofliste.xlsx','Fahrzeugbestand und Ablöse am 25. September',[
      ('Fahrzeuge','Abgleich Fahrzeugbriefschrank · Beträge ohne abzugsfähige Umsatzsteuer. Die beiden Kommissionsfahrzeuge stehen in der Halle zur Verkaufsvermittlung.',
       ['Hof-Nr.','Objekt','Grund der Überlassung','Buchwert EUR','Ablöse EUR'],[15,35,31,18,18],
       [[a,b,c,d,f] for a,b,c,d,_,f in AUTOS]+[['','Summe','',('=SUM(D5:D12)',206000),('=SUM(E5:E12)',140000)]])])
    word(g/'V02_Einkaufsfinanzierung.docx','Hofwagen Finanz GmbH','Händlerfinanzierung · Sindelfingen','Rahmenvertrag für den Lagerwageneinkauf','Vertragsakte HF 28 / 2025 · Stammvertrag 18.08.2025 · Nachtrag 22.09.2026 · Lesefassung 25.09.2026',[
      ('1. Objektgebundene Valuta','Die Finanzierung wird auf den einzelnen Fahrzeugeinkauf gebucht. Das Autohaus trägt Standkosten, Wertschwankungen und Verkaufsrisiko. Es führt für jedes Fahrzeug einen eigenen Ablöseposten. Fahrzeuge aus Kommissionsgeschäften dürfen nicht belastet werden.'),
      ('2. Sicherungsübereignung und Verwertung','Die in den Einzelabrufen bezeichneten Fahrzeuge dienen der Sicherung. Fahrzeugbriefe bleiben bis zur Ablösung bei Hofwagen Finanz. Ein Verkauf ist bei gleichzeitiger Überweisung der abgerufenen Objektvaluta gestattet. Bei Verwertung wird zuerst die offene Valuta bedient. Ein verbleibender Erlös steht dem Autohaus zu. Eine Unterdeckung bleibt als persönliche Forderung bestehen.'),
      ('3. Zahlungstermine','Die Endfälligkeit folgt aus der Einzelzusage. Für die sechs in der Hofliste V01 geführten Abrufe wurden am 22. September Endfälligkeiten zwischen dem 30. Oktober und 18. Dezember 2026 bestätigt. Eine vorzeitige Fälligkeit entsteht bei Veräußerung. Für keines der sechs Fahrzeuge liegt am 25. September ein bindender Kaufvertrag vor.'),
      ('4. Umfang des Rahmens','Der Einkaufsrahmen erlaubt ausschließlich Finanzierungen gegen Fahrzeugrechnung. Eine Überweisung auf das Betriebskonto zur freien Verwendung ist ausgeschlossen. Die Verfügungsrechte und Sicherheiten der Hausbank am dort geführten Konto bleiben getrennt.')],
      'Für Stammvertrag und Nachtrag zeichnen Nina Luz, Hofwagen Finanz GmbH, und Eva Mergenthal, Autohaus Schönbuchring GmbH. Lesefassung mit Objektstand vom 25. September 2026.')

def dispositionsplan(g):
    template=['Periode','Von','Bis','Mittel Beginn EUR','Ein EUR','Aus EUR','Mittel Ende EUR']
    wg=[];mg=[];saldo=60000
    for i,(a,b,e,z) in enumerate(wochen(),start=1):
        row=i+4
        wg.append([f'W{i:02}',str(a),str(b),saldo if i==1 else (f'=G{row-1}',saldo),e,z,(f'=D{row}+E{row}-F{row}',saldo+e-z)])
        saldo+=e-z
    for i,(e,z) in enumerate(zip(MONAT_EIN,MONAT_AUS),start=1):
        # Erste Rumpfperiode schließt direkt an Woche 13 an.
        start=date(2026,12,26) if i==1 else date(2027,i-1,26);end=date(2027,i,25);row=i+4
        mg.append([f'M{i:02}',str(start),str(end),("='13 Wochen'!G17" if i==1 else f'=G{row-1}',saldo),e,z,(f'=D{row}+E{row}-F{row}',saldo+e-z)])
        saldo+=e-z
    sheet(g/'P01_Terminplan.xlsx','Kassenplanung für den Gesellschaftertermin',[
      ('13 Wochen','Fassung Freitag, 25.09., 18:40. Startbetrag lt. Übersichtsmaske plus Kasse und abrufbarer Linie. Keine Gesellschafterbrücke eingerechnet. Beträge brutto.',
       template,[12,15,15,19,18,18,20],wg),
      ('Anschluss','Monatliche Fortschreibung bis 25.09.2027. Die Woche 13 endet 25.12.2026. Die Märzfälligkeit des Gesellschafterdarlehens liegt in M04 (26.03.–25.04.).',
       template,[12,15,15,19,18,18,20],mg)])
def post(g,n):
    mail(g/'A01_Mandatsanfrage.eml','2026-09-25T19:04:00+02:00',GF,BERATUNG,
      'Vor dem Montagstermin – wie lange reicht die Kasse auf der Hulb?',
      '''Sehr geehrte Frau Nehring,

auf dem Hof stehen acht Wagen, aber fünf Interessenten haben im September nur nach einem günstigeren Leasing gefragt. In der Werkstatt haben wir für Montag 19 Auftragskarten liegen. Die Kolleginnen fragen inzwischen, ob sie bei der Teileausgabe auf Barzahlung umstellen sollen. Wir haben 14 Beschäftigte, davon drei Auszubildende. Das Gebäude ist gepachtet.

Meine Buchhalterin hat den Lauf mit dem Habensaldo aus der Startansicht geplant. Beim letzten Fahrzeugverkauf haben wir zuerst die Objektvaluta abgelöst. Vielleicht hängt deshalb wieder die zweite Kontomaske. Beim Einkaufskredit liegen Fahrzeugbriefe, die Linie ist für Teile- und Lohnzahlungen nicht frei.

Ich brauche Ihren Blick auf den Stand heute Abend. Was können wir in den nächsten drei Wochen und über das Quartal tatsächlich zahlen? Reicht die Zusage unserer Gesellschafterin für das kommende Jahr? Bitte führen Sie die kurzfristige Zahlungsfrage und den Wert des Betriebs für mich getrennt aus. Legen Sie mir für Montag auch die zwei dringendsten Rückfragen hin. Die Heimfahrt des Vorführwagens SB-107 ist verschoben.

Mit freundlichen Grüßen
Eva Mergenthal
Autohaus Schönbuchring GmbH · Geschäftsführung''')
    mail(g/'P02_Gesellschafterpost.eml','2026-09-25T15:33:00+02:00',
      'Mara Gehring <m.gehring@mergenthal-holding.example>',GF,
      'Unser Gespräch am Freitagmorgen – möglicher Zuschuss',
      '''Liebe Eva,

ich bringe eine zusätzliche Einzahlung bis 90.000 Euro am Montag auf die Tagesordnung. Unser Beirat hat mir weder die Summe noch einen Zahlungstermin freigegeben. Die Liquidität der Beteiligungsgesellschaft wird für eine Anleiherate benötigt. Bevor wir selbst einen Termin versprechen, möchte ich die Kassenplanung und den Eingang des Kaufpreises für unseren alten Standort sehen. Eine Veräußerung ist dafür erst angebahnt.

Der bestehende Darlehensvertrag läuft wie vereinbart. Einen geänderten Rang oder einen Erlass kann ich heute nicht zusagen. Bitte teile keinem Lieferanten mit, das Geld sei schon angewiesen.

Mara''')
    letter(n/'N01_Dispositionsbestaetigung.pdf',BANK,'Kreditsachbearbeitung · Konto BB 4416',ADRESSE,'28.09.2026','KD 1784 / Abfrage vom 25.09.','Verfügungsrahmen am Freitag um 18 Uhr',[
      'Wir haben die Historie des Freigabejournals für Freitag, den 25. September, wiederhergestellt. Der Zahlungseingang zu SB-066 war auf dem Konto gebucht. Um 16:15 Uhr am 24. September wurde gemäß Sicherungsabrede vom 18. September ein Teilbetrag von 32.000 Euro für das Investitionsdarlehen über 50.000 Euro gesperrt. Der Betrag bleibt zivilrechtlich eine Bankforderung des Autohauses. Wir bewerten ihn in der Geschäftsbeziehung zum Nominalbetrag.',
      'Der Sperrbetrag war Freitag weder über das Portal noch per Schalterauftrag abrufbar. Bis einschließlich 16. Oktober ist keine Freigabe zugesagt. Eine Überziehung und ein neuer Zwischenkredit wurden am 24. September nach abschließender Kreditentscheidung abgelehnt. Die Kundenberaterin kann die Entscheidung nicht im Telefonweg ändern. Weitere Zusagen oder automatische Gegenbuchungen bestehen nicht.',
      'Den betreffenden Journalauszug sendet Ihnen unser Firmenservice elektronisch. Ihr Zweitbankkonto und der Einkaufsrahmen sind keine Bestandteile dieser Bestätigung.','Tobias Wieland · Firmenkundenservice'])
    with (n/'N03_Freigabejournal.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f,delimiter=';');w.writerows([['Zeit MESZ','Kontokennung','Art','Betrag EUR','Referenz'],['24.09.2026 16:15','BB 4416','Sperre aktiv','32000,00','KD-1784'],['25.09.2026 17:30','BB 4416','Buchsaldo','50000,00','ABS-25'],['25.09.2026 17:30','BB 4416','effektiver Verfügungsbetrag','18000,00','DIS-25'],['28.09.2026 08:30','BB 4416','Sperre weiter aktiv','32000,00','KD-1784']])
    mail(n/'N05_Antwort_Firmenservice.eml','2026-09-28T09:02:00+02:00','Tobias Wieland <dispo@wuermquell.example>',FI,
         'BB 4416 / der abweichende Betrag im Auftragsschirm',
         'Guten Morgen Frau Kopp,\n\nim Abruf vom Freitag standen Buchsaldo und Auftragsrahmen auf unterschiedlichen Reitern. Anbei die Ereignisse aus dem zweiten Reiter, wie soeben besprochen. Die Vertragsauskunft ist Ihnen als gesondertes Schreiben N01 zugegangen.\n\nTobias Wieland',n/'N03_Freigabejournal.csv')
    letter(n/'N02_Verwertungsangebot.pdf','Hubert Ganter Fahrzeughandel','Händlerankauf und Werkstattausstattung · Gäufelden',ADRESSE,'28.09.2026','Ankauf HG-104 / Bewertung 25.09.','Abholung der Fahrzeuge und Werkstatteinrichtung',[
       'Unser Einkauf hat die sechs Fahrzeuge am 25. September besichtigt. Die nachstehenden Nettoerlöse entsprechen den Einzelpreisen nach Transport, Auktionsgebühr und auszusondernder Umsatzsteuer. Die für die Erstaufnahme an der Hallenwand fotografierten Preise sind Endkunden-Wunschpreise.',
       'Werkstattausstattung und Teilelager sind bei Einzelabgabe im Paket realisierbar. Die 41.000 Euro bzw. 17.000 Euro verstehen sich nach Ausbau, Verladung und weiterer Verwertung. Das Wartungsabonnement erlischt laut Anbieter bei Betriebsaufgabe ohne Erstattung. Die vier Garantievorgänge des Verkäufers bleiben bei ihm. Wir übernehmen keine Gewährleistungsschulden.',
       'Die Eigentümer der zwei Kommissionsfahrzeuge verkaufen separat. Wir zahlen frühestens am 23. Oktober, vorausgesetzt die Papiere sind freigegeben. Die Ablöse kann über eine direkte Zahlungsanweisung an Hofwagen Finanz erfolgen. Eine Abschlagszahlung im September oder bis zum 16. Oktober kommt nicht in Betracht. Das Angebot gilt bis Ende September.'],
        [['Objekt','Erlös nach Einzelkosten EUR']]+[[r[0]+' · '+r[1],eur(r[4])] for r in AUTOS[:6]]+[['Werkstattausstattung',eur(41000)],['Ersatzteil- und Räderlager',eur(17000)]])
    mail(n/'N04_Rechnung_AR130.eml','2026-09-28T10:27:00+02:00','Lea Geiß <verfahren@geiss-kollegium.example>',GF,
       'Schwanenflug / Stand des Vergleichsangebots bei Büroschluss Freitag',
       '''Sehr geehrte Frau Mergenthal,

der gegnerische Versicherer hat uns am 24. September schriftlich eine einmalige Zahlung von 8.000 Euro zur endgültigen Erledigung der Rechnung AR-130 angeboten. Annahme bleibt bis 5. Oktober offen. Vor dem 30. November wird keine Zahlung fällig. Die restlichen 14.000 Euro bestreitet die Gegenseite wegen des früheren Anstoßes an der linken Fahrzeugseite. Eine Fotoserie von der Anlieferung fehlt. Für einen zeitnahen Verkauf des Anspruchs liegt kein besseres Angebot vor.

Das Angebot war in unserem elektronischen Postfach bereits am Freitag zugänglich. Ich habe Ihnen die Nachricht erst heute weitergeleitet. Ihre Zustimmung steht noch aus.

Lea Geiß · Rechtsanwältin''')
    mail(n/'N06_Brueckenanfrage.eml','2026-09-28T14:10:00+02:00','Mara Gehring <m.gehring@mergenthal-holding.example>',GF,
      'Beiratssitzung beendet – keine Freigabe für Oktober',
      '''Liebe Eva,

der Beirat hat heute weder einen Zuschuss noch ein weiteres Darlehen freigegeben. Wir müssen die Anleiherate aus den Mitteln der Holding bedienen. Wir hatten am Freitag keine unterschriebene Zusage. Es gibt auch keinen Termin, zu dem ich noch einmal für eine Auszahlung vor dem 16. Oktober vorsprechen könnte.

Mit dem Gebäudeeigentümer gibt es bislang nur ein telefonisches Gespräch über eine Untervermietung von zwei Hebebühnen. Bitte lasst diese Hoffnung nicht wie einen Mietvertrag durch die Planung laufen. Nächste reguläre Beratung im November.

Mara''',reply='<p02.sr26@schoenbuchring.example>')

def einzelbelege(g):
    letter(g/'O05_Rechnung_Lackzentrum.pdf','Lackzentrum Böblinger Tal GmbH','Auftragsabrechnung · Kälberhalde 12 · 71032 Böblingen',ADRESSE,
      '24.09.2026','Zweitschrift der Rechnung vom 04.09. · EA-971 · Kundenkonto 148','Lackierarbeiten an den Werkstattlosen 158 bis 173',[
        'Leistungszeitraum 10. bis 28. August 2026. Die zugehörigen Reparaturkarten wurden bei der Rückgabe vom Werkstattleiter gegengezeichnet. Dieses Sammellos betrifft Kundenfahrzeuge. Die Lackierung der sechs finanzierten Verkaufsfahrzeuge ist nicht Gegenstand dieser Abrechnung.',
        'Der Rechnungsbetrag von 19.000,00 Euro ist am 18. September 2026 fällig. Nach dem Kontenabgleich vom 24. September ist keine Zahlung verbucht. Wir bitten um Ausgleich unter Angabe EA-971. Eine Stundung oder Gutschrift ist bisher nicht vereinbart.'],
        [['Leistung','EUR'],['Arbeits- und Kabinenzeit netto','12.355,46'],['Material und Entsorgung netto','3.610,93'],['Umsatzsteuer 19 %','3.033,61'],['Zahlbetrag','19.000,00']])
    mail(g/'O06_Avis_Flieder.eml','2026-09-24T14:46:00+02:00','Hanna Bihl <disposition@flieder-kurier.example>',FI,
       'AR-482 im Zahllauf vom Dienstag',
       'Guten Tag Frau Kopp,\n\nwir haben die Karten für die fünf Transporter mit den Schlüsselübergaben abgeglichen. Der Leihwagen für Wagen 4 ist berücksichtigt. Die Rechnung AR-482 über 18.000 Euro ist im Lauf FK-42 freigegeben. Die Wertstellung auf Ihrem Geschäftskonto ist für den 29. September eingetragen. Es gibt weder Abzüge noch einen offenen Rückruf. Die Fahrerin bringt Ihnen am Montag noch den Klinikparkausweis zurück.\n\nHanna Bihl · Flieder Kurierdienst')
    word(g/'P03_Planungsannahmen.docx',FIRMA,'Controlling und Service','Verkaufsannahmen für den Werkstatt- und Händlerbetrieb','Aktennotiz vom 25.09.2026 zur Fassung P01, Freigabe 18:40 Uhr',[
      ('1. Übergang vom Zahlungskalender','Die ersten drei Wochen enthalten die einzelnen offenen und fällig werdenden Verpflichtungen sowie die bestätigten Kundenabrufe. Der Plan sieht die Begleichung aller vier Rückstände bis 2. Oktober vor. Die vier Wochenenden Ende September und im Oktober begrenzen die zur Verfügung stehenden Auslieferungsslots. Zwei Vorführwagentermine wurden bereits abgesagt.'),
      ('2. Planung nach dem 16. Oktober','Ab Woche 4 werden Werkstattaufträge und Teileumsätze aus der Terminbelegung fortgeschrieben. Monatlich werden zwischen 72 und 91 Arbeitsaufträge mit Zahlung per Karte bei Abholung unterstellt. Im Fahrzeuggeschäft sind die erwarteten Verkaufsentgelte und die jeweils erforderlichen Ablösezahlungen brutto in der Ein- bzw. Auszahlungsseite enthalten. Die vier fest disponierten Auslieferungstage am Monatswechsel November/Dezember tragen den Sprung in Woche 10. Vor dem 17. Oktober wird kein Lagerverkauf unterstellt.'),
      ('3. Zahlungsbedingungen und fehlende Zusagen','Die zweckgebundene Einkaufsfinanzierung verlängert das Ziel zur Fahrzeugablösung. Einen Geldzufluss aus ihr plant das Büro nicht. Im Monatsanschluss sind die Löhne von 14 Beschäftigten, die Grundstückspacht, Abgaben, Kauf und Ablösung von Lagerwagen, der Schuldendienst und die auslaufenden Garantien enthalten. Die Rückführung des bis Jahresende nutzbaren Zweitbankrahmens von 8.000 Euro ist im ersten Anschlussmonat, die Fälligkeit des Investitionsdarlehens im Juni berücksichtigt. Die Rückzahlung an die Beteiligungsgesellschaft ist in der Periode 26. März bis 25. April eingestellt. Für externe Finanzmittel gibt es im Plan keine weitere Position.'),
      ('4. Operative Untergrenze','Ohne Ersatzteile kann die Werkstatt nur begonnene Arbeiten fertigstellen. Ein Stilllegen der Lackkabine vermindert kurzfristig den Stromverbrauch, kostet zugleich abrechenbare Aufträge. Die Geschäftsleitung hat weder über geänderte Lieferfristen noch über Kurzarbeit oder die Abgabe eines Betriebsteils entschieden. Die Schichttafel bleibt auf zwei Teams. Für Woche 1 liegt kein verbindlicher Käufer für Anlagevermögen vor.')],'Jule Kopp · gegengelesen von Eva Mergenthal')

def recheneingaben(path):
    cash=[('B01','Verfügbarer Teil des Betriebskontos','B02 25.09. und N01, N03 17:30',18000),('B03','Barbestand','B03 letzter Bon 005731',2000),('B04','Abrufbare Zweitbanklinie','B04 KK 870',8000)]
    def item(key,desc,beleg,euro,**attrs):
        return {'id':key,'description':desc,'source':beleg,'amountCents':euro*100,'decision':'include',**attrs}
    liquid={
        'complete':True,
        'nearClosure':{'result':'not_established','source':'N01, P02, N06 und Händlerankauf N02','reason':'Kein disponibler Überbrückungskredit oder fristgerechter Kaufpreisanspruch. Vor dem 16. Oktober besteht keine belastbare weitere Finanzierungszusage.'},
        'assets':[item(a,b,c,d,kind='cash',availableOn=str(STICHTAG)) for a,b,c,d in cash]+[
            item(r[0],r[2]+' / '+r[1],'O02 und O03, '+r[6],r[5],kind='inflow',availableOn=r[4]) for r in DEBITOREN[:-1]]+[
            item('SP','Gesperrter Teil des Buchguthabens','N01 und N03, KD 1784',32000,decision='exclude',reason='Für die ganze Dreiwochenfrist gesperrt.',kind='cash',availableOn=str(STICHTAG))],
        'liabilities':[item(r[0],r[2]+' / '+r[3],'O01 '+r[1]+' und O04, Abschnitt 1',r[5],dueOn=r[4]) for r in KREDITOREN],
    }
    over={'complete':True,'forecast':{'result':'negative','through':'2027-09-25','failureOn':'2026-10-02','source':'P01 13 Wochen und Anschluss, B04, N01, P02 und N06','reason':'Spätestens am Ende von Woche 1 fehlen 9.500 Euro. Der Plan kann die fälligen Zahlungen ohne unverbindliche neue Mittel nicht abbilden. Der unbestätigte Zuschuss und das spätere Kaufangebot schließen die Lücke nicht.'},
          'assets':[item(a,b,e,d) for a,b,c,d,e in AKTIVA],
          'liabilities':[item(a,b,e,d) for a,b,c,d,e in PASSIVA]}
    control={'caseName':FIRMA,'dates':[{'date':str(STICHTAG),'liquidity':liquid,'overindebtedness':over}]}
    plan={'schemaVersion':2,'firma':FIRMA,'stichtag':str(STICHTAG),'bank':18000,'kasse':2000,'kkfrei':8000,'passivaI':52000,'passivaII':78000,'vollstaendig':True,
      'ein':[{'label':'Bestätigte Kundenavis F01 bis F07','w':[36500,24500,25000]}],
      'aus':[{'label':'Altverbindlichkeiten im Zahlungslauf','w':[52000,0,0]},{'label':'Neu fällige Verbindlichkeiten','w':[22000,31000,25000]}],
      'ofGesamt':108000,'ofErwartet':86000,'ofTituliert':0,'ofZweifel':22000,'indizien':[False]*9,
      'notes':'Bewertung zum 25.09. nach Vorlage N01. B02 Buchsaldo 50.000; N03 verfügbar 18.000 Euro. Die ausgefüllten Eingaben sind eine Kontrollrechnung. P01 zeigt weitere zehn Wochen und den Anschluss bis September 2027.'}
    for name,data in [('kontrolle-liquiditaetsplaner.json',plan),('kontrolle-insolvenzreife.json',control)]:
        (path/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
    g,n=CASE/'Grundakte',CASE/'Nachlieferung';g.mkdir(parents=True,exist_ok=True);n.mkdir(parents=True,exist_ok=True)
    konten(g);finanzen(g,n);dispositionsplan(g);post(g,n);einzelbelege(g);recheneingaben(HERE)
