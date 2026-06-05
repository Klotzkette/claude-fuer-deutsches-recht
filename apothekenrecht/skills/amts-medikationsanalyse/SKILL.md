---
name: amts-medikationsanalyse
description: "Amts Medikationsanalyse: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Amts Medikationsanalyse

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Amts Medikationsanalyse** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `amts-medikationsanalyse-beratungspflicht` | AMTS Medikationsanalyse Beratungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `apothekenbetriebsordnung-grundpflichten` | Apothekenbetriebsordnung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `apothekenerlaubnis-apog-persoenliche-voraussetzungen` | Apothekenerlaubnis ApoG persönliche Voraussetzungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Amts Medikationsanalyse**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `amts-medikationsanalyse-beratungspflicht`

**Fokus:** AMTS Medikationsanalyse Beratungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# AMTS Medikationsanalyse Beratungspflicht

## Fachkern: AMTS Medikationsanalyse Beratungspflicht
- **Spezialgegenstand:** AMTS Medikationsanalyse Beratungspflicht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: AMTS Medikationsanalyse Beratungspflicht** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 2. `apothekenbetriebsordnung-grundpflichten`

**Fokus:** Apothekenbetriebsordnung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Apothekenbetriebsordnung Grundpflichten

## Fachkern: Apothekenbetriebsordnung Grundpflichten
- **Spezialgegenstand:** Apothekenbetriebsordnung Grundpflichten. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die Apothekenbetriebsordnung (ApBetrO) regelt sämtliche operative Pflichten beim Betrieb einer öffentlichen Apotheke: Räume, Personal, Sortiment, Beratung, Dokumentation, Qualitätsmanagement (QMS), Hygiene, Defektur und Rezeptur. Die Checkliste ordnet die zwölf zentralen Grundpflichten für Selbstüberprüfung, Übernahmeprüfung und Reaktion auf eine Apothekenrevision.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Vorbereitung einer Apothekenrevision durch die Landesaufsicht.
- Übernahme einer Apotheke und Bestandsaufnahme.
- Anhörung wegen Beanstandung (z. B. fehlende Plausibilitätsprüfung, Hygienemängel).
- Neu zugelassener Apotheker, der die Mindeststandards rekapitulieren muss.

Eingaben:
- Letzter Revisionsbericht (sofern vorhanden).
- Aktuelles QM-Handbuch der Apotheke, SOP-Liste, Schulungsnachweise.
- Inventar Räume (Offizin, Labor, Nachtdienstraum, Lager, Beratungszone).
- Personalstruktur (Apotheker, PTA, PKA, Auszubildende, Boten).
- Sortimentsstruktur (Rx, OTC, BtM, apothekenpflichtige, freiverkäufliche Waren, apothekenübliche Waren).

## Rechtlicher Rahmen

- **§ 1a ApBetrO:** Begriffsbestimmungen.
- **§ 2 ApBetrO:** Apothekenleiter (Aufgaben, Verantwortung, Vertretung).
- **§ 2a ApBetrO:** Qualitätsmanagementsystem (QMS) — Pflicht zur SOP-Dokumentation, Selbstinspektion.
- **§ 3 ApBetrO:** Apothekenpersonal (Apotheker, PTA, PKA; Vertretung; Schulungen).
- **§ 4 ApBetrO:** Beschaffenheit, Größe und Einrichtung der Apothekenbetriebsräume; Mindestgrundfläche.
- **§ 5 ApBetrO:** Hygienemaßnahmen.
- **§ 6 ApBetrO:** Allgemeine Vorschriften über die Herstellung und Prüfung.
- **§§ 7–8 ApBetrO:** Rezeptur und Defektur.
- **§ 11 ApBetrO:** Sonderregelungen für die Abgabe (z.B. Notfall, Versand).
- **§ 12 ApBetrO:** Verschreibung und Abgabe (Form, Plausibilitätsprüfung am Rezept).
- **§ 16 ApBetrO:** Lagerung — Ordnung, Trennung, Temperaturkontrolle, Kühlkette.
- **§ 17 ApBetrO:** Erwerb und Abgabe von Arzneimitteln.
- **§ 18 ApBetrO:** Dokumentationspflichten Rezeptur, Defektur, BtM.
- **§ 20 ApBetrO:** Information und Beratung beim Abgabevorgang.
- **§ 21 ApBetrO:** Apothekenübliche Dienstleistungen (z.B. pharmazeutische Dienstleistungen).
- **§ 25 ApBetrO:** Apothekenübliche Waren (Abgrenzungskatalog).
- **§§ 34 ff. ApBetrO:** Krankenhausapotheken (Personal § 28, Räume § 29).

