---
name: mandat-triage-strafrecht
description: "Strukturierte Eingangs-Abfrage fuer Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschuldigtenrechte § 136 § 137 § 140 § 141 StPO Pflichtverteidiger-Bestellung Mitbeschuldigte (Konflikt-Check § 43a BRAO § 146 StPO). Sofort-Fristen-Check Haftbeschwerde § 117 StPO Haftpruefung § 117 § 118 StPO Akteneinsicht § 147 StPO. Eskalation Telefon-Sofort bei Untersuchungshaft binnen 24 Stunden. Routing zu akteneinsicht-strafrecht-auswerten."
---

# Mandat-Triage Strafrecht

## Zweck

Erstkontakt im Strafverfahren — oft mit hoher Eilbedürftigkeit (Festnahme U-Haft Durchsuchung). Strukturierte Triage stellt rechtliche und kommunikative Priorität sicher.

## Ablauf — acht Fragen

### Frage 1 — Wer ruft an und für wen?

- Beschuldigter selbst
- Angehöriger
- Polizei (selten — Notdienst)
- Anderer Anwalt (Vertretung)

### Frage 2 — Akute Eilbedürftigkeit?

- Festnahme erfolgt — Vorführung läuft heute
- Untersuchungshaft seit Stunden / Tagen
- Durchsuchung läuft / steht bevor
- Aussage bei Polizei für heute terminiert
- Hauptverhandlung beginnt morgen

**Eskalation:** Festnahme U-Haft Durchsuchung → Telefon-Sofort an Anwalt; binnen einer Stunde Beistand; Anwesenheit bei Vernehmung Pflicht.

### Frage 3 — Verfahrensstadium?

- Ermittlungsverfahren bei Polizei (kein Aktenzeichen StA noch nicht)
- Ermittlungsverfahren bei Staatsanwaltschaft (Az StA vorhanden)
- Zwischenverfahren (Anklage zugestellt — Eröffnungsbeschluss?)
- Hauptverfahren (Hauptverhandlungstermin)
- Berufung / Revision
- Strafvollstreckung
- Strafvollzug (Vollzugsplan Lockerungen Strafaussetzung)

### Frage 4 — Tatvorwurf?

- Norm (§ ggf. StGB Nebengesetz)
- Strafrahmen — Vergehen unter ein Jahr Vergehen ab ein Jahr Verbrechen ab ein Jahr Mindeststrafe (§ 12 StGB)
- Bei Verbrechen oder Strafrahmen ab ein Jahr — notwendige Verteidigung § 140 StPO

### Frage 5 — Haftsituation?

- In Freiheit
- Vorgeführt — Vorführungsbeschluss / Haftbefehl?
- Untersuchungshaft — Haftgründe (Flucht-, Verdunkelungs-, Wiederholungs-)
- Strafvollzug

### Frage 6 — Mitbeschuldigte?

- Wer ist mitbeschuldigt?
- Ist Mitbeschuldigter bereits anwaltlich vertreten?
- Konflikt-Check § 43a Abs. 4 BRAO § 146 StPO Mehrfachverteidigung verboten

### Frage 7 — Aktenstand?

- Aktenstand nachgefragt?
- Akteneinsicht beantragt § 147 StPO
- Bei U-Haft Pflicht-Akteneinsicht Abs. 4

### Frage 8 — Wirtschaftliche Verhältnisse / Pflichtverteidigung?

- Pflichtverteidigung § 140 § 141 StPO bei notwendiger Verteidigung
- Vergütung nach RVG plus eventuell Honorarvereinbarung

## Routing-Matrix

| Verfahrensstadium | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| U-Haft | Haftbeschwerde § 117 StPO | Haftprüfungsantrag drei Monate § 121 StPO |
| Vorfeld Durchsuchung | Beschwerde § 304 StPO | ggf. nicht statthaft wenn beendet — Feststellungsantrag |
| Polizei-Vernehmung steht an | Verteidigerbeistand § 168c StPO | Termin verlegen oder begleiten |
| Anklage zugestellt | Stellungnahme zur Eröffnung | Frist nach § 201 StPO |
| Hauptverhandlung | `akteneinsicht-strafrecht-auswerten` | Beweisanträge vor Schluss Beweisaufnahme |
| Berufung Revision | Rechtsmittel-Frist eine Woche § 314 StPO | Begründung eine Woche / ein Monat |

