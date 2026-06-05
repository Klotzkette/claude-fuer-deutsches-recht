# Big-Law-Großkanzlei-Corporate/M&A-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`grosskanzlei-corporate-ma`) | [`grosskanzlei-corporate-ma.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grosskanzlei-corporate-ma.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |
| **Akte LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH** (`sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`) | [Gesamt-PDF lesen](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/gesamt-pdf/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger_gesamt.pdf) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |
| **Sanierungsgewinn im Insolvenzplan — Grossbach Druckguss & Präzision GmbH & Co. KG Erfurt (2026)** (`sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026/gesamt-pdf/sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026.zip) |
| **Sanierungsgewinn bei solventer GmbH-Liquidation — Strassburger Handelshof GmbH (Berlin-Charlottenburg)** (`sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026/gesamt-pdf/sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026.zip) |
| **Sanierungsgewinn im StaRUG-Plan — Pellbach Windenergie GmbH Brandenburg (2026)** (`sanierungsgewinn-starug-plan-windenergie-pellbach-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-starug-plan-windenergie-pellbach-2026/gesamt-pdf/sanierungsgewinn-starug-plan-windenergie-pellbach-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-starug-plan-windenergie-pellbach-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-starug-plan-windenergie-pellbach-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Technischer Plugin-Name: `grosskanzlei-corporate-ma`.

Dies ist das freistehende Großkanzlei-Corporate/M&A-Plugin für den gesamten Transaktionslebenszyklus: Intake, Aktenanlage, Konflikt-/GwG-/Sanktionscheck, Datenraum, Due Diligence, Tabellenreview, Liquiditätsvorschau, Insolvenzreife, Q&A, SPA/APA, Disclosure Schedules, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing, XRechnung/ZUGFeRD-Vorbereitung, GoBD-Protokoll und Closing Bible.

Für neue Nutzerinnen und Nutzer gibt es zusätzlich einen **Anfänger-/First-Year-Associate-Modus**: Das Plugin fragt bei Bedarf am Anfang, wie viel Führung gewünscht ist, erklärt Deal-Begriffe nur dort, wo sie gebraucht werden, zerlegt Aufgaben in kleine Schritte und setzt Senior-Review-Gates, bevor etwas an Mandanten, Gegenseite, Notar, Bank oder Behörde geht.

**Wichtig:** Dieses Plugin funktioniert vollständig allein. Alle Kernabläufe, Hilfstabellen, Prüfungsschablonen und Workflows liegen im Plugin selbst; für die hier beschriebenen M&A-Workflows ist keine Zusatzinstallation nötig.


## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `grosskanzlei-corporate-ma.zip` hochladen.
5. Mit einem konkreten Deal-Auftrag starten, zum Beispiel: `Starte das Corporate-M&A-Kommandocenter für diesen Datenraum.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

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

Automatisch generierte Komplett-Liste aller 196 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `beirat-abgrenzung-aufsichtsrat` | Beirat Abgrenzung Aufsichtsrat: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-amtszeit-und-rotation` | Beirat Amtszeit Und Rotation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-bank-sanierung-beratungsfunktion` | Beirat Bank Und Sanierung, Beirat Beratungsfunktion, Beirat Beschlussfassung, Beirat Beschlussmaengel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `beirat-bank-und-sanierung` | Beirat Bank Und Sanierung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-beratungsfunktion` | Beirat Beratungsfunktion: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-beschlussfassung` | Beirat Beschlussfassung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-beschlussmaengel` | Beirat Beschlussmaengel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-bestellung-und-abberufung` | Beirat Bestellung Und Abberufung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-budget-und-businessplan` | Beirat Budget Und Businessplan: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-compliance-und-internal-investigation` | Beirat Compliance Und Internal Investigation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-datenschutz-ki-deadlock-mechanik` | Beirat Datenschutz Und Ki, Beirat Deadlock Mechanik, Beirat Entscheidungsbefugnisse, Beirat Fakultativer Aufsichtsrat 52 Gmbhg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächste... |
| `beirat-datenschutz-und-ki` | Beirat Datenschutz Und KI: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-deadlock-mechanik` | Beirat Deadlock Mechanik: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-entscheidungsbefugnisse` | Beirat Entscheidungsbefugnisse: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-fakultativer-aufsichtsrat-52-gmbhg` | Beirat Fakultativer Aufsichtsrat 52 Gmbhg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-familiengesellschaft` | Beirat Familiengesellschaft: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-geschaeftsfuehrerabberufung` | Beirat Geschaeftsfuehrerabberufung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-geschaeftsfuehrerbestellung` | Beirat Geschaeftsfuehrerbestellung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-geschaeftsordnung` | Beirat Geschaeftsordnung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-geschaeftsordnung-immobilien` | Beirat Geschaeftsordnung, Beirat Immobilien Und Investitionen, Beirat Informationsrechte, Beirat Insolvenznaehe: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren O... |
| `beirat-gmbh-zustimmungskatalog` | Prüft und entwirft GmbH-Beiratsregeln für mittelständische und Corporate-Mandate: Vetorechte, Investorenschutz, Haftung, Protokoll, Deadlock und Geschäftsführerautonomie. |
| `beirat-immobilien-und-investitionen` | Beirat Immobilien Und Investitionen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-informationsrechte` | Beirat Informationsrechte: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-insolvenznaehe` | Beirat Insolvenznaehe: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-interessenkonflikte` | Beirat Interessenkonflikte: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-kaltstart-und-zielbild` | Beirat Kaltstart Und Zielbild: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `beirat-katalog-wesentlicher-geschaefte` | Beirat Katalog Wesentlicher Geschaefte: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-kontrollfunktion` | Beirat Kontrollfunktion: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-mitbestimmung-abgrenzung` | Beirat Mitbestimmung Abgrenzung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-mitbestimmung-abgrenzung-nachfolge` | Beirat Mitbestimmung Abgrenzung, Beirat Nachfolge, Beirat Private Equity Investor, Beirat Register Und Notar: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `beirat-musterklauseln` | Beirat Musterklauseln: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-nachfolge` | Beirat Nachfolge: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-private-equity-investor` | Beirat Private Equity Investor: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-red-team-satzung` | Beirat Red Team Satzung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-register-und-notar` | Beirat Register Und Notar: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-satzungsgrundlage` | Beirat Satzungsgrundlage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-sitzung-und-protokoll` | Beirat Sitzung Und Protokoll: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-startup-investor-director` | Beirat Startup Investor Director: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-streit-gesellschafter` | Beirat Streit Gesellschafter: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-streit-gesellschafter-transaktionen-ma` | Beirat Streit Gesellschafter, Beirat Transaktionen Ma, Beirat Verguetung, Beirat Verschwiegenheit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `beirat-transaktionen-ma` | Beirat Transaktionen M&A: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-verguetung` | Beirat Verguetung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-verschwiegenheit` | Beirat Verschwiegenheit: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-veto-rechte` | Beirat Veto Rechte: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `beirat-zustimmungsvorbehalte` | Beirat Zustimmungsvorbehalte: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `expert-calls-fair-disclosure-financing` | Grosskanzlei Corporate Ma Expert Calls Transkripte, Grosskanzlei Corporate Ma Fair Disclosure Knowledge, Grosskanzlei Corporate Ma Financing Security Documents, Grosskanzlei Corporate Ma Foreign Subsidies Regulation Fsr: wählt den konkre... |
| `gk-ma-lma-loan-transfer` | Prüft LMA-basierte Transfermechanik im syndizierten Kredit: Assignment, Novation, Transfer Certificate, Consent, Agent und Register. |
| `gk-ma-npl-portfolio-und-loan-to-own` | Strukturiert NPL-Portfoliokauf, distressed secondary loan trade, enforcement und Debt-Equity-Strategie. |
| `gk-ma-npl-schuldschein-darlehen` | Gk Ma Npl Portfolio Und Loan To Own, Gk Ma Schuldschein Darlehen Transfer, Gk Sanierungsgewinn 3a Estg Praxis Für Corporate Ma, Gk Sanierungsgewinn Bmf Ankoppelung Und Strategie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `gk-ma-schuldschein-darlehen-transfer` | Begleitet Übertragung von Schuldscheindarlehen in M&A, Refinanzierung, Distressed Debt und Portfoliotransaktionen. |
| `gk-sanierungsgewinn-3a-estg-praxis-corporate` | Praxisleitfaden zu § 3a EStG für das Corporate-/M&A-Team einer Großkanzlei. Erklärt die vier Tatbestandsmerkmale (Sanierungsbedürftigkeit, Sanierungsfähigkeit, Sanierungseignung des Schulderlasses, Sanierungsabsicht der Gläubiger) im Tra... |
| `gk-sanierungsgewinn-asset-deal-vs-share` | Strukturvergleich Asset Deal vs. Share Deal im Distressed-M&A mit Sanierungsgewinn-Bezug. Vergleicht Verlustvortrag-Schicksal, Anwendbarkeit § 3a EStG, § 8c KStG-Effekt, übertragende Sanierung nach §§ 163 InsO, § 613a BGB-Wirkung und Tax... |
| `gk-sanierungsgewinn-bmf-ankoppelung-strategie` | BMF-Ankoppelung und strategische Auseinandersetzung mit den Verwaltungsanweisungen zu § 3a EStG. Analysiert das BMF-Schreiben vom 27.04.2017 und nachfolgende Verlautbarungen sowie die Wirkungen des Wachstumschancengesetzes und weiterer G... |
| `gk-sanierungsgewinn-bond-restructuring` | Sanierungsgewinn in Bond-Restrukturierungen und bei Finanzgesellschaften. Behandelt die Besonderheiten der Anleihegläubiger-Strukturen, das Schuldverschreibungsgesetz, Mehrheitsentscheidungen der Anleihegläubigerversammlung, Lock-up Agre... |
| `gk-sanierungsgewinn-debt-equity-swap-spa` | Debt-Equity-Swap (DES) als Bestandteil einer M&A-Transaktion mit Sanierungsgewinn-Bezug. Beschreibt die Mechanik des DES, die steuerlichen Wirkungen auf Schuldnerseite (Sanierungsertrag, § 3a EStG) und Gläubigerseite (Forderungseinbringu... |
| `gk-sanierungsgewinn-eu-beihilfe-und-altmark` | EU-beihilferechtliche Prüfung von Sanierungsmaßnahmen nach Art. 107 AEUV. Behandelt die Sanierungsklausel § 8c Abs. 1a KStG als Beihilfegegenstand, die Anwendung der Altmark-Trans-Kriterien, die De-minimis-Verordnung und das Notifizierun... |
| `gk-sanierungsgewinn-forderungsverzicht-vs` | Konkurrenz und Wechselwirkung von Forderungsverzicht (§ 3a EStG) und schädlichem Beteiligungserwerb (§ 8c KStG). Beschreibt die fatale Konstellation, in der eine Sanierung mit Anteilseignerwechsel den Verlustvortrag vor seinem Einsatz im... |
| `gk-sanierungsgewinn-fruehe-mandantsteuerung-q` | Q-12-Frühwarn-Skill für Großkanzlei-Mandate mit absehbarem Sanierungsbedarf. Steuert die Mandantenkommunikation zwölf Monate vor der formellen Anzeige eines Restrukturierungsplans oder StaRUG-Verfahrens und bindet die Steuerseite (§ 3a E... |
| `gk-sanierungsgewinn-konzern-und-cross-border` | Sanierungsgewinn in Konzernstrukturen und bei grenzüberschreitenden Sanierungen. Behandelt Forderungsverzichte zwischen Konzerngesellschaften, organschaftliche Verflechtungen, Verlustnutzung im internationalen Konzern, Wechselwirkung mit... |
| `gk-sanierungsgewinn-private-equity` | Sanierungsgewinn im PE-Mandat. Adressiert PE-Investoren in der Rolle des Sanierungserwerbers oder Sanierungsexits, das Zusammenspiel von Management Equity Plan (MEP) und Sanierungsertrag, die steuerliche Behandlung von Sweet Equity und M... |
| `gk-sanierungsgewinn-stille-reserven-klausel` | Stille-Reserven-Klausel des § 8c Abs. 4 KStG und § 8d KStG als Schutzmechanismen für Verlustvorträge bei einem schädlichen Beteiligungserwerb. Beschreibt die Tatbestandsmerkmale, die Berechnungsmechanik, die Ermittlung der stillen Reserv... |
| `gk-sanierungsgewinn-tax-due-diligence` | Tax Due Diligence Modul für Distressed-M&A-Transaktionen mit Sanierungsgewinn-Bezug. Geht über die Standard-Tax-DD hinaus und prüft Verlustvorträge, Zinsvortrag, EBITDA-Vortrag, schwebende Außenprüfungen, vorhandene oder fehlende verbind... |
| `gk-sanierungsgewinn-tax-step-plan` | Tax Step Plan für komplexe Restrukturierungen mit Sanierungsgewinn-Bezug. Reihenfolge der Strukturschritte zwischen Kapitalmaßnahmen, Forderungsverzicht, Debt-Equity-Swap, Anteilsübertragung und Antragstellung nach § 3a EStG. Modelliert... |
| `gk-sanierungsgewinn-tax-warranty-tax` | Strukturierung von Tax Warranty und Tax Indemnity im SPA für Transaktionen mit Sanierungsgewinn-Risiko nach § 3a EStG. Adressiert die Verteilung des Risikos zwischen Verkäufer und Käufer für den Fall, dass die Steuerbefreiung versagt wir... |
| `gk-sanierungsgewinn-verlustvortraege-sanity` | Sanity-Check der Verlustvorträge im Distressed-Due-Diligence-Prozess. Modelliert den Verbrauch von körperschaft- und gewerbesteuerlichen Verlustvorträgen, Zinsvorträgen und EBITDA-Vorträgen durch einen prognostizierten Sanierungsertrag (... |
| `gk-sanierungsgewinn-vorbescheid-verbindliche` | Verbindliche Auskunft nach § 89 AO im Sanierungskontext. Beschreibt Antragsstruktur, Sachverhaltsdarstellung, Tatsachen- und Rechtsfragen, Bindungswirkung und Reichweite. Liefert Antrags-Template, Sachverhalts-Dossier-Struktur, Kommunika... |
| `grosskanzlei-corporate-beirat-haftung` | Beirat Haftung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `grosskanzlei-corporate-beirat-haftung-gk-sanierungsgewinn-debt` | Beirat Haftung / Gk Sanierungsgewinn Debt Equity Swap / Gk Sanierungsgewinn Fruehe Mandantsteuerung Q / Gk Sanierungsgewinn Bond Restructuring Finanzgesellschaften / 3 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule,... |
| `grosskanzlei-corporate-grosskanzlei-corporate-ma` | Grosskanzlei Corporate Ma Auction Process / Grosskanzlei Corporate Ma Authority Matrix / Grosskanzlei Corporate Ma Automation Monitoring / Grosskanzlei Corporate Ma Bank Consents / 3 weitere Module: führt durch diese fachlich verbundenen... |
| `grosskanzlei-corporate-grosskanzlei-corporate-ma-02` | Grosskanzlei Corporate Ma Datenqualitaet Xai / Grosskanzlei Corporate Ma Datenraum Aufbau / Grosskanzlei Corporate Ma Datenraum Gap / Grosskanzlei Corporate Ma Deal Intake / 3 weitere Module: führt durch diese fachlich verbundenen Arbeit... |
| `grosskanzlei-corporate-grosskanzlei-corporate-ma-03` | Grosskanzlei Corporate Ma Due Diligence / Grosskanzlei Corporate Ma Due Diligence / Grosskanzlei Corporate Ma Due Diligence / Grosskanzlei Corporate Ma Employment Works / 3 weitere Module: führt durch diese fachlich verbundenen Arbeitsmo... |
| `grosskanzlei-corporate-grosskanzlei-corporate-ma-04` | Grosskanzlei Corporate Ma Liability Limitations / Grosskanzlei Corporate Ma Litigation Disputes / Grosskanzlei Corporate Ma Locked Box / Grosskanzlei Corporate Ma Look And / 3 weitere Module: führt durch diese fachlich verbundenen Arbeit... |
| `grosskanzlei-corporate-ma` | Handelsregister-Abruf und Registerrecherche für M&A-Transaktionen: Anwendungsfall Anwalt recherchiert offiziellen Registerstand für Zielgesellschaft, Kaeufer-Holding, Komplementaer-GmbH oder Beteiligungsketten. §§ 8-10 GmbHG, §§ 29 ff. H... |
| `grosskanzlei-corporate-ma-02` | Corporate und M&A Rechtsprechungsrecherche: Anwendungsfall Anwalt braucht für Gutachten, Schriftsatz oder DD-Report relevante BGH-Rechtsprechung zu Organpflichten, Kapitalmarkt, Umwandlung oder Insolvenz. §§ 93 und 179a AktG, § 15 AktG V... |
| `grosskanzlei-corporate-ma-03` | Transaktionsstruktur für M&A entwickeln und Varianten bewerten: Anwendungsfall Mandant fragt welche Transaktionsstruktur für seinen Unternehmenskauf -verkauf oder Carve-out am besten passt. Share Deal Asset Deal Carve-out Joint Venture V... |
| `grosskanzlei-corporate-ma-04` | Umwandlungssteuerrecht Buchwertantrag steuerliche Rückwirkung und Verlustuntergang prüfen: Anwendungsfall Corporate-Team und Steuerteam muessen umwandlungssteuerliche Strukturentscheidung abstimmen. §§ 20-24 UmwStG Einbringung, § 8c KStG... |
| `grosskanzlei-corporate-ma-ai-vdr-classifier` | AI VDR Classifier: klassifiziert Datenraumdokumente, erkennt Dokumentfamilien, fehlende Anlagen, Widersprueche, Dubletten, Clean-Room-Bedarf und Pruefprioritaeten. |
| `grosskanzlei-corporate-ma-aktenanlage` | Grosskanzlei Corporate Ma Wi Insurance, Grosskanzlei Ma Aktenanlage, Grosskanzlei Ma Insolvenzreife, Grosskanzlei Ma Liquiditaetsvorschau: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `grosskanzlei-corporate-ma-ancillary-documents` | Ancillary Documents, TSA und SLA Skill: baut Nebenvertragslandschaft fuer M&A, einschliesslich Transitional Services, IP-License, Supply, Lease, Escrow und Management Agreements. |
| `grosskanzlei-corporate-ma-anfaenger-modus` | Anfänger- und First-Year-Associate-Modus für Großkanzlei Corporate/M&A: fragt Erfahrungslevel, Deal-Phase, Aufgabe, Frist, Unterlagen und gewünschte Führung ab; erklärt Begriffe, zerlegt Aufgaben in kleine Schritte, schlägt passende Plug... |
| `grosskanzlei-corporate-ma-antitrust-gun` | Antitrust, Gun-Jumping und Clean-Team Spezialist: prueft Wettbewerberkontakte, Informationsaustausch, Vollzugsverbot, Integration Planning und Clean-Team-Design. |
| `grosskanzlei-corporate-ma-auction-process` | Auction Process Letter Generator: erstellt und prueft Prozessbriefe fuer strukturierte Verkaufs- und Bieterverfahren mit Deadlines, Bid Requirements und Verfahrensregeln. |
| `grosskanzlei-corporate-ma-authority-matrix` | Authority Matrix und Approvals Skill: prueft Zeichnungsberechtigungen, Gremienkompetenzen, Vollmachten, Gesellschafterbeschluesse, Board Consents und interne Freigaben. |
| `grosskanzlei-corporate-ma-automation` | Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen. §§ 35 ff. GWB Karte... |
| `grosskanzlei-corporate-ma-bank-consents` | Bank Consents und Change-of-Control in Finanzierungsvertraegen: erkennt Consent-Pflichten, Default-Risiken, Waiver-Bedarf und Closing-CPs. |
| `grosskanzlei-corporate-ma-bidder-instructions` | Bidder Instructions und VDR Rules fuer grosse M&A-Prozesse: formuliert Datenraumregeln, Q&A-Disziplin, Upload-Standards, Clean-Room-Grenzen und Sanktionen bei Prozessverstoessen. |
| `grosskanzlei-corporate-ma-billing-narratives` | Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss taugliche Time Narratives Phasenbudgets Workstream-Rechnungen Cap- und Success-Fee-Hinweise erstellen. § 3a RVG Stun... |
| `grosskanzlei-corporate-ma-board-consents` | Board Consents, Minutes und Resolutions fuer M&A: erstellt Beschlussvorlagen, Protokolle, Umlaufbeschluesse und Entscheidungsunterlagen mit Business-Judgment-Absicherung. |
| `grosskanzlei-corporate-ma-board-paper` | Board Paper und Business Judgment Rule Prüfung für M&A-Entscheidungen: Anwendungsfall Vorstand AG Geschäftsführer GmbH oder Aufsichtsrat muss Transaktionsentscheidung formal absichern. § 93 Abs. 1 Satz 2 AktG Business Judgment Rule Infor... |
| `grosskanzlei-corporate-ma-cap-table-carve-out` | Grosskanzlei Corporate Ma Board Paper Business Judgment, Grosskanzlei Corporate Ma Cap Table Ownership Chain, Grosskanzlei Corporate Ma Carve Out Separation Tsa, Grosskanzlei Corporate Ma Client Update Pack: wählt den konkreten Prüfpfad,... |
| `grosskanzlei-corporate-ma-cap-table-ownership` | Cap Table und Ownership Chain Analyzer: rekonstruiert Beteiligungsketten, wirtschaftliche Berechtigte, Optionen, VSOP/ESOP, Wandeldarlehen, Gesellschafterlisten und Registerlage. |
| `grosskanzlei-corporate-ma-carve-out` | Carve-out Separation und TSA Deep Dive: plant Herausloesung von Geschaeftsbereichen, Assets, Mitarbeitern, IT, Daten, Genehmigungen und Uebergangsleistungen. |
| `grosskanzlei-corporate-ma-client-update-pack` | Client Update Pack fuer M&A-Mandanten: erstellt laufende Statusupdates, Weekly Reports, Entscheidungsvorlagen, Risikoampeln und naechste Mandanten-Requests. |
| `grosskanzlei-corporate-ma-closing-bible` | Closing Bible und Deal-Archiv erstellen: Anwendungsfall Mandant oder Counsel braucht nach Signing/Closing vollständige Dokumentensammlung aller executed Agreements, Signaturseiten und Registerbelege. §§ 433 ff. BGB SPA-Pflichten, Notarre... |
| `grosskanzlei-corporate-ma-conflict-gwg` | Mandatsannahme-Prüfung im Corporate/M&A-Mandat: Interessenkonflikte nach § 43a BRAO, Geldwäschegesetz-Prüfung wirtschaftlich Berechtigter nach § 3 GwG, Sanktionsscreening nach AWG und EU-Verordnungen. Anwendungsfall neue Transaktionsmand... |
| `grosskanzlei-corporate-ma-cp-beirat` | Grosskanzlei Corporate Ma Rechtsprechungsrecherche, Grosskanzlei Ma Fristen Cp Kalender, Beirat Musterklauseln, Gk Sanierungsgewinn Stille Reserven Klausel 8c Iv Kstg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `grosskanzlei-corporate-ma-data-protection` | Data Protection Transfer DD fuer M&A: prueft DSGVO-Risiken, Datenuebertragung, Datenraumzugriff, Kunden-/Mitarbeiterdaten, Drittlandtransfer und Post-Closing-Migration. |
| `grosskanzlei-corporate-ma-datenqualitaet-xai` | KI-Qualitaetskontrolle und Halluzinations-Absicherung in M&A-Transaktionen: Anwendungsfall KI-generierte DD-Berichte, Klauseln oder Recherchen sollen auf Datenqualitaet, Bias und Black-Box-Risiken geprüft werden. Art. 22 DSGVO automatisi... |
| `grosskanzlei-corporate-ma-datenraum-aufbau` | Due Diligence Datenraum strukturieren und bestücken: Anwendungsfall Mandant bereitet Verkaufsprozess vor oder Buyer-Team benoetigt strukturierten Datenraum für Private M&A, Public M&A, Carve-out oder Distressed-Prozesse. §§ 433 ff. BGB,... |
| `grosskanzlei-corporate-ma-datenraum-gap-clean` | Datenraum-Lueckenanalyse und Clean-Room-Protokoll für M&A Due Diligence: Anwendungsfall Anwalt oder Mandant stellt fest dass Datenraum Luecken hat oder sensible Wettbewerbsdaten nur unter Clean-Room-Bedingungen geteilt werden koennen. §§... |
| `grosskanzlei-corporate-ma-deal-intake` | Neues M&A-Mandat aufnehmen und strukturieren: Anwendungsfall Partner oder Associate erhaelt Erstanfrage zu einer Transaktion und muss Deal-Profil, Rolle, Parteien, Zeitplan und Workstreams erfassen. §§ 3a RVG Honorar, § 43a BRAO Konflikt... |
| `grosskanzlei-corporate-ma-deal-os` | Deal-OS-Orchestrator fuer grosse Corporate- und M&A-Mandate: steuert Deal-Phase, Rolle, Fristen, Workstreams, Risikoampeln, Padlet-Canvas, Tabellenmatrix, Junior-Fuehrung und naechste Deliverables aus einer Hand. |
| `grosskanzlei-corporate-ma-deal-team-staffing` | Deal-Team-Besetzung und Staffing-Plan für Corporate/M&A-Transaktionen: Anwendungsfall Senior-Partner oder Team-Lead muss Workstreams Anwalt, Counsel, Associate, Paralegals und externe Spezialisten zuweisen. §§ 43a BRAO Interessenkonflikt... |
| `grosskanzlei-corporate-ma-disclosure` | Disclosure Schedules und Guarantees-Abgleich im SPA/APA: Anwendungsfall Verkaeufer-Anwalt erstellt Disclosure Schedules zur Einschraenkung von Reps and Warranties oder Kaeufer prüft ob Disclosure ausreichend ist. §§ 433 ff. BGB, SPA Disc... |
| `grosskanzlei-corporate-ma-distressed-ma` | Distressed M&A Transaktion begleiten: Anwendungsfall Unternehmen in Krise oder Insolvenz soll verkauft werden oder Investor prüft Erwerb notleidender Vermögenswerte. §§ 17-19 InsO Insolvenztatbestaende, § 1 StaRUG Sanierung, §§ 433 ff. B... |
| `grosskanzlei-corporate-ma-due-diligence` | Commercial Contracts Due Diligence im M&A-Datenraum: Anwendungsfall Kaeufer-Anwalt prüft wesentliche Kundenvertraege, Lieferantenvertraege, IP-Lizenzen, Change-of-Control-Klauseln und Kündigungsrechte. §§ 433 ff. BGB SPA-Garantien, §§ 30... |
| `grosskanzlei-corporate-ma-due-diligence-02` | Due Diligence Report erstellen und strukturieren: Anwendungsfall After DD-Phase muss Anwalt einen umfassenden DD-Bericht für Kaeufer-Management, Investitionskomitee oder Finanzierungsbank erstellen. SPA-Berichtspflichten, § 93 AktG Infor... |
| `grosskanzlei-corporate-ma-due-diligence-legal` | Legal Due Diligence im M&A-Prozess: Anwendungsfall Kaeufer-Anwalt prüft Corporate-Unterlagen, Rechtsstreitigkeiten, Regulatory-Status, Arbeitsrecht und IP der Zielgesellschaft. §§ 433 ff. BGB SPA-Garantien, § 93 AktG Organpflichten. Prüf... |
| `grosskanzlei-corporate-ma-employment-works` | Employment, Works Council und Betriebsuebergang Skill: prueft Arbeitnehmer, Betriebsrat, Mitbestimmung, § 613a BGB, Retention, Bonus, Change of Control und Restrukturierung. |
| `grosskanzlei-corporate-ma-environmental-esg` | Environmental, ESG und Compliance DD fuer M&A: prueft Umweltgenehmigungen, Lieferketten, Sanktionen, Anti-Korruption, ESG-Offenlegung und Reputationsrisiken. |
| `grosskanzlei-corporate-ma-exclusivity-no-shop` | Exclusivity, No-Shop und Prozessdisziplin Skill: entwirft und prueft Exklusivitaet, Break Fees, Fiduciary Out, Prozessverstoss und Kommunikationsregeln. |
| `grosskanzlei-corporate-ma-executive-summary` | Executive Summary und Onepager fuer Board, Investment Committee und Partner: verdichtet komplexe M&A-Befunde in klare, entscheidbare, nicht ueberverkaufte Kurzformate. |
| `grosskanzlei-corporate-ma-expert-calls` | Expert Calls und Transkript-Auswertung für M&A Due Diligence: Anwendungsfall Deal-Team hat Experteninterviews oder Management-Presentations transkribiert und muss Kernaussagen strukturiert extrahieren. MAR Vertraulichkeit, §§ 433 ff. BGB... |
| `grosskanzlei-corporate-ma-fair-disclosure` | Fair Disclosure und Knowledge-Qualifikation in M&A-Vertraegen: Anwendungsfall Vertragsparteien verhandeln Wissenszurechnung, Kenntnis-Definitionen und Fair-Disclosure-Mechanismus im SPA. §§ 433 ff. BGB, § 442 BGB Kaeufer-Kenntnis. Prüfra... |
| `grosskanzlei-corporate-ma-financing-security` | Financing und Security Documents Skill: prueft Akquisitionsfinanzierung, Sicherheiten, Intercreditor, Conditions, Funds Flow und Bank-Deliverables. |
| `grosskanzlei-corporate-ma-foreign-subsidies` | Foreign Subsidies Regulation FSR Skill: prueft EU-FSR-Relevanz, Drittstaaten-Finanzbeitraege, Transaktionsdaten, Filing-Risiko und Koordination mit Merger Control/FDI. |
| `grosskanzlei-corporate-ma-freundlicher` | Freundlicher M&A-Deal-Copilot für junge Anwaelte und Associates: Anwendungsfall Junior-Associate oder Trainee arbeitet an erster groesserer Corporate-Transaktion und braucht verstaendnisbasierte Begleitung ohne Vorwurf. M&A-Praxis, SPA S... |
| `grosskanzlei-corporate-ma-gesellschaftsrecht` | Corporate Housekeeping und Register-Prüfung im M&A-Kontext: Anwendungsfall Anwalt prüft für Kaeufer oder Verkaeufer HRB/HRA-Eintrag, Gesellschafterlisten, Satzungen, Beschluesse, Vollmachten und Organstellung der Zielgesellschaft. §§ 8-1... |
| `grosskanzlei-corporate-ma-insurance-risk-dd` | Insurance Risk DD und Policies Check: prueft D&O, Cyber, Product Liability, Warranty, Property, Claims History und Versicherbarkeit von Risiken. |
| `grosskanzlei-corporate-ma-ip-it-data-assets` | IP, IT und Data Assets Due Diligence: prueft Rechteketten, Software, Open Source, Lizenzen, Datenrechte, KI-Assets, Cyberrisiken und Change-of-Control. |
| `grosskanzlei-corporate-ma-ip-it-junior-mentor` | Grosskanzlei Corporate Ma Insurance Risk Dd, Grosskanzlei Corporate Ma Ip It Data Assets Dd, Grosskanzlei Corporate Ma Junior Mentor Training Loop, Grosskanzlei Corporate Ma Ki Governance Berufsrecht: wählt den konkreten Prüfpfad, trennt... |
| `grosskanzlei-corporate-ma-junior-mentor` | Junior-Mentor fuer Corporate/M&A: erklaert Begriffe, zerlegt Aufgaben in First-Year-Schritte, prueft Entwuerfe freundlich, staerkt Schwachstellen und gibt Senior-Review-taugliches Feedback. |
| `grosskanzlei-corporate-ma-kaltstart` | Kanzlei- und Mandantenpraeferenzen für Corporate/M&A erfassen: Anwendungsfall bei erstem Einsatz des Plugins konfiguriert Anwalt oder Kanzlei Deal-Playbooks, Materiality-Schwellen, Reporting-Standards, Abrechnungsmodell und KI-Governance... |
| `grosskanzlei-corporate-ma-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Großkanzlei-Corporate/M&A-Plugin. Fragt Rolle, Erfahrungslevel, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klar... |
| `grosskanzlei-corporate-ma-kg` | KG und Personengesellschaften in M&A-Transaktionen: Anwendungsfall Mandat betrifft Kommanditanteilsuebertragung, Fondsvehikel-Struktur, Kommanditistenwechsel oder Einbringung in KG. §§ 161-177 HGB, MoPeG, §§ 20-24 UmwStG Einbringung. Prü... |
| `grosskanzlei-corporate-ma-ki-governance` | KI-Einsatz im Transaktionsmandat berufsrechtlich absichern: Anwendungsfall Anwalt moechte KI-Tools für Datenraumanalyse oder Vertragsentwurf nutzen und muss Mandatsgeheimnis, Datenschutz und KI-VO-Betreiberpflichten einhalten. § 43a BRAO... |
| `grosskanzlei-corporate-ma-kommandocenter` | Deal-Kommandocenter Corporate/M&A: Schnellstart und Fallrouting für alle Transaktionsphasen. Anwendungsfall Anwalt gibt Kuerzel, Dokument oder Sachverhaltssatz ein und wird in richtigen Deal-Skill geleitet. SPA Share Purchase Agreement,... |
| `grosskanzlei-corporate-ma-legal-fact-book` | Legal Fact Book Generator: erstellt ein sell-side-taugliches Faktenbuch mit Corporate, Material Contracts, Litigation, Employment, IP, Regulatory, Real Estate und Compliance. |
| `grosskanzlei-corporate-ma-lessons-learned` | Lessons Learned und Deal Post-Mortem Skill: analysiert abgeschlossene Deals, Fehler, Prozessbremsen, gute Klauseln, Knowledge-Management und Playbook-Updates. |
| `grosskanzlei-corporate-ma-liability` | Liability Limitations, Basket, De Minimis und Cap: verhandelt Haftungsbegrenzungen, Ausschluesse, Verjaehrung und Buyer Protections im SPA. |
| `grosskanzlei-corporate-ma-litigation-disputes` | Litigation und Disputes DD: prueft Prozesse, Schiedsverfahren, Verwaltungsverfahren, Threatened Claims, Rueckstellungen und SPA-Risikotransfer. |
| `grosskanzlei-corporate-ma-locked-box` | Locked Box und Completion Accounts Spezialist: vergleicht Kaufpreismechaniken, Leakage, Working Capital, Net Debt, Accounts-Prozess und Dispute-Mechanik. |
| `grosskanzlei-corporate-ma-look-and-feel` | Corporate-Deal-Workspace Darstellung und Ausgabeformat: Anwendungsfall alle sichtbaren Outputs sollen im einheitlichen M&A-Kanzleistil erscheinen — ruhig, edel, deal-informationsdicht ohne Marketing-Ton. Big-Law-Standard, Partnerqualitae... |
| `grosskanzlei-corporate-ma-mac-ordinary-course` | MAC, Ordinary Course und Interim Covenants: prueft Signing-to-Closing-Pflichten, Zustimmungsvorbehalte, Notice-Prozesse und Covenant-Verstoesse. |
| `grosskanzlei-corporate-ma-management` | Management-Presentation-Prep: bereitet Fragen, Red-Flags, Sprechzettel, Follow-up-Requests und Expert-Call-Protokolle fuer M&A-Managementtermine vor. |
| `grosskanzlei-corporate-ma-matter-file` | Deal-Akte und Matter-Workspace anlegen: Anwendungsfall bei Mandatsannahme wird strukturierter Matter-Workspace benoetigt mit allen Workstreams, Datenraumspiegel, Register-Links, Q&A-Tracker und Closing-Archiv. § 43a BRAO Aktenführung, Go... |
| `grosskanzlei-corporate-ma-nda-clean-team` | NDA- und Clean-Team-Protokoll fuer Bieterprozesse: prueft Vertraulichkeit, kartellrechtliche Informationsgrenzen, Clean-Room-Zugang, Datenklassifikation und Prozessdisziplin. |
| `grosskanzlei-corporate-ma-negotiation` | Verhandlungsstrategie und Battlecards fuer SPA, APA, Term Sheet, W&I, CPs und Disclosure: erstellt Position, Fallbacks, rote Linien, Gegenargumente und Formulierungsvorschlaege. |
| `grosskanzlei-corporate-ma-notar-vollmachte-02` | Notar-, Vollmachts- und Signaturmechanik fuer Corporate/M&A: plant Beurkundung, notarielle Vollmachten, Legalisation/Apostille, elektronische Signatur und Closing-Mechanik. |
| `grosskanzlei-corporate-ma-notar-vollmachten` | Grosskanzlei Corporate Ma Negotiation Strategy Battlecards, Grosskanzlei Corporate Ma Notar Vollmachten Signaturmechanik, Grosskanzlei Corporate Ma Outside In Target Screening, Grosskanzlei Corporate Ma Padlet Deal Canvas: wählt den konk... |
| `grosskanzlei-corporate-ma-outside-target` | Zielobjekt-Screening und Pipeline-Analyse aus öffentlichen Quellen: Anwendungsfall Mandant oder Deal-Team sucht geeignete Akquisitionsziele und muss fruehe Analyse aus Registern, Finanzdaten, Nachrichten und Branchenhinweisen erstellen.... |
| `grosskanzlei-corporate-ma-padlet-deal-canvas` | Interaktiver Deal-Padlet-Canvas fuer Corporate/M&A: visualisiert Parteien, Struktur, Dokumente, Risiken, Q&A, CPs, Gremien, Register, To-dos und Entscheidungspunkte als bewegliches Arbeitsboard. |
| `grosskanzlei-corporate-ma-pension-bav` | Pension und bAV Liabilities in M&A: prueft Pensionszusagen, CTA, PSV, Bilanzierung, Change of Control, Versorgungssysteme und SPA-Risikoallokation. |
| `grosskanzlei-corporate-ma-post-closing` | Post-Merger-Integration planen und begleiten: Anwendungsfall nach Closing muessen DD-Findings, SPA-Pflichten und Earn-Out-Mechanismen in PMI-Plan uebersetzt und Betriebsuebergang sowie Registeranmeldungen abgewickelt werden. § 613a BGB B... |
| `grosskanzlei-corporate-ma-public-ma` | Public M&A und Kapitalmarkt-Compliance bei boersennotierten Transaktionen: Anwendungsfall Anwalt begleitet Übernahmeangebot, Pflichtangebot oder Squeeze-Out § 327a AktG bei boersennotierter Zielgesellschaft. WpUEG Angebotsunterlage, MAR... |
| `grosskanzlei-corporate-ma-purchase-price` | Purchase Price Adjustment und Earn-out Skill: modelliert Anpassungen, Earn-out-KPIs, Manipulationsschutz, Covenants und Streitbeilegung. |
| `grosskanzlei-corporate-ma-qa-information` | Q&A-Prozess und Information Requests in der Due Diligence steuern: Anwendungsfall Deal-Team muss aus DD-Analyse gezielte Fragen an Verkaeufer formulieren, priorisieren und Antworten gegen Datenraum-Belege prüfen. SPA Due Diligence Prozes... |
| `grosskanzlei-corporate-ma-real-estate-leases` | Real Estate, Leases und Sites Due Diligence: prueft Grundstuecke, Mietvertraege, Belastungen, Genehmigungen, Umwelt, Change-of-Control und Standortkritikalitaet. |
| `grosskanzlei-corporate-ma-real-estate-redline` | Grosskanzlei Corporate Ma Purchase Price Adjustment Earn Out, Grosskanzlei Corporate Ma Real Estate Leases Sites, Grosskanzlei Corporate Ma Redline Comparison Automation, Grosskanzlei Corporate Ma Register Filings Implementation: wählt d... |
| `grosskanzlei-corporate-ma-redline-comparison` | Redline Comparison Automation fuer M&A-Dokumente: vergleicht Markups, extrahiert Key Issues, erkennt stille Aenderungen und baut Antwortvorschlaege. |
| `grosskanzlei-corporate-ma-register-filings` | Register Filings und Implementation Manager: plant Handelsregister, Transparenzregister, Gesellschafterlisten, Umwandlungsanmeldungen, Notarvollzug und Post-Closing-Filings. |
| `grosskanzlei-corporate-ma-regulatory-fdi` | Fusionskontrolle und FDI-Investitionsprüfung für M&A-Transaktionen: Anwendungsfall Signing naht und Deal-Team prüft ob Kartellrechts-Freigabe oder AWV-Prüfung benoetigt wird. §§ 35-44 GWB inlaendische Fusionskontrolle, Art. 4 FKVO EU-Fus... |
| `grosskanzlei-corporate-ma-restructuring` | StaRUG-Restrukturierung und Insolvenzplanverfahren begleiten: Anwendungsfall Unternehmen mit drohender Zahlungsunfähigkeit prüft Restrukturierungsoptionen einschließlich StaRUG-Plan, praeventiyen Restrukturierungsrahmen oder Insolvenzpla... |
| `grosskanzlei-corporate-ma-risk-heatmap-board` | Risk Heatmap Board fuer Corporate/M&A: visualisiert Risiken nach Wahrscheinlichkeit, Impact, Verhandelbarkeit, Quellenstaerke, Owner und Deal-Blocker-Potential. |
| `grosskanzlei-corporate-ma-sector-regulatory` | Sector Regulatory DD fuer regulierte Targets: prueft Erlaubnisse, Aufsicht, Change-of-Control, Inhaberqualifikation, Meldepflichten und regulatorische CPs. |
| `grosskanzlei-corporate-ma-shareholder-loan-02` | Shareholder Loans, Rangruecktritt und Gesellschafterfinanzierung im M&A: prueft Darlehen, Nachrang, Insolvenznahe, Debt Pushdown, Verzicht und SPA-Behandlung. |
| `grosskanzlei-corporate-ma-shareholder-loans` | Grosskanzlei Corporate Ma Sector Regulatory Dd, Grosskanzlei Corporate Ma Shareholder Loans Subordination, Grosskanzlei Corporate Ma Signing Closing Conditions, Grosskanzlei Corporate Ma Signing Closing Room Manager: wählt den konkreten... |
| `grosskanzlei-corporate-ma-signing-closing` | Signing-to-Closing-Prozess mit Conditions Precedent für M&A-Transaktionen: Anwendungsfall nach Signing muessen alle Closing-Bedingungen erfuellt und Closing Deliverables koordiniert werden. SPA Closing Conditions, § 179a AktG Hauptversam... |
| `grosskanzlei-corporate-ma-signing-closing-02` | Signing- und Closing-Room-Manager: koordiniert Execution-Versionen, Signaturseiten, CPs, Bring-downs, Funds Flow, Closing Minutes und Post-Closing-Ablage. |
| `grosskanzlei-corporate-ma-simulation-bidder` | M&A-Bieterprozess simulieren für Training und Mandatsvorbereitung: Anwendungsfall Junior-Anwalt oder Deal-Team ueben beschleunigten Transaktions-Tag mit Datenraum Q&A SPA-Markup CP-Liste und Board-Call. SPA Share Purchase Agreement, Due... |
| `grosskanzlei-corporate-ma-spa-apa-entwurf` | SPA Share Purchase Agreement und APA Asset Purchase Agreement entwerfen: Anwendungsfall Anwalt erstellt Kaufvertrag für Share Deal oder Asset Deal aus Term Sheet DD-Findings und Transaktionsstruktur. §§ 433 ff. BGB Kaufrecht, § 15 GmbHG... |
| `grosskanzlei-corporate-ma-specific` | Specific Indemnities und Risk Transfer Skill: entwickelt Sonderfreistellungen, Escrow, W&I-Schnittstellen, Tax Deeds und Risikoallokation fuer erkannte Findings. |
| `grosskanzlei-corporate-ma-steps-plan-pmo` | Deal-PMO und Steps-Plan für Pre-Signing bis Post-Closing: Anwendungsfall Transaktion braucht praezisen Aufgaben- und Zeitplan aus Vertraegen, DD-Unterlagen und Gremienunterlagen extrahiert. SPA Closing Conditions, CPs Conditions Preceden... |
| `grosskanzlei-corporate-ma-tabellen-matrix` | Tabellen- und Matrix-Fabrik fuer M&A: baut DD-Grids, Risk Heatmaps, Issue Lists, CP-Tracker, Authority-Matrizen, Disclosure-Schedules und Registerabgleich als direkt nutzbare Tabellen. |
| `grosskanzlei-corporate-ma-tabellenreview-3d` | 3D-Tabellenreview M&A-Datenraum: Dokumente Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft verbinden: Anwendungsfall Deal-Team prüft Datenraum-Dokumente systematisch mit internem Review-Cube nach mehreren Workstream-Perspektiven. SP... |
| `grosskanzlei-corporate-ma-tax-structuring` | Tax Structuring General fuer Corporate/M&A: fuehrt steuerliche Strukturthemen, UmwStG-Schnittstellen, Verlustvortraege, Grunderwerbsteuer, Quellensteuer und SPA-Tax-Klauseln zusammen. |
| `grosskanzlei-corporate-ma-teaser-processdocs` | Investment Teaser Information Memorandum und Prozessdokumente erstellen: Anwendungsfall Sell-side-Mandat braucht Teaser für erste Bieterkontakte, Information Memorandum und Process Letter für strukturierten Auktionsprozess. SPA M&A-Proze... |
| `grosskanzlei-corporate-ma-term-sheet` | Grosskanzlei Corporate Ma Teaser Im Processdocs, Grosskanzlei Corporate Ma Term Sheet To Spa Bridge, Grosskanzlei Corporate Ma Translations Multijurisdictional, Grosskanzlei Corporate Ma Transparenzregister Ubo Chain: wählt den konkreten... |
| `grosskanzlei-corporate-ma-term-sheet-to-spa` | Term-Sheet-to-SPA-Bridge: uebersetzt Term Sheet, LOI oder MoU in SPA-/APA-Struktur, Klauselarchitektur, offene Punkte und Drafting-Anweisungen. |
| `grosskanzlei-corporate-ma-translations` | Multi-Jurisdiction-Koordination und Übersetzungen in grenzüberschreitenden M&A-Transaktionen: Anwendungsfall Transaktion mit mehreren Laendern erfordert Koordination lokaler Counsel, Übersetzungen und Rechtsvergleich. Internationales Pri... |
| `grosskanzlei-corporate-ma-transparenzregister` | Transparenzregister- und UBO-Chain-Check fuer M&A: prueft wirtschaftlich Berechtigte, Kontrollketten, PEP-/Sanktionsschnittstellen und Dokumentationsbedarf. |
| `grosskanzlei-corporate-ma-umwandlungsrecht` | Umwandlungsrecht Verschmelzung Spaltung Formwechsel und Carve-outs nach UmwG bearbeiten: Anwendungsfall Mandant plant Verschmelzung zweier GmbHs Ausgliederung eines Geschäftsbereichs oder Formwechsel AG zu GmbH im Rahmen einer Transaktio... |
| `grosskanzlei-corporate-ma-vendor-due` | Vendor Due Diligence und Vendor Assistance: strukturiert Sell-side-Pruefung, Datenraumreife, Legal Fact Book, Issue Remediation und Bieterkommunikation. |
| `grosskanzlei-corporate-ma-versand-signing` | Transaktionsoutput, Signing-Pack und Versand vorbereiten: Anwendungsfall Closing oder Signing naht und Anwalt muss Markups, Board Papers, Signing Packs, Closing Deliverables und beA/Notar/Email-Versand koordinieren. §§ 125 ff. BGB Formvo... |
| `grosskanzlei-corporate-ma-vertragsmarkup-key` | SPA/APA/NDA Markup analysieren und Key Issues List erstellen: Anwendungsfall Anwalt erhaelt Gegenentwurf oder Markup und muss wirtschaftlich relevante Abweichungen strukturieren und Gegenvorschlaege formulieren. §§ 433 ff. BGB Kaufrecht,... |
| `grosskanzlei-corporate-ma-warranty-catalogue` | Warranty Catalogue Negotiation: baut und prueft Garantiepakete fuer Corporate, Accounts, Tax, Employment, IP, IT, Data, Compliance, Real Estate und Material Contracts. |
| `grosskanzlei-corporate-ma-weakness-diagnostic` | Schwaechen-Diagnose-Coach fuer Deal-Arbeit: erkennt juristisch duenne Argumente, fehlende Fakten, falsche Begriffe, zu schwache Klauseln, unklare Risiken und baut daraus einen konkreten Verbesserungsplan. |
| `grosskanzlei-corporate-ma-wi-insurance` | W&I-Versicherung Warranty and Indemnity in M&A-Transaktionen: Anwendungsfall Kaeufer oder Verkaeufer erwägt W&I-Versicherung für SPA-Garantien und muss Underwriting-Prozess, DD-Berichts-Anforderungen und Deckungsausschluesse klaeren. SPA... |
| `grosskanzlei-gk-sanierungsgewinn-corporate-ma` | Gk Sanierungsgewinn Verlustvortraege Sanity Im Dd Prozess, Grosskanzlei Corporate Ma Deal Os Orchestrator, Grosskanzlei Corporate Ma Kg Personengesellschaften, Grosskanzlei Corporate Ma Matter File: wählt den konkreten Prüfpfad, trennt F... |
| `grosskanzlei-gk-sanierungsgewinn-tax-step` | Gk Sanierungsgewinn Tax Due Diligence Im Distressed Mna, Gk Sanierungsgewinn Tax Step Plan Restrukturierung, Gk Sanierungsgewinn Vorbescheid Und Verbindliche Auskunft, Grosskanzlei Corporate Ma Ai Vdr Classifier: wählt den konkreten Prüf... |
| `grosskanzlei-ma-aktenanlage` | Freistehende M&A-Aktenanlage ohne externes Plugin: Anwendungsfall neue Corporate-Transaktion wird aufgenommen und Deal-Akte mit Aktenzeichen Parteienregister Ordnerstruktur Datenraumspiegel und Closing-Bible-Grundgeruest wird benoetigt.... |
| `grosskanzlei-ma-erechnung-gobd` | Freistehender Billing- GoBD- und E-Rechnungsfür M&A-Mandate: Anwendungsfall Kanzlei muss für M&A-Mandat GoBD-konforme Rechnung XRechnung-XML und ZUGFeRD-Prüfpaket erstellen. § 3a RVG Stundenhonorar, GoBD Aufbewahrung, ZUGFeRD XRechnung S... |
| `grosskanzlei-ma-fristen-cp-kalender` | Freistehender Deal-Fristen- und CP-Kalender für M&A-Mandate: Anwendungsfall Fristen aus Signing Closing Q&A Regulatory Register Board und Restrukturierung muessen in einem Kalender zusammengeführt werden. SPA Closing Conditions, §§ 35 ff... |
| `grosskanzlei-ma-insolvenzreife` | Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: Anwendungsfall im Kaufprozess oder Beratungsmandat muss geprüft werden ob Zielunternehmen oder Mandant nahe an Insolvenzantragspflicht ist. §§ 17-19 InsO Zahlungsunfähigkei... |
| `grosskanzlei-ma-liquiditaetsvorschau` | Freistehende Liquiditaetsvorschau für Corporate M&A und Distressed M&A: Anwendungsfall Kaeufer Verkaeufer oder Vorstand braucht kurzfristige Zahlungsfähigkeits-Übersicht 3-Wochen bis 13-Wochen-Horizont. § 17 InsO Zahlungsunfähigkeit, § 1... |
| `grosskanzlei-ma-schreibcanvas` | Freistehender Corporate-Schreibcanvas für SPA Board Paper und DD-Report: Anwendungsfall Anwalt entwirft SPA-Klausel Markup-Antwort DD-Report oder Mandatsvereinbarung und braucht substanzorientierten Schreibbegleiter der unsubstantiierte... |
| `grosskanzlei-ma-tabellenreview` | Freistehender Tabellenreview für Corporate M&A-Dokumente Datenpunkte und Perspektiven: Anwendungsfall Tabellen Formeln Excel-Modelle oder Dokumentenmatrizen in Transaktionen muessen auf Formelbrueche widersprüchliche Zahlen und Inkonsist... |
| `ki-einsatz-bei-gutachten-mandatsseite` | Großkanzlei-Mandatsseite bei KI-Verdacht gegenüber gerichtlichen oder vorgerichtlichen Sachverständigengutachten in Corporate-, M&A- und Schiedsverfahren. Strategische Prüfung der höchstpersönlichen Erstellungspflicht nach § 407a Abs. 1... |
| `rechtsabteilung-fusionskontrolle-closing` | Rechtsabteilungs-Fachmodul für Fusionskontrolle als Closing Condition: Regulatory Timetable, Hell-or-High-Water und Long Stop Date werden verknüpft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `rechtsabteilung-fusionskontrolle-legal` | Rechtsabteilung Fusionskontrolle Als Closing Condition, Rechtsabteilung Legal Tech Dd Mit Halluzinationsschutz, Rechtsabteilung Locked Box Leakage Aus Konzerncashpool, Rechtsabteilung Warranty And Indemnity Versicherung Im Claimfall: wäh... |
| `rechtsabteilung-legal-tech-dd` | Rechtsabteilungs-Fachmodul für Legal Tech DD mit Halluzinationsschutz: AI-gestützte DD wird mit Quellenregister, Privilege-Log und Red-Flag-Audit kontrolliert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `rechtsabteilung-locked-box-leakage` | Rechtsabteilungs-Fachmodul für Locked Box Leakage aus Konzerncashpool: Leakage wird aus Zahlungsflüssen, Cashpool, Management Fees und Related-Party-Deals herausgezogen. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlun... |
| `rechtsabteilung-mac-klausel-signing-closing` | Rechtsabteilungs-Fachmodul für MAC-Klausel bei Signing-Closing-Bruch: Ein Deal-Team erhält eine deutsche Auslegungsmatrix für MAC, MAE und Bring-down-Zertifikate. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `rechtsabteilung-warranty-indemnity` | Rechtsabteilungs-Fachmodul für Warranty-and-Indemnity-Versicherung im Claimfall: Notice-Fristen, Knowledge Scrape, Exclusions und Claim Preservation werden als geführt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlung... |
| `spa-apa-vertragsmarkup-key-rechtsabteilung` | Grosskanzlei Corporate Ma Spa Apa Entwurf, Grosskanzlei Corporate Ma Vertragsmarkup Key Issues, Rechtsabteilung Mac Klausel Bei Signing Closing Bruch: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `tax-structuring-transaktionsstruktur` | Grosskanzlei Corporate Ma Tax Structuring General, Grosskanzlei Corporate Ma Transaktionsstruktur, Grosskanzlei Corporate Ma Umwandlungsrecht, Grosskanzlei Corporate Ma Umwandlungssteuerrecht: wählt den konkreten Prüfpfad, trennt Frist,... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
