# Fachanwalt Handels- und Gesellschaftsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-handels-gesellschaftsrecht`) | [`fachanwalt-handels-gesellschaftsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-handels-gesellschaftsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Gesellschafterstreit / Squeeze-out — Küchenkönig Manufaktur GmbH & Co. KG (Paderborn)** (`gesellschafterstreit-squeeze-out-kuechenkoenig-paderborn`) | [Gesamt-PDF lesen](../testakten/gesellschafterstreit-squeeze-out-kuechenkoenig-paderborn/gesamt-pdf/gesellschafterstreit-squeeze-out-kuechenkoenig-paderborn_gesamt.pdf) | [`testakte-gesellschafterstreit-squeeze-out-kuechenkoenig-paderborn.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschafterstreit-squeeze-out-kuechenkoenig-paderborn.zip) |
| **NeuroChain Labs — Gründung eines KI/Krypto-Startups in Berlin, Musterprotokoll vs. individuelle Satzung** (`gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/gesamt-pdf/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll_gesamt.pdf) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip) |
| **Roeschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation** (`gesellschaftsgruender-streit-roeschen-tech`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) |
| **Handelsrecht HGB — Elbwerft Solar: eGbR, OHG-Statuswechsel, KG und Handelskauf** (`handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona`) | [Gesamt-PDF lesen](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/gesamt-pdf/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona_gesamt.pdf) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

## Anwalts-Dashboard für den Schnelleinstieg

Der Skill `einstieg-routing` ist das Anwalts-Dashboard zu diesem Plugin:
Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch,
Zustaendigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs,
Norm-Radar, Leitentscheidungs-Anker und genau eine Rueckfrage - bei
klarer Faktenlage sofort zum Spezial-Skill. Der Anwalt bleibt im Driver Seat.

Konvention: [`references/anwalts-dashboard-konvention.md`](../references/anwalts-dashboard-konvention.md)
| Quellen-Anker: [`references/leitentscheidungen-anker.md`](../references/leitentscheidungen-anker.md)
| Quellenhygiene: [`references/quellenhygiene.md`](../references/quellenhygiene.md).


Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO § 14i. HGB, AktG, GmbHG, PartGG, UmwG, MoPeG (GbR seit 2024). Geschäftsführerhaftung §§ 43 GmbHG, 93 AktG. Gesellschafterstreit und Beschlussanfechtung. Handelsvertreterausgleich § 89b HGB.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-handels-gesellschaftsrecht-orientierung` | Orientierung Handels- und Gesellschaftsrecht. FAO § 14i Voraussetzungen Normen typische Mandate. |
| `fachanwalt-handels-gesellschaftsrecht-geschaeftsfuehrerhaftung` | Geschäftsführerhaftung § 43 GmbHG und § 93 AktG. Innenhaftung Außenhaftung Business Judgement Rule. |
| `fachanwalt-handels-gesellschaftsrecht-gesellschafterstreit` | Gesellschafterstreit. Beschlussanfechtung Einberufungsmangel Stimmverbot. Ausschluss aus wichtigem Grund. |
| `fachanwalt-handels-gesellschaftsrecht-handelsvertreterausgleich` | Handelsvertreterausgleichsanspruch § 89b HGB. Drei Voraussetzungen Berechnung Höchstgrenze. |

## Zitierweise

Folgt `zitierweise-deutsches-recht` v3.0 (Az.-Marker, BGH-Pinpoint mit Rn., Hierarchie Bundesgerichte vor Instanzgerichten).

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 65 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ag-vorstandsvertrag-vorbereiten` | Vorstandsvertrag AG vorbereiten: §§ 84 ff: AktG, Bestellung und Anstellung trennen, Vergueng (fix, variabel, ESG-LTI), D and O Versicherung, Tantieme Caps nach VorstAG, Anstellungsbedingungen Compliance, Sonderkuen... |
| `aktg-behoerden-gericht-und-registerweg` | AktG: Behörden-, Gerichts- oder Registerweg im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und dir... |
| `aktionaersklage-anfechtung-paragraf-243-aktg` | Aktionaersklage Anfechtung § 243 AktG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `anfechtungsklage-bgb-gesellschaft-bgh-ii-zr-66-20` | Anfechtungsklage BGB Gesellschaft BGH Ii Zr 66 20: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Handels- und Gesellschaftsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 246 AktG Anfechtung 1 Monat, Satzung, Gesellschafterbeschluss, HV-Protokoll), dokumentiert Router-Entscheidung mit Begründ... |
| `beschlussanfechtung-mehrparteien-konflikt-und-interessen` | Beschlussanfechtung: Mehrparteienkonflikt und Interessenmatrix im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, F... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Handels- und Gesellschaftsrecht: sortiert Satzung, Gesellschafterbeschluss, HV-Protokoll, prüft Datum, Absender, Frist und Beweiswert (Gesellschafterprotokolle, HR-Auszug); markiert Lücken; berücksichtigt... |
| `einstieg-in-den-skill-verbund-handels-und-gesellschaftsrecht` | Einstieg in den Skill-Verbund Handels- und Gesellschaftsrecht: FAO § 14i Voraussetzungen 80 Faelle davon 40 rechtsfoermlich. HGB AktG GmbHG PartGG UmwG MoPeG. Typische Mandate Gründung Satzungsa... |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Handels- und Gesellschaftsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rüc... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Handels Gesellschaftsrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt p... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Handels- und Gesellschaftsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstg... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbre... |
| `fao-dokumentenmatrix-und-lueckenliste` | FAO: Dokumentenmatrix, Lückenliste und Nachforderung im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbrems... |
| `geschaeftsfuehrerhaftung` | Fachanwalt Handels Gesellschaftsrecht Geschäftsführerhaftung: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Handels Gesellschaftsrecht Geschäftsführerhaftung: o... |
| `geschaeftsfuehrerhaftung-zahlen-schwellen-und-berechnung` | Geschäftsführerhaftung: Zahlen, Schwellenwerte und Berechnung im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten,... |
| `gesellschafterstreit` | Fachanwalt Handels Gesellschaftsrecht Gesellschafterstreit: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Handels Gesellschaftsrecht Gesellschafterstreit: ordnet No... |
| `gesellschafterstreit-compliance-dokumentation-und-akte` | Gesellschafterstreit: Compliance-Dokumentation und Aktenvermerk im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten,... |
| `gesellschaftervertrag-abschlussprodukt-und-uebergabe` | Gesellschaftervertrag: Abschlussprodukt und Übergabe im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbrems... |
| `gesellschaftsrecht-fristen-form-und-zustaendigkeit` | Gesellschaftsrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, F... |
| `gmbh-beirat-vetorechte-und-organnaehe` | Entwirft und prüft mächtige GmbH-Beiräte mit Zustimmungskatalogen, Informationsrechten, Investorenschutz, Organnähe, Interessenkonflikten und Haftungsbegrenzung: Entwirft und prüft mächtige GmbH-Beiräte mit Zustimmungskatalogen, Informat... |
| `gmbh-cash-flow-und-darlehen-gesellschafter` | Gesellschafterdarlehen und Cash-Flow GmbH: § 39 Abs: 1 Nr. 5 InsO Subordination, § 135 InsO Anfechtbarkeit Rueckzahlung in der Krise, Stehenlassen als Eigenkapitalersatz alter Rechtslage gegenueber neuer... |
| `gmbh-gf-haftung-paragraf-43-gmbhg` | Gmbh gf Haftung § 43 GmbHG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `gmbhg-schriftsatz-brief-und-memo-bausteine` | Gmbhg: Schriftsatz-, Brief- und Memo-Bausteine im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und... |
| `handels-tatbestand-beweis-und-belege` | Handels: Tatbestandsmerkmale, Beweisfragen und Beleglage im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerb... |
| `handelsvertreterausgleich` | Fachanwalt Handels Gesellschaftsrecht Handelsvertreterausgleich: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Handels Gesellschaftsrecht Handelsvertreterausgleich:... |
| `handelsvertreterausgleich-international-schnittstellen` | Handelsvertreterausgleich: Internationaler Bezug und Schnittstellen im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargument... |
| `hgb-einsichtsrecht-kommanditist-paragraf-166-hgb-bgh-ii-zr-31-21` | Hgb Einsichtsrecht Kommanditist Paragraf 166 Hgb BGH Ii Zr 31 21: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `hgb-risikoampel-und-gegenargumente` | HGB: Risikoampel, Gegenargumente und Verteidigungslinien im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerb... |
| `hgesr-einfuehrung-rechtsformen` | Einfuehrung deutsche Rechtsformen für Handels- und Gesellschaftsrecht: GbR, OHG, KG, GmbH und Co KG, GmbH, UG haftungsbeschraenkt, AG, KGaA, SE, eingetragene Genossenschaft: Einfuehrung deutsche Rechtsformen für Handels- und Gesellschaft... |
| `hgesr-grenzueberschreitende-formwechsel` | Grenzueberschreitende Formwechsel und Sitzverlegung nach EU-Mobilitaetsrichtlinie und UmwG: Verfahrensschritte, Schutz Gläubiger, Minderheitsgesellschafter, Arbeitnehmer: Grenzueberschreitende Formwechsel und Sitzverlegung nach EU-Mobil... |
| `hgesr-handelsvertreterausgleich-detail` | Handelsvertreterausgleich § 89b HGB detailliert: Voraussetzungen Nichtwirksamwerden des Vertrags, Unternehmervorteile bestehen fort, Provisionsverluste, Billigkeit: Handelsvertreterausgleich § 89b HGB detailliert: Voraussetzungen Nichtwi... |
| `hgesr-mbg-modernisierungsgesetz-praxis` | MoPeG (Modernisierungsgesetz Personengesellschaftsrecht) seit 2024 in der Praxis: neue GbR mit Rechtsfaehigkeit und Gesellschaftsregister, Auswirkungen auf Grundbuch, OHG-Aktualisierungen, KG-Detailaenderungen: MoPeG (Modernisierungsgese... |
| `hgr-aktionsbindungsvertrag-spezial` | Spezialfall Aktionsbindungsvertrag bei AG: zulaessige Stimmbindungen, Sperrwirkung gegenueber Satzung, Prüfung BGH-Rechtsprechung: Spezialfall Aktionsbindungsvertrag bei AG: zulaessige Stimmbindungen, Sperrwirkung gegenueber Satzung, Pr... |
| `hgr-dis-schiedsverfahren-streit` | Gesellschafter streiten und wollen Schiedsverfahren statt Klage oder laufendes Schiedsverfahren managen: DIS-Schiedsverfahren Gesellschafterstreit. Prüf... |
| `hgr-dlt-pilotregime-token` | EU-DLT-Pilotregime VO 2022/858 (anwendbar 23.3.2023, verlängert voraussichtlich bis 23.3.2029) für DLT-basierte Wertpapierinfrastruktur: EU-DLT-Pilotregime VO 2022/858 (anwendbar 23.3.2023, verlängert voraussichtlich bis 23.3.2029) für D... |
| `hgr-due-diligence-cheker-light` | Due-Diligence-Checker light für kleinere Mandate: Standard-Risikofelder (Steuer, Arbeit, IT, IP, Compliance, ESG), Datenraum-Struktur, Reviewer-Aufteilung, Sample-Quoten: Due-Diligence-Checker light für kleinere Mandate: Standard-Risikof... |
| `hgr-gesellschaftervertrag-tour` | Gesellschaftervertrags-Tour: GmbH-Standardklauseln Vinkulierung, Wettbewerbsverbot, Abfindungsklausel, Gesellschafterversammlung, Tag-along / Drag-along: Gesellschaftervertrags-Tour: GmbH-Standardklauseln Vinkulierung, Wettbewerbsverbot,... |
| `hgr-kollektivverteidigung-direktorenhaftung-spezial` | Spezialfall Kollektivverteidigung in Direktorenhaftungsfaellen: § 116 AktG, gesamtschuldnerische Haftung Vorstand, Koordinierung Verteidigung, D-and-O-Versicherung: Spezialfall Kollektivverteidigung in Direktorenhaftungsfaellen: § 116 Ak... |
| `holding-strukturplanung` | Holding-Strukturplanung: § 8b KStG Schachtelprivileg (95 % steuerfreier Exit), Varianten Einzel-Holding, Vermögens-Holding, Doppel-Holding mit Familienstiftung: Holding-Strukturplanung: § 8b KStG Schachtelprivileg (95 % steuerfreier Exit... |
| `inhabilitaet-geschaeftsfuehrer-paragraf-6-gmbhg` | Inhabilitaet Geschäftsführer § 6 GmbHG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `kanzlei-beweislast-und-darlegungslast` | Kanzlei: Beweislast, Darlegungslast und Substantiierung im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbr... |
| `kapitalerhaltung-paragraf-30-gmbhg-bgh-ii-zr-66-19` | Kapitalerhaltung Paragraf 30 GmbHG BGH Ii Zr 66 19: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `ma-due-diligence-findings` | Anwalt hat Datensichtung abgeschlossen und muss Due-Diligence-Bericht für M&A-Transaktion strukturieren: M&A Due Diligence Report Legal Tax Commercial.... |
| `mopeg-formular-portal-und-einreichung` | Mopeg: Formular, Portal und Einreichungslogik im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `nachfolgeklausel-gesellschaftsvertrag` | Nachfolgeklausel Gesellschaftsvertrag: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `output-waehlen` | Output-Wahl für Fachanwalt Handels- und Gesellschaftsrecht: stimmt Adressat (Gesellschafter/Aktionäre, Vorstand/Geschäftsführung, Aufsichtsrat), Frist (§ 246 AktG Anfechtung 1 Monat) und Form auf den Zweck ab — typische Outputs: Beschlus... |
| `partg-haftung-paragraf-8-partgg` | Partg Haftung § 8 PartGG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `partgg-verhandlung-vergleich-und-eskalation` | Partgg: Verhandlung, Vergleich und Eskalation im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `pilotregime-sonderfall-edge-case` | Pilotregime: Sonderfall und Edge-Case-Prüfung im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Handels- und Gesellschaftsrecht: prüft Normen (HGB, GmbHG, AktG, BGB §§ 705 ff., UmwG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Handelsregister und Quellenhygiene nach refe... |
| `registerrecht-handelsregister-praxis` | Handelsregister-Praxis: Anmeldungen, Form (notariell, öffentlich beglaubigt), zuständiges Gericht, elektronische Einreichung XJustiz, Prüfungsumfang nach FamFG: Handelsregister-Praxis: Anmeldungen, Form (notariell, öffentlich beglaubi... |
| `schnittstellen-mandantenentscheidung` | Schnittstellen: Mandantenkommunikation und Entscheidungsvorlage im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten,... |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Anfechtungs-/Nichtigkeitsklage GV-Beschluss, Auskunftsklage, Squeeze-out: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiierter... |
| `seit-fehlerkatalog` | Seit Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `squeeze-out-aktionaersbarabfindung` | Squeeze out Aktionaersbarabfindung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `squeeze-out-verfahren` | Mehrheitsaktionaer will Minderheitsaktionaere aus AG herausdrangen oder Minderheitsaktionaer wird herausgedraengt: Squeeze-out §§ 327a ff. Akt... |
| `token-fristennotiz-und-naechster-schritt` | Token: Fristennotiz und nächster Schritt im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `umwandlung-paragraf-202-umwg` | Umwandlung § 202 UmwG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `umwg-quellenkarte` | Umwg Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Handels- und Gesellschaftsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Satzung, Gesellschafterbeschluss, HV-Protokoll), nennt pro Lücke Beweisthema, Beschaffungsweg (Handelsregister... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Handels- und Gesellschaftsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich): Vergleichsverhandlungs-S... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`fachanwalt-handels-gesellschaftsrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/fachanwalt-handels-gesellschaftsrecht.md) (58 KB)
- Im Repo: [`testakten/megaprompts/fachanwalt-handels-gesellschaftsrecht.md`](../testakten/megaprompts/fachanwalt-handels-gesellschaftsrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Anfechtungsklage Paragraf 246 Aktg | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-handels-gesellschaftsrecht/anfechtungsklage-paragraf-246-aktg.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-handels-gesellschaftsrecht/anfechtungsklage-paragraf-246-aktg.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich prüfen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->
