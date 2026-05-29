---
name: mandat-triage-medizinrecht
description: "Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate. Klaert Mandantenrolle (Patient Arzt Krankenhaus Heilberufler Pharma Krankenkasse) Sachgebiet (Behandlungsfehler Aufklärungspflicht-Verletzung Honorarstreit GOAe EBM Approbationsrecht Krankenhausrecht Heilmittelwerberecht Vertragsarztrecht KV-Recht Apotheken- und Arzneimittelrecht Pharmastrafrecht) Sofort-Fristen-Check Verjährung drei Jahre § 195 BGB ab Kenntnis Hoechstfrist dreissig Jahre Personenschaden § 199 Abs. 2 BGB Approbations-Widerruf-Verfahren Vorlaeufige Ruhensanordnung. Eskalation Telefon-Sofort bei Approbations-Verlust drohend. Routing zu behandlungsfehler-anspruch-prüfen."
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
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.

## Vertiefung — Rechtsprechung und Normenkette

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Ergänzung — Wichtige Normen Triage-Routing

- § 195 BGB (regelmäßige Verjährung 3 Jahre) i.V.m. § 199 Abs. 1 BGB (Kenntnis-Beginn) und § 204 BGB (Hemmung durch Klage, Schlichtungsantrag, Mahnbescheid)
- § 630g BGB (Einsichtsrecht Patientenakte — unverzüglich zu gewähren, Kopien auf Kosten des Patienten)
- § 116 SGB X (Übergang Schadensersatzanspruch auf Sozialversicherungsträger)
- § 299a StGB (Bestechlichkeit im Gesundheitswesen), § 299b StGB (Bestechung im Gesundheitswesen)
- §§ 203, 204 StGB (Schweigepflicht, Schweigepflichtentbindung obligatorisch vor Aktenweitergabe)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.