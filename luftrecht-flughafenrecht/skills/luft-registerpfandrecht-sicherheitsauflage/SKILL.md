---
name: luft-registerpfandrecht-sicherheitsauflage
description: "Luft Registerpfandrecht Sicherheitsauflage: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Registerpfandrecht Sicherheitsauflage

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Registerpfandrecht Sicherheitsauflage** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-056-registerpfandrecht-sicherheitsauflage` | Pfandrecht-Glaeubigers Sicherheiten werden durch LuftSiG-Auflagen oder EASA-Massnahmen beeintraechtigt. Skill prueft wie Sicherheitsauflagen den Wert des Pfandobjekts beeinflussen welche Handlungsoptionen bestehen und liefert Risikobewertung und Vertragsklausel-Empfehlung. |
| `luft-057-registerpfandrecht-insolvenzrisiko-mar` | Schuldner zeigt Insolvenzzeichen; Pfandglaeubigerposition zu sichern. Prueft InsO §§ 21 50 89 Absonderungsrecht Vollstreckungssperre Cape-Town-Art. 30 Insolvenzschutz und liefert Risikoampel fuer Pfandglaeubiger und Reaktionsplan. |
| `luft-058-registerpfandrecht-local-counsel-brief` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Pfandrechts-Vollstreckungs-Mandat briefen: Rang-Analyse AG-Braunschweig-Register Cape-Town-Eintrag IDERA-Status. Skill erstellt englisches Briefing-Memo mit deutschem Pfandrechtsrecht und konkreten Fragen an Local Counsel. |
| `luft-059-registerpfandrecht-dashboard-bauen` | Pfandglaeubigerbank braucht Echtzeit-Dashboard fuer Pfandrechts-Portfolio: AG-Braunschweig-Status Cape-Town-Eintrag IDERA Schuldner-Solvenz Flugzeugwert. Skill strukturiert Datenquellen und liefert befuellbares Portfolio-Dashboard-Template. |
| `luft-060-registerpfandrecht-mandantenmemo-schre` | Anwalt schreibt Mandantenmemo fuer Pfandglaeubiger zu komplexem Pfandrechts-Fall: Rang-Konflikt Insolvenz Cape-Town-Default-Remedies oder Vollstreckungs-Hindernis. Skill strukturiert Memo mit Sachverhalt Rechtslage Handlungsoptionen und Empfehlung. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Registerpfandrecht Sicherheitsauflage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-056-registerpfandrecht-sicherheitsauflage`

**Fokus:** Pfandrecht-Glaeubigers Sicherheiten werden durch LuftSiG-Auflagen oder EASA-Massnahmen beeintraechtigt. Skill prueft wie Sicherheitsauflagen den Wert des Pfandobjekts beeinflussen welche Handlungsoptionen bestehen und liefert Risikobewertung und Vertragsklausel-Empfehlung.

# Registerpfandrecht – Sicherheitsauflage bewerten

## Mandantenfall

