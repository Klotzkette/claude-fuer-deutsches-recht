---
name: unterhaltsberechnung-vollpruefung
description: "Für Unterhaltsberechnung im Familienrecht: Vollprüfung: rechnet Beträge, Schwellen und Varianten; Ergebnis: Berechnungstabelle mit Annahmen und Kontrollfragen."
---

# Unterhaltsberechnung im Familienrecht: Vollprüfung

## Zweck und Anwendungsfall

Dieser Skill ist eine vollständige Vollprüfung für die Berechnung von Unterhalt im deutschen Familienrecht. Er führt von der Mandatslage über die Einkommensermittlung bis zum ausformulierten Berechnungsergebnis und deckt alle praktisch wichtigen Unterhaltsarten ab: Kindesunterhalt (minderjährig und volljährig), Trennungsunterhalt und nachehelichen Unterhalt.

Der Skill ist als fachlicher Vollprüfungsbaustein geschrieben. Er ersetzt keine anwaltliche Prüfung im Einzelfall.

## Eingaben

Erhebe zu Beginn nur das Nötigste; fehlt etwas, setze einen klar markierten Platzhalter `[noch zu klären: …]` und rechne mit einer ausdrücklich benannten Annahme weiter.

- Welche Unterhaltsart? (Kindesunterhalt, Trennungsunterhalt, nachehelicher Unterhalt, mehrere zugleich.)
- Rolle der Mandantin oder des Mandanten: unterhaltspflichtig oder unterhaltsberechtigt.
- Beteiligte: Kinder mit Geburtsdatum, Ehegatten, Betreuungssituation (Residenz- oder Wechselmodell).
- Einkommen beider Seiten (Art, Höhe, Belege), Wohnsituation, Schulden, vorrangige Pflichten.
- Stichtag der Berechnung und Datum der Verzugsbegründung oder Antragstellung.

## Quellenpflicht und Quellenhygiene

- Jede rechtliche Aussage wird belegt; Zitierweise nach `references/zitierweise.md`.
- Gesetzesnormen werden im Volltext über gesetze-im-internet.de geprüft.
- Tabellenwerte der Düsseldorfer Tabelle, Selbstbehaltssätze, Kindergeldhöhe und Mindestunterhalt sind **stichtagsabhängig** und werden vor Verwendung an der amtlichen Quelle (OLG Düsseldorf, zuständiges Bundesministerium) verifiziert. Dieser Skill enthält bewusst keine fest eingetragenen Eurobeträge, sondern den Rechenweg, in den die verifizierten Werte einzusetzen sind.
- Rechtsprechung wird nicht aus dem Gedächtnis zitiert. Aktenzeichen und Fundstellen werden vor jeder Verwendung in einer Schrift live über BGH-, OLG- oder frei zugängliche Datenbanken (dejure.org, openJur) verifiziert. Keine Kommentar-, Handbuch- oder Aufsatz-Blindzitate.

## Disclaimer-Hinweis

Beginne die Ausgabe mit einem kurzen Hinweis, dass es sich um eine methodisch geführte Berechnung handelt, deren tagesaktuelle Tabellen- und Rechtsprechungswerte zu verifizieren sind, und die keine Rechtsberatung im Einzelfall ersetzt.

## Ablauf

### Phase 0 — Sofort-Check

1. Bestimme die Unterhaltsart und die Rolle (pflichtig oder berechtigt). Bei mehreren Unterhaltsverhältnissen: alle benennen und die Rangfolge nach Paragraf 1609 BGB vormerken.

2. Markiere Stichtag und Verzug. Unterhalt für die Vergangenheit besteht erst ab Verzug, Auskunftsaufforderung oder Rechtshängigkeit (Paragraf 1613 BGB; für Trennungsunterhalt Paragraf 1361 i. V. m. Paragraf 1585b BGB). Kläre, ab welchem Monat gerechnet wird.

3. Prüfe Eilbedarf: Bei akutem Bedarf kommt eine einstweilige Anordnung in Betracht (Paragrafen 246 ff. FamFG); bei Auskunftsverweigerung die Stufenklage (Paragraf 254 ZPO).

