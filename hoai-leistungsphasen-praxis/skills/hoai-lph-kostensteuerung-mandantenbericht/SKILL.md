---
name: hoai-lph-kostensteuerung-mandantenbericht
description: "LPH Kostensteuerung Mandantenbericht: bündelt 18 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# LPH Kostensteuerung Mandantenbericht

## Arbeitsbereich

Dieser Skill bündelt 18 sachlich verwandte Arbeitsschritte rund um **LPH Kostensteuerung Mandantenbericht** im Plugin HOAI-Leistungsphasen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-lph-05-kostensteuerung` | HOAI LPH 5 Ausführungsplanung: prüft Kostenermittlung, Kostenfortschreibung, Budgetwarnung und Änderungsfolgen; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-mandantenbericht` | HOAI LPH 5 Ausführungsplanung: erstellt verständlichen Statusbericht mit Ampel und nächstem Schritt; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-mangel-claim-vorsorge` | HOAI LPH 5 Ausführungsplanung: sichert spätere Mängel-, Behinderungs- und Nachtragskonflikte; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-nachtrag-und-change-request` | HOAI LPH 5 Ausführungsplanung: erkennt Planungsänderung, Zusatzleistung, Anordnung und Vergütungsfolge; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-oeffentlicher-auftraggeber` | HOAI LPH 5 Ausführungsplanung: berücksichtigt Vergabe, Haushaltsrecht, Fördermittel und Dokumentationspflicht; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-outputpaket` | HOAI LPH 5 Ausführungsplanung: liefert alle Dokumente, Tabellen und Entscheidungen für den Abschluss der Phase; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-planfreigabe-und-versionierung` | HOAI LPH 5 Ausführungsplanung: prüft Planindex, Freigaben, Verteiler und alte Planstände; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-qualitaetsgate` | HOAI LPH 5 Ausführungsplanung: erstellt ein Qualitygate, bevor die nächste Leistungsphase startet; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-rechnung-und-prueffaehigkeit` | HOAI LPH 5 Ausführungsplanung: prüft Abschlag, Schlussrechnung, Prüfbarkeit und Einwendungen; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-risikoregister` | HOAI LPH 5 Ausführungsplanung: baut Risiko-, Annahmen- und Entscheidungsregister; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-sachverstaendigen-pruefung` | HOAI LPH 5 Ausführungsplanung: übersetzt den LPH-Stand in Gutachterfragen und Prüfspur; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-schnittstelle-vob-bgb` | HOAI LPH 5 Ausführungsplanung: prüft VOB/B, Bauvertragsrecht und HOAI-Schnittstelle; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-streitfall-vorbereitung` | HOAI LPH 5 Ausführungsplanung: macht aus der Phase eine Prozess-/Schiedsgutachten- oder Vergleichsakte; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-terminsteuerung` | HOAI LPH 5 Ausführungsplanung: baut Terminlog, Fristen, Meilensteine, Puffer und Behinderungsrisiken; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-05-verbraucher-privater-bauherr` | HOAI LPH 5 Ausführungsplanung: erklärt Pflichten, Widerruf, Kostentransparenz und Verständlichkeit; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume. |
| `hoai-lph-06-abnahme-und-teilabnahme` | HOAI LPH 6 Vorbereitung der Vergabe: ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsanteil 10 % Gebäude / 7 % Innenräume. |
| `hoai-lph-06-anwaltlicher-pruefvermerk` | HOAI LPH 6 Vorbereitung der Vergabe: erstellt anwaltliches Kurzmemorandum zum LPH-Stand; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsanteil 10 % Gebäude / 7 % Innenräume. |
| `hoai-lph-06-bauherrnfreigabe` | HOAI LPH 6 Vorbereitung der Vergabe: strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsanteil 10 % Gebäude / 7 % Innenräume. |

## Arbeitsweg

Im Plugin HOAI-Leistungsphasen gilt für **LPH Kostensteuerung Mandantenbericht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hoai-lph-05-kostensteuerung`

