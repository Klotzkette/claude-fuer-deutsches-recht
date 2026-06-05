---
name: luft-luftfracht-dashboard-mandantenmemo
description: "Luft Luftfracht Dashboard Mandantenmemo: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Luftfracht Dashboard Mandantenmemo

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Luftfracht Dashboard Mandantenmemo** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-089-luftfracht-dashboard-bauen` | Luftfrachtfuehrer oder grosser Spediteur braucht Dashboard fuer Fracht-Compliance: Regulated-Agent-Status Gefahrgut-Zulassungen Sicherheitsfindings Versicherung. Skill strukturiert Datenquellen und liefert befuellbares Compliance-Dashboard. |
| `luft-090-luftfracht-mandantenmemo-schreiben` | Anwalt schreibt Mandantenmemo fuer Luftfrachtfuehrer oder Spediteur zu Haftungsfall Gefahrgutvorfall Sicherheitsauflage oder Insolvenznaehe. Skill strukturiert Memo mit Sachverhalt Montreal Convention Rechtslage Handlungsoptionen und Empfehlung. |
| `luft-092-acc3-register-auswerten` | Mandant will ACC3-Designierungsstatus und Validierungsstand eines Carriers auswerten. Prueft EU-DVO 2015/1998 EU-Datenbank fuer ACC3-designierte Carrier RA3/KC3-Status und Validierungsgueltigkeit und liefert Compliance-Status-Bericht. |
| `luft-093-acc3-pfandrecht-vorbereiten` | ACC3-Carrier will Flugzeuge fuer Drittland-Frachtbetrieb finanzieren; Pfandrecht und Cape-Town-Eintrag nötig. Prueft Cape-Town-Convention LuftFzgG EU-VO 300/2008 Betriebsvoraussetzungen und liefert kombinierte Sicherungs- und Compliance-Strategie. |
| `luft-094-acc3-pfaendung-planen` | Glaeubiger will Frachtflugzeuge eines ACC3-Carriers pfaenden. Prueft ZPO §§ 864-871 LuftFzgG Cape-Town-Remedies und EU-Luftsicherheitsstatus bei Vollstreckung und liefert Pfaendungsplan fuer ACC3-Frachtflotte. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Luftfracht Dashboard Mandantenmemo**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-089-luftfracht-dashboard-bauen`

**Fokus:** Luftfrachtfuehrer oder grosser Spediteur braucht Dashboard fuer Fracht-Compliance: Regulated-Agent-Status Gefahrgut-Zulassungen Sicherheitsfindings Versicherung. Skill strukturiert Datenquellen und liefert befuellbares Compliance-Dashboard.

# Luftfracht – Dashboard bauen

## Mandantenfall

- Frachtführer hat Betrieb an 5 Flughäfen; Dashboard soll Genehmigungen und Sicherheitsstatus bündeln.
- Regulierungsbehörde verlangt laufendes Compliance-Reporting; Dashboard als Grundlage.
- Investor prüft Frachtunternehmen; Dashboard für Due Diligence.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 IATA DGR LuftVG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

EU-DVO 2015/1998 EU-VO 300/2008 LuftSiG § 9 IATA DGR LuftVG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Strukturierter Vermerk zu Luftfracht – Dashboard bauen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-090-luftfracht-mandantenmemo-schreiben`

**Fokus:** Anwalt schreibt Mandantenmemo fuer Luftfrachtfuehrer oder Spediteur zu Haftungsfall Gefahrgutvorfall Sicherheitsauflage oder Insolvenznaehe. Skill strukturiert Memo mit Sachverhalt Montreal Convention Rechtslage Handlungsoptionen und Empfehlung.

# Luftfracht – Mandantenmemo schreiben

## Mandantenfall

- Frachtführer nach Gefahrgutvorfall: Memo über Haftungslage Montreal Convention Bußgeldrisiken.
- Spediteur verliert Regulated-Agent-Status; Memo über Rechtsmittel und Betriebsunterbrechungsfolgen.
- Frachtführer erhält LuftSiG-Auflage; Memo über Handlungsoptionen und Fristen.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: Montreal Convention LuftVG LuftSiG § 9 HGB § 440 InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

Montreal Convention LuftVG LuftSiG § 9 HGB § 440 InsO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Output

Strukturierter Vermerk zu Luftfracht – Mandantenmemo schreiben mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Montrealer Übereinkommen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A22001A0718%2801%29
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-092-acc3-register-auswerten`

