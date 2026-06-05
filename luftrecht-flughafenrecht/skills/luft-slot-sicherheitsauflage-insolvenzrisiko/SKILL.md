---
name: luft-slot-sicherheitsauflage-insolvenzrisiko
description: "Luft Slot Sicherheitsauflage Insolvenzrisiko: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Slot Sicherheitsauflage Insolvenzrisiko

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Slot Sicherheitsauflage Insolvenzrisiko** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-106-slot-sicherheitsauflage-bewerten` | Slot-Zuweisung ist mit Auflagen verbunden oder Slot-Nutzung wird durch LuftSiG-Auflage eingeschraenkt. Skill prueft VO EWG 95/93 Auflagen-Moeglichkeiten LuftSiG-Verbot und Verhaeltnismaessigkeit und liefert Auflagen-Bewertungs-Vermerk. |
| `luft-107-slot-insolvenzrisiko-markieren` | Insolvente oder insolvenznahe Airline hat wertvolle Slot-Portfolio. Skill prueft EuGH C-272/06 Slots keine Vermoegenswerte InsO-Folgen Fluko-Einziehung und Restrukturierungs-Optionen und liefert Risikoampel fuer Glaeubiger und Investoren. |
| `luft-108-slot-local-counsel-briefen` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Slot-Mandat briefen: Slot-Zuweisung Insolvenz oder Wechsel von koordiniertem Flughafen. Skill erstellt englisches Briefing-Memo mit deutschem Slot-Recht EU-VO und konkreten Fragen. |
| `luft-109-slot-dashboard-bauen` | Airline braucht Slot-Dashboard fuer laufendes Saison-Management: Bestand Nutzungsquote Waiver-Status Fristen Koordinierungsantraege. Skill strukturiert Datenquellen Fluko VO EWG 95/93 und liefert befuellbares Slot-Management-Dashboard. |
| `luft-110-slot-mandantenmemo-schreiben` | Anwalt schreibt Mandantenmemo fuer Airline zu Slot-Verlust Use-it-or-lose-it Waiver-Ablehnung oder Slot-Insolvenzfragen. Skill strukturiert Memo mit Sachverhalt Slot-Recht Handlungsoptionen und Empfehlung. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Slot Sicherheitsauflage Insolvenzrisiko**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-106-slot-sicherheitsauflage-bewerten`

**Fokus:** Slot-Zuweisung ist mit Auflagen verbunden oder Slot-Nutzung wird durch LuftSiG-Auflage eingeschraenkt. Skill prueft VO EWG 95/93 Auflagen-Moeglichkeiten LuftSiG-Verbot und Verhaeltnismaessigkeit und liefert Auflagen-Bewertungs-Vermerk.

# Slot – Sicherheitsauflage bewerten

## Mandantenfall

- Fluko erteilt Slot mit Nachtflug-Beschränkung als Auflage; Airline will anfechten.
- LuftSiG-Auflage beschränkt Betrieb in bestimmten Zeitfenstern; Slot-Nutzung gefährdet.
- Behörde ordnet Sicherheitscheck für alle Nachtflüge an; Slot-Nutzungsquote unterschritten.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 Art. 10 LuftVG §§ 27a-27d LuftSiG VwVfG § 36.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 Art. 10 LuftVG §§ 27a-27d LuftSiG VwVfG § 36 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Output

Strukturierter Vermerk zu Slot – Sicherheitsauflage bewerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
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

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-107-slot-insolvenzrisiko-markieren`

**Fokus:** Insolvente oder insolvenznahe Airline hat wertvolle Slot-Portfolio. Skill prueft EuGH C-272/06 Slots keine Vermoegenswerte InsO-Folgen Fluko-Einziehung und Restrukturierungs-Optionen und liefert Risikoampel fuer Glaeubiger und Investoren.

# Slot – Insolvenzrisiko markieren

## Mandantenfall

- Airline ist insolvent; Insolvenzverwalter fragt ob Slot-Portfolio wertvoll ist und gerettet werden kann.
- Investor prüft Airline-Übernahme hauptsächlich wegen der wertvollen Slots an Heathrow.
- Gläubiger fragt ob Slots in der Insolvenz-Verteilung berücksichtigt werden können.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: InsO §§ 15a 17-19 EuGH C-272/06 VO EWG 95/93 LuftVG §§ 27a-27d.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

InsO §§ 15a 17-19 EuGH C-272/06 VO EWG 95/93 LuftVG §§ 27a-27d – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Output

Strukturierter Vermerk zu Slot – Insolvenzrisiko markieren mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
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

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-108-slot-local-counsel-briefen`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Slot-Mandat briefen: Slot-Zuweisung Insolvenz oder Wechsel von koordiniertem Flughafen. Skill erstellt englisches Briefing-Memo mit deutschem Slot-Recht EU-VO und konkreten Fragen.

# Slot – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll in UK Local Counsel briefen für Slot-Streit an Heathrow mit deutschem Carrier.
- Britische Airline fragt nach deutschen Slot-Koordinierungsregeln für neuen Einstieg in Frankfurt.
- Insolvenzverwalter beauftragt Kanzlei in Irland für Slot-Restrukturierung nach Airline-Insolvenz.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 LuftVG §§ 27a-27d FHKV EuGH C-272/06 InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 LuftVG §§ 27a-27d FHKV EuGH C-272/06 InsO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Output

Strukturierter Vermerk zu Slot – Local Counsel briefen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
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

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-109-slot-dashboard-bauen`

**Fokus:** Airline braucht Slot-Dashboard fuer laufendes Saison-Management: Bestand Nutzungsquote Waiver-Status Fristen Koordinierungsantraege. Skill strukturiert Datenquellen Fluko VO EWG 95/93 und liefert befuellbares Slot-Management-Dashboard.

# Slot – Dashboard bauen

## Mandantenfall

- Airline mit Betrieb an 5 koordinierten Flughäfen braucht Dashboard für Slot-Nutzungsquoten und Fristen.
- Insolvenzverwalter übernimmt Airline; Dashboard für sofortigen Überblick über Slot-Portfolio.
- Investor kauft Airline; Slot-Dashboard als Teil der Due Diligence.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 LuftVG §§ 27a-27d FHKV Fluko.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 LuftVG §§ 27a-27d FHKV Fluko – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Strukturierter Vermerk zu Slot – Dashboard bauen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
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

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-110-slot-mandantenmemo-schreiben`

**Fokus:** Anwalt schreibt Mandantenmemo fuer Airline zu Slot-Verlust Use-it-or-lose-it Waiver-Ablehnung oder Slot-Insolvenzfragen. Skill strukturiert Memo mit Sachverhalt Slot-Recht Handlungsoptionen und Empfehlung.

# Slot – Mandantenmemo schreiben

## Mandantenfall

- Airline verliert Grandfather-Slots wegen Unterschreitung der Use-it-or-lose-it-Quote; Memo über Rechtsmittel.
- Waiver-Antrag abgelehnt; Memo über Klage und Chancenabwägung.
- Insolvenzverwalter braucht Memo: Was passiert mit Slots in der Insolvenz.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: VO EWG 95/93 Art. 8 10 12 EuGH C-272/06 InsO LuftVG §§ 27a-27d.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

VO EWG 95/93 Art. 8 10 12 EuGH C-272/06 InsO LuftVG §§ 27a-27d – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Output

Strukturierter Vermerk zu Slot – Mandantenmemo schreiben mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
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

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
