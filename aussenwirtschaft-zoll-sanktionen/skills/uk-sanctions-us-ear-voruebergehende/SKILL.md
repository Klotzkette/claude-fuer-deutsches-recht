---
name: uk-sanctions-us-ear-voruebergehende
description: "UK Sanctions US EAR Voruebergehende: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# UK Sanctions US EAR Voruebergehende

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **UK Sanctions US EAR Voruebergehende** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-uk-sanctions-touchpoint` | UK-Sanktionsrecht als Touchpoint im EU-Exportkontrollmandat: SAMLA 2018 OFSI-Richtlinien und UK-Konsolidierte-Sanktionsliste nach Brexit. Vergleich mit EU-Sanktionen bei Transaktionen ueber UK-Tochtergesellschaften oder UK-Banken. Output: UK-EU-Sanktionsvergleich und Handlungsempfehlung fuer Transaktionen mit UK-Bezug. |
| `aussenwirtschaft-us-ear-itar` | US-Exportkontrolle als Touchpoint im deutschen Mandat: EAR (Export Administration Regulations 15 CFR Parts 730-774) ITAR (22 CFR Parts 120-130) und ECCN-Klassifizierung. De-minimis-Regel und Foreign-Direct-Product-Rule als Risiken fuer EU-Reexporte. Output: US-Touchpoint-Vermerk und Abgrenzung zu EU-Dual-Use-Kontrollen. |
| `aussenwirtschaft-voruebergehende-verwendung-ata-carnet` | Voruebergehende Verwendung nach UZK Art. 250 ff. und ATA-Carnet nach Istanbul-Konvention: Messe- und Ausstellungsgueter Berufsausruestung Transportmittel und Ersatzteile. Beantragung beim Hauptzollamt Buergschaftspflichten und Riedereinf uehrungspflicht. Risiken bei Nichtrueckfuehr und Zollschuldentstehung. Output: ATA-Carnet-Antragsmappe und Verwendungsnachweis. |
| `aussenwirtschaft-vub-einfuhr-ausfuhr` | Verbote und Beschraenkungen (VuB) bei der Ein- und Ausfuhr: Ueberwachungsmassnahmen bei CITES-Waren Drogenvorstufen Kulturgut Lebensmitteln und anderen regulierten Waren. Schnittstelle ATLAS-VuB-Meldung und Koordination mit spezialzustaendigen Behoerden (BZSt BAFA BLE BfR). Output: VuB-Pruefprotokoll und Behoerdenkoordinationsplan. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **UK Sanctions US EAR Voruebergehende**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-uk-sanctions-touchpoint`

**Fokus:** UK-Sanktionsrecht als Touchpoint im EU-Exportkontrollmandat: SAMLA 2018 OFSI-Richtlinien und UK-Konsolidierte-Sanktionsliste nach Brexit. Vergleich mit EU-Sanktionen bei Transaktionen ueber UK-Tochtergesellschaften oder UK-Banken. Output: UK-EU-Sanktionsvergleich und Handlungsempfehlung fuer Transaktionen mit UK-Bezug.

# UK-Sanktionen als Touchpoint: SAMLA und OFSI nach Brexit

## Mandantenfall

- Deutsches Unternehmen hat UK-Tochter; Transaktion unter EU-Sanktionen erlaubt aber OFSI-Lizenz noetig?
- Zahlung soll ueber britische Barclays-Korrespondenzbank laufen; UK-OFSI-Liste pruefen.
- UK-Tochter fragt ob sie nach Brexit weiter mit sanktionierter Person handeln darf wenn EU-Lizenz vorliegt.

## Erste Schritte

1. Relevanz UK-Recht pruefen: UK-Entitaet UK-Bank oder UK-Buerger beteiligt?
2. UK-Konsolidierte-Sanktionsliste (OFSI) abrufen und mit EU-Konsolidierter-Liste abgleichen.
3. Divergenzen dokumentieren: Personen nur in EU oder nur in UK gelistet.
4. OFSI-Lizenzmechanismus pruefen falls Transaktion benoetigt wird.
5. SAMLA 2018 Strafandrohungen und OFSI-Enforcement-Praxis bewerten.
6. Koordination zwischen EU- und UK-Compliance des Konzerns sicherstellen.

## Rechtsrahmen

