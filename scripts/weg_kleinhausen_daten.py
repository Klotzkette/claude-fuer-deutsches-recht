"""Einfache Verwaltungsakte mit fünf selbst genutzten Wohnungen.

Die zwei Übertragungsfehler gehören allein zur ursprünglichen Entwurfsfassung.
Bauprüfwerte und Eingabevarianten werden nicht als Aktenstück exportiert.
"""
from datetime import date, timedelta
from decimal import Decimal


def D(file, title, day, sender, recipient, body, **extra):
    return dict(file=file, title=title, date=day, sender=sender, recipient=recipient, body=body.strip(), **extra)


def E(file, title, day, sender, recipient, body):
    return dict(file=file, title=title, date=day, **{'from': sender, 'to': recipient}, body=body.strip())


def euro(value):
    return f'{Decimal(str(value)):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') + ' EUR'


def bankday(month, day):
    result = date(2025, month, day)
    closed = {date(2025, 1, 1), date(2025, 4, 18), date(2025, 4, 21), date(2025, 5, 1), date(2025, 12, 25), date(2025, 12, 26)}
    while result.weekday() > 4 or result in closed:
        result += timedelta(days=1)
    return result


SLUG = 'weg-kleinhausen'
HV = 'Hausverwaltung Klein und Klar\nInhaberin Lotte Klar\nMarktstraße 8, 31134 Hildesheim\nlotte@kleinundklar.example'
WEG = 'Gemeinschaft der Wohnungseigentümer Kleinhausen\nLindenweg 5, 31139 Hildesheim'
OWNERS = [('WE01', 'Marta Blum', 'Erdgeschoss links'), ('WE02', 'Otto Freund', 'Erdgeschoss rechts'), ('WE03', 'Nora Sommer', 'Obergeschoss links'), ('WE04', 'Emil Kurz', 'Obergeschoss rechts'), ('WE05', 'Aylin Berg', 'Dachgeschoss')]
COSTS = [('Wasser und Abwasser', 1600, 'WA-2025-05', '09_Wasser_Abwasser.docx'), ('Müllabfuhr', 600, 'MU-2025-05', '10_Muellgebuehren.docx'), ('Gebäudeversicherung', 1000, 'GV-2025-05', '11_Gebaeudeversicherung.docx'), ('Allgemeinstrom', 240, 'ST-2025-05', '12_Allgemeinstrom.docx'), ('Treppenhausreinigung', 960, 'R-2025-17', '13_Treppenhausreinigung.docx'), ('Kleinreparatur', 300, 'HR-2025-48', '14_Tuerreparatur.docx'), ('Verwaltung', 900, 'HV-2025-05', '15_Verwalterhonorar.docx'), ('Bankentgelte', 60, 'BK-2025-05', '16_Bankentgelte.docx')]
assert sum(c[1] for c in COSTS) == 5660

TRANSACTIONS = []
for month in range(1, 13):
    for unit, name, _ in OWNERS:
        TRANSACTIONS.append((bankday(month, 5), f'Hausgeld {unit} {name}', 125, 0, unit))
    for day, label, amount, reference in [(18, 'Allgemeinstrom', 20, 'ST-2025-05'), (20, 'Treppenhausreinigung', 80, 'R-2025-17'), (25, 'Verwaltung', 75, 'HV-2025-05'), (28, 'Kontoführung', 5, 'BK-2025-05')]:
        TRANSACTIONS.append((bankday(month, day), label, 0, amount, reference))
    if month in (3, 6, 9, 12):
        TRANSACTIONS.append((bankday(month, 14), 'Wasser und Abwasser', 0, 400, 'WA-2025-05'))
TRANSACTIONS += [(date(2025, 1, 15), 'Gebäudeversicherung', 0, 1000, 'GV-2025-05'), (date(2025, 2, 18), 'Müllabfuhr', 0, 600, 'MU-2025-05'), (date(2025, 6, 24), 'Türschließer eingestellt', 0, 300, 'HR-2025-48'), (date(2025, 12, 29), 'Übertrag Rücklagenkonto', 0, 1500, 'RL-2025-01')]
TRANSACTIONS.sort(key=lambda t: (t[0], t[4]))
assert len(TRANSACTIONS) == 116
bank_rows = [['01.01.2025', 'Anfangsbestand Betriebskonto', 1000, 0, '=C2-D2', 'Vortrag 2024']]
for row, (day, label, incoming, outgoing, reference) in enumerate(TRANSACTIONS, 3):
    bank_rows.append([day.strftime('%d.%m.%Y'), label, incoming, outgoing, f'=E{row-1}+C{row}-D{row}', reference])
monthly_rows = []
running = 1000
for month in range(1, 13):
    records = [t for t in TRANSACTIONS if t[0].month == month]
    received = sum(t[2] for t in records)
    costs = sum(t[3] for t in records if t[4] != 'RL-2025-01')
    transfer = sum(t[3] for t in records if t[4] == 'RL-2025-01')
    running += received - costs - transfer
    monthly_rows.append([f'{month:02d}/2025', euro(received), euro(costs), euro(transfer), euro(running)])
assert running == 1340

advance_rows = []
for row, (unit, name, _) in enumerate(OWNERS, 2):
    advance_rows.append([unit, name, 100, 25, f'=C{row}*12', f'=D{row}*12', f'=SUMIFS(\'Bankbuch\'!$C$3:$C$118,\'Bankbuch\'!$F$3:$F$118,A{row})', f'=E{row}+F{row}-G{row}'])
advance_rows.append(['Summe', '', '=SUM(C2:C6)', '=SUM(D2:D6)', '=SUM(E2:E6)', '=SUM(F2:F6)', '=SUM(G2:G6)', '=SUM(H2:H6)'])
draft_rows = []
for row, (label, amount, reference, _) in enumerate(COSTS, 2):
    draft_rows.append([label, 260 if label == 'Allgemeinstrom' else amount, 'R-2025-71' if label == 'Treppenhausreinigung' else reference, f'=B{row}/5'])
