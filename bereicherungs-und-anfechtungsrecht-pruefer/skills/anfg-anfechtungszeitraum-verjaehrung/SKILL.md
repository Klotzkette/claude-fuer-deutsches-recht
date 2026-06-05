---
name: anfg-anfechtungszeitraum-verjaehrung
description: "Anfg Anfechtungszeitraum Verjaehrung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anfg Anfechtungszeitraum Verjaehrung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Anfg Anfechtungszeitraum Verjaehrung** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anfg-fristen-und-anfechtungszeitraum` | Anfechtungsfristen im außerinsolvenzlichen Anfechtungsrecht bestimmen: zehn Jahre Vorsatzanfechtung, vier Jahre unentgeltliche Leistung. Normen: §§ 3 4 AnfG, §§ 195 199 BGB. Prüfraster: Fristbeginn, Fristberechnung, Verjährungsverhältnis, Hemmungstatbestände. Output: Fristenblatt mit Anfechtungszeiträumen. Abgrenzung: nicht InsO-Anfechtungsfristen §§ 130 ff. InsO. |
| `verjaehrung-bereicherung-anfechtung-fristen` | Verjährung und Anfechtungsfristen trennen: § 195 und § 199 BGB für Bereicherung, § 15 AnfG, § 146 InsO mit Verweis auf regelmäßige BGB-Verjährung. Prüft Fristbeginn, Kenntnis, grob fahrlässige Unkenntnis, Hemmung, Anfechtungszeiträume §§ 130-135 InsO und keine pauschale Zehn-Jahres-Grenze ab Rechtshandlung. |
| `konkurrenz-bereicherung-vertraglich-deliktisch` | Verhältnis von Bereicherungsrecht zu vertraglichen Ansprüchen und Deliktsrecht §§ 823 ff. BGB klären. Normen: §§ 812 823 987 ff. BGB. Prüfraster: Vorrang-/Spezialitätsfragen, bereicherungsrechtliche Lückenfüllung. Output: Anspruchsprioriserungstabelle. Abgrenzung: nicht Konkurrenz mit AnfG/InsO-Anfechtung (eigener Skill). |
| `nichtiger-vertrag-134-138-und-rueckforderung` | Dieses Fachmodul greift, wenn Verbots- oder Sittenwidrigkeit die Rückforderung prägt. Normen: §§ 134 und 138 BGB; §§ 812 und 817 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Prüfergebnis Rückforderung bei Nichtigkeit mit § 817-S.-2-Sperre. Abgrenzung: nicht Anfechtung §§ 119 ff. BGB. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Anfg Anfechtungszeitraum Verjaehrung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anfg-fristen-und-anfechtungszeitraum`

**Fokus:** Anfechtungsfristen im außerinsolvenzlichen Anfechtungsrecht bestimmen: zehn Jahre Vorsatzanfechtung, vier Jahre unentgeltliche Leistung. Normen: §§ 3 4 AnfG, §§ 195 199 BGB. Prüfraster: Fristbeginn, Fristberechnung, Verjährungsverhältnis, Hemmungstatbestände. Output: Fristenblatt mit Anfechtungszeiträumen. Abgrenzung: nicht InsO-Anfechtungsfristen §§ 130 ff. InsO.

# Fristen und Anfechtungszeitraum — AnfG

## Triage — kläre vor Fristprüfung

1. Wann wurde die anfechtbare Rechtshandlung vorgenommen (Datum)?
2. Wird Vorsatzanfechtung (§ 3 AnfG, 10 Jahre) oder unentgeltliche Leistung (§ 4 AnfG, 4 Jahre) geltend gemacht?
3. Wann hat der Gläubiger von der Rechtshandlung und dem Anfechtungsgrund Kenntnis erlangt? (Verjährungsbeginn §§ 195 199 BGB)
4. Ist die Verjährung bereits eingetreten oder kann sie noch gehemmt werden?

## Zentrale Normen

- § 3 Abs. 1 AnfG — Vorsatzanfechtung: Frist 10 Jahre
- § 4 Abs. 1 AnfG — Unentgeltliche Leistung: Frist 4 Jahre
- § 15 AnfG — Verjährung des Anfechtungsanspruchs (Verweis auf §§ 195 ff. BGB)
- §§ 195 199 BGB — Verjährungsfrist 3 Jahre ab Kenntnis Jahresende
- §§ 203-211 BGB — Hemmung der Verjährung (Verhandlungen, Klageerhebung)

## Rechtsprechung (BGH — Leitsätze Fristen AnfG)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Überblick Anfechtungsfristen

| Anfechtungstatbestand | Frist | Fristbeginn |
|---|---|---|
| § 3 Abs. 1 AnfG (Vorsatz) | 10 Jahre | Vornahme der Rechtshandlung |
| § 4 AnfG (unentgeltlich) | 4 Jahre | Vornahme der Rechtshandlung |

## Fristberechnung § 3 AnfG

Die Rechtshandlung muss innerhalb von zehn Jahren vor Erhebung der Anfechtungsklage oder (bei außergerichtlicher Anfechtung) vor der Anfechtungserklärung vorgenommen worden sein.

**Beginn der Frist:** Zeitpunkt der Vornahme der anfechtbaren Rechtshandlung, nicht Zeitpunkt der Kenntnis des Gläubigers.

**Rechtliche Handlung in mehreren Schritten:** Bei Grundstücksübertragungen beginnt die Frist mit Eintragung der Auflassung im Grundbuch (Vollendung der Rechtshandlung).

## Fristberechnung § 4 AnfG

Vier-Jahres-Frist, die rückwirkend von der Anfechtungserklärung berechnet wird.

## Verjährung des Anfechtungsanspruchs — § 15 AnfG

Der Anfechtungsanspruch verjährt nach § 15 AnfG in drei Jahren (§ 195 BGB), beginnend mit dem Schluss des Jahres, in dem der Gläubiger von der Rechtshandlung und dem Anfechtungsgrund Kenntnis erlangt hat (§ 199 Abs. 1 BGB).

**Absolute Grenze:** Zehn Jahre nach der Rechtshandlung (§ 199 Abs. 4 BGB analog; streitig).

## Praktische Checkliste

1. Wann wurde die Rechtshandlung vorgenommen?
2. Wird die Zehn-Jahres-Frist (§ 3) oder Vier-Jahres-Frist (§ 4) eingehalten?
3. Wann hat der Gläubiger von der Rechtshandlung Kenntnis erlangt?
4. Ist der Anfechtungsanspruch verjährt?

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 2. `verjaehrung-bereicherung-anfechtung-fristen`

**Fokus:** Verjährung und Anfechtungsfristen trennen: § 195 und § 199 BGB für Bereicherung, § 15 AnfG, § 146 InsO mit Verweis auf regelmäßige BGB-Verjährung. Prüft Fristbeginn, Kenntnis, grob fahrlässige Unkenntnis, Hemmung, Anfechtungszeiträume §§ 130-135 InsO und keine pauschale Zehn-Jahres-Grenze ab Rechtshandlung.

# Verjährung: Bereicherung, AnfG und InsO-Anfechtung

## Triage — kläre vor der Prüfung

1. Wann ist der Bereicherungs- oder Anfechtungsanspruch entstanden, und wann hatte der Gläubiger Kenntnis?
2. Ist die dreijährige Regelverjährung (§ 195 BGB) bereits abgelaufen?
3. Welche BGB-Höchstfrist ist einschlägig, und ab welchem Zeitpunkt läuft sie wirklich?
4. Wurde die Verjährung gehemmt (§§ 203 ff. BGB: Verhandlungen, Klageerhebung, Mahnbescheid)?
5. Handelt es sich um eine Anfechtungsfrist (§§ 3, 4 AnfG; §§ 130–134 InsO) oder um die Verjährung des Rückgewähranspruchs (§ 15 AnfG; § 146 InsO)?

## Zentrale Normen

§ 195 BGB (Regelverjährung drei Jahre) — § 199 BGB (Verjährungsbeginn und Höchstfristen) — §§ 203–213 BGB (Verjährungshemmung) — § 15 AnfG (Verjährung AnfG-Anspruch) — § 146 InsO (Verjährung InsO-Anfechtung) — §§ 3, 4 AnfG (Anfechtungsfristen zehn / vier Jahre) — §§ 130–135 InsO (Anfechtungszeiträume)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Übersicht Verjährungsfristen

| Anspruchsgrundlage | Verjährungsfrist | Beginn | Absolute Grenze |
|---|---|---|---|
| § 812 BGB | drei Jahre (§ 195 BGB) | Schluss des Jahres der Kenntnis (§ 199 Abs. 1) | zehn Jahre ab Entstehung (§ 199 Abs. 4) |
| § 11 AnfG | drei Jahre (§ 15 AnfG) | Kenntnis von Handlung und Anfechtungsgrund | zehn Jahre (§ 199 Abs. 4 analog) |
| §§ 129 ff. InsO | regelmäßige Verjährung nach BGB (§ 146 InsO) | nach BGB, regelmäßig Schluss des Jahres der Kenntnis oder grob fahrlässigen Unkenntnis | Höchstfristen nach § 199 BGB fallbezogen prüfen |

## Anfechtungsfristen (materiell-rechtlich, keine Verjährung)

| Anfechtungstatbestand | Frist |
|---|---|
| § 3 Abs. 1 AnfG (Vorsatz) | zehn Jahre |
| § 4 AnfG (Unentgeltlichkeit) | vier Jahre |
| § 130 InsO (kongruente Deckung) | drei Monate |
| § 131 InsO (inkongruente Deckung) | drei Monate |
| § 133 Abs. 1 InsO (Vorsatz) | zehn Jahre |
| § 133 Abs. 2 InsO (Deckungshandlung) | vier Jahre |
| § 133 Abs. 4 InsO (entgeltlicher Vertrag mit nahestehender Person) | zwei Jahre |
| § 134 InsO (Unentgeltlichkeit) | vier Jahre |
| § 135 Abs. 1 Nr. 1 InsO (Sicherheit Gesellschafterdarlehen) | zehn Jahre |
| § 135 Abs. 1 Nr. 2 InsO (Befriedigung Gesellschafterdarlehen) | ein Jahr |

## Prüfschema

1. Anspruch entstanden wann? Kenntnis wann?
2. Dreijährige Verjährung abgelaufen?
3. Höchstfrist nach § 199 BGB fallbezogen bestimmen; nicht mit dem Anfechtungszeitraum verwechseln.
4. Hemmung (Klage, Mahnbescheid, Verhandlungen)?
5. Anfechtungsfrist noch offen (gesondert von Verjährung!)?

## Output-Template

**Prüfung Verjährung — Bereicherung / AnfG / InsO**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Entstehung des Anspruchs | [...] |
| Kenntnis des Gläubigers/Verwalters | [...] |
| Verjährungsbeginn (Schluss des Jahres) | 31.12.[Jahr] |
| Verjährungsende (drei Jahre) | 31.12.[Jahr+3] |
| Heute noch offen? | ja / nein → verjährt |
| BGB-Höchstfrist | [...] → eingehalten / überschritten / offen |
| Hemmung eingetreten | ja: [...] / nein |
| Anfechtungsfrist (§§ 3/4 AnfG; §§ 130–134 InsO) | offen / abgelaufen |

**Ergebnis:** Anspruch [verjährt / nicht verjährt]. Anfechtungsfrist [offen / abgelaufen].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 3. `konkurrenz-bereicherung-vertraglich-deliktisch`

**Fokus:** Verhältnis von Bereicherungsrecht zu vertraglichen Ansprüchen und Deliktsrecht §§ 823 ff. BGB klären. Normen: §§ 812 823 987 ff. BGB. Prüfraster: Vorrang-/Spezialitätsfragen, bereicherungsrechtliche Lückenfüllung. Output: Anspruchsprioriserungstabelle. Abgrenzung: nicht Konkurrenz mit AnfG/InsO-Anfechtung (eigener Skill).

# Konkurrenz: Bereicherung neben Vertrag, Delikt und EBV

## Triage — kläre vor der Prüfung

1. Besteht ein wirksamer Vertrag mit eigenem Rückabwicklungsregime (§§ 346 ff. BGB bei Rücktritt) — verdrängt dieser § 812 BGB?
2. Ist der Vertrag nichtig (§§ 134, 138, 142 BGB) — fehlt damit der Rechtsgrund für § 812 BGB?
3. Soll Schadensersatz (§§ 823 ff. BGB, Verschulden erforderlich) oder Herausgabe des Erlangten (§ 812 BGB, kein Verschulden) geltend gemacht werden?
4. Liegt eine Konstellation des Eigentümer-Besitzer-Verhältnisses vor (§§ 987 ff. BGB als lex specialis)?
5. Welche Verjährungsfrist ist günstiger (§ 195 BGB, 3 Jahre, gilt für alle)?

## Zentrale Normen

§ 812 Abs. 1 BGB (Leistungskondiktion) — §§ 346 ff. BGB (Rücktrittsfolgen) — §§ 134, 138, 142 BGB (Nichtigkeitsgründe) — §§ 823, 826 BGB (Deliktshaftung) — §§ 985–993 BGB (Eigentümer-Besitzer-Verhältnis) — § 195 BGB (Regelverjährung) — § 199 BGB (Verjährungsbeginn)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Grundsatz: Subsidiarität des Bereicherungsrechts

Das Bereicherungsrecht ist in bestimmten Konstellationen subsidiär, in anderen kann es neben anderen Ansprüchen stehen.

## § 812 BGB neben vertraglichen Ansprüchen

### Nebeneinander möglich

- Nichtiger Vertrag: kein Erfüllungsanspruch, aber § 812 BGB greift.
- Anfechtung des Vertrags (§ 142 BGB): § 812 BGB für die Rückabwicklung.

### Ausschluss bei wirksamen Rückabwicklungsregeln

Bei Rücktritt (§§ 346 ff. BGB) verdrängen diese den § 812 BGB-Anspruch für die Rückabwicklung des konkreten Vertragsverhältnisses.

## § 812 BGB neben §§ 823 ff. BGB (Delikt)

**Nebeneinander:** Bereicherungsrecht und Deliktsrecht stehen nebeneinander.

**Unterschied:** Delikt setzt Verschulden voraus; § 812 BGB nicht. Deliktsrecht gewährt Schmerzensgeld; § 812 BGB nur Herausgabe des wirtschaftlichen Vorteils.

**Verjährung:** § 195 BGB (drei Jahre) gilt für beide; Beginn nach § 199 BGB.

## § 812 BGB neben §§ 987 ff. BGB (EBV)

**Vorrang des EBV:** §§ 987 ff. BGB sind als lex specialis gegenüber § 812 BGB zu betrachten, solange Eigentum und Besitz auseinanderfallen.

**Subsidiarität des § 812 BGB:** Ist § 985 BGB gegeben, kann daneben kein § 812 BGB-Anspruch auf denselben Gegenstand geltend gemacht werden.

**Ausnahme:** Nach Eigentumsübergang (z. B. gutgläubiger Erwerb) greift § 812 BGB wieder.

## Prüfschema

1. Wirksamer Vertrag mit Rücktrittsfolge? → §§ 346 ff. BGB verdrängen § 812 BGB.
2. Vertrag nichtig (§§ 134/138/142)? → § 812 BGB greift.
3. Delikt und Bereicherung nebeneinander? → ja, Wahl der günstigsten Grundlage.
4. EBV (§§ 987 ff.) einschlägig? → lex specialis, § 812 BGB tritt zurück.

## Output-Template

**Konkurrenzprüfung: § 812 BGB neben anderen Ansprüchen**

Sachverhalt (kurz): [...]

| Konkurrenz | Ergebnis |
|---|---|
| Wirksamer Vertrag + Rücktritt | §§ 346 ff. BGB vorrangig / § 812 verdrängt |
| Nichtiger Vertrag | § 812 Abs. 1 S. 1 BGB direkt einschlägig |
| Deliktshaftung §§ 823 ff. | nebeneinander mit § 812 BGB |
| EBV §§ 987 ff. / § 985 BGB | lex specialis; § 812 nur nach Eigentumsübergang |

**Empfehlung:** Stütze Klage primär auf [...]; hilfsweise auf [...].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 4. `nichtiger-vertrag-134-138-und-rueckforderung`

**Fokus:** Dieses Fachmodul greift, wenn Verbots- oder Sittenwidrigkeit die Rückforderung prägt. Normen: §§ 134 und 138 BGB; §§ 812 und 817 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Prüfergebnis Rückforderung bei Nichtigkeit mit § 817-S.-2-Sperre. Abgrenzung: nicht Anfechtung §§ 119 ff. BGB.

# Nichtiger Vertrag nach §§ 134 und 138 BGB

## Einsatzbereich

Dieses Fachmodul greift, wenn Verbots- oder Sittenwidrigkeit die Rückforderung prägt. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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
