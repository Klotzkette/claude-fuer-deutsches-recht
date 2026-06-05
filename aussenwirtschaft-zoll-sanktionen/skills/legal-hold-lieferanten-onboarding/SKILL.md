---
name: legal-hold-lieferanten-onboarding
description: "Legal Hold Lieferanten Onboarding: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Legal Hold Lieferanten Onboarding

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Legal Hold Lieferanten Onboarding** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-legal-hold-datenextraktion` | Legal Hold und digitale Datenextraktion bei Exportkontroll- und Sanktionsermittlungen: Sicherung von ATLAS-Daten, ERP-Exportdaten, E-Mail-Archiven und Zollanmeldungen, DSGVO-Konformitaet der Datensicherung, eDiscovery-Anforderungen bei US-Behoerden. Output: Legal-Hold-Anordnung und Datensicherungsprotokoll. |
| `aussenwirtschaft-lieferanten-onboarding-aussenhandel` | Exportkontroll- und sanktionsrechtliches Onboarding neuer Lieferanten: KYC-Lieferantenpruefung, Sanktionslistenscreening, Herkunftsland-Compliance, Lieferantenerklaerung fuer praeferenzielle Behandlung, Sorgfaltspflichten nach LkSG. Output: Lieferanten-Onboarding-Paket und Risikoklassifizierung. |
| `aussenwirtschaft-lieferkettensorgfalt-aussenhandel` | Lieferkettensorgfaltspflichten im Aussenwirtschaftskontext nach LkSG und EU-Lieferkettengesetz (CSDDD): Risikoanalyse im Aussenhandel, Menschenrechtspruefung bei Importguetererzeugern, Sanktions-Ueberschneidungen mit LkSG-Pflichten und Dokumentationsanforderungen. Output: LkSG-Risikomatrix fuer Import-Lieferkette. |
| `aussenwirtschaft-ma-sanctions-export-dd` | Exportkontroll- und Sanktions-Due-Diligence bei M&A-Transaktionen: Identifizierung von Sanktionsexposure des Zielunternehmens, Exportkontrollverstoss-Historizitaet, ICP-Qualitaet, Haftungsrisiken und Vertragsgestaltung (Rep und Warranties, Ruecktrittsrechte). Output: M&A-Exportkontroll-DD-Bericht. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Legal Hold Lieferanten Onboarding**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-legal-hold-datenextraktion`

**Fokus:** Legal Hold und digitale Datenextraktion bei Exportkontroll- und Sanktionsermittlungen: Sicherung von ATLAS-Daten, ERP-Exportdaten, E-Mail-Archiven und Zollanmeldungen, DSGVO-Konformitaet der Datensicherung, eDiscovery-Anforderungen bei US-Behoerden. Output: Legal-Hold-Anordnung und Datensicherungsprotokoll.

# Legal Hold und Datenextraktion bei Aussenwirtschafts-Ermittlungen

## Mandantenfall

- BAFA kuendigt Aussenpruefung an; Legal Hold fuer alle Exportdaten der letzten 5 Jahre notwendig.
- OFAC-Anfrage zu Transaktionen; US-eDiscovery-Standards und deutsches Datenschutzrecht kollidieren.
- Interne Investigation nach Hinweisgeber-Meldung; IT-forensische Sicherung vor regulaerer Loeschung noetig.

## Erste Schritte

1. Legal-Hold-Anordnung formulieren und an IT, Compliance, Archiv und betroffene Abteilungen senden.
2. Datenkategorien definieren: ATLAS-Daten, ERP-Exportmodule, E-Mails, Vertraege, EUC, Sanktionsscreening-Logs.
3. Technische Sicherungsmassnahmen einrichten: Backup-Stopp fuer relevante Datenbereiche.
4. DSGVO-Rechtsgrundlage fuer Datensicherung pruefen (Art. 6 Abs. 1 lit. c fuer gesetzliche Pflicht).
5. Bei US-eDiscovery: Datenschutzkonforme Transfer-Grundlage beachten (SCCs, DSGVO Art. 49).
6. Protokollierung der gesicherten Datenbestaende mit Hash-Werten fuer Integritaetssicherung.

## Rechtsrahmen

