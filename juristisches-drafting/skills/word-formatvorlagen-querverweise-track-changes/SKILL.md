---
name: word-formatvorlagen-querverweise-track-changes
description: "Microsoft Word für juristisches Drafting. Formatvorlagen (Standard; Überschrift eins bis fünf; Definition; Zitat; Anlage) sorgen für einheitliches Schriftbild; automatisches Inhaltsverzeichnis; Verzeichnisse von Definitionen und Anlagen. Querverweise per Feldfunktion machen Verschiebungen sicher. Änderungen verfolgen aktivieren; sichtbar halten; Annehmen oder Ablehnen einzeln. Kommentare am Rand. Vergleichen-Funktion. Mit Tabelle Word-Feature gegen Anwendungsfall und Liste der Anti-Patterns wie manuelle Nummerierung und Hardcoded Verweise."
---

# Word: Formatvorlagen, Querverweise und Track Changes

## Zweck

Microsoft Word ist das deutsche Kanzlei-Werkzeug. Wer Word nicht beherrscht, baut Verträge und Schriftsätze auf Sand. Drei Funktionsgruppen sind unverzichtbar: Formatvorlagen (für einheitliches Schriftbild und automatische Verzeichnisse), Querverweise (für interne Verweise, die Verschiebungen mitführen) und Änderungen verfolgen (für jeden Revisions-Workflow).

Dieser Skill erklärt diese drei Gruppen praxisorientiert. Er zeigt, welche Word-Funktion welchen Drafting-Zweck erfüllt, und vermeidet die häufigsten Anti-Patterns.

## Eingaben

- Word-Dokumenttyp (Vertrag, Schriftsatz, NDA, AGB, Memo)
- Vorhandene Vorlage der Kanzlei (Briefkopf, Schriftbild, Formatvorlagen-Satz)
- Word-Version (mindestens 2016, sinnvollerweise 365)
- Verteilung (intern, Mandant, Gegenseite, Gericht)

## Rechtlicher und methodischer Rahmen

- Inhaltliche Sorgfaltspflicht aus § 43a BRAO; Word-Hygiene ist Teil dieser Sorgfalt.
- § 130a ZPO und § 31a ERVV: elektronischer Rechtsverkehr; PDF/A-konforme Ausfertigung über beA.
- § 32a StPO für Strafverfahren und § 55a VwGO für Verwaltungsgerichte für analoge Anforderungen.
- Schriftform und Textform: §§ 126, 126a, 126b BGB; im Word geht es um den Entwurf, nicht um die Form der Unterschrift.
- Mandantengeheimnis: § 203 StGB. Metadaten und Dokumenteneigenschaften können Mandantennamen, Autoren und Pfade enthalten; vor Versand entfernen.

## Ablauf / Checkliste

1. **Formatvorlagen statt manueller Formatierung.** Standard, Überschrift 1 bis 5, Definition (eigene Vorlage), Zitat, Anlage. Vor dem Schreiben anlegen; nicht zwischendurch.
2. **Überschriften gliedern hierarchisch.** Überschrift 1 für Hauptabschnitte; Überschrift 2 für Paragraphen; Überschrift 3 für Absätze; tiefer nur, wenn nötig. Automatische Nummerierung über die Listenformatvorlage aktivieren.
3. **Inhaltsverzeichnis erzeugen.** Verweise einfügen, Inhaltsverzeichnis aus Formatvorlagen. Aktualisierung über F9 oder Rechtsklick.
4. **Querverweise per Feldfunktion.** Einfügen, Querverweis, Typ wählen (Nummeriertes Element oder Überschrift), Verweis (Absatznummer, Seitenzahl). Vorteil: Verschiebt sich das Ziel, verschiebt sich der Verweis automatisch.
5. **Definitionen-Verzeichnis.** Eigene Formatvorlage "Definition" anlegen. Index erzeugen über Verweise, Index einfügen.
6. **Änderungen verfolgen aktivieren.** Überprüfen, Änderungen verfolgen einschalten. Markup: Alle Markups anzeigen. Bei Versand prüfen: an oder aus.
7. **Kommentare am Rand.** Überprüfen, neuer Kommentar. Sind nicht Track Changes, sondern Anmerkungen.
8. **Annehmen oder Ablehnen einzeln.** Vor der finalen Ausfertigung jede Änderung einzeln prüfen; nicht pauschal "Alle annehmen".
9. **Vergleichen-Funktion.** Überprüfen, Vergleichen, zwei Versionen wählen. Ergebnis: Redline-Dokument.
10. **Metadaten vor Versand entfernen.** Datei, Informationen, auf Probleme überprüfen, Dokument prüfen. Autor, Kommentare, Versionen, persönliche Pfadangaben.

### Word-Feature gegen Anwendungsfall

