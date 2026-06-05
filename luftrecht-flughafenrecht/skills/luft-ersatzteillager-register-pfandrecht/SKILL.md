---
name: luft-ersatzteillager-register-pfandrecht
description: "Luft Ersatzteillager Register Pfandrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Ersatzteillager Register Pfandrecht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Ersatzteillager Register Pfandrecht** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-062-ersatzteillager-register-auswerten` | Mandant will Register-/Inventar-Status fuer Luftfahrzeug-Ersatzteile auswerten. Prueft EASA Part-145 AMO-Zertifizierung LuftVG-Eintragung Cape-Town-Convention fuer Triebwerke und Luftfahrzeugteile und liefert Bestandsaufnahme-Bericht mit Zertifizierungsstatus. |
| `luft-063-ersatzteillager-pfandrecht-vorbereiten` | Kreditgeber will Pfandrecht an Ersatzteillager und Flugzeugteilen als Kreditsicherheit bestellen. Prueft BGB §§ 1204 ff. Mobiliarpfandrecht LuftFzgG Cape-Town-Convention fuer Triebwerke und Zubehoer und liefert Sicherungsstruktur-Vermerk fuer Spares-Finanzierung. |
| `luft-064-ersatzteillager-pfaendung-planen` | Glaeubiger will Ersatzteillager oder einzelne Flugzeugteile pfaenden. Prueft ZPO § 808 Mobiliarpfaendung Cape-Town-Motorenerfassung LuftFzgG Zubehoerpfandrecht und Insolvenz-Freigabe und liefert Pfaendungsplan fuer Teile-Vollstreckung. |
| `luft-065-ersatzteillager-genehmigung-pruefen` | Ersatzteillager braucht Genehmigungen: EASA Part-145 AMO-Zertifizierung LBA-Anerkennung Zollgenehmigung Gefahrguterlaubnis. Skill prueft Genehmigungsstatus und liefert Genehmigungslücken-Analyse mit Antragsfristen. |
| `luft-066-ersatzteillager-sicherheitsauflage-bew` | Ersatzteillager erhaelt EASA oder LBA-Auflage zur Lagerung zertifizierter Teile oder Gefahrgut-Auflage. Prueft EASA Part-145 Anforderungen LuftVG Gefahrgutrecht IATA DGR und liefert Auflagen-Bewertungs-Vermerk und Compliance-Plan. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Ersatzteillager Register Pfandrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-062-ersatzteillager-register-auswerten`

**Fokus:** Mandant will Register-/Inventar-Status fuer Luftfahrzeug-Ersatzteile auswerten. Prueft EASA Part-145 AMO-Zertifizierung LuftVG-Eintragung Cape-Town-Convention fuer Triebwerke und Luftfahrzeugteile und liefert Bestandsaufnahme-Bericht mit Zertifizierungsstatus.

# Ersatzteillager – Register auswerten

## Mandantenfall

- Verkäufer eines MRO-Betriebs will vor Kaufvertrag prüfen ob alle Teile EASA-zertifiziert und frei von Belastungen sind.
- Leasinggesellschaft prüft bei Rückgabe des Flugzeugs ob alle Originalteile vorhanden und eingetragen sind.
- Insolvenzverwalter braucht Inventar-Bewertung aller Ersatzteile und deren Zertifizierungsstatus.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EASA Part-145 Cape Town Convention Art. 2 LuftFzgG BGB §§ 1204 ff..
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EASA Part-145 Cape Town Convention Art. 2 LuftFzgG BGB §§ 1204 ff. – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Ersatzteillager – Register auswerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-063-ersatzteillager-pfandrecht-vorbereiten`

**Fokus:** Kreditgeber will Pfandrecht an Ersatzteillager und Flugzeugteilen als Kreditsicherheit bestellen. Prueft BGB §§ 1204 ff. Mobiliarpfandrecht LuftFzgG Cape-Town-Convention fuer Triebwerke und Zubehoer und liefert Sicherungsstruktur-Vermerk fuer Spares-Finanzierung.

# Ersatzteillager – Pfandrecht vorbereiten

## Mandantenfall

