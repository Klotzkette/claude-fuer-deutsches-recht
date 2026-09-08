# Vollprüfung: schadensregulierung

## Zusammensetzung

Diese Vollprüfung enthält alle 10 Skills des Plugins `schadensregulierung`.

## Inhaltsverzeichnis

1. **schadenfall-aufnehmen** — Beginnt die Schadenabwicklung für Unternehmen, Anspruchsgegner oder regulierende Haftpflichtversicherer aus Meldung und …
2. **regulierung-korrespondieren** — Formuliert Eingangsbestätigungen, Belegnachforderungen, Zwischenbescheide, Teilregulierungen und begründete Ablehnungen …
3. **versicherung-einschalten** — Erstellt die Haftpflicht-Schadenanzeige und klärt Police, versichertes Unternehmen, Tätigkeit, Zeitraum, Selbstbehalt, D…
4. **haftpflichtschaden-regulieren** — Bearbeitet einen Haftpflichtschaden aus Sicht des regulierenden Versicherers: Deckungsstand, Anspruchsprüfung, Besichtig…
5. **regress-und-anspruchsuebergang** — Ordnet Schadenforderungen zwischen Geschädigtem, Krankenkasse, Arbeitgeber und Sachversicherer zu. Prüft sachlich und ze…
6. **vergleich-und-zahlung-abschliessen** — Führt eine geprüfte Schadenforderung zur kontrollierten Teilzahlung, Abfindung oder Ablehnung und zum Aktenabschluss. Kl…
7. **schadenpositionen-pruefen** — Prüft geltend gemachte Personen- und Sachschäden positionsweise anhand von Befunden, Kaufbelegen und Ausfällen. Trennt S…
8. **haftungsweg-bestimmen** — Prüft die Verantwortlichkeit des in Anspruch genommenen Unternehmens aus Vertrag, Delikt und einschlägiger Gefährdungsha…
9. **unfallbelege-sichern** — Sichert flüchtige Belege zu einem Schadenfall: Video, Tür- und Betriebsprotokolle, Produkt oder beschädigte Sache, Zeuge…
10. **abschleppschaden-pruefen** — Prüft Fahrzeugschäden beim Abschleppen aus Busspur, Haltestelle oder Privatfläche. Trennt Anordnung und Kosten von Ausfü…

---

## Skill: `schadenfall-aufnehmen`

_Beginnt die Schadenabwicklung für Unternehmen, Anspruchsgegner oder regulierende Haftpflichtversicherer aus Meldung und Aktenordner. Ordnet Rolle, Belegverlust und nächsten Entwurf zu; unterscheidet allgemeine Personen- und Sachschäden, U-Bahn-Vorfälle und Abschleppschäden. Keine erneute Vollaufnahme bekannter Vorgänge._

# Schadenfall aufnehmen

## 1. Zweck und Anwendungsfall

Ein Fahrgast meldet eine Verletzung, ein Kunde einen Produktschaden, ein Fahrzeughalter einen Abschleppschaden oder ein Haftpflichtversicherer übernimmt die Abwicklung. Führe die Angelegenheit sofort in einen bearbeitbaren Zustand. Die Unternehmens- oder Versichererperspektive bedeutet sachgerechte Aufklärung, nicht reflexhafte Ablehnung. Eine vorhandene Rolle bleibt erhalten; der Versicherer erhält keine Schadenanzeige an sich selbst.

## 2. Eingaben

Lies zuerst die bereitgestellte Meldung, den letzten Schriftwechsel und die einschlägige Police. Ermittle Ereignisort und -zeit, eigene Rolle, Anspruchsteller, Schadenarten und vorhandene Vorgangsnummer. Ist ein bestimmtes Schreiben verlangt, beginne damit. Ohne Material frage gebündelt nach Ereignis, eigener Rolle und gewünschtem Empfänger; eine fehlende Kaufquittung sperrt nicht die Schadenanzeige.

## 3. Ablauf

1. Sichere bei fortbestehender Gefahr die menschliche Eskalation an Betrieb oder Notdienst. Dieser Vorgang ist keine Leitstelle. Medizinische Akuthilfe und Betriebsfreigabe werden nicht durch einen Chat ersetzt.
2. Erfasse Verletzte, Anspruchsgegner, Betreiber, Halter, Hersteller und Versicherer als verschiedene Rollen. Eine Konzernmarke ersetzt keinen Rechtsträger. Eigenschäden erhalten eigene Positionen und keinen automatischen Abzug von der Fremdforderung.
3. Setze als Erstes die nächste tatsächliche Frist: Videoüberschreibung, Versicherungsanzeige, gerichtlicher Termin oder belegter Zugang. Ein selbst gesetztes Antwortdatum ist keine gesetzliche Ausschlussfrist.
4. Notiere ausschließlich einen kompakten Fallstand: Aussage, Herkunft, Bestätigung oder Widerspruch. Bei der U-Bahn sind Fahrt, Türposition, Fahrgastwechsel, Bewegungsbeginn und Nothalt wichtiger als eine lange allgemeine Personenliste.
5. Wähle einen nächsten Arbeitsschritt. Nutze bei konkret drohendem Belegverlust `unfallbelege-sichern`, bei einer Anzeige des Unternehmens `versicherung-einschalten`, bei aktiver Versichererbearbeitung `haftpflichtschaden-regulieren`, bei Beschädigung durch Umsetzen `abschleppschaden-pruefen` und bei bezifferter Forderung `schadenpositionen-pruefen`. Lade nur den benötigten Skill. Ein reiner Abschleppgebührenstreit ist keine Fahrzeugschadenregulierung.
6. Halte Bearbeiter, Vertretung und Wiedervorlage fest. Keine automatische Nachricht, kein Anerkenntnis, keine Zahlung. Bei Werkzeugfehlern arbeite am unabhängigen Text weiter; behaupte keine erfolgte Sicherung.

## 4. Quellenpflicht

Beachte die lokal mitgelieferte [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md) und [Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md). VVG Paragraf 104 unterscheidet Wochenanzeigen von unverzüglichen Anzeigen gerichtlicher Verfahren. Verjährungsdaten nicht aus der bloßen Schadenhöhe ableiten.

## 5. Ausgabeformat

Liefere zuerst den verlangten Entwurf, sonst ein Fallblatt mit Ereignis, Parteien, akutem Handlungsbedarf und verantwortlichem nächsten Schritt. Beleglücken stehen bei der betroffenen Aussage. Schreiben sind in vollständigen Sätzen auszuformulieren; keine Halbsätze oder leeren Textgerüste als Endprodukt. Formatierte Dokumente verwenden soweit möglich Times New Roman 11 pt und dezimale Gliederung. Ohne Export liefere Text statt eines erfundenen Downloads.

## 6. Beispiel

„Unser Fahrgast wurde gestern beim Aussteigen mitgezogen; Polizei war nicht vor Ort.“ Das erste Produkt ist die Sicherungsanforderung an den Betrieb und eine fristgerechte Versicherungsanzeige aus bekannten Daten. Es beginnt nicht mit einer Schmerzensgeldforderung und wartet nicht auf eine endgültige ärztliche Prognose.

