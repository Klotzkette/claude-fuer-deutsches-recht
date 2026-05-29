---
name: stb-susa-formfehler-pruefen
description: "SuSa-Prüfung auf Formfehler Plausibilitaet und Differenzen. Anwendungsfall Qualitaetsprüfung der SuSa vor Versand oder Prüfung Buchungsdifferenzen typische Anomalien. Methodik Checkliste Plausibilitaet Differenz-Analyse. Output Fehlerprotokoll Korrekturmassnahmen."
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

### Phase 2 — Konten-Plausibilitaet (Kontennummern beispielhaft im SKR 03; aktuelle DATEV-Kontenrahmenfassung pruefen)

| Konto-Bereich | Erwartung | Auffaelligkeit |
|---|---|---|
| 8000er Erloese (SKR 03) | Habensaldo | Sollsaldo deutet auf nicht erfasste Gutschriften hin |
| 4000er Aufwand (SKR 03) | Sollsaldo | Habensaldo deutet auf nicht erfasste Stornos hin |
| 1200 Bank | Sollsaldo oder Habensaldo (Kontokorrent) | Mit Bankauszug abgleichen |
| 1400er Forderungen (SKR 03 Sammelkonto) | Sollsaldo | Habensaldo deutet auf Kundenvorauszahlungen hin |
| 1700er Verbindlichkeiten LuL (SKR 03 Sammelkonto) | Habensaldo | Sollsaldo deutet auf Vorauszahlungen an Lieferanten hin |
| USt-Konten (z. B. 1576 Vorsteuer 19 Prozent / 1776 USt 19 Prozent im SKR 03) | Plausibel zur USt-Voranmeldung | Differenz weist auf USt-Buchungsfehler hin |
| Geldtransit-/Verrechnungskonten (z. B. SKR 03 1590/1599) | Saldo null | Saldo deutet auf nicht zugeordnete Buchungen hin |
| Eigenkapital-Konto (z. B. SKR 03 2000) | Habensaldo (positives EK) | Sollsaldo bedeutet negatives Eigenkapital — Krisensignal |

### Phase 3 — USt-Konsistenz (Kontennummern beispielhaft im SKR 03; mit aktueller DATEV-Kontenrahmenfassung abgleichen)

- USt-Konto 19 Prozent (typisch SKR 03 1776) gegen USt-Voranmeldung pruefen.
- Vorsteuer-Konto 19 Prozent (typisch SKR 03 1576) gegen USt-Voranmeldung pruefen.
- Innergemeinschaftlicher Erwerb (USt-Konten im 1780er-Bereich, z. B. SKR 03 1786): Erfassung pruefen.
- Reverse-Charge nach § 13b UStG: typische Konten SKR 03 1787 (Umsatzsteuer) und 1576/1577 (Vorsteuer-Gegenbuchung); konkrete Kontonummern in DATEV-Kontenrahmen SKR 03 nachschlagen (DATEV-Kontenrahmen-PDF unter datev.de).

### Phase 4 — Hauptbuch-Nebenbuch-Konsistenz

- Saldo Forderungssammelkonto (typisch SKR 03 1400) gegen Summe der Debitoren-OPOS pruefen.
- Saldo Verbindlichkeiten-Sammelkonto (typisch SKR 03 1700) gegen Summe der Kreditoren-OPOS pruefen.
- Bei Differenz: Buchungen ohne Personenkonto-Zuordnung suchen (DATEV-Klickpfad: Rechnungswesen → Buchungserfassung → Stapelverarbeitung → Filter "ohne OPOS-Zuordnung").

### Phase 5 — Anlagenkonten und AfA

- Anlagenkonten-Saldo (Klasse 0 SKR 03) gegen Buchwert im Anlagenspiegel pruefen.
- AfA-Aufwandskonten (typisch SKR 03 4830 fuer Sachanlagen) gegen Summe der AfA aus dem Anlagenspiegel abstimmen.
- Bei Zu- oder Abgaengen Anlagenspiegel synchronhalten.

### Phase 6 — Fehlerprotokoll und Korrektur

```
FEHLERPROTOKOLL SUSA-PRUEFUNG
Datum: [Datum] Bearbeiter: [Name]

1. Verrechnungskonto (z. B. SKR 03 1590) Saldo 12.500 EUR — nicht abgebaut.
   Ursache: unzugeordnete Bankbuchung 28.04.2026.
   Korrektur: Buchungsaufloesung gegen Forderungssammelkonto (SKR 03 1400), GVC-Zuordnung 71.

2. Erloeskonto Habensaldo wider Erwarten gering, Sollsaldo 850 EUR.
   Ursache: Gutschrift Kunde 10002 wurde gegen Erloeskonto gebucht statt Erloesschmaelerung.
   Korrektur: Umbuchung auf Erloesschmaelerungs-Konto im 8730er-Bereich (SKR 03; typisch Konto 8736 oder 8739 je nach Steuerklasse; konkrete Kontonummer in DATEV-Kontenrahmen-Dokumentation nachschlagen).

3. Differenz USt-Konto (z. B. SKR 03 1776) vs. USt-Voranmeldung 240 EUR.
   Ursache: vergessene Buchung am 30.04.2026.
   Korrektur: Nachbuchung mit Steuerschluessel 3 (Umsatz 19 Prozent).
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
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 239.
- AO §§ 146, 153.
- StBerG §§ 33, 57.
- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 2 ersetzt (DATEV-Kontonummern-Hinweise ohne Marker neu formuliert) -->
