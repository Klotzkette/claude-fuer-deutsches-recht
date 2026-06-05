---
name: condictio-causa-data-indebiti-bgb-ob-causam
description: "Condictio Causa Data Indebiti BGB OB Causam: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Condictio Causa Data Indebiti BGB OB Causam

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Condictio Causa Data Indebiti BGB OB Causam** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `condictio-causa-data-causa-non-secuta` | Dieses Fachmodul greift, wenn der erwartete Leistungserfolg endgültig nicht eingetreten ist. Normen: § 812 Abs. 1 S. 2 Alt. 2 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Prüfergebnis condictio ob rem mit Zweckverfehlung und Anspruchshöhe. Abgrenzung: nicht condictio indebiti § 812 Abs. 1 S. 1 Alt. 1 BGB. |
| `condictio-indebiti-813-bgb` | Rückforderung trotz Erfüllung einer einredebehafteten Verbindlichkeit nach § 813 BGB prüfen. Normen: § 813 BGB. Prüfraster: dauernde vs. temporäre Einreden, Verjährungseinrede, Tatbestandsmerkmale. Output: Prüfergebnis condictio indebiti mit Einredenklassifikation. Abgrenzung: nicht condictio § 812 Abs. 1 S. 1 Alt. 1 BGB bei fehlendem Rechtsgrund. |
| `condictio-ob-causam-finitam-wegfall-des-rechtsgrundes` | Dieses Fachmodul greift, wenn ein zunächst bestehender Rechtsgrund später entfallen sein kann. Normen: § 812 Abs. 1 S. 2 Alt. 1 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Prüfergebnis condictio ob causam finitam mit Wegfallzeitpunkt. Abgrenzung: nicht condictio indebiti (Rechtsgrund von Anfang an fehlend). |
| `condictio-ob-rem-zweckabrede` | Dieses Fachmodul greift, wenn eine Leistung für einen erkennbar bezweckten Erfolg erbracht wurde. Normen: § 812 Abs. 1 S. 2 Alt. 2 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Prüfergebnis condictio ob rem mit Zweckabrede und Erfolgseintritt. Abgrenzung: nicht condictio causa data (endgültiger Misserfolg). |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Condictio Causa Data Indebiti BGB OB Causam**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `condictio-causa-data-causa-non-secuta`

**Fokus:** Dieses Fachmodul greift, wenn der erwartete Leistungserfolg endgültig nicht eingetreten ist. Normen: § 812 Abs. 1 S. 2 Alt. 2 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Prüfergebnis condictio ob rem mit Zweckverfehlung und Anspruchshöhe. Abgrenzung: nicht condictio indebiti § 812 Abs. 1 S. 1 Alt. 1 BGB.

# Causa data causa non secuta

## Einsatzbereich

Dieses Fachmodul greift, wenn der erwartete Leistungserfolg endgültig nicht eingetreten ist. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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

## 2. `condictio-indebiti-813-bgb`

**Fokus:** Rückforderung trotz Erfüllung einer einredebehafteten Verbindlichkeit nach § 813 BGB prüfen. Normen: § 813 BGB. Prüfraster: dauernde vs. temporäre Einreden, Verjährungseinrede, Tatbestandsmerkmale. Output: Prüfergebnis condictio indebiti mit Einredenklassifikation. Abgrenzung: nicht condictio § 812 Abs. 1 S. 1 Alt. 1 BGB bei fehlendem Rechtsgrund.

# Condictio indebiti — § 813 BGB

## Triage — kläre vor der Prüfung

1. Hat der Leistende auf eine Verbindlichkeit gezahlt, gegen die ihm eine dauernde (nicht nur vorübergehende) Einrede zustand?
2. Welche konkrete Einrede ist einschlägig — insbesondere: war die Forderung bereits verjährt (§ 214 BGB)?
3. Kannte der Leistende die Einrede im Zeitpunkt der Leistung (Ausschluss nach § 813 Abs. 1 S. 2 BGB)?
4. Handelt es sich um eine Verbindlichkeit aus einem einseitigen Rechtsgeschäft (Ausschluss § 813 Abs. 2 BGB)?
5. Kommt § 814 BGB (Kenntnis der Nichtschuld) als vorrangige Norm in Betracht?

## Zentrale Normen

§ 813 BGB (Rückforderung bei dauernder Einrede) — § 214 BGB (Verjährungseinrede) — § 853 BGB (Einrede der Arglist) — § 812 Abs. 1 S. 1 Alt. 1 BGB (Leistungskondiktion) — § 814 BGB (Kenntnis der Nichtschuld) — § 818 BGB (Umfang der Herausgabe) — § 222 BGB a.F. (Verjährungseinrede, für Altfälle)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

§ 813 BGB ist ein Sonderfall der Leistungskondiktion. Er erlaubt die Rückforderung einer Leistung, die zur Erfüllung einer Verbindlichkeit erbracht wurde, gegen die dem Leistenden eine dauernde Einrede zustand.

## Obersatz

