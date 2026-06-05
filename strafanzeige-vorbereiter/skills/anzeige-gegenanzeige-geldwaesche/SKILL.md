---
name: anzeige-gegenanzeige-geldwaesche
description: "Anzeige Gegenanzeige Geldwaesche: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anzeige Gegenanzeige Geldwaesche

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anzeige Gegenanzeige Geldwaesche** im Plugin Strafanzeige Vorbereiter. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-gegenanzeige-risiko` | Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Datenschutzverstoß oder Prozessbetrug. |
| `anzeige-geldwaesche-261` | Geldwäscheverdacht: Tatertrag, Verschleierung, Transaktionen, GwG-Verdachtsmeldung vs Strafanzeige. |

## Arbeitsweg

Im Plugin Strafanzeige Vorbereiter gilt für **Anzeige Gegenanzeige Geldwaesche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anzeige-gegenanzeige-risiko`

**Fokus:** Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Datenschutzverstoß oder Prozessbetrug.

# Gegenanzeige-Risiko

## Einsatz

Für konfliktgeladene Anzeigen.

## Norm- und Quellenanker

StGB §§ 164, 186, 187, 240, 263; DSGVO.

## Arbeitsfragen

1. Welche Gegenbehauptungen zu erwarten?
2. Welche eigene Schwachstelle?
3. Welche Formulierung minimiert Risiko?

## Output

Gegenanzeigen-Risikovermerk.

## Red Flags

- eigene Rolle verschwiegen
- Beweise manipuliert
- Dritte diffamiert

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-geldwaesche-261`

**Fokus:** Geldwäscheverdacht: Tatertrag, Verschleierung, Transaktionen, GwG-Verdachtsmeldung vs Strafanzeige.

# Geldwäsche § 261 StGB

## Einsatz

Für Unternehmen mit verdächtigen Zahlungsflüssen.

## Norm- und Quellenanker

StGB § 261; GwG; FIU/goAML; StPO.

## Arbeitsfragen

1. Welche Vortat/Quelle?
2. Welche Transaktion?
3. Besteht GwG-Meldepflicht?

## Output

Geldwäsche-Routing Anzeige/FIU.

## Red Flags

- FIU-Meldung durch Anzeige ersetzt
- Tipping-off Risiko
- eigene Rolle unklar

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
