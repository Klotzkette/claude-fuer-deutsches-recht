---
name: tk-marktanalyse-tk-meldepflicht
description: "TK Marktanalyse TK Meldepflicht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Marktanalyse TK Meldepflicht

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Marktanalyse TK Meldepflicht** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-marktanalyse-betraechtliche-marktmacht` | Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht, Konsultation, EU-Abstimmung und Regulierungsverfügung. |
| `tk-meldepflicht-it-sicherheitsvorfall` | Sicherheitsvorfälle bei TK-Anbietern: BNetzA/BSI/DSGVO-Meldungen, Kundenkommunikation, Ursachenanalyse und Abhilfe. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Marktanalyse TK Meldepflicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-marktanalyse-betraechtliche-marktmacht`

**Fokus:** Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht, Konsultation, EU-Abstimmung und Regulierungsverfügung.

# Marktanalyse und beträchtliche Marktmacht

## Einsatz

Für regulierte Märkte, in denen Zugang/Entgelt nur nach Marktmachtanalyse angeordnet werden kann.

## Norm- und Quellenanker

TKG Marktregulierung; EECC; BNetzA/BEREC/EU-Kommission live prüfen.

## Arbeitsfragen

1. Welcher relevante Markt ist betroffen?
2. Welche Marktanteile, Kontrolle über Infrastruktur und Wettbewerbsparameter liegen vor?
3. Welche Konsultation/Notifizierung läuft?

## Output

Marktanalyse-Memo und Stellungnahme.

## Red Flags

- Marktabgrenzung zu grob
- alte Regulierungsverfügung verwendet
- EU-Konsultation übersehen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-meldepflicht-it-sicherheitsvorfall`

**Fokus:** Sicherheitsvorfälle bei TK-Anbietern: BNetzA/BSI/DSGVO-Meldungen, Kundenkommunikation, Ursachenanalyse und Abhilfe.

# IT-Sicherheitsvorfall und Meldepflicht

## Einsatz

Für Incident Response im TK-Betrieb.

## Norm- und Quellenanker

TKG Sicherheitsvorschriften; BSI-Gesetz/NIS2; DSGVO Art. 33, 34.

## Arbeitsfragen

1. Was ist passiert und welche Dienste betroffen?
2. Welche Meldewege und Fristen?
3. Welche Sofortmaßnahmen?

## Output

Incident-Meldeplan und Vorstandsvorlage.

## Red Flags

- Meldung nur intern
- DSGVO und TKG nicht koordiniert
- Kundenkommunikation zu spät

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