4. Stelle die eine Frage, deren Antwort den größten Einfluss auf das Ergebnis hat, bevor du weiterrechnest (häufig: Höhe und Nachweis des bereinigten Nettoeinkommens der pflichtigen Person).

### Phase 1 — Bereinigtes Nettoeinkommen

Das unterhaltsrechtlich relevante Einkommen ist nicht das Steuer-Brutto und nicht das einfache Netto, sondern das **bereinigte** Nettoeinkommen. Ermittle es für jede Seite getrennt.

#### 1.1 Einkommensquellen

Erfasse alle Einkünfte: nichtselbständige Arbeit, selbständige Tätigkeit, Gewerbe, Kapitalvermögen, Vermietung, Renten, Sozialleistungen mit Lohnersatzcharakter, geldwerte Vorteile (Dienstwagen zur Privatnutzung, freie Kost und Logis).

#### 1.2 Nichtselbständige

Maßgeblich ist das Durchschnittsnetto der letzten zwölf Monate einschließlich anteiliger Sonderzahlungen (Weihnachts-, Urlaubsgeld, Boni, regelmäßige Überstunden). Steuererstattungen erhöhen, Nachzahlungen mindern das Einkommen im Zuflussjahr.

#### 1.3 Selbständige und Gewerbetreibende

1. Lege den Durchschnitt der letzten drei Wirtschaftsjahre zugrunde (Gewinn laut Jahresabschluss, nicht die Privatentnahmen).

2. Korrigiere unterhaltsrechtlich: Privatentnahmen, die den Gewinn übersteigen, deuten auf höhere Leistungsfähigkeit; rein steuerliche Abschreibungen (insbesondere degressive AfA, Sonderabschreibungen) werden ganz oder teilweise hinzugerechnet; private Kostenanteile (Pkw, Telefon) werden bereinigt.

3. Bei Verschleierung oder Erwerbsobliegenheitsverletzung ist ein fiktives Einkommen anzusetzen. Begründe die Schätzgrundlage und benenne den Auskunftsanspruch (Paragraf 1605 BGB) als Mittel der Aufklärung.

#### 1.4 Abzüge (in dieser Reihenfolge)

1. Steuern und Sozialabgaben (tatsächlich; bei Selbständigen Einkommensteuer und Kranken-/Pflegeversicherung).

2. Berufsbedingte Aufwendungen: pauschal regelmäßig 5 Prozent des Nettoeinkommens innerhalb eines von der Rechtsprechung gezogenen Rahmens, höhere Kosten nur gegen Beleg.

3. Altersvorsorge: primäre Vorsorge ist in den Sozialabgaben enthalten; zusätzliche (sekundäre) Altersvorsorge wird innerhalb der von der Rechtsprechung anerkannten Quote des Bruttoeinkommens abgesetzt. Den konkreten Prozentsatz für Kindes- und für Ehegattenunterhalt vor Verwendung verifizieren.

4. Berücksichtigungsfähige Verbindlichkeiten: ehebedingte und vor der Trennung begründete Kredite nach Abwägung; Zins und Tilgung werden gegen den Wohnvorteil und gegen den Unterhaltszweck abgewogen.

5. Wohnvorteil: Wer mietfrei im eigenen Heim wohnt, dem wird ein Wohnwert zugerechnet (im Trennungsjahr zunächst der angemessene, später der objektive Mietwert; Finanzierungslasten gegenrechnen).

#### 1.5 Zwischenergebnis

Stelle das bereinigte Nettoeinkommen jeder Seite als nachvollziehbares Tableau dar (Ausgangsbetrag, jede Position mit Vorzeichen, Endbetrag).

### Phase 2 — Kindesunterhalt

#### 2.1 Barunterhalt und Betreuungsunterhalt

Beim Residenzmodell erbringt der betreuende Elternteil den Unterhalt durch Pflege und Erziehung (Paragraf 1606 Abs. 3 Satz 2 BGB); der andere Elternteil schuldet Barunterhalt. Beim echten Wechselmodell haften beide anteilig nach ihren Einkommen bar; der Bedarf erhöht sich um Mehrkosten zweier Haushalte.

#### 2.2 Tabellenbedarf

