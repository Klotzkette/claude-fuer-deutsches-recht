"""Ausformulierte zusätzliche Rohbelege; keine rechtliche Musterlösung.

Der Kernstand vom 02.10.2026 bleibt erhalten. Neue Erkenntnisse enden am
08.10.2026. Dateinamen werden nur unter Nachtrag_2026-10-08 erzeugt.
"""
from textwrap import dedent

def doc(name, title, day, sender, recipient, body):
    return dict(file=name+'.docx', title=title, date=day, sender=sender,
                recipient=recipient, body=dedent(body).strip())

def mail(name, title, day, sender, recipient, body, attachments=()):
    return dict(file=name+'.eml', title=title, date=day, sender=sender,
                recipient=recipient, body=dedent(body).strip(), attachments=list(attachments))

BERLIN = dict(slug='gesellschafterstreit-klageerwiderung-berlin', label='Berlin',
    entry='Beginnen Sie mit N07 und N01. Vergleichen Sie die neue Gerätezuordnung mit dem alten Wareneingang und der Behauptung in der Klage. Für den kurzen Termin genügt anschließend N13; N02 bis N06 dienen der Vertiefung.',
    xlsx='N13_Belegabgleich_Lindenhof.xlsx',
    chat='N14_Buerochat_08_Oktober.txt',
    chat_body='''Bürochat Spreebogen, Export Ottilie Heller am 08.10.2026 um 11:46 Uhr. Zeitzone Berlin.

11:08 Kunigunde: Ich habe die sechs Geräte nun dreimal durchgezählt. Das löst die Rechnungsfrage offenbar nicht.
11:11 Tassilo: Bitte die Fotos vom Dienstag nicht als Zustand im August bezeichnen. L-427 war schon 2025 da.
11:14 Ottilie: Genau deshalb stehen in meiner Liste Bestand, Lieferschein und Zahlung getrennt.
11:20 Kunigunde: Kannst Du der Kanzlei noch den Umschlag geben? Morgen steht in deren Kalender etwas.
11:22 Ottilie: Umschlag geht heute mit dem Boten. Frau Pape erwartet ihn bis 15 Uhr. Einen Gerichtsausgang habe ich in unserem Büro nicht gesehen.
11:25 Tassilo: Ich bin ab morgen auf Montage. Montag um 16 Uhr könnte ich erklären, was am Dienstag geprüft wurde.
11:31 Kunigunde: Dann halte ich den Termin frei. Gottfried soll die fehlende Seriennummer nennen können, bevor wir ihm falsche Geräte zuschreiben.
11:39 Ottilie: Von einer neuen Abstimmung habe ich keinen Auftrag. Ich lasse das Protokoll vom September unverändert.
''', docs=[
doc('N01_Ergaenzung_Brandt','Ergänzende Erinnerung zum Lindenhof','06.10.2026','Tassilo Brandt\nWerkstattleiter der Spreebogen Lichtwerk GmbH','Dr. Adelbert Feuchtwanger\naf@feuchtwanger-recht.example','''
Sehr geehrter Herr Dr. Feuchtwanger,

Frau Rabenstein hat mir Ihre Fragen weitergeleitet. Ich möchte meine Nachricht vom 1. Oktober ergänzen, weil ich heute erstmals die Typenschilder auf der Bühne mit unserer Werkstattliste verglichen habe. Ich habe meine alte Nachricht nicht geändert. Bei dem schwarzen Transportkoffer am Freitag, 21. August, bleibe ich dabei: Ich habe beim Einladen geholfen, aber den Inhalt nicht gesehen.

## 1 Beobachtung am 6 Oktober

Herr Riedel hat mich um 08:40 Uhr in den Technikraum gelassen. Eingebaut waren L-402, L-407, L-411 und L-419 aus meinem Wareneingang vom 24. August sowie L-427 und L-433. Die Nummern standen auf den Gehäusen. Ich konnte nicht sehen, wann die beiden letzten Geräte dorthin gekommen waren. Herr Riedel legte danach einen Wartungszettel aus Februar 2025 vor. Dort steht L-427 bereits. Der Zettel zu L-433 nennt den 22. August 2026, ist aber erst am 25. August von ihm nachgetragen worden. Ich habe keine Prüfung vorgenommen, ob das Gehäuse und die Elektronik dieselbe Herkunft haben.

In meiner Mail vom 1. Oktober habe ich aus der Erinnerung von zwei weiterbenutzten Altgeräten gesprochen. Nach dem heutigen Abgleich kann ich das derzeit nur L-427 zuordnen. Die zweite Zuordnung war nicht anhand einer Seriennummer geprüft. Bitte übernehmen Sie meine frühere Zahl deshalb nicht ungeprüft als feststehende Herkunft beider Geräte.

## 2 Gespräch am 24 August

Ich kam gegen 08:15 Uhr ins Büro, um den Schlüssel für den Montagewagen zu holen. Frau Rabenstein fragte nach einer Freigabe. Herr Seidel antwortete ungefähr: Das Geld ist raus, die Geräte sind da, wir klären die Zettel später. Ich war nur wenige Minuten dabei. Die Frage, ob jemand vor der Überweisung telefoniert hatte, habe ich nicht gehört. Ich kann nicht bestätigen, dass Frau Rabenstein den Preis von 18.400 EUR am Telefon gebilligt oder abgelehnt hätte.

## 3 Mein Wareneingang

Die vier Geräte im Wareneingang habe ich selbst gezählt und geprüft. Mit meiner Unterschrift habe ich weder die Rechnung über sechs Geräte noch deren Preis freigegeben. Als Gottfried mir am 4. September sagte, ich solle die sechs Stück bestätigen, habe ich auf meine ursprüngliche Liste verwiesen. Das war ein kurzer Wortwechsel an meinem Arbeitsplatz; andere Beschäftigte standen nicht daneben. Ich habe dazu damals keine weitere Notiz geschrieben.

Bitte legen Sie mir einen späteren Text vor, wenn Sie meine Angaben darin verwenden. Ich möchte insbesondere nicht als Zeuge dafür benannt werden, dass zwei Geräte sicher niemals geliefert wurden. Für eine Besprechung bin ich am 12. Oktober ab 16 Uhr verfügbar.

Mit freundlichen Grüßen
Tassilo Brandt
'''),
doc('N02_Betriebsbuch_Riedel','Auszug aus dem Betriebsbuch Lindenhof','06.10.2026','Albrecht Riedel\nTechnische Betreuung Kulturhaus Lindenhof\nar@lindenhof-kultur.example','Spreebogen Lichtwerk GmbH','''
Sehr geehrte Frau Rabenstein,

ich übersende die von mir abgeschriebenen Einträge aus unserem gebundenen Betriebsbuch. Die Seiten haben wir heute gemeinsam mit Herrn Brandt angesehen. Ich habe hier die Texte und Nummern übernommen, keine neuen Lieferscheine angefertigt. Das Buch bleibt im Technikraum und kann nach Terminvereinbarung eingesehen werden.

## 1 Eintrag vom 17 Februar 2025

Unter der Überschrift Wartung Saallicht steht: Steuergerät L-427 weiter in Betrieb; zweites Altgerät L-398 als Reserve im Schrank, Ausgang 4 gelegentlich ohne Signal. Ich habe diesen Eintrag damals selbst geschrieben. Er betrifft zwei Geräte aus unserer vorhandenen Anlage und keine Rechnung aus August 2026. Für L-427 wurde am 6. Oktober 2026 dasselbe Typenschild abgelesen. Ob innere Bauteile zwischenzeitlich ausgetauscht wurden, weiß ich nicht.

## 2 Nachtrag vom 25 August 2026 zum Samstag

Der Eintrag lautet: Seidel kam Samstag gegen 11 Uhr mit schwarzem Koffer. Ein Gerät neben Steuerpult gestellt, Schild L-433. Zweite Kiste geschlossen. Abfahrt vor Mittagsprobe. Ich habe den Eintrag erst am Dienstag geschrieben, weil am Wochenende nur die Haustechnik besetzt war. Mit der zweiten Kiste kann ein Gerät, Werkzeug oder Zubehör gemeint gewesen sein; ich habe sie nicht geöffnet. Herr Seidel hat mir keinen Lieferschein zur Unterschrift gegeben. Ich habe ihm auch keinen Stückpreis bestätigt.

## 3 Abschluss der Arbeiten

Am 27. August habe ich nach der Lichtprobe vermerkt, dass die sechs benutzten Kreise funktionieren. Das war eine Funktionskontrolle für unseren Veranstaltungsbetrieb. Sie besagt nicht, dass sechs Geräte neu geliefert wurden. Bei der Wiedereröffnung am 29. August gab es keine Störung. Den Betrieb mit dem einen früheren Gerät hielt ich für selbstverständlich, weil ich keine Vereinbarung über den Austausch sämtlicher Geräte kannte.

Unsere Buchhaltung hat den Abschlag von 25.000 EUR am 18. August und den Rest von 12.000 EUR am 28. August an Spreebogen bezahlt. Diese Zahlungen beziehen sich auf unseren Gesamtauftrag. Wir haben die Rechnung der Einzelfirma Seidel nicht geprüft. Bitte verwenden Sie die Kundenzahlung nicht als meine Bestätigung ihrer einzelnen Positionen.

Albrecht Riedel
Übertragung am 06.10.2026, 10:25 Uhr; Originalbuch Seiten 38 und 61.
'''),
doc('N03_Seidel_Kalkulationsnachtrag','Nachgereichte Erläuterung meiner Rechnung','07.10.2026','Gottfried Seidel\nSeidel Bühnenservice e.K.\nrechnung@seidel-buehnenservice.example','Rechtsanwältin Walburga Fürst\npost@fuerst-recht.example','''
Liebe Frau Fürst,

bitte verwenden Sie die beigefügten Zahlen erst, wenn wir darüber gesprochen haben. Ich habe meine Kalendernotizen und den Materialordner durchgesehen. Nicht alles passt so zusammen, wie ich das in der ersten Woche aus der Erinnerung geschildert habe. An der tatsächlich ausgeführten Zahlung von 18.400 EUR ändert diese Zusammenstellung nichts.

## 1 Sechs Geräte in der Rechnung

Für vier Geräte mit den Nummern L-402, L-407, L-411 und L-419 liegt Tassilos Annahme vor. L-433 habe ich am Samstag zum Lindenhof gebracht. Beim sechsten Gerät muss ich nachsehen. Ich erinnere mich an einen Austausch der Platine eines schon vorhandenen Gehäuses. Wenn das L-427 gewesen sein sollte, muss die Formulierung sechs überholte Steuergeräte erläutert werden. Ich will jetzt nicht aus einer Erinnerung eine Seriennummer machen. Mein Preis von 1.950 EUR netto je Gerät ging von einem Austauschpaket aus; einen schriftlichen Auftrag mit dieser Beschreibung finde ich noch nicht.

## 2 Rechnungspositionen und erste Zahl

Die Endrechnung enthält 11.700 EUR für Geräte, 1.900 EUR für Kabel und Stecker, 1.000 EUR für Transport und Einbauunterstützung sowie 862,18 EUR für Expressbeschaffung und Zusatzarbeit. Die Nettosumme von 15.462,18 EUR ergibt mit 2.937,82 EUR Umsatzsteuer den bezahlten Betrag. Die erste Zahl von 14.900 EUR brutto war eine telefonische Kalkulation. Der Unterschied beträgt 3.500 EUR brutto; ich habe dafür keinen zeitgleichen durchgehenden Rechenbogen.

Vier zusätzliche Stunden zu je 90 EUR netto ergeben 360 EUR. Mein Kalendereintrag am 20. August lautet 18 bis 22 Uhr, Kabel und Prüfung. Die übrigen 502,18 EUR der Expressposition betreffen nach meiner Erinnerung Material und Beschaffung. Eine Fremdrechnung über genau diesen Restbetrag habe ich nicht gefunden. Das ist kein zusätzlicher Rechnungsbetrag neben den 862,18 EUR. Eine endgültige Gutschrift habe ich bisher nicht erstellt.

## 3 Was ich aufrechterhalte

Kunigunde wusste, dass ich meine Firma einschalte. Ob sie auch die endgültige Summe vor Zahlung kannte, kann ich aus dem Nachrichtenverlauf nicht beweisen. Ich habe den Hinweis um 07:31 Uhr nach meiner Erinnerung erst nach der Überweisung gelesen. Die Uhrzeit einer Ankunft auf dem Telefon beantwortet für mich noch nicht, wann ich die Nachricht geöffnet habe. Eine nachträgliche Gesellschafterfreigabe behaupte ich nicht.

Gottfried Seidel
Arbeitsnotiz für meine eigene Anwältin, 07.10.2026, 17:20 Uhr.
'''),
doc('N04_Heller_Post_und_Ablage','Nachtrag zum Posteingang und zur Gerichtsakte','08.10.2026','Ottilie Heller\nBuchhaltung Spreebogen Lichtwerk GmbH','Kanzlei Dr. Adelbert Feuchtwanger','''
Sehr geehrte Frau Pape,

den gelben Umschlag lege ich dem Boten heute bei. Auf der Vorderseite steht als Zustelltag der 25. September 2026. Ich habe das Datum am 25. September in unser Papierpostbuch übernommen. Beim späteren Scannen ist die Rückseite zuerst erfasst worden; auf der ersten Scan-Seite war das Datum deshalb nicht zu sehen. Das war der Grund für die Nachfrage, kein zweiter Zustellvorgang.

## 1 Inhalt und Weitergabe

Der Zusteller übergab mir das Paket am Empfang. Darin waren die Verfügung vom 24. September, die Klage vom 22. September und die Anlagen K1 bis K9. Das Papierpaket habe ich noch am selben Vormittag auf Frau Rabensteins Tisch gelegt. Sie war beim Kunden. Die Dateien wurden erst am 1. Oktober vollständig zusammengestellt und am 2. Oktober mit ihrem Auftrag an Ihre Kanzlei verschickt. Herr Seidel hat die Zustellung im Betrieb nicht entgegengenommen.

## 2 Was in unserem Kalender steht

Am 2. Oktober habe ich nach dem Telefonat mit Ihrer Kanzlei den 9. Oktober und den 23. Oktober als Wiedervorlagen übernommen. Daneben steht Verteidigungsanzeige beziehungsweise Klageerwiderung. Ich habe diese Daten nicht selbst rechtlich berechnet. Die gerichtliche Verfügung verlangt zwei Wochen nach Zustellung und anschließend weitere zwei Wochen. Eine Fristverlängerung oder ein Schreiben des Gerichts nach dem 24. September liegt in unserer Papierakte nicht. Die Daten im Firmenkalender ersetzen Ihren Fristenkalender nicht.

## 3 Stand heute 10 Uhr

Im Firmenpostausgang befindet sich kein Schriftsatz an das Gericht. Ob Ihre Kanzlei bereits aus dem anwaltlichen Postfach übermittelt hat, kann ich nicht sehen. Ich habe Frau Rabenstein deshalb um eine Rückmeldung gebeten. Ihre Bitte, keinen neuen Vorwurf ohne Beleg hinzuzufügen, ist den Beschäftigten weitergegeben worden. Eine Prozessvollmacht befindet sich noch in der Mappe zur Unterschrift. Der Entwurf lag gestern bei Frau Rabenstein; einen unterschriebenen Rücklauf habe ich bisher nicht gescannt.

Das Originalprotokoll vom 9. September bleibt unverändert. Ich habe meine Enthaltung bei der Abberufung erklärt, weil ich den Lieferumfang nicht einschätzen konnte. Das ist keine Aussage, dass ich den Einkauf vorher gebilligt hätte. Bitte halten Sie meine Rolle als Gesellschafterin und Versammlungsleiterin neben meiner Tätigkeit in der Buchhaltung sichtbar.

Mit freundlichen Grüßen
Ottilie Heller
'''),
doc('N05_IT_Nachrichtenexport','Sicherung des betrieblichen Nachrichtenverlaufs','05.10.2026','Erna Wendt\nWendt Büroservice\nit@wendt-buero.example','Kunigunde Rabenstein\nSpreebogen Lichtwerk GmbH','''
Sehr geehrte Frau Rabenstein,

auf Ihren Auftrag vom 2. Oktober habe ich den betrieblichen Kanal Lindenhof Einkauf im Nur-Lese-Modus exportiert. Der zuvor von Ihnen erstellte Textauszug wurde nicht überschrieben. Der neue Export betrifft denselben Zeitraum vom 19. bis 21. August und wurde im Ordner IT / Lindenhof / Export 2026-10-05 abgelegt. Ich beschreibe hier den Arbeitsumfang, damit die Kanzlei die Aussagekraft der Dateien einordnen kann.

## 1 Umfang der Sicherung

Die Nachrichten haben dieselbe Reihenfolge und denselben Wortlaut wie Ihre Datei 11_Nachrichten_K7.txt. Die Nachricht vom 19. August um 08:04 Uhr enthält nach Dann mach das unmittelbar die Bitte um endgültige Zahl, Preisabgleich, anderes Angebot und Nachfrage bei Ottilie. Im Export ist dies eine einzige Nachricht. Ein Absatz wurde nicht nachträglich ergänzt. Im sichtbaren Änderungsfeld ist für diese Nachricht kein Bearbeitungszeitpunkt verzeichnet. Das ist keine Untersuchung sämtlicher Sicherungskopien des Systems.

## 2 Zeitangaben

Das System speichert Ereignisse in UTC; für diese Zusammenstellung wurden zwei Stunden addiert. Der Eintrag vom 21. August, 07:31 Uhr Berliner Zeit, hat den Serverzeitpunkt 05:31 Uhr UTC. Er wurde technisch an das Nutzerkonto GS zugestellt. Eine belastbare Lesebestätigung liefert der bereitgestellte Export nicht. Ich habe weder Herrn Seidels privates Telefon ausgelesen noch dessen Benutzung beobachtet. Aus der Serverzustellung lässt sich daher nicht feststellen, ob er vor 07:43 Uhr den Text gelesen hatte.

## 3 Lücken

Telefonate, persönliche Besprechungen und E-Mails sind nicht Bestandteil dieses Kanals. Auch eine mögliche Zahlungsgenehmigung außerhalb des Kanals würde mit diesem Export nicht ausgeschlossen. Die Bankanwendung wurde nicht untersucht. Zwischen der Nachricht um 07:31 Uhr und der Antwort um 07:49 Uhr steht keine weitere Nachricht im untersuchten Kanal. Ein gelöschter Nachrichtentext wurde nicht wiederhergestellt.

Die Sicherungsdatei enthält betriebliche Daten weiterer Projekte nur in den Metadaten der Kanalbezeichnung; diese wurden in der übergebenen Ansicht weggelassen. Der vollständige Export ist erhalten. Für eine weitergehende Untersuchung benötige ich eine konkrete Bezeichnung der Geräte und einen gesonderten Auftrag. Ihre Frage, ob eine Zustimmung rechtlich ausreicht, kann ich als technische Dienstleisterin nicht beantworten.

Erna Wendt
'''),
doc('N06_Rabenstein_Stellungnahme','Meine Angaben für die Klageerwiderung','08.10.2026','Kunigunde Rabenstein\nGeschäftsführerin Spreebogen Lichtwerk GmbH','Dr. Adelbert Feuchtwanger\naf@feuchtwanger-recht.example','''
Sehr geehrter Herr Dr. Feuchtwanger,

die neuen Angaben von Herrn Riedel ändern meine Vermutung, dass nur vier Geräte im Projekt angekommen seien. Vier Geräte sind nach unserer Werkstattliste sicher eingegangen. Für ein weiteres gibt es nun Riedels Notiz. Beim letzten ist offenbar unklar, ob ein schon vorhandenes Gerät bearbeitet wurde. Bitte formulieren Sie unsere Darstellung entsprechend und schreiben Sie nicht, sämtliche Leistungen seien wertlos gewesen. Der Lindenhof hat funktioniert und bezahlt.

## 1 Nachricht und Telefonate

Mit Dann mach das wollte ich, dass Gottfried die Ersatzbeschaffung organisiert. Ich wollte nicht, dass er ohne endgültigen Preisvergleich an seine eigene Firma zahlt. Den vollständigen Satz habe ich in derselben Nachricht geschrieben. Am 20. August habe ich zweimal versucht, ihn zu erreichen. Ich finde in meiner Telefonliste ausgehende Anrufe um 09:08 Uhr und 12:26 Uhr; beide ohne Gesprächsdauer. Daraus kann ich nicht ausschließen, dass wir später über ein anderes Gerät gesprochen haben. An eine Zustimmung zu 18.400 EUR erinnere ich mich nicht.

## 2 Bedeutung für den Betrieb

Wir hatten im Januar 2025 die Freigaben gerade deshalb aufgeschrieben, weil wir beide bei Eile manchmal allein bestellten. Ich möchte keinen älteren Vorfall als bereits bewiesene Wiederholung verwenden. Den genauen Betrag einer früheren Bestellung weiß ich nicht mehr. Bei der Versammlung am 9. September ging es für mich um die aktuelle Eigenbeauftragung, die fehlende Freigabe und die trotz Rückfrage ausgeführte Zahlung. Mir war damals nicht bekannt, ob L-433 tatsächlich auf der Bühne stand.

## 3 Mein Auftrag heute

Bitte verteidigen Sie die Gesellschaft in dem bestehenden Verfahren. Ich wünsche keine Widerklage oder zusätzliche Zahlungsforderung, bevor Lieferumfang und Rechnung geprüft sind. Über eine technische Mitarbeit Gottfrieds können wir sprechen, ohne seinen Geschäftsführervertrag nebenbei als beendet zu behandeln. Das Septembergehalt ist bezahlt. Für Oktober ist die Abrechnung noch nicht freigegeben, weil die Buchhaltung nach der Zuständigkeit gefragt hat.

Ihre Mitarbeiterin hat mich auf die noch ausstehende Vollmacht angesprochen. Ich bringe die unterschriebene Fassung heute bis 14 Uhr vorbei. Soweit Sie für die Vertretung einen weiteren Gesellschaftsbeschluss benötigen, bitte ich um einen konkreten Entwurf. Diesen Absatz verstehe ich nicht als Ersatz für eine solche Entscheidung. Bitte bestätigen Sie mir gesondert den tatsächlichen Eingang der erforderlichen Anzeige beim Gericht; ein vorbereiteter Schriftsatz beruhigt mich bei der kurzen Frist noch nicht.

Mit freundlichen Grüßen
Kunigunde Rabenstein
''')], emails=[
mail('N07_Brandt_Nachreichung','Lindenhof: Nachtrag nach Besuch vor Ort','2026-10-06T13:18:00+02:00','Tassilo Brandt <tb@spreebogen-lichtwerk.example>','Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>','''Sehr geehrter Herr Dr. Feuchtwanger,

anbei mein heutiger Bericht. Ich war mit Herrn Riedel im Technikraum und habe die Nummern abgelesen. Das war erst heute und nicht am Einbautag. Bei einem Gerät gibt es einen alten Wartungseintrag; bei einem anderen einen später geschriebenen Eintrag über den Samstag. Ich kann deswegen meine Aussage nicht einfach in sechs Stück vollständig geliefert ändern.

Riedel sendet seine Abschrift selbst. Ich habe ihn nicht gebeten, eine bestimmte Formulierung zu verwenden. Die Zeit beim Montagsgespräch schätze ich aus dem Schlüsselholen für den Montagewagen. Eine genaue Gesprächsaufzeichnung besitze ich nicht.

Bitte melden Sie sich direkt bei mir, wenn etwas nicht verständlich ist. Ich möchte nicht mehrere abgestimmte Fassungen über die Werkstatt verteilen.

Viele Grüße
Tassilo Brandt''',('N01_Ergaenzung_Brandt.docx',)),
mail('N08_Riedel_Betriebsbuch','Ihre Rückfrage zu den Steuergeräten','2026-10-06T14:02:00+02:00','Albrecht Riedel <ar@lindenhof-kultur.example>','Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>','''Sehr geehrte Frau Rabenstein,

wie angekündigt sende ich die Abschrift aus unserem Betriebsbuch. Ich habe den Eintrag über den Samstag erst am Dienstag geschrieben. Das möchte ich ausdrücklich stehen lassen. Die Unterlage ist keine von uns unterschriebene Bestätigung einer Lieferung von sechs neuen Geräten.

Für den 13. Oktober kann ich Ihrer Kanzlei ab 09 Uhr die Papierseiten zeigen. Bitte kündigen Sie an, wer kommt. Ich kann nur zu den Vorgängen bei uns etwas sagen. Die Auseinandersetzung zwischen Ihren Gesellschaftern kenne ich nicht aus eigener Wahrnehmung.

Unsere Zahlungen über zusammen 37.000 EUR bezogen sich auf den Gesamtauftrag. Falls Sie hierfür noch einen Beleg brauchen, muss ich unsere Buchhaltung fragen; die Abschrift ist kein Bankauszug.

Mit freundlichen Grüßen
Albrecht Riedel''',('N02_Betriebsbuch_Riedel.pdf',)),
mail('N09_Gegenseite_Kalkulation','Seidel / Spreebogen: ergänzende Angaben zur Rechnung','2026-10-08T08:36:00+02:00','Walburga Fürst <post@fuerst-recht.example>','Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>','''Sehr geehrter Herr Kollege,

mein Mandant hat seine Kalkulation durchgesehen. Mit seinem Einverständnis übermittle ich seine Erläuterung vom 7. Oktober. Einzelne Erinnerungen, insbesondere zum sechsten Gerät, bedürfen noch der Prüfung. Aus dieser Offenlegung folgt weder eine Rücknahme der Klage noch die Anerkennung eines Rückzahlungsanspruchs. Eine Gutschrift ist nicht erteilt.

Bitte ermöglichen Sie meinem Mandanten Einsicht in die projektbezogenen Wareneingangsunterlagen und den vollständigen Nachrichtenexport. Hierfür schlage ich den 14. Oktober um 10 Uhr in Ihrer Kanzlei vor. Eine Weitergabe personenbezogener Lohnunterlagen ist nicht erforderlich. Die von ihm verwendeten privaten Kalendernotizen bringt er mit.

Eine Verlängerung gerichtlicher Fristen ist zwischen uns nicht vereinbart. Falls Sie gegenüber dem Gericht einen entsprechenden Antrag stellen, bitte ich um Nachricht.

Mit kollegialen Grüßen
Walburga Fürst, Rechtsanwältin''',('N03_Seidel_Kalkulationsnachtrag.pdf',)),
mail('N10_IT_Uebergabe','Lindenhof Nachrichtenexport vom 5. Oktober','2026-10-05T16:44:00+02:00','Erna Wendt <it@wendt-buero.example>','Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>','''Sehr geehrte Frau Rabenstein,

mein Bericht hängt an. Den vollständigen betrieblichen Export habe ich in Ihrer gesicherten Ablage abgelegt. In dieser Mail versende ich nur den Bericht; er benennt die Grenzen der Sicherung. Die Daten enthalten keine verlässliche Lesebestätigung für Herrn Seidels Gerät. Bitte leiten Sie nicht allein aus der Serverzeit ab, er müsse die Nachricht vor der Zahlung gesehen haben.

Ihre bisherige Textdatei entspricht im Wortlaut dem geprüften Zeitraum. Telefonate und andere Kanäle fehlen in beiden Ansichten. Für eine Bildschirmbesprechung mit der Kanzlei habe ich am 12. Oktober um 09:30 Uhr Zeit. Dafür benötige ich keine weiteren Kennwörter in einer E-Mail.

Freundliche Grüße
Erna Wendt''',('N05_IT_Nachrichtenexport.pdf',)),
mail('N11_Kanzleibuero_Unterlagen','32 O 187/26: Umschlag und Vollmacht heute','2026-10-08T10:14:00+02:00','Hedwig Pape <hp@feuchtwanger-recht.example>','Ottilie Heller <oh@spreebogen-lichtwerk.example>','''Sehr geehrte Frau Heller,

bitte lassen Sie uns den Originalumschlag und die unterschriebene Vollmacht heute bis 15 Uhr zukommen. Ihre ergänzende Posteingangsnotiz habe ich erhalten und füge sie zur eindeutigen Zuordnung dieser Nachricht bei. Unsere bisherige Wiedervorlage für die Verteidigungsanzeige lautet 9. Oktober. Die Sache ist Herrn Dr. Feuchtwanger heute vorgelegt.

Bitte bestätigen Sie keine Erledigung des Gerichtsausgangs gegenüber der Geschäftsführung, solange Sie die gesonderte Übermittlungsbestätigung der Kanzlei nicht haben. Diese Nachricht bestätigt nur den Unterlageneingang. Eine gerichtliche Fristverlängerung liegt uns nicht vor.

Die Erklärung von Herrn Brandt legen wir getrennt von Ihrem Bericht ab. Der Anwalt meldet sich zu noch offenen Fragen. Den Termin zur Belegsicht am 14. Oktober bestätigen wir erst nach Abstimmung.

Mit freundlichen Grüßen
Hedwig Pape, Rechtsanwaltsfachangestellte''',('N04_Heller_Post_und_Ablage.docx',)),
mail('N12_Rabenstein_Stand','Meine Angaben und die offenen Punkte','2026-10-08T11:05:00+02:00','Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>','Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>','''Sehr geehrter Herr Dr. Feuchtwanger,

anbei meine Stellungnahme. Ich habe die unsicheren Erinnerungen ausdrücklich so gelassen. Bitte machen Sie daraus keine feste Zusage eines Telefonats, an das ich mich nicht erinnere. Andererseits möchte ich auch nicht, dass mein halber Satz aus dem Chat als uneingeschränkte Preisfreigabe stehen bleibt.

Die neue Tabelle von Ottilie soll nur helfen, Rechnung, Geräte und Bankzahlung auseinanderzuhalten. Der dort errechnete Betrag für eine Rechnungsposition ist kein von mir beschlossener Rückforderungsbetrag. Mein Auftrag bleibt die Verteidigung der Gesellschaft.

Ich bin um 14 Uhr mit der Vollmacht in Ihrer Kanzlei. Bis dahin bitte ich Rückfragen auf diese Adresse zu senden; die Werkstatt braucht die Angaben nicht in einer Gruppenmail.

Mit freundlichen Grüßen
Kunigunde Rabenstein''',('N06_Rabenstein_Stellungnahme.docx',))])

