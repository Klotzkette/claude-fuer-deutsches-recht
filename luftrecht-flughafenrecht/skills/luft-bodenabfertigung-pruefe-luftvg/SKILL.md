---
name: luft-bodenabfertigung-pruefe-luftvg
description: "Luft Bodenabfertigung Pruefe Luftvg: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Bodenabfertigung Pruefe Luftvg

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Bodenabfertigung Pruefe Luftvg** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-111-bodenabfertigung-zustaendigkeit-pruefe` | Bodenabfertigungs-Mandat: unklar welche Behoerde zustaendig ist Landesluftfahrtbehoerde Wettbewerbsbehoerde oder Flughafenbetreiber. Prueft BADV EU-RL 96/67 EG LuftVG § 6 und Ausschreibungsrecht und liefert Zustaendigkeits-Vermerk fuer Bodenabfertigungs-Streit. |
| `luft-002-luftvg-anwendungsbereich` | Mandant fragt ob LuftVG gilt: Drohnenflug im Ausland Segelflug auf Privatgelände auslaendische Airline auf deutschem Flughafen. Prueft §§ 1 und 6 LuftVG Hoheitsgebiet/Luftfahrzeugbegriff Chicagoer Abkommen Art. 1 sowie EASA Basic Regulation Anwendungsausnahmen und liefert Normanwendbarkeits-Vermerk. |
| `luft-004-flugzeugrolle-und-register` | Mandant will Luftfahrzeugrolle abfragen Eigentuemer klaeren oder Halteraenderung eintragen. Prueft LuftVG §§ 64-65 LuftVZO §§ 14-24 Rollenanforderungen Datenabruf LBA Braunschweig Pfandrechtsregister AG Braunschweig und Cape-Town-ICAO-Register und liefert Registerauszugs-Auswertung mit Handlungsoptionen. |
| `luft-005-luftfahrzeugpfandrecht` | Kreditgeber sichert Flugzeugfinanzierung durch Pfandrecht oder Pfandrechtsinhaber will vollstrecken. Prueft LuftFzgG §§ 1-28 Entstehung Rang Durchsetzung Eintragung AG Braunschweig und Abgrenzung zu Cape Town Convention International Interest und liefert Sicherungsstrategie-Vermerk und Vollstreckungs-Checkliste. |
| `luft-006-pfaendung-flugzeug-deutschland` | Glaeubiger will inlaendisches Flugzeug pfaenden oder Schuldner wehrt Pfaendung ab. Prueft ZPO §§ 808 864-871 Mobiliarpfaendung vs. Luftfahrzeug-Zwangsversteigerung LuftFzgG Pfandrechtsregister AG Braunschweig Arrestgrund ZPO § 917 und liefert Pfaendungsstrategie oder Abwehr-Schriftsatz-Baustein. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Bodenabfertigung Pruefe Luftvg**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-111-bodenabfertigung-zustaendigkeit-pruefe`

**Fokus:** Bodenabfertigungs-Mandat: unklar welche Behoerde zustaendig ist Landesluftfahrtbehoerde Wettbewerbsbehoerde oder Flughafenbetreiber. Prueft BADV EU-RL 96/67 EG LuftVG § 6 und Ausschreibungsrecht und liefert Zustaendigkeits-Vermerk fuer Bodenabfertigungs-Streit.

# Bodenabfertigung – Zuständigkeit prüfen

## Mandantenfall

- Bodenabfertigungsdienstleister wird vom Flughafen ausgeschlossen; fragt welche Behörde zuständig ist.
- Flughafen will selbst Bodenabfertigung beschränken; Airline fragt welche Rechte sie hat.
- Streit über Bodenabfertigungsentgelte; unklar ob Zivilgericht oder Regulierungsbehörde zuständig.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: BADV EU-RL 96/67 EG LuftVG § 6 GWB Verwaltungsrecht.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

BADV EU-RL 96/67 EG LuftVG § 6 GWB Verwaltungsrecht – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

