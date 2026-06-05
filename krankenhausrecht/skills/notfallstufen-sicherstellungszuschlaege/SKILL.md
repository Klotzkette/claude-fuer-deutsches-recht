---
name: notfallstufen-sicherstellungszuschlaege
description: "Notfallstufen Sicherstellungszuschlaege: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Notfallstufen Sicherstellungszuschlaege

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Notfallstufen Sicherstellungszuschlaege** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `notfallstufen-und-sicherstellungszuschlaege` | Notfallversorgungsstufen nach G-BA-Notfallstufenkonzept und Sicherstellungszuschlaege nach KHEntgG: Eingruppierung, Strukturmerkmale, Vergueterelevanz, Verlust bei Strukturveraenderung. |
| `patientenbeschwerde-und-risikomanagement` | Patientenbeschwerde und Risikomanagement: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `personaluntergrenzen-pflege-ppugv` | Pflegepersonaluntergrenzen-Verordnung (PpUGV): pflegesensitive Bereiche, Quotenberechnung, Schichten, Meldepflicht, Sanktionen und Strukturpruefung. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Notfallstufen Sicherstellungszuschlaege**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `notfallstufen-und-sicherstellungszuschlaege`

**Fokus:** Notfallversorgungsstufen nach G-BA-Notfallstufenkonzept und Sicherstellungszuschlaege nach KHEntgG: Eingruppierung, Strukturmerkmale, Vergueterelevanz, Verlust bei Strukturveraenderung.

# Notfallstufen und Sicherstellungszuschlaege

## Fachkern: Notfallstufen und Sicherstellungszuschlaege
- **Spezialgegenstand:** Notfallstufen und Sicherstellungszuschlaege. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Die G-BA-Regelung zur Notfallversorgung (Notfallstufen-RL) teilt Krankenhaeuser in drei Stufen ein: Basis (Stufe 1), erweiterte (Stufe 2), umfassende (Stufe 3) Notfallversorgung — plus die Sonderform Spezialversorgung. Eingruppierung beeinflusst Verguetungszuschlaege. Parallel ermoeglicht § 17b Abs. 1a KHEntgG Sicherstellungszuschlaege fuer duenn besiedelte Regionen.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche Notfallstufe hat die Klinik aktuell?
- Werden Strukturmerkmale (Personal, Geraete, Bereitschaft) durchgaengig erfuellt?
- Liegt eine Strukturpruefung des MD vor?
- Ist die Klinik in einer Versorgungslueckenregion (Sicherstellungszuschlag)?
- Drohen Stufenrueckstufung oder Wegfall Sicherstellungszuschlag?

## Rechtlicher Rahmen
- **SGB V § 136c Abs. 4** G-BA-Regelung Notfallversorgung.
- **G-BA Notfallstufen-Richtlinie (Notfallstufen-RL)** als Mass.
- **KHEntgG § 9 Abs. 1a, § 17b Abs. 1a** Zu-/Abschlaege fuer Notfallstufen, Sicherstellungszuschlag.
- **KHVVG** Modifikationen Notfallstufenkonzept (z. B. Level Ii-Kliniken).
- **Landeskrankenhausgesetze** Konkretisierung Versorgungsbeduerfnis.
- **MD-Strukturpruefung** zur Verifizierung der Stufenmerkmale.

## / Schritt fuer Schritt
1. **Eingruppierung pruefen:** Welche Stufe gilt aktuell, welche soll gehalten/erreicht werden?
2. **Strukturmerkmale gegenrechnen:** Aerzte, Pflege, Geraete, 24/7-Bereitschaft, intensivmed. Anbindung.
3. **MD-Bericht auswerten:** Welche Beanstandungen, welche Heilungsmoeglichkeiten?
4. **Verguetungswirkung modellieren:** Zuschlag-/Abschlagshoehe je Stufe und je Fallpauschale.
5. **Sicherstellungszuschlag pruefen:** Bedarfsplan, Erreichbarkeitsanalyse, Bevoelkerungsdichte.
6. **Antrag/Widerspruch:** Stufenerhalt oder -anhebung; Sicherstellungs-Antrag an Land/GKV.

## Trade-off-Matrix

| Lage | Strategie | Effekt |
|---|---|---|
| Stufe 1/2 erfuellt, Stufe 3 angestrebt | Strukturen aufbauen | hoeherer Zuschlag, hoehere Kosten |
| Stufe 2 in Gefahr | gezielte Strukturhaerten | Erhalt der Zuschlaege |
| Stufenverlust droht | Verlegungs-/Kooperationsmodell | abgemildert Erloesausfall |
| Sicherstellungslage klar | Antrag stellen | befristete Zuschlaege |

