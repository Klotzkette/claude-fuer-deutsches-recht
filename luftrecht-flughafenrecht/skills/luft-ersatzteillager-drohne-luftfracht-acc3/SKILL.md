---
name: luft-ersatzteillager-drohne-luftfracht-acc3
description: "Luft Ersatzteillager Drohne Luftfracht Acc3: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Ersatzteillager Drohne Luftfracht Acc3

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Ersatzteillager Drohne Luftfracht Acc3** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-061-ersatzteillager-zustaendigkeit-pruefen` | Ersatzteillager fuer Luftfahrzeuge: unklar welche Behoerde zustaendig ist LBA EASA Zollbehoerde oder Gefahrgut-Aufsicht. Prueft LuftVG EASA Part-145 Approved Maintenance Organisation Zollrecht und Gefahrgutrecht und liefert Zustaendigkeits-Vermerk fuer Lager-Genehmigung. |
| `luft-071-drohne-zustaendigkeit-pruefen` | Drohnen-Mandat: unklar ob LBA EASA Landesbehoerde oder Luftraum-Nutzer-Behoerde zustaendig. Prueft EU-VO 2019/947 Betriebskategorien LuftVG § 21a und U-Space-Regulierung und liefert Zustaendigkeits-Vermerk fuer Drohnen-Genehmigung oder Streit. |
| `luft-081-luftfracht-zustaendigkeit-pruefen` | Luftfracht-Mandat: unklar welche Behoerde zustaendig ist LBA EASA Zollbehoerde oder Luftsicherheitsbehoerde. Prueft LuftVG Montreal Convention Art. 18 IATA-Frachtregeln Zollrecht und liefert Zustaendigkeits-Vermerk fuer Luftfracht-Streit oder Genehmigungsverfahren. |
| `luft-091-acc3-zustaendigkeit-pruefen` | ACC3-Mandat: Luftfrachttraeger der Fracht aus Drittlaendern in EU bringt muss Designierung und Validierung nachweisen. Prueft EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 und EU-Validierungs-Verfahren und liefert Zustaendigkeits-Vermerk fuer ACC3-Designierungsverfahren. |
| `luft-101-slot-zustaendigkeit-pruefen` | Slot-Mandat: unklar ob Fluko LBA oder Verwaltungsgericht zustaendig ist fuer Slot-Zuweisung Widerspruch oder Klage. Prueft LuftVG §§ 27a-27d FHKV VO EWG 95/93 und Verwaltungsrechtsweg und liefert Zustaendigkeits-Vermerk fuer Slot-Rechtsstreit. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Ersatzteillager Drohne Luftfracht Acc3**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-061-ersatzteillager-zustaendigkeit-pruefen`

**Fokus:** Ersatzteillager fuer Luftfahrzeuge: unklar welche Behoerde zustaendig ist LBA EASA Zollbehoerde oder Gefahrgut-Aufsicht. Prueft LuftVG EASA Part-145 Approved Maintenance Organisation Zollrecht und Gefahrgutrecht und liefert Zustaendigkeits-Vermerk fuer Lager-Genehmigung.

# Ersatzteillager – Zuständigkeit prüfen

## Mandantenfall

- MRO-Betrieb fragt welche Behörde für Genehmigung des Ersatzteillagers zuständig ist: LBA EASA oder Landesbehörde.
- Flughafen-Dienstleister lagert Flugzeugteile; Zoll fragt nach Zulassung als Luftfahrtteilehersteller.
- Airline lagert EASA-zertifizierte Teile; unklarer Genehmigungsstatus nach Reorganisation.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EASA Part-145 LuftVG § 29 Zollrecht Gefahrgutrecht IATA DGR.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EASA Part-145 LuftVG § 29 Zollrecht Gefahrgutrecht IATA DGR – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Strukturierter Vermerk zu Ersatzteillager – Zuständigkeit prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Part-145-Compliance-Checkliste für Lager. Dokumentationsnachweis-Schema.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA Part-145: https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-ec-no-20422003
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Ersatzteillager für Luftfahrzeuge und Part-145-Zulassung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-071-drohne-zustaendigkeit-pruefen`

**Fokus:** Drohnen-Mandat: unklar ob LBA EASA Landesbehoerde oder Luftraum-Nutzer-Behoerde zustaendig. Prueft EU-VO 2019/947 Betriebskategorien LuftVG § 21a und U-Space-Regulierung und liefert Zustaendigkeits-Vermerk fuer Drohnen-Genehmigung oder Streit.

# Drohne – Zuständigkeit prüfen

## Mandantenfall

- Drohnenbetreiber hat Bescheid der Luftsicherheitsbehörde erhalten; unklar ob LBA oder Landesbehörde zuständig ist.
- Behörde hat gewerblichen Drohnenbetrieb ohne Genehmigung beanstandet; Mandant fragt welches Recht gilt.
- Drohnenunfall über Nationalpark; unklar welche Behörde Unfalluntersuchung führt.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-VO 2019/947 LuftVG § 21a EASA BNatSchG LuftSiG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-VO 2019/947 LuftVG § 21a EASA BNatSchG LuftSiG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Strukturierter Vermerk zu Drohne – Zuständigkeit prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
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

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-081-luftfracht-zustaendigkeit-pruefen`

