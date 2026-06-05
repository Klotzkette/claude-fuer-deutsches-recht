---
name: luft-luftfracht-pfaendung-genehmigung
description: "Luft Luftfracht Pfaendung Genehmigung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Luftfracht Pfaendung Genehmigung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Luftfracht Pfaendung Genehmigung** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-084-luftfracht-pfaendung-planen` | Glaeubiger will Luftfracht oder Luftfrachtansprueche pfaenden. Prueft ZPO § 808 Mobiliarpfaendung HGB Frachtfuehrer-Pfandrecht Montreal Convention Art. 35 Verjaehrung und liefert Pfaendungsplan fuer Luftfracht-Vollstreckung. |
| `luft-085-luftfracht-genehmigung-pruefen` | Luftfrachtfuehrer oder Spediteur fraucht Genehmigung: Luftverkehrsbetreiberzeugnis AOC Gefahrgut-Erlaubnis oder Regulated-Agent-Status. Skill prueft LuftVG EASA Part-OPS IATA DGR EU-VO 300/2008 und liefert Genehmigungsstatus-Vermerk. |
| `luft-086-luftfracht-sicherheitsauflage-bewerten` | Luftfrachtfuehrer oder Spediteur erhaelt LuftSiG oder EU-Luftsicherheits-Auflage. Prueft LuftSiG § 9 Sicherheitsprogramm EU-DVO 2015/1998 EU-VO 300/2008 Findings-Kategorien und liefert Auflagen-Bewertungs-Vermerk und Corrective-Action-Plan. |
| `luft-087-luftfracht-insolvenzrisiko-markieren` | Luftfrachtfuehrer oder grosser Luftfracht-Spediteur zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 Frachtfuehrer-Pfandrecht HGB § 440 Montreal Convention Haftungsgrenzen und liefert Risikoampel fuer Fracht-Glaeubiger. |
| `luft-088-luftfracht-local-counsel-briefen` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Luftfracht-Mandat briefen: Montreal Convention Haftung Gefahrgutvorfall oder Frachtführer-Insolvenz. Skill erstellt englisches Briefing-Memo mit Sachverhalt deutschem Recht und konkreten Fragen. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Luftfracht Pfaendung Genehmigung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-084-luftfracht-pfaendung-planen`

**Fokus:** Glaeubiger will Luftfracht oder Luftfrachtansprueche pfaenden. Prueft ZPO § 808 Mobiliarpfaendung HGB Frachtfuehrer-Pfandrecht Montreal Convention Art. 35 Verjaehrung und liefert Pfaendungsplan fuer Luftfracht-Vollstreckung.

# Luftfracht – Pfändung planen

## Mandantenfall

- Gläubiger will Luftfracht eines Schuldners pfänden die sich noch auf dem Flughafen befindet.
- Frachtführer hält Sendung zurück wegen ausstehender Frachtzahlung; Absender will Herausgabe erzwingen.
- Insolvenz des Absenders: Insolvenzverwalter will Fracht für Masse sichern; Frachtführer hat Pfandrecht.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: ZPO § 808 HGB § 440 Montreal Convention Art. 9 35 InsO §§ 47 89.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

ZPO § 808 HGB § 440 Montreal Convention Art. 9 35 InsO §§ 47 89 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **Montrealer Übereinkommen Art. 18**: Haftung des Luftfrachtführers für Beschädigung; Haftungsausschlüsse.
- **LuftVG § 44**: Nationale Verweisung auf Montrealer Übereinkommen für innerdeutsche Flüge.
- **EU-VO 300/2008 und DVO 2015/1998**: Sicherheitsanforderungen für Luftfracht; ACC3 und RA/KC-Status.
- **HGB § 475**: Frachtführerhaftung subsidiär; nur soweit MÜ keine Regelung trifft.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Haftungsgrenze (22 SZR/kg) eingehalten oder Werterklärung im AWB vermerkt?
8. Ist die Frachtkette lückenlos dokumentiert (AWB Sicherheitsdeklaration Manifest)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Haftungsregime Montrealer Übereinkommen mit HGB-Recht vermischt; falsche Haftungssumme.
- AWB fehlt oder unvollständig; Beweislastumkehr zulasten des Frachtführers.

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Strukturierter Vermerk zu Luftfracht – Pfändung planen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-085-luftfracht-genehmigung-pruefen`

