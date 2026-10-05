<!-- decimal-anchor --> <a id="playbook-prüfer"></a>

# 1. Playbook-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="was-ist-das-hier"></a>

## 1.1. Was ist das hier?

Verträge regelweise an freigegebenen Kanzlei-Playbooks prüfen: Themen, Ausgangspositionen, Kompromisse und rote Linien mit Originalzitaten und Word-Bericht.

Dieses Plugin gehört zum Marketplace mit 275 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

<!-- decimal-anchor --> <a id="welche-datei-wofür--which-file-should-i-use"></a>

## 1.2. Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`playbook-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/playbook-pruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/playbook-pruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/playbook-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

<!-- decimal-anchor --> <a id="in-30-sekunden-starten"></a>

## 1.3. In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/playbook-pruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Playbook-Prüfer:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Erstelle den vollständigen Prüfbericht zum aktuellen Vertrag und seinen Anlagen anhand des freigegebenen Playbooks; bewerte jede Regel mit Originalfundstelle, zähle rote Linien wörtlich und formuliere die beauftragten Änderungen aus. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

<!-- decimal-anchor --> <a id="downloads"></a>

## 1.4. Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`playbook-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/playbook-pruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`playbook-pruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-schnellstart.md) · [`playbook-pruefer-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`playbook-pruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-werkstatt.md) · [`playbook-pruefer-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-hauptproblem.md" download>playbook-pruefer-hauptproblem.md</a> · [`playbook-pruefer-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/playbook-pruefer-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 275 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

<!-- decimal-anchor --> <a id="zugeordnete-testakten"></a>

