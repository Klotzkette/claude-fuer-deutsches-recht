# Mitwirken

Beiträge sind willkommen – insbesondere zu neuen Rechtsgebieten, aktuelleren Auflagen von Kommentaren und neuen BGH-/EuGH-Entscheidungen.

## Pull-Request-Checkliste

- [ ] Sprache deutsch.
- [ ] Zitierweise nach [`references/zitierweise.md`](./references/zitierweise.md).
- [ ] Methodik nach [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md).
- [ ] Skill-Frontmatter vollständig und validatorfest (ausschließlich `name` und `description`).
- [ ] Skills sind kanzleitauglich (reproduzierbar, mit Quellenpflicht, mit Fristlogik wo relevant).
- [ ] Keine Mandantendaten / personenbezogene Daten im Beispiel.
- [ ] `node scripts/validate-plugin-structure.mjs` läuft fehlerfrei.
- [ ] `python3 scripts/validate-yaml-frontmatter.py` läuft fehlerfrei.
- [ ] `node scripts/validate-marketplace-import.mjs` läuft fehlerfrei.
- [ ] `python3 scripts/audit-skill-activation.py` meldet keine schwachen Auswahlbeschreibungen.

## Skill-Struktur

```
plugin-slug/skills/skill-slug/SKILL.md
plugin-slug/skills/skill-slug/references/  (optional)
```

`SKILL.md`-Frontmatter:

```yaml
---
name: Kurzname
description: Wann wird dieser Skill ausgewählt, welches Problem löst er und welches Arbeitsprodukt liefert er?
---
```

## Wie ergänze ich eine neue Anspruchsgrundlage?

1. Skill-Verzeichnis anlegen.
2. SKILL.md mit Frontmatter, Ablauf, Beispielen, Quellen.
3. Auf `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` verlinken.
4. Eintrag in `references/rechtsgebiete-uebersicht.md` ergänzen.
5. PR mit kurzer Begründung.

## Code of Conduct

Siehe [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

## Lizenz

Doppellizenziert unter **Apache License, Version 2.0** ODER **MIT License**, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`) – siehe [`LICENSE`](./LICENSE), [`LICENSE-APACHE`](./LICENSE-APACHE), [`LICENSE-MIT`](./LICENSE-MIT) und [`NOTICE`](./NOTICE). Mit deinem Beitrag stimmst du der Veröffentlichung unter diesen Bedingungen zu.
