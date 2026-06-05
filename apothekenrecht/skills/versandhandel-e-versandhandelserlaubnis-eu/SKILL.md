---
name: versandhandel-e-versandhandelserlaubnis-eu
description: "Versandhandel E Versandhandelserlaubnis EU: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versandhandel E Versandhandelserlaubnis EU

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Versandhandel E Versandhandelserlaubnis EU** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versandhandel-und-e-rezept-intake` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Versandhandel und E-Rezept Intake. |
| `versandhandelserlaubnis-eu-versandapotheke` | Versandhandelserlaubnis EU Versandapotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `versorgung-pflegeheim-schnittstelle` | Versorgung Pflegeheim Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Versandhandel E Versandhandelserlaubnis EU**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versandhandel-und-e-rezept-intake`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Versandhandel und E-Rezept Intake.

# Versandhandel und E-Rezept Intake

## Fachkern: Versandhandel und E-Rezept Intake
- **Spezialgegenstand:** Versandhandel und E-Rezept Intake. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Aufnahme eines Versandhandelsfalls: Bestelleingang einer Versandapotheke, Prüfung der gesetzlichen Voraussetzungen für den Versand verschreibungspflichtiger und apothekenpflichtiger Arzneimittel, Schnittstelle zum E-Rezept. Der Skill fasst die Pflichtangaben, Beratungsdokumentation und Verbots-Sortimente zusammen — insbesondere das Rx-Versandverbot (RxVV-Diskussion) und das Versandverbot für bestimmte Arzneimittel.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Versandapotheke nimmt erstmals E-Rezept-Bestellungen entgegen.
- Beanstandung der Aufsicht wegen unzureichender Beratungsdokumentation oder Versand verbotener Arzneimittel.
- Patient bestellt rezeptpflichtiges Arzneimittel, das nicht versandt werden darf (z. B. bestimmte Kühlware, BtM, T-Rezept).
- Aufbau eines internen SOP-Pakets für Versandhandel.

Eingaben:
- Versandhandelserlaubnis (§ 11a ApoG) der inländischen Apotheke.
- Bei EU-Versandapotheke: Erlaubnis der jeweiligen EU-Behörde, Eintrag im DEAS-Register, deutsche Versandhandels-Sicherheitslogo.
- Bestelleingang (Bestellnummer, Patient, Arzneimittel, ggf. E-Rezept-Token).
- Beratungsprotokoll (telefonisch oder schriftlich), Identitätsnachweis Empfänger.

## Rechtlicher Rahmen

- **§ 11a ApoG:** Versandhandelserlaubnis für apothekenpflichtige Arzneimittel; Voraussetzungen — Apothekenerlaubnis, QM-System, Beratungsmöglichkeit, Transportbedingungen.
- **§ 73 AMG:** Verbringungsverbot, Ausnahmen.
- **§ 43 AMG:** Apothekenpflicht.
- **AMVV** und § 360 SGB V (E-Rezept-Pflicht).
- **VersandhandelsVO** (Rahmenvereinbarung GKV-Spitzenverband — Stand vom Anwender zu verifizieren).
- **Sicherheitslogo-VO** (DIMDI / BfArM-Register).
- **§ 7 HWG**, Werbeverbote.
- BGH und EuGH, staend. Rspr. zur grenzüberschreitenden Versand-Apotheke (DocMorris).

## / Schritt für Schritt

1. **Bestelleingang erfassen:** Datum, Patient, Arzneimittel, Lieferadresse, ggf. Rezept-Token.
2. **Verbots-Sortiment prüfen:**
 - BtM: kein Versand erlaubt (§ 11a Abs. 2 ApoG i.V.m. BtMG, ständige Praxis).
 - T-Rezept-Arzneimittel: kein Versand (vom Anwender zu verifizieren).
 - Bestimmte Kühlware bei nicht gesicherter Kühlkette: kein Versand.
3. **E-Rezept einlösen:** Token-Verarbeitung über TI-Anbindung (siehe Skill `e-rezept-ti-gematik-apothekenprozess`).
4. **Plausibilitätsprüfung:** Apotheker prüft Indikation, Dosierung, Kontraindikation.
5. **Beratung anbieten:** Bei jedem Versand muss Beratung erreichbar sein — Telefon, Chat, E-Mail; bei Rx Pflicht, bei OTC Angebot. Dokumentation muss revisionsfest sein.
6. **Aut-idem / Rabattvertrag** (siehe `substitution-rabattvertrag-aut-idem`).
7. **Versandvorgang:** Verpackung, Kühlkette, GDP-konformes Transportverfahren, Sendungsverfolgung.
8. **Lieferung:** Identitätsprüfung Empfänger bei Rx (Personalausweis-Foto, Kuriernachweis, Codeprüfung).
9. **Dokumentation:** Bestellnummer, Beratung, Versandbeleg, drei Jahre Aufbewahrung.

