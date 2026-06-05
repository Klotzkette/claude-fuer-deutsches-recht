---
name: hybrid-drg-insolvenz-intensivmedizin-beatmung
description: "Hybrid DRG Insolvenz Intensivmedizin Beatmung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Hybrid DRG Insolvenz Intensivmedizin Beatmung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Hybrid DRG Insolvenz Intensivmedizin Beatmung** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hybrid-drg-115f-sgb-v` | Hybrid-DRG nach § 115f SGB V: sektorengleiche Verguetung fuer haeufige Eingriffe (Hernie, Tonsillektomie u. a.), Katalog, Abrechnung gegen Kasse, Abgrenzung zu AOP und stationaerer DRG. |
| `insolvenz-eines-krankenhauses-versorgungssicherung` | Insolvenz eines Krankenhauses Versorgungssicherung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `intensivmedizin-beatmung-verlegung` | Intensivmedizin, Beatmung und Patientenverlegung: PpUGV-Intensiv, Verlegungsfaehigkeit, IPReG-Bedingungen ausserklinische Beatmung, Strukturanforderungen, OPS- und MD-Pruefung. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Hybrid DRG Insolvenz Intensivmedizin Beatmung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hybrid-drg-115f-sgb-v`

**Fokus:** Hybrid-DRG nach § 115f SGB V: sektorengleiche Verguetung fuer haeufige Eingriffe (Hernie, Tonsillektomie u. a.), Katalog, Abrechnung gegen Kasse, Abgrenzung zu AOP und stationaerer DRG.

# Hybrid-DRG § 115f SGB V

## Fachkern: Hybrid-DRG § 115f SGB V
- **Spezialgegenstand:** Hybrid-DRG § 115f SGB V. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Seit 2024 sind **Hybrid-DRG** eingefuehrt: einheitliche Verguetung fuer einen abschliessenden Katalog von Eingriffen — unabhaengig davon, ob die Leistung stationaer (Kurzliegerfall) oder ambulant erbracht wird. Ziel: gleiches Geld fuer gleichen medizinischen Inhalt, Hospitalisierungs-Anreiz beseitigen.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Ist der konkrete Eingriff im Hybrid-DRG-Katalog (Verordnung BMG)?
- Wird Patient stationaer mit Kurzliegerfall behandelt oder ambulant?
- Liegen Strukturmerkmale fuer die Hybrid-DRG-Abrechnung vor (Personal, Geraete)?
- Wird die Abrechnung direkt gegenueber der Kasse oder ueber KV gefuehrt?
- Wirkt die Hybrid-DRG auf die DRG-Mengen- und Vorhalteberechnung?

## Rechtlicher Rahmen
- **SGB V § 115f** Hybrid-DRG-Eingriff, sektorengleiche Verguetung.
- **Hybrid-DRG-Verordnung (HybDRG-V)** vom BMG, Katalog und Festpreise.
- **AOP-Vertrag § 115b SGB V** als Abgrenzungsfeld.
- **InEK-Hybrid-DRG-Katalog** mit OPS-/ICD-Zuordnung.
- **KHEntgG/DRG-Katalog** fuer stationaere Restmengen.
- **DKR** fuer Kodierung.

## / Schritt fuer Schritt
1. **Katalog-Treffer pruefen:** OPS und ICD im Hybrid-DRG-Katalog?
2. **Behandlungsweg dokumentieren:** Ambulant, stationaer Kurzlieger (< 1 Tag), stationaer mit Indikation.
3. **Abrechnungsweg waehlen:** Hybrid-DRG (Kasse direkt) bei Katalogfall, sonst AOP (KV) oder DRG (Kasse).
4. **Dokumentation sichern:** Indikation, Kontextfaktoren bei stationaerer Wahl.
5. **MD-Pruefung antizipieren:** Bei stationaerer Aufnahme trotz Hybrid-DRG-Tatbestand droht Fehlbelegungspruefung.

## Trade-off-Matrix

| Setting | Empfohlene Schiene | Erloeshoehe |
|---|---|---|
| ambulanter Routineeingriff im Katalog | Hybrid-DRG | mittel, festpreis |
| Komorbiditaet rechtfertigt stationaere Aufnahme | DRG (stationaer) | meist hoeher, MD-Risiko |
| Eingriff nicht im Katalog | AOP/DRG | nach klassischer Schiene |
| postoperative Komplikation | DRG stationaer | DRG-Recodierung pruefen |

## Praxistipps
- Hybrid-DRG-Katalog wird jaehrlich erweitert (Live-Check BMG/InEK).
- Festpreis entkoppelt Anreiz zur stationaeren Aufnahme — Kurzliegerprobleme.
- AOP und Hybrid-DRG sind voneinander zu trennen: AOP geht ueber KV, Hybrid-DRG direkt gegen Kasse.
- Hybrid-DRG-Mengen fliessen in Casemix-Volumen ein, nicht in DRG-Casemix; Auswirkung auf Vorhaltebudget pruefen.
- Bei stationaerer Aufnahme trotz Hybrid-DRG-Indikation Kontextfaktor sorgfaeltig dokumentieren.

## Mustertexte
**Indikationsbegruendung stationaer trotz Hybrid-DRG:**
> Trotz Vorliegen der Hybrid-DRG-OPS [Code] war eine stationaere Aufnahme indiziert wegen [Komorbiditaet/Risikoanaesthesie/soziale Lage]. Die Entscheidung folgt den Kontextkriterien des AOP-Vertrags und der DKR. Dokumentation: …

**Antwort auf MD-Pruefung Fehlbelegung:**
> Die MD-Pruefung beanstandet stationaere Aufnahme bei Hybrid-DRG-Tatbestand. Wir verweisen auf [konkreter Kontextfaktor]; die Aufnahme war medizinisch indiziert. Hilfsweise: Recodierung als Kurzliegerfall im DRG.

## Typische Fehler
- AOP und Hybrid-DRG verwechseln (KV vs. Kasse direkt).
- Hybrid-DRG ohne Festpreisbeachtung abrechnen — Kassen kuerzen.
- Stationaere Aufnahme ohne dokumentierte Begruendung — MD-Risiko.
- Hybrid-DRG-Mengen nicht in Casemix-Statistik beachten.

## Querverweise
- `ambulantes-operieren-115b-sgb-v`
- `khentgg-budgetverhandlung-drg-pepp-abgrenzung`
- `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung`
- `strukturpruefung-ops-und-md`
- `sektorenuebergreifende-versorgung-level-ii-klinik`
- `dokumentation-aufbewahrung-beweislast`

## Quellen Stand 06/2026
- SGB V § 115f.
- Hybrid-DRG-Verordnung (Live-Check BMG, gkv-spitzenverband.de).
- InEK-Katalog Hybrid-DRG (Live-Check g-drg.de).
- AOP-Vertrag und AOP-Katalog (Live-Check dkgev.de).
- BSG, staend. Rspr. zu Sektorenabgrenzung und Fehlbelegung.

## 2. `insolvenz-eines-krankenhauses-versorgungssicherung`

**Fokus:** Insolvenz eines Krankenhauses Versorgungssicherung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Insolvenz eines Krankenhauses Versorgungssicherung

## Fachkern: Insolvenz eines Krankenhauses Versorgungssicherung
- **Spezialgegenstand:** Insolvenz eines Krankenhauses Versorgungssicherung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Insolvenz eines Krankenhauses Versorgungssicherung** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `intensivmedizin-beatmung-verlegung`

**Fokus:** Intensivmedizin, Beatmung und Patientenverlegung: PpUGV-Intensiv, Verlegungsfaehigkeit, IPReG-Bedingungen ausserklinische Beatmung, Strukturanforderungen, OPS- und MD-Pruefung.

# Intensivmedizin Beatmung Verlegung

## Fachkern: Intensivmedizin Beatmung Verlegung
- **Spezialgegenstand:** Intensivmedizin Beatmung Verlegung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Die Intensivmedizin ist hochreguliert: Personaluntergrenzen (PpUGV-Intensiv), Strukturmerkmale fuer Beatmungs-OPS, Verlegung gemaess Intensivkapazitaeten, ausserklinische Beatmung nach IPReG (Intensivpflege- und Rehabilitationsstaerkungsgesetz). Fehleinordnung gefaehrdet Verguetung und Patientensicherheit.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche Intensivstation (Erwachsene, Kinder, Neonatologie, Spezial)?
- Wird Beatmung dokumentiert (Beatmungsstunden, Geraet, OPS 8-71x)?
- Ist Verlegung intern oder zwischen Kliniken (Triage, Kapazitaet)?
- Liegt Antrag/Voraussetzung ausserklinische Beatmung nach IPReG vor?
- Drohen MD-Pruefung, Pflegeuntergrenze, Strukturzuschlag-Wegfall?

## Rechtlicher Rahmen
- **PpUGV** Anlage Intensiv (Erwachsene, Kinder, Neonatologie).
- **OPS 8-71x** Beatmungs- und Komplexbehandlungs-Kodes.
- **G-BA-Richtlinien** Versorgungsstrukturen Intensiv (Stroke, Trauma, Perinatalzentrum).
- **IPReG** (Intensivpflege- und Rehabilitationsstaerkungsgesetz) Ausserklinische Beatmung.
- **SGB V § 37c** Spezialisierte Ambulante Palliativversorgung (SAPV) als angrenzendes Feld.
- **G-DRG-Katalog** Beatmungs- und Sepsis-DRGs mit Strukturmerkmal.

## / Schritt fuer Schritt
1. **Stationskategorisierung pruefen:** Erwachsenen-, Kinder-, Neonatologie-Intensiv; Bettenzahl, Beatmungsplaetze.
2. **PpUGV-Quote rechnen:** Pflege je Schicht, examinierte Quote, Helferanrechnung.
3. **Beatmungsstunden korrekt erfassen:** Beginn (Intubation/Tracheostoma) bis Ende (Extubation), MD-konforme Doku.
4. **OPS-Strukturmerkmal pruefen:** OPS 8-980 Komplexbehandlung Intensiv mit Strukturmerkmalen (Personal, Geraete, Routine).
5. **Verlegung dokumentieren:** Intensivkapazitaet, Triage-Entscheidung, Begruendung medizinisch und kapazitiv.
6. **IPReG-Verlegung ausserklinisch:** Indikationspruefung, Genehmigung Kasse, Versorgungsstruktur.
7. **MD-Pruefung antizipieren:** Strukturpruefung kann Beatmungs-DRG kassieren.

## Trade-off-Matrix

| Konstellation | Massnahme | Verguetungseffekt |
|---|---|---|
| Beatmung > 24h | OPS 8-71x, Beatmungs-DRG | hoeher als nicht beatmet |
| Komplexbehandlung Intensiv | OPS 8-980 erfuellt? | Zusatzentgelt |
| Verlegung zur Intensiv extern | Begruendung Triage | DRG-Anteilig |
| Ausserklinische Beatmung (IPReG) | Antrag, Strukturen | langfristige Versorgungsfragen |

## Praxistipps
- Beatmungsstunden-OPS sind MD-Pruefungs-Hotspot; Doku-Genauigkeit zentral.
- OPS 8-980 Komplexbehandlung verlangt Mindestpersonal pro Schicht — Pflegepersonalbericht mitfuehren.
- Triage-Entscheidung dokumentieren (BAEK-/DIVI-Empfehlungen).
- IPReG verlangt Indikationspruefung; AOK/Ersatzkassen pruefen Versorgungsweg.
- Pflegeuntergrenze-Verletzung in Intensiv fuehrt zu Verguetungsabschlag.

## Mustertexte
**OPS-Doku Beatmungsbeginn:**
> Datum/Uhrzeit: …, Patient: …, Indikation: respiratorische Insuffizienz, Mode: BiPAP/druckkontrolliert, Tubus/Tracheostoma: …, FiO2: …, PEEP: …, Beatmungsbeginn-OPS 8-71x ab [Uhrzeit]. Aerztl. Anordnung: [Name].

**Verlegungsbericht intern:**
> Patient [Name], Diagnose [ICD]; Verlegung von Intensiv [Station] zur [Ziel]; Begruendung: medizinisch stabil/unverlegbar, kapazitiv: Bettensituation/Triage. Mitfuehrungsunterlagen: Medikationsplan, Beatmungsprotokoll, Pflegebericht.

## Typische Fehler
- Beatmungsstunden zu generoes oder zu knapp (MD-Streit).
- Komplexbehandlungs-OPS ohne Strukturnachweis.
- Triage-Entscheidung ohne Dokumentation.
- Ausserklinische Beatmung ohne IPReG-Indikationspruefung.

## Querverweise
- `personaluntergrenzen-pflege-ppugv`
- `strukturpruefung-ops-und-md`
- `triage-notaufnahme-ueberlastung-dokumentation`
- `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung`
- `notfallstufen-und-sicherstellungszuschlaege`
- `kinder-und-jugendmedizin-besondere-versorgung`

## Quellen Stand 06/2026
- PpUGV (Live-Check BMG).
- OPS-Katalog BfArM (Live-Check bfarm.de).
- IPReG (Live-Check BMG, gkv-spitzenverband.de).
- G-BA Strukturqualitaetsrichtlinien (Live-Check g-ba.de).
- BSG, staend. Rspr. zu Beatmungsstunden und Strukturpruefung.
- DIVI-Empfehlungen zu Triage und Intensivverlegung.
