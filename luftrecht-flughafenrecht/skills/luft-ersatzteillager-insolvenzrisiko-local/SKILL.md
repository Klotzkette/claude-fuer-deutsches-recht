---
name: luft-ersatzteillager-insolvenzrisiko-local
description: "Luft Ersatzteillager Insolvenzrisiko Local: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Ersatzteillager Insolvenzrisiko Local

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Ersatzteillager Insolvenzrisiko Local** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-067-ersatzteillager-insolvenzrisiko-markie` | MRO-Betrieb oder Airline mit grossem Ersatzteillager zeigt Insolvenzzeichen. Prueft InsO §§ 47 50 103 Aus- und Absonderungsrechte an Ersatzteilen und Werkzeugpfandrecht des Reparateurs und liefert Risikoampel fuer Glaeubiger. |
| `luft-068-ersatzteillager-local-counsel-briefen` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Ersatzteillager-Mandat briefen: EASA-Zertifizierungsstatus Cape-Town-Triebwerks-Pfandrecht deutsches Insolvenzrecht. Skill erstellt englisches Briefing-Memo mit konkreten Fragen. |
| `luft-069-ersatzteillager-dashboard-bauen` | MRO-Gesellschaft oder Airline braucht Inventar-Dashboard fuer Ersatzteillager: EASA-Zertifizierungsstatus Pfandrechte Cape-Town-Eintrag Versicherung Wert. Skill strukturiert Datenquellen und liefert befuellbares Inventar-Dashboard-Template. |
| `luft-070-ersatzteillager-mandantenmemo-schreibe` | Anwalt schreibt Mandantenmemo fuer MRO-Betrieb oder Airline zu Ersatzteillager-Rechtsfragen: EASA-Compliance Pfandrecht Insolvenz oder Gefahrgut-Auflage. Skill strukturiert Memo mit Sachverhalt Rechtslage Handlungsoptionen und Empfehlung. |
| `luft-072-drohne-register-auswerten` | Mandant will Registrierungsstatus einer Drohne beim LBA auswerten. Prueft EU-VO 2019/947 Art. 14 Registrierungspflicht ab 250 g LuftVG § 21a und Betreiber-Identifikation und liefert Registrierungs-Auswertung mit Compliance-Status. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Ersatzteillager Insolvenzrisiko Local**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-067-ersatzteillager-insolvenzrisiko-markie`

**Fokus:** MRO-Betrieb oder Airline mit grossem Ersatzteillager zeigt Insolvenzzeichen. Prueft InsO §§ 47 50 103 Aus- und Absonderungsrechte an Ersatzteilen und Werkzeugpfandrecht des Reparateurs und liefert Risikoampel fuer Glaeubiger.

# Ersatzteillager – Insolvenzrisiko markieren

## Mandantenfall

- MRO-Betrieb zahlt Lieferanten nicht mehr; diese wollen Teile zurückholen; Aussonderungsrecht prüfen.
- Airline insolvent; Insolvenzverwalter will Ersatzteillager für Masse verwenden; Leasinggeber widerspricht.
- Bank hat Pfandrecht an Ersatzteilen; Insolvenzverwalter will Teile für laufenden Betrieb verwenden.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: InsO §§ 47 50 103 BGB § 369 Handelspfandrecht EASA Part-145 LuftFzgG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

InsO §§ 47 50 103 BGB § 369 Handelspfandrecht EASA Part-145 LuftFzgG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EASA Part-145 M.A.501**: Anforderungen an genehmigte Instandhaltungsbetriebe; Teileherkunft und Dokumentation.
- **EASA Part-145 145.A.42**: Akzeptanz von Teilen und Materialien; Konformitätsnachweise (EASA Form 1).
- **LuftVG § 10**: Instandhaltungsorganisation; Verbindung zur LBA-Aufsicht.
- **HGB § 475h**: Lagerhalter-Haftung; Freizeichnung bei mangelhafter Dokumentation.
- **VO (EG) 2042/2003 Anhang II (Part-145)**: Genehmigungsumfang; Erweiterung von Ratings.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Liegt für jedes eingelagerte Teil ein gültiger Konformitätsnachweis (EASA Form 1) vor?
8. Sind Lagerorte und Umgebungsbedingungen nach Part-145 dokumentiert?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Teile ohne EASA Form 1 eingelagert; bei Einbau Bußgeld und Zulassungsverlust.
- Lagervertrag nicht Part-145-konform; zivilrechtliche Haftung trifft Betreiber.

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Output

