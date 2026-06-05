---
name: tk-wholesale-tk-bauarbeiten
description: "TK Wholesale TK Bauarbeiten: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Wholesale TK Bauarbeiten

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Wholesale TK Bauarbeiten** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-wholesale-reseller-mvno-vertrag` | Wholesale-, Reseller- und MVNO-Verträge: Zugang, SLA, Entgelt, Nummerierung, Kundenschutz, Datenschutz und Exit. |
| `tk-bauarbeiten-kabelschaden` | Kabelschäden: Leitungsauskunft, Verkehrssicherung, Tiefbau, Schadensersatz, Betriebsunterbrechung und Beweissicherung. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Wholesale TK Bauarbeiten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-wholesale-reseller-mvno-vertrag`

**Fokus:** Wholesale-, Reseller- und MVNO-Verträge: Zugang, SLA, Entgelt, Nummerierung, Kundenschutz, Datenschutz und Exit.

# Wholesale, Reseller und MVNO-Verträge

## Einsatz

Für Anbieterketten im Mobilfunk/Festnetz.

## Norm- und Quellenanker

TKG; BGB/HGB; GWB; DSGVO/TKG-Datenschutz.

## Arbeitsfragen

1. Wer schuldet Endkundenleistung?
2. Welche Vorleistungen/SLA?
3. Welche Daten- und Nummernverantwortung?

## Output

Vertrags-Redline und Risikoampel.

## Red Flags

- Endkundenpflichten fehlen
- Nummernportierung ungeklärt
- SLA ohne Sanktion

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-bauarbeiten-kabelschaden`

**Fokus:** Kabelschäden: Leitungsauskunft, Verkehrssicherung, Tiefbau, Schadensersatz, Betriebsunterbrechung und Beweissicherung.

# Kabelschaden durch Bauarbeiten

## Einsatz

Für Netzbetreiber, Bauunternehmen und Versicherer.

## Norm- und Quellenanker

BGB §§ 823, 280; TKG Infrastruktur; Straßen-/Baurecht; ZPO.

## Arbeitsfragen

1. Wurde Leitungsauskunft eingeholt?
2. Welche Pläne und Markierungen?
3. Welcher Schaden und Folgeschaden?

## Output

Kabelschaden-Dossier und Anspruchsschreiben.

## Red Flags

- Leitungspläne veraltet
- Folgeschäden unbelegt
- Subunternehmerkette unklar

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
