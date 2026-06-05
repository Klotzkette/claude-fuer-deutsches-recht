---
name: luft-lba-airline-flughafen-flugzeugleasing
description: "Luft LBA Airline Flughafen Flugzeugleasing: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft LBA Airline Flughafen Flugzeugleasing

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft LBA Airline Flughafen Flugzeugleasing** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-003-lba-zustaendigkeit-pruefen` | Mandant erhaelt LBA-Bescheid oder fragt ob LBA oder Landesbehoerde zustaendig ist. Prueft §§ 29 31 LuftVG Zustaendigkeitsabgrenzung LBA vs. Landesluftfahrtbehoerde EU-VO 1008/2008 Art. 4 Aufsichtsstaat und liefert Zustaendigkeitsvermerk mit richtigem Adressaten fuer Widerspruch oder Klage. |
| `luft-021-airline-zustaendigkeit-pruefen` | Airline-Mandat: unklar welche Behoerde zustaendig ist LBA EU-Behoerde Landesbehoerde oder auslaendische Luftfahrtbehoerde. Prueft EU-VO 1008/2008 Art. 4 Aufsichtsstaat LuftVG §§ 29-31 EASA und bilaterale Abkommen und liefert Zustaendigkeits-Vermerk mit korrektem Antragsadressaten. |
| `luft-031-flughafen-zustaendigkeit-pruefen` | Flughafen-Mandat: unklar ob Landesluftfahrtbehoerde LBA oder Planfeststellungsbehoerde zustaendig. Prueft LuftVG §§ 6 8 29 Behoerdenabgrenzung Planfeststellungspflicht Landesrecht und liefert Zustaendigkeits-Vermerk fuer Flughafen-Bescheid oder Planfeststellungsverfahren. |
| `luft-041-flugzeugleasing-zustaendigkeit-pruefen` | Flugzeugleasing-Mandat: unklar welche Behoerde zustaendig ist LBA EASA Cape-Town-Registry oder auslaendische Luftfahrtbehoerde. Prueft EU-VO 1008/2008 Art. 13 LuftVG § 21a Cape-Town-Registrierung und liefert Zustaendigkeits-Vermerk fuer Wet-Dry-Finance-Lease-Situationen. |
| `luft-051-registerpfandrecht-zustaendigkeit-prue` | Pfandrecht an Luftfahrzeugen: Zustaendigkeit AG Braunschweig vs. ICAO-Register vs. Cape-Town-Registry. Prueft LuftFzgG § 1 AG-Braunschweig-Registerzustaendigkeit Cape-Town-Convention Art. 16 und Kollisionsrecht und liefert Zustaendigkeits-Vermerk fuer nationales und internationales Pfandrecht. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft LBA Airline Flughafen Flugzeugleasing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-003-lba-zustaendigkeit-pruefen`

**Fokus:** Mandant erhaelt LBA-Bescheid oder fragt ob LBA oder Landesbehoerde zustaendig ist. Prueft §§ 29 31 LuftVG Zustaendigkeitsabgrenzung LBA vs. Landesluftfahrtbehoerde EU-VO 1008/2008 Art. 4 Aufsichtsstaat und liefert Zustaendigkeitsvermerk mit richtigem Adressaten fuer Widerspruch oder Klage.

# LBA-Zuständigkeit prüfen – Behörde korrekt adressieren

## Mandantenfall

- Airline erhält Widerrufsbescheid der Betriebsgenehmigung vom LBA; Mandant fragt ob Widerspruch ans LBA oder an ein Landesministerium zu richten ist.
- Kleines Charterunternehmen möchte AOC beantragen und ist unsicher ob LBA oder Landesluftfahrtbehörde Sachsen-Anhalt zuständig ist.
- Halter eines Ultraleichtflugzeugs streitet über Eintrag in Luftsportgeräteverzeichnis; Behörde hat falsche Stelle angeschrieben.

## Erste Schritte

