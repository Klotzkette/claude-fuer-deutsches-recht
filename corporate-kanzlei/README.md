# Corporate-Kanzlei-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`corporate-kanzlei.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/corporate-kanzlei.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/corporate-kanzlei/corporate-kanzlei-werkstatt.md" download><code>corporate-kanzlei-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/corporate-kanzlei/corporate-kanzlei-schnellstart.md" download><code>corporate-kanzlei-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Insolvenz-Asset-Deal — ChainCortex AI GmbH (Berlin) → Voracis Ventures GmbH: [Gesamt-PDF](../testakten/insolvenz-asset-deal-chaincortex-ai-berlin/gesamt-pdf/insolvenz-asset-deal-chaincortex-ai-berlin_gesamt.pdf), [`testakte-insolvenz-asset-deal-chaincortex-ai-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenz-asset-deal-chaincortex-ai-berlin.zip), [`testakte-insolvenz-asset-deal-chaincortex-ai-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenz-asset-deal-chaincortex-ai-berlin-einzelpdfs.zip); M&A Asset Deal MedTech — VENERA/FraktoMedis Präzision (Darmstadt): [Gesamt-PDF](../testakten/ma-asset-deal-medtech-volkenrath-darmstadt/gesamt-pdf/ma-asset-deal-medtech-volkenrath-darmstadt_gesamt.pdf), [`testakte-ma-asset-deal-medtech-volkenrath-darmstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ma-asset-deal-medtech-volkenrath-darmstadt.zip), [`testakte-ma-asset-deal-medtech-volkenrath-darmstadt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ma-asset-deal-medtech-volkenrath-darmstadt-einzelpdfs.zip); Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio: [Gesamt-PDF](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf), [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip), [`testakte-private-equity-buyout-schuldschein-npl-heidelberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine gesellschaftsrechtliche Maßnahme rechtssicher beschliessen und dokumentieren.
Technischer Plugin-Name: `corporate-kanzlei`.

Eigenständiges Corporate-Kanzlei-Plugin für große Corporate- und M&A-Mandate: Origination, Outside-in-Assessment, Datenraum, Due Diligence, Tabellenreview, Q&A, SPA/APA, Disclosure Schedules, Knowledge/Fair Disclosure, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing und Closing Bible.

Es ist als leistungsstarker Arbeitsrahmen für erfahrene Transaktionsteams gedacht, bleibt aber freundlich genug, um jüngere Anwender Schritt für Schritt durch große Deal-Workflows zu führen.

## Installation

