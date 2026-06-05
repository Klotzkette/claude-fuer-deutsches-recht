---
name: aufbewahrung-beweislast-dora-it
description: "Aufbewahrung Beweislast Dora IT: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Aufbewahrung Beweislast Dora IT

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Aufbewahrung Beweislast Dora IT** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dokumentation-aufbewahrung-beweislast` | Krankenhaus-Dokumentation, Aufbewahrungsfristen und Beweislast: § 630f BGB, RoeV/StrlSchV, BO-Aerzte, GoBD, DSGVO, Aufbewahrung 10 bis 30 Jahre und elektronische Patientenakte (ePA). |
| `dora-und-it-dienstleister-soweit-einschlaegig` | DORA und IT-Dienstleister soweit einschlägig: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `entlassmanagement-39-abs-1a-sgb-v` | Entlassmanagement nach § 39 Abs. 1a SGB V: Rahmenvertrag Entlassmanagement, Patienteneinwilligung, Verordnungsbefugnis (AU, Heil-/Hilfsmittel, AM), Schnittstelle ambulante Versorgung. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Aufbewahrung Beweislast Dora IT**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dokumentation-aufbewahrung-beweislast`

**Fokus:** Krankenhaus-Dokumentation, Aufbewahrungsfristen und Beweislast: § 630f BGB, RoeV/StrlSchV, BO-Aerzte, GoBD, DSGVO, Aufbewahrung 10 bis 30 Jahre und elektronische Patientenakte (ePA).

# Dokumentation Aufbewahrung Beweislast

## Fachkern: Dokumentation Aufbewahrung Beweislast
- **Spezialgegenstand:** Dokumentation Aufbewahrung Beweislast. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Die Krankenhausdokumentation ist Pflicht (§ 630f BGB, MBO-Aerzte), Verguetungsgrundlage (MD-Pruefung), Compliance-Schutz und im Streit oft die einzige Verteidigung. Aufbewahrungsfristen liegen zwischen 10 Jahren (Standard) und 30 Jahren (Strahlentherapie, Bluttransfusion), je nach Materie.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche Doku-Pflicht ist betroffen (Aerztlich, Pflege, Aufklaerung, Strahlentherapie, Blut)?
- Ist analog/digital gefuehrt? Liegen Manipulationssicherung und Versionierung vor?
- Welche Aufbewahrungsfrist gilt (10, 15, 30 Jahre)?
- Wird die Akte fuer Patient, MD, Gericht oder Aufsicht verlangt?
- Drohen Beweislastnachteile bei Behandlungsfehlerklage (§ 630h BGB)?

## Rechtlicher Rahmen
- **BGB § 630f** Dokumentationspflicht des Behandelnden, Sofort, dauerhaft, vollstaendig.
- **BGB § 630h Abs. 3** Beweislastumkehr bei Dokumentationsfehlern (vermutet: nicht durchgefuehrt).
- **MBO-Aerzte § 10** Aufbewahrungspflicht 10 Jahre, ggf. laenger.
- **RoeV § 28 Abs. 3 StrlSchG, § 85 StrlSchV** 30 Jahre Roentgen/Strahlentherapie.
- **TFG (Transfusionsgesetz)** Aufbewahrung Blutprodukte-Dokumentation 30 Jahre (§ 14 Abs. 3 TFG).
- **GoBD** elektronische Buchfuehrung (Patientenakte ist auch Geschaeftsunterlage).
- **DSGVO Art. 5, 17, 18** Datenschutz, Speicherbegrenzung, Loeschpflicht nach Ablauf.
- **SGB X § 84** Aufbewahrung sozialrechtliche Unterlagen.

## / Schritt fuer Schritt
1. **Aktenklassen identifizieren:** Aerztlich, Pflege, Aufklaerung, Bildgebung, OP, Anaesthesie, Blut, Labor.
2. **Aufbewahrungsfrist je Klasse:** Standard 10 Jahre, Roentgen/Strahlentherapie 30 Jahre, Blut 30 Jahre, Geburten 30 Jahre (haftungsrechtlich BGH).
3. **Form pruefen:** Analog vs. digital, ePA-Anbindung, Manipulationssicherheit.
4. **Versionierung sichern:** Aenderungen § 630f Abs. 2 BGB nachvollziehbar.
5. **Loeschplan nach Frist:** DSGVO-konforme Vernichtung.
6. **Beweislastpruefung bei Streit:** Lueche zur Pflichtdoku → § 630h Abs. 3 BGB Beweislastumkehr.

## Trade-off-Matrix

| Aktenklasse | Mindestfrist | Praxisfrist |
|---|---|---|
| Allg. aerztliche Doku | 10 Jahre (§ 630f Abs. 3) | 30 Jahre wegen Verjaehrung (BGH) |
| Roentgen, Strahlentherapie | 30 Jahre (StrlSchV) | 30 Jahre |
| Transfusion Blut | 30 Jahre (TFG) | 30 Jahre |
| Geburten | empfohlen 30 Jahre | mind. bis Volljaehrigkeit + 3 Jahre |
| Wahlleistungen, Vertraege | 6/10 Jahre (HGB/AO) | 10 Jahre |
| Forschungsdaten (klinische Studie) | 10-25 Jahre (GCP) | je nach Pruefer |

