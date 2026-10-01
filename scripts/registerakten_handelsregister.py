"""Drei fiktive Handelsregister-Arbeitsakten; Daten für gemeinsamen Renderer."""

def D(file,title,body,date='01.10.2026',**kw):
    return dict(file=file,title=title,body=body,date=date,**kw)

def E(file,title,body,date,sender,recipient):
    return D(file,title,body,date,**{'from':sender,'to':recipient,'subject':title})

CASES=[]
CASES.append({
 'slug':'handelsregister-assistent-kiezkolben-colombo','plugin':'handelsregister-assistent',
 'title':'Kiezkolben und die Gesellschafterin aus Colombo',
 'subtitle':'Vierzig Prozent, zwei Direktoren und ein Paket, das immer noch wächst',
 'date':'01.10.2026','client':'Kiezkolben Maschinenverleih GmbH',
 'summary':'Kunigunde Knatter möchte einen Teil ihrer Anteile an eine Gesellschaft aus Colombo übertragen. Der Kaufpreis ist eingegangen, aber beim Notariat und beim Registergericht bestehen Fragen zur Vertretung der Erwerberin. Zwischen alten Registerformularen, einem Rücktritt und einer nachgereichten Board-Erklärung stehen inzwischen vier verschiedene Datumsfolgen.',
 'assignment':'Lesen Sie die Unterlagen, ordnen Sie den Stand der Gesellschafterliste und der Vertretungsnachweise und fertigen Sie die jetzt benötigten Schreiben an Notariat und Registergericht. Klären Sie gezielt die noch entscheidenden Lücken; veranlassen Sie keine externe Übermittlung.',
 'documents':[
 E('01_Kunigunde_bitte_nicht_noch_eine_Runde.eml','Colombo-Sache: bitte einmal zu Ende bringen',
 '''Sehr geehrte Frau Rechtsanwältin Öztürk,

ich sende Ihnen den Ordner, den Herr Holzapfel vom Notariat zusammengestellt hat. Wir vermieten kleine Maschinen an Werkstätten und Bühnenbauer. Ceylon Cloud will unser Buchungssystem mitentwickeln und hat mir vier von meinen sechs Anteilen abgekauft. Das Geld ist seit dem 16. September da. Otto sagt inzwischen, Nirmala habe gar nicht allein unterschreiben dürfen. Vorher hat er die Zusammenarbeit selbst vorgeschlagen.

Ich möchte keine Entscheidung über einen Gesellschafterprozess, sondern erst einmal wissen, was wir dem Gericht und dem Notar jetzt schicken müssen. Die Frist soll der 12. Oktober sein. Bitte prüfen Sie auch, ob unsere neue Liste überhaupt schon aufgenommen wurde. Im Ordner heißt eine Datei „final“, aber ich sehe im Register noch meine alten sechzig Prozent.

Matthias aus Colombo ist nett, schreibt aber auf jede zweite Frage „certificate attached“. Wenn Sie genaue Fragen formulieren, leite ich die gern weiter. Bitte noch nichts direkt absenden; ich möchte die Schreiben vorher sehen.

Mit freundlichen Grüßen
Kunigunde Knatter
Geschäftsführerin, Kiezkolben Maschinenverleih GmbH''','2026-10-01T08:12:00+02:00','Kunigunde Knatter <kunigunde@kiezkolben.example>','Derya Öztürk <derya@kanzlei-spreebogen.example>'),
 D('02_Registerstand_30September_Arbeitskopie.pdf','Arbeitsabschrift des Registerauszugs',
 '''Amtsgericht Charlottenburg – HRB 248765 B
Abrufvermerk der Sachbearbeitung: 30.09.2026, 17:42 Uhr. Abschrift der für die Akte übernommenen Daten; ohne amtliche Beglaubigung.

Firma: Kiezkolben Maschinenverleih GmbH. Sitz: Berlin. Geschäftsanschrift: Zangenhof 14, 10997 Berlin. Stammkapital: 25.000 EUR. Gegenstand: Vermietung, Wartung und Handel mit transportablen Maschinen, Werkzeugen und Zubehör für Handwerk, Veranstaltungen und Werkstätten, soweit hierfür keine besondere Erlaubnis erforderlich ist.

Allgemeine Vertretungsregel: Ist nur ein Geschäftsführer bestellt, vertritt er allein. Sind mehrere Geschäftsführer bestellt, wird die Gesellschaft durch zwei Geschäftsführer gemeinsam oder durch einen Geschäftsführer gemeinsam mit einem Prokuristen vertreten. Einzelvertretungsbefugnis kann erteilt werden.

Geschäftsführerin: Kunigunde Knatter, geboren am 14.02.1979, Berlin; einzelvertretungsberechtigt, mit der Befugnis, Rechtsgeschäfte mit sich selbst oder als Vertreter eines Dritten abzuschließen.

Letzte Eintragung im Registerblatt: 11.05.2024. In der geöffneten Dokumentliste wurde eine Gesellschafterliste vom 09.05.2024 angezeigt. Ein weiterer Datensatz war in der Arbeitsansicht als eingegangen am 18.09.2026 vermerkt; ein herunterladbares neues Listendokument erschien beim Abruf nicht. Der Browser wurde nach einem erneuten Ladeversuch geschlossen.''','30.09.2026'),
 {'file':'03_Anteile_alt_neu.xlsx','title':'Anteilübersicht aus der Geschäftsführung','date':'17.09.2026','sheets':[{'name':'Liste_2024','headers':['Anteil','Inhaberin oder Inhaber','Nennbetrag EUR','Kapitalquote'],'rows':[[i,'Kunigunde Knatter' if i<=6 else 'Otto Pumpernickel',2500,f'=C{i+1}/25000']for i in range(1,11)],'formats':{'C':'#,##0.00','D':'0.00%'}},{'name':'Plan_nach_Kauf','headers':['Anteil','Vorgesehene Inhaberin','Nennbetrag EUR','Kapitalquote','Notiz'],'rows':[[i,('Kunigunde Knatter' if i<=2 else 'Ceylon Cloud (Private) Limited' if i<=6 else 'Otto Pumpernickel'),2500,f'=C{i+1}/25000','Kaufpreis laut Bank eingegangen' if 3<=i<=6 else 'unverändert']for i in range(1,11)],'formats':{'C':'#,##0.00','D':'0.00%'}},{'name':'Kaufpreis','headers':['Position','Betrag EUR'],'rows':[['Anteile 3 bis 6',80000],['Bankeingang 16.09.2026',80000],['Differenz','=B2-B3']]}]},
 D('04_Satzung_Kiezkolben_Auszug.docx','Gesellschaftsvertrag – Arbeitsabschrift der maßgeblichen Bestimmungen',
 '''1. Firma und Sitz

Die Gesellschaft führt die Firma Kiezkolben Maschinenverleih GmbH. Ihr Sitz ist Berlin.

2. Stammkapital und Geschäftsanteile

Das Stammkapital beträgt 25.000 EUR. Es ist in zehn Geschäftsanteile mit den laufenden Nummern 1 bis 10 im Nennbetrag von jeweils 2.500 EUR eingeteilt. Jede volle Einheit von einem Euro eines Geschäftsanteils gewährt eine Stimme.

3. Verfügung über Geschäftsanteile

Die Abtretung eines Geschäftsanteils oder eines Teils davon bedarf der Zustimmung der Gesellschafterversammlung. Der Beschluss wird mit mindestens 75 Prozent der abgegebenen Stimmen gefasst. Der veräußernde Gesellschafter ist bei diesem Beschluss stimmberechtigt. Die Zustimmung kann vor Abschluss des Abtretungsvertrags erteilt werden und ist schriftlich zu dokumentieren.

4. Beschlussfassung

Beschlüsse können außerhalb einer Versammlung in Textform gefasst werden, wenn sämtliche Gesellschafter mit dieser Form der Beschlussfassung einverstanden sind. Die Geschäftsführung übersendet den vollständigen Beschlussantrag und setzt eine angemessene Antwortfrist. Nicht abgegebene Stimmen gelten nicht als Zustimmung.

5. Geschäftsführung

Die Gesellschafterversammlung bestellt und beruft Geschäftsführer ab. Bei mehreren Geschäftsführern wird die Gesellschaft durch zwei Geschäftsführer gemeinsam oder durch einen Geschäftsführer gemeinsam mit einem Prokuristen vertreten. Einzelvertretung und Befreiung von den Beschränkungen des § 181 BGB können durch Gesellschafterbeschluss erteilt werden.

Übernommen aus dem vollständigen Satzungstext vom 09.05.2024. Die übrigen Bestimmungen betreffen Geschäftsjahr, Gewinnverwendung, Einziehung und Bekanntmachungen. Die vollständige Datei liegt nach Auskunft der Buchhaltung im Notariatsarchiv.''','09.05.2024'),
 E('05_Otto_Zustimmung.eml','Beschlussantrag Ceylon Cloud',
 '''Hallo Kunigunde,

mit der Abstimmung per E-Mail bin ich einverstanden. Ich stimme dem Antrag vom 2. September zu: Du darfst die Geschäftsanteile 3 bis 6 an Ceylon Cloud (Private) Limited in Colombo verkaufen und abtreten. Die Zustimmung gilt für den Vertrag, den Frau Doktor Zingel am 4. September herumgeschickt hat, mit 80.000 EUR Kaufpreis und ohne Verpflichtungen der Kiezkolben gegenüber der Käuferin.

Bitte lass uns das Entwicklungsbudget danach gesondert besprechen. Ich will nicht, dass aus dem Anteilskauf automatisch ein Auftrag über 200.000 EUR wird. Nirmala hatte im Gespräch gesagt, ihr Board sei einverstanden. Die Unterlagen dazu habe ich nicht gesehen.

Grüße
Otto''','2026-09-05T09:17:00+02:00','Otto Pumpernickel <otto@kiezkolben.example>','Kunigunde Knatter <kunigunde@kiezkolben.example>'),
 D('06_Anteilskauf_Arbeitsabschrift.docx','Anteilskauf und Abtretung – Arbeitsabschrift',
 '''Urkundenbezug der Beteiligten: Nummer 318/2026 der Notarin Dr. Ottilie Zingel, Berlin; Termin vom 15.09.2026. Diese für die Mandatsbearbeitung übertragene Arbeitsabschrift enthält keine Siegel oder Unterschriftsabbildungen.

1. Beteiligte und Vertretungsangaben

Kunigunde Knatter, geboren am 14.02.1979, wohnhaft in Berlin, handelt im eigenen Namen. Nirmala Jayawardena, geboren am 28.07.1984, wohnhaft in Colombo, erklärt, als Direktorin für Ceylon Cloud (Private) Limited mit Sitz in Colombo, Registrierungsnummer PV 00289176, zu handeln. Ein aktueller Nachweis der Einzelvertretungsbefugnis liegt im Termin nicht vor. Die Erwerberin soll ergänzende Nachweise beibringen. Eine persönliche Zahlungspflicht der erschienenen Nirmala Jayawardena wird dadurch nicht vereinbart.

2. Kaufgegenstand

Die Verkäuferin verkauft die Geschäftsanteile mit den Nummern 3, 4, 5 und 6 im Nennbetrag von jeweils 2.500 EUR an der Kiezkolben Maschinenverleih GmbH, Amtsgericht Charlottenburg, HRB 248765 B, an die Erwerberin. Der Gesamtnennbetrag beträgt 10.000 EUR. Die Verkäuferin erklärt, dass diese Anteile nach ihrer Kenntnis nicht verpfändet oder mit Rechten Dritter belastet sind.

3. Kaufpreis

Der Kaufpreis beträgt 80.000 EUR. Er ist binnen fünf Bankarbeitstagen auf das der Erwerberin gesondert mitgeteilte Konto der Verkäuferin zu zahlen. Maßgeblich ist der endgültige, frei verfügbare Geldeingang. Ein Zahlungsauftrag allein genügt nicht. Die Verkäuferin teilt den Eingang der Notarin unverzüglich mit und legt einen geeigneten Beleg vor.

4. Abtretung und Bedingung

Die Verkäuferin tritt die bezeichneten Geschäftsanteile an die Erwerberin ab. Die für die Erwerberin auftretende Person erklärt die Annahme. Die Abtretung steht unter der aufschiebenden Bedingung vollständiger Kaufpreiszahlung. Die Frage der nachgewiesenen Vertretung der Erwerberin bleibt hiervon unberührt. Die Beteiligten verpflichten sich, die hierfür benötigten Unterlagen unverzüglich beizubringen.

5. Zustimmung

Die Beteiligten nehmen auf die in Textform dokumentierte Zustimmung der Gesellschafter vom 05.09.2026 Bezug. Die Verkäuferin erklärt, dass sich der Vertragsgegenstand und der Kaufpreis gegenüber dem dort bezeichneten Entwurf nicht geändert haben. Eine Beauftragung von Entwicklungsleistungen durch die Zielgesellschaft wird mit diesem Vertrag nicht vereinbart.

6. Liste und Kosten

Die Notarin soll die Änderung der Gesellschafterliste nach Eintritt der maßgeblichen Voraussetzungen veranlassen. Die Erwerberin trägt die Kosten dieses Vertrags und seines Vollzugs; eine darüber hinausgehende Übernahme ausländischer Beratungs- oder Registerkosten ist gesondert zwischen den Parteien abzustimmen.

7. Weitere Erklärungen

Eine unwirksame Vertretung soll nicht durch eine bloße Mitteilung der Kaufpreiszahlung ersetzt werden. Erforderliche ergänzende Erklärungen sind in der jeweils notwendigen Form abzugeben. Die Beteiligten erhalten Abschriften zur Prüfung und weiteren Nachweisbeschaffung.''','15.09.2026'),
 D('07_eROC_Suchnotiz.png','Interne Abrufnotiz – Namenssuche',
 '''Rechercheboard / Sachbearbeitung Emmerich Holzapfel
16.09.2026, 11:08 Uhr
Suchbegriff: Ceylon Cloud
Treffer übernommen: Ceylon Cloud (Private) Limited
Nummer: PV 00289176
Die Arbeitsansicht zeigt Firma und Nummer. Keine Angabe zur Einzelvertretung gespeichert.
Nirmala: „Das ist der aktuelle Auszug.“
Nächster Dateieingang laut E-Mail: zertifizierte Formularkopien.
Kein Nachweis einer Übermittlung an das deutsche Registergericht.''','16.09.2026'),
 D('08_Gruendungsnachweis_2019_Abschrift.pdf','Gründungsnachweis – deutsche Arbeitsübersetzung',
 '''Ceylon Cloud (Private) Limited – Registrierungsnummer PV 00289176
Gründungsdatum laut übermittelter Kopie: 18.11.2019. Sitzanschrift bei Gründung: 41 Lotus Yard, Colombo 05, Sri Lanka.

Die übermittelte Urkunde bestätigt nach ihrem Wortlaut die Registrierung der bezeichneten Gesellschaft als Private Limited Company. Das Dokument enthält den Firmennamen, die Registrierungsnummer und das Gründungsdatum. Namen der zum 15.09.2026 amtierenden Direktoren oder eine aktuelle Einzelvertretungsregel sind in dieser Kopie nicht aufgeführt.

Übertragungsvermerk von Irmtraud Kandel, 17.09.2026: Grundlage war die von Matthias Dissanayake am 16.09.2026 übersandte englischsprachige PDF-Datei „incorporation_2019.pdf“. Eine elektronische Signaturprüfung oder Rückfrage bei der ausstellenden Stelle wurde für diese Arbeitsübersetzung nicht beauftragt. Der sichtbare Code im unteren Bereich war im zugesandten Scan nur teilweise lesbar.

Eingangsstempel des Büros in Textform: 17.09.2026. Die Originaldatei wurde dem Notariat weitergeleitet; eine Papierausfertigung liegt in diesem Ordner nicht vor.''','17.09.2026'),
 D('09_Secretary_Bestaetigung.docx','Bestätigung des Company Secretary – deutsche Fassung',
 '''An das Notariat Dr. Zingel, Berlin

Sehr geehrte Frau Dr. Zingel,

ich bin seit 2021 als Company Secretary der Ceylon Cloud (Private) Limited tätig. Nach meinen Unterlagen ist die Gesellschaft unter PV 00289176 registriert und hat ihren Geschäftsbetrieb nicht eingestellt. Nirmala Jayawardena ist Direktorin der Gesellschaft. Sie hat die Verhandlungen über die Beteiligung an Kiezkolben geführt und das Board über die wirtschaftlichen Eckpunkte informiert.

Ich bestätige, dass das vorgelegte Dokument „Board approval 12 September“ aus unserem Büro stammt. Es wurde von Nirmala elektronisch an mich übermittelt und von mir in die Beschlusssammlung aufgenommen. Die im Dokument genannte Befugnis sollte den Anteilserwerb in Deutschland ermöglichen. Ich war bei dem deutschen Notartermin nicht anwesend.

Zu der Frage, ob die im Beschluss verwendete Formulierung nach allen Anforderungen des anwendbaren Gesellschaftsrechts zur Alleinvertretung ausreicht, habe ich kein gesondertes Rechtsgutachten erstellt. Nach unserem üblichen Ablauf werden Auslandsverträge von der verhandelnden Direktorin unterzeichnet. Die aktuelle Form-20-Kopie habe ich beantragt und reiche sie nach Eingang weiter.

Mit freundlichen Grüßen
Matthias Dissanayake
Company Secretary
secretary@ceyloncloud.example''','18.09.2026'),
 D('10_Articles_Auszug_Arbeitsuebersetzung.docx','Articles of Association – Arbeitsübersetzung der Organisationsregeln',
 '''Unterlagenbezug: Ceylon Cloud (Private) Limited, Fassung aus dem Gesellschaftsordner vom 18.11.2019, übersandt am 19.09.2026.

1. Zusammensetzung des Board

Die Gesellschaft hat mindestens zwei Direktoren. Das Board führt die Geschäfte, soweit eine Angelegenheit nicht durch zwingendes Recht oder diese Articles der Gesellschafterversammlung vorbehalten ist. Eine Vakanz ist zeitnah zu besetzen.

2. Sitzung und Beschlussfähigkeit

Sitzungen können durch persönliche Teilnahme oder eine gleichzeitige audiovisuelle Verbindung stattfinden. Jeder amtierende Direktor soll eine Einladung mit den wesentlichen Beratungsgegenständen erhalten. Für die Beschlussfähigkeit sind zwei Direktoren erforderlich. Eine Beteiligung per Telefon genügt, wenn alle Teilnehmer einander hören und sich zum Beschlussgegenstand äußern können.

3. Schriftliche Beschlüsse

Ein außerhalb einer Sitzung gefasster Beschluss ist wirksam, wenn sämtliche zur Mitwirkung berechtigten Direktoren dem vollständigen Beschlusstext zustimmen. Die Zustimmung kann in getrennten Dokumenten erklärt werden, sofern der Wortlaut übereinstimmt. Der Company Secretary hält die Erklärungen in der Beschlusssammlung fest.

4. Ausführung von Geschäften

Dokumente werden für die Gesellschaft durch zwei Direktoren oder durch eine Person unterzeichnet, die aufgrund eines wirksam gefassten Board-Beschlusses für das bezeichnete Geschäft hierzu ermächtigt ist. Die Ermächtigung soll Gegenstand und Umfang des Geschäfts erkennen lassen. Diese Bestimmung trifft keine Aussage über zusätzliche zwingende gesetzliche Anforderungen.

5. Dokumentation

Der Company Secretary verwahrt Beschlüsse und führt die Gesellschaftsunterlagen. Er kann Abschriften aus dieser Sammlung bestätigen. Allein aus dieser Aufgabe folgt nach dem vorliegenden Text keine allgemeine Vertretungsmacht für Anteilserwerbe.

Anmerkung der Übersetzerin: Die Fassung wurde aus einem zugesandten Scan übertragen. Ob spätere Änderungen registriert oder beschlossen wurden, ist nicht Gegenstand des Übersetzungsauftrags.''','19.09.2026'),
 D('11_Form20_2024_Abschrift.pdf','Historische Organmeldung – übertragene Daten',
 '''Gesellschaft: Ceylon Cloud (Private) Limited, PV 00289176.
Dokumentbezeichnung der zugesandten Datei: Form 20 – Notice of Change of Director/Secretary.
Ereignisdatum laut Formular: 01.03.2024. Dateiausgabe laut Fußzeile der Kopie: 04.03.2024.

Aufgeführt sind Nirmala Jayawardena als Director, Suresh Weerasinghe als Director und Matthias Dissanayake als Secretary. Für Nirmala und Suresh ist keine auf das deutsche Anteilsgeschäft bezogene Einzelvollmacht enthalten. Eine gesonderte Vertretungsregel ist in den übernommenen Formularfeldern nicht wiedergegeben.

Die Kopie trägt im Dokumentkopf die Registrierungsnummer PV 00289176. Im eingescannten Anhang steht auf einem handschriftlichen Ablagezettel „CeylonCloud / directors final“. Der Ablagezettel ist kein Bestandteil des übernommenen Formulartextes.

Sachbearbeitungsvermerk: Diese Fassung ging am 18.09.2026 ein. Ein aktuelleres Formular war zu diesem Zeitpunkt angekündigt, aber nicht beigefügt. Die Datei wurde nicht als Beweis dafür verwendet, dass seit März 2024 keine Veränderungen mehr stattgefunden haben.''','18.09.2026'),
 D('12_Board_12September.docx','Board approval – deutsche Arbeitsfassung',
 '''Ceylon Cloud (Private) Limited
Beschlussdatum: 12.09.2026. Auf dem Dokument angegeben: „Written board approval“.

Das Board billigt den Erwerb der Geschäftsanteile 3 bis 6 an der Kiezkolben Maschinenverleih GmbH mit einem Gesamtnennbetrag von 10.000 EUR zu einem Kaufpreis von 80.000 EUR. Nirmala Jayawardena wird ermächtigt, die für den Erwerb erforderlichen Erklärungen abzugeben und den Kaufvertrag im deutschen Notartermin zu unterzeichnen. Die Ermächtigung erstreckt sich nicht auf eine Verpflichtung der Kiezkolben zur Abnahme von Softwareleistungen.

Nirmala Jayawardena soll nach Vollzug über die endgültigen Vertragsunterlagen und die neue Gesellschafterliste berichten. Der Company Secretary wird gebeten, dem deutschen Notariat die für den Nachweis der Gesellschaft und ihrer Vertretung erforderlichen Unterlagen zur Verfügung zu stellen.

Am Ende des zugesandten Dokuments stehen die Textzeilen „Nirmala Jayawardena – Director“ und „Matthias Dissanayake – Company Secretary“. Eine weitere Zustimmungserklärung ist in dieser Datei nicht enthalten.

Begleitvermerk aus der E-Mail vom 19.09.2026: Matthias schrieb, Suresh sei zu diesem Zeitpunkt bereits ausgeschieden. Auf die Frage nach einem weiteren Direktor antwortete er, Tariq sei „in transition“. Ein gesondertes Datum wurde in dieser Nachricht nicht genannt.''','12.09.2026'),
 E('13_Suresh_Ruecktritt_weitergeleitet.eml','Weiterleitung: mein Rücktritt',
 '''Liebe Nirmala,

ich lege mein Amt als Director mit Wirkung zum Ende des 9. September nieder. Bitte bestätige den Erhalt dieser Erklärung. Ich werde die laufende Bankvollmacht nicht weiter nutzen. Das Gespräch über Kiezkolben finde ich wirtschaftlich weiterhin sinnvoll, aber ich werde bei dem Kauf nicht mehr mitzeichnen.

Die Unterlagen zu Tariq hatte ich am Montag unterschrieben. Bitte schau, dass das Datum im Formular nicht wieder der Tag des Hochladens wird. Ich kann in der kommenden Woche wegen einer Familienangelegenheit keine Videotermine wahrnehmen.

Suresh

Weiterleitungsvermerk Nirmala, 11.09.2026, 08:10 Uhr: „Received yesterday evening, sorry for late reply. Matthias will update the records.“

Weiterleitung an das Berliner Notariat durch Matthias am 21.09.2026. Die ursprüngliche Serverkopfzeile wurde nicht mitgesendet; diese Nachricht enthält die im Büro weitergeleitete Textfassung.''','2026-09-21T10:20:00+02:00','Matthias Dissanayake <secretary@ceyloncloud.example>','Emmerich Holzapfel <holzapfel@notariat-zingel.example>'),
 {'file':'14_Bankeingaenge_Kunigunde.csv','title':'Kontoumsätze September – Auszug für den Anteilskauf','headers':['Buchungstag','Wertstellung','Buchungstext','Betrag EUR','Kontoinhaberin'],'rows':[['15.09.2026','15.09.2026','Laufende Kosten',-286.40,'Kunigunde Knatter'],['16.09.2026','16.09.2026','CEYLON CLOUD PVT LTD SHARE PURCHASE KK 3-6',80000,'Kunigunde Knatter'],['17.09.2026','17.09.2026','Notariat Vorschuss',-1250,'Kunigunde Knatter'],['18.09.2026','18.09.2026','Umbuchung Tagesgeld',-50000,'Kunigunde Knatter']]},
 E('15_Notariat_Rueckfrage.eml','Kiezkolben / Vertretungsnachweis bitte konkretisieren',
 '''Sehr geehrte Frau Knatter,

Ihre Mitteilung über den Kaufpreiseingang haben wir erhalten. Für die endgültige Einordnung der Erwerbervertretung fehlen weiterhin Unterlagen. Die bisher vorgelegte Organmeldung nennt zwei Direktoren. Der Beschluss vom 12. September enthält nach der zugesandten Fassung nur die Erklärung von Frau Jayawardena und die Bestätigung des Company Secretary.

Bitte teilen Sie uns mit, wer am 12. und am 15. September dem Board angehörte. Falls ein schriftlicher Beschluss außerhalb einer Sitzung gefasst wurde, benötigen wir die zugehörigen Zustimmungen. Falls es eine Sitzung gab, bitten wir um deren vollständige Dokumentation. Wir benötigen außerdem die geltende Satzungsfassung und eine nachvollziehbare Erläuterung des anwendbaren Vertretungsrechts.

Die am 18. September elektronisch übermittelte Liste wurde auf Grundlage des damaligen Arbeitsstands erstellt. Wir haben das Gericht mit heutigem Schreiben gebeten, die beigefügten ergänzenden Hinweise zur noch laufenden Vertretungsprüfung zu beachten. Bitte verwenden Sie die Liste gegenüber der Bank derzeit nicht als abschließenden Nachweis eines unstreitigen Erwerbs.

Mit freundlichen Grüßen
Emmerich Holzapfel
Notariatsmitarbeiter''','2026-09-22T13:48:00+02:00','Emmerich Holzapfel <holzapfel@notariat-zingel.example>','Kunigunde Knatter <kunigunde@kiezkolben.example>'),
 D('16_Gericht_Verfuegung_Arbeitsabschrift.docx','Registergericht – Arbeitsabschrift der Verfügung',
 '''Amtsgericht Charlottenburg – Registergericht
HRB 248765 B – Kiezkolben Maschinenverleih GmbH
Verfügung vom 24.09.2026, laut elektronischem Empfangsnachweis bekanntgegeben am 25.09.2026.

Sehr geehrte Frau Notarin,

zu der am 18.09.2026 eingereichten Gesellschafterliste und Ihrem ergänzenden Schreiben vom 22.09.2026 wird um Erläuterung der Vertretung der neu aufgeführten Ceylon Cloud (Private) Limited gebeten. Die vorliegenden Unterlagen lassen nicht hinreichend erkennen, aufgrund welcher Bestellung und Vertretungsregel Frau Jayawardena den Erwerb am 15.09.2026 allein erklärt hat.

Bitte reichen Sie einen auf diesen Zeitpunkt bezogenen Nachweis ein. Soweit kein entsprechender aktueller Registerauszug verfügbar ist, erläutern Sie die Aussagekraft der vorgelegten amtlichen Unterlagen und der ergänzenden gesellschaftsinternen Dokumente. Zu dem Beschluss vom 12.09.2026 ist insbesondere die vollständige Organbesetzung und Beschlussfassung darzustellen.

Für die Ergänzung wird eine Frist bis zum 12.10.2026 bestimmt. Eine abschließende Entscheidung über die Aufnahme der Liste ist damit nicht verbunden. Bitte nehmen Sie im Antwortschreiben auf die einzelnen Nachweise Bezug und vermeiden Sie eine bloße erneute Übersendung derselben ungeklärten Anlagen.

R. Wendel
Rechtspflegerin

Für die Mandatsakte aus dem übermittelten Dokument übertragen. Keine amtliche Ausfertigung.''','24.09.2026'),
 D('17_Chat_Kiezkolben_Colombo.txt','Chat-Auszug: Freitagabend im Maschinenlager',
 '''25.09.2026, 18:03 – Kunigunde: Otto, du hattest doch zugestimmt. Jetzt steht die Bank auf der Bremse.
18:06 – Otto: Dem Verkauf ja. Nicht einer Unterschrift von jemandem, der vielleicht gar nicht darf. Das ist etwas anderes.
18:09 – Nirmala: I was authorised. Matthias has the board paper.
18:11 – Kunigunde: Können wir hier bitte Deutsch schreiben? Ich verliere schon bei den Dateinamen den Überblick.
18:14 – Nirmala: Entschuldigung. Ich dachte, die Bestätigung von Matthias reicht. Tariq ist seit dem 10. bei uns. Er hat nichts gegen den Kauf.
18:16 – Otto: Hat Tariq den Beschluss vom 12. gesehen oder nicht?
18:21 – Nirmala: Er war in Doha. Ich habe ihm die Eckdaten per Nachricht geschickt. Das eigentliche PDF ging später raus.
18:25 – Kunigunde: Bitte nichts neu datieren. Frau Öztürk soll sagen, welche Unterlagen wirklich nötig sind.
18:29 – Matthias: Ich habe zwei Formulare im System. Eins zeigt den Wechsel, eins den aktualisierten Kontakt. Morgen suche ich die Bestätigung heraus.
18:31 – Otto: Und wir sollten nicht „final-final2“ an ein Gericht schicken.
18:34 – Kunigunde: Das sagt der Mann, dessen Lagerliste „wirklich_neu_7“ heißt.''','25.09.2026'),
 D('18_Lokale_Stellungnahme_entwurf.docx','Vorläufige rechtliche Stellungnahme – zur Tatsachenbestätigung',
 '''An das Notariat Dr. Zingel

Sehr geehrte Frau Dr. Zingel,

ich wurde von Ceylon Cloud (Private) Limited gebeten, die Vertretung beim Erwerb der bezeichneten deutschen Geschäftsanteile zu erläutern. Mir liegen derzeit die Articles in der Fassung vom 18.11.2019, die Organmeldung vom März 2024, der Text eines schriftlichen Beschlusses vom 12.09.2026 und die Rücktrittsnachricht von Herrn Weerasinghe vor. Eine vollständige amtliche historische Registerakte habe ich noch nicht eingesehen.

Nach den vorliegenden Articles kann eine Einzelperson ein bezeichnetes Geschäft ausführen, wenn eine wirksame Board-Ermächtigung besteht. Die vorgelegte Beschlussfassung muss deshalb anhand der tatsächlich amtierenden Direktoren und des gewählten Beschlussverfahrens beurteilt werden. Die Unterschrift des Company Secretary ersetzt nach dem von mir gelesenen Satzungstext nicht die Zustimmung eines weiteren stimmberechtigten Direktors.

Für eine abschließende Stellungnahme benötige ich die Unterlagen zur Bestellung von Herrn Tariq Rahman, den Nachweis des Wirksamkeitsdatums und die vollständige Kommunikation über den Beschluss vom 12.09.2026. Ferner ist zu bestätigen, ob seit 2019 Änderungen der Articles beschlossen wurden. Erst danach kann ich das Ergebnis mit den einschlägigen gesetzlichen Bestimmungen und einer belastbaren Dokumentengrundlage abschließend begründen.

Bitte verwenden Sie diesen Entwurf nicht als vorbehaltlose Bestätigung der Alleinvertretungsmacht am 15.09.2026. Ich kann nach Eingang der genannten Unterlagen kurzfristig eine überarbeitete Fassung liefern.

Mit freundlichen Grüßen
Rechtsanwältin Mala Senanayake
Colombo
mala@senanayake-law.example''','26.09.2026'),
 D('19_Neue_Organmeldung_Abschrift.docx','Nachgereichte Organmeldung – Datenübertragung',
 '''Ceylon Cloud (Private) Limited, PV 00289176
Vom Company Secretary übersandte elektronische Kopie: Form 20, Eingang im Berliner Büro am 28.09.2026.

Im Feld „Date of change“ ist für Tariq Rahman der 10.09.2026 angegeben. Im Feld zur Übermittlung steht 23.09.2026. Für Suresh Weerasinghe ist der 09.09.2026 als Beendigungsdatum eingetragen. Nirmala Jayawardena wird weiterhin als Director aufgeführt. Matthias Dissanayake bleibt als Secretary genannt.

Die beigefügte Bestellungsniederschrift trägt den 05.09.2026 und nennt als Wirksamkeitsdatum den 10.09.2026. Sie beschreibt einen Gesellschafterbeschluss und eine schriftliche Annahmeerklärung von Tariq. Die Annahmeerklärung ist in der zugesandten Datei als eigene Seite enthalten und auf den 08.09.2026 datiert.

Im E-Mail-Betreff der Übersendung steht „current directors 23 September“. Die Unterlagen enthalten keine Aussage dazu, ob Tariq den Beschluss vom 12.09.2026 vollständig erhalten und ihm zugestimmt hat. Eine Bescheinigung über die Echtheit der elektronischen Registerkopie liegt dem deutschen Büro in dieser Datei nicht separat bei.''','28.09.2026'),
 {'file':'20_Dokumente_Colombo_Stand.xlsx','title':'Beschaffungsstand der Auslandsunterlagen','date':'29.09.2026','sheets':[{'name':'Dokumente','headers':['Dokument','Angefordert','Eingegangen','Quelle','Offene Rückfrage'],'rows':[['Incorporation','16.09.2026','16.09.2026','Matthias / PDF','Code im Scan schlecht lesbar'],['Articles 2019','18.09.2026','19.09.2026','Matthias / Scan','Spätere Änderungen?'],['Form 20 März 2024','16.09.2026','18.09.2026','Company file','Historischer Stand'],['Form 20 September 2026','22.09.2026','28.09.2026','eROC-Dateikopie','Herkunft prüfen'],['Tariq Bestellung/Annahme','24.09.2026','28.09.2026','Board-/Gesellschafterordner','Vollständigkeit'],['Zustimmung 12. September','24.09.2026','','Tariq','Vollständiger Text zugegangen?'],['Rechtsgutachten final','25.09.2026','','Mala','Wartet auf Unterlagen']]},{'name':'Kosten','headers':['Position','Netto EUR','USt EUR','Gesamt EUR'],'rows':[['Übersetzung',240,45.6,'=B2+C2'],['Lokale Beratung Vorschuss',600,0,'=B3+C3'],['Kurierreserve',80,0,'=B4+C4'],['Summe','=SUM(B2:B4)','=SUM(C2:C4)','=SUM(D2:D4)']]}]},
 D('21_Board_28September_Bestaetigung.docx','Board-Beschluss zur Bestätigung des Anteilserwerbs',
 '''Ceylon Cloud (Private) Limited
Sitzung vom 28.09.2026, 15:00 bis 15:35 Uhr Colombo-Zeit, per Videokonferenz.

Teilgenommen haben Nirmala Jayawardena und Tariq Rahman. Matthias Dissanayake führte die Niederschrift. Beide Direktoren bestätigen, die vollständige deutsche Arbeitsübersetzung des Vertrags vom 15.09.2026 und die englische Vertragskopie erhalten zu haben. Die Beschlussfähigkeit wird von der Sitzungsleitung festgestellt.

Das Board billigt den Erwerb der Geschäftsanteile 3 bis 6 an der Kiezkolben Maschinenverleih GmbH zum Kaufpreis von 80.000 EUR. Soweit für die Wirksamkeit des bereits erklärten Erwerbs eine weitere Erklärung der Gesellschaft erforderlich sein sollte, soll diese in der vom deutschen Notariat für erforderlich gehaltenen Form abgegeben werden. Nirmala und Tariq sind bereit, hierfür gemeinsam aufzutreten. Eine rückdatierte Erklärung soll nicht erstellt werden.

Tariq erklärt, er habe vor dem 15.09.2026 nur eine Nachricht mit Kaufpreis und Beteiligungsquote erhalten. Der vollständige Vertragsentwurf und der genaue Wortlaut des Beschlusses vom 12.09.2026 seien ihm erst am 22.09.2026 zugegangen. Er habe am 11.09.2026 geschrieben, das Investment sei „im Grundsatz gut“, damals aber noch keinen vollständigen Beschluss unterschrieben.

Das Board bittet die lokale Rechtsberaterin, die neuen Unterlagen zu prüfen und das deutsche Notariat über die möglichen weiteren Schritte zu informieren. Die ursprünglichen Nachrichten und Dokumente sollen unverändert aufbewahrt werden.

Textlich vermerkte Unterzeichnungen: Nirmala Jayawardena; Tariq Rahman. Der Company Secretary hat die Datei am 29.09.2026 weitergeleitet. Die Signatur- und Identitätsprüfung der elektronischen Datei ist in dieser Arbeitsabschrift nicht enthalten.''','28.09.2026'),
 E('22_Matthias_zu_den_Bestaetigungen.eml','Welche Bestätigung brauchen Sie genau?',
 '''Sehr geehrte Frau Öztürk,

ich habe die neuen Kopien aus dem Company-File-System geschickt. Es gibt hier ein Unternehmensregister; das ist also nicht das Problem. Einen Auszug mit einer deutschen Formulierung „alleinvertretungsberechtigt“ bekomme ich auf Knopfdruck allerdings nicht. Ich kann weitere amtliche Formularkopien beschaffen und die Dokumentkennungen weitergeben.

Eine Apostille für Sri Lanka konnte ich nicht bestellen. Ein Dienstleister hat mir stattdessen eine notarielle Bestätigung meiner Unterschrift angeboten. Bitte sagen Sie mir, ob Sie das überhaupt benötigen. Ich möchte nicht wieder 300 Euro für einen Stempel ausgeben, der Ihre Frage nicht beantwortet.

Zu dem Beschluss vom 12. September: Ich hatte Nirmalas Datei in die Sammlung übernommen und angenommen, Tariq sei einverstanden. Eine separate Zustimmung zum genauen Text habe ich nicht gefunden. Die neue Erklärung vom 28. September liegt jetzt vor. Mala hat um die unveränderten Originaldateien gebeten; die schicke ich ihr heute.

Mit freundlichen Grüßen
Matthias Dissanayake''','2026-09-30T07:42:00+02:00','Matthias Dissanayake <secretary@ceyloncloud.example>','Derya Öztürk <derya@kanzlei-spreebogen.example>'),
 D('23_Uebersetzungsrechnung.pdf','Rechnung IK-2026-118',
 '''Irmtraud Kandel – Übersetzungsbüro
An: Kiezkolben Maschinenverleih GmbH, Zangenhof 14, 10997 Berlin
Rechnungsdatum: 29.09.2026. Leistungszeitraum: 17.09.2026 bis 29.09.2026.

Übertragung der Gründungsbescheinigung, der Organisationsbestimmungen und zweier Organmeldungen aus dem Englischen ins Deutsche für die interne rechtliche Bearbeitung: 240,00 EUR netto.
Umsatzsteuer 19 Prozent: 45,60 EUR.
Rechnungsbetrag: 285,60 EUR.

Die Leistung umfasst keine Bescheinigung zur Echtheit der Ausgangsdokumente und keine rechtliche Bewertung der Vertretungsmacht. Eine zur Vorlage beim Gericht geeignete bestätigte Übersetzung war bislang nicht beauftragt. Bitte teilen Sie mit, falls ein solcher weiterer Auftrag nach Rücksprache mit dem Notariat erforderlich wird.

Zahlbar bis 13.10.2026 unter Angabe der Rechnungsnummer. Bankverbindung wird im geschützten Kundenportal bereitgestellt.
Kontakt: rechnung@kandel-uebersetzt.example''','29.09.2026'),
 E('24_Otto_Status_bleibt_offen.eml','Zur Liste und zur nächsten Versammlung',
 '''Sehr geehrte Frau Öztürk,

ich möchte klarstellen, dass ich dem Verkauf weiterhin nicht grundsätzlich widerspreche. Ich bestreite aber, dass die Erwerberin schon durch die bisherige Erklärung wirksam Gesellschafterin geworden ist. Sollte die Liste jetzt einfach aufgenommen werden, wäre meine Frage damit nicht erledigt.

Für die Versammlung am 9. Oktober stehen Budget und Geschäftsführerentlastung auf der Tagesordnung. Kunigunde möchte Nirmala bereits mit vierzig Prozent abstimmen lassen. Ich bitte um eine klare Rückmeldung, welche Unterlagen tatsächlich vorliegen und ob wir den Termin verschieben sollten. Eine Beschlussfassung über das Entwicklungsprojekt ist von meiner damaligen Zustimmung zum Verkauf nicht umfasst.

Ich habe keine Unterlagen vernichtet und keine eigene Liste an das Gericht geschickt. In meiner Ablage liegt weiterhin die Liste vom Mai 2024. Bitte übernehmen Sie die Zahl „60 Prozent Kunigunde“ nicht einfach in jedes neue Schreiben, wenn der Erwerb inzwischen anderweitig wirksam bestätigt sein sollte. Ich möchte nur, dass wir das nachvollziehbar klären.

Mit freundlichen Grüßen
Otto Pumpernickel''','2026-09-30T16:31:00+02:00','Otto Pumpernickel <otto@kiezkolben.example>','Derya Öztürk <derya@kanzlei-spreebogen.example>')
 ]})
