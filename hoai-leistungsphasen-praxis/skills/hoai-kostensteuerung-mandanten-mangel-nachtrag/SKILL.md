---
name: hoai-kostensteuerung-mandanten-mangel-nachtrag
description: "Kostensteuerung Mandanten Mangel Nachtrag: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kostensteuerung Mandanten Mangel Nachtrag

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Kostensteuerung Mandanten Mangel Nachtrag** im Plugin HOAI-Leistungsphasen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-lph-07-kostensteuerung` | HOAI LPH 7 Mitwirkung bei der Vergabe: prüft Kostenermittlung, Kostenfortschreibung, Budgetwarnung und Änderungsfolgen; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume. |
| `hoai-lph-07-mandantenbericht` | HOAI LPH 7 Mitwirkung bei der Vergabe: erstellt verständlichen Statusbericht mit Ampel und nächstem Schritt; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume. |
| `hoai-lph-07-mangel-claim-vorsorge` | HOAI LPH 7 Mitwirkung bei der Vergabe: sichert spätere Mängel-, Behinderungs- und Nachtragskonflikte; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume. |
| `hoai-lph-07-nachtrag-und-change-request` | HOAI LPH 7 Mitwirkung bei der Vergabe: erkennt Planungsänderung, Zusatzleistung, Anordnung und Vergütungsfolge; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume. |
| `hoai-lph-07-oeffentlicher-auftraggeber` | HOAI LPH 7 Mitwirkung bei der Vergabe: berücksichtigt Vergabe, Haushaltsrecht, Fördermittel und Dokumentationspflicht; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume. |

## Arbeitsweg

Im Plugin HOAI-Leistungsphasen gilt für **Kostensteuerung Mandanten Mangel Nachtrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hoai-lph-07-kostensteuerung`

**Fokus:** HOAI LPH 7 Mitwirkung bei der Vergabe: prüft Kostenermittlung, Kostenfortschreibung, Budgetwarnung und Änderungsfolgen; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume.

# LPH 7 Mitwirkung bei der Vergabe: Prüft kostenermittlung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 7 (Mitwirkung bei der Vergabe)** gedacht. Er prüft prüft Kostenermittlung, Kostenfortschreibung, Budgetwarnung und Änderungsfolgen im Kontext dieser Phase: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen. Bewertungsanker für Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-7-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-7-Zweck: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-7-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 7

- Phase: Mitwirkung bei der Vergabe
- Praktischer Kern: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen
- Bewertungsanker Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 2. `hoai-lph-07-mandantenbericht`

**Fokus:** HOAI LPH 7 Mitwirkung bei der Vergabe: erstellt verständlichen Statusbericht mit Ampel und nächstem Schritt; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume.

# LPH 7 Mitwirkung bei der Vergabe: Erstellt verständlichen statusbericht mit ampel und nächstem schritt

## Einsatz

Dieser Skill ist nur für **Leistungsphase 7 (Mitwirkung bei der Vergabe)** gedacht. Er prüft erstellt verständlichen Statusbericht mit Ampel und nächstem Schritt im Kontext dieser Phase: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen. Bewertungsanker für Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-7-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-7-Zweck: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-7-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 7

- Phase: Mitwirkung bei der Vergabe
- Praktischer Kern: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen
- Bewertungsanker Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 3. `hoai-lph-07-mangel-claim-vorsorge`

**Fokus:** HOAI LPH 7 Mitwirkung bei der Vergabe: sichert spätere Mängel-, Behinderungs- und Nachtragskonflikte; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume.

# LPH 7 Mitwirkung bei der Vergabe: Sichert spätere mängel-

## Einsatz

Dieser Skill ist nur für **Leistungsphase 7 (Mitwirkung bei der Vergabe)** gedacht. Er prüft sichert spätere Mängel-, Behinderungs- und Nachtragskonflikte im Kontext dieser Phase: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen. Bewertungsanker für Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-7-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-7-Zweck: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-7-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 7

- Phase: Mitwirkung bei der Vergabe
- Praktischer Kern: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen
- Bewertungsanker Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 4. `hoai-lph-07-nachtrag-und-change-request`

**Fokus:** HOAI LPH 7 Mitwirkung bei der Vergabe: erkennt Planungsänderung, Zusatzleistung, Anordnung und Vergütungsfolge; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume.

# LPH 7 Mitwirkung bei der Vergabe: Erkennt planungsänderung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 7 (Mitwirkung bei der Vergabe)** gedacht. Er prüft erkennt Planungsänderung, Zusatzleistung, Anordnung und Vergütungsfolge im Kontext dieser Phase: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen. Bewertungsanker für Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-7-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-7-Zweck: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-7-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 7

- Phase: Mitwirkung bei der Vergabe
- Praktischer Kern: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen
- Bewertungsanker Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 5. `hoai-lph-07-oeffentlicher-auftraggeber`

**Fokus:** HOAI LPH 7 Mitwirkung bei der Vergabe: berücksichtigt Vergabe, Haushaltsrecht, Fördermittel und Dokumentationspflicht; mit Fokus auf Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen und Bewertungsanteil 4 % Gebäude / 3 % Innenräume.

# LPH 7 Mitwirkung bei der Vergabe: Berücksichtigt vergabe

## Einsatz

Dieser Skill ist nur für **Leistungsphase 7 (Mitwirkung bei der Vergabe)** gedacht. Er prüft berücksichtigt Vergabe, Haushaltsrecht, Fördermittel und Dokumentationspflicht im Kontext dieser Phase: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen. Bewertungsanker für Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume.

## Arbeitsweise

1. Nimm zuerst nur den LPH-7-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-7-Zweck: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-7-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 7

- Phase: Mitwirkung bei der Vergabe
- Praktischer Kern: Angebotsprüfung, Bieterspiegel, Vergabevorschlag, Kostenanschlag und Vertragsunterlagen
- Bewertungsanker Gebäude/Innenräume: 4 % Gebäude / 3 % Innenräume
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.
