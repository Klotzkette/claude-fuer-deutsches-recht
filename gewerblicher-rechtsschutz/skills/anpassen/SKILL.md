---
name: anpassen
description: "Kanzleiprofil nachträglich anpassen: Durchsetzungsstrategie, Genehmigungsmatrix, Portfolio-Register, OSS-Richtlinie oder Überwachungslisten aktualisieren, ohne das gesamte kaltstart-interview erneut auszuführen."
---

# Kanzleiprofil anpassen

## Zweck

Gezielte Nachbearbeitung einzelner Abschnitte des Kanzleiprofils ohne vollständiges Wiederholungs-Interview. Einsatzfelder: neue Marke ins Portfolio aufnehmen, Genehmigungsmatrix nach Personalwechsel anpassen, OSS-Richtlinie nach Strategie-Update aktualisieren, externen Berater wechseln.

## Eingaben

- Gewünschte Änderung im Klartext (z. B. „Füge Marke NORDBLATT DE hinzu", „Ändere Genehmiger für Abmahnungen auf Max Mustermann")
- Ggf. neue Dokumente (Portfolio-Export, OSS-Richtlinie als PDF/DOCX)

## Ablauf

### 1. Kanzleiprofil laden

Konfiguration aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/gewerblicher-rechtsschutz/CLAUDE.md` lesen. Falls Platzhalter vorhanden: auf `kaltstart-interview` hinweisen.

### 2. Änderungsumfang bestimmen

| Änderungsart | Betroffener Abschnitt |
|---|---|
| Schutzrecht hinzufügen/entfernen | `## IP-Portfolio` + `portfolio.yaml` |
| Durchsetzungsstrategie ändern | `## Durchsetzungsstrategie` |
| Genehmigungsmatrix ändern | `## Durchsetzungsstrategie > Genehmigung` |
| Externen Berater ändern | `## IP-Kanzleiprofil > Externe Berater` |
| OSS-Richtlinie | separates oss-policy-Dokument |
| Überwachungsliste | `## Markenschutz > Überwachte Marken` |
| Integrationen | `## Verfügbare Integrationen` |

### 3. Änderungen vorschlagen und bestätigen

Änderungen als Diff-artige Vorschau zeigen (alt → neu). Nutzer bestätigt, bevor geschrieben wird.

### 4. Profil aktualisieren

Nach Bestätigung das betreffende Profil schreiben. Änderungsdatum vermerken:
`# Zuletzt geändert: [JJJJ-MM-TT]`

### 5. Downstream-Folgen prüfen

Einige Änderungen haben Folgewirkungen auf andere Skills:

| Änderung | Downstream-Folgen |
|---|---|
| Durchsetzungsstrategie von „ausgewogen" auf „offensiv" | unterlassungsverlangen-Skill senkt Schwelle für Abmahnempfehlung |
| Neuer Genehmiger | alle Genehmigungsgates aktualisiert |
| Neues Schutzrecht | portfolio-Skill fügt Fristen automatisch hinzu |
| OSS-Richtlinie verschärft | open-source-pruefung-Skill verwendet neue Whitelist |

Folgewirkungen dem Nutzer mitteilen.

## Quellen und Zitierweise

Keine primären Rechtsquellen – administrativer Skill. Zitierweise nach `../references/zitierweise.md` gilt für alle vom Skill erzeugten Dokumente.

## Ausgabeformat

Diff-Vorschau (alt / neu) je geändertem Abschnitt → Bestätigungsaufforderung → Bestätigungsmeldung nach Schreiben.

## Risiken / typische Fehler

- **Unbeabsichtigtes Überschreiben:** Nur den betreffenden Abschnitt ändern; nicht das gesamte Profil neu schreiben.
- **Inkonsistente Matrix:** Genehmigungsmatrix und Durchsetzungsstrategie müssen zueinander passen; bei Widerspruch nachfragen.
- **Kein Rollback:** Das Plugin speichert keine Vorversionen; bei wichtigen Änderungen vorher eine Sicherungskopie anlegen.
