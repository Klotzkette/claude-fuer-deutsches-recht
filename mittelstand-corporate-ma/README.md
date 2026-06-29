# Mittelständische Kanzlei – Corporate/M&A-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Mittelstandsmandat-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`mittelstand-corporate-ma.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mittelstand-corporate-ma.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mittelstand-corporate-ma-werkstatt.md" download><code>mittelstand-corporate-ma-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mittelstand-corporate-ma-schnellstart.md" download><code>mittelstand-corporate-ma-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-share-deal-familienunternehmen-pellbach-werkzeugbau-passau-nachfolge.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-share-deal-familienunternehmen-pellbach-werkzeugbau-passau-nachfolge.zip) (Share Deal Pellbach Werkzeugbau GmbH & Co. KG — Familiennachfolge mit PE-Beteiligung, Earn-Out, MAC) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine gesellschaftsrechtliche Maßnahme rechtssicher beschliessen und dokumentieren.
Technischer Plugin-Name: `mittelstand-corporate-ma`.

Dies ist das freistehende Corporate/M&A-Plugin für mittelständische Kanzleien für den gesamten Transaktionslebenszyklus: Intake, Aktenanlage, Konflikt-/GwG-/Sanktionscheck, Datenraum, Due Diligence, Tabellenreview, Liquiditätsvorschau, Insolvenzreife, Q&A, SPA/APA, Disclosure Schedules, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing, XRechnung/ZUGFeRD-Vorbereitung, GoBD-Protokoll und Closing Bible.

**Wichtig:** Dieses Plugin funktioniert vollständig allein. Alle Kernabläufe, Hilfstabellen, Prüfungsschablonen und Workflows liegen im Plugin selbst; für die hier beschriebenen M&A-Workflows ist keine Zusatzinstallation nötig.

## Installation

