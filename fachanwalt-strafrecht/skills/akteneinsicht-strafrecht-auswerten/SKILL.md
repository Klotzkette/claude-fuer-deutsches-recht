---
name: akteneinsicht-strafrecht-auswerten
description: "Strukturierte Auswertung der Strafakte nach Akteneinsicht § 147 StPO. Erstellt Beweismittelverzeichnis (Urkunden Augenscheinsobjekte Zeugen Sachverstaendige) Personenregister Chronologie Aussagen-Synopse mit Inkonsistenzen Verwertungsverbots-Pruefung Belehrungsfehler § 136a StPO Beschuldigtenrechte § 136 StPO Beweisverwertungsverbote sowie Verteidigungsstrategie-Optionen. Ergebnis ist Aktenexzerpt zur Hauptverhandlungsvorbereitung mit Beweisantraegen Befangenheits-Pruefung und Vermerk fuer Beweisverwertung."
---

# Akteneinsicht — Strafakte auswerten

## Zweck

Aus der oft tausende Seiten umfassenden Strafakte das Verteidigungs-relevante extrahieren und systematisch ordnen.

## Voraussetzung

- Akteneinsicht § 147 StPO gewährt
- Akte als PDF mit OCR
- Mandantengespräch zur Sachlage erfolgt

## Schritt 1 — Personenregister

Tabelle aller in der Akte erwähnten Personen:

| Rolle | Name | Geburtsdatum | Funktion / Tat-Bezug | Aussage Bl. | Anschrift |
|---|---|---|---|---|---|
| Beschuldigter | … | … | … | … | … |
| Geschädigter | … | … | … | … | … |
| Zeuge | … | … | … | … | … |
| Polizeibeamter | … | … | … | … | … |
| Sachverständiger | … | … | … | … | … |

## Schritt 2 — Chronologie

Zeitleiste in Tag-Stunde-Format:

```
2025-11-12 23:15 — angeblicher Tatzeitpunkt
2025-11-12 23:47 — Zeugenanruf 110
2025-11-13 00:02 — Streifenwagen am Tatort
2025-11-13 00:14 — Festnahme Beschuldigter
2025-11-13 00:42 — Belehrung § 136 StPO laut Bl. 27
2025-11-13 01:35 — Beschuldigtenvernehmung beginnt Bl. 31
…
```

## Schritt 3 — Beweismittelverzeichnis

### Urkunden
- Bl. 1–5 Anzeige
- Bl. 27 Belehrungsprotokoll
- Bl. 31–48 Beschuldigtenvernehmung
- Bl. 49 ff. Vermessungs- und Spurensicherungs-Protokoll
- Bl. … Sachverständigengutachten

### Augenscheinsobjekte
- Asservat 1 Tatwaffe
- Asservat 2 Bekleidung
- Video-DVD aus Überwachungskamera

### Personalbeweise
- Z1 Anzeigeerstatter
- Z2 Augenzeuge
- Z3 Lebensgefährtin Beschuldigter
- SV1 Rechtsmediziner

## Schritt 4 — Aussagen-Synopse

Pro Tat-Element (objektiver Tatbestand: Wer Wann Wo Wie):

| Element | Aussage Z1 | Aussage Z2 | Beschuldigter | Anderes Beweismittel |
|---|---|---|---|---|
| Tatort | … | … | bestreitet | Spurensicherung |
| Tatzeit | 23:15 | 23:30 | 23:00 | Handydaten |

**Inkonsistenzen markieren** — jede Abweichung ist möglicher Ansatzpunkt.

## Schritt 5 — Verwertungsverbote prüfen

### Belehrungsfehler

- **§ 136 StPO** Beschuldigtenbelehrung — Schweigerecht Verteidiger-Hinzuziehung
- **§ 136a StPO** Misshandlung Ermüdung Täuschung Drohung Hypnose Versprechen — absolutes Verwertungsverbot
- **§ 163a StPO** Belehrung bei polizeilicher Vernehmung
- **§ 52 ff. StPO** Zeugnisverweigerungsrecht
- **§ 110a StPO** Verdeckte Ermittler — Trennungsgebot

### Wohnungsdurchsuchung

- **§ 105 StPO** richterliche Anordnung Pflicht Gefahr im Verzug eng auszulegen (BVerfGE 103, 142)
- **§ 102 StPO** Beschuldigten-Wohnung
- Fund von Beweismitteln über Anordnungs-Gegenstand hinaus — Zufallsfund § 108 StPO

### Telekommunikationsüberwachung