CASES.append({
 'slug':'handelsregister-assistent-polter-prokura','plugin':'handelsregister-assistent',
 'title':'Polter & Partner: zwei Unterschriften zu wenig',
 'subtitle':'Ein Geschäftsführerwechsel zwischen Lagerhalle, Bank und Videotermin',
 'date':'01.10.2026','client':'Polter Veranstaltungstechnik GmbH',
 'summary':'Bei Polter Veranstaltungstechnik soll Aylin Yılmaz die Geschäftsführung übernehmen. Die alte Prokuristin hält ihre Befugnis für unverändert, die Personalabteilung für beendet. Ein im Ausland durchgeführter Videotermin und eine dringende Bankanfrage sorgen dafür, dass mehrere Beteiligte dieselben Unterlagen für ganz unterschiedliche Dinge verwenden.',
 'assignment':'Erstellen Sie eine datierte Organ- und Vertretungsübersicht, prüfen Sie die vorbereitete Registerstrecke und fertigen Sie den konkreten Notariatsauftrag sowie die notwendige Antwort zum Vollzugsstand. Benennen Sie entscheidende offene Tatsachen und senden Sie nichts ab.',
 'documents':[
 E('01_Aylin_Mandatsanfrage.eml','Ich soll heute anfangen – wer darf jetzt was?',
 '''Sehr geehrte Frau Dr. Abendroth,

ich bin laut Beschluss seit heute Geschäftsführerin von Polter Veranstaltungstechnik. Die Bank führt weiter Hieronymus als Geschäftsführer und Erna als Prokuristin. Hildegard meint, die Prokura sei schon vor zwei Wochen per E-Mail beendet worden. Erna sagt, eine Gesellschafterin könne ihr das nicht einfach schreiben. Im Lager wartet ein Vertrag über neue Traversenteile, der angeblich schon unterschrieben ist.

Herr Knautsch hat die Registerunterlagen während seines Urlaubs in Österreich online beglaubigen lassen. Das Registergericht hat jetzt eine Nachricht geschickt, die ich noch nicht richtig verstehe. Bitte ordnen Sie das und bereiten Sie die richtigen Unterlagen vor. Ich möchte nicht auf gut Glück dieselbe Datei ein zweites Mal einreichen.

Ich kann morgen um elf Uhr zu einem Berliner Notar kommen. Meine persönlichen Angaben sind im Personalbogen; meine privaten Ausweiskopien möchte ich nicht öffentlich im Register sehen. Wenn Sie noch eine Erklärung von mir brauchen, sagen Sie bitte genau welche.

Mit freundlichen Grüßen
Aylin Yılmaz''','2026-10-01T07:58:00+02:00','Aylin Yılmaz <aylin@polter-technik.example>','Dr. Frieda Abendroth <frieda@abendroth-recht.example>'),
 D('02_Register_Altstand_Arbeitskopie.pdf','Registerstand vom 30.09.2026 – Arbeitsabschrift',
 '''Amtsgericht Charlottenburg, HRB 219843 B
Polter Veranstaltungstechnik GmbH, Berlin
Geschäftsanschrift: Kulissenweg 8, 12059 Berlin. Stammkapital: 50.000 EUR.

Allgemeine Vertretungsregel: Ist nur ein Geschäftsführer bestellt, vertritt er die Gesellschaft allein. Sind mehrere Geschäftsführer bestellt, wird die Gesellschaft durch zwei Geschäftsführer gemeinsam oder durch einen Geschäftsführer gemeinsam mit einem Prokuristen vertreten.

Geschäftsführer: Hieronymus Knautsch, geboren am 03.06.1968, Berlin, einzelvertretungsberechtigt. Befreiung von den Beschränkungen des § 181 BGB ist eingetragen.

Prokura: Erna-Louise Zickzack, geboren am 19.11.1977, Berlin. Gesamtprokura gemeinsam mit einem Geschäftsführer oder einem weiteren Prokuristen. Eine weitere Prokuristenperson ist im aktuellen Ausdruck nicht aufgeführt.

Dokumentenansicht: Satzung vom 17.04.2021; Gesellschafterliste vom 18.04.2021. Zu einer am 28.09.2026 eingegangenen Anmeldung ist noch keine Veränderung im Registerblatt ersichtlich.

Abgerufen und für die Arbeitsakte übertragen von Lenja Özdemir am 30.09.2026, 16:18 Uhr. Keine amtlich beglaubigte Ausfertigung.''','30.09.2026'),
 {'file':'03_Gesellschafter_und_Stimmen.xlsx','title':'Beteiligung und Beschlussstimmen','date':'12.09.2026','sheets':[{'name':'Beteiligung','headers':['Person','Anteil','Nennbetrag EUR','Kapitalquote','Stimmen'],'rows':[['Hildegard Polter',1,30000,'=C2/50000',30000],['Yusuf Demir',2,20000,'=C3/50000',20000],['Summe','', '=SUM(C2:C3)','=SUM(D2:D3)','=SUM(E2:E3)']],'formats':{'D':'0.00%'}},{'name':'Beschluss_12September','headers':['Gegenstand','Polter','Demir','Ergebnis laut Protokoll'],'rows':[['Abberufung Knautsch zum 30.09.',30000,20000,'Zustimmung beider'],['Bestellung Yılmaz ab 01.10.',30000,20000,'Zustimmung beider'],['Einzelvertretung Yılmaz',30000,20000,'Zustimmung beider'],['Prokura Zickzack','nicht abgestimmt','nicht abgestimmt','kein Beschlusspunkt']]}]},
 D('04_Satzung_Auszug.docx','Satzung – Organisationsbestimmungen',
 '''1. Geschäftsführung und Vertretung

Die Gesellschaft hat einen oder mehrere Geschäftsführer. Ist nur ein Geschäftsführer bestellt, vertritt dieser allein. Bei mehreren Geschäftsführern vertreten zwei Geschäftsführer gemeinsam oder ein Geschäftsführer gemeinsam mit einem Prokuristen. Die Gesellschafterversammlung kann einzelnen Geschäftsführern Einzelvertretungsbefugnis und Befreiung von den Beschränkungen des § 181 BGB erteilen.

2. Gesellschafterbeschlüsse

Soweit Gesetz oder Satzung nichts anderes bestimmen, werden Beschlüsse mit einfacher Mehrheit der abgegebenen Stimmen gefasst. Je ein Euro eines Geschäftsanteils gewährt eine Stimme. Eine Beschlussfassung außerhalb einer Versammlung ist zulässig, wenn sämtliche Gesellschafter der konkreten Form zustimmen.

3. Zustimmungspflichtige Geschäfte

Die Geschäftsführung bedarf intern der Zustimmung der Gesellschafterversammlung für Investitionen von mehr als 75.000 EUR im Einzelfall sowie für die Bestellung von Prokuristen. Die Vertretungsbefugnis gegenüber Dritten richtet sich nach den gesetzlichen Vorschriften. Eine interne Zustimmung ersetzt keine erforderliche Mitwirkung eines weiteren Vertretungsberechtigten.

4. Personal und Vollmachten

Die Geschäftsführung organisiert die Personalverwaltung und kann Handlungsvollmachten erteilen. Die Personalabteilung handelt innerhalb der ihr übertragenen Aufgaben. Eine allgemeine Befugnis zur Erteilung oder zum Widerruf von Prokura ist mit der Leitung der Personalabteilung nicht verbunden.

Arbeitsabschrift der Fassung vom 17.04.2021, erstellt für die Akte am 29.09.2026. Die vollständige Satzungsdatei wurde dem Notariat bereits übermittelt.''','17.04.2021'),
 D('05_Beschluss_12September.docx','Niederschrift der Gesellschafterversammlung',
 '''Polter Veranstaltungstechnik GmbH
Versammlung am 12.09.2026, 10:00 bis 10:45 Uhr, Kulissenweg 8, Berlin.

Anwesend waren Hildegard Polter mit dem Geschäftsanteil 1 im Nennbetrag von 30.000 EUR und Yusuf Demir mit dem Geschäftsanteil 2 im Nennbetrag von 20.000 EUR. Beide erklärten sich mit Durchführung und Tagesordnung einverstanden. Hildegard führte den Vorsitz; Yusuf fertigte die Niederschrift.

1. Wechsel der Geschäftsführung

Hieronymus Knautsch wird mit Ablauf des 30.09.2026 als Geschäftsführer abberufen. Seine Tätigkeit bis zu diesem Zeitpunkt soll die geordnete Übergabe der laufenden Aufträge ermöglichen. Der Anstellungsvertrag und dessen Beendigung werden gesondert geregelt.

Aylin Yılmaz, geboren am 22.08.1986, wohnhaft in Berlin, wird mit Wirkung ab dem 01.10.2026 zur Geschäftsführerin bestellt. Sie soll die Gesellschaft einzeln vertreten dürfen. Eine Befreiung von den Beschränkungen des § 181 BGB wird in diesem Beschluss nicht erteilt. Frau Yılmaz soll ihre Annahme schriftlich erklären.

2. Vollzug

Die Geschäftsführung wird gebeten, die erforderlichen Registerunterlagen vorzubereiten und den notariellen Vollzug zu koordinieren. Die Gesellschafter wollen vor einer Einreichung die endgültige Fassung erhalten. Der Wechsel soll gegenüber Banken und wesentlichen Auftraggebern anhand der tatsächlich vorliegenden Nachweise kommuniziert werden.

3. Prokura

Die künftige Stellung von Erna-Louise Zickzack wurde besprochen, aber nicht beschlossen. Hildegard wünscht eine Verringerung ihrer Bankzugriffe. Yusuf bittet, erst das Gespräch mit Frau Zickzack am 20.09.2026 abzuwarten. Ein Widerruf der Prokura ist nicht Bestandteil dieses Beschlusses.

Sämtliche Beschlüsse zu Ziffern 1 und 2 wurden mit 50.000 Ja-Stimmen gefasst. Die Textfassung wurde am selben Tag von beiden Gesellschaftern bestätigt.''','12.09.2026'),
 D('06_Annahme_Aylin.docx','Annahme der Geschäftsführerbestellung',
 '''An die Polter Veranstaltungstechnik GmbH, zu Händen der Gesellschafter

Sehr geehrte Frau Polter, sehr geehrter Herr Demir,

ich nehme die im Beschluss vom 12.09.2026 enthaltene Bestellung zur Geschäftsführerin mit Wirkung ab dem 01.10.2026 an. Die Einzelvertretungsbefugnis habe ich zur Kenntnis genommen. Mir ist bekannt, dass der Beschluss keine Befreiung von den Beschränkungen des § 181 BGB enthält.

Für die Vorbereitung der Anmeldung werde ich die erforderlichen persönlichen Angaben unmittelbar an das verantwortliche Notariat übermitteln. Eine Erklärung über gesetzliche Bestellungshindernisse möchte ich nach der vorgesehenen Belehrung in der dafür erforderlichen Form abgeben. Diese Annahmeerklärung soll eine solche Versicherung nicht ersetzen.

Ich werde vor dem 01.10.2026 die Übergabe vorbereiten, aber keine Erklärung als bereits amtierende Geschäftsführerin abgeben. Soweit vor diesem Datum eine gesonderte Vollmacht benötigt wird, bitte ich um einen konkreten Entwurf mit bezeichnetem Umfang.

Mit freundlichen Grüßen
Aylin Yılmaz
Berlin, 14.09.2026''','14.09.2026'),
 D('07_Dienstvertrag_Ende_Knautsch.docx','Vereinbarung zur Beendigung des Dienstverhältnisses',
 '''Zwischen Polter Veranstaltungstechnik GmbH und Hieronymus Knautsch wird vereinbart:

1. Vertragsende

Der Geschäftsführerdienstvertrag endet im gegenseitigen Einvernehmen mit Ablauf des 31.10.2026. Ab dem 01.10.2026 unterstützt Herr Knautsch die Übergabe auf Anforderung von Frau Yılmaz. Mit dieser Unterstützungsaufgabe wird keine neue organschaftliche Vertretungsbefugnis begründet.

2. Vergütung und Herausgabe

Die bisherige monatliche Vergütung wird bis zum Vertragsende fortgezahlt. Firmenfahrzeug, Schlüssel und Mobiltelefon sind spätestens am 02.11.2026 zurückzugeben. Das elektronische Signaturmittel soll nicht an eine andere Person weitergegeben werden; die zuständige Administration koordiniert die Sperrung beziehungsweise Rückgabe mit Herrn Knautsch.

3. Register und Außenauftritt

Die Parteien nehmen den gesonderten Gesellschafterbeschluss zur Abberufung mit Ablauf des 30.09.2026 zur Kenntnis. Diese Vereinbarung verschiebt dieses Datum nicht. Geschäftspartneranfragen nach dem 01.10.2026 sind an die neue Geschäftsführung weiterzuleiten.

4. Offene Angelegenheiten

Die abschließende Abrechnung von Reisekosten und Urlaub erfolgt getrennt. Die Parteien bestätigen keine vollständige Erledigung aller Ansprüche aus dem Dienstverhältnis.

Textlich bestätigte Unterzeichnungen vom 18.09.2026: Hildegard Polter für die aufgrund Gesellschafterbeschlusses vertretene Gesellschaft; Hieronymus Knautsch.''','18.09.2026'),
 D('08_Prokura_Erna_2022.docx','Erteilung der Gesamtprokura',
 '''Sehr geehrte Frau Zickzack,

hiermit erteile ich Ihnen namens der Polter Veranstaltungstechnik GmbH mit Wirkung ab dem 01.07.2022 Gesamtprokura gemeinsam mit einem Geschäftsführer oder einem weiteren Prokuristen. Die Erteilung erfolgt auf Grundlage der Zustimmung der Gesellschafterversammlung vom 24.06.2022. Die Anmeldung zum Handelsregister wird veranlasst.

Für den internen Geschäftsablauf ist vorgesehen, dass Investitionen oberhalb von 25.000 EUR vorab mit der Geschäftsführung abgestimmt werden. Diese interne Vorgabe soll den gesetzlichen Umfang der Prokura im Außenverhältnis nicht abweichend darstellen. Für Grundstücksveräußerungen oder Grundstücksbelastungen wird mit diesem Schreiben keine besondere Ermächtigung erteilt.

Bitte verwenden Sie bei Unterzeichnung den Zusatz „ppa.“ und beachten Sie, dass Ihre Unterschrift nach der erteilten Gesamtprokura die Mitwirkung einer weiteren befugten Person voraussetzt. Die Ablage einer eingescannten Unterschrift einer anderen Person ersetzt deren Mitwirkung nicht.

Mit freundlichen Grüßen
Hieronymus Knautsch
Geschäftsführer
Empfang von Erna-Louise Zickzack am 30.06.2022 bestätigt.''','30.06.2022'),
 E('09_Hildegard_Personalabteilung.eml','Erna bitte sofort aus den Freigaben nehmen',
 '''Liebe Lenja,

bitte nehmt Erna ab sofort aus allen Freigaben. Wir haben am 12. beschlossen, dass Aylin übernimmt. Ich möchte nicht, dass kurz vorher noch etwas Großes bestellt wird. Schreibt ihr bitte, dass ihre Prokura damit beendet ist. Ich habe heute keine Zeit für die Formulare.

Hieronymus ist bis Sonntag in Tirol, aber telefonisch erreichbar. Er weiß, dass ich keine Alleingänge mehr will. Yusuf und ich besprechen die restlichen Personalthemen nächste Woche. Bitte sperrt nicht gleich ihren gesamten Zugang; sie muss die Lohnliste noch fertig machen.

Hildegard

Weiterleitungsvermerk Lenja an Erna, 15.09.2026, 14:22 Uhr: „Anbei die Weisung von Frau Polter. Bitte keine Bestellungen mehr freigeben.“''','2026-09-15T13:41:00+02:00','Hildegard Polter <hildegard@polter-technik.example>','Lenja Özdemir <personal@polter-technik.example>'),
 E('10_Erna_Reaktion.eml','Re: Freigaben und Prokura',
 '''Liebe Lenja,

ich werde selbstverständlich keine neuen Investitionen ohne Abstimmung freigeben. Die Behauptung, meine Prokura sei automatisch durch Aylins Bestellung beendet, verstehe ich aber nicht. Aylin fängt doch erst im Oktober an. Im Beschluss vom 12. September steht nach meiner Kopie ausdrücklich, dass über mich noch nicht entschieden wurde.

Bitte lass mir eine eindeutige Erklärung der zuständigen Geschäftsführung zukommen, wenn die Prokura widerrufen werden soll. Bis dahin werde ich nur die bereits abgestimmten Routinevorgänge bearbeiten. Ich unterschreibe ohnehin nicht allein; bei der Bank ist aber eine technische Einzelbestätigung für vorbereitete Zahlungen hinterlegt. Diese Berechtigung kann gern separat geändert werden.

Das Angebot über die Traversenteile ist noch nicht angenommen. Der Lieferant hat uns bis Ende September den Preis zugesagt. Hieronymus wollte sich am Montag darum kümmern.

Viele Grüße
Erna''','2026-09-16T08:25:00+02:00','Erna-Louise Zickzack <erna@polter-technik.example>','Lenja Özdemir <personal@polter-technik.example>'),
 D('11_Widerruf_Prokura.docx','Widerruf der Prokura',
 '''An Frau Erna-Louise Zickzack
Polter Veranstaltungstechnik GmbH

Sehr geehrte Frau Zickzack,

namens der Polter Veranstaltungstechnik GmbH widerrufe ich hiermit die Ihnen erteilte Prokura mit Wirkung ab Zugang dieser Erklärung. Ihre Befugnisse aus gesonderten Handlungsvollmachten bleiben nur insoweit bestehen, wie sie Ihnen ausdrücklich schriftlich bestätigt werden. Die technische Bankberechtigung wird unabhängig davon angepasst.

Bitte geben Sie ab Zugang dieser Erklärung keine neuen Erklärungen unter Verwendung der Prokura ab. Bereits vorbereitete Vorgänge legen Sie mir bis zum Ende meiner Amtszeit und anschließend Frau Yılmaz zur Entscheidung vor. Die Anmeldung des Erlöschens der Prokura zum Handelsregister wird veranlasst.

Dieser Widerruf enthält keine Kündigung Ihres Arbeitsverhältnisses. Die weitere Aufgabenverteilung wird mit Ihnen gesondert besprochen.

Mit freundlichen Grüßen
Hieronymus Knautsch
Geschäftsführer
Berlin, 27.09.2026

Übermittlungsvermerk der Assistenz: Als PDF an erna@polter-technik.example am 29.09.2026, 10:14 Uhr versandt; Papierumschlag am selben Tag auf ihren Schreibtisch gelegt. Persönliche Übergabe nicht dokumentiert.''','27.09.2026'),
 D('12_Mailserver_und_Buero_Notiz.txt','Zugangsnachweise aus IT und Büro',
 '''29.09.2026, 10:14:12 – Nachricht „Prokura / Erklärung Geschäftsführung“ vom Server angenommen.
10:14:14 – Zustellung an Postfach erna@polter-technik.example protokolliert.
10:14:15 – Regel „Personal vertraulich“ verschiebt Nachricht in Unterordner Personal.
Kein Lesebestätigungsereignis angefordert. Die IT kann aus diesem Protokoll nicht feststellen, wann Erna die Nachricht tatsächlich geöffnet hat.

Lenja, Notiz vom 30.09.2026: Ich habe den Umschlag am 29. gegen halb elf auf Ernas Platz gelegt. Sie war vormittags im Außenlager. Als ich um 16 Uhr ging, lag der Umschlag nicht mehr dort. Ich weiß nicht, wer ihn mitgenommen hat.

Erna, Nachricht vom 30.09.2026, 08:32 Uhr: „Ich habe den Brief heute früh geöffnet. Die Mail war in einem Unterordner, den ich gestern nicht angesehen habe. Den Umschlag hatte ich gestern Nachmittag in meine Tasche gesteckt, weil ich zum Lieferanten musste.“

Hieronymus, Telefonnotiz: Er habe Erna am 28. schon gesagt, dass der Widerruf kommen werde. Er sei sich nicht sicher, ob er „ab jetzt“ oder „sobald der Brief da ist“ gesagt habe.''','30.09.2026'),
 D('13_Traversteile_Bestellung.docx','Bestellung VT-260929',
 '''Bestellerin: Polter Veranstaltungstechnik GmbH, Kulissenweg 8, 12059 Berlin.
Lieferantin: Bühnenbolzen Technik GmbH, Rampenstraße 22, 39108 Magdeburg.

1. Ware und Preis

Bestellt werden 48 Aluminiumtraversen des Typs BB-T40, 96 Verbinder und zwei Transportwagen gemäß Angebot BB-447 vom 10.09.2026. Der Gesamtpreis beträgt 38.400 EUR netto zuzüglich gesetzlicher Umsatzsteuer. Die Lieferung soll bis zum 30.10.2026 an das Berliner Lager erfolgen.

2. Zahlung

Eine Anzahlung von 30 Prozent ist nach schriftlicher Auftragsbestätigung fällig. Der Rest ist binnen 14 Tagen nach vollständiger Lieferung und Rechnungseingang zu zahlen. Die Parteien haben keine automatische Belastung des Bankkontos vereinbart.

3. Annahme und Unterzeichnung

Auf der von der Lieferantin zurückgesandten Arbeitskopie steht unter „Polter Veranstaltungstechnik GmbH“ die Textzeile „ppa. Erna-Louise Zickzack“. Ein zweites Namensfeld ist leer. Im Begleittext der E-Mail vom 29.09.2026, 18:02 Uhr, schrieb Erna: „Hieronymus hat es grundsätzlich freigegeben; seine Unterschrift kommt nach.“

Die Lieferantin bestätigte am 30.09.2026, 09:11 Uhr, die Reservierung der Ware und bat um eine zweite Unterschrift oder einen aktuellen Nachweis, dass Erna allein handeln dürfe. Eine Anzahlung ist im beigefügten Zahlungsjournal bis zum 01.10.2026 nicht erfasst.''','29.09.2026'),
 E('14_Bank_Berechtigungen.eml','Polter GmbH – Organwechsel und Zeichnung',
 '''Sehr geehrte Frau Yılmaz,

vielen Dank für den Beschluss und Ihre Nachricht. In unseren Stammdaten ist weiterhin Herr Knautsch als Geschäftsführer hinterlegt. Für Frau Zickzack besteht eine technische Berechtigung zur Freigabe vorbereiteter Zahlungen bis 20.000 EUR. Diese Bankberechtigung beruht auf einer gesonderten Kontovereinbarung und wird nicht allein durch einen Registerabruf automatisch geändert.

Bitte teilen Sie uns mit, welche Änderung Sie konkret wünschen, und reichen Sie die hierfür erforderlichen Erklärungen der vertretungsberechtigten Gesellschaft ein. Den Nachweis Ihres Amtsbeginns und der Vertretungsregel prüfen wir anhand der vorhandenen Dokumente und des aktuellen Registerstands. Die bloße E-Mail von Frau Polter genügt für die gewünschte Kontoumstellung nicht.

Das von Ihnen übersandte Dokument zur österreichischen Videobeglaubigung prüfen wir nicht als Bestätigung einer bereits erfolgten Registereintragung. Bitte senden Sie uns die gerichtliche Vollzugsmitteilung nach, sobald diese vorliegt. Für die zwischenzeitliche Bearbeitung steht Ihnen Frau Birkner telefonisch zur Verfügung.

Mit freundlichen Grüßen
Saskia Birkner
Firmenkundenservice, Spreebogen Bank''','2026-09-30T11:03:00+02:00','Saskia Birkner <firmenkunden@spreebogen-bank.example>','Aylin Yılmaz <aylin@polter-technik.example>'),
 {'file':'15_Zeichnungsplan_verschiedene_Staende.xlsx','title':'Zeichnungs- und Systemberechtigungen','date':'30.09.2026','sheets':[{'name':'Recht_und_System','headers':['Person','Funktion laut interner Liste','Registerstand 30.09.','Bankzugriff','Letzte Änderung','Bemerkung'],'rows':[['Hieronymus Knautsch','GF bis 30.09.','GF einzeln','Administrator','01.07.2022','Sperrung zum 01.10. angefragt'],['Aylin Yılmaz','GF ab 01.10.','noch nicht eingetragen','Leserecht','25.09.2026','Unterschriftsprobe fehlt'],['Erna-Louise Zickzack','Einkauf/Personal','Gesamtprokura','Freigabe bis 20000','15.09.2026','Personalnotiz: Prokura beendet'],['Lenja Özdemir','Personalverwaltung','keine Eintragung','kein Zugriff','03.02.2025','führt Stammdaten']]},{'name':'Zahlungsjournal','headers':['Datum','Vorgang','Netto EUR','USt EUR','Brutto EUR','Status'],'rows':[['29.09.2026','Traversen Angebot',38400,'=ROUND(C2*0.19,2)','=C2+D2','keine Zahlung'],['30.09.2026','Anzahlung geplant','=ROUND(C2*0.3,2)','=ROUND(D2*0.3,2)','=C3+D3','nicht freigegeben'],['30.09.2026','Büromaterial',148.9,'=ROUND(C4*0.19,2)','=C4+D4','bezahlt']] }]},
 D('16_Videobeglaubigung_Arbeitskopie.pdf','Österreichischer Videotermin – übertragene Angaben',
 '''Dokumentbezeichnung der erhaltenen Datei: „Beglaubigung elektronischer Signatur – Polter GmbH“.
Termin laut Datei: 26.09.2026, 15:00 Uhr. Urkundsperson laut Kopf: Mag. Severin Moosbauer, Notar mit Amtssitz in Salzburg. Beteiligte laut Protokoll: Hieronymus Knautsch und Aylin Yılmaz.

Der Text beschreibt eine optische und akustische Zweiwegverbindung über einen von einem privaten Dienstleister bereitgestellten Videodienst. Zur Identifizierung seien Ausweise in die Kamera gehalten und anhand von Sicherheitsmerkmalen geprüft worden. Eine elektronische Signatur der Beteiligten sei anschließend im vorgesehenen Dienst erstellt worden. Angaben zum elektronischen Auslesen eines amtlich gespeicherten Lichtbilds sind in dieser Arbeitskopie nicht enthalten.

Als Gegenstand werden die Anmeldung des Geschäftsführerwechsels zum 01.10.2026 und die Änderung der Vertretung genannt. Die Prokura von Erna-Louise Zickzack ist im Anlagenverzeichnis dieser Fassung nicht aufgeführt.

Die Datei wurde am 27.09.2026 von Herrn Knautsch an die Berliner Sachbearbeitung geschickt. Die Sachbearbeitung hat weder das technische Identifizierungsverfahren noch die Signatur selbst geprüft. Diese Arbeitsabschrift gibt den übermittelten Text wieder und stellt keine deutsche Anerkennungs- oder Gleichwertigkeitsbescheinigung dar.''','27.09.2026'),
 E('17_Knautsch_war_doch_Notar.eml','Der Videotermin war doch beim Notar',
 '''Liebe Aylin, liebe Frieda,

ich verstehe die Aufregung nicht ganz. Der Termin war bei einem richtigen Notar in Österreich, nicht bei irgendeiner App. Wir haben unsere Ausweise gezeigt und elektronisch unterschrieben. Ich dachte, in der EU müsse das funktionieren. Der Dienstleister hatte ausdrücklich „für deutsche Register“ geschrieben.

Die Prokura hatte ich in dieser Fassung noch nicht aufgenommen, weil Erna den Brief erst bekommen sollte. Wenn wir deshalb noch etwas ergänzen müssen, mache ich das. Ab heute bin ich aber nicht mehr Geschäftsführer. Bitte prüfen Sie deshalb auch, wer die Ergänzung jetzt unterschreiben muss.

Den Vertrag mit Bühnenbolzen habe ich nicht selbst unterschrieben. Ich hatte Erna gesagt, der Preis sei in Ordnung. Das war am Telefon, vor der Widerrufserklärung. Ob ich dabei schon verbindlich bestellt habe, müsste man sich genau ansehen; die Lieferantin war nicht im Gespräch.

Viele Grüße
Hieronymus''','2026-10-01T09:06:00+02:00','Hieronymus Knautsch <hieronymus@polter-technik.example>','Aylin Yılmaz <aylin@polter-technik.example>'),
 D('18_Registergericht_Formhinweis.docx','Registergericht – Mitteilung zur Anmeldung',
 '''Amtsgericht Charlottenburg – Registergericht
HRB 219843 B – Polter Veranstaltungstechnik GmbH
Mitteilung vom 30.09.2026, elektronisch eingegangen im bearbeitenden Notariat um 14:46 Uhr.

Sehr geehrte Damen und Herren,

zu der am 28.09.2026 eingegangenen Anmeldung wird darauf hingewiesen, dass die vorgelegte Onlinebeglaubigung nicht ohne Weiteres als formgerechter Nachweis behandelt werden kann. Aus der übermittelten Beschreibung ergibt sich ein österreichisches Videobeglaubigungsverfahren. Bitte legen Sie dar, auf welcher Grundlage dessen Gleichwertigkeit für den angemeldeten Vorgang angenommen wird, oder reichen Sie eine den geltenden Anforderungen entsprechende Anmeldung ein.

Die angemeldete Bestellung ist nach dem beigefügten Beschluss auf den 01.10.2026 bezogen. Der derzeitige Registerstand ist noch nicht geändert. Hinsichtlich einer Prokuraänderung enthält die eingegangene Anmeldung keine Erklärung.

Vor einer abschließenden Entscheidung wird Gelegenheit zur Stellungnahme bis zum 14.10.2026 gegeben. Bei einer neu eingereichten Fassung bitten wir um eindeutige Bezeichnung, in welchem Umfang diese die bisherige Anmeldung ersetzen oder ergänzen soll.

R. Wendel, Rechtspflegerin
Für die Mandatsakte aus der elektronisch übermittelten Nachricht übertragen; ohne amtliche Beglaubigung.''','30.09.2026'),
 D('19_Telefonnotiz_Notariat.txt','Telefonat mit dem Berliner Notariat',
 '''01.10.2026, 09:35 bis09:48 Uhr
Teilnehmer: Lenja Özdemir und Notariatsmitarbeiterin Fritzi Brösel, Büro Notar Dr. Wendelin Wacker.

Frau Brösel bietet einen Termin am02.10.um11:00Uhr an. Frau Yılmaz soll die Einladung und Hinweise zur Identifizierung direkt erhalten. Das Büro benötigt vorab den vollständigen Satzungstext, Beschluss vom12.09., Annahmeerklärung und die aktuelle Registerkopie. Die persönliche Versicherung soll im Termin anhand der vorgesehenen Belehrung behandelt werden.

Zum Prokurawiderruf bittet Frau Brösel um die unterschriebene Erklärung und die vorhandenen Zugangsnachweise. Sie will nicht allein die Personal-E-Mail von Frau Polter übernehmen. Der genaue Anmeldungstext wird nach Prüfung der Unterlagen vorgeschlagen.

Lenja erwähnt die österreichische Datei. Frau Brösel bittet, diese samt der gerichtlichen Nachricht mitzusenden; sie möchte erkennen, welcher Vorgang bereits eingegangen ist. Ein erneutes Absenden derselben Datei ohne Abstimmung solle vermieden werden.

Es wurde noch keine Einreichungsfreigabe erteilt. Der Termin steht unter dem Vorbehalt, dass Frau Yılmaz ihre Teilnahme bestätigt.''','01.10.2026'),
 D('20_Personenbogen_Aylin.docx','Persönliche Angaben für das Notariat',
 '''Name: Aylin Yılmaz. Geburtsdatum: 22.08.1986. Wohnort: Berlin. Beruf: Veranstaltungstechnikerin und künftig Geschäftsführerin. Staatsangehörigkeit: deutsch.

Die private Straßenanschrift wurde dem Notariat im gesonderten Identifizierungsbogen übermittelt und soll nicht ohne gesetzliche Notwendigkeit in die öffentliche Fassung übernommen werden. Eine Ausweiskopie ist diesem Arbeitsordner nicht beigefügt. Frau Yılmaz bringt das Identifizierungsmittel zum Termin mit.

Bestellung laut Beschluss: ab 01.10.2026. Annahmeerklärung:14.09.2026. Einzelvertretungsbefugnis: im Beschluss ausdrücklich erteilt. Eine Befreiung von §181BGB wurde nicht beschlossen.

Erklärung für die Vorbereitung: Mir ist kein Umstand bekannt, der meiner Bestellung entgegenstehen könnte. Die hierfür gesetzlich erforderliche Versicherung möchte ich nach der Belehrung im Notariat abgeben. Diese vorbereitende Angabe soll die formgerechte Erklärung nicht ersetzen.

Kontakt für Terminfragen: aylin@polter-technik.example. Frau Yılmaz ist am02.10.von10:30bis13:00Uhr erreichbar und kann persönlich erscheinen. Ein fremdes Signaturmittel soll nicht verwendet werden.''','01.10.2026'),
 D('21_Interne_Aufgabenansicht.png','Internes Aufgabenboard – Donnerstagmorgen',
 '''POLTER / Übergabe
01.10.2026, 10:04Uhr
Aylin: Bestellung abheute, Registereintrag offen.
Lenja: Bankänderung vorbereitet, noch nicht freigegeben.
Erna: technische Freigabe noch sichtbar; keine neue Zahlung angelegt.
Hieronymus: Signaturkarte liegt bei ihm, keine Weitergabe.
Fritzi: Termin morgen11Uhr reserviert.
Roter Kommentar von Hildegard: „Bitte nicht wieder nur eine Liste mit Fragen!“
Anhang: Gericht30September.pdf''','01.10.2026'),
 D('22_Notariatsvorschuss.pdf','Vorschussanforderung W-2026-204',
 '''Notariat Dr. Wendelin Wacker
An Polter Veranstaltungstechnik GmbH
Datum:01.10.2026. Vorgang: Geschäftsführerwechsel und Prokuraänderung, HRB219843B.

Für die Vorbereitung der beantragten notariellen Tätigkeit wird ein Vorschuss von450,00EUR angefordert. Die endgültige Kostenberechnung erfolgt nach dem tatsächlichen Gegenstand und Umfang der Tätigkeit nach dem GNotKG. In diesem Vorschuss ist keine Zusage enthalten, dass das Registergericht die Anmeldung an einem bestimmten Tag vollzieht.

Bitte geben Sie bei Zahlung den VorgangW-2026-204an. Die Bankverbindung erhalten Sie über den bereits vereinbarten sicheren Kommunikationsweg. Bei Unklarheiten zu den Zahlungsdaten kontaktieren Sie unser Büro unter der bekannten Rufnummer; Bankdatenänderungen werden nicht allein per unerwarteter E-Mail mitgeteilt.

Der Termin am02.10.2026um11:00Uhr ist vorgemerkt. Die abschließende Fassung der Anmeldung wird nach Eingang der noch bezeichneten Unterlagen abgestimmt.

Fritzi Brösel, Notariatsmitarbeiterin
buero@notariat-wacker.example''','01.10.2026'),
 E('23_Erna_Gespraechsangebot.eml','Ich möchte das ordentlich übergeben',
 '''Sehr geehrte Frau Dr. Abendroth,

ich will hier keinen Machtkampf. Die Nachricht von Frau Polter am15.September habe ich als interne Arbeitsanweisung verstanden. Den ausdrücklichen Widerruf von Herrn Knautsch habe ich am30.September gelesen. Den Umschlag hatte ich am29.mitgenommen, aber erst zu Hause in die Tasche gelegt und nicht geöffnet.

Bei Bühnenbolzen habe ich die Bestellung mit meiner Unterschrift zurückgeschickt, weil Herr Knautsch vorher den Preis freigegeben hatte. Mir ist klar, dass meine Gesamtprokura keine gewöhnliche Einzelprokura ist. Ich ging davon aus, dass seine Unterschrift nachgereicht wird. Die Lieferantin hat die Ware nach ihrer Nachricht nur reserviert. Geld habe ich nicht freigegeben.

Bitte sagen Sie mir, welche Erklärung ich für die Übergabe tatsächlich abgeben soll. Ich unterschreibe keine rückdatierte Empfangsbestätigung. Die Original-E-Mail und den Umschlag habe ich aufgehoben. Die Unterlagen können Sie heute Nachmittag abholen lassen.

Mit freundlichen Grüßen
Erna-Louise Zickzack''','2026-10-01T10:26:00+02:00','Erna-Louise Zickzack <erna@polter-technik.example>','Dr. Frieda Abendroth <frieda@abendroth-recht.example>'),
 E('24_Hildegard_Abschlusswunsch.eml','Bitte fertige Schreiben statt noch einer Runde',
 '''Liebe Frau Dr. Abendroth,

bitte machen Sie uns heute ein verständliches Blatt dazu, welcher Stand aus den Unterlagen folgt, und den Auftrag an Herrn Wacker. Die Frage mit dem Liefervertrag können Sie getrennt als offenen Punkt kennzeichnen, solange klar ist, wer jetzt gegenüber Bühnenbolzen handeln darf. Wir wollen keine ungeprüfte Bestätigung, dass alles schon im Register stehe.

Ich hatte tatsächlich gedacht, mein Schreiben an die Personalabteilung reiche aus. Wenn es dafür eine andere Erklärung braucht, soll diese ordentlich erfolgen. Bitte ändern Sie dabei nicht den Beschluss vom12.September rückwirkend. Aylin soll die Geschäftsführung heute übernehmen; eine §181-Befreiung hatten wir bewusst nicht beschlossen.

Die Bank braucht bis morgen16Uhr eine Rückmeldung. Sie muss nicht zwingend schon den neuen Registerauszug haben, verlangt aber eine nachvollziehbare Darstellung und die vorhandenen Belege. Bitte formulieren Sie auch diese Antwort so, dass wir sie nach Prüfung verwenden können.

Freundliche Grüße
Hildegard Polter''','2026-10-01T10:41:00+02:00','Hildegard Polter <hildegard@polter-technik.example>','Dr. Frieda Abendroth <frieda@abendroth-recht.example>')
 ]})
