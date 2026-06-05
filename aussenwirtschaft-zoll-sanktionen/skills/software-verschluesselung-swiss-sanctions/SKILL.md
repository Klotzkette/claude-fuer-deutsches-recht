---
name: software-verschluesselung-swiss-sanctions
description: "Software Verschluesselung Swiss Sanctions: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Software Verschluesselung Swiss Sanctions

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Software Verschluesselung Swiss Sanctions** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-software-verschluesselung-kryptografie` | Exportkontrolle fuer Verschluesselungssoftware und Kryptografieprodukte nach VO (EU) 2021/821 Kategorie 5 Teil 2 (Telekommunikation/Informationssicherheit): Klassifizierung von Algorithmen (AES 256 bit RSA ECC) Exportgenehmigungspflicht und Allgemeine Genehmigung EU001. Besonderheiten bei Open-Source-Software und Cloud-Diensten. Output: Klassifizierungsvermerk und Genehmigungspfad. |
| `aussenwirtschaft-swiss-sanctions-touchpoint` | Schweizer Sanktionsrecht als Touchpoint im EU-Exportkontrollmandat: EmbG (Embargogesetz SR 946.231) SECO-Sanktionslisten und deren Konvergenz und Divergenz zu EU-Sanktionen. Relevant bei in der Schweiz ansaessigen Konzerntochtern oder Transaktionen ueber Schweizer Banken. Output: Kurzvergleich EU-CH-Sanktionen und Handlungsempfehlung fuer Schweizer Transaktionsweg. |
| `aussenwirtschaft-trade-finance-lc-guarantees` | Sanktions- und Exportkontrollpruefung bei Trade-Finance-Instrumenten: Akkreditiv (Letter of Credit) Bankgarantien Avale und Dokumenteninkasso unter Beruecksichtigung von VO (EU) 833/2014 Art. 5a (Finanzhilfen) und Korrespondenzbanken-Verboten. Pruefraster fuer Bank-Compliance und Handelsfinanzierungsabteilung. Output: Pruefprotokoll und Freigabeempfehlung. |
| `aussenwirtschaft-transferpricing-zollwert-abgleich` | Abgleich von Verrechnungspreisen und Zollwerten nach UZK Art. 70 (Transaktionswert) und OECD-Verrechnungspreisleitlinien: Pruefung ob konzerninterne Preise den Zollwert beguenstigen und APA-Vereinbarungen mit Zollbewertung kollidieren. Risiko rueckwirkender Zollnacherhebung bei Preisanpassungen. Output: Zollwert-Verrechnungspreis-Konsistenzanalyse. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Software Verschluesselung Swiss Sanctions**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-software-verschluesselung-kryptografie`

**Fokus:** Exportkontrolle fuer Verschluesselungssoftware und Kryptografieprodukte nach VO (EU) 2021/821 Kategorie 5 Teil 2 (Telekommunikation/Informationssicherheit): Klassifizierung von Algorithmen (AES 256 bit RSA ECC) Exportgenehmigungspflicht und Allgemeine Genehmigung EU001. Besonderheiten bei Open-Source-Software und Cloud-Diensten. Output: Klassifizierungsvermerk und Genehmigungspfad.

# Exportkontrolle fuer Verschluesselungssoftware: Kryptografie und Dual-Use-Kategorie 5

## Mandantenfall

- Softwarehaus moechte Produkt mit AES-256-Verschluesselung in Drittlaender exportieren; Genehmigungspflicht unklar.
- Cloud-Dienst mit Ende-zu-Ende-Verschluesselung wird von EU-Kunden an Endkunden in Embargo-Staaten bereitgestellt.
- Open-Source-Kryptobibliothek soll in Exportprodukt integriert werden; Klassifizierung pruefen.

## Erste Schritte

1. Kryptografische Parameter bestimmen: Algorithmus, Schluessellaenge, Protokoll (TLS SSL VPN SSH).
2. Einreihung in Kategorie 5 Teil 2 der EU-Dual-Use-Liste (VO 2021/821 Anhang I) pruefen.
3. Ausnahmeregelungen pruefen: Massenmarktprodukt mit Standard-Kryptografie, Open-Source-Ausnahme.
4. Allgemeine Genehmigung EU001 auf Anwendbarkeit pruefen (Standard-Verschluesselung in Massenmarktsoftware).
5. Ziellaender und Endverwender auf Embargo und Catch-All pruefen.
6. Ergebnis als Klassifizierungsvermerk dokumentieren.

## Rechtsrahmen

