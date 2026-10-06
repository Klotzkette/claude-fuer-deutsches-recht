#!/usr/bin/env python3
"""Additive Belege 58–71; historische Quellen 01–57 bleiben unverändert."""
from pathlib import Path
import importlib.util, hashlib, json
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('basis', ROOT/'scripts/build-bauwirtschaft-kaufmaennisch-akten.py')
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
C = b.BAD; CASE = ROOT/'testakten'/C
QA = Path('/tmp/bauwirtschaft-vertiefung-20261006/bad'); QA.mkdir(parents=True, exist_ok=True)
before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in CASE.iterdir() if p.is_file() and p.name[:2].isdigit() and int(p.name[:2]) <= 57}
b.register_fonts()
def doc(name,title,text,issuer=None,receiver=None,date='25. September 2026'):
    b.doc(C,name,issuer or b.B_OWNER,receiver or 'Nora Brinkmann | Kaufmännische Leitung',title,date,text)
def pdf(name,title,text,issuer,date='25. September 2026'):
    b.pdf(C,name,issuer,b.B_OWNER,title,date,text,keep_blocks=True)
def mail(name,sender,subject,text,attachment=None,date='2026-09-25T10:30:00'):
    b.mail(C,name,sender,'Nora Brinkmann <n.brinkmann@mertens-bau.de>',date,subject,text,attachment=attachment)

doc('58_Uebergabe_Detailnachweise.docx','Nachlieferung für den Freitagsabschluss','''1 Stand der Ablage

Nora, ich habe die Unterlagen zu unserem Besprechungstermin um 15:15 Uhr zusammengestellt. Die beiden Stapel betreffen weiterhin denselben Stand vom 25. September, 16:00 Uhr. In den nachgereichten Unterlagen sind keine weiteren Lieferantenrechnungen enthalten. Die ergänzten Aufmaße, Mietaufstellungen und Rückmeldungen gehören zu bereits erfassten Rechnungen. Bitte lege sie bei diesen Rechnungen ab; die Nummern 58 bis 75 sind Dokumentnummern unserer Ablage und keine neuen Buchungsnummern.

2 Rückmeldungen der Bauleitung

Lea hat die Flächen zu Trockenbau Vogt nach Bereichen aufgeteilt und den Rücklauf der Schalungsplatten erläutert. Jan hat die Planlieferung von Retzer durchgesehen. Er möchte zwei Punkte zur Eingangstreppe noch beantwortet haben. Seine Notiz enthält deshalb keine Zahlungsfreigabe. Die Retzer-Rechnung und die Rechnung des Büros Seidel betreffen verschiedene Leistungen. Bitte beide Vorgänge mit ihren eigenen Rechnungsnummern weiterführen.

Mietpark Rethmar hat die Anrechnung unserer Teilzahlung bestätigt. Das ist ein anderer Lieferant als Weser Miettechnik. Die zusätzliche Zahlung an Weser vom 24. September bleibt bei uns ungeklärt. Enno Weber hat noch keine abschließende Zuordnung geschickt. Auch eine Rücküberweisung ist nicht eingegangen. Die offenen Unterlagen zum Bauabzug bei Vogt und Ahle sind ebenfalls noch nicht vollständig.

3 Übergabe an die Buchhaltung

Bitte übernimm die neuen Angaben in die ergänzenden Excel-Mappen und notiere dort jeweils den Beleg. Die alten Mappen 24, 25 und 55 sollen als damaliger Arbeitsstand erhalten bleiben. Bei der Freigabe unterscheiden wir zwischen einem erfassten offenen Posten und einer Zahlung, die ich tatsächlich anweisen soll. Neue Bankumsätze nach dem Stichtag darfst du erst mit einem neuen Kontoauszug ergänzen.

Für den nächsten Lauf möchte ich eine kurze Liste der Unterlagen sehen, die noch fehlen, und eine Vorschau je Bankkonto. Die Projektkonto- und Betriebskontobestände sollen getrennt bleiben. Einen Umbuchungsauftrag zwischen beiden Konten habe ich nicht erteilt.

Tobias Mertens''',receiver='Nora Brinkmann | Besprechungsvorbereitung',date='25. September 2026, 15:00 Uhr')