draft_rows += [['Kosten gesamt', '=SUM(B2:B9)', '', '=SUM(D2:D9)'], ['', None, '', None], ['Kostenvorschüsse 2025', "='Vorschuesse'!E7", 'Beschluss vom 15.11.2024', '=B12/5'], ['Guthaben laut Entwurf', '=B12-B10', 'Fassung vom 15.09.2026', '=D12-D10']]

documents = [
E('01_Auftrag.eml', 'Kleinhausen Abrechnung einmal in Ruhe prüfen', '2026-09-24T09:10:00+02:00', 'Lotte Klar <lotte@kleinundklar.example>', 'Büro Morgen <post@morgen.example>', '''Guten Tag Frau Morgen,

ich verwalte das kleine Haus Kleinhausen mit fünf Wohnungen. Alle fünf Eigentümer wohnen selbst dort. Die laufenden Kosten und die Vorschüsse werden immer zu gleichen Teilen verteilt. Für 2025 sind alle zwölf Hausgeldraten von allen Eigentümern eingegangen.

Ich habe am 16. September die erste Fassung der Jahresabrechnung geschickt. Nun haben Frau Blum und Herr Freund zwei Rückfragen. Bitte sehen Sie die Belege und meine Excel-Datei durch, berichtigen Sie nötigenfalls die Abrechnung und formulieren Sie eine freundliche gemeinsame Erläuterung sowie fünf kurze Begleitbriefe. Die Beschlussvorlage soll anschließend ebenfalls zum geprüften Zahlenstand passen. Die Rücklage möchte ich verständlich, aber getrennt von den verbrauchten Kosten darstellen.

Die jährliche Versammlung ist für den 20. November 2026 um 18 Uhr im Nachbarschaftsraum Lindenweg 7 vorgemerkt. Die Einladung ist noch nicht verschickt. Nach der Prüfung habe ich ausreichend Zeit für den Versand. Eine Entscheidung über die Abrechnung gibt es noch nicht. Bitte senden Sie selbst nichts an die Eigentümer und lösen Sie keine Auszahlungen aus. Ich lese die Entwürfe vorher durch und kümmere mich um den weiteren Ablauf.

Vielen Dank und freundliche Grüße
Lotte Klar'''),
D('02_Stammdaten.docx', 'Kleinhausen Stammdaten der Gemeinschaft', '02.09.2026', HV, 'Verwaltungsunterlagen', '''Das Haus am Lindenweg 5 hat fünf Wohnungen. Jede Wohnung gehört seit vor dem 1. Januar 2025 genau einer Person und hat 200 von 1.000 Miteigentumsanteilen. Eigentümerwechsel gab es 2025 nicht. Alle Wohnungen werden von ihren Eigentümern selbst genutzt.

Marta Blum wohnt in Wohnung 1 im Erdgeschoss links. Otto Freund wohnt in Wohnung 2 im Erdgeschoss rechts. Nora Sommer wohnt in Wohnung 3 im Obergeschoss links. Emil Kurz wohnt in Wohnung 4 im Obergeschoss rechts. Aylin Berg wohnt in Wohnung 5 im Dachgeschoss. Die Wohnungsnummern in der Buchhaltung lauten WE01 bis WE05. Jeder Eigentümer hat eine Stimme.

Die Gemeinschaft hat ein Betriebskonto mit der internen Kennung KH-B und ein gesondertes Rücklagenkonto KH-R. Beide Konten lauten auf die Gemeinschaft. Zahlungsaufträge werden ausschließlich über die im Verwaltungsbüro hinterlegten Bankdaten ausgeführt. Das Rücklagenkonto wird nicht für laufende Rechnungen verwendet.

Die Wohnungen haben eigene Heizungen und eigene Stromverträge. Die Gemeinschaft rechnet dafür keine Kosten ab. Die gemeinschaftliche Wasserversorgung wird nach den Miteigentumsanteilen verteilt. Weitere Kostenverteilungsschlüssel oder Sonderregelungen sind für diese Abrechnung nicht vorhanden.

Die Post geht jeweils an den Eigentümer in seiner Wohnung. Für E-Mails verwenden wir die freigegebenen Adressen marta@blum.example, otto@freund.example, nora@sommer.example, emil@kurz.example und aylin@berg.example. Lotte Klar ist unter lotte@kleinundklar.example erreichbar.'''),
D('03_Gemeinschaftsordnung.docx', 'Gemeinschaftsordnung Kleinhausen Auszug', '12.06.2012', WEG, 'Abschrift für die Verwaltungsakte', '''1. Gemeinschaft und Wohnungen

Die fünf Wohnungen bilden eine einheitliche Gemeinschaft. Jeder Wohnung sind 200 von insgesamt 1.000 Miteigentumsanteilen zugeordnet. Es bestehen keine Teileigentumseinheiten, Untergemeinschaften oder gesonderten Abrechnungskreise.

2. Verteilung der Kosten

Die Kosten der Verwaltung und des gemeinschaftlichen Eigentums werden nach Miteigentumsanteilen verteilt. Die Beiträge zur Erhaltungsrücklage werden ebenfalls nach Miteigentumsanteilen aufgebracht. Für die in dieser Abschrift behandelten Kostenarten ist keine abweichende Verteilung vereinbart. Individuelle Verträge der Bewohner mit Energieversorgern gehören nicht zur gemeinschaftlichen Abrechnung.

3. Rechnungsjahr und Unterlagen

Das Rechnungsjahr entspricht dem Kalenderjahr. Die Verwaltung führt für die Gemeinschaft eine geordnete Sammlung der Rechnungen, Zahlungsnachweise und Beschlüsse. Die Eigentümer können nach Terminvereinbarung die Verwaltungsunterlagen einsehen. Vorschüsse und die nach einer Abrechnung erforderlichen Anpassungen werden von der Eigentümerversammlung gesondert beschlossen.

Die vorstehende Abschrift gibt die für die laufende Jahresabrechnung benötigten Regelungen wieder. Lotte Klar hat sie am 02.09.2026 mit der im Büro verwahrten Ausfertigung abgeglichen. Nach dem Beschlussverzeichnis wurde der Verteilungsschlüssel seitdem nicht geändert.'''),
D('04_Verwalterauftrag.docx', 'Verwaltung des Hauses Kleinhausen', '15.11.2024', WEG, HV, '''1. Bestellung und Vertragsdauer

Die Eigentümer bestellen Lotte Klar, handelnd als Hausverwaltung Klein und Klar, für den Zeitraum vom 1. Januar 2025 bis zum 31. Dezember 2027 zur Verwalterin. In der Eigentümerversammlung vom 15. November 2024 stimmen alle fünf Eigentümer der Bestellung und diesem Vertrag zu. Die Niederschrift ist von der Versammlungsleiterin Marta Blum und dem Eigentümer Otto Freund unterzeichnet.

2. Leistungen

Die Verwalterin führt die Konten und Belege der Gemeinschaft, überwacht die beschlossenen Vorschüsse, bereitet jährlich den Wirtschaftsplan, die Jahresabrechnung und den Vermögensbericht vor und organisiert die ordentliche Eigentümerversammlung. Sie beantwortet Rückfragen zu diesen Unterlagen und ermöglicht die Einsicht in die Belege. Sie stimmt notwendige Handwerkertermine mit dem Haus ab. Über Aufträge außerhalb ihrer Befugnisse lässt sie zuvor beschließen.

3. Vergütung

Die Gemeinschaft zahlt monatlich 75,00 EUR einschließlich Umsatzsteuer. Die Vergütung ist jeweils am 25. des Monats fällig. Sie umfasst die Verwaltung aller fünf Wohnungen als Gemeinschaft sowie eine ordentliche Versammlung im Jahr. Für die in diesem Vertrag beschriebenen laufenden Leistungen fallen keine zusätzlichen Gebühren an. Private Leistungen für einzelne Eigentümer sind nicht beauftragt.

4. Konten und Jahresabschluss

Die Verwalterin verwendet ausschließlich Konten der Gemeinschaft. Beschlossene Rücklagenbeiträge werden auf dem gesonderten Rücklagenkonto gesammelt. Die Eigentümer erhalten die Abrechnungsunterlagen so rechtzeitig, dass sie vor der Beschlussfassung Rückfragen stellen können.

Für die Gemeinschaft unterzeichnet Marta Blum aufgrund des Beschlusses vom 15. November 2024. Für die Hausverwaltung unterzeichnet Lotte Klar. Beide Unterschriften wurden am 18. November 2024 geleistet.'''),
D('05_Vorschussbeschluss_2025.docx', 'Beschluss über die Vorschüsse für 2025', '15.11.2024', WEG, 'Auszug aus der Niederschrift der Eigentümerversammlung', '''Die Eigentümer beschließen für das Kalenderjahr 2025 Vorschüsse auf die laufenden Kosten von insgesamt 6.000,00 EUR. Zusätzlich werden Beiträge zur Erhaltungsrücklage von insgesamt 1.500,00 EUR beschlossen. Die Verteilung erfolgt nach den jeweils 200 von 1.000 Miteigentumsanteilen. Für jede Wohnung beträgt der laufende Kostenvorschuss somit 1.200,00 EUR im Jahr und der Rücklagenbeitrag 300,00 EUR im Jahr.

Jeder Eigentümer zahlt von Januar bis Dezember 2025 monatlich 125,00 EUR auf das Betriebskonto der Gemeinschaft. Davon entfallen 100,00 EUR auf die laufenden Kosten und 25,00 EUR auf die Erhaltungsrücklage. Die Rate ist jeweils bis zum 10. Kalendertag des Monats fällig. Die Eigentümer richten entsprechende Daueraufträge ein.

Die Verwalterin überträgt die eingegangenen Rücklagenbeiträge spätestens zum Jahresende auf das gesonderte Rücklagenkonto. Ein Ausgeben der Rücklage wird mit diesem Beschluss nicht gestattet. Über die nach Ablauf des Jahres festzustellenden Anpassungsbeträge wird erst aufgrund der Jahresabrechnung entschieden.

Für den Beschluss stimmen Marta Blum, Otto Freund, Nora Sommer, Emil Kurz und Aylin Berg. Gegenstimmen und Enthaltungen gibt es nicht. Die Versammlungsleiterin Marta Blum stellt den Beschluss fest. Sie und Otto Freund unterzeichnen die Niederschrift am 18.11.2024.'''),
dict(file='06_Abrechnung_2025_Arbeitsdatei.xlsx', title='Kleinhausen Abrechnung 2025 Fassung vom 15 September 2026', sheets=[
    dict(name='Abrechnungsentwurf', headers=['Kostenart', 'Gesamt EUR', 'Belegnummer', 'Je Wohnung EUR'], widths=[36,20,33,22], formats={'B':'#,##0.00','D':'#,##0.00'}, rows=draft_rows, expected={'B10':5680,'D10':1136,'B12':6000,'B13':320,'D13':64}, perturbations=[dict(input='B5', value=240, output='D13', expected=68), dict(input='B5', value=0, output='D13', expected=116)]),
    dict(name='Vorschuesse', headers=['Einheit', 'Eigentümer', 'Kosten monatlich EUR', 'Rücklage monatlich EUR', 'Kostensoll Jahr EUR', 'Rücklagensoll Jahr EUR', 'Eingegangen EUR', 'Offen EUR'], widths=[13,27,19,19,19,19,19,16], formats={c:'#,##0.00' for c in 'CDEFGH'}, rows=advance_rows, expected={'E7':6000,'F7':1500,'G7':7500,'H7':0}),
    dict(name='Bankbuch', headers=['Buchungstag', 'Buchung', 'Eingang EUR', 'Ausgang EUR', 'Saldo EUR', 'Referenz'], widths=[18,35,18,18,18,24], formats={c:'#,##0.00' for c in 'CDE'}, rows=bank_rows, expected={'E2':1000,'E118':1340}),
]),
D('07_Bank_Jahresuebersicht.docx', 'Betriebskonto Kleinhausen Jahresübersicht 2025', '07.01.2026', 'Bürgerbank Innerstetal\nKundenservice Gemeinschaftskonten\nbank@innerstetal.example', WEG, '''Das Betriebskonto KH-B wird im Namen der Gemeinschaft geführt. Es weist am 1. Januar 2025 einen Anfangsbestand von 1.000,00 EUR und am 31. Dezember 2025 einen Schlussbestand von 1.340,00 EUR aus. Alle Beträge dieser Übersicht sind in EUR angegeben.

Im Jahr 2025 gingen 60 Hausgeldraten von jeweils 125,00 EUR ein. Die Summe beträgt 7.500,00 EUR. Die Zahlungen betreffen jeweils zwölf Raten für jede der fünf Wohnungen. Rückgaben oder Stornobuchungen gab es nicht. Die Ausgaben an Versorger, Dienstleister und Bank betragen zusammen 5.660,00 EUR. Zusätzlich wurden am 29. Dezember 1.500,00 EUR auf das Rücklagenkonto KH-R übertragen.

Die nachstehende Monatsübersicht fasst sämtliche Bewegungen des Jahres zusammen. Die vollständigen 116 Einzelbuchungen einschließlich der Rücklagenübertragung sind im mitgelieferten Blatt Bankbuch der Datei 06_Abrechnung_2025_Arbeitsdatei.xlsx enthalten. Der dort vorangestellte Anfangsbestand ist keine Einzahlung des Jahres. Die Bankreferenz entspricht jeweils dem Beleg oder der Wohnungsnummer.

Das Konto ist ein Guthabenkonto. Die hier ausgewiesenen Kontoführungsentgelte sind vollständig gebucht; zusätzliche Jahresgebühren fallen nicht an.''', tables=[dict(headers=['Monat', 'Eingang', 'Kosten', 'Rücklage', 'Schlussbestand'], rows=monthly_rows)]),
D('08_Ruecklagenkonto.docx', 'Rücklagenkonto Kleinhausen Jahresübersicht 2025', '07.01.2026', 'Bürgerbank Innerstetal\nKundenservice Gemeinschaftskonten\nbank@innerstetal.example', WEG, '''Das Rücklagenkonto KH-R lautet auf die Gemeinschaft der Wohnungseigentümer Kleinhausen. Der Kontostand am 1. Januar 2025 betrug 5.000,00 EUR.

Am 29. Dezember 2025 wurde ein Betrag von 1.500,00 EUR vom Betriebskonto KH-B mit dem Verwendungszweck „Rücklagenbeiträge 2025“ gutgeschrieben. Die Buchungsreferenz lautet RL-2025-01. Weitere Einzahlungen oder Entnahmen gab es im Jahr 2025 nicht. Das Konto war im gesamten Jahr unverzinslich und kostenfrei.

Der Schlussbestand am 31. Dezember 2025 beträgt 6.500,00 EUR. Der Betrag steht vollständig auf dem Rücklagenkonto. Es bestehen keine Verpfändung und keine Verfügungssperre.

Diese Jahresübersicht enthält alle Bewegungen des Kontos im Kalenderjahr 2025. Rückfragen beantwortet der Kundenservice unter Angabe der internen Kontokennung KH-R.'''),
]

