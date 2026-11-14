# Prompt- und Skill-Integration: gezielter Nachlauf

Prüfdatum: 14.11.2026. Alle 21 angeforderten allgemeinen Prüfkommandos sind erfolgreich; die JSON-Beilage nennt Einzelstatus, echte Testzahlen, Logpfade und Prüfsummen. Dies ist eine technische und redaktionelle Integrationsprüfung, keine erneute rechtliche Vollprüfung aller 315 Plugins.

Geprüfte und korrigierte Integrationspunkte:

- Die Sammlung von Werkstatt- und Megaprompt-Fachmaterial liest alle erhaltenen Originalmodule. Das kleinere aktive Menü ersetzt keine fachliche Grundlage. Beide neuen Regressionen scheitern beim bisherigen Algorithmus nachweislich. Keine breite Fachprompt-Neugenerierung.
- Schwerpunktkatalog: validierte `selection.target_skill` und passende aktuelle Hashbindung statt des ersten beliebigen Evaluationsfalls. Ein neuer Test verwirft veraltete Fokusbindungen.
- Der Routingaudit überspringt verschobene oder fehlende Einzelfachquellen nicht mehr; fachliche Verbotsanker werden weiter geprüft. Neue Negativfälle sichern dies.
- Integrationhelper: der generische Fokus-Hash gehört zum Prompt, wenn beide Pfade vorliegen; sämtliche alten Bindungspfade werden vor einer Mutation gesichert. Drei Regressionen verwerfen das vorherige Verhalten. Vier echte Profile mit dieser Feldform benötigten nach Abgleich ihrer unveränderten gültigen Bindungen keine Änderung.
- Arbeitsrecht-Hauptproblem redaktionell auf 7489 UTF-8-Bytes und 7356 Zeichen verdichtet, sämtliche BAG-Aussagegrenzen erhalten. Eigener Nachprüfvermerk: `quality/source-audits/2026-11-14/arbeitsrecht-hauptproblem-redaktion.md`.
- Sieben unveränderte fachliche Zitierregelvarianten nach vollständiger Lektüre exakt registriert; keine allgemeine Quellenneuverifikation. Scope: `quality/source-audits/2026-11-14/zitierregeln-nachpruefung.md`.
- Nested Vergaberecht: Fachbestand bleibt 122/113/20, aktive Auswahl wird separat gegen die Registry geprüft; Format- und Insolvenzmodulprüfungen sowie vier Zuständigkeitsgrenzen bleiben erhalten. Workflow-Validator und Smokeabschnitte 3/10/11 erfolgreich. Abschließende Routingmigration/Quick-Smoke wird separat dokumentiert.

| Prüfung | Ergebnis |
| --- | --- |
| `test-quality-lab.py` | 73 Tests; Exit 0 |
| `test-schwerpunkt-coverage.py` | 12 Tests; Exit 0 |
| `test-prompt-profile-app-boundary.py` | 3 Tests; Exit 0 |
| `test-prompt-publication-profiles.py` | 10 Tests; Exit 0 |
| `test-prompt-generator-excerpts.py` | Exit 0 |
| `test-prompt-routing-scope.py` | Exit 0 |
| `test-prompt-workflow-preservation.py` | 43 Tests; Exit 0 |
| `test-prompt-openings.py` | 6 Tests; Exit 0 |
| `test-prompt-hygiene-links.py` | 15 Tests; Exit 0 |
| `test-portable-starts.py` | 11 Tests; Exit 0 |
| `test-generate-megaprompt.py` | Exit 0 |
| `audit-generated-prompt-hygiene.py` | Exit 0 |
| `audit-prompt-profile-routing.py` | Exit 0 |
| `test-quickstart-usability.py` | 17 Tests; Exit 0 |
| `audit-quickstart-usability.py` | Exit 0 |
| `test-werkstatt-visualisierung.py` | 27 Tests; Exit 0 |
| `test-official-plugin-validation.py` | 10 Tests; Exit 0 |
| `test-skill-sources.py` | 4 Tests; Exit 0 |
| `test-skill-cap-integration.py` | 13 Tests; Exit 0 |
| `test-runtime-performance.py` | 7 Tests; Exit 0 |
| `validate-runtime-performance.py` | Exit 0 |

Keine Veröffentlichung oder neue Version durch diesen Prüflauf. Frühere Quellenprüfzeitpunkte und die eingefrorene ursprüngliche Migrationsinventur bleiben erhalten.

Zusätzlicher Vergaberecht-Nachlauf: `validate-legal-regressions.py` löst auch die 13 weiteren verschobenen Pflichtquellen streng über die Registry auf. Alle Rechtsmuster, Norm- und Schwellenwertmarker sind unverändert. Der Validator ist erfolgreich (579 Textdateien, 161 Binärartefakte), zwei neue Tests sichern entfernte Marker, fehlende Quellen und unregistrierte Ersatzdateien. Smokeabschnitt 1 mit sämtlichen Validatoren, sieben Rubrics und der vollständigen Unittest-Discovery ist jetzt erfolgreich. Die JSON-Beilage enthält Ergebnisse und Log-Hashes.
