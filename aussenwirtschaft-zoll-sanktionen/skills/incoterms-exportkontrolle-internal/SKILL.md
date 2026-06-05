---
name: incoterms-exportkontrolle-internal
description: "Incoterms Exportkontrolle Internal: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Incoterms Exportkontrolle Internal

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Incoterms Exportkontrolle Internal** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-incoterms-exportkontrolle` | Schnittstelle zwischen Incoterms 2020 und Exportkontrollverantwortung: Bestimmung des Ausfuehrers bei EXW (Abholklausel), Pflichtenuebertragung und Haftungsluecken bei DDP, Verantwortung fuer Ausfuhranmeldung und Exportkontroll-Compliance je Klausel. Output: Incoterms-Exportkontroll-Matrix und Vertragsempfehlung. |
| `aussenwirtschaft-internal-investigation-aussenwirtschaft` | Interne Ermittlung bei Verdacht auf Verstoss gegen Exportkontroll- oder Sanktionsrecht: Sicherung digitaler und physischer Beweise (Legal Hold), Mitarbeiterbefragungen, Compliance-Bericht, Schadensquantifizierung und Weichenstellung fuer freiwillige Offenlegung oder Verteidigung. Output: Investigation-Protokoll und Abschlussberichtsgliederung. |
| `aussenwirtschaft-investitionspruefung-bmwk` | Investitionspruefung durch das BMWK nach AWG §§ 55 ff. und AWV §§ 55 ff.: sektorspezifische Pruefung (KRITIS) und allgemeine Pruefung, Anteilsschwellen (10/20/25 Prozent), Vollzugsverbot, Freigabe und Untersagung. Drittstaatsinvestoren und inlaendische Erwerber. Output: Anmeldeformular und M&A-Pruefcheckliste. |
| `aussenwirtschaft-know-your-customer-exportkontrolle` | KYC-Prozess fuer Exportkontrollzwecke: Kundenidentifizierung, Endverwender-Screening, UBO-Ermittlung nach VO (EU) 2021/821 und BAFA-Anforderungen, Red-Flag-Analyse bei verdaechtigen Bestellmuster und Sanktionslistenabgleich. Output: KYC-Kundenprofil und Freigabe-/Sperrentscheidung. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Incoterms Exportkontrolle Internal**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-incoterms-exportkontrolle`

**Fokus:** Schnittstelle zwischen Incoterms 2020 und Exportkontrollverantwortung: Bestimmung des Ausfuehrers bei EXW (Abholklausel), Pflichtenuebertragung und Haftungsluecken bei DDP, Verantwortung fuer Ausfuhranmeldung und Exportkontroll-Compliance je Klausel. Output: Incoterms-Exportkontroll-Matrix und Vertragsempfehlung.

# Incoterms und Exportkontrolle: Verantwortung und Haftungsluecken

## Mandantenfall

- Verkauf EXW ab Werk: Auslaendischer Kaeufer holt Ware ab; Dual-Use-Exportkontrolle beim Verkaeufer oder Kaeufer?
- DDP-Lieferung nach USA: deutsches Unternehmen als Importeur-of-Record; ITAR-Exponierung.
- CFR-Lieferung nach Russland: Frachtfuehrer bucht Umweg ueber Tuerkei; Verantwortungsabgrenzung.

## Erste Schritte

1. Incoterms-Klausel im Vertrag identifizieren und exportkontrollrechtliche Implikation analysieren.
2. Ausfuehrer nach UZK bestimmen: Wer ist Eigentuemer zum Ausfuhrmoment?
3. EXW: Klarstellen ob EXW-Verkaeufer dennoch Exportkontrollpruefung durchfuehren muss.
4. DDP: US-ITAR/EAR-Importeur-of-Record-Funktion und Sanktionsrisiko bewerten.
5. Genehmigungspflicht dem Ausfuehrer zuordnen; Vertragsklausel anpassen wenn noetig.
6. Incoterms-Exportkontroll-Matrix erstellen fuer das eigene Produktportfolio.

## Rechtsrahmen

