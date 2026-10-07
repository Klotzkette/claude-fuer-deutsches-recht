---
name: zahlungen-buchhaltung
description: "Verwenden, wenn Zahlungseingänge, Vorschüsse, Drittzahlungen, Kostenerstattungen oder Fremdgeld belegt zugeordnet, Teilzahlungen verrechnet, Zahlungen gemahnt oder Buchungsvorschläge für die Finanzbuchhaltung erstellt werden sollen. Liefert Zahlungsklärung. Nicht für Rechnung oder Honorarvereinbarung."
---

# Zahlungen zuordnen und Buchhaltung vorbereiten

## 1. Zweck und Anwendungsfall

### 1.1. Jeder Geldfluss erhält einen belegten Rechtsgrund

Dieser Skill verarbeitet konkrete Zahlungsbelege und erstellt daraus einen nachvollziehbaren Zuordnungs- und Buchungsvorschlag. Er unterscheidet Geldbewegung, Forderung, wirtschaftliche Berechtigung, steuerlichen Tatbestand und buchhalterische Erfassung. Ein Zahlungseingang auf einem Kanzleikonto ist nicht automatisch Honorar, und eine Rechnung ist nicht bezahlt, weil ein gleich hoher Betrag eingeht. Eine Zahlung der Gegenseite kann Hauptforderung, Zinsen, Kosten oder einen Vergleichsbetrag betreffen und wird entsprechend aufgeschlüsselt.

Das Verfahren beginnt beim Beleg und endet mit einem prüfbaren Vorschlag, einer abgeschlossenen Klärung oder einer im Auftrag tatsächlich ausgeführten Buchung. Das lokale Mandatsjournal ist kein Hauptbuch; es dokumentiert Zahlungen gesondert und verrechnet sie nicht mit Honorar.

### 1.2. Fremdgeld hat einen eigenständigen Schutzstatus