1. Ordne das bereinigte Nettoeinkommen der barpflichtigen Person der zutreffenden Einkommensgruppe der Düsseldorfer Tabelle zu. Die Tabelle ist seit 2022 auf fünfzehn Einkommensgruppen erweitert und bleibt nach dem Stand 2026 bei fünfzehn Gruppen; die genauen Gruppengrenzen und Beträge des maßgeblichen Stands sind zu verifizieren.

2. Bestimme die Altersstufe des Kindes (Stufen nach vollendetem 5., 11., 17. Lebensjahr sowie ab Volljährigkeit) und entnimm den Tabellenbetrag.

3. Bei mehr oder weniger als zwei Unterhaltsberechtigten ist eine Höher- oder Herabstufung zu prüfen; halte das ausdrücklich fest.

#### 2.3 Kindergeldanrechnung

Das Kindergeld wird beim minderjährigen Kind zur Hälfte auf den Barunterhalt angerechnet (Paragraf 1612b Abs. 1 BGB); beim volljährigen Kind in voller Höhe. Der Zahlbetrag ist der Tabellenbetrag abzüglich des anzurechnenden Kindergeldanteils. Kindergeldhöhe und Mindestunterhalt (Paragraf 1612a BGB) sind stichtagsabhängig und zu verifizieren.

#### 2.4 Selbstbehalt und Mangelfall

1. Der barpflichtigen Person verbleibt mindestens der notwendige Selbstbehalt gegenüber minderjährigen und privilegiert volljährigen Kindern, gegenüber anderen Berechtigten der angemessene Selbstbehalt (Beträge verifizieren).

2. Reicht das Einkommen nach Abzug des Selbstbehalts nicht für alle gleichrangigen Bedarfe, liegt ein Mangelfall vor. Verteile die Verteilungsmasse im Verhältnis der Einsatzbeträge auf die gleichrangig Berechtigten und rechne die Quote vor.

3. Beachte die Rangfolge des Paragraf 1609 BGB: minderjährige und privilegiert volljährige Kinder zuerst, dann betreuende oder langjährig verheiratete Ehegatten, dann weitere.

#### 2.5 Volljährige und Studenten

1. Mit Volljährigkeit haften beide Elternteile anteilig nach ihren Einkommen (Paragraf 1606 Abs. 3 Satz 1 BGB); das Kind macht den Anspruch selbst geltend, das volle Kindergeld wird angerechnet.

2. Privilegiert volljährige Kinder (bis 21, im Haushalt eines Elternteils, allgemeine Schulausbildung) bleiben im ersten Rang (Paragraf 1603 Abs. 2 Satz 2 BGB).

3. Für Studenten mit eigenem Hausstand gilt regelmäßig ein pauschaler Gesamtbedarf (Betrag verifizieren); eigene Einkünfte und BAföG sind zu berücksichtigen.

#### 2.6 Mehr- und Sonderbedarf

Mehrbedarf (regelmäßig, etwa Kindergarten, Hort, krankheits- oder behinderungsbedingte Dauerkosten) und Sonderbedarf (einmalig, unvorhersehbar) werden zusätzlich nach dem Verhältnis der Einkommen beider Eltern getragen; rechne den Quotenanteil aus. Vom jeweiligen Einkommen ist vor der Quotenbildung der angemessene Selbstbehalt abzuziehen.

#### 2.7 Bedarfskontrollbetrag

Zu jeder Einkommensgruppe gehört ein Bedarfskontrollbetrag, der eine ausgewogene Verteilung zwischen der unterhaltspflichtigen Person und den Berechtigten sichern soll. Unterschreitet das nach Abzug aller Zahlbeträge verbleibende Einkommen den Bedarfskontrollbetrag der gewählten Gruppe, ist in die nächstniedrigere Gruppe herabzustufen, bis er gewahrt ist. Halte die Herabstufung ausdrücklich fest (Betrag und Gruppe zu verifizieren).

#### 2.8 Wechselmodell

Beim echten Wechselmodell (annähernd hälftige Betreuung) schulden beide Eltern Barunterhalt. Vorgehen:

