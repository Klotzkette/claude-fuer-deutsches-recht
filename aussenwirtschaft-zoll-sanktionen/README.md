# Außenwirtschaft, Sanktionen, Zoll und CBAM

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

## Testakte

Zum Ausprobieren liegt eine fiktive Testakte unter `testakten/aussenwirtschaft-zoll-sanktionen-globalmaschinen`. Sie wird im Release als `testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip` bereitgestellt und ist kein Bestandteil des Plugin-ZIPs.

## Download

- Plugin-ZIP: [aussenwirtschaft-zoll-sanktionen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aussenwirtschaft-zoll-sanktionen.zip)
- Testakte: [testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip)
