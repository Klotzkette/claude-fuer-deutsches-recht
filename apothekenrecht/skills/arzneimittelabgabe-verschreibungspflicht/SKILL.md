---
name: arzneimittelabgabe-verschreibungspflicht
description: "Arzneimittelabgabe Verschreibungspflicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arzneimittelabgabe Verschreibungspflicht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Arzneimittelabgabe Verschreibungspflicht** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arzneimittelabgabe-verschreibungspflicht` | Arzneimittelabgabe Verschreibungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `cannabis-medizinalcannabis-abgabe-dokumentation` | Cannabis Medizinalcannabis Abgabe Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `tierarzneimittel-apothekenabgabe-versand-ab-2026` | Tierarzneimittel Apothekenabgabe Versand ab 2026: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Arzneimittelabgabe Verschreibungspflicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `arzneimittelabgabe-verschreibungspflicht`

**Fokus:** Arzneimittelabgabe Verschreibungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Arzneimittelabgabe Verschreibungspflicht

## Fachkern: Arzneimittelabgabe Verschreibungspflicht
- **Spezialgegenstand:** Arzneimittelabgabe Verschreibungspflicht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Abgabe verschreibungspflichtiger Arzneimittel (Rx) durch öffentliche Apotheken. Geregelt sind: Verschreibungspflicht, formale Anforderungen an die ärztliche Verordnung (Papierrezept, Muster-16, E-Rezept), Identitätsprüfung, Plausibilitätsprüfung, Aushändigung, Beratung, Dokumentation. Abgrenzung zur OTC-Abgabe (apothekenpflichtig, nicht verschreibungspflichtig) und zur BtM-Abgabe (gesondertes Regime).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Konflikt um eine zu Unrecht oder zu Recht durchgeführte Abgabe.
- Retax wegen Formalfehler auf dem Rezept.
- Strafrechtlicher Vorwurf: Abgabe ohne gültige Verschreibung (§ 96 Nr. 4, 13 AMG).
- Beanstandung durch Krankenkasse oder Aufsicht.

Eingaben:
- Rezept (Original oder E-Rezept-Token / Beleg).
- Abgabedokumentation (Zeit, abgebende Person, Charge).
- ggf. Vorgespräch, falls Patient nicht der Adressat war.
- Korrespondenz mit Arzt, Krankenkasse oder Behörde.

## Rechtlicher Rahmen

- **§ 48 AMG:** Verschreibungspflicht — definiert, wann ein Arzneimittel nur auf ärztliche Verordnung abgegeben werden darf.
- **AMVV (Arzneimittelverschreibungsverordnung):** Formerfordernisse, Geltungsdauer (drei Monate, BtM sieben Tage), Pflichtangaben.
- **§ 17 ApBetrO:** Abgabevorgang — Identitätskontrolle, Plausibilitätsprüfung, Beratung, Dokumentation.
- **§§ 12, 12a ApBetrO:** Beratungspflicht.
- **§ 21 AMG:** Zulassungspflicht.
- **§ 73 AMG:** Verbringungsverbot, Ausnahmen Einzelimport.
- **§ 96 AMG:** Strafvorschrift — Abgabe ohne ärztliche Verordnung.
- **§ 97 AMG:** Ordnungswidrigkeit.
- **SGB V § 360:** E-Rezept-Pflicht seit 01.01.2024.
- BGH/OLG, staend. Rspr. zu Heilmittelwerbung und Apothekenabgabe.

## / Schritt für Schritt

1. **Identität prüfen:** Bei E-Rezept Token/Code; bei Papierrezept Plausibilität der Verordnerangaben (Arzt, Praxis, BSNR/LANR).
2. **Formelle Prüfung:** Datum, Name Patient, Name Arzneimittel, Stärke, Menge, Dosierung, Unterschrift Arzt (bei Papier) / qualifizierte elektronische Signatur (E-Rezept).
3. **Geltungsdauer:** Drei Monate ab Ausstellung (§ 2 AMVV); GKV vier Wochen für Versorgung; BtM sieben Tage.
4. **Plausibilität:** Indikation, Dosierung, Interaktion, Kontraindikation. Bei Unklarheit Rücksprache Arzt.
5. **Substitutionsprüfung:** Aut-idem-Status, Rabattvertrag (siehe Skill `substitution-rabattvertrag-aut-idem`).
6. **Aushändigung mit Beratung:** Informationen zur Anwendung, Nebenwirkungen, Aufbewahrung.
7. **Dokumentation:** Im Apothekenwarenwirtschaftssystem; Rezept aufbewahren (drei Jahre, bei BtM zehn Jahre).
8. **Sonderfälle:** Notfallabgabe ohne Rezept (§ 4 AMVV) bei akutem Bedarf, max. kleinste Packung; Heimversorgung, Patientenstellvertretung.