- **Sanctions and Anti-Money Laundering Act (SAMLA) 2018 (UK)**: Ermaechtigunsgrundlage fuer UK-Sanktionen.
- **OFSI (Office of Financial Sanctions Implementation)**: UK-Behoerde fuer Finanzsanktionsvollzug.
- **UK Consolidated Sanctions List**: Massgebliche UK-Sanktionsliste nach Brexit.
- **VO (EU) 833/2014**: EU-Referenz fuer Divergenzanalyse.
- **AWG § 1**: Territorialer Anwendungsbereich des deutschen Rechts bei UK-Transaktionen.

## Pruef-Raster

- [ ] UK-Entitaet oder UK-Bank in Transaktion involviert?
- [ ] UK-Konsolidierte-Sanktionsliste aktuell abgerufen und abgeglichen?
- [ ] Divergenzen EU-UK-Liste identifiziert und bewertet?
- [ ] OFSI-Lizenz-Option geprueft falls Transaktion benoetigt wird?
- [ ] Konzernkoordination UK-Compliance sichergestellt?

## Typische Fallstricke

- UK folgt EU-Sanktionen nach Brexit nicht automatisch; zeitliche Divergenzen moeglich.
- OFSI-Enforcement ist aktiv und verhängt Geldstrafen unabhaengig von EU-Entscheidungen.
- SAMLA ermoeglicht UK eigene Sanktionsregimes unabhaengig von EU.
- UK-Tochter unterliegt SAMLA; EU-Genehmigung entbindet nicht von OFSI-Pflichten.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

UK-EU-Sanktionsvergleich mit Divergenz-Tabelle, OFSI-Lizenz-Bewertung und Koordinationsprotokoll fuer Konzern-Compliance.

## Quellen

