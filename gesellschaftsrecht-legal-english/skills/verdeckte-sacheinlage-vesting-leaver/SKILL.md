---
name: verdeckte-sacheinlage-vesting-leaver
description: "Verdeckte Sacheinlage Vesting Leaver: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verdeckte Sacheinlage Vesting Leaver

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Verdeckte Sacheinlage Vesting Leaver** im Plugin Corporate law in legal English. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verdeckte-sacheinlage` | Erkennt und prueft verdeckte Sacheinlage und Hin-und-Her-Zahlung nach § 19 Abs. 4 und Abs. 5 GmbHG, einschließlich Anrechnungsloesung, Vorbelastungshaftung und der typischen M&A-Fallen bei Cash-Capitalization, Wandeldarlehen, Verrechnungsabreden und Gesellschafterdarlehen. |
| `vesting-leaver-cliff` | Erklaert Vesting, Cliff, Good Leaver, Bad Leaver, Founder Lock-up, Call Options, Einziehung und Rueckuebertragung im deutschen Gesellschaftsrecht. |

## Arbeitsweg

Im Plugin Corporate law in legal English gilt für **Verdeckte Sacheinlage Vesting Leaver**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verdeckte-sacheinlage`

**Fokus:** Erkennt und prueft verdeckte Sacheinlage und Hin-und-Her-Zahlung nach § 19 Abs. 4 und Abs. 5 GmbHG, einschließlich Anrechnungsloesung, Vorbelastungshaftung und der typischen M&A-Fallen bei Cash-Capitalization, Wandeldarlehen, Verrechnungsabreden und Gesellschafterdarlehen.

# Verdeckte Sacheinlage und Hin-und-Her-Zahlung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verdeckte Sacheinlage und Hin-und-Her-Zahlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Verdeckte Sacheinlage ist einer der am haeufigsten uebersehenen Basics im M&A- und Finanzierungs-Alltag. M&A-Anwaelte denken in Vertragsrecht, doch § 19 Abs. 4 GmbHG ist zwingendes Kapitalaufbringungsrecht und bricht jede schuldrechtliche Konstruktion. Wer das uebersieht, erzeugt Differenzhaftung (§ 9 Abs. 1 GmbHG analog ueber § 19 Abs. 4 Satz 3 GmbHG) und im Insolvenzfall ein erhebliches Haftungsrisiko fuer die Geschaeftsfuehrung.

## Kernregeln

1. **§ 19 Abs. 4 GmbHG (verdeckte Sacheinlage):** Wenn eine Bareinlage wirtschaftlich als Sacheinlage zu werten ist, befreit die Bareinlage nicht von der Einlagepflicht. Der Gesellschafter haftet weiter. Auf seine Einlagepflicht wird der Wert des verdeckt eingelegten Vermoegensgegenstandes im Zeitpunkt der Anmeldung bzw. seiner Ueberlassung angerechnet (Anrechnungsloesung seit MoMiG 2008).
2. **§ 19 Abs. 5 GmbHG (Hin-und-Her-Zahlung):** Wenn vor der Einlage eine Leistung an den Gesellschafter vereinbart ist, die wirtschaftlich einer Rueckzahlung der Einlage entspricht, befreit die Bareinlage nur, wenn die Leistung durch einen vollwertigen Rueckgewaehranspruch gedeckt ist, der jederzeit faellig gestellt werden kann oder durch fristlose Kuendigung faellig werden kann, und wenn dies in der Anmeldung offengelegt wird.
3. **Verbindung mit § 19 Abs. 2 GmbHG:** Aufrechnung gegen die Einlageforderung ist grundsaetzlich unzulaessig. Verrechnungs- und Aufrechnungsabreden im SPA oder SHA muessen daran gemessen werden.

## Pruefraster

1. Gibt es zwischen Gesellschaft und einlegendem Gesellschafter eine zeitlich, sachlich oder personell verknuepfte Leistung (Kauf, Darlehen, Beraterhonorar, Lizenz, Dienstleistung, Uebernahme von Verbindlichkeiten)?
2. Wird die Bareinlage wirtschaftlich gleich wieder an den Gesellschafter zurueckgefuehrt? Dann § 19 Abs. 5 GmbHG (Hin-und-Her-Zahlung).
3. Wird mit der Bareinlage ein Vermoegensgegenstand des Gesellschafters erworben? Dann § 19 Abs. 4 GmbHG (verdeckte Sacheinlage).
4. Anrechnungsloesung greifen lassen: Wert des Gegenstandes im Zeitpunkt der Anmeldung. Beweislast: Gesellschafter.
5. Bei Hin-und-Her-Zahlung: ist der Rueckgewaehranspruch vollwertig und jederzeit faellig stellbar? Offenlegung in der Anmeldung erfolgt?
6. Sind die Geschaeftsfuehrer ihrer Pflicht nach § 8 Abs. 2, § 9c GmbHG zur korrekten Anmeldung nachgekommen? Strafbarkeit nach § 82 GmbHG pruefen.

## Typische M&A- und Finanzierungs-Fallen

