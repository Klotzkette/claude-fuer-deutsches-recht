# Corporate-Kanzlei-Plugin

Technischer Plugin-Name: `corporate-kanzlei`.

Eigenständiges Corporate-Kanzlei-Plugin für große Corporate- und M&A-Mandate: Origination, Outside-in-Assessment, Datenraum, Due Diligence, Tabellenreview, Q&A, SPA/APA, Disclosure Schedules, Knowledge/Fair Disclosure, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing und Closing Bible.

Es ist als leistungsstarker Arbeitsrahmen für erfahrene Transaktionsteams gedacht, bleibt aber freundlich genug, um jüngere Anwender Schritt für Schritt durch große Deal-Workflows zu führen.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Corporate-Kanzlei Corporate/M&A (`corporate-kanzlei`) | [corporate-kanzlei.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/corporate-kanzlei.zip) |
| Tabellenreview 3D | [tabellenreview-3d.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tabellenreview-3d.zip) |
| Gesellschaftsrecht | [gesellschaftsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht.zip) |

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `corporate-kanzlei.zip` hochladen.
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
| corporate-kanzlei-public-ma-kapitalmarkt-mar | Public M&A, Kapitalmarkt und MAR | Begleitet börsennotierte Transaktionen: WpUEG-Unterlagen, Ad-hoc-Prüfung, Insiderlisten, Stellungnahmen und Marktgerüchte. |
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
- Public M&A, MAR, WpUEG, Kartellrecht, Investitionskontrolle, Sanktionen, StaRUG und Insolvenzreife sind rote Schwellen.