invoices = [
('09_Wasser_Abwasser.docx', 'Wasser und Abwasser Kleinhausen 2025', '09.01.2025', 'Wasserverband Innerstetal\nAm Wasserwerk 4, 31139 Hildesheim', 'WA-2025-05', '''Für die Versorgung des Hauses Lindenweg 5 werden im Kalenderjahr 2025 insgesamt 1.600,00 EUR berechnet. Davon entfallen 900,00 EUR auf Trinkwasser einschließlich 7 Prozent Umsatzsteuer und 700,00 EUR auf die umsatzsteuerfreie Abwassergebühr. Der Trinkwasserbetrag setzt sich aus 841,12 EUR netto und 58,88 EUR Umsatzsteuer zusammen.

Der Betrag ist in vier Raten von jeweils 400,00 EUR im März, Juni, September und Dezember zu entrichten. Die Beiträge betreffen den gemeinsamen Hausanschluss. Eine Abrechnung gegenüber den einzelnen Wohnungen nehmen wir nicht vor.

Zahlungsvermerk der Buchhaltung vom 22.12.2025: Die vier Raten gingen am 14. März, 16. Juni, 15. September und 15. Dezember 2025 ein. Das Kundenkonto für 2025 ist ausgeglichen. Es bleibt kein Betrag für dieses Kalenderjahr offen.'''),
('10_Muellgebuehren.docx', 'Müllgebühren für das Haus Kleinhausen 2025', '27.01.2025', 'Kommunaler Abfallservice Innerstetal\nWerkstraße 9, 31139 Hildesheim', 'MU-2025-05', '''Für die regelmäßige Leerung der gemeinschaftlichen Restmüll- und Biotonnen des Hauses Lindenweg 5 im Zeitraum vom 1. Januar bis zum 31. Dezember 2025 wird eine Jahresgebühr von 600,00 EUR festgesetzt. Die Papierentsorgung ist in dieser Gebühr enthalten. Zusätzliche Abholungen sind nicht beauftragt.

Die öffentlich-rechtliche Gebühr wird ohne Umsatzsteuer erhoben. Sie ist am 18. Februar 2025 fällig. Bitte verwenden Sie bei der Zahlung die Gebührennummer MU-2025-05.

Zahlungsvermerk vom 20.02.2025: Die vollständigen 600,00 EUR gingen am 18. Februar 2025 ein. Das Gebührenkonto weist für 2025 keinen offenen Betrag aus.'''),
('11_Gebaeudeversicherung.docx', 'Gebäudeversicherung Kleinhausen Beitrag 2025', '06.01.2025', 'Innerstetal Schutzversicherung AG\nVersicherungsplatz 2, 31134 Hildesheim', 'GV-2025-05', '''Versichert ist das Gebäude Lindenweg 5 mit seinen fünf Wohnungen. Die Versicherungsperiode läuft vom 1. Januar bis zum 31. Dezember 2025. Der Jahresbeitrag einschließlich Versicherungssteuer beträgt 1.000,00 EUR. Umsatzsteuer wird nicht erhoben.

Der Versicherungsumfang des bestehenden Vertrags bleibt unverändert. Es handelt sich um die übliche Gebäudeversicherung der Gemeinschaft. Der Beitrag ist zum 15. Januar 2025 fällig und wird vom Betriebskonto der Gemeinschaft eingezogen.

Zahlungsvermerk vom 17.01.2025: Der Einzug über 1.000,00 EUR wurde am 15. Januar 2025 ausgeführt. Der Beitrag ist vollständig bezahlt.'''),
('12_Allgemeinstrom.docx', 'Allgemeinstrom Kleinhausen Jahresabrechnung 2025', '31.12.2025', 'Lichtblick Innerstetal Energie GmbH\nStromstraße 6, 31134 Hildesheim', 'ST-2025-05', '''Diese Abrechnung betrifft ausschließlich Treppenhauslicht, Kellerlicht und die Klingelanlage des Hauses Lindenweg 5 im Kalenderjahr 2025. Wohnungsstrom und Heizungen sind nicht angeschlossen. Der Jahresbetrag beträgt 240,00 EUR einschließlich Umsatzsteuer. Darin enthalten sind 201,68 EUR netto und 38,32 EUR Umsatzsteuer.

Der Ablesestand des Allgemeinzählers KH-L betrug zu Jahresbeginn 10.000 kWh und zum Jahresende 10.400 kWh. Für die 400 kWh werden 120,00 EUR brutto berechnet. Hinzu kommt ein jährlicher Grundpreis von 120,00 EUR brutto.

Die zwölf monatlichen Zahlungen von jeweils 20,00 EUR sind eingegangen. Die Summe der Zahlungen entspricht dem Abrechnungsbetrag. Es ergibt sich weder eine Nachzahlung noch ein Guthaben. Diese Jahresabrechnung fordert keine erneute Zahlung an. Die Monatszahlungen sind unter der Referenz ST-2025-05 auf dem Betriebskonto nachgewiesen.'''),
('13_Treppenhausreinigung.docx', 'Treppenhausreinigung Kleinhausen 2025', '31.12.2025', 'Sauber und Fein Gebäudereinigung\nInhaberin Frieda Fein\nGartenstraße 12, 31139 Hildesheim', 'R-2025-17', '''Wir rechnen die vereinbarte wöchentliche Reinigung des Treppenhauses, des Eingangsbereichs und der gemeinschaftlichen Kellertreppe im Kalenderjahr 2025 ab. Auf die Jahresvergütung wurden monatliche Abschläge von 80,00 EUR einschließlich Umsatzsteuer geleistet. Bei Feiertagen wurde der Reinigungstermin jeweils in derselben Woche verlegt.

Die Jahresvergütung beträgt 960,00 EUR brutto. Darin enthalten sind 806,72 EUR netto und 153,28 EUR Umsatzsteuer. Es wurden ausschließlich Reinigungsleistungen erbracht. Handwerkerarbeiten oder private Wohnungsreinigungen sind nicht Teil dieser Abrechnung.

Alle zwölf Abschläge sind bezahlt. Die gezahlten 960,00 EUR entsprechen dem Jahresbetrag; es ergibt sich weder eine Nachzahlung noch ein Guthaben. Die Rechnungsnummer lautet R-2025-17. Bitte verwenden Sie diese Nummer auch bei Rückfragen.

Freundliche Grüße
Frieda Fein'''),
('14_Tuerreparatur.docx', 'Einstellen des Haustürschließers Kleinhausen', '18.06.2025', 'Hahn und Handwerk\nInhaber Paul Hahn\nWerkstattgasse 3, 31139 Hildesheim', 'HR-2025-48', '''Am 17. Juni 2025 haben wir den vorhandenen Haustürschließer am Lindenweg 5 eingestellt, eine verschlissene Halterung ersetzt und den Schließlauf geprüft. Die Tür schließt seitdem ohne Zuschlagen. Der Auftrag wurde von Lotte Klar für die Gemeinschaft erteilt und umfasst eine kleine Instandsetzung im Rahmen der laufenden Verwaltung.

Für Arbeitszeit und Material berechnen wir zusammen 252,10 EUR netto zuzüglich 47,90 EUR Umsatzsteuer. Der Gesamtbetrag beträgt 300,00 EUR brutto. Die Arbeit ist abgeschlossen. Es sind keine weiteren Leistungen aus diesem Auftrag offen.

Zahlungsvermerk vom 25.06.2025: Die 300,00 EUR gingen am 24. Juni 2025 unter Angabe der Rechnungsnummer HR-2025-48 ein. Der Rechnungsbetrag ist vollständig beglichen.

Mit freundlichen Grüßen
Paul Hahn'''),
('15_Verwalterhonorar.docx', 'Verwalterhonorar Kleinhausen Jahresabrechnung 2025', '31.12.2025', HV, 'HV-2025-05', '''Für die Verwaltung der Gemeinschaft im Zeitraum vom 1. Januar bis zum 31. Dezember 2025 rechnen wir die Jahresvergütung ab. Die Vergütung beruht auf dem am 18. November 2024 abgeschlossenen Verwaltervertrag. Monatlich wurden 75,00 EUR brutto als Abschlag auf den Jahresbetrag entrichtet.

Der Jahresbetrag beträgt 900,00 EUR einschließlich Umsatzsteuer. Er setzt sich aus 756,30 EUR netto und 143,70 EUR Umsatzsteuer zusammen. Die laufende Buchhaltung, die Vorbereitung der Jahresunterlagen und eine ordentliche Eigentümerversammlung sind von dieser Vergütung umfasst.

Alle zwölf Abschläge wurden vom Betriebskonto der Gemeinschaft bezahlt. Ihre Summe beträgt 900,00 EUR. Sondervergütungen sind nicht angefallen. Es ergibt sich weder eine Nachzahlung noch ein Guthaben aus dieser Jahresabrechnung.

Lotte Klar'''),
('16_Bankentgelte.docx', 'Kontoführungsentgelte Kleinhausen 2025', '31.12.2025', 'Bürgerbank Innerstetal\nKundenservice Gemeinschaftskonten\nbank@innerstetal.example', 'BK-2025-05', '''Für das Betriebskonto KH-B wurden im Kalenderjahr 2025 zwölf monatliche Kontoführungsentgelte von jeweils 5,00 EUR belastet. Die Jahresbelastung beträgt damit 60,00 EUR. Es handelt sich um umsatzsteuerfreie Bankentgelte.

Die Entgelte wurden jeweils am 28. des Monats oder am folgenden Bankarbeitstag direkt dem Betriebskonto belastet. Alle zwölf Buchungen sind im Jahresbuchungsbestand unter der Referenz BK-2025-05 enthalten.

Für das gesonderte Rücklagenkonto KH-R wurde kein Entgelt berechnet. Es gibt keine zusätzliche Jahresabrechnungsgebühr und keinen noch einzuziehenden Restbetrag.'''),
]
for filename, title, day, sender, reference, body in invoices:
    documents.append(D(filename, title, day, sender + '\nrechnung@lieferant.example', WEG, body, reference=reference))

