---
name: gesellschaftsgruender-cap-table
description: "Cap-Table-Erzeugung Capitalization Table. Pre-Money und Post-Money-Bewertung Bezugsrechtsverteilung Verwaesserung Anteilsklassen. Liquidation-Preference-Waterfall. Cap-Table als Excel JSON oder Markdown. Schnittstelle zum Notar mit beglaubigter Gesellschafterliste Paragraf 40 GmbHG. Vesting-Schedule pro Gruender. Mit Beispielen Solo Gruender bis Series A."
---

# Cap Table

## Zweck

Der Cap Table (Capitalization Table) zeigt **wer wieviele Anteile zu welchem Wert** haelt — Grundlage für Notar-Anmeldung, Investor-Verhandlungen, Verwässerungs-Simulationen und steuerliche Bewertungen.

## 1) Inhalte

### Pflicht-Spalten

- Gesellschafter (Name, Geburtsdatum)
- Anteilsklasse (Common, A, B, C, ...)
- Anzahl Anteile / Nennwert pro Anteil / Summe Nennwert
- Anteil in Prozent
- Stimmrechte (falls abweichend von Quote)
- Vesting-Status (gevested / ungevested, Cliff-Datum)

### Optionale Spalten

- Erwerbs-Datum
- Erwerbs-Preis pro Anteil
- Aktueller Verkehrswert pro Anteil
- Liquidation Preference (z.B. 1x non-participating)
- Anti-Dilution-Status

## 2) Beispiel: Solo-Gründer mit Pre-Seed-Investor

```
| Gesellschafter        | Klasse | Anteile | Nennwert | %     | Stimmen | Vesting |
|-----------------------|--------|---------|----------|-------|---------|---------|
| Anna Mueller (Gruender)| Common | 20.000  | 1 EUR    | 80 %  | 80 %    | 25/48 nach 12 Monaten Cliff |
| Investor I AG         | A      | 5.000   | 1 EUR    | 20 %  | 20 %    | -       |
| Stammkapital gesamt   |        | 25.000  | 25.000 EUR | 100 %| 100 %  |         |
```

## 3) Beispiel: Mehrgründer-GmbH mit Class-Shares nach Series A

```
| Gesellschafter        | Klasse | Anteile | %     | Stimmen | Liquidation Preference |
|-----------------------|--------|---------|-------|---------|------------------------|
| Anna Mueller (CEO)    | Common | 12.000  | 30 %  | 30 %    | -                      |
| Bernd Schmidt (CTO)   | Common | 12.000  | 30 %  | 30 %    | -                      |
| Carla Wagner (CFO)    | Common | 4.000   | 10 %  | 10 %    | -                      |
| Founders Holding GmbH | Common | 4.000   | 10 %  | 10 %    | -                      |
| Investor I AG         | A      | 6.000   | 15 %  | 18 % (1,2x)| 1x non-participating|
| Investor II Capital   | B      | 2.000   | 5 %   | 6 % (1,2x) | 1,5x participating |
| ESOP-Pool             | Common | 0       | 0 %   | 0 %     | (reserviert 10 %)      |
| Stammkapital gesamt   |        | 40.000  | 100 % | 94 %    |                        |
```

(Stimmrechte > 100 % möglich bei Vorzugsklassen mit Mehrstimmrecht)

## 4) Pre-Money / Post-Money

### Begriffe

- **Pre-Money**: Bewertung vor Investment
- **Post-Money**: Bewertung nach Investment = Pre-Money + Investment-Summe
- **Investor-Anteil** = Investment / Post-Money

### Beispiel

- Pre-Money: 4 Mio. EUR
- Investment: 1 Mio. EUR
- Post-Money: 5 Mio. EUR
- Investor-Anteil: 1 / 5 = 20 %
- Gründer-Verwässerung: von 100 % auf 80 %

## 5) Bezugsrechte und Verwässerung

### Bezugsrecht (Paragraf 55 II GmbHG bzw. analog)

- Bei Kapitalerhöhung: bestehende Gesellschafter haben Bezugsrecht auf neue Anteile **anteilig**
- Vermeidet Verwässerung
- Kann durch Gesellschafterbeschluss (75 %) **ausgeschlossen** werden — `gesellschaftsgruender-kapitalerhoehung-bezugsrecht`

### Verwässerung simulieren