pdf('60_Mietnachweis_Rethmar.pdf','Mietkarte MR 260907','''Mietpark Rethmar bestätigt den Mietverlauf zum Minibagger für den Werkstattanbau Fricke, Projekt BS26-01. Grundlage ist die Abholung am 1. September und die Rücknahme am 6. September 2026. Die sechs berechneten Kalendertage stimmen mit dem vereinbarten Zeitraum überein. Das Gerät wurde ohne Bedienpersonal überlassen. Fahrerleistungen unseres Hauses wurden weder bestellt noch ausgeführt.

Der Mietpreis beträgt 150,00 EUR netto je Kalendertag. Sechs Tage ergeben 900,00 EUR netto, zuzüglich 171,00 EUR Umsatzsteuer, insgesamt 1.071,00 EUR. Dieser Betrag ist bereits mit Rechnung MR-260907 vom 7. September berechnet. Die Mietkarte ist ein nachgereichter Leistungsnachweis und keine zweite Rechnung.

Bei der Rückgabe wurde das Gerät als betriebsbereit aufgenommen. Es wurden keine Schäden vermerkt. Eine zusätzliche Tank-, Reinigungs- oder Transportrechnung gehört nicht zu diesem Mietvorgang. Die Betriebsstundenzähler wurden bei der Rücknahme nicht gesondert in unserer Karte notiert. Der vereinbarte Tagespreis hängt hier nicht von einer stundenweisen Abrechnung ab.

Ihre Überweisung vom 18. September über 500,00 EUR wurde auf MR-260907 gebucht. Wir führen noch 571,00 EUR als Restforderung. Eine weitere Zahlung oder Gutschrift ist bis zum 25. September, 10:00 Uhr, auf diesem Kundenkonto nicht erfasst. Bitte geben Sie bei der Restzahlung diese Rechnungsnummer an. Wir haben keine Anweisung erhalten, Beträge anderer Mietunternehmen mit diesem Posten zu verrechnen.

Ruth Rethmar
Kundenkonto und Vermietung''','Mietpark Rethmar GmbH\nKundenkonto Bauunternehmen Mertens GmbH',date='25. September 2026, 10:00 Uhr')
mail('59_Rethmar_Restforderung.eml','Ruth Rethmar <buchhaltung@mietpark-rethmar.de>','MR-260907 / Restbetrag und nachgereichte Mietkarte','''Guten Tag Frau Brinkmann,

anbei die Mietkarte, die Sie für Ihren Abschluss angefordert haben. Unsere Rechnung über 1.071,00 EUR steht nach Ihrer Teilzahlung über 500,00 EUR noch mit 571,00 EUR offen. Der Zahlungseingang wurde am 18. September zugeordnet. Bitte prüfen Sie den Restbetrag für Ihren nächsten Lauf.

Die in Ihrem Telefonat genannten 1.785,00 EUR können wir auf unserem Kundenkonto nicht finden. Sie sagten anschließend, auf dem Bankbeleg stehe Weser Miettechnik. Wir sind Mietpark Rethmar; zwischen den beiden Kundenkonten besteht keine gemeinsame Verrechnung. Bitte setzen Sie sich wegen dieser Zahlung mit dem dortigen Empfänger in Verbindung.

Am Minibagger gab es keine zusätzlichen Schäden und keine Nachberechnung. Falls Ihnen unsere Rechnung noch einmal als Scan zugeschickt wurde, handelt es sich um denselben Vorgang MR-260907. Schicken Sie mir bitte eine kurze Rückmeldung, sobald der Restbetrag angewiesen wurde. Eine bloße Vormerkung für den nächsten Lauf buchen wir noch nicht als Zahlungseingang.

Freundliche Grüße
Ruth Rethmar''',attachment='60_Mietnachweis_Rethmar.pdf',date='2026-09-25T10:18:00')

