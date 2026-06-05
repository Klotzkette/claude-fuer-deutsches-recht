---
name: tk-anschlussbereitstellung-tk
description: "TK Anschlussbereitstellung TK: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Anschlussbereitstellung TK

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Anschlussbereitstellung TK** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-anschlussbereitstellung-verzug` | Bereitstellung von Festnetz-, Glasfaser-, Mobilfunk- oder Business-Anschluss: Terminversäumnis, Verzug, Entschädigung, Rücktritt, Ersatzlösung und Beweis. |
| `tk-behoerdenkommunikation-kooperationsstrategie` | Kommunikationsstrategie gegenüber der Bundesnetzagentur: kooperativ, präzise, aktenfest, geheimnisschonend und entscheidungsorientiert. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Anschlussbereitstellung TK**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-anschlussbereitstellung-verzug`

**Fokus:** Bereitstellung von Festnetz-, Glasfaser-, Mobilfunk- oder Business-Anschluss: Terminversäumnis, Verzug, Entschädigung, Rücktritt, Ersatzlösung und Beweis.

# Anschlussbereitstellung und Verzug

## Einsatz

Für Fälle, in denen ein Anschluss nicht kommt, Technikertermine platzen oder der Anbieter zwischen Tiefbau, Hausverwaltung und Netzbetreiber verweist.

## Norm- und Quellenanker

TKG Kundenschutz §§ 51 ff. live prüfen; BGB §§ 280, 286, 323; ZPO; BNetzA-Verbraucherinformationen.

## Arbeitsfragen

1. Was wurde vertraglich zugesagt und bis wann?
2. Welche Termine wurden versäumt und wer hat sie bestätigt?
3. Ist Verbraucher- oder Geschäftskundenrecht betroffen?
4. Welche Ersatzkosten sind entstanden?

## Output

Verzugsfahrplan, Entschädigungsforderung, Rücktrittsoption und Belegmatrix.

## Red Flags

- Termin nur telefonisch vereinbart
- Hausanschluss/Tarifaktivierung verwechselt
- Verbraucherentschädigung und SLA nicht getrennt
- Mitwirkungspflicht des Kunden unklar

## Anschluss-Skills

- tk-stoerung-minderung-ausfallentschaedigung
- tk-glasfaser-hausanschluss-wegerecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-behoerdenkommunikation-kooperationsstrategie`

**Fokus:** Kommunikationsstrategie gegenüber der Bundesnetzagentur: kooperativ, präzise, aktenfest, geheimnisschonend und entscheidungsorientiert.

# Behördenkommunikation mit BNetzA

## Einsatz

Für regulierte Unternehmen und Beschwerdegegner.

## Norm- und Quellenanker

VwVfG; TKG; Geschäftsgeheimnisgesetz; Compliance-Dokumentation.

## Arbeitsfragen

1. Was ist Ziel der Kommunikation?
2. Welche Fakten sind gesichert?
3. Welche Geheimnisse sind zu markieren?

## Output

Kommunikationsleitfaden und Antwortentwurf.

## Red Flags

- zu viel freiwillige Information
- unklare Zusagen
- keine Aktennotiz

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