## Praxistipps
- Notfallstufen-RL des G-BA wird mit KHVVG-Konkretisierung weiterentwickelt — Live-Check g-ba.de.
- Sicherstellungszuschlag ist befristet und an Bedarfslage geknuepft (z. B. Distanz zu naechstem Versorger).
- Level Ii-Kliniken (KHVVG) bilden Bruecke ambulant-stationaer; Notfallstufung muss separat gepruegt werden.
- Stufenverlust wirkt sich oft staerker aus als Mengenrueckgang — Bewertung im Budget zwingend.

## Mustertexte
**Antrag auf Anhebung Notfallstufe:**
> Wir beantragen die Eingruppierung in Notfallstufe [2/3] nach G-BA Notfallstufen-RL. Strukturmerkmale: Anlage 1 (Personal 24/7), Anlage 2 (Geraete), Anlage 3 (Intensivanbindung), Anlage 4 (Schlaganfall-/Trauma-Anbindung). Wir bitten um Bestaetigung der Stufeneingruppierung mit Wirkung [Datum].

**Sicherstellungszuschlag-Antrag:**
> Antrag nach § 17b Abs. 1a KHEntgG. Begruendung: Distanz zum naechsten Versorger [km], Bevoelkerungsdichte [Zahl], saisonale Spitzenlasten, fehlende Alternativen. Anlage: Erreichbarkeitsanalyse Land.

## Typische Fehler
- Notfallstufe als reines Verguetungsthema lesen; sie ist primaer Strukturqualitaet.
- Sicherstellungszuschlag mit Notfallstufenzuschlag verwechseln (unterschiedliche Rechtsgrundlagen).
- Bei Stufenverlust Personaldisposition nicht anpassen — Kosten bleiben, Erloese sinken.
- Strukturpruefung des MD nicht ernsthaft begleitet; spaeter Widerspruch erschwert.

## Querverweise
- `leistungsgruppen-und-qualitaetskriterien-reformlogik`
- `sektorenuebergreifende-versorgung-level-ii-klinik`
- `rettungsdienst-schnittstelle-aufnahme-pflicht`
- `triage-notaufnahme-ueberlastung-dokumentation`
- `khentgg-budgetverhandlung-drg-pepp-abgrenzung`
- `landeskrankenhausplan-aufnahme-herausnahme-aenderung`

## Quellen Stand 06/2026
- SGB V § 136c.
- G-BA Notfallstufen-RL (Live-Check g-ba.de).
- KHEntgG §§ 9 Abs. 1a, 17b Abs. 1a.
- KHVVG-Konkretisierungen 2025/2026 (Live-Check BMG).
- BSG, staend. Rspr. zu Notfallzuschlaegen und Versorgungsauftrag.

## 2. `patientenbeschwerde-und-risikomanagement`

**Fokus:** Patientenbeschwerde und Risikomanagement: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Patientenbeschwerde und Risikomanagement

## Fachkern: Patientenbeschwerde und Risikomanagement
- **Spezialgegenstand:** Patientenbeschwerde und Risikomanagement. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Patientenbeschwerde und Risikomanagement** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `personaluntergrenzen-pflege-ppugv`

**Fokus:** Pflegepersonaluntergrenzen-Verordnung (PpUGV): pflegesensitive Bereiche, Quotenberechnung, Schichten, Meldepflicht, Sanktionen und Strukturpruefung.

# Personaluntergrenzen Pflege PpUGV

## Fachkern: Personaluntergrenzen Pflege PpUGV
- **Spezialgegenstand:** Personaluntergrenzen Pflege PpUGV. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Die **Pflegepersonaluntergrenzen-Verordnung (PpUGV)** auf Grundlage § 137i SGB V definiert Mindestbesetzungen in pflegesensitiven Bereichen (z. B. Intensivmedizin, Geriatrie, Kardiologie, Unfallchirurgie). Verstoesse fuehren zu Verguetungsabschlaegen und Sanktionen.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche pflegesensitiven Bereiche fuehrt die Klinik?
- Sind die Quoten (Patient:Pflege-Verhaeltnis) in Tag-/Nachtschicht erreicht?
- Liegen Meldungen ans InEK rechtzeitig vor?
- Drohen Verguetungsabschlaege, Strukturpruefung, Aufsichtsmassnahmen?
- Gibt es Ausnahme- oder Uebergangsregelungen (Notfall, Ueberhang)?

