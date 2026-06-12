---
name: prompt-versionierung-paket-review
description: "Prompt-Versionen für den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Prüfraster: Versionsnummer, Änderungsprotokoll, aktive Version. Output: Prompt-Versionsprotokoll. Abgrenzung: nicht Prompt-Erstellung im Tabellenreview 3d."
---

# /tabellenreview-3d:prompt-versionierung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Versionierungsschema

Semantische Versions-ID pro Prompt: `<spalte-id>@<major>.<minor>.<patch>`

### Patch (`x.y.Z+1`)

- Wortlautfeinheiten ohne Sinnänderung (Tippfehler / Stilkorrektur / Beispiel ergänzt)
- Vorhandene Zellen NICHT invalidiert
- Empfehlung: bestehende Zellen behalten

### Minor (`x.Y+1.0`)

- Antworttyp geändert (z. B. Freitext zu Ja-Nein)
- Ampelregel geändert (Schwelle verschoben)
- Antwortdimension hinzugefügt (z. B. zusätzlich Schwelle in EUR abfragen)
- Vorhandene Zellen werden auf `nachprüfen` gesetzt
- Empfehlung: betroffene Spalten erneut laufen lassen (Teil-Rerun)

### Major (`X+1.0.0`)

- Prüfdimension geändert (z. B. Spalte 'AGB-Wirksamkeit' splittet zu 'Wirksam' und 'Anwendbares-AGB-Regime')
- Spalte umbenannt oder zusammengelegt
- Vorhandene Zellen werden invalidiert
- Empfehlung: betroffene Zellen komplett neu berechnen

## Aktivierung und Deaktivierung

- Nur eine Version pro Spalte ist gleichzeitig aktiv (`aktive-prompts.yaml`)
- Alte Versionen liegen im `prompt-historie.yaml` mit `gültig-bis`-Datum
- Wer den aktiven Prompt ändert trägt zwingend den Migrationspfad für bestehende Zellen ein

## Pflichtfelder pro Prompt-Version

```yaml
- spalte-id: change-of-control
 version: "2.1.0"
 wortlaut: |
 Enthält der Vertrag eine Klausel die bei Kontrollwechsel ...
 antworttyp: zitat-mit-fundstelle-und-schwelle
 ampel-regel:
 rot: "Klausel vorhanden + harte Kündigungsfolge ohne Heilung"
 gelb: "Zustimmungsvorbehalt mit unklarer Schwelle"
 gruen: "Keine Klausel oder branchenübliche Schwelle"
 geaendert-am: "2026-05-20"
 geaendert-von: "anwalt-x"
 migrationspfad: "Patch-Änderung — bestehende Zellen behalten gültig."
```

## Integration mit Audit-Trail

Jede Prompt-Änderung erzeugt einen `prompt.geändert` Eintrag im `audit-trail-protokoll` mit Versionsnummer und Begründung.

## Grenzen

Versionierung verhindert keine schlechten Prompts — sie macht sie nur sichtbar. Der Prüfer entscheidet ob Migration noetig ist.
