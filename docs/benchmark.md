# 1. Testakten und juristische Arbeitsergebnisse prüfen

Prüfe entweder den Bestand einer Testakte oder das Arbeitsergebnis eines tatsächlich ausgeführten Auftrags. Die Aktenprüfung kontrolliert vorhandene Dateien und Merkmale. Das [Qualitätslabor](../quality/README.md) bewertet die erzeugten Ergebnisse anhand fachlicher Kriterien und dokumentiert die Bedingungen, unter denen sie vergleichbar sind.

## 1.1. Prüfwege

| Aufgabe | Aussage des Ergebnisses | Werkzeug |
|---|---|---|
| Bestand einer Testakte prüfen | Dateien und technische Kriterien der `rubric.yaml` sind geprüft. Manuelle Kriterien bleiben offen. | [Aktenprüfung](../scripts/run-eval.py) |
| Zwei Aktenbestände vergleichen | Die Tabelle stellt die technischen Befunde aus den Aktenprüfungen gegenüber. | [Strukturvergleich](../scripts/compare-eval-runs.py) |
| Ausgeführte Aufträge bewerten und vergleichen | Zwei Prüfer bewerten das tatsächlich erzeugte Arbeitsprodukt anhand fachlicher Einzelkriterien. Die Wiederholungen werden anhand ihrer dokumentierten Bedingungen gruppiert. | [Qualitätslabor](../quality/README.md) |

## 1.2. Technischen Aktenbestand prüfen

```bash
# Alle Rubriken ausführen und einen technischen Vergleichsstand speichern.
python3 scripts/run-eval.py --structural-only --json-out /tmp/akten-vorher.json --label vorher

# Nach einer Änderung denselben Bestand noch einmal prüfen.
python3 scripts/run-eval.py --structural-only --json-out /tmp/akten-nachher.json --label nachher
python3 scripts/compare-eval-runs.py /tmp/akten-vorher.json /tmp/akten-nachher.json --out /tmp/akten-vergleich.md
```

## 1.3. Prüfrubrik für eine Testakte

```yaml
name: "Beschreibung der Testakte"
plugin: "primary-plugin-name"

checks:
  - id: r01-readme
    check_type: file_exists
    description: "README vorhanden"
    path: "README.md"

  - id: r02-fristhinweis
    check_type: regex_match
    description: "Standardfrist im Mandantenbrief erwaehnt"
    path: "01_mandantenbrief.md"
    pattern: "(3-Wochen|drei.{0,3}Wochen|. 4 KSchG)"

  - id: r03-anlagen-vorhanden
    check_type: file_count
    description: "Mindestens drei Anlagen"
    glob: "anlagen/*.*"
    min: 3

  - id: r04-bag-rspr-zitiert
    check_type: text_contains
    description: "BAG-Linie referenziert"
    path: "memo.md"
    contains: "BAG"

  - id: r05-finale-pruefung-manuell
    check_type: human_review
    description: "Finale Stil- und Schluesselbotschafts-Pruefung"
    note: "vor Mandanten-Versand manuell pruefen"
```

### 1.3.1. Prüfarten

| `check_type` | Pruefung |
|---|---|
| `file_exists` | Datei existiert |
| `text_contains` | Substring kommt in Datei vor |
| `regex_match` | Regex matcht in Datei |
| `file_count` | Anzahl Dateien matchen Glob >= min |
| `human_review` | Manuell — Eval-Skript zaehlt als `skipped` |

Offene `human_review`-Prüfungen verhindern ein vollständiges Bestehen. `--structural-only` lässt einen technisch fehlerfreien Aktenbestand für die Qualitätskontrolle durchlaufen und weist offene manuelle Prüfungen weiterhin aus.

## 1.4. Arbeitsergebnisse bewerten und vergleichen

Das Qualitätslabor unterstützt vollständige fachliche Prüfrubriken. Nach dem Vorbild von Harvey LAB erhält jede Einzelanforderung nur die für sie relevanten Ergebnisdateien. Das Gesamturteil ist positiv, wenn beide Prüfmodelle sämtliche Kriterien bestehen lassen. Offene oder widersprüchliche Urteile bleiben als solche sichtbar. [Harvey LAB, Bewertungsmethodik](https://github.com/harveyai/harvey-labs/blob/7f9b1ee19f9224576a5a5143c4e6f75842ac7020/docs/eval-strategies.md)

Harvey LAB weist Änderungen an Aufgaben, Laufumgebung, Bewertung und Schnittstellen als mögliche Ursache für verschobene Ergebnisse aus. Hier führt `compare` Eingabeprüfsummen, den Prüfcode, die von den Prüfern gelesenen Quellentexte und die verwendeten Extraktionsbibliotheken im Bericht. Das verhindert, dass Wiederholungen mit abweichenden Akten oder Bewertungsständen gemeinsam als Stichprobe erscheinen. [Harvey LAB, Änderungen mit Auswirkungen auf Bewertungszahlen](https://github.com/harveyai/harvey-labs/blob/7f9b1ee19f9224576a5a5143c4e6f75842ac7020/CHANGELOG.md)

BigLaw Bench unterscheidet die fachliche Güte der Antwort von der Verlässlichkeit ihrer Quellen und berücksichtigt konkrete Fehler. Für eigene Ergebnisfälle lassen sich entsprechend unabhängige Kriterien formulieren, etwa „fügt eine schlüssige Kündigungsfristberechnung bei“ und „ordnet der angeführten Entscheidung keine im bereitgestellten Volltext unbelegte Rechtsfolge zu“. Die Kriterien geben dem Prüfer jeweils die betroffene Ergebnisdatei an. Die eigenständige Prüfung der Rechtsquelle bleibt erforderlich. [BigLaw Bench, Bewertungsmethodik](https://github.com/harveyai/biglaw-bench/blob/138fd481b459a00bbd98eeb710f69ada1052bd47/README.md#evaluation-methodology)
