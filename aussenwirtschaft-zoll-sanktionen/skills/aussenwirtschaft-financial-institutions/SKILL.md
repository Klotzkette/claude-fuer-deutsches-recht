---
name: aussenwirtschaft-financial-institutions
description: "Financial Institutions: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Financial Institutions

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Financial Institutions** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-financial-institutions-correspondent-banking` | Sanktions-Compliance fuer Banken und Finanzinstitute im Korrespondenzbankgeschaeft: Sanktionsscreening von Transaktionen und Gegenparteien nach VO (EU) 2580/2001 und sektorspezifischen Sanktionsverordnungen, SWIFT-Ausschluss-Implikationen, Correspondent-Banking-Due-Diligence. Output: Transaktions-Pruefprotokoll und Risikoklassifizierung. |
| `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll` | Strategische und operative Vorbereitung einer freiwilligen Selbstanzeige bei BAFA oder Hauptzollamt nach §§ 22 Abs. 4 AWG und 371 AO analog: Strafmildernde Wirkung, Sachverhaltsaufklaerung, Zeitpunkt, Form und Inhalt der Anzeige, Koordination mit Strafverfolgungsbehoerden. Output: Selbstanzeigenschreiben und Verteidigungsstrategie. |
| `aussenwirtschaft-gueterlisten-klassifizierung` | Technische Klassifizierung von Waren, Software und Technologie nach Gueterlisten: EU-Dual-Use-Liste Anhang I VO (EU) 2021/821, Kriegswaffenkontrollliste (KrWaffKontrG), MTCR, NSG und Wassenaar-Arrangement. Abgrenzung ML-Gueter von EG-Dual-Use. Output: Klassifizierungsgutachten mit Listenpositionen. |
| `aussenwirtschaft-icp-kontrollsystem` | Aufbau und Auditierung eines Internal Compliance Programme (ICP) nach BAFA-Leitfaden und EU Best Practice Guidelines: Risikobasierte Struktur, Schluessel-Compliance-Elemente, Ausfuhrverantwortlicher, Screening-Prozesse, Dokumentation und Schulungspflichten. Output: ICP-Handbuch-Gliederung und Gap-Analyse. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Financial Institutions**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-financial-institutions-correspondent-banking`

**Fokus:** Sanktions-Compliance fuer Banken und Finanzinstitute im Korrespondenzbankgeschaeft: Sanktionsscreening von Transaktionen und Gegenparteien nach VO (EU) 2580/2001 und sektorspezifischen Sanktionsverordnungen, SWIFT-Ausschluss-Implikationen, Correspondent-Banking-Due-Diligence. Output: Transaktions-Pruefprotokoll und Risikoklassifizierung.

# Korrespondenzbankgeschaeft: Sanktions-Compliance und Transaktionsscreening

## Mandantenfall

- Deutsche Korrespondenzbank erhaelt USD-Zahlung ueber US-Korrespondenten aus Russland; OFAC-Exposure.
- Bank soll Akkreditiv fuer iranischen Importeur eroeffnen; Gegenpartei nicht in SDN-Liste, aber enge Verbindungen zum Staat.
- Finanzinstitut prueft neue Korrespondenzbankbeziehung mit Tuerkei; Sanktionsumgehungsrisiko Russland.

## Erste Schritte

1. Transaktionsparteien und Zahlungsweg vollstaendig erfassen (Auftraggeber, Beguenstigter, alle Intermediare).
2. Screening gegen konsolidierte EU-Sanktionsliste, OFAC SDN und sektorspezifische Listen.
3. Eigentums- und Kontrollpruefung (50-%-Regel) aller Parteien.
4. Korrespondenzbank-Risikoklassifizierung: CDD-Dokumente, Sanktionsprogramme des Partnerlandes.
5. Bei Risikoindikatoren: Enhanced Due Diligence, Rueckfragen, ggf. Ablehnung.
6. Transaktionsentscheidung mit Quellenprotokoll und Datum dokumentieren.

## Rechtsrahmen

- **VO (EU) 2580/2001**: Terrorismusfinanzierungs-Sanktionen.
- **VO (EU) 833/2014 Art. 5 ff.**: Finanzierungsverbote Russland.
- **VO (EU) 267/2012 Art. 23**: Finanzsanktionen Iran.
- **§§ 3 ff. GwG**: Sorgfaltspflichten bei Verdacht auf Sanktionsverstoesse.
- **§ 18 AWG i.V.m. § 17 AWV**: Bereitstellungsverbot im Zahlungsverkehr.

