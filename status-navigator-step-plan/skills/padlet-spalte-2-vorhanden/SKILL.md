---
name: padlet-spalte-2-vorhanden
description: "Baut die zweite Padlet-Spalte als Pendant zu Reiter 2 der Step-Plan-Excel. Vorliegende Dokumente mit Type-Tag (Vertrag, Bescheid, Erklaerung, Beschluss, Schreiben) und Statusbadge fuer den Unterschriftsstatus."
---

# Padlet Reiter 2 Verfuegbar aufbauen

## Ziel
Spalte 2 des Padlets bildet Reiter 2 der Step-Plan-Excel ab: vorliegende
Dokumente mit Detailblick auf Unterschriftsstatus.

## Vorlage-Bezug
Spaltenkopf: `2. Verfuegbar`
Subtitle: `Aktuell vorliegende Dokumente. Die Spalte Unterzeichnet von
listet die unterzeichnenden Parteien und deren Funktion auf.`

Karteninhalt (sechs Felder aus der Excel-Vorlage):

| Padlet-Feld | Inhalt aus Excel-Vorlage |
|---|---|
| Kartentitel | Dokument (Bezeichnung) |
| Untertitel | Datum |
| Typ-Tag | Typ (Vertrag, Bescheid, Erklaerung, Beschluss, Schreiben) |
| Body Absatz 1 | Unterzeichnet von (Partei und Funktion) |
| Statusbadge | Unterschriftsstatus |
| Body Absatz 2 | Anmerkung |

## Padlet-Konfiguration
- Spaltenfarbe: blau-grau (markiert: Detailspalte)
- Kartenfarbe: nach Unterschriftsstatus (GRUEN, GELB, ROT)
- Type-Tag oben links farblich gefuehrt:
  - Vertrag = dunkelblau
  - Bescheid = dunkelgruen
  - Erklaerung = orange
  - Beschluss = lila
  - Schreiben = grau

## Vorgehen
1. Spalte 2 anlegen, Namen setzen.
2. Aus Reiter 1 alle GRUENEN und GELBEN Dokumente uebernehmen, die als
   `vorliegend` markiert sind. ROTE (`FEHLT`) gehoeren in Spalte 3.
3. Pro Karte Type-Tag setzen.
4. Pro Karte den Unterschriftsbefund aus dem Skill unterschriftspruefung
   in der Anmerkung kurzfassen.
5. Anhaenge verlinken.

## Anwendungsbeispiel
LausitzStorage-Akte, Spalte 2 enthaelt 16 Karten:
- Pachtvertrag (GRUEN, Vertrag-Tag): UR-Nr. 217/2025 Notar Albers,
  Tresor Pohlmann und Pohlmann
- 1. Nachtrag (GELB, Vertrag-Tag): Kosturek allein, § 177 BGB schwebend
- Senior-Darlehensvertrag (GRUEN, Vertrag-Tag): Le Bouedec + Kraft
- Wandeldarlehen (GELB, Vertrag-Tag): Datums-Copy-Paste 14.10. vs 17.10.
- Gesellschafterbeschluss (GRUEN, Beschluss-Tag): UR-Nr. 387/2025

## Output-Module
- Padlet-Spalte 2 mit allen vorliegenden Dokumenten als Karten
- Type-Tag je Karte
- Statusbadge entsprechend Unterschriftsstatus

## Grenzen
- **Type-Tag ist Hilfsklassifikation**, keine rechtliche Einordnung.
- **Anmerkungsfeld kurz halten.** Detailbefunde gehoeren in den
  Skill unterschriftspruefung oder copy-paste-fehler-erkennung.

## Plugin-Kontext
Spalte 2 ist Lieferquelle fuer die Querkommunikation zwischen Padlet-Karten
und Excel-Reitern. Wer hier sauber Type-Tags vergibt, kann spaeter
filtern (zum Beispiel `nur Beschluesse anzeigen`).
