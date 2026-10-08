# Testakte für den Eval-Harness

Diese kleine, absichtlich fachneutrale Akte prüft die deklarativen Checktypen
des Eval-Harness. Sie gehört nicht zum Vorlagenbestand und wird weder als ODT
noch als Downloadpaket veröffentlicht.

Die Akte deckt positive Prüfungen für Datei, Text, regulären Ausdruck,
Dateianzahl, YAML-Feld, JSON-Feld und manuelle Prüfung ab. Fehlerfälle wie
ungültige reguläre Ausdrücke, doppelte Check-IDs und unbekannte Vorlagen-Slugs
werden in `tests/test_run_eval.py` isoliert erzeugt.
