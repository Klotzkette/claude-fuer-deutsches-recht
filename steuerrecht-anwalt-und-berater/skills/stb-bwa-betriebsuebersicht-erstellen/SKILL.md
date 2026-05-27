---
name: stb-bwa-betriebsuebersicht-erstellen
description: "Betriebsuebersicht als ergaenzende Auswertung zur BWA. Anwendungsfall ausfuehrliche Monats- oder Quartalsauswertung mit allen Sachkonten-Salden ergaenzend zur kompakten BWA. Methodik Konfiguration in DATEV oder Addison als Kontenliste mit Vorjahres- und Plan-Spalten. Output Betriebsuebersicht als PDF Anhang zur BWA."
---

# Betriebsuebersicht erstellen — Ergaenzung zur BWA

## Kernsachverhalt

Die Standard-BWA fasst Konten in funf Bloecken zusammen. Fuer detaillierte Analysen reicht das nicht — der Mandant will wissen, woraus sich "sonstige betriebliche Aufwendungen" zusammensetzen oder welche Erloeskonten beigetragen haben. Die Betriebsuebersicht ist die Kontenliste mit Salden, Vorjahresvergleich und ggf. Plan-Werten. Sie ergaenzt die BWA und ist Standard bei groesseren Mandanten und im Steuerberater-Buero zur internen Analyse.

## Kaltstart-Rueckfragen

1. Welche Detailtiefe — alle Konten oder nur die wesentlichen?
2. Mandantenwunsch Layout — Konten in der Reihenfolge des Kontenrahmens oder strukturiert nach Funktionsbereichen?
3. Welche Vergleichsspalten — Vormonat, Vorjahres-Monat, kumulierter Jahresvergleich, Plan?
4. Welche Sortierung — Saldenhoehe, Kontenrahmen, alphabetisch?
5. Welche Schwellenwerte — Konten mit Saldo unter X EUR ausblenden?
6. Liegen Sachkontenbezeichnungen aktuell vor (Stammdaten aktualisieren)?
7. Wird die Uebersicht intern oder extern (Mandant, Bank, Investor) genutzt?
8. Welche Konten muessen vertraulich gefuehrt werden (z.B. GF-Bezuege)?

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 33 StBerG** — Aufgabenkreis StB.

### Standards

- DATEV BWA-Form 21 (Branchen-BWA) und Kontenuebersicht.
- IDW PS 480 (Erstellungsgrundsaetze).

## Workflow

### Phase 1 — Konfigurations-Wahl

| Form | Verwendung |
|---|---|
| Reine Kontenliste | Interne Stichprobe, Sachbearbeiter-Pruefung |
| Strukturierte Betriebsuebersicht | Mandant, Berufstraeger-Pruefung |
| Branchen-Betriebsuebersicht | Branchen-Vergleich (BBE) |
| Erweiterte Betriebsuebersicht | Bank-/Investor-Reporting |

### Phase 2 — Aufbau strukturierte Betriebsuebersicht

Beispiel-Aufbau (Kontennummern typische SKR 03-Beispiele; konkrete Nummern mit aktueller DATEV-Kontenrahmenfassung abgleichen):

```
BETRIEBSUEBERSICHT
Mandant: [Firma]
Zeitraum: [Monat / kumuliert]

I. UMSATZ UND BETRIEBLICHE ERTRAEGE
  8400 Erloese 19 Prozent USt                   [X]
  8300 Erloese 7 Prozent USt                    [X]
  8125 Erloese steuerfreie innergem. Lieferung  [X]
  8200 Sonstige betriebliche Ertraege           [X]

II. MATERIAL- UND WARENEINSATZ
  3400 Wareneingang 19 Prozent VSt              [X]
  3300 Wareneingang 7 Prozent VSt               [X]
  3100 Fremdleistungen                          [X]

III. PERSONALKOSTEN
  4120 Loehne                                   [X]
  4130 Gehaelter                                [X]
  4138 Beitraege zur Berufsgenossenschaft       [X]
  4140 Krankenkassen-AG-Anteil                  [X]

IV. SONSTIGE BETRIEBLICHE AUFWENDUNGEN
  4210 Miete                                    [X]
  4240 Gas Strom Wasser                         [X]
  4500 Kfz-Kosten                               [X]
  4600 Werbe- und Reisekosten                   [X]
  4900 Sonstige betriebliche Aufwendungen       [X]

V. ABSCHREIBUNGEN
  4830 Absetzungen auf Sachanlagen              [X]

VI. ZINSERGEBNIS UND STEUERN
  7300 Zinsen und aehnliche Aufwendungen        [X]
  7100 Zinsertraege                             [X]
  7600 Steuern vom Einkommen und Ertrag         [X]

ERGEBNIS NACH STEUERN                           [X]
```

### Phase 3 — Vergleichsspalten

| Spalte | Inhalt | Quelle |
|---|---|---|
| Monat aktuell | Ist-Saldo der Periode | BWA-Buchungen |
| Monat Vorjahres-Periode | Saldo gleicher Monat Vorjahr | Vorjahres-DATEV |
| Kumuliert Jahr | Saldo seit Jahresbeginn | Year-to-Date |
| Kumuliert Vorjahres-Jahr | Vorjahres-YTD | Vorjahres-DATEV |
| Plan-Wert | Aus Stammdaten | Plan-Eingabe |
| Abweichung absolut | Ist minus Vorjahr / Plan | Berechnung |
| Abweichung in Prozent | absolute Abweichung / Vergleichswert | Berechnung |

### Phase 4 — Filter und Sortierung

- Konten ohne Saldo ausblenden (Default).
- Konten mit Saldo < 100 EUR ggf. ausblenden (oder als "Sonstige" zusammenfassen).
- Sortierung nach Kontenrahmen (SKR 03 oder SKR 04).
- Innerhalb der Bloecke nach Saldenhoehe absteigend (optional).

### Phase 5 — Vertrauliche Konten

- GF-Bezuege, Tantiemen: Mandantenwunsch beachten (oft separat behandeln).
- Privatentnahmen Einzelunternehmer: nicht in BWA, sondern Kapitalkonto.
- Sondergesellschafterdarlehen: separat ausweisen.

### Phase 6 — Versand und Ablage

- Als PDF gemeinsam mit BWA.
- Ablage in Mandantenakte mit Versanddatum.
- Mandanten-Portal-Download moeglich.

## Output

- Betriebsuebersicht als strukturiertes PDF.
- Anhang zur BWA.
- Interne Auswertungs-Datei (Excel-Export aus DATEV).

## Strategie und Praxis-Tipps

- Betriebsuebersicht ist Pflicht bei Mittelstand und Konzern-Reporting.
- Bei KMU: optional, mandantenabhaengig anbieten.
- Vertrauliche Konten klar markieren oder in geschuetzten Bereich auslagern.
- Bei Wechsel des Kontenrahmens Vorjahresvergleich nicht moeglich ohne Brueckenposten.
- DATEV-Tipp: Standard-Betriebsuebersicht 21 oder individuelle Konfiguration ueber Berater-Stammdaten.
- StBVV: Standardform pauschaliert, individuelle Konfiguration als Zeithonorar.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-susa-erstellen-grundlagen` — Summen- und Saldenliste als Grundlage.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Vorjahresvergleich.
- `stb-bwa-kontenrahmen-skr03-skr04` — Kontenrahmenwahl und Mapping.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252.
- StBerG § 33.
- DATEV BWA-Form 21, Kontenuebersicht.
- IDW PS 480.