1. Bilde den Gesamtbedarf des Kindes nach dem zusammengerechneten Einkommen beider Eltern und erhöhe ihn um die wechselmodellbedingten Mehrkosten (zwei Haushalte, Fahrtkosten); berücksichtige das volle Kindergeld bedarfsdeckend.

2. Verteile den Bedarf auf beide Eltern im Verhältnis ihrer den jeweiligen angemessenen Selbstbehalt übersteigenden Einkommen.

3. Verrechne die Anteile; der Mehrverdienende zahlt den Differenzbetrag, häufig an einen Betreuungswechsel- oder Kinderkonto. Rechne die Verrechnung offen vor.

#### 2.9 Sehr hohe Einkommen oberhalb der Tabelle

Liegt das Einkommen oberhalb der höchsten Einkommensgruppe (nach dem Stand 2026 die fünfzehnte Gruppe), wird der Bedarf nicht automatisch fortgeschrieben. Bis zum Doppelten des höchsten Tabellensatzes ist eine Fortschreibung vertretbar; darüber hinaus ist der Bedarf konkret darzulegen, weil mit steigendem Einkommen ein zunehmender Anteil der Vermögensbildung dient. Verlange in diesem Fall eine konkrete Bedarfsdarstellung statt einer bloßen Quote.

### Phase 3 — Trennungsunterhalt (Paragraf 1361 BGB)

#### 3.1 Bedarf nach den ehelichen Lebensverhältnissen

Der Bedarf bemisst sich nach den ehelichen Lebensverhältnissen im Trennungszeitpunkt. Maßgeblich ist das beiderseitige bereinigte Nettoeinkommen.

#### 3.2 Quoten- oder Differenzmethode

1. Ermittle vorab den Kindesunterhalt; er wird vom Einkommen der pflichtigen Person abgezogen (Vorwegabzug), bevor der Ehegattenbedarf berechnet wird.

2. Sind beide erwerbstätig, beträgt der Anspruch regelmäßig die Hälfte der Differenz der bereinigten Einkommen, vermindert um den Erwerbstätigenbonus (verbreitet 1/10, in einigen Oberlandesgerichtsbezirken 1/7; den im Zuständigkeitsbereich geltenden Bonus verifizieren). Ist nur eine Seite erwerbstätig, wird der Bonus nur einmal angesetzt.

3. Rechne die Methode offen vor und benenne sie. Vermeide es, eine grobe Schnellformel ohne Bonus und Vorwegabzug als Endergebnis stehenzulassen; weise stattdessen einen realistischen Korridor aus.

#### 3.3 Erwerbsobliegenheit und Vorsorgeunterhalt

1. Im Trennungsjahr besteht regelmäßig noch keine gesteigerte Erwerbsobliegenheit; das ändert sich mit fortschreitender Trennungsdauer und nach Betreuungslage.

2. Auf Verlangen kann zusätzlich Vorsorgeunterhalt (Kranken- und Altersvorsorge) geltend gemacht werden; weise ihn gesondert aus.

### Phase 4 — Nachehelicher Unterhalt

#### 4.1 Grundsatz der Eigenverantwortung

Nach der Scheidung gilt der Grundsatz der Eigenverantwortung (Paragraf 1569 BGB). Ein Anspruch besteht nur, wenn ein Unterhaltstatbestand erfüllt ist. Prüfe die Tatbestände einzeln und in dieser Reihenfolge.

#### 4.2 Unterhaltstatbestände

1. Betreuungsunterhalt (Paragraf 1570 BGB): Basisunterhalt bis zur Vollendung des dritten Lebensjahres des Kindes, Verlängerung aus kind- und elternbezogenen Billigkeitsgründen.

2. Unterhalt wegen Alters (Paragraf 1571 BGB): wenn eine Erwerbstätigkeit im Zeitpunkt von Scheidung, Betreuungsende oder Wegfall anderer Gründe altersbedingt nicht mehr erwartet werden kann.

3. Unterhalt wegen Krankheit oder Gebrechen (Paragraf 1572 BGB) zu denselben Einsatzzeitpunkten.

4. Unterhalt wegen Erwerbslosigkeit und Aufstockungsunterhalt (Paragraf 1573 BGB): wenn trotz Bemühens keine angemessene Erwerbstätigkeit gefunden wird beziehungsweise das eigene Einkommen den vollen Bedarf nicht deckt.

