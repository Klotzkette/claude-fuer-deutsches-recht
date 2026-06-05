---
name: pharmazeutische-dienstleistungen-preisangaben
description: "Pharmazeutische Dienstleistungen Preisangaben: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pharmazeutische Dienstleistungen Preisangaben

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pharmazeutische Dienstleistungen Preisangaben** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pharmazeutische-dienstleistungen-verguetung` | Pharmazeutische Dienstleistungen Vergütung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `preisangaben-e-commerce-apotheke` | Preisangaben E-Commerce Apotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `preisbindung-arzneimittel-ampreisv` | Preisbindung Arzneimittel AMPreisV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Pharmazeutische Dienstleistungen Preisangaben**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pharmazeutische-dienstleistungen-verguetung`

**Fokus:** Pharmazeutische Dienstleistungen Vergütung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Pharmazeutische Dienstleistungen Vergütung

## Fachkern: Pharmazeutische Dienstleistungen Vergütung
- **Spezialgegenstand:** Pharmazeutische Dienstleistungen Vergütung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Seit der ApothekenstärkungsG-Reform 2020 und nachfolgenden Vereinbarungen können Apotheken zusätzliche pharmazeutische Dienstleistungen (pDL) erbringen und gegenüber GKV abrechnen. Beispiele: erweiterte Medikationsberatung, Blutdruckmessung im Rahmen der Polymedikationsanalyse, Inhalator-Training, Beratung von Patienten mit Krebsmedikation. Die Vergütung erfolgt aus einem festen Topf (Apothekenhonorar) und ist an strikte Voraussetzungen geknüpft.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Apotheke will pDL anbieten und abrechnen.
- Krankenkasse weist Abrechnung zurück — formale Mängel.
- Patient verlangt pDL — Voraussetzungen prüfen.
- Personalqualifikation (Apotheker, Fortbildung) klären.
- Vereinbarkeit mit ärztlicher Aufgabenverteilung.

Eingaben:
- Versicherter mit konkretem Bedarf (Polymedikation, Inhalator, neue Onkologie-Therapie).
- Apothekenstamm-Daten in ABDA-Modulen.
- Fortbildungsnachweise des durchführenden Apothekers.
- Beratungsprotokoll mit standardisierten Formularen.

## Rechtlicher Rahmen

- **§ 1a, § 129 Abs. 5e SGB V:** Rechtsgrundlage pDL.
- **Rahmenvertrag pDL** (zwischen DAV und GKV-Spitzenverband, Stand vom Anwender zu verifizieren) — Anlage mit Leistungskatalog, Vergütung, Voraussetzungen.
- **ApBetrO §§ 12, 12a:** Beratungspflicht; pDL gehen über Standard-Beratung hinaus.
- **§§ 31, 33 SGB V:** Arzneimittel- und Hilfsmittelversorgung.
- **§ 73 SGB V:** Wirtschaftlichkeit, Abgrenzung zur ärztlichen Tätigkeit.
- **DSGVO Art. 9** bei Gesundheitsdaten-Verarbeitung.
- Berufsordnung Apothekerkammer — Zulässigkeit, Werbeauftritt.

## / Schritt für Schritt

1. **Leistungskatalog prüfen:** Welche pDL-Leistung ist vergütungsfähig? Aktueller Stand Rahmenvertrag.
2. **Patienten-Anspruch prüfen:** Versichertenstatus, Indikation (z. B. mind. fünf systematisch eingenommene Arzneimittel für Polymedikationsanalyse).
3. **Einwilligung Patient:** Schriftliche Einwilligung zur Datenverarbeitung (DSGVO Art. 9 Abs. 2 lit. a) und zur Leistungserbringung.
4. **Durchführung:** Standardisierte Protokolle nutzen (z. B. ABDA-Vorlagen). Apotheker:in mit Fortbildung muss persönlich tätig werden.
5. **Dokumentation:** Protokoll mit Datum, Patient, Inhalt, festgestellten Auffälligkeiten, Empfehlungen, ggf. Übermittlung an Hausarzt.
6. **Abrechnung:** Abrechnungscode des Rahmenvertrags, Versichertenstammdaten, Apothekenname.
7. **Aufbewahrung:** Drei Jahre, DSGVO-konform.
8. **Werbung:** Keine reisserische Werbung; sachliche Information zulässig (§ 11 HWG, BO).

## Trade-off-Matrix

