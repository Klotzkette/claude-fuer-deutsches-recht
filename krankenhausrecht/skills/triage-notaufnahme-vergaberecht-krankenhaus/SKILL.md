---
name: triage-notaufnahme-vergaberecht-krankenhaus
description: "Triage Notaufnahme Vergaberecht Krankenhaus: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Triage Notaufnahme Vergaberecht Krankenhaus

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Triage Notaufnahme Vergaberecht Krankenhaus** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `triage-notaufnahme-ueberlastung-dokumentation` | Triage in der Notaufnahme: Manchester-/ESI-System, Wartezeit, Ueberlastung, Sekundaer-Triage Intensiv, ex-post Triage rechtlich, Dokumentationspflicht und Haftung. |
| `vergaberecht-krankenhaus-einkauf-bau-it` | Vergaberecht Krankenhaus Einkauf Bau IT: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `vorhalteverguetung-leistungsgruppen-krankenhausreform` | Vorhaltefinanzierung nach KHVVG: berechnet den Vorhalteanteil je Leistungsgruppe, ordnet die Konvergenzphase 2025 bis 2027, prueft Auswirkungen auf Erloesbudget und Liquiditaet. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Triage Notaufnahme Vergaberecht Krankenhaus**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `triage-notaufnahme-ueberlastung-dokumentation`

**Fokus:** Triage in der Notaufnahme: Manchester-/ESI-System, Wartezeit, Ueberlastung, Sekundaer-Triage Intensiv, ex-post Triage rechtlich, Dokumentationspflicht und Haftung.

# Triage Notaufnahme Ueberlastung Dokumentation

## Fachkern: Triage Notaufnahme Ueberlastung Dokumentation
- **Spezialgegenstand:** Triage Notaufnahme Ueberlastung Dokumentation. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Notaufnahmen muessen Patienten anhand validierter Triagesysteme (Manchester Triage System MTS, Emergency Severity Index ESI) priorisieren. Bei Ueberlastung und Knappheit (Intensivbetten, Beatmungsgeraete) bestehen ethisch-rechtliche Vorgaben (BVerfG-Beschluss zur Triage 2021/2022; § 5c IfSG nach Pandemienovelle).

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche Triage-Lage (Routine, Massenanfall, Ressourcenknappheit)?
- Welches Triagesystem ist eingefuehrt (MTS, ESI, andere)?
- Liegen Dokumentationsstandards, Schulungsnachweise vor?
- Gab es einen konkreten Vorfall (Triagefehler, Behandlungsverzoegerung)?
- Drohen Haftungsrisiken, Aufsicht oder Patientenbeschwerde?

## Rechtlicher Rahmen
- **BGB §§ 630a ff.** Behandlungspflicht, Aufnahme-/Ueberweisungspflicht in Notlage.
- **GG Art. 3 Abs. 3 S. 2** Benachteiligungsverbot wegen Behinderung — BVerfG 16.12.2021 zur Triage (1 BvR 1541/20).
- **§ 5c IfSG** Triagegrundsaetze (Pandemienovelle 2022).
- **DIVI- und DGINA-Empfehlungen** zu Triagesystemen und Krisenversorgung.
- **Notaufnahmevergaben G-BA** Stufenkonzept und Strukturmerkmale.
- **MD-Strukturpruefung** und MBO-Aerzte.

## / Schritt fuer Schritt
1. **Triagesystem dokumentieren:** Welches System, wer triagiert (Notfallpflege, Aerztlich), Schulungsnachweis.
2. **Dokumentation jeder Triage:** Eingangstrias mit Datum/Uhrzeit, Kategorie, Vitalparameter, Begruendung.
3. **Re-Triage:** Bei Verzoegerung erneute Bewertung; Verlauf dokumentieren.
4. **Sekundaer-Triage:** Bei knappen Ressourcen (Intensivbett, Beatmung) Entscheidung anhand § 5c IfSG: Erfolgsaussicht im Einzelfall, kein Diskriminierungskriterium.
5. **Ueberlastung melden:** Innerbehoerdlich, ggf. Leitstelle Rettungsdienst (Abmeldung Aufnahmestatus).
6. **Vorfall-/Haftungspruefung:** Fehlerquellen, dokumentierte Begruendung, Nachschulung.

## Trade-off-Matrix

