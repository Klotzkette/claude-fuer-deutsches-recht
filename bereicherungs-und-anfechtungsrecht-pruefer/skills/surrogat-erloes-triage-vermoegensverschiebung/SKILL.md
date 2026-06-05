---
name: surrogat-erloes-triage-vermoegensverschiebung
description: "Surrogat Erloes Triage Vermoegensverschiebung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Surrogat Erloes Triage Vermoegensverschiebung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Surrogat Erloes Triage Vermoegensverschiebung** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `surrogat-erloes-versicherung-ersatzforderung` | Dieses Fachmodul greift, wenn an die Stelle des Erlangten ein Ersatzwert getreten sein kann. Normen: § 818 Abs. 1 BGB; § 285 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und ersparte Aufwendungen vor § 818 Abs. 3 BGB; Bewerte Dienstleistung und Gebrauchsvorteil objektiv nach Markt- oder Nutzungswert. Output: Surrogationskette mit Erlös, Versicherungsleistung und Ersatzforderung. Abgrenzung: nicht Schadensersatzforderung gegen Schädiger direkt. |
| `triage-vermoegensverschiebung-erfassen` | Erster Schritt: Vermögenverschiebung strukturiert erfassen für Bereicherungs- und Anfechtungsrecht. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Wer hat was an wen geleistet, Zeitpunkt, Belegsicherung, Weichenstellung Regelungskreis. Output: Erfassungsbogen Vermögenverschiebung. Abgrenzung: nicht inhaltliche Prüfung. |
| `umfang-der-herausgabe-818-bgb-und-entreicherung` | Umfang der Bereicherungshaftung nach § 818 BGB bestimmen: Erlangtes, Nutzungen, Surrogate, Wertersatz, Entreicherung, ersparte Aufwendungen und Zurechnung des Wegfalls. Output: Werttabelle mit Einredeprüfung. |
| `verfuegung-eines-nichtberechtigten-816-bgb` | Bereicherungsanspruch des Berechtigten nach § 816 BGB gegen verfügenden Nichtberechtigten prüfen. Normen: § 816 BGB. Prüfraster: wirksame Verfügung durch Gutglaubenserwerb oder Genehmigung, entgeltlich vs. unentgeltlich, Anspruch auf Erlangtes. Output: Prüfergebnis Anspruch § 816 BGB. Abgrenzung: nicht § 822 BGB (unentgeltliche Weitergabe). |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Surrogat Erloes Triage Vermoegensverschiebung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `surrogat-erloes-versicherung-ersatzforderung`

**Fokus:** Dieses Fachmodul greift, wenn an die Stelle des Erlangten ein Ersatzwert getreten sein kann. Normen: § 818 Abs. 1 BGB; § 285 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und ersparte Aufwendungen vor § 818 Abs. 3 BGB; Bewerte Dienstleistung und Gebrauchsvorteil objektiv nach Markt- oder Nutzungswert. Output: Surrogationskette mit Erlös, Versicherungsleistung und Ersatzforderung. Abgrenzung: nicht Schadensersatzforderung gegen Schädiger direkt.

# Surrogat, Erlös, Versicherung und Ersatzforderung

## Einsatzbereich

Dieses Fachmodul greift, wenn an die Stelle des Erlangten ein Ersatzwert getreten sein kann. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Was war ursprünglich erlangt und was ist heute noch vorhanden?
2. Welche Nutzungen, Surrogate, Erlöse oder Ersatzforderungen gibt es?
3. Welche eigenen Ausgaben wurden erspart?
4. Wann traten Verlust, Verbrauch, Kenntnis und Rechtshängigkeit ein?
5. Welche Bewertungsmethode ist belegbar?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Erstelle eine Vermögensbilanz statt einer Gegenstandsliste.
- Prüfe Nutzungen, Surrogate und ersparte Aufwendungen vor § 818 Abs. 3 BGB.
- Bewerte Dienstleistung und Gebrauchsvorteil objektiv nach Markt- oder Nutzungswert.
- Ordne Wertverluste nach Risiko, Kenntnis und Rechtshängigkeit zu.
- Verlange substantiierte Belege für Entreicherung.

