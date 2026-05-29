---
name: stb-susa-debitorenliste-osa-offene-posten
description: "Debitoren-Saldenliste und Offene-Posten-Auswertung OPOS. Anwendungsfall Monats- oder Quartalsauswertung Mahnwesen Forderungsanalyse Bilanzvorbereitung. Methodik OPOS-Liste Fälligkeitsstrukur Top-Schuldner Risikoprüfung. Output OPOS-Liste mit Fälligkeitsstaffel."
---

# Debitoren-Saldenliste / Offene-Posten-Auswertung (OPOS)

## Kernsachverhalt

Die Debitoren-Saldenliste zeigt alle Forderungen gegen Kunden mit Saldo, Faelligkeit und Status. Die OPOS-Auswertung ist Standardinstrument fuer Mahnwesen, Bilanzvorbereitung und Liquiditaetsplanung. Der Steuerberater erstellt sie monatlich (oder mit BWA-Frequenz), prueft die Werthaltigkeit grosser Posten und gibt Hinweise auf Forderungsausfall-Risiken.

## Kaltstart-Rueckfragen

1. Welcher Stichtag — Monatsende, Quartalsende, Bilanzstichtag?
2. Welche Detailtiefe — alle OP oder nur ueberfaellige?
3. Welche Faelligkeitsstaffeln (0-30, 31-60, 61-90, > 90 Tage)?
4. Welche Top-Schuldner sind zu beobachten?
5. Welche Forderungen sind strittig oder von Mandantenkonflikten betroffen?
6. Welche Mahnsystematik ist mit dem Mandanten vereinbart?
7. Welche Einzelwertberichtigungen sind anzusetzen?
8. Welche Pauschalwertberichtigung (1 Prozent) gilt fuer Bilanzstichtag?

## Rechtlicher Rahmen

### Primaernormen

**§ 252 Abs. 1 Nr. 4 HGB** — Vorsichtsprinzip; Forderungen niederwertbewertet.

**§ 253 Abs. 4 HGB** — Niederstwertprinzip Umlaufvermoegen; Forderungen.

**§ 6 Abs. 1 Nr. 2 EStG** — steuerliche Bewertung; voraussichtlich uneinbringliche Forderung.

**§ 17 InsO** — Zahlungsunfaehigkeit; Faelligkeitsstruktur ist Indikator.

**§ 102 StaRUG** — Hinweispflicht.

### Standards

- BMF zu Forderungsbewertung: massgeblich sind §§ 252, 253 HGB und § 6 Abs. 1 Nr. 2 EStG; aktuelle BMF-Schreiben zur Einzel- und Pauschalwertberichtigung ueber bundesfinanzministerium.de abrufbar.
- IDW PS 480.
- DATEV OPOS-Modul.

## Workflow

### Phase 1 — Datenbasis

- OPOS-Liste aus DATEV/Addison/Sage.
- Mahnstand und Mahnbescheid-Vermerke.
- Strittige Forderungen aus Mandantenkommunikation.
- Insolvenzvermerke (Schuldner in Insolvenz?).

### Phase 2 — Aufbau OPOS-Liste

```
DEBITOREN-OPOS-LISTE
Stichtag: [Datum]

Konto    Name             Saldo EUR   Faelligkeit   Mahnstand   Bemerkung
10001    [Kunde A]        5.500       30 Tage       1. Mahnung  Brief am [Datum]
10002    [Kunde B]        12.000      90 Tage       3. Mahnung  Anwalt eingeschaltet
10003    [Kunde C]        850         15 Tage       —           im Plan
...
SUMME                     [X]
```

### Phase 3 — Faelligkeitsstaffel

| Staffel | Anteil | Bewertung |
|---|---|---|
| Nicht faellig (0-30 Tage) | [X Prozent] | Normalbestand |
| 31-60 Tage faellig | [Y Prozent] | Erinnerung versenden |
| 61-90 Tage faellig | [Z Prozent] | Mahnung 1./2. Stufe |
| Ueber 90 Tage | [A Prozent] | Anwalt einschalten |
| Ueber 180 Tage | [B Prozent] | Einzelwertberichtigung |

### Phase 4 — Bewertung

- Einzelwertberichtigung bei konkretem Ausfallrisiko (Schuldner in Insolvenz, Bestreitung).
- Pauschalwertberichtigung: 1 Prozent der nicht-einzelwertberichtigten Restforderung (in der Steuerbilanz; in der Handelsbilanz mit konkreter Risikobewertung).
- Forderungen aus Lieferungen und Leistungen mit USt: VBerich brutto bewerten, USt-Berichtigung nach § 17 UStG.

### Phase 5 — Mahnwesen

- Aufbau-Mahnstufen: Zahlungserinnerung (kostenfrei), 1. Mahnung (15 EUR), 2. Mahnung (20 EUR), Anwalt (gerichtlich).
- Mahnbeschuldigung ueber DATEV-Mahnmodul oder externes Inkasso.
- Bei groesseren Forderungen: Anwalt mit Klage beauftragen.

### Phase 6 — Reporting an Mandant

- OPOS-Auszug monatlich an Mandant.
- Hinweis auf Top-Schuldner und Verdaechtige.
- Empfehlungen zum Mahnwesen.
- Bei drohendem grossen Forderungsausfall: Liquiditaets-Eskalation.

## Output

- OPOS-Liste mit Faelligkeitsstaffel.
- Mahnempfehlung mit Top-Schuldnern.
- Einzelwertberichtigungs-Vorschlag.

## Strategie und Praxis-Tipps

- Bei Bilanzstichtag detaillierte Forderungsbewertung — Einzel- und Pauschalwertberichtigung dokumentieren.
- Top-Schuldner mit groesseren Forderungen einzeln pruefen (z.B. Top-10).
- Bei Forderungsausfall-Risiko ueber 10 Prozent der Bilanzsumme: Hinweispflicht § 102 StaRUG ausgeloest.
- Mahnwesen frueh ansetzen — je laenger gewartet wird, desto schwieriger ist Durchsetzung.
- StBVV: OPOS in Buchfuehrungspauschale; separates Mahnwesen-Honorar.
- DATEV-Tipp: DATEV-OPOS-Auswertung mit Faelligkeitsstaffeln und Mahn-Bewegungs-Eingabe.

## Querverweise

- `stb-susa-kreditorenliste-ova` — Kreditoren-OPOS.
- `stb-susa-saldenabstimmung-bestaetigung` — Saldenabstimmung.
- `stb-bwa-statische-liquiditaet-kennzahlen` — Liquiditaet.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bilanzvorbereitung.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 252, 253.
- EStG §§ 5, 6.
- UStG § 17.
- InsO § 17.
- StaRUG § 102.
- IDW PS 480.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (BMF-Hinweis ohne Marker neu formuliert) -->
