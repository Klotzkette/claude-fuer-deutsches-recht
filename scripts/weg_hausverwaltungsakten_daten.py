"""Vier eigenständige WEG-Lebensakten; keine Auswertung oder Musterlösung.

Fiktive Sachbelege, unveränderte MIME-Anhänge und unabhängige Rechenkontrollen.
Die erwarteten Tabellenwerte dienen allein der Bauprüfung und werden nicht exportiert.
"""
from decimal import Decimal


def D(file, title, date, sender, recipient, body, **extra):
    return dict(file=file, title=title, date=date, sender=sender, recipient=recipient, body=body.strip(), **extra)


def E(file, title, date, sender, recipient, body):
    return dict(file=file, title=title, date=date, **{'from': sender, 'to': recipient}, body=body.strip())


def T(file, title, date, body):
    return dict(file=file, title=title, date=date, body=body.strip())


def X(file, title, sheets):
    return dict(file=file, title=title, sheets=sheets)


def euro(value):
    return f'{Decimal(str(value)):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') + ' EUR'


PLUGIN = 'weg-hausverwaltung'
CASES = []
HV = 'Havel und Hof Hausverwaltung GmbH\nSachbearbeiterin Noura Selim, Berlin\nverwaltung@havelhof.example'
WEG1 = 'Gemeinschaft der Wohnungseigentümer Lindenhof 18\nLindenhof 18, Berlin'
OWNERS = [(1, 'Edeltraud Tüddel', 100, 'Selbstnutzung'), (2, 'Kian Yilmaz', 110, 'Vermietet'), (3, 'Kunigunde Wackernagel', 120, 'Selbstnutzung'), (4, 'Mirela Popescu', 120, 'Vermietet'), (5, 'Alwin Pfitzner', 130, 'Selbstnutzung'), (6, 'Asha Krüger', 130, 'Vermietet'), (7, 'Bodo Zuckermann', 140, 'Selbstnutzung'), (8, 'Noa Winter', 150, 'Vermietet')]
COSTS = [('Wasser und Abwasser', 3840, 'W-25-818', '07_Wasserrechnung.docx'), ('Müllentsorgung', 2880, 'M-25-180', '08_Muellrechnung.docx'), ('Gebäudeversicherung', 2160, 'GV-25-188', '09_Gebaeudeversicherung.docx'), ('Allgemeinstrom', 720, 'ST-25-991', '10_Stromrechnung.docx'), ('Treppenreinigung', 3600, 'R-25-144', '11_Reinigung.docx'), ('Hausmeister', 4800, 'HM-25-218', '12_Hausmeisterrechnung.docx'), ('Dachreparatur', 2400, 'D-25-512', '14_Dachreparatur.docx'), ('Verwaltung', 3840, 'V-25-118', '15_Verwalterhonorar.docx'), ('Kontoführung', 120, 'BK-25-118', '16_Bankentgelte.docx')]
assert sum(x[1] for x in COSTS) == 24360
owner_rows = []
for n, name, mea, use in OWNERS:
    owner_rows.append([n, name, mea, mea * .8, use, f'WE{n:02d}'])
advance_rows = []
for r, (n, name, mea, _) in enumerate(OWNERS, 2):
    advance_rows.append([n, name, mea * 2, round(mea * 2 / 3, 2), f"='Eigentum'!C{r}*32", mea * 32 - (320 if n == 4 else 0), f'=E{r}-F{r}'])
