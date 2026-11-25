# Betreuungsrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Betreuungsrechtliche Skills für ehrenamtliche Familienbetreuer, Berufs- und Vereinsbetreuer: Kaltstart, Scan-Akte, Kalender, Gerichtskommunikation, Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Wunschermittlung, Kontoanalyse und Schutzplan nach BtOG und BGB.

Zur Installation laden Sie das Einzel-ZIP herunter. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`betreuungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/betreuungsrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/betreuungsrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/betreuungsrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/betreuungsrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/betreuungsrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/betreuungsrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Betreuungsrecht:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`betreuungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/betreuungsrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`betreuungsrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/betreuungsrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`betreuungsrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/betreuungsrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [4 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält die Plugins der ausgewiesenen Ausgabe. Die Einzelpakete finden Sie im [Download-Index](../ASSET_INDEX.md). Werkstatt und Schnellstart stehen als Markdown bereit.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Hafenpolizei - Dienstunfall, Burnout und Wiedereingliederung](../testakten/beamtenrecht-dienstunfall-burnout-wiedereingliederung-hafenpolizei/README.md) | [Gesamt-PDF](../testakten/beamtenrecht-dienstunfall-burnout-wiedereingliederung-hafenpolizei/gesamt-pdf/beamtenrecht-dienstunfall-burnout-wiedereingliederung-hafenpolizei_gesamt.pdf) | [`testakte-beamtenrecht-dienstunfall-burnout-wiedereingliederung-hafenpolizei.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-beamtenrecht-dienstunfall-burnout-wiedereingliederung-hafenpolizei.zip) | [`testakte-beamtenrecht-dienstunfall-burnout-wiedereingliederung-hafenpolizei-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-beamtenrecht-dienstunfall-burnout-wiedereingliederung-hafenpolizei-einzelpdfs.zip) |
| [Testakte Adelheid Pfister](../testakten/betreuung-adelheid-pfister-dreijahresabrechnung/README.md) | [Gesamt-PDF](../testakten/betreuung-adelheid-pfister-dreijahresabrechnung/gesamt-pdf/betreuung-adelheid-pfister-dreijahresabrechnung_gesamt.pdf) | [`testakte-betreuung-adelheid-pfister-dreijahresabrechnung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-betreuung-adelheid-pfister-dreijahresabrechnung.zip) | [`testakte-betreuung-adelheid-pfister-dreijahresabrechnung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/betreuungsrecht-v445.33.3/testakte-betreuung-adelheid-pfister-dreijahresabrechnung-einzelpdfs.zip) |
| [Betreuungsfall Hildegard Sauer](../testakten/betreuung-hildegard-sauer/README.md) | [Gesamt-PDF](../testakten/betreuung-hildegard-sauer/gesamt-pdf/betreuung-hildegard-sauer_gesamt.pdf) | [`testakte-betreuung-hildegard-sauer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-betreuung-hildegard-sauer.zip) | [`testakte-betreuung-hildegard-sauer-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-betreuung-hildegard-sauer-einzelpdfs.zip) |
| [Akte Betreuung Schmalfeld: Kontodaten und verdächtige Verträge](../testakten/betreuung-schmalfeld-kontodaten-vertraege/README.md) | [Gesamt-PDF](../testakten/betreuung-schmalfeld-kontodaten-vertraege/gesamt-pdf/betreuung-schmalfeld-kontodaten-vertraege_gesamt.pdf) | [`testakte-betreuung-schmalfeld-kontodaten-vertraege.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-betreuung-schmalfeld-kontodaten-vertraege.zip) | [`testakte-betreuung-schmalfeld-kontodaten-vertraege-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-betreuung-schmalfeld-kontodaten-vertraege-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

## Unterlagen aus drei Jahren auswerten

Das Fachmodul [Unterlagen auswerten, abrechnen und Anschreiben erstellen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/unterlagen-auswerten-abrechnung-anschreiben/FACHINHALT.md) führt von Kontoauszügen, Rechnungen und E-Mails zu einer nachvollziehbaren Excel-Abrechnung und konkreten Briefentwürfen. Es ist insbesondere für die Übernahme einer Betreuung mit ungeordneten Altunterlagen gedacht.

Beginnen Sie beispielsweise so:

> Ich habe die Vermögenssorge gerade übernommen. Untersuchen Sie die Unterlagen der letzten drei Jahre. Stellen Sie Einnahmen, Ausgaben und Kontensalden in Excel dar, verknüpfen Sie jede Position mit dem Beleg und klären Sie auffällige Zahlungen. Berücksichtigen Sie die Wünsche der betreuten Person. Entwerfen Sie anschließend die sachlich und rechtlich passenden Anschreiben an Bank, Angehörige und Anbieter.

Der Ablauf sichert zuerst Auftrag, Zeitraum und Originalbelege. Danach folgen Buchungserfassung, Kontenabgleich, Belegprüfung und Rückfragen. Interne Umbuchungen werden in der Gesamtrechnung herausgerechnet; Barabhebungen beweisen für sich allein keine Ausgaben oder Veruntreuung. Für jede Unklarheit werden mögliche Erklärungen und Gegenbelege mitgeführt. Adressen und Vertragsnummern stammen aus den Unterlagen, fehlende Angaben bleiben offen. Die historische Rekonstruktion wird von der eigenen Rechnungslegung seit Bestellung getrennt.

| Zugang | Inhalt |
| --- | --- |
| [Unterlagen-Werkstatt als Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/betreuungsrecht-unterlagen-werkstatt.md) | Großer eigenständiger Prompt mit Arbeitsablauf, Excel-Schema, Quellenprüfung und ausformulierten Briefbeispielen; ohne Plugin verwendbar. |
| [Identische Textfassung](betreuungsrecht-unterlagen-werkstatt.txt) | Derselbe Prompt zum Kopieren oder Hochladen. |
| [Excel-Vorlage](templates/unterlagen-abrechnung.xlsx) | Eingabe, Fundstellen, Kontenabstimmung, Auswertung und offene Fragen. Die Vorlage enthält keine Lösung der Testakte. |
| [Dreijahresakte Adelheid Pfister](../testakten/betreuung-adelheid-pfister-dreijahresabrechnung/README.md) | Drei Jahre vor Übernahme, zwei Konten, Rechnungen, E-Mails, Vertragsunterlagen und unterschiedliche Auskünfte aus dem Umfeld. |

In Fassung 445.33.3 heißt die betreute Person Adelheid Pfister; die Familiennamen, Unterlagen und Downloads sind entsprechend angepasst. Sachverhalt und Rechnungsdaten bleiben gleich.

Die Akten Schmalfeld, Hildegard Sauer und Adelheid Pfister bieten unterschiedliche Einstiege in den Betreuungsalltag. Die Dreijahresabrechnung liegt im [Aktenrelease 445.33.3](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/betreuungsrecht-v445.33.3). Das aktuelle Pluginpaket 445.35.4 ist oben verlinkt; allgemeine Sammelarchive können einen früheren Stand enthalten.

Briefe werden als Entwürfe erstellt. Die rechtliche Prüfung entscheidet für jeden Vertrag gesondert zwischen Nachfrage, Bestreiten, Kündigung oder einem tatsächlich eröffneten Gestaltungsrecht. Eine betreute Person ist nicht allein wegen der Betreuung geschäftsunfähig. Verdachtsmomente sind keine festgestellte Ausnutzung. Die Entscheidung über eine Erklärung und deren Versand bleibt bei der hierzu befugten Person.
Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Skills für **ehrenamtliche Familienbetreuerinnen und Familienbetreuer**, berufliche
Betreuerinnen und Betreuer, Vereinsbetreuer, Betreuungsbehörden und anwaltliche
Begleitung nach dem Betreuungsorganisationsgesetz (BtOG) und den §§ 1814 ff. BGB.

Das Plugin soll gerade nicht nur juristisch prüfen, sondern Betreuung praktisch
handhabbar machen: Post scannen, Fristen sehen, Berichte vorbereiten, mit dem
Betreuungsgericht ruhig kommunizieren, Kalender führen, Vermögen sauber trennen,
Wünsche der betreuten Person dokumentieren und rechtzeitig Hilfe holen.

> ⚠️ **Experimentell — keine Fachgutachten.** Die Skills sind generalisierte
> Beispiele. Jede Betreuerin und jeder Betreuer prüft jeden generierten Bericht,
> jede gerichtliche Eingabe und jede Fristenliste vor Verwendung. Bei
> Vermögen, Grundstücken, Erbe, Unterbringung, Zwangsbehandlung, Wohnungsaufgabe
> oder Familienkonflikt lieber früh Betreuungsgericht, Betreuungsverein,
> Betreuungsbehörde oder anwaltliche Hilfe einschalten.

## Enthaltene Skills

| Skill | Gegenstand | Rechtsnorm |
|---|---|---|
| `ehrenamtlicher-betreuer-erster-monat` | Startplan für Angehörige und ehrenamtliche Erstbetreuer: Beschluss lesen, Hilfe-System aktivieren, Unterlagen sichern, Fristenkalender anlegen | §§ 1814, 1821 BGB; §§ 15, 21, 22 BtOG |
| `familienbetreuer-alltagscockpit` | Wochenplan für Post, Pflege, Bank, Arzttermine, Gericht, Behörden, Wünsche und Risikoampel | §§ 1821, 1863 BGB |
| `dokumentenscan-aktenablage-und-belegmappe` | Scan-, Ablage- und Beleglogik für gerichtstaugliche Betreuungsakten | §§ 1835, 1863 BGB |
| `kalender-reminder-und-fristenmanagement` | Reminder für Jahresbericht, Vermögensverzeichnis, Bescheide, Gerichtstermine, Zahlungen und Routinekontakte | §§ 1835, 1863 BGB |
| `betreuungsgericht-kommunikation-fuer-angehoerige` | kurze, sachliche Briefe und Rückfragen an Gericht, Behörde, Verein, Bank, Heim und Arzt | BtOG, FamFG, §§ 1814 ff. BGB |
| `wunschermittlung-unterstuetzte-entscheidung` | Wünsche, Präferenzen, mutmaßlichen Willen und unterstützte Entscheidungen dokumentieren | § 1821 BGB |
| `jahresbericht-betreuungsgericht` | Strukturierter Jahresbericht ans Betreuungsgericht aus Ereignissen, E-Mails, Quittungen und Aktenvermerken | § 1863 BGB |
| `vermoegensverzeichnis-pruefung` | Erstellung und Aktualisierung des Vermögensverzeichnisses bei Übernahme der Betreuung | §§ 1835, 1839 BGB |
| `genehmigungspflicht-pruefung` | Prüfung, ob ein konkretes Rechtsgeschäft (Grundstücksverkauf, Erbausschlagung, Darlehen, Wohnungsauflösung, Heimvertrag) der Genehmigung des Betreuungsgerichts bedarf | §§ 1848–1858 BGB |
| `kontodaten-vertragsverdacht-pruefung` | Kontoauszüge und Vertragsunterlagen auf verdächtige Vermögensabflüsse, Fernwartung, Hochrisikoanlagen, Auslandszahlungen und Schutzmaßnahmen prüfen | §§ 1821, 1825, 1835, 1865 BGB |

## Adressatenkreis

- Ehrenamtliche Betreuerinnen und Betreuer, insbesondere Angehörige und nahestehende Personen
- Familienbetreuer, die erstmals mit Gericht, Bank, Heim, Pflegekasse und Arztkommunikation umgehen müssen
- Berufsbetreuerinnen und Berufsbetreuer mit Sachkundenachweis nach § 23 BtOG
- Vereinsbetreuerinnen und Vereinsbetreuer (§ 18 BtOG)
- Mitarbeiter von Betreuungsbehörden (§§ 6 ff. BtOG)
- Anwälte, die Betreuer, Angehörige oder Betroffene begleiten

## Wichtige Rechtsgrundlagen

- **BGB Buch 4 Abschnitt 3 (§§ 1814–1881)** — Rechtliche Betreuung (Reform 2023)
- **BtOG** — Betreuungsorganisationsgesetz (Betreuungsbehörde, Betreuungsvereine, ehrenamtliche und berufliche Betreuer)
- **VBVG** — Vormünder- und Betreuervergütungsgesetz
- **FamFG §§ 271 ff.** — Verfahren in Betreuungssachen

## Zitierhinweise

Alle Skills zitieren nach den in der deutschen Rechtspraxis üblichen Konventionen:

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

## Datenschutz und Vertraulichkeit

Berichte an das Betreuungsgericht enthalten Gesundheits-, Vermögens- und Sozialdaten.
Beim Einsatz von KI-Tools sind insbesondere zu beachten:

- Art. 9 DSGVO (besondere Kategorien personenbezogener Daten)
- berufliche Schweige-, Datenschutz- und Vertraulichkeitspflichten je nach Rolle
- Empfehlung: Personenbezogene Daten vor Übergabe an KI pseudonymisieren
  (siehe Skill `playbook-aus-eigenen-daten` im Plugin `kanzlei-builder-hub`)

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **118 vollständigen Fachmodule** und ihre Hilfsdateien stehen in der [Fachbibliothek](FACHMODULE.md). Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Person und Verfahren | [`person-und-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/person-und-verfahren-bearbeiten/SKILL.md) |
| 3. Erforderlichkeit und Aufgabenbereich | [`erforderlichkeit-und-aufgabenbereich-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/erforderlichkeit-und-aufgabenbereich-bearbeiten/SKILL.md) |
| 4. Entscheidung und Genehmigung | [`entscheidung-und-genehmigung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/entscheidung-und-genehmigung-bearbeiten/SKILL.md) |
| 5. Rechnungs- und Berichtswesen | [`rechnungs-und-berichtswesen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/rechnungs-und-berichtswesen-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Betreuungsrecht: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. Vollständige Fachanweisung... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Für Betreuungsrecht: Arbeitsprodukt: Antrag, Stellungnahme, Genehmigungsvorlage, Jahresbericht, Vermögensübersicht, Schutzplan oder Gerichtsschreiben erstellen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem kon... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Betreuungsrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/einstieg-routing/SKILL.md) |
| [`entscheidung-und-genehmigung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/entscheidung-und-genehmigung-bearbeiten/SKILL.md) | Für Betreuungsrecht: Entscheidung und Genehmigung: Vertretungsmacht, Ausschluss, Gesundheit, Unterbringung, Wohnung, Vermögen und Grundstücksgeschäft prüfen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkre... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/entscheidung-und-genehmigung-bearbeiten/SKILL.md) |
| [`erforderlichkeit-und-aufgabenbereich-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/erforderlichkeit-und-aufgabenbereich-bearbeiten/SKILL.md) | Für Betreuungsrecht: Erforderlichkeit und Aufgabenbereich: Unterstützungsbedarf, andere Hilfen, Wunsch, Einwilligungsfähigkeit und konkrete Angelegenheit trennen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem k... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/erforderlichkeit-und-aufgabenbereich-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/juristischer-argumentationskern/SKILL.md) | Betreuungsfall vom konkreten Bedarf zum begründeten Antrag führen. Nutzt vorhandene Falldaten, entscheidet die maßgeblichen rechtlichen Abzweigungen und verbindet passende Fachprüfungen mit einem vollständig ausgearbeiteten Ergebnis eins... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`person-und-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/person-und-verfahren-bearbeiten/SKILL.md) | Für Betreuungsrecht: Person und Verfahren: Betroffener, Betreuer, Vollmacht, Verfahrensstand, Anhörung, Gutachten und Eilbedarf erfassen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkreten Auftrag eingesetzt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/person-und-verfahren-bearbeiten/SKILL.md) |
| [`rechnungs-und-berichtswesen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/rechnungs-und-berichtswesen-bearbeiten/SKILL.md) | Für Betreuungsrecht: Rechnungs- und Berichtswesen: Vermögensverzeichnis, Belege, Kontobewegungen, Jahresbericht, Vergütung und Fristen nachvollziehbar aufbauen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem kon... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/rechnungs-und-berichtswesen-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Für Betreuungsrecht: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. Vollständige Fachanweisungen und lokale Vorlagen werden gezie... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Betreuungsrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