## Praxistipps
- Lange Verjaehrungsfrist Behandlungsfehler (§ 199 BGB: 3 Jahre ab Kenntnis, Hoechstfrist 30 Jahre); deshalb Praxis 30 Jahre archivieren.
- Digitale Akte muss revisionssicher sein (GoBD), inkl. Zeitstempel und Berechtigungskonzept.
- Aerztliche und pflegerische Doku zeitnah, nicht retrospektiv "geglaettet".
- Aufklaerungsdoku ist Schlachtfeld bei Haftungsstreit — Vordrucke + handschriftliche Notiz schaffen Authentizitaet.
- DSGVO: Loeschung nach Frist Pflicht; Aufbewahrungspflicht bricht aber Loeschanspruch (Art. 17 Abs. 3 lit. b).

## Mustertexte
**Internes Memo zur Aufbewahrungspflicht:**
> Klassifizierung Krankenhausakten. Klasse A (allg. aerztlich): 30 Jahre. Klasse B (Roentgen, Strahlentherapie): 30 Jahre. Klasse C (Transfusion Blut): 30 Jahre. Klasse D (Geburten): 30 Jahre. Klasse E (Wahlleistungen/Vertraege): 10 Jahre. Verantwortlich: Archivleitung, Vertretung: …

**Verteidigung gegen Doku-Vorwurf:**
> Die in der Klagebegruendung behauptete Dokumentationsluecke besteht nicht. Anlage A enthaelt den vollstaendigen Pflegebericht; Anlage B den Aerztlichen Verlauf; Anlage C die Aufklaerungsdokumentation. Eine Beweislastumkehr nach § 630h Abs. 3 BGB liegt nicht vor.

## Typische Fehler
- Aufbewahrung nur 10 Jahre — bei Spaetfaellen Beweisnot.
- Digitale Akte ohne Manipulationssicherheit.
- Aufklaerungsdokumente nicht in Patientenakte integriert.
- Loeschen nach Frist ohne Pruefung etwa laufender Verfahren.
- Pflegedokumentation lueckenhaft — § 630h-Risiko.

## Querverweise
- `patientenrechte-behandlungsvertrag-aufklaerung`
- `datenschutz-krankenhaus-patientenakte-forschung`
- `haftpflichtfall-krankenhaus-gutachtenstrategie`
- `blutprodukte-transfusionsrecht-dokumentation`
- `strahlenschutz-radiologie-nuklearmedizin`
- `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung`

## Quellen Stand 06/2026
- BGB §§ 630a-630h.
- StrlSchG § 28, StrlSchV § 85.
- TFG § 14.
- MBO-Aerzte § 10.
- BGH, staend. Rspr. zur Aufbewahrungsdauer (Haftungsverjaehrung).
- GoBD, DSGVO Art. 5, 17, 18.

## 2. `dora-und-it-dienstleister-soweit-einschlaegig`

**Fokus:** DORA und IT-Dienstleister soweit einschlägig: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# DORA und IT-Dienstleister soweit einschlägig

## Fachkern: DORA und IT-Dienstleister soweit einschlägig
- **Spezialgegenstand:** DORA und IT-Dienstleister soweit einschlägig. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: DORA und IT-Dienstleister soweit einschlägig** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `entlassmanagement-39-abs-1a-sgb-v`

**Fokus:** Entlassmanagement nach § 39 Abs. 1a SGB V: Rahmenvertrag Entlassmanagement, Patienteneinwilligung, Verordnungsbefugnis (AU, Heil-/Hilfsmittel, AM), Schnittstelle ambulante Versorgung.

# Entlassmanagement § 39 Abs. 1a SGB V

## Fachkern: Entlassmanagement § 39 Abs. 1a SGB V
- **Spezialgegenstand:** Entlassmanagement § 39 Abs. 1a SGB V. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Das Krankenhaus muss Patienten geordnet entlassen und die naehtlose Anschlussversorgung sichern — § 39 Abs. 1a SGB V. Kernelemente: schriftliche Patienteneinwilligung, Entlassmanagementplan, befristete Verordnungsbefugnis fuer Arzneimittel, Heil-/Hilfsmittel, Soziotherapie, AU-Bescheinigung; Uebergabe an Vertragsarzt.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Liegt schriftliche Patienteneinwilligung vor (Modul der Aufnahme oder gesondert)?
- Welche Anschlussversorgung wird benoetigt (Pflege, Reha, ambulante Therapie, Hilfsmittel)?
- Sind Verordnungen ausgestellt (Arzneimittel max. 7 Tage Wirkdauer, Heilmittel max. 7 Tage, AU max. 7 Tage)?
- Ist die Schnittstelle zur Reha-/Pflegedienstleistung organisiert?
- Drohen MDK-Pruefung oder Beschwerden wegen unzureichender Entlassung?