**Fokus:** HOAI LPH 5 Ausführungsplanung: prüft Kostenermittlung, Kostenfortschreibung, Budgetwarnung und Änderungsfolgen; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Prüft kostenermittlung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft prüft Kostenermittlung, Kostenfortschreibung, Budgetwarnung und Änderungsfolgen im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 2. `hoai-lph-05-mandantenbericht`

**Fokus:** HOAI LPH 5 Ausführungsplanung: erstellt verständlichen Statusbericht mit Ampel und nächstem Schritt; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Erstellt verständlichen statusbericht mit ampel und nächstem schritt

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft erstellt verständlichen Statusbericht mit Ampel und nächstem Schritt im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 3. `hoai-lph-05-mangel-claim-vorsorge`

**Fokus:** HOAI LPH 5 Ausführungsplanung: sichert spätere Mängel-, Behinderungs- und Nachtragskonflikte; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Sichert spätere mängel-

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft sichert spätere Mängel-, Behinderungs- und Nachtragskonflikte im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 4. `hoai-lph-05-nachtrag-und-change-request`

**Fokus:** HOAI LPH 5 Ausführungsplanung: erkennt Planungsänderung, Zusatzleistung, Anordnung und Vergütungsfolge; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Erkennt planungsänderung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft erkennt Planungsänderung, Zusatzleistung, Anordnung und Vergütungsfolge im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 5. `hoai-lph-05-oeffentlicher-auftraggeber`

**Fokus:** HOAI LPH 5 Ausführungsplanung: berücksichtigt Vergabe, Haushaltsrecht, Fördermittel und Dokumentationspflicht; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Berücksichtigt vergabe

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft berücksichtigt Vergabe, Haushaltsrecht, Fördermittel und Dokumentationspflicht im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 6. `hoai-lph-05-outputpaket`

**Fokus:** HOAI LPH 5 Ausführungsplanung: liefert alle Dokumente, Tabellen und Entscheidungen für den Abschluss der Phase; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Liefert alle dokumente

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft liefert alle Dokumente, Tabellen und Entscheidungen für den Abschluss der Phase im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 7. `hoai-lph-05-planfreigabe-und-versionierung`

**Fokus:** HOAI LPH 5 Ausführungsplanung: prüft Planindex, Freigaben, Verteiler und alte Planstände; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Prüft planindex

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft prüft Planindex, Freigaben, Verteiler und alte Planstände im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 8. `hoai-lph-05-qualitaetsgate`

**Fokus:** HOAI LPH 5 Ausführungsplanung: erstellt ein Qualitygate, bevor die nächste Leistungsphase startet; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Erstellt ein qualitygate

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft erstellt ein Qualitygate, bevor die nächste Leistungsphase startet im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 9. `hoai-lph-05-rechnung-und-prueffaehigkeit`

**Fokus:** HOAI LPH 5 Ausführungsplanung: prüft Abschlag, Schlussrechnung, Prüfbarkeit und Einwendungen; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Prüft abschlag

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft prüft Abschlag, Schlussrechnung, Prüfbarkeit und Einwendungen im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 10. `hoai-lph-05-risikoregister`

**Fokus:** HOAI LPH 5 Ausführungsplanung: baut Risiko-, Annahmen- und Entscheidungsregister; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Baut risiko-

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft baut Risiko-, Annahmen- und Entscheidungsregister im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 11. `hoai-lph-05-sachverstaendigen-pruefung`

**Fokus:** HOAI LPH 5 Ausführungsplanung: übersetzt den LPH-Stand in Gutachterfragen und Prüfspur; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Übersetzt den lph-stand in gutachterfragen und prüfspur

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft übersetzt den LPH-Stand in Gutachterfragen und Prüfspur im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 12. `hoai-lph-05-schnittstelle-vob-bgb`

**Fokus:** HOAI LPH 5 Ausführungsplanung: prüft VOB/B, Bauvertragsrecht und HOAI-Schnittstelle; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Prüft vob/b

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft prüft VOB/B, Bauvertragsrecht und HOAI-Schnittstelle im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 13. `hoai-lph-05-streitfall-vorbereitung`

