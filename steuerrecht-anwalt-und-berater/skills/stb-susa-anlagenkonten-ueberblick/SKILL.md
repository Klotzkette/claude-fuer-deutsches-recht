---
name: stb-susa-anlagenkonten-ueberblick
description: "Anlagenbuchhaltung in der SuSa Anlagenkonten Klasse 0 SKR 03 immaterielle WG Sachanlagen Finanzanlagen Buchwerte. Anwendungsfall Monats- oder Jahres-SuSa mit Anlagenbestand AfA-Aktualisierung Zu- und Abgaenge. Methodik Anlagenspiegel-Abgleich. Output Anlagen-Kontenuebersicht mit Buchwerten."
---

# Anlagenkonten in der SuSa — Ueberblick und Abstimmung

## Kernsachverhalt

Anlagenkonten der Klasse 0 (SKR 03) bzw. 0xxx-1xxx (SKR 04) zeigen die Buchwerte des Anlagevermoegens: immaterielle WG, Sachanlagen, Finanzanlagen. Die SuSa enthaelt nur die Saldenstaende; die Detailinformation steckt im Anlagenspiegel (Anlagenverzeichnis). Hauptbuch und Anlagenspiegel muessen abgestimmt sein. Der Steuerberater stellt diese Konsistenz monatlich oder mindestens quartalsweise sicher.

## Kaltstart-Rueckfragen

1. Liegt ein aktueller Anlagenspiegel vor (Stichtag, Bewegungen)?
2. Welche Anlagenkategorien — immaterielle WG, Sachanlagen, Finanzanlagen?
3. Werden Anlagen monatlich abgeschrieben (1/12-Methode) oder jaehrlich?
4. Welche Sonderabschreibungen (§ 7g EStG, § 7b EStG, § 6b EStG)?
5. Liegen Zu- oder Abgaenge in der Periode vor (Investitionen, Verkauf)?
6. Sind GWG (gerinwertige Wirtschaftsgueter) bis 800 EUR netto erfasst?
7. Welche AfA-Methode (linear, degressiv, Leistungs-AfA)?
8. Welche Pauschalwertberichtigung Anlagenvermoegen (selten)?

## Rechtlicher Rahmen

### Primaernormen

**§ 247 HGB** — Anlagevermoegen-Definition.

**§ 253 HGB** — Bewertung Anlagevermoegen mit fortgefuehrten Anschaffungs-/Herstellungskosten.

**§ 7 EStG** — AfA-Vorschriften.

**§ 7g EStG** — Sonderabschreibung KMU.

**§ 7b EStG** — Sonderabschreibung Wohnungsbau (befristet, aktuelle Geltung verifizieren).

**§ 6 Abs. 2 EStG** — Geringwertige Wirtschaftsgueter; aktuelle Wertgrenze (zuletzt 800 EUR netto, etwaige Anhebung Stand 2026 in juris verifizieren).

**§ 6 Abs. 2a EStG** — Pool-/Sammelposten-Abschreibung; Wertgrenzen (zuletzt 250-1.000 EUR; etwaige Erhoehung Stand 2026 in juris verifizieren).

### Standards

- BMF AfA-Tabellen (Stand 2026 ueber bundesfinanzministerium.de verifizieren).
- IDW PS 480.
- DATEV/Addison Anlagenbuchhaltungs-Module.

## Workflow

### Phase 1 — Hauptbuch-Bestaende

Anlagenkonten SKR 03 (Kontennummern typische Beispiele; konkrete Nummern mit aktueller DATEV-Kontenrahmenfassung abgleichen):

```
0010   Immaterielle Wirtschaftsgueter
0020   Grundstuecke und Bauten
0080   Maschinen
0440   Geringwertige Wirtschaftsgueter
0500   Fuhrpark
0670   Betriebs- und Geschaeftsausstattung
0900   Anzahlungen auf Anlagen
1000   Beteiligungen
```

### Phase 2 — Anlagenspiegel-Auswertung

