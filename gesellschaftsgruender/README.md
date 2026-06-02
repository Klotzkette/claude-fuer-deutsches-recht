# gesellschaftsgründer — Gründungsassistent für deutsche Gesellschaften

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`gesellschaftsgruender`) | [`gesellschaftsgruender.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsgruender.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **NeuroChain Labs — Gründung eines KI/Krypto-Startups in Berlin, Musterprotokoll vs. individuelle Satzung** (`gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/gesamt-pdf/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll_gesamt.pdf) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip) |
| **Roeschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation** (`gesellschaftsgruender-streit-roeschen-tech`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) |
| **Handelsrecht HGB — Elbwerft Solar: eGbR, OHG-Statuswechsel, KG und Handelskauf** (`handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona`) | [Gesamt-PDF lesen](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/gesamt-pdf/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona_gesamt.pdf) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes, anfängerfreundliches und zugleich professionelles Plugin für die Gründung und frühe Führung deutscher Gesellschaften. Es hilft beim ersten Sortieren ebenso wie bei einem fast fertigen Gründungspaket: Rechtsformwahl, Rollen der Gründerinnen und Gründer, Satzung, Gesellschaftervereinbarung, Cap Table, Notar, Handelsregister, Bank/KYC, Behörden, Steuerstart, IP, Datenschutz, erste 100 Tage und Streitprävention.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `gesellschaftsgruender.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte die Gesellschaftsgründung. Ich habe drei Gründer, eine GmbH-Idee und noch keine Satzung.`

Alternativ via Marketplace:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install gesellschaftsgruender@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und das Verzeichnis `skills/` enthalten.

## So Startet Es

Der `allgemein`-Skill beginnt bewusst leicht. Er fragt nicht sofort nach allen juristischen Details, sondern sortiert zuerst:

1. **Wer gründet?** Personen, Rollen, Wohnsitz, Auslandsbezug, Minderjährige, Treuhand, Familien- oder Investorensituation.
2. **Was soll die Gesellschaft tun?** Geschäftszweck, reguliertes Geschäft, IP, Daten, KI, Produkt, Finanzierung, Personal.
3. **Welche Rechtsform liegt nahe?** GmbH, UG, eGbR, OHG, KG, GmbH & Co. KG, PartG mbB, gGmbH, eG, AG, Holding oder Sonderstruktur.
4. **Was muss jetzt zuerst passieren?** Notarbriefing, Gesellschaftsvertrag, Bankkonto, Transparenzregister, Steuererfassung, Gewerbe, IHK/BG, Versicherungen.
5. **Wo brennt es?** Registerbeanstandung, Gründerstreit, KYC-Blockade, IP-Lücke, Sacheinlage, Stammkapitalverlust, Liquiditätsproblem.

Das Plugin schlägt danach aktiv die passenden Anschluss-Skills vor, statt die Nutzerin oder den Nutzer mit einer langen Skillliste allein zu lassen.

## Arbeitsphasen

| Phase | Ziel | Typische Outputs |
| --- | --- | --- |
| **0 Intake** | Idee, Beteiligte, Geld, Risiko und Zeitplan verstehen | One-Page-Roadmap, Rückfragenliste, Risikoampel |
| **1 Rechtsform** | passende Struktur auswählen und falsche Abzweigungen vermeiden | Rechtsformmatrix, Entscheidungsvorlage, Stoppschilder |
| **2 Dokumente** | Gründungspaket bauen | Satzung, SHA, Geschäftsführerunterlagen, Gesellschafterliste, Notarbriefing |
| **3 Vollzug** | Notar, Register, Bank, Behörden und Steuerstart koordinieren | Closing-Checkliste, KYC-Paket, ELSTER-/Gewerbe-/BG-Liste |
| **4 Betrieb** | erste 100 Tage sauber organisieren | Board Pack, Beschlussvorlagen, Versicherungs- und Compliance-Check |
| **5 Konflikt** | Streit früh erkennen und kontrolliert eskalieren | Deadlock-Matrix, Mediationsplan, Eilmaßnahmen-Check, Registerstrategie |

