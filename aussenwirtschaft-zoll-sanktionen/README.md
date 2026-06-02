# Außenwirtschaft, Sanktionen, Zoll und CBAM

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`aussenwirtschaft-zoll-sanktionen`) | [`aussenwirtschaft-zoll-sanktionen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aussenwirtschaft-zoll-sanktionen.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Außenwirtschaft, Zoll, Sanktionen und CBAM – Globalmaschinen GmbH** (`aussenwirtschaft-zoll-sanktionen-globalmaschinen`) | [Gesamt-PDF lesen](../testakten/aussenwirtschaft-zoll-sanktionen-globalmaschinen/gesamt-pdf/aussenwirtschaft-zoll-sanktionen-globalmaschinen_gesamt.pdf) | [`testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip) |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Außenwirtschafts-, Sanktions-, Zoll- und CBAM-Plugin für international tätige Unternehmen, Einzelpersonen, Verbände, Import-/Exportabteilungen, Zollteams, Compliance, Geschäftsleitung und anwaltliche Krisenmandate.

Dieses Plugin ist **vollständig freistehend**. Es verweist nicht auf andere Plugins und bringt eigene Skills, Vorlagen, Leitplanken, Vorschau und Testakte mit. Wenn keine Schnittstelle zu ERP, Zollsoftware, Screening-Tool, CBAM-Register, ELAN-K2, Bundesbank-Portal oder Kanzleisystem besteht, arbeitet es mit manuellen Uploads oder einem ausdrücklich gekennzeichneten Simulationsmodus.

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **GlobalMaschinen (Aussenwirtschaft, Zoll, Sanktionen)** | [testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip) |

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

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Aussenwirtschaft Zoll Sanktionen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klare... |
| `aussenwirtschaft-abfallverbringung` | Vertiefter Skill fuer Abfallverbringung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-aeo-bewilligung-monitoring` | Vertiefter Skill fuer Aeo Bewilligung Monitoring. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-aktive-veredelung` | Vertiefter Skill fuer Aktive Veredelung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-allgemeingenehmigung-agg-finder` | Vertiefter Skill fuer Allgemeingenehmigung Agg Finder. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-aml-kyc-sanktionen` | Verknuepft GwG-Risikoanalyse KYC Sanktionsscreening und interne Kontrollpflichten im Aussenhandel. Anwendungsfall Exporteur oder Haendler braucht integriertes AML- und Sanktions-Compliance-System für grenzüberschreitende Geschäfte. Norme... |
| `aussenwirtschaft-antidumping-ausgleich` | Antidumping Antisubvention und Ausgleichsmassnahmen im EU-Aussenhandelsrecht. Anwendungsfall Import- oder Exporteur ist von Antidumping-Massnahmen betroffen oder will Erstattungsantrag stellen. Normen EU-Antidumpingverordnung 2016/1036 A... |
| `aussenwirtschaft-antidumping-erstattung-review` | Vertiefter Skill fuer Antidumping Erstattung Review. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-antidumping-taric-massnahmen` | Vertiefter Skill fuer Antidumping TARIC Massnahmen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-asset-freeze-sofortmassnahmen` | Vertiefter Skill fuer Asset Freeze Sofortmassnahmen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-atlas-ausfuhranmeldung-check` | Vertiefter Skill fuer Atlas Ausfuhranmeldung Check. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-atlas-einfuhr-abgabenbescheid` | Vertiefter Skill fuer Atlas Einfuhr Abgabenbescheid. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-audit-trail-freigaben` | Vertiefter Skill fuer Audit Trail Freigaben. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-ausfuhrverantwortlicher-organisation` | Vertiefter Skill fuer Ausfuhrverantwortlicher Organisation. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-awv-beteiligungsmeldungen` | Vertiefter Skill fuer AWV Beteiligungsmeldungen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-awv-bundesbank` | Meldepflichten nach Aussenwirtschaftsverordnung AWV gegenüber Bundesbank für grenzüberschreitende Zahlungen und Beteiligungen. Anwendungsfall Unternehmen hat Zahlungen ins Ausland oder Auslandsforderungen und prüft AWV-Meldepflichten. No... |
| `aussenwirtschaft-awv-z4-z10-z11-meldungen` | Vertiefter Skill fuer AWV Z4 Z10 Z11 Meldungen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-bafa-elan-k2-antragspaket` | Vertiefter Skill fuer BAFA-ELAN-K2-Antrag mit Anlagen, technischer Beschreibung und Endverbleibsdokumenten. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Z... |
| `aussenwirtschaft-bafa-genehmigungen` | BAFA-Genehmigungsverfahren für Exporte und Dienstleistungen mit Genehmigungspflicht. Anwendungsfall Exporteur braucht BAFA-Ausfuhrgenehmigung für gueterlistenpflichtige Ware oder Technologie. Normen § 8 AWG Genehmigungspflicht EU-Dual-Us... |
| `aussenwirtschaft-bafa-nullbescheid-azg` | Vertiefter Skill fuer BAFA Nullbescheid Azg. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-catch-all-pruefung` | Vertiefter Skill fuer Catch-all-Pruefung bei kritischer Endverwendung, Militaerbezug oder Massenvernichtungswaffenrisiko. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenw... |
| `aussenwirtschaft-cbam-berichtspflichten-uebergang` | Vertiefter Skill fuer CBAM-Uebergangsberichte, CN-Codes, direkte und indirekte Emissionen und Lieferantendaten. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts... |
| `aussenwirtschaft-cbam-co2-zoll` | Carbon Border Adjustment Mechanism CBAM CO2-Grenzausgleich für Einfuhren aus Drittlaendern. Anwendungsfall Unternehmen importiert CBAM-pflichtige Waren Stahl Aluminium Zement Duenger Strom und muss CBAM-Pflichten erfuellen. Normen EU-CBA... |
| `aussenwirtschaft-cbam-lieferantendaten-emissionen` | Vertiefter Skill fuer CBAM Lieferantendaten Emissionen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-cbam-zertifikate-kosten` | Vertiefter Skill fuer CBAM-Zertifikate, Kostenmodell, Einkaufsdaten und Controlling-Schnittstelle. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und... |
| `aussenwirtschaft-chemikalien-reach-pic` | Vertiefter Skill fuer Chemikalien Reach Pic. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-cites-artenschutz` | Vertiefter Skill fuer Cites Artenschutz. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-distributor-vertrag-exportkontrolle` | Vertiefter Skill fuer Distributor Vertrag Exportkontrolle. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-dual-use-forschung-hochschule` | Vertiefter Skill fuer Dual Use Forschung Hochschule. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-embargo-belarus` | Vertiefter Skill fuer Belarus-Embargo mit Sanktionslisten, Gueterverboten, Transport- und Finanzierungsfragen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-... |
| `aussenwirtschaft-embargo-iran` | Vertiefter Skill fuer Embargo Iran. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-embargo-myanmar` | Vertiefter Skill fuer Embargo Myanmar. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-embargo-nordkorea` | Vertiefter Skill fuer Embargo Nordkorea. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-embargo-russland` | Vertiefter Skill fuer EU-Russland-Embargo, Umgehungsrisiken, No-Russia-Clause, Altvertrag und Dienstleistungsverbote. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirts... |
| `aussenwirtschaft-embargo-syrien` | Vertiefter Skill fuer Embargo Syrien. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-endverwendung-endverwender-euc` | Vertiefter Skill fuer Endverwendung Endverwender Euc. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-eori-registrierung-stammdaten` | Vertiefter Skill fuer EORI Registrierung Stammdaten. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-erp-stammdaten-kontrollpunkte` | Vertiefter Skill fuer ERP Stammdaten Kontrollpunkte. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-ersatzteile-dual-use` | Vertiefter Skill fuer Ersatzteile Dual Use. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-exporteur-ausfuehrer-anmelder-rollen` | Vertiefter Skill fuer Exporteur Ausfuehrer Anmelder Rollen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-exportkontrolle-dual-use` | Exportkontrolle Dual-Use-Prüfung für Gueter Software Technologie und Dienstleistungen mit Doppelverwendungszweck. Anwendungsfall Exporteur prüft ob Ware oder Software unter Dual-Use-Regulierung faellt und Genehmigung benoetigt. Normen EU... |
| `aussenwirtschaft-exportkontrollklauseln-vertrag` | Vertiefter Skill fuer Exportkontrollklauseln Vertrag. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-f-gase-ozonstoffe` | Vertiefter Skill fuer F Gase Ozonstoffe. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-financial-institutions-correspondent-banking` | Vertiefter Skill fuer Financial Institutions Correspondent Banking. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-finanzsanktionen-eigentum-kontrolle` | Vertiefter Skill fuer Finanzsanktionen Eigentum Kontrolle. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll` | Vertiefter Skill fuer Freiwillige Offenlegung BAFA Zoll. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-gueterlisten-klassifizierung` | Klassifizierungsdossier für Exportkontrolle Zolltarif und Dual-Use-Einordnung. Anwendungsfall Produkt muss für Exportkontrolle und Zoll einheitlich klassifiziert werden. Normen EU-Dual-Use-Liste Anhang I Verordnung 2021/821 UZK Art. 33 V... |
| `aussenwirtschaft-icp-kontrollsystem` | Entwurf und Haertung eines integrierten Compliance-Programms ICP für Exportkontrolle Zoll Sanktionen CBAM und AML. Anwendungsfall Unternehmen will rechtssicheres ICP aufbauen oder bestehendes System haerten. Normen AWG § 22 Sorgfaltspfli... |
| `aussenwirtschaft-incoterms-exportkontrolle` | Vertiefter Skill fuer Incoterms Exportkontrolle. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-internal-investigation-aussenwirtschaft` | Vertiefter Skill fuer Internal Investigation Aussenwirtschaft. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-investitionspruefung-bmwk` | Vertiefter Skill fuer AWV-Investitionspruefung beim BMWK, sektoruebergreifend und sektorspezifisch. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und... |
| `aussenwirtschaft-know-your-customer-exportkontrolle` | Vertiefter Skill fuer Know Your Customer Exportkontrolle. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-kommandocenter` | Kommandocenter für alle Aussenhandels- Zoll- Sanktions- CBAM- und Ermittlungsmandate vom Intake bis zum Handlungsvorschlag. Anwendungsfall Anwalt oder Compliance-Beauftragter will grenzüberschreitendes Mandat schnell triagieren. Normen A... |
| `aussenwirtschaft-kontingente-lizenzen-trq` | Vertiefter Skill fuer Kontingente Lizenzen Trq. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-kritische-infrastruktur-investment` | Vertiefter Skill fuer Kritische Infrastruktur Investment. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-kulturgut-einfuhr-ausfuhr` | Vertiefter Skill fuer Kulturgut Einfuhr Ausfuhr. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-lebensmittel-futtermittel-vub` | Vertiefter Skill fuer Lebensmittel Futtermittel VUB. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-legal-hold-datenextraktion` | Vertiefter Skill fuer Legal Hold Datenextraktion. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-lieferanten-onboarding-aussenhandel` | Vertiefter Skill fuer Lieferanten Onboarding Aussenhandel. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-lieferkettensorgfalt-aussenhandel` | Vertiefter Skill fuer Lieferkettensorgfalt Aussenhandel. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-ma-sanctions-export-dd` | Vertiefter Skill fuer Ma Sanctions Export Dd. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-nichtpraeferenzieller-ursprung-made-in` | Vertiefter Skill fuer Nichtpraeferenzieller Ursprung Made In. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-ofac-sdn-non-sdn` | Vertiefter Skill fuer US-Sanktionslisten, SDN-, Non-SDN- und Fifty-Percent-Rule als Risikohinweis fuer deutsche Unternehmen. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Auss... |
| `aussenwirtschaft-passive-veredelung` | Vertiefter Skill fuer Passive Veredelung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-post-merger-icp-integration` | Vertiefter Skill fuer Post Merger Icp Integration. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-praeferenzkalkulation-lieferantenerklaerung` | Vertiefter Skill fuer Praeferenzkalkulation Lieferantenerklaerung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-presse-krise` | Rechtliche und kommunikative Schadensbegrenzung bei Sanktionsverstoss Behördenmassnahmen oder Lieferkettenvorwuerfen. Anwendungsfall negative Berichterstattung droht oder Behoerde hat Massnahmen eingeleitet und Unternehmen braucht kombin... |
| `aussenwirtschaft-produktsicherheit-vub-schnittstelle` | Vertiefter Skill fuer Produktsicherheit VUB Schnittstelle. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-pruefung-ermittlung` | Begleitung von Aussenwirtschaftsprüfungen Zollprüfungen Durchsuchungen und Strafverfahren. Anwendungsfall Behorde kueendigt Prüfung an oder Durchsuchung hat stattgefunden. Normen AWG § 34 Strafrecht OWiG § 19 Sanktionen ZK Art. 48 Zollpr... |
| `aussenwirtschaft-reexport-weitergabe-kettenlieferung` | Vertiefter Skill fuer Reexport Weitergabe Kettenlieferung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-rueckwaren-erlass-erstattung` | Vertiefter Skill fuer Rueckwaren Erlass Erstattung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-sammelgenehmigung-export` | Vertiefter Skill fuer Sammelgenehmigung Export. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-sanktionen-embargos` | Prüfung von Laenderembargos personenbezogenen Sanktionen und Umgehungsrisiken im Aussenhandel. Anwendungsfall Handelspartner koennte Sanktionslistentreffer haben oder Lieferung in Sanktionsland geht. Normen EU-Sanktionsverordnungen Art.... |
| `aussenwirtschaft-sanktionsscreening-fuzzy-match` | Vertiefter Skill fuer Sanktionsscreening mit Fuzzy Matches, wirtschaftlich Berechtigten und Freigabeprotokoll. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-... |
| `aussenwirtschaft-sanktionsumgehung-red-flags` | Vertiefter Skill fuer Sanktionsumgehung Red Flags. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-schulung-exportkontrolle-rollout` | Vertiefter Skill fuer Schulung Exportkontrolle Rollout. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-schutzmassnahmen-safeguards` | Vertiefter Skill fuer Schutzmassnahmen Safeguards. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-screening-tool-validierung` | Vertiefter Skill fuer Screening Tool Validierung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-software-verschluesselung-kryptografie` | Vertiefter Skill fuer Software Verschluesselung Kryptografie. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-swiss-sanctions-touchpoint` | Vertiefter Skill fuer Swiss Sanctions Touchpoint. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-technologie-transfer-cloud-download` | Vertiefter Skill fuer Technologie Transfer Cloud Download. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-trade-finance-lc-guarantees` | Vertiefter Skill fuer Trade Finance Lc Guarantees. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-transferpricing-zollwert-abgleich` | Vertiefter Skill fuer Transferpricing Zollwert Abgleich. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-uk-sanctions-touchpoint` | Vertiefter Skill fuer UK Sanctions Touchpoint. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-us-ear-itar` | US-Exportkontrolle EAR ITAR und OFAC für Unternehmen mit US-Bezug im Aussenhandel. Anwendungsfall Produkt enthaelt US-Komponenten oder unterliegt US-Recht und Reexport- oder Weitergabepflichten muessen geprüft werden. Normen EAR 15 CFR §... |
| `aussenwirtschaft-verbrauchsteuer` | Verbrauchsteuerrecht für Energieerzeugnisse Strom Tabak Alkohol Bier Schaumwein und Kaffee. Anwendungsfall Hersteller oder Haendler prüft Steuerlager Steueraussetzungsverfahren oder Entlastungsantrag. Normen EnergieStG StromStG TabakStG... |
| `aussenwirtschaft-versandverfahren-ncts` | Vertiefter Skill fuer Versandverfahren NCTS. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-voruebergehende-verwendung-ata-carnet` | Vertiefter Skill fuer Voruebergehende Verwendung ATA Carnet. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-vub-einfuhr-ausfuhr` | Verbote und Beschraenkungen VuB für besondere Waren wie Dual-Use Kulturgut CITES F-Gase Lebensmittel und Russland-Iranembargos. Anwendungsfall Import oder Export einer Ware koennte VuB-Beschraenkungen unterliegen. Normen CITES-Verordnung... |
| `aussenwirtschaft-vzta-antrag-qualitaetsgate` | Vertiefter Skill fuer VZTA Antrag Qualitaetsgate. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-warennummer-hs-cn-taric-einreihung` | Vertiefter Skill fuer Warennummer, HS, KN, TARIC, Einreihungsargumentation und verbindliche Zolltarifauskunft. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-... |
| `aussenwirtschaft-wto-handelspolitik` | WTO Handelspolitik GATT GATS TRIPS und Streitbeilegung für Aussenhandelsmandate. Anwendungsfall Handelspartner klagt WTO-Verstoss oder Unternehmen ist von Schutzmassnahmen betroffen. Normen GATT 1994 GATS TRIPS DSU Streitbeilegungsverein... |
| `aussenwirtschaft-zoll-straf-bussgeld-selbstkorrektur` | Vertiefter Skill fuer Zoll Straf Bussgeld Selbstkorrektur. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-zolllager-freilager` | Vertiefter Skill fuer Zolllager Freilager. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-zollpruefung-aussenpruefung` | Vertiefter Skill fuer Zollpruefung Aussenpruefung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-zollschuld-entstehung-haftung` | Vertiefter Skill fuer Zollschuld Entstehung Haftung. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-zolltarif-vzta` | Workflow-Skill zu aussenwirtschaft zolltarif vzta. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `aussenwirtschaft-zollverfahren-bewilligungen` | Zollverfahren und Bewilligungen im Union-Zollkodex für AEO vereinfachte Anmeldung und besondere Verfahren. Anwendungsfall Unternehmen will Versandverfahren Zolllager aktive Veredelung oder AEO-Zertifizierung nutzen. Normen UZK Art. 77 ff... |
| `aussenwirtschaft-zollwert-royalties-assists` | Vertiefter Skill fuer Zollwert Royalties Assists. Fuehrt durch Intake, Rechtsrahmen, Beleglage, Risikoampel, Dokumentation, Freigabe und naechste Schritte im Aussenwirtschafts-, Zoll- und Sanktionsrecht. |
| `aussenwirtschaft-zollwert-ursprung` | Zollwert Warenursprung Praeferenznachweise und Lieferantenerklarungen im EU-Zollrecht. Anwendungsfall Zoll bestreitet Zollwert oder Praeferenzursprungsnachweis fehlt und Einfuhrabgaben werden nachgefordert. Normen UZK Art. 69-76 Zollwert... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
