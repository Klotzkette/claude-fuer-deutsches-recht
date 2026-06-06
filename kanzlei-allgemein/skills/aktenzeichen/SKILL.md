---
name: aktenzeichen
description: "Erkennung Normalisierung und Verknuepfung von Aktenzeichen in der Kanzlei. Anwendungsfall beA-Nachricht oder Brief enthaelt Aktenzeichen das einer Akte zugeordnet werden muss. Normen § 51 BRAO Organisationspflicht § 253 Abs. 2 Nr. 1 ZPO § 130a ZPO. Prüfraster Typen (eigenes gerichtliches behoerdliches gegnerisches) Normalisierung Varianten Kollisionen Kontext. Output Verknuepfungstabelle mit Sicherheitsgrad Kollisionswarnungen Rückfragen bei Unsicherheit. Abgrenzung zu kanzlei-allgemein-akte und kanzlei-allgemein-intake im Kanzlei Allgemein: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Aktenzeichen und Verknüpfungen

## Arbeitsbereich

Erkennung Normalisierung und Verknuepfung von Aktenzeichen in der Kanzlei. Anwendungsfall beA-Nachricht oder Brief enthaelt Aktenzeichen das einer Akte zugeordnet werden muss. Normen § 51 BRAO Organisationspflicht § 253 Abs. 2 Nr. 1 ZPO § 130a ZPO. Prüfraster Typen (eigenes gerichtliches behoerdliches gegnerisches) Normalisierung Varianten Kollisionen Kontext. Output Verknuepfungstabelle mit Sicherheitsgrad Kollisionswarnungen Rückfragen bei Unsicherheit. Abgrenzung zu kanzlei-allgemein-akte und kanzlei-allgemein-intake. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Liegt ein eigenes Kanzlei-Aktenzeichen, ein gerichtliches Aktenzeichen oder ein behördliches Zeichen vor?
2. Gibt es Kollisionsgefahr bei aehnlichen Aktenzeichen-Varianten in derselben Akte?
3. Soll das Aktenzeichen einem bereits vorhandenen Mandat zugeordnet oder als neues Mandat angelegt werden?
4. Sind fremde Aktenzeichen (Gegner, Versicherung, Rechtsschutz) mit dem eigenen verknuepft?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 51 BRAO — Berufshaftpflicht des Rechtsanwalts; Aktenzeichen-Fehler als Pflichtverletzung
- § 253 Abs. 2 Nr. 1 ZPO — Bezeichnungspflicht der Parteien und Sache in der Klageschrift
- § 319 ZPO — Berichtigung offensichtlicher Unrichtigkeiten in Urteilen (auch Aktenzeichen)
- § 130a ZPO — Pflichtangaben beim elektronischen Dokument, inkl. Aktenzeichen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill verhindert Suchchaos. Er erkennt Aktenzeichen aus Texten, Dateinamen, Betreffzeilen, beA-Nachrichten, PDFs, Screenshots und Notizen und verknüpft sie mit der richtigen Kanzleiakte.

## Typen von Aktenzeichen

- Eigenes Kanzlei-Aktenzeichen.
- Gerichtliches Aktenzeichen.
- Behördenzeichen.
- Gegnerisches Aktenzeichen.
- Versicherungs- oder Schadennummer.
- Rechtsschutz-Schadennummer.
- Mandanteninterne Projektnummer.
- Altaktenzeichen.

## Ablauf

1. Alle Kandidaten extrahieren.
2. Varianten normalisieren: Leerzeichen, Schrägstrich, Bindestrich, führende Nullen.
3. Kontext prüfen: Name, Gericht, Gegner, Datum, Betreff.
4. Kollisionen markieren.
5. Eindeutige Verknüpfung vorschlagen.
6. Unsichere Zuordnung als Rückfrage ausgeben.

## Ausgabe

```markdown
## Aktenzeichen-Verknüpfung

| Typ | Aktenzeichen | Quelle | Akte | Sicherheit | Notiz |
| --- | --- | --- | --- | --- | --- |
```

## Sicherheitsregel

Wenn zwei Akten plausibel sind, nicht automatisch ablegen. Immer nachfragen.
