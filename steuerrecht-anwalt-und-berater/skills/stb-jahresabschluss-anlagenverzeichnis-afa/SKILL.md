---
name: stb-jahresabschluss-anlagenverzeichnis-afa
description: "Anlagenverzeichnis und AfA-Buchung Jahresabschluss. Anwendungsfall vollständige Aktualisierung Anlagen Zugaenge Abgaenge AfA-Methoden Sonderabschreibung 7g 7b 6b EStG. Methodik AfA-Tabellen. Output Anlagenspiegel."
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
- § 7g EStG in der Fassung des JStG 2020 (massgeblich ab 01.01.2020; Sonder-AfA 40 Prozent, IAB 50 Prozent); aktuelle Gesetzesfassung auf gesetze-im-internet.de.

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
| Degressiv (§ 7 Abs. 2 EStG) | Wachstumschancengesetz 2024: bewegliche WG 01.04.2024-31.12.2024 max. 20 %, 2-fach linear. Ab 01.07.2025 (Investitionsbooster): bewegliche WG max. 30 %, 3-fach linear, befristet bis 31.12.2027 (Koalitionsvertrag 2025). Fuer neue Zugaenge 2026: 30 %-Regel pruefen. |
| Leistungs-AfA (§ 7 Abs. 1 S. 6 EStG) | Bewegliche WG mit messbarer Leistung |
| Sonder-AfA § 7g Abs. 5 EStG | KMU: bis 40 % der AHK (fuer Anschaffungen ab 01.01.2024; fuer Anschaffungen vor 01.01.2024: 20 %; JStG 2020), frei verteilbar auf Anschaffungsjahr und 4 Folgejahre; Gewinngrenze 200.000 EUR im Vorjahr (§ 7g Abs. 6 EStG) |
| Sonder-AfA § 7b EStG | Mietwohnungsneubau: 5 % p.a. fuer 4 Jahre; Bauantrag nach 31.12.2022 und vor 01.10.2029; EH-40-Standard mit QNG-Siegel; Baukostengrenze 5.200 EUR/m²; Foerderhoechstgrenze 4.000 EUR/m² (Stand: Wachstumschancengesetz 2024, BGBl. 2024 I Nr. 108) |

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
- Hinweis: degressive AfA 2026 nach § 7 Abs. 2 EStG: Investitionsbooster ab 01.07.2025 (max. 30 %, 3-fach linear, bis 31.12.2027) gilt fuer neue Zugaenge. Fuer Zugaenge 01.04.2024-31.12.2024: max. 20 %, 2-fach linear.
- Hinweis: § 7g EStG Sonder-AfA 40 Prozent und IAB 50 Prozent stabil seit JStG 2020 (fuer Anschaffungen ab 01.01.2024); Gewinngrenze 200.000 EUR.

<!-- AUDIT 27.05.2026 | welle 6 | 6 Marker aufgeloest: 5 bestaetigt (degressive AfA 2024/2026, § 7g 40%, § 7b bis 2029 recherchiert), 1 ersetzt (BMF 2007 obsolet, durch aktuelle Gesetzeslage ersetzt) -->
