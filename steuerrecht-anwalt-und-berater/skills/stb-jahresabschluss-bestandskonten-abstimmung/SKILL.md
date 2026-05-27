---
name: stb-jahresabschluss-bestandskonten-abstimmung
description: "Bestandskonten-Abstimmung zum Jahresabschluss. Anwendungsfall Endbestaende Bank Kasse Forderungen Verbindlichkeiten Anlagen Eigenkapital abstimmen Inventur-Werte einarbeiten. Methodik Saldenabstimmung Vergleich. Output abgestimmte Bestandskonten."
---

# Bestandskonten-Abstimmung zum Jahresabschluss

## Kernsachverhalt

Vor dem JA-Endlauf muessen alle Bestandskonten (Klasse 0-3 SKR 03 bzw. entsprechende SKR-04-Konten) abgestimmt sein: Bank gegen Bankauszug, Kasse gegen Kassenbericht, Forderungen gegen Personenkonten, Anlagen gegen Anlagenspiegel, Eigenkapital gegen Gesellschaftervereinbarungen. Differenzen muessen aufgeklaert werden.

## Kaltstart-Rueckfragen

1. Welche Bestandskonten sind vorhanden?
2. Welche Saldenabstimmungs-Antworten liegen vor?
3. Liegen Bankbestaetigungen vor (Saldenbestaetigung)?
4. Anlagenspiegel mit Hauptbuch abgestimmt?
5. Liegen Inventur-Werte vor?
6. Welche Korrekturen aus der Saldenabstimmung?
7. Welche Sondervorgaenge (Kapitalbewegungen)?
8. Welche Werterhellung nach Stichtag?

## Rechtlicher Rahmen

### Primaernormen

**§ 240 HGB** — Inventarpflicht.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 253 HGB** — Bewertung Vermoegen.

**§ 246 HGB** — Vollstaendigkeit.

**§ 5 EStG** — Massgeblichkeit Handelsbilanz.

### Standards

- IDW PS 480.
- IDW PS 302 (Saldenbestaetigungen).

## Workflow

### Phase 1 — Bestandskonten-Inventur

| Konto | Abstimmungs-Basis |
|---|---|
| Bank | Bankauszuege, Saldenbestaetigung Bank |
| Kasse | Kassenbericht, Z-Bons |
| Forderungen LuL | Debitoren-OPOS, Saldenbestaetigung Kunden |
| Sonstige Forderungen | Einzelnachweis |
| Vorraete | Inventur-Protokoll |
| Anlagen | Anlagenspiegel |
| Verbindlichkeiten LuL | Kreditoren-OPOS, Saldenbestaetigung Lieferanten |
| Bank-Verbindlichkeiten | Darlehensvertraege, Saldenbestaetigung Bank |
| Steuerverbindlichkeiten | FA-Bescheide |
| SV-Verbindlichkeiten | KK-Beitragsabrechnungen |
| Rueckstellungen | Bewertungsgrundlagen |
| Eigenkapital | Gesellschaftervereinbarungen, Vorjahresvortrag |

### Phase 2 — Differenzen klaeren

- Bei Hauptbuch-Nebenbuch-Differenzen: Personenkonto-Pflege.
- Bei Bankabstimmungs-Differenzen: Cut-off-Buchungen.
- Bei Vorraete-Differenzen: Inventur-Pruefung.

### Phase 3 — Anpassungs-Buchungen

- Endgueltige AfA-Buchung.
- Periodenabgrenzungs-Buchungen.
- Rueckstellungs-Buchungen.

### Phase 4 — Werterhellung

- Wesentliche Ereignisse zwischen Stichtag und Aufstellung pruefen.
- Insolvenz-Antraege bei Schuldnern (Forderungsausfall-Risiko).
- Wesentliche Vertragsabschluesse (Auswirkung auf Risiko/Rueckstellung).

### Phase 5 — Bestand-Bewertung

- Forderungen: Einzelwertberichtigung bei zweifelhaften Schuldnern.
- Vorraete: Niederstwertprinzip; Veraltete Bestaende.
- Anlagen: Ausserplanmaessige Abschreibung bei dauerhafter Wertminderung.

### Phase 6 — Endgueltige Bilanz

- Bestandskonten-Endsalden bilden Bilanzposten.
- Endsalden in Bilanz uebernehmen.
- Konsistenzcheck.

## Output

- Abgestimmte Bestandskonten.
- Anpassungs-Buchungen dokumentiert.
- Bilanz vorbereitet.

## Strategie und Praxis-Tipps

- Bestandskonten-Abstimmung ist Pflicht — nicht abgekuerzte Pruefung.
- Bei Pruefungspflicht: WP fordert Abstimmung formell.
- Bei groesseren Mandanten: Saldenabstimmung mit Lieferanten/Kunden Standard.
- Werterhellung-Pruefung kann erhebliche Auswirkungen haben.

## Querverweise

- `stb-susa-saldenabstimmung-bestaetigung` — Saldenabstimmung.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-warenbestand-inventur` — Inventur.
- `stb-jahresabschluss-anlagenverzeichnis-afa` — AfA.
- `stb-jahresabschluss-rueckstellungen-bewertung` — Rueckstellungen.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 246, 252, 253.
- EStG § 5.
- IDW PS 480, IDW PS 302.