| Lage | Triagesystem | Risiko |
|---|---|---|
| Routinenotaufnahme | MTS/ESI | wenig |
| Massenanfall MANV | MTS-MCI / SIEVE-START | hohe Anforderung Doku |
| Pandemielage knapper Intensivbetten | § 5c IfSG (Erfolgsaussicht) | verfassungsrechtl. Sensibilitaet |
| Ueberlastung dauerhaft | Strukturkritik, Aufsichtsdialog | Strukturpruefung droht |

## Praxistipps
- BVerfG-Beschluss (1 BvR 1541/20) hat Gesetzgeber zu Schutzregeln verpflichtet — § 5c IfSG ist die Antwort.
- Triagesystem zertifiziert anwenden (z. B. MTS-Lizenz, ESI-Schulung), Schulungsnachweis aufbewahren.
- Ex-post-Triage (Behandlungsabbruch zugunsten anderer) ist verfassungsrechtlich verboten (§ 5c Abs. 2 IfSG).
- Re-Triage bei langer Wartezeit zwingend — Verlaufsdokumentation.
- Abmeldung Aufnahmestatus an Rettungsleitstelle ist klare Eskalationsmassnahme bei Ueberlastung.

## Mustertexte
**Triage-Dokumentation (Routine):**
> Eingangsdatum/-zeit: …, Patient: …, Triage-System: MTS, Kategorie: rot/orange/gelb/gruen/blau, Vitalparameter (RR, HF, AF, SpO2, Schmerzen NRS): …, Triagierende Person (Quali, Schulung): …, Nachsicht/Re-Triage: ja/nein.

**Vorfallmemo Triagefehler:**
> Vorfall vom [Datum], Patient [ID], Kategorie [vergeben], tatsaechliche Schwere: …, Folge: …, Ursachenanalyse: …, Massnahmen: Schulung, Audit, Eskalationspfad.

## Typische Fehler
- Triage durch ungeschultes Personal.
- Re-Triage fehlt bei langen Wartezeiten.
- Dokumentation unvollstaendig — Beweisnot bei Haftung.
- § 5c IfSG-Vorgaben nicht in SOP integriert (Diskriminierungsverbot).
- Aufnahmestatus nicht abgemeldet trotz Ueberlastung.

## Querverweise
- `notfallstufen-und-sicherstellungszuschlaege`
- `intensivmedizin-beatmung-verlegung`
- `rettungsdienst-schnittstelle-aufnahme-pflicht`
- `patientenrechte-behandlungsvertrag-aufklaerung`
- `dokumentation-aufbewahrung-beweislast`
- `haftpflichtfall-krankenhaus-gutachtenstrategie`

## Quellen Stand 06/2026
- BVerfG 16.12.2021, 1 BvR 1541/20.
- § 5c IfSG.
- DIVI-/DGINA-Triage-Empfehlungen (Live-Check divi.de, dgina.de).
- G-BA Notfallstufen-RL (Live-Check g-ba.de).
- BGH, staend. Rspr. zu Aufnahmepflicht und Behandlungsverzoegerung.

## 2. `vergaberecht-krankenhaus-einkauf-bau-it`

**Fokus:** Vergaberecht Krankenhaus Einkauf Bau IT: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Vergaberecht Krankenhaus Einkauf Bau IT

## Fachkern: Vergaberecht Krankenhaus Einkauf Bau IT
- **Spezialgegenstand:** Vergaberecht Krankenhaus Einkauf Bau IT. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Vergaberecht Krankenhaus Einkauf Bau IT** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `vorhalteverguetung-leistungsgruppen-krankenhausreform`

**Fokus:** Vorhaltefinanzierung nach KHVVG: berechnet den Vorhalteanteil je Leistungsgruppe, ordnet die Konvergenzphase 2025 bis 2027, prueft Auswirkungen auf Erloesbudget und Liquiditaet.

# Vorhalteverguetung Leistungsgruppen Krankenhausreform

## Fachkern: Vorhalteverguetung Leistungsgruppen Krankenhausreform
- **Spezialgegenstand:** Vorhalteverguetung Leistungsgruppen Krankenhausreform. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Mit dem KHVVG wird die Krankenhausverguetung umgestellt: Statt fast vollstaendiger DRG-Finanzierung erhaelt jedes Plankrankenhaus kuenftig einen mengenunabhaengigen Vorhalteanteil (Zielmarke 60 %), der je Leistungsgruppe ausgereicht wird. Konvergenzphase 2025-2027.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Liegen LG-Zuweisungen des Landes vor?
- Wie ist die Casemix-Historie der vergangenen drei Jahre?
- Welche Vorhalteanteile sind fuer welche LG aktuell relevant?
- Wie wirkt die Konvergenz auf das laufende Budget?
- Gibt es Mehrleistungen, Strukturveraenderungen, neue LG?

