# Verlagsredaktion

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Verlagsdesk für juristische und fachliche Verlage: Eingangskorb, Manuskript, Redaktion, Rechtecheck, Zitate, Bildrechte, Autorenkommunikation, Heftplanung, Buchprojekte, Satzfahnen, Metadaten, Marketing und Produktionsübergabe.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`verlagsredaktion.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/verlagsredaktion.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/verlagsredaktion.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/verlagsredaktion-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/verlagsredaktion-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/verlagsredaktion.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/verlagsredaktion.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Verlagsredaktion:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`verlagsredaktion.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/verlagsredaktion.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`verlagsredaktion-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/verlagsredaktion-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`verlagsredaktion-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/verlagsredaktion-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Urheberrecht Musik-Songstreit Auerbach](../testakten/urheberrecht-musik-ki-songstreit-auerbach/README.md) | [Gesamt-PDF](../testakten/urheberrecht-musik-ki-songstreit-auerbach/gesamt-pdf/urheberrecht-musik-ki-songstreit-auerbach_gesamt.pdf) | [`testakte-urheberrecht-musik-ki-songstreit-auerbach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-urheberrecht-musik-ki-songstreit-auerbach.zip) | [`testakte-urheberrecht-musik-ki-songstreit-auerbach-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-urheberrecht-musik-ki-songstreit-auerbach-einzelpdfs.zip) |
| [Akte Lilienfeld Verlag: Fachbuch, E-Book-Bundle, Remittenden und Preisbindungsabmahnung](../testakten/verlagsrecht-buchpreisbindung-fachverlag-lilienfeld/README.md) | [Gesamt-PDF](../testakten/verlagsrecht-buchpreisbindung-fachverlag-lilienfeld/gesamt-pdf/verlagsrecht-buchpreisbindung-fachverlag-lilienfeld_gesamt.pdf) | [`testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld.zip) | [`testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld-einzelpdfs.zip) |
| [Verlagsredaktion Morgenlage Fachverlag](../testakten/verlagsredaktion-morgenlage-fachverlag/README.md) | [Gesamt-PDF](../testakten/verlagsredaktion-morgenlage-fachverlag/gesamt-pdf/verlagsredaktion-morgenlage-fachverlag_gesamt.pdf) | [`testakte-verlagsredaktion-morgenlage-fachverlag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-verlagsredaktion-morgenlage-fachverlag.zip) | [`testakte-verlagsredaktion-morgenlage-fachverlag-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-verlagsredaktion-morgenlage-fachverlag-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Ein Verlagsdesk für juristische und fachliche Verlage: Eingangskorb, Manuskriptaufnahme, Redaktion, Rechtecheck, Zitat- und Fundstellenkontrolle, Autorenkommunikation, Heftplanung, Buchprojektsteuerung, Satzfahnen, Metadaten, Marketingtexte, Produktionsübergabe und Qualitätstor.

Bei einem ungeordneten Postfach erstellt das Plugin eine Morgenlage mit Prioritäten und nächstem Arbeitsschritt. Ist bereits ein bestimmtes Lektorat, eine Autorenantwort oder eine Rechteprüfung beauftragt, beginnt es nach Sichtung der einschlägigen Unterlagen unmittelbar damit. Nur entscheidende Lücken werden erfragt und Antworten in die begonnene Fassung eingearbeitet.

## Installation

1. ZIP herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize → Plugins** bzw. **Personal plugins** öffnen.
4. **Upload plugin** wählen und `verlagsredaktion.zip` hochladen.

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `references/` enthalten.

## Was das Plugin gut können soll

- Aus einer unordentlichen Inbox eine Tagesübersicht machen.
- Manuskripte, Diktate, Folien, Screenshots, Tabellen und Autorenmails inventarisieren.
- Rohmanuskripte als Anschubhilfe erstellen, ohne fremde Texte zu kopieren.
- Vorhandene Texte strukturieren, kürzen, glätten und auf Widersprüche prüfen.
- Zitate, Fundstellen, Randnummern und Quellenstatus transparent markieren.
- Rechtefragen zu UrhG, Verlagsgesetz, Bildrechten, Tabellen und Fremdmaterialien als Ampel vorbereiten.
- Autoren freundlich, knapp und verbindlich anschreiben.
- Heft-, Buch- und Online-First-Workflows in Aufgaben und Fristen übersetzen.
- Klappentexte, Vorschauen, Metadaten und Marketingtexte aus dem Manuskript ableiten.
- Satzfahnen und Korrekturläufe steuern.
- KI-Einsatz, Datenschutz und Vertraulichkeit konservativ dokumentieren.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `kaltstart-triage` | Unterlagen sichten und zwischen Morgenlage, Lektorat, Autorenkommunikation und Rechteprüfung verzweigen. |
| `sachbearbeiterinnen-cockpit` | Persönliches Arbeitscockpit für Sachbearbeitung, Redaktion und Herstellung. |
| `eingangskorb-triage` | Mails, Dateien, Screenshots und Fristen in Prioritäten verwandeln. |
| `projektplan-fristen-heftplanung` | Projektplan für Heft, Online-Beitrag, Buchkapitel oder Kommentarupdate. |
| `manuskriptaufnahme-materialinventar` | Materialinventar mit Herkunft, Nutzbarkeit, Lücken und Rechteampel. |
| `verlagsredaktion` | Klassischer Rohmanuskript-/Editionsassistent. |
| `rohmanuskript-anschubhilfe` | Aus Material ein erstes, klar markiertes Rohmanuskript bauen. |
| `lektorat-struktur-redaktion` | Gliederung, Dramaturgie, Kürzung, Redundanz- und Widerspruchsprüfung. |
| `sprachlektorat-stil-tonalitaet` | Ton, Satzbau, Lesbarkeit, Verlagssprache, Zielgruppe. |
| `quellen-zitate-fundstellencheck` | Zitat- und Quellenhygiene ohne erfundene Literatur. |
| `rechtecheck-urhg-verlg` | Urheberrecht, Verlagsgesetz, Nutzungsrechte, Zitatrecht und Zweitveröffentlichung. |
| `bildrechte-grafiken-tabellen` | Bilder, Screenshots, Tabellen, Grafiken, Diagramme und Credits prüfen. |
| `fremdtext-plagiat-uebernahmecheck` | Fremdtext, KI-Text, Copy-Paste und Paraphrase-Risiken markieren. |
| `autorenkommunikation-email` | Autorenmails, Erinnerungen, Freigaben, Nachforderungen. |
| `honorar-vertrag-royalties-triage` | Vertrags-/Honorar-/Royalty-Fragen für redaktionelle Vorprüfung. |
| `metadaten-seo-klappentext` | Titel, Untertitel, Abstract, Schlagworte, VLB-/Web-Metadaten, Klappentext. |
| `zeitschriften-heftplanung` | Hefte, Rubriken, Deadlines, Online-first, Fahnen und Umbruch koordinieren. |
| `buchprojekt-kapitelkoordination` | Kapitel, Autoren, Register, Abbildungen, Vorwort und Produktionsstand. |
| `kommentar-aktualisierung-randnummern` | Kommentarupdates, Randnummern, Nachweise, Rechtsstandsvermerk. |
| `entscheidungsmonitor-rechtsstand` | Entscheidungen und Gesetzesänderungen als Aktualisierungsanlass erfassen. |
| `satzfahne-korrekturlauf` | Fahnenprüfung, Korrekturzeichen, Umbruch, Freigabe und letzte Checks. |
| `barrierefreiheit-epub-pdf` | Alt-Texte, Überschriftenlogik, Tabellenzugänglichkeit, EPUB/PDF-Check. |
| `marketing-presse-social` | Vorschau, Newsletter, Social Copy, Presseinfo und Nutzenargumente. |
| `sales-katalog-vlb-buchhandel` | Vertriebskurztext, Katalogdaten, Buchhandelsargumente, Zielgruppen. |
| `knowledge-base-faq-kundenservice` | FAQ und interne Wissensbasis für Vertrieb, Support und Redaktion. |
| `ai-einsatz-transparenz-datenschutz` | KI-Einsatz, Vertraulichkeit, DSGVO, Rechte und Freigabe dokumentieren. |
| `produktionsuebergabe-checkliste` | Übergabe an Herstellung, Satz, Online, Marketing, Vertrieb und Archiv. |
| `qualitaetsgate-verlag` | Schlussprüfung vor Autorenversand, Satz, Onlinegang oder Druck. |

## Quellenregel

- Keine Kommentar-, Handbuch-, Aufsatz- oder Datenbankfundstellen aus Modellwissen.
- Literatur nur aus Nutzerquelle, frei zugänglicher Quelle oder lizenziertem Live-Zugriff.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Fremdtexte niemals wörtlich übernehmen, außer der Nutzer verlangt ein zulässiges kurzes Zitat mit sauberer Quellenangabe und Zweck.
- Bei Verlagstexten immer trennen: Autorenmaterial, Redaktionstext, Fremdquelle, KI-Vorschlag und offene Lücke.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **13 auswählbare Skills**. Die **118 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Themen, Heftplanung und Redaktionskoordination | [`planung-koordination-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/planung-koordination-bearbeiten/SKILL.md) |
| 3. Materialaufnahme und Manuskriptentwicklung | [`material-manuskript-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/material-manuskript-bearbeiten/SKILL.md) |
| 4. Struktur-, Sprach- und Konsistenzlektorat | [`lektorat-sprache-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/lektorat-sprache-bearbeiten/SKILL.md) |
| 5. Rechtsstand, Quellen, Zitate und Aussageprüfung | [`quellen-aussagen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/quellen-aussagen-bearbeiten/SKILL.md) |
| 6. Autorenvertrag, Rechte, Honorar und Abrechnung | [`autorenrechte-honorar-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/autorenrechte-honorar-bearbeiten/SKILL.md) |
| 7. Rechtlicher Schutz, Datenschutz und Fehlerkorrektur | [`schutz-compliance-korrektur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/schutz-compliance-korrektur-bearbeiten/SKILL.md) |
| 8. Satz, Korrekturfahne, Barrierefreiheit und Produktion | [`satz-produktion-formate-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/satz-produktion-formate-bearbeiten/SKILL.md) |
| 9. Kommentar, Loseblatt und fortlaufende Aktualisierung | [`fortsetzungswerke-update-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/fortsetzungswerke-update-bearbeiten/SKILL.md) |
| 10. Metadaten, Marketing und Kundeninformation | [`vermarktung-kundenservice-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/vermarktung-kundenservice-bearbeiten/SKILL.md) |
| 11. Redaktionsauftrag, Aktenstand und geprüfte Übergabe | [`auftrag-uebergabe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/auftrag-uebergabe-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 13 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`auftrag-uebergabe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/auftrag-uebergabe-bearbeiten/SKILL.md) | Ordne Auftrag, Material, offene Punkte und Abstimmungen und liefere das beauftragte redaktionelle Ergebnis mit nachvollziehbarem Freigabestand. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig gelesen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/auftrag-uebergabe-bearbeiten/SKILL.md) |
| [`autorenrechte-honorar-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/autorenrechte-honorar-bearbeiten/SKILL.md) | Prüfe Verlags- und Nutzungsrechte, Autorenvereinbarung, Honorierung, Vorschuss und Abrechnung anhand des vereinbarten Werks und Umfangs. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig gelesen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/autorenrechte-honorar-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Verlagsredaktion. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/einstieg-routing/SKILL.md) |
| [`fortsetzungswerke-update-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/fortsetzungswerke-update-bearbeiten/SKILL.md) | Koordiniere Aktualisierung, Randnummern, Fassung und Fortsetzungsstand von Kommentaren und Loseblattwerken mit konkreten Quellen und Änderungsbezügen. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig ge... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/fortsetzungswerke-update-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Verlagsredaktion ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/juristischer-argumentationskern/SKILL.md) |
| [`lektorat-sprache-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/lektorat-sprache-bearbeiten/SKILL.md) | Überarbeite Aufbau, Sprache, Stil, Terminologie und innere Beziehungen ohne belegte Aussagen oder Autorenposition stillschweigend zu verändern. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig gelesen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/lektorat-sprache-bearbeiten/SKILL.md) |
| [`material-manuskript-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/material-manuskript-bearbeiten/SKILL.md) | Ordne Rohmaterial, ungewöhnliche Formate, Audio, Folien oder Notizen und entwickle daraus einen strukturierten Beitrag mit offengelegten Lücken. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig gelesen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/material-manuskript-bearbeiten/SKILL.md) |
| [`planung-koordination-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/planung-koordination-bearbeiten/SKILL.md) | Entwickle aus Zielgruppe und Fachprogramm einen belastbaren Themen- und Produktionsplan mit Zuständigkeit, Terminen und nachvollziehbaren Abstimmungen. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig g... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/planung-koordination-bearbeiten/SKILL.md) |
| [`quellen-aussagen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/quellen-aussagen-bearbeiten/SKILL.md) | Prüfe tragende Aussage, Fundstelle, Rechtsstand und Zitat im zugänglichen Original und kennzeichne nicht belegte Aussagen statt sie redaktionell zu verstärken. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und volls... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/quellen-aussagen-bearbeiten/SKILL.md) |
| [`satz-produktion-formate-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/satz-produktion-formate-bearbeiten/SKILL.md) | Prüfe Formatvorlage, Fahne, Layout, Barrierefreiheit und Übergabe an Satz oder Druck mit tatsächlichen Dateiprüfungen und Freigabestand. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig gelesen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/satz-produktion-formate-bearbeiten/SKILL.md) |
| [`schutz-compliance-korrektur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/schutz-compliance-korrektur-bearbeiten/SKILL.md) | Prüfe Fremdtext, Persönlichkeits- und Datenschutzrisiken, Impressum, KI-Einsatz und erforderliche Korrektur oder Rückruf gesondert von der sprachlichen Qualität. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vol... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/schutz-compliance-korrektur-bearbeiten/SKILL.md) |
| [`vermarktung-kundenservice-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/vermarktung-kundenservice-bearbeiten/SKILL.md) | Erstelle zutreffende Klappen-, Katalog-, Presse-, Newsletter- oder Social-Media-Texte und halte Produktbeschreibung und Fachinhalt konsistent. Die einschlägigen Fachmodule werden am konkreten Auftrag ausgewählt und vollständig gelesen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/vermarktung-kundenservice-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Verlagsredaktion. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verlagsredaktion/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Halten Sie fest, wer welche Passage in welcher Fassung geprüft und die redaktionelle Verantwortung übernommen hat. Eine bloße Schlussfreigabe ohne erkennbaren Gegenstand ist als Beleg gesondert zu würdigen.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
