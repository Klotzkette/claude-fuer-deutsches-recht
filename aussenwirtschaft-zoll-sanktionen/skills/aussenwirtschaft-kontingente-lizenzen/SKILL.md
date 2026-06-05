---
name: aussenwirtschaft-kontingente-lizenzen
description: "Kontingente Lizenzen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kontingente Lizenzen

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Kontingente Lizenzen** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-kontingente-lizenzen-trq` | Verwaltung von Zollkontingenten und Tariff-Rate-Quotas (TRQ) nach UZK Art. 56 Abs. 2 lit. b und VO (EU) 952/2013: Antragstellung, TARIC-Kontingentabruf, Kontingentschoepfung, kritische Kontingente und Kontingentlizenzen bei Agrarerzeugnissen. Output: Kontingentantrag und Lizenz-Management-Plan. |
| `aussenwirtschaft-kritische-infrastruktur-investment` | Investitionspruefung bei Erwerb kritischer Infrastruktur (KRITIS) durch Drittstaatsinvestoren nach AWV § 55a und Anhang A: Sektoren Energie, Wasser, Digitale Infrastruktur, Finanzmarkt. Anmeldeschwelle 10 Prozent, BMWK-Verfahren und Verbotstatbestaende. Output: KRITIS-Pruefbericht und BMWK-Anmeldung. |
| `aussenwirtschaft-kulturgut-einfuhr-ausfuhr` | Rechtliche Anforderungen bei grenzueberschreitender Bewegung von Kulturguetern nach VO (EU) 2019/880 und KGSG: Importlizenz fuer archaeologische Gegenstande und Kunstwerke ab Schwellenwert, Ausfuhrgenehmigung nach KGSG, UNESCO-Konvention-Sorgfaltspflichten. Output: Kulturgut-Compliance-Pruefbericht und Antrag. |
| `aussenwirtschaft-lebensmittel-futtermittel-vub` | Verbote und Beschraenkungen (VuB) bei Einfuhr von Lebensmitteln und Futtermitteln: EU-Lebensmittelrecht VO (EG) 178/2002, Pflanzenschutzmittelrueckstaende, RASFF-Notifikationen, Grenzkontrolle und BVVG-Verfahren. Besondere Anforderungen fuer Tierprodukte, Pflanzen und Hochrisiko-Gueter. Output: Einfuhr-VuB-Checkliste. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Kontingente Lizenzen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-kontingente-lizenzen-trq`

**Fokus:** Verwaltung von Zollkontingenten und Tariff-Rate-Quotas (TRQ) nach UZK Art. 56 Abs. 2 lit. b und VO (EU) 952/2013: Antragstellung, TARIC-Kontingentabruf, Kontingentschoepfung, kritische Kontingente und Kontingentlizenzen bei Agrarerzeugnissen. Output: Kontingentantrag und Lizenz-Management-Plan.

# Zollkontingente und TRQ: Antragstellung und Lizenzmanagement

## Mandantenfall

- Fleischimporteur moechte Rindfleiisch aus Uruguay zu Vorzugszollsatz importieren; TRQ-Zuteilung beantragt.
- Stahleinfuhr aus Drittlaendern; Safeguard-Kontingent fast erschoepft; kritisches Kontingent-Management.
- Textilinporteur stellt fest, dass Kontingent fuer bevorzugte Lieferung nicht ausgeschoepft ist; Uebertragung moeglich?

## Erste Schritte

1. TARIC-Datenbank auf Kontingente fuer betroffene Waren und Ursprungslaender pruefen.
2. Kontingentart bestimmen: autonom, praeferenziell, TRQ aus Handelsabkommen.
3. Kontingentlizenzen bei der zustendigen Stelle beantragen (z.B. BLE fuer Agrar-TRQ).
4. Kontingenterschoepfung und kritischen Status in TARIC kontinuierlich monitoring.
5. Zollanmeldung mit Kontingent-Requestcode erstellen (Zusatzcode in TARIC).
6. Kontingentlizenz aufbewahren und fristgerecht verwenden.

## Rechtsrahmen

- **UZK Art. 56 Abs. 2 lit. b**: Ermaechtigung fuer Kontingente.
- **VO (EU) 2021/2278**: Autonome Zollaussetzungen und Kontingente.
- **VO (EU) 1308/2013**: Agrar-TRQ-Verwaltung.
- **UZK-IA Art. 49 ff.**: Verwaltung und Zuteilung von Zollkontingenten.
- **UZK Art. 49**: Kritisches Kontingent und Sicherheitsleistung.