## Trade-off-Matrix

| Situation | Sofortabgabe möglich? | Beleg | Risiko |
|---|---|---|---|
| Vollständiges E-Rezept | ja | Token + Quittung | gering |
| Papierrezept Muster-16 vollständig | ja | Original + Quittung | gering |
| Rezept ohne Unterschrift | nein | Rücksprache Arzt | hoch (Strafbarkeit) |
| Notfall ohne Rezept § 4 AMVV | ja, kleinste Packung | Notfallprotokoll | mittel, Dokumentation zwingend |
| Telefonische Verordnung | nein, aber Notfall-Regelung | schriftliche Bestätigung Arzt binnen einer Woche | mittel |
| Rezept abgelaufen | nein | Hinweis an Patient | gering |
| Faxrezept (BtM) | nein (Original zwingend) | — | hoch |

## Praxistipps

- Bei Plausibilitätszweifeln: nicht aus Eile abgeben, sondern Arzt anrufen — fehlerhafte Abgaben sind sowohl OWi/Strafbarkeitsrisiko als auch Patientenrisiko.
- Notfallabgabe immer mit schriftlicher Notiz: "Notfallabgabe nach § 4 AMVV, Indikation, Versorgungslücke, Folgerezept binnen [Frist] verlangt."
- E-Rezept: bei technischer Störung muss "Ersatzverfahren" (Papier oder Token-Print) genutzt werden — siehe Gematik-Vorgaben.
- Bei Substitution Aut-idem-Liste (§ 129 SGB V, Anlage) prüfen und Pharmazeutische Bedenken dokumentieren, falls trotz Rabattvertrag abgewichen wird.

## Mustertexte

### Dokumentation Notfallabgabe (Auszug)
"Notfallabgabe am [Datum, Uhrzeit] nach § 4 AMVV. Patient: [Name, Geb.-Datum]. Arzneimittel: [Name, Stärke, kleinste verfügbare Packung]. Indikation: [akut, z. B. Asthma-Anfall, Insulin]. Patient erklärt: [Rezept verloren / Arzt nicht erreichbar / Wochenende]. Folgerezept ist binnen sieben Tagen vorzulegen; entsprechende Aufforderung wurde übergeben (Anlage). Abgebender Apotheker: [Name]. Beratung: erfolgt."

### Hinweis an Patient bei abgelaufenem Rezept (Auszug)
"Sehr geehrte:r [Patient:in], das vorgelegte Rezept vom [Datum] ist nach § 2 AMVV abgelaufen (Geltungsdauer drei Monate). Wir können das Arzneimittel daher nicht zu Lasten der Krankenkasse oder als verschreibungspflichtige Abgabe abgeben. Bitte wenden Sie sich an die ausstellende Praxis für ein neues Rezept. Bei akutem Bedarf prüfen wir eine Notfallabgabe nach § 4 AMVV."

## Typische Fehler

- Abgabe trotz fehlender Unterschrift; eigene Anbringung der Unterschrift wäre Urkundenfälschung (§ 267 StGB).
- Notfallabgabe ohne Dokumentation des Notfallbezugs.
- Substitution gegen Patientenwunsch ohne Plausibilitätsdokumentation; Patient verklagt wegen Pharmazeutische Bedenken.
- E-Rezept-Token mehrfach eingelöst; Doppelabgabe wegen mangelhaftem Workflow.
- Faxrezept BtM angenommen — Original ist zwingend.

## Querverweise

- `btm-rezept-betaeubungsmittel-dokumentation` (BtM-Sonderrecht)
- `e-rezept-ti-gematik-apothekenprozess` (E-Rezept-Workflow)
- `substitution-rabattvertrag-aut-idem` (Austausch)
- `retaxationsabwehr-nullretax-risiko` (Formfehler-Folgen)
- `lieferengpaesse-austausch-dokumentation` (Austausch bei Nichtverfügbarkeit)
- `notfallkontrazeption-beratung` (Sonderfall OTC mit Beratungspflicht)

## Quellen Stand 06/2026

- AMG, AMVV — aktueller Stand zur Anwendung im Bundesgesetzblatt prüfen.
- ApBetrO §§ 17, 20.
- SGB V § 360 zur E-Rezept-Pflicht.
- BGH, staend. Rspr. zur Apothekenabgabe.
- Gematik-Vorgaben zum E-Rezept (vom Anwender zu verifizieren — Versionsstand).

## 2. `cannabis-medizinalcannabis-abgabe-dokumentation`

