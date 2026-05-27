---
name: mandat-triage-vergaberecht
description: "Eingangs-Triage fuer vergaberechtliche Mandate: Mandantenrolle, Schwellenwert, Verfahrensstand und Frist-Sofort-Check. Normen: § 106 GWB (EU-Schwellen), § 134 GWB (Vorabinformation 10 Kalendertage Stillhaltefrist), § 160 Abs. 3 GWB (Ruegefrist 15 Tage). Pruefraster: Mandantenrolle (Bieter/Auftraggeber), Schwelle, Verfahrensstand (Bekanntmachung bis Zuschlag), Frist-Sofort-Check, Eskalation bei drohendem Zuschlag. Output Triage-Protokoll, Fristen-Ampel, Routing. Abgrenzung: Detailpruefung siehe vergabe-nachpruefung-aussicht; Schriftsatz siehe ruegeschriftsatz-erstellen."
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
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

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

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Vergaberecht Mandat triage und routen | Triage-Protokoll; Template unten |
| Variante A — Unterhalb EU-Schwellenwert | Nationales Haushalts-/Vergaberecht; keine VK-Zustaendigkeit |
| Variante B — Verteidigung Auftraggeber | Andere Beratungsrichtung; VK-Verteidigung |
| Variante C — Eilsituation Stillhaltefrist | Frist-Prioritaet; Ruege und NPA sofort |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Ausgabe

- `triage-protokoll-vergaberecht.md`
- Aktenanlage
- Frist im Fristenbuch (zehn Kalendertage § 134 GWB fünfzehn Kalendertage § 160 GWB)
- Rüge-Schriftsatz-Entwurf
- Nachprüfungs-Antrag-Entwurf bei akutem Bedarf
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Quellen

- GWB §§ 97 ff. 123 124 127 134 135 155 160 167 169 171 173 181
- VgV VOB/A-EU UVgO SektVO KonzVgV
- GKG § 50
- BGH XIII. Zivilsenat (Vergaberecht seit 01.01.2021; vorher X. Zivilsenat)
- Burgi Vergaberecht

## Vertiefung: Leitsaetze und Output-Template Triage

### Triage-Vertiefung — kritische Vergaberecht-Fristen

- BGH, Beschl. v. 03.07.2020 - X ZB 12/19, NJW 2020, 2880 — Ruegeobliegenheit: max. 10 Tage nach Kenntnis.
- BGH, Beschl. v. 18.06.2019 - X ZB 4/19, NJW 2019, 3151 — 15 Tage Nachpruefungsantrag nach Ruegerueckweisung.
- BGH, Beschl. v. 12.07.2021 - X ZB 7/20, NJW 2022, 58 — Bieter muss konkrete Beeintraechtigung seiner Vergabechancen darlegen.
- OLG Dusseldorf, Beschl. v. 25.01.2023 - Verg 30/22, NZBau 2023, 255 — Wertungsmatrix: transparente Anwendung obligatorisch.

### Output-Template Triage-Protokoll Vergaberecht
**Adressat:** Intern — Tonfall: schnell, fristorientiert

```
TRIAGE-PROTOKOLL Vergaberecht
=========================================
Eingangsdatum:              [TT.MM.JJJJ]
Mandant:                    [NAME / UNTERNEHMEN]
Vergabeverfahren:           [BEZEICHNUNG, TED-NR.]
Auftragsgegenstand:         [LIEFERUNG / DIENSTLEISTUNG / BAU]
Auftragswert (geschaetzt):  EUR [BETRAG]
EU-Schwellenwert:           UEBERSCHRITTEN / NICHT UEBERSCHRITTEN
Mandantenrolle:             [Bieter / Auftraggeber / Beigeladene]
Verstoss:                   [WERTUNG / EIGNUNG / DISKRIMINIERUNG ...]
Kenntnisdatum:              [TT.MM.JJJJ]
Ruegeobliegenheit-Frist:    [TT.MM.JJJJ]
Informationsschreiben §134: [JA vom DATUM / NEIN]
Stillhaltefrist bis:        [DATUM]
Zuschlag erteilt:           JA / NEIN
Prioritaet:                 ROT (Sofort) / GELB / GRUEN
Naechster Schritt:          [Ruege / NPA / §181-Klage]
=========================================
```
