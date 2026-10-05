<!-- decimal-headings -->

<!-- decimal-anchor --> <a id="transparenzregister-assistent"></a>

# 1. Transparenzregister-Assistent

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="was-ist-das-hier"></a>

## 1.1. Was ist das hier?

Transparenzregister: Kontrollketten ermitteln, Meldungen und Berichtigungen vorbereiten, Einsicht und Unstimmigkeiten bearbeiten sowie optional freigegebene Portalhandlungen begleiten. Zehn Fachskills und ein Hauptproblem-Skill mit drei Akten.

Dieses Plugin gehört zum Marketplace mit 275 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

<!-- decimal-anchor --> <a id="welche-datei-wofür--which-file-should-i-use"></a>

## 1.2. Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`transparenzregister-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/transparenzregister-assistent.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/transparenzregister-assistent.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Alle elf Skills sind unmittelbar enthalten: zehn Fachskills und der Hauptproblem-Skill. Werkstatt, Mini und Hauptproblem-Prompt sind getrennte eigenständige Downloads. Beim Einzel-Download eines Skills müssen die verlinkten Referenzen zusätzlich verfügbar sein.

All eleven skills are directly included: ten task workflows and one main problem workflow. Workshop, mini and focus prompts are separate standalone downloads. A downloaded individual skill also needs its linked references.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/transparenzregister-assistent.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

<!-- decimal-anchor --> <a id="in-30-sekunden-starten"></a>

## 1.3. In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/transparenzregister-assistent.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Transparenzregister-Assistent:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

<!-- decimal-anchor --> <a id="downloads"></a>

