---
name: nichtpraeferenzieller-ursprung-ofac-sdn-post
description: "Nichtpraeferenzieller Ursprung Ofac SDN Post: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nichtpraeferenzieller Ursprung Ofac SDN Post

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Nichtpraeferenzieller Ursprung Ofac SDN Post** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-nichtpraeferenzieller-ursprung-made-in` | Nichtpraeferenzieller Ursprung nach UZK Art. 59-61 und UZK-DA Art. 31-36: Bestimmung durch wesentliche Be- oder Verarbeitung, Listenregeln fuer HS-Wechsel, Wertschwellen und Letzte-wesentliche-Bearbeitung-Kriterium. Bedeutung fuer Made-in-Bezeichnung im Handelsrecht, Antidumping-Umgehungspruefung und Nachweispflichten gegenueber Zollbehoerden. Output: Ursprungsgutachten und Nachweispaket fuer Hauptzollamt. |
| `aussenwirtschaft-ofac-sdn-non-sdn` | US-OFAC-Sanktionsregime fuer deutsche und EU-Unternehmen: SDN List, sectoral sanctions (SSI-List), secondary sanctions-Risiken, US-Nexus bei Dollar-Transaktionen und US-Technologie, Blocking-Statute VO (EG) 2271/96 als Gegengewicht. Output: US-Sanktions-Touchpoint-Analyse und Handlungsempfehlung. |
| `aussenwirtschaft-post-merger-icp-integration` | Integration des Internal Compliance Programme nach M&A: Harmonisierung von ICP-Standards zwischen Kaeufer und Zielunternehmen, Risikolucken-Schliessen, Schulungsrollout fuer neue Mitarbeiter, BAFA-Mitteilung bei Inhaberwechsel exportkontrollrelevanter Genehmigungen. Output: ICP-Integrationsplan und Meilensteintabelle. |
| `aussenwirtschaft-praeferenzkalkulation-lieferantenerklaerung` | Berechnung und Dokumentation des praeferenziellen Ursprungs nach UZK Art. 64 und DA Anhang 22-03: Listenregeln, HS-Wechsel, Wertschwell, vollstaendige Gewinnung, Kumulierungsmoeglichkeiten, Lieferantenerklaerung nach VO (EU) 1207/2001 und VO (EU) 2015/2447. Output: Ursprungskalkulation und Lieferantenerklaerungsvorlage. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Nichtpraeferenzieller Ursprung Ofac SDN Post**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-nichtpraeferenzieller-ursprung-made-in`

**Fokus:** Nichtpraeferenzieller Ursprung nach UZK Art. 59-61 und UZK-DA Art. 31-36: Bestimmung durch wesentliche Be- oder Verarbeitung, Listenregeln fuer HS-Wechsel, Wertschwellen und Letzte-wesentliche-Bearbeitung-Kriterium. Bedeutung fuer Made-in-Bezeichnung im Handelsrecht, Antidumping-Umgehungspruefung und Nachweispflichten gegenueber Zollbehoerden. Output: Ursprungsgutachten und Nachweispaket fuer Hauptzollamt.

# Nichtpraeferenzieller Ursprung und Made-in-Bezeichnung: Berechnung und Nachweis

## Mandantenfall

- Maschinenbauer assembliert in Deutschland Teile aus China; 'Made in Germany' korrekt verwendbar?
- Antidumping-Massnahmen auf Ware aus China; Ursprung nach Zusammenbau in Polen wird geprueft.
- Exporteur verwendet 'Made in EU' Kennzeichnung; Ursprungsberechnung fuer UZK-Zwecke geprueft.

## Erste Schritte

1. HS-Code der Fertigware bestimmen.
2. Ursprungsregel fuer den HS-Code nach UZK-DA Anhang 22-01 ermitteln (HS-Wechsel oder Wertschwell).
3. Wertschwell-Berechnung wenn Wertkriterium anwendbar (Nicht-Ursprungsmaterialienanteil am EXW-Preis).
4. Letzte wesentliche Bearbeitung oder Verarbeitung feststellen.
5. 'Made in Germany' Zulassigkeit pruefen: Kernprozess und wesentliche Teile in Deutschland.
6. Ursprungsgutachten mit HS-Code-Wechsel-Dokumentation oder Wertschwell-Berechnung erstellen.

## Rechtsrahmen

