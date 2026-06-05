---
name: aussenwirtschaft-versandverfahren-ncts
description: "Versandverfahren Ncts: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versandverfahren Ncts

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Versandverfahren Ncts** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-versandverfahren-ncts` | Unionszollkodex-Versandverfahren (T1/T2) im NCTS (New Computerised Transit System): Eroeffffnung Sicherheitsleistung Transit-Begleitdokument (TAD) Bestimmungsstelle und Freigabe. Besonderheiten bei Bahn-CMR-Luft-Transit und AEO-Verguenstigungen. Risiko Transit-Nichtbeendigung und Nacherhebung. Output: Versandanmeldungs-Anleitung und Sicherheitsleistungs-Kalkulation. |
| `aussenwirtschaft-zollverfahren-bewilligungen` | Zollverfahren und Bewilligungen nach UZK Art. 211: Uebersicht aktive und passive Veredelung Zolllager Voruebergehende Verwendung Versandverfahren und Endverwendung. Bewilligungsvoraussetzungen wirtschaftliche Voraussetzungen und Vereinfachungen fuer AEO-Inhaber. Output: Verfahrens-Auswahlmatrix und Bewilligungsantrag-Vorlage. |
| `aussenwirtschaft-distributor-vertrag-exportkontrolle` | Exportkontrollklauseln in Distributor- und Handelsvertretervertraegen: Vertragliche Pflichten des Importeurs zur Einhaltung von Re-Export-Verboten, Endverwender-Verpflichtungen und No-Russia-Clause (Art. 12g VO 833/2014). Haftungsklauseln, Compliance-Pflichten des Partners und Due-Diligence-Rechte des Exporteurs. Output: Standardklauselwerk und Compliance-Schedule. |
| `aussenwirtschaft-exportkontrollklauseln-vertrag` | Gestaltung exportkontrollrechtlicher Vertragsklauseln in Liefer-, Lizenz- und Kooperationsvertraegen: No-Russia-Clause nach Art. 12g VO (EU) 833/2014, Endverwendungsklauseln, Re-Export-Verbote, Ruecktrittsrechte bei Genehmigungsversagung, Vertragsstrafen bei Verstoss. Output: Klauselbausteine und Vertragspruefbericht. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Versandverfahren Ncts**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-versandverfahren-ncts`

**Fokus:** Unionszollkodex-Versandverfahren (T1/T2) im NCTS (New Computerised Transit System): Eroeffffnung Sicherheitsleistung Transit-Begleitdokument (TAD) Bestimmungsstelle und Freigabe. Besonderheiten bei Bahn-CMR-Luft-Transit und AEO-Verguenstigungen. Risiko Transit-Nichtbeendigung und Nacherhebung. Output: Versandanmeldungs-Anleitung und Sicherheitsleistungs-Kalkulation.

# NCTS-Versandverfahren T1/T2: Anmeldung Sicherheitsleistung und Bestimmungsstelle

## Mandantenfall

- Spediteur benoetigt T1-Anmeldung fuer Nicht-Unionsware durch Deutschland nach Polen.
- AEO-Inhaber moechte Erleichterungen beim Versandverfahren (vereinfachte Verfahren zulassige Abgangsstelle) nutzen.
- Transitpapier nicht bei Bestimmungsstelle vorgelegt; Zollschuldentstehung und Nacherhebung.

## Erste Schritte

1. Versandverfahren-Typ bestimmen: T1 (Nicht-Unionsware) oder T2 (Unionsware auSSERhalb EU-Zollgebiet).
2. Sicherheitsleistung kalkulieren: Art. 89 ff. UZK; Gesamtbuergschaft oder Einzelsicherheit.
3. NCTS-Anmeldung bei Abgangsstelle; Felder Waren-Code Menge Wert Empfaenger Bestimmungsstelle.
4. Transit-Begleitdokument (TAD) drucken und Sendung begleiten.
5. Bestimmungsstelle: Warenankunft melden und Entladungsprotokoll erstellen.
6. Freigabe in NCTS beantragen; Sicherheitsleistung freigeben nach Beendigung.

## Rechtsrahmen

