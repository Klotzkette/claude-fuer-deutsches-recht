---
name: anzeige-muster-noetigung
description: "Anzeige Muster Noetigung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anzeige Muster Noetigung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anzeige Muster Noetigung** im Plugin Strafanzeige Vorbereiter. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-muster-strafanzeige-generator` | Erzeugt eine nüchterne Strafanzeige mit optionalem Strafantrag, Anlagen, Beweismatrix und Risikoformulierungen. |
| `anzeige-noetigung-240` | Nötigung prüfen: Gewalt/Drohung, empfindliches Übel, Verwerflichkeit, legitime Anzeigeandrohung vs. Missbrauch. |

## Arbeitsweg

Im Plugin Strafanzeige Vorbereiter gilt für **Anzeige Muster Noetigung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anzeige-muster-strafanzeige-generator`

**Fokus:** Erzeugt eine nüchterne Strafanzeige mit optionalem Strafantrag, Anlagen, Beweismatrix und Risikoformulierungen.

# Muster-Strafanzeige Generator

## Einsatz

Für Fälle, die nach Red-Team wirklich angezeigt werden sollen.

## Norm- und Quellenanker

StPO § 158; StGB § 77b; betroffene Straftatbestände.

## Arbeitsfragen

1. Welche Tatbestände nur als Verdacht?
2. Welche Anlagen?
3. Welche Ermittlungsanregungen?

## Output

fertiger Anzeigeentwurf.

## Red Flags

- Täter sicher behauptet ohne Beweis
- Antrag vergessen
- Anlagen fehlen

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-noetigung-240`

**Fokus:** Nötigung prüfen: Gewalt/Drohung, empfindliches Übel, Verwerflichkeit, legitime Anzeigeandrohung vs. Missbrauch.

# Nötigung § 240 StGB

## Einsatz

Für Drucksituationen.

## Norm- und Quellenanker

StGB § 240; BGB/Arbeitsrecht als Kontext.

## Arbeitsfragen

1. Welches Mittel?
2. Welcher Zweck?
3. Warum verwerflich?

## Output

Nötigungsprüfung und Anzeigeentwurf.

## Red Flags

- jede harte Verhandlung als Nötigung
- legitime Rechtsverfolgung verkannt
- Mittel-Zweck fehlt

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
