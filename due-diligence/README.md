# 1. DD – Due Diligence

DD prüft Unternehmen, Beteiligungen, Personal und Kreditportfolios aus Sicht des Käufers oder Investors und unterstützt ebenso die vorbereitende Verkäuferprüfung. Zehn Fachskills und ein steuernder Hauptskill führen von der belegten Schnellprüfung über Excel-Auswertung und Rückfragen bis zur Entscheidungsvorlage, Kaufpreisüberleitung und konkreten Vertragsregelung.

Das Ziel lautet: Was wird tatsächlich übernommen, welche Belastungen sind belegt, welche Zahlen stimmen und was muss vor dem Erwerb noch geklärt oder abgesichert werden? Ein Datenraumbericht wird nicht mit einer geprüften Bilanz, einem vollständigen Rechtsgutachten zu jedem Nebengebiet oder einer automatischen Kaufentscheidung gleichgesetzt.

## 1.1. Einstieg

Installieren Sie das Plugin in einer unterstützten Umgebung oder verwenden Sie einen der eigenständigen Prompts. Stellen Sie Auftrag und Unterlagen bereit und schreiben Sie beispielsweise:

> Ich vertrete die Käuferin. Prüfen Sie zunächst, was wir aus dieser Akte tatsächlich über die Gesellschaft und den Personalbestand wissen. Erstellen Sie eine nachvollziehbare Excel mit Belegen, offenen Punkten und Kostenfolgen. Formulieren Sie anschließend die wichtigsten Rückfragen an die Verkäuferseite. Der Erwerbsumfang ist im beigefügten Angebot beschrieben.

Das System liest vorhandene Angaben zuerst und klärt nur entscheidende Lücken. Wählbar sind Schnellprüfung, vertiefte Fachprüfung und Entscheidungsvorlage. Nach einer Antwort oder neuen Unterlage setzt es am dokumentierten Stand fort. Interne Prüfung und Berechnung laufen innerhalb des Auftrags weiter; externe Anfragen, Datenweitergabe und rechtsgeschäftliche Zusagen verlangen eine passende menschliche Freigabe.

## 1.2. Plugin und Prompts

Komponentenfassung **1.0.0**, Quellen- und Bearbeitungsstand 10. Oktober 2026. Das installierbare Plugin enthält Skills, Referenzen und Befehle. Testakten und eigenständige Prompts sind getrennte Downloads. Die Akten enthalten Übungsmaterial und werden nicht bei jedem Start ungefragt in den Arbeitskontext geladen.

| Zugang | Inhalt | Download |
| --- | --- | --- |
| Plugin | Elf Skills, Referenzen und Befehle | [Installierbares ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/due-diligence-v1.0.0/due-diligence.zip) |
| Portable Ablage | Derselbe Pluginbestand mit übergeordnetem Ordner | [Portable ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/due-diligence-v1.0.0/due-diligence-portable.zip) |
| Werkstatt | 25 Kapitel mit Arbeitsschritten und Rückfrageschleifen | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/due-diligence-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/due-diligence-werkstatt.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/due-diligence-v1.0.0/due-diligence-werkstatt.pdf) |
| Schnellstart | Kompakter Ablauf bis zum bestellten Produkt | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/due-diligence-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/due-diligence-schnellstart.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/due-diligence-v1.0.0/due-diligence-schnellstart.pdf) |
| Hauptproblem | Was erwerben wir und zu welchen Bedingungen? | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/due-diligence-hauptproblem.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/due-diligence-hauptproblem.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/due-diligence-v1.0.0/due-diligence-hauptproblem.pdf) |

Mini- und Hauptproblem-Prompt bleiben jeweils innerhalb von 7.500 UTF-8-Bytes. Markdown und Text sind byteidentisch. Für ChatGPT kann der Schnellstart als Projektanweisung dienen; Werkstatt und benötigte Referenzen werden als Projektdateien ergänzt. Verfügbarkeit von Dateiexport, Webrecherche, Kontextgröße und Befehlsdarstellung hängt vom jeweiligen Produkt ab. Ein Plugin-ZIP garantiert keinen direkten Import in jede ChatGPT-Oberfläche.

## 1.3. Arbeitsprodukte

Das Plugin erstellt eine belegte Übersicht, ein Befund- und Dokumentenregister, eine Personal- oder Kreditmatrix, Zahlenüberleitungen und konkrete Rückfragen. Bei entsprechendem Auftrag folgen ein vollständig formulierter DD-Bericht, ein Mandanten- oder Verkäuferanschreiben und ausformulierte Vertragsvorschläge. Preisannahmen, Garantien, Freistellungen, Bedingungen vor Vollzug und spätere Maßnahmen werden getrennt behandelt.