documents.append(D('17_Gesamtabrechnung_Entwurf.docx', 'Jahresabrechnung Kleinhausen 2025 Entwurf', '15.09.2026', HV, WEG, '''1. Zahlen der Gemeinschaft

Das Betriebskonto begann mit 1.000,00 EUR. Es gingen Hausgeldzahlungen von 7.500,00 EUR ein. Nach den Bankunterlagen wurden 5.660,00 EUR für laufende Kosten und die kleine Türreparatur bezahlt. Weitere 1.500,00 EUR wurden auf das Rücklagenkonto übertragen. Der Schlussbestand des Betriebskontos beträgt 1.340,00 EUR. Das Rücklagenkonto stieg von 5.000,00 EUR auf 6.500,00 EUR.

2. Verteilung laut Arbeitsdatei

Die nachstehende Kostenliste wurde aus der Arbeitsdatei in diese erste Fassung übernommen. Alle Positionen werden nach den fünf gleichen Miteigentumsanteilen verteilt. Die Liste ergibt insgesamt 5.680,00 EUR und damit 1.136,00 EUR je Wohnung. Auf die laufenden Kosten wurden je Wohnung Vorschüsse von 1.200,00 EUR beschlossen und vollständig gezahlt. Daraus weist diese Fassung ein Guthaben von jeweils 64,00 EUR aus.

3. Rücklage und weiterer Ablauf

Jeder Eigentümer hat zusätzlich 300,00 EUR als Rücklagenbeitrag gezahlt. Diese Beiträge wurden vollständig auf das Rücklagenkonto übertragen. Sie werden nicht noch einmal als verbrauchte Kosten verteilt. Die erste Abrechnungsfassung ist noch nicht beschlossen. Bitte reichen Sie Rückfragen vor der geplanten Versammlung am 20. November 2026 ein. Die Einladung folgt gesondert. Eine Auszahlung wird erst nach der erforderlichen Beschlussfassung veranlasst.

Freundliche Grüße
Lotte Klar''', tables=[dict(headers=['Kostenart', 'Gesamtbetrag', 'Belegnummer'], rows=[[label, euro(260 if label == 'Allgemeinstrom' else amount), 'R-2025-71' if label == 'Treppenhausreinigung' else reference] for label, amount, reference, _ in COSTS])]))
for index, (unit, name, location) in enumerate(OWNERS, 18):
    documents.append(D(f'{index:02d}_Einzelabrechnung_{unit}.docx', f'Jahresabrechnung 2025 Wohnung {unit[-1]} Entwurf', '15.09.2026', HV, f'{name}\nLindenweg 5, {location}\n31139 Hildesheim', f'''Guten Tag {name},

Ihre Wohnung {unit[-1]} ist mit 200 von 1.000 Miteigentumsanteilen an der Gemeinschaft beteiligt. Damit entfällt auf Sie ein Fünftel aller in der beigefügten Gesamtabrechnung aufgeführten Kosten. Die erste Fassung weist für das Jahr 2025 gemeinschaftliche Kosten von 5.680,00 EUR aus. Ihr Anteil beträgt 1.136,00 EUR.

Für Ihre Wohnung waren Kostenvorschüsse von 1.200,00 EUR beschlossen. Diese wurden vollständig gezahlt. Nach der vorliegenden Fassung ergibt sich ein Guthaben von 64,00 EUR. Es handelt sich noch um einen Entwurf für die Vorbereitung der Beschlussfassung, nicht um eine bereits freigegebene Auszahlung.

Zusätzlich haben Sie zwölf Rücklagenbeiträge von je 25,00 EUR, insgesamt 300,00 EUR, geleistet. Auch diese Beiträge sind vollständig eingegangen. Sie bleiben in der gemeinschaftlichen Erhaltungsrücklage. Die Beiträge sind in den vorstehend verteilten Kosten nicht enthalten. Insgesamt gingen von Ihnen im Jahr 2025 zwölf Monatsraten von 125,00 EUR, also 1.500,00 EUR, ein. Es bestehen keine Vorschussrückstände.

Die Gesamtabrechnung, die Belege und die Kontenübersichten können Sie im Büro einsehen. Schreiben Sie mir gern, wenn Sie einen Betrag erklärt haben möchten. Die jährliche Versammlung ist für den 20. November 2026 vorgesehen. Eine gesonderte Einladung folgt.

Freundliche Grüße
Lotte Klar'''))