**Fokus:** Mandant will ACC3-Designierungsstatus und Validierungsstand eines Carriers auswerten. Prueft EU-DVO 2015/1998 EU-Datenbank fuer ACC3-designierte Carrier RA3/KC3-Status und Validierungsgueltigkeit und liefert Compliance-Status-Bericht.

# ACC3 – Register auswerten

## Mandantenfall

- Airline will prüfen ob sie noch korrekt als ACC3 in EU-Datenbank eingetragen ist und ob Validierung noch gültig ist.
- Behörde prüft ob Absender aus Drittland über validierten RA3-Status verfügt bevor Fracht angenommen wird.
- Insolvenzverwalter braucht Übersicht über alle Designierungen und Validierungen eines Carriers.

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

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Strukturierter Vermerk zu ACC3 – Register auswerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-093-acc3-pfandrecht-vorbereiten`

**Fokus:** ACC3-Carrier will Flugzeuge fuer Drittland-Frachtbetrieb finanzieren; Pfandrecht und Cape-Town-Eintrag nötig. Prueft Cape-Town-Convention LuftFzgG EU-VO 300/2008 Betriebsvoraussetzungen und liefert kombinierte Sicherungs- und Compliance-Strategie.

# ACC3 – Pfandrecht vorbereiten

## Mandantenfall

- Frachtflugzeug-Finanzierung für ACC3-Betrieb: Bank will Pfandrecht und Cape-Town-Eintrag koordinieren.
- ACC3-Carrier will Frachtflotte erweitern; Finanzier verlangt Sicherheiten und Nachweis der ACC3-Designierung.
- Refinanzierung der ACC3-Frachtflotte erfordert Neustrukturierung der Sicherheiten.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: Cape Town Convention LuftFzgG EU-DVO 2015/1998 EU-VO 300/2008.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

Cape Town Convention LuftFzgG EU-DVO 2015/1998 EU-VO 300/2008 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Strukturierter Vermerk zu ACC3 – Pfandrecht vorbereiten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-094-acc3-pfaendung-planen`

**Fokus:** Glaeubiger will Frachtflugzeuge eines ACC3-Carriers pfaenden. Prueft ZPO §§ 864-871 LuftFzgG Cape-Town-Remedies und EU-Luftsicherheitsstatus bei Vollstreckung und liefert Pfaendungsplan fuer ACC3-Frachtflotte.

# ACC3 – Pfändung planen

## Mandantenfall

- Pfandgläubiger will aus eingetragenem Pfandrecht an Frachtflugzeug des ACC3-Carriers vollstrecken.
- Insolvenz eines ACC3-Carriers: Pfandgläubiger will Absonderungsrecht geltend machen.
- Cape-Town-Gläubiger betreibt IDERA-Entregistrierung; ACC3-Betrieb gefährdet.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: ZPO §§ 864-871 LuftFzgG Cape Town Convention Art. 8-10 InsO § 89 EU-DVO 2015/1998.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

ZPO §§ 864-871 LuftFzgG Cape Town Convention Art. 8-10 InsO § 89 EU-DVO 2015/1998 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Strukturierter Vermerk zu ACC3 – Pfändung planen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. ACC3-Compliance-Matrix. Validierungskalender mit Ablaufdaten.
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

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich ACC3-Zulassung und Sicherheitsvalidierung Luftfracht Drittstaaten sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
