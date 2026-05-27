---
name: mandat-triage-transport-speditionsrecht
description: "Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs. international. Normen: §§ 407 454 HGB, CMR. Pruefraster: Vertragstyp, Schadenstyp, Dringlichkeit, Fristen. Output: Mandat-Triage-Protokoll Transport-Speditionsrecht. Abgrenzung: nicht Erstgespraeches-Aufnahme."
---

# Mandat-Triage Transport- und Speditionsrecht

## Zweck

Transportmandate sind zeitkritisch — Reklamationsfristen sind kurz und können Anspruchsverlust de facto bedeuten. Triage stellt sicher dass die Frist gewahrt wird.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Versender / Verlader
- Empfänger
- Frachtführer
- Spediteur
- Lager-Betreiber
- Versicherer (Cargo Verkehrshaftung)
- Subunternehmer / Nachunternehmer

### Frage 2 — Verkehrsträger?

- Straße — Lkw
- Schiene — Eisenbahn
- Wasser — Binnen / See
- Luft
- Multimodal — kombiniert
- Lager / Umschlag

### Frage 3 — Geografie?

- Inland
- Grenzüberschreitend EU
- Grenzüberschreitend Drittstaat
- Transit

### Frage 4 — Akute Eilbedürftigkeit?

- **Reklamationsfrist** läuft (sofort / sieben / einundzwanzig Tage)
- **Verjährungsfrist** ein Jahr läuft ab
- **Gefahrgut-Zwischenfall** ADR-Meldung
- **Embargo / Sanktionen** plötzlich greifend
- **Beschlagnahme Zoll** Akut
- **Frachtgut nicht ausgehändigt** wegen Frachtstreit
- **Versicherungs-Stichtag** läuft

### Frage 5 — Sachgebiet?

- Verlust Sendung
- Beschädigung Sendung
- Lieferfrist-Überschreitung
- Frachtforderung Frachtführer
- Speditionsvergütung
- Multimodal-Vertrag
- Gefahrgut-Recht
- Zollrecht
- Lagerlogistik
- Transport-Versicherungs-Streit
- Frachtbrief-Fälschung

### Frage 6 — Frist?

- **Reklamation Verlust erkennbar Beschädigung** sofort schriftlich
- **Reklamation verdeckter Schaden** sieben Tage CMR Art. 30 / § 438 HGB
- **Reklamation Verzug** einundzwanzig Tage
- **Verjährung CMR** ein Jahr / drei Jahre bei Vorsatz
- **Verjährung HGB** ein Jahr / drei Jahre
- **Versicherungs-Anspruch** drei Jahre § 195 BGB
- **CMR-Klage** ein Jahr nach Ablieferung

### Frage 7 — Wirtschaftliche Verhältnisse?

- Versicherung Cargo Verkehrshaftung
- Schadenshöhe vs. SDR-Begrenzung
- Streitwert für Klage
- Bei Spedition: ADSp-Geltung

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Schadensersatz Frachtführer | `frachtfuehrerhaftung-pruefen` |
| Speditionsverhalten | `frachtfuehrerhaftung-pruefen` plus ADSp Spezifika |
| Frachtforderung-Klage | (Skill frachtforderung — perspektivisch) |
| Multimodal-Vertrag | (Skill multimodal — perspektivisch) |
| Gefahrgut ADR | (Skill gefahrgut-adr — perspektivisch) |
| Zollrecht | weiter an `mandat-triage-verwaltungsrecht` plus Spezial |
| Versicherungs-Streit | weiter an `mandat-triage-versicherungsrecht` |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Versender/Frachtführer
- **Streitwert** Sendung-Wert oder Frachtforderung
- **Sachverständigen-Bedarf** Transport- und Verpackungs-SV
- **Versicherungs-Deckung** Verkehrshaftungs-Versicherung Mandant prüfen

## Eskalation

- **Telefon-Sofort** Reklamationsfrist heute / morgen Gefahrgut-Vorfall
- **Binnen einer Stunde** Schriftliche Reklamation Frachtbrief-Bemerkung
- **Heute** Auskunfts-Aufforderung an Frachtführer
- **Diese Woche** Klage vor Verjährungs-Ablauf

## Ausgabe

- `triage-protokoll-transport-spedition.md`
- Aktenanlage mit Verkehrsträger und Anwendung CMR/HGB
- Frist im Fristenbuch (Reklamation Verjährung)
- Reklamations-Schreiben sofort
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

## Quellen

- CMR 1956
- HGB §§ 407 ff. 453 ff.
- MÜ CIM CMNI
- ADSp
- BGH I. Zivilsenat
- Koller Transport-/Speditionsrecht

## Aktuelle Rechtsprechung Triage Transport

- BGH, Urt. v. 29.01.2015 - I ZR 195/13, NJW 2015, 2426 — Verjaehrungs-Sofort-Check: HGB § 439 kennt nur 1 Jahr Verjaehrung (Sonderrecht); versaeumter Hinweis auf kuerzere Verjaehmrungsfrist als im allg. BGB-Recht (3 Jahre) begruendet Anwaltshaftung.
- BGH, Urt. v. 01.02.2018 - I ZR 246/16, NJW 2018, 1382 — CMR Art. 32: internationale Transporte unterliegen CMR-Verjaehrung (1 Jahr; 3 Jahre bei Vorsatz); nationale HGB-Verjaehrung tritt zurueck; Triage muss pruefen: grenzueberschreitend oder national?
- OLG Koeln, Urt. v. 07.05.2019 - 3 U 40/18, TranspR 2019, 348 — Multimodal-Transport: Triage muss klaeren, welches Recht gilt, wenn Transport Strasse und Schiene kombiniert; unimodales Regime nur anwendbar, wenn Schadensort bekannt (§ 452a HGB).