advance_rows.append(['Summe', '', '=SUM(C2:C9)', '=SUM(D2:D9)', '=SUM(E2:E9)', '=SUM(F2:F9)', '=SUM(G2:G9)'])
cost_rows = [[name, value, ref, file] for name, value, ref, file in COSTS]
cost_rows.append(['Summe', '=SUM(B2:B10)', '', ''])
bank_rows = [
    ['01.01.2025', 'Anfangsbestand Betrieb', 3000, 0, '=C2-D2', 'Kontoauszug Anfang'],
    ['31.12.2025', 'Hausgeldzahlungen Januar bis November', 29333.37, 0, '=E2+C3-D3', 'Zahlungsjournal 2025'],
    ['31.12.2025', 'Hausgeldzahlungen Dezember', 2346.63, 0, '=E3+C4-D4', 'Zahlungsjournal 2025'],
    ['31.12.2025', 'Ausgaben laut Kostenblatt', 0, 24360, '=E4+C5-D5', 'Belege 07 bis 16'],
    ['31.12.2025', 'Übertrag Rücklage', 0, 7920, '=E5+C6-D6', 'Kontoauszug Rücklage'],
]
# Die Monatsaufteilung der Bankübersicht stammt aus gerundeten Daueraufträgen;
# der Jahresabgleich ist maßgeblich, die einzelnen Dauerauftragsraten stehen im Journal.
documents = [
D('01_Auftrag_Abrechnung.docx', 'Abrechnung Lindenhof vor der Eigentümerversammlung', '18.09.2026', HV, 'Rechtsanwältin Friederike Morgen\nkanzlei@morgen.example', '''Sehr geehrte Frau Morgen,

bitte prüfen Sie die bereits versandten Abrechnungen für 2025 und erstellen Sie eine verständliche Antwort an Frau Popescu sowie eine belastbare Beschlussvorlage für die Versammlung am 22. Oktober. Acht Einheiten gehören acht verschiedenen Personen. Unsere frühere Buchhalterin hat die Zahlen exportiert, ich habe die Briefe am 8. September verschickt. Nach einer Rückfrage bin ich unsicher, ob die Spalte „Nachzahlung“ überall dasselbe enthält.

Frau Popescu hat im Dezember 2025 ein Hausgeld ausgelassen. Der Beirat findet außerdem die Hausmeisterrechnung zu pauschal. Die Dachreparatur wurde vom laufenden Konto bezahlt, die Rücklage blieb auf ihrem Konto. Die Reserve soll nicht noch einmal als Verbrauch in der Abrechnung erscheinen. Für die Vermietungen stellen wir auf Wunsch Unterlagen bereit; eine Mieterabrechnung ist nicht Bestandteil unseres laufenden Verwaltervertrags.

Ich brauche jetzt korrigierbare Einzelbriefe, eine Liste der noch benötigten Belege und einen eindeutigen Vorschlag, welche Fassung in der Versammlung behandelt wird. Bitte keine Zahlungsaufforderungen oder Einladungsänderungen ohne unsere Freigabe versenden. Die Originalauszüge liegen im Büro bereit. Frau Tüddel möchte die Unterlagen am 25. September einsehen; bitte berücksichtigen Sie, dass ich ihr dafür bereits einen Termin zugesagt habe.

Mit freundlichen Grüßen
Noura Selim'''),
D('02_Gemeinschaftsordnung.docx', 'Gemeinschaftsordnung Lindenhof 18', '17.05.2014', 'Gemeinschaft der Wohnungseigentümer Lindenhof 18', 'Ausfertigung für die Verwaltung', '''1. Einheiten und Beteiligung

Die Wohnanlage besteht aus acht Wohnungen. Die Miteigentumsanteile ergeben sich aus dem Einheitenverzeichnis und betragen zusammen 1.000 Tausendstel. Kellerabteile sind den Wohnungen zugeordnet; tragende Bauteile, Dach, Fassade und gemeinsame Leitungen gehören zum gemeinschaftlichen Eigentum. Die Einheiten werden ausschließlich zu Wohnzwecken genutzt.

2. Kostenverteilung

Die Kosten der gemeinschaftlichen Verwaltung und des gemeinschaftlichen Gebrauchs werden nach Miteigentumsanteilen verteilt, soweit keine gesetzlich zwingende oder wirksam beschlossene abweichende Verteilung gilt. In der Anlage besitzt jede Wohnung eine eigene Gasetagenheizung. Der Gasverbrauch der Wohnungen wird nicht durch die Gemeinschaft abgerechnet. Für Wasser bestehen keine wohnungsweisen Zähler; die Gemeinschaftskosten werden nach dem vorgenannten Schlüssel verteilt.

3. Vorschüsse und Erhaltungsrücklage

Die Eigentümer leisten die beschlossenen monatlichen Vorschüsse auf das Gemeinschaftskonto. Die im Wirtschaftsplan gesondert bezeichneten Rücklagenbeiträge sind auf einem getrennten Konto der Gemeinschaft anzulegen. Entnahmen erfolgen nur aufgrund eines Beschlusses oder einer anderweitig bestehenden gesetzlichen Befugnis. Kontoauszüge und Verwendungsnachweise sind zu den Verwaltungsunterlagen zu nehmen.

4. Unterlagen und Verwaltung

Die Verwaltung führt eine nach Jahren geordnete Belegablage. Auf Verlangen eines Eigentümers stimmt sie einen Termin zur Einsicht in die Verwaltungsunterlagen ab. Unterlagen über andere Eigentümer sind nicht für eine Veröffentlichung in Hauschats bestimmt. Die Beauftragung einer individuellen Mietverwaltung bedarf einer gesonderten Vereinbarung.

Diese Abschrift enthält die für den Abrechnungsvorgang einschlägigen Bestimmungen. Nach dem von der Verwaltung geführten Beschlussverzeichnis ist für 2025 keine Änderung der Kostenverteilung eingetragen.'''),
X('03_Eigentuemer_und_Vorschuesse.xlsx', 'Eigentümer und Vorschüsse 2025', [dict(name='Eigentum', headers=['Einheit', 'Eigentümer', 'MEA von 1000', 'Wohnfläche m²', 'Nutzung', 'Kontokennung'], widths=[12,32,17,17,22,18], formats={'A':'0','C':'0','D':'0.00'}, rows=owner_rows, expected={'C2':100,'D9':120}), dict(name='Vorschuesse', headers=['Einheit','Eigentümer','Kosten monatlich EUR','Rücklage monatlich EUR','Soll Jahr EUR','Ist Jahr EUR','Offen EUR'], widths=[10,30,18,18,18,18,16], formats={c:'#,##0.00' for c in 'CDEFG'}, rows=advance_rows, expected={'E10':32000,'F10':31680,'G10':320}, perturbations=[dict(input='F5',value=3840,output='G10',expected=0)])]),
D('04_Wirtschaftsplan_Beschluss.docx', 'Beschluss über die Vorschüsse für 2025', '21.11.2024', WEG1, 'Niederschrift der Eigentümerversammlung', '''Die Eigentümer beschließen für das Kalenderjahr 2025 Kostenvorschüsse von insgesamt 24.000 EUR und Beiträge zur Erhaltungsrücklage von insgesamt 8.000 EUR. Beide Beträge werden nach Miteigentumsanteilen verteilt. Die in der Anlage ausgewiesenen Monatsraten sind zum dritten Werktag jedes Monats fällig. Die Jahresbeträge je Einheit sind maßgeblich; Rundungsdifferenzen der Monatsraten werden mit der Dezemberrate ausgeglichen.

Für Wohnung 4 entfallen jährlich 2.880 EUR auf die laufenden Kosten und 960 EUR auf die Rücklage. Die Monatsrate beträgt dort 320 EUR. Für die übrigen Einheiten gelten die im Vorschussverzeichnis aufgeführten anteiligen Beträge. Für diesen Beschluss stimmen alle acht Eigentümer; Gegenstimmen und Enthaltungen werden nicht abgegeben.

Die Dachrinnenstelle über dem Hof wird im Frühjahr untersucht. Über eine etwa erforderliche Reparatur soll nach Vorlage eines Angebots gesondert entschieden werden. Der Wirtschaftsplan ermächtigt nicht zur Verwendung von Rücklagemitteln für einen bestimmten Auftrag.

Versammlungsleiterin Noura Selim; Beiratsvorsitzender Alwin Pfitzner; Eigentümerin Edeltraud Tüddel. Die Niederschrift wurde von den Genannten am 25.11.2024 unterzeichnet.'''),
X('05_Buchhaltung_2025.xlsx', 'Buchhaltung Lindenhof 2025', [dict(name='Kosten', headers=['Kostenart','Bezahlt EUR','Belegnummer','Unterlage'], widths=[31,18,18,48], formats={'B':'#,##0.00'}, rows=cost_rows, expected={'B11':24360}, perturbations=[dict(input='B8',value=0,output='B11',expected=21960)]),dict(name='Betriebskonto',headers=['Datum','Buchung','Eingang EUR','Ausgang EUR','Saldo EUR','Quelle'],widths=[17,35,17,17,18,32],formats={c:'#,##0.00' for c in 'CDE'},rows=bank_rows,expected={'E6':2400},perturbations=[dict(input='C4',value=2666.63,output='E6',expected=2720)]),dict(name='Ruecklage',headers=['Datum','Buchung','Eingang EUR','Ausgang EUR','Saldo EUR'],widths=[20,47,19,19,20],formats={c:'#,##0.00' for c in 'CDE'},rows=[['01.01.2025','Anfangsbestand',40000,0,'=C2-D2'],['31.12.2025','Übertrag aus Betrieb',7920,0,'=E2+C3-D3'],['31.12.2025','Zinsgutschrift',80,0,'=E3+C4-D4']],expected={'E4':48000},perturbations=[dict(input='C3',value=8000,output='E4',expected=48080)])]),
D('06_Ruecklagenkonto_Bankauszug.docx', 'Jahresübersicht Rücklagenkonto 2025', '05.01.2026', 'Bürgerbank an der Havel\nKundenservice Gemeinschaftskonten\nservice@buergerbank.example', WEG1, '''Konto: Rücklage Lindenhof, interne Kontonummer RL-118. Kontoinhaberin ist die Gemeinschaft der Wohnungseigentümer Lindenhof 18. Diese Übersicht enthält aus Gründen der internen Ablage keine Zahlungsadresse.

Der Bestand am 01.01.2025 betrug 40.000,00 EUR. Im Kalenderjahr wurden vom Betriebskonto insgesamt 7.920,00 EUR übertragen. Entnahmen sind nicht gebucht. Am 31.12.2025 wurden 80,00 EUR Zinsen gutgeschrieben. Der Schlussbestand am 31.12.2025 beträgt 48.000,00 EUR.

Die Überträge stimmen mit den von der Verwaltung veranlassten Buchungen überein. Die Bank hat nicht geprüft, ob alle Eigentümer ihre beschlossenen Beiträge geleistet haben. Eine Sollstellung von 8.000 EUR ist keine Bankbuchung. Für einzelne Zahlungsaufträge sind die monatlichen Auszüge maßgeblich.'''),
]
invoice_info = [
('07_Wasserrechnung.docx','Wasser und Abwasser 2025','Wasserwerk Kieztal','W-25-818',3840,'Trinkwasser 2.160 EUR einschließlich 7 Prozent Umsatzsteuer; Abwassergebühr 1.680 EUR ohne Umsatzsteuer. Der Hauptzähler L18-44 wurde am 02.01.2025 mit 12.100 m³ und am 02.01.2026 mit 12.940 m³ abgelesen. Abgerechnet werden 840 m³. Die hier ausgewiesenen Jahreskosten enthalten keine wohnungsweisen Verbräuche.','Die zwölf Abschläge und die Ausgleichszahlung sind vollständig eingegangen. Ein Guthaben besteht nicht.'),
('08_Muellrechnung.docx','Entsorgungsentgelte 2025','Sauberer Hof Entsorgung','M-25-180',2880,'Für die regelmäßige Leerung der Gemeinschaftsbehälter werden für Januar bis Dezember 2025 insgesamt 2.880 EUR berechnet. Sperrmüllabholungen oder private Entrümpelungen sind nicht enthalten. Die Abrechnung erfolgt als öffentlich-rechtliche Gebühr ohne gesonderten Umsatzsteuerausweis.','Der Jahresbetrag wurde mit vier Raten zu je 720 EUR beglichen.'),
('09_Gebaeudeversicherung.docx','Beitragsrechnung Gebäudeversicherung 2025','Havel Schutz Versicherung','GV-25-188',2160,'Versichert ist das Gebäude Lindenhof 18. Der Zeitraum läuft vom 01.01. bis 31.12.2025. Der Bruttobeitrag von 2.160 EUR enthält Versicherungssteuer und keine Umsatzsteuer. Privater Hausrat der Bewohner ist nicht Gegenstand dieses Vertrags.','Der Beitrag wurde am 06.01.2025 vom Betriebskonto eingezogen. Eine Schadenleistung wurde 2025 nicht erbracht.'),
('10_Stromrechnung.docx','Allgemeinstrom 2025','Kiezstrom Energie GmbH','ST-25-991',720,'Der Zähler AL18-09 versorgt Treppenhauslicht, Kellerlicht und die gemeinschaftliche Klingelanlage. Die Jahresabrechnung für 2025 beträgt 605,04 EUR netto zuzüglich 114,96 EUR Umsatzsteuer. Der Verbrauch beträgt 1.800 kWh. Die Wohnungshauptzähler sind nicht erfasst.','Die geleisteten Abschläge entsprechen dem Bruttobetrag. Eine Restforderung besteht nicht.'),
('11_Reinigung.docx','Treppenhausreinigung 2025','Blitzblank Berta e.K.','R-25-144',3600,'Abgerechnet werden 50 ausgeführte Reinigungen des Treppenhauses einschließlich Geländer und Eingangsbereich. Zwei vereinbarte Feiertagswochen wurden mit einer zusätzlichen Reinigung in der Folgewoche ausgeglichen. Das Jahreshonorar beträgt 3.025,21 EUR netto und 574,79 EUR Umsatzsteuer.','Die monatlichen Rechnungen zu 300 EUR brutto sind beglichen. Diese Jahresbestätigung fordert keine zweite Zahlung an.'),
('12_Hausmeisterrechnung.docx','Jahresabrechnung Hausmeisterdienst 2025','Hausdienst Kuno Knarzkopf','HM-25-218',4800,'Für die Betreuung der Anlage werden 4.033,61 EUR netto zuzüglich 766,39 EUR Umsatzsteuer berechnet. Die Pauschale umfasst Kontrollgänge, Bereitstellen der Müllbehälter, kleinere Reparaturen und die monatliche Ablage von Handwerkerterminen. Unsere ursprüngliche Rechnung unterscheidet diese Bestandteile nicht betragsmäßig.','Die monatlichen zwölf Raten zu 400 EUR brutto sind bezahlt. Auf die Anfrage der Verwaltung können wir eine Tätigkeitsaufstellung nachreichen.'),
('14_Dachreparatur.docx','Rechnung über die Reparatur der Dachrinne','Dach und Drauf Dachbau GmbH','D-25-512',2400,'Am 15.05.2025 wurden drei laufende Meter korrodierte Dachrinne am Hofanschluss ersetzt und der betroffene Ablauf neu abgedichtet. Abgerechnet werden 2.016,81 EUR netto zuzüglich 383,19 EUR Umsatzsteuer. Wiederkehrende Reinigung ist nicht enthalten. Der Auftrag entspricht dem angenommenen Angebot vom 20.04.2025.','Die Zahlung ging am 28.05.2025 vom Betriebskonto Lindenhof ein. Die Verwaltung benannte dieses Konto ausdrücklich als Zahlungskonto.'),
('15_Verwalterhonorar.docx','Jahresbestätigung Verwalterhonorar 2025','Havel und Hof Hausverwaltung GmbH','V-25-118',3840,'Die Grundvergütung beträgt je Wohnung monatlich 40 EUR brutto. Acht Wohnungen und zwölf Monate ergeben 3.840 EUR brutto, darin 3.226,89 EUR netto und 613,11 EUR Umsatzsteuer. Die Grundvergütung erfasst Gemeinschaftsverwaltung, eine ordentliche Versammlung und die gemeinschaftliche Abrechnung.','Die zwölf Monatsbeträge sind bezahlt. Eine individuelle Betriebskostenabrechnung für einen Mietvertrag ist nicht umfasst.'),
('16_Bankentgelte.docx','Entgeltabrechnung Gemeinschaftskonto 2025','Bürgerbank an der Havel','BK-25-118',120,'Für das Betriebskonto wurden zwölf monatliche Entgelte von jeweils 10 EUR belastet. Die Kontoführung ist umsatzsteuerfrei. Der Rücklagenkontovertrag enthält im Jahr 2025 kein zusätzliches Entgelt.','Die Belastungen sind in der Jahressumme der Betriebskontoausgänge enthalten. Es wurde kein Entgelt vom privaten Konto eines Eigentümers eingezogen.'),
]
for filename,title,vendor,reference,amount,performance,payment in invoice_info:
    documents.append(D(filename,title,'31.12.2025',f'{vendor}\nAbrechnung Lindenhof 18\nrechnung@lieferant.example',WEG1,f'''Sehr geehrte Damen und Herren,

{performance}

Der Bruttobetrag für den bezeichneten Leistungszeitraum beträgt {euro(amount)}. Die Rechnungsnummer lautet {reference}. Die Leistung wurde für die Gemeinschaft am Objekt Lindenhof 18 erbracht. Die Abrechnung betrifft ausschließlich die vorstehend genannten Leistungen.

{payment}

Bitte führen Sie Rückfragen unter Angabe der Rechnungsnummer an unsere Buchhaltung. Ein Austausch des Dokuments soll erst nach Abstimmung erfolgen; die ursprüngliche Rechnung bleibt in unserer Ablage erhalten.''',reference=reference))
documents.append(D('13_Hausmeister_Leistungsnachweis.docx','Tätigkeitsnachweis Hausdienst 2025','31.12.2025','Hausdienst Kuno Knarzkopf',WEG1,'''Die Wochenzettel nennen 180 Stunden für Mülltonnen und Sichtkontrollen, 45 Stunden für das Einstellen von Türen, das Ersetzen einzelner Leuchten und ähnliche Arbeiten sowie 15 Stunden für Terminabstimmung und Ablage. Der kalkulatorische Satz für diese Jahresauswertung beträgt 20 EUR brutto je Stunde. Der Gesamtbetrag von 4.800 EUR stimmt mit der bezahlten Jahrespauschale überein.

Bei den 45 Stunden sind Arbeits- und Materialanteile nicht getrennt erfasst. Zwei Leuchten wurden vollständig ersetzt, an anderen Tagen wurden nur Leuchtmittel gewechselt. Die Unterlagen enthalten keine wohnungsweisen Tätigkeiten. Die 15 Stunden betreffen Termine der Verwaltung und keine Reinigung.

Diese Aufstellung wurde zunächst für unsere eigene Nachkalkulation erstellt. Sie ersetzt nicht die Rechnung. Kuno Knarzkopf hat die Angaben am 31.12.2025 aus den Wochenzetteln übertragen. Die Wochenzettel liegen im Büro des Hausdienstes und können nach Terminvereinbarung bereitgestellt werden.'''))
documents.append(D('17_Gesamtabrechnung_Entwurf.docx','Jahresabrechnung 2025 Fassung vom 6 September','06.09.2026',HV,WEG1,'''1. Zahlungen und Konten

Das Betriebskonto beginnt mit 3.000 EUR. Im Jahr 2025 gingen 31.680 EUR Hausgeld ein. Die Ausgaben für das Gebäude und die Verwaltung betragen 24.360 EUR; auf das Rücklagenkonto wurden 7.920 EUR überwiesen. Der Schlussbestand auf dem Betriebskonto beträgt 2.400 EUR. Die Rücklage stieg von 40.000 EUR durch Beiträge von 7.920 EUR und Zinsen von 80 EUR auf 48.000 EUR.

2. Kostenverteilung

Die 24.360 EUR werden nach 1.000 Miteigentumsanteilen verteilt. Die Vorschusszahlungen werden nach dem Export der Buchhaltung gegengerechnet. Der Export setzt bei Wohnung 4 für laufende Kosten 2.640 EUR statt des Jahresplanwerts ein. Die Liste weist deshalb Nachzahlungen von zusammen 600 EUR aus. Rücklagenbeiträge werden in diesem Abschnitt nicht als Gebäudekosten mitverteilt.

3. Stand der Unterlagen

Die Dachreparatur wurde im Mai vom Betriebskonto bezahlt. Eine Entnahme aus der Rücklage ist nicht gebucht. Der Hausmeister hat die Tätigkeitsnachweise noch nicht nachgereicht. Diese Fassung wurde von der Sachbearbeitung erstellt und dem Beirat zur Prüfung überlassen; eine Beschlussfassung liegt noch nicht vor.

Noura Selim'''))
for n,name,mea,use in OWNERS:
    share = Decimal(24360) * Decimal(mea) / 1000
    paid = Decimal(mea) * 24 - (240 if n == 4 else 0)
    diff = share - paid
    reserve = Decimal(mea) * 8 - (80 if n == 4 else 0)
    documents.append(D(f'{17+n:02d}_Einzelabrechnung_WE{n:02d}.docx',f'Jahresabrechnung 2025 Wohnung {n}','06.09.2026',HV,f'{name}\nEigentum Wohnung {n}, Lindenhof 18',f'''Sehr geehrte Eigentümerin, sehr geehrter Eigentümer,

Ihre Wohnung ist mit {mea} von 1.000 Miteigentumsanteilen an der Anlage beteiligt. Die gemeinschaftlichen Jahreskosten von 24.360 EUR ergeben für Ihre Einheit {euro(share)}. In der Buchhaltung sind für laufende Kosten {euro(paid)} als Zahlung berücksichtigt. Daraus weist unser vorliegender Export eine Nachzahlung von {euro(diff)} aus. Der Betrag soll Gegenstand der Beschlussfassung am 22. Oktober sein und ist mit diesem Entwurf noch nicht neu angefordert.

Auf die Erhaltungsrücklage wurden für Ihre Einheit im Jahr 2025 {euro(reserve)} gezahlt. Der anteilige Jahresplanwert beträgt {euro(Decimal(mea)*8)}. Die Rücklage ist in der vorstehenden Kostensumme nicht enthalten. Die vollständigen Gemeinschaftsbestände entnehmen Sie bitte der Gesamtabrechnung.

Die Kosten bestehen aus Wasser, Müll, Gebäudeversicherung, Allgemeinstrom, Treppenreinigung, Hausmeister, Dachreparatur, Verwaltung und Kontoführung. Alle Positionen wurden nach Miteigentumsanteilen verteilt. Ob einzelne Bestandteile gegenüber einem Mieter abzurechnen sind, ist nicht Gegenstand dieses Schreibens. Bitte reichen Sie Rückfragen möglichst vor der Versammlung ein.

Mit freundlichen Grüßen
Noura Selim'''))
documents.extend([
E('26_Versand_Abrechnung.eml','Lindenhof: Ihre Abrechnung für 2025','2026-09-08T11:34:00+02:00','Noura Selim <verwaltung@havelhof.example>','Mirela Popescu <mirela@popescu.example>','''Sehr geehrte Frau Popescu,

anbei erhalten Sie die Gesamtabrechnung und den Export für Ihre Wohnung 4. Die Abrechnung wird auf der Versammlung behandelt. Eine Einladung mit den übrigen Tagesordnungspunkten folgt gesondert. Bitte gleichen Sie die Angaben mit Ihren Zahlungen ab. Für die Belegeinsicht stimmen wir gern einen Termin ab.

Mit freundlichen Grüßen
Noura Selim'''),
E('27_Popescu_Rueckfrage.eml','Re: Lindenhof: Warum 283,20 Euro und nochmals 320 Euro?','2026-09-10T08:19:00+02:00','Mirela Popescu <mirela@popescu.example>','Noura Selim <verwaltung@havelhof.example>','''Liebe Frau Selim,

auf meiner Abrechnung stehen 283,20 EUR. Zugleich fordert Ihre Zahlungserinnerung weiter 320 EUR aus Dezember 2025. Mein Dauerauftrag war nach dem Bankwechsel wirklich ausgefallen; das bestreite ich nicht. Aber wird damit nicht ein Teil zweimal verlangt? Im Wirtschaftsplan stehen für laufende Kosten doch 2.880 EUR für mich.

Die 320 EUR habe ich heute überwiesen. Bitte sagen Sie mir, wofür die Zahlung jetzt gebucht wird. Mein Mieter hat schon gefragt, ob die Dachreparatur auf ihn zukommt. Ich möchte ihm noch nichts Falsches schicken.

Herzliche Grüße
Mirela Popescu'''),
D('28_Beiratsnotiz.docx','Notizen aus der Belegprüfung am 12 September','12.09.2026','Alwin Pfitzner und Edeltraud Tüddel\nVerwaltungsbeirat',HV,'''Wir haben am 12.09.2026 die Jahresunterlagen im Büro angesehen. Die Summe der neun Kostenpositionen lässt sich mit den vorgelegten Zahlungsbestätigungen auf 24.360 EUR abstimmen. Das Rücklagenkonto zeigt 48.000 EUR. Den Übertrag von 7.920 EUR haben wir auf beiden Konten gefunden. Die anfängliche mündliche Angabe „8.000 eingezahlt“ war gerundet und stimmt mit dem Bankbestand nicht überein.

Bei Wohnung 4 ist die offene Dezemberrate in der Eigentümerkontokarte und außerdem teilweise in der Spalte Nachzahlung enthalten. Uns fehlt eine Erklärung, ob die Versammlung darüber doppelt beschließen soll. Wir möchten, dass die Darstellung vor der Einladung berichtigt oder jedenfalls verständlich getrennt wird.

Die Hausmeisterrechnung enthält auch Reparaturen und Ablagearbeit. Für die WEG-Gesamtausgabe ist der volle bezahlte Betrag vorhanden. Für Bescheinigungen und Vermieterunterlagen benötigen wir die tatsächliche Aufteilung. Eine vorbehaltlose Empfehlung zur Beschlussfassung haben wir deshalb noch nicht abgegeben. Frau Selim wird uns die nächste Fassung mit sichtbarem Datum zusenden.'''),
E('29_Anfrage_Hausmeister.eml','HM-25-218: Bitte Tätigkeiten aufteilen','2026-09-12T14:05:00+02:00','Noura Selim <verwaltung@havelhof.example>','Kuno Knarzkopf <kuno@hausdienst.example>','''Guten Tag Herr Knarzkopf,

bitte senden Sie uns Ihre Jahresaufstellung zu den Kontrollgängen, Reparaturen und Büroarbeiten. Auf der Rechnung steht nur die Pauschale von 4.800 EUR. Wir benötigen keine neue Rechnung mit einem anderen Gesamtbetrag, sondern eine nachvollziehbare Zuordnung. Bitte erläutern Sie auch, was mit den ersetzten Leuchten gemeint ist.

Viele Grüße
Noura Selim'''),
E('30_Antwort_Hausmeister.eml','Re: HM-25-218 Tätigkeitsnachweis','2026-09-14T09:22:00+02:00','Kuno Knarzkopf <kuno@hausdienst.example>','Noura Selim <verwaltung@havelhof.example>','''Guten Morgen Frau Selim,

anbei die Jahresaufstellung. Die 180 Stunden ergeben kalkulatorisch 3.600 EUR, die 45 Stunden 900 EUR und die 15 Stunden 300 EUR. Das sind keine zusätzlichen Forderungen. Bei zwei der Leuchten habe ich das komplette Gehäuse ausgetauscht. Den Materialanteil bekomme ich aus der Jahrespauschale nicht ohne die einzelnen Einkaufsbelege heraus.

Die Frau in Wohnung 3 hat übrigens recht: Das Putzen der Treppe war nicht meine Leistung, dafür kam Berta. Ich habe nur die Behälter bewegt und die Anlagen angesehen. Bitte nicht zweimal als Reinigung bezeichnen.

Freundliche Grüße
Kuno Knarzkopf'''),
T('31_Beirat_Chat.txt','Ausschnitt aus dem Beiratschat','15.09.2026','''15.09.2026 18:42 Edeltraud: Im Flur heißt es schon wieder, die Verwaltung hätte 80 Euro verloren.
15.09.2026 18:44 Alwin: Die 80 fehlen nicht auf dem Bankkonto. Die Monatsrate aus Wohnung 4 war noch offen.
15.09.2026 18:45 Edeltraud: Dann bitte genau so erklären, ohne Kontodaten von Mirela an alle zu schicken.
15.09.2026 18:47 Noura: Ihre Zahlung kam inzwischen. Ich schicke morgen den Buchungsvermerk, keine Kontoauszüge in den Chat.
15.09.2026 18:49 Alwin: Und bitte Fassung zwei deutlich anders nennen. Bei mir heißen beide Anhänge Abrechnung_final.'''),
D('32_Einladung_Entwurf.docx','Einladung zur Eigentümerversammlung am 22 Oktober','16.09.2026',HV,'Eigentümerinnen und Eigentümer Lindenhof 18', '''Sehr geehrte Damen und Herren,

wir laden Sie zur Eigentümerversammlung am 22.10.2026 um 18.30 Uhr in den Gemeinschaftsraum des Nachbarschaftshauses am Lindenhof ein. Die Tagesordnung umfasst die Feststellung der Teilnahme, den Bericht der Verwaltung, die Beschlussfassung über Nachschüsse oder die Anpassung der beschlossenen Vorschüsse auf Grundlage der Jahresabrechnung 2025 sowie den Wirtschaftsplan 2027.

Die bisher übersandten Einzelabrechnungen werden derzeit anhand der Beiratsrückfragen geprüft. Die endgültige Fassung soll mit der Einladung bereitgestellt werden. Diese im Verwaltungsordner gespeicherte Einladung ist noch nicht versandt. Der Beschlussvorschlag verweist bislang auf die Fassung vom 6. September; dieser Verweis ist vor dem Versand abzugleichen.

Für die Einsicht in die Belege steht am 25.09.2026 ab 10 Uhr ein Termin im Verwaltungsbüro bereit. Bitte melden Sie sich an, damit wir die Unterlagen bereitlegen können. Wer verhindert ist, kann einen weiteren Termin abstimmen.

Mit freundlichen Grüßen
Noura Selim'''),
D('33_Beschlussvorlage_Arbeitsfassung.docx','Beschlussvorlage Jahresabrechnung 2025','16.09.2026',HV,'Interne Vorbereitung der Eigentümerversammlung', '''Die Wohnungseigentümer beschließen die in den Einzelabrechnungen vom 06.09.2026 ausgewiesenen Nachzahlungen von insgesamt 600 EUR. Die Zahlung soll vier Wochen nach der Versammlung fällig werden. Die Rückstände aus dem Wirtschaftsplan bleiben daneben fällig.

Die Hausverwaltung stellt diese Formulierung zur internen Abstimmung mit dem Beirat bereit. Eine Abstimmung der Eigentümer ist nicht erfolgt. Frau Selim hat die Vorlage am 16.09.2026 aus dem früheren Textbaustein übernommen; sie ist wegen der offenen Rückfrage zu Wohnung 4 noch nicht für den Einladungsversand freigegeben.'''),
D('34_Ueberweisungsbestaetigung_Popescu.docx','Überweisung Hausgeld Dezember 2025','10.09.2026','Mirela Popescu\nAusdruck aus ihrem Zahlungsjournal',HV,'''Ausführung am 10.09.2026 um 08.01 Uhr. Zahlungsempfängerin: Gemeinschaft der Wohnungseigentümer Lindenhof 18. Betrag: 320,00 EUR. Verwendungszweck: WE04 Hausgeld Dezember 2025, laufende Kosten 240 EUR und Rücklage 80 EUR.

Der Auftrag ist im Onlinebanking als ausgeführt markiert. Die Darstellung zeigt die internen Kontobezeichnungen Privat-Popescu und WEG-Lindenhof. Eine vollständige IBAN ist in diesem Ausdruck nicht enthalten. Frau Popescu hat den Ausdruck am selben Morgen an Frau Selim weitergeleitet.

Diese Überweisung betrifft nicht die neue Abrechnung für 2025 und enthält keine Erklärung zur Anerkennung der dort ausgewiesenen Nachzahlung.'''),
E('35_Buchung_Nachzahlung.eml','WE04: Eingang 320 EUR am 11. September','2026-09-16T11:02:00+02:00','Oskar Pudel <buchhaltung@havelhof.example>','Noura Selim <verwaltung@havelhof.example>','''Hallo Noura,

die 320 EUR wurden am 11. September 2026 gutgeschrieben. Ich habe sie mit dem angegebenen Zweck auf die alte Dezemberforderung gebucht: 240 EUR Kosten und 80 EUR Rücklage. Das verändert den Bankbestand 2026, nicht den Schlussbestand zum 31. Dezember 2025. Den Rücklagenübertrag für die 80 EUR habe ich heute ausgelöst.

Im Eigentümerkonto ist die Dezemberforderung jetzt ausgeglichen. Die schon verschickte Abrechnung bleibt aber unverändert im Archiv. Ich kann die Vorfassung nicht einfach durch eine neue Datei unter demselben Namen ersetzen, weil Frau Popescu sie bereits hat.

Viele Grüße
Oskar'''),
E('36_Auftrag_Fassung_zwei.eml','Lindenhof: Bitte korrigierte Unterlagen zusammenstellen','2026-09-18T16:07:00+02:00','Noura Selim <verwaltung@havelhof.example>','Friederike Morgen <kanzlei@morgen.example>','''Sehr geehrte Frau Morgen,

Sie erhalten ergänzend die Rückmeldung der Buchhaltung und den Beiratsvermerk. Bitte entwerfen Sie eine persönliche Antwort an Frau Popescu, die überarbeitete Beschlussformulierung und die dazu passenden Zahlen je Wohnung. Die Eigentümer sollen erkennen, welche Fassung ersetzt wird und was sich verändert. Eine abstrakte Erläuterung allein reicht uns nicht, weil die Einladung jetzt vorbereitet werden muss.

Bitte trennen Sie außerdem die interne Gemeinschaftsabrechnung von der Unterlage, die vermietende Eigentümer eventuell für ihre Mieter brauchen. Die Hausmeisteraufteilung möchte ich nicht ungeprüft als „voll umlagefähig“ bescheinigen.

Mit freundlichen Grüßen
Noura Selim'''),
])
assert len(documents) == 36
CASES.append(dict(slug='weg-lindenhof-jahresabrechnung-2025',title='Lindenhof und die zweite Abrechnungsfassung',plugin=PLUGIN,date='18.09.2026',client='Havel und Hof Hausverwaltung GmbH für die Gemeinschaft Lindenhof 18',summary='Acht Eigentümer erhalten ihre Abrechnung. Eine ausgefallene Dezemberrate, eine gemischte Hausmeisterrechnung und zwei ähnlich benannte Fassungen bringen Beirat und Verwaltung ins Gespräch.',assignment='Die Abrechnung anhand der Originalbelege prüfen, erforderliche Rückfragen stellen und die Einzelunterlagen, eine Antwort an die betroffene Eigentümerin und die Beschlussvorlage bearbeiten. Vorfassungen und Änderungen nachvollziehbar auseinanderhalten.',documents=sorted(documents,key=lambda d:d['file']),attachments={'26_Versand_Abrechnung.eml':['17_Gesamtabrechnung_Entwurf.docx','21_Einzelabrechnung_WE04.docx'],'30_Antwort_Hausmeister.eml':['13_Hausmeister_Leistungsnachweis.docx'],'36_Auftrag_Fassung_zwei.eml':['28_Beiratsnotiz.docx','35_Buchung_Nachzahlung.eml']}))

