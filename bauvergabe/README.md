<!-- decimal-headings -->

# 1. Bauvergabe – vom Leistungsverzeichnis bis zum Nachtrag

[Repository-Start](../README.md) · [Alle Plugins](../README.md#was-ist-drin) · [Testakten](../testakten/README.md)

## 1.1. Fünf Plugins in einer gemeinsamen Reihe

Diese Reihe überträgt den Ablauf der Dienstleistungsvergabe auf Bauleistungen: Bedarf und Planung prüfen, Vergabeunterlagen erstellen, ein Verfahren führen, ein Angebot bearbeiten, Rechtsschutz betreiben und den gewonnenen Bauauftrag einschließlich Nachträgen begleiten. Sie behandelt Hochbau, Klinik- und Apothekengebäude, Produktionshallen, Wohnungsbau sowie Straßen, Tunnel und Schutzeinrichtungen mit ihren jeweiligen technischen Schnittstellen.

Der Ordner `bauvergabe` ist die gemeinsame Übersicht. Installiert werden die fünf darunterliegenden Plugins einzeln oder gemeinsam. Jedes enthält **zehn Fachskills und einen elften Hauptskill**, einen umfangreichen, eigenständig nutzbaren Werkstatt-Prompt und einen Mini-Prompt bis 7.500 UTF-8-Bytes. Zusammen sind es 55 Skills. Die Werkstatt ist zugleich der große Mega-Prompt; daneben entsteht keine inhaltsgleiche dritte Langfassung.

| Plugin und Einstieg | Arbeitsprodukt | Installation |
| --- | --- | --- |
| [Vergabeunterlagen erstellen](bauvergabe-unterlagen/README.md) | Bedarf, Auftragswert, Lose, Baugrund und Planungsreife; Leistungsbeschreibung, Eignung, Zuschlagskriterien und Vertragsentwurf mit Freigabeprüfung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/bauvergabe-unterlagen.zip) |
| [Vergabeverfahren führen](bauvergabe-verfahren/README.md) | Bekanntmachung, Bieterkommunikation, Berichtigung, Öffnung, Nachforderung, Eignung, Wertung, Information und Zuschlag oder Aufhebung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/bauvergabe-verfahren.zip) |
| [Als Bieter teilnehmen](bauvergabe-bieter/README.md) | Teilnahmeentscheidung, LV-Prüfung, Kalkulation, Bietergemeinschaft, Nachunternehmer, Eignungsleihe, Angebot und Vertragsübergabe. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/bauvergabe-bieter.zip) |
| [Bauvergaberechtsschutz](bauvergabe-rechtsschutz/README.md) | Rüge, Fristprüfung, Nachprüfungsantrag, Zuschlagsschutz, Akteneinsicht, Auftraggeberverteidigung, Beiladung und Beschwerde. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/bauvergabe-rechtsschutz.zip) |
| [Nachträge bearbeiten](bauvergabe-nachtragsmanagement/README.md) | Vertragsbaseline, Anordnung, Mehrmengen, zusätzliche Leistungen, Behinderung, Nachweiskosten, Prüfung nach § 132 GWB und Abrechnung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bauvergabe-nachtragsmanagement.zip) |

## 1.2. Ohne Installation mit dem Prompt beginnen

Je Arbeitsstation entweder den ausführlichen Werkstatt-Prompt oder den kompakten Mini-Prompt verwenden. Beide führen durch Rückfragen, Quellenprüfung, Ausarbeitung, Gegenprüfung und den nächsten konkreten Arbeitsschritt. Der jeweilige Hauptskill übernimmt diese Steuerung innerhalb des installierten Plugins.

| Arbeitsstation | Werkstatt / Mega-Prompt | Mini-Prompt |
| --- | --- | --- |
| Unterlagen | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-unterlagen/bauvergabe-unterlagen-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-unterlagen/bauvergabe-unterlagen-werkstatt.txt) | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-unterlagen/bauvergabe-unterlagen-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-unterlagen/bauvergabe-unterlagen-schnellstart.txt) |
| Verfahren | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-verfahren/bauvergabe-verfahren-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-verfahren/bauvergabe-verfahren-werkstatt.txt) | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-verfahren/bauvergabe-verfahren-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-verfahren/bauvergabe-verfahren-schnellstart.txt) |
| Bieter | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-bieter/bauvergabe-bieter-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-bieter/bauvergabe-bieter-werkstatt.txt) | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-bieter/bauvergabe-bieter-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-bieter/bauvergabe-bieter-schnellstart.txt) |
| Rechtsschutz | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-rechtsschutz/bauvergabe-rechtsschutz-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-rechtsschutz/bauvergabe-rechtsschutz-werkstatt.txt) | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-rechtsschutz/bauvergabe-rechtsschutz-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-rechtsschutz/bauvergabe-rechtsschutz-schnellstart.txt) |
| Nachträge | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-nachtragsmanagement/bauvergabe-nachtragsmanagement-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-nachtragsmanagement/bauvergabe-nachtragsmanagement-werkstatt.txt) | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-nachtragsmanagement/bauvergabe-nachtragsmanagement-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bauvergabe/bauvergabe-nachtragsmanagement/bauvergabe-nachtragsmanagement-schnellstart.txt) |

## 1.3. Zwei zusammenhängende Testakten