CASES.append({
 'slug':'handelsregister-assistent-nachtbrot-umzug','plugin':'handelsregister-assistent',
 'title':'Nachtbrot zieht um',
 'subtitle':'Eine neue Stadt, eine zu kurze Satzung und die alte Privatanschrift',
 'date':'01.10.2026','client':'Nachtbrot Automaten GmbH',
 'summary':'Nachtbrot will von Berlin nach Potsdam wechseln, die Firma verkürzen und ein zusätzliches Lager als Zweigniederlassung bezeichnen. Das Registergericht verlangt weitere Unterlagen, während die Buchhaltung bereits neue Briefköpfe benutzt. In der öffentlich abrufbaren Anmeldung steht außerdem eine private Anschrift, die dort nach Ansicht der Geschäftsführerin nichts zu suchen hat.',
 'assignment':'Ordnen Sie Sitz, Anschrift, Firma und geplante Niederlassung getrennt. Fertigen Sie die Antwort auf die gerichtlichen Schreiben, einen konkreten Ergänzungsauftrag an das Notariat und die benötigte Erklärung zum Austausch öffentlicher Daten. Berücksichtigen Sie Fristen und tatsächlichen Vollzugsstand, ohne etwas zu versenden.',
 'documents':[
 E('01_Anneliese_Ordner_weiter.eml','Nachtbrot: Umzug ist fertig, Register offenbar nicht',
 '''Sehr geehrter Herr Rechtsanwalt Morgenstern,

wir sitzen seit dem21.September in Potsdam. Die Automaten werden weiter aus Berlin betreut, und in Leipzig haben wir einen kleinen Lagerraum angemietet. Unser Designer hat bereits „Nachtbrot GmbH, Potsdam“ auf die Rechnungen geschrieben. Das Register zeigt aber nach meinem letzten Blick noch Berlin und den alten Namen.

Frau Wacker vom Notariat hat zwei Nachrichten des Gerichts weitergeleitet. Einmal fehlt wohl die ganze Satzung, einmal geht es um den Namen. Ich verstehe nicht, ob wir einfach Seiten nachreichen können oder noch einmal abstimmen müssen. Milan findet, die IHK habe die Firma doch schon vor Wochen freigegeben.

Außerdem steht in der veröffentlichten Anmeldung meine private Straßenanschrift mit meiner Unterschrift. Die Unterlage mit meinem Ausweis sollte nach meiner Erinnerung nur für das Notariat sein. Bitte kümmern Sie sich um eine saubere Fassung und sagen Sie konkret, was jetzt gebraucht wird. Ich möchte keine rückdatierten Unterlagen und keine zweite Anmeldung, die der ersten widerspricht.

Mit freundlichen Grüßen
Anneliese Flunder
Geschäftsführerin''','2026-10-01T08:34:00+02:00','Anneliese Flunder <anneliese@nachtbrot.example>','Kaspar Morgenstern <kaspar@morgenstern-recht.example>'),
 D('02_Register_Berlin_Arbeitsabschrift.pdf','Aktueller Ausdruck – in die Arbeitsakte übertragen',
 '''Amtsgericht Charlottenburg – HRB239681B
Firma: Nachtbrot Automaten GmbH. Sitz: Berlin. Geschäftsanschrift: Röstergasse17,12053Berlin. Stammkapital:25.000EUR.

Gegenstand: Betrieb, Vermietung und Wartung von Verkaufsautomaten für Backwaren und verpackte Lebensmittel sowie logistische Dienstleistungen im Zusammenhang mit diesem Betrieb, soweit keine besondere Erlaubnis erforderlich ist.

Geschäftsführerin: Anneliese Flunder, geboren am08.12.1981, Berlin, einzelvertretungsberechtigt. Die Gesellschaft wird bei mehreren Geschäftsführern durch zwei Geschäftsführer gemeinsam oder einen Geschäftsführer gemeinsam mit einem Prokuristen vertreten. Eine Prokura ist nicht eingetragen.

Letzte Eintragung:17.06.2023. Im chronologischen Verlauf ist zum Abrufzeitpunkt keine vollzogene Sitzverlegung vermerkt. In der Dokumentenansicht liegt eine Anmeldung vom11.09.2026. Im internen Abrufprotokoll wurde festgehalten, dass die Verlegungssache an das Gericht am Zielort weitergegeben wurde; eine neue Potsdamer Registernummer ist in dieser Arbeitskopie nicht ausgewiesen.

Abruf durch Büro Nachtbrot am30.09.2026,18:22Uhr. Die vorliegende Abschrift ist keine amtlich beglaubigte Ausfertigung.''','30.09.2026'),
 D('03_Mietvertrag_Potsdam.docx','Gewerberaummietvertrag – maßgebliche Vereinbarungen',
 '''1. Parteien und Mietgegenstand

Die Werkhöfe Havel GmbH vermietet an Nachtbrot Automaten GmbH die Büro- und Dispositionsräume im Gebäude2, Malzweg12,14473Potsdam. Die Räume umfassen ein Büro mit38Quadratmetern und einen Besprechungsraum mit22Quadratmetern. Ein eigener Produktionsbetrieb ist dort nicht vorgesehen.

2. Mietbeginn und Nutzung

Das Mietverhältnis beginnt am01.09.2026. Die Übergabe der Schlüssel erfolgt am18.09.2026. Die Mieterin nutzt die Räume für Geschäftsleitung, Disposition und Kundenbetreuung. Sie ist berechtigt, unter ihrer jeweils rechtmäßig geführten Firma ein Schild am Haupteingang und am Briefkasten anzubringen.

3. Postannahme

Der Empfang des Gewerbehofs nimmt an Werktagen von08:00bis17:00Uhr Post an. Die Mieterin teilt dem Empfang die zutreffende Firma und die Namen empfangsberechtigter Personen mit. Eine Zustellung unter einer nicht mitgeteilten abweichenden Firmierung kann die Vermieterin nicht gewährleisten. Der Briefkasten wird nicht durch die Vermieterin geleert.

4. Miete und Kaution

Die monatliche Nettomiete beträgt1.200EUR zuzüglich250EUR Betriebskostenvorauszahlung und gesetzlicher Umsatzsteuer. Die Kaution beträgt3.600EUR. Die erste reguläre Mietzahlung wurde am03.09.2026 veranlasst.

5. Keine Registervertretung

Die Vermieterin übernimmt keine Vertretung der Mieterin gegenüber Behörden oder Gerichten. Die Nutzung der Anschrift und die gesellschaftsrechtlichen Erklärungen bleiben Aufgabe der Mieterin.

Unterzeichnet laut Vertragsablage am20.08.2026 von Anneliese Flunder und Gisbert Havelmann.''','20.08.2026'),
 D('04_Postnotiz_Briefkasten.png','Interne Fototranskription des Briefkastens',
 '''Büroservice Werkhöfe Havel / 24.09.2026
Beschriftung oben: NACHTBROT GmbH
Klebezettel darunter: vormals Nachtbrot Automaten
Haus: Malzweg12, Gebäude2
Rückläufer im Fach: Bankpost vom22.09. an „Nachtbrot Automaten GmbH“
Handschrift Gisbert: „Empfang hatte nur neuen Namen. Bitte Firmenliste korrigieren.“
Anneliese: Schild vorerst beide Namen, Post annehmen.
Diese interne Arbeitsansicht enthält keine amtliche Zustellbestätigung.''','24.09.2026'),
 D('05_Gesellschafterbeschluss_Umzug.docx','Beschlussprotokoll vom05.09.2026',
 '''Nachtbrot Automaten GmbH
Gesellschafterversammlung in Berlin am05.09.2026,09:00Uhr.

Anwesend sind Ottilie Wursthorn mit einem Anteil im Nennbetrag von15.000EUR, Milan Petrović mit6.250EUR und Bao-Linh Sauter mit3.750EUR. Sämtliche Gesellschafter sind mit der Durchführung und der angekündigten Tagesordnung einverstanden.

1. Firma und Sitz

Die Firma soll in Nachtbrot GmbH geändert werden. Der Satzungssitz soll von Berlin nach Potsdam verlegt werden. Die entsprechende Änderung der Satzung soll notariell beurkundet und zur Eintragung angemeldet werden. Die Geschäftsanschrift soll ab tatsächlicher Aufnahme des Bürobetriebs Malzweg12,14473Potsdam, lauten.

2. Operative Standorte

Der Berliner Automatenservice wird weiter betrieben. Für Leipzig soll zunächst nur ein Lagerraum mit etwa40Quadratmetern angemietet werden. Eine eigene Leitung, ein eigener Kundenstamm oder eine selbständige Abrechnung am Leipziger Standort werden derzeit nicht eingerichtet. Über eine spätere organisatorische Erweiterung wird erneut beschlossen.

3. Kommunikation

Die neue Kurzbezeichnung darf in Entwürfen vorbereitet werden. Die Geschäftsführung soll vor der endgültigen Umstellung des rechtlichen Briefkopfs den Registervollzug prüfen. Die Marke und die Internetadresse „Nachtbrot“ sollen unverändert genutzt werden.

Die Beschlüsse wurden einstimmig gefasst. Dieses Protokoll dokumentiert die interne Beschlussfassung; der notarielle Termin zur Satzungsänderung ist für den11.09.2026 vorgesehen.''','05.09.2026'),
 D('06_Notarielle_Aenderung_Arbeitsabschrift.docx','Satzungsänderung – Arbeitsabschrift',
 '''Urkundenbezug: UVZ418/2026 des Notars Dr. Wendelin Wacker, Berlin, Termin11.09.2026. Für die Mandatsbearbeitung übertragene Fassung ohne Siegel und Unterschriftsabbildungen.

Die erschienenen Gesellschafter Ottilie Wursthorn, Milan Petrović und Bao-Linh Sauter vertreten das gesamte Stammkapital der Nachtbrot Automaten GmbH, Amtsgericht Charlottenburg, HRB239681B. Sie beschließen einstimmig die folgende Änderung des Gesellschaftsvertrags:

1. Firma

Paragraf1Absatz1des Gesellschaftsvertrags lautet künftig: „Die Gesellschaft führt die Firma Nachtbrot GmbH.“

2. Sitz

Paragraf1Absatz2des Gesellschaftsvertrags lautet künftig: „Sitz der Gesellschaft ist Potsdam.“

3. Übrige Bestimmungen

Die übrigen Bestimmungen des Gesellschaftsvertrags bleiben unverändert. Die Geschäftsführung wird gebeten, die Anmeldung vorzunehmen und den vollständigen Gesellschaftsvertrag in der erforderlichen bescheinigten Fassung einzureichen.

4. Kosten

Die Gesellschaft trägt die Kosten der Satzungsänderung und ihres Registervollzugs.

Die Notariatsablage enthält neben dieser Arbeitsabschrift eine Änderungsfassung und eine Datei mit dem Titel „Satzung_neu_Seiten1-2“. In dieser Akte liegt kein Vermerk vor, dass mit dieser letztgenannten Datei bereits der vollständige bescheinigte Satzungswortlaut übermittelt wurde.''','11.09.2026'),
 D('07_Satzung_neu_nur_Seiten1_2.docx','Gesellschaftsvertrag – zugesandte Kurzfassung',
 '''Dateiname aus der E-Mail: Satzung_neu_Seiten1-2.docx
Bearbeitungsdatum:12.09.2026,10:11Uhr. Bearbeitervermerk: Lenja, nach Telefonat mit Notariat.

1. Firma und Sitz

Die Gesellschaft führt die Firma Nachtbrot GmbH. Sitz der Gesellschaft ist Potsdam.

2. Gegenstand

Gegenstand ist der Betrieb, die Vermietung und Wartung von Verkaufsautomaten für Backwaren und verpackte Lebensmittel sowie die damit verbundenen logistischen Dienstleistungen, soweit keine besondere Erlaubnis erforderlich ist.

3. Stammkapital

Das Stammkapital beträgt25.000EUR. Es wird von den Gesellschaftern nach Maßgabe der zuletzt aufgenommenen Gesellschafterliste gehalten.

4. Hinweis aus der Bearbeitungsdatei

Ab Abschnitt4entspricht der Text der bisherigen Fassung. Die Seiten mit Geschäftsführung, Beschlussfassung, Verfügung über Geschäftsanteile, Einziehung und Schlussbestimmungen wurden in dieser Datei nicht erneut eingefügt. Die Bearbeiterin ging davon aus, dass die alten Seiten im Register bereits vorliegen.

Am Ende der Datei ist keine notarielle Bescheinigung enthalten. Die Datei wurde als Anlage der Sammelnachricht vom12.09.2026an das Notariat versandt.''','12.09.2026'),
 D('08_Alte_Satzung_vollstaendige_Abschrift.pdf','Gesellschaftsvertrag vom16.06.2023 – Arbeitsabschrift',
 '''1. Firma und Sitz
Die Gesellschaft führt die Firma Nachtbrot Automaten GmbH. Ihr Sitz ist Berlin.

2. Gegenstand
Gegenstand sind Betrieb, Vermietung und Wartung von Verkaufsautomaten für Backwaren und verpackte Lebensmittel sowie hiermit verbundene logistische Dienstleistungen, soweit keine besondere Erlaubnis erforderlich ist.

3. Kapital
Das Stammkapital beträgt25.000EUR. Ottilie Wursthorn hält Anteil1mit15.000EUR, Milan Petrović Anteil2mit6.250EUR und Bao-Linh Sauter Anteil3mit3.750EUR. Je ein Euro vermittelt eine Stimme.

4. Geschäftsführung
Ist nur ein Geschäftsführer bestellt, vertritt er allein. Bei mehreren Geschäftsführern vertreten zwei gemeinsam oder ein Geschäftsführer gemeinsam mit einem Prokuristen. Einzelvertretung und Befreiung von §181BGB können durch Gesellschafterbeschluss erteilt werden.

5. Beschlüsse
Beschlüsse werden mit einfacher Mehrheit gefasst, soweit Gesetz oder Satzung keine andere Mehrheit bestimmen. Satzungsänderungen bedürfen mindestens75Prozent der abgegebenen Stimmen. Eine Beschlussfassung in Textform setzt das Einverständnis sämtlicher Gesellschafter mit dieser Form voraus.

6. Anteilsverfügungen
Die Abtretung oder Belastung eines Geschäftsanteils bedarf der Zustimmung der Gesellschafterversammlung. Die Zustimmung ist in Textform zu dokumentieren. Gesetzliche Formanforderungen des Anteilsgeschäfts bleiben unberührt.

7. Einziehung
Die Einziehung mit Zustimmung des betroffenen Gesellschafters ist zulässig. Ohne Zustimmung ist sie nur unter den in der vollständigen notariellen Urschrift bezeichneten Voraussetzungen zulässig. Die hier übertragene Arbeitsabschrift verweist insoweit auf die gesondert beigefügte Klauselseite der Originalablage; diese Klauselseite liegt in dieser PDF-Arbeitskopie nicht vor.

8. Geschäftsjahr und Ergebnis
Geschäftsjahr ist das Kalenderjahr. Über die Verwendung des Ergebnisses beschließt die Gesellschafterversammlung nach Feststellung des Jahresabschlusses.

9. Bekanntmachungen und Kosten
Gesetzlich vorgeschriebene Bekanntmachungen erfolgen in den dafür vorgesehenen Medien. Die Gründungskosten trägt die Gesellschaft bis zu dem in der Urschrift bezeichneten Höchstbetrag.

Übertragungsvermerk: Diese als „vollständig“ benannte Bürodatei wurde am26.09.2026an die Kanzlei weitergegeben. Bei der Übertragung fiel der Verweis in Abschnitt7auf eine nicht beigefügte Klauselseite auf. Die notarielle Urschrift ist im Notariat verfügbar.''','26.09.2026'),
 D('09_Anmeldung_Arbeitsfassung.docx','Anmeldung vom11.09.2026 – Arbeitsfassung',
 '''An das Amtsgericht Charlottenburg – Registergericht
Nachtbrot Automaten GmbH, HRB239681B

Zur Eintragung wird die Änderung der Firma in Nachtbrot GmbH und die Verlegung des Sitzes nach Potsdam angemeldet. Die neue inländische Geschäftsanschrift lautet Malzweg12,14473Potsdam. Auf den notariellen Satzungsänderungsbeschluss vom11.09.2026,UVZ418/2026, wird Bezug genommen.

Die Anmeldung erfolgt durch die einzelvertretungsberechtigte Geschäftsführerin Anneliese Flunder, geboren am08.12.1981, wohnhaft in Berlin. In der vom Büro gespeicherten Ursprungsfassung folgt an dieser Stelle zusätzlich die private Straßenanschrift „Drosselhöfe27,12051Berlin“. Am Ende ist eine Abbildung der Unterschrift enthalten.

Beigefügt werden nach dem im Dokument enthaltenen Anlagenverzeichnis der Satzungsänderungsbeschluss und der Gesellschaftsvertrag in der neuen Fassung. Die vom Büro tatsächlich zugeordnete Satzungsdatei trägt den Namen „Satzung_neu_Seiten1-2.pdf“.

Im internen Verteiler ist als Verwendungszweck „Registervollzug“ eingetragen. Ein separater Vermerk zur Erstellung einer datensparsamen öffentlichen Abschrift findet sich in der übersandten Kopie nicht. Die rechtliche Form und die tatsächlich versandte notarielle Datei sind anhand des Notariatsausgangs zu prüfen.''','11.09.2026'),
 D('10_Versand_und_Weiterleitung.txt','Notariatsausgang und gerichtliche Weiterleitung',
 '''15.09.2026,09:24Uhr: Nachricht an Amtsgericht Charlottenburg übermittelt. Betreff: HRB239681B / Sitz und Firma.
Anlagen laut Ausgangsliste: Anmeldung11September.pdf; BeschlussUVZ418.pdf; Satzung_neu_Seiten1-2.pdf.
09:25Uhr: Technische Eingangsbestätigung vorhanden. Keine Eintragungsmitteilung.

18.09.2026: Gerichtlicher Vermerk im Büro eingegangen: Verlegungssache an das Amtsgericht Potsdam weitergegeben. Bezug bleibt HRB239681B des Amtsgerichts Charlottenburg. Eine neue Potsdamer Registernummer ist nicht mitgeteilt.

22.09.2026: Nachricht aus Potsdam mit Anforderung des vollständigen Satzungswortlauts.
24.09.2026: Weitere Nachricht zur beantragten Firma. Im Büro zunächst beide Nachrichten unter „Zwischenverfügung“ abgelegt.

29.09.2026: Fristverlängerungsbitte als Entwurf angelegt. Der Entwurf hat kein Versandprotokoll und keinen Eintrag in der Ausgangsliste. Milan hat die Datei am30.September mit „sieht gut aus“ kommentiert.''','30.09.2026'),
 D('11_Potsdam_Zwischenverfuegung.docx','Zwischenverfügung – Arbeitsabschrift',
 '''Amtsgericht Potsdam – Registergericht
Verlegungssache Nachtbrot Automaten GmbH, bisher Amtsgericht Charlottenburg, HRB239681B
Verfügung vom22.09.2026, bekanntgegeben am23.09.2026.

Der Anmeldung liegt kein vollständiger Wortlaut des Gesellschaftsvertrags mit der nach §54Absatz1GmbHG erforderlichen Bescheinigung bei. Die übermittelte Datei umfasst nur die Abschnitte1bis3und verweist für den übrigen Text auf frühere Unterlagen. Bitte reichen Sie den vollständigen und entsprechend bescheinigten Wortlaut ein.

Hierfür wird eine Frist bis zum07.10.2026bestimmt. Diese Verfügung betrifft zunächst den bezeichneten Unterlagenmangel. Die Prüfung der beantragten Firma am neuen Sitz bleibt vorbehalten.

Gegen diese Entscheidung ist die Beschwerde nach den gesetzlichen Vorschriften statthaft. Die Einzelheiten ergeben sich aus der dem elektronischen Original beigefügten Belehrung. In der vorliegenden Arbeitsabschrift ist die Belehrung nicht vollständig wiedergegeben; das Original befindet sich im Notariatsordner.

H. Krumme, Rechtspfleger
Für die Mandatsakte übertragen, ohne amtliche Beglaubigung.''','22.09.2026'),
 E('12_IHK_Berlin_alte_Auskunft.eml','Firmenvoranfrage Nachtbrot',
 '''Sehr geehrter Herr Petrović,

auf Grundlage Ihrer Anfrage zur Bezeichnung „Nachtbrot Automaten GmbH“ und dem angegebenen Sitz Berlin bestehen aus unserer Sicht derzeit keine ersichtlichen firmenrechtlichen Bedenken gegen diese Bezeichnung. Diese Einschätzung erfolgt auf Basis der mitgeteilten Angaben und ersetzt nicht die Entscheidung des zuständigen Registergerichts.

Sie erwähnten außerdem eine spätere Verkürzung auf „Nachtbrot GmbH“. Dazu liegt uns keine vollständige gesonderte Anfrage mit dem beabsichtigten neuen Sitz vor. Bitte beachten Sie, dass eine Sitzverlegung an einen anderen Ort eine erneute Betrachtung der dort vorhandenen Firmen erforderlich machen kann. Eine markenrechtliche Recherche ist nicht Bestandteil dieser Auskunft.

Mit freundlichen Grüßen
Gertrud Schnörkel
Firmenservice
firmen@kammer-berlin.example''','2026-08-18T10:05:00+02:00','Gertrud Schnörkel <firmen@kammer-berlin.example>','Milan Petrović <milan@nachtbrot.example>'),
 D('13_Potsdam_Firmenhinweis.docx','Gerichtlicher Hinweis zur Firma – Arbeitsabschrift',
 '''Amtsgericht Potsdam – Registergericht
Verlegungssache Nachtbrot Automaten GmbH, bisher HRB239681B des Amtsgerichts Charlottenburg
Schreiben vom24.09.2026, eingegangen am25.09.2026.

Bei der Prüfung der beantragten Firma „Nachtbrot GmbH“ ist die am Zielort bereits registrierte Firma „Nachtbrot Backwaren GmbH“ zu berücksichtigen. Nach vorläufiger Auffassung des Gerichts fehlt der beantragten Kurzfirma die erforderliche deutliche Unterscheidbarkeit. Die in der Akte befindliche Auskunft aus Berlin betrifft eine andere Firmenfassung und einen anderen Sitz.

Es wird Gelegenheit gegeben, hierzu bis zum09.10.2026Stellung zu nehmen. Sofern die beantragte Firma unverändert aufrechterhalten wird und keine weiteren Gesichtspunkte vorgetragen werden, beabsichtigt das Gericht, den entsprechenden Antrag abzulehnen. Eine abweichende Firma bedarf einer hierfür geeigneten gesellschaftsrechtlichen Grundlage; eine bloße Korrektur des Anschreibens genügt hierfür nicht.

Die Zwischenverfügung vom22.09.2026zum fehlenden vollständigen Satzungswortlaut bleibt hiervon unberührt. Dieses Schreiben ist ein Hinweis vor der angekündigten Entscheidung und enthält keine Aufforderung, den Antrag ohne weitere Prüfung zurückzunehmen.

H. Krumme, Rechtspfleger
Für die Arbeitsakte aus dem elektronischen Dokument übertragen.''','24.09.2026'),
 D('14_Chat_Name_und_Lager.txt','Chat der drei Gesellschafter',
 '''25.09.2026,19:12 – Milan: Die IHK hatte doch ja gesagt. Ich hänge die Mail noch mal an.
19:16 – Bao-Linh: Da steht Automaten und Berlin. Wir haben jetzt beides geändert.
19:18 – Ottilie: Dann heißen wir eben Nachtbrot Automatenlogistik GmbH. Hauptsache der Umzug ist nicht wieder blockiert.
19:20 – Milan: Bitte nicht vier Wörter auf dem Automaten. Die Marke bleibt Nachtbrot, oder?
19:23 – Bao-Linh: Marke und Firmenname sind nicht dasselbe. Auf dem Display kann weiter Nachtbrot stehen. Aber die Rechnungen müssen stimmen.
19:26 – Ottilie: Können wir den Sitz schon machen und den Namen später? Frage für Kaspar.
19:28 – Milan: Und Leipzig? Der Vermieter hat „Zweigniederlassung“ in die Übergabe geschrieben.
19:32 – Bao-Linh: Dort steht ein Regal und ein Ersatzautomat. Niemand arbeitet dort dauerhaft. Wir fakturieren alles aus Potsdam.
19:35 – Ottilie: Ich kann am2.Oktober um14Uhr zu einem Notartermin. Danach bin ich zehn Tage bei meiner Schwester.
19:38 – Milan: Ich kann per Video, falls das formal geht. Bitte keine spontane Zoom-Lösung, wenn die wieder Ärger macht.''','25.09.2026'),
 {'file':'15_Fristen_und_Aufgaben.xlsx','title':'Arbeitsplan Registerumzug','date':'30.09.2026','sheets':[{'name':'Fristen','headers':['Vorgang','Bekanntgabe','Gesetzter Termin','Status','Verantwortlich','Beleg'],'rows':[['Vollständige Satzung','23.09.2026','07.10.2026','offen','Notariat Wacker','Verfügung 22.09.'],['Firmenstellungnahme','25.09.2026','09.10.2026','offen','Kanzlei Morgenstern','Hinweis 24.09.'],['Verlängerungsbitte','', '06.10.2026','Entwurf nicht versandt','Lenja','kein Ausgang'],['Gesellschaftertermin','', '02.10.2026','Ottilie kann 14 Uhr','Milan','Chat 25.09.'],['Briefkopf korrigieren','', '01.10.2026','Designer informiert','Bao-Linh','Mail 30.09.']]},{'name':'Kosten','headers':['Position','Netto EUR','USt EUR','Gesamt EUR'],'rows':[['Designanpassung',180,34.2,'=B2+C2'],['Umzug Büro',960,182.4,'=B3+C3'],['Zusätzliche Beratung Budget',750,142.5,'=B4+C4'],['Summe','=SUM(B2:B4)','=SUM(C2:C4)','=SUM(D2:D4)']]}]},
 {'file':'16_Beteiligung_Beschlussplanung.xlsx','title':'Beteiligung und geplante Beschlussfassung','date':'30.09.2026','sheets':[{'name':'Kapital','headers':['Person','Anteil','Nennbetrag EUR','Quote','Erreichbarkeit'],'rows':[['Ottilie Wursthorn',1,15000,'=C2/25000','02.10. um 14 Uhr vor Ort'],['Milan Petrović',2,6250,'=C3/25000','auf Dienstreise'],['Bao-Linh Sauter',3,3750,'=C4/25000','vor Ort möglich'],['Summe','', '=SUM(C2:C4)','=SUM(D2:D4)','']],'formats':{'D':'0.00%'}},{'name':'Varianten','headers':['Bezeichnung','Nennung durch','Datum','Beschlossen?'],'rows':[['Nachtbrot GmbH','notarieller Beschluss','11.09.2026','ja'],['Nachtbrot Automatenlogistik GmbH','Ottilie im Chat','25.09.2026','nein'],['Nachtbrot Automaten GmbH','bestehende Firma','16.06.2023','bestehender Registerstand']]}]},
 D('17_Leipzig_Lagervertrag.docx','Nutzungsvertrag Lager Leipzig',
 '''1. Vertragsparteien und Fläche

Lagerhof Plagwitz Vermietung GmbH überlässt Nachtbrot Automaten GmbH ab 01.10.2026eine abgeschlossene Lagerfläche von42Quadratmetern in der Rampe9,04229Leipzig. Die Fläche dient der Aufbewahrung eines Ersatzautomaten, verpackter Ersatzteile und Werbematerialien.

2. Nutzung

Ein dauerhafter Arbeitsplatz, ein Verkauf an Endkunden und eine eigene Kundenannahme sind nicht vorgesehen. Anlieferungen erfolgen nach Abstimmung mit dem Lagerhof. Die Mieterin verfügt über einen eigenen Schlüssel und kann die Fläche werktags zwischen06:00und22:00Uhr betreten. Die Abrechnung mit ihren Kunden erfolgt nicht über den Lagerhof.

3. Miete

Die monatliche Nettomiete beträgt340EUR zuzüglich gesetzlicher Umsatzsteuer. Nebenkosten sind damit abgegolten. Der Vertrag ist mit einer Frist von drei Monaten zum Monatsende kündbar.

4. Anschrift und Außenauftritt

Im Übergabeformular des Vermieters ist das Feld „Zweigniederlassung des Mieters“ vorgedruckt. Die Parteien vereinbaren damit keine bestimmte gesellschafts- oder registerrechtliche Einordnung. Ein Firmenschild darf nach vorheriger Abstimmung angebracht werden; ein eigener Briefkasten ist bislang nicht bestellt.

5. Ansprechpartner

Für den Zugang vor Ort ist Mechthild Mumpitz vom Lagerhof zuständig. Auf Seiten der Mieterin koordiniert Bao-Linh Sauter die Anlieferungen. Eine Vollmacht zum Abschluss von Kundengeschäften wird mit diesem Mietvertrag nicht erteilt.''','19.09.2026'),
 E('18_Notariat_Satzung_Beschaffung.eml','Nachtbrot – vollständiger Text und weitere Firma',
 '''Sehr geehrter Herr Morgenstern,

wir haben die Ausgangsliste geprüft. Tatsächlich wurde die kurze Satzungsdatei statt des vollständigen bescheinigten Wortlauts zugeordnet. Die Urschrift der Satzung von2023und der Änderungsbeschluss liegen bei uns vor. Eine vollständige Fassung kann nach Abgleich erstellt werden; bitte senden Sie nicht selbst die im Mandantenordner als „vollständig“ bezeichnete Arbeitskopie ein, da auch diese einen ausgelagerten Abschnitt enthält.

Zur Firma benötigen wir eine klare Entscheidung der Gesellschafter. Eine neue Firmenvariante kann nicht allein durch die Bearbeitung des Begleitschreibens eingeführt werden. Ob die Sitzverlegung in der bestehenden Firma gesondert vollzogen werden soll, müsste anhand des Beschlusses und des gewünschten weiteren Vorgehens abgestimmt werden.

Die öffentliche Anmeldung enthält nach unserer ersten Sichtung die private Straßenanschrift und eine Unterschriftsabbildung. Wir können eine geeignete auszugsweise elektronische Abschrift prüfen. Bitte bezeichnen Sie, welche konkrete Fassung ausgetauscht werden soll und welche Daten betroffen sind. Das Original wird dadurch nicht vernichtet.

Mit freundlichen Grüßen
Fritzi Brösel
Notariat Dr. Wacker''','2026-09-30T15:42:00+02:00','Fritzi Brösel <buero@notariat-wacker.example>','Kaspar Morgenstern <kaspar@morgenstern-recht.example>'),
 D('19_Anneliese_Datenschutzerklaerung.docx','Erklärung zur veröffentlichten Anmeldung',
 '''An das bearbeitende Notariat und die beauftragte Kanzlei

Ich, Anneliese Flunder, habe am30.09.2026die öffentlich abrufbare Anmeldung vom11.09.2026gesehen. Darin stehen meine private Straßenanschrift Drosselhöfe27,12051Berlin, und die Abbildung meiner Unterschrift. Ich möchte, dass diese Angaben in der öffentlich zugänglichen Fassung entfernt werden, soweit ihre Veröffentlichung nicht gesetzlich erforderlich ist.

Soweit die öffentliche Bereitstellung dieser zusätzlichen Angaben auf meine Einwilligung gestützt werden sollte, widerrufe ich diese Einwilligung. Ich verlange keine Entfernung meines Namens oder anderer tatsächlich vorgeschriebener Registerangaben allein deshalb, weil sie mich identifizieren. Mir geht es um die bezeichnete Straßenanschrift und das Unterschriftsbild.

Bitte prüfen Sie eine ordnungsgemäße Ersatzfassung für den öffentlichen Registerordner. Ich bin damit einverstanden, dass die ursprüngliche Urkunde nach den gesetzlichen Vorschriften in der Registerakte aufbewahrt wird. Die vorliegende Erklärung ermächtigt nicht dazu, eine signierte Datei technisch zu verändern und anschließend als unverändert beglaubigt auszugeben.

Berlin/Potsdam,01.10.2026
Anneliese Flunder
Kontakt für Rückfragen: anneliese@nachtbrot.example''','01.10.2026'),
 D('20_Designer_Rechnung.pdf','Rechnung LUM-2026-77',
 '''Lumen & Lauge Gestaltung – Fridolin Funk
An Nachtbrot Automaten GmbH
Rechnungsdatum:28.09.2026. Leistungsdatum:23.09.2026.

Leistungsbeschreibung: Anpassung des digitalen Briefkopfs, der Rechnungsvorlage und zweier E-Mail-Signaturen auf die vom Auftraggeber mitgeteilte Bezeichnung „Nachtbrot GmbH“ sowie die Anschrift Malzweg12,14473Potsdam.

Nettohonorar:180,00EUR. Umsatzsteuer19Prozent:34,20EUR. Gesamtbetrag:214,20EUR.

Die Leistung umfasst keine firmen-, register- oder markenrechtliche Prüfung. Der Auftraggeber hat die Schreibweise am22.09.2026per E-Mail mitgeteilt. Eine weitere Korrektur auf eine abweichende rechtliche Firmierung kann innerhalb von14Tagen ohne zusätzliches Gestaltungshonorar vorgenommen werden, wenn nur die Textzeile ersetzt wird.

Zahlbar bis12.10.2026. Kontakt: fridolin@lumen-lauge.example.

Hinweis aus der Buchhaltung: Rechnung noch nicht bezahlt; Korrektur der Vorlage am30.09.angefragt.''','28.09.2026'),
 E('21_Designer_braucht_Firmierung.eml','Welche Zeile soll jetzt auf die Rechnungen?',
 '''Hallo Bao-Linh,

ich habe die neue Anschrift eingetragen, weil ihr geschrieben habt, der Umzug sei durch. Beim Firmennamen habe ich mich auf Milans Mail verlassen. Ich kann die Zeile heute zurückändern und bis zur endgültigen Rückmeldung wieder Nachtbrot Automaten GmbH verwenden. Bitte sagt mir ausdrücklich, welche rechtliche Firmierung und welcher Sitz derzeit angegeben werden sollen.

Die öffentliche Marke auf den Automaten und der Website ist davon in meiner Datei getrennt. Dafür muss ich nichts ändern. Bei den Rechnungen sind seit23.September insgesamt sechs Entwürfe mit der Kurzfirma erstellt worden. Drei wurden laut eurer Software schon versandt; die RechnungsnummernNB-260923-01bis03stehen in der angehängten Tabelle. Ich habe keine Rechnungen storniert oder neue verschickt.

Bitte lasst mich nicht selbst aus dem Register ableiten, was zulässig ist. Eine eindeutige Zeile genügt, dann setze ich sie um.

Viele Grüße
Fridolin''','2026-09-30T17:04:00+02:00','Fridolin Funk <fridolin@lumen-lauge.example>','Bao-Linh Sauter <bao@nachtbrot.example>'),
 {'file':'22_Rechnungsentwuerfe_September.csv','title':'Rechnungsjournal mit Briefkopfstand','headers':['Nummer','Datum','Kunde','Netto EUR','USt EUR','Brutto EUR','Briefkopf','Status'],'rows':[['NB-260923-01','23.09.2026','Werkraum Havel',460,87.4,547.4,'Nachtbrot GmbH Potsdam','versandt'],['NB-260923-02','23.09.2026','Bürohaus Kranich',380,72.2,452.2,'Nachtbrot GmbH Potsdam','versandt'],['NB-260923-03','23.09.2026','Atelier Zimt',220,41.8,261.8,'Nachtbrot GmbH Potsdam','versandt'],['NB-260925-04','25.09.2026','Bühnenhof Süd',590,112.1,702.1,'Nachtbrot GmbH Potsdam','Entwurf'],['NB-260928-05','28.09.2026','Gleiswerk Büro',310,58.9,368.9,'Nachtbrot GmbH Potsdam','Entwurf'],['NB-260929-06','29.09.2026','Werkhof Teich',270,51.3,321.3,'Nachtbrot GmbH Potsdam','Entwurf']]},
 D('23_Telefon_Gericht_Notiz.txt','Telefonvermerk vom01.10.2026',
 '''10:12bis10:20Uhr – Gespräch Kaspar Morgenstern mit Geschäftsstelle Registergericht Potsdam.

Die Geschäftsstelle bestätigt den Eingang der Verlegungssache und die beiden Schreiben vom22.und24.September. Eine Fristverlängerungsbitte ist nach Auskunft der Mitarbeiterin in der elektronischen Akte derzeit nicht ersichtlich. Die Mitarbeiterin erteilt keine Zusage über eine Fristverlängerung und verweist für einen Antrag auf eine konkrete schriftliche Begründung.

Zur Firma teilt sie mit, dass der Hinweis vom24.September keine erfolgte Ablehnung ist. Eine Entscheidung über eine abweichende Firma sei ohne entsprechende Unterlagen nicht vorbereitet. Sie äußert sich nicht dazu, ob die Sitzverlegung aus dem vorhandenen Beschluss isoliert vollzogen werden kann.

Zum Austausch der öffentlichen Anmeldung bittet sie um genaue Dokumentbezeichnung und eine geeignete Ersatzfassung. Ob der Antrag beim bisher führenden Registergericht oder im Zusammenhang mit der übergebenen Sache zu behandeln ist, müsse nach Eingang geklärt werden. Eine vollständige Löschung der Ursprungsurkunde wurde nicht zugesagt.

Gesprächspartnerin nannte ihren Nachnamen als Behrendt. Es wurde kein Akteninhalt telefonisch geändert.''','01.10.2026'),
 E('24_Bao_Linh_Entscheidungsvorbereitung.eml','Morgen können wir entscheiden, wenn der Text da ist',
 '''Sehr geehrter Herr Morgenstern,

Ottilie und ich können morgen beim Notar sein. Milan ist unterwegs und fragt, ob ein zulässiger Videoweg möglich ist oder eine andere Form seiner Mitwirkung gebraucht wird. Bitte lassen Sie das mit dem Notariat klären, bevor wir ihm irgendeinen Link schicken.

Wir brauchen eine klare Entscheidungsvorlage: entweder die Kurzfirma rechtlich weiterverfolgen oder eine andere Firmenfassung beschließen, gegebenenfalls den Sitzwechsel mit der bestehenden Firma vorziehen, wenn das auf der vorhandenen Grundlage möglich ist. Bitte schreiben Sie nicht schon in den Beschluss hinein, welche Variante wir gewählt hätten. Wir entscheiden erst nach Ihrer Rückmeldung.

Für Leipzig wollen wir zunächst nur das Lager nutzen. Niemand soll dort im Namen einer angeblich selbständigen Niederlassung Verträge schließen. Falls eine Anmeldung dafür derzeit gar nicht passt, möchten wir trotzdem eine kurze, verständliche Begründung und eine Liste der Tatsachen, die bei einer späteren Erweiterung neu zu prüfen wären.

Die Antwort ans Gericht soll die zwei unterschiedlichen Schreiben auseinanderhalten. Und bitte nehmen Sie Annelieses Privatanschrift nicht noch einmal in den Briefkopf auf.

Mit freundlichen Grüßen
Bao-Linh Sauter''','2026-10-01T10:58:00+02:00','Bao-Linh Sauter <bao@nachtbrot.example>','Kaspar Morgenstern <kaspar@morgenstern-recht.example>')
 ]})