## Rechtlicher Rahmen
- **SGB V § 137i** Rechtsgrundlage fuer PpUGV.
- **PpUGV** in der jeweils aktuellen Fassung; jaehrlich angepasst.
- **KHEntgG § 8 Abs. 4** Sanktionen bei Verstoss.
- **InEK-Vorgaben** zur Datenmeldung (Quartalsmeldung).
- **Pflegepersonalbemessung (PPR 2.0)** ergaenzt PpUGV, ueber § 137k SGB V derzeit in Konkretisierung.
- **TVoeD/Tarifrecht** Personalplanung und Ueberlastungsanzeigen.

## / Schritt fuer Schritt
1. **Pflegesensitive Bereiche identifizieren:** PpUGV-Anlage, Stationsschluessel.
2. **Quote berechnen:** Pflegekraefte (examiniert + Helfer mit Anrechnung) gegen Patienten je Schicht.
3. **Meldungen pruefen:** Quartalsweise InEK-Meldung; Korrekturmoeglichkeiten beachten.
4. **Sanktion vermeiden:** Bei Untergrenzverletzung Ueberlastungsanzeigen, Personalpoolnutzung, Verlegungen.
5. **Strukturpruefung vorbereiten:** MD-Pruefung kann PpUGV-Daten heranziehen.
6. **Ausnahmen pruefen:** Notfall (Bereitschaftsdienst, kurzfristige Erkrankung), Genehmigungstatbestaende.

## Trade-off-Matrix

| Mangellage | Reaktion | Folge |
|---|---|---|
| temporaere Untergrenzverletzung | Verlegung, Schliessung Betten | Erloesreduktion akut |
| dauerhafte Untergrenz-Luecke | Personal aufbauen | Kostendruck, oft alternativlos |
| Meldepflichtverletzung | Selbstanzeige | mildere Sanktion |
| Quotenfehlinterpretation | Klage gegen Bescheid | Verfahrensdauer |

## Praxistipps
- PpUGV-Bereiche werden schrittweise erweitert; Live-Check g-ba.de und gkv-spitzenverband.de.
- Pflegepool, Leiharbeit anrechnen nur, wenn examiniert und im Stationsplan.
- PPR 2.0 (§ 137k SGB V) wird Pflegepersonalbemessung erweitern (Live-Check Konkretisierung).
- Ueberlastungsanzeigen rechtssicher dokumentieren — Beweismittel bei MD-Pruefung.
- Bei wiederholten Verstoessen droht Landesaufsicht (§§ … LKHG).

## Mustertexte
**Internes Memo zur Quote-Auswertung:**
> Pflegesensitive Bereiche der Klinik nach PpUGV: 1. Intensivstation (Erwachsene): Tagschicht Quote 1:2,5 ueberschritten (gefordert 1:2). 2. Geriatrie: 1:10 im Sollbereich. Massnahmen: 1. … 2. … Meldung InEK [Datum].

**Antwortschreiben auf MD-Strukturpruefung:**
> Die PpUGV-Quote in der Periode [Quartal] ist nachweislich eingehalten, mit Ausnahme von Tagen … (Begruendung, Verlegungen, Ueberlastungsanzeigen). Anlagen: Dienstplanauszug, Personalmeldung InEK.

## Typische Fehler
- Pflegehelfer voll anrechnen statt mit Anrechnungsfaktor.
- Nur Soll-Besetzung melden statt Ist-Daten.
- Notfall-/Ausnahmetatbestaende nicht dokumentiert.
- Bei pflegesensitiven Bereichen falsche OPS-Zuordnung.

## Querverweise
- `leistungsgruppen-und-qualitaetskriterien-reformlogik`
- `arbeitszeit-bereitschaftsdienst-rufdienst`
- `pflegebudget-vereinbarung-nachweis-risiken`
- `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung`
- `intensivmedizin-beatmung-verlegung`
- `landesaufsicht-krankenhausaufsicht-beanstandung`

## Quellen Stand 06/2026
- SGB V §§ 137i, 137k.
- PpUGV (Live-Check bundesgesundheitsministerium.de, gkv-spitzenverband.de).
- InEK-Datenmeldungsregularien (Live-Check g-drg.de).
- BSG, staend. Rspr. zu Personalvorgaben und Verguetungsabschlaegen.
- DKG-Empfehlungen zur PpUGV-Umsetzung.