MUENCHEN = dict(slug='gesellschafterstreit-shareholder-agreement-muenchen', label='München',
    entry='Beginnen Sie mit N07 und dem Gesprächsprotokoll N01. N02 ist ein neuer, weiterhin ungezeichneter Gründerentwurf. Mit N13 lassen sich Kapital, Aufgeld und Mehrheitswünsche abgleichen; die übrigen Belege vertiefen konkrete Vertragsfragen.',
    xlsx='N13_Kapital_und_Freigaben.xlsx', chat='N14_Chat_Lager_und_Vertretung.txt',
    chat_body='''Chat Hildegard Steinlechner / Quirin Rottmayer, Export am 08.10.2026 um 09:10 Uhr.

08:12 Quirin: Kessel braucht morgen das Layout. Das ist die schon bestellte Maschine, kein neuer Investitionsantrag.
08:17 Hildegard: Dann bitte trotzdem prüfen, ob die geänderte Steckdose Mehrkosten auslöst. Ottmar hat nur den alten Preis.
08:23 Quirin: Kein Aufpreis laut Kessels Mail. Das neue Ersatzteillager ist dagegen noch offen. Die 28.000 netto sind nicht bestellt.
08:28 Hildegard: Genau die zwei Dinge wirft Albrecht in seiner Liste zusammen. Kannst Du das im Gespräch erklären?
08:32 Quirin: Ja. Beim Pflegefall wollte ich sechs Monate Hilfe organisieren, nicht Deinen Anteil nach sechs Monaten kaufen.
08:36 Hildegard: Dann muss das im Entwurf auch so stehen. Den Buchwerttext unterschreibe ich nicht.
08:41 Quirin: Verstanden. Die Bewertungsfrage habe ich noch nicht gelöst. Bitte nicht als fertigen Vertrag herumreichen.
08:49 Hildegard: Kanzlei bekommt beide Stände. Albrecht soll seine Kundenkontakte beschreiben, ohne Umsatz zu versprechen.
''', docs=[
doc('N01_Gespraech_05_Oktober','Protokoll des Beteiligungsgesprächs','05.10.2026','Ottmar Fürst\nBuchhaltung Isarwinkel Gerätebau GmbH','Hildegard Steinlechner, Quirin Rottmayer und Albrecht Vogl','''
Das Gespräch fand am 5. Oktober von 14:00 bis 15:35 Uhr in der Werkstatt statt. Hildegard Steinlechner, Quirin Rottmayer und Albrecht Vogl waren anwesend. Ich habe Zahlen notiert und dieses Protokoll am Abend verschickt. Es wurde nicht gemeinsam unterschrieben. Die Teilnehmer sollten bis 8. Oktober Korrekturen melden. Die Kanzlei war nicht anwesend.

## 1 Einzahlung und Gegenleistung

Albrecht bestätigte, dass 200.000 EUR vollständig in die GmbH fließen sollen. Er verlangt dafür 20 Prozent nach Kapitalerhöhung. Die Gründer zeigten ihm die Rechnung mit 6.250 EUR neuem Nennbetrag und 193.750 EUR Aufgeld. Hildegard und Quirin sollen danach 48 beziehungsweise 32 Prozent halten. Es wurde weder Geld überwiesen noch eine Übernahmeerklärung abgegeben. Albrecht möchte persönlich zeichnen; eine Beteiligung über eine Gesellschaft verfolgt er derzeit nicht.

## 2 Entscheidungen im Betrieb

Albrecht möchte Kredite, Geschäfte mit Beteiligten und größere Ausgaben außerhalb des Budgets seiner Zustimmung unterwerfen. Er nannte 25.000 EUR netto je Vorhaben, Hildegard 50.000 EUR. Quirin fragte, ob zusammengehörige Bestellungen zusammengerechnet würden. Dazu gab es noch keinen Wortlaut. Beim Vorschlag einer Mehrheit von 85 Prozent sagte Hildegard, dann reichten ihre 48 und Quirins 32 Prozent zusammen nicht. Albrecht erklärte, das sei für diese besonderen Geschäfte beabsichtigt, nicht für jede Entscheidung.

## 3 Krankheit und Verkauf

Hildegard lehnte eine Anteilsabgabe allein wegen sechsmonatiger Pflege ihrer Mutter ab. Albrecht könnte eine Vertretungslösung akzeptieren, will jedoch regelmäßige Informationen über die Betriebsfähigkeit. Quirin möchte Familienübertragungen zulassen, solange die Kontrolle bei ihm bleibt. Albrecht befürchtet, dass dadurch fremde wirtschaftliche Interessen in die Gesellschaft gelangen. Eine Lösung wurde nicht beschlossen.

Beim Mitverkauf bestand Einigkeit nur über dieselbe wirtschaftliche Gegenleistung je Anteilseinheit. Hildegard widersprach einer unbegrenzten Haftung für alle Verkäufer. Albrecht hielt an einem noch zu verhandelnden Mindestpreis fest. Niemand erklärte, ab heute an einen Verkauf durch zwei Personen gebunden zu sein. Quirin soll seinen alten Entwurf mit diesen offenen Punkten an die Kanzlei geben.

## 4 Aufgaben und nächstes Gespräch

Ottmar soll die Kapitalrechnung und den Stand der bereits bezahlten Prüfstandanzahlung beifügen. Quirin klärt die Nutzung seiner Rottkern-Bibliothek und fragt Walburga Horn nach einem konkreten Zusatzangebot. Hildegard sendet das vollständige Paket an das Notariat. Für den 12. Oktober um 15 Uhr ist ein weiteres Gespräch vorgeschlagen. Die Reservierung am 22. Oktober bleibt vorbehaltlich der Entwurfsbearbeitung bestehen.

Ottmar Fürst, 05.10.2026, 18:10 Uhr
'''),
doc('N02_Quirin_Gegenentwurf','Überarbeitete Vorschläge für unsere Vereinbarung','07.10.2026','Quirin Rottmayer\nqr@isarwinkel-geraetebau.example','Hildegard Steinlechner und Kanzlei Dr. Mechthild Färber','''
Hildegard, ich habe die Punkte nach unserem Gespräch neu geschrieben. Das ist mein ungezeichneter Arbeitsstand, nicht Albrechts Zustimmung und noch keine Fassung für die Unterschrift. Ich möchte die Sätze der Kanzlei zeigen, damit sie sieht, was wir im Alltag brauchen. Die Regelung zur Reihenfolge von Satzung und privater Vereinbarung aus meinem alten Entwurf habe ich noch nicht durch einen fertigen Text ersetzt.

## 1 Entscheidungen und Bericht

Die Geschäftsführung darf im Rahmen eines von den Gesellschaftern genehmigten Jahresbudgets Bestellungen selbst freigeben. Für nicht im Budget enthaltene Vorhaben ab 50.000 EUR netto soll vorher eine Zustimmung eingeholt werden. Bestellungen für dasselbe Vorhaben sollen zusammengerechnet werden. Albrecht hat 25.000 EUR genannt; meine Zahl ist daher ausdrücklich noch nicht abgestimmt. Für laufende Materialkäufe aus fest angenommenen Kundenaufträgen möchte ich keine zweite Zustimmung verlangen, solange das Budget eingehalten wird.

Bis zum 15. des Folgemonats soll Albrecht eine Übersicht über Bankbestand, offene Kundenrechnungen und fällige Lieferantenrechnungen bekommen. Einzelne Lohnabrechnungen gehören für mich nicht in diesen Bericht. Für Geschäfte mit uns, unseren Angehörigen oder unseren anderen Unternehmen muss die Kanzlei einen gesonderten Entscheidungsweg entwerfen. Ich habe dafür noch keinen geeigneten Satz.

## 2 Ausfall eines Gründers

Bei längerer Krankheit oder Pflegezeit soll zunächst ein Vertreter für das Tagesgeschäft organisiert werden. Die betroffene Person soll ihren Anteil nicht allein wegen der Dauer der Abwesenheit verlieren. Nach sechs Monaten sollen die Beteiligten über die weitere Aufgabenverteilung sprechen. Eine automatische Kaufpflicht oder Kaufoption entsteht durch dieses Gespräch nicht. Meine frühere Formulierung zum Buchwert soll hierfür nicht verwendet werden.

## 3 Verkauf und Familie

Bei einem Verkauf an einen Dritten sollen alle für ihre Anteile denselben Preis je Nennbetrag erhalten. Garantien zum gesamten Unternehmen sollen nur diejenigen übernehmen, die den jeweiligen Sachverhalt kennen; eine Haftung für alles und jeden möchte ich nicht versprechen. Die erforderliche Mehrheit für eine Mitverkaufspflicht und Albrechts Mindestpreis sind offen. Hier darf kein unterschriftsreifer Zwang zum Verkauf aus meinem Text abgeleitet werden.

Eine Übertragung in meine vollständig kontrollierte Familiengesellschaft soll möglich sein, wenn keine fremde Person die Kontrolle übernimmt. Was bei meinem Tod, meiner Scheidung oder einer Verpfändung dieser Familiengesellschaft geschieht, ist noch zu ergänzen. Ich kann nicht allein beurteilen, welche dieser Regelungen in die Satzung müssen. Bitte besprechen Sie das mit dem Notariat, bevor wir den Vertrag per E-Mail freigeben.

Quirin, 07.10.2026, 21:05 Uhr
'''),
doc('N03_Ottmar_Zahlungsstand','Zahlungsstand und Prüfstandbestellung','08.10.2026','Ottmar Fürst\nBuchhaltung Isarwinkel Gerätebau GmbH','Hildegard Steinlechner und Quirin Rottmayer','''
Ich habe den Bankabruf vom 7. Oktober mit der Budgetnotiz vom 30. September abgeglichen. Bitte verwendet für das Gespräch mit Albrecht die folgenden Beträge. Die alten Kundenanzahlungen und die Prüfstandanzahlung sind bereits in unserem Anfangsbestand enthalten. Sie dürfen nicht ein zweites Mal als neue Bewegung angesetzt werden.

## 1 Konto vom 30 September bis 7 Oktober

Der bestätigte Anfangsbestand beträgt 86.200 EUR. Am 2. Oktober gingen 6.400 EUR Miete ab, am 5. Oktober 1.900 EUR Energieabschlag und am 6. Oktober 9.800 EUR an Materialkontor West. Zuletzt hat Molkerei Auenbach am 7. Oktober 5.474 EUR für den Ersatzteilauftrag IW-26055 bezahlt, bestehend aus 4.600 EUR netto und 874 EUR Umsatzsteuer. Der Bankabruf ergibt damit 73.574 EUR. Andere Bewegungen enthält dieser Abrufzeitraum nicht. Die Zahlung der Oktobergehälter steht noch bevor.

Die 9.800 EUR sind Teil der im September genannten offenen Materialrechnungen von 21.800 EUR. Daraus bleiben nach unserem Buchungsstand 12.000 EUR offen. Die Rechnungssumme ist keine neue zusätzliche Verpflichtung von 21.800 EUR neben dem bereits bezahlten Teil. Weitere laufende Ausgaben und Steuern werden erst nach dem nächsten Abgleich ergänzt. Die ungezogene Kreditlinie wird nicht als Geld auf dem Bankkonto ausgewiesen.

## 2 Prüfstand und Ersatzteillager

Der bestellte Prüfstand kostet 120.000 EUR netto und 142.800 EUR brutto. 35.700 EUR sind am 18. September abgeflossen. Die Restzahlung beträgt 107.100 EUR brutto. Kessel hat heute die Inbetriebnahme weiter für den 16. November vorgesehen. Die Schlussrate wird nach Rechnung und dokumentierter Inbetriebnahme fällig; ein früherer Zahlungstermin ist nicht bestätigt. Die Layoutfreigabe wird morgen benötigt, verursacht laut Kessel aber noch keine Zusatzkosten.

Quirins Ersatzteilwunsch über 28.000 EUR netto ist weiterhin nicht bestellt. Bei 19 Prozent Umsatzsteuer wären das 33.320 EUR brutto. Dieses neue Vorhaben ist von der bereits unterschriebenen Prüfstandbestellung zu unterscheiden. Ich habe beide Positionen deshalb getrennt in der Liste gelassen.

## 3 Kapitalaufnahme

Von Albrecht ist bis zum Abruf vom 7. Oktober kein Geld eingegangen. Seine 200.000 EUR bleiben ein Verhandlungsvorschlag. Nach der diskutierten Rechnung sollen 6.250 EUR dem Stammkapital und 193.750 EUR dem Aufgeld zugeordnet werden. Es ist keine Auszahlung an die Gründer vorgesehen. Ich benötige vor einer Buchung die endgültigen Unterlagen und den tatsächlichen Zahlungseingang.

Ottmar Fürst
'''),
doc('N04_Horn_Zusatzangebot','Angebot für ergänzende Softwarerechte','06.10.2026','Walburga Horn\nHorn Interfacegestaltung\nwh@horn-interface.example','Isarwinkel Gerätebau GmbH\nQuirin Rottmayer','''
Hallo Quirin,

nach unserem Telefonat schlage ich folgende Ergänzung zu meinem Angebot vom 4. Februar 2022 vor. Das ursprüngliche Honorar von 9.600 EUR netto bleibt davon unberührt. Bisher habe ich keine zusätzliche Vereinbarung unterschrieben. Dieses Schreiben ist bis 23. Oktober als mein Angebot gemeint; bitte lasst die genaue Fassung durch Eure Kanzlei prüfen.

## 1 Zusätzlicher Nutzungsumfang

Für die von mir im damaligen Projekt erstellten produktspezifischen Oberflächen der Reihe IW-2 biete ich Euch ein zeitlich unbeschränktes, weltweites Nutzungsrecht auch für Nachfolgemodelle derselben Adapterfamilie an. Die GmbH soll diese Teile bearbeiten, vervielfältigen, ausliefern und durch beauftragte Dienstleister warten lassen dürfen. Bei einem Verkauf des Geschäftsbetriebs möchte ich die Übertragung an den Erwerber zulassen. Ob ein Verkauf der Geschäftsanteile hierfür überhaupt eine gesonderte Übertragung erfordert, habe ich nicht geprüft.

## 2 Meine allgemeinen Bausteine

Die allgemeine Navigation und die von mir schon vor dem Auftrag verwendeten Dialogbausteine will ich weiterhin für andere Kunden einsetzen. Für diese Bestandteile biete ich ein nicht ausschließliches Recht zur Verwendung innerhalb Eurer Produkte an. Ich werde bis 12. Oktober eine Dateiliste liefern, die produktspezifische Teile, allgemeine Bausteine und von Dritten stammende Komponenten trennt. Für Quirins Rottkern kann ich keine Rechte erteilen. Eine Zusicherung, dass alle Programmteile ausschließlich der GmbH gehören, unterschreibe ich nicht.

## 3 Vergütung und Übergabe

Für die Erweiterung und die Dokumentation schlage ich einmalig 2.400 EUR netto zuzüglich 456 EUR Umsatzsteuer vor, insgesamt 2.856 EUR. Die Zahlung soll binnen 14 Tagen nach beiderseitiger Unterzeichnung und Übergabe der vereinbarten Dateiliste erfolgen. Vorher ist nichts fällig. Änderungen am Programm selbst sind in diesem Preis nicht enthalten; dafür würde ich ein gesondertes Angebot erstellen.

Bitte nennt mir den vorgesehenen Erwerberkreis und die Produkte, bevor Ihr dieses Schreiben als Anlage in eine Garantie packt. Ich möchte keine Verantwortung für Änderungen übernehmen, die andere nach meiner Übergabe vorgenommen haben. Über eine angemessene Haftungsregelung können wir sprechen. Euer bisheriges Nutzungsrecht an IW-2 stelle ich mit diesem Angebot nicht infrage.

Viele Grüße
Walburga Horn
'''),
doc('N05_Notariat_Unterlagen','Unterlagen für den reservierten Beurkundungstermin','07.10.2026','Notariat Dr. Fridolin Aichner\nRoswitha Kirchner\nrk@notariat-aichner.example','Isarwinkel Gerätebau GmbH\nKanzlei Dr. Mechthild Färber','''
Sehr geehrte Frau Steinlechner, sehr geehrte Frau Dr. Färber,

wir haben die Satzungsabschrift von 2021, die bisherige Gesellschafterliste und Herrn Vogls Eckpunkte erhalten. Die Reservierung für den 22. Oktober um 14 Uhr bleibt bestehen. Eine vollständige Entwurfsfassung oder verbindliche Terminbestätigung haben wir noch nicht versandt. Bitte reichen Sie die offenen Angaben möglichst gesammelt bis 14. Oktober ein, damit der weitere Ablauf abgestimmt werden kann.

## 1 Kapitalmaßnahme

Nach Ihrer Mitteilung ist eine Erhöhung des Stammkapitals von 25.000 EUR um 6.250 EUR auf 31.250 EUR vorgesehen. Herr Vogl soll den neuen Geschäftsanteil übernehmen und insgesamt 200.000 EUR leisten. Bitte bestätigen Sie, ob das Aufgeld von 193.750 EUR vollständig bei der Gesellschaft verbleiben soll und welche Zahlungstermine gewünscht werden. In den Unterlagen steht bislang kein Kaufpreis an die Altgesellschafter. Bitte veranlassen Sie noch keine Einzahlung unter einer von Ihnen selbst gewählten Bezeichnung; der konkrete Vollzugsablauf wird gesondert mitgeteilt.

## 2 Zusammenhängende Vereinbarungen

Bitte senden Sie neben dem Satzungsvorschlag auch sämtliche Nebenvereinbarungen mit. Uns liegen Hinweise auf Kaufoptionen, Mitverkaufsrechte und eine mögliche Pflicht zur Übertragung von Anteilen vor. Wir benötigen die tatsächlich vorgesehenen Fassungen einschließlich Anlagen. Ob eine Regelung nur intern gelten soll, ersetzt für die Entwurfsbearbeitung nicht die Prüfung ihres Zusammenhangs mit der Kapitalmaßnahme und möglichen Anteilsübertragungen. Die entsprechende Abstimmung erfolgt durch Herrn Dr. Aichner mit der beauftragten Kanzlei.

## 3 Beteiligte und Vertretung

Herr Vogl soll nach Ihrer jüngsten Nachricht persönlich handeln. Seine vollständigen persönlichen Angaben und die Angaben der bisherigen Gesellschafter werden über den gesonderten Übermittlungsweg aufgenommen. Bitte senden Sie keine Ausweiskopien im offenen Verteiler. Wenn jemand vertreten werden soll, teilen Sie Person und vorgesehene Vollmacht rechtzeitig mit. Ein automatisch gemeinsamer Auftrag zur Beratung sämtlicher persönlichen Interessen ergibt sich aus unserer Terminreservierung nicht.

## 4 Noch offener Entwurfsstand

Bei Mehrheiten und Zustimmungsvorbehalten nennen die bisherigen Texte unterschiedliche Beträge und Prozentwerte. Bitte kennzeichnen Sie die noch streitigen Varianten. Wir benötigen außerdem die vorgesehene Behandlung von Abwesenheit, Erbfall und Familienübertragungen. Eine von einem Gründer per E-Mail als gut bezeichnete Fassung werden wir ohne weitere Abstimmung nicht als vollständig freigegeben behandeln.

Mit freundlichen Grüßen
Roswitha Kirchner, Notariatsmitarbeiterin
'''),
doc('N06_Vogl_Anmerkungen','Meine Anmerkungen zum Beteiligungsgespräch','08.10.2026','Albrecht Vogl\nav@vogl-industrie.example','Hildegard Steinlechner und Quirin Rottmayer','''
Liebe Hildegard, lieber Quirin,

Ottmars Protokoll trifft den Verlauf überwiegend. Ich möchte die folgenden Punkte ergänzen, bevor jemand daraus eine Einigung macht. Mir geht es um einen überschaubaren Beteiligungsvertrag. Trotzdem müssen die Dinge, die für uns wirtschaftlich entscheidend sind, vor meiner Einzahlung feststehen.

## 1 Zustimmung und Budget

Für Geschäfte außerhalb des vereinbarten Budgets halte ich an 25.000 EUR netto je zusammengehörigem Vorhaben fest. Die 85 Prozent sollen nur für einen klar bezeichneten Katalog gelten. Mir ist bewusst, dass Eure geplanten 48 und 32 Prozent zusammen 80 Prozent ergeben. Ich möchte bei neuen großen Schulden und Geschäften mit Euren anderen Unternehmen mitentscheiden. Ersatzteile aus einem gemeinsam genehmigten Budget möchte ich nicht einzeln abzeichnen. Der bereits bestellte Prüfstand soll im ersten Budget ausdrücklich aufgeführt werden.

## 2 Geld und Anteil

Meine 200.000 EUR sollen gegen 20 Prozent nach Erhöhung in die Gesellschaft gehen. Die Aufteilung 6.250 EUR Stammkapital und 193.750 EUR Aufgeld ist mir vorgerechnet worden. Ich habe noch nicht überwiesen. Ich werde den Betrag erst nach abgestimmten Vertragsunterlagen und der Nachricht des Notariats zum Ablauf bereitstellen. Einen Nachschuss oder eine unbefristete Pflicht zur Rettung der Firma übernehme ich nicht. Meine Mitteilung ersetzt keine Bankbestätigung über frei verfügbare Mittel.

## 3 Verkauf und persönliche Haftung

Beim Mitverkauf will ich vermeiden, dass Ihr Eure Mehrheit verkauft und ich mit einem unbekannten Partner übrig bleibe. Für eine Pflicht, auch meine Anteile abzugeben, verlange ich einen nachvollziehbaren Mindestpreis und dieselben Zahlungsbedingungen. Meine Idee vom doppelten Einsatz ist noch kein vereinbarter Preis. Hildegards Einwand zu unbegrenzten Garantien verstehe ich. Ich kann mir eine Begrenzung vorstellen; für absichtlich falsche Angaben will ich allerdings keinen pauschalen Freibrief.

## 4 Kunden und Mitarbeit

Ich stelle Kontakte her, verspreche aber keine Aufträge. Molkerei Auenbach ist bereits Euer Kunde; deren laufende Zahlungen sind kein von mir vermittelter neuer Umsatz. Meine anderen Beteiligungen will ich vor Unterzeichnung offenlegen. Ein dreijähriges Verbot jeder Tätigkeit in der Branche kommt für mich nicht in Betracht. Kundendaten, die ich nur für dieses Projekt erhalte, behandle ich vertraulich. Auch dafür möchte ich eine klare gegenseitige Vereinbarung.

Bitte besprecht diese Punkte am 12. Oktober mit der Kanzlei. Ich lasse meine persönlichen Interessen zusätzlich selbst prüfen. Frau Dr. Färber ist nach meinem Verständnis von der GmbH beauftragt.

Herzliche Grüße
Albrecht
''')], emails=[
mail('N07_Ottmar_Protokoll','Montagsgespräch: bitte Korrekturen zum Protokoll','2026-10-05T18:22:00+02:00','Ottmar Fürst <of@isarwinkel-geraetebau.example>','Hildegard Steinlechner <hs@isarwinkel-geraetebau.example>, Quirin Rottmayer <qr@isarwinkel-geraetebau.example>, Albrecht Vogl <av@vogl-industrie.example>','''Guten Abend zusammen,

anbei mein Protokoll. Ich habe die offenen Zahlen und Formulierungen als offen stehen lassen. Wer bis Donnerstag nichts ergänzt, stimmt dadurch nicht automatisch einem Vertrag zu. Bitte sagt mir nur, wenn ich den Gesprächsverlauf falsch wiedergegeben habe.

Die Kapitalrechnung beruht auf der bisherigen Liste. Herr Vogl ist noch nicht als Gesellschafter erfasst. Die 200.000 EUR stehen deshalb auch nicht im Bankbestand. Für das Notariat brauchen wir eine abgestimmte Antwort, ob sämtliche Nebenabreden schon in derselben Runde mitgeprüft werden sollen.

Ich bereite bis Donnerstag den Zahlungsabgleich zum Prüfstand vor. Für die laufende Buchhaltung brauche ich inzwischen eine klare Freigabe der restlichen Materialrechnungen.

Viele Grüße
Ottmar''',('N01_Gespraech_05_Oktober.docx',)),
mail('N08_Hildegard_Entwurf','Quirins neuer Stand und meine Ergänzung','2026-10-08T08:16:00+02:00','Hildegard Steinlechner <hs@isarwinkel-geraetebau.example>','Dr. Mechthild Färber <mf@faerber-kanzlei.example>','''Sehr geehrte Frau Dr. Färber,

ich leite Quirins neuen Arbeitsstand weiter. Er ist gegenüber dem alten Text besser an unserem Gespräch orientiert, aber nicht von mir freigegeben. Insbesondere reicht mir ein Gespräch nach sechs Monaten Abwesenheit nur, wenn anschließend keine automatische Abgabe zum Buchwert versteckt ist. Ich möchte meine Pflegezeit organisieren können, ohne um den Anteil zu fürchten.

Bitte klären Sie auch die Mehrheitsbasis: Meint Albrecht 85 Prozent aller Anteile oder der tatsächlich abgegebenen Stimmen? Bei Enthaltung könnte das sonst anders laufen, als wir am Montag gedacht haben. Ich will erst den konkreten Text sehen.

Der Gesellschaftsauftrag bleibt bestehen. Meine persönlichen Interessen bespreche ich gesondert. Für morgen braucht Quirin eine betriebliche Layoutentscheidung zum bereits bestellten Prüfstand.

Mit freundlichen Grüßen
Hildegard Steinlechner''',('N02_Quirin_Gegenentwurf.docx',)),
mail('N09_Vogl_Position','Korrektur zu den offenen Verhandlungspunkten','2026-10-08T09:02:00+02:00','Albrecht Vogl <av@vogl-industrie.example>','Hildegard Steinlechner <hs@isarwinkel-geraetebau.example>, Quirin Rottmayer <qr@isarwinkel-geraetebau.example>','''Liebe Hildegard, lieber Quirin,

anbei meine Anmerkungen. Bei den besonderen Beschlüssen meinte ich zunächst 85 Prozent des gesamten Stammkapitals. Wenn die Kanzlei eine andere Grundlage vorschlägt, möchte ich deren Wirkung anhand unserer Anteile erklärt bekommen. Mein Schweigen zu Quirins alter Datei war keine Zustimmung.

Ich kann am 12. Oktober ab 15 Uhr teilnehmen. Zu den Bankunterlagen sende ich auf gesondertem Weg eine Bestätigung, sobald klar ist, welche Information tatsächlich gebraucht wird. Eine bloße Bildschirmansicht meines Kontos möchte ich nicht in der allgemeinen Runde verteilen.

Meine Kundenkontakte werde ich mit einer Liste der bestehenden Beziehungen beschreiben. Daraus ergibt sich kein garantierter Umsatz. Bitte macht auch aus dem angekündigten Geld noch keinen Eingang in der Liquiditätsplanung.

Herzliche Grüße
Albrecht''',('N06_Vogl_Anmerkungen.pdf',)),
mail('N10_Horn_Angebot','Zusätzliche Rechte IW-2: mein Angebot','2026-10-06T16:17:00+02:00','Walburga Horn <wh@horn-interface.example>','Quirin Rottmayer <qr@isarwinkel-geraetebau.example>','''Hallo Quirin,

anbei mein Angebot für die Erweiterung. Die Liste der Programmteile stelle ich bis Montag zusammen. Bitte unterschreibt nicht vorher eine pauschale Zusicherung, dass alle Bausteine ausschließlich Euch gehören. In meinem Angebot ist gerade zwischen produktspezifischen und allgemeinen Teilen unterschieden.

Ich kann Euch beim Gespräch am 12. Oktober ab 16 Uhr die Liste erklären. Dass Ihr einen Investor aufnehmt, stört mich nicht. Ich möchte nur wissen, welche zusätzlichen Produkte und welche Weitergabe künftig gemeint sind. Für Änderungen am Code selbst ist die angebotene Vergütung nicht kalkuliert.

Eine Rechnung über die 2.856 EUR brutto habe ich noch nicht gestellt. Der Betrag ist kein bereits fälliger offener Posten.

Viele Grüße
Walburga''',('N04_Horn_Zusatzangebot.pdf',)),
mail('N11_Bank_Stand','Beteiligungsänderung: Linie und Bürgschaften','2026-10-08T10:42:00+02:00','Ottokar Heller <oh@stadtbank-isartal.example>','Hildegard Steinlechner <hs@isarwinkel-geraetebau.example>','''Sehr geehrte Frau Steinlechner,

Ihre Nachricht zur geplanten Beteiligungsänderung ist eingegangen. Die Betriebsmittellinie von 80.000 EUR ist nach unserer Abfrage weiterhin nicht gezogen. Die aktuelle Vertragslage wird durch diese Mitteilung nicht geändert. Eine Zusage zur Entlassung von Ihnen oder Herrn Rottmayer aus den Bürgschaften über jeweils bis zu 40.000 EUR können wir heute nicht erteilen.

Bitte reichen Sie den endgültigen Beteiligungsstand und den unterschriebenen Vertragsstand nach. Die angekündigte Einzahlung von Herrn Vogl ist in unserer Betrachtung noch kein verfügbarer Kontobestand. Ottmars beigefügte Aufstellung haben wir zur Akte genommen; sie ist eine Zusammenstellung Ihrer Gesellschaft und keine von uns ausgestellte Bankbestätigung.

Für ein Gespräch zur Finanzierung der Novemberzahlung haben wir am 15. Oktober um 10 Uhr Zeit.

Freundliche Grüße
Ottokar Heller''',('N03_Ottmar_Zahlungsstand.pdf',)),
mail('N12_Notariat_Nachforderung','22. Oktober: fehlende Fassungen und Anlagen','2026-10-07T11:26:00+02:00','Roswitha Kirchner <rk@notariat-aichner.example>','Hildegard Steinlechner <hs@isarwinkel-geraetebau.example>, Dr. Mechthild Färber <mf@faerber-kanzlei.example>','''Sehr geehrte Frau Steinlechner, sehr geehrte Frau Dr. Färber,

anbei unser Schreiben zur weiteren Vorbereitung. Bitte senden Sie auch die noch nicht abgestimmten Nebenvereinbarungen und kennzeichnen Sie deren Stand. Wir benötigen nicht nur die Teile, die Sie selbst als beurkundungsbedürftig ansehen. Herr Dr. Aichner stimmt den Umfang der Urkunde mit der Kanzlei ab.

Die Reservierung am 22. Oktober ist derzeit noch keine Bestätigung, dass sämtliche Unterlagen rechtzeitig fertig werden. Wenn die wirtschaftlichen Punkte bis zum 14. Oktober offen bleiben, sprechen wir über den Termin. Eine Einzahlung sollte nicht allein aufgrund dieser Mail ausgelöst werden.

Für die persönlichen Daten nutzen Sie bitte den bereits getrennt zugesandten Übermittlungsweg. Ausweise gehören nicht in diesen Verteiler.

Mit freundlichen Grüßen
Roswitha Kirchner''',('N05_Notariat_Unterlagen.pdf',))])