## / Schritt für Schritt

1. **Räume (§ 4 ApBetrO):** Offizin, Laboratorium, ausreichender Lagerraum und Nachtdienstzimmer; Gesamt-Grundfläche der Betriebsräume mindestens 110 Quadratmeter (§ 4 Abs. 2 Satz 3 ApBetrO). Keine fixe Einzelflächenvorgabe pro Raum; Laboratorium mit Abzug/Absaugvorrichtung. Behindertenzugang; abschliessbarer BtM-Schrank.
2. **Personal (§ 3 ApBetrO, § 7 ApoG):** Apothekerleitung anwesend oder vertretungsbefugt. PTA-Tätigkeit unter Apothekeraufsicht; Vertretungsregelung dokumentiert.
3. **QMS (§ 2a ApBetrO):** Schriftliches QM-Handbuch, SOPs für alle relevanten Prozesse (Annahme, Lagerung, Abgabe, Beratung, Notfall, Defektur, Rezeptur, Reklamation, Rückruf); regelmäßige Selbstinspektion.
4. **Beratung (§ 20 ApBetrO):** Pflicht zur Information und Beratung bei jeder Abgabe. Bei Rx zusätzlich Plausibilitätsprüfung nach § 12 ApBetrO (Vollständigkeit der Verschreibung, Dosierung, Wechselwirkungen).
5. **Dokumentation (§ 18 ApBetrO):** Prüfprotokoll für jede Rezeptur und jede Defektur. BtM-Buchführung (siehe Skill `btm-rezept-betaeubungsmittel-dokumentation`).
6. **Lagerhaltung (§ 16 ApBetrO):** Trennung, FIFO, Temperaturkontrolle dokumentiert; Kühlkette nachweisbar (siehe Skill `kuehlkette-temperaturmonitoring-gdp`).
7. **Sortiment (§ 25 ApBetrO):** Trennung Rx, OTC, apothekenpflichtig, apothekenüblich. Keine Drogeriewaren über apothekenüblichen Katalog hinaus.
8. **Hygiene (§ 5 ApBetrO):** Reinigung dokumentiert, Hygieneplan nach RKI-Empfehlung.
9. **Revisionsfähigkeit:** Alle Dokumente an einem Ort, drei Jahre Aufbewahrung (BtM zehn Jahre, § 13 BtMVV).

## Trade-off-Matrix

| Aspekt | Mindeststandard | Empfohlener Praxisstandard | Riskante Lücke |
|---|---|---|---|
| QM-Handbuch | vorhanden | jährlich aktualisiert | älter als drei Jahre, keine Datierung |
| Plausibilitätsprüfung | dokumentiert | digitales Tool mit Audit-Trail | nur mündliche Plausibilisierung |
| Temperatur Kühlkette | manuell zweimal täglich | digitale Logger mit Alarm | keine Lückenfüllung dokumentiert |
| BtM-Buch | handschriftlich/elektronisch | elektronisches BtM-System | keine tägliche Saldierung |
| Notfallplan | vorhanden | regelmässig geübt | nur Vorlage, nie geübt |

## Praxistipps

- Vor Revision Checkliste der letzten drei Revisionen abarbeiten — wiederkehrende Beanstandungen werden besonders kritisch geprüft.
- Schulungen aller Mitarbeiter mindestens einmal jährlich dokumentieren; nicht nur Teilnahmebestätigung, sondern Inhalt und Schulungsdauer.
- SOPs sollen kurz und verständlich sein, nicht jede ist sechs Seiten lang; lieber zehn klare als drei perfekte.
- Behördliche Hinweisschreiben (z. B. BfArM-Rote-Hand-Briefe) im QM-System ablegen mit Eingangsdatum und Empfangsbestätigung.

## Mustertexte

