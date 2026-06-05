---
name: leistungsgruppen-qualitaetskriterien
description: "Leistungsgruppen Qualitaetskriterien: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Leistungsgruppen Qualitaetskriterien

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Leistungsgruppen Qualitaetskriterien** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `leistungsgruppen-und-qualitaetskriterien-reformlogik` | Leistungsgruppen und Qualitaetskriterien nach KHVVG: prueft Strukturmerkmale, Personal- und Geraeteanforderungen, OPS-Kodierlogik, Zuweisung durch das Land und Kooperationsmoeglichkeiten. |
| `medizinprodukterecht-betreiberpflichten-mdr-mpbetreibv` | Medizinprodukterecht Betreiberpflichten MDR MPBetreibV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `mindestmengen-g-ba-qualitaetssicherung` | Mindestmengen nach § 136b SGB V und G-BA-Mm-R: Prognoseverfahren, Ausnahmen, Erbringungsverbote, Pruefung durch Land und Klage gegen Negativfeststellung. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Leistungsgruppen Qualitaetskriterien**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `leistungsgruppen-und-qualitaetskriterien-reformlogik`

**Fokus:** Leistungsgruppen und Qualitaetskriterien nach KHVVG: prueft Strukturmerkmale, Personal- und Geraeteanforderungen, OPS-Kodierlogik, Zuweisung durch das Land und Kooperationsmoeglichkeiten.

# Leistungsgruppen und Qualitaetskriterien Reformlogik

## Fachkern: Leistungsgruppen und Qualitaetskriterien Reformlogik
- **Spezialgegenstand:** Leistungsgruppen und Qualitaetskriterien Reformlogik. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Leistungsgruppen (LG) sind das neue Plan-Raster der Krankenhausreform: 65 Gruppen, die ICD-/OPS-basierte Versorgungstypen buendeln und an Strukturqualitaetsmerkmale gekoppelt sind. Der Skill prueft, ob eine Klinik die geforderte Struktur erfuellt und ob ein LG-Bescheid haltbar ist.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche LG wird gewollt/bestritten (z. B. LG 14 Allgemeine Innere, LG 27 Komplexe Wirbelsaeule)?
- Liegen Personalbesetzungs-, Geraete-, OP-Bereitschafts-Nachweise vor?
- Ist die Klinik in Notfallstufe 1/2/3 oder ohne Notfallstufe?
- Gibt es kooperierende Haeuser (Verbund, Konsiliarsystem, Tele-Anbindung)?
- Welches Land vergibt — und welche landesrechtlichen Konkretisierungen gelten?

## Rechtlicher Rahmen
- **KHG § 6a** Bundeseinheitliche Leistungsgruppen, Anlage zum KHG.
- **KHEntgG § 5** Verguetung an LG geknuepft, Vorhalteanteil.
- **SGB V § 135a, 136, 137** Qualitaetssicherung, Strukturmerkmale.
- **G-BA-Strukturqualitaetsrichtlinien** (z. B. fuer Stroke Units, Perinatalzentren, Onkologie).
- **Landeskrankenhausgesetze** Ausnahmen aus Sicherstellungsgruenden, Kooperationsregelungen.
- **OPS- und ICD-Klassifikation** zur Zuordnung Fall → LG (BfArM/InEK).

## / Schritt fuer Schritt
1. **LG identifizieren:** Welche LG ist betroffen? Anlage KHG nutzen, ggf. Vorgaben des Landes.
2. **Strukturqualitaetsmerkmale auflisten:** Personal (Aerzte, Pflege, qualifiziert), Geraete, 24/7-Bereitschaft, intensivmed. Anbindung.
3. **Erfuellungsgrad messen:** Nachweise (Dienstplaene, Geraeteliste, Personalmeldung) auswerten.
4. **Luecken identifizieren:** Welche Merkmale fehlen, wie zeitnah erfuellbar?
5. **Kooperationsmodelle pruefen:** Verbund-LG, Konsiliar-Anbindung, Teleneurologie, Telemedizin.
6. **Bescheid pruefen oder Antrag formulieren:** Sachverhaltsfeststellung der Behoerde gegen tatsaechliche Lage abgleichen.

## Trade-off-Matrix

| Modell | Vorteil | Nachteil |
|---|---|---|
| LG vollumfaenglich selbst erfuellen | volle Planautoritaet | hohe Personalkosten, ggf. Doppelvorhaltung |
| Kooperation/Verbund | Aufgabenteilung | Steuerungsaufwand, Vertragsgestaltung |
| Telemedizin-Anbindung | guenstig, schnell | nur fuer bestimmte LG zulaessig (z. B. Stroke) |
| LG abgeben | Konzentration auf Kernportfolio | Erloesausfall, Personalfolgen |

