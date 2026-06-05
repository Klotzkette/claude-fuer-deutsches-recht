---
name: aussenwirtschaft-bafa-genehmigungen-cbam-co2
description: "Bafa Genehmigungen Cbam CO2: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bafa Genehmigungen Cbam CO2

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Bafa Genehmigungen Cbam CO2** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-bafa-genehmigungen` | BAFA-Exportgenehmigungsverfahren fuer Dual-Use-Gueter und kontrollierte Technologien: Einzelgenehmigung, Sammelgenehmigung, Globalgenehmigung und Nullbescheid nach AWG/AWV und VO (EU) 2021/821. Steuerung des Antragsverfahrens ueber ELAN-K2, Bearbeitungsfristen, Nachfragen und Widerspruchsverfahren. Output: Antrags- und Widerspruchsdokumentation. |
| `aussenwirtschaft-cbam-co2-zoll` | Carbon Border Adjustment Mechanism (CBAM): Berechnung der CO2-Abgabe auf Einfuhren kohlenstoffintensiver Waren nach VO (EU) 2023/956. Ab 2026 Pflicht zum Kauf von CBAM-Zertifikaten entsprechend eingebetteter Emissionen. Schnittpunkte mit TARIC und Zollwert. Output: CBAM-Kostenabschaetzung und Zertifikatskalkulation fuer Importplanung. |
| `aussenwirtschaft-cbam-zertifikate-kosten` | Kosten und Beschaffung von CBAM-Zertifikaten ab 2026: Berechnung der erforderlichen Zertifikatsanzahl, Kauf ueber nationales CBAM-Konto, Anrechnung auslaendischer CO2-Preise und Jahresabgabe. Risikomanagement bei schwankenden ETS-Preisen. Output: CBAM-Zertifikatsstrategie mit Kostenmodell und Beschaffungsplan. |
| `aussenwirtschaft-kommandocenter` | Steuerungsmodul fuer Mandanten mit mehreren parallelen Aussenwirtschafts-Sachverhalten: gleichzeitige Handhabung von Zoll-, Sanktions-, Exportkontroll- und AWV-Verfahren, Prioritaetensetzung, Ressourcenplanung und Eskalationsmanagement. Output: Sachverhalts-Priorisierungsmatrix und Koordinationsplan. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Bafa Genehmigungen Cbam CO2**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-bafa-genehmigungen`

**Fokus:** BAFA-Exportgenehmigungsverfahren fuer Dual-Use-Gueter und kontrollierte Technologien: Einzelgenehmigung, Sammelgenehmigung, Globalgenehmigung und Nullbescheid nach AWG/AWV und VO (EU) 2021/821. Steuerung des Antragsverfahrens ueber ELAN-K2, Bearbeitungsfristen, Nachfragen und Widerspruchsverfahren. Output: Antrags- und Widerspruchsdokumentation.

# BAFA-Genehmigungsverfahren: Einzel- Sammel- und Globalgenehmigung

## Mandantenfall

- Exporteur beantragt Einzelgenehmigung fuer Lieferung von Laseranlagen nach China; Bearbeitung laeuft seit 3 Monaten.
- Unternehmen mit laufenden Lieferbeziehungen in Laender der Partnerliste moechte auf Sammelgenehmigung umstellen.
- BAFA verweigert Genehmigung; Widerspruchsmoeglichkeit und Erfolgschancen pruefen.

## Erste Schritte

1. Genehmigungsart bestimmen: Einzel-, Sammel- oder Globalgenehmigung? Nullbescheid-Option pruefen.
2. Antrag ueber ELAN-K2 vollstaendig einreichen (EUC, technische Beschreibung, Gueterlisten-Code).
3. Bearbeitungsfristen nach AWG § 22 Abs. 1 kalkulieren; Untaetigkeitsklage bei Fristablauf pruefen.
4. BAFA-Nachfragen schnell und vollstaendig beantworten; Fristverlaengerung beantragen wenn noetig.
5. Genehmigungsauflagen im Betrieb umsetzen (Endverwender-Berichte, Wiederausfuhrverbote).
6. Widerspruch formgerecht einlegen; Begrenztheit der Ermessens-Nachpruefung beachten.

## Rechtsrahmen