- **VO (EU) 2021/821 Anhang I Kategorie 5 Teil 2**: EU-Dual-Use-Liste fuer Kryptografieprodukte.
- **Art. 9 VO (EU) 2021/821**: Allgemeine Genehmigungen (EU001) fuer bestimmte Kryptografieexporte.
- **AWG § 8**: Genehmigungsvorbehalt fuer kontrollierte Waren.
- **EAR Part 742.15 (US)**: US-spezifische Kryptografie-Exportkontrolle (als Risikoanker).
- **Art. 4 VO (EU) 2021/821**: Catch-All bei militaerischer Endverwendung von Kryptografietechnologie.

## Pruef-Raster

- [ ] Kryptografische Parameter vollstaendig erfasst (Algorithmus Schluessellaenge Protokoll)?
- [ ] Einreihung in Kategorie 5 Teil 2 geprueft?
- [ ] Massenmarkt- oder Open-Source-Ausnahme anwendbar?
- [ ] Allgemeine Genehmigung EU001 greift?
- [ ] Zielland und Endverwender auf Embargo und Catch-All geprueft?
- [ ] Klassifizierungsvermerk mit Quellenangabe erstellt?

## Typische Fallstricke

- Standardmaessig eingebettete TLS-Bibliotheken fallen trotzdem unter Dual-Use-Kontrolle.
- Open-Source-Ausnahme gilt nicht fuer modifizierte oder proprietaer eingebettete Varianten.
- Cloud-Dienste: Technologie-Transfer durch Download von verschluesselter Software ueber Landesgrenze.
- US-Re-Export-Kontrollen (EAR) ueberlagern EU-Genehmigung bei US-Ursprungstechnologie.

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

Klassifizierungsvermerk mit Normgrundlage, Genehmigungspfad-Dokumentation und Exportkontroll-Checkliste fuer Produkt-Releases.

## Quellen

