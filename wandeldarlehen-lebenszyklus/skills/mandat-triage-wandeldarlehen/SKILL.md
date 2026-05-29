---
name: mandat-triage-wandeldarlehen
description: "Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Vertragstyp SAFE Convertible Note Laufzeit Wandlungsereignisse offene Punkte. Output: Mandatssteckbrief Routen-Empfehlung Datenliste. Abgrenzung: Triage und Einstieg; Detailarbeit in Spezialist-Skills."
---

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