## Surrogat-Suchroutine

Prüfe bei behauptetem Wegfall immer:

- Verkaufserlös oder Tauschgegenstand.
- Rückerstattung, Gutschrift oder Verrechnung.
- Versicherungsleistung oder Schadensersatzanspruch.
- Ersatzlieferung oder Ersatzforderung.
- ersparte Neuanschaffung.
- Wertsteigerung eines anderen Vermögensgegenstands.

Ein Surrogat muss nicht denselben Namen tragen wie das Erlangte. Entscheidend ist, ob der Vermögensvorteil wirtschaftlich an die Stelle des ursprünglichen Vorteils getreten ist.

## Typische Fehler

- "Geld ist weg" als Ergebnis genügen lassen.
- Surrogate und Ersparnisse übersehen.
- Zinsen, Nutzungen und Wertersatz doppelt zählen.

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

## Surrogat-Output

| ursprünglicher Vorteil | Ersatzwert | noch vorhanden? | herauszugeben? |
|---|---|---|---|
| [...] | [...] | ja / nein | ja / nein / streitig |

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

## 2. `triage-vermoegensverschiebung-erfassen`

**Fokus:** Erster Schritt: Vermögenverschiebung strukturiert erfassen für Bereicherungs- und Anfechtungsrecht. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Wer hat was an wen geleistet, Zeitpunkt, Belegsicherung, Weichenstellung Regelungskreis. Output: Erfassungsbogen Vermögenverschiebung. Abgrenzung: nicht inhaltliche Prüfung.

# Triage: Vermögensverschiebung erfassen

## Triage — kläre vor der Prüfung

1. Sind alle Beteiligten (Leistender, Empfänger, weitere Personen) vollständig identifiziert?
2. Ist der Gegenstand der Vermögensverschiebung (Geld, Sache, Forderung, Sicherheit) konkret bezeichnet?
3. Ist das genaue Datum oder der Zeitraum der Vermögensverschiebung bekannt?
4. Liegt eine rechtliche Beziehung zwischen den Beteiligten vor (Vertrag, Gesellschaft, Ehe)?
5. Ist über das Vermögen des Leistenden ein Insolvenzverfahren eröffnet oder beantragt?

## Zentrale Normen

§ 812 Abs. 1 BGB (Leistungsbegriff, Zweckbestimmung) — § 129 InsO (Rechtshandlung vor Verfahrenseröffnung) — § 2 AnfG (vollstreckbarer Titel) — § 17 InsO (Zahlungsunfähigkeit: maßgeblicher Zeitpunkt) — § 199 BGB (Verjährungsbeginn: Kenntnis) — § 286 BGB (Verzugseintritt: Datum der Forderung)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ist der Einstiegspunkt. Bevor eine Weichenstellung zwischen Bereicherungsrecht, AnfG-Anfechtung und InsO-Anfechtung erfolgen kann, muss der Lebenssachverhalt vollständig und strukturiert vorliegen.

## Ablauf

### Schritt 1 — Beteiligte Personen

1. Wer ist Leistender?
2. Wer ist Empfänger?
3. Gibt es weitere Beteiligte (Bevollmächtigte, Treuhänder, Gesellschaften)?
4. Besteht zwischen Leistendem und Empfänger eine rechtliche Beziehung?

### Schritt 2 — Art der Vermögensverschiebung

1. Was wurde übertragen (Geld, Sache, Forderungsabtretung, Grundstücksübereignung, Sicherheit)?
2. In welcher Form (Überweisung, Barzahlung, notarielle Übertragung, Pfandbestellung)?
3. Wann fand die Vermögensverschiebung statt (Datum oder Zeitraum)?
4. Welchen Wert hatte die Vermögensverschiebung?

