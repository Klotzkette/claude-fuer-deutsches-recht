# Big-Law-Großkanzlei-Corporate/M&A-Plugin


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Akte LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH** (`sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`) | [Gesamt-PDF lesen](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/gesamt-pdf/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Technischer Plugin-Name: `grosskanzlei-corporate-ma`.

Dies ist das freistehende Großkanzlei-Corporate/M&A-Plugin für den gesamten Transaktionslebenszyklus: Intake, Aktenanlage, Konflikt-/GwG-/Sanktionscheck, Datenraum, Due Diligence, Tabellenreview, Liquiditätsvorschau, Insolvenzreife, Q&A, SPA/APA, Disclosure Schedules, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing, XRechnung/ZUGFeRD-Vorbereitung, GoBD-Protokoll und Closing Bible.

Für neue Nutzerinnen und Nutzer gibt es zusätzlich einen **Anfänger-/First-Year-Associate-Modus**: Das Plugin fragt bei Bedarf am Anfang, wie viel Führung gewünscht ist, erklärt Deal-Begriffe nur dort, wo sie gebraucht werden, zerlegt Aufgaben in kleine Schritte und setzt Senior-Review-Gates, bevor etwas an Mandanten, Gegenseite, Notar, Bank oder Behörde geht.

**Wichtig:** Dieses Plugin funktioniert vollständig allein. Alle Kernabläufe, Hilfstabellen, Prüfungsschablonen und Workflows liegen im Plugin selbst; für die hier beschriebenen M&A-Workflows ist keine Zusatzinstallation nötig.


## ⬇️ Zum Ausprobieren: Arbeitsakten (separat)

Mandatsakten zum sofortigen Ausprobieren — **kein Teil des Plugins**, separater Download:

| Akte | Direkt-Download |
| --- | --- |
| **sachverstaendigengutachten ki vorwurf lg regensburg sieglinger** | [testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |
| **gesellschaftsrecht legal english frankfurt startup** | [testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Großkanzlei Corporate/M&A (`grosskanzlei-corporate-ma`) | [grosskanzlei-corporate-ma.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grosskanzlei-corporate-ma.zip) |

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `grosskanzlei-corporate-ma.zip` hochladen.
5. Mit einem konkreten Deal-Auftrag starten, zum Beispiel: `Starte das Corporate-M&A-Kommandocenter für diesen Datenraum.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

### Zum Ausprobieren: Arbeitsakten (separat)

Mandatsakten zum sofortigen Ausprobieren — **kein Teil des Plugins**, separater Download:

| Akte | Direkt-Download |
| --- | --- |
| **Grosskanzlei Corporate M&A Datenraum** | [testakte-grosskanzlei-corporate-ma-datenraum.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grosskanzlei-corporate-ma-datenraum.zip) |
| **Gesellschaftsrecht Legal English Frankfurt Startup** | [testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |


## Freistehende Kernmodule

| Modul | Enthaltene Funktion |
| --- | --- |
| Anfänger-Modus | Geführter First-Year-Associate-Workflow mit Level-Abfrage, Begriffserklärungen, Kleinschritten und Senior-Review-Gates. |
| Aktenanlage | Deal-Akte, Aktenzeichen, Parteienregister, Ordnerplan, Datenraumspiegel, Closing-Bible-Grundgerüst. |
| Tabellenreview | Interner Review-Würfel für Dokumente, Datenpunkte, Tabellen, Formeln und Perspektiven. |
| Liquiditätsvorschau | 3-Wochen-Prüfung, 13-Wochen-Cash-Bridge, Runway, OPOS, Bankdaten, Distressed-M&A-Ampel. |
| Insolvenzreife | § 17, § 18, § 19 InsO, § 15a InsO, StaRUG-Frühwarnung, Deal-Auswirkungen und Senior-Review-Gate. |
| Fristen/CP | Signing, Closing, Q&A, Regulatory, Register, Board, Ordinary Course, Long Stop Date und PMI. |
| Billing/E-Rechnung | Narratives, Workstream-Rechnung, GoBD-Protokoll, XRechnung-Datenblock, ZUGFeRD-Prüfpaket. |
| Schreibcanvas | Freundlicher Qualitätsbegleiter für SPA, DD-Report, Board Paper, Registertext und Mandatskommunikation. |

## Skill-Landkarte

| Skill | Zweck |
| --- | --- |
| `grosskanzlei-corporate-ma-anfaenger-modus` | Anfänger- und First-Year-Associate-Modus: fragt Erfahrungslevel, Deal-Phase, Aufgabe, Frist und gewünschte Führung ab; erklärt Begriffe, zerlegt Aufgaben in kleine Schritte, routet zu Spezialskills und setzt Senior-Review-Gates. |
| `grosskanzlei-corporate-ma-automation-monitoring` | Automationen und Monitoring: Entwirft Monitore für Datenraum-Neuzugänge, Q&A, CP-Deadlines, Registerupdates, News, MAR-Signale und PMI-Aufgaben. |
| `grosskanzlei-corporate-ma-billing-narratives` | Big-Law Billing Narratives: erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. |
| `grosskanzlei-corporate-ma-board-paper-business-judgment` | Board Paper und Business Judgment: Erstellt Entscheidungsunterlagen für Vorstand/Geschäftsführung/Aufsichtsrat mit Informationsgrundlage, Alternativen, Risiken und KI-Einsatztransparenz. |
| `grosskanzlei-corporate-ma-closing-bible-archiv` | Closing Bible und Archiv: Erstellt Closing Bible, Versionierung, Signaturketten, Registerbelege und Deal-Archiv. |
| `grosskanzlei-corporate-ma-conflict-gwg-sanctions` | Konflikt-, GwG- und Sanktionscheck: Führt Annahmeprüfung für Corporate/M&A: Interessenkonflikte, wirtschaftlich Berechtigte, Sanktionen, PEP, Mittelherkunft, Sektor- und Länder-Risiken. |
| `grosskanzlei-corporate-ma-datenqualitaet-xai-qualitaetskontrolle` | Datenqualität und XAI-Qualitätskontrolle: Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab. |
| `grosskanzlei-corporate-ma-datenraum-aufbau` | Datenraum-Aufbau: Strukturiert und bestückt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. |
| `grosskanzlei-corporate-ma-datenraum-gap-clean-room` | Datenraum-Gap-Analyse und Clean Room: Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Lücken, Widersprüche, Dubletten und Clean-Room-Bedarf. |
| `grosskanzlei-corporate-ma-deal-intake` | Deal-Intake: Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung. |
| `grosskanzlei-corporate-ma-deal-team-staffing` | Deal-Team und Staffing: Plant Workstreams, Rollen, Kapazitäten, Review-Level und Eskalationswege für große Transaktionen. |
| `grosskanzlei-corporate-ma-disclosure-schedules` | Disclosure Schedules: Leitet Disclosure Schedules aus Datenraum, DD-Findings, Q&A und SPA-Garantien ab. |
| `grosskanzlei-corporate-ma-distressed-ma` | Distressed M&A: führt Unternehmenskauf in Krise, vorläufiger Insolvenz, StaRUG, Insolvenzplan oder Asset Deal aus der Insolvenz mit Liquiditäts- und Closing-Fokus. |
| `grosskanzlei-corporate-ma-due-diligence-commercial-contracts` | Kommerzielle Vertrags-DD: Prüft Kunden-, Lieferanten-, Händler-, SaaS-, Lizenz- und Materialverträge auf Change of Control, Kündigung, Exklusivität, Haftung, IP und Preisrisiken. |
| `grosskanzlei-corporate-ma-due-diligence-legal` | Legal Due Diligence: Führt standardisierte Legal Due Diligence mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report. |
| `grosskanzlei-corporate-ma-due-diligence-reporting` | DD Reporting und Legal Fact Book: Erstellt Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary und Issues-to-SPA-Mapping. |
| `grosskanzlei-corporate-ma-expert-calls-transkripte` | Expert Calls und Transkripte: Bereitet Management Presentations, Expert Calls und Transkripte für DD und SPA-Verhandlung auf. |
| `grosskanzlei-corporate-ma-fair-disclosure-knowledge` | Fair Disclosure und Knowledge: Prüft Wissens-, Kenntnis-, Fair-Disclosure- und Aktenwissen-Klauseln im Lichte von KI-gestützter Datenraumprüfung. |
| `grosskanzlei-corporate-ma-freundlicher-copilot` | Freundlicher Deal-Copilot: Führt junge Anwender verzeihend durch große Transaktionen, erkennt unausgesprochene Absichten und meldet sich kurz mit hilfreichen Hinweisen. |
| `grosskanzlei-corporate-ma-gesellschaftsrecht-register` | Corporate Housekeeping und Register: Prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschlüsse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals. |
| `grosskanzlei-corporate-ma-handelsregisterabruf` | Handelsregister- und Registerabruf: Führt offizielle Registerabrufe für Zielgesellschaft, Verkäufer, Erwerber, Beteiligungsketten, KG und Organstellung. |
| `grosskanzlei-corporate-ma-kaltstart` | Deal-Kaltstart: Nimmt Kanzlei- und Mandantenpräferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln. |
| `grosskanzlei-corporate-ma-kg-personengesellschaften` | KG und Personengesellschaften: Spezialworkflow für KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register. |
| `grosskanzlei-corporate-ma-ki-governance-berufsrecht` | KI-Governance und Berufsrecht: Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe. |
| `grosskanzlei-corporate-ma-kommandocenter` | Deal-Kommandocenter: Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt Deal-Karte, Ampel, Rollen und nächste Aktion. |
| `grosskanzlei-corporate-ma-look-and-feel` | Corporate-Cowork-Look: Definiert die sichtbare Oberfläche: sehr ruhig, edel, bläulich-silbern mit warmem Orange für Entscheidungspunkte, dichte Deal-Information statt Marketing. |
| `grosskanzlei-corporate-ma-matter-file` | Deal-Akte: Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI. |
| `grosskanzlei-corporate-ma-output-versand-signing` | Output, Signing und Versand: Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand. |
| `grosskanzlei-corporate-ma-outside-in-target-screening` | Outside-in Target Screening: Erstellt frühe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen. |
| `grosskanzlei-corporate-ma-post-closing-integration` | Post-Closing Integration: Übersetzt DD-Findings, SPA-Pflichten und Synergieannahmen in einen PMI-Plan. |
| `grosskanzlei-corporate-ma-public-ma-kapitalmarkt-mar` | Public M&A, Kapitalmarkt und MAR: Begleitet börsennotierte Transaktionen: WpUEG-Unterlagen, Ad-hoc-Prüfung, Insiderlisten, Stellungnahmen und Marktgerüchte. |
| `grosskanzlei-corporate-ma-qa-information-requests` | Q&A und Information Requests: Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität. |
| `grosskanzlei-corporate-ma-rechtsprechungsrecherche` | Corporate-Rechtsprechungsrecherche: Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. |
| `grosskanzlei-corporate-ma-regulatory-fdi-merger-control` | Fusionskontrolle und Investitionskontrolle: Erstellt Freigabe-Landkarte für Kartellrecht, Fusionskontrolle, AWV/FDI, Sektorregulierung und Multi-Jurisdiction-Filings. |
| `grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan` | StaRUG und Insolvenzplan: unterstützt Restrukturierungsfälle mit Planoptionen, Gläubigerklassen, Liquiditätsprüfung, Antragspflichten, Distressed M&A und Zeitplan. |
| `grosskanzlei-corporate-ma-signing-closing-conditions` | Signing, Closing und CPs: Führt Signing-to-Closing: Conditions Precedent, Ordinary Course, Bring-down, Closing Deliverables, Funds Flow und Closing Bible. |
| `grosskanzlei-corporate-ma-simulation-bidder-process` | Bieterprozess-Simulation: Simuliert einen beschleunigten achtstündigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call. |
| `grosskanzlei-corporate-ma-spa-apa-entwurf` | SPA/APA-Entwurf: Erstellt und strukturiert Kaufvertragsentwürfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur. |
| `grosskanzlei-corporate-ma-steps-plan-pmo` | Deal-PMO und Steps Plan: Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing. |
| `grosskanzlei-corporate-ma-tabellenreview-3d-datenraum` | 3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft. |
| `grosskanzlei-corporate-ma-teaser-im-processdocs` | Teaser, IM und Prozessdokumente: Unterstützt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation. |
| `grosskanzlei-corporate-ma-transaktionsstruktur` | Transaktionsstrukturierung: Entwickelt Strukturvarianten für Share Deal, Asset Deal, Carve-out, Joint Venture, Verschmelzung, Spaltung, Formwechsel, Roll-over und Managementbeteiligung. |
| `grosskanzlei-corporate-ma-translations-multijurisdictional` | Multi-Jurisdiction und Übersetzungen: Koordiniert lokale Kanzleien, Übersetzungen, Rechtsvergleich und Multi-Jurisdiction-Matrizen. |
| `grosskanzlei-corporate-ma-umwandlungsrecht` | Umwandlungsrecht: Bearbeitet Verschmelzung, Spaltung, Ausgliederung, Formwechsel, Einbringung und Vorfeld-Carve-outs nach Umwandlungsrecht. |
| `grosskanzlei-corporate-ma-umwandlungssteuerrecht` | Umwandlungssteuerrecht: Erfasst umwandlungssteuerliche Strukturfragen als Arbeitsmatrix für Steuerteam und Corporate-Team. |
| `grosskanzlei-corporate-ma-vertragsmarkup-key-issues` | Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive. |
| `grosskanzlei-corporate-ma-wi-insurance` | W&I-Versicherung: Bereitet W&I-Prozess, Underwriting, DD-Berichte, KI-DD-Transparenz und Deckungsausschlüsse vor. |
| `grosskanzlei-ma-aktenanlage` | Freistehende M&A-Aktenanlage: eröffnet Deal-Akte, Aktenzeichen, Parteienregister, Ordnerstruktur, Datenraumspiegel, Vertraulichkeitsstufen und Closing-Bible-Grundgerüst mit vollständig interner Arbeitslogik. |
| `grosskanzlei-ma-erechnung-gobd` | Freistehender Billing-, GoBD- und E-Rechnungsworkflow für M&A-Mandate: erzeugt Narratives, Workstream-Abrechnung, XRechnung-XML, ZUGFeRD-Prüfpaket und revisionssicheren Buchungsnachweis. |
| `grosskanzlei-ma-fristen-cp-kalender` | Freistehender Deal-Fristen- und CP-Kalender: führt Signing-, Closing-, Q&A-, Regulatory-, Register-, Board-, Ordinary-Course- und Restrukturierungsfristen im M&A-Mandat. |
| `grosskanzlei-ma-insolvenzreife` | Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: prüft Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit, Überschuldung, Antragspflichten und Deal-Auswirkungen intern. |
| `grosskanzlei-ma-liquiditaetsvorschau` | Freistehende Liquiditätsvorschau für Corporate/M&A und Distressed M&A: prüft 3-Wochen-Liquidität, 13-Wochen-Cash-Bridge, Runway, OPOS, Bankdaten und Insolvenzschwellen intern. |
| `grosskanzlei-ma-schreibcanvas` | Freistehender Corporate-Schreibcanvas: begleitet SPA, Replik, Board Paper, Mandatsvereinbarung, DD-Report und Registertext mit freundlichen substanz- und belegorientierten Hinweisen. |
| `grosskanzlei-ma-tabellenreview` | Freistehender Tabellenreview für Corporate/M&A: prüft Dokumente, Datenpunkte, Tabellen, Formeln und Perspektiven als interne Review-Matrix mit vollständig interner Review-Logik. |

## Typische Workflows

- Buy-side: Target Screening -> NDA -> Aktenanlage -> Datenraum -> Tabellenreview -> Legal DD -> Q&A -> SPA-Markup -> Signing/Closing -> PMI.
- Sell-side: Teaser/IM -> Datenraumaufbau -> Vendor DD/Fact Book -> Bieter-Q&A -> Disclosure Schedules -> Vertragsverhandlung.
- Public M&A: Insider-/MAR-Prüfung -> Angebotsunterlage/Stellungnahme -> Kapitalmarktkommunikation -> Closing-Auflagen.
- Restrukturierung: Liquiditätsvorschau -> Insolvenzreifecheck -> StaRUG/Insolvenzplan -> Distressed M&A -> Gerichtsschritte -> Closing.
- Corporate Reorganisation: Umwandlung -> Umwandlungssteuerrecht -> Register/Notar -> Carve-out -> Closing.
- Billing: Zeitnachweise -> Narratives -> Workstream-Rechnung -> XRechnung/ZUGFeRD-Prüfpaket -> GoBD-Protokoll.

## Sicherheitsleitplanken

- Keine echte Transaktionsberatung ohne menschliche Letztprüfung.
- Keine Mandatsgeheimnisse, Insiderinformationen, Datenraumzugangsdaten oder Clean-Room-Daten in nicht freigegebene Systeme.
- KI-DD immer als `KI-gestützt`, `stichprobenvalidiert` oder `voll menschlich validiert` kennzeichnen.
- Register-, Rechtsprechungs-, Gesetzes- und Datenraumbelege müssen verifizierbar sein.
- Public M&A, MAR, WpÜG, Kartellrecht, Investitionskontrolle, Sanktionen, StaRUG, Zahlungsunfähigkeit und Überschuldung sind rote Schwellen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 56 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Großkanzlei-Corporate/M&A-Plugin. Fragt Rolle, Erfahrungslevel, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in e... |
| `grosskanzlei-corporate-ma-anfaenger-modus` | Anfänger- und First-Year-Associate-Modus für Großkanzlei Corporate/M&A: fragt Erfahrungslevel, Deal-Phase, Aufgabe, Frist, Unterlagen und gewünschte Führung ab; erklärt Begriffe, zerlegt Aufgaben in kleine Schritte, schlägt passende Plug... |
| `grosskanzlei-corporate-ma-automation-monitoring` | Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen. §§ 35 ff. GWB Karte... |
| `grosskanzlei-corporate-ma-billing-narratives` | Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss taugliche Time Narratives Phasenbudgets Workstream-Rechnungen Cap- und Success-Fee-Hinweise erstellen. § 3a RVG Stun... |
| `grosskanzlei-corporate-ma-board-paper-business-judgment` | Board Paper und Business Judgment Rule Prüfung für M&A-Entscheidungen: Anwendungsfall Vorstand AG Geschäftsführer GmbH oder Aufsichtsrat muss Transaktionsentscheidung formal absichern. § 93 Abs. 1 Satz 2 AktG Business Judgment Rule Infor... |
| `grosskanzlei-corporate-ma-closing-bible-archiv` | Closing Bible und Deal-Archiv erstellen: Anwendungsfall Mandant oder Counsel braucht nach Signing/Closing vollständige Dokumentensammlung aller executed Agreements, Signaturseiten und Registerbelege. §§ 433 ff. BGB SPA-Pflichten, Notarre... |
| `grosskanzlei-corporate-ma-conflict-gwg-sanctions` | Mandatsannahme-Prüfung im Corporate/M&A-Mandat: Interessenkonflikte nach § 43a BRAO, Geldwäschegesetz-Prüfung wirtschaftlich Berechtigter nach § 3 GwG, Sanktionsscreening nach AWG und EU-Verordnungen. Anwendungsfall neue Transaktionsmand... |
| `grosskanzlei-corporate-ma-datenqualitaet-xai-qualitaetskontrolle` | KI-Qualitaetskontrolle und Halluzinations-Absicherung in M&A-Transaktionen: Anwendungsfall KI-generierte DD-Berichte, Klauseln oder Recherchen sollen auf Datenqualitaet, Bias und Black-Box-Risiken geprüft werden. Art. 22 DSGVO automatisi... |
| `grosskanzlei-corporate-ma-datenraum-aufbau` | Due Diligence Datenraum strukturieren und bestücken: Anwendungsfall Mandant bereitet Verkaufsprozess vor oder Buyer-Team benoetigt strukturierten Datenraum für Private M&A, Public M&A, Carve-out oder Distressed-Prozesse. §§ 433 ff. BGB,... |
| `grosskanzlei-corporate-ma-datenraum-gap-clean-room` | Datenraum-Lueckenanalyse und Clean-Room-Protokoll für M&A Due Diligence: Anwendungsfall Anwalt oder Mandant stellt fest dass Datenraum Luecken hat oder sensible Wettbewerbsdaten nur unter Clean-Room-Bedingungen geteilt werden koennen. §§... |
| `grosskanzlei-corporate-ma-deal-intake` | Neues M&A-Mandat aufnehmen und strukturieren: Anwendungsfall Partner oder Associate erhaelt Erstanfrage zu einer Transaktion und muss Deal-Profil, Rolle, Parteien, Zeitplan und Workstreams erfassen. §§ 3a RVG Honorar, § 43a BRAO Konflikt... |
| `grosskanzlei-corporate-ma-deal-team-staffing` | Deal-Team-Besetzung und Staffing-Plan für Corporate/M&A-Transaktionen: Anwendungsfall Senior-Partner oder Team-Lead muss Workstreams Anwalt, Counsel, Associate, Paralegals und externe Spezialisten zuweisen. §§ 43a BRAO Interessenkonflikt... |
| `grosskanzlei-corporate-ma-disclosure-schedules` | Disclosure Schedules und Guarantees-Abgleich im SPA/APA: Anwendungsfall Verkaeufer-Anwalt erstellt Disclosure Schedules zur Einschraenkung von Reps and Warranties oder Kaeufer prüft ob Disclosure ausreichend ist. §§ 433 ff. BGB, SPA Disc... |
| `grosskanzlei-corporate-ma-distressed-ma` | Distressed M&A Transaktion begleiten: Anwendungsfall Unternehmen in Krise oder Insolvenz soll verkauft werden oder Investor prüft Erwerb notleidender Vermögenswerte. §§ 17-19 InsO Insolvenztatbestaende, § 1 StaRUG Sanierung, §§ 433 ff. B... |
| `grosskanzlei-corporate-ma-due-diligence-commercial-contracts` | Commercial Contracts Due Diligence im M&A-Datenraum: Anwendungsfall Kaeufer-Anwalt prüft wesentliche Kundenvertraege, Lieferantenvertraege, IP-Lizenzen, Change-of-Control-Klauseln und Kündigungsrechte. §§ 433 ff. BGB SPA-Garantien, §§ 30... |
| `grosskanzlei-corporate-ma-due-diligence-legal` | Legal Due Diligence im M&A-Prozess: Anwendungsfall Kaeufer-Anwalt prüft Corporate-Unterlagen, Rechtsstreitigkeiten, Regulatory-Status, Arbeitsrecht und IP der Zielgesellschaft. §§ 433 ff. BGB SPA-Garantien, § 93 AktG Organpflichten. Prüf... |
| `grosskanzlei-corporate-ma-due-diligence-reporting` | Due Diligence Report erstellen und strukturieren: Anwendungsfall After DD-Phase muss Anwalt einen umfassenden DD-Bericht für Kaeufer-Management, Investitionskomitee oder Finanzierungsbank erstellen. SPA-Berichtspflichten, § 93 AktG Infor... |
| `grosskanzlei-corporate-ma-expert-calls-transkripte` | Expert Calls und Transkript-Auswertung für M&A Due Diligence: Anwendungsfall Deal-Team hat Experteninterviews oder Management-Presentations transkribiert und muss Kernaussagen strukturiert extrahieren. MAR Vertraulichkeit, §§ 433 ff. BGB... |
| `grosskanzlei-corporate-ma-fair-disclosure-knowledge` | Fair Disclosure und Knowledge-Qualifikation in M&A-Vertraegen: Anwendungsfall Vertragsparteien verhandeln Wissenszurechnung, Kenntnis-Definitionen und Fair-Disclosure-Mechanismus im SPA. §§ 433 ff. BGB, § 442 BGB Kaeufer-Kenntnis. Prüfra... |
| `grosskanzlei-corporate-ma-freundlicher-copilot` | Freundlicher M&A-Deal-Copilot für junge Anwaelte und Associates: Anwendungsfall Junior-Associate oder Trainee arbeitet an erster groesserer Corporate-Transaktion und braucht verstaendnisbasierte Begleitung ohne Vorwurf. M&A-Praxis, SPA S... |
| `grosskanzlei-corporate-ma-gesellschaftsrecht-register` | Corporate Housekeeping und Register-Prüfung im M&A-Kontext: Anwendungsfall Anwalt prüft für Kaeufer oder Verkaeufer HRB/HRA-Eintrag, Gesellschafterlisten, Satzungen, Beschluesse, Vollmachten und Organstellung der Zielgesellschaft. §§ 8-1... |
| `grosskanzlei-corporate-ma-handelsregisterabruf` | Handelsregister-Abruf und Registerrecherche für M&A-Transaktionen: Anwendungsfall Anwalt recherchiert offiziellen Registerstand für Zielgesellschaft, Kaeufer-Holding, Komplementaer-GmbH oder Beteiligungsketten. §§ 8-10 GmbHG, §§ 29 ff. H... |
| `grosskanzlei-corporate-ma-kaltstart` | Kanzlei- und Mandantenpraeferenzen für Corporate/M&A erfassen: Anwendungsfall bei erstem Einsatz des Plugins konfiguriert Anwalt oder Kanzlei Deal-Playbooks, Materiality-Schwellen, Reporting-Standards, Abrechnungsmodell und KI-Governance... |
| `grosskanzlei-corporate-ma-kg-personengesellschaften` | KG und Personengesellschaften in M&A-Transaktionen: Anwendungsfall Mandat betrifft Kommanditanteilsuebertragung, Fondsvehikel-Struktur, Kommanditistenwechsel oder Einbringung in KG. §§ 161-177 HGB, MoPeG, §§ 20-24 UmwStG Einbringung. Prü... |
| `grosskanzlei-corporate-ma-ki-governance-berufsrecht` | KI-Einsatz im Transaktionsmandat berufsrechtlich absichern: Anwendungsfall Anwalt moechte KI-Tools für Datenraumanalyse oder Vertragsentwurf nutzen und muss Mandatsgeheimnis, Datenschutz und KI-VO-Betreiberpflichten einhalten. § 43a BRAO... |
| `grosskanzlei-corporate-ma-kommandocenter` | Deal-Kommandocenter Corporate/M&A: Schnellstart und Workflow-Routing für alle Transaktionsphasen. Anwendungsfall Anwalt gibt Kuerzel, Dokument oder Sachverhaltssatz ein und wird in richtigen Deal-Skill geleitet. SPA Share Purchase Agreem... |
| `grosskanzlei-corporate-ma-look-and-feel` | Corporate-Deal-Workspace Darstellung und Ausgabeformat: Anwendungsfall alle sichtbaren Outputs sollen im einheitlichen M&A-Kanzleistil erscheinen — ruhig, edel, deal-informationsdicht ohne Marketing-Ton. Big-Law-Standard, Partnerqualitae... |
| `grosskanzlei-corporate-ma-matter-file` | Deal-Akte und Matter-Workspace anlegen: Anwendungsfall bei Mandatsannahme wird strukturierter Matter-Workspace benoetigt mit allen Workstreams, Datenraumspiegel, Register-Links, Q&A-Tracker und Closing-Archiv. § 43a BRAO Aktenführung, Go... |
| `grosskanzlei-corporate-ma-output-versand-signing` | Transaktionsoutput, Signing-Pack und Versand vorbereiten: Anwendungsfall Closing oder Signing naht und Anwalt muss Markups, Board Papers, Signing Packs, Closing Deliverables und beA/Notar/Email-Versand koordinieren. §§ 125 ff. BGB Formvo... |
| `grosskanzlei-corporate-ma-outside-in-target-screening` | Zielobjekt-Screening und Pipeline-Analyse aus öffentlichen Quellen: Anwendungsfall Mandant oder Deal-Team sucht geeignete Akquisitionsziele und muss fruehe Analyse aus Registern, Finanzdaten, Nachrichten und Branchenhinweisen erstellen.... |
| `grosskanzlei-corporate-ma-post-closing-integration` | Post-Merger-Integration planen und begleiten: Anwendungsfall nach Closing muessen DD-Findings, SPA-Pflichten und Earn-Out-Mechanismen in PMI-Plan uebersetzt und Betriebsuebergang sowie Registeranmeldungen abgewickelt werden. § 613a BGB B... |
| `grosskanzlei-corporate-ma-public-ma-kapitalmarkt-mar` | Public M&A und Kapitalmarkt-Compliance bei boersennotierten Transaktionen: Anwendungsfall Anwalt begleitet Übernahmeangebot, Pflichtangebot oder Squeeze-Out § 327a AktG bei boersennotierter Zielgesellschaft. WpUEG Angebotsunterlage, MAR... |
| `grosskanzlei-corporate-ma-qa-information-requests` | Q&A-Prozess und Information Requests in der Due Diligence steuern: Anwendungsfall Deal-Team muss aus DD-Analyse gezielte Fragen an Verkaeufer formulieren, priorisieren und Antworten gegen Datenraum-Belege prüfen. SPA Due Diligence Prozes... |
| `grosskanzlei-corporate-ma-rechtsprechungsrecherche` | Corporate und M&A Rechtsprechungsrecherche: Anwendungsfall Anwalt braucht für Gutachten, Schriftsatz oder DD-Report relevante BGH-Rechtsprechung zu Organpflichten, Kapitalmarkt, Umwandlung oder Insolvenz. §§ 93 und 179a AktG, § 15 AktG V... |
| `grosskanzlei-corporate-ma-regulatory-fdi-merger-control` | Fusionskontrolle und FDI-Investitionsprüfung für M&A-Transaktionen: Anwendungsfall Signing naht und Deal-Team prüft ob Kartellrechts-Freigabe oder AWV-Prüfung benoetigt wird. §§ 35-44 GWB inlaendische Fusionskontrolle, Art. 4 FKVO EU-Fus... |
| `grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan` | StaRUG-Restrukturierung und Insolvenzplanverfahren begleiten: Anwendungsfall Unternehmen mit drohender Zahlungsunfähigkeit prüft Restrukturierungsoptionen einschließlich StaRUG-Plan, praeventiyen Restrukturierungsrahmen oder Insolvenzpla... |
| `grosskanzlei-corporate-ma-signing-closing-conditions` | Signing-to-Closing-Prozess mit Conditions Precedent für M&A-Transaktionen: Anwendungsfall nach Signing muessen alle Closing-Bedingungen erfuellt und Closing Deliverables koordiniert werden. SPA Closing Conditions, § 179a AktG Hauptversam... |
| `grosskanzlei-corporate-ma-simulation-bidder-process` | M&A-Bieterprozess simulieren für Training und Mandatsvorbereitung: Anwendungsfall Junior-Anwalt oder Deal-Team ueben beschleunigten Transaktions-Tag mit Datenraum Q&A SPA-Markup CP-Liste und Board-Call. SPA Share Purchase Agreement, Due... |
| `grosskanzlei-corporate-ma-spa-apa-entwurf` | SPA Share Purchase Agreement und APA Asset Purchase Agreement entwerfen: Anwendungsfall Anwalt erstellt Kaufvertrag für Share Deal oder Asset Deal aus Term Sheet DD-Findings und Transaktionsstruktur. §§ 433 ff. BGB Kaufrecht, § 15 GmbHG... |
| `grosskanzlei-corporate-ma-steps-plan-pmo` | Deal-PMO und Steps-Plan für Pre-Signing bis Post-Closing: Anwendungsfall Transaktion braucht praezisen Aufgaben- und Zeitplan aus Vertraegen, DD-Unterlagen und Gremienunterlagen extrahiert. SPA Closing Conditions, CPs Conditions Preceden... |
| `grosskanzlei-corporate-ma-tabellenreview-3d-datenraum` | 3D-Tabellenreview M&A-Datenraum: Dokumente Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft verbinden: Anwendungsfall Deal-Team prüft Datenraum-Dokumente systematisch mit internem Review-Cube nach mehreren Workstream-Perspektiven. SP... |
| `grosskanzlei-corporate-ma-teaser-im-processdocs` | Investment Teaser Information Memorandum und Prozessdokumente erstellen: Anwendungsfall Sell-side-Mandat braucht Teaser für erste Bieterkontakte, Information Memorandum und Process Letter für strukturierten Auktionsprozess. SPA M&A-Proze... |
| `grosskanzlei-corporate-ma-transaktionsstruktur` | Transaktionsstruktur für M&A entwickeln und Varianten bewerten: Anwendungsfall Mandant fragt welche Transaktionsstruktur für seinen Unternehmenskauf -verkauf oder Carve-out am besten passt. Share Deal Asset Deal Carve-out Joint Venture V... |
| `grosskanzlei-corporate-ma-translations-multijurisdictional` | Multi-Jurisdiction-Koordination und Übersetzungen in grenzüberschreitenden M&A-Transaktionen: Anwendungsfall Transaktion mit mehreren Laendern erfordert Koordination lokaler Counsel, Übersetzungen und Rechtsvergleich. Internationales Pri... |
| `grosskanzlei-corporate-ma-umwandlungsrecht` | Umwandlungsrecht Verschmelzung Spaltung Formwechsel und Carve-outs nach UmwG bearbeiten: Anwendungsfall Mandant plant Verschmelzung zweier GmbHs Ausgliederung eines Geschäftsbereichs oder Formwechsel AG zu GmbH im Rahmen einer Transaktio... |
| `grosskanzlei-corporate-ma-umwandlungssteuerrecht` | Umwandlungssteuerrecht Buchwertantrag steuerliche Rückwirkung und Verlustuntergang prüfen: Anwendungsfall Corporate-Team und Steuerteam muessen umwandlungssteuerliche Strukturentscheidung abstimmen. §§ 20-24 UmwStG Einbringung, § 8c KStG... |
| `grosskanzlei-corporate-ma-vertragsmarkup-key-issues` | SPA/APA/NDA Markup analysieren und Key Issues List erstellen: Anwendungsfall Anwalt erhaelt Gegenentwurf oder Markup und muss wirtschaftlich relevante Abweichungen strukturieren und Gegenvorschlaege formulieren. §§ 433 ff. BGB Kaufrecht,... |
| `grosskanzlei-corporate-ma-wi-insurance` | W&I-Versicherung Warranty and Indemnity in M&A-Transaktionen: Anwendungsfall Kaeufer oder Verkaeufer erwägt W&I-Versicherung für SPA-Garantien und muss Underwriting-Prozess, DD-Berichts-Anforderungen und Deckungsausschluesse klaeren. SPA... |
| `grosskanzlei-ma-aktenanlage` | Freistehende M&A-Aktenanlage ohne externes Plugin: Anwendungsfall neue Corporate-Transaktion wird aufgenommen und Deal-Akte mit Aktenzeichen Parteienregister Ordnerstruktur Datenraumspiegel und Closing-Bible-Grundgeruest wird benoetigt.... |
| `grosskanzlei-ma-erechnung-gobd` | Freistehender Billing- GoBD- und E-Rechnungsworkflow für M&A-Mandate: Anwendungsfall Kanzlei muss für M&A-Mandat GoBD-konforme Rechnung XRechnung-XML und ZUGFeRD-Prüfpaket erstellen. § 3a RVG Stundenhonorar, GoBD Aufbewahrung, ZUGFeRD XR... |
| `grosskanzlei-ma-fristen-cp-kalender` | Freistehender Deal-Fristen- und CP-Kalender für M&A-Mandate: Anwendungsfall Fristen aus Signing Closing Q&A Regulatory Register Board und Restrukturierung muessen in einem Kalender zusammengeführt werden. SPA Closing Conditions, §§ 35 ff... |
| `grosskanzlei-ma-insolvenzreife` | Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: Anwendungsfall im Kaufprozess oder Beratungsmandat muss geprüft werden ob Zielunternehmen oder Mandant nahe an Insolvenzantragspflicht ist. §§ 17-19 InsO Zahlungsunfähigkei... |
| `grosskanzlei-ma-liquiditaetsvorschau` | Freistehende Liquiditaetsvorschau für Corporate M&A und Distressed M&A: Anwendungsfall Kaeufer Verkaeufer oder Vorstand braucht kurzfristige Zahlungsfähigkeits-Übersicht 3-Wochen bis 13-Wochen-Horizont. § 17 InsO Zahlungsunfähigkeit, § 1... |
| `grosskanzlei-ma-schreibcanvas` | Freistehender Corporate-Schreibcanvas für SPA Board Paper und DD-Report: Anwendungsfall Anwalt entwirft SPA-Klausel Markup-Antwort DD-Report oder Mandatsvereinbarung und braucht substanzorientierten Schreibbegleiter der unsubstantiierte... |
| `grosskanzlei-ma-tabellenreview` | Freistehender Tabellenreview für Corporate M&A-Dokumente Datenpunkte und Perspektiven: Anwendungsfall Tabellen Formeln Excel-Modelle oder Dokumentenmatrizen in Transaktionen muessen auf Formelbrueche widersprüchliche Zahlen und Inkonsist... |
| `ki-einsatz-bei-gutachten-mandatsseite` | Großkanzlei-Mandatsseite bei KI-Verdacht gegenüber gerichtlichen oder vorgerichtlichen Sachverständigengutachten in Corporate-, M&A- und Schiedsverfahren. Strategische Prüfung der höchstpersönlichen Erstellungspflicht nach § 407a Abs. 1... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
