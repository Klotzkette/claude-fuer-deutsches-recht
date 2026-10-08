# 1. Öffentliche Einbettung

## 1. Umfang

Diese Komponente liegt unter `vergaberecht-werkstatt/` im öffentlichen
Repository `Klotzkette/claude-fuer-deutsches-recht`.
Version: `445.33.1`. Komponenten-Release: `vergaberecht-werkstatt-v445.33.1`.
Der öffentliche Installationsnamensraum ist
`klotzkette-german-legal-skills`; der lokale Marketplace heißt weiterhin
`vergaberecht-werkstatt` und verwendet relative Rollenpfade.

Die 990 Quelldateien bleiben erhalten, abgesehen von zwei dokumentierten
Pfadumbenennungen. Lizenzen, NOTICE, Fallunterlagen und binäre Dateien sind
unverändert. Rubrics und historische Audits bleiben als Entwicklungsquellen
erhalten, gehören aber nicht in Arbeitsakten-ZIPs.

## 2. Rollen Und Prompts

| Rolle | Skills | Werkstatt | Schnellstart |
| --- | ---: | --- | --- |
| Vergabestelle | 122 | [Volltext](vergabestelle-behoerden/vergabestelle-behoerden-werkstatt.md) | [Markdown](vergabestelle-behoerden/vergabestelle-behoerden-schnellstart.md) |
| Bieter | 113 | [Volltext](bieter-unternehmen/bieter-unternehmen-werkstatt.md) | [Markdown](bieter-unternehmen/bieter-unternehmen-schnellstart.md) |
| Konkurrent | 20 | [Volltext](konkurrenten-rechtsschutz/konkurrenten-rechtsschutz-werkstatt.md) | [Markdown](konkurrenten-rechtsschutz/konkurrenten-rechtsschutz-schnellstart.md) |

Die Werkstattdateien übernehmen den vollständigen Fachinhalt der vorhandenen
Arbeitsprompts. Nur in den kanonischen Rollen-Kopien werden Überschriften
dezimal nummeriert, bisher als H3 markierte Unterpunkte hierarchisch als H4
eingeordnet und Produktbezeichnungen in der Skill-Routing-Prosa neutralisiert.
Die historischen Quellprompts bleiben unverändert; technische Literale und
Codeblöcke werden nicht umgeschrieben.
Bei den Unified-Mini-Prompts wurden nur Leerzeichen an Tabellenzellen entfernt,
damit jede Datei und ihre Schnellstart-Kopie höchstens 7500 UTF-8-Bytes hat.
Fachlicher Inhalt, Normen und Fallanker wurden dabei nicht gekürzt.
Die Standalone-Prompts werden einzeln als Markdown angeboten, nicht als
Prompt-ZIPs oder als Bestandteile der installierbaren Plugin-/Skills-ZIPs.
Ein vollständiges Quellarchiv darf sie enthalten und ist kein Plugin.

Nur zwei Rollen enthielten den zu beanstandenden Skillpfad:

- `vergabestelle-behoerden/skills/vergaberechtliche-pruefung-anwaltlich-megaprompt/SKILL.md`
  wurde zu `vergabestelle-behoerden/skills/vergaberechtliche-pruefung-anwaltlich/SKILL.md`.
- `bieter-unternehmen/skills/vergaberechtliche-pruefung-anwaltlich-megaprompt/SKILL.md`
  wurde zu `bieter-unternehmen/skills/vergaberechtliche-pruefung-anwaltlich/SKILL.md`.

Frontmatter, aktive Verweise, Index und Regressionstests verwenden den neuen
Slug. Die dritte Rolle enthielt keinen solchen Skill; kein Skill wurde
hinzugefügt oder gelöscht.
Arbeitsdatei-Links in den Rollen-READMEs und Skill-Indizes verwenden den
öffentlichen Markdown-Downloader mit dem Komponentenpräfix.
README- und andere Navigationsseiten bleiben normale Seitenlinks.

## 3. Build Für Den Root-Wrapper

Alle Befehle laufen mit Arbeitsverzeichnis `vergaberecht-werkstatt`.
Die Dateien unter `.github/workflows/` sind hier inert und kein Root-Workflow.
Installation der lokalen Prüfabhängigkeiten:

