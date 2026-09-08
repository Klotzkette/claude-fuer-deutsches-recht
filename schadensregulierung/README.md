# Schadensregulierung

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Schadensabwicklung für Unternehmen und Anspruchsgegner: sichert Belege, trennt Haftung und Versicherungsdeckung, prüft Personen- und Sachschäden sowie Regress und erstellt Korrespondenz, Vergleich und kontrollierte Zahlungsvorlage.

Dieses Plugin gehört zum Marketplace mit 236 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`schadensregulierung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schadensregulierung.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/schadensregulierung.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/schadensregulierung-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/schadensregulierung-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/schadensregulierung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/schadensregulierung.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Schadensregulierung:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: eine Schadenanzeige mit belegtem Ereignis, gefährdeten Belegen und offener Deckungsfrage. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`schadensregulierung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schadensregulierung.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`schadensregulierung-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/schadensregulierung-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`schadensregulierung-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/schadensregulierung-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 236 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Türvorfall am Märkischen Museum in Berlin](../testakten/schadensregulierung-ubahn-tuerunfall-berlin/README.md) | [Gesamt-PDF](../testakten/schadensregulierung-ubahn-tuerunfall-berlin/gesamt-pdf/schadensregulierung-ubahn-tuerunfall-berlin_gesamt.pdf) | [`testakte-schadensregulierung-ubahn-tuerunfall-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schadensregulierung-ubahn-tuerunfall-berlin.zip) | [`testakte-schadensregulierung-ubahn-tuerunfall-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schadensregulierung-ubahn-tuerunfall-berlin-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

## 1. Vom Vorfall zur nachvollziehbaren Regulierung

Für Rechtsabteilung, Schadenbearbeiter und Anwalt auf Unternehmens- oder Beklagtenseite. Acht Skills führen vom ersten Hinweis auf einen Schaden über Beweissicherung und Versicherungsanzeige bis zur begründeten Zahlung, Teilregulierung, Ablehnung oder Übergabe an den Prozessvertreter. Eigene Schäden des Unternehmens werden getrennt erfasst; sie verwandeln den Vorgang nicht ungefragt in eine Klägerstrategie.

Der ausführliche Werkstatt-Prompt ist der wichtigste eigenständige Arbeitsweg. Er benötigt keine installierten Skills. Der Schnellstart bildet den Kern eines überschaubaren Schadenfalls ab. Beide lesen zuerst bereitgestellte Unterlagen und fragen nur nach einer Information, die den nächsten Arbeitsschritt tatsächlich verändert.

## 2. Acht Aufgaben statt eines überfüllten Menüs

| Situation | Skill | Ergebnis |
| --- | --- | --- |
| Ein Vorfall wird erstmals gemeldet | [Schadenfall aufnehmen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenfall-aufnehmen/SKILL.md) | Fallblatt mit Zuständigkeit, Eilbedarf und nächster Handlung |
| Video, Protokoll oder Zeuge droht verloren zu gehen | [Unfallbelege sichern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/unfallbelege-sichern/SKILL.md) | Sicherungsanforderung und überprüfbare Chronologie |
| Das Unternehmen soll für den Schaden einstehen | [Haftungsweg bestimmen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/haftungsweg-bestimmen/SKILL.md) | Abgegrenzte Anspruchsprüfung mit Beweislast |
| Police, Anzeige oder Regulierungsvollmacht ist offen | [Versicherung einschalten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/versicherung-einschalten/SKILL.md) | Schadenanzeige und Deckungsabfrage |
| Verletzung, Kleidung oder Verdienstausfall wird beziffert | [Schadenpositionen prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenpositionen-pruefen/SKILL.md) | Belegte Positionsrechnung, getrennt vom Schmerzensgeld |
| Krankenkasse, Arbeitgeber oder weiterer Schädiger meldet sich | [Regress und Anspruchsübergang](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regress-und-anspruchsuebergang/SKILL.md) | Gläubiger- und Zahlungszuordnung ohne Doppelausgleich |
| Ein Betroffener wartet auf eine sachgerechte Antwort | [Regulierung korrespondieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regulierung-korrespondieren/SKILL.md) | Empfängerfertiges Schreiben statt bloßer Textbausteine |
| Teilzahlung, Vergleich oder Aktenabschluss steht an | [Vergleich und Zahlung abschließen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/vergleich-und-zahlung-abschliessen/SKILL.md) | Freigabevorlage, Vereinbarung und Abschlusskontrolle |

Beginnen Sie beispielsweise mit: „Die Unterlagen liegen im freigegebenen Ordner. Wir sind das in Anspruch genommene Unternehmen. Erstellen Sie zunächst die Schadenanzeige an unseren Versicherer und sichern Sie den nächsten Belegverlust.“ Wenn stattdessen eine konkrete Antwort oder ein Vergleich gewünscht ist, wird unmittelbar daran gearbeitet.

## 3. Fachliche Grenzen, die Geld und Zeit sparen

Bei einer U-Bahn ist insbesondere das Haftpflichtgesetz zu prüfen; das StVG wird nicht deshalb einschlägig, weil ein Verkehrsunternehmen beteiligt ist. Ein technisches Türsignal beweist nicht ohne Weiteres, dass kein Kleidungsstück eingeklemmt war. Die Versicherungsanzeige ersetzt weder den Haftungsnachweis noch eine Deckungszusage. Eine Zahlung an den Fahrgast erledigt keine bereits auf Krankenkasse oder Arbeitgeber übergegangenen Ansprüche.

Das Plugin erstellt keine medizinischen Diagnosen und garantiert keine Entschädigungshöhe. Es versendet keine Schreiben, unterschreibt keine Vergleiche und löst keine Zahlungen aus. Die zuständige Person prüft und autorisiert die jeweilige Außenhandlung. Ohne Dateizugriff oder Exportwerkzeug bleibt ein verwendbarer Textstand mit konkreter Lückenangabe möglich.

## 4. Berliner U-Bahn-Vorgang

Die [Akte Türvorfall Märkisches Museum](../testakten/schadensregulierung-ubahn-tuerunfall-berlin/README.md) enthält die Meldung eines Fahrgasts, Betriebsunterlagen, medizinische Unterlagen, Kaufbeleg, Versicherungsverkehr und eine Anfrage der Krankenkasse. Sie liefert Sachverhalt und Belege, keine Lösung. Gesamt-PDF, Einzel-PDF-ZIP und ein flaches ZIP der Originalformate stehen auf der Aktenseite bereit.

## 5. English Summary

This is a compact defendant-side claims-handling workflow for companies and their lawyers. Eight focused skills cover incident intake, evidence preservation, liability, insurance, loss assessment, transferred claims, correspondence and settlement/payment control. The detailed workshop and the short prompt work independently of the installed plugin. The Berlin underground incident file is available separately in combined PDF, individual-PDF ZIP and original-format ZIP versions. No message, settlement or payment is executed automatically.

## 6. Quellen und Pflege

Die [fachlichen Quellen](references/haftung-und-regulierung.md) erläutern die verwendeten Normen und die Reichweite der Entscheidungsanker. Prüfstand: 8. September 2026. Vor einer rechtlichen Freigabe sind Ereignisdatum, maßgebliche Fassung und eine etwaige Fortentwicklung zu prüfen. Eine Quellenlücke wird nicht durch ein erfundenes Urteil ersetzt.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | [`unfallbelege-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/unfallbelege-sichern/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`haftungsweg-bestimmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/haftungsweg-bestimmen/SKILL.md), [`regress-und-anspruchsuebergang`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regress-und-anspruchsuebergang/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`vergleich-und-zahlung-abschliessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/vergleich-und-zahlung-abschliessen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`regulierung-korrespondieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regulierung-korrespondieren/SKILL.md), [`schadenfall-aufnehmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenfall-aufnehmen/SKILL.md), [`schadenpositionen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenpositionen-pruefen/SKILL.md), [`versicherung-einschalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/versicherung-einschalten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`haftungsweg-bestimmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/haftungsweg-bestimmen/SKILL.md) | Prüft die Verantwortlichkeit des in Anspruch genommenen Unternehmens aus Vertrag, Delikt und einschlägiger Gefährdungshaftung. Unterscheidet U-Bahn und Straßenverkehr, Betreiber und Hersteller sowie Haftung, Mitverschulden und Beweislast... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/haftungsweg-bestimmen/SKILL.md) |
| [`regress-und-anspruchsuebergang`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regress-und-anspruchsuebergang/SKILL.md) | Ordnet Schadenforderungen zwischen Geschädigtem, Krankenkasse, Arbeitgeber und Sachversicherer zu. Prüft kongrünte Leistungszeiträume, Anspruchsübergänge und Rückgriff gegen weitere Verantwortliche; verhindert Doppelzahlungen und eine Ab... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regress-und-anspruchsuebergang/SKILL.md) |
| [`regulierung-korrespondieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regulierung-korrespondieren/SKILL.md) | Formuliert konkrete Eingangsbestätigungen, begrenzte Belegnachforderungen, Zwischenbescheide, Teilregulierungen und begründete Ablehnungen im Schadenfall. Schreibt aus Sicht des Unternehmens respektvoll und klar, ohne verdeckte Anerkennt... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/regulierung-korrespondieren/SKILL.md) |
| [`schadenfall-aufnehmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenfall-aufnehmen/SKILL.md) | Beginnt die Schadenabwicklung auf Unternehmens- oder Beklagtenseite aus Meldung und Aktenordner. Bestimmt Vorfall, Beteiligte, Verletzung, Belegverlust, Versicherungsanzeige und Verantwortlichen; liefert das Fallblatt und den nächsten ko... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenfall-aufnehmen/SKILL.md) |
| [`schadenpositionen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenpositionen-pruefen/SKILL.md) | Prüft geltend gemachte Personen- und Sachschäden positionsweise anhand von Befunden, Kaufbelegen und Ausfällen. Trennt Schmerzensgeld, Kleidung, Behandlungskosten und Verdienstausfall, berücksichtigt psychische Unfallfolgen ohne Eigendia... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/schadenpositionen-pruefen/SKILL.md) |
| [`unfallbelege-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/unfallbelege-sichern/SKILL.md) | Sichert flüchtige Belege zu einem Schadenfall: Video, Tür- und Betriebsprotokolle, Produkt oder beschädigte Sache, Zeugen und Behandlungsunterlagen. Trennt eigene Wahrnehmung, Zeitstempel und Schlussfolgerung und formuliert konkrete Sich... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/unfallbelege-sichern/SKILL.md) |
| [`vergleich-und-zahlung-abschliessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/vergleich-und-zahlung-abschliessen/SKILL.md) | Führt eine geprüfte Schadenforderung zur kontrollierten Teilzahlung, Abfindung oder Ablehnung und zum Aktenabschluss. Klärt Vollmacht, Versichererfreigabe, Anspruchsinhaberschaft, Zukunftsschäden, Anrechnung und Zahlungsempfänger; erstel... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/vergleich-und-zahlung-abschliessen/SKILL.md) |
| [`versicherung-einschalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/versicherung-einschalten/SKILL.md) | Erstellt die Haftpflicht-Schadenanzeige und klärt Police, versichertes Unternehmen, Tätigkeit, Zeitraum, Selbstbehalt, Deckung und Regulierungsvollmacht. Erkennt Anzeige- und Prozessfristen, trennt Vorbehalt von Deckungszusage und vermei... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schadensregulierung/skills/versicherung-einschalten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