- **UZK Art. 226-236**: Unionsversandverfahren T1 und T2.
- **UZK-DA Art. 275-285**: Vereinfachungen fuer zugelassene Versender/Empfaenger.
- **UZK Art. 89-100**: Sicherheitsleistung im Versandverfahren.
- **UZK Art. 79**: Zollschuldentstehung bei nicht ordnungsgemaesser Erledigung.
- **AEO-Leitlinien (TAXUD/B2/047/2011)**: AEO-Erleichterungen im Versandverfahren.

## Pruef-Raster

- [ ] Versandverfahren-Typ (T1/T2) korrekt bestimmt?
- [ ] Sicherheitsleistung ausreichend und gueltig?
- [ ] NCTS-Anmeldung vollstaendig und korrekt?
- [ ] TAD korrekt ausgedruckt und Sendung begleitend?
- [ ] Bestimmungsstelle rechtzeitig angemeldet?
- [ ] Freigabe in NCTS und Entlastung der Sicherheitsleistung bestaetigt?

## Typische Fallstricke

- Nicht-Vorlage bei Bestimmungsstelle loest automatische Mahnverfahren und Zollschuld aus.
- Sicherheitsleistung bei haeufigen Sendungen schnell erschoepft; Monitoring noetig.
- Vereinfachte Verfahren (zugelassener Versender) erfordern separate Bewilligung.
- TIR-Carnets als Alternative haben andere Sicherheitsleistungsstruktur.

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

NCTS-Versandanmeldungs-Anleitung, Sicherheitsleistungs-Kalkulator, Checkliste Bestimmungsstellen-Vorgang und Muster-Eskalationsprotokoll bei Transit-Nichtbeendigung.

## Quellen

- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Versandverfahren](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollverfahren-allgemein/Versandverfahren/versandverfahren_node.html)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)

## 2. `aussenwirtschaft-zollverfahren-bewilligungen`

**Fokus:** Zollverfahren und Bewilligungen nach UZK Art. 211: Uebersicht aktive und passive Veredelung Zolllager Voruebergehende Verwendung Versandverfahren und Endverwendung. Bewilligungsvoraussetzungen wirtschaftliche Voraussetzungen und Vereinfachungen fuer AEO-Inhaber. Output: Verfahrens-Auswahlmatrix und Bewilligungsantrag-Vorlage.

# Zollverfahren und Bewilligungen: Auswahl wirtschaftliche Voraussetzungen und AEO

## Mandantenfall

- Produktionsunternehmen fragt welches Zollverfahren fuer Import von Vorprodukten mit Wiederausfuhr optimal ist.
- Unternehmen hat Bewilligung fuer aktive Veredelung erhalten; wirtschaftliche Voraussetzungen nachweisen.
- AEO-Inhaber fragt welche Verfahrenserleichterungen er bei Bewilligungsantrag nutzen kann.

## Erste Schritte

1. Verwendungszweck der Ware klaren: Verarbeitung Lagerung Durchfuhr oder Endverwendung?
2. Verfahren auswaehlen: Aktive Veredelung (Rueckaustausch) Zolllager Voruebergehende Verwendung oder Versand?
3. Wirtschaftliche Voraussetzungen nach UZK Art. 211 Abs. 3 pruefen: EU-Produktionsinteressen nicht beeintraechtigt?
4. Bewilligungsantrag in ATLAS-Antragsmodul vorbereiten; AEO-Status angeben.
5. Buergschaft/Sicherheitsleistung kalkulieren und bei Zollbehoerde hinterlegen.
6. Bewilligungsdokument prufen: Gueltigkeitsdauer Waren-Scope Mengendeckel und Abrechnungsfristen.

## Rechtsrahmen

- **UZK Art. 210-225**: Besondere Verfahren und Bewilligungsrahmen.
- **UZK Art. 211**: Bewilligungsvoraussetzungen und wirtschaftliche Pruefung.
- **UZK-DA Art. 161-184**: Detailregeln fuer besondere Verfahren.
- **UZK Art. 38-41**: AEO-Zulassung und Erleichterungen.
- **UZK-IA Art. 13-17**: AEO-Verfahrensvereinfachungen.

## Pruef-Raster

- [ ] Verwendungszweck klar und Verfahren optimal ausgewaehlt?
- [ ] Wirtschaftliche Voraussetzungen nach Art. 211 Abs. 3 geprueft?
- [ ] Bewilligungsantrag vollstaendig und korrekt ausgefuellt?
- [ ] Sicherheitsleistung ausreichend und gueltig?
- [ ] AEO-Status fuer Erleichterungen genutzt?
- [ ] Bewilligungsdokument auf Scope und Fristen geprueft?

