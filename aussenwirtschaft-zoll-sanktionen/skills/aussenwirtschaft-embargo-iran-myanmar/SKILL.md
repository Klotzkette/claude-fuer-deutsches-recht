---
name: aussenwirtschaft-embargo-iran-myanmar
description: "Embargo Iran Myanmar: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Embargo Iran Myanmar

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Embargo Iran Myanmar** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-embargo-iran` | EU-Iran-Sanktionsregime nach VO (EU) 267/2012 (Nuklear) und VO (EU) 359/2011 (Menschenrechte): gelistete Personen, Finanzsanktionen, Guetersanktionen und Dienstleistungsverbote. Besondere Risiken im Dual-Use-Bereich und bei Oel/Gas-Sektor. Fallkonstellation: Unternehmen erhalt Anfrage aus Iran. Output: Iran-Embargo-Pruefungsvermerk mit Risikoampel. |
| `aussenwirtschaft-embargo-myanmar` | EU-Myanmar-Sanktionsregime nach VO (EU) 401/2013 und Folgeverordnungen: gelistete Personen und Entitaeten des Militaerregimes, Finanzsanktionen, Waffenembargo und sektorale Einschraenkungen. Besondere Risiken bei Handels- und Investitionsbeziehungen mit Staatsunternehmen. Output: Myanmar-Embargo-Screening und Pruefungsvermerk. |
| `aussenwirtschaft-embargo-nordkorea` | EU- und UN-Sanktionsregime gegen Nordkorea: VO (EU) 2017/1509 und UN-Resolutionen 1718/1874/2270 ff. Umfassendes Guetersanktionsregime, Waffenembargo, Finanzsanktionen und Transshipment-Risiken. Catch-All fuer Proliferationsverdacht besonders weitreichend. Output: Nordkorea-Embargo-Pruefvermerk und Transshipment-Risikoanalyse. |
| `aussenwirtschaft-embargo-russland` | EU-Russland-Sanktionsregime: VO (EU) 833/2014 (Sektoral/Gueter) und VO (EU) 269/2014 (Finanzsanktionen). Verbotene Gueter (Anhaenge VO 833/2014), No-Russia-Clause Art. 12g, Dienstleistungsverbote (Art. 5n), Umgehungsverbot. Catch-All und Red-Flags. Mandant prueft Lieferkette auf Russland-Kontamination. Output: Russland-Embargo-Pruefvermerk mit Ampel und Massnahmenplan. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Embargo Iran Myanmar**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-embargo-iran`

**Fokus:** EU-Iran-Sanktionsregime nach VO (EU) 267/2012 (Nuklear) und VO (EU) 359/2011 (Menschenrechte): gelistete Personen, Finanzsanktionen, Guetersanktionen und Dienstleistungsverbote. Besondere Risiken im Dual-Use-Bereich und bei Oel/Gas-Sektor. Fallkonstellation: Unternehmen erhalt Anfrage aus Iran. Output: Iran-Embargo-Pruefungsvermerk mit Risikoampel.

# Embargo Iran: Nukleare Sanktionen und Doppelverwendungsrisiken

## Mandantenfall

- Maschinenbauer erhalt Anfrage fuer Lieferung von Pumpen nach Iran; sektorale Verbote pruefen.
- Bank prueft Zahlung eines iranischen Unternehmens; Listentreffer nach VO 267/2012.
- Technologie-KMU fragt, ob Software-Lieferung in den Iran nach EU-Recht erlaubt ist.

## Erste Schritte

1. EU-Sanktionsliste Iran (VO 267/2012) und konsolidierte Finanzsanktionsliste pruefen.
2. Guetersanktionen-Katalog (Dual-Use, militaer, Raketentechnologie, Nuklearguter) pruefen.
3. Oel/Gas-Sektor-Embargo (Art. 8-9 VO 267/2012) bei Rohstoffbezug pruefen.
4. Catch-All fuer Gueter mit WMD/Raketenprogramm-Relevanz auswerten.
5. US-Sanktionen (OFAC Iran-Programme) als Risiko-Mitpruefung fuer USD-Zahlungen.
6. Stop-Ship und Eskalation bei Zweifeln; BAFA-Anfrage bei konkreter Unsicherheit.

