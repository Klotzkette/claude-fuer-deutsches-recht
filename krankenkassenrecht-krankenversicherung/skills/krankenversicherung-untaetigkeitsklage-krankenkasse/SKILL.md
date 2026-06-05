---
name: krankenversicherung-untaetigkeitsklage-krankenkasse
description: "Untaetigkeitsklage Krankenkasse: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Untaetigkeitsklage Krankenkasse

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Untaetigkeitsklage Krankenkasse** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-026-untaetigkeitsklage-krankenkasse-und-akteneinsicht` | Rechtsdurchsetzung bei untätiger Krankenkasse: Untätigkeitsklage (§ 88 SGG), Akteneinsichtsrecht (§ 25 SGB X), Fristen und Beschleunigungsstrategien. |
| `kv-027-datenschutz-gesundheitsdaten-krankenkasse-arbeitgeber` | Datenschutz im Krankenversicherungsrecht: DSGVO, § 67 SGB X, Weitergabe an Arbeitgeber, MDK-Datenschutz und Auskunftsrechte. |
| `kv-029-pkv-leistungspflicht-medizinische-notwendigkeit` | Leistungspflicht in der PKV nach § 192 VVG und MB/KK: medizinische Notwendigkeit, Behandlungsmethoden, Kostenbegrenzungsklauseln und Beweislast. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Untaetigkeitsklage Krankenkasse**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-026-untaetigkeitsklage-krankenkasse-und-akteneinsicht`

**Fokus:** Rechtsdurchsetzung bei untätiger Krankenkasse: Untätigkeitsklage (§ 88 SGG), Akteneinsichtsrecht (§ 25 SGB X), Fristen und Beschleunigungsstrategien.

# Untätigkeitsklage, Krankenkasse und Akteneinsicht

## Skill-Zweck

Krankenkassen entscheiden manchmal nicht oder zu spät. Dieser Skill nutzt die **Untätigkeitsklage (§ 88 SGG)** und das **Akteneinsichtsrecht (§ 25 SGB X)** als Druckmittel und Informationsquelle zur Rechtsdurchsetzung.

## Rechtlicher Rahmen

- **§ 88 SGG** – Untätigkeitsklage: 6 Monate nach Antragstellung oder 3 Monate nach Widerspruch
- **§ 13 Abs. 3a SGB V** – Genehmigungsfiktion: 5 Wochen bei Leistungsantrag, 3 Wochen bei Eilbedarf
- **§ 25 SGB X** – Akteneinsicht: Recht auf Einsicht in Verwaltungsvorgänge
- **§ 19 SGB X** – Amtsermittlungspflicht der Kasse
- **§ 84 Abs. 1 SGG** – Widerspruchsfrist (relevant für Ausgangspunkt Untätigkeit)
- **§ 193 Abs. 4 SGG** – Kostenentscheidung bei Untätigkeitsklage
- BSG B 3 KR 9/10 R (Untätigkeitsklage, Fristberechnung)

## Untätigkeitsklage-Fristen

| Fallgruppe | Wartepflicht | Rechtsgrundlage |
|-----------|-------------|-----------------|
| Erstantrag auf Leistung | 6 Monate | § 88 Abs. 1 SGG |
| Widerspruch eingelegt | 3 Monate | § 88 Abs. 2 SGG |
| Ausnahme: besondere Gründe | Kürzere Frist möglich | Gericht entscheidet |
| Genehmigungsfiktion | 5 Wochen (3 Wochen Eilbedarf) | § 13 Abs. 3a SGB V |

## Prüfprogramm

### Schritt 1 – Wartepflicht prüfen
- Antragsdatum feststellen (Eingangsbestätigung der Kasse)
- Ergebnis noch nicht ergangen? 6 Monate ab Antrag abgelaufen?
- Widerspruch eingelegt? 3 Monate ab Widerspruchseingang abgelaufen?
- Ausnahme: besonders wichtige Gründe (z.B. Lebensgefahr) → kürzere Frist

### Schritt 2 – Genehmigungsfiktion (§ 13 Abs. 3a SGB V)
- Leistungsantrag → 5-Wochen-Frist (3 Wochen bei Eilbedarf)
- Keine Entscheidung innerhalb Frist → Genehmigung gilt als erteilt
- Schriftlich auf Fiktion hinweisen, Behandlung beginnen
- Kasse muss Behandlung finanzieren; nachträgliche Ablehnung nur in sehr engen Grenzen

### Schritt 3 – Akteneinsicht (§ 25 SGB X)
- Recht auf Einsicht in alle Verwaltungsvorgänge der eigenen Akte
- Antrag schriftlich an Kasse; Kasse hat keine bestimmte Frist (aber zeitnah)
- Verzögerung oder Verweigerung: Klage auf Akteneinsicht gesondert (Untätigkeitsklage oder Feststellungsklage)
- Kopien anfertigen: Verwaltungsakte, MDK-Gutachten, interne Vermerke

