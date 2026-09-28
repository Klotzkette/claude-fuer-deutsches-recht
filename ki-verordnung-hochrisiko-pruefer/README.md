# KI-Verordnung Hochrisiko-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft Software nach Artikel 6 KI-Verordnung: Produktpfad, sämtliche Anhang-III-Bereiche, Ausnahmen, Profiling und Rollenwechsel. Erstellt Einstufungen, Anbieternachforderungen und Umsetzungsdokumente. Recruiting und eigenmächtige Chatbot-Nutzung bilden den vertieften Praxisfall.

Dieses Plugin gehört zum Marketplace mit 252 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`ki-verordnung-hochrisiko-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-verordnung-hochrisiko-pruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/ki-verordnung-hochrisiko-pruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/ki-verordnung-hochrisiko-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/ki-verordnung-hochrisiko-pruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für KI-Verordnung Hochrisiko-Prüfer:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`ki-verordnung-hochrisiko-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-verordnung-hochrisiko-pruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`ki-verordnung-hochrisiko-pruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`ki-verordnung-hochrisiko-pruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 252 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Kasseler Bewerbungsauswahl](../testakten/ki-hochrisiko-bewerbungsauswahl-kassel/README.md) | [Gesamt-PDF](../testakten/ki-hochrisiko-bewerbungsauswahl-kassel/gesamt-pdf/ki-hochrisiko-bewerbungsauswahl-kassel_gesamt.pdf) | [`testakte-ki-hochrisiko-bewerbungsauswahl-kassel.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.14.0/testakte-ki-hochrisiko-bewerbungsauswahl-kassel.zip) | [`testakte-ki-hochrisiko-bewerbungsauswahl-kassel-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.14.0/testakte-ki-hochrisiko-bewerbungsauswahl-kassel-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

## 1 Zweck

Dieses Plugin prüft Software anhand beider Pfade des Artikels 6 KI-Verordnung: produktbezogene Hochrisikosysteme und sämtliche acht Bereiche des Anhangs III. Nicht jede Software ist ein KI-System, nicht jedes KI-System hochriskant. Die [bereichsübergreifende Prüfreferenz](references/artikel-6-und-anhang-iii.md) ordnet Tatbestände und Grenzen zu. Recruiting bildet den vertieften Praxisfall: Das Plugin trennt angebotenes System, konkrete Konfiguration und eigenmächtigen Beschäftigteneinsatz. Aus „Sortieren“ folgt weder stets Hochrisiko noch eine generelle Ausnahme. Menschliche Schlussentscheidung beseitigt vorgelagerten Einfluss nicht von selbst.

## 2 Einstieg

Den Fallordner bereitstellen und das gewünschte Ergebnis nennen, beispielsweise: „Prüfe die beiden Werkzeuge getrennt und schreibe der Geschäftsführung eine Entscheidungsvorlage.“ Vorhandene Unterlagen werden zuerst gelesen. Bei leerem Auftrag wird nur nach dem Ordner und dem nächsten benötigten Dokument gefragt. Ein später eingereichter Beleg wird in das bereits bestellte Dokument eingearbeitet, nicht mit einer erneuten allgemeinen Bestandsaufnahme beantwortet.

Die ausführliche [Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-werkstatt.md) führt vom Ordner bis zum verwendbaren Dokument. Der [Schnellstart](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/ki-verordnung-hochrisiko-pruefer-schnellstart.md) enthält denselben Prüfungskern in kurzer Form. [Quellen und Rechtsstand](references/rechtsstand-und-quellen.md) unterscheiden Normtext, Änderungsrecht, Entwurf und eigene Auslegung.

## 3 Navigation

| Arbeitsauftrag | Skill | Ergebnis |
| --- | --- | --- |
| Beliebige Software nach Produktpfad oder Anhang III einordnen | [Allgemeine Artikel-6-Prüfung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/artikel-6-software-einstufen/SKILL.md) | Subsumierter Einstufungsvermerk mit konkretem Folgeauftrag |
| Zwei Werkzeuge oder verschiedene Betriebsarten auseinanderhalten | [Zweck und System](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hr-zweck-und-systemabgrenzung/SKILL.md) | Versionsbezogene Systembeschreibung und gezieltes Auskunftsschreiben |
| Recruiting-Funktion rechtlich einstufen | [Hochrisiko-Einstufung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hochrisiko-einstufung-recruiting/SKILL.md) | Begründeter Einstufungsvermerk |
| Eine behauptete Ausnahme prüfen | [Ausnahmebegründung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/ausnahmebegruendung-artikel-6/SKILL.md) | Tragfähige Dokumentation oder begründete Ablehnung |
| Eigenmächtigen Chatbot-Einsatz oder Umwidmung bearbeiten | [Rollenwechsel](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rollenwechsel-und-shadow-ai/SKILL.md) | Rollenvermerk und konkrete Sicherungsweisung |
| Den tatsächlichen Personalprozess organisieren | [Betreiberkonzept](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/betreiberkonzept-bewerbungsauswahl/SKILL.md) | Ausformulierte Betriebsanweisung mit Zuständigkeiten |
| Zertifikats-, CE- und Datenbankbehauptungen prüfen | [Konformität und Registrierung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/konformitaet-und-registrierung/SKILL.md) | Nachweisprüfung und versandfertige Nachforderung |
| Beschwerde, Fehlfunktion und Meldeweg beurteilen | [Vorfallbewertung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/vorfallbewertung-und-meldeentwurf/SKILL.md) | Vorfallvermerk und erforderlichenfalls Meldeentwurf |
| Einführung, Bestandsbetrieb oder Änderung terminieren | [Rechtsstand und Einführung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rechtsstand-und-einfuehrungsentscheidung/SKILL.md) | Datierte Entscheidungsvorlage mit belastbaren Bedingungen |

## 4 Rechtsstand und Grenzen

Redaktionsstand: 28. September 2026. Die Verordnung (EU) 2026/1744 ist geltendes Änderungsrecht, nicht mehr nur der Omnibus-Vorschlag von 2025. Artikel 113 Buchstabe c verschiebt Kapitel III Abschnitte 1 bis 3 grundsätzlich auf den 2. Dezember 2027 für Anhang III und den 2. August 2028 für Anhang I. Andere Vorschriften und Artikel 111 sind jeweils gesondert zu prüfen. Die Hochrisiko-Leitlinien vom 19. Mai 2026 werden weiterhin als Entwurf veröffentlicht. Ihr Inhalt ist keine verbindliche Freistellung.

Das Plugin ersetzt weder eine technische Konformitätsprüfung noch die Entscheidung einer Behörde. Es verschickt keine Meldung und verändert keine Bewerberentscheidung ohne ausdrücklichen Auftrag. Datenschutz, Diskriminierung und Beteiligungsrechte werden bei konkreten Anhaltspunkten gesondert bearbeitet, nicht aus einer KI-Risikoklasse als miterledigt behandelt.

## 5 Übungsakte

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

[Kasseler Bewerbungsauswahl: Originalbelege und Arbeitsauftrag](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/testakten/ki-hochrisiko-bewerbungsauswahl-kassel)

## 6 Prüfung

Der lokale Regressionstest heißt `scripts/test-ki-verordnung-hochrisiko-pruefer.py`. Das getrennte Qualitätsprofil liegt unter `quality/evals/ki-verordnung-hochrisiko-pruefer.json`. Technische Prüfungen und redaktionelle Durchgänge sind keine behaupteten Live-Modelltests. Die zentrale Registrierung, Gesamt-PDFs und ZIP-Pakete werden außerhalb dieses Plugin-Builders integriert.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 3. Prüfung, Anspruch und Subsumtion | [`hochrisiko-einstufung-recruiting`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hochrisiko-einstufung-recruiting/SKILL.md), [`vorfallbewertung-und-meldeentwurf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/vorfallbewertung-und-meldeentwurf/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`betreiberkonzept-bewerbungsauswahl`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/betreiberkonzept-bewerbungsauswahl/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`artikel-6-software-einstufen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/artikel-6-software-einstufen/SKILL.md), [`ausnahmebegruendung-artikel-6`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/ausnahmebegruendung-artikel-6/SKILL.md), [`hr-zweck-und-systemabgrenzung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hr-zweck-und-systemabgrenzung/SKILL.md), [`konformitaet-und-registrierung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/konformitaet-und-registrierung/SKILL.md), [`rechtsstand-und-einfuehrungsentscheidung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rechtsstand-und-einfuehrungsentscheidung/SKILL.md), [`rollenwechsel-und-shadow-ai`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rollenwechsel-und-shadow-ai/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`artikel-6-software-einstufen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/artikel-6-software-einstufen/SKILL.md) | Ordnet beliebige Software anhand der KI-Systemdefinition, des Produktpfads aus Artikel 6 Absatz 1 und aller acht Bereiche des Anhangs III ein. Nutzen für eine konkrete Hochrisikofrage in Bildung, Infrastruktur, Biometrie, Beschäftigung,... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/artikel-6-software-einstufen/SKILL.md) |
| [`ausnahmebegruendung-artikel-6`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/ausnahmebegruendung-artikel-6/SKILL.md) | Prüft und formuliert die Anbieterbegründung einer Ausnahme nach Artikel 6 Absatz 3 und 4 einschließlich verbleibender Registrierung. Für eng begrenzte vorbereitende HR-Funktionen; erstellt keine gewünschte Freistellung ohne belegte Vorau... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/ausnahmebegruendung-artikel-6/SKILL.md) |
| [`betreiberkonzept-bewerbungsauswahl`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/betreiberkonzept-bewerbungsauswahl/SKILL.md) | Erstellt aus Freigabe, Gebrauchsanleitung und tatsächlichen Auswahlabläufen eine ausführbare Betriebsanweisung für KI im Recruiting. Nutzen, wenn menschliche Aufsicht, Eingabekontrolle, Protokolle, Beschäftigteninformation und Unterbrech... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/betreiberkonzept-bewerbungsauswahl/SKILL.md) |
| [`hochrisiko-einstufung-recruiting`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hochrisiko-einstufung-recruiting/SKILL.md) | Erstellt einen begründeten Einstufungsvermerk für KI-gestützte Bewerbungsauswahl nach Artikel 6 und Anhang III Nummer 4 Buchstabe a. Prüft Entscheidungswirkung und Profiling statt jede Sortierung oder jeden Chatbot pauschal als Hochrisik... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hochrisiko-einstufung-recruiting/SKILL.md) |
| [`hr-zweck-und-systemabgrenzung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hr-zweck-und-systemabgrenzung/SKILL.md) | Rekonstruiert aus HR-Akten Zweck, Version und tatsächlichen Einsatz mehrerer KI-Werkzeuge und erstellt eine belastbare Systembeschreibung samt gezielter Nachforderung. Für unklare Recruiting-Prozesse, nicht für allgemeine KI-Inventare. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/hr-zweck-und-systemabgrenzung/SKILL.md) |
| [`konformitaet-und-registrierung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/konformitaet-und-registrierung/SKILL.md) | Prüft Konformitätsunterlagen und Registrierungsangaben für Recruiting-KI und formuliert eine gezielte Anbieternachforderung. Trennt interne Kontrolle nach Artikel 43 von notifizierter Stelle, CE, EU-Datenbank und Vorfallmeldung. Nutzen b... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/konformitaet-und-registrierung/SKILL.md) |
| [`rechtsstand-und-einfuehrungsentscheidung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rechtsstand-und-einfuehrungsentscheidung/SKILL.md) | Erstellt eine datierte Einführungs- oder Änderungsentscheidung für Recruiting-KI mit belegten Anwendungsdaten, Übergangsrecht und konkreten Voraussetzungen. Nutzen bei Aussagen über verschobene KI-Pflichten, Digital Omnibus, Altversionen... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rechtsstand-und-einfuehrungsentscheidung/SKILL.md) |
| [`rollenwechsel-und-shadow-ai`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rollenwechsel-und-shadow-ai/SKILL.md) | Bearbeitet nicht freigegebenen Chatbot-Einsatz und Änderungen des Recruiting-Zwecks. Erstellt einen Rollenvermerk nach Artikel 25 und eine konkrete Sicherungsweisung, ohne Beschäftigten eigenständige Betreiberrollen oder Arbeitgebern pau... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/rollenwechsel-und-shadow-ai/SKILL.md) |
| [`vorfallbewertung-und-meldeentwurf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/vorfallbewertung-und-meldeentwurf/SKILL.md) | Bewertet einen konkreten Fehler oder eine Beschwerde bei KI-gestützter Personalauswahl und erstellt einen internen Vorfallvermerk sowie nötige Informations- oder Meldeentwürfe. Trennt Betreiberinformation, schwerwiegenden Vorfall und Anb... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-hochrisiko-pruefer/skills/vorfallbewertung-und-meldeentwurf/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
