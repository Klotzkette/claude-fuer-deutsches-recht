---
name: jahresabschluss-bestandskonten-abstimmung
description: "Bestandskonten-Abstimmung zum Jahresabschluss. Anwendungsfall Endbestaende Bank Kasse Forderungen Verbindlichkeiten Anlagen Eigenkapital abstimmen Inventur-Werte einarbeiten. Methodik Saldenabstimmung Vergleich. Output abgestimmte Bestandskonten."
---

# Bestandskonten-Abstimmung zum Jahresabschluss

## Fachlicher Anker

- **Normen:** § 6a, § 240 HGB, § 252 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Vor dem JA-Endlauf müssen alle Bestandskonten (Klasse 0-3 SKR 03 bzw. entsprechende SKR-04-Konten) abgestimmt sein: Bank gegen Bankauszug, Kasse gegen Kassenbericht, Forderungen gegen Personenkonten, Anlagen gegen Anlagenspiegel, Eigenkapital gegen Gesellschaftervereinbarungen. Differenzen müssen aufgeklaert werden.

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

**§ 253 HGB** — Bewertung Vermögen.

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

### Phase 2 — Differenzen klären

- Bei Hauptbuch-Nebenbuch-Differenzen: Personenkonto-Pflege.
- Bei Bankabstimmungs-Differenzen: Cut-off-Buchungen.
- Bei Vorraete-Differenzen: Inventur-Prüfung.

### Phase 3 — Anpassungs-Buchungen

- Endgueltige AfA-Buchung.
- Periodenabgrenzungs-Buchungen.
- Rueckstellungs-Buchungen.

### Phase 4 — Werterhellung

- Wesentliche Ereignisse zwischen Stichtag und Aufstellung prüfen.
- Insolvenz-Antraege bei Schuldnern (Forderungsausfall-Risiko).
- Wesentliche Vertragsabschluesse (Auswirkung auf Risiko/Rueckstellung).

### Phase 5 — Bestand-Bewertung

- Forderungen: Einzelwertberichtigung bei zweifelhaften Schuldnern.
- Vorraete: Niederstwertprinzip; Veraltete Bestaende.
- Anlagen: Ausserplanmäßige Abschreibung bei dauerhafter Wertminderung.

### Phase 6 — Endgueltige Bilanz

- Bestandskonten-Endsalden bilden Bilanzposten.
- Endsalden in Bilanz uebernehmen.
- Konsistenzcheck.

## Strategie und Praxis-Tipps

- Bestandskonten-Abstimmung ist Pflicht — nicht abgekuerzte Prüfung.
- Bei Prüfungspflicht: WP fordert Abstimmung formell.
- Bei groesseren Mandanten: Saldenabstimmung mit Lieferanten/Kunden Standard.
- Werterhellung-Prüfung kann erhebliche Auswirkungen haben.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 246, 252, 253.
- EStG § 5.
- IDW PS 480, IDW PS 302.
