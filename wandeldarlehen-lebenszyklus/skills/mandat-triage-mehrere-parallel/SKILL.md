---
name: mandat-triage-mehrere-parallel
description: "Mandat Triage Mehrere Parallel: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandat Triage Mehrere Parallel

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Mandat Triage Mehrere Parallel** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mandat-triage-wandeldarlehen` | Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Vertragstyp SAFE Convertible Note Laufzeit Wandlungsereignisse offene Punkte. Output: Mandatssteckbrief Routen-Empfehlung Datenliste. Abgrenzung: Triage und Einstieg; Detailarbeit in Spezialist-Skills. |
| `mehrere-wandeldarlehen-parallel` | Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren und Konflikte erkennen. §§ 488 ff. BGB § 39 InsO Rangrücktritt. Prüfraster: Pari-passu-Stellung Rangregelungen Wandlungsrechte Verwasserungsschutz Vesting. Output: Übersichtsmatrix Konfliktliste Handlungsempfehlung. Abgrenzung: nicht für Einzeldarlehen-Erstellung. |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Mandat Triage Mehrere Parallel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mandat-triage-wandeldarlehen`

**Fokus:** Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Vertragstyp SAFE Convertible Note Laufzeit Wandlungsereignisse offene Punkte. Output: Mandatssteckbrief Routen-Empfehlung Datenliste. Abgrenzung: Triage und Einstieg; Detailarbeit in Spezialist-Skills.

# Mandat-Triage Wandeldarlehen – Erstgespräch

## Zweck

Dieser Skill strukturiert das erste Gespräch mit dem Mandanten über ein beabsichtigtes Wandeldarlehen. Er klärt die wesentlichen Rahmenbedingungen (Rechtsform, Parteien, Konditionen, Wandelereignisse, Formalien), erstellt einen Mandatssteckbrief und empfiehlt den nächsten Workflow-Schritt. Phase A des Lebenszyklus.

## Eingaben

- Rechtsform der Gesellschaft: GmbH oder UG (haftungsbeschränkt)
- Firmenname, HRB-Nummer, Amtsgericht, Sitz
- Namen und Rollen der Gesellschafterinnen (Anzahl, Anteile)
- Name und Rechtsform des Darlehensgebers (Privatperson oder juristische Person)
- Beabsichtigter Darlehensbetrag (EUR) und Laufzeit
- Zinssatz (Standard fünf Prozent p.a.)
- Gewünschte Wandelereignisse (Qualified Financing, Exit, Maturity)
- Sprachen-Stack: bilingual DE/EN oder nur DE
- Vorhandener Gesellschafterbeschluss zur grundsätzlichen Kapitalerhöhungsbereitschaft: ja/nein
- Zeitdruck / gewünschtes Unterzeichnungsdatum

## Rechtlicher Rahmen

### Primärnormen
- § 488 BGB (Darlehensvertrag)
- § 1 GmbHG (Rechtsform GmbH), § 5a GmbHG (UG haftungsbeschränkt)
- § 15 Abs. 3, Abs. 4 GmbHG (Anteilsübertragung, Form)
- § 55 ff. GmbHG (Kapitalerhöhung)
- § 126b BGB (Textform)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Rechtsform und Register prüfen
Klären: GmbH oder UG? Bei UG Mindestkapital EUR 1 (§ 5a GmbHG), Thesaurierungspflicht (§ 5a Abs. 3 GmbHG) ansprechen. HRB und Amtsgericht notieren.

### 2. Parteien und Vertretungsmacht erfassen
Gesellschaft: Geschäftsführung alleinvertretungsberechtigt oder Gesamtvertretung? Gesellschafterinnen: Zahl, Anteilsverhältnis, Privatpersonen oder juristische Personen? Darlehensgeber: Privatperson oder GmbH/KG – wer vertritt?

### 3. Wandelereignisse klären
Qualifizierte Finanzierungsrunde: Schwellenwerte Bewertung und Investitionsvolumen bereits bekannt? Exit-Trigger (Share Deal >50%, Asset Deal, IPO, Fusion)? Maturity mit Fall-back-Bewertung: Betrag schon vorstellbar?

### 4. Formfragen vorab
Sprachen-Stack: bilingual oder nur DE? DocuSign-Unterzeichnung akzeptiert? Notarielle Beurkundung gewünscht oder nur Textform?

### 5. Mandatssteckbrief erstellen
Strukturierte Zusammenfassung aller erfassten Punkte; offene Lücken markieren; Skill-Empfehlung ausgeben.

### 6. Nächsten Skill empfehlen
Empfehlung: `parteien-erfassen` für vollständige KYC-Daten, dann `darlehenshoehe-konditionen`.

## Beispiel-Mandatssteckbrief

