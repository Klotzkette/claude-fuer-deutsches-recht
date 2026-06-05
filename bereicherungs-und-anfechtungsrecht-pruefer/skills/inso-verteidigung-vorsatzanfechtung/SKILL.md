---
name: inso-verteidigung-vorsatzanfechtung
description: "Inso Verteidigung Vorsatzanfechtung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inso Verteidigung Vorsatzanfechtung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Inso Verteidigung Vorsatzanfechtung** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `inso-verteidigung-anfechtungsgegner` | Verteidigung des Anfechtungsgegners gegen Insolvenzanfechtung nach §§ 129-147 InsO strukturieren. Prüft fehlende Rechtshandlung oder Gläubigerbenachteiligung, Fristen, Kenntnis, § 133-Vermutungen, Bargeschäft § 142, Gegenleistung § 144, Verjährung § 146 und Vergleichsstrategie. Output: Abwehrmatrix und Schriftsatzgerüst. |
| `inso-vorsatzanfechtung-133` | Vorsatzanfechtung nach § 133 InsO prüfen: Benachteiligungsvorsatz, Kenntnis, Vermutungsregel, Deckungshandlungen mit Vier-Jahres-Frist, kongruente Deckung mit Zahlungsunfähigkeit, Zahlungserleichterungs-Vermutung, nahestehende Personen und Bargeschäft § 142. Output: Indizienmatrix mit Human-Review-Pflicht. |
| `insolvenzrisiko-im-dreipersonenverhaeltnis` | Dieses Fachmodul greift, wenn ein Direktanspruch im Dreieck faktisch ein Insolvenzrisiko verlagern würde. Normen: §§ 812 und 818 BGB; §§ 129 ff. InsO. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Risiko-Analyse Direktanspruch mit Insolvenzfolgen-Bewertung. Abgrenzung: nicht Insolvenzanfechtung §§ 129 ff. InsO. |
| `ip-lizenzanalogie-und-bereicherung` | Dieses Fachmodul greift, wenn ersparte Lizenz und Schutzrechtsnutzung bereicherungsrechtlich bewertet werden. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB; § 97 UrhG; § 14 MarkenG; § 139 PatG. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt; Bestimme den Zuweisungsgehalt der verletzten Position; Ordne Nutzung, Verfügung oder Weitergabe der passenden Anspruchsgrundlage zu. Output: Lizenzanalogie-Berechnung mit Wertbestimmung und Verschuldensunabhängigkeit. Abgrenzung: nicht Schadensersatz nach Lizenzanalogie. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Inso Verteidigung Vorsatzanfechtung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `inso-verteidigung-anfechtungsgegner`

**Fokus:** Verteidigung des Anfechtungsgegners gegen Insolvenzanfechtung nach §§ 129-147 InsO strukturieren. Prüft fehlende Rechtshandlung oder Gläubigerbenachteiligung, Fristen, Kenntnis, § 133-Vermutungen, Bargeschäft § 142, Gegenleistung § 144, Verjährung § 146 und Vergleichsstrategie. Output: Abwehrmatrix und Schriftsatzgerüst.

# Verteidigung des Anfechtungsgegners — §§ 129 ff. InsO

## Aufgabe

Dieser Skill baut die Gegenwehr gegen ein Anfechtungsschreiben oder eine Anfechtungsklage auf. Er prüft nicht aus Verwaltersicht, was maximal denkbar ist, sondern aus Sicht des Empfängers: Welche Tatbestandsmerkmale sind nicht substantiiert, welche Einreden und Gegenargumente sind tragfähig, und welche Unterlagen müssen sofort gesichert werden?

## Sofortfragen

1. Welche konkrete Rechtshandlung wird angefochten: Zahlung, Sicherheit, Verrechnung, Aufrechnung, Verzicht, Drittzahlung?
2. Auf welche Norm stützt sich der Verwalter: § 130, § 131, § 133, § 134, § 135 oder nur pauschal §§ 129 ff. InsO?
3. Welche Daten sind sicher: Insolvenzantrag, Eröffnung, Rechtshandlung, Rechnung, Fälligkeit, Leistung?
4. Welche Kenntnis wird behauptet und durch welche Belege?
5. Gab es Gegenleistung, Bargeschäft, laufende Geschäftsbeziehung oder Sanierungsinformationen?
6. Droht Verjährung nur als Argument oder ist bereits Klage erhoben?

