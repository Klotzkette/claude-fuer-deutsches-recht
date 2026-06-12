---
name: forderungsaufnahme
description: "Forderung systematisch aufnehmen: Gläubiger, Schuldner, Rechtsgrund, Hauptforderung, Nebenforderungen (Zinsen § 288 BGB, vorgerichtliche Anwaltskosten § 280, § 286 BGB, Mahngebuehren), Faelligkeit § 271 BGB, Verjährungsbeginn § 199 BGB. Output: vollstaendige Forderungsbeschreibung als Basis für..."
---

# Forderungsaufnahme

Erste systematische Erfassung einer Forderung vor jeder rechtlichen Handlung. Zweck: Vollstaendigkeit der Datenbasis, frueherkennung von Klagehindernissen, Eingangstuer für alle anderen Skills.

## Aufnahme-Schema

### 1. Gläubiger

| Datenfeld | Erforderlich | Beleg |
|---|---|---|
| Name natuerliche Person / Firma | ja | Personalausweis / HRB-Auszug |
| Rechtsform (GmbH, AG, GbR, eK) | ja | HRB-Auszug |
| Vertretungsberechtigung | ja | HRB-Auszug, Prokura |
| Anschrift | ja | aktuelle Auskunft |
| USt-ID / Kleinunternehmer § 19 UStG | ja | Steuerbescheid |
| Bankverbindung | ja | Kontoinhabernachweis |
| Verbraucher oder Unternehmer? | ja | Geschäftszweck |

### 2. Schuldner

