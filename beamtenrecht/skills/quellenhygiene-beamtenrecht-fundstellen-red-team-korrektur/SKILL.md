---
name: quellenhygiene-beamtenrecht-fundstellen-red-team-korrektur
description: "Quellenhygiene-Red-Team für Beamten- und Richterrecht: erkennt verrutschte Fundstellen, private Datenbankzitate, falsche Entscheidungsdaten, Landesrechtsfallen und alte Rechtslage."
---

# Quellenhygiene im Beamten- und Richterrecht

## Aufgabe

Dieser Skill ist die Bremse, bevor eine scheinbar glänzende Antwort mit falscher Fundstelle herausgeht. Er prüft, ob Normen, Rechtsprechung und Landesrecht belegbar sind.

## Prüfliste

| Risiko | Kontrolle |
| --- | --- |
| BeckRS/juris-Blindzitat | Entfernen oder durch amtliche/freie Quelle ersetzen. |
| Falsches Gericht | Gericht, Datum, Aktenzeichen mit Fundstelle abgleichen. |
| Landesrecht verwechselt | Bundesland und amtliches Portal prüfen. |
| Alte Rechtslage | Reformdatum und Übergangsvorschriften prüfen. |
| Pressemitteilung statt Entscheidung | Entscheidung nachziehen oder Unsicherheit offenlegen. |
| Literatur als Rechtsquelle | Nicht als Beleg verwenden, allenfalls als nicht zitierte Arbeitsanregung. |

## Beamtenrechtliche Spezialfallen

- BBesG für Landesbeamte nach 2006.
- BeamtStG als Vollregelung für Laufbahn oder Versorgung.
- BDG 2024 auf Länderfälle übertragen.
- § 38 BDG ohne § 63 BDG-Rechtsschutz.
- Richterdienstgericht und Verwaltungsgericht verwechseln.
- alte Stalking-/Strafrechtslogik in Disziplinarfällen nebenbei mitschleppen.

## Ausgabeformat

Der Skill erzeugt eine Fundstellen-Tabelle:

| Behauptung | Quelle | Status | Handlung |
| --- | --- | --- | --- |
| ... | ... | verifiziert / unsicher / falsch | zitieren / live prüfen / entfernen |

## Harte Regel

Wenn Gericht, Datum und Aktenzeichen nicht zusammenpassen, wird nicht geraten. Der Skill formuliert dann: „Diese Fundstelle ist nicht belastbar; vor Verwendung amtlich oder frei verifizieren."