## Typische Fallstricke

- Wirtschaftliche Voraussetzungen muessen regelmaessig nachgewiesen werden; nicht nur bei Erstantrag.
- Verfahren mischen (z.B. aktive Veredelung + Zolllager) ist moeglich aber erfordert separate Bewilligungen.
- Abrechnung nach Ablauf der Bewilligungsfrist vergessen loest Zollschuld aus.
- AEO-Status verloren: Erleichterungen enden automatisch; Bewilligung erneut prufen.

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

Verfahrens-Auswahlmatrix mit Kosten-Nutzen-Analyse, Bewilligungsantrag-Vorlage und Abrechnungskalender.

## Quellen

- [UZK Art. 211 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Besondere Verfahren](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollverfahren-allgemein/Besondere-Verfahren/besondere-verfahren_node.html)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [BAFA AEO](https://www.bafa.de/DE/Aussenwirtschaft/AEO/aeo_node.html)

## 3. `aussenwirtschaft-distributor-vertrag-exportkontrolle`

**Fokus:** Exportkontrollklauseln in Distributor- und Handelsvertretervertraegen: Vertragliche Pflichten des Importeurs zur Einhaltung von Re-Export-Verboten, Endverwender-Verpflichtungen und No-Russia-Clause (Art. 12g VO 833/2014). Haftungsklauseln, Compliance-Pflichten des Partners und Due-Diligence-Rechte des Exporteurs. Output: Standardklauselwerk und Compliance-Schedule.

# Distributor-Vertrag und Exportkontrolle: Klauseln und Compliance-Pflichten

## Mandantenfall

- Exporteur schliesst Distributionsvertrag mit Haendler in den VAE; Re-Export-Risiken vertraglich absichern.
- Konzern prueft Bestandsvertraege mit Distributoren auf Russland-No-Russia-Clause-Konformitaet.
- KMU moechte vertragliche Handhabe um Distributor bei Verdacht auf Sanktionsumgehung zu korrekt.

## Erste Schritte

1. Risikoprofil des Distributors und der Ziellaender ermitteln.
2. Pflicht zur No-Russia-Clause pruefen (Art. 12g VO 833/2014) fuer relevante Gueterkategorien.
3. Exportkontroll-Klauseln entwerfen: Re-Export-Verbot, Endverwender-Pflicht, Screeningpflicht, Audit-Recht.
4. Gerichtsstand und anwendbares Recht mit Blick auf Durchsetzbarkeit der Exportkontroll-Pflichten waehlen.
5. Vertragspartner bei Widerstand aufklaeren: Haftungsrisiken fuer den Distributor selbst.
6. Bestandsvertraege auf fehlende Klauseln pruefen und Nachtragsvereinbarungen vorbereiten.

## Rechtsrahmen

- **Art. 12g VO (EU) 833/2014**: Pflichtklausel in Vertraegen ueber bestimmte Gueter.
- **AWG §§ 17-18**: Haftung des Exporteurs bei Kenntnis der Weiterlieferung.
- **Art. 9 VO (EU) 2021/821**: Vertragliche Compliance-Pflichten im Rahmen von ICP.
- **§ 242 BGB**: Treu und Glauben als Auslegungsmassstab fuer Exportkontrollklauseln.
- **VO (EU) 269/2014 Art. 2**: Bereitstellungsverbot auch durch Dritte.

## Pruef-Raster

- [ ] No-Russia-Clause fuer relevante Gueterkategorien integriert?
- [ ] Re-Export-Verbot in Kaufvertrag aufgenommen?
- [ ] Endverwender-Erklaerungspflicht des Distributors geregelt?
- [ ] Audit-Recht des Exporteurs vertraglich gesichert?
- [ ] Gerichtsstand fuer Compliance-Streitigkeiten bestimmt?
- [ ] Bestandsvertraege nachtraeglich angepasst?

## Typische Fallstricke

- Zu allgemeine Formulierungen ('comply with all applicable laws') genuegen fuer Art. 12g VO 833/2014 nicht.
- Fehlende Audit-Rechte verhindern effektive Ueberwachung.
- Ohne Ruecktrittsrecht bei Sanktionsverstoessen bleibt Exporteur in der Haftung.
- Englische Klauselsprache kann bei auslaendischem Gericht anders ausgelegt werden.

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

Standardklauselwerk fuer Exportkontroll-Compliance-Schedule, No-Russia-Clause-Template, Muster-Nachtrag fuer Bestandsvertraege.

## Quellen

- [VO (EU) 833/2014 Art. 12g auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA Compliance im Vertrieb](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Interne_Compliance/interne_compliance_node.html)

## 4. `aussenwirtschaft-exportkontrollklauseln-vertrag`

**Fokus:** Gestaltung exportkontrollrechtlicher Vertragsklauseln in Liefer-, Lizenz- und Kooperationsvertraegen: No-Russia-Clause nach Art. 12g VO (EU) 833/2014, Endverwendungsklauseln, Re-Export-Verbote, Ruecktrittsrechte bei Genehmigungsversagung, Vertragsstrafen bei Verstoss. Output: Klauselbausteine und Vertragspruefbericht.

# Exportkontrollklauseln im Vertrag: Gestaltung und Pruefung

## Mandantenfall

- Liefervertrag mit tuerkischem Abnehmer enthaelt keine Re-Export-Beschraenkung; Russland-Sanktionsrisiko.
- Lizenzvertrag mit US-Technologie-Lizenzgeber verlangt ITAR-Flowdown-Klauseln.
- Kaufvertrag ueber Dual-Use-Maschine ohne Ruecktrittsrecht bei Genehmigungsversagung abgeschlossen.

## Erste Schritte

1. Gueter und Technologie klassifizieren und Genehmigungspflicht feststellen.
2. Relevante Rechtsregime identifizieren: EU-Sanktionen (No-Russia-Clause), US EAR/ITAR, nationale Genehmigungen.
3. Bestehenden Vertrag auf exportkontrollrechtliche Klauseln pruefen.
4. Erforderliche Klauseln identifizieren: No-Russia, Endverwendung, Re-Export-Verbot, Ruecktrittsrecht.
5. Klauselbausteine formulieren oder US-Musterklauseln adaptieren.
6. Vertragsstrafenregime fuer Verstoss gegen Exportkontrollklauseln einbauen.

## Rechtsrahmen

- **Art. 12g VO (EU) 833/2014**: Pflicht zur No-Russia-Clause fuer Anhaenge-XI/XX/XXXV-Gueter.
- **Art. 9 VO (EU) 833/2014**: Bereitstellungsverbot und vertragliche Absicherung.
- **§ 18 AWG**: Strafbarkeit; vertragliche Mitverantwortung.
- **§ 280 BGB**: Schadensersatz bei Verletzung vertraglicher Exportkontrollpflichten.
- **§ 119 BGB**: Anfechtung bei Irrtum ueber Genehmigungspflicht.

## Pruef-Raster

- [ ] No-Russia-Clause nach Art. 12g VO 833/2014 erforderlich und enthalten?
- [ ] Endverwendungsklausel mit konkreten Verboten formuliert?
- [ ] Ruecktrittsrecht bei Genehmigungsversagung vereinbart?
- [ ] Re-Export-Verbot in relevante Drittlaender enthalten?
- [ ] Vertragsstrafe bei Verstoss bestimmt und durchsetzbar?
- [ ] US-Recht-Flowdown-Anforderungen des Lizenzgebers beachtet?

## Typische Fallstricke

- No-Russia-Clause nur auf Papier ohne Monitoring ist kein Schutz; Vertragsstrafe muss Abschreckungswirkung haben.
- Ruecktrittsrecht muss Genehmigungsversagung als Schicksal der Lieferpflicht regeln.
- ITAR-Flowdown durch US-Lizenzgeber kann unbemerkt weitgehende Pflichten auferlegten.
- Formulierung 'geltende Exportkontrollvorschriften' ist zu unbestimmt; konkrete Normen nennen.

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

Klauselbausteine fuer No-Russia, Endverwendung, Re-Export-Verbot, Ruecktrittsrecht und Vertragsstrafe; Vertragspruefbericht mit Lueckenanalyse.

## Quellen

- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [EU-Kommission No-Russia-Clause Muster](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/sanctions-policy-and-legal-framework_en)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA Exportkontrolle allgemein](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