WEG2 = 'Gemeinschaft der Wohnungseigentümer Spreebogen 7\nSpreebogen 7, Berlin'
costs2 = [('Wasser',2880,'05_Wasser.docx'),('Müll',1920,'06_Muell.docx'),('Gebäudeversicherung',2112,'07_Versicherung.docx'),('Reinigung',2880,'08_Reinigung.docx'),('Hausmeister',2880,'09_Hausmeister.docx'),('Allgemeinstrom',1056,'10_Allgemeinstrom.docx'),('Heizung',17280,'11_Gasrechnung.docx'),('Verwaltung',3840,'15_Verwalterentgelt.docx'),('Dachreparatur',6000,'16_Dachrechnung.docx'),('Bankkosten',480,'03_WEG_Jahresabrechnung.docx'),('Rücklagenbeitrag',8000,'17_Ruecklagennachweis.docx')]
assert sum(x[1] for x in costs2) == 49328
rows2 = [[name,amount,8,f'=B{r}/C{r}',source] for r,(name,amount,source) in enumerate(costs2,2)]
rows2 += [['Summe','=SUM(B2:B12)','', '=SUM(D2:D12)','Export für Vermieter vom 15. September']]
payments2 = [['05.'+f'{m:02d}'+'.2025',f'Vorauszahlung {m:02d}/2025',280,'Mietkonto N-04'] for m in range(1,13)]
payments2.append(['31.12.2025','Summe','=SUM(C2:C13)',''])
docs2 = [
D('01_Auftrag_Vermieterabrechnung.docx','Abrechnung für Frau Nair und Herrn Biber','25.09.2026',HV,'Rechtsanwältin Friederike Morgen', '''Sehr geehrte Frau Morgen,

Herr Ottfried Knöpfle vermietet Wohnung 4 im Spreebogen 7 an Leela Nair und Juri Biber. Er hat unseren WEG-Export in einen eigenen Brief eingefügt und fordert nun 2.806 EUR nach. Die Mieter fragen nach Belegen und halten den Betrag für falsch. Herr Knöpfle meint, wir hätten ihm eine mietrechtlich fertige Abrechnung gegeben. Unser Verwaltervertrag betrifft nur die Gemeinschaft; im September hat er uns erstmals wegen seiner Mieter geschrieben.

Bitte prüfen Sie, welche Unterlagen wir gegenüber Herrn Knöpfle bereitstellen sollen und wie eine getrennte, nachvollziehbare Mietabrechnung aussehen müsste. Für den Vermieter bitten wir um einen überarbeitbaren Abrechnungsentwurf und einen individuellen Antwortbrief. Dazu hat er uns am 24. September ausdrücklich beauftragt. Der Versand erfolgt erst nach seiner Freigabe. Bei fehlenden Tatsachen bitte gezielt nachfragen.

Wir haben Heizdaten und CO₂-Angaben nachgefordert. Die Gemeinschaft hat eine zentrale Gasheizung, alle acht Wohnungen sind gleich groß. Die Dachrechnung ist eine einmalige Reparatur. Ein unterschriebener gesonderter Beschluss zur Verteilung von Mietbetriebskosten existiert nicht. Die Mieter haben für 2025 monatlich 280 EUR vorausgezahlt.

Mit freundlichen Grüßen
Noura Selim'''),
D('02_Mietvertrag.docx','Wohnraummietvertrag Spreebogen Wohnung 4','12.11.2023','Ottfried Knöpfle, Vermieter\nottfried@knoepfle.example','Leela Nair und Juri Biber, Mieter\nleela@nair.example', '''1. Wohnung und Mietbeginn

Ottfried Knöpfle vermietet Leela Nair und Juri Biber die Wohnung 4 im zweiten Obergeschoss des Hauses Spreebogen 7 in Berlin. Die Wohnung umfasst drei Zimmer, Küche, Bad, Flur und Balkon mit einer vereinbarten Wohnfläche von 80 m². Das zugeordnete Kellerabteil darf mitbenutzt werden. Das Mietverhältnis beginnt am 01.01.2024 und läuft auf unbestimmte Zeit. Beide Mieter haften für ihre vertraglichen Zahlungspflichten als Gesamtschuldner.

2. Miete und Vorauszahlungen

Die monatliche Nettokaltmiete beträgt 1.050 EUR. Zusätzlich werden monatlich 280 EUR als Vorauszahlung auf Betriebskosten einschließlich Heiz- und Warmwasserkosten geleistet. Der Gesamtbetrag von 1.330 EUR ist monatlich spätestens zum dritten Werktag auf das benannte Mietkonto zu entrichten. Abgerechnet wird jährlich nach dem Kalenderjahr; geleistete Vorauszahlungen werden angerechnet.

3. Vereinbarte Betriebskosten

Die Mieter tragen die umlagefähigen Betriebskosten nach der Betriebskostenverordnung, soweit sie für das Gebäude tatsächlich anfallen. Vereinbart sind insbesondere Wasser und Entwässerung, Müllentsorgung, Gebäudereinigung, Allgemeinstrom, Sach- und Haftpflichtversicherung sowie umlagefähige Hauswartleistungen. Verwaltungs-, Instandhaltungs- und Instandsetzungskosten sind nicht als Betriebskosten vereinbart. Sonstige Betriebskosten werden durch diesen Vertrag nicht zusätzlich benannt.

4. Verteilung und Heizkosten

Soweit keine zwingenden Vorschriften oder Verbrauchserfassung etwas anderes erfordern, werden die vereinbarten Betriebskosten nach Wohnfläche verteilt. Die zentrale Heizung wird entsprechend der Heizkostenverordnung abgerechnet. Die Wohnung wird ganzjährig von beiden Mietern genutzt. Änderungen der Personenzahl allein ändern den vereinbarten Flächenschlüssel nicht. Auf die Jahresabrechnung folgt keine automatische Anerkennung durch Schweigen.

5. Nutzung und Kommunikation

Die Mieter zeigen Mängel der Wohnung dem Vermieter an. Die WEG-Hausverwaltung ist für gemeinschaftliche Gebäudefragen erreichbar, wird dadurch aber nicht selbst Vermieterin. Ein Einsichtstermin zu Abrechnungsbelegen wird mit dem Vermieter abgestimmt. Er kann die Verwaltung mit der Bereitstellung beauftragen, bleibt Ansprechpartner für die eigene Abrechnung.

Der Vertrag wurde am 12.11.2023 von Ottfried Knöpfle, Leela Nair und Juri Biber unterzeichnet. Im Jahr 2025 wurden die Vorauszahlungen nicht geändert.'''),
D('03_WEG_Jahresabrechnung.docx','WEG Abrechnung 2025 Wohnung 4','14.09.2026',HV,'Ottfried Knöpfle', '''Die acht Wohnungen im Spreebogen 7 haben je 80 m² Wohnfläche und je 125 von 1.000 Miteigentumsanteilen. Für Wohnung 4 entfallen aus der gemeinschaftlichen Kostenrechnung 360 EUR auf Wasser, 240 EUR auf Müll, 264 EUR auf die Gebäudeversicherung, 360 EUR auf Reinigung, 360 EUR auf Hausmeisterleistungen und 132 EUR auf Allgemeinstrom. Die Heizkostenabrechnung weist 2.160 EUR aus.

Hinzu kommen 480 EUR Verwaltung, 750 EUR Dachreparatur und 60 EUR Bankkosten. Die gemeinschaftlichen Kosten für diese Wohnung betragen damit 5.166 EUR. Die geleisteten Beiträge zur Erhaltungsrücklage von 1.000 EUR werden getrennt nachgewiesen. Der beigefügte Datenexport summiert sämtliche für den Eigentümer dargestellten Positionen einschließlich dieses Beitrags auf 6.166 EUR.

Der Bankkostenanteil beruht auf insgesamt 480 EUR jährlichen Kontoführungs- und Transaktionsentgelten. Die Rücklage ist auf dem Gemeinschaftskonto angelegt und wurde 2025 nicht für die Dachrechnung eingesetzt. Die Heizkosten enthalten nach Mitteilung des Messdienstes noch die vollen CO₂-Kosten; eine mietvertragliche Weiterverrechnung wurde durch die Verwaltung nicht vorgenommen.

Diese Eigentümerunterlage enthält keine Abrechnung gegenüber Leela Nair und Juri Biber. Die WEG-Beschlüsse und der Mietvertrag sind verschiedene Unterlagen. Noura Selim hat den Export auf Wunsch des Eigentümers zusätzlich als Excel-Datei bereitgestellt.'''),
X('04_Hausgeldexport.xlsx','Datenexport Eigentümer Spreebogen 2025',[dict(name='Eigentuemerkosten',headers=['Position','Haus gesamt EUR','Teiler','Wohnung 4 EUR','Quelle'],widths=[29,20,12,21,45],formats={'B':'#,##0.00','C':'0','D':'#,##0.00'},rows=rows2,expected={'B13':49328,'D13':6166},perturbations=[dict(input='B12',value=0,output='D13',expected=5166)]),dict(name='Heizdaten',headers=['Messgröße','Wert','Einheit','Quelle'],widths=[40,20,19,42],formats={'B':'0.00'},rows=[['Wohnfläche Gebäude',640,'m²','26_Flaechenverzeichnis.docx'],['Wohnfläche Wohnung 4',80,'m²','26_Flaechenverzeichnis.docx'],['Verteilte Heizkosten',17280,'EUR','12_Heizkostenabrechnung.docx'],['CO₂ Emissionen Gebäude',21760,'kg','14_CO2_Liefernachweis.docx'],['CO₂ je Wohnfläche','=B5/B2','kg/m²','Liefernachweis und Flächen'],['CO₂ Kosten Gebäude',1440,'EUR','14_CO2_Liefernachweis.docx'],['CO₂ Kosten Wohnung 4','=B7*B3/B2','EUR','Heizkostenanteil hier 1/8']],expected={'B6':34,'B8':180},perturbations=[dict(input='B5',value=25600,output='B6',expected=40)])]),
]
invoice2 = [
('05_Wasser.docx','Wasser und Abwasser 2025','Kanal und Quelle',2880,'W-SP-25','Der Jahresbetrag besteht aus Trinkwasser von 1.680 EUR einschließlich 7 Prozent Umsatzsteuer und Abwassergebühren von 1.200 EUR ohne Umsatzsteuer. Erfasst wird ausschließlich der Hauptzähler SP-7001; Wohnungswasserzähler bestehen nicht.'),
('06_Muell.docx','Müllentsorgung 2025','Stadtsauber Spree',1920,'M-SP-25','Regelmäßige Leerung der Restmüll- und Wertstoffbehälter im Kalenderjahr 2025. Der Gebührenbescheid weist keine Umsatzsteuer aus. Private Sperrmüllbestellungen sind nicht enthalten.'),
('07_Versicherung.docx','Gebäudeversicherung 2025','Spree Schutz Versicherung',2112,'GV-SP-25','Versichert sind Gebäude und gemeinschaftliche Anlagen. Der Beitrag enthält Versicherungssteuer und keine Umsatzsteuer. Er beinhaltet keine private Rechtsschutzversicherung des Verwalters oder Vermieters.'),
('08_Reinigung.docx','Reinigung der Gemeinschaftsflächen 2025','Feudel Feinschliff GmbH',2880,'R-SP-25','Treppenhaus und Eingangsbereich wurden einmal wöchentlich gereinigt. Die Summe entspricht 2.420,17 EUR netto zuzüglich 459,83 EUR Umsatzsteuer. Eine Sonderreinigung nach Bauarbeiten ist nicht enthalten.'),
('09_Hausmeister.docx','Hausmeisterleistungen 2025','Balthasar Balkon Hausdienst',2880,'HM-SP-25','Bereitstellen der Müllbehälter, Reinigung des Hofablaufs und Kontrollgänge wurden monatlich erbracht. Reparatur- und Verwaltungstätigkeiten wurden nicht abgerechnet. Die Summe entspricht 2.420,17 EUR netto zuzüglich 459,83 EUR Umsatzsteuer. Die wöchentlichen Tätigkeitszettel liegen zur Einsicht vor.'),
('10_Allgemeinstrom.docx','Stromrechnung Treppenhaus 2025','Kiezstrom Energie GmbH',1056,'ST-SP-25','Der Zähler SP-AL02 versorgt nur Treppenhaus, Keller und Hofbeleuchtung. Die Summe entspricht 887,39 EUR netto zuzüglich 168,61 EUR Umsatzsteuer. Der Energieverbrauch beträgt 2.640 kWh.'),
]
for filename,title,vendor,amount,reference,body in invoice2:
    docs2.append(D(filename,title,'31.12.2025',vendor+'\nrechnung@spree-lieferant.example',WEG2,f'''Sehr geehrte Damen und Herren,

für den Zeitraum 01.01.2025 bis 31.12.2025 rechnen wir die nachfolgenden Leistungen für das Haus Spreebogen 7 ab. {body}

Der Gesamtbetrag beträgt {euro(amount)}. Die geleisteten Abschläge beziehungsweise Monatszahlungen decken den Betrag vollständig. Diese Jahresbestätigung begründet keine zusätzliche Forderung. Die im Eigentümerexport genannten Teilbeträge stammen aus der Verteilung durch die Hausverwaltung, nicht aus einer wohnungsweisen Lieferrechnung.

Bitte nennen Sie bei Rückfragen die Rechnungsnummer {reference}. Leistungsnachweise und Zahlungszuordnung können nach Terminabstimmung eingesehen werden.''',reference=reference))
docs2.extend([
D('11_Gasrechnung.docx','Gaslieferung Zentralheizung 2025','12.02.2026','Spreegas Energie GmbH\nrechnung@spreegas.example',WEG2,'''Die Jahreslieferung vom 01.01. bis 31.12.2025 für den Zähler SP-G701 umfasst 108.800 kWh Gas. Der Bruttobetrag beträgt 17.280 EUR, darin 14.521,01 EUR netto und 2.758,99 EUR Umsatzsteuer. Der Betrag enthält sämtliche in dieser Rechnung ausgewiesenen Lieferentgelte. Die gesondert erläuterten CO₂-Kosten von 1.440 EUR brutto sind Teil dieses Betrags und dürfen nicht nochmals hinzuaddiert werden.

Die Abschläge von insgesamt 16.800 EUR und die am 27.02.2026 geleistete Schlusszahlung von 480 EUR gleichen die Rechnung aus. Für die Heizkostenaufstellung 2025 wurde der gesamte Lieferbetrag dem Verbrauchszeitraum 2025 zugeordnet. Die Zahlung der Schlussrechnung erst im Folgejahr ist in der Verwaltung dokumentiert.

Die aus der Lieferung resultierenden CO₂-Emissionen betragen 21.760 kg. Weitere Angaben enthält der Liefernachweis. Unsere Rechnung bestimmt nicht, welcher Anteil zwischen einem Eigentümer und dessen Mietern zu tragen ist. Es wurden keine Kosten für Reparatur oder Neuanschaffung der Heizungsanlage abgerechnet.''',reference='SG-2025-701'),
D('12_Heizkostenabrechnung.docx','Heizkosten 2025 Wohnung 4','02.09.2026','Messdienst Wärmewort GmbH\nservice@waermewort.example','Ottfried Knöpfle über Havel und Hof', '''1. Abrechnungseinheit

Das Haus Spreebogen 7 verfügt über eine zentrale Gasheizung ohne zentrale Warmwasserbereitung. Warmwasser wird in den Wohnungen elektrisch erzeugt. Die verteilten Heizkosten betragen 17.280 EUR. Zusätzliche Wartungs- oder Messdienstkosten wurden für diesen Zeitraum nicht in diese Kostenaufstellung eingestellt. Abgerechnet wird das volle Kalenderjahr 2025.

2. Verteilung

30 Prozent, somit 5.184 EUR, werden nach 640 m² Wohnfläche verteilt. Auf die 80 m² der Wohnung 4 entfallen 648 EUR. 70 Prozent, somit 12.096 EUR, werden nach 80.000 Verbrauchseinheiten verteilt. Für Wohnung 4 sind 10.000 Einheiten erfasst; ihr Anteil beträgt 1.512 EUR. Insgesamt ergeben sich 2.160 EUR.

3. CO₂ und Weiterverwendung

Der ausgewiesene Anteil enthält 180 EUR der in der Lieferrechnung enthaltenen CO₂-Kosten. Die vom Eigentümer zu tragende beziehungsweise gegenüber Mietern anzusetzende Quote wurde in dieser an die WEG gerichteten technischen Kostenverteilung noch nicht umgesetzt. Der Liefernachweis und die Flächenangaben sind beigefügt. Für die vermieterseitige Abrechnung benötigt der Auftraggeber eine entsprechende gesonderte Prüfung.

Die Werte beruhen auf den vollständig abgelesenen Geräten. Es liegt weder eine Verbrauchsschätzung noch ein Nutzerwechsel vor.'''),
D('13_Verbrauchsablesung.docx','Ableseprotokoll Wohnung 4','05.01.2026','Messdienst Wärmewort GmbH','Verwaltungsablage Spreebogen 7', '''Abgelesen wurde am 05.01.2026 der gespeicherte Stichtagswert zum 31.12.2025. Im Wohnzimmer sind 3.800, im Schlafzimmer 2.300, im Arbeitszimmer 2.600 und in der Küche 1.300 bewertete Einheiten gespeichert. Zusammen ergeben sich 10.000 Einheiten. Die Gerätekennungen lauten SP4-W, SP4-S, SP4-A und SP4-K.

Leela Nair war bei der Funktionskontrolle anwesend. Es wurden keine defekten Geräte und keine fehlenden Stichtagswerte vermerkt. Die Summe aller acht Wohnungen beträgt nach dem Hausprotokoll 80.000 Einheiten. Ein Foto einer Geräteanzeige aus dem Mai 2026 betrifft einen anderen laufenden Zeitraum und wurde nicht als Jahresendwert verwendet.

Technikerin Minou Herbst hat die Werte am 05.01.2026 in das Erfassungsblatt übernommen. Die Mieter haben den Termin bestätigt, nicht die spätere Kostenverteilung anerkannt.'''),
D('14_CO2_Liefernachweis.docx','CO2 Angaben zur Gaslieferung 2025','12.02.2026','Spreegas Energie GmbH',WEG2,'''Zur Rechnung SG-2025-701 bestätigen wir einen Energiegehalt der gelieferten Brennstoffmenge von 108.800 kWh, daraus resultierende CO₂-Emissionen von 21.760 kg und enthaltene CO₂-Kosten von 1.440 EUR brutto. Die Angaben beziehen sich ausschließlich auf den Lieferzeitraum 01.01. bis 31.12.2025.

Die Verwaltung hat uns als gesamte Wohnfläche 640 m² mitgeteilt. Eine tatsächliche Vermessung des Gebäudes haben wir nicht vorgenommen. Die jährlichen Emissionen je Quadratmeter sind aus Liefermenge und der zutreffenden Fläche zu bestimmen. Die Gebäudeakte enthält nach Auskunft der Verwaltung keine baurechtliche oder denkmalschutzrechtliche Beschränkung einer energetischen Verbesserung; eine eigenständige Prüfung dieser Auskunft haben wir nicht vorgenommen.

Unsere Auskunft ist eine Lieferinformation. Sie enthält weder eine mietrechtliche Abrechnung noch eine Zusicherung, dass eine bestimmte Ausnahme oder Verteilung im Verhältnis zwischen Vermieter und Mietern vorliegt.'''),
D('15_Verwalterentgelt.docx','Verwaltervergütung für 2025','31.12.2025',HV,WEG2,'''Die vereinbarte monatliche Grundvergütung beträgt 40 EUR brutto je Einheit. Acht Einheiten und zwölf Monate ergeben 3.840 EUR brutto. Darin enthalten sind 3.226,89 EUR netto und 613,11 EUR Umsatzsteuer. Die Vergütung erfasst ausschließlich Gemeinschaftsverwaltung, Buchhaltung, Versammlung und die hierfür vereinbarten Grundleistungen.

Die zwölf Lastschriften wurden vom Konto der Gemeinschaft eingelöst. Der auf Wohnung 4 entfallende Eigentümeranteil beträgt bei acht gleich großen Einheiten 480 EUR. Ein Anspruch gegen die Mieter dieser Wohnung wird durch diese Rechnung nicht begründet. Eine gesonderte Mietverwaltung wurde für 2025 nicht beauftragt.''',reference='HH-SP-25'),
D('16_Dachrechnung.docx','Abdichtung am Dachanschluss Spreebogen','17.06.2025','Dachkultur Emil und Söhne GmbH\nrechnung@dachkultur.example',WEG2,'''Für die am 10. und 11.06.2025 ausgeführte Reparatur des undichten Anschlusses zur Hoffassade berechnen wir 5.042,02 EUR netto zuzüglich 957,98 EUR Umsatzsteuer, insgesamt 6.000 EUR. Der schadhafte Anschluss wurde geöffnet, die beschädigte Abdichtung ersetzt und die Anschlussbleche neu befestigt. Die Rechnung enthält keine jährliche Wartung.

Der Auftrag beruhte auf der schriftlichen Beauftragung vom 28.05.2025. Der Verwalter hat die Leistung am 12.06.2025 anhand des Fertigstellungsberichts entgegengenommen. Am 30.06.2025 gingen 6.000 EUR vom Betriebskonto der Gemeinschaft ein. Der Zahlungseingang wurde vollständig zugeordnet.

Die Feststellung, ob die Kosten gegenüber einem Mieter abzurechnen sind, war nicht Gegenstand unseres Auftrags. Herr Knöpfle hat die Rechnung am 20.09.2026 nochmals angefordert; es handelt sich dabei um eine Kopie derselben Rechnung.''',reference='DK-25-611'),
D('17_Ruecklagennachweis.docx','Rücklagenbeiträge und Bestände 2025','14.09.2026',HV,'Ottfried Knöpfle', '''Die Eigentümer haben für 2025 Beiträge zur Erhaltungsrücklage von insgesamt 8.000 EUR beschlossen und vollständig geleistet. Auf Wohnung 4 entfallen 1.000 EUR. Der Betrag ist als Beitrag auf dem Rücklagenkonto ausgewiesen und wurde nicht für eine Leistung verbraucht.

Der Anfangsbestand von 24.000 EUR und die Jahresbeiträge ergeben einen Schlussbestand von 32.000 EUR. Im betrachteten Zeitraum sind weder Entnahmen noch Zinsen gebucht. Die Dachreparatur wurde aus dem Betriebskonto beglichen. Ein bloßer Eigentümerexport mit der Überschrift „Kosten und Beiträge“ fasst unterschiedliche Zahlungen zusammen und ersetzt deren Belege nicht.

Die Kontounterlagen stehen zur Einsicht bei der Verwaltung bereit. Diese Aufstellung dient der Zuordnung im Verhältnis zwischen Gemeinschaft und Eigentümer.'''),
D('18_Mieterabrechnung_Vorfassung.docx','Betriebskostenabrechnung 2025','16.09.2026','Ottfried Knöpfle','Leela Nair und Juri Biber\nSpreebogen 7, Wohnung 4', '''Sehr geehrte Frau Nair, sehr geehrter Herr Biber,

die Verwaltung hat für unsere Wohnung im Kalenderjahr 2025 insgesamt 6.166 EUR mitgeteilt. Die dazugehörige Aufstellung füge ich bei. Ihre Vorauszahlungen von monatlich 280 EUR ergeben 3.360 EUR. Damit verbleibt eine Nachzahlung von 2.806 EUR. Bitte überweisen Sie diesen Betrag bis zum 30.09.2026 auf das bekannte Mietkonto.

Die Wohnung hat 80 m² von insgesamt 640 m². Ich habe den für meine Wohnung genannten Betrag unverändert übernommen, weil ich als Eigentümer alles bezahlen musste. Die Heizkosten sind in der Summe enthalten. Eine weitere CO₂-Berechnung habe ich nicht gemacht, da dies nach meiner Auffassung bereits der Messdienst erledigt haben müsste.

Bitte richten Sie Fragen zu Rechnungen direkt an die Hausverwaltung. Ich selbst habe nur die Jahresübersicht. Wenn die Verwaltung später andere Werte liefert, werde ich das prüfen.

Mit freundlichen Grüßen
Ottfried Knöpfle'''),
E('19_Versand_an_Mieter.eml','Abrechnung 2025 zur Kenntnis','2026-09-16T19:14:00+02:00','Ottfried Knöpfle <ottfried@knoepfle.example>','Leela Nair <leela@nair.example>','''Guten Abend Frau Nair,

anbei mein Abrechnungsbrief und die Unterlage der Verwaltung. Ich sende beides morgen auch per Post, damit Sie es in Papier haben. Sie müssen nichts doppelt bezahlen. Das Datum 30. September habe ich gewählt, weil ich die Dachrechnung ja schon vorgestreckt habe.

Viele Grüße
Ottfried Knöpfle'''),
D('20_Postzugang_Notiz.docx','Eingang des Abrechnungsbriefs','19.09.2026','Leela Nair und Juri Biber','Private Unterlagen zur Wohnung 4', '''Der Briefumschlag mit dem Abrechnungsbrief vom 16.09.2026 lag am Samstag, 19.09.2026, nachmittags im Briefkasten. Der Umschlag trug einen Poststempel vom 17.09.2026. Darin lagen zwei Unterlagen: der Brief über die Nachzahlung und die WEG-Jahresabrechnung. Einzelrechnungen waren nicht enthalten.

Leela hatte die E-Mail bereits am 16.09.2026 auf dem Mobiltelefon gesehen und am nächsten Morgen mit den Anhängen gespeichert. Juri hat erst den Papierbrief gelesen. Ein Einschreibebeleg oder eine persönliche Übergabe liegen nicht vor. Die Notiz wurde am Tag des Briefeingangs gemeinsam erstellt.'''),
E('21_Einwendungen_Mieter.eml','Abrechnung 2025: Belege und Rücklagen','2026-09-21T10:23:00+02:00','Leela Nair und Juri Biber <leela@nair.example>','Ottfried Knöpfle <ottfried@knoepfle.example>','''Sehr geehrter Herr Knöpfle,

wir können Ihre Nachforderung so nicht nachvollziehen. In der beigefügten Übersicht stehen Verwaltung, Dachreparatur, Bankkosten und Rücklage. Wir möchten wissen, warum diese Positionen bei uns landen. Die Heizkostenabrechnung erwähnt außerdem, dass die CO₂-Verteilung noch nicht berücksichtigt ist.

Bitte schicken Sie eine nach Kostenarten und unserem Anteil nachvollziehbare Abrechnung und ermöglichen Sie Einsicht in die Rechnungen sowie die zugehörigen Zahlungsbelege. Mit Ihrer bisherigen Zahlungsfrist sind wir nicht einverstanden. Wir verweigern keine Prüfung einer nachvollziehbaren Forderung, möchten aber nicht erst 2.806 EUR zahlen und dann hinterherlaufen.

Freundliche Grüße
Leela Nair und Juri Biber'''),
E('22_Hausverwaltung_an_Eigentuemer.eml','Spreebogen WE4: Ihre weitergeleitete Mietabrechnung','2026-09-22T08:48:00+02:00','Noura Selim <verwaltung@havelhof.example>','Ottfried Knöpfle <ottfried@knoepfle.example>','''Sehr geehrter Herr Knöpfle,

unser Export ist die Eigentümerübersicht. Die Kennzeichnung als fertige Mieterabrechnung stammt nicht von uns. Wir können Ihnen die Originalbelege und Heizdaten bereitstellen. Ob und wie Sie diese gegenüber Ihren Mietern abrechnen, muss anhand Ihres Mietvertrags geprüft werden.

Für einen Einsichtstermin benötigen wir Ihre Beauftragung, weil wir die Mieter nicht ohne Abstimmung in sämtliche Eigentümerunterlagen einsehen lassen. Die für deren Abrechnung benötigten Rechnungen und Zahlungszuordnungen können wir geordnet bereitstellen. Bitte schicken Sie uns den Vertrag und teilen Sie mit, ob wir auch die Erstellung einer korrigierten Abrechnung koordinieren sollen.

Mit freundlichen Grüßen
Noura Selim'''),
E('23_Terminangebot_Belege.eml','Belegeinsicht Spreebogen: zwei Termine','2026-09-23T14:21:00+02:00','Noura Selim <verwaltung@havelhof.example>','Leela Nair <leela@nair.example>','''Sehr geehrte Frau Nair,

Herr Knöpfle hat uns heute mit der Bereitstellung der Abrechnungsbelege beauftragt. Wir bieten Ihnen Montag, den 28. September, um 16 Uhr oder Mittwoch, den 30. September, um 10 Uhr in unserem Verwaltungsbüro an. Die Rechnungen und die zugehörigen Zahlungseinträge liegen bereit. Sie können die einschlägigen Unterlagen ansehen und mit einem eigenen Gerät Aufnahmen für Ihre Prüfung anfertigen.

Die Kontobewegungen anderer Eigentümer werden wir nicht offen auslegen. Falls Sie weitere konkret bezeichnete Unterlagen benötigen, teilen Sie uns dies bitte vorher mit. Die Entscheidung über die geltend gemachte Mietnachforderung treffen wir mit diesem Terminangebot nicht.

Mit freundlichen Grüßen
Noura Selim'''),
E('24_Mieter_Terminbestaetigung.eml','Re: Belegeinsicht am 28. September','2026-09-24T07:52:00+02:00','Leela Nair <leela@nair.example>','Noura Selim <verwaltung@havelhof.example>','''Guten Morgen Frau Selim,

wir kommen am Montag um 16 Uhr. Bitte legen Sie auch die Tätigkeitszettel des Hausmeisters und den Nachweis über die Dachzahlung bereit. Uns geht es nicht darum, die privaten Zahlungsprobleme anderer Eigentümer zu sehen. Wir wollen verstehen, wofür die auf unserer Abrechnung genannten Beträge stehen.

Ich bringe den Brief mit, der am Samstag eingegangen ist. Das im Mai aufgenommene Heizgerätefoto finde ich ebenfalls, weiß aber nicht, ob es für 2025 etwas sagt.

Viele Grüße
Leela Nair'''),
T('25_Chat_Knoepfle_Tochter.txt','Chat Ottfried und Finja','24.09.2026','''24.09.2026 18:11 Ottfried: Wenn ich das zahlen muss, müssen die Mieter es doch auch zahlen.
24.09.2026 18:14 Finja: Die Rücklage bleibt doch dein Geld im Gemeinschaftstopf. Schau lieber in den Vertrag.
24.09.2026 18:16 Ottfried: Die Verwaltung soll nicht so tun, als wäre das mein Problem. Da stand 6166.
24.09.2026 18:19 Finja: Du hast die Überschrift Betriebskosten selbst darüber geschrieben.
24.09.2026 18:26 Ottfried: Gut. Ich will keinen Streit um jeden Cent, aber auch nichts verschenken. Frau Selim soll eine ordentliche neue Fassung machen lassen.'''),
D('26_Flaechenverzeichnis.docx','Flächen und Einheiten Spreebogen 7','02.01.2025',HV,'Abrechnungsablage', '''Das Gebäude umfasst acht Wohnungen mit jeweils 80 m² Wohnfläche. Die Gesamtwohnfläche beträgt 640 m². Jede Wohnung ist mit 125 von 1.000 Miteigentumsanteilen verbunden. Gemeinschaftliche Keller- und Treppenhausflächen sind in diesen Wohnflächen nicht enthalten. Eine gewerbliche Einheit besteht nicht.

Wohnung 4 wird im gesamten Jahr 2025 von Leela Nair und Juri Biber bewohnt. Ottfried Knöpfle ist im betrachteten Jahr durchgehend Eigentümer und Vermieter. Ein Nutzer- oder Eigentümerwechsel ist für diese Wohnung nicht vermerkt. Die Flächen stammen aus der bei der Verwaltung hinterlegten Teilungserklärung und wurden seit deren Erstellung nicht verändert.

Eine Einschränkung energetischer Maßnahmen durch Denkmalschutz ist in der Objektakte nicht abgelegt. Die Verwaltung kann eine fehlende Unterlage nicht durch eine abschließende öffentlich-rechtliche Auskunft ersetzen.'''),
D('27_Reparaturauftrag_Dach.docx','Auftrag zur Abdichtung des Dachanschlusses','28.05.2025',HV,'Dachkultur Emil und Söhne GmbH', '''Sehr geehrte Damen und Herren,

namens der Gemeinschaft der Wohnungseigentümer Spreebogen 7 beauftragen wir die im Angebot DK-A-250519 beschriebenen Arbeiten für 6.000 EUR brutto. Gegenstand ist die Beseitigung der festgestellten Undichtigkeit am hofseitigen Dachanschluss. Ein turnusmäßiger Wartungsvertrag wird damit nicht abgeschlossen.

Die Eigentümer haben den Auftrag am 27.05.2025 mit acht Ja-Stimmen beschlossen. Die Zahlung soll vom laufenden Gemeinschaftskonto erfolgen. Eine Rücklagenentnahme ist nicht beschlossen. Bitte stimmen Sie den Zugang zum Dach über das Treppenhaus mindestens zwei Werktage vorher mit uns ab und hinterlassen Sie die Verkehrsflächen nach Abschluss sauber.

Zusatzleistungen bedürfen einer gesonderten Beauftragung. Einen nachträglich entdeckten weiteren Schaden teilen Sie uns zunächst mit; dieser Auftrag enthält keine unbeschränkte Mehrkostenfreigabe.

Mit freundlichen Grüßen
Noura Selim'''),
E('28_Eigentuemer_Beauftragung.eml','Bitte Mietabrechnung prüfen lassen','2026-09-24T19:02:00+02:00','Ottfried Knöpfle <ottfried@knoepfle.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

ich beauftrage Sie, die Belege für den Termin bereitzustellen und Frau Morgen um einen korrigierten Abrechnungsentwurf sowie eine Antwort an meine Mieter zu bitten. Den Mietvertrag füge ich bei. Bitte versenden Sie noch keine neue Forderung. Ich möchte den Betrag und die Begründung vorher verstehen.

Die Mietzahlungen sind vollständig eingegangen. Auf dem Mietkonto steht seit Januar 2025 jeden Monat 1.330 EUR. Davon sind 280 EUR die Vorauszahlungen. Eine Sondervereinbarung, nach der die Mieter mein Hausgeld tragen, gibt es neben dem Vertrag nicht.

Mit freundlichen Grüßen
Ottfried Knöpfle'''),
X('29_Mietvorauszahlungen.xlsx','Vorauszahlungen Nair und Biber 2025',[dict(name='Mietkonto',headers=['Datum','Buchung','Vorauszahlung EUR','Quelle'],widths=[20,42,24,35],formats={'C':'#,##0.00'},rows=payments2,expected={'C14':3360},perturbations=[dict(input='C13',value=0,output='C14',expected=3080)])]),
D('30_Antwortbrief_Vorfassung.docx','Antwort auf Ihre Fragen zur Abrechnung','24.09.2026','Ottfried Knöpfle','Leela Nair und Juri Biber', '''Sehr geehrte Frau Nair, sehr geehrter Herr Biber,

ich habe Ihre Einwendungen an die Verwaltung weitergegeben. Nach meiner bisherigen Ansicht müssen alle tatsächlich von mir gezahlten Positionen weiterberechnet werden. Ich habe für Sie keine zusätzlichen Leistungen bestellt. Deshalb halte ich die bisherige Nachforderung zunächst aufrecht. Die Belege können Sie am vereinbarten Termin bei der Verwaltung ansehen.

Die CO₂-Kosten müssten nach meinem Verständnis schon in den Heizkosten erledigt sein. Ob in der beigefügten technischen Abrechnung etwas anderes steht, lasse ich noch klären. Eine neue Zahlungsfrist habe ich noch nicht festgelegt.

Mit freundlichen Grüßen
Ottfried Knöpfle

Der Brief liegt als nicht versandter Entwurf im E-Mail-Anhang an die Verwaltung. Herr Knöpfle hat um Prüfung gebeten, bevor er ihn abschickt.'''),
E('31_Belege_an_Vermieter.eml','Spreebogen: Gasbeleg und Messdienstunterlagen','2026-09-25T09:15:00+02:00','Noura Selim <verwaltung@havelhof.example>','Ottfried Knöpfle <ottfried@knoepfle.example>','''Sehr geehrter Herr Knöpfle,

anbei die Gasrechnung, die technische Heizkostenverteilung und der CO₂-Liefernachweis. Die technischen Angaben nennen eine noch nicht umgesetzte Verteilung zwischen Ihnen und Ihren Mietern. Bitte verwenden Sie deshalb Ihren vorbereiteten Antwortbrief zunächst nicht.

Die Jahresrechnung der Gemeinschaft und die Beiträge zur Rücklage bleiben in unserer Akte unverändert erhalten. Die daraus zu erstellende Mietabrechnung wird eine eigene Datei mit eigenem Datum erhalten. Die beiden Vorgänge sollen anschließend auch bei Rückfragen zugeordnet werden können.

Mit freundlichen Grüßen
Noura Selim'''),
E('32_Bearbeitungsauftrag_Nachtrag.eml','Spreebogen: Zahlenbrief und Antwort zusammenführen','2026-09-25T13:46:00+02:00','Noura Selim <verwaltung@havelhof.example>','Friederike Morgen <kanzlei@morgen.example>','''Sehr geehrte Frau Morgen,

bitte berücksichtigen Sie den unterschiedlichen Zugang per E-Mail und Post, die bereits vereinbarte Belegeinsicht und den unversandten Antwortentwurf. Wir benötigen für Herrn Knöpfle einen konkreten nächsten Schritt. Er soll erkennen können, welche Kostenposition welchen Beleg trägt, welche Daten noch zu prüfen sind und welche neue Nachricht an die Mieter sinnvoll ist.

Die Mieter haben seit dem Schreiben keine Zahlung gekürzt. Eine Kündigung oder gerichtliche Geltendmachung ist nicht beauftragt. Bitte behandeln Sie die Nachforderung nicht vorschnell als unstreitig fällig.

Mit freundlichen Grüßen
Noura Selim'''),
])
assert len(docs2) == 32
CASES.append(dict(slug='weg-spreebogen-mieterumlage-belege',title='Spreebogen und das weitergereichte Hausgeld',plugin=PLUGIN,date='25.09.2026',client='Havel und Hof Hausverwaltung GmbH sowie Eigentümer Ottfried Knöpfle',summary='Ein Vermieter reicht den gesamten WEG-Export an seine Mieter weiter. Die Mieter fragen nach Rücklage, Reparatur und CO₂-Anteil; die Verwaltung organisiert erstmals eine individuelle Mietabrechnung und Belegeinsicht.',assignment='WEG-Unterlagen, Mietvertrag, Abrechnungsentwurf und Belege abgleichen. Eine nachvollziehbare Mietabrechnung und eine persönliche Antwort vorbereiten, Belegzugang und weitere Kommunikation organisieren.',documents=sorted(docs2,key=lambda d:d['file']),attachments={'19_Versand_an_Mieter.eml':['18_Mieterabrechnung_Vorfassung.docx','03_WEG_Jahresabrechnung.docx'],'28_Eigentuemer_Beauftragung.eml':['02_Mietvertrag.docx','30_Antwortbrief_Vorfassung.docx'],'31_Belege_an_Vermieter.eml':['11_Gasrechnung.docx','12_Heizkostenabrechnung.docx','14_CO2_Liefernachweis.docx']}))

WEG3 = 'Gemeinschaft der Wohnungseigentümer Kastanienhof 9\nKastanienhof 9, Berlin'
docs3 = [
D('01_Auftrag_Kellervorfall.docx','Kellerzugang und verschwundene Fahrräder','23.09.2026',HV,'Rechtsanwältin Friederike Morgen', '''Sehr geehrte Frau Morgen,

in der Nacht zum 11. September wurde die Kellertür im Kastanienhof beschädigt. Es fehlen zwei Fahrräder und Werkzeug. Wir haben die Tür zunächst sichern lassen und einen Versicherungsfall gemeldet. Inzwischen gibt es widersprüchliche Erinnerungen dazu, wie lange die Tür vorher schon klemmte. Im Hauschat werden Namen genannt; niemand hat nach unserem Kenntnisstand den Einbruch beobachtet.

Bitte ordnen Sie die Vorgänge für die Gemeinschaft, die betroffenen Eigentümer und deren Mieter getrennt. Wir benötigen eine belastbare Nachricht an die Bewohner, die Antwort an den Gebäudeversicherer und eine Beschlussvorlage für die weitere Türreparatur. Der Beirat diskutiert zusätzlich zwei Kameras. Frau Hummel möchte morgen im Umlaufverfahren abstimmen und verlangt drei Angebote; Herr Wackel schlägt vor, alle Kosten gleichmäßig auf die Wohnungen zu verteilen.

Die provisorische Sicherung ist bezahlt. Ein dauerhafter Austausch wurde noch nicht freigegeben. Die Wohnungseigentümer haben unterschiedliche Anteile und Wohnungsgrößen. Bitte prüfen Sie auch, was jetzt ohne Versammlungsbeschluss veranlasst werden kann und welche Tatsachen wir vor weitergehenden Entscheidungen benötigen. Ansprüche dürfen nicht ohne Klärung anerkannt werden; die Bewohner sollen trotzdem konkrete Hilfe erhalten.

Mit freundlichen Grüßen
Noura Selim'''),
D('02_Objekt_und_Zustaendigkeiten.docx','Objektunterlagen Kastanienhof 9','02.01.2026',HV,'Gemeinschaftsablage', '''Die Gemeinschaft besteht aus sechs Wohnungen. Wohnung 1 gehört Hildegard Hummel mit 80/1.000 Anteilen und 48 m², Wohnung 2 Ilyas Ben Salem mit 120/1.000 und 72 m², Wohnung 3 Lotte Wackel mit 150/1.000 und 90 m², Wohnung 4 Benedikt Brösel mit 180/1.000 und 108 m², Wohnung 5 Yuna Albrecht mit 220/1.000 und 132 m², Wohnung 6 Nepomuk Fiedler mit 250/1.000 und 150 m². Zusammen sind dies 600 m² und 1.000 Anteile.

Die Hauseingangstür und die Tür zum gemeinschaftlichen Kellerflur gehören zum gemeinschaftlichen Eigentum. Die Abteile sind den Wohnungen zur ausschließlichen Nutzung zugeordnet. Die vorhandenen Abteiltüren und privaten Vorhängeschlösser sind nach der Teilungserklärung von den jeweiligen Eigentümern zu unterhalten. Das Fahrradregal im Gemeinschaftsflur darf von den Bewohnern mitbenutzt werden; die Hausordnung sieht dafür keine Bewachung vor.

Die Kosten des gemeinschaftlichen Eigentums werden nach Miteigentumsanteilen getragen. Eine abweichende Verteilung nach Einheiten ist nicht eingetragen. Die Verwaltung führt kleinere laufende Maßnahmen aus; für nicht laufende Aufträge sieht der Verwaltervertrag ohne besonderen Beschluss eine interne Wertgrenze von 1.500 EUR brutto vor. Gesetzliche Befugnisse für dringliche Maßnahmen bleiben im Vertrag ausdrücklich unberührt.'''),
E('03_Erste_Meldung.eml','Kellertür beschädigt, mein Fahrrad fehlt','2026-09-11T06:58:00+02:00','Sana Özdemir <sana@ozdemir.example>','Noura Selim <verwaltung@havelhof.example>','''Guten Morgen,

ich wollte gerade zur Arbeit. Die Kellertür steht schief, am Schließblech ist Holz abgesplittert. Mein dunkelblaues E-Bike ist aus dem Gemeinschaftsregal verschwunden. Ich hatte es gestern um etwa 20 Uhr dort angeschlossen. Das durchtrennte Schloss liegt noch auf dem Boden. Ich fasse erst einmal nichts an und habe die Polizei verständigt.

Ich wohne zur Miete bei Herrn Ben Salem in Wohnung 2. Bitte lassen Sie die Tür heute sichern. Frau Hummel sagt, sie habe gestern schon gegen 19 Uhr gesehen, dass sie nicht ganz schließt. Ob das stimmt, weiß ich selbst nicht.

Sana Özdemir'''),
D('04_Besichtigungsprotokoll.docx','Besichtigung des Kellerzugangs am 11 September','11.09.2026',HV,WEG3,'''Noura Selim besichtigte den Kellerzugang am 11.09.2026 von 08.35 bis 09.00 Uhr in Anwesenheit von Sana Özdemir und Hausmeister Bruno Fink. Am Schließblech waren frische Ausbrüche und am Türfalz mehrere Druckspuren sichtbar. Das Türblatt ließ sich ohne zusätzliche Sicherung nicht zuverlässig verriegeln. Der obere Türschließer war nicht abgerissen.

Im Gemeinschaftsflur lag ein durchtrenntes Fahrradschloss. Sana Özdemir ordnete es ihrem E-Bike zu. Benedikt Brösel meldete telefonisch ein fehlendes Kinderfahrrad. Das Vorhängeschloss an Abteil 5 war geöffnet; Yuna Albrecht meldete später fehlendes Werkzeug. Die Besichtigung klärte weder Zeitpunkt noch Person des Zugangs. Es wurden keine eigenen Durchsuchungen vorgenommen.

Die Polizei hatte vor der Besichtigung erste Angaben aufgenommen. Frau Selim bat den Schlüsseldienst um eine reversible Sicherung der gemeinschaftlichen Tür. Private Abteile sollten nur mit Zustimmung des jeweiligen Nutzers geöffnet werden. Das lose Schließblech wurde nach fotografischer Dokumentation durch den Monteur übernommen und in einem beschrifteten Beutel bei der Verwaltung verwahrt.'''),
D('05_Polizeiliche_Bestaetigung.docx','Bestätigung der Anzeigenaufnahme','11.09.2026','Polizei Berlin\nSachbearbeitung Eigentumsdelikte\nkontakt@polizeiakte.example','Sana Özdemir', '''Ihre Anzeige wegen des gemeldeten Diebstahls eines E-Bikes aus dem gemeinschaftlichen Kellerbereich Kastanienhof 9 wurde am 11.09.2026 aufgenommen. Die vorläufige Vorgangsnummer lautet K-260911-481. Als möglicher Tatzeitraum wurde nach Ihren Angaben 10.09.2026, etwa 20 Uhr, bis 11.09.2026, etwa 06.45 Uhr, erfasst.

Bitte reichen Sie Kaufunterlagen, Rahmennummer, Beschreibung und Fotos des Fahrrads nach, soweit vorhanden. Hinweise weiterer Betroffener können unter Bezug auf die Vorgangsnummer übermittelt werden. Diese Bestätigung enthält keine Feststellung zu einer bestimmten tatverdächtigen Person, zur Eintrittsweise oder zur Einstandspflicht eines Versicherers.

Ein später mitgeteilter abweichender Beobachtungszeitpunkt wird als ergänzende Angabe aufgenommen. Verändern Sie vorhandene Spuren nur, soweit dies zur Sicherung des Gebäudes erforderlich ist, und dokumentieren Sie erforderliche Veränderungen nachvollziehbar.

Im Auftrag
R. Seidel'''),
D('06_Notdienstrechnung.docx','Provisorische Sicherung der Kellertür','11.09.2026','Schlüsselhilfe Minou GmbH\nrechnung@schluesselhilfe.example',WEG3, '''Am 11.09.2026 wurde von 09.20 bis 10.05 Uhr am gemeinschaftlichen Kellerzugang eine provisorische Schließblechverstärkung angebracht und der vorhandene Zylinder weiterverwendet. Die Tür ist vorläufig abschließbar. Der geschädigte Rahmen muss dauerhaft instand gesetzt werden. Ein Austausch sämtlicher Hauszylinder war für diese Sicherung nicht erforderlich.

Anfahrt 45 EUR netto, Arbeitszeit 95 EUR netto, Sicherungsmaterial 60 EUR netto: zusammen 200 EUR netto, 38 EUR Umsatzsteuer und 238 EUR brutto. Frau Selim beauftragte die Arbeiten telefonisch namens der Gemeinschaft. Der Betrag ist bis zum 25.09.2026 zu zahlen.

Die Sicherung ist eine Zwischenmaßnahme. Wir empfehlen, den Rahmen innerhalb von zwei Wochen dauerhaft reparieren zu lassen. Eine Aussage darüber, ob die Tür vor dem Ereignis ordnungsgemäß geschlossen war, ist aufgrund der vorgefundenen Beschädigung nicht möglich.''',reference='SM-260911-07'),
E('07_Hummel_Erinnerung.eml','Die Tür hat schon Donnerstag geklemmt','2026-09-11T12:32:00+02:00','Hildegard Hummel <hildegard@hummel.example>','Noura Selim <verwaltung@havelhof.example>','''Liebe Frau Selim,

ich war am Donnerstag gegen 19 Uhr am Keller und musste die Tür fest zuziehen. Sie fiel nicht von allein ins Schloss. Ich dachte, Bruno hätte das schon gesehen, und bin nicht noch einmal hochgegangen. Einen fremden Menschen habe ich nicht gesehen. Den genauen Zeitpunkt entnehme ich jetzt meiner Erinnerung, nicht einer Uhr.

Vielleicht war es auch schon nach 20 Uhr, weil ich vorher mit meiner Schwester telefoniert hatte. Bitte schreiben Sie nicht, ich hätte einen Einbrecher gesehen. So etwas habe ich niemals behauptet.

Hildegard Hummel'''),
E('08_Hausmeister_Antwort.eml','Kontrollgang vom 10. September','2026-09-11T14:08:00+02:00','Bruno Fink <bruno@hausdienst.example>','Noura Selim <verwaltung@havelhof.example>','''Hallo Noura,

ich habe die Tür am Donnerstag um 16.20 Uhr bei meinem Kontrollgang einmal geöffnet und geschlossen. Dabei rastete sie ein. Eine längere Funktionsprüfung habe ich nicht gemacht. Von Frau Hummel hatte ich vor heute keine Nachricht. Im August hatte ich die Scharniere nachgestellt; den Arbeitszettel füge ich bei.

Das bedeutet natürlich nicht, dass sie abends genauso funktioniert hat. Ich war nach 16.30 Uhr nicht mehr im Haus. Bitte gib im Hauschat keine Garantie in meinem Namen ab.

Bruno'''),
D('09_Arbeitszettel_August.docx','Nachstellen der Kellertür','19.08.2026','Bruno Fink Hausdienst','Havel und Hof Hausverwaltung GmbH', '''Am 19.08.2026 wurde die Tür zum Kellerflur nach einer Meldung von Herrn Fiedler geprüft. Die Tür streifte unten an der Zarge. Die Scharniere wurden nachgestellt; anschließend schloss sie bei drei Versuchen ohne zusätzlichen Druck. Ein Austausch des Türschließers wurde nicht vorgenommen.

Die Arbeiten dauerten von 10.10 bis 10.40 Uhr und wurden im laufenden Hausdiensthonorar erfasst. Für Material entstanden keine gesonderten Kosten. Bruno Fink trug den Vorgang am selben Tag in sein Servicebuch ein. Eine weitere Mängelmeldung wurde bis zum Kontrollgang vom 10.09.2026 nicht bei ihm erfasst.

Die Notiz dokumentiert den damaligen Testzustand. Sie enthält keine technische Langzeitprüfung und keine Aussage zum späteren Einbruch.'''),
D('10_Kaufbeleg_E_Bike.docx','Kaufrechnung Stadtrad Lumen 4','15.04.2024','Radladen Rollfein GmbH\nrechnung@rollfein.example','Sana Özdemir', '''Sie haben am 15.04.2024 ein E-Bike Stadtrad Lumen 4 in Dunkelblau zum Preis von 2.299 EUR brutto erworben. Der Betrag enthält 1.931,93 EUR netto und 367,07 EUR Umsatzsteuer. Die Rahmennummer lautet LUM24-SO-0815. Ein Rahmenschloss und Ladegerät gehören zum Lieferumfang.

Bezahlt wurde bei Abholung per Karte. Ein zusätzliches Kettenschloss wurde am selben Tag nicht bei uns erworben. Die Rechnung dient der Zuordnung des verkauften Rads und ist kein Nachweis seines Zustands im September 2026. Die Werkstatt hatte das Rad am 18.04.2025 zur Inspektion; ein Verkauf durch die Kundin ist uns nicht bekannt.''',reference='RF-240415-88'),
D('11_Kaufbeleg_Kinderfahrrad.docx','Kaufrechnung Kinderfahrrad Komet','22.05.2025','Pedalperle Fahrradhandel\nrechnung@pedalperle.example','Benedikt Brösel', '''Geliefert wurde am 22.05.2025 ein Kinderfahrrad Komet 24 in Rot für 420 EUR brutto, darin 352,94 EUR netto und 67,06 EUR Umsatzsteuer. Die Rahmennummer lautet KOM25-BB-0021. Der Kaufpreis wurde vollständig per Karte bezahlt.

Ein Schloss ist in dieser Rechnung nicht enthalten. Die Verkaufsunterlage nennt weder einen späteren Abstellort noch eine Versicherung. Herr Brösel bat am 12.09.2026 um eine Rechnungskopie; die Kopie verändert die ursprünglichen Rechnungsdaten nicht.''',reference='PP-250522-31'),
E('12_Werkzeugmeldung.eml','Auch aus Abteil 5 fehlt etwas','2026-09-12T09:41:00+02:00','Yuna Albrecht <yuna@albrecht.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

aus meinem Kellerabteil fehlen nach erster Sichtung ein Akkuschrauber und ein kleiner Werkzeugkoffer. Den Koffer habe ich vor Jahren gebraucht gekauft; einen Beleg habe ich nicht. Für beides zusammen schätze ich den damaligen Kaufwert auf etwa 180 EUR. Die Geräte gehörten mir, nicht meinem Mieter.

Ich bin nicht sicher, ob das Vorhängeschloss aufgebrochen oder von mir beim letzten Besuch nicht richtig eingerastet war. Es ist noch vorhanden und äußerlich nicht verbogen. Bitte führen Sie meine Schätzung getrennt von den beiden Fahrradrechnungen. Ich suche am Wochenende noch nach einem Foto.

Mit freundlichen Grüßen
Yuna Albrecht'''),
D('13_Gebaeudeversicherung_Vertrag.docx','Versicherungsumfang Kastanienhof 9','01.01.2026','Havel Schutz Versicherung\nservice@havelschutz.example',WEG3, '''1. Versicherte Sache und Zeitraum

Versicherungsnehmerin ist die Gemeinschaft der Wohnungseigentümer Kastanienhof 9. Versichert sind das bezeichnete Wohngebäude und die zugehörigen gemeinschaftlichen Gebäudebestandteile vom 01.01. bis 31.12.2026. Bewegliche Sachen einzelner Bewohner, insbesondere Fahrräder und privates Werkzeug, gehören nicht zu den versicherten Gebäudebestandteilen.

2. Einbruchbedingte Gebäudeschäden

Der vereinbarte Baustein umfasst nach Maßgabe der Bedingungen Beschädigungen versicherter Gebäudeteile durch einen versuchten oder vollendeten Einbruch. Für jeden entschädigungspflichtigen Schaden gilt ein Selbstbehalt von 500 EUR. Kosten notwendiger vorläufiger Sicherungsmaßnahmen sind mit der Schadenbearbeitung abzustimmen; dringliche Sicherung darf unter Dokumentation der Umstände vorgenommen werden.

3. Schadenmeldung und Unterlagen

Die Versicherungsnehmerin meldet den Schaden unverzüglich und ermöglicht die Prüfung von Ursache und Umfang. Rechnungen, Angebote, Tatbeschreibung und vorhandene polizeiliche Vorgangsangaben sind vorzulegen. Ein Anerkenntnis zugunsten Dritter darf nicht ohne Abstimmung im Namen des Versicherers erklärt werden. Die Prüfung bleibt auch nach Vergabe einer Schadennummer offen.

Policennummer HS-KH-2026. Dieser Vertragsauszug umfasst die für die gemeldete Gebäudebeschädigung bereitgelegten Bestimmungen.'''),
E('14_Schadenmeldung_Gebaeude.eml','HS-KH-2026: Beschädigte Kellertür','2026-09-11T11:18:00+02:00','Noura Selim <verwaltung@havelhof.example>','Havel Schutz Schadenservice <schaden@havelschutz.example>','''Sehr geehrte Damen und Herren,

wir melden namens der Gemeinschaft die Beschädigung des gemeinschaftlichen Kellerzugangs im Kastanienhof 9. Die Tür wurde heute vorläufig gesichert, damit der Keller wieder abschließbar ist. Den Besichtigungsvermerk und die Rechnung reichen wir mit dieser Nachricht ein. Dauerhafte Reparaturangebote folgen.

Daneben sind private Fahrräder und Werkzeug als verschwunden gemeldet. Wir führen diese Angaben getrennt und machen damit keine Gebäudeeigenschaft dieser Gegenstände geltend. Der genaue Hergang ist noch offen. Bitte teilen Sie mit, welche Unterlagen Sie vor der dauerhaften Reparatur benötigen.

Mit freundlichen Grüßen
Noura Selim'''),
E('15_Versicherer_Nachforderung.eml','Schaden KH-261109: Unterlagen vor Reparatur','2026-09-14T10:17:00+02:00','Havel Schutz Schadenservice <schaden@havelschutz.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

wir führen den Vorgang unter KH-261109. Bitte übersenden Sie zwei nachvollziehbare Reparaturangebote oder erläutern Sie, weshalb ein Preisvergleich nicht möglich ist. Wir benötigen außerdem Angaben zur vorherigen Türfunktion, die polizeiliche Vorgangsnummer und die Dokumentation des ausgebauten Schließblechs. Eine Besichtigung wollen wir nach Eingang der Angebote abstimmen.

Eine Deckungszusage ist mit dieser Nachricht nicht verbunden. Die provisorische Sicherung können Sie dokumentiert belassen. Bitte unterscheiden Sie die Wiederherstellung des beschädigten Zustands von einer zusätzlichen Sicherheitsverbesserung. Über private Fahrradschäden entscheiden wir in diesem Gebäudevorgang nicht.

Mit freundlichen Grüßen
Marta Winterfeld'''),
E('16_Hausratversicherung_Mieterin.eml','Fahrradmeldung SO-2611: Bitte Sicherung erläutern','2026-09-15T08:02:00+02:00','Hausrat Direkt <leistung@hausratdirekt.example>','Sana Özdemir <sana@ozdemir.example>','''Sehr geehrte Frau Özdemir,

wir haben Ihre Meldung erhalten. Bitte teilen Sie mit, ob das Fahrrad mit einem gesonderten Schloss an einem festen Gegenstand angeschlossen war, und reichen Sie die Rechnung sowie die polizeiliche Vorgangsnummer ein. Aus Ihrer Police ergibt sich ein vereinbarter Fahrradbaustein; dessen Voraussetzungen und Entschädigungsgrenze prüfen wir anhand der Unterlagen.

Bitte legen Sie keine allein auf Vermutungen beruhende Bestätigung der Hausverwaltung zur Türfunktion vor. Eigene Wahrnehmungen der Beteiligten können als solche beigefügt werden. Eine Zahlung oder Ablehnung ist noch nicht entschieden.

Freundliche Grüße
Maja Rose'''),
D('17_Angebot_Tuer_Reparatur.docx','Angebot zur Wiederherstellung der Kellertür','16.09.2026','Tischlerei Ottokar Ast\nangebot@ottokarast.example',WEG3, '''Wir bieten die Reparatur der beschädigten Zarge und die Erneuerung von Schließblech und Befestigung für insgesamt 714 EUR brutto an. Der Nettobetrag beträgt 600 EUR, die Umsatzsteuer 114 EUR. Das vorhandene Türblatt und der vorhandene Zylinder bleiben erhalten, soweit die Prüfung beim Ausbau keine weiteren Schäden ergibt.

Die Arbeiten dauern voraussichtlich vier Stunden. Terminoption ist der 28.09.2026 ab 9 Uhr. Zusätzliche Schäden werden vor einer Erweiterung des Auftrags angezeigt. Die vorläufige Verstärkung kann nach erfolgter Rahmenreparatur entfernt werden. Im Angebot ist keine neue Schließanlage und keine Kamera enthalten.

Wir halten uns bis zum 30.09.2026 an das Angebot gebunden. Ein Versicherungsanerkenntnis oder eine bestimmte Einbruchhemmungsklasse wird mit dieser Reparatur nicht zugesagt. Das Angebot ist noch nicht beauftragt.''',reference='OA-260916-12'),
D('18_Angebot_Schliessung.docx','Angebot neuer Kellerzylinder und Schließblech','16.09.2026','Schlüsselhilfe Minou GmbH',WEG3, '''Für den Austausch des Kellerzylinders, ein verstärktes Schließblech und zwölf neue Schlüssel bieten wir 1.000 EUR netto zuzüglich 190 EUR Umsatzsteuer, insgesamt 1.190 EUR brutto, an. Die Reparatur der ausgebrochenen Holzzarge ist nicht enthalten und muss vorher durch einen Tischlereibetrieb erfolgen.

Das Angebot verbessert die vorhandene Schließung und ersetzt den bisherigen Kellerzylinder. Ob der alte Zylinder technisch beschädigt ist, konnten wir bei der provisorischen Sicherung nicht feststellen. Die Haustürschließung bleibt unverändert. Die neuen Kellerschlüssel wären zusätzlich zu den vorhandenen Hausschlüsseln zu führen.

Lieferzeit ist voraussichtlich zwei Wochen nach Auftrag. Bei Vergabe werden die bisherigen Bewohnerlisten nur für die Schlüsselverteilung verwendet. Eine Weitergabe dieser Listen an einen Kameradienst ist nicht Teil der Leistung. Das Angebot ist bis zum 02.10.2026 befristet.''',reference='SM-A-260916'),
X('19_Kosten_und_Schaeden.xlsx','Kosten und Schadenmeldungen Kastanienhof',[dict(name='Gemeinschaft',headers=['Position','Netto EUR','USt EUR','Brutto EUR','Stand'],widths=[38,18,18,18,39],formats={c:'#,##0.00' for c in 'BCD'},rows=[['Provisorische Sicherung',200,"=ROUND(B2*0.19,2)",'=B2+C2','Bezahlt 14.09.2026'],['Rahmenreparatur',600,"=ROUND(B3*0.19,2)",'=B3+C3','Angebot OA-260916-12'],['Zusätzliche Schließung',1000,"=ROUND(B4*0.19,2)",'=B4+C4','Angebot SM-A-260916'],['Summe Optionen','=SUM(B2:B4)','=SUM(C2:C4)','=SUM(D2:D4)','Keine gemeinsame Beauftragung']],expected={'D5':2142},perturbations=[dict(input='B4',value=0,output='D5',expected=952)]),dict(name='Private_Meldungen',headers=['Gegenstand','Person','Kaufwert EUR','Nachweis','Versicherung'],widths=[27,25,19,35,27],formats={'C':'#,##0.00'},rows=[['E-Bike','Sana Özdemir',2299,'10_Kaufbeleg_E_Bike.docx','Hausratprüfung läuft'],['Kinderfahrrad','Benedikt Brösel',420,'11_Kaufbeleg_Kinderfahrrad.docx','Noch keine Meldung'],['Werkzeug','Yuna Albrecht',180,'Schätzung per E-Mail','Noch offen'],['Summe gemeldet','','=SUM(C2:C4)','Kein festgestellter Erstattungswert','']],expected={'C5':2899},perturbations=[dict(input='C4',value=0,output='C5',expected=2719)]),dict(name='Verteilung_Arbeitsblatt',headers=['Wohnung','MEA','Betrag im Vergleich EUR','Anteil nach MEA EUR','Je Einheit EUR'],widths=[22,16,28,28,28],formats={'B':'0','C':'#,##0.00','D':'#,##0.00','E':'#,##0.00'},rows=[[n,mea,714,f'=ROUND(C{r}*B{r}/1000,2)',f'=C{r}/6'] for r,(n,mea) in enumerate([(1,80),(2,120),(3,150),(4,180),(5,220),(6,250)],2)],expected={'D2':57.12,'E2':119,'D7':178.5},perturbations=[dict(input='C2',value=1000,output='D2',expected=80)])]),
D('20_Angebot_Kameras.docx','Kameraangebot Eingangsbereich und Keller','17.09.2026','Blickpunkt Sicherheitstechnik\nangebot@blickpunkt.example',WEG3, '''Wir bieten zwei netzwerkfähige Kameras, einen Recorder und die Montage für 2.400 EUR netto zuzüglich 456 EUR Umsatzsteuer, insgesamt 2.856 EUR brutto, an. Eine Kamera soll den Hauseingang innen erfassen, die zweite den Zugang zum Keller. Der Recorder kann technisch bis zu 30 Tage speichern; die tatsächliche Konfiguration ist vor Inbetriebnahme festzulegen.

Der vorgeschlagene Blickwinkel am Hauseingang erfasst alle eintretenden Personen und bei geöffneter Tür einen schmalen Teil des Gehwegs. Eine alternative Position könnte diesen Ausschnitt verkleinern. Eine reine Gegensprechanlage ohne dauerhafte Aufzeichnung ist in diesem Angebot nicht enthalten. Mobile Fernzugriffe können eingerichtet werden, müssen aber ausdrücklich bestellt und berechtigt werden.

Unser Angebot umfasst keine rechtliche Prüfung, keine Bewohnerinformation und keine Entscheidung über Berechtigte, Löschfristen oder Auskunftsverfahren. Ein Auftrag liegt noch nicht vor. Vor einer Installation benötigen wir die freigegebene Planung und die Benennung der für den Betrieb verantwortlichen Stelle.'''),
E('21_Beirat_Drei_Angebote.eml','Vor einer Entscheidung brauchen wir drei Angebote','2026-09-18T11:51:00+02:00','Hildegard Hummel <hildegard@hummel.example>','Noura Selim <verwaltung@havelhof.example>','''Liebe Frau Selim,

mein früherer Verwalter sagte immer, ohne genau drei Angebote dürfe überhaupt nichts beschlossen werden. Wir haben aber nur einen Tischler und einen Schlüsseldienst, die noch dazu verschiedene Dinge anbieten. Können wir trotzdem über die Rahmenreparatur entscheiden, wenn wir erklären, warum wir sie benötigen? Den provisorischen Riegel möchte ich nicht den ganzen Herbst behalten.

Bei den Kameras bin ich inzwischen unsicher. Ich wollte nicht, dass jemand meine täglichen Wege im Recorder sieht. Bitte schicken Sie kein Rundschreiben, das so tut, als hätten wir die Installation schon beschlossen.

Hildegard Hummel'''),
E('22_Verteilung_nach_Wohnungen.eml','Einmal durch sechs wäre doch einfacher','2026-09-18T16:33:00+02:00','Lotte Wackel <lotte@wackel.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

alle gehen durch dieselbe Kellertür. Ich möchte die Reparatur und vielleicht die neue Schließung daher gleichmäßig auf sechs Wohnungen verteilen. Frau Hummel hätte dann denselben Betrag wie Herr Fiedler. Ob das zu den sehr unterschiedlichen Wohnungsgrößen passt, weiß ich nicht. Können wir das einfach in denselben Beschluss schreiben?

Bitte rechnen Sie einmal beide Varianten vor. Es geht mir nicht um die privaten Räder; die sollen nicht in unsere Türrechnung geraten.

Freundliche Grüße
Lotte Wackel'''),
E('23_Mieterin_an_Vermieter.eml','Kellerdiebstahl und Zugang für die Reparatur','2026-09-19T08:49:00+02:00','Sana Özdemir <sana@ozdemir.example>','Ilyas Ben Salem <ilyas@bensalem.example>','''Sehr geehrter Herr Ben Salem,

ich habe meinen Hausratversicherer informiert. Bitte sorgen Sie dafür, dass der Keller wieder ordentlich schließt. Den genauen Termin brauche ich, weil mein Ladegerät noch im Abteil liegt. Für das Fahrrad verlange ich noch keinen bestimmten Betrag von Ihnen; zunächst möchte ich wissen, was über die vorherige Türstörung dokumentiert ist.

Im Hauschat heißt es, die Verwaltung müsse automatisch jedes gestohlene Fahrrad ersetzen. Das kann ich selbst nicht beurteilen. Bitte geben Sie meinen Kaufbeleg nicht an alle Eigentümer weiter. Für die Schadensbearbeitung bei der Versicherung können Sie ihn an die dafür zuständige Stelle übermitteln.

Freundliche Grüße
Sana Özdemir'''),
E('24_Vermieter_Weiterleitung.eml','WE2: Nachricht meiner Mieterin','2026-09-19T12:12:00+02:00','Ilyas Ben Salem <ilyas@bensalem.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

meine Mieterin bittet um Informationen zur Tür und zum Reparaturtermin. Bitte teilen Sie mit, was tatsächlich bekannt ist und was noch geprüft wird. Ich werde ihr selbst antworten. Einen Schadenersatzanspruch habe ich weder für mich noch für die Gemeinschaft anerkannt.

Die Aussage im Chat über den Paketboten stammt nicht von Sana. Bitte behandeln Sie sie nicht als Zeugenaussage. Ich würde gern wissen, ob es überhaupt einen konkreten Namen oder nur die Bemerkung „ein Mann mit Tasche“ gab.

Mit freundlichen Grüßen
Ilyas Ben Salem'''),
T('25_Hauschat_Ausschnitt.txt','Hauschat zum Keller','19.09.2026','''19.09.2026 19:06 Nepomuk: Vielleicht war es der Mann mit der großen Tasche von letzter Woche.
19.09.2026 19:07 Yuna: Das war mein Bruder mit dem Werkzeug. Das hat nichts mit Donnerstag zu tun.
19.09.2026 19:09 Hildegard: Bitte keine Namen raten. Ich habe nur die Tür gesehen.
19.09.2026 19:12 Lotte: Die Kamera müsste wenigstens alle Gesichter speichern, sonst bringt sie nichts.
19.09.2026 19:15 Sana: Ich möchte nicht auf Verdacht Nachbarn aufzeichnen. Erst die Tür reparieren.
19.09.2026 19:18 Noura: Der Hergang wird noch geprüft. Ich fasse die gesicherten Angaben morgen zusammen; bitte keine unbestätigten Vorwürfe weiterleiten.'''),
D('26_Schluesselliste.docx','Schlüsselbestand Kellerzugang','21.09.2026',HV,'Interne Objektverwaltung', '''Zum bisherigen Kellerzylinder wurden bei Einrichtung zwölf Schlüssel ausgegeben, je zwei pro Wohnung. Die Verwaltung hält keinen zusätzlichen Bewohnerersatzschlüssel. Der Hausdienst hat einen gesonderten Dienstschlüssel, der auch den Keller öffnet; sein Verbleib wurde am 21.09.2026 von Bruno Fink bestätigt.

Für Wohnung 6 hat Nepomuk Fiedler im Jahr 2023 einen weiteren Schlüssel auf eigene Kosten nachbestellen lassen. Die Nachbestellung wurde mit Sicherungskarte über die Verwaltung veranlasst. Ein Schlüsselverlust ist in der Objektakte nicht gemeldet. Nicht erfasst ist, wem die Eigentümer ihre jeweiligen Zweitschlüssel innerhalb des Haushalts oder Mietverhältnisses überlassen haben.

Eine vollständige namentliche Liste aller tatsächlichen Schlüsselbesitzer kann deshalb aus dieser Ausgabeübersicht nicht abgeleitet werden. Die Liste wurde für die Vorbereitung einer möglichen Umstellung erstellt und ist nicht für den Hauschat freigegeben.'''),
D('27_Beschlussentwurf_Tuer.docx','Entwurf zur dauerhaften Reparatur des Kellerzugangs','21.09.2026',HV,'Verwaltungsbeirat Kastanienhof 9', '''Die Gemeinschaft beauftragt die Tischlerei Ottokar Ast mit der Reparatur des beschädigten Türrahmens nach Angebot OA-260916-12 zum Preis von 714 EUR brutto. Die Verwaltung soll den Termin nach Abstimmung mit dem Versicherer vereinbaren. Zusatzleistungen sind von diesem Auftrag nicht umfasst und werden vor Beauftragung gesondert abgestimmt.

Für die Verteilung der Kosten ist in der vorliegenden Arbeitsfassung noch der Textbaustein „zu gleichen Teilen auf sämtliche Wohnungen“ eingetragen. Frau Selim hat daneben handschriftlich „MEA oder gesonderter Verteilungsbeschluss klären“ vermerkt. Der Betrag der provisorischen Sicherung ist in dieser Vorlage noch nicht gesondert erwähnt.

Der zusätzliche Zylinderwechsel und das Kameraangebot sollen nicht mit dieser Reparatur beauftragt werden. Die Vorlage ist bisher nur dem Beirat zur Abstimmung übersandt. Eine wirksame Beschlussfassung wird mit diesem gespeicherten Dokument nicht dokumentiert.'''),
E('28_Tischler_Termin.eml','OA-260916-12: Termin am 28. September','2026-09-22T07:36:00+02:00','Ottokar Ast <angebot@ottokarast.example>','Noura Selim <verwaltung@havelhof.example>','''Guten Morgen Frau Selim,

ich halte Montag, 28. September, 9 Uhr bis Freitagmittag für Sie frei. Danach muss ich den Auftrag neu einplanen. Die bisherige Sicherung sollte bis dahin ausreichen, wenn die Tür nicht gewaltsam betätigt wird. Ein Versicherungsbesuch wäre am Freitagvormittag noch möglich, ich muss dafür nicht anwesend sein.

Der Zylinderwechsel aus dem anderen Angebot ist nicht Voraussetzung meiner Rahmenreparatur. Bitte bestätigen Sie vor dem Termin den Auftrag und teilen Sie mit, wer uns Zugang gibt.

Freundliche Grüße
Ottokar Ast'''),
E('29_Versicherer_Besichtigung.eml','KH-261109: Besichtigung am Freitag','2026-09-22T13:45:00+02:00','Havel Schutz Schadenservice <schaden@havelschutz.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

unser Sachverständiger könnte am 25.09.2026 um 10 Uhr die Tür besichtigen. Bitte halten Sie das ausgebaute Schließblech und die Unterlagen zur Augustarbeit bereit. Die Prüfung soll auch klären, welcher Teil Wiederherstellung und welcher Teil Verbesserung ist. Wir möchten die Reparatur nicht unnötig verzögern, benötigen aber eine kurze Terminbestätigung.

Der Selbstbehalt von 500 EUR ist bei einer später festgestellten Deckung zu berücksichtigen. Eine pauschale Erstattung aller drei im Kostenblatt genannten Positionen ist derzeit nicht zugesagt.

Mit freundlichen Grüßen
Marta Winterfeld'''),
D('30_Bewohnerinformation_Entwurf.docx','Information zum Kellerzugang','22.09.2026',HV,'Bewohnerinnen und Bewohner Kastanienhof 9', '''Sehr geehrte Bewohnerinnen und Bewohner,

der Kellerzugang ist seit dem 11. September vorläufig gesichert. Wir bereiten eine dauerhafte Reparatur vor. Der angebotene Termin ist der 28. September; eine verbindliche Bestätigung folgt nach Abstimmung der noch offenen Punkte. Bitte schließen Sie die Tür sorgfältig und melden Sie neue Auffälligkeiten mit Zeitpunkt und eigener Beobachtung an die Verwaltung.

Der Hergang des Vorfalls ist noch nicht aufgeklärt. Vermutungen über einzelne Personen sollen nicht als Tatsachen verbreitet werden. Wer eigene Gegenstände vermisst, dokumentiert diese bitte und informiert seinen jeweiligen Versicherer sowie erforderlichenfalls die Polizei. Die Verwaltung führt den Gebäudeschaden getrennt von privaten Schadenmeldungen.

Über eine Kameraanlage ist noch nicht entschieden. Es gibt weder einen Installationsauftrag noch eine freigegebene Aufzeichnung. Die Verwaltung wird einen Vorschlag nur nach weiterer Prüfung und der erforderlichen Beschlussfassung umsetzen.

Mit freundlichen Grüßen
Noura Selim

Stand der internen Datei: 22.09.2026, noch nicht versandt.'''),
T('31_Telefonnotiz_Broesel.txt','Telefonnotiz Kinderfahrrad','22.09.2026','''22.09.2026 16:20, Noura Selim mit Benedikt Brösel.
Herr Brösel berichtet, das Kinderfahrrad sei am Dienstag zuletzt von ihm gesehen worden. Er hatte zunächst Donnerstag als letzten Tag genannt, weil er den Verlust zusammen mit Frau Özdemir am Freitag bemerkte. Sein Sohn war am Donnerstag nicht Fahrrad gefahren. Das Rad stand nach seiner Erinnerung unverschlossen im Gemeinschaftsregal.
Er hat die Rechnung gefunden. Eine Hausratversicherung besteht, der Vertrag liegt ihm aber noch nicht vor. Er möchte die Verlustmeldung ergänzen, nicht einen Anspruch gegen die Gemeinschaft beziffern. Frau Selim sagte zu, die geänderte Zeitangabe in der Akte zu vermerken.'''),
E('32_Nachtrag_Bearbeitungsauftrag.eml','Kastanienhof: Termin und Antwort an Versicherer','2026-09-23T09:18:00+02:00','Noura Selim <verwaltung@havelhof.example>','Friederike Morgen <kanzlei@morgen.example>','''Sehr geehrte Frau Morgen,

bitte liefern Sie zuerst die Antwort für den Versicherer und die Nachricht an die Bewohner. Die Besichtigung am 25. September und die Angebotsbindung sind die nächsten praktischen Termine. Danach brauchen wir die saubere Beschlussfassung zu Tür und Kosten. Die Kamera ist ein eigener, noch offener Vorgang.

Bitte setzen Sie keine private Fahrradforderung in die gemeinschaftliche Kostenabrechnung ein. Für Frau Özdemir und Herrn Ben Salem genügt zunächst eine sachliche Auskunft zu den eigenen Unterlagen der Gemeinschaft, ohne Haftungsanerkenntnis. Die neue Telefonnotiz zu Herrn Brösel ist beigefügt.

Mit freundlichen Grüßen
Noura Selim'''),
]
assert len(docs3) == 32
CASES.append(dict(slug='weg-kastanienhof-kellerdiebstahl',title='Kastanienhof und die offene Kellertür',plugin=PLUGIN,date='23.09.2026',client='Havel und Hof Hausverwaltung GmbH für die Gemeinschaft Kastanienhof 9',summary='Nach einem Kellereinbruch stehen Sicherung, Reparatur und Versicherungen an. Private Schäden, eine unklare Vorgeschichte der Tür und der Wunsch nach Kameras vermischen sich im Hauschat.',assignment='Die gesicherten Tatsachen und Schadenpositionen ordnen, fehlende Belege nachfordern, Versichererkorrespondenz und Bewohnerinformation erstellen sowie eine umsetzbare Beschlussvorlage vorbereiten.',documents=docs3,attachments={'08_Hausmeister_Antwort.eml':['09_Arbeitszettel_August.docx'],'14_Schadenmeldung_Gebaeude.eml':['04_Besichtigungsprotokoll.docx','06_Notdienstrechnung.docx'],'32_Nachtrag_Bearbeitungsauftrag.eml':['31_Telefonnotiz_Broesel.txt']}))

WEG4 = 'Gemeinschaft der Wohnungseigentümer Sonnenwinkel 12\nSonnenwinkel 12, Berlin'
docs4 = [
D('01_Auftrag_Bettwanzen.docx','Befall im Sonnenwinkel und die Kostenfrage','24.09.2026',HV,'Rechtsanwältin Friederike Morgen', '''Sehr geehrte Frau Morgen,

im Sonnenwinkel wurden in zwei Wohnungen Bettwanzen fachlich festgestellt. Die erste Meldung stammt aus Wohnung 4, eine spätere aus Wohnung 5. Der Schädlingsbekämpfer kann den Ausgangspunkt bisher nicht bestimmen. Die Eigentümerin von Wohnung 4 hat bereits eine erste Untersuchung beauftragt; die Gemeinschaft hat anschließend ein abgestimmtes Vorgehen beschlossen. Nun will ein Eigentümer sämtliche Rechnungen als laufende Betriebskosten weiterreichen.

Bitte klären Sie die Zuständigkeiten und erstellen Sie konkrete Schreiben an die betroffenen Eigentümer und Vermieter. Die Mieter sollen Zugangstermine und angemessene Hinweise erhalten, ohne dass ihnen ein unbewiesener Vorwurf gemacht wird. Wir brauchen außerdem eine nachvollziehbare Zuordnung der bisherigen Kosten und eine Entscheidungsvorlage für die noch anstehende Kontrolle. Private Erstattungswünsche sollen separat erfasst werden.

Die Gemeinschaft hat keine regelmäßige Schädlingsbekämpfungspauschale vereinbart. Es geht um diesen einzelnen Vorgang. Die vorhandenen Rechnungen, Zugangsabsprachen und Befundberichte sind beigefügt. Eine eigenständige medizinische Bewertung von Hautreaktionen oder Anleitung zur Selbstbehandlung ist nicht beauftragt. Bitte keine Namen betroffener Mieter in einen allgemeinen Hausbrief übernehmen.

Mit freundlichen Grüßen
Noura Selim'''),
D('02_Objekt_Mietverhaeltnisse.docx','Einheiten und Ansprechpartner Sonnenwinkel','03.08.2026',HV,'Interne Objektakte', '''Die Gemeinschaft Sonnenwinkel 12 besteht aus sechs Wohnungen. Alle Einheiten haben 90 m² Wohnfläche und gleiche Miteigentumsanteile. Die Verteilung gemeinschaftlicher Kosten richtet sich nach diesen Anteilen. Wohnung 4 gehört Roswitha Rumpel und ist seit 2022 an Amina Diop und Carlo Klee vermietet. Wohnung 5 gehört Theobald Schreck und ist seit 2024 an Linh Tran vermietet. Wohnung 6 bewohnt Eigentümerin Esmeralda Fuchs selbst.

Die Wohnungstrennwände, Leitungsschächte und gemeinschaftlichen Installationen sind gemeinschaftliches Eigentum. Die Wohnungsinnenausstattung und privaten Möbel stehen nicht im Eigentum der Gemeinschaft. Die Verwaltung verfügt über keine Generalschlüssel zu den Wohnungen. Zugang wird mit den jeweiligen Berechtigten konkret vereinbart.

Eine vorangegangene Schädlingsbekämpfung ist in der seit 2019 geführten Objektakte nicht dokumentiert. Es besteht kein Dauerdienstvertrag für Bekämpfung oder Monitoring. Die regelmäßige Treppenreinigung umfasst keine Schädlingsbehandlung.'''),
E('03_Erstmeldung_Mieter.eml','Kleine Insekten am Bett, bitte um Prüfung','2026-08-18T07:26:00+02:00','Amina Diop <amina@diop.example>','Roswitha Rumpel <roswitha@rumpel.example>','''Sehr geehrte Frau Rumpel,

seit einigen Tagen finden wir kleine Tiere am Bettgestell. Wir haben eines in einem verschlossenen Behälter aufbewahrt. Im Internet sieht vieles ähnlich aus; wir möchten nicht selbst raten. Carlo hat Hautreaktionen, lässt diese aber unabhängig davon ärztlich abklären.

Bitte organisieren Sie zeitnah eine fachliche Besichtigung. Wir waren im Juli auf einer Reise, haben aber auch im Juni ein gebrauchtes Regal gekauft. Ob irgendetwas damit zusammenhängt, wissen wir nicht. Wir möchten nicht, dass im Haus herumgeht, wir hätten die Tiere sicher eingeschleppt.

Freundliche Grüße
Amina Diop'''),
E('04_Vermieterin_Beauftragt_Befund.eml','Bitte Wohnung 4 fachlich untersuchen','2026-08-18T12:45:00+02:00','Roswitha Rumpel <roswitha@rumpel.example>','Sachverständigendienst Kiezklar <service@kiezklar.example>','''Sehr geehrte Damen und Herren,

ich beauftrage die angebotene Erstbesichtigung meiner vermieteten Wohnung 4 im Sonnenwinkel 12 für 297,50 EUR brutto. Die Mieter Amina Diop und Carlo Klee können am 20. August ab 15 Uhr Zugang ermöglichen. Bitte bestimmen Sie den Fund fachlich und teilen Sie mit, welche weiteren Untersuchungen sinnvoll sind.

Eine vollständige Bekämpfung, ein Öffnen gemeinschaftlicher Bauteile oder die Entsorgung von Möbeln sind mit diesem Erstauftrag noch nicht freigegeben. Bitte sprechen Sie zusätzliche Maßnahmen vorher mit mir und bei gemeinschaftlichen Bereichen mit der Verwaltung ab.

Mit freundlichen Grüßen
Roswitha Rumpel'''),
D('05_Befund_Wohnung4.docx','Befundbericht Wohnung 4','20.08.2026','Kiezklar Schädlingsmanagement GmbH\nFachberaterin Dr. Tessa Blum\nservice@kiezklar.example','Roswitha Rumpel', '''Am 20.08.2026 wurden die von den Bewohnern gesicherten Exemplare untersucht und als Bettwanzen bestimmt. Bei der Besichtigung fanden sich weitere Spuren am Bettgestell und in dessen unmittelbarer Umgebung. Die Untersuchung bestätigt einen Befall der Wohnung 4. Eine medizinische Diagnose bei Bewohnern wurde nicht vorgenommen.

Der Zeitpunkt des Eintrags und der Ausgangspunkt lassen sich aus diesem Befund nicht verlässlich ableiten. Reisegepäck, gebrauchte Gegenstände oder ein Übergang aus anderen Bereichen sind ohne zusätzliche Feststellungen keine bewiesene Ursache. Die sichtbare Ordnung oder Sauberkeit der Wohnung erlaubt keine eindeutige Aussage darüber, wie die Tiere eingetragen wurden.

Wir empfehlen ein abgestimmtes Vorgehen mit der Verwaltung und eine fachliche Prüfung angrenzender Bereiche. Maßnahmen in anderen Wohnungen erfordern abgestimmte Zugangstermine. Überflüssiges Umstellen von Gegenständen in gemeinschaftliche Flure sollte bis zur fachlichen Abstimmung unterbleiben. Die konkrete Durchführung und produktspezifische Sicherheitsunterweisung erfolgen ausschließlich durch den beauftragten Fachbetrieb.

Der Bericht umfasst die Untersuchung vom 20. August; er erklärt nicht sämtliche weiteren Wohnungen für befallsfrei.'''),
D('06_Rechnung_Erstbesichtigung.docx','Rechnung Erstbesichtigung Wohnung 4','21.08.2026','Kiezklar Schädlingsmanagement GmbH','Roswitha Rumpel', '''Für die beauftragte Besichtigung und fachliche Bestimmung am 20.08.2026 berechnen wir 250 EUR netto zuzüglich 47,50 EUR Umsatzsteuer, insgesamt 297,50 EUR brutto. Die Leistung umfasst Anfahrt, Untersuchung der vorgelegten Exemplare, Besichtigung des betroffenen Bereichs und den schriftlichen Befundbericht.

Eine Behandlung anderer Wohnungen und die Durchführung weiterer Kontrollen sind nicht enthalten. Der Betrag ist bis zum 04.09.2026 zu zahlen. Eine Beauftragung oder Zahlung der Gemeinschaft ist in unserem Kundenkonto nicht erfasst.

Bitte verwenden Sie bei Rückfragen die Rechnungsnummer KK-260821-4. Die Benennung der Rechnungsempfängerin enthält keine Feststellung dazu, wer die Kosten im Innenverhältnis letztlich tragen muss.''',reference='KK-260821-4'),
E('07_Meldung_an_Verwaltung.eml','Befund Wohnung 4 und gemeinschaftliche Bereiche','2026-08-21T09:43:00+02:00','Roswitha Rumpel <roswitha@rumpel.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

anbei der fachliche Befund. Bitte stimmen Sie mit dem Unternehmen ab, ob gemeinschaftliche Schächte oder angrenzende Wohnungen untersucht werden müssen. Ich habe zunächst nur die Untersuchung in meiner Wohnung beauftragt. Eine Verursachung durch meine Mieter ist damit ausdrücklich nicht nachgewiesen.

Ich möchte die Kostenfrage getrennt besprechen. Mir geht es jetzt darum, dass keine unkoordinierten Einzelmaßnahmen den Ablauf erschweren. Bitte behandeln Sie Namen und Gesundheitsangaben vertraulich.

Mit freundlichen Grüßen
Roswitha Rumpel'''),
E('08_Folgemeldung_Wohnung5.eml','Auch bei mir wurde ein Tier gefunden','2026-08-24T20:18:00+02:00','Linh Tran <linh@tran.example>','Theobald Schreck <theobald@schreck.example>','''Guten Abend Herr Schreck,

ich habe heute ein Tier am Sofa gefunden und getrennt gesichert. Ob es dasselbe ist wie bei den Nachbarn, kann ich nicht sagen. Bitte organisieren Sie eine Prüfung. Ich bin Mittwoch nach 16 Uhr oder Donnerstag vormittags da.

Ich habe bisher nichts auf den Flur gestellt und keinen Fachbetrieb eigenständig beauftragt. Aus dem Hauschat möchte ich nicht erfahren müssen, dass ich angeblich die Ursache bin. Bitte geben Sie keine Behauptung weiter, nur weil mein Sofa gebraucht gekauft war.

Linh Tran'''),
D('09_Folgebefund_Wohnung5.docx','Befundbericht Wohnung 5 und Anschlussbereiche','27.08.2026','Kiezklar Schädlingsmanagement GmbH',HV, '''Am 27.08.2026 wurde das in Wohnung 5 gesicherte Exemplar ebenfalls als Bettwanze bestimmt. Weitere Spuren wurden am Sofa festgestellt. Im zugänglichen Abschnitt des Installationsschachts zwischen den Wohnungen 4 und 5 fanden sich bei dieser Sichtprüfung keine eindeutigen Befunde. Verdeckte Bereiche wurden nicht geöffnet.

Die Untersuchung kann einen Übergang zwischen Wohnungen weder beweisen noch ausschließen. Auch die Reihenfolge der Meldungen erlaubt keinen sicheren Schluss auf die zuerst betroffene Wohnung. Eine Aussage, Amina Diop, Carlo Klee oder Linh Tran hätten den Befall verursacht, ist fachlich nicht begründet.

Wir schlagen eine abgestimmte Behandlung beider bestätigten Befallsbereiche mit nachfolgenden Kontrollen vor. Weitere Wohnungen sollen bei konkreten Hinweisen oder nach fachlicher Einschätzung gezielt einbezogen werden. Pauschale Erklärungen über die Befallsfreiheit des ganzen Hauses sind vor Abschluss der vorgesehenen Kontrollen nicht möglich.'''),
D('10_Angebot_Kiezklar.docx','Angebot abgestimmter Maßnahmen für zwei Wohnungen','28.08.2026','Kiezklar Schädlingsmanagement GmbH',WEG4, '''Für die koordinierte Behandlung der bestätigten Befallsbereiche in den Wohnungen 4 und 5 bieten wir einen ersten Einsatz für 1.200 EUR netto zuzüglich 228 EUR Umsatzsteuer, insgesamt 1.428 EUR brutto, an. Darin enthalten sind die Terminabstimmung, die fachgerechte Durchführung und ein schriftlicher Einsatzbericht. Eine Kontrolle mit erforderlicher fachlicher Nachbearbeitung wird gesondert für 600 EUR netto zuzüglich 114 EUR Umsatzsteuer, insgesamt 714 EUR brutto, angeboten.

Der erste Einsatz ist für den 03.09.2026 vorgesehen. Die Kontrolle soll nach Abstimmung am 17.09.2026 erfolgen. Zusätzliche Einsätze werden vor Beauftragung gesondert beschrieben und beziffert. Ein bestimmter Erfolg nach einem einzigen Termin wird nicht garantiert. Die Bewohner erhalten die für den konkreten Einsatz erforderlichen Hinweise unmittelbar durch unser Fachpersonal.

Die Erstuntersuchung in Wohnung 4 ist bereits gesondert abgerechnet und in diesen Beträgen nicht nochmals enthalten. Abdichtungsarbeiten durch einen Handwerksbetrieb und private Reinigungskosten sind ebenfalls nicht enthalten. Die Frage einer rechtlichen Kostentragung zwischen Gemeinschaft, Eigentümern und Mietern ist nicht Gegenstand unseres Angebots.''',reference='KK-A-260828'),
D('11_Vergleichsangebot.docx','Angebot Sichtprüfung und weitere Planung','29.08.2026','Befund und Ruhe Schädlingsservice\nangebot@befundruhe.example',WEG4, '''Wir bieten eine erneute Sichtprüfung beider betroffener Wohnungen einschließlich Bericht für 420 EUR netto zuzüglich 79,80 EUR Umsatzsteuer, insgesamt 499,80 EUR brutto, an. Ein erster Termin wäre am 11.09.2026 möglich. Die eigentliche Behandlung und spätere Kontrollen sind nicht Bestandteil dieses Betrags; hierfür würden wir nach der Besichtigung ein weiteres Angebot erstellen.

Vorhandene Befundberichte können Sie uns vorab übermitteln. Wir übernehmen nicht ohne eigene Untersuchung die Beurteilung des bisherigen Dienstleisters. Der angebotene Betrag ist deshalb nicht unmittelbar mit einem bereits bezifferten Behandlungsangebot für beide Wohnungen vergleichbar.

Das Angebot ist bis zum 08.09.2026 gültig. Einen Auftrag oder eine Terminreservierung haben wir bisher nicht erhalten.'''),
D('12_Beschluss_Abgestimmtes_Vorgehen.docx','Beschluss zur koordinierten Bearbeitung des Befalls','31.08.2026',WEG4,'Niederschrift der außerordentlichen Eigentümerversammlung', '''Die Gemeinschaft beauftragt Kiezklar Schädlingsmanagement mit dem im Angebot KK-A-260828 bezeichneten ersten Einsatz in beiden betroffenen Wohnungen für 1.428 EUR brutto und der Kontrolle für 714 EUR brutto. Die Verwaltung stimmt die Zugangstermine mit den Eigentümern und Mietern ab. Die Gemeinschaft verauslagt diese beiden Beträge aus dem laufenden Konto. Über eine mögliche Erstattung durch Dritte wird damit nicht entschieden.

Die Eigentümer wurden darüber informiert, dass die Ursache fachlich noch offen ist und die Vergleichsanfrage nur eine spätere Untersuchung, nicht dieselben Behandlungsleistungen umfasst. Fünf Eigentümer stimmen zu, Theobald Schreck enthält sich. Eine Kostenumlage auf einzelne Mieter oder ein personenbezogener Verursacherbeschluss werden nicht gefasst.

Ein Angebot für eine fachlich empfohlene Abdichtung soll getrennt eingeholt werden. Die Verwaltung darf für diesen zusätzlichen Auftrag aus diesem Beschluss noch keine Zahlung zusagen. Weitere Bekämpfungstermine über die genannten Leistungen hinaus bedürfen einer erneuten Abstimmung, soweit keine anderweitige Befugnis besteht.'''),
E('13_Zugangsabstimmung.eml','Sonnenwinkel: Termine am 3. September','2026-09-01T10:47:00+02:00','Noura Selim <verwaltung@havelhof.example>','Amina Diop und Linh Tran <termine@bewohner-sonnenwinkel.example>','''Sehr geehrte Frau Diop, sehr geehrte Frau Tran,

der Fachbetrieb schlägt für Wohnung 4 am 3. September 9 Uhr und für Wohnung 5 am selben Tag 11 Uhr vor. Bitte bestätigen Sie jeweils Ihren eigenen Zugang. Eine Weitergabe Ihres Wohnungsschlüssels an andere Bewohner ist nicht erforderlich. Der Fachbetrieb erläutert Ihnen seine konkreten vorbereitenden Hinweise direkt.

Die Nachricht enthält keine Festlegung zur endgültigen Kostentragung. Bitte stellen Sie bis zur Abstimmung keine Gegenstände in den Gemeinschaftsflur. Falls der Termin wegen Arbeit oder Betreuung nicht möglich ist, teilen Sie uns eine konkrete Alternative mit.

Mit freundlichen Grüßen
Noura Selim'''),
E('14_Abweichender_Termin.eml','Wohnung 5: 11 Uhr geht nicht','2026-09-01T16:02:00+02:00','Linh Tran <linh@tran.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

ich habe am Donnerstag eine medizinische Untersuchung und komme voraussichtlich erst gegen 12.30 Uhr zurück. Ich kann den Zugang ab 13 Uhr ermöglichen. Meine Nachbarin hat keinen Schlüssel und soll auch keinen bekommen. Bitte werten Sie die Uhrzeitänderung nicht als Verweigerung des Termins.

Am 17. September bin ich ganztägig verfügbar. Wenn der erste Termin um 13 Uhr nicht möglich ist, könnte ich Freitag ab 8 Uhr. Bitte bestätigen Sie die tatsächliche Zeit, damit ich nicht den ganzen Nachmittag warten muss.

Freundliche Grüße
Linh Tran'''),
E('15_Bestaetigung_Dienstleister.eml','Wohnung 5 am 3. September um 13 Uhr','2026-09-02T09:20:00+02:00','Kiezklar Disposition <service@kiezklar.example>','Noura Selim <verwaltung@havelhof.example>','''Guten Morgen Frau Selim,

die Verschiebung von Wohnung 5 auf 13 Uhr ist möglich und verursacht keine Zusatzkosten. Wohnung 4 bleibt bei 9 Uhr. Wir haben beide Bewohnerinnen direkt informiert und ihre Bestätigungen erhalten. Unsere Mitarbeitenden führen die einsatzbezogene Unterweisung jeweils vor Ort durch.

Bitte streichen Sie die alte 11-Uhr-Angabe aus dem Terminblatt. Für den 17. September bleibt die Kontrolle ab 9 Uhr vorgesehen; die genaue Reihenfolge stimmen wir vorher ab.

Viele Grüße
Tessa Blum'''),
D('16_Einsatzbericht_Erster_Termin.docx','Einsatzbericht vom 3 September','03.09.2026','Kiezklar Schädlingsmanagement GmbH',WEG4, '''Der beauftragte erste Einsatz wurde am 03.09.2026 in Wohnung 4 ab 9 Uhr und in Wohnung 5 ab 13 Uhr durchgeführt. Beide Wohnungen waren zum jeweils vereinbarten Termin zugänglich. Eine erfolglose Anfahrt ist nicht angefallen. Die Bewohner erhielten die konkreten Hinweise durch die eingesetzten Fachkräfte und bestätigten deren Empfang.

Die Bearbeitung bezog sich auf die fachlich festgestellten Bereiche. Das Vorgehen und die verwendeten zugelassenen Mittel sind in der beim Unternehmen geführten Einsatzdokumentation hinterlegt. Dieser Verwaltungsbericht enthält keine Anleitung zur eigenständigen Anwendung. Für Rückfragen sollen die Bewohner unmittelbar den Fachbetrieb kontaktieren.

Die Kontrolle am 17. September bleibt erforderlich. Aus dem Abschluss des ersten Einsatzes wird keine endgültige Befallsfreiheit abgeleitet. Die Ursache und eine personenbezogene Verantwortung sind weiterhin nicht festgestellt. Im zugänglichen Schachtbereich wurde eine bauliche Fuge vermerkt, deren Abdichtung gesondert durch einen geeigneten Handwerksbetrieb geprüft werden soll.'''),
D('17_Rechnung_Erster_Einsatz.docx','Rechnung koordinierter Einsatz','04.09.2026','Kiezklar Schädlingsmanagement GmbH',WEG4, '''Für den ersten Einsatz in den Wohnungen 4 und 5 am 03.09.2026 berechnen wir gemäß Angebot KK-A-260828 1.200 EUR netto zuzüglich 228 EUR Umsatzsteuer, insgesamt 1.428 EUR brutto. Der Betrag umfasst beide Wohnungen und die abgestimmte Terminänderung. Eine gesonderte Ausfallpauschale wird nicht berechnet.

Die Zahlung ging am 09.09.2026 vom Konto der Gemeinschaft ein. Eine interne Aufteilung auf die beiden Eigentümer oder deren Mieter haben wir nicht vorgenommen. Die Erstbesichtigung von Wohnung 4 wird nicht nochmals berechnet. Die spätere Kontrolle ist Gegenstand einer eigenen Rechnung.

Die Rechnung trägt die Nummer KK-260904-12 und ist vollständig ausgeglichen.''',reference='KK-260904-12'),
D('18_Kontrollbericht.docx','Kontrolle am 17 September','17.09.2026','Kiezklar Schädlingsmanagement GmbH',WEG4, '''Am 17.09.2026 waren beide Wohnungen nach vereinbarter Reihenfolge zugänglich. In Wohnung 4 wurden bei der Kontrolle keine lebenden Exemplare festgestellt. In Wohnung 5 wurde ein weiterer eindeutiger Befund erhoben und fachlich nachbearbeitet. Die Kontrollleistung einschließlich der vorgesehenen Nachbearbeitung fällt unter das Angebot vom 28. August.

Ein einzelner unauffälliger Kontrolltermin reicht nicht aus, um eine dauerhafte Befallsfreiheit sämtlicher Bereiche des Hauses zu bestätigen. Wir empfehlen eine weitere Kontrolle beider Wohnungen Anfang Oktober. Dies wäre eine zusätzliche, noch zu beauftragende Leistung. Die Gemeinschaft sollte den Zugang rechtzeitig abstimmen.

Aus dem erneuten Befund in Wohnung 5 kann nicht auf einen Neueintrag durch Frau Tran geschlossen werden. Ebenso wenig belegt die frühere Meldung aus Wohnung 4 einen von dort ausgehenden Eintrag. Der Zusammenhang bleibt fachlich offen.'''),
D('19_Rechnung_Kontrolle.docx','Rechnung Kontrolle und Nachbearbeitung','18.09.2026','Kiezklar Schädlingsmanagement GmbH',WEG4, '''Für die Kontrolle und im vereinbarten Umfang ausgeführte Nachbearbeitung am 17.09.2026 berechnen wir 600 EUR netto zuzüglich 114 EUR Umsatzsteuer, insgesamt 714 EUR brutto. Die Rechnung beruht auf dem zweiten ausdrücklich angebotenen Leistungsblock im Angebot KK-A-260828.

Der Betrag ist bis zum 02.10.2026 zu zahlen. Am Ausstellungsdatum ist noch kein Zahlungseingang gebucht. Eine weitere Kontrolle im Oktober ist nicht in dieser Rechnung enthalten. Ihre Kosten werden nur aufgrund eines gesonderten Auftrags abgerechnet.

Bitte geben Sie im Verwendungszweck KK-260918-12 an. Die bestehende Gemeinschaftsbeauftragung wird nicht durch eine Rechnung gegen einen einzelnen Mieter ersetzt.''',reference='KK-260918-12'),
D('20_Angebot_Fugenabdichtung.docx','Angebot Abdichtung gemeinschaftlicher Anschlussfuge','19.09.2026','Dicht und Gut Bauhandwerk\nangebot@dichtgut.example',WEG4, '''Wir bieten die fachgerechte Abdichtung der zugänglichen Anschlussfuge im gemeinschaftlichen Installationsbereich zwischen den Wohnungen 4 und 5 für 450 EUR netto zuzüglich 85,50 EUR Umsatzsteuer, insgesamt 535,50 EUR brutto, an. Die Arbeiten sollen nach Abstimmung mit dem Schädlingsfachbetrieb erfolgen. Eine Öffnung weiterer Bauteile ist nicht umfasst.

Die Abdichtung ist eine bauliche Maßnahme und kein Ersatz für die erforderlichen Kontrollen. Wir bestätigen weder eine bestimmte Herkunft des Befalls noch, dass diese einzelne Fuge dessen Ausbreitungsweg war. Der angebotene Termin ist der 06.10.2026 ab 9 Uhr. Für Arbeiten innerhalb der Wohnungen muss der Zugang gesondert vereinbart werden.

Das Angebot ist bis zum 30.09.2026 gültig. Eine Beauftragung liegt nicht vor. Mehrleistungen werden nur nach Rücksprache und zusätzlicher Freigabe ausgeführt.'''),
E('21_Schreck_Will_Umlage.eml','Die Rechnungen gehören in die Betriebskosten','2026-09-20T11:23:00+02:00','Theobald Schreck <theobald@schreck.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

Schädlingsbekämpfung steht doch irgendwo in den Betriebskosten. Bitte verteilen Sie deshalb sämtliche Beträge einschließlich Fugenarbeiten in der nächsten Abrechnung und schreiben Sie in meiner Mieterliste „umlagefähig“. Frau Tran hat ein gebrauchtes Sofa; für mich liegt der Zusammenhang nahe.

Ich habe noch keinen Fachbeleg für diese Vermutung. Trotzdem möchte ich nicht als Eigentümer zahlen. Falls die Gemeinschaft mir etwas belastet, reiche ich das einfach vollständig an die Mieterin weiter. Bitte schicken Sie mir dafür einen fertigen Absatz.

Mit freundlichen Grüßen
Theobald Schreck'''),
D('22_Mietvertrag_Wohnung5.docx','Mietvertrag Sonnenwinkel Wohnung 5','10.06.2024','Theobald Schreck','Linh Tran', '''1. Mietgegenstand und Beginn

Theobald Schreck vermietet Linh Tran die Wohnung 5 im Sonnenwinkel 12 in Berlin mit 90 m² Wohnfläche. Die Wohnung umfasst drei Zimmer, Küche, Bad und Flur. Das Mietverhältnis beginnt am 01.07.2024 und läuft auf unbestimmte Zeit. Ein Kellerabteil wird zur Nutzung überlassen.

2. Miete und Betriebskosten

Die monatliche Nettokaltmiete beträgt 1.170 EUR. Für Betriebskosten einschließlich Heizung werden monatlich 290 EUR vorausgezahlt. Der Vermieter rechnet kalenderjährlich ab. Umlagefähig sind die nach der Betriebskostenverordnung vereinbarten laufenden Betriebskosten, soweit sie tatsächlich anfallen. Eine allgemeine Pflicht der Mieterin, sämtliche vom Wohnungseigentümer gezahlten Gemeinschaftskosten zu erstatten, wird nicht vereinbart.

3. Erhaltung und Mängelanzeige

Die Mieterin zeigt auftretende Mängel dem Vermieter ohne schuldhaftes Zögern an. Der Vermieter veranlasst die im Rahmen seiner Pflichten erforderliche Prüfung und Abhilfe. Ein Zugang zu erforderlichen Arbeiten wird nach Ankündigung unter Berücksichtigung berechtigter Interessen abgestimmt. Eine generelle Schlüsselhinterlegung bei der Hausverwaltung ist nicht vereinbart.

4. Verantwortlichkeit

Gesetzliche Ansprüche wegen schuldhaft verursachter Schäden bleiben unberührt. Weder die bloße Feststellung eines Mangels in der Wohnung noch die Reihenfolge einer Meldung wird durch den Vertrag als Nachweis eines Verschuldens festgelegt. Zusätzliche Vereinbarungen über einen laufenden Schädlingsbekämpfungsdienst bestehen nicht.

Theobald Schreck und Linh Tran haben den Vertrag am 10.06.2024 unterzeichnet.'''),
E('23_Mieterin_Widerspricht.eml','Ihre Nachricht zur Kostenübernahme','2026-09-21T08:04:00+02:00','Linh Tran <linh@tran.example>','Theobald Schreck <theobald@schreck.example>','''Sehr geehrter Herr Schreck,

ich habe Ihre Nachricht verstanden, dass Sie mir alle Kosten weiterreichen wollen. Damit bin ich nicht einverstanden. Der Fachbericht sagt gerade nicht, dass mein Sofa die Ursache war. Ich habe den ersten Fund sofort gemeldet und alle abgestimmten Termine ermöglicht. Die Änderung von 11 auf 13 Uhr war bestätigt und kostenfrei.

Bitte schicken Sie mir die genaue Forderung und ihre Grundlage, falls Sie daran festhalten. Ich möchte eine weitere Kontrolle ermöglichen; das ist keine Anerkennung einer Zahlungspflicht. Für einen Termin Anfang Oktober kann ich Montag nach 15 Uhr oder Dienstagvormittag anbieten.

Mit freundlichen Grüßen
Linh Tran'''),
D('24_Waschereibeleg.docx','Beleg über beauftragte Wäschereileistung','08.09.2026','Waschsalon Seifenblase\nservice@seifenblase.example','Amina Diop', '''Am 07.09.2026 wurden die von der Kundin bezeichneten Textilien nach zuvor mit dem Fachbetrieb abgestimmter Behandlung zur Reinigung übernommen und am Folgetag zurückgegeben. Für die vereinbarte Dienstleistung werden 72,61 EUR netto zuzüglich 13,79 EUR Umsatzsteuer, insgesamt 86,40 EUR brutto, berechnet.

Die Kundin zahlte bei Abholung mit Karte. Der Waschsalon bescheinigt die ausgeführte Reinigungsleistung, nicht eine fachliche Befallsdiagnose oder die Verantwortlichkeit Dritter. Gegenstände wurden nicht im Gemeinschaftsflur abgestellt. Die Abholbestätigung ist auf denselben Auftrag bezogen.

Auftragsnummer SB-260907-18. Die Rechnung ist vollständig bezahlt.''',reference='SB-260907-18'),
E('25_Erstattungsbitte_Mieter.eml','Kosten Wäscherei und zusätzlicher Aufwand','2026-09-21T17:22:00+02:00','Amina Diop <amina@diop.example>','Roswitha Rumpel <roswitha@rumpel.example>','''Sehr geehrte Frau Rumpel,

anbei der Beleg über 86,40 EUR. Wir bitten um Prüfung, ob Sie uns diese Kosten erstatten. Wir haben außerdem zwei Nachmittage für die Termine freigehalten. Dafür stellen wir zunächst keinen Betrag in Rechnung. Eine Hotelübernachtung war nicht erforderlich und wird nicht verlangt.

Carlo hat eine neue Matratze gekauft, aber wir wissen selbst noch nicht, ob der Kauf nötig war oder eher seine persönliche Entscheidung. Wir möchten den Kauf deshalb nicht einfach in dieselbe Forderung aufnehmen. Bitte geben Sie die Wäschereirechnung nicht ohne Anlass in den Hauschat.

Mit freundlichen Grüßen
Amina Diop'''),
T('26_Hauschat_Befall.txt','Hauschat Sonnenwinkel','22.09.2026','''22.09.2026 18:10 Esmeralda: Bitte stellt keine Matratzen auf den Flur. Dort kommt man mit dem Kinderwagen kaum durch.
22.09.2026 18:12 Amina: Von uns steht dort nichts. Das braune Regal gehört zum Umzug im Erdgeschoss.
22.09.2026 18:14 Theobald: Irgendjemand muss das doch angeschleppt haben.
22.09.2026 18:17 Roswitha: Der Fachbericht sagt, die Ursache ist offen. Wir brauchen zuerst die Kontrolle.
22.09.2026 18:20 Noura: Bitte meldet eigene Beobachtungen direkt an uns. Namen, Gesundheitsangaben und Vermutungen gehören nicht in diesen Verteiler.
22.09.2026 18:23 Linh: Danke. Ich habe die Termine nicht verweigert. 13 Uhr war bestätigt.'''),
X('27_Kosten_und_Termine.xlsx','Kosten und Zugang Sonnenwinkel',[dict(name='Kosten',headers=['Vorgang','Brutto EUR','Bezahlt EUR','Offen EUR','Auftraggeber und Stand'],widths=[38,19,19,19,43],formats={c:'#,##0.00' for c in 'BCD'},rows=[['Erstbesichtigung',297.50,297.50,'=B2-C2','Roswitha Rumpel, bezahlt'],['Erster Einsatz',1428,1428,'=B3-C3','Gemeinschaft, bezahlt'],['Kontrolle September',714,0,'=B4-C4','Gemeinschaft, beauftragt'],['Fugenabdichtung',535.50,0,'=B5-C5','Nur Angebot, nicht beauftragt'],['Wäscherei',86.40,86.40,'=B6-C6','Amina Diop, Erstattung erbeten'],['Summe Unterlagen','=SUM(B2:B6)','=SUM(C2:C6)','=SUM(D2:D6)','Keine Festlegung der Tragung']],expected={'B7':3061.40,'C7':1811.90,'D7':1249.50},perturbations=[dict(input='C4',value=714,output='D7',expected=535.50)]),dict(name='Zugang',headers=['Datum','Wohnung','Bestätigte Uhrzeit','Status','Quelle'],widths=[19,16,25,34,42],rows=[['20.08.2026',4,'15:00','Erfolgt','05_Befund_Wohnung4.docx'],['27.08.2026',5,'10:00','Erfolgt','09_Folgebefund_Wohnung5.docx'],['03.09.2026',4,'09:00','Erfolgt','16_Einsatzbericht_Erster_Termin.docx'],['03.09.2026',5,'13:00','Erfolgt, keine Ausfallkosten','15_Bestaetigung_Dienstleister.eml'],['17.09.2026',4,'09:00','Erfolgt','18_Kontrollbericht.docx'],['17.09.2026',5,'10:30','Erfolgt','18_Kontrollbericht.docx'],['06.10.2026',4,'09:00','Noch abzustimmen','20_Angebot_Fugenabdichtung.docx'],['06.10.2026',5,'09:00','Noch abzustimmen','20_Angebot_Fugenabdichtung.docx']],formats={'B':'0'},expected={'B2':4})]),
D('28_Angebot_Oktoberkontrolle.docx','Angebot weitere Kontrolle im Oktober','22.09.2026','Kiezklar Schädlingsmanagement GmbH',WEG4, '''Für eine weitere Kontrolle der Wohnungen 4 und 5 bieten wir 300 EUR netto zuzüglich 57 EUR Umsatzsteuer, insgesamt 357 EUR brutto, an. Es handelt sich um eine neue Leistung nach den bereits beauftragten Septemberterminen. Zusätzliche Maßnahmen bei einem erneuten Befund würden vor Durchführung gesondert beschrieben und abgestimmt.

Ein Termin ist am 05.10.2026 ab 15 Uhr möglich. Für Wohnung 5 wurde bisher nur eine Verfügbarkeit am Montag nach 15 Uhr oder Dienstagvormittag genannt; für Wohnung 4 fehlt eine verbindliche Rückmeldung. Die anschließende bauliche Abdichtung muss mit dem ausführenden Handwerksbetrieb koordiniert werden.

Die Rechnung vom 18. September enthält diese Oktoberkontrolle nicht. Bitte senden Sie eine eindeutige Beauftragung und die abgestimmten Zugangsdaten. Ohne Bestätigung fahren wir die Wohnungen nicht auf Verdacht an.'''),
E('29_Beirat_Kostenfrage.eml','Wer zahlt was und welcher Beschluss fehlt?','2026-09-23T09:42:00+02:00','Esmeralda Fuchs <esmeralda@fuchs.example>','Noura Selim <verwaltung@havelhof.example>','''Liebe Frau Selim,

in der Tabelle steht alles zusammen, auch die privat bezahlte Erstbesichtigung und die Wäscherei. Bitte verhindern Sie, dass die Gesamtsumme ohne Prüfung als Gemeinschaftsausgabe gebucht wird. Zugleich soll Frau Rumpel ihre Frage nach Erstattung ordentlich stellen können.

Für die Fuge haben wir noch keinen Auftrag beschlossen. Die Oktoberkontrolle steht ebenfalls erst als Angebot im Raum. Ich möchte nicht, dass wegen der Kostenfrage die Termine aus dem Blick geraten. Können wir die erforderlichen Schritte und die spätere Tragung sauber getrennt entscheiden?

Viele Grüße
Esmeralda'''),
D('30_Eigentuemerbrief_Vorfassung.docx','Hinweis auf zusätzliche Kosten im Sonnenwinkel','23.09.2026',HV,'Eigentümerinnen und Eigentümer Sonnenwinkel 12', '''Sehr geehrte Damen und Herren,

im Zusammenhang mit dem derzeitigen Befall liegen uns verschiedene Rechnungen und Angebote vor. Die Verwaltung beabsichtigt, die im Kostenblatt genannten Beträge in der Jahresabrechnung zu berücksichtigen. In der bisherigen internen Textvorlage steht dazu „sämtliche Maßnahmen als umlagefähige Schädlingsbekämpfungskosten erfassen“.

Der Beirat hat dieser pauschalen Formulierung widersprochen und eine Trennung nach Auftrag, Zahlung und Gegenstand verlangt. Der Brief ist deshalb noch nicht versandt. Die von einzelnen Eigentümern oder Mietern privat bezahlten Leistungen werden bis zur Klärung nicht als bereits aus dem Gemeinschaftskonto bezahlt bezeichnet.

Für die nächste Kontrolle und die angebotene Abdichtung werden konkrete Entscheidungen vorbereitet. Über eine Verantwortung einer bestimmten Person ist bislang keine Feststellung getroffen worden.

Mit freundlichen Grüßen
Noura Selim'''),
E('31_Vermieterin_Klaert_Auftrag.eml','Erstbesichtigung war mein eigener Auftrag','2026-09-23T14:11:00+02:00','Roswitha Rumpel <roswitha@rumpel.example>','Noura Selim <verwaltung@havelhof.example>','''Sehr geehrte Frau Selim,

ich bestätige nochmals, dass ich die 297,50 EUR selbst beauftragt und am 25.08.2026 aus meinem Privatkonto bezahlt habe. Ich bitte um Prüfung einer möglichen Erstattung, behaupte aber nicht, die Gemeinschaft hätte den Auftrag damals erteilt. Meine Mieter haben die Meldung frühzeitig gemacht und kooperiert.

Der Wäschereibeleg betrifft deren eigene Zahlung. Bitte unterscheiden Sie diese Forderung von meiner Rechnung. Eine Abtretung oder gemeinsame Zahlungsvereinbarung gibt es nicht. Ich möchte beiden gegenüber nachvollziehbar erklären können, wie weiter vorgegangen wird.

Mit freundlichen Grüßen
Roswitha Rumpel'''),
E('32_Abschlussauftrag_Verwaltung.eml','Sonnenwinkel: Jetzt konkrete Briefe und Entscheidungsvorlage','2026-09-24T11:36:00+02:00','Noura Selim <verwaltung@havelhof.example>','Friederike Morgen <kanzlei@morgen.example>','''Sehr geehrte Frau Morgen,

bitte erstellen Sie die Antwort an Herrn Schreck, einen diskreten allgemeinen Bewohnerhinweis und eine Vorlage für die weitere Beauftragung. Für die Buchhaltung benötigen wir die eindeutige Trennung von bezahlter Gemeinschaftsleistung, offener Rechnung, bloßem Angebot und privater Erstattungsbitte. Die Unterlagen sollen anschließend bei Rückfragen nicht wieder vermischt werden.

Die Kontrollen und die Abstimmung des Zugangs sollen weiterlaufen. Eine abschließende Verursacherfeststellung liegt nicht vor. Wenn für einen Anspruch oder die endgültige Kostenverteilung weitere Angaben entscheidend sind, formulieren Sie bitte die konkrete Nachfrage an die richtige Person. Ein Schreiben mit einem unbewiesenen Schuldvorwurf soll nicht entstehen.

Mit freundlichen Grüßen
Noura Selim'''),
]
assert len(docs4) == 32
CASES.append(dict(slug='weg-sonnenwinkel-bettwanzen',title='Sonnenwinkel und die ungeklärte Befallsquelle',plugin=PLUGIN,date='24.09.2026',client='Havel und Hof Hausverwaltung GmbH für die Gemeinschaft Sonnenwinkel 12',summary='Zwei benachbarte Wohnungen sind betroffen. Fachberichte, Zugangstermine und Rechnungen treffen auf vorschnelle Schuldzuweisungen und den Wunsch, sämtliche Kosten an Mieter weiterzureichen.',assignment='Maßnahmen und Termine koordinieren, Kosten und Verantwortlichkeiten anhand der Belege trennen und konkrete Eigentümer-, Vermieter- und Bewohnerkommunikation erstellen. Die offene Ursache darf nicht durch Vermutungen ersetzt werden.',documents=docs4,attachments={'07_Meldung_an_Verwaltung.eml':['05_Befund_Wohnung4.docx','06_Rechnung_Erstbesichtigung.docx'],'25_Erstattungsbitte_Mieter.eml':['24_Waschereibeleg.docx'],'32_Abschlussauftrag_Verwaltung.eml':['27_Kosten_und_Termine.xlsx','28_Angebot_Oktoberkontrolle.docx']}))
