---
name: luft-drohne-pfandrecht-pfaendung-planen
description: "Luft Drohne Pfandrecht Pfaendung Planen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Drohne Pfandrecht Pfaendung Planen

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Drohne Pfandrecht Pfaendung Planen** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-073-drohne-pfandrecht-vorbereiten` | Kreditgeber will Pfandrecht an teurer Drohne oder Drohnenflotte als Sicherheit bestellen. Prueft BGB §§ 1204 ff. Mobiliarpfandrecht LuftVG § 21a Registrierungsstatus und Cape-Town-Abgrenzung und liefert Sicherungsstruktur-Vermerk. |
| `luft-074-drohne-pfaendung-planen` | Glaeubiger will gewerbliche Drohne oder Drohnenflotte pfaenden. Prueft ZPO § 808 Mobiliarpfaendung BGB-Eigentumsrecht Sicherungsübereignung und LuftVG § 21a Registrierungsstatus und liefert Pfaendungsplan. |
| `luft-075-drohne-genehmigung-pruefen` | Drohnenbetreiber braucht Genehmigung fuer Spezialoperationen oder hat Betriebsgenehmigung verloren. Prueft EU-VO 2019/947 Betriebskategorien LuftVG § 21a LBA-Genehmigungsverfahren und Specific Category Operational Authorization und liefert Genehmigungsstatus-Vermerk. |
| `luft-076-drohne-sicherheitsauflage-bewerten` | Drohnenbetreiber erhaelt LBA oder Landesbehoerden-Auflage nach Drohnenvorfall oder Routineinspektion. Prueft EU-VO 2019/947 LuftVG § 21a Verhaeltnismaessigkeit der Auflage und Widerspruchsmoeglichkeit und liefert Auflagen-Bewertungs-Vermerk. |
| `luft-077-drohne-insolvenzrisiko-markieren` | Drohnendienstleister zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 Insolvenzantragspflicht Aussonderungsrechte Leasinggeber bei Drohnenflotte und Kundenforderungen und liefert Risikoampel-Bewertung. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Drohne Pfandrecht Pfaendung Planen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-073-drohne-pfandrecht-vorbereiten`

**Fokus:** Kreditgeber will Pfandrecht an teurer Drohne oder Drohnenflotte als Sicherheit bestellen. Prueft BGB §§ 1204 ff. Mobiliarpfandrecht LuftVG § 21a Registrierungsstatus und Cape-Town-Abgrenzung und liefert Sicherungsstruktur-Vermerk.

# Drohne – Pfandrecht vorbereiten

## Mandantenfall

- Bank finanziert Kauf einer teuren Industrie-Drohne; will Sicherheit bestellen; Drohne ist nicht in Luftfahrzeugrolle.
- Leasinggesellschaft verleast Drohnenflotte; will Sicherungsübereignung statt Pfandrecht.
- Drohnenhersteller gibt Händlerkredit; Eigentumsvorbehalt vs. Pfandrecht abwägen.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BGB §§ 1204 ff. BGB §§ 929 930 Sicherungsübereignung LuftVG § 21a.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BGB §§ 1204 ff. BGB §§ 929 930 Sicherungsübereignung LuftVG § 21a – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EU-VO 2019/947 Art. 5**: Betriebskategorien offene spezifische zertifizierte Kategorie; Abgrenzungskriterien.
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

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Strukturierter Vermerk zu Drohne – Pfandrecht vorbereiten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
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

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-074-drohne-pfaendung-planen`

**Fokus:** Glaeubiger will gewerbliche Drohne oder Drohnenflotte pfaenden. Prueft ZPO § 808 Mobiliarpfaendung BGB-Eigentumsrecht Sicherungsübereignung und LuftVG § 21a Registrierungsstatus und liefert Pfaendungsplan.

# Drohne – Pfändung planen

## Mandantenfall

- Gläubiger will Drohnenflotte eines insolventen Drohnendienstleisters pfänden; Finanzier hat Sicherungsübereignung.
- Gerichtsvollzieher findet Drohne nicht im Lager; Eigentümer behauptet Drohne sei verleast.
- Drohne wird in der Luft betrieben; Gläubiger fragt wann und wo Pfändung möglich.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: ZPO § 808 InsO §§ 47 89 BGB §§ 929 930 LuftVG § 21a.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

ZPO § 808 InsO §§ 47 89 BGB §§ 929 930 LuftVG § 21a – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EU-VO 2019/947 Art. 5**: Betriebskategorien offene spezifische zertifizierte Kategorie; Abgrenzungskriterien.
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

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Strukturierter Vermerk zu Drohne – Pfändung planen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
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

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-075-drohne-genehmigung-pruefen`

