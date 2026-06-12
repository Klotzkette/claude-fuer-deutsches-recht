---
name: lizenz-urheberrecht-und-software-urhg
description: "Urheberrechts- und Software-Lizenzen nach UrhG: $ 31 ff. UrhG einfache und ausschliessliche Nutzungsrechte, $ 32 angemessene Verguetung, $ 32a Bestseller-Klausel, $ 69a-g UrhG Computerprogramme, $ 137l UrhG unbekannte Nutzungsarten. Mit Klauselbausteinen."
---

# Lizenz Urheberrecht / Software ($$ 31 ff. UrhG)

## Normenanker

- $ 31 UrhG - Einraeumung von Nutzungsrechten (einfach vs. ausschließlich)
- $ 31a UhG - Verträge über unbekannte Nutzungsarten
- $ 32 UrhG - angemessene Vergütung (Anspruch des Urhebers)
- $ 32a UrhG - weitere Beteiligung des Urhebers (Bestseller-Klausel; $ 32a Abs. 2 für Dritte)
- $ 35 UrhG - Einraeumung weiterer Nutzungsrechte (Sub-Lizenz)
- $ 40 UrhG - Verträge über kuenftige Werke
- $ 41 UrhG - Rueckrufsrecht wegen Nichtausuebung
- $ 42 UrhG - Rueckrufsrecht wegen gewandelter Ueberzeugung
- $$ 69a-g UrhG - Schutz von Computerprogrammen (Sonderrecht)

## Lizenzformen

| Typ | Definition | Klauselbeispiel |
|---|---|---|
| einfaches Nutzungsrecht | $ 31 Abs. 2 UrhG; nicht-exklusiv | "Der Lizenzgeber raeumt dem Lizenznehmer das einfache Nutzungsrecht ein…" |
| ausschliessliches Nutzungsrecht | $ 31 Abs. 3 UrhG; exklusiv | "ausschliessliches Nutzungsrecht, beschraenkt auf [Territorium/Zeit/Feld]" |
| zeitlich beschraenkt | $ 31 Abs. 1 S. 2 UrhG | Konkrete Laufzeit mit Verlaengerungsklausel |
| raeumlich beschraenkt | $ 31 Abs. 1 S. 2 UrhG | Land/Region/Sprachraum |
| inhaltlich beschraenkt | $ 31 Abs. 1 S. 2 UrhG (Zweckuebertragungstheorie) | Konkrete Nutzungsart benennen |

## Pflichten und Schranken

- **Zweckuebertragungstheorie ($ 31 Abs. 5 UrhG):** Im Zweifel nur die Rechte, die für den Vertragszweck erforderlich sind. → Im Vertrag konkrete Nutzungsarten aufzaehlen.
- **Angemessenheits-Korrektur ($ 32 UrhG):** Urheber hat Anspruch auf nachtraegliche Anpassung der Vergütung; nicht abdingbar (zwingend).
- **Bestsellerparagraf ($ 32a UrhG):** Bei auffaelligem Missverhaeltnis nachtraeglicher Korrekturanspruch; auch gegen Lizenznehmer-Sub-Lizenznehmer in der Kette.

## Software-Spezifika ($$ 69a-g UrhG)

| Norm | Inhalt |
|---|---|
| $ 69a | Schutzfaehigkeit von Computerprogrammen; Ausdrucksform |
| $ 69b | Arbeitsergebnis des Arbeitnehmers - AG erwirbt ausschliessliche Nutzungsrechte kraft Gesetzes |
| $ 69c | Zustimmungsbeduerftige Handlungen (Vervielfaeltigung, Umarbeitung, Verbreitung) |
| $ 69d | Erlaubte Handlungen ohne Zustimmung (bestimmungsgemaesse Benutzung, Sicherheitskopie) |
| $ 69e | Dekompilierung zur Interoperabilitaet |
| $ 69f | Verletzungsfolgen |
| $ 69g | Verhältnis zu sonstigen Vorschriften |

## Source-Code vs. Object-Code

- **Object-Code-Lizenz** (Standard): nur Ausfuehrung, keine Quellcode-Einsicht.
- **Source-Code-Lizenz** (selten direkt): mit Recht zur Bearbeitung; meist nur als Escrow.
- → Bei Software-Abhaengigkeit: Source-Code-Escrow vereinbaren (siehe `escrow-quellcode-verwahrer-vereinbarung`).

## Open-Source-Compliance

Prüfen vor Vertragsschluss:
- Open-Source-Bill-of-Materials (OSS-BOM): welche Komponenten sind im Stack?
- Copyleft-Risiken: GPL, AGPL → Quellcode-Offenlegungspflicht?
- LGPL: dynamisches Linking unproblematisch für Distribution.
- MIT/Apache-2.0: zulaessige Mischung.
- Lizenzkompatibilitaet $ 69c UrhG; bei GPL-Verstoss: Loeschung der OSS-Komponente vor Distribution.

## Klausel-Bausteine (DE)

**1. Lizenzgegenstand:**
> "Der Lizenzgeber raeumt dem Lizenznehmer hiermit das [einfache / ausschliessliche] Nutzungsrecht an der in **Anlage A** bezeichneten Software ("Lizenzgegenstand") für die in **Anlage B** definierten Nutzungsarten ein."

**2. Nutzungsarten:**
> "Die Lizenz umfasst die Vervielfaeltigung im Sinne des $ 69c Nr. 1 UrhG, die bestimmungsgemaesse Benutzung im Sinne des $ 69d Abs. 1 UrhG sowie [Verbreitung / Bearbeitung / oeffentliche Wiedergabe]."

**3. Vergütung:**
> "Die Vergütung betraegt [Pauschale / Running Royalty in Höhe von X % des Nettoumsatzes]. Die Parteien bestaetigen, dass die Vergütung im Sinne des $ 32 UrhG angemessen ist."

## Anschluss

- Source-Code-Escrow: `escrow-quellcode-verwahrer-vereinbarung`
- Verguetungsklausel: `klausel-verguetung-pauschale-royalty-tiered`
- Insolvenz: `insolvenz-fortbestand-paragraf-103-inso-lizenz`
