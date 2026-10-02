"""Einzeln ausgearbeitete Geschäftsdokumente zur Reinigungsvergabe GVB-REI-2026-017."""

GVB = ["GVB Gemeinsame Verkehrsbetriebe Berlin", "Anstalt des öffentlichen Rechts", "Zentraler Einkauf | Köpenicker Straße 186 | 10997 Berlin", "vergabestelle@gvb-berlin.example | Telefon 030 5550 1700"]
SPREE = ["Spreeklar Gebäudedienste GmbH", "Kundenservice Verkehr und Infrastruktur", "Wilhelminenhofstraße 76 | 12459 Berlin", "angebote@spreeklar.example | Telefon 030 5550 2810", "Geschäftsführer: Henrik Seidel"]
MARK = ["Märkischer Objektservice GmbH", "Vergabeteam | Ringbahnstraße 42 | 12099 Berlin", "vergabe@maerkischer-objektservice.example | Telefon 030 5550 3920", "Geschäftsführer: Nils Faber"]
NORD = ["Nordlicht Reinigung Berlin GmbH", "Betriebsleitung | Am Borsigturm 62 | 13507 Berlin", "kontakt@nordlicht-reinigung.example | Telefon 030 5550 4630", "Geschäftsführer: Daniel Lindner"]
DOCS = []

def document(number, slug, sender, recipient, date, title, paragraphs, signature):
    DOCS.append(dict(name=f"{number:02d}_{slug}", sender=sender, recipient=recipient,
                     date=date, title=title, paragraphs=paragraphs.strip().split("\n\n"), signature=signature))

document(1, "Bedarfsanmeldung", GVB, "An den Zentralen Einkauf und den Bereich Finanzen", "20.07.2026", "Reinigung von Verkehrsanlagen und Fahrzeugen ab Januar 2027", """
Sehr geehrter Herr Winter,

die gegenwärtigen Reinigungsverträge für das Teilnetz Südost enden am 31.12.2026. Bitte bereiten Sie die Anschlussvergabe vor. Die Betriebsleitung hat keinen Auftrag zur Verlängerung erteilt. Die Reinigung muss am 01.01.2027 um 04:00 Uhr ohne Lücke anlaufen. Schlüsselübergaben und Unterweisungen benötigen nach unserer Erfahrung sechs Wochen; der Dienstleister darf vor Beginn keine Reinigungsleistungen abrechnen, wohl aber nach Terminabsprache seine Objektleitung einweisen lassen.

Die GVB ist eine Anstalt des öffentlichen Rechts. Träger ist das Land Berlin. Unser Vorstand verantwortet U-Bahn, Straßenbahn und Busverkehr in Berlin. Der vorliegende Bedarf wird von der GVB selbst beschafft und bezahlt, nicht durch eine Tochtergesellschaft. Er betrifft betriebliche Verkehrsanlagen, Fahrzeuge und Räume für Fahr- und Betriebspersonal. Vermietete Ladenräume gehören nicht dazu. Das Erdgeschoss des Dienstgebäudes Adlergestell enthält eine extern vermietete Bäckerei; deren Verkaufs- und Küchenräume sind aus der Flächenliste herauszunehmen. Die vom Fahrpersonal benutzten Toiletten daneben verbleiben bei uns.

Wir schlagen drei Lose vor: Los 1 Stationen und Betriebsräume, Los 2 Fahrzeugreinigung, Los 3 Glasreinigung. Fahrzeuge dürfen nur an zugewiesenen Abstellorten und nach Übergabe durch unseren Betrieb bewegt oder betreten werden. Ein Reinigungsvertrag enthält keine Befugnis zum Rangieren. Für die Stationen ist nachts weniger Zeit verfügbar als in der früheren Ausschreibung. Die Feinabstimmung mit der Betriebsleitstelle läuft noch.

Die Leistung soll zunächst vier Jahre laufen. Ein weiteres Jahr soll einseitig abrufbar sein. Für Sonderreinigungen benötigen wir ein begrenztes Abrufbudget; Graffiti an Fahrzeugaußenseiten und die Entsorgung gefährlicher Stoffe wollen wir vorerst nicht mitvergeben. Bitte rechnen Sie nicht nur mit dem ersten Haushaltsjahr. Das beigefügte Kostenblatt enthält unsere Ansätze für alle Lose und für das optionale fünfte Jahr, jeweils ohne Umsatzsteuer.

Die Stationsreinigung ist zuletzt hauptsächlich wegen nicht erreichbarer Objektleiter und unklarer Zuständigkeiten zwischen Glas- und Unterhaltsreinigung aufgefallen. Wir brauchen eine erreichbare Einsatzleitung, nachvollziehbare Vertretungen und Leistungsnachweise je Objekt. Eine bestimmte Fabrikatsmarke für Reinigungsmittel ist nicht vorgegeben. Geruchsarme Mittel und die Verträglichkeit mit Naturstein sind wesentlich. Die Fachabteilung legt bis 22.07.2026 die vorhandenen Objektblätter vor.

Für den Standort Adlergestell muss der Einkauf noch klären, ob die an der Fassade eingetragene Glasfläche ein- oder beidseitig vermessen wurde. Ich möchte diesen Unterschied nicht stillschweigend als Sicherheitszuschlag im Preis verschwinden lassen. Die betriebliche Ansprechpartnerin ist Silke Mertens, Durchwahl 1714; Vertretung übernimmt Jens Ahrens, Durchwahl 1721.
""", "Mit freundlichen Grüßen\nSilke Mertens\nLeitung Reinigung und Stationsservice")

document(4, "Begehung_Betrieb", GVB, "Einkauf; Stationsservice; Arbeitssicherheit", "22.07.2026", "Begehungsprotokoll Stationen und Betriebshof", """
Teilnehmer: Silke Mertens, Jens Ahrens, Malte Winter und Mehmet Demir, Arbeitssicherheit. Beginn 09:10 Uhr am Dienstzugang Hermannstraße, Ende 12:35 Uhr am Betriebshof Adlergestell. Die Angaben ergänzen das Aufmaß vom 17.07.2026. Die Flächenzahlen sind keine zusichernde Vermessung.

1. Stationen

In Hermannstraße sind die maschinell zu reinigenden Bodenflächen ohne Bahnsteigkante aufgenommen. Die Bahnsteigkante bleibt Handarbeit mit gesichertem Arbeitsbereich. Zwischen 00:45 und 02:15 Uhr sind die Arbeiten Montag bis Donnerstag möglich. Am Freitag und Samstag läuft der Verkehr durch; dann sind nur abgesperrte Teilflächen zu bearbeiten. Nasse Flächen dürfen nicht bis zur Wiederaufnahme des Regelbetriebs ungesichert bleiben. Der Fahrerwechsel am Ausgang Süd wird auch nachts benutzt.

In Neukölln liegt am östlichen Treppenabgang eine beschädigte Fuge. Demir hat sie an den Bereich Instandhaltung gemeldet. Die Reinigung soll den Schaden weder beheben noch überdecken. In Treptower Park handelt es sich in dieser Akte ausschließlich um den GVB-Busbereich und das Personalgebäude, nicht um Anlagen eines anderen Verkehrsunternehmens. Müllbehälter fremder Betreiber sind nicht im Auftrag enthalten.

2. Räume und Schlüssel

Im Betriebshof Adlergestell stehen ein abschließbarer Geräteraum mit 14 m² und ein Ausgussbecken zur Verfügung. Es gibt keinen Lagerraum für große Chemikaliengebinde. Trinkwasser und Strom am Übergabepunkt stellt die GVB. Die Reinigungsfirma beschafft Geräte, Verbrauchsmaterial und persönliche Schutzausrüstung. Für den Schlüsselsatz werden zwei Empfänger benannt; jede Ausgabe wird von der Pforte quittiert. Ersatzschlüssel bleiben bei der GVB.

3. Abgrenzung Glas

Im Aufmaß ist die Südfassade des Dienstgebäudes mit 780 m² eingetragen. Mertens hat auf dem Papier daneben „zwei Seiten?“ notiert. Ahrens berichtet, dass der letzte Dienstleister 1560 m² je Durchgang berechnet hat. Ein Beleg dafür liegt bei der Begehung nicht vor. Die Fenster des Bäckereiladens sind im alten Plan farblich nicht abgegrenzt. Malte Winter nimmt die Rückfrage mit; die Zahl wird heute nicht verändert.

4. Störungen und Nachweis

Meldungen über ausgelaufene Getränke gehen über die Leitstelle an den Objektleiter. Körperflüssigkeiten erfordern geschultes Personal und gesonderte Ausrüstung. Der Betrieb stellt keine rund um die Uhr verfügbare Begleitung für Fremdpersonal. Verzögert eine Sperrung den Zugang, sind Ankunft, Freigabe und tatsächlich bearbeitete Fläche festzuhalten. Ein ausgefallener Einsatz darf nicht als vollständig durchgeführt unterschrieben werden.

Das Protokoll wurde um 15:40 Uhr an die Teilnehmer versandt. Demir ergänzt um 16:05 Uhr telefonisch: Unterweisung vor dem ersten Einsatz; keine Gleisquerung als Abkürzung.
""", "Aufgenommen: Jens Ahrens\nGegengelesen: Silke Mertens, 23.07.2026")

document(5, "Leistungsbeschreibung_Stand_23_07", GVB, "Vergabeunterlagen GVB-REI-2026-017 | Los 1", "23.07.2026", "Unterhaltsreinigung von Stationen und Betriebsräumen", """
1. Gegenstand und Leistungsgrenzen

Der Auftrag umfasst die in der Objektliste bezeichneten Verkehrsflächen, Personalräume und Sanitärräume. Die Objektliste nennt Flächen und Reinigungsdurchgänge je Jahr. Die Vertragsleistung ist das dort beschriebene Reinigungsergebnis, nicht allein die Anwesenheit einer bestimmten Zahl von Mitarbeitern. Fahrgäste, Fahrpersonal und Rettungswege dürfen nicht behindert werden. Gleisbereiche, private Verkaufsflächen und die Innenreinigung der Fahrzeuge sind nicht Bestandteil von Los 1.

2. Ausführung

Bodenflächen sind von losem Schmutz, klebrigen Rückständen und sichtbaren Laufspuren zu befreien. Maschinelle Nassreinigung ist nur bei geeigneter Bodenverträglichkeit und gesicherter Trocknung zulässig. Kanten und nicht zugängliche Ecken sind manuell zu bearbeiten. Abfallbehälter werden geleert, gereinigt und mit passenden Beuteln versehen; die getrennte Sammlung ist fortzuführen. Behälter mit Spritzen oder unbekannten Flüssigkeiten dürfen nicht mit der Hand nachsortiert werden.

Handläufe, Türdrücker und Bedienflächen sind nach Hygieneplan zu reinigen. Für Toiletten werden getrennte Arbeitsmittel eingesetzt. Verbrauchsmaterial ist täglich zu kontrollieren. Die GVB stellt das Papier und die Seife, der Auftragnehmer verteilt sie aus dem Objektlager. Fehlbestände sind vor Ende der Schicht zu melden. Duftspender sind nicht gefordert. Aufzüge bleiben während des Fahrgastbetriebs nutzbar; Sperrungen sind mit der Leitstelle abzustimmen.

3. Arbeitszeiten und Zugang

Regelfenster für zusammenhängende Nassreinigung in Stationen ist zunächst 00:30 bis 03:30 Uhr. Die abschließende Bestätigung der Betriebsleitstelle erfolgt durch eine für alle Bewerber veröffentlichte Ergänzung. Im Wochenendverkehr können nur Teilflächen gesperrt werden. Die betriebliche Einweisung, Schlüsselverwaltung und Wegezeiten sind in das Einsatzkonzept einzubeziehen. Die Unterkunft der Reinigungskräfte ist Sache des Auftragnehmers.

4. Kontrolle und Leistungsnachweis

Der Objektleiter dokumentiert täglich die bearbeiteten Bereiche, Ausfälle und Sonderereignisse. Monatlich findet eine gemeinsame Stichprobenbegehung an wechselnden Objekten statt. Festgestellte Mängel werden mit Ort, Uhrzeit und Bildbeleg beschrieben und dem Auftragnehmer mitgeteilt. Dieser bestätigt die Kenntnisnahme und nennt einen Behebungstermin. Abzüge setzen die Feststellung der betroffenen Leistung und die vertraglich vereinbarte Behandlung voraus; eine bloße Beschwerdezahl ersetzt keinen Nachweis.

5. Sonderbedarf und Schnittstellen

Sonderreinigungen werden schriftlich durch die benannte GVB-Einsatzleitung abgerufen, im Eilfall telefonisch mit anschließender Bestätigung. Die Preisblattpositionen begründen keine Mindestabnahme. Glasflächen gehören zum gesonderten Los 3; Spiegel in Sanitärräumen gehören zu Los 1. Bei Unklarheiten wird die Stelle fotografiert und gemeldet. Eine doppelte Abrechnung derselben Fläche ist nicht vorgesehen.

6. Angebotsunterlagen

Einzureichen sind das ausgefüllte Preisblatt sowie ein objektbezogenes Einsatz- und Qualitätssicherungskonzept mit Vertretung, Störungsannahme und Übergabe zum Vertragsbeginn. Eigene Produktnamen dürfen benannt werden, werden aber nicht allein wegen ihrer Marke bevorzugt. Das Konzept darf den in der veröffentlichten Wertungsanlage beschriebenen Umfang nicht überschreiten.
""", "Malte Winter\nZentraler Einkauf | Unterlagenfassung 1")