## Rechtlicher Rahmen
- **SGB V § 39 Abs. 1a** Entlassmanagement, Verordnungsbefugnis Krankenhaus.
- **Rahmenvertrag Entlassmanagement** zwischen GKV-SV, KBV, DKG.
- **SGB V §§ 73, 73a** Hausaerztliche Versorgung und Schnittstelle.
- **SGB V § 87** Bewertungsmassstab, ggf. Verguetung Entlassgespraech.
- **SGB XI** Pflegeueberleitung.
- **PatientenrechteG / BGB §§ 630a ff.** Behandlungsvertrag, Aufklaerung.

## / Schritt fuer Schritt
1. **Einwilligung einholen:** Schriftliche oder dokumentierte Einwilligung zum Entlassmanagement bei Aufnahme oder spaetestens vor Entlassung.
2. **Bedarfsabschaetzung:** Pflegeeinstufung, Reha-Bedarf, Soziotherapie, Hilfsmittel, Heilmittel, Arzneimittel.
3. **Entlassplan erstellen:** Konkrete Massnahmen, Ansprechpartner, Termine.
4. **Verordnungen ausstellen:** Befristet (max. 7 Tage) Arzneimittel, Heil-/Hilfsmittel, AU; mit Verordnungsausweis.
5. **Uebergabe an Vertragsarzt/Pflegedienst:** Schriftlich, mit Kurzarztbrief, Medikationsplan, Begleitdokumenten.
6. **Dokumentation:** Einwilligung, Entlassgespraech, Plan, Verordnungen — Aufbewahrung mind. 10 Jahre.

## Trade-off-Matrix

| Versorgungsbedarf | Werkzeug Krankenhaus | Limit |
|---|---|---|
| Arzneimittel kurzfristig | Verordnung KH | max. 7 Tage Wirkdauer |
| AU-Bescheinigung | KH-Arzt | max. 7 Tage |
| Reha | Reha-Antrag, AHB | Vorbereitung Kasse |
| Pflege | Pflegeueberleitung | SGB XI; Pflegegrad ggf. neu |
| Hilfsmittel (Rollator etc.) | KH-Verordnung | max. 7 Tage; danach Vertragsarzt |

## Praxistipps
- Einwilligung am besten in Aufnahmeunterlagen verankern (Datenschutz: separate Module).
- Medikationsplan nach § 31a SGB V immer beilegen, wenn ≥ 3 Wirkstoffe.
- Wochenend-/Feiertagsentlassungen rechtssicher absichern — Vertragsarzt nicht erreichbar.
- Pflegeueberleitung frueh starten, Pflegegrad-Antrag ggf. vorbereiten.
- Wirtschaftliche Verordnung beachten: Rabattvertraege, Aut-idem-Regelung.

## Mustertexte
**Patienteneinwilligung Entlassmanagement:**
> Ich willige in das Entlassmanagement nach § 39 Abs. 1a SGB V ein. Ich bin ueber den Zweck (geordnete Entlassung, Anschlussversorgung) und ueber meine Rechte (Widerruf, Datenschutz) informiert. Datum, Unterschrift.

**Kurzarztbrief Strukturvorlage:**
> Aufnahme: [Datum, Diagnose]. Behandlungsverlauf: … Entlassdiagnose: … Empfohlene Anschlussversorgung: 1. Vertragsarzt [Fach], 2. Pflegegrad [Antrag], 3. Reha [AHB], 4. Medikation (Plan beigefuegt), 5. Verordnungen [Liste]. Kontakt: [KH-Ansprechpartner, Tel.].

## Typische Fehler
- Einwilligung fehlt oder ist undatiert.
- Verordnungen ueberschreiten 7-Tage-Frist.
- Medikationsplan unvollstaendig.
- Reha-Antrag erst nach Entlassung — Versorgungslueche.
- Pflegeueberleitung erst am Entlasstag — Pflegegrad-Lueche.

## Querverweise
- `patientenrechte-behandlungsvertrag-aufklaerung`
- `datenschutz-krankenhaus-patientenakte-forschung`
- `dokumentation-aufbewahrung-beweislast`
- `krankenhausapotheke-arzneimittelversorgung`
- `sektorenuebergreifende-versorgung-level-ii-klinik`
- `kinder-und-jugendmedizin-besondere-versorgung`

## Quellen Stand 06/2026
- SGB V § 39 Abs. 1a.
- Rahmenvertrag Entlassmanagement (Live-Check gkv-spitzenverband.de, dkgev.de, kbv.de).
- SGB XI Pflegeueberleitung.
- BGB §§ 630a ff., PatientenrechteG.
- BSG, staend. Rspr. zur Anschlussversorgung.