## Konflikt-Check

- Mehrfachverteidigung verboten § 146 StPO
- § 43a Abs. 4 BRAO Interessenkollision
- Frühere Vertretung von Mitbeschuldigtem oder Geschädigtem prüfen

## Sofort-Fristen

- **Haftbeschwerde** § 117 StPO — keine Frist aber sinnvoll sofort
- **Haftprüfung** § 117 Abs. 1 StPO — jederzeit
- **Sechs-Monats-Prüfung** OLG § 121 StPO
- **Einspruch Strafbefehl** § 410 StPO zwei Wochen
- **Berufung** § 314 StPO eine Woche
- **Revision** § 341 StPO eine Woche; Begründung § 345 StPO ein Monat

## Eskalationspfad

- **Telefon-Sofort** Vorführung Untersuchungshaft Durchsuchung Vernehmung-Termin heute
- **Binnen einer Stunde** Anfahrt zur Vernehmung — Verteidigerbeistand
- **Heute** Akteneinsichtsantrag § 147 StPO Haftbeschwerde
- **Diese Woche** Stellungnahme Anklage Berufungseinlegung

## Ausgabe

- `triage-protokoll-strafrecht.md` mit acht Fragen
- Aktenanlage Az-Vorschlag
- Fristenbuch-Eintrag (Hauptfrist Vorfrist)
- Mandatsvereinbarung Vorlage mit Pflichtverteidigerbestellungs-Antrag falls notwendig
- Empfehlung Folge-Skill plus Begründung

## Quellen

- StPO §§ 117 121 137 140 141 146 147 168c 201 304 314 341 410
- StGB § 12 (Verbrechen-Vergehen)
- BRAO § 43a
- BVerfGE 70, 297 (Verteidiger-Beistand)

## Aktuelle Rechtsprechung Mandat-Triage

- BVerfG, Beschl. v. 13.10.2016 - 2 BvR 1454/16, NJW 2017, 290 — Pflichtverteidiger-Bestellung muss rechtzeitig erfolgen, damit Verteidiger ausreichend Vorbereitungszeit hat; spaete Bestellung verletzt Recht auf effektive Verteidigung (Art. 6 III lit. c EMRK).
- BVerfG, Beschl. v. 19.01.2015 - 2 BvR 1487/11, NStZ 2015, 417 — Akteneinsicht im Haftverfahren: haftrelevante Aktenbestandteile muessen dem Verteidiger unverzueglich zuganglich gemacht werden; spataestens vor dem Haftpruefungstermin vollstaendige Einsicht.
- BGH, Beschl. v. 14.11.2018 - 1 StR 429/18, NStZ 2019, 164 — Mehrfachverteidigung (§ 146 StPO): auch gemeinsame Vertretung von Beschuldigten, die sich nicht offen widersprechen, kann unzulaessig sein, wenn Interessenkonflikt latent besteht.
- BGH, Urt. v. 25.07.2000 - 1 StR 205/00, BGHSt 46, 130 — GwG-Pflichten des Verteidigers: Honorarannahme aus offensichtlich inkriminierter Quelle begrundet Strafbarkeit nach § 261 StGB auch fuer den Rechtsanwalt.

## Normen Triage-Check

- § 112 StPO — Haftbefehl (Flucht-, Verdunkelungs-, Wiederholungsgefahr)
- § 117 StPO — Haftpruefungsantrag (jederzeit)
- § 118a StPO — Haftpruefungstermin mit muendlicher Verhandlung
- § 140 StPO — notwendige Verteidigung (Bestellungsgrunde)
- § 141 StPO — Pflichtverteidiger-Bestellung (Zeitpunkt, Ablauf)
- § 146 StPO — Verbot Mehrfachverteidigung
- §§ 10 ff. GwG — Identifizierungspflichten Sorgfaltspflichten Rechtsanwalt
