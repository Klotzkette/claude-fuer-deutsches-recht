# 1. Gesellschafterstreit – Erweiterung 445.34.1

## 1.1. Umfang und Erhaltung

Redaktioneller Abschluss: 09.10.2026. Die elf bestehenden Skills bleiben erhalten. Ihre Abläufe, die drei eigenständigen Prompts und vier Fachreferenzen wurden vertieft. Die drei bisherigen Testakten erhalten jeweils einen getrennten Nachtrag; die 76 bisherigen Originaldateien werden anhand unabhängiger SHA-256-Werte unverändert erhalten. Die einfachen Einstiege bleiben weiterhin verwendbar.

Die Erweiterung enthält 60 zusätzliche Dateien: 18 Word-Dokumente mit 18 inhaltsgleichen PDF-Lesefassungen, 18 E-Mails mit eingebetteten Anhängen, drei Excel-Arbeitsmappen und drei Chat-Texte. Insgesamt stehen damit 136 Originaldateien zur Verfügung. Word und PDF desselben Dokuments zählen als zwei Dateien, nicht als zwei verschiedene Sachbelege.

## 1.2. Fachliche Prüfung

Der [Quellenbericht](../source-audits/gesellschafterstreit-2026-10-08/quellenbericht.md) dokumentiert 18 am amtlichen Volltext geprüfte BGH-Entscheidungen, darunter drei neu aufgenommene Entscheidungen von 2026. Die 15 früheren Originale wurden erneut geladen und mit identischen Hashes bestätigt. [Fachbefund](../source-audits/gesellschafterstreit-2026-10-08/fachbefund.md), Originalarchive und Normenregister zeigen konkrete Anwendung und Grenzen.

Die neuen Anker betreffen Beschlussfassung bei entsprechender Satzung, Mitgliedschaftsfeststellung trotz positiver Liste und die getrennte Prüfung von Leaver-Klausel, Preis und Ausübung. Kein Anker beruht nur auf einem Suchauszug. Nicht im Original zugängliche Recherchehinweise wurden nicht als bestätigte Rechtsprechung übernommen. Eine vollständige Erfassung aller veröffentlichten Entscheidungen wird nicht behauptet.

## 1.3. Prompts und Arbeitsprodukte

Mini und Hauptproblem bleiben unter 7.500 UTF-8-Bytes; alle drei MD/TXT-Paare sind byteidentisch. Die Werkstatt enthält zusätzliche vollständige Abläufe für Klageerwiderung und ein abgestimmtes gesellschaftsrechtliches Regelungswerk. Fristmaßstab, konkrete Stimmverbote, Beweisgrenzen, Anspruchsinhaber, Verfahrenswahl und Vollzug werden getrennt behandelt.

Das [Prüfprofil](../evals/gesellschafterstreit.json) führt frühere Probeläufe mit ihren damaligen Hashes fort. Historische Erfolge werden nicht auf geänderte Prompts übertragen. Die neue Prüfung ist ausdrücklich nach Textprüfung, technischer Kontrolle und tatsächlicher Anwendungsprobe getrennt.

## 1.4. Lesefassungen

Das Skill-Handbuch umfasst 22 Seiten, die Werkstatt-Lesefassung 27 Seiten. Beide wurden mit Times New Roman gesetzt. Vollständige Quelltextabdeckung, alle 49 Seiten auf leere Seiten und außerhalb der Seite liegende Textspannen sowie acht ausgewählte Seiten visuell geprüft. Nach Korrektur der Quellenstands-Fußzeile auf 08./09.10.2026 wurden beide Titelseiten nochmals visuell geprüft. Die Dateien sind Lesefassungen der Instruktionen, keine neuen Fachgutachten.

## 1.5. Prüfabschluss

Der [Aktenbericht](akten-nachtrag.md) dokumentiert 63 Formeln, 33 Rechenkontrollen, zwölf native Eingabeproben sowie alle 18 MIME-Anhänge. Die Gesamtakten umfassen 46 Seiten (Berlin), 42 Seiten (München) und 72 Seiten (Zink und Zunder). Alle 160 Seiten bestanden die Leer- und Seitengrenzenprüfung; sechs ausgewählte Seiten wurden zusätzlich von der Hauptprüfung angesehen, darunter alle drei neuen Finanzblätter. Details stehen im [Layoutprotokoll](pdf-layout.json).

Bestanden sind Frontmatter-Prüfung, Plugin-Struktur, fünf Marketplace-Tests, Markdown-Struktur, Root-README-Übersicht, sechs Routingtests und elf Office-Resilienztests. Das individuelle Qualitätsprofil einschließlich fachbezogener Redaktion ist gültig. Alle zehn Tests von `scripts/test-gesellschafterstreit-update.py --dist /tmp/gs-dist-final` sind bestanden: 136 Originaldateien, 42 eigenständige E-Mails, 30 byteidentische Anhänge, Original-/Einzel-PDF-Archive und alle 19 Release-Dateien. Die bestehende Vorführakten-Suite besteht mit 17 erfolgreichen Tests und einer optionalen, nicht ausgeführten Altarchivprüfung. Die neue Suite prüft die tatsächlich gebauten aktuellen Archive vollständig.