# Typografische Normalisierung nur menschlicher Dokumenttexte; IDs, Dateinamen,
# Kontaktdatenfelder, Formeln und tabellarische Rohdaten bleiben unverändert.
import re as _re

def _lesetext(value):
    if not isinstance(value,str):
        return value
    value=_re.sub(r'(?<=[a-zäöüß])(?=\d)', ' ', value)
    value=_re.sub(r'(?<=\d)(?=[a-zäöüß])', ' ', value)
    value=_re.sub(r'(?<=\d\.)(?=[A-Za-zÄÖÜäöüß])', ' ', value)
    value=_re.sub(r'(?<=\d)(?=(?:EUR|Uhr|Prozent|Quadratmeter|Absatz|Abs\.|GmbHG|BGB))', ' ', value)
    value=_re.sub(r'\bHRB(?=\d)', 'HRB ', value)
    value=_re.sub(r'\bUVZ(?=\d)', 'UVZ ', value)
    value=_re.sub(r'§(?=\d)', '§ ', value)
    value=_re.sub(r'(?<=\d)bis(?=\d)', ' bis ', value)
    return value

for _case in CASES:
    for _document in _case['documents']:
        for _field in ('title','body'):
            if _field in _document:
                _document[_field]=_lesetext(_document[_field])

# Unabhängige Rechenproben: Beträge/Quoten und Änderungen eines Eingabewerts.
_RECHENPROBEN = {
 ('03_Anteile_alt_neu.xlsx','Liste_2024'): ({'D2':0.1,'D11':0.1}, {'input':'C2','value':5000,'output':'D2','expected':0.2}),
 ('03_Anteile_alt_neu.xlsx','Plan_nach_Kauf'): ({'D4':0.1,'D11':0.1}, {'input':'C4','value':1250,'output':'D4','expected':0.05}),
 ('03_Anteile_alt_neu.xlsx','Kaufpreis'): ({'B4':0}, {'input':'B3','value':79000,'output':'B4','expected':1000}),
 ('20_Dokumente_Colombo_Stand.xlsx','Kosten'): ({'D2':285.6,'D5':965.6}, {'input':'B4','value':100,'output':'D5','expected':985.6}),
 ('03_Gesellschafter_und_Stimmen.xlsx','Beteiligung'): ({'D2':0.6,'D3':0.4,'C4':50000,'D4':1}, {'input':'C2','value':25000,'output':'D2','expected':0.5}),
 ('15_Zeichnungsplan_verschiedene_Staende.xlsx','Zahlungsjournal'): ({'E2':45696,'E3':13708.8,'E4':177.19}, {'input':'C2','value':40000,'output':'E3','expected':14280}),
 ('15_Fristen_und_Aufgaben.xlsx','Kosten'): ({'D5':2249.1}, {'input':'B2','value':200,'output':'D5','expected':2269.1}),
 ('16_Beteiligung_Beschlussplanung.xlsx','Kapital'): ({'D2':0.6,'D3':0.25,'D4':0.15,'C5':25000,'D5':1}, {'input':'C3','value':5000,'output':'D3','expected':0.2}),
}
for _case in CASES:
 for _document in _case['documents']:
  for _sheet in _document.get('sheets',[]):
   _probe = _RECHENPROBEN.get((_document['file'],_sheet['name']))
   if _probe:
    _sheet['expected'],_change=_probe
    _sheet['perturbations']=[_change]
    if _sheet['name'] in ('Kosten','Kaufpreis','Zahlungsjournal'):
     _sheet['formats']={**_sheet.get('formats',{}),**{c:'#,##0.00' for c in ({'Kosten':['B','C','D'],'Kaufpreis':['B'],'Zahlungsjournal':['C','D','E']}[_sheet['name']])}}
