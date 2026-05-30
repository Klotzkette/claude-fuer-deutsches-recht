# Anlagen zu Schriftsätzen


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren** (`anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler`) | [Gesamt-PDF lesen](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Zuordnung von Anlagen zu gerichtlichen Schriftsätzen. Sortiert PDF/Word/Excel nach Schriftsatz-Logik (Klage/Erwiderung/Replik), konvertiert nach PDF, vergibt K/B/AST/AG, stempelt oben rechts in Arial 12, beA-tauglich, mit Konvolut. Modi: Auto-Benennung, Schriftsatz folgt, Prüfmodus.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Anlagen zu Schriftsätzen (`anlagen-zu-schriftsaetzen`, dieses Plugin) | [anlagen-zu-schriftsaetzen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `anlagen-zu-schriftsaetzen` | Zuordnung von Anlagen zu gerichtlichen Schriftsätzen. Liest den Schriftsatz (Klage/Klageerwiderung/Replik), erkennt vorhandene Beweisstücke, sortiert nach Schriftsatz-Logik, konvertiert alles nach PDF, benennt nach … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 2 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Anlagen Zu Schriftsaetzen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbei... |
| `anlagen-zu-schriftsaetzen` | Anwalt hat Schriftsatz fertig und muss Anlagen korrekt benennen nummerieren und als PDF-Konvolut aufbereiten. Anlagemanagement gerichtliche Schriftsaetze. Prüfraster: Schriftsatz lesen Beweisstuecke erkennen sortieren beA-konforme Benenn... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