### Schritt 3 — Rechtlicher Rahmen

1. Liegt ein schriftlicher oder mündlicher Vertrag vor?
2. Besteht oder bestand ein vollstreckbarer Titel?
3. Ist ein Insolvenzverfahren eröffnet oder beantragt?
4. Gibt es Hinweise auf Zahlungsunfähigkeit zum Zeitpunkt der Leistung?

### Schritt 4 — Belegerfassung

- Kontoauszüge oder Buchungsbelege
- Vertragsurkunden oder Quittungen
- Notarielle Urkunden
- Schriftverkehr, E-Mails oder SMS
- Vollstreckungstitel
- Insolvenzaktenzeichen und Beschlüsse des Insolvenzgerichts

## Typische Erfassungsfehler

- Schätzungen statt konkreter Daten.
- Beteiligte Dritte werden nicht erwähnt.
- Zeitpunkt der Bestellung statt der tatsächlichen Vermögensverschiebung.
- Teilvermögensverschiebungen werden als Einheit geschildert.

## Output-Template

**Triage: Vermögensverschiebung**

| Merkmal | Angabe des Nutzers |
|---|---|
| Leistender | [...] |
| Empfänger | [...] |
| Weitere Beteiligte | [...] / keine |
| Gegenstand der Leistung | [...] |
| Form der Leistung | [...] |
| Datum / Zeitraum | [...] |
| Wert | [...] EUR |
| Rechtsbeziehung | Vertrag / keine |
| Vollstreckbarer Titel | ja / nein |
| Insolvenzverfahren | eröffnet / beantragt / nein |
| Hinweise auf Zahlungsunfähigkeit | ja: [...] / nein |

**Weiter zu:** Weichenstellung → `weichenstellung-bereicherung-oder-anfechtung`

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 3. `umfang-der-herausgabe-818-bgb-und-entreicherung`

**Fokus:** Umfang der Bereicherungshaftung nach § 818 BGB bestimmen: Erlangtes, Nutzungen, Surrogate, Wertersatz, Entreicherung, ersparte Aufwendungen und Zurechnung des Wegfalls. Output: Werttabelle mit Einredeprüfung.

# Umfang der Herausgabe — § 818 BGB und Entreicherung

## Triage — kläre vor der Prüfung

1. Was genau wurde erlangt, und ist Herausgabe in Natur noch möglich?
2. Wurden Nutzungen oder Surrogate aus dem Erlangten gezogen (§ 818 Abs. 1 Alt. 1 und 2 BGB)?
3. Ist der Empfänger noch bereichert, oder hat er das Erlangte verbraucht/verloren (§ 818 Abs. 3 BGB)?
4. Kannte der Empfänger den Mangel des Rechtsgrundes — liegt Bösgläubigkeit vor (§ 819 BGB)?
5. Ist die Klage bereits zugestellt (Rechtshängigkeit → § 818 Abs. 4 BGB)?

## Zentrale Normen

§ 818 Abs. 1 BGB (Herausgabe, Nutzungen, Surrogate) — § 818 Abs. 2 BGB (Wertersatz) — § 818 Abs. 3 BGB (Entreicherungseinrede) — § 818 Abs. 4 BGB (Rechtshängigkeit) — § 819 BGB (verschärfte Haftung Bösgläubigkeit) — § 292 BGB (Haftung des Schuldners ab Rechtshängigkeit) — §§ 987–993 BGB (EBV, entsprechend anwendbar)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Primäranspruch: Herausgabe des Erlangten (§ 818 Abs. 1 BGB)