## Skillgruppen

- **Einstieg und Anfängerführung:** Kaltstart, einfache Sprache, One-Page-Roadmap, Gründerrollen, Mandantenbrief, Checkliste vor Unterschrift.
- **Rechtsformen:** GmbH, UG, eGbR, OHG, KG, GmbH & Co. KG, PartG mbB, gGmbH, eG, AG, SE und Holdingmodelle.
- **Dokumente und Vollzug:** Satzung, Gesellschaftervereinbarung, Geschäftsführervertrag, Geschäftsordnung, Gesellschafterliste, Notarbriefing, Registerbeanstandung.
- **Finanzierung und Beteiligung:** Cap Table, Seed-Runde, Wandeldarlehen, Founder Vesting, Leaver, ESOP/VSOP, Vinkulierung, Drag/Tag, Bezugsrechte.
- **Risikothemen:** Auslandsgründer, KYC, Sanktionen, Transparenzregister, Sacheinlagen, IP-Übertragung, Open Source, Datenschutz/KI, regulierte Geschäftsmodelle.
- **Operativer Start:** Bankkonto, Steuerliche Erfassung, Umsatzsteuer, Payroll, Mietvertrag, Kundenstart, Produkthaftung, Versicherungen, Cash Burn und Insolvenzfrühwarnung.

## Demonstrationsakte

Die Akte `gesellschaftsgruender-streit-roeschen-tech` zeigt eine Gründung, die nicht lehrbuchartig glatt läuft: drei Gründer, ein technisches Produkt, IP-Fragen, Series-A-Druck, B-Shares, Bezugsrechtsstreit, KYC-Rückfragen, Registerlogik, Gründer-Vesting, Leaver-Risiken, Datenschutz-/KI-Fragen und ein Konflikt, der parallel über Notar, Bank, Investorin, Beirat und Registergericht läuft.

Sie enthält unter anderem Satzungsentwurf, Gesellschaftervereinbarung, Cap-Table-Varianten, E-Mails, Register-/Notarvermerke, KYC-Nachfragen, IP-/Open-Source-Notizen, Vesting-Matrix, Board Pack, Cash-Burn-Übersicht, Compliance-Startliste, CSV-Tabellen und ein Gesamt-PDF.

## Stoppschilder

- **Notar:** Beurkundung, Handelsregisteranmeldung und bestimmte Vollmachten müssen notariell laufen.
- **Steuer:** Rechtsform, Holding, Sacheinlage, ESOP/VSOP, USt und Verrechnungspreise gehören früh in steuerkundige Hände.
- **Aufsicht und Erlaubnis:** Finanzen, Versicherung, Kryptowerte, Zahlungsdienste, Medizin, Bewachung, Handwerk, Lebensmittel, Transport und ähnliche Modelle brauchen einen Erlaubnischeck vor dem Start.
- **Krise:** Bei Zahlungsunfähigkeit, Überschuldung, hälftigem Stammkapitalverlust oder Liquiditätslücke geht es nicht mehr nur um Gründung, sondern um Organhaftung und Insolvenzrecht.
- **Streit:** Bei Gesellschafterstreit, Registerblockade oder Investorendruck braucht es eine Beweis-, Fristen- und Eskalationsstrategie.

## Quellenhygiene

Gesetzesstände, Registervorgaben, Formularwege und Behördenpraxis sind vor produktiver Verwendung live zu prüfen. Rechtsprechung wird nicht aus Modellwissen zitiert; sie muss vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle verifiziert werden.