## Trade-off-Matrix

| Versandkonstellation | Zulässig | Beratung | Risiko |
|---|---|---|---|
| OTC apothekenpflichtig inländisch | ja | Beratungsangebot Pflicht | gering |
| Rx-GKV inländisch | ja, mit Erlaubnis § 11a ApoG | Pflichtberatung dokumentiert | mittel (Retax) |
| Rx aus EU-Apotheke an Patient in D | ja, bei Eintrag DEAS-Register | wie inländisch | mittel |
| BtM-Versand | nein | — | strafbewehrt |
| T-Rezept Versand | grds. nein | — | hoch |
| Kühlware ohne Kühlkette | nein | — | hoch |

## Praxistipps

- Beratungsangebot muss tatsächlich erreichbar sein — Hotline mit Öffnungszeiten, Chat mit Apothekerinnen, E-Mail-Antwort binnen 24 h.
- Sendungsverfolgung als Anti-Retax-Beweis archivieren.
- Bei Kühlware: zwischenliegende Kontrollpunkte mit Temperaturlogger, Lieferquittung mit Temperaturnachweis.
- DEAS-Eintrag bei EU-Versand prüfen; nicht-eingetragene EU-Apotheken sind in Deutschland nicht zugelassen.
- Werbeauftritt prüfen — HWG-Vorgaben gelten auch im Versandhandel; Aktionen ("Schenken statt nehmen") oft heikel.

## Mustertexte

### Beratungsprotokoll Versandhandel (Vorlage)
"Datum / Bestell-Nr.: [...] / Patient: [...] / Arzneimittel: [Name, Stärke, Menge] / E-Rezept-Token: [...] / Beratungsangebot ausgesprochen: [ja/nein] / Beratungsweg: [Telefon/Chat/E-Mail] / Inhalte: [Dosierung / Kontraindikation / Aufbewahrung / Nebenwirkungen] / Apotheker:in: [Name] / Versandbeleg-Nr.: [...]"

### Hinweis an Patient bei Versandverbot (Auszug)
"Sehr geehrte:r [Patient:in], das von Ihnen bestellte Arzneimittel [Name] gehört zu den Betäubungsmitteln nach BtMG. Ein Versand ist gesetzlich ausgeschlossen. Wir empfehlen Ihnen, dieses Arzneimittel persönlich in einer nahegelegenen Apotheke abzuholen. Selbstverständlich beraten wir Sie unter [Telefonnummer] zu Alternativen."

## Typische Fehler

- BtM versendet — Strafbarkeitsrisiko nach § 29 BtMG.
- Beratung nur "auf Wunsch" angeboten, aber kein Beratungskanal mit dokumentierter Erreichbarkeit.
- Kühlkette nicht überwacht — Insulin oder Biologika werden inaktiviert.
- EU-Versandapotheke ohne DEAS-Eintrag — Patient kauft, Apotheke wird wegen unerlaubten Versands verfolgt.
- Identitätsprüfung Empfänger bei Rx-Versand fehlt — Doppelabgabe an Dritte.

## Querverweise

- `versandhandelserlaubnis-eu-versandapotheke` (EU-Konstellation)
- `e-rezept-ti-gematik-apothekenprozess` (E-Rezept-Workflow)
- `kuehlkette-temperaturmonitoring-gdp` (Transport)
- `preisbindung-arzneimittel-ampreisv` (Preisbindung)
- `onlinewerbung-hwg-apotheken` (Werbung)
- `rezeptsammelstelle-botendienst-versandhandel` (Abgrenzung)

## Quellen Stand 06/2026

- ApoG § 11a; AMG §§ 43, 73; AMVV; SGB V § 360.
- BfArM DIMDI-Sicherheitslogo-Register; DEAS-Register EU-Versandapotheken.
- BGH staend. Rspr. zum Apothekenversand und Wettbewerbsrecht.
- EuGH staend. Rspr. zur Grenzüberschreitung (DocMorris).
- ABDA-Hinweise zum Versandhandel (vom Anwender zu verifizieren).

## 2. `versandhandelserlaubnis-eu-versandapotheke`

**Fokus:** Versandhandelserlaubnis EU Versandapotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Versandhandelserlaubnis EU Versandapotheke

