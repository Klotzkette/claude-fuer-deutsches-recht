---
name: susa-anlagenkonten-ueberblick
description: "Anlagenbuchhaltung in der SuSa Anlagenkonten Klasse 0 SKR 03 immaterielle WG Sachanlagen Finanzanlagen Buchwerte. Anwendungsfall Monats- oder Jahres-SuSa mit Anlagenbestand AfA-Aktualisierung Zu- und Abgaenge. Methodik Anlagenspiegel-Abgleich. Output Anlagen-Kontenuebersicht mit Buchwerten."
---

# Anlagenkonten in der SuSa — Ueberblick und Abstimmung

## Fachlicher Anker

- **Normen:** § 6a, § 7g EStG, § 7b EStG.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

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

**§ 7b EStG** — Sonderabschreibung Mietwohnungsneubau (5 % p.a. für 4 Jahre; Bauantrag nach 31.12.2022 und vor 01.10.2029; EH-40 mit QNG-Siegel Pflicht; aktiv bis 2029).

**§ 6 Abs. 2 EStG** — Geringwertige Wirtschaftsgueter; Wertgrenze 800 EUR netto (stabil seit 2018; keine Anhebung beschlossen, Stand 2026).

**§ 6 Abs. 2a EStG** — Pool-/Sammelposten-Abschreibung; Wertgrenzen 250-1.000 EUR netto (stabil seit 2018; keine Anhebung beschlossen, Stand 2026).

### Standards

- BMF AfA-Tabellen (massgeblich: BMF-Schreiben vom 15.12.2000, BStBl 2000 I S. 1532 für allgemein verwendbare Anlagegueter; branchenspezifische Tabellen abrufbar unter bundesfinanzministerium.de).
- IDW PS 480.
- DATEV/Addison Anlagenbuchhaltungs-Module.

## Workflow

### Phase 1 — Hauptbuch-Bestaende

Anlagenkonten SKR 03 (Kontennummern typische Beispiele; konkrete Nummern mit aktueller DATEV-Kontenrahmenfassung abgleichen):

```
0010 Immaterielle Wirtschaftsgueter
0020 Grundstuecke und Bauten
0080 Maschinen
0440 Geringwertige Wirtschaftsgueter
0500 Fuhrpark
0670 Betriebs- und Geschaeftsausstattung
0900 Anzahlungen auf Anlagen
1000 Beteiligungen
```

### Phase 2 — Anlagenspiegel-Auswertung

```
ANLAGENSPIEGEL (Auszug)
Bezeichnung Anschaffung Bisherige AfA Buchwert Anfang Zugang Abgang AfA Periode Buchwert Ende
Maschine A 50.000 30.000 20.000 — — 2.500 17.500
Pkw Mazda 25.000 8.000 17.000 — — 2.083 14.917
GWG-Pool 2026 1.200 — — 1.200 — 240 960
Buero-Ausstattung 15.000 6.000 9.000 — — 1.500 7.500
```

### Phase 3 — Abstimmung Hauptbuch / Anlagenspiegel

- Saldo Hauptbuch Anlagekonten zum Stichtag = Summe Buchwerte Anlagenspiegel?
- Differenz = Fehler.
- AfA-Buchung im Hauptbuch (Konto 4830/4832) = Summe AfA Anlagenspiegel?

### Phase 4 — Zu- und Abgaenge

- Zugang: Anschaffung neu, Aktivierung Eigenleistung, Einlage.
- Abgang: Verkauf, Verschrottung, Entnahme.
- Bei Anlagenabgang: Restbuchwert ausbuchen, Verkaufserloes gegenrechnen.
- Veraeusserungserloese im SKR 03: Konten im 8400er-Bereich (Erloese aus Anlagenverkauf); konkrete Kontonummer je nach Umsatzsteuerpflicht in DATEV-Kontenrahmen SKR 03 nachschlagen (DATEV-Handbuch oder Kontenrahmen-PDF unter datev.de).

### Phase 5 — Sonder-AfA und § 6b EStG

- § 7g EStG: Sonderabschreibung für KMU bis 40 % (für Anschaffungen ab 01.01.2024), IAB bis 50 %; Gewinngrenze 200.000 EUR im Vorjahr (§ 7g Abs. 6 EStG, stabile Rechtslage seit JStG 2020).
- § 7b EStG: Sonderabschreibung Wohnungsneubau (befristete Förderung; aktuelle Geltungsdauer Stand 2026 pruefen).
- § 6b EStG Ruecklage: bei Veraeusserung Grund und Boden, Gebaeude — Uebertragung auf Reinvestitionen.

### Phase 6 — Reporting

- Anlagenspiegel als Anhang zum Jahresabschluss.
- Monatliche Anlagen-Uebersicht in Quartalsberichten.
- Bei groesseren Investitionen: Beratung zu IAB § 7g EStG.

## Output

- Anlagenspiegel mit Zugaengen, Abgaengen, AfA.
- Hauptbuch-Anlagenspiegel-Abstimmung.
- AfA-Buchungsbeleg für SuSa.

## Strategie und Praxis-Tipps

- Anlagenspiegel und Hauptbuch sollten quartalsweise abgestimmt werden.
- GWG-Pool optional (§ 6 Abs. 2a EStG) — bietet Vereinfachung mit Sammelposten-Abschreibung ueber fuenf Jahre.
- Beim Investitionsabzugsbetrag nach § 7g EStG: Quote 50 Prozent vorab abziehbar, Hoechstbetrag 200.000 EUR; Gewinngrenze 200.000 EUR (stabile Rechtslage seit JStG 2020, § 7g Abs. 1 EStG).
- Sonderabschreibungen § 7b EStG: befristet für Bauantraege nach 31.12.2022 und vor 01.10.2029 (EH-40-Standard Pflicht); aktiv bis 2029.
- StBVV: Anlagenbuchhaltung als separater Auftrag oder in Buchfuehrungspauschale.
- DATEV-Tipp: DATEV-Anlagenbuchhaltung mit automatischer 1/12-AfA-Buchung in der SuSa (Klickpfad: Anlagenbuchfuehrung → Abschreibungsbuchungen → Buchungsstapel an Rechnungswesen uebergeben).

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-jahresabschluss-anlagenverzeichnis-afa` — JA-AfA-Verzeichnis.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 247, 253.
- EStG §§ 6, 7, 7b, 7g.
- BMF AfA-Tabellen.
- IDW PS 480.
- Hinweis: § 7b EStG Förderung laeuft bis Bauantraege vor 01.10.2029; keine gesetzliche Aenderung 2026.
- Hinweis: § 7g EStG Sonder-AfA 40 Prozent und IAB 50 Prozent seit JStG 2020 stabil.

<!-- AUDIT 27.05.2026 | welle 6 | 10 Marker aufgeloest: 8 bestaetigt (§ 7b bis 2029, GWG 800 EUR stabil, Sammelposten 250-1000 EUR stabil, § 7g 40%/50% stabil, BMF AfA-Tabelle AV 15.12.2000), 2 ersetzt (DATEV-Kontonummern-Hinweise ohne Marker neu formuliert) -->

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
