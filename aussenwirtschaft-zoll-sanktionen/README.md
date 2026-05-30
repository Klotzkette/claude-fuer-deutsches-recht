# Außenwirtschaft, Sanktionen, Zoll und CBAM

Freistehendes Außenwirtschafts-, Sanktions-, Zoll- und CBAM-Plugin für international tätige Unternehmen, Einzelpersonen, Verbände, Import-/Exportabteilungen, Zollteams, Compliance, Geschäftsleitung und anwaltliche Krisenmandate.

Dieses Plugin ist **vollständig freistehend**. Es verweist nicht auf andere Plugins und bringt eigene Skills, Vorlagen, Leitplanken, Vorschau und Testakte mit. Wenn keine Schnittstelle zu ERP, Zollsoftware, Screening-Tool, CBAM-Register, ELAN-K2, Bundesbank-Portal oder Kanzleisystem besteht, arbeitet es mit manuellen Uploads oder einem ausdrücklich gekennzeichneten Simulationsmodus.

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **GlobalMaschinen (Aussenwirtschaft, Zoll, Sanktionen)** | [testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Außenwirtschaft, Zoll, Sanktionen und CBAM – Globalmaschinen GmbH** ([`testakten/aussenwirtschaft-zoll-sanktionen-globalmaschinen/`](../testakten/aussenwirtschaft-zoll-sanktionen-globalmaschinen/)).

Direkt-Download als ZIP: [testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Schnellstart

1. Plugin aktivieren oder ZIP aus dem Release installieren.
2. Neue Sache mit `aussenwirtschaft-kommandocenter` starten.
3. Ware, Software, Technologie, Dienstleistung oder Zahlung nennen.
4. Länder, Beteiligte, Banken, Endverwender, Zolltarifnummer und vorhandene Dokumente hochladen oder simulieren.
5. Am Ende immer das Qualitätstor ausgeben lassen: Quellenstand, Trefferlog, Fristen, Verbote, Genehmigungen, Meldungen, Abgaben, Anlagen und Sofortmaßnahmen.

## Enthaltene Skills

- `aussenwirtschaft-kommandocenter` - Außenwirtschaft-Kommandocenter
- `aussenwirtschaft-exportkontrolle-dual-use` - Exportkontrolle und Dual-Use
- `aussenwirtschaft-gueterlisten-klassifizierung` - Güterlisten- und Klassifizierungslog
- `aussenwirtschaft-bafa-genehmigungen` - BAFA-Genehmigungen und Anfragen
- `aussenwirtschaft-sanktionen-embargos` - Sanktionen, Embargos und Bereitstellungsverbote
- `aussenwirtschaft-us-ear-itar` - US EAR, ITAR und Extraterritorialität
- `aussenwirtschaft-zolltarif-vzta` - Zolltarif, TARIC und vZTA
- `aussenwirtschaft-zollwert-ursprung` - Zollwert, Ursprung und Präferenzen
- `aussenwirtschaft-zollverfahren-bewilligungen` - Zollverfahren, Bewilligungen und Vereinfachungen
- `aussenwirtschaft-vub-einfuhr-ausfuhr` - Verbote und Beschränkungen bei Ein- und Ausfuhr
- `aussenwirtschaft-cbam-co2-zoll` - CBAM und CO2-Grenzausgleich
- `aussenwirtschaft-verbrauchsteuer` - Verbrauchsteuer
- `aussenwirtschaft-antidumping-ausgleich` - Antidumping- und Ausgleichszölle
- `aussenwirtschaft-wto-handelspolitik` - WTO und handelspolitische Maßnahmen
- `aussenwirtschaft-awv-bundesbank` - AWV- und Bundesbank-Meldepflichten
- `aussenwirtschaft-aml-kyc-sanktionen` - AML, KYC und Sanktions-Compliance
- `aussenwirtschaft-pruefung-ermittlung` - Prüfungen, Ermittlungen und Offenlegung
- `aussenwirtschaft-presse-krise` - Presse, Reputation und Krisenkommunikation
- `aussenwirtschaft-icp-kontrollsystem` - Internal Compliance Program

## Vorlagen

- `assets/templates/aussenwirtschaft-mandatskarte.md` - Außenwirtschaft-Mandatskarte
- `assets/templates/transaction-screening-matrix.md` - Transaktions-Screening-Matrix
- `assets/templates/exportkontrolle-dual-use-pruefung.md` - Exportkontrolle- und Dual-Use-Prüfung
- `assets/templates/gueterlisten-klassifizierungslog.md` - Güterlisten-Klassifizierungslog
- `assets/templates/bafa-genehmigungsantrag.md` - BAFA-Genehmigungs- und Anfragepaket
- `assets/templates/sanktions-embargo-trefferlog.md` - Sanktions- und Embargo-Trefferlog
- `assets/templates/us-ear-itar-touchpoint.md` - US EAR/ITAR-Touchpoint-Check
- `assets/templates/zolltarif-vzta-antrag.md` - Zolltarif- und vZTA-Antrag
- `assets/templates/zollwert-ursprung-praeferenz.md` - Zollwert, Ursprung und Präferenzmatrix
- `assets/templates/zollverfahren-bewilligungen.md` - Zollverfahren- und Bewilligungsmatrix
- `assets/templates/vub-einfuhr-ausfuhr.md` - VuB-Check Einfuhr/Ausfuhr
- `assets/templates/cbam-emissionsdaten-register.md` - CBAM-Emissionsdatenregister
- `assets/templates/verbrauchsteuer-bewilligung.md` - Verbrauchsteuer-Bewilligungs- und Entlastungscheck
- `assets/templates/antidumping-ausgleichszoll-check.md` - Antidumping- und Ausgleichszollcheck
- `assets/templates/wto-handelspolitik-memo.md` - WTO- und Handelspolitik-Memo
- `assets/templates/awv-bundesbank-meldekalender.md` - AWV-Bundesbank-Meldekalender
- `assets/templates/aml-kyc-sanktions-risk-assessment.md` - AML/KYC- und Sanktions-Risikoanalyse
- `assets/templates/pruefung-ermittlung-sofortplan.md` - Prüfungs- und Ermittlungs-Sofortplan
- `assets/templates/offenlegung-verstoss-plan.md` - Offenlegungs- und Nachholplan
- `assets/templates/presse-krisenkommunikation.md` - Presse- und Krisenkommunikationskarte
- `assets/templates/icp-kontrollsystem.md` - Internal-Compliance-Program-Blueprint

## Offizielle Startquellen

- [BAFA Exportkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Allgemeine_Einfuehrung/allgemeine_einfuehrung.html)
- [BAFA Embargos und Namenslistenhinweise](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Embargos/embargos.html)
- [EU Sanctions Map und konsolidierte Finanzsanktionsliste](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en)
- [EU TARIC](https://taxation-customs.ec.europa.eu/customs/common-customs-tariff-cct/tariff-classification-goods/eu-customs-tariff-taric_de)
- [EU CBAM](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)
- [Deutsche Bundesbank AWV-Zahlungsmeldungen](https://www.bundesbank.de/de/service/meldewesen/aussenwirtschaft-formular-center/zahlungsmeldungen)
- [EU Trade Defence Antidumping](https://policy.trade.ec.europa.eu/enforcement-and-protection/trade-defence/anti-dumping-measures_en)
- [Zoll Verbrauchsteuererhebung](https://www.zoll.de/DE/Der-Zoll/Aufgaben-des-Zolls/Einnahmen-fuer-Deutschland-und-Europa/Verbrauchsteuererhebung/verbrauchsteuererhebung.html)

## Freistehende Leitplanken

- Keine Entscheidung auf Basis eingebauter Altdaten: Sanktionen, Embargos, TARIC, CBAM und AWV werden live oder mit dokumentiertem Abrufstand geprüft.
- Keine Sanktionsfreigabe ohne Trefferlog, Eigentum/Kontrolle, Umgehungsprüfung und Freigabeprozess.
- Keine Exportkontrollfreigabe ohne Produktdaten, technische Spezifikation, Güterlistenprüfung, Endverwendung und Endverwender.
- Keine Zollfreigabe ohne Einreihung, Ursprung, Zollwert, Dokumentencodes und TARIC-Maßnahmen.
- Keine CBAM-Aussage ohne Warencode, Warenmenge, Emissionsdatenquelle und sichtbare Annahmen.
- Bei Prüfung, Anhörung, Durchsuchung, Presseanfrage oder möglichem Verstoß: erst Legal Hold, Zuständigkeiten und Verteidigungsstrategie.

## Download

- Plugin-ZIP: [aussenwirtschaft-zoll-sanktionen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aussenwirtschaft-zoll-sanktionen.zip)
- Akte: [testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 20 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Aussenwirtschaft Zoll Sanktionen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klare... |
| `aussenwirtschaft-aml-kyc-sanktionen` | Verknuepft GwG-Risikoanalyse KYC Sanktionsscreening und interne Kontrollpflichten im Aussenhandel. Anwendungsfall Exporteur oder Haendler braucht integriertes AML- und Sanktions-Compliance-System für grenzüberschreitende Geschäfte. Norme... |
| `aussenwirtschaft-antidumping-ausgleich` | Antidumping Antisubvention und Ausgleichsmassnahmen im EU-Aussenhandelsrecht. Anwendungsfall Import- oder Exporteur ist von Antidumping-Massnahmen betroffen oder will Erstattungsantrag stellen. Normen EU-Antidumpingverordnung 2016/1036 A... |
| `aussenwirtschaft-awv-bundesbank` | Meldepflichten nach Aussenwirtschaftsverordnung AWV gegenüber Bundesbank für grenzüberschreitende Zahlungen und Beteiligungen. Anwendungsfall Unternehmen hat Zahlungen ins Ausland oder Auslandsforderungen und prüft AWV-Meldepflichten. No... |
| `aussenwirtschaft-bafa-genehmigungen` | BAFA-Genehmigungsverfahren für Exporte und Dienstleistungen mit Genehmigungspflicht. Anwendungsfall Exporteur braucht BAFA-Ausfuhrgenehmigung für gueterlistenpflichtige Ware oder Technologie. Normen § 8 AWG Genehmigungspflicht EU-Dual-Us... |
| `aussenwirtschaft-cbam-co2-zoll` | Carbon Border Adjustment Mechanism CBAM CO2-Grenzausgleich für Einfuhren aus Drittlaendern. Anwendungsfall Unternehmen importiert CBAM-pflichtige Waren Stahl Aluminium Zement Duenger Strom und muss CBAM-Pflichten erfuellen. Normen EU-CBA... |
| `aussenwirtschaft-exportkontrolle-dual-use` | Exportkontrolle Dual-Use-Prüfung für Gueter Software Technologie und Dienstleistungen mit Doppelverwendungszweck. Anwendungsfall Exporteur prüft ob Ware oder Software unter Dual-Use-Regulierung faellt und Genehmigung benoetigt. Normen EU... |
| `aussenwirtschaft-gueterlisten-klassifizierung` | Klassifizierungsdossier für Exportkontrolle Zolltarif und Dual-Use-Einordnung. Anwendungsfall Produkt muss für Exportkontrolle und Zoll einheitlich klassifiziert werden. Normen EU-Dual-Use-Liste Anhang I Verordnung 2021/821 UZK Art. 33 V... |
| `aussenwirtschaft-icp-kontrollsystem` | Entwurf und Haertung eines integrierten Compliance-Programms ICP für Exportkontrolle Zoll Sanktionen CBAM und AML. Anwendungsfall Unternehmen will rechtssicheres ICP aufbauen oder bestehendes System haerten. Normen AWG § 22 Sorgfaltspfli... |
| `aussenwirtschaft-kommandocenter` | Kommandocenter für alle Aussenhandels- Zoll- Sanktions- CBAM- und Ermittlungsmandate vom Intake bis zum Handlungsvorschlag. Anwendungsfall Anwalt oder Compliance-Beauftragter will grenzüberschreitendes Mandat schnell triagieren. Normen A... |
| `aussenwirtschaft-presse-krise` | Rechtliche und kommunikative Schadensbegrenzung bei Sanktionsverstoss Behördenmassnahmen oder Lieferkettenvorwuerfen. Anwendungsfall negative Berichterstattung droht oder Behoerde hat Massnahmen eingeleitet und Unternehmen braucht kombin... |
| `aussenwirtschaft-pruefung-ermittlung` | Begleitung von Aussenwirtschaftsprüfungen Zollprüfungen Durchsuchungen und Strafverfahren. Anwendungsfall Behorde kueendigt Prüfung an oder Durchsuchung hat stattgefunden. Normen AWG § 34 Strafrecht OWiG § 19 Sanktionen ZK Art. 48 Zollpr... |
| `aussenwirtschaft-sanktionen-embargos` | Prüfung von Laenderembargos personenbezogenen Sanktionen und Umgehungsrisiken im Aussenhandel. Anwendungsfall Handelspartner koennte Sanktionslistentreffer haben oder Lieferung in Sanktionsland geht. Normen EU-Sanktionsverordnungen Art.... |
| `aussenwirtschaft-us-ear-itar` | US-Exportkontrolle EAR ITAR und OFAC für Unternehmen mit US-Bezug im Aussenhandel. Anwendungsfall Produkt enthaelt US-Komponenten oder unterliegt US-Recht und Reexport- oder Weitergabepflichten muessen geprüft werden. Normen EAR 15 CFR §... |
| `aussenwirtschaft-verbrauchsteuer` | Verbrauchsteuerrecht für Energieerzeugnisse Strom Tabak Alkohol Bier Schaumwein und Kaffee. Anwendungsfall Hersteller oder Haendler prüft Steuerlager Steueraussetzungsverfahren oder Entlastungsantrag. Normen EnergieStG StromStG TabakStG... |
| `aussenwirtschaft-vub-einfuhr-ausfuhr` | Verbote und Beschraenkungen VuB für besondere Waren wie Dual-Use Kulturgut CITES F-Gase Lebensmittel und Russland-Iranembargos. Anwendungsfall Import oder Export einer Ware koennte VuB-Beschraenkungen unterliegen. Normen CITES-Verordnung... |
| `aussenwirtschaft-wto-handelspolitik` | WTO Handelspolitik GATT GATS TRIPS und Streitbeilegung für Aussenhandelsmandate. Anwendungsfall Handelspartner klagt WTO-Verstoss oder Unternehmen ist von Schutzmassnahmen betroffen. Normen GATT 1994 GATS TRIPS DSU Streitbeilegungsverein... |
| `aussenwirtschaft-zolltarif-vzta` | Workflow-Skill zu aussenwirtschaft zolltarif vzta. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `aussenwirtschaft-zollverfahren-bewilligungen` | Zollverfahren und Bewilligungen im Union-Zollkodex für AEO vereinfachte Anmeldung und besondere Verfahren. Anwendungsfall Unternehmen will Versandverfahren Zolllager aktive Veredelung oder AEO-Zertifizierung nutzen. Normen UZK Art. 77 ff... |
| `aussenwirtschaft-zollwert-ursprung` | Zollwert Warenursprung Praeferenznachweise und Lieferantenerklarungen im EU-Zollrecht. Anwendungsfall Zoll bestreitet Zollwert oder Praeferenzursprungsnachweis fehlt und Einfuhrabgaben werden nachgefordert. Normen UZK Art. 69-76 Zollwert... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
