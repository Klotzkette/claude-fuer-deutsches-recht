# Mitwirken

Beiträge sollen die drei Marktrollen der Vergaberecht-Werkstatt praktisch
verbessern: Vergabestelle, Bieter/Bewerber oder Konkurrent/Zuschlagsgegner.
Neue Inhalte brauchen einen klaren Falltrigger, einen reproduzierbaren
Arbeitsablauf, passende Normen, belastbare Quellen und einen unmittelbar
verwendbaren Output.

## Pull-Request-Checkliste

- [ ] Marktrolle und Verfahrensstand sind eindeutig.
- [ ] Methodik folgt [`references/methodik-vergaberecht.md`](./references/methodik-vergaberecht.md).
- [ ] Zitierweise folgt [`references/zitierweise.md`](./references/zitierweise.md).
- [ ] Rechtsprechung wurde gegen eine amtliche oder frei prüfbare Quelle verifiziert.
- [ ] Skill-Frontmatter enthält ausschließlich `name` und `description`.
- [ ] Die `description` benennt Aufgabe, Trigger und wichtigsten Output konkret.
- [ ] Fristen, Rechtsstandsweichen und Beweisbedarf sind fallbezogen eingebaut.
- [ ] Beispiele enthalten nur fiktive Personen, Unternehmen und Vergabenummern.
- [ ] Gemeinsame Referenzen wurden mit `python3 scripts/sync-references.py` verteilt.
- [ ] Die schnelle Prüfkette läuft mit `python3 scripts/run-smoke-tests.py --quick` fehlerfrei.

Vor einem Commit sind mindestens diese beiden Marketplace-Prüfungen zwingend:

```bash
python3 scripts/validate-yaml-frontmatter.py
node scripts/validate-plugin-structure.mjs
```

## Skill-Struktur

```text
[plugin]/skills/[skill-slug]/SKILL.md
[plugin]/skills/[skill-slug]/references/  optional
```

Das Frontmatter ist einzeilig und enthält keine weiteren Felder:

```yaml
---
name: Niedrigpreisaufklärung steuern
description: Prüft bei auffälligem Preisabstand Anlass Ablauf und Dokumentation der Aufklärung nach Paragraf 60 VgV. Einsetzen vor Ausschluss oder Zuschlag sowie bei einer Niedrigpreisrüge. Liefert Fragenkatalog Antwortmatrix Geheimnisschutz und belastbaren Wertungsvermerk.
---
```

Der Body beginnt mit einem sprechenden Titel und führt durch Intake,
Tatbestand, Beleg, Entscheidung, Rechtsfolge und Output. Detaillierte Tabellen
oder Varianten gehören in eine direkt verlinkte Skill-Referenz, wenn der Body
sonst 500 Zeilen überschreiten würde.

## Neue oder geänderte Skills

1. Bestehende Skills derselben Marktrolle auf Überschneidungen prüfen.
2. Slug stabil, kleingeschrieben und unter 65 Zeichen halten.
3. Frontmatter und Workflow erstellen; generische Sammelnormen vermeiden.
4. Skill in Plugin-README, `SKILLS.md` und passendem Skill-Index sichtbar machen.
5. Bei zentraler Referenz `scripts/sync-references.py` ausführen.
6. Prompt-Routing nur ergänzen, wenn der Skill einen typischen Starttrigger abdeckt.
7. Vollständige Prüfkette aus `tests/smoke-tests.md` ausführen.

## Code of Conduct

Siehe [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

## Lizenz

Doppellizenziert unter Apache License 2.0 oder MIT License nach Wahl der
Nutzerin oder des Nutzers. Siehe [`LICENSE`](./LICENSE),
[`LICENSE-APACHE`](./LICENSE-APACHE), [`LICENSE-MIT`](./LICENSE-MIT) und
[`NOTICE`](./NOTICE). Beiträge werden unter denselben Bedingungen veröffentlicht.