## Verteidigungsmatrix

| Angriff | Verteidigung |
|---|---|
| § 129 InsO | keine Rechtshandlung, kein Vermögensabfluss, keine objektive Gläubigerbenachteiligung, falscher Zeitpunkt nach § 140 InsO |
| § 130 InsO | keine kongruente Deckung, keine Zahlungsunfähigkeit zum Zeitpunkt, keine Kenntnis oder keine zwingenden Umstände |
| § 131 InsO | Leistung war kongruent, Frist nicht getroffen, im zweiten oder dritten Monat keine Zusatzvoraussetzung |
| § 133 InsO | kein Benachteiligungsvorsatz, keine Kenntnis, Vermutung widerlegt, Sanierungs- oder Vollbefriedigungsperspektive |
| § 134 InsO | nicht unentgeltlich, objektive Gegenleistung, Gelegenheitsgeschenk geringen Werts, Entreicherung nach § 143 Abs. 2 |
| § 135 InsO | keine Gesellschafterrolle, keine wirtschaftliche Gleichstellung, Frist verfehlt, § 39 Abs. 4 oder 5 InsO |
| § 142 InsO | gleichwertiger unmittelbarer Austausch; bei § 133 zusätzlich keine Kenntnis unlauteren Handelns |
| §§ 143-146 InsO | Betrag falsch, Gegenleistung § 144, Zinsen erst bei Verzug oder § 291 BGB, Verjährung |

## § 133 InsO — besondere Vorsicht

Die Verteidigung muss Indizien zerlegen, nicht nur bestreiten.

| Behauptung Verwalter | Gegenprüfung |
|---|---|
| Zahlungsunfähigkeit war bekannt | Welche konkrete Information hatte der Empfänger wirklich? Mahnungen allein genügen nicht automatisch. |
| Ratenzahlung beweist Kenntnis | § 133 Abs. 3 S. 2 InsO enthält bei Zahlungsvereinbarung oder Zahlungserleichterung eine Vermutung gegen Kenntnis der Zahlungsunfähigkeit. |
| Sanierung war aussichtslos | Gibt es ein Sanierungskonzept, Beraterkorrespondenz, Finanzierungszusage oder Vollbefriedigungsperspektive? |
| Liquiditätsstatus beweist Zahlungsunfähigkeit | Ist der Liquiditätsstatus einzelfallbezogen substantiiert und belegt? |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Bargeschäft § 142 InsO

Prüfe:

1. Gleichwertigkeit der Gegenleistung.
2. unmittelbarer Austausch nach Art der Leistungen und Gepflogenheiten des Geschäftsverkehrs.
3. Bei Arbeitsentgelt: Drei-Monats-Regel aus § 142 Abs. 2 InsO beachten.
4. Bei § 133 InsO: Das Bargeschäft schützt nur, wenn zusätzlich keine erkannte Unlauterkeit des Schuldners vorliegt.

Keine pauschale 30-Tage-Regel verwenden; der zeitliche Zusammenhang ist geschäftsbezogen zu begründen.

## Verjährung und Zinsen

§ 146 InsO verweist auf die regelmäßige Verjährung nach BGB. Der Verwalter muss seine Kenntnis- und Ermittlungslage offenlegen, wenn Verjährung streitig wird.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Zinsen: Nach § 143 Abs. 1 S. 3 InsO ist eine Geldschuld nur bei Verzug oder nach § 291 BGB zu verzinsen; Nutzungsherausgabe darüber hinaus ist ausgeschlossen.

## Output-Template

**Abwehrmatrix Insolvenzanfechtung**

| Punkt | Stand |
|---|---|
| Angegriffene Handlung | [...] |
| Norm des Verwalters | [...] |
| stärkstes Gegenargument | [...] |
| fehlende Belege | [...] |
| Vergleichskorridor | [...] |
| Human-Review-Punkt | [...] |