**Gegenstand:** Alles Erlangte einschließlich:
- Der Sache oder des Geldbetrags selbst.
- Gezogener Nutzungen (Früchte, Gebrauchsvorteile: § 818 Abs. 1 Alt. 1 BGB).
- Surrogate: Was der Empfänger aufgrund des erlangten Rechts oder als Ersatz für Zerstörung/Beschädigung erlangt hat (§ 818 Abs. 1 Alt. 2 BGB).
- ersparte Aufwendungen, wenn der Empfänger eigene Kosten nicht tragen musste.

## Vermögensbilanz statt Gegenstandsfixierung

Die Prüfung darf nicht beim Satz enden: "Der Gegenstand ist weg." § 818 BGB verlangt eine Vermögensbilanz:

1. Ursprünglich erlangter Vorteil.
2. Heute noch vorhandener Vorteil.
3. Ersatzwerte, Erlöse, Forderungen, Versicherungsleistungen.
4. Nutzungen und Gebrauchsvorteile.
5. Ersparnisse eigener Aufwendungen.
6. Wegfall des Vorteils und dessen Zurechnung.

Verwende bei komplexen Fällen zusätzlich `nutzungen-verwendungen-gefahrtragung-818`.

## Vorteilsstrang-Methode

Verfolge den Vorteil wie einen Strang durch das Vermögen:

| Stufe | Frage | Folge |
|---|---|---|
| Ursprung | Was wurde erlangt? | Ausgangswert |
| Umwandlung | Wurde der Vorteil verkauft, getauscht, verrechnet oder ersetzt? | Surrogat/Ersatzwert |
| Nutzung | Wurden Früchte, Zinsen oder Gebrauchsvorteile gezogen? | zusätzlicher Herausgabeposten |
| Verbrauch | Wurde der Vorteil ausgegeben oder verbraucht? | § 818 Abs. 3 nur nach Ersparnisprüfung |
| Risikowechsel | Wann kamen Kenntnis oder Rechtshängigkeit hinzu? | verschärfte Haftung |
| Sonderwertung | Gibt es Minderjährigen-, Verbraucher-, EBV- oder Vertragsrückabwicklung? | Korrektur des Ergebnisses |

Diese Methode verhindert, dass die Entreicherungseinrede die eigentliche Rechtsfolgenprüfung ersetzt.

## Wertersatz (§ 818 Abs. 2 BGB)

Herausgabe in Natur unmöglich (Dienstleistung, Verbrauch) → Wertersatz. Bewertungszeitpunkt: Wert beim Empfang (h.M.).

## Entreicherungseinrede (§ 818 Abs. 3 BGB)

**Tatbestand:** Empfänger ist nicht mehr bereichert — das Erlangte ist aus seinem Vermögen ausgeschieden ohne Surrogat oder Ersparniseffekt.

**Beispiele:**
- Geld für Konsumausgaben verbraucht (keine Ersparnis eigener Ausgaben) → bereichert nicht mehr.
- Sache untergegangen ohne Versicherungsleistung → bereichert nicht mehr.
- Nicht: Geld für Miete ausgegeben, die sowieso hätte gezahlt werden müssen (Ersparnis = noch bereichert).

## Zurechnung des Wegfalls

Der Wegfall ist nur beachtlich, wenn er bereicherungsrechtlich dem Empfänger nicht mehr zugerechnet wird. Prüfe deshalb:

- **Surrogat:** Ist etwas an die Stelle des Erlangten getreten?
- **Ersparnis:** Wurden eigene Ausgaben vermieden?
- **Eigenes Risiko:** Hat der Empfänger den Vorteil spekulativ eingesetzt, freiwillig verschenkt oder bewusst verbraucht?
- **Verbrauchsart:** War es außergewöhnlicher Luxusverbrauch oder normale Lebenshaltung?
- **Zeitpunkt:** Lag Kenntnis des Rechtsgrundmangels oder Rechtshängigkeit bereits vor?
- **Sonderregime:** Ändert ein Vertrag, Rücktrittsrecht, Widerrufsrecht, EBV oder Deliktsrecht die Risikozuweisung?

