---
name: hoai-lph-risikoregister-sachverstaendigen
description: "LPH Risikoregister Sachverstaendigen: bündelt 18 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# LPH Risikoregister Sachverstaendigen

## Arbeitsbereich

Dieser Skill bündelt 18 sachlich verwandte Arbeitsschritte rund um **LPH Risikoregister Sachverstaendigen** im Plugin HOAI-Leistungsphasen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-lph-04-risikoregister` | HOAI LPH 4 Genehmigungsplanung: baut Risiko-, Annahmen- und Entscheidungsregister; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume. |
| `hoai-lph-04-sachverstaendigen-pruefung` | HOAI LPH 4 Genehmigungsplanung: übersetzt den LPH-Stand in Gutachterfragen und Prüfspur; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume. |
| `hoai-lph-04-schnittstelle-vob-bgb` | HOAI LPH 4 Genehmigungsplanung: prüft VOB/B, Bauvertragsrecht und HOAI-Schnittstelle; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume. |
| `hoai-lph-04-streitfall-vorbereitung` | HOAI LPH 4 Genehmigungsplanung: macht aus der Phase eine Prozess-/Schiedsgutachten- oder Vergleichsakte; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume. |
| `hoai-lph-04-terminsteuerung` | HOAI LPH 4 Genehmigungsplanung: baut Terminlog, Fristen, Meilensteine, Puffer und Behinderungsrisiken; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume. |
| `hoai-lph-04-verbraucher-privater-bauherr` | HOAI LPH 4 Genehmigungsplanung: erklärt Pflichten, Widerruf, Kostentransparenz und Verständlichkeit; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume. |
| `hoai-lph-05-abnahme-und-teilabnahme` | HOAI LPH 5 Ausführungsplanung: ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-anwaltlicher-pruefvermerk` | HOAI LPH 5 Ausführungsplanung: erstellt anwaltliches Kurzmemorandum zum LPH-Stand; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-bauherrnfreigabe` | HOAI LPH 5 Ausführungsplanung: strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-bim-und-datenraum` | HOAI LPH 5 Ausführungsplanung: ordnet digitale Modelle, CDE, Planversionen und Zugriffsnachweise; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-dokumentation-und-belegakte` | HOAI LPH 5 Ausführungsplanung: sichert Protokolle, Planstände, Entscheidungen, Mails und Nachweise; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-fachplaner-schnittstellen` | HOAI LPH 5 Ausführungsplanung: koordiniert Architekt, TGA, Tragwerk, Brandschutz, Baugrund und Sonderplaner; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-foerdermittel-und-nachweis` | HOAI LPH 5 Ausführungsplanung: prüft Fördermittelbedingungen, Berichtspflichten und Kostenbelege; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-genehmigungen-und-auflagen` | HOAI LPH 5 Ausführungsplanung: ordnet öffentlich-rechtliche Auflagen und Genehmigungslasten; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-grundleistung-besondere-leistung` | HOAI LPH 5 Ausführungsplanung: grenzt HOAI-Grundleistung, Besondere Leistung und Zusatzauftrag ab; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-honorar-und-prozentwert` | HOAI LPH 5 Ausführungsplanung: prüft Bewertungsanteil, Honorarlogik, Basishonorarsatz und Abrechnung; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-input-und-zielcheck` | HOAI LPH 5 Ausführungsplanung: prüft Eingaben, Ziele, offene Entscheidungen und Mindestunterlagen; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-kommunikation-baustelle-behoerde` | HOAI LPH 5 Ausführungsplanung: formuliert klare E-Mails an Bauherr, Behörde, Unternehmer oder Fachplaner; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |

## Arbeitsweg

