# 1. Untersuchungshaft

Untersuchungshaft anordnen, überprüfen oder beenden und Rechte während des Vollzugs klären: Dieses Plugin unterstützt Gericht, Staatsanwaltschaft, Verteidigung und Betroffene mit genau zehn Skills. Aus Haftbefehl, Beschlüssen und Belegen entstehen konkrete Anträge, Stellungnahmen oder Entscheidungsentwürfe. Der nächste Verfahrensschritt bestimmt die Bearbeitung, nicht ein vollständiges Interview bei jedem Start.

[Hauptübersicht](../README.md) · [Alle Skills](../SKILLS.md) · [Skills dieses Plugins](../skills-index/untersuchungshaft.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [Plugin-Dateien](.) · [English guide](#16-english-guide)

## 1.1. Mit der anstehenden Entscheidung beginnen

Installieren Sie das Plugin und geben Sie Rolle, Auftrag und vorhandene Unterlagen an. Ist der passende Verfahrensweg noch offen, beginnen Sie mit `uhaft-verfahren-steuern`. Liegt bereits ein konkreter Auftrag vor, verwenden Sie unmittelbar den betreffenden Fachskill.

| Situation | Einstieg | Angestrebtes Ergebnis |
| --- | --- | --- |
| Festnahme oder bevorstehende Vorführung | `vorfuehrung-verteidigung-sichern` | Eilantrag zu Verteidigerkontakt, Verständigung oder Haftunterlagen; nachvollziehbare Zeitangaben. |
| Haftgrund oder Tatverdacht zweifelhaft | `haftbefehl-voraussetzungen-pruefen` | Rollenbezogener Antrag oder begründeter Beschlussentwurf mit Belegstellen. |
| Neue Wohnung, Arbeit oder Betreuung nachgewiesen | `haftverschonung-entlassung-beantragen` | Antrag auf Aufhebung oder konkrete mildere Maßnahmen, ohne eine Entlassung vorwegzunehmen. |
| Haftentscheidung überprüfen lassen | `haftpruefung-muendlich-vorbereiten` oder `haftbeschwerde-begruenden` | Zunächst passenden Verfahrensweg wählen, dann Antrag oder Rechtsbehelf ausformulieren. |
| Lange Haft, ausgefallene Termine, Sechsmonatsvorlage | `haftdauer-beschleunigung-pruefen` | Belegte Chronologie und daraus begründete Stellungnahme oder Antrag. |
| Besuch, Telefon oder Post eingeschränkt | `beschraenkungen-kontakt-pruefen` | Gerichtliche Anordnung, konkretes Risiko und mildere Kontaktregel prüfen. |
| Anstalt lehnt Kleidung, Versorgung oder anderen Vollzugsantrag ab | `vollzugsbedingungen-gerichtlich-pruefen` | Landesrecht, Anstaltsentscheidung und passenden gerichtlichen Rechtsschutz zuordnen. |
| Jugendlicher oder Heranwachsender betroffen | `jugendliche-heranwachsende-pruefen` ergänzen | Alter, Verteidigung, Jugendhilfe und tatsächlich verfügbare Alternativen berücksichtigen. |

Beispiel: „Ich bin Verteidiger. Haftbefehl, Wohnraumzusage und Arbeitgebermail liegen im Ordner. Bereite einen Haftverschonungsantrag vor und frage nur die noch fehlenden Nachweise ab.“ Für eine gerichtliche Prüfung stattdessen ausdrücklich einen neutralen Beschlussentwurf mit belastenden und entlastenden Umständen beauftragen.

Eigene Anträge des Betroffenen sind möglich; das Arbeitsmittel ersetzt jedoch keine notwendige Verteidigung. Angehörige sind nicht automatisch Verfahrensvertreter. Bei akuter gesundheitlicher Gefahr ist unmittelbar Hilfe durch Anstaltsdienst und ärztlichen Dienst erforderlich, nicht erst ein fertig formulierter Antrag. Keine Einreichung, Kontaktaufnahme oder behördliche Anordnung erfolgt allein durch das Erstellen eines Entwurfs.

## 1.2. Plugin, Werkstatt oder Mini wählen

| Fassung / Format | Verwendung / Use | Download |
| --- | --- | --- |
| Plugin-ZIP | Zehn Skills und Referenzen; Marketplace-Name `untersuchungshaft` / Ten skills and references | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.1.0/untersuchungshaft.zip) |
| Portables Plugin-ZIP | Derselbe Inhalt in einem umschließenden Plugin-Ordner / Same content in a containing plugin folder | [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.1.0/untersuchungshaft-portable.zip) |
| Werkstatt-Prompt | Ausführlicher eigenständiger Ablauf mit Rollen, Verzweigungen und Dokumentproduktion / Detailed standalone workflow | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/untersuchungshaft-werkstatt.md" download>Werkstatt als Markdown / Download workshop</a> |
| Mini-Prompt / Schnellstart | Kompakter eigenständiger Ablauf für den konkreten Haftauftrag / Compact standalone workflow | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/untersuchungshaft-schnellstart.md" download>Mini als Markdown / Download quick start</a> |

Die Markdown-Links verwenden die Downloadhilfe und liefern die aktuelle Arbeitsfassung als Datei. Fest versionierte Pakete und separate Prompt-Downloads gehören zum [Komponentenrelease 1.1.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/untersuchungshaft-v1.1.0). [Release-Beschreibung als Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=docs/releases/untersuchungshaft-v1.1.0.md).

Der Werkstatt-Prompt enthält fünfzehn nach Streitfragen eingeordnete Entscheidungen mit Randnummern, Quellenstatus und Grenzen ihrer Übertragung. Die Rechtsprechung führt jeweils zu einer konkreten Rückfrage, einem Antrag oder einer Entscheidung. Der Mini-Prompt gliedert denselben Arbeitsweg in zehn kurze Abschnitte mit neun ausgewählten Entscheidungen und bleibt auch einschließlich Leerzeichen und Windows-Zeilenumbrüchen unter 7.500 Zeichen beziehungsweise UTF-8-Bytes. Die Kürze begrenzt den Umfang, nicht die Pflicht zur Einzelfallprüfung.

Werkstatt und Mini funktionieren unabhängig vom Plugin: Datei herunterladen, im verwendeten System als Arbeitsanweisung übergeben und den Auftrag samt Unterlagen hinzufügen. Das Plugin-ZIP enthält ausschließlich Manifeste, README, Skills, Referenzen und Lizenz. Promptdateien, Qualitätsprüffälle und Testakten werden nicht mitinstalliert. Je Auftrag wird nur der benötigte Fachweg vertieft; es ist nicht nötig, alle zehn Skills und alle Akten gleichzeitig zu laden.

Eine Oberfläche muss das jeweilige Pluginformat tatsächlich unterstützen. Andernfalls die eigenständigen Markdown-Dateien verwenden. Datei-, Recherche- und Exportfunktionen hängen von den verfügbaren Werkzeugen und erteilten Zugriffsrechten ab. Das Plugin enthält keinen eingebauten Gerichts-, Anstalts- oder Datenbankzugang.

## 1.3. Alle zehn Skills als einzelne Dateien

Die Übersicht ist alphabetisch; die Tabelle zum Einstieg oben folgt dem Verfahrensablauf. Jeder Download enthält einen vollständigen Skill. `uhaft-verfahren-steuern` ist der Hauptskill innerhalb der zehn, kein zusätzlicher elfter Skill.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`beschraenkungen-kontakt-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/beschraenkungen-kontakt-pruefen/SKILL.md) | Prüft gerichtliche Besuchs-, Telefon- und Postbeschränkungen in Untersuchungshaft. Unterscheidet Verfahrenssicherung von Anstaltsregeln, schützt Verteidigerkontakt und formuliert begrenzte Anträge auf Änderung oder Aufhebung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/beschraenkungen-kontakt-pruefen/SKILL.md) |
| [`haftbefehl-voraussetzungen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftbefehl-voraussetzungen-pruefen/SKILL.md) | Prüft dringenden Tatverdacht, konkrete Haftgründe und Verhältnismäßigkeit eines Haftbefehls. Ordnet Belege und Gegenindizien zu und erstellt je nach Rolle Haftantrag, Beschlussentwurf oder begründeten Aufhebungsantrag. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftbefehl-voraussetzungen-pruefen/SKILL.md) |
| [`haftbeschwerde-begruenden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftbeschwerde-begruenden/SKILL.md) | Verfasst Haftbeschwerden und prüft weitere Beschwerde, Abhilfe und Zuständigkeit. Trennt Haftentscheidung, Vollzugsmaßnahme und Verfassungsbeschwerde und richtet die Begründung auf konkrete tragende Fehler aus. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftbeschwerde-begruenden/SKILL.md) |
| [`haftdauer-beschleunigung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftdauer-beschleunigung-pruefen/SKILL.md) | Prüft lange Untersuchungshaft, Sechsmonatsvorlage und Verfahrensbeschleunigung anhand belegter Haft- und Termindaten. Erstellt Haftfortdauerstellungnahme oder Entlassungsantrag ohne automatische Fristverkürzungen zu behaupten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftdauer-beschleunigung-pruefen/SKILL.md) |
| [`haftpruefung-muendlich-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftpruefung-muendlich-vorbereiten/SKILL.md) | Bereitet Haftprüfung und mündliche Verhandlung vor. Prüft Zuständigkeit, Anhörungsanspruch und laufende Beschwerden und erstellt Antrag, gezielte Beweisanträge und eine fortschreibbare Terminsvorbereitung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftpruefung-muendlich-vorbereiten/SKILL.md) |
| [`haftverschonung-entlassung-beantragen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftverschonung-entlassung-beantragen/SKILL.md) | Entwickelt belegte Alternativen zum Haftvollzug und prüft Aufhebung, Außervollzugsetzung und Wiederinvollzugsetzung. Formuliert Anträge, Auflagen und Entlassungsabläufe mit Wohnsitz, Meldung, Sicherheit und Kontaktregelung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/haftverschonung-entlassung-beantragen/SKILL.md) |
| [`jugendliche-heranwachsende-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/jugendliche-heranwachsende-pruefen/SKILL.md) | Prüft Untersuchungshaft bei Jugendlichen und Heranwachsenden mit besonderem Blick auf Alter, Jugendhilfe, Unterbringungsalternativen und Verteidigung. Erstellt altersgerechte Anträge und trennt die Reichweite der JGG-Sonderregeln. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/jugendliche-heranwachsende-pruefen/SKILL.md) |
| [`uhaft-verfahren-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/uhaft-verfahren-steuern/SKILL.md) | Steuert Untersuchungshaftsachen vom Haftbefehl bis zur Entlassung. Wählt für Gericht, Staatsanwaltschaft, Verteidigung oder Betroffene den passenden Antrag, prüft Eile und führt nach Rückfragen am konkreten Dokument weiter. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/uhaft-verfahren-steuern/SKILL.md) |
| [`vollzugsbedingungen-gerichtlich-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/vollzugsbedingungen-gerichtlich-pruefen/SKILL.md) | Prüft Unterbringung, Kleidung, Arbeit, Besuche und Gesundheitsversorgung während der Untersuchungshaft nach dem jeweiligen Landesrecht. Erstellt Anträge an die JVA und gerichtlichen Eilrechtsschutz nach Paragraf 119a StPO. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/vollzugsbedingungen-gerichtlich-pruefen/SKILL.md) |
| [`vorfuehrung-verteidigung-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/vorfuehrung-verteidigung-sichern/SKILL.md) | Sichert bei Festnahme und Haftvorführung Verteidigerkontakt, verständliche Belehrung, Dolmetscher, wesentliche Haftbelege und die richterliche Entscheidung. Erstellt eilbedürftige Anträge und ein überprüfbares Vorführungsprotokoll. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/skills/vorfuehrung-verteidigung-sichern/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