1. Bescheidaussteller identifizieren: LBA oder Landesluftfahrtbehörde.
2. Sachgebiets-Mapping nach LuftVG §§ 29-31: LBA für Betriebsgenehmigung Luftfahrzeugrolle AOC-Kern Musterzulassung; Länder für Flugplätze Lizenzen Luftsportgeräte.
3. EU-Recht-Ebene prüfen: EASA für Musterzulassung Pilotenlizenz.
4. Aufsichtsstaat nach EU-VO 1008/2008 Art. 4 bestimmen: Hauptgeschäftssitz entscheidet.
5. Rechtsschutzbehelf bestimmen: Widerspruch an erlassende Behörde (§ 68 VwGO) dann Klage beim zuständigen VG.
6. Zuständigkeitsvermerk mit Begründung und Adressat des Widerspruchs erstellen.

## Rechtsrahmen

- **LuftVG § 29 Abs. 1**: Aufsicht über Luftfahrt durch LBA und Landesluftfahrtbehörden.
- **LuftVG § 31**: Bundesbehörden-Aufgaben des LBA; abschließende Aufzählung.
- **LuftVZO § 14**: Eintragung von Flugzeugen in Luftfahrzeugrolle durch LBA.
- **EU-VO 1008/2008 Art. 4**: Aufsicht durch Mitgliedstaat des Hauptgeschäftssitzes.
- **LuftVG § 20**: Betriebsgenehmigung durch LBA für gewerblichen Linienverkehr.
- **VwGO § 68**: Widerspruchspflicht; Widerspruch an erlassende Behörde.
## Prüfraster

1. Hat LBA oder Landesbehörde den Bescheid erlassen?
2. Welchem Sachgebiet ist der Streit zuzuordnen?
3. Ist EASA-Recht vorrangig und schließt nationale Behördenzuständigkeit aus?
4. Gilt der EU-Aufsichtsstaat-Grundsatz (Hauptgeschäftssitz)?
5. Ist Widerspruchsbehörde identisch mit Ausgangsbehörde?
6. Ist einstweiliger Rechtsschutz wegen Sofortvollziehbarkeit nötig?

## Typische Fallstricke

- Widerspruch an falsche Behörde; führt zu Fristablauf ohne Hemmung.
- EASA-Zuständigkeit mit LBA-Zuständigkeit verwechselt.
- Aufsichtsstaat-Prinzip ignoriert: Airline mit Hauptsitz in Irland muss bei IAA klagen.
- Widerspruchserfordernis übersehen bei Bescheiden mit Sofortvollzug.


## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Zuständigkeitsvermerk mit Rechtsgrundlage korrekter Behörde und Widerspruchsadressat. Fristberechnung Widerspruch/Klage.

## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftVZO: https://www.gesetze-im-internet.de/luftvzo/
- LBA Aufgaben: https://www.lba.de/DE/Aufgaben/aufgaben_node.html
- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-021-airline-zustaendigkeit-pruefen`

**Fokus:** Airline-Mandat: unklar welche Behoerde zustaendig ist LBA EU-Behoerde Landesbehoerde oder auslaendische Luftfahrtbehoerde. Prueft EU-VO 1008/2008 Art. 4 Aufsichtsstaat LuftVG §§ 29-31 EASA und bilaterale Abkommen und liefert Zustaendigkeits-Vermerk mit korrektem Antragsadressaten.

# Airline – Zuständigkeit prüfen

## Mandantenfall

- Airline mit Hauptsitz Hamburg betreibt Verbindung nach Wien; österreichische Behörde beanstandet; Mandant fragt welche Behörde zuständig ist.
- Tochtergesellschaft eines US-Konzerns registriert in Deutschland; Frage ob LBA oder FAA für AOC zuständig.
- Airline möchte Strecke nach Nordafrika eröffnen; Bilateralabkommen Deutschland-Marokko unbekannt.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Vermerk zu Airline – Zuständigkeit prüfen mit Ampel-Rating Fristenstand und nächsten Schritten. Checkliste offener Punkte. Zuständigkeitsmatrix Behörde/Register. Fristenkalender mit Ampelstatus.
## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-031-flughafen-zustaendigkeit-pruefen`

**Fokus:** Flughafen-Mandat: unklar ob Landesluftfahrtbehoerde LBA oder Planfeststellungsbehoerde zustaendig. Prueft LuftVG §§ 6 8 29 Behoerdenabgrenzung Planfeststellungspflicht Landesrecht und liefert Zustaendigkeits-Vermerk fuer Flughafen-Bescheid oder Planfeststellungsverfahren.

# Flughafen – Zuständigkeit prüfen

## Mandantenfall

