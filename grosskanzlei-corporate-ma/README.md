# Big-Law-Großkanzlei-Corporate-M&A-Plugin

Technischer Plugin-Name: `grosskanzlei-corporate-ma`.

Dies ist das freistehende Großkanzlei-Corporate/M&A-Plugin für den gesamten Transaktionslebenszyklus: Intake, Aktenanlage, Konflikt-/GwG-/Sanktionscheck, Datenraum, Due Diligence, Tabellenreview, Liquiditätsvorschau, Insolvenzreife, Q&A, SPA/APA, Disclosure Schedules, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing, XRechnung/ZUGFeRD-Vorbereitung, GoBD-Protokoll und Closing Bible.

**Wichtig:** Dieses Plugin funktioniert vollständig allein. Alle Kernabläufe, Hilfstabellen, Prüfungsschablonen und Workflows liegen im Plugin selbst; für die hier beschriebenen M&A-Workflows ist keine Zusatzinstallation nötig.

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

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **Grosskanzlei Corporate M&A Datenraum** | [testakte-grosskanzlei-corporate-ma-datenraum.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grosskanzlei-corporate-ma-datenraum.zip) |


## Freistehende Kernmodule

| Modul | Enthaltene Funktion |
| --- | --- |
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