## 1.4. Vier Akten zum Ausprobieren / Four practice cases

Jede Akte wird zentral gepflegt. Gesamt-PDF, flaches ZIP mit Einzel-PDFs und flaches ZIP mit Originalunterlagen bilden denselben Fall ab. Die Originale enthalten Word-Dokumente, E-Mails, CSV und Textdateien statt bloßer Fallbeschreibungen. Beide ZIPs enthalten den Hinweis in einer `README.txt`; die PDF-Dokumente selbst enthalten keine Warnseite. Eine Äußerung eines Beteiligten oder ein vorhandener Beschluss ist keine vorgegebene Lösung für die weitere Bearbeitung.

Each case has a combined PDF, a flat ZIP of individual PDFs and a flat ZIP of native documents. The ZIP warning is in `README.txt`; PDF warnings appear here, immediately before the downloads. Read the actual documents rather than treating a party's account as the correct outcome.

### 1.4.1. Haftverschonung Fliederborn Berlin

Ein Lagerdiebstahlsvorwurf, eine Reisebuchung und nachgereichte Wohn- und Arbeitsnachweise: Haftbefehl, Vernehmung, Zusagen und Korrespondenz erlauben die Prüfung der veränderten Tatsachengrundlage. Eine neue Haftentscheidung ist offen. [Aktenordner und Unterlagen](../testakten/uhaft-haftverschonung-fliederborn-berlin/).

