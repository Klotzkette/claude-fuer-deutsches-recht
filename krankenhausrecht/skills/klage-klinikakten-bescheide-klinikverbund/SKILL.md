---
name: klage-klinikakten-bescheide-klinikverbund
description: "Klage Klinikakten Bescheide Klinikverbund: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klage Klinikakten Bescheide Klinikverbund

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Klage Klinikakten Bescheide Klinikverbund** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klage-gegen-budgetbescheid-oder-schiedsstellenentscheidung` | Klage gegen Budgetbescheid (Land) oder Schiedsstellenentscheidung: Rechtsweg, Verwaltungs- vs. Sozialgericht, Klagearten, Frist, Begruendung, einstweiliger Rechtsschutz. |
| `klinikakten-und-bescheide-sortieren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Klinikakten und Bescheide sortieren. |
| `klinikverbund-fusion-kartell-vergabe-planungsrecht` | Klinikverbund Fusion Kartell Vergabe Planungsrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Klage Klinikakten Bescheide Klinikverbund**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klage-gegen-budgetbescheid-oder-schiedsstellenentscheidung`

**Fokus:** Klage gegen Budgetbescheid (Land) oder Schiedsstellenentscheidung: Rechtsweg, Verwaltungs- vs. Sozialgericht, Klagearten, Frist, Begruendung, einstweiliger Rechtsschutz.

# Klage gegen Budgetbescheid oder Schiedsstellenentscheidung

## Fachkern: Klage gegen Budgetbescheid oder Schiedsstellenentscheidung
- **Spezialgegenstand:** Klage gegen Budgetbescheid oder Schiedsstellenentscheidung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Budget-/Pflegesatzbescheide und Schiedsstellenentscheidungen koennen vor dem Sozialgericht (SGB-V-Bezug) oder Verwaltungsgericht (KHG-Bezug) angefochten werden. Die Rechtswegabgrenzung haengt vom Streitgegenstand ab. Klagearten und Fristen sind unterschiedlich.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Liegt Budgetbescheid (Landesplanungsbehoerde) oder Schiedsstellenentscheidung (§ 18a KHG) vor?
- Welcher Streitgegenstand: Erloesbudget, Pflegesatz, Verguetung, Versorgungsauftrag?
- Ist Frist (1 Monat) eingehalten?
- Welche Klageart (Anfechtung, Leistung, Feststellung, Verpflichtung)?
- Eilbeduerftigkeit gegeben (Liquiditaet, Sofortvollzug)?

## Rechtlicher Rahmen
- **KHG § 18a Abs. 4** Schiedsstellenentscheidung; Klagerecht vor VG/SG.
- **KHEntgG § 14** Genehmigung Pflegesatz/Budget durch Land.
- **SGB V § 109** Versorgungsauftrag, Versorgungsvertrag.
- **VwGO §§ 40, 42, 80, 113** Verwaltungsrechtsweg.
- **SGG §§ 51, 54, 86b** Sozialgerichtsweg, einstweiliger Rechtsschutz.
- **BSG-/BVerwG-Abgrenzung** zum Rechtsweg.

## / Schritt fuer Schritt
1. **Streitgegenstand klassifizieren:** Verguetungsstreit ↔ Strukturstreit; SGB V ↔ KHG.
2. **Rechtsweg bestimmen:**
 - Schiedsstellenentscheidung nach KHG → Verwaltungsgericht (§ 18a Abs. 4 KHG).
 - Verguetung im Einzelfall (Abrechnungsstreit) → Sozialgericht.
 - Versorgungsauftrag § 109 SGB V → Sozialgericht.
3. **Klageart pruefen:** Anfechtung, Feststellung, Leistung, Verpflichtung.
4. **Frist sichern:** 1 Monat ab Zustellung (§ 70 VwGO/§ 87 SGG).
5. **Eilbeduerftigkeit pruefen:** § 80 Abs. 5 VwGO / § 86b SGG.
6. **Begruendung:** Sachverhaltsfeststellung, Ermessen, Verhaeltnismaessigkeit, Verfahrensfehler, materielle Bewertung.

## Trade-off-Matrix

| Streitgegenstand | Rechtsweg | Klageart | Frist |
|---|---|---|---|
| Schiedsstellenentscheidung (Budget) | VG | Anfechtung + Verpflichtung | 1 Monat |
| Genehmigungsbescheid Land KHEntgG | VG | Anfechtung | 1 Monat |
| Einzelabrechnung SGB V | SG | Leistungsklage | 4 Jahre (Verjaehrung) |
| Versorgungsauftrag § 109 | SG | Feststellung | offen |
| Plankrankenhaus-Bescheid | VG | Anfechtung/Verpflichtung | 1 Monat |

## Praxistipps
- Schiedsstellenentscheidung ist VA mit Klagerecht beim VG (§ 18a Abs. 4 KHG); kein Vorverfahren.
- Bei Mischsachverhalten (Verguetung + Struktur) kann Streit auf beide Gerichtsbarkeiten verteilt sein — Doppelklage pruefen.
- Einstweiliger Rechtsschutz: § 80 Abs. 5 VwGO bei Sofortvollzug; § 86b SGG bei sozialgerichtlichem Eilfall.
- Klagebegruendung muss Sachverhaltsfeststellung des Bescheids konkret angreifen — nicht nur Ergebnis.
- BVerwG/BSG haben staend. Rspr. zur Schiedsstellenkontrolle: nur eingeschraenkte Pruefdichte (Beurteilungsspielraum).

## Mustertexte
**Klageschrift (Skizze, VG):**
> An das Verwaltungsgericht [Ort]. Klagepartei: [Krankenhaus]. Beklagte: [Land]. Streitgegenstand: Anfechtung der Schiedsstellenentscheidung vom [Datum]. Klageantrag: 1. Entscheidung aufzuheben. 2. Hilfsweise: Beklagte zu verpflichten, Erloesbudget 2026 unter Beachtung der Rechtsauffassung des Gerichts neu festzusetzen. Begruendung … Anlagen …

**Eilantrag § 80 Abs. 5 VwGO:**
> Die aufschiebende Wirkung der Anfechtungsklage wird angeordnet/wiederhergestellt. Begruendung: 1. Rechtswidrigkeit summarisch erkennbar. 2. Aussetzungsinteresse: Liquiditaetsfolgen, Versorgungssicherung. 3. Folgen …

## Typische Fehler
- Rechtsweg falsch (SG statt VG bei Schiedsstellensache).
- Klagefrist versaeumt — Bestandskraft.
- Begruendung bleibt im Ergebnis stehen, ohne Sachverhaltsfeststellung anzugreifen.
- Eilantrag versaeumt — Bescheid wirkt vor Klageentscheidung.
- Schiedsstellenkontrolle ueberschaetzt (Beurteilungsspielraum begrenzt).

## Querverweise
- `schiedsstellenverfahren-krankenhausentgelt`
- `khentgg-budgetverhandlung-drg-pepp-abgrenzung`
- `landeskrankenhausplan-aufnahme-herausnahme-aenderung`
- `vorhalteverguetung-leistungsgruppen-krankenhausreform`
- `pflegebudget-vereinbarung-nachweis-risiken`
- `landesaufsicht-krankenhausaufsicht-beanstandung`

## Quellen Stand 06/2026
- KHG § 18a Abs. 4.
- KHEntgG § 14.
- SGB V § 109.
- VwGO §§ 40, 42, 80, 113; SGG §§ 51, 54, 86b.
- BVerwG, staend. Rspr. zur Schiedsstellenkontrolle (Beurteilungsspielraum).
- BSG, staend. Rspr. zum sozialgerichtlichen Verguetungsstreit.

## 2. `klinikakten-und-bescheide-sortieren`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Klinikakten und Bescheide sortieren.

# Klinikakten und Bescheide sortieren

## Fachkern: Klinikakten und Bescheide sortieren
- **Spezialgegenstand:** Klinikakten und Bescheide sortieren. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Klinikakten und Bescheide sortieren** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Krankenhausrecht zwischen KHG, KHEntgG, SGB V, Landeskrankenhausrecht, G-BA-Vorgaben, Krankenhausreform, MD-Prüfung, Budgetverhandlung und Klinik-Compliance.

## Startfragen
- Was soll sofort entstehen: Kurztriage, Aktenplan, Fragenliste, Memo, Schriftsatz, Vertrag, Formular oder Mandantenbrief?
- Wo drohen Fristen, Formerfordernisse, Bußgelder, Gebührennachteile, Verfahrensfehler oder irreversible Schritte?
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

## 3. `klinikverbund-fusion-kartell-vergabe-planungsrecht`

**Fokus:** Klinikverbund Fusion Kartell Vergabe Planungsrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Klinikverbund Fusion Kartell Vergabe Planungsrecht

## Fachkern: Klinikverbund Fusion Kartell Vergabe Planungsrecht
- **Spezialgegenstand:** Klinikverbund Fusion Kartell Vergabe Planungsrecht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Klinikverbund Fusion Kartell Vergabe Planungsrecht** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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
