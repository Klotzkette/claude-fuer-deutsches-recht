# Übertragbare Ansätze aus Claude for Legal und Harvey

Verglichen am 16. November 2026 wurden die öffentlichen Quellstände von [Claude for Legal](https://github.com/anthropics/claude-for-legal/tree/4a6c651889c97cc9140580363c73e0eb17379c2b), [Harvey LAB](https://github.com/harveyai/harvey-labs/tree/7f9b1ee19f9224576a5a5143c4e6f75842ac7020) und [BigLaw Bench](https://github.com/harveyai/biglaw-bench/tree/138fd481b459a00bbd98eeb710f69ada1052bd47) mit der bestehenden deutschen Sammlung.

## 1. Playbook-Prüfung mit wiederverwendbarem Arbeitsprofil

Anthropic speichert die Arbeitsweise und Zuständigkeiten eines Teams in einem Praxisprofil. Das deutsche [Kanzlei-Arbeitsprofil](../../../playbook-pruefer/references/kanzlei-arbeitsprofil.md) kann bei Bedarf direkt mit dem Auftrag in Claude oder ChatGPT vorgelegt werden. Die Kopie ist für diesen konkreten Auftrag vorgesehen. Bei passender Geltung und Freigabe kann sie Format, Zuständigkeiten und den Verweis auf das Playbook liefern. Dessen Text, Version und Geltung bleiben überprüfbare Eingaben; ein Verweis allein trägt keine Klauselfreigabe. Ein Profil aus einer fremden Vertragsdatei oder ohne passende Geltung wird nicht zur Vorgabe. Bei einem konkreten Auftrag ohne Profil beginnt die Prüfung direkt.

Die Profilvorlage liegt im Plugin-ZIP. Die zwei betroffenen Skills und alle drei eigenständigen Prompts verwenden dieselbe Abgrenzung. Die beiden Playbook-Testakten und die bestehende Regel- und Quellenprüfung sind weiterhin nutzbar. [Anthropics Praxisprofil und Konfiguration](https://github.com/anthropics/claude-for-legal/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/commercial-legal/skills/cold-start-interview/SKILL.md)

## 2. Agentenübergaben

Der in dieser Sammlung vorhandene Orchestrator enthielt noch die frühere Extraktion bis zur ersten schließenden Klammer. Die Übernahme der Idee aus Anthropic nutzt den JSON-Decoder, damit auch verschachtelte Payloads und geschweifte Klammern im Text erhalten bleiben. Die Versionierung und Quellenangabe des Codes bleiben in der Datei kenntlich. Der Weiterleitungsweg verwendet die aktuell dokumentierten Sitzungsereignisse. Die [Anleitung zur Referenzlaufzeit](../../../verwaltete-agentenrezepte/README.md) erläutert Einrichtung, Zielzuordnung und Prüfgrenzen. [Anthropic-Parserkorrektur](https://github.com/anthropics/claude-for-legal/commit/88c89068315dba1358dd5058ac4cdce4023682d8) · [Claude-Sitzungsereignisse](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)

## 3. Vergleich fairer Ergebnisläufe

Harvey LAB legt offen, welchen Einfluss verfügbare Abgaben und die tatsächlich ausgewertete Textsicht auf Vergleiche haben. Im Qualitätslabor fließen Aktenbytes, Bewertungsstand und aufbereitete Eingabetexte in die Gruppierung ein. Ältere Scores bleiben sichtbar, ihr unbekannter Bewertungsstand wird ausgewiesen. Die vorhandenen deutschen Akten, Kriterien und die getrennte professionelle Rechtsprüfung bleiben Grundlage. [Qualitätslabor](../../../quality/README.md) · [Vergleichsmethodik](../../../docs/benchmark.md) · [Harvey LAB v1.4.0](https://github.com/harveyai/harvey-labs/blob/7f9b1ee19f9224576a5a5143c4e6f75842ac7020/CHANGELOG.md)

## 4. Herkunft

Die Betriebsmethode des Arbeitsprofils und die Vergleichslogik des Qualitätslabors wurden eigenständig für diese Sammlung umgesetzt. Verwendet wurden die veröffentlichten Quellen und ihre Dokumentation. US-Rechtsinhalte, Benchmarktasks, Anbieterzugänge und Fremdinstallationen waren nicht erforderlich. Der Lizenzhinweis nennt für Anthropic die seit dem Initialcommit belegte Apache-2.0-Lizenz. [Anthropic-Lizenz](https://github.com/anthropics/claude-for-legal/blob/d541734b08e67aae330a362b256d1eb6808a08f5/LICENSE)