| Leistung | Voraussetzung Apotheke | Vergütung | Patient |
|---|---|---|---|
| Polymedikationsanalyse | Fortbildung Apotheker | Vergütung im pDL-Topf | mind. fünf chronische AM |
| Inhalator-Training | Schulung | Pauschale | Asthma/COPD-Patient |
| Beratung bei oraler Krebstherapie | spezifische Fortbildung | Pauschale | onkologischer Patient |
| Blutdruckmessung allein | regulär | nicht GKV-vergütet (Selbstzahler-IGeL-ähnlich) | jeder |
| Impfberatung (allgemein) | Apotheker | je nach Lage; ggf. Honorar als Impfdienstleistung | — |

## Praxistipps

- Pdl ist eine **eigenständige Leistung** zusätzlich zur Standard-Beratung; nicht doppelt abrechnen.
- Standardisierte Formulare verwenden — verkürzt Dokumentationszeit und sichert Abrechnungsfähigkeit.
- Fortbildungsnachweise aktuell halten — bei Kontrolle vorzeigen können.
- Patientenakte (Sub-Akte in Apotheken-Software) führen; DSGVO-Verarbeitungsverzeichnis aktualisieren.
- Keine ärztliche Diagnostik betreiben — Grenze einhalten, sonst Berufsrechtskonflikt mit Ärzteschaft.

## Mustertexte

### Einwilligung Patient (Auszug)
"Ich, [Name, Geb.-Datum], willige ein, dass die Apotheke [Name] eine pharmazeutische Dienstleistung (Polymedikationsanalyse) für mich erbringt. Die Apotheke darf hierzu meine Gesundheitsdaten (verordnete Arzneimittel, Vorerkrankungen, Allergien) erheben und verarbeiten (Art. 9 Abs. 2 lit. a DSGVO). Die Daten werden für die Dauer von drei Jahren aufbewahrt. Eine Übermittlung an meinen Hausarzt erfolgt [ja/nein] mit meiner Einwilligung. Ich kann meine Einwilligung jederzeit widerrufen."

### Abschlussprotokoll Polymedikationsanalyse (Auszug)
"Datum / Apotheker:in: [...] / Patient: [Name, Geb.-Datum] / Versicherung: [Kasse, Nr.] / Erfasste Arzneimittel: [Liste mit Wirkstoff, Stärke, Dosierung] / Auffälligkeiten: 1. Interaktion [Wirkstoff A + B]; 2. Dosierungsfehler [...]; 3. fehlende Anwendungsinformation [...] / Empfehlung: [Konkrete Massnahmen] / Übermittlung Hausarzt: [ja/nein] / Patientenkopie: [ja, Empfangsbestätigung]"

## Typische Fehler

- pDL ohne Patienteneinwilligung — DSGVO-Verstoss.
- Abrechnung pDL ohne Fortbildungsnachweis Apotheker:in — Rückforderung.
- Doppelabrechnung Standard-Beratung + pDL für gleiche Leistung.
- Werbung mit pDL als "Gesundheits-Check" überschreitet HWG-Grenzen.
- Dokumentation nicht patientenbezogen — bei Stichprobenprüfung nicht nachweisbar.

## Querverweise

- `amts-medikationsanalyse-beratungspflicht` (Beratungspflicht)
- `impfleistungen-in-apotheken` (Impfdienstleistung)
- `datenschutz-in-apotheke-gesundheitsdaten` (DSGVO)
- `qualitaetsmanagement-qms-sops` (SOP-Pflege)
- `kooperation-arzt-apotheke-antikorruption` (Schnittstelle Arzt)
- `apothekenbetriebsordnung-grundpflichten` (Rahmen)

## Quellen Stand 06/2026

- SGB V §§ 1a, 31, 73, 129 Abs. 5e.
- Rahmenvertrag pDL DAV / GKV-Spitzenverband (Stand vom Anwender zu verifizieren — Leistungskatalog und Vergütungssätze).
- ApBetrO §§ 12, 12a.
- DSGVO Art. 9; BDSG.
- ABDA-Fortbildungskataloge (vom Anwender zu verifizieren).
- Berufsordnungen Apothekerkammern.

## 2. `preisangaben-e-commerce-apotheke`

**Fokus:** Preisangaben E-Commerce Apotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Preisangaben E-Commerce Apotheke

