# Qualitätsnachweis KI-Halluzinationsreduzierer

## 1. Gegenstand und Grenzen

Gegenstand ist die Komponentenfassung 1.1.0 vom 19.10.2026 mit zehn Fachskills, einem Hauptskill, drei eigenständigen Prompts und fünf Referenzen. Das Werkzeug untersucht Quellenbehauptungen und Fallübertragung. Bei gerichtlicher Verwendung kommt eine gesonderte Prüfung von Aktenbezug, Verfahrensbegründung und tatsächlich mitgeteilter menschlicher Entscheidung hinzu. Es erkennt keine KI-Autorenschaft und garantiert keine prozessuale Wirksamkeit.

Eine strukturelle Prüfung bestätigt Dateien, Verweise und Paketidentität; sie beweist keine juristische Fehlerfreiheit. Die redaktionelle Gegenprüfung untersucht Methodik und belegte Aussagegrenzen. Die Modellproben verwenden ausdrücklich hypothetische Eingaben. Eine erfolgreiche Ausführung in Claude Cowork, Codex oder ChatGPT wird dadurch nicht behauptet.

## 2. Amtlich geprüfte Rechtsprechung

Der [Quellenbericht vom 19.10.2026](rechtsprechung-quellen-2026-10-19.md) dokumentiert sieben tatsächlich geöffnete amtliche Volltexte, genaue Leseumfänge und acht unmittelbar benötigte amtliche Einzelnormen. Er unterscheidet den Abruf eines vollständigen Textes von der Lektüre seiner hier entscheidenden Abschnitte. Sekundärfundstellen und in Gerichtsgründen genannte weitere Entscheidungen wurden nicht pauschal als verifiziert übernommen.

BAG, Beschluss vom 30.09.2026 – 2 AZN 339/26, betrifft die fehlende eigenverantwortliche Prüfung eines Fremdentwurfs und zusätzlich die unzureichende Darlegung von Zulassungsgründen. Drei Beschlüsse des VGH Baden-Württemberg unterscheiden fortbestehende Zulässigkeit, fehlende fallbezogene Begründung und eine offengelassene Nichtberücksichtigung. Drei KG-Beschlüsse betreffen die Quellenkontrolle, falsche Verfahrensbehauptungen und eine ausdrücklich offene Frage zur automatisierten Textbausteinbegründung.

Die [Rechtsprechungsreferenz](../../ki-halluzinationsreduzierer/references/rechtsprechung-ki-schriftsaetze.md) benennt zu jedem Anker „Trägt“ und „Trägt nicht“. Die [Schriftsatzprüfung](../../ki-halluzinationsreduzierer/references/schriftsatzpruefung.md) ist die daraus entwickelte organisatorische Arbeitshilfe. Ihr Prüfjournal ist keine gerichtlich vorgeschriebene zusätzliche Form. Die eigene menschliche Prüfung darf weder aus einer Signatur fingiert noch durch einen automatischen Freigabeeintrag ersetzt werden.

## 3. Redaktionelle Gegenprüfung und Modellanwendung

Alle elf Skills behalten sechs Hauptabschnitte, A-/F-/Q-Kennungen und fünf getrennte Fundstellendimensionen. Die unabhängige redaktionelle Gegenprüfung umfasste die geänderten Skills, Prompts, Referenzen, Befehle und das README. Ein konkreter Befund wurde korrigiert: Die Mini-Fassung darf einen bloß unverifizierten Altbeleg beim Einsetzen einer Ersatzquelle nicht pauschal als falsch bezeichnen. Der frühere Befund bleibt erhalten.

Das [Prüfprofil](../evals/ki-halluzinationsreduzierer.json) enthält 14 Ergebnisfälle. Die ursprüngliche [Anwendungsprobe mit sechs simulierten Evidenzlagen](anwendungsprobe.md) bleibt als historischer Nachweis der Erstfassung erhalten. Die ergänzende [Rechtsprechungs-Anwendungsprobe](rechtsprechung-anwendungsprobe-2026-10-19.md) dokumentiert acht tatsächlich formulierte Modellantworten mit 24 Kriterien. Alle 24 lokalen Kriterien sind in der redaktionellen Selbstprüfung erfüllt; sie sind nicht wortgleich mit dem Eval-Profil und belegen keinen vollständigen Modell-Pass seiner 14 Fälle. Ein gesondert dokumentierter Nachtest des BAG-Falls erfüllt drei von drei unveränderten finalen Profilkriterien. Es handelt sich weder um unabhängige Blindtests noch um App-, Versand- oder Gerichtsversuche.