- [OFSI UK Sanktionen](https://www.gov.uk/government/organisations/office-of-financial-sanctions-implementation)
- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 2. `aussenwirtschaft-us-ear-itar`

**Fokus:** US-Exportkontrolle als Touchpoint im deutschen Mandat: EAR (Export Administration Regulations 15 CFR Parts 730-774) ITAR (22 CFR Parts 120-130) und ECCN-Klassifizierung. De-minimis-Regel und Foreign-Direct-Product-Rule als Risiken fuer EU-Reexporte. Output: US-Touchpoint-Vermerk und Abgrenzung zu EU-Dual-Use-Kontrollen.

# US-Exportkontrolle EAR und ITAR als Touchpoint im EU-Mandat

## Mandantenfall

- EU-Unternehmen reexportiert Software mit US-Komponenten in Drittland; de-minimis-Pruefung noetig.
- Ruestungsunternehmen erhalt ITAR-kontrollierte Technologie von US-Partner; Weitergabe an EU-Partner erlaubt?
- Europaeischer Halbleiterhersteller nutzt US-Produktionsanlagen; Foreign-Direct-Product-Rule greift.

## Erste Schritte

1. US-Ursprungsanteil des Produkts bestimmen: Technologie Software Ausruestung US-Herkunft?
2. De-minimis-Schwelle pruefen (10 Prozent fuer CCL-Waren; 0 Prozent fuer Russland/China Militaer).
3. Foreign-Direct-Product-Rule (FDPR) auf Relevanz pruefen bei US-Produktionsausruestung.
4. ITAR-Anwendbarkeit pruefen: US-Ruestungsgueter nach USML; Reexport-Genehmigung noetig?
5. ECCN-Klassifizierung des Produkts anhand CCL (Commerce Control List) pruefen.
6. US-Touchpoint-Vermerk erstellen und klar als US-Risikomarker kennzeichnen.

## Rechtsrahmen

- **EAR 15 CFR Part 730-774**: US-Exportkontrolle fuer Dual-Use-Gueter.
- **ITAR 22 CFR Parts 120-130**: US-Ruestungsguterkontrolle fuer USML-Produkte.
- **EAR Part 734.4**: De-minimis-Schwellen fuer US-Ursprungsanteile.
- **EAR Part 734.9**: Foreign-Direct-Product-Rule bei US-Technologieeinsatz.
- **AWG § 1**: Abgrenzung des deutschen Rechts zu US-extraterritorialen Regelungen.

## Pruef-Raster

- [ ] US-Ursprungsanteil quantifiziert?
- [ ] De-minimis-Schwelle berechnet und dokumentiert?
- [ ] Foreign-Direct-Product-Rule auf Relevanz geprueft?
- [ ] ITAR-Anwendbarkeit fuer militaerische Produkte geprueft?
- [ ] ECCN-Klassifizierung anhand CCL durchgefuehrt?
- [ ] US-Touchpoint-Vermerk als Risikomarker im Mandat gesetzt?

## Typische Fallstricke

- FDPR greift auch bei EU-Produkten die mit US-Ausruestung hergestellt wurden.
- De-minimis gilt nicht bei Gutern fuer Russland China Militaer; 0-Prozent-Schwelle beachten.
- ITAR verbietet jede Weitergabe ohne spezifische US-Genehmigung; kein EU-Pendant akzeptabel.
- US-Re-Export-Controls koennen EU-Sanktionsausnahmen unterlaufen.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

US-Touchpoint-Vermerk mit ECCN de-minimis-Kalkulation FDPR-Bewertung und klarer Abgrenzung zwischen EU-Genehmigung und US-Re-Export-Pflichten.

## Quellen

- [BIS Export Administration Regulations](https://www.bis.doc.gov/index.php/regulations/export-administration-regulations-ear)
- [DDTC ITAR](https://www.pmddtc.state.gov/ddtc_public/ddtc_public?id=ddtc_public_portal_itar_landing)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA Dual-Use](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)

## 3. `aussenwirtschaft-voruebergehende-verwendung-ata-carnet`

**Fokus:** Voruebergehende Verwendung nach UZK Art. 250 ff. und ATA-Carnet nach Istanbul-Konvention: Messe- und Ausstellungsgueter Berufsausruestung Transportmittel und Ersatzteile. Beantragung beim Hauptzollamt Buergschaftspflichten und Riedereinf uehrungspflicht. Risiken bei Nichtrueckfuehr und Zollschuldentstehung. Output: ATA-Carnet-Antragsmappe und Verwendungsnachweis.

# Voruebergehende Verwendung und ATA-Carnet: Messeware und Berufsausruestung

## Mandantenfall

- Messebauer transportiert Ausstellungsexponate nach Dubai; ATA-Carnet fuer Nicht-EU-Land beantragen.
- Filmproduktion nimmt Kameraausruestung zum Drehen nach Kanada mit; ATA-Carnet Berufsausruestung.
- Maschinenexporteur bringt Demonstrationsgeraet nach Japan; Zollabruf und Wiedereinf uehrung.

## Erste Schritte

1. Bestimmungsland pruefen: ATA-Carnet-Partnerland (WCO-Mitglied) oder EU-Bewilligung voruebergehende Verwendung?
2. Warenart pruefen: Messeware Berufsausruestung Transportmittel oder Ersatzteile?
3. ATA-Carnet bei zustaendiger Handelskammer (IHK) beantragen; Buergschaftshoehe kalkulieren.
4. Carnet vollstaendig ausfuellen; Warenliste mit HS-Codes Werten und Seriennummern.
5. Ausreise: Carnet bei Abgangszollstelle abstempeln lassen.
6. Wiedereinf uehrung innerhalb der Gueltigkeitsdauer; Gegenzeichnung bei Rieder eintrittszollstelle.

## Rechtsrahmen

- **UZK Art. 250-262**: Voruebergehende Verwendung als EU-Zollverfahren.
- **Istanbul-Konvention (1990)**: Voelkerrechtliche Grundlage fuer ATA-Carnet-System.
- **UZK-DA Art. 322 ff.**: Voraussetzungen fuer Bewilligung voruebergehende Verwendung.
- **UZK Art. 79**: Zollschuldentstehung bei Nichtrueckfuehr.
- **ATA-Convention Annex B.2 (Messe)**: Spezifische Regeln fuer Ausstellungsgueter.

## Pruef-Raster

- [ ] Bestimmungsland ist ATA-Carnet-Partnerland?
- [ ] Warenart unter ATA-Carnet-Anwendung?
- [ ] Carnet vollstaendig und mit korrekten Warenbeschreibungen ausgefuellt?
- [ ] Buergschaft gueltig und ausreichend?
- [ ] Abgangszollstelle hat Carnet korrekt abgestempelt?
- [ ] Rueckfuehrungsfrist eingehalten und Gegenzeichnung erhalten?

## Typische Fallstricke

- Rueckfuehrungsfrist versaeumt: Zollschuldentstehung und IHK haftet aus Buergschaft.
- Warenveraenderung im Ausland (Reparatur) fuehrt zu Statusverlust voruebergehende Verwendung.
- ATA-Carnet gilt nicht in der EU selbst; dort gelten EU-Zollverfahren.
- Verlust des Carnets im Ausland: Notfallverfahren ueber IHK und WCO.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

ATA-Carnet-Antragsmappe mit Warenliste, Buergschaftsberechnung, Ausfuhr-/Einf uehrer-Abstempelungsanleitung und Wiedereinf uehrungsnachweis.

## Quellen

- [UZK Art. 250 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Voruebergehende Verwendung](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollverfahren-allgemein/Besondere-Verfahren/Voruebergehende-Verwendung/voruebergehende-verwendung_node.html)
- [DIHK ATA-Carnet](https://www.dihk.de/de/themen-und-positionen/internationales/zoll/ata-carnet)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)

## 4. `aussenwirtschaft-vub-einfuhr-ausfuhr`

**Fokus:** Verbote und Beschraenkungen (VuB) bei der Ein- und Ausfuhr: Ueberwachungsmassnahmen bei CITES-Waren Drogenvorstufen Kulturgut Lebensmitteln und anderen regulierten Waren. Schnittstelle ATLAS-VuB-Meldung und Koordination mit spezialzustaendigen Behoerden (BZSt BAFA BLE BfR). Output: VuB-Pruefprotokoll und Behoerdenkoordinationsplan.

# Verbote und Beschraenkungen (VuB) bei Ein- und Ausfuhr: Behoerdenkoordination

## Mandantenfall

- Importeur von Gewuerzen erhalt VuB-Sperrung in ATLAS; BLE-Genehmigung fehlt.
- Exporteur von Antiquitaeten benötigt Kulturgut-Ausfuhrgenehmigung vor ATLAS-Abfertigung.
- Pharmazeutischer Importeur muss Genehmigung nach BtMG und BAFA-Erfordernis koordinieren.

## Erste Schritte

1. Warenklassifizierung: HS-/KN-Code und TARIC auf VuB-Eintraege pruefen.
2. Relevante Behoerde identifizieren: BLE (Lebensmittel) BZSt (Drogen) BAFA (Dual-Use/Embargo) BMUV (Umwelt) Kulturbehoerde.
3. Genehmigung/Lizenz bei zustaendiger Behoerde vor Zollanmeldung beantragen.
4. ATLAS-Zollanmeldung: VuB-Code eintragen und Dokument-Referenz hinterlegen.
5. Begleitdokumentation (CITES-Zertifikat BLE-Genehmigung etc.) bei Abfertigung vorlegen.
6. Abfertigungszeitraum kalkulieren: VuB-Pruefungen verlaengern Zollabfertigung.

## Rechtsrahmen

- **UZK Art. 134**: Nichtpraefer enzielle Ursprungsregeln und Verbote.
- **VO (EG) 338/97 (CITES-VO)**: Artenschutzregelungen beim Im-/Export.
- **EG-Drogenvorstufen-VO 111/2005**: Einfuhrgenehmigungen fuer Praekursoren.
- **§§ 1-5 KultSchG**: Kulturgutschutz bei Ausfuhr.
- **BtMG §§ 3 ff.**: Betaeubungsmittelrecht bei Im- und Export.

## Pruef-Raster

- [ ] TARIC auf VuB-Eintraege fuer HS-Code geprueft?
- [ ] Zustaendige Behoerde korrekt identifiziert?
- [ ] Genehmigung/Lizenz vor Zollanmeldung beantragt und erhalten?
- [ ] VuB-Code und Dokument-Referenz in ATLAS-Anmeldung eingetragen?
- [ ] Begleitdokumentation vollstaendig bei Abfertigung vorhanden?
- [ ] Zeitpuffer fuer VuB-Pruefung in Lieferplanung beruecksichtigt?

## Typische Fallstricke

- VuB-Genehmigung nach Zollanmeldung nicht mehr moeglich; Vorab-Beantragung Pflicht.
- TARIC-VuB-Eintraege werden regelmaessig aktualisiert; Check vor jeder Sendung noetig.
- Multiples VuB mehrerer Behoerden bei ein und derselben Ware moeglich.
- Zeitverzug bei Behoerden-Genehmigungen kann Lieferketten erheblich stoeren.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

VuB-Pruefprotokoll mit Behoerdenidentifikation, Genehmigungs-Checkliste, ATLAS-Eintragungsanleitung und Lieferketten-Zeitplanung.

## Quellen

- [Zoll.de TARIC-Datenbank](https://www.zoll.de/DE/Fachthemen/Zoelle/Zolltarif/Taric/taric_node.html)
- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [BAFA Ausfuhrkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
