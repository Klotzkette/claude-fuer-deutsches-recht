---
name: verschaerfte-haftung-abgetretene-forderung
description: "Verschaerfte Haftung Abgetretene Forderung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verschaerfte Haftung Abgetretene Forderung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Verschaerfte Haftung Abgetretene Forderung** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` | Verschärfte Bereicherungshaftung nach § 819 BGB bei Bösgläubigkeit oder Rechtshängigkeit prüfen. Normen: §§ 819 818 Abs. 4 BGB. Prüfraster: Kenntnis des Mangels, Zeitpunkt, Umfang verschärfte Haftung, Rechtshängigkeitswirkung. Output: Prüfergebnis verschärfte Haftung mit Berechnungshinweis. Abgrenzung: nicht gutgläubiger Entreicherungsschutz § 818 Abs. 3 BGB. |
| `abgetretene-forderung-und-zession` | Dieses Fachmodul greift, wenn Abtretung, Zahlung und Forderungsbestand auseinandergehalten werden müssen. Normen: §§ 398-413 BGB sowie §§ 812 und 818 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Zessionsmatrix mit Deckungs- und Valutaverhältnis, Anspruchsgegner und Belegbedarf. Abgrenzung: nicht Insolvenzanfechtung §§ 129 ff. InsO. |
| `anfechtung-142-und-rueckabwicklung` | Dieses Fachmodul greift, wenn eine wirksame Anfechtung den Rechtsgrund rückwirkend beseitigt. Normen: §§ 119 bis 124 BGB sowie §§ 142 und 812 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Anfechtungs- und Rückabwicklungsmatrix mit Anspruchszielen. Abgrenzung: nicht Rücktritt §§ 346 ff. BGB. |
| `anfg-anfechtungsklage-prozessuales` | Mandant hat vollstreckbaren Titel und will angefochtene Vermögensverschiebung gerichtlich angreifen: Anfechtungsklage nach AnfG erheben. Normen: §§ 2 11 13 AnfG, §§ 195 199 BGB. Prüfraster: Titel und Fristprüfung, Duldungs- vs. Wertersatzantrag, sachliche Zuständigkeit AG/LG, örtliche Zuständigkeit. Output: Klageantragsentwurf Duldungsurteil mit Hilfsantrag Wertersatz. Abgrenzung: nicht InsO-Anfechtung durch Insolvenzverwalter. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Verschaerfte Haftung Abgetretene Forderung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit`

**Fokus:** Verschärfte Bereicherungshaftung nach § 819 BGB bei Bösgläubigkeit oder Rechtshängigkeit prüfen. Normen: §§ 819 818 Abs. 4 BGB. Prüfraster: Kenntnis des Mangels, Zeitpunkt, Umfang verschärfte Haftung, Rechtshängigkeitswirkung. Output: Prüfergebnis verschärfte Haftung mit Berechnungshinweis. Abgrenzung: nicht gutgläubiger Entreicherungsschutz § 818 Abs. 3 BGB.

# Verschärfte Haftung — § 819 BGB bei Bösgläubigkeit

## Triage — kläre vor der Prüfung

1. Wann hatte der Empfänger Kenntnis vom Mangel des Rechtsgrundes (§ 819 Abs. 1 BGB)?
2. Liegt ein Verstoß gegen ein Verbotsgesetz oder die guten Sitten vor (§ 819 Abs. 2 i.V.m. § 817 S. 1 BGB)?
3. Wann wurde die Klage zugestellt (Rechtshängigkeit → § 818 Abs. 4 BGB)?
4. Welche Nutzungen, Gebrauchsvorteile oder Surrogate sind ab Bösgläubigkeit angefallen?
5. Ist der Gegenstand nach Bösgläubigkeit zufällig untergegangen (verschärfte Zufallshaftung)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persönlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

§ 819 Abs. 1 BGB (Bösgläubigkeit: Kenntnis des Mangels) — § 819 Abs. 2 BGB (Gesetz-/Sittenverstoß) — § 818 Abs. 3 BGB (Entreicherungseinrede: ausgeschlossen) — § 818 Abs. 4 BGB (Rechtshängigkeit) — § 292 BGB (Haftung bei Pflicht zur Herausgabe) — §§ 987–993 BGB (EBV, entsprechend) — § 817 S. 1 BGB (verbotener Zweck beim Empfänger)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

§ 819 BGB schließt die Entreicherungseinrede aus und unterwirft den bösgläubigen Bereicherungsschuldner einer verschärften Haftung.

## Tatbestand § 819 Abs. 1 BGB — Kenntnis des Mangels

**Voraussetzung:** Positive Kenntnis der Tatsachen, aus denen sich das Fehlen des Rechtsgrundes ergibt. Grob fahrlässige Unkenntnis genügt nach dem Gesetzeswortlaut nicht (str.).

**Zeitpunkt:** Kenntnis muss nicht bei Empfang vorliegen; spätere Kenntnis führt zur verschärften Haftung ab dem Zeitpunkt der Kenntniserlangung.

## Tatbestand § 819 Abs. 2 BGB — Gesetzes- oder Sittenverstoß

Ist der Empfang der Leistung mit einem Verstoß gegen ein gesetzliches Verbot oder die guten Sitten verbunden (§ 817 S. 1 BGB), tritt die verschärfte Haftung ab Empfang ein.

## Rechtsfolge der Verschärfung

- Kein Entreicherungseinwand nach § 818 Abs. 3 BGB.
- Haftung für zufälligen Untergang (§ 287 S. 2 BGB analog).
- Herausgabe von Nutzungen auch wenn nicht gezogen aber hätten können werden können.
- Haftung für Verschlechterungen.

## Rechtshängigkeit (§ 818 Abs. 4 BGB)

Ab Zustellung der Klageschrift: dieselben verschärften Regeln, unabhängig von Bösgläubigkeit.

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkürzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. Wann Kenntnis vom Mangel des Rechtsgrundes (§ 819 Abs. 1)?
2. Gesetz-/Sittenverstoß beim Empfänger (§ 819 Abs. 2)?
3. Wann Zustellung Klageschrift (Rechtshängigkeit § 818 Abs. 4)?
4. Nutzungen und Schäden ab diesem Zeitpunkt?

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefüllt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** mögliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Bereicherungsschuldner bösgläubig ab bestimmtem Zeitpunkt | § 819 Abs. 1 Kenntnisnachweis; Template-Prüfung unten |
| Variante A — Kenntnis schwer nachweisbar | Häufung von Indizien; Rechtshängigkeits-Zustellzeitpunkt sicherer |
| Variante B — Gesetzes- oder Sittenverstoß (§ 819 Abs. 2) | Verschärfung ab Empfang; kein Kenntnisnachweis nötig |
| Variante C — Gesamtschuldner mit unterschiedlicher Kenntnis | Individuell je Schuldner prüfen; kein Einheitsansatz |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzulösen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Prüfung § 819 BGB — Verschärfte Haftung**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Positive Kenntnis des Mangels (§ 819 Abs. 1) | ja ab [...] / nein |
| Gesetz-/Sittenverstoß (§ 819 Abs. 2) | ja → ab Empfang / nein |
| Rechtshängigkeit (§ 818 Abs. 4) | ab [...] (Zustellung) |
| Entreicherungseinrede ausgeschlossen | ja (ab Bösgläubigkeit/Rechtshängigkeit) |
| Nutzungen herausgebbar | ja: [...] EUR / nein |
| Zufälliger Untergang ab Bösgläubigkeit | ja → haftet / nein |

**Ergebnis:** Verschärfte Haftung nach § 819 BGB ab [...]. Anspruch in Höhe von [...] EUR.

---

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Lösung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwünscht? [Mediation / Direktgespräch / Settlement vor Klageerhebung]

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 2. `abgetretene-forderung-und-zession`

**Fokus:** Dieses Fachmodul greift, wenn Abtretung, Zahlung und Forderungsbestand auseinandergehalten werden müssen. Normen: §§ 398-413 BGB sowie §§ 812 und 818 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Zessionsmatrix mit Deckungs- und Valutaverhältnis, Anspruchsgegner und Belegbedarf. Abgrenzung: nicht Insolvenzanfechtung §§ 129 ff. InsO.

# Abgetretene Forderung und Zession

## Einsatzbereich

Dieses Fachmodul greift, wenn Abtretung, Zahlung und Forderungsbestand auseinandergehalten werden müssen. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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

## Typische Fehler

- Tatsächlichen Empfänger automatisch als Schuldner behandeln.
- Doppelmangel zu einem Pauschalanspruch verschmelzen.
- Insolvenzrisiko ohne Rechtsgrund verlagern.

## Zessionsspezifische Sonderfragen

- **§ 407 BGB Schutz des Schuldners:** Schuldner darf an Zedenten leisten, solange er die Abtretung nicht kennt — Zessionar trägt das Risiko der Mitteilung. Bei nichtiger Zession wirkt Zahlung an Zedenten **schuldbefreiend** gegenüber dem Schuldner.
- **§ 404 BGB Einwendungserhalt:** Zessionar muss alle Einwendungen aus dem Schuldverhältnis gegen sich gelten lassen, die der Schuldner gegen den Zedenten hatte (z. B. Mangelhaftung, Aufrechnungslage § 406 BGB).
- **Globalzession vs. Sicherungszession:**
 - Sicherungszession: Zessionar (i.d.R. Bank) hält Forderung treuhänderisch; bei Tilgung Rückübertragungspflicht. Wirtschaftliche Zuordnung bleibt Zedent.
 - Globalzession: Übertragung aller bestehenden und künftigen Forderungen — Bestimmtheits- und Bestimmbarkeitserfordernis (BGH-Linie zu § 398 BGB).
- **Doppelzession und Prioritätsgrundsatz:** Erste wirksame Abtretung erfasst die Forderung (§ 398 BGB), zweite geht ins Leere — außer § 405 BGB (Urkundenvorlage und Schuldnerschutz).
- **Insolvenzanfechtung der Zession § 130 InsO:** kongruente Deckung anfechtbar binnen 3 Monaten vor Antrag; bei Globalzession Anfechtungsfrist beachten — BGH-Linie zur Vertragstreue bei revolvierenden Sicherheiten.

## Bereicherungsrechtliche Wickung im Zessions-Dreieck

- **Schuldner zahlt an Nichtberechtigten** (Zessionar bei nichtiger Zession): Leistungskondiktion gegen Empfänger? Oder Direktkondiktion des Zedenten?
- **Empfehlung BGH:** Wickung **in der jeweils fehlerhaften Beziehung** (Zessionsverhältnis), d. h. Zedent kondiziert vom Zessionar. Direktkondiktion nur in Ausnahmefällen (§ 822 BGB-Konstellationen, Doppelmangel).

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

## 3. `anfechtung-142-und-rueckabwicklung`

**Fokus:** Dieses Fachmodul greift, wenn eine wirksame Anfechtung den Rechtsgrund rückwirkend beseitigt. Normen: §§ 119 bis 124 BGB sowie §§ 142 und 812 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Anfechtungs- und Rückabwicklungsmatrix mit Anspruchszielen. Abgrenzung: nicht Rücktritt §§ 346 ff. BGB.

# Anfechtung nach § 142 BGB und Rückabwicklung

## Einsatzbereich

Dieses Fachmodul greift, wenn eine wirksame Anfechtung den Rechtsgrund rückwirkend beseitigt. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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

## Anfechtungstatbestände im Überblick (§§ 119–124 BGB)

- **§ 119 Abs. 1 BGB Inhaltsirrtum:** Irrtum über Erklärungsinhalt — kausaler Irrtum bei verständiger Würdigung.
- **§ 119 Abs. 1 BGB Erklärungsirrtum:** Verschreiben, Vergreifen — Falschübermittlung.
- **§ 119 Abs. 2 BGB Eigenschaftsirrtum:** verkehrswesentliche Eigenschaft einer Person oder Sache (z. B. Authentizität eines Gemäldes).
- **§ 120 BGB Übermittlungsirrtum:** Bote übermittelt falsch.
- **§ 123 Abs. 1 BGB arglistige Täuschung / widerrechtliche Drohung:** verschärfte Schutzwirkung, keine Schadensersatzpflicht § 122 BGB.
- **Fristen:** § 121 BGB unverzüglich (für § 119, 120 BGB); § 124 BGB ein Jahr ab Entdeckung (für § 123 BGB).

## Rechtsfolge § 142 Abs. 1 BGB

- **Ex tunc-Nichtigkeit:** das angefochtene Rechtsgeschäft wird **von Anfang an** nichtig — Rechtsgrund entfällt rückwirkend.
- **Folge:** §§ 812 Abs. 1 S. 1 Alt. 1 BGB Leistungskondiktion (Leistung ohne Rechtsgrund, weil Rechtsgrund weggefallen ist) — Rückabwicklung in Natur (§ 818 Abs. 1 BGB) oder Wertersatz (§ 818 Abs. 2 BGB).

## Saldotheorie bei gegenseitigen Verträgen

- Bei nichtigem gegenseitigem Vertrag (z. B. Kauf nach § 142 BGB): Saldotheorie der h.M. — der Mindererlangende kondiziert nur den Differenzbetrag (Saldo) zur Gegenleistung.
- **Ausnahmen** der Saldotheorie (Zweikondiktionentheorie greift): § 119 BGB-Anfechtung wegen Eigenschaftsirrtum; § 123 BGB-Täuschung zum Schutz des Getäuschten; Geschäftsunfähige § 105 BGB; Minderjährige § 106 BGB.
- **Bei § 123 BGB:** Getäuschter kann **volle** Rückzahlung verlangen, ohne eigene Gegenleistung anrechnen zu müssen — wegen Sittenwidrigkeit der Täuschung.

## Schadensersatz und § 122 BGB

- § 122 BGB Vertrauensschaden bei §§ 119, 120 BGB: Anfechtender haftet für Vertrauensschaden, nicht für Erfüllungsinteresse.
- Bei § 123 BGB **keine** Haftung des Anfechtenden — Täuschende/Drohende verlieren Vertrauensschutz.

## Anti-Halluzinations-Hinweise

- § 142 BGB ist **nicht** zu verwechseln mit § 142 InsO (Bargeschäft) — Bezeichnung "Anfechtung" findet sich in beiden Gebieten.
- § 119 ff. BGB betreffen Willenserklärungen, nicht das Insolvenzanfechtungsrecht (§§ 129 ff. InsO).

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

## 4. `anfg-anfechtungsklage-prozessuales`

**Fokus:** Mandant hat vollstreckbaren Titel und will angefochtene Vermögensverschiebung gerichtlich angreifen: Anfechtungsklage nach AnfG erheben. Normen: §§ 2 11 13 AnfG, §§ 195 199 BGB. Prüfraster: Titel und Fristprüfung, Duldungs- vs. Wertersatzantrag, sachliche Zuständigkeit AG/LG, örtliche Zuständigkeit. Output: Klageantragsentwurf Duldungsurteil mit Hilfsantrag Wertersatz. Abgrenzung: nicht InsO-Anfechtung durch Insolvenzverwalter.

# Anfechtungsklage AnfG — Prozessuales

## Triage — kläre vor Klageerhebung

1. Liegt ein vollstreckbarer Titel gegen den Schuldner vor (§ 2 AnfG)?
2. Ist die Verjährungsfrist nach §§ 195 199 BGB (3 Jahre) noch nicht abgelaufen?
3. Ist der Streitwert für AG (bis EUR 5.000) oder LG (über EUR 5.000)?
4. Wird Duldung (Regelfall) oder Wertersatz (bei Untergang des Gegenstands) beantragt?

## Zentrale Normen

- § 2 AnfG — Anfechtungsberechtigung (Titel, fällige Forderung, Fruchtlosigkeit)
- § 11 AnfG — Rechtsfolge: Duldung der Zwangsvollstreckung
- § 13 AnfG — Klage oder Widerspruch in der Zwangsvollstreckung
- §§ 195 199 BGB — Regelmässige Verjährungsfrist 3 Jahre ab Kenntnis
- §§ 23 71 GVG — Sachliche Zuständigkeit (AG unter EUR 5.000 / LG über EUR 5.000)
- §§ 888 890 ZPO — Vollstreckung aus Duldungsurteil

## Rechtsprechung (BGH — Leitsätze AnfG)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Klageform

Die Anfechtung nach dem AnfG kann nach § 13 AnfG durch Klage oder (in laufenden Vollstreckungsverfahren) durch Widerspruch gegen die Zwangsvollstreckung geltend gemacht werden.

## Klagefrist und Verjährung

Kein gesetzlich festgelegter Klagezwang; jedoch läuft die Verjährung des Anfechtungsanspruchs nach § 195 BGB in drei Jahren ab Kenntnis von Rechtshandlung und Anfechtungsgrund (§ 199 Abs. 1 BGB). Anfechtungsklage ist als verjährungshemmende Maßnahme zu verstehen.

## Sachliche Zuständigkeit

- Bis EUR 5.000: Amtsgericht (§ 23 Nr. 1 GVG).
- Über EUR 5.000: Landgericht (§ 71 Abs. 1 GVG).
- Die Zuständigkeit richtet sich nach dem Wert des angefochtenen Gegenstands.

## Örtliche Zuständigkeit

Allgemeiner Gerichtsstand des Anfechtungsgegners (§ 12 ZPO, §§ 13 17 ZPO). Kein besonderer Gerichtsstand im AnfG selbst.

## Klageantrag — Tenor

**Duldungsantrag:** Der Beklagte wird verurteilt, die Zwangsvollstreckung in [konkret bezeichneten Gegenstand] zu dulden, soweit dies zur Befriedigung der vollstreckbaren Forderung des Klägers gegen [Schuldner] aus dem Urteil des [Gericht] vom [Datum] in Höhe von [Betrag] erforderlich ist.

**Hilfsantrag Wertersatz:** Hilfsweise: Der Beklagte wird verurteilt, an den Kläger EUR [Betrag] zu zahlen.

## Streitwert

Wert des angefochtenen Gegenstands, maximal begrenzt auf die Höhe der vollstreckbaren Forderung des Gläubigers.

## Vollstreckung

Das Anfechtungsurteil verpflichtet zur Duldung; Vollstreckung erfolgt nach §§ 888 890 ZPO (Ordnungsgeld oder Ordnungshaft) oder durch unmittelbare Zwangsvollstreckung in den Gegenstand.

## Output-Template Klageantrag AnfG

**Adressat:** Gericht — Tonfall: sachlich-juristisch

```
An das [GERICHT]

Klage

des [KLÄGER NAME] — Kläger —
gegen
[ANFECHTUNGSGEGNER NAME] — Beklagter —

wegen Duldung der Zwangsvollstreckung (§§ 2 11 13 AnfG)

Anträge:
1. Der Beklagte wird verurteilt, die Zwangsvollstreckung in [GEGENSTAND KONKRET BEZEICHNEN]
 zu dulden, soweit dies zur Befriedigung der vollstreckbaren Forderung des Klägers gegen
 [SCHULDNER] aus [TITEL] in Höhe von EUR [BETRAG] erforderlich ist.
2. Hilfsweise: Der Beklagte wird verurteilt, an den Kläger EUR [BETRAG] zu zahlen.

Streitwert: EUR [WERT DES GEGENSTANDS max. FORDERUNGSHÖHE]
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.
