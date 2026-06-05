---
name: luft-acc3-genehmigung-sicherheitsauflage
description: "Luft Acc3 Genehmigung Sicherheitsauflage: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Acc3 Genehmigung Sicherheitsauflage

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Acc3 Genehmigung Sicherheitsauflage** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-095-acc3-genehmigung-pruefen` | ACC3-Carrier prueft Designierungsstatus und ob alle erforderlichen Genehmigungen fuer Drittland-Fracht-Betrieb vorliegen. Prueft EU-DVO 2015/1998 EU-VO 300/2008 Validierungsgueltigkeit und LuftVG-Betriebsgenehmigung und liefert Genehmigungsstatus-Vermerk. |
| `luft-096-acc3-sicherheitsauflage-bewerten` | ACC3-Carrier erhaelt Sicherheitsauflage nach EU-Luftsicherheits-Inspektion. Prueft EU-DVO 2015/1998 Findings-Kategorien EU-VO 300/2008 LuftSiG § 9 Verhaeltnismaessigkeit und liefert Auflagen-Bewertungs-Vermerk und Corrective-Action-Plan fuer ACC3-Betrieb. |
| `luft-097-acc3-insolvenzrisiko-markieren` | ACC3-Carrier zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 EU-VO 1008/2008 Art. 9 Betriebsgenehmigung Cape-Town-Remedies und liefert Risikoampel fuer Glaeubiger und Geschaeftspartner des ACC3-Carriers. |
| `luft-098-acc3-local-counsel-briefen` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer ACC3-Mandat briefen: Designierungsverlust Sicherheitsauflage oder Carrier-Insolvenz. Skill erstellt englisches Briefing-Memo mit EU-Sicherheitsrecht und konkreten Fragen. |
| `luft-099-acc3-dashboard-bauen` | ACC3-Carrier braucht Compliance-Dashboard: Designierungsstatus Validierungsgueltigkeit RA3/KC3-Datenbank Sicherheitsfindings. Skill strukturiert Datenquellen EU-Datenbanken EU-DVO 2015/1998 und liefert befuellbares Compliance-Dashboard. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Acc3 Genehmigung Sicherheitsauflage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-095-acc3-genehmigung-pruefen`

**Fokus:** ACC3-Carrier prueft Designierungsstatus und ob alle erforderlichen Genehmigungen fuer Drittland-Fracht-Betrieb vorliegen. Prueft EU-DVO 2015/1998 EU-VO 300/2008 Validierungsgueltigkeit und LuftVG-Betriebsgenehmigung und liefert Genehmigungsstatus-Vermerk.

# ACC3 – Genehmigung prüfen

## Mandantenfall

- ACC3-Carrier fragt ob seine Designierung für neue Strecken aus Drittland gilt oder neue Validierung nötig ist.
- Behörde stellt fest dass ACC3-Validierung abgelaufen ist; Carrier fragt wie Betrieb aufrechterhalten werden kann.
- Neuer Frachtcarrier will ACC3-Status erlangen; Prüfung der Genehmigungsvoraussetzungen.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-DVO 2015/1998 EU-VO 300/2008 LuftVG EASA Part-OPS.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-DVO 2015/1998 EU-VO 300/2008 LuftVG EASA Part-OPS – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Output

Strukturierter Vermerk zu ACC3 – Genehmigung prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-096-acc3-sicherheitsauflage-bewerten`

**Fokus:** ACC3-Carrier erhaelt Sicherheitsauflage nach EU-Luftsicherheits-Inspektion. Prueft EU-DVO 2015/1998 Findings-Kategorien EU-VO 300/2008 LuftSiG § 9 Verhaeltnismaessigkeit und liefert Auflagen-Bewertungs-Vermerk und Corrective-Action-Plan fuer ACC3-Betrieb.

# ACC3 – Sicherheitsauflage bewerten

## Mandantenfall

- ACC3-Carrier erhält nach EU-Inspektion Finding zu unzureichender Screening-Dokumentation; 30-Tage-Frist.
- EU-Validierungsprüfer stellt Non-Conformity fest; ACC3-Designierung droht entzogen zu werden.
- Neue EU-Anforderungen zu Vor-Screening an Drittland-Flughäfen treten in Kraft; Carrier braucht Umsetzungsplan.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 EASA.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 EASA – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Output

Strukturierter Vermerk zu ACC3 – Sicherheitsauflage bewerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-097-acc3-insolvenzrisiko-markieren`

**Fokus:** ACC3-Carrier zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 EU-VO 1008/2008 Art. 9 Betriebsgenehmigung Cape-Town-Remedies und liefert Risikoampel fuer Glaeubiger und Geschaeftspartner des ACC3-Carriers.

# ACC3 – Insolvenzrisiko markieren

## Mandantenfall

- ACC3-Carrier zahlt Handling-Fees nicht; Flughäfen drohen mit Betriebsunterbrechung.
- Kreditgeber beobachtet sinkende Auslastung des ACC3-Carriers; will Risikoampel.
- ACC3-Carrier stellt Insolvenzantrag; Kunden fragen ob Fracht-Handling noch sichergestellt ist.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: InsO §§ 15a 17-19 47 EU-VO 1008/2008 Art. 9 EU-DVO 2015/1998.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

InsO §§ 15a 17-19 47 EU-VO 1008/2008 Art. 9 EU-DVO 2015/1998 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EU-VO 300/2008 Art. 6**: Grundsatz der Gleichwertigkeit; Drittstaaten-Maßnahmen.
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

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Output

Strukturierter Vermerk zu ACC3 – Insolvenzrisiko markieren mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-098-acc3-local-counsel-briefen`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer ACC3-Mandat briefen: Designierungsverlust Sicherheitsauflage oder Carrier-Insolvenz. Skill erstellt englisches Briefing-Memo mit EU-Sicherheitsrecht und konkreten Fragen.

# ACC3 – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll in UAE Local Counsel briefen für ACC3-Carrier nach Designierungsverlust.
- Europäischer Carrier fragt nach ACC3-Anforderungen für neuen Drittland-Flughafen.
- Insolvenzverwalter beauftragt Kanzlei in Singapur für Fracht-Rückholung nach Insolvenz eines ACC3.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-DVO 2015/1998 EU-VO 300/2008 LuftVG InsO Cape Town Convention.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-DVO 2015/1998 EU-VO 300/2008 LuftVG InsO Cape Town Convention – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Output

Strukturierter Vermerk zu ACC3 – Local Counsel briefen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-099-acc3-dashboard-bauen`

**Fokus:** ACC3-Carrier braucht Compliance-Dashboard: Designierungsstatus Validierungsgueltigkeit RA3/KC3-Datenbank Sicherheitsfindings. Skill strukturiert Datenquellen EU-Datenbanken EU-DVO 2015/1998 und liefert befuellbares Compliance-Dashboard.

# ACC3 – Dashboard bauen

## Mandantenfall

- ACC3-Carrier mit Betrieb an 4 Drittland-Flughäfen braucht Dashboard für Validierungsstatus.
- Behörde verlangt Compliance-Reporting des ACC3; Dashboard als strukturierte Grundlage.
- Investor prüft ACC3-Carrier; Dashboard für Due Diligence zu Designierungsstatus und Sicherheitsfindings.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 EU-ACC3-Datenbank.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 EU-ACC3-Datenbank – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Strukturierter Vermerk zu ACC3 – Dashboard bauen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