doc('61_Planpruefung_Eingangstreppe.docx','Planprüfung der Eingangstreppe in Lage','''1 Unterlagen und Besprechung

Ich habe die von Retzer am 10. September übermittelten Planstände für die Eingangstreppe der Ladenfläche Lage durchgesehen. Auf der Planliste stehen Grundriss, Schnitt und Anschlussdetail. Die Rechnung TP-260910 nennt hierfür 15 Stunden Ausführungsplanung zu 80,00 EUR. Die Unterlagen liegen im Projektordner; meine Prüfung heute bezog sich auf die Maße am Türanschluss und den Übergang zum Belag.

2 Rückfragen an Retzer

Die lichte Durchgangsbreite ist im Grundriss eingetragen. Im Anschlussdetail fehlt mir die nachvollziehbare Zuordnung zum von uns gemessenen Bestandsmaß. Außerdem möchte ich wissen, ob die eingezeichnete Öffnungsrichtung der Tür mit dem letzten Aufmaß abgeglichen wurde. Ich habe Retzer um eine kurze Gegenüberstellung der beiden Maße und eine Erläuterung der Türdarstellung gebeten. Solange die Rückmeldung fehlt, kann ich die Planlieferung inhaltlich nicht abschließend bestätigen.

Der Planer hat heute erklärt, die 15 Stunden umfassten Bestandsabgleich, Zeichnung und Abstimmung. Diese Erklärung habe ich zur Rechnung genommen. Einen Beleg für zusätzliche Stunden oder einen Nachtrag hat er damit nicht eingereicht. Eine örtliche Ausführung der Treppe durch Retzer hat es nicht gegeben.

3 Buchhaltung und weitere Bearbeitung

Nora soll die Rechnung im offenen Postenbestand belassen. Mein Hinweis, dass die Unterlagen angekommen sind, ist keine sachliche Zahlungsfreigabe. Über einen Einbehalt oder eine Minderung haben wir mit Retzer bisher nichts vereinbart. Ich werde den Inhalt nach Eingang der Maßgegenüberstellung erneut prüfen und die Freigabe oder weitere Rückfrage schriftlich an die Buchhaltung schicken.

Die frühere Anfrage zur Tragwerksplanung Seidel bleibt ein eigener Vorgang mit der Rechnung ST-260922. Eine Rückmeldung zur Eingangstreppe erledigt diese andere Prüfung nicht mit. Bitte in der Mappe die vollständige Rechnungsnummer verwenden, damit die ähnlich aussehenden Kürzel nicht vertauscht werden.

Jan Hellwig
Bauleitung BS26-02''',issuer='Bauunternehmen Mertens GmbH\nJan Hellwig | Projekt BS26-02',date='25. September 2026, 12:05 Uhr')
mail('62_Retzer_Leistungsaufteilung.eml','Emil Retzer <planung@retzer-planung.de>','TP-260910 / Erläuterung der 15 Stunden','''Guten Tag Frau Brinkmann,

Herr Hellwig hat mich gebeten, den Ansatz auf unserer Rechnung zu erläutern. Die 15 Stunden setzen sich aus vier Stunden Bestandsabgleich am 7. September, acht Stunden Zeichnungsbearbeitung am 8. und 9. September und drei Stunden Zusammenstellung und Abstimmung am 10. September zusammen. Der vereinbarte Satz beträgt 80,00 EUR netto. Die Rechnung bleibt deshalb bei 1.200,00 EUR netto und 1.428,00 EUR einschließlich Umsatzsteuer.

Die Frage zum Türanschluss ist bei uns eingegangen. Ich gleiche das Bestandsmaß am Montag mit der ursprünglichen Aufmaßnotiz ab und melde mich bei Herrn Hellwig. Heute kann ich nicht bestätigen, ob eine Berichtigung der Zeichnung erforderlich wird. Mit der Erläuterung der Stunden beantragen wir keinen zusätzlichen Auftrag. Wir haben an der Treppe selbst keine Bauleistung ausgeführt.

Bitte lassen Sie uns wissen, welcher Punkt einer Freigabe noch entgegensteht. Dass die Rechnung bereits im System erfasst ist, verstehe ich nach Ihrem Hinweis nicht als Zahlungszusage. Wir führen sie weiterhin offen und haben weder eine Teilzahlung noch eine Verrechnung erhalten.

Freundliche Grüße
Emil Retzer
Planungsbüro Retzer GmbH''',date='2026-09-25T11:42:00')

