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
| Unterzeichnet von | die Personen, die zeichnen muessen |
| Versendet an | Empfaenger, ggfs mit Sendeweg (Bote, Einschreiben, Notar, HR) |

## Vorgehen
1. **Pro Zeile aus Reiter 3 einen Schrittplan.** Bei Aval-Beschaffung sind
   das typischerweise: 1. Antrag, 2. Rueckfrageabarbeitung, 3. Komitee,
   4. Urkunde abholen, 5. an Glaeubiger zustellen.
2. **Vorlauf realistisch einrechnen.** Notartermin braucht 1 bis 2 Wochen,
   ILB-Komitee tagt monatlich, HR-Eintragung 2 bis 6 Wochen.
3. **Verantwortung benennen.** Wer macht den Schritt? RAin? GF? Notar?
   Vertragspartner? Behoerde? Konkret in der Spalte Unterzeichnet oder
   Versendet ausweisen.
4. **Rechtsgrundlage benennen.** Welche Vertragsklausel oder welcher
   Paragraph trifft hier? Ein Hinweis, keine Pruefung.
5. **Sendeweg auswaehlen.** Bote mit Empfangsbestaetigung
   ist haufig die sicherste Variante.

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
- Tabelleneintraege fuer Reiter 4
- Reihenfolge-Visualisierung als Gantt-aehnliche Liste (Datumsspalte
  optional)
- Verantwortlichkeiten-Liste pro Person
- Eingangsstapel fuer optionale Reiter (Fristen, Beteiligte)

## Grenzen
- **Workflow ist Vorschlag, kein Anwaltsplan.** Anwaeltliche Pruefung der
  Rechtsgrundlagen-Spalte erforderlich.
- **Versendungswege sind Vorschlag.** Tatsaechlicher Zugangsweg muss
  haendisch abgesichert werden.
- **Zeitschaetzungen sind grob.** Behoerdliche Bearbeitungszeiten variieren.

## Plugin-Kontext
Reiter 4 ist der Action-Plan. Wenn Reiter 1 bis 3 sauber sind, schreibt
Reiter 4 sich fast von selbst. Optional ergaenzbar durch Reiter 5
(Fristen), Reiter 6 (Beteiligte), Reiter 7 (Rangfolge) und Reiter 8
(Sicherheiten).
