---
name: padlet-spalte-3-fehlend
description: "Baut die dritte Padlet-Spalte als Pendant zu Reiter 3 der Step-Plan-Excel. Fehlende Dokumente mit Frist im Untertitel, Beschaffungsweg in zwei Absaetzen und Restzeit-Ampel (gruen mehr als 30 Tage, gelb 8 bis 30, rot bis 7)."
---

# Padlet Reiter 3 Fehlend aufbauen

## Ziel
Spalte 3 des Padlets bildet Reiter 3 der Step-Plan-Excel ab: fehlende
Dokumente mit Beschaffungsweg.

## Vorlage-Bezug
Spaltenkopf: `3. Fehlend`
Subtitle: `Dokumente oder Nachweise, die noch zu beschaffen sind.
Angefordert von bzw. Zu beschaffen von beschreibt den Beschaffungsweg.`

Karteninhalt (fuenf Felder aus der Excel-Vorlage):

| Padlet-Feld | Inhalt aus Excel-Vorlage |
|---|---|
| Kartentitel | Erforderliches Dokument oder erforderlicher Nachweis |
| Untertitel | Frist (falls vorhanden, sonst `Frist offen`) |
| Body Absatz 1 | Angefordert von (intern) |
| Body Absatz 2 | Zu beschaffen von (extern) |
| Body Absatz 3 | Grund der Erforderlichkeit (Klausel oder Paragraph) |
| Statusbadge | Status (offen, Anforderung raus, in Bearbeitung, ...) |

## Padlet-Konfiguration
- Spaltenfarbe: rot-orange (markiert: Aktionspflicht)
- Karten sortiert nach Frist aufsteigend (frueheste Frist zuerst)
- Kartenfarbe: nach Restzeit zur Frist
  - GRUEN: mehr als 30 Tage
  - GELB: 8 bis 30 Tage
  - ROT: bis zu 7 Tage

## Anwendungsbeispiel
LausitzStorage-Akte, Spalte 3 mit 12 Karten:
- Karte 1 (ROT, Frist 09.06.): Aushaendigung LEAG-Aval –
  bei LausitzStorage, an LEAG, § 11 Pachtvertrag
- Karte 2 (ROT, Frist 10.06.): Notartermin Klarstellungs-Nachtrag Pacht –
  RAin, Notar Albers, § 5 Pachtvertrag
- Karte 3 (ROT, Frist 11.06.): Klarstellungs-Side-Letter Anlage 4 –
  RAin, alle vier Gesellschafter, § 8 Konsortialvertrag
- Karte 4 (GELB, Frist 18.06.): ILB-Komitee Einzelaval 50Hertz
- Karte 5 (GELB, Frist 30.06.): BImSchG-Hauptantrag

## Output-Module
- Padlet-Spalte 3 mit Beschaffungs-Karten
- Sortierung nach Frist
- Fristen-Ampel je Karte
- Eingangsstapel für Spalte 4

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Grenzen
- **Frist-Tracking ersetzt keinen Fristenkalender.** Anwaltlicher
  Fristenkalender bleibt verbindlich.
- **Beschaffungswege sind Hypothesen.** Behoerdliche und gerichtliche
  Bearbeitungszeiten realistisch ansetzen.

## Plugin-Kontext
Spalte 3 ist der Treiber für Spalte 4. Jede Karte hier wird in Spalte 4
mit einem Schrittplan ausgearbeitet.
