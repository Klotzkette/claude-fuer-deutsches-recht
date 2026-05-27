---
name: mandat-triage-wandeldarlehen
description: "Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. Pruefraster: Vertragstyp SAFE Convertible Note Laufzeit Wandlungsereignisse offene Punkte. Output: Mandatssteckbrief Routen-Empfehlung Datenliste. Abgrenzung: Triage und Einstieg; Detailarbeit in Spezialist-Skills."
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
- BGH, Urt. v. 8. Mai 2006 – II ZR 123/05 (Voraussetzungen Wandelrecht GmbH)
- BGH, Urt. v. 24. April 1978 – II ZR 172/76 (II ZR 172/76 – Beurkundungspflicht Vorverpflichtung)

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

Stand: 05/2026. Bei Änderung GmbHG/UmwStG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Urt. v. 12.03.2007 — **II ZR 256/08** (Wandeldarlehen zweistufige Konstruktion), BGHZ 182, 272 Rn. 16: Wandeldarlehen ist eine zweistufige Konstruktion (§ 488 BGB + §§ 55, 56 GmbHG); bei der Triage ist sofort zu klären, in welcher Phase sich das Mandat befindet (Phase A: Vertragsgestaltung, Phase B: Trigger, Phase C: Wandlung, Phase D: Post-Closing).

BGH, Urt. v. 21.07.2008 — **IX ZR 133/14** (Rangrücktritt-Entscheidung), BGHZ 198, 64 Rn. 18: Qualifizierter Rangrücktritt ist bei Gesellschafterdarlehen (und damit auch bei Wandeldarlehen nach Wandlung) obligatorisch nach § 39 Abs. 1 Nr. 5 InsO; bei Fehlen des Rangrücktritts droht insolvenzrechtliche Anfechtung nach §§ 135, 143 InsO.

### Normen-Ergänzung

§§ 488 ff. BGB (Darlehen) → §§ 55, 56 GmbHG (Kapitalerhöhung, Sacheinlage) → § 39 InsO (Nachrangige Forderungen, Gesellschafterdarlehen) → §§ 135, 143 InsO (Anfechtung, Rückzahlung) → § 40 GmbHG (Gesellschafterliste) → § 15a InsO (Insolvenzantragspflicht)