## Pruef-Raster

- [ ] TARIC-Kontingente fuer Ware und Ursprungsland abgefragt?
- [ ] Kontingentart und Verwaltungsstelle korrekt identifiziert?
- [ ] Kontingentlizenz rechtzeitig beantragt?
- [ ] Erschoepfungsstatus vor Anmeldung geprueft?
- [ ] Anmeldung mit korrektem Kontingent-Requestcode erstellt?
- [ ] Lizenz archiviert und Verwendungspflichten beachtet?

## Typische Fallstricke

- Kontingent sichtbar erschoepft kurz vor Anmeldung; Anmeldung trotzdem einreichen und ggf. Sicherheitsleistung.
- Agrar-TRQ-Lizenzen der BLE sind nicht uebertragbar.
- Kritisches Kontingent kann Sicherheitsleistung erfordern; cash-flow-Auswirkung.
- Kontingent gilt oft pro Kontingentsjahr; Jahreswechsel-Management notwendig.

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

Kontingentantrag bei zustaendiger Stelle, Kontingent-Monitoring-Plan fuer TARIC-Erschoepfung, Lizenz-Management-Kalender.

## Quellen

- [TARIC-Datenbank EU-Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [BLE Agrar-TRQ-Lizenzen](https://www.ble.de/DE/Themen/Markt-Absatz/markt-absatz_node.html)
- [Zoll.de Zollkontingente](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollkontingente/zollkontingente_node.html)

## 2. `aussenwirtschaft-kritische-infrastruktur-investment`

**Fokus:** Investitionspruefung bei Erwerb kritischer Infrastruktur (KRITIS) durch Drittstaatsinvestoren nach AWV § 55a und Anhang A: Sektoren Energie, Wasser, Digitale Infrastruktur, Finanzmarkt. Anmeldeschwelle 10 Prozent, BMWK-Verfahren und Verbotstatbestaende. Output: KRITIS-Pruefbericht und BMWK-Anmeldung.

# KRITIS-Investitionspruefung: Drittstaatserwerb in kritischer Infrastruktur

## Mandantenfall

- Asiatischer Fonds erwirbt 12 Prozent an Stadtwerken (Strom und Gas); KRITIS-Anmeldepflicht.
- US-Unternehmen kauft deutschen Cloud-Infrastruktur-Anbieter; Digitale-Infrastruktur-Sektor geprueft.
- Staatsfonds erwirbt Minderheitsbeteiligung an Mobilfunkanbieter; 5G-Infrastruktur als kritisch eingestuft.

## Erste Schritte

1. Zielunternehmen einem KRITIS-Sektor nach AWV Anhang A zuordnen.
2. Erwerber auf Drittstaats-Eigenschaft pruefen (Nicht-EU/EFTA/NATO).
3. Anteilsschwelle 10 % bei KRITIS-Sektor bestimmen; Vollzugsverbot beachten.
4. BMWK-Anmeldung vorbereiten: Gesellschaftsstruktur, Geschaftstaetigkeit, Sicherheitskonzept.
5. Moegliche Auflagen und Sicherheitszusagen mit BMWK abstimmen.
6. Closing nur nach BMWK-Freigabe oder Ablauf der Prueffrist.

## Rechtsrahmen

- **AWV § 55a**: KRITIS-Investitionspruefung mit 10-%-Schwelle.
- **AWV Anhang A**: Abschliessende Liste der KRITIS-Sektoren.
- **AWG § 55**: Grundlage fuer Untersagung oder Auflagen.
- **KRITIS-VO (Entwurf 2026)**: Geplante Verschaerfung der Pruefkriterien.
- **EU-Screening-VO (EU) 2019/452**: EU-Kooperationsmechanismus bei Drittstaatsinvestitionen.**

## Pruef-Raster

- [ ] Zielunternehmen in AWV Anhang A gelistetem KRITIS-Sektor?
- [ ] Erwerber ist Drittstaatsinvestor?
- [ ] 10-%-Schwelle ueberschritten oder kontrollierender Einfluss?
- [ ] Vollzugsverbot beachtet?
- [ ] BMWK-Anmeldeunterlagen vollstaendig?
- [ ] Sicherheitszusagen oder Auflagen mit BMWK vorbereitet?

## Typische Fallstricke

- Intrakonzern-Restrukturierungen fallen ebenfalls unter KRITIS-Pruefung wenn Drittstaatsbezug besteht.
- Mittelbare Kontrolle (Vetomacht, Aufsichtsratssitz) kann Anmeldepflicht auslosen.
- BMWK-Pruefung kann Closing erheblich verzoegern; M&A-Zeitplan muss 6+ Monate einplanen.
- Auflagen koennen Betriebsmodell verandern; Auflagenrisiko als wesentlicher M&A-Risikofaktor.

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

KRITIS-Pruefbericht mit Sektoranalyse und Schwellenberechnung, BMWK-Anmeldeformular und Sicherheitszusagen-Entwurf.

## Quellen

- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [BMWK Investitionspruefung KRITIS](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/investitionspruefung.html)
- [VO (EU) 2019/452 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 3. `aussenwirtschaft-kulturgut-einfuhr-ausfuhr`

**Fokus:** Rechtliche Anforderungen bei grenzueberschreitender Bewegung von Kulturguetern nach VO (EU) 2019/880 und KGSG: Importlizenz fuer archaeologische Gegenstande und Kunstwerke ab Schwellenwert, Ausfuhrgenehmigung nach KGSG, UNESCO-Konvention-Sorgfaltspflichten. Output: Kulturgut-Compliance-Pruefbericht und Antrag.

# Kulturgutschutz: Einfuhr- und Ausfuhranforderungen fuer Kunstwerke und Antiquitaeten

## Mandantenfall

- Auktionshaus importiert 200 Jahre alte Vasen aus Aegypten; Importlizenz nach VO (EU) 2019/880 erforderlich?
- Privatperson moechte Gemaelde aus US-Nachlass nach Deutschland importieren; Sorgfaltspflichten.
- Kunsthaendler exportiert seltene Manuskripte; deutsches Ausfuhrverbot nach KGSG?

## Erste Schritte

1. Kulturgut-Kategorie und Ursprungsland bestimmen.
2. Schwellenwerte VO (EU) 2019/880 pruefen: Alter und Wert der Ware.
3. Importlizenzverpflichtung und Erklaerung des Importeurs pruefen.
4. Sorgfaltspflicht: Provenienzrecherche und Dokumentation der legalen Ausfuhr aus Ursprungsland.
5. Nationales Ausfuhrverbot nach KGSG (nationales Kulturgut) pruefen.
6. Einfuhr-/Ausfuhranmeldung mit korrektem HS-Code und TARIC-Besonderheiten.

## Rechtsrahmen

- **VO (EU) 2019/880**: Einfuhr von Kulturguetern; Importlizenz und Importeurerklaerung.
- **KGSG**: Schutz deutschen Kulturgutes; Ausfuhrgenehmigungspflicht.
- **UNESCO-Konvention 1970**: Sorgfaltspflichten bei Kulturgut.
- **UZK Art. 56**: Verbote und Beschraenkungen bei Einfuhr.
- **§ 83 KGSG**: Bussgeldbewehrung bei unrechtmaessiger Ausfuhr.**

## Pruef-Raster

- [ ] Kulturgut-Kategorie und Ursprungsland korrekt bestimmt?
- [ ] Schwellenwerte (Alter und Wert) nach VO (EU) 2019/880 geprueft?
- [ ] Importlizenz oder Importeurerklaerung vorbereitet?
- [ ] Provenienzrecherche vollstaendig und dokumentiert?
- [ ] Nationales Kulturgut-Ausfuhrverbot nach KGSG geprueft?
- [ ] TARIC-Besonderheiten und VB-Codes in Zollanmeldung?

## Typische Fallstricke

- Fehlen von Ausfuhrdokumenten aus Ursprungsland loest Sorgfaltspflicht-Verletzung aus.
- Kunstwerke von Fluchtgut-Listungen ('Haus der Kunst' u.a.) koennen Beschlagnahme-Risiko tragen.
- UNESCO-Verdachtslaender (Irak, Syrien, Libyen) erfordern erhoehte Due Diligence.
- Schwellenwerte nach VO (EU) 2019/880 aendern sich bei Erweiterung der Kategorien.

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

Kulturgut-Compliance-Pruefbericht, Importlizenzantrag, Provenienz-Dokumentationsvorlage und ggf. KGSG-Ausfuhrantrag.

## Quellen

- [VO (EU) 2019/880 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0880)
- [KGSG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/kgsg/index.html)
- [Zoll.de Kulturguter](https://www.zoll.de/DE/Fachthemen/Verbote-Beschraenkungen/Kulturgut/kulturgut_node.html)
- [BKM Kulturgutschutz](https://www.bundesregierung.de/breg-de/suche/kulturgutschutz)

## 4. `aussenwirtschaft-lebensmittel-futtermittel-vub`

**Fokus:** Verbote und Beschraenkungen (VuB) bei Einfuhr von Lebensmitteln und Futtermitteln: EU-Lebensmittelrecht VO (EG) 178/2002, Pflanzenschutzmittelrueckstaende, RASFF-Notifikationen, Grenzkontrolle und BVVG-Verfahren. Besondere Anforderungen fuer Tierprodukte, Pflanzen und Hochrisiko-Gueter. Output: Einfuhr-VuB-Checkliste.

# Lebensmittel- und Futtermitteleinfuhr: Verbote, Beschraenkungen und Grenzkontrolle

## Mandantenfall

- Importeur bringt Getrocknetenfischprodukte aus Vietnam ein; amtliche Kontrolle am Grenzuebergangsstelle notwendig?
- Einfuhr von Gewuerzen aus Indien; Pestizidruckstaende-Anforderungen und RASFF-Warnungen.
- Tierhalter importiert Futtermittel aus Weissrussland; Ursprungszeugnisse und Seuchenschutzanforderungen.

## Erste Schritte

1. Produkt nach VO (EG) 178/2002 und VO (EG) 853/2004 einordnen; tierischen oder pflanzlichen Ursprungs?
2. Bestimmung des Grenzuebergangsstelle mit amtlicher Kontrollstelle (BVVG-Liste).
3. RASFF-Datenbank auf aktuell laufende Warnungen fuer Produkt/Ursprungsland pruefen.
4. Veterinar-/Phytosanitaere Zertifikate aus Exportland beschaffen.
5. IMPORT-Voranmeldung im TRACES NT-System vornehmen.
6. Probennahme und Laboranalyse planen; Lieferverzugsrisiko einkalkulieren.

## Rechtsrahmen

- **VO (EG) 178/2002**: Allgemeines Lebensmittelrecht, Sicherheitsanforderungen.
- **VO (EU) 2017/625**: Amtliche Kontrollen bei Einfuhr; Grenzkontrollstellen.
- **VO (EG) 853/2004**: Hygieneanforderungen fuer Lebensmittel tierischen Ursprungs.
- **RL 2000/29/EG**: Pflanzenschutz-Einfuhrverbote.
- **VO (EU) 142/2011**: Tierische Nebenprodukte (ANP); Einfuhrverbote.

## Pruef-Raster

- [ ] Produkt-Einstufung (tierisch/pflanzlich) und anwendbares EU-Hygienerecht klar?
- [ ] Grenzkontrollstelle mit amtlicher Kontrollfunktion fuer Produkt identifiziert?
- [ ] RASFF-Warnungen fuer Produkt und Ursprungsland geprueft?
- [ ] Gesundheits-/Veterinarzertifikate vollstaendig und aktuell?
- [ ] TRACES NT-Voranmeldung rechtzeitig erfolgt?
- [ ] Probennahme-Risiko in Lieferzeitplan eingeplant?

## Typische Fallstricke

- TRACES NT-Voranmeldung zu spaet kann amtliche Kontrolle verzoegern und Ware einfrieren.
- RASFF-Warnungen veraendern sich schnell; vor jeder Sendung pruefen.
- Einfuhr aus bestimmten Drittlaendern erfordert zusaetzliche Einfuhrbescheinigungen.
- Futtermittel unterliegen eigenen Regelwerken (VO (EG) 183/2005); nicht mit Lebensmittelrecht verwechseln.

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

Einfuhr-VuB-Checkliste fuer Lebensmittel/Futtermittel, TRACES NT-Voranmeldeprotokoll, Grenzkontrollstellen-Uebersicht und RASFF-Pruefprotokoll.

## Quellen

- [VO (EG) 178/2002 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32002R0178)
- [RASFF-Datenbank EU-Kommission](https://webgate.ec.europa.eu/rasff-window/screen/search)
- [Zoll.de Lebensmittel](https://www.zoll.de/DE/Fachthemen/Verbote-Beschraenkungen/Lebensmittel-Futtermittel/lebensmittel-futtermittel_node.html)
- [BVL Lebensmitteleinfuhr](https://www.bvl.bund.de/DE/Arbeitsbereiche/01_Lebensmittel/03_Verbraucherinnen_und_Verbraucher/lebensmittel_node.html)
