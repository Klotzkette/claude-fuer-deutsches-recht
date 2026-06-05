---
name: anzeige-gegenanzeige-geldwaesche
description: "Anzeige Gegenanzeige Risiko, Anzeige Geldwaesche 261: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Anzeige Gegenanzeige Risiko, Anzeige Geldwaesche 261

## Arbeitsbereich

Dieser Skill bündelt **Anzeige Gegenanzeige Risiko, Anzeige Geldwaesche 261** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `anzeige-gegenanzeige-risiko` | Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Datenschutzverstoß oder Prozessbetrug. |
| `anzeige-geldwaesche-261` | Geldwäscheverdacht: Tatertrag, Verschleierung, Transaktionen, GwG-Verdachtsmeldung vs Strafanzeige. |

## Arbeitsweg

Für **Anzeige Gegenanzeige Risiko, Anzeige Geldwaesche 261** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `strafanzeige-vorbereiter` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

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