## Praxistipps
- 65 LG sind bundeseinheitlich; das Land entscheidet aber, **welche** Klinik welche LG bekommt.
- Strukturmerkmale werden teils stufenweise scharf gestellt (Konvergenz 2025-2027).
- Personalmeldung an InEK ist nicht identisch mit LG-Strukturnachweis — beides braucht es.
- G-BA-Richtlinien (Stroke, Perinatal, Onkologie) gelten parallel und sind oft strenger.
- LG-Verlust ist meist verbunden mit Erloesrueckgang und Konsequenz fuer Vorhaltebudget.

## Mustertexte
**Strukturqualitaetsnachweis fuer LG-Antrag:**
> Anlage 1: Personalbesetzung Stichtag [Datum]. Anlage 2: Geraeteliste (z. B. CT 24/7, MRT, Linksherzkatheter). Anlage 3: Dienstplan zum Nachweis der 24/7-Praesenz. Anlage 4: Kooperationsvertraege Konsiliararzt/Telemedizin.

**Widerspruch gegen LG-Versagung:**
> Gegen den Bescheid vom [Datum], zugestellt am [Datum], wird Widerspruch eingelegt. Begruendung folgt. Die Strukturqualitaetsmerkmale fuer LG [Nr.] sind ausweislich der beigefuegten Nachweise erfuellt … hilfsweise: Sicherstellungsausnahme nach Landeskrankenhausgesetz.

## Typische Fehler
- LG mit OPS-Code verwechseln: OPS triggert LG, ist aber nicht die LG selbst.
- G-BA-Qualitaetsanforderungen vergessen — sie gelten parallel.
- Personal nur als Soll-Besetzung melden, statt als Ist-Lage zum Stichtag.
- Kooperationsmodelle ohne schriftliche Vertraege/Dienstanweisungen — nicht anerkennbar.

## Querverweise
- `krankenhausreform-leistungsgruppen-routing`
- `vorhalteverguetung-leistungsgruppen-krankenhausreform`
- `mindestmengen-g-ba-qualitaetssicherung`
- `qualitaets-und-strukturvorgaben-intake`
- `strukturpruefung-ops-und-md`
- `personaluntergrenzen-pflege-ppugv`

## Quellen Stand 06/2026
- KHG Anlage zu § 6a (Leistungsgruppen-Liste), Fassung KHVVG 12/2024.
- G-BA-Richtlinien zur Strukturqualitaet (Live-Check: g-ba.de/richtlinien).
- BMG-Hinweise und FAQ zur Reformumsetzung (Live-Check: bundesgesundheitsministerium.de).
- BSG, staend. Rspr. zum Versorgungsauftrag und zur Strukturqualitaet.
- InEK-Vorgaben zur Personaldaten-Meldung (Live-Check: g-drg.de).

## 2. `medizinprodukterecht-betreiberpflichten-mdr-mpbetreibv`

**Fokus:** Medizinprodukterecht Betreiberpflichten MDR MPBetreibV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Medizinprodukterecht Betreiberpflichten MDR MPBetreibV

## Fachkern: Medizinprodukterecht Betreiberpflichten MDR MPBetreibV
- **Spezialgegenstand:** Medizinprodukterecht Betreiberpflichten MDR MPBetreibV. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Medizinprodukterecht Betreiberpflichten MDR MPBetreibV** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `mindestmengen-g-ba-qualitaetssicherung`

**Fokus:** Mindestmengen nach § 136b SGB V und G-BA-Mm-R: Prognoseverfahren, Ausnahmen, Erbringungsverbote, Pruefung durch Land und Klage gegen Negativfeststellung.

# Mindestmengen G-BA Qualitaetssicherung

## Fachkern: Mindestmengen G-BA Qualitaetssicherung
- **Spezialgegenstand:** Mindestmengen G-BA Qualitaetssicherung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Fuer bestimmte planbare Eingriffe (z. B. Knie-TEP, Bauchspeicheldruesen-OP, Fruehgeborene < 1250 g, Lebertransplantation, Stammzelltransplantation) verlangt § 136b SGB V Mindestmengen pro Standort und Jahr. Bei Unterschreiten gilt grundsaetzlich ein Erbringungsverbot.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welcher Mindestmengen-Tatbestand betrifft die Klinik (OPS-Liste der G-BA-Mm-R)?
- Liegen Prognose-/Negativfeststellung des Landes vor?
- Wird Ausnahme nach G-BA-Mm-R § 5 (z. B. fuer Versorgungssicherstellung) beansprucht?
- Welche Mengen wurden erbracht (Vorjahr, Prognose)?

