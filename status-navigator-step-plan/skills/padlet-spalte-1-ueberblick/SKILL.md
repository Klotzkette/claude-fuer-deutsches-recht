---
name: padlet-spalte-1-ueberblick
description: "Baut die erste Padlet-Spalte als Pendant zu Reiter 1 der Step-Plan-Excel. Überblick aller erforderlichen Dokumente mit Ampelfaerbung, Sortierung nach Vertragsebene und sieben Kartenfeldern (Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Unterzeichnet von, Rechtsgrundlage, Zweck)."
---

# Padlet Reiter 1 Überblick aufbauen

## Ziel
Spalte 1 des Padlets bildet Reiter 1 der Step-Plan-Excel ab: alle
erforderlichen Dokumente auf einen Blick, ampelfarblich gefuehrt.

## Vorlage-Bezug
Padlet-Spaltenkopf: `1. Uebersicht aller erforderlichen Dokumente`
Subtitle: `Alle für die Durchsetzung erforderlichen Dokumente in einer
einzigen Übersicht.`

Karteninhalt pro Dokument (sieben Felder aus der Excel-Vorlage):

| Padlet-Feld | Inhalt aus Excel-Vorlage |
|---|---|
| Kartentitel | Dokument |
| Untertitel | Datum |
| Statusbadge oben rechts | Verfuegbarkeit |
| Badge zweite Reihe | Unterschriftsstatus |
| Body Absatz 1 | Unterzeichnet von (Partei und Funktion) |
| Body Absatz 2 | Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) |
| Body Absatz 3 | Zweck |

## Padlet-Konfiguration
- Layout: **Shelf** (Spalten)
- Sortierung innerhalb der Spalte: nach Vertragsebene
  (Pacht, Netz, Genehmigung, Finanzierung, Gesellschaft, EPC)
- Kartenfarbe: GRUEN, GELB, ROT entsprechend Ampel
- Standardansicht: kompakte Karten

## Anwendungsbeispiel
LausitzStorage-Akte:
- Erste Karte oben (GRUEN): Pachtvertrag LEAG Hauptvertrag, 11.07.2025,
  vorliegend, vollstaendig.
- Zweite Karte (ROT): 1. Nachtrag Pacht, 09.10.2025, vorliegend
  privatschriftlich, fragwuerdig (§ 177 BGB).
- Dritte Karte (ROT): 2. Nachtrag Pacht, 14.02.2026, fragwuerdig.
- Vierte Karte (GRUEN): Netzanschlussvertrag 50Hertz, 28.08.2025,
  vollstaendig.
- ...

## Output-Module
- Padlet-Spalte 1 mit allen Dokumenten als Karten
- Ampelfarbe je Karte
- Anhaenge verlinkt
- Sortierreihenfolge nach Vertragsebenen

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Grenzen
- **Cloud-Dienst.** Vor Einsatz Datenschutzpruefung (siehe Padlet-Intro-Skill).
- **Maximale Sinnhaftigkeit bei bis zu 50 Dokumenten.** Darueber wird
  die Spalte unuebersichtlich; dann Excel bevorzugen oder mehrere
  Padlets pro Vertragsebene.

## Plugin-Kontext
Spalte 1 ist die Eingangsansicht. Die folgenden drei Padlet-Skills bauen
die Detailspalten 2, 3 und 4 auf.
