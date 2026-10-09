# 1 KI-Verordnung Hochrisiko-Prüfer

[Repository-Start](../README.md) · [Alle Skills](../SKILLS.md) · [Skill-Detailseite](../skills-index/ki-verordnung-hochrisiko-pruefer.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [Plugin-Dateien](.)

Version 445.35.0, Rechtsabgleich vom 9. Oktober 2026. Zehn Fachskills und ein elfter Hauptproblem-Skill prüfen die konkrete Funktion einer KI nach Artikel 6. Der vorhandene Recruiting-Schwerpunkt bleibt erhalten; Justizassistenz und Medizinprodukt ergänzen ihn um zwei eigenständige Fallakten.

## 2 Einstieg und Arbeitsweise

Für eine reine Einstufung verwenden Sie den Skill **Artikel 6 Software einstufen**. Für einen Vorgang mit Unterlagen, Rückfragen und fertigen Dokumenten beginnen Sie mit **Hochrisikofrage lösen**. Geben Sie den vorhandenen Ordner und das gewünschte Ergebnis an: beispielsweise Einstufungsvermerk, Anbieteranschreiben oder Entscheidungsvorlage. Die Unterlagen werden zuerst ausgewertet; nur entscheidende fehlende Angaben werden nachgefragt. Ein neuer Beleg setzt die Prüfung an der betroffenen Stelle fort.

Claude Cowork und Claude Code können das Plugin mit seinen Skills verwenden. Für Codex enthält es zusätzlich ein eigenes Manifest. In ChatGPT verwenden Sie den Mini-Prompt als Projektanweisung und Werkstatt sowie Referenzen als Dateien. Dateierzeugung und Dateizugriff hängen von der tatsächlich verfügbaren Umgebung ab. Ohne diese Fähigkeiten werden ausformulierte Dokumenttexte geliefert; ein erzeugtes Word-Dokument, Registereintrag oder versandtes Schreiben wird nicht vorgetäuscht.

[Workflow, Produkte und Übergaben](references/workflow-und-uebergaben.md) halten Zweckfassung, Belegstand, offene Fragen und nächsten Bearbeitungsschritt zusammen. Außenwirksame Maßnahmen benötigen einen konkreten Auftrag und eine dokumentierte menschliche Freigabe.

## 3 Die elf Skills

| Skill | Aufgabe | Ergebnis |
|---|---|---|
| [Hochrisikofrage lösen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hochrisikofrage-loesen/SKILL.md) | Führt die zehn Fachwege durch den konkreten Vorgang | Vollständiges Dokument und fortsetzbarer Stand |
| [Artikel 6 Software einstufen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/artikel-6-software-einstufen/SKILL.md) | Prüft ausschließlich die Einstufung einschließlich aller Anhang-III-Bereiche | Begründeter Einstufungsvermerk |
| [Produktpfad und Sicherheitsbauteil prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/produktpfad-sicherheitsbauteil-pruefen/SKILL.md) | Prüft Anhang I, Sicherheitsfunktion und vorgeschriebene Drittbewertung | Produktpfadvermerk mit Nachforderungen |
| [HR-Zweck und Systemabgrenzung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hr-zweck-und-systemabgrenzung/SKILL.md) | Trennt Funktionen, Versionen und tatsächliche Nutzung | System- und Zweckvermerk |
| [Recruiting einstufen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hochrisiko-einstufung-recruiting/SKILL.md) | Prüft Auswahl, Ranking und tatsächlichen Einfluss | Recruiting-Einstufung |
| [Ausnahme begründen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/ausnahmebegruendung-artikel-6/SKILL.md) | Prüft vier Alternativen, Risikokontext und Profiling | Tragfähige Ausnahmeprüfung oder Ablehnung |
| [Rollenwechsel und Shadow AI](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rollenwechsel-und-shadow-ai/SKILL.md) | Prüft Übernahme, Zweckänderung und konkrete Anbieterrolle | Rollenvermerk und Sicherungsanweisung |
| [Konformität und Registrierung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/konformitaet-und-registrierung/SKILL.md) | Ordnet Folgewege getrennt zu | Anbieteranschreiben und Nachweisliste |
| [Betreiberkonzept Bewerberauswahl](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/betreiberkonzept-bewerbungsauswahl/SKILL.md) | Macht menschliche Aufsicht im tatsächlichen Ablauf überprüfbar | Betriebsanweisung |
| [Vorfall bewerten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/vorfallbewertung-und-meldeentwurf/SKILL.md) | Trennt Ereignis, Vorfall, Informationsweg und Meldung | Vorfallvermerk oder Meldeentwurf |
| [Rechtsstand und Einführung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rechtsstand-und-einfuehrungsentscheidung/SKILL.md) | Prüft Fassung, Artikel 111/113 und Änderungen im Bestand | Einführungsentscheidung mit offenen Voraussetzungen |

## 4 Prompts und Installation

| Fassung | Lesen | Textdatei |
|---|---|---|
| Mini-Prompt | [Schnellstart](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-schnellstart.md) | [TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-schnellstart.txt) |
| Großer Werkstatt-Prompt | [Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-werkstatt.md) | [TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-werkstatt.txt) |
| Hauptproblem-Prompt | [Hauptproblem](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-hauptproblem.md) | [TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-hauptproblem.txt) |

Mini und Hauptproblem passen jeweils in 7.500 UTF-8-Bytes. Alle drei MD/TXT-Paare enthalten identischen Text. Die Werkstatt behandelt beide Einstufungspfade, sämtliche Katalogbereiche, vier Ausnahmealternativen, Profiling und die Fortsetzung nach neuen Belegen ausführlich.

[Plugin-ZIP der Komponentenfassung 445.35.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.0/ki-verordnung-hochrisiko-pruefer.zip)

## 5 Fachlicher Stand und konkrete Grenzen

Gelesen wurden die amtliche konsolidierte KI-Verordnung in der Fassung vom 27. Juli 2026 und die deutsche Berichtigung vom 29. September 2026. Artikel 6 Absatz 1b gilt **ungeachtet** des Absatzes 1a: Eine bloße Bezeichnung als Komfortfunktion entkräftet mögliche gesundheits- oder sicherheitsgefährdende Ausfallfolgen nicht. Die vier Alternativen des Absatzes 3 betreffen den Anhang-III-Pfad; sie befreien keinen Produktpfad nach Absatz 1. Profiling natürlicher Personen sperrt die Ausnahme innerhalb des Anhang-III-Pfads.

Die Registrierung der dokumentierten Ausnahme nach Artikel 6 Absatz 4 und Artikel 49 Absatz 2 ist vereinfacht, nicht abgeschafft. Artikel 113 verschiebt die bezeichneten Abschnitte 1 bis 3 des Kapitels III, nicht pauschal jeden Artikel der Verordnung. Die konkrete Verzahnung mit Bestandsschutz, Konformität, Registrierung und Meldung muss begründet werden. [Quellen, Rechtsstand und Reichweite](references/rechtsstand-und-quellen.md) sowie [vollständiger Einstufungskatalog](references/artikel-6-und-anhang-iii.md) erläutern dies.

Risikomanagement nach Artikel 9, Qualitätsmanagement nach Artikel 17, Grundrechte-Folgenabschätzung nach Artikel 27 und technische beziehungsweise betriebliche menschliche Aufsicht werden getrennt behandelt. Ein ISO-Zertifikat, allgemeines Risikoregister oder Etikett „Agent“ beantwortet die Einstufung nicht. Der übernommene EuGH-Anker C-634/21 betrifft Artikel 22 DSGVO, keine Entscheidung zu Artikel 6 KI-Verordnung. Für ein Medizinprodukt bleiben das aktuelle Produktrecht, die tatsächliche Zweckbestimmung und der zutreffende Bewertungsweg gesondert zu prüfen.

## 6 Testakten

Die bestehende Akte Kassel bleibt vollständig erhalten. Die zwei Ergänzungen enthalten jeweils zwölf native Arbeitsdateien: vier E-Mails, drei Word-Dokumente, drei PDF-Belege, eine Excel-Arbeitsmappe mit zwei Blättern und einen Chattext. Je zwei E-Mails haben echte Anhänge; diese Anhänge sind mit den separat vorhandenen Dateien identisch. Die Tabellen enthalten Formeln und Quellenhinweise. Die Prüfentwürfe sind ausformulierte Arbeitsstände mit offenen Tatsachen, keine Lösungsschlüssel.

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fallakte | Bearbeitungsanlass | Einstieg |
|---|---|---|
| Bewerbungsauswahl Kassel | Ranking, verdeckte Vorauswahl, Privatprompt und Einführung | [README und Downloads](../testakten/ki-hochrisiko-bewerbungsauswahl-kassel/README.md) |
| Justizassistenz Jena | Register 1.4, Entscheidungsentwurf 2.0 und personenbezogene Kennzeichnung 2.1 | [README und zwölf Dateien](../testakten/ki-hochrisiko-justizassistenz-jena/README.md) |
| Medizinprodukt Saalfeld | Archivfunktion, diagnostische Assistenz und noch offene Produktklassifizierung | [README und zwölf Dateien](../testakten/ki-hochrisiko-medizinprodukt-saalfeld/README.md) |

## 7 Prüfung und Grenzen des Nachweises

Das [Prüfprofil](../quality/evals/ki-verordnung-hochrisiko-pruefer.json) enthält positive und negative Einstufungsfälle, Dokumentaufträge und getrennte Bewertungskriterien. Der [Fach- und Dateiprüfbericht](../quality/ki-verordnung-2026-10-09/hochrisiko/README.md) dokumentiert Quellenlesung, Hashes, native Dateiprüfung und visuelle Kontrolle. Redaktionelle Prüfung und lokale Regressionen sind keine Aussage über eine erfolgreiche Live-Ausführung in einem bestimmten Client. Nur tatsächlich verfügbare Werkzeuge verwenden und keine Freigabe, Zertifizierung oder Registrierung behaupten, die nicht erfolgt ist.

## 9. PDF-Lesefassungen und Prüfbericht

[Skills-Handbuch](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.0/ki-verordnung-hochrisiko-pruefer-skills-handbuch.pdf) · [Werkstatt-Lesefassung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.0/ki-verordnung-hochrisiko-pruefer-werkstatt-lesefassung.pdf) · [Prüfbericht](../quality/ki-verordnung-2026-10-09/README.md)
