# KI-Governance-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`ki-governance.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-governance.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/ki-governance.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/ki-governance.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/ki-governance.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für KI-Governance-Plugin:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Einordnungsmemo: Das System ist nach derzeitigem Stand [Rolle/Risikoklasse], weil [Zweckbestimmung] unter [Norm] fällt; Stichtag und Quellenstatus: [Datum/Quelle]. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`ki-governance.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-governance.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`ki-governance-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`ki-governance-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/ki-governance-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [10 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [NeuroChain Labs — Gründung eines digitale Systeme/Krypto-Startups in Berlin, Musterprotokoll vs. individuelle Satzung](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/README.md) | [Gesamt-PDF](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/gesamt-pdf/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll_gesamt.pdf) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip) |
| [Falkenried & Partner mbB — Managementakte Q2/2026](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/README.md) | [Gesamt-PDF](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip) |
| [digitale Systeme-Governance Konzern-Rollout — Thalheim Industries SE](../testakten/ki-governance-konzern-rollout-thalheim-industries/README.md) | [Gesamt-PDF](../testakten/ki-governance-konzern-rollout-thalheim-industries/gesamt-pdf/ki-governance-konzern-rollout-thalheim-industries_gesamt.pdf) | [`testakte-ki-governance-konzern-rollout-thalheim-industries.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-governance-konzern-rollout-thalheim-industries.zip) | [`testakte-ki-governance-konzern-rollout-thalheim-industries-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-governance-konzern-rollout-thalheim-industries-einzelpdfs.zip) |
| [digitale Systeme-Recht — Betreiberpflichten und Grundrechte-Folgenabschätzung im Sozialamt (Duisburg)](../testakten/ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg/README.md) | [Gesamt-PDF](../testakten/ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg/gesamt-pdf/ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg_gesamt.pdf) | [`testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg.zip) | [`testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-betreiberpflichten-fria-sozialamt-jobcenter-duisburg-einzelpdfs.zip) |
| [digitale Systeme-Recht — GPAI, Deepfake-Transparenz und Wahlwerbung (Berlin/Havelbrück)](../testakten/ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin/README.md) | [Gesamt-PDF](../testakten/ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin/gesamt-pdf/ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin_gesamt.pdf) | [`testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin.zip) | [`testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-gpai-transparenz-deepfake-wahlwerbung-berlin-einzelpdfs.zip) |
| [digitale Systeme-Recht — digitale Systeme-Vorfall mit Doppel- und Dreifachrelevanz (autonomer Lagerroboter, Dortmund)](../testakten/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund/README.md) | [Gesamt-PDF](../testakten/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund/gesamt-pdf/ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund_gesamt.pdf) | [`testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund.zip) | [`testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-ki-vorfall-dsgvo-produkthaftung-lager-roboter-dortmund-einzelpdfs.zip) |
| [digitale Systeme-Recht — Konformitätsbewertung mit Lücken an der Schnittstelle zum Medizinprodukterecht (Triage-System, Freiburg)](../testakten/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg/README.md) | [Gesamt-PDF](../testakten/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg/gesamt-pdf/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg_gesamt.pdf) | [`testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg.zip) | [`testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg-einzelpdfs.zip) |
| [digitale Systeme-Recht — Marktüberwachungs- und Sanktionsverfahren wegen Emotionserkennung am Arbeitsplatz (Bonn)](../testakten/ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn/README.md) | [Gesamt-PDF](../testakten/ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn/gesamt-pdf/ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn_gesamt.pdf) | [`testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn.zip) | [`testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-marktueberwachung-sanktionsverfahren-emotionserkennung-bonn-einzelpdfs.zip) |
| [digitale Systeme-Recht — Verbotene Praktik oder zulässige Risikobewertung? Kommunales Social Scoring (Chemnitz)](../testakten/ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz/README.md) | [Gesamt-PDF](../testakten/ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz/gesamt-pdf/ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz_gesamt.pdf) | [`testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz.zip) | [`testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-verbotene-praktik-social-scoring-abgrenzung-kommune-chemnitz-einzelpdfs.zip) |
| [Akte Lahnwerke Maschinenbau AG - Slack, AirTags und IT-Sicherheitslage](../testakten/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit/README.md) | [Gesamt-PDF](../testakten/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit/gesamt-pdf/nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit_gesamt.pdf) | [`testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit.zip) | [`testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nis2-cybersecurity-lahnwerke-slack-airtags-it-sicherheit-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Abläufe für betriebliche und kanzleiinterne KI-Governance: Use-Case-Triage, KI-Folgenabschätzungen,
Vendor-KI-Review und Gap-Analyse neuer Rechtsakte gegenüber bestehender Richtlinien- und Praxislage.
Das Plugin ist auf die EU-KI-Verordnung (VO 2024/1689, "KI-VO"), die DSGVO, das BDSG sowie
einschlägige deutschsprachige Rechtsgrundlagen (ProdHaftG, GeschGehG, UrhG, § 203 StGB) ausgerichtet.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – mit Fundstellen, Markierungen und
Kontrollgates versehen; kein Rechtsgutachten.** Das Plugin erledigt die Vorarbeit: Dokumente
lesen, Prüfrahmen anwenden, Probleme aufdecken, Memo entwerten. Der Anwalt prüft, verifiziert
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

Das Plugin befragt Sie, um zu erfahren: Sind Sie Anbieter, Betreiber oder beides? Welche
Regelwerke greifen konkret? Wo sind die roten Linien? Wie sieht eine interne Folgenabschätzung
bei Ihnen aus? Danach liest es Ihre Seed-Dokumente und lernt Ihre tatsächlichen Positionen
und Ihren Haustil.

```
/ki-governance:kaltstart-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/ki-governance:kaltstart-interview` | Kaltstart-Interview – schreibt Ihr Praxisprofil |
| `/ki-governance:ki-inventar [list \| add \| edit \| classify \| show]` | KI-Inventar verwalten – Rolle und Risikoklasse je KI-System nach KI-VO erfassen |
| `/ki-governance:anwendungsfall-triage [Anwendungsfall]` | Use-Case gegen Ihr Register prüfen (genehmigt / bedingt / nie) |
| `/ki-governance:ki-folgenabschaetzung [Anwendungsfall]` | KI-Folgenabschätzung (FRIA Art. 27 KI-VO + DSFA Art. 35 DSGVO) erstellen |
| `/ki-governance:ki-anbieter-pruefung [Anbieter/Datei]` | Vendor-KI-Vertrag gegen Ihre Positionen prüfen |
| `/ki-governance:regulierungs-luecken-analyse [Rechtsakt]` | Neuen Rechtsakt oder Leitlinie gegen aktuelle Richtlinien/Praxis abgleichen |
| `/ki-governance:richtlinien-monitor` | Wöchentliche Prüfung auf Richtliniendrift oder direkte Anfrage zu neuer Praxis |
| `/ki-governance:richtlinien-vorlage` | Erstentwurf einer KI-Richtlinie auf Basis Ihres Praxisprofils erstellen |
| `/ki-governance:mandat-arbeitsbereich` | Mandatsworkspaces verwalten (nur Kanzleipraxis) – new, list, switch, close, none |

## Skills

| Skill | Zweck |
|---|---|
| **kaltstart-interview** | Schreibt `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md` aus Interview + Seed-Dokumente |
| **ki-inventar** | KI-Inventar nach KI-VO – Rolle (Anbieter, Betreiber, Einführer, Händler, Bevollmächtigter, Produkthersteller) und Risikoklasse je System, Art. 6 KI-VO |
| **anwendungsfall-triage** | Prüft Anwendungsfälle gegen das Register; meldet fehlende Folgenabschätzungen |
| **ki-folgenabschätzung** | KI-Folgenabschätzung im Hausformat (FRIA + DSFA) |
| **ki-anbieter-prüfung** | KI-spezifischer Vertragsreview gegen Governance-Positionen (Art. 11 KI-VO, Art. 28 DSGVO) |
| **regulierungs-luecken-analyse** | Neuer Rechtsakt/Leitlinie vs. Ist-Stand, Remediation-Plan |
| **richtlinien-monitor** | Prüft Ausgaben auf Praxisdrift; entwirft KI-Richtlinien-Updates |
| **richtlinien-vorlage** | Erstellt KI-Richtlinien-Entwurf auf Basis publizierter Musterrichtlinien (BVDW, Bitkom, EDSA, BSI, KI-VO), angepasst an Ihr Praxisprofil |
| **mandat-arbeitsbereich** | Mandatsworkspaces anlegen, auflisten, wechseln und schließen; isoliert jeden Mandanten/Auftrag, damit Kontext nicht durchsickert |

## Schnellstart

### 1. Einrichtung

```
/ki-governance:kaltstart-interview
```

Halten Sie bereit (soweit vorhanden): Ihre KI- oder Acceptable-Use-Richtlinie, eine frühere
Folgenabschätzung, Vendor-KI-Verträge, KI-Modell-Inventar oder genehmigte Tool-Liste.

Ihre Konfiguration wird gespeichert unter
`~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
und überlebt Plugin-Updates.

### 2. Neuen Anwendungsfall prüfen

```
/ki-governance:anwendungsfall-triage "Vertrieb möchte KI zur automatischen Lead-Bewertung einsetzen"
```

Ausgabe: Risikoklasse nach KI-VO, Registerabgleich oder -lücke, erforderliche Bedingungen,
Folgenabschätzung erforderlich oder nicht.

### 3. Folgenabschätzung erstellen

```
/ki-governance:ki-folgenabschaetzung "KI-gestützte Lebenslauf-Analyse für HR"
```

Aufnahme-Fragen → Folgenabschätzung im Hausformat → Richtlinien-Konsistenzprüfung →
Mitigationsbedingungen.

### 4. Vendor-KI-Vertrag prüfen

```
/ki-governance:ki-anbieter-pruefung openai-terms.pdf
```

Ausgabe: Klausel-für-Klausel-Vergleich mit Ihren Positionen, vorgeschlagene Änderungen,
Eskalationslücken.

## Dreieck: KI-Governance ↔ Produktrecht ↔ Datenschutzrecht

Diese drei Plugins sind aufeinander abgestimmt. KI-Governance ist das dritte Element.

- **Produktrecht** erkennt, wenn ein Launch eine KI-Komponente enthält → Übergabe an
  `/ki-governance:anwendungsfall-triage` und `/ki-governance:ki-folgenabschaetzung`
- **Datenschutzrecht** erkennt, wenn ein KI-Anwendungsfall personenbezogene Daten umfasst →
  Übergabe an `/datenschutzrecht:dsfa-erstellung`, sofern das Plugin installiert ist
- **KI-Governance** erkennt, wenn eine Folgenabschätzung datenschutzrechtliche Fragen aufwirft →
  Übergabe an `/datenschutzrecht:dsfa-erstellung`

Die Übergabe ist explizit: Jedes Plugin meldet, wann das andere benötigt wird, und benennt
die zu klärende Frage.

## Rechtliche Grundlagen (Überblick)

| Rechtsakt | Relevanz im Plugin |
|---|---|
| **KI-VO (VO 2024/1689)** | Risikoklassen (Art. 6, Anh. I–III), Verbote (Art. 5), Betreiberpflichten (Art. 26), Transparenz (Art. 50), Bußgeld (Art. 99), FRIA (Art. 27), Technische Dokumentation (Art. 11) |
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


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-router`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anschluss-router/SKILL.md), [`anwendungsfall-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anwendungsfall-triage/SKILL.md), [`dokumente-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dokumente-intake/SKILL.md), [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/einstieg-routing/SKILL.md), [`kaltstart-interview`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kaltstart-interview/SKILL.md), [`ki-folgenabschaetzung-ki-governance-mandat`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-folgenabschaetzung-ki-governance-mandat/SKILL.md), [`ki-governance-mandatsworkspace-kontexttrennung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-governance-mandatsworkspace-kontexttrennung/SKILL.md), [`mandat-arbeitsbereich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/mandat-arbeitsbereich/SKILL.md), [`triage-haftung-versicherung-anwendungsfall`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/triage-haftung-versicherung-anwendungsfall/SKILL.md), [`workflow-anschluss-skills-router`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-anschluss-skills-router/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`governance-compliance-dokumentation-und-akte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/governance-compliance-dokumentation-und-akte/SKILL.md), [`inventar-dokumentenmatrix-und-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/inventar-dokumentenmatrix-und-lueckenliste/SKILL.md), [`monitoring-quellenkarte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/monitoring-quellenkarte/SKILL.md), [`quellen-livecheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/quellen-livecheck/SKILL.md), [`rechtsquellen-sonderfall-edge-case`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rechtsquellen-sonderfall-edge-case/SKILL.md), [`regulierungs-luecken-analyse`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/regulierungs-luecken-analyse/SKILL.md), [`spezial-monitoring-livequellen-und-rechtsprechungscheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/spezial-monitoring-livequellen-und-rechtsprechungscheck/SKILL.md), [`unterlagen-luecken`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/unterlagen-luecken/SKILL.md), [`werbung-beweislast-und-darlegungslast`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/werbung-beweislast-und-darlegungslast/SKILL.md), [`workflow-chronologie-und-belegmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`dpia-risikoampel-und-gegenargumente`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dpia-risikoampel-und-gegenargumente/SKILL.md), [`fristen-risikoampel-mandantenkommunikation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/fristen-risikoampel-mandantenkommunikation/SKILL.md), [`inventar-kontrollen-konformitaetsbewertung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/inventar-kontrollen-konformitaetsbewertung/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/juristischer-argumentationskern/SKILL.md), [`ki-anbieter-pruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-anbieter-pruefung/SKILL.md), [`ki-haftung-und-versicherung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-haftung-und-versicherung/SKILL.md), [`ki-hochrisiko-anhang-iii-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-hochrisiko-anhang-iii-pruefen/SKILL.md), [`kig-konformitaetsbewertung-risikobewertung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-konformitaetsbewertung-risikobewertung/SKILL.md), [`kig-risikobewertung-hochrisiko-leitfaden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-risikobewertung-hochrisiko-leitfaden/SKILL.md), [`rollen-rasci-hochrisiko-anhang-incident`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rollen-rasci-hochrisiko-anhang-incident/SKILL.md), [`spezial-pruefung-internationaler-bezug-und-schnittstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/spezial-pruefung-internationaler-bezug-und-schnittstellen/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`drift-verhandlung-vergleich-und-eskalation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/drift-verhandlung-vergleich-und-eskalation/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`review-schriftsatz-brief-und-memo-bausteine`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/review-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`vendor-behoerden-gericht-und-registerweg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/vendor-behoerden-gericht-und-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`marketing-mandantenkommunikation-entscheidungsvorlage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/marketing-mandantenkommunikation-entscheidungsvorlage/SKILL.md), [`output-waehlen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/output-waehlen/SKILL.md), [`workflow-mandantenkommunikation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-mandantenkommunikation/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`konformitaetsbewertung-red-team-und-qualitaetskontrolle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/konformitaetsbewertung-red-team-und-qualitaetskontrolle/SKILL.md), [`review-richtlinie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/review-richtlinie/SKILL.md), [`workflow-redteam-qualitygate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`anbieter-mehrparteien-konflikt-und-interessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anbieter-mehrparteien-konflikt-und-interessen/SKILL.md), [`anpassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anpassen/SKILL.md), [`case-dpia-drift`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/case-dpia-drift/SKILL.md), [`dsgvo-governance-inventar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dsgvo-governance-inventar/SKILL.md), [`gpai-modelle-ki-anbieter-arbeitsrecht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/gpai-modelle-ki-anbieter-arbeitsrecht/SKILL.md), [`ki-arbeitsrecht-mitbestimmung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-arbeitsrecht-mitbestimmung/SKILL.md), [`ki-incident-management-art-73`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-incident-management-art-73/SKILL.md), [`ki-inventar-marketing-werbung-rote-linien`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-inventar-marketing-werbung-rote-linien/SKILL.md), [`ki-marketing-und-werbung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-marketing-und-werbung/SKILL.md), [`ki-rote-linien-art-5-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-rote-linien-art-5-pruefen/SKILL.md), [`kig-ai-act-rollenmodell-bauleiter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-ai-act-rollenmodell-bauleiter/SKILL.md), [`kig-foundation-model-anbieterpflichten-spezial`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-foundation-model-anbieterpflichten-spezial/SKILL.md), [`richtlinie-zahlen-schwellen-und-berechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinie-zahlen-schwellen-und-berechnung/SKILL.md), [`richtlinien-monitor-vorlage-anbieter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinien-monitor-vorlage-anbieter/SKILL.md), [`richtlinien-vorlage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinien-vorlage/SKILL.md), [`rollenmodell-use-case-vendor`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rollenmodell-use-case-vendor/SKILL.md), [`use-case-risk-classification`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/use-case-risk-classification/SKILL.md), [`vo-pflichtenpyramide-kig-ai-foundation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/vo-pflichtenpyramide-kig-ai-foundation/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 60 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anbieter-mehrparteien-konflikt-und-interessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anbieter-mehrparteien-konflikt-und-interessen/SKILL.md) | Für Anbieter: Mehrparteienkonflikt und Interessenmatrix: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anbieter-mehrparteien-konflikt-und-interessen/SKILL.md) |
| [`anpassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anpassen/SKILL.md) | Für /anpassen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anpassen/SKILL.md) |
| [`anschluss-router`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anschluss-router/SKILL.md) | Für digitale Werkzeuge-Governance — Allgemein: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anschluss-router/SKILL.md) |
| [`anwendungsfall-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anwendungsfall-triage/SKILL.md) | Für digitale Werkzeuge-Anwendungsfall-Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/anwendungsfall-triage/SKILL.md) |
| [`case-dpia-drift`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/case-dpia-drift/SKILL.md) | Für Case: Tatbestandsmerkmale, Beweisfragen und Beleglage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/case-dpia-drift/SKILL.md) |
| [`dokumente-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dokumente-intake/SKILL.md) | Für Dokumentenintake: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dokumente-intake/SKILL.md) |
| [`dpia-risikoampel-und-gegenargumente`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dpia-risikoampel-und-gegenargumente/SKILL.md) | Für Dpia: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dpia-risikoampel-und-gegenargumente/SKILL.md) |
| [`drift-verhandlung-vergleich-und-eskalation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/drift-verhandlung-vergleich-und-eskalation/SKILL.md) | Für Drift: Verhandlung, Vergleich und Eskalation: entwickelt Ziel, Vergleich und Eskalation; Ergebnis: Verhandlungs- oder Eskalationslinie. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/drift-verhandlung-vergleich-und-eskalation/SKILL.md) |
| [`dsgvo-governance-inventar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dsgvo-governance-inventar/SKILL.md) | Für DSGVO: Erstprüfung, Rollenklärung und Mandatsziel: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/dsgvo-governance-inventar/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/einstieg-routing/SKILL.md) |
| [`fristen-risikoampel-mandantenkommunikation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/fristen-risikoampel-mandantenkommunikation/SKILL.md) | Für Fristen- und Risikoampel: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/fristen-risikoampel-mandantenkommunikation/SKILL.md) |
| [`governance-compliance-dokumentation-und-akte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/governance-compliance-dokumentation-und-akte/SKILL.md) | Für Governance: Compliance-Dokumentation und Aktenvermerk: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/governance-compliance-dokumentation-und-akte/SKILL.md) |
| [`gpai-modelle-ki-anbieter-arbeitsrecht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/gpai-modelle-ki-anbieter-arbeitsrecht/SKILL.md) | Für GPAI: Systemic-Risk-Modelle: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/gpai-modelle-ki-anbieter-arbeitsrecht/SKILL.md) |
| [`inventar-dokumentenmatrix-und-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/inventar-dokumentenmatrix-und-lueckenliste/SKILL.md) | Für Inventar: Dokumentenmatrix, Lückenliste und Nachforderung: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/inventar-dokumentenmatrix-und-lueckenliste/SKILL.md) |
| [`inventar-kontrollen-konformitaetsbewertung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/inventar-kontrollen-konformitaetsbewertung/SKILL.md) | Für digitale Werkzeuge-Inventar, Governance und Kontrollen: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/inventar-kontrollen-konformitaetsbewertung/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn bei der Governance algorithmischer Systeme ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Recht... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-interview`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kaltstart-interview/SKILL.md) | Für Erstgespräch digitale Werkzeuge-Governance: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kaltstart-interview/SKILL.md) |
| [`ki-anbieter-pruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-anbieter-pruefung/SKILL.md) | Für digitale Werkzeuge-Anbieterprüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-anbieter-pruefung/SKILL.md) |
| [`ki-arbeitsrecht-mitbestimmung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-arbeitsrecht-mitbestimmung/SKILL.md) | Für digitale Werkzeuge: Arbeitsrecht und BR: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-arbeitsrecht-mitbestimmung/SKILL.md) |
| [`ki-folgenabschaetzung-ki-governance-mandat`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-folgenabschaetzung-ki-governance-mandat/SKILL.md) | Für /ki-folgenabschätzung – digitale Werkzeuge-Folgenabschätzung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-folgenabschaetzung-ki-governance-mandat/SKILL.md) |
| [`ki-governance-mandatsworkspace-kontexttrennung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-governance-mandatsworkspace-kontexttrennung/SKILL.md) | Für digitale Werkzeuge-Governance-Mandatsworkspace und Kontexttrennung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-governance-mandatsworkspace-kontexttrennung/SKILL.md) |
| [`ki-haftung-und-versicherung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-haftung-und-versicherung/SKILL.md) | Für digitale Werkzeuge-Haftung und Versicherung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-haftung-und-versicherung/SKILL.md) |
| [`ki-hochrisiko-anhang-iii-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-hochrisiko-anhang-iii-pruefen/SKILL.md) | Für Hochrisiko-digitale Werkzeuge Anhang III: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-hochrisiko-anhang-iii-pruefen/SKILL.md) |
| [`ki-incident-management-art-73`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-incident-management-art-73/SKILL.md) | Für digitale Werkzeuge Incident-Management: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-incident-management-art-73/SKILL.md) |
| [`ki-inventar-marketing-werbung-rote-linien`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-inventar-marketing-werbung-rote-linien/SKILL.md) | Für /ki-inventar: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-inventar-marketing-werbung-rote-linien/SKILL.md) |
| [`ki-marketing-und-werbung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-marketing-und-werbung/SKILL.md) | Für digitale Werkzeuge: Marketing und Werbung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-marketing-und-werbung/SKILL.md) |
| [`ki-rote-linien-art-5-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-rote-linien-art-5-pruefen/SKILL.md) | Für Verbotene digitale Werkzeuge Art. 5 prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/ki-rote-linien-art-5-pruefen/SKILL.md) |
| [`kig-ai-act-rollenmodell-bauleiter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-ai-act-rollenmodell-bauleiter/SKILL.md) | Für KIG: digitale Werkzeuge-Act-Rollenmodell: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-ai-act-rollenmodell-bauleiter/SKILL.md) |
| [`kig-foundation-model-anbieterpflichten-spezial`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-foundation-model-anbieterpflichten-spezial/SKILL.md) | Für KIG: GPAI Anbieterpflichten: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-foundation-model-anbieterpflichten-spezial/SKILL.md) |
| [`kig-konformitaetsbewertung-risikobewertung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-konformitaetsbewertung-risikobewertung/SKILL.md) | Für KIG: Konformitätsbewertung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-konformitaetsbewertung-risikobewertung/SKILL.md) |
| [`kig-risikobewertung-hochrisiko-leitfaden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-risikobewertung-hochrisiko-leitfaden/SKILL.md) | Für KIG: Risikobewertung Hochrisiko: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/kig-risikobewertung-hochrisiko-leitfaden/SKILL.md) |
| [`konformitaetsbewertung-red-team-und-qualitaetskontrolle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/konformitaetsbewertung-red-team-und-qualitaetskontrolle/SKILL.md) | Für Konformitätsbewertung: Red-Team und Qualitätskontrolle: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/konformitaetsbewertung-red-team-und-qualitaetskontrolle/SKILL.md) |
| [`mandat-arbeitsbereich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/mandat-arbeitsbereich/SKILL.md) | Für /mandat-arbeitsbereich: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/mandat-arbeitsbereich/SKILL.md) |
| [`marketing-mandantenkommunikation-entscheidungsvorlage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/marketing-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Für Marketing: Mandantenkommunikation und Entscheidungsvorlage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Mandantennachricht oder Entscheidungsvorlage. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/marketing-mandantenkommunikation-entscheidungsvorlage/SKILL.md) |
| [`monitoring-quellenkarte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/monitoring-quellenkarte/SKILL.md) | Für Monitoring Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/monitoring-quellenkarte/SKILL.md) |
| [`output-waehlen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/output-waehlen/SKILL.md) | Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/output-waehlen/SKILL.md) |
| [`quellen-livecheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/quellen-livecheck/SKILL.md) | Für Rechtsquellen-Livecheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/quellen-livecheck/SKILL.md) |
| [`rechtsquellen-sonderfall-edge-case`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rechtsquellen-sonderfall-edge-case/SKILL.md) | Für Rechtsquellen: Sonderfall und Edge-Case-Prüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rechtsquellen-sonderfall-edge-case/SKILL.md) |
| [`regulierungs-luecken-analyse`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/regulierungs-luecken-analyse/SKILL.md) | Für digitale Werkzeuge-Regulierungs-Lückenanalyse: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/regulierungs-luecken-analyse/SKILL.md) |
| [`review-richtlinie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/review-richtlinie/SKILL.md) | Für Prüfung: Internationaler Bezug und Schnittstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/review-richtlinie/SKILL.md) |
| [`review-schriftsatz-brief-und-memo-bausteine`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/review-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Für Review: Schriftsatz-, Brief- und Memo-Bausteine: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/review-schriftsatz-brief-und-memo-bausteine/SKILL.md) |
| [`richtlinie-zahlen-schwellen-und-berechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinie-zahlen-schwellen-und-berechnung/SKILL.md) | Für Richtlinie: Zahlen, Schwellenwerte und Berechnung: rechnet Beträge, Schwellen und Varianten; Ergebnis: Berechnungstabelle mit Annahmen und Kontrollfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinie-zahlen-schwellen-und-berechnung/SKILL.md) |
| [`richtlinien-monitor-vorlage-anbieter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinien-monitor-vorlage-anbieter/SKILL.md) | Für digitale Werkzeuge-Richtlinien-Monitor: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinien-monitor-vorlage-anbieter/SKILL.md) |
| [`richtlinien-vorlage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinien-vorlage/SKILL.md) | Für digitale Werkzeuge-Richtlinien-Starter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/richtlinien-vorlage/SKILL.md) |
| [`rollen-rasci-hochrisiko-anhang-incident`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rollen-rasci-hochrisiko-anhang-incident/SKILL.md) | Für digitale Werkzeuge-Governance Rollen-Modell: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rollen-rasci-hochrisiko-anhang-incident/SKILL.md) |
| [`rollenmodell-use-case-vendor`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rollenmodell-use-case-vendor/SKILL.md) | Für Rollenmodell: Formular, Portal und Einreichungslogik: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/rollenmodell-use-case-vendor/SKILL.md) |
| [`spezial-monitoring-livequellen-und-rechtsprechungscheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/spezial-monitoring-livequellen-und-rechtsprechungscheck/SKILL.md) | Für Monitoring: Livequellen- und Rechtsprechungscheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/spezial-monitoring-livequellen-und-rechtsprechungscheck/SKILL.md) |
| [`spezial-pruefung-internationaler-bezug-und-schnittstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/spezial-pruefung-internationaler-bezug-und-schnittstellen/SKILL.md) | Für Prüfung: Internationaler Bezug und Schnittstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/spezial-pruefung-internationaler-bezug-und-schnittstellen/SKILL.md) |
| [`triage-haftung-versicherung-anwendungsfall`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/triage-haftung-versicherung-anwendungsfall/SKILL.md) | Für Triage: Fristen, Form, Zuständigkeit und Rechtsweg: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/triage-haftung-versicherung-anwendungsfall/SKILL.md) |
| [`unterlagen-luecken`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/unterlagen-luecken/SKILL.md) | Für Unterlagen und Lücken: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/unterlagen-luecken/SKILL.md) |
| [`use-case-risk-classification`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/use-case-risk-classification/SKILL.md) | Für Use-Case-Risikoklassifizierung nach europäischer Technikregulierungsrahmen und DSGVO: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/use-case-risk-classification/SKILL.md) |
| [`vendor-behoerden-gericht-und-registerweg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/vendor-behoerden-gericht-und-registerweg/SKILL.md) | Für Vendor: Behörden-, Gerichts- oder Registerweg: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Einreichungsplan mit Form- und Nachweischeck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/vendor-behoerden-gericht-und-registerweg/SKILL.md) |
| [`vo-pflichtenpyramide-kig-ai-foundation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/vo-pflichtenpyramide-kig-ai-foundation/SKILL.md) | Für europäischer Technikregulierungsrahmen Pflichtenpyramide: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/vo-pflichtenpyramide-kig-ai-foundation/SKILL.md) |
| [`werbung-beweislast-und-darlegungslast`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/werbung-beweislast-und-darlegungslast/SKILL.md) | Für Werbung: Beweislast, Darlegungslast und Substantiierung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/werbung-beweislast-und-darlegungslast/SKILL.md) |
| [`workflow-anschluss-skills-router`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-anschluss-skills-router/SKILL.md) | Für Anschluss-Skills Router: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-anschluss-skills-router/SKILL.md) |
| [`workflow-chronologie-und-belegmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Für Chronologie und Belegmatrix: ordnet Akte, Belege und Lücken; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-chronologie-und-belegmatrix/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-kaltstart-und-routing/SKILL.md) |
| [`workflow-mandantenkommunikation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-mandantenkommunikation/SKILL.md) | Für Mandantenkommunikation: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Mandantennachricht oder Entscheidungsvorlage. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-mandantenkommunikation/SKILL.md) |
| [`workflow-redteam-qualitygate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-redteam-qualitygate/SKILL.md) | Für Red-Team Qualitygate: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-redteam-qualitygate/SKILL.md) |
| [`workflow-unterlagen-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-unterlagen-lueckenliste/SKILL.md) | Für Unterlagen- und Lückenliste: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: Technik-Governance. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-governance/skills/workflow-unterlagen-lueckenliste/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