## Rechtsrahmen

- **VO (EU) 267/2012**: Restriktive Massnahmen gegen Iran (Nuklear).
- **VO (EU) 359/2011**: Massnahmen wegen Verletzung der Menschenrechte Iran.
- **AWG § 18 AWG**: Strafbarkeit bei Embargo-Verstoss.
- **Art. 4 VO (EU) 2021/821**: Catch-All fuer WMD-Proliferationsverdacht.
- **AWV § 9**: Nationale Genehmigungsfreiheitsmerkmale (Abgrenzung).

## Pruef-Raster

- [ ] Partei auf EU-Sanktionsliste Iran geprueft?
- [ ] Dual-Use-Listenpruefung mit Iran-Bezug durchgefuehrt?
- [ ] Oel/Gas-Sektor-Embargo relevanz geprueft?
- [ ] WMD/Raketenprogramm-Catch-All-Risiko ausgeschlossen?
- [ ] US-Sanktionen fuer USD-Zahlungen mitgeprueft?
- [ ] Stop-Ship bei Risikoindikatoren ausgeloest?

## Typische Fallstricke

- Iran-Sanktionen sind besonders komplex wegen mehrerer EU-Verordnungen.
- Catch-All trifft oft nicht-gelistete technische Gueter mit Dual-Use-Potenzial.
- US-Extraterritorialer Sanktionsdruck auf EU-Unternehmen trotz unterschiedlichem EU-Recht.
- Scheinbar zivilwirtschaftliche Endverwender koennen Frontgesellschaften sein.

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

Iran-Embargo-Pruefungsvermerk mit Listenscan, Gueterkategorien-Analyse, Catch-All-Bewertung und Risikoampel (Gruen/Gelb/Rot).

## Quellen