document(6, "Eignung_Wertungsanlage", GVB, "Vergabeunterlagen GVB-REI-2026-017 | Los 1", "23.07.2026", "Teilnahmebedingungen und Zuschlagskriterien", """
1. Teilnahme

Der Teilnahmeantrag enthält Unternehmensdaten, die benannten vertretungsberechtigten Personen, Erklärungen zu Ausschlussgründen und die vorgesehenen Nachunternehmer mit Leistungsanteil. Die wirtschaftliche Leistungsfähigkeit ist durch den Umsatz im Tätigkeitsbereich Gebäudereinigung in den letzten drei abgeschlossenen Geschäftsjahren darzustellen. Der geforderte Mindestumsatz beträgt 900000 EUR netto jährlich für Los 1. Bietergemeinschaften stellen die Aufgabenverteilung und die gemeinsam verfügbaren Mittel dar.

Gefordert sind zwei Referenzen für die Reinigung öffentlich zugänglicher Objekte in laufendem Betrieb mit jeweils mindestens 3000 m² und mindestens zwölf Monaten Leistungsdauer innerhalb der letzten drei Jahre. Verkehrsstationen sind nicht zwingend. Auftraggeber, Kontakt, Zeitraum, Umfang und eigene Leistung sind anzugeben. Für die angebotene Leistung muss eine Betriebshaftpflichtversicherung mit 5000000 EUR für Personen- und Sachschäden sowie 250000 EUR für Schlüsselverlust spätestens zum Leistungsbeginn vorliegen. Eine verbindliche Versichererbestätigung über die mögliche Deckung genügt im Teilnahmeantrag.

Es ist keine Beschränkung der Bewerberzahl vorgesehen. Jeder geeignete, nicht auszuschließende Bewerber wird zur Angebotsabgabe aufgefordert. Die GVB kann im rechtlich zulässigen Umfang Erklärungen und Nachweise nachfordern. Eine Nachforderung wird über dieselbe Vergabeplattform an den betroffenen Bewerber gestellt und enthält eine konkrete Frist.

2. Preis

Der Preis erhält höchstens 60 Punkte. Maßgeblich ist der rechnerische Gesamtpreis aus vier Grundjahren, dem optionalen fünften Jahr und den im Preisblatt angegebenen Wertungsmengen für Sonderreinigungen. Der niedrigste wertbare Gesamtpreis erhält 60 Punkte. Andere Angebote erhalten 60 multipliziert mit dem niedrigsten wertbaren Gesamtpreis, geteilt durch ihren eigenen Gesamtpreis. Erst das Ergebnis wird auf zwei Nachkommastellen gerundet. Die Optionsausübung ist durch diese Rechnung noch nicht zugesagt.

3. Ausführungskonzept

Das Konzept erhält höchstens 40 Punkte: Personal- und Vertretungsplanung 15, Durchführung in den vorgegebenen Zeitfenstern 15, Qualitätskontrolle und Störungsbearbeitung 10. Je Unterkriterium werden 0 bis 5 Bewertungsstufen vergeben; der Anteil am Höchstwert errechnet sich aus Stufe geteilt durch 5. Stufe 0 bedeutet keine verwertbare Darstellung, 1 eine bloße allgemeine Zusage, 2 einen lückenhaften Objektbezug, 3 eine vollständige und nachvollziehbare Darstellung, 4 zusätzlich belegte Reserven für die beschriebenen Störungen und 5 eine besonders belastbare, anhand konkreter Abläufe nachvollziehbare Umsetzung einschließlich erprobter Vertretung.

Die Beurteilung muss auf den eingereichten Angaben beruhen. Reine Seitenzahl, Markenbekanntheit oder ein zusätzliches Zertifikat bringen keine eigenen Punkte. Das Konzept darf zehn A4-Seiten umfassen; Deckblatt und Inhaltsverzeichnis zählen mit, geforderte Referenznachweise nicht. Ein kleines lesbares Organigramm ist zulässig. Die veröffentlichten Mindestbedingungen bleiben auch bei einem überzeugenden Konzept einzuhalten.

4. Verhandlung und Abschluss

Verhandelt werden können Organisation und Ausführungsdetails, nicht die bekannt gemachten Zuschlagskriterien oder Mindestbedingungen. Eine Änderung der für alle geltenden Leistungsunterlagen wird einheitlich mitgeteilt. Die abschließende Angebotsaufforderung benennt die letzte Frist. Über abschließende Angebote wird nicht mehr verhandelt. Ein Zuschlag auf Erstangebote ohne Verhandlung ist in diesem Verfahren nicht vorbehalten.
""", "Malte Winter\nAnlage W | Fassung 1")

document(7, "Reinigungsvertrag_Entwurf", GVB, "Vertragsunterlage zu GVB-REI-2026-017 | Los 1", "23.07.2026", "Vertrag über die Unterhaltsreinigung", """
1. Vertragsschluss und Bestandteile

Die GVB Gemeinsame Verkehrsbetriebe Berlin AöR beauftragt den im Zuschlag bezeichneten Auftragnehmer mit der Unterhaltsreinigung von Stationen und Betriebsräumen. Der Auftragnehmer wird durch sein Angebot und den Zuschlag bestimmt. Vertragsbestandteile sind der Zuschlag, diese Vertragsbedingungen, die abschließend veröffentlichten Antworten und Änderungen, Leistungsbeschreibung, Objektliste, Preisblatt und das angenommene Ausführungskonzept. Allgemeine Geschäftsbedingungen des Auftragnehmers werden nicht allein durch einen Hinweis auf seiner Rechnung Vertragsbestandteil.

2. Laufzeit und Übergabe

Leistungsbeginn ist der 01.01.2027. Der Vertrag endet am 31.12.2030. Die GVB kann ihn durch Erklärung in Textform bis zum 30.06.2030 einmal um zwölf Monate verlängern. Ein Anspruch des Auftragnehmers auf die Verlängerung besteht nicht. Die Übergabe der Objekte und Schlüssel wird protokolliert. Der Auftragnehmer benennt vor der Übergabe Objektleiter und Stellvertreter und weist Unterweisungen nach. Arbeitsverhältnisse, Personalübernahmen und erforderliche Unterrichtungen sind von den Beteiligten gesondert anhand der tatsächlichen Verhältnisse zu behandeln; der Vertrag behauptet dazu keine abschließende Einordnung.

3. Entgelt und Abrechnung

Die regelmäßigen Leistungen werden monatlich mit einem Zwölftel des vereinbarten Jahrespreises abgerechnet. Abrufe sind mit Datum, anordnender Person, Ort, Menge und vereinbartem Einheitspreis nachzuweisen. Umsatzsteuer wird gesondert ausgewiesen. Nicht angeordnete Zusatzleistungen werden nicht dadurch anerkannt, dass ein Mitarbeiter der GVB auf einem Arbeitszettel lediglich die Anwesenheit bestätigt. Die Rechnung nennt Vergabenummer, Los, Leistungsmonat und die Objektkennungen. Die Zahlungsfrist beträgt 30 Tage nach Zugang einer prüffähigen Rechnung.

4. Entgeltanpassung

Bei verbindlichen Änderungen der für die eingesetzten Beschäftigten maßgeblichen Löhne kann jede Partei eine Anpassung des nachgewiesenen Lohnkostenanteils für die Zukunft verlangen. Ausgangslohn, betroffene Stunden und Zuschläge sind offen zu legen. Der übrige Kalkulationsanteil wird dadurch nicht automatisch angehoben. Eine Rückrechnung vor Wirksamwerden der Lohnänderung ist ausgeschlossen. Die Parteien dokumentieren die Einigung; die bloße Ankündigung ersetzt keine geänderte Rechnung.

5. Personal und Nachunternehmer

Die gültigen besonderen Vertragsbedingungen des Landes Berlin zu Tariftreue und Mindeststundenentgelt, Kontrolle und Sanktionen sowie Umweltschutz werden mit den Vergabeunterlagen bereitgestellt. Die GVB verlangt die darin vorgesehenen Nachweise auch bei zulässigen Nachunternehmern. Jeder neue Nachunternehmer ist vor Einsatz mit Tätigkeit, Ansprechpartner und Nachweisen mitzuteilen. Die Verantwortung des Auftragnehmers für die Leistung bleibt bestehen. Zutritt wird nur unterwiesenem Personal mit dokumentierter Schlüsselberechtigung gewährt.

6. Mängel, Schäden und Versicherung

Beanstandungen werden objekt- und zeitbezogen mitgeteilt. Für die Nachbesserung wird eine der Störung angemessene Frist gesetzt. Sofortige Gefahren sind der Leitstelle zu melden und abzusichern, soweit dies gefahrlos möglich ist. Der Auftragnehmer führt die zugesagte Haftpflichtdeckung während der Vertragszeit fort und meldet deren Wegfall unverzüglich. Schadensersatz, Vergütungsminderung und Vertragsbeendigung setzen ihre jeweiligen Voraussetzungen voraus; eine pauschale Belastung für sämtliche Fahrgastbeschwerden ist nicht vereinbart.

7. Änderungen und Ende

Mengenänderungen und zusätzliche Objekte bedürfen einer dokumentierten Beauftragung; der Auftragnehmer darf sein Personal nicht allein aufgrund einer mündlichen Bitte eines örtlichen Mitarbeiters dauerhaft auf weitere Gebäude umstellen. Zum Vertragsende werden Schlüssel, Objektunterlagen und offene Störungsmeldungen übergeben. Die Parteien benennen Ansprechpartner für die Übergabe. Der Entwurf ist noch nicht unterzeichnet und begründet für sich allein keinen Auftrag.
""", "Vertragsredaktion: Malte Winter\nAusgabe zur Angebotskalkulation")