- **LuftVG §§ 6 20 29 31 64**: Genehmigung Betrieb Register Aufsicht.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung Sicherheitsprogramme Aufsicht.
- **EU-VO 1008/2008 Art. 3-9**: Betriebsgenehmigung finanzielle Leistungsfähigkeit Überwachung.
- **Cape Town Convention Art. 2-16**: Internationale Sicherungsinteressen ICAO-Register.
- **LuftFzgG §§ 1-28**: Nationales Pfandrecht Vollstreckung AG Braunschweig.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht Gläubigerrechte.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **BADV § 3**: Genehmigungspflicht für Bodenabfertigungsdienstleister; Zugang zum Bodenabfertigungsmarkt.
- **BADV § 7**: Selbstabfertigungsrecht der Luftverkehrsgesellschaft; Voraussetzungen.
- **BADV § 16**: Auswahlverfahren bei Kapazitätsbeschränkung; Vergabekommission.
- **EU-Richtlinie 96/67/EG Art. 6**: Marktöffnung für Bodenabfertigungsdienste.
- **LuftVG § 45**: Haftung bei Bodenabfertigungsschäden; Verweis auf allg. Deliktsrecht.
## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind alle Register vollständig abgefragt?
3. Laufen Fristen – sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet?
6. Sind Sicherheitsauflagen auf Verhältnismäßigkeit geprüft?
7. Ist Genehmigung nach BADV § 3 aktuell und umfasst die tatsächlich erbrachten Dienste?
8. Hat Flughafen Kapazitätsbeschränkung nach BADV § 16 rechtmäßig festgesetzt?
## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne eigene Prüfung.
- Selbstabfertigungsrecht beansprucht ohne Nachweis nach BADV § 7; Ablehnung durch Flughafen.
- Vergabekommissions-Entscheidung nicht fristgerecht angefochten; Bestandskraft eingetreten.

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Output

