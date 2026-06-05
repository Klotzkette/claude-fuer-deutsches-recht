---
name: tk-bundesnetzagentur-tk-zustaendigkeits
description: "TK Bundesnetzagentur TK Zustaendigkeits: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Bundesnetzagentur TK Zustaendigkeits

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **TK Bundesnetzagentur TK Zustaendigkeits** im Plugin Telekommunikationsrecht (TKG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-bundesnetzagentur-verfahren-akteneinsicht-fristen` | Verfahren vor der Bundesnetzagentur: Anhörung, Akteneinsicht, Geschäftsgeheimnisse, Beiladung, Fristen, Beschlusskammerlogik und gerichtliche Anschlussstrategie. |
| `tk-zustaendigkeits-router-bnetza-vg-lg` | Rechtsweg- und Zuständigkeitsrouter für TK-Streitigkeiten: Verbraucheranspruch, BNetzA-Regulierungsverfahren, zivilrechtlicher Vertrag, verwaltungsgerichtlicher Eilrechtsschutz und Kartell-/Missbrauchsschnittstelle. |

## Arbeitsweg

Im Plugin Telekommunikationsrecht (TKG) gilt für **TK Bundesnetzagentur TK Zustaendigkeits**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-bundesnetzagentur-verfahren-akteneinsicht-fristen`

**Fokus:** Verfahren vor der Bundesnetzagentur: Anhörung, Akteneinsicht, Geschäftsgeheimnisse, Beiladung, Fristen, Beschlusskammerlogik und gerichtliche Anschlussstrategie.

# BNetzA-Verfahren: Akteneinsicht, Anhörung, Fristen

## Einsatz

Der Skill begleitet regulierte Unternehmen und Wettbewerber durch BNetzA-Verfahren, ohne Akteneinsicht und Geheimnisschutz zu verschlampen.

## Norm- und Quellenanker

TKG; VwVfG §§ 28, 29; VwGO; Geschäftsgeheimnisgesetz; BNetzA-Verfahrenshinweise live prüfen.

## Arbeitsfragen

1. Welche Beschlusskammer/Einheit führt das Verfahren?
2. Wurde angehört, beigeladen oder beschieden?
3. Welche Aktenbestandteile sind geschwärzt oder geheimhaltungsbedürftig?
4. Welche Frist für Stellungnahme/Rechtsmittel läuft?

## Output

Verfahrensfahrplan, Akteneinsichtsantrag, Geheimnisschutzvermerk und Stellungnahmegliederung.

## Red Flags

- Anhörungsfrist verpasst
- Geschäftsgeheimnisse ungekennzeichnet
- Beiladung nicht beantragt
- Rechtsbehelfsbelehrung ignoriert

## Anschluss-Skills

- tk-eilrechtsschutz-bnetza-beschluss
- tk-behoerdenkommunikation-kooperationsstrategie

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-zustaendigkeits-router-bnetza-vg-lg`

**Fokus:** Rechtsweg- und Zuständigkeitsrouter für TK-Streitigkeiten: Verbraucheranspruch, BNetzA-Regulierungsverfahren, zivilrechtlicher Vertrag, verwaltungsgerichtlicher Eilrechtsschutz und Kartell-/Missbrauchsschnittstelle.

# Zuständigkeit: BNetzA, Verwaltungsgericht, Zivilgericht, Kartellspur

## Einsatz

Für Fälle, in denen unklar ist, ob man zur Bundesnetzagentur, zum Verwaltungsgericht, zum Amts-/Landgericht oder in eine kartellrechtliche Spur muss.

## Norm- und Quellenanker

TKG; VwGO; VwVfG; GVG/ZPO; GWB; AEUV Art. 101/102; Rechtsbehelfsbelehrung live prüfen.

## Arbeitsfragen

1. Welche Entscheidung/Handlung wird angegriffen?
2. Ist es Verwaltungsakt, Allgemeinverfügung, zivilrechtliche Rechnung oder Marktverhalten?
3. Welche Rechtsbehelfsbelehrung steht im Dokument?
4. Gibt es parallele Schlichtung oder Beschwerde?

## Output

Rechtsweg-Vermerk mit taktischem Parallelfahrplan und Fristenampel.

## Red Flags

- falsche Klageart
- Beschwerde ohne Hemmung
- zivilrechtliche Forderung als Regulierungsstreit behandelt
- Kartellspur übersehen

## Anschluss-Skills

- tk-verwaltungsrecht-anfechtung-bnetza
- tk-zivilklage-lg-entgelt-schadensersatz

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