## Fachkern: Versandhandelserlaubnis EU Versandapotheke
- **Spezialgegenstand:** Versandhandelserlaubnis EU Versandapotheke. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Erlaubnis zum Versandhandel mit apothekenpflichtigen Arzneimitteln in Deutschland — sowohl für inländische Apotheken (§ 11a ApoG) als auch für EU-/EWR-Apotheken (anerkanntes Verfahren, § 73 Abs. 1 Nr. 1a AMG). Dieser Skill behandelt den Erlaubnis- und Anerkennungsprozess, Eintragung im Sicherheitslogo-Register sowie Sortimentsgrenzen, Beratungspflicht und Aufsichtsregime.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Inländische Apotheke will Versandhandelserlaubnis beantragen.
- EU-Apotheke (z. B. NL, IS) will deutschen Markt bedienen.
- Aufsicht beanstandet fehlenden DEAS-Eintrag.
- Werbliche Auftritt einer EU-Apotheke in D wird wettbewerbsrechtlich angegriffen.
- Wechsel des Versandlogistik-Dienstleisters.

Eingaben:
- Apothekenerlaubnis (inländisch) oder ausländische Apothekenerlaubnis nach EU-/EWR-Recht.
- QM-Handbuch mit Versand-SOPs (Annahme, Verpackung, Kühlkette, Reklamation).
- Beratungskonzept (Hotline, Chat, E-Mail) mit Öffnungszeiten und Personal.
- Anschriften von Hauptapotheke und Versandlager (müssen identisch oder vertraglich gebunden sein).
- Bei EU: Anerkennungsbescheid und nationale Apothekenerlaubnis im Herkunftsland.

## Rechtlicher Rahmen

- **§ 11a ApoG:** Inländische Versandhandelserlaubnis — Voraussetzungen: bestehende Apotheke, QM, Beratungssystem, sichere Verpackung, dokumentierte Transportkette.
- **§ 73 Abs. 1 Nr. 1a AMG:** Zulässigkeit des Versands aus EU-/EWR-Staaten an Endverbraucher in D, sofern gleichwertige Erlaubnis im Herkunftsland vorliegt.
- **§ 11a Abs. 1 Nr. 4 ApoG:** Pflicht zur Eintragung im Sicherheitslogo-Register (DIMDI / BfArM).
- **Richtlinie 2011/62/EU** (Fälschungsrichtlinie) und delegierte Verordnung 2016/161 (Securpharm).
- **AMVV** für Rx-Versand.
- **SGB V § 360** (E-Rezept).
- BGH und EuGH staend. Rspr. (DocMorris, Apothekenpreisbindung, Versandhandelsverbot).
- **§ 7 HWG** und § 11 HWG zur Werbebeschränkung.

## / Schritt für Schritt

1. **Inländische Apotheke:**
 a. Antrag bei der Landesaufsicht (§ 11a Abs. 1 ApoG).
 b. Vorlage QM-Handbuch, SOPs Versand, Beratungskonzept, Transportverträge.
 c. Inspektion durch Aufsicht (möglich).
 d. Bescheidserteilung, Eintragung im Sicherheitslogo-Register beim BfArM.

2. **EU-Apotheke:**
 a. Apothekenerlaubnis nach Heimatlandrecht muss bestehen und Versand erlauben.
 b. Anmeldung beim BfArM zum Sicherheitslogo-Register (DIMDI-Verfahren).
 c. Anerkennungserklärung; ggf. Vorlage Übersetzungen.
 d. Eintragung — erst danach legaler Versand nach D.

3. **Sortimentsgrenzen:** BtM und T-Rezept-Arzneimittel sind nicht versandfähig. Bestimmte Kühlware nur mit lückenloser Kühlkette. Apothekenpflichtige Arzneimittel — ja. Apothekenexklusive Waren (z. B. bestimmte Diagnostika) — vom Anwender zu verifizieren.

4. **Beratungssystem:** Hotline Apothekerinnen erreichbar; Aufzeichnung Beratungspflicht-Inhalte (Rx zwingend, OTC angeboten).

5. **Aufsicht:** Landesaufsicht in D auch für EU-Versandapotheken bei Beanstandungen im deutschen Markt zuständig (§ 78 AMG und Aufsichtsregelung). Wettbewerbsrechtlich auch BGH und OLG.

## Trade-off-Matrix

