# Arbeitsrecht-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Arbeitsrechtliche Workflows für Kündigung, Befristung, Urlaub, AGG, Aufhebungsvertrag, Betriebsrat, Arbeitszeit, Lohn und Expansion. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle verwendet.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`arbeitsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/arbeitsrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/arbeitsrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/arbeitsrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/arbeitsrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitsrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/arbeitsrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Arbeitsrecht-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Antrag, Sachverhalt, Beweisplan und nächste Frist. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/arbeitsrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`arbeitsrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/arbeitsrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`arbeitsrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/arbeitsrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [15 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [1. Bewerbung im Berliner Kundenservice](../testakten/agg-bewerbung-sprachanforderung-berlin/README.md) | [Gesamt-PDF](../testakten/agg-bewerbung-sprachanforderung-berlin/gesamt-pdf/agg-bewerbung-sprachanforderung-berlin_gesamt.pdf) | [`testakte-agg-bewerbung-sprachanforderung-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-agg-bewerbung-sprachanforderung-berlin.zip) | [`testakte-agg-bewerbung-sprachanforderung-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-agg-bewerbung-sprachanforderung-berlin-einzelpdfs.zip) |
| [Asset Deal und Personalbestand in Berlin: 50 Arbeitsverträge](../testakten/arbeitsrecht-asset-deal-50-vertraege-berlin/README.md) | [Gesamt-PDF](../testakten/arbeitsrecht-asset-deal-50-vertraege-berlin/gesamt-pdf/arbeitsrecht-asset-deal-50-vertraege-berlin_gesamt.pdf) | [`testakte-arbeitsrecht-asset-deal-50-vertraege-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-arbeitsrecht-asset-deal-50-vertraege-berlin.zip) | [`testakte-arbeitsrecht-asset-deal-50-vertraege-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-arbeitsrecht-asset-deal-50-vertraege-berlin-einzelpdfs.zip) |
| [1. Ottilie Riemenschneider und die Versanddisposition in Leipzig](../testakten/arbeitsrecht-kuendigung-betriebsbedingt-leipzig/README.md) | [Gesamt-PDF](../testakten/arbeitsrecht-kuendigung-betriebsbedingt-leipzig/gesamt-pdf/arbeitsrecht-kuendigung-betriebsbedingt-leipzig_gesamt.pdf) | [`testakte-arbeitsrecht-kuendigung-betriebsbedingt-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-arbeitsrecht-kuendigung-betriebsbedingt-leipzig.zip) | [`testakte-arbeitsrecht-kuendigung-betriebsbedingt-leipzig-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/arbeitsrecht-kuendigungsschutzklagewerkstatt-v1.0.0/testakte-arbeitsrecht-kuendigung-betriebsbedingt-leipzig-einzelpdfs.zip) |
| [1. Adelheid Merz und die Poststelle in Augsburg](../testakten/arbeitsrecht-kuendigung-schwangerschaft-augsburg/README.md) | [Gesamt-PDF](../testakten/arbeitsrecht-kuendigung-schwangerschaft-augsburg/gesamt-pdf/arbeitsrecht-kuendigung-schwangerschaft-augsburg_gesamt.pdf) | [`testakte-arbeitsrecht-kuendigung-schwangerschaft-augsburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-arbeitsrecht-kuendigung-schwangerschaft-augsburg.zip) | [`testakte-arbeitsrecht-kuendigung-schwangerschaft-augsburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/arbeitsrecht-kuendigungsschutzklagewerkstatt-v1.0.0/testakte-arbeitsrecht-kuendigung-schwangerschaft-augsburg-einzelpdfs.zip) |
| [1. Muster ./. Seewerk – vorlagengetreue Konzeptfassung](../testakten/arbeitsrecht-muster-seewerk-konzept-radolfzell/README.md) | [Gesamt-PDF](../testakten/arbeitsrecht-muster-seewerk-konzept-radolfzell/gesamt-pdf/arbeitsrecht-muster-seewerk-konzept-radolfzell_gesamt.pdf) | [`testakte-arbeitsrecht-muster-seewerk-konzept-radolfzell.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-arbeitsrecht-muster-seewerk-konzept-radolfzell.zip) | [`testakte-arbeitsrecht-muster-seewerk-konzept-radolfzell-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/arbeitsrecht-kuendigungsschutzklagewerkstatt-v1.1.0/testakte-arbeitsrecht-muster-seewerk-konzept-radolfzell-einzelpdfs.zip) |
| [1. Muster ./. Seewerk – ausführliche Lebensakte](../testakten/arbeitsrecht-muster-seewerk-lebensakte-radolfzell/README.md) | [Gesamt-PDF](../testakten/arbeitsrecht-muster-seewerk-lebensakte-radolfzell/gesamt-pdf/arbeitsrecht-muster-seewerk-lebensakte-radolfzell_gesamt.pdf) | [`testakte-arbeitsrecht-muster-seewerk-lebensakte-radolfzell.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-arbeitsrecht-muster-seewerk-lebensakte-radolfzell.zip) | [`testakte-arbeitsrecht-muster-seewerk-lebensakte-radolfzell-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/arbeitsrecht-kuendigungsschutzklagewerkstatt-v1.1.0/testakte-arbeitsrecht-muster-seewerk-lebensakte-radolfzell-einzelpdfs.zip) |
| [1. Fridolin Karg und das fehlende Messgerät in Bonn](../testakten/arbeitsrecht-verdachtskuendigung-bonn/README.md) | [Gesamt-PDF](../testakten/arbeitsrecht-verdachtskuendigung-bonn/gesamt-pdf/arbeitsrecht-verdachtskuendigung-bonn_gesamt.pdf) | [`testakte-arbeitsrecht-verdachtskuendigung-bonn.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-arbeitsrecht-verdachtskuendigung-bonn.zip) | [`testakte-arbeitsrecht-verdachtskuendigung-bonn-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/arbeitsrecht-kuendigungsschutzklagewerkstatt-v1.0.0/testakte-arbeitsrecht-verdachtskuendigung-bonn-einzelpdfs.zip) |
| [Befristungskontrollklage Vogt ./. Stadtwerke Neukölln GmbH](../testakten/befristungskontrollklage-vogt-stadtwerke/README.md) | [Gesamt-PDF](../testakten/befristungskontrollklage-vogt-stadtwerke/gesamt-pdf/befristungskontrollklage-vogt-stadtwerke_gesamt.pdf) | [`testakte-befristungskontrollklage-vogt-stadtwerke.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-befristungskontrollklage-vogt-stadtwerke.zip) | [`testakte-befristungskontrollklage-vogt-stadtwerke-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-befristungskontrollklage-vogt-stadtwerke-einzelpdfs.zip) |
| [Akte Waldkrone HealthTech GmbH - NDA, Meldekanal und Lieferantenhinweis](../testakten/hinweisgeberschutz-nda-meldekanal-waldkrone/README.md) | [Gesamt-PDF](../testakten/hinweisgeberschutz-nda-meldekanal-waldkrone/gesamt-pdf/hinweisgeberschutz-nda-meldekanal-waldkrone_gesamt.pdf) | [`testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip) | [`testakte-hinweisgeberschutz-nda-meldekanal-waldkrone-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-hinweisgeberschutz-nda-meldekanal-waldkrone-einzelpdfs.zip) |
| [Vertriebsbonus und staatsanwaltschaftlicher Honeypot](../testakten/internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot/README.md) | [Gesamt-PDF](../testakten/internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot/gesamt-pdf/internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot_gesamt.pdf) | [`testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot.zip) | [`testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot-einzelpdfs.zip) |
| [Kündigungsschutzklage Weber ./. TechLogix GmbH](../testakten/kuendigungsschutzklage-weber-techlogix/README.md) | [Gesamt-PDF](../testakten/kuendigungsschutzklage-weber-techlogix/gesamt-pdf/kuendigungsschutzklage-weber-techlogix_gesamt.pdf) | [`testakte-kuendigungsschutzklage-weber-techlogix.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-kuendigungsschutzklage-weber-techlogix.zip) | [`testakte-kuendigungsschutzklage-weber-techlogix-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-kuendigungsschutzklage-weber-techlogix-einzelpdfs.zip) |
| [Akte Lahnwerke Maschinenbau AG - Slack, AirTags und IT-Sicherheitslage](../testakten/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit/README.md) | [Gesamt-PDF](../testakten/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit/gesamt-pdf/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit_gesamt.pdf) | [`testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit.zip) | [`testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit-einzelpdfs.zip) |
| [Rentenberaterakte Betriebsrentenberatung Pflegedienst Halle](../testakten/rentenberater-bav-firmenberatung-pflegedienst-halle/README.md) | [Gesamt-PDF](../testakten/rentenberater-bav-firmenberatung-pflegedienst-halle/gesamt-pdf/rentenberater-bav-firmenberatung-pflegedienst-halle_gesamt.pdf) | [`testakte-rentenberater-bav-firmenberatung-pflegedienst-halle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-rentenberater-bav-firmenberatung-pflegedienst-halle.zip) | [`testakte-rentenberater-bav-firmenberatung-pflegedienst-halle-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-rentenberater-bav-firmenberatung-pflegedienst-halle-einzelpdfs.zip) |
| [Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/README.md) | [Gesamt-PDF](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-robotikrecht-roboterflotte-vellbruck-muenchen-einzelpdfs.zip) |
| [Klingenhain Musikschule / DRV-Statusprüfung](../testakten/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain/README.md) | [Gesamt-PDF](../testakten/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain/gesamt-pdf/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain_gesamt.pdf) | [`testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip) | [`testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Bearbeite den konkreten arbeitsrechtlichen Auftrag: Kündigung, Vergütung, Vertrag oder Personalmaßnahme. Bei einer Kündigung sind Form, Zugang und Klagefrist besonders dringlich; nicht jeder Auftrag verlangt eine Kündigungsschutzprüfung.
Arbeitsrechtliche Abläufe für Personalabteilungen und Arbeitsrechtler: Einstellungsprüfung, Kündigungsprüfung, Richtlinienerstellung, Personalhandbuch-Updates, Lohn-und-Arbeitszeitfragen sowie Statusfeststellung – auf das deutsche Arbeitsrecht (KSchG, BetrVG, BGB, AGG, ArbZG, MiLoG, MuSchG, BEEG, TzBfG, BUrlG, EFZG, SGB IV) zugeschnitten.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – mit belegten Zitaten und gesonderten Prüfhinweisen. Ein Entwurfshinweis garantiert keinen technischen Schutz vor Weitergabe. Das Plugin erledigt die Recherchearbeit: Es liest Dokumente, wendet Ihre Prüfschemata an, benennt Risiken und erstellt Entwürfe. Die rechtliche Beurteilung und die Entscheidung liegen beim Rechtsanwalt oder Syndikusrechtsanwalt.** Zitate werden nach ihrer Quelle gekennzeichnet, damit klar ist, welche überprüft werden müssen. Vertraulichkeitsvermerke werden zurückhaltend gesetzt. Folgenreiche Handlungen – Einreichen, Versenden, Vollziehen – erfordern ausdrückliche Freigabe.

## Für wen ist das Plugin

| Rolle | Primäre Abläufe |
|---|---|
| **Arbeitsrechtlicher Berater / Fachanwalt Arbeitsrecht** | Kündigungsprüfung, Statusfeststellung, Interne Untersuchung, KSchG-Klage, Aufhebungsvertrag |
| **Syndikusrechtsanwalt (in-house)** | Einstellungsprüfung, Personalrichtlinien, Betriebsratsanhörung, Lohn-und-Arbeitszeitfragen |
| **HR Business Partner / Personalleiter** | Einstellungsprüfung, Handbuch-Updates, Urlaub-/Fehlzeiten-Tracker, Abmahnungsentwürfe |
| **GC / Leiter Rechtsabteilung** | Eskalationsempfänger bei hochriskanten Kündigungen, Massenentlassungen, Einigungsstellenverfahren |

## Ersteinrichtung: Kaltstart

Die Einrichtung eines Kanzlei- oder Unternehmensprofils ist optional und setzt einen entsprechenden Auftrag voraus. Für einen konkreten Fall zuerst die vorliegenden Unterlagen auswerten und direkt den bestellten Entwurf bearbeiten; weder ein Personalhandbuch noch drei weitere Kündigungsakten sind dafür zwingend. Nur entscheidende Angaben nachfragen und nach Antworten am bestehenden Ergebnis weiterarbeiten. Speicherung und zusätzliche Unterlagen richten sich nach dem ausdrücklich beauftragten Einrichtungsumfang.

```
/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: kaltstart-interview
```

Die Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` gespeichert und übersteht Plugin-Updates.

## Voraussetzungen

- **Persistenter Datenpfad.** Der Urlaubsregister, die Untersuchungsprotokolle und die Entsendungs-Tracker werden unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/` gespeichert. Diese Dateien enthalten privilegierte und personenbezogene Daten – vergewissern Sie sich, dass das Verzeichnis gesichert und zugriffsgeschützt ist (§ 26 BDSG, Art. 5 Abs. 1 lit. f DSGVO).
- **Rechtsdatenbank-Zugang.** Die Skills speichern keine konkreten Rechtsnorminhalte (Schwellenwerte, Fristenberechnungen, länderspezifische Regelungen). Alle jurisdiktionsspezifischen Regeln werden zum Zeitpunkt der Prüfung recherchiert und zitiert. Stellen Sie sicher, dass die Sitzung Zugang zu den genutzten Recherchewerkzeugen hat.
- **Faktizitäts-Gate.** Für aktuelle BAG-/BSG-Linien, Statusfeststellung, Urlaub, AGG/Equal Pay, Freistellung und Lohn/SV zuerst `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: rechtsstand-mai-2026-faktenbank` laden. Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen; Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freier Quelle.
- **Außenanwalt bei Fachfragen.** Für neue Jurisdiktionen, komplexe Statusfeststellungen oder hochriskante Maßnahmen wird externer Sachverstand empfohlen.
- **Mandatsgeheimnis.** § 43a Abs. 2 BRAO, § 203 StGB und § 53 StPO gelten für alle Ausgaben dieses Plugins. Keine Weitergabe vertraulicher Mandantendaten ohne ausdrückliche Freigabe.

## Skills

| Skill | Funktion |
|---|---|
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: kaltstart-interview` | Ersteinrichtung – Standortprofil, Eskalationsregeln, Handbuchwissen |
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: rechtsstand-mai-2026-faktenbank` | Quellen-Gate: verifizierte BAG-/BSG-Anker zu Mindesturlaub, Equal Pay, Freistellung und Statusfeststellung; sperrt Blindzitate |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: einstellungspruefung` | Arbeitsvertragsprüfung: Befristung (TzBfG), AGG, AÜG, Nachweisgesetz |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kuendigungs-pruefung` | Kündigungsprüfung: KSchG, § 102 BetrVG, §§ 622, 626 BGB, Sozialauswahl |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kuendigungsschutzklage` | Entwurf und Prüfung der KSchG-Klage, § 4 KSchG, 3-Wochen-Frist, Klageschrift ArbG |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: abmahnung-arbeitsrecht` | Abmahnungsentwurf und -bewertung nach BAG-Grundsätzen |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: aufhebungsvertrag` | Aufhebungsvertrag inkl. Sperrzeitprüfung § 159 SGB III, Abfindungssteuer § 34 EStG |
| `/arbeitsrecht:betriebsrat-tarif-uebergang-bearbeiten Thema: betriebsrat-anhoerung` | Betriebsratsanhörung § 102 BetrVG – Fristen, Inhalt, Mitteilungspflichten |
| `/arbeitsrecht:entgelt-urlaub-arbeitszeit-bearbeiten Thema: lohn-arbeitszeit-fragen` | Lohn-/Arbeitszeitfragen: ArbZG, MiLoG, EFZG – standortbezogen |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: arbeitnehmer-status` | Statusfeststellung § 7a SGB IV, Scheinselbständigkeit, AÜG |
| `/arbeitsrecht:entgelt-urlaub-arbeitszeit-bearbeiten Thema: lohnsteuer-sozialversicherung` | Statusfeststellung, Scheinselbständigkeit, Clearingverfahren DRV |
| `/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: fehlzeiten-register` | Urlaubsregister und Fehlzeitentracker: BUrlG, EFZG, MuSchG, BEEG |
| `/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: fehlzeit-erfassen` | Neue Fehlzeit / neuen Urlaub im Register anlegen |
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: expansion-auftakt [Land]` | Entsendungs-/Expansionsprojekt eröffnen: AÜG, A1, EU-Entsende-RL, ÄntG |
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: expansion-aktualisierung [Land]` | Offenes Entsendungsprojekt aktualisieren |
| `/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: untersuchung-eroeffnen` | Interne Untersuchung eröffnen – Intake, Quellenplan, Protokoll anlegen |
| `/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: untersuchung-ergaenzen` | Dokumente / Gesprächsnotizen zu offener Untersuchung hinzufügen |
| `/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: untersuchung-abfrage` | Fragen gegen Untersuchungsprotokoll stellen |
| `/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: untersuchungs-memo` | Privilegiertes Untersuchungs-Memo erstellen oder aktualisieren |
| `/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: untersuchungs-zusammenfassung` | Zielgruppenspezifische Zusammenfassung (HR, Geschäftsführung, Außenanwalt) |
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: handbuch-aktualisierung` | Personalrichtlinien diff und Betriebsvereinbarungsauswirkungen prüfen |
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: richtlinien-entwurf [Thema]` | BetrVG-konforme Richtlinie entwerfen, BR-Anhörung planen |
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: mandat-arbeitsbereich` | Mandatsakte verwalten (multi-mandant): neu, auflisten, wechseln, schließen, keine |
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: arbeitsrecht-anpassen` | Kanzlei-/Unternehmensprofil gezielt anpassen |

### Aktuelle verifizierte Rechtsprechung 2025/2026

Gezielter Nachcheck am 16.10.2026: [BAG, Urteil vom 07.05.2026, 2 AZR 184/25](https://www.bundesarbeitsgericht.de/entscheidung/2-azr-184-25/), Rn. 24 bis 31 und 33 bis 34, gelesen. Die Bestätigung am Scanner vor Einwurf begründet im entschiedenen Zustellablauf keinen Anscheinsbeweis; andere Beweismittel bleiben möglich. Der Fall betraf den Zugang einer bEM-Einladung. Ein unterbliebenes bEM macht eine Kündigung nicht automatisch unwirksam, verschärft aber die Darlegungslast zu milderen Mitteln. Keine pauschale Aussage über alle Einwurf-Einschreiben und keine Vollaktualisierung der übrigen Rechtsprechung.

| Skill | Funktion |
|---|---|
| `/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: rechtsstand-mai-2026-faktenbank` | Zentrale Faktenbank: BAG 03.06.2025, 9 AZR 104/24 (Mindesturlaub/kein Verzicht im bestehenden Arbeitsverhältnis); BAG 23.10.2025, 8 AZR 300/24 (Equal Pay/Paarvergleich); BAG 25.03.2026, 5 AZR 108/25 (Freistellungsklausel/Dienstwagen); BSG 05.11.2024, B 12 BA 3/23 R und BSG 12.06.2024, B 12 BA 2/22 R (Statusfeststellung). |

## Interaktive Skills vs. geplante Agenten

Die obigen Skills werden auf Abruf ausgeführt. Der folgende Agent läuft nach Zeitplan:

| Agent | Überwacht | Standard-Rhythmus |
|---|---|---|
| **urlaub-fehlzeiten** | Offene Abwesenheiten mit gesetzlichen Fristen – BUrlG, EFZG, MuSchG, BEEG; Fristen- und Entscheidungshinweise vor Ablauf | Wöchentlich (montags) |

## Anwendungsbeispiele für die deutsche Kanzlei

**Szenario 1 – Ordentliche Kündigung mit Sozialauswahl:**
```
/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kuendigungs-pruefung
Mandant plant betriebsbedingte Kündigung von 3 von 12 Arbeitnehmern.
Betrieb hat 15 AN, kein BR. Bitte Sozialauswahl prüfen und § 1 KSchG
Interessenabwägung durchführen.
```

**Szenario 2 – Befristeter Arbeitsvertrag:**
```
/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: einstellungspruefung
Neuer Mitarbeiter, Befristung ohne Sachgrund auf 2 Jahre nach § 14 Abs. 2
TzBfG. Vorherige Beschäftigung beim selben Arbeitgeber vor 5 Jahren.
Bitte Vorbeschäftigungsverbot prüfen.
```

**Szenario 3 – Abmahnung wegen unentschuldigten Fehlens:**
```
/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: abmahnung-arbeitsrecht
Mitarbeiter war an 3 Tagen ohne Krankmeldung nicht erschienen. Erste
Abmahnung. Bitte BAG-konforme Abmahnung entwerfen.
```

**Szenario 4 – Interne Untersuchung / Compliance:**
```
/arbeitsrecht:beschaeftigtenschutz-untersuchung-bearbeiten Thema: untersuchung-eroeffnen
Verdacht auf Unterschlagung durch Teamleiter in der Buchhaltung. Hinweis
durch anonyme Meldestelle. Bitte Untersuchungsprotokoll anlegen und
Quellenplan § 26 BDSG-konform erstellen.
```

**Szenario 5 – Entsendung nach Frankreich:**
```
/arbeitsrecht:mandatsakte-quellen-kommunikation-bearbeiten Thema: expansion-auftakt Frankreich
Mitarbeiter soll für 18 Monate nach Paris entsendet werden. Bitte A1-
Bescheinigung, AEntG-Anforderungen und Entsendevertrag-Checkliste.
```

## Neue Workflows v3.3.1

### Bündel 1: Kündigungsschutzklage Selbsthilfe-Workflow (KüSchK)

Vollständiger Workflow für Verbraucher und Anwälte zur eigenständigen Einreichung und Verteidigung einer Kündigungsschutzklage — von der Triage über die Klageschrift bis zur Vergleichsverhandlung.

| Skill | Funktion |
|---|---|
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-triage-laie-oder-anwalt` | KERNEINSTIEG: Anwalt oder Laie; Weichenstellung für den gesamten Workflow |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-grundwarnung-falsche-wiese-und-haftung` | Pflichtkopf für alle Laien-Schriftsätze: Haftungsausschluss, Dreiwochenfrist |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-anwendbarkeit-kschg-pruefen` | § 1 Abs. 1 KSchG Wartezeit; § 23 KSchG Betriebsgröße; Teilzeit-Berechnung |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-kuendigungsgrund-personen-verhalten-betrieb` | Drei Kündigungsgründe § 1 Abs. 2 KSchG; Sonderkündigungsschutz-Querverweis |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-sonderkuendigungsschutz-checkliste` | Schwangerschaft, Elternzeit, Schwerbehinderung, BR-Mitglied, Datenschutzbeauftragter |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-formfehler-pruefen` | § 623 BGB, § 174 BGB Vollmachtsrüge, § 102 BetrVG, §§ 17/18 KSchG |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-frist-und-zugang-pruefen` | § 4 KSchG Dreiwochenfrist; § 5 KSchG nachträgliche Zulassung; Zugangsbeweis |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-klageschrift-laie-baustein` | Ausfüllbare Klageschrift Schritt für Schritt für Laien |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-klageschrift-anwalt-baustein` | Anwaltliche Klageschrift mit Hilfsanträgen und Anlagen-Checkliste |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-allgemeiner-und-besonderer-feststellungsantrag` | Punktueller Antrag § 4 KSchG vs. Schleppnetz § 256 ZPO |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-weiterbeschaeftigungsantrag-grosser-senat` | BAG GS 1985; Voraussetzungen; Vor- und Nachteile |
| `/arbeitsrecht:entgelt-urlaub-arbeitszeit-bearbeiten Thema: kueschk-annahmeverzug-loehne-anrechnung-zwischenverdienst` | § 615 BGB; § 11 KSchG Anrechnung; böswilliges Unterlassen |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-erwiderung-arbeitgeber-strategien-typisch` | Typische Arbeitgeberstrategien; Stricken-Anwälte; Hinhaltetaktik |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-replik-arbeitnehmer-baustein` | Replik auf Klageerwiderung; Substantiierungstiefe; Beweismittel |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-guetetermin-strategie-und-sprechzettel` | § 54 ArbGG Gütetermin; Sprechzettel; was sagen / nicht sagen |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-kammertermin-sprechzettel` | Kammertermin Hauptverhandlung; Antragsstellung; Reaktionsmuster |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-muendliche-verhandlung-praxistipps-laie` | Auftreten, Kleidung, Anrede, Sitzungsverlauf für Laien |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-vergleichsverhandlung-checkliste` | Alle Vergleichsbausteine: Abfindung, Zeugnis, Freistellung, Erledigung |
| `/arbeitsrecht:kuendigung-zugang-trennung-bearbeiten Thema: kueschk-abfindung-faustformel-und-spannweite` | Faustformel; Spannweite; § 34 EStG Fünftel-Regelung |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-stricken-anwalt-risiko-und-vergleichsdruck` | KERNWARNUNG: Stricken-Strategie; Rückkehrpflicht; § 12 KSchG; § 9 KSchG |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-aufloesungsantrag-arbeitnehmer-9-kschg` | Auflösungsantrag § 9 KSchG bei Unzumutbarkeit; Abfindung § 10 KSchG |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-paragraph-12-kschg-neuer-job-einseitig` | § 12 KSchG einseitige Lösung; Wochenfrist; Abgrenzung § 9 KSchG |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-zeugnisanspruch-und-vergleich` | § 109 GewO; BAG-Mindeststandard; geheime Negativsignale; Vergleichsformulierungen |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-streitwert-kostenfolge-prozesskostenhilfe` | § 42 GKG; § 12a ArbGG keine Kostenerstattung erste Instanz; PKH |
| `/arbeitsrecht:arbeitsgericht-prozess-vergleich-bearbeiten Thema: kueschk-berufung-und-revision-lag-bag` | Berufung LAG; Revision BAG; Zulassungsgründe; Fristen |
| `/arbeitsrecht:kueschk-output-warnschriftsatz-laie` | Vollständige Klageschrift mit Pflicht-Disclaimer für Laien |

### Bündel 2: Entfristungsklage / Befristungskontrollklage (TzBfG)

Vollständiger Workflow für die Klage auf Feststellung, dass ein angeblich befristeter Vertrag unbefristet ist — insbesondere bei Schriftformverstößen nach § 14 Abs. 4 TzBfG und digitaler Vertragsunterzeichnung.

| Skill | Funktion |
|---|---|
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-triage-was-will-user` | Einstieg; Erkennung Entfristungsklage; Abgrenzung zu KüSchK |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-laie-oder-anwalt-frage` | Statusabfrage; Laien-Warnungen; Empfehlung anwaltlicher Beratung |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-grundwarnung-drei-wochen-frist` | § 17 TzBfG Dreiwochenfrist ab vereinbartem Ende; Fiktionswirkung § 7 KSchG |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-sachgrund-pruefen-14-abs-1` | Acht Sachgründe § 14 Abs. 1 TzBfG; Prüfungsstruktur; Beweislast |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-sachgrundlos-14-abs-2-vorbeschaeftigung` | § 14 Abs. 2 TzBfG; Vorbeschäftigungsverbot; BVerfG 2018; Karenzzeit |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-sachgrundlos-14-abs-2a-neugruendung` | Neugründungsprivileg vier Jahre § 14 Abs. 2a TzBfG |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-sachgrundlos-14-abs-3-aelter-52` | § 14 Abs. 3 TzBfG; Befristung ab 52; Vorarbeitslosigkeit |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-schriftform-14-abs-4-erkennen` | KERNSKILL: Schriftform § 14 Abs. 4 TzBfG; Papieroriginal oder echte QES; Scan/einfache Signatur genügt nicht |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-elektronische-signatur-vorsicht` | DocuSign, Adobe Sign, Zertifikate, QES-Abgrenzung und Formrisiko |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-rechtsfolge-16-tzbfg-unbefristet` | § 16 Satz 1 TzBfG Vertrag gilt als unbefristet; früheste Kündigung § 16 Satz 2 |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-klageschrift-laie-baustein` | Schritt-für-Schritt Klageschrift Entfristungsklage für Laien |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-klageschrift-anwalt-baustein` | Anwaltliche Klageschrift mit Hilfsanträgen und Weiterbeschäftigungsantrag |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-guetetermin-und-kammertermin-sprechzettel` | Sprechzettel mündliche Verhandlung; Kernargumente Schriftformmangel |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-vergleichsverhandlung-checkliste` | Vergleichsbausteine Entfristungsklage; Beendigungsdatum; Abfindung; Zeugnis |
| `/arbeitsrecht:arbeitsvertrag-status-befristung-bearbeiten Thema: entfristung-output-warnschriftsatz-laie` | Vollständige Klageschrift mit Pflicht-Disclaimer für Laien |

## Lerneffekt

Ihr Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich durch Nutzung. Skills weisen Sie hin, wenn eine Ausgabe auf einem Standardwert beruht, der angepasst werden sollte. Sie können die Einrichtung erneut ausführen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine neue Position zu speichern.

## Hinweise

- **Standortkenntnis ist der Kern.** Das Plugin kennt die Unterschiede zwischen Bundesländern und berücksichtigt betriebliche Besonderheiten (Betriebsgröße, Betriebsrat, Tarifbindung).
- **Kündigungsprüfung ersetzt nicht das Gespräch mit HR und Führungskraft.** Sie ist eine Checkliste, die den vergessenen Punkt findet.
- **Lohn-/Arbeitszeitfragen zitieren die Norm**, kennzeichnen aber Grenzfälle zur menschlichen Prüfung. Einstufungsentscheidungen haben Konsequenzen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **100 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/kaltstart-triage/SKILL.md) |
| 2. Arbeitsvertrag, Status und Befristung | [`arbeitsvertrag-status-befristung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/arbeitsvertrag-status-befristung-bearbeiten/SKILL.md) |
| 3. Entgelt, Urlaub und Arbeitszeit | [`entgelt-urlaub-arbeitszeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/entgelt-urlaub-arbeitszeit-bearbeiten/SKILL.md) |
| 4. Kündigung, Zugang und Aufhebungsvertrag | [`kuendigung-zugang-trennung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/kuendigung-zugang-trennung-bearbeiten/SKILL.md) |
| 5. Betriebsrat und Betriebsübergang | [`betriebsrat-tarif-uebergang-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/betriebsrat-tarif-uebergang-bearbeiten/SKILL.md) |
| 6. Beschäftigtenschutz und interne Untersuchung | [`beschaeftigtenschutz-untersuchung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/beschaeftigtenschutz-untersuchung-bearbeiten/SKILL.md) |
| 7. Arbeitsgericht, Schriftsatz und Vergleich | [`arbeitsgericht-prozess-vergleich-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/arbeitsgericht-prozess-vergleich-bearbeiten/SKILL.md) |
| 8. Mandatsakte, Quellen und Kommunikation | [`mandatsakte-quellen-kommunikation-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/mandatsakte-quellen-kommunikation-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsgericht-prozess-vergleich-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/arbeitsgericht-prozess-vergleich-bearbeiten/SKILL.md) | Arbeitsrechtliche Mandatsbearbeitung: Klagen, Erwiderungen, Termine, Rechtsmittel, Kosten und gerichtliche Vergleiche zu einem vollständigen Prozessprodukt ausarbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/arbeitsgericht-prozess-vergleich-bearbeiten/SKILL.md) |
| [`arbeitsvertrag-status-befristung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/arbeitsvertrag-status-befristung-bearbeiten/SKILL.md) | Arbeitsrechtliche Mandatsbearbeitung: Vertragsinhalt, Beschäftigungsstatus, Befristung und Entfristung anhand von Vereinbarung und tatsächlicher Tätigkeit prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/arbeitsvertrag-status-befristung-bearbeiten/SKILL.md) |
| [`beschaeftigtenschutz-untersuchung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/beschaeftigtenschutz-untersuchung-bearbeiten/SKILL.md) | Arbeitsrechtliche Mandatsbearbeitung: AGG, Hinweisgeberschutz, BEM, Beschäftigtendaten und interne Untersuchungen mit Schutzpflichten und Beweisfragen bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/beschaeftigtenschutz-untersuchung-bearbeiten/SKILL.md) |
| [`betriebsrat-tarif-uebergang-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/betriebsrat-tarif-uebergang-bearbeiten/SKILL.md) | Arbeitsrechtliche Mandatsbearbeitung: Kollektive Beteiligungsrechte, Betriebsratsbeschlüsse, Wahlen und Betriebsübergang im jeweiligen Verfahren prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/betriebsrat-tarif-uebergang-bearbeiten/SKILL.md) |
| [`entgelt-urlaub-arbeitszeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/entgelt-urlaub-arbeitszeit-bearbeiten/SKILL.md) | Arbeitsrechtliche Mandatsbearbeitung: Vergütung, Entgeltgleichheit, Annahmeverzug, Freistellung, Urlaub und Arbeitszeit mit Berechnungen und Anspruchszeiträumen bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/entgelt-urlaub-arbeitszeit-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Arbeitsrecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/kaltstart-triage/SKILL.md) | Für Kaltstart Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Arbeitsrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/kaltstart-triage/SKILL.md) |
| [`kuendigung-zugang-trennung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/kuendigung-zugang-trennung-bearbeiten/SKILL.md) | Arbeitsrechtliche Mandatsbearbeitung: Kündigungsgrund, Schutzvorschriften, Form, Zugang und Trennungsalternativen bis zur Verhandlung prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/kuendigung-zugang-trennung-bearbeiten/SKILL.md) |
| [`mandatsakte-quellen-kommunikation-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/mandatsakte-quellen-kommunikation-bearbeiten/SKILL.md) | Arbeitsrechtliche Mandatsbearbeitung: Mandat, Unterlagen, Zeitablauf, Quellenkontrolle, Risikobewertung und Kommunikation des arbeitsrechtlichen Auftrags steuern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitsrecht/skills/mandatsakte-quellen-kommunikation-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