pdf('63_Aufmass_Trockenbau_Vogt.pdf','Flächenherleitung zu TB 260905','''Am 25. September haben Lea Tönnies und Otto Vogt die Abrechnung der Trockenbauflächen für den Werkstattanbau Fricke anhand der Aufmaßblätter zusammengeführt. Die Leistungen waren bis zum 5. September ausgeführt. Es geht um die bereits berechneten 120,00 m²; zusätzliche Flächen werden mit diesem Blatt nicht angemeldet.

Der erste Bereich an der Werkstattseite misst 12,00 m in der Länge und 3,00 m in der Höhe. Er ergibt 36,00 m². Der zweite Bereich besteht aus einer durchgehenden Fläche von 11,00 m mal 4,00 m und ergibt 44,00 m². Der dritte Bereich misst 10,00 m mal 4,00 m und ergibt 40,00 m². In diesen drei Teilflächen sind keine Öffnungen enthalten. Sie liegen außerhalb der separat gemessenen Türfelder; Türflächen werden hier nicht mitgerechnet.

Die Summe beträgt 120,00 m². Mit dem vereinbarten Einheitspreis von 40,00 EUR netto ergibt sich der Rechnungsbetrag von 4.800,00 EUR netto aus TB-260905. Die Rechnung weist keine vom Lieferanten berechnete Umsatzsteuer aus. Die Flächenbestätigung ersetzt keine steuerliche Prüfung und enthält keine Aussage zum Bauabzug.

Lea Tönnies bestätigt die Mengen anhand der örtlichen Aufnahme. Sie erklärt damit weder eine rechtsgeschäftliche Abnahme des gesamten Gewerks noch die Anweisung einer Zahlung. Ein Sicherheitseinbehalt oder ein Skonto wurde für diese Rechnung nicht vereinbart. Ob und wie die Buchhaltung den Betrag anweist, wird gesondert durch die kaufmännische Leitung und die Geschäftsführung entschieden.

Aufgestellt Otto Vogt
Mengenabgleich Lea Tönnies''','Trockenbau Vogt GmbH\nProjekt BS26-01 | Rechnungsbezug TB-260905')
pdf('64_Stundennachweis_Sanitaer_Ahle.pdf','Stundenherleitung zu SA 260906','''Für den Umbau der Ladenfläche Lage wurden vom 1. bis 6. September 2026 insgesamt 40 Monteurstunden erfasst. Am 1. September entfielen acht Stunden auf das Einrichten und Ausmessen der Leitungsführung. Am 2. September wurden acht Stunden für die Befestigungen und die Vorbereitung der Anschlüsse verwendet. Die Leitungsinstallation am 3. und 4. September beanspruchte jeweils acht Stunden. Am 6. September wurden in acht Stunden die Anschlüsse fertiggestellt und die bearbeiteten Bereiche aufgeräumt. Am 5. September ist in diesem Vorgang kein Einsatz erfasst.

Die Stundenangaben sind Personenstunden eines Monteurs. Sie dürfen nicht noch einmal mit einer Kolonnenstärke multipliziert werden. Die beschriebenen Arbeiten gehören zur Leistungszeile der Rechnung SA-260906. Der vereinbarte Satz beträgt 80,00 EUR netto je Stunde; 40 Stunden ergeben damit 3.200,00 EUR netto. Material oder zusätzliche Anfahrtspauschalen werden mit diesem Nachweis nicht nachberechnet.

Jan Hellwig hat die Anwesenheit anhand der Baustelleneinträge abgeglichen. Der Nachweis belegt den abgerechneten Einsatz, enthält aber keine abschließende Funktionsprüfung des gesamten Sanitärsystems und keine Abnahmeerklärung. Für die Zahlungsbearbeitung hat die Buchhaltung noch die angeforderten steuerlichen Unterlagen zu prüfen. Ein Nachweis hierzu ist diesem Stundenblatt nicht beigefügt.

Bitte ordnen Sie dieses Blatt ausschließlich SA-260906 zu. Der Betrag ist bereits im ergänzenden Rechnungseingang erfasst. Die Übersendung soll die Mengenherleitung erläutern und keinen zweiten offenen Posten erzeugen. Eine Zahlung haben wir bis zum heutigen Vormittag auf dieser Rechnung nicht verbucht.

Hermann Ahle
Ausführung und Abrechnung''','Sanitär Ahle GmbH\nProjekt BS26-02 | Rechnungsbezug SA-260906')
mail('65_Vogt_Bescheinigung_angefordert.eml','Otto Vogt <abrechnung@trockenbau-vogt.de>','TB-260905 / Unterlagen für den Zahlungslauf','''Guten Tag Frau Brinkmann,

das ergänzte Flächenblatt haben wir heute mit Frau Tönnies besprochen. Die 120 m² und der Satz von 40,00 EUR bleiben unverändert. Ihre Bitte um eine für den Zahlungszeitpunkt gültige Freistellungsbescheinigung habe ich an unser Büro weitergegeben. Ich habe hier auf der Baustelle nur einen älteren Scan und möchte den nicht als aktuellen Nachweis verschicken. Das Büro prüft die Gültigkeit und den Umfang.

Sie fragten außerdem nach sämtlichen Leistungen an Ihr Unternehmen in diesem Kalenderjahr. Ich kann das aus meiner Baustellenliste nicht vollständig beantworten. Dort steht Fricke; kleinere Einsätze anderer Kolonnen sind in unserer zentralen Abrechnung erfasst. Eine Aussage, dass dies unser einziger Auftrag bei Mertens im Jahr 2026 sei, kann ich heute nicht abgeben.

Bitte lassen Sie die Frage bis zur Rückmeldung offen. Wir beantragen mit dieser Nachricht weder eine zusätzliche Vergütung noch einen anderen Rechnungstext. Einen Zahlungsabzug haben wir bislang nicht miteinander abgerechnet. Ich melde mich am Montag wegen der Bescheinigung.

Freundliche Grüße
Otto Vogt''',date='2026-09-25T13:12:00')
mail('66_Ahle_Jahresumfang_offen.eml','Hermann Ahle <buero@sanitaer-ahle.de>','SA-260906 / Rückfrage zum Jahresumfang','''Guten Tag Frau Brinkmann,

den Stundenbeleg zu Lage haben Sie jetzt. Zu Ihrer weiteren Frage nach dem Jahresumfang: Herr Mertens hat mit mir am Telefon über einen möglichen kleinen Sanitärumbau an einem anderen Objekt gesprochen. Eine Bestellung liegt mir dazu nicht vor. Mengen und Ausführungstermin wurden noch nicht festgelegt; aus dem Gespräch kann ich keinen verlässlichen Auftragswert ableiten.

Unsere Buchhalterin gleicht am Montag die im Jahr 2026 bereits ausgeführten Leistungen an Mertens mit den angenommenen Bestellungen ab. Erst danach können wir Ihre Rückfrage vollständig beantworten. Bitte behandeln Sie den möglichen Folgeauftrag bis dahin weder als bestätigte Bestellung noch als sicher entfallenen Auftrag. Ob unsere Freistellungsbescheinigung den maßgeblichen Zeitpunkt und diesen Vorgang abdeckt, muss sie ebenfalls anhand des Originals prüfen.

Für SA-260906 gilt weiterhin der Rechnungsbetrag von 3.200,00 EUR. Wir haben keinen Skontoabzug und keinen vertraglichen Sicherheitseinbehalt vereinbart. Die nachgereichte Stundenaufteilung ist keine neue Rechnung. Bitte senden Sie mir Ihre konkrete Unterlagenanforderung gesammelt zu, damit unser Büro den Vorgang am Montag vollständig bearbeiten kann.

Viele Grüße
Hermann Ahle''',date='2026-09-25T13:38:00')