- **AWV § 24**: Aufbewahrungspflicht fuer Ausfuhrunterlagen (10 Jahre).
- **UZK Art. 51**: Aufbewahrungspflicht fuer Zollanmeldungen.
- **DSGVO Art. 6**: Rechtsgrundlage fuer Datensicherung.
- **§ 146 AO**: Buchfuehrungsunterlagen-Aufbewahrungspflicht.
- **§ 97 StPO**: Beschlagnahmefreiheit anwaltlicher Unterlagen.

## Pruef-Raster

- [ ] Legal-Hold-Anordnung alle relevante Datenkategorien erfassend?
- [ ] IT-Sicherungsmassnahmen zeitnah eingeleitet?
- [ ] DSGVO-Rechtsgrundlage fuer Datenzugriff geprueft?
- [ ] US-eDiscovery-Anforderungen mit deutschem Datenschutzrecht abgestimmt?
- [ ] Integritaets-Hash-Werte fuer gesicherte Datenbestaende erstellt?
- [ ] Aufbewahrungsfristen (AWV 10 Jahre) gegen Legal-Hold-Anforderungen abgeglichen?

## Typische Fallstricke

- Legal Hold zu spaet: regulaere Loeschroutinen haben Daten vernichtet.
- US-eDiscovery und DSGVO kollidieren direkt; ohne datenschutzkonforme Grundlage keine Uebertragung.
- Hash-Werte fehlen; Integritaet der gesicherten Daten nicht nachweisbar.
- ERP-Daten enthalten keine Exportkontroll-spezifischen Felder; separate ATLAS-Sicherung noetig.

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

Legal-Hold-Anordnung, Datenkategorie-Inventar, IT-Sicherungsprotokoll mit Hash-Werten, DSGVO-Pruefvermerk und eDiscovery-Transfergrundlage-Analyse.

## Quellen

- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [UZK Art. 51 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [DSGVO auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679)
- [AO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/index.html)

## 2. `aussenwirtschaft-lieferanten-onboarding-aussenhandel`

**Fokus:** Exportkontroll- und sanktionsrechtliches Onboarding neuer Lieferanten: KYC-Lieferantenpruefung, Sanktionslistenscreening, Herkunftsland-Compliance, Lieferantenerklaerung fuer praeferenzielle Behandlung, Sorgfaltspflichten nach LkSG. Output: Lieferanten-Onboarding-Paket und Risikoklassifizierung.

# Lieferanten-Onboarding: Aussenwirtschaftliche Compliance und Sanktionspruefung

## Mandantenfall

- Einkauf moechte neuen Lieferanten aus Tuerkei aufnehmen; Sanktions- und Dual-Use-Weiterlieferungsrisiko.
- Lieferant aus China soll Vorprodukte fuer Dual-Use-Endprodukt liefern; Herkunft und Endverwendung pruefen.
- LkSG-Sorgfaltspflicht erfordert Lieferanten-Risikoanalyse auch fuer Aussenwirtschafts-Compliance.

## Erste Schritte

1. Lieferanten-Fragebogen erstellen: Identitaet, Eigentuemer, Sitz, Produkte, Herkunft der Vorprodukte.
2. Sanktionslistenscreening Lieferant und UBO-Kette.
3. Herkunftsland-Pruefung: Sanktionsbetroffenes Land? Umgehungsland?
4. Dual-Use-Vorprodukt-Check: Liefert der Lieferant Dual-Use-Gueter?
5. Lieferantenerklaerung fuer Praeferenzursprung anfordern und auf Plausibilitaet pruefen.
6. Risikoklassifizierung und periodisches Re-Screening-Intervall festlegen.

## Rechtsrahmen

- **VO (EU) 269/2014, 833/2014**: Bereitstellungsverbote fuer sanktionierten Lieferanten.
- **LkSG § 3 ff.**: Sorgfaltspflichten in Lieferketten inkl. aussenwirtschaftlicher Aspekte.
- **VO (EU) 2021/821 Art. 4**: Catch-All bei Kenntnislage aus Lieferantenbeziehung.
- **VO (EU) 952/2013 (UZK) Art. 62**: Praeferenzursprung und Lieferantenerklaerung.
- **GwG § 10**: Sorgfaltspflichten bei Geschaeftsbeziehungen.

## Pruef-Raster

- [ ] Lieferantenidentitaet und UBO vollstaendig verifiziert?
- [ ] Sanktionslistenscreening Lieferant und verbundene Unternehmen?
- [ ] Herkunftsland auf Sanktions- oder Umgehungsrisiken geprueft?
- [ ] Dual-Use-Charakter der Liefergueter bewertet?
- [ ] Lieferantenerklaerung fuer Praeferenzursprung vollstaendig?
- [ ] Risikoklassifizierung und Re-Screening-Intervall festgelegt?

## Typische Fallstricke

- Erstes Screening genuegt nicht; periodisches Re-Screening unverzichtbar.
- Lieferanten mit unverdaechtigen Produkten koennen sanktionierte Eigentuemer haben.
- Praeferenz-Lieferantenerklaerungen falsch oder verfallt; Nachzollrisiko.
- LkSG-Sorgfaltspflicht und Exportkontroll-KYC werden nicht integriert; Doppelaufwand.

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

Lieferanten-Onboarding-Paket (Fragebogen, Checkliste, Screening-Protokoll), Risikoklassifizierung und Re-Screening-Kalender.

## Quellen

- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [LkSG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/lksg/index.html)
- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [Zoll.de Ursprungserklaerungen](https://www.zoll.de/DE/Fachthemen/Zoelle/Praeferenzrecht/praeferenzrecht_node.html)

## 3. `aussenwirtschaft-lieferkettensorgfalt-aussenhandel`

**Fokus:** Lieferkettensorgfaltspflichten im Aussenwirtschaftskontext nach LkSG und EU-Lieferkettengesetz (CSDDD): Risikoanalyse im Aussenhandel, Menschenrechtspruefung bei Importguetererzeugern, Sanktions-Ueberschneidungen mit LkSG-Pflichten und Dokumentationsanforderungen. Output: LkSG-Risikomatrix fuer Import-Lieferkette.

# Lieferkettensorgfaltspflichten im Aussenhandel: LkSG und CSDDD

## Mandantenfall

- Importeur bezieht Textilien aus Bangladesch; LkSG-Risikoanalyse und Massnahmenplan erforderlich.
- Elektronikhersteller importiert Rohstoffe aus Kongo (Mineralien); Konfliktmineralien und LkSG-Pflichten.
- CSDDD-Umsetzung erfordert Due Diligence fuer gesamte Lieferkette inkl. Unterlieferanten.

## Erste Schritte

1. LkSG-Pflichtenzeitplan pruefen: Ab wann anwendbar (Mitarbeiterzahl) fuer das Unternehmen?
2. Risikobranchen und Hochrisikolaender fuer Import-Lieferkette identifizieren.
3. Abstracted Due Diligence: direkte Lieferanten bewerten (Tier 1); Tier-2-Priorierung.
4. Praezisierte Risikoanalyse bei Hochrisikobranchen (Textil, Elektronik, Rohstoffe).
5. Praventionsmassnahmen und Abhilfemassnahmen dokumentieren.
6. Beschwerdemechanismus einrichten und Berichtspflicht nach § 10 LkSG erfuellen.

## Rechtsrahmen

- **LkSG §§ 3-10**: Sorgfaltspflichten, Risikoanalyse, Massnahmen und Berichtspflicht.
- **EU-CSDDD (2024/1760)**: EU-weite Sorgfaltspflichten ab Umsetzungsfrist.
- **VO (EU) 2017/821**: Konfliktmineralien-Verordnung fuer bestimmte Erze.
- **§ 24 LkSG**: Bussgeldbewehrung bei Verstoss gegen Sorgfaltspflichten.
- **VO (EU) 2021/821 Art. 4**: Schnittstelle Dual-Use-Catch-All zu LkSG.**

## Pruef-Raster

- [ ] LkSG-Anwendbarkeit geprueft (Mitarbeiterzahl, Umsatz)?
- [ ] Risikoanalyse fuer Import-Lieferkette vollstaendig und dokumentiert?
- [ ] Hochrisikolieferanten identifiziert und mit verstaerkter Sorgfalt geprueft?
- [ ] Massnahmenplan fuer identifizierte Risiken vorhanden?
- [ ] Beschwerdemechanismus implementiert?
- [ ] Jahresbericht nach § 10 LkSG erstellt und veroeffentlicht?

## Typische Fallstricke

- LkSG und Exportkontroll-KYC werden unabgestimmt parallel betrieben.
- Tier-2-Lieferanten werden pauschal ignoriert; Hochrisiko-Positionen dort.
- Berichtspflicht wird als Checklist-Uebung behandelt; inhaltliche Substanz fehlt.
- CSDDD-Anforderungen ueber LkSG hinaus werden unterschaetzt.

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

LkSG-Risikomatrix fuer Import-Lieferkette, Massnahmenplan, Beschwerdemechanismus-Beschreibung und Jahresbericht-Gliederung.

## Quellen

- [LkSG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/lksg/index.html)
- [EU-CSDDD auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L1760)
- [VO (EU) 2017/821 Konfliktmineralien](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R0821)
- [BAFA LkSG](https://www.bafa.de/DE/Lieferketten/lieferketten_node.html)

## 4. `aussenwirtschaft-ma-sanctions-export-dd`

**Fokus:** Exportkontroll- und Sanktions-Due-Diligence bei M&A-Transaktionen: Identifizierung von Sanktionsexposure des Zielunternehmens, Exportkontrollverstoss-Historizitaet, ICP-Qualitaet, Haftungsrisiken und Vertragsgestaltung (Rep und Warranties, Ruecktrittsrechte). Output: M&A-Exportkontroll-DD-Bericht.

# M und A Exportkontroll- und Sanktions-Due-Diligence

## Mandantenfall

- Private-Equity kauft deutschen Maschinenbauer; DD zeigt ungeloeste BAFA-Pruefung aus Vorjahr.
- Strategischer Erwerber plant Akquisition eines US-Lizenztechnologie-Unternehmens mit ITAR-Daten.
- Zielunternehmen hat erhebliche Russland-Kundenbeziehungen; Sanktionsexposure-Quantifizierung noetig.

## Erste Schritte

1. Exportkontroll- und Sanktions-DD-Fragebogen an Zielunternehmen senden.
2. Exportprofile pruefen: Hauptmaerkte, Produktkategorien, Genehmigungshistorie, BAFA-Kontakte.
3. Historische BAFA-Pruefungen und Sanktionsscreening-Prozesse analysieren.
4. ICP-Qualitaet bewerten: Struktur, gelebte Praxis, Luecken.
5. Sanktionsexposure quantifizieren: aktive Kundenbeziehungen, laufende Vertraege, offene Verbindlichkeiten.
6. M&A-Reps-and-Warranties und Ruecktrittsklauseln fuer Exportkontroll-Risiken formulieren.

## Rechtsrahmen

- **AWG § 18**: Strafbarkeit; Rechtsnachfolge-Haftung bei Umwandlungen.
- **§ 25 UmwG**: Haftung des Rechtsnachfolgers bei Gesamtrechtsnachfolge.
- **VO (EU) 833/2014, 269/2014**: Aktuelle Sanktionslage als DD-Massstab.
- **§ 130 OWiG**: Organschaftliche Verantwortung des Erwerbers.
- **§ 438 BGB**: Maengelansprueche bei versteckten Exportkontrollverstossen.

## Pruef-Raster

- [ ] Exportprofile und Hauptmaerkte des Zielunternehmens vollstaendig erfasst?
- [ ] BAFA-Pruefungshistorie und Ergebnisse analysiert?
- [ ] ICP-Qualitaet bewertet und Luecken dokumentiert?
- [ ] Sanktionsexposure quantifiziert (Kundenbeziehungen, Vertraege)?
- [ ] Haftungsrisiken fuer Kaeufer bewertet und in Kaufpreis reflektiert?
- [ ] M&A-Reps-and-Warranties fuer Exportkontrollrisiken formuliert?

## Typische Fallstricke

- Vererbte BAFA-Pruefungen werden nach Closing zu Kaeufer-Problem.
- ITAR-contamination: US-Technologie im Zielunternehmen uebertraegt sich auf Kaeufer (ITAR 22 CFR 127.1).
- Historische Verstoss-Potenziale (Verjaeahrungsfristen beachten; AWG 5 Jahre) koennen nach Closing aufschlagen.
- ICP-Luecken bedeuten kontinuierliches Risiko; Integrations-ICP-Plan erforderlich.

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

M&A-Exportkontroll-DD-Bericht mit Risikoklassifizierung, ICP-Bewertung, Sanktionsexposure-Quantifizierung und Transaktionsgestaltungsempfehlungen.

## Quellen

- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [BAFA Ausfuhrkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
- [UmwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/umwg_1994/index.html)