Bei nicht mitziehender Bezugsrechte-Ausübung:

```
Vor Runde:  Gruender 80 %, Pre-Money 4 Mio.
Series A:   2 Mio. EUR neue Anteile, Bezugsrecht ausgeschlossen
Post-Money: 6 Mio. EUR
Investor:   33 %
Gruender:   80 % * (4 / 6) = 53 %
```

## 6) Liquidation-Waterfall

Bei Exit / Auflösung:

1. **Liquidation Preference** der Vorzugsanteile (sortiert nach Vorrang)
2. Restbetrag wird nach Anteilen verteilt (bei „participating" zusätzlich)

### Beispiel

- Exit-Preis: 10 Mio. EUR
- Investor I A: 1 Mio. EUR Investment, 1x non-participating, 20 % Anteil
- Investor II B: 0,5 Mio. EUR Investment, 1,5x participating, 5 % Anteil
- Gründer: 75 % Anteil

Waterfall:

- Investor II B: 0,5 * 1,5 = 0,75 Mio. (Preference)
- Restbetrag für Investor I A: max(1 Mio., 20 % * Rest)
- Schritt 1: Restbetrag = 10 - 0,75 = 9,25 Mio.
- 20 % davon: 1,85 Mio. — also Investor I A wählt **anteilig** (1,85 > 1,0)
- Investor I A: 1,85 Mio.
- Investor II B (participating, anteilig zusätzlich): 5 % * 9,25 = 0,46 Mio. ZUSAETZLICH zur Preference
- Investor II B insgesamt: 0,75 + 0,46 = 1,21 Mio.
- Gründer: 9,25 - 1,85 - 0,46 = 6,94 Mio.

## 7) Vesting-Schedule

Standard:

- **4 Jahre Vesting**, **12 Monate Cliff**
- Bis 12 Monate: 0 vested
- Bei 12 Monaten: 25 % vested (12/48)
- Danach: monatlich 1/48 zusätzlich
- Bei 48 Monaten: 100 %

Bei Bad-Leaver vor Vollvestung: Anteile gehen zurueck an die Gesellschaft (Einziehung Paragraf 34 GmbHG oder Pflicht-Rueckverkauf zum Nominalwert).

## 8) Format-Vorlagen

- **Excel/CSV** (Standard bei Investoren-Reportings)
- **Markdown** (in Datenraum)
- **JSON** (für automatische Pipelines)
- **PDF** (mit Stempel-/Signatur für Notar / Investor)

## 9) Gesellschafterliste Paragraf 40 GmbHG

### Pflicht

- Erste Liste mit Notar-Anmeldung
- Jede Änderung: neue Liste binnen Änderung
- Notar reicht ein bei Anteilsübertragung (Paragraf 40 II GmbHG)
- Im Handelsregister hinterlegt, öffentlich einsehbar

### Inhalt der Gesellschafterliste

- Vor- und Nachname (bei juristischer Person Firma)
- Anschrift, Geburtsdatum
- Geschäftsanteile mit Nummer und Nennwert
- Eintragungs-Datum

### Cap Table vs. Gesellschafterliste

Der Cap Table ist die **interne** Übersicht (alle Klassen, Verwässerung, Vesting). Die Gesellschafterliste ist die **öffentliche** Liste (HR). Beide müssen konsistent sein.

## 10) Typische Cap-Table-Fehler

1. **Vesting nicht abgebildet** im Cap Table -> bei Leaver-Diskussion fehlt Datenbasis
2. **Liquidation Preference nicht waterfall-simuliert** -> Investor versteht Konsequenzen nicht
3. **ESOP-Pool vergessen** -> Spätere Aufnahme verwaessert Gründer, nicht Investor
4. **Genehmigtes Kapital nicht berücksichtigt** -> Bei Aufstockung Verwirrung
5. **Anteilsklassen vermischt** -> Stimmrechte und wirtschaftliche Anteile divergieren, im Cap Table aber nicht klar abgebildet

## Anschluss

- `gesellschaftsgruender-share-classes-a-b-c` — bei mehreren Klassen
- `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` — Verwässerung
- `gesellschaftsgruender-genehmigtes-kapital` — Vorrats-Beschluss
- `gesellschaftsgruender-notar-vorbereitung` — Gesellschafterliste für Anmeldung