---

## Skill: `regulierung-korrespondieren`

_Formuliert Eingangsbestätigungen, Belegnachforderungen, Zwischenbescheide, Teilregulierungen und begründete Ablehnungen für Unternehmen oder regulierende Haftpflichtversicherer. Trennt Außenbrief und interne Freigabe, ohne verdeckte Anerkenntnisse, leere Prüfversprechen oder unnötige Gesundheitsabfragen._

# Regulierung korrespondieren

## 1. Zweck und Anwendungsfall

Ein Betroffener wartet auf eine Antwort, ein Versicherer braucht Ergänzungen oder eine Forderung ist entscheidungsreif. Verfasse genau das benötigte Schreiben. Erneute allgemeine Fallaufnahme nur, wenn Rolle oder Vorgang nicht zugeordnet werden können.

## 2. Eingaben

Letztes Schreiben, bestätigte Tatsachen, konkreter Prüfstand, Empfänger, Vertretung und freigegebene Zusagen. Interne Reserven oder Verhandlungsspielräume gehören nicht ungefragt in den Außenbrief.

## 3. Ablauf

1. Bestimme Absenderrolle und Textfunktion: Eingang, konkrete Nachfrage, Sachstand, Angebot, Teilzahlung oder Ablehnung. Ein Versicherer benennt den vertretenen Versicherungsnehmer und handelt nur im Umfang seiner Vollmacht; Direktanspruch und bloße Korrespondenzbefugnis sind nicht dasselbe. Interne Deckungsnachfrage und Außenantwort bleiben getrennte Schreiben. Ein Dank für die Meldung und Bedauern über die Belastung sind von einer rechtlichen Haftungszusage zu trennen.
2. Wiederhole nur den notwendigen Ereigniskern. Behauptungen mit „Nach Ihrer Schilderung“ kennzeichnen; belegte eigene Erkenntnisse nicht hinter Leerformeln verstecken. Keine unbelegten Vorwürfe an den Fahrgast.
3. Frage fehlende Nachweise einzeln mit Zweck ab: Kaufdatum zur Sachbewertung, Erstbefund zur Verletzung, Fahrtbeleg zur Ausgabe. Verlange nicht vorsorglich die gesamte Krankenhistorie oder sämtliche privaten Kontoauszüge.
4. Sage konkret, welcher Schritt als Nächstes bearbeitet wird und wann eine Rückmeldung vorgesehen ist. Keine Abschlussfrist versprechen, die von ungeklärter Technik, Gutachten oder Deckung abhängt. Eine Zwischenantwort ist kein Verjährungsverzicht.
5. Bei Teilregulierung Betrag, Position, Anrechnung und nicht erledigte Punkte ausformulieren. Bei Ablehnung den tragenden Tatsachen- oder Rechtsgrund nennen und unterscheiden, ob etwas widerlegt, nicht belegt oder noch in Prüfung ist.
6. Prüfe Anerkenntnis- und Verjährungswirkung nach Erklärungsinhalt. Die Floskel „ohne Anerkennung einer Rechtspflicht“ ist kein universeller Schutz. Bei Anwaltsschreiben Vertretung und geeigneten Kommunikationsweg beachten; keine automatischen Außenhandlungen.

## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md), [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). BGB Paragraf 203 zu Verhandlungen und Paragraf 212 zum Neubeginn gesondert prüfen. VVG Paragraf 105 nicht als pauschales Kontakt- oder Entschuldigungsverbot missverstehen.

## 5. Ausgabeformat

Adressat, Datum, eigene und fremde Vorgangsnummer, aussagekräftiger Betreff, Anrede, verständlicher Text, konkrete nächste Schritte, Anlagen und Unterschriftszeile. Vollständige Sätze statt einer Bausteinliste. Times New Roman 11 pt soweit möglich und dezimale Gliederung nur soweit der Brief sie benötigt. Interne Freigabehinweise außerhalb des versandfertigen Textes halten; kein erfundener Dateilink.

## 6. Beispiel

„Wir haben Ihre Unterlagen zur Hose erhalten. Für die technische Prüfung liegt uns bisher nur das nach dem Vorfall erstellte Prüfprotokoll vor. Wir haben daher die Aufzeichnungen zum Fahrtzeitpunkt angefordert und melden uns bis zum [intern bestätigtes Datum] zum Stand dieser Anforderung.“ Nur als Entwurf verwenden, solange die Anforderung nicht wirklich versandt wurde.

---

## Skill: `versicherung-einschalten`

_Erstellt die Haftpflicht-Schadenanzeige und klärt Police, versichertes Unternehmen, Tätigkeit, Zeitraum, Selbstbehalt, Deckung und Regulierungsvollmacht. Erkennt Anzeige- und Prozessfristen, trennt Vorbehalt von Deckungszusage und vermeidet falsche Aussagen über Anerkenntnisverbote oder Direktansprüche._

# Versicherung einschalten

## 1. Zweck und Anwendungsfall

Der Betrieb muss einen möglichen Haftpflichtfall melden oder eine bereits gemeldete Forderung dem richtigen Versicherer und Sachbearbeiter zuordnen. Dieser Skill führt die Versicherungsseite, ohne die Haftungsentscheidung vorwegzunehmen. Arbeitet der Nutzer bereits als regulierender Versicherer, verwende `haftpflichtschaden-regulieren` statt eine Meldung an sich selbst zu erzeugen. Bei Abschleppunternehmen Tätigkeit, Obhutsschaden und Kfz-Risiko ausdrücklich mit den tatsächlichen Vertragsklauseln abgleichen; der Policentitel allein genügt nicht.

## 2. Eingaben

Police und Nachträge, versicherte Rechtsträger und Tätigkeit, Ereignisdatum, erster Kenntnistag, Anspruchsschreiben sowie bisherige Korrespondenz lesen. Ein Versicherungsauszug ist kein Beleg für nicht enthaltene Ausschlüsse. Fehlt die Police, fertige die Meldung mit benannter Policenlücke und fordere den Vertrag gezielt an.

## 3. Ablauf

