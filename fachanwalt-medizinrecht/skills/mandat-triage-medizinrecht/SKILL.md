---
name: mandat-triage-medizinrecht
description: "Strukturierte Eingangs-Abfrage fuer medizinrechtliche Mandate. Klaert Mandantenrolle (Patient Arzt Krankenhaus Heilberufler Pharma Krankenkasse) Sachgebiet (Behandlungsfehler Aufklaerungspflicht-Verletzung Honorarstreit GOAe EBM Approbationsrecht Krankenhausrecht Heilmittelwerberecht Vertragsarztrecht KV-Recht Apotheken- und Arzneimittelrecht Pharmastrafrecht) Sofort-Fristen-Check Verjaehrung drei Jahre § 195 BGB ab Kenntnis Hoechstfrist dreissig Jahre Personenschaden § 199 Abs. 2 BGB Approbations-Widerruf-Verfahren Vorlaeufige Ruhensanordnung. Eskalation Telefon-Sofort bei Approbations-Verlust drohend. Routing zu behandlungsfehler-anspruch-pruefen."
---

# Mandat-Triage Medizinrecht

## Zweck

Medizinrecht ist breit — vom Behandlungsfehler bis zur Pharmavermarktung. Triage stellt die richtige Rechtsmaterie und die richtige Eskalation sicher.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Patient (Anspruch auf Schadensersatz)
- Niedergelassener Arzt (Verteidigung Honorar Approbation)
- Krankenhaus / Klinik (Haftpflicht Vertragsklinik)
- Hebamme / Pflegefachkraft
- Heilberufler (Heilpraktiker)
- Pharma- Medizinprodukte-Unternehmen
- Krankenkasse (Regress)
- Apotheker

### Frage 2 — Sachgebiet?

- Behandlungsfehler / Aufklärungsfehler / Dokumentation
- Wirtschaftliche Aufklärung § 630c Abs. 3 BGB
- Honorar GOÄ EBM
- Approbation Widerruf Ruhen Versagung
- Berufsrechtliches Verfahren Berufsgericht
- Vertragsarztrecht (Zulassung KV-Recht Plausibilitätsprüfung)
- Krankenhausrecht (Krankenhausplanung Vergütung Wahlleistung)
- Heilmittelwerberecht (HWG)
- Apotheken- Arzneimittelrecht
- Medizinprodukterecht MDR
- Pharmastrafrecht (Korruption im Gesundheitswesen § 299a § 299b StGB)
- Datenschutz im Gesundheitswesen

### Frage 3 — Akute Eilbedürftigkeit?

- Approbations-Widerruf / Ruhensanordnung sofort vollziehbar
- Strafverfahren Pharma-Korruption
- Existenzbedrohung Praxis
- Personenschaden akut vor Verjährung
- Krankenkassen-Regress drohend mit Verjährung
- Patientenverfügung lebensbedrohlich

### Frage 4 — Verfahrensstand?

- Beratungsbedarf (vor Klage Anzeige)
- Schlichtungsstelle Ärztekammer läuft
- Klage erhoben (LG bei Behandlungsfehler typisch Streitwert über EUR 10000 jetzt LG)
- Strafverfahren Ermittlungs- Anklage Hauptverhandlung
- Approbationsverfahren Widerspruch Klage Verwaltungsgericht
- Berufsgerichtliches Verfahren

### Frage 5 — Beteiligte?

- Behandler einzeln (Hauptverantwortlich)
- Behandler-Team Krankenhaus
- Haftpflichtversicherer
- Krankenkasse
- Krankenkassenverband KV
- Patientenanwalt Gegnerseite
- Sachverständigen-Gutachter

### Frage 6 — Dokumente?

- Patientenakte vollständig (Recht § 630g BGB)
- Aufklärungsbögen
- Gutachten Schlichtungsstelle MDK
- Strafanzeige Akten StA
- Approbationsakte Behörde

### Frage 7 — Frist?

- **Behandlungsfehler-Verjährung** drei Jahre / dreißig Jahre § 195 199 BGB
- **Strafverfahren** Verjährung je nach Tat
- **Approbationsanfechtung** ein Monat § 70 VwGO Widerspruch / ein Monat Klage
- **Schlichtungsstelle** keine Frist aber Hemmung Verjährung
- **Krankenkassen-Regress** vier Jahre § 199 SGB X

### Frage 8 — Versicherungs- und Vertragslage?