Bei nichtigen gegenseitigen Verträgen nicht isoliert nur § 818 Abs. 3 prüfen, sondern zuerst die Saldierung der beiderseitigen Leistungen aufbauen.

## Entreicherungsatlas

| Wegfalltyp | Regelmäßige Einordnung | Belegbedarf |
|---|---|---|
| Verbrauch für zusätzliche Luxusausgabe | eher beachtlicher Wegfall | Anlass, Zeitpunkt, ohne Bereicherung unterblieben |
| Tilgung eigener Schuld | regelmäßig fortwirkende Bereicherung | getilgte Forderung, Kontoauszug |
| gewöhnliche Lebenshaltung | nur bei konkreter Mehr-Ausgabe beachtlich | Haushalts-/Kontobelege |
| Schenkung an Dritte | eigenes Weitergaberisiko oder § 822 BGB prüfen | Empfänger, Rechtsgrund, Unentgeltlichkeit |
| Verlust/Untergang ohne Ersatz | möglich beachtlich | Ursache, Versicherung, Verschulden, Zeitpunkt |
| Verkauf des Erlangten | keine Entreicherung, sondern Surrogat | Erlös, Kaufvertrag |
| Spekulation/Investition | meist eigenes Vermögensrisiko | Anlageentscheidung, Kenntnisstand |
| Verrechnung mit eigener Forderung | Ersparnis oder Befreiung prüfen | Verrechnungsabrede |
| Verbrauch nach Kenntnis | regelmäßig keine Berufung auf § 818 Abs. 3 | Kenntniszeitpunkt |

## Ausschluss der Entreicherungseinrede

§ 818 Abs. 3 BGB greift nicht bei:
- Bösgläubigkeit (§ 819 Abs. 1 BGB).
- Rechtshängigkeit (§ 818 Abs. 4 BGB i.V.m. § 292 BGB).
- Konstellationen, in denen der Wegfall als eigenes Risiko des Empfängers oder nach verschärfter Haftung zuzurechnen ist.

## Prüfschema

1. Was genau wurde erlangt?
2. Herausgabe in Natur möglich?
3. Nutzungen und Surrogate (§ 818 Abs. 1)?
4. Ersparnisse eigener Aufwendungen?
5. Noch bereichert (§ 818 Abs. 3)?
6. Ist der Wegfall dem Empfänger zurechenbar?
7. Bösgläubigkeit oder Rechtshängigkeit (Ausschluss § 818 Abs. 3)?

## Output-Template

**Prüfung §§ 818–819 BGB — Umfang der Herausgabe**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Erlangtes (Naturalrestitution möglich) | ja: [...] / nein → Wertersatz |
| Nutzungen gezogen | ja: [...] EUR / nein |
| Surrogate erlangt | ja: [...] / nein |
| ersparte Aufwendungen | ja: [...] EUR / nein |
| Wegfall zurechenbar? | ja / nein: [...] |
| Entreicherung (§ 818 Abs. 3) | ja: [...] verbraucht / nein: Ersparnis |
| Wegfalltyp | Luxus / Schuldtilgung / Lebenshaltung / Verlust / Weitergabe / Investition |
| Bösgläubigkeit (§ 819 Abs. 1) | ja ab [...] / nein |
| Rechtshängigkeit (§ 818 Abs. 4) | seit [...] |

**Ergebnis:** Bereicherungsanspruch in Höhe von [...] EUR. [Herausgabe in Natur / Wertersatz]. Entreicherungseinrede [greift / greift nicht].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 4. `verfuegung-eines-nichtberechtigten-816-bgb`

**Fokus:** Bereicherungsanspruch des Berechtigten nach § 816 BGB gegen verfügenden Nichtberechtigten prüfen. Normen: § 816 BGB. Prüfraster: wirksame Verfügung durch Gutglaubenserwerb oder Genehmigung, entgeltlich vs. unentgeltlich, Anspruch auf Erlangtes. Output: Prüfergebnis Anspruch § 816 BGB. Abgrenzung: nicht § 822 BGB (unentgeltliche Weitergabe).

