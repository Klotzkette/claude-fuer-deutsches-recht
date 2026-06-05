---
name: klageantrag-zahlung-kondiktion-schwarzarbeit
description: "Klageantrag Zahlung Kondiktion Schwarzarbeit: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klageantrag Zahlung Kondiktion Schwarzarbeit

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Klageantrag Zahlung Kondiktion Schwarzarbeit** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klageantrag-zahlung-herausgabe-zug-um-zug` | Dieses Fachmodul greift, wenn aus der Prüfung ein vollstreckbarer Antrag gebaut werden muss. Normen: §§ 812 und 818 BGB; §§ 253 und 322 BGB; § 348 BGB; § 274 BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview; Halte Beweisbedarf und offene Tatsachen sichtbar; Formuliere Hilfspositionen für Wertersatz, Saldo und Zug um Zug. Output: Klageantragsentwurf mit Tenorvorschlag und Zug-um-Zug-Verknüpfung. Abgrenzung: nicht materiell-rechtliche Anspruchsprüfung. |
| `kondiktion-bei-schwarzarbeit-und-illegalitaet` | Dieses Fachmodul greift, wenn illegale Austauschverhältnisse bereicherungsrechtlich nicht normalisiert werden dürfen. Normen: §§ 134 und 817 BGB; SchwarzArbG. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Prüfergebnis Schwarzarbeitskondiktion mit § 817 S. 2 BGB Sperre. Abgrenzung: nicht regulärer Werklohnanspruch § 631 BGB. |
| `kondiktionskarte-vollstaendiger-fallaufbau` | Dieses Fachmodul greift, wenn ein komplexer Fall zuerst als Personen-, Leistungs- und Vermögenskarte erfasst werden muss. Normen: §§ 812 bis 822 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Personen-, Leistungs- und Vermögenskarte mit Anspruchsknoten. Abgrenzung: nicht punktuelle Einzelprüfung eines Anspruchs. |
| `konkurrenz-bereicherung-anfechtung-und-vindikation` | Anspruchskonkurrenzen zwischen Bereicherungsrecht §§ 812 ff. BGB, AnfG/InsO-Anfechtung und Vindikation § 985 BGB klären. Normen: §§ 812 985 BGB, §§ 129 ff. InsO, AnfG. Prüfraster: Verdrängungsregeln, Subsidiarität, Parallelität der Ansprüche. Output: Konkurrenzübersicht mit Handlungsempfehlung. Abgrenzung: nicht Einzelprüfung innerhalb eines Regelungskreises. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Klageantrag Zahlung Kondiktion Schwarzarbeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klageantrag-zahlung-herausgabe-zug-um-zug`

**Fokus:** Dieses Fachmodul greift, wenn aus der Prüfung ein vollstreckbarer Antrag gebaut werden muss. Normen: §§ 812 und 818 BGB; §§ 253 und 322 BGB; § 348 BGB; § 274 BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview; Halte Beweisbedarf und offene Tatsachen sichtbar; Formuliere Hilfspositionen für Wertersatz, Saldo und Zug um Zug. Output: Klageantragsentwurf mit Tenorvorschlag und Zug-um-Zug-Verknüpfung. Abgrenzung: nicht materiell-rechtliche Anspruchsprüfung.

# Klageantrag: Zahlung, Herausgabe, Zug um Zug

## Einsatzbereich

Dieses Fachmodul greift, wenn aus der Prüfung ein vollstreckbarer Antrag gebaut werden muss. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welches praktische Ziel soll der Output erreichen?
2. Welche Tatsachen sind beweisbar und welche offen?
3. Welche Einreden muss der Entwurf antizipieren?
4. Welche Haupt-, Hilfs- oder Zug-um-Zug-Anträge sind nötig?
5. Welche Aussage darf ohne verifizierte Grundlage nicht getroffen werden?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview.
- Halte Beweisbedarf und offene Tatsachen sichtbar.
- Formuliere Hilfspositionen für Wertersatz, Saldo und Zug um Zug.
- Vermeide ungeprüfte Fundstellen und scheinpräzise Beträge.
- Gib am Ende eine knappe Risikoeinschätzung aus.

## Typische Fehler

- Rechtliches Ergebnis ohne Tatsachenbasis ausgeben.
- Hilfsanträge und Einreden vergessen.
- Unverifizierte Zitate oder Scheinsicherheit verwenden.

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

## 2. `kondiktion-bei-schwarzarbeit-und-illegalitaet`

**Fokus:** Dieses Fachmodul greift, wenn illegale Austauschverhältnisse bereicherungsrechtlich nicht normalisiert werden dürfen. Normen: §§ 134 und 817 BGB; SchwarzArbG. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Prüfergebnis Schwarzarbeitskondiktion mit § 817 S. 2 BGB Sperre. Abgrenzung: nicht regulärer Werklohnanspruch § 631 BGB.

# Kondiktion bei Schwarzarbeit und Illegalität

## Einsatzbereich

Dieses Fachmodul greift, wenn illegale Austauschverhältnisse bereicherungsrechtlich nicht normalisiert werden dürfen. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welches Spezialregime steht neben oder vor §§ 812 ff. BGB?
2. Welche Schutzrichtung verfolgt dieses Regime?
3. Welche Leistungen und Gegenleistungen sind betroffen?
4. Würde Bereicherungsrecht die Spezialwertung unterlaufen?
5. Welche Fristen, Formfragen oder Rechtswege sind gesondert zu prüfen?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht.
- Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung.
- Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung.
- Setze § 812 BGB nur ergänzend ein, wenn kein abschließendes Regime greift.
- Markiere Rechtsweg-, Frist- und Beweisrisiken.