| Datenfeld | Erforderlich | Beleg |
|---|---|---|
| Name natuerliche Person / Firma | ja | offizielle Korrespondenz |
| Rechtsform | ja | HRB / Vereinsregister / GbR-Vertrag |
| Vertretungsberechtigung | ja | HRB aktuell (nicht aelter als 6 Monate) |
| Ladungsfaehige Anschrift | ja | Meldeauskunft, Handelsregister |
| Verbraucher oder Unternehmer? | ja | Vertragszweck |
| Insolvenzstatus | prüfen | [insolvenzbekanntmachungen.de](https://www.insolvenzbekanntmachungen.de) |
| Bonitaetsindikatoren | prüfen | Creditreform, Schufa |
| Auslandsbezug | prüfen | EuGVVO/EuMVVO/Brusssel Ia |

### 3. Rechtsgrund

Praezise Subsumtion welcher Anspruch auf welcher Norm beruht:

| Anspruchstyp | Norm | Faelligkeitsregel |
|---|---|---|
| Kaufpreis Sache | § 433 Abs. 2 BGB | mit Lieferung (§ 271 BGB) |
| Kaufpreis Online | § 433 Abs. 2 BGB | i.d.R. Vorkasse / mit Versand |
| Werklohn | § 631 Abs. 1, § 641 BGB | nach Abnahme |
| Honorar Anwalt | § 8 RVG | nach Erledigung Auftrag |
| Honorar Arzt | § 12 GOAE / GOZ | Rechnungserteilung |
| Mietzins | § 535 Abs. 2 BGB | im voraus zum 3. Werktag (§ 556b BGB) |
| Pacht | § 581 BGB | nach Vertrag |
| Darlehen Rueckzahlung | § 488 Abs. 3 BGB | mit Faelligkeit (Kuendigung) |
| Schadensersatz | §§ 280, 281, 823 BGB | mit Schadenseintritt |
| Bereicherung | § 812 BGB | mit Erlangung |

### 4. Hauptforderung

- Genauer Betrag in EUR.
- Brutto/Netto unterscheiden (B2B mit Vorsteuerabzug oft netto, B2C immer brutto).
- Teilzahlungen abziehen, mit Datum und Verbuchungsreihenfolge nach § 366 BGB.

### 5. Nebenforderungen

| Position | Norm | Voraussetzung |
|---|---|---|
| Verzugszinsen | § 288 Abs. 1/2 BGB | Verzug (§ 286 BGB) |
| Faelligkeitszinsen B2B | § 353 HGB | Faelligkeit |
| Verzugspauschale 40 EUR | § 288 Abs. 5 BGB | Verzug + B2B |
| Mahnkosten | § 280, 286 BGB | Konkreter Aufwand ab 2. Mahnung |
| Vorgerichtliche Anwaltskosten | § 280, 286 BGB | Erforderlich + verhaeltnismaessig |
| Auskunftskosten (Meldeauskunft, HRB) | § 280, 286 BGB | Erforderlich |
| Mahngebuehren Inkassobuero | § 4 RDGEG | begrenzt auf RA-Geschäftsgebuehr |

### 6. Faelligkeit § 271 BGB

- Sofort bei Vertragsschluss, sofern nicht abweichend bestimmt.
- Werkvertrag: nach Abnahme (§ 641 BGB).
- Verbrauchsguterkauf: mit Lieferung.
- Stundung verschiebt Faelligkeit nach hinten.

### 7. Verjährung § 199 BGB

- Berechnung Verjährungsbeginn: Schluss des Jahres mit Kenntnis.
- Regelverjaehrung 3 Jahre (§ 195 BGB).
- Hoechstfristen 10 / 30 Jahre (§ 199 Abs. 2-4 BGB).

### 8. Belege / Anlagenliste

| Beleg | Zweck |
|---|---|
| Vertrag / Auftragsbestaetigung / AGB | Anspruchsgrund |
| Lieferschein / Abnahmeprotokoll | Erfuellung Kläger |
| Rechnung | Bezifferung, Faelligkeitsausloeser |
| Mahnungen mit Zustellnachweis | Verzug |
| Kontoauszuege | Teilzahlungen, Anrechnung § 366 BGB |
| Korrespondenz | Anerkenntnisse § 212 BGB |
| Handelsregisterauszug | Vertretung, Identitaet |

## Forderungsaufstellung (Output-Template)

```
Forderungsaufstellung Stand TT.MM.JJJJ
Glaeubiger:      [Name, Anschrift]
Schuldner:       [Name, Anschrift, ladungsfaehig]
Rechtsgrund:     [Vertragstyp, Datum, ggf. AGB]

Hauptforderung:                              EUR ...
Teilzahlungen (mit Datum, § 366 BGB):       EUR -...
Restliche Hauptforderung:                    EUR ...
Verzugszinsen [Zinssatz, Zeitraum]:         EUR ...
Verzugspauschale § 288 Abs. 5 BGB:          EUR 40,00
Mahnkosten:                                  EUR ...
Vorgerichtliche RA-Kosten (1,3 GG):         EUR ...
==============================================
Gesamtforderung:                             EUR ...
```

## Klagehindernisse fruehzeitig erkennen

- Verjährung droht (Restlaufzeit < 6 Monate) → MB / Klage sofort.
- Insolvenz Schuldner → § 174 InsO Tabelle, keine Klage.
- Vergleichsbereitschaft → Stundung dokumentieren (Anerkenntnis § 212 BGB nutzt).
- AGB-Vereinbarung mit unwirksamen Klauseln → § 305 ff. BGB Kontrolle.
- Schiedsklausel → § 1029 ZPO statt Klage.

## Quellen
- BGB § 271 Faelligkeit [gesetze-im-internet.de/bgb/__271.html](https://www.gesetze-im-internet.de/bgb/__271.html)
- BGB § 286, 288 [gesetze-im-internet.de/bgb/__286.html](https://www.gesetze-im-internet.de/bgb/__286.html)
- BGB § 366 Tilgungsbestimmung [gesetze-im-internet.de/bgb/__366.html](https://www.gesetze-im-internet.de/bgb/__366.html)
- BGB § 195, 199 Verjährung [gesetze-im-internet.de/bgb/__195.html](https://www.gesetze-im-internet.de/bgb/__195.html)
- RDGEG § 4 Inkassokosten [gesetze-im-internet.de/rdgeg/__4.html](https://www.gesetze-im-internet.de/rdgeg/__4.html)
- Insolvenzbekanntmachungen [insolvenzbekanntmachungen.de](https://www.insolvenzbekanntmachungen.de)