**Schriftsatzgerüst**

1. Sachverhalt je Rechtshandlung trennen.
2. Anfechtungstatbestand bestreiten.
3. Hilfsweise § 142 InsO und § 144 InsO darstellen.
4. Hilfsweise Betrag, Zinsen und Verjährung bestreiten.
5. Vergleichsvorschlag nur bei wirtschaftlich sinnvoller Quote.

---

Hinweis: Keine Rechtsberatung. Verteidigung nie pauschal führen; jeder Zahlungsvorgang braucht eigene Norm, eigene Frist und eigene Beleglage.

## 2. `inso-vorsatzanfechtung-133`

**Fokus:** Vorsatzanfechtung nach § 133 InsO prüfen: Benachteiligungsvorsatz, Kenntnis, Vermutungsregel, Deckungshandlungen mit Vier-Jahres-Frist, kongruente Deckung mit Zahlungsunfähigkeit, Zahlungserleichterungs-Vermutung, nahestehende Personen und Bargeschäft § 142. Output: Indizienmatrix mit Human-Review-Pflicht.

# Vorsatzanfechtung — § 133 InsO

## Triage — kläre vor der Prüfung

1. Welche Rechtshandlung soll angefochten werden, und wann wurde sie nach § 140 InsO vorgenommen?
2. Handelt es sich um eine Deckungshandlung, also Sicherung oder Befriedigung eines Anspruchs?
3. Welche Tatsachen belegen den Benachteiligungsvorsatz des Schuldners?
4. Welche Tatsachen belegen die Kenntnis des Anfechtungsgegners?
5. Greift die Vermutung des § 133 Abs. 1 S. 2 InsO?
6. Greift bei kongruenter Deckung § 133 Abs. 3 InsO?
7. Wurde eine Zahlungsvereinbarung oder Zahlungserleichterung gewährt?
8. Liegt ein Bargeschäft nach § 142 InsO vor und hat der andere Teil unlauteres Handeln erkannt?

## Zentrale Normen

§ 133 InsO — § 129 InsO — § 130 InsO — § 131 InsO — § 138 InsO — § 140 InsO — § 142 InsO — § 143 InsO — § 17 InsO — § 18 InsO.

## Gesetzliche Struktur

| Norm | Inhalt | Zeitraum |
|---|---|---|
| § 133 Abs. 1 InsO | vorsätzliche Benachteiligung mit Kenntnis des anderen Teils | zehn Jahre vor Antrag oder nach Antrag |
| § 133 Abs. 2 InsO | Sicherung oder Befriedigung des anderen Teils | vier Jahre statt zehn Jahre |
| § 133 Abs. 3 S. 1 InsO | bei kongruenter Deckung tritt eingetretene Zahlungsunfähigkeit an die Stelle drohender Zahlungsunfähigkeit | nur bei Deckung |
| § 133 Abs. 3 S. 2 InsO | Zahlungsvereinbarung oder Zahlungserleichterung begründet Vermutung gegen Kenntnis der Zahlungsunfähigkeit | entlastender Anknüpfungspunkt |
| § 133 Abs. 4 InsO | entgeltlicher Vertrag mit nahestehender Person bei unmittelbarer Benachteiligung | ausgeschlossen, wenn früher als zwei Jahre vor Antrag |

Wichtig: Die Vier-Jahres-Frist des § 133 Abs. 2 InsO gilt für Deckungshandlungen, nicht nur für nahestehende Personen. Nahestehende Personen sind in § 133 Abs. 4 InsO gesondert geregelt.

## Rechtsprechungsleitlinien BGH IX. ZS (offene Quellen)