1. Match nach Risiko und Vertrag, nicht nach dem Versichererlogo: Betriebshaftpflicht, Kfz-Haftpflicht, Produkthaftpflicht oder eigene Sachversicherung. Versicherungsfallprinzip, Versicherungsperiode, örtlicher Geltungsbereich und Nachmeldebestimmungen nur aus tatsächlichen Bedingungen übernehmen.
2. Nach VVG Paragraf 104 mögliche Verantwortlichkeit und spätere Anspruchserhebung jeweils binnen einer Woche anzeigen; gerichtliche Inanspruchnahme, Prozesskostenhilfe, Streitverkündung und einschlägiges Ermittlungsverfahren unverzüglich. Erkennbare Fristen zunächst kalendern; Obliegenheitsfolgen nur anhand wirksamer Regelung und Voraussetzungen prüfen.
3. Anzeige mit Bekanntem erstellen: Ereignis, eigene Rolle, Geschädigter, Verletzung, Sachschaden, vorhandene Belege, bisherige Erklärungen und dringende Sicherung. Unbekannte Schadenshöhe ausdrücklich offenlassen. Ein fehlender Arztbericht rechtfertigt keinen Meldestillstand.
4. Erbitte Eingangsbestätigung, Schadennummer, Ansprechpartner, Deckungsstand, Beauftragungs- und Regulierungsvollmacht sowie Vorgehen bei Sofortkosten. VVG Paragraf 100 und Paragraf 101 betreffen Freistellung und Abwehr, nicht nur die spätere Zahlung.
5. Unterscheide „Meldung eingegangen“, „Deckung unter Vorbehalt“ und „Deckung bestätigt“. Ein Selbstbehalt betrifft zunächst den internen Risikotransfer und mindert nicht automatisch den Anspruch des Geschädigten.
6. Behaupte kein pauschales Anerkenntnisverbot: VVG Paragraf 105 erklärt entsprechende Leistungsfreiheitsvereinbarungen für unwirksam. Ein eigenmächtiges Anerkenntnis bindet den Versicherer aber nicht automatisch über den gesetzlichen Haftungsumfang hinaus. Vor einer Bindung Freigabe und Vollmacht klären.
7. Einen Direktanspruch nach VVG Paragraf 115 nur nach seinen besonderen Voraussetzungen prüfen; nicht jede Betriebshaftpflicht eröffnet ihn. Bei gerichtlicher Post laufen Prozessfristen unabhängig von der Reaktionszeit des Versicherers weiter.

## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md), insbesondere amtliches VVG Paragraf 100 bis Paragraf 106 und Paragraf 115, sowie [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). Bei Eigenschäden VVG Paragraf 86 gesondert beachten. Vertragszitate erhalten Klauselnummer, Fassung und Datei.

## 5. Ausgabeformat

Vollständig ausformulierte Schadenanzeige und kurze Deckungsabfrage; daneben Fristentabelle und fehlende Vertragsseiten. Keine ungeprüfte Freigabe und kein tatsächlicher Versand. Times New Roman 11 pt soweit möglich, dezimale Gliederung; ohne Dateiwerkzeuge verwendbaren Nachrichtentext liefern.

## 6. Beispiel

Eine Police sieht 2500 EUR Selbstbehalt vor, der Fahrgast verlangt 468 EUR und ein noch unbeziffertes Schmerzensgeld. Melde den Personenschaden auch dann, wenn der bisher bezifferte Betrag unter dem Selbstbehalt liegt; verwechsle diesen nicht mit einer Haftungsfreigrenze.

---

## Skill: `haftpflichtschaden-regulieren`

_Bearbeitet einen Haftpflichtschaden aus Sicht des regulierenden Versicherers: Deckungsstand, Anspruchsprüfung, Besichtigung, Reserve, Abwehr, Teilzahlung und Vergleich. Für Schadenbearbeiter mit bestehender Schadenakte und geklärtem Mandat; nicht nur eine Schadenanzeige des versicherten Unternehmens._

# Haftpflichtschaden regulieren

## 1. Zweck und Anwendungsfall

Der Haftpflichtversicherer führt die Abwicklung für ein versichertes Unternehmen. Liefere die jetzt benötigte Entscheidungsvorlage und das passende Schreiben. Prüfe berechtigte wie unbegründete Positionen; die Versichererperspektive ist kein Auftrag zur pauschalen Kürzung.

## 2. Eingaben

Lies Schadenmeldung, letzte Bearbeitungsnotiz, Anspruchsschreiben, Versicherungsschein mit Bedingungen und Vollmacht. Übernimm vorhandene Schadennummer und Sachbearbeiter. Unterscheide Versicherungsnehmer, mitversicherte Person, Geschädigten, Vertreter und weiteren Versicherer. Fehlt allein eine Bedingungsseite, sichere den Tatsachenstand und fordere genau diese Seite an.

## 3. Ablauf

### 3.1. Deckung, Haftung und Außenbefugnis trennen

Halte drei getrennte Entscheidungen fest: Deckung gegenüber dem Versicherungsnehmer, Haftung gegenüber dem Geschädigten und Befugnis zur Außenregulierung. Eine interne Reserve ist weder Haftungsanerkenntnis noch Angebot. Ein Schadenaktenzeichen beweist keinen Direktanspruch.

### 3.2. Versichertes Risiko bestimmen

VVG Paragraf 100 und Paragraf 101 betreffen Freistellung und Abwehr. Bestimme anhand des Vertrags versicherte Tätigkeit, Zeitraum, Ausschlüsse, Selbstbehalt und Kostenregelung. Bei Abschleppbetrieben Schäden an übernommenen Fahrzeugen, Tätigkeitsschäden, Obhut, Transport und Kfz-Risiko ausdrücklich anhand der vorhandenen Klauseln abgleichen. Aus „Betriebshaftpflicht“ folgt keine automatische Deckung jeder Beschädigung.

### 3.3. Deckungsmitteilung begrenzen

Bereite eine begrenzte Deckungsmitteilung vor: bestätigte Punkte, genaue offene Vertrags- oder Tatsachenfrage, erbetener Beleg und nächste Prüfung. Fehlende Deckung ist keine materiell-rechtliche Ablehnung des Geschädigtenanspruchs. Mögliche Interessenkonflikte bei gemeinsamer Vertretung oder Rückgriff gesondert eskalieren.

### 3.4. Besichtigung und Aufklärung organisieren

Organisiere die entscheidende Aufklärung mit Kostenfreigabe, Untersuchungsumfang, Beteiligten und Termin. Eine Besichtigung darf Beweiserhaltung und zumutbare Reparatur nicht auf unbestimmte Zeit blockieren. Keine heimliche Weisung, belastendes Material zu entfernen; Originalbefunde bleiben erhalten.

### 3.5. Forderungen und interne Reserve prüfen

Prüfe jede Forderung nach Anspruchsinhaber, Haftungsgrund, Kausalität, Beleg, Umsatzsteuer, Vorzahlung und offenem Rest. Reserve aus begründeten Szenarien und erwarteten Abwehrkosten intern dokumentieren, nicht als mathematischen Anspruchswert verkaufen. Keine willkürliche Quote allein wegen lückenhafter Unterlagen.

### 3.6. Regulierungsweg zur Freigabe vorlegen

Lege begründete Abwehr, weitere Aufklärung, unstreitige Teilregulierung oder Vergleich zur Freigabe vor. Das Außenanschreiben enthält keine internen Reserven. Bei der üblichen Betriebshaftpflicht ausdrücklich im Namen und Auftrag des bezeichneten Versicherungsnehmers handeln, soweit die Vollmacht das trägt; VVG Paragraf 115 nur bei erfüllten besonderen Voraussetzungen als Direktanspruch behandeln.

### 3.7. Fälligkeit und Prozessfristen sichern

VVG Paragraf 106: Die Zweiwochenfrist betrifft die dort geregelte bindende Feststellung beziehungsweise Befriedigung und Kostenmitteilung, nicht pauschal zwei Wochen nach jeder Erstmeldung. Gerichtliche Fristen und erforderliche Abwehr laufen unabhängig davon weiter. VVG Paragraf 105 ist kein allgemeines Anerkenntnisverbot.

