---
name: zv-kontensuche-drittschuldner
description: "Konten und Drittschuldner des Schuldners finden, wenn Bank, Arbeitgeber oder Forderungsschuldner unbekannt sind. Nutzt § 802l ZPO Drittauskünfte (Rentenversicherung Bund, Bundeszentralamt für Steuern Kontenabruf, Kraftfahrt-Bundesamt) sowie Schuldnerverzeichnis § 882b ZPO. Lädt vor jeder PfÜB-Pfändung ohne bekannten Drittschuldner."
---

# Kontensuche und Drittschuldnerermittlung

## Aufgabe

Bevor eine Forderungspfändung Sinn ergibt, muss der Drittschuldner bekannt sein. Dieser Skill beschafft die Daten, ohne unnötige PfÜB ins Leere zu werfen.

## Startet bei

- Titel vorhanden, aber kein Konto, kein Arbeitgeber, keine sonstige Forderung des Schuldners bekannt
- Frühere Versuche ergebnislos
- Vermögensauskunft des Schuldners liegt vor oder Sperrfrist hindert sie nicht

## Rechtsgrundlagen

- § 802l ZPO – Drittauskünfte des Gerichtsvollziehers
- § 93 Abs. 7 AO – Kontenabrufverfahren über das BZSt
- § 24c KWG – Kontenevidenzzentrale der BaFin
- § 802c ZPO – primäre Quelle: Vermögensauskunft
- § 882b ZPO – Schuldnerverzeichnis
- § 33 StVG – Halterauskunft KBA

## Workflow

1. **Schuldnerverzeichnis abfragen** über das zentrale Vollstreckungsportal der Länder (`vollstreckungsportal.de`). Kostenpflichtig.
2. **Vorhandene Vermögensauskunft einsehen**, falls noch nicht zwei Jahre alt.
3. **Drittauskunft § 802l ZPO** durch den Gerichtsvollzieher beantragen, sobald Forderung mindestens 500 EUR und Vermögensauskunft erfolglos oder Schuldner nicht erreichbar:
   - **Deutsche Rentenversicherung Bund**: aktueller Arbeitgeber oder Rentenzahlstelle
   - **Bundeszentralamt für Steuern (BZSt)**: Kontostammdaten nach § 24c KWG, alle deutschen Kreditinstitute mit Konten des Schuldners
   - **Kraftfahrt-Bundesamt**: KFZ-Halterauskunft
4. **Ausländische Konten**: nicht über § 802l erreichbar, aber EU-Kontenpfändungsbeschluss (EuKtPVO) ist Alternative über `zv-pfueb-bank`.
5. **Plausibilitätsprüfung**: Auskunft veraltet sich. Konten existieren ggf. nicht mehr, Arbeitgeber gewechselt.
6. **Anschluss**: bekannte Bank → `zv-pfueb-bank`, bekannter Arbeitgeber → `zv-pfueb-arbeitsentgelt`.

## Voraussetzungen § 802l ZPO im Einzelnen

- Forderung mindestens 500 EUR (§ 802l Abs. 1 ZPO).
- Schuldner hat seinen gewöhnlichen Aufenthalt unbekannt **oder** Vermögensauskunft hat keine Befriedigung erwarten lassen **oder** Vermögensauskunft wurde nicht abgegeben.
- Antrag stets über den Gerichtsvollzieher; der Gerichtsvollzieher leitet die Anfragen weiter und übermittelt das Ergebnis.

## Leitentscheidungen

- BGH 22.10.2015 – I ZB 70/14 (Voraussetzungen § 802l)
- BGH 26.1.2017 – I ZB 38/16 (Reihenfolge der Drittauskünfte)
- BGH 20.4.2017 – I ZB 88/16 (Kontenabruf trotz neuer Vermögensauskunft)

## Ausgabeformat

```
DRITTSCHULDNERSUCHE [Mandant] gegen [Schuldner]

Titel:                 [Art, Datum]
Forderungshöhe:        EUR x (≥ 500 EUR? ja/nein)
VA-Stand:              [vorhanden, Datum / fehlt / unergiebig]
Beantragte Auskünfte:  [DRV / BZSt / KBA]
Geschätzte Dauer:      4-8 Wochen ab GV-Antrag
Folgeskill:            [zv-pfueb-bank / -arbeitsentgelt / ...]

WIEDERVORLAGE:         DD.MM.JJJJ
```

## Qualitätsgates

- Niemals § 802l ZPO unterhalb der Bagatellgrenze 500 EUR beantragen.
- Niemals BZSt-Kontenabruf ohne erfolglose Vermögensauskunft oder unbekannten Aufenthalt.
- Daten sind sensibel – Datenschutz beachten, Auskunft nur für konkrete Vollstreckung.
- Doppelte Abfragen vermeiden (Kostenfalle).

## Querverweise

- `zv-vermoegensauskunft-gv` – Hauptquelle vor § 802l
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-kommandocenter`
- `zv-elektronische-zustellung-2027`