## Fachkern: Preisangaben E-Commerce Apotheke
- **Spezialgegenstand:** Preisangaben E-Commerce Apotheke. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Preisangaben E-Commerce Apotheke** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `preisbindung-arzneimittel-ampreisv`

**Fokus:** Preisbindung Arzneimittel AMPreisV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Preisbindung Arzneimittel AMPreisV

## Fachkern: Preisbindung Arzneimittel AMPreisV
- **Spezialgegenstand:** Preisbindung Arzneimittel AMPreisV. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die Arzneimittelpreisverordnung (AMPreisV) bindet die Endpreise verschreibungspflichtiger Arzneimittel auf einheitliche Höhe — unabhängig davon, in welcher inländischen Apotheke das Rx eingelöst wird. Die Preisbindung gilt für GKV-Patienten und PKV gleichermassen. Diskutiert wird die Geltung gegenüber EU-Versandapotheken (EuGH 2016; BGH-Folge-Rspr.). Boni, Rabatte und Gutscheine sind nur in engen Grenzen zulässig (siehe Skill `skonti-boni-rabatte-zuweisungsverbot`).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Bonus- oder Skonto-Programm geplant, Vereinbarkeit mit AMPreisV zu prüfen.
- Wettbewerber gewährt Rabatte; Anspruch auf Unterlassung zu prüfen.
- EU-Versandapotheke unterbietet Endpreis; UWG-Verstoss?
- Preisauszeichnung im Schaufenster, Pflichtangaben.
- Frage nach zulässiger Werbung mit Preisvorteilen.

Eingaben:
- Konkrete Rabattaktion / Bonus-Modell.
- ABDA-Datenbank / Lauer-Taxe-Daten (vom Anwender bereitzustellen).
- Geschäftliche Kommunikation, Werbung, Onlineshop-Auftritt.
- ggf. Schreiben Wettbewerber oder Verband Sozialer Wettbewerb.

## Rechtlicher Rahmen

- **§ 78 AMG:** Pflicht zur Festlegung von Preisspannen in der AMPreisV.
- **AMPreisV** (Arzneimittelpreisverordnung): bindender Endpreis-Berechnungspfad — Herstellerabgabepreis (HAP), Apothekenzuschlag (3 Prozent + Festbetrag), MwSt.
- **§ 7 HWG:** Verbot von Geschenken/Zuwendungen über § 7 Abs. 1 HWG-Grenzen hinaus; Ausnahme geringwertige Kleinigkeiten.
- **§ 78 Abs. 1 S. 4 AMG i.V.m. § 8 AMPreisV:** Festlegung des einheitlichen Endpreises für Rx GKV.
- **EuGH 19.10.2016, C-148/15** (DocMorris): Preisbindung gegen ausländische EU-Versandapotheken EU-rechtswidrig (vom Anwender Aktualität zu verifizieren).
- BGH-Folge-Rspr., staend. Rspr.
- **UWG § 3a** (Verstoss gegen Marktverhaltensregel) bei Rabatten oder Boni.

## / Schritt für Schritt

1. **Status des Arzneimittels:** Rx oder OTC? Preisbindung gilt für Rx; OTC-Preise sind freigegeben.
2. **Preiskette nachvollziehen:** HAP, Grosshandelszuschlag, Apothekenzuschlag, MwSt.
3. **Geplante Aktion einordnen:**
 - Echter Preisrabatt auf Rx: unzulässig (Inland), für EU-Versand teilweise zulässig (BGH-Rspr.).
 - Sachbonus, Gutschein, Punktesystem: Wertgrenze beachten (HWG-Geringwertigkeit, in der Rspr. um 1 Euro/Aktion umstritten).
 - Beratung als Mehrwertleistung: unproblematisch.
 - Kostenfreier Botendienst innerorts: regelmässig zulässig.
4. **Wettbewerbsrechtliche Würdigung:** Verstösse gegen Preisbindung sind UWG-relevant (§ 3a, § 8 UWG); Abmahnung, Unterlassungsklage möglich.
5. **Werbung:** HWG-konforme Werbung; keine "Schnäppchen-Preise" für Rx.
6. **Bei EU-Versand:** Aktualität BGH-Rspr. prüfen — Preisbindung gegen EU-Versandapotheken eingeschränkt anwendbar.

## Trade-off-Matrix

