# Arbeitszeugnis-Analyse (Ampelsystem)

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Analyse deutscher Arbeitszeugnisse nach Ampelsystem. Prüft Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien, Satznoten und Gesamtnotenspanne. Führt vom Erstgespräch über Mandantenbericht und Aufforderungsschreiben bis zur Klagestrategie.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`arbeitszeugnis-analyse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/arbeitszeugnis-analyse.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/arbeitszeugnis-analyse.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/arbeitszeugnis-analyse-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/arbeitszeugnis-analyse-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitszeugnis-analyse.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/arbeitszeugnis-analyse.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Arbeitszeugnis-Analyse (Ampelsystem):

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnis-analyse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/arbeitszeugnis-analyse.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`arbeitszeugnis-analyse-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/arbeitszeugnis-analyse-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`arbeitszeugnis-analyse-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/arbeitszeugnis-analyse-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Arbeitszeugnis-Analyse — aus dem blühenden Leben](../testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) | [Gesamt-PDF](../testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-ergaenzung-v1.0.0/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein deutsches Arbeitszeugnis nach dem Ampelsystem decodieren, die versteckte Gesamtnote bestimmen und entscheiden, ob sich ein Berichtigungsverlangen oder eine Zeugnisklage lohnt.

Dieses Plugin erläutert den Aussagegehalt deutscher Arbeitszeugnisse. Die Ampel kennzeichnet Prüfbedarf, nicht eine verbindliche Note oder eine nachgewiesene verdeckte Absicht. Ungewohnte Wörter, Reihenfolge und Schlussformel werden im Zusammenhang beurteilt; sie erlauben keine automatische Abwertung. Maßgeblich bleibt die im Werkstatt-Prompt erläuterte Gesamtbetrachtung nach BAG, Urteil vom 15.11.2011, 9 AZR 386/10, ohne hier eine neue Quellenprüfung zu behaupten.

Das Plugin richtet sich an Arbeitnehmer, die ihr eigenes Zeugnis verstehen oder verbessern wollen, an Rechtsanwälte, die Zeugnisstreitigkeiten begleiten, und an Personalverantwortliche, die Zeugnisse professionell ausstellen oder prüfen möchten.

**Hinweis:** Im Repository liegt ergänzend die Testakte `testakten/arbeitszeugnis-analyse-bluehendes-leben/` mit zehn realistisch ausgearbeiteten Zeugnisfällen. Jede Ausgabe ist ein Analyse-Entwurf zur eigenverantwortlichen Prüfung — kein Ersatz für anwaltliche Beratung im Einzelfall.

## Ampelsystem

Das Ampelsystem klassifiziert jeden notenrelevanten Satz in drei Kategorien:

| Ampel | Bedeutung | Prüfbedarf |
|---|---|---|
| Grün | Aussage passt zum Gesamttext und den belegten Aufgaben | Kein konkreter Änderungsbedarf erkannt |
| Orange | Einschränkung, Lücke oder mehrdeutige Aussage | Kontext und Beurteilungsgrundlage klären |
| Rot | Konkret begründeter Widerspruch oder Mangel | Passage mit Beleg und Ersatzvorschlag bearbeiten |

Rote Signale entstehen durch: das Wort "bemüht", Einschränkungen wie "im Wesentlichen", fehlende positionsnahe Erwartungsbausteine wie Integritäts- oder Führungsverhalten, falsche Reihenfolge bei Personengruppen in der Verhaltensbeurteilung oder eine auffällig kühle Schlussformel. Bei der Schlussformel ist strikt zu trennen: starke Signalwirkung im Bewerbungsverkehr, aber kein automatischer einklagbarer Anspruch auf Dank, Bedauern und Wünsche.

## Enthaltene Skills

Die wichtigsten Skills sind alphabetisch geordnet; die vollständige automatisch generierte Liste steht weiter unten:

| Skill | Funktion |
|---|---|
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: ampelsystem-tabellenausgabe` | Standardisiertes Ausgabeformat mit Ampeltabelle (Satz / Ampel / Bewertung / Note / Begründung) |
| `/arbeitszeugnis-analyse:berichtigung-anspruch-verfahren-bearbeiten Thema: aufforderungsschreiben-arbeitgeber` | Außergerichtliches Berichtigungsverlangen an den Arbeitgeber mit Wortlaut alt/neu pro Streitstelle |
| `/arbeitszeugnis-analyse:zeugnisauftrag-form-taetigkeit-bearbeiten Thema: azubi-zeugnis-analyse` | Ausbildungszeugnisse nach BBiG: Lernfortschritt, Berufsschule, Praxis, Verhalten |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: bereichs-drift-detektor` | Erkennt das Schaufenster-Pattern: Spitzensatz und Durchschnittssatz im selben Themenbereich |
| `/arbeitszeugnis-analyse:formulierungen-klarheit-schluss-bearbeiten Thema: branchen-spezifische-formulierungen` | Branchenspezifika für Vertrieb, Recht, IT, Pflege und weitere Bereiche |
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: erstgespraech-und-mandatsannahme` | Mandatsannahme mit Dank für das Zeugnis, Anforderung der noch fehlenden Unterlagen, Erstgespräch-Leitfaden |
| `/arbeitszeugnis-analyse:formulierungen-klarheit-schluss-bearbeiten Thema: geheimcode-katalog` | Zentraler Referenzkatalog aller Standardformulierungen mit Ampelzuordnung |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: gesamtnoten-aggregation` | Aggregation der Einzelbewertungen zur gewichteten Gesamtnote |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: gruen-flaggen-katalog` | Katalog aller grünen Signale: Superlative, vollständige Formeln, Note 1-2 |
| `/arbeitszeugnis-analyse:berichtigung-anspruch-verfahren-bearbeiten Thema: klage-strategie-zeugnisberichtigung` | Vom Befund zur Klage: Berichtigungsverlangen, Klageantrag, Beweislast, Streitwert |
| `/arbeitszeugnis-analyse:zeugnisauftrag-form-taetigkeit-bearbeiten Thema: leitende-positionen-zeugnisse` | Führungskräfte-Zeugnisse: Mitarbeiterführung, Strategie, Loyalität |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: leistungsbeurteilung-analyse` | Arbeitsqualität, Arbeitsbereitschaft, Belastbarkeit, Eigeninitiative |
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: mandantenbericht-zeugnisanalyse` | Ergebnisbericht an den Arbeitnehmer mit Gesamtnote, kritischen Stellen, drei Handlungsoptionen, klarer Empfehlung |
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: muster-arbeitszeugnis-gemischte-noten` | Schulungsmuster mit Schaufenster-Pattern: 1er- und 3er-Sätze gemischt, vollständige Drift-Analyse |
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: muster-arbeitszeugnis-mit-roten-flaggen` | Schulungsbeispiel mit gemischten Bewertungen und vollständiger Analyse |
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: muster-arbeitszeugnis-note-1` | Vollständiges Musterzeugnis Note 1 — alle Bausteine grün |
| `/arbeitszeugnis-analyse:formulierungen-klarheit-schluss-bearbeiten Thema: negationen-und-auslassungen-erkennen` | Fehlende Pflichtaussagen als versteckte Negativsignale erkennen |
| `/arbeitszeugnis-analyse:formulierungen-klarheit-schluss-bearbeiten Thema: negative-codeworte-katalog` | Erweiterter Katalog negativer Codeworte: Alkohol, Krankheit, Diebstahl, Konflikte, Loyalität |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: notenrelevante-saetze-identifizieren` | Trennung notenrelevanter Sätze von neutralen Aufgabenbeschreibungen |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: orange-flaggen-katalog` | Schwache positive Formulierungen, Note 3, fehlende Steigerungen |
| `/arbeitszeugnis-analyse:berichtigung-anspruch-verfahren-bearbeiten Thema: rechtliche-bewertung-bag-rechtsprechung` | Paragraf 109 GewO, BAG-Rechtsprechung, Beweislast, Zeugnisklage |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: rote-flaggen-katalog` | Klassische Warnsignale: "bemüht", "im Großen und Ganzen", Note 4-5 |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: satzweise-notenmatrix` | Satz-für-Satz-Notenzuweisung von eins bis fünf mit Themenbereich — Datenbasis für Drift |
| `/arbeitszeugnis-analyse:formulierungen-klarheit-schluss-bearbeiten Thema: schlussformel-bewertung` | Bedauern, Dank, Zukunftswünsche — Signalwirkung, Ton und rechtliche Durchsetzbarkeit getrennt |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: steigerungsadverbien-katalog` | Vollständige Referenzliste der Steigerer mit Notenwirkung — echte, scheinbare und negative Adverbien |
| `/arbeitszeugnis-analyse:formulierungen-klarheit-schluss-bearbeiten Thema: verbesserungsvorschlaege-formulieren` | Konkrete Textvorschläge zur Aufwertung von roten und orangen Formulierungen |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: verhaltensbeurteilung-analyse` | Verhalten zu Vorgesetzten, Kollegen, Kunden; Reihenfolge und Euphemismen |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: widerspruechliche-bewertungen` | Widersprüche zwischen Leistungs-, Verhaltensteil und Schlussformel |
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: zeugnis-problem-sortieren` | Neuer Einstieg für unsortierte Fragen: Was ist eigentlich das Problem am Zeugnis? |
| `/arbeitszeugnis-analyse:zeugnisauftrag-form-taetigkeit-bearbeiten Thema: zeugnisart-erkennung` | Qualifiziertes/einfaches Zeugnis, Zwischen-/Endzeugnis, Ausbildungszeugnis |
| `/arbeitszeugnis-analyse:zeugnisbericht-muster-qualitaet-bearbeiten Thema: zeugnis-ueberblick-extraktion` | Kopfdaten: Arbeitgeber, Arbeitnehmer, Zeitraum, Position, Unterschrift |
| `/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: zufriedenheitsformel-decodierung` | Fünfstufige Zufriedenheitsformel von Note 1 bis Note 5 |

## Verwendung

Laden Sie das zu analysierende Arbeitszeugnis hoch oder fügen Sie es als Text ein. Starten Sie dann mit dem gewünschten Skill:

```
/arbeitszeugnis-analyse:leistung-verhalten-noten-bearbeiten Thema: notenrelevante-saetze-identifizieren