Wer zur Erfüllung einer Verbindlichkeit geleistet hat, gegen die ihm eine dauernde Einrede zusteht, kann das Geleistete nach § 813 Abs. 1 S. 1 BGB zurückfordern.

## Tatbestandsmerkmale

### 1. Leistung zur Erfüllung einer Verbindlichkeit

Der Leistende muss in der Vorstellung gehandelt haben, eine bestehende Schuld zu tilgen. Kein Schenkungswille.

### 2. Dauernde Einrede

**Definition:** Eine Einrede, die nicht nur vorübergehend die Durchsetzbarkeit hemmt, sondern die Verbindlichkeit auf Dauer unvollkommen macht.

**Beispiele dauernder Einreden:**
- Verjährungseinrede (§ 214 BGB) — wichtigster Anwendungsfall.
- Einrede der Arglist (§ 853 BGB) bei Ansprüchen aus unerlaubter Handlung.

**Keine dauernde Einrede:**
- Stundungsabrede (nur vorübergehend).
- Einrede des nicht fälligen Anspruchs.

### 3. Kein Ausschluss nach § 813 Abs. 1 S. 2 BGB

Hat der Leistende die Einrede im Zeitpunkt der Leistung gekannt, ist die Rückforderung ausgeschlossen.

### 4. Kein Ausschluss nach § 813 Abs. 2 BGB

§ 813 Abs. 2 BGB schließt die Rückforderung bei Leistung auf eine Verbindlichkeit aus einem einseitigen Rechtsgeschäft (z. B. Wechsel, Scheck) aus, soweit ein gutgläubiger Dritter betroffen ist.

## Besonderheit: Verjährungseinrede

Zahlt der Schuldner auf eine bereits verjährte Forderung, steht ihm die Einrede aus § 214 BGB zu. In Kenntnis der Verjährung ist Rückforderung nach § 813 Abs. 1 S. 2 BGB ausgeschlossen; ohne Kenntnis ist Rückforderung möglich.

## Prüfschema

1. Leistung zur Tilgung einer Verbindlichkeit?
2. Bestand eine dauernde Einrede?
3. Kannte der Leistende die Einrede (→ Ausschluss)?
4. Ausschluss nach § 813 Abs. 2 BGB (einseitiges Rechtsgeschäft)?

## Output-Template

**Prüfung § 813 BGB — Condictio indebiti**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Leistung zur Tilgung einer Verbindlichkeit | ja / nein |
| Art der Einrede | z. B. Verjährung (§ 214 BGB) |
| Dauernde Einrede (nicht nur vorübergehend) | ja / nein |
| Kenntnis der Einrede bei Leistung | ja → Ausschluss / nein → § 813 greift |
| § 813 Abs. 2 BGB einschlägig | ja / nein |

**Ergebnis:** Rückforderung nach § 813 Abs. 1 S. 1 BGB [möglich / ausgeschlossen].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 3. `condictio-ob-causam-finitam-wegfall-des-rechtsgrundes`

**Fokus:** Dieses Fachmodul greift, wenn ein zunächst bestehender Rechtsgrund später entfallen sein kann. Normen: § 812 Abs. 1 S. 2 Alt. 1 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Prüfergebnis condictio ob causam finitam mit Wegfallzeitpunkt. Abgrenzung: nicht condictio indebiti (Rechtsgrund von Anfang an fehlend).

# Condictio ob causam finitam: Wegfall des Rechtsgrundes

## Einsatzbereich

Dieses Fachmodul greift, wenn ein zunächst bestehender Rechtsgrund später entfallen sein kann. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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

## Condictio ob causam finitam (§ 812 Abs. 1 S. 2 Alt. 1 BGB)

- **Tatbestand:** Leistung zur Erfüllung einer bestehenden Verbindlichkeit; der Rechtsgrund **entfällt nachträglich** mit Wirkung ex nunc oder ex tunc.
- **Abgrenzung condictio indebiti § 812 Abs. 1 S. 1 Alt. 1 BGB:** Rechtsgrund fehlt von Anfang an (z. B. nichtiger Vertrag § 134, § 138 BGB).
- **Abgrenzung condictio ob rem § 812 Abs. 1 S. 2 Alt. 2 BGB:** ein gar nicht bezweckter Erfolg tritt nicht ein; condictio ob causam finitam dagegen bezieht sich auf einen bestehenden, später wegfallenden Rechtsgrund.

## Typische Wegfallsereignisse

- **§ 142 BGB Anfechtung:** ex tunc-Nichtigkeit — Rückabwicklung nach §§ 812 ff. BGB; **Hinweis:** beim Streit um Subsumtion ggf. condictio indebiti (Rechtsgrund von Anfang an fehlend, weil ex tunc) — h.M. ordnet aber unter § 812 Abs. 1 S. 2 Alt. 1 BGB ein.
- **Auflösende Bedingung § 158 Abs. 2 BGB:** mit Bedingungseintritt entfällt der Rechtsgrund ex nunc.
- **Auflösender Endtermin § 163 BGB:** Vertrag endet zum Termin, danach Rückabwicklung der nach Termin erfolgten Leistungen.
- **Wegfall der Geschäftsgrundlage § 313 BGB:** Vorrang Anpassung; bei Unmöglichkeit der Anpassung Rücktrittsrecht und Rückabwicklung nach §§ 346 ff. BGB (kein direkter Bereicherungsanspruch).
- **Erlöschen eines Erbteils** durch Anfechtung der Erbschaftsannahme § 1957 BGB.

