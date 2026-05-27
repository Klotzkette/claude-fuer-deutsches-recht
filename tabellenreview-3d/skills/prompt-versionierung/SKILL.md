---
name: prompt-versionierung
description: "Prompt-Versionen fuer den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Pruefraster: Versionsnummer, Aenderungsprotokoll, aktive Version. Output: Prompt-Versionsprotokoll. Abgrenzung: nicht Prompt-Erstellung."
---

# /tabellenreview-3d:prompt-versionierung


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


## Zweck

Wenn der Spaltenprompt 'Change-of-Control' heute leicht anders formuliert ist als gestern dann sind die heutigen Zellen mit den gestrigen nicht vergleichbar. Dieser Skill macht den Unterschied explizit.

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

- Pruefdimension geändert (z. B. Spalte 'AGB-Wirksamkeit' splittet zu 'Wirksam' und 'Anwendbares-AGB-Regime')
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
