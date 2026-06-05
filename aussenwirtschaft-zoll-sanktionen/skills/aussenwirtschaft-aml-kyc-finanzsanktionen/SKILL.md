---
name: aussenwirtschaft-aml-kyc-finanzsanktionen
description: "AML KYC Finanzsanktionen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# AML KYC Finanzsanktionen

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **AML KYC Finanzsanktionen** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-aml-kyc-sanktionen` | Schnittstelle von AML/KYC-Pflichten und Sanktionsrecht: Risikobasierte Kundenpruefung nach GwG (§§ 10-17 GwG) kombiniert mit Sanktionsscreening nach EU-Finanzsanktionsrecht (VO 269/2014 und andere). Identifizierung wirtschaftlich Berechtigter (UBO), Pruefung von PEP-Status und Hochrisikoindikatoren. Output: KYC-Dossier mit Sanktionsabklaerungsvermerk und Eskalationspfad. |
| `aussenwirtschaft-finanzsanktionen-eigentum-kontrolle` | Pruefung von Eigentum und Kontrolle sanktionierter Personen bei juristischen Personen nach Art. 2 Abs. 1 lit. a VO (EU) 269/2014 und EU-Leitlinien zur 50-%-Regel: Mehrheitsbesitz, mittelbare Kontrolle, Treuhandstrukturen. Umgehungsrisiken bei Tochtergesellschaften und Geschaeftspartnern. Output: UBO-Analysevermerk. |
| `aussenwirtschaft-sanktionen-embargos` | Ueberblick und Triage ueber EU-Sanktionen und Embargos: Russland (VO 833/2014 und 269/2014), Iran (VO 267/2012), Belarus (VO 765/2006), Nordkorea, Myanmar, Syrien. Bereitstellungsverbote, Sektorensanktionen, Finanzsanktionen und Reisebeschraenkungen. Output: Sanktionslage-Uebersicht und Erstbewertung. |
| `aussenwirtschaft-sanktionsscreening-fuzzy-match` | Technische und rechtliche Anforderungen an Sanktionslistenscreening mit Fuzzy-Matching: Schwellenwerte fuer Namensaehnlichkeit, Algorithmen (Levenshtein, phonetisch), False-Positive-Management, Dokumentation und Validierungspflicht des Screening-Tools nach EU-Sanktionsrecht. Output: Screening-Methodikbeschreibung und Validierungsprotokoll. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **AML KYC Finanzsanktionen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-aml-kyc-sanktionen`

**Fokus:** Schnittstelle von AML/KYC-Pflichten und Sanktionsrecht: Risikobasierte Kundenpruefung nach GwG (§§ 10-17 GwG) kombiniert mit Sanktionsscreening nach EU-Finanzsanktionsrecht (VO 269/2014 und andere). Identifizierung wirtschaftlich Berechtigter (UBO), Pruefung von PEP-Status und Hochrisikoindikatoren. Output: KYC-Dossier mit Sanktionsabklaerungsvermerk und Eskalationspfad.

# AML/KYC und Sanktionen: Risikobasierte Kundenpruefung und Sanktionsscreening

## Mandantenfall

- Bank erhalt Zahlungsauftrag aus UAE mit unklaren UBO-Angaben; Fragestellung Sanktions-Treffer moeglich?
- Handelsunternehmen onboardet neuen Kunden aus der Tuerkei; interne KYC-Abteilung fordert enhanced due diligence.
- Finanzdienstleister prueft, ob Russe mit Oligarchen-Nahbeziehung unter Art. 2 VO 269/2014 faellt.

## Erste Schritte

1. Identifizierungspflicht ausloesen: Ist Geschaeftsbeziehung gemaess §§ 10 GwG begruendet?
2. UBO-Ermittlung nach § 3 GwG und Art. 3 Nr. 6 4. EU-GwRL (AMLD4): Eigentums- und Kontrollstrukturen bis zum natuerllichen Endbeguenstigten aufloesen.
3. Sanktionsscreening in konsolidierter EU-Finanzsanktionsliste (OFAC, UK-HMT optional ergaenzend).
4. PEP-Status pruefen (§ 1 Abs. 12 GwG) und erweiterte Sorgfaltspflichten aktivieren.
5. Risikobewertung nach geldwaescherechtlicher Risikoanalyse erstellen.
6. Entscheidung: Kundenbeziehung freigeben, einschraenken oder ablehnen; Meldung an FIU pruefen.

