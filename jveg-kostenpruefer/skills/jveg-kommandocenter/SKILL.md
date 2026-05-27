---
name: jveg-kommandocenter
description: "Navigationszentrum fuer alle JVEG-Kostenpruefer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Pruefraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output: Navigationshinweis zum richtigen JVEG-Skill. Abgrenzung: kein inhaltlicher Berechnungs-Skill."
---

# JVEG-Kommandocenter

## Aufgabe
Erfasse alle Parameter eines JVEG-Kostenvorgangs und erstelle eine vollständige Kostenlandkarte, die den Prüfvorgang strukturiert und an die richtigen Spezial-Skills weiterleitet.

## Triage — kläre vor dem Start

1. **Anspruchsberechtigter:** Welche Rolle hat die Person (§ 2 JVEG)?
2. **Leistungsart:** Sachverständigengutachten, Dolmetscherleistung, Zeugnis, Übersetzung?
3. **Gewünschter Output:** Prüfmatrix, Antragsschreiben, Beschwerdeschrift oder Rechenblatt?
4. **Fristen:** Dreimonatsfrist § 23 JVEG — noch offen oder bereits versäumt?
5. **Vorschussstand:** Wurde ein Vorschuss gewährt, und wenn ja, in welcher Höhe?

## Speziallogik: Kostenlandkarte
Das Kommandocenter baut zu Beginn eine strukturierte Übersicht aller Anspruchspositionen:
- Jede Position wird einer Normengruppe zugeordnet.
- Offene Fragen und fehlende Belege werden markiert.
- Die Landkarte dient als Steuerungsgrundlage für nachgelagerte Skills.

## Zentrale Normen
- § 1 JVEG (Anwendungsbereich)
- § 2 JVEG (Anspruchsberechtigte)
- § 3 JVEG (Vorschuss)
- § 4 JVEG (Festsetzung)
- § 23 JVEG (Dreimonatsfrist)
- §§ 5–22 JVEG (Vergütungsgruppen)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Alle Vergütungspositionen sind voneinander unabhängig zu prüfen; ein Fehler bei einer Position infiziert nicht automatisch andere Positionen.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Eine umfassende Prüfung setzt voraus, dass alle Positionen vollständig erfasst sind; lückenhafte Antragstellung geht zu Lasten des Antragstellers.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Kostenprüfungen müssen strukturiert nach Normengruppen erfolgen; unsystematische Prüfung führt zu vermeidbaren Fehlern.
4. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — Die Weiterleitung an den zuständigen Kostenbeamten setzt die vollständige Dokumentation aller geltend gemachten Positionen voraus.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, § 1 Rn. 1 ff., § 2 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG Vor § 1 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG Vor § 1 Rn. 1 ff.

## Startet bei
Jeder neue JVEG-Kostenvorgang oder wenn Überblick über einen laufenden Vorgang gefragt ist.

## Arbeitsweise
1. Rolle und Anspruchsart nach § 2 JVEG klären.
2. Alle geltend gemachten Positionen erfassen.
3. Kostenlandkarte erstellen (Positionen → Normen → offene Punkte).
4. Frist § 23 JVEG prüfen.
5. An Spezial-Skills weiterleiten (Fahrtkosten, Sachverständige, Dolmetscher, Zeugen).

## Output-Template

**Kostenlandkarte — JVEG-Vorgang**

| Position | Betrag (EUR) | Norm | Beleg vorhanden | Spezialist-Skill |
|---|---|---|---|---|
| [Position 1] | 00,00 | § X JVEG | Ja/Nein | jveg-fahrtkosten |
| [Position 2] | 00,00 | § Y JVEG | Ja/Nein | jveg-sachverstaendigenrechnung |
| **Gesamtbetrag** | **00,00** | | | |

**Fristenstatus § 23 JVEG:** [Fristende TT.MM.JJJJ]
**Vorschussstand:** [EUR / Kein Vorschuss]
**Nächste Schritte:** [Skill-Weiterleitungen]

## Ausgabe
Vollständige Kostenlandkarte mit Normenzuordnung, Belegstatus und Skill-Routing.

## Leitplanken
- Kostenlandkarte immer zuerst; keine Position ohne Normbezug.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
