---
name: tk-zugangsregulierung-tk-zusammenschaltung
description: "TK Zugangsregulierung TK Zusammenschaltung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Zugangsregulierung TK Zusammenschaltung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Zugangsregulierung TK Zusammenschaltung** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-zugangsregulierung-vorleistung` | Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen. |
| `tk-zusammenschaltung-interconnection` | Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Zugangsregulierung TK Zusammenschaltung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-zugangsregulierung-vorleistung`

**Fokus:** Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen.

# Zugangsregulierung und Vorleistungen

## Einsatz

Für Wettbewerber, die Zugang brauchen, oder Netzbetreiber, die Zugangspflichten erfüllen müssen.

## Norm- und Quellenanker

TKG Zugangsregulierung; BNetzA-Standardangebote; GWB/AEUV.

## Arbeitsfragen

1. Welcher Zugang wird verlangt?
2. Ist Pflicht, freiwilliger Open Access oder Vertrag betroffen?
3. Welche technischen/kommerziellen Bedingungen sind streitig?

## Output

Zugangsantrag/Stellungnahme und Konditionenmatrix.

## Red Flags

- Nichtdiskriminierung nicht belegt
- technische Schnittstelle unklar
- Vertraulichkeit überdehnt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-zusammenschaltung-interconnection`

**Fokus:** Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung.

# Zusammenschaltung und Interconnection

## Einsatz

Für Netzbetreiber, MVNOs und Diensteanbieter bei Interconnection-Konflikten.

## Norm- und Quellenanker

TKG Zusammenschaltung; EECC; BNetzA-Streitbeilegung.

## Arbeitsfragen

1. Welche Netze/Dienste werden verbunden?
2. Welche technischen Spezifikationen und Entgelte gelten?
3. Welche Störung/Verweigerung liegt vor?

## Output

Interconnection-Matrix, Streitbeilegungsantrag und SLA-Check.

## Red Flags

- technische und rechtliche Ebene vermischt
- Terminierungsentgelt veraltet
- QoS nicht gemessen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
