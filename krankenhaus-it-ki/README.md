# Krankenhaus-IT und KI

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Krankenhaus-IT und KI: elf Skills für Datenschutz, Cloud, TIA, DSFA, Medizinprodukte, Forschung und sicheren Betrieb; mit eigenständigen Prompts und einer Thüringer Klinikakte.

Dieses Plugin gehört zum Marketplace mit 296 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`krankenhaus-it-ki.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.0/krankenhaus-it-ki.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/krankenhaus-it-ki.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/krankenhaus-it-ki.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/krankenhaus-it-ki.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Krankenhaus-IT und KI:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`krankenhaus-it-ki.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.0/krankenhaus-it-ki.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`krankenhaus-it-ki-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-schnellstart.md) · [`krankenhaus-it-ki-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`krankenhaus-it-ki-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-werkstatt.md) · [`krankenhaus-it-ki-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-hauptproblem.md" download>krankenhaus-it-ki-hauptproblem.md</a> · [`krankenhaus-it-ki-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 296 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Krankenhaus Auenhöhe in Thüringen](../testakten/krankenhaus-it-ki-auenhoehe-thueringen/README.md) | [Gesamt-PDF](../testakten/krankenhaus-it-ki-auenhoehe-thueringen/gesamt-pdf/krankenhaus-it-ki-auenhoehe-thueringen_gesamt.pdf) | [`testakte-krankenhaus-it-ki-auenhoehe-thueringen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/krankenhaus-it-ki-v445.33.1/testakte-krankenhaus-it-ki-auenhoehe-thueringen.zip) | [`testakte-krankenhaus-it-ki-auenhoehe-thueringen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/krankenhaus-it-ki-v445.33.1/testakte-krankenhaus-it-ki-auenhoehe-thueringen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Dieses Plugin unterstützt IT-Verantwortliche in Krankenhäusern und Klinikverbünden dabei, moderne Systeme im Alltag einzuführen: von der Briefassistenz über medizinische KI bis zur Forschung. Es übersetzt Datenschutz, Lieferantenanforderungen, Sicherheit und Produktrecht in konkrete Fragen, ausformulierte Dokumente und begründete Entscheidungen.

Sie brauchen weder Programmierkenntnisse noch eine juristische Spezialausbildung. Medizinische, datenschutzrechtliche und unternehmerische Zuständigkeiten bleiben sichtbar. Der Assistent bereitet deren Entscheidungen vor und begleitet die Bearbeitung bis zum benötigten Ergebnis.

## 1. Direkt beginnen

> Prüfe die beigefügte Projektakte für unsere Krankenhaus-IT. Erstelle zuerst einen knappen Status pro Vorhaben. Arbeite anschließend die benötigten Datenschutzhinweise, die DSFA oder das TIA vollständig aus. Stelle nur die Fragen, die eine konkrete Entscheidung verändern, und bearbeite unabhängige Teile weiter.

Bei einem konkreten Wunsch genügt beispielsweise: „Formuliere anhand dieser Unterlagen die Datenschutzhinweise für die Entlassbriefassistenz.“

## 2. Plugin und eigenständige Prompts

| Einstieg | Verwendung | Datei |
| --- | --- | --- |
| Plugin-ZIP | Vollständiges Plugin mit elf Skills und Fachreferenzen. | [Plugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.0/krankenhaus-it-ki.zip) |
| Hauptskill | Ein Vorhaben vom Eingang bis zur Entscheidung steuern. | [Krankenhausdigitalisierung steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/krankenhaus-digitalisierung-steuern/SKILL.md) |
| Werkstatt-Prompt | Ausführlicher, eigenständig nutzbarer Workflow mit konkreten Dokumentenmustern. | [Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-werkstatt.md) |
| Mini-Prompt | Kompakter eigenständiger Workflow bis 7.500 UTF-8-Bytes. | [Schnellstart](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-schnellstart.md) |
| Hauptproblem-Prompt | EU-Cloud, Fernsupport und medizinischer KI-Einsatz in einer gemeinsamen Pilotentscheidung. | [Hauptproblem](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/krankenhaus-it-ki-hauptproblem.md) |

Die Markdown- und Textfassungen der drei Prompts sind inhaltsgleich. Sie benötigen für ihren Grundablauf keine anderen Plugin-Dateien. Aktuelle Quellen können nur geprüft werden, wenn das verwendete System Zugriff auf sie oder auf bereitgestellte Unterlagen hat. Das Plugin richtet keinen Cloudzugang ein und verbindet sich nicht automatisch mit Patientensystemen.