**Fokus:** Luftfrachtfuehrer oder Spediteur fraucht Genehmigung: Luftverkehrsbetreiberzeugnis AOC Gefahrgut-Erlaubnis oder Regulated-Agent-Status. Skill prueft LuftVG EASA Part-OPS IATA DGR EU-VO 300/2008 und liefert Genehmigungsstatus-Vermerk.

# Luftfracht – Genehmigung prüfen

## Mandantenfall

- Luftfrachtführer fragt welche Genehmigungen er für den Start eines Frachtbetriebs benötigt.
- Spediteur will Regulated-Agent-Status erlangen; Prüfung der Anforderungen nach EU-VO 300/2008.
- Bestehende Frachtgenehmigung wird auf Weitergelten für neue Strecken geprüft.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftVG EASA Part-OPS EU-VO 300/2008 EU-VO 965/2012 IATA DGR.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftVG EASA Part-OPS EU-VO 300/2008 EU-VO 965/2012 IATA DGR – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **Montrealer Übereinkommen Art. 18**: Haftung des Luftfrachtführers für Beschädigung; Haftungsausschlüsse.
- **LuftVG § 44**: Nationale Verweisung auf Montrealer Übereinkommen für innerdeutsche Flüge.
- **HGB § 475**: Frachtführerhaftung subsidiär; nur soweit MÜ keine Regelung trifft.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Haftungsgrenze (22 SZR/kg) eingehalten oder Werterklärung im AWB vermerkt?
8. Ist die Frachtkette lückenlos dokumentiert (AWB Sicherheitsdeklaration Manifest)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Haftungsregime Montrealer Übereinkommen mit HGB-Recht vermischt; falsche Haftungssumme.
- AWB fehlt oder unvollständig; Beweislastumkehr zulasten des Frachtführers.

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Output

Strukturierter Vermerk zu Luftfracht – Genehmigung prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-086-luftfracht-sicherheitsauflage-bewerten`

**Fokus:** Luftfrachtfuehrer oder Spediteur erhaelt LuftSiG oder EU-Luftsicherheits-Auflage. Prueft LuftSiG § 9 Sicherheitsprogramm EU-DVO 2015/1998 EU-VO 300/2008 Findings-Kategorien und liefert Auflagen-Bewertungs-Vermerk und Corrective-Action-Plan.

# Luftfracht – Sicherheitsauflage bewerten

## Mandantenfall

- Luftfrachtführer erhält nach Sicherheitskontrolle Finding zu unzureichenden Gefahrgut-Screening-Verfahren.
- Spediteur verliert Regulated-Agent-Status nach negativer Behördenprüfung; Geschäft gefährdet.
- EU-DVO verschärft Anforderungen für Luftfrachtkontrollen; Umsetzungskosten erheblich.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftSiG § 9 EU-DVO 2015/1998 EU-VO 300/2008 IATA DGR.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftSiG § 9 EU-DVO 2015/1998 EU-VO 300/2008 IATA DGR – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **Montrealer Übereinkommen Art. 18**: Haftung des Luftfrachtführers für Beschädigung; Haftungsausschlüsse.
- **LuftVG § 44**: Nationale Verweisung auf Montrealer Übereinkommen für innerdeutsche Flüge.
- **HGB § 475**: Frachtführerhaftung subsidiär; nur soweit MÜ keine Regelung trifft.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Haftungsgrenze (22 SZR/kg) eingehalten oder Werterklärung im AWB vermerkt?
8. Ist die Frachtkette lückenlos dokumentiert (AWB Sicherheitsdeklaration Manifest)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Haftungsregime Montrealer Übereinkommen mit HGB-Recht vermischt; falsche Haftungssumme.
- AWB fehlt oder unvollständig; Beweislastumkehr zulasten des Frachtführers.

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Output

Strukturierter Vermerk zu Luftfracht – Sicherheitsauflage bewerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-087-luftfracht-insolvenzrisiko-markieren`