**Klinikum Lindenbogen Münster:** Ambulanzneubau mit Krankenhausapotheke. Das Rohbaulos läuft vom unvollständigen Planungsstand über eine Bodenberichtigung, Kalkulation und beanstandete Regionalpunkte bis zur erneuten Wertung, zum Zuschlag und zu einer geänderten Gründung.

**16 Wohnungen am Quittenhof in Bielefeld:** Kommunales Wohnungsbauprojekt mit Eignungsleihe für Brandwandarbeiten. Eine fehlende Verpflichtungserklärung, ihre Nachforderung und die Frage einer nachträglich veränderten Bieterkapazität bilden den Streit. Nach dem Zuschlag folgen Brandwandänderung, Aufmaß, Nachtragsangebot und Abrechnung.

Beide Fälle sind fiktiv und enthalten bearbeitbare Word-Dokumente, Brief-PDFs, E-Mails mit tatsächlichen Dateianhängen, Excel-Kalkulationen und CSV-Listen. Die Projektordner bleiben in beiden ZIP-Fassungen erhalten. Ausgangspunkt ist ein prüfbedürftiger Arbeitsstand; fehlende Planfreigaben und Beweise sind Teil der Übung. Die Fall-READMEs erklären den zulässigen Informationsstand jeder Rolle.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Durchgehende Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Klinikum Münster – Aktenführer](../testakten/bauvergabe-klinikum-muenster/README.md) | [PDF](../testakten/bauvergabe-klinikum-muenster/gesamt-pdf/bauvergabe-klinikum-muenster_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.33.1/testakte-bauvergabe-klinikum-muenster.zip) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.33.1/testakte-bauvergabe-klinikum-muenster-einzelpdfs.zip) |
| [Wohnhaus Bielefeld – Aktenführer](../testakten/bauvergabe-wohnhaus-bielefeld/README.md) | [PDF](../testakten/bauvergabe-wohnhaus-bielefeld/gesamt-pdf/bauvergabe-wohnhaus-bielefeld_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.33.1/testakte-bauvergabe-wohnhaus-bielefeld.zip) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.33.1/testakte-bauvergabe-wohnhaus-bielefeld-einzelpdfs.zip) |

## 1.4. So greifen die Stationen ineinander

1. Mit `01-vergabeunterlagen` beginnen. Aus dem Planungsstand eine Lückenliste und eine bearbeitbare Vergabeakte entwickeln; Freigaben nicht erfinden.
2. Für die Vergabestelle `02-vergabeverfahren` hinzunehmen. Jede Berichtigung erhält einen nachvollziehbaren Stand und wird allen betroffenen Bietern gleich zugänglich gemacht.
3. Auf Bieterseite nur veröffentlichte Unterlagen und `03-bieterarbeit` laden. Konkurrenzpreise und interne Vergabevermerke bleiben außerhalb dieses Arbeitskontexts. Das Angebot anhand der veröffentlichten Fassung erstellen.
4. Für die rivalisierende Bieterin `04-rechtsschutz` verwenden. Rügefrist, Nichtabhilfemitteilung, Antrag und Zuschlagsverbot getrennt prüfen. Die spätere Fortgangsnotiz nicht als bereits bekanntes Ergebnis vorwegnehmen.
5. Nach dem Zuschlag mit `05-nachtragsmanagement` weiterarbeiten. Das unterschriebene Angebot und die angenommenen Vertragsunterlagen bilden die Ausgangsbasis. Zivilrechtlicher Mehrvergütungsanspruch und vergaberechtliche Änderungszulässigkeit sind getrennt zu begründen.

Bei jedem Wechsel ein Übergabeblatt mit Rolle, Aktenstand, aktuellen Fristen, offenen Belegen, verbindlichen Entscheidungen und nächsten Arbeitsschritten anlegen. Ein Modell erhält keinen Auftrag, widersprüchliche Interessen gleichzeitig zu vertreten.

## 1.5. Fachlicher Zuschnitt und Quellen

Rechtsstand: **6. Oktober 2026**. Die Reihe berücksichtigt insbesondere § 97a GWB, die aktuelle Verweisung in § 2 VgV auf die VOB/A 2026 und die seit 2026 geltenden Bau-Schwellenwerte. Altfälle werden anhand der Übergangsvorschriften eingeordnet. Die Quellenverzeichnisse der fünf Plugins enthalten konkrete EuGH- und BGH-Entscheidungen mit Fundstelle, Aussage und Grenze ihrer Übertragbarkeit. Ein älteres Urteil wird nicht als Entscheidung aus 2026 ausgegeben.

Die technischen Regeln für Klinik, Apotheke, Industrie, Wohnen und Verkehrsbau werden projektbezogen angefordert. Die Reihe ersetzt weder Fachplanung noch Statik, Baugrunduntersuchung oder einen geprüften GAEB-Export. Eine VOB/B-Vereinbarung und ihre konkrete Fassung sind Vertragsdaten, keine Folge jeder öffentlichen Ausschreibung.

Die Plugins liefern Arbeitsabläufe und Entwürfe. Tatsächliche Veröffentlichung, Angebotsabgabe, Zuschlag, Rechtsbehelf oder Zahlungsfreigabe brauchen einen dafür geeigneten Zugang und eine konkrete, geprüfte Freigabe. Ein Vergabeportal-Connector wird durch die Installation nicht eingerichtet.
