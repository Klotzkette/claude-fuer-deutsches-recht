---
name: stb-bwa-bewegungsbilanz-erstellen
description: "Bewegungsbilanz aus BWA und SuSa erstellen. Anwendungsfall Veranschaulichung Geld- und Mittelfluss zwischen zwei Stichtagen Vermoegens- und Kapitalbewegung. Methodik Aktiva und Passiva Vergleich Mittelherkunft Mittelverwendung. Output Bewegungsbilanz als Anhang zur BWA. Querverweis stb-bwa-cashflow-laienverstaendlich."
---

# Bewegungsbilanz aus BWA und SuSa

## Kernsachverhalt

Die Bewegungsbilanz stellt die Veraenderungen einzelner Bilanzposten zwischen zwei Stichtagen dar und macht damit deutlich, woher Mittel kamen (Mittelherkunft) und wohin sie geflossen sind (Mittelverwendung). Sie ist Vorstufe der Kapitalflussrechnung nach DRS 21 und IDW S 6 und wird besonders bei Bankgespraechen, Sanierungsmandaten und im Vorfeld der Fortbestehensprognose benoetigt. Der Steuerberater erstellt sie aus der SuSa zum Anfangs- und Endstichtag plus den BWA-Erfolgskonten.

## Kaltstart-Rueckfragen

1. Welche Stichtage — Quartal, Halbjahr, Jahresende?
2. Liegt eine Stichtag-SuSa vor (Anfang und Ende der Periode)?
3. Welche Detailtiefe — Hauptposten oder einzelne Konten?
4. Sondereffekte in der Periode (Anlagenverkauf, Kapitalerhoehung, Gesellschafterdarlehen)?
5. Verwendungszweck — interne Steuerung, Bankgespraech, Sanierungskonzept?
6. Welche Vergleichsperiode — Vorjahresperiode parallel?
7. Welche Konsolidierung — Einzelgesellschaft oder Konzernblick?
8. Welche Abgrenzung — Geldfluss vs. nicht-zahlungswirksame Posten (Abschreibungen, Rueckstellungen)?

## Rechtlicher Rahmen

### Primaernormen

**§ 264 HGB** — Aufstellungspflicht Jahresabschluss; Anhang ggf. mit Kapitalflussrechnung.

**§ 297 HGB** — Konzernabschluss; Kapitalflussrechnung verpflichtend.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 19 InsO** — Fortbestehensprognose; Bewegungsbilanz als analytische Grundlage.

### Standards

- DRS 21 — Kapitalflussrechnung (verbindlich fuer Konzernabschluesse, empfohlen fuer Einzelabschluesse).
- IDW S 6 — Sanierungskonzept (Bewegungsbilanz als analytische Grundlage).
- IDW PS 305 — Risikofrueherkennung § 91 Abs. 2 AktG.

## Workflow

### Phase 1 — Datenbasis

- SuSa zum Anfangsstichtag (z.B. 31.12. Vorjahr).
- SuSa zum Endstichtag (z.B. 31.12. Berichtsjahr).
- BWA-Daten fuer die Periode (insbesondere Abschreibungen, Rueckstellungsveraenderung).
- Anlagenspiegel (Zugaenge, Abgaenge, AfA).

### Phase 2 — Strukturierung Aktiva

```
AKTIVA-VERAENDERUNG:
Position                        Anfang     Ende    Veraenderung
Anlagevermoegen
  Sachanlagen                   [X]        [Y]      [+/-Z]
  Immaterielle WG               [X]        [Y]      [+/-Z]
  Finanzanlagen                 [X]        [Y]      [+/-Z]
Umlaufvermoegen
  Vorraete                      [X]        [Y]      [+/-Z]
  Forderungen LuL               [X]        [Y]      [+/-Z]
  Sonstige Forderungen          [X]        [Y]      [+/-Z]
  Liquide Mittel                [X]        [Y]      [+/-Z]
Aktive Rechnungsabgrenzung      [X]        [Y]      [+/-Z]
```