Strukturierter Vermerk zu Ersatzteillager – Insolvenzrisiko markieren mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-068-ersatzteillager-local-counsel-briefen`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Ersatzteillager-Mandat briefen: EASA-Zertifizierungsstatus Cape-Town-Triebwerks-Pfandrecht deutsches Insolvenzrecht. Skill erstellt englisches Briefing-Memo mit konkreten Fragen.

# Ersatzteillager – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll in Singapur Local Counsel briefen für Pfändung von Triebwerken aus deutschem Ersatzteillager.
- Irischer Leasinggeber fragt nach Cape-Town-Schutz für Triebwerke die in deutschem Lager gelagert werden.
- Insolvenzverwalter beauftragt Kanzlei in UK zur Rückholung von Triebwerken auf britischem Flughafen.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EASA Part-145 Cape Town Convention LuftFzgG InsO ZPO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EASA Part-145 Cape Town Convention LuftFzgG InsO ZPO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EASA Part-145 M.A.501**: Anforderungen an genehmigte Instandhaltungsbetriebe; Teileherkunft und Dokumentation.
- **EASA Part-145 145.A.42**: Akzeptanz von Teilen und Materialien; Konformitätsnachweise (EASA Form 1).
- **LuftVG § 10**: Instandhaltungsorganisation; Verbindung zur LBA-Aufsicht.
- **HGB § 475h**: Lagerhalter-Haftung; Freizeichnung bei mangelhafter Dokumentation.
- **VO (EG) 2042/2003 Anhang II (Part-145)**: Genehmigungsumfang; Erweiterung von Ratings.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Liegt für jedes eingelagerte Teil ein gültiger Konformitätsnachweis (EASA Form 1) vor?
8. Sind Lagerorte und Umgebungsbedingungen nach Part-145 dokumentiert?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Teile ohne EASA Form 1 eingelagert; bei Einbau Bußgeld und Zulassungsverlust.
- Lagervertrag nicht Part-145-konform; zivilrechtliche Haftung trifft Betreiber.

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Output

Strukturierter Vermerk zu Ersatzteillager – Local Counsel briefen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-069-ersatzteillager-dashboard-bauen`

**Fokus:** MRO-Gesellschaft oder Airline braucht Inventar-Dashboard fuer Ersatzteillager: EASA-Zertifizierungsstatus Pfandrechte Cape-Town-Eintrag Versicherung Wert. Skill strukturiert Datenquellen und liefert befuellbares Inventar-Dashboard-Template.

# Ersatzteillager – Dashboard bauen

## Mandantenfall

