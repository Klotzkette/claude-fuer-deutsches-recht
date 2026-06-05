---
name: tk-missbrauchsaufsicht-tk-mitnutzung
description: "TK Missbrauchsaufsicht TK Mitnutzung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Missbrauchsaufsicht TK Mitnutzung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Missbrauchsaufsicht TK Mitnutzung** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-missbrauchsaufsicht-sonderkartellrecht` | Missbrauchsaufsicht im TK-Recht: Marktmacht, Diskriminierung, Behinderung, Margin Squeeze, Zugang und Verhältnis zu GWB/AEUV. |
| `tk-mitnutzung-gebaeude-netze` | Mitnutzung von Gebäudenetzen, Leerrohren, Masten, Schächten und passiver Infrastruktur. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Missbrauchsaufsicht TK Mitnutzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-missbrauchsaufsicht-sonderkartellrecht`

**Fokus:** Missbrauchsaufsicht im TK-Recht: Marktmacht, Diskriminierung, Behinderung, Margin Squeeze, Zugang und Verhältnis zu GWB/AEUV.

# TK-Missbrauchsaufsicht als Sonderkartellrecht

## Einsatz

Für Wettbewerberbeschwerden und Verteidigung von Netzbetreibern.

## Norm- und Quellenanker

TKG; GWB §§ 18–20; AEUV Art. 102; BNetzA/BKartA-Schnittstelle.

## Arbeitsfragen

1. Welche Marktstellung und Infrastrukturkontrolle?
2. Welche Behinderung/Diskriminierung ist konkret?
3. Ist BNetzA oder BKartA führend?

## Output

Missbrauchsmemo und Behördenstrategie.

## Red Flags

- Kartellbegriffe ohne TK-Norm
- keine Vergleichsgruppe
- Parallelzuständigkeit ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-mitnutzung-gebaeude-netze`

**Fokus:** Mitnutzung von Gebäudenetzen, Leerrohren, Masten, Schächten und passiver Infrastruktur.

# Mitnutzung von Gebäudenetzen und passiver Infrastruktur

## Einsatz

Für Ausbau ohne doppelten Tiefbau.

## Norm- und Quellenanker

TKG Mitnutzung; WEG/BGB; Infrastrukturatlas/BNetzA; Geschäftsgeheimnisse.

## Arbeitsfragen

1. Welche Infrastruktur existiert?
2. Wer darf sie nutzen und zu welchen Bedingungen?
3. Welche Sicherheits-/Kapazitätsgrenzen?

## Output

Mitnutzungsantrag und Entgelt-/Kapazitätsmatrix.

## Red Flags

- Eigentümer unklar
- Kapazität nur behauptet
- Geschäftsgeheimnisse nicht geschützt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
