---
name: luft-acc3-mandantenmemo-slot-register
description: "Luft Acc3 Mandantenmemo Slot Register: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Acc3 Mandantenmemo Slot Register

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Acc3 Mandantenmemo Slot Register** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-100-acc3-mandantenmemo-schreiben` | Anwalt schreibt Mandantenmemo fuer ACC3-Carrier zu Designierungsverlust Sicherheitsauflage Insolvenznaehe oder Validierungsfehler. Skill strukturiert Memo mit Sachverhalt EU-Sicherheitsrecht Handlungsoptionen und Empfehlung. |
| `luft-102-slot-register-auswerten` | Mandant will Slot-Bestand einer Airline fuer Sommer- oder Wintersaison bei Fluko auswerten. Prueft VO EWG 95/93 Grandfather Rights Use-it-or-lose-it Slot-Pool und Fluko-Daten und liefert Slot-Portfolio-Analyse mit Nutzungsquoten. |
| `luft-103-slot-pfandrecht-vorbereiten` | Kreditgeber fragt ob Slots als Sicherheit dienen koennen. Skill prueft VO EWG 95/93 Slot-Nicht-Uebertragbarkeit EuGH-Rechtsprechung und alternative Sicherheiten fuer Airline-Finanzierung und liefert Sicherungs-Alternativen-Vermerk. |
| `luft-104-slot-pfaendung-planen` | Glaeubiger will Slots einer Airline pfaenden. Skill prueft VO EWG 95/93 Slot-Nicht-Pfaendbarkeit EuGH C-272/06 und ZPO-Pfaendungsrecht sowie Alternativen und liefert Rechtsgutachten zur Slot-Pfaendbarkeit. |
| `luft-105-slot-genehmigung-pruefen` | Airline braucht Slot-Bestätigung oder neuen Slot und prueft Genehmigungsstand. Prueft VO EWG 95/93 Grandfather Rights Koordinierungsstand FHKV IATA-WSAG Saisonantrag und liefert Slot-Bedarfs-Analyse und Antrags-Checkliste. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Acc3 Mandantenmemo Slot Register**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-100-acc3-mandantenmemo-schreiben`

**Fokus:** Anwalt schreibt Mandantenmemo fuer ACC3-Carrier zu Designierungsverlust Sicherheitsauflage Insolvenznaehe oder Validierungsfehler. Skill strukturiert Memo mit Sachverhalt EU-Sicherheitsrecht Handlungsoptionen und Empfehlung.

# ACC3 – Mandantenmemo schreiben

## Mandantenfall

- ACC3-Carrier verliert Designierung nach Inspektion; Memo über Rechtsmittel und Betriebsunterbrechungsfolgen.
- ACC3-Carrier erhält Level-1-Finding; Memo über sofortigen Handlungsbedarf und Eskalationsstufen.
- Insolvenz des ACC3-Carriers: Memo für Vorstand über Haftungsrisiken und Ablauf.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-DVO 2015/1998 EU-VO 300/2008 LuftVG LuftSiG § 9 InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-DVO 2015/1998 EU-VO 300/2008 LuftVG LuftSiG § 9 InsO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftSiG § 3c**: Nationale Umsetzung der EU-Sicherheitsarchitektur; Zuständigkeit LBA.
- **ICAO Annex 17 Std. 4.6**: Frachtsicherheitskette; Verantwortung des Luftfrachtführers.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist der EU-Validator zugelassen und sein Bericht nicht älter als 3 Jahre?
8. Sind alle Sub-Auftragnehmer in der Lieferkette als RA oder KC anerkannt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- ACC3-Validierungsbericht abgelaufen; Flights ab EU-Flughafen verboten bis Erneuerung.
- Sub-Auftragnehmer ohne KC-Status in Sicherheitsnachweis gelistet; ungültige Sicherheitserklärung.

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Output

Strukturierter Vermerk zu ACC3 – Mandantenmemo schreiben mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-DVO 2015/1998: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32015R1998
- LBA ACC3: https://www.lba.de
- ICAO: https://www.icao.int/Security/SFP/Pages/default.aspx