1. ZIP herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `mittelstand-corporate-ma.zip` hochladen.
5. Mit einem konkreten Deal-Auftrag starten, zum Beispiel: `Starte das Corporate-M&A-Kommandocenter für diesen Datenraum.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

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
| `mittelstand-corporate-ma-automation-monitoring` | Automationen und Monitoring: Entwirft Monitore für Datenraum-Neuzugänge, Q&A, CP-Deadlines, Registerupdates, News, MAR-Signale und PMI-Aufgaben. |
| `mittelstand-corporate-ma-billing-narratives` | Mittelstandsmandat Billing Narratives: erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. |
| `mittelstand-corporate-ma-board-paper-business-judgment` | Board Paper und Business Judgment: Erstellt Entscheidungsunterlagen für Vorstand/Geschäftsführung/Aufsichtsrat mit Informationsgrundlage, Alternativen, Risiken und KI-Einsatztransparenz. |
| `mittelstand-corporate-ma-closing-bible-archiv` | Closing Bible und Archiv: Erstellt Closing Bible, Versionierung, Signaturketten, Registerbelege und Deal-Archiv. |
| `mittelstand-corporate-ma-conflict-gwg-sanctions` | Konflikt-, GwG- und Sanktionscheck: Führt Annahmeprüfung für Corporate/M&A: Interessenkonflikte, wirtschaftlich Berechtigte, Sanktionen, PEP, Mittelherkunft, Sektor- und Länder-Risiken. |
| `mittelstand-corporate-ma-datenqualitaet-xai-qualitaetskontrolle` | Datenqualität und XAI-Qualitätskontrolle: Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab. |
| `mittelstand-corporate-ma-datenraum-aufbau` | Datenraum-Aufbau: Strukturiert und bestückt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. |
| `mittelstand-corporate-ma-datenraum-gap-clean-room` | Datenraum-Gap-Analyse und Clean Room: Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Lücken, Widersprüche, Dubletten und Clean-Room-Bedarf. |
| `mittelstand-corporate-ma-deal-intake` | Deal-Intake: Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung. |
| `mittelstand-corporate-ma-deal-team-staffing` | Deal-Team und Staffing: Plant Workstreams, Rollen, Kapazitäten, Review-Level und Eskalationswege für große Transaktionen. |
| `mittelstand-corporate-ma-disclosure-schedules` | Disclosure Schedules: Leitet Disclosure Schedules aus Datenraum, DD-Findings, Q&A und SPA-Garantien ab. |
| `mittelstand-corporate-ma-distressed-ma` | Distressed M&A: führt Unternehmenskauf in Krise, vorläufiger Insolvenz, StaRUG, Insolvenzplan oder Asset Deal aus der Insolvenz mit Liquiditäts- und Closing-Fokus. |
| `mittelstand-corporate-ma-due-diligence-commercial-contracts` | Kommerzielle Vertrags-DD: Prüft Kunden-, Lieferanten-, Händler-, SaaS-, Lizenz- und Materialverträge auf Change of Control, Kündigung, Exklusivität, Haftung, IP und Preisrisiken. |
| `mittelstand-corporate-ma-due-diligence-legal` | Legal Due Diligence: Führt standardisierte Legal Due Diligence mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report. |
| `mittelstand-corporate-ma-due-diligence-reporting` | DD Reporting und Legal Fact Book: Erstellt Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary und Issues-to-SPA-Mapping. |
| `mittelstand-corporate-ma-expert-calls-transkripte` | Expert Calls und Transkripte: Bereitet Management Presentations, Expert Calls und Transkripte für DD und SPA-Verhandlung auf. |
| `mittelstand-corporate-ma-fair-disclosure-knowledge` | Fair Disclosure und Knowledge: Prüft Wissens-, Kenntnis-, Fair-Disclosure- und Aktenwissen-Klauseln im Lichte von KI-gestützter Datenraumprüfung. |
| `mittelstand-corporate-ma-freundlicher-copilot` | Freundlicher Deal-Copilot: Führt junge Anwender verzeihend durch große Transaktionen, erkennt unausgesprochene Absichten und meldet sich kurz mit hilfreichen Hinweisen. |
| `mittelstand-corporate-ma-gesellschaftsrecht-register` | Corporate Housekeeping und Register: Prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschlüsse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals. |
| `mittelstand-corporate-ma-handelsregisterabruf` | Handelsregister- und Registerabruf: Führt offizielle Registerabrufe für Zielgesellschaft, Verkäufer, Erwerber, Beteiligungsketten, KG und Organstellung. |
| `mittelstand-corporate-ma-kaltstart` | Deal-Kaltstart: Nimmt Kanzlei- und Mandantenpräferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln. |
| `mittelstand-corporate-ma-kg-personengesellschaften` | KG und Personengesellschaften: Spezialworkflow für KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register. |
| `mittelstand-corporate-ma-ki-governance-berufsrecht` | KI-Governance und Berufsrecht: Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe. |
| `mittelstand-corporate-ma-kommandocenter` | Deal-Kommandocenter: Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt Deal-Karte, Ampel, Rollen und nächste Aktion. |
| `mittelstand-corporate-ma-look-and-feel` | Corporate-Cowork-Look: Definiert die sichtbare Oberfläche: sehr ruhig, edel, bläulich-silbern mit warmem Orange für Entscheidungspunkte, dichte Deal-Information statt Marketing. |
| `mittelstand-corporate-ma-matter-file` | Deal-Akte: Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI. |
| `mittelstand-corporate-ma-output-versand-signing` | Output, Signing und Versand: Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand. |
| `mittelstand-corporate-ma-outside-in-target-screening` | Outside-in Target Screening: Erstellt frühe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen. |
| `mittelstand-corporate-ma-post-closing-integration` | Post-Closing Integration: Übersetzt DD-Findings, SPA-Pflichten und Synergieannahmen in einen PMI-Plan. |
| `mittelstand-corporate-ma-public-ma-kapitalmarkt-mar` | Public M&A, Kapitalmarkt und MAR: Begleitet börsennotierte Transaktionen: WpUEG-Unterlagen, Ad-hoc-Prüfung, Insiderlisten, Stellungnahmen und Marktgerüchte. |
| `mittelstand-corporate-ma-qa-information-requests` | Q&A und Information Requests: Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität. |
| `mittelstand-corporate-ma-rechtsprechungsrecherche` | Corporate-Rechtsprechungsrecherche: Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. |
| `mittelstand-corporate-ma-regulatory-fdi-merger-control` | Fusionskontrolle und Investitionskontrolle: Erstellt Freigabe-Landkarte für Kartellrecht, Fusionskontrolle, AWV/FDI, Sektorregulierung und Multi-Jurisdiction-Filings. |
| `mittelstand-corporate-ma-restructuring-starug-insolvenzplan` | StaRUG und Insolvenzplan: unterstützt Restrukturierungsfälle mit Planoptionen, Gläubigerklassen, Liquiditätsprüfung, Antragspflichten, Distressed M&A und Zeitplan. |
| `mittelstand-corporate-ma-signing-closing-conditions` | Signing, Closing und CPs: Führt Signing-to-Closing: Conditions Precedent, Ordinary Course, Bring-down, Closing Deliverables, Funds Flow und Closing Bible. |
| `mittelstand-corporate-ma-simulation-bidder-process` | Bieterprozess-Simulation: Simuliert einen beschleunigten achtstündigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call. |
| `mittelstand-corporate-ma-spa-apa-entwurf` | SPA/APA-Entwurf: Erstellt und strukturiert Kaufvertragsentwürfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur. |
| `mittelstand-corporate-ma-steps-plan-pmo` | Deal-PMO und Steps Plan: Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing. |
| `mittelstand-corporate-ma-tabellenreview-3d-datenraum` | 3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft. |
| `mittelstand-corporate-ma-teaser-im-processdocs` | Teaser, IM und Prozessdokumente: Unterstützt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation. |
| `mittelstand-corporate-ma-transaktionsstruktur` | Transaktionsstrukturierung: Entwickelt Strukturvarianten für Share Deal, Asset Deal, Carve-out, Joint Venture, Verschmelzung, Spaltung, Formwechsel, Roll-over und Managementbeteiligung. |
| `mittelstand-corporate-ma-translations-multijurisdictional` | Multi-Jurisdiction und Übersetzungen: Koordiniert lokale Kanzleien, Übersetzungen, Rechtsvergleich und Multi-Jurisdiction-Matrizen. |
| `mittelstand-corporate-ma-umwandlungsrecht` | Umwandlungsrecht: Bearbeitet Verschmelzung, Spaltung, Ausgliederung, Formwechsel, Einbringung und Vorfeld-Carve-outs nach Umwandlungsrecht. |
| `mittelstand-corporate-ma-umwandlungssteuerrecht` | Umwandlungssteuerrecht: Erfasst umwandlungssteuerliche Strukturfragen als Arbeitsmatrix für Steuerteam und Corporate-Team. |
| `mittelstand-corporate-ma-vertragsmarkup-key-issues` | Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive. |
| `mittelstand-corporate-ma-wi-insurance` | W&I-Versicherung: Bereitet W&I-Prozess, Underwriting, DD-Berichte, KI-DD-Transparenz und Deckungsausschlüsse vor. |
| `mittelstand-ma-aktenanlage` | Freistehende M&A-Aktenanlage: eröffnet Deal-Akte, Aktenzeichen, Parteienregister, Ordnerstruktur, Datenraumspiegel, Vertraulichkeitsstufen und Closing-Bible-Grundgerüst mit vollständig interner Arbeitslogik. |
| `mittelstand-ma-erechnung-gobd` | Freistehender Billing-, GoBD- und E-Rechnungsworkflow für M&A-Mandate: erzeugt Narratives, Workstream-Abrechnung, XRechnung-XML, ZUGFeRD-Prüfpaket und revisionssicheren Buchungsnachweis. |
| `mittelstand-ma-fristen-cp-kalender` | Freistehender Deal-Fristen- und CP-Kalender: führt Signing-, Closing-, Q&A-, Regulatory-, Register-, Board-, Ordinary-Course- und Restrukturierungsfristen im M&A-Mandat. |
| `mittelstand-ma-insolvenzreife` | Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: prüft Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit, Überschuldung, Antragspflichten und Deal-Auswirkungen intern. |
| `mittelstand-ma-liquiditaetsvorschau` | Freistehende Liquiditätsvorschau für Corporate/M&A und Distressed M&A: prüft 3-Wochen-Liquidität, 13-Wochen-Cash-Bridge, Runway, OPOS, Bankdaten und Insolvenzschwellen intern. |
| `mittelstand-ma-schreibcanvas` | Freistehender Corporate-Schreibcanvas: begleitet SPA, Replik, Board Paper, Mandatsvereinbarung, DD-Report und Registertext mit freundlichen substanz- und belegorientierten Hinweisen. |
| `mittelstand-ma-tabellenreview` | Freistehender Tabellenreview für Corporate/M&A: prüft Dokumente, Datenpunkte, Tabellen, Formeln und Perspektiven als interne Review-Matrix mit vollständig interner Review-Logik. |

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

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `automation-monitoring` | Mandant oder Kanzlei will Deal-Aktivitaeten automatisch tracken: Datenraum-Neuzugaenge Fristen Q&A MAR-Signale PMI-Aufgaben. Normen MAR VO 596/2014 §§ 35-44 GWB Insiderlisten. Prüfraster Datenraum-Monitor CP-Deadline-Kalender Register-Up... |
| `beirat-abgrenzung-aufsichtsrat` | GmbH-Beirat: Beirat Abgrenzung Aufsichtsrat; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-amtszeit-rotation-bank-sanierung` | GmbH-Beirat: Beirat Amtszeit Und Rotation; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-bank-und-sanierung` | GmbH-Beirat: Beirat Bank Und Sanierung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-beratungsfunktion` | GmbH-Beirat: Beirat Beratungsfunktion; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-beschlussfassung` | GmbH-Beirat: Beirat Beschlussfassung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-beschlussmaengel-bestellung-abberufung` | GmbH-Beirat: Beirat Beschlussmaengel; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-bestellung-und-abberufung` | GmbH-Beirat: Beirat Bestellung Und Abberufung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-budget-und-businessplan` | GmbH-Beirat: Beirat Budget Und Businessplan; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-compliance-und-internal-investigation` | GmbH-Beirat: Beirat Compliance Und Internal Investigation; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-datenschutz-ki-deadlock-mechanik` | GmbH-Beirat: Beirat Datenschutz Und KI; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-deadlock-mechanik` | GmbH-Beirat: Beirat Deadlock Mechanik; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-entscheidungsbefugnisse` | GmbH-Beirat: Beirat Entscheidungsbefugnisse; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-fakultativer-aufsichtsrat-52-gmbhg` | GmbH-Beirat: Beirat Fakultativer Aufsichtsrat 52 Gmbhg; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-familiengesellschaft` | GmbH-Beirat: Beirat Familiengesellschaft; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-geschaeftsfuehrerabberufung` | GmbH-Beirat: Beirat Geschäftsführerabberufung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-geschaeftsfuehrerbestellung` | GmbH-Beirat: Beirat Geschäftsführerbestellung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-geschaeftsordnung` | GmbH-Beirat: Beirat Geschäftsordnung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-gmbh-zustimmungskatalog-und-konfliktmatrix` | Prüft und entwirft GmbH-Beiratsregeln für mittelständische und Corporate-Mandate: Vetorechte, Investorenschutz, Haftung, Protokoll, Deadlock und Geschäftsführerautonomie im Mittelstand Corporate Ma. |
| `beirat-haftung` | GmbH-Beirat: Beirat Haftung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-immobilien-investitionen` | GmbH-Beirat: Beirat Immobilien Und Investitionen; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-informationsrechte` | GmbH-Beirat: Beirat Informationsrechte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-insolvenznaehe` | GmbH-Beirat: Beirat Insolvenznaehe; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-interessenkonflikte` | GmbH-Beirat: Beirat Interessenkonflikte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-kaltstart-und-zielbild` | Beirat Kaltstart Und Zielbild: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad |
| `beirat-katalog-wesentlicher-kontrollfunktion` | GmbH-Beirat im Mittelstand: Katalog zustimmungsbedürftiger Geschäfte, Kontrollfunktion, Geschäftsführungsautonomie, Deadlock-Vermeidung, Schwellenwerte, Eilkompetenz und beschlussfeste Beiratsordnung. |
| `beirat-kontrollfunktion` | GmbH-Beirat: Beirat Kontrollfunktion; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-mitbestimmung-abgrenzung` | GmbH-Beirat: Beirat Mitbestimmung Abgrenzung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-musterklauseln` | GmbH-Beirat: Beirat Musterklauseln; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-nachfolge` | GmbH-Beirat: Beirat Nachfolge; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-private-equity-register-notar` | GmbH-Beirat: Beirat Private Equity Investor; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-red-team-satzung` | Beirat Red Team Satzung: Du bist GmbH-Beiratsarchitekt. Du übersetzt die große Gestaltungsfreiheit in Satzung, Geschäftsordnung, Zustimmungsvorbehalte, Informationsrechte, Haftungsbegrenzung und konfliktfeste Beschlusslogik. |
| `beirat-register-und-notar` | GmbH-Beirat: Beirat Register Und Notar; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-satzungsgrundlage` | GmbH-Beirat: Beirat Satzungsgrundlage; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-sitzung-und-protokoll` | GmbH-Beirat: Beirat Sitzung Und Protokoll; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-startup-investor-streit-gesellschafter` | GmbH-Beirat: Beirat Startup Investor Director; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-streit-gesellschafter` | GmbH-Beirat: Beirat Streit Gesellschafter; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-transaktionen-ma` | GmbH-Beirat: Beirat Transaktionen M&A; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-verguetung` | GmbH-Beirat im Mittelstand: Vergütung, Auslagen, D&O, Haftungsfreistellung, Interessenkonflikte, Drittvergleich, Beschlusszuständigkeit und steuer-/sozialversicherungsnahe Plausibilitätsprüfung. |
| `beirat-verschwiegenheit-veto-rechte` | GmbH-Beirat: Beirat Verschwiegenheit; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-veto-rechte` | GmbH-Beirat: Beirat Veto Rechte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `beirat-zustimmungsvorbehalte` | GmbH-Beirat: Beirat Zustimmungsvorbehalte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Mittelstand Corporate Ma. |
| `billing-narratives` | Kanzlei erstellt Rechnung für M&A-Mandat und braucht praezise zeitgerechte Leistungsbeschreibungen: Time Narratives Phasenbudgets Workstream-Rechnungen Cap/Success-Fee-Berechnung. Normen RVG §§ 1 ff. BRAO § 49b AO-Steuerrecht. Prüfraster... |
| `board-paper-closing-bible-conflict-gwg` | Vorstand GF oder Aufsichtsrat braucht Entscheidungsunterlage für M&A-Beschluss: Board Paper Business-Judgment-Dokumentation KI-Einsatztransparenz. Normen §§ 93 AktG 43 GmbHG Business-Judgment Rule ARAG/Garmenbeck. Prüfraster Informations... |
| `closing-bible-archiv` | Transaktion vor Closing und Anwalt muss Closing Bible erstellen: Versionierung Signaturketten Registerbelege Deal-Archiv. Normen §§ 311b 15 GmbHG BeurkG SPA-Pflichten Notarrecht. Prüfraster Vollständigkeit Unterlagen Signatur-Tracking Re... |
| `conflict-gwg-sanctions` | Konflikt- GwG- und Sanktionscheck: Annahmeprüfung Corporate/M&A: Interessenkonflikte, wirtschaftlich Berechtigte, Sanktionen, PEP, Mittelherkunft, Sektorrisiken, BRAO 43a im Mittelstand Corporate Ma. |
| `cp-kalender-beirat` | Corporate-Rechtsprechungsrecherche: Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung im Mittelstand Corporate Ma. |
| `datenqualitaet-xai-qualitaetskontrolle` | Datenqualität und XAI-Qualitätskontrolle: Sichert KI-gestuetzte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab im Mittelstand Corporate Ma. |
| `datenraum-aufbau-gap-deal-intake-team` | Datenraum-Aufbau: Strukturiert und bestueckt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse im Mittelstand Corporate Ma. |
| `datenraum-gap-clean-room` | Datenraum-Gap-Analyse und Clean Room: Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Luecken, Widersprueche, Dubletten und Clean-Room-Bedarf im Mittelstand Corporate Ma. |
| `deal-intake` | Deal-Intake: Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung im Mittelstand Corporate Ma. |
| `deal-kommandocenter` | Deal-Kommandocenter: Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-und erzeugt Deal-Karte, Ampel, Rollen und nächste Aktion im Mittelstand Corporate Ma. |
| `deal-team-staffing` | Kanzlei strukturiert Transaktionsteam für grosse M&A-Mandate: Workstreams Rollen Kapazitaetsplanung Review-Level Eskalationswege. Normen BRAO § 43a Berufsrecht Mandantsgeheimnis-Sicherung. Prüfraster Workstream-Karte Rollen-Matrix Kapazi... |
| `distressed-due` | Disclosure Schedules: Ableitung aus Datenraum, DD-Findings, Q&A und SPA-Garantien; Materiality Auslesen, Earn-Out-Konflikte, Vendor DD, Fair Disclosure nach BGH-Rechtsprechung im Mittelstand Corporate Ma. |
| `distressed-ma` | Distressed M&A: Unternehmenskauf in Krise, vorläufiger Insolvenz, StaRUG, Insolvenzplan oder Asset Deal aus der Insolvenz; §§ 17-19 InsO, § 15a InsO, § 135 InsO, §§ 1-93 StaRUG im Mittelstand Corporate Ma. |
| `due-diligence-commercial-contracts` | Kommerzielle Vertrags-DD: Prüft Kunden-, Lieferanten-, Haendler-, SaaS-, Lizenz- und Materialvertraege auf Change of Control, Kündigung, Exklusivitaet, Haftung, IP und Preisrisiken im Mittelstand Corporate Ma. |
| `due-diligence-legal` | Legal Due Diligence: standardisierte Legal DD mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report für Share Deal und Asset Deal im Mittelstand Corporate Ma. |
| `expert-calls-fair` | DD Reporting und Legal Fact Book: Erstellt Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary und Issues-to-SPA-Mapping im Mittelstand Corporate Ma. |
| `expert-calls-transkripte` | Anwalt wertet Management Presentations Expert Calls und Verhandlungstranskripte für DD und SPA-Vorbereitung aus. Normen §§ 311 241 BGB Vorvertragspflichten Geheimhaltungsvereinbarungen NDA. Prüfraster Kernaussagen-Extrakt Widerspruechepr... |
| `fair-disclosure-knowledge` | Fair Disclosure und Knowledge: Prüft Wissens-, Kenntnis-, Fair-Disclosure- und Aktenwissen-Klauseln im Lichte von KI-gestuetzter Datenraumprüfung im Mittelstand Corporate Ma. |
| `freundlicher-copilot` | Junger Anwalt oder Berufseinsteiger braucht unterstuetzenden Begleiter durch grosse Transaktion ohne Angst vor Fehlern. Normen BRAO § 43 Sorgfaltspflicht. Prüfraster Intentionserkennung Fehlerfreundliche Hinweise Eskalationsvorschlaege.... |
| `gesellschaftsrecht-register` | Corporate Housekeeping und Register: prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschluesse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals für M&A im Mittelstand Corporate Ma. |
| `handelsregisterabruf` | Handelsregister- und Registerabruf: offizielle Registerabrufe für Zielgesellschaft, Kaeufer, Erwerber, Beteiligungsketten, KG und Organstellung; §§ 8-10 GmbHG, §§ 29 HGB ff im Mittelstand Corporate Ma. |
| `kaltstart` | Deal-Kaltstart: Nimmt Kanzlei- und Mandantenpraeferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Mittelstand Corporate Ma-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Be... |
| `kg-personengesellschaften` | KG und Personengesellschaften: KG, GmbH und Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme, Register; §§ 161-177 HGB, MoPeG, BGH-Rechtsprechung im Mittelstand Corporate Ma. |
| `ki-governance-berufsrecht` | KI-Governance und Berufsrecht: Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe im Mittelstand Corporate Ma. |
| `liquiditaetsvorschau-schreibcanvas` | Unternehmen in M&A oder Krise braucht Liquiditaetsvorschau: 3-Wochen-Liquiditaet 13-Wochen-Cash-Bridge Runway OPOS Bankdaten Insolvenzschwellen. Normen §§ 17-19 InsO IDW S 11 GoF. Prüfraster Zufluss-Abfluss-Plan OPOS-Abgleich Banklinien-... |
| `look-and-feel` | Kanzlei oder Plugin-Entwickler definiert visuelles Erscheinungsbild des Deal-Copiloten: ruhig edel blaeulch-silbern warmes Orange für Entscheidungspunkte. Normen keine (UI/UX-Guideline). Prüfraster Farbpalette Typografie Informationsdich... |
| `matter-file` | Deal-Akte: Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI im Mittelstand Corporate Ma. |
| `mittelstand-ma-aktenanlage` | Kanzlei eroeffnet neue Deal-Akte für M&A-Mandat: Aktenzeichen Parteienregister Ordnerstruktur Datenraumspiegel Vertraulichkeitsstufen Closing-Bible-Grundgeruest. Normen BRAO §§ 43 50 Aktenaufbewahrungspflicht DSGVO. Prüfraster Vollständi... |
| `mittelstand-ma-erechnung-gobd` | Kanzlei braucht GoBD-konforme E-Rechnung für M&A-Mandat: XRechnung-XML ZUGFeRD Workstream-Abrechnung revisionssicheren Buchungsnachweis. Normen GoBD BMF-Schreiben 2019 UStG §§ 14 14a ZUGFeRD EN 16931. Prüfraster Pflichtfelder XRechnung P... |
| `mittelstand-ma-fristen-cp-kalender` | Kanzlei oder Mandant benoetigt Fristen- und CP-Kalender für M&A-Mandat: Signing Closing Q&A Regulatory Register Board Ordinary-Course. Normen §§ 187-193 BGB Fristberechnung MAR-Fristen GWB-Fristen AWV-Fristen. Prüfraster CP-Vollständigke... |
| `mittelstand-ma-insolvenzreife` | Unternehmen in M&A-Situation oder Krise und Anwalt prüft ob Insolvenzantragspflicht besteht: Zahlungsunfähigkeit drohende Zahlungsunfähigkeit Überschuldung StaRUG-Schwelle. Normen §§ 17-19 InsO § 15a InsO §§ 1-4 StaRUG. Prüfraster Zahlun... |
| `mittelstand-ma-schreibcanvas` | Kanzlei-Anwalt schreibt SPA Replik Board Paper Mandatsvereinbarung DD-Report oder Registertext und braucht substanzorientierten Feedback-Begleiter. Normen BRAO § 43 Sorgfalt Zitierstandards. Prüfraster Sachverhalts-Unterlegung Quellenbel... |
| `mittelstand-ma-tabellenreview` | Kanzlei prüft Dokumente Tabellen Formeln und Datenpunkte für Corporate/M&A mit interner Review-Matrix aus drei Perspektiven: Recht Steuer Wirtschaft. Normen §§ 276 278 BGB Sorgfaltspflicht. Prüfraster Formel-Validierung Datenpunkt-Konsis... |
| `outside-in-target-screening` | Outside-in Target Screening: Erstellt fruehe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen im Mittelstand Corporate Ma. |
| `public-kapitalmarkt` | Post-Closing Integration: DD-Findings, SPA-Pflichten und Synergieannahmen in PMI-Plan; Earn-Out-Monitoring, Post-Closing-Ansprüche, Betriebsuebergang, § 613a BGB im Mittelstand Corporate Ma. |
| `public-ma-kapitalmarkt-mar` | Public M&A Kapitalmarkt und MAR: boersennotierte Transaktionen, WpUEG-Unterlagen, Ad-hoc-Prüfung, Insiderlisten, Stellungnahmen, Marktgerueichte; WpUEG, MAR VO 596/2014, WpHG im Mittelstand Corporate Ma. |
| `qa-information-requests` | DD-Team verwaltet Q&A-Prozess im Datenraum: Information Request Lists Follow-ups Antwortqualitaets-Check. Normen §§ 311 241 BGB Offenbarungspflicht Disclosure-Prinzipien. Prüfraster IRL-Vollständigkeit Antwortprüfung Offene-Punkte-Tracki... |
| `rechtsabteilung-betriebsuebergang-im-asset-deal` | Rechtsabteilungs-Fachmodul für Betriebsübergang im Asset Deal: Informationsschreiben, Widerspruchsrisiko und Closing-Unterlagen werden koordiniert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Mittelstan... |
| `rechtsabteilung-earn-out-bei-mittelstandsverkauf` | Rechtsabteilungs-Fachmodul für Earn-out bei Mittelstandsverkauf: Earn-out-KPIs, Manipulationsschutz und Post-Closing-Steuerung werden für Verkäufer und Käufer geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungs... |
| `rechtsabteilung-familiengesellschafter-und-zustimmungsketten` | Rechtsabteilungs-Fachmodul für Familiengesellschafter und Zustimmungsketten: Zustimmungen, Vorkaufsrechte, Güterstand und Nachfolge werden vor Signing gesichert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption... |
| `rechtsabteilung-garantiekatalog-vendor-due` | Rechtsabteilungs-Fachmodul für Garantiekatalog ohne Großkanzlei-Overkill: Garantien werden für Mittelstandstransaktionen risikobasiert gestrafft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Mittelstand... |
| `rechtsabteilung-vendor-due-diligence-fuer-versteckte-altlasten` | Rechtsabteilungs-Fachmodul für Vendor Due Diligence für versteckte Altlasten: Der Verkäufer baut eine Verteidigungsakte statt bloßer Verkaufsbroschüre. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Mittel... |
| `regulatory-fdi-merger-control` | Fusionskontrolle und FDI: Freigabe-Landkarte für Kartellrecht GWB/FKVO, AWV-Investitionsprüfung, Sektorregulierung; Multi-Jurisdiction-Filings; §§ 35-44 GWB, Art. 4 FKVO im Mittelstand Corporate Ma. |
| `signing-closing` | Unternehmen in Krise oder Insolvenz braucht Restrukturierungsplan: StaRUG Insolvenzplan Gläubigerklassen Liquiditaetsprüfung Distressed M&A. Normen §§ 1-93 StaRUG §§ 217-269 InsO §§ 17-19 InsO Antragspflichten. Prüfraster Plan-Optionen G... |
| `signing-closing-conditions` | Signing Closing und CPs: Signing-to-Closing-Prozess mit Conditions Precedent, Ordinary Course, Bring-down, Closing Deliverables, Funds Flow und Closing Bible für M&A-Transaktionen im Mittelstand Corporate Ma. |
| `simulation-bidder-process` | Bieterprozess-Simulation: Simuliert einen beschleunigten achtstuendigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call im Mittelstand Corporate Ma. |
| `spa-apa-entwurf` | SPA/APA-Entwurf: Kaufvertragsentwuerfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur; §§ 433 BGB, 15 GmbHG, 179 AktG, Garantiekatalog, MAC, Earn-Out im Mittelstand Corporate Ma. |
| `steps-plan-pmo` | Deal-PMO und Steps Plan: Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing im Mittelstand Corporate Ma. |
| `tabellenreview-3d-datenraum` | 3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft im Mittelstand Corporate Ma. |
| `teaser-processdocs-transaktionsstruktur` | Teaser, IM und Prozessdokumente: Unterstuetzt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation im Mittelstand Corporate Ma. |
| `transaktionsstruktur` | Transaktionsstrukturierung: Entwickelt Strukturvarianten für Share Deal, Asset Deal, Carve-out, Joint Venture, Verschmelzung, Spaltung, Formwechsel, Roll-over und Managementbeteiligung im Mittelstand Corporate Ma. |
| `translations-multijurisdictional` | Multi-Jurisdiction und Übersetzungen: Koordiniert lokale Kanzleien, Übersetzungen, Rechtsvergleich und Multi-Jurisdiction-Matrizen im Mittelstand Corporate Ma. |
| `umwandlungsrecht` | Umwandlungsrecht: Verschmelzung, Spaltung, Ausgliederung, Formwechsel, Einbringung und Vorfeld-Carve-outs nach UmwG mit Normen, BGH-Rechtsprechung und Schritt-Workflow im Mittelstand Corporate Ma. |
| `umwandlungssteuerrecht-tabellenreview` | Umwandlungssteuerrecht: UmwStG-Strukturfragen, Buchwertantrag, steuerliche Rückwirkung, § 8c KStG Verlustuntergang, GrESt-Ergaenzungstatbestand, Einbringung §§ 20-24 UmwStG im Mittelstand Corporate Ma. |
| `versand-signing` | Output, Signing und Versand: Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand. |
| `vertragsmarkup-key-beirat-haftung-billing` | Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschlaege nach Parteiperspektive im Mittelstand Corporate Ma. |
| `wi-insurance-aktenanlage-erechnung-gobd` | W&I-Versicherung: W&I-Prozess, Underwriting, DD-Berichte, Deckungsausschluesse, AI-DD-Transparenz, Synthetic Warranties, Materiality Auslesen und Disclosure Letter für M&A im Mittelstand Corporate Ma. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