# Verfügung eines Nichtberechtigten — § 816 BGB

## Triage — kläre vor der Prüfung

1. Hat ein Nichtberechtigter über einen fremden Gegenstand verfügt (Veräußerung, Übereignung, Belastung)?
2. Ist die Verfügung dem wahren Berechtigten gegenüber wirksam (Gutglaubenserwerb §§ 932 ff. BGB oder Genehmigung des Berechtigten)?
3. War die Verfügung entgeltlich (§ 816 Abs. 1 S. 1 BGB) oder unentgeltlich (§ 816 Abs. 1 S. 2 BGB)?
4. Kommt § 816 Abs. 2 BGB in Betracht (Leistung an einen Nichtberechtigten durch Dritten)?
5. Konkurriert § 816 BGB mit § 822 BGB oder § 812 BGB?

## Zentrale Normen

§ 816 Abs. 1 S. 1 BGB (entgeltliche Verfügung Nichtberechtigter) — § 816 Abs. 1 S. 2 BGB (unentgeltliche Verfügung) — § 816 Abs. 2 BGB (Leistung an Nichtberechtigten) — §§ 932 ff. BGB (gutgläubiger Erwerb) — § 822 BGB (Bereicherung Dritter) — § 812 BGB (Leistungskondiktion, subsidiär) — § 818 BGB (Umfang Herausgabe)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

§ 816 BGB schließt eine Lücke: Wenn ein Nichtberechtigter wirksam über einen Gegenstand verfügt, verliert der wahre Berechtigte sein Recht. § 816 BGB gibt ihm einen Ausgleichsanspruch gegen den Verfügenden.

## § 816 Abs. 1 S. 1 BGB — Entgeltliche Verfügung

**Tatbestand:**
1. Verfügung eines Nichtberechtigten.
2. Wirksamkeit gegenüber dem wahren Berechtigten (Gutglaubenserwerb, Genehmigung).
3. Entgeltliche Verfügung.

**Rechtsfolge:** Herausgabe der Gegenleistung (Erlös) an den wahren Berechtigten.

## § 816 Abs. 1 S. 2 BGB — Unentgeltliche Verfügung

**Tatbestand:** Verfügung ohne Gegenleistung.

**Rechtsfolge:** Direktanspruch des Berechtigten gegen den Dritten (Empfänger der unentgeltlichen Zuwendung).

## § 816 Abs. 2 BGB — Leistung an Nichtberechtigten

**Tatbestand:** Dritter leistet an Nichtberechtigten; Leistung ist dem Berechtigten gegenüber wirksam.

**Rechtsfolge:** Anspruch des Berechtigten gegen den Nichtberechtigten auf Herausgabe.

## Prüfschema

1. Wer ist der wahre Berechtigte?
2. Nichtberechtigte Verfügung?
3. Wirksam (Gutglaubenserwerb/Genehmigung)?
4. Entgeltlich oder unentgeltlich?
5. Was hat der Verfügende als Gegenleistung erhalten?

## Output-Template

**Prüfung § 816 BGB — Verfügung eines Nichtberechtigten**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Wahres Berechtigter | [...] |
| Nichtberechtigter Verfügender | [...] |
| Verfügung wirksam (Gutglauben/Genehmigung) | ja / nein → § 985 BGB statt § 816 |
| Entgeltlichkeit | ja → § 816 Abs. 1 S. 1 / nein → § 816 Abs. 1 S. 2 |
| Gegenleistung / Erlös | [...] EUR |
| § 816 Abs. 2 BGB einschlägig | ja / nein |

**Ergebnis:** Anspruch aus § 816 Abs. 1 S. [...] / Abs. 2 BGB auf [...] EUR gegen [...].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.