- **UZK Art. 59-61**: Nichtpraeferenzieller Ursprung, Definition und Kriterien.
- **UZK-DA Art. 31-36**: Bearbeitungs- und Verarbeitungsregeln fuer nichtpraeferenziellen Ursprung.
- **UZK-DA Anhang 22-01**: Listenregeln HS-Code-Wechsel fuer nichtpraeferenziellen Ursprung.
- **VO (EG) 1215/2009**: Antidumping-Ursprungsregeln (Referenz).
- **UWG § 5**: Irrefuehrende 'Made in'-Angaben als Wettbewerbsverstoß.**

## Pruef-Raster

- [ ] HS-Code der Fertigware eindeutig bestimmt?
- [ ] Ursprungsregel nach UZK-DA Anhang 22-01 fuer HS-Code abgerufen?
- [ ] HS-Wechsel-Anforderung bei allen Nicht-Ursprungsmaterialien geprueft?
- [ ] Wertschwell-Berechnung mit EXW-Preis und Nicht-Ursprungsmaterialienwert?
- [ ] 'Made in'-Bezeichnung wettbewerbsrechtlich zulassig?
- [ ] Ursprungsgutachten vollstaendig und archiviert?

## Typische Fallstricke

- Einfaches Assemblieren von Fertigteilen (Minimal Operations) verleiht keinen Ursprung.
- HS-Wechsel muss fuer ALLE Nicht-Ursprungsmaterialien erfolgen, nicht nur die wichtigsten.
- 'Made in Germany' ist gesetzlich nicht definiert; Irrefuehrungs-Risiko nach UWG.
- Antidumping-Umgehung durch Ursprungsverlagerung loest erhoehte Zollpruefung aus.

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

Ursprungsgutachten mit HS-Code-Analyse, Listenregelnachweis, Wertschwell-Berechnung und Empfehlung zur 'Made in'-Kennzeichnung.

## Quellen

- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [UZK-DA Anhang 22-01](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de Ursprung](https://www.zoll.de/DE/Fachthemen/Zoelle/Ursprung-Praeferenzen/ursprung-praeferenzen_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 2. `aussenwirtschaft-ofac-sdn-non-sdn`

**Fokus:** US-OFAC-Sanktionsregime fuer deutsche und EU-Unternehmen: SDN List, sectoral sanctions (SSI-List), secondary sanctions-Risiken, US-Nexus bei Dollar-Transaktionen und US-Technologie, Blocking-Statute VO (EG) 2271/96 als Gegengewicht. Output: US-Sanktions-Touchpoint-Analyse und Handlungsempfehlung.

# US-OFAC-Sanktionen fuer EU-Unternehmen: SDN, Sektoral und Secondary Sanctions

## Mandantenfall

- Deutsches Unternehmen kauft Oel aus Drittland; Frachtschiff steht auf OFAC-SDN-Liste.
- EU-Bank wickelt USD-Zahlung ab; Gegenpartei auf SSI-Liste; US-Korrespondenzbank blockiert.
- Blocker-Statute VO 2271/96: europaeischer Tochterbetrieb von US-Muttergesellschaft weigert sich, Verbot zu befolgen.

## Erste Schritte

1. US-Nexus feststellen: USD-Transaktion, US-Technologie (EAR/ITAR), US-Person/Unternehmen beteiligt?
2. SDN-Liste und SSI-Liste (OFAC) auf alle Transaktionsparteien pruefen.
3. Sektoral sanctions (SSI) pruefen: welche Finanzierungsformen sind fuer SSI-Personen verboten?
4. Secondary-sanctions-Risiko bewerten: Exposure fuer Drittland-Unternehmen.
5. EU-Blocking-Statute VO 2271/96 pruefen: gilt es fuer den Sachverhalt? Pflicht zur Befolgung des US-Verbots?
6. Handlungsempfehlung: Transaktion fortsetzen, anpassen oder abbrechen; Kommunikationsstrategie.

## Rechtsrahmen

- **50 CFR Parts 500 ff. (OFAC-Vorschriften)**: Grundlage fuer SDN und Sektorsanktionen.
- **VO (EG) 2271/96**: EU-Blocking-Statute gegen extraterritoriale US-Sanktionen.
- **VO (EU) 2018/1100**: Aktualisierung des Blocking-Statutes fuer Iran-Sanktionen.
- **AWG § 4 Abs. 1 Nr. 4**: Schutz wesentlicher Sicherheitsinteressen als Rechtsgrundlage.
- **§ 18 AWG**: Strafbarkeit bei Sanktionsverstoss nach deutschem Recht.

## Pruef-Raster

- [ ] US-Nexus (USD, US-Person, US-Technologie) identifiziert?
- [ ] SDN-Liste und SSI-Liste fuer alle Parteien geprueft?
- [ ] Sektorsanktionen fuer relevante Finanzierungsform analysiert?
- [ ] Secondary-sanctions-Risiko quantifiziert?
- [ ] EU-Blocking-Statute Anwendbarkeit geprueft?
- [ ] Handlungsempfehlung mit Risiko-Abwaegung dokumentiert?

## Typische Fallstricke

- SDN und SSI sind verschiedene Listen; SSI-Verbote sind enger als SDN-Totalverbot.
- USD-Clearing durch US-Korrespondenzbank schafft automatisch US-Jurisdiktion.
- Blocking-Statute und US-Recht kollidieren; Unternehmen in echtem Dilemma ohne rechtssichere Loesung.
- Secondary sanctions treffen EU-Unternehmen auch ohne direkten US-Kontakt (Iran CAATSA).

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

US-Sanktions-Touchpoint-Analyse mit SDN/SSI-Pruefprotokoll, Secondary-sanctions-Risikobewertung, Blocking-Statute-Analyse und Handlungsempfehlung.

## Quellen

- [OFAC Sanctions List](https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/default.aspx)
- [VO (EG) 2271/96 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31996R2271)
- [BAFA US-Sanktionen](https://www.bafa.de/DE/Aussenwirtschaft/Finanzsanktionen/finanzsanktionen_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 3. `aussenwirtschaft-post-merger-icp-integration`

**Fokus:** Integration des Internal Compliance Programme nach M&A: Harmonisierung von ICP-Standards zwischen Kaeufer und Zielunternehmen, Risikolucken-Schliessen, Schulungsrollout fuer neue Mitarbeiter, BAFA-Mitteilung bei Inhaberwechsel exportkontrollrelevanter Genehmigungen. Output: ICP-Integrationsplan und Meilensteintabelle.

# Post-Merger ICP-Integration: Harmonisierung und Lueckenschliessung

## Mandantenfall

- Kaeufer hat starkes ICP; Zielunternehmen hat nur rudimentaere Exportkontroll-Prozesse; 6-Monate-Plan.
- Genehmigungen des Zielunternehmens (BAFA-Genehmigungen) laufen auf alten Rechtstraeger; Uebertragung?
- Konzernweite ICP-Vereinheitlichung nach Auslandsaqkuisition in Drittland.

## Erste Schritte

1. ICP-Gap-Analyse zwischen Kaeufer-Standard und Zielunternehmen durchfuehren.
2. Kritische Luecken identifizieren: fehlende Gueterklassifizierungen, kein Sanktionsscreening, kein Ausfuhrverantwortlicher.
3. BAFA ueber relevante Aenderungen (Inhaberwechsel, Umstrukturierung) informieren; Genehmigungsuebertragung pruefen.
4. Integrationsplan mit Meilensteinen: sofortige Massnahmen, 3 Monate, 6 Monate.
5. Schulungsrollout fuer alle exportkontrollrelevanten Mitarbeiter des Zielunternehmens planen.
6. Gemeinsames ICP-Handbuch verabschieden und System-Integration (ERP, Screening-Tool) vorantreiben.

## Rechtsrahmen

- **Art. 12 VO (EU) 2021/821**: ICP als Bedingung fuer Globalgenehmigungen.
- **AWG § 18**: Fortlaufende Strafbarkeit des Rechtsnachfolgers bei Verstossen.
- **AWV §§ 68 ff.**: Aufzeichnungspflichten unveraendert nach Inhaberwechsel.
- **§ 25 UmwG**: Gesamtrechtsnachfolge und Haftungswirkung.
- **§ 130 OWiG**: Aufsichtspflichtverletzung als Bussgeltatbestand.**

## Pruef-Raster

- [ ] ICP-Gap-Analyse vollstaendig durchgefuehrt?
- [ ] BAFA ueber Inhaberwechsel und Genehmigungsaenderungen informiert?
- [ ] Kritische Sofortmassnahmen innerhalb erster 30 Tage eingeleitet?
- [ ] Schulungsplan fuer neue Mitarbeiter konkret terminiert?
- [ ] Integrationsplan mit Meilensteinen und Verantwortlichen verabschiedet?
- [ ] Gemeinsames ICP-Handbuch erstellt?

## Typische Fallstricke

- BAFA-Genehmigungen erlischen bei Inhaberwechsel; neue Genehmigung erforderlich.
- Mitarbeiter des Zielunternehmens kennen Exportkontrollpflichten nicht; hohes Risiko in Uebergangsphase.
- ICP-Luecken aus Zielunternehmen werden unsichtbar weiter gelebt.
- US-ITAR-Daten im Zielunternehmen erfordern US-DDTC-Genehmigung bei Uebertragung an EU-Erwerber.

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

ICP-Gap-Analyse, Integrationsplan mit Meilensteinen, Schulungsrollout-Plan und Vorlage BAFA-Mitteilung bei Inhaberwechsel.

## Quellen

- [BAFA ICP-Merkblatt](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Interne_Compliance/interne_compliance_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [UmwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/umwg_1994/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 4. `aussenwirtschaft-praeferenzkalkulation-lieferantenerklaerung`

**Fokus:** Berechnung und Dokumentation des praeferenziellen Ursprungs nach UZK Art. 64 und DA Anhang 22-03: Listenregeln, HS-Wechsel, Wertschwell, vollstaendige Gewinnung, Kumulierungsmoeglichkeiten, Lieferantenerklaerung nach VO (EU) 1207/2001 und VO (EU) 2015/2447. Output: Ursprungskalkulation und Lieferantenerklaerungsvorlage.

# Praeferenzkalkulation und Lieferantenerklaerung: Nachweis des Praeferenzursprungs

## Mandantenfall

- Exporteur nach Suedkorea (KOREU) muss praeferenziellen EU-Ursprung fuer Tarifvorteil nachweisen.
- Lieferant gibt Lieferantenerklaerung ab; Nachverifizierungsanfrage des Zollbehorde in Japan.
- Unternehmen hat Zulieferer in mehreren EU-Laendern; bilaterale Kumulierung nach GSP-Regeln.

## Erste Schritte

1. Handelsabkommen mit Bestimmungsland identifizieren (KOREU, CETA, EU-UK, EPA) und Ursprungsprotokoll abrufen.
2. Listenregel fuer HS-Code der Ware im Ursprungsprotokoll nachschlagen.
3. Stuckliste (BOM) mit Ursprung aller Materialien erstellen.
4. Listenregel anwenden: HS-Wechsel und/oder Wertschwell-Berechnung.
5. Kumulierungsmoeglichkeiten pruefen (bilateral, diagonal, vollstaendig).
6. Lieferantenerklaerung nach VO (EU) 1207/2001 oder Langzeit-Lieferantenerklaerung erstellen.

## Rechtsrahmen

- **UZK Art. 64**: Praeferenzieller Ursprung und Handelsabkommen.
- **UZK-DA Anhang 22-03**: Ursprungsregeln fuer allgemeines Praeferenzsystem.
- **VO (EU) 1207/2001**: Lieferantenerklaerungen; Form und Inhalt.
- **VO (EU) 2015/2447 Art. 57-66**: Ursprungsnachweis und REX-System.
- **UZK Art. 62**: Ursprungsnachweis fuer zollbefreiten Import.**

## Pruef-Raster

- [ ] Handelsabkommen und Ursprungsprotokoll fuer Bestimmungsland korrekt identifiziert?
- [ ] Listenregel fuer HS-Code korrekt angewendet?
- [ ] Stuckliste vollstaendig und Ursprung aller Materialien belegt?
- [ ] Kumulierungsmoeglichkeiten geprueft?
- [ ] Lieferantenerklaerung form- und fristgerecht erstellt?
- [ ] Nachverifizierungs-Anfragen bearbeitbar (Beleglage vorhanden)?

## Typische Fallstricke

- Falsche Wertschwell-Berechnung: EXW-Preis statt Fabrikhofpreis verwendet.
- Ursprungsnachweis erloschen; Langzeit-Lieferantenerklaerung verfallen ohne Erneuerung.
- Kumulierungspartner hat Ursprung nicht korrekt berechnet; Fehler setzt sich fort.
- Nachverifizierung im Bestimmungsland: fehlende Beleglage fuehrt zu Zollnacherhebung.

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

Ursprungskalkulation mit BOM-Analyse und Listenregelnachweis, Lieferantenerklaerungsvorlage, Kumulierungsmatrix und Nachverifizierungs-Handbuch.

## Quellen

- [UZK-DA Anhang 22-03 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [VO (EU) 1207/2001 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32001R1207)
- [Zoll.de Praeferenzrecht](https://www.zoll.de/DE/Fachthemen/Zoelle/Praeferenzrecht/praeferenzrecht_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