5. Ausbildungs-, Fortbildungs- und Umschulungsunterhalt (Paragraf 1575 BGB).

6. Billigkeitsunterhalt (Paragraf 1576 BGB) als eng auszulegender Auffangtatbestand.

#### 4.3 Bedarf, Bedürftigkeit, Leistungsfähigkeit

1. Bedarf: nach den ehelichen Lebensverhältnissen, berechnet nach denselben Grundsätzen wie beim Trennungsunterhalt (Quoten- oder Differenzmethode mit Vorwegabzug des Kindesunterhalts).

2. Bedürftigkeit: eigene Einkünfte und zumutbar erzielbares (gegebenenfalls fiktives) Einkommen mindern den Anspruch.

3. Leistungsfähigkeit: dem Pflichtigen verbleibt der angemessene Selbstbehalt gegenüber dem geschiedenen Ehegatten (Betrag verifizieren).

#### 4.4 Befristung und Herabsetzung (Paragraf 1578b BGB)

1. Der Anspruch ist zu befristen oder der Höhe nach herabzusetzen, soweit ein zeitlich unbegrenzter Unterhalt nach den ehelichen Lebensverhältnissen unbillig wäre.

2. Entscheidend sind ehebedingte Nachteile (insbesondere Erwerbsnachteile durch Kinderbetreuung oder Haushaltsführung). Bestehen keine fortwirkenden ehebedingten Nachteile, ist eine Befristung naheliegend; bestehen sie, ist der Ausgleich dieser Nachteile maßgeblich. Arbeite die ehebedingten Nachteile konkret heraus.

#### 4.5 Verwirkung (Paragraf 1579 BGB)

Prüfe Verwirkungsgründe (kurze Ehedauer, verfestigte neue Lebensgemeinschaft, schwerwiegendes Fehlverhalten) und ihre Rechtsfolge (Versagung, Herabsetzung oder zeitliche Begrenzung).

#### 4.6 Halbteilung, Drei-Stufen-Prüfung und Realsplitting

1. Prüfe jeden Ehegattenunterhalt in drei Stufen: Bedarf (nach den ehelichen Lebensverhältnissen), Bedürftigkeit (eigenes und zumutbar erzielbares Einkommen) und Leistungsfähigkeit (Wahrung des Selbstbehalts).

2. Der Halbteilungsgrundsatz begrenzt den Anspruch: Dem Pflichtigen muss nach Abzug des Unterhalts nicht weniger verbleiben als dem Berechtigten einschließlich des Unterhalts. Weise die Halbteilung als Kontrollrechnung aus.

3. Unterscheide Anrechnungs- und Differenzmethode: prägende eigene Einkünfte der berechtigten Person fließen über die Differenzmethode in die Bedarfsbemessung ein; nicht prägende oder überobligatorische Einkünfte werden nach der Anrechnungsmethode behandelt. Benenne, welche Methode du anwendest und warum.

4. Steuerliche Optimierung: Beim Trennungs- und nachehelichen Ehegattenunterhalt kommt das begrenzte Realsplitting (Paragraf 10 Abs. 1a EStG) in Betracht. Die zahlende Person setzt den Unterhalt als Sonderausgabe ab, die empfangende versteuert ihn; der steuerliche Vorteil erhöht das unterhaltsrelevante Einkommen und der entstehende Nachteil der berechtigten Person ist auszugleichen. Weise den Effekt aus, ohne ihn als feststehende Steuerberatung darzustellen.

### Phase 5 — Rang, Mangel und Selbstbehalte

1. Stelle bei mehreren Berechtigten die Rangfolge nach Paragraf 1609 BGB klar und ordne jeden Anspruch ein.

2. Liste die einschlägigen Selbstbehaltssätze (notwendiger Selbstbehalt erwerbstätig und nicht erwerbstätig, angemessener Selbstbehalt, Ehegattenselbstbehalt, Bedarfskontrollbetrag) mit dem ausdrücklichen Hinweis auf, dass die Beträge zum Stichtag zu verifizieren sind.