| Konstellation | Inländisch (§ 11a ApoG) | EU-Versand (§ 73 AMG) |
|---|---|---|
| Erlaubnisbehörde | Landesaufsicht | Heimatlandbehörde + BfArM-Eintrag |
| Sicherheitslogo | Pflicht | Pflicht |
| Kontrolldichte | Standard ApBetrO + Versand | Heimatland + deutsche Marktkontrolle |
| Preisbindung | AMPreisV | strittig, BGH-Rspr. beachten |
| BtM-Versand | nein | nein |
| E-Rezept-Einlösung | über TI | über TI, Schnittstelle erforderlich |

## Praxistipps

- Sicherheitslogo (DIMDI / BfArM) auf jeder Webseite eingebunden und mit Echtheits-Klick verlinkt — fehlende Verlinkung führt zu Beanstandungen.
- DEAS-Register: regelmässig prüfen, ob Eintrag noch besteht.
- EU-Versandapotheken müssen die deutsche AMPreisV bei Rx GKV beachten (vom Anwender Aktualität zu prüfen, BGH-Rspr.).
- Beratungssystem: tatsächliche Erreichbarkeit zu üblichen Zeiten; bei Pannen Tagesprotokoll führen.
- Bei EU-Versand und gleichzeitiger inländischer Niederlassung: getrennte Geschäftsführung dokumentieren, sonst Fremdbesitz-Risiko.

## Mustertexte

### Antrag Versandhandelserlaubnis nach § 11a ApoG (Auszug)
"Hiermit beantrage ich, [Apothekenname], Apothekenerlaubnis vom [Datum], die Erteilung der Versandhandelserlaubnis nach § 11a ApoG. Beigefügt sind: 1. Aktuelles QM-Handbuch (Stand [Datum]), 2. SOP-Versand-Paket (SOP-Nr. [...]), 3. Beratungskonzept mit Hotline [Nummer] (Öffnungszeiten Mo-Fr 8-20 Uhr, Sa 8-14 Uhr), 4. Transportvertrag [Logistikpartner] mit GDP-Bestätigung, 5. Übersicht Kühlkette inkl. Datenlogger. Wir erklären, die Sortimentsgrenzen einzuhalten (kein BtM-, kein T-Rezept-Versand)."

### Anmeldung zum Sicherheitslogo-Register (Auszug)
"Hiermit melde ich, [Apothekenname, Anschrift], die Apotheke zur Aufnahme in das nationale Verzeichnis der zum Versandhandel berechtigten Apotheken (DIMDI / BfArM) an. Beigefügt sind: 1. Versandhandelserlaubnis vom [Datum], Az [...], 2. Webseiten-URL, auf der das Logo eingebunden wird, 3. Erklärung, das Logo nur in der vorgegebenen Form zu nutzen."

## Typische Fehler

- Eintrag im Sicherheitslogo-Register fehlt — Apotheke versendet trotzdem; UWG-Risiko.
- Logo wird auf der Webseite ohne Klick-Verifikation eingebaut.
- BtM oder T-Rezept-Arzneimittel werden mit versandt — strafbewehrt.
- Beratungssystem ist nur formell — keine echte Erreichbarkeit, keine Dokumentation.
- EU-Apotheke verschickt an Patient in D ohne Anerkennung — Aufsichtsbeanstandung, ggf. wettbewerbsrechtliche Unterlassungsklage.

## Querverweise

- `versandhandel-und-e-rezept-intake` (operativer Workflow)
- `e-rezept-ti-gematik-apothekenprozess` (TI-Anbindung)
- `securpharm-faelschungsschutz` (Verifikation)
- `kuehlkette-temperaturmonitoring-gdp` (Kühlkette)
- `preisbindung-arzneimittel-ampreisv` (Preisbindung)
- `onlinewerbung-hwg-apotheken` (HWG)
- `digitale-plattformen-marktplatz-apothekenrecht` (Plattformen)

## Quellen Stand 06/2026

- ApoG § 11a; AMG § 73 Abs. 1 Nr. 1a.
- BfArM DIMDI-Sicherheitslogo-Register.
- Richtlinie 2011/62/EU + delegierte VO 2016/161/EU.
- EuGH, staend. Rspr. (DocMorris-Komplex).
- BGH, staend. Rspr. zur Preisbindung im EU-Versandhandel (vom Anwender zu verifizieren Aktualität).
- Landesaufsichtsbehörden — Erlaubnisleitfäden (vom Anwender zu verifizieren).

## 3. `versorgung-pflegeheim-schnittstelle`

**Fokus:** Versorgung Pflegeheim Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Versorgung Pflegeheim Schnittstelle

## Fachkern: Versorgung Pflegeheim Schnittstelle
- **Spezialgegenstand:** Versorgung Pflegeheim Schnittstelle. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Versorgung Pflegeheim Schnittstelle** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

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