Strukturierter Vermerk zu Bodenabfertigung – Zuständigkeit prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. BADV-Compliance-Checkliste. Vergabeverfahrens-Protokoll. Selbstabfertigungs-Antrag.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- EU-Richtlinie 96/67/EG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0067
- LBA: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Bodenabfertigungsdienste und Selbstabfertigungsrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-002-luftvg-anwendungsbereich`

**Fokus:** Mandant fragt ob LuftVG gilt: Drohnenflug im Ausland Segelflug auf Privatgelände auslaendische Airline auf deutschem Flughafen. Prueft §§ 1 und 6 LuftVG Hoheitsgebiet/Luftfahrzeugbegriff Chicagoer Abkommen Art. 1 sowie EASA Basic Regulation Anwendungsausnahmen und liefert Normanwendbarkeits-Vermerk.

# LuftVG Anwendungsbereich – Normanwendbarkeit im Einzelfall

## Mandantenfall

- Drohnenbetreiber fragt ob §§ 21a ff. LuftVG für seinen kommerziellen Multikopter-Einsatz in Österreich gilt weil das Gerät in Deutschland zugelassen ist.
- Segelflugverein prüft ob Platzrunde über eigenem Gelände der LuftVG-Aufsicht unterliegt.
- Ausländische Frachtairline möchte wissen ob sie beim Transit durch deutschen Luftraum einer LBA-Genehmigung bedarf.

## Erste Schritte

1. Klären ob Luftfahrzeug im Sinne § 1 Abs. 2 LuftVG erfasst ist: Flugzeug Drehflügler Luftschiff Segelflugzeug Drohne Ballon oder Raketengerät.
2. Territorialprinzip nach § 1 Abs. 1 LuftVG prüfen: Benutzung des deutschen Luftraums unabhängig von Nationalität des Luftfahrzeugs.
3. Registrierungsstaat-Prinzip prüfen: in Deutschland eingetragenes Luftfahrzeug unterliegt deutschem Recht auch im Ausland für Airworthiness und Betriebsgenehmigung.
4. Ausnahmen checken: § 1 Abs. 3 LuftVG Staatsluftfahrzeuge Chicagoer Abkommen Art. 3 EASA Basic Regulation Art. 2.
5. EU-Recht prüfen: EASA Basic Regulation gilt für gewerbliche Luftfahrt in EU; nationale LuftVG-Normen bleiben für nicht-EASA-Bereich.
6. Ergebnis dokumentieren: Normanwendbarkeits-Vermerk mit Begründung und ggf. Kollisionsnorm.

## Rechtsrahmen

- **LuftVG § 1 Abs. 1**: Benutzung des Luftraums über deutschem Hoheitsgebiet; gilt für alle Luftfahrzeuge.
- **LuftVG § 1 Abs. 2**: Luftfahrzeugbegriff; abschließende Liste erfasster Geräte.
- **LuftVG § 1 Abs. 3**: Ausnahme für Staatsluftfahrzeuge.
- **LuftVG § 6**: Erlaubnispflicht für Flugplätze.
- **Chicagoer Abkommen Art. 1**: Vollständige Souveränität über nationalen Luftraum.
- **Chicagoer Abkommen Art. 3**: Staatsluftfahrzeuge ausgenommen.
- **EASA Basic Regulation EU 2018/1139 Art. 2**: Anwendungsbereich; Ausnahmen für Militär Polizei Zoll.
- **LuftVG § 21a**: Unbemannte Luftfahrtsysteme.

## Prüfraster

1. Liegt ein Luftfahrzeug i.S.d. § 1 Abs. 2 LuftVG vor?
2. Findet Betrieb im deutschen Luftraum statt oder ist deutsches Luftfahrzeug im Ausland?
3. Greift staatliche Ausnahme nach § 1 Abs. 3 LuftVG?
4. Ist EASA-Recht vorrangig?
5. Gilt Drohnen-Sonderregime (EU-VO 2019/947)?
6. Bestehen bilaterale Abkommen die deutsches LuftVG modifizieren?

## Typische Fallstricke

- Drohne als Spielzeug eingestuft obwohl gewerblicher Einsatz § 21a LuftVG auslöst.
- EASA-Recht und LuftVG parallel angewendet ohne Vorrangprüfung.
- Staatsluftfahrzeug-Ausnahme auf kommerzielle Charter ausgedehnt.
- Transitflug als volle LBA-Genehmigungspflicht eingestuft obwohl Art. 5 Chicagoer Abkommen gilt.

## Output

Normanwendbarkeits-Vermerk (1 Seite) mit Subsumtionsschema. Kollisionstabelle LuftVG vs. EASA-Recht vs. Chicagoer Abkommen.

## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Chicagoer Abkommen: https://www.icao.int/publications/pages/doc7300.aspx
- EASA Basic Regulation: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32018R1139
- EU-VO 2019/947: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019R0947

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

### Weitere Praxishinweise

- Anwendungsbereich des LuftVG stets zuerst prüfen bevor andere Normen herangezogen werden.

## 3. `luft-004-flugzeugrolle-und-register`

**Fokus:** Mandant will Luftfahrzeugrolle abfragen Eigentuemer klaeren oder Halteraenderung eintragen. Prueft LuftVG §§ 64-65 LuftVZO §§ 14-24 Rollenanforderungen Datenabruf LBA Braunschweig Pfandrechtsregister AG Braunschweig und Cape-Town-ICAO-Register und liefert Registerauszugs-Auswertung mit Handlungsoptionen.

# Luftfahrzeugrolle und Register – Registerabfrage und Eintragsänderung

## Mandantenfall

- Kreditinstitut finanziert Flugzeugkauf und will sicherstellen dass Pfandrecht korrekt in Luftfahrzeugrolle und Pfandrechtsregister AG Braunschweig eingetragen ist.
- Halter erhält Steuerbescheid für vermeintlich sein Fahrzeug; Luftfahrzeugrolle zeigt noch alten Eigentümer nach Veräußerung.
- Leasingnehmer möchte prüfen ob auf dem geleasten Flugzeug Cape-Town-Eintragungen im ICAO-Register bestehen.

## Erste Schritte

1. Luftfahrzeugrolle beim LBA abrufen: schriftlicher Antrag oder Online-Auskunft; Auszug enthält Eigentümer Halter Hersteller Seriennummer Kennzeichen.
2. Pfandrechtsregister beim AG Braunschweig abfragen: öffentliches Register; Einsicht vor Ort oder Auszug per Antrag.
3. ICAO-Register prüfen: https://www.internationalregistry.aero für Cape-Town-Eintragungen nach Airframe-Seriennummer.
4. Abweichungen zwischen den drei Registern feststellen und Handlungsbedarf benennen.
5. Änderungsantrag bei LBA stellen: Formular mit Belegen für neuen Eigentümer/Halter.
6. Frist nach LuftVZO § 24: Änderungen unverzüglich anzuzeigen; Ordnungswidrigkeit bei Verzögerung.

## Rechtsrahmen

- **LuftVG § 64 Abs. 1**: Luftfahrzeugrolle beim LBA.
- **LuftVG § 64 Abs. 3**: Pflichtangaben in der Rolle.
- **LuftVG § 64 Abs. 5**: Anzeigepflicht bei Änderungen unverzüglich.
- **LuftVZO § 14**: Eintragung von Amts wegen bei Verkehrszulassung.
- **LuftVZO § 19**: Löschung aus der Luftfahrzeugrolle bei Außerdienststellung.
- **LuftFzgG § 1**: Luftfahrzeugpfandrecht; Eintragung AG Braunschweig.
- **Cape Town Convention Art. 16**: Internationales Register; Vorrang vor nationalem Register.
## Prüfraster

1. Stimmt Eingetragener in Luftfahrzeugrolle mit aktuellem Eigentümer überein?
2. Sind Pfandrechte im AG-Braunschweig-Register eingetragen?
3. Existieren Cape-Town-Eintragungen im internationalen Register?
4. Ist Anzeigepflicht nach § 64 Abs. 5 LuftVG erfüllt?
5. Sind Kennzeichen und Seriennummer in allen Registern konsistent?
6. Besteht Löschungsanspruch nach Tilgung des Pfandrechts?

## Typische Fallstricke

- Verkauf ohne Ummeldung in Luftfahrzeugrolle; Steuern und Haftung treffen alten Eingetragenen.
- Pfandrecht im nationalen Register ohne Cape-Town-Eintrag; internationaler Gläubiger verliert Vorrang.
- Löschung aus Rolle ohne vorherige Entpfandung; Register widersprüchlich.
- ICAO-Registerauszug nicht eingeholt; versteckte internationale Belastungen.


## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Registerauszugs-Auswertung: Eigentümer/Halter/Pfandrechte je Register. Handlungsmatrix. Muster-Änderungsantrag LBA.

## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- LuftVZO: https://www.gesetze-im-internet.de/luftvzo/
- Internationales Register Cape Town: https://www.internationalregistry.aero
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Luftfahrzeugrolle/luftfahrzeugrolle_node.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-005-luftfahrzeugpfandrecht`

