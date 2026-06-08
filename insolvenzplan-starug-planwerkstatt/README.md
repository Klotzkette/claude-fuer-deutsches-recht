# Insolvenzplan- und StaRUG-Planwerkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`insolvenzplan-starug-planwerkstatt`) | [`insolvenzplan-starug-planwerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzplan-starug-planwerkstatt.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Metallbau Hansa GmbH – Insolvenzplan und StaRUG-Restrukturierung** (`insolvenzplan-starug-planwerkstatt-metallbau-hansa`) | [Gesamt-PDF lesen](../testakten/insolvenzplan-starug-planwerkstatt-metallbau-hansa/gesamt-pdf/insolvenzplan-starug-planwerkstatt-metallbau-hansa_gesamt.pdf) | [`testakte-insolvenzplan-starug-planwerkstatt-metallbau-hansa.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenzplan-starug-planwerkstatt-metallbau-hansa.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für die Erstellung, Prüfung und Härtung von Insolvenzplänen und StaRUG-Restrukturierungsplänen. Es führt vom Kaltstart über Datenraum, Sanierungskonzept, integrierte Planung, Vergleichsrechnung, Gruppen- und Klassenbildung, darstellenden und gestaltenden Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, gerichtliche Schritte und Planvollzug bis zum Monitoring.

## Wofür das Plugin gedacht ist

- Insolvenzplan im Regelverfahren, in Eigenverwaltung und im Schutzschirm.
- StaRUG-Restrukturierungsplan mit Auswahl der Planbetroffenen, Gruppen, Abstimmung, gerichtlichen Instrumenten und Stabilisierung.
- Vergleichsrechnung als zentrales Entscheidungselement mit Planfall, Fortführung ohne Plan, Liquidation, Sicherheiten, Sonderaktiva und Planmehrwert.
- Sanierungskonzept, integrierte Ertrags-, Finanz- und Liquiditätsplanung sowie Maßnahmenprogramm.
- Gerichtsfeste Entwurfsarbeit mit Anlagen, Red-Team-Prüfung, Freigabeampel und Planvollzug.

## Leitprinzip

Das Plugin ist verzeihend im Intake und streng im Ergebnis. Es darf mit chaotischen Tabellen, unvollständigen OPOS-Listen, widersprüchlichen Sicherheitenangaben und unfertigen Managementannahmen starten. Es macht daraus aber keinen scheinbar fertigen Plan. Jede Annahme bleibt sichtbar, jede Zahl bekommt eine Quelle oder Warnung, jede Rechtswirkung wird auf Bestimmtheit, Vergleichsrechnung und Minderheitenschutz zurückgeführt.

## Typischer Ablauf

