# Staatsanwaltschaft Praxis-Einstieg

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Praxisplugin für neue Staatsanwaelte: Aktenstart, Anfangsverdacht, Ermittlungsauftrag, Eingriffe, Anklage, Strafbefehl, Einstellung, Sitzungsdienst, Rechtsmittel und OWiG.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`staatsanwaltschaft-praxis-einstieg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/staatsanwaltschaft-praxis-einstieg.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../../skills-index/staatsanwaltschaft-praxis-einstieg.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/staatsanwaltschaft-praxis-einstieg-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/staatsanwaltschaft-praxis-einstieg-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../../SKILLS.md) · [Skills dieses Plugins](../../skills-index/staatsanwaltschaft-praxis-einstieg.md) · [Plugin-Dateien](.) · [Download-Index](../../ASSET_INDEX.md) · [Installation](../../INSTALLATION_EINFACH.md) · [Testakten](../../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../../skills-index/staatsanwaltschaft-praxis-einstieg.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Staatsanwaltschaft Praxis-Einstieg:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`staatsanwaltschaft-praxis-einstieg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/staatsanwaltschaft-praxis-einstieg.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`staatsanwaltschaft-praxis-einstieg-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/staatsanwaltschaft-praxis-einstieg-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`staatsanwaltschaft-praxis-einstieg-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/staatsanwaltschaft-praxis-einstieg-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [9 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Betäubungsmittel-Kurierfahrt auf der A3 bei Köln](../../testakten/strafrecht-btm-kokain-kurierfahrt-a3-koeln/README.md) | [Gesamt-PDF](../../testakten/strafrecht-btm-kokain-kurierfahrt-a3-koeln/gesamt-pdf/strafrecht-btm-kokain-kurierfahrt-a3-koeln_gesamt.pdf) | [`testakte-strafrecht-btm-kokain-kurierfahrt-a3-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-btm-kokain-kurierfahrt-a3-koeln.zip) | [`testakte-strafrecht-btm-kokain-kurierfahrt-a3-koeln-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-btm-kokain-kurierfahrt-a3-koeln-einzelpdfs.zip) |
| [Phishing und Bankzugang Leipzig](../../testakten/strafrecht-cybercrime-phishing-bankzugang-leipzig/README.md) | [Gesamt-PDF](../../testakten/strafrecht-cybercrime-phishing-bankzugang-leipzig/gesamt-pdf/strafrecht-cybercrime-phishing-bankzugang-leipzig_gesamt.pdf) | [`testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig.zip) | [`testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-cybercrime-phishing-bankzugang-leipzig-einzelpdfs.zip) |
| [Häusliche Gewalt und gefährliche Körperverletzung Dresden](../../testakten/strafrecht-haeusliche-gewalt-koerperverletzung-dresden/README.md) | [Gesamt-PDF](../../testakten/strafrecht-haeusliche-gewalt-koerperverletzung-dresden/gesamt-pdf/strafrecht-haeusliche-gewalt-koerperverletzung-dresden_gesamt.pdf) | [`testakte-strafrecht-haeusliche-gewalt-koerperverletzung-dresden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-haeusliche-gewalt-koerperverletzung-dresden.zip) | [`testakte-strafrecht-haeusliche-gewalt-koerperverletzung-dresden-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-haeusliche-gewalt-koerperverletzung-dresden-einzelpdfs.zip) |
| [Jugendstrafsache Schulhofraub Hamburg-Wilhelmsburg](../../testakten/strafrecht-jugendlicher-raub-schulhof-hamburg/README.md) | [Gesamt-PDF](../../testakten/strafrecht-jugendlicher-raub-schulhof-hamburg/gesamt-pdf/strafrecht-jugendlicher-raub-schulhof-hamburg_gesamt.pdf) | [`testakte-strafrecht-jugendlicher-raub-schulhof-hamburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-jugendlicher-raub-schulhof-hamburg.zip) | [`testakte-strafrecht-jugendlicher-raub-schulhof-hamburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-jugendlicher-raub-schulhof-hamburg-einzelpdfs.zip) |
| [Korruptionsverdacht in der Vergabestelle München](../../testakten/strafrecht-korruption-bauamt-vergabestelle-muenchen/README.md) | [Gesamt-PDF](../../testakten/strafrecht-korruption-bauamt-vergabestelle-muenchen/gesamt-pdf/strafrecht-korruption-bauamt-vergabestelle-muenchen_gesamt.pdf) | [`testakte-strafrecht-korruption-bauamt-vergabestelle-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-korruption-bauamt-vergabestelle-muenchen.zip) | [`testakte-strafrecht-korruption-bauamt-vergabestelle-muenchen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-korruption-bauamt-vergabestelle-muenchen-einzelpdfs.zip) |
| [Aussage-gegen-Aussage-Verfahren Mainz](../../testakten/strafrecht-sexualdelikt-aussage-gegen-aussage-mainz/README.md) | [Gesamt-PDF](../../testakten/strafrecht-sexualdelikt-aussage-gegen-aussage-mainz/gesamt-pdf/strafrecht-sexualdelikt-aussage-gegen-aussage-mainz_gesamt.pdf) | [`testakte-strafrecht-sexualdelikt-aussage-gegen-aussage-mainz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-sexualdelikt-aussage-gegen-aussage-mainz.zip) | [`testakte-strafrecht-sexualdelikt-aussage-gegen-aussage-mainz-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-sexualdelikt-aussage-gegen-aussage-mainz-einzelpdfs.zip) |
| [Digitales Stalking und Kontaktverbot Hannover](../../testakten/strafrecht-stalking-digitales-kontaktverbot-hannover/README.md) | [Gesamt-PDF](../../testakten/strafrecht-stalking-digitales-kontaktverbot-hannover/gesamt-pdf/strafrecht-stalking-digitales-kontaktverbot-hannover_gesamt.pdf) | [`testakte-strafrecht-stalking-digitales-kontaktverbot-hannover.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-stalking-digitales-kontaktverbot-hannover.zip) | [`testakte-strafrecht-stalking-digitales-kontaktverbot-hannover-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-stalking-digitales-kontaktverbot-hannover-einzelpdfs.zip) |
| [Vereinskasse, Sponsoring und Untreue Kassel](../../testakten/strafrecht-untreue-vereinskasse-kassel/README.md) | [Gesamt-PDF](../../testakten/strafrecht-untreue-vereinskasse-kassel/gesamt-pdf/strafrecht-untreue-vereinskasse-kassel_gesamt.pdf) | [`testakte-strafrecht-untreue-vereinskasse-kassel.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-untreue-vereinskasse-kassel.zip) | [`testakte-strafrecht-untreue-vereinskasse-kassel-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-untreue-vereinskasse-kassel-einzelpdfs.zip) |
| [Arbeitsunfähigkeitsbescheinigung im Pflegedienst Bremen](../../testakten/strafrecht-urkundenfaelschung-au-pflegedienst-bremen/README.md) | [Gesamt-PDF](../../testakten/strafrecht-urkundenfaelschung-au-pflegedienst-bremen/gesamt-pdf/strafrecht-urkundenfaelschung-au-pflegedienst-bremen_gesamt.pdf) | [`testakte-strafrecht-urkundenfaelschung-au-pflegedienst-bremen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafrecht-urkundenfaelschung-au-pflegedienst-bremen.zip) | [`testakte-strafrecht-urkundenfaelschung-au-pflegedienst-bremen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-urkundenfaelschung-au-pflegedienst-bremen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

## Die lokale Übungsakte

Für den ersten Durchgang öffnen Sie im Arbeits-ZIP `Grundakte/00_Posteingang`. Die vollständige Akte enthält auch die späteren Verfahrensstücke. [Fallordner im Druckpaket nachschlagen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/docs/grundakten-lebenswelt/README.md#weitere-arbeitsakten-und-eigenständige-pluginfassungen).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fall | Originalunterlagen und Eingangspost | Lesefassungen |
| --- | --- | --- |
| Testakte StA Musterstadt 7 Js 4412/26 — Ermittlungsverfahren wegen Ladendiebstahls | [Arbeits-ZIP mit Eingangspost](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-lebenswelt-v1.0.0/lebensakte-gericht-staatsanwaltschaft-praxis-einstieg.zip) | [Druckpaket 18](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-lebenswelt-v1.0.0/lesepaket-18.zip) |

Wenn du das hier öffnest, willst du einen staatsanwaltschaftlichen Vorgang führen: Anfangsverdacht, Ermittlungsverfügung, Zwangsmittel, Beweiswürdigung, Abschlussverfügung, Anklage, Strafbefehlsantrag oder Einstellung.
> **Strafverfolgung und Justiz getrennt prüfen:** Artikel 6 Absatz 2 mit den konkreten Tatbeständen des Anhangs III Nummern 6 und 8 Buchstabe a anwenden; nicht jede technische Funktion ist erfasst. Artikel 6 Absatz 3 gilt nur im Anhang-III-Pfad: kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte, einschließlich keiner wesentlichen Beeinflussung des Entscheidungsergebnisses, und mindestens eine Fallgruppe nach Buchstaben a bis d belegen. Profiling natürlicher Personen schließt die Ausnahme aus. Anbieter dokumentieren nach Absatz 4 und registrieren nach Artikel 49 Absatz 2; menschliche Schlusskontrolle oder die Bezeichnung „vorbereitend“ allein genügen nicht. Artikel 113 Buchstabe c erfasst Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5: bei Anhang III ab 02.12.2027, bei Anhang I ab 02.08.2028. Artikel 111 und die Zeitverschränkung mit anderen Abschnitten gesondert prüfen; keine pauschale Verschiebung sämtlicher Pflichten. Für Strafverfolgungsdaten das einschlägige Datenschutzregime prüfen; Artikel 22 DSGVO ist keine pauschale Rechtsgrundlage für jede staatsanwaltschaftliche Verarbeitung. Entscheidungen bleiben bei den zuständigen Amtsträgern. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
Praxisplugin für neue Staatsanwälte und Sitzungsdienst: Ermittlungsverfahren, Polizei, RiStBV, Vermerke, Beschlagnahme, digitale Beweise, Anklage, Strafbefehl, Hauptverhandlung, Plädoyer, Rechtsmittel und gerichtliche Bußgeldverfahren nach OWiG.

## Worum es geht

Dieses Plugin ist ein experimentelles Arbeits- und Lernwerkzeug. Es soll keine echten Amts-, Mandats-, Steuer-, Prüfungs- oder Berufsgeheimnisse aufnehmen, solange die technische und rechtliche Umgebung dafür nicht ausdrücklich freigegeben ist. Es arbeitet am besten mit anonymisierten, abstrahierten oder synthetischen Fällen und mit Dokumenten, die vor der Nutzung datenschutz- und geheimnisschutzrechtlich geprüft wurden.

## Arbeitsweise

Der Allgemein-Skill startet kurz, sortiert Rolle, Verfahrensstand, Frist, Unterlagen und gewünschtes Arbeitsprodukt und routet dann in die passenden Spezial-Skills. Jeder Skill verlangt Quellenhygiene: Normen, Behördenhinweise, Formulare und Rechtsprechung werden vor tragenden Aussagen live aus amtlichen oder frei zugänglichen Quellen geprüft; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Typische Outputs

- Kurzvermerk und Risikoampel
- Checkliste für den nächsten Arbeitstag
- Fragenliste an Behörde, Gericht, Kammer, Mandant, Partei oder Zeugen
- Entwurf für Verfügung, Vermerk, Schriftsatz, Antrag, E-Mail oder Gesprächsleitfaden
- Red-Team-Check gegen Fristenfehler, Zuständigkeitsfehler und Scheingenauigkeit

## OWiG- und Bußgeldspur

Für Ordnungswidrigkeiten arbeitet das Plugin bewusst mit anderer Sprache: kein Anklagesatz, kein Strafbefehl, sondern Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage über die Staatsanwaltschaft, gerichtliches Bußgeldverfahren, Beschlussverfahren, Hauptverhandlung und Rechtsbeschwerde. Die neuen `owi-*`-Skills helfen insbesondere bei Datenschutzbußgeldern, Verkehrs-OWi, Unternehmensgeldbußen, Aufsichtspflichtverletzungen, Umwelt-/Arbeitsschutz-/Produktsicherheits-OWi und der Frage, wann die Staatsanwaltschaft am Termin nach Paragraf 75 OWiG teilnehmen sollte.

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI in der Strafverfolgung. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Strafverfolgung:** Die einzelnen Zweckbestimmungen und Einschränkungen des Anhangs III Nummer 6 prüfen. Ein allgemeiner Einsatz „zur Aufklärung“ reicht als Begründung nicht. Verbot nach Artikel 5 vorrangig und anschließend die Ausnahme nach Artikel 6 Absatz 3 einschließlich Profiling-Sperre prüfen. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehörde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsätzlich **Hochrisiko-KI**.
- **Ausnahme nach Artikel 6 Absatz 3:** Artikel 6 Absatz 3 gilt nur im Anhang-III-Pfad: kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte, einschließlich keiner wesentlichen Beeinflussung des Entscheidungsergebnisses, und mindestens eine Fallgruppe nach Buchstaben a bis d belegen. Profiling natürlicher Personen schließt die Ausnahme aus. Anbieter dokumentieren nach Absatz 4 und registrieren nach Artikel 49 Absatz 2; menschliche Schlusskontrolle oder die Bezeichnung „vorbereitend“ allein genügen nicht. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **Registrierung und Rollen:** Artikel 6 Absatz 4 und Artikel 49 Absatz 2 richten die Dokumentations- und Registrierungspflicht bei der Ausnahme an Anbieter beziehungsweise gegebenenfalls deren Bevollmächtigte. Öffentliche Betreiber prüfen daneben Artikel 49 Absatz 3. Registrierung in der vorgesehenen Datenbank und Notifizierung einer Konformitätsbewertungsstelle sind unterschiedliche Vorgänge. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- Entscheidungsvorschläge und automatisierte Würdigung anhand des konkreten vorgesehenen Einsatzes, der genannten Anhangstatbestände und der Ausnahmevoraussetzungen beurteilen. Nicht allein aus der Bezeichnung „Subsumtion“ auf Hochrisiko schließen; umgekehrt genügt menschliche Schlusskontrolle allein nicht, um die Einstufung auszuschließen.

### Verantwortliche Verfahrensentscheidung

Das Plugin erstellt Entwürfe, keine eigenständigen Anklage-, Einstellungs- oder Haftentscheidungen. Der zuständige Staatsanwalt prüft, gewichtet und entscheidet selbst. Für Strafverfolgungsdaten ist das einschlägige Datenschutzregime zu bestimmen; Artikel 22 DSGVO ist dafür kein pauschaler Ersatz. Ein vollständiger Entwurf bleibt bis zur verantwortlichen Prüfung und Freigabe ein Entwurf.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und das Amtsverschwiegenheitsgebot sind strikt zu wahren.
- Akteninhalte dürfen nicht ungeprüft an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewährleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behördlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Sämtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Staatsanwalt vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde.
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die staatsanwaltschaftliche Bearbeitung wird dokumentiert.
- Aufbewahrungsfristen nach Aktenordnung und KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Staatsanwaltschaften werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis führen, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Installation

ZIP aus dem aktuellen Release laden und über die Plugin-Verwaltung installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **146 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/juristischer-argumentationskern/SKILL.md) |
| 2. Tatvorwurf und materielles Recht | [`tatvorwurf-und-materielles-recht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/tatvorwurf-und-materielles-recht-bearbeiten/SKILL.md) |
| 3. Ermittlungsverfahren und Eingriffe | [`ermittlungsverfahren-und-eingriffe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/ermittlungsverfahren-und-eingriffe-bearbeiten/SKILL.md) |
| 4. Beweis und Aktenanalyse | [`beweis-und-aktenanalyse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/beweis-und-aktenanalyse-bearbeiten/SKILL.md) |
| 5. Anklage und Hauptverhandlung | [`anklage-und-hauptverhandlung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/anklage-und-hauptverhandlung-bearbeiten/SKILL.md) |
| 6. Entscheidung und Rechtsmittel | [`entscheidung-und-rechtsmittel-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/entscheidung-und-rechtsmittel-bearbeiten/SKILL.md) |
| 7. Sanktion und Vollstreckung | [`sanktion-und-vollstreckung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/sanktion-und-vollstreckung-bearbeiten/SKILL.md) |
| 8. Geschädigte und besondere Rollen | [`geschaedigte-und-besondere-rollen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/geschaedigte-und-besondere-rollen-bearbeiten/SKILL.md) |
| 9. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 10. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anklage-und-hauptverhandlung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/anklage-und-hauptverhandlung-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Anklage und Hauptverhandlung: Anklage, Zwischenverfahren, Einlassung, Beweisantrag, Verhandlung und Verständigung bis zum Schriftsatz vorbereiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/anklage-und-hauptverhandlung-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`beweis-und-aktenanalyse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/beweis-und-aktenanalyse-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Beweis und Aktenanalyse: Akteninhalt, Aussage, Sachverständige, digitale Daten und Beweisverwertung mit Widersprüchen und Grenzen auswerten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/beweis-und-aktenanalyse-bearbeiten/SKILL.md) |
| [`entscheidung-und-rechtsmittel-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/entscheidung-und-rechtsmittel-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Entscheidung und Rechtsmittel: Einstellung, Strafbefehl, Urteil, Strafzumessung, Berufung und Revision mit Form und Frist bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/entscheidung-und-rechtsmittel-bearbeiten/SKILL.md) |
| [`ermittlungsverfahren-und-eingriffe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/ermittlungsverfahren-und-eingriffe-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Ermittlungsverfahren und Eingriffe: Beschuldigung, Polizei, Staatsanwaltschaft, Durchsuchung, Beschlagnahme, Haft und Beschuldigtenrechte bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/ermittlungsverfahren-und-eingriffe-bearbeiten/SKILL.md) |
| [`geschaedigte-und-besondere-rollen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/geschaedigte-und-besondere-rollen-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Geschädigte und besondere Rollen: Opferrechte, Nebenklage, Adhäsion, Jugend, Unternehmen und Zeugenbeistand nach der tatsächlichen Rolle bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/geschaedigte-und-besondere-rollen-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/juristischer-argumentationskern/SKILL.md) | Dezernatsvorgang von Akteneingang bis ausformulierter Verfügung führen. Verarbeitet vorhandene Unterlagen, prüft entscheidende Fachfragen und führt den Auftrag zum vollständig formulierten Ergebnis. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/juristischer-argumentationskern/SKILL.md) |
| [`sanktion-und-vollstreckung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/sanktion-und-vollstreckung-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Sanktion und Vollstreckung: Strafe, Bewährung, Maßregel, Einziehung, Vollzug und nachträgliche Entscheidungen getrennt prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/sanktion-und-vollstreckung-bearbeiten/SKILL.md) |
| [`tatvorwurf-und-materielles-recht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/tatvorwurf-und-materielles-recht-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Tatvorwurf und materielles Recht: Tatbestand, Beteiligung, Irrtum, Rechtfertigung, Schuld und Konkurrenz am belegten Geschehen prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/tatvorwurf-und-materielles-recht-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Praktischer Einstieg in die Staatsanwaltschaft: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Unterscheiden Sie bei der Anwendung für staatsanwaltschaftlicher Einstieg technische Aktenorganisation von der Würdigung von Tatsachen und Recht. Prüfen Sie den konkreten Justiz- oder Strafverfolgungsbezug in Anhang III und den tatsächlichen Einfluss auf die Entscheidung; eine formale Schlusszeichnung allein genügt nicht als Gegenbeleg.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
