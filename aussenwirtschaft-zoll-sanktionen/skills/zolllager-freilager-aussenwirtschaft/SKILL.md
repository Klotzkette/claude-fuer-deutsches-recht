---
name: zolllager-freilager-aussenwirtschaft
description: "Zolllager Freilager Aussenwirtschaft: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zolllager Freilager Aussenwirtschaft

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Zolllager Freilager Aussenwirtschaft** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-zolllager-freilager` | Zolllager und Freilager nach UZK Art. 240 ff.: Bewilligungsvoraussetzungen Lagerhalterpflichten Bestandsbuchfuehrung Abgabenaussetzung und Aufforderungsverfahren bei Fehlmengen. Unterschied oeffentliches und privates Zolllager und Sonderform Freilager. AEO-Erleichterungen. Output: Bewilligungsantrag und Lagerbuch-Vorlage. |
| `aussenwirtschaft-abfallverbringung` | Grenzueberschreitende Abfallverbringung nach EU-AbfVerbrV (VO 1013/2006 bzw. VO 1418/2007) und KrWG: Notifizierungsverfahren fuer Abfaelle der Gruenen/Gelben/Roten Liste, Genehmigungspflichten beim Hauptzollamt und Bundesumweltamt, AVV-Schluessel-Pruefung, Kontrolle von Empfaengerlandzustimmungen. Output: Verbringungsantrag mit Begleitdokumenten und Behordenschreiben. |
| `aussenwirtschaft-aeo-bewilligung-monitoring` | AEO-Zugelassener-Wirtschaftsbeteiligter-Bewilligung (Customs Simplification/Security/Full): Monitoring laufender Bewilligungsbedingungen nach Art. 38-39 UZK und AEOC/AEOS/AEOF. Prueft regelmaessige Selbstevaluation, Ereignismeldepflichten an Hauptzollamt, Aenderungen in Haftungsverhaeltnissen, Compliance-Systemen und Sicherheitsstandards. Output: Monitoring-Checkliste und Meldedokumentation. |
| `aussenwirtschaft-aktive-veredelung` | Zollverfahren aktive Veredelung nach Art. 256-258 UZK und Art. 240-262 UZK-DA: Beantragung und Nutzung der Bewilligung beim Hauptzollamt, Mengenueberwachung (INF-Blatt), Ausbeute- und Aequivalenzwarensystem, Gesamtabrechnung und Ausfuhr veredelter Erzeugnisse. Prueft wirtschaftliche Voraussetzungen und Rueckgabefristen. Output: Antragsunterlagen und Abschlussabrechnung. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Zolllager Freilager Aussenwirtschaft**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-zolllager-freilager`

**Fokus:** Zolllager und Freilager nach UZK Art. 240 ff.: Bewilligungsvoraussetzungen Lagerhalterpflichten Bestandsbuchfuehrung Abgabenaussetzung und Aufforderungsverfahren bei Fehlmengen. Unterschied oeffentliches und privates Zolllager und Sonderform Freilager. AEO-Erleichterungen. Output: Bewilligungsantrag und Lagerbuch-Vorlage.

# Zolllager und Freilager: Bewilligung Lagerhalterpflichten und Bestandskontrolle

## Mandantenfall

- Spediteur moechte Zolllager fuer Nicht-Unionsware beantragen; Voraussetzungen und Antrag.
- Lagerhalter hat Fehlmenge im Zolllager festgestellt; Nacherhebungsrisiko und Meldepflicht.
- Unternehmen prueft ob Freilager als Alternative zum Zolllager sinnvoll ist.

## Erste Schritte