Wichtige Startanker sind insbesondere BGB §§ 705 ff., HGB §§ 105 ff. und §§ 161 ff., GmbHG, AktG, PartGG, GenG, GwG/Transparenzregister, GewO, AO/UStG, SGB IV/SGB VII, InsO § 15a und die Register-/Notarvorgaben nach BeurkG und HRegV.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing für das Gesellschaftsgründer-Plugin; besonders anfängerfreundlich, mit Rollenklärung, Dokumentenintake, Rechtsformwahl und Anschluss-Skills. |
| `gesellschaftsgruender-ag-kleine-ag` | Prüft AG-Gründung, Satzung, Vorstand, Aufsichtsrat, Kapital und Investorenfähigkeit. |
| `gesellschaftsgruender-anfaenger-kaltstart` | Führt absolute Anfänger durch die ersten Entscheidungen einer Gesellschaftsgründung ohne Fachsprachenfalle. |
| `gesellschaftsgruender-aufloesung-liquidation-start` | Prüft geordnete Beendigung einer jungen Gesellschaft: Beschluss, Liquidatoren, Sperrjahr, Register, Gläubiger. |
| `gesellschaftsgruender-auslandsgesellschafter-kyc` | Prüft Gründung mit ausländischen Gesellschaftern: Dokumente, Apostille, Register, Sanktionen, UBO und Bank-KYC. |
| `gesellschaftsgruender-bankkonto-kyc-paket` | Erstellt Bankkonto-Unterlagenpaket für Gründung und Kapitalerhöhung. |
| `gesellschaftsgruender-beirat-advisory-board` | Beirat oder Advisory Board für GmbH oder UG einrichten: Satzungsregelung, Bestellungsverfahren, Beratungsvertrag. Normen: §§ 45 52 GmbHG, §§ 95 ff. AktG analog. Prüfraster: Kompetenzen, Verguetung, Haftung, Abberufung, Datenschutz. Outpu... |
| `gesellschaftsgruender-bilinguale-dokumente` | Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen: zweisprachige Satzung, Gesellschafterbeschluss, SHA. Normen: §§ 2 3 GmbHG, HGB. Prüfraster: rechtliche Verbindlichkeit der deutschen Fassung, Abweichungsregelung, Notar... |
| `gesellschaftsgruender-board-pack-erste-100-tage` | Erstellt Board-/Beiratsunterlagen für die ersten 100 Tage nach Gründung. |
| `gesellschaftsgruender-cap-table` | Cap-Table für GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Prüfraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output: Cap-Table-Tabelle m... |
| `gesellschaftsgruender-cashburn-insolvenzfruehwarnung` | Prüft Liquiditätsreichweite, Stammkapitalverlust, Zahlungsunfähigkeit und Überschuldungswarnungen. |
| `gesellschaftsgruender-checkliste-vor-unterschrift` | Letztes Qualitygate vor Satzung, SHA, GF-Vertrag, Bankformular oder Notartermin. |
| `gesellschaftsgruender-daten-und-ki-compliance-start` | Prüft Datenschutz, KI-VO, Datenquellen und Modellnutzung im Gründungsstadium. |
| `gesellschaftsgruender-deadlock-und-mediation` | Entwirft Deadlock-Mechanismen, Eskalationsleitern und Mediationsklauseln. |
| `gesellschaftsgruender-egbr-grundstueck` | Prüft eGbR bei Grundstückserwerb, Grundbuchfähigkeit, Register und Gesellschafterwechsel. |
| `gesellschaftsgruender-egbr-mopeg` | GbR nach MoPeG 2024 und Eintragung ins Gesellschaftsregister als eGbR vorbereiten. Normen: §§ 705 ff. BGB n.F. MoPeG, §§ 707 ff. BGB Gesellschaftsregister. Prüfraster: Eintragungsvoraussetzungen, Gesellschafterverzeichnis, Vertretungsreg... |
| `gesellschaftsgruender-familiengesellschaft` | Prüft Familien-GbR/GmbH/KG für Vermögen, Nachfolge, Minderjährige und Stimmrechte. |
| `gesellschaftsgruender-finanzierungsrunde-seed` | Führt durch Seed-Runde: Term Sheet, Bewertung, Verwässerung, Cap Table, Satzung, SHA, Closing. |
| `gesellschaftsgruender-firmenname-pruefung` | Firmenname auf Zulässigkeit und Verwechslungsgefahr prüfen: Differenzierungsgebot, Irreführungsverbot. Normen: §§ 17 18 HGB, § 4 GmbHG. Prüfraster: Unterscheidungskraft, Irreführungsverbot, Handelsregisterfähigkeit, Markenrecherche-Empfe... |
| `gesellschaftsgruender-founder-vesting` | Entwirft Founder-Vesting mit Cliff, Good/Bad Leaver und Rückübertragung. |
| `gesellschaftsgruender-freiberufler-partg-mbb` | Prüft Freiberuflerstrukturen, PartG, PartG mbB, Berufshaftpflicht und Berufsrecht. |
| `gesellschaftsgruender-gbr-zu-ohg-statuswechsel` | Prüft MoPeG-Statuswechsel von eGbR zu OHG/KG bei wachsendem Geschäftsbetrieb. |
| `gesellschaftsgruender-genehmigtes-kapital` | Genehmigtes Kapital für GmbH oder AG in Satzung aufnehmen: Ermaechtigungsbeschluss, Hoechstbetrag, Bezugsrechtsausschluss. Normen: §§ 55a GmbHG, §§ 202 ff. AktG. Prüfraster: Ermaechtigungsrahmen, Fristen, Bezugsrechte, Eintragungserforde... |
| `gesellschaftsgruender-genossenschaft-eg` | Prüft, ob eine eG statt GmbH/GbR sinnvoll ist. |
| `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` | Pflichten des GmbH-Geschäftsführers in Gründungs- und Startphase: Stammkapitaleinzahlung, Insolvenzantragspflicht, Buchführung. Normen: §§ 35 43 64 GmbHG, § 15a InsO. Prüfraster: Handlungspflichten, Haftungsrisiken, Compliance-Checkliste... |
| `gesellschaftsgruender-geschaeftsfuehrervertrag` | Geschäftsführervertrag für GmbH-Geschäftsführer aufsetzen: Verguetung, Wettbewerbsverbot, Abberufung, Kündigungsfristen. Normen: §§ 35 38 GmbHG, BGB Dienstvertrag. Prüfraster: Verguetungsstruktur, Tantieme, Freistellung, Geheimhaltung, P... |
| `gesellschaftsgruender-geschaeftsordnung-gf` | Geschäftsordnung für GmbH-Geschäftsführung entwerfen: Ressortzuteilung, Zustimmungsvorbehalte, Berichtspflichten. Normen: §§ 35 37 GmbHG. Prüfraster: Kompetenzbereiche, interne Beschraenkungen, Zustimmungskataloge. Output: Geschäftsordnu... |
| `gesellschaftsgruender-gesellschafterliste-qualitygate` | Prüft Gesellschafterliste, Nennbeträge, Nummerierung, Prozentangaben und Veränderungsspalten. |
| `gesellschaftsgruender-gesellschafterstreit-eilantraege` | Eilmassnahmen im Gesellschafterstreit der GmbH: einstweilige Verfuegung gegen Mitgesellschafter oder Geschäftsführer. Normen: §§ 935 940 ZPO, §§ 37 38 GmbHG. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Arrest vs. einstweilige Verf... |
| `gesellschaftsgruender-gesellschaftervereinbarung` | Gesellschaftervereinbarung (SHA) neben dem Gesellschaftsvertrag entwerfen: Vorkaufsrechte, Drag-Along, Tag-Along. Normen: §§ 705 ff. BGB, GmbHG. Prüfraster: schuldrechtliche Bindung, Satzungsrang, Durchsetzbarkeit, Vertragsstrafe. Output... |
| `gesellschaftsgruender-gesellschaftsvertrag-gmbh` | GmbH-Gesellschaftsvertrag aufsetzen: Mindestinhalt, Stammkapital, Beschlussfassung, Gewinnverteilung. Normen: §§ 2 3 5 GmbHG. Prüfraster: Notarerfordernis, Pflichtinhalte, Optionalklauseln, Sonderrechte. Output: GmbH-Gesellschaftsvertrag... |
| `gesellschaftsgruender-gewerbeanmeldung-finanzamt` | Gewerbeanmeldung und steuerliche Ersterfassung nach GmbH-Gründung vorbereiten: Fragebogen Finanzamt, Gewerbeamt. Normen: § 14 GewO, AO, UStG. Prüfraster: Steuerklassen, USt-Voranmeldung, Betriebsstaette, Umsatzsteuer-ID. Output: Ausfuell... |
| `gesellschaftsgruender-gf-meeting-templates` | Vorlagen für Geschäftsführersitzungen und Protokolle erstellen: Tagesordnung, Beschlussprotokoll, Aktionsliste. Normen: §§ 35 ff. GmbHG. Prüfraster: Beschlussfähigkeit, Umlaufverfahren, Dokumentationspflichten. Output: Meeting-Templates... |
| `gesellschaftsgruender-gf-sozialversicherungs-status` | Sozialversicherungsrechtlichen Status des GmbH-Geschäftsführers klaeren: Pflichtversicherung vs. Befreiung bei beherrschendem Gesellschafter-GF. Normen: § 7 SGB IV, §§ 1 ff. SGB VI. Prüfraster: Beteiligungshoehe, Weisungsabhaengigkeit, B... |
| `gesellschaftsgruender-ggmbh-gemeinnuetzigkeit` | Prüft gGmbH-Gründung, Satzungszweck, Mittelbindung und Finanzamt-Abstimmung. |
| `gesellschaftsgruender-gmbh-vorbereitung` | GmbH-Gründung vorbereiten: Gründerprüfung, Kapitalplanung, Notar-Auftrag, Gesellschafterliste. Normen: §§ 2 3 5 7 GmbHG. Prüfraster: Mindestkapital 25000 Euro, Einzahlungsnachweis, Gesellschafterkreis, Geschäftsführereignung. Output: Vor... |
| `gesellschaftsgruender-golden-share-und-vetorechte` | Golden Shares und Vetorechte in GmbH oder AG satzungsmäßig absichern: Sonderrechte, Sperrminoritaeten. Normen: §§ 35 45 GmbHG, §§ 23 ff. AktG. Prüfraster: Satzungsgestaltung, Grenzen der Satzungsautonomie, Bestandsschutz, Vinkulierung. O... |
| `gesellschaftsgruender-gruender-intake` | Ersterfassung des Gründungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschäftszweck. Normen: GmbHG, AktG, HGB. Prüfraster: Intake-Fragen Rechtsformwahl, Haftung, steuerliche Aspekte, Zeitplan. Output: Gründungsintake-Bogen. Ab... |
| `gesellschaftsgruender-gruenderrollen-konfliktcheck` | Klärt Rollen, Beiträge, Erwartungen, Streitpunkte und Exit-Szenarien vor Satzungsentwurf. |
| `gesellschaftsgruender-gv-einladung-tagesordnung` | Gesellschafterversammlungs-Einladung und Tagesordnung nach GmbHG erstellen: Fristen, Formen, Mindestinhalt. Normen: §§ 49 51 GmbHG. Prüfraster: Ladungsfrist, Schriftform, Tagesordnungspunkte, Beschlussfähigkeit. Output: GV-Einladungsschr... |
| `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` | Gesellschafterversammlungs-Protokoll anfertigen und Versammlungsleitung durchführen. Normen: §§ 48 ff. GmbHG. Prüfraster: Protokollierungspflicht, Abstimmungsergebnis, Unterschriften, Formfehler. Output: GV-Protokoll-Vorlage. Abgrenzung:... |
| `gesellschaftsgruender-handelsregister-anmeldung` | Erstanmeldung der GmbH zum Handelsregister vorbereiten: Notarauftrag, Eintragungsvoraussetzungen, Gründungsunterlagen. Normen: §§ 7 ff. GmbHG, §§ 12 ff. HGB. Prüfraster: Einzahlungsnachweis, Notarbeglaubigung, Gesellschafterliste, HR-For... |
| `gesellschaftsgruender-holdingmodell` | Prüft Holding vor operativer Gesellschaft, Beteiligungen, Steuer-/Haftungs- und Governancefragen. |
| `gesellschaftsgruender-ihk-und-berufsgenossenschaft` | IHK-Pflichtmitgliedschaft und Berufsgenossenschafts-Anmeldung nach GmbH-Gründung erledigen. Normen: §§ 2 ff. IHKG, §§ 150 ff. SGB VII. Prüfraster: Branchenzuordnung BG, IHK-Beitragspflicht, Fristen. Output: Checkliste IHK-Anmeldung und B... |
| `gesellschaftsgruender-intake-decision-tree` | Entscheidungsbaum für GmbH-Gründung: Rechtsformwahl, Gründungsweg, Kapitalausstattung. Normen: GmbHG, AktG, PartGG, HGB. Prüfraster: Haftung, Steuer, Kapital, Gesellschafteranzahl. Output: Entscheidungsmatrix Rechtsformwahl. Abgrenzung:... |
| `gesellschaftsgruender-investor-dd-vorbereiten` | Baut Datenraum für Investor-DD: Corporate, Finance, IP, HR, Datenschutz, Verträge. |
| `gesellschaftsgruender-ip-einbringung` | Prüft, ob Software, Marken, Designs, Domains und Know-how sauber in die Gesellschaft gelangen. |
| `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` | Kapitalerhöhung der GmbH mit und ohne Bezugsrecht der Gesellschafter durchführen. Normen: §§ 55 56 56a GmbHG. Prüfraster: Gesellschafterbeschluss, Bezugsrechtsausschluss, Einlageverpflichtung, Handelsregisteranmeldung. Output: Beschlussv... |
| `gesellschaftsgruender-kg-und-gmbhcokg` | KG und GmbH und Co. KG gründen: Gesellschaftsvertrag, Haftungsstruktur, steuerliche Transparenz. Normen: §§ 161 ff. HGB, GmbHG. Prüfraster: Komplementaer-GmbH, Kommanditistenstellung, steuerliche Behandlung. Output: KG-Gesellschaftsvertr... |
| `gesellschaftsgruender-klauselkatalog-bilingual` | Klauselkatalog für GmbH-Satzung und SHA in Deutsch und Englisch: Standardklauseln für internationale Investoren. Normen: GmbHG, BGB. Prüfraster: Drag-Along, Tag-Along, Liquidationspräferenzen, Leaver-Klauseln. Output: Klauselkatalog bili... |
| `gesellschaftsgruender-kommandocenter` | Navigationszentrum für alle Gründungs-Skills: Fortschrittsanzeige, Delegierung an Fachinhalte, Status. Normen: GmbHG, AktG, HGB. Prüfraster: aktueller Gründungsstand, offene Schritte, Notartermin, Eintragungsstatus. Output: Statusuebersi... |
| `gesellschaftsgruender-leaver-klauseln` | Prüft Good/Bad-Leaver-Klauseln, Abfindung, Einziehung und Durchsetzbarkeit. |
| `gesellschaftsgruender-lizenz-und-vertriebsstart` | Erstellt rechtliche Startliste für erste Kundenverträge, AGB, Datenschutz, IP und Gewährleistung. |
| `gesellschaftsgruender-lohn-payroll-start` | Prüft erste Beschäftigte, Minijob, SV-Meldung, Lohnkonto, BG und Arbeitsverträge. |
| `gesellschaftsgruender-mandantenbrief-naechste-schritte` | Schreibt verständlichen Gründerbrief mit Entscheidungen, Risiken, To-dos, Kosten und Zeitplan. |
| `gesellschaftsgruender-mietvertrag-buero-labor` | Prüft Mietvertrag vor Gründung/Eintragung, Vor-GmbH-Haftung und Genehmigungen. |
| `gesellschaftsgruender-minderjaehrige-gesellschafter` | Prüft Minderjährige in Gesellschaften: Vertretung, Familiengericht, Haftung und Genehmigungen. |
| `gesellschaftsgruender-mitarbeiter-gf-arbeitsvertrag` | Prüft Gründeranstellung, Geschäftsführervertrag, Sozialversicherung, IP und Wettbewerbsverbote. |
| `gesellschaftsgruender-mitarbeiterbeteiligung-esop-vsop` | Prüft Mitarbeiterbeteiligung, virtuelle Anteile, Vesting, Leaver und Steuer-/Arbeitsrechtsschnittstellen. |
| `gesellschaftsgruender-musterprotokoll-vs-satzung` | Entscheidet, ob Musterprotokoll reicht oder individuelle Satzung nötig ist. |
| `gesellschaftsgruender-notar-vorbereitung` | Notartermin für GmbH-Gründung vorbereiten: Unterlagencheck, Vollmachten, Ausweisanforderungen. Normen: §§ 2 7 GmbHG, BeurkG. Prüfraster: Gesellschafterliste, Musterprotokoll vs. individueller Gesellschaftsvertrag, Vollmachten. Output: No... |
| `gesellschaftsgruender-notarbriefing-onepager` | Erstellt ein Notarbriefing mit Firma, Sitz, Gegenstand, Kapital, Gesellschaftern, GF, Besonderheiten. |
| `gesellschaftsgruender-one-page-roadmap` | Erstellt eine einseitige Roadmap von Idee bis Eintragung und operativem Start. |
| `gesellschaftsgruender-online-gruendung-dirug` | Online-Gründung der GmbH nach DiRUG ohne persoenlichen Notartermin: Voraussetzungen, Verfahren, Grenzen. Normen: § 2 Abs. 3 GmbHG, DiRUG. Prüfraster: Musterprotokoll-Pflicht, Videoidentifikation, Beschraenkungen. Output: Checkliste Onlin... |
| `gesellschaftsgruender-open-source-startup` | Prüft Open-Source-Risiken vor Gründung, Finanzierung und Due Diligence. |
| `gesellschaftsgruender-plain-language-modus` | Übersetzt Gründungsrecht in einfache Sprache, ohne rechtliche Präzision zu verlieren. |
| `gesellschaftsgruender-produkt-und-produkthaftung-start` | Prüft CE, Produktsicherheit, Bedienungsanleitung, Haftung und Versicherung vor Markteintritt. |
| `gesellschaftsgruender-rechtsformwahl` | Rechtsformwahl für Unternehmen: GmbH, UG, AG, GbR, PartG, KG, SE im Vergleich. Normen: GmbHG, AktG, PartGG, HGB, SE-VO. Prüfraster: Haftung, Steuern, Kapital, Mitbestimmung, Borsenreife. Output: Rechtsformvergleich-Matrix mit Empfehlung.... |
| `gesellschaftsgruender-redteam-gruendungspaket` | Prüft das gesamte Gründungspaket auf typische Fehler, Streitbomben und Register-/Bankhindernisse. |
| `gesellschaftsgruender-registerbeanstandung-beantworten` | Hilft bei Zwischenverfügung/Registerbeanstandung nach Gründung oder Änderung. |
| `gesellschaftsgruender-reguliertes-geschaeftsmodell` | Erkennt Erlaubnispflichten vor Gründung: Finanzen, Versicherung, Medizin, Makler, Bewachung, Handwerk, Güterverkehr, Lebensmittel. |
| `gesellschaftsgruender-sacheinlage-und-verdeckte-sacheinlage` | Prüft Sacheinlagen, Werthaltigkeit, Sachgründungsbericht und verdeckte Sacheinlage. |
| `gesellschaftsgruender-sanktionen-investorcheck` | Prüft Investoren und Gesellschafter auf Sanktions-, Geldwäsche- und Außenwirtschaftsrisiken. |
| `gesellschaftsgruender-se-und-crossborder` | Prüft SE und grenzüberschreitende Gründungs-/Holdingfragen auf Einstiegsebene. |
| `gesellschaftsgruender-sha-satzung-stimmverpflichtung` | Stimmbindungsvereinbarung und SHA-Regelungen zu Abstimmungspflichten in GmbH aufsetzen. Normen: §§ 47 48 GmbHG, BGB. Prüfraster: zulässige Stimmbindung, Durchsetzbarkeit, Vertragsstrafe, Grenze Satzungsautonomie. Output: SHA-Klausel Stim... |
| `gesellschaftsgruender-share-classes-a-b-c` | Anteilsklassen A, B, C in GmbH oder AG gestalten: unterschiedliche Gewinn-, Stimm- und Liquidationsrechte. Normen: §§ 29 47 GmbHG, §§ 11 12 AktG. Prüfraster: Satzungsgestaltung, steuerliche Wirkung, Investorenerwartungen. Output: Satzung... |
| `gesellschaftsgruender-stammkapital-einzahlung` | Stammkapitaleinzahlung bei GmbH-Gründung nachweisen: Mindesteinzahlung, Bankbescheinigung, Sacheinlage. Normen: §§ 7 Abs. 2 und 19 GmbHG. Prüfraster: Mindesteinzahlung 50 Prozent, Bankbescheinigung, Sacheinlageprüfung, verdeckte Sacheinl... |
| `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` | Hälftiger Stammkapitalverlust nach § 49 Abs. 3 GmbHG: Einberufungspflicht und Insolvenzprüfung. Normen: §§ 49 Abs. 3 64 GmbHG, § 15a InsO. Prüfraster: Bilanzkennzahlen, Einberufungspflicht, Haftungsrisiken GF. Output: Stellungnahme Stamm... |
| `gesellschaftsgruender-steuerliche-erfassung-elster` | Führt durch Fragebogen steuerliche Erfassung, USt, Dauerfristverlängerung und Lohnsteuer. |
| `gesellschaftsgruender-transparenzregister` | Transparenzregister-Meldung für GmbH oder UG: wirtschaftlich Berechtigte, Fristen, Bußgelder. Normen: §§ 18 ff. GwG, GeldwäscheG. Prüfraster: Identifikation wirtschaftlich Berechtigter, Meldepflicht, Meldefristen, Aktualisierungen. Outpu... |
| `gesellschaftsgruender-transparenzregister-update` | Prüft Aktualisierung wirtschaftlich Berechtigter nach Anteilserwerb, Treuhand, Pooling oder Kontrolle. |
| `gesellschaftsgruender-treuhand-und-nominee` | Prüft Treuhand, wirtschaftlich Berechtigte, Stimmrechte, Steuer- und GwG-Risiken. |
| `gesellschaftsgruender-ug-vorbereitung` | UG haftungsbeschraenkt gründen: Musterprotokoll, Mindestkapital 1 Euro, Thesaurierungspflicht. Normen: § 5a GmbHG, §§ 2 3 GmbHG. Prüfraster: Stammkapital 1 Euro bis unter 25000 Euro, Musterprotokoll-Pflicht, Rücklagenbildung 25 Prozent J... |
| `gesellschaftsgruender-umsatzsteuer-start` | Prüft USt-Startfragen, Kleinunternehmer, Reverse Charge, innergemeinschaftliche Lieferungen und Rechnungen. |
| `gesellschaftsgruender-versicherungen-start` | Prüft D&O, Betriebshaftpflicht, Cyber, Produkthaftpflicht, Berufshaftpflicht und Key Person. |
| `gesellschaftsgruender-vinkulierung-und-transfer` | Prüft Vinkulierung, Zustimmung, Vorerwerbsrechte, Drag/Tag und Joinder. |
| `gesellschaftsgruender-wandeldarlehen-safe` | Prüft Wandeldarlehen, Discount, Cap, Wandlung, Rang, Prospekt-/Bankaufsichtsrisiken. |
| `spezial-geschaeftsfuehrervertrag-livequellen-check` | Geschaeftsfuehrervertrag: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gesellschaften-tatbestand-beweis-und-belege` | Gesellschaften: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gesellschaftsvertrag-vergleich-eskalation` | Gesellschaftsvertrag: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ggmbh-risikoampel-und-gegenargumente` | Ggmbh: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gmbh-fristen-form-und-zustaendigkeit` | GmbH: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gruendungsassistent-erstpruefung-und-mandatsziel` | Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-partg-dokumentenmatrix-und-lueckenliste` | PartG: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsformwahl-behoerden-gericht-und-registerweg` | Rechtsformwahl: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ueber-schriftsatz-brief-und-memo-bausteine` | Ueber: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin gesellschaftsgruender: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin gesellschaftsgruender: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin gesellschaftsgruender: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin gesellschaftsgruender: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