Berlin: an existing detention order, disputed evidence and subsequent housing and employment documents. Use the file to prepare the next application without assuming its outcome.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamte Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/refs/heads/main/testakten/uhaft-haftverschonung-fliederborn-berlin/gesamt-pdf/uhaft-haftverschonung-fliederborn-berlin_gesamt.pdf) |
| Einzel-PDFs / Individual PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-haftverschonung-fliederborn-berlin-einzelpdfs.zip) |
| Originalunterlagen / Native documents | [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-haftverschonung-fliederborn-berlin.zip) |

### 1.4.2. Kontakte und Vollzugsalltag Falkenried Köln

Gerichtlicher Besuchsvorbehalt, Anstaltsantwort zur Kleidung und ärztlicher Terminbedarf stammen von unterschiedlichen Stellen. Besuchsantrag, Befund, Familienkorrespondenz und Eingangsregister lassen die einzelnen Anliegen getrennt bearbeiten. [Aktenordner und Unterlagen](../testakten/uhaft-vollzug-falkenried-koeln/).

Cologne: judicial contact restrictions, a prison clothing decision and a medical appointment request. Identify the decision-maker and requested remedy for each issue.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamte Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/refs/heads/main/testakten/uhaft-vollzug-falkenried-koeln/gesamt-pdf/uhaft-vollzug-falkenried-koeln_gesamt.pdf) |
| Einzel-PDFs / Individual PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-vollzug-falkenried-koeln-einzelpdfs.zip) |
| Originalunterlagen / Native documents | [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-vollzug-falkenried-koeln.zip) |

