# Testakten

Die Testakten prüfen die Qualitätswerkzeuge der Vorlagensammlung mit kleinen,
kontrollierten Beispieldaten. Sie gehören nicht zum juristischen
Vorlagenbestand, werden nicht als ODT erzeugt und gelangen nicht in die
Downloadpakete.

## Enthaltene Testakten

| Testakte | Zweck |
|---|---|
| [`eval-harness/`](eval-harness/) | Deckt alle deklarativen Checktypen des Eval-Harness ab und stellt Daten für gezielte Fehlerproben bereit. |

## Prüfprinzip

Jede Testakte enthält nur die Daten, die ein bestimmtes Verhalten eindeutig
belegen. Positive Fälle stehen in der Testakte selbst. Negativfälle wie
unbekannte Checktypen, doppelte IDs, ungültige reguläre Ausdrücke oder
unbekannte Vorlagen-Slugs erzeugt
[`tests/test_run_eval.py`](../test_run_eval.py) isoliert in temporären
Verzeichnissen. Dadurch bleiben Fehlertests reproduzierbar und können keine
echte Vorlage oder Rubric verändern.