## 3. Elf Skills

Zehn Spezialskills und ein Hauptskill decken die zusammenhängenden Arbeitsschritte ab.

| Skill | Konkrete Aufgabe |
| --- | --- |
| [Vorhaben, Datenflüsse und Verantwortung klären](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/vorhaben-datenfluesse-rollen/SKILL.md) | Erfasst neue Krankenhaus-IT und KI vom Behandlungsvorgang bis zu Support und Training. Erstellt eine belegte Datenflusskarte und trennt Konzernrollen sowie offene Freigaben. |
| [Rechtsgrundlagen und Verzeichnis der Verarbeitungstätigkeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/rechtsgrundlagen-vvt-pruefen/SKILL.md) | Prüft Zweck und Rechtsgrundlage neuer Krankenhausverarbeitungen einschließlich Gesundheitsdaten und Landesrecht. Erstellt oder aktualisiert das VVT ohne pauschale Einwilligung für sämtliche KI-Nutzung. |
| [Datenschutzinformationen und Patientenrechte bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/datenschutzinformationen-betroffenenrechte/SKILL.md) | Erstellt verständliche Datenschutzhinweise für Patienten und Beschäftigte und bearbeitet Auskunfts-, Kopie-, Berichtigungs- und Löschbegehren bei Krankenhaus-IT und KI. |
| [Lieferanten, AVV und Geheimnisschutz prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/lieferanten-avv-geheimnisschutz/SKILL.md) | Prüft Krankenhaus-IT-Verträge auf Rollen, Auftragsverarbeitung, Unterauftragnehmer, Geheimnisschutz, Trainingsnutzung und Ausstieg. Formuliert konkrete Vertragsänderungen und Nachfragen. |
| [Drittlandzugriffe und TIA bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/drittland-transfer-impact-assessment/SKILL.md) | Bewertet Fernwartung und Drittlandtransfers in Krankenhaus-Clouds. Prüft Transfermechanismus und ergänzende Maßnahmen und erstellt ein nachvollziehbares Transfer Impact Assessment. |
| [DSFA und Schutzmaßnahmen erarbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/dsfa-schutzmassnahmen-erarbeiten/SKILL.md) | Erstellt eine Datenschutz-Folgenabschätzung für Krankenhaus-IT und KI mit patientenbezogenen Risiken, überprüfbaren Schutzmaßnahmen und begründeter Restrisikobewertung. |
| [KI und Medizinprodukt-Konformität einordnen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/ki-medizinprodukt-konformitaet/SKILL.md) | Ordnet Krankenhaus-KI nach Zweckbestimmung, KI-Verordnung und Medizinprodukterecht ein. Erstellt eine Konformitätsbetrachtung und Nachweisliste ohne eine Zertifizierung oder klinische Freigabe vorzutäuschen. |
| [Forschung und Sekundärnutzung abgrenzen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/forschung-sekundaernutzung-abgrenzen/SKILL.md) | Prüft retrospektive Versorgungsforschung und andere Sekundärnutzung von Krankenhausdaten. Trennt Forschungsprojekt, Qualitätssicherung, Anonymisierung und Anbietertraining mit konkreter Datenfreigabestrecke. |
| [Sicherheit, Ausfall und Datenpannen steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/sicherheit-stoerungen-vorfaelle/SKILL.md) | Bereitet sichere Krankenhaus-IT und KI auf Ausfälle und Vorfälle vor. Verbindet Wiederanlauf, Datenschutzmeldungen und einschlägige Sicherheitsregime mit klaren Zuständigkeiten und belastbarer Zeitleiste. |
| [Pilot, Beschäftigte und sicheren Betrieb vorbereiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/pilot-schulung-betrieb/SKILL.md) | Plant begrenzte Krankenhaus-KI-Piloten mit kompetenten Nutzern, Beschäftigtenbeteiligung, Freigabekriterien und Rückfallbetrieb. Erstellt Betriebsregeln, Schulung und nachvollziehbare Fortführungsentscheidungen. |
| [Krankenhausdigitalisierung vom Vorhaben zum Betrieb steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/krankenhaus-digitalisierung-steuern/SKILL.md) | Hauptskill für IT-Verantwortliche eines Krankenhauskonzerns. Führt administrative, medizinische und wissenschaftliche KI-Vorhaben durch konkrete Prüfschritte bis zu Dokumenten, Pilotentscheidung und Betrieb. |