document(8, "Bekanntmachungsdaten", GVB, "Zentraler Einkauf | Veröffentlichungsakte", "24.07.2026", "Bekanntmachungsdaten zur Reinigungsvergabe", """
Vergabenummer: GVB-REI-2026-017. Interne Versandkennung: GVB-PUB-240726-017. Der Datensatz wurde am 24.07.2026 um 09:12 Uhr zur Veröffentlichung weitergegeben. Die Versandkennung ist keine TED-Veröffentlichungsnummer. Die gesonderte EU-Veröffentlichungsbestätigung befindet sich nicht in diesem Ausdruck.

Auftraggeber ist die GVB Gemeinsame Verkehrsbetriebe Berlin, Anstalt des öffentlichen Rechts, Köpenicker Straße 186, 10997 Berlin. Kontakt: Zentraler Einkauf, Malte Winter, vergabestelle@gvb-berlin.example. Haupttätigkeit ist der öffentliche Personenverkehr mit U-Bahn, Straßenbahn und Omnibussen. Erfüllungsort ist Berlin, Deutschland; NUTS DE300. CPV-Hauptcode: 90910000, Reinigungsdienste.

Vorgesehen ist ein Verhandlungsverfahren mit Teilnahmewettbewerb. Gegenstand sind Los 1 Unterhaltsreinigung von Stationen und Betriebsräumen, Los 2 Fahrzeugreinigung und Los 3 Glasreinigung. Angebote können für ein oder mehrere Lose abgegeben werden. Es gibt keine Zuschlagsbegrenzung. Die veröffentlichten Kriterien, Vertragsunterlagen und Informationen werden kostenfrei auf dem Vergabeportal bereitgestellt. Rückfragen und Teilnahmeanträge werden ausschließlich über das Portal angenommen.

Der geschätzte Gesamtwert über alle Lose, vier Jahre Grundlaufzeit, ein optionales Jahr und alle im Kostenblatt angesetzten Sonderabrufe beträgt 7000000 EUR netto. Los 1 umfasst geschätzt 4020000 EUR einschließlich der dort zugeordneten Sonderabrufe für fünf Jahre. Es besteht keine Mindestabnahme für Sonderabrufe. Leistungsbeginn 01.01.2027, Ende der Grundlaufzeit 31.12.2030, Option bis 31.12.2031.

Teilnahmeanträge sind bis 24.08.2026, 12:00 Uhr, Berliner Ortszeit, einzureichen. Die Aufforderung zur Angebotsabgabe ist für den 26.08.2026 vorgesehen. Keine zahlenmäßige Begrenzung geeigneter Bewerber. Mindestbedingungen und Wertungsmaßstab ergeben sich aus Anlage W. Nebenangebote sind nicht zugelassen. Die Angebotssprache ist Deutsch. Einzelne fremdsprachige Nachweise dürfen mit verständlicher Übersetzung vorgelegt werden.

Zuständige Nachprüfungsstelle: Vergabekammer des Landes Berlin. Die Bekanntmachung verweist hinsichtlich Zulässigkeit und Fristen eines Nachprüfungsantrags auf Paragraf 160 Absatz 3 GWB. Eine Information nach Paragraf 134 GWB wird vor dem beabsichtigten Zuschlag versandt. Veröffentlichung, Zugang von Nachrichten und Fristberechnung sind getrennt in der Vergabeakte zu dokumentieren.

Dieser Ausdruck enthält den redaktionell freigegebenen Datensatz. Die elektronische Versandquittung ist durch die Plattformverwaltung beizuziehen, sobald sie vorliegt. Zeichnung: Einkauf 24.07.2026, 08:55 Uhr; Finanzen 23.07.2026, 16:20 Uhr.
""", "Malte Winter\nZentraler Einkauf")

document(12, "Teilnahmeantrag_Maerkischer", MARK, "GVB | Zentraler Einkauf | über Vergabeplattform", "21.08.2026", "Teilnahmeantrag Los 1", """
Sehr geehrter Herr Winter,

wir beantragen die Teilnahme am Verhandlungsverfahren GVB-REI-2026-017 für Los 1. Wir bewerben uns als einzelner Bieter und beabsichtigen keine Bietergemeinschaft. Die nächtliche Unterhaltsreinigung erbringen wir mit eigenem Personal. Für einmalige Höhenarbeiten im Gerätebereich ist bisher kein Nachunternehmer beauftragt; solche Arbeiten sollen nur nach gesonderter Abstimmung stattfinden und gehören nicht zu unserem Angebot auf Glasreinigung.

Unsere Umsätze in der Gebäudereinigung betrugen 2023 netto 2810000 EUR, 2024 netto 3040000 EUR und 2025 netto 3260000 EUR. Die Zahlen beziehen sich auf die Märkischer Objektservice GmbH, nicht auf verbundene Unternehmen. Die Geschäftsführung bestätigt die Richtigkeit nach dem abgeschlossenen Jahresabschluss beziehungsweise der endgültigen Umsatzaufstellung des Steuerbüros.

Referenz 1: Einkaufszentrum Lindenhof, öffentlich zugängliche Verkehrsflächen 8600 m², Unterhaltsreinigung seit 01.04.2022, Kontakt Auftraggeber Herr Ostermann, objektleitung@lindenhof-center.example. Wir betreuen täglich wechselnde Teilflächen im laufenden Betrieb und außerhalb der Öffnungszeit. Referenz 2: Städtisches Sport- und Veranstaltungszentrum Havelbogen, 4200 m², Reinigung vom 01.01.2023 bis 31.12.2025, Ansprechpartner Frau Brenner, betrieb@havelbogen-sport.example. Dort waren Wochenenddienste und kurzfristige Sonderreinigungen eingeschlossen.

Die Vertretung des Unternehmens erfolgt durch mich. Zu Ausschlussgründen erklären wir: Uns sind für unser Unternehmen keine rechtskräftigen Verurteilungen oder bestandskräftigen Bußgeldentscheidungen wegen der in den Teilnahmeunterlagen abgefragten Tatbestände bekannt. Steuern und Sozialversicherungsbeiträge werden laufend entrichtet. Ein Insolvenzverfahren ist weder beantragt noch eröffnet. Auskünfte und ergänzende Nachweise werden auf Anforderung vorgelegt.

Die Betriebshaftpflicht besteht bei der Havel-Assekuranz AG unter Vertrag HA-20-4418. Die Deckung für Personen- und Sachschäden beträgt 5000000 EUR. Der aktuell vorhandene Versicherungsauszug nennt für Schlüsselverlust 100000 EUR. Unser Makler hat die Erhöhung angefragt. Dessen Antwort reichen wir nach, sobald sie vorliegt. Eine bereits erteilte Erhöhungsbestätigung können wir heute nicht beifügen.

Wir haben die angebotenen Objekte am 13.08.2026 mit Ihrem Stationsservice besichtigt und die veröffentlichten Ergänzungen abgerufen. Ansprechpartner für Rückfragen ist Frau Rabe im Vergabeteam, Durchwahl 3922. Die technischen Konzeptunterlagen reichen wir erst mit dem Angebot ein.
""", "Mit freundlichen Grüßen\nNils Faber\nGeschäftsführer")

document(16, "Angebot_Spreeklar", SPREE, "GVB | Zentraler Einkauf | Vergabeportal Los 1", "10.09.2026", "Erstangebot mit Ausführungskonzept", """
Sehr geehrter Herr Winter,

wir bieten die Leistungen von Los 1 nach den bis einschließlich 17.08.2026 veröffentlichten Unterlagen an. Unser Grundpreis beträgt 714000 EUR netto pro Jahr. Für die im Preisblatt angesetzten Sonderreinigungen kalkulieren wir jährlich 28000 EUR netto. Unser Wertungspreis für fünf Jahre einschließlich Option und der vorgegebenen Sondermengen beträgt damit 3710000 EUR netto. Eine Mindestabnahme der Sondermengen ist damit nicht verbunden.

1. Einsatzplanung

Für die Stationen setzen wir zwei Nachtteams mit jeweils vier Beschäftigten ein. Ein Springer deckt Urlaub und kurzfristige Erkrankungen. Die Objektleitung ist zwischen 22:00 und 06:00 Uhr telefonisch erreichbar. An Wochenenden bearbeiten wir Teilflächen hinter mobilen Absperrungen. Der tägliche Reinigungsnachweis wird nach Objekt und Einsatzzeit geführt. Fotos werden nur von der gereinigten Fläche ohne Fahrgäste aufgenommen.

Wir haben für die Nachtteams zunächst eine Anwesenheit von jeweils drei Stunden je Stationenschicht gerechnet. In den letzten Unterlagen finden sich daneben einzelne kürzere Sperrfenster. Nach unserem Verständnis beziehen diese sich nur auf die Gleisnähe. Den übrigen Bahnsteig wollen wir vor und nach diesem Fenster abschnittsweise bearbeiten. Bitte bestätigen Sie, ob die Stationsleitung hierfür die Zugänge öffnen kann. Die Kalkulation enthält derzeit keine zusätzliche Begleitung durch eigenes Sicherungspersonal.

2. Qualität und Störungen

Objektleiter ist Tobias Krüger, Stellvertreterin ist Elena Sander. Beide betreuen vergleichbare Verkehrsanlagen. Die Leitstelle erreicht uns über eine feste Mobilnummer; eingehende Störungen werden mit Rückrufzeit dokumentiert. Innerhalb von 20 Minuten wird ein Ansprechpartner zurückrufen. Für sofortige Sonderreinigungen disponiert der Objektleiter den nächsten verfügbaren Springer. Eine feste Ankunftszeit für jedes Objekt können wir ohne Kenntnis der Zugangssituation nicht zusagen.

Unsere Wochenkontrolle erfasst Sanitärbereiche, Abfallstellen und Bodenbeläge an wechselnden Punkten. Bei einer Beanstandung wird die Fläche erneut geprüft, die Abweichung dokumentiert und die Behebung bestätigt. Nachunternehmer sind für Los 1 nicht vorgesehen. Reinigungsmittel werden nach Materialverträglichkeit beschafft; wir legen Sicherheitsdatenblätter vor dem ersten Einsatz vor.

3. Kalkulation und Bindung

Der Preis beruht auf 22800 produktiven Stunden pro Jahr. Unsere durchschnittlichen direkten Lohnkosten haben wir mit 15,50 EUR je Stunde angesetzt; Zuschläge, Ausfallzeiten und sonstige Kosten legen wir im Verhandlungsgespräch gesondert offen. Das Preisblatt verwendet die veröffentlichten Jahresmengen. Bei Änderung der Zeitfenster müssen wir die Tourenplanung überprüfen. An dieses Erstangebot halten wir uns bis 30.11.2026 gebunden.
""", "Mit freundlichen Grüßen\nHenrik Seidel\nGeschäftsführer")