**Fokus:** Cannabis Medizinalcannabis Abgabe Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Cannabis Medizinalcannabis Abgabe Dokumentation

## Fachkern: Cannabis Medizinalcannabis Abgabe Dokumentation
- **Spezialgegenstand:** Cannabis Medizinalcannabis Abgabe Dokumentation. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Medizinalcannabis (Cannabis-Blüten, Cannabis-Extrakte) ist seit dem Cannabisgesetz 2024 nicht mehr Betäubungsmittel im engeren Sinne, fällt aber unter besondere Verkehrs- und Verschreibungsregeln des Konsumcannabisgesetzes (KCanG) / Medizinal-Cannabisgesetz (MedCanG). Apotheken müssen verschreibungsrechtliche, lager- und dokumentationsrechtliche Pflichten beachten. Cannabis-Importe sind über die Cannabisagentur des BfArM (vormals) geregelt; aktueller Stand vom Anwender zu verifizieren.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Patient bringt erstmals Cannabis-Rezept (BtM- oder normales Rx-Formular je nach Rechtsstand 2024+).
- Apotheke baut neuen Cannabis-Bezugsweg auf.
- Lagerbestand soll erweitert werden — Sicherheits-/Lageranforderungen.
- Krankenkasse fordert Therapienachweise vor Erstattung.
- Verkehrsrechtsfragen (Patient fragt nach Auto fahren).

Eingaben:
- Rezept Medizinalcannabis (Form je nach aktuellem Rechtsstand: BtM-Rezept oder gesondertes Cannabis-Rezept).
- Bezugsdokumentation (Importeur, Charge).
- Patientendaten (Indikation, vorherige Therapieversuche, Kostenzusage GKV).
- Lagerprotokolle.

## Rechtlicher Rahmen

- **Cannabisgesetz (CanG) 2024 / KCanG / MedCanG** (vom Anwender Aktualität zu verifizieren — laufende Anpassungen).
- **BtMG / BtMVV** Übergangsregelungen je nach Wirkstoff.
- **AMG** §§ 21, 43, 73 zur Apotheken-Abgabe und Import.
- **SGB V § 31 Abs. 6:** Erstattungsregelung Medizinalcannabis durch GKV (Genehmigungspflicht).
- **AMVV** für Rezeptformerfordernisse.
- **ApBetrO** für Lagerung und QM.
- Bundesinstitut für Arzneimittel und Medizinprodukte (BfArM) — Bezugsweg, Cannabisagentur-Erbe.
- BSG, staend. Rspr. zur Erstattung Cannabinoid-Therapie.

## / Schritt für Schritt

1. **Rezeptform prüfen:** Aktueller Stand — Cannabis-Rezept (mit besonderem Formular) oder weiterhin BtM-Rezept je nach Wirkstoff/Form (Blüte, Extrakt, Fertigarzneimittel wie Sativex, Epidyolex). Vom Anwender Stand 2026 zu verifizieren.
2. **Verschreibungsangaben:** Wirkstoff (THC- und CBD-Gehalt bei Blüten zwingend), Sorte (genaue Bezeichnung), Menge, Dosierung, Anwendungsform.
3. **Erstattung GKV:** Genehmigungspflicht nach § 31 Abs. 6 SGB V; ohne Kassengenehmigung kein Erstattungsanspruch.
4. **Bezug:** Über zugelassene Importeure / Vertriebspartner; Securpharm bei Fertigarzneimitteln.
5. **Lagerung:** Falls weiterhin BtM-Schrank-pflichtig — abschliessbar; ansonsten verschlossener Apothekenschrank.
6. **Abgabe:** Identitätsprüfung Patient, Beratung zu Anwendung, Verkehrstauglichkeit, Nebenwirkungen.
7. **Dokumentation:** Eintrag im BtM-Buch (sofern noch erforderlich) oder gesondertem Cannabis-Buch; Verlauf Patientenversorgung.
8. **Verkehrsrechtshinweis:** Patient ist auf § 24a StVG hinzuweisen; Berufskraftfahrer besonders aufklären.

## Trade-off-Matrix

| Cannabis-Produkt | Verschreibung | Lagerung | Erstattung GKV | Hinweis |
|---|---|---|---|---|
| Cannabis-Blüte (lose) | Cannabis-Rezept (Form vom Anwender zu prüfen) | gesondert | Genehmigung § 31 VI SGB V | Sortenangabe Pflicht |
| Cannabis-Extrakt (öl-/dronabinolhaltig) | Cannabis-Rezept / BtM-Rezept je Wirkstoff | gesondert | Genehmigung | Wirkstoff-Konzentration angeben |
| Fertigarzneimittel Sativex | Rx-Rezept | Standard | wie Rx | Indikation MS-Spastik |
| Fertigarzneimittel Epidyolex | Rx-Rezept | Standard | wie Rx | seltene Epilepsie-Formen |