## Rechtlicher Rahmen
- **KHEntgG § 5** Vorhalteverguetung, Konvergenzregelung.
- **KHG § 6a** LG als Bezugsgroesse.
- **SGB V § 109** Versorgungsauftrag.
- **KHVVG** vom 12.12.2024 (Artikelgesetz).
- **BMG-/InEK-Hinweise** zur LG-Casemix-Berechnung und Vorhalteanteil-Bestimmung.
- **PrEV/Pflegebudget** bleibt separat.

## / Schritt fuer Schritt
1. **LG-Zuweisung dokumentieren:** Welche LG hat die Klinik? Welche Mengen sind erbracht?
2. **Vorhalteanteil je LG berechnen:** Bundesweit normierter Anteil x Casemix-Volumen der Klinik.
3. **Konvergenzpfad anwenden:** 2025: 0 %, 2026: 20 % (Schaetzung, abhaengig von KHVVG-Konkretisierungen), 2027: 60 %.
4. **DRG-Restanteil pruefen:** DRG bleibt fuer den verbleibenden Anteil; weiterhin Casemix-relevant.
5. **Budget-Auswirkungen modellieren:** Vorher/Nachher-Vergleich pro LG; Liquiditaetseffekt.
6. **AEB anpassen:** Vorhalteanteile in Budgetvereinbarung gesondert ausweisen.

## Trade-off-Matrix

| Strategie | Effekt | Risiko |
|---|---|---|
| breit aufgestelltes LG-Portfolio | mehr Vorhalte-Volumen | Strukturkosten je LG hoch |
| Konzentration auf wenige LG | klare Strukturqualitaet | Erloesabhaengigkeit |
| Verbund-Vorhalten | geteilte Kosten | Vertrags- und Steuerungsaufwand |
| LG abgeben | Kostenreduktion | Vorhalte-Erloes faellt weg |

## Praxistipps
- Vorhalteverguetung **kompensiert keinen Casemix-Rueckgang** — Mengen weiterhin abrechnen.
- Konvergenz wirkt asymmetrisch: profitabel fuer Kliniken mit hohem Fixkostenanteil und niedriger Auslastung.
- 60 %-Vorhalteziel ist politisch; tatsaechliche Implementierung kann sich verzoegern (Live-Check BMG).
- Bei LG-Verlust: Vorhaltebudget faellt schrittweise weg, Personaldispositionen anpassen.
- Verhandlung 2026 ist die erste mit substanziellem Vorhalteanteil — gute Datengrundlage wichtig.

## Mustertexte
**Vorhalte-Modellrechnung im AEB:**
> Vorhalteanteil 2026 je LG (Anlage 5): LG 14 Allgemeine Innere: Casemix-Volumen 12.500, Vorhalteanteil 20 % entspricht … EUR. LG 27: … LG 33: … Summe Vorhalte: … EUR.

**Schreiben an Kasse zur Konvergenz:**
> In der Budgetverhandlung 2026 ist nach KHEntgG der Vorhalteanteil gesondert auszuweisen. Wir haben die Berechnung gemaess BMG-Hinweis vom [Datum] vorgenommen. Anlage: Vorhalteanteil-Matrix.

## Typische Fehler
- Vorhalteanteil mit Mengenausgleich verwechseln; Vorhalt ist mengenunabhaengig.
- Konvergenzphase als sofortige 60 %-Vorhaltequote behandeln.
- Pflegebudget in Vorhalteanteil hineinrechnen; Pflege bleibt separat.
- LG-Verlust ohne Folgen modellieren; Vorhalte verschwindet mit LG.

## Querverweise
- `khentgg-budgetverhandlung-drg-pepp-abgrenzung`
- `leistungsgruppen-und-qualitaetskriterien-reformlogik`
- `krankenhausreform-leistungsgruppen-routing`
- `pflegebudget-vereinbarung-nachweis-risiken`
- `klage-gegen-budgetbescheid-oder-schiedsstellenentscheidung`
- `schiedsstellenverfahren-krankenhausentgelt`

## Quellen Stand 06/2026
- KHEntgG i. d. F. KHVVG 12/2024.
- KHG § 6a (LG-Anlage).
- KHVVG-Konkretisierung 2025/2026 (Live-Check BMG, GKV-Spitzenverband, DKG).
- InEK-Casemix-Vorgaben (Live-Check g-drg.de).
- BSG, staend. Rspr. zur Budgetverhandlung.