### Stellungnahme zur Revisionsfeststellung "Plausibilitätsprüfung unzureichend" (Auszug)
"Die in der Beanstandung vom [Datum] angesprochene Plausibilitätsprüfung bei der Abgabe vom [Datum] ist im System unter [Vorgangsnummer] dokumentiert. Geprüft wurden gemäss § 7 ApBetrO Indikation, Dosierung, Kontraindikation und Interaktion. Eine Sichtdokumentation als PDF-Export liegt als Anlage [Nr.] bei. Die Apothekenleitung hat zusätzlich am [Datum] eine SOP-Aktualisierung veranlasst (Anlage [Nr.])."

### SOP-Kopfzeile (Vorlage)
"SOP-Nr. [XX], Titel: [Prozess], Version: [n.n], Stand: [Datum], gültig ab: [Datum], Verantwortlich: [Name], freigegeben durch: [Apothekenleitung], Revisionszyklus: jährlich."

## Typische Fehler

- QM-Handbuch ist alt, SOPs verweisen auf Software, die nicht mehr genutzt wird.
- Plausibilitätsprüfung wird mündlich erledigt, aber nicht dokumentiert; Behörde sieht keinen Nachweis.
- Apothekenübliche Waren werden über § 25 ApBetrO hinaus angeboten (z. B. Tee, Lebensmittel ohne Indikation).
- Temperaturlücke in der Kühlkette wird nicht dokumentiert; bei Audit als nicht GDP-konform beanstandet.
- Personalengpass führt zu kurzfristiger Schliessung ohne Dienstbereitschaftsmeldung an die Aufsicht.

## Querverweise

- `apothekenrevision-vorbereitung-antwort` (Revisionsablauf)
- `qualitaetsmanagement-qms-sops` (QMS-Tiefe)
- `personal-pharmazeutisch-nichtpharmazeutisch-vertretung` (Personalstruktur)
- `raeume-ausstattung-rezeptur-defektur-labor` (Räume)
- `arzneimittelabgabe-verschreibungspflicht` (Abgabevorgang)
- `apothekenuebliche-waren-abgrenzung` (Sortimentsgrenzen)

## Quellen Stand 06/2026

- ApBetrO, aktueller Stand zur Recherche im Bundesgesetzblatt.
- BfArM-Bekanntmachungen zu Lieferengpässen, Hygiene, GDP — konkrete Bezeichnung vom Anwender zu verifizieren.
- ABDA-Leitlinien und Empfehlungen (Bundesvereinigung Deutscher Apothekerverbände) — beratend, nicht verbindlich.
- BGH und OVG-Rspr. zur Apothekenaufsicht, staend. Rspr.
- Landesapothekerkammer-Merkblätter und Revisionsleitfäden (vom Anwender zu verifizieren).

## 3. `apothekenerlaubnis-apog-persoenliche-voraussetzungen`

**Fokus:** Apothekenerlaubnis ApoG persönliche Voraussetzungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Apothekenerlaubnis ApoG persönliche Voraussetzungen

## Fachkern: Apothekenerlaubnis ApoG persönliche Voraussetzungen
- **Spezialgegenstand:** Apothekenerlaubnis ApoG persönliche Voraussetzungen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Erlaubnis zum Betrieb einer Apotheke nach §§ 1, 2 ApoG. Die Erlaubnis ist personengebunden, nicht übertragbar und an konkret bezeichnete Räume gebunden. Geprüft werden in diesem Skill ausschliesslich die **persönlichen** (subjektiven) Voraussetzungen des Apothekenleiters; sachliche Voraussetzungen (Räume, Ausstattung) sind im Skill `raeume-ausstattung-rezeptur-defektur-labor` abgebildet.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Neuerteilung einer Apothekenerlaubnis, Inhaberwechsel, Filialgründung, Wiederaufnahme nach Ruhen, Rückkehr aus dem Ausland.
- Behörde droht mit Versagung oder Widerruf wegen "Unzuverlässigkeit", "fehlender Approbation" oder Insolvenz.

