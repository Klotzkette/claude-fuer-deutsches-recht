---
name: excel-reiter-4-workflow
description: "Baut Reiter 4 der Step-Plan-Excel: Workflow je Dokument in Reihenfolge der Beschaffung. Spalten erforderliches Dokument, Schritte in Reihenfolge, Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag), Unterzeichnet von und Versendet an. Liefert den konkreten Action-Plan."
---

# Reiter 4 Workflow Step-Plan

## Rolle und Fokus
Reiter 4 ist das Herzstueck. Hier wird aus jedem fehlenden Dokument ein
konkreter Step-Plan: welche Schritte in welcher Reihenfolge, mit welcher
Rechtsgrundlage, von wem zu unterzeichnen, an wen zu versenden.

## Vorlage-Bezug
Reiter 4 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Erforderliches Dokument | aus Reiter 3 uebernommen |
| Schritte zur Beschaffung (in Reihenfolge) | nummeriert 1. 2. 3. ... |
| Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) | Klausel oder Paragraph |
| Unterzeichnet von | die Personen, die zeichnen müssen |
| Versendet an | Empfaenger, ggfs mit Sendeweg (Bote, Einschreiben, Notar, HR) |

## Anwendungsbeispiel
LausitzStorage-Akte, Reiter 4 enthaelt 12 Beschaffungs-Workflows.
Beispiele:
- Einzelaval 50Hertz: 1. Antwort ILB-Rueckfrage 18.04. ergaenzen,
  2. ILB-Komitee 18.06. abwarten, 3. Backup-Antrag Berliner Sparkasse
  parallel halten, 4. Aval-Urkunde an 50Hertz.
- Reparaturvereinbarung Wandeldarlehen NordCap: 1. Entwurf Akte 22
  finalisieren, 2. NordCap-Anwalt Mitzeichnung, 3. Bauernfeind
  unterzeichnet.

## Output-Module
- Tabelleneintraege für Reiter 4
- Reihenfolge-Visualisierung als Gantt-aehnliche Liste (Datumsspalte
  optional)
- Verantwortlichkeiten-Liste pro Person
- Eingangsstapel für optionale Reiter (Fristen, Beteiligte)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Grenzen
- **Workflow ist Vorschlag, kein Anwaltsplan.** Anwaeltliche Prüfung der
  Rechtsgrundlagen-Spalte erforderlich.
- **Versendungswege sind Vorschlag.** Tatsaechlicher Zugangsweg muss
  haendisch abgesichert werden.
- **Zeitschaetzungen sind grob.** Behoerdliche Bearbeitungszeiten variieren.

## Plugin-Kontext
Reiter 4 ist der Action-Plan. Wenn Reiter 1 bis 3 sauber sind, schreibt
Reiter 4 sich fast von selbst. Optional ergaenzbar durch Reiter 5
(Fristen), Reiter 6 (Beteiligte), Reiter 7 (Rangfolge) und Reiter 8
(Sicherheiten).
