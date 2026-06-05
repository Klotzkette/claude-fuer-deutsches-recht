---
name: luft-flughafen-pfaendung-genehmigung
description: "Luft Flughafen Pfaendung Genehmigung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Flughafen Pfaendung Genehmigung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Flughafen Pfaendung Genehmigung** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-034-flughafen-pfaendung-planen` | Glaeubiger will Flughafen-Grundstuecke oder Betriebseinrichtungen pfaenden oder Zwangsverwaltung beantragen. Skill prueft ZVG §§ 146 ff. Grundstückszwangsversteigerung LuftVG-Betriebspflichten und Gemeinwohlvorbehalt und liefert Pfaendungsplan oder Abwehrstrategie. |
| `luft-035-flughafen-genehmigung-pruefen` | Flughafenbetriebsgenehmigung ist unklar: LuftVG § 6 Genehmigung Planfeststellungsbeschluss Betriebserlaubnis Nebenbestimmungen oder Auflagen laeuft aus oder wird angefochten. Skill prueft LuftVG §§ 6-10 Auflagen und liefert Genehmigungsstatus-Vermerk mit Handlungsbedarf. |
| `luft-036-flughafen-sicherheitsauflage-bewerten` | Flughafen erhaelt LuftSiG-Bescheid mit Sicherheitsauflagen oder EASA-Inspektion ergibt Findings. Skill prueft LuftSiG § 8 Sicherheitsprogrammpflichten EU-DVO 2015/1998 Findings-Kategorien Verhaeltnismaessigkeit und Widerspruchsrecht und liefert Auflagen-Bewertungs-Vermerk und Abhilfeplan-Muster. |
| `luft-037-flughafen-insolvenzrisiko-markieren` | Regionaler Flughafen zeigt Insolvenzzeichen: Subventionsstopp sinkende Passagierzahlen Darlehensausfaelle. Skill prueft InsO §§ 15a 17-19 EU-Beihilferecht Daseinsvorsorge-Ausnahme und LuftVG-Betriebspflichten und liefert Risikoampel-Bewertung fuer Kreditgeber oder Minderheitsgesellschafter. |
| `luft-038-flughafen-local-counsel-briefen` | Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Flughafen-Mandat briefen: Planfeststellung Sicherheitsauflage oder Insolvenz. Skill erstellt englisches Briefing-Memo mit deutschem Planfeststellungsrecht LuftSiG LuftVG und konkreten Fragen an Local Counsel. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Flughafen Pfaendung Genehmigung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-034-flughafen-pfaendung-planen`

**Fokus:** Glaeubiger will Flughafen-Grundstuecke oder Betriebseinrichtungen pfaenden oder Zwangsverwaltung beantragen. Skill prueft ZVG §§ 146 ff. Grundstückszwangsversteigerung LuftVG-Betriebspflichten und Gemeinwohlvorbehalt und liefert Pfaendungsplan oder Abwehrstrategie.

# Flughafen – Pfändung planen

## Mandantenfall

- Gläubiger will Zwangsversteigerung des Flughafengrundstücks beantragen nach Zahlungsausfall des Betreibers.
- Flughafenbetreiber erhält Pfändungs- und Überweisungsbeschluss; Mandant will aufschiebende Wirkung.
- Gemeinde fragt ob Flughafen als Daseinsvorsorge-Einrichtung vor Pfändung geschützt ist.

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

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Vermerk zu Flughafen – Pfändung planen mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-035-flughafen-genehmigung-pruefen`

**Fokus:** Flughafenbetriebsgenehmigung ist unklar: LuftVG § 6 Genehmigung Planfeststellungsbeschluss Betriebserlaubnis Nebenbestimmungen oder Auflagen laeuft aus oder wird angefochten. Skill prueft LuftVG §§ 6-10 Auflagen und liefert Genehmigungsstatus-Vermerk mit Handlungsbedarf.

# Flughafen – Genehmigung prüfen

## Mandantenfall

- Flughafenbetreiber fragt welche Genehmigungen für Betrieb und geplante Erweiterung vorliegen müssen.
- Auflagen aus Planfeststellungsbeschluss sollen überprüft werden; einige sind 15 Jahre alt und möglicherweise überholt.
- Betriebsgenehmigung läuft mit Befristung aus; Verlängerungsantrag noch nicht gestellt.

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

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Output

Vermerk zu Flughafen – Genehmigung prüfen mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-036-flughafen-sicherheitsauflage-bewerten`

**Fokus:** Flughafen erhaelt LuftSiG-Bescheid mit Sicherheitsauflagen oder EASA-Inspektion ergibt Findings. Skill prueft LuftSiG § 8 Sicherheitsprogrammpflichten EU-DVO 2015/1998 Findings-Kategorien Verhaeltnismaessigkeit und Widerspruchsrecht und liefert Auflagen-Bewertungs-Vermerk und Abhilfeplan-Muster.

# Flughafen – Sicherheitsauflage bewerten

## Mandantenfall

- Flughafen erhält nach LuftSiG-Inspektion 8 Findings; 2 davon Level 1 mit sofortigem Handlungsbedarf.
- Neue EU-DVO-Anforderung zu Perimeterzäunung tritt in Kraft; Flughafen braucht Umsetzungsplan.
- Flughafen fechtet unverhältnismäßige Auflage zur Videoüberwachung an; Kosten 3 Mio. Euro.

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

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Output

Vermerk zu Flughafen – Sicherheitsauflage bewerten mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-037-flughafen-insolvenzrisiko-markieren`

**Fokus:** Regionaler Flughafen zeigt Insolvenzzeichen: Subventionsstopp sinkende Passagierzahlen Darlehensausfaelle. Skill prueft InsO §§ 15a 17-19 EU-Beihilferecht Daseinsvorsorge-Ausnahme und LuftVG-Betriebspflichten und liefert Risikoampel-Bewertung fuer Kreditgeber oder Minderheitsgesellschafter.

# Flughafen – Insolvenzrisiko markieren

## Mandantenfall

- Regionaler Flughafen hat Subventionen von EU-Kommission zurückzuzahlen; Liquidität kritisch.
- Minderheitsgesellschafter will wissen ob er persönlich haftet wenn Flughafen Insolvenz beantragt.
- Kreditgeber prüft ob Darlehen wertberichtigt werden muss; Insolvenzfrühzeichen sichtbar.

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

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Output

Vermerk zu Flughafen – Insolvenzrisiko markieren mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-038-flughafen-local-counsel-briefen`

**Fokus:** Deutsches Kanzleiteam muss auslaendischen Anwalt fuer Flughafen-Mandat briefen: Planfeststellung Sicherheitsauflage oder Insolvenz. Skill erstellt englisches Briefing-Memo mit deutschem Planfeststellungsrecht LuftSiG LuftVG und konkreten Fragen an Local Counsel.

# Flughafen – Local Counsel briefen

## Mandantenfall

- Deutsche Kanzlei soll Local Counsel in UK briefen wegen Dispute über Flughafenentgelte mit britischer Airline.
- Ausländischer Investor braucht Briefing zu deutschem Flughafen-Planungsrecht vor Beteiligungserwerb.
- Insolvenzverwalter beauftragt Kanzlei in Paris zur Rückholung von Vorauszahlungen; Briefing zu deutschem Insolvenzrecht nötig.

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

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Output

Vermerk zu Flughafen – Local Counsel briefen mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