## 4. Die Arbeitsergebnisse

Auf Wunsch entstehen vollständige Datenschutzhinweise, Verarbeitungseinträge, Lieferantenbriefe, Vertragsklauseln, Transfer Impact Assessments, Datenschutz-Folgenabschätzungen, Konformitätsbetrachtungen, Forschungsdatenvermerke, Pilotpläne, Schulungsunterlagen und Vorfallmeldungen. Eine Checkliste ersetzt kein bestelltes Dokument.

Die Prüfung unterscheidet Belege, Anbieterbehauptungen, Annahmen und offene Punkte. „DSGVO-konform“, „CE-ready“ oder „EU-Cloud“ sind keine ausreichenden Nachweise. Zweck, Produktversion, Datenstufe und Rechtsträger bestimmen den Umfang jeder Empfehlung.

## 5. Testakte Klinikverbund Auenhöhe

Die fiktive Klinik in Thüringen versorgt eine ländliche Region auf hohem medizinischem Niveau. IT-Leiterin Nora Bergmann koordiniert Diktat- und Entlassbriefassistenz, Radiologie-Triage und retrospektive Versorgungsforschung. Ein EU-Cloudangebot mit möglichem US-Support, unvollständige Produktnachweise und unterschiedliche Freigaben sorgen für einen realistischen Arbeitsstand.

Die Testakte enthält bewusst Arbeitsentwürfe, Fragen und Widersprüche. Die Aufgabe besteht darin, belegte Voraussetzungen von offenen Entscheidungen zu trennen und die erforderlichen Dokumente fertig auszuarbeiten. [Testakte mit Unterlagen und Downloads öffnen](../testakten/krankenhaus-it-ki-auenhoehe-thueringen/README.md).

## 6. Quellen und Grenzen

[Rechtsquellen und Rechtsprechung](references/rechtsquellen.md) · [IT- und KI-Regulatorik](references/it-ki-regulatorik.md) · [Zitierstandard](references/zitierweise.md)

Datenschutz, medizinische Sicherheit und Produktkonformität werden getrennt geprüft. Eine rechtliche Arbeitshilfe stellt keine behördliche Zulassung oder Medizinproduktezertifizierung aus. Das Plugin gibt keine individuellen Diagnose- oder Behandlungsempfehlungen. Entwürfe werden innerhalb des Auftrags selbstständig erstellt; Übermittlungen, Meldungen und Änderungen an produktiven Systemen benötigen einen konkreten Auftrag.

## 7. Lizenz

