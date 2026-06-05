---
name: luft-airline-local-dashboard-bauen
description: "Luft Airline Local Dashboard Bauen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Airline Local Dashboard Bauen

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Airline Local Dashboard Bauen** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-028-airline-local-counsel-briefen` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Airline-Mandat briefen: Arrest Insolvenz Cape-Town oder Betriebsgenehmigung. Skill erstellt strukturiertes englisches Briefing-Memo mit Sachverhalt deutschem Rechtsrahmen Cape-Town-Status IDERA und konkreten Fragen an Local Counsel. |
| `luft-029-airline-dashboard-bauen` | Kanzlei oder Mandant braucht operatives Airline-Dashboard fuer laufendes Mandat: Genehmigungsstatus Flotte Slots Sicherheitsauflagen Insolvenzrisiko. Skill strukturiert Datenquellen LBA EU-VO 1008/2008 Art. 9 Fluko ICAO-Register und liefert befuellbares Dashboard-Template mit Aktualisierungs-Checkliste. |
| `luft-030-airline-mandantenmemo-schreiben` | Anwalt schreibt Mandantenmemo fuer Airline zu komplexem Luftrechtsfall: Genehmigungsrisiko Sicherheitsauflage Slot-Verlust oder Insolvenznaehe. Skill strukturiert Memo nach Sachverhalt Rechtslage Handlungsoptionen Risikobewertung und Empfehlung und liefert fertigen Memo-Baustein mit Nächste-Schritte-Tabelle. |
| `luft-032-flughafen-register-auswerten` | Mandant will Grundbuch Liegenschaftsregister und LuftVG-Genehmigungshistorie eines Flughafens auswerten. Skill prueft LuftVG § 6 Genehmigungsurkunde Planfeststellungsbeschluss Grundbuch und FluglaermG-Zoneneinteilung und liefert strukturierten Genehmigungsstatus-Bericht. |
| `luft-033-flughafen-pfandrecht-vorbereiten` | Kreditgeber will Sicherheiten an Flughafen-Infrastruktur bestellen. Skill prueft Grundbuchrecht Hypothek Grundschuld GBO LuftVG-Betreiberpflichten und Abgrenzung vom Luftfahrzeugpfandrecht und liefert Sicherungsstrategie-Vermerk fuer Flughafen-Finanzierung. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Airline Local Dashboard Bauen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-028-airline-local-counsel-briefen`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Airline-Mandat briefen: Arrest Insolvenz Cape-Town oder Betriebsgenehmigung. Skill erstellt strukturiertes englisches Briefing-Memo mit Sachverhalt deutschem Rechtsrahmen Cape-Town-Status IDERA und konkreten Fragen an Local Counsel.

# Airline – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll Arrest auf Flugzeug einer deutschen Airline in Dubai beantragen; lokaler Anwalt braucht Briefing zu deutschem Pfandrecht und Cape-Town-Status.
- Irischer Leasinggeber gibt deutschem Anwalt Auftrag Local Counsel zu briefen für Herausgabeklage gegen insolvente Airline.
- Insolvenzverwalter beauftragt Kanzlei in London zur Rückholung von Flugzeugen; Briefing zu deutschem Insolvenzrecht und Cape Town nötig.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Output

Vermerk zu Airline – Local Counsel briefen mit Ampel-Rating Fristenstand und nächsten Schritten. Checkliste offener Punkte. Zuständigkeitsmatrix Behörde/Register. Fristenkalender mit Ampelstatus.
## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-029-airline-dashboard-bauen`

**Fokus:** Kanzlei oder Mandant braucht operatives Airline-Dashboard fuer laufendes Mandat: Genehmigungsstatus Flotte Slots Sicherheitsauflagen Insolvenzrisiko. Skill strukturiert Datenquellen LBA EU-VO 1008/2008 Art. 9 Fluko ICAO-Register und liefert befuellbares Dashboard-Template mit Aktualisierungs-Checkliste.

# Airline – Dashboard bauen

## Mandantenfall

- Kanzlei betreut Airline dauerhaft und braucht strukturiertes internes Dashboard für Mandatsstatus Fristen und Risiken.
- Insolvenzverwalter übernimmt Airline; braucht sofort strukturierten Überblick über alle relevanten Daten.
- Investor führt Due Diligence durch; Dashboard als Instrument für strukturierte Datenzusammenführung.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Vermerk zu Airline – Dashboard bauen mit Ampel-Rating Fristenstand und nächsten Schritten. Checkliste offener Punkte. Zuständigkeitsmatrix Behörde/Register. Fristenkalender mit Ampelstatus.
## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-030-airline-mandantenmemo-schreiben`