- Berufshaftpflicht Arzt / Klinik
- Rechtsschutz Patient
- Vertragsklinik-Vereinbarung
- Privat-/Kassenpatient

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Behandlungsfehler-Patient | `behandlungsfehler-anspruch-pruefen` |
| Behandlungsfehler-Arzt-Verteidigung | `behandlungsfehler-anspruch-pruefen` (Beweislast-Sicht) |
| Honorarstreit GOÄ EBM | (Skill arzt-honorar — perspektivisch) |
| Approbation-Widerruf | weiter an `mandat-triage-verwaltungsrecht` plus Spezial |
| KV-Plausibilitätsprüfung Regress | (Skill kv-regress — perspektivisch) |
| Pharma-Korruption § 299a StGB | weiter an `mandat-triage-strafrecht` plus Spezial |
| Heilmittelwerberecht | (Skill hwg-werberecht — perspektivisch) |
| Datenschutz Gesundheitswesen | weiter an `datenschutzrecht`-Plugin |

## Mandatsannahme

- **Konflikt-Check** — Patient/Arzt/Klinik/KK selbe Sache strikte Trennung
- **Streitwert** Schaden Schmerzensgeld
- **Sachverständigen-Bedarf** Patientenakten-Auswertung medizinisch
- **Versicherungsdeckung** Berufshaftpflicht Arzt prüfen
- **Schweigepflicht** § 203 StGB — Aufhebung durch Patient erforderlich

## Eskalation

- **Telefon-Sofort** Approbations-Ruhensanordnung sofort vollziehbar
- **Binnen einer Stunde** Polizei-Vernehmung Arzt Strafverfahren
- **Heute** Patientenakte anfordern § 630g BGB Schlichtungsantrag
- **Diese Woche** Klage-Erstentwurf Sachverständigenauftrag

## Ausgabe

- `triage-protokoll-medizinrecht.md`
- Aktenanlage
- Frist im Fristenbuch
- Schweigepflichtsentbindung als Entwurf
- Patientenakten-Anforderung § 630g BGB Entwurf
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Quellen

- BGB §§ 195 199 253 630a–630h 823
- StGB §§ 203 222 229 299a 299b
- SGB V § 66 SGB X §§ 116 199
- BGH VI. Zivilsenat 5. Strafsenat
- Spickhoff Medizinrecht-Kommentar

## Vertiefung — Rechtsprechung und Normenkette

### Leitsatz-Zitate

BGH, Urt. v. 07.11.2023 — **VI ZR 79/22**, NJW 2024, 392 Rn. 18: Die Verjährung von Schadensersatzansprüchen wegen Behandlungsfehlern beginnt gemäß § 199 Abs. 1 BGB, wenn der Patient sowohl Kenntnis vom Schaden als auch von der Person des Schädigers hat; Unkenntnis über den genauen Kausalverlauf hemmt den Beginn der Verjährungsfrist nicht, solange die Tatsachen für eine Klageerhebung ausreichen.

BGH, Urt. v. 27.03.2007 — **VI ZR 55/05**, NJW 2007, 2771 Rn. 14: Der Behandler ist nach § 630f BGB (früher gewohnheitsrechtlich anerkannt) zur vollständigen und zeitnahen Dokumentation verpflichtet; lückenhafte Dokumentation begründet zugunsten des Patienten die Vermutung, dass die nicht dokumentierte Maßnahme unterblieben ist.

BSG, Urt. v. 18.11.2014 — **B 1 KR 8/13 R**, BSGE 117, 212 Rn. 30: Krankenkassen-Regress nach § 116 SGB X setzt voraus, dass der Dritte (Schädiger/Behandler) gegenüber dem Geschädigten (Versicherten) schadensersatzpflichtig ist; der Anspruch geht im Zeitpunkt des Schadenseintritts auf die Krankenkasse über, soweit diese Leistungen erbringt.

### Ergänzung — Wichtige Normen Triage-Routing

- § 195 BGB (regelmäßige Verjährung 3 Jahre) i.V.m. § 199 Abs. 1 BGB (Kenntnis-Beginn) und § 204 BGB (Hemmung durch Klage, Schlichtungsantrag, Mahnbescheid)
- § 630g BGB (Einsichtsrecht Patientenakte — unverzüglich zu gewähren, Kopien auf Kosten des Patienten)
- § 116 SGB X (Übergang Schadensersatzanspruch auf Sozialversicherungsträger)
- § 299a StGB (Bestechlichkeit im Gesundheitswesen), § 299b StGB (Bestechung im Gesundheitswesen)
- §§ 203, 204 StGB (Schweigepflicht, Schweigepflichtentbindung obligatorisch vor Aktenweitergabe)

### Kommentarliteratur

- Spickhoff, Medizinrecht, 4. Aufl. 2022: Mandantsrollen und Sachgebietssystematik; Querverweis auf Einzelkommentierungen §§ 630a–h BGB und SGB V.
- Laufs/Kern/Rehborn, Handbuch des Arztrechts, 5. Aufl. 2019, § 13 (Mandatsaufnahme Behandlungsfehler) und § 52 (Vertragsarztrecht): Triage-Systematik und Fallkonstellationen.