## Rechtsrahmen

- **§§ 10-17 GwG**: Kundensorgfaltspflichten, UBO-Ermittlung, Hochrisikofaelle.
- **Art. 2 VO (EU) 269/2014**: Bereitstellungsverbot fuer gelistete Personen/Unternehmen (Russland-Sanktionen).
- **Art. 11 VO (EU) 269/2014**: Meldepflicht bei eingefrorenen Geldern.
- **§ 43 GwG**: Verdachtsmeldepflicht an FIU.
- **Zahlungsdiensteaufsichtsgesetz (ZAG)**: Erweiterter Anwendungsbereich fuer Zahlungsdienstleister.

## Pruef-Raster

- [ ] UBO vollstaendig und belegt ermittelt (25 %-Schwelle und Kontrollpruefung)?
- [ ] Sanktionsscreening mit Trefferprotokoll durchgefuehrt?
- [ ] PEP-Status und Hochrisikoindikatoren bewertet?
- [ ] Abweichende/unklare Angaben des Kunden dokumentiert?
- [ ] Risikoklasse korrekt eingestuft und Massnahmen angemessen?
- [ ] Meldepflicht an FIU geprueft?

## Typische Fallstricke

- Indirektes Eigentum ueber Offshore-Strukturen wird unterschaetzt; nur direkte Anteilseigner pruefen reicht nicht.
- 'Fuzzy Match' bei abweichender Schreibweise des Namens fuehrt zu Nichtentdeckung.
- PEP-Status laeuft nach Amt-Ende weiter (mindestens 12 Monate); kein automatischer Wegfall.
- Sanktions- und GwG-Pruefung werden organisatorisch getrennt durchgefuehrt und kommunizieren nicht.

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

KYC-Dossier mit UBO-Mapping, Sanktions-Trefferlog, PEP-Klassifizierung, Risikoampel und Freigabe-/Ablehnungsvermerk.

## Quellen

- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [VO (EU) 269/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [EU Finanzsanktionsliste (FSDB)](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [BaFin Merkblatt Geldwaeschegesetz](https://www.bafin.de/DE/Aufsicht/Geldwaeschebekaempfung/geldwaeschebekaempfung_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 2. `aussenwirtschaft-finanzsanktionen-eigentum-kontrolle`

**Fokus:** Pruefung von Eigentum und Kontrolle sanktionierter Personen bei juristischen Personen nach Art. 2 Abs. 1 lit. a VO (EU) 269/2014 und EU-Leitlinien zur 50-%-Regel: Mehrheitsbesitz, mittelbare Kontrolle, Treuhandstrukturen. Umgehungsrisiken bei Tochtergesellschaften und Geschaeftspartnern. Output: UBO-Analysevermerk.

# 50-Prozent-Regel bei Sanktionen: Eigentum, Kontrolle und Umgehungsrisiken

## Mandantenfall

- Lieferant eines deutschen Unternehmens ist zu 51 Prozent im Besitz einer sanktionierten russischen Bank.
- Immobilientransaktion: Kaeufer wird von Holdingstruktur gehalten, deren UBO sanktioniert ist.
- Konzerngesellschaft in Drittland hat sanktionierte Person im Aufsichtsrat mit Vetomacht.

## Erste Schritte

1. Alle juristischen Personen in der Transaktionskette identifizieren.
2. Eigentuemerstruktur bis zur natuerlichen Person oder staatlichen Entitaet verfolgen (UBO-Analyse).
3. 50-%-Schwelle nach Besitz und Kontrolle gesondert pruefen (Art. 2 VO 269/2014).
4. EU-Leitlinien zur Akkumulation von Eigentumsanteilen beachten.
5. Treuhandverhaeltnisse und Nominee-Strukturen aufdecken.
6. Ergebnis mit Quellenbelegen und Entscheidung dokumentieren.

## Rechtsrahmen

- **Art. 2 Abs. 1 VO (EU) 269/2014**: Bereitstellungsverbot fuer gelistete Personen und von ihnen kontrollierte Entitaeten.
- **EU-Leitlinien zu Art. 2 VO 269/2014**: Interpretation der 50-%-Regel bei Eigentum/Kontrolle.
- **VO (EU) 833/2014 Art. 11**: Eingefroren Gelder und Bereitstellungsverbot.
- **§ 3 GwG**: UBO-Definition und Transparenzpflicht.
- **§ 18 AWG**: Strafbarkeit bei Bereitstellung gegenueber sanktionierter Entitaet.

## Pruef-Raster

- [ ] UBO-Kette bis zur natuerlichen Person vollstaendig verfolgt?
- [ ] 50-%-Schwelle nach Eigentumsanteilen und Stimmrechten getrennt geprueft?
- [ ] Mittelbare Kontrolle (mehrstufige Holdingstrukturen) beruecksichtigt?
- [ ] Treuhand- und Nominee-Verhaeltnisse ausgeschlossen oder aufgedeckt?
- [ ] EU-Leitlinien zur Akkumulation konsultiert?
- [ ] Quellenstand und Abrufdatum dokumentiert?

## Typische Fallstricke

- Kontrolle ohne Mehrheitsbesitz (Veto, Vorstandsmandat) loest ebenfalls Bereitstellungsverbot aus.
- Sanktionierte Person haelt 25 % + eine weitere sanktionierte Person 26 % = zusammen ueber 50 %.
- Treuhandstrukturen verschleiern wirtschaftlich Berechtigten; Gegenverifizierung noetig.
- Tochtergesellschaften sanktionierter Banken in Drittlaendern nicht automatisch sanktioniert, aber Risiko hoch.

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

UBO-Analysevermerk mit Eigentumsdiagramm, 50-%-Regel-Pruefergebnis, Quellenprotokoll und Freigabe- oder Sperrentscheidung.

## Quellen

- [VO (EU) 269/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [EU-Leitlinien zu Eigentum/Kontrolle](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [BAFA Finanzsanktionen](https://www.bafa.de/DE/Aussenwirtschaft/Finanzsanktionen/finanzsanktionen_node.html)

## 3. `aussenwirtschaft-sanktionen-embargos`

**Fokus:** Ueberblick und Triage ueber EU-Sanktionen und Embargos: Russland (VO 833/2014 und 269/2014), Iran (VO 267/2012), Belarus (VO 765/2006), Nordkorea, Myanmar, Syrien. Bereitstellungsverbote, Sektorensanktionen, Finanzsanktionen und Reisebeschraenkungen. Output: Sanktionslage-Uebersicht und Erstbewertung.

# EU-Sanktionen und Embargos: Triage und Sanktionslage-Uebersicht

## Mandantenfall

- Neuer Lieferauftrag mit Gegenpartei aus Russland; welche Sanktionsverordnungen sind relevant?
- Zahlung aus iranischem Bankhandelsinstrument soll empfangen werden; Finanzsanktionen geprueft.
- Lieferung von Konsumgueter nach Belarus; Embargo oder Ausnahme?

## Erste Schritte

1. Sanktionsregime identifizieren: Land/Region, Rechtsgrundlage, Verordnung.
2. EU-Finanzsanktionsliste (FSAP) und ggf. nationale Listen auf Parteien pruefen.
3. Guetersanktionen pruefen: HS/KN-Code gegen Listen der relevanten Verordnung.
4. Sektorsanktionen pruefen: Energie, Finanzsektor, Transport, Dienstleistungen.
5. Ausnahmen und Ausnahmegenehmigungen sichten: humanitaere Ausnahme, Altvertraege.
6. Sanktionslage mit Datum protokollieren; Verordnung konsultiert.

## Rechtsrahmen

- **VO (EU) 833/2014 und 269/2014**: Russland-Embargo und Finanzsanktionen.
- **VO (EU) 267/2012**: Iran-Sanktionen und Finanzsanktionen.
- **VO (EU) 765/2006**: Belarus-Sanktionen.
- **VO (EU) 2017/1509**: Nordkorea-Sanktionen.
- **AWG § 4 Abs. 1 Nr. 3**: Nationale Ermaechtigung fuer Embargomassnahmen.**

## Pruef-Raster

- [ ] Sanktionsregime und anwendbare Verordnung identifiziert?
- [ ] Parteien gegen EU-Finanzsanktionsliste geprueft?
- [ ] Gueter gegen Sanktionsanhaenge der Verordnung geprueft?
- [ ] Sektorsanktionen fuer relevante Taetigkeitsbereiche geprueft?
- [ ] Ausnahmen und Genehmigungstatbestaende geprueft?
- [ ] Sanktionslage mit Quellenstand und Datum dokumentiert?

## Typische Fallstricke

- Sanktionspakete werden haufig aktualisiert; immer konsolidierte Fassung auf EUR-Lex nutzen.
- Ausnahmen sind eng gefasst; humanitaere Ausnahme gilt nicht pauschal.
- Guetersanktionen und Personensanktionen laufen parallel und unabhaengig voneinander.
- Keine veraltete Sanktionslage annehmen; Listing-Datum und Delistings pruefen.

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

Sanktionslage-Uebersicht mit Verordnung, Listenstand und Erstbewertung; Screening-Protokoll und Entscheidungsempfehlung.

## Quellen

- [EU-Finanzsanktionsliste FSAP](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [VO (EU) 267/2012 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R0267)
- [BAFA Finanzsanktionen](https://www.bafa.de/DE/Aussenwirtschaft/Finanzsanktionen/finanzsanktionen_node.html)

## 4. `aussenwirtschaft-sanktionsscreening-fuzzy-match`

**Fokus:** Technische und rechtliche Anforderungen an Sanktionslistenscreening mit Fuzzy-Matching: Schwellenwerte fuer Namensaehnlichkeit, Algorithmen (Levenshtein, phonetisch), False-Positive-Management, Dokumentation und Validierungspflicht des Screening-Tools nach EU-Sanktionsrecht. Output: Screening-Methodikbeschreibung und Validierungsprotokoll.

# Sanktionsscreening mit Fuzzy-Match: Methodik, Schwellenwerte und Validierung

## Mandantenfall

- Screening-Tool gibt 80 False Positives pro Tag aus; Compliance-Kapazitaet ueberlastet; Optimierung.
- Neues Screening-Tool wird implementiert; Validierung der Erkennungsleistung vor Go-Live.
- BAFA-Pruefung beanstandet, dass Screening-Schwellenwert zu hoch gesetzt war und Treffer verpasst wurden.

## Erste Schritte

1. Screening-Algorithmen des Tools dokumentieren (Levenshtein-Distanz, Soundex, Metaphon etc.).
2. Schwellenwerte fuer Namensaehnlichkeit festlegen und begruenden (z.B. 80 % als Minimum).
3. Test-Datensatz mit bekannten Treffern und bekannten Nicht-Treffern aufbauen.
4. Erkennungsleistung messen: Sensitivity (korrekte Treffer) und Specificity (False Positives).
5. Validierungsprotokoll erstellen und periodisch wiederholen (mindestens jaehrlich).
6. False-Positive-Management: eskalationsbasiertes Workflow-System.

## Rechtsrahmen

- **VO (EU) 269/2014 und 833/2014**: Bereitstellungsverbote erfordern effektives Screening.
- **BAFA-Informationssystem Sanktionen**: Anforderungen an Screening-Qualitaet.
- **GwG § 10 Abs. 1 Nr. 4**: Transaktionsmonitoring mit Namensabgleich.
- **§ 130 OWiG**: Organisationspflichtverletzung bei unzureichendem Screening.
- **AWG § 18**: Strafbarkeit bei Bereitstellung an gelistete Personen.**

## Pruef-Raster

- [ ] Screening-Algorithmen dokumentiert und begruendet?
- [ ] Schwellenwert fuer Fuzzy-Match definiert und schriftlich festgelegt?
- [ ] Validierungstest mit bekannten Treffern durchgefuehrt?
- [ ] False-Positive-Rate gemessen und dokumentiert?
- [ ] Validierungsprotokoll erstellt und im ICP hinterlegt?
- [ ] Periodische Re-Validierung geplant?

## Typische Fallstricke

- Zu hoher Schwellenwert (95 %) verpasst Treffer bei Schreibvarianten oder Transliterationen.
- Zu niedriger Schwellenwert erzeugt unbearbeitbare False-Positive-Last.
- Screening nur auf Name, nicht auf Geburtsdaten und Adressen; False-Negative-Risiko.
- Validierungstest fehlt; Tool wurde nie auf Erkennungsleistung geprueft.

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

Screening-Methodikbeschreibung, Schwellenwert-Begruendung, Validierungsprotokoll mit Sensitivity/Specificity-Kennzahlen und False-Positive-Workflow.

## Quellen

- [EU-Finanzsanktionsliste FSAP](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [BAFA Finanzsanktionen](https://www.bafa.de/DE/Aussenwirtschaft/Finanzsanktionen/finanzsanktionen_node.html)
- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [VO (EU) 269/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