document(17, "Angebot_Maerkischer", MARK, "GVB | Zentraler Einkauf | Vergabeportal Los 1", "10.09.2026", "Erstangebot und Objektkonzept", """
Sehr geehrter Herr Winter,

wir bieten Los 1 zum Grundpreis von 776000 EUR netto pro Jahr an. Bei den vorgegebenen Wertungsmengen entfallen weitere 31000 EUR netto jährlich auf Sonderreinigungen. Der Wertungspreis über fünf Jahre beträgt 4035000 EUR netto. Das Preisblatt wurde durch Nils Faber am 10.09.2026 um 09:45 Uhr freigegeben und um 10:12 Uhr über das Portal eingereicht.

Wir legen die am 17.08.2026 klargestellten Zugangsfenster zugrunde. In Hermannstraße und Neukölln stehen für die zusammenhängende Nassreinigung nur 90 Minuten zur Verfügung. Zwei mobile Teams treffen deshalb bereits vor Beginn am jeweiligen Materialraum ein, ohne die gesperrte Fläche vorzeitig zu betreten. Die übrigen Bereiche werden tagsüber abschnittsweise gereinigt. Wege-, Rüst- und Kontrollzeiten sind neben den reinen Flächenstunden kalkuliert.

Für den Regelbetrieb sind 28600 produktive Stunden pro Jahr vorgesehen. Die Personaldisposition umfasst einen fest zugeordneten Objektleiter, zwei Teamleiter und einen Vertretungspool. Eine Vertretung wird nicht gleichzeitig für mehrere ausgefallene Beschäftigte eingeplant. Die Mitarbeiter erhalten vor Einsatz eine örtliche Unterweisung. Der Objektleiter führt täglich eine Abgleichliste zwischen geplanten und erbrachten Einsätzen. Abweichungen wegen einer betrieblichen Sperrung werden nicht als gereinigte Fläche abgerechnet.

Die Störungsannahme ist durchgehend erreichbar. Für Getränkeaustritte halten wir während der Betriebszeit ein Fahrzeug mit Grundausstattung bereit. Bei unbekannten Flüssigkeiten klärt die GVB zunächst die Freigabe; wir versprechen keine gefahrlose Aufnahme unbekannter Stoffe ohne entsprechende Prüfung. Für die Wochenkontrolle erhalten Ihre Mitarbeiter ein kurzes Protokoll mit Ort, Zeitpunkt, Abweichung und Erledigung. Personenbezogene Leistungsrankings unserer Beschäftigten sind nicht vorgesehen.

Die direkte Lohnkalkulation beruht auf durchschnittlich 17,25 EUR pro produktiver Stunde. Dazu kommen bezahlte Ausfallzeiten, Arbeitgeberkosten und Nacht- beziehungsweise Wochenendzuschläge. Unser Versicherer hat die benötigte Schlüsselverlustdeckung für den Auftragsfall bestätigt. Diese Bestätigung ging Ihnen bereits auf Ihre Nachforderung zu. Die Jahrespreise enthalten Geräteverschleiß, Ersatzbeschaffung und die standortbezogene Einweisung.

Wir bitten im Verhandlungsgespräch um Klärung, ob die GVB den Geräteraum am Adlergestell ab 16.11.2026 für die Einrichtung freigibt. Ein früherer Zugang ist für unser Angebot nicht zwingend. Wir möchten aber vermeiden, dass Reinigungsmittel unmittelbar vor dem Jahreswechsel ohne geordnetes Lager eintreffen. Wir halten uns bis 30.11.2026 an unser Angebot gebunden.
""", "Mit freundlichen Grüßen\nNils Faber\nGeschäftsführer")

document(18, "Angebot_Nordlicht", NORD, "GVB | Zentraler Einkauf | Vergabeportal Los 1", "10.09.2026", "Angebot zur Unterhaltsreinigung", """
Sehr geehrte Damen und Herren,

unser Angebot betrifft Los 1. Der Grundpreis beträgt 808000 EUR netto pro Jahr; die vorgegebenen Sondermengen sind mit 32000 EUR netto jährlich kalkuliert. Für vier Vertragsjahre und ein Optionsjahr ergibt sich ein Wertungspreis von 4200000 EUR netto. Nebenangebote geben wir nicht ab. Die letzten Ergänzungen vom 17.08.2026 liegen der Planung zugrunde.

Für die Stationen arbeiten drei kleine Teams zeitversetzt. So können wir kurze Freigabefenster nutzen, ohne die anderen Objekte derselben Schicht unbesetzt zu lassen. Der Objektleiter ist für die GVB namentlich benannt; außerhalb seiner Arbeitszeit übernimmt ein diensthabender Einsatzleiter. Die Disposition hält tägliche Soll- und Ist-Zeiten fest. Den Aufenthalt von Fremdpersonal im Gleisbereich schließen wir aus unserer Reinigung ausdrücklich aus.

Die Kalkulation umfasst 29200 produktive Stunden. Die Reinigungsgeräte werden aus unserem Berliner Bestand gestellt, bei Ausfall binnen einer Schicht ersetzt. In der Anlaufphase prüfen wir mit der GVB die Verträglichkeit auf den vorhandenen Steinflächen. Mittel mit auffälliger Geruchsentwicklung setzen wir nur ein, wenn die GVB den Bereich vorab freigibt und Fahrgäste nicht betroffen sind. Die Glasfassaden werden nicht mitgerechnet.

Sonderreinigungen werden über die Einsatzleitung bestellt. Der Mitarbeiter vor Ort nimmt keine dauerhafte Erweiterung des Auftrags an. Wir dokumentieren auch einen vergeblichen Anlauf, wenn der Zugang geschlossen ist. Eine pauschale Bestätigung aller Monatseinsätze durch die Pforte genügt uns nicht; wir bitten um einen verantwortlichen Ansprechpartner des Stationsservice.

Unsere Referenzen und die Versicherungszusage wurden mit dem Teilnahmeantrag am 20.08.2026 vorgelegt. Sollte eine Unterlage nicht lesbar sein, bitten wir um konkrete Nachricht. Wir halten die Unterlagen digital und in Papierform bereit. Die Preisbindung endet am 30.11.2026.
""", "Mit freundlichen Grüßen\nDaniel Lindner\nGeschäftsführer")

document(20, "Verhandlung_Spreeklar", GVB, "GVB Einkauf und Spreeklar Gebäudedienste GmbH", "16.09.2026", "Protokoll des Verhandlungsgesprächs zu Los 1", """
Teilnehmer: Malte Winter und Silke Mertens für die GVB, Henrik Seidel und Tobias Krüger für Spreeklar. Videokonferenz 09:00 bis 10:05 Uhr. Das Protokoll wurde allen Teilnehmern am selben Tag um 13:20 Uhr zur Durchsicht übersandt. Es dokumentiert das Gespräch und ist kein Zuschlag.

1. Zeitfenster

Mertens erläutert, dass in Hermannstraße und Neukölln das 90-Minuten-Fenster die zusammenhängende Nassreinigung der benannten Bahnsteigbereiche betrifft. Eine Verlängerung durch die örtliche Stationsleitung ist nicht zugesagt. Abschnittsweise Tagesreinigung ist nur im zulässigen Rahmen der veröffentlichten Unterlagen möglich. Seidel erklärt, er habe bisher mit drei Stunden für dieselbe zusammenhängende Leistung gerechnet. Krüger möchte die Schichten auf kleinere Teams verteilen. Eine zusätzliche Freigabe der Gleisbereiche wird nicht verlangt und nicht angeboten.

2. Personal und Vertretung

Winter fragt, wie der einzelne Springer bei gleichzeitigem Ausfall an zwei Stationen eingesetzt wird. Krüger nennt einen weiteren Mitarbeiter aus einem benachbarten Objekt. Auf Nachfrage wird erklärt, dass dessen Anwesenheit bisher nicht fest für die GVB gebunden ist. Spreeklar will im abschließenden Konzept einen eigenen Vertretungsplan vorlegen. Die GVB erklärt nicht, dass ein bestimmter Personalschlüssel die Mindestbedingungen erfüllt; das Konzept muss die Leistung innerhalb der Fenster nachvollziehbar darstellen.

3. Preise

Winter verlangt eine Aufschlüsselung zu produktiven Stunden, bezahlten Ausfallzeiten, Arbeitgeberkosten, Zuschlägen, Geräten, Fahrten und Gemeinkosten. Seidel kündigt eine neue Stundenplanung und einen angepassten Preis an. Die GVB weist darauf hin, dass alle Bewerber dieselbe Gelegenheit zum abschließenden Angebot erhalten. Informationen über Preise oder Konzepte anderer Bewerber werden nicht weitergegeben.

4. Weiteres Vorgehen

Die GVB wird die abschließende Angebotsaufforderung am 17.09.2026 über das Portal versenden. Frist ist der 22.09.2026 um 12:00 Uhr. Änderungen der veröffentlichten Kriterien sind nicht Gegenstand dieses Gesprächs. Die Gesprächsteilnehmer sind sich einig, dass das nächste Angebot als abschließend bezeichnet wird. Gegen dieses Protokoll geht bis 18.09.2026 keine Berichtigung ein.
""", "Aufgenommen: Malte Winter\nKenntnisnahme per Portal: Henrik Seidel, 17.09.2026, 08:46 Uhr")

document(23, "Preisaufklaerung_Spreeklar", SPREE, "GVB | Zentraler Einkauf | Nachricht vom 23.09.2026", "24.09.2026", "Erläuterung unseres abschließenden Preises", """
Sehr geehrter Herr Winter,

Sie baten gestern um Aufklärung zu unserem abschließenden Angebot vom 22.09.2026. Wir bestätigen den angebotenen Grundpreis von 748000 EUR netto pro Jahr sowie jährlich 28000 EUR netto für die vorgegebenen Sondermengen. Der Wertungspreis über fünf Jahre beträgt 3880000 EUR netto. Wir ändern mit dieser Erläuterung weder Preis noch Leistungsumfang.

Unser abschließendes Konzept sieht 26400 produktive Stunden pro Jahr vor. Die direkten Lohnkosten hierfür betragen bei unserem kalkulierten Durchschnitt von 16,40 EUR je Stunde 432960 EUR. Bezahlte Ausfallzeiten sind mit 58000 EUR, Arbeitgeberkosten mit 100000 EUR und Zuschläge mit 54000 EUR berücksichtigt. Geräte und Chemie entfallen mit 38000 EUR, Fahrten mit 22000 EUR, Objektleitung und allgemeine Kosten mit 30000 EUR auf den Grundauftrag. Der Restbetrag beträgt 13040 EUR. Diese Ansätze ergeben zusammen 748000 EUR.

Die 16,40 EUR sind ein gewichteter Kalkulationswert und keine Aussage, dass jeder eingesetzte Beschäftigte diesen Stundenlohn erhält. Für die unterschiedlichen Tätigkeiten und Zuschläge gelten die jeweils verbindlichen Vorgaben. Die mit dem Angebot abgegebenen Verpflichtungserklärungen bleiben bestehen. Wir haben für Wochenendvertretungen Mitarbeiter mit unterschiedlichen vertraglichen Stundenumfängen vorgesehen. Die vollständige Personaleinsatzliste mit Namen geben wir aus Gründen des Beschäftigtenschutzes nicht an konkurrierende Unternehmen weiter.

Die erhöhte Stundenzahl gegenüber dem Erstangebot beruht auf der verkürzten zusammenhängenden Reinigungszeit und zusätzlicher Rüstzeit. Für zwei kurze Schichten benötigt man mehr paralleles Personal, nicht automatisch mehr Maschinen. Wir nutzen vorhandene Geräte; die ausgewiesenen 38000 EUR enthalten deren laufende Ersatzbeschaffung. Den Vertretungspool halten wir durch feste Einsatzvereinbarungen vor. Eine Ausführung durch nicht benannte Nachunternehmer ist nicht vorgesehen.

Bitte behandeln Sie die detaillierten Kostenansätze und unsere Personaleinsatzplanung vertraulich. Uns ist bewusst, dass gegenüber anderen Bietern möglicherweise wesentliche Gründe einer Zuschlagsentscheidung mitzuteilen sind. Unsere Bitte betrifft die konkrete interne Kostenzerlegung und personenbezogene Einzelangaben. Die Erklärung enthält keine Einwilligung in eine Veröffentlichung sämtlicher Angebotsunterlagen.
""", "Mit freundlichen Grüßen\nHenrik Seidel\nGeschäftsführer")