### 3.8. Zahlung und Aktenabschluss kontrollieren

Vor Zahlung Anspruchsinhaber, Konto, Vorleistungen, Abtretungen und Freigabe prüfen. Kaskoleistung kann nach VVG Paragraf 86 einen Übergang bewirken; Selbstbehalt und nicht ersetzte Positionen verbleiben nicht automatisch ebenfalls beim Kaskoversicherer. Abgeschlossene Positionen quittieren, den offenen Rest mit Wiedervorlage fortführen. Kein Versand, Vergleich oder Zahlungsauftrag ohne gesonderte Autorisierung.


## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). Gesetz und konkrete Versicherungsbedingungen getrennt belegen. Der Abschleppanker BGH, Urteil vom 18.02.2014, VI ZR 383/12, betrifft den öffentlich beauftragten Unternehmer und den Anspruchsgegner, nicht die Deckung einer beliebigen Abschlepppolice.

## 5. Ausgabeformat

Liefere eine interne Regulierungsvorlage mit Deckungsstand, Haftung, Positionsrechnung, Aufklärungsbedarf, Reservegrund und Freigabe; getrennt davon einen vollständig formulierten Außenbrief. Keine internen Überlegungen versehentlich als Anlage mitsenden. Times New Roman 11 pt soweit möglich, dezimale Gliederung. Ohne Export verwendbaren Text liefern.

## 6. Beispiel

Ein Abschleppbetrieb meldet einen beschädigten Schweller. Die Police enthält eine besondere Obhutsklausel, der öffentliche Auftrag ist noch nicht vollständig vorgelegt. Bereite Besichtigung und begrenzte Deckungsnachforderung vor; entscheide nicht aus dem Vorliegen der Police, dass der Betrieb dem Halter persönlich haftet oder bereits eine Zahlung zugesagt sei.

---

## Skill: `regress-und-anspruchsuebergang`

_Ordnet Schadenforderungen zwischen Geschädigtem, Krankenkasse, Arbeitgeber und Sachversicherer zu. Prüft sachlich und zeitlich entsprechende Leistungen, Anspruchsübergänge und Rückgriff gegen weitere Verantwortliche; verhindert Doppelzahlungen und eine Abfindung fremder Ansprüche ohne Berechtigung._

# Regress und Anspruchsübergang

## 1. Zweck und Anwendungsfall

Eine Krankenkasse meldet Heilbehandlungskosten, ein Arbeitgeber Entgeltfortzahlung oder das Unternehmen will bei Wartungsfirma oder Hersteller Rückgriff nehmen. Trenne Anspruchsinhaberschaft und Haftungsgrund von der bloßen Zahlstelle.

## 2. Eingaben

Leistungsaufstellung mit Zeitraum und Leistungsart, Versicherungsdaten, Entgeltfortzahlungsnachweis, Abtretung, eigene Zahlungen und Verträge mit weiteren Verantwortlichen. Eine pauschale Regressankündigung ist noch keine vollständig belegte Forderung.

## 3. Ablauf

1. Ordne jede Position einem ursprünglichen Gläubiger, möglichen Übergangstatbestand, Leistungsträger und Zeitraum zu. Nach SGB X Paragraf 116 sachliche und zeitliche Kongruenz und die weiteren Voraussetzungen prüfen. Die bloße Mitgliedschaft in einer Krankenkasse überträgt nicht sämtliche Ansprüche.
2. Schmerzensgeld, eigener Sachschaden und selbst getragene Kosten bleiben von übergegangenen Heilbehandlungskosten zu unterscheiden. Dieselbe Behandlung darf nicht vollständig an den Fahrgast und zusätzlich an die Krankenkasse bezahlt werden.
3. Bei Entgeltfortzahlung EntgFG Paragraf 6, bei eigener Sachversicherung VVG Paragraf 86 prüfen. Zahlende Stelle, tatsächliche Leistung, Umfang, Vorrechte und gegebenenfalls Quotenvorrecht nicht durch die Haftungsquote ersetzen.
4. Bei mehreren Verantwortlichen Außenhaftung, gesamtschuldnerischen Ausgleich nach BGB Paragraf 426, gegebenenfalls HaftPflG Paragraf 13 und vertraglichen Rückgriff auseinanderhalten. Bei hoheitlichem Abschleppen Verwaltungsträger im Außenverhältnis und vertraglichen Rückgriff gegen den Unternehmer nicht vermengen. Nach Kaskozahlung Betrag, Selbstbehalt, Restpositionen und Übergang nach VVG Paragraf 86 abgleichen; eine bloße Kaskomeldung ist noch keine Leistung. Ein Werkstattauftrag beweist keinen Wartungsfehler. Herstellersicherung und technische Prüfung dürfen nicht zur Belegvernichtung führen.
5. Behandle den eigenen Unternehmensschaden in einem getrennten Forderungsblatt mit eigenen Anspruchs- und Verjährungsvoraussetzungen. Aufrechnung nur bei tatsächlich bestehender Gegenforderung und zulässiger Aufrechnungslage prüfen; kein automatisches „Netting“.
6. Fordere fehlende Regressangaben zielgenau an. Prüfe bei Zahlung oder Vergleich, ob der Empfänger über die Position verfügen darf. Fremde oder bereits übergegangene Ansprüche ausdrücklich außerhalb einer persönlichen Abfindung belassen.

## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). SGB X Paragraf 116 einschließlich etwaiger Begrenzungen, EntgFG Paragraf 6, VVG Paragraf 86 sowie BGB Paragraf 426 anhand der konkreten Leistung prüfen. Eine Quellenliste ersetzt keine Abgrenzung der Gläubiger.

## 5. Ausgabeformat

Gläubigertabelle „Position / Zeitraum / Leistung / Rechtsübergang / Empfänger / Zahlungsstand“ und ein vollständig ausformulierter Antwortentwurf. Keine abschließende Regressquote ohne Daten. Format soweit möglich Times New Roman 11 pt und dezimale Gliederung. Fehlende Unterlagen blockieren nur die betroffene Position.

## 6. Beispiel

Der Fahrgast verlangt eine Zuzahlung, die Krankenkasse Behandlungskosten und der Arbeitgeber fortgezahltes Entgelt. Das sind drei getrennte Prüfungen; die Freigabe eines Hosenersatzes erledigt keine dieser drei Forderungen.

---

## Skill: `vergleich-und-zahlung-abschliessen`

_Führt eine geprüfte Schadenforderung zur kontrollierten Teilzahlung, Abfindung oder Ablehnung und zum Aktenabschluss. Klärt Vollmacht, Versichererfreigabe, Anspruchsinhaberschaft, Zukunftsschäden, Anrechnung und Zahlungsempfänger; erstellt Vergleich und Freigabevorlage, löst aber keine Zahlung aus._

# Vergleich und Zahlung abschließen

## 1. Zweck und Anwendungsfall

