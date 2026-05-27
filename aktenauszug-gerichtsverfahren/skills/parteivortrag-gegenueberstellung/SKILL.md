---
name: parteivortrag-gegenueberstellung
description: "Erstellt eine Tabelle mit zwei Spalten (Klaegerseite und Beklagtenseite) fuer streitige Sachverhaltsangaben Punkt fuer Punkt. Jeder Streitpunkt wird als eigene Zeile gegenuebergestellt. Fundstellen in Schriftsaetzen werden angegeben. Keine Wertung welcher Vortrag zutreffend ist. Massstab §§ 138 286 ZPO."
---

# Parteivortrag — Gegenüberstellung

## Zweck

Die Parteivortrag-Tabelle stellt streitige Sachverhaltsangaben der Kläger- und der Beklagtenseite Punkt für Punkt gegenüber. Sie ermöglicht dem Anwalt, auf einen Blick zu erkennen, was tatsächlich streitig ist und was als unstreitig gilt.

## Triage — kläre vor Erstellung

1. Liegt bereits ein gerichtlicher Hinweis vor, was das Gericht für streitig und entscheidungserheblich hält?
2. Hat das Gericht einen Beweisbeschluss erlassen? (Streitpunkte sind dann für Gericht bereits benannt)
3. Welche Schriftsätze liegen vor? Klageerwiderung, Replik, Duplik?
4. Gibt es Präklusionsrisiken (§§ 296, 531 ZPO) durch verspäteten Vortrag?

## Zentrale Normen

- § 138 ZPO — Erklärungspflicht über Tatsachen des Gegners (Wahrheitspflicht, substantiiertes Bestreiten)
- § 286 ZPO — Freie Beweiswürdigung; Grundlage für Identifikation der streitigen Punkte
- § 296 Abs. 1 ZPO — Präklusion verspäteten Vortrags in erster Instanz
- § 531 Abs. 2 ZPO — Beschränktes Vorbringen neuer Angriffs- und Verteidigungsmittel in der Berufungsinstanz
- § 139 ZPO — Richterliche Hinweispflicht; Gericht weist auf Lücken im Vortrag hin

## Rechtsprechung zum Parteivortrag und Bestreiten

- BGH, Urt. v. 04.07.2017 - XI ZR 233/16, NJW 2017, 3376 — Unsubstantiiertes Bestreiten genügt nicht; eine Partei muss auf spezifischen Vortrag des Gegners konkret eingehen (§ 138 Abs. 2 ZPO).
- BGH, Urt. v. 12.07.2016 - II ZR 153/15, NJW 2016, 3237 — Einfaches Bestreiten mit Nichtwissen (§ 138 Abs. 4 ZPO) nur bei eigenen Handlungen unzulässig; bei Handlungen Dritter unter Voraussetzungen möglich.
- BGH, Urt. v. 23.04.2015 - VII ZR 131/13, NJW 2015, 2111 — Zur Darlegungs- und Beweislastverteilung beim Werkvertrag: Besteller muss Mangel darlegen und beweisen; Unternehmer hat Mangelfreiheit nicht positiv zu beweisen.
- BGH, Urt. v. 29.01.2019 - XI ZR 265/17, NJW 2019, 1375 — Zum Bestreiten mit Nichtwissen nach § 138 Abs. 4 ZPO: auch für juristische Personen bei Vorgängen im eigenen Organisationsbereich unzulässig.

## Kommentarliteratur

- Zöller/Greger ZPO, § 138 Rn. 1 ff. (Erklärungspflicht und Bestreiten)
- MüKo ZPO/Fritsche, § 286 Rn. 1 ff. (Freie Beweiswürdigung)
- Thomas/Putzo ZPO, § 139 Rn. 1 ff. (Richterliche Prozessleitung)

## Tabellenstruktur

```markdown
| Streitpunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| [Bezeichnung des Streitpunkts] | [Vortrag Kläger] | [Vortrag Beklagter] |
```

## Kategorien von Streitpunkten

- Vertragsinhalt (Leistungsumfang, Preis, Nebenabreden)
- Tatsächliche Leistungserbringung (wer hat was wann geliefert / erbracht)
- Mängel (ob Mangel vorliegt, wessen Ursache)
- Kenntnis und Verschulden
- Schaden und Schadenshöhe
- Vorgerichtliche Kommunikation (wer hat was gesagt)
- Fristen und Termine (Vereinbartes Lieferdatum etc.)

## Beispiel

| Streitpunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| Leistungsumfang | Auftrag umfasste vollständige Schlüsselübergabe inkl. Einweisung (K 1 Bl. 12) | Einweisung war nicht vereinbart sondern nur Lieferung (B 1 Bl. 40) |
| Mangel Dach | Dach war bei Abnahme undicht nachweislich Wassereintritt im Oktober (K 4 Bl. 26) | Undichtigkeit erst durch unsachgemäße Nutzung entstanden (B 3 Bl. 50) |
| Verschulden | Beklagte kannte Mangel und schwieg (K 5 Bl. 29) | Kein Arglistvorwurf; Mangel war nicht erkennbar (B 4 Bl. 53) |
| Schadenshöhe | Schaden EUR 45.000 belegt durch Gutachten (K 8 Bl. 60) | Überhöhte Schadensberechnung; tatsächlicher Schaden unter EUR 15.000 (B 6 Bl. 65) |

## Unstreitige Punkte

Unstreitige Sachverhaltselemente werden unterhalb der Tabelle als Block „Unstreitiger Sachverhalt" aufgeführt. Sie fließen nicht in die Streitpunkt-Tabelle ein.

## Hinweise

- Pro Zeile genau ein Streitpunkt — nicht mehrere Punkte in einer Zelle
- Vortrag neutral wiedergeben (paraphrasieren, nicht werten)
- Fundstelle in Schriftsatz oder Anlage angeben
- Wenn eine Partei zu einem Punkt schweigt: „Kein Vortrag" in die entsprechende Zelle
- Keine Prognose welcher Vortrag zutrifft

## Qualitätscheck

- [ ] Alle wesentlichen Streitpunkte erfasst?
- [ ] Keine Wertung enthalten?
- [ ] Fundstellen angegeben?
- [ ] Unstreitiger Sachverhalt separat ausgewiesen?
- [ ] Präkludierte Punkte (§§ 296 531 ZPO) als solche markiert?
