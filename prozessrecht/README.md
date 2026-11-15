# Prozessrecht-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prozessrechtliche Skills für Mandate, Fristen, Mahnbescheid, Eilverfahren, Vollstreckung und Schriftsätze.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`prozessrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/prozessrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/prozessrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/prozessrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/prozessrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/prozessrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/prozessrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Prozessrecht-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`prozessrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/prozessrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`prozessrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/prozessrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`prozessrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/prozessrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Kita Mühlenhof Lichtenrade - HOAI-Leistungsphasen und Bauüberwachung 2026](../testakten/hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026/README.md) | [Gesamt-PDF](../testakten/hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026/gesamt-pdf/hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026_gesamt.pdf) | [`testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip) | [`testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026-einzelpdfs.zip) |
| [Werkvertragsstreit Pohlmann / Saalbau Rosenheim — Baumängel, BGH-Revision, Zurückverweisung](../testakten/zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann/README.md) | [Gesamt-PDF](../testakten/zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann/gesamt-pdf/zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann_gesamt.pdf) | [`testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip) | [`testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-2-v445.35.3/testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Unterstützung für Prozessanwälte und Syndikusrechtsanwälte bei der Führung eines Mandatsportfolios im deutschen Zivil-, Straf-, Verwaltungs- und Arbeitsrecht. Der Kaltstart-Interview erfasst Risikobereitschaft, Mandatslandschaft und Kanzleistil – der Rahmen, gegen den jedes neue Mandat eingeordnet wird. Einheitliche Aufnahme (Intake) überführt neue Mandate in strukturierte Logeinträge und mandatsbezogene Historiendateien. Statusübersichten und Tiefenbriefings lesen aus dem Log.

Konzipiert für Anwälte, die viele Mandate gleichzeitig betreuen, von denen die meisten durch externe Kanzleien oder Korrespondenzanwälte bearbeitet werden. Dieses Plugin ist ein Denkpartner, kein Mandatsverwaltungssystem. Wenn Sie LawVu, SimpleLegal oder eine vergleichbare Software einsetzen, ersetzt dieses Plugin diese nicht – es ergänzt sie als strukturierte Argumentations- und Analyseschicht.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, markiert und abgesichert –, keine rechtliche Schlussfolgerung.** Das Plugin erledigt die Arbeit: liest die Dokumente, wendet Ihr Playbook an, findet die Probleme, entwirft das Memo. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu überprüfen sind. Mandatsgeheimnismarker werden konservativ angewendet, damit keine unbeabsichtigte Offenbarung erfolgt (§ 43a Abs. 2 BRAO, § 203 StGB). Folgenreiche Handlungen – Einreichen, Versenden, Vollstrecken – sind durch ausdrückliche Bestätigung abgesichert.

## Voraussetzungen

Einige Funktionen verweisen auf Outlook- und Kalender-Integrationen. Diese erfordern MCP-Server in Ihrer Umgebung – sie sind nicht im Plugin enthalten. Ohne sie werden Ausgaben als Dateien gespeichert:

- **Outlook MCP** – `/gegenseite-status` erstellt Outlook-Entwürfe, sofern authentifiziert; andernfalls Markdown-Entwürfe in `gegenseite-status/[JJJJ-MM-TT]/[slug].md`.
- **Kalender-MCP** – keine automatische Terminplanung enthalten. Richten Sie eine Wiederholungserinnerung ein, um wöchentliche Befehle aufzurufen.

Das Plugin funktioniert vollständig ohne beide Integrationen; diese sind additiv.

## Für wen ist das?

| Rolle | Hauptverwendung |
|---|---|
| **Prozessanwalt (Kanzlei oder Syndikus)** | Alles – Intake, Triage, Status, Historie, Briefings |
| **Stellvertretender Justiziar / leitender Syndikus** | Portfolio-Übersicht, Vorstandsberichterstattung |
| **Hauptjustiziar / Leiter Rechtsabteilung** | Schneller Portfoliostatus, Tiefeneinblick in einzelne Mandate |
| **Außenanwalt** | Per-Mandat-Verlaufsdokumentation, Schriftsatzentwürfe, Fristen |

## Anwendungsbereich

Das Plugin deckt das **deutsche Zivilprozessrecht (ZPO)** als Kernbereich ab und enthält spezialisierte Skills für:

- **Strafrecht / Strafverteidigung** – StPO, Pflichtverteidigung, Akteneinsicht
- **Digitale StPO-Ermittlungsmaßnahmen** – biometrischer Internetabgleich, KI-Analyseplattformen, Akteneinsicht, Benachrichtigung, Löschung und Verwertungsangriffe
- **Verwaltungsrecht** – VwGO, Widerspruchsverfahren
- **Arbeitsrecht** – ArbGG, einstweiliger Rechtsschutz
- **Familienrecht** – FamFG
- **Steuerrecht** – FGO, BFH
- **Sozialrecht** – SGG, BSG
- **Zwangsvollstreckung** – §§ 704 ff. ZPO
- **Einstweilige Verfügung** – §§ 935, 940 ZPO
- **Mahnverfahren** – §§ 688 ff. ZPO
- **Verkehrsunfallrecht** – StVG, § 115 VVG

Für harte ZPO-Fakten gibt es den Spezialskill `amtlicher-zpo-verfahrenscheck`. Er nutzt den aktuellen amtlichen ZPO-Normkern und trennt Zuständigkeit, Form, Zustellung, Fristen, Klage, Beweis, Mahnverfahren, Vollstreckung, Arrest und einstweilige Verfügung.

## Informationsbeschaffung und Beweissicherung

Vor einer Klage kommen je nach Rechtsverhältnis materielle Einsichts- und Auskunftsansprüche in Betracht, etwa nach Paragraf 810 BGB, aus Paragraf 242 BGB oder nach Paragraf 666 BGB. Paragrafen 259 und 260 BGB regeln den Umfang bestimmter Rechenschafts- und Auskunftspflichten, begründen aber keinen allgemeinen Ausforschungsanspruch. Art. 15 DSGVO betrifft personenbezogene Daten, nicht unterschiedslos sämtliche Prozessunterlagen.

Das selbständige Beweisverfahren nach Paragrafen 485 ff. ZPO kann unter seinen gesetzlichen Voraussetzungen bereits vor einem Hauptsacheverfahren der Beweissicherung oder Streitvermeidung dienen. Davon zu unterscheiden sind gerichtliche Anordnungen nach Paragrafen 142 und 144 ZPO zur Urkundenvorlage, zum Augenschein oder zur Begutachtung im Verfahren. Die Stufenklage nach Paragraf 254 ZPO ist eine Klageform zur Verbindung eines Auskunfts- oder Rechnungslegungsbegehrens mit dem noch zu beziffernden Leistungsbegehren, keine vorgerichtliche Ermittlungsbefugnis.

Zum Schutz anwaltlicher Unterlagen: § 43a Abs. 2 BRAO, § 203 StGB; Zeugnisverweigerungsrecht § 383 Abs. 1 Nr. 6 ZPO; Beschlagnahmefreiheit §§ 97, 53 StPO; Editionsverweigerung §§ 142, 383 ZPO.

Gerichtsentscheidungen begründen grundsätzlich keine allgemeine Präzedenzbindung für jeden späteren Fall. Davon zu trennen sind die materielle Rechtskraft nach Paragraf 322 ZPO, gesetzliche Bindungen im konkreten Verfahren und die besondere Bindungswirkung nach Paragraf 31 BVerfGG. Einschlägige Rechtsprechung ist mit tragendem Rechtssatz, Sachverhaltsvergleich und Übertragungsgrenze auszuwerten; Literatur und Kommentare ergänzen diese Prüfung.

## Rechtsgebiete und Verfahrensordnungen

| Verfahren | Rechtsgrundlage |
|---|---|
| Zivilprozess | ZPO, GVG, RVG, GKG |
| Strafprozess | StPO, GVG, RVG |
| Verwaltungsstreit | VwGO, VwVfG |
| Finanzgerichtsbarkeit | FGO, AO |
| Sozialgerichtsbarkeit | SGG, SGB |
| Arbeitsgerichtsbarkeit | ArbGG, KSchG |
| Familiensachen | FamFG, BGB |
| Zwangsvollstreckung | §§ 704–915h ZPO |

## Dateistruktur

```
prozessrecht/
├── CLAUDE.md              # Praxisprofil (vom Kaltstart geschrieben)
├── README.md              # Diese Datei
├── mandate/               # Pro-Mandat-Ordner: mandat.md + verlauf.md
│   └── _log.yaml          # Portfolio-Log aller Mandate
├── demand-letters/        # Ausgehende Schreiben und Entwürfe
├── inbound/               # Eingegangene Schreiben, Mahnungen, Beschlüsse
├── gegenseite-status/             # Korrespondenz mit Gegenseite / Außenanwälten
└── skills/                # Plugin-Skills (automatisch geladen)
```

## Nutzungshinweis

Alle Ausgaben des Plugins sind **Entwürfe zur anwaltlichen Prüfung**. Das Plugin ersetzt keine Rechtsberatung und trifft keine Entscheidungen. Berufsrechtliche Pflichten nach BRAO, BORA, RVG und die anwaltliche Verschwiegenheit nach § 43a Abs. 2 BRAO bleiben unberührt. Für die Überprüfung und Freigabe jedes Dokuments ist stets der verantwortliche Anwalt zuständig.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **65 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Prozessroute | [`prozessroute-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/prozessroute-bearbeiten/SKILL.md) |
| 3. Antrag und Streitgegenstand | [`antrag-und-streitgegenstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/antrag-und-streitgegenstand-bearbeiten/SKILL.md) |
| 4. Beweis | [`beweis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/beweis-bearbeiten/SKILL.md) |
| 5. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 6. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 7. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`antrag-und-streitgegenstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/antrag-und-streitgegenstand-bearbeiten/SKILL.md) | Zivilprozessuale Mandatsbearbeitung: Antrag und Streitgegenstand: Klageziel, Lebenssachverhalt, Haupt- und Hilfsanträge, Nebenforderungen und Erledigung trennen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/antrag-und-streitgegenstand-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Zivilprozessuale Mandatsbearbeitung: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Zivilprozessuale Mandatsbearbeitung: Arbeitsprodukt: Klageschrift, Klageerwiderung, Hinweisverfügung, Beschluss, Urteil, Tenor, Anlagenverzeichnis oder Fristenblatt erstellen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`beweis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/beweis-bearbeiten/SKILL.md) | Zivilprozessuale Mandatsbearbeitung: Beweis: Beweisthema, Beweismittel, Substantiierung, Beweislast, Beweiswürdigung und Beweisbeschluss aus der Akte entwickeln. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/beweis-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Prozessrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/einstieg-routing/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Prozessrecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`prozessroute-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/prozessroute-bearbeiten/SKILL.md) | Zivilprozessuale Mandatsbearbeitung: Prozessroute: Gericht, Rechtsweg, Zuständigkeit, Streitwert, Frist, Einreichungsweg und Verfahrensstand sichern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/prozessroute-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Zivilprozessuale Mandatsbearbeitung: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Prozessrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=prozessrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Unterscheiden Sie private Schriftsatzhilfe von einem im Auftrag der Justiz eingesetzten entscheidungsunterstützenden System. Die Bezeichnung Recherchehilfe beweist nicht, dass tatsächlicher Entscheidungseinfluss fehlt.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
