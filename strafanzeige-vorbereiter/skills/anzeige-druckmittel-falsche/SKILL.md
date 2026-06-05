---
name: anzeige-druckmittel-falsche
description: "Anzeige Druckmittel Falsche: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anzeige Druckmittel Falsche

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anzeige Druckmittel Falsche** im Plugin Strafanzeige Vorbereiter. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-druckmittel-verbot-noetigung` | Prüft, ob Drohung mit Strafanzeige oder Anzeige selbst als unzulässiges Druckmittel/Nötigung wirken kann. |
| `anzeige-falsche-verdaechtigung-164` | Warn- und Prüfskill zu § 164 StGB: niemanden sicher beschuldigen, wenn nur Verdachtsmomente oder Hörensagen vorliegen. |

## Arbeitsweg

Im Plugin Strafanzeige Vorbereiter gilt für **Anzeige Druckmittel Falsche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anzeige-druckmittel-verbot-noetigung`

**Fokus:** Prüft, ob Drohung mit Strafanzeige oder Anzeige selbst als unzulässiges Druckmittel/Nötigung wirken kann.

# Anzeige als Druckmittel vermeiden

## Einsatz

Für Vergleichs- und Forderungssituationen.

## Norm- und Quellenanker

StGB § 240; BGB § 138/242; Berufsrecht bei Anwälten.

## Arbeitsfragen

1. Ist Forderung berechtigt?
2. Ist Mittel-Zweck-Relation sauber?
3. Wie formulieren ohne Drohung?

## Output

Druckmittel-Risikoampel.

## Red Flags

- „Zahl sonst Anzeige“
- unberechtigte Forderung
- Öffentlichkeitsdrohung

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-falsche-verdaechtigung-164`

**Fokus:** Warn- und Prüfskill zu § 164 StGB: niemanden sicher beschuldigen, wenn nur Verdachtsmomente oder Hörensagen vorliegen.

# Falsche Verdächtigung § 164 StGB

## Einsatz

Für alle Anzeigen gegen benannte Personen.

## Norm- und Quellenanker

StGB § 164; StPO § 158; BGB § 823.

## Arbeitsfragen

1. Was weiß der Anzeigende sicher?
2. Welche entlastenden Umstände gibt es?
3. Muss gegen Unbekannt formuliert werden?

## Output

Risikoformulierung und Tatsachen-/Vermutungstrennung.

## Red Flags

- bewusst falscher Tätername
- Entlastendes verschwiegen
- Rachemotiv

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