### Schritt 4 – Untätigkeitsklage einreichen
- Klage beim Sozialgericht am Wohnort
- Keine Anwaltspflicht im 1. Instanzgericht
- Klageinhalt: Verpflichtungsantrag (Kasse zu bescheiden), Sachverhalt, Fristen
- Kosten: im Untätigkeitsklage-Urteil trägt Kasse Kosten wenn sie ohne Grund nicht entschieden hat

### Schritt 5 – Druckmittel und Praxis
- Kasse beschleunigt oft wenn Untätigkeitsklage angekündigt wird
- Kassenaufsicht einschalten (Skill kv-072): ergänzend, kein Ersatz für Klage
- Patientenbeauftragte/Ombudsmann: bei Beratungsfragen; keine Rechtsdurchsetzung

## Typische Fallen

- **Frist noch nicht abgelaufen**: Untätigkeitsklage zu früh → unzulässig; Gericht weist ab.
- **Besondere Gründe**: BSG-Rechtsprechung: erhebliche Verzögerung durch Kasse selbst begründet kürzere Frist (z.B. MDK-Auftrag vergessen).
- **Genehmigungsfiktion praktisch**: Kasse macht nichts → nach 5 Wochen Anspruch durchsetzen; aber Kasse kann noch ablehnen wenn Behandlung noch nicht begonnen.
- **Datenschutz in Akteneinsicht**: Akte enthält Daten Dritter (z.B. Arbeitgeber-Auskunft) → diese Teile können geschwärzt werden.

## Output-Formate

- Genehmigungsfiktion-Schreiben (Muster)
- Akteneinsichtsantrag (Muster)
- Untätigkeitsklage (Muster)
- Fristenkalender Untätigkeit
- Kassenaufsichts-Beschwerde (ergänzend)

## Quellen