documents += [
E('23_Versand_Abrechnung.eml', 'Kleinhausen Ihre Abrechnung 2025 als erster Entwurf', '2026-09-16T10:15:00+02:00', 'Lotte Klar <lotte@kleinundklar.example>', 'Marta Blum <marta@blum.example>', '''Guten Tag Frau Blum,

anbei erhalten Sie die erste Gesamtabrechnung und die Einzelabrechnung für Ihre Wohnung. Ich habe die entsprechende Einzelabrechnung heute auch jeweils gesondert an die vier anderen Eigentümer geschickt.

Bitte schauen Sie in Ruhe auf die Angaben und schreiben Sie mir bei Rückfragen. Für Belegeinsicht können wir einen Termin vereinbaren. Die Einladung zur Versammlung am 20. November folgt später. Mit dieser E-Mail wird noch kein Guthaben ausgezahlt.

Freundliche Grüße
Lotte Klar'''),
E('24_Rueckfrage_Marta.eml', 'Re Kleinhausen Allgemeinstrom und Rücklage', '2026-09-18T08:40:00+02:00', 'Marta Blum <marta@blum.example>', 'Lotte Klar <lotte@kleinundklar.example>', '''Guten Morgen Frau Klar,

danke für die Unterlagen. Ich komme mit der Einzelabrechnung grundsätzlich zurecht. Beim Allgemeinstrom stehen in der Kostenliste 260 Euro. In meiner Notiz zur Jahresbesprechung mit Ihnen hatte ich einen anderen Betrag aufgeschrieben. Können Sie mir den Jahresbeleg schicken und die Zahl bitte noch einmal abgleichen?

Außerdem möchte ich nur sicher sein, dass ich die Rücklage richtig verstehe: Die 25 Euro im Monat bleiben auf dem anderen Konto und sind nicht noch einmal in meinen Kosten enthalten? Ich habe alle zwölf Monatsraten bezahlt. Mir reicht dazu eine kurze Erklärung, keine lange juristische Abhandlung.

Herzliche Grüße
Marta Blum'''),
E('25_Rueckfrage_Otto.eml', 'Kleinhausen Rechnungsnummer der Reinigung', '2026-09-19T17:25:00+02:00', 'Otto Freund <otto@freund.example>', 'Lotte Klar <lotte@kleinundklar.example>', '''Guten Tag Frau Klar,

in der Liste steht bei der Treppenhausreinigung die Nummer R-2025-71. Frau Fein hatte mir beim letzten Gespräch die Nummer R-2025-17 genannt. Sind das zwei Rechnungen oder ist nur etwas vertauscht worden? Der Betrag von 960 Euro entspricht den zwölf Monatsbeträgen, die wir vereinbart hatten.

Ansonsten habe ich keine Beanstandung. Die Tür schließt seit der kleinen Reparatur gut. Wenn Sie die Abrechnung neu verschicken, schreiben Sie bitte kurz dazu, welche Fassung wir zur Versammlung mitbringen sollen. Sonst sitze ich wieder mit dem falschen Ausdruck am Tisch.

Viele Grüße
Otto Freund'''),
E('26_Antwort_Verwaltung.eml', 'Kleinhausen ich gleiche die beiden Stellen ab', '2026-09-21T09:05:00+02:00', 'Lotte Klar <lotte@kleinundklar.example>', 'Marta Blum <marta@blum.example>', '''Guten Tag Frau Blum,

vielen Dank für Ihren Hinweis. Ich gleiche die Stromposition mit dem Beleg und dem Bankbuch ab. Herr Freund hat außerdem wegen der Rechnungsnummer der Reinigung gefragt. Auch diese Stelle nehme ich mir vor.

Ihre zwölf Monatsraten sind vollständig in unserer Buchhaltung angekommen. Ich melde mich mit einer kurzen Erläuterung, sobald die Durchsicht fertig ist. Die erste Fassung bleibt bis dahin als Entwurf in der Akte. Bitte veranlassen Sie aufgrund dieses Entwurfs noch nichts.

Freundliche Grüße
Lotte Klar'''),
D('27_Besprechungsnotiz.docx', 'Kurze Besprechung zur Abrechnung Kleinhausen', '22.09.2026', HV, 'Verwaltungsakte', '''Lotte Klar hat am 22. September um 16 Uhr mit Marta Blum im Büro gesprochen. Frau Blum möchte verstehen, wie ihre zwölf Monatsraten und die Rücklage in der Abrechnung zusammenhängen. Sie hat keine fehlende Zahlung geltend gemacht und keine Erstattung verlangt, bevor die Abrechnung geprüft ist.

Otto Freund hat telefonisch ergänzt, dass er die Rechnung der Reinigungsfirma wiederfinden möchte. Er vermutet eine vertauschte Ziffer in der Belegnummer. Den Jahrespreis stellt er nicht infrage. Beide Rückfragen sollen in einem gemeinsamen kurzen Begleittext erklärt werden. Die Einzelbriefe werden anschließend separat an die jeweiligen Eigentümer geschickt.

Die übrigen drei Eigentümer haben sich bislang nicht zur Abrechnung gemeldet. Es gibt keine weiteren offenen Sachfragen aus dem Haus. Zum Abrechnungsstichtag 31. Dezember 2025 weisen die Bankunterlagen 1.340,00 EUR auf dem Betriebskonto und 6.500,00 EUR auf dem Rücklagenkonto aus. Weitere Geldanlagen, Forderungen, Verbindlichkeiten oder wesentliche Vermögenspositionen hat die Durchsicht der Verwaltungsunterlagen zu diesem Stichtag nicht ergeben.

Lotte Klar stellt die Rechnungen, den Jahresbuchungsbestand und den Vorschussbeschluss für die Prüfung zusammen. Danach sollen eine einheitlich datierte Abrechnungsfassung, die Begleitbriefe und die Beschlussvorlage fertiggestellt werden. Die Einladung für den 20. November ist noch nicht versandt. Sie soll erst nach dieser Durchsicht verschickt werden.'''),
D('28_Beschlussvorlage_Entwurf.docx', 'Kleinhausen Beschlussvorlage zur Abrechnung 2025', '15.09.2026', HV, 'Unversandter Entwurf für die Versammlung am 20. November 2026', '''1. Vorgesehener Tagesordnungspunkt

Die Eigentümerversammlung soll über die Anpassung der beschlossenen Kostenvorschüsse für 2025 auf Grundlage der geprüften Jahresabrechnung entscheiden. Die Kontenübersichten und der Vermögensbericht werden den Eigentümern zur Information vorgelegt. Diese Vorlage wurde anhand der ersten Abrechnungsfassung vom 15. September erstellt. Vor dem Versand der Einladung ist sie mit dem Ergebnis der Belegprüfung abzugleichen.

2. Beschlusstext der ersten Fassung

Auf Grundlage der Einzelabrechnungen 2025 vom 15. September 2026 werden die für das Kalenderjahr 2025 beschlossenen Kostenvorschüsse für die Wohnungen WE01, WE02, WE03, WE04 und WE05 um jeweils 64,00 EUR herabgesetzt. Da die bisherigen Kostenvorschüsse vollständig gezahlt wurden, ergibt sich für jeden der fünf Eigentümer ein Guthaben von 64,00 EUR. Die Verwalterin wird beauftragt, die Guthaben innerhalb von vierzehn Tagen nach der Beschlussfassung aus dem Betriebskonto an die jeweiligen Eigentümer auszuzahlen. Die beschlossenen Beiträge zur Erhaltungsrücklage bleiben unverändert.

3. Stand der Vorbereitung

Über diesen Text wurde noch nicht abgestimmt. Er ist weder Teil einer versandten Einladung noch als Beschluss in die Beschlusssammlung aufgenommen. Die Verwaltung hält diese Ausgangsfassung in der Akte fest. Die endgültige Vorlage soll die nach der Prüfung maßgebliche Abrechnungsfassung eindeutig bezeichnen.'''),
E('29_Versand_Belege.eml', 'Kleinhausen die beiden gewünschten Jahresbelege', '2026-09-22T11:30:00+02:00', 'Lotte Klar <lotte@kleinundklar.example>', 'Marta Blum <marta@blum.example>', '''Guten Tag Frau Blum,

hier kommen der Jahresbeleg für den Allgemeinstrom und der Jahresbeleg der Reinigungsfirma. Frau Fein hat darin die zwölf Zahlungen zusammengefasst. Die Dateien stammen aus unserer Belegablage.

Ich habe Herrn Freund den Reinigungsbeleg ebenfalls geschickt. Falls Sie die übrigen Belege im Zusammenhang sehen möchten, können Sie sie bei unserem Termin im Büro durchblättern. Die Korrektur der Abrechnungsunterlagen folgt nach der Durchsicht.

Freundliche Grüße
Lotte Klar'''),
dict(file='30_Hausnotiz.txt', title='Notiz am Küchentisch von Marta Blum', date='22.09.2026', body='Lotte hat die Belege geschickt. Otto bringt zur Versammlung seine Lesebrille mit. Nora kann den Nachbarschaftsraum aufschließen, Emil stellt die Tische zusammen und Aylin bringt eine Kanne Kaffee. Freitag, 20. November, 18 Uhr ist bei allen vorgemerkt.\n\nIch möchte bei der Abrechnung nur wissen, was ich tatsächlich zurückbekomme und wo die Rücklage steht. Die Fenster im Treppenhaus sind frisch geputzt, und die Haustür fällt nicht mehr so laut ins Schloss. Für weitere Arbeiten hat gerade niemand einen Wunsch.'),
D('31_Vermoegensbericht.docx', 'Vermögensbericht Kleinhausen zum 31 Dezember 2025', '15.09.2026', HV, WEG, '''Zum 31. Dezember 2025 beträgt der Stand der Erhaltungsrücklage 6.500,00 EUR. Der Betrag liegt vollständig auf dem gesonderten Rücklagenkonto KH-R der Gemeinschaft. Der Anfangsbestand von 5.000,00 EUR wurde durch die im Jahr 2025 vollständig eingegangenen Rücklagenbeiträge von 1.500,00 EUR erhöht. Es gab keine Entnahmen, Zinsen oder Kontogebühren für dieses Konto.

Auf dem Betriebskonto KH-B stehen zum selben Stichtag 1.340,00 EUR zur Verfügung. Die beiden Bankguthaben betragen zusammen 7.840,00 EUR. Der Stand der Erhaltungsrücklage und das Guthaben des Rücklagenkontos beschreiben denselben Betrag; sie werden nicht doppelt als Vermögen addiert.

Alle für 2025 beschlossenen Vorschüsse sind gezahlt. Die Rechnungen des Jahres sind bezahlt. Es bestehen zum Stichtag keine weiteren Forderungen, Verbindlichkeiten, Darlehen oder wesentlichen Vermögensgegenstände der Gemeinschaft. Das Gebäude ist nicht als Bankvermögen der Gemeinschaft angesetzt. Die künftige Anpassung der Vorschüsse aufgrund der noch zu beschließenden Jahresabrechnung ist in diesem Stichtagsbericht nicht vorweggenommen.

Die Bankbestände lassen sich anhand der beiden Jahresübersichten und des vollständigen Buchungsbestands nachvollziehen. Dieser Bericht wird allen Eigentümern zusammen mit den Abrechnungsunterlagen zur Verfügung gestellt.

Lotte Klar'''),
]

assert len(documents) == 31
CASES = [dict(slug=SLUG, title='Kleinhausen', plugin='weg-hausverwaltung', intro='Fünf selbst genutzte Wohnungen, eine kleine Verwaltung und die erste Jahresabrechnung für 2025.', documents=documents, attachments={'23_Versand_Abrechnung.eml':['17_Gesamtabrechnung_Entwurf.docx','18_Einzelabrechnung_WE01.docx'], '29_Versand_Belege.eml':['12_Allgemeinstrom.docx','13_Treppenhausreinigung.docx']})]
