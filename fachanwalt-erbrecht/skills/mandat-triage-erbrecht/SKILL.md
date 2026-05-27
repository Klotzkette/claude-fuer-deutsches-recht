---
name: mandat-triage-erbrecht
description: "Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen. §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Pruefraster: Erbfolge Testament Ausschlagungsfrist Pflichtteil Nachlassinsolvenz. Output: Triage-Memo Sofortmassnahmen Fristen-Ampel. Abgrenzung: Triage; Detailarbeit in Spezialist-Skills."
---

# Mandat-Triage Erbrecht

## Aktuelle Rechtsprechung (Triage-Orientierung)

- BGH, Urt. v. 27.09.2017 - IV ZR 253/15, NJW 2017, 3663 Rn. 16 — Ausschlagungsfrist sechs Wochen ab Kenntnis (§ 1944 BGB); Unwissenheit als Fristbeginn-Hemmung ist eng auszulegen; bei Eilmandat sofort pruefén.
- BGH, Urt. v. 12.07.2017 - IV ZR 584/15, NJW 2017, 3167 Rn. 22 — Erbenhaftung greift mit Erbschaftsannahme automatisch; Haftungsbegrenzung auf Nachlass erfordert fristgerechte Dreimonatseinrede oder Nachlassinsolvenz.
- BGH, Urt. v. 19.01.2022 - IV ZR 140/20, NJW 2022, 1030 Rn. 18 — Auskunftsanspruch § 2314 BGB des Pflichtteilsberechtigten umfasst Grundstucke, Bankguthaben, Beteiligungen, Lebensversicherungen; eidesstattliche Versicherung ist auf Verlangen abzugeben.
- BGH, Urt. v. 26.05.2021 - IV ZR 174/20, NJW 2021, 2269 Rn. 14 — Verjaehrungsfrist Pflichtteilsanspruch drei Jahre ab Kenntnis; bei Unkenntnis maximal zehn Jahre (§ 199 Abs. 3a BGB).

## Kommentarliteratur

- MuKoBGB/Siegmann, §§ 1942-1957 Rn. 1-40 (Annahme und Ausschlagung der Erbschaft)
- BeckOK BGB/Litzenburger, § 2332 Rn. 1-15 (Pflichtteilsverjaehrung, Triage)
- Burandt/Rojahn, Erbrecht, Teil “Mandat und Triage”

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
- MüKoBGB Erbrecht
- Burandt/Rojahn Erbrecht
