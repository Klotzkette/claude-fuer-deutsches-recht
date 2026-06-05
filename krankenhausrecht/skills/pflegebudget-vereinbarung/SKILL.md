---
name: pflegebudget-vereinbarung
description: "Pflegebudget Vereinbarung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pflegebudget Vereinbarung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pflegebudget Vereinbarung** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pflegebudget-vereinbarung-nachweis-risiken` | Pflegebudget nach § 17 KHEntgG / Pflegepersonalkostenausgliederung: Berechnung, Nachweis, Pflegeentgeltwert, MD-Strukturpruefung, Schiedsstellenrisiken und Reformbezuege (PPR 2.0). |
| `planfeststellungsbescheid-rechtsbehelf-und-eilrechtsschutz` | Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `privatisierung-betriebsuebergang-traegerwechsel` | Privatisierung Betriebsübergang Trägerwechsel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Pflegebudget Vereinbarung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pflegebudget-vereinbarung-nachweis-risiken`

**Fokus:** Pflegebudget nach § 17 KHEntgG / Pflegepersonalkostenausgliederung: Berechnung, Nachweis, Pflegeentgeltwert, MD-Strukturpruefung, Schiedsstellenrisiken und Reformbezuege (PPR 2.0).

# Pflegebudget Vereinbarung Nachweis Risiken

## Fachkern: Pflegebudget Vereinbarung Nachweis Risiken
- **Spezialgegenstand:** Pflegebudget Vereinbarung Nachweis Risiken. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Das Pflegebudget ist seit 2020 aus den DRG ausgegliedert (frueher § 6a KHEntgG, jetzt im neugefassten KHEntgG abgebildet). Pflegepersonalkosten werden gesondert verhandelt; der Pflegeentgeltwert wird budgetbasiert berechnet. PPR 2.0 (§ 137k SGB V) konkretisiert die Personalbemessung schrittweise.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Liegt Pflegepersonalkostennachweis (PpUKN) aktualisiert vor?
- Ist Pflegeentgeltwert verhandelt oder strittig?
- Welche Bereiche zaehlen pflegerisch (Tarifgruppen, ausgegliederte Bereiche)?
- Drohen MD-Strukturpruefung oder Schiedsstellenverfahren?
- Greift PPR 2.0 schon konkret oder im Uebergang?

## Rechtlicher Rahmen
- **KHEntgG § 17** Pflegepersonalkosten und Pflegeentgeltwert.
- **KHEntgG § 4** Erloesbudget; Pflegebudget separat.
- **SGB V § 137k** PPR 2.0-Konkretisierung.
- **PpUGV** Pflegeuntergrenzen (parallel; gleiche Personalbasis).
- **InEK-Datenlieferung** Pflegepersonalkostennachweis.
- **KHG § 18a** Schiedsstelle bei Dissens.

## / Schritt fuer Schritt
1. **Pflegepersonalkostennachweis (PpUKN) erstellen:** Beruecksichtigte Berufsgruppen, Tarifgruppen, Kosten je Vollkraft.
2. **Bereinigung:** Was zaehlt zum Pflegebudget (bettenbezogene Pflege), was nicht (OP-Pflege, Intensivpflege je nach Vorgabe).
3. **Pflegeentgeltwert berechnen:** Pflegebudget / Pflegetage (DRG-Pflegetage als Verteilungsbasis).
4. **Verhandlung mit Kassen:** Plausibilitaet, Tarifsteigerungen, Personalaufstockung.
5. **MD-Strukturpruefung beobachten:** Pflegepersonal in pflegesensitiven Bereichen muss PpUGV erfuellen.
6. **PPR 2.0 antizipieren:** Personalbemessung nach Versorgungskategorien; schrittweise Einfuehrung.
7. **Schiedsstelle bei Dissens:** § 18a KHG, separates Verfahren.

## Trade-off-Matrix

| Forderung | Argument | Risiko |
|---|---|---|
| Tarifsteigerung voll geltend machen | Tarifvertrag, Personalentwicklung | Kassen pruefen Plausibilitaet |
| Aufstockung Pflegepersonal | Versorgungsqualitaet | Plausibilitaet, Strukturpruefung |
| Bereinigung um OP-Pflege | KHEntgG-Vorgabe | Auslegungsstreit |
| Schiedsstelle anrufen | objektive Drittentscheidung | Verfahrenskosten |

## Praxistipps
- Pflegebudget wird tarifbedingt jaehrlich angepasst — TVoeD-/AVR-Tariferhoehung Pflicht-Input.
- InEK-Datenlieferung zur Pflegepersonalkostenmeldung Quartalsweise — Fristen wahren.
- PpUGV-Quoten und Pflegebudget sind verbunden: Untergrenz-Verletzung gefaehrdet Budget.
- PPR 2.0 wird Personalbemessung ueber Versorgungskategorien (A, S, T) konkretisieren — Live-Check g-ba.de.
- Ausgliederung OP-Pflege ist Streitpunkt; § 17 KHEntgG konkretisiert.

## Mustertexte
**PpUKN-Begruendung:**
> Anlage: Pflegepersonalkostennachweis 2026. Berechnung: Vollkraftaequivalente x Tarifsatz x Bereinigungsfaktor (OP/Funktionsdienste ausgegliedert). Tarifsteigerung TVoeD: …. Aufstockung gemaess Personalplanung: …. Gesamtsumme: …

**Schiedsantrag Pflegebudget:**
> Wir beantragen Festsetzung des Pflegebudgets 2026 auf [EUR]. Pflegeentgeltwert: [EUR] / Pflegetag. Begruendung: PpUKN, Tarifsteigerung, Personalentwicklung. Anlagen: PpUKN, Tarifvertrag, InEK-Meldung.

## Typische Fehler
- Pflegebudget mit Erloesbudget vermischen.
- OP-Pflege/Funktionsdienste nicht korrekt ausgegliedert.
- Tarifsteigerung doppelt geltend gemacht.
- PpUGV-Verletzung nicht in Plausibilitaet einbezogen.
- Frist InEK-Meldung versaeumt.

## Querverweise
- `khentgg-budgetverhandlung-drg-pepp-abgrenzung`
- `personaluntergrenzen-pflege-ppugv`
- `vorhalteverguetung-leistungsgruppen-krankenhausreform`
- `schiedsstellenverfahren-krankenhausentgelt`
- `klage-gegen-budgetbescheid-oder-schiedsstellenentscheidung`
- `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung`

## Quellen Stand 06/2026
- KHEntgG § 17 i. d. F. KHVVG.
- SGB V § 137k (PPR 2.0).
- PpUGV.
- InEK-Datenlieferungsvereinbarungen (Live-Check g-drg.de).
- BSG, staend. Rspr. zu Pflegebudget und Pflegeentgeltwert.
- KHG § 18a (Schiedsstelle).

## 2. `planfeststellungsbescheid-rechtsbehelf-und-eilrechtsschutz`

**Fokus:** Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz

## Fachkern: Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz
- **Spezialgegenstand:** Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Krankenhausrecht zwischen KHG, KHEntgG, SGB V, Landeskrankenhausrecht, G-BA-Vorgaben, Krankenhausreform, MD-Prüfung, Budgetverhandlung und Klinik-Compliance.

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

## 3. `privatisierung-betriebsuebergang-traegerwechsel`

**Fokus:** Privatisierung Betriebsübergang Trägerwechsel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Privatisierung Betriebsübergang Trägerwechsel

## Fachkern: Privatisierung Betriebsübergang Trägerwechsel
- **Spezialgegenstand:** Privatisierung Betriebsübergang Trägerwechsel. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Privatisierung Betriebsübergang Trägerwechsel** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Krankenhausrecht zwischen KHG, KHEntgG, SGB V, Landeskrankenhausrecht, G-BA-Vorgaben, Krankenhausreform, MD-Prüfung, Budgetverhandlung und Klinik-Compliance.

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
