---
name: susa-haupt-und-personenkonten
description: "SuSa-Auswertung Hauptbuchkonten und Personenkonten separat auswerten. Anwendungsfall Prüfung Hauptbuch Sammelkonten 1400 1500 vs Personenkonten Debitoren Kreditoren OPOS. Methodik Konsistenz Hauptbuch zu Personenkonten Abstimmung. Output Vollabstimmung Hauptbuch Nebenbuch."
---

# Hauptbuchkonten und Personenkonten — Abstimmung

## Fachlicher Anker

- **Normen:** § 6a, § 239 HGB, § 238 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die SuSa zeigt einen Saldo auf dem Sammelkonto "Forderungen aus Lieferungen und Leistungen" (typisch SKR 03 1400). Die Detailebene mit Einzelkunden liegt im Nebenbuch in den Personenkonten (Debitorennummern-Bereich des aktuellen DATEV-Kontenrahmens beachten). Hauptbuch und Nebenbuch müssen abgestimmt sein — der Sammelkonto-Saldo muss mit der Summe der Personenkonten-Salden uebereinstimmen. Differenzen sind Fehler, die der Steuerberater aufspueren muss.

## Kaltstart-Rueckfragen

1. Welches Buchhaltungs-System — DATEV, Addison, Sage, BuchhaltungsButler?
2. Liegt eine Trennung Hauptbuch / Personenkonto vor, oder ist alles im Hauptbuch?
3. Welche Sammelkonten — nur Forderungen LuL und Verbindlichkeiten LuL, oder auch Banken, Steuern?
4. Liegen aktuelle Personen-OPOS-Listen vor?
5. Welche Periodizitaet der Abstimmung — monatlich, quartalsweise, jaehrlich?
6. Welche Differenzkriterien (in EUR und in Prozent)?
7. Welche Sondersituation (Massenbuchungen, Storno-Pauschalen)?
8. Welche Dokumentationspflicht (intern, Prüfer)?

## Rechtlicher Rahmen

### Primaernormen

**§ 239 HGB** — Form und Inhalt der Buchfuehrung; vollstaendig, geordnet, nachpruefbar.

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 146 AO** — Zeitgerechtigkeit und Vollstaendigkeit.

**§ 33 StBerG** — StB-Aufgabenkreis.

### Standards

- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.

## Workflow

### Phase 1 — Sammelkonten-Saldo aus SuSa

Typische SKR-03-Sammelkonten (Nummern beispielhaft; bei Abweichungen in der aktuellen DATEV-Kontenrahmenfassung nachschlagen):

```
1200 Bank [X]
1400 Forderungen LuL [X]
1700 Verbindlichkeiten LuL [X]
1576 Vorsteuer 19 Prozent [X]
1776 USt 19 Prozent [X]
```

### Phase 2 — Personenkonten-OPOS

- Debitoren-OPOS-Liste mit Salden aller Personenkonten.
- Kreditoren-OPOS-Liste mit Salden.
- Bank-Detail-Konten (oft separates Konto je Bank).

### Phase 3 — Abstimmung

| Position | Hauptbuch | Summe Personenkonten | Differenz |
|---|---|---|---|
| Forderungen LuL | [X] | [Y] | [Z] |
| Verbindlichkeiten LuL | [X] | [Y] | [Z] |
| Bank | [X] | [Y] | [Z] |

Differenzen müssen 0 sein. Bei Abweichung: Fehler im System (Buchung ohne Personenkonto-Zuordnung) oder Zeitversatz.

### Phase 4 — Differenzursachen

| Differenz-Typ | Ursache | Klärung |
|---|---|---|
| Saldo Hauptbuch > Personenkonten | Buchung direkt auf Sammelkonto ohne Personenzuordnung | Korrektur-Buchung mit Personenzuordnung |
| Saldo Hauptbuch < Personenkonten | Personenkonto mit Saldo, kein Hauptbuch-Eintrag | Buchung prüfen |
| Cut-off-Differenz | Zahlung am letzten Tag, Buchung Folgetag | Cut-off-Korrektur |
| Storno-Pauschale | Pauschal-Storno ohne Personenkonto | Personalisieren oder akzeptieren |

### Phase 5 — Korrekturmassnahmen

- Buchungen mit klarer Personenkonto-Zuordnung (Debitor: 10001, 10002 etc.).
- Bei "direkter Buchung Sammelkonto" durch Sachbearbeiter: Aufklaerung und Schulung.
- Cut-off-Korrekturen mit klarem Vermerk.

### Phase 6 — Prüfer-Vorbereitung

- Bei WP-Prüfung Abstimmungsprotokoll als Prüfungsunterlage.
- Bei BP-Prüfung Hauptbuch und OPOS-Listen gemeinsam vorlegen.
- Bei Mandantenwechsel Abstimmung als Übergabeunterlage.

## Strategie und Praxis-Tipps

- Hauptbuch-Nebenbuch-Abstimmung sollte monatlich erfolgen — nicht erst zum Jahresabschluss.
- Bei automatisierten Systemen (DATEV) sind Differenzen selten — bei manuellen Buchungen haeufig.
- Schulung der Sachbearbeiter: jede Buchung auf 1400/1500 braucht Personenkonto-Zuordnung.
- StBVV: Abstimmung in Buchfuehrungspauschale.
- DATEV-Tipp: DATEV-Auswertung "Sachkonten und Personenkonten" bietet automatische Differenzanzeige.
- Bei wiederholten Differenzen über 1.000 EUR: systemischer Fehler — Buchungslogik prüfen.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 239.
- AO § 146.
- StBerG § 33.
- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (Kontenrahmen-Hinweis ohne Marker neu formuliert) -->