Fremde Gelder werden unverzüglich an den Empfangsberechtigten weitergeleitet oder auf ein Anderkonto eingezahlt; maßgeblich ist zum dokumentierten Rechtsstand [§ 43a Absatz 7 BRAO](https://www.gesetze-im-internet.de/brao/__43a.html), konkretisiert durch § 4 BORA. Die alte Absatznummer aus historischen Entscheidungen wird nicht in aktuelle Handlungsempfehlungen übernommen.

Eine Verrechnung von Honorar mit einem Herausgabeanspruch auf Fremdgeld ist keine Routinefunktion, sondern braucht eine gesonderte zivilrechtliche, berufsrechtliche und gegebenenfalls insolvenzrechtliche Prüfung von Zweckbindung, Drittberechtigung, Aufrechnungslage, Verboten und Erklärung.

### 1.3. Auslöser, Abgrenzung und Nachbarskills

Starte diesen Skill, wenn ein Kontoauszug einen Eingang zeigt, dessen Rechtsgrund nicht aus dem Verwendungszweck folgt. Starte ihn, wenn ein Rechtsschutzversicherer gesetzliche Gebühren überweist und die Differenz zur vereinbarten Vergütung offen bleibt, wenn eine Vergleichssumme oder eine Kostenerstattung der Gegenseite auf dem Geschäftskonto statt auf dem Anderkonto eingeht, wenn ein Vorschuss mit einer Schlussrechnung verrechnet werden soll, wenn eine Rücklastschrift eine als bezahlt geführte Rechnung wieder öffnet oder wenn Buchhaltung oder Steuerberatung den Monatsabgleich mit Buchungsvorschlägen verlangen.

Die Rechnung selbst, ihre Pflichtangaben nach § 10 RVG und das XRechnungsformat erstellt [Abrechnung und E-Rechnung](../abrechnung-e-rechnung/SKILL.md). Die Honorargrundlage eines Vorschusses oder einer Verrechnung klärt [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md); Zeiteinträge pflegt [Zeiten erfassen](../zeiten-erfassen/SKILL.md). Die Schlussabrechnung mit Fremdgeldausgleich und Aufbewahrungsentscheidung führt [Mandat abschließen](../mandat-abschliessen/SKILL.md). Eine streitige berufsrechtliche Bewertung eines Einbehalts geht an [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md). Barzahlungen oder Zahlungen aus unbeteiligten Quellen lösen zusätzlich [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md) aus. Mandantenbriefe über die reine Zahlungsklärung hinaus formuliert [Mandantenkommunikation](../mandantenkommunikation/SKILL.md).

Dieser Skill führt keine Finanzbuchhaltung, erstellt keine Umsatzsteuervoranmeldung, ersetzt keine Steuerberatung und gibt keine Zahlungen frei.

## 2. Eingaben

### 2.1. Zahlungsbeleg und Gegenbelege

Benötigt werden Konto, Buchungsdatum, Wertstellung, Betrag, Währung, Zahlender, Verwendungszweck und eine eindeutige Transaktionsreferenz; ergänzend Rechnung, Mandatsvereinbarung, Vorschussanforderung, Kostenfestsetzungsbeschluss, Vergleich oder Zahlungsankündigung. Erhalte den unveränderten Originalbeleg. Ein aus einer E-Mail abgeschriebener Betrag ist allenfalls eine Ankündigung und beweist keinen Eingang.

Prüfe, ob derselbe Umsatz bereits erfasst wurde; eine identische Summe an zwei Tagen kann zwei Zahlungen oder eine Korrekturbuchung betreffen. Ein Zahlungsdienstleister kann Gebühren einbehalten, sodass der Geldeingang von der Tilgungsleistung abweicht; die Differenz wird anhand der Abrechnung geklärt, nicht als Honorarreduzierung behandelt.

### 2.2. Honorarstand und Rechnungsbezug

Halte bei jedem wesentlichen Schritt den gespeicherten Honorarstand (Modell, Satz/Betrag, Umfang, Deckel, netto/brutto) knapp vor: „Die Rechnung R-2026-41 beruht auf dem bestätigten Festpreis von 1.800 Euro netto. Der Zahlungseingang beträgt 2.142 Euro und trägt diese Rechnungsnummer.“ Sind Honorarstand, Rechnung und Betrag eindeutig, wird nicht erneut nach dem Vergütungsmodell gefragt; fehlt eine Zuordnung, kläre nur die konkrete Lücke.

Ist die Vergütungsbasis selbst ungeklärt, frage nach RVG, Zeithonorar, Festpreis, verbindlichem Fee Quote oder Schätzung mit oder ohne Deckel sowie Netto- oder Bruttobezug. Eine Zahlung wird nicht als Zustimmung zu einer unklaren Honorarvereinbarung behandelt. Die Zuordnung bereits belegter Zahlungen kann unabhängig davon vorbereitet werden.

### 2.3. Buchhalterischer und steuerlicher Rahmen

Kläre Gewinnermittlungsart, Umsatzsteuerverfahren, Kontenrahmen, Buchungsperiode und zuständige Buchhaltung. Einnahmenüberschussrechnung und Bilanzierung, Soll- und Istbesteuerung folgen unterschiedlichen zeitlichen Regeln; die Bezeichnung einer Zahlung als „Vorschuss“ beantwortet diese Fragen nicht.

Der Skill benötigt nur die für den Vorgang erforderlichen Daten; vollständige Bankumsätze aller Mandanten werden nicht ohne Anlass an externe Werkzeuge übertragen. Prüfe Geheimniszugang und Datenschutzrolle des Buchhaltungsdienstleisters nach § 43e BRAO und Artikel 28 DSGVO getrennt; ein Auftragsverarbeitungsvertrag ersetzt nicht jede berufsrechtliche Voraussetzung.

### 2.4. Entscheidende Angaben im Überblick

| Angabe | Warum entscheidend | Vorgehen, wenn sie fehlt |
|---|---|---|
| Kontoauszug mit Transaktionsreferenz | Nur der Beleg beweist den Eingang und verhindert Doppelerfassung | Keine Zuordnung; Ankündigung als unbestätigt führen |
| Zahlender und Verwendungszweck | Trennt Mandant, Drittzahler und Gegner; erster Tilgungshinweis | Beleg lesen; bei Unklarheit Zahlungsklärung entwerfen |
| Wirtschaftlich Berechtigter | Entscheidet zwischen Honorar, Vorschuss und Fremdgeld | Fremdgeldroute vorsorglich eröffnen, nicht vereinnahmen |
| Rechnung oder Vorschussanforderung | Ohne Forderung gibt es keine Tilgung | Als ungeklärt separieren; Honorarskill einbinden |
| Tilgungsbestimmung des Schuldners | Geht nach § 366 Absatz 1 BGB der gesetzlichen Reihenfolge vor | Gesetzliche Reihenfolge nur bei fehlender Bestimmung anwenden |
| Vergleichs- oder Titelwortlaut | Verteilt den Betrag auf Hauptforderung, Zinsen und Kosten | Vermerk ohne Aufteilung; Text anfordern |
| Deckungszusage des Rechtsschutzversicherers | Bestimmt Umfang, Selbstbehalt und Restforderung | Differenz nicht dem Mandanten zuweisen; Zusage anfordern |
| Umsatzsteuerverfahren der Kanzlei | Soll- oder Istversteuerung verschiebt den Steuerzeitpunkt | Buchungsvorschlag mit offenem Steuerzeitpunkt kennzeichnen |
| Gewinnermittlungsart | EÜR und Bilanz behandeln Jahreswechsel verschieden | Periode offen lassen; Buchhaltung fragen |
| Kontenrahmen und Konto des Anderkontos | Buchungsvorschlag braucht reale Konten | Kategorien statt Kontonummern nennen |
| Insolvenzstand des Mandanten | Entscheidet über Masse, Anfechtung und Aufrechnung | Bei Anzeichen keine Verrechnung; Verwalter ermitteln |
| Bankverbindung für Rückzahlung oder Weiterleitung | Falsche Auszahlung ist nicht rückholbar | Bestätigung auf zweitem Weg einholen |

### 2.5. Rückfragen in der richtigen Reihenfolge

Stelle die Fragen in dieser Reihenfolge und nur, soweit die Akte sie nicht beantwortet. Erste Frage: „Liegt der Kontoauszug mit Transaktionsreferenz vor, oder handelt es sich um eine Zahlungsankündigung?“ Zweite Frage: „Für wen ist der Betrag wirtschaftlich bestimmt: für die Kanzlei als Honorar oder Vorschuss, für den Mandanten oder für einen Dritten?“ Dritte Frage: „Auf welche Rechnung oder Vorschussanforderung soll die Zahlung nach Verwendungszweck oder ausdrücklicher Bestimmung des Zahlenden entfallen?“ Vierte Frage: „Gilt die gespeicherte Honorargrundlage für diesen Vorgang unverändert?“ Fünfte Frage: „Versteuert die Kanzlei nach vereinbarten oder nach vereinnahmten Entgelten, und welcher Kontenrahmen wird verwendet?“ Sechste Frage: „Gibt es Anzeichen für Insolvenz, Pfändung oder einen Streit um die Berechtigung?“

Ohne Antwort auf die erste Frage wird nur die Ankündigung dokumentiert. Ohne Antwort auf die zweite wird der Betrag separiert und die Fremdgeldroute vorsorglich eröffnet, weil eine verspätete Weiterleitung schwerer wiegt als eine verspätete Honorarbuchung. Ohne Antwort auf die dritte bis fünfte Frage entstehen Zuordnungsvermerk mit offenen Feldern, Zahlungsklärung an den Mandanten und Journaleintrag mit `confirmed=false`. Ohne Antwort auf die sechste unterbleibt jede Verrechnung.

## 3. Ablauf und Checkliste

### 3.1. Entscheidungsbaum für einen Zahlungseingang

Stelle zuerst fest, ob der Eingang gebucht oder nur angekündigt ist. Dann prüfe, für wen der Betrag wirtschaftlich bestimmt ist: für den Mandanten oder einen Dritten (Fremdgeldroute), zur Begleichung einer Kanzleiforderung (Rechnung und Tilgungsbestimmung) oder für künftige Leistungen (Vorschussroute). Bleibt der Zweck unklar, wird der Betrag separiert und eine gezielte Klärung vorbereitet.

Im zweiten Schritt wird die Höhe abgeglichen: Vollzahlung, Teilzahlung, Überzahlung, Doppelzahlung und Sammelzahlung. Im dritten Schritt wird die steuerliche Behandlung anhand des Rechtsgrunds bestimmt. Erst danach entsteht ein Buchungsvorschlag, damit eine zufällig passende Summe die rechtliche Einordnung nicht ersetzt.

### 3.2. Tilgungsbestimmung und mehrere Forderungen

Erfüllung tritt nach § 362 Absatz 1 BGB ein, wenn die geschuldete Leistung an den Gläubiger bewirkt wird. Hat der Schuldner bei mehreren Forderungen bestimmt, auf welche Schuld er leistet, ist diese Bestimmung nach § 366 Absatz 1 BGB maßgeblich. Fehlt sie, gilt die gesetzliche Reihenfolge des § 366 Absatz 2 BGB: zunächst die fällige Schuld, unter mehreren fälligen die mit geringerer Sicherheit, unter gleich sicheren die dem Schuldner lästigere, unter gleich lästigen die ältere und bei gleichem Alter jede verhältnismäßig. Innerhalb einer Schuld verteilt § 367 Absatz 1 BGB eine nicht ausreichende Zahlung zunächst auf Kosten, dann auf Zinsen und zuletzt auf die Hauptleistung; eine abweichende Bestimmung des Schuldners kann der Gläubiger nach § 367 Absatz 2 BGB ablehnen. Der Buchungsvorschlag nennt die angewandte Reihenfolge und ihre Tatsachengrundlage.

Ein Verwendungszweck „Rechnung 41“ ist ein stärkerer Zuordnungshinweis als die Übereinstimmung mit einer offenen Gesamtsumme. Bei einer Sammelzahlung mit mehreren Rechnungsnummern wird die Aufteilung anhand der Zahlungsavisdatei nachvollzogen; fehlt sie, wird nicht automatisch die älteste Forderung als getilgt markiert, wenn gegenläufige Angaben vorliegen. Prüfe zudem, ob Zinsen und Kosten tatsächlich geschuldet sind; eine unberechtigte Mahngebühr wird nicht dadurch berechtigt, dass sie im offenen Posten steht.

### 3.3. Drittzahlungen und Rechtsschutzversicherung

Nach § 267 Absatz 1 BGB kann auch ein Dritter die Leistung bewirken, wenn der Schuldner nicht in Person zu leisten hat; der Dritte wird dadurch nicht Vertragspartner. Erfasse Zahlenden und Leistungsempfänger getrennt. Bei einer Rechtsschutzversicherung werden Schadennummer, Mandat, Rechnung, Deckungsumfang und Selbstbehalt abgeglichen. Eine Differenz zwischen gezahlten gesetzlichen Gebühren und vereinbarter Vergütung wird anhand der Vereinbarung, des Hinweises nach § 3a Absatz 1 Satz 3 RVG und der tatsächlichen Deckung erläutert, nicht pauschal dem Mandanten aufgebürdet.

Bei Zahlung durch Arbeitgeber, Konzernmutter oder Familienangehörige hängt ein Rückforderungsanspruch von der konkreten Leistungsbeziehung ab; die ursprüngliche Zahlstelle ist ein Hinweis, nicht die Antwort. Ein externer Zahlender erhält nicht die vertrauliche Mandatsabrechnung, sondern nur die für die Zuordnung erforderlichen Angaben. Deckungsfragen, Schweigepflichtentbindung und Mandantenauftrag bleiben getrennte Prüfpunkte.

### 3.4. Kostenerstattung durch die Gegenseite und Kostenfestsetzung

Eine Zahlung der Gegenseite auf einen Kostenfestsetzungsbeschluss nach §§ 103, 104 ZPO erfüllt den prozessualen Kostenerstattungsanspruch des Mandanten, nicht die Honorarforderung der Kanzlei. Der Betrag ist deshalb Fremdgeld, auch wenn er die Anwaltsgebühren wirtschaftlich abbildet. Ob er mit einer offenen Honorarforderung verrechnet werden darf, folgt aus Mandatsvereinbarung, Abtretung oder Einziehungsermächtigung und den Grenzen des § 4 BORA, nicht aus dem Beschluss. Nach § 104 Absatz 1 Satz 2 ZPO ist der festgesetzte Betrag ab Eingang des Festsetzungsantrags zu verzinsen; Zinssatz und die Erklärung zur Vorsteuerabzugsberechtigung nach § 104 Absatz 2 ZPO sind am Volltext zu prüfen, bevor Zinsanteile zugeordnet werden.

Ein Verwendungszweck „Kosten gemäß KFB“ nennt den Grund, nicht den Berechtigten. Hat der Mandant die Gebühren bereits bezahlt, ist die Erstattung an ihn weiterzuleiten; hat er noch nicht bezahlt, bleibt der Betrag Fremdgeld, bis die Verrechnungsvoraussetzungen dokumentiert sind. Erstattet die Gegenseite weniger als festgesetzt, wird die Differenz als offener Erstattungsrest des Mandanten geführt, nicht als Honorarausfall.

### 3.5. Vorschüsse und spätere Verrechnung

Nach § 9 RVG kann der Rechtsanwalt für entstandene und voraussichtlich entstehende Gebühren und Auslagen einen angemessenen Vorschuss fordern. Ein Vorschuss ist weder verdientes Honorar noch Fremdgeld; bestimme Rechtsgrund, Zweckbindung und umsatzsteuerliche Behandlung. Im inländischen steuerpflichtigen Standardfall löst die Vereinnahmung vor Leistungsausführung nach § 13 Absatz 1 Nummer 1 Buchstabe a UStG mit Ablauf des Voranmeldungszeitraums der Vereinnahmung Umsatzsteuer aus; die genaue Satzfolge ist am Volltext zu prüfen. Eine bloß gestellte Vorschussrechnung ist keine vereinnahmte Vorauszahlung.

Bei der Schlussabrechnung werden zugeordnete Vorschüsse berücksichtigt; § 10 Absatz 2 RVG verlangt ihre Angabe in der Berechnung. Ein Vorschuss von 1.190 Euro brutto entspricht bei feststehendem Satz von 19 Prozent 1.000 Euro netto und 190 Euro Steuer; diese Rechnung gilt nicht für Auslands- oder Kleinunternehmerfälle. Die Verrechnung erfolgt mit geeignetem Rechnungswerkzeug; [`xrechnung.py`](../../scripts/xrechnung.py) unterstützt sie nicht.

Ist das Mandat beendet, wird ein nicht verbrauchter Vorschuss abgerechnet und zurückgezahlt; die Schlussaufstellung enthält Ausgangsvorschuss, verwendeten Betrag, begründete Restforderung oder Rückzahlungsbetrag und die Belege.

### 3.6. Fremdgeld erkennen, auf das Anderkonto nehmen und unverzüglich weiterleiten

Typische Fremdgeldindikatoren sind Zahlungen auf die Hauptforderung des Mandanten, Vergleichssummen, Kostenerstattungen der Gegenseite, treuhänderische Einbehalte oder für Dritte bestimmte Beträge; prüfe neben dem Verwendungszweck Auftrag und Rechtsgrund. Steht der Empfangsberechtigte fest, wird die unverzügliche Weiterleitung vorbereitet. Ist eine Auszahlung noch nicht möglich, verlangen § 43a Absatz 7 BRAO und § 4 BORA die Einzahlung auf ein Anderkonto; ob und ab welcher Höhe ein gesondertes Anderkonto je Mandat statt eines Sammelanderkontos erforderlich ist, ist am Wortlaut der BORA zu prüfen. Eine ungeklärte Bankverbindung rechtfertigt keine betriebliche Nutzung des Geldes.

Dokumentiere Eingang, Berechtigten, Zweck, Verwahrort, geplante Weiterleitung und erfolgte Verfügung. Bei streitiger Berechtigung wird die verantwortliche anwaltliche Person eingeschaltet; eine Treuhandbedingung wird nicht durch den Auszahlungswunsch einer Partei übergangen. Eine Gegenforderung der Kanzlei ist kein Grund, sämtliche Beträge einzubehalten; § 4 BORA erlaubt einen Einbehalt zur Deckung eigener Vergütungsforderungen nur in engen, am Volltext zu prüfenden Grenzen, etwa bei Zusammenhang mit demselben Mandat, Fälligkeit und vorheriger Mitteilung an den Mandanten.

Die steuerliche Einordnung als durchlaufender Posten nach § 10 Absatz 1 UStG setzt das Handeln im Namen und für Rechnung eines anderen voraus und wird eigenständig geprüft. Eine Zahlung auf dem Geschäftskonto kann berufsrechtlich problematisch sein, ohne ihren wirtschaftlichen Zweck zu verlieren: Die steuerliche Einordnung als durchlaufender Posten erlaubt keine berufsrechtlich unzulässige Vermischung, und ein Berufsrechtsverstoß ersetzt keine steuerliche Subsumtion.

### 3.7. Aufrechnung und Verrechnung nur nach gesonderter Prüfung

Prüfe bei einer beabsichtigten Aufrechnung zunächst Gegenseitigkeit, Gleichartigkeit, Fälligkeit und Erfüllbarkeit nach § 387 BGB sowie die Erklärung nach § 388 BGB, anschließend vertragliche, treuhänderische und berufsrechtliche Grenzen. Bei für Dritte bestimmtem Geld scheidet eine Verrechnung regelmäßig an der Gegenseitigkeit: Das Geld eines Dritten oder ein für den Gegner bestimmter Betrag ist nicht Vermögen des Mandanten. Eine Einzugsvollmacht beantwortet diese Fragen nicht.

Der Steuerfall wird gesondert beurteilt: Eine nach außen erklärte Behandlung von Fremdgeld als eigenes Honorar kann die Voraussetzungen eines durchlaufenden Postens verändern, begründet aber keine zivilrechtliche Zulässigkeit der Aufrechnung. Ein interner Buchungsvorschlag ist keine Aufrechnungserklärung. Wird eine Erklärung beauftragt, wird sie vollständig ausformuliert und bezeichnet den Anspruch eindeutig; ohne Auftrag ergeht keine Erklärung. Das Journal wird nicht durch einen negativen Zahlungsbetrag manipuliert, um eine ungeklärte Verrechnung darzustellen.

### 3.8. Insolvenz des Mandanten

Liegt ein Insolvenzantrag oder ein Eröffnungsbeschluss vor, verändert sich die Zuordnung grundlegend. Fremdgeld des Mandanten fällt mit Eröffnung in die Masse; Empfangsberechtigter ist dann der Insolvenzverwalter, nicht der bisherige Ansprechpartner. Eine Honorarforderung für Leistungen vor Eröffnung ist Insolvenzforderung und wird zur Tabelle angemeldet; nur Vergütung für Tätigkeiten, die der Verwalter nach Eröffnung beauftragt, kann Masseverbindlichkeit nach § 55 Absatz 1 InsO sein. Die Abgrenzung ist am Volltext und am konkreten Auftrag zu prüfen.

Eine Aufrechnung gegen Fremdgeldherausgabeansprüche ist in der Insolvenz zusätzlich an § 96 InsO zu messen. Zahlungen des Mandanten in den letzten drei Monaten vor dem Antrag können nach § 130 InsO anfechtbar sein, wenn er zahlungsunfähig war und die Kanzlei das wusste; dieses Risiko wird im Vermerk benannt, nicht entschieden; Frist und Kenntnisvoraussetzungen sind am Volltext zu prüfen. Jede Verrechnung unterbleibt bis zur Klärung.

### 3.9. Offene Posten, Mahnung, Verzug, Skonto und Erlass

Vor jeder Mahnung werden Rechnung, Zugang, Fälligkeit, Teilzahlungen und Beanstandungen geprüft. Die Vergütung ist nach § 10 Absatz 1 RVG erst einforderbar, wenn eine Berechnung in Textform mitgeteilt wurde. Ein abgelaufenes Zahlungsziel allein begründet nicht in jeder Konstellation Verzug: § 286 BGB unterscheidet Mahnung, kalendermäßige Bestimmung, weitere Ausnahmen und die 30-Tage-Regel nach Absatz 3, die bei Verbrauchern den besonderen Hinweis in der Rechnung voraussetzt.

Für Verzugszinsen werden der geltende Basiszinssatz aus amtlicher Quelle, Beginn, Ende und Teilzahlungen berücksichtigt. Die Aufschläge unterscheiden sich nach § 288 BGB: Neun Prozentpunkte für Entgeltforderungen setzen voraus, dass kein Verbraucher beteiligt ist. Die 40-Euro-Pauschale wird nicht gegenüber Verbrauchern angesetzt und nicht neben denselben Rechtsverfolgungskosten addiert.

Ein gewährter Skonto mindert das Entgelt und die Bemessungsgrundlage nach § 17 UStG und wird als vereinbarte Entgeltminderung dokumentiert. Ein Erlass nach § 397 BGB ist ein Vertrag und braucht die Annahme des Mandanten; eine interne Ausbuchung ist kein Erlass. Ein Nachlass auf gesetzliche Gebühren ist an § 49b Absatz 1 BRAO zu messen. Dokumentiere, ob ein Einwand geprüft, eine Stundung vereinbart oder eine Frist verlängert wurde; „wir zahlen später“ wird nicht ohne Annahme zur Stundung.

### 3.10. Überzahlungen, Rücklastschriften und Erstattungen

Bei einer Überzahlung vergleiche Originalforderung, bisherige Zahlungen und mögliche Tilgungsbestimmungen; prüfe, ob eine Doppelzahlung vorliegt oder ein weiterer Vorschuss gemeint ist. Ein Überschuss wird nicht als Erlös behandelt; der Rückzahlungsanspruch folgt aus § 812 Absatz 1 Satz 1 BGB. Eine Rückzahlung an ein neu mitgeteiltes Konto erfolgt erst nach Berechtigten- und Kontoprüfung auf einem zweiten Weg, nicht aufgrund einer unbestätigten E-Mail.

Eine Rücklastschrift ist eine neue Geldbewegung und wird nicht durch Löschen des ursprünglichen Eingangs unsichtbar gemacht. Verknüpfe beide Belege und prüfe, welche Forderung wieder offen ist. Bankgebühren sind nur mit Grundlage weiterbelastbar, bei einem Fehler der Kanzlei gar nicht. Bei Rückzahlung eines Vorschusses oder einer korrigierten Vergütung werden Umsatzsteuerkorrektur nach § 17 UStG und Buchungsperiode mitgedacht; die Erstattung erhält einen Bezug zur ursprünglichen Rechnung und Zahlung, und der Mandant bekommt eine Aufstellung ohne interne Kontonummern.

### 3.11. Umsatzsteuer bei Vereinnahmung und Istversteuerung

Versteuert die Kanzlei nach § 20 UStG nach vereinnahmten Entgelten, entsteht die Steuer nach § 13 Absatz 1 Nummer 1 Buchstabe b UStG mit Ablauf des Voranmeldungszeitraums der Vereinnahmung; der Zahlungseingang ist dann der steuerauslösende Vorgang, nicht das Rechnungsdatum. Freiberufler können die Istversteuerung nach § 20 Satz 1 Nummer 3 UStG unabhängig von der Umsatzgrenze beantragen; Umsatzgrenze und Genehmigungsweg sind am Volltext zu prüfen. Der Buchungsvorschlag nennt bei Istversteuerung stets Vereinnahmungsdatum und Wertstellung.

Bei Sollversteuerung ist die Steuer mit Leistungsausführung entstanden; der Eingang tilgt dann nur die Forderung. In beiden Verfahren löst eine Anzahlung vor Leistungsausführung die Steuer mit Vereinnahmung aus. Durchlaufende Posten nach § 10 Absatz 1 UStG gehören nicht zum Entgelt: Gerichtskosten, die die Kanzlei im Namen und für Rechnung des Mandanten verauslagt, sind keine steuerpflichtige Auslage, eigene Auslagen wie Kopien oder Fahrtkosten dagegen schon. Diese Trennung entscheidet, ob eine Auslage über [`expense`](../../scripts/kanzlei.py) mit `tax_classification=own_taxable` erfasst werden darf.

### 3.12. Aufbewahrung und Grundsätze ordnungsmäßiger Buchführung

Zahlungsbelege, Kontoauszüge und Buchungsvorschläge sind steuerlich nach § 147 AO aufzubewahren, Rechnungsdoppel zusätzlich nach § 14b UStG. Nach dem im Plugin dokumentierten Prüfstand gelten zehn Jahre für Bücher und Abschlüsse, acht Jahre für Buchungsbelege und sechs Jahre für sonstige Unterlagen; die durch das Vierte Bürokratieentlastungsgesetz geänderten Fristen, ihr Beginn und Übergangsregeln sind vor jeder Löschentscheidung am Volltext zu prüfen. Die Handaktenfrist des § 50 BRAO ist davon zu unterscheiden; die Entscheidung trifft [Mandat abschließen](../mandat-abschliessen/SKILL.md).

Die GoBD in der amtlichen Fassung 2026 verlangen Nachvollziehbarkeit, Vollständigkeit, zeitgerechte Erfassung, Unveränderbarkeit und einen Prüfpfad vom Beleg zur Buchung. Deshalb trägt jeder Buchungsvorschlag Beleg-ID und Transaktionsreferenz, Korrekturen erfolgen durch Storno und neue Buchung, und ein elektronisch eingegangener Kontoauszug bleibt im Original erhalten. Das lokale Journal ist kein GoBD-konformes Archiv.

### 3.13. Buchungsvorschlag statt erfundener Finanzbuchung

Ein Buchungsvorschlag enthält Beleg-ID, Transaktionsreferenz, Datum, Betrag, Währung, Mandat, Rechtsgrund, steuerliche Einordnung, vorgesehenes Konto und Gegenkonto sowie offene Prüfungen. Kontonummern stammen aus dem tatsächlich verwendeten Kontenrahmen; der Skill erfindet keine vermeintlich universellen DATEV-Konten. Debitor, Erlöskonto, Umsatzsteuer, Anderkonto und Fremdgeldverbindlichkeit sind unterschiedliche Kategorien, deren technische Umsetzung vom System abhängt.

Bei Einnahmenüberschussrechnung nach § 4 Absatz 3 EStG wird der Zufluss nach § 11 EStG geprüft; die Regel für regelmäßig wiederkehrende Einnahmen kurz vor oder nach dem Jahreswechsel ist am Volltext zu prüfen. Bei Bilanzierung ist zusätzlich die Forderungsebene maßgeblich. Ein Export an die Steuerberatung enthält die Einordnung und die verbleibende Unsicherheit ausdrücklich. Ein Import in ein Produktivsystem erfolgt nur innerhalb des Auftrags; sein Erfolg wird anhand tatsächlicher Rückmeldung kontrolliert, eine lokal erzeugte CSV-Datei ist kein Import.

### 3.14. Lokales Mandatsjournal richtig verwenden

Die Schnittstelle in [Mandatsordner und CLI](../../references/mandatsordner-und-cli.md) sieht für `payment` die Felder `id`, `date`, `gross_eur`, `kind`, `reference`, `source` und `confirmed` vor. Zulässige Arten sind `payment`, `advance` und `third_party`; `date` im Format `YYYY-MM-DD`, `gross_eur` höchstens centgenau, `confirmed` ausdrücklich `true` oder `false`. Ein Fremdgeldfeld gibt es nicht; Fremdgeld wird nicht im Journal erfasst, sondern in der gesonderten Fremdgeldaufstellung je Berechtigtem geführt.

Der Aufruf lautet `python3 "<Pluginordner>/scripts/kanzlei.py" payment --akte "<Mandatsordner>" --data "<Zahlungsdatei.json>"`. Das Skript [`kanzlei.py`](../../scripts/kanzlei.py) kennt die Befehle `init`, `terms`, `time`, `expense`, `payment`, `manual-fee`, `void`, `status` und `draft` sowie die Optionen `--akte`, `--data`, `--id` und `--reason`; es führt keine Netzwerkaufrufe, keine Finanzbuchung und keinen Versand aus. Der Bruttobetrag wird nur aus dem Beleg übernommen; Ankündigungen bleiben `confirmed=false`. Das Journal listet Zahlungen gesondert und weist bei jedem Lauf darauf hin, dass sie nicht verrechnet sind. Nach Ausführung werden `matter_id`, `journal_revision`, `open_items` und `known_gross_eur` in der JSON-Ausgabe kontrolliert; `invoice_ready` ist immer `false`.

`status` liest den Stand, ohne Dateien zu schreiben. `draft` erzeugt `rechnungsentwurf.md`, `rechnungsentwurf.json` und `zeiten.csv` erneut; der Abschnitt „Zahlungsnotizen und nächste Prüfung“ listet jede Zahlung mit Art, Referenz und Bestätigungsstand. Korrekturen erfolgen über `void --id "<ID>" --reason "<Grund>"` und eine neue ID; eine identische Eingabe unter derselben ID ist wirkungslos, eine abweichende wird abgewiesen. Der führende Stand liegt in `00_Mandat/mandatsjournal.sqlite`; abgeleitete Dateien werden regeneriert, nicht manuell verändert. Eine Sicherung erfolgt über das SQLite-Backup-Verfahren oder bei geschlossenem Werkzeug.

### 3.15. Monatliche Abstimmung: Bank, Kasse, Journal und Fremdgeld

Gleiche Bankbewegungen, Kassenbuch, Mandatsjournal, offene Posten und Buchhaltung ab. Untersuche Differenzen einzeln; ein ausgeglichener Gesamtsaldo kann verdecken, dass zwei Mandanten vertauscht wurden, deshalb werden auch Belegzuordnung und Berechtigte geprüft. Eine Barkasse wird mit Kassenbuch, Belegen und Zählprotokoll abgestimmt; Bareinzahlungen werden quittiert und auf Geldwäscheindikatoren geprüft.

Die Fremdgeldabstimmung beginnt mit dem Anfangsbestand je Berechtigtem, addiert nachweisbare Eingänge, zieht belegte Auszahlungen ab und vergleicht den Endbestand mit Anderkonto und Einzelfallzuordnung. Ein Kontogesamtsaldo genügt nicht, weil eine Überzahlung an einen Mandanten durch den Betrag eines anderen verdeckt sein könnte. Eine kleine Restsumme darf nicht wegen ihrer Höhe in Kanzleierlös umgebucht werden; ermittle, wem sie zusteht, weshalb sie nicht weitergeleitet wurde und welche Maßnahme nötig ist. Ist der Berechtigte verstorben, insolvent oder nicht mehr vertretungsberechtigt, wird der rechtliche Auszahlungsempfänger gesondert festgestellt.

Bei einer Differenz wird geprüft, ob ein Erfassungsfehler, eine fehlende Buchung, eine Bankgebühr oder eine Fehlverfügung vorliegt; ein Fehlbetrag wird nicht durch Umbuchung aus einem anderen Mandat kaschiert. Die Übergabe an Buchhaltung oder Steuerberatung enthält Belege und einen kurzen Entscheidungsvermerk; „bitte prüfen“ genügt bei einem erkannten konkreten Problem nicht.

### 3.16. Jahreswechsel und Zahlung unter Vorbehalt

Beim Jahreswechsel werden Rechnungsdatum, Leistungszeitraum, Zahlungsdatum und Wertstellung getrennt dokumentiert. Bei EÜR entscheidet der Zufluss nach § 11 EStG, bei Bilanzierung kann die Forderung bereits erfasst sein, die Umsatzsteuer folgt § 13 UStG. Eine pauschale Zuordnung sämtlicher Dezemberrechnungen zum alten Jahr wäre ebenso falsch wie die Behandlung sämtlicher Januareingänge als neue Leistung.

Eine Zahlung unter Vorbehalt wird mit dem konkreten Vorbehalt dokumentiert; sie kann die Geldschuld erfüllen, ohne den Streit über den Rechtsgrund zu erledigen. Zahlungsstatus und Streitstatus werden getrennt geführt: Eine Rechnung kann bezahlt sein, während ein Rückforderungsstreit offen bleibt.

### 3.17. Sammelzahlung mit Gebührenabzug

Ein Zahlungsdienstleister überweist 2.350 Euro, während der Mandant nachweislich 2.380 Euro bezahlt hat und die Abrechnung 30 Euro Dienstleistergebühr ausweist. Erfolgte die Zahlungsabwicklung im Auftrag der Kanzlei, ist die Schuld des Mandanten durch die volle Zahlung erfüllt; der Unterschied erscheint nicht als Restforderung von 30 Euro gegen ihn, sondern wird nach dem Rechtsverhältnis zum Dienstleister gebucht, Vorsteuer nur bei ordnungsgemäßer Rechnung. Hat dagegen der Mandant eigenmächtig Bankspesen abgezogen, sind Vertrag, Zahlungsort und Kostentragung gesondert zu prüfen.

### 3.18. Abschlusskontrolle und Gegenposition

Prüfe jeden wesentlichen Schluss gegen die stärkste naheliegende Gegenposition: Ein Betrag passt zur Rechnung, könnte aber einem anderen Mandat gehören; „Kosten“ im Verwendungszweck könnte Gerichtskosten statt Honorar meinen; ein Eingang des Versicherers könnte eine Abschlagszahlung sein; ein scheinbarer Überschuss könnte auf einer noch nicht erfassten Rechnung beruhen. Der Vermerk nennt, welcher Beleg die Alternative bestätigt oder widerlegt. Die Statusmeldung unterscheidet bestätigte Zahlung, geklärte Zuordnung, vorgeschlagene Buchung, gebuchte Position und Auszahlung; kein Status wird aus dem vorherigen abgeleitet.

### 3.19. Honorar- und Zeitanschluss

Nach [Arbeitsweise](../../references/arbeitsweise.md) wird der gespeicherte Honorarstand vor jeder Verrechnung kurz vorgehalten: „Gespeichert: Zeithonorar 240 Euro netto je Stunde, Deckel 1.200 Euro netto nur Gebühren. Gilt das unverändert?“ Für die Zahlungsklärung frage nach tatsächlichen Minuten, Datum, Person und Abrechenbarkeit und übergib den Zeitstand (bestätigte Minuten, offene Zeitfragen) an [Zeiten erfassen](../zeiten-erfassen/SKILL.md). Reine Buchhaltungsarbeit wird nur berechnet, wenn die Vereinbarung das deckt; fehlende Zeit bleibt offen, nicht null.

### 3.20. Agentischer Lauf und Freigabestufe

Dieser Skill verantwortet die Phase `zahlung` des Mandatslaufs nach [Mandatslauf und Freigaben](../../references/mandatslauf-und-freigaben.md). Die Phase endet mit der Zahlungsklärung und dem Buchungsvorschlag als führender Fassung. Trifft ein Zahlungsbeleg während laufender Sacharbeit ein, wird `zahlung` mit `--nebenlauf` neben die Hauptphase gesetzt; die Sacharbeit läuft weiter. Je Freigabestufe gilt:

| Stufe | Ohne Rückfrage |
|---|---|
| 0 | Beleg lesen; Zuordnungsvermerk, Buchungsvorschlag und Klärungsbrief nur als Text liefern |
| 1 | Vermerk und Buchungsvorschlag unter `01_Bearbeitung` anlegen; Kontoauszug unverändert kopieren; Dokumentregister führen |
| 2 | Belegte Eingänge mit `kanzlei.py payment` und `confirmed=true` buchen; Ankündigungen mit `confirmed=false`; Fremdgeldaufstellung und Mandatslauf fortschreiben |
| 3 | Übergabevermerk mit Hash und Buchhaltungsexport als Datei erzeugen; Nachbarskills anstoßen |

Auf keiner Stufe erteilt der Skill eine Zahlungsanweisung, führt eine Überweisung, Rückzahlung oder Weiterleitung aus, erklärt eine Aufrechnung, bucht im Produktivsystem der Finanzbuchhaltung oder kennzeichnet eine Rechnung als bezahlt, bevor das Buchhaltungssystem dies zurückgemeldet hat.

Für jede Auszahlung, Verrechnung oder Weiterleitung öffnet der Skill das Gate G5 Zahlung und Fremdgeld und legt dafür den Buchungsvorschlag mit Beleg-ID, Berechtigtem, Betrag und auf zweitem Weg bestätigter Bankverbindung bereit. Freigegeben wird G5 von einem Berufsträger, bei Fremdgeld von der mandatsverantwortlichen Anwältin oder dem Anwalt. Nach der Freigabe trägt der Skill den Ausführungsbeleg der Bank mit Datum und bei einer Verrechnung die Aufrechnungserklärung mit Zugangsdatum nach; erst dann lautet der Status „ausgezahlt“ oder „verrechnet“. Eine bestätigte Honorarzahlung ohne Auszahlung öffnet kein Gate. Barzahlungen und Zahlungen Unbeteiligter gehen an [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md), das über G7 Meldung entscheidet; dieser Skill öffnet G7 nicht selbst.

Im Produktregister trägt der Skill die Zahlungsklärung oder den Buchungsvorschlag mit dem Zustand `entwurf` ein und setzt ihn nach der Gegenkontrolle nach 3.21 auf `geprueft`; `freigegeben` folgt erst aus der namentlichen Freigabe von G5. Bestätigte Vorschüsse gehen anschließend ohne Rückfrage als Liste an [Abrechnung und E-Rechnung](../abrechnung-e-rechnung/SKILL.md). Der Lauf wird mit [`mandatslauf.py`](../../scripts/mandatslauf.py) dokumentiert:

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" phase --akte "/Mandate/M-2026-014" --phase zahlung --grund "Vergleichssumme eingegangen" --nebenlauf
python3 "<Pluginordner>/scripts/mandatslauf.py" product --akte "/Mandate/M-2026-014" --id buchungsvorschlag-B-2026-0898 --pfad "01_Bearbeitung/Buchungsvorschlag_B-2026-0898.md" --skill zahlungen-buchhaltung --zustand geprueft
python3 "<Pluginordner>/scripts/mandatslauf.py" gate --akte "/Mandate/M-2026-014" --gate G5 --aktion oeffnen --bezug "Buchungsvorschlag_B-2026-0898.md"
python3 "<Pluginordner>/scripts/mandatslauf.py" next --akte "/Mandate/M-2026-014"
```

Stoppregel: Ist der wirtschaftlich Berechtigte eines Eingangs streitig oder wird eine Verrechnung ohne dokumentierte Aufrechnungslage verlangt, separiert der Skill den Betrag, öffnet G5 und arbeitet an diesem Vorgang nicht weiter, bis ein Berufsträger entschieden hat.

### 3.21. Typische Fehler und Gegenkontrolle

| Fehler | Woran erkennbar | Gegenkontrolle |
|---|---|---|
| Fremdgeld als Honorar vereinnahmt | Vergleichssumme oder KFB-Betrag auf Erlöskonto | Berechtigten je Eingang benennen; Anderkonto abgleichen |
| Verrechnung ohne Aufrechnungslage | Honorar „abgezogen“, keine Erklärung in der Akte | § 387 BGB und § 4 BORA prüfen; Erklärung dokumentieren |
| Ankündigung als Eingang gebucht | Kein Kontoauszug, nur E-Mail | Transaktionsreferenz verlangen; `confirmed=false` |
| Gesetzliche Reihenfolge trotz Tilgungsbestimmung | Verwendungszweck nennt andere Rechnung | § 366 Absatz 1 BGB vor Absatz 2 anwenden |
| Zinsen vor Kosten zugeordnet | Teilzahlung nur auf Hauptforderung gebucht | § 367 Absatz 1 BGB: Kosten, Zinsen, Hauptleistung |
| Versicherer als Leistungsempfänger behandelt | Rechnung an Versicherer adressiert | Mandant bleibt Leistungsempfänger; Drittzahler erfassen |
| Vorschuss ohne Umsatzsteuer gebucht | Steuer erst mit Schlussrechnung | § 13 UStG: Steuer mit Vereinnahmung |
| Rücklastschrift durch Löschung „bereinigt“ | Ursprungsbuchung fehlt | Beide Belege verknüpfen; Storno mit Grund |
| Gerichtskosten als eigene Auslage | `own_taxable` für durchlaufenden Posten | § 10 Absatz 1 UStG; Weiterbelastung ohne Steuer |
| Kleinbetrag aus Fremdgeld in Erlös umgebucht | Altbestand „bereinigt“ ohne Berechtigten | Berechtigten ermitteln; Weiterleitung veranlassen |
| Verrechnung trotz Insolvenzanzeichen | Zahlung in den drei Monaten vor Antrag | § 96 und § 130 InsO als Risiko benennen; stoppen |
| Produktive Buchung behauptet | „gebucht“ ohne Systemrückmeldung | Status „vorgeschlagen“ bis Rückmeldung vorliegt |

### 3.22. Übergabe an Nachbarskills

Jede Übergabe nennt die führende Fassung (Pfad und Hash), den Honorarstand (Modell, Satz/Betrag, Umfang, Deckel, netto/brutto), den Zeitstand (bestätigte Minuten, offene Zeitfragen), die offenen Gates und die offenen Fragen. Ein Fristobjekt entsteht in diesem Skill nur ausnahmsweise, etwa eine zugesagte Rückzahlungs- oder Weiterleitungsfrist; es geht erfasst an [Fristen berechnen und überwachen](../fristen-berechnen-ueberwachen/SKILL.md) und kommt berechnet zurück, eingetragen wird es erst nach G2.

An [Abrechnung und E-Rechnung](../abrechnung-e-rechnung/SKILL.md) geht die Liste der bestätigten Vorschüsse mit Datum, Bruttobetrag und Steueranteil für den Ausweis nach § 10 Absatz 2 RVG; zurück kommt die Rechnung mit Nummer und Fälligkeit. An [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) geht die Feststellung, dass ein Eingang auf eine ungeklärte Vergütungsbasis trifft; zurück kommt der bestätigte Honorarstand. An [Mandat abschließen](../mandat-abschliessen/SKILL.md) gehen Fremdgeldaufstellung je Berechtigtem, Vorschussabrechnung und Aufbewahrungsbeginn; zurück kommt die Freigabe der Schlussauszahlung. An [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md) geht ein beabsichtigter Einbehalt mit Betrag, Anspruchsgrundlage und Mandatsbezug; zurück kommt die berufsrechtliche Bewertung. An [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md) gehen Barzahlung oder Zahlung unbeteiligter Dritter mit Beleg; zurück kommt der Prüfvermerk. An [Workflow und Übergabe](../workflow-uebergabe/SKILL.md) geht der Monatsabgleich mit offenen Gates, offenen Fragen, verantwortlicher Person und Klärungsfrist.

## 4. Quellenpflicht

### 4.1. Tragende Normen

Verwende die [Zitierweise](../../references/zitierweise.md) und die [Rechtsquellen](../../references/rechtsquellen.md) des Plugins. Tragend sind [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) mit der Fremdgeldregel in Absatz 7, § 4 BORA, [§ 9 RVG](https://www.gesetze-im-internet.de/rvg/__9.html), [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html), [§ 267 BGB](https://www.gesetze-im-internet.de/bgb/__267.html), [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html), [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html), [§ 362 BGB](https://www.gesetze-im-internet.de/bgb/__362.html), [§ 366 BGB](https://www.gesetze-im-internet.de/bgb/__366.html), [§ 367 BGB](https://www.gesetze-im-internet.de/bgb/__367.html), [§ 387 BGB](https://www.gesetze-im-internet.de/bgb/__387.html), [§ 103 ZPO](https://www.gesetze-im-internet.de/zpo/__103.html), [§ 104 ZPO](https://www.gesetze-im-internet.de/zpo/__104.html), [§ 10 UStG](https://www.gesetze-im-internet.de/ustg_1980/__10.html), [§ 13 UStG](https://www.gesetze-im-internet.de/ustg_1980/__13.html), [§ 20 UStG](https://www.gesetze-im-internet.de/ustg_1980/__20.html), [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html), [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html), [§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html), [§ 55 InsO](https://www.gesetze-im-internet.de/inso/__55.html), [§ 96 InsO](https://www.gesetze-im-internet.de/inso/__96.html) und [§ 130 InsO](https://www.gesetze-im-internet.de/inso/__130.html). GoBD, Aufbewahrung und das Buchführungssystem werden getrennt vom materiellen Zahlungsanspruch behandelt.

### 4.2. Verifizierte Rechtsprechungsanker

BFH, Urteil vom 29.09.2020 – VIII R 14/17, Rn. 20–32, insbesondere 23 und 28–31, [amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202110029/). Trägt: Eine nach außen erklärte Behandlung von Fremdgeld als eigenes Honorar kann die für den durchlaufenden Posten maßgebliche Verknüpfung lösen und den Betrag steuerlich zum Entgelt machen. Trägt nicht: eine berufsrechtliche oder zivilrechtliche Erlaubnis zur Aufrechnung gegen Fremdgeld.

BFH, Urteil vom 16.12.2014 – VIII R 19/12, Leitsätze und Rn. 17–25, [amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE201510153/). Trägt: Die steuerliche Behandlung veruntreuter Fremdgelder ist von ihrer rechtswidrigen Verwendung getrennt zu beurteilen. Trägt nicht: eine Gestattung der Vermischung oder Eigennutzung fremder Gelder.

BGH, Urteil vom 27.04.2017 – IX ZR 198/16, Rn. 14–16, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2016/IX_ZR_198-16.pdf?__blob=publicationFile&v=1). Trägt: Aussonderung und Vermischung von Treuhandguthaben im Insolvenzfall hängen von Konto und Rechtsverhältnis ab. Trägt nicht: eine Aussage zur anwaltlichen Standardabrechnung; die Übertragung verlangt die Prüfung des konkreten Anderkontos.

BFH, Beschluss vom 26.02.2026 – V B 11/25, Rn. 2, [amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650044/). Trägt: Eine Revision zur Frage des Vorsteuerzeitpunkts bei ursprünglich nicht berichtigungsfähigen Dokumenten ist zugelassen; der Folgestand V R 7/26 ist anhängig. Trägt nicht: eine Sachentscheidung, auf die eine Buchungsentscheidung gestützt werden könnte.

### 4.3. Belegdisziplin

Zum Prüfstand 07.10.2026 waren die amtlichen Normseiten und Gerichtsseiten aus der Arbeitsumgebung nicht abrufbar. Deshalb enthält dieser Skill keine neu aufgenommene Entscheidung, und jede Normaussage mit konkreter Frist, Schwelle oder Satznummer, die nicht bereits in den Rechtsquellen des Plugins verifiziert ist, trägt den Vermerk „am Volltext zu prüfen“; vor Verwendung ist die amtliche Seite zu lesen. Kommentar-, Handbuch- und Aufsatzfundstellen werden nicht aus Modellwissen zitiert. Eine Entscheidung wird nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, amtlicher Quelle und gelesener Randnummer genannt. Es gibt keine Präjudizienbindung; jeder Anker nennt, was er trägt und was nicht.

## 5. Ausgabeformat

### 5.1. Nachvollziehbarer Zahlungs- und Buchungsvermerk

Liefere den Zuordnungsvermerk, den vollständigen Buchungsvorschlag und erforderlichenfalls ein fertiges Klärungs-, Rückzahlungs- oder Erinnerungsschreiben. Tabellen können Beträge und Belegreferenzen ordnen; das juristische Ergebnis wird in vollständigen, ausformulierten Sätzen erläutert. Skelette, Halbsätze und reine Aufzählungsgerüste sind als Endprodukt verboten. Formatierte Texte verwenden, soweit technisch möglich, Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei reiner Textausgabe steht der Exporthinweis mit diesem Formatwunsch gesondert außerhalb des Empfängertextes.

Die Ausgabe nennt die Grenzen des Erledigten: erfasst, zugeordnet, vorgeschlagen, importiert oder ausgezahlt. Technische Hinweise, Quellenprotokolle und Kontierungsfragen gehören nicht in einen versandfertigen Mandantenbrief.

### 5.2. Abnahmekriterien

Das Produkt ist fertig, wenn jeder Eingang eine Beleg-ID, eine Transaktionsreferenz und einen benannten wirtschaftlich Berechtigten trägt. Das Produkt ist fertig, wenn Honorar, Vorschuss, Drittzahlung und Fremdgeld in getrennten Kategorien erscheinen. Das Produkt ist fertig, wenn jede Verrechnung eine dokumentierte Aufrechnungslage oder Verrechnungsabrede nennt oder ausdrücklich unterblieben ist. Das Produkt ist fertig, wenn der Steuerzeitpunkt nach Soll- oder Istversteuerung bezeichnet oder als offen gekennzeichnet ist. Das Produkt ist fertig, wenn der Status jedes Vorgangs als erfasst, zugeordnet, vorgeschlagen, gebucht oder ausgezahlt angegeben ist und kein Status behauptet wird, der nicht durch Rückmeldung belegt ist. Das Produkt ist fertig, wenn jedes Schreiben an den Mandanten in Sie-Form, vollständig ausformuliert und ohne interne Kontonummern vorliegt. Das Produkt ist fertig, wenn offene Fragen mit verantwortlicher Person und benötigtem Beleg benannt sind. Das Produkt ist fertig, wenn es im Mandatslauf als führende Fassung mit Pfad und Hash eingetragen ist oder, ohne Dateizugriff, der Übergabevermerk Pfad und Hash nennt, und wenn kein Gate, insbesondere G5, stillschweigend als freigegeben behandelt wurde.

## 6. Beispiele

### 6.1. Vollzahlung auf eindeutig bezeichnete Rechnung

Der Bankbeleg weist 2.380 Euro mit dem Verwendungszweck „R-2026-41“ aus; die Rechnung lautet auf denselben Betrag, Vorzahlungen fehlen. Der Vermerk lautet: „Der am Montag, 05.10.2026, eingegangene Betrag von 2.380 Euro ist der Rechnung R-2026-41 zuzuordnen. Schuldner und Verwendungszweck stimmen mit den Stammdaten überein; der Rechnungsbetrag ist vollständig erfüllt. Die Umsetzung erfolgt im Kontenrahmen mit Bezug auf Bankbeleg B-2026-0912.“ Der Journaldatensatz enthält `kind=payment`, `gross_eur="2380.00"`, die Rechnungsreferenz und `confirmed=true`. Die Ausbuchung des offenen Postens wird erst behauptet, wenn sie im Buchhaltungssystem erfolgt ist.

### 6.2. Ausformulierte Zahlungsklärung an die Mandantin

Am Montag, 05.10.2026, gehen 1.500 Euro mit dem Verwendungszweck „Beratung“ ein; offen sind die Rechnung R-2026-37 über 1.071 Euro und die Vorschussanforderung vom 14.09.2026 über 1.500 Euro. Der Brief lautet:

> Sehr geehrte Frau Albrecht,
>
> in dem Mandat Albrecht gegen Weidner Bau GmbH ist am Montag, 05.10.2026, auf unserem Konto ein Betrag von 1.500 Euro mit dem Verwendungszweck „Beratung“ eingegangen. Wir danken Ihnen für die Zahlung.
>
> In Ihrem Mandat sind derzeit zwei Positionen offen: die Rechnung R-2026-37 vom 14.09.2026 über 1.071 Euro für die außergerichtliche Vertretung und die Vorschussanforderung vom selben Tag über 1.500 Euro für das Klageverfahren. Der Verwendungszweck lässt nicht erkennen, auf welche dieser Positionen Sie gezahlt haben. Der Betrag entspricht der Vorschussanforderung; wir möchten diese Zuordnung jedoch nicht vermuten, sondern von Ihnen bestätigen lassen.
>
> Bitte teilen Sie uns bis Mittwoch, 21.10.2026, mit, ob die Zahlung den Vorschuss für das Klageverfahren betrifft oder ob sie auf die Rechnung R-2026-37 angerechnet werden soll. Im zweiten Fall verbleibt ein Guthaben von 429 Euro, das wir auf den Vorschuss anrechnen würden, sofern Sie damit einverstanden sind. Bis zu Ihrer Antwort führen wir den Betrag gesondert und behandeln keine der beiden Positionen als ausgeglichen. Die vereinbarte Vergütungsgrundlage bleibt unverändert. Verzugsfolgen aus der Rechnung R-2026-37 machen wir bis zur Klärung nicht geltend.
>
> Sobald die Zuordnung feststeht, erhalten Sie eine aktualisierte Übersicht über Vorschuss, Rechnung und Restbetrag.
>
> Mit freundlichen Grüßen
>
> Dr. Lena Kessler, Rechtsanwältin

Der Journaleintrag lautet bis zur Antwort `kind=advance`, `confirmed=false`, `reference="Zuordnung offen, Klärung 05.10.2026"`. Die Exportnotiz an den Auftraggeber, getrennt vom Brief, nennt Times New Roman 11 pt und den Vorbehalt der Kontoprüfung.

### 6.3. Ausformulierter Buchungsvorschlag mit Fremdgeldtrennung

Am Freitag, 02.10.2026, gehen auf dem Geschäftskonto 12.000 Euro „Vergleich Hartmann“ ein. Der Vergleich vom 14.09.2026 sieht 10.000 Euro Hauptforderung und 2.000 Euro Kostenerstattung vor; die Rechnung R-2026-29 über 1.785 Euro ist noch offen. Der Buchungsvorschlag lautet:

> Buchungsvorschlag zu Bankbeleg B-2026-0898, Transaktionsreferenz 7F3K-2026-1002, Eingang Freitag, 02.10.2026, Wertstellung 02.10.2026, 12.000 Euro, Mandat M-2026-014 Hartmann gegen Reuter.
>
> Der Betrag ist nach dem Vergleich vom 14.09.2026 aufzuteilen. Der Hauptforderungsanteil von 10.000 Euro steht dem Mandanten zu. Er ist Fremdgeld im Sinne des § 43a Absatz 7 BRAO, wird in voller Höhe auf das Anderkonto umgebucht und in der Fremdgeldaufstellung unter dem Berechtigten Hartmann mit dem Zweck „Vergleichssumme“ geführt. Die Weiterleitung an die hinterlegte und am 06.10.2026 telefonisch bestätigte Bankverbindung des Mandanten wird zur Freigabe vorgelegt.
>
> Der Kostenanteil von 2.000 Euro erfüllt den Erstattungsanspruch des Mandanten aus dem Vergleich. Er ist ebenfalls Fremdgeld und wird gesondert unter dem Zweck „Kostenerstattung Vergleich“ geführt. Eine Verrechnung mit der offenen Rechnung R-2026-29 über 1.785 Euro wird nicht vorgeschlagen, weil weder eine Verrechnungsabrede noch eine Aufrechnungserklärung vorliegt. Die verantwortliche Anwältin entscheidet, ob eine Aufrechnung in den Grenzen des § 4 BORA erklärt wird; bis dahin bleibt der Betrag auf dem Anderkonto.
>
> Steuerlich sind beide Anteile durchlaufende Posten nach § 10 Absatz 1 UStG; eine Umsatzsteuer entsteht nicht. Eine Erfassung im Mandatsjournal als Zahlung unterbleibt, weil kein Honorar vereinnahmt wurde. Offen bleibt die schriftliche Bestätigung der Bankverbindung, die bis Freitag, 09.10.2026, erwartet wird. Status: zugeordnet und vorgeschlagen; nicht gebucht, nicht ausgezahlt.

Konto und Gegenkonto werden erst mit dem Kontenrahmen der Kanzlei ergänzt. Im Mandatslauf wird die Phase `zahlung` als Nebenlauf zur laufenden Sacharbeit gesetzt und der Buchungsvorschlag als Produkt `buchungsvorschlag-B-2026-0898` im Zustand `geprueft` mit Pfad und Hash eingetragen. Für die Weiterleitung der 10.000 Euro wird G5 Zahlung und Fremdgeld mit Bezug auf diese Datei geöffnet; die Einbehaltsfrage zu den 1.785 Euro geht ohne Rückfrage mit Betrag, Anspruchsgrundlage und Mandatsbezug an Anwaltsberufsrecht prüfen. Dort bleibt der Lauf stehen: Bis Dr. Kessler G5 namentlich freigibt, liegt der Betrag auf dem Anderkonto, und `next` verweist auf das offene Gate statt auf einen weiteren Skill.

### 6.4. Negativbeispiel: Fremdgeld mit Honorar verrechnet

Falsche Ausgabe zum Sachverhalt aus 6.3: „Eingang 12.000 Euro Vergleich Hartmann am 02.10.2026. Davon 1.785 Euro auf Rechnung R-2026-29 verbucht, Rechnung ausgeglichen. Rest 10.215 Euro an Mandant überwiesen. Journal: payment 1785.00 bestätigt.“

Diese Ausgabe ist aus fünf Gründen falsch. Erstens behandelt sie den Kostenanteil als Honorar, obwohl der Erstattungsanspruch dem Mandanten zusteht und der gesamte Betrag Fremdgeld ist. Zweitens verrechnet sie ohne Aufrechnungserklärung nach § 388 BGB und ohne Prüfung des § 4 BORA. Drittens behauptet sie eine weder freigegebene noch ausgeführte Überweisung. Viertens bucht sie den Kostenanteil als steuerpflichtiges Entgelt, was nach BFH VIII R 14/17 die Verknüpfung des durchlaufenden Postens lösen kann, ohne die berufsrechtliche Zulässigkeit zu beantworten. Fünftens erfasst sie im Journal eine bestätigte Honorarzahlung, die nicht stattgefunden hat.

Korrigierte Fassung: „Der Eingang von 12.000 Euro vom Freitag, 02.10.2026, ist in voller Höhe Fremdgeld des Mandanten Hartmann und wird auf das Anderkonto umgebucht. Die Rechnung R-2026-29 bleibt offen. Ob die Kanzlei mit dem Kostenerstattungsanteil aufrechnet, entscheidet die verantwortliche Anwältin nach Prüfung des § 4 BORA; eine etwaige Erklärung ergeht schriftlich an den Mandanten. Eine Auszahlung ist bisher nicht erfolgt. Im Mandatsjournal wird keine Zahlung erfasst.“

### 6.5. Vorschussabrechnung nach Mandatsende

> Sehr geehrter Herr Brandt,
>
> wir haben die Abrechnung des am Dienstag, 15.09.2026, beendeten Mandats abgeschlossen. Sie haben am Montag, 31.08.2026, einen Vorschuss von 1.190 Euro brutto geleistet. Die nach der Vergütungsvereinbarung vom 24.08.2026 und den bestätigten Leistungsnachweisen entstandene Vergütung beträgt 800 Euro netto zuzüglich 152 Euro Umsatzsteuer, insgesamt 952 Euro brutto. Weitere abrechenbare Auslagen sind nicht angefallen.
>
> Nach Verrechnung des Vorschusses verbleibt ein Guthaben zu Ihren Gunsten von 238 Euro. Die beigefügte Schlussabrechnung stellt Leistung und Vorschuss gegenüber. Die Rückzahlung erfolgt nach Prüfung der hinterlegten Bankverbindung innerhalb von zehn Tagen nach Zugang dieses Schreibens.
>
> Mit freundlichen Grüßen
>
> Dr. Lena Kessler, Rechtsanwältin

Die bevorstehende Zahlung wird nicht als erfolgte Überweisung formuliert, solange sie nicht ausgeführt und bestätigt ist.

### 6.6. Sachliche Zahlungserinnerung

> Sehr geehrte Frau Albrecht,
>
> nach Abgleich unserer Zahlungseingänge ist aus der Rechnung R-2026-37 vom 14.09.2026 noch ein Betrag von 571 Euro offen. Die Rechnung beruht auf der bestätigten Vergütungsvereinbarung vom 03.08.2026 für die außergerichtliche Vertretung. Ihre Teilzahlung vom 28.09.2026 über 500 Euro haben wir berücksichtigt.
>
> Bitte überweisen Sie den verbleibenden Betrag bis Freitag, 23.10.2026. Falls Sie bereits gezahlt haben, genügt ein Hinweis auf Zahlungsdatum und Verwendungszweck. Sollten Sie eine Rechnungsposition beanstanden, teilen Sie uns bitte mit, welche Position betroffen ist; wir erläutern sie anhand der Leistungsaufstellung. Verzugsfolgen machen wir nur auf der Grundlage der gesetzlichen und vertraglichen Voraussetzungen geltend.
>
> Mit freundlichen Grüßen
>
> Dr. Lena Kessler, Rechtsanwältin

Vor Verwendung werden Zugang der Berechnung nach § 10 RVG, Fälligkeit und Saldo geprüft; eine Mahnung mit Zinsen oder Kosten braucht die Berechnung nach §§ 286, 288 BGB.