3. Bei nicht ausreichender Masse: Mangelfallberechnung mit offen ausgewiesener Verteilungsquote.

### Phase 6 — Durchsetzung und Verfahren

1. Auskunft: Anspruch auf Auskunft und Belege über das Einkommen (Paragraf 1605 BGB), bei Selbständigen über mehrere Jahre.

2. Stufenklage (Paragraf 254 ZPO): Auskunft, gegebenenfalls Versicherung an Eides statt, dann bezifferte Leistung.

3. Verzug und Rückstand: Unterhalt für die Vergangenheit nur ab Verzug, Auskunftsaufforderung oder Rechtshängigkeit (Paragraf 1613 BGB).

4. Titulierung und Abänderung: Jugendamtsurkunde, gerichtlicher Vergleich, Beschluss; Abänderung bei wesentlicher Änderung der Verhältnisse (Paragraf 238 FamFG; vereinfachtes Verfahren für den Kindesunterhalt Paragraf 249 FamFG).

5. Dynamisierung des Kindesunterhalts als Prozentsatz des Mindestunterhalts (Paragraf 1612a BGB).

### Phase 7 — Plausibilitäts- und Selbstkontrolle

Bevor du das Ergebnis ausgibst, prüfe es gegen sich selbst:

1. Selbstbehalt gewahrt? Der pflichtigen Person verbleibt mindestens der einschlägige Selbstbehalt (notwendig oder angemessen, je nach Rang).

2. Rangfolge beachtet? Kindesunterhalt vor Ehegattenunterhalt; Paragraf 1609 BGB korrekt angewandt.

3. Vorwegabzug erfolgt? Der Kindesunterhalt wurde vor der Ehegattenbedarfsberechnung abgezogen.

4. Halbteilung eingehalten? Dem Pflichtigen verbleibt nach Unterhalt nicht weniger als der berechtigten Person mit Unterhalt.

5. Bedarfskontrollbetrag gewahrt oder Herabstufung dokumentiert?

6. Summenprobe: Alle Zahlbeträge zusammen überschreiten nicht die verteilbare Masse; bei Mangelfall ist die Quote sauber gerechnet.

7. Stichtag und Verzug konsistent; Werte (Tabelle, Selbstbehalt, Kindergeld) als verifizierungsbedürftig markiert.

## Ausgabeformat

Liefere das Ergebnis vollständig ausformuliert, nicht als Stichwort-Skelett. Struktur:

1. Kurzhinweis und Disclaimer (zwei bis drei Sätze).

2. Sachverhalts- und Datenbasis mit klar markierten Annahmen und offenen Punkten.

3. Einkommenstableau je Seite (bereinigtes Nettoeinkommen, jede Position nachvollziehbar).

4. Berechnung je Unterhaltsart mit offenem Rechenweg und Zwischenergebnissen.

5. Ergebnis: konkrete Zahlbeträge je Berechtigtem und Monat, bei Unsicherheit ein begründeter Korridor.

6. Rang- und Mangelfallbetrachtung, soweit einschlägig.

7. Durchsetzung und nächste Schritte (Auskunft, Verzug, Titulierung, Fristen).

8. Offene Punkte und ausdrücklich zu verifizierende Werte (Tabellenstand, Selbstbehalte, Kindergeld, Rechtsprechung).

9. Quellenverzeichnis nach `references/zitierweise.md`.

Die Gliederung folgt ausschließlich dem Dezimalschema (1, 1.1, 1.1.1); zwischen Gliederungsüberschrift und folgendem Inhalt steht stets eine Leerzeile.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiele

### Beispiel 1 — Kindesunterhalt im Residenzmodell

Eingabe: ein barpflichtiger Elternteil mit bereinigtem Nettoeinkommen, zwei Kinder (7 und 13 Jahre) im Haushalt des anderen Elternteils. Erwartetes Vorgehen: Einkommensgruppe bestimmen, Tabellenbeträge je Altersstufe entnehmen, hälftiges Kindergeld abziehen, Selbstbehalt prüfen, bei Unterdeckung Mangelfallquote rechnen, Zahlbeträge ausweisen.

### Beispiel 2 — Trennungsunterhalt bei beiderseitiger Erwerbstätigkeit

