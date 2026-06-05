---
name: tk-netzneutralitaet-tk-nis2
description: "TK Netzneutralitaet TK Nis2: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Netzneutralitaet TK Nis2

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Netzneutralitaet TK Nis2** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-netzneutralitaet-zero-rating-throttling` | Netzneutralität: Zero-Rating, Priorisierung, Drosselung, Spezialdienste, Traffic Management und Beschwerde-/Abmahnrisiken. |
| `tk-nis2-kritis-bsi-schnittstelle` | NIS2/KRITIS/BSI-Anforderungen für TK-Unternehmen, Rechenzentren, Managed Services und kritische Kommunikation. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Netzneutralitaet TK Nis2**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-netzneutralitaet-zero-rating-throttling`

**Fokus:** Netzneutralität: Zero-Rating, Priorisierung, Drosselung, Spezialdienste, Traffic Management und Beschwerde-/Abmahnrisiken.

# Netzneutralität, Zero-Rating und Drosselung

## Einsatz

Für Anbieterprodukte und Beschwerden, wenn Datenverkehr unterschiedlich behandelt wird.

## Norm- und Quellenanker

EU-Verordnung 2015/2120; TKG; BEREC-Leitlinien live prüfen; UWG/GWB-Schnittstelle.

## Arbeitsfragen

1. Welche Verkehrsbehandlung unterscheidet wen oder was?
2. Ist sie technisch notwendig, diskriminierend oder tariflich gesteuert?
3. Gibt es Spezialdienst oder Netzmanagement?
4. Welche BNetzA-/BEREC-Linie ist live zu prüfen?

## Output

Netzneutralitätsprüfung, Produkt-Redline, BNetzA-Risiko und Kundenkommunikation.

## Red Flags

- Marketingtarif vor Rechtsprüfung
- Drosselung nach App-Kategorie
- Spezialdienst ohne Kapazitätsnachweis
- BEREC-Leitlinien nicht geprüft

## Anschluss-Skills

- tk-eu-eecc-router
- tk-missbrauchsaufsicht-sonderkartellrecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-nis2-kritis-bsi-schnittstelle`

**Fokus:** NIS2/KRITIS/BSI-Anforderungen für TK-Unternehmen, Rechenzentren, Managed Services und kritische Kommunikation.

# NIS2, KRITIS und BSI-Schnittstelle

## Einsatz

Für Unternehmen, die TK- oder digitale Infrastruktur betreiben.

## Norm- und Quellenanker

NIS2; BSI-Gesetz; TKG; DORA bei Finanzkunden.

## Arbeitsfragen

1. Ist die Einheit erfasst?
2. Welche technischen und organisatorischen Maßnahmen?
3. Welche Leitungsorganpflichten?

## Output

NIS2-Gap-Analyse und Maßnahmenplan.

## Red Flags

- Schwellenwerte ungeprüft
- Geschäftsführung nicht eingebunden
- Lieferkette vergessen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
