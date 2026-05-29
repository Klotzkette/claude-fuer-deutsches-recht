---
name: jveg-kommandocenter
description: "Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output: Navigationshinweis zum richtigen JVEG-Skill. Abgrenzung: kein inhaltlicher Berechnungs-Skill."
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
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