Erforderliche Eingaben vom Mandanten:
- Approbationsurkunde (Apotheker:in), Staatsangehörigkeit, ggf. EU-Anerkennungsbescheid.
- Persönliche Erklärung zu Vorstrafen, laufenden Ermittlungen, anhängigen Disziplinarverfahren.
- Führungszeugnis zur Vorlage bei Behörden (§ 30 Abs. 5 BZRG, sog. "behördliches Führungszeugnis").
- Bescheinigung der zuständigen Apothekerkammer über die Mitgliedschaft.
- Nachweis der gesundheitlichen Eignung (ärztliches Zeugnis, üblicherweise Hausarzt).
- Erklärung zur wirtschaftlichen Leistungsfähigkeit (Vermögensauskunft, EVZ-Auszug).
- Bei Personengesellschaft/OHG: Gesellschaftsvertrag, Auszug aus Apothekerverzeichnis aller Gesellschafter.

## Rechtlicher Rahmen

- **§ 1 ApoG:** Apothekenbetriebspflicht und persönliche Leitung durch Apotheker.
- **§ 2 ApoG:** Erlaubnisvoraussetzungen — Approbation oder Berufserlaubnis, deutsche Staatsangehörigkeit oder Gleichstellung (EU/EWR/Schweiz), gesundheitliche Eignung, Zuverlässigkeit, wirtschaftliche Leistungsfähigkeit; Versagung bei Vorstrafen, die Apothekerberuf unwürdig erscheinen lassen.
- **§ 7 ApoG:** Persönliche Leitungspflicht — der Erlaubnisinhaber muss die Apotheke persönlich leiten.
- **§ 4 ApoG:** Widerruf und Rücknahme — bei nachträglichem Wegfall.
- **§ 8 ApoG:** Ausnahme für OHG, Erbenfortführung (max. zwölf Monate, § 13 ApoG).
- BVerfG, staend. Rspr. zu Art. 12 GG und Apothekenrecht (Apothekenurteil 1958).
- Berufsordnung der jeweiligen Landesapothekerkammer.

## / Schritt für Schritt

1. **Approbation prüfen:** Approbationsurkunde, Datum, ausstellende Behörde. Bei EU-Anerkennung: Bescheid nach §§ 4, 4a BApO.
2. **Staatsangehörigkeit:** Deutsche, EU-, EWR-, Schweizer Staatsangehörigkeit unproblematisch; Drittstaatler nur über § 2 Abs. 2 ApoG (Härtefall, Ausnahmegenehmigung).
3. **Gesundheitliche Eignung:** Aktuelles ärztliches Zeugnis (max. drei Monate alt). Suchterkrankungen, schwere psychische Erkrankungen können entgegenstehen.
4. **Zuverlässigkeit:** Führungszeugnis nach § 30 Abs. 5 BZRG. Eintragungen wegen Vermögensdelikten, BtM-Delikten, Steuerhinterziehung sind Versagungsgrund.
5. **Wirtschaftliche Leistungsfähigkeit:** Vermögensauskunft, EVZ-Negativauszug, ggf. Bonitätsauskunft. Eidesstattliche Versicherung der letzten drei Jahre ist Ausschlussgrund.
6. **Vier-Apotheken-Grenze prüfen:** § 1 Abs. 2 ApoG erlaubt eine Hauptapotheke plus bis zu drei Filialen — nicht mehr (siehe Skill `fremd-und-mehrbesitzverbot-apothekenrecht`).
7. **Antrag bei zuständiger Behörde:** In den meisten Ländern Regierungspräsidium oder Landesamt für Gesundheit. Anhörung nach § 28 VwVfG.
8. **Bei Versagungstendenz:** Frist für Stellungnahme aushandeln, Belege vorlegen, ggf. Anhörung des Antragstellers verlangen.

## Trade-off-Matrix

| Konstellation | Variante A: Einzelinhaber | Variante B: OHG | Variante C: Erbenfortführung |
|---|---|---|---|
| Erlaubnisträger | natürliche Person | OHG, alle Ges. Apotheker | Erbe (auch Nicht-Apotheker) |
| Persönliche Leitung | zwingend, § 7 ApoG | von einem Gesellschafter | durch angestellten Apotheker |
| Dauer | unbefristet | unbefristet | max. zwölf Monate, § 13 ApoG |
| Übergangsfähig | nein | bei Gesellschafterwechsel ja | nein |
| Steuerlich | EStG natürliche Person | Mitunternehmerschaft | Erbschaft, ggf. EStG |

