---
name: klausel-verguetung-pauschale-royalty-tiered
description: "Für Klausel Vergütung — Pauschale, Royalty, Tiered: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Klausel Vergütung — Pauschale, Royalty, Tiered

## Verguetungsformen

| Form | Mechanik | Wann sinnvoll |
|---|---|---|
| **Pauschale (Lump Sum)** | einmaliger Betrag | Markenrecht ohne Nutzungsabhaengigkeit, hochpreisige One-Off-Deals |
| **Running Royalty pro Stueck** | Royalty pro verkauftem Produkt | Patent, Gebrauchsmuster bei klar messbarem Stueck |
| **Running Royalty in % vom Umsatz** | X % vom Nettoumsatz | Software-SaaS, Marke |
| **Tiered Royalty** | sinkende Royalty bei steigendem Umsatz (z. B. 8 % bis 10 Mio, 5 % darueber) | Anreiz für Volumenwachstum |
| **Mindestlizenz** | Untergrenze pro Periode | Ausschliessliche Lizenz mit Anreiz auf aktive Nutzung |
| **Upfront + Running** | Initialzahlung + laufende Royalty | Patent mit Risikoteilung |
| **Milestones** | Zahlung an bestimmte Erfolge gebunden | Pharma, Forschungs-Lizenz |

## Klausel-Bausteine

**A. Pauschale:**
> "Paragraf 5 Vergütung. Der Lizenznehmer zahlt eine einmalige Lizenzgebuehr in Höhe von [Betrag] EUR zzgl. gesetzlicher Umsatzsteuer, faellig binnen 30 Tagen nach Vertragsunterzeichnung auf das Konto des Lizenzgebers."

**B. Running Royalty:**
> "Der Lizenznehmer zahlt eine Running Royalty in Höhe von [X] Prozent des Nettoumsatzes mit Lizenzprodukten. 'Nettoumsatz' bezeichnet die mit den Lizenzprodukten erzielten Brutto-Erloese abzueglich Rabatte, Boni, Skonti, Umsatzsteuer, Versand- und Versicherungskosten. Die Royalty wird kalenderquartalsweise berechnet und ist binnen 30 Tagen nach Quartalsende faellig."

**C. Tiered:**
> "Die Royalty wird in Stufen wie folgt berechnet:
> - bis Jahresumsatz EUR 10 Mio.: 8 %
> - über EUR 10 Mio. bis EUR 50 Mio.: 5 %
> - über EUR 50 Mio.: 3 %
> Die Berechnung erfolgt jaehrlich; Stufenwechsel wirkt für den ueberlaufenden Anteil."

**D. Mindestlizenz:**
> "Unabhaengig vom tatsaechlichen Umsatz zahlt der Lizenznehmer eine Mindestlizenzgebuehr von [Betrag] EUR pro Kalenderjahr. Die Mindestlizenzgebuehr wird auf die in dem jeweiligen Kalenderjahr auflaufenden Running Royalties angerechnet."

**E. Milestones:**
> "Zusaetzlich zur Running Royalty zahlt der Lizenznehmer Milestone-Zahlungen wie folgt:
> - Milestone 1 (Markteinfuehrung): [Betrag]
> - Milestone 2 (Erstes Jahr mit Umsatz > [X]): [Betrag]
> - Milestone 3 (Kumulierter Umsatz > [Y]): [Betrag]"

## Rechen-Beispiel Tiered Royalty

Jahresumsatz 30 Mio. EUR mit Tieredmodell oben:
- Tier 1: 10 Mio × 8 % = 800.000 EUR
- Tier 2: 20 Mio × 5 % = 1.000.000 EUR
- Summe: 1.800.000 EUR Royalty

## Bezugsgroesse "Nettoumsatz" — Definitionsstreit

Wesentliche Streitpunkte:
- Rabatte (Listenpreis vs. Netto)
- Konzerninterne Lieferungen (Transfer Pricing)
- Bundles (Royalty-Stripping)
- Garantieleistungen
→ Vertrag muss "Nettoumsatz" praezise definieren.

## Quellensteuer

Royalties haben Quellensteuer (DE: 15 % nach Paragraf 49 EStG); bei DBA-Anwendung oft Reduktion auf 0/5/10 %. → Skill `steuern-quellensteuer-und-dba-lizenz`.

## Anschluss

- Mindestlizenzen + Audit: `klausel-mindestlizenzen-meldungen-audit`
- Steuern: `steuern-quellensteuer-und-dba-lizenz`