| Word-Funktion | Drafting-Anwendung |
|---|---|
| Formatvorlage Überschrift 1 bis 5 | Vertragsstruktur, Schriftsatzgliederung |
| Formatvorlage Definition (eigen) | Defined Terms im Vertrag, automatisches Verzeichnis |
| Formatvorlage Anlage (eigen) | Anlagenverzeichnis K1, B1 |
| Listenformatvorlage | Klauselnummerierung 1.1, 1.1.1 |
| Querverweis Überschrift | "wie in § 5 dieses Vertrages geregelt" mit Aktualisierung |
| Querverweis Nummeriertes Element | Verweis auf Anlage K3 |
| Inhaltsverzeichnis | Übersicht bei Verträgen über 20 Seiten |
| Indizes | Definitionen-Verzeichnis, Stichwortverzeichnis |
| Änderungen verfolgen | Revisionen mit Gegenseite und Mandant |
| Kommentare | Anmerkungen für Mandanten oder Co-Drafter |
| Vergleichen | Redline zweier Versionen |
| Dokument prüfen | Metadaten entfernen vor Versand |
| Felder F9 aktualisieren | Inhaltsverzeichnis und Querverweise nach Änderungen |

## Typische Drafting-Fehler

- **Manuelle Nummerierung.** "1." getippt statt Listenformatvorlage. Beim Verschieben einer Klausel hängen Nummern und Verweise.
- **Hardcoded Verweise.** "wie in § 5" geschrieben statt Querverweis. Verschiebt sich § 5, bleibt der Text "§ 5" stehen.
- **Tabulator-Listen.** "1. <Tab> Text" statt Listenformatvorlage. Schriftbild nicht einheitlich; Inhaltsverzeichnis unbrauchbar.
- **Heading-Styling mit fettem Standard.** Überschrift sieht aus wie Überschrift; Inhaltsverzeichnis findet sie nicht.
- **Track-Changes-Versand vergessen.** Sichtbares Markup beim Gegner; oder unsichtbares Markup, das beim Klick auftaucht.
- **Metadaten-Leak.** Autorenfeld zeigt Mandantenname; Dokumenteigenschaften zeigen Kanzleipfad.
- **Felder nicht aktualisiert.** Inhaltsverzeichnis zeigt alte Seitenzahlen.
- **Verschiedene Dokumentschutz-Modi gemischt.** Schreibgeschütztes Markup mit eingeschalteter Bearbeitung verwirrt.

## Ausgabeformat

- Empfehlung pro Drafting-Aufgabe, welche Word-Funktion einzusetzen ist.
- Anleitung zur Einrichtung eines Formatvorlagen-Satzes.
- Checklist vor Versand: Felder aktualisieren, Markup einstellen, Metadaten entfernen.

## Beispiele

### Beispiel Formatvorlagen-Satz Vertrag

```
Standard            (Calibri 11, Zeilenabstand 1.15, Blocksatz)
Überschrift 1       (§-Ebene; vor 12 pt, nach 6 pt, fett 12 pt)
Überschrift 2       (Absatzebene; fett 11 pt)
Überschrift 3       (Unterabsatzebene; 11 pt kursiv)
Definition          (eingerückt; Begriff fett; Nummerierung optional)
Anlage              (zentriert; Versalien; "Anlage K1")
Zitat               (eingerückt; 10 pt; ohne Anführungszeichen)
```

### Beispiel Querverweis-Workflow

1. § 5 nummeriert über Überschrift 2 mit Listenformatvorlage.
2. Im Fließtext: Einfügen, Querverweis, "Überschrift", Verweis "Absatznummer". Ergebnis: "5".
3. Klausel wird verschoben und wird zu § 7. Felder über F9 aktualisieren. Verweis zeigt jetzt "7".

### Beispiel Track-Changes-Versand

1. Eigene Änderungen einpflegen.
2. Überprüfen, Markup, "Alle Markups anzeigen".
3. Vor Versand: Datei, Dokument prüfen, Probleme prüfen, persönliche Daten und Kommentare entfernen, falls erwünscht.
4. Speichern als neue Version v3 mit Datum: "Vertrag_LiefererXY_v3_2026-05-30.docx".

## Querverweise

- `revisions-prozess-redlines-comparison` für den Workflow zwischen Parteien
- `cowork-cloud-kollaboration-drafting` für Cloud-Kollaboration
- `dokumentstruktur-makroebene-vertrag-und-schriftsatz`
- `verweis-und-querverweis-technik` für die Drafting-Seite der Querverweise

## Quellen (Stand 05/2026)

- § 43a BRAO, § 203 StGB für anwaltliche Sorgfalt und Vertraulichkeit (Metadaten).
- § 130a ZPO, § 31a ERVV für elektronischen Rechtsverkehr.
- §§ 126, 126a, 126b BGB für Schriftform und Textform.
- Microsoft-Dokumentation zu Formatvorlagen und Felder über support.microsoft.com.
- `references/zitierweise.md` für Belegpflicht in den daraus erzeugten Dokumenten.