## 4. Technische Abnahme

Die Komponentenprüfung umfasst acht Tests: Manifeste und Marketplace-Version, genau elf Skills und deren Struktur, lokale Verweise, identische Promptpaare und Prüfhashes, Erkennung fehlender PDF-Inhalte, Release-Inventar, bytegenaue ZIP-Inhalte sowie PDF-Text, Schrift und Seitenbegrenzungen. Der finale Build enthält dreizehn Assets. Mini und Hauptproblem bleiben auch mit CRLF-Zeilenenden unter 7.500 UTF-8-Bytes.

Zusätzlich werden Pluginstruktur, Marketplace-Import, Frontmatter, Skill-Aktivierung, Qualitätsprofile, Fachprofilzuordnung, Prompt-Einstiege, Routing, Markdownstruktur und zentrale Navigation geprüft. Die ausgeführten Prüfbefehle und abschließenden Ergebnisse stehen in Abschnitt 6. Automatische Prüfungen ersetzen keine eigene rechtliche Bewertung.

## 5. Umfang und Lesefassungen

Die elf Skills enthalten zusammen 13.651 Wörter Textkörper. Die Werkstatt umfasst 30 Kapitel und 6.821 Wörter; der Mini enthält 7.418 UTF-8-Bytes mit LF beziehungsweise 7.483 mit CRLF. Der Hauptproblem-Prompt hat 7.361 Bytes mit CRLF. Die Lesefassungen umfassen 17, drei und drei Seiten und verwenden lokal Times New Roman, 11 pt. Einzelwerte stehen in [umfang.json](umfang.json).

Beim ersten PDF-Abgleich fiel der enge Normenblock auf; er wurde in lesbare Absätze überführt. Die Sichtprüfung erkannte außerdem nicht interpretierte Markdown-Unterüberschriften. Diese wurden im Prompt mit einer unterstützten Überschriftsebene und unveränderter dezimaler Nummerierung gesetzt. Der finale Textabgleich weist keine fehlenden Wörter, fehlenden Glyphen oder Inhalte außerhalb der Seiten aus. Die [PDF-Sichtprüfung](pdf-sichtpruefung.md) dokumentiert die tatsächlich geprüften Fassungen getrennt nach Version.

## 6. Prüfbefehle der Fassung 1.1.0

Alle nachfolgend aufgeführten Prüfungen sind am 19.10.2026 erfolgreich abgeschlossen. Die Komponentenprüfung bestand acht Tests; die Navigation 51 Tests und das komponentenbezogene Release-Routing elf Tests. Eine veraltete Gesamtzahl in der zentralen Promptliste wurde von 303 auf 304 Plugins berichtigt. Der Navigationsvalidator prüfte 43.692 lokale Links und 2.206 Anker.

| Prüfung | Befehl |
| --- | --- |
| Komponente und Pakete | `python3 scripts/test-ki-halluzinationsreduzierer.py --dist /tmp/halluzination-release-1.1.0` |
| Plugin und Marketplace | `node scripts/validate-plugin-structure.mjs`; `node scripts/validate-marketplace-import.mjs` |
| Frontmatter und Aktivierung | `python3 scripts/validate-yaml-frontmatter.py`; `python3 scripts/audit-skill-activation.py` |
| Qualitäts- und Fachprofile | `python3 scripts/quality-lab.py audit --require-editorial --require-workflow`; `python3 scripts/audit-prompt-profile-routing.py` |
| Promptablauf und Routing | `python3 scripts/test-prompt-openings.py`; `python3 scripts/test-prompt-routing-scope.py`; `python3 scripts/test-scoped-release-routing.py` |
| Übersichten und Navigation | `python3 scripts/validate-root-readme-overview.py`; `python3 scripts/validate-readme-navigation.py`; `python3 scripts/test-readme-navigation.py` |
| Markdown und Diff | `python3 scripts/validate-markdown-structure.py`; `git diff --check` |

Die Prüfumgebung verwendet zusätzlich die in der Sitzung installierten Parserabhängigkeiten; die PDF-Bibliotheken stammen aus der lokalen Laufzeit. Keine Prüfbefehle erteilen eine Einreichungsfreigabe.
