# KI-Governance-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`ki-governance.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/ki-governance.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/ki-governance.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/ki-governance.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/ki-governance.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für KI-Governance-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`ki-governance.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/ki-governance.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`ki-governance-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`ki-governance-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [10 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [NeuroChain Labs — Gründung eines digitale Systeme/Krypto-Startups in Berlin, Musterprotokoll vs. individuelle Satzung](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/README.md) | [Gesamt-PDF](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/gesamt-pdf/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll_gesamt.pdf) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip) |
| [Falkenried & Partner mbB — Managementakte Q2/2026](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/README.md) | [Gesamt-PDF](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip) |
| [digitale Systeme-Governance Konzern-Rollout — Thalheim Industries SE](../testakten/ki-governance-konzern-rollout-thalheim-industries/README.md) | [Gesamt-PDF](../testakten/ki-governance-konzern-rollout-thalheim-industries/gesamt-pdf/ki-governance-konzern-rollout-thalheim-industries_gesamt.pdf) | [`testakte-ki-governance-konzern-rollout-thalheim-industries.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-governance-konzern-rollout-thalheim-industries.zip) | [`testakte-ki-governance-konzern-rollout-thalheim-industries-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-governance-konzern-rollout-thalheim-industries-einzelpdfs.zip) |
| [digitale Systeme-Recht — Betreiberpflichten und Grundrechte-Folgenabschätzung im Sozialamt (Duisburg)](../testakten/ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg/README.md) | [Gesamt-PDF](../testakten/ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg/gesamt-pdf/ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg_gesamt.pdf) | [`testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg.zip) | [`testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg-einzelpdfs.zip) |
| [digitale Systeme-Recht — GPAI, Deepfake-Transparenz und Wahlwerbung (Berlin/Havelbrück)](../testakten/ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin/README.md) | [Gesamt-PDF](../testakten/ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin/gesamt-pdf/ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin_gesamt.pdf) | [`testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin.zip) | [`testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin-einzelpdfs.zip) |
| [digitale Systeme-Recht — digitale Systeme-Vorfall mit Doppel- und Dreifachrelevanz (autonomer Lagerroboter, Dortmund)](../testakten/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund/README.md) | [Gesamt-PDF](../testakten/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund/gesamt-pdf/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund_gesamt.pdf) | [`testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund.zip) | [`testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund-einzelpdfs.zip) |
| [digitale Systeme-Recht — Konformitätsbewertung mit Lücken an der Schnittstelle zum Medizinprodukterecht (Triage-System, Freiburg)](../testakten/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg/README.md) | [Gesamt-PDF](../testakten/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg/gesamt-pdf/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg_gesamt.pdf) | [`testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg.zip) | [`testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg-einzelpdfs.zip) |
| [digitale Systeme-Recht — Marktüberwachungs- und Sanktionsverfahren wegen Emotionserkennung am Arbeitsplatz (Bonn)](../testakten/ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn/README.md) | [Gesamt-PDF](../testakten/ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn/gesamt-pdf/ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn_gesamt.pdf) | [`testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn.zip) | [`testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn-einzelpdfs.zip) |
| [digitale Systeme-Recht — Verbotene Praktik oder zulässige Risikobewertung? Kommunales Social Scoring (Chemnitz)](../testakten/ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz/README.md) | [Gesamt-PDF](../testakten/ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz/gesamt-pdf/ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz_gesamt.pdf) | [`testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz.zip) | [`testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz-einzelpdfs.zip) |
| [Akte Lahnwerke Maschinenbau AG - Slack, AirTags und IT-Sicherheitslage](../testakten/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit/README.md) | [Gesamt-PDF](../testakten/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit/gesamt-pdf/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit_gesamt.pdf) | [`testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit.zip) | [`testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Prüfe einen konkreten KI-Anwendungsfall, einen Anbieterentwurf oder eine bestehende Richtlinie. Für Datenschutz, Rechtsabteilung und Einkauf entstehen daraus die beauftragte Folgenabschätzung, Vertragsänderung oder Entscheidungsvorlage mit belegten Freigabebedingungen. Vorhandene Unterlagen bestimmen den Einstieg, nicht ein vorgeschaltetes Standardinterview.
Rechtsstand 10. September 2026: Die Governance-Routen unterscheiden geltende Betriebs- und Transparenzpflichten von späteren Hochrisikopflichten. Kompetenzmaßnahmen, Bias-Prüfung, Freigabe und Behördenkontakt greifen auf denselben datierten Rechtsstand zurück. [Rechtsstandkarte lesen](./references/digitaler-omnibus-2026.md) · <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/references/digitaler-omnibus-2026.md" download>MD herunterladen</a>.

Bei KI-Einsatz am Arbeitsplatz führt die Werkstatt die angemessene Informationsgrundlage für die Leitung, sichere Arbeitspraxis, die Beteiligung des Betriebsrats und Qualifizierung in einem befristeten Einführungsbeschluss zusammen. Die Rechtsgrundlagen und die jeweilige Verantwortung bleiben dabei einzeln sichtbar.

English: The updated workflows distinguish enacted law, future application dates and pending proposals. The reference note identifies official sources and the competent supervisory authority for each route.
Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Abläufe für betriebliche und kanzleiinterne KI-Governance: Use-Case-Triage, KI-Folgenabschätzungen,
Vendor-KI-Review und Gap-Analyse neuer Rechtsakte gegenüber bestehender Richtlinien- und Praxislage.
Das Plugin ist auf die EU-KI-Verordnung (VO 2024/1689, "KI-VO"), die DSGVO, das BDSG sowie
einschlägige deutschsprachige Rechtsgrundlagen (ProdHaftG, GeschGehG, UrhG, § 203 StGB) ausgerichtet.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – mit Fundstellen, Markierungen und
Kontrollgates versehen; kein Rechtsgutachten.** Das Plugin erledigt die Vorarbeit: Dokumente
lesen, Prüfrahmen anwenden, Probleme aufdecken, Memo entwerfen. Der Anwalt prüft, verifiziert
und entscheidet. Quellenangaben sind nach Herkunft gekennzeichnet. Berufsrechtliche Markierungen
(§ 203 StGB, § 43a Abs. 2 BRAO) werden konservativ gesetzt. Folgenreiche Handlungen
(Einreichen, Versenden, Ausführen) werden vor Umsetzung explizit bestätigt.

## Zielgruppe

| Rolle | Primäre Abläufe |
|---|---|
| **Datenschutzbeauftragte / KI-Governance-Counsel** | Folgenabschätzungen, Vendor-KI-Review, Gap-Analyse |
| **Syndikusanwälte / Produktjuristen** | Use-Case-Triage, Launch-Review mit KI-Komponente |
| **GC / Legal Ops** | KI-Richtlinien-Governance, Eskalation, Vorstandsthemen |
| **Einkauf / Vertragsrecht** | Vendor-KI-Vertragsreview nach Art. 28 DSGVO / Art. 11 KI-VO |

## Erster Start: das Kaltstart-Interview

Das optionale Interview richtet ein wiederverwendbares Praxisprofil ein. Zuerst werden die
vorhandenen Richtlinien, Verträge und früheren Prüfungen gelesen. Nur offene Rollen,
Entscheidungen oder Hausvorgaben werden erfragt. Bei einem konkreten Anwendungsfall oder
Dokumentauftrag beginnt die Facharbeit direkt; neue Antworten ergänzen den laufenden Entwurf.

```
/ki-governance:behoerden-und-sanktionslage-bearbeiten Thema: kaltstart-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/ki-governance:behoerden-und-sanktionslage-bearbeiten Thema: kaltstart-interview` | Kaltstart-Interview – schreibt Ihr Praxisprofil |
| `/ki-governance:rolle-und-lieferkette-bearbeiten Thema: ki-inventar-marketing-werbung-rote-linien [list \| add \| edit \| classify \| show]` | KI-Inventar verwalten – Rolle und Risikoklasse je KI-System nach KI-VO erfassen |
| `/ki-governance:unterlagen-und-quellen-auswerten-bearbeiten Thema: anwendungsfall-triage [Anwendungsfall]` | Use-Case gegen Ihr Register prüfen (genehmigt / bedingt / nie) |
| `/ki-governance:rolle-und-lieferkette-bearbeiten Thema: ki-folgenabschaetzung-ki-governance-mandat [Anwendungsfall]` | Auslöser für FRIA nach Artikel 27 und DSFA nach Artikel 35 getrennt prüfen und die jeweils erforderliche Folgenabschätzung erstellen |
| `/ki-governance:rolle-und-lieferkette-bearbeiten Thema: ki-anbieter-pruefung [Anbieter/Datei]` | Vendor-KI-Vertrag gegen Ihre Positionen prüfen |
| `/ki-governance:unterlagen-und-quellen-auswerten-bearbeiten Thema: regulierungs-luecken-analyse [Rechtsakt]` | Neuen Rechtsakt oder Leitlinie gegen aktuelle Richtlinien/Praxis abgleichen |
| `/ki-governance:rolle-und-lieferkette-bearbeiten Thema: richtlinien-monitor-vorlage-anbieter` | Wöchentliche Prüfung auf Richtliniendrift oder direkte Anfrage zu neuer Praxis |
| `/ki-governance:rolle-und-lieferkette-bearbeiten Thema: richtlinien-vorlage` | Erstentwurf einer KI-Richtlinie auf Basis Ihres Praxisprofils erstellen |
| `/ki-governance:arbeitsprodukt-bearbeiten Thema: mandat-arbeitsbereich` | Mandatsworkspaces verwalten (nur Kanzleipraxis) – new, list, switch, close, none |

## Skills

| Skill | Zweck |
|---|---|
| **kaltstart-interview** | Schreibt `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md` aus Interview + Seed-Dokumente |
| **ki-inventar** | Internes Organisationsverzeichnis mit Rollen, Funktionen, parallelen Pflichten und Quellen; von gesetzlichen Datenbankeinträgen nach Artikel 49 und 71 zu unterscheiden |
| **anwendungsfall-triage** | Prüft Anwendungsfälle gegen das Register; meldet fehlende Folgenabschätzungen |
| **ki-folgenabschätzung** | Auslöser für FRIA und DSFA getrennt prüfen; nur die jeweils erforderliche Prüfung im Hausformat ausarbeiten |
| **ki-anbieter-prüfung** | KI-spezifischer Vertragsreview gegen Governance-Positionen (Art. 11 KI-VO, Art. 28 DSGVO) |
| **regulierungs-luecken-analyse** | Neuer Rechtsakt/Leitlinie vs. Ist-Stand, Remediation-Plan |
| **richtlinien-monitor** | Prüft Ausgaben auf Praxisdrift; entwirft KI-Richtlinien-Updates |
| **richtlinien-vorlage** | Erstellt KI-Richtlinien-Entwurf auf Basis publizierter Musterrichtlinien (BVDW, Bitkom, EDSA, BSI, KI-VO), angepasst an Ihr Praxisprofil |
| **mandat-arbeitsbereich** | Mandatsworkspaces anlegen, auflisten, wechseln und schließen; isoliert jeden Mandanten/Auftrag, damit Kontext nicht durchsickert |

## Schnellstart

### 1. Optionale Einrichtung

```
/ki-governance:behoerden-und-sanktionslage-bearbeiten Thema: kaltstart-interview
```

Halten Sie bereit (soweit vorhanden): Ihre KI- oder Acceptable-Use-Richtlinie, eine frühere
Folgenabschätzung, Vendor-KI-Verträge, KI-Modell-Inventar oder genehmigte Tool-Liste.

Ihre Konfiguration wird gespeichert unter
`~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
und überlebt Plugin-Updates.

### 2. Neuen Anwendungsfall prüfen

```
/ki-governance:unterlagen-und-quellen-auswerten-bearbeiten Thema: anwendungsfall-triage "Vertrieb möchte KI zur automatischen Lead-Bewertung einsetzen"
```

Ausgabe: Risikoklasse nach KI-VO, Registerabgleich oder -lücke, erforderliche Bedingungen,
Folgenabschätzung erforderlich oder nicht.

### 3. Folgenabschätzung erstellen

```
/ki-governance:rolle-und-lieferkette-bearbeiten Thema: ki-folgenabschaetzung-ki-governance-mandat "KI-gestützte Lebenslauf-Analyse für HR"
```

Vorhandene System- und Einsatzunterlagen → entscheidende Lücken klären → ausgelöste
Folgenabschätzung im Hausformat → Richtlinienabgleich und konkrete Schutzbedingungen.

### 4. Vendor-KI-Vertrag prüfen

```
/ki-governance:rolle-und-lieferkette-bearbeiten Thema: ki-anbieter-pruefung openai-terms.pdf
```

Ausgabe: Klausel-für-Klausel-Vergleich mit Ihren Positionen, vorgeschlagene Änderungen,
Eskalationslücken.

## Dreieck: KI-Governance ↔ Produktrecht ↔ Datenschutzrecht

Diese drei Plugins sind aufeinander abgestimmt. KI-Governance ist das dritte Element.

- **Produktrecht** erkennt, wenn ein Launch eine KI-Komponente enthält → Übergabe an
  `/ki-governance:unterlagen-und-quellen-auswerten-bearbeiten Thema: anwendungsfall-triage` und `/ki-governance:rolle-und-lieferkette-bearbeiten Thema: ki-folgenabschaetzung-ki-governance-mandat`
- **Datenschutzrecht** erkennt, wenn ein KI-Anwendungsfall personenbezogene Daten umfasst →
  Übergabe an `/datenschutzrecht:dsfa-vvt-technische-organisation-bearbeiten Thema: dsfa-erstellung`, sofern das Plugin installiert ist
- **KI-Governance** erkennt, wenn eine Folgenabschätzung datenschutzrechtliche Fragen aufwirft →
  Übergabe an `/datenschutzrecht:dsfa-vvt-technische-organisation-bearbeiten Thema: dsfa-erstellung`

Die Übergabe ist explizit: Jedes Plugin meldet, wann das andere benötigt wird, und benennt
die zu klärende Frage.

## Rechtliche Grundlagen (Überblick)

| Rechtsakt | Relevanz im Plugin |
|---|---|
| **KI-Verordnung** | Verbote Artikel 5, beide Hochrisiko-Pfade Artikel 6 mit Anhängen I und III, rollenbezogene Pflichten, Modellpflichten, Transparenz und zeitliche Anwendung jeweils getrennt |
| **DSGVO** | DSFA (Art. 35), Auftragsverarbeitung (Art. 28), Auskunftsrecht (Art. 15), Automatisierte Entscheidungen (Art. 22) |
| **BDSG** | Beschäftigtendatenschutz (§ 26), ergänzende Regelungen zur DSGVO |
| **ProdHaftG / Produktsicherheitsrecht** | KI-Systeme als Produkte; Haftung für fehlerhafte KI-Ausgaben |
| **GeschGehG** | Schutz von Trainings- und Prozessdaten, Geheimhaltungspflichten |
| **UrhG / § 44b UrhG** | Text- und Data-Mining-Schranke (Art. 4 DSM-RL), Trainingsdaten, Opt-out |
| **§ 203 StGB** | Mandantengeheimnis, Schweigepflicht bei KI-Einsatz in der Kanzlei |

## Dateistruktur

```
ki-governance/
├── CLAUDE.md
├── README.md
├── references/
│   └── currency-watch.md
└── skills/
    ├── kaltstart-interview/
    ├── ki-inventar/          (ki-inventar)
    ├── anwendungsfall-triage/
    ├── ki-folgenabschaetzung/
    ├── ki-anbieter-pruefung/
    ├── regulierungs-luecken-analyse/
    ├── richtlinien-monitor/
    ├── richtlinien-vorlage/
    ├── mandat-arbeitsbereich/
    └── anpassen/
```

## Wie das Plugin lernt

Ihr Praxisprofil unter
`~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
ist nicht statisch – es verbessert sich durch die Nutzung. Skills zeigen an, wenn eine Ausgabe
auf einem Standard basiert, den Sie anpassen sollten. Der `richtlinien-monitor`-Agent beobachtet
Drift zwischen Ihrer KI-Governance-Richtlinie und Ihrer Praxis und schlägt Updates vor.
Sie können das Setup wiederholen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine
neue Position zu erfassen.

## Hinweise

- **Gap-Analyse** (`regulierungs-luecken-analyse`) verarbeitet eingehende Rechtsakte. **Policy-Monitor**
  behandelt internen Praxisdrift. Verschiedene Werkzeuge für verschiedene Änderungsrichtungen.
- Policy-Monitor benötigt einen konfigurierten Ausgabeordner für den Sweep. Direktabfrage-Modus
  funktioniert ohne diesen.
- Use-Case-Triage ist nur so gut wie das Register. Verbringen Sie Zeit im Setup-Interview damit,
  die roten Linien richtig zu erfassen – sie steuern alles.
- Format der Folgenabschätzung kommt aus Ihrer Seed-Folgenabschätzung. Ohne Seed-Dokument
  wird eine Grundstruktur verwendet – führen Sie das Setup erneut durch, um es zu verbessern.
- Anbieter- und Betreiberpflichten werden getrennt behandelt. Wenn Sie beides sind, fragen die
  Skills, welche Rolle Sie für die jeweilige Aufgabe tragen.
- Gap-Analyse ist manuell (Sie weisen auf einen Rechtsakt oder ein Leitliniendokument hin). Für
  automatisiertes Monitoring koppeln Sie mit dem `regulatorisches-recht`-Plugin.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **11 auswählbare Skills**. Die **60 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Rolle und Lieferkette | [`rolle-und-lieferkette-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rolle-und-lieferkette-bearbeiten/SKILL.md) |
| 3. Risikoklasse | [`risikoklasse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/risikoklasse-bearbeiten/SKILL.md) |
| 4. Stichtag | [`stichtag-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/stichtag-bearbeiten/SKILL.md) |
| 5. Nachweisakte | [`nachweisakte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/nachweisakte-bearbeiten/SKILL.md) |
| 6. Behörden- und Sanktionslage | [`behoerden-und-sanktionslage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/behoerden-und-sanktionslage-bearbeiten/SKILL.md) |
| 7. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 8. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 9. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

## KI-Einführung und Beschäftigung in der Praxis

Die Fallreihen verbinden Einstufung und Betreiberpflichten mit Arbeitsablauf, Qualifizierung, Datenschutz und Beteiligung. [Hamelner Compliance-Fälle](../compliance-abteilung-grosskonzern/README.md#4-ki-einführung-und-arbeit) · [Arbeitsrechtsfälle](../fachanwalt-arbeitsrecht/README.md#fallreihe-ki-und-arbeit)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Arbeitsprodukt: Einordnungsmemo, Roadmap, Vorstandsvorlage, Behördenantwort, Q&A, Vertragsmatrix oder Freigabevermerk erstellen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`behoerden-und-sanktionslage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/behoerden-und-sanktionslage-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Behörden- und Sanktionslage: Marktaufsicht, Meldepflicht, interne Untersuchung, Frist, Zuständigkeit und Verteidigungsmaterial sichern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/behoerden-und-sanktionslage-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/einstieg-routing/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/juristischer-argumentationskern/SKILL.md) | KI-Einsatz vom Anwendungsfall zur belastbaren Betriebsentscheidung führen. Verarbeitet vorhandene Unterlagen, verbindet entscheidende Fachprüfungen und belegte Quellen, erstellt das beauftragte Ergebnis und führt denselben Vorgang nach n... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/juristischer-argumentationskern/SKILL.md) |
| [`nachweisakte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/nachweisakte-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Nachweisakte: Risikomanagement, Daten, technische Dokumentation, Logging, menschliche Aufsicht, Testing und EU-Datenbank als Beleglinie führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/nachweisakte-bearbeiten/SKILL.md) |
| [`risikoklasse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/risikoklasse-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Risikoklasse: Art. 5, Art. 6 Abs. 1, Art. 6 Abs. 2, Art. 50, GPAI und Ausschlüsse in einer Entscheidungszeile ordnen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/risikoklasse-bearbeiten/SKILL.md) |
| [`rolle-und-lieferkette-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rolle-und-lieferkette-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Rolle und Lieferkette: Anbieter, Betreiber, Importeur, Händler, Bevollmächtigter, Produktintegration und Zweckbestimmung trennen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rolle-und-lieferkette-bearbeiten/SKILL.md) |
| [`stichtag-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/stichtag-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Stichtag: Änderungsverordnung 2026/1744 anwenden; feste Anhang-III- und Anhang-I-Termine, Bestandssysteme, GPAI, neue Verbote und Artikel 50 absatzbezogen trennen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/stichtag-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Unternehmerische KI-Governance: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Verbinden Sie Systemrisiken, Anbieter-QMS, konkrete Betreiberverwendung und Vorfallbearbeitung über gemeinsame Versions- und Zweckangaben. Ein umfassendes Richtlinienpaket ohne ausgeführte Tests beantwortet die materiellen Systemanforderungen nicht.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