Die [Arbeitsweise](references/arbeitsweise.md) definiert Phasen, Übergaben und Freigaben. Das [Excel- und Befundschema](references/befund-und-excel-schema.md) hält Kennungen, Datenstatus und Rechenlogik zusammen. Die [Rechtsquellen](references/rechtsquellen.md) unterscheiden gelesene Normen, begrenzte Entscheidungsanker und im Einzelfall erneut zu prüfende Fragen. Ein Quellenabruf ist keine Zertifizierung aller möglichen Anwendungen.

## 1.4. Drei Testakten

Die beiden vorhandenen Akten werden als eigene DD-Akten gespiegelt; die ursprünglichen Akten bleiben erhalten. Der [SHA-256-Spiegelnachweis](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/quality/due-diligence/spiegelung.json) dokumentiert die Byteidentität sämtlicher übernommenen nativen Dateien. Historische Aktenbehauptungen und Bewertungen bleiben Prüfgegenstand; sie sind keine verifizierten Rechtsquellen.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Prüffokus | Unterlagen und Downloads |
| --- | --- | --- |
| Innovation Systems Berlin | 50 Arbeitsverträge, zwei gesonderte Geschäftsführeranstellungen, Personal- und Zahlungsabgleich beim geplanten Betriebserwerb | [README mit Original-ZIP, Einzel-PDFs und Gesamt-PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/dd-arbeitsvertraege-innovation-berlin/README.md) |
| Silberfalke | Gesellschaftsstruktur, Ausgliederung, M&A-Datenraum, Q&A, finanzielle Angaben und Kaufvertragsmechanik | [README mit Original-ZIP, Einzel-PDFs und Gesamt-PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/dd-corporate-silberfalke/README.md) |
| Englische Bank mit Filiale Erfurt | Portfolio von 1.000 Verbraucherdarlehen mit 20 vertieften Kreditakten, Forderungsrechnung, Übertragung und Servicing | [README mit Original-ZIP, Einzel-PDFs und Gesamt-PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/dd-bankfiliale-verbraucherdarlehen-erfurt/README.md) |

Innovation Systems umfasst 110 exportierbare Arbeitsunterlagen. Silberfalke umfasst 55 exportierbare Arbeitsunterlagen und enthält bereits historische DD-Bewertungen; es ist daher ausdrücklich eine Nachprüfungs- und Lernakte. Die Bankakte verwendet eine bewusste Auswahl unterschiedlicher Risiken. 20 Detailfälle sind ohne Auswahl- und Hochrechnungsmethode keine repräsentative Aussage über alle 1.000 Darlehen.

Verwenden Sie für eine Analyse entweder Originale, Einzel-PDFs oder Gesamt-PDF. Das zusätzlich im Original-ZIP enthaltene Gesamt-PDF wird bei Einzeldateiauswertung nicht nochmals als unabhängige Quelle eingelesen. Die Fallstichtage bleiben akteneigen; das Veröffentlichungsdatum verschiebt sie nicht.

## 1.5. Was bei der Bankakte zu unterscheiden ist

Forderungskauf, vollständige Vertragsübernahme und Erwerb eines Filialbetriebs sind unterschiedliche Gegenstände. Das Plugin prüft ursprünglichen Kreditgeber, deutsche Zweigstelle, Erwerber und Dienstleister gesondert. Es unterscheidet laufende und notleidende Kredite, Buchsaldo und Rechtsanspruch, Rückstand und Gesamtfälligkeit, Titel und tatsächliche Einbringlichkeit sowie Insolvenz und Restschuldbefreiung. Eine englische Herkunft bewirkt weder einen automatischen EU-Pass noch den pauschalen Ausschluss des Kreditzweitmarktgesetzes.

Der Überblick soll schnell entstehen; die behauptete Prüfungstiefe muss dem tatsächlich gelesenen Bestand entsprechen. Fehlende Nachweise bleiben sichtbar. Tabellenformeln ersetzen keine Rechtsprüfung, und ein Verkäufermemo ersetzt keinen Originalbeleg.

## 1.6. Installation und Befehle

In Claude Code oder einer passenden Cowork-Installation dienen `/dd`, `/dd-schnellpruefung`, `/dd-rueckfragen` und `/dd-entscheidung` als Einstieg. In Codex oder ChatGPT können Sie dieselben Wörter als normale Arbeitsaufträge verwenden, wenn keine Slash-Befehle angezeigt werden. Die Beispiele beschreiben die beabsichtigte Nutzung; eine identische Bedienoberfläche in allen Produkten wird nicht zugesagt.