- **AWG §§ 8-10, 22**: Genehmigungsverfahren und Fristen.
- **AWV §§ 8-12**: Nationale Genehmigungspflichten und Ausfuehrungsvorschriften.
- **Art. 10-13 VO (EU) 2021/821**: Einzelgenehmigung, Globalgenehmigung und AGG.
- **§ 24 VwVfG**: Untersuchungsgrundsatz im Verwaltungsverfahren.
- **§ 68 VwGO**: Widerspruchsverfahren vor Verwaltungsgericht.

## Pruef-Raster

- [ ] Antragsunterlagen vollstaendig und konsistent?
- [ ] Bearbeitungsfristen des BAFA kalkuliert und Eskalationsplan vorhanden?
- [ ] Nachfragen des BAFA vollstaendig beantwortet?
- [ ] Genehmigungsauflagen im Betrieb implementierbar?
- [ ] Widerspruch fristgerecht eingelegt (1 Monat nach Bescheid)?
- [ ] Alternative Genehmigungsform (Sammelgenehmigung) geprueft?

## Typische Fallstricke

- Keine aufschiebende Wirkung des Widerspruchs bei Versagung; Lieferung darf nicht stattfinden.
- Auflagen in der Genehmigung werden nicht vollstaendig umgesetzt; Genehmigungswiderruf droht.
- Sammelgenehmigung ist an engere Laenderliste gebunden als Einzelgenehmigung.
- BAFA-Nachfragen oft zeitkritisch; verspaetete Antwort verlaengert Verfahren signifikant.

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

Antragspaket, Nachfragen-Antwortdokumentation, Genehmigungsauflagen-Checkliste, Widerspruchsschreiben mit Begruendung.

## Quellen

