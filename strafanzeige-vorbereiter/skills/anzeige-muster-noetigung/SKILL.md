---
name: anzeige-muster-noetigung
description: "Anzeige Muster Strafanzeige Generator, Anzeige Noetigung 240: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Anzeige Muster Strafanzeige Generator, Anzeige Noetigung 240

## Arbeitsbereich

Dieser Skill bündelt **Anzeige Muster Strafanzeige Generator, Anzeige Noetigung 240** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `anzeige-muster-strafanzeige-generator` | Erzeugt eine nüchterne Strafanzeige mit optionalem Strafantrag, Anlagen, Beweismatrix und Risikoformulierungen. |
| `anzeige-noetigung-240` | Nötigung prüfen: Gewalt/Drohung, empfindliches Übel, Verwerflichkeit, legitime Anzeigeandrohung vs. Missbrauch. |

## Arbeitsweg

Für **Anzeige Muster Strafanzeige Generator, Anzeige Noetigung 240** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `strafanzeige-vorbereiter` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

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