| Aktion | Rx Inland | OTC | EU-Versandapotheke Rx |
|---|---|---|---|
| Endpreis unterhalb AMPreisV | unzulässig | irrelevant (freier Preis) | strittig, im EuGH-Sinne ggf. zulässig |
| Gutschein 1 Euro für Folgekauf | grenzwertig, eher unzulässig | zulässig | nicht durchsetzbar inland-rechtlich |
| Bonus bei E-Rezept-Einlösung | unzulässig | zulässig | strittig |
| Kostenfreie Lieferung innerorts | regelmässig zulässig | zulässig | zulässig |
| Rabatt für Senioren auf Rx | unzulässig | zulässig | strittig |

## Praxistipps

- Bei Rabattaktionen schriftlich prüfen lassen — UWG-Abmahnungen sind teuer.
- "Apothekenbonus" über Treuepunkte ist regelmässig als unzulässige Zuwendung qualifiziert.
- Kostenlose Beratung, Patientenseminar, Gesundheitscheck — zulässig, da nicht direkt am Arzneimittelpreis hängend.
- EU-Versandapotheke-Konkurrenz: EuGH-Linie hat AMPreisV bei grenzüberschreitenden Bezügen relativiert; inländische Apotheke bleibt voll preisgebunden.
- BMG-Reform-Beobachtung: Diskussion um Apothekenhonorar (Festzuschlag) und Skonti-Streit (BGH-Linie zu Grosshandel-Skonti).

## Mustertexte

### Unterlassungsschreiben an Wettbewerber (Auszug)
"Sehr geehrte Damen und Herren, wir wurden auf eine Werbeaktion Ihres Hauses aufmerksam, in der Sie Versicherten der GKV bei Einlösung eines Rezeptes über die Höhe der Zuzahlung hinaus einen Gutschein in Höhe von [Betrag] gewähren. Diese Praxis verstösst gegen die Arzneimittelpreisverordnung i.V.m. § 78 AMG, da der Endpreis für Rx-Arzneimittel inländisch gebunden ist. Wir fordern Sie auf, bis [Frist] die Werbung einzustellen und eine strafbewehrte Unterlassungserklärung abzugeben. Andernfalls behalten wir uns die gerichtliche Geltendmachung vor."

### Internes Memo zu Bonusaktion (Auszug)
"Die geplante Aktion 'Kunden-Treuepunkte' wurde geprüft. Ergebnis: Bei Rx-Arzneimitteln verstösst die Punktegewährung gegen § 78 AMG i.V.m. AMPreisV. Empfehlung: Aktion auf OTC und apothekenübliche Waren beschränken; bei Rx ausschliesslich Beratungsmehrwerte (nicht-monetäre Vorteile) anbieten. Bei rechtlicher Unsicherheit: Konsultation Apothekerkammer und Anwalt für Apothekenrecht."

## Typische Fehler

- "Kombi-Bonus" Rx + OTC: Behörden / Gerichte rechnen Bonus dem Rx-Teil zu, AMPreisV-Verstoss.
- Treuepunkt-System ohne klare Trennung — wird als verdeckter Preisnachlass behandelt.
- "Wir gleichen den Versandhandelspreis an" — strafbewehrte Unterlassung droht.
- Botendienst über Stadtgrenzen hinaus mit Werbung "kostenfrei" — Wettbewerbsproblem.
- Werbung mit "günstigster Apotheke" für Rx — irreführend.

## Querverweise

- `skonti-boni-rabatte-zuweisungsverbot` (Boni-Detail)
- `onlinewerbung-hwg-apotheken` (HWG)
- `preisangaben-e-commerce-apotheke` (E-Commerce-Preisangaben)
- `versandhandelserlaubnis-eu-versandapotheke` (EU-Versand)
- `kooperation-arzt-apotheke-antikorruption` (Zuweisungsverbot)
- `digitale-plattformen-marktplatz-apothekenrecht` (Marktplätze)

## Quellen Stand 06/2026

- AMG § 78; AMPreisV (Stand zur Berechnung im amtlichen Bundesgesetzblatt prüfen).
- EuGH 19.10.2016, C-148/15 (DocMorris).
- BGH, staend. Rspr. zur Preisbindung und Bonusaktionen; aktuelle Bestätigung zu Skonti-Vorschriften vom Anwender zu verifizieren.
- ABDA-Stellungnahmen zur Apothekenhonorarreform (vom Anwender zu verifizieren).
- BMG-Mitteilungen zur Apothekenreform.