Eingabe: beide Ehegatten erwerbstätig mit unterschiedlichem Einkommen, ein Kind. Erwartetes Vorgehen: Kindesunterhalt vorab abziehen, Differenz der bereinigten Einkommen bilden, Erwerbstätigenbonus des zuständigen Oberlandesgerichtsbezirks ansetzen, hälftige Differenz berechnen, Vorsorgeunterhalt auf Verlangen gesondert ausweisen, Korridor angeben.

### Beispiel 3 — Nachehelicher Unterhalt mit Befristungsfrage

Eingabe: langjährige Ehe, ein Ehegatte hat zur Kinderbetreuung beruflich zurückgesteckt. Erwartetes Vorgehen: einschlägigen Tatbestand bestimmen (Betreuungs-, danach Aufstockungsunterhalt), Bedarf nach ehelichen Lebensverhältnissen, ehebedingte Nachteile herausarbeiten und an Paragraf 1578b BGB für Befristung oder Herabsetzung spiegeln, Verwirkung prüfen.

### Beispiel 4 — Vollständig durchgerechnet (Arbeitswerte, zu verifizieren)

Die folgenden Eurobeträge sind reine **Arbeitswerte** zur Demonstration des Rechenwegs; die tatsächlichen Tabellen-, Kindergeld- und Selbstbehaltswerte des Stichtags sind vor jeder Verwendung an amtlicher Quelle einzusetzen.

Eingabe: M ist barpflichtig (Nettoeinkommen 3.500 EUR), F betreut die beiden Kinder K1 (9 Jahre) und K2 (5 Jahre) und verdient netto 1.500 EUR. Beide sind erwerbstätig, Trennungsjahr läuft.

1. Bereinigtes Nettoeinkommen M: 3.500 − berufsbedingte Aufwendungen 5 Prozent (175) = **3.325 EUR** (Arbeitswert). F: 1.500 − 75 = **1.425 EUR**.

2. Kindesunterhalt (Einordnung des bereinigten Einkommens von M in die zutreffende Einkommensgruppe; Arbeitswerte für Tabellenbetrag und hälftiges Kindergeld):

   - K1 (Altersstufe 6 bis 11): Tabellenbetrag 530 − hälftiges Kindergeld 128 = Zahlbetrag **402 EUR**.

   - K2 (Altersstufe 0 bis 5): Tabellenbetrag 450 − 128 = Zahlbetrag **322 EUR**.

   - Summe Kindesunterhalt: **724 EUR**. Selbstbehalt (notwendig, Arbeitswert 1.450 EUR) bleibt gewahrt: 3.325 − 724 = 2.601 EUR.

3. Trennungsunterhalt: Kindesunterhalt vorab von M abziehen → 3.325 − 724 = 2.601 EUR. Bereinigtes Einkommen F: 1.425 EUR. Differenz: 2.601 − 1.425 = 1.176 EUR. Erwerbstätigenbonus 1/10 auf die Differenz (Arbeitswert; je nach Oberlandesgerichtsbezirk 1/7): hälftige Differenz abzüglich Bonus → 1.176 × 0,5 = 588; abzüglich Bonus rund 59 = **rund 529 EUR** Trennungsunterhalt (Arbeitswert).

4. Plausibilität: Bei M verbleiben 2.601 − 529 = 2.072 EUR; bei F 1.425 + 529 = 1.954 EUR zuzüglich Betreuungsleistung — Halbteilung ist im Rahmen, Selbstbehalt gewahrt.

5. Ergebnis: Kindesunterhalt 402 EUR (K1) und 322 EUR (K2), Trennungsunterhalt rund 529 EUR; sämtliche Tabellen-, Kindergeld- und Bonuswerte vor Verwendung verifizieren.

## Häufige Fehler

1. Tabellenwerte, Selbstbehalt oder Kindergeld aus dem Gedächtnis oder einem veralteten Stand übernehmen, statt sie zu verifizieren.

2. Den Kindesunterhalt beim Ehegattenunterhalt nicht vorweg abziehen.

3. Den Erwerbstätigenbonus vergessen oder den falschen Bruchteil des Oberlandesgerichtsbezirks ansetzen.