1. Kaltstart: Rolle, Route, Schuldnerdaten, Krise, Zielbild, Gericht, Fristen und verfügbare Unterlagen erfassen.
2. Datenraum: Jahresabschlüsse, BWA, SuSa, OPOS, Liquidität, Verträge, Sicherheiten, Personal, Steuern und Organunterlagen sortieren.
3. Sanierung: Krisenursachen, Maßnahmen, Fortführungsfähigkeit, Stakeholderbeiträge und integrierte Planung erarbeiten.
4. Vergleich: Planfall, Ohne-Plan-Szenario, Sicherheitenwerte, Sonderaktiva, Kosten, Quoten und Planmehrwert berechnen.
5. Plan bauen: Darstellender Teil, gestaltender Teil, Gruppen oder Klassen, Anlagen, Abstimmung und gerichtliche Route entwerfen.
6. Härtung: Cram-down, Minderheitenschutz, Bestätigungsrisiken, Einwände und Vollzug red-teamen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| ips-kommandocenter | Route, Material, Risiken und nächste Ausgaben steuern. |
| ips-verfahrenswahl | Den passenden Sanierungsrahmen auswählen. |
| ips-kaltstart-interview | Aus wenigen Angaben eine belastbare Arbeitsakte machen. |
| ips-datenraum-register | Alle Planbausteine belegbar machen. |
| ips-sanierungskonzept | Das wirtschaftliche Fundament des Plans herstellen. |
| ips-integrierte-planung | Zahlen konsistent, nachvollziehbar und gerichtsfähig machen. |
| ips-vergleichsrechnung | Herzstück des Plans rechnen und erklären. |
| ips-insolvenzplan-architektur | Einen vollständigen InsO-Plan strukturieren. |
| ips-starug-plan-architektur | Einen vollständigen Restrukturierungsplan strukturieren. |
| ips-darstellender-teil | Die Entscheidungsgrundlage vollständig machen. |
| ips-gestaltender-teil | Rechtswirkungen bestimmt und vollziehbar formulieren. |
| ips-gruppen-klassenbildung | Abstimmungsarchitektur belastbar machen. |
| ips-sicherheiten-drittsicherheiten | Besicherte Positionen planfest und wertklar behandeln. |
| ips-planbetroffene-auswahl | StaRUG-Eingriffe fokussiert und begründet halten. |
| ips-abstimmung-mehrheiten | Mehrheiten vor dem Termin realistisch prüfen. |
| ips-cramdown-obstruktion | Ablehnende Gruppen gerichtsfest einordnen. |
| ips-minderheitenschutz | Opposition ernst nehmen und Planangriff vermeiden. |
| ips-anlagenpaket | Nichts einreichen, was Anlagenlücken hat. |
| ips-gerichtliche-schritte | Verfahren und Gerichtskommunikation steuern. |
| ips-stabilisierung-starug | Zeit kaufen, ohne die Planroute zu beschädigen. |
| ips-planvollzug-monitoring | Nach Bestätigung die Umsetzung führen. |
| ips-steuern-bilanz-folgen | Planwirkungen nicht an Nebenfolgen scheitern lassen. |
| ips-stakeholder-kommunikation | Akzeptanz für den Plan organisieren. |
| ips-redteam-qualitygate | Den Plan vor Gegnern und Gericht hart prüfen. |

## Grenzen