Lesefassungen verwenden Times New Roman 11 pt, soweit verfügbar. Der Linux-Releasebuild verwendet andernfalls Liberation Serif mit ausdrücklichem Schriftvermerk. Die technischen Prüfungen und ihre Grenzen stehen im [Prüfbericht](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/quality/due-diligence/README.md).


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`auftrag-transaktion-abgrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/auftrag-transaktion-abgrenzen/SKILL.md) | Legt Mandatsseite, Erwerbsstruktur, Prüfbestand, Wesentlichkeit und Entscheidungsziel einer Due Diligence fest. Erstellt einen konkreten Prüfauftrag mit Zeitplan, Verantwortlichkeiten und begründeten Prüfgrenzen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/auftrag-transaktion-abgrenzen/SKILL.md) |
| [`befunde-qa-verfolgen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/befunde-qa-verfolgen/SKILL.md) | Konsolidiert DD-Feststellungen zu belegten Befunden und präzisen Rückfragen. Prüft Antworten gegen Originalunterlagen, verfolgt Zuständigkeit und Nachweise und verhindert unbegründete Erledigung oder doppelte Risikozählung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/befunde-qa-verfolgen/SKILL.md) |
| [`bilanz-finanzierung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/bilanz-finanzierung-pruefen/SKILL.md) | Gleicht Jahresabschluss, Konten, offene Posten und Zahlungsbelege ab. Trennt Buchwert, Liquidität und Unternehmenswert und erstellt erklärte Excel-Brücken für Nettoverschuldung, Betriebskapital und erkennbare Finanzierungsrisiken. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/bilanz-finanzierung-pruefen/SKILL.md) |
| [`datenraum-belege-ordnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/datenraum-belege-ordnen/SKILL.md) | Erfasst Datenraumdateien, Originale, Anhänge, Fassungen und Offenlegungszeitpunkte. Erstellt einen belastbaren Index mit Lücken und Nachweisen, damit jede DD-Aussage auf eine auffindbare Quelle zurückgeführt werden kann. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/datenraum-belege-ordnen/SKILL.md) |
| [`due-diligence-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/due-diligence-steuern/SKILL.md) | Steuert die Käufer-, Investoren- oder Verkäuferprüfung eines Unternehmens, Betriebs oder Kreditportfolios. Verbindet zehn Fachskills zu belegter Analyse, Excel-Abgleich, Rückfragen, Vertragsabsicherung und Vollzugsentscheidung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/due-diligence-steuern/SKILL.md) |
| [`gesellschaft-beteiligungen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/gesellschaft-beteiligungen-pruefen/SKILL.md) | Prüft Gesellschaftsbestand, Beteiligungskette, Gesellschafterlisten, Einlagen, Beschlüsse und Vertretungsmacht für Unternehmens- und Beteiligungskäufe. Übersetzt ungeklärte Eigentums- und Zustimmungslagen in konkrete Vollzugsbedingungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/gesellschaft-beteiligungen-pruefen/SKILL.md) |
| [`kaufentscheidung-absichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/kaufentscheidung-absichern/SKILL.md) | Übersetzt verifizierte DD-Befunde in eine verständliche Kaufentscheidung, Preisfolgen, Garantien, Freistellungen und Vollzugsbedingungen. Erstellt vollständige Entwürfe und verfolgt den Nachweis ihrer Erfüllung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/kaufentscheidung-absichern/SKILL.md) |
| [`kreditportfolio-uebertragen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/kreditportfolio-uebertragen/SKILL.md) | Prüft Übertragungsgegenstand, Abtretungskette, Sicherheiten, Kreditdienstleistung und Vollzugsorganisation eines Kreditportfolios. Trennt leistungsfähige und notleidende Kredite, Erlaubnisfragen, Schuldnerschutz und Datenübergabe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/kreditportfolio-uebertragen/SKILL.md) |
| [`personal-arbeitsvertraege-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/personal-arbeitsvertraege-pruefen/SKILL.md) | Prüft jeden vorgelegten Arbeitsvertrag samt Nachträgen, Personalkosten und Zuordnung beim Betriebsübergang. Erkennt Nebenabreden, Übernahmerisiken und Datenlücken und erstellt eine erklärte Excel-Personalübersicht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/personal-arbeitsvertraege-pruefen/SKILL.md) |
| [`verbraucherdarlehen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/verbraucherdarlehen-pruefen/SKILL.md) | Prüft Verbraucherdarlehen vom Vertrag über Zahlung, Stundung und Kündigung bis Titel oder Insolvenz. Rekonstruiert den rechtlich prüfbaren Saldo und trennt Forderungsbestand, Durchsetzbarkeit und wirtschaftlichen Rückfluss. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/verbraucherdarlehen-pruefen/SKILL.md) |
| [`vertraege-vermoegen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/vertraege-vermoegen-pruefen/SKILL.md) | Prüft wesentliche Kunden-, Liefer-, Miet-, IT- und Finanzierungsverträge sowie Vermögensrechte. Erkennt Übertragungs- und Kontrollwechselhindernisse, Abhängigkeiten und fehlende Rechte und bereitet konkrete Zustimmungen und Schutzklausel... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=due-diligence/skills/vertraege-vermoegen-pruefen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