**Fokus:** Anwalt schreibt Mandantenmemo fuer Airline zu komplexem Luftrechtsfall: Genehmigungsrisiko Sicherheitsauflage Slot-Verlust oder Insolvenznaehe. Skill strukturiert Memo nach Sachverhalt Rechtslage Handlungsoptionen Risikobewertung und Empfehlung und liefert fertigen Memo-Baustein mit Nächste-Schritte-Tabelle.

# Airline – Mandantenmemo schreiben

## Mandantenfall

- Airline-Vorstand braucht Memo nach LBA-Schreiben zu finanzieller Leistungsfähigkeit; Entscheidungsgrundlage für Vorstandssitzung.
- Airline soll Insolvenz beantragen; Memo an Gesellschafter über Rechtslage Ablauf und Alternativen.
- Audit-Finding Level 1; Memo an Airline-Compliance-Abteilung über sofortigen Handlungsbedarf.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Output

Vermerk zu Airline – Mandantenmemo schreiben mit Ampel-Rating Fristenstand und nächsten Schritten. Checkliste offener Punkte. Zuständigkeitsmatrix Behörde/Register. Fristenkalender mit Ampelstatus.
## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-032-flughafen-register-auswerten`

**Fokus:** Mandant will Grundbuch Liegenschaftsregister und LuftVG-Genehmigungshistorie eines Flughafens auswerten. Skill prueft LuftVG § 6 Genehmigungsurkunde Planfeststellungsbeschluss Grundbuch und FluglaermG-Zoneneinteilung und liefert strukturierten Genehmigungsstatus-Bericht.

# Flughafen – Register auswerten

## Mandantenfall

- Investor prüft Erwerb von Flughafeninfrastruktur; Due-Diligence verlangt vollständigen Überblick über Genehmigungsstand und Auflagen.
- Anwohnerin will wissen welche Betriebsgenehmigung gilt und ob Nachtflugbeschränkungen drin stehen.
- Gläubiger will Flughafengrundstücke pfänden; Grundbuchsituation und Eigentümerstruktur unklar.

## Erste Schritte

1. Sachverhalt strukturieren: Flughafen Art des Problems beteiligte Behörden Fristen.
2. Planfeststellungsstatus prüfen: LuftVG § 6/8 Genehmigung Auflagen aktuell.
3. Grundbuch und Eigentümerstruktur klären: kommunal staatlich privatwirtschaftlich.
4. LuftSiG-Sicherheitsprogramm auf Aktualität prüfen: EU-DVO 2015/1998 Anforderungen.
5. Finanzlage einschätzen: EU-Beihilferechtsstatus Subventionen Darlehen.
6. Handlungsbedarf dokumentieren: Vermerk mit Fristenstand und Empfehlungen.

## Rechtsrahmen

- **LuftVG §§ 6-8**: Flugplatzgenehmigung und Planfeststellungspflicht.
- **LuftVG § 10**: Wirkung des Planfeststellungsbeschlusses.
- **LuftSiG § 8**: Sicherheitspflichten des Flugplatzbetreibers.
- **EU-DVO 2015/1998**: Technische Sicherheitsanforderungen.
- **FluglärmG §§ 2-9**: Lärmschutzbereiche und Schallschutzansprüche.
- **InsO §§ 15a 17-19**: Insolvenzantragspflicht.
- **VwVfG §§ 72-78**: Planfeststellungsverfahren.
- **LuftVG § 6**: Genehmigung des Flughafenbetriebs; sachliche und persönliche Voraussetzungen.
- **LuftVG § 8**: Planfeststellungsverfahren für Flughafenausbau; UVP-Pflicht.
- **LuftVG § 9**: Planfeststellungsbeschluss; Drittwirkung und Bestandsschutz.
- **FluglärmG § 4**: Lärmschutzbereiche; Tagschutzzonen 1 und 2 sowie Nachtschutzzone.
- **VwVfG § 72**: Planfeststellungsverfahren allgemein; Beteiligungsrechte betroffener Dritter.
## Prüfraster

1. Ist Planfeststellungsbeschluss aktuell und vollständig umgesetzt?
2. Sind LuftSiG-Sicherheitsprogramme auf aktuellem EU-DVO-Stand?
3. Ist Grundbuchsituation und Eigentümerstruktur klar?
4. Bestehen offene Klagen oder Einwendungsverfahren?
5. Zeigen Finanzkennzahlen Insolvenzfrühzeichen?
6. Sind alle Auflagen aus Planfeststellungsbeschluss fristgerecht erfüllt?
7. Ist eine UVP nach UVPG § 4 durchgeführt und aktuell?
8. Sind Lärmschutzbereiche nach FluglärmG § 4 neu zu ermitteln nach Bauerweiterung?
## Typische Fallstricke

