---
name: lizenz-urheberrecht-und-software-urhg
description: "Wenn es um Lizenz Urheberrecht / Software (Paragrafen 31 ff. UrhG) in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

# Lizenz Urheberrecht / Software (Paragrafen 31 ff. UrhG)

## Normenanker

- Paragraf 31 UrhG - Einraeumung von Nutzungsrechten (einfach vs. ausschließlich)
- Paragraf 31a UhG - Verträge über unbekannte Nutzungsarten
- Paragraf 32 UrhG - angemessene Vergütung (Anspruch des Urhebers)
- Paragraf 32a UrhG - weitere Beteiligung des Urhebers (Bestseller-Klausel; Paragraf 32a Abs. 2 für Dritte)
- Paragraf 35 UrhG - Einraeumung weiterer Nutzungsrechte (Sub-Lizenz)
- Paragraf 40 UrhG - Verträge über kuenftige Werke
- Paragraf 41 UrhG - Rueckrufsrecht wegen Nichtausuebung
- Paragraf 42 UrhG - Rueckrufsrecht wegen gewandelter Ueberzeugung
- Paragrafen 69a-g UrhG - Schutz von Computerprogrammen (Sonderrecht)

## Lizenzformen

| Typ | Definition | Klauselbeispiel |
|---|---|---|
| einfaches Nutzungsrecht | Paragraf 31 Abs. 2 UrhG; nicht-exklusiv | "Der Lizenzgeber raeumt dem Lizenznehmer das einfache Nutzungsrecht ein…" |
| ausschliessliches Nutzungsrecht | Paragraf 31 Abs. 3 UrhG; exklusiv | "ausschliessliches Nutzungsrecht, beschraenkt auf [Territorium/Zeit/Feld]" |
| zeitlich beschraenkt | Paragraf 31 Abs. 1 S. 2 UrhG | Konkrete Laufzeit mit Verlaengerungsklausel |
| raeumlich beschraenkt | Paragraf 31 Abs. 1 S. 2 UrhG | Land/Region/Sprachraum |
| inhaltlich beschraenkt | Paragraf 31 Abs. 1 S. 2 UrhG (Zweckuebertragungstheorie) | Konkrete Nutzungsart benennen |

## Pflichten und Schranken

- **Zweckuebertragungstheorie (Paragraf 31 Abs. 5 UrhG):** Im Zweifel nur die Rechte, die für den Vertragszweck erforderlich sind. → Im Vertrag konkrete Nutzungsarten aufzaehlen.
- **Angemessenheits-Korrektur (Paragraf 32 UrhG):** Urheber hat Anspruch auf nachtraegliche Anpassung der Vergütung; nicht abdingbar (zwingend).
- **Weitere Beteiligung (Paragraf 32a UrhG):** Bei auffälligem Missverhältnis besteht ein zwingender Anspruch auf Vertragsanpassung. Hat der ursprüngliche Vertragspartner das Nutzungsrecht übertragen oder weitere Nutzungsrechte eingeräumt und ergibt sich das Missverhältnis aus Erträgen oder Vorteilen eines Dritten, richtet sich der Anspruch nach Absatz 2 unmittelbar gegen diesen Dritten; die Haftung des ursprünglichen Vertragspartners entfällt insoweit. Rechtekette, Erlösstufe und Anspruchsgegner deshalb getrennt feststellen.

## Software-Spezifika (Paragrafen 69a-g UrhG)

| Norm | Inhalt |
|---|---|
| Paragraf 69a | Schutzfaehigkeit von Computerprogrammen; Ausdrucksform |
| Paragraf 69b | Arbeitsergebnis des Arbeitnehmers - AG erwirbt ausschliessliche Nutzungsrechte kraft Gesetzes |
| Paragraf 69c | Zustimmungsbeduerftige Handlungen (Vervielfaeltigung, Umarbeitung, Verbreitung) |
| Paragraf 69d | Erlaubte Handlungen ohne Zustimmung (bestimmungsgemaesse Benutzung, Sicherheitskopie) |
| Paragraf 69e | Dekompilierung zur Interoperabilitaet |
| Paragraf 69f | Verletzungsfolgen |
| Paragraf 69g | Verhältnis zu sonstigen Vorschriften |

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
- Lizenzkompatibilitaet Paragraf 69c UrhG; bei GPL-Verstoss: Loeschung der OSS-Komponente vor Distribution.

## Klausel-Bausteine (DE)

**1. Lizenzgegenstand:**
> "Der Lizenzgeber raeumt dem Lizenznehmer hiermit das [einfache / ausschliessliche] Nutzungsrecht an der in **Anlage A** bezeichneten Software ("Lizenzgegenstand") für die in **Anlage B** definierten Nutzungsarten ein."

**2. Nutzungsarten:**
> "Die Lizenz umfasst die Vervielfaeltigung im Sinne des Paragraf 69c Nr. 1 UrhG, die bestimmungsgemaesse Benutzung im Sinne des Paragraf 69d Abs. 1 UrhG sowie [Verbreitung / Bearbeitung / oeffentliche Wiedergabe]."

**3. Vergütung:**
> "Die Vergütung betraegt [Pauschale / Running Royalty in Höhe von X % des Nettoumsatzes]. Die Parteien bestaetigen, dass die Vergütung im Sinne des Paragraf 32 UrhG angemessen ist."

## Anschluss

- Source-Code-Escrow: `escrow-quellcode-verwahrer-vereinbarung`
- Verguetungsklausel: `klausel-verguetung-pauschale-royalty-tiered`
- Insolvenz: `insolvenz-fortbestand-paragraf-103-inso-lizenz`