## Praxistipps

- Sortenidentität der Cannabis-Blüte tagesgenau prüfen (Bezeichnung Hersteller); Substitution selten zulässig (besondere Stabilität, THC-Gehalt-Variabilität).
- Lagerung: trockenenergiefester abschliessbarer Schrank; Temperaturkontrolle empfohlen.
- Beratungspflicht intensiv: Dosis-Titration, Verkehrstauglichkeit, Beruf, Schwangerschaft.
- Erstattungs-Probleme: Krankenkassen prüfen Therapieerfolg streng; Apotheke unterstützt Antrag mit Informationsmaterial.
- Sicherheit: Tresor, Alarmsysteme, dokumentierte Schlüsselverwahrung.

## Mustertexte

### Beratungsprotokoll Cannabis-Erstabgabe (Auszug)
"Datum / Patient: [Initialen] / Verordnung: [Sorte / Wirkstoff, THC- und CBD-Gehalt, Menge, Anwendungsform] / Indikation: [...] / GKV-Genehmigung: [vorliegend / Datum / Az] / Beratung erfolgt zu: 1. Dosis-Titration, langsam einschleichen; 2. Verkehrstauglichkeit (§ 24a StVG, Patient ist Berufskraftfahrer? ja/nein); 3. Wechselwirkungen mit anderen Arzneimitteln; 4. Lagerung (kühl, dunkel, kindersicher); 5. Auswirkung bei Schwangerschaft / Stillzeit; 6. Geräteempfehlung (Verdampfer/Vaporizer). Patient bestätigt Verständnis. Apotheker:in: [Name]."

### Information zur Verkehrstauglichkeit (Auszug)
"Sehr geehrte:r [Patient:in], die Einnahme von Medizinalcannabis kann die Fahrtüchtigkeit beeinträchtigen. Bei bestimmungsgemässer Einnahme nach ärztlicher Verordnung gilt § 24a Abs. 2 StVG nicht uneingeschränkt — gleichwohl müssen Sie sicherstellen, dass Sie zum Zeitpunkt des Führens eines Kraftfahrzeugs nicht eingeschränkt sind. Bei Beginn der Therapie sollten Sie zunächst nicht fahren. Bewahren Sie die ärztliche Verordnung im Fahrzeug auf, falls eine Kontrolle erfolgt."

## Typische Fehler

- Substitution einer Sorte ohne Plausibilitätsprüfung — Patient verträgt anders, klagt.
- Erstattung GKV nicht vorab geklärt — Apotheke trägt Kosten oder Patient ist verärgert.
- Sortenangabe auf Rezept fehlt — formaler Mangel, Patient muss erneut zum Arzt.
- Lagerung in unzureichend gesichertem Schrank — Diebstahlrisiko.
- Patient nicht zur Verkehrstauglichkeit aufgeklärt — Haftungsrisiko bei Unfall.

## Querverweise

- `btm-rezept-betaeubungsmittel-dokumentation` (verwandte Regelungen)
- `arzneimittelabgabe-verschreibungspflicht` (allgemein)
- `import-einzelimport-73-amg` (Cannabis-Import)
- `beanstandung-durch-aufsichtsbehoerde-anhoerung` (Aufsichtskontakt)
- `securpharm-faelschungsschutz` (Verifikation Fertigarzneimittel)
- `apothekenbetriebsordnung-grundpflichten` (Lagerung)

## Quellen Stand 06/2026

- Cannabisgesetz (CanG) / KCanG / MedCanG — Stand vom Anwender zu verifizieren (laufende Anpassungen 2024–2026).
- BtMG, BtMVV (Übergangsregelungen).
- AMG §§ 21, 43, 73; SGB V § 31 Abs. 6.
- BfArM-Bekanntmachungen zur Cannabisversorgung.
- BSG, staend. Rspr. zur Cannabis-Erstattung.
- DAV-Handlungsempfehlungen zur Cannabis-Abgabe (vom Anwender zu verifizieren).

## 3. `tierarzneimittel-apothekenabgabe-versand-ab-2026`

**Fokus:** Tierarzneimittel Apothekenabgabe Versand ab 2026: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Tierarzneimittel Apothekenabgabe Versand ab 2026

## Fachkern: Tierarzneimittel Apothekenabgabe Versand ab 2026
- **Spezialgegenstand:** Tierarzneimittel Apothekenabgabe Versand ab 2026. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Tierarzneimittel Apothekenabgabe Versand ab 2026** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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