### 1.4.3. Sechsmonatsvorlage Kornfeld Dresden

Brandermittlung mit Gutachterauftrag, Gutachten, Anklage und Terminverfügung. Verfahrensjournal und Vorlagebestätigung dokumentieren den zeitlichen Verlauf; über die Fortdauer ist noch zu entscheiden. [Aktenordner und Unterlagen](../testakten/uhaft-sechsmonate-kornfeld-dresden/).

Dresden: a pending six-month review with expert evidence, scheduling correspondence and documented referral. Distinguish elapsed time from actual procedural progress.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamte Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/refs/heads/main/testakten/uhaft-sechsmonate-kornfeld-dresden/gesamt-pdf/uhaft-sechsmonate-kornfeld-dresden_gesamt.pdf) |
| Einzel-PDFs / Individual PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-sechsmonate-kornfeld-dresden-einzelpdfs.zip) |
| Originalunterlagen / Native documents | [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-sechsmonate-kornfeld-dresden.zip) |

### 1.4.4. Haftvorführung Wolkensteg Bremen

Ein 15-Jähriger vor der Haftentscheidung: Festnahmebericht und Haftantrag treffen auf Angaben aus Familie, Schule und Jugendhilfe sowie eine angefragte betreute Unterbringung. Erreichbarkeit und tatsächliche Aufnahmebedingungen bleiben anhand der Unterlagen zu klären. [Aktenordner und Unterlagen](../testakten/uhaft-jugend-wolkensteg-bremen/).

Bremen: a 15-year-old awaiting a detention decision, with family and school records and a proposed supervised placement. Check the actual evidence and availability of the alternative.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamte Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/refs/heads/main/testakten/uhaft-jugend-wolkensteg-bremen/gesamt-pdf/uhaft-jugend-wolkensteg-bremen_gesamt.pdf) |
| Einzel-PDFs / Individual PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-jugend-wolkensteg-bremen-einzelpdfs.zip) |
| Originalunterlagen / Native documents | [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/untersuchungshaft-v1.0.0/testakte-uhaft-jugend-wolkensteg-bremen.zip) |

## 1.5. Quellen, Prüfstand und Grenzen