- [VO (EU) 267/2012 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R0267)
- [VO (EU) 359/2011 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32011R0359)
- [EU Sanctions Map Iran](https://www.sanctionsmap.eu/#/main/details/7)
- [BAFA Embargo Iran](https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/Embargolaender/embargolaender_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 2. `aussenwirtschaft-embargo-myanmar`

**Fokus:** EU-Myanmar-Sanktionsregime nach VO (EU) 401/2013 und Folgeverordnungen: gelistete Personen und Entitaeten des Militaerregimes, Finanzsanktionen, Waffenembargo und sektorale Einschraenkungen. Besondere Risiken bei Handels- und Investitionsbeziehungen mit Staatsunternehmen. Output: Myanmar-Embargo-Screening und Pruefungsvermerk.

# Embargo Myanmar: Militaerregime-Sanktionen und Guetersperren

## Mandantenfall

- Importeur bezieht Textilwaren aus Myanmar; Verbindung zu Militaer-nahem Unternehmen pruefen.
- Bank erhalt Auftrag fuer Korrespondenz-Zahlung an burmesischen Staatskonzern.
- Maschinenproduzent erhalt Anfrage aus Myanmar fuer Lieferung von Industrie-Equipment.

## Erste Schritte

1. EU-Sanktionsliste Myanmar (VO 401/2013) und aktuelle Ergaenzungsverordnungen pruefen.
2. Militaer-Verbindung des Unternehmens pruefen (Unternehmensregister, Eigentuemerstruktur).
3. Waffenembargo und Rueustungsguter-Verbote pruefen (Anhang VO 401/2013).
4. Sektorale Einschraenkungen fuer Treibstoff, Holz, Jade und Rubine pruefen.
5. Finanzsanktionen und Bereitstellungsverbote fuer gelistete Personen pruefen.
6. Dokumentation der Pruefung und Freigabe-/Sperrempfehlung.

## Rechtsrahmen

- **VO (EU) 401/2013**: Restriktive Massnahmen gegen Myanmar.
- **Folgeverordnungen nach 2021-Coup**: Erweiterte Personenliste und sektorale Massnahmen.
- **AWG § 18**: Strafbarkeit bei Embargo-Verstoss.
- **Art. 2 VO (EU) 401/2013**: Waffenembargo und militaerische Gueter.
- **UZK Art. 56**: Zolltarifanwendung bei Embargogutern.

## Pruef-Raster

- [ ] Partei auf EU-Sanktionsliste Myanmar geprueft?
- [ ] Militaer-Eigentumsverbindung aufgeklaert?
- [ ] Waffenembargo und Ruestungsguterliste geprueft?
- [ ] Sektorale Verbote (Treibstoff, Edelsteine, Holz) relevant?
- [ ] Finanztransaktion auf Bereitstellungsverbot geprueft?
- [ ] Dokumentation vollstaendig?

## Typische Fallstricke

- Myanmar-Sanktionen wurden nach Coup 2021 massiv ausgeweitet; aeltere Prueflisten veraltet.
- Militaer haelt Anteile an zahlreichen scheinbar zivilwirtschaftlichen Unternehmen.
- Sektorale Verbote gelten auch fuer Handelsfinanzierung.

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

Myanmar-Embargo-Screening-Protokoll, Gueterkategorien-Uebersicht, Unternehmenspruefvermerk und Freigabe-/Sperrempfehlung.

## Quellen

- [VO (EU) 401/2013 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0401)
- [EU Sanctions Map Myanmar](https://www.sanctionsmap.eu/#/main/details/25)
- [BAFA Myanmar-Embargo](https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/Embargolaender/embargolaender_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 3. `aussenwirtschaft-embargo-nordkorea`

**Fokus:** EU- und UN-Sanktionsregime gegen Nordkorea: VO (EU) 2017/1509 und UN-Resolutionen 1718/1874/2270 ff. Umfassendes Guetersanktionsregime, Waffenembargo, Finanzsanktionen und Transshipment-Risiken. Catch-All fuer Proliferationsverdacht besonders weitreichend. Output: Nordkorea-Embargo-Pruefvermerk und Transshipment-Risikoanalyse.

# Embargo Nordkorea: Umfassendes Sanktionsregime und Proliferationskontrolle

## Mandantenfall

- Schifffahrtsunternehmen prueft Ladung, die moeglicherweise via Drittland an Nordkorea weitergeleitet wird.
- Exporteur von Elektronikbauteilen erhalt Order ueber Singapur-Zwischenhaendler; Endverwender unklar.
- Bank prueft Korrespondenz-Zahlung mit nordkoreanischem Bezug.

## Erste Schritte

1. EU-Sanktionsliste Nordkorea (VO 2017/1509) und UN-Konsolidierte Sanktionsliste pruefen.
2. Umfassenden Guetersanktionskatalog pruefen: kein Export von Luxusgutern, Ruestung, Dual-Use und weiteren.
3. Transshipment-Risiko bewertet: Drittland-Intermediary mit NK-Verbindung?
4. Catch-All fuer Proliferations- und WMD-Verdacht bewertet.
5. Finanzsanktionen und Zahlungsrouting-Verbot geprueft.
6. Sofortiger Stopp und Meldung falls Hinweise auf NK-Endverwendung.

## Rechtsrahmen

- **VO (EU) 2017/1509**: Restriktive Massnahmen gegen Nordkorea.
- **UN-SR-Resolutionen 1718/1874/2270/2321 ff.**: Universelle Sanktionen gegen Nordkorea.
- **AWG § 18**: Strafbarkeit.
- **Art. 4 VO (EU) 2021/821**: Catch-All Proliferationsverdacht.
- **VO (EU) 2017/1509 Art. 19**: Finanztransaktionsverbote.

## Pruef-Raster

- [ ] Partei auf EU-Sanktionsliste NK und UN-Liste geprueft?
- [ ] Guetersanktionskatalog auf Vollstaendigkeit geprueft?
- [ ] Transshipment-Risiko via Drittland untersucht?
- [ ] Catch-All fuer Proliferationsverdacht bewertet?
- [ ] Zahlungsrouting auf NK-Verbindung geprueft?
- [ ] Sofortiger Stopp bei NK-Indizien eingeleitet?

## Typische Fallstricke

- NK-Sanktionsumgehung laeuft fast immer ueber Drittlaender; nur direkte Pruefung reicht nicht.
- Catch-All fuer NK-Proliferation ist extraterritorial wirksam.
- UN-Sanktionen gehen ueber EU-Sanktionen hinaus und binden auch Nicht-EU-Tochtergesellschaften.

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

Nordkorea-Embargo-Pruefvermerk, Transshipment-Risikoanalyse, Screening-Protokoll und Eskalationsplan.

## Quellen

- [VO (EU) 2017/1509 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1509)
- [UN Nordkorea Sanctions](https://www.un.org/securitycouncil/sanctions/1718)
- [BAFA Nordkorea-Embargo](https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/Embargolaender/embargolaender_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 4. `aussenwirtschaft-embargo-russland`

**Fokus:** EU-Russland-Sanktionsregime: VO (EU) 833/2014 (Sektoral/Gueter) und VO (EU) 269/2014 (Finanzsanktionen). Verbotene Gueter (Anhaenge VO 833/2014), No-Russia-Clause Art. 12g, Dienstleistungsverbote (Art. 5n), Umgehungsverbot. Catch-All und Red-Flags. Mandant prueft Lieferkette auf Russland-Kontamination. Output: Russland-Embargo-Pruefvermerk mit Ampel und Massnahmenplan.

# Embargo Russland: Sektoralsanktionen und Umgehungsverbote

## Mandantenfall

- Maschinenhersteller hat Altvertrag mit russischem Staatsunternehmen; Lieferpflicht vs. Embargoverstoß abwaegen.
- Logistikunternehmen befodert Gueter ueber Kasachstan; No-Russia-Clause und Umgehungsrisiko pruefen.
- IT-Dienstleister fragt, ob Wartungsvertrag mit russischer Tochter weiterhin erlaubt ist.

## Erste Schritte

1. VO 833/2014 (konsolidiert) und VO 269/2014 aktuell abfragen (laufende Sanktionspakete).
2. Guetersanktionskatalog (Anh. VII, XXIII, IV, XVIII etc.) mit KN-Code des Exporteurs abgleichen.
3. No-Russia-Clause nach Art. 12g fuer Anh. XI/XX/XXXV-Gueter in Drittlandevertraegen pruefen.
4. Dienstleistungsverbote Art. 5n pruefen: IT, Rechts-, Buchhaltungs-, Steuerberatung.
5. Umgehungsindizien pruefen: Routen ueber Drittlaender, ungewoehnliche Ziellaender, Red Flags.
6. Altvertrag: Winddown-Ausnahme und Genehmigungspflicht beim BAFA pruefen.

## Rechtsrahmen

- **VO (EU) 833/2014 konsolidiert**: Sektorales Embargo und Gueterlisten.
- **VO (EU) 269/2014**: Finanzsanktionen gegen gelistete Personen.
- **Art. 12g VO 833/2014**: Pflichtklausel No-Russia-Clause.
- **Art. 5n VO 833/2014**: Dienstleistungsverbote.
- **AWG §§ 17-18**: Straf- und Bussgeldtatbestaende.

## Pruef-Raster

- [ ] Gueter auf Verbotslisten der VO 833/2014 geprueft?
- [ ] No-Russia-Clause in Drittlandevertraegen implementiert?
- [ ] Dienstleistungsvertrag auf Art. 5n-Verbot geprueft?
- [ ] Umgehungsindizien und Red Flags ausgeschlossen?
- [ ] Personenliste VO 269/2014 geprueft?
- [ ] BAFA-Genehmigung fuer Altvertrags-Winddown beantragt?

## Typische Fallstricke

- Laufende Sanktionspakete aendern Anhangslisten; nur tagesaktuelle Pruefung.
- No-Russia-Clause-Fehlen ist eigenstaendiger Verstoss; auch bei genehmigungsfreier Ware.
- Dienstleistungsverbote greifen auch bei indirekter Leistungserbringung im Konzern.
- Umgehungsverbote sind subjektiv sehr weit ausgelegt; Fahrlassigkeit reicht.

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

Russland-Embargo-Pruefvermerk mit Ampel, Gueterlisten-Screening, Vertragsklausel-Check und Massnahmenplan (Stopp/Genehmigung/Offenlegung).

## Quellen

- [VO (EU) 833/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [VO (EU) 269/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [EU Sanctions Map Russland](https://www.sanctionsmap.eu/#/main/details/36)
- [BAFA Russland-Embargo](https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/Embargolaender/embargolaender_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