Haftung und Schaden sind ausreichend aufgeklärt oder ein bewusst begrenzter Vergleich soll Unsicherheit beenden. Die Aufgabe endet nicht mit „zahlen“, sondern mit eindeutiger Leistungszuordnung, Freigabe und überprüfbarem Abschlussstand.

## 2. Eingaben

Aktuelle Positionsrechnung, Haftungsvermerk, Deckungsstand, Vergleichsmandat, bekannte Folgeschäden, bisherige Zahlungen, Regressanmeldungen und verifizierte Empfängerdaten. Fehlt eine wesentliche Freigabe, fertige einen Entwurf ohne vorgetäuschte Abschlussreife.

## 3. Ablauf

1. Trenne Abschlag, Teilregulierung und endgültige Abfindung. Ein Abschlag benötigt klare Anrechnung; eine Abfindung benötigt einen eindeutig vereinbarten Erledigungsumfang. BGB Paragraf 779 verlangt für den Vergleich die entsprechenden Voraussetzungen.
2. Beschreibe den Vorgang und die erfassten Positionen. Prüfe, ob unbezifferte Zukunftsschäden eingeschlossen werden sollen, medizinisch hinreichend überschaubar sind und die Verfügung dem Berechtigten zusteht. Bei unklarem Verlauf zunächst bezifferte Schäden oder einen klar abgegrenzten Teil vergleichen.
3. Ansprüche von Krankenkasse, Arbeitgeber, Kaskoversicherer oder Leasingeigentümer nicht ohne Berechtigung erledigen. Beim Abschleppen Ausführungsschaden, Abschleppgebühr und Rückgriff des öffentlichen Auftraggebers getrennt behandeln. Eine globale Formulierung „sämtliche Ansprüche aller Beteiligten“ darf diese Prüfung nicht ersetzen.
4. Lege Betrag, Zahlungsfrist, Empfänger, Anrechnung früherer Zahlungen, Kosten und Umfang eines Vorbehalts fest. Rechtlich oder medizinisch offene Punkte ausdrücklich in der internen Freigabe kennzeichnen. Ein Vergleichsentwurf darf selbst keine verbindliche Zusage auslösen.
5. Prüfe Vertretung, interne Zeichnungsgrenze und Versichererbefugnis. Zahlungsdaten mit einer vertrauenswürdigen bereits bekannten Quelle abgleichen; ein geändertes Konto in einer einzelnen E-Mail reicht nicht. Zahlung und Bankfreigabe erfolgen außerhalb dieses Skills durch Berechtigte.
6. Prüfe Verjährung, Hemmung und Anerkenntniswirkung positions- und gläubigerbezogen. Nicht unterstellen, dass alle Ansprüche durch fortlaufende Korrespondenz unbegrenzt gehemmt sind.
7. Abschließen erst nach belegter Annahme und Zahlung beziehungsweise begründeter Ablehnung mit geregelter Wiedervorlage. Offene Krankenkassenforderung, möglicher Rückgriff und unklare Spätfolgen behalten getrennte Status. Sicherheitsmaßnahmen des Betriebs laufen unabhängig von der Entschädigung weiter.

## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md), [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). BGB Paragraf 195, Paragraf 199, Paragraf 203, Paragraf 212 und Paragraf 779, VVG Paragraf 105 und Paragraf 106 sowie einschlägige Anspruchsübergänge. Rechtswirkung anhand des konkreten Wortlauts, nicht allein einer Überschrift prüfen.

## 5. Ausgabeformat

Vollständig ausformulierter Vergleich oder Zahlungs-/Ablehnungsbrief; daneben interne Freigabe mit offenen Sperren und eine Abschlussliste mit tatsächlichen Erledigungsnachweisen. Keine Klauselskelette. Soweit möglich Times New Roman 11 pt, dezimale Gliederung. Ohne Export Text liefern; ein fehlender Zahlungsnachweis darf nicht durch „erledigt“ ersetzt werden.

## 6. Beispiel

Der Sachschaden steht fest, die Behandlung dauert an. Eine sachlich begrenzte Teilzahlung ist von einer umfassenden Personenschadenabfindung zu trennen. Ein bereits vorgemerkter Krankenkassenregress bleibt in einem eigenen Teilvorgang offen.

---

## Skill: `schadenpositionen-pruefen`

_Prüft geltend gemachte Personen- und Sachschäden positionsweise anhand von Befunden, Kaufbelegen und Ausfällen. Trennt Schmerzensgeld, Kleidung, Behandlungskosten und Verdienstausfall, berücksichtigt psychische Unfallfolgen ohne Eigendiagnose und liefert eine nachvollziehbare Regulierungsvorlage._

# Schadenpositionen prüfen

## 1. Zweck und Anwendungsfall

Die Forderung ist ganz oder teilweise beziffert. Prüfe jede Position nach Schaden, Ursachenzusammenhang, erforderlichem Aufwand, Gläubiger und Nachweis; eine offene psychische Folge darf nicht die Prüfung eines belegten Sachschadens blockieren.

## 2. Eingaben

Forderung, Kauf- und Zahlungsbelege, Alter und Zustand der Sache, Reparaturauskunft, Behandlungsberichte, Zuzahlungen, Arbeitsunfähigkeit, Entgeltfortzahlung und vorhandene Zahlungen. Gesundheitsangaben nur soweit erforderlich auswerten; eine allgemeine Schilderung ersetzt keine vollständige Krankenakte und rechtfertigt auch nicht deren pauschale Anforderung.

## 3. Ablauf

1. Erstelle eine Zeile pro wirtschaftlichem Schaden. Trenne gefordert, belegt, noch zu prüfen, bereits bezahlt und möglicherweise übergegangen. Keine Vermengung von Haftungsquote, Deckungsselbstbehalt und Sachwertabzug.
2. Bei Kleidung Eigentum, Kaufdatum, tatsächlich gezahlten Preis, Vorschaden, Reparaturfähigkeit und verbleibende Nutzbarkeit prüfen. Kein automatischer Neupreis und keine frei erfundene jährliche Abschreibung. Eine beschädigte Hose kann getrennt von einer eingeklemmten, aber unbeschädigten Jacke zu behandeln sein.
3. Bei Abrasionen Erstbefund, Wundversorgung, Heilungsverlauf, Schmerzen, Narben und Alltagseinschränkungen erfassen. Zwischen Patientenschilderung und medizinischem Befund unterscheiden. Keine Diagnose oder Dauerfolge aus einem Foto ableiten.
4. Angst, Schlafstörung und Vermeidungsverhalten ernst nehmen, ohne automatisch eine posttraumatische Belastungsstörung zu behaupten. Direkte Unfallbeteiligung ist kein mittelbarer Angehörigen-Schockschaden. Ist schon eine Körperverletzung belegt, können die erlittene Angst und der Verlauf in die Gesamtbemessung eingehen; eine zusätzliche eigenständige Diagnose ist nicht pauschal Voraussetzung jeder Berücksichtigung.
5. Schmerzensgeld nach BGB Paragraf 253 Absatz 2 beziehungsweise HaftPflG Paragraf 6 Satz 2 insgesamt bewerten. Vergleichsentscheidungen nur bei hinreichend ähnlichen Verletzungen, Verlauf und Entscheidungszeitpunkt verwenden. Keine Tagessatzrechnung oder automatische Addition eines Angstpauschalbetrags.
6. Behandlungs-, Fahrt- und Betreuungskosten nach Erforderlichkeit und tatsächlichem Träger prüfen. Arbeitsunfähigkeit allein beweist keinen eigenen Nettoverdienstausfall. Haushaltstätigkeit, Ausfalltage und Ersatzhilfe konkretisieren, statt eine Monatspauschale zu unterstellen.
7. Bei Fahrzeugschäden Vorschaden, neue Beschädigung, Reparaturkalkulation und tatsächliche Rechnung trennen. Umsatzsteuer nach BGB Paragraf 249 Absatz 2 Satz 2 nur soweit angefallen; Vorsteuerabzug gesondert prüfen. Mietwagen, Nutzungsausfall und gewerblichen Ausfall nicht für dieselbe Beeinträchtigung doppelt ansetzen. Leasingeigentum, Reparaturermächtigung, Abtretung und Kaskovorleistung vor einer Zahlung klären.
8. Additionen mit Dezimalarithmetik oder überprüfbarer Rechnung kontrollieren. Umsatzsteuer bei Sachschäden nur im rechtlich maßgeblichen Umfang; Vorsteuerabzug beim Unternehmen prüfen. Schmerzensgeld bleibt außerhalb einer rein rechnerischen Zwischensumme.

## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md), [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). BGH, Urteil vom 15.02.2022, VI ZR 937/20, Randnummer 13 ff.: Gesamtbetrachtung statt taggenauer Berechnung. BGH, Urteil vom 06.12.2022, VI ZR 168/21, Randnummer 13 ff.: psychische Störung von Krankheitswert; der Ausgangsfall war ein mittelbarer Schockschaden. BGB Paragraf 249 bis Paragraf 254; ZPO Paragraf 286 und Paragraf 287 nicht austauschbar verwenden.

## 5. Ausgabeformat

Positionsrechnung mit Einheiten, Belegen, Vorzahlungen und offener Differenz sowie ein ausformuliertes Ergebnis mit begründetem Nachforderungsbedarf. Keine erfundene gerichtliche Betragsgarantie. Schreiben in vollständigen Sätzen, Times New Roman 11 pt soweit möglich, dezimale Gliederung. Bei fehlendem Tabellenexport die Rechnung im Text mit Rechenweg liefern.

## 6. Beispiel

Zur Hose liegen 329 EUR Kaufpreis und 84 EUR Reparaturangebot vor, zu weiteren Fahrtkosten nur eine Liste. Prüfe Reparaturumfang, Eignung und Zahlungsnachweis; entscheide nicht allein nach dem kleineren Betrag. Trenne das von ärztlich noch ungeklärten Folgebeschwerden.

---

## Skill: `haftungsweg-bestimmen`

_Prüft die Verantwortlichkeit des in Anspruch genommenen Unternehmens aus Vertrag, Delikt und einschlägiger Gefährdungshaftung. Unterscheidet U-Bahn und Straßenverkehr, Betreiber und Hersteller sowie Haftung, Mitverschulden und Beweislast; keine bloße Normensammlung und keine Deckungsprüfung._

# Haftungsweg bestimmen

## 1. Zweck und Anwendungsfall

Klärung, ob und weshalb das Unternehmen für den konkreten Schaden einstehen muss. Beginne mit dem geltend gemachten Vorgang und der stärksten tragfähigen Anspruchsgrundlage, nicht mit sämtlichen denkbaren Haftungsarten.

## 2. Eingaben

Nutze Ereignisbericht, Vertrag oder Fahrschein, beteiligte Rechtsträger, Betriebsunterlagen und Gegenposition. Fehlt die eigene Rolle, kläre sie vor einer Empfehlung. Fehlende Deckungsunterlagen hindern die Haftungsprüfung nicht.

## 3. Ablauf

1. Ordne Vertrag und Anspruchsteller zu. Bei vertraglichen Schutzpflichten BGB Paragraf 280 Absatz 1 in Verbindung mit Paragraf 241 Absatz 2 prüfen, einschließlich Vertretenmüssen und Erfüllungsgehilfen nach Paragraf 278. Die Entlastung zum Vertretenmüssen ersetzt nicht den Nachweis aller übrigen Voraussetzungen.
2. Bei Körper-, Gesundheits- oder Eigentumsverletzung BGB Paragraf 823 Absatz 1 prüfen. Mitarbeiterzurechnung nicht pauschal mit der vertraglichen Haftung vermengen; Paragraf 831 und gegebenenfalls Organ- und Organisationshaftung unterscheiden.
3. Bei Schienenbetrieb HaftPflG Paragraf 1: Betriebsunternehmer, Betriebszusammenhang, Rechtsgutsverletzung, Kausalität, höhere Gewalt; mitgeführte Kleidung ist nicht pauschal vom Sachschutz ausgeschlossen. Paragraf 4, Paragraf 6 sowie Haftungshöchstbeträge und Anspruchskonkurrenz getrennt prüfen.
4. Bei Kraftfahrzeugen erst den Anwendungsbereich des StVG feststellen, dann insbesondere Paragraf 7, Paragraf 18 und gegebenenfalls Paragraf 17 prüfen. Eine U-Bahn ist nicht aufgrund der Unternehmensbranche ein Kraftfahrzeug. PBefG und BOStrab bestimmen unter anderem betriebliche Anforderungen, aber keinen universellen Auszahlungsanspruch.
5. Bei Produktfehlern Hersteller und Betreiber auseinanderhalten. Nach ProdHaftG Paragraf 1 trägt grundsätzlich der Geschädigte Fehler, Schaden und Ursachenzusammenhang vor und beweist sie. Sachschäden erfordern eine andere, privat bestimmte und überwiegend privat verwendete Sache; Paragraf 11 regelt die Selbstbeteiligung. Diese Einschränkungen nicht auf andere Anspruchsgrundlagen übertragen. Ereignis- und Inverkehrbringensdatum wegen gesetzlicher Übergänge prüfen.
6. Formuliere jede Einwendung mit Tatbestandsmerkmal und Beleg. Mitverschulden nach BGB Paragraf 254 beziehungsweise HaftPflG Paragraf 4 nicht allein aus der Unfallbeteiligung ableiten. Eine Abfahrtswarnung beweist weder verspäteten Ausstieg noch die Ursächlichkeit eines Fehlverhaltens.
7. Bei Abschleppschäden zuerst Auftraggeber und hoheitliche oder private Ausführung klären. BGB Paragraf 839 mit Artikel 34 GG und öffentlich-rechtliche Verwahrung können den Anspruch gegen den Verwaltungsträger lenken; BGH, Urteil vom 18.02.2014, VI ZR 383/12, nicht als generelle Haftung des Abschleppunternehmers missverstehen. Für diese Rollenprüfung `abschleppschaden-pruefen` nutzen. Rechtmäßigkeit, Kosten und Ausführungsschaden bleiben getrennt.
8. Ergebnis in unstreitige Voraussetzungen, streitige Voraussetzungen, verfügbare Beweise und verbleibendes Risiko trennen. Keine Haftungsquote aus unbelegten Prozentannahmen erzeugen.

## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). Normfassung zum Ereignisdatum, danach aktuelle Fortentwicklung prüfen. BGH, Urteil vom 06.12.2022, VI ZR 168/21, betrifft die eigene psychische Gesundheitsverletzung bei mittelbar ausgelöstem Schockschaden; das ist kein Urteil über Berliner U-Bahn-Türen und keine feststehende Haftungsquote.

## 5. Ausgabeformat

Begründeter Haftungsvermerk mit einer Tabelle „Anspruch / Voraussetzung / Beleg / Beweislast / Einwendung / Folge“. Der entscheidende Begründungstext steht in vollständigen Sätzen, nicht in einem Stichwortgerüst. Format soweit möglich Times New Roman 11 pt, ausschließlich dezimal. Eine offene Quellenprüfung sperrt die rechtliche Freigabe des betroffenen Punkts, nicht den gesamten Tatsachenentwurf.

## 6. Beispiel

Beim Einklemmen einer Jacke während des Aussteigens untersuche zunächst Betreiber und Betriebsvorgang. Eine mögliche Fehlfunktion kann für einen Rückgriff gegen einen Hersteller relevant sein, ist aber nicht automatisch Voraussetzung jeder Betreiberhaftung.

---

## Skill: `unfallbelege-sichern`

_Sichert flüchtige Belege zu einem Schadenfall: Video, Tür- und Betriebsprotokolle, Produkt oder beschädigte Sache, Zeugen und Behandlungsunterlagen. Trennt eigene Wahrnehmung, Zeitstempel und Schlussfolgerung und formuliert konkrete Sicherungsanforderungen für das betroffene Unternehmen._

# Unfallbelege sichern

## 1. Zweck und Anwendungsfall

Verhindere, dass die spätere Haftungsprüfung an überschriebenen Bildern, entsorgten Sachen oder einer nur nacherzählten Beobachtung scheitert. Erstelle eine überprüfbare Belegkette, keine vorweggenommene technische oder medizinische Begutachtung.

## 2. Eingaben

Benötigt werden Ereigniszeit mit Zeitzone, Ort, Fahrzeug oder Produkt, bekannte Dateiquellen und erreichbare Zeugen. Suche diese Angaben im Bestand. Frage nur nach dem Identifikator, ohne den die Sicherungsanforderung ihr Ziel verfehlt. Verarbeite nur rechtmäßig bereitgestelltes Material; sensible Gesundheitsunterlagen nur im erforderlichen Umfang an berechtigte Empfänger geben.

## 3. Ablauf

1. Stelle Quelle, Verantwortlichen, Umfang und drohenden Verlust nebeneinander. Für Video: Kamera, Zeitfenster vor und nach dem Vorfall, Originalformat, Ton vorhanden oder nicht, geplante Überschreibung. Bitte um Sicherung, nicht ungeprüfte Weitergabe aller Aufnahmen.
2. Bewahre Originale unverändert; Arbeitskopie, Prüfsumme, Exportzeit und Bearbeitungsschritte getrennt dokumentieren, soweit Werkzeuge verfügbar sind. Ein Screenshot ersetzt weder Videosequenz noch ursprüngliche Logdatei.
3. Vergleiche Uhrquellen. Leitstellenzeit, Fahrzeugzeit und Zeugenhandy können abweichen. Rechne nur einen belegten Versatz um und behalte Originalzeiten. Schätzungen wie „ungefähr fünf Meter“ bleiben Schätzungen.
4. Frage Zeugen nach Standort, Sichtachse, Beginn der Wahrnehmung, konkreter Beobachtung und Erinnerungslücken. Keine suggestive Vorgabe wie „Die Tür muss defekt gewesen sein“. Ein späterer gemeinsamer Bericht ersetzt keine getrennten Aussagen.
5. Trenne technische Anzeige und tatsächlichen Zustand: „Tür geschlossen“ ist ein Signal, kein automatischer Nachweis freien Türraums. Ein unauffälliger Werkstatttest am nächsten Tag rekonstruiert nicht selbst den Unfallzustand. Bei Produktfällen Seriennummer, Charge, Umbau und Aufbewahrung erfassen.
6. Bei Abschleppvorgängen Auftrag, Beschilderung samt Zusatzzeichen zur Ereigniszeit, Ausgangsstandort, Aufnahme, Transport und Abstellort sichern. Aufnahmefotos müssen gerade die später beanstandete Stelle zeigen; fehlende Unterbodenbilder nicht als Schadensfreiheit werten. Hebepunkte, Hilfsrollen, bekannte Vorschäden und Zeitpunkt der Entdeckung getrennt aufnehmen. Besichtigung vor Reparatur ermöglichen, soweit zumutbar; ausgetauschte Teile zur beweissicheren Aufbewahrung anfordern.
7. Erstelle eine Chronologie nur aus belegten Ereignissen. Die Spalte „offen“ benennt die konkrete fehlende Quelle. Wurde eine Sicherungsbitte nur entworfen, ist der Status „nicht versandt“ und nicht „gesichert“.

## 4. Quellenpflicht

[Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md) und [Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md) beachten. BOStrab Paragraf 43 und Paragraf 54 für Tür- und Abfahrtthemen nur nach Anwendungsprüfung. ZPO Paragraf 286 und Paragraf 287 unterscheiden; eine Schadensschätzung heilt nicht jede fehlende Primärtatsache. Bei drohendem Verlust kann eine anwaltliche Prüfung eines selbständigen Beweisverfahrens nach ZPO Paragraf 485 sinnvoll sein, nicht ein allgemeiner Anspruch auf vorprozessuale Offenlegung.

## 5. Ausgabeformat

Eine versandfertig ausformulierte Sicherungsanforderung mit Adressat, Ereignis, exakt bezeichnetem Material und erbetener Rückmeldung; daneben die Chronologie mit Quelle und Unsicherheit. Keine leeren Listen als Endprodukt. Times New Roman 11 pt soweit möglich, dezimale Gliederung. Ohne Export Text liefern; bei fehlendem Lesewerkzeug die einzelne unlesbare Datei benennen und den Rest bearbeiten.

## 6. Beispiel

Ein Bahnsteigvideo zeigt erst den Nothalt, nicht den Moment des Einklemmens. Kennzeichne seinen begrenzten Ausschnitt und fordere das vorausgehende Fenster an; behaupte weder Widerlegung noch Bestätigung des gesamten Fahrgastberichts.

---

## Skill: `abschleppschaden-pruefen`

_Prüft Fahrzeugschäden beim Abschleppen aus Busspur, Haltestelle oder Privatfläche. Trennt Anordnung und Kosten von Ausführungsschaden, bestimmt öffentlichen oder privaten Auftraggeber, Anspruchsgegner und Versicherungsweg und klärt Vorschäden, Obhut, Reparatur und Anspruchsinhaber._

