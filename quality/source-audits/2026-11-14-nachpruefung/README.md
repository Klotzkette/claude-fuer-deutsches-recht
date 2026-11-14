# 1. Nachprüfung der vier offenen Profile

Dieser Bericht dokumentiert die 31 Dateireviews, die nach der Qualitätsrunde 445.36.0 noch offen waren. Fachliche Lektüre und Quellenabrufe: 14. November 2026; Integration und Abschluss: 15. November 2026. Ausgangspunkt ist Commit `d4d621de34186d03e343fdb144176b9986f1f1fe`. Die maschinellen Prüftage verwenden UTC: Der Abschluss am 15. November in Europe/Berlin liegt noch am 14. November UTC. Beide Angaben stehen ausdrücklich im Abschlussbeleg; die Zukunftsdatumsprüfung bleibt unverändert.

## 1.1. Umfang und Ergebnisse

| Profil | Vollständig nachgeprüfte Dateien | Ergebnis |
| --- | ---: | --- |
| [Anwaltschaft allgemein](anwaltschaft-generell.md) | 2 | Mini und Werkstatt vollständig gelesen; DSGVO-Bearbeitungsfrist präzisiert, zwei frühere Volltextlücken geschlossen, Zustellungsanker ergänzt. |
| [Corporate Contract Law](corporate-contract-law.md) | 20 | Alle Skills vollständig gelesen; sieben präzisiert, dreizehn beibehalten. Fünf BGH-Originale mit ihren tragenden Gründen geprüft. |
| [Gesellschafterstreit](gesellschafterstreit.md) | 3 | README, Mini und Werkstatt vollständig gelesen; 18 BGH-Originale erneut abgerufen und einschlägige Passagen gelesen. Historische PDF-Handbücher gekennzeichnet. |
| [Wirtschaftsanwalt](wirtschaftsanwalt.md) | 6 | Beide Manifeste, README, Fachquellen, Mini und Werkstatt vollständig gelesen. Berufsgeheimnis, Überschuldung, Liquiditätsbelege und Zustellungsnachweis präzisiert. |

Die zwanzig Corporate-Skills sind der dortige vollständige Nachprüfungsumfang. Zusätzlich geänderte Dateien besitzen individuelle Nachweise: Mini und Hauptproblem wurden vollständig gelesen; bei Werkstatt und README wurden die betroffenen vollständigen Absätze und abschließenden Metadaten geprüft. Eine zusätzliche Volllektüre dieser beiden Gesamtdateien wird nicht behauptet.

## 1.2. Nachweis statt bloßer Hashfortschreibung

[baseline.json](baseline.json) hält die früheren offenen Dateilisten und ihre Hashes aus dem Git-Ausgangsstand fest. `historical-profiles/` enthält die vier früheren Profile unverändert. Jeder Beleg unter `completed/` bindet den damaligen Status, den gelesenen Endstand, konkrete Prüfpunkte, das Ergebnis und die fachlichen Berichte mit SHA-256.

Das Qualitätslabor akzeptiert `reviewed` nur mit vollständigen Belegen. Fehlende Einzelprüfungen, geänderte Dateien, veränderte Berichte oder eine falsche Pluginzuordnung sperren den Abschluss beziehungsweise Releasebau. Die Schranken belegen Identität und Vollständigkeit der Dokumentation; sie beweisen weder eine tatsächliche menschliche Lektüre noch juristische Richtigkeit. Die inhaltliche Prüfung ist in den vier Fachberichten beschrieben.

## 1.3. Quellenstatus und Grenzen

Gelesene Normen und Urteilsgründe sind von historischen Suchnachweisen, Pressemitteilungen und fehlgeschlagenen Abrufen getrennt. Fehlgeleitete EUR-Lex-Antworten und CURIA-Anwendungsschalen wurden nicht als Volltextlektüre gewertet. BfDI-Normtexte wurden nur für die dokumentierten Artikel verwendet. Beim Wirtschaftsanwalt bleiben im Recherchewerkzeug lesbare amtliche BGH-PDF-Texte von erfolglosen direkten Originaldownloads unterschieden.

Die Dateireviews sind abgeschlossen; dokumentierte Quellenzugriffsgrenzen bleiben bestehen. Es gibt keinen neuen Live-Modelltest und keine pauschale Aktualitätsfreigabe sämtlicher Rechtsgebiete oder Testakten. Historische Modellproben und Prüfungen bleiben erhalten.

## 1.4. Veröffentlichung

[Qualitätsrunde 445.36.1](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/qualitaetsrunde-v445.36.1) umfasst vier native Plugin-ZIPs, fünfzehn eigenständige Promptdateien sowie Inventar und SHA-256-Prüfsummen. Die Pakete behalten zehn, zwanzig, elf beziehungsweise zehn aktive Skills. Der Workflow prüft einen festgelegten Main-Commit und erneut heruntergeladene Assets vor Veröffentlichung. [Releaseumfang und Prüfverfahren](../../../docs/releases/qualitaetsrunde-v445.36.1.md).