pdf('67_Ruecklieferbeleg_Holzhandel.pdf','Rücklieferung und Rechnungskorrektur','''Zum Liefervorgang HB-260903 wurden am 15. September Schalungsplatten aus dem Projekt BS26-01 zurückgenommen. Die Rücknahme betrifft einen vereinbarten Warenwert von 200,00 EUR netto. Die mengenmäßige Bewertung der Rückgabe wurde mit dem Kunden pauschal auf diesen Betrag festgelegt; die Rückgabe wird deshalb nicht durch eine nachträgliche Änderung des ursprünglichen Einheitspreises abgebildet.

Wir haben den Vorgang am 16. September mit HB-G260916 abgerechnet. Zu 200,00 EUR netto kommen 38,00 EUR Umsatzsteuer; die Rechnungskorrektur beträgt insgesamt 238,00 EUR zugunsten des Kunden. Diese Korrektur gehört zur Rechnung HB-260903 über 2.856,00 EUR. Der verbleibende Zahlungsbetrag beträgt 2.618,00 EUR. Dieser Betrag wurde mit Ihrer Zahlung vom 17. September ausgeglichen.

Die jetzt übersandte Bestätigung ist ein Nachweis zur bereits ausgestellten Rechnungskorrektur. Sie stellt keine weitere Gutschrift aus und begründet keinen zusätzlichen Erstattungsanspruch. Bitte erfassen Sie weder den Nettowert von 200,00 EUR noch den Bruttobetrag von 238,00 EUR ein zweites Mal im Kreditorenkonto.

Nach der Verrechnung der Korrektur und Ihrer Zahlung führen wir den Vorgang HB-260903 ausgeglichen. Weitere Rücklieferungen aus diesem Vorgang sind bis zum 25. September, 11:00 Uhr, bei uns nicht erfasst. Falls Ihre Baustellenablage andere Mengen enthält, bitten wir vor einer weiteren Buchung um die betreffende Rücknahmenummer.

Lieselotte Bega
Warenrücknahme und Abrechnung''','Holzhandel Bega GmbH\nKundenkonto Mertens | HB-260903 und HB-G260916')
pdf('68_Steinwerk_Sammelzahlung.pdf','Zuordnung der Sammelzahlung','''Wir bestätigen die Zuordnung Ihrer Zahlung über 2.856,00 EUR vom 16. September 2026. Im Verwendungszweck sind die beiden Rechnungen ST-260902 und ST-260911 angegeben. Unsere Debitorenbuchhaltung hat hiervon 2.142,00 EUR auf ST-260902 und 714,00 EUR auf ST-260911 gebucht. Die Teilbeträge ergeben zusammen genau den eingegangenen Betrag.

ST-260902 betrifft die Lieferung von 600 Kalksandsteinen zu 3,00 EUR netto, zusammen 1.800,00 EUR netto und 342,00 EUR Umsatzsteuer. ST-260911 betrifft 30 Sack Mörtel zu 20,00 EUR netto, zusammen 600,00 EUR netto und 114,00 EUR Umsatzsteuer. Beide Lieferungen gehören nach Ihren Bestellangaben zum Werkstattanbau Fricke, Projekt BS26-01.

Mit der Zuordnung sind beide Rechnungen ausgeglichen. Ein Skonto wurde nicht abgezogen. Eine weitere Rechnung in Höhe des Sammelzahlungsbetrags haben wir nicht ausgestellt. Ihr Bankdatensatz EB-0916A bleibt deshalb ein Zahlungsvorgang, zu dem in der Rechnungszuordnung zwei Zeilen gehören. Bitte vervielfachen Sie nicht den Bankabgang, wenn Sie die Belege einzeln prüfen.

Das Kürzel ST verwenden wir für Steinwerk. Eine Tragwerksplanungsrechnung eines anderen Lieferanten ist kein Bestandteil unseres Kundenkontos. Für Nachfragen benötigen wir deshalb neben der Rechnungsnummer auch den Lieferantennamen. Bis zum 25. September, 11:20 Uhr, liegt uns keine Rücklastschrift zu Ihrer Überweisung vor.

Friedhelm Stein
Debitorenbuchhaltung''','Steinwerk Leopoldshöhe GmbH\nKundenkonto Bauunternehmen Mertens GmbH')