## Hinweise für die Praxis

Dieser Skill deckt den Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-102-slot-register-auswerten`

**Fokus:** Mandant will Slot-Bestand einer Airline fuer Sommer- oder Wintersaison bei Fluko auswerten. Prueft VO EWG 95/93 Grandfather Rights Use-it-or-lose-it Slot-Pool und Fluko-Daten und liefert Slot-Portfolio-Analyse mit Nutzungsquoten.

# Slot – Register auswerten

## Mandantenfall

- Airline prüft vor Saisonstart ob alle historischen Slots korrekt bestätigt sind.
- Investor kauft Airline; Due Diligence des Slot-Portfolios als Werttreiber.
- Insolvenzverwalter braucht Übersicht über Slot-Bestand; Frage der Übertragbarkeit.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 LuftVG §§ 27a-27d FHKV EuGH C-272/06.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 LuftVG §§ 27a-27d FHKV EuGH C-272/06 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **VO EWG 95/93 Art. 8**: Historische Slots (Grandfather Rights); Nutzungsquote 80/20.
- **LuftVG § 27a**: Deutsche Koordinierungsstelle (Fluko); Rechtsstellung und Aufgaben.
- **BVerwG Urt. v. 26.01.2012 – 3 C 8.11**: Slot-Entzug als Verwaltungsakt; Rechtsweg VG.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die 80/20-Nutzungsquote (VO EWG 95/93 Art. 8) im letzten IATA-Season eingehalten?
8. Sind Force-Majeure-Ausnahmen (COVID-Pandemie-Sonderregeln) korrekt beantragt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Slot-Rückgabe zu spät angezeigt; keine Waiver-Ausnahme mehr möglich.
- Slot-Übertragung als privatrechtlich behandelt; VO EWG 95/93 erlaubt keine freie Übertragung.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Slot – Register auswerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- VO EWG 95/93: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31993R0095
- LBA/Fluko: https://www.lba.de
- BVerwG: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Slot-Koordination und Flughafenkapazität ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-103-slot-pfandrecht-vorbereiten`

**Fokus:** Kreditgeber fragt ob Slots als Sicherheit dienen koennen. Skill prueft VO EWG 95/93 Slot-Nicht-Uebertragbarkeit EuGH-Rechtsprechung und alternative Sicherheiten fuer Airline-Finanzierung und liefert Sicherungs-Alternativen-Vermerk.

# Slot – Pfandrecht vorbereiten

## Mandantenfall

