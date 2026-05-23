---
name: mandat-triage-vergaberecht
description: Strukturierte Eingangs-Abfrage fuer vergaberechtliche Mandate. Klaert Mandantenrolle (Bieter beteiligt nicht beteiligt potenzieller Bieter oeffentlicher Auftraggeber Sektorenauftraggeber Konzessionsgeber) Schwelle (oberhalb EU-Schwelle unterhalb) Verfahrensstand (Vorinformation Bekanntmachung Teilnahmewettbewerb Submission Vorabinformation Zuschlag § 134 GWB Nachpruefung) Fristen-Sofort-Check Stillhaltefrist § 134 GWB zehn Kalendertage Antragsfrist § 160 Abs. 3 GWB fuenfzehn Kalendertage. Eskalation Telefon-Sofort bei drohendem Zuschlag binnen 24 Stunden. Routing zu vergabe-nachpruefung-aussicht.
---

# Mandat-Triage Vergaberecht

## Zweck

Vergaberecht ist hochgradig fristen-kritisch — die Stillhaltefrist § 134 GWB ist nur zehn Kalendertage. Triage stellt Sofort-Eilbedürftigkeit fest.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Bieter beteiligt (Angebot abgegeben oder Teilnahme erklärt)
- Potenzieller Bieter (nicht beteiligt aber wollte oder hätte wollen)
- Öffentlicher Auftraggeber (Verteidigung Nachprüfungs-Antrag)
- Sektorenauftraggeber
- Konzessionsgeber
- Subunternehmer / Nachunternehmer

### Frage 2 — Auftragsart?

- Liefer-Auftrag
- Dienstleistungs-Auftrag
- Bauauftrag (VOB/A-EU)
- Konzession
- Sektorenauftraggeber-Vergabe
- Mischauftrag
- Rahmen-Vereinbarung

### Frage 3 — Schwelle?

- Oberhalb EU-Schwelle (Schwellenwerte aktuell prüfen — Liefer-/Dienstleistungs-Bund EUR 143000 Kommunen EUR 221000 Bau EUR 5538000)
- Unterhalb EU-Schwelle (Landes-/Kommunalvergabeverfahren UVgO)

### Frage 4 — Verfahrensstand?

- Vor Bekanntmachung (Auftraggeber-Beratung)
- Bekanntmachung erschienen — Teilnahme-Vorbereitung
- Teilnahmewettbewerb
- Angebot-Abgabefrist offen
- Submission erfolgt — Wertung
- Vorabinformation § 134 GWB erhalten
- Zuschlag erteilt
- Nachprüfungsantrag bei VK läuft
- Sofortige Beschwerde OLG

### Frage 5 — Akute Eilbedürftigkeit?

- **Stillhaltefrist § 134 GWB** zehn Kalendertage — Zuschlag droht
- **Eil-Antrag** § 169 GWB Zuschlag-Sperre
- **Fünfzehn-Kalender-Tage-Frist** § 160 Abs. 3 GWB
- **Angebot-Abgabefrist** kurz
- **Klage gegen Direktvergabe** ohne Bekanntmachung

### Frage 6 — Rüge erfolgt?

- Rüge an Auftraggeber abgesendet?
- Datum Rüge?
- Reaktion Auftraggeber?
- Nicht-Abhilfe Mitteilung?

### Frage 7 — Wirtschaftliche Verhältnisse?

- Auftrag-Volumen (Streitwert § 50 Abs. 2 GKG fünf Prozent Bruttoauftragssumme)
- Gewinn-Erwartung Mandant
- Kostenrisiko bei Verfahren
- Versicherungs-Deckung

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Nachprüfungs-Antrag VK | `vergabe-nachpruefung-aussicht` |
| Direktvergabe ohne Bekanntmachung | `vergabe-nachpruefung-aussicht` plus § 135 GWB Unwirksamkeit |
| Sofortige Beschwerde OLG | `vergabe-nachpruefung-aussicht` plus Berufungs-Strategie |
| Vergabe-Schadensersatz | (Skill vergabe-schadensersatz — perspektivisch) |
| Unterhalb-Schwelle | (Skill unterhalb-schwelle-uvgo — perspektivisch) |
| Auftraggeber-Beratung Verfahrenswahl | (Skill verfahrenswahl-beratung — perspektivisch) |

## Eilmodus Stillhaltefrist

Bei Stillhaltefrist § 134 GWB läuft:

1. Kalender prüfen — wann genau Eingang Vorabinformation?
2. Rüge sofort an Auftraggeber sofern nicht erfolgt
3. Bei Nicht-Abhilfe oder Schweigen: Nachprüfungs-Antrag VK fünfzehn Tage
4. Antrag mit Eil-Antrag § 169 GWB Aufschiebung
5. Bei Drohung Zuschlag binnen 24 Stunden: Eil-Antrag VK mit aufschiebender Wirkung

## Mandatsannahme

- **Konflikt-Check** — kein Doppel-Mandat unter Bietern
- **Streitwert** § 50 Abs. 2 GKG fünf Prozent Brutto-Auftragssumme bei Liefer- Dienstleistungs- und Bauaufträgen — ohne gesetzliche Höchst- oder Mindestgrenze (BGH XIII ZB 64/21 vom 29.11.2022 zur Berechnungsgrundlage einschließlich durchlaufender Posten)
- **Komplexität** Sachverständigen-Bedarf technisch Kalkulationen
- **Versicherungs-Deckung** Bietern selten — Berufshaftpflicht Anwalt prüfen

## Eskalation

- **Telefon-Sofort** Stillhaltefrist läuft binnen 24 Stunden
- **Binnen einer Stunde** Rüge-Schriftsatz Vergabekammer-Eil-Antrag
- **Heute** Nachprüfungs-Antrag bei VK
- **Diese Woche** Sofortige Beschwerde OLG bei VK-Beschluss

## Ausgabe

- `triage-protokoll-vergaberecht.md`
- Aktenanlage
- Frist im Fristenbuch (zehn Kalendertage § 134 GWB fünfzehn Kalendertage § 160 GWB)
- Rüge-Schriftsatz-Entwurf
- Nachprüfungs-Antrag-Entwurf bei akutem Bedarf
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

## Quellen

- GWB §§ 97 ff. 123 124 127 134 135 155 160 167 169 171 173 181
- VgV VOB/A-EU UVgO SektVO KonzVgV
- GKG § 50
- BGH XIII. Zivilsenat (Vergaberecht seit 01.01.2021; vorher X. Zivilsenat)
- Burgi Vergaberecht