- Luftsicherheitsbehörde ordnet Umbaumaßnahmen an die Flugzeugwert reduzieren; Pfandgläubiger fragt nach Handlungsoptionen.
- EASA entzieht Musterzulassung eines Flugzeugtyps; gesamte Pfandrechts-Flotte verliert an Wert.
- LuftSiG-Auflage zu Nachrüstung verursacht hohe Kosten; Leasingnehmer zahlungsunfähig.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftSiG §§ 8-9 EU-DVO 2015/1998 EASA Basic Regulation Cape Town Convention Art. 9.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftSiG §§ 8-9 EU-DVO 2015/1998 EASA Basic Regulation Cape Town Convention Art. 9 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftFzgG § 1**: Begriffsbestimmung Luftfahrzeugpfandrecht; dingliches Recht nach deutschem Recht.
- **LuftFzgG § 4**: Pfandrechtseintragung beim AG Braunschweig; konstitutive Wirkung.
- **LuftFzgG § 25**: Pfandrechtsvollstreckung; Verwertung durch Versteigerung.
- **ZPO § 864**: Pfändung eingetragener Luftfahrzeuge; besonderer Vollstreckungsweg.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die Rangfolge konkurrierender Pfandrechte (national vs. Cape Town) klar ermittelt?
8. Ist das Pfandrecht bei Weiterveräußerung des Luftfahrzeugs erloschen (LuftFzgG § 27)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Nationaler Pfandrechtsrang ignoriert weil Cape-Town-Priorität falsch eingeschätzt.
- AG Braunschweig-Auszug veraltet; zwischenzeitlich eingetragene Nachrangpfandrechte übersehen.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Registerpfandrecht – Sicherheitsauflage bewerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfahrzeugpfandrecht und Register ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfahrzeugpfandrecht und Register sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-057-registerpfandrecht-insolvenzrisiko-mar`

**Fokus:** Schuldner zeigt Insolvenzzeichen; Pfandglaeubigerposition zu sichern. Prueft InsO §§ 21 50 89 Absonderungsrecht Vollstreckungssperre Cape-Town-Art. 30 Insolvenzschutz und liefert Risikoampel fuer Pfandglaeubiger und Reaktionsplan.

# Registerpfandrecht – Insolvenzrisiko markieren

## Mandantenfall

- Airline zahlt Kreditzinsen verspätet; Pfandgläubiger-Bank erwägt Kündigung des Kreditvertrags und Verwertung des Pfandrechts.
- Schuldner hat Insolvenzantrag gestellt; Pfandgläubiger fragt ob Verwertung noch möglich ist.
- Vorläufiger Insolvenzverwalter sichert Flugzeug; Pfandgläubiger will Herausgabe erwirken.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: InsO §§ 21 50 89 Cape Town Convention Art. 30 Aircraft Protocol Art. XI LuftFzgG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

InsO §§ 21 50 89 Cape Town Convention Art. 30 Aircraft Protocol Art. XI LuftFzgG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftFzgG § 1**: Begriffsbestimmung Luftfahrzeugpfandrecht; dingliches Recht nach deutschem Recht.
- **LuftFzgG § 4**: Pfandrechtseintragung beim AG Braunschweig; konstitutive Wirkung.
- **LuftFzgG § 25**: Pfandrechtsvollstreckung; Verwertung durch Versteigerung.
- **ZPO § 864**: Pfändung eingetragener Luftfahrzeuge; besonderer Vollstreckungsweg.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die Rangfolge konkurrierender Pfandrechte (national vs. Cape Town) klar ermittelt?
8. Ist das Pfandrecht bei Weiterveräußerung des Luftfahrzeugs erloschen (LuftFzgG § 27)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Nationaler Pfandrechtsrang ignoriert weil Cape-Town-Priorität falsch eingeschätzt.
- AG Braunschweig-Auszug veraltet; zwischenzeitlich eingetragene Nachrangpfandrechte übersehen.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Registerpfandrecht – Insolvenzrisiko markieren mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfahrzeugpfandrecht und Register ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfahrzeugpfandrecht und Register sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-058-registerpfandrecht-local-counsel-brief`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Pfandrechts-Vollstreckungs-Mandat briefen: Rang-Analyse AG-Braunschweig-Register Cape-Town-Eintrag IDERA-Status. Skill erstellt englisches Briefing-Memo mit deutschem Pfandrechtsrecht und konkreten Fragen an Local Counsel.