1. Lagerart bestimmen: Oeffentliches Zolllager (Typ I/II) oder privates Zolllager (Typ III/IV/V)?
2. Bewilligungsvoraussetzungen nach UZK-DA Art. 189 pruefen: Wirtschaftliches Beduerfnis Lagerbuchfuehrung Sicherheitsleistung.
3. Antrag beim Hauptzollamt mit Lagerbeschreibung und Lagerbuchkonzept stellen.
4. Lagerbuch einrichten: Wareneingaenge Ausgaenge Bestandskontrolle und Fehlmengenmeldung.
5. Sicherheitsleistung kalkulieren: Zollwert der gelagerten Ware x Zollsatz x Sicherheitsfaktor.
6. Freilager-Option pruefen: Freilager nach Art. 243 UZK fuer Nicht-Unionsware mit Zollfreiheit.

## Rechtsrahmen

- **UZK Art. 240-248**: Zolllager als besonderes Verfahren.
- **UZK Art. 243-249**: Freilager als Sonderform.
- **UZK-DA Art. 189-198**: Bewilligungsvoraussetzungen und Lagerarten.
- **UZK Art. 79**: Zollschuldentstehung bei Fehlmengen.
- **AEO-Leitlinien TAXUD/B2/047/2011**: AEO-Erleichterungen im Lagerverfahren.

## Pruef-Raster

- [ ] Lagerart korrekt gewaehlt und Bewilligungsvoraussetzungen erfuellt?
- [ ] Lagerbuch mit allen Pflichtfeldern eingerichtet?
- [ ] Sicherheitsleistung ausreichend kalibriert?
- [ ] Fehlmengen-Meldeverfahren dokumentiert?
- [ ] AEO-Erleichterungen beantragt falls vorhanden?
- [ ] Freilager als Alternative geprueft?

## Typische Fallstricke

- Fehlmengen im Zolllager loesen automatisch Zollschuld aus wenn keine Entlastung moeglich.
- Lagerbuch unvollstaendig: BAFA- und Zollpruefung kann Lager sperren.
- Warenfremde Nutzung des Zolllagers (Verarbeitung ohne Bewilligung) fuehrt zu Statusverlust.
- Ueberschreitung der Bewilligungsdauer bei Bewilligung auf Zeit ohne Verlaengerungsantrag.

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

Bewilligungsantrag-Vorlage fuer Hauptzollamt, Lagerbuch-Vorlage mit Pflichtfeldern, Sicherheitsleistungs-Kalkulator und Fehlmengen-Meldeverfahren-Anleitung.

## Quellen

- [UZK Art. 240 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Zolllager](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollverfahren-allgemein/Besondere-Verfahren/Zolllagerverfahren/zolllagerverfahren_node.html)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)

## 2. `aussenwirtschaft-abfallverbringung`

**Fokus:** Grenzueberschreitende Abfallverbringung nach EU-AbfVerbrV (VO 1013/2006 bzw. VO 1418/2007) und KrWG: Notifizierungsverfahren fuer Abfaelle der Gruenen/Gelben/Roten Liste, Genehmigungspflichten beim Hauptzollamt und Bundesumweltamt, AVV-Schluessel-Pruefung, Kontrolle von Empfaengerlandzustimmungen. Output: Verbringungsantrag mit Begleitdokumenten und Behordenschreiben.

# Abfallverbringung: Grenzueberschreitende Entsorgung und Notifizierungsverfahren

## Mandantenfall

- Unternehmen moechte Elektronikschrott (WEEE) zur Verwertung nach Polen verschiffen; Zollabfertigung haelt die Sendung an.
- Recyclingbetrieb importiert Kunststoffabfaelle aus der Tuerkei; Bunderumweltamt fordert Notifizierungsunterlagen.
- Exporteur erhaelt Zollanmeldungsruecklage, weil AVV-Code und gruene Liste nicht uebereinstimmen.

## Erste Schritte