**Fokus:** Luftfracht-Mandat: unklar welche Behoerde zustaendig ist LBA EASA Zollbehoerde oder Luftsicherheitsbehoerde. Prueft LuftVG Montreal Convention Art. 18 IATA-Frachtregeln Zollrecht und liefert Zustaendigkeits-Vermerk fuer Luftfracht-Streit oder Genehmigungsverfahren.

# Luftfracht – Zuständigkeit prüfen

## Mandantenfall

- Luftfrachtführer erhält Bescheid der Luftsicherheitsbehörde wegen unzureichender Gefahrgut-Kontrollen; Frage welche Behörde zuständig ist.
- Frachtführer hat Luftfrachtbrief-Streit mit Versender; Frage ob deutsches Gericht oder Schiedsgericht zuständig.
- Zollbehörde hat Fracht festgehalten; unklar ob LBA oder Zoll Federführung hat.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: Montreal Convention Art. 18 LuftVG LuftSiG EU-VO 300/2008 IATA-Frachtregeln Zollrecht.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

Montreal Convention Art. 18 LuftVG LuftSiG EU-VO 300/2008 IATA-Frachtregeln Zollrecht – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Strukturierter Vermerk zu Luftfracht – Zuständigkeit prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-091-acc3-zustaendigkeit-pruefen`

**Fokus:** ACC3-Mandat: Luftfrachttraeger der Fracht aus Drittlaendern in EU bringt muss Designierung und Validierung nachweisen. Prueft EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 und EU-Validierungs-Verfahren und liefert Zustaendigkeits-Vermerk fuer ACC3-Designierungsverfahren.

# ACC3 – Zuständigkeit prüfen

## Mandantenfall

- Fluggesellschaft aus Nahost will Fracht aus Drittland-Flughafen in EU bringen; fragt welche Behörde für ACC3-Designierung zuständig ist.
- Validierungsfirma will ACC3-Validierungen durchführen; fragt nach EU-Zulassungsvoraussetzungen.
- ACC3 hat Designierung verloren; fragt welche Behörde Widerspruch annimmt.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Strukturierter Vermerk zu ACC3 – Zuständigkeit prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-101-slot-zustaendigkeit-pruefen`

**Fokus:** Slot-Mandat: unklar ob Fluko LBA oder Verwaltungsgericht zustaendig ist fuer Slot-Zuweisung Widerspruch oder Klage. Prueft LuftVG §§ 27a-27d FHKV VO EWG 95/93 und Verwaltungsrechtsweg und liefert Zustaendigkeits-Vermerk fuer Slot-Rechtsstreit.

# Slot – Zuständigkeit prüfen

## Mandantenfall

- Airline erhält von Fluko negative Slot-Entscheidung; fragt ob Widerspruch an Fluko oder LBA zu richten ist.
- Airline will Klage gegen Slot-Zuweisung erheben; fragt welches VG zuständig ist.
- Flughafen und Airline streiten über Kapazitätsfeststellung; Zuständigkeit LBA vs. Fluko unklar.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftVG §§ 27a-27d FHKV VO EWG 95/93 VwGO § 40.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftVG §§ 27a-27d FHKV VO EWG 95/93 VwGO § 40 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Strukturierter Vermerk zu Slot – Zuständigkeit prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Slot-Portfolio-Analyse mit Nutzungsnachweis. Koordinatoren-Schreiben-Template.
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

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Slot-Koordination und Flughafenkapazität sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
