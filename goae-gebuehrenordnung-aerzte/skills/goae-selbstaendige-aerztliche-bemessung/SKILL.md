---
name: goae-selbstaendige-aerztliche-bemessung
description: "Selbstaendige Aerztliche Bemessung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Selbstaendige Aerztliche Bemessung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Selbstaendige Aerztliche Bemessung** im Plugin Goae Gebuehrenordnung Aerzte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `goae-4-selbstaendige-aerztliche-leistung-zielleistungsprinzip` | GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. |
| `goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle` | GOÄ § 5 Bemessung Gebührenrahmen 2 und 3 1 und 8 1 und 15 Schwelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. |
| `goae-5a-bemessung-im-basistarif` | GOÄ § 5a Bemessung im Basistarif: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. |

## Arbeitsweg

Im Plugin Goae Gebuehrenordnung Aerzte gilt für **Selbstaendige Aerztliche Bemessung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `goae-4-selbstaendige-aerztliche-leistung-zielleistungsprinzip`

**Fokus:** GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise.

# GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip

## Fachkern: GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip
- **Spezialgegenstand:** GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip** im Bereich **GOÄ Gebührenordnung für Ärzte**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Gebührenordnung für Ärzte mit Schwellenwerten, Steigerungssätzen, Analogabrechnung, Zielleistungsprinzip, Auslagen, Wahlleistungen, PKV/Beihilfe und Honorarstreit.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 2. `goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle`

**Fokus:** GOÄ § 5 Bemessung Gebührenrahmen 2 und 3 1 und 8 1 und 15 Schwelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise.

# GOÄ § 5 Bemessung Gebührenrahmen 2,3 1,8 1,15 Schwelle

## Fachkern: GOÄ § 5 Bemessung Gebührenrahmen 2,3 1,8 1,15 Schwelle
- **Spezialgegenstand:** GOÄ § 5 Bemessung Gebührenrahmen 2,3 1,8 1,15 Schwelle wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: GOÄ § 5 Bemessung Gebührenrahmen 2,3 1,8 1,15 Schwelle** im Bereich **GOÄ Gebührenordnung für Ärzte**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Gebührenordnung für Ärzte mit Schwellenwerten, Steigerungssätzen, Analogabrechnung, Zielleistungsprinzip, Auslagen, Wahlleistungen, PKV/Beihilfe und Honorarstreit.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 3. `goae-5a-bemessung-im-basistarif`

**Fokus:** GOÄ § 5a Bemessung im Basistarif: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise.

# GOÄ § 5a Bemessung im Basistarif

## Fachkern: GOÄ § 5a Bemessung im Basistarif
- **Spezialgegenstand:** GOÄ § 5a Bemessung im Basistarif wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: GOÄ § 5a Bemessung im Basistarif** im Bereich **GOÄ Gebührenordnung für Ärzte**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Gebührenordnung für Ärzte mit Schwellenwerten, Steigerungssätzen, Analogabrechnung, Zielleistungsprinzip, Auslagen, Wahlleistungen, PKV/Beihilfe und Honorarstreit.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