1. AVV-Abfallschluessel und Abfallart bestimmen; Einstufung in Gruene/Gelbe/Rote Liste (Anhaenge VO 1013/2006) pruefen.
2. Bestimmungsland identifizieren: OECD-Mitglied, Nicht-OECD, Basler-Konvention-Vertragspartei oder Verbot?
3. Notifizierungspflicht feststellen (Art. 3 ff. VO 1013/2006); bei gruener Liste vereinfachtes Verfahren?
4. Begleitformular (Anhang VII) oder Notifizierungsdokument (Anhang IA/IB) aufbereiten.
5. Zustaendige Behoerden benennen: Bundesumweltamt als zust. Behoerde am Versandort, Hauptzollamt fuer Ausfuhranmeldung.
6. Sicherheitsleistung (Art. 6 VO 1013/2006) kalkulieren und beantragen.

## Rechtsrahmen

- **VO (EG) 1013/2006** (Verbringungsverordnung): Kernrechtsrahmen fuer Notifizierung und Begleitdokumente.
- **VO (EG) 1418/2007**: Verbote und Einschraenkungen fuer Ausfuhr von gruenen Abfaellen in Nicht-OECD-Laender.
- **§§ 54-55 KrWG**: Genehmigungspflichten und Bussgeldbewehrung bei unerlaubter Verbringung.
- **Art. 36 VO 1013/2006**: Ausfuhrverbote fuer Abfaelle in Nicht-OECD-Staaten.
- **§ 18 AWG**: Aussenwirtschaftsrechtliche Ordnungswidrigkeit bei Umgehungsversuchen.

## Pruef-Raster

- [ ] AVV-Code korrekt und mit Abfallbeschaffenheit konsistent?
- [ ] Eingruppierung in Gruene/Gelbe/Rote Liste und Verfahren korrekt ausgewaehlt?
- [ ] Bestimmungsland hat Zustimmung erteilt (Art. 9 VO 1013/2006)?
- [ ] Begleitformular/Notifizierungsdokument vollstaendig ausgefuellt?
- [ ] Sicherheitsleistung beantragt und bestaetigt?
- [ ] Ausfuhranmeldung in ATLAS mit korrektem Verfahrenscode gestellt?
- [ ] Verbringungsnachweispflicht (Eingangsbestaetigung des Empfaengers) sichergestellt?

## Typische Fallstricke

- Fehlklassifizierung als Produkt statt Abfall: Zollamt und Umweltamt pruefen unabhaengig voneinander.
- Fehlende oder verspaetete Empfaengerbestaetigung fuehrt zu Vollzugsdefizit und Bussgelddruck.
- Kein Notifizierungsverfahren fuer gemischte Fraktionen ohne separate AVV-Einstufung jeder Fraktion.
- Gruene-Liste-Ausfuhr in Nicht-OECD ohne Zustimmung ist formell verboten (VO 1418/2007 Anlage).
- Sicherheitsleistung unterschaetzt: Muss Verbringungs- und Entsorgungskosten abdecken.

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

Verbringungsantrag mit ausgefuelltem Notifizierungsdokument (Anhang IA/IB), Begleitformular (Anhang VII), Checkliste offener Behoerdenbestaedigungen, Kurzvermerkt fuer Zollabfertigung.

## Quellen