## 1.5. Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Spreebogen und der Arbeitsvertrag von Nora Aydin](../testakten/playbook-arbeitsvertrag-spreebogen/README.md) | [Gesamt-PDF](../testakten/playbook-arbeitsvertrag-spreebogen/gesamt-pdf/playbook-arbeitsvertrag-spreebogen_gesamt.pdf) | [`testakte-playbook-arbeitsvertrag-spreebogen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-playbook-arbeitsvertrag-spreebogen.zip) | [`testakte-playbook-arbeitsvertrag-spreebogen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-playbook-arbeitsvertrag-spreebogen-einzelpdfs.zip) |
| [Kupferfink und das NDA für Federlicht](../testakten/playbook-nda-kupferfink/README.md) | [Gesamt-PDF](../testakten/playbook-nda-kupferfink/gesamt-pdf/playbook-nda-kupferfink_gesamt.pdf) | [`testakte-playbook-nda-kupferfink.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-playbook-nda-kupferfink.zip) | [`testakte-playbook-nda-kupferfink-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-playbook-nda-kupferfink-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

<!-- decimal-headings -->
Verträge anhand der eigenen Verhandlungsstandards prüfen: Themen, Ausgangspositionen, geordnete Rückfälle und rote Linien werden bis auf einzelne Regeln ausgewertet. Jeder Befund erhält einen konkreten Vertragsbeleg; das Ergebnis sind Themenrisiken, ein strukturierter Bericht und bei Auftrag vollständig formulierte Änderungen.

Das Plugin enthält **zehn Fachskills und einen zusätzlichen Hauptskill**. Werkstatt, Mini-Prompt und Hauptproblem-Prompt sind eigenständig nutzbar. Zwei getrennte Testakten enthalten ein NDA beziehungsweise einen Arbeitsvertrag mit dem jeweils eigenen Unternehmensplaybook, mehreren Vertragsständen und Verhandlungsmaterial.

<!-- decimal-anchor --> <a id="so-arbeitet-der-playbook-prüfer"></a>

## 1.6. So arbeitet der Playbook-Prüfer

1. Der Hauptskill bestimmt Auftrag, vertretene Seite, freigegebenes Playbook und maßgeblichen Vertragsverbund.
2. Jede anwendbare Regel wird am Originaltext geprüft. Zitat, Fassung und Seite oder Klausel bleiben nachvollziehbar; fehlende Anlagen und widersprüchliche Entwürfe bleiben sichtbar.
3. Ausgangs- und Rückfallpositionen werden kumulativ geprüft. Für rote Linien wird ausdrücklich festgelegt, ob ein einzelnes verbotenes Merkmal oder erst eine Kombination auslöst.
4. Themenfund und Risiko werden getrennt ausgegeben. Eine erforderliche fehlende Klausel ist „Nicht gefunden“ und kann gleichzeitig hohes Risiko bedeuten.
5. Der Bericht enthält sämtliche Positions- und Regelbefunde sowie die beauftragten ausformulierten Änderungen. Eine echte Worddatei entsteht nur bei tatsächlich verfügbarer Dateierzeugung.

**Rote Linien werden wörtlich gezählt:** „2/2 erkannt“ bedeutet zwei nachgewiesene verbotene Merkmale. Nicht prüfbare Regeln stehen separat. Ein guter Durchschnitt verdeckt keine rote Linie; ein noch unbekannter Punkt senkt kein bereits belegtes hohes Risiko.

<!-- decimal-anchor --> <a id="die-elf-skills"></a>

## 1.7. Die elf Skills

| Skill | Konkretes Ergebnis |
| --- | --- |
| [Vertrag vollständig am Playbook prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-pruefung-durchfuehren/SKILL.md) | Der zusätzliche Hauptskill führt vom vorhandenen Vertrag zum vollständigen zitatbelegten Ergebnis. |
| [Passendes Playbook festlegen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-auswaehlen/SKILL.md) | Bestimmter Maßstab mit Version, Rolle, Umfang und Freigaben. |
| [Playbook-Regeln entscheidbar machen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-regeln-schaerfen/SKILL.md) | Testbare Einzelregeln mit klarer UND-/ODER-Logik und Geltungsbereich. |
| [Verbindlichen Dokumentverbund bestimmen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsstand-bestimmen/SKILL.md) | Saubere Zuordnung von Hauptvertrag, Anlagen, Alternativen und Mails. |
| [Belastbare Vertragsbelege erfassen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsbelege-erfassen/SKILL.md) | Exakte Zitate beziehungsweise nachvollziehbare Fehlstellensuche. |
| [Jede Playbook-Regel beurteilen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/regeln-beurteilen/SKILL.md) | Vollständige begründete Einzelbefunde ohne umgekehrte Redline-Zählung. |
| [Themenrisiko und Freigabebedarf bestimmen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/themenrisiken-entscheiden/SKILL.md) | Nachvollziehbare Aggregation mit konkreten nächsten Schritten. |
| [NDA am Playbook prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/nda-am-playbook-pruefen/SKILL.md) | Prüfung von Zweck, Empfängern, Ausnahmen, Laufzeit, Löschung, Rechten und Sanktionen. |
| [Arbeitsvertrag am Playbook prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/arbeitsvertrag-am-playbook-pruefen/SKILL.md) | Prüfung der Beschäftigungsbedingungen samt getrennter rechtlicher Kontrolle. |
| [Änderungen und Rückfälle ausformulieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/klauseln-und-rueckfall-verhandeln/SKILL.md) | Vollständige Ersatzklauseln und konkrete Rückfallentscheidungen. |
| [Strukturierten Prüfbericht ausgeben](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/pruefbericht-erstellen/SKILL.md) | Verwendbarer Bericht mit Regelkarten, Quellen und tatsächlichen Exporten. |

<!-- decimal-anchor --> <a id="zwei-übungsakten"></a>

## 1.8. Zwei Übungsakten

- **[Kupferfink – NDA prüfen](../testakten/playbook-nda-kupferfink/README.md):** Ein gegenseitiges NDA für das Projekt Federlicht. Das Unternehmensplaybook, verschiedene Vertragsstände, eine vorrangige Anlage und die Korrespondenz bilden einen nachvollziehbaren Verhandlungsvorgang.
- **[Spreebogen – Arbeitsvertrag prüfen](../testakten/playbook-arbeitsvertrag-spreebogen/README.md):** Arbeitgeberprüfung für Nora Aydin. Playbook, Arbeitsvertragsfassungen, Regelungen zum mobilen Arbeiten und Begleitunterlagen liefern die konkrete Prüfgrundlage.

Die Arbeitsunterlagen enthalten keine vorweggenommenen Musterbewertungen. Die Akten werden getrennt vom Plugin bereitgestellt; ihre README-Seiten führen zu den jeweiligen Downloads.

<!-- decimal-anchor --> <a id="recht-quellen-und-lokale-prüfhilfe"></a>

## 1.9. Recht, Quellen und lokale Prüfhilfe

Kanzleistandard und gesetzliche Wirksamkeit bleiben getrennt. Die beispielhaften Werte von 40 Wochenstunden oder zehn abgegoltenen Überstunden sind keine gesetzlichen Grenzen. Die [Rechtsanker](references/rechtsprechungsanker.md) enthalten gezielte Primärquellen, darunter **BAG, Urteil vom 25.03.2026 – Az. 5 AZR 108/25** zur formularmäßigen Freistellung bei jeder Kündigung. Jeder Anker erklärt seine konkrete Anwendung und Übertragungsgrenze.

Die [Prüflogik](references/prueflogik.md), [Beleg- und Berichtsvorgaben](references/beleg-und-bericht.md) sowie [NDA- und Arbeitsvertragsprüfpfade](references/nda-und-arbeitsvertrag.md) sind im Plugin enthalten. Die [optionale lokale Rechenhilfe](references/maschinenformat.md) prüft bereits erarbeitete Befunde, wörtliche Zitate, Regelvollständigkeit, Zähler und Risikozuweisung. Sie ersetzt keine Vertragsauslegung oder Rechtsprüfung und versendet keine Dokumente.

Das Plugin benötigt keine bestimmte Anbieteroberfläche. Es behauptet keine nicht vorhandenen Viewer-Markierungen, gespeicherten Projektprüfungen oder Wordexporte. Die eigenständigen Prompts liefern den vollständigen Arbeitsablauf auch ohne lokale Rechenhilfe.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

<!-- decimal-anchor --> <a id="orientierung-nach-arbeitslogik"></a>

## 1.10. Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | [`vertragsbelege-erfassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsbelege-erfassen/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`playbook-pruefung-durchfuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-pruefung-durchfuehren/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`arbeitsvertrag-am-playbook-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/arbeitsvertrag-am-playbook-pruefen/SKILL.md), [`klauseln-und-rueckfall-verhandeln`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/klauseln-und-rueckfall-verhandeln/SKILL.md), [`vertragsstand-bestimmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsstand-bestimmen/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`regeln-beurteilen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/regeln-beurteilen/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`pruefbericht-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/pruefbericht-erstellen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`nda-am-playbook-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/nda-am-playbook-pruefen/SKILL.md), [`playbook-auswaehlen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-auswaehlen/SKILL.md), [`playbook-regeln-schaerfen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-regeln-schaerfen/SKILL.md), [`themenrisiken-entscheiden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/themenrisiken-entscheiden/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.11. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsvertrag-am-playbook-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/arbeitsvertrag-am-playbook-pruefen/SKILL.md) | Prüft einen deutschen Arbeitsvertragsentwurf gegen konkrete Arbeitgeber- oder Arbeitnehmerstandards und getrennt auf rechtliche Risiken bei Arbeitszeit, Vergütung, Befristung, Freistellung und Ausschlussfristen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/arbeitsvertrag-am-playbook-pruefen/SKILL.md) |
| [`klauseln-und-rueckfall-verhandeln`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/klauseln-und-rueckfall-verhandeln/SKILL.md) | Entwirft belegbezogene Ersatzklauseln und geordnete Verhandlungsrückfälle innerhalb der tatsächlichen Befugnis und prüft neue Fassungen erneut gegen betroffene Playbook-Regeln. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/klauseln-und-rueckfall-verhandeln/SKILL.md) |
| [`nda-am-playbook-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/nda-am-playbook-pruefen/SKILL.md) | Prüft eine konkrete Geheimhaltungsvereinbarung gegen freigegebene NDA-Positionen und getrennt gegen einschlägiges deutsches Recht; erfasst Zweck, Empfänger, Ausnahmen, Laufzeit, Löschung, Restwissen und Haftung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/nda-am-playbook-pruefen/SKILL.md) |
| [`playbook-auswaehlen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-auswaehlen/SKILL.md) | Wählt für einen konkreten Vertragsprüfauftrag das tatsächlich freigegebene Playbook, klärt vertretene Seite, Version und Verhandlungsbefugnis und erstellt einen begrenzten Prüfauftrag. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-auswaehlen/SKILL.md) |
| [`playbook-pruefung-durchfuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-pruefung-durchfuehren/SKILL.md) | Hauptskill für die vollständige Prüfung eines Vertragsverbunds gegen ein Kanzlei- oder Unternehmensplaybook: bestimmt Versionen, bewertet jede Regel belegt, aggregiert Risiken und liefert Bericht sowie beauftragte Änderungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-pruefung-durchfuehren/SKILL.md) |
| [`playbook-regeln-schaerfen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-regeln-schaerfen/SKILL.md) | Überführt vorhandene Verhandlungspositionen in einzelne prüfbare Regeln mit Geltungsbereich, Einheiten, Belegen sowie ausdrücklicher UND- oder ODER-Verknüpfung, ohne Standards stillschweigend zu ändern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/playbook-regeln-schaerfen/SKILL.md) |
| [`pruefbericht-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/pruefbericht-erstellen/SKILL.md) | Erstellt den nachvollziehbaren Themen- und Regelbericht mit wörtlichen Positionszählern, Quellen, Änderungen und Freigabebedarf; erzeugt eine echte Worddatei nur bei tatsächlich verfügbarer Dateiausgabe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/pruefbericht-erstellen/SKILL.md) |
| [`regeln-beurteilen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/regeln-beurteilen/SKILL.md) | Bewertet jede anwendbare Regel belegt als erfüllt, nicht erfüllt oder nicht prüfbar; rote Linien behalten dieselbe wörtliche Logik und werden als erkannt oder nicht erkannt angezeigt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/regeln-beurteilen/SKILL.md) |
| [`themenrisiken-entscheiden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/themenrisiken-entscheiden/SKILL.md) | Aggregiert vollständige Regelbewertungen mit ausdrücklicher UND-/ODER-Logik zu Themenrisiken, hält fehlende Themen und ungeklärte Fragen sichtbar und verhindert eine Freigabe durch Durchschnittswerte. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/themenrisiken-entscheiden/SKILL.md) |
| [`vertragsbelege-erfassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsbelege-erfassen/SKILL.md) | Verknüpft jede Playbook-Regel mit exakten Zitaten und stabilen Fundorten des richtigen Vertragsstands oder mit einem dokumentierten Abwesenheitsnachweis. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsbelege-erfassen/SKILL.md) |
| [`vertragsstand-bestimmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsstand-bestimmen/SKILL.md) | Ordnet Hauptvertrag, Anlagen, E-Mails und alternative Entwürfe zu einem eindeutig bestimmten Prüfstand und verhindert die Vermischung verschiedener Vertragsfassungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=playbook-pruefer/skills/vertragsstand-bestimmen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
