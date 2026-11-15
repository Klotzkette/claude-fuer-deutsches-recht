# Anlagen zu Schriftsätzen

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Gerichtsprozess-Dokumentenproduktion bis zur beA-fertigen Versandmappe: liest Schriftsatz und Anlagenordner, führt K/B/AST/AG fort, konvertiert und stempelt jede PDF-Seite, prüft ERVV, Signatur, Dateinamen, Empfänger und Eingang und liefert Verzeichnis, Manifest und Freigabevermerk.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`anlagen-zu-schriftsaetzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/anlagen-zu-schriftsaetzen.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/anlagen-zu-schriftsaetzen.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/anlagen-zu-schriftsaetzen-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/anlagen-zu-schriftsaetzen-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/anlagen-zu-schriftsaetzen.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/anlagen-zu-schriftsaetzen.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Anlagen zu Schriftsätzen:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: eine Produktionsmatrix und kontrollierte Gerichtsmappe. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`anlagen-zu-schriftsaetzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/anlagen-zu-schriftsaetzen.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`anlagen-zu-schriftsaetzen-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/anlagen-zu-schriftsaetzen-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`anlagen-zu-schriftsaetzen-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/anlagen-zu-schriftsaetzen-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/README.md) | [Gesamt-PDF](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf) | [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip) | [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler-einzelpdfs.zip) |
| [Der große Baufall - Talbrücke Fuchsbachtal und Tunnel Hirschleite](../testakten/baurecht-grosser-baufall-talbruecke-tunnel-a44/README.md) | [Gesamt-PDF](../testakten/baurecht-grosser-baufall-talbruecke-tunnel-a44/gesamt-pdf/baurecht-grosser-baufall-talbruecke-tunnel-a44_gesamt.pdf) | [`testakte-baurecht-grosser-baufall-talbruecke-tunnel-a44.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-baurecht-grosser-baufall-talbruecke-tunnel-a44.zip) | [`testakte-baurecht-grosser-baufall-talbruecke-tunnel-a44-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-baurecht-grosser-baufall-talbruecke-tunnel-a44-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin ist die Gerichtsprozess-Dokumentenproduktion für den letzten Weg bis zur versandfertigen beA-Mappe. Es nimmt einen Schriftsatz, einen chaotischen Mandantenordner oder ein schon halb nummeriertes Anlagenpaket und macht daraus eine nachvollziehbare, gerichtstaugliche Anlagenstruktur mit getrennten Versand-PDFs, Stempel auf jeder Anlagenseite, Manifest, Freigabevermerk und Eingangskontrolle.

Der schnellste vollständige Weg ist [`bea-versandmappe-endfertigung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/bea-versandmappe-endfertigung/FACHINHALT.md). Das Fachmodul liest vorhandenes Material zuerst und fragt nur nach einer wirklich blockierenden Weiche; es löst keinen Versand aus.

Für den optionalen lokalen PDF-Werkzeuglauf sind `pypdf` und `reportlab` in [`requirements.txt`](requirements.txt) dokumentiert. Fehlt eine Bibliothek, bricht das Werkzeug sofort mit einer Installationsangabe ab; der fachliche Skill-Workflow bleibt davon unabhängig nutzbar.

Der mitgelieferte Helfer `office_process.py` gehört neben `build_anlagenkonvolut.py`. Office erhält ein separates temporäres Profil; nach 120 Sekunden wird eine blockierte Konvertierung abgebrochen. Unter Linux und macOS werden auch ihre Kindprozesse beendet. Die übrigen Anlagen bleiben bearbeitbar, die fehlerhafte Anlage sperrt aber die Freigabe und benötigt einen Ersatzexport.

Es hilft besonders dann, wenn nicht einfach „Anlage K1 bis K12“ vorliegt, sondern wenn eine echte Akte lebt: E-Mails mit Anhängen, Scans ohne OCR, Excel-Tabellen, Fotos, Chat-Screenshots, mehrere Vertragsfassungen, fremdsprachige Unterlagen, doppelte Dateien, geschwärzte Drittunterlagen, beA-Grenzen, Verfahrenswechsel und Richterhinweise. Das Plugin führt dann nicht nur eine Nummerierung aus, sondern baut eine Arbeitslogik: Welche Tatsache soll durch welche Anlage belegt werden? Welche Datei gehört wirklich zu K1? Welche Unterlagen sind nur Konvolutbestandteil? Welche Anlage ist zu groß, unleserlich, falsch benannt, doppelt oder im Schriftsatz nicht eingeführt?

## Wofür es gedacht ist

| Situation | Was das Plugin macht | Ergebnis |
| --- | --- | --- |
| Klage/Replik liegt vor, Anlagen sind noch ungeordnet | Schriftsatz lesen, Beweisanker erkennen, K-Nummern vorschlagen, Dateien zuordnen | K1/K2/K3-Reihenfolge, Anlagenverzeichnis, Lückenliste |
| Anlagen sind schon nummeriert, aber niemand traut dem Paket | Prüfmodus: Nummern, Zitate, Dateien, Stempel, Namen, Lesbarkeit und beA-Fähigkeit prüfen | Fehlerprotokoll mit Korrekturplan |
| Mandant liefert Datenraum/ZIP/USB-Stick | Duplikate, Fassungen, Hashes, Dateitypen, Zeitfolge und Relevanz sortieren | Belegmatrix und Nachforderungsliste |
| Eine Anlage ist ein Konvolut | Deckblatt, Untergliederung, interne Seiten-/Dokumentlogik, kurze Erläuterung für Gericht | `Anlage K1` mit `K1.1`, `K1.2`, `K1.3` |
| Elektronische Einreichung steht bevor | Dateinamen, PDF/OCR, Paketgrößen, Anlagenverzeichnis, Prüfvermerk | beA-/ERV-taugliches Versandpaket |

## Der K1-Gedanke

Die erste Anlage ist fast nie nur eine Datei. In großen Verfahren ist `K1` häufig der Orientierungspunkt für das Gericht: Vertrag, Auftrag, Rahmenvereinbarung, Nachtrag, Bestätigungsmail, Protokoll oder Dokumentenfamilie. Das Plugin behandelt `K1` deshalb als Sortierproblem:

1. **Was soll K1 beweisen?** Nicht „alles zum Vertrag“, sondern eine konkrete Tatsache.
2. **Ist K1 Einzelanlage oder Konvolut?** Bei Konvolut: Deckblatt, Reihenfolge, interne Kurzbezeichnungen.
3. **Welche Fassungen gibt es?** Entwurf, unterschriebene Fassung, Scan, OCR-PDF, E-Mail-Anhang, spätere Ergänzung.
4. **Welche Datei ist die gerichtliche Fassung?** Die anderen Fassungen wandern in den internen Hash-/Versionenlog.
5. **Wie wird K1 im Schriftsatz eingeführt?** Der Schriftsatz muss den Tatsachenkern selbst tragen; die Anlage belegt ihn nur.

## Drei Arbeitsmodi

**Auto-Benennung:** Der Schriftsatz enthält noch keine Nummern. Das Plugin liest die Beweisstellen und schlägt die Reihenfolge vor.

**Schriftsatz folgt:** Der Schriftsatz enthält bereits `Anlage K...`-Verweise. Das Plugin sucht die passenden Dateien, erkennt Lücken und meldet Überschüsse.

**Prüfmodus:** Ein fertiges Anlagenpaket wird gegengeprüft: `K7` fehlt, `K12` ist doppelt, `K18` wird im Schriftsatz nie erwähnt, `K23` hat keinen OCR-Text, `K31` enthält ungeschwärzte Drittinformationen.

## Typische Outputs

- Anlagenverzeichnis für Gericht und Kanzleiakte.
- K/B/AST/AG-Nummerierung mit eindeutiger Dateinamenkonvention.
- Konvolutdeckblätter für Sammelanlagen.
- Belegmatrix: Tatsachenbehauptung ↔ Schriftsatzstelle ↔ Anlage ↔ Datei ↔ Status.
- Hash-/Duplikat-/Fassungslog für interne Kontrolle.
- beA-Versandliste mit Paketgrößen, Dateinamen und letzten Prüfpunkten.
- Nachforderungsliste an Mandant oder Sachbearbeitung.
- Berichtigungs- oder Nachreichungsplan nach gerichtlichem Hinweis.

## Wichtig

Anlagen ersetzen keinen Tatsachenvortrag. Wenn eine Behauptung entscheidungserheblich ist, muss sie im Schriftsatz stehen. Die Anlage belegt, erläutert oder vertieft; sie darf nicht der Ort sein, an dem der eigentliche Vortrag versteckt wird.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Upload plugin` wählen und die Datei auswählen.
3. Plugin aktivieren und eine neue Aufgabe öffnen; den passenden Skill ausdrücklich auswählen.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Besonders wichtige Skills

| Skill | Zweck |
| --- | --- |
| `bea-versandmappe-endfertigung` | Führt Schriftsatz und Anlagen vom Aktenordner bis zur kontrollierten Versandmappe mit Form-, Signatur- und Eingangskontrolle. |
| `anlagen-zu-schriftsaetzen-allgemein` | Kaltstart, Triage, Nummernkreis, Ziel-Schriftsatz, K1-Frage und Routing in die passenden Spezial-Skills. |
| `anlagen-zu-schriftsaetzen` | Hauptworkflow für Auto-Benennung, Schriftsatz-folgt-Modus, Prüfmodus und Reparatur nach Hinweis. |
| `k1-sortierwerkstatt` | Baut aus Vertrag, Nachtrag, Mail, Scan und OCR-Fassung eine klare Leit-Anlage `K1` oder ein K1-Konvolut. |
| `schriftsatz-anlagen-mapping` | Verknüpft Tatsachenvortrag, Schriftsatzstelle, Beweisangebot, Anlage und Datei in einer Belegmatrix. |
| `anlagen-duplikate-versionen-hashlog` | Erkennt Dubletten, Versionen, OCR-Kopien und die maßgebliche gerichtliche Fassung. |
| `bea-paketierung-groessen-und-versandplan` | Plant Dateinamen, Paketgrößen, Teilpakete, Begleitvermerk und Eingangskontrolle. |
| `anlagen-qualitygate-finalcheck` | Letzter strenger Check vor Versand: Nummern, Zitate, Dateien, OCR, Schwärzung, Stempel, Paket. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **118 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`anlagen-zu-schriftsaetzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/anlagen-zu-schriftsaetzen/SKILL.md), [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Prozessroute | [`prozessroute-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/prozessroute-bearbeiten/SKILL.md) |
| 3. Beweis | [`beweis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/beweis-bearbeiten/SKILL.md) |
| 4. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 5. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anlagen-zu-schriftsaetzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/anlagen-zu-schriftsaetzen/SKILL.md) | Hauptworkflow für gerichtliche Anlagenproduktion: liest Schriftsatz und Aktenordner zuerst, verbindet jede Behauptung mit ihrem Beleg, hält K-, B-, AST- oder AG-Nummern fort, erkennt Lücken und Dubletten und routet bei bevorstehendem Ver... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/anlagen-zu-schriftsaetzen/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Anlagen zu Schriftsätzen: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Anlagen zu Schriftsätzen: Arbeitsprodukt: Klageschrift, Klageerwiderung, Hinweisverfügung, Beschluss, Urteil, Tenor, Anlagenverzeichnis oder Fristenblatt erstellen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`beweis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/beweis-bearbeiten/SKILL.md) | Anlagen zu Schriftsätzen: Beweis: Beweisthema, Beweismittel, Substantiierung, Beweislast, Beweiswürdigung und Beweisbeschluss aus der Akte entwickeln. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/beweis-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Anlagen zu Schriftsätzen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/einstieg-routing/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Anlagen Zu Schriftsätzen ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/juristischer-argumentationskern/SKILL.md) |
| [`prozessroute-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/prozessroute-bearbeiten/SKILL.md) | Anlagen zu Schriftsätzen: Prozessroute: Gericht, Rechtsweg, Zuständigkeit, Streitwert, Frist, Einreichungsweg und Verfahrensstand sichern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/prozessroute-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Anlagen zu Schriftsätzen: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Anlagen zu Schriftsätzen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=anlagen-zu-schriftsaetzen/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
