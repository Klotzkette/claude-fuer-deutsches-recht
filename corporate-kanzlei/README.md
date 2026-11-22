# Corporate-Kanzlei-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`corporate-kanzlei.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/corporate-kanzlei.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/corporate-kanzlei.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/corporate-kanzlei-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/corporate-kanzlei-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/corporate-kanzlei.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/corporate-kanzlei.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Corporate-Kanzlei-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`corporate-kanzlei.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/corporate-kanzlei.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`corporate-kanzlei-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/corporate-kanzlei-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`corporate-kanzlei-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/corporate-kanzlei-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Insolvenz-Asset-Deal — ChainCortex AI GmbH (Berlin) → Voracis Ventures GmbH](../testakten/insolvenz-asset-deal-chaincortex-ai-berlin/README.md) | [Gesamt-PDF](../testakten/insolvenz-asset-deal-chaincortex-ai-berlin/gesamt-pdf/insolvenz-asset-deal-chaincortex-ai-berlin_gesamt.pdf) | [`testakte-insolvenz-asset-deal-chaincortex-ai-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-insolvenz-asset-deal-chaincortex-ai-berlin.zip) | [`testakte-insolvenz-asset-deal-chaincortex-ai-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-insolvenz-asset-deal-chaincortex-ai-berlin-einzelpdfs.zip) |
| [M&A Asset Deal MedTech — VENERA/FraktoMedis Präzision (Darmstadt)](../testakten/ma-asset-deal-medtech-volkenrath-darmstadt/README.md) | [Gesamt-PDF](../testakten/ma-asset-deal-medtech-volkenrath-darmstadt/gesamt-pdf/ma-asset-deal-medtech-volkenrath-darmstadt_gesamt.pdf) | [`testakte-ma-asset-deal-medtech-volkenrath-darmstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ma-asset-deal-medtech-volkenrath-darmstadt.zip) | [`testakte-ma-asset-deal-medtech-volkenrath-darmstadt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ma-asset-deal-medtech-volkenrath-darmstadt-einzelpdfs.zip) |
| [Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/README.md) | [Gesamt-PDF](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-private-equity-buyout-schuldschein-npl-heidelberg-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein Corporate-Mandat steuern: Beschlüsse, Organmaßnahmen, Register, Kapitalmaßnahmen, Beteiligungen, Gesellschafterkonflikte, Transaktion oder Governance-Entscheidung.
Technischer Plugin-Name: `corporate-kanzlei`.

Eigenständiges Corporate-Kanzlei-Plugin für große Corporate- und M&A-Mandate: Origination, Outside-in-Assessment, Datenraum, Due Diligence, Tabellenreview, Q&A, SPA/APA, Disclosure Schedules, Knowledge/Fair Disclosure, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing und Closing Bible.

Es ist als leistungsstarker Arbeitsrahmen für erfahrene Transaktionsteams gedacht, bleibt aber freundlich genug, um jüngere Anwender Schritt für Schritt durch große Deal-Workflows zu führen.

## Installation

1. ZIP herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize → Plugins** bzw. **Personal plugins** öffnen.
4. **Upload plugin** wählen und `corporate-kanzlei.zip` hochladen.
5. Mit einem konkreten Deal-Auftrag starten, zum Beispiel: `Starte das Corporate-M&A-Kommandocenter für diesen Datenraum.`

Wichtig: Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und optional `references/` enthalten.

## Skill-Landkarte

| Skill | Bereich | Zweck |
| --- | --- | --- |
| corporate-kanzlei-kommandocenter | Deal-Kommandocenter | Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt eine D... |
| corporate-kanzlei-look-and-feel | Corporate-Cowork-Look | Definiert die sichtbare Oberfläche: sehr ruhig, edel, bläulich-silbern mit warmem Orange für Entscheidungspunkte, dichte Deal-Information stat... |
| corporate-kanzlei-kaltstart | Deal-Kaltstart | Nimmt Kanzlei- und Mandantenpräferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sich... |
| corporate-kanzlei-freundlicher-copilot | Freundlicher Deal-Copilot | Führt junge Anwender verzeihend durch große Transaktionen, erkennt unausgesprochene Absichten und meldet sich kurz mit hilfreichen Hinweisen. |
| corporate-kanzlei-deal-intake | Deal-Intake | Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung. |
| corporate-kanzlei-matter-file | Deal-Akte | Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI. |
| corporate-kanzlei-conflict-gwg-sanctions | Konflikt-, GwG- und Sanktionscheck | Führt Annahmeprüfung für Corporate/M&A: Interessenkonflikte, wirtschaftlich Berechtigte, Sanktionen, PEP, Mittelherkunft, Sektor- und Länder-... |
| corporate-kanzlei-deal-team-staffing | Deal-Team und Staffing | Plant Workstreams, Rollen, Kapazitäten, Review-Level und Eskalationswege für große Transaktionen. |
| corporate-kanzlei-outside-in-target-screening | Outside-in Target Screening | Erstellt frühe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen. |
| corporate-kanzlei-teaser-im-processdocs | Teaser, IM und Prozessdokumente | Unterstützt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation. |
| corporate-kanzlei-datenraum-aufbau | Datenraum-Aufbau | Strukturiert und bestückt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. |
| corporate-kanzlei-datenraum-gap-clean-room | Datenraum-Gap-Analyse und Clean Room | Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Lücken, Widersprüche, Dubletten und Clean-Room-Bedarf. |
| corporate-kanzlei-due-diligence-legal | Legal Due Diligence | Führt standardisierte Legal Due Diligence mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report. |
| corporate-kanzlei-due-diligence-commercial-contracts | Kommerzielle Vertrags-DD | Prüft Kunden-, Lieferanten-, Händler-, SaaS-, Lizenz- und Materialverträge auf Change of Control, Kündigung, Exklusivität, Haftung, IP und P... |
| corporate-kanzlei-tabellenreview-3d-datenraum | 3D-Tabellenreview im Datenraum | Verbindet M&A-Datenraumprüfung mit dem Tabellenreview-3D-Ansatz: Dokumente x Datenpunkte x Perspektiven Recht/Steuer/Wirtschaft. |
| corporate-kanzlei-qa-information-requests | Q&A und Information Requests | Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität. |
| corporate-kanzlei-expert-calls-transkripte | Expert Calls und Transkripte | Bereitet Management Presentations, Expert Calls und Transkripte für DD und SPA-Verhandlung auf. |
| corporate-kanzlei-transaktionsstruktur | Transaktionsstrukturierung | Entwickelt Strukturvarianten für Share Deal, Asset Deal, Carve-out, Joint Venture, Verschmelzung, Spaltung, Formwechsel, Roll-over und Managemen... |
| corporate-kanzlei-umwandlungsrecht | Umwandlungsrecht | Bearbeitet Verschmelzung, Spaltung, Ausgliederung, Formwechsel, Einbringung und Vorfeld-Carve-outs nach Umwandlungsrecht. |
| corporate-kanzlei-umwandlungssteuerrecht | Umwandlungssteuerrecht | Erfasst umwandlungssteuerliche Strukturfragen als Arbeitsmatrix für Steuerteam und Corporate-Team. |
| corporate-kanzlei-kg-personengesellschaften | KG und Personengesellschaften | Spezialworkflow für KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register. |
| corporate-kanzlei-gesellschaftsrecht-register | Corporate Housekeeping und Register | Prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschlüsse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals. |
| corporate-kanzlei-spa-apa-entwurf | SPA/APA-Entwurf | Erstellt und strukturiert Kaufvertragsentwürfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur. |
| corporate-kanzlei-vertragsmarkup-key-issues | Markup und Key Issues | Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive. |
| corporate-kanzlei-disclosure-schedules | Disclosure Schedules | Leitet Disclosure Schedules aus Datenraum, DD-Findings, Q&A und SPA-Garantien ab. |
| corporate-kanzlei-fair-disclosure-knowledge | Fair Disclosure und Knowledge | Prüft Wissens-, Kenntnis-, Fair-Disclosure- und Aktenwissen-Klauseln im Lichte von KI-gestützter Datenraumprüfung. |
| corporate-kanzlei-signing-closing-conditions | Signing, Closing und CPs | Führt Signing-to-Closing: Conditions Precedent, Ordinary Course, Bring-down, Closing Deliverables, Funds Flow und Closing Bible. |
| corporate-kanzlei-regulatory-fdi-merger-control | Fusionskontrolle und Investitionskontrolle | Erstellt Freigabe-Landkarte für Kartellrecht, Fusionskontrolle, AWV/FDI, Sektorregulierung und Multi-Jurisdiction-Filings. |
| corporate-kanzlei-public-ma-kapitalmarkt-mar | Public M&A, Kapitalmarkt und MAR | Begleitet börsennotierte Transaktionen: WpÜG-Unterlagen, Ad-hoc-Prüfung, Insiderlisten, Stellungnahmen und Marktgerüchte. |
| corporate-kanzlei-wi-insurance | W&I-Versicherung | Bereitet W&I-Prozess, Underwriting, DD-Berichte, KI-DD-Transparenz und Deckungsausschlüsse vor. |
| corporate-kanzlei-restructuring-starug-insolvenzplan | StaRUG und Insolvenzplan | Unterstützt Restrukturierungsfälle: StaRUG-Plan, Insolvenzplan, Distressed M&A, Gläubigerklassen, Planbetroffenheit und Zeitplan. |
| corporate-kanzlei-distressed-ma | Distressed M&A | Führt Unternehmenskauf in Krise, vorläufiger Insolvenz, Insolvenzplan oder Asset Deal aus der Insolvenz. |
| corporate-kanzlei-post-closing-integration | Post-Closing Integration | Übersetzt DD-Findings, SPA-Pflichten und Synergieannahmen in einen PMI-Plan. |
| corporate-kanzlei-steps-plan-pmo | Deal-PMO und Steps Plan | Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing. |
| corporate-kanzlei-rechtsprechungsrecherche | Corporate-Rechtsprechungsrecherche | Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. |
| corporate-kanzlei-handelsregisterabruf | Handelsregister- und Registerabruf | Führt offizielle Registerabrufe für Zielgesellschaft, Verkäufer, Erwerber, Beteiligungsketten, KG und Organstellung. |
| corporate-kanzlei-datenqualität-xai-qualitätskontrolle | Datenqualität und XAI-Qualitätskontrolle | Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab. |
| corporate-kanzlei-ki-governance-berufsrecht | KI-Governance und Berufsrecht | Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe. |
| corporate-kanzlei-board-paper-business-judgment | Board Paper und Business Judgment | Erstellt Entscheidungsunterlagen für Vorstand/Geschäftsführung/Aufsichtsrat mit Informationsgrundlage, Alternativen, Risiken und KI-Einsatztra... |
| corporate-kanzlei-billing-narratives | Corporate Billing Narratives | Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. |
| corporate-kanzlei-output-versand-signing | Output, Signing und Versand | Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand. |
| corporate-kanzlei-due-diligence-reporting | DD Reporting und Legal Fact Book | Erstellt Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary und Issues-to-SPA-Mapping. |
| corporate-kanzlei-simulation-bidder-process | Bieterprozess-Simulation | Simuliert einen beschleunigten achtstündigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call. |
| corporate-kanzlei-automation-monitoring | Automationen und Monitoring | Entwirft Monitore für Datenraum-Neuzugänge, Q&A, CP-Deadlines, Registerupdates, News, MAR-Signale und PMI-Aufgaben. |
| corporate-kanzlei-closing-bible-archiv | Closing Bible und Archiv | Erstellt Closing Bible, Versionierung, Signaturketten, Registerbelege und Deal-Archiv. |
| corporate-kanzlei-translations-multijurisdictional | Multi-Jurisdiction und Übersetzungen | Koordiniert lokale Kanzleien, Übersetzungen, Rechtsvergleich und Multi-Jurisdiction-Matrizen. |

## Typische Workflows

- Buy-side: Target Screening -> NDA -> Datenraum -> Legal DD -> Q&A -> SPA-Markup -> Signing/Closing -> PMI.
- Sell-side: Teaser/IM -> Datenraumaufbau -> Vendor DD/Fact Book -> Bieter-Q&A -> Disclosure Schedules -> Vertragsverhandlung.
- Public M&A: Insider-/MAR-Prüfung -> Angebotsunterlage/Stellungnahme -> Kapitalmarktkommunikation -> Closing-Auflagen.
- Restrukturierung: StaRUG/Insolvenzplan -> Distressed M&A -> Planvergleich -> Stakeholder- und Gerichtsschritte.
- Corporate Reorganisation: Umwandlung -> Umwandlungssteuerrecht -> Register/Notar -> Carve-out -> Closing.

## Sicherheitsleitplanken

- Keine echte Transaktionsberatung ohne menschliche Letztprüfung.
- Keine Mandatsgeheimnisse, Insiderinformationen, Datenraumzugangsdaten oder Clean-Room-Daten in nicht freigegebene Systeme.
- KI-DD immer als `KI-gestuetzt`, `stichprobenvalidiert` oder `voll menschlich validiert` kennzeichnen.
- Register-, Rechtsprechungs-, Gesetzes- und Datenraumbelege müssen verifizierbar sein.
- Public M&A, MAR, WpÜG, Kartellrecht, Investitionskontrolle, Sanktionen, StaRUG und Insolvenzreife sind rote Schwellen.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **11 auswählbare Skills**. Die **88 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/juristischer-argumentationskern/SKILL.md), [`kommandocenter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/kommandocenter/SKILL.md) |
| 2. Transaktion und Struktur | [`transaktion-und-struktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/transaktion-und-struktur-bearbeiten/SKILL.md) |
| 3. Due Diligence und Risikoprüfung | [`due-diligence-und-risikopruefung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/due-diligence-und-risikopruefung-bearbeiten/SKILL.md) |
| 4. Kaufvertrag und Preis | [`kaufvertrag-und-preis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/kaufvertrag-und-preis-bearbeiten/SKILL.md) |
| 5. Finanzierung und Beteiligung | [`finanzierung-und-beteiligung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/finanzierung-und-beteiligung-bearbeiten/SKILL.md) |
| 6. Governance und Gesellschafter | [`governance-und-gesellschafter-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/governance-und-gesellschafter-bearbeiten/SKILL.md) |
| 7. Signing und Vollzug | [`signing-und-vollzug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/signing-und-vollzug-bearbeiten/SKILL.md) |
| 8. Krise und Streit | [`krise-und-streit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/krise-und-streit-bearbeiten/SKILL.md) |
| 9. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 10. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`due-diligence-und-risikopruefung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/due-diligence-und-risikopruefung-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Due Diligence und Risikoprüfung: Datenraum, Verträge, Personal, IP, IT, Compliance und erkennbare Risiken belegen und für die Transaktion bewerten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/due-diligence-und-risikopruefung-bearbeiten/SKILL.md) |
| [`finanzierung-und-beteiligung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/finanzierung-und-beteiligung-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Finanzierung und Beteiligung: Equity, Darlehen, Wandlung, Sicherheiten, Gesellschafterdarlehen und Kapitalmaßnahmen anhand der Vertragsunterlagen gestalten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/finanzierung-und-beteiligung-bearbeiten/SKILL.md) |
| [`governance-und-gesellschafter-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/governance-und-gesellschafter-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Governance und Gesellschafter: Beteiligungsrechte, Organe, Beirat, Management, Vergütung und Exit im Gesellschaftsvertrag abstimmen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/governance-und-gesellschafter-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Corporate Kanzlei ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaufvertrag-und-preis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/kaufvertrag-und-preis-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Kaufvertrag und Preis: Kaufgegenstand, Kaufpreis, Garantien, Freistellungen, Haftung und Anpassungsmechanik ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/kaufvertrag-und-preis-bearbeiten/SKILL.md) |
| [`kommandocenter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/kommandocenter/SKILL.md) | Corporate- und M&A-Mandat bis zum konkreten Deal-Dokument führen. Wertet vorhandene Unterlagen aus, entscheidet die fachlichen Weichen und liefert vollständigen SPA-/APA-Abschnitt, Beschluss, Board Paper oder Closing-Vermerk samt belegte... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/kommandocenter/SKILL.md) |
| [`krise-und-streit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/krise-und-streit-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Krise und Streit: Sanierung, Insolvenz, Sanierungsgewinn, Organhaftung und Transaktionsstreit mit dem richtigen Anspruchsinhaber prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/krise-und-streit-bearbeiten/SKILL.md) |
| [`signing-und-vollzug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/signing-und-vollzug-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Signing und Vollzug: Bedingungen, Unterschriften, Notar, Register, Closing, Übertragung und Integration bis zur dokumentierten Umsetzung führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/signing-und-vollzug-bearbeiten/SKILL.md) |
| [`transaktion-und-struktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/transaktion-und-struktur-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Transaktion und Struktur: Share Deal, Asset Deal, Beteiligte, Erwerbsstruktur und maßgebliche Rechtsordnung festlegen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/transaktion-und-struktur-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Kanzleipraxis: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=corporate-kanzlei/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Verlangen Sie für ein KI-Zielunternehmen die konkrete Systemliste samt Version, Zweck, Rolle und tatsächlichen Konformitätsbelegen. Ein Zertifikat der Muttergesellschaft rechtfertigt keine Garantie für sämtliche Produkte der Tochter.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