**Fokus:** Luftfrachtfuehrer oder grosser Luftfracht-Spediteur zeigt Insolvenzzeichen. Prueft InsO §§ 15a 17-19 Frachtfuehrer-Pfandrecht HGB § 440 Montreal Convention Haftungsgrenzen und liefert Risikoampel fuer Fracht-Glaeubiger.

# Luftfracht – Insolvenzrisiko markieren

## Mandantenfall

- Luftfrachtführer zahlt Lieferanten nicht; Fracht sitzt noch im Lager; Eigentümer will zurückholen.
- Großspediteur hat Cash-Probleme; Auftraggeber fragt ob Vorauszahlungen gefährdet sind.
- Frachtführer stellt Insolvenzantrag; Empfänger will Fracht trotzdem erhalten.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: InsO §§ 15a 17-19 47 HGB § 440 Montreal Convention Art. 18 35.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

InsO §§ 15a 17-19 47 HGB § 440 Montreal Convention Art. 18 35 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **Montrealer Übereinkommen Art. 18**: Haftung des Luftfrachtführers für Beschädigung; Haftungsausschlüsse.
- **LuftVG § 44**: Nationale Verweisung auf Montrealer Übereinkommen für innerdeutsche Flüge.
- **EU-VO 300/2008 und DVO 2015/1998**: Sicherheitsanforderungen für Luftfracht; ACC3 und RA/KC-Status.
- **HGB § 475**: Frachtführerhaftung subsidiär; nur soweit MÜ keine Regelung trifft.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Haftungsgrenze (22 SZR/kg) eingehalten oder Werterklärung im AWB vermerkt?
8. Ist die Frachtkette lückenlos dokumentiert (AWB Sicherheitsdeklaration Manifest)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Haftungsregime Montrealer Übereinkommen mit HGB-Recht vermischt; falsche Haftungssumme.
- AWB fehlt oder unvollständig; Beweislastumkehr zulasten des Frachtführers.

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Output

Strukturierter Vermerk zu Luftfracht – Insolvenzrisiko markieren mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-088-luftfracht-local-counsel-briefen`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Luftfracht-Mandat briefen: Montreal Convention Haftung Gefahrgutvorfall oder Frachtführer-Insolvenz. Skill erstellt englisches Briefing-Memo mit Sachverhalt deutschem Recht und konkreten Fragen.

# Luftfracht – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll in USA Local Counsel briefen für Haftungsklage nach Frachtschaden bei US-Airline.
- Absender in Singapur fragt nach deutschem Recht für Gefahrgutvorfall bei deutschem Frachtführer.
- Insolvenzverwalter beauftragt Kanzlei in Dubai zur Rückholung von Fracht aus UAE-Lager.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: Montreal Convention LuftVG HGB § 440 IATA DGR InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

Montreal Convention LuftVG HGB § 440 IATA DGR InsO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **Montrealer Übereinkommen Art. 18**: Haftung des Luftfrachtführers für Beschädigung; Haftungsausschlüsse.
- **LuftVG § 44**: Nationale Verweisung auf Montrealer Übereinkommen für innerdeutsche Flüge.
- **EU-VO 300/2008 und DVO 2015/1998**: Sicherheitsanforderungen für Luftfracht; ACC3 und RA/KC-Status.
- **HGB § 475**: Frachtführerhaftung subsidiär; nur soweit MÜ keine Regelung trifft.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Haftungsgrenze (22 SZR/kg) eingehalten oder Werterklärung im AWB vermerkt?
8. Ist die Frachtkette lückenlos dokumentiert (AWB Sicherheitsdeklaration Manifest)?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Haftungsregime Montrealer Übereinkommen mit HGB-Recht vermischt; falsche Haftungssumme.
- AWB fehlt oder unvollständig; Beweislastumkehr zulasten des Frachtführers.

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Output

Strukturierter Vermerk zu Luftfracht – Local Counsel briefen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
