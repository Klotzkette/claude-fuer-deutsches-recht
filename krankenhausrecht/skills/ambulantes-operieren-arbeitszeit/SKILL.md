---
name: ambulantes-operieren-arbeitszeit
description: "Ambulantes Operieren Arbeitszeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ambulantes Operieren Arbeitszeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ambulantes Operieren Arbeitszeit** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ambulantes-operieren-115b-sgb-v` | Ambulantes Operieren am Krankenhaus nach § 115b SGB V: AOP-Vertrag, AOP-Katalog mit Schweregradkontexten, Abrechnung gegenueber KV, Abgrenzung zum stationaeren Aufenthalt und Hybrid-DRG. |
| `arbeitszeit-bereitschaftsdienst-rufdienst` | Arbeitszeit Bereitschaftsdienst Rufdienst: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `barrierefreiheit-krankenhauskommunikation` | Barrierefreiheit Krankenhauskommunikation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Ambulantes Operieren Arbeitszeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ambulantes-operieren-115b-sgb-v`

**Fokus:** Ambulantes Operieren am Krankenhaus nach § 115b SGB V: AOP-Vertrag, AOP-Katalog mit Schweregradkontexten, Abrechnung gegenueber KV, Abgrenzung zum stationaeren Aufenthalt und Hybrid-DRG.

# Ambulantes Operieren § 115b SGB V

## Fachkern: Ambulantes Operieren § 115b SGB V
- **Spezialgegenstand:** Ambulantes Operieren § 115b SGB V. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
§ 115b SGB V eroeffnet Krankenhaeusern die Moeglichkeit, ambulante Operationen im Rahmen des AOP-Katalogs zu erbringen. Seit 2023 gilt ein erweiterter Katalog mit Kontextfaktoren (Schweregrad, soziale Lage, Risikofaktoren). Abrechnung gegenueber Kassenaerztlicher Vereinigung (KV), nicht Kasse direkt.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche Eingriffe sind betroffen (OPS-Codes im AOP-Katalog)?
- Liegen Kontextfaktoren vor (BMI, Komorbiditaet, Pflegegrad, soziale Lage)?
- Wird Abrechnung gegen KV oder als Hybrid-DRG (§ 115f SGB V) gefuehrt?
- Existiert AOP-Vertrag (Bundesrahmenvertrag GKV-SV/DKG/KBV)?
- Drohen MD-Pruefungen wegen Fehlbelegung?

## Rechtlicher Rahmen
- **SGB V § 115b** Ambulantes Operieren am Krankenhaus, AOP-Vertrag.
- **AOP-Vertrag** zwischen GKV-SV, KBV, DKG i. d. F. 2023 ff.
- **AOP-Katalog (Anlage 1 AOP-Vertrag)** mit Kontextfaktoren.
- **SGB V § 115f** Hybrid-DRG fuer haeufige Eingriffe (Schnittstelle ambulant/stationaer).
- **BMV-AE** und KV-Abrechnungsregeln (HVM, EBM).
- **MD-Pruefung § 275c SGB V** und § 17c KHG zur Fehlbelegungspruefung.

## / Schritt fuer Schritt
1. **Eingriff im AOP-Katalog identifizieren:** OPS-Code abgleichen.
2. **Kontextfaktoren pruefen:** Sind Schweregrad-/Risiko-Konstellationen erfuellt, die stationaeren Aufenthalt rechtfertigen?
3. **Abrechnungsweg waehlen:** AOP (KV) oder Hybrid-DRG (Kasse direkt) oder stationaer (Kasse, DRG).
4. **Dokumentation sichern:** OP-Bericht, Anaesthesie-Protokoll, Verlaufsbeobachtung, Entlassbrief.
5. **MD-Pruefung antizipieren:** Fehlbelegung wuerde stationaeren Erloes zur AOP-Pauschale reduzieren.
6. **Abrechnung:** KV (Quartalsabrechnung) oder Hybrid-DRG (direkt).

## Trade-off-Matrix

| Konstellation | Empfohlene Schiene | Risiko |
|---|---|---|
| reiner Routineeingriff, gesunder Patient | AOP/Hybrid-DRG | bei Hybrid-DRG groesserer Erloes |
| Komorbiditaet, hohes Alter, Pflegegrad | stationaer | MD-Pruefung droht trotzdem |
| Notfall ueber Aufnahmediagnostik | stationaer | Dokumentation Begruendung wichtig |
| Patient lehnt ambulante Versorgung ab | dokumentieren, ggf. stationaer | sozialer Kontextfaktor |

## Praxistipps
- AOP-Katalog 2023 hat Kontextfaktoren neu eingefuehrt — sie machen die Abgrenzung lebbar.
- Hybrid-DRG (§ 115f SGB V) ist seit 2024 fuer einen wachsenden Katalog scharf gestellt; einheitlicher Festbetrag.
- Personalmeldung an InEK auch fuer ambulante Eingriffe relevant (Strukturpruefung).
- Bei MD-Pruefung "primaere Fehlbelegung" droht Abschlag auf AOP-Pauschale; Begruendung Kontextfaktor sichern.
- KV-Honorar-HVM kann Pauschalierungen, Quoten und Begrenzungen vorsehen.

## Mustertexte
**Dokumentationspflicht-Hinweis intern:**
> Bei jedem AOP-Eingriff sind Kontextfaktoren zwingend zu dokumentieren: 1. BMI, 2. ASA-Klassifikation, 3. Komorbiditaet (Liste), 4. Pflegegrad, 5. soziale Lage (Begruendung), 6. Risikoanaesthesie. Bei stationaerer Indikation: Begruendung zwingend, sonst MD-Pruefung droht.

**Widerspruch gegen MD-Fehlbelegung:**
> Die MD-Stellungnahme verkennt die Kontextfaktoren nach AOP-Katalog 2023. Vorliegend lag [Faktor] dokumentiert vor. Die stationaere Behandlung war indiziert. Anlagen: Aerztliche Doku, Pflegebericht.

## Typische Fehler
- AOP-Katalog 2023 nicht aktualisiert; Kontextfaktoren ignoriert.
- Hybrid-DRG-Faelle ueber AOP abgerechnet (falsch — Hybrid-DRG hat eigenen Weg).
- Stationaere Aufnahme ohne dokumentierte Begruendung — MD-Risiko.
- KV-Abrechnung nicht in Budgetbetrachtung beruecksichtigt.

## Querverweise
- `hybrid-drg-115f-sgb-v`
- `krankenhaus-mvz-gruendung-zulassung-compliance`
- `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung`
- `strukturpruefung-ops-und-md`
- `khentgg-budgetverhandlung-drg-pepp-abgrenzung`
- `sektorenuebergreifende-versorgung-level-ii-klinik`

## Quellen Stand 06/2026
- SGB V §§ 115b, 115f.
- AOP-Vertrag (Live-Check gkv-spitzenverband.de, kbv.de, dkgev.de).
- AOP-Katalog Anlage 1 (jaehrlich aktualisiert).
- Hybrid-DRG-Verordnung (Live-Check BMG).
- BSG, staend. Rspr. zur Fehlbelegung und zum AOP-Vertrag.

## 2. `arbeitszeit-bereitschaftsdienst-rufdienst`

**Fokus:** Arbeitszeit Bereitschaftsdienst Rufdienst: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Arbeitszeit Bereitschaftsdienst Rufdienst

## Fachkern: Arbeitszeit Bereitschaftsdienst Rufdienst
- **Spezialgegenstand:** Arbeitszeit Bereitschaftsdienst Rufdienst. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Arbeitszeit Bereitschaftsdienst Rufdienst** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `barrierefreiheit-krankenhauskommunikation`

**Fokus:** Barrierefreiheit Krankenhauskommunikation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Barrierefreiheit Krankenhauskommunikation

## Fachkern: Barrierefreiheit Krankenhauskommunikation
- **Spezialgegenstand:** Barrierefreiheit Krankenhauskommunikation. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Barrierefreiheit Krankenhauskommunikation** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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
