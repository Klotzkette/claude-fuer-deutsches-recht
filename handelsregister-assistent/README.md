<!-- decimal-headings -->

<!-- decimal-anchor --> <a id="handelsregister-assistent"></a>

# 1. Handelsregister-Assistent

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="was-ist-das-hier"></a>

## 1.1. Was ist das hier?

Handelsregister recherchieren und Registervorgänge vollziehen: Auszüge, Gesellschafterlisten, Auslandsvertretung, Organwechsel, Anmeldung, Zwischenverfügung und Datenschutz. Zehn Fachworkflows und ein Hauptproblem-Skill führen zu konkreten Dokumenten und nachgewiesenem Vollzugsstand.

Dieses Plugin gehört zum Marketplace mit 275 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

<!-- decimal-anchor --> <a id="welche-datei-wofür--which-file-should-i-use"></a>

## 1.2. Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`handelsregister-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-assistent.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/handelsregister-assistent.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Alle elf Skills sind unmittelbar enthalten: zehn Fachskills und der Hauptproblem-Skill. Werkstatt, Mini und Hauptproblem-Prompt sind getrennte eigenständige Downloads. Beim Einzel-Download eines Skills müssen die verlinkten Referenzen zusätzlich verfügbar sein.

All eleven skills are directly included: ten task workflows and one main problem workflow. Workshop, mini and focus prompts are separate standalone downloads. A downloaded individual skill also needs its linked references.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/handelsregister-assistent.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

<!-- decimal-anchor --> <a id="in-30-sekunden-starten"></a>

## 1.3. In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/handelsregister-assistent.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Handelsregister-Assistent:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

<!-- decimal-anchor --> <a id="downloads"></a>

## 1.4. Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`handelsregister-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-assistent.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`handelsregister-assistent-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-schnellstart.md) · [`handelsregister-assistent-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`handelsregister-assistent-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-werkstatt.md) · [`handelsregister-assistent-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-hauptproblem.md" download>handelsregister-assistent-hauptproblem.md</a> · [`handelsregister-assistent-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 275 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

<!-- decimal-anchor --> <a id="zugeordnete-testakten"></a>