- BGH, Urt. v. 06.05.2021 – Az. IX ZR 72/20 — Neuausrichtung der Vorsatzanfechtung; alleinige Kenntnis der Zahlungsunfaehigkeit traegt den Benachteiligungsvorsatz nicht mehr schematisch; massgeblich ist Wissen oder Inkaufnahme, dass kuenftige Glaeubiger nicht voll befriedigt werden. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=06.05.2021&Aktenzeichen=IX+ZR+72/20
- BGH, Urt. v. 18.04.2024 – Az. IX ZR 129/22 — Weiterentwicklung der Linie zu § 133 InsO bei kongruenter Deckung; Verwalter traegt Darlegungslast hinsichtlich Deckungsluecke und prognostischer Befriedigungsaussicht; einfaches Bestreiten kann genuegen. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129%2F22
- BGH, Urt. v. 18.04.2024 – Az. IX ZR 239/22 — Parallelentscheidung zur Anfechtung wegen gesellschafteraehnlicher Stellung (§ 135 InsO i.V.m. § 133 InsO). Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22
- Weiterfuehrende Rechtsprechungsdurchsicht: https://www.bundesgerichtshof.de und https://openjur.de.

## § 133 als Human-Review-Norm

§ 133 InsO enthält innere Tatsachen und Gesamtwürdigung. Die KI darf hier eine Indizienmatrix bauen, aber nicht ohne fachliche Prüfung "Vorsatz bewiesen" schreiben.

| Indiz | Belastet | Entlastet |
|---|---|---|
| erkannte Zahlungsunfähigkeit | kann Vorsatz und Kenntnis stützen | genügt nach neuerer BGH-Linie nicht schematisch allein |
| inkongruente Deckung | starkes Indiz | Einzelfall und Gegenindizien prüfen |
| Zahlungsvereinbarung | kann Krise zeigen | § 133 Abs. 3 S. 2 InsO vermutet fehlende Kenntnis der Zahlungsunfähigkeit |
| Sanierungsversuch | nur belastend, wenn erkennbar untauglich | tragfähiges Konzept kann Vorsatz entkräften |
| Vollbefriedigungsperspektive | entlastend | nur mit belastbaren Informationen |

## Bargeschäft bei § 133

§ 142 Abs. 1 InsO lässt ein Bargeschäft nur anfechten, wenn die Voraussetzungen des § 133 Abs. 1 bis 3 InsO vorliegen **und** der andere Teil erkannt hat, dass der Schuldner unlauter handelte. Deshalb muss bei Bargeschäften ein eigener Unlauterkeits- und Kenntnisblock ausgefüllt werden.

## Prüfschema

1. § 129 InsO: Rechtshandlung, Gläubigerbenachteiligung, Anfechtungsbefugnis.
2. § 133 Abs. 1: Benachteiligungsvorsatz des Schuldners.
3. Kenntnis des anderen Teils oder Vermutung nach § 133 Abs. 1 S. 2.
4. Bei Deckung: Zeitraum auf vier Jahre begrenzen.
5. Bei kongruenter Deckung: § 133 Abs. 3 prüfen.
6. Zahlungserleichterung: Vermutung fehlender Kenntnis der Zahlungsunfähigkeit prüfen.
7. Nahestehende Person und § 133 Abs. 4 gesondert prüfen.
8. Bargeschäft und Unlauterkeit nach § 142 InsO prüfen.

## Output-Template

**Prüfung § 133 InsO — Vorsatzanfechtung**

| Merkmal | Ergebnis | Beleg |
|---|---|---|
| Rechtshandlung und Zeitpunkt | [...] | [...] |
| Deckungshandlung | ja/nein | [...] |
| maßgeblicher Zeitraum | zehn Jahre/vier Jahre/zwei Jahre | [...] |
| Benachteiligungsvorsatz | belegt/offen/nicht belegt | [...] |
| Kenntnis des anderen Teils | belegt/vermutet/widerlegt/offen | [...] |
| § 133 Abs. 3 | greift/greift nicht | [...] |
| Zahlungsvereinbarung | ja/nein | [...] |
| Bargeschäft und Unlauterkeit | ja/nein/offen | [...] |

**Ergebnis:** § 133 InsO [nicht tragfähig / nur Prüfspur / tragfähig nach Human Review].

---

Hinweis: Keine Rechtsberatung. § 133 InsO ist keine reine Mustererkennung; jede KI-Ausgabe muss die Indizien und Gegenindizien sichtbar machen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `insolvenzrisiko-im-dreipersonenverhaeltnis`