4. Bei Selbständigen die Privatentnahmen mit dem Gewinn verwechseln oder steuerliche Abschreibungen ungeprüft übernehmen.

5. Volles statt hälftiges Kindergeld beim minderjährigen Kind anrechnen (oder umgekehrt beim volljährigen).

6. Den Bedarfskontrollbetrag und die Halbteilung nicht prüfen; den Mangelfall ohne offene Quote verteilen.

7. Beim nachehelichen Unterhalt die Befristung nach Paragraf 1578b BGB und die ehebedingten Nachteile übergehen.

## Unterhalts-Schärfung: Rechenweg, Auskunft, Abänderung

1. Anspruchsart festlegen.
   - Kindesunterhalt, Trennungsunterhalt, nachehelicher Unterhalt, Mehrbedarf, Sonderbedarf, Elternunterhalt oder Anpassung im Versorgungsausgleich dürfen nicht vermischt werden.
2. Auskunftsstufe vorbereiten.
   - Vor jeder Berechnung werden Auskunft, Belege und eidesstattliche Versicherung geprüft. Pflichtanker sind Paragraf 1605 BGB, Paragraf 1580 BGB, Paragraf 235 FamFG und bei Stufenklage Paragraf 113 FamFG in Verbindung mit Paragraf 254 ZPO.
3. Einkommen bereinigen.
   - Bei Arbeitnehmern: Brutto, Netto, Steuer, Sozialabgaben, berufsbedingte Aufwendungen, Altersvorsorge, Schulden und Wohnvorteil. Bei Selbstständigen: regelmäßig Drei-Jahres-Bild, Steuerbescheide, Gewinnermittlungen, BWA, Privatentnahmen, Darlehen, Investitionen und Liquidität plausibilisieren.
4. Bedarf und Leistungsfähigkeit rechnen.
   - Düsseldorfer Tabelle stets live nachziehen; Selbstbehalt, Rang, Kindergeldanrechnung, Erwerbstätigenbonus, Mangelfall und Verteilungsmasse offenlegen.
5. Antrag oder Schreiben ausformulieren.
   - Ergebnis ist eine Stufenklage, ein Auskunftsverlangen, ein Zahlungsantrag, ein Abänderungsantrag oder ein Vergleichsvorschlag mit konkretem Rechenweg.

## Unterhalts-Anker

- BGH, Beschluss vom 16.09.2020 - XII ZB 499/19: Auskunft kann nicht pauschal mit behaupteter unbegrenzter Leistungsfähigkeit verweigert werden.
- BGH, Beschluss vom 15.04.2026 - XII ZB 415/25: Erweiterter Umgang begründet keine anteilige Barunterhaltspflicht des hauptbetreuenden Elternteils. Möglich sind eine Herabstufung in der Düsseldorfer Tabelle und bei bedarfsdeckenden Leistungen ein geschätzter Abzug von regelmäßig 10 Prozent, ausnahmsweise höchstens 15 Prozent; Vertretung und Verfahrensstandschaft nach Paragraf 1629 Abs. 2 und 3 BGB sind gesondert zu prüfen.
- BGH, Beschluss vom 25.09.2019 - XII ZB 25/19: Beim Ehegattenunterhalt trägt die Quotenmethode bei hohem Einkommen nur innerhalb der anerkannten Verbrauchsvermutung; darüber hinaus ist die konkrete Verwendung für den Lebensbedarf darzulegen und im Bestreitensfall zu beweisen.
- Paragrafen 1601, 1602, 1603, 1605, 1610, 1612a, 1612b, 1361, 1569, 1570 bis 1578b, 1580 BGB und Paragrafen 235, 243 FamFG bilden den Kernbestand.

## Unterhalts-Stop

Wenn aktuelle Tabelle, vollständige Belege, Steuerlast, Wohnvorteil, Selbstständigenunterlagen oder Betreuungsmodell fehlen, wird nicht gerechnet, sondern ein Auskunfts- und Belegplan erstellt. Jede Zahl braucht eine Aktenfundstelle oder den Hinweis, dass sie nur Platzhalter bis zur Belegprüfung ist.