## 1.5. Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Kiezkolben und die Gesellschafterin aus Colombo](../testakten/handelsregister-assistent-kiezkolben-colombo/README.md) | [Gesamt-PDF](../testakten/handelsregister-assistent-kiezkolben-colombo/gesamt-pdf/handelsregister-assistent-kiezkolben-colombo_gesamt.pdf) | [`testakte-handelsregister-assistent-kiezkolben-colombo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-handelsregister-assistent-kiezkolben-colombo.zip) | [`testakte-handelsregister-assistent-kiezkolben-colombo-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-handelsregister-assistent-kiezkolben-colombo-einzelpdfs.zip) |
| [Nachtbrot zieht um](../testakten/handelsregister-assistent-nachtbrot-umzug/README.md) | [Gesamt-PDF](../testakten/handelsregister-assistent-nachtbrot-umzug/gesamt-pdf/handelsregister-assistent-nachtbrot-umzug_gesamt.pdf) | [`testakte-handelsregister-assistent-nachtbrot-umzug.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-handelsregister-assistent-nachtbrot-umzug.zip) | [`testakte-handelsregister-assistent-nachtbrot-umzug-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-handelsregister-assistent-nachtbrot-umzug-einzelpdfs.zip) |
| [Polter & Partner: zwei Unterschriften zu wenig](../testakten/handelsregister-assistent-polter-prokura/README.md) | [Gesamt-PDF](../testakten/handelsregister-assistent-polter-prokura/gesamt-pdf/handelsregister-assistent-polter-prokura_gesamt.pdf) | [`testakte-handelsregister-assistent-polter-prokura.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-handelsregister-assistent-polter-prokura.zip) | [`testakte-handelsregister-assistent-polter-prokura-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-handelsregister-assistent-polter-prokura-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Eine Registerwerkstatt für belastbare Recherche, konkrete Anmeldungen und vollständigen Schriftverkehr. Zehn Fachskills und ein elfter Hauptproblem-Skill führen vom vorhandenen Aktenstand zum verwendbaren Dokument und zum nachgewiesenen Vollzugsstand. Das bestehende Plugin `handelsregister-praxis` bleibt erhalten.

Werkstatt zum Bearbeiten und Lesen: [Word](assets/handelsregister-assistent-werkstatt.docx) · [PDF](assets/handelsregister-assistent-werkstatt.pdf).

<!-- decimal-anchor --> <a id="schnell-anfangen"></a>

## 1.6. Schnell anfangen

Laden Sie Ihre Unterlagen und nennen Sie das gewünschte Ergebnis, etwa: „Prüfen Sie, wer am Vertragstag vertreten konnte“, „Fertigen Sie die Gesellschafterliste“ oder „Beantworten Sie die Zwischenverfügung“. Bekannte Daten werden übernommen; Rückfragen beziehen sich auf den tatsächlichen Engpass. Nachgereichte Unterlagen führen zur überarbeiteten Fassung.

- [Große Werkstatt mit acht ausformulierten Dokumentmustern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-werkstatt.md).
- [Mini-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-schnellstart.md).
- [Hauptproblem-Prompt: Den stockenden Vorgang zum Ergebnis führen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/handelsregister-assistent-hauptproblem.md).
- [Normen, Rechtsprechung und aktuelle Länderwege](references/registerverfahren-und-quellen.md).

Die Werkstatt enthält über 12000 Wörter in einer eigenständig nutzbaren Arbeitsanweisung. Mini und Hauptproblem sind jeweils auf höchstens 7500 UTF-8-Bytes und Zeichen begrenzt. Die langen Vertiefungen müssen nicht bei jeder einfachen Recherche vollständig geladen werden.

<!-- decimal-anchor --> <a id="elf-skills"></a>

## 1.7. Elf Skills

| Nummer | Fachworkflow | Skill |
| --- | --- | --- |
| 1 | Registerrecherche und belastbare Auszüge | [registerrecherche-und-auszuege](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerrecherche-und-auszuege/SKILL.md) |
| 2 | Vertretung zum richtigen Zeitpunkt | [vertretung-und-registerpublizitaet](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/vertretung-und-registerpublizitaet/SKILL.md) |
| 3 | Gesellschafterliste mit belegter Veränderung | [gesellschafterliste-erstellen-und-abgleichen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gesellschafterliste-erstellen-und-abgleichen/SKILL.md) |
| 4 | Ausländische Gesellschaften und Urkunden | [auslandsvertretung-und-urkunden](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/auslandsvertretung-und-urkunden/SKILL.md) |
| 5 | Organwechsel und Prokura sauber vollziehen | [organwechsel-und-prokura](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/organwechsel-und-prokura/SKILL.md) |
| 6 | Gründung, Satzung und Kapital anmelden | [gruendung-satzung-und-kapital-anmelden](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gruendung-satzung-und-kapital-anmelden/SKILL.md) |
| 7 | Sitz, Zweigniederlassung und Strukturwechsel | [sitz-zweigniederlassung-und-strukturwechsel](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/sitz-zweigniederlassung-und-strukturwechsel/SKILL.md) |
| 8 | Registerschriftverkehr und Zwischenverfügung | [registerschriftverkehr-und-zwischenverfuegung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerschriftverkehr-und-zwischenverfuegung/SKILL.md) |
| 9 | Einreichung vorbereiten und Vollzug nachhalten | [einreichung-und-vollzug-nachhalten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/einreichung-und-vollzug-nachhalten/SKILL.md) |
| 10 | Registerdaten berichtigen und öffentliche Kopien bereinigen | [registerdaten-und-datenschutz](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerdaten-und-datenschutz/SKILL.md) |
| 11 | Hauptproblem: Registervorgang vom Befund zum Vollzug | [hauptproblem-registervorgang-zum-vollzug](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/hauptproblem-registervorgang-zum-vollzug/SKILL.md) |

<!-- decimal-anchor --> <a id="form-und-verantwortung"></a>

## 1.8. Form und Verantwortung

Öffentliche Recherche und Entwürfe sind ohne Notareigenschaft möglich. Handelsregisteranmeldungen unterliegen dagegen der öffentlich beglaubigten elektronischen Form nach § 12 HGB sowie der notariellen Prüfung und Weiterleitung nach dem aktuellen § 378 Absatz 3 FamFG. Vor dem entsprechenden Vollzug fragt der Workflow nach Notariatsrolle, Befugnis und Zugang. Ein Anwaltspostfach ersetzt diesen Weg nicht. Gesellschafterlisten nach § 40 GmbHG und bloßer Schriftverkehr werden jeweils gesondert eingeordnet.

Agentische Portalaktionen erfolgen nur mit tatsächlich verfügbaren Werkzeugen und konkreter Freigabe für die externe Handlung. Nutzer übernehmen Login und Mehrfaktorauthentifizierung; Geheimnisse werden nicht gespeichert und Zugriffssperren nicht umgangen. Persönliche Versicherungen, Beglaubigungen und notarielle Amtshandlungen bleiben den zuständigen Personen vorbehalten. Ein technischer Eingang ist keine Eintragung.

<!-- decimal-anchor --> <a id="drei-lebendige-arbeitsakten"></a>

## 1.9. Drei lebendige Arbeitsakten

Alle Personen, Gesellschaften, Registerzeichen und Vorgänge der Testakten sind fiktiv. Kontakte verwenden reservierte `.example`-Domains. Die Akten enthalten weder Musterlösung noch vorweggenommene gerichtliche Endentscheidung. Arbeitsabschriften tragen keine nachgeahmten amtlichen Siegel oder Unterschriftsbilder.

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Testakte | Ausgangslage | Akte und Downloadseite |
| --- | --- | --- |
| Kiezkolben und die Gesellschafterin aus Colombo | eROC-Unterlagen, Organwechsel, unklare Einzelvertretung, fehlende Apostille und nachgereichte Board-Dokumente | [Kiezkolben](../testakten/handelsregister-assistent-kiezkolben-colombo/README.md) |
| Polter & Partner: zwei Unterschriften zu wenig | Neuer Geschäftsführer, alte Prokura, widersprüchliche Zugangsnachweise und ausstehender Registervollzug | [Polter & Partner](../testakten/handelsregister-assistent-polter-prokura/README.md) |
| Nachtbrot zieht um | Anschrift, Satzungssitz, Firmenprüfung am Zielort, Zwischenverfügung und Dokumentaustausch | [Nachtbrot](../testakten/handelsregister-assistent-nachtbrot-umzug/README.md) |

<!-- decimal-anchor --> <a id="aktuelle-anker-mit-begrenzter-aussage"></a>

## 1.10. Aktuelle Anker mit begrenzter Aussage

Stand 01.10.2026: BGH II ZR 50/25 zur materiellen Gesellschafterstellung trotz Liste; II ZB 13/24 zur konkret untersuchten österreichischen Onlinebeglaubigung; II ZB 2/25 zum Austausch überschießender öffentlicher Registerdaten. II ZB 15/22 ergänzt die Abgrenzung zwischen Zwischenverfügung und endgültiger Ablehnung. Die [Quellenprüfung](../quality/source-audits/registerwerkstaetten-2026-10-01/handelsregister.md) dokumentiert gelesene Passagen und Grenzen.

Sri Lanka hat ein Unternehmensregister. Der Pflichtfall beruht auf einem unzureichenden konkreten Vertretungsdossier, nicht auf einem erfundenen registerlosen Staat. HCCH-Status und Hinweise der deutschen Botschaft Colombo wurden geprüft; eine mögliche Amts- oder Rechtshilfe wird nicht als garantierte Prüfung von Gesellschaftsurkunden ausgegeben.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

<!-- decimal-anchor --> <a id="orientierung-nach-arbeitslogik"></a>

## 1.11. Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Recherche und Registerlage | [`hauptproblem-registervorgang-zum-vollzug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/hauptproblem-registervorgang-zum-vollzug/SKILL.md), [`registerrecherche-und-auszuege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerrecherche-und-auszuege/SKILL.md), [`registerdaten-und-datenschutz`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerdaten-und-datenschutz/SKILL.md) |
| 2. Vertretung und Gesellschafterliste | [`vertretung-und-registerpublizitaet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/vertretung-und-registerpublizitaet/SKILL.md), [`auslandsvertretung-und-urkunden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/auslandsvertretung-und-urkunden/SKILL.md), [`gesellschafterliste-erstellen-und-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gesellschafterliste-erstellen-und-abgleichen/SKILL.md) |
| 3. Anmeldungen und Strukturänderungen | [`gruendung-satzung-und-kapital-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gruendung-satzung-und-kapital-anmelden/SKILL.md), [`organwechsel-und-prokura`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/organwechsel-und-prokura/SKILL.md), [`sitz-zweigniederlassung-und-strukturwechsel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/sitz-zweigniederlassung-und-strukturwechsel/SKILL.md) |
| 4. Schriftverkehr und Vollzug | [`registerschriftverkehr-und-zwischenverfuegung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerschriftverkehr-und-zwischenverfuegung/SKILL.md), [`einreichung-und-vollzug-nachhalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/einreichung-und-vollzug-nachhalten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.12. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`auslandsvertretung-und-urkunden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/auslandsvertretung-und-urkunden/SKILL.md) | Ordnet fremdes Gesellschaftsrecht, Existenz, Organbestellung, Vertretungsmacht, Echtheit und Form getrennt und entwickelt konkrete alternative Nachweispakete. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/auslandsvertretung-und-urkunden/SKILL.md) |
| [`einreichung-und-vollzug-nachhalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/einreichung-und-vollzug-nachhalten/SKILL.md) | Stellt Anmeldung und Anlagen versandfertig zusammen, prüft Notariats- und Zugangsvoraussetzungen und dokumentiert belegten Eingang und Eintragungsstand. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/einreichung-und-vollzug-nachhalten/SKILL.md) |
| [`gesellschafterliste-erstellen-und-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gesellschafterliste-erstellen-und-abgleichen/SKILL.md) | Erstellt oder korrigiert GmbH- und UG-Gesellschafterlisten und trennt materielle Beteiligung, formelle Legitimation und Einreichungszuständigkeit. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gesellschafterliste-erstellen-und-abgleichen/SKILL.md) |
| [`gruendung-satzung-und-kapital-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gruendung-satzung-und-kapital-anmelden/SKILL.md) | Führt Gründungen, Satzungsänderungen und Kapitalmaßnahmen zum vollständigen rechtsformspezifischen Notariatspaket. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/gruendung-satzung-und-kapital-anmelden/SKILL.md) |
| [`hauptproblem-registervorgang-zum-vollzug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/hauptproblem-registervorgang-zum-vollzug/SKILL.md) | Führt einen unklaren oder stockenden Registervorgang vom Dokumentenbefund über die passende Anmeldung oder Antwort bis zum nachgewiesenen Vollzugsstand. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/hauptproblem-registervorgang-zum-vollzug/SKILL.md) |
| [`organwechsel-und-prokura`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/organwechsel-und-prokura/SKILL.md) | Bereitet Geschäftsführerwechsel, Vertretungsänderung sowie Erteilung und Widerruf von Prokura mit datierter Wirksamkeits- und Nachweisfolge vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/organwechsel-und-prokura/SKILL.md) |
| [`registerdaten-und-datenschutz`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerdaten-und-datenschutz/SKILL.md) | Prüft falsche Registerdaten und überschießende personenbezogene Angaben und erstellt einen konkreten Berichtigungs- oder Austauschauftrag. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerdaten-und-datenschutz/SKILL.md) |
| [`registerrecherche-und-auszuege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerrecherche-und-auszuege/SKILL.md) | Sucht die richtige Gesellschaft, liest aktuelle und chronologische Auszüge sowie Registerdokumente und erstellt einen datierten Recherchebericht mit gezielten Nachabrufen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerrecherche-und-auszuege/SKILL.md) |
| [`registerschriftverkehr-und-zwischenverfuegung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerschriftverkehr-und-zwischenverfuegung/SKILL.md) | Bearbeitet Beanstandungen, Nachreichungen, Sachstandsanfragen und Rechtsbehelfe mit Fristen und vollständigen Antwortentwürfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/registerschriftverkehr-und-zwischenverfuegung/SKILL.md) |
| [`sitz-zweigniederlassung-und-strukturwechsel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/sitz-zweigniederlassung-und-strukturwechsel/SKILL.md) | Ordnet Anschriftsänderung, inländischen Sitzwechsel, Zweigniederlassung, Liquidation und Umwandlung der richtigen Registerstrecke zu. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/sitz-zweigniederlassung-und-strukturwechsel/SKILL.md) |
| [`vertretung-und-registerpublizitaet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/vertretung-und-registerpublizitaet/SKILL.md) | Prüft organschaftliche Vertretung, Prokura und Registerpublizität anhand eines konkreten Geschäfts und erstellt einen belastbaren Vertretungsvermerk. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=handelsregister-assistent/skills/vertretung-und-registerpublizitaet/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
