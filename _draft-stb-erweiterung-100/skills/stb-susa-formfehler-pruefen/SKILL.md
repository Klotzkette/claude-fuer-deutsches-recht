---
name: stb-susa-formfehler-pruefen
description: "SuSa-Pruefung auf Formfehler Plausibilitaet und Differenzen. Anwendungsfall Qualitaetspruefung der SuSa vor Versand oder Pruefung Buchungsdifferenzen typische Anomalien. Methodik Checkliste Plausibilitaet Differenz-Analyse. Output Fehlerprotokoll Korrekturmassnahmen."
---

# SuSa-Pruefung — Formfehler, Plausibilitaet, Differenzen

## Kernsachverhalt

Eine fehlerhafte SuSa ist Risiko fuer alle Folgeauswertungen — BWA, USt-VA, Jahresabschluss. Der Steuerberater muss die SuSa systematisch auf Plausibilitaet pruefen, bevor er sie verwendet. Typische Fehler: Pruefsumme-Differenz, ungewoehnliche Salden, USt-Inkonsistenz, offene Verrechnungskonten. Dieser Skill ist Pflicht-Checkliste fuer Sachbearbeiter und Berufstraeger.

## Kaltstart-Rueckfragen

1. Welche Periode wird geprueft — Monat, Quartal, kumuliert?
2. Welche Pruef-Tiefe — Standard-Checkliste oder vertieft?
3. Wurde die laufende Buchfuehrung bereits einmal geprueft?
4. Welche systembedingten Auffaelligkeiten (DATEV-Pruefliste)?
5. Welche Sondereffekte sind erwartet (Anlagenkauf, Sondertilgung)?
6. Welche Konsistenz-Quellen liegen vor (Bankauszug, USt-VA, Lohnauswertung)?
7. Welche Vorperioden-Korrektur ist zu bearbeiten?
8. Welche Eskalation bei wesentlichen Fehlern?

## Rechtlicher Rahmen

### Primaernormen

**§ 239 HGB** — ordnungsgemaesse Buchfuehrung.

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit, Richtigkeit.

**§ 33 StBerG** — StB-Aufgabenkreis (Sorgfalt).

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 153 AO** — Berichtigungspflicht bei erkannten Fehlern.

### Standards

- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.
- DATEV-Pruefliste Monatsabschluss.

## Workflow

### Phase 1 — Pruefsumme Soll/Haben

- Summe Soll-Buchungen = Summe Haben-Buchungen (doppelte Buchfuehrung).
- Differenz = Systemfehler (selten, aber bei Datenmigrationen moeglich).
- Bei Differenz: Konto-Pruefung bis zur Buchung zurueck.

### Phase 2 — Konten-Plausibilitaet

| Konto | Erwartung | Auffaelligkeit |
|---|---|---|
| 8000-8999 Erloese (SKR 03) | Habensaldo | Sollsaldo = Gutschriften nicht erfasst |
| 4000-4999 Aufwand (SKR 03) | Sollsaldo | Habensaldo = Storno nicht erfasst |
| 1200 Bank | Sollsaldo oder Habensaldo (Kontokorrent) | Plausibel mit Bankauszug |
| 1400 Forderungen | Sollsaldo | Habensaldo = Vorauszahlungen Kunden |
| 1500 Verbindlichkeiten LuL | Habensaldo | Sollsaldo = Vorauszahlungen Lieferanten |
| 1576/1776 USt | Plausibel zu USt-VA | Differenz = USt-Fehler |
| 1590/1599 Verrechnungskonten | Saldo 0 | Saldo > 0 = nicht zugeordnete Buchungen |
| 2000 Eigenkapital | Habensaldo (positives EK) | Sollsaldo = negatives EK; Krisensignal |

### Phase 3 — USt-Konsistenz

- USt aus 1776 vs. USt-VA: Differenz pruefen.
- Vorsteuer aus 1576 vs. VA: Differenz pruefen.
- Innergemeinschaftlicher Erwerb (Konto 1786 SKR 03): Erfassung pruefen.
- Reverse-Charge: Konten 1781/1787 (SKR 03) korrekt?

### Phase 4 — Hauptbuch-Nebenbuch-Konsistenz

- Saldo 1400 Hauptbuch = Summe Debitoren-OPOS.
- Saldo 1500 Hauptbuch = Summe Kreditoren-OPOS.
- Bei Differenz: Buchung ohne Personenkonto-Zuordnung suchen.

### Phase 5 — Anlagenkonten und AfA

- Anlagenkonten Saldo = Buchwert Anlagenspiegel.
- AfA-Buchung gegen 4830/4832 = Summe AfA Anlagenspiegel.
- Bei Zu- oder Abgaengen Anlagenspiegel synchron.

### Phase 6 — Fehlerprotokoll und Korrektur

```
FEHLERPROTOKOLL SUSA-PRUEFUNG
Datum: [Datum] Bearbeiter: [Name]

1. Konto 1590 Saldo 12.500 EUR — nicht abgebaut.
   Ursache: unzugeordnete Bankbuchung 28.04.2026.
   Korrektur: Buchung GVC-Zuordnung 71 (Kunde) und Konto 1400.

2. Konto 4000 Habensaldo 850 EUR — ungewoehnlich.
   Ursache: Gutschrift Kunde 10002 ohne Erloesschmaelerung.
   Korrektur: Konto 8730 (Erloesschmaelerung) statt Erlosrueckbuchung.

3. Differenz 1776 USt vs. USt-VA 240 EUR.
   Ursache: vergessene Buchung am 30.04.2026.
   Korrektur: Nachbuchung mit Steuerschluessel 3.
```

## Output

- Fehlerprotokoll mit konkreten Korrekturmassnahmen.
- Korrigierte SuSa.
- Pruefer-Vermerk in Mandantenakte.

## Strategie und Praxis-Tipps

- SuSa-Pruefung sollte vor jedem Versand erfolgen — auch bei Routine-Mandanten.
- Bei wiederholten Fehlern (gleiches Konto, gleicher Sachbearbeiter): Schulung.
- Pruefliste standardisieren — Sachbearbeiter haben einheitliches Pruefraster.
- Bei wesentlichen Fehlern in der Vorperiode: § 153 AO Berichtigungspflicht.
- StBVV: Pruefung als Bestandteil der Buchfuehrungspauschale.
- DATEV-Tipp: DATEV-Pruefliste Monatsabschluss systematisch durchgehen; "Konten mit ungewoehnlichem Saldo" als Standardlauf.

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-susa-haupt-und-personenkonten` — Hauptbuch-Nebenbuch.
- `stb-susa-vorperiode-vergleich` — Periodenvergleich.
- `stb-bwa-fehlerquellen-haeufig` — BWA-Fehler.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 239.
- AO §§ 146, 153.
- StBerG §§ 33, 57.
- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.
