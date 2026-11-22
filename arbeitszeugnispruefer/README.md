# Arbeitszeugnisse prüfen und analysieren

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft Arbeitszeugnisse aus Arbeitnehmersicht: gezielte Rückfragen, vertiefte Rechtsprechung, belegbare Änderungen, kurzer Mandantenbrief und passendes Arbeitgeberschreiben. Führt den Fall bis zur Kontrolle der Neufassung; auch für Chat und Word ausgearbeitet.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.11/arbeitszeugnispruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/arbeitszeugnispruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitszeugnispruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/arbeitszeugnispruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Arbeitszeugnisprüfer:

> Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Stelle der sichtbaren Ausgabe weder einen Statuskopf noch einen Datei-, Metadaten-, Rollen-, Aktenstands- oder Bearbeitungsblock voran. Beginne unmittelbar mit folgendem Arbeitsschritt: die vollständige Arbeitnehmerprüfung mit ausführlicher Analyse, konkreten Ersatzsätzen, kurzem Mandantenschreiben und – bei tragfähiger Änderung oder wirklichem Verhandlungswunsch – abgestuftem Arbeitgeberschreiben. Fehlt ein klarer Gegenhinweis, arbeite auf Arbeitnehmerseite. Ein in den Chat kopierter Prompt wird interaktiv bearbeitet und ist kein automatischer Einmalauftrag. Auch eine einzelne hochgeladene Promptdatei startet ohne Plugin oder zusätzliche Startformel; fasse sie nicht ungefragt zusammen. Fehlt das Zeugnis, bitte um die vollständige Fassung, das Prüfziel und eine erkennbare dringende Frist. Bei vollständigen Angaben beginne unmittelbar mit den Ergebnissen. Fehlt eine entscheidungserhebliche Tatsache, beginne mit der Rückfrage. Stelle nur entscheidungserhebliche Rückfragen zusammengehörig, nenne ihre Folgen und warte auf die tatsächliche Antwort; gesicherte Teile dürfen vorläufig weiterbearbeitet werden. Setze danach am bestehenden Stand fort und liefere die vollständige Analyse sowie die angezeigten Schreiben ohne neuen Auftrag. Übernimm Teilantworten und kläre nur entscheidende Restlücken oder Widersprüche. Ist ein Beleg endgültig nicht beschaffbar, begrenze das Begehren und beende die Suchschleife. Neue Arbeitgeberantworten und Korrekturfassungen führen zur gezielten Nachprüfung und zu den nötigen Folgeschreiben. Bei ausdrücklich nichtinteraktiver Bearbeitung verwende Platzhalter oder bedingte Varianten, nie erfundene Antworten. Ist keine Änderung vertretbar und keine Verhandlung gewünscht, erläutere dies im Mandantenschreiben und erzeuge kein künstliches Arbeitgeberschreiben.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.11/arbeitszeugnispruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`arbeitszeugnispruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`arbeitszeugnispruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [beide Aktenbestände](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| Pluginlokale Akte | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf) | [`arbeitszeugnispruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte.zip) | [`arbeitszeugnispruefer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte-einzelpdfs.zip) |
| [Arbeitszeugnis-Analyse — aus dem blühenden Leben](../testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) | [Gesamt-PDF](../testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-ergaenzung-v1.0.0/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Prüfe und analysiere ein vorliegendes deutsches Arbeitszeugnis bis zum beauftragten Ergebnis. Der gemeinsame Prüfer verbindet die ausführliche Arbeitnehmerberatung mit begrenzten Analyseaufträgen, Satz- und Fassungsvergleichen sowie den besonderen Fragen von Ausbildung und Führung. Die [Arbeitsmodi](references/arbeitszeugnis-auslegung-und-arbeitsmodi.md) zeigen, welche Unterlagen und Endprodukte zum konkreten Auftrag gehören.

## Floristik und Kassenabschluss

Beginnen Sie mit der Eingangspost und vergleichen Sie die Beobachtungen zum Kassenabschluss mit der Darstellung im Zeugnis. [Fallordner im Druckpaket nachschlagen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/docs/grundakten-lebenswelt/README.md#weitere-arbeitsakten-und-eigenständige-pluginfassungen).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fall | Originalunterlagen und Eingangspost | Lesefassungen |
| --- | --- | --- |
| Floristik – der Kassenabschluss | [Arbeits-ZIP mit Eingangspost](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-lebenswelt-v1.0.0/lebensakte-arbeitszeugnis-floristik-kassenabschluss.zip) | [Druckpaket 04](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-lebenswelt-v1.0.0/lesepaket-04.zip) |

## Wenn du das brauchst

- **Arbeitnehmerinnen und Arbeitnehmer** wollen eine verständliche Prüfung, konkrete Ersatzsätze und eine realistische Empfehlung.
- **Kanzleien** erhalten einen ausführlichen Prüfvermerk, genaue Ersatzformulierungen, einen kurzen Mandantenbrief und bei tragfähiger Änderung oder tatsächlichem Verhandlungswunsch das passende Arbeitgeberanschreiben.
- **Arbeitgeber und Personalabteilungen** wollen vor Erteilung oder Berichtigung eine wahrheitsgemäße, klare und widerspruchsfreie Gesamtfassung.
- **Beratungsstellen** benötigen eine sachliche Einordnung, ohne eine nicht beauftragte Parteimaßnahme zu erzeugen.

## Was du am Ende in der Hand hast

Der allgemeine Arbeitnehmer-Prüfauftrag umfasst die ausführliche Analyse, genaue Ersatzsätze, den kurzen verständlichen Mandantenbrief und das fachlich angezeigte Arbeitgeberanschreiben. Beide Schreiben werden nach Klärung der erheblichen Tatsachen ohne weiteren Entwurfsauftrag fertiggestellt. Nur ohne tragfähigen Änderungspunkt und ohne Verhandlungswunsch entfällt das Arbeitgeberanschreiben. Klage, Vergleich und Vollstreckung bleiben ausdrücklich beauftragte Folgearbeit.

## Der Weg dorthin

Zeugnis lesen → konkrete Fragen und Belege klären → tatsächliche Antworten auswerten → erforderlichenfalls gezielt nachfragen → ausführliche Prüfung und beide passenden Schreiben erstellen → Arbeitgeberantwort und vollständige neue Zeugnisfassung kontrollieren → Restpunkte weiterbearbeiten oder abschließen.

## Rückfragen und Verzweigungen

Gefragt wird nur, wenn die Antwort Bewertung, Ersatzwortlaut, Frist, Beweisführung oder Enddokument verändert. Die Rückfrage ist stets ein Zwischenschritt: Der gesicherte Teil wird schon ausgearbeitet, die möglichen Antworten werden als Varianten abgebildet und nur der abhängige Teil bleibt vorläufig. Nach der Antwort geht es am bestehenden Bearbeitungsstand weiter.

Teilantworten, unbekannte Informationen und widersprüchliche Belege erhalten eigene Folgeschritte. Ist ein Beleg nicht beschaffbar, wird der Fall nach der richtigen Beweislast eingeordnet und nicht endlos weiterbefragt. Bei ausreichenden Angaben folgen unmittelbar die Analyse und die geschuldeten Schreiben. Ein bloßer Dateianhang startet denselben Dialog ohne zusätzlichen Starter; Versand und gerichtliche Schritte bleiben freigabepflichtig.

Die unabhängigen [Dialogproben](../docs/arbeitszeugnis-dialogpruefung.md) dokumentieren tatsächlich erzeugte Antworten und ihre Grenzen. Sie sind keine pauschale Funktionsgarantie für fremde Chatbots.

## 1. Arbeitsbuch und konkrete Fallprüfung

Das [Arbeitsbuch](references/arbeitszeugnis-handbuch.md) ergänzt die Prüfung um ausführliche Entscheidungsbesprechungen, Beweisfragen, Gegenfälle und eigene Mandatsbeispiele. Kapitel 20 führt durch Chat, Plugin und Word; Kapitel 21 behandelt Leistung, Verhalten und Beweise; Kapitel 22 Schlussformeln, Bindung und Status; Kapitel 23 Form, Fristen und Verfahren. Die Skills ziehen die zum Fall passenden Teile heran und arbeiten danach bis zu den geschuldeten Entwürfen weiter. Das Buch ersetzt weder die Prüfung der Originalunterlagen noch die aktuelle Verifikation einer tragenden Quelle.

Bei einem Zeugnisvergleich prüft der Hauptskill den vereinbarten Wortlaut, den letzten Entwurf und die tatsächlich erteilte Fassung. Das Arbeitsbuch zeigt in Abschnitt 22.2.11, wann „viel Erfolg“ die vereinbarte Schlussformel erfüllt. Abschnitt 23.8.7 behandelt den Fall, dass eine einzige wesentliche Tätigkeit streitig bleibt. Für Ausbildungszeugnisse unterscheiden die Fachmodule den gesetzlichen Pflichtinhalt von einer zusätzlich verlangten Leistungs- und Verhaltensbeurteilung.

Die [Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md) enthält das Arbeitsbuch vollständig und kann als einzelne Datei verwendet werden. Das Plugin nutzt dieselbe Fassung als mitgepackte Referenz; die Werkstatt selbst bleibt außerhalb des Pluginpakets. Alle 78 Fachvertiefungen sind über 8 Skills erreichbar, und der [kleine Schnellstart](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md) wird nicht zum Handbuch aufgebläht. Bei Word richtet sich die Bearbeitung nach den tatsächlich verfügbaren Lese- und Änderungsfunktionen. Ohne Dateiexport werden die vollständigen Texte im Chat ausgegeben; eine nicht erzeugte Datei wird nicht behauptet.

Die neuen Prüffälle für Einzeldateinutzung, Word-Zugriffsgrenzen und Bindung sind im [Qualitätsprofil](../quality/evals/arbeitszeugnispruefer.json) festgehalten. Ihre Ergänzung ist noch kein durchgeführter Verhaltenstest; tatsächlich erfolgte Prüfungen und verbleibende Grenzen stehen im [Änderungsbericht](../quality/arbeitszeugnispruefer/handbuch-2026-10-08/plugin-anbindung.md).

## Aussage, Beleg und Neufassung

Werkstatt und Mini führen Belege jetzt enger auf ihren tatsächlichen Zeitraum, persönlichen Anteil und Bewertungsbereich zurück. Eine gute Teilbewertung erzwingt keine höhere Gesamtnote. Bei einer angegriffenen schlechten Note und einer gewünschten guten Note werden Abwehr der Abwertung und weitere Aufwertung getrennt begründet.

Ersatzsätze sind konkrete Vorschläge; eine Bindung an genau diese Wörter wird nur bei entsprechender Grundlage angenommen. Neue Zeugnisse werden vollständig und nach ihrem Bedeutungsgehalt verglichen: Gleichwertige Korrekturen werden akzeptiert, neue nachteilige Änderungen und unbelegte alte Aussagen gesondert geprüft. Analyse, Ersatztexte und Briefe müssen dasselbe Begehren tragen.

Einfaches Zeugnis, Ausbildungszeugnis und verweigerte Erteilung haben eigene fachliche Wege. Die Werkstatt vertieft außerdem ursprüngliches Ausstellungsdatum, geeignete Unterzeichnung und Zwischenzeugnisbindung nach einem Betriebsübergang. Die [Quellenprüfung](../quality/arbeitszeugnispruefer/verfeinerung-2026-09-30/quellenpruefung.md) unterscheidet amtliche Texte, Gerichtsfassungen auf nichtamtlichen Hosts und redaktionelle Altvolltexte. Das Plugin verbindet 78 Fachvertiefungen in 8 Skills; der Mini bleibt höchstens 7.500 UTF-8-Bytes. Drei [unabhängige Fallproben](../quality/arbeitszeugnispruefer/verfeinerung-2026-09-30/README.md) dokumentieren die tatsächlich erzeugten Antworten, einschließlich zwei mehrstufiger Dialoge.

## Fachliche Leitlinien

- Einzelne Wörter und vermeintliche Geheimcode-Listen ersetzen nicht die Auslegung des gesamten Zeugnisses aus objektiver Empfängersicht.
- Eine bessere Gesamtbewertung als „zur vollen Zufriedenheit“ muss durch konkrete bessere Leistungen getragen werden.
- Auslassungen und die Reihenfolge von Personengruppen werden nur anhand der tatsächlichen Tätigkeit und der konkreten Textwirkung beanstandet.
- Dank, Bedauern und Zukunftswünsche werden getrennt von der Leistungs- und Verhaltensnote geprüft und sind regelmäßig freiwillig.
- Papierausfertigung und elektronische Form mit Einwilligung und qualifizierter elektronischer Signatur werden getrennt beurteilt.

## Rechtlicher Anker

- Paragraf 109 GewO zu Inhalt, Klarheit und Form des Arbeitszeugnisses
- Paragraf 16 BBiG für Ausbildungszeugnisse
- BAG, Urteil vom 18. November 2014 – 9 AZR 584/13 zur überdurchschnittlichen Gesamtbewertung
- BAG, Urteil vom 15. November 2011 – 9 AZR 386/10 zur kontextbezogenen Zeugnisklarheit
- BAG, Urteil vom 11. Dezember 2012 – 9 AZR 227/11 und Urteil vom 25. Januar 2022 – 9 AZR 146/21 zur Schlussformel
- [BAG, Teilurteil vom 18. Juni 2025, 2 AZR 96/24 (B)](https://www.bundesarbeitsgericht.de/wp-content/uploads/2025/09/2-AZR-96-24--B.pdf): kein wirksamer Vorausverzicht auf das künftige qualifizierte Zeugnis vor Ende des Arbeitsverhältnisses; spätere Vereinbarungen getrennt prüfen.
- [BAG, Beschluss vom 7. Mai 2026, 8 AZB 25/25](https://www.bundesarbeitsgericht.de/entscheidung/8-azb-25-25/): ein vereinbartes Entwurfsrecht kann vollstreckbar sein. Nachvollziehbare Einwendungen gegen Wahrheit oder Klarheit können trotzdem ein neues Erkenntnisverfahren erforderlich machen.

## KI-Verordnung: mögliche Einstufung als Hochrisiko-KI

Die rechtliche Prüfung eines vorgelegten Zeugnisses für einen Arbeitnehmer ist nicht allein wegen ihres Personalbezugs ein Hochrisikofall. Maßgeblich sind das konkrete System, seine Zweckbestimmung und seine Einbindung in Entscheidungen. Wird es für die Bewertung von Beschäftigten oder Entscheidungen über Arbeitsbedingungen eingesetzt, ist Anhang III Nummer 4 Buchstabe b zu prüfen; bei Bewerberauswahl kommt Buchstabe a in Betracht. Die Ausnahmen des Artikels 6 Absatz 3 und deren Grenzen sind gesondert zu prüfen. Eine menschliche Schlussfreigabe befreit nicht automatisch. Der [Hochrisiko-Prüfer](../ki-verordnung-hochrisiko-pruefer/README.md) führt diese Einordnung anhand der tatsächlichen Nutzung durch.

Folgen einer Einstufung als Hochrisiko-KI können sein: Pflicht zu menschlicher Aufsicht, Dokumentations- und Transparenzpflichten, Risikomanagement, Information der Beschäftigten beziehungsweise des Betriebsrats und gegebenenfalls eine Grundrechte-Folgenabschätzung. Die genaue Reichweite hängt vom Einsatzkontext, von der Rolle als Anbieter oder Betreiber und vom Geltungsbeginn nach Artikel 113 KI-VO ab. Diese Hinweise sind keine Rechtsberatung; im Zweifel ist eine arbeitsrechtliche und KI-rechtliche Bewertung im Einzelfall geboten.

## Hinweise

Das Plugin ersetzt keine Prüfung des Einzelfalls durch eine hierzu befugte Person. Tatsachen, Belege, Fristen und aktuelle Quellen sind vor Versand oder Einreichung zu kontrollieren. Das Plugin unterschreibt, versendet oder reicht nichts ohne ausdrückliche Freigabe ein.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **8 auswählbare Skills**. Die **78 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/juristischer-argumentationskern/SKILL.md)  · [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/einstieg-routing/SKILL.md)  · [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/kaltstart-triage/SKILL.md) |
| 2. Zeugnisauftrag, Form und Tätigkeitsbild | [`zeugnisauftrag-form-taetigkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) |
| 3. Leistung, Verhalten und Noten | [`leistung-verhalten-noten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/leistung-verhalten-noten-bearbeiten/SKILL.md) |
| 4. Formulierungen, Klarheit und Schlussformel | [`formulierungen-klarheit-schluss-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/formulierungen-klarheit-schluss-bearbeiten/SKILL.md) |
| 5. Berichtigung, Anspruch und Verfahren | [`berichtigung-anspruch-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/berichtigung-anspruch-verfahren-bearbeiten/SKILL.md) |
| 6. Zeugnisbericht, Muster und Qualitätskontrolle | [`zeugnisbericht-muster-qualitaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisbericht-muster-qualitaet-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`berichtigung-anspruch-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/berichtigung-anspruch-verfahren-bearbeiten/SKILL.md) | Arbeitszeugnisse prüfen und berichtigen: Berichtigungsanspruch, Beweislast, Fristen, Aufforderungsschreiben und gerichtliche Durchsetzung bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/berichtigung-anspruch-verfahren-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/einstieg-routing/SKILL.md) | Arbeitszeugnis prüfen und korrigierten Text liefern. Wertet vorhandene Unterlagen aus, entscheidet die fachlichen Weichen und liefert vollständige verbesserte Zeugnisfassung und gegebenenfalls ein begründetes Berichtigungsverlangen mit p... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/einstieg-routing/SKILL.md) |
| [`formulierungen-klarheit-schluss-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/formulierungen-klarheit-schluss-bearbeiten/SKILL.md) | Arbeitszeugnisse prüfen und berichtigen: Auslassungen, Mehrdeutigkeiten, vermeintliche Codes und Schlussformeln am objektiven Empfängerhorizont prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/formulierungen-klarheit-schluss-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/juristischer-argumentationskern/SKILL.md) | Begründet erhebliche Beanstandungen eines vorhandenen Arbeitszeugnisses mit Norm, Gesamtzusammenhang, konkreter Fundstelle, Beleglage, Gegenposition und genauer Rechtsfolge und führt sie in das bestellte Dokument über. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/kaltstart-triage/SKILL.md) | Beginnt die Prüfung eines hochgeladenen Arbeitszeugnisses, erkennt entscheidende Leselücken und Fristen und arbeitet vom vorhandenen Material bis zum bestellten Entwurf weiter. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/kaltstart-triage/SKILL.md) |
| [`leistung-verhalten-noten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/leistung-verhalten-noten-bearbeiten/SKILL.md) | Arbeitszeugnisse prüfen und berichtigen: Bewertungssätze, Leistungsmerkmale und Verhalten im Gesamtzusammenhang analysieren und mit Belegen vergleichen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/leistung-verhalten-noten-bearbeiten/SKILL.md) |
| [`zeugnisauftrag-form-taetigkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) | Arbeitszeugnisse prüfen und berichtigen: Zeugnisart, Anspruch, äußere Form, Tätigkeitsdarstellung und Anlass des Zeugnisses klären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) |
| [`zeugnisbericht-muster-qualitaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisbericht-muster-qualitaet-bearbeiten/SKILL.md) | Arbeitszeugnisse prüfen und berichtigen: Analyse, Beleglücken, Ergebnisdarstellung und Formulierungsentwurf zu einem verständlichen Arbeitsprodukt verbinden. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisbericht-muster-qualitaet-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="vertiefte-ki-einstufung"></a>

## 2. Vertiefte KI-Einstufung

[Konkrete Zweckprüfung, Rechtsprechungsgrenzen und vollständige Übungsakte](references/ki-normen-und-fallpruefung.md): Arbeitnehmerberatung, Zeugnisentwurf und arbeitgeberseitiges Profiling getrennt behandeln. Eine menschliche Schlussunterschrift widerlegt maßgeblichen automatisierten Entscheidungseinfluss nicht allein.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