document(24, "Vorabinformation_Maerkischer", GVB, "Märkischer Objektservice GmbH | Herrn Nils Faber | über Vergabeportal", "25.09.2026", "Information zum beabsichtigten Zuschlag für Los 1", """
Sehr geehrter Herr Faber,

wir beabsichtigen, den Zuschlag im Verfahren GVB-REI-2026-017, Los 1, an die Spreeklar Gebäudedienste GmbH, Wilhelminenhofstraße 76, 12459 Berlin, zu erteilen. Ihr abschließendes Angebot vom 22.09.2026 wird nicht berücksichtigt.

Das Angebot des vorgesehenen Auftragnehmers hat nach unserer Bewertung insgesamt die höhere Punktzahl erreicht. Ihr Angebot ist im Preis weniger günstig. Bei der Bewertung des Ausführungskonzepts ergaben sich Unterschiede in der Einsatzorganisation. Weitere Einzelheiten betreffen vertrauliche Angebotsinhalte des vorgesehenen Auftragnehmers und werden mit diesem Schreiben nicht mitgeteilt.

Die Gesamtpreise für die Wertung betrugen bei Ihnen 4010000 EUR netto und beim vorgesehenen Auftragnehmer 3880000 EUR netto. Beide Beträge enthalten vier Grundjahre, das optionale fünfte Jahr sowie die bekannt gegebenen Sondermengen. Dieses Schreiben erteilt noch keinen Zuschlag. Als frühesten Tag des Vertragsschlusses sehen wir den 06.10.2026 vor.

Die Nachricht wird elektronisch über die Vergabeplattform versandt. Für Fragen verwenden Sie bitte den Nachrichtenbereich des Verfahrens und nennen Sie die Vergabenummer. Der Eingang einer Rückfrage verändert Fristen nicht allein durch seine Bezeichnung. Die bisherige Bindefrist bleibt unberührt.
""", "Mit freundlichen Grüßen\nMalte Winter\nZentraler Einkauf\nVersand im Portal: 25.09.2026, 15:18 Uhr")

document(26, "Ruege_Maerkischer", MARK, "GVB | Zentraler Einkauf | über Vergabeportal", "28.09.2026", "Beanstandung der Vorabinformation und der Wertung Los 1", """
Sehr geehrter Herr Winter,

wir rügen die mit Ihrem Schreiben vom 25.09.2026 mitgeteilte Entscheidung. Wir haben die Nachricht am selben Tag um 15:31 Uhr abgerufen. Das Schreiben nennt zwar zwei Preise, aber keine nachvollziehbaren Gründe, weshalb unser objektbezogenes Konzept schlechter oder insgesamt weniger wirtschaftlich bewertet wurde. Insbesondere fehlt jede Aussage zu den veröffentlichten Unterkriterien und zu den erreichten Punkten.

Unser Angebot berücksichtigt die verkürzten Reinigungsfenster, fest eingeplante Vertretungen und die Kosten bezahlter Ausfallzeiten. Aus Ihrem Schreiben können wir nicht erkennen, ob diese Punkte bei allen Angeboten nach demselben Maßstab beurteilt wurden. Die bloße Berufung auf Vertraulichkeit genügt uns nicht. Wir verlangen keine Namen fremder Beschäftigter und keine ungeschwärzte interne Kalkulation, sondern verständliche Gründe der für unser Angebot nachteiligen Entscheidung.

Ferner bitten wir um Bestätigung, dass das Angebot von Spreeklar die am 17.08.2026 verbindlich mitgeteilten 90-Minuten-Fenster berücksichtigt und eine auskömmliche Personaleinsatzplanung enthält. Der Preisabstand allein beweist aus unserer Sicht keinen Verstoß. Er veranlasst aber zusammen mit den knappen Angaben zur Einsatzorganisation eine konkrete Nachfrage. Wir können die Unterlagen unseres Wettbewerbers nicht einsehen und behaupten daher keinen uns unbekannten Kalkulationsinhalt.

Bitte überprüfen Sie die Wertung, teilen Sie uns die wesentlichen Gründe konkret mit und sehen Sie bis zur Klärung von einem Zuschlag ab. Wir erwarten Ihre Antwort spätestens am 30.09.2026 um 16:00 Uhr. Sollte keine Abhilfe erfolgen, behalten wir uns einen Nachprüfungsantrag bei der Vergabekammer Berlin vor. Der von Ihnen genannte 06.10.2026 liegt zeitlich nahe; bitte bestätigen Sie den Eingang dieser Rüge kurzfristig.
""", "Mit freundlichen Grüßen\nNils Faber\nGeschäftsführer")

document(28, "Nichtabhilfe_GVB", GVB, "Märkischer Objektservice GmbH | Herrn Nils Faber | Vergabeportal", "30.09.2026", "Antwort auf Ihre Beanstandung vom 28.09.2026", """
Sehr geehrter Herr Faber,

wir haben Ihre Beanstandung geprüft und helfen ihr nicht ab. Nach unserer Auffassung wurden die veröffentlichten Bedingungen und Kriterien einheitlich angewandt. Spreeklar hat nach dem Verhandlungsgespräch ein abschließendes Konzept eingereicht. Den niedrigeren Preis haben wir vor der Zuschlagsentscheidung erläutern lassen. Die Leistung ist aus unserer Sicht mit dem beschriebenen Einsatz zu erbringen.

Die Angebotswertung liegt in unserer Vergabeakte vor. Wir halten die mitgeteilten Gesamtpreise und den Hinweis auf die Einsatzorganisation für ausreichend. Eine weitergehende Offenlegung der internen Kalkulation oder der personenbezogenen Einsatzpläne des Wettbewerbers lehnen wir ab. Ihre Kritik ist zur Vergabeakte genommen worden. Die von Ihnen vorgetragenen Gesichtspunkte führen für uns nicht zu einer Änderung der beabsichtigten Entscheidung.

Wir halten am geplanten Zuschlag frühestens am 06.10.2026 fest. Das Verfahren ist noch nicht durch Zuschlag abgeschlossen. Für einen etwaigen Nachprüfungsantrag beachten Sie bitte die gesetzlichen Zulässigkeitsvoraussetzungen und Fristen. Dieses Schreiben ist die Mitteilung, dass wir Ihrer Rüge nicht abhelfen.
""", "Mit freundlichen Grüßen\nMalte Winter\nZentraler Einkauf\nElektronischer Versand: 30.09.2026, 14:22 Uhr")

document(29, "Nachpruefungsantrag", ["Kanzlei Falk und Bremer", "Rechtsanwälte | Kantstraße 118 | 10625 Berlin", "post@falk-bremer.example | Telefon 030 5550 5870", "Bearbeiter: Rechtsanwalt Dr. Paul Falk"], "An die Vergabekammer des Landes Berlin", "01.10.2026", "Nachprüfungsantrag Märkischer Objektservice gegen GVB", """
Unser Zeichen: 26194-PF. Vergabenummer: GVB-REI-2026-017, Los 1. Antragstellerin: Märkischer Objektservice GmbH, Ringbahnstraße 42, 12099 Berlin, vertreten durch Geschäftsführer Nils Faber. Antragsgegnerin: GVB Gemeinsame Verkehrsbetriebe Berlin AöR, Köpenicker Straße 186, 10997 Berlin.

Namens und mit Vollmacht der Antragstellerin beantragen wir, der Antragsgegnerin die Zuschlagserteilung auf Grundlage der bisherigen Wertung zu untersagen und sie zu verpflichten, das Verfahren unter Beachtung der Rechtsauffassung der Vergabekammer fortzuführen. Ferner beantragen wir Akteneinsicht in die entscheidungserheblichen Teile der Vergabeakte unter Wahrung schutzwürdiger Geschäftsgeheimnisse sowie die Auferlegung der Verfahrenskosten auf die Antragsgegnerin.

Die Antragstellerin hat ein fristgerechtes abschließendes Angebot mit einem Wertungspreis von 4010000 EUR netto eingereicht. Sie hat damit ihr Interesse am Auftrag bekundet. Nach der Vorabinformation vom 25.09.2026 soll Spreeklar den Zuschlag erhalten. Das Schreiben und die Nichtabhilfe enthalten keine belastbare Erläuterung der Konzeptwertung. Ohne eine ordnungsgemäße Wertung kann die Antragstellerin aus ihrer Sicht den Auftrag verlieren, obwohl ihr Angebot bei einheitlicher Anwendung der Kriterien zum Zuge kommen könnte.

Die Antragstellerin rügte am 28.09.2026 die unzureichende Information sowie die Behandlung der Einsatzorganisation. Die Nichtabhilfe ging ihr am 30.09.2026 um 14:37 Uhr im Portal zu. Der beabsichtigte Zuschlag ist für frühestens 06.10.2026 angekündigt. Die Antragstellerin kann nicht prüfen, welche Unterschiede bei den drei Unterkriterien angesetzt wurden. Sie verlangt keine pauschale Offenlegung des gesamten Konkurrenzangebots. Eine mit den Geschäftsgeheimnissen vereinbare Mitteilung der wesentlichen Gründe muss jedoch möglich sein.

Hinzu kommt die ungeklärte Bewertung der kurzen nächtlichen Reinigungsfenster. Die Antragstellerin hat dafür zusätzliche parallele Teams kalkuliert. Ob das Konkurrenzangebot denselben Betriebsbedingungen entspricht, kann sie mangels Akteneinsicht nicht abschließend vortragen. Die Antragsgegnerin verweist lediglich auf eine Erläuterung des Preises. Die Antragstellerin beantragt deshalb Einsicht insbesondere in die dokumentierte Konzeptbewertung und in die Behandlung dieser Zeitfenster. Der Vortrag wird nach Akteneinsicht ergänzt.

Anlagen: Vorabinformation vom 25.09.2026, Rüge vom 28.09.2026, Nichtabhilfe vom 30.09.2026 und Vollmacht vom 01.10.2026. Die zugehörigen Dokumente werden jeweils gesondert beigefügt. Die Dringlichkeit folgt aus dem angekündigten Zuschlagstermin. Bitte bestätigen Sie den Eingang und unterrichten Sie die Antragsgegnerin unverzüglich über den Antrag.
""", "Dr. Paul Falk\nRechtsanwalt\nElektronisch übermittelt am 01.10.2026, 09:26 Uhr")

document(30, "Vollmacht", MARK, "Kanzlei Falk und Bremer | Rechtsanwalt Dr. Paul Falk", "01.10.2026", "Vollmacht im Vergabenachprüfungsverfahren", """
Die Märkischer Objektservice GmbH, Ringbahnstraße 42, 12099 Berlin, vertreten durch ihren Geschäftsführer Nils Faber, bevollmächtigt die Rechtsanwälte der Kanzlei Falk und Bremer, Kantstraße 118, 10625 Berlin, zur Vertretung im Vergabeverfahren GVB-REI-2026-017, Los 1, gegenüber der GVB Gemeinsame Verkehrsbetriebe Berlin AöR sowie im dazugehörigen Nachprüfungsverfahren.

Die Vollmacht umfasst die Einreichung und Begründung eines Nachprüfungsantrags, Akteneinsicht, die Abgabe und Entgegennahme von Erklärungen und Zustellungen sowie die Vertretung in der mündlichen Verhandlung. Ein Vergleich oder die Rücknahme des Nachprüfungsantrags bedarf im Innenverhältnis der vorherigen Freigabe durch den Geschäftsführer. Über Rechtsmittel soll gesondert nach Zugang der jeweiligen Entscheidung entschieden werden.

Der Auftrag bezieht sich auf Los 1. Er enthält keine Vollmacht zur Abgabe eines neuen Angebots, zur Unterzeichnung eines Reinigungsvertrags oder zur Weitergabe fremder Angebotsdaten an Dritte. Sachlicher Ansprechpartner ist Frau Rabe, Durchwahl 3922. Eilige Nachrichten sind gleichzeitig an den Geschäftsführer zu richten.

Berlin, 01.10.2026\nNils Faber\nGeschäftsführer\nNamenszug auf dem unterschriebenen Original; elektronische Abschrift an die Kanzlei um 08:52 Uhr übersandt.
""", "Märkischer Objektservice GmbH")

