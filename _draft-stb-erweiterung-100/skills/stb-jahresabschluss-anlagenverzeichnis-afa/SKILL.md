---
name: stb-jahresabschluss-anlagenverzeichnis-afa
description: "Anlagenverzeichnis und AfA-Buchung Jahresabschluss. Anwendungsfall vollstaendige Aktualisierung Anlagen Zugaenge Abgaenge AfA-Methoden Sonderabschreibung 7g 7b 6b EStG. Methodik AfA-Tabellen. Output Anlagenspiegel."
---

# Anlagenverzeichnis und AfA — Jahresabschluss-Aktualisierung

## Kernsachverhalt

Der Anlagenspiegel (Anlagenverzeichnis) bildet die Bestandsentwicklung des Anlagevermoegens ueber das Geschaeftsjahr ab: Anfangsbestand, Zugaenge, Abgaenge, Abschreibungen, Zuschreibungen, Endbestand. Im Jahresabschluss ist er Pflicht-Bestandteil bei mittelgrossen und grossen Kapitalgesellschaften (§ 268 Abs. 2 HGB).

## Kaltstart-Rueckfragen

1. Welche Anlagengruppen sind vorhanden (immaterielle WG, Sachanlagen, Finanzanlagen)?
2. Welche Zugaenge im Jahr (Investitionen)?
3. Welche Abgaenge (Verkauf, Verschrottung, Entnahme)?
4. Welche AfA-Methode (linear, degressiv, Leistungs-AfA)?
5. Sonderabschreibungen § 7g, § 7b, § 6b EStG?
6. Welche Nutzungsdauern laut AfA-Tabelle?
7. Welche Investitionsabzugsbetraege § 7g EStG anstehend?
8. Welche GWG-Konfiguration (Wahlrecht 800 EUR oder Pool 1.000 EUR)?

## Rechtlicher Rahmen

### Primaernormen

**§ 247 HGB** — Anlagevermoegen-Definition.

**§ 253 HGB** — Bewertung mit fortgefuehrten Anschaffungs-/Herstellungskosten.

**§ 268 Abs. 2 HGB** — Anlagenspiegel-Pflicht.

**§ 6 EStG** — Bewertung.

**§ 7 EStG** — AfA-Methoden.

**§ 7g EStG** — IAB und Sonderabschreibung.

**§ 7b EStG** — Sonderabschreibung Wohnungsbau (befristet).

**§ 6 Abs. 2 EStG** — GWG bis 800 EUR.

**§ 6 Abs. 2a EStG** — Pool-Abschreibung 250-1.000 EUR.

### Verwaltungsanweisungen

- BMF AfA-Tabellen.
- BMF v. 19.04.2007 zu § 7g EStG (verifizieren).

## Workflow

### Phase 1 — Anlagenspiegel-Struktur

```
ANLAGENSPIEGEL [Geschaeftsjahr]
Position           | AHK Anfang | Zugang | Abgang | Umgliederung | Endbestand AHK | Kum. AfA Anfang | AfA des Jahres | Abgang AfA | Kum. AfA Ende | Buchwert Anfang | Buchwert Ende
Immaterielle WG    | [X]        | [Y]    | [Z]    | -            | [A]            | [B]             | [C]            | [Z]        | [D]           | [E]             | [F]
Sachanlagen        | ...
Finanzanlagen      | ...
```

### Phase 2 — Zugaenge

- Anschaffungskosten (incl. Anschaffungsnebenkosten).
- Herstellungskosten (Eigenbau).
- Aktivierungswahlrechte fuer immaterielle WG.

### Phase 3 — Abgaenge

- Verkauf: Buchwert ausbuchen, Erloes gegenrechnen.
- Verschrottung: voll abschreiben.
- Entnahme (Personenges): Privatanteil.

### Phase 4 — AfA-Methoden

| Methode | Anwendung |
|---|---|
| Linear | Standard nach AfA-Tabelle |
| Degressiv | Befristet wiedereingefuehrt; aktuelle Geltung 2026 verifizieren |
| Leistungs-AfA | Maschinen mit messbarer Leistung |
| Sonder-AfA § 7g EStG | KMU bis 50 Prozent erste 5 Jahre |
| Sonder-AfA § 7b EStG | Wohnungsneubau (befristet) |

### Phase 5 — Investitionsabzugsbetrag § 7g EStG

- Vorab 50 Prozent von den Anschaffungskosten als IAB.
- Voraussetzung: KMU-Schwellen (Gewinn vor IAB unter 200.000 EUR; aktuell verifizieren).
- Ruecklage im Eigenkapital.
- Aufloesung mit tatsaechlicher Anschaffung binnen 3 Jahren.

### Phase 6 — GWG

- Sofortabschreibung bis 800 EUR netto.
- Pool-Abschreibung 250-1.000 EUR (5 Jahre).
- Wahlrecht im Wirtschaftsjahr einheitlich.

## Output

- Anlagenspiegel als Bestandteil JA.
- AfA-Buchung im Hauptbuch.
- IAB-Dokumentation.

## Strategie und Praxis-Tipps

- Anlagenspiegel ist Pflicht bei mittelgrossen/grossen Kapitalgesellschaften (§ 288 HGB).
- AfA-Tabellen sind nicht zwingend (BMF-Tabellen sind Verwaltungsanweisung, aber praktisch verbindlich).
- IAB § 7g EStG: gestaltungsstark, aber 3-Jahres-Frist beachten.
- GWG-Wahlrecht jaehrlich, aber einheitlich im Wirtschaftsjahr.

## Querverweise

- `stb-susa-anlagenkonten-ueberblick` — Anlagen in SuSa.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 247, 253, 268, 288.
- EStG §§ 5, 6, 7, 7b, 7g.
- BMF AfA-Tabellen.
- Verifikations-Hinweis: degressive AfA-Geltung 2026 verifizieren.
- Verifikations-Hinweis: § 7g EStG Schwellenwerte 2026 verifizieren.
