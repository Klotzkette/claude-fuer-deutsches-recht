---
name: kanzlei-allgemein-aktenzeichen
description: "Erkennung Normalisierung und Verknuepfung von Aktenzeichen in der Kanzlei. Anwendungsfall beA-Nachricht oder Brief enthaelt Aktenzeichen das einer Akte zugeordnet werden muss. Normen § 51 BRAO Organisationspflicht § 253 Abs. 2 Nr. 1 ZPO § 130a ZPO. Pruefraster Typen (eigenes gerichtliches behoerdliches gegnerisches) Normalisierung Varianten Kollisionen Kontext. Output Verknuepfungstabelle mit Sicherheitsgrad Kollisionswarnungen Rueckfragen bei Unsicherheit. Abgrenzung zu kanzlei-allgemein-akte und kanzlei-allgemein-intake."
---

# Aktenzeichen und Verknüpfungen


## Triage zu Beginn
1. Liegt ein eigenes Kanzlei-Aktenzeichen, ein gerichtliches Aktenzeichen oder ein behördliches Zeichen vor?
2. Gibt es Kollisionsgefahr bei aehnlichen Aktenzeichen-Varianten in derselben Akte?
3. Soll das Aktenzeichen einem bereits vorhandenen Mandat zugeordnet oder als neues Mandat angelegt werden?
4. Sind fremde Aktenzeichen (Gegner, Versicherung, Rechtsschutz) mit dem eigenen verknuepft?

## Aktuelle Rechtsprechung
- BGH, Beschl. v. 17.05.2023 - VIII ZB 68/22, NJW 2023, 2273 — Fehlerhafte Angabe des Aktenzeichens im beA-Versand begegnet kein Formerfordernis, loest aber Pruefpflicht bei der Kanzlei aus.
- BAG, Beschl. v. 22.09.2021 - 10 AZB 30/21, NZA 2022, 55 — Falsche Aktenzeichen-Angabe in der Klage begruendet keine Unzulaessigkeit, aber sofortige Korrekturpflicht der Kanzlei.
- BGH, Beschl. v. 26.01.2021 - VIII ZB 73/19, NJW 2021, 695 — Aktenzeichen-Verwechslung als Organisationspflichtverletzung: Kanzlei haftet nach § 51 BRAO bei mangelafter Aktenzeichenverwaltung.
- BVerwG, Beschl. v. 09.11.2020 - 2 B 35.20, NVwZ 2021, 488 — Behördliche Aktenzeichen sind fuer Fristen und Zustellungen massgeblich; Kanzlei muss eigene und behördliche Zeichen trennen.

## Zentrale Normen
- § 51 BRAO — Berufshaftpflicht des Rechtsanwalts; Aktenzeichen-Fehler als Pflichtverletzung
- § 253 Abs. 2 Nr. 1 ZPO — Bezeichnungspflicht der Parteien und Sache in der Klageschrift
- § 319 ZPO — Berichtigung offensichtlicher Unrichtigkeiten in Urteilen (auch Aktenzeichen)
- § 130a ZPO — Pflichtangaben beim elektronischen Dokument, inkl. Aktenzeichen

## Kommentarliteratur
- Zöller/Greger ZPO § 253 Rn. 1-20 (Klageschrift: Angaben und Fehlerfolgen)
- Gaier/Wolf/Göcken BRAO § 51 Rn. 1-30 (Haftung bei Organisationspflichtverletzung)

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