- [§ 88 SGG – Untätigkeitsklage](https://www.gesetze-im-internet.de/sgg/__88.html)
- [§ 13 Abs. 3a SGB V – Genehmigungsfiktion](https://www.gesetze-im-internet.de/sgb_5/__13.html)
- [§ 25 SGB X – Akteneinsicht](https://www.gesetze-im-internet.de/sgb_10/__25.html)
- [BSG Untätigkeitsklage](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 88 SGG](https://dejure.org/gesetze/SGG/88.html)
- [Sozialgericht Klageanleitung](https://www.sozialgerichtsbarkeit.de)

## 2. `kv-027-datenschutz-gesundheitsdaten-krankenkasse-arbeitgeber`

**Fokus:** Datenschutz im Krankenversicherungsrecht: DSGVO, § 67 SGB X, Weitergabe an Arbeitgeber, MDK-Datenschutz und Auskunftsrechte.

# Datenschutz: Gesundheitsdaten, Krankenkasse und Arbeitgeber

## Skill-Zweck

Gesundheitsdaten genießen besonderen Schutz. Dieser Skill klärt, **welche Daten die Krankenkasse verarbeiten darf**, wann sie Daten weitergeben darf und welche Rechte der Versicherte hat – insbesondere gegenüber dem Arbeitgeber.

## Rechtlicher Rahmen

- **DSGVO Art. 9** – Besondere Kategorien personenbezogener Daten (Gesundheitsdaten)
- **§ 67 SGB X** – Sozialdatenschutz: Grundsätze, Zweckbindung
- **§ 76 SGB X** – Übermittlung von Sozialdaten an Strafverfolgungsbehörden
- **§ 77 SGB X** – Übermittlung für wissenschaftliche Forschung
- **§ 295 SGB V** – Datenübermittlung Arzt → Kasse (Diagnosen, Leistungsdaten)
- **§ 305 SGB V** – Auskunftsanspruch des Versicherten
- **§ 611a BGB** – Datenschutz im Arbeitsverhältnis (kein Recht auf AU-Diagnose durch AG)
- **BDSG** §§ 22, 26 – Beschäftigtendatenschutz
- BSG B 1 KR 25/17 R (Sozialdatenschutz und Weitergabe)

## Schutzbereich und Weitergabe-Verbote

| Datenkategorie | Weitergabe an Arbeitgeber | Rechtsgrundlage |
|---------------|--------------------------|-----------------|
| AU-Diagnose | VERBOTEN | § 294 SGB V; kein Anspruch AG |
| AU-Fakt (ja/nein) | Nur durch Arbeitnehmer selbst | § 5 EFZG |
| Behandlungsart | VERBOTEN ohne Einwilligung | DSGVO Art. 9 |
| MDK-Gutachteninhalt | VERBOTEN gegenüber AG | § 67 SGB X |
| Beitragsschulden | Beitreibungsmaßnahmen nicht an AG | § 76 SGB X |

## Prüfprogramm

### Schritt 1 – Datenverarbeitung durch Kasse
- Welche Daten verarbeitet die Kasse? (§ 284 SGB V: abschließende Aufzählung)
- Zweckbindung: Kasse darf Daten nur für den gesetzlichen Aufgabenbereich nutzen
- Datenminimierung: nur erforderliche Daten erheben (DSGVO Art. 5 Abs. 1 lit. c)

### Schritt 2 – Weitergabe an Arbeitgeber
- Arbeitgeber hat keinen Anspruch auf Diagnosen; Auskunftspflicht des AN: nur „krank ja/nein"
- Kasse darf keine Gesundheitsdaten an Arbeitgeber übermitteln
- Ausnahme: Arbeitgeber zahlt Entgeltfortzahlung → hat Anspruch auf Bestätigung AU, aber nicht Diagnose
- Betriebsarzt: separates System; Betriebsarzt darf keine Diagnosen an Arbeitgeber weitergeben (§ 8 ASiG)

### Schritt 3 – MDK und Datenschutz
- MDK-Gutachten enthält sensible Gesundheitsdaten; verbleibt beim MD
- Arbeitgeber hat kein Recht auf MDK-Gutachten
- Sozialgerichte: können Gutachten beiziehen; Akteneinsicht nur Partei (Versicherter, Kasse)

### Schritt 4 – Auskunftsrechte des Versicherten
- § 305 SGB V: Kasse muss Versicherten über gespeicherte Daten informieren
- DSGVO Art. 15: Auskunftsrecht über alle personenbezogenen Daten
- Löschung: nicht möglich wenn gesetzliche Aufbewahrungspflicht (§ 110 SGB IV: 10 Jahre)

### Schritt 5 – Elektronische Patientenakte (ePA) und Datenschutz
- ePA: Daten freiwillig eingestellt; Versicherter entscheidet über Zugriffsrechte
- Arbeitgeber hat kein Zugriffsrecht auf ePA
- Opt-out-Regelung (ab 2025): ePA standardmäßig angelegt; Widerspruch möglich

## Typische Fallen

- **Krankenkassen-App-Daten**: Gesundheitsdaten in Apps der Kasse fallen unter DSGVO; Einwilligung prüfen.
- **Entgeltfortzahlungs-Erstattung**: Wenn AG von Kasse EFZG-Erstattung erhält, fließen keine Diagnosen → nur Betrag.
- **Bonusprogramme und Datenkrake**: Fitnessdaten, Vorsorge-Nachweise → DSGVO-Einwilligung prüfen; Widerruf möglich.
- **Auskunftsersuchen Strafverfolgung**: Enge Voraussetzungen (§ 76 SGB X); Kasse muss kein Selbstauskunftsrecht sabotieren.

## Output-Formate

- Datenschutz-Auskunftsantrag (DSGVO Art. 15)
- Beschwerde bei Datenschutzbeauftragten (Aufsichtsbehörde)
- Widerspruch gegen Datenweitergabe
- ePA-Widerspruchsschreiben
- Informationsblatt für Arbeitnehmer

## Quellen

- [DSGVO Art. 9 – Gesundheitsdaten](https://dsgvo-gesetz.de/art-9-dsgvo/)
- [§ 67 SGB X – Sozialdatenschutz](https://www.gesetze-im-internet.de/sgb_10/__67.html)
- [§ 284 SGB V – Datenverarbeitung Kassen](https://www.gesetze-im-internet.de/sgb_5/__284.html)
- [§ 305 SGB V – Auskunftsanspruch](https://www.gesetze-im-internet.de/sgb_5/__305.html)
- [Bundesdatenschutzgesetz BDSG](https://www.gesetze-im-internet.de/bdsg_2018/)
- [dejure.org § 67 SGB X](https://dejure.org/gesetze/SGB_X/67.html)
- [BfDI – Bundesbeauftragter Datenschutz](https://www.bfdi.bund.de)

## 3. `kv-029-pkv-leistungspflicht-medizinische-notwendigkeit`

**Fokus:** Leistungspflicht in der PKV nach § 192 VVG und MB/KK: medizinische Notwendigkeit, Behandlungsmethoden, Kostenbegrenzungsklauseln und Beweislast.

# PKV-Leistungspflicht: Medizinische Notwendigkeit

## Skill-Zweck

In der PKV schuldet der Versicherer Leistungen für **medizinisch notwendige Heilbehandlungen**. Dieser Skill analysiert den Leistungsanspruch, die Prüfung der medizinischen Notwendigkeit und typische Streitfälle.

## Rechtlicher Rahmen

- **§ 192 VVG** – Leistungspflicht des Versicherers: Erstattung ärztlicher Kosten
- **§ 193 VVG** – Versicherungspflicht in der PKV (Basistarif)
- **MB/KK 2009 § 1** – Gegenstand der Versicherung: medizinisch notwendige Heilbehandlungen
- **MB/KK 2009 § 4** – Umfang der Leistungspflicht; Ausschlüsse
- **GOÄ, GOZ** – Ärztliche und zahnärztliche Honorarordnungen
- BGH IV ZR 194/07 (medizinische Notwendigkeit), BGH IV ZR 231/15 (Kostenbegrenzung)
- BVerfG 1 BvR 2019/17 (Basistarif-Leistungsumfang)

## Begriff der medizinischen Notwendigkeit

| Dimension | Inhalt |
|-----------|--------|
| Diagnose | Muss gesichert oder hinreichend wahrscheinlich sein |
| Behandlungserforderlichkeit | Behandlung muss zur Bekämpfung der Krankheit oder Minderung von Beschwerden geeignet und erforderlich sein |
| Wissenschaftlicher Standard | Schulmedizin grundsätzlich maßgeblich; Außenseitermethoden → Evidenzprüfung |
| Prognose | Exante-Beurteilung: was war zum Behandlungszeitpunkt vertretbar? |

## Prüfprogramm

### Schritt 1 – Leistungsanspruch bestimmen
- Liegt eine Krankheit vor? (Krankenbehandlungs-Begriff: Abweichung vom normalen Körper- oder Geisteszustand)
- Welche Behandlung ist ärztlich verordnet und warum?
- Welcher Tarif gilt? (Tarif, Zusatztarif, Basistarif) – Tarif­bedingungen lesen

### Schritt 2 – Medizinische Notwendigkeit prüfen
- PKV-Gutachter: überprüft ex ante, ob Behandlung zum Zeitpunkt der Durchführung notwendig war
- BGH-Maßstab: „ex ante Betrachtung eines verständigen, informierten Arztes"
- Nachträgliche Erfolglosigkeit der Behandlung schließt Notwendigkeit nicht aus

### Schritt 3 – Außenseitermethoden
- Methode nicht in schulmedizinischen Leitlinien: PKV darf ablehnen wenn wissenschaftliche Wirksamkeit fehlt
- Ausnahme: PKV-Tarif deckt explizit alternative Methoden ab
- BGH IV ZR 194/07: Alternativmethode erstattungsfähig wenn ernsthaft auf Heilung gerichtet und keine schulmedizinische Alternative

### Schritt 4 – Stationäre Notwendigkeit
- PKV prüft: War stationäre Behandlung notwendig oder ambulant ausreichend?
- Kriterien: Überwachungsbedarf, Infusionen, Bettruhe, fehlende ambulante Kapazität
- Gutachten der PKV: Gegengutachten des Krankenhauses organisieren

### Schritt 5 – Kostenbegrenzungsklauseln
- Tarif enthält Kostenbegrenzung (z.B. max. Tagessatz, Modultarif): Klausel prüfen auf AGB-Kontrolle (§§ 307–309 BGB)
- BGH: überraschende und unangemessene Klauseln unwirksam
- Transparenzgebot: Klausel muss klar und verständlich sein

## Typische Fallen

- **Schönheitsoperation**: Grundsätzlich keine medizinische Notwendigkeit; außer krankhafte Entstellung, psychische Erkrankungsfolge.
- **Wahlleistungen Krankenhaus**: Einzelzimmer, Chefarzt: Wahlleistung = PKV-Leistung nach Tarif; immer im Tarif nachsehen.
- **Präventionsleistungen**: PKV schuldet keine vorsorgebezogenen Leistungen; aber Tarif kann Prävention einschließen.
- **GOÄ-Abrechnung**: Arzt rechnet nach GOÄ ab; Steigerungsfaktoren können PKV-interne Beschränkungen unterliegen.

## Output-Formate

- PKV-Leistungsbrief (Anspruchsbegründung)
- Widerspruch gegen PKV-Ablehnung
- Gutachten-Briefing (medizinische Notwendigkeit)
- GOÄ-Prüfungsprotokoll
- Klageschrift gegen PKV (Amtsgericht, wenn < 5.000 €)

## Quellen

- [§ 192 VVG – PKV-Leistungspflicht](https://www.gesetze-im-internet.de/vvg_2008/__192.html)
- [MB/KK 2009](https://www.pkv.de/service/broschueren/mustervertragsbedingungen/)
- [BGH IV ZR 194/07](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [GOÄ – Ärztliche Gebührenordnung](https://www.bundesaerztekammer.de/fileadmin/user_upload/downloads/GOAe_20130901.pdf)
- [dejure.org § 192 VVG](https://dejure.org/gesetze/VVG/192.html)
- [PKV-Verband Leistungspflicht](https://www.pkv.de)