Bitte analysiere das folgende Arbeitszeugnis und identifiziere alle notenrelevanten Sätze mit Ampelzuordnung:

[Zeugnis hier einfügen]
```

Die folgende Auswahl beschreibt einen umfassenden Prüfauftrag, keinen Pflichtdurchlauf. Zuerst vorhandenes Zeugnis und Auftrag lesen; nur entscheidende Lücken erfragen und Antworten im bestehenden Bericht verarbeiten. Beim einfachen Zeugnis entfallen Leistungsnoten und Verhaltensbewertung. Einzelaufträge enden mit dem bestellten Ergebnis, nicht automatisch mit Aufforderung oder Klage.
1. `erstgespraech-und-mandatsannahme` — Eingangsbestätigung, Unterlagenanforderung, Erstgespräch
2. `zeugnis-ueberblick-extraktion` — Kopfdaten prüfen
3. `zeugnisart-erkennung` — Zeugnistyp bestimmen
4. `notenrelevante-saetze-identifizieren` — Sätze kategorisieren
5. `steigerungsadverbien-katalog` — Adverbien tabellieren und Notenwirkung bestimmen
6. `satzweise-notenmatrix` — Aussage je Themenbereich einordnen; Notentendenz nur bei tragfähigem Kontext
7. `zufriedenheitsformel-decodierung` — Kernformel decodieren
8. `leistungsbeurteilung-analyse` + `verhaltensbeurteilung-analyse` — Detailanalyse
9. `schlussformel-bewertung` — Schlussformel als Signal und als Rechtsproblem getrennt bewerten
10. `negationen-und-auslassungen-erkennen` — Auslassungen prüfen
11. `negative-codeworte-katalog` — Auffällige Formulierungen prüfen, ohne aus einzelnen Wörtern Krankheit oder Fehlverhalten zu unterstellen
12. `bereichs-drift-detektor` — Schaufenster-Pattern prüfen
13. `widerspruechliche-bewertungen` — Block-Widersprüche prüfen
14. `ampelsystem-tabellenausgabe` — Gesamttabelle
15. `gesamtnoten-aggregation` — Gesamtbewertung begründen, keine rechnerische Note aus Satzmittelwerten oder automatischem Abschlag bilden
16. `verbesserungsvorschlaege-formulieren` — Aufwertungs-Rewrites pro Satz
17. `rechtliche-bewertung-bag-rechtsprechung` — rechtliche Einordnung der Befunde
18. `mandantenbericht-zeugnisanalyse` — Ergebnisbericht an den Mandanten mit drei Handlungsoptionen
19. `aufforderungsschreiben-arbeitgeber` — außergerichtliches Berichtigungsverlangen
20. `klage-strategie-zeugnisberichtigung` — bei gesondertem Durchsetzungsauftrag Erfolgsaussicht, Belege und Klageweg prüfen

## Rechtsgrundlagen

- **Paragraf 109 GewO** — Zeugnisanspruch: Anspruch auf einfaches oder qualifiziertes Zeugnis, Wahrheitspflicht, Wohlwollensgebot
- **Paragraf 16 BBiG** — Zeugnisanspruch für Auszubildende

Kein Ersatz für anwaltliche Beratung. Für die gerichtliche Geltendmachung eines Zeugnisberichtigungsanspruchs ist die Beauftragung eines Rechtsanwalts empfohlen.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **8 auswählbare Skills**. Die **51 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/kaltstart-triage/SKILL.md) |
| 2. Zeugnisauftrag, Form und Tätigkeitsbild | [`zeugnisauftrag-form-taetigkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) |
| 3. Leistung, Verhalten und Noten | [`leistung-verhalten-noten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/leistung-verhalten-noten-bearbeiten/SKILL.md) |
| 4. Formulierungen, Klarheit und Schlussformel | [`formulierungen-klarheit-schluss-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/formulierungen-klarheit-schluss-bearbeiten/SKILL.md) |
| 5. Berichtigung, Anspruch und Verfahren | [`berichtigung-anspruch-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/berichtigung-anspruch-verfahren-bearbeiten/SKILL.md) |
| 6. Zeugnisbericht, Muster und Qualitätskontrolle | [`zeugnisbericht-muster-qualitaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/zeugnisbericht-muster-qualitaet-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`berichtigung-anspruch-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/berichtigung-anspruch-verfahren-bearbeiten/SKILL.md) | Arbeitszeugnisanalyse mit Ampelbewertung: Berichtigungsanspruch, Beweislast, Fristen, Aufforderungsschreiben und gerichtliche Durchsetzung bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/berichtigung-anspruch-verfahren-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Arbeitszeugnis-Analyse. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/einstieg-routing/SKILL.md) |
| [`formulierungen-klarheit-schluss-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/formulierungen-klarheit-schluss-bearbeiten/SKILL.md) | Arbeitszeugnisanalyse mit Ampelbewertung: Auslassungen, Mehrdeutigkeiten, vermeintliche Codes und Schlussformeln am objektiven Empfängerhorizont prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/formulierungen-klarheit-schluss-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Arbeitszeugnis Analyse ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/kaltstart-triage/SKILL.md) | Für Kaltstart Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Arbeitszeugnis-Analyse. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/kaltstart-triage/SKILL.md) |
| [`leistung-verhalten-noten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/leistung-verhalten-noten-bearbeiten/SKILL.md) | Arbeitszeugnisanalyse mit Ampelbewertung: Bewertungssätze, Leistungsmerkmale und Verhalten im Gesamtzusammenhang analysieren und mit Belegen vergleichen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/leistung-verhalten-noten-bearbeiten/SKILL.md) |
| [`zeugnisauftrag-form-taetigkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) | Arbeitszeugnisanalyse mit Ampelbewertung: Zeugnisart, Anspruch, äußere Form, Tätigkeitsdarstellung und Anlass des Zeugnisses klären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) |
| [`zeugnisbericht-muster-qualitaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/zeugnisbericht-muster-qualitaet-bearbeiten/SKILL.md) | Arbeitszeugnisanalyse mit Ampelbewertung: Analyse, Beleglücken, Ergebnisdarstellung und Formulierungsentwurf zu einem verständlichen Arbeitsprodukt verbinden. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnis-analyse/skills/zeugnisbericht-muster-qualitaet-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