## Typische Fehler

- Spezialrecht durch § 812 BGB überspielen.
- Schutzvorschriften in Wertersatz umwandeln.
- Fristen oder Rechtsweg übersehen.

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

## 3. `kondiktionskarte-vollstaendiger-fallaufbau`

**Fokus:** Dieses Fachmodul greift, wenn ein komplexer Fall zuerst als Personen-, Leistungs- und Vermögenskarte erfasst werden muss. Normen: §§ 812 bis 822 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erkennbarer Zweckbindung; Prüfe Teilmängel und zeitliche Zäsuren betragsgenau. Output: Personen-, Leistungs- und Vermögenskarte mit Anspruchsknoten. Abgrenzung: nicht punktuelle Einzelprüfung eines Anspruchs.

# Kondiktionskarte: vollständiger Fallaufbau

## Einsatzbereich

Dieses Fachmodul greift, wenn ein komplexer Fall zuerst als Personen-, Leistungs- und Vermögenskarte erfasst werden muss. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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

## 4. `konkurrenz-bereicherung-anfechtung-und-vindikation`

**Fokus:** Anspruchskonkurrenzen zwischen Bereicherungsrecht §§ 812 ff. BGB, AnfG/InsO-Anfechtung und Vindikation § 985 BGB klären. Normen: §§ 812 985 BGB, §§ 129 ff. InsO, AnfG. Prüfraster: Verdrängungsregeln, Subsidiarität, Parallelität der Ansprüche. Output: Konkurrenzübersicht mit Handlungsempfehlung. Abgrenzung: nicht Einzelprüfung innerhalb eines Regelungskreises.

# Konkurrenz: Bereicherung, Anfechtung und Vindikation

## Triage — kläre vor der Prüfung

1. Besteht noch Eigentum des Anspruchstellers am streitigen Gegenstand (→ § 985 BGB vorrangig)?
2. Fehlt ein Rechtsgrund für das Behaltendürfen (→ § 812 BGB), oder liegt eine Gläubigerbenachteiligung vor (→ AnfG / §§ 129 ff. InsO)?
3. Ist ein Insolvenzverfahren eröffnet (→ §§ 129 ff. InsO) oder handelt es sich um eine außerinsolvenzliche Einzelanfechtung (→ AnfG)?
4. Haben sowohl § 812 BGB als auch ein Anfechtungsanspruch Erfolg — wie wird Doppelbefriedigung vermieden?
5. Hat der Anfechtungsgegner nach § 144 InsO eine Gegenleistung zurückerhalten, die den parallelen Bereicherungsanspruch tilgt?

## Zentrale Normen

§ 812 Abs. 1 BGB (Leistungskondiktion/Nichtleistungskondiktion) — § 985 BGB (Vindikation) — §§ 987–993 BGB (Eigentümer-Besitzer-Verhältnis) — §§ 129–147 InsO (Insolvenzanfechtung) — §§ 1–13 AnfG (Gläubigeranfechtung) — § 55 InsO (Masseverbindlichkeiten) — § 144 InsO (Rückgewähr Gegenleistung)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verhältnis § 812 BGB zu AnfG

**Grundsatz Nebeneinander:** Bereicherungsrecht und AnfG schützen unterschiedliche Interessen und können nebeneinander angewendet werden.

**Doppelbefriedigung ausgeschlossen:** Gläubiger kann nicht mehr erhalten, als er zu beanspruchen hat.

## Verhältnis § 812 BGB zu §§ 129 ff. InsO

**Mit Verfahrenseröffnung:** Insolvenzverwalter hat Zugriff auf beide Anspruchsgrundlagen.

**Priorität der Masse:** Bereicherungsansprüche der Insolvenzmasse (§ 812 BGB) sind Masseforderungen (§ 55 InsO).

**Kein doppeltes Entgelt:** Hat der Anfechtungsgegner nach § 144 InsO seine Gegenleistung zurückerhalten, erlischt der parallele Bereicherungsanspruch insoweit.

## Verhältnis § 812 BGB zu § 985 BGB (Vindikation)

**Vindikation hat Vorrang:** Solange Eigentum besteht, geht § 985 BGB vor.

**Bereicherungsrecht tritt ein, wenn:** Eigentum durch wirksame Verfügung übergegangen ist (z. B. gutgläubiger Erwerb § 932 BGB) → dann § 812 BGB oder § 816 BGB.

## Prüfreihenfolge

1. Besteht noch Eigentum? → § 985 BGB (vorrangig).
2. Kein Eigentum mehr, fehlender Rechtsgrund? → § 812 BGB.
3. Rechtsgrund vorhanden, Gläubigerbenachteiligung? → AnfG oder §§ 129 ff. InsO.

## Output-Template

**Weichenstellung: Bereicherung / Anfechtung / Vindikation**

Sachverhalt (kurz): [...]

| Anspruchsgrundlage | Tatbestand erfüllt? | Vorrang/Konkurrenz |
|---|---|---|
| § 985 BGB (Vindikation) | Eigentum noch vorhanden? ja / nein | Vorrang wenn ja |
| § 812 BGB | Kein Rechtsgrund | neben § 985 nur nach Eigentumsübergang |
| AnfG | Einzelgläubiger mit Titel, Benachteiligung | neben § 812 möglich |
| §§ 129 ff. InsO | Insolvenzverfahren + Verwalter | verdrängt AnfG nach Verfahrenseröffnung |

**Ergebnis:** Anzuwendende Anspruchsgrundlage(n): [...]. Doppelbefriedigung ausgeschlossen.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.