## 1.4. Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`transparenzregister-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/transparenzregister-assistent.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`transparenzregister-assistent-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-schnellstart.md) · [`transparenzregister-assistent-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`transparenzregister-assistent-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-werkstatt.md) · [`transparenzregister-assistent-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-hauptproblem.md" download>transparenzregister-assistent-hauptproblem.md</a> · [`transparenzregister-assistent-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-hauptproblem.txt) |
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
| [Kranichhof und der verschwundene Poolnachtrag](../testakten/transparenzregister-kranichhof/README.md) | [Gesamt-PDF](../testakten/transparenzregister-kranichhof/gesamt-pdf/transparenzregister-kranichhof_gesamt.pdf) | [`testakte-transparenzregister-kranichhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-transparenzregister-kranichhof.zip) | [`testakte-transparenzregister-kranichhof-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-transparenzregister-kranichhof-einzelpdfs.zip) |
| [Spree Aurora und die finnische Beteiligung](../testakten/transparenzregister-spree-aurora/README.md) | [Gesamt-PDF](../testakten/transparenzregister-spree-aurora/gesamt-pdf/transparenzregister-spree-aurora_gesamt.pdf) | [`testakte-transparenzregister-spree-aurora.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-transparenzregister-spree-aurora.zip) | [`testakte-transparenzregister-spree-aurora-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-transparenzregister-spree-aurora-einzelpdfs.zip) |
| [Stifterglück, die Werkstatt und das Familienvermögen](../testakten/transparenzregister-stifterglueck/README.md) | [Gesamt-PDF](../testakten/transparenzregister-stifterglueck/gesamt-pdf/transparenzregister-stifterglueck_gesamt.pdf) | [`testakte-transparenzregister-stifterglueck.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-transparenzregister-stifterglueck.zip) | [`testakte-transparenzregister-stifterglueck-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-transparenzregister-stifterglueck-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Kontrolle nachvollziehen, Meldungen vorbereiten und Registervorgänge bis zum belegten Abschluss bearbeiten. Das Plugin enthält **zehn Fachskills und einen elften Hauptproblem-Skill**, eine umfangreiche eigenständig verwendbare Werkstatt, einen Mini-Prompt und einen fokussierten Hauptproblem-Prompt.

Werkstatt zum Bearbeiten und Lesen: [Word](assets/transparenzregister-assistent-werkstatt.docx) · [PDF](assets/transparenzregister-assistent-werkstatt.pdf).

<!-- decimal-anchor --> <a id="direkt-beginnen"></a>

## 1.6. Direkt beginnen

- [Werkstatt-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-werkstatt.md): durchgehender Arbeitsablauf mit konkreten Rückfragen, ausformulierten Schreiben und kontrollierter Portalübergabe.
- [Mini-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-schnellstart.md): kompakter eigenständiger Ablauf.
- [Hauptproblem-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/transparenzregister-assistent-hauptproblem.md): widersprüchliche Kontrolle bei dringender Meldung auflösen.
- [Geprüfte Rechtsquellen](references/rechtsprechung-und-rechtsstand.md): einschließlich EuGH vom 21.05.2026 und 03.09.2026 mit gelesenen Passagen und Grenzen.

<!-- decimal-anchor --> <a id="elf-skills"></a>

## 1.7. Elf Skills

| Nr. | Skill | Aufgabe |
| --- | --- | --- |
| 1 | [Registervorgang und Verantwortung klären](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registervorgang-aufnehmen/SKILL.md) | Bestimmt für einen konkreten Transparenzregistervorgang Rechtseinheit, Rolle, Mitteilungspflicht und den nächsten Arbeitsauftrag. Nutzt vorhandene Unterlagen und führt direkt zum benötigten Dokument. |
| 2 | [Beteiligung und tatsächliche Kontrolle prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/kontrollketten-und-stimmrechte-pruefen/SKILL.md) | Ermittelt natürliche wirtschaftlich Berechtigte aus Kapital, Stimmen, Pool-, Organ- und Vetorechten über mehrere Gesellschaftsebenen. Verhindert schematische Quotenmultiplikation. |
| 3 | [Treuhand, Stiftung und Trust zuordnen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/treuhand-stiftung-und-trust-pruefen/SKILL.md) | Trennt die Meldung einer Gesellschaft von einer möglichen eigenen Registerpflicht einer Treuhand oder Stiftung und ermittelt funktionsbezogene Berechtigte. |
| 4 | [Erstmeldung beleggestützt vorbereiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/erstmeldung-vollstaendig-vorbereiten/SKILL.md) | Erstellt aus einer geklärten Kontrollstruktur einen vollständigen Transparenzregisterdatensatz samt Nachweisen und überprüfbarer Freigabeansicht. |
| 5 | [Änderung, Berichtigung und Historie ordnen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/aenderung-und-berichtigung-ordnen/SKILL.md) | Rekonstruiert Registerzeiträume, trennt neue Ereignisse von früheren Fehlern und erstellt konsistente Änderungs- oder Berichtigungsdaten. |
| 6 | [Einsicht und Schutz der Daten steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/einsicht-und-datenschutz-steuern/SKILL.md) | Begründet Einsichtsanträge nach der passenden Berechtigungsgruppe, prüft Schutzbeschränkungen und trennt Abruf von weiterer Veröffentlichung. |
| 7 | [Unstimmigkeit melden oder beantworten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/unstimmigkeiten-pruefen-und-beantworten/SKILL.md) | Vergleicht Registerdaten mit eigenen Erkenntnissen und erstellt eine rollengerechte Unstimmigkeitsmeldung oder Verfahrensantwort samt Belegen. |
| 8 | [PEP und Mittelherkunft getrennt prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/pep-und-mittelherkunft-trennen/SKILL.md) | Prüft politische Exponiertheit und verstärkte Sorgfalt getrennt von der wirtschaftlichen Berechtigung und begrenzt die Datenweitergabe auf den konkreten Zweck. |
| 9 | [Registerschriftverkehr und Anhörung bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registerkorrespondenz-und-anhoerung/SKILL.md) | Erstellt präzise Antworten auf Nachforderungen, Gebührenfragen und Anhörungen und trennt Datenkorrektur von einer ungeprüften Einlassung zu möglichen Sanktionen. |
| 10 | [Freigegebene Portalhandlungen und Nachhalten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/portalbedienung-und-nachhalten/SKILL.md) | Begleitet optional Registrierung und Portalbearbeitung bei verfügbarem Werkzeug. Verlangt Berechtigung und konkrete Freigabe, schützt persönliche Authentifizierung und verhindert Doppelmeldungen. |
| 11 | [Hauptproblem: Unklare Kontrolle unter Meldedruck](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/hauptproblem-unklare-kontrolle-loesen/SKILL.md) | Löst den typischen Engpass widersprüchlicher Pool- und Vertretungsunterlagen bei dringender Registermeldung: belastbare Varianten, gezielte Rückfragen und das jetzt notwendige vollständige Dokument. |

<!-- decimal-anchor --> <a id="portalbedienung-und-verantwortung"></a>

## 1.8. Portalbedienung und Verantwortung

Das Plugin enthält keine Zugangsdaten und keine vorkonfigurierte Portalverbindung. Bei vorhandenem Browserwerkzeug und berechtigtem Zugang kann es den konkret beauftragten Vorgang agentisch begleiten. Login, Passwort, MFA und persönliche Identitätsprüfung erledigt die berechtigte Person selbst. Geheimnisse werden nicht gespeichert.

**Eine Registrierung ist keine Versand- oder Zahlungsfreigabe.** Vor einer externen Erklärung steht der vollständige konkrete Datensatz mit Zeiträumen, Anlagen und erkennbaren Kosten zur Prüfung bereit. Eine bereits erteilte passende Freigabe wird genutzt; wesentliche Änderungen werden erneut vorgelegt. Bei fehlendem Werkzeug entsteht ein vollständiges Übergabepaket. Ein unklarer Versandstatus wird vor einem weiteren Versand geprüft.

PEP-Prüfung und wirtschaftliche Berechtigung bleiben getrennt. Ein öffentliches Amt führt nicht automatisch zur UBO-Stellung und es gibt keinen eigenständigen PEP-Registereintrag. Die Verstärkung der Sorgfalt betrifft den jeweiligen Verpflichteten, nicht unterschiedslos jede Gesellschaft.

<!-- decimal-anchor --> <a id="drei-testakten"></a>

## 1.9. Drei Testakten

Alle Personen, Unternehmen, Registerkennungen und Behördenvorgänge in den Akten sind erfunden. Die finnische Amtsträgerin ist eine reine Kunstfigur und stellt keine reale Politikerin dar. Kontakte verwenden reservierte `.example`-Domains. Die Akten enthalten keine Musterlösung und keine nachgebildeten amtlichen Siegel oder Ausweisdokumente.

<!-- reserved-example-contacts -->

- [Spree Aurora und die finnische Beteiligung](../testakten/transparenzregister-spree-aurora/README.md): 24 Originaldateien mit Poolkonflikt, PEP-Eigenerklärung, Mittelherkunft, Bankkorrespondenz und fehlender Versandbestätigung.
- [Kranichhof und der Poolnachtrag](../testakten/transparenzregister-kranichhof/README.md): 24 Originaldateien mit Komplementärstruktur, bedingtem Poolwechsel, Kündigung, Registerhistorie und Unstimmigkeitsverfahren.
- [Stifterglück und das Familienvermögen](../testakten/transparenzregister-stifterglueck/README.md): 24 Originaldateien zu nichtrechtsfähiger Stiftung, Anteilstreuhand, Minderjährigem, Einsicht und Schutzbegehren.

Die jeweiligen Aktenseiten enthalten Gesamt-PDF, Originaldateien und Einzel-PDF-Downloads mit dem zugehörigen Herkunftshinweis.

<!-- decimal-anchor --> <a id="qualität-und-grenzen"></a>

## 1.10. Qualität und Grenzen

Rechts- und Quellenprüfung: 01.10.2026. Vier Entscheidungen wurden anhand amtlicher Volltextpassagen ausgewertet; der Quellenbericht benennt den tatsächlich gelesenen Umfang. Die 2026-Rechtsprechung ersetzt keine spätere Aktualitätsprüfung. Das Werkzeug ist ein Experiment und keine eigenständige Rechtsberatung. Verantwortliche Rechtsprüfung, echte Berechtigung und verlässliche Fristenkontrolle bleiben erforderlich.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

<!-- decimal-anchor --> <a id="orientierung-nach-arbeitslogik"></a>

## 1.11. Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und Berechtigung | [`hauptproblem-unklare-kontrolle-loesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/hauptproblem-unklare-kontrolle-loesen/SKILL.md), [`registervorgang-aufnehmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registervorgang-aufnehmen/SKILL.md) |
| 2. Kontrolle und Sonderstrukturen | [`kontrollketten-und-stimmrechte-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/kontrollketten-und-stimmrechte-pruefen/SKILL.md), [`treuhand-stiftung-und-trust-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/treuhand-stiftung-und-trust-pruefen/SKILL.md), [`pep-und-mittelherkunft-trennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/pep-und-mittelherkunft-trennen/SKILL.md) |
| 3. Meldung und Aufklärung | [`erstmeldung-vollstaendig-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/erstmeldung-vollstaendig-vorbereiten/SKILL.md), [`aenderung-und-berichtigung-ordnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/aenderung-und-berichtigung-ordnen/SKILL.md), [`unstimmigkeiten-pruefen-und-beantworten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/unstimmigkeiten-pruefen-und-beantworten/SKILL.md), [`registerkorrespondenz-und-anhoerung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registerkorrespondenz-und-anhoerung/SKILL.md) |
| 4. Einsicht und Portalvollzug | [`einsicht-und-datenschutz-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/einsicht-und-datenschutz-steuern/SKILL.md), [`portalbedienung-und-nachhalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/portalbedienung-und-nachhalten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.12. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`aenderung-und-berichtigung-ordnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/aenderung-und-berichtigung-ordnen/SKILL.md) | Rekonstruiert Registerzeiträume, trennt neue Ereignisse von früheren Fehlern und erstellt konsistente Änderungs- oder Berichtigungsdaten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/aenderung-und-berichtigung-ordnen/SKILL.md) |
| [`einsicht-und-datenschutz-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/einsicht-und-datenschutz-steuern/SKILL.md) | Begründet Einsichtsanträge nach der passenden Berechtigungsgruppe, prüft Schutzbeschränkungen und trennt Abruf von weiterer Veröffentlichung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/einsicht-und-datenschutz-steuern/SKILL.md) |
| [`erstmeldung-vollstaendig-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/erstmeldung-vollstaendig-vorbereiten/SKILL.md) | Erstellt aus einer geklärten Kontrollstruktur einen vollständigen Transparenzregisterdatensatz samt Nachweisen und überprüfbarer Freigabeansicht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/erstmeldung-vollstaendig-vorbereiten/SKILL.md) |
| [`hauptproblem-unklare-kontrolle-loesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/hauptproblem-unklare-kontrolle-loesen/SKILL.md) | Löst den typischen Engpass widersprüchlicher Pool- und Vertretungsunterlagen bei dringender Registermeldung: belastbare Varianten, gezielte Rückfragen und das jetzt notwendige vollständige Dokument. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/hauptproblem-unklare-kontrolle-loesen/SKILL.md) |
| [`kontrollketten-und-stimmrechte-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/kontrollketten-und-stimmrechte-pruefen/SKILL.md) | Ermittelt natürliche wirtschaftlich Berechtigte aus Kapital, Stimmen, Pool-, Organ- und Vetorechten über mehrere Gesellschaftsebenen. Verhindert schematische Quotenmultiplikation. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/kontrollketten-und-stimmrechte-pruefen/SKILL.md) |
| [`pep-und-mittelherkunft-trennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/pep-und-mittelherkunft-trennen/SKILL.md) | Prüft politische Exponiertheit und verstärkte Sorgfalt getrennt von der wirtschaftlichen Berechtigung und begrenzt die Datenweitergabe auf den konkreten Zweck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/pep-und-mittelherkunft-trennen/SKILL.md) |
| [`portalbedienung-und-nachhalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/portalbedienung-und-nachhalten/SKILL.md) | Begleitet optional Registrierung und Portalbearbeitung bei verfügbarem Werkzeug. Verlangt Berechtigung und konkrete Freigabe, schützt persönliche Authentifizierung und verhindert Doppelmeldungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/portalbedienung-und-nachhalten/SKILL.md) |
| [`registerkorrespondenz-und-anhoerung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registerkorrespondenz-und-anhoerung/SKILL.md) | Erstellt präzise Antworten auf Nachforderungen, Gebührenfragen und Anhörungen und trennt Datenkorrektur von einer ungeprüften Einlassung zu möglichen Sanktionen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registerkorrespondenz-und-anhoerung/SKILL.md) |
| [`registervorgang-aufnehmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registervorgang-aufnehmen/SKILL.md) | Bestimmt für einen konkreten Transparenzregistervorgang Rechtseinheit, Rolle, Mitteilungspflicht und den nächsten Arbeitsauftrag. Nutzt vorhandene Unterlagen und führt direkt zum benötigten Dokument. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/registervorgang-aufnehmen/SKILL.md) |
| [`treuhand-stiftung-und-trust-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/treuhand-stiftung-und-trust-pruefen/SKILL.md) | Trennt die Meldung einer Gesellschaft von einer möglichen eigenen Registerpflicht einer Treuhand oder Stiftung und ermittelt funktionsbezogene Berechtigte. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/treuhand-stiftung-und-trust-pruefen/SKILL.md) |
| [`unstimmigkeiten-pruefen-und-beantworten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/unstimmigkeiten-pruefen-und-beantworten/SKILL.md) | Vergleicht Registerdaten mit eigenen Erkenntnissen und erstellt eine rollengerechte Unstimmigkeitsmeldung oder Verfahrensantwort samt Belegen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=transparenzregister-assistent/skills/unstimmigkeiten-pruefen-und-beantworten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
