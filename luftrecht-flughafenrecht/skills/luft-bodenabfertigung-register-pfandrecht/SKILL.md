---
name: luft-bodenabfertigung-register-pfandrecht
description: "Luft Bodenabfertigung Register Pfandrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Bodenabfertigung Register Pfandrecht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Bodenabfertigung Register Pfandrecht** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-112-bodenabfertigung-register-auswerten` | Mandant will Zulassungsstatus und Entgelt-Tarife von Bodenabfertigungsdienstleistern auswerten. Skill prueft BADV EU-RL 96/67 EG Zulassungsregister und Entgelt-Genehmigungen und liefert Compliance-Status-Bericht. |
| `luft-113-bodenabfertigung-pfandrecht-vorbereite` | Kreditgeber will Pfandrecht an Bodenabfertigungs-Equipment als Sicherheit bestellen. Skill prueft BGB §§ 1204 ff. Mobiliarpfandrecht BADV-Zulassung als Wertfaktor und liefert Sicherungsstruktur-Vermerk. |
| `luft-114-bodenabfertigung-pfaendung-planen` | Glaeubiger will Bodenabfertigungs-Equipment oder Entgelt-Forderungen pfaenden. Prueft ZPO § 808 Mobiliarpfaendung ZPO §§ 828 ff. Forderungspfaendung InsO-Vollstreckungssperre und liefert Pfaendungsplan. |
| `luft-115-bodenabfertigung-genehmigung-pruefen` | Bodenabfertigungsdienstleister braucht Zulassung nach BADV oder Genehmigung des Flughafenbetreibers. Skill prueft BADV EU-RL 96/67 EG Zulassungsvoraussetzungen LuftSiG-Anforderungen und liefert Genehmigungsstatus-Vermerk mit Handlungsbedarf. |
| `luft-116-bodenabfertigung-sicherheitsauflage-be` | Bodenabfertigungsdienstleister erhaelt LuftSiG-Auflage oder Betreiber-Auflage des Flughafens. Skill prueft LuftSiG § 7 Zuverlässigkeitsüberprüfung EU-DVO 2015/1998 BADV und liefert Auflagen-Bewertungs-Vermerk. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Bodenabfertigung Register Pfandrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-112-bodenabfertigung-register-auswerten`

**Fokus:** Mandant will Zulassungsstatus und Entgelt-Tarife von Bodenabfertigungsdienstleistern auswerten. Skill prueft BADV EU-RL 96/67 EG Zulassungsregister und Entgelt-Genehmigungen und liefert Compliance-Status-Bericht.

# Bodenabfertigung – Register auswerten

## Mandantenfall

- Airline prüft vor Vertragsabschluss ob Bodenabfertigungsdienstleister korrekt zugelassen ist.
- Neuer Marktteilnehmer will Bodenabfertigung anbieten; Prüfung der Zulassungsvoraussetzungen.
- Flughafen hat Dienstleister ausgeschlossen; Mandant prüft ob Ausschluss rechtmäßig ist.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BADV EU-RL 96/67 EG LuftVG § 6 GWB Vergaberecht.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BADV EU-RL 96/67 EG LuftVG § 6 GWB Vergaberecht – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Register auswerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-113-bodenabfertigung-pfandrecht-vorbereite`

**Fokus:** Kreditgeber will Pfandrecht an Bodenabfertigungs-Equipment als Sicherheit bestellen. Skill prueft BGB §§ 1204 ff. Mobiliarpfandrecht BADV-Zulassung als Wertfaktor und liefert Sicherungsstruktur-Vermerk.

# Bodenabfertigung – Pfandrecht vorbereiten

## Mandantenfall

- Bank finanziert Kauf von Spezial-Bodenabfertigungs-Fahrzeugen; will Mobiliarpfandrecht bestellen.
- Leasinggesellschaft verleast Pushback-Fahrzeuge; will Sicherungsübereignung statt Pfandrecht.
- Bodenabfertigungsunternehmen will Kredit; Bank fragt ob BADV-Zulassung als Sicherheit geeignet ist.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BGB §§ 1204 ff. BGB §§ 929 930 BADV LuftVG § 6.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BGB §§ 1204 ff. BGB §§ 929 930 BADV LuftVG § 6 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Pfandrecht vorbereiten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-114-bodenabfertigung-pfaendung-planen`

**Fokus:** Glaeubiger will Bodenabfertigungs-Equipment oder Entgelt-Forderungen pfaenden. Prueft ZPO § 808 Mobiliarpfaendung ZPO §§ 828 ff. Forderungspfaendung InsO-Vollstreckungssperre und liefert Pfaendungsplan.

# Bodenabfertigung – Pfändung planen

## Mandantenfall

- Gläubiger will Bodenabfertigungs-Fahrzeuge einer insolventen Handling-Firma pfänden.
- Airline will Bodenabfertigungsentgelt-Erstattung pfänden nach Überzahlung.
- Insolvenz des Bodenabfertigungsunternehmens; Flughafen fragt ob er Entgelte einbehalten kann.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: ZPO §§ 808 828 ff. InsO §§ 89 47 BGB § 320.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

ZPO §§ 808 828 ff. InsO §§ 89 47 BGB § 320 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Pfändung planen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-115-bodenabfertigung-genehmigung-pruefen`

**Fokus:** Bodenabfertigungsdienstleister braucht Zulassung nach BADV oder Genehmigung des Flughafenbetreibers. Skill prueft BADV EU-RL 96/67 EG Zulassungsvoraussetzungen LuftSiG-Anforderungen und liefert Genehmigungsstatus-Vermerk mit Handlungsbedarf.

# Bodenabfertigung – Genehmigung prüfen

## Mandantenfall

- Neuer Bodenabfertigungsdienstleister fragt was er braucht um am Flughafen tätig zu werden.
- Bestehende Zulassung läuft aus; Verlängerungsantrag noch nicht gestellt.
- Dienstleister expandiert auf neuen Flughafen; fragt ob neue Zulassung oder Erweiterung nötig.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BADV EU-RL 96/67 EG LuftSiG § 7 LuftVG § 6.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BADV EU-RL 96/67 EG LuftSiG § 7 LuftVG § 6 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Genehmigung prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-116-bodenabfertigung-sicherheitsauflage-be`

**Fokus:** Bodenabfertigungsdienstleister erhaelt LuftSiG-Auflage oder Betreiber-Auflage des Flughafens. Skill prueft LuftSiG § 7 Zuverlässigkeitsüberprüfung EU-DVO 2015/1998 BADV und liefert Auflagen-Bewertungs-Vermerk.

# Bodenabfertigung – Sicherheitsauflage bewerten

## Mandantenfall

- Bodenabfertigungsdienstleister erhält Auflage zu verstärkten Personenkontrollen; Kosten erheblich.
- Flughafen-Betreiber macht Zugang zum Vorfeld von Zertifizierungs-Auflage abhängig.
- EU-DVO-Anforderungen zu Fahrzeugkontrollen verschärft; Bodenabfertigungs-Firma braucht Umsetzungsplan.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftSiG § 7 EU-DVO 2015/1998 BADV LuftVG § 6.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftSiG § 7 EU-DVO 2015/1998 BADV LuftVG § 6 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Sicherheitsauflage bewerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