# Registerpfandrecht – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll in UK Local Counsel briefen für Vollstreckung aus deutschem Pfandrecht an in Großbritannien gestandenem Flugzeug.
- Irischer Leasinggeber fragt nach deutschem Pfandrecht als Sicherungsinstrument.
- Insolvenzverwalter braucht in Frankreich Vollstreckung aus deutschem Pfandrecht; Briefing nötig.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG Cape Town Convention InsO ZPO §§ 864-871.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG Cape Town Convention InsO ZPO §§ 864-871 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftFzgG § 1**: Begriffsbestimmung Luftfahrzeugpfandrecht; dingliches Recht nach deutschem Recht.
- **LuftFzgG § 4**: Pfandrechtseintragung beim AG Braunschweig; konstitutive Wirkung.
- **LuftFzgG § 25**: Pfandrechtsvollstreckung; Verwertung durch Versteigerung.
- **ZPO § 864**: Pfändung eingetragener Luftfahrzeuge; besonderer Vollstreckungsweg.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die Rangfolge konkurrierender Pfandrechte (national vs. Cape Town) klar ermittelt?
8. Ist das Pfandrecht bei Weiterveräußerung des Luftfahrzeugs erloschen (LuftFzgG § 27)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Nationaler Pfandrechtsrang ignoriert weil Cape-Town-Priorität falsch eingeschätzt.
- AG Braunschweig-Auszug veraltet; zwischenzeitlich eingetragene Nachrangpfandrechte übersehen.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Registerpfandrecht – Local Counsel briefen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfahrzeugpfandrecht und Register ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfahrzeugpfandrecht und Register sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-059-registerpfandrecht-dashboard-bauen`

**Fokus:** Pfandglaeubigerbank braucht Echtzeit-Dashboard fuer Pfandrechts-Portfolio: AG-Braunschweig-Status Cape-Town-Eintrag IDERA Schuldner-Solvenz Flugzeugwert. Skill strukturiert Datenquellen und liefert befuellbares Portfolio-Dashboard-Template.

# Registerpfandrecht – Dashboard bauen

## Mandantenfall

- Bank hat 20 Flugzeuge als Pfandobjekte in Portfolio; Dashboard soll Risiken und Fristen bündeln.
- Risikoabteilung will monatliches Reporting über Pfandrechts-Portfolio; Dashboard als Grundlage.
- M&A-Prozess für Kredit-Portfolio; Dashboard als Due-Diligence-Instrument.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG Cape Town Convention ICAO-Register InsO AG Braunschweig.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG Cape Town Convention ICAO-Register InsO AG Braunschweig – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftFzgG § 1**: Begriffsbestimmung Luftfahrzeugpfandrecht; dingliches Recht nach deutschem Recht.
- **LuftFzgG § 4**: Pfandrechtseintragung beim AG Braunschweig; konstitutive Wirkung.
- **LuftFzgG § 25**: Pfandrechtsvollstreckung; Verwertung durch Versteigerung.
- **ZPO § 864**: Pfändung eingetragener Luftfahrzeuge; besonderer Vollstreckungsweg.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die Rangfolge konkurrierender Pfandrechte (national vs. Cape Town) klar ermittelt?
8. Ist das Pfandrecht bei Weiterveräußerung des Luftfahrzeugs erloschen (LuftFzgG § 27)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Nationaler Pfandrechtsrang ignoriert weil Cape-Town-Priorität falsch eingeschätzt.
- AG Braunschweig-Auszug veraltet; zwischenzeitlich eingetragene Nachrangpfandrechte übersehen.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Registerpfandrecht – Dashboard bauen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfahrzeugpfandrecht und Register ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfahrzeugpfandrecht und Register sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-060-registerpfandrecht-mandantenmemo-schre`

**Fokus:** Anwalt schreibt Mandantenmemo fuer Pfandglaeubiger zu komplexem Pfandrechts-Fall: Rang-Konflikt Insolvenz Cape-Town-Default-Remedies oder Vollstreckungs-Hindernis. Skill strukturiert Memo mit Sachverhalt Rechtslage Handlungsoptionen und Empfehlung.

# Registerpfandrecht – Mandantenmemo schreiben

## Mandantenfall

- Bank-Vorstand braucht Memo nach Insolvenzantrag des Kreditnehmers; Pfandrecht eingetragen; Cape-Town-Eintrag unklar.
- Pfandgläubiger-Konsortium muss über Rang-Streit mit nachrangigem Gläubiger entscheiden.
- Mandant hat Vollstreckungshindernis (Insolvenzsperre); Memo über Alternativen und Cape-Town-Remedies.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG Cape Town Convention InsO ZPO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG Cape Town Convention InsO ZPO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftFzgG § 1**: Begriffsbestimmung Luftfahrzeugpfandrecht; dingliches Recht nach deutschem Recht.
- **LuftFzgG § 4**: Pfandrechtseintragung beim AG Braunschweig; konstitutive Wirkung.
- **LuftFzgG § 25**: Pfandrechtsvollstreckung; Verwertung durch Versteigerung.
- **ZPO § 864**: Pfändung eingetragener Luftfahrzeuge; besonderer Vollstreckungsweg.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist die Rangfolge konkurrierender Pfandrechte (national vs. Cape Town) klar ermittelt?
8. Ist das Pfandrecht bei Weiterveräußerung des Luftfahrzeugs erloschen (LuftFzgG § 27)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Nationaler Pfandrechtsrang ignoriert weil Cape-Town-Priorität falsch eingeschätzt.
- AG Braunschweig-Auszug veraltet; zwischenzeitlich eingetragene Nachrangpfandrechte übersehen.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu Registerpfandrecht – Mandantenmemo schreiben mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfahrzeugpfandrecht und Register ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfahrzeugpfandrecht und Register sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