- [VO (EU) 2021/821 Anhang I auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Dual-Use Allgemeine Genehmigungen](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Ausfuhrgenehmigungen/Allgemeine_Genehmigungen/allgemeine_genehmigungen_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 2. `aussenwirtschaft-swiss-sanctions-touchpoint`

**Fokus:** Schweizer Sanktionsrecht als Touchpoint im EU-Exportkontrollmandat: EmbG (Embargogesetz SR 946.231) SECO-Sanktionslisten und deren Konvergenz und Divergenz zu EU-Sanktionen. Relevant bei in der Schweiz ansaessigen Konzerntochtern oder Transaktionen ueber Schweizer Banken. Output: Kurzvergleich EU-CH-Sanktionen und Handlungsempfehlung fuer Schweizer Transaktionsweg.

# Schweizer Sanktionen als Touchpoint: EmbG und SECO-Listen im EU-Mandat

## Mandantenfall

- Deutsches Unternehmen wickelt Zahlungen ueber Schweizer Tochtergesellschaft ab; SECO-Listencheck erforderlich.
- Schweizer Konzernzentrale stellt Frage ob EU-Russland-Sanktionen fuer CH-Entitaet gelten.
- Transaktion soll ueber Schweizer Bank abgewickelt werden; Sanktionskonvergenz pruefen.

## Erste Schritte

1. Relevanz der Schweizer Sanktionen pruefen: Schweizer Entitaet beteiligt oder Schweizer Bankverbindung?
2. SECO-Sanktionsliste abrufen und mit EU-Konsolidierter-Liste abgleichen.
3. Divergenzen identifizieren: Welche Personen/Entitaeten sind nur in EU oder nur in CH-Liste?
4. EmbG-Verbote fuer konkrete Transaktion anwenden.
5. Koordination zwischen EU-Compliance und CH-Compliance der Gruppe sicherstellen.
6. Ergebnis als Touchpoint-Vermerk im EU-Mandat festhalten.

## Rechtsrahmen

- **EmbG SR 946.231 (CH)**: Schweizer Embargogesetz als nationale Umsetzungsgrundlage.
- **SECO-Verordnungen (CH)**: Spezifische Embargomasnahmen gegen Russland Iran etc.
- **VO (EU) 833/2014**: EU-Russland-Sanktionen als Referenzrahmen fuer Divergenzanalyse.
- **AWG § 1**: Territorialer Anwendungsbereich des deutschen Aussenwirtschaftsrechts.
- **Art. 11 VO (EU) 833/2014**: Gerichtsbarkeitsregeln fuer konzerninterne Transaktionen.

## Pruef-Raster

- [ ] Schweizer Entitaet oder Bank in Transaktion beteiligt?
- [ ] SECO-Liste aktuell abgerufen und abgeglichen?
- [ ] Divergenzen zwischen EU- und CH-Sanktionsliste identifiziert?
- [ ] EmbG-Verbote fuer konkrete Sachverhalt geprueft?
- [ ] Konzernweite Koordination sichergestellt?

## Typische Fallstricke

- Schweiz folgt EU-Sanktionen meist aber mit Zeitverzug; aktuelle Fassung von SECO abrufen.
- Schweizer Banken unterliegen SECO-Recht; EU-Sanktionen gelten fuer sie nur indirekt.
- Konzernmutter in EU kann nicht die Schweizer Tochter zur Verletzung von EmbG anweisen.
- Eigentums-/Kontrollkette muss auch nach Schweizer Gesellschaftsrecht analysiert werden.

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

Kurzvergleich EU-CH-Sanktionslage mit Divergenz-Tabelle, Handlungsempfehlung fuer Schweizer Transaktionsweg und Koordinationsprotokoll fuer Konzern-Compliance.

## Quellen

- [SECO Sanktionen Schweiz](https://www.seco.admin.ch/seco/de/home/Aussenwirtschaftspolitik_Wirtschaftliche_Zusammenarbeit/Wirtschaftsbeziehungen/exportkontrollen-und-sanktionen/sanktionen-embargos.html)
- [EmbG SR 946.231 auf admin.ch](https://www.fedlex.admin.ch/eli/cc/2003/304/de)
- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 3. `aussenwirtschaft-trade-finance-lc-guarantees`

**Fokus:** Sanktions- und Exportkontrollpruefung bei Trade-Finance-Instrumenten: Akkreditiv (Letter of Credit) Bankgarantien Avale und Dokumenteninkasso unter Beruecksichtigung von VO (EU) 833/2014 Art. 5a (Finanzhilfen) und Korrespondenzbanken-Verboten. Pruefraster fuer Bank-Compliance und Handelsfinanzierungsabteilung. Output: Pruefprotokoll und Freigabeempfehlung.

# Trade Finance und Sanktionen: Akkreditive Garantien und Finanzhilfe-Verbote

## Mandantenfall

- Bank erhalt Anfrage zur Eroeffffnung eines Akkreditivs fuer Lieferung nach Russland; Sanktionspruefung.
- Exporteur beantragt Ausfuhrgarantie fuer Lieferung an iranischen Staatskonzern; EUC und Sanktionscheck.
- Dokumenteninkasso fuer Textillieferung nach Belarus; Korrespondenzbank-Kette pruefen.

## Erste Schritte

1. Transaktionsstruktur aufnehmen: Akkreditivbeteiligter Importeur Exporteur eroeffnende und bestaetigende Bank.
2. Alle Beteiligten gegen EU-Konsolidierte-Liste OFAC-SDN und BAFA-Embargo pruefen.
3. Verbote fuer Finanzhilfe (Art. 5a VO 833/2014 fuer Russland) und Bereitstellungsverbote pruefen.
4. Bestimmungsland und Waren-HS-Codes auf Gueter-Embargo pruefen.
5. Korrespondenzbank-Kette auf sanktionierte Institute pruefen.
6. Freigabeentscheidung mit Quellennachweis dokumentieren.

## Rechtsrahmen

- **Art. 5a VO (EU) 833/2014**: Verbot von Transaktionen mit bestimmten russischen Staatsbanken.
- **Art. 2 Abs. 1 VO (EU) 269/2014**: Bereitstellungsverbot fuer Gelder an gelistete Personen.
- **Art. 26 VO (EU) 267/2012 (Iran)**: Finanzhilfeverbot gegenueber iranischen Banken.
- **§ 18 AWG**: Strafbarkeit bei verbotener Finanzhilfe an sanktionierte Entitaeten.
- **UZK Art. 87**: Zollwertbescheinigung und Dokumentationspflicht bei Trade-Finance.

## Pruef-Raster

- [ ] Alle Trade-Finance-Beteiligten gegen Sanktionslisten geprueft?
- [ ] Finanzhilfe-Verbote fuer Bestimmungsland relevant?
- [ ] Warenklassifizierung und Embargo-Relevanz der Lieferung geprueft?
- [ ] Korrespondenzbank-Kette auf sanktionierte Banken durchsucht?
- [ ] Quellenstand der Sanktionsliste dokumentiert?
- [ ] Freigabe- oder Ablehungsentscheidung archiviert?

## Typische Fallstricke

- Zweitbeguenstigte hinter Akkreditiv kann gelistete Person/Entitaet sein.
- Finanzhilfe-Verbote greifen auch bei mittelbarer Unterstuetzung durch nicht-sanktionierte Partei.
- Korrespondenzbanken in Drittlaendern haben eigene Listenpflichten; Konflikte moeglich.
- Alte Akkreditive bleiben gueltig bis Ablauf; Sanktionsaenderungen erfordern Re-Pruefung.

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

Trade-Finance-Pruefprotokoll mit Sanktionslistenabgleich, Waren-Embargo-Check, Entscheidungsmatrix und archivierter Freigabe- oder Ablehungsbegruendung.

## Quellen

- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [VO (EU) 269/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [EU-Konsolidierte Finanzsanktionsliste EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0044)
- [BAFA Embargos](https://www.bafa.de/DE/Aussenwirtschaft/Embargos/embargos_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 4. `aussenwirtschaft-transferpricing-zollwert-abgleich`

**Fokus:** Abgleich von Verrechnungspreisen und Zollwerten nach UZK Art. 70 (Transaktionswert) und OECD-Verrechnungspreisleitlinien: Pruefung ob konzerninterne Preise den Zollwert beguenstigen und APA-Vereinbarungen mit Zollbewertung kollidieren. Risiko rueckwirkender Zollnacherhebung bei Preisanpassungen. Output: Zollwert-Verrechnungspreis-Konsistenzanalyse.

# Zollwert und Verrechnungspreise: Konsistenzpruefung und Nacherhebungsrisiko

## Mandantenfall

- Konzern vereinbart Preisanpassung nach Jahresabschluss (true-up); Zollwert der unterjaerigen Einfuhren muss korrigiert werden.
- APA-Vereinbarung mit Finanzamt setzt Verrechnungspreisbandbreite fest; Hauptzollamt akzeptiert Transaktionswert nicht.
- Intrakonzernlieferung zu Niedrigpreis; Zollpruefung zweifelt an Transaktionswert nach UZK Art. 70.

## Erste Schritte

1. Verrechnungspreisdokumentation (Masterfile Localfile) auf Relevanz fuer Zollwert pruefen.
2. Transaktionswert nach UZK Art. 70 Pruefung: Gibt es Preisbeeinflussung durch Verhaeltnis (Art. 70 Abs. 3)?
3. Preisanpassungen und True-Ups: retroaktive Zollwertkorrektur und Nachanmeldungspflicht pruefen.
4. APA-Vereinbarung auf Zollwert-Kompatibilitaet pruefen; WTO Valuation Agreement Art. 1.
5. Alternativmethoden nach UZK Art. 74 wenn Transaktionswert abgelehnt wird.
6. Risikobewertung: Zollnacherhebung und moegliche Zinsen/Bussgelder dokumentieren.

## Rechtsrahmen

- **UZK Art. 70**: Transaktionswert als primaere Zollwertmethode.
- **UZK Art. 71-74**: Alternativmethoden bei Versagen des Transaktionswerts.
- **UZK-DA Art. 127-146**: Detailregelung Zollwertermittlung.
- **OECD-Verrechnungspreisleitlinien (2022)**: Armlaengenprinzip und Dokumentationsstandards.
- **§ 22 ZollVG**: Auskunftspflichten und Nacherhebungsfristen.

## Pruef-Raster

- [ ] Verrechnungspreisdokumentation vorhanden und konsistent mit Zollwert?
- [ ] Transaktionswert-Voraussetzungen (Art. 70 UZK) erfuellt?
- [ ] True-Up-Klauseln und retroaktive Preisanpassungen auf Zollwert-Auswirkung geprueft?
- [ ] APA-Vereinbarung mit WTO-Bewertungsabkommen kompatibel?
- [ ] Risiko rueckwirkender Zollnacherhebung quantifiziert?
- [ ] Alternativmethoden als Fallback dokumentiert?

## Typische Fallstricke

- Nachtraegliche Preisminderungen erhoehen den Zollwert nicht; Nachtragsanmeldung bei Erhoehungen Pflicht.
- APAs mit Finanzbehorden binden Zollbehoerden nicht automatisch.
- Lizenzgebuehren und Royalties koennen den Zollwert erhoehen (UZK Art. 71 Abs. 1 lit. c).
- Konzernmutter-Verrechnungspreise muessen Armlaengenprinzip erfuellen um Transaktionswert zu stuetzen.

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

Konsistenzanalyse Zollwert/Verrechnungspreise, Nacherhebungsrisiko-Memo, Empfehlungen fuer True-Up-Klauseln und Ruecksprache-Strategie mit Haupt- und Finanzzollamt.

## Quellen

- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de Zollwert](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollwert/zollwert_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
