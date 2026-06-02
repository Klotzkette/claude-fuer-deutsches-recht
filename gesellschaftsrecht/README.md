# Gesellschaftsrecht-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`gesellschaftsrecht`) | [`gesellschaftsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Roeschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation** (`gesellschaftsgruender-streit-roeschen-tech`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) |
| **Akte Kometenfalter Systems GmbH — Series A Project Comet Moth** (`gesellschaftsrecht-legal-english-frankfurt-startup`) | [Gesamt-PDF lesen](../testakten/gesellschaftsrecht-legal-english-frankfurt-startup/gesamt-pdf/gesellschaftsrecht-legal-english-frankfurt-startup_gesamt.pdf) | [`testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |
| **Handelsrecht HGB — Elbwerft Solar: eGbR, OHG-Statuswechsel, KG und Handelskauf** (`handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona`) | [Gesamt-PDF lesen](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/gesamt-pdf/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona_gesamt.pdf) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Abläufe für gesellschaftsrechtliche Mandate in deutschen Kanzleien und Rechtsabteilungen: M&A-Transaktionen, Organe und Protokollwesen, Gesellschafts-Compliance und Unternehmensführung. Aktiviere nur die Module, die für deine Praxis relevant sind. Das Kaltstart-Interview ist modular – es stellt gezielte Fragen je aktivem Bereich und schreibt nur die entsprechenden Abschnitte in dein Praxisprofil.

**Jedes Ergebnis ist ein Entwurf zur anwaltlichen Überprüfung – zitiert, markiert und gesperrt – kein Rechtsgutachten.** Das Plugin übernimmt die Arbeit: liest Dokumente, wendet dein Playbook an, findet die Issues, erstellt den Bericht. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Zitate sind mit Quellen gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu prüfen sind. Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB) wird konservativ gewahrt. Folgenreiche Handlungen – Einreichung, Versendung, Beurkundung – werden durch ausdrückliche Bestätigung gesperrt.


## ⬇️ Zum Ausprobieren: Arbeitsakten (separat)

Mandatsakten zum sofortigen Ausprobieren — **kein Teil des Plugins**, separater Download:

| Akte | Direkt-Download |
| --- | --- |
| **gesellschaftsgruender streit roeschen tech** | [testakte-gesellschaftsgruender-streit-roeschen-tech.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) |
| **gesellschaftsrecht legal english frankfurt startup** | [testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Gesellschaftsrecht (`gesellschaftsrecht`, dieses Plugin) | [gesellschaftsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Für wen

| Rolle | Aktive Module |
|---|---|
| **M&A-Anwalt (Kanzlei oder Inhouse)** | M&A |
| **Gesellschaftssekretär / Corporate Secretary** | Organe & Protokoll |
| **General Counsel, Aktiengesellschaft** | M&A + Börse/Kapitalmarkt + Organe & Protokoll |
| **General Counsel, GmbH** | M&A + Organe & Protokoll + Gesellschafts-Compliance |
| **Legal Ops / Solo-GC** | Nach Bedarf – beliebige Kombination |

## Erster Start

```
/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview
```

Führt durch die Modulauswahl und ein kurzes Zielinterview je aktivem Bereich. Schreibt ein modulares Praxisprofil nach:
`~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/CLAUDE.md`

Deine Konfiguration bleibt dort und übersteht Plugin-Updates.

Dealspezifisches Setup (nur M&A-Modul):

```
/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview --neues-mandat
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview` | Modulares Kaltstart oder `--neues-mandat` / `--modul [m&a \| organe \| boerse \| compliance]` |
| `/gesellschaftsrecht:dd-findings-extraktion [ordner]` | Datenraum-Dokumente lesen, Issues im Hauskatalog extrahieren |
| `/gesellschaftsrecht:tabellenpruefung` | Tabellarisches Review – eine Zeile pro Dokument, eine Spalte pro Datenpunkt, jede Zelle mit Fundstelle, Excel-Ausgabe |
| `/gesellschaftsrecht:wesentliche-vertraege-anlage` | Wesentliche-Verträge-Anlage (Disclosure Schedule) aus DD-Findings |
| `/gesellschaftsrecht:vollzugs-checkliste` | Vollzugscheckliste – was blockiert den Closing, kritischer Pfad |
| `/gesellschaftsrecht:gesellschafterbeschluss` | Gesellschafterbeschluss im schriftlichen Verfahren § 48 II GmbHG, Muster mit Unterzeichner-Tracker |
| `/gesellschaftsrecht:gesellschafts-compliance` | Gesellschafts-Compliance-Tracker – init, Bericht, Update, Audit, Export |
| `/gesellschaftsrecht:integrations-management` | Post-Closing-Integrationsplan, Zustimmungsregister, Vertragsübertragung, Statusberichte |
| `/gesellschaftsrecht:gesellschaftsrecht-mandat-arbeitsbereich` | Mandatsarbeitsbereiche verwalten (Mehrmandat-Kanzleien) – neu, liste, wechsel, schließ, keins |
| `/gesellschaftsrecht:gmbh-gruendung` | GmbH-Gründung Schritt-für-Schritt: Gesellschaftsvertrag, Notar, Handelsregister |
| `/gesellschaftsrecht:handelsregisteranmeldung` | Handelsregisteranmeldungen: HRB/HRA, Änderungen, Kapitalmaßnahmen |

## Voraussetzungen

Mehrere Funktionen verweisen auf Slack, Google Drive, SharePoint, Box, Datasite- oder VDR-Integrationen. Diese erfordern MCP-Server in deiner Umgebung – sie sind **nicht im Plugin enthalten**. Ohne sie greift das Plugin auf lokale Dateiausgabe zurück (Entwürfe lokal gespeichert statt in einen Kanal gepostet, Tracker-Dateien auf Festplatte statt in einem verbundenen Repository).

MCP-Server konfigurieren unter `.mcp.json` auf Repo- oder Benutzerebene. Skills und Agenten erkennen zur Laufzeit, was verfügbar ist, und passen ihr Verhalten an.

## Skills

| Skill | Modul | Zweck |
|---|---|---|
| **kaltstart-interview** | Alle | Modulares Interview – aktiviert nur relevante Abschnitte |
| **dd-findings-extraktion** | M&A | Datenraum-Dokumente → Issues im Hauskatalog, nach Kategorie |
| **tabellarisches-review** | M&A | Dokumentensatz gegen typisiertes Spaltenformat prüfen; Zellen mit Fundstelle; `.xlsx` / `.csv` / Markdown; speist wesentliche-vertraege-anlage |
| **dealteam-zusammenfassung** | M&A | Stufenbriefings: Geschäftsführung / Deal-Lead / Arbeitsteam |
| **wesentliche-vertraege-anlage** | M&A | Disclosure Schedule gemäß SPA-Definition |
| **vollzugs-checkliste** | M&A | Selbstaktualisierend: nimmt Einträge aus DD und Schedule-Builds auf |
| **ki-werkzeug-uebergabe** | M&A | Luminance/Kira-Integration – Massenextraktion + QA-Schicht |
| **aufsichtsrat-protokoll** | Organe & Protokoll | Kalendererkennung für Sitzungen → Protokollentwurf im Hausformat (AG: § 107 AktG; GmbH: § 48 GmbHG) |
| **gesellschafterbeschluss** | Organe & Protokoll | Beschlüsse im schriftlichen Verfahren § 48 II GmbHG mit Mustersuche aus dem Beschluss-Repository; Hinweis bei wesentlichen Einzelmaßnahmen |
| **gesellschafts-compliance** | Gesellschafts-Compliance | Compliance-Kalender-Tracker (YAML); Einreichungsfristen nach Rechtsträger; Bilanzpublizität § 325 HGB; Transparenzregister § 20 GwG; Gesundheitsaudit; CSV-Export |
| **post-merger-integration** | M&A | Post-Closing-Integrationsplan; phasenweiser Arbeitsplan (Tag 1/30/90/180); Zustimmungsregister mit SPA-Fristen; Vertragsübertragung; Wochenstatusberichte |
| **mandat-arbeitsbereich** | Alle | Mandatsarbeitsbereiche erstellen, auflisten, wechseln und schließen für Mehrmandat-Kanzleien; isoliert jeden Mandanten/Auftrag, damit Kontext nicht übergreift |
| **gmbh-gruendung** | Compliance | GmbH-Gründung: Gesellschaftsvertrag, Stammkapital, Notar, Handelsregister, IHK, Gewerbe |
| **gesellschafterbeschluss-vorlagen** | Organe | Beschlussvorlagen GmbH/AG, Beschlussfähigkeit, Mehrheiten, Anfechtungsklage |
| **handelsregisteranmeldung** | Compliance | HRB/HRA-Anmeldungen, Änderungen, Kapitalmaßnahmen, notarielle Form |

## Interaktive Befehle vs. geplante Agenten

Die Befehle oben laufen, wenn du sie aufrufst – für das aktive Mandat. Die Agenten unten laufen nach Zeitplan – für das, was sich bewegt, während du nicht hinschaust:

| Agent | Modul | Was er beobachtet | Standard-Rhythmus |
|---|---|---|---|
| **datenraum-monitor** | M&A | VDR auf neue Dokumenten-Uploads; markiert Uploads, die zu Hochprioritätskategorien passen; aktualisiert Vollzugschecklisten-Status | Wöchentlich |

## Integrationen

**Verbinde zuerst ein Recherchetool – die Zitier-Absicherung hängt davon ab.** Ohne eines wird jedes Zitat mit `[prüfen]` markiert und der Prüfer-Hinweis über jedem Ergebnis vermerkt, dass Quellen nicht verifiziert wurden. Skills funktionieren in beiden Fällen; ein Recherchetool (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, Westlaw DE) verlagert Verifikationsarbeit aus deiner Hand.

Mitgeliefert wird:

- **Slack** – Nachrichten suchen, Kanäle lesen, Diskussionen finden
- **Google Drive** – Dokumente suchen, lesen und abrufen
- **Box** – Datenraum und Dokumentenverwaltung

Datasite, Intralinks und weitere VDR-Connectoren können in `.mcp.json` ergänzt werden, wenn Partner-URLs verfügbar sind.

## Recht und Quellen

Maßgebliche Gesetze dieses Plugins:

- **GmbHG** – Gesetz betreffend die Gesellschaften mit beschränkter Haftung
- **AktG** – Aktiengesetz
- **HGB** – Handelsgesetzbuch (§§ 238 ff. Buchführung, §§ 290 ff. Konzernabschluss, § 325 Bilanzpublizität)
- **UmwG** – Umwandlungsgesetz (Verschmelzung, Spaltung, Formwechsel)
- **WpÜG** – Wertpapiererwerbs- und Übernahmegesetz (öffentliche Übernahmen, Pflichtangebote)
- **MoPeG** – Gesetz zur Modernisierung des Personengesellschaftsrechts (GbR-Reform 2024)
- **WEG** – Wohnungseigentumsgesetz (soweit gesellschaftsrechtlich relevant)
- **GwG** – Geldwäschegesetz (Transparenzregister § 20 GwG)

Zitierweise nach `../references/zitierweise.md` (BGH-Stil).

## Lernen

Dein Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich mit der Nutzung des Plugins. Skills informieren dich, wenn ein Ergebnis einen Standard verwendet, den du anpassen solltest. Du kannst das Setup erneut ausführen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine neue Position zu speichern.

## M&A-Hinweise

- Die Issue-Extraktion wendet Wesentlichkeitsschwellen an – nicht jedes Dokument wird gelesen, wenn die Schwelle Top-N nach Wert vorschreibt.
- Käufer- und Verkäuferseite werden beide unterstützt. Das Praxisprofil erfasst, welche Seite für dieses Mandat gilt; Skills passen ihre Haltung entsprechend an.
- **Due Diligence:** DD läuft über Q&A-Prozess, Datenraum (VDR), Disclosure Letter und gesetzliche Auskunftsansprüche (§§ 242, 259, 666 BGB; Art. 15 DSGVO). Auskunftsansprüche im Streitfall: §§ 142, 144 ZPO; § 254 ZPO (Stufenklage).
- KI-Tool-Übergabe (Luminance/Kira) ist optional. Wenn das Praxisprofil kein Tool angibt, läuft alle Extraktion über den direkten Skill.
- Die Vollzugscheckliste wird aus dem SPA initialisiert und aktualisiert sich selbst, wenn die DD Zustimmungserfordernisse aufdeckt.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agio-und-kapitalruecklage` | Echtes (korporatives) und unechtes (schuldrechtliches) Agio in der GmbH bei Gründung und Kapitalerhöhung; § 3 Abs. 2 GmbHG als Anker; § 272 Abs. 2 Nr. 1 vs. Nr. 4 HGB; Sachagio im Rahmen des qualifizierten Anteilstauschs nach § 21 UmwStG... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Gesellschaftsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `aufsichtsrat-protokoll` | 'Erstellt Protokolle von Vorstandssitzungen (AG), Aufsichtsratssitzungen (AG, § 107 AktG) und Gesellschafterversammlungen (GmbH, § 48 GmbHG) im Hausformat. Erkennt bevorstehende Organsitzungen aus dem Kalender, fragt nach Tagesordnung un... |
| `dd-findings-extraktion` | Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und Wesentlichkeitsschwellen im Findings-Report-Format. Laden wenn der Nutzer Datenraum prüfen, DD-Issues extrahieren aus [Ordner], Due-Diligence-Prüfung oder was is... |
| `dealteam-zusammenfassung` | Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status für Geschäftsführung, Team-Update, Deal-Team-Summary. |
| `geschaeftsfuehrer-haftung-43-gmbhg` | Geschäftsführer haftet persoenlich oder Gesellschaft klagt gegen ihn auf Schadensersatz nach Insolvenz. Prüfraster § 43 GmbHG Sorgfalt ordentlicher Geschäftsmann Business Judgement Rule analog § 93 Abs. 1 Satz 2 AktG. Insolvenzantragspfl... |
| `gesellschafterbeschluss` | Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrheitserfordernisse, Beschlussfähigkeit, Formfragen, Protokollführung sowie Nichtigkeit (241 AktG analog) und Anfechtba... |
| `gesellschafterstreit-loesungsstrategie` | Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38 GmbHG. Normen § 34... |
| `gesellschafts-compliance` | 'Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach Rechtsträger und Rech... |
| `gesellschaftsrecht-anpassen` | 'Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil, Eskalationskontakte, aktive Module (M&A / Governance / Kapita... |
| `gesellschaftsrecht-kaltstart-interview` | Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst Tätigkeitsbereiche (M&A, Gesellschafterversammlung/Aufsichtsrat, Kapitalmarkt, Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Hausstil und Eskalations... |
| `gesellschaftsrecht-mandat-arbeitsbereich` | 'Mandats-Workspaces verwalten — anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen, damit Mehrfachmandatsanwälte den Kontext eines Mandats sauber von jedem anderen trennen. Wird von allen inhaltlichen Skills gelesen,... |
| `gesr-corporate-governance-kodex-spezial` | Spezialfall Corporate-Governance-Kodex: Empfehlungen, Anregungen, Entsprechenserklaerung § 161 AktG. Pruefraster fuer boersennotierten Vorstand und Aufsichtsrat. |
| `gesr-gesellschafterversammlung-protokoll-leitfaden` | Leitfaden Protokoll Gesellschafterversammlung GmbH: Einberufung, Tagesordnung, Beschluesse, Anfechtung. Pruefraster fuer Geschaeftsfuehrer und Berater. |
| `gesr-gesellschaftsformwahl-bauleiter` | Bauleiter Gesellschaftsformwahl: GmbH, UG, GmbH und Co. KG, AG, eG, Stiftung. Pruefraster Haftung, Steuern, Mitbestimmung, Publizitaet. Entscheidungstabelle. |
| `gesr-kgaa-und-se-spezial` | Spezialfall KGaA und SE: Hybridform, Vorstandsbestellung, Mitbestimmungsfreiheit der SE. Pruefraster fuer Family Office und boersennotierte Gruppe. |
| `gmbh-gruendung` | Begleitung der GmbH-Gründung von der Satzungserstellung (§ 2 GmbHG) bis zur Eintragung ins Handelsregister (§ 7 GmbHG) einschließlich UG-Variante (§ 5a GmbHG), Gewerbeanmeldung und Transparenzregister. Lädt bei Mandaten zur Neugründung,... |
| `handelsregisteranmeldung` | Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen; Eintragungsgrundätze und W... |
| `integrations-management` | 'Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste. Berücksichtigt § 613a BGB... |
| `ki-werkzeug-uebergabe` | 'KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer "Luminance", "Kira", "KI-Prüfung", "automatische Extraktion" oder "Massenprüfung" erwähnt oder der Datenraum mehr als ~50 Verträge enthält, die e... |
| `mandat-triage-gesellschaftsrecht` | Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert Mandantenrolle (Gesellschafter G... |
| `schriftliche-beschlussfassung` | 'Entwirft Beschlüsse im schriftlichen Verfahren (§ 48 Abs. 2 GmbHG) oder Umlaufbeschlüsse im Hausstil mit Präzedenzsuche im Beschlussarchiv. Bei der AG: Hinweis, dass HV-Beschlüsse Präsenz oder virtuelle HV (§ 118a AktG) erfordern und no... |
| `spezial-anmeldungen-verhandlung-vergleich-und-eskalation` | Anmeldungen: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-arbeitsbereich-mandantenentscheidung` | Arbeitsbereich: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-checklists-zahlen-schwellen-und-berechnung` | Checklists: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-closing-livequellen-und-rechtsprechungscheck` | Closing: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-compliance-compliance-dokumentation-und-akte` | Compliance: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-datenraum-behoerden-gericht-und-registerweg` | Datenraum: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-diligence-dokumentenmatrix-und-lueckenliste` | Diligence: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-discovery-risikoampel-und-gegenargumente` | Discovery: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fristen-mehrparteien-konflikt-und-interessen` | Fristen: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gesellschafterbeschluesse-textbausteine` | Gesellschafterbeschluesse: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gesellschafterstreit-international-schnittstellen` | Gesellschafterstreit: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gesellschaftsrecht-erstpruefung-und-mandatsziel` | Gesellschaftsrecht: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gmbh-tatbestand-beweis-und-belege` | GmbH: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-handelsregisteranmeldung-frist-naechster-schritt` | Handelsregisteranmeldung: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-livecheck-sonderfall-und-edge-case` | Livecheck: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-loesungsstrategie-formular-portal-und-einreichung` | Loesungsstrategie: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mandat-red-team-und-qualitaetskontrolle` | Mandat: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-personengesellschaften-fristen-form-und-zustaendigkeit` | Personengesellschaften: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsquellen-beweislast-und-darlegungslast` | Rechtsquellen: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `tabellenpruefung` | 'Tabellarisches Vertragsreview als Prompt-Matrix — pro Spalte ein Extraktionsprompt (was wird gefragt), pro Zeile ein dokumentspezifischer Prompt (wie wird dieses Dokument behandelt). Eine Zeile pro Dokument, eine Spalte pro Datenpunkt,... |
| `vollzugs-checkliste` | 'Vollzugscheckliste für M&A-Transaktionen nach deutschem Recht – was blockiert den Vollzug (Closing), kritischer Pfad, Tage bis Vollzug. Selbstaktualisierend: nimmt neue Einträge aus DD-Findings und Anlage-Erstellung auf. Trigger: "Vollz... |
| `wesentliche-vertraege-anlage` | 'Erstellt das Verzeichnis wesentlicher Verträge (Material Contracts Schedule) aus Due-Diligence-Erkenntnissen auf Grundlage der SPA-Definition und des Anhangformats. Berücksichtigt Change-of-Control-Klauseln (BGH-Rspr.), Vendor-Disclosur... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin gesellschaftsrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin gesellschaftsrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin gesellschaftsrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin gesellschaftsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin gesellschaftsrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin gesellschaftsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin gesellschaftsrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin gesellschaftsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin gesellschaftsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin gesellschaftsrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