- Planfeststellungsauflagen veraltet und nicht auf aktuelles Recht angepasst.
- LuftSiG-Sicherheitsprogramm nicht auf neue EU-DVO aktualisiert.
- Insolvenzfrühzeichen bei regionalen Flughäfen unterschätzt.
- Verfahrensfristen im Planfeststellungsverfahren versäumt.
- Planfeststellungsbeschluss nicht vollständig umgesetzt; Auflagen aus Lärmschutzbereich vergessen.
- Dritte (Anwohner) fristgerecht Klage erhoben; aufschiebende Wirkung ignoriert.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Vermerk zu Flughafen – Register auswerten mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-033-flughafen-pfandrecht-vorbereiten`

**Fokus:** Kreditgeber will Sicherheiten an Flughafen-Infrastruktur bestellen. Skill prueft Grundbuchrecht Hypothek Grundschuld GBO LuftVG-Betreiberpflichten und Abgrenzung vom Luftfahrzeugpfandrecht und liefert Sicherungsstrategie-Vermerk fuer Flughafen-Finanzierung.

# Flughafen – Pfandrecht vorbereiten

## Mandantenfall

- Bank finanziert Terminalerweiterung; will Grundschuld an Flughafengelände bestellen; Eigentümerstruktur (Bund/Land/Privat) komplex.
- Leasinggeber will Grundschuld an Passagierterminal; Frage ob Pfandrecht oder Nießbrauch besser geeignet.
- Investoren-Konsortium prüft Flughafenübernahme; Sicherheiten-Struktur muss vor Signing feststehen.

## Erste Schritte

1. Sachverhalt strukturieren: Flughafen Art des Problems beteiligte Behörden Fristen.
2. Planfeststellungsstatus prüfen: LuftVG § 6/8 Genehmigung Auflagen aktuell.
3. Grundbuch und Eigentümerstruktur klären: kommunal staatlich privatwirtschaftlich.
4. LuftSiG-Sicherheitsprogramm auf Aktualität prüfen: EU-DVO 2015/1998 Anforderungen.
5. Finanzlage einschätzen: EU-Beihilferechtsstatus Subventionen Darlehen.
6. Handlungsbedarf dokumentieren: Vermerk mit Fristenstand und Empfehlungen.

## Rechtsrahmen

- **LuftVG §§ 6-8**: Flugplatzgenehmigung und Planfeststellungspflicht.
- **LuftVG § 10**: Wirkung des Planfeststellungsbeschlusses.
- **LuftSiG § 8**: Sicherheitspflichten des Flugplatzbetreibers.
- **EU-DVO 2015/1998**: Technische Sicherheitsanforderungen.
- **FluglärmG §§ 2-9**: Lärmschutzbereiche und Schallschutzansprüche.
- **InsO §§ 15a 17-19**: Insolvenzantragspflicht.
- **VwVfG §§ 72-78**: Planfeststellungsverfahren.
- **LuftVG § 6**: Genehmigung des Flughafenbetriebs; sachliche und persönliche Voraussetzungen.
- **LuftVG § 8**: Planfeststellungsverfahren für Flughafenausbau; UVP-Pflicht.
- **LuftVG § 9**: Planfeststellungsbeschluss; Drittwirkung und Bestandsschutz.
- **FluglärmG § 4**: Lärmschutzbereiche; Tagschutzzonen 1 und 2 sowie Nachtschutzzone.
- **VwVfG § 72**: Planfeststellungsverfahren allgemein; Beteiligungsrechte betroffener Dritter.
## Prüfraster

1. Ist Planfeststellungsbeschluss aktuell und vollständig umgesetzt?
2. Sind LuftSiG-Sicherheitsprogramme auf aktuellem EU-DVO-Stand?
3. Ist Grundbuchsituation und Eigentümerstruktur klar?
4. Bestehen offene Klagen oder Einwendungsverfahren?
5. Zeigen Finanzkennzahlen Insolvenzfrühzeichen?
6. Sind alle Auflagen aus Planfeststellungsbeschluss fristgerecht erfüllt?
7. Ist eine UVP nach UVPG § 4 durchgeführt und aktuell?
8. Sind Lärmschutzbereiche nach FluglärmG § 4 neu zu ermitteln nach Bauerweiterung?
## Typische Fallstricke

- Planfeststellungsauflagen veraltet und nicht auf aktuelles Recht angepasst.
- LuftSiG-Sicherheitsprogramm nicht auf neue EU-DVO aktualisiert.
- Insolvenzfrühzeichen bei regionalen Flughäfen unterschätzt.
- Verfahrensfristen im Planfeststellungsverfahren versäumt.
- Planfeststellungsbeschluss nicht vollständig umgesetzt; Auflagen aus Lärmschutzbereich vergessen.
- Dritte (Anwohner) fristgerecht Klage erhoben; aufschiebende Wirkung ignoriert.

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Vermerk zu Flughafen – Pfandrecht vorbereiten mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
