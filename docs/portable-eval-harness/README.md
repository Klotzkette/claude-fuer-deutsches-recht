# Portable Eval-Harness — Drop-In für beliebige Legal-AI-Repos

[Repository-Start](../../README.md) · [Testakten](../../testakten/README.md) · [Qualitätsstandard](../../testakten/QUALITAETSSTANDARD.md)

Bringe den Klotzkette/Harvey-LAB-Style-Bewertungsrahmen in dein eigenes Repo.

## Was du bekommst

Vier Dateien, mehr nicht:

```
scripts/
  run-eval.py              # Execution Harness
  compare-eval-runs.py     # Modell-zu-Modell-Dashboard
  llm-judge-eval.py        # LLM-Judge (Anthropic-Adapter, Dry-Run-Fallback)
  generate-default-rubrics.py   # erzeugt Baseline-Rubrics fuer alle Testakten
```

Plus eine Konvention: pro Testakte eine `testakten/<slug>/rubric.yaml`.

## Drop-In in 4 Schritten

```bash
# 1) Klon das Klotzkette-Repo (oder lade die scripts/ als ZIP)
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git /tmp/klotzkette

# 2) Scripts in dein Repo kopieren
mkdir -p scripts
cp /tmp/klotzkette/scripts/run-eval.py scripts/
cp /tmp/klotzkette/scripts/compare-eval-runs.py scripts/
cp /tmp/klotzkette/scripts/llm-judge-eval.py scripts/
cp /tmp/klotzkette/scripts/generate-default-rubrics.py scripts/

# 3) Baseline-Rubrics fuer alle Testakten erzeugen (legt rubric.yaml an,
#    ueberschreibt nichts Bestehendes)
python3 scripts/generate-default-rubrics.py

# 4) Eval laufen lassen
python3 scripts/run-eval.py --report
```

## Anpassung an Repo-Struktur

Die Scripts erwarten:

```
<repo>/
  testakten/
    <slug>/
      README.md
      rubric.yaml
      ...
  scripts/
    run-eval.py
    ...
```

Wenn dein Repo eine andere Struktur hat, ändere oben in `run-eval.py` die Konstante:

```python
REPO = Path(__file__).resolve().parents[1]
TESTAKTEN = REPO / "testakten"   # <-- ggf. anpassen
```

## Anwendungsfaelle

### Fall 1: Arbeitszeugnispruefer-Repo

```bash
cd arbeitszeugnispruefer-skill
mkdir -p scripts testakten/dein-pruefkorpus
# Skill als Test-Subjekt, Pruefkorpus als Testakten
cp /tmp/klotzkette/scripts/*.py scripts/
# Eigene rubric.yaml pro Zeugnis-Testfall:
cat > testakten/zeugnis-note-1/rubric.yaml <<'EOF'
name: "Zeugnis Note 1 Positivreferenz"
plugin: "arbeitszeugnis-pruefer"

checks:
  - id: r01-readme
    check_type: file_exists
    description: "Zeugnis-Text als Testfall vorhanden"
    path: "README.md"

  - id: r02-ampel-symbol-im-output
    check_type: regex_match
    description: "Wenn ein Output existiert, ist die Ampel als Symbol gesetzt"
    path: "output.md"
    pattern: "(🟢|🔴|🟠|GRUEN|ROT|ORANGE)"

  - id: r03-bag-rechtsprechung-mit-az
    check_type: regex_match
    description: "Mindestens ein verifiziertes BAG-Aktenzeichen im Output"
    path: "output.md"
    pattern: "BAG.{0,20}[0-9]+ AZR.{0,20}/[0-9]+"

  - id: r04-quellenhygiene-keine-erfundenen-az
    check_type: human_review
    description: "BAG-Az. live verifiziert? (keine Modellwissens-Az.)"
    note: "Vor Schriftsatz: Aktenzeichen in bundesarbeitsgericht.de pruefen."
EOF

python3 scripts/run-eval.py --report
```

### Fall 2: Vorlagen-Repo

```bash
cd vorlagen-fuer-recht
mkdir -p scripts testakten/asset-deal-vorlage
cp /tmp/klotzkette/scripts/*.py scripts/

# Vorlagen-Check: muessen alle relevanten Klauseln drinstehen?
cat > testakten/asset-deal-vorlage/rubric.yaml <<'EOF'
name: "Vorlage Asset-Deal Vertrag"
plugin: "lizenzvertragsersteller"

checks:
  - id: r01-vertrag-docx
    check_type: file_exists
    description: "DOCX-Vorlage vorhanden"
    path: "docx/vertrag.docx"

  - id: r02-paragraf-613a
    check_type: text_contains
    description: "Paragraf 613a BGB-Klausel enthalten"
    path: "vertrag.md"
    contains: "613a"

  - id: r03-rechtswahl
    check_type: text_contains
    description: "Rechtswahl-Klausel praesent"
    path: "vertrag.md"
    contains: "Recht der Bundesrepublik Deutschland"

  - id: r04-final-review
    check_type: human_review
    description: "Anwaltliche Endpruefung vor Verwendung im Mandat"
    note: "Vorlage ist Geruest - immer individualisieren"
EOF

python3 scripts/run-eval.py --report
```

## Check-Typen

| `check_type` | Was es prüft |
|---|---|
| `file_exists` | Datei existiert |
| `text_contains` | Substring kommt in Datei vor |
| `regex_match` | Regex matcht in Datei |
| `file_count` | Anzahl Dateien matchen Glob >= min |
| `human_review` | Manueller Check - wird als 'skipped' gezaehlt |

## Modellvergleich (z. B. Opus 4.7 vs. 4.8)

```bash
# Lauf 1 mit Modell A:
python3 scripts/run-eval.py --json-out runs/opus-4-7.json --label "opus-4-7"
# Lauf 2 mit Modell B (nachdem Skills ggf. modellabhaengig angepasst wurden):
python3 scripts/run-eval.py --json-out runs/opus-4-8.json --label "opus-4-8"
# Side-by-Side mit Delta-Spalte:
python3 scripts/compare-eval-runs.py runs/opus-4-7.json runs/opus-4-8.json
```

## LLM-Judge

Für subjektive Pass/Fail-Kriterien, die keine reine Substring/Regex-Prüfung erlauben:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 scripts/llm-judge-eval.py path/to/skill-output.md path/to/criterion.md --out judge-result.json
```

Ohne API-Key: Dry-Run mit ausgegebenem Prompt — du kannst diesen manuell an ein Modell übergeben.

## Lizenz

Apache-2.0 OR MIT — die Eval-Harness-Scripts sind frei nutzbar in beliebigen Folge-Repos.

## Verhältnis zu Harvey LAB

Harvey LAB (https://github.com/harveyai/harvey-labs) ist das Vorbild: Task-Datenraum + Execution Harness + Rubrics + LLM-Judge. Diese portable Implementierung folgt demselben Paradigma, ist aber auf das deutsche Rechtssegment zugeschnitten und unabhängig vom Klotzkette-Skill-Bestand nutzbar.