ZINK = dict(slug='gesellschafterstreit-zink-und-zunder', label='Zink und Zunder',
    entry='Für den kurzen Einstieg N07 und N01 mit dem bisherigen Septemberbanklauf vergleichen. Danach N02 neben das unveränderte Versammlungsprotokoll legen. N03 und N04 liefern gegensätzliche Grenzen der Konkurrenzbehauptung; N13 hält Zahlungen und bloße Bewertungswünsche auseinander.',
    xlsx='N13_Zahlungen_und_Abfindungsannahmen.xlsx', chat='N14_Chat_Termin_und_Betrieb.txt',
    chat_body='''Gruppe Werkstattorganisation, Export Gundula Pfennig am 08.10.2026 um 10:05 Uhr.

09:04 Kunibert: Ich will morgen beim Notar endlich die Kapitalfrage erledigen.
09:09 Romy: Ich habe nichts zur Unterschrift freigegeben. Meine 60.000 stehen schon im Betrieb.
09:14 Gundula: Das Büro des Notars wartet auf eine abgestimmte Fassung. Ich habe nur den Termin vorgemerkt, keine Urkunde erhalten.
09:18 Thekla: Bitte keine neue Liste mit mir als einziger Gesellschafterin versenden. So wollte ich das nicht.
09:23 Kunibert: Dann müssen wir anders Geld finden. Die Maschinenrechnung kommt nächste Woche.
09:27 Gundula: Die steht mit 25.000 am 15. Oktober in der Liste. Die neuen Zahlungen bitte nicht mit dem Septemberlauf vermischen.
09:34 Romy: Für die Beratung brauche ich Deine Nachricht zur Rückzahlung vom 14. September vollständig.
09:41 Kunibert: Schicke ich. Ich hatte nach 30.000 gefragt, nicht nach der ganzen Summe.
09:47 Thekla: Können wir heute wenigstens entscheiden, wer mit dem Lieferanten telefoniert?
09:52 Gundula: Ich stelle die Rückfrage. Eine Stundung ist bisher nicht bestätigt.
''', docs=[
doc('N01_Gundula_Bank_und_OP','Fortschreibung der Bank und offenen Posten','08.10.2026','Gundula Pfennig\nKaufmännische Verwaltung\ngundula@zink-zunder.example','Geschäftsführung und Beirat Zink und Zunder','''
Ich habe den Septemberabschluss mit den Buchungen bis einschließlich 7. Oktober abgeglichen. Die Liste dient der Besprechung am 8. Oktober. Sie schreibt keine Bilanzwerte fort. Bei den strittigen Darlehen zeigt sie den Zahlungsstand, ohne über Genehmigungen oder Ansprüche zu entscheiden.

## 1 Bankbewegungen

Der Bankbestand zum 30. September beträgt 25.000 EUR. Am 1. Oktober gingen 3.200 EUR für die restliche Augustmiete ab. Am 2. Oktober wurden 12.000 EUR für den noch offenen Teil der Septemberlöhne ausgeführt. Am 5. Oktober zahlte Treppenhof 18.000 EUR auf den bestehenden Auftrag. Am 6. Oktober wurden 8.000 EUR an Stahlkontor Nord auf STA-0821 bezahlt. Daraus ergibt sich zum 7. Oktober ein Bankbestand von 19.800 EUR. Weitere Bewegungen enthält der abgerufene Zeitraum nicht.

Die Zahlung von Treppenhof wurde mit der Offenen-Posten-Liste des Kunden abgeglichen. Sie ist kein neuer Auftrag und keine Kapitaleinlage. Die Zahlung an Stahlkontor hat die Rechnung über 12.000 EUR teilweise ausgeglichen; verbleibend sind 4.000 EUR. In der bisherigen Septemberliste bleiben die tatsächlich im September erfolgten Buchungen unverändert. Die Rückzahlung an Kunibert von 30.000 EUR wird im Oktober nicht noch einmal abgezogen.

## 2 Offene Rechnungen aus der Septemberliste

Von den am 30. September bereits fälligen 50.000 EUR sind 23.200 EUR bezahlt. Offen bleiben aus dieser Liste 26.800 EUR: 4.000 EUR Stahlkontor, 2.800 EUR Steuerbüro, 1.600 EUR Energienachzahlung und 18.400 EUR Beschläge. Für die Beschläge wird eine Mängelprüfung verlangt, aber bisher keine Stundung bestätigt. Die Maschinenrechnung über 25.000 EUR zum 15. Oktober kommt zusätzlich hinzu. Die so fortgeschriebene alte Liste enthält 51.800 EUR. Neue Oktoberrechnungen sind darin nicht vollständig enthalten.

## 3 Darlehenskonten und unbestätigte Mittel

Romy hat weiterhin 60.000 EUR Hauptforderung im Darlehenskonto. Bei Kunibert stehen nach der Zahlung vom 15. September rechnerisch 10.000 EUR. Eine weitere Tilgung und eine Zinszahlung 2026 sind nicht gebucht. Die feste Zinszahlung von 1.800 EUR an Romy im Dezember 2025 gehört nicht zur Tilgung. Kuniberts vorgeschlagene neue Einzahlung von 80.000 EUR ist bis zum 7. Oktober nicht eingegangen.

Für Hannas Gesprächspreis gibt es weder einen Kaufvertrag noch eine Einzahlung. Auch eine Finanzierung möglicher Abfindungen hat sie nicht zugesagt. Bitte verwendet den Kontobestand und die alten offenen Posten nicht ohne Ergänzungen als vollständige Finanzplanung. Mir fehlen insbesondere die Oktoberfälligkeiten und eine bestätigte Auskunft zu verfügbaren zusätzlichen Mitteln.

Gundula Pfennig
'''),
doc('N02_Thekla_Erinnerung','Ergänzende Erinnerung an die Abstimmungen','05.10.2026','Thekla Spätzle\nthekla@zink-zunder.example','Clara Klee\nclara@klee-kolben.example','''
Sehr geehrte Frau Klee,

Romy hat mich gebeten, meine Erinnerung noch einmal aufzuschreiben. Ich weiß, dass Sie persönlich für Romy tätig sind. Ich erteile Ihnen damit keinen Auftrag und bitte Sie nicht, meine Interessen mitzuvertreten. Meine Notiz vom 25. September und das später versandte Protokoll sollen unverändert bleiben. Diese Ergänzung ist kein neu festgestelltes Beschlussergebnis.

## 1 Kapitalfrage

Kunibert sagte bei der Kapitalerhöhung sinngemäß, wer das Geld nicht mitbringen könne, dürfe den Rettungsversuch nicht aufhalten. Ich habe Romys Nein daraufhin nicht mitgerechnet. Sie hat nachdrücklich gesagt, sie verzichte auf nichts. Ich erinnere mich nicht daran, dass jemand eine schriftliche Verzichtserklärung vorgelegt hätte. Meine Zahl 32.500 bezog sich auf Kuniberts und meine Stimmen. Romys abgegebene 17.500 Nein-Stimmen standen daneben in meiner Mitschrift.

## 2 Abberufung und Einziehung

Bei Kuniberts Abberufung habe ich mich enthalten, weil ich die technischen Unterlagen nicht kannte. Bei der späteren Einziehung seines Anteils habe ich Ja gesagt. Ich wollte damals den Streit beenden, nicht eine schon berechnete Abfindung zusagen. Zwischen diesen Abstimmungen wurde keine neue Beteiligungsliste hergestellt. Bei den Anträgen gegen Romy verwendete ich weiter die ursprünglichen Nennbeträge. Sie hat ausdrücklich gesagt, das passe nicht zu meiner vorigen Feststellung über Kuniberts Anteil.

Ich habe Romys Nein bei ihrer Abberufung und Einziehung jeweils aufgeschrieben, aber nicht gezählt. Bei ihrer Abberufung habe ich selbst Nein gestimmt; die kaufmännischen Aufgaben mussten weitergehen. Bei der Einziehung habe ich Ja gestimmt, weil ich auf einen Verkauf an Hanna hoffte. Niemand hat mir dafür Geld zugesagt. Heute sehe ich, dass ich wirtschaftliche Erwartungen und einzelne Abstimmungen im Kopf vermischt habe.

## 3 Bekanntgabe und spätere Unterlagen

Ich habe die Ergebnisse jeweils im Raum ausgesprochen. Bei den Einziehungen und Romys Abberufung habe ich hinzugefügt, dass die Umsetzung geprüft werden müsse. Ob dieses Hinzufügen rechtlich etwas verändert, weiß ich nicht. Einen gemeinsamen Beschluss, alles vorläufig ruhen zu lassen, habe ich nicht ausgerufen. Beide haben mehrfach widersprochen. Das spätere Versenden des Protokolls sollte den Wortlaut festhalten, keine neue Abstimmung ersetzen.

Bitte lassen Sie mich einen Wortlaut gegenlesen, falls daraus eine Aussage für ein Verfahren wird. Ich will weder nachträglich Kuniberts Nein bei seiner Abberufung streichen noch Romys Nein bei der Kapitalfrage verschwinden lassen. Ich war selbst an den Entscheidungen beteiligt und kann keine neutrale Bewertung ihrer Wirksamkeit liefern.

Mit freundlichen Grüßen
Thekla Spätzle
'''),
doc('N03_Milena_USB_Nachtrag','Nachtrag zur freiwillig vorgelegten Dateikopie','06.10.2026','Milena Roth\nExterner IT-Service\nit@roth-service.example','Zink und Zunder Metallbau GmbH','''
Sehr geehrte Frau Yilmaz, sehr geehrter Herr Knopf,

Herr Knopf hat mir am 5. Oktober in Ihrer beider Anwesenheit einen USB-Datenträger gezeigt und zwei Dateien in ein gesondertes Übergabeverzeichnis kopieren lassen. Mein Auftrag bestand im Vergleich dieser Kopien mit dem gesicherten Serverbestand. Eine Durchsuchung privater Geräte und eine vollständige Untersuchung des Datenträgers waren nicht beauftragt. Ich habe keine Dateien gelöscht.

## 1 Vergleich der beiden Kopien

Die Dateien Fensterrahmen_ZZ_2025_v7.step und Kundenplan_Hofdurchfahrt_v1.dwg im Übergabeverzeichnis stimmen nach Bytevergleich mit den im September gesicherten Serverdateien überein. Damit ist nicht gesagt, dass keine weiteren Kopien oder bearbeiteten Fassungen existieren. Die bloße Vorlage dieser Dateien beweist auch nicht, dass gerade der vorgelegte Datenträger am 16. September angeschlossen war. Eine eindeutige gerätebezogene Seriennummer ist im damaligen Ereignisauszug nicht erfasst.

## 2 Angaben von Herrn Knopf

Herr Knopf erklärte, er habe den Datenträger für ein Gespräch über eine mögliche Fertigung außerhalb der Werkstatt vorbereitet. Er habe nach dem Streit nichts mehr damit gemacht. Diese Erklärung gebe ich als seine Aussage wieder; ich habe weder den Gesprächspartner befragt noch dessen Rechner gesehen. Im vorgelegten Übergabeverzeichnis fand ich keine andere CAD-Datei. Daraus lässt sich über weitere Ordner, Nachrichten oder Cloud-Speicher nichts ableiten.

## 3 Erhalt des Serverbestands

Die Serverdateien und der frühere Logauszug sind weiterhin vorhanden. Die Zugriffsrechte im Entwicklungsordner wurden im Rahmen dieses Auftrags nicht verändert. Die getrennte Ablage vom 22. September bleibt erhalten. Ich habe die aktuelle Übergabe mit Datum und den Beteiligten protokolliert, damit eine spätere Besprechung die beiden Sicherungsvorgänge unterscheiden kann.

Der Bytevergleich beantwortet keine Frage nach der Urheberschaft oder nach Nutzungsrechten. Zu dem externen Zeichner liegt mir noch kein Vertrag vor. Frau Alt hat mir keine Freigabe ihres Kundenplans mitgeteilt. Falls die Gesellschaft eine weitergehende Sicherung wünscht, sind Umfang, Zugang und Auftraggeber zuerst eindeutig festzulegen. Ich kann aus diesem beschränkten Vergleich weder eine Nutzung bei Fensterfuchs bestätigen noch sie ausschließen.

Mit freundlichen Grüßen
Milena Roth
'''),
doc('N04_Marta_Gespraechsnotiz','Unsere Anfrage zur Hofdurchfahrt','06.10.2026','Marta Alt\nAltbogen Projektbüro\nmarta@altbogen.example','Romy Yilmaz und Kunibert Knopf','''
Guten Tag Frau Yilmaz, guten Tag Herr Knopf,

nach zwei telefonischen Rückfragen möchte ich schriftlich festhalten, worüber wir gesprochen haben. Unser bestehender Treppenauftrag liegt bei Zink und Zunder. Die Zahlung vom 4. September über 28.000 EUR gehört zu diesem Auftrag. Für die Metallfenster an der Hofdurchfahrt haben wir bislang niemanden beauftragt und keinen Preis angenommen.

## 1 Ansprache Anfang September

Herr Knopf sprach mich am 8. September nach einem Baustellentermin an. Er sagte, er überlege, Sonderfenster künftig in einer kleineren eigenen Werkstatt anzubieten. Ich fragte, ob die bisherige GmbH dann weiter unser Ansprechpartner sei. Er antwortete, für die laufenden Arbeiten ändere sich zunächst nichts. Einen Namen für das neue Vorhaben habe ich an diesem Tag nicht notiert. Das Gespräch dauerte vielleicht zehn Minuten. Andere Personen waren nicht unmittelbar dabei.

Am 11. September schickte ich ihm die Zeichnung der Hofdurchfahrt auf seine betriebliche Adresse. Ich wollte eine technische Einschätzung, ob die Öffnung mit den vorhandenen Maßen gefertigt werden könnte. Am 16. September kam das Profil Fensterfuchs. Daraufhin schrieb ich am 18. September an Frau Yilmaz. Eine Preisofferte oder einen Vertragsentwurf habe ich von Fensterfuchs bis heute nicht erhalten.

## 2 Zeichnung und Termin

Die Zeichnung stammt aus unserem Planungsbüro. Unser Auftraggeber hat uns erlaubt, sie für die konkrete Angebotsanfrage zu verwenden. Eine allgemeine Freigabe für weitere Projekte oder Unternehmen haben wir Herrn Knopf nicht erteilt. Wer später fertigt, muss mit uns den benötigten Nutzungsumfang und die aktuelle Planfassung abstimmen. Inzwischen gibt es eine geänderte lichte Breite; die alte Datei allein reicht für ein endgültiges Angebot ohnehin nicht aus.

Wir brauchen bis zum 16. Oktober eine Auskunft, wer die Anfrage bearbeiten kann. Das ist unser Beschaffungstermin, keine gesetzte Frist für Ihren Gesellschafterstreit. Wenn Sie intern noch nicht entscheiden können, werden wir einen weiteren Metallbaubetrieb anfragen. Wir wollen keinen Beteiligten unterstützen oder einen Anteilskauf beeinflussen. Uns geht es um eine technisch belastbare Ausführung und eine eindeutige Vertragspartnerin.

Freundliche Grüße
Marta Alt
'''),
doc('N05_Hanna_Gespraech_06_Oktober','Notiz zum Erwerbsgespräch am 6 Oktober','06.10.2026','Hanna Blech\nBlechwerk Beteiligungen\nhanna@blechwerk.example','Romy Yilmaz, Kunibert Knopf und Thekla Spätzle','''
Guten Tag zusammen,

ich fasse unser Gespräch vom heutigen Vormittag zusammen, damit meine Preisvorstellung nicht für andere Zwecke verwendet wird. Ich bleibe grundsätzlich an der Werkstatt interessiert. Ein verbindliches Kaufangebot mache ich weiterhin nicht. Die offenen Streitigkeiten über Anteile und Geschäftsführung erschweren die Prüfung erheblich.

## 1 Preis und Darlehen

Die 150.000 EUR aus meinem Schreiben vom 3. September waren ein Ausgangspunkt für sämtliche Geschäftsanteile. Sie sind kein festgestellter Unternehmenswert und keine zugesagte Abfindungsfinanzierung. Die Darlehen müssen daneben behandelt werden. Ich habe im Gespräch verstanden, dass Romy weiterhin 60.000 EUR beansprucht und bei Kunibert nach einer Teilrückzahlung rechnerisch 10.000 EUR im Konto stehen. Die Wirksamkeit und Fälligkeit dieser Positionen habe ich nicht geprüft.

Romy verlangt mindestens 60.000 EUR für ihren Anteil zusätzlich zur gesonderten Behandlung ihres Darlehens. Kunibert möchte seinen verbleibenden Darlehensbetrag beim Vollzug erhalten. Thekla hat noch keine eigene Preisforderung genannt. Diese Wünsche ergeben nicht automatisch einen gemeinsamen Gesamtkaufpreis. Ich habe keine persönliche Schuldübernahme erklärt und werde vor einem Vertrag kein Geld zur Finanzierung des Streits überweisen.

## 2 Informationen für die Prüfung

Ich benötige aktuelle offene Posten, den vollständigen Darlehensstand, eine belastbare Auftragsübersicht und die Unterlagen zu den technischen Rechten. Die Augustbilanznotiz allein reicht mir nicht. Über die Verwendung der Kundendatei Altbogen möchte ich nicht anhand eines Dateinamens entscheiden. Bitte klären Sie außerdem, welche Personen bei einem möglichen Verkauf welche Erklärungen abgeben könnten.

## 3 Fortsetzung

Ich kann am 20. Oktober nochmals sprechen, wenn bis dahin eine geordnete Unterlage vorliegt. Exklusivität ist weiterhin nicht vereinbart. Für einen Kauf aller Anteile brauche ich einen abgestimmten Vertrag mit allen erforderlichen Beteiligten. Die in der Versammlung im September erklärte Verkaufszustimmung oder deren Ablehnung ersetzt aus meiner Sicht kein von mir und den Verkäufern unterschriebenes Geschäft; ich habe an dieser Versammlung nicht teilgenommen.

Bitte schicken Sie mir keine Personalakten oder privaten Bankunterlagen, die für die Prüfung nicht benötigt werden. Betriebswirtschaftliche Unterlagen sollen über einen gemeinsam benannten Ansprechpartner kommen. Ich möchte keine abweichenden Zahlenstände aus drei privaten Postfächern zusammenbauen müssen.

Mit freundlichen Grüßen
Hanna Blech
'''),
doc('N06_Samir_Bewertungsunterlagen','Unterlagen für eine mögliche Anteilsbewertung','08.10.2026','Samir Senf\nsamir@senf-beratung.example','Thekla Spätzle\nthekla@zink-zunder.example','''
Guten Tag Frau Spätzle,

Sie baten mich um eine Einschätzung, welche Unterlagen ein unabhängiger Bewerter benötigen würde. Ich kann die Unterlagenliste vorbereiten. Einen Abfindungswert berechne ich mit diesem Schreiben nicht. Die getrennte rechtliche Prüfung der umstrittenen Beschlüsse und der Zuständigkeit für eine Beauftragung wird dadurch nicht ersetzt.

## 1 Ausgangsunterlagen

Benötigt werden die vollständigen Abschlüsse und Kontennachweise der letzten drei Jahre, der aktuelle Buchungsstand, Forderungen und Verbindlichkeiten mit Fälligkeiten sowie eine erläuterte Auftrags- und Ergebnisplanung. Bei Vorräten und unfertigen Arbeiten müssen veraltete oder nicht mehr absetzbare Positionen erkennbar sein. Die Augustnotiz weist 7.000 EUR rechnerisches Eigenkapital aus. Daraus lässt sich der Verkehrswert eines Anteils nicht einfach ablesen. Dasselbe gilt für Hannas unverbindliche Preiszahl von 150.000 EUR.

## 2 Darlehen und Liquidität

Die Darlehenshauptforderungen von rechnerisch 60.000 EUR und 10.000 EUR sind getrennt von einem Anteilspreis zu zeigen. Rückzahlung, Zinsen und mögliche Einwendungen müssen anhand der Verträge und Zahlungsbelege behandelt werden. Die Auszahlung von 30.000 EUR an Kunibert am 15. September ist keine Aufwandsposition, die man ohne Weiteres noch einmal vom Septemberergebnis abziehen dürfte.

Die neue Bankliste zeigt 19.800 EUR zum 7. Oktober. Die fortgeschriebene alte OP-Liste allein ist keine vollständige Liquiditätsvorschau. Vor einer Zusage zu Raten brauchen wir sämtliche Fälligkeiten, erwartete Eingänge und belastbare Finanzierungen. Eine Abfindung in drei Jahresraten lässt eine fehlende Finanzierung nicht verschwinden. Hanna hat hierfür gerade keine Zahlung zugesagt.

## 3 Offene Grundlagen

Bitte fragen Sie zunächst, auf welchen Stichtag und für welchen konkreten Vorgang eine Bewertung benötigt wird. Ich möchte keinen Auftrag für einen bereits wirksam ausgeschiedenen Gesellschafter formulieren, solange gerade dieser Ausgangspunkt bestritten wird. Ein Bewerter benötigt auch die Information, ob und wie sich das Konkurrenzprojekt auf Aufträge und Erträge tatsächlich auswirkt. Ein bloßer Verdacht ersetzt keine bezifferte Auswirkung.

Ich habe außerdem die Beiratsordnung nachgesehen. Im nachgetragenen Ablagevermerk vom 23. September berichtet Frau Pfennig von der Wiederbestellung beider Mitglieder am 10. März 2026 für weitere drei Jahre. Die zugrunde liegende Niederschrift soll im Personalbüro liegen. Bitte nehmen Sie diese Niederschrift ebenfalls zu den übergebenen Unterlagen. In meiner eigenen Ablage finde ich bislang nur Einladungen zu späteren Gesprächen. Ich behaupte damit nicht, es habe keine Wiederbestellung gegeben. Aus dem bekannten Bestellungsvermerk folgt für mich auch keine Zustimmung zu einem bestimmten Darlehen oder zur Rückzahlung.

Mit freundlichen Grüßen
Samir Senf
''')], emails=[
mail('N07_Gundula_Zahlen','Oktoberstand: Septemberzahlungen nicht doppelt buchen','2026-10-08T08:22:00+02:00','Gundula Pfennig <gundula@zink-zunder.example>','Romy Yilmaz <romy@zink-zunder.example>, Kunibert Knopf <kunibert@zink-zunder.example>, Thekla Spätzle <thekla@zink-zunder.example>','''Guten Morgen zusammen,

anbei mein Abgleich bis einschließlich 7. Oktober. Der Septemberendbestand von 25.000 EUR ist die Ausgangszahl. Die Teilrückzahlung an Kunibert steckt bereits darin. Bitte zieht sie nicht noch einmal ab, wenn Ihr über die aktuellen Mittel sprecht.

Die 8.000 EUR an Stahlkontor sind nur eine Teilzahlung auf STA-0821. Die alte OP-Liste ist danach fortgeschrieben, aber noch nicht um alle Oktoberbelege ergänzt. Eine unterschriebene Stundungsvereinbarung habe ich weiterhin nicht. Zur Maschinenzahlung am 15. Oktober frage ich den Lieferanten gesondert an.

Die 80.000 EUR aus Kuniberts Kapitalvorschlag sind nicht eingegangen. Auch von Hanna liegt keine Finanzierungszusage vor. Ich brauche heute eine konkrete Zuständigkeit für die offenen Rückfragen.

Freundliche Grüße
Gundula Pfennig''',('N01_Gundula_Bank_und_OP.docx',)),
mail('N08_Thekla_Ergaenzung','Meine Erinnerung bitte zusätzlich ablegen','2026-10-05T15:09:00+02:00','Thekla Spätzle <thekla@zink-zunder.example>','Clara Klee <clara@klee-kolben.example>','''Sehr geehrte Frau Klee,

ich übersende die gewünschte Ergänzung. Bitte ersetzen Sie damit weder meine ursprüngliche Mitschrift noch das Protokoll. Ich kann mich an die ausgesprochenen Zahlen gut erinnern, habe aber die Folgen der aufeinanderfolgenden Abstimmungen nicht verstanden. Das möchte ich heute nicht nachträglich glätten.

Romy hat die neue Notiz noch nicht mit mir durchgesprochen. Ich habe sie allein geschrieben. Mir ist bewusst, dass Sie nur Romy vertreten. Falls ich meine eigene Beratung brauche, werde ich sie gesondert beauftragen.

Ich habe keine neue Gesellschafterliste freigegeben. Insbesondere habe ich nicht erklärt, nun alleinige Gesellschafterin zu sein. Bei einer weiteren Besprechung kann ich meine ursprünglichen handschriftlichen Notizen zeigen.

Mit freundlichen Grüßen
Thekla Spätzle''',('N02_Thekla_Erinnerung.docx',)),
mail('N09_Kunibert_USB','USB-Vergleich und meine Darstellung','2026-10-06T17:03:00+02:00','Kunibert Knopf <kunibert@zink-zunder.example>','Romy Yilmaz <romy@zink-zunder.example>','''Romy,

Milenas Bericht hängt an. Ich habe die Dateien freiwillig gezeigt, weil ich nichts verschwinden lassen will. Ich bestreite weiter, damit schon einen Auftrag von Altbogen übernommen zu haben. Über eine eigene Werkstatt habe ich gesprochen; ein unterschriebener Kundenvertrag existiert nicht. Dass die Kopien mit dem Server übereinstimmen, ist für mich nachvollziehbar.

Ich behaupte nicht, Milena hätte sämtliche privaten Geräte geprüft. Meine Aussage bleibt, dass ich die Kopien nicht weiter genutzt habe. Wenn Ihr eine weitere Untersuchung wollt, müssen Umfang und Auftrag vorher klar sein.

Die Unterlagen zum Darlehen schicke ich getrennt. Ich habe am 14. September um 30.000 EUR gebeten, weil ich eine private Anschaffung geplant hatte. Eine zusätzliche Zinszahlung habe ich nicht verlangt.

Kunibert''',('N03_Milena_USB_Nachtrag.pdf',)),
mail('N10_Altbogen_Klarstellung','Hofdurchfahrt: noch kein Auftrag und kein Preis','2026-10-06T12:18:00+02:00','Marta Alt <marta@altbogen.example>','Romy Yilmaz <romy@zink-zunder.example>, Kunibert Knopf <kunibert@zink-zunder.example>','''Guten Tag zusammen,

anbei meine Notiz. Bitte verstehen Sie unsere Anfrage nicht als bereits verlorenen Auftrag der GmbH oder schon gewonnenen Auftrag von Fensterfuchs. Wir haben bisher nur Informationen erbeten. Die Zahlung vom September gehört zum alten Treppenauftrag und nicht zu dieser neuen Anfrage.

Die Herkunft unserer Zeichnung und das Gespräch vom 8. September habe ich so genau aufgeschrieben, wie ich mich erinnern kann. Ich habe keinen Wortlaut mit Herrn Knopf oder Frau Yilmaz abgestimmt. Die neue Planfassung stellen wir bereit, sobald die Zuständigkeit feststeht.

Wenn bis zum 16. Oktober niemand verbindlich die Angebotserstellung übernimmt, müssen wir einen anderen Betrieb anfragen. Ich hoffe, wir können das ohne weitere Verwechslungen klären.

Freundliche Grüße
Marta Alt''',('N04_Marta_Gespraechsnotiz.pdf',)),
mail('N11_Hanna_Gespraech','Ergebnis unseres Gesprächs ohne Kaufzusage','2026-10-06T18:10:00+02:00','Hanna Blech <hanna@blechwerk.example>','Romy Yilmaz <romy@zink-zunder.example>, Kunibert Knopf <kunibert@zink-zunder.example>, Thekla Spätzle <thekla@zink-zunder.example>','''Guten Abend zusammen,

anbei meine Zusammenfassung. Ich habe verstanden, dass die Beteiligungsverhältnisse gerade streitig behandelt werden. Bitte leiten Sie aus meiner Gesprächsbereitschaft keine Bestätigung einer der vertretenen Positionen ab. Für eine Prüfung benötige ich eine nachvollziehbare Ausgangslage und vollständige Zahlen.

Insbesondere sind die 150.000 EUR weder eine verbindliche Kaufzusage noch ein Angebot, Abfindungen vorzufinanzieren. Ich werde auch die Darlehen nicht ohne gesonderte Vereinbarung übernehmen. Romys persönliche Preisforderung ist mir bekannt, aber noch nicht akzeptiert.

Den 20. Oktober halte ich als weiteren Gesprächstermin frei. Wenn die Unterlagen bis dahin nicht vorliegen, sollten wir den Termin verschieben. Exklusivität oder eine Pflicht zum Weiterverhandeln ist nicht vereinbart.

Mit freundlichen Grüßen
Hanna Blech''',('N05_Hanna_Gespraech_06_Oktober.docx',)),
mail('N12_Samir_Amtszeit','Bewertung und die ältere Beiratsbestellung','2026-10-08T09:41:00+02:00','Samir Senf <samir@senf-beratung.example>','Thekla Spätzle <thekla@zink-zunder.example>, Gundula Pfennig <gundula@zink-zunder.example>','''Guten Tag Frau Spätzle, guten Tag Frau Pfennig,

anbei meine Unterlagenliste. Der Ablagevermerk vom 23. September nennt die Wiederbestellung beider Beiratsmitglieder am 10. März 2026 für weitere drei Jahre. Bitte reichen Sie die dort bezeichnete Niederschrift aus dem Personalbüro nach. In meiner eigenen Ablage finde ich bislang nur Einladungen zu späteren Gesprächen. Ich stelle die berichtete Wiederbestellung damit nicht als unterblieben dar; ich möchte den zugrunde liegenden Beleg neben dem Vermerk haben.

Frau Mohn sucht ebenfalls in ihrer Ablage. Für die historische Darlehenszustimmung ist außerdem maßgeblich, welche konkrete Fassung wann vorlag. Ich habe die 30.000-EUR-Rückzahlung vor dem 15. September nicht in einer Unterlage gesehen; ob jemand anders Unterlagen hatte, kann ich nicht ausschließen.

Die aktuelle Anfrage beantworte ich als Zusammenstellung vorhandener Informationen. Eine nachträgliche Genehmigung oder eine Abfindungsbewertung liegt darin nicht.

Mit freundlichen Grüßen
Samir Senf''',('N06_Samir_Bewertungsunterlagen.pdf',))])

CASES = [BERLIN, MUENCHEN, ZINK]