- **UZK Art. 1 Nr. 19, DA Art. 1 Nr. 18**: Ausfuehrer-Definition.
- **AWV § 2**: Ausfuehrer und seine Pflichten.
- **§ 18 AWG**: Strafbarkeit des Ausfuehrers unabhaengig von Incoterms-Klausel.
- **US EAR 15 CFR Part 758.3**: US-Ausfuehrer-Definition (unabhaengig von Incoterms).
- **VO (EU) 2021/821 Art. 2 Nr. 3**: Ausfuehrender im Sinne der Dual-Use-Verordnung.

## Pruef-Raster

- [ ] Incoterms-Klausel und Eigentuemeruebergang im Vertrag bestimmt?
- [ ] Ausfuehrer nach UZK und AWV unabhaengig von Incoterms ermittelt?
- [ ] EXW: Vereinbarung mit auslaendischem Kaeufer ueber Exportkontrollverantwortung?
- [ ] DDP: US-ITAR/EAR-Pflichten und Importeur-of-Record-Risiko geprueft?
- [ ] Genehmigungsinhaber und Ausfuehrer konsistent?
- [ ] Vertragsklausel an Exportkontrollverantwortung angepasst?

## Typische Fallstricke

- EXW entbindet Verkaeufer nicht von Exportkontrollpruefung wenn er weiss, wohin Ware geht.
- DDP nach USA macht deutschen Lieferanten zum US-Importer-of-Record mit ITAR-Pflichten.
- Incoterms regeln nur Kostenuebergang, nicht Exportkontrollverantwortung.
- Subunternehmer-Spediteur bei FOB/CFR kann eigene Exportkontrollpruefung nicht uebernehmen.

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

Incoterms-Exportkontroll-Matrix mit Verantwortungszuordnung je Klausel, Vertragsklausel-Empfehlungen und Haftungsluecken-Analyse.

## Quellen

- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA Ausfuhrkontrolle allgemein](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)

## 2. `aussenwirtschaft-internal-investigation-aussenwirtschaft`

**Fokus:** Interne Ermittlung bei Verdacht auf Verstoss gegen Exportkontroll- oder Sanktionsrecht: Sicherung digitaler und physischer Beweise (Legal Hold), Mitarbeiterbefragungen, Compliance-Bericht, Schadensquantifizierung und Weichenstellung fuer freiwillige Offenlegung oder Verteidigung. Output: Investigation-Protokoll und Abschlussberichtsgliederung.

# Interne Ermittlung bei Exportkontroll- und Sanktionsverstoss

## Mandantenfall

- Hinweisgeber meldet, dass Exportabteilung systematisch falsche HS-Codes zur Umgehung von Genehmigungspflichten verwendet.
- Zollpruefung deckt auf, dass drei Sendungen ohne BAFA-Genehmigung exportiert wurden; Umfang unklar.
- Banktransfer an russische Gegenpartei; Compliance identifiziert Sanktionspotenzial erst nach Ausfuehrung.

## Erste Schritte

1. Legal Hold sofort einrichten: E-Mails, ATLAS-Daten, ERP-Exportdaten, interne Kommunikation sichern.
2. Untersuchungsauftrag und Untersuchungsrahmen durch Geschaeftsfuehrung oder Aufsichtsrat freigeben.
3. Untersuchungsteam zusammenstellen: externer Rechtsanwalt, interner Compliance, IT-Forensik.
4. Sachverhaltserstellung durch strukturierte Befragungen und Dokumentenanalyse.
5. Schadensquantifizierung: Anzahl Verstoesse, Zeitraum, beteiligte Personen, betroffene Gueter und Werte.
6. Abschlussbericht mit Empfehlung: freiwillige Offenlegung, Verteidigung oder beides.

## Rechtsrahmen

- **§ 22 Abs. 4 AWG**: Strafmilderung bei freiwilliger Offenlegung.
- **§ 130 OWiG**: Aufsichtspflichtverletzung, Unternehmensgeldbuse.
- **§ 97 StPO**: Beschlagnahmefreiheit anwaltlicher Unterlagen.
- **§ 14 AWG**: Auskunftspflichten gegenueber Behoerden.
- **DSGVO Art. 6**: Rechtsgrundlage fuer Mitarbeiterdatenzugriff bei Investigation.

## Pruef-Raster