- **§ 100a StPO** Katalogstraftaten Subsidiaritätsklausel
- **§ 100e StPO** richterliche Anordnung
- Verwendung in anderen Verfahren § 100e Abs. 6 StPO

### Beschuldigtenrecht

- **§ 137 StPO** Verteidigerwahl
- **§ 140 StPO** notwendige Verteidigung
- **§ 141 StPO** Pflichtverteidiger-Bestellung

## Schritt 6 — Verteidigungsstrategie

### Optionen aufstellen

- Vollumfängliches Bestreiten
- Teilgeständnis bezüglich Randdetails
- Verfahrenseinstellung § 153 § 153a § 154 § 154a StPO (Bagatelle Auflage Teileinstellung)
- Verständigung § 257c StPO
- Beweisanträge zur Erschütterung der Belastungsbeweise

### Beweisantragsvorbereitung

- **Beweisthema** klar formuliert
- **Beweismittel** konkret bezeichnet (Zeugen mit Anschrift, Augenscheinsobjekt)
- **Konnex** zwischen Beweismittel und Tatumstand
- **Frist** spätestens vor letzter Schließung der Beweisaufnahme

## Schritt 7 — Sachverständigengutachten kritisch lesen

- **Anknüpfungstatsachen** vollständig der SV mitgeteilt?
- **Methode** anerkannt? (DNA mtDNA STR-Analyse Kapillarvergleich)
- **Schluss-folgerung** zwingend oder eine von mehreren?
- **Gegengutachten** denkbar?

## Schritt 8 — Befangenheit prüfen

- Richter § 24 StPO Ablehnungsgründe
- Sachverständiger § 74 StPO

## Ausgabe

- `aktenexzerpt-{az}.md` Hauptdokument
- `personenregister.md` Tabelle
- `chronologie.md` Zeitleiste
- `aussagen-synopse.md` Inkonsistenzen markiert
- `verwertungsverbote.md` mit Begründung pro Beweismittel
- `verteidigungsstrategie.md` Optionen plus Bewertung
- Liste vorbereiteter Beweisanträge
- Termin-Check Hauptverhandlung

## Quellen

- StPO §§ 136 136a 137 140 141 147 163a
- BVerfGE 103, 142 (Hausdurchsuchung Gefahr im Verzug)
- BGH 2. und 5. Strafsenat (Verwertungsverbote)
- Meyer-Goßner/Schmitt StPO
- Beulke/Swoboda Strafprozessrecht

## Aktuelle Rechtsprechung Aktenauswertung

- BVerfGE 103, 142 (Beschl. v. 20.02.2001 - 2 BvR 1444/00) — Hausdurchsuchung: "Gefahr im Verzug" nach § 105 I StPO ist eng auszulegen; richterliche Anordnung bleibt Regelfall; polizeiliche Eigenmaechtikeit ohne konkrete Eilbegruendung fuehrt zum Beweisverwertungsverbot.
- BGH, Urt. v. 26.11.1998 - 4 StR 493/98, BGHSt 44, 308 — Beweisverwertungsverbot bei Belehrungsfehler (§ 136 StPO): Vernehmungsprotokoll ist grundsaetzlich unverwertbar, wenn der Beschuldigte nicht ordnungsgemaess ueber sein Schweigerecht belehrt wurde.
- BGH, Urt. v. 18.04.2007 - 5 StR 546/06, BGHSt 51, 285 — TKU-Zufall-Funde (§ 108 StPO): aus einer TKU nach § 100a StPO gewonnene Erkenntnisse duerfen nur in dem Mass in anderen Verfahren verwertet werden wie § 100e VI StPO es erlaubt; Verwendungsbeschrankung.
- BGH, Urt. v. 30.07.1999 - 1 StR 618/98, BGHSt 45, 221 — Aussagen-Wuerdigung bei Aussage-gegen-Aussage: Gericht muss alle Glaubwuerdigkeitsmerkmale pruefen (Konstanz, Detailreichtum, Entstehungsgeschichte); Revisionsgericht kontrolliert Methodenfehler.

## Kommentarliteratur Aktenauswertung

- Meyer-Gossner/Schmitt, StPO, 67. Aufl. 2024, § 136a Rn. 1-40 (verbotene Vernehmungsmethoden)
- Eisenberg, Beweisrecht der StPO, 11. Aufl. 2022 (Standardwerk Beweisverwertungsverbote)
- Schoenke/Schroeder, StGB, 30. Aufl. 2019, Vorb. §§ 1 ff. Rn. 1-30 (Grundlagen Strafrecht)
