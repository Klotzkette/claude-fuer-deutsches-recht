---
name: rettungsdienst-schnittstelle
description: "Rettungsdienst Schnittstelle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rettungsdienst Schnittstelle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Rettungsdienst Schnittstelle** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rettungsdienst-schnittstelle-aufnahme-pflicht` | Rettungsdienst Schnittstelle Aufnahme Pflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `sektorenuebergreifende-versorgung-level-ii-klinik` | Sektorenuebergreifende Versorgung und Level Ii-Klinik nach KHVVG: Bruecke ambulant/stationaer, Strukturmerkmale, Verguetungslogik, Versorgungsauftrag und Kooperationsmodelle mit MVZ und Praxen. |
| `strahlenschutz-radiologie-nuklearmedizin` | Strahlenschutz Radiologie Nuklearmedizin: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Rettungsdienst Schnittstelle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rettungsdienst-schnittstelle-aufnahme-pflicht`

**Fokus:** Rettungsdienst Schnittstelle Aufnahme Pflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Rettungsdienst Schnittstelle Aufnahme Pflicht

## Fachkern: Rettungsdienst Schnittstelle Aufnahme Pflicht
- **Spezialgegenstand:** Rettungsdienst Schnittstelle Aufnahme Pflicht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Rettungsdienst Schnittstelle Aufnahme Pflicht** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 2. `sektorenuebergreifende-versorgung-level-ii-klinik`

**Fokus:** Sektorenuebergreifende Versorgung und Level Ii-Klinik nach KHVVG: Bruecke ambulant/stationaer, Strukturmerkmale, Verguetungslogik, Versorgungsauftrag und Kooperationsmodelle mit MVZ und Praxen.

# Sektorenuebergreifende Versorgung Level Ii Klinik

## Fachkern: Sektorenuebergreifende Versorgung Level Ii Klinik
- **Spezialgegenstand:** Sektorenuebergreifende Versorgung Level Ii Klinik. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Mit der Krankenhausreform (KHVVG) entstand die Stufe **Level Ii** (sektorenuebergreifend) — Bruecke zwischen vollstaendiger stationaerer Klinik (Level I bis III) und rein ambulanter Versorgung. Sie soll wohnortnahe Grund- und Regelversorgung sichern, kombiniert ambulant-stationaer und arbeitet mit Hybrid-DRG, AOP und stationaerer Kurzliegerversorgung.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Ist die Klinik als Level Ii vorgesehen oder im Umbau?
- Welche Leistungsgruppen passen zur sektorenuebergreifenden Versorgung?
- Liegen Kooperationsvertraege mit Praxen, MVZ, ambulanten OP-Zentren vor?
- Welche Strukturmerkmale (Personal, Geraete, Bereitschaft) sind erforderlich?
- Wie wird verguetet (Hybrid-DRG, DRG, AOP, sektorengleiche Pauschalen)?

## Rechtlicher Rahmen
- **KHG § 6a** Leistungsgruppen, mit Level-Ii-Komponente.
- **KHVVG** vom 12.12.2024.
- **SGB V §§ 115b, 115f, 116, 116a, 116b, 140a** Ambulant am Krankenhaus, Hybrid-DRG, Spezialaerztliche Versorgung, Selektivvertraege.
- **Landeskrankenhausgesetze** Plansetzung und Strukturmerkmale.
- **MVZ-Recht § 95 SGB V** Medizinische Versorgungszentren.
- **G-BA-Beschluesse** zu sektorenuebergreifenden Versorgungsformen.

## / Schritt fuer Schritt
1. **Versorgungsmodell entwerfen:** Welche Leistungen ambulant, welche kurzstationaer, welche stationaer?
2. **Strukturmerkmale pruefen:** Personal (Aerzte/Pflege 24/7 oder erweitert), Geraete, OP, Notfallaufnahme.
3. **Kooperationsmodelle:** MVZ-Anbindung, Praxen, Telemedizin, Rettungsdienst-Kooperation.
4. **Verguetungspfade:** AOP (KV), Hybrid-DRG (Kasse), DRG (Kasse), Selektivvertraege (§ 140a SGB V).
5. **Antrag auf Plan-Einstufung Level Ii:** Konzept, Bedarfsbegruendung, Strukturqualitaetsnachweise, Kooperationsvertraege.
6. **Investitionsfoerderung:** Transformationsfonds KHVVG, Landesinvestitionsfoerderung.
7. **Risiken:** Aufrechterhaltung der Notfallversorgung, Personalbedarf, Verguetungsmix.

## Trade-off-Matrix

| Modell | Vorteil | Nachteil |
|---|---|---|
| Reine Level Ii | wohnortnah, fokussiert | reduzierte Erloese je Fall |
| Level Ii + MVZ-Anbindung | Versorgungsbreite | Steuerungsaufwand |
| Verbund mit Vollversorger | gesamthafte Versorgung | Komplexitaet, Abhaengigkeit |
| Selektivvertrag § 140a | innovative Versorgungsmodelle | Bindung an Kasse |

## Praxistipps
- Level Ii ist konzeptionell mit Notaufnahme + ambulant-stationaerer Versorgung verbunden — Strukturanforderungen bleiben sportlich.
- Hybrid-DRG-Katalog ist die wirtschaftliche Achse; Personal/Geraete fuer haeufige Hybrid-DRG-Eingriffe vorhalten.
- Kooperationsvertraege schriftlich, mit Steuerungsstruktur und Vertretungsregeln.
- Transformationsfonds (50 Mrd. EUR) ist die wichtigste Foerderquelle fuer Level-Ii-Umbau.
- Bei Reduzierung von vollstationaerer Versorgung Personalplan und betriebsuebergangsrechtliche Fragen pruefen.

## Mustertexte
**Konzept Level Ii (Skizze):**
> Konzept Level Ii-Klinik [Standort]. 1. Versorgungsauftrag: Grund-/Regelversorgung. 2. Leistungsgruppen: LG 14 Allg. Innere, LG 15 Geriatrie, LG 12 Notfall. 3. Strukturmerkmale: Personal …, Geraete …, Notfallaufnahme …. 4. Kooperationen: MVZ [Name], Praxis [Name], Telemedizin [Anbieter]. 5. Verguetungsmix: 50 % Hybrid-DRG, 30 % DRG, 20 % AOP. 6. Investitionsplan / Transformationsfondsantrag.

**Antrag Transformationsfonds (Skizze):**
> Wir beantragen Mittel aus dem Transformationsfonds nach KHVVG fuer den Umbau zur Level Ii-Klinik. Konzept Anlage 1; Bedarfsbegruendung Anlage 2; Wirtschaftlichkeit Anlage 3; Kofinanzierung Land Anlage 4.

## Typische Fehler
- Level Ii als reine Ambulanz-Ausweichloesung verstanden — Strukturmerkmale Notfall bleiben.
- Hybrid-DRG-Katalog ignoriert — Verguetungsmix instabil.
- Kooperationsvertraege ohne Steuerungsregelungen.
- Personal-/Betriebsuebergang nicht geregelt (§ 613a BGB).
- Transformationsfondsantrag ohne klares Strukturveraenderungskonzept.

## Querverweise
- `krankenhausreform-leistungsgruppen-routing`
- `hybrid-drg-115f-sgb-v`
- `ambulantes-operieren-115b-sgb-v`
- `krankenhaus-mvz-gruendung-zulassung-compliance`
- `notfallstufen-und-sicherstellungszuschlaege`
- `privatisierung-betriebsuebergang-traegerwechsel`

## Quellen Stand 06/2026
- KHG § 6a, KHEntgG, SGB V §§ 115b, 115f, 116, 140a.
- KHVVG (12.12.2024).
- BMG-Konkretisierung Level Ii (Live-Check bundesgesundheitsministerium.de).
- G-BA-Beschluesse zu sektorenuebergreifender Versorgung (Live-Check g-ba.de).
- BSG, staend. Rspr. zum Versorgungsauftrag.

## 3. `strahlenschutz-radiologie-nuklearmedizin`

**Fokus:** Strahlenschutz Radiologie Nuklearmedizin: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Strahlenschutz Radiologie Nuklearmedizin

## Fachkern: Strahlenschutz Radiologie Nuklearmedizin
- **Spezialgegenstand:** Strahlenschutz Radiologie Nuklearmedizin. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Strahlenschutz Radiologie Nuklearmedizin** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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