```
ANLAGENSPIEGEL (Auszug)
Bezeichnung      Anschaffung  Bisherige AfA  Buchwert Anfang  Zugang  Abgang  AfA Periode  Buchwert Ende
Maschine A       50.000       30.000         20.000           —       —       2.500        17.500
Pkw Mazda        25.000       8.000          17.000           —       —       2.083        14.917
GWG-Pool 2026    1.200        —              —                1.200   —       240          960
Buero-Ausstattung 15.000      6.000          9.000            —       —       1.500        7.500
```

### Phase 3 — Abstimmung Hauptbuch / Anlagenspiegel

- Saldo Hauptbuch Anlagekonten zum Stichtag = Summe Buchwerte Anlagenspiegel?
- Differenz = Fehler.
- AfA-Buchung im Hauptbuch (Konto 4830/4832) = Summe AfA Anlagenspiegel?

### Phase 4 — Zu- und Abgaenge

- Zugang: Anschaffung neu, Aktivierung Eigenleistung, Einlage.
- Abgang: Verkauf, Verschrottung, Entnahme.
- Bei Anlagenabgang: Restbuchwert ausbuchen, Verkaufserloes gegenrechnen.
- Veraeusserungserloese im SKR 03: Konten im 8400er-Bereich (Erloese aus Anlagenverkauf); konkrete Kontonummer fuer steuerfreien bzw. steuerpflichtigen Verkauf im aktuellen DATEV-Kontenrahmen verifizieren.

### Phase 5 — Sonder-AfA und § 6b EStG

- § 7g EStG: Sonderabschreibung fuer KMU (Hoehe und Bedingungen wurden in den letzten Jahren mehrfach angepasst; aktuelle Quote und Voraussetzungen Stand 2026 in juris verifizieren).
- § 7b EStG: Sonderabschreibung Wohnungsneubau (befristete Foerderung; aktuelle Geltungsdauer Stand 2026 pruefen).
- § 6b EStG Ruecklage: bei Veraeusserung Grund und Boden, Gebaeude — Uebertragung auf Reinvestitionen.

### Phase 6 — Reporting

- Anlagenspiegel als Anhang zum Jahresabschluss.
- Monatliche Anlagen-Uebersicht in Quartalsberichten.
- Bei groesseren Investitionen: Beratung zu IAB § 7g EStG.

## Output

- Anlagenspiegel mit Zugaengen, Abgaengen, AfA.
- Hauptbuch-Anlagenspiegel-Abstimmung.
- AfA-Buchungsbeleg fuer SuSa.

## Strategie und Praxis-Tipps

- Anlagenspiegel und Hauptbuch sollten quartalsweise abgestimmt werden.
- GWG-Pool optional (§ 6 Abs. 2a EStG) — bietet Vereinfachung mit Sammelposten-Abschreibung ueber fuenf Jahre.
- Beim Investitionsabzugsbetrag nach § 7g EStG (Quote zuletzt 50 Prozent vorab abziehbar) sind die Bedingungen mehrfach angepasst worden; aktuelle Quote und Anspruchsvoraussetzungen Stand 2026 verifizieren.
- Sonderabschreibungen § 7b EStG sind gesetzlich befristet — Geltung Stand 2026 verifizieren.
- StBVV: Anlagenbuchhaltung als separater Auftrag oder in Buchfuehrungspauschale.
- DATEV-Tipp: DATEV-Anlagenbuchhaltung mit automatischer 1/12-AfA-Buchung in der SuSa (Klickpfad: Anlagenbuchfuehrung → Abschreibungsbuchungen → Buchungsstapel an Rechnungswesen uebergeben).

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-jahresabschluss-anlagenverzeichnis-afa` — JA-AfA-Verzeichnis.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-bwa-aufbau-grundlagen` — BWA.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 247, 253.
- EStG §§ 6, 7, 7b, 7g.
- BMF AfA-Tabellen.
- IDW PS 480.
- Verifikations-Hinweis: § 7b EStG Geltung 2026 verifizieren (Verlaengerung).
- Verifikations-Hinweis: § 7g EStG Konditionen 2026 verifizieren.