MAILS = [
    (9, "Zugangsfenster", "2026-08-11T07:42:00+02:00", "Jens Ahrens <j.ahrens@gvb-berlin.example>", "Malte Winter <m.winter@gvb-berlin.example>", "Los 1: Das Zeitfenster muss noch geändert werden", """Hallo Malte,

die Leitstelle hat mir gestern die endgültigen Sperrfenster gegeben. In Hermannstraße und Neukölln sind es montags bis donnerstags 00:45 bis 02:15 Uhr. Drei zusammenhängende Stunden gibt es dort nicht. Für die übrigen Flächen bleibt die abschnittsweise Reinigung im Betrieb möglich, aber nicht einfach mit der großen Maschine durch die Fahrgäste.

Im PDF vom 23. Juli steht noch 00:30 bis 03:30 Uhr. Bitte ändere das nicht nur in unserer internen Liste. Beim Besichtigungstermin haben zwei Firmen mitgeschrieben. Wir müssen alle auf denselben Stand bringen. Für Freitag und Samstag bleibt es beim durchgehenden Verkehr.

Am Adlergestell habe ich außerdem nachgemessen: 780 m² ist die einfache Glasfläche einschließlich der Ladenfront. Davon sind 90 m² Bäckerei. Wenn innen und außen gereinigt wird, ist die Arbeitsfläche eben eine andere Zahl. Das betrifft das Glaslos; im Stationslos sollten wir die Spiegel nicht versehentlich streichen.

Gruß
Jens Ahrens
GVB Stationsservice | Durchwahl 1721
Köpenicker Straße 186, 10997 Berlin"""),
    (10, "Bewerberfrage", "2026-08-12T11:18:00+02:00", "Nora Rabe <n.rabe@maerkischer-objektservice.example>", "Vergabestelle <vergabestelle@gvb-berlin.example>", "GVB-REI-2026-017: Frage 07 zu Nachtfenstern und Glas", """Sehr geehrter Herr Winter,

bei der Besichtigung wurden für zwei Stationen 90 Minuten genannt. In der Leistungsbeschreibung stehen drei Stunden. Welche Zeit ist für die Kalkulation verbindlich? Müssen Geräte und Personal in diesem Zeitraum auch hinein- und herausgebracht werden oder gibt es dafür einen separaten Vorlauf?

Außerdem nennt die Objektliste die Südfassade mit 780 m². Verstehen wir richtig, dass diese Fläche allein Los 3 betrifft? Die Kollegen haben am Gebäude einen vermieteten Laden gesehen. Wir wollen dessen Schaufenster nicht versehentlich mit anbieten.

Bitte stellen Sie die Antwort allen Bewerbern zur Verfügung. Wir rechnen nicht damit, dass eine mündliche Aussage bei der Besichtigung die veröffentlichte Unterlage ersetzt. Danke.

Mit freundlichen Grüßen
Nora Rabe | Vergabeteam
Märkischer Objektservice GmbH
Ringbahnstraße 42, 12099 Berlin | Telefon 030 5550 3922"""),
    (11, "Portalantwort_07", "2026-08-17T10:00:00+02:00", "Vergabeportal GVB <nachrichten@gvb-berlin.example>", "Registrierte Bewerber <bewerberkreis@gvb-berlin.example>", "GVB-REI-2026-017: Ergänzung 2 und Antwort auf Frage 07", """Sehr geehrte Damen und Herren,

die GVB stellt die Unterlagen zu Los 1 wie folgt klar: Für zusammenhängende Nassreinigung in Hermannstraße und Neukölln gilt montags bis donnerstags das Fenster 00:45 bis 02:15 Uhr. Das frühere Zeitfenster wird für diese beiden Stationen ersetzt. Geräte können nach Anmeldung 15 Minuten vor Beginn im Materialbereich bereitgestellt werden; die Reinigung der gesperrten Fläche beginnt erst nach Freigabe. Das Fenster umfasst die Räumung der Fläche. Die abschnittsweise Tagesreinigung übriger Flächen bleibt zulässig, soweit Rettungswege und Fahrgastbetrieb frei bleiben.

Die Glasfassade Adlergestell gehört zu Los 3. Aus 780 m² einfacher Fläche sind 90 m² Ladenfront herauszunehmen. Beidseitige Reinigung ergibt daher 1380 m² Arbeitsfläche je Durchgang. Spiegel in Sanitärräumen bleiben in Los 1. Die Mengenänderung betrifft nicht den Grundpreis für Los 1.

Die Teilnahmeantragsfrist bleibt am 24.08.2026, 12:00 Uhr. Mit der Angebotsaufforderung erhalten alle geeigneten Bewerber die bereinigten Unterlagen. Es werden noch keine Angebote oder Preise abgefordert. Diese Nachricht ist Bestandteil der Unterlagenfassung 2.

Mit freundlichen Grüßen
Malte Winter | Zentraler Einkauf
GVB Gemeinsame Verkehrsbetriebe Berlin AöR
Köpenicker Straße 186, 10997 Berlin"""),
    (13, "Nachforderung_Versicherung", "2026-08-24T14:36:00+02:00", "Malte Winter <m.winter@gvb-berlin.example>", "Nora Rabe <n.rabe@maerkischer-objektservice.example>", "GVB-REI-2026-017: Bestätigung Schlüsselverlustdeckung", """Sehr geehrte Frau Rabe,

Ihr Teilnahmeantrag nennt 100000 EUR bestehende Deckung für Schlüsselverlust. Gefordert sind 250000 EUR spätestens zum Leistungsbeginn; im Teilnahmeantrag genügt die verbindliche Versichererbestätigung über die mögliche Deckung im Auftragsfall. Bitte legen Sie genau diese Bestätigung bis 25.08.2026, 16:00 Uhr, im Nachrichtenbereich vor. Eine allgemeine Maklerauskunft, man werde sich darum kümmern, genügt nicht.

Die Anforderung betrifft den Versicherungsnachweis. Bitte reichen Sie damit kein vorgezogenes Preisangebot ein. Bei Problemen mit dem lesbaren Hochladen melden Sie sich vor Fristablauf über das Portal und sichern Sie die Fehlermeldung.

Mit freundlichen Grüßen
Malte Winter | Zentraler Einkauf
GVB Gemeinsame Verkehrsbetriebe Berlin AöR
Telefon 030 5550 1703"""),
    (14, "Versichererbestaetigung", "2026-08-25T10:08:00+02:00", "Carsten Voss <c.voss@havel-assekuranz.example>", "Nora Rabe <n.rabe@maerkischer-objektservice.example>", "Vertrag HA-20-4418: Deckung im Auftragsfall GVB Los 1", """Sehr geehrte Frau Rabe,

für die Märkischer Objektservice GmbH bestätigen wir verbindlich, dass wir im Fall der Zuschlagserteilung für GVB-REI-2026-017, Los 1, die Schlüsselverlustdeckung des Vertrags HA-20-4418 auf 250000 EUR je Versicherungsfall zum Leistungsbeginn 01.01.2027 erhöhen. Die bestehende Deckung von 5000000 EUR für Personen- und Sachschäden bleibt bestehen. Die Selbstbeteiligung bei Schlüsselverlust beträgt 1000 EUR.

Die Erhöhung setzt die Mitteilung des Zuschlags und des tatsächlichen Leistungsbeginns voraus; eine erneute Risikoprüfung ist für den beschriebenen Auftrag nicht erforderlich. Die Mehrprämie teilen wir Ihnen separat mit. Die Erklärung darf der GVB für dieses Vergabeverfahren vorgelegt werden. Sie ist keine Versicherungsbestätigung für andere Unternehmen einer Bietergemeinschaft.

Mit freundlichen Grüßen
Carsten Voss | Gewerbliche Haftpflicht
Havel-Assekuranz AG | Kaiserdamm 39, 14057 Berlin
Telefon 030 5550 6441"""),
    (15, "Angebotsaufforderung", "2026-08-26T09:15:00+02:00", "Vergabestelle <vergabestelle@gvb-berlin.example>", "Bieterkreis Los 1 <bewerberkreis@gvb-berlin.example>", "GVB-REI-2026-017: Aufforderung zur Angebotsabgabe Los 1", """Sehr geehrte Damen und Herren,

nach Abschluss der Teilnahmeprüfung fordern wir Sie zur Abgabe eines Erstangebots für Los 1 auf. Die Frist endet am 10.09.2026 um 12:00 Uhr. Verwenden Sie die Unterlagenfassung 2 einschließlich Antwort 07 vom 17.08.2026. Die Grundlaufzeit beträgt vier Jahre, hinzu kommt ein optionales Jahr. Das Portalpreisblatt enthält für die Wertung die jährlichen Mengen einschließlich Sonderabrufen. Bitte füllen Sie alle Einheitspreise aus, auch wenn Sie sich für eine Position keinen Abruf erwarten.

Beizufügen sind Ihr Ausführungskonzept und die geforderten Erklärungen. Reichen Sie das Angebot verschlossen über die Angebotsfunktion ein, nicht als offene Nachricht an den Einkauf. Eine Angebotsänderung ist bis zum Ablauf nur über dieselbe Funktion möglich. Die Bindefrist endet am 30.11.2026.

Die Verhandlungsgespräche sind für den 16.09.2026 vorgesehen. Sie erhalten jeweils einen eigenen Termin. Fragen sind über das Portal zu stellen. Die Ausschreibung von Los 2 und Los 3 wird in gesonderten Teilakten geführt; diese Einladung betrifft ausschließlich Los 1.

Mit freundlichen Grüßen
Malte Winter | Zentraler Einkauf
GVB Gemeinsame Verkehrsbetriebe Berlin AöR"""),
    (21, "Letzte_Angebotsrunde", "2026-09-17T09:00:00+02:00", "Vergabestelle <vergabestelle@gvb-berlin.example>", "Bieterkreis Los 1 <bewerberkreis@gvb-berlin.example>", "GVB-REI-2026-017: Abschließende Angebote bis 22.09.2026", """Sehr geehrte Damen und Herren,

die Verhandlungsgespräche sind abgeschlossen. Bitte reichen Sie Ihr abschließendes Angebot einschließlich der geänderten Konzeptteile bis 22.09.2026, 12:00 Uhr, über die Angebotsfunktion ein. Für alle drei eingeladenen Bieter gilt dieselbe Frist. Grundlage bleiben die veröffentlichten Mindestbedingungen, die Kriterien der Anlage W und die am 17.08.2026 geklärten Reinigungsfenster.

Bitte kennzeichnen Sie, welche Passagen des Erstkonzepts ersetzt werden. Wo Sie nichts ändern, bleibt Ihr bisheriger Text Bestandteil des Angebots. Preise sind vollständig in der neuen Preisblattfassung einzutragen; eine Nachricht „wie bisher mit Rabatt“ reicht für die Zuordnung nicht aus. Die Wertungsmengen bleiben unverändert. Nach dem Ablauf dieser Runde werden wir nicht weiter verhandeln.

Die geplanten sechs Wochen zur Mobilisierung bleiben im Terminplan. Eine Bestellung von Geräten auf eigenes Risiko vor Zuschlag ist keine Beauftragung durch die GVB.

Mit freundlichen Grüßen
Malte Winter | Zentraler Einkauf
GVB Gemeinsame Verkehrsbetriebe Berlin AöR"""),
    (25, "Interne_Rueckfrage_Wertung", "2026-09-25T16:07:00+02:00", "Silke Mertens <s.mertens@gvb-berlin.example>", "Malte Winter <m.winter@gvb-berlin.example>", "Los 1: Begründungen im Bewertungsbogen", """Hallo Malte,

ich habe deine Versandkopie gesehen. In meiner Datei standen bei den Konzepten noch Kommentare hinter den Punkten, nicht nur die Punkte selbst. Im Export vom Einkauf sehe ich die Kommentare nicht mehr. Jens hatte zum Vertretungspool noch einen telefonischen Hinweis, den wir nicht mit anderen Angaben vermischen sollten.

Kannst du die Arbeitsfassung vom 24. September sichern? Die Zahlenblätter mit der Preisrechnung liegen unter der Vergabenummer; meine eigentlichen Einzelbegründungen sind noch im freigegebenen Teamordner. Ich bin am Montag erst ab 10 Uhr im Haus. Bitte nichts rückwirkend auf heute datieren, falls wir noch etwas ergänzen müssen.

Gruß
Silke Mertens
Leitung Reinigung und Stationsservice | Telefon 030 5550 1714"""),
    (27, "Ruege_Eingang", "2026-09-28T09:42:00+02:00", "Vergabestelle <vergabestelle@gvb-berlin.example>", "Nils Faber <vergabe@maerkischer-objektservice.example>", "GVB-REI-2026-017: Eingang Ihrer Nachricht", """Sehr geehrter Herr Faber,

Ihre Rüge vom heutigen Tag ist um 09:34 Uhr im Portal eingegangen. Wir haben die Fachabteilung zur Stellungnahme aufgefordert und werden Ihnen über das Portal antworten. Eine Aussage zur Begründetheit oder eine Änderung des angekündigten Zuschlagstermins ist mit dieser Eingangsbestätigung nicht verbunden.

Bitte richten Sie ergänzende Unterlagen an denselben Vorgang, damit sie der richtigen Losakte zugeordnet werden. Die Abwesenheitsvertretung für Herrn Winter übernimmt Frau Mertens. Der Eingang wird in unserem Fristenkalender erfasst.

Mit freundlichen Grüßen
Lea Berger | Vergabeassistenz
GVB Gemeinsame Verkehrsbetriebe Berlin AöR
Köpenicker Straße 186, 10997 Berlin | Telefon 030 5550 1700"""),
    (32, "Aktenanforderung_intern", "2026-10-02T08:17:00+02:00", "Malte Winter <m.winter@gvb-berlin.example>", "Silke Mertens <s.mertens@gvb-berlin.example>", "Dringend: Unterlagen Los 1 nach Kammermitteilung", """Guten Morgen Silke,

die Nachricht der Vergabekammer ist gestern um 13:46 Uhr eingegangen. Ich habe die Bestellfreigabe in unserem Einkaufssystem gesperrt. Der Entwurf des Zuschlagsschreibens ist nicht versandt worden. Bitte gib auch an die Pforte weiter, dass keine Schlüsselübergabe an einen neuen Dienstleister veranlasst werden darf.

Wir brauchen jetzt deine Bewertungsnotizen in der ursprünglichen Fassung, die Zugangsfenster, die drei abschließenden Konzepte und den Nachweis, wann alle Bieter die Änderungen erhalten haben. Im Exportordner fehlen mir noch die vollständige EU-Veröffentlichungsquittung und die separaten Protokolle der Gespräche mit Märkischer und Nordlicht. Bitte sende nichts mit neuem Datum als angeblich alten Stand. Wenn etwas nicht vorhanden ist, sag mir das bitte ausdrücklich.

Die laufende Reinigung durch den bisherigen Dienstleister endet erst am 31. Dezember. Heute besteht deshalb keine betriebliche Lücke. Die Leitung möchte dennoch wissen, ob sich unser Übergabetermin verschiebt. Ich antworte erst nach Rücksprache mit der Rechtsabteilung.

Viele Grüße
Malte Winter | Zentraler Einkauf
GVB Gemeinsame Verkehrsbetriebe Berlin AöR | Durchwahl 1703"""),
]

