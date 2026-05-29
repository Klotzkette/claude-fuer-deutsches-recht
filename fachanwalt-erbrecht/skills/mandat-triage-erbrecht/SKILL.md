---
name: mandat-triage-erbrecht
description: "Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen. §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Prüfraster: Erbfolge Testament Ausschlagungsfrist Pflichtteil Nachlassinsolvenz. Output: Triage-Memo Sofortmassnahmen Fristen-Ampel. Abgrenzung: Triage; Detailarbeit in Spezialist-Skills."
---

# Mandat-Triage Erbrecht

## Aktuelle Rechtsprechung (Triage-Orientierung, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH 12.03.2025 - IV ZR 88/24 (Pflichtteilsanspruch nichteheliches Kind; § 2317 Abs. 1 BGB maßgebend trotz Ausübungssperre)
- BGH 02.07.2025 - IV ZR 93/24 (Zuwendung an behandelnden Arzt; Berufsordnung kein § 134 BGB-Verbot; Testierfreiheit; § 138 BGB Einzelfallprüfung)

Anhängig: BVerfG 1 BvR 804/22 zur Verfassungsmäßigkeit der erbschaftsteuerlichen Begünstigung von Betriebsvermögen (Stand 05/2026 nicht entschieden).

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org oder openjur.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Erbrechtsmandate sind zeitkritisch (Ausschlagungsfrist) und psychologisch sensibel. Triage stellt Sofort-Fristen sicher und ordnet das Mandat dem richtigen Folge-Skill zu.

## Ablauf — sieben Fragen

### Frage 1 — Vorsorge oder Abwicklung?

- Vorsorge (Erblasser lebt — Testament Erbvertrag Vorsorgevollmacht)
- Abwicklung (Erblasser verstorben — Erbschein Pflichtteil Auseinandersetzung)
- Streit über Lebzeit-Schenkungen

### Frage 2 — Mandantenrolle?

- Erblasser (vor Tod)
- Erbe (Alleinerbe Miterbe)
- Pflichtteilsberechtigter (enterbt oder zu wenig erhalten)
- Vermächtnisnehmer
- Testamentsvollstrecker
- Erblasser-Gläubiger
- Nachlassgläubiger
- Finanzamt (selten — vertretbar nur unter strikter Trennung)

### Frage 3 — Akute Eilbedürftigkeit?

- **Ausschlagungsfrist** läuft (sechs Wochen ab Kenntnis § 1944 BGB; sechs Monate bei Auslandsbezug oder Erblasser-Wohnsitz Ausland)
- **Erbenhaftung droht** — überschuldeter Nachlass
- **Vorrätige Nachlassgegenstände** akut zu sichern
- **Beerdigung organisatorisch** offen
- **Erbschaftsteuer-Anzeige** drei Monate § 30 ErbStG
- **Räumung Wohnung** Mietvertrag Erblasser
- **Patientenverfügung Vorsorge** akut benötigt — meist `betreuungsrecht`-Plugin

### Frage 4 — Vorgang konkret?

- Erbschein-Antrag
- Testamentseröffnung
- Testamentsanfechtung
- Erbauseinandersetzung (Teilungsversteigerung)
- Pflichtteils-Anspruch
- Vermächtnis-Anspruch
- Auflagen-Erfüllung
- Erbschaftsausschlagung
- Nachlassinsolvenz
- Erbschaftsteuer
- Testamentsvollstreckung

### Frage 5 — Verfügungen?

- Testament öffentlich oder eigenhändig
- Berliner Testament
- Erbvertrag notariell
- Patientenverfügung Vorsorgevollmacht
- Schenkungsversprechen Schenkungsverträge
- Lebensversicherung mit Bezugsberechtigung

### Frage 6 — Familienverhältnisse?

- Ehegatte / eingetragener Lebenspartner — Güterstand!
- Abkömmlinge (eheliche nichteheliche adoptiert)
- Eltern — sofern keine Abkömmlinge
- Geschwister Verwandte zweite Ordnung
- Patchwork-Konstellation

### Frage 7 — Wirtschaftliche Verhältnisse?

- Nachlasswert geschätzt
- Schulden
- Schenkungen letzte zehn Jahre
- Pflichtteils-Verzichts-Verträge
- Erbschaftsteuer-Belastung
- Mandanten-Vermögen (PKH-Bedürftigkeit)

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Pflichtteil | `pflichtteil-berechnen` |
| Vorsorge Testament-Vertragsentwurf | (Skill testament-erbvertrag-entwurf — perspektivisch) |
| Erbschein-Antrag | (Skill erbschein-antrag — perspektivisch) |
| Testamentsanfechtung | (Skill testamentsanfechtung — perspektivisch) |
| Erbauseinandersetzung | (Skill erbauseinandersetzung — perspektivisch) |
| Ausschlagung überschuldet | (Skill ausschlagung-nachlassinsolvenz — perspektivisch) |
| Erbschaftsteuer | weiter an `anw-mandat-triage-steuerrecht` ErbSt-Spezifikum |
| Testamentsvollstreckung | (Skill testamentsvollstreckung — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — keine doppelte Vertretung Miterben gegeneinander
- **Streitwert** Nachlasswert oder Pflichtteils-Forderungs-Höhe
- **Komplexität** Auslandsbezug Unternehmensbeteiligung Stiftungs-Errichtung

## Sofort-Fristen

- **Ausschlagung** sechs Wochen § 1944 BGB
- **Pflichtteils-Verjährung** drei Jahre § 2332 BGB
- **Erbschaftsteuer-Anzeige** drei Monate § 30 ErbStG
- **Erbschaftsteuer-Erklärung** mind. ein Monat nach Aufforderung
- **Anfechtung Testament** ein Jahr ab Kenntnis § 2082 BGB

## Eskalation

- **Telefon-Sofort** Ausschlagungsfrist läuft heute / morgen — überschuldeter Nachlass
- **Binnen einer Stunde** Erbenhaftung droht
- **Heute** Auskunftsschreiben § 2314 BGB Erbschein-Antrag-Vorbereitung
- **Diese Woche** Pflichtteils-Stufenklage Testamentsentwurf

## Ausgabe

- `triage-protokoll-erbrecht.md`
- Aktenanlage
- Frist im Fristenbuch (Ausschlagung Pflichtteils-Verjährung Erbschaftsteuer)
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill
- Hinweis Sachverständigen-Bewertung Immobilie Unternehmen wenn relevant

## Quellen

- BGB §§ 1922 ff. 1944 2303 ff. 2332 § 2082
- ErbStG § 30
- BGH IV. Zivilsenat
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Burandt/Rojahn Erbrecht
