---
name: tk-nummerierung-tk-open
description: "TK Nummerierung TK Open: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Nummerierung TK Open

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Nummerierung TK Open** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-nummerierung-rufnummernzuteilung` | Rufnummernzuteilung, Nutzung, Entzug, Mehrwertdienste, geografische Nummern, 0800/0900, M2M und Nummernportierung. |
| `tk-open-ran-lieferketten` | Open-RAN-/Netzkomponenten: Lieferkette, Sicherheit, Interoperabilität, Ausfall, Exportkontrolle und kritische Komponenten. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Nummerierung TK Open**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-nummerierung-rufnummernzuteilung`

**Fokus:** Rufnummernzuteilung, Nutzung, Entzug, Mehrwertdienste, geografische Nummern, 0800/0900, M2M und Nummernportierung.

# Nummerierung und Rufnummernzuteilung

## Einsatz

Für Anbieter und Dienste, deren Geschäftsmodell an Rufnummern hängt.

## Norm- und Quellenanker

TKG Nummerierungsrecht; BNetzA-Nummernpläne/Verfügungen live prüfen.

## Arbeitsfragen

1. Welche Nummernart und Nutzungsbedingung?
2. Ist Nutzung zweckgerecht?
3. Droht Entzug oder Abschaltung?

## Output

Nummernrechtsmemo und BNetzA-Antrag/Antwort.

## Red Flags

- Nummernart falsch
- Werbung/Missbrauch droht
- Zuteilungsinhaber und Nutzer verwechselt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-open-ran-lieferketten`

**Fokus:** Open-RAN-/Netzkomponenten: Lieferkette, Sicherheit, Interoperabilität, Ausfall, Exportkontrolle und kritische Komponenten.

# Open RAN und Lieferketten

## Einsatz

Für Netzmodernisierung und Vendor-Management.

## Norm- und Quellenanker

TKG; NIS2/BSI; IT-Sicherheitsgesetz; Außenwirtschaftsrecht; Vertragsrecht.

## Arbeitsfragen

1. Welche Komponenten und Lieferanten?
2. Welche Sicherheits-/Zertifizierungsanforderungen?
3. Welche Exit- und Interoperabilitätsrechte?

## Output

Lieferketten-Risikomemo und Vertragsklauseln.

## Red Flags

- Vendor Lock-in trotz Open RAN
- Sicherheitsnachweise fehlen
- Exportkontrollrisiko

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