TEXTS = {
    "19_Telefonnotiz_Personal.txt": """GVB | Zentraler Einkauf | GVB-REI-2026-017 | Los 1
Telefonnotiz von Lea Berger
15.09.2026, 11:47 bis 11:56 Uhr
Anrufer: Jens Ahrens, Stationsservice, Durchwahl 1721

Jens ruft aus dem Dienstwagen an. Er ist auf dem Weg nach Hermannstraße.
Er sagt, die drei Angebote hätten unterschiedliche Stundenansätze.
Er habe keine Kalkulation nachgerechnet. Er wolle nur vermeiden, dass
wir wieder jemanden nachts vor verschlossenen Türen stehen lassen.

Zu den 90 Minuten: Der Schichtleiter darf keine Verlängerung versprechen.
Ein Team kann sich im Geräteraum vorbereiten, aber nicht schon vorher
mit der Maschine über den gesperrten Bereich fahren. An einem Standort
liegt der Geräteraum fünf Gehminuten vom Bahnsteig entfernt.

Jens fragt, ob die Bewerber alle die gleiche Ergänzung bekommen haben.
Ich verweise auf den Portalversand vom 17.08.2026. Abrufzeiten habe ich
während des Telefonats nicht geöffnet. Er bittet um Weitergabe an Malte.

11:58 Uhr: Weitergeleitet an Malte Winter, keine Preisangaben ergänzt.
Lea Berger
""",
    "31_Kammermitteilung.txt": """Vergabekammer des Landes Berlin
Elektronische Übermittlungsabschrift zur Vergabenummer GVB-REI-2026-017
01.10.2026, 13:42 Uhr | Eingang GVB 13:46 Uhr
An die GVB Gemeinsame Verkehrsbetriebe Berlin AöR, Zentraler Einkauf

Nachprüfungsantrag der Märkischer Objektservice GmbH, Los 1

Sehr geehrte Damen und Herren,

anliegend übermitteln wir den am heutigen Tag eingegangenen
Nachprüfungsantrag nebst Anlagen. Wir weisen auf das gesetzliche
Zuschlagsverbot nach Paragraf 169 Absatz 1 GWB hin.

Bitte übersenden Sie die vollständige Vergabeakte elektronisch und
geordnet sowie Ihre Stellungnahme bis zum 06.10.2026, 12:00 Uhr.
Kennzeichnen Sie Unterlagen, die Geschäftsgeheimnisse enthalten,
konkret und begründen Sie den Schutzbedarf. Reichen Sie erforderlichenfalls
eine zusätzlich geschwärzte Fassung ein. Eine pauschale Kennzeichnung
der gesamten Vergabeakte als vertraulich ist nicht ausreichend.

Bitte bestätigen Sie den Zugang dieser Mitteilung noch heute und teilen
Sie mit, ob bereits ein Zuschlag erteilt wurde. Sollte die elektronische
Übermittlung einzelner Dateien technisch nicht möglich sein, stimmen
Sie den Übermittlungsweg rechtzeitig mit der Geschäftsstelle ab.

Mit freundlichen Grüßen
Für die Geschäftsstelle: K. Rehberg

Übermittlungsvermerk GVB: Eingang bestätigt 01.10.2026, 14:03 Uhr.
Mitgeteilt: Zuschlag noch nicht erteilt. Bearbeiter Malte Winter.
""",
    "33_Stationsservice_Chat.txt": """Chat-Export | GVB Stationsservice | Kanal Übergabe Reinigung
Zeitzone Europe/Berlin | Export: 02.10.2026, 09:10 Uhr
Teilnehmer: Jens Ahrens, Silke Mertens, Mehmet Demir

21.07.2026 08:13 | Jens Ahrens
Habe das alte Aufmaß gefunden. Bei Adlergestell steht 780, aber auf der
letzten Rechnung 1560. Muss ich noch messen. Die Ladenfront ist da mit drin.

21.07.2026 08:19 | Silke Mertens
Danke. Bitte nicht einfach die Rechnung übernehmen. Die Bäckerei putzt
ihre Scheiben selbst. Bei uns bleiben der Personalzugang und die Fassade.

22.07.2026 16:05 | Mehmet Demir
Noch zur Begehung: Keine Gleisquerung für das Reinigungsteam. Auch nicht
nach Betriebsschluss. Bitte ausdrücklich in die Einweisung aufnehmen.

11.08.2026 07:31 | Jens Ahrens
Jetzt Bestätigung der Leitstelle: 00:45 bis 02:15 in Hermannstraße und
Neukölln. Habe Malte geschrieben. Mit drei Stunden können wir nicht planen.

01.10.2026 14:24 | Silke Mertens
Einkauf hat die Freigabe gesperrt. Keine Schlüssel für den Nachfolger
ausgeben. Der bisherige Dienst läuft normal weiter.

02.10.2026 08:51 | Jens Ahrens
Verstanden. Pforte weiß Bescheid. Der Raum ist ohnehin noch voller
Ersatzteile. Ich räume den bis zum vorgesehenen Übergabetermin frei.
""",
}

document(35, "Abschliessendes_Konzept_Spreeklar", SPREE, "GVB | Zentraler Einkauf | Los 1", "22.09.2026", "Abschließendes Angebot und geänderte Einsatzplanung", """
Sehr geehrter Herr Winter,

wir geben unser abschließendes Angebot ab. Der Grundpreis beträgt 748000 EUR netto pro Jahr, die Sondermengen betragen 28000 EUR netto pro Jahr. Der Wertungspreis beträgt für fünf Jahre 3880000 EUR netto. Diese Preise ersetzen die Beträge unseres Erstangebots vollständig. Die Preisbindung bis 30.11.2026 bleibt bestehen.

Das nachfolgende Konzept ersetzt die Abschnitte 1 und 3 des Erstkonzepts. Abschnitt 2 bleibt bestehen, soweit die jetzt fest vereinbarte Vertretung abweichend beschrieben wird. Wir berücksichtigen das Reinigungsfenster 00:45 bis 02:15 Uhr für die zusammenhängende Nassreinigung in Hermannstraße und Neukölln. Je Station werden in diesem Fenster vier Beschäftigte parallel eingesetzt. Vorbereitung erfolgt nur im dafür freigegebenen Materialbereich. Außerhalb des Fensters werden ausschließlich die nach den Unterlagen zulässigen Teilflächen bearbeitet; eine verlängerte Sperrung ist keine Voraussetzung unseres Angebots.

Wir kalkulieren nun 26400 produktive Stunden je Jahr. Davon entfallen 13200 auf die beiden Stationen, 10200 auf die übrigen Regelobjekte und 3000 auf die im Grundauftrag enthaltenen Kontrollen, Rüst- und Vertretungsleistungen. Die im Preisblatt gesondert bewerteten Sonderabrufe gehören nicht zu diesen 26400 Stunden. Der Pool besteht aus vier eingewiesenen Beschäftigten mit schriftlich reservierten Zeitanteilen. Bei zwei gleichzeitigen Ausfällen ruft der Objektleiter zwei verschiedene Poolmitarbeiter ab; eine Doppelbelegung derselben Person ist nicht vorgesehen.

Tobias Krüger führt die Disposition und Elena Sander vertritt ihn. Die Schichtlisten dokumentieren für jeden Mitarbeiter Objekt, Beginn, Ende und den tatsächlich geleisteten Einsatz. Bei fehlendem Zutritt erfolgt eine Meldung an die Leitstelle und ein gesonderter Vermerk. Eine bloße Anwesenheit an der Pforte ersetzt den Leistungsnachweis nicht. Die täglichen Objektkontrollen werden mit der Wochenkontrolle abgeglichen; die GVB erhält nur die für ihren Leistungsnachweis erforderlichen Angaben.

Den Geräteraum nutzen wir erst nach protokollierter Übergabe. Die Schlüssel werden ausschließlich an die benannten Objektverantwortlichen ausgegeben. Sollte sich der Zugang zur Mobilisierung verzögern, stimmen wir eine Zwischenlagerung ab, ohne einen früheren Leistungsbeginn zu behaupten. Eine abweichende Mindestanforderung oder eine Änderung der veröffentlichten Bewertungsmaßstäbe verlangen wir nicht.
""", "Mit freundlichen Grüßen\nHenrik Seidel\nGeschäftsführer\nPortaleingang: 22.09.2026, 10:34:18 Uhr")

