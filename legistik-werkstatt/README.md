# Legistik-Werkstatt

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Legistik-Werkstatt für Ministerien, Bundestag, Fraktionen/Opposition, Länder, Landtage und Normgeber. Baut Referenten- und Kabinettsentwürfe, Vorlagen aus der Mitte, Änderungs-/Entschließungsanträge, Rechtsverordnungen und Satzungen mit Begründung, Synopse, XML und Prüfpfaden.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`legistik-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/legistik-werkstatt.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/legistik-werkstatt.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/legistik-werkstatt-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/legistik-werkstatt-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/legistik-werkstatt.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/legistik-werkstatt.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Legistik-Werkstatt:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`legistik-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/legistik-werkstatt.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`legistik-werkstatt-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/legistik-werkstatt-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`legistik-werkstatt-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/legistik-werkstatt-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Elektronisches Pflichtpostfach](../testakten/legistik-pflichtpostfach/README.md) | [Gesamt-PDF](../testakten/legistik-pflichtpostfach/gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf) | [`testakte-legistik-pflichtpostfach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-legistik-pflichtpostfach.zip) | [`testakte-legistik-pflichtpostfach-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-legistik-pflichtpostfach-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Vollständige Werkstatt für Legistinnen und Legisten in Bundesministerien, Bundestag, Fraktionen, Oppositionsarbeit, Landesministerien, Landtagen sowie kommunalen und kammerlichen Normgebern. Vom politischen Auftrag über Startbahn, Normhierarchie, Kompetenzprüfung, Normenkartierung und Terminologie zu Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Rechtsverordnung und Satzung. Mit Querschnittsprüfungen Verfassungsrecht Europarecht Folgenabschätzung Goldplating Bestimmtheit Zirkelschluss. Liefert den vollständigen Entwurf und, bei verfügbaren Render-Werkzeugen, DOCX und PDF im passenden Layout - ministerieller Referentenentwurf-Stil, BT-/Landtagsdrucksachen-Stil oder Arbeitsfassung für Fraktion, Ausschuss und Normgeber.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Upload plugin` wählen und die Datei auswählen.
3. Plugin aktivieren und eine neue Aufgabe öffnen; den passenden Skill ausdrücklich auswählen.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Was kann das Plugin?

Das Plugin deckt **alle Normebenen** ab:

- Bundesgesetz (Stammgesetz, Mantelgesetz, Änderungsgesetz)
- Landesgesetz
- Rechtsverordnung des Bundes und der Länder (Art. 80 GG, Landesverfassungen)
- Satzungen von Kommunen, Kammern und Hochschulen (Art. 28 Abs. 2 GG, Selbstverwaltung)
- Sekundärrechtsdurchführung und Notifizierung
- parlamentarischer Antrag, Entschließungsantrag, Änderungsantrag und Gesetzentwurf aus der Mitte des Bundestages oder Landtages

Das Plugin arbeitet mit **fünf Startbahnen**:

- Bundesressort / Bundesregierung: Referentenentwurf, Ressortabstimmung, NKR, Kabinett, Bundesrat, Bundestag
- Bundestag / Fraktion / Abgeordnete: Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag, Entschließungsantrag, Ausschussfassung
- Landesressort / Landesregierung: Landesreferentenentwurf, Landesverordnung, Kabinetts- und Landtagsweg
- Landtag / Landtagsfraktion: landesspezifischer Gesetzentwurf, Änderungsantrag, Antrag, Entschließungsantrag
- sonstiger Normgeber: kommunale Satzung, Kammerrecht, Hochschulsatzung, Beschlussvorlage, Bekanntmachung

Das Plugin prüft **immer**:

- Verfassungsrecht (GG, Landesverfassungen, BVerfG-Rechtsprechung)
- Europarecht (Primärrecht, Sekundärrecht, Notifizierung 2015/1535)
- Folgen (Erfüllungsaufwand, Bürokratiekosten, Nachhaltigkeit, KMU-Test)
- Goldplating und Wesentlichkeit
- Bestimmtheit, Terminologie und Zirkelschluss

Am Ende steht der vollständig beauftragte Entwurf. DOCX und PDF werden im passenden Layout erzeugt, wenn Dateizugriff und die unten genannten Render-Werkzeuge tatsächlich verfügbar sind; sonst wird der fertige Dokumenttext geliefert. Layoutprüfung und politische beziehungsweise institutionelle Freigabe sind getrennte Schritte. Unterstützte Ausgabearten:

- **Referentenentwurf** (Arial 11pt, Bearbeitungsstand-Kopf, A-F-Vorblatt)
- **BT-Drucksache** (Times New Roman 11pt, Drucksachennummer + Wahlperiode in der Kopfzeile, Sperrsatz für Hauptüberschriften, Anschreiben des Bundeskanzlers)
- **Formulierungshilfe / parlamentarische Vorlage** (für Koalition, Opposition, Ausschuss oder Ministerialzulieferung)
- **Antrag / Entschließungsantrag** (beschlussreif, mit Begründung und Kurzvermerk)
- **Synopse** (dreispaltig)
- **Lesefassung** (konsolidiert nach Inkrafttreten)
- **Kabinettsmappe** (Deckblatt + Anlagenverzeichnis)

## Skill-Tabelle

Die folgende Auswahl ordnet typische Schritte eines Gesetzgebungsvorhabens; sie ist kein vollständiges Bestandsverzeichnis.

| Phase | Skill | Zweck |
| --- | --- | --- |
| Auftrag | `legistik-auftragsaufnahme` | Startbahn, Institution, formalen Initiator und Regelungsauftrag übersetzen |
| Normhierarchie | `normhierarchie-routing` | Regierung vs Parlament; Gesetz vs Verordnung vs Satzung vs Antrag; Bund vs Land |
| Kompetenz | `gesetzgebungskompetenz-pruefen` | Art. 70 bis 74 GG, Erforderlichkeit |
| Kompetenz | `verordnungsermaechtigung-art80` | Inhalt Zweck Ausmass nach Art. 80 GG |
| Kompetenz | `satzungskompetenz-pruefen` | Art. 28 Abs. 2 GG, Kammern, Hochschulen |
| Mapping | `normenkartierung` | Verweisnetz und Änderungsstellen |
| Sprache | `terminologie-konsistenz` | Begriffsbrüche aufspüren |
| Sprache | `zirkelschluss-pruefen` | Verweisgraf zykelfrei |
| Entwurf | `referentenentwurf-bauen` | Vollformat des Bundes- oder Landes-Referentenentwurfs |
| Entwurf | `formulierungshilfe-bauen` | Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Antrag oder Entschließungsantrag |
| Entwurf | `gesetzesentwurf-kabinett` | Kabinettsmappe |
| Entwurf | `begruendung-allgemein-und-besonders` | Teil A I-VII und Teil B |
| Entwurf | `synopse-erstellen` | Dreispaltige Synopse |
| Entwurf | `lesefassung-konsolidiert` | Konsolidierte Fassung nach Inkrafttreten |
| Entwurf | `xml-paralleldarstellung` | LegalDocML.de und eNorm |
| Prüfung | `europarechtskonformitaet` | Primärrecht Sekundärrecht Notifizierung |
| Prüfung | `goldplating-vermeiden` | Überschießende Umsetzung von Unionsrecht |
| Prüfung | `verfassungsmaessigkeit-quercheck` | Grundrechte Verhältnismäßigkeit Bestimmtheit |
| Folgen | `folgenabschaetzung-erfuellungsaufwand` | Erfüllungsaufwand quantifizieren |
| Folgen | `folgenabschaetzung-nachhaltigkeit` | SDGs Klima Generationengerechtigkeit |
| Inkrafttreten | `inkrafttreten-uebergangsrecht` | Zeitpunkt Übergang Verkündung |
| Beteiligung | `verbaendeanhoerung-ressortabstimmung` | Anhörung und Abstimmung |
| Beteiligung | `normenkontrollrat-kmu-check` | NKR-Stellungnahme einholen |
| Lieferung | `dokumente-rendern-docx-pdf` | DOCX und PDF im offiziellen Layout |
| Schulung | `schulung-legistik` | Trainerleitfaden für Schulungen |

Alle Skills und Vertiefungen stehen mit Kurzbeschreibung und Download in der [vollständigen Skill-Liste](../skills-index/legistik-werkstatt.md).

## Beispielprojekt - Pflichtpostfachgesetz

Das Repository enthält eine vollständige Arbeitsakte unter `testakten/legistik-pflichtpostfach/`. Sie simuliert den Weg von der politischen Vorgabe (Koalitionsvertrag) zum lieferfertigen Referentenentwurf eines neuen Stammgesetzes über das elektronische Pflichtpostfach für HReg-Gesellschaften und sehr große Online-Plattformen.

So erzeugen Sie die fertigen Dokumente:

```bash
cd claude-fuer-deutsches-recht
python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format referentenentwurf \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output

python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format bt-drucksache \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output
```

Voraussetzung: `pip install python-docx pyyaml`. Für die PDF-Konvertierung zusätzlich LibreOffice (`soffice`).

## Disclaimer

Dieses Plugin ist ein Werkzeug zur Beschleunigung legistischer Arbeit. Es ersetzt nicht die juristische Prüfung durch verantwortliche Fachreferentinnen und Fachreferenten und nicht die Prüfung durch die Ressortleitung und das Bundesministerium der Justiz im Rahmen der Rechtsförmlichkeitsprüfung.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **14 auswählbare Skills**. Die **254 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`dokumente-rendern-docx-pdf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/dokumente-rendern-docx-pdf/SKILL.md), [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Regelungsziel und Kompetenz | [`regelungsziel-und-kompetenz-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/regelungsziel-und-kompetenz-bearbeiten/SKILL.md) |
| 3. Normtext und Rechtsförmlichkeit | [`normtext-und-rechtsfoermlichkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/normtext-und-rechtsfoermlichkeit-bearbeiten/SKILL.md) |
| 4. Folgen Kosten und Evaluation | [`folgen-kosten-und-evaluation-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/folgen-kosten-und-evaluation-bearbeiten/SKILL.md) |
| 5. Verfahren und Abstimmung | [`verfahren-und-abstimmung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/verfahren-und-abstimmung-bearbeiten/SKILL.md) |
| 6. Wirtschaft Finanzen und Infrastruktur | [`wirtschaft-finanzen-und-infrastruktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/wirtschaft-finanzen-und-infrastruktur-bearbeiten/SKILL.md) |
| 7. Soziales Gesundheit und Bildung | [`soziales-gesundheit-und-bildung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/soziales-gesundheit-und-bildung-bearbeiten/SKILL.md) |
| 8. Sicherheit Verwaltung und Europa | [`sicherheit-verwaltung-und-europa-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/sicherheit-verwaltung-und-europa-bearbeiten/SKILL.md) |
| 9. Umwelt Ernährung und Ressourcen | [`umwelt-ernaehrung-und-ressourcen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/umwelt-ernaehrung-und-ressourcen-bearbeiten/SKILL.md) |
| 10. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 11. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 14 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 14 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlun... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`dokumente-rendern-docx-pdf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/dokumente-rendern-docx-pdf/SKILL.md) | Für Dokumente rendern - DOCX und PDF im offiziellen HdR-Layout: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/dokumente-rendern-docx-pdf/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Legistik-Werkstatt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/einstieg-routing/SKILL.md) |
| [`folgen-kosten-und-evaluation-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/folgen-kosten-und-evaluation-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Folgen Kosten und Evaluation: Wirkung, Aufwand, Vollzug, digitale Tauglichkeit und Evaluation aus nachvollziehbaren Annahmen ableiten. Vollständige Fachanweisungen und lokale Vor... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/folgen-kosten-und-evaluation-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Legistik Werkstatt ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/juristischer-argumentationskern/SKILL.md) |
| [`normtext-und-rechtsfoermlichkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/normtext-und-rechtsfoermlichkeit-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Normtext und Rechtsförmlichkeit: Formulierungen, Änderungsbefehle, Verweisungen, Übergangsrecht und Inkrafttreten konsistent entwerfen. Vollständige Fachanweisungen und lokale Vo... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/normtext-und-rechtsfoermlichkeit-bearbeiten/SKILL.md) |
| [`regelungsziel-und-kompetenz-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/regelungsziel-und-kompetenz-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Regelungsziel und Kompetenz: Regelungsbedarf, Gesetzgebungskompetenz, Ermächtigung und grundrechtliche Grenzen bestimmen. Vollständige Fachanweisungen und lokale Vorlagen werden... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/regelungsziel-und-kompetenz-bearbeiten/SKILL.md) |
| [`sicherheit-verwaltung-und-europa-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/sicherheit-verwaltung-und-europa-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Sicherheit Verwaltung und Europa: Verwaltungs-, Sicherheits-, Justiz-, Digital- und Außenrecht sowie europäische Vorgaben regimestimmig umsetzen. Vollständige Fachanweisungen und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/sicherheit-verwaltung-und-europa-bearbeiten/SKILL.md) |
| [`soziales-gesundheit-und-bildung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/soziales-gesundheit-und-bildung-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Soziales Gesundheit und Bildung: Sozial-, Gesundheits-, Bildungs- und Forschungsrecht mit Vollzug und Schnittstellen ausgestalten. Vollständige Fachanweisungen und lokale Vorlage... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/soziales-gesundheit-und-bildung-bearbeiten/SKILL.md) |
| [`umwelt-ernaehrung-und-ressourcen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/umwelt-ernaehrung-und-ressourcen-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Umwelt Ernährung und Ressourcen: Umwelt-, Agrar-, Lebensmittel- und Ressourcenrecht mit den einschlägigen Genehmigungs- und Kontrollsystemen entwerfen. Vollständige Fachanweisung... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/umwelt-ernaehrung-und-ressourcen-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. Vollständige Fachanweis... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`verfahren-und-abstimmung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/verfahren-und-abstimmung-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Verfahren und Abstimmung: Gesetzgebungsverfahren, Beteiligung, Abstimmung und Notifizierung mit Zuständigkeit und Frist vorbereiten. Vollständige Fachanweisungen und lokale Vorla... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/verfahren-und-abstimmung-bearbeiten/SKILL.md) |
| [`wirtschaft-finanzen-und-infrastruktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/wirtschaft-finanzen-und-infrastruktur-bearbeiten/SKILL.md) | Für Staatsorganisation, Haushalts- und Normsetzungspraxis: Wirtschaft Finanzen und Infrastruktur: Fiskal-, Wirtschafts-, Bau- und Verkehrsvorhaben anhand ihrer fachlichen Systematik bearbeiten. Vollständige Fachanweisungen und lokale Vor... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/wirtschaft-finanzen-und-infrastruktur-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Legistik-Werkstatt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=legistik-werkstatt/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Trennen Sie bestehende unionsrechtliche Anforderungen von zusätzlichem nationalem Regelungsbedarf. Eine technische Norm oder Kommissionsleitlinie darf nicht ohne Prüfung ihres Rechtsstatus als gesetzliche Ermächtigung behandelt werden.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