# Abschleppschaden prüfen

## 1. Zweck und Anwendungsfall

Ein Fahrzeug wurde umgesetzt und soll dabei beschädigt worden sein. Arbeite für den beauftragenden Betrieb, das Abschleppunternehmen oder dessen Haftpflichtversicherer, entsprechend dem tatsächlichen Mandat. Beginne nicht mit dem Satz, wer falsch parke, müsse sämtliche Schäden selbst tragen.

## 2. Eingaben

Lies Auftrag, Auftraggeber, Ort und Beschilderung zur Ereigniszeit, Einsatzprotokoll, Fahrzeugdaten, Übernahme- und Abstellzustand, Forderung und Police. Öffentlicher Straßenraum und Privatparkplatz sind unterschiedliche Ausgangslagen. Eine bloße Meldung des Busfahrers ist noch kein behördlicher Abschleppauftrag.

## 3. Ablauf

### 3.1. Anordnung, Kosten und Schaden trennen

Trenne drei Vorgänge: Rechtmäßigkeit der Anordnung, Abschleppkosten und Beschädigung bei Aufnahme, Transport oder Abstellen. Ein rechtmäßiger Auftrag erlaubt keine unsorgfältige Ausführung. Ein rechtswidriges Parken beweist weder den Schaden noch dessen Verursachung und erzeugt keine automatische Mithaftungsquote.

### 3.2. Beschilderung zur Ereigniszeit lesen

Für die Busspur Zeichen 245 mit Zusatzzeichen und zeitlicher Geltung dokumentieren. Zeichen 224 verbietet das Parken bis zu 15 Meter vor und hinter der Haltestelle, nicht jedes kurze Halten. StVO Paragraf 12 Absatz 2 unterscheidet Halten und Parken; weitere Verbote und konkrete Behinderung bleiben relevant. Keine pauschale bundesweite Abschleppbefugnis eines Verkehrsunternehmens behaupten.

### 3.3. Hoheitlichen Auftrag und Anspruchsgegner bestimmen

Auftraggeber und hoheitliche Grundlage anhand der Einsatzunterlagen bestimmen. Bei behördlicher Ersatzvornahme BGB Paragraf 839 mit Artikel 34 GG sowie das öffentlich-rechtliche Verwahrungsverhältnis prüfen. BGH, Urteil vom 18.02.2014, VI ZR 383/12: In dieser Konstellation ist der private Abschleppunternehmer hoheitlich tätig; der Außenanspruch ist nicht schlicht als Deliktsanspruch gegen ihn zu führen. Den Verwaltungsträger und einen möglichen internen Vertragsrückgriff getrennt ermitteln.

### 3.4. Eigene Befugnis und privaten Auftrag abgrenzen

Bei eigener Befugnis eines Verkehrsbetriebs das konkrete Landesrecht prüfen; in Berlin insbesondere MobG BE Paragraf 23 in der Ereignisfassung. Die Befugnisse der dort genannten BVG nicht auf jede private Busgesellschaft übertragen. Bei rein privatem Auftrag Vertragspartner, Eigentümer, Besitzschutz, mögliche Schutzwirkung und gegebenenfalls einschlägiges Frachtrecht anhand der übernommenen Leistung prüfen. Keine Übertragung des öffentlich-rechtlichen BGH-Falls auf jeden Privatparkplatz.

### 3.5. Obhutskette und Originalbelege sichern

Obhutskette aufbauen: Ausgangszustand, Aufnahmemethode, Zug- oder Hebepunkte, Radstellung, Hilfsrollen, Transport, Abstellplatz und Entdeckung. Originalfotos einschließlich Metadaten, Fahrzeughinweise und Aussagen sichern. Ein Foto ohne sichtbaren Unterboden beweist dessen Unversehrtheit nicht. Eine Unterschrift zur Fahrzeugübernahme ist nicht automatisch Verzicht auf verdeckte Schäden.

### 3.6. Vorschaden und Kausalität untersuchen

Jeden Kratzer und jede Verformung einzeln zuordnen. Vorschäden, Reparaturhistorie, Spurenlage und technische Kompatibilität sachverständig abgrenzen, ohne Kausalität aus dem zeitlichen Nacheinander allein zu folgern. Beweislast und mögliche Erleichterungen aus Obhut und Anspruchsgrundlage begründen; keine automatische Beweislastumkehr für sämtliche Schäden. Vor Reparatur zumutbare Besichtigungsmöglichkeit und Beweissicherung abstimmen.

### 3.7. Reparatur und Folgekosten beziffern

Kalkulation, tatsächliche Reparatur und Zahlungsbeleg unterscheiden. BGB Paragraf 249 Absatz 2 Satz 2: Umsatzsteuer nur soweit tatsächlich angefallen; Vorsteuerabzug gesondert. Erforderliche Mietwagenkosten, Nutzungsausfall und gewerblichen Ausfall nicht doppelt ansetzen. Standkosten, Gutachterkosten, Wertminderung und Sicherheitsbeeinträchtigung belegen statt pauschal addieren.

### 3.8. Anspruchsinhaber, Deckung und Fristen klären

Eigentum, Leasing, Reparaturermächtigung, Abtretung und Kaskovorleistung prüfen. Betriebshaftpflicht, Kfz-Haftpflicht des Abschleppfahrzeugs und Kasko nicht gleichsetzen. Haftung, Deckung, Direktanspruch nach VVG Paragraf 115 und Rückgriff nach VVG Paragraf 86 jeweils gesondert behandeln. Anordnungs- und Kostenrechtsbehelfe haben einen eigenen Fristenweg; kein Stillstand wegen laufender Regulierung.


## 4. Quellenpflicht

[Fachquellen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/haftung-und-regulierung.md), Abschnitt Abschleppen, und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/schadensregulierung/references/zitierweise.md). BGH VI ZR 383/12 nur innerhalb seiner hoheitlichen Auftragskonstellation verwenden. Aktuelle Landesnorm, Versicherungsbedingungen und eventuelles Frachtrecht vor Freigabe im Original prüfen; keine erfundenen Haftungsgrenzen.

## 5. Ausgabeformat

Liefere einen begründeten Vermerk mit getrennten Spalten „Anordnung und Kosten“, „Ausführung und Schaden“ und „Deckung und Rückgriff“, danach das tatsächlich benötigte Schreiben an Geschädigten, Versicherer, Auftraggeber oder Sachverständigen. Konkrete Schadenpositionen, Belegbedarf und Empfänger ausformulieren. Times New Roman 11 pt soweit möglich, dezimale Gliederung; bei fehlendem Export Text statt eines erfundenen PDF.

## 6. Beispiel

Ein Wagen steht in einer Busspur; nach dem Umsetzen zeigt sich eine Delle im Schweller. Die Felge hatte schon zuvor einen Randkratzer. Fordere den Auftrag und die Aufnahmedokumentation an, trenne beide Beschädigungen und die Abschleppgebühr. Ein Versichererbrief mit Schadennummer ersetzt weder den Nachweis der Delle noch die Prüfung des richtigen Anspruchsgegners.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
