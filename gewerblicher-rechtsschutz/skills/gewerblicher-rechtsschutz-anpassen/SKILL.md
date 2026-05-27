---
name: gewerblicher-rechtsschutz-anpassen
description: "Kanzlei moechte ihr gewerbliches-Rechtsschutz-Profil nachjustieren ohne das gesamte Ersteinrichtungsinterview zu wiederholen. Profil-Update Gewerblicher Rechtsschutz. Pruefraster: Durchsetzungsstrategie Genehmigungsmatrix Portfolio-Register OSS-Richtlinie Ueberwachungslisten. Output: aktualisiertes Kanzleiprofil CLAUDE.md. Abgrenzung zu gewerblicher-rechtsschutz-kaltstart-interview (Ersteinrichtung) und gewerblicher-rechtsschutz-mandat-arbeitsbereich."
---

# Kanzleiprofil anpassen

## Zweck

Gezielte Nachbearbeitung einzelner Abschnitte des Kanzleiprofils ohne vollständiges Wiederholungs-Interview. Einsatzfelder: neue Marke ins Portfolio aufnehmen, Genehmigungsmatrix nach Personalwechsel anpassen, OSS-Richtlinie nach Strategie-Update aktualisieren, externen Berater wechseln.

## Eingaben

- Gewünschte Änderung im Klartext (z. B. „Füge Marke NORDBLATT DE hinzu", „Ändere Genehmiger für Abmahnungen auf Max Mustermann")
- Ggf. neue Dokumente (Portfolio-Export, OSS-Richtlinie als PDF/DOCX)

## Ablauf

### 1. Kanzleiprofil laden

Konfiguration aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/gewerblicher-rechtsschutz/CLAUDE.md` lesen. Falls Platzhalter vorhanden: auf `gewerblicher-rechtsschutz-kaltstart-interview` hinweisen.

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
| OSS-Richtlinie verschärft | open-source-prüfung-Skill verwendet neue Whitelist |

Folgewirkungen dem Nutzer mitteilen.

## Quellen und Zitierweise

Keine primären Rechtsquellen – administrativer Skill. Zitierweise nach `../references/zitierweise.md` gilt für alle vom Skill erzeugten Dokumente.

## Ausgabeformat

Diff-Vorschau (alt / neu) je geändertem Abschnitt → Bestätigungsaufforderung → Bestätigungsmeldung nach Schreiben.

## Risiken / typische Fehler

- **Unbeabsichtigtes Überschreiben:** Nur den betreffenden Abschnitt ändern; nicht das gesamte Profil neu schreiben.
- **Inkonsistente Matrix:** Genehmigungsmatrix und Durchsetzungsstrategie müssen zueinander passen; bei Widerspruch nachfragen.
- **Kein Rollback:** Das Plugin speichert keine Vorversionen; bei wichtigen Änderungen vorher eine Sicherungskopie anlegen.

## Rechtlicher Hintergrund: Kanzleipflichten bei Profilaenderungen

Bei Änderungen der Genehmigungsmatrix und Durchsetzungsstrategie sind folgende Normen relevant:

- BGH, Urt. v. 17.10.2019 – I ZR 34/18, GRUR 2020, 401 Rn. 22 – DSDS: Abmahnbefugnis setzt konkretes Wettbewerbsverhältnis voraus; bei Änderung des Mandantenprofils pruefen ob Aktivlegitimation noch besteht.
- BGH, Urt. v. 07.03.2019 – I ZR 184/17, GRUR 2019, 748 Rn. 31 – Energieeffizienzklasse III: Missbrauch nach § 8c UWG bei Serienvorgehen ohne ernsthaftes Unterlassungsinteresse; Genehmigungsmatrix sollte Missbr auchsprüfung enthalten.
- § 43a Abs. 2 BRAO – Verschwiegenheitspflicht: Kanzleiprofil und Mandantenstruktur unterfallen Verschwiegenheitspflicht; Profilaenderungen nur in gesicherter Umgebung.
- § 203 StGB – Unbefugte Offenbarung von Geheimnissen: Weitergabe von Mandantenstrukturdaten an ungesicherte Drittsysteme strafbewehrt.