**Fokus:** Dieses Fachmodul greift, wenn ein Direktanspruch im Dreieck faktisch ein Insolvenzrisiko verlagern würde. Normen: §§ 812 und 818 BGB; §§ 129 ff. InsO. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Risiko-Analyse Direktanspruch mit Insolvenzfolgen-Bewertung. Abgrenzung: nicht Insolvenzanfechtung §§ 129 ff. InsO.

# Insolvenzrisiko im Dreipersonenverhältnis

## Einsatzbereich

Dieses Fachmodul greift, wenn ein Direktanspruch im Dreieck faktisch ein Insolvenzrisiko verlagern würde. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

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

## Insolvenzrisiko ist kein Tatbestandsmerkmal

Die Zahlungsunfähigkeit einer Zwischenperson macht den Endempfänger nicht automatisch zum Bereicherungsschuldner. Frage stattdessen:

- Hatte der Zahlende bewusst das Bonitätsrisiko des Mittlers übernommen?
- Hat der Endempfänger eine ihm zustehende Forderung gutgläubig erfüllt bekommen?
- Lag der Fehler in der Sphäre des Zahlenden, des Mittlers, des Empfängers oder einer Bank?
- Würde ein Direktanspruch die gewählte Leistungsstruktur nachträglich umschreiben?
- Gibt es besondere Umstände, die den Empfängerschutz entfallen lassen?

Ein Direktanspruch ist nur tragfähig, wenn die Leistungszurechnung selbst fehlerhaft ist oder der Empfänger keinen anerkennenswerten Behaltensgrund hat.

## Typische Fehler

- Tatsächlichen Empfänger automatisch als Schuldner behandeln.
- Doppelmangel zu einem Pauschalanspruch verschmelzen.
- Insolvenzrisiko ohne Rechtsgrund verlagern.

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

## Risikozuweisungs-Output

| Risiko | Träger nach normaler Leistungsbeziehung | Korrekturgrund? |
|---|---|---|
| Insolvenz des Mittlers | [...] | ja / nein |
| Fehlerhafte Anweisung | [...] | ja / nein |
| Fehlender Valutagrund | [...] | ja / nein |
| Empfängervertrauen | geschützt / nicht geschützt | [...] |

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

## 4. `ip-lizenzanalogie-und-bereicherung`

**Fokus:** Dieses Fachmodul greift, wenn ersparte Lizenz und Schutzrechtsnutzung bereicherungsrechtlich bewertet werden. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB; § 97 UrhG; § 14 MarkenG; § 139 PatG. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt; Bestimme den Zuweisungsgehalt der verletzten Position; Ordne Nutzung, Verfügung oder Weitergabe der passenden Anspruchsgrundlage zu. Output: Lizenzanalogie-Berechnung mit Wertbestimmung und Verschuldensunabhängigkeit. Abgrenzung: nicht Schadensersatz nach Lizenzanalogie.

# IP-Lizenzanalogie und Bereicherung

## Einsatzbereich

Dieses Fachmodul greift, wenn ersparte Lizenz und Schutzrechtsnutzung bereicherungsrechtlich bewertet werden. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welche Rechtsposition weist den wirtschaftlichen Nutzen zu?
2. Hat der Gegner diese Position ohne Leistung des Anspruchstellers genutzt?
3. Gab es Lizenz, Gestattung oder gesetzliche Erlaubnis?
4. Ist § 816 BGB oder § 822 BGB spezieller?
5. Wie wird der objektive Nutzungs- oder Lizenzwert bestimmt?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt.
- Bestimme den Zuweisungsgehalt der verletzten Position.
- Ordne Nutzung, Verfügung oder Weitergabe der passenden Anspruchsgrundlage zu.
- Bewerte nach objektivem Markt-, Lizenz- oder Erlöswert.
- Trenne Bereicherung von Schaden, Gewinnabschöpfung und Unterlassung.

## Typische Fehler

- Alt. 2 als Auffangtatbestand ohne Zuweisungsgehalt nutzen.
- Schadensersatz und Bereicherung vermischen.
- Lizenzwert ohne Methode schätzen.

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