**Fokus:** HOAI LPH 5 Ausführungsplanung: macht aus der Phase eine Prozess-/Schiedsgutachten- oder Vergleichsakte; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Macht aus der phase eine prozess-/schiedsgutachten- oder vergleichsakte

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft macht aus der Phase eine Prozess-/Schiedsgutachten- oder Vergleichsakte im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 14. `hoai-lph-05-terminsteuerung`

**Fokus:** HOAI LPH 5 Ausführungsplanung: baut Terminlog, Fristen, Meilensteine, Puffer und Behinderungsrisiken; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Baut terminlog

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft baut Terminlog, Fristen, Meilensteine, Puffer und Behinderungsrisiken im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 15. `hoai-lph-05-verbraucher-privater-bauherr`

**Fokus:** HOAI LPH 5 Ausführungsplanung: erklärt Pflichten, Widerruf, Kostentransparenz und Verständlichkeit; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und Bewertungsanteil 25 % Gebäude / 30 % Innenräume.

# LPH 5 Ausführungsplanung: Erklärt pflichten

## Einsatz

Dieser Skill ist nur für **Leistungsphase 5 (Ausführungsplanung)** gedacht. Er prüft erklärt Pflichten, Widerruf, Kostentransparenz und Verständlichkeit im Kontext dieser Phase: durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung. Bewertungsanker für Gebäude/Innenräume: 25 % Gebäude / 30 % Innenräume.

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

## 16. `hoai-lph-06-abnahme-und-teilabnahme`

**Fokus:** HOAI LPH 6 Vorbereitung der Vergabe: ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsanteil 10 % Gebäude / 7 % Innenräume.

# LPH 6 Vorbereitung der Vergabe: Ordnet abnahme

## Einsatz

Dieser Skill ist nur für **Leistungsphase 6 (Vorbereitung der Vergabe)** gedacht. Er prüft ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB im Kontext dieser Phase: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur. Bewertungsanker für Gebäude/Innenräume: 10 % Gebäude / 7 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-6-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-6-Zweck: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-6-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 6

- Phase: Vorbereitung der Vergabe
- Praktischer Kern: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur
- Bewertungsanker Gebäude/Innenräume: 10 % Gebäude / 7 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 17. `hoai-lph-06-anwaltlicher-pruefvermerk`

**Fokus:** HOAI LPH 6 Vorbereitung der Vergabe: erstellt anwaltliches Kurzmemorandum zum LPH-Stand; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsanteil 10 % Gebäude / 7 % Innenräume.

# LPH 6 Vorbereitung der Vergabe: Erstellt anwaltliches kurzmemorandum zum lph-stand

## Einsatz

Dieser Skill ist nur für **Leistungsphase 6 (Vorbereitung der Vergabe)** gedacht. Er prüft erstellt anwaltliches Kurzmemorandum zum LPH-Stand im Kontext dieser Phase: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur. Bewertungsanker für Gebäude/Innenräume: 10 % Gebäude / 7 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-6-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-6-Zweck: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-6-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 6

- Phase: Vorbereitung der Vergabe
- Praktischer Kern: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur
- Bewertungsanker Gebäude/Innenräume: 10 % Gebäude / 7 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 18. `hoai-lph-06-bauherrnfreigabe`

**Fokus:** HOAI LPH 6 Vorbereitung der Vergabe: strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsanteil 10 % Gebäude / 7 % Innenräume.

# LPH 6 Vorbereitung der Vergabe: Strukturiert freigabeentscheidung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 6 (Vorbereitung der Vergabe)** gedacht. Er prüft strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche im Kontext dieser Phase: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur. Bewertungsanker für Gebäude/Innenräume: 10 % Gebäude / 7 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-6-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-6-Zweck: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-6-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 6

- Phase: Vorbereitung der Vergabe
- Praktischer Kern: Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur
- Bewertungsanker Gebäude/Innenräume: 10 % Gebäude / 7 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.
