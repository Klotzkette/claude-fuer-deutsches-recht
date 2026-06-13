# Hinweise fuer automatisierte Aufraeum- und Codex-Laeufe

Diese Datei richtet sich an Codex, Claude Code und vergleichbare
automatisierte Agenten, die im Repo aufraeumen, refaktorieren oder
Wartungs-Sweeps durchfuehren. Sie ist verbindlich.

## Bitte NICHT loeschen oder leeren

Die folgenden Bestandteile sind absichtlich da, auch wenn sie auf den
ersten Blick wie Hilfsdateien oder Duplikate aussehen koennen. Sie
duerfen nicht entfernt, verschoben oder geleert werden, ohne dass
Klotzkette das ausdruecklich anweist.

### Hilfsmaterial unter `testakten/`

- `testakten/formatvorlagen-paradebeispiele/` — Formatvorlagen pro
  Plugin. Hat bewusst KEINE `gesamt-pdf/`-Struktur und wird vom
  `validate-testakten-gesamt-pdf.py` explizit via `SKIP_DIRS`
  ausgenommen.
- `testakten/megaprompts/` — 213 Megaprompt-Markdown-Dateien (seit
  Welle 4 fuer alle Plugins), die pro Plugin via
  `scripts/generate-megaprompt.py` erzeugt werden. Ebenfalls in
  `SKIP_DIRS`. Diese Dateien duerfen ueberschrieben, aber nicht
  ersatzlos geloescht werden.

### Sammel- und Index-Dokumente

- `SKILLS.md`, `ASSET_INDEX.md`, `TESTBERICHT.md`, `EVAL_RESULTS.md`,
  `PROMPTLISTE.md`, `QUICKSTART.md`, `INSTALLATION_EINFACH.md`,
  `SKILL_REVIEW_CLAUDE.md`, `CONNECTORS.md`, `CONTRIBUTING.md`,
  `CODE_OF_CONDUCT.md` — alle Top-Level-Dokumente sind bewusst
  vorhanden, auch wenn sie sich teilweise inhaltlich ueberlappen. Sie
  werden von der Startseite und von Plugin-READMEs aus verlinkt.
- `CODEX_INSTRUCTIONS_SKILL_VEREDELUNG.md` — inhaltliche
  Veredelungs-Anweisungen pro Skill, kein Duplikat dieser Datei.

### Hilfsscripts unter `scripts/`

Folgende Skripte sind idempotente Wartungs-Werkzeuge und sollen erhalten
bleiben — auch wenn sie nur einmal oder unregelmaessig laufen:

- `cleanup-megaprompt-disclaimers.py`
- `move-megaprompt-block-to-end.py`
- `fill-missing-plugin-keywords.py`
- `inject-megaprompt-section.py`
- `generate-megaprompt.py`
- `generate-formatvorlagen.py`
- `sweep-umlaut-welle-2.py`, `sweep-umlaut-welle-3.py`
- alle `validate-*` Scripts und `generate-skills-*` Scripts

### Plugin-Hilfsdateien

- `0_setup-cowork3p-eu-gateway/` ist anbieterneutral gehalten. Keine
  konkreten Anbieternamen (`langdock`, `helicone`, vergleichbare)
  wieder einsetzen. Die Generalisierung war Ergebnis mehrerer
  expliziter User-Runden (PRs #262, #266, #269).

## Verbindliche Regeln

1. Vor jeder Loeschung mehr als einer Datei: `git fetch origin` und auf
   den letzten `main`-Stand pruefen.
2. Keine Skill-Frontmatter-Felder einfuegen, die nicht in
   `scripts/validate-yaml-frontmatter.py` unter `ALLOWED_FIELDS`
   stehen (`name`, `description`, `allowed-tools`).
3. Keine `description`-Strings ueber 1024 Zeichen, keine XML-Tags,
   keine `\d,\d`-Komma-Zahlen — sonst bricht Cowork-Validierung.
4. `name`-Felder in YAML-Frontmatter und Plugin-Manifest: ausschliesslich
   `[a-z0-9-]`, maximal 64 Zeichen. Slug == Ordnername.
5. Commits niemals mit Author `Claude`, `Codex`, `AI` oder
   vergleichbaren Maschinen-Identitaeten taggen. Verwende
   `Klotzkette / 39582916+Klotzkette@users.noreply.github.com`.
6. Vor jedem Push: alle drei Validatoren laufen lassen:
   - `python3 scripts/validate-yaml-frontmatter.py`
   - `node scripts/validate-plugin-structure.mjs`
   - `python3 scripts/validate-testakten-gesamt-pdf.py`
7. Versions-Bumps konsistent durchziehen: alle 213 `plugin.json` und
   `.claude-plugin/marketplace.json` muessen dieselbe Version tragen.
8. Tags `vN.0.0` triggern `.github/workflows/release-plugin-zips.yml`.
   Ein zweites Tag mit gleicher Versionsnummer muss vorher geloescht
   werden (`git push origin :refs/tags/vN.0.0`).

## Was Codex bei einem Veredelungs-Lauf gefahrlos darf

- Tippfehler in Markdown-Fliesstext korrigieren.
- Trailing whitespace und leere Zeilen-Sequenzen normalisieren.
- README-Block-Reihenfolge angleichen (z. B. `<!-- BEGIN
  megaprompt-und-vorlagen -->`-Block am Datei-Ende lassen, nicht
  oben).
- Plugin-`keywords`-Listen erweitern, sofern sie ein bestehendes
  Keyword nicht entfernen.
- Skill-`description`-Felder umformulieren, solange Pflichtregeln
  eingehalten sind.

Sollten Zweifel bestehen, lieber einen separaten Branch mit
`chore/codex-cleanup-YYYY-MM-DD` anlegen und einen PR fuer Klotzkette
oeffnen, statt direkt auf main zu pushen.

## Wer hat zuletzt veredelt

- v311 — Validator-Skip Hilfsmaterial, Megaprompt-Disclaimer-Cleanup
- v312/v313 — Quality loops + Release-Synchronisierung (Claude)
- v314 — Welle 4: Megaprompts fuer alle 213 Plugins + Link-Hygiene
  (Claude)
- v315 — `keywords` aufgefuellt (72 Plugins), Validator parallelisiert,
  diese CODEX.md neu (Klotzkette via Computer)