**Fokus:** Kreditgeber sichert Flugzeugfinanzierung durch Pfandrecht oder Pfandrechtsinhaber will vollstrecken. Prueft LuftFzgG §§ 1-28 Entstehung Rang Durchsetzung Eintragung AG Braunschweig und Abgrenzung zu Cape Town Convention International Interest und liefert Sicherungsstrategie-Vermerk und Vollstreckungs-Checkliste.

# Luftfahrzeugpfandrecht – Bestellung, Rang und Vollstreckung

## Mandantenfall

- Bank finanziert Kauf eines Turboprop-Flugzeugs und will erstrangiges Pfandrecht bestellen; unklar ob deutsches LuftFzgG oder Cape Town Convention vorgeht.
- Leasinggeber meldet sich weil Leasingnehmer insolvent ist und Pfandrecht auf dem Flugzeug lastet; Rangfrage mit anderen Gläubigern.
- Flugzeug wird versteigert; Käufer fragt ob er lastenfrei erwirbt oder Pfandrechte übergehen.

## Erste Schritte

1. Registrierungsstaat prüfen: deutsches Pfandrecht setzt Eintragung ins Pfandrechtsregister AG Braunschweig voraus.
2. Pfandrechtsbestellung: notarielle Einigung plus Eintragungsantrag beim AG Braunschweig; kein Besitzerfordernis.
3. Rang klären: Zeitpunkt der Eintragung entscheidet (LuftFzgG § 12); ältere Eintragung geht vor.
4. Cape Town Convention prüfen: internationales Sicherungsinteresse im ICAO-Register geht nationalem Pfandrecht vor wenn früher eingetragen.
5. Vollstreckung: Pfandgläubiger betreibt Zwangsversteigerung ZPO §§ 864 ff. oder nutzt Cape Town Remedies Art. 8 ff. Aircraft Protocol.
6. Insolvenz: Absonderungsrecht nach InsO § 50; Cape Town Art. 30 schützt internationale Sicherungsinteressen.