## Praxistipps

- Führungszeugnis und ärztliches Zeugnis frühzeitig beantragen — die Wartezeiten betragen oft drei bis sechs Wochen.
- Bei laufenden Strafverfahren: keinesfalls verschweigen, sondern aktiv ansprechen und Stand erläutern. Verschweigen ist eigene Unzuverlässigkeitsindikation.
- EU-Anerkennung kann Monate dauern — falls Approbation aus Drittstaat: Anerkennungsverfahren rechtzeitig einleiten.
- Wirtschaftliche Leistungsfähigkeit ist kein "Vermögensnachweis", sondern Negativ-Erklärung: keine eidesstattliche Versicherung, keine Insolvenz, keine offenen Vollstreckungen.
- Bei Insolvenz in der Vergangenheit: Restschuldbefreiung und mindestens drei Jahre seitdem absolvierte Berufsausübung dokumentieren.

## Mustertexte

### Antragsschreiben (Auszug)
"Sehr geehrte Damen und Herren, hiermit beantrage ich, [Name, Anschrift, Geburtsdatum], approbierte:r Apotheker:in (Approbationsurkunde vom [Datum], ausgestellt durch [Behörde]), die Erlaubnis zum Betrieb einer Apotheke nach §§ 1, 2 ApoG am Standort [Anschrift]. Beigefügt sind: 1. Approbationsurkunde (beglaubigte Kopie), 2. Behördliches Führungszeugnis (Antrag vom [Datum]), 3. Ärztliches Zeugnis (Datum), 4. EVZ-Auszug Vermögensverzeichnis, 5. Bescheinigung der Apothekerkammer [Land] über die Mitgliedschaft."

### Stellungnahme zur Anhörung bei Versagungstendenz (Auszug)
"In der Anhörung vom [Datum] führt die Behörde aus, die Zuverlässigkeit sei wegen [Vorhaltung] in Zweifel zu ziehen. Hierzu nehme ich wie folgt Stellung: [Sachverhalt klarstellen, ggf. Einstellung des Strafverfahrens nach § 153a StPO darlegen, Resozialisierung belegen]. Die Behörde wird gebeten, von der Versagung abzusehen, da die persönliche Zuverlässigkeit im Sinne des § 2 Abs. 1 Nr. 4 ApoG vorliegt."

## Typische Fehler

- Antragsteller verschweigt laufendes Strafverfahren — Behörde erfährt ohnehin über Polizeiabfrage; Verschweigen verstärkt Unzuverlässigkeitsverdacht.
- Ärztliches Zeugnis ist abgelaufen (älter als drei Monate) — Behörde verzögert Verfahren.
- Persönliche Leitung wird durch verwaltende Tätigkeit ersetzt; die Behörde verlangt jedoch tatsächliche Anwesenheit und pharmazeutische Letztverantwortung.
- Bei OHG-Gründung wird ein Nicht-Apotheker als Gesellschafter geführt — verstösst gegen § 8 ApoG (Fremdbesitzverbot).
- Vier-Apotheken-Grenze wird übersehen, wenn Mandant bereits drei Filialen führt.

## Querverweise

- `fremd-und-mehrbesitzverbot-apothekenrecht` (Eigentumsstruktur)
- `filialapotheke-hauptapotheke-leitung-vertretung` (mehrere Betriebsstätten)
- `widerruf-ruecknahme-ruhen-apothekenerlaubnis` (Verlust der Erlaubnis)
- `inhaberwechsel-kauf-apothekenbetrieb` (Eigentümerwechsel)
- `apothekenbetriebsordnung-grundpflichten` (sachliche Anforderungen)

## Quellen Stand 06/2026

- ApoG, Stand zur Antragstellung im amtlichen Bundesgesetzblatt prüfen.
- BApO (Bundes-Apothekerordnung) §§ 4, 4a für Approbation.
- BfArM und Landesapothekerkammern — Merkblätter zur Erlaubniserteilung (vom Anwender zu verifizieren).
- BVerfG, staend. Rspr. zur Apothekenfreiheit nach Art. 12 GG.
- Vom Anwender vor Antragstellung: aktuelles Landesrecht (z. B. HeilberufeKG, GAVG) verifizieren.
