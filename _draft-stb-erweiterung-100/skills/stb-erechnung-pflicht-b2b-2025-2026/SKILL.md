---
name: stb-erechnung-pflicht-b2b-2025-2026
description: "eRechnung-Pflicht B2B seit 01.01.2025 § 14 UStG ViDA. Anwendungsfall Pruefung Mandantenbetrieb eRechnungs-Empfang Versand Uebergangsfristen PDF reicht nicht mehr. Methodik Format XRechnung ZUGFeRD. Output eRechnungs-Konfiguration."
---

# eRechnung-Pflicht B2B seit 01.01.2025

## Kernsachverhalt

Seit 01.01.2025 ist die eRechnung (elektronische Rechnung in strukturierter Form) im B2B-Bereich Pflicht. Grundlage: § 14 UStG i.V.m. ViDA (VAT in the Digital Age) und Wachstumschancengesetz 2024. PDF-Rechnungen reichen nicht mehr aus. Akzeptierte Formate: XRechnung (XML) und ZUGFeRD (Hybrid). Uebergangsfristen fuer den Versand bis 31.12.2027 (bei kleineren Umsaetzen). Der Steuerberater muss Mandanten ueber die Pflicht informieren und Konfigurationen anpassen.

## Kaltstart-Rueckfragen

1. Welche Umsatzgroesse hat der Mandant (Uebergangsfristen)?
2. Welche Kunden — B2B (eRechnung-pflichtig) oder B2C (PDF weiterhin moeglich)?
3. Welche Lieferanten senden bereits eRechnungen?
4. Welche ERP/Faktura-Software wird genutzt?
5. Welche Empfangs-Adresse (Mail-Postfach oder Peppol)?
6. Welche Archivierung GoBD-konform?
7. Welche Format-Praeferenz XRechnung vs. ZUGFeRD?
8. Welche Mandanten-Beratungsbedarf?

## Rechtlicher Rahmen

### Primaernormen

**§ 14 UStG** — Rechnungspflichten.

**§ 14 Abs. 4a UStG** — eRechnung-Definition.

**§ 14 Abs. 2 UStG** — Ausstellungspflicht.

**Wachstumschancengesetz 2024** — Einfuehrung.

**EU-RL 2014/55** — eRechnung-Standard.

### Verwaltungsanweisungen

- BMF v. 15.10.2024 zur eRechnung-Pflicht.
- BMF v. 22.06.2023 ViDA.

## Workflow

### Phase 1 — Geltungsbereich

| Phase | Zeitraum | Pflicht |
|---|---|---|
| Empfang | Ab 01.01.2025 | Alle Unternehmer im B2B (zwingende Empfangsbereitschaft) |
| Versand | Ab 01.01.2025 | Grosse Unternehmen (Umsatz > 800.000 EUR Vorjahr) |
| Versand kleine Unternehmen | Ab 01.01.2027 | Schwellenwert je nach Reform-Verlauf; aktuell verifizieren |
| Versand alle | Ab 01.01.2028 | Verbindlich; PDF nicht mehr akzeptiert |

(Schwellenwerte und Daten 2026 verifizieren.)

### Phase 2 — Format-Wahl

| Format | Eigenschaften |
|---|---|
| XRechnung | Reines XML, von Bund vorgegebener Standard |
| ZUGFeRD | Hybrid PDF + XML-Anhang; Mensch und Maschine lesbar |
| Sonstige (z.B. EDIFACT) | Branchen-spezifisch; nach Vereinbarung |

ZUGFeRD ab Version 2.2 ist gleichberechtigt mit XRechnung.

### Phase 3 — Empfangs-Setup

- Mailpostfach fuer eRechnung definieren.
- Peppol-Anschluss (selten in DACH; wachsend).
- DATEV Empfang ueber DUO oder externes Tool (z.B. Inposia, Coupa).

### Phase 4 — Versand-Setup

- Faktura-Software mit eRechnung-Ausgabe.
- Datenmapping (Konten zu eRechnung-Feldern).
- Test-Rechnungen mit Lieferanten/Kunden.

### Phase 5 — Archivierung

- GoBD-konforme Archivierung im Originalformat XML.
- 10 Jahre Aufbewahrung.
- Lesbarkeitserhaltung.

### Phase 6 — Mandanten-Information

- Rundbrief an alle Mandanten ueber Pflicht.
- Konfigurationsberatung.
- ggf. Software-Empfehlung.

## Output

- Konfiguration Empfang/Versand eRechnung.
- Archivierungs-Routine.
- Mandanten-Information.

## Strategie und Praxis-Tipps

- eRechnung-Pflicht ist Reform-Hebel — Mandanten frueh informieren.
- Empfang ab 01.01.2025 zwingend — wer nicht empfangsbereit ist, kann eRechnung nicht abrechnen.
- ZUGFeRD ist Standard fuer Mittelstand (PDF + XML; auch Auge-freundlich).
- XRechnung ist Pflicht fuer oeffentliche Auftraggeber (Bund seit 2020).
- DATEV-Tipp: DATEV DUO + DATEV-Faktura unterstuetzen eRechnung; Update zwingend.
- StBVV: Konfigurationsberatung als Sonderauftrag.

## Querverweise

- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.

## Quellen und Updates

Stand: 05/2026.

- UStG § 14.
- Wachstumschancengesetz 2024.
- BMF v. 15.10.2024.
- BMF v. 22.06.2023 ViDA.
- EU-RL 2014/55.
- Verifikations-Hinweis: Schwellenwerte und Uebergangsfristen 2026 verifizieren.
