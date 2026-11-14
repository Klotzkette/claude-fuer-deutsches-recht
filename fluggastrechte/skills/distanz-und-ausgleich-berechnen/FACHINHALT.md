---
name: distanz-und-ausgleich-berechnen
description: "Für Distanz und Ausgleichszahlung berechnen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Distanz und Ausgleichszahlung berechnen

## Norm

Art. 7 VO 261/2004 — Ausgleichsanspruch in drei Stufen:

| Stufe | Distanz | Höhe pro Passagier |
|---|---|---|
| 1 | bis 1500 km | 250 EUR |
| 2 | mehr als 1500 km innergemeinschaftlich | 400 EUR |
| 2 | 1500 bis 3500 km nicht-innergemeinschaftlich | 400 EUR |
| 3 | mehr als 3500 km nicht-innergemeinschaftlich | 600 EUR |

## Distanzberechnung

- **Großkreisrechnung** (Great Circle Distance) zwischen Abflug- und Zielflughafen.
- IATA-Standardkoordinaten der Flughaefen.
- Anschlussflug über Drittstaat als Umweg zählt nicht (Direktverbindungs-Maßstab).

## Begriff innergemeinschaftlich vs nicht-innergemeinschaftlich

- **Innergemeinschaftlich** Flug zwischen zwei Flughaefen die in der EU liegen.
- **Nicht-innergemeinschaftlich** mindestens ein Flughafen außerhalb der EU.
- **Sondergebiete** Kanaren Madeira Azoren EU-Außengebiete EU-Recht gilt (innergemeinschaftlich).
- **Norwegen Schweiz Island Liechtenstein** mehrere bilaterale Abkommen — beachten ob VO 261/2004 anwendbar.

## Beispielberechnungen

- **Berlin (BER) — Madrid (MAD)** ca. 1872 km innergemeinschaftlich → Stufe 2 → 400 EUR
- **München (MUC) — Lissabon (LIS)** ca. 2280 km innergemeinschaftlich → Stufe 2 → 400 EUR
- **Frankfurt (FRA) — Mallorca (PMI)** ca. 1245 km innergemeinschaftlich → Stufe 1 → 250 EUR
- **Hamburg (HAM) — New York (JFK)** ca. 6125 km nicht-innergemeinschaftlich → Stufe 3 → 600 EUR
- **Wien (VIE) — Dubai (DXB)** ca. 4275 km nicht-innergemeinschaftlich → Stufe 3 → 600 EUR

## Halbierungsregel (Art. 7 Abs. 2 VO 261/2004)

Die Airline kann den Ausgleich **um 50 Prozent kuerzen** wenn dem Fluggast eine **anderweitige Beförderung** angeboten wurde **und** die tatsächliche Ankunftszeit am Endziel nicht überschreitet:

- Bei Distanz **bis 1500 km** die geplante Ankunftszeit um **mehr als zwei Stunden**.
- Bei Distanz **1500 bis 3500 km nicht-innergemeinschaftlich oder über 1500 km innergemeinschaftlich** die geplante Ankunftszeit um **mehr als drei Stunden**.
- Bei Distanz **mehr als 3500 km nicht-innergemeinschaftlich** die geplante Ankunftszeit um **mehr als vier Stunden**.

Folge: Stufe 1 → 125 EUR; Stufe 2 → 200 EUR; Stufe 3 → 300 EUR.

## Mehrere Passagiere

- **Eigenständiger Anspruch pro Passagier** (Art. 7 VO 261/2004 ist persönlich).
- **Auch Kinder** mit eigener Beförderung (eigenes Ticket) haben den vollen Anspruch — auch bei Kindertarif.
- **Babys ohne eigenen Sitzplatz** (Lap-Infant) haben i. d. R. keinen eigenen Ausgleichsanspruch wenn nicht gesondert befoerdert.

## Nebenforderungen

- **Verzugszinsen** ab Mahnung (§§ 286 288 BGB) — Verbraucher 5 Prozentpunkte über Basiszinssatz.
- **Auslagen** wenn Verbraucher selbst Auslagen getragen hat (Hotel Verpflegung Telefon) bei verletzter Betreuungspflicht (Art. 9 VO 261/2004) — separat zur Ausgleichszahlung.

## Pauschalreise

- Bei Pauschalreise greifen zusätzliche Ansprueche gegen den Reiseveranstalter nach §§ 651a ff. BGB.

## Ausgabe

```
Berechnung Ausgleich
Fall-ID: FG-2026-0042
Flug: LH 1234 MUC-LIS
Distanz: 2280 km (innergemeinschaftlich)
Stufe: 2 (mehr als 1500 km innergemeinschaftlich)
Ausgleich pro Passagier: 400 EUR
Anzahl Passagiere: 3
Gesamtausgleich: 1200 EUR

Halbierungsregel prüfen:
- Ersatzflug am 13.05.2026 LH 1234
- Tatsächliche Ankunft 13.05.2026 12:00 statt geplant 12.05.2026 11:00
- Verspätung: 25 Stunden über drei Stunden → keine Halbierung
- → 1200 EUR Anspruch in voller Hoehe
```

## Hinweise

- Beweislast für Distanzangaben liegt nicht beim Fluggast (Standard-Flugplandaten frei zugänglich).
- Bei strittiger Distanz: Gericht stellt anhand IATA-Daten fest.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
