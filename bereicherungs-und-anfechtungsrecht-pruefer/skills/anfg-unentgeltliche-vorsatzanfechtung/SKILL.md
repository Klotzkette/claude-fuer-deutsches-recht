---
name: anfg-unentgeltliche-vorsatzanfechtung
description: "Anfg Unentgeltliche Vorsatzanfechtung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anfg Unentgeltliche Vorsatzanfechtung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Anfg Unentgeltliche Vorsatzanfechtung** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anfg-unentgeltliche-leistung-4` | Anfechtung unentgeltlicher Leistungen außerhalb der Insolvenz prüfen: Schenkungsanfechtung in den letzten vier Jahren nach § 4 AnfG. Normen: § 4 AnfG. Prüfraster: Unentgeltlichkeitsbegriff, gemischte Schenkungen, Ausnahmen für Anstandsschenkungen, kein Verschuldenserfordernis. Output: Prüfergebnis Anfechtbarkeit mit Anfechtungszeitraum. Abgrenzung: nicht § 134 InsO (erfordert Insolvenzeröffnung). |
| `anfg-vorsatzanfechtung-3-i` | Vorsatzanfechtung außerhalb der Insolvenz geltend machen: Benachteiligungsvorsatz und Kenntnis des Anfechtungsgegners nach § 3 Abs. 1 AnfG. Normen: § 3 Abs. 1 AnfG. Prüfraster: Benachteiligungsvorsatz-Indizien, Kenntnis des Gegners, Zehn-Jahres-Frist, Beweisführung. Output: Prüfergebnis Anfechtbarkeit und Klageschriftstruktur. Abgrenzung: nicht § 133 InsO (nur bei eroffnetem Insolvenzverfahren). |
| `anspruchsziel-und-rueckabwicklungsarchitektur` | Dieses Fachmodul greift, wenn das praktische Rückabwicklungsziel in eine belastbare Anspruchsarchitektur übersetzt werden muss. Normen: §§ 812 und 818 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Anspruchsarchitektur mit Ziel, Norm und Tatsachenbedarf. Abgrenzung: nicht inhaltliche Anspruchsprüfung (siehe Fachmodule). |
| `anweisungsfall-deckungs-und-valutaverhaeltnis` | Dieses Fachmodul greift, wenn ein Zahlungs- oder Leistungsdreieck mit Deckungs- und Valutaverhältnis vorliegt. Normen: § 670 BGB und §§ 812 ff. BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Dreiecksdiagramm mit Fehlerort und korrektem Rückabwicklungsweg. Abgrenzung: nicht echte Drittleistung § 267 BGB ohne Anweisung. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Anfg Unentgeltliche Vorsatzanfechtung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anfg-unentgeltliche-leistung-4`

**Fokus:** Anfechtung unentgeltlicher Leistungen außerhalb der Insolvenz prüfen: Schenkungsanfechtung in den letzten vier Jahren nach § 4 AnfG. Normen: § 4 AnfG. Prüfraster: Unentgeltlichkeitsbegriff, gemischte Schenkungen, Ausnahmen für Anstandsschenkungen, kein Verschuldenserfordernis. Output: Prüfergebnis Anfechtbarkeit mit Anfechtungszeitraum. Abgrenzung: nicht § 134 InsO (erfordert Insolvenzeröffnung).

# Unentgeltliche Leistung — § 4 AnfG

## Triage — kläre vor Prüfung § 4 AnfG

1. Erhielt der Schuldner eine gleichwertige Gegenleistung? (Verneinung → unentgeltlich)
2. Liegt eine gemischte Schenkung vor? (dann nur teilweise Anfechtung)
3. Wann erfolgte die Leistung — innerhalb der Vier-Jahres-Frist?
4. Handelt es sich um eine Erfüllung einer sittlichen Pflicht (§ 4 Abs. 2 AnfG — enge Ausnahme)?

## Zentrale Normen

- § 4 Abs. 1 AnfG — Anfechtung unentgeltlicher Leistungen (Frist 4 Jahre; kein Verschuldenserfordernis)
- § 4 Abs. 2 AnfG — Ausnahme: Erfüllung sittlicher Pflicht oder anständiger Rücksicht
- §§ 516 ff. BGB — Schenkung (Vergleichsbegriff; AnfG-Unentgeltlichkeit ist weiter)
- §§ 195 199 BGB — Verjährung des Anfechtungsanspruchs

## Rechtsprechung (BGH — Leitsätze § 4 AnfG / unentgeltliche Leistung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Obersatz

Anfechtbar sind unentgeltliche Leistungen des Schuldners, es sei denn, sie sind früher als vier Jahre vor der Anfechtungserklärung vorgenommen worden (§ 4 Abs. 1 AnfG).

## Tatbestandsmerkmale

### 1. Leistung des Schuldners

Jede Zuwendung, die das Vermögen des Schuldners vermindert.

### 2. Unentgeltlichkeit

**Definition:** Der Schuldner hat keine oder keine angemessene Gegenleistung erhalten. Maßgeblich ist der objektive Wert der Gegenleistung im Verhältnis zur Leistung des Schuldners.

**Gemischte Schenkung:** Liegt teilweise Entgeltlichkeit vor, ist die Anfechtung auf den unentgeltlichen Teil beschränkt.

**Nicht unentgeltlich:**
- Schenkung unter einer Auflage (soweit Auflage wirtschaftlich gleichwertig).
- Leistung in Erfüllung einer sittlichen Pflicht (enge Ausnahme nach § 4 Abs. 2 AnfG).

### 3. Anfechtungsfrist: Vier Jahre

Die Leistung muss innerhalb von vier Jahren vor der Anfechtungserklärung vorgenommen worden sein.

## Ausnahmen — § 4 Abs. 2 AnfG

Nicht anfechtbar: Schenkungen, die in der Erfüllung einer sittlichen Pflicht oder einer auf den Anstand zu nehmenden Rücksicht bestehen (z. B. übliche Gelegenheitsgeschenke). Diese Ausnahme ist eng auszulegen.

## Verhältnis zu § 3 AnfG

§ 4 AnfG erfordert kein Verschulden und keinen Benachteiligungsvorsatz. Er ist insofern leichter zu beweisen. Der Nachteil ist die kürzere Frist (vier statt zehn Jahre).

## Praktische Bedeutung

Typische Anwendungsfälle:
- Grundstücksübertragung an Ehepartner ohne Gegenleistung.
- Schenkung an Kinder kurz vor der Insolvenz.
- Verzicht auf eine Forderung ohne Gegenleistung.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 2. `anfg-vorsatzanfechtung-3-i`

**Fokus:** Vorsatzanfechtung außerhalb der Insolvenz geltend machen: Benachteiligungsvorsatz und Kenntnis des Anfechtungsgegners nach § 3 Abs. 1 AnfG. Normen: § 3 Abs. 1 AnfG. Prüfraster: Benachteiligungsvorsatz-Indizien, Kenntnis des Gegners, Zehn-Jahres-Frist, Beweisführung. Output: Prüfergebnis Anfechtbarkeit und Klageschriftstruktur. Abgrenzung: nicht § 133 InsO (nur bei eroffnetem Insolvenzverfahren).

# Vorsatzanfechtung — § 3 Abs. 1 AnfG

## Triage — kläre vor Prüfung § 3 AnfG

1. Hatte der Schuldner Benachteiligungsvorsatz (zumindest dolus eventualis)?
2. Kannte der Anfechtungsgegner den Benachteiligungsvorsatz zum Zeitpunkt der Handlung?
3. Ist der Anfechtungsgegner eine nahestehende Person i.S.d. § 138 InsO (analog)? (Vermutungsregel!)
4. Lag die Rechtshandlung innerhalb der Zehn-Jahres-Frist des § 3 AnfG?

## Zentrale Normen

- § 3 Abs. 1 AnfG — Vorsatzanfechtung (Benachteiligungsvorsatz + Kenntnis des Anfechtungsgegners + 10 Jahre)
- § 138 InsO — Nahestehende Personen (analog für Kenntnisvermutung im AnfG)
- § 2 AnfG — Anfechtungsberechtigung als Grundvoraussetzung
- §§ 195 199 BGB — Verjährung des Anfechtungsanspruchs

## Rechtsprechung (BGH — Leitsätze § 3 AnfG Vorsatzanfechtung)

- Die zur Insolvenzanfechtung nach § 133 InsO ergangene Neuausrichtung des BGH gilt grundsaetzlich uebertragbar auch fuer § 3 Abs. 1 AnfG, weil beide Vorschriften denselben Wortlaut zur Vorsatzanfechtung tragen. Leitlinie: BGH, Urt. v. 06.05.2021 – Az. IX ZR 72/20 (Insolvenz; uebertragbar). Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=06.05.2021&Aktenzeichen=IX+ZR+72/20
- Weiterentwicklung: BGH, Urt. v. 18.04.2024 – Az. IX ZR 129/22 — Verwalter muss Deckungsluecke darlegen; einfaches Bestreiten kann genuegen; insoweit ebenfalls auf § 3 AnfG uebertragbar, weil der Anfechtende dort dieselben Darlegungslasten traegt. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129%2F22
- Aktenzeichen und Uebertragbarkeit auf den konkreten Mandatssachverhalt vor Schriftsatzverwendung pruefen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Obersatz

Anfechtbar sind Rechtshandlungen des Schuldners, die er mit dem Vorsatz vorgenommen hat, seine Gläubiger zu benachteiligen, wenn der Anfechtungsgegner zur Zeit der Handlung den Vorsatz des Schuldners kannte (§ 3 Abs. 1 AnfG).

## Tatbestandsmerkmale

### 1. Rechtshandlung des Schuldners

Jedes rechtlich erhebliche Handeln oder Unterlassen des Schuldners. Auch Unterlassen der Geltendmachung von Forderungen kann Rechtshandlung sein.

### 2. Gläubigerbenachteiligungsvorsatz des Schuldners

**Definition:** Der Schuldner handelt mit dem Willen, seine Gläubiger zu benachteiligen, oder nimmt die Benachteiligung zumindest als sicher vorhergesehene Folge hin (dolus eventualis genügt nach h.M.).

**Indizien für Benachteiligungsvorsatz:**
- Kenntnis der eigenen Zahlungsunfähigkeit.
- Inkongruente Leistung (Leistung auf nicht fällige oder nicht in dieser Art geschuldete Forderung).
- Verschleuderung von Vermögenswerten unter Wert.
- Übertragung auf nahestehende Personen kurz vor Insolvenz.

### 3. Kenntnis des Anfechtungsgegners

Der Anfechtungsgegner muss zum Zeitpunkt der Handlung den Benachteiligungsvorsatz des Schuldners gekannt haben.

**Vermutungsregel:** Kenntnis der drohenden Zahlungsunfähigkeit und Kenntnis der Gläubigerbenachteiligung werden vermutet, wenn der Anfechtungsgegner nahestehende Person (§ 138 InsO analog) ist.

### 4. Anfechtungsfrist: Zehn Jahre

§ 3 Abs. 1 AnfG: Rechtshandlungen bis zehn Jahre vor der Anfechtungserklärung.

## Beweislast

- Vorsatz des Schuldners: Gläubiger (Anfechtender).
- Kenntnis des Anfechtungsgegners: Anfechtender (erleichtert durch Indizien und Vermutungen).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 3. `anspruchsziel-und-rueckabwicklungsarchitektur`

**Fokus:** Dieses Fachmodul greift, wenn das praktische Rückabwicklungsziel in eine belastbare Anspruchsarchitektur übersetzt werden muss. Normen: §§ 812 und 818 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Anspruchsarchitektur mit Ziel, Norm und Tatsachenbedarf. Abgrenzung: nicht inhaltliche Anspruchsprüfung (siehe Fachmodule).

# Anspruchsziel und Rückabwicklungsarchitektur

## Einsatzbereich

Dieses Fachmodul greift, wenn das praktische Rückabwicklungsziel in eine belastbare Anspruchsarchitektur übersetzt werden muss. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welcher Vermögensvorteil ist exakt gemeint?
2. Welcher Zweck oder welche Erwartung wurde rechtlich relevant?
3. Ist der Rechtsgrund nie entstanden, später entfallen oder nur teilweise fehlend?
4. Gibt es trotz Fehler einen Behaltensgrund?
5. Welche Tatsachen fehlen für eine belastbare Subsumtion?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor.
- Trenne innere Motivation von erkennbarer Zweckbindung.
- Prüfe Teilmängel und zeitliche Zäsuren betragsgenau.
- Kontrolliere § 814 BGB, § 815 BGB, § 817 S. 2 BGB und Spezialregime.
- Gib am Ende ein Anspruchsziel mit Beweisbedarf aus.

## Typische Fehler

- Zweck mit Motiv verwechseln.
- Rechtsgrundmangel nur behaupten.
- Behaltensgrund nicht gesondert prüfen.

## Anspruchsgrundlagenarchitektur — Reihenfolge

1. **Vertraglicher Anspruch:**
 - § 433 BGB Kaufpreis, § 535 BGB Mietzins, § 611 BGB Vergütung.
 - § 346 BGB Rückgewähr nach Rücktritt.
 - § 357 BGB Rückgewähr nach Widerruf.
2. **c.i.c. — § 280 Abs. 1 i.V.m. § 311 Abs. 2 BGB:** vorvertragliche Pflichtverletzung.
3. **GoA §§ 677, 683 BGB:** Aufwendungsersatz aus berechtigter Geschäftsführung ohne Auftrag.
4. **Dingliche Ansprüche:**
 - § 985 BGB Herausgabe (Eigentümer-Besitzer-Verhältnis).
 - §§ 987 ff. BGB Folgeansprüche (Nutzungen, Schadensersatz, Verwendungen).
5. **Delikt:**
 - § 823 Abs. 1 BGB Schadensersatz aus Verletzung absoluter Rechtsgüter.
 - § 823 Abs. 2 BGB i.V.m. Schutzgesetz.
 - § 826 BGB sittenwidrige vorsätzliche Schädigung.
 - § 831 BGB Verrichtungsgehilfe.
6. **Bereicherungsrecht §§ 812 ff. BGB:**
 - § 812 Abs. 1 S. 1 Alt. 1 BGB Leistungskondiktion (Leistung ohne Rechtsgrund).
 - § 812 Abs. 1 S. 1 Alt. 2 BGB Nichtleistungskondiktion (Eingriffskondiktion).
 - § 812 Abs. 1 S. 2 Alt. 1 BGB condictio ob causam finitam (Wegfall des Rechtsgrunds).
 - § 812 Abs. 1 S. 2 Alt. 2 BGB condictio ob rem (Zweckverfehlung).
 - § 813 BGB condictio indebiti bei Erfüllung einredebehafteter Forderung.
 - § 816 Abs. 1, 2 BGB Verfügung eines Nichtberechtigten / Empfang an Nichtberechtigten.
 - § 822 BGB Bereicherung eines Dritten.

## Rückabwicklungs-Architektur — Reihenfolge der Prüfung

- Bei nichtigem gegenseitigen Vertrag: **Saldotheorie** vs. Zweikondiktionentheorie (Ausnahmen siehe `saldotheorie-rueckabwicklung-nichtiger-vertraege`).
- Bei wirksamer Anfechtung § 142 BGB: ex tunc-Nichtigkeit → Bereicherungsrecht.
- Bei Rücktritt §§ 346 ff. BGB: vorrangiges Spezialregime — keine Leistungskondiktion.
- Bei Insolvenz: zusätzlich Anfechtungsanspruch §§ 129 ff. InsO / AnfG prüfen.

## Anti-Halluzinations-Hinweise

- Reihenfolge der Anspruchsprüfung: Vertrag — c.i.c. — GoA — dinglich — Delikt — Bereicherung. (CLAUDE.md-Vorgabe).
- Keine Vermengung von Anfechtung im BGB-Sinne (§§ 119 ff. BGB) und Insolvenzanfechtung (§§ 129 ff. InsO) oder AnfG-Anfechtung.

## Arbeitsausgabe

| Punkt | Ergebnis | Belegbedarf |
|---|---|---|
| Anspruchsziel | [...] | [...] |
| beteiligte Personen | [...] | [...] |
| Vermögensvorteil | [...] | [...] |
| Zweck/Zurechnung | [...] | [...] |
| Rechtsgrund/Behaltensgrund | [...] | [...] |
| § 818 BGB | [...] | [...] |
| Einreden/Spezialregime | [...] | [...] |
| vorläufiges Ergebnis | [...] | [...] |

## Mini-Check vor Output

- Kein Direktanspruch ohne begründete Zurechnung.
- Kein Wertersatz ohne Bewertungsmethode.
- Keine Entreicherung ohne konkreten Vermögensweg.
- Keine Saldierung ohne beiderseitige Leistungstabelle.
- Offene Tatsachen bleiben als offen markiert.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `anweisungsfall-deckungs-und-valutaverhaeltnis`

**Fokus:** Dieses Fachmodul greift, wenn ein Zahlungs- oder Leistungsdreieck mit Deckungs- und Valutaverhältnis vorliegt. Normen: § 670 BGB und §§ 812 ff. BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Dreiecksdiagramm mit Fehlerort und korrektem Rückabwicklungsweg. Abgrenzung: nicht echte Drittleistung § 267 BGB ohne Anweisung.

# Anweisungsfall: Deckungs- und Valutaverhältnis

## Einsatzbereich

Dieses Fachmodul greift, wenn ein Zahlungs- oder Leistungsdreieck mit Deckungs- und Valutaverhältnis vorliegt. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welche Personen und Beziehungen bilden das Leistungsdreieck oder die Kette?
2. Wer hat den Leistungszweck objektiv gesetzt?
3. War eine Anweisung, Vollmacht, Zession oder Drittleistung wirksam und zurechenbar?
4. Welches Verhältnis ist fehlerhaft?
5. Würde ein Direktanspruch nur ein Insolvenz- oder Vertragsrisiko verschieben?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl.
- Bestimme den Empfängerhorizont des Endempfängers.
- Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab.
- Prüfe Direktkondiktion nur mit eigenständiger Ausnahmebegründung.
- Halte Vertrauensschutz und Risikozuweisung ausdrücklich fest.

## Dreiecks-Kompass

| Ebene | Leitfrage | Ergebnis |
|---|---|---|
| Zahlungsweg | Wer hat den Vermögensvorteil tatsächlich bewegt? | technische Spur |
| Deckung | Warum sollte der Zahlende gegenüber dem Mittler handeln? | A-B-Fehler oder A-B-Rechtsgrund |
| Valuta | Warum sollte der Mittler gegenüber dem Empfänger leisten? | B-C-Fehler oder B-C-Rechtsgrund |
| Empfängerhorizont | Als wessen Leistung durfte C die Zahlung verstehen? | Zurechnung |
| Risiko | Wer trägt Bonitäts-, Insolvenz- und Fehlerquellenrisiko? | Anspruchsgegner |

Der Zahlungsweg ist nur der Anfang. Der Anspruch folgt aus Zweck- und Risikozurechnung.

## Anspruchsentscheidung

- **Wirksame, zurechenbare Anweisung:** A kondiziert bei Deckungsfehler regelmäßig gegen B; B kondiziert bei Valutafehler gegen C.
- **Keine zurechenbare Anweisung:** A kann gegen C vorgehen, weil C keinen belastbaren Leistungsgrund aus B herleiten kann.
- **Doppelmangel:** getrennt denken; ein Direktanspruch braucht zusätzlich fehlenden Empfängerschutz oder eine besondere Korrekturwertung.
- **Zahlstelle oder Bote:** die Zwischenperson ist nur dann Schuldner, wenn sie selbst behalten darf oder die Zweckbindung verletzt.
- **Drittleistung:** wenn eine fremde Schuld wirksam getilgt wird, liegt der Rückgriff eher beim begünstigten Schuldner als beim befriedigten Gläubiger.

## Typische Fehler

- Tatsächlichen Empfänger automatisch als Schuldner behandeln.
- Doppelmangel zu einem Pauschalanspruch verschmelzen.
- Insolvenzrisiko ohne Rechtsgrund verlagern.
- Innenwillen des Zahlenden über den objektiven Empfängerhorizont stellen.
- Die technische Bankspur mit der bereicherungsrechtlichen Leistungsrichtung verwechseln.

## Arbeitsausgabe

| Punkt | Ergebnis | Belegbedarf |
|---|---|---|
| Anspruchsziel | [...] | [...] |
| beteiligte Personen | [...] | [...] |
| Vermögensvorteil | [...] | [...] |
| Zweck/Zurechnung | [...] | [...] |
| Rechtsgrund/Behaltensgrund | [...] | [...] |
| § 818 BGB | [...] | [...] |
| Einreden/Spezialregime | [...] | [...] |
| vorläufiges Ergebnis | [...] | [...] |

## Zusatzoutput: Dreiecksentscheidung

| Frage | Antwort |
|---|---|
| Anweisung vorhanden und wirksam? | [...] |
| Deckungsverhältnis fehlerhaft? | [...] |
| Valutaverhältnis fehlerhaft? | [...] |
| C durfte Leistung von wem annehmen? | [...] |
| Direktkondiktion begründet? | ja / nein, weil [...] |

## Mini-Check vor Output

- Kein Direktanspruch ohne begründete Zurechnung.
- Kein Wertersatz ohne Bewertungsmethode.
- Keine Entreicherung ohne konkreten Vermögensweg.
- Keine Saldierung ohne beiderseitige Leistungstabelle.
- Offene Tatsachen bleiben als offen markiert.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