```bash
python3 -m pip install -r requirements-dev.txt
```

Nach einer inhaltlich beabsichtigten Änderung:

```bash
python3 scripts/generate-unified-mini-prompts.py
python3 scripts/generate-skills-md.py
python3 scripts/generate-skills-overview.py
python3 scripts/generate-megaprompt.py
python3 scripts/inject-plugin-sofort-download-section.py
python3 scripts/inject-top-readme-downloads.py
python3 scripts/inject-gesamt-pdf-section.py
python3 scripts/sync-public-entrypoints.py
```

Build und Prüfung ohne Veröffentlichung:

```bash
python3 scripts/sync-public-entrypoints.py --check
python3 scripts/validate-public-integration.py
python3 scripts/run-smoke-tests.py --quick
python3 scripts/build-plugin-release-zips.py dist
python3 scripts/build-testakten-release-zips.py dist
python3 scripts/build-skills-markdown-bundles.py dist
python3 scripts/validate-release-zips.py dist
python3 scripts/validate-testakten-release-zips.py dist
```

Der Testakten-Builder erzeugt pro Akte
`testakte-<slug>.zip`, `testakte-<slug>-einzelpdfs.zip` und
`<slug>_gesamt.pdf`, außerdem das kombinierte Arbeitsakten-ZIP.
Beide Akten-ZIP-Varianten und das kombinierte ZIP sind flach; erster Eintrag
ist `README.txt` mit dem zweisprachigen Warnhinweis. Das Gesamt-PDF wird
nur separat angeboten und nicht erneut in Arbeits-ZIPs aufgenommen. Die PDF-Inhalte werden
nicht verändert. Interne Bewertungsraster, Lösungsmetadaten und
Markdown-Aktenfragmente werden nicht in die Arbeits-ZIPs aufgenommen.

Der Root-Wrapper sammelt zusätzlich die Markdown-Einzeldateien und erstellt
die drei Sammelpakete `alle-plugins-megazip.zip`,
`alle-skills-markdown.zip` und `alles-komplettpaket.zip`.
Sammelpakete mit Testakten benötigen ebenfalls die unveränderte
`testakten/README.txt` auf ZIP-Wurzelebene.
Das Komplettpaket enthält den vollständigen Komponenten-Quellbestand unter
`vergaberecht-werkstatt/` und den Warnhinweis als `README.txt` auf
ZIP-Wurzelebene. Es ist kein installierbares Plugin und verwendet nicht die
frühere Teilkopie unter `repo-uebersichten/`.
Der optionale lokale Gesamtbau `python3 scripts/build-release-assets.py dist`
setzt ein leeres Ausgabeverzeichnis voraus und erstellt alle Komponentenassets
einschliesslich Prüfsummen; er führt keinen Upload aus.

## 4. Änderungsbereiche

- `.claude-plugin/marketplace.json` und die drei Rollenmanifeste:
  Version, Autorenkontakt und öffentliche Projektziele.
- Rollen-READMEs, Komponenten-README, `SKILLS.md`, `skills-index/`,
  `unified-mini-prompts/README.md` und Testakten-READMEs:
  Downloadziele, Installation, Dateiformate und Warnhinweise.
- `scripts/public_release.py`, `scripts/testakte_notices.py`,
  `scripts/sync-public-entrypoints.py`: gemeinsame Releaseziele,
  Warnhinweise und Kopiensynchronisation.
- Bestehende Generatoren, ZIP-Builder, Validatoren, Smoke-Tests und
  `tests/test_public_integration.py`: reproduzierbare technische Anpassung.
- `.github/workflows/release-plugin-zips.yml`: deaktivierter Altworkflow,
  Komponenten-Tag und sichere Übergabe des manuellen Tags.

Der optionale externe Entwicklungshelfer
`scripts/llm-judge-eval.py` ist nicht Bestandteil der Plugin-ZIPs und
kein Installationsschritt. Sein gesonderter Aufruf mit SDK und API-Schlüssel
übermittelt eingelesene Ausgabedaten und Prüfkriterien an einen externen
Dienst. Die lokalen Prüfketten rufen ihn nicht auf.
Fiktive Kontaktdaten aus den Testakten dürfen nicht zur Kontaktaufnahme,
Zustellung oder Einreichung verwendet werden.