| Feld | Inhalt |
|---|---|
| Gesellschaft | Sonnenglas Solartechnologie UG (haftungsbeschränkt), HRB 123456, AG Berlin |
| Stammkapital | EUR 1000, 100 Anteile à EUR 1 Nennwert |
| Gesellschafterinnen | Dr. Mira Schöneck 40 Anteile, Lina Habersaat 35 Anteile, Treasury 25 Anteile |
| Darlehensgeber | Northstar Pre-Seed Partners GmbH & Co. KG |
| Betrag | EUR 250000 |
| Laufzeit | 2 Jahre feste Laufzeit |
| Zinssatz | fünf Prozent p.a. (act/360) |
| Cap | EUR 4000000 Pre-Money |
| Discount | zwanzig Prozent |
| Sprache | bilingual DE/EN |
| Unterzeichnung | DocuSign (Textform § 126b BGB) |
| Gesellschafterbeschluss | noch nicht gefasst |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Wandelereignis schon eingetreten | Nachträgliche Vereinbarung problematisch | Wandelereignis kurz bevorstehend | Wandelereignis weit in Zukunft |
| Keine Fall-back-Bewertung vereinbart | Maturity-Wandlung unklar | Bewertung grob geschätzt | Bewertung durch TS belegt |
| Gesellschafterbeschluss fehlt | Mitwirkungspflicht § 5 ungesichert | Beschluss in Planung | Beschluss liegt vor |
| Mehrere parallele Wandeldarlehen | MFN und Stack unklar | Nur ein weiteres WD | Keine weiteren WD |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/parteien-erfassen/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/darlehenshoehe-konditionen/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungsmechanik-konzipieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/beurkundungserfordernis-pruefung/SKILL.md`

## Quellen und Updates

Stand: 05/2026.
- GmbHG: https://www.gesetze-im-internet.de/gmbhg/
- §§ 488 ff. BGB (Darlehen): https://www.gesetze-im-internet.de/bgb/__488.html
- § 55 GmbHG (Kapitalerhoehungsbeschluss): https://www.gesetze-im-internet.de/gmbhg/__55.html
- § 56 GmbHG (Sacheinlage): https://www.gesetze-im-internet.de/gmbhg/__56.html
- § 39 InsO (Nachraenge): https://www.gesetze-im-internet.de/inso/__39.html
- §§ 135, 143 InsO (Gesellschafterdarlehen, Anfechtung): https://www.gesetze-im-internet.de/inso/__135.html
- § 15a InsO (Insolvenzantragspflicht): https://www.gesetze-im-internet.de/inso/__15a.html
- § 19 IV GmbHG (Erleichterung Aufrechnung Stammeinlage gegen Gesellschafterforderung — Hinweis: § 19 IV GmbHG i.d.F. MoMiG 2008 weiterhin maßgeblich; DiRUG/DiREG haben Form (Online-Beurkundung) modifiziert, materielle Aufrechnungsregel unveraendert): https://www.gesetze-im-internet.de/gmbhg/__19.html
- DiRUG (BGBl. I 2021, 3338; in Kraft Bargruendung 01.08.2022): https://www.gesetze-im-internet.de/beurkg/__16a.html
- DiREG (in Kraft 01.08.2023; Online-Beurkundung Kapitalerhoehung/Satzungsaenderung bei einstimmigem Beschluss): https://www.bmjv.de/SharedDocs/Pressemitteilungen/DE/2022/0729_DIREG_DIRUG.html
- StaRUG (SanInsFoG, BGBl. I 2020, 3256; in Kraft 01.01.2021): https://www.gesetze-im-internet.de/starug/
- § 15b InsO (rechtsformneutrales Zahlungsverbot): https://www.gesetze-im-internet.de/inso/__15b.html
- Bei Aenderung GmbHG/UmwStG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 488 ff. BGB (Darlehen) → §§ 55, 56 GmbHG (Kapitalerhöhung, Sacheinlage) → § 39 InsO (Nachrangige Forderungen, Gesellschafterdarlehen) → §§ 135, 143 InsO (Anfechtung, Rückzahlung) → § 40 GmbHG (Gesellschafterliste) → § 15a InsO (Insolvenzantragspflicht)

## 2. `mehrere-wandeldarlehen-parallel`

**Fokus:** Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren und Konflikte erkennen. §§ 488 ff. BGB § 39 InsO Rangrücktritt. Prüfraster: Pari-passu-Stellung Rangregelungen Wandlungsrechte Verwasserungsschutz Vesting. Output: Übersichtsmatrix Konfliktliste Handlungsempfehlung. Abgrenzung: nicht für Einzeldarlehen-Erstellung.

# Mehrere parallele Wandeldarlehen

## Zweck

Dieser Skill behandelt die Besonderheiten, wenn gleichzeitig mehrere Wandeldarlehen von verschiedenen Lenders bestehen. Er klärt Stack-Order, MFN-Pflichten, gleichzeitige Wandlung und kombinierte Cap-Table-Auswirkungen. Phase C des Lebenszyklus.

## Eingaben

- Liste aller Wandeldarlehen: Lender, Betrag, Datum, Laufzeit, Cap, Discount, MFN-Klausel
- Aktuelles Wandlungsereignis: für welche Lenders gilt es?
- Vertragliche Stack-Order oder Gleichrangigkeit?
- MFN-Klauseln im jeweiligen Vertrag?
- Vollverwässerte Anteile vor Wandlung aller Lenders

## Rechtlicher Rahmen

### Primärnormen
- § 4.7 Wandeldarlehensvertrag (MFN-Klausel: günstigere Rechte automatisch gültig)
- § 39 Abs. 2 InsO (Gleichrang der Nachrangforderungen untereinander)
- § 55 GmbHG (Kapitalerhöhung – mehrere Übernahmen gleichzeitig möglich)
- § 328 BGB (Drittschutz der Rangrücktrittsvereinbarung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Bestandsaufnahme aller Wandeldarlehen
Tabelle: Lender / Betrag / Datum / Cap / Discount / MFN / Rangrücktritt / Wandlungsstatus. Zeitliche Reihenfolge der Darlehensgewährung (relevant für MFN).

### 2. MFN-Prüfung
Enthält ein späteres Wandeldarlehen einen günstigeren Cap oder Discount? Dann haben frühere Lender (mit MFN-Klausel) Anspruch auf diese günstigeren Konditionen. Automatischer Anpassungsmechanismus.

### 3. Gleichzeitige Wandlung
Alle Lenders wandeln zum gleichen Wandlungsereignis: Berechne Wandlungssumme je Lender (Darlehen + Zinsen). Berechne Wandlungspreis je Lender (nach je eigenem Cap/Discount). Addiere neue Anteile aller Lenders. Dann: Kapitalerhöhungsrunde.

### 4. Kapitalerhöhungsbeschluss für mehrere Lenders
Ein Beschluss kann mehrere Übernahmen gleichzeitig enthalten (§ 55 Abs. 1 GmbHG). Gesellschafterliste nach Kapitalerhöhung: alle neuen Gesellschafter eintragen.

### 5. Stack-Order im Insolvenzfall
Alle Wandeldarlehen mit qualifiziertem Rangrücktritt: gleichrangig nach § 39 Abs. 2 InsO. Keine Priorität unter sich, alle hinter § 38/39 Abs. 1-Gläubigern.

### 6. Kombinierte Cap-Table-Auswirkung
Post-Money-Cap-Table mit allen Lenders und neuen Investoren. Gesamtverwässerung der Altgesellschafterinnen = Summe der Einzelverwässerungen.

## Beispiel: Zwei Wandeldarlehen gleichzeitig

| Parameter | Northstar | Angel-Investor B |
|---|---|---|
| Darlehen | EUR 250000 | EUR 100000 |
| Zinsen | EUR 25694 | EUR 10277 |
| Wandlungssumme | EUR 275694 | EUR 110277 |
| Cap | EUR 4000000 | EUR 3500000 |
| Discount | zwanzig Prozent | fünfzehn Prozent |
| Anteile (100 vor Runde, Pre-Money EUR 6 Mio) | | |
| Cap-Preis Northstar | EUR 40000 | — |
| Cap-Preis Angel B | — | EUR 35000 |
| Neue Anteile | 7 | 4 |
| MFN: Angel B Cap günstiger | Northstar erhält MFN → Cap EUR 35000 | — |
| Neue Anteile Northstar (mit MFN) | 275694/35000 = 7.88 → 8 | 4 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| MFN-Trigger übersehen | Lender erhält schlechtere Konditionen | MFN-Prüfung durchgeführt | MFN automatisch ausgelöst |
| Stack-Order nicht vereinbart | Rangstreit im Insolvenzfall | Mündliche Abrede | Schriftliche Stack-Order |
| Zu viele Lenders auf einmal | Cap-Table komplex, HR-Eintragung aufwändig | Drei bis vier Lenders | Maximal zwei |
| Kapitalerhöhungsbeschluss nur für einen Lender | Zweite Kapitalerhöhung nötig | Beschluss erweiterbar | Umfassender Beschluss |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 55 ff. oder InsO § 39 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 39 InsO (Nachrang Gesellschafterdarlehen) → § 135 InsO (Anfechtung) → §§ 55, 56 GmbHG (Kapitalerhöhung bei Wandlung) → § 5 Abs. 1 GmbHG (Mindest-Nennbetrag Anteile 1 EUR) → § 40 GmbHG (Gesellschafterliste parallele Updates)