- **Cash-In-Series-A plus Akquisition aus Series-A-Mitteln:** Wenn die Mandantin mit dem Series-A-Cash unmittelbar Vermoegensgegenstaende eines Investors oder einer ihm nahestehenden Person erwirbt, ist die Naehe zur verdeckten Sacheinlage zu pruefen.
- **Wandeldarlehen, das im Zuge der Kapitalerhoehung zurueckgefuehrt und neu als Eigenkapital gezeichnet wird:** Klassische Hin-und-Her-Zahlung. Vollwertigkeit und Faelligstellbarkeit muessen sauber dokumentiert sein, sonst nur Anrechnungsloesung.
- **Verrechnungsabreden im SPA:** Aufrechnung gegen die Einlageforderung ist nach § 19 Abs. 2 GmbHG verboten; Verrechnungsklauseln im SPA muessen die Einlageforderung explizit aussparen.
- **Gesellschafterdarlehen als Quasi-Eigenkapital:** Auch nach Wegfall der Eigenkapitalersatzregeln bleiben die Kapitalaufbringungsregeln scharf, wenn aus dem Darlehen heraus eine Kapitalerhoehung gezeichnet wird.
- **Sale-and-lease-back kurz vor oder nach Closing:** Gegenstand bleibt wirtschaftlich beim Gesellschafter, Cash fliesst hin und zurueck. Genau pruefen.
- **Beraterhonorar an Investor:** Wenn das Investmentvehikel direkt nach Closing ein laufendes Beraterhonorar bekommt, das wirtschaftlich Teil des Investments ist, kann Hin-und-Her-Zahlung vorliegen.

## Antwortvorgaben

- Trennen: Was sagt der Vertrag (M&A-Sicht) versus was sagt das Kapitalaufbringungsrecht (Gesellschaftsrecht-Sicht).
- Immer die Rechtsfolgen aus § 19 Abs. 4 Satz 3 GmbHG benennen: Anrechnung des Wertes im Zeitpunkt der Anmeldung; Beweislast beim Gesellschafter; Differenzhaftung bleibt.
- Auf § 9c GmbHG verweisen, wenn die Anmeldung Falschangaben enthielte.
- Konkrete Heilung anbieten: Offenlegung in der Anmeldung, Wertgutachten, Sachgruendungsbericht, ggf. echte Sachkapitalerhoehung mit ordnungsgemaesser Werthaltigkeitspruefung.
- Verweis auf die in der Akte typisch verlinkten Skills: `cap-table-gesellschafterliste`, `financing-convertible-loan-safe`, `articles-association-satzung`.

## Quellen

- BGH, Urt. v. 16.03.1998 - II ZR 303/96 (Lufttaxi), grundlegend zur verdeckten Sacheinlage vor MoMiG; weiterhin als Auslegungshintergrund relevant.
- BGH, Urt. v. 06.12.2011 - II ZR 149/10 zur Anrechnungsloesung nach MoMiG.
- BGH, Urt. v. 20.07.2009 - II ZR 273/07 (Cash-Pool) zur Hin-und-Her-Zahlung.
- Begruendung MoMiG, BT-Drucksache 16/6140, zu § 19 Abs. 4 und Abs. 5 GmbHG.
- § 19 GmbHG, § 9 GmbHG, § 9c GmbHG, § 82 GmbHG.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `vesting-leaver-cliff`

**Fokus:** Erklaert Vesting, Cliff, Good Leaver, Bad Leaver, Founder Lock-up, Call Options, Einziehung und Rueckuebertragung im deutschen Gesellschaftsrecht.

# Vesting, Leaver und Cliff

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vesting, Leaver und Cliff` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Ziel

Vesting ist in deutschen Startups häufig keine echte Entstehung von Anteilen, sondern eine vertragliche Rückerwerbs- oder Sanktionsmechanik für Gründeranteile.

## Prüffragen

1. Echte Anteile oder virtuelle Beteiligung?
2. Monatliches Vesting, Jahresvesting oder Meilensteine?
3. Cliff: Wann beginnt die Unverfallbarkeit?
4. Good Leaver, Bad Leaver, Grey Leaver definiert?
5. Rückkaufpreis: Nominalwert, Fair Market Value, Discount?
6. Umsetzung: Call Option, Abtretungspflicht, Einziehung, Vollmacht?

## Risiko

- Überharte Bad-Leaver-Regeln.
- Unklare Kündigungsgründe.
- Fehlende notarielle Struktur bei Geschäftsanteilen.
- Steuer- und Arbeitsrechtsfragen ausgeblendet.
- Satzung und SHA widersprechen sich.

## Output

- Leaver-Matrix.
- Timeline.
- Formulierungs- und Rückfragenliste.
- Senior-Review-Gate.

## Didaktischer Arbeitsmodus

- Erklaere jeden Begriff zweispurig: englischer Praxisbegriff, naheliegende deutsche Entsprechung und warum beides nicht deckungsgleich sein muss.
- Arbeite immer an der Dokumentstelle: Term Sheet, SHA, SPA, Satzung, Gesellschafterliste, Cap Table, Board Paper oder Closing Checklist.
- Gib eine Anfängerfassung in klarer Sprache und eine Praxisfassung fuer die Partnerin oder den Mandanten.
- Wenn ein common-law-Begriff nach deutschem Recht verwendet wird, markiere Auslegungsrisiko, deutsches Ersatzkonzept und Formulierungsvorschlag.

## Ausgabeformat

1. Kurzantwort.
2. Begriff entschluesselt.
3. Deutsche Rechtsfunktion.
4. Wirtschaftlicher Effekt.
5. Typische Fallen.
6. Naechster Drafting- oder Review-Schritt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