### Phase 3 — Strukturierung Passiva

```
PASSIVA-VERAENDERUNG:
Eigenkapital
  Gezeichnetes Kapital          [X]        [Y]      [+/-Z]
  Kapitalruecklagen             [X]        [Y]      [+/-Z]
  Gewinn-/Verlustruecklage      [X]        [Y]      [+/-Z]
  Jahresergebnis                [X]        [Y]      [+/-Z]
Rueckstellungen                 [X]        [Y]      [+/-Z]
Verbindlichkeiten
  Kreditinstitute               [X]        [Y]      [+/-Z]
  Lieferanten                   [X]        [Y]      [+/-Z]
  Sonstige Verbindlichkeiten    [X]        [Y]      [+/-Z]
Passive Rechnungsabgrenzung     [X]        [Y]      [+/-Z]
```

### Phase 4 — Mittelherkunft und Mittelverwendung

```
MITTELHERKUNFT:
- Jahresueberschuss
- Abschreibungen (zahlungsunwirksam)
- Erhoehung Rueckstellungen
- Erhoehung Verbindlichkeiten
- Verringerung Vorraete
- Verringerung Forderungen
- Anlagenabgang (Veraeusserung)
- Kapitalerhoehung Gesellschafter

MITTELVERWENDUNG:
- Jahresfehlbetrag
- Verringerung Rueckstellungen
- Verringerung Verbindlichkeiten
- Erhoehung Vorraete
- Erhoehung Forderungen
- Anlagenzugang (Investition)
- Ausschuettung an Gesellschafter
```

### Phase 5 — Saldo und Pruefung

- Saldo Mittelherkunft minus Mittelverwendung = Veraenderung liquide Mittel.
- Gegencheck: Veraenderung Bank-Konten in SuSa muss matchen.
- Differenz zeigt Fehler in der Aufstellung — pruefen.

### Phase 6 — Erlaeuterung und Versand

- Erlaeuterungstext fuer wesentliche Bewegungen.
- Bei Bank-/Investor-Reporting: zusammen mit Bilanz und BWA.
- Mandantenakte dokumentieren.

## Output

- Bewegungsbilanz als strukturiertes PDF.
- Erlaeuterungstext zu wesentlichen Veraenderungen.
- Vorstufe fuer Kapitalflussrechnung.

## Strategie und Praxis-Tipps

- Die Bewegungsbilanz ist bei Kleinunternehmen keine Pflicht, gehoert bei mittelstaendischer Bilanzanalyse jedoch zum Standard.
- Banken erwarten bei groesseren Kreditengagements regelmaessig eine Bewegungsbilanz oder direkt eine Kapitalflussrechnung.
- Bei Sanierungsmandaten ist die Bewegungsbilanz Pflichtbestandteil neben dem Liquiditaetsplan.
- Praxis-Tipp: Die Bewegungsbilanz wird ueblicherweise halbjaehrlich erstellt und nicht monatlich, da der Aufstellungsaufwand bei kuerzerem Intervall den Steuerungsnutzen uebersteigt.
- StBVV: Diese Sonderauswertung wird ueber Zeithonorar oder Pauschalvereinbarung gesondert abgerechnet.
- DATEV-Tipp: Das DATEV-Bilanzbericht-/BAB-Modul automatisiert die Bewegungsbilanz aus zwei SuSa-Stichtagen (Klickpfad: Rechnungswesen → Auswertungen → Bewegungsbilanz oder Bilanzanalyse-Auswertungspaket).

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-kapitalflussrechnung-iduk` — Kapitalflussrechnung.
- `stb-bwa-cashflow-laienverstaendlich` — Cashflow.
- `stb-liquiditaetsvorschau-3-6-12-monate` — Liquiditaetsplan.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 264, 297.
- DRS 21.
- IDW S 6, IDW PS 305.
- InsO § 19.
- DATEV BAB-Modul.
