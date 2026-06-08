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
| **NeuroChain Labs — Gründung eines KI/Krypto-Startups in Berlin, Musterprotokoll vs. individuelle Satzung** (`gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/gesamt-pdf/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll_gesamt.pdf) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip) |
| **Roeschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation** (`gesellschaftsgruender-streit-roeschen-tech`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) |
| **Akte Kometenfalter Systems GmbH — Series A Project Comet Moth** (`gesellschaftsrecht-legal-english-frankfurt-startup`) | [Gesamt-PDF lesen](../testakten/gesellschaftsrecht-legal-english-frankfurt-startup/gesamt-pdf/gesellschaftsrecht-legal-english-frankfurt-startup_gesamt.pdf) | [`testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |
| **Handelsrecht HGB — Elbwerft Solar: eGbR, OHG-Statuswechsel, KG und Handelskauf** (`handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona`) | [Gesamt-PDF lesen](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/gesamt-pdf/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona_gesamt.pdf) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip) |
| **Mandatsbeziehung Nordstern BioTherapeutics — Kanzlei Falkenried** (`mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech`) | [Gesamt-PDF lesen](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/gesamt-pdf/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech_gesamt.pdf) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip) |
| **Codeforst / Sonnenklee - RouteLuchs** (`softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen`) | [Gesamt-PDF lesen](../testakten/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen/gesamt-pdf/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen_gesamt.pdf) | [`testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Abläufe für gesellschaftsrechtliche Mandate in deutschen Kanzleien und Rechtsabteilungen: M&A-Transaktionen, Organe und Protokollwesen, Gesellschafts-Compliance und Unternehmensführung. Aktiviere nur die Module, die für deine Praxis relevant sind. Das Kaltstart-Interview ist modular – es stellt gezielte Fragen je aktivem Bereich und schreibt nur die entsprechenden Abschnitte in dein Praxisprofil.

**Jedes Ergebnis ist ein Entwurf zur anwaltlichen Überprüfung – zitiert, markiert und gesperrt – kein Rechtsgutachten.** Das Plugin übernimmt die Arbeit: liest Dokumente, wendet dein Playbook an, findet die Issues, erstellt den Bericht. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Zitate sind mit Quellen gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu prüfen sind. Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB) wird konservativ gewahrt. Folgenreiche Handlungen – Einreichung, Versendung, Beurkundung – werden durch ausdrückliche Bestätigung gesperrt.


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

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agio-und-kapitalruecklage` | Echtes (korporatives) und unechtes (schuldrechtliches) Agio in der GmbH bei Gründung und Kapitalerhöhung; § 3 Abs. 2 GmbHG als Anker; § 272 Abs. 2 Nr. 1 vs. Nr. 4 HGB; Sachagio im Rahmen des qualifizierten Anteilstauschs nach § 21 UmwStG... |
| `anmeldungen-verhandlung-vergleich-und-eskalation` | Anmeldungen: Verhandlung, Vergleich und Eskalation im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `anpassen` | Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil, Eskalationskontakte, aktive Module (M&A / Governance / Kapital... |
| `anschluss` | Einstieg, Schnelltriage und Fallrouting im Gesellschaftsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Doku... |
| `arbeitsbereich-mandantenentscheidung` | Arbeitsbereich: Mandantenkommunikation und Entscheidungsvorlage im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse... |
| `aufsichtsrat-protokoll` | Erstellt Protokolle von Vorstandssitzungen (AG), Aufsichtsratssitzungen (AG, § 107 AktG) und Gesellschafterversammlungen (GmbH, § 48 GmbHG) im Hausformat. Erkennt bevorstehende Organsitzungen aus dem Kalender, fragt nach Tagesordnung und... |
| `beirat-abgrenzung-aufsichtsrat` | GmbH-Beirat: Beirat Abgrenzung Aufsichtsrat; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-amtszeit-und-rotation` | GmbH-Beirat: Beirat Amtszeit Und Rotation; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-bank-und-sanierung` | GmbH-Beirat: Beirat Bank Und Sanierung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-beratungsfunktion-beschlussfassung` | GmbH-Beirat: Beirat Beratungsfunktion; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-beschlussfassung` | GmbH-Beirat: Beirat Beschlussfassung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-beschlussmaengel` | GmbH-Beirat: Beirat Beschlussmaengel; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-bestellung-und-abberufung` | GmbH-Beirat: Beirat Bestellung Und Abberufung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-budget-und-businessplan` | GmbH-Beirat: Beirat Budget Und Businessplan; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-datenschutz-und-ki` | GmbH-Beirat: Beirat Datenschutz Und KI; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-deadlock-mechanik` | GmbH-Beirat: Beirat Deadlock Mechanik; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-entscheidungsbefugnisse` | GmbH-Beirat: Beirat Entscheidungsbefugnisse; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-fakultativer-aufsichtsrat-52-gmbhg` | GmbH-Beirat: Beirat Fakultativer Aufsichtsrat 52 Gmbhg; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-familiengesellschaft` | GmbH-Beirat: Beirat Familiengesellschaft; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-geschaeftsfuehrerabberufung` | GmbH-Beirat: Beirat Geschaeftsfuehrerabberufung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-geschaeftsfuehrerbestellung` | GmbH-Beirat: Beirat Geschaeftsfuehrerbestellung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-geschaeftsordnung` | GmbH-Beirat: Beirat Geschaeftsordnung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-haftung` | GmbH-Beirat: Beirat Haftung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-immobilien-und-investitionen` | GmbH-Beirat: Beirat Immobilien Und Investitionen; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-informationsrechte-insolvenznaehe` | GmbH-Beirat: Beirat Informationsrechte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-insolvenznaehe` | GmbH-Beirat: Beirat Insolvenznaehe; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-interessenkonflikte` | GmbH-Beirat: Beirat Interessenkonflikte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-internal-investigation-datenschutz-ki` | GmbH-Beirat: Beirat Compliance Und Internal Investigation; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-kaltstart-und-zielbild` | Beirat Kaltstart Und Zielbild: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `beirat-katalog-wesentlicher-geschaefte` | GmbH-Beirat: Beirat Katalog Wesentlicher Geschaefte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-kontrollfunktion` | GmbH-Beirat: Beirat Kontrollfunktion; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-mitbestimmung-abgrenzung-nachfolge` | GmbH-Beirat: Beirat Mitbestimmung Abgrenzung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-musterklauseln-haftung` | GmbH-Beirat: Beirat Musterklauseln; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-nachfolge` | GmbH-Beirat: Beirat Nachfolge; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-private-equity-investor` | GmbH-Beirat: Beirat Private Equity Investor; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-red-team-satzung` | GmbH-Beirat: Beirat Red Team Satzung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-register-und-notar` | GmbH-Beirat: Beirat Register Und Notar; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-satzungsgrundlage-sitzung-protokoll` | GmbH-Beirat: Beirat Satzungsgrundlage; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-sitzung-und-protokoll` | GmbH-Beirat: Beirat Sitzung Und Protokoll; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-startup-investor-director` | GmbH-Beirat: Beirat Startup Investor Director; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-streit-gesellschafter` | GmbH-Beirat: Beirat Streit Gesellschafter; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-transaktionen-ma` | GmbH-Beirat: Beirat Transaktionen M&A; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-verguetung-verschwiegenheit-veto` | GmbH-Beirat: Beirat Verguetung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-verschwiegenheit` | GmbH-Beirat: Beirat Verschwiegenheit; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-veto-rechte` | GmbH-Beirat: Beirat Veto Rechte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `beirat-zustimmungsvorbehalte` | GmbH-Beirat: Beirat Zustimmungsvorbehalte; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output im Gesellschaftsrecht. |
| `checklists-zahlen-schwellen-und-berechnung` | Checklists: Zahlen, Schwellenwerte und Berechnung im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nut... |
| `closing-quellenkarte` | Closing Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `compliance-compliance-dokumentation-und-akte` | Compliance: Compliance-Dokumentation und Aktenvermerk im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `datenraum-behoerden-gericht-und-registerweg` | Datenraum: Behörden-, Gerichts- oder Registerweg im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutz... |
| `dd-findings-extraktion` | Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und Wesentlichkeitsschwellen im Findings-Report-Format. Laden wenn der Nutzer Datenraum prüfen, DD-Issues extrahieren aus [Ordner], Due-Diligence-Prüfung oder was is... |
| `dealteam-zusammenfassung` | Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status für Geschäftsführung, Team-Update, Deal-Team-Summary im Gese... |
| `diligence-dokumentenmatrix-und-lueckenliste` | Diligence: Dokumentenmatrix, Lückenliste und Nachforderung im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `discovery-gesellschafterbeschluesse` | Discovery: Risikoampel, Gegenargumente und Verteidigungslinien im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse u... |
| `dokumente-intake` | Dokumentenintake für Gesellschaftsrecht: sortiert Satzung, Geschäftsführerdienstvertrag, Hauptversammlungsprotokoll, prüft Datum, Absender, Frist und Beweiswert (HR-Auszug, Gesellschafterbeschluss); markiert Lücken; berücksichtigt Mandat... |
| `einstieg-routing` | Einstieg, Triage und Routing für Gesellschaftsrecht: ordnet Rolle (Gesellschafter/Aktionäre, Geschäftsführung/Vorstand, Aufsichtsrat), markiert Frist (Anfechtungsklage 1 Monat § 246 AktG), wählt Norm (GmbHG, AktG, HGB, BGB §§ 705 ff., Um... |
| `fristen-mehrparteien-konflikt-und-interessen` | Fristen: Mehrparteienkonflikt und Interessenmatrix im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `geschaeftsfuehrer-haftung-43-gmbhg` | Geschäftsführer haftet persoenlich oder Gesellschaft klagt gegen ihn auf Schadensersatz nach Insolvenz. Prüfraster § 43 GmbHG Sorgfalt ordentlicher Geschäftsmann Business Judgement Rule analog § 93 Abs. 1 Satz 2 AktG. Insolvenzantragspfl... |
| `gesellschafterbeschluesse-textbausteine` | Gesellschafterbeschluesse: Schriftsatz-, Brief- und Memo-Bausteine im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbrem... |
| `gesellschafterbeschluss` | Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrheitserfordernisse, Beschlussfähigkeit, Formfragen, Protokollführung sowie Nichtigkeit (241 AktG analog) und Anfechtba... |
| `gesellschafterliste-registerstreit-legitimationswirkung` | Prüft § 16 und § 40 GmbHG, unrichtige Listen, Einziehung, Abtretung, Notar-/Registerrolle, einstweilige Verfügung und praktische Vollzugssperren im Gesellschaftsrecht. |
| `gesellschafterstreit-international-schnittstellen` | Gesellschafterstreit: Internationaler Bezug und Schnittstellen im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse u... |
| `gesellschafterstreit-loesungsstrategie` | Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38 GmbHG. Normen § 34... |
| `gesellschafts-compliance` | Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach Rechtsträger und Recht... |
| `gesellschaftsrecht-erstpruefung-und-mandatsziel` | Gesellschaftsrecht: Erstprüfung, Rollenklärung und Mandatsziel im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse u... |
| `gesr-corporate-governance-kodex-spezial` | Spezialfall Corporate-Governance-Kodex: Empfehlungen, Anregungen, Entsprechenserklaerung § 161 AktG. Pruefraster für boersennotierten Vorstand und Aufsichtsrat im Gesellschaftsrecht. |
| `gesr-gesellschafterversammlung-protokoll-leitfaden` | Leitfaden Protokoll Gesellschafterversammlung GmbH: Einberufung, Tagesordnung, Beschluesse, Anfechtung. Pruefraster für Geschaeftsfuehrer und Berater im Gesellschaftsrecht. |
| `gesr-gesellschaftsformwahl-aufsichtsrat` | Bauleiter Gesellschaftsformwahl: GmbH, UG, GmbH und Co. KG, AG, eG, Stiftung. Pruefraster Haftung, Steuern, Mitbestimmung, Publizitaet. Entscheidungstabelle im Gesellschaftsrecht. |
| `gesr-kgaa-und-se-spezial` | Spezialfall KGaA und SE: Hybridform, Vorstandsbestellung, Mitbestimmungsfreiheit der SE. Pruefraster für Family Office und boersennotierte Gruppe im Gesellschaftsrecht. |
| `gmbh-gruendung` | Begleitung der GmbH-Gründung von der Satzungserstellung (§ 2 GmbHG) bis zur Eintragung ins Handelsregister (§ 7 GmbHG) einschließlich UG-Variante (§ 5a GmbHG), Gewerbeanmeldung und Transparenzregister. Lädt bei Mandaten zur Neugründung,... |
| `gmbh-tatbestand-beweis-und-belege` | GmbH: Tatbestandsmerkmale, Beweisfragen und Beleglage im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `handelsregisteranmeldung-frist-naechster-schritt` | Handelsregisteranmeldung: Fristennotiz und nächster Schritt im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und... |
| `handelsregisteranmeldung-integrations` | Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen; Eintragungsgrundätze und W... |
| `integrations-management` | Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste. Berücksichtigt § 613a BGB (... |
| `kaltstart-interview` | Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst Tätigkeitsbereiche (M&A, Gesellschafterversammlung/Aufsichtsrat, Kapitalmarkt, Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Hausstil und Eskalations... |
| `ki-werkzeug-uebergabe` | KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer Luminance, Kira, KI-Prüfung, automatische Extraktion oder Massenprüfung erwähnt oder der Datenraum mehr als ~50 Verträge enthält, die ein einheitl... |
| `livecheck-sonderfall-loesungsstrategie-mandat` | Livecheck: Sonderfall und Edge-Case-Prüfung im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `loesungsstrategie-formular-portal-und-einreichung` | Loesungsstrategie: Formular, Portal und Einreichungslogik im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und di... |
| `mandat-arbeitsbereich-gesr-corporate` | Mandats-Workspaces verwalten — anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen, damit Mehrfachmandatsanwälte den Kontext eines Mandats sauber von jedem anderen trennen. Wird von allen inhaltlichen Skills gelesen,... |
| `mandat-red-team-und-qualitaetskontrolle` | Mandat: Red-Team und Qualitätskontrolle im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arb... |
| `mandat-triage-gesellschaftsrecht` | Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert Mandantenrolle (Gesellschafter G... |
| `output-waehlen-workflow-redteam-interessen` | Output wählen: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung im Gesellschaftsrecht. |
| `personengesellschaften-fristen-form-und-zustaendigkeit` | Personengesellschaften: Fristen, Form, Zuständigkeit und Rechtsweg im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbrem... |
| `quellen-livecheck` | Quellen-Live-Check für Gesellschaftsrecht: prüft Normen (GmbHG, AktG, HGB, BGB §§ 705 ff., UmwG, MitbestG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Handelsregister und Quellenhygiene nach references/quellen... |
| `rechtsabteilung-beirat-mit-vetorechten-in-der-gmbh` | Rechtsabteilungs-Fachmodul für Beirat mit Vetorechten in der GmbH: Beiratsrechte werden zwischen Beratung, Zustimmung, Weisung und faktischer Geschäftsführung abgegrenzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlu... |
| `rechtsabteilung-geschaeftsfuehrerhaftung-fuer-compliance-versage` | Rechtsabteilungs-Fachmodul für Geschäftsführerhaftung für Compliance-Versagen: Compliance-Redflags werden in Organpflichten, Ressortverteilung und D&O-Meldung übersetzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlun... |
| `rechtsabteilung-gesellschafterliste` | Rechtsabteilungs-Fachmodul für Gesellschafterliste und Registerstreit: Liste, Legitimationswirkung, Widerspruch und Registersperre werden als Fristenplan bearbeitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsop... |
| `rechtsabteilung-kapitalerhoehung-mit-bezugsrechtsausschluss` | Rechtsabteilungs-Fachmodul für Kapitalerhöhung mit Bezugsrechtsausschluss: Minderheitenschutz, Verwässerung, Bewertungsunterlagen und Eilrechtsschutz werden geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsop... |
| `rechtsabteilung-stimmbindung-und-beschlussmangel-nach-hannover-9` | Rechtsabteilungs-Fachmodul für Stimmbindung und Beschlussmangel nach Hannover-96-Linie: Rechtsabteilungen trennen Satzungsverstoß, schuldrechtliche Stimmbindung und Anfechtbarkeit. Mit Normen, Rechtsprechungsanker, Belegmatrix und schnel... |
| `rechtsquellen-beweislast-darlegungslast` | Rechtsquellen: Beweislast, Darlegungslast und Substantiierung im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse un... |
| `schriftliche-beschlussfassung` | Entwirft Beschlüsse im schriftlichen Verfahren (§ 48 Abs. 2 GmbHG) oder Umlaufbeschlüsse im Hausstil mit Präzedenzsuche im Beschlussarchiv. Bei der AG: Hinweis, dass HV-Beschlüsse Präsenz oder virtuelle HV (§ 118a AktG) erfordern und not... |
| `tabellenpruefung-cap-table` | 'Tabellarisches Vertragsreview als Prompt-Matrix — pro Spalte ein Extraktionsprompt (was wird gefragt), pro Zeile ein dokumentspezifischer Prompt (wie wird dieses Dokument behandelt). Eine Zeile pro Dokument, eine Spalte pro Datenpunkt,... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Gesellschaftsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Satzung, Geschäftsführerdienstvertrag, Hauptversammlungsprotokoll), nennt pro Lücke Beweisthema, Beschaffungsweg (Handelsregister), Fr... |
| `vollzugs-checkliste` | Vollzugscheckliste für M&A-Transaktionen nach deutschem Recht – was blockiert den Vollzug (Closing), kritischer Pfad, Tage bis Vollzug. Selbstaktualisierend: nimmt neue Einträge aus DD-Findings und Anlage-Erstellung auf. Trigger: Vollzug... |
| `wesentliche-vertraege` | Wesentliche Vertraege im Plugin Gesellschaftsrecht im Gesellschaftsrecht. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Gesellschaftsrecht. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Gesellschaftsrecht. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Gesellschaftsrecht. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Gesellschaftsrecht. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Gesellschaftsrecht. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