## Rechtsrahmen

- **LuftFzgG § 1**: Entstehung durch Einigung und Eintragung; kein Besitzerfordernis.
- **LuftFzgG § 12**: Rangordnung nach Eintragungszeitpunkt.
- **LuftFzgG § 22**: Vollstreckung; Verweis auf ZPO-Zwangsversteigerungsrecht.
- **ZPO §§ 864-871**: Zwangsversteigerung von Luftfahrzeugen.
- **Cape Town Convention Art. 2**: Internationales Sicherungsinteresse.
- **Aircraft Protocol Art. IX**: Rangverhältnis; Eintragungszeitpunkt im ICAO-Register entscheidend.
- **InsO § 50**: Absonderungsrecht des Pfandgläubigers in Insolvenz.
## Prüfraster

1. Ist Pfandrecht korrekt im AG Braunschweig eingetragen?
2. Besteht konkurrierendes Cape-Town-Interesse im ICAO-Register?
3. Welcher Eintrag ist zeitlich früher?
4. Ist Pfandgläubiger bei Insolvenz als Absonderungsberechtigter angemeldet?
5. Wurde Flugzeug sichergestellt (Arrest LuftFzgG § 24)?
6. Besteht gesetzliches Pfandrecht (Werker/Lagerer) mit Vorrang?

## Typische Fallstricke

- Pfandrecht ohne notarielle Einigung bestellt; formunwirksam.
- Cape-Town-Register ignoriert; internationaler Gläubiger hat ältere Eintragung.
- Insolvenzanmeldung versäumt; Pfandrecht geht in Restschuldmasse auf.
- Zwangsversteigerung ohne Vorabsicherung; Schuldner verbringt Flugzeug ins Ausland.


## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Sicherungsstrategie-Vermerk mit Pfandrechtsbestellung inkl. Cape-Town-Check. Ranganalyse-Tabelle. Vollstreckungs-Checkliste.

## Quellen

- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- Pfandrechtsregister: https://www.verwaltungsdaten-informationsplattform.de/register/22
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-006-pfaendung-flugzeug-deutschland`

**Fokus:** Glaeubiger will inlaendisches Flugzeug pfaenden oder Schuldner wehrt Pfaendung ab. Prueft ZPO §§ 808 864-871 Mobiliarpfaendung vs. Luftfahrzeug-Zwangsversteigerung LuftFzgG Pfandrechtsregister AG Braunschweig Arrestgrund ZPO § 917 und liefert Pfaendungsstrategie oder Abwehr-Schriftsatz-Baustein.

# Pfändung Flugzeug Deutschland – Zwangsvollstreckung und Gegenargumentation

## Mandantenfall

- Urteilsgläubiger will Flugzeug des insolvenznahen Luftfahrtunternehmens pfänden bevor Insolvenzantrag gestellt wird.
- Fluggesellschaft erhält Pfändungs- und Überweisungsbeschluss; Mandant will aufschiebende Wirkung oder Freigabe erwirken.
- Leasinggesellschaft will Flugzeug nach Vertragsbeendigung zurückholen; Frage ob Pfändung oder einstweilige Verfügung.

## Erste Schritte

1. Vollstreckungstitel prüfen: rechtskräftiges Urteil Vollstreckungsbescheid oder vollstreckbare notarielle Urkunde (ZPO § 794).
2. Art der Vollstreckung bestimmen: Pfändung beweglicher Sachen (§ 808 ZPO) bei Besitzkontrolle; Luftfahrzeug-Zwangsversteigerung (LuftFzgG §§ 22 ff.) bei Grundpfandrechts-ähnlichem Vorgehen.
3. Arrest prüfen: bei Fluchgefahr Arrestantrag §§ 916 ff. ZPO beim Vollstreckungsgericht am Standort des Flugzeugs.
4. Pfandrechte im AG Braunschweig abfragen: bestehende Pfandrechte haben Vorrang; Gläubiger rückt nach.
5. Insolvenzrisiko einschätzen: bei drohender Insolvenz Anmeldung als Insolvenzgläubiger prüfen; Absonderungsrecht InsO § 50.
6. Abwehr prüfen: § 765a ZPO Vollstreckungsschutz; § 767 ZPO Einwendungsklage; § 771 ZPO Drittwiderspruchsklage.

## Rechtsrahmen

- **ZPO §§ 808-827**: Pfändung beweglicher Sachen durch Gerichtsvollzieher; Besitzerfordernis.
- **ZPO §§ 864-871**: Zwangsversteigerung von Luftfahrzeugen; § 864 Abs. 2 Analogie.
- **LuftFzgG §§ 22-28**: Zwangsvollstreckung in eingetragene Luftfahrzeuge.
- **ZPO §§ 916-934**: Arrest; Arrestanspruch und Arrestgrund bei Fluchtverdacht.
- **ZPO § 771**: Drittwiderspruchsklage des Eigentümers gegen Pfändung fremder Sachen.
- **InsO § 89**: Vollstreckungssperre nach Insolvenzeröffnung.
- **Cape Town Convention Art. 10**: Zwangsmassnahmen in Insolvenz.
## Prüfraster

1. Liegt wirksamer Vollstreckungstitel vor?
2. Befindet sich Flugzeug im Inland?
3. Bestehen vorrangige Pfandrechte im AG-Braunschweig-Register?
4. Ist Insolvenzantrag bereits gestellt (Vollstreckungssperre § 89 InsO)?
5. Besteht Arrestgrund (Fluchtverdacht Veräußerungsabsicht)?
6. Ist Cape-Town-Gläubiger bekannt der parallel Entregistrierung betreibt?

## Typische Fallstricke

- Pfändung nach §§ 808 ff. ZPO ohne Besitz scheitert; Luftfahrzeug-Vollstreckung braucht anderen Weg.
- Insolvenzsperre übersehen: nach Insolvenzeröffnung Vollstreckung unwirksam.
- Arrest zu eng beantragt; Gericht lehnt mangels Arrestgrund ab.
- Cape-Town-Gläubiger hat Vorrang und betreibt parallel Entregistrierung.


## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Pfändungsstrategie-Vermerk mit Vollstreckungsweg und Ranganalyse. Arrest-Antrag-Baustein. Abwehr-Schriftsatz-Baustein für Schuldner.

## Quellen

- ZPO: https://www.gesetze-im-internet.de/zpo/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