Ein nachgewiesener Fehler der neuen DOCX/PDF-Inhaltsprüfung wurde gezielt korrigiert: Laufende Seitenzahlen zwischen fortgesetzten Absätzen werden nur bei wiederkehrender geometrischer Randposition aus dem Textvergleich ausgenommen. Die Regression scheiterte mit der alten Extraktion und besteht mit dem Helfer. Reguläre Zahlen, Beträge und Aktenkennungen bleiben geprüft; zentrale Validatoren wurden nicht geändert.

Die [aktuelle Berliner Anwendungsprobe](anwendungsprobe-berlin/Lese_und_Werkzeugbericht.md) wurde mit dem Mini-Prompt und allen 40 nativen Dateien durchgeführt, ohne Bewertungsunterlagen oder Musterlösung. [Klageerwiderung](anwendungsprobe-berlin/Klageerwiderung.md), [interne Notiz](anwendungsprobe-berlin/Interne_Notiz.md) und [Exporthinweis](anwendungsprobe-berlin/Exporthinweis.md) liegen getrennt vor. Die Hauptprüfung hat die Produkte vollständig gelesen. Alle fünf neu definierten Nachtragskriterien sind in diesem konkreten Durchlauf erfüllt: Mandat/Fristen, substantiierte Erwiderung und Beweisgrenzen, korrigierte Gerätezuordnung, offengelegte Cent-Differenz ohne erfundene Forderung sowie konkrete Anlagenzuordnung und rechtliche Begründung. Die alternative Stimmenrechnung, Prozessvertretung und Fortbestand des Anstellungsvertrags sind zusätzlich behandelt.

Die Probe ist ein einzelner Agentendurchlauf, kein Vergleich verschiedener Modelle und kein erneuter vollständiger Durchlauf der historischen Zink-Kriterien. Offene Zeugenanschriften, Originalexporte, Vollmacht und tatsächlicher Gerichtseingang bleiben ausdrücklich offen. Kein Cowork-/Codex-Import oder tatsächlicher Versand wurde getestet. Die amtlichen Quellen der Probe liegen platzsparend als gzip mit Originalhashes in ihrer Quellenmappe; die PDF-/HTML-Endung ist vor Öffnung durch Dekomprimieren wiederherzustellen.

Drei globale Prüfungen enthalten unveränderte Befunde außerhalb dieser Erweiterung: Dem Plugin `kanzlei-website-redaktion` fehlt das individuelle Qualitätsprofil; eine Beschreibung in `ki-native-kanzlei` überschreitet 360 Zeichen; der globale Navigationsprüfer meldet neun bestehende Link-/Downloadwegprobleme in anderen Bereichen. Diese Befunde bestanden bereits im Ausgangscommit und werden nicht als bestanden ausgegeben. Gesellschafterstreit ist in diesen Fehlermeldungen nicht betroffen. Reale Einreichungen, Nachrichten oder Registerhandlungen gehören nicht zu dieser Prüfung.

## 1.6. Nachprüfung des Linux-Releasebaus

Der erste GitHub-Lauf `37854258087` bestand die Quellenprüfungen und baute 19 Dateien, stoppte aber vor Veröffentlichung: Die alte Berliner Tabelle `19_Projektkonto.xlsx` wurde unter Linux in der Einzel-PDF auf 8,906 pt verkleinert. Die Mindestprüfung von 9 pt blieb aktiv; weder Originaldatei noch Grenzwert wurde geändert. Der Build erhält deshalb ausdrücklich freie Ersatzschriften und eine feste Fontconfig-Zuordnung für Arial, Times New Roman und Calibri. Ein Fehlerartefakt ermöglicht bei erneutem Scheitern die Sichtprüfung der tatsächlichen Linux-Ausgabe. Der erneute GitHub-Lauf wurde vollständig bestanden; der Abschluss ist nachstehend dokumentiert.

## 1.7. Veröffentlichung und öffentlicher Download-Abgleich

Am 09.10.2026 wurde die Komponentenfassung [445.34.1](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/gesellschafterstreit-v445.34.1) veröffentlicht. Der [GitHub-Lauf 37855136076](https://github.com/Klotzkette/claude-fuer-deutsches-recht/actions/runs/37855136076) bestand Quellenprüfung, PDF-/Paketbau und Veröffentlichungsprüfung. Alle 19 Dateien wurden anschließend über die öffentlichen Download-URLs ohne Authentifizierung erneut geladen; alle 18 aufgeführten SHA-256-Prüfsummen stimmen. Die zehn Komponententests wurden gegen diese heruntergeladenen Pakete wiederholt und vollständig bestanden. Versionsstand, Release-Commit, Dateigrößen und Hashes stehen im [Verifikationsprotokoll](release-445.34.1-verifikation.json).

Die zuvor betroffene Linux-Lesefassung `19_Projektkonto.pdf` enthält nach Installation von Carlito und der systemweiten Schriftzuordnung wieder mindestens 10,006 pt große Schrift. Die tatsächliche öffentliche PDF wurde zusätzlich visuell geprüft: eine vollständige, lesbare Seite ohne abgeschnittene Inhalte. Originale, Prüfschwelle und zentrale PDF-Validatoren blieben unverändert. Die in Abschnitt 1.5 genannten globalen Befunde außerhalb des Plugins werden durch diese erfolgreiche Komponentenveröffentlichung nicht als behoben ausgegeben.