Das Plugin ersetzt keine anwaltliche, steuerliche oder betriebswirtschaftliche Endprüfung. Es ist ein Arbeits-, Strukturierungs- und Qualitätssicherungswerkzeug. Bei Planbestätigung, gerichtlicher Einreichung, steuerlichen Folgen, Organpflichten, Sicherheitenwerten, Drittsicherheiten und streitigen Gläubigerrechten verlangt es menschliche Freigabe.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abstimmung-anlagen-interessen-cram` | Abstimmung: Internationaler Bezug und Schnittstellen im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und... |
| `abstimmung-mehrheiten-anlagenpaket` | Abstimmungsmehrheiten für Insolvenzplan nach InsO und Restrukturierungsplan nach StaRUG simulieren und Abstimmungstermin vorbereiten. §§ 244 245 InsO Kopf- und Summenmehrheit §§ 25 26 StaRUG Klassenmehrheit. Prüfraster: Stimmberechtigte... |
| `anlagen-mehrparteien-konflikt-und-interessen` | Anlagen: Mehrparteienkonflikt und Interessenmatrix im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `anlagenpaket` | Pflichtanlagen für Insolvenzplan oder StaRUG-Plan vollständig zusammenstellen. §§ 229 230 InsO §§ 14 15 StaRUG Planunterlagen. Prüfraster: Pflichtanlagen je Route Vermögensuebersicht Finanzplan Erklärungen Beteiligtenlisten Unterschrifte... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `asset-deals-im-plan-grundstuecke-marken-kundendaten` | Asset-Deals im Insolvenzplan strukturieren wenn Grundstuecke Marken oder Kundendaten uebertragen werden sollen. §§ 311b 398 BGB §§ 27 ff. MarkenG § 15 PatG. Prüfraster: Übertragungsgegenstand Formerfordernis Grundbuch Markenregister Date... |
| `cram-formular-portal-und-einreichung` | Cram: Formular, Portal und Einreichungslogik im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `cramdown-obstruktion-datenraum-register` | Obstruktionsverbot und gruppenuebergreifende Mehrheitsentscheidung prüfen wenn ablehnende Gruppen oder Klassen den Plan blockieren. § 245 InsO § 27 StaRUG Cramdown. Prüfraster: Schlechterstellung angemessene Beteiligung absolute Priorita... |
| `darstellender-quellenkarte` | Darstellender Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `darstellender-teil` | Darstellenden Teil des Insolvenzplans oder StaRUG-Plans vollständig verfassen. § 220 InsO § 6 StaRUG Darstellungspflichten. Prüfraster: Krisengeschichte Massnahmen Finanzplanung Vergleichsrechnung Sonderaktiva Sicherheiten Steuerfolgen O... |
| `datenraum-register` | Planbegleitenden Datenraum aufbauen und Dokumentenregister führen damit alle Planbausteine belegbar sind. §§ 218 229 InsO §§ 14 15 StaRUG Planunterlagen. Prüfraster: Pflichtunterlagen Jahresabschluesse BWA OPOS Vertraege Sicherheiten Lue... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `down-red-gestaltender-gruppen` | Down: Red-Team und Qualitätskontrolle im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbar... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `gerichtliche-schritte-kommandocenter` | Gerichtliche Verfahrensschritte für Insolvenzplan und StaRUG-Plan steuern von Einreichung bis Planbestätigung. §§ 231 232 248 InsO §§ 45 ff. StaRUG Gerichtsverfahren. Prüfraster: Einreichung Vorprüfung Eroerterungstermin Abstimmung Bestä... |
| `gestaltender-teil` | Gestaltenden Teil des Insolvenzplans oder StaRUG-Plans mit konkreten Rechtsaenderungen Quoten und Vollstreckungsgrundlagen formulieren. § 221 InsO § 7 StaRUG Planwirkungen. Prüfraster: Rechtsaenderungen je Gruppe Quoten Stundungen Sicher... |
| `gestaltender-zahlen-schwellen-und-berechnung` | Gestaltender: Zahlen, Schwellenwerte und Berechnung im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und... |
| `gruppen-klassenbildung` | Abstimmungsgruppen nach InsO und Klassen nach StaRUG sachgerecht bilden. §§ 222 223 InsO §§ 9 10 StaRUG Klassenbildung. Prüfraster: Rechtsstellung Absonderung Insolvenzgläubiger Nachrang Anteilsinhaber Gruppeninterne wirtschaftliche Inte... |
| `gruppen-schriftsatz-brief-und-memo-bausteine` | Gruppen: Schriftsatz-, Brief- und Memo-Bausteine im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und dir... |
| `inso-starug-planwerkstatt-start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Insolvenzplan Starug Planwerkstatt-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbei... |
| `insolvenzplan-architektur` | Vollständigen Insolvenzplan nach §§ 217 ff. InsO strukturieren und alle Pflichtbestandteile verbinden. §§ 217 220 221 InsO Planarchitektur §§ 222 229 InsO Gruppen und Anlagen. Prüfraster: Planvorlageberechtigung darstellender gestaltende... |
| `insolvenzplan-intake-klassen` | Insolvenzplan: Erstprüfung, Rollenklärung und Mandatsziel im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbrems... |
| `insolvenzplan-vergleichsrechnung-quote` | Vergleichsrechnung Quote im Plugin Insolvenzplan Starug Planwerkstatt im Insolvenzplan Starug Planwerkstatt: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-P... |
| `intake-dokumentenmatrix-und-lueckenliste` | Intake: Dokumentenmatrix, Lückenliste und Nachforderung im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse... |
| `integrierte-planung` | Integrierte Planrechnung aus GuV Liquiditaet und Bilanz für Insolvenzplan oder StaRUG erstellen. §§ 220 229 InsO §§ 14 StaRUG Finanzplanung. Prüfraster: Ist-Zahlen Planannahmen Base-Case Stressszenarien Brückenrechnung Annahmenregister K... |
| `ipsplan-cram-down-spezial` | Spezialfall gruppenuebergreifender Cram-Down: Voraussetzungen, faire Beteiligung am Planwert, Vergleichsrechnung. Pruefraster für Planersteller im Insolvenzplan Starug Planwerkstatt: prüft konkret die einschlägigen Tatbestandsmerkmale, F... |
| `ipsplan-gruppenbildung-leitfaden` | Leitfaden Gruppenbildung im Insolvenz- und Restrukturierungsplan §§ 222 InsO, §§ 9 ff. StaRUG: sachgerechte Abgrenzung, Schlechterstellungsverbot. Pruefraster für Planersteller im Insolvenzplan Starug Planwerkstatt: prüft konkret die ein... |
| `ipsplan-planstruktur-prepack-plan` | Bauleiter Planstruktur Insolvenzplan und StaRUG-Restrukturierungsplan: darstellender und gestaltender Teil, Anlagen. Pruefraster für Planerstellung im Insolvenzplan Starug Planwerkstatt: prüft konkret die einschlägigen Tatbestandsmerkmal... |
| `ipsplan-prepack-plan-spezial` | Spezialfall Prepack-Plan und Eigenverwaltung: Plan vor Antrag, Sachwalter, Glaeubiger einbinden. Pruefraster für Krisenberater im Insolvenzplan Starug Planwerkstatt: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege un... |
| `kaltstart-interview` | Insolvenzplan- oder StaRUG-Mandat durch strukturiertes Erstgespraech aufgleisen wenn Unterlagen fehlen. §§ 13 15a InsO §§ 29 42 StaRUG Antragspflichten. Prüfraster: Basisdaten Krisenursachen Gläubigerlandschaft Liquiditaetslage Sanierung... |
| `klassen-verhandlung-vergleich-und-eskalation` | Klassen: Verhandlung, Vergleich und Eskalation im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direk... |
| `kommandocenter` | Insolvenzplan- oder StaRUG-Mandat starten und Verfahrensroute Ampelstatus und naechste Schritte bestimmen. §§ 217 218 InsO §§ 29 ff. StaRUG. Prüfraster: Rolle Verfahrensziel Datenraumstand Zahlenstand Stakeholder Fristen naechste Aktion.... |
| `minderheitenschutz-planbetroffene` | Schlechterstellungsrisiken opponierender Beteiligter analysieren und Planangriffe durch Minderheitenschutzprüfung abwenden. § 251 InsO § 64 StaRUG Minderheitenschutz. Prüfraster: individuelle Schlechterstellung Sicherheitsleistungen Verg... |
| `output-waehlen` | Output wählen im Plugin Insolvenzplan Starug Planwerkstatt: Diese Output-Weiche für Insolvenzplan Starug Planwerkstatt entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste... |
| `planbetroffene-auswahl` | Planbetroffene im StaRUG-Verfahren sachgerecht auswaehlen und Nichteinbeziehung dokumentiert begründen. §§ 2 4 StaRUG Gestaltbarkeit Ausnahmen. Prüfraster: gestaltbare Rechtsverhältnisse Ausnahmen Arbeitnehmer deliktische Forderungen Nic... |
| `planvollzug-monitoring` | Planvollzug nach Bestätigung ueberwachen Zahlungen kontrollieren und Abweichungen dokumentieren. §§ 248 261 InsO Planueberwachung §§ 69 72 StaRUG. Prüfraster: Bedingungen Fälligkeiten Quoten Zahlstellen Covenants Wiederaufleben Abweichun... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `redteam-qualitygate-sanierungskonzept` | Insolvenzplan oder StaRUG-Plan vor Einreichung aus Gegnersicht und Gerichtssicht prüfen. §§ 231 245 251 InsO Versagungsgründe § 64 StaRUG. Prüfraster: Vollständigkeit Bewertungswiderspruch Gruppenmissbrauch fehlende Anlagen unbestimmte K... |
| `restrukturierungsplan-fristen-form-und-zustaendigkeit` | Restrukturierungsplan: Fristen, Form, Zuständigkeit und Rechtsweg im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Feh... |
| `sanierungskonzept` | Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Ausgangslage, Krisenstadium, Krisenursachen, Leitbild, Maßnahmenpaket... |
| `sanierungskonzept-starug-spezial-teil` | Sanierungskonzept: Risikoampel, Gegenargumente und Verteidigungslinien im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten... |
| `sanierungsmoderation-94-starug` | Sanierungsmoderation nach § 94 StaRUG vorbereiten und durchführen wenn außergerichtliche Einigung mit moderierender Instanz angestrebt wird. §§ 94 ff. StaRUG Sanierungsmoderation. Prüfraster: Antrag Bestellungsvoraussetzungen Moderations... |
| `sicherheiten-drittsicherheiten` | Absonderungsrechte und Drittsicherheiten im Insolvenzplan und StaRUG planfest behandeln und Ausfallwerte bestimmen. §§ 49 50 51 224 InsO §§ 2 Abs. 4 StaRUG Drittsicherheiten. Prüfraster: Sicherheitenregister Eingriffsbeschreibung Ausfall... |
| `stabilisierung-stakeholder` | StaRUG-Stabilisierungsmassnahmen beantragen wenn Vollstreckungsdruck die Planarbeit gefaehrdet. §§ 49 50 51 StaRUG Stabilisierungsanordnung. Prüfraster: Stabilisierungsbedarf Verhältnismäßigkeit Gläubiger Dauer Insolvenznaehe Organpflich... |
| `stakeholder-kommunikation` | Gläubiger Banken Arbeitnehmer Lieferanten Gericht und Investoren zielgruppengerecht über Insolvenzplan oder StaRUG informieren. §§ 232 235 InsO §§ 17 20 StaRUG Gläubigerinfo. Prüfraster: Stakeholdergruppen Sorgen Botschaften Q and A One-... |
| `starug-plan-architektur` | Vollständigen StaRUG-Restrukturierungsplan strukturieren von Planbetroffenenauswahl bis Bestätigungspfad. §§ 6 7 8 StaRUG Planinhalt §§ 60 ff. StaRUG Abstimmung Gerichtsverfahren. Prüfraster: Restrukturierungsfähigkeit drohende ZU gestal... |
| `starug-tatbestand-beweis-und-belege` | StaRUG: Tatbestandsmerkmale, Beweisfragen und Beleglage im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse... |
| `steuern-bilanz-folgen` | Steuerliche und bilanzielle Folgen des Plans prüfen damit Planwirkungen nicht an Nebenfolgen scheitern. §§ 3a 3c EStG Sanierungsgewinn § 8c KStG Verlustvortrag. Prüfraster: Erlass Stundung Debt-Equity-Swap Bilanzierung Verlustvortraege U... |
| `teil-compliance-dokumentation-und-akte` | Teil: Compliance-Dokumentation und Aktenvermerk im Insolvenzplan und StaRUG: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und dire... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verfahrenswahl-restrukturierungsplan` | Passenden Sanierungsrahmen auswaehlen und Insolvenzplan Eigenverwaltung Schutzschirm StaRUG und außergerichtliche Einigung vergleichen. §§ 270 270d InsO §§ 29 42 StaRUG. Prüfraster: Zahlungsunfähigkeit Masse Zeitfenster Eingriffstiefe Ge... |
| `vergleichsrechnung-ipsplan-cram` | Vergleichsrechnung als Herzstuck des Plans erstellen: Planfall gegen Ohne-Plan-Szenario je Gruppe oder Klasse. §§ 220 229 InsO § 6 Abs. 2 StaRUG Schlechterstellungsverbot. Prüfraster: Masse Kosten Sicherheiten Anfechtung Organhaftung Pla... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Insolvenzplan Starug Planwerkstatt: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Insolvenzplan Starug Planwerkstatt: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsp... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