document(36, "Abschliessendes_Angebot_Maerkischer", MARK, "GVB | Zentraler Einkauf | Los 1", "22.09.2026", "Abschließendes Angebot nach dem Verhandlungsgespräch", """
Sehr geehrter Herr Winter,

unser abschließender Grundpreis beträgt 771000 EUR netto pro Jahr. Die Sondermengen bleiben bei 31000 EUR netto jährlich. Der Wertungspreis für vier Jahre und das optionale fünfte Jahr beträgt 4010000 EUR netto. Diese Preisangaben ersetzen die Preise im Schreiben vom 10.09.2026. Die Reduzierung des Grundpreises um 5000 EUR pro Jahr beruht auf einer günstigeren Gerätemiete, nicht auf einer Reduzierung der Stunden oder der Vertretungsreserve.

Unser Konzept vom 10.09.2026 bleibt mit 28600 produktiven Stunden pro Jahr bestehen. Im Gespräch am 16.09.2026 haben wir klargestellt, dass die Springer nicht nur im Krankheitsfall, sondern auch während planmäßigen Urlaubs verfügbar sind. Der Pool umfasst sechs Beschäftigte mit zeitlich begrenzter Zuordnung zu diesem Auftrag; pro Schicht werden mindestens zwei unterschiedliche Ersatzpersonen verfügbar gehalten. Wege zwischen den Objekten sind in der Disposition berücksichtigt. Die Einsatzliste wird vor Leistungsbeginn mit den örtlichen Zugangsberechtigungen abgeglichen.

Eine verbindliche Antwort auf unsere Frage zur Lagerfreigabe am 16.11.2026 steht noch aus. Wie bereits angeboten, machen wir davon weder Preis noch Leistung abhängig. Bei späterer Übergabe lagern wir die Geräte zunächst auf unserem Betriebshof. Die GVB soll uns nur einen belastbaren Termin mitteilen, bevor wir die Lieferungen disponieren.

Wir bestätigen sämtliche bisher abgegebenen Verpflichtungserklärungen. Der Versicherungsnachweis für Schlüsselverlust bleibt gültig. Wir bieten keine Nachverhandlung der veröffentlichten Mindestbedingungen an und erklären die Preisbindung bis 30.11.2026. Die Übermittlung dieser Datei und des ausgefüllten Preisblatts ist um 11:02:45 Uhr im Portal quittiert worden.
""", "Mit freundlichen Grüßen\nNils Faber\nGeschäftsführer")

document(37, "Abschliessendes_Angebot_Nordlicht", NORD, "GVB | Zentraler Einkauf | Los 1", "22.09.2026", "Abschließendes Angebot zur Stationsreinigung", """
Sehr geehrter Herr Winter,

wir legen unseren abschließenden Grundpreis auf 801000 EUR netto pro Jahr fest. Die Sondermengen bleiben mit 32000 EUR netto pro Jahr unverändert. Der Wertungspreis über fünf Jahre beträgt 4165000 EUR netto. Der Grundpreis ist gegenüber dem Erstangebot um 7000 EUR pro Jahr reduziert. Hintergrund ist die gebündelte Beschaffung der benötigten Geräte zusammen mit einem weiteren Auftrag; eine Mitbenutzung desselben Geräts zur selben Zeit ist nicht vorgesehen.

Das Ausführungskonzept vom 10.09.2026 mit 29200 produktiven Stunden bleibt bestehen. Die drei kleinen Teams erhalten getrennte Gerätesätze, sodass kein nächtlicher Transport zwischen Hermannstraße und Neukölln erforderlich ist. Der diensthabende Einsatzleiter nimmt Störungen persönlich an. Bei einem kurzfristigen Personalengpass werden die dafür reservierten Mitarbeiter aus unserem Betriebshof eingesetzt, nicht Beschäftigte aus einer bereits voll verplanten Nachtschicht.

Die im Gespräch angesprochene monatliche Qualitätsbegehung kann gemeinsam mit Ihrem Stationsservice durchgeführt werden. Unsere wöchentlichen Eigenkontrollen bleiben zusätzlich bestehen. Die Dokumentation nennt Objekt, Datum, Zeit und konkrete Fläche. Bei verschlossenem Zugang wird ein eigener Vorgang angelegt; die übrigen ausgeführten Leistungen werden davon getrennt abgerechnet.

Wir bestätigen die Unterlagenfassung 2 und sämtliche veröffentlichten Antworten. Es bestehen keine Nebenangebote oder Bedingungen, die erst nach Zuschlag vereinbart werden müssten. Die Bindefrist endet am 30.11.2026. Den Portaleingang um 09:56:02 Uhr haben wir gesichert.
""", "Mit freundlichen Grüßen\nDaniel Lindner\nGeschäftsführer")

CSVS = {
    "02_Objektliste_17_07.csv": [
        ["Objekt", "Bereich", "Los", "Menge", "Einheit", "Durchgänge/Jahr", "Stand"],
        ["Hermannstraße", "Bahnsteig und Zugang", 1, 4200, "m²", 365, "17.07.2026"],
        ["Neukölln", "Bahnsteig und Zugang", 1, 3800, "m²", 365, "17.07.2026"],
        ["Busbereich Treptower Park", "Personalräume", 1, 720, "m²", 260, "17.07.2026"],
        ["Betriebshof Adlergestell", "Personal und Sanitärräume", 1, 1480, "m²", 365, "17.07.2026"],
        ["Betriebshof Adlergestell", "Verwaltung ohne Laden", 1, 2100, "m²", 260, "17.07.2026"],
        ["Busbestand Teilnetz", "Innenreinigung Standard", 2, 96, "Fahrzeuge", 300, "17.07.2026"],
        ["Straßenbahnbestand Teilnetz", "Innenreinigung Standard", 2, 28, "Fahrzeuge", 300, "17.07.2026"],
        ["U-Bahn-Bestand Teilnetz", "Innenreinigung Einheit", 2, 24, "Einheiten", 300, "17.07.2026"],
        ["Dienstgebäude Adlergestell", "Südfassade einfache Fläche", 3, 780, "m²", 4, "17.07.2026"],
        ["Stationen zusammen", "Übrige Glasflächen zweiseitig", 3, 1860, "m²", 4, "17.07.2026"],
    ],
    "03_Kostenansatz_Finanzen.csv": [
        ["Los", "Position", "Jahr_EUR_netto", "Jahre", "Gesamt_EUR_netto", "Quelle"],
        [1, "Unterhaltsreinigung", 780000, 5, 3900000, "Planansatz Finanzen 20.07.2026"],
        [2, "Fahrzeugreinigung", 480000, 5, 2400000, "Planansatz Betrieb 20.07.2026"],
        [3, "Glasreinigung", 64000, 5, 320000, "Planansatz Immobilien 20.07.2026"],
        [1, "Sonderabrufe Stationen", 24000, 5, 120000, "Bedarfsanmeldung 20.07.2026"],
        [2, "Sonderabrufe Fahrzeuge", 44000, 5, 220000, "Bedarfsanmeldung 20.07.2026"],
        [3, "Sonderabrufe Glas", 8000, 5, 40000, "Bedarfsanmeldung 20.07.2026"],
    ],
    "22_Abschliessende_Preisangaben.csv": [
        ["Bieter", "Position", "Jahr_EUR_netto", "Jahre", "Gesamt_EUR_netto", "Eingang_22_09_2026"],
        ["Spreeklar", "Grundpreis", 748000, 5, 3740000, "10:34:18"],
        ["Spreeklar", "Sondermengen", 28000, 5, 140000, "10:34:18"],
        ["Märkischer Objektservice", "Grundpreis", 771000, 5, 3855000, "11:02:45"],
        ["Märkischer Objektservice", "Sondermengen", 31000, 5, 155000, "11:02:45"],
        ["Nordlicht", "Grundpreis", 801000, 5, 4005000, "09:56:02"],
        ["Nordlicht", "Sondermengen", 32000, 5, 160000, "09:56:02"],
    ],
    "34_Portalprotokoll.csv": [
        ["Datum", "Uhrzeit", "Vorgang", "Empfänger", "Nachweis"],
        ["24.07.2026", "09:12:00", "Datensatz zur Veröffentlichung versandt", "Publikationsdienst", "GVB-PUB-240726-017"],
        ["17.08.2026", "10:00:00", "Antwort 07 bereitgestellt", "Alle registrierten Bewerber", "MSG-071"],
        ["17.08.2026", "10:07:12", "Antwort 07 abgerufen", "Spreeklar", "READ-071-1"],
        ["17.08.2026", "10:11:43", "Antwort 07 abgerufen", "Märkischer Objektservice", "READ-071-2"],
        ["17.08.2026", "11:20:15", "Antwort 07 abgerufen", "Nordlicht", "READ-071-3"],
        ["25.08.2026", "10:42:00", "Versichererbestätigung eingegangen", "GVB Einkauf", "UP-083"],
        ["26.08.2026", "09:15:00", "Angebotsaufforderung versandt", "Drei geeignete Bewerber Los 1", "MSG-091"],
        ["17.09.2026", "09:00:00", "Letzte Angebotsrunde eröffnet", "Drei Bieter Los 1", "MSG-138"],
        ["25.09.2026", "15:18:00", "Vorabinformation versandt", "Märkischer Objektservice", "MSG-163"],
        ["25.09.2026", "15:31:00", "Vorabinformation abgerufen", "Märkischer Objektservice", "READ-163"],
        ["28.09.2026", "09:34:00", "Rüge eingegangen", "GVB Einkauf", "UP-172"],
        ["30.09.2026", "14:22:00", "Nichtabhilfe versandt", "Märkischer Objektservice", "MSG-184"],
        ["30.09.2026", "14:37:00", "Nichtabhilfe abgerufen", "Märkischer Objektservice", "READ-184"],
        ["01.10.2026", "13:46:00", "Kammermitteilung eingegangen", "GVB Einkauf", "POST-201"],
        ["01.10.2026", "14:03:00", "Eingang Kammermitteilung bestätigt", "Vergabekammer", "POST-202"],
    ],
    "38_Leistungsverzeichnis_Preisblatt.csv": [
        ["Position", "Leistung", "Einheit", "Menge_Jahr", "EP_EUR_netto", "Zuordnung"],
        ["1.01", "Hermannstraße Boden und Zugang", "m² je Durchgang", 1533000, "", "Los 1 Grundauftrag"],
        ["1.02", "Neukölln Boden und Zugang", "m² je Durchgang", 1387000, "", "Los 1 Grundauftrag"],
        ["1.03", "Treptower Park Personalräume", "m² je Durchgang", 187200, "", "Los 1 Grundauftrag"],
        ["1.04", "Adlergestell Personal und Sanitär", "m² je Durchgang", 540200, "", "Los 1 Grundauftrag"],
        ["1.05", "Adlergestell Verwaltung ohne Laden", "m² je Durchgang", 546000, "", "Los 1 Grundauftrag"],
        ["1.06", "Störungsannahme und Objektleitung", "Monat", 12, "", "Los 1 Grundauftrag"],
        ["1.07", "Material und Gerätevorhaltung", "Monat", 12, "", "Los 1 Grundauftrag"],
        ["1.91", "Sonderreinigung werktags tagsüber", "Stunde", 400, "", "Los 1 Sondermenge zur Wertung"],
        ["1.92", "Sonderreinigung nachts", "Stunde", 200, "", "Los 1 Sondermenge zur Wertung"],
        ["1.93", "Sonderreinigung Sonn und Feiertag", "Stunde", 100, "", "Los 1 Sondermenge zur Wertung"],
    ],
}
