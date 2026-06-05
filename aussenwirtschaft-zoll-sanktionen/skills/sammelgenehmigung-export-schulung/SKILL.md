---
name: sammelgenehmigung-export-schulung
description: "Sammelgenehmigung Export Schulung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sammelgenehmigung Export Schulung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Sammelgenehmigung Export Schulung** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-sammelgenehmigung-export` | Globale und Sammelausfuhrgenehmigungen bei BAFA: Allgemeine Ausfuhrgenehmigungen EU001-EU008, nationale AGG, globale Einzelgenehmigungen; Voraussetzungen ICP, Berichtspflichten und Ablauf des Antragsverfahrens ueber ELAN-K2. Output: Sammelgenehmigungsantrag und Nutzungsprotokoll. |
| `aussenwirtschaft-schulung-exportkontrolle-rollout` | Konzeption und Durchfuehrung von Exportkontroll-Schulungen nach BAFA-ICP-Anforderungen: Zielgruppen (Vertrieb, Einkauf, Logistik, IT), Schulungsinhalte, Nachweisdokumentation, E-Learning vs. Praesenz, jaehrliche Wiederholung. Output: Schulungskonzept und Nachweisprotokoll. |
| `aussenwirtschaft-schutzmassnahmen-safeguards` | EU-Schutzmassnahmen (Safeguards) nach VO (EU) 2015/478 Art. 16 und VO (EU) 2015/755 Art. 13: Mengenbeschraenkungen Ueberwachungsmassnahmen und Antragstellung bei der EU-Kommission. Wirkung auf Importeure und Exporteure in betroffenen Sektoren (Stahl Solar Keramik). Abgrenzung zu Antidumping-Zoellen. Output: Safeguard-Pruefvermerk und Reaktionsplan. |
| `aussenwirtschaft-screening-tool-validierung` | Validierung und Qualitaetssicherung von Sanktionsscreening-Tools: Testfall-Design fuer SDN/EU-Konsolidierte-Liste, Trefferqualitaet (False Positives/Negatives), Fuzzy-Match-Schwellenwerte und Audit-Readiness nach BAFA- und Bankaufsichtsanforderungen. Bewertet ob das eingesetzte Tool die regulatorischen Mindestanforderungen erfuellt. Output: Validierungsbericht mit Gap-Analyse. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Sammelgenehmigung Export Schulung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-sammelgenehmigung-export`

**Fokus:** Globale und Sammelausfuhrgenehmigungen bei BAFA: Allgemeine Ausfuhrgenehmigungen EU001-EU008, nationale AGG, globale Einzelgenehmigungen; Voraussetzungen ICP, Berichtspflichten und Ablauf des Antragsverfahrens ueber ELAN-K2. Output: Sammelgenehmigungsantrag und Nutzungsprotokoll.

# Sammelgenehmigungen und AGG fuer Dual-Use-Exporte: Beantragung und Nutzung

## Mandantenfall

- Exporteur exportiert regelmaessig Dual-Use-Gueter in NATO-Laender; AGG EU001 genuegt oder globale Einzelgenehmigung noetig?
- Unternehmen hat staerkeres ICP und moechte globale Genehmigung BAFA beantragen.
- Sammelgenehmigung ausgelaufen; Lieferung steht an; Notfallverfahren?

## Erste Schritte

1. Gueter und Bestimmungslaender bestimmen; AGGs EU001-EU008 auf Anwendbarkeit pruefen.
2. Ausschlusslisten der AGGs pruefen: Gueter und Laender, die explizit ausgeschlossen sind.
3. ICP-Anforderungen fuer globale Einzelgenehmigung bei BAFA pruefen.
4. BAFA-Antrag ueber ELAN-K2 aufbereiten: Gueter, Laender, Werte, ICP-Nachweis.
5. Berichtspflichten bei Nutzung von AGG und globaler Genehmigung planen (Jahresbericht BAFA).
6. Genehmigungsnutzungs-Protokoll fuer jede Sendung fuehren.

## Rechtsrahmen

- **Art. 12 VO (EU) 2021/821**: EU-Allgemeine Ausfuhrgenehmigungen (EU001-EU008).
- **AWV §§ 8-14**: Nationale Allgemeine Genehmigungen (AGG).
- **§ 11 AWV**: Globale Einzelgenehmigung und Anforderungen.
- **§ 26 AWV**: Berichtspflichten bei Nutzung von Genehmigungen.
- **BAFA-Merkblatt Genehmigungsverfahren**: Verfahrensanforderungen fuer ELAN-K2.**

## Pruef-Raster

- [ ] AGG EU001-EU008 auf Gueter und Bestimmungslaender geprueft?
- [ ] Ausschlusslisten der AGGs vollstaendig durchsucht?
- [ ] ICP-Anforderungen fuer globale Genehmigung erfuellt und nachgewiesen?
- [ ] Jahresbericht-Pflicht bei AGG/globaler Genehmigung bekannt und geplant?
- [ ] Nutzungsprotokoll fuer jede Sendung unter Sammelgenehmigung gefuehrt?
- [ ] Ablaufdatum der Genehmigung im Kalender?

## Typische Fallstricke

- AGG EU001 und EU002 haben lange Ausschlusslisten fuer Laender; UAE, Tuerkei oft ausgeschlossen.
- Berichtspflichten nicht erfuellt; BAFA kann Genehmigung entziehen.
- Nutzungsprotokoll fehlt; bei Pruefung Nachweis nicht moeglich.
- Globale Genehmigung abgelaufen; Zeitlucke zwischen altem und neuem Antrag.

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

AGG-Anwendbarkeitsmatrix, Sammelgenehmigungsantrag ueber ELAN-K2, Nutzungsprotokoll-Vorlage und Berichtspflichten-Kalender.

## Quellen

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Allgemeine Genehmigungen](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/Allgemeine_Genehmigungen/allgemeine_genehmigungen_node.html)
- [BAFA ELAN-K2](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ELAN_K2/elan_k2_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 2. `aussenwirtschaft-schulung-exportkontrolle-rollout`

**Fokus:** Konzeption und Durchfuehrung von Exportkontroll-Schulungen nach BAFA-ICP-Anforderungen: Zielgruppen (Vertrieb, Einkauf, Logistik, IT), Schulungsinhalte, Nachweisdokumentation, E-Learning vs. Praesenz, jaehrliche Wiederholung. Output: Schulungskonzept und Nachweisprotokoll.

# Exportkontroll-Schulungskonzept: ICP-konforme Schulungsplanung und Nachweis

## Mandantenfall

- ICP-Einfuehrung; 150 Mitarbeiter in Vertrieb und Logistik muessen innerhalb 3 Monate geschult sein.
- BAFA beanstandet bei Pruefung fehlende Schulungsnachweise; Nachschulung und Dokumentation noetig.
- Akquisition integriert; neue Tochterfirma mit 80 Mitarbeitern muss Konzernstandard uebernehmen.

## Erste Schritte

1. Zielgruppen definieren: Vertrieb, Einkauf, Logistik, Compliance, IT, Geschaeftsfuehrung.
2. Schulungsinhalt je Zielgruppe anpassen: Gueterklassifizierung fuer Vertrieb, Screening fuer Einkauf.
3. Format waehlen: E-Learning (Skalierbarkeit), Prasenzschulung (Tiefenwirkung), Kombination.
4. Schulungskalender erstellen; jhrliche Wiederholung planen.
5. Schulungsnachweis-Dokumentation: Teilnahmeliste mit Unterschrift, E-Learning-Zertifikat, Inhalt.
6. Quiz oder Test am Ende als Nachweis des Lernerfolgs einbauen.

## Rechtsrahmen

- **BAFA-Merkblatt ICP Element 4**: Schulungspflicht als Kernelement des ICP.
- **Art. 12 VO (EU) 2021/821**: ICP-Nachweis fuer globale Genehmigungen erfordert Schulungsnachweise.
- **§ 130 OWiG**: Aufsichtspflichtverletzung bei fehlender Mitarbeiterschulung.
- **AWV § 26**: Allgemeine Dokumentationspflicht, Schulungsnachweise als Teil.
- **§ 43 GwG**: Schulungspflicht analog auch fuer exportkontrollrelevante Bereiche.**

## Pruef-Raster

- [ ] Alle exportkontrollrelevanten Zielgruppen identifiziert?
- [ ] Schulungsinhalte zielgruppengerecht aufbereitet?
- [ ] Nachweisdokumentation vollstaendig (Teilnahmeliste, Inhaltsverzeichnis)?
- [ ] Jaehrliche Wiederholungsschulung geplant?
- [ ] Testergebnis als Nachweis des Lernerfolgs vorhanden?
- [ ] Neue Mitarbeiter-Onboarding-Schulung ins Standardprozess integriert?

## Typische Fallstricke

- Schulung ohne Nachweis-Dokumentation hat keinen ICP-Wert bei BAFA-Pruefung.
- Generische Online-Schulungen ohne Anpassung an Unternehmensgueter und -maerkte wenig wirksam.
- Schulungsinhalt veraltet; Dual-Use-Liste-Aenderungen nicht eingearbeitet.
- Vertrieb wird oft vergessen; hat aber die meisten Kundenkontakte mit Red-Flag-Potenzial.

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

Schulungskonzept mit Zielgruppen, Inhalten und Format; Schulungskalender, Nachweisprotokoll-Vorlage und Testfragenkatalog.

## Quellen

- [BAFA ICP-Merkblatt Schulung](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Interne_Compliance/interne_compliance_node.html)
- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [OWiG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig_1968/index.html)

## 3. `aussenwirtschaft-schutzmassnahmen-safeguards`

**Fokus:** EU-Schutzmassnahmen (Safeguards) nach VO (EU) 2015/478 Art. 16 und VO (EU) 2015/755 Art. 13: Mengenbeschraenkungen Ueberwachungsmassnahmen und Antragstellung bei der EU-Kommission. Wirkung auf Importeure und Exporteure in betroffenen Sektoren (Stahl Solar Keramik). Abgrenzung zu Antidumping-Zoellen. Output: Safeguard-Pruefvermerk und Reaktionsplan.

# EU-Schutzmassnahmen (Safeguards): Mengenbeschraenkungen und Unternehmensreaktion

## Mandantenfall

- Stahlimporteur ist von EU-Stahl-Safeguard-Kontingenten betroffen; Kontingentanteil beantragen.
- Exporteur aus Drittland fragt wie er auf EU-Safeguard-Untersuchung reagieren kann.
- Solarpanel-Importeur fragt ob auslaufende Safeguard-Massnahme verlaengert wird.

## Erste Schritte

1. Massnahmenart feststellen: Safeguard-Zoll oder Mengen-Kontingent (Tariff Rate Quota)?
2. Betroffenen HS-Code und Ursprungsland in TARIC auf Safeguard-Eintrag pruefen.
3. Kontingents-Zuteilung pruefen: Traditioneller Importeur oder neuer Lieferant?
4. Antrag auf Kontingentszuteilung bei Kommission oder Hauptzollamt fristgerecht stellen.
5. EU-Safeguard-Untersuchung: Als interessierte Partei registrieren und Fragebogen beantworten.
6. Ablauf-Check: Ist Massnahme befristet? Verlaengerungsankuendigung der Kommission beobachten.

## Rechtsrahmen

- **VO (EU) 2015/478 Art. 16**: Safeguard-Massnahmen bei Einfuhren aus WTO-Laendern.
- **VO (EU) 2015/755 Art. 13**: Safeguards fuer Einfuhren aus Laendern ohne Marktwirtschaft.
- **GATT Art. XIX**: WTO-Grundlage fuer Schutzmassnahmen.
- **VO (EU) 2019/159**: Stahlschutzmasnahmen-Verordnung (aktuell in Kraft).
- **UZK Art. 56**: Anwendung von Safeguard-Zolls aetzen in der Zollanmeldung.

## Pruef-Raster

- [ ] HS-Code und Ursprungsland auf Safeguard-Massnahme in TARIC geprueft?
- [ ] Kontingents-Zuteilungssystem verstanden (TRQ-Verfahren)?
- [ ] Antrag auf Kontingent fristgerecht eingereicht?
- [ ] Status als interessierte Partei in Untersuchung registriert?
- [ ] Ablauf der Massnahme im Blick und Reaktionsplanung vorbereitet?
- [ ] Abgrenzung Safeguard/Antidumping fuer kumulierte Belastung analysiert?

## Typische Fallstricke

- Safeguard-Kontingente erschoepfen sich schnell am Jahresanfang; Antrag so frueh wie moeglich.
- Ursprungsland-Shifting (Ausweichen auf Nicht-Safeguard-Land) wird als Umgehung verfolgt.
- EU-Safeguards enden oder werden verlaengert; Planung ohne Monitoring gefaehrlich.
- Kumulierung Safeguard + Antidumping-Zoll auf dieselbe Ware moeglich und kostspielig.

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

Safeguard-Pruefvermerk mit TARIC-Abfrage-Nachweis, Kontingentsantrag-Vorlage, Reaktionsplan fuer laufende Untersuchungen und Monitoring-Kalender.

## Quellen

- [VO (EU) 2015/478 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R0478)
- [VO (EU) 2019/159 Stahl-Safeguards auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0159)
- [TARIC-Datenbank EU-Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [WTO Safeguards](https://www.wto.org/english/tratop_e/safeg_e/safeg_e.htm)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 4. `aussenwirtschaft-screening-tool-validierung`

**Fokus:** Validierung und Qualitaetssicherung von Sanktionsscreening-Tools: Testfall-Design fuer SDN/EU-Konsolidierte-Liste, Trefferqualitaet (False Positives/Negatives), Fuzzy-Match-Schwellenwerte und Audit-Readiness nach BAFA- und Bankaufsichtsanforderungen. Bewertet ob das eingesetzte Tool die regulatorischen Mindestanforderungen erfuellt. Output: Validierungsbericht mit Gap-Analyse.

# Screening-Tool-Validierung: Trefferqualitaet und Audit-Readiness

## Mandantenfall

- Compliance-Abteilung muss gegenueber BAFA nachweisen, dass Screening-Tool Sanktionslisten vollstaendig abdeckt.
- Bank prueft neues Screening-System vor Go-live; Testfall-Set gesucht.
- Bestehendes Tool liefert zu viele False Positives; Schwellenwert-Kalibrierung noetig.

## Erste Schritte

1. Scope festlegen: Welche Listen soll das Tool abdecken (EU-Konsolidierte, OFAC-SDN, UN, BAFA-Embargo)?
2. Testfall-Set erstellen: Bekannte Listeneintraege, Namensvarationen, bekannte False-Positive-Faelle.
3. False-Positive- und False-Negative-Rate messen und dokumentieren.
4. Fuzzy-Match-Schwellenwert analysieren; Einfluss von Umlaut-Normalisierung und Transliteration.
5. Aktualitaet der Listen pruefen: Wie haeufig wird die Listendatenbank aktualisiert?
6. Validierungsbericht erstellen und Schwachstellen mit Korrekturmanahmen priorisieren.

## Rechtsrahmen

- **Art. 2 VO (EU) 2016/679 (DSGVO)**: Datenschutzanforderungen beim Verarbeiten von Personendaten im Screening.
- **OFAC Sanctions Compliance Guidance (2019)**: Empfehlungen zur Screening-Tool-Kalibrierung.
- **BaFin Rundschreiben 08/2021 (GW)**: Mindestanforderungen an Transaktionsmonitoring und Screening.
- **AWV § 24**: Aufbewahrungspflichten fuer Screening-Ergebnisse.
- **Art. 20 VO (EU) 2021/821**: Aufzeichnungspflichten fuer Exportkontrollentscheidungen.

## Pruef-Raster

- [ ] Alle relevanten Sanktionslisten im Tool integriert und aktuell?
- [ ] False-Positive-Rate dokumentiert und tolerierbar?
- [ ] False-Negative-Test mit bekannten Listentreffer durchgefuehrt?
- [ ] Fuzzy-Match-Schwellenwert kalibriert und begruendet?
- [ ] Update-Frequenz der Listendatenbank ausreichend?
- [ ] Audit-Dokumentation fuer BAFA-/BaFin-Pruefung vorhanden?

## Typische Fallstricke

- Zu hoher Fuzzy-Schwellenwert erzeugt Tausende False Positives und laehmt Operations.
- Zu niedriger Schwellenwert uebersieht Namensvarationen sanktionierter Personen.
- Testfall-Sets veraltert und decken neue Listeneintraege nicht ab.
- Transliteration aus kyrillischen oder arabischen Schriften unzureichend.

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

Validierungsbericht mit Testfall-Protokoll, False-Positive/Negative-Rate, Schwachstellen-Liste, Empfehlungen zur Schwellenwert-Kalibrierung und Gap-Analyse fuer Audit.

## Quellen

- [EU-Konsolidierte Finanzsanktionsliste](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0044)
- [BAFA Sanktionen und Embargos](https://www.bafa.de/DE/Aussenwirtschaft/Embargos/embargos_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
