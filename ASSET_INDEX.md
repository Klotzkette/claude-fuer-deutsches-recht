# Release-Asset-Index

Übersicht aller Dateien, die der Release-Workflow (`.github/workflows/release-plugin-zips.yml`) pro Tag-Release `vX.Y.Z` an den GitHub-Release anhängt.

**Stand:** v3.0.10

## Asset-Typen

| Typ | Erkennungsmerkmal | Verwendung |
| --- | --- | --- |
| **plugin** | `<plugin-name>.zip` | Über „Customize Plugins -> Install from .zip“ in Claude Code/Cowork hochladen. |
| **fallakte** | `testakte-<aktenname>.zip` | **Kein Plugin.** Mandatsunterlagen für Testzwecke. In den Chat ziehen, nicht zum Plugin-Upload geben. |
| **manifest** | `marketplace.json` | **Kein Plugin.** Marketplace-Manifest für `/plugin marketplace add` und zur manuellen Inspektion. |

## Plugin-Assets (80 Stück)

Alphabetisch wie in `.claude-plugin/marketplace.json`. URL-Schema:
`https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<name>.zip`

| Plugin | Kurzbeschreibung |
| --- | --- |
| `aktenaufbereiter-strafrecht` | Aktenaufbereiter fuer die Strafverteidigung. Bringt grosse Strafakten in den Griff durch sechs Excel-faehige Uebersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergaenzbar. Erkennt Luecken und Widersprueche. Kein Ersatz fuer Aktenlektuere. |
| `anlagen-zu-schriftsaetzen` | Zuordnung von Anlagen zu gerichtlichen Schriftsaetzen. Sortiert PDF/Word/Excel nach Schriftsatz-Logik (Klage/Erwiderung/Replik), konvertiert nach PDF, vergibt K/B/AST/AG, stempelt oben rechts in Arial 12, beA-tauglich, mit Konvolut. Modi: Auto-Benennung, Schriftsatz folgt, Pruefmodus. |
| `arbeitsrecht` | Kündigung (KSchG-Klage, 3-Wochen-Frist), Aufhebungsvertrag inkl. Sperrzeit, Abmahnung, Anhörung Betriebsrat § 102 BetrVG, Statusfeststellung, Personalrichtlinien (BetrVG, AGG, ArbZG, MuSchG, BEEG). |
| `aussenwirtschaft-zoll-sanktionen` | Freistehendes Außenwirtschafts-, Sanktions-, Zoll- und CBAM-Plugin: Exportkontrolle, BAFA, Dual-Use, Embargos, TARIC, Ursprung, Zollwert, Verbrauchsteuer, Antidumping, AWV, AML/KYC, Ermittlungen und Krisenkommunikation. |
| `berufsrecht-ki-vertragspruefung` | Berufsrechtliche und strafrechtliche Forprüfung von Verträgen mit privaten Legal-AI-Anbietern. Für Rechtsanwälte Steuerberater Wirtschaftsprüfer Patentanwälte Notare. §§ 43e BRAO 62a StBerG 50a WPO 39c PAO 26a BNotO § 203 StGB. Maßstab DAV-Stellungnahme. Gutachten Rückfragebrief Klauselvorschläge. |
| `betreuungsrecht` | Skills für berufliche Betreuer nach BtOG und §§ 1814 ff. BGB (Reform 2023): Jahresbericht ans Betreuungsgericht (§ 1863 BGB), Vermögensverzeichnis und Rechnungslegung (§§ 1835, 1865 BGB), Genehmigungspflicht-Prüfung (§§ 1848 ff., 1831, 1832 BGB), Kontoanalyse und verdächtige Verträge in der Vermögenssorge. |
| `common-law-kompass` | Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews. |
| `corporate-kanzlei` | Corporate/M&A-Plugin (46 Skills) für transaktionsstarke Kanzleien: Deal-Kommandocenter, Datenraum, Due Diligence, Tabellenreview, SPA/APA, Disclosure Schedules, Signing/Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, StaRUG, Insolvenzplan, PMI. |
| `datenschutzrecht` | DSGVO/BDSG/TTDSG: PIA/DPIA, AVV-Review als Verantwortlicher und Auftragsverarbeiter, Auskunftsersuchen Art. 15 DSGVO, Datenpannenmeldung Art. 33/34, Beschäftigtendatenschutz. |
| `einfache-leichte-sprache-jura` | Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen. |
| `energierecht` | Freistehendes Energierecht-Plugin: Stadtwerke, Strom-, Gas- und Wärmeversorgung, Netze, Speicher, Vertrieb, Industrie, EEG/KWKG, Quartiere, Fernwärme, Wettbewerb, Verwaltungsverfahren, Transaktionen, PPA und Projektfinanzierung. |
| `europarecht-kompass` | Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting. |
| `fachanwalt-agrarrecht` | Light-Touch-Plugin Fachanwalt fuer Agrarrecht. Orientierung Hoefeordnung Anerbenrechte Landpachtrecht BGB §§ 581 ff. GrdstVG EU-GAP Direktzahlungen Cross-Compliance Duengeverordnung Pflanzenschutzrecht Tierschutz Forstrecht. |
| `fachanwalt-arbeitsrecht` | Light-Touch-Plugin Fachanwalt fuer Arbeitsrecht nach FAO § 10. KSchG Kuendigungsschutzklage Frist drei Wochen § 4 KSchG. BetrVG Betriebsratsanhoerung § 102. TzBfG Befristung. AGG. Schnittstellen arbeitsrecht und kanzlei-cowork. |
| `fachanwalt-bank-kapitalmarktrecht` | Light-Touch-Plugin Fachanwalt fuer Bank- und Kapitalmarktrecht. Orientierung KWG ZAG WpHG WpIG MiFID-II MAR Marktmissbrauch MiCAR Verbraucherkredit Vermoegensanlage Beratungshaftung. Schnittstellen gesellschaftsrecht und regulatorisches-recht. |
| `fachanwalt-bau-architektenrecht` | Light-Touch-Plugin Fachanwalt fuer Bau- und Architektenrecht. Orientierung BGB Werkvertragsrecht §§ 650a ff. Bauvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht der Laender. Schnittstellen Vergaberecht und Verwaltungsrecht. |
| `fachanwalt-erbrecht` | Light-Touch-Plugin Fachanwalt fuer Erbrecht. Orientierung BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaft- und Schenkungsteuer ErbStG EU-ErbVO. Schnittstellen steuerrecht-kanzlei und gesellschaftsrecht. |
| `fachanwalt-familienrecht` | Light-Touch-Plugin Fachanwalt fuer Familienrecht. Orientierung Normen typische Mandate Fristen Standardliteratur. Familiengericht FamFG Scheidung Sorgerecht Umgangsrecht Unterhalt Zugewinn Ehevertrag. Tiefe Bearbeitung erfordert weiterhin Fachanwaltsexpertise. |
| `fachanwalt-gewerblicher-rechtsschutz` | Light-Touch-Plugin Fachanwalt fuer gewerblichen Rechtsschutz nach FAO § 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezuege. Markenanmeldung DPMA EUIPO. UWG-Abmahnung §§ 8 ff. UWG. Designverletzung. Einstweilige Verfuegung Verletzungsklage Lizenzanaloger Schadensersatz. |
| `fachanwalt-handels-gesellschaftsrecht` | Light-Touch-Plugin Fachanwalt fuer Handels- und Gesellschaftsrecht nach FAO § 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschaeftsfuehrerhaftung §§ 43 GmbHG 93 AktG. Gesellschafterstreit Beschlussanfechtung. Handelsvertreterausgleich § 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein. |
| `fachanwalt-insolvenz-sanierungsrecht` | Light-Touch-Plugin Fachanwalt fuer Insolvenz- und Sanierungsrecht nach FAO § 14. InsO Eroeffnung Antragspflicht § 15a Glaeubigerantrag § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung §§ 129 ff. InsO. Schnittstellen insolvenzrecht und steuerrecht-kanzlei. |
| `fachanwalt-internationales-wirtschaftsrecht` | Light-Touch-Plugin Fachanwalt fuer Internationales Wirtschaftsrecht. Orientierung CISG Bruessel Ia Rom I Rom II grenzueberschreitende Vertragspraxis Schiedsverfahren ICC UNCITRAL Investitionsschutz ICSID WTO EU-Aussenhandel LkSG. |
| `fachanwalt-it-recht` | Light-Touch-Plugin Fachanwalt fuer Informationstechnologierecht. Orientierung SaaS-Vertraege Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG Open-Source-Compliance Plattformhaftung DSA DMA EU-KI-VO. Schnittstellen datenschutzrecht ki-governance vertragsrecht. |
| `fachanwalt-medizinrecht` | Light-Touch-Plugin Fachanwalt fuer Medizinrecht. Orientierung Arzthaftung §§ 630a ff. BGB Patientenrechte Vertragsarztrecht Berufsrecht Aerzte und Heilberufe SGB V Krankenversicherung MPDG Apothekenrecht. Schnittstellen sozialrecht-kanzlei. |
| `fachanwalt-miet-wohnungseigentumsrecht` | Light-Touch-Plugin Fachanwalt fuer Miet- und Wohnungseigentumsrecht nach FAO § 14e. BGB §§ 535 ff. Wohnraummiete und Gewerberaummiete. Mieterhoehung §§ 558 ff. Kuendigung §§ 543 569 573 BGB. WEG-Beschlussanfechtung § 44 WEG. BetrKV. Schnittstellen kanzlei-allgemein. |
| `fachanwalt-migrationsrecht` | Light-Touch-Plugin Fachanwalt fuer Migrationsrecht. Orientierung AufenthG AsylG GFK Dublin-VO EU-Verfahrensrichtlinie Qualifikations-RL StAG Einbuergerung Aufenthaltsverfestigung Familiennachzug. Notfrist § 36 AsylG (eine Woche). |
| `fachanwalt-sozialrecht` | Light-Touch-Plugin Fachanwalt fuer Sozialrecht nach FAO § 11. SGB I bis XII Sozialgerichtsbarkeit SGG. Widerspruch § 84 SGG Frist ein Monat. Klage Sozialgericht § 87 SGG. Erwerbsminderungsrente. SGB II Buergergeld Bescheid. Schnittstellen sozialrecht-kanzlei und kanzlei-cowork. |
| `fachanwalt-sportrecht` | Light-Touch-Plugin Fachanwalt fuer Sportrecht. Orientierung Verbandsrecht der Sportverbaende DFB FIFA UEFA IOC DOSB CAS Schiedsverfahren Spielervertraege Doping WADA-Code NADA Sponsoring Persoenlichkeitsrechte Sportler Veranstalterhaftung. |
| `fachanwalt-steuerrecht` | Light-Touch-Plugin Fachanwalt fuer Steuerrecht nach FAO § 9. AO Einspruch Stundung Vollstreckungsaufschub. Aussenpruefung Schlussbesprechung. Steuerstrafrecht Selbstanzeige § 371 AO. Schnittstellen steuerrecht-kanzlei und kanzlei-cowork. |
| `fachanwalt-strafrecht` | Light-Touch-Plugin Fachanwalt fuer Strafrecht. Orientierung Normen Notfristen Standardliteratur. StPO StGB Nebenstrafrecht. Strafverteidigung Ermittlungsverfahren Hauptverhandlung Berufung Revision Verfassungsbeschwerde. Ergaenzend zum Plugin aktenaufbereiter-strafrecht. |
| `fachanwalt-transport-speditionsrecht` | Light-Touch-Plugin Fachanwalt fuer Transport- und Speditionsrecht. Orientierung HGB §§ 407 ff. Frachtvertrag §§ 425 ff. Haftung §§ 453 ff. Speditionsvertrag CMR COTIF Montrealer Uebereinkommen Haager Visby Regeln ADSp. |
| `fachanwalt-urheber-medienrecht` | Light-Touch-Plugin Fachanwalt fuer Urheber- und Medienrecht. Orientierung UrhG VGG Verwertungsgesellschaften KUG Recht am eigenen Bild Presserecht Persoenlichkeitsrecht Medienstaatsvertrag. EU-Bezug InfoSoc-RL DSM-RL. Schnittstellen gewerblicher-rechtsschutz und verlagsredaktion. |
| `fachanwalt-vergaberecht` | Light-Touch-Plugin Fachanwalt fuer Vergaberecht. Orientierung GWB §§ 97 ff. VgV UVgO SektVO KonzVgV VOB-A EU-Vergabe-RL Nachpruefungsverfahren Vergabekammer OLG-Vergabesenat. Schnittstellen fachanwalt-bau-architektenrecht. |
| `fachanwalt-verkehrsrecht` | Light-Touch-Plugin Fachanwalt fuer Verkehrsrecht. Orientierung StVG StVO PflVG VVG-Bezuege. Verkehrsunfall Personenschaden Sachschaden Bussgeld Fahrerlaubnis OWi-Verfahren Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstellen zu Versicherungs- und Strafrecht. |
| `fachanwalt-versicherungsrecht` | Light-Touch-Plugin Fachanwalt fuer Versicherungsrecht. Orientierung VVG VAG Berufsunfaehigkeit private Krankenversicherung Lebens- und Rentenversicherung Sachversicherung Haftpflicht D-und-O. Schnittstellen kanzlei-cowork und fachanwalt-verkehrsrecht. |
| `fachanwalt-verwaltungsrecht` | Light-Touch-Plugin Fachanwalt fuer Verwaltungsrecht. Orientierung VwGO VwVfG Bundesland-VwVfG. Anfechtungs- und Verpflichtungsklage Eilrechtsschutz Normenkontrolle Polizei- und Ordnungsrecht. Schnittstellen Migrations- und Sozialrecht. |
| `fluggastrechte` | Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rspr. Tickets erfassen Annullierung vs Verspaetung pruefen aussergewoehnliche Umstaende Distanz und Ausgleich Forderungsschreiben Mahnung Klage Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden. |
| `forderungsmanagement-klagewerkstatt` | Generalisierter Klage-Assistent für Forderungsmanagement-Klagen mit eigenem Plugin-Generator, Zuständigkeitsprüfung und direktem Inkasso-Zahlungsklage-Ersteller. Mahnvorlauf, Teilzahlung/Erfüllung, Anspruchs-Gatekeeper und Klage nur für klare, fällige und belegte Positionen. |
| `fortbestehensprognose` | Fortbestehensprognose nach § 19 Abs. 2 InsO als Geschaeftsfuehrer-Selbstdokumentation. Pruefablauf Bilanzstatus Annahmen Plausibilisierung 12-Monats-Liquiditaet. Sanierungsbausteine harte Patronatserklaerung Comfortletter Gesellschafterdarlehen Rangruecktritt Stundung Forderungsverzicht. IDW S 11 S 6 StaRUG. Funktioniert allein; empfohlene Begleitplugins liquiditaetsplanung (wochenbasierte Liquiditaet) und insolvenzrecht (§ 17 § 18 InsO Antragspflicht). |
| `geldwaeschepraevention-aml-kyc` | Freistehendes Geldwäscheprävention-/AML-/KYC-Plugin: GwG-Risikoanalyse, Kundenprüfung, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister, Monitoring, Schulung, Audit, Behördenverfahren und Remediation. |
| `gesellschaftsrecht` | M&A-Due-Diligence (ohne Discovery, mit Q&A/Datenraum), Gesellschafterbeschlüsse, Closing Checklists, HRB/HRA-Anmeldungen, Compliance-Fristen. |
| `gewerblicher-rechtsschutz` | DPMA-/EUIPO-Markenrecherche und Anmeldung, Freedom-to-Operate, Patentscreening, UWG-/Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechtsfristen. |
| `grosskanzlei-corporate-ma` | Freistehendes Big-Law-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI. |
| `immobilienrechtspraxis` | Werkzeuge fuer immobilienrechtliche Rechtsabteilungen — musterbasierte Vertragserstellung mit Klauselschutz; Vertragspruefung gegen Playbook; Grundbuchanalyse; Sachverhaltsermittlung; Mieteranfragen mit BGH-Verankerung; Case Management; projektbasierte Arbeitsweise mit AVV-Pruefung. |
| `insolvenzforderungsanmeldungspruefung` | Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung. |
| `insolvenzplan-starug-planwerkstatt` | Freistehende Insolvenzplan- und StaRUG-Planwerkstatt: Sanierungskonzept, integrierte Planung, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug. |
| `insolvenzrecht` | Insolvenz- und sanierungsrechtliche Skills: strukturierte Prüfung Zahlungsunfähigkeit (§ 17 InsO) anhand der BGH-Rechtsprechung (BGHZ 163, 134), zweistufige Überschuldungsprüfung (§ 19 InsO) mit Fortbestehensprognose nach IDW S 11, Antragspflicht Geschäftsleiter (§ 15a InsO) und Haftung Insolvenzverschleppung, Gläubigerantrag-Prüfung (§ 14 InsO), rollierende Liquiditätsvorschau 13 Wochen / 24 Monate. |
| `insolvenzverwaltung` | Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, § 15b InsO, Masse, Forderungsprüfung, Insolvenzplan-/StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung. |
| `jveg-kostenpruefer` | Freistehender JVEG-Kostenprüfer: Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen-/Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle. |
| `jurastudium` | Studium und Referendariat – Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte, Lernstrategien, Tatbestände lernen, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung. |
| `kanzlei-allgemein` | Kanzlei-Allgemein-Plugin: edles Cowork-Kommandocenter, Mandatsannahme/GwG, Klage/Replik, Vertrag, Rechtsprechungsrecherche, Handelsregister, beA, Fristen, HR, Rechnung, Bankmatching, XRechnung, UStVA. |
| `kanzlei-builder-hub` | Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Einsatz in der Kanzleiumgebung. Enthält zusätzlich den Skill 'playbook-aus-eigenen-daten', der aus Mandantenkorrespondenz und Aktenexporten ein wiederverwendbares Spielbuch (Playbook) ableitet — mit verbindlicher Pseudonymisierung nach DSGVO/BRAO. |
| `kanzlei-cowork` | Cowork-Assistent fuer die deutsche Anwaltskanzlei. Fristenbuch Timesheet Rechnungserstellung nach RVG Versand-Vor-Check (PDF beA Signatur Adressat Anlagen) beA-Versand-Pruefung Postein- und ausgang Mandantenakte Aktenbestandspflege Honorar-Mahnwesen Mandantenbrief-Vorlagen Geburtstags- und Weihnachtskarten Sekretariats-Tagesbrief. |
| `ki-governance` | EU-KI-VO + DSGVO: Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie. |
| `liquiditaetsplanung` | Eigenständiges Power-Plugin Liquiditätsvorschau nach deutschem Recht. Wochenaktuelle 3-Wochen-Vorschau § 17 InsO und rollierende 13/26/52-Wochen-Planung, jeweils mit Excel-Vorlage (Freitag-Stichtag, KW-Spalten) und optionalem interaktivem HTML-Padlet oder Markdown-Artefakt. BGH-Schema strikt: Passiva II zwingend (BGHZ 217, 129), 10-%-Schwelle und 3-Wochen-Horizont (BGHZ 163, 134), Bugwellenrspr. (BGH II ZR 112/21), titulierte Forderungen mit Nennwert (BGH IX ZR 229/22), objektive Beurteilung (BGH II ZR 139/23). Banking optional (manuell, CAMT.053/MT940/CSV/DATEV-OPOS, Connector). Memo nur auf Anfrage. Funktioniert allein, ergänzt sich aber mit insolvenzrecht und steuerberater-werkzeuge. |
| `memorandums-ersteller` | Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausfuehrungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. |
| `methodenlehre-buergerliches-recht` | Deutsche juristische Methodenlehre und Falllösung fuer das buergerliche Recht aus anwaltlicher Perspektive. Gutachtenstil mit Anspruchsgrundlagen-Reihenfolge. Auslegung Wortlaut Systematik Historie Telos ohne starre Rangfolge — pragmatische Gewichtung wie in der BGH-Praxis. Generalklauseln und Rechtsfortbildung als reale Werkzeuge. Anwaltliche Strategie statt richterliche Selbstbindung. Breaking Change in v3.0 umbenannt von methodenlehre-deutsches-recht. |
| `mietrecht` | Mietrecht fuer Mieter und Vermieter mit ausschliesslich amtlichen Mietspiegel-Quellen pro Bundesland und fuer Top- und Universitaetsstaedte. Acht Skills Datenerhebung Mieterhoehungs-Widerspruch Mietsenkungsverlangen Nebenkostenpruefung Mieteranfragen Klageentwurf Amtsgericht. |
| `mittelstand-corporate-ma` | Freistehendes Corporate/M&A-Plugin für mittelständische Kanzleien: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI. |
| `nda-abgleich` | NDA-Verhandlungshilfe fuer die empfangende Seite. Akzeptiert den Entwurf der Gegenseite und setzt den eigenen Standard chirurgisch durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Word-Tracked-Changes. Keine Absatzloeschungen, keine Klausel-Neufassungen. |
| `patentrecherche` | Patentrecherche fuer Patentanwaelte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO PATENTSCOPE USPTO. Stand der Technik Neuheit (§ 3 PatG Art. 54 EPUe) erfinderische Taetigkeit (§ 4 PatG Art. 56 EPUe) Problem-Solution-Approach Freedom-to-Operate CPC-/IPC-Klassifikation INPADOC-Patentfamilie Rechtsstand Patentbeobachtung Recherchebericht. Funktioniert allein; empfohlenes Begleitplugin gewerblicher-rechtsschutz (Marke Design UWG). |
| `phishing-vorfall-pruefer` | Freistehender Phishing-Vorfall-Prüfer für Online-Banking: § 675u/§ 675v BGB, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Banklogs, Bankpflichten, Schlichtung und Klage. |
| `produktrecht` | Produkt-Launches, Impressumspflicht (§§ 5, 6 DDG), Preisangabenverordnung, Marketing-Claims, UWG-Konformität, schnelle 'Ist das ein Problem?'-Bewertungen. |
| `prozessrecht` | Zivil-, Straf-, Verwaltungs- und Arbeitsgerichtsprozess: Mandatsportfolio, Fristen, Mahnbescheid, einstweilige Verfügung + Schutzschrift, Zwangsvollstreckung, Verkehrsunfall, Schriftsatzentwürfe, Anhörungsrüge, Beweisermittlung ohne Discovery. |
| `rechtsberatungsstelle` | Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe. |
| `regulatorisches-recht` | Aufsichtsrecht (KWG, ZAG, WpHG, GwG), EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds und Wochendigest. |
| `sozialrecht-kanzlei` | Vollassistenz fuer die sozialrechtliche Kanzlei: Bescheidanalyse Widerspruch Klage zum Sozialgericht Eilantrag Akteneinsicht Anlagenerstellung. Spezialisiert auf Buergergeld SGB II SGB IX Schwerbehinderung Pflege Hilfsmittel (Rollstuhl Hoerhilfe Vorlesekraft) Eingliederungshilfe SGB VIII Schulbegleitung. Fristenbuch und PKH. Funktioniert allein; empfohlenes Begleitplugin kanzlei-cowork (Skill versand-vor-check fuer Versandkontrolle Fristenbuch Mandantenakte). |
| `steuerberater-werkzeuge` | Werkzeugbox für Steuerberater und GmbH-Geschäftsleitung: BWA-/SuSa-/Bilanz-Krisenprüfung (§§ 17, 19 InsO, § 102 StaRUG-Hinweispflicht). Für die rollierende Liquiditätsplanung 13/26/52 Wochen siehe das eigene Plugin `liquiditaetsplanung`. |
| `steuerrecht-kanzlei` | Vollassistenz fuer die steuerrechtsanwaltliche Kanzlei: Bescheidanalyse Einspruch nach AO Klage zum Finanzgericht Aussetzung der Vollziehung Aussenpruefung Selbstanzeige Verbindliche Auskunft Akteneinsicht Steuerakte. Nicht Steuererklaerung (DATEV Steuerberater) sondern anwaltlich-streitbezogene Folgebearbeitung. |
| `strafbefehl-verteidiger` | Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung. |
| `tabellenreview-3d` | 3D-Tabellenreview als Wuerfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenpruefung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette. |
| `umweltrecht` | Freistehendes Umweltrecht-Plugin: Emissionshandel, BImSchG, Störfall, Abfall und Circular Economy, Wasser, Boden, Naturschutz, UIG/IFG, Verwaltungsverfahren, Bußgeld, Schulung und Umwelt-Due-Diligence. |
| `verfassungsrecht` | Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz formelle und materielle Verfassungsmäßigkeit Grundrechte und Verfassungsbeschwerde. |
| `verkehr-infrastrukturrecht` | Freistehendes Verkehrs- und Infrastrukturrecht-Plugin: Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Sondernutzung, Parkraumbewirtschaftung, Wirtschaftsverkehr, Lieferzonen, Verkehrswende, Schulwegsicherheit, Förderung und Vergabe. |
| `verkehrsowi-verteidiger` | Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht. |
| `verlagsredaktion` | Verlegerischer Redaktionsassistent. Modus A macht aus disparaten Inputs (Transkripte PPT Screenshots Videos Notizen) ein Rohmanuskript als Anschubhilfe. Modus B ueberarbeitet umgliedert verdichtet erkennt Widersprueche. Hauszitierweise mit Pinpoint-Randnummer. |
| `vertragsausfueller` | Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, Clean-Verträge erzeugen und Track Changes nur nach ausdrücklicher Nachfrage vorbereiten. |
| `vertragsrecht` | Prüft NDA, AGB, SaaS-Verträge, Lieferanten- und Vertriebsverträge nach deutschem Recht (§§ 305 ff. BGB, HGB), trackt Verlängerungs- und Kündigungstermine, eskaliert nach internem Playbook und erstellt Business-Zusammenfassungen. |
| `zitierweise-deutsches-recht` | Deutsche juristische Hauszitierweise v3.0. Rspr. mit Az.-Marker Datum Aktenzeichen Fundstelle Rn. Bearbeiter-Kommentar mit in: und Einzelautorenkommentar ohne in:. Verlag bei Monographien. Diss. und Habil. mit Hochschulort. Reihenfolge erst Gerichtshierarchie dann Chronologie oder Relevanz. Palandt heisst seit 2022 Grueneberg. |
| `zwangsverwaltung-zvg` | Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme. |