## Pruef-Raster

- [ ] Alle Transaktionsparteien inkl. Intermediare gescreent?
- [ ] 50-%-Eigentums-/Kontrollregel fuer alle juristischen Personen geprueft?
- [ ] OFAC-Exposure bei USD-Transaktionen beachtet?
- [ ] Korrespondenzbank-CDD-Dokumentation vollstaendig?
- [ ] Sektorspezifische Verbote (Finanzierung, Anleihen) geprueft?
- [ ] Transaktionsentscheidung mit Datum und Quellenstand protokolliert?

## Typische Fallstricke

- Indirekte Sanktionsexponierung durch Korrespondenzbank-Kette wird unterschaetzt.
- OFAC-Jurisdiktion bei USD-Transaktionen gilt unabhaengig von EU-Sanktionsstatus.
- 50-%-Regel fuer Eigentum und Kontrolle wird bei komplexen Holdingstrukturen nicht vollstaendig angewendet.
- SWIFT-Ausschluss russischer Banken schliesst nicht alle Transfermoeglichkeiten aus.

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

Transaktions-Pruefprotokoll mit Screening-Ergebnis, Risikoklassifizierung der Korrespondenzbank, Entscheidungsvermerk und Enhanced-Due-Diligence-Dossier.

## Quellen

- [EU-Finanzsanktionsliste FSAP](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [BAFA Finanzsanktionen](https://www.bafa.de/DE/Aussenwirtschaft/Finanzsanktionen/finanzsanktionen_node.html)

## 2. `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`

**Fokus:** Strategische und operative Vorbereitung einer freiwilligen Selbstanzeige bei BAFA oder Hauptzollamt nach §§ 22 Abs. 4 AWG und 371 AO analog: Strafmildernde Wirkung, Sachverhaltsaufklaerung, Zeitpunkt, Form und Inhalt der Anzeige, Koordination mit Strafverfolgungsbehoerden. Output: Selbstanzeigenschreiben und Verteidigungsstrategie.

# Freiwillige Offenlegung bei BAFA und Zoll: Strategie und Vorbereitung

## Mandantenfall

- Unternehmen stellt bei interner Revision fest, dass Dual-Use-Maschinen ohne Genehmigung exportiert wurden.
- Banktransfer an Tochtergesellschaft in Russland versehentlich getaetigt; Sanktionsverstoß erkannt.
- Zollanmeldungen enthielten falsche Ursprungsangaben; Gesamtschaden noch nicht beziffert.

## Erste Schritte

1. Sachverhalt vollstaendig intern aufklaeren und sichern (Legal Hold) bevor Offenlegung.
2. Strafbarkeit und Ordnungswidrigkeitenrisiko fuer jede Handlung bewerten.
3. Zeitpunkt pruefen: Noch vor Behordenerkenntnis oder bereits im Ermittlungsverfahren?
4. Anzeigeinhalte formulieren: Sachverhalt, Ausmass, betroffene Personen, Massnahmen.
5. Koordination mit Strafverteidiger; keine Selbstbelastung einzelner Mitarbeiter ohne Schutzkonzept.
6. Korrekturmassnahmen und ICP-Verbesserungen als Anlage beifuegen.

## Rechtsrahmen

- **§ 22 Abs. 4 AWG**: Strafmilderung bei freiwilliger Offenlegung von Verstoessen.
- **§ 371 AO**: Strafbefreiende Selbstanzeige (analog bei Zollverstoss).
- **§ 153 AO**: Berichtigungspflicht bei erkannter Fehlererklaerung.
- **§ 154 StPO**: Einstellung von Nebenverfahren bei Kooperation.
- **§ 18 AWG**: Strafrahmen Ausfuhrdelikt (bis 5 Jahre Freiheitsstrafe).

## Pruef-Raster

- [ ] Sachverhalt vollstaendig intern aufgeklaert und gesichert?
- [ ] Behordenerkenntnis noch nicht eingetreten?
- [ ] Strafbarkeit einzelner Personen bewertet, Schutzkonzept vorhanden?
- [ ] Anzeigeninhalt vollstaendig (Sachverhalt, Ausmass, Betroffene)?
- [ ] Korrektur- und ICP-Massnahmen formuliert?
- [ ] Abgestimmte Kommunikationsstrategie (intern/extern) bereit?

## Typische Fallstricke

- Unvollstaendige Offenlegung ist schlimmer als keine Offenlegung; alles oder nichts.
- Mitarbeiter muessen gesondert beraten und geschuetzt werden (kein Selbstbelastungszwang).
- Bei laufenden Ermittlungen ist Offenlegung nur im Rahmen der Verteidigungsstrategie sinnvoll.
- Nachtraegliche Korrekturen in ATLAS-Systemen sind moeglicher Beweis; nur mit Behoerdenabstimmung.

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

Selbstanzeigenschreiben an BAFA/Hauptzollamt, Sachverhaltschronologie, Schadensquantifizierung, Massnahmenplan und Verteidigungsstrategie-Kurzpapier.

## Quellen

- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA Exportkontrolle Verstoss](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
- [AO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/index.html)
- [Zoll.de Zollrecht und Strafrecht](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollkodex/zollkodex_node.html)

## 3. `aussenwirtschaft-gueterlisten-klassifizierung`

**Fokus:** Technische Klassifizierung von Waren, Software und Technologie nach Gueterlisten: EU-Dual-Use-Liste Anhang I VO (EU) 2021/821, Kriegswaffenkontrollliste (KrWaffKontrG), MTCR, NSG und Wassenaar-Arrangement. Abgrenzung ML-Gueter von EG-Dual-Use. Output: Klassifizierungsgutachten mit Listenpositionen.

# Gueterlistenklassifizierung: Systematische Einreihung in Dual-Use und Ruestungsgueterlisten

## Mandantenfall

- Maschinenbauer fragt, ob seine neue Praezisionsfraesmaschine unter Kategorie 2B002 der Dual-Use-Liste faellt.
- Chemiehersteller muss Exportkontrollstatus eines Vorlaeuferchemikals klaren; CWC-Bezug geprueft.
- Ruestungsunternehmen exportiert Bauelemente; Abgrenzung EG-Dual-Use zu Kriegswaffe unklar.

## Erste Schritte

1. Produkt technisch vollstaendig beschreiben: Funktion, Parameter, Betriebsbedingungen, Software.
2. Gueterliste systematisch durchsuchen: Anhang I VO (EU) 2021/821, Kategorien 0-9, alle Untereintraege.
3. Technische Parameter mit Listenschwellenwerten abgleichen (z.B. Genauigkeit, Geschwindigkeit, Frequenz).
4. Kriegswaffenliste pruefen (KrWaffKontrG Anlage), Abgrenzung zu ML-Position des Wassenaar-Arrangements.
5. Bei Listentreffer: Eintrag genau dokumentieren mit Kategorie, Eintragsnummer und Schwellenwertvergleich.
6. Ergebnis als Klassifizierungsgutachten dokumentieren; BAFA-Auskunftsverfahren bei Unsicherheit.

## Rechtsrahmen

- **Anhang I VO (EU) 2021/821**: EU-Dual-Use-Gueterliste, Kategorien EG0-EG9.
- **KrWaffKontrG Anlage Teil A/B**: Kriegswaffenliste Deutschland.
- **§ 1 KrWaffKontrG**: Genehmigungspflicht fuer Kriegswaffen.
- **AWV Anlage AL**: Nationale Ausfuhrliste (komplementaer zur EU-Liste).
- **Art. 3 VO (EU) 2021/821**: Genehmigungspflicht bei Listentreffer.

## Pruef-Raster

- [ ] Alle 10 Kategorien des Anhangs I VO (EU) 2021/821 systematisch durchsucht?
- [ ] Technische Parameter exakt mit Schwellenwerten verglichen?
- [ ] Kriegswaffenliste und Munitionsliste separat geprueft?
- [ ] Nationale Ausfuhrliste (AWV Anlage AL) beachtet?
- [ ] Abgrenzung EG-Dual-Use vs. ML-Gueter geklaert?
- [ ] Klassifizierungsergebnis mit Listenstelle und Begruendung dokumentiert?

## Typische Fallstricke

- Suche nach Produktbeschreibung ist unzureichend; nur Parametervergleich entscheidet.
- Softwarekomponenten und technische Unterstuetzung koennen hoher klassifiziert sein als die Hardware.
- Aenderungen der Gueterliste (jaehrliche Aktualisierung) werden nicht nachverfolgt.
- 'Entwickelt fuer' vs. 'geeignet fuer': Kriterium variiert je nach Listeneintrag.

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

Klassifizierungsgutachten mit Produktbeschreibung, systematischer Listenpruefung, Parametervergleich, Listentreffer oder Negativklassifizierung und BAFA-Auskunftsanfrage.

## Quellen

- [VO (EU) 2021/821 Anhang I auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Gueterlisten](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/Gueterlisten/gueterlisten_node.html)
- [KrWaffKontrG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/krwaffkontrg/index.html)
- [AWV Anlage AL](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 4. `aussenwirtschaft-icp-kontrollsystem`

**Fokus:** Aufbau und Auditierung eines Internal Compliance Programme (ICP) nach BAFA-Leitfaden und EU Best Practice Guidelines: Risikobasierte Struktur, Schluessel-Compliance-Elemente, Ausfuhrverantwortlicher, Screening-Prozesse, Dokumentation und Schulungspflichten. Output: ICP-Handbuch-Gliederung und Gap-Analyse.

# Internal Compliance Programme (ICP): Aufbau und Gap-Analyse

## Mandantenfall

- Mittelstaendischer Exporteur muss ICP als Voraussetzung fuer Globalausfuhrgenehmigung nachweisen.
- BAFA-Aussenpruefung beanstandet fehlendes ICP; Unternehmen hat 6 Monate zur Abhilfe.
- Konzern integriert neue Akquisition; ICP-Standards muessen harmonisiert und ausgerollt werden.

## Erste Schritte

1. BAFA-ICP-Leitfaden und EU-Leitfaden Best Practices herunterladen und Pflicht-Elemente identifizieren.
2. Ist-Stand des Unternehmens erheben: vorhandene Prozesse, Verantwortlichkeiten, IT-Systeme.
3. Gap-Analyse durchfuehren: welche Pflicht-Elemente fehlen oder sind unvollstaendig?
4. ICP-Handbuch-Gliederung erstellen mit allen 8 BAFA-Kernelementen.
5. Ausfuhrverantwortlichen benennen und Stellvertreterregelung schaffen.
6. Zeitplan fuer ICP-Implementierung und erste interne Revision festlegen.

## Rechtsrahmen

- **Art. 12 VO (EU) 2021/821**: ICP als Bedingung fuer globale Ausfuhrgenehmigungen.
- **BAFA-Merkblatt ICP**: 8 Kernelement-Anforderungen des BAFA.
- **§ 14 AWG**: Auskunftspflicht gegenueber BAFA (Pruefrelevanz ICP).
- **AWV §§ 68 ff.**: Aufzeichnungspflichten im Ausfuhrverfahren.
- **§ 130 OWiG**: Aufsichtspflichtverletzung bei fehlendem Compliance-System.

## Pruef-Raster

- [ ] Ausfuhrverantwortlicher schriftlich benannt und Stellvertreter geregelt?
- [ ] Risikoanalyse dokumentiert und aktuell?
- [ ] Screening-Prozess fuer Kunden und Endverwender beschrieben?
- [ ] Schulungen fuer exportkontrollrelevante Mitarbeiter nachgewiesen?
- [ ] Dokumentation und Archivierung nach AWV sichergestellt?
- [ ] Internes Audit-Verfahren und Korrekturmassnahmenprozess etabliert?
- [ ] Red-Flag-Eskalationsprozess definiert?

## Typische Fallstricke

- ICP auf Papier ohne gelebte Prozesse schutzt nicht bei BAFA-Aussenpruefung.
- Ausfuhrverantwortlicher hat keine ausreichende Entscheidungsbefugnis; ICP-Wirkung entfallt.
- Schulungsnachweis fehlt; Teilnahmelisten und Inhaltsdokumentation noetig.
- ICP deckt Technologietransfer und Dienstleistungen nicht ab, nur Warenausfuhr.

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

ICP-Handbuch-Gliederung nach BAFA-Standard, Gap-Analyse mit Priorisierung, Umsetzungsplan und Dokumentationsvorlagen fuer Screening und Entscheidungen.

## Quellen

- [BAFA ICP-Merkblatt](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Interne_Compliance/interne_compliance_node.html)
- [EU Best Practice Guidelines ICP](https://ec.europa.eu/trade/import-and-export-rules/export-from-eu/dual-use-controls/index_en.htm)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