## Rechtlicher Rahmen
- **SGB V § 136b Abs. 1 Nr. 2** Mindestmengen-Festlegung durch G-BA.
- **G-BA Mindestmengenregelungen (Mm-R)** in der jeweils aktuellen Fassung.
- **SGB V § 137 Abs. 3** Datenmeldung an Land/G-BA.
- **Landeskrankenhausgesetze** Pruefung der Prognose durch Landesbehoerde.
- **G-BA-Beschluesse** zu Aufnahme/Streichung von Mindestmengen-Tatbestaenden.
- **BVerfG** zu Berufsausuebungsfreiheit und Mindestmengen (Verhaeltnismaessigkeit).

## / Schritt fuer Schritt
1. **Mindestmengen-Tatbestand identifizieren:** OPS-Liste Mm-R Anlage.
2. **Vorjahresmengen ausweisen:** § 137 SGB V-Meldung.
3. **Prognose fuer Folgejahr erstellen:** Plausibilitaet, Versorgungsbedarf, Personalplanung.
4. **Negativfeststellung pruefen:** Landesbehoerde stellt fest, ob Prognose haltbar.
5. **Ausnahmetatbestand pruefen:** Sicherstellung, Versorgungsluecke, atypische Lage.
6. **Rechtsschutz:** Widerspruch/Klage gegen Negativfeststellung; einstweiliger Rechtsschutz.

## Trade-off-Matrix

| Lage | Strategie | Folge |
|---|---|---|
| Mindestmenge knapp erfuellt | Prognose plausibel begruenden | Fortfuehrung |
| Mindestmenge nicht erreicht | Ausnahme beantragen (Sicherstellung) | aufschiebende Wirkung pruefen |
| Mehrere Standorte | Konzentrierung an Hauptstandort | Strukturkosten reduziert |
| dauerhafte Unterschreitung | LG abgeben | Konzentration auf andere LG |

## Praxistipps
- Prognose ist keine bloße Schaetzung; sie braucht eine plausible Anknuepfung an Vorjahre, Personalbestand und Versorgungsauftrag.
- Erbringungsverbot greift in Regel zum Folgejahr; einstweiliger Rechtsschutz § 80 Abs. 5 VwGO zum Verwaltungsgericht.
- Ausnahmen sind eng auszulegen (BSG; BVerfG: Mm sind verfassungsrechtlich grundsaetzlich zulaessig).
- Mindestmengen wirken parallel zu LG-Strukturmerkmalen; LG kann ohne Mm-Tatbestand nicht ausgehoehlt werden.

## Mustertexte
**Begruendung der Prognose Knie-TEP:**
> Im Vorjahr [Datum] wurden [N] Knie-TEP-Eingriffe am Standort durchgefuehrt. Personalbestand und OP-Kapazitaeten erlauben fuer das Folgejahr eine Prognose von [N+x]. Begruendung: stabile Auslastung, Personalfortbildung, Versorgungsauftrag laut LG [Nr.].

**Widerspruch gegen Negativfeststellung:**
> Gegen die Negativfeststellung vom [Datum] wird Widerspruch eingelegt. Die Prognose ist plausibel ausweislich (Anlage 1-3). Hilfsweise: Ausnahme nach G-BA-Mm-R § 5 wegen Versorgungssicherstellung im Raum [Region], Begruendung …

## Typische Fehler
- Prognose mit Vorjahres-Ist-Werten gleichsetzen (G-BA fordert begruendete Vorausschau).
- Ausnahmetatbestand zu weit interpretieren (Sicherstellung verlangt Versorgungsluecke).
- Frist fuer Negativfeststellungsanzeige verpassen.
- Mindestmenge mit Vorhalteanteil/LG verwechseln.

## Querverweise
- `leistungsgruppen-und-qualitaetskriterien-reformlogik`
- `qualitaets-und-strukturvorgaben-intake`
- `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung`
- `notfallstufen-und-sicherstellungszuschlaege`
- `landeskrankenhausplan-aufnahme-herausnahme-aenderung`
- `klage-gegen-budgetbescheid-oder-schiedsstellenentscheidung`

## Quellen Stand 06/2026
- SGB V § 136b.
- G-BA Mindestmengenregelungen (Mm-R) in aktueller Fassung (Live-Check g-ba.de/richtlinien/38/).
- BSG, staend. Rspr. zur Mindestmengen-Prognose.
- BVerfG zu Verfassungsmaessigkeit von Mindestmengen.
- Landeskrankenhausgesetze 16 Laender zur Aufsicht und Negativfeststellung.