- Bank will Ersatzteillager einer MRO-Gesellschaft als Kreditsicherheit nehmen; Frage ob Mobiliar- oder Luftfahrzeugpfandrecht.
- Leasinggesellschaft will Triebwerke als gesonderte Pfandobjekte sichern; Cape-Town-Eintrag für Triebwerke prüfen.
- Finanzier will Spares-Pool-Finanzierung; Sicherungsstruktur über mehrere Länder und Registrierungsstaaten.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BGB §§ 1204 ff. LuftFzgG §§ 3-5 Cape Town Convention Art. 2 ICAO-Register.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BGB §§ 1204 ff. LuftFzgG §§ 3-5 Cape Town Convention Art. 2 ICAO-Register – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Strukturierter Vermerk zu Ersatzteillager – Pfandrecht vorbereiten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-064-ersatzteillager-pfaendung-planen`

**Fokus:** Glaeubiger will Ersatzteillager oder einzelne Flugzeugteile pfaenden. Prueft ZPO § 808 Mobiliarpfaendung Cape-Town-Motorenerfassung LuftFzgG Zubehoerpfandrecht und Insolvenz-Freigabe und liefert Pfaendungsplan fuer Teile-Vollstreckung.

# Ersatzteillager – Pfändung planen

## Mandantenfall

- Gläubiger will Ersatzteillager einer insolventen MRO-Gesellschaft pfänden; Pfandrechte des Leasinggebers an Triebwerken beachten.
- Cape-Town-Gläubiger beansprucht Triebwerke aus Lager als Teil seines Sicherungsinteresses.
- Zwangsversteigerung von EASA-zertifizierten Teilen; Käufer fragt ob Zertifizierung auf ihn übergeht.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: ZPO § 808 LuftFzgG §§ 3-5 Cape Town Convention InsO §§ 47 89.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

ZPO § 808 LuftFzgG §§ 3-5 Cape Town Convention InsO §§ 47 89 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Strukturierter Vermerk zu Ersatzteillager – Pfändung planen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-065-ersatzteillager-genehmigung-pruefen`

**Fokus:** Ersatzteillager braucht Genehmigungen: EASA Part-145 AMO-Zertifizierung LBA-Anerkennung Zollgenehmigung Gefahrguterlaubnis. Skill prueft Genehmigungsstatus und liefert Genehmigungslücken-Analyse mit Antragsfristen.

# Ersatzteillager – Genehmigung prüfen

## Mandantenfall

- MRO-Betrieb hat EASA Part-145 Zertifizierung; fragt ob zusätzliche LBA-Genehmigung nötig ist.
- Neuer Lagerstandort geplant; welche Genehmigungen sind neu zu beantragen.
- Gefahrgut-haltige Teile (hydraulische Flüssigkeiten) sollen eingelagert werden; Zollgenehmigung unklar.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EASA Part-145 LuftVG § 29 Zollrecht IATA DGR Gefahrgutrecht.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EASA Part-145 LuftVG § 29 Zollrecht IATA DGR Gefahrgutrecht – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Output

Strukturierter Vermerk zu Ersatzteillager – Genehmigung prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-066-ersatzteillager-sicherheitsauflage-bew`

**Fokus:** Ersatzteillager erhaelt EASA oder LBA-Auflage zur Lagerung zertifizierter Teile oder Gefahrgut-Auflage. Prueft EASA Part-145 Anforderungen LuftVG Gefahrgutrecht IATA DGR und liefert Auflagen-Bewertungs-Vermerk und Compliance-Plan.

# Ersatzteillager – Sicherheitsauflage bewerten

## Mandantenfall

- EASA-Inspektion des Ersatzteillagers ergibt Non-Conformity zu Part-145 Anforderungen; 30-Tage-Frist zur Abhilfe.
- Gefahrgut-Aufsichtsbehörde beanstandet Lagerung von Hydraulikflüssigkeiten ohne Genehmigung.
- LBA ordnet nach Unfall Nachrüstung der Lagereinrichtungen an; Verhältnismäßigkeit fraglich.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EASA Part-145 LuftVG Gefahrgutrecht IATA DGR EU-DVO 2015/1998.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EASA Part-145 LuftVG Gefahrgutrecht IATA DGR EU-DVO 2015/1998 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Output

Strukturierter Vermerk zu Ersatzteillager – Sicherheitsauflage bewerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