1. ZIP herunterladen.
2. Plugin-Umgebung öffnen.
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
| corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle | Datenqualität und XAI-Qualitätskontrolle | Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab. |
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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 87 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agio` | Strukturierung von Kapitalerhöhungen mit Agio bei VC-Finanzierungsrunden Holding-Aufbauten und M&A-Sekundärfinanzierungen. Übersetzung US-Term-Sheet-Begriffe (Original Purchase Price Par Value APIC Liquidation Preference) in deutsche Kat... |
| `agio-und-kapitalerhoehungsstruktur` | Strukturierung von Kapitalerhöhungen mit Agio bei VC-Finanzierungsrunden Holding-Aufbauten und M&A-Sekundärfinanzierungen. Übersetzung US-Term-Sheet-Begriffe (Original Purchase Price Par Value APIC Liquidation Preference) in deutsche Kat... |
| `automation-monitoring` | Automationen und Monitoring: Entwirft Monitore für Datenraum-Neuzugaenge, Q&A-Status, CP-Deadlines, Registerupdates, MAR-Signale und PMI-Aufgaben im Corporate/M&A-Kontext. Normen: MAR Art. 17, § 41 GWB (Vollzugsverbot), § 56 AWV. |
| `automation-monitoring-billing-narratives` | Automationen und Monitoring: Entwirft Monitore für Datenraum-Neuzugaenge, Q&A-Status, CP-Deadlines, Registerupdates, MAR-Signale und PMI-Aufgaben im Corporate/M&A-Kontext. Normen: MAR Art. 17, § 41 GWB (Vollzugsverbot), § 56 AWV im Corpo... |
| `beirat-gmbh-zustimmungskatalog` | Prüft und entwirft GmbH-Beiratsregeln für mittelständische und Corporate-Mandate: Vetorechte, Investorenschutz, Haftung, Protokoll, Deadlock und Geschäftsführerautonomie |
| `beirat-gmbh-zustimmungskatalog-und-konfliktmatrix` | Prüft und entwirft GmbH-Beiratsregeln für mittelständische und Corporate-Mandate: Vetorechte, Investorenschutz, Haftung, Protokoll, Deadlock und Geschäftsführerautonomie im Corporate Kanzlei. |
| `billing-narratives` | Corporate Billing Narratives: Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. Normen: RVG (wenn anwendbar), Stundenhonorar-Vereinbarung, BRAO § 49b. |
| `board-paper-business` | Board Paper und Business Judgment Rule (§ 93 AktG, § 43 GmbHG) erstellen: Vorlage für Vorstand/Geschäftsführung/Aufsichtsrat bei M&A-Entscheidungen, Strukturwahl, Risikotransaktionen. Prüfraster: Informationsgrundlage, Entscheidungsalter... |
| `board-paper-closing-bible` | Board Paper und Business Judgment Rule (§ 93 AktG, § 43 GmbHG) erstellen: Vorlage für Vorstand/Geschäftsführung/Aufsichtsrat bei M&A-Entscheidungen, Strukturwahl, Risikotransaktionen. Prüfraster: Informationsgrundlage, Entscheidungsalter... |
| `board-paper-rechtsprechungsradar-gmbh-governance` | Corporate-Board-Paper-Skill für aktuelle GmbH-Governance-Rechtsprechung: Abberufung, Weisungen, Binnenpflichtverletzung, Registervollzug und Deal-Risiko nach BGH II ZR 71/23. |
| `closing-bible-archiv` | Closing Bible und Deal-Archiv nach M&A-Closing erstellen: Mandant oder Partner benoetigt vollständige Vertragsdokumentation mit Signaturketten, Registerbelegen, Notarbestätigungen und Anlagen. Normen: SPA Deliverables-Checkliste, § 15 Gm... |
| `conflict-gwg-datenqualitaet-xai` | Konflikt-, GwG- und Sanktionscheck: Mandatsannahmeprüfung für Corporate/M&A: Interessenkonflikte (§ 43a BRAO), wirtschaftlich Berechtigte (§§ 2 ff. GwG), Sanktionen (EU/US OFAC), PEP, Mittelherkunft, Sektor- und Länderrisiken im Corporat... |
| `conflict-gwg-sanctions` | Konflikt-, GwG- und Sanktionscheck: Mandatsannahmeprüfung für Corporate/M&A: Interessenkonflikte (§ 43a BRAO), wirtschaftlich Berechtigte (§§ 2 ff. GwG), Sanktionen (EU/US OFAC), PEP, Mittelherkunft, Sektor- und Länderrisiken. |
| `corporate-beirat-gmbh` | Corporate: Erstprüfung, Rollenklärung und Mandatsziel im Corporate Law: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/M&A), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `corporate-kanzlei-translations-multijurisdictional` | Mehrsprachige Transaktionsdokumente in DE/EN erstellen und prüfen: Internationale M&A-Transaktion erfordert konsistente Terminologie in beiden Sprachen. Normen: § 184 GVG (Deutsch als Gerichtssprache), EGBGB Art. 10 ff. (Sprache des Rech... |
| `datenqualitaet-xai` | Qualitaetskontrolle und Quellenvalidierung im Corporate/M&A-Mandat: Partner oder Counsel prüft KI-generierte DD-Findings auf fehlerhafte Quellen, Luecken in der Belegkette und Black-Box-Schluesse. Normen: BRAO § 43a (Sorgfaltspflicht), E... |
| `datenqualitaet-xai-qualitaetskontrolle` | Qualitaetskontrolle und Quellenvalidierung im Corporate/M&A-Mandat: Partner oder Counsel prüft KI-generierte DD-Findings auf fehlerhafte Quellen, Luecken in der Belegkette und Black-Box-Schluesse. Normen: BRAO § 43a (Sorgfaltspflicht), E... |
| `datenraum-aufbau` | Virtuellen Datenraum strukturieren und befuellen für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. Anwendungsfall: Verkaeuferkanzlei richtet DR ein oder Kaeufer hat Zugang erhalten. Normen: DSGVO Art. 28 (Auftragsverarbeitu... |
| `datenraum-aufbau-gap` | Virtuellen Datenraum strukturieren und befuellen für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. Anwendungsfall: Verkaeuferkanzlei richtet DR ein oder Kaeufer hat Zugang erhalten. Normen: DSGVO Art. 28 (Auftragsverarbeitu... |
| `datenraum-gap-clean-room` | Gap-Analyse des Datenraums und Clean-Room-Protokoll für M&A-Transaktionen: Identifiziert fehlende Dokumente, verwaltet IRL-Status (Information Request List), trennt sensible Wettbewerberdaten. Normen: DSGVO, GWB Clean-Team-Grundsaetze, M... |
| `deal-intake` | Neues Transaktionsmandat strukturiert aufnehmen aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message oder DR-Einladung. Anwendungsfall: Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen. Normen: BRAO § 43a, GwG §§ 10 ff. (KYC), W... |
| `deal-intake-team` | Neues Transaktionsmandat strukturiert aufnehmen aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message oder DR-Einladung. Anwendungsfall: Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen. Normen: BRAO § 43a, GwG §§ 10 ff. (KYC), W... |
| `deal-team-staffing` | Transaktionsteam zusammenstellen und Workstreams verteilen für M&A-Mandate: Senior Associate braucht Team-Plan oder Partner will Kapazitaeten ueberprüfen. Normen: BRAO § 43a (Interessenkonflikte), RVG/Stundenhonorar, Budget-Richtlinien.... |
| `disclosure-schedules` | Disclosure Schedules zum SPA erstellen und prüfen: Verkaeufer offenbart bekannte Risiken um Warranty-Verletzungen nach § 444 BGB (Arglist) zu verhindern; Kaeufer prüft Vollständigkeit. Normen: § 444 BGB, § 311 Abs. 2 BGB (vorvertragliche... |
| `disclosure-schedules-distressed-ma` | Disclosure Schedules zum SPA erstellen und prüfen: Verkaeufer offenbart bekannte Risiken um Warranty-Verletzungen nach § 444 BGB (Arglist) zu verhindern; Kaeufer prüft Vollständigkeit. Normen: § 444 BGB, § 311 Abs. 2 BGB (vorvertragliche... |
| `distressed-ma` | Prüfungslinie für corporate kanzlei distressed ma im Corporate Kanzlei. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `due-diligence-commercial` | Commercial Contracts Due Diligence: Prüft wesentliche Vertraege im M&A-Datenraum auf Change-of-Control-Klauseln, Kündigungsrechte, Exklusivitaet, Haftungsgrenzen und Material-Contract-Risiken für SPA-Reps. Normen: §§ 305 ff. BGB, § 311 A... |
| `due-diligence-commercial-und-legal` | Commercial Contracts Due Diligence: Prüft wesentliche Vertraege im M&A-Datenraum auf Change-of-Control-Klauseln, Kündigungsrechte, Exklusivitaet, Haftungsgrenzen und Material-Contract-Risiken für SPA-Reps. Normen: §§ 305 ff. BGB, § 311 A... |
| `due-diligence-expert-calls` | DD-Reporting: Konsolidiert Legal, Tax, Financial und Commercial Due-Diligence-Workstreams zu einem integrierten DD-Bericht für M&A-Transaktionen. Normen: §§ 311 Abs. 2 und 444 BGB; SPA Representations & Warranties. Prüfraster: Executive... |
| `due-diligence-legal` | Legal Due Diligence für M&A-Transaktionen: Prüft Corporate, Vertragswerk, HR, IP, Litigation und Compliance im Datenraum. Normen: §§ 311 Abs. 2 und 444 BGB sowie GmbHG, AktG, einschlaegige Sondergesetze. Prüfraster: Risk-Rating (hoch/mit... |
| `due-diligence-reporting` | DD-Reporting: Konsolidiert Legal, Tax, Financial und Commercial Due-Diligence-Workstreams zu einem integrierten DD-Bericht für M&A-Transaktionen. Normen: §§ 311 Abs. 2 und 444 BGB; SPA Representations & Warranties. Prüfraster: Executive... |
| `einstieg-routing` | Einstieg, Triage und Routing für Corporate-Kanzlei (M&A, Gesellschaftsrecht): ordnet Rolle (Seller, Buyer, Target, Berater (anwaltlich, steuerlich, M&A), Aufsichtsrat), markiert Frist (Ad-hoc unverzüglich), wählt Norm (AktG, GmbHG, HGB,... |
| `erstpruefung-rollenklaerung-mandatsziel` | Corporate: Erstprüfung, Rollenklärung und Mandatsziel im Corporate Law: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/M&A), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `expert-calls-transkripte` | Expert Calls und Transkript-Auswertung in M&A-Due-Diligence: DD-Team führt Experten-Interviews durch und will strukturierte Findings extrahieren. Normen: § 17 UWG (Geschäftsgeheimnis), DSGVO Art. 6, MAR Insider-Abgrenzung, Expert Network... |
| `fair-disclosure-kg-personengesellschaften` | Fair Disclosure und Knowledge Management: Steuert Informationsfluss in M&A-Transaktionen nach MAR, Kartellrecht-Clean-Team und Insider-Regelungen. Normen: Art. 17-18 MAR, §§ 1 und 41 GWB, § 43a BRAO. Insider-Log, Need-to-know, Firewall i... |
| `fair-disclosure-knowledge` | Fair Disclosure und Knowledge Management: Steuert Informationsfluss in M&A-Transaktionen nach MAR, Kartellrecht-Clean-Team und Insider-Regelungen. Normen: Art. 17-18 MAR, §§ 1 und 41 GWB, § 43a BRAO. Insider-Log, Need-to-know, Firewall. |
| `freundlicher-copilot` | Freundlicher Corporate-Copilot: Einstiegshilfe für alle Corporate/M&A-Aufgaben. Erklärt Fachbegriffe, gibt Überblicke zu Transaktionsstrukturen, beantwortet Erstfragen und leitet zu passenden Fach-Skills weiter. |
| `freundlicher-copilot-gesellschaftsrecht` | Freundlicher Corporate-Copilot: Einstiegshilfe für alle Corporate/M&A-Aufgaben. Erklärt Fachbegriffe, gibt Überblicke zu Transaktionsstrukturen, beantwortet Erstfragen und leitet zu passenden Fach-Skills weiter im Corporate Kanzlei. |
| `gesellschaftsrecht-register` | Gesellschaftsrechtliche Registeranmeldungen und Satzungsaenderungen durchführen: Handelsregister-Anmeldung von GF-Bestellung, Kapitalerhoehung, Satzungsaenderung, Verschmelzung. Normen: §§ 39-45 GmbHG, §§ 36-39 AktG, HRV, §§ 8-15 HGB. Pr... |
| `handelsregisterabruf` | Handelsregister-Daten abrufen und analysieren: Anwalt oder Mandant benoetigt Gesellschaftsstruktur, Haftungsverhältnisse, Offenlegungspflichten aus HRA/HRB, Bundesanzeiger und Transparenzregister. Normen: §§ 8-15 HGB, § 9 GmbHG, §§ 67-68... |
| `handelsregisterabruf-ki-governance` | Handelsregister-Daten abrufen und analysieren: Anwalt oder Mandant benoetigt Gesellschaftsstruktur, Haftungsverhältnisse, Offenlegungspflichten aus HRA/HRB, Bundesanzeiger und Transparenzregister. Normen: §§ 8-15 HGB, § 9 GmbHG, §§ 67-68... |
| `kaltstart` | Kaltstart Corporate-Kanzlei: Strukturiert den Einstieg in ein neues Corporate/M&A-Mandat mit Schnellerfassung von Parteien, Dealtyp, Phase, ersten Risiken und naechsten Schritten. Normen: BRAO §§ 43a und 49b; GwG § 10 (KYC); MAR Insider-... |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Corporate Kanzlei-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokum... |
| `kg-personengesellschaften` | KG und Personengesellschaften im Corporate/M&A-Kontext begleiten: Anteilsuebertragung, Haftungsstruktur, Ergebnisverwendung bei KG, GmbH & Co. KG, Partnerschaft und GbR nach MoPeG 2024. Normen: HGB §§ 105-177a, MoPeG 2024, AktG (Kommandi... |
| `ki-governance-berufsrecht` | KI-Governance und Berufsrecht: Rechtliche Rahmenbedingungen für den Einsatz von KI-Werkzeugen in Kanzleien. EU-KI-VO (AI Act), BRAO-Verschwiegenheit, Mandanteninformation, Haftung, Qualitaetssicherung. Dokumentation für BJR-Schutz. |
| `kommandocenter` | Deal-Kommandocenter Corporate/M&A: Schnellstart für Mandate. Erkennt Dealtyp, Phase und Parteiperspektive; erzeugt Deal-Karte mit Ampel, Rollen, naechster Aktion und Freigabegrad. Routet an passenden Fachmodul (SPA, DD, StaRUG, Kapitalma... |
| `lma-facility` | Deal-Kommandocenter Corporate/M&A: Schnellstart für Mandate. Erkennt Dealtyp, Phase und Parteiperspektive; erzeugt Deal-Karte mit Ampel, Rollen, naechster Aktion und Freigabegrad. Routet an passenden Fachmodul (SPA, DD, StaRUG, Kapitalma... |
| `lma-facility-und-transfer` | Prüft hochgeladene LMA-basierte Kreditverträge aus deutscher Corporate-Sicht: Transfer, Assignment, Novation, Agent, Conditions, Covenants und Default. |
| `look-and-feel` | Corporate-Cowork-Design: Definiert die visuelle Oberflaeche für Partner, Counsel und Associates. Ruhig, edel, blaeulich-silbern; Orange für Entscheidungspunkte. Statuskarten, Ampeln und dichte Deal-Information statt Marketing. Keine Spie... |
| `look-feel-matter-file` | Corporate-Cowork-Design: Definiert die visuelle Oberflaeche für Partner, Counsel und Associates. Ruhig, edel, blaeulich-silbern; Orange für Entscheidungspunkte. Statuskarten, Ampeln und dichte Deal-Information statt Marketing. Keine Spie... |
| `matter-file` | Transaktionsakte strukturieren und verwalten für Corporate/M&A-Mandate: Anwalt benoetigt Dokument-Klassifizierung, Versionskontrolle, Zugriffsrechteverwaltung und Aufbewahrungsplanung. Normen: §§ 257 HGB, 147 AO (Aufbewahrungspflichten),... |
| `npl-distressed-loan` | Prüft Erwerb/Verkauf notleidender Darlehen im Corporate-Kontext: KrZwMG-Rollen, Datenschutz, Sicherheiten, Borrower Notices, Portfolio-DD und Enforcement. |
| `npl-distressed-outside-target` | Prüft Erwerb/Verkauf notleidender Darlehen im Corporate-Kontext: KrZwMG-Rollen, Datenschutz, Sicherheiten, Borrower Notices, Portfolio-DD und Enforcement im Corporate Kanzlei. |
| `output-versand-signing` | Signing-Management und Output-Verteilung für M&A-Vertraege: Koordiniert physisches und virtuelles Signing, Signaturseiten-Protokoll, qualifizierte eSignatur (QES), Exekution und Verteilung. Normen: §§ 126 und 126a und 127 BGB (Schriftfor... |
| `outside-in-target-screening` | Outside-In-Zielunternehmen-Screening aus öffentlichen Quellen für M&A-Vorprüfung: M&A-Team benoetigt schnellen Überblick über Target ohne Datenraumzugang. Normen: § 3 GwG (UBO-Identifikation), DSGVO, WpHG §§ 33 ff. (Stimmrechtsmitteilung... |
| `post-closing-integration` | Post-Closing-Integration (PMI) rechtlich begleiten: Unmittelbar nach Closing muessen Handelsregister, Vertraege, Organ-Strukturen und Steuereinheiten angepasst werden. Normen: GmbHG, AktG, UmwStG, KStG (Organschaft), § 613a BGB (Betriebs... |
| `post-closing-umwandlungssteuerrecht` | Post-Closing-Integration (PMI) rechtlich begleiten: Unmittelbar nach Closing muessen Handelsregister, Vertraege, Organ-Strukturen und Steuereinheiten angepasst werden. Normen: GmbHG, AktG, UmwStG, KStG (Organschaft), § 613a BGB (Betriebs... |
| `public-ma-kapitalmarkt-mar` | Public M&A und Kapitalmarkt: Begleitet Öffentliche Angebote (WpueG), Pflichtangebote, Squeeze-Out und Delisting. Normen: WpueG, AktG §§ 327a-f, WpHG/MAR Ad-hoc, §§ 39a-c WpueG. Leitsaetze BGH und BaFin-Praxis. |
| `public-ma-qa-information` | Public M&A und Kapitalmarkt: Begleitet Öffentliche Angebote (WpueG), Pflichtangebote, Squeeze-Out und Delisting. Normen: WpueG, AktG §§ 327a-f, WpHG/MAR Ad-hoc, §§ 39a-c WpueG. Leitsaetze BGH und BaFin-Praxis im Corporate Kanzlei. |
| `qa-information-requests` | Q&A- und Information-Request-Management in M&A-Transaktionen: DD-Team erhaelt schriftliche Datenraum-Fragen und muss konsistente Antworten mit Disclosure-Wirkung erstellen. Normen: § 311 Abs. 2 BGB, Disclosure-Praxis SPA, MAR Insider-Abg... |
| `rechtsprechungsrecherche` | Corporate-Rechtsprechungsrecherche: Sucht und bewertet Urteile für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. Liefert Fundstellenliste mit Aktenzeichen, Datum, Leitsatz-Paraphrase und Verwert... |
| `rechtsprechungsrecherche-spa-apa` | Corporate-Rechtsprechungsrecherche: Sucht und bewertet Urteile für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. Liefert Fundstellenliste mit Aktenzeichen, Datum, Leitsatz-Paraphrase und Verwert... |
| `regulatory-fdi-merger` | Anmeldepflichten Fusionskontrolle und FDI prüfen: M&A-Transaktion erfordert Clearance. Normen: §§ 35 ff. GWB (deutsches Fusionskontrollrecht), Art. 1 ff. FKVO (EU-Fusionskontrolle), AWG/AWV (Investitionsprüfung), SektSchV (Sektorschutz),... |
| `regulatory-fdi-restructuring-starug` | Anmeldepflichten Fusionskontrolle und FDI prüfen: M&A-Transaktion erfordert Clearance. Normen: §§ 35 ff. GWB (deutsches Fusionskontrollrecht), Art. 1 ff. FKVO (EU-Fusionskontrolle), AWG/AWV (Investitionsprüfung), SektSchV (Sektorschutz),... |
| `restructuring-starug` | StaRUG-Restrukturierungsplan und Insolvenzplan für distressed Unternehmen: Schuldner oder Berater plant außergerichtliche Sanierung oder Insolvenzplanverfahren. Normen: §§ 7 ff. StaRUG (Planarchitektur), §§ 217 ff. InsO (Insolvenzplan),... |
| `restructuring-starug-insolvenzplan` | StaRUG-Restrukturierungsplan und Insolvenzplan für distressed Unternehmen: Schuldner oder Berater plant außergerichtliche Sanierung oder Insolvenzplanverfahren. Normen: §§ 7 ff. StaRUG (Planarchitektur), §§ 217 ff. InsO (Insolvenzplan),... |
| `schuldschein-darlehen` | Prüft Schuldscheindarlehen in Corporate/M&A, Refinanzierung und Secondary Trades: Darlehensgeberregister, Zahlstelle, Abtretung, Zustimmung, Sicherheiten und Notice. |
| `schuldschein-darlehen-signing-closing` | Prüft Schuldscheindarlehen in Corporate/M&A, Refinanzierung und Secondary Trades: Darlehensgeberregister, Zahlstelle, Abtretung, Zustimmung, Sicherheiten und Notice im Corporate Kanzlei. |
| `signing-closing-conditions` | Signing und Closing Conditions verwalten: M&A-Transaktion naehert sich Signing oder Closing und alle CPs muessen erledigt sein. Normen: § 158 BGB (Bedingungseintritt), SPA Conditions Precedent, § 41 GWB (Vollzugsverbot). Prüfraster: CP-C... |
| `simulation-bidder-process` | Auktionsprozess und Bieter-Perspektive in M&A-Transaktionen simulieren: Verkaeufer-Kanzlei plant Bieter-Prozess oder Kaeufer bereitet NBO/BO vor. Normen: SPA, WpueG (Public M&A), Marktstandard M&A-Auktion. Prüfraster: Process Letter, Bie... |
| `simulation-bidder-steps-plan` | Auktionsprozess und Bieter-Perspektive in M&A-Transaktionen simulieren: Verkaeufer-Kanzlei plant Bieter-Prozess oder Kaeufer bereitet NBO/BO vor. Normen: SPA, WpueG (Public M&A), Marktstandard M&A-Auktion. Prüfraster: Process Letter, Bie... |
| `spa-apa-entwurf` | SPA (Share Purchase Agreement) oder APA (Asset Purchase Agreement) entwerfen und strukturieren aus Term Sheet und DD-Findings. Normen: §§ 433 ff. BGB (Kaufrecht), § 444 BGB (Gewaehrleistung), §§ 311 Abs. 2 und 280 BGB. Prüfraster: Kaufpr... |
| `steps-plan-pmo` | Steps Plan und Transaktions-PMO für M&A-Mandate erstellen: Deal-Team benoetigt Gesamtprojektplan mit Workstream-Koordination, CP-Tracking und Status-Reporting. Normen: SPA Closing Conditions, § 158 BGB. Prüfraster: Workstream-Matrix (Leg... |
| `tabellenreview-3d-datenraum` | Strukturierte Datentabellen aus M&A-Datenräumen prüfen und qualitaetssichern: Vertragslisten, Litigation-Tracker, IP-Register, HR-Listen auf Luecken, Inkonsistenzen und Offenlegungsrisiken. Normen: § 311 Abs. 2 BGB, Disclosure-Praxis, Ak... |
| `tabellenreview-3d-teaser-processdocs` | Strukturierte Datentabellen aus M&A-Datenräumen prüfen und qualitaetssichern: Vertragslisten, Litigation-Tracker, IP-Register, HR-Listen auf Luecken, Inkonsistenzen und Offenlegungsrisiken. Normen: § 311 Abs. 2 BGB, Disclosure-Praxis, Ak... |
| `teaser-im-processdocs` | Teaser, Information Memorandum und Prozessdokumente für M&A-Auktionsprozesse erstellen: Verkaeuferkanzlei oder Investmentbank benoetigt anonymisierten Teaser, IM und VDD. Normen: § 311 Abs. 2 BGB (vorvertragliche Haftung), MAR (Insiderin... |
| `transaktionsstruktur` | Transaktionsstruktur: Entwickelt und bewertet Transaktionsstrukturen für M&A (Share Deal, Asset Deal, Merger, Carve-out, Holding-Interposition). Normen: KStG, UmwStG, GrEStG, GmbHG, AktG. Leitentscheidungen BGH und BFH. |
| `transaktionsstruktur-translations` | Transaktionsstruktur: Entwickelt und bewertet Transaktionsstrukturen für M&A (Share Deal, Asset Deal, Merger, Carve-out, Holding-Interposition). Normen: KStG, UmwStG, GrEStG, GmbHG, AktG. Leitentscheidungen BGH und BFH im Corporate Kanzlei. |
| `translations` | Mehrsprachige Transaktionsdokumente in DE/EN erstellen und prüfen: Internationale M&A-Transaktion erfordert konsistente Terminologie in beiden Sprachen. Normen: § 184 GVG (Deutsch als Gerichtssprache), EGBGB Art. 10 ff. (Sprache des Rech... |
| `translations-multijurisdictional` | Mehrsprachige Transaktionsdokumente in DE/EN erstellen und prüfen: Internationale M&A-Transaktion erfordert konsistente Terminologie in beiden Sprachen. Normen: § 184 GVG (Deutsch als Gerichtssprache), EGBGB Art. 10 ff. (Sprache des Rech... |
| `umwandlungsrecht` | Umwandlungsrecht: Begleitet Verschmelzung, Spaltung, Formwechsel und Vermögensuebertragung nach UmwG. Normen: §§ 2-122 UmwG (Verschmelzung), §§ 123-173 UmwG (Spaltung), §§ 190-304 UmwG (Formwechsel). Schlüsselentscheidungen BGH und BayObLG. |
| `umwandlungsrecht-wi-insurance` | Umwandlungsrecht: Begleitet Verschmelzung, Spaltung, Formwechsel und Vermögensuebertragung nach UmwG. Normen: §§ 2-122 UmwG (Verschmelzung), §§ 123-173 UmwG (Spaltung), §§ 190-304 UmwG (Formwechsel). Schlüsselentscheidungen BGH und BayOb... |
| `umwandlungssteuerrecht` | Umwandlungssteuerrecht: Begleitet Verschmelzung, Spaltung und Formwechsel nach UmwStG auf Steuerneutralitaet, Buchwertfortführung, Sperrfristen, Verlustnutzung und Grunderwerbsteuer. Normen: §§ 11-25 UmwStG, §§ 1 ff. GrEStG, § 8c KStG. |
| `vertragsmarkup-key-agio` | Juristischen Markup für M&A-Vertraege und Key-Issues-Memo erstellen: Gegenpartei hat SPA/SHA/NDA/LOI-Entwurf uebersandt und muss kommentiert werden. Normen: §§ 305 ff. BGB (AGB-Kontrolle im B2B), Marktstandard DE/UK M&A. Prüfraster: Abwe... |
| `vertragsmarkup-key-issues` | Juristischen Markup für M&A-Vertraege und Key-Issues-Memo erstellen: Gegenpartei hat SPA/SHA/NDA/LOI-Entwurf uebersandt und muss kommentiert werden. Normen: §§ 305 ff. BGB (AGB-Kontrolle im B2B), Marktstandard DE/UK M&A. Prüfraster: Abwe... |
| `wi-insurance` | W&I-Versicherung (Warranty & Indemnity Insurance) strukturieren und prüfen: M&A-Berater braucht Policen-Analyse oder Underwriting-Vorbereitung. Normen: SPA Reps & Warranties, VVG, englisches Insurance-Recht (Lloydserfahrung). Prüfraster:... |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