doc('69_Arbeitsanweisung_Excel_Fortfuehrung.docx','Arbeitsanweisung für die ergänzenden Mappen','''1 Ablage und Eingaben

Die Mappen 72 bis 75 führen die vorhandenen Belege für unseren Freitagsabschluss zusammen. Bitte vor Änderungen eine eigene Arbeitskopie speichern. Blau gesetzte Zahlen und Eingabefelder stammen aus Belegen oder sind von uns zu pflegen. Schwarz gesetzte Beträge werden gerechnet; grüne Formeln übernehmen Werte aus einem anderen Blatt derselben Mappe. Die Kopfzeile jedes Blatts nennt Einheit und Stichtag. Eine leere Freigabe bedeutet, dass die Entscheidung noch aussteht.

2 Rechnungen und Zahlungen

In Mappe 72 stehen die Rechnungsbeträge, die bereits erfassten Korrekturen und die zugeordneten Zahlungen nebeneinander. Die Belegwege sind gesondert erklärt. Der Sicherheitseinbehalt zu Röding bleibt ein Teil der offenen Verbindlichkeit. Die zusätzliche Weser-Zahlung über 1.785,00 EUR hat keine belastbare Rechnungszuordnung und wird dort nicht gegen eine andere Mietrechnung verrechnet.

Die Stundenmappe 73 zeigt den Übergang von den Auguststunden zu Bruttolohn und Arbeitgeberbelastung. Ihre Summe ist ein Kostenwert. Für den Geldabfluss sind daneben die drei Bankzahlungen zu betrachten. Der Arbeitgeberanteil darf nicht ein zweites Mal zu der bereits vollständigen Auszahlungssumme addiert werden.

3 Miete und Zahlungsplanung

Mappe 74 trennt die Mietrechnungen nach Lieferant und Bankkonto. Die Vorgangsnummer führt zum Mietnachweis. Der ähnliche Begriff Mietpark im Banktext ist kein Beweis, dass eine Zahlung zu Rethmar gehört.

In Mappe 75 sind fünf Zeilen für einen späteren Zahlungsvorschlag vorbereitet. Die Freigabefelder stehen zunächst auf offen. Ein Betrag an den Lieferanten und eine etwaige gesonderte Steuerzahlung werden erst nach Prüfung eingetragen. Ist kein gesonderter Abfluss erforderlich, ist ausdrücklich 0 einzutragen. Die Formel soll unvollständige Angaben sichtbar lassen. Eine Tabellenzeile führt keinen Bankauftrag aus.

4 Weitere Bearbeitung

Bitte zu jeder Freigabe Namen, Zeitpunkt und Beleg im Kommentarbereich ergänzen. Bei neuen Bankumsätzen ist zuerst die Quelle zu sichern. Das Blatt mit den Bankbeständen ist eine Vorschau auf Basis der beiden Kontoauszüge, kein aktueller Abruf aus dem Bankportal. Die ursprünglichen Dateien 24, 25 und 55 werden nicht überschrieben.

Nora Brinkmann''',issuer='Nora Brinkmann\nKaufmännische Leitung | Bauunternehmen Mertens GmbH',receiver='Buchhaltung und Vertretung',date='25. September 2026, 15:40 Uhr')
doc('70_Zahlungsbesprechung_Freitag.docx','Besprechung zum nächsten Zahlungslauf','''1 Teilnehmer und Ausgangsstand

Tobias Mertens und Nora Brinkmann haben am 25. September von 15:15 bis 15:35 Uhr den offenen Postenbestand besprochen. Jan Hellwig war für die Rückfragen zu Lage telefonisch zugeschaltet. Grundlage waren die beiden Kontoauszüge bis zum heutigen Stichtag und die nachgereichten Leistungsnachweise. Während der Besprechung wurde kein Bankauftrag angelegt oder freigegeben.

2 Besprochene Rechnungen

Rethmar führt nach der Teilzahlung noch 571,00 EUR offen. Nora soll den Belegweg für den nächsten Lauf zusammenstellen. Tobias möchte die endgültige Liste am Montag vor Ausführung noch einmal sehen. Eine Vorabfreigabe für einen Bankauftrag hat er heute nicht erteilt. Die offene Weser-Zuordnung über 1.785,00 EUR bleibt bei Enno Weber in Klärung. Sie soll nicht mit Rethmar saldiert werden.

Zu Retzer wartet Jan auf die Erläuterung zum Bestandsmaß und zur Türdarstellung. Zur Tragwerksplanung Seidel steht seine gesonderte Rückmeldung weiter aus. Nora soll die beiden offenen Rechnungen weiterführen und die Freigabe jeweils gesondert dokumentieren. Der Eingang der Rechnung allein genügt Tobias für die Anweisung nicht.

3 Unterlagen zum Bauabzug

Bei Vogt und Ahle sind die Bescheinigungen und der Jahresumfang noch zu klären. Die Nachweise zur ausgeführten Leistung liegen nun detaillierter vor. Tobias bittet Nora, die steuerliche Behandlung vor einer Auszahlung mit dem betreuenden Steuerbüro abzustimmen. Ein bestimmter Abzugsbetrag wurde in dieser Besprechung nicht festgelegt. Die steuerlichen Rückfragen sind unabhängig davon zu bearbeiten, dass die Rechnungen keine vom Lieferanten berechnete Umsatzsteuer enthalten.

4 Konten und Abschluss

Der Betriebskontoauszug endet mit 79.211,80 EUR, der Projektkontoauszug mit 38.218,80 EUR. Es wurde keine Umbuchung zwischen den Konten beschlossen. Eine Liquiditätsvorschau soll beide Konten getrennt fortführen. Tobias entscheidet über die nächste Liste nach Sichtung der ergänzten Freigaben. Nora hält die ursprünglichen offenen Posten und die später tatsächlich ausgeführten Zahlungen getrennt fest.

Aufgezeichnet Nora Brinkmann''',receiver='Tobias Mertens | Geschäftsführung',date='25. September 2026, 15:35 Uhr')
doc('71_Lohnstunden_Kostenverteilung.docx','Auguststunden und Zahlungen im September','''1 Herkunft der Stunden

Die übergebenen 700 Stunden betreffen den Abrechnungsmonat August 2026. Für die Personalnummern P001 bis P010 wurden jeweils 70 Stunden zu 30,00 EUR erfasst. Die Personen P001 bis P006 sind im übergebenen Stundenbestand vollständig BS26-01 zugeordnet; P007 bis P010 sind BS26-02 zugeordnet. Eine Änderung dieser Verteilung ist in den nachgereichten Unterlagen nicht enthalten.

2 Kostenansatz

Je Person ergeben sich 2.100,00 EUR Bruttolohn und 440,00 EUR Arbeitgeberbelastung. Die Bruttolohnsumme beträgt damit 21.000,00 EUR, die Arbeitgeberbelastung 4.400,00 EUR. Für diese Abrechnung beträgt der gesamte Personalaufwand 25.400,00 EUR. Die Aufteilung nach Projekt folgt den übergebenen Stunden und ordnet auch die jeweilige Arbeitgeberbelastung dem zugehörigen Projekt zu. Es handelt sich um die vorliegende Lohnzusammenfassung, nicht um eine Neuberechnung individueller Abgaben.

3 Zahlungsnachweise

Auf dem Betriebskonto sind im September 15.700,00 EUR Nettolohn, 7.700,00 EUR Sozialversicherung und 2.000,00 EUR Lohnsteuer ausgeführt worden. Die Sozialversicherungszahlung enthält 3.300,00 EUR Arbeitnehmeranteile und 4.400,00 EUR Arbeitgeberanteile. Die drei Zahlungen ergeben zusammen 25.400,00 EUR. Die Arbeitgeberanteile sind darin bereits enthalten.

Der zeitliche Unterschied ist für die Abstimmung festzuhalten: Die Arbeitsleistung gehört in den August, die bezeichneten Geldabflüsse liegen im September. Aus dem Zahlungsdatum folgt kein zweiter Septemberlohnaufwand. Die Personalnummern dienen der Zuordnung im übergebenen Stundenbestand; Namen und individuelle Lohnsteuermerkmale werden hierfür nicht benötigt.

Bitte richten Sie Rückfragen zu den Summen an unser Büro und ändern Sie die Abrechnung nicht anhand einer bloßen Differenz in einer Projektliste. Bei einer späteren Korrektur würden wir eine gekennzeichnete neue Abrechnung übergeben.

Sabine Krüger
Lohnbüro''',issuer='Sabine Krüger | Lohnbüro',receiver='Nora Brinkmann\nBauunternehmen Mertens GmbH',date='25. September 2026, 14:20 Uhr')

after = {n: hashlib.sha256((CASE/n).read_bytes()).hexdigest() for n in before}
assert before == after, 'Historische Originale verändert'
(QA/'source-preservation.json').write_text(json.dumps({'count':len(before),'unchanged':True,'hashes':before},ensure_ascii=False,indent=2))
print('14 ergänzende Belege erstellt; 57 historische Originale unverändert.')