- Flughafenbetreiber erhält Bescheid zu baulicher Änderung eines Terminals; unklar ob Planfeststellungsbehörde oder LBA zuständig.
- Gemeinde will gegen Erweiterungsbeschluss vorgehen; Frage welches Gericht zuständig ist.
- Flugplatzbetreiber fragt ob für Erweiterung Sicherheitsbereichs eine neue Genehmigung nötig ist.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Vermerk zu Flughafen – Zuständigkeit prüfen mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-041-flugzeugleasing-zustaendigkeit-pruefen`

**Fokus:** Flugzeugleasing-Mandat: unklar welche Behoerde zustaendig ist LBA EASA Cape-Town-Registry oder auslaendische Luftfahrtbehoerde. Prueft EU-VO 1008/2008 Art. 13 LuftVG § 21a Cape-Town-Registrierung und liefert Zustaendigkeits-Vermerk fuer Wet-Dry-Finance-Lease-Situationen.

# Flugzeugleasing – Zuständigkeit prüfen

## Mandantenfall

- Leasinggeber in Irland gibt Flugzeug an deutsche Airline; unklar ob LBA oder IAA für AOC zuständig.
- Wet-Lease-Arrangement mit ausländischer Crew in Deutschland; EASA-Sondergenehmigung unklar.
- Finance-Lease läuft aus; Kaufoption ausgeübt; Eigentümer-Umschreibung in Luftfahrzeugrolle nötig.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-VO 1008/2008 Art. 13 LuftVG § 21a Cape Town Convention EASA Part-OPS.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen). Wet-Lease-Genehmigung gesondert prüfen: EU-VO 1008/2008 Art. 13 für EU-interne Wet-Leases.
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-VO 1008/2008 Art. 13 LuftVG § 21a Cape Town Convention EASA Part-OPS – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **Cape Town Aircraft Protocol Art. XII**: Prioritäten konkurrierender Sicherungsrechte im internationalen Register.
- **LuftFzgG § 3**: Entstehung des Pfandrechts; Eintragungszeitpunkt als Prioritätsregel.
- **InsO § 47**: Aussonderungsrecht des Leasinggebers; Priorität gegenüber Insolvenzgläubigern.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist eine IDERA (Irrevocable Deregistration and Export Request Authorisation) im Cape-Town-Register eingetragen?
8. Hat Leasinggeber wirksam nach InsO § 47 Aussonderung geltend gemacht?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- IDERA nicht im Cape-Town-Register eingetragen; Deregistrierung im Streitfall verzögert.
- Leasingvertrag nach englischem Recht; deutsches Insolvenzgericht weicht Aussonderungsanspruch ab.

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Zuständigkeits-Vermerk mit Behördentabelle. Antragsadressat je Teilfrage. Cape-Town-Registrierungs-Checkliste. Aussonderungsvermerk bei Insolvenz.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- ICAO International Registry: https://www.internationalregistry.aero

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flugzeug-Leasing und Cape Town Convention ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Flugzeug-Leasing und Cape Town Convention sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-051-registerpfandrecht-zustaendigkeit-prue`

**Fokus:** Pfandrecht an Luftfahrzeugen: Zustaendigkeit AG Braunschweig vs. ICAO-Register vs. Cape-Town-Registry. Prueft LuftFzgG § 1 AG-Braunschweig-Registerzustaendigkeit Cape-Town-Convention Art. 16 und Kollisionsrecht und liefert Zustaendigkeits-Vermerk fuer nationales und internationales Pfandrecht.

# Registerpfandrecht – Zuständigkeit prüfen

## Mandantenfall

- Gläubiger fragt ob Pfandrecht im AG Braunschweig oder im ICAO Cape-Town-Register einzutragen ist oder in beiden.
- Ausländisches Gericht fragt nach Anerkennung des deutschen Luftfahrzeugpfandrechts.
- Insolvenzverwalter prüft Rang von Pfandrechten aus verschiedenen Registern.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG §§ 1-12 Cape Town Convention Art. 16 29 ZPO InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG §§ 1-12 Cape Town Convention Art. 16 29 ZPO InsO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Strukturierter Vermerk zu Registerpfandrecht – Zuständigkeit prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfahrzeugpfandrecht und Register ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Luftfahrzeugpfandrecht und Register sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
