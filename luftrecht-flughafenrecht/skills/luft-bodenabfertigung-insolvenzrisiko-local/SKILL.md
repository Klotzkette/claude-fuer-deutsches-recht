---
name: luft-bodenabfertigung-insolvenzrisiko-local
description: "Luft Bodenabfertigung Insolvenzrisiko Local: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Bodenabfertigung Insolvenzrisiko Local

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Luft Bodenabfertigung Insolvenzrisiko Local** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-117-bodenabfertigung-insolvenzrisiko-marki` | Bodenabfertigungsunternehmen zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 Auswirkungen auf Flughafenvertrag BADV-Zulassung und Airline-Vertretung und liefert Risikoampel fuer Flughafenbetreiber Glaeubiger und Airlines. |
| `luft-118-bodenabfertigung-local-counsel-briefen` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Bodenabfertigungs-Mandat briefen: BADV-Zulassung Entgelt-Streit oder Insolvenz einer Handling-Firma. Skill erstellt englisches Briefing-Memo. |
| `luft-119-bodenabfertigung-dashboard-bauen` | Flughafen oder Bodenabfertigungsunternehmen braucht Dashboard: Zulassungsstatus Entgelt-Genehmigungen LuftSiG-Findings Personalzuverlässigkeit Finanzkennzahlen. Skill strukturiert Datenquellen BADV LuftSiG und liefert befuellbares Dashboard-Template. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Bodenabfertigung Insolvenzrisiko Local**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-117-bodenabfertigung-insolvenzrisiko-marki`

**Fokus:** Bodenabfertigungsunternehmen zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 Auswirkungen auf Flughafenvertrag BADV-Zulassung und Airline-Vertretung und liefert Risikoampel fuer Flughafenbetreiber Glaeubiger und Airlines.

# Bodenabfertigung – Insolvenzrisiko markieren

## Mandantenfall

- Bodenabfertigungsunternehmen zahlt Mitarbeiter verspätet; Flughafen fragt nach Konsequenzen.
- Airline hat Exklusiv-Vertrag mit Handling-Firma die insolvent zu werden droht; Contingency-Plan nötig.
- Bank hat Pfandrecht an Bodenabfertigungs-Equipment; fragt ob Verwertung vor Insolvenz möglich.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: InsO §§ 15a 17-19 47 BADV EU-RL 96/67 EG LuftVG § 6.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

InsO §§ 15a 17-19 47 BADV EU-RL 96/67 EG LuftVG § 6 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **BADV § 3**: Genehmigungspflicht für Bodenabfertigungsdienstleister; Zugang zum Bodenabfertigungsmarkt.
- **BADV § 7**: Selbstabfertigungsrecht der Luftverkehrsgesellschaft; Voraussetzungen.
- **BADV § 16**: Auswahlverfahren bei Kapazitätsbeschränkung; Vergabekommission.
- **EU-Richtlinie 96/67/EG Art. 6**: Marktöffnung für Bodenabfertigungsdienste.
- **LuftVG § 45**: Haftung bei Bodenabfertigungsschäden; Verweis auf allg. Deliktsrecht.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Genehmigung nach BADV § 3 aktuell und umfasst die tatsächlich erbrachten Dienste?
8. Hat Flughafen Kapazitätsbeschränkung nach BADV § 16 rechtmäßig festgesetzt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Selbstabfertigungsrecht beansprucht ohne Nachweis nach BADV § 7; Ablehnung durch Flughafen.
- Vergabekommissions-Entscheidung nicht fristgerecht angefochten; Bestandskraft eingetreten.

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Insolvenzrisiko markieren mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-118-bodenabfertigung-local-counsel-briefen`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Bodenabfertigungs-Mandat briefen: BADV-Zulassung Entgelt-Streit oder Insolvenz einer Handling-Firma. Skill erstellt englisches Briefing-Memo.

# Bodenabfertigung – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll in Spanien Local Counsel briefen für Streit über Bodenabfertigungsentgelte mit spanischem Flughafen.
- Britischer Flughafen fragt nach deutschen Bodenabfertigungs-Regulierungsanforderungen.
- Insolvenzverwalter beauftragt Kanzlei in Frankreich für Rückholung von Equipment aus französischem Flughafen.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BADV EU-RL 96/67 EG LuftVG § 6 InsO GWB.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BADV EU-RL 96/67 EG LuftVG § 6 InsO GWB – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **BADV § 3**: Genehmigungspflicht für Bodenabfertigungsdienstleister; Zugang zum Bodenabfertigungsmarkt.
- **BADV § 7**: Selbstabfertigungsrecht der Luftverkehrsgesellschaft; Voraussetzungen.
- **BADV § 16**: Auswahlverfahren bei Kapazitätsbeschränkung; Vergabekommission.
- **EU-Richtlinie 96/67/EG Art. 6**: Marktöffnung für Bodenabfertigungsdienste.
- **LuftVG § 45**: Haftung bei Bodenabfertigungsschäden; Verweis auf allg. Deliktsrecht.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Genehmigung nach BADV § 3 aktuell und umfasst die tatsächlich erbrachten Dienste?
8. Hat Flughafen Kapazitätsbeschränkung nach BADV § 16 rechtmäßig festgesetzt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Selbstabfertigungsrecht beansprucht ohne Nachweis nach BADV § 7; Ablehnung durch Flughafen.
- Vergabekommissions-Entscheidung nicht fristgerecht angefochten; Bestandskraft eingetreten.

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Local Counsel briefen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-119-bodenabfertigung-dashboard-bauen`

**Fokus:** Flughafen oder Bodenabfertigungsunternehmen braucht Dashboard: Zulassungsstatus Entgelt-Genehmigungen LuftSiG-Findings Personalzuverlässigkeit Finanzkennzahlen. Skill strukturiert Datenquellen BADV LuftSiG und liefert befuellbares Dashboard-Template.

# Bodenabfertigung – Dashboard bauen

## Mandantenfall

- Bodenabfertigungsunternehmen mit Betrieb an 3 Flughäfen braucht Compliance-Dashboard.
- Flughafenbetreiber überwacht Dienstleister; Dashboard für strukturiertes Monitoring.
- Investor kauft Bodenabfertigungsunternehmen; Dashboard für Due Diligence.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BADV EU-RL 96/67 EG LuftSiG § 7 EU-DVO 2015/1998 LuftVG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BADV EU-RL 96/67 EG LuftSiG § 7 EU-DVO 2015/1998 LuftVG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **BADV § 3**: Genehmigungspflicht für Bodenabfertigungsdienstleister; Zugang zum Bodenabfertigungsmarkt.
- **BADV § 7**: Selbstabfertigungsrecht der Luftverkehrsgesellschaft; Voraussetzungen.
- **BADV § 16**: Auswahlverfahren bei Kapazitätsbeschränkung; Vergabekommission.
- **EU-Richtlinie 96/67/EG Art. 6**: Marktöffnung für Bodenabfertigungsdienste.
- **LuftVG § 45**: Haftung bei Bodenabfertigungsschäden; Verweis auf allg. Deliktsrecht.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Genehmigung nach BADV § 3 aktuell und umfasst die tatsächlich erbrachten Dienste?
8. Hat Flughafen Kapazitätsbeschränkung nach BADV § 16 rechtmäßig festgesetzt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Selbstabfertigungsrecht beansprucht ohne Nachweis nach BADV § 7; Ablehnung durch Flughafen.
- Vergabekommissions-Entscheidung nicht fristgerecht angefochten; Bestandskraft eingetreten.

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Dashboard bauen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
