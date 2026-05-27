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
| Linear (§ 7 Abs. 1 EStG) | Standard nach AfA-Tabelle |
| Degressiv (§ 7 Abs. 2 EStG) | Befristet wiedereingefuehrt (Wachstumschancengesetz 2024: bewegliche WG ab 01.04.2024 - 31.12.2024 mit max. 20 % bzw. 2-fach linear); aktuelle Geltung 2026 ueber BMF / Beck-Online verifizieren |
| Leistungs-AfA (§ 7 Abs. 1 S. 6 EStG) | Bewegliche WG mit messbarer Leistung |
| Sonder-AfA § 7g Abs. 5 EStG | KMU: bis 40 % (durch JStG 2020 fuer Anschaffungen ab 2020 angehoben von 20 %) im Jahr der Anschaffung und den folgenden 4 Jahren — Werte aktuell verifizieren |
| Sonder-AfA § 7b EStG | Mietwohnungsneubau (zeitlich befristete Foerderung; Aufstockung durch Wachstumschancengesetz 2024 — aktuellen Stand verifizieren) |

### Phase 5 — Investitionsabzugsbetrag § 7g EStG

- IAB: bis zu 50 % der voraussichtlichen Anschaffungs- oder Herstellungskosten ausserbilanziell gewinnmindernd vor der Anschaffung; Hoechstbetrag 200.000 EUR im Wirtschaftsjahr (Werte aktuellen Stand pruefen).
- Voraussetzung: einheitliche Gewinngrenze 200.000 EUR (durch das JStG 2020 fuer alle Einkunftsarten); aktuellen Stand fortlaufend pruefen.
- IAB ist ausserbilanzielle Gewinnminderung (keine handelsrechtliche Ruecklage; nur in der steuerlichen Gewinnermittlung).
- Investitionsfrist: bis zum Ende des **dritten** auf das Abzugsjahr **folgenden** Wirtschaftsjahres (§ 7g Abs. 3 S. 1 EStG) — insgesamt also rund 4 Jahre Zeit einschliesslich des Abzugsjahres.
- Aufloesung im Jahr der tatsaechlichen Investition gegen Hinzurechnung; bei Wegfall der Voraussetzungen rueckwirkende Aufloesung mit Anpassung des Veranlagungsjahres und Verzinsung gem. § 233a AO.

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