## Saldotheorie und § 818 Abs. 3 BGB

- Bei gegenseitigem Vertrag mit Wegfall des Rechtsgrunds: Saldotheorie wie bei Rückabwicklung nichtiger Verträge.
- Entreicherungseinrede § 818 Abs. 3 BGB für gutgläubigen Empfänger; § 819 BGB Verschärfung ab Kenntnis vom Wegfallsereignis.

## Konkurrenz und Vorrang

- **Rücktritt §§ 346 ff. BGB:** Bei wirksamem Rücktritt **kein** Bereicherungsanspruch — § 346 BGB ist abschließendes Spezialregime.
- **Widerruf §§ 355, 357 BGB:** ebenfalls Spezialregime mit eigenen Rückabwicklungsregeln.
- **Anfechtung § 142 BGB:** Rechtsgrund ex tunc nichtig, dann §§ 812 ff. BGB.

## Beweis

- Anspruchsteller: Bestehen des ursprünglichen Rechtsgrunds + Wegfallsereignis mit Datum.
- Anspruchsgegner: Entreicherung, Bösgläubigkeitsausschluss.

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

## 4. `condictio-ob-rem-zweckabrede`

**Fokus:** Dieses Fachmodul greift, wenn eine Leistung für einen erkennbar bezweckten Erfolg erbracht wurde. Normen: § 812 Abs. 1 S. 2 Alt. 2 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Prüfergebnis condictio ob rem mit Zweckabrede und Erfolgseintritt. Abgrenzung: nicht condictio causa data (endgültiger Misserfolg).

# Condictio ob rem: Zweckabrede

## Einsatzbereich

Dieses Fachmodul greift, wenn eine Leistung für einen erkennbar bezweckten Erfolg erbracht wurde. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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

## Condictio ob rem — Zweckverfehlungskondiktion (§ 812 Abs. 1 S. 2 Alt. 2 BGB)

- **Tatbestand:** Leistung an den Empfänger zu einem nach dem Vertragsinhalt **nicht geschuldeten** Erfolg (kein Erfüllungsanspruch), wobei der Empfänger den Zweck **kannte oder kennen musste** und sich auf diesen Zweck **eingelassen** hat (sog. Zweckabrede oder factum). Der bezweckte Erfolg tritt nicht ein.
- **Abgrenzung Motiv vs. Zweckabrede:** Reines einseitiges Motiv des Leistenden genügt nicht — der Zweck muss zum **gemeinsamen Verständnis** geworden sein.
- **Abgrenzung condictio indebiti § 812 Abs. 1 S. 1 Alt. 1 BGB:** dort fehlt der Rechtsgrund von Anfang an; bei condictio ob rem gibt es eine Zweckabrede, deren Zweck verfehlt wurde.
- **Abgrenzung condictio ob causam finitam § 812 Abs. 1 S. 2 Alt. 1 BGB:** dort entfällt ein einmal bestandener Rechtsgrund nachträglich; bei condictio ob rem wird ein angestrebter Erfolg nicht erreicht.

## Typische Fallgruppen

- **Schwiegerelternzuwendungen** an die Schwiegerkinder zur Familienvermögensbildung — Trennung der Ehe führt zur Zweckverfehlung, Rückforderung möglich (BGH-Linie zur unbenannten Zuwendung unter Ehegatten, Az. zu verifizieren).
- **Investitionen in fremde Sache** in Erwartung einer späteren Übertragung (z. B. Hausbau auf Schwiegerelterngrundstück).
- **Vorleistungen** auf einen erwarteten künftigen Vertragsabschluss, der nicht zustande kommt.

## Konkurrenzen und Ausschlüsse

- **§ 815 BGB:** ausgeschlossen, wenn Eintritt des Erfolgs von Anfang an unmöglich war und Leistender dies wusste, oder wenn Leistender den Erfolgseintritt treuwidrig verhindert.
- **§ 814 BGB:** kein Ausschluss, da Zweckverfehlung nicht „Kenntnis der Nichtschuld" voraussetzt.
- **§ 313 BGB Geschäftsgrundlage:** Vorrang bei wirksamem Vertrag mit Geschäftsgrundlagenstörung.

## Saldierung und § 818 Abs. 3 BGB

- Bei Rückforderung von Bauleistungen / werterhöhenden Verwendungen: Wertersatz nach § 818 Abs. 2 BGB; Saldierung mit eigenen Nutzungen des Leistenden.
- Bei Entreicherung des Empfängers (z. B. Geld bereits verlebt): § 818 Abs. 3 BGB greift, sofern nicht § 819 BGB Bösgläubigkeit.

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