Redaktioneller Stand: 16.10.2026. Bundesrecht, Landesrecht und Verfahrensstand müssen für den konkreten Fall erneut abgeglichen werden. Das [Quellenverzeichnis als Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=untersuchungshaft/references/rechtsquellen.md) trennt Normen, tragende Aussagen und Übertragungsgrenzen. Elf BVerfG-Entscheidungen wurden im amtlichen Volltext geprüft. BGH, 03.04.2025, StB 8/25, und BGH, 04.08.2026, StB 46/26, sind als abgeglichene Sekundärvolltextquellen gekennzeichnet; ihr amtlicher Originalabruf steht aus. Nichtannahmebeschlüsse und ausdrücklich offengelassene Fragen werden nicht als erfolgreiche Entlassung oder abschließend geklärte Rechtslage dargestellt.

Das Qualitätsprofil enthält zehn individuelle Prüffälle, einen je Skill. Es dokumentiert eine redaktionelle Prüfung der vorhandenen Anweisungen, keine durchgeführten Modellläufe, keine Erfolgsquote und keine rechtliche Zertifizierung. Technische Paketprüfungen ersetzen weder fachliche Einzelfallprüfung noch einen Live-Test in einer bestimmten Oberfläche.

Dieses Angebot ist ein experimentelles Arbeitsmittel, keine Rechtsberatung und keine Zusage eines bestimmten Haftausgangs. Es ersetzt weder einen Verteidiger noch die verantwortliche gerichtliche oder staatsanwaltschaftliche Entscheidung. Fehler und unvollständige Quellen sind möglich; vor Verwendung eines Entwurfs müssen Zuständigkeit, Form, Tatsachen, Recht und notwendige Freigaben geprüft werden.

## 1.6. English Guide

This plugin supports German pretrial-detention work for courts, prosecutors, defence counsel and affected individuals. It contains exactly ten skills, including the coordinating skill `uhaft-verfahren-steuern`. It prepares applications, submissions and draft decisions; it does not decide cases or operate court systems.

### 1.6.1. Start with the current task

Use the installation or Markdown links in section 1.2. Supply your role, the current detention order or decision, and the document you need. If the procedural route is unclear, start with the coordinating skill. Otherwise use the matching specialist skill from section 1.3. Existing documents are read before questions are asked; only missing information that matters to the next step should be requested.

For example: “Act for defence counsel. Read the detention order, housing confirmation and employer's email. Draft an application for suspension of detention and ask only for the remaining essential evidence.” A court user should instead request an impartial draft addressing both inculpatory and exculpatory material. After a reply or a new decision arrives, continue the same task rather than restarting the intake.

### 1.6.2. Choose the right route and format

The skills distinguish arrest and initial judicial appearance, detention grounds, release or suspension, judicial detention review, complaint proceedings, prolonged detention, judicial contact restrictions, prison conditions and young defendants. A prison measure is not automatically the same procedural issue as the detention order. The applicable German state law must be checked for prison conditions.

The detailed workshop and compact quick-start files are standalone alternatives, not additional installed skills. Download one Markdown file and provide it as instructions in a system able to read it. The plugin archives contain only manifests, this README, the ten skills, references and the licence. Practice files and standalone prompts remain separate downloads. Host support, file access and export tools must be checked in the environment actually used; no universal live-client test is claimed.

The workshop integrates thirteen decisions with pinpoint references and limits of application. Eleven were checked against official full texts; two federal criminal-court decisions remain marked as secondary-source cross-checks. The quick-start follows ten short sections and uses eight selected decisions. Its size stays below 7,500 characters and UTF-8 bytes, including spaces and Windows line endings. Neither version treats a procedural rejection or an unresolved issue as a successful release ruling.

### 1.6.3. Use the cases and retain human control

Section 1.4 provides four independent cases in three formats each: combined PDF, flat individual-PDF ZIP and flat native-document ZIP. Both ZIP variants carry the bilingual warning in a root-level `README.txt`. Individual documents contain factual accounts, evidence and procedural correspondence, not a prescribed answer.

Personal applications do not replace mandatory defence counsel. Relatives do not automatically have authority to represent the detained person. Urgent medical concerns require immediate assistance from prison and medical staff rather than waiting for a document. Drafting does not constitute filing, service, a judicial order or confirmed release. Every external action requires explicit authorization and legal authority. This is an experimental working aid, not legal advice or a guarantee of an outcome.