Im Plugin HOAI-Leistungsphasen gilt für **LPH Risikoregister Sachverstaendigen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hoai-lph-04-risikoregister`

**Fokus:** HOAI LPH 4 Genehmigungsplanung: baut Risiko-, Annahmen- und Entscheidungsregister; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume.

# LPH 4 Genehmigungsplanung: Baut risiko-

## Einsatz

Dieser Skill ist nur für **Leistungsphase 4 (Genehmigungsplanung)** gedacht. Er prüft baut Risiko-, Annahmen- und Entscheidungsregister im Kontext dieser Phase: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik. Bewertungsanker für Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-4-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-4-Zweck: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-4-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 4

- Phase: Genehmigungsplanung
- Praktischer Kern: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik
- Bewertungsanker Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 2. `hoai-lph-04-sachverstaendigen-pruefung`

**Fokus:** HOAI LPH 4 Genehmigungsplanung: übersetzt den LPH-Stand in Gutachterfragen und Prüfspur; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume.

# LPH 4 Genehmigungsplanung: Übersetzt den lph-stand in gutachterfragen und prüfspur

## Einsatz

Dieser Skill ist nur für **Leistungsphase 4 (Genehmigungsplanung)** gedacht. Er prüft übersetzt den LPH-Stand in Gutachterfragen und Prüfspur im Kontext dieser Phase: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik. Bewertungsanker für Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-4-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-4-Zweck: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-4-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 4

- Phase: Genehmigungsplanung
- Praktischer Kern: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik
- Bewertungsanker Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 3. `hoai-lph-04-schnittstelle-vob-bgb`

**Fokus:** HOAI LPH 4 Genehmigungsplanung: prüft VOB/B, Bauvertragsrecht und HOAI-Schnittstelle; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume.

# LPH 4 Genehmigungsplanung: Prüft vob/b

## Einsatz

Dieser Skill ist nur für **Leistungsphase 4 (Genehmigungsplanung)** gedacht. Er prüft prüft VOB/B, Bauvertragsrecht und HOAI-Schnittstelle im Kontext dieser Phase: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik. Bewertungsanker für Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-4-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-4-Zweck: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-4-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 4

- Phase: Genehmigungsplanung
- Praktischer Kern: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik
- Bewertungsanker Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 4. `hoai-lph-04-streitfall-vorbereitung`

**Fokus:** HOAI LPH 4 Genehmigungsplanung: macht aus der Phase eine Prozess-/Schiedsgutachten- oder Vergleichsakte; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume.

# LPH 4 Genehmigungsplanung: Macht aus der phase eine prozess-/schiedsgutachten- oder vergleichsakte

## Einsatz

Dieser Skill ist nur für **Leistungsphase 4 (Genehmigungsplanung)** gedacht. Er prüft macht aus der Phase eine Prozess-/Schiedsgutachten- oder Vergleichsakte im Kontext dieser Phase: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik. Bewertungsanker für Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-4-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-4-Zweck: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-4-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 4

- Phase: Genehmigungsplanung
- Praktischer Kern: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik
- Bewertungsanker Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 5. `hoai-lph-04-terminsteuerung`

**Fokus:** HOAI LPH 4 Genehmigungsplanung: baut Terminlog, Fristen, Meilensteine, Puffer und Behinderungsrisiken; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume.

# LPH 4 Genehmigungsplanung: Baut terminlog

## Einsatz

Dieser Skill ist nur für **Leistungsphase 4 (Genehmigungsplanung)** gedacht. Er prüft baut Terminlog, Fristen, Meilensteine, Puffer und Behinderungsrisiken im Kontext dieser Phase: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik. Bewertungsanker für Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-4-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-4-Zweck: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-4-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 4

- Phase: Genehmigungsplanung
- Praktischer Kern: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik
- Bewertungsanker Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 6. `hoai-lph-04-verbraucher-privater-bauherr`

**Fokus:** HOAI LPH 4 Genehmigungsplanung: erklärt Pflichten, Widerruf, Kostentransparenz und Verständlichkeit; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Bewertungsanteil 3 % Gebäude / 2 % Innenräume.

# LPH 4 Genehmigungsplanung: Erklärt pflichten

## Einsatz

Dieser Skill ist nur für **Leistungsphase 4 (Genehmigungsplanung)** gedacht. Er prüft erklärt Pflichten, Widerruf, Kostentransparenz und Verständlichkeit im Kontext dieser Phase: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik. Bewertungsanker für Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-4-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-4-Zweck: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-4-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 4

- Phase: Genehmigungsplanung
- Praktischer Kern: öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik
- Bewertungsanker Gebäude/Innenräume: 3 % Gebäude / 2 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 7. `hoai-lph-05-abnahme-und-teilabnahme`

**Fokus:** HOAI LPH 5 Ausführungsplanung: ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Ordnet abnahme

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 8. `hoai-lph-05-anwaltlicher-pruefvermerk`

**Fokus:** HOAI LPH 5 Ausführungsplanung: erstellt anwaltliches Kurzmemorandum zum LPH-Stand; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Erstellt anwaltliches kurzmemorandum zum lph-stand

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft erstellt anwaltliches Kurzmemorandum zum LPH-Stand im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 9. `hoai-lph-05-bauherrnfreigabe`

**Fokus:** HOAI LPH 5 Ausführungsplanung: strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Strukturiert freigabeentscheidung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 10. `hoai-lph-05-bim-und-datenraum`

**Fokus:** HOAI LPH 5 Ausführungsplanung: ordnet digitale Modelle, CDE, Planversionen und Zugriffsnachweise; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Ordnet digitale modelle

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft ordnet digitale Modelle, CDE, Planversionen und Zugriffsnachweise im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 11. `hoai-lph-05-dokumentation-und-belegakte`

**Fokus:** HOAI LPH 5 Ausführungsplanung: sichert Protokolle, Planstände, Entscheidungen, Mails und Nachweise; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Sichert protokolle

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft sichert Protokolle, Planstände, Entscheidungen, Mails und Nachweise im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 12. `hoai-lph-05-fachplaner-schnittstellen`

**Fokus:** HOAI LPH 5 Ausführungsplanung: koordiniert Architekt, TGA, Tragwerk, Brandschutz, Baugrund und Sonderplaner; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Koordiniert architekt

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft koordiniert Architekt, TGA, Tragwerk, Brandschutz, Baugrund und Sonderplaner im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 13. `hoai-lph-05-foerdermittel-und-nachweis`

**Fokus:** HOAI LPH 5 Ausführungsplanung: prüft Fördermittelbedingungen, Berichtspflichten und Kostenbelege; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Prüft fördermittelbedingungen

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft prüft Fördermittelbedingungen, Berichtspflichten und Kostenbelege im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 14. `hoai-lph-05-genehmigungen-und-auflagen`

**Fokus:** HOAI LPH 5 Ausführungsplanung: ordnet öffentlich-rechtliche Auflagen und Genehmigungslasten; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Ordnet öffentlich-rechtliche auflagen und genehmigungslasten

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft ordnet öffentlich-rechtliche Auflagen und Genehmigungslasten im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 15. `hoai-lph-05-grundleistung-besondere-leistung`

**Fokus:** HOAI LPH 5 Ausführungsplanung: grenzt HOAI-Grundleistung, Besondere Leistung und Zusatzauftrag ab; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Grenzt hoai-grundleistung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft grenzt HOAI-Grundleistung, Besondere Leistung und Zusatzauftrag ab im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 16. `hoai-lph-05-honorar-und-prozentwert`

**Fokus:** HOAI LPH 5 Ausführungsplanung: prüft Bewertungsanteil, Honorarlogik, Basishonorarsatz und Abrechnung; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Prüft bewertungsanteil

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft prüft Bewertungsanteil, Honorarlogik, Basishonorarsatz und Abrechnung im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 17. `hoai-lph-05-input-und-zielcheck`

**Fokus:** HOAI LPH 5 Ausführungsplanung: prüft Eingaben, Ziele, offene Entscheidungen und Mindestunterlagen; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Prüft eingaben

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft prüft Eingaben, Ziele, offene Entscheidungen und Mindestunterlagen im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 18. `hoai-lph-05-kommunikation-baustelle-behoerde`

**Fokus:** HOAI LPH 5 Ausführungsplanung: formuliert klare E-Mails an Bauherr, Behörde, Unternehmer oder Fachplaner; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Formuliert klare e-mails an bauherr

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft formuliert klare E-Mails an Bauherr, Behörde, Unternehmer oder Fachplaner im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-5-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-5-Zweck: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-5-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 5

- Phase: Ausführungsplanung
- Praktischer Kern: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung
- Bewertungsanker Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.