**Fokus:** Drohnenbetreiber braucht Genehmigung fuer Spezialoperationen oder hat Betriebsgenehmigung verloren. Prueft EU-VO 2019/947 Betriebskategorien LuftVG § 21a LBA-Genehmigungsverfahren und Specific Category Operational Authorization und liefert Genehmigungsstatus-Vermerk.

# Drohne – Genehmigung prüfen

## Mandantenfall

- Drohnenbetreiber will Flüge über Menschenansammlungen durchführen; welche Specific-Category-Genehmigung nötig.
- LBA hat Betriebsgenehmigung widerrufen; Mandant fragt nach Widerspruchsmöglichkeit.
- Neuer Drohnenbetreiber fragt welche Genehmigungen er für kommerziellen Betrieb benötigt.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-VO 2019/947 Art. 12 LuftVG § 21a EASA Specific Category STS-Szenarien.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-VO 2019/947 Art. 12 LuftVG § 21a EASA Specific Category STS-Szenarien – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Output

Strukturierter Vermerk zu Drohne – Genehmigung prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
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

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-076-drohne-sicherheitsauflage-bewerten`

**Fokus:** Drohnenbetreiber erhaelt LBA oder Landesbehoerden-Auflage nach Drohnenvorfall oder Routineinspektion. Prueft EU-VO 2019/947 LuftVG § 21a Verhaeltnismaessigkeit der Auflage und Widerspruchsmoeglichkeit und liefert Auflagen-Bewertungs-Vermerk.

# Drohne – Sicherheitsauflage bewerten

## Mandantenfall

- LBA hat nach Drohnenvorfall Auflagen zur Flugbeschränkung erteilt; Mandant fragt ob verhältnismäßig.
- Drohnenbetreiber erhält neue U-Space-Anforderungen; Umsetzungskosten erheblich.
- Behörde beanstandet Drohnenbetrieb wegen fehlender Haftpflichtversicherung.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-VO 2019/947 LuftVG § 21a EU-VO 785/2004 VwVfG § 36.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-VO 2019/947 LuftVG § 21a EU-VO 785/2004 VwVfG § 36 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Output

Strukturierter Vermerk zu Drohne – Sicherheitsauflage bewerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
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

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-077-drohne-insolvenzrisiko-markieren`

**Fokus:** Drohnendienstleister zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 Insolvenzantragspflicht Aussonderungsrechte Leasinggeber bei Drohnenflotte und Kundenforderungen und liefert Risikoampel-Bewertung.

# Drohne – Insolvenzrisiko markieren

## Mandantenfall

- Drohnendienstleister zahlt Leasingraten nicht; Leasinggeber fragt nach Herausgaberecht.
- Drohnen-Startup hat Cash-Probleme; Geschäftsführer fragt nach Insolvenzantragspflicht.
- Kunde des Drohnendienstleisters hat Vorauszahlungen geleistet; Insolvenz droht.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: InsO §§ 15a 17-19 47 BGB §§ 929 930 EU-VO 785/2004.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

InsO §§ 15a 17-19 47 BGB §§ 929 930 EU-VO 785/2004 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **EU-VO 2019/947 Art. 5**: Betriebskategorien offene spezifische zertifizierte Kategorie; Abgrenzungskriterien.
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

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Output

Strukturierter Vermerk zu Drohne – Insolvenzrisiko markieren mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
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

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
