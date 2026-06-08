---
name: rechenblatt
description: "JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares Rechenblatt JVEG. Abgrenzung: nicht Antragsgenerator im Jveg Kostenpruefer."
---

# JVEG-Rechenblatt

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: JVEG-Rechenblatt
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Triage — kläre vor der Erstellung

1. **Positionen:** Welche Vergütungspositionen sollen im Rechenblatt erfasst werden?
2. **Honorargruppe:** Bei Sachverständigen — welche Honorargruppe nach § 9 JVEG?
3. **Zeitnachweise:** Liegen dokumentierte Zeitangaben (Beginn/Ende) für die Tätigkeit vor?
4. **Kappungsgrenzen:** Gibt es Höchstbeträge (z.B. Tagesgeld, Übernachtungspauschale)?
5. **Vorschussabzug:** Ist ein bereits ausgezahlter Vorschuss in Abzug zu bringen?

## Zentrale Normen
- § 8 JVEG (Sachverständigenvergütung — Stundensatz)
- § 9 JVEG (Honorargruppen-Tabelle)
- § 10 JVEG (Reisezeit)
- § 5 JVEG (Fahrtkosten — Kilometer × Satz)
- § 11 JVEG (Übernachtungsgeld — Kappungsgrenze)
- § 12 JVEG (Tagegeld)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Startet bei
Fertigstellung der Positionserfassung (jveg-aktenstripper); vor Antragserstellung.

## Output-Template

| Position | Norm | Eingabewert | Kappung | Rechenschritt | Beleg | Ergebnis (EUR) |
|---|---|---|---|---|---|---|
| Stunden Honorar [X Std. × Y EUR] | § 8 i.V.m. § 9 JVEG | X Std. | — | X × Y = | Anlage 1 | 00,00 |
| Reisezeit [X Std. × Y EUR] | § 10 JVEG | X Std. | — | X × Y = | Anlage 2 | 00,00 |
| Fahrtkosten [X km × Y EUR] | § 5 JVEG | X km | — | X × Y = | Anlage 3 | 00,00 |
| Übernachtung | § 11 JVEG | 1 Nacht | 00,00 EUR | Beleg | Anlage 4 | 00,00 |
| **Brutto** | | | | | | **00,00** |
| ./. Vorschuss | § 3 JVEG | | | | | -00,00 |
| **Restforderung** | | | | | | **00,00** |

## Ausgabe
Vollständiges Rechenblatt; dient als Anlage zum Festsetzungsantrag.

## Leitplanken
- Jede Zeile braucht Norm + Beleg; leere Felder blockieren die Ausgabe.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