- [ ] Legal Hold umfasst alle relevanten Datenkategorien?
- [ ] Untersuchungsauftrag schriftlich erteilt und Rahmen definiert?
- [ ] Rechtsanwaltsprivileg fuer Investigation-Unterlagen sichergestellt?
- [ ] Mitarbeiterbefragungen mit Belehrungsprotokoll durchgefuehrt?
- [ ] Datenschutzrechtliche Grundlage fuer Datenzugriff geprueft?
- [ ] Schadensquantifizierung vollstaendig und belegbar?
- [ ] Abschlussbericht mit konkreter Empfehlung versehen?

## Typische Fallstricke

- Legal Hold zu spaet eingeleitet; Beweise ueberschrieben oder Datenschutzloeschfristen abgelaufen.
- Interne Mitarbeiter untersuchen sich selbst; Interessenkonflikt.
- Investigation-Berichte ohne Anwaltsprivileg koennen von Behoerden beschlagnahmt werden.
- Mitarbeiter ohne Belehrung ueber Aussageverweigerungsrecht befragt; spaetere Verwertungsprobleme.

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

Legal-Hold-Anordnung, Investigation-Protokoll mit Befragungsprotokollen, Schadenstabelle, Abschlussbericht-Gliederung und Empfehlung freiwillige Offenlegung oder Verteidigung.

## Quellen

- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [OWiG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig_1968/index.html)
- [BAFA Exportkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
- [Zoll.de Zollrecht](https://www.zoll.de/DE/Fachthemen/Zoelle/zoll_node.html)

## 3. `aussenwirtschaft-investitionspruefung-bmwk`

**Fokus:** Investitionspruefung durch das BMWK nach AWG §§ 55 ff. und AWV §§ 55 ff.: sektorspezifische Pruefung (KRITIS) und allgemeine Pruefung, Anteilsschwellen (10/20/25 Prozent), Vollzugsverbot, Freigabe und Untersagung. Drittstaatsinvestoren und inlaendische Erwerber. Output: Anmeldeformular und M&A-Pruefcheckliste.

# Investitionspruefung BMWK: AWG-Verfahren bei auslaendischen Unternehmenserwerben

## Mandantenfall

- Chinesischer Investor erwirbt 20 Prozent an deutschem Sicherheitstechnikunternehmen; Anmeldepflicht geprueft.
- US-Private-Equity uebernimmt deutschen Hersteller von Halbleitern; sektorspezifische Pruefung.
- Arabischer Staatsfonds kauft 15 Prozent an Energieversorger; KRITIS-Pruefung eingeleitet.

## Erste Schritte

1. Erwerber und Zielunternehmen identifizieren; Drittstaatsbezug und Branche feststellen.
2. Sektor des Zielunternehmens einordnen: KRITIS (Anhang A AWV) oder allgemeiner Sektor (Anhang B AWV).
3. Anteilsschwelle pruefen: 10 % (KRITIS/kritische Technologien), 20 %, 25 %.
4. Anmeldepflicht oder freiwillige Anmeldung bestimmen; Vollzugsverbot beachten.
5. Antrag beim BMWK-Referat 533 stellen; erforderliche Unterlagen zusammenstellen.
6. Verfahrenszeitplan planen (3 Monate Pruefung, Verlaengerung moeglich).

## Rechtsrahmen

- **AWG §§ 55-59**: Pruefungsgrundlage, Anmelde- und Genehmigungspflicht.
- **AWV §§ 55-62**: Sektorspezifische und allgemeine Pruefverfahren, Anteilsschwellen.
- **AWV Anhang A**: KRITIS-Sektoren mit 10-%-Schwelle.
- **AWV Anhang B**: Weitere Sektoren mit 20-%-Schwelle (u.a. kuenstliche Intelligenz, Halbleiter).
- **§ 18 AWG**: Sanktionen bei Vollzug ohne Freigabe.

## Pruef-Raster

- [ ] Erwerber aus Drittstaat (Nicht-EU/EFTA/NATO)?
- [ ] Sektor des Zielunternehmens in Anhang A oder B AWV?
- [ ] Anteilsschwelle ueberschritten oder wird ueberschritten?
- [ ] Vollzugsverbot beachtet; kein Closing vor Freigabe?
- [ ] Alle erforderlichen Unterlagen fuer BMWK-Anmeldung vollstaendig?
- [ ] Verfahrenszeitplan in M&A-Zeitplan integriert?

## Typische Fallstricke

- Vollzugsverbot gilt ab Anmeldepflicht; Closing vor Freigabe ist bussgeldbewehrt.
- Intrakonzernuebertragungen koennen Pruefpflicht ausloesen wenn Letzteigentuemer wechselt.
- Berechnung Anteilsschwelle muss alle Stimmrechte und wirtschaftliche Einflussmoeglichkeiten einschliessen.
- BMWK-Pruefverfahren kann laenger als 3 Monate dauern; Verlaengerungen moeglich.

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

BMWK-Anmeldeformular, M&A-Pruefcheckliste fuer Investitionspruefung, Risikoklassifizierung Zielunternehmen und Zeitplan-Empfehlung.

## Quellen

- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [BMWK Investitionspruefung](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/investitionspruefung.html)
- [EUR-Lex VO (EU) 2019/452 Screening-Verordnung](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)

## 4. `aussenwirtschaft-know-your-customer-exportkontrolle`

**Fokus:** KYC-Prozess fuer Exportkontrollzwecke: Kundenidentifizierung, Endverwender-Screening, UBO-Ermittlung nach VO (EU) 2021/821 und BAFA-Anforderungen, Red-Flag-Analyse bei verdaechtigen Bestellmuster und Sanktionslistenabgleich. Output: KYC-Kundenprofil und Freigabe-/Sperrentscheidung.

# Know Your Customer im Exportkontrollkontext: Kundenscreening und Endverwenderidentifizierung

## Mandantenfall

- Neuer Kunde aus UAE bestellt Hochfrequenzelektronik; ungewoehnlich hohe Bestellmenge, Endverwendung unklar.
- Vertrieb hat Stammkunden in Tuerkei; Umgehungsroute nach Russland aus Presseberichten bekannt.
- Forschungspartner in China ist staatliche Universitaet mit militaerischen Verbindungen.

## Erste Schritte

1. Kundenidentitaet vollstaendig verifizieren: Firmenname, Handelsregisternummer, Adresse, UBO.
2. Sanktionslistenscreening aller Parteien und verbundener Unternehmen.
3. Red-Flag-Analyse: Bestellmuster, Mengen, Verwendungszweck, Zahlungsmodalitaeten.
4. Endverwender-Erklaerung oder EUC anfordern und auf Plausibilitaet pruefen.
5. Offene Quellen recherchieren: BAFA-Informationen, US-Denied-Persons-List, Presseberichte.
6. KYC-Kundenprofil erstellen und Entscheidung mit Beleglage dokumentieren.

## Rechtsrahmen

- **Art. 4 VO (EU) 2021/821**: Catch-All bei Kenntnislagen bezueglich militaerischer Endverwendung.
- **BAFA-Merkblatt Red Flags**: Anzeichen fuer Umgehungsversuche.
- **§ 18 AWG**: Strafbarkeit auch bei leichtfertiger Unkenntnis von Risiken.
- **§ 10 GwG**: KYC-Pflichten (gleichzeitig relevant fuer Sanktions-Compliance).
- **VO (EU) 269/2014 Art. 2**: Bereitstellungsverbot fuer gelistete Personen.

## Pruef-Raster

- [ ] Kundenidentitaet vollstaendig und verifiziert?
- [ ] UBO ermittelt und gegen Sanktionslisten geprueft?
- [ ] Red-Flag-Checkliste vollstaendig abgearbeitet?
- [ ] Endverwender-Erklaerung plausibel und konkret?
- [ ] Offene Quellen (Denied Parties, Presse) konsultiert?
- [ ] KYC-Entscheidung mit Datumsstempel und Verantwortlichem dokumentiert?

## Typische Fallstricke

- Stammkunden werden seltener neu gescreent; Situation kann sich aendern.
- Red Flags einzeln unbedenklich, zusammen signifikant (Gesamtbild).
- UAE, Tuerkei, Armenien als bekannte Umgehungslaender erfordern erhoehte Sorgfalt.
- EUC-Formulierung 'Eigenbedarf' ohne Angabe des konkreten Verwendungszwecks ist unzureichend.

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

KYC-Kundenprofil mit UBO-Kette, Red-Flag-Protokoll, Sanktionsscreening-Ergebnis, Endverwender-Bewertung und Freigabe-/Sperrentscheidung.

## Quellen

- [BAFA Red-Flags-Merkblatt](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
