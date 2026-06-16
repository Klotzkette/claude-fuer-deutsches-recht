---
name: padlet-spalte-4-workflow
description: "Baut die vierte Padlet-Spalte als Pendant zu Reiter 4 der Step-Plan-Excel. Workflow-Karten mit nummerierten Checkbox-Schritten, Rechtsgrundlage, Tags fuer Unterzeichner und Empfaenger sowie Fortschritts-Sortierung."
---

# Padlet Reiter 4 Workflow aufbauen

## Ziel
Spalte 4 des Padlets bildet Reiter 4 der Step-Plan-Excel ab: Workflow je
fehlendes Dokument, Schritt für Schritt.

## Vorlage-Bezug
Spaltenkopf: `4. Erstellung und Beschaffung`
Subtitle: `Für jedes zu erstellende bzw. zu beschaffende Dokument: die
erforderlichen Schritte in der Reihenfolge ihrer Ausfuehrung.`

Karteninhalt (fuenf Felder aus der Excel-Vorlage):

| Padlet-Feld | Inhalt aus Excel-Vorlage |
|---|---|
| Kartentitel | Erforderliches Dokument |
| Body Schrittliste | Schritte zur Beschaffung (in Reihenfolge), nummeriert |
| Body Absatz | Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) |
| Tag links | Unterzeichnet von |
| Tag rechts | Versendet an |

## Padlet-Konfiguration
- Spaltenfarbe: gruen-blau (markiert: Aktionsplan)
- Karten als To-do-Listen mit Checkboxen pro Schritt
- Fortschrittsanzeige: Prozentual erledigte Schritte pro Karte
  (Padlet-Funktion `Checklisten`)

## Anwendungsbeispiel
LausitzStorage-Akte, Spalte 4 mit 12 Workflow-Karten, davon:

**Karte Einzelaval 50Hertz**
- Tag links: ILB
- Tag rechts: 50Hertz
- Rechtsgrundlage: § 7 Netzanschlussvertrag; §§ 765 ff BGB
- Schritte:
  1. Antwort auf ILB-Rueckfrage 18.04.2026 ergaenzen
  2. ILB-Komitee 18.06.2026 abwarten
  3. Backup-Antrag Berliner Sparkasse parallel halten
  4. Aval-Urkunde an 50Hertz uebergeben

**Karte Reparaturvereinbarung Wandeldarlehen NordCap**
- Tag links: NordCap + Bauernfeind
- Tag rechts: NordCap + LausitzStorage
- Rechtsgrundlage: §§ 133, 157 BGB
- Schritte:
  1. Entwurf Akte 22 finalisieren
  2. NordCap-Anwalt Mitzeichnung
  3. Bauernfeind unterzeichnet
  4. Optional Notar Albers mitzeichnen

## Output-Module
- Padlet-Spalte 4 mit Workflow-Karten
- Checkboxen je Schritt
- Fortschritts-Sortierung
- Mandat-Reporting auf Knopfdruck

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Grenzen
- **Workflow ist Vorschlag**, anwaltliche Prüfung erforderlich.
- **Tags sind Hilfsklassifikation**, ersetzen keine Vollmachtspruefung.

## Plugin-Kontext
Spalte 4 schliesst den Step-Plan ab. Optional erweiterbar um eine
Spalte 5 (Fristen) und Spalte 6 (Beteiligte) – siehe Skills
erweiterung-rangfolge-reiter und excel-reiter-fristen-optional, die
analog als Padlet-Spalten ausspielbar sind.