- [BAFA Ausfuhrkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [VwVfG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwvfg/index.html)

## 2. `aussenwirtschaft-cbam-co2-zoll`

**Fokus:** Carbon Border Adjustment Mechanism (CBAM): Berechnung der CO2-Abgabe auf Einfuhren kohlenstoffintensiver Waren nach VO (EU) 2023/956. Ab 2026 Pflicht zum Kauf von CBAM-Zertifikaten entsprechend eingebetteter Emissionen. Schnittpunkte mit TARIC und Zollwert. Output: CBAM-Kostenabschaetzung und Zertifikatskalkulation fuer Importplanung.

# CBAM CO2-Zoll: Zertifikatspflicht und Kostenberechnung ab 2026

## Mandantenfall

- Stahlimporteur plant 2026 weiterhin grosse Mengen aus Nicht-EU-Laendern einzufuehren; CBAM-Kosten kalkulieren.
- Aluminium-Importeur fragt, ob Vorleistungsemissionen in Drittland abgezogen werden koennen.
- Elektrizitaetsimporteur aus Schweiz prueft CBAM-Relevanz nach Ende der Uebergangsphase.

## Erste Schritte

1. CBAM-pflichtige Waren nach Anhang I VO 2023/956 und KN-Code pruefen.
2. Eingebettete Emissionen je Tonne Ware ermitteln (Lieferantendaten oder Standardwerte).
3. Anzahl der erforderlichen CBAM-Zertifikate berechnen: Emissionen - angerechnetes Drittland-CO2-Preis.
4. CBAM-Zertifikatspreis (CO2-Preis EU-ETS aktuell) fuer Kostenschaetzung ansetzen.
5. CBAM-Konto als 'Declarant' beim nationalen Zustaendigkeitspunkt anlegen.
6. Jaehrliche Zertifikatsabgabepflicht nach 31. Mai des Folgejahres einplanen.

## Rechtsrahmen

- **Art. 6-7 VO (EU) 2023/956**: CBAM-Zertifikate und Jahreserklarungspflicht.
- **Art. 4-5 VO (EU) 2023/956**: Meldepflichten und Erklaerungspflichten ab 2026.
- **Richtlinie 2003/87/EG (ETS-RL)**: EU-Emissionshandelssystem als Bezugssystem.
- **UZK Art. 56**: CBAM-Abgaben als Teil des Zolltarifs.
- **Art. 9 VO (EU) 2023/956**: Befreiungen fuer Laender mit vergleichbarem CO2-Preis.

## Pruef-Raster

- [ ] Alle CBAM-pflichtigen Waren und KN-Codes korrekt ermittelt?
- [ ] Emissionsintensitaet vom Lieferanten dokumentiert?
- [ ] CBAM-Konto als Declarant eingerichtet?
- [ ] Anrechenbares Drittland-CO2-Preis ermittelt?
- [ ] Kostenabschaetzung und Budget-Planung erstellt?
- [ ] Jahrliche Abgabepflicht nach 31. Mai eingeplant?

## Typische Fallstricke

- Standardwerte koennen hoeher sein als tatsaechliche Emissionen; Lieferantendaten einholen.
- CBAM und Antidumping/Safeguards sind kumulativ anwendbar; Gesamtkosten summieren.
- Drittland-CO2-Preis muss tatsaechlich entrichtet worden sein; Scheinzahlungen nicht anerkannt.
- CBAM-Zertifikatspreis schwankt mit EU-ETS; Kalkulation regelmaessig aktualisieren.

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

CBAM-Kostenkalkulation mit Emissionsschema und Zertifikatsanzahl, Zertifikatspreis-Szenarioanalyse und Jahresplanung, Muster-Erklaerungsformular.

## Quellen

- [VO (EU) 2023/956 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R0956)
- [EU-Kommission CBAM-Info](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)
- [ETS-Richtlinie 2003/87/EG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32003L0087)
- [Zoll.de CBAM](https://www.zoll.de/DE/Fachthemen/Steuern/Einfuhrumsatzsteuer/cbam/cbam_node.html)

## 3. `aussenwirtschaft-cbam-zertifikate-kosten`

**Fokus:** Kosten und Beschaffung von CBAM-Zertifikaten ab 2026: Berechnung der erforderlichen Zertifikatsanzahl, Kauf ueber nationales CBAM-Konto, Anrechnung auslaendischer CO2-Preise und Jahresabgabe. Risikomanagement bei schwankenden ETS-Preisen. Output: CBAM-Zertifikatsstrategie mit Kostenmodell und Beschaffungsplan.

# CBAM-Zertifikate: Beschaffung, Kosten und Jahresabgabepflicht

## Mandantenfall

- CFO eines Stahlimporteurs fragt nach Kostenplanung fuer CBAM-Zertifikate ab 2026.
- Importeur hat im Drittland CO2-Abgaben fuer Produktion gezahlt; Anrechnung auf CBAM pruefen.
- Unternehmen moechte CBAM-Zertifikate vorausschauend kaufen; Preisrisiko einschaetzen.

## Erste Schritte

1. Einfuhrmenge und eingebettete Emissionen (Tonnen CO2e) fuer das Planjahr ermitteln.
2. Anrechenbare Drittland-CO2-Preise (tatsaechlich gezahlt, dokumentiert) herausrechnen.
3. Erforderliche Netto-Zertifikatsanzahl berechnen: Emissionen minus Anrechnung.
4. CBAM-Konto beim nationalen Zustaendigkeitspunkt einrichten (in DE: Zoll/BAFA).
5. Zertifikatsbeschaffungsstrategie: Einzelkauf vs. Hedging-Strategie bei ETS-Preisschwankungen.
6. Jaehrliche Abgabepflicht bis 31. Mai nach Ende des Vorjahrs einplanen.

## Rechtsrahmen

- **Art. 6-8 VO (EU) 2023/956**: CBAM-Zertifikate, Beschaffung und Abgabe.
- **Art. 9 VO (EU) 2023/956**: Anrechnung gezahlter CO2-Preise im Drittland.
- **Art. 22 VO (EU) 2023/956**: Kauf und Verkauf von CBAM-Zertifikaten.
- **Richtlinie 2003/87/EG ETS**: Bezugspreis fuer CBAM-Zertifikate.
- **Art. 26 VO (EU) 2023/956**: Strafzahlungen bei nicht abgegebenen Zertifikaten.

## Pruef-Raster

- [ ] Emissionsmenge fuer Planjahr kalkuliert?
- [ ] Anrechenbare Drittland-CO2-Preise belegt?
- [ ] CBAM-Konto eingerichtet?
- [ ] Beschaffungsstrategie fuer Zertifikate bestimmt (Spot vs. Hedging)?
- [ ] Abgabepflicht 31. Mai eingeplant?
- [ ] Strafzahlungsrisiko bei Nichtabgabe bewertet?

## Typische Fallstricke

- ETS-Preisschwankungen veraendern CBAM-Kosten drastisch; keine statische Kalkulation.
- Drittland-CO2-Preis muss tatsaechlich gezahlt worden sein; Dokumentationspflicht streng.
- Vorzeitiger Kauf von Zertifikaten hat Verfallsrisiko bei Gesetzesaenderungen.
- Nicht abgegebene Zertifikate kosten dreifachen ETS-Preis als Strafe (Art. 26 VO 2023/956).

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

CBAM-Zertifikatskostenmodell mit Szenarien, Beschaffungsplan, Anrechnungsnachweis-Dokumentation und Abgabe-Terminkalender.

## Quellen

- [VO (EU) 2023/956 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R0956)
- [EU ETS Informationsseite](https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets_en)
- [EU-Kommission CBAM-Zertifikate](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)
- [Zoll.de CBAM](https://www.zoll.de/DE/Fachthemen/Steuern/Einfuhrumsatzsteuer/cbam/cbam_node.html)

## 4. `aussenwirtschaft-kommandocenter`

**Fokus:** Steuerungsmodul fuer Mandanten mit mehreren parallelen Aussenwirtschafts-Sachverhalten: gleichzeitige Handhabung von Zoll-, Sanktions-, Exportkontroll- und AWV-Verfahren, Prioritaetensetzung, Ressourcenplanung und Eskalationsmanagement. Output: Sachverhalts-Priorisierungsmatrix und Koordinationsplan.

# Kommandocenter Aussenwirtschaft: Mehrfach-Sachverhalts-Steuerung

## Mandantenfall

- Konzern hat gleichzeitig laufende BAFA-Pruefung, Russland-Sanktionsfall, CBAM-Implementierung und AEO-Verlaengerung.
- Kanzlei betreut drei Mandanten gleichzeitig mit Zollpruefungen und einer internen Exportkontroll-Investigation.
- Compliance-Abteilung muss Jahresbericht, Neukunden-KYC-Backlog und Systemmigration gleichzeitig bewaltigen.

## Erste Schritte

1. Alle offenen Aussenwirtschafts-Sachverhalte mit Status, Fristen und Zustaendigkeit erfassen.
2. Prioritaetenbewertung: Strafrisiko, Fristen, Geldwert, Reputationsschaden.
3. Ressourcen zuordnen: externe Berater, interne Experten, IT-Kapazitaet.
4. Kritische-Pfad-Analyse fuer zeitkritische Verfahren.
5. Eskalationsprozess und Berichtslinien fuer Geschaeftsfuehrung definieren.
6. Woechentliche Statusuebersicht und Fristen-Dashboard einrichten.

## Rechtsrahmen

- **AWG § 14**: Auskunftspflichten mit Fristen gegenueber Behoerden.
- **UZK Art. 22**: Bescheidfrist bei Bewilligungsantraegen.
- **AWV § 61**: Meldefristen AWV-Zahlungsmeldungen.
- **BAFA-Verfahrensordnung**: Bearbeitungsfristen fuer Genehmigungsantraege.
- **§ 130 OWiG**: Organisationspflichtverletzung als Bussgelstatbestand.

## Pruef-Raster

- [ ] Alle offenen Sachverhalte vollstaendig erfasst?
- [ ] Fristen fuer Behoerdenverfahren identifiziert und im Kalender eingetragen?
- [ ] Prioritaetenbewertung nach Risikokategorien durchgefuehrt?
- [ ] Ressourcenzuordnung realistisch und bestaetigt?
- [ ] Eskalationsweg zur Geschaeftsfuehrung definiert?
- [ ] Statusreporting-Format und Rhythmus festgelegt?

## Typische Fallstricke

- Behordliche Fristen werden unter Last von Parallelverfahren verpasst.
- Niedrig priorisierte Sachverhalte akkumulieren sich zu Krisenfall.
- Externe Berater haben keine Gesamtsicht; Koordinationsfehler.
- BAFA- und Zollfristen laufen unabhaengig voneinander; kein zentrales Fristenmanagement.

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

Sachverhalts-Priorisierungsmatrix, Ressourcen- und Fristenplan, Eskalations-Regelwerk und Wochen-Dashboard-Vorlage.

## Quellen

- [BAFA Aussenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [Zoll.de](https://www.zoll.de/DE/Home/home_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