- MRO-Gesellschaft hat Teile in 5 Lagern; Dashboard soll Zertifizierungsstatus und Belastungen bündeln.
- Insolvenzverwalter braucht sofortigen Überblick über Inventar-Wert und Gläubiger-Ansprüche.
- Käufer des MRO-Betriebs führt Due Diligence durch; Dashboard als Datenzusammenführungs-Instrument.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EASA Part-145 Cape Town Convention LuftFzgG InsO BGB.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EASA Part-145 Cape Town Convention LuftFzgG InsO BGB – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EASA Part-145 M.A.501**: Anforderungen an genehmigte Instandhaltungsbetriebe; Teileherkunft und Dokumentation.
- **EASA Part-145 145.A.42**: Akzeptanz von Teilen und Materialien; Konformitätsnachweise (EASA Form 1).
- **LuftVG § 10**: Instandhaltungsorganisation; Verbindung zur LBA-Aufsicht.
- **HGB § 475h**: Lagerhalter-Haftung; Freizeichnung bei mangelhafter Dokumentation.
- **VO (EG) 2042/2003 Anhang II (Part-145)**: Genehmigungsumfang; Erweiterung von Ratings.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Liegt für jedes eingelagerte Teil ein gültiger Konformitätsnachweis (EASA Form 1) vor?
8. Sind Lagerorte und Umgebungsbedingungen nach Part-145 dokumentiert?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Teile ohne EASA Form 1 eingelagert; bei Einbau Bußgeld und Zulassungsverlust.
- Lagervertrag nicht Part-145-konform; zivilrechtliche Haftung trifft Betreiber.

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Strukturierter Vermerk zu Ersatzteillager – Dashboard bauen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-070-ersatzteillager-mandantenmemo-schreibe`

**Fokus:** Anwalt schreibt Mandantenmemo fuer MRO-Betrieb oder Airline zu Ersatzteillager-Rechtsfragen: EASA-Compliance Pfandrecht Insolvenz oder Gefahrgut-Auflage. Skill strukturiert Memo mit Sachverhalt Rechtslage Handlungsoptionen und Empfehlung.

# Ersatzteillager – Mandantenmemo schreiben

## Mandantenfall

- MRO-Vorstand braucht Memo nach EASA Non-Conformity; 30-Tage-Frist läuft; Betriebsunterbrechung möglich.
- Leasinggeber fragt nach Schutz seiner Triebwerke im Ersatzteillager einer insolventen Airline.
- Finanzierer braucht Memo über Sicherheitsstruktur für Ersatzteillager-Finanzierung.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EASA Part-145 Cape Town Convention InsO LuftFzgG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EASA Part-145 Cape Town Convention InsO LuftFzgG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EASA Part-145 M.A.501**: Anforderungen an genehmigte Instandhaltungsbetriebe; Teileherkunft und Dokumentation.
- **EASA Part-145 145.A.42**: Akzeptanz von Teilen und Materialien; Konformitätsnachweise (EASA Form 1).
- **LuftVG § 10**: Instandhaltungsorganisation; Verbindung zur LBA-Aufsicht.
- **HGB § 475h**: Lagerhalter-Haftung; Freizeichnung bei mangelhafter Dokumentation.
- **VO (EG) 2042/2003 Anhang II (Part-145)**: Genehmigungsumfang; Erweiterung von Ratings.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Liegt für jedes eingelagerte Teil ein gültiger Konformitätsnachweis (EASA Form 1) vor?
8. Sind Lagerorte und Umgebungsbedingungen nach Part-145 dokumentiert?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Teile ohne EASA Form 1 eingelagert; bei Einbau Bußgeld und Zulassungsverlust.
- Lagervertrag nicht Part-145-konform; zivilrechtliche Haftung trifft Betreiber.

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Output

Strukturierter Vermerk zu Ersatzteillager – Mandantenmemo schreiben mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-072-drohne-register-auswerten`

**Fokus:** Mandant will Registrierungsstatus einer Drohne beim LBA auswerten. Prueft EU-VO 2019/947 Art. 14 Registrierungspflicht ab 250 g LuftVG § 21a und Betreiber-Identifikation und liefert Registrierungs-Auswertung mit Compliance-Status.

# Drohne – Register auswerten

## Mandantenfall

- Behörde fragt nach Registrierungsnachweis für gewerblich eingesetzte Drohne; Mandant hat Nachweis verloren.
- Drohnenflotte eines Unternehmens soll auf Registrierungsstatus geprüft werden.
- Drohnenunfall: Behörde will Registrierung des Verursachers prüfen; Eigentümer unklar.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-VO 2019/947 Art. 14 LuftVG § 21a LBA-Registrierungssystem.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-VO 2019/947 Art. 14 LuftVG § 21a LBA-Registrierungssystem – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21e**: Nationales UAS-Register; Registrierungspflicht ab 250 g.
- **LuftVO § 21b**: Betriebsverbote und Beschränkungszonen; Kontrollluftraum.
- **EASA Easy Access Rules for UAS**: Konsolidierte Fassung aller UAS-Verordnungen.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Betriebskategorie (offen/spezifisch/zertifiziert) korrekt eingestuft (EU-VO 2019/947 Art. 5)?
8. Liegt für spezifische Kategorie ein genehmigter SORA-Risikoplan vor?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Drohne über 250 g nicht im UAS-Register eingetragen; Bußgeld nach LuftVG § 58.
- Betriebszone ohne LBA-Genehmigung überflogen; Strafbarkeit nach § 315a StGB.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Drohne – Register auswerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-VO 2019/947: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019R0947
- LBA UAS: https://www.lba.de/DE/Drohnen/Drohnen_node.html
- EASA UAS: https://www.easa.europa.eu/en/domains/civil-drones

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Drohnen und UAS-Betrieb ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
