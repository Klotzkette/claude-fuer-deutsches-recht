---
name: stb-susa-vorperiode-vergleich
description: "SuSa-Periodenvergleich Vormonat und Vorjahr. Anwendungsfall Pruefung Salden-Konsistenz Saldenentwicklung Vergleich der einzelnen Konten ueber Perioden. Methodik Differenz-Tabelle Auffaelligkeit Hinweis-Liste. Output SuSa mit Vergleichsspalten Auswertung Differenzen."
---

# SuSa-Periodenvergleich — Vormonat und Vorjahres-Periode

## Kernsachverhalt

Eine isolierte SuSa zeigt nur den Stichtag. Erst die Gegenueberstellung mit Vormonat oder Vorjahres-Periode zeigt Entwicklungen und Auffaelligkeiten. Konten mit ungewoehnlicher Saldenentwicklung deuten auf Buchungsfehler, geschaeftliche Aenderungen oder Krisensignale hin. Der Steuerberater nutzt den SuSa-Vergleich als Pruefinstrument im Monatsabschluss und im Jahresabschluss-Vorlauf.

## Kaltstart-Rueckfragen

1. Welcher Vergleich — Vormonat, Vorjahres-Monat, kumulierter YTD?
2. Welche Detailtiefe — alle Konten oder nur die wesentlichen?
3. Welche Schwellenwerte fuer Auffaelligkeit (absolute und prozentuale)?
4. Welche Sondereffekte sind herauszurechnen?
5. Welche Periodendefinitions (Kalender vs. abweichendes Wirtschaftsjahr)?
6. Welche Auswertungsfrequenz (monatlich vs. quartalsweise)?
7. Welche Verwendungszweck (interne Pruefung, Mandanten-Kommunikation)?
8. Welche Buchungs-Kontinuitaet vs. Aenderungen Kontenrahmen?

## Rechtlicher Rahmen

### Primaernormen

**§ 252 Abs. 1 Nr. 6 HGB** — Bewertungsstetigkeit; auch in der SuSa.

**§ 265 HGB** — Vergleichbarkeit der Vorjahreszahlen.

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 33 StBerG** — StB-Aufgabenkreis.

### Standards

- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.
- DATEV/Addison Periodenvergleichs-Module.

## Workflow

### Phase 1 — Datenbasis

- Aktuelle SuSa zur Periode X.
- Vorperiode-SuSa (Vormonat).
- Vorjahres-Periode-SuSa.
- Kontinuitaet pruefen (Kontenrahmen unveraendert).

### Phase 2 — Vergleichs-Tabelle

```
SUSA-VERGLEICH (Auszug)
Konto  Bezeichnung      Aktuell  Vormonat  Diff  Vorjahres-Periode  Diff
1200   Bank             [X]      [Y]       [Z]   [A]                [B]
1400   Forderungen      [X]      [Y]       [Z]   [A]                [B]
1500   Verbindl. LuL    [X]      [Y]       [Z]   [A]                [B]
1576   Vorsteuer 19     [X]      [Y]       [Z]   [A]                [B]
1776   USt 19           [X]      [Y]       [Z]   [A]                [B]
2000   Eigenkapital     [X]      [Y]       [Z]   [A]                [B]
4000   Erloese 19       [X]      [Y]       [Z]   [A]                [B]
5000   Wareneingang 19  [X]      [Y]       [Z]   [A]                [B]
6100   Lohn             [X]      [Y]       [Z]   [A]                [B]
...
```

### Phase 3 — Auffaelligkeits-Schwellen

| Schwelle absolut | Schwelle prozentual | Aktion |
|---|---|---|
| > 5.000 EUR | > 50 Prozent | Pruefung erforderlich |
| > 10.000 EUR | > 100 Prozent | Klaerung mit Mandant |
| > 50.000 EUR | > 200 Prozent | Sondergespraech |

### Phase 4 — Konten-Cluster-Analyse

- Bestandskonten: hohe Aenderung deutet auf Geschaeftsdynamik oder Buchungsfehler.
- Erfolgskonten: monatliche Saldenaenderung ist normal; aber Anomalien (Habensaldo Aufwand) deutet auf Fehlbuchung.
- USt-Konten: Vorsteuer und USt sollten in plausiblem Verhaeltnis stehen.
- Verrechnungskonten: sollten zeitnah auf null zurueck.

### Phase 5 — Auffaelligkeits-Liste

```
AUFFAELLIGKEITS-LISTE
1. Konto 4000 (Erloese 19): aktueller Monat [X] Soll-Saldo vs. Habensaldo Vormonat.
   Ursache vermuten: Gutschriften nicht erfasst?
   Klaerung: Belege durchsehen.

2. Konto 1590 (Verrechnungskonto): Saldo 12.500 EUR — kein Abbau.
   Ursache vermuten: nicht zugeordnete Bankbewegungen.
   Klaerung: GVC-Buchungen nachverfolgen.

3. Konto 6020 (Loehne): Anstieg 38 Prozent vs. Vorjahres-Monat.
   Ursache vermuten: neue Mitarbeiter oder Sonderzahlung.
   Klaerung: mit Lohnabrechnung abgleichen.
```

### Phase 6 — Korrektur und Reporting

- Korrektur-Buchungen mit klarem Vermerk.
- Auffaelligkeits-Liste in Mandantenakte.
- Bei wesentlichen Krisensignalen: Querverweis stb-bwa-sus-bilanz-pruefung.

## Output

- SuSa mit Vergleichsspalten Aktuell / Vormonat / Vorjahres-Periode.
- Auffaelligkeits-Liste mit Klaerungsmassnahmen.
- Korrektur-Protokoll.

## Strategie und Praxis-Tipps

- SuSa-Vergleich ist Standardpruefung im Monatsabschluss — nicht nur bei Jahresabschluss.
- Bei wiederholten Auffaelligkeiten auf demselben Konto: systemischer Fehler (Kontierungsregel falsch).
- Vergleichs-Schwellen mandantenabhaengig — bei Kleinmandanten geringere absolute Schwellen.
- Bei Wechsel des Kontenrahmens: Vergleich nicht moeglich ohne Brueckenposten.
- StBVV: Periodenvergleich in der Buchfuehrungspauschale.
- DATEV-Tipp: DATEV-Sachkontenauswertung mit Vergleichsspalten und automatischer Abweichungsmarkierung.

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-susa-formfehler-pruefen` — Pruefung.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — BWA-Vergleich.
- `stb-bwa-fehlerquellen-haeufig` — BWA-Fehler.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 265.
- StBerG § 33.
- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.
