---
name: bim-modell-kostenobergrenze-budget-lph
description: "BIM Modell Kostenobergrenze Budget LPH: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# BIM Modell Kostenobergrenze Budget LPH

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **BIM Modell Kostenobergrenze Budget LPH** im Plugin HOAI-Leistungsphasen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-bim-modell-planstand-cde-haftung` | HOAI-Fachfrage: BIM, Common Data Environment, Modellstand, Planfreigabe, Kollisionsprüfung, Datenhoheit, Auftraggeber-Informationsanforderungen und Haftung im digitalen Planen prüfen. |
| `hoai-kostenobergrenze-budget-haftung` | HOAI-Fachfrage: Baukostenobergrenze, Budget, Kostenrahmen, Beschaffenheitsvereinbarung und Architektenhaftung nach BGH VII ZR 395/01 und VII ZR 185/13 mit Beweislast und Dolo-agit-Einwand prüfen. |
| `hoai-lph-01-haftungsfalle` | HOAI LPH 1 Grundlagenermittlung: identifiziert typische Haftungsrisiken und Beweisvorsorge; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |
| `hoai-lph-02-haftungsfalle` | HOAI LPH 2 Vorplanung: identifiziert typische Haftungsrisiken und Beweisvorsorge; mit Fokus auf Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrundlage und Bewertungsanteil 7 %. |
| `hoai-lph-03-haftungsfalle` | HOAI LPH 3 Entwurfsplanung: identifiziert typische Haftungsrisiken und Beweisvorsorge; mit Fokus auf stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung und Bewertungsanteil 15 %. |

## Arbeitsweg

Im Plugin HOAI-Leistungsphasen gilt für **BIM Modell Kostenobergrenze Budget LPH**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hoai-bim-modell-planstand-cde-haftung`

**Fokus:** HOAI-Fachfrage: BIM, Common Data Environment, Modellstand, Planfreigabe, Kollisionsprüfung, Datenhoheit, Auftraggeber-Informationsanforderungen und Haftung im digitalen Planen prüfen.

# BIM, CDE Und Planstandshaftung

## Einsatz

Dieses Fachmodul bei digitalen Modellen, CDE, BIM-Abwicklungsplan, Kollisionsprüfung oder Streit, ob Modell oder 2D-Plan maßgeblich war.

## Normanker

- HOAI-Leistungsbild bleibt leistungsbezogen; BIM-Leistungen können besondere Leistungen oder vertraglich konkretisierte Grundleistungen sein.
- § 650p BGB für Planungsziele.

## Prüffragen

1. Gibt es AIA, BAP, Modellstruktur, Freigabeprozess?
2. Was ist vertraglich führend: Modell, Plan, LV, Protokoll?
3. Wer prüft Kollisionen und in welchem Detaillierungsgrad?
4. Wurden Modellstände versioniert und verteilt?
5. Entsteht Mehrleistung durch BIM-Koordination oder nur andere Arbeitsmethode?

## Output

BIM-Risikoblatt mit Datenstand, Freigaben, Kollisionsliste, Verantwortlichen und Honorar-/Haftungshinweis.

## 2. `hoai-kostenobergrenze-budget-haftung`

**Fokus:** HOAI-Fachfrage: Baukostenobergrenze, Budget, Kostenrahmen, Beschaffenheitsvereinbarung und Architektenhaftung nach BGH VII ZR 395/01 und VII ZR 185/13 mit Beweislast und Dolo-agit-Einwand prüfen.

# Kostenobergrenze, Budget Und Haftung

## Einsatz

Dieses Fachmodul greift, wenn Bauherr und Planer darüber streiten, ob eine Zahl nur Budgetwunsch, Kostenrahmen, Fördermittelgrenze, Kostenobergrenze oder verbindliche Beschaffenheitsvereinbarung war.

## Rechtsprechungsanker

- BGH, Urteil vom 13.02.2003, VII ZR 395/01: Eine Bausumme im Bauantrag wird nicht allein durch Unterschrift zur Baukostenobergrenze.
- BGH, Urteil vom 06.10.2016, VII ZR 185/13: Baukostenobergrenze kann Haftung auslösen; Beweislast und Honorarfolge sauber prüfen.

## Prüffragen

1. Wer hat die Zahl wann formuliert?
2. Stand sie im Vertrag, Protokoll, Förderbescheid, Kostenberechnung, Bauantrag oder nur in einer E-Mail?
3. Wurde sie als zwingend, Ziel, Obergrenze, Wunsch oder Schätzung bezeichnet?
4. Hat der Planer bei Kostensteigerungen gewarnt?
5. Gibt es Bauherrnänderungen, Baupreissteigerungen oder Genehmigungsauflagen?

## Output

Baue eine Chronologie aus Zahl, Quelle, Rechtsqualität, Warnung, Freigabe und Schaden. Ergebnis: "Obergrenze wahrscheinlich", "nur Budgetindikator" oder "Beweis offen".

## 3. `hoai-lph-01-haftungsfalle`

**Fokus:** HOAI LPH 1 Grundlagenermittlung: identifiziert typische Haftungsrisiken und Beweisvorsorge; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %.

# LPH 1 Grundlagenermittlung: Identifiziert typische haftungsrisiken und beweisvorsorge

## Einsatz

Dieser Skill ist nur für **Leistungsphase 1 (Grundlagenermittlung)** gedacht. Er prüft identifiziert typische Haftungsrisiken und Beweisvorsorge im Kontext dieser Phase: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren. Bewertungsanker für Gebäude/Innenräume: 2 %.

## Arbeitsweise

1. Nimm zuerst nur den LPH-1-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-1-Zweck: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-1-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 1

- Phase: Grundlagenermittlung
- Praktischer Kern: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren
- Bewertungsanker Gebäude/Innenräume: 2 %
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 4. `hoai-lph-02-haftungsfalle`

**Fokus:** HOAI LPH 2 Vorplanung: identifiziert typische Haftungsrisiken und Beweisvorsorge; mit Fokus auf Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrundlage und Bewertungsanteil 7 %.

# LPH 2 Vorplanung: Identifiziert typische haftungsrisiken und beweisvorsorge

## Einsatz

Dieser Skill ist nur für **Leistungsphase 2 (Vorplanung)** gedacht. Er prüft identifiziert typische Haftungsrisiken und Beweisvorsorge im Kontext dieser Phase: Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrundlage. Bewertungsanker für Gebäude/Innenräume: 7 %.

## Arbeitsweise

1. Nimm zuerst nur den LPH-2-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-2-Zweck: Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrundlage.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-2-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 2

- Phase: Vorplanung
- Praktischer Kern: Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrundlage
- Bewertungsanker Gebäude/Innenräume: 7 %
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 5. `hoai-lph-03-haftungsfalle`

**Fokus:** HOAI LPH 3 Entwurfsplanung: identifiziert typische Haftungsrisiken und Beweisvorsorge; mit Fokus auf stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung und Bewertungsanteil 15 %.

# LPH 3 Entwurfsplanung: Identifiziert typische haftungsrisiken und beweisvorsorge

## Einsatz

Dieser Skill ist nur für **Leistungsphase 3 (Entwurfsplanung)** gedacht. Er prüft identifiziert typische Haftungsrisiken und Beweisvorsorge im Kontext dieser Phase: stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung. Bewertungsanker für Gebäude/Innenräume: 15 %.

## Arbeitsweise

1. Nimm zuerst nur den LPH-3-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-3-Zweck: stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-3-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 3

- Phase: Entwurfsplanung
- Praktischer Kern: stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung
- Bewertungsanker Gebäude/Innenräume: 15 %
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.