- Bank will Slots einer Airline als Kreditsicherheit; Mandant fragt ob das rechtlich möglich ist.
- Airline will Slots an Dritte verpfänden um Liquidität zu gewinnen; Frage der rechtlichen Möglichkeit.
- Insolvenzverwalter prüft ob Slots für Sanierungsplan verwertet werden können.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 Art. 8a LuftVG §§ 27a-27d EuGH C-272/06 InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 Art. 8a LuftVG §§ 27a-27d EuGH C-272/06 InsO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 27a**: Deutsche Koordinierungsstelle (Fluko); Rechtsstellung und Aufgaben.
- **BVerwG Urt. v. 26.01.2012 – 3 C 8.11**: Slot-Entzug als Verwaltungsakt; Rechtsweg VG.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die 80/20-Nutzungsquote (VO EWG 95/93 Art. 8) im letzten IATA-Season eingehalten?
8. Sind Force-Majeure-Ausnahmen (COVID-Pandemie-Sonderregeln) korrekt beantragt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Slot-Rückgabe zu spät angezeigt; keine Waiver-Ausnahme mehr möglich.
- Slot-Übertragung als privatrechtlich behandelt; VO EWG 95/93 erlaubt keine freie Übertragung.

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Strukturierter Vermerk zu Slot – Pfandrecht vorbereiten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- VO EWG 95/93: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31993R0095
- LBA/Fluko: https://www.lba.de
- BVerwG: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Slot-Koordination und Flughafenkapazität ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-104-slot-pfaendung-planen`

**Fokus:** Glaeubiger will Slots einer Airline pfaenden. Skill prueft VO EWG 95/93 Slot-Nicht-Pfaendbarkeit EuGH C-272/06 und ZPO-Pfaendungsrecht sowie Alternativen und liefert Rechtsgutachten zur Slot-Pfaendbarkeit.

# Slot – Pfändung planen

## Mandantenfall

- Gläubiger beantragt Pfändung der Slots einer Airline nach Urteil; Vollstreckungsgericht fragt nach Vollstreckungsgegenstand.
- Insolvenzverwalter prüft ob Slot-Pool-Zuweisung für Insolvenz-Plan genutzt werden kann.
- Airline-Käufer will sicherstellen dass Slots auf ihn übergehen; rechtliche Gestaltungsfrage.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 EuGH C-272/06 ZPO InsO LuftVG §§ 27a-27d.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 EuGH C-272/06 ZPO InsO LuftVG §§ 27a-27d – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **VO EWG 95/93 Art. 8**: Historische Slots (Grandfather Rights); Nutzungsquote 80/20.
- **LuftVG § 27a**: Deutsche Koordinierungsstelle (Fluko); Rechtsstellung und Aufgaben.
- **BVerwG Urt. v. 26.01.2012 – 3 C 8.11**: Slot-Entzug als Verwaltungsakt; Rechtsweg VG.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die 80/20-Nutzungsquote (VO EWG 95/93 Art. 8) im letzten IATA-Season eingehalten?
8. Sind Force-Majeure-Ausnahmen (COVID-Pandemie-Sonderregeln) korrekt beantragt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Slot-Rückgabe zu spät angezeigt; keine Waiver-Ausnahme mehr möglich.
- Slot-Übertragung als privatrechtlich behandelt; VO EWG 95/93 erlaubt keine freie Übertragung.

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Strukturierter Vermerk zu Slot – Pfändung planen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- VO EWG 95/93: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31993R0095
- LBA/Fluko: https://www.lba.de
- BVerwG: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Slot-Koordination und Flughafenkapazität ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-105-slot-genehmigung-pruefen`

**Fokus:** Airline braucht Slot-Bestätigung oder neuen Slot und prueft Genehmigungsstand. Prueft VO EWG 95/93 Grandfather Rights Koordinierungsstand FHKV IATA-WSAG Saisonantrag und liefert Slot-Bedarfs-Analyse und Antrags-Checkliste.

# Slot – Genehmigung prüfen

## Mandantenfall

- Airline will neue Strecke aufnehmen; fragt welche Slots verfügbar sind und wie man sie beantragt.
- Airline hat Grandfather-Right-Slots aber Betrieb ruht; fragt ob Waiver-Antrag nötig ist.
- Neueinsteiger-Airline braucht Slots an Engpassflughafen; Prüfung der Pool-Zuteilungsregeln.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 Art. 8 10 12 LuftVG §§ 27a-27d FHKV IATA-WASG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 Art. 8 10 12 LuftVG §§ 27a-27d FHKV IATA-WASG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 27a**: Deutsche Koordinierungsstelle (Fluko); Rechtsstellung und Aufgaben.
- **BVerwG Urt. v. 26.01.2012 – 3 C 8.11**: Slot-Entzug als Verwaltungsakt; Rechtsweg VG.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die 80/20-Nutzungsquote (VO EWG 95/93 Art. 8) im letzten IATA-Season eingehalten?
8. Sind Force-Majeure-Ausnahmen (COVID-Pandemie-Sonderregeln) korrekt beantragt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Slot-Rückgabe zu spät angezeigt; keine Waiver-Ausnahme mehr möglich.
- Slot-Übertragung als privatrechtlich behandelt; VO EWG 95/93 erlaubt keine freie Übertragung.

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Output

Strukturierter Vermerk zu Slot – Genehmigung prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- VO EWG 95/93: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31993R0095
- LBA/Fluko: https://www.lba.de
- BVerwG: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Slot-Koordination und Flughafenkapazität ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
