# arbeitszeugnisprüfer-skill — Eval-Harness Drop-In-Bundle

Komplettes Pull-Request-Gerüst zum manuellen Einspielen in das externe Repo
[`Klotzkette/arbeitszeugnispruefer-skill`](https://github.com/Klotzkette/arbeitszeugnispruefer-skill).

## Was im Bundle ist

```
arbeitszeugnispruefer-skill-bundle/
  scripts/
    run-eval.py                  # Execution Harness
    compare-eval-runs.py         # Modell-zu-Modell-Dashboard
    llm-judge-eval.py            # LLM-Judge (Anthropic-Adapter)
    generate-default-rubrics.py  # Baseline-Rubric-Generator
    run-eval-adapter.patch       # Hinweis zur Pfad-Anpassung (rein informativ)
  fixtures/
    zeugnis-note-1/              # Positivreferenz
      README.md                  # Eingabe-Zeugnis
      rubric.yaml                # 7 Pass/Fail-Checks
    zeugnis-rote-flaggen/        # Note 4 mit roten Codes
      README.md
      rubric.yaml                # 9 Pass/Fail-Checks
    zeugnis-schaufenster-drift/  # Note 2-3 mit Drift
      README.md
      rubric.yaml                # 6 Pass/Fail-Checks
    zeugnis-azubi-bbig/          # Paragraf 16 BBiG-Sonderfall
      README.md
      rubric.yaml                # 6 Pass/Fail-Checks
```

## Manueller Drop-In in 5 Schritten

```bash
# 1) Klon des externen Repos
git clone https://github.com/Klotzkette/arbeitszeugnispruefer-skill.git
cd arbeitszeugnispruefer-skill
git checkout -b feature/harvey-style-eval-harness

# 2) Bundle herunterladen (von hier per raw.githubusercontent oder Klon)
curl -L https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/main.tar.gz | \
  tar -xz --strip-components=4 \
  claude-fuer-deutsches-recht-main/docs/portable-eval-harness/arbeitszeugnispruefer-skill-bundle/

# 3) Scripts + Testakten ins Repo kopieren
mkdir -p scripts fixtures
cp arbeitszeugnispruefer-skill-bundle/scripts/*.py scripts/
cp -r arbeitszeugnispruefer-skill-bundle/fixtures/* fixtures/

# 4) PyYAML installieren (optional, fuer robusteres YAML-Parsing)
pip install pyyaml

# 5) Erster Eval-Lauf
python3 scripts/run-eval.py --report
# Erwartete Ausgabe: 4 Testfaelle, 4/4 PASS (sofern keine output.md vorhanden:
# die output.md-bezogenen Checks scheitern, weil der Skill-Output fehlt —
# das ist das gewuenschte Verhalten.)
```

## Eval-Workflow im Echtbetrieb

```bash
# Pro Testfall:
# 1) Skill auf das README.md anwenden (manuell oder via Chat-Agent / Claude Code)
# 2) Skill-Output als output.md im selben Verzeichnis ablegen
echo "$SKILL_OUTPUT" > fixtures/zeugnis-note-1/output.md

# 3) Eval-Lauf
python3 scripts/run-eval.py --report --json-out runs/$(date -u +%Y%m%d-%H%M).json --label "$MODEL"

# 4) Modellvergleich (zwei oder mehr Snapshots)
python3 scripts/compare-eval-runs.py runs/opus-4-7.json runs/opus-4-8.json

# 5) Bei subjektiven Kriterien: LLM-Judge
export ANTHROPIC_API_KEY=sk-ant-...
python3 scripts/llm-judge-eval.py fixtures/zeugnis-note-1/output.md eval-criteria/quellenhygiene.md
```

## Optional: PR-Beschreibung für das externe Repo

```markdown
## Summary

Bringt einen Harvey-LAB-style Eval-Harness ins Repo. Vier Scripts + vier
Beispiel-Testfaelle. Erlaubt automatisierte Pass/Fail-Bewertung der Skill-
Outputs gegen handgepflegte Rubrics, plus Modellvergleich und LLM-Judge.

## Was reinkommt

- `scripts/run-eval.py` - Execution Harness (All-Pass-Scoring)
- `scripts/compare-eval-runs.py` - Modell-zu-Modell-Dashboard
- `scripts/llm-judge-eval.py` - LLM-Judge mit Anthropic-Adapter + Dry-Run
- `scripts/generate-default-rubrics.py` - Baseline-Rubric-Generator
- `fixtures/zeugnis-note-1/` - Positivreferenz, 7 Checks
- `fixtures/zeugnis-rote-flaggen/` - Note 4 mit roten Codes, 9 Checks
- `fixtures/zeugnis-schaufenster-drift/` - Drift-Pattern, 6 Checks
- `fixtures/zeugnis-azubi-bbig/` - Paragraf 16 BBiG-Sonderfall, 6 Checks

## Test plan

- [ ] PyYAML installiert
- [ ] `python3 scripts/run-eval.py --report` laeuft durch
- [ ] Stichprobe: Skill manuell auf zeugnis-note-1 anwenden, output.md
      schreiben, eval erneut laufen lassen, Score notieren

## Inspiration

Harvey LAB (https://github.com/harveyai/harvey-labs). Diese Implementierung
ist auf das deutsche Recht und den Arbeitszeugnis-Pruefer zugeschnitten.
```

## Hinweise

- Die Scripts sind portabel und brauchen keine Änderung — die Konstante `TESTAKTEN = REPO / "fixtures"` passt zur Repo-Struktur des arbeitszeugnisprüfer-skill-Repos.
- Die Rubrics verwenden `output.md` als erwarteten Skill-Output-Pfad. Falls der Skill seinen Output anders nennt, in `rubric.yaml` den `path:`-Wert anpassen.
- Beim ersten Lauf ohne `output.md` werden die Checks scheitern, die auf `output.md` zugreifen — das ist erwartet und zeigt nur, dass der Skill noch nicht ausgefuehrt wurde.

## Lizenz

Apache-2.0 OR MIT - frei nutzbar im Folge-Repo.