Apache-2.0 OR MIT.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | [`datenschutzinformationen-betroffenenrechte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/datenschutzinformationen-betroffenenrechte/SKILL.md), [`vorhaben-datenfluesse-rollen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/vorhaben-datenfluesse-rollen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`drittland-transfer-impact-assessment`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/drittland-transfer-impact-assessment/SKILL.md), [`dsfa-schutzmassnahmen-erarbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/dsfa-schutzmassnahmen-erarbeiten/SKILL.md), [`forschung-sekundaernutzung-abgrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/forschung-sekundaernutzung-abgrenzen/SKILL.md), [`ki-medizinprodukt-konformitaet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/ki-medizinprodukt-konformitaet/SKILL.md), [`krankenhaus-digitalisierung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/krankenhaus-digitalisierung-steuern/SKILL.md), [`lieferanten-avv-geheimnisschutz`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/lieferanten-avv-geheimnisschutz/SKILL.md), [`pilot-schulung-betrieb`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/pilot-schulung-betrieb/SKILL.md), [`rechtsgrundlagen-vvt-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/rechtsgrundlagen-vvt-pruefen/SKILL.md), [`sicherheit-stoerungen-vorfaelle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/sicherheit-stoerungen-vorfaelle/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`datenschutzinformationen-betroffenenrechte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/datenschutzinformationen-betroffenenrechte/SKILL.md) | Erstellt verständliche Datenschutzhinweise für Patienten und Beschäftigte und bearbeitet Auskunfts-, Kopie-, Berichtigungs- und Löschbegehren bei Krankenhaus-IT und KI. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/datenschutzinformationen-betroffenenrechte/SKILL.md) |
| [`drittland-transfer-impact-assessment`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/drittland-transfer-impact-assessment/SKILL.md) | Bewertet Fernwartung und Drittlandtransfers in Krankenhaus-Clouds. Prüft Transfermechanismus und ergänzende Maßnahmen und erstellt ein nachvollziehbares Transfer Impact Assessment. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/drittland-transfer-impact-assessment/SKILL.md) |
| [`dsfa-schutzmassnahmen-erarbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/dsfa-schutzmassnahmen-erarbeiten/SKILL.md) | Erstellt eine Datenschutz-Folgenabschätzung für Krankenhaus-IT und KI mit patientenbezogenen Risiken, überprüfbaren Schutzmaßnahmen und begründeter Restrisikobewertung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/dsfa-schutzmassnahmen-erarbeiten/SKILL.md) |
| [`forschung-sekundaernutzung-abgrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/forschung-sekundaernutzung-abgrenzen/SKILL.md) | Prüft retrospektive Versorgungsforschung und andere Sekundärnutzung von Krankenhausdaten. Trennt Forschungsprojekt, Qualitätssicherung, Anonymisierung und Anbietertraining mit konkreter Datenfreigabestrecke. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/forschung-sekundaernutzung-abgrenzen/SKILL.md) |
| [`ki-medizinprodukt-konformitaet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/ki-medizinprodukt-konformitaet/SKILL.md) | Ordnet Krankenhaus-KI nach Zweckbestimmung, KI-Verordnung und Medizinprodukterecht ein. Erstellt eine Konformitätsbetrachtung und Nachweisliste ohne eine Zertifizierung oder klinische Freigabe vorzutäuschen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/ki-medizinprodukt-konformitaet/SKILL.md) |
| [`krankenhaus-digitalisierung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/krankenhaus-digitalisierung-steuern/SKILL.md) | Hauptskill für IT-Verantwortliche eines Krankenhauskonzerns. Führt administrative, medizinische und wissenschaftliche KI-Vorhaben durch konkrete Prüfschritte bis zu Dokumenten, Pilotentscheidung und Betrieb. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/krankenhaus-digitalisierung-steuern/SKILL.md) |
| [`lieferanten-avv-geheimnisschutz`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/lieferanten-avv-geheimnisschutz/SKILL.md) | Prüft Krankenhaus-IT-Verträge auf Rollen, Auftragsverarbeitung, Unterauftragnehmer, Geheimnisschutz, Trainingsnutzung und Ausstieg. Formuliert konkrete Vertragsänderungen und Nachfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/lieferanten-avv-geheimnisschutz/SKILL.md) |
| [`pilot-schulung-betrieb`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/pilot-schulung-betrieb/SKILL.md) | Plant begrenzte Krankenhaus-KI-Piloten mit kompetenten Nutzern, Beschäftigtenbeteiligung, Freigabekriterien und Rückfallbetrieb. Erstellt Betriebsregeln, Schulung und nachvollziehbare Fortführungsentscheidungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/pilot-schulung-betrieb/SKILL.md) |
| [`rechtsgrundlagen-vvt-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/rechtsgrundlagen-vvt-pruefen/SKILL.md) | Prüft Zweck und Rechtsgrundlage neuer Krankenhausverarbeitungen einschließlich Gesundheitsdaten und Landesrecht. Erstellt oder aktualisiert das VVT ohne pauschale Einwilligung für sämtliche KI-Nutzung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/rechtsgrundlagen-vvt-pruefen/SKILL.md) |
| [`sicherheit-stoerungen-vorfaelle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/sicherheit-stoerungen-vorfaelle/SKILL.md) | Bereitet sichere Krankenhaus-IT und KI auf Ausfälle und Vorfälle vor. Verbindet Wiederanlauf, Datenschutzmeldungen und einschlägige Sicherheitsregime mit klaren Zuständigkeiten und belastbarer Zeitleiste. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/sicherheit-stoerungen-vorfaelle/SKILL.md) |
| [`vorhaben-datenfluesse-rollen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/vorhaben-datenfluesse-rollen/SKILL.md) | Erfasst neue Krankenhaus-IT und KI vom Behandlungsvorgang bis zu Support und Training. Erstellt eine belegte Datenflusskarte und trennt Konzernrollen sowie offene Freigaben. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=krankenhaus-it-ki/skills/vorhaben-datenfluesse-rollen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