## Fallakten-Assets (28 Stück)

URL-Schema: `https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<asset>.zip`

**Wichtig:** Diese ZIPs sind **keine Plugins**. Sie enthalten Mandatsunterlagen für Testzwecke und gehören in den Chat, nicht in den Plugin-Upload-Dialog.

| Asset | Inhalt |
| --- | --- |
| `testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip` | siehe `testakten/aussenwirtschaft-zoll-sanktionen-globalmaschinen/` |
| `testakte-beispielakte-edelholz-berlin.zip` | siehe `testakten/beispielakte-edelholz-berlin/` |
| `testakte-betreuung-hildegard-sauer.zip` | siehe `testakten/betreuung-hildegard-sauer/` |
| `testakte-betreuung-schmalfeld-kontodaten-vertraege.zip` | siehe `testakten/betreuung-schmalfeld-kontodaten-vertraege/` |
| `testakte-common-law-kompass-crossborder-contract.zip` | siehe `testakten/common-law-kompass-crossborder-contract/` |
| `testakte-einfache-leichte-sprache-jura-mandantenbrief.zip` | siehe `testakten/einfache-leichte-sprache-jura-mandantenbrief/` |
| `testakte-energierecht-stadtwerke-quartier.zip` | siehe `testakten/energierecht-stadtwerke-quartier/` |
| `testakte-europarecht-kompass-beihilfe-richtlinie.zip` | siehe `testakten/europarecht-kompass-beihilfe-richtlinie/` |
| `testakte-fluggastrechte-familie-braeutigam.zip` | siehe `testakten/fluggastrechte-familie-braeutigam/` |
| `testakte-fortbestehensprognose-paragrafix-gmbh.zip` | siehe `testakten/fortbestehensprognose-paragrafix-gmbh/` |
| `testakte-geldwaesche-aml-kyc-musterholding.zip` | siehe `testakten/geldwaesche-aml-kyc-musterholding/` |
| `testakte-grosskanzlei-corporate-ma-datenraum.zip` | siehe `testakten/grosskanzlei-corporate-ma-datenraum/` |
| `testakte-insolvenzverwaltung-moebelwerk-havelberg-regelverfahren.zip` | siehe `testakten/insolvenzverwaltung-moebelwerk-havelberg-regelverfahren/` |
| `testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip` | siehe `testakten/insolvenzforderungsanmeldungspruefung-phoenix-solar/` |
| `testakte-insolvenzplan-starug-planwerkstatt-metallbau-hansa.zip` | siehe `testakten/insolvenzplan-starug-planwerkstatt-metallbau-hansa/` |
| `testakte-inkasso-zahlungsklage-modefuchs.zip` | siehe `testakten/inkasso-zahlungsklage-modefuchs/` |
| `testakte-jveg-zeugin-berger-lg-tuebingen.zip` | siehe `testakten/jveg-zeugin-berger-lg-tuebingen/` |
| `testakte-kanzlei-allgemein-alltag.zip` | siehe `testakten/kanzlei-allgemein-alltag/` |
| `testakte-phishing-vorfall-mayer-sparkasse-berlin.zip` | siehe `testakten/phishing-vorfall-mayer-sparkasse-berlin/` |
| `testakte-sozialrecht-rollstuhl-tannenberg.zip` | siehe `testakten/sozialrecht-rollstuhl-tannenberg/` |
| `testakte-strafbefehl-ladendiebstahl-fahrerflucht-musterakte.zip` | siehe `testakten/strafbefehl-ladendiebstahl-fahrerflucht-musterakte/` |
| `testakte-umweltrecht-industrieanlage-genehmigung.zip` | siehe `testakten/umweltrecht-industrieanlage-genehmigung/` |
| `testakte-verkehr-infrastrukturrecht-strassenbahn-ladezonen.zip` | siehe `testakten/verkehr-infrastrukturrecht-strassenbahn-ladezonen/` |
| `testakte-verkehrsowi-rotlicht-tempo-musterakte.zip` | siehe `testakten/verkehrsowi-rotlicht-tempo-musterakte/` |
| `testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip` | siehe `testakten/vertragsausfueller-bsag-kiosk-huckelriede/` |
| `testakte-zwangsverwaltung-friedrichshoefe-berlin.zip` | siehe `testakten/zwangsverwaltung-friedrichshoefe-berlin/` |
| `testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip` | siehe `testakten/zwangsverwaltung-zvg-versteigerung-eppendorf-altbau/` |
| `testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip` | siehe `testakten/zwangsverwaltung-zvg-mietshaus-parkstrasse/` |

## Manifest-Asset (1 Stück)

| Asset | Verwendung |
| --- | --- |
| `marketplace.json` | Marketplace-Manifest mit Plugin-Liste und Beschreibungen. **Kein Plugin.** |

## Asset-Anzahl pro Release

| Typ | Anzahl | Summe |
| --- | --- | --- |
| plugin | 80 | |
| fallakte | 28 | |
| manifest | 1 | |
| **gesamt** | | **109** |

## Verifikation eines Release

```bash
curl -s "https://api.github.com/repos/Klotzkette/claude-fuer-deutsches-recht/releases/latest" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('Tag:', d['tag_name']); print('Assets:', len(d['assets'])); [print(' -', a['name']) for a in d['assets']]"
```

Erwartet: 108 Assets, davon 80 Plugin-ZIPs, 27 Fallakten-ZIPs mit `testakte-`-Prefix und eine `marketplace.json`.