- [VO (EG) 1013/2006 konsolidiert](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02006R1013-20230101)
- [VO (EG) 1418/2007 Ausfuhren in Nicht-OECD](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32007R1418)
- [KrWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/krwg/index.html)
- [Bundesumweltamt: Abfallverbringung](https://www.umweltbundesamt.de/themen/abfall-ressourcen/abfallverbringung)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 3. `aussenwirtschaft-aeo-bewilligung-monitoring`

**Fokus:** AEO-Zugelassener-Wirtschaftsbeteiligter-Bewilligung (Customs Simplification/Security/Full): Monitoring laufender Bewilligungsbedingungen nach Art. 38-39 UZK und AEOC/AEOS/AEOF. Prueft regelmaessige Selbstevaluation, Ereignismeldepflichten an Hauptzollamt, Aenderungen in Haftungsverhaeltnissen, Compliance-Systemen und Sicherheitsstandards. Output: Monitoring-Checkliste und Meldedokumentation.

# AEO-Bewilligung: Monitoring laufender Bedingungen und Meldepflichten

## Mandantenfall

- Spediteur mit AEOS-Status stellt Veraenderung in der Geschaeftsfuehrung fest; Frage: Meldepflicht an Hauptzollamt?
- Hersteller mit AEOC erhaelt Hinweis aus Zollpruefung auf mangelhafte Compliance-Dokumentation.
- Konzernmutter moechte AEO-Status auf neue Tochtergesellschaft nach Fusion ausdehnen.

## Erste Schritte

1. Bewilligungstext und erteilte AEO-Kategorie (AEOC/AEOS/AEOF) sichten; Auflagen und Bedingungen identifizieren.
2. Ereignis-/Aenderungslog fuer die letzten 12 Monate erstellen: Personalwechsel, IT-Systeme, Sicherheitskonzept, Eigentuemerstruktur.
3. Meldepflicht nach Art. 23 Abs. 2 UZK-IA und Hauptzollamt-Merkblatt bewerten; Meldefrist kalkulieren.
4. Selbstevaluationsformular des Hauptzollamts aufrufen und aktuellen Erfuellungsgrad feststellen.
5. Etwaige Versaumnisse dokumentieren und Nachbesserungsplan mit Terminen festlegen.
6. Monatlichen Monitoring-Rhythmus mit Verantwortlichen und Eskalationspfad einrichten.

## Rechtsrahmen

- **Art. 38-39 UZK (VO (EU) 952/2013)**: Grundvoraussetzungen und Kategorien der AEO-Zulassung.
- **Art. 24-35 UZK-DA (VO (EU) 2015/2446)**: Beurteilungskriterien fuer Compliance, Buchfuehrung, Solvenz, Sicherheit.
- **Art. 23 Abs. 2 UZK-IA (VO (EU) 2015/2447)**: Meldepflicht bei aenderungsrelevanten Ereignissen.
- **§ 10 ZollVG**: Nationale Kontrollbefugnisse des Hauptzollamts.
- **Art. 27-28 UZK-DA**: Aussetzung und Widerruf der AEO-Bewilligung.

## Pruef-Raster

- [ ] Alle in der Bewilligung genannten Standorte und Prozesse unveraendert oder Aenderungen gemeldet?
- [ ] Geschaeftsfuehrung, UBO und Haftungsverhaeltnisse ohne meldepflichtige Aenderung?
- [ ] Solvenzanforderungen (Art. 26 UZK-DA) erneut geprueft?
- [ ] IT- und Sicherheitskonzept dem aktuellen AEOS/AEOC-Standard entsprechend?
- [ ] Interne Audits durchgefuehrt und dokumentiert?
- [ ] Korrespondierende Behordenkommunikation mit Datum und Aktenzeichen abgelegt?

## Typische Fallstricke

- Meldepflicht nach Art. 23 Abs. 2 UZK-IA wird bei Unternehmensumstrukturierungen oft uebersehen.
- AEO-Status wird nicht automatisch auf Tochtergesellschaften uebertragen; neuer Antrag noetig.
- Versaumnisse bei regelmaessiger Selbstevaluation fuehren zu Aussetzungsverfahren.
- Compliance-Luecken bei Subunternehmern im Sicherheitskonzept werden unterschaetzt.

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

Monitoring-Checkliste mit Bewertung jedes Kriteriums, Meldedokument an Hauptzollamt, Massnahmenplan mit Terminen und Verantwortlichen.

## Quellen

- [UZK Art. 38-39 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de AEO-Merkblatt](https://www.zoll.de/DE/Fachthemen/Zoelle/AEO/aeo_node.html)
- [ZollVG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zollvg/index.html)

## 4. `aussenwirtschaft-aktive-veredelung`

**Fokus:** Zollverfahren aktive Veredelung nach Art. 256-258 UZK und Art. 240-262 UZK-DA: Beantragung und Nutzung der Bewilligung beim Hauptzollamt, Mengenueberwachung (INF-Blatt), Ausbeute- und Aequivalenzwarensystem, Gesamtabrechnung und Ausfuhr veredelter Erzeugnisse. Prueft wirtschaftliche Voraussetzungen und Rueckgabefristen. Output: Antragsunterlagen und Abschlussabrechnung.

# Aktive Veredelung: Bewilligung, Mengenueberwachung und Abschlussabrechnung

## Mandantenfall

- Maschinenbauer moechte importierte Komponenten verarbeiten und als Endprodukt exportieren ohne Einfuhrzoll zu zahlen.
- Textilfirma hat Bewilligung, aber die Ausbeute-Koeffizientenberechnung stimmt nicht mit ATLAS-Buchfuehrung ueberein.
- Pharmaunternehmen beantragt aktive Veredelung fuer Wirkstoffimport aus Indien zur Weiterverarbeitung und EU-Ausfuhr.

## Erste Schritte

1. Wirtschaftliche Voraussetzungen pruefen (Art. 211 Abs. 3 lit. a UZK): Interessentest und Ausfuhrnachweis.
2. Beantragung der Bewilligung beim oertlich zustaendigen Hauptzollamt (Muster: DEK/INT/AV).
3. Buchfuehrungsanforderungen klaren: Lagerbuchhaltungssystem, Mengenueberwachung, Ausbeute-Koeffizienten.
4. INF-Blatt-Verfahren fuer Mehrniederlassungsveredelung pruefen.
5. Aequivalenzwaren-Option bewerten: Gleiche oder gleichartige Waren als Ersatz.
6. Gesamtabrechnung mit Frist planen: Ausbeute-Ist vs. Soll, Fehlmengenbehandlung.

## Rechtsrahmen

- **Art. 256-258 UZK (VO (EU) 952/2013)**: Anwendungsbereich und Bewilligungsvoraussetzungen.
- **Art. 240-262 UZK-DA (VO (EU) 2015/2446)**: Technische Bedingungen, Ausbeute, Aequivalenz.
- **Art. 321-330 UZK-IA (VO (EU) 2015/2447)**: Buchfuehrungs- und Abschlusspflichten.
- **Art. 212-214 UZK**: Bewilligungsantrag und wirtschaftliche Voraussetzungen.
- **§ 10 ZollVG**: Hauptzollamtliche Kontrolle.

## Pruef-Raster

- [ ] Wirtschaftlicher Interessentest dokumentiert und bestanden?
- [ ] Bewilligung aktuell gueltig und Standorte vollstaendig erfasst?
- [ ] Lagerbuchhaltung mit Ausbeute-Koeffizienten und Mengenueberwachung eingerichtet?
- [ ] INF-Blatt fuer Mehrparteienverfahren beantragt?
- [ ] Gesamtabrechnung fristgerecht (Erledigungsfrist aus Bewilligung) erstellt?
- [ ] Nicht veredelter Restbestand korrekt behandelt (Wiederausfuhr, Ueberfuehung in freien Verkehr)?

## Typische Fallstricke

- Ausbeute-Koeffizient zu hoch angesetzt fuehrt zu Zollschuldrisiko bei Gesamtabrechnung.
- Fristversaeumnis bei Erledigungsfrist loest Zollschuld fuer Gesamtmenge aus.
- Aequivalenzwaren ohne spezifische Bewilligungsgrundlage unzulaessig.
- Buchfuehrungs-Luecken bei Unterauftragsvergabe (Lohnveredelung) oft nicht erkannt.

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

Bewilligungsantrag mit wirtschaftlichem Interessennachweis, Buchfuehrungskonzept, INF-Blatt-Muster, Gesamtabrechnungsvorlage.

## Quellen

- [UZK konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de: Aktive Veredelung](https://www.zoll.de/DE/Fachthemen/Zoelle/Besondere-Zollverfahren/Veredelungsverkehr/Aktive-Veredelung/aktive-veredelung_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
