---
name: jveg-dolmetscher-uebersetzer
description: "Verguetung fuer gerichtliche Dolmetscher und Uebersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Pruefraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Uebersetzung je Seite. Output: Verguetungsberechnung Dolmetscher und Uebersetzer. Abgrenzung: nicht Sachverstaendigenverguetung."
---

# JVEG-Dolmetscher-Uebersetzer

## Aufgabe
Prüfe die Vergütungsansprüche von Dolmetschern und Übersetzern nach §§ 13–16 JVEG auf Stundensatz, Textumfang, Reisezeiten und Terminlogik.

## Triage — kläre vor der Prüfung

1. **Tätigkeit:** Dolmetschen (mündlich, § 13 JVEG) oder Übersetzen (schriftlich, § 16 JVEG)?
2. **Sprachkombination:** Welche Sprache — liegt eine Sonderregelung für seltene Sprachen vor?
3. **Umfang:** Stunden (Dolmetscher) oder Zeilen/Normseiten (Übersetzer) — wie belegt?
4. **Reisezeit und Fahrtkosten:** Sind Reisezeiten als Wartezeit oder als Dolmetschzeit abgerechnet?
5. **Fristen:** Dreimonatsfrist § 23 JVEG gewahrt?

## Zentrale Normen
- § 13 JVEG (Dolmetscher — Stundensatz, Mindestdauer)
- § 14 JVEG (Zuschlag für besondere Leistungen)
- § 15 JVEG (Kürzung bei unvollständiger Tätigkeit)
- § 16 JVEG (Übersetzer — Vergütung nach Zeilen)
- §§ 5–7 JVEG (Fahrtkosten)
- § 23 JVEG (Dreimonatsfrist)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Auch bei Dolmetschern ist die vergütungsfähige Zeit objektiv zu bestimmen; reine Wartezeiten ohne Dolmetschleistung sind nicht erstattungsfähig.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Die Dreimonatsfrist des § 23 JVEG gilt auch für Dolmetscher und Übersetzer ohne Ausnahme.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Fahrtkosten für Dolmetscher werden nach denselben Wirtschaftlichkeitsgrundsätzen wie bei Sachverständigen geprüft.
4. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — Eine Abrechnung nach Übersetzungszeilen setzt die Vorlage des Ausgangstextes und die Angabe der Normzeilenanzahl voraus.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, §§ 13–16 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG §§ 13–16 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 13 Rn. 1 ff.

## Startet bei
Eingang einer Rechnung eines Dolmetschers oder Übersetzers im gerichtlichen Verfahren.

## Arbeitsweise
1. Tätigkeitsart abgrenzen (mündlich/schriftlich).
2. Ansatz auf Normkonformität prüfen (Stundensatz/Zeilenpreis).
3. Zeitnachweis oder Zeilennachweis prüfen.
4. Reisezeiten und Fahrtkosten separat prüfen.
5. Frist § 23 JVEG notieren.

## Output-Template

| Position | Geltend (EUR) | Norm | Prüfbefund | Anerkannt (EUR) |
|---|---|---|---|---|
| Dolmetschzeit [X Std.] | 00,00 | § 13 JVEG | [Befund] | 00,00 |
| Übersetzungszeilen [X] | 00,00 | § 16 JVEG | [Befund] | 00,00 |
| Fahrtkosten | 00,00 | § 5 JVEG | [Befund] | 00,00 |
| **Gesamt** | **00,00** | | | **00,00** |

**Fristenstatus § 23 JVEG:** [Fristende]

## Ausgabe
Positionsgenaues Prüfergebnis mit anerkanntem Betrag und Kürzungsbegründung.

## Leitplanken
- Wartezeiten ohne Dolmetschleistung nicht vergütungsfähig.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
