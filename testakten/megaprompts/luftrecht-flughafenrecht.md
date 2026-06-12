# Megaprompt: luftrecht-flughafenrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 120 Skills (gekuerzt fuer Chat-Fenster) des Plugins `luftrecht-flughafenrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Luftrecht und Flughafenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und e…
2. **aircraft-arrest-airline-finanzielle** — Mandant will Flugzeug im Ausland arrestieren oder auslaendischer Glaeubiger arrestiert in Deutschland. Prueft Cape Town …
3. **airline-dashboard-bauen** — Kanzlei oder Mandant braucht operatives Airline-Dashboard für laufendes Mandat: Genehmigungsstatus Flotte Slots Sicherhe…
4. **airline-finanzielle-leistungsfaehigkei** — LBA prueft finanzielle Leistungsfaehigkeit nach EU-VO 1008/2008 Art. 5 oder Mandant bewertet Insolvenzrisiko einer Flugg…
5. **airline-genehmigung-pruefen** — Airline-Genehmigungsstand ist unklar: Betriebsgenehmigung AOC Streckengenehmigung oder Sonderflugerlaubnis fehlt oder la…
6. **airline-insolvenzrisiko-markieren** — Mandant will Insolvenzrisiko einer Airline fruehzeitig erkennen: sinkende Liquiditaet schlechte Ratings Zahlungsruecksta…
7. **airline-local-dashboard-bauen** — Deutsches Kanzleiteam muss auslaendischen Anwalt für Airline-Mandat briefen: Arrest Insolvenz Cape-Town oder Betriebsgen…
8. **airline-mandantenmemo-schreiben** — Anwalt schreibt Mandantenmemo für Airline zu komplexem Luftrechtsfall: Genehmigungsrisiko Sicherheitsauflage Slot-Verlus…

---

## Skill: `kaltstart-triage`

_Luftrecht und Flughafenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe._

# Luftrecht und Flughafenrecht - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Luftrecht Flughafenrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Startfragen

1. Wer nutzt das Plugin: Laie, Verband, Kanzlei, Behörde, Unternehmen, Presse, Verwaltung oder Fachabteilung?
2. Welche Entscheidung steht jetzt an und welche Frist läuft?
3. Welche Dokumente liegen vor, welche fehlen und welche Quelle muss live geprüft werden?
4. Welche Behörde, welches Gericht, welches Register oder welcher private Akteur ist betroffen?
5. Soll am Ende ein Antrag, ein Widerspruch, eine Klage-/Eilantragslinie, ein Dashboard, ein Memo oder ein Schreiben entstehen?

## Workflow

1. Sachverhalt in Akte, Normpfad, Zuständigkeit, Frist, Beweis und Ziel zerlegen.
2. Die einschlägige Norm nicht aus dem Gedächtnis final behaupten, sondern als Live-Check gegen amtliche Quelle markieren.
3. Ablehnungs-, Kosten-, Zuständigkeits- und Beweisrisiken offen in einer Ampel führen.
4. Bei Mehr-Ebenen-Recht immer Bund, Land, Kommune, EU/international und Spezialgesetz trennen.
5. Ausgabe mit konkretem nächsten Schritt, offenen Rückfragen und einer kurzen Fassung für Nichtjuristen schließen.

## Typische Ausgaben

- Prüfvermerk mit Normpfad und Live-Check-Liste
- Fristen- und Zuständigkeitsmatrix
- Entwurf für Antrag, Widerspruch, Klagebaustein oder Behördenbrief
- Dashboard-/Tracker-Eintrag mit Status, Risiko und nächster Aktion

## Red Flags

- blindes Zitieren nicht verifizierter Rechtsprechung oder alter Gesetzesstände
- falsche Behörde, falscher Rechtsweg oder unbemerkte Spezialzuständigkeit
- Gebühren-, Frist-, Präklusions-, Geheimschutz-, Datenschutz- oder Drittbetroffenenproblem
- politisch klingende Bewertung ohne saubere Rechtsgrundlage und Beleglogik

## Quellen- und Qualitätsregel

Primär mit amtlichen Gesetzestexten, Behördenhinweisen, Gerichtsentscheidungen mit Datum/Aktenzeichen und frei prüfbaren Quellen arbeiten. Literatur, Datenbanken hinter Paywalls und Fundstellen ohne Nutzerquelle nicht behaupten. Wenn Landesrecht, EU-Recht oder ausländisches Recht berührt ist, den Rechtsstand ausdrücklich live prüfen und die Ausgabe als Arbeitsfassung kennzeichnen.

---

## Skill: `aircraft-arrest-airline-finanzielle`

_Mandant will Flugzeug im Ausland arrestieren oder auslaendischer Glaeubiger arrestiert in Deutschland. Prueft Cape Town Convention Art. 8-10 Aircraft Protocol Remedies IDERA bilaterale Vollstreckungsvertraege und nationales ZPO-Arrestrecht und liefert Arrest-Strategie und Local-Counsel-Briefing-V..._

# Aircraft Arrest International – grenzüberschreitender Flugzeug-Arrest

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Deutscher Leasinggeber will nach Vertragsbruch des ausländischen Leasingnehmers das Flugzeug bei Zwischenstopp in London arrestieren lassen.
- Ausländischer Gläubiger will Flugzeug einer deutschen Airline bei Landung in New York sichern.
- Airline-Insolvenz: mehrere Gläubiger aus verschiedenen Ländern konkurrieren um Arreste auf die verbliebene Flotte.

## Erste Schritte

1. Aufenthaltsort des Flugzeugs ermitteln: Flugplan ADS-B-Tracking Flughafendaten; Jurisdiktion folgt physischem Standort.
2. Cape Town Convention prüfen: beide Länder Vertragsstaaten? Dann gelten Art. 8-15 Aircraft Protocol für Sicherungsrechte und Remedies.
3. IDERA prüfen: Irrevocable Deregistration and Export Request Authorisation; ermöglicht Entregistrierung ohne Gerichtsverfahren.
4. Lokalen Counsel beauftragen: Arrest-Antrag nach lokaler ZPO; in UK CPR Part 61 in USA Federal Aviation Act.
5. Cape Town Remedies in Insolvenz: Art. 30 Aircraft Protocol; Alternative A (automatische Herausgabe) oder Alternative B (Genehmigungserfordernis).
6. Koordination: deutsche Vollstreckungsmaßnahmen (ZPO §§ 916 ff.) parallel zu internationalem Arrest.

## Rechtsrahmen

- **Cape Town Convention Art. 8**: Gläubigerrechte bei Nichterfüllung; Besitznahme Veräußerung Vermietung.
- **Cape Town Convention Art. 10**: Zusätzliche Remedies in Insolvenz.
- **Aircraft Protocol Art. IX**: Entregistrierung und Verbringung; IDERA als Instrument.
- **Aircraft Protocol Art. XI Alt. A/B**: Insolvenz-Schutzregime; Unterschiede je nach Ratifikationserklärung.
- **ZPO §§ 916-934**: Arrestrecht; Arrestanspruch und Arrestgrund.
- **Montreal Convention Art. 35**: Verjährungsfrist 2 Jahre für Frachtansprüche.
- **Chicago Convention Art. 79**: Zusammenarbeit der Staaten bei Luftfahrt-Streitigkeiten.

## Prüfraster

1. Sind beide Staaten Vertragsstaaten der Cape Town Convention?
2. Ist IDERA korrekt registriert und beim ICAO-Register hinterlegt?
3. Hat der Staat Alternative A oder B erklärt?
4. Besteht Arrestgrund (Fluchtverdacht Veräußerungsabsicht Zahlungsunfähigkeit)?
5. Rangverhältnis der Gläubiger im ICAO-Register?
6. Ist Insolvenzverfahren eröffnet (lex fori concursus)?

## Typische Fallstricke

- IDERA nicht hinterlegt; Entregistrierungsweg entfällt.
- Staat des Flugzeugstandorts hat Cape Town nicht ratifiziert; rein nationales Recht gilt.
- Alternative-B-Staat: kein automatischer Herausgabeanspruch in Insolvenz.
- Parallel laufende nationale Arreste konkurrieren; Prioritätsreihenfolge unklar.

## Quellen

- Cape Town Convention/Aircraft Protocol: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- ICAO Internationales Register: https://www.internationalregistry.aero
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- ZPO: https://www.gesetze-im-internet.de/zpo/

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

---

## Skill: `airline-dashboard-bauen`

_Kanzlei oder Mandant braucht operatives Airline-Dashboard für laufendes Mandat: Genehmigungsstatus Flotte Slots Sicherheitsauflagen Insolvenzrisiko. Skill strukturiert Datenquellen LBA EU-VO 1008/2008 Art. 9 Fluko ICAO-Register und liefert befuellbares Dashboard-Template mit Aktualisierungs-Check..._

# Airline – Dashboard bauen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Kanzlei betreut Airline dauerhaft und braucht strukturiertes internes Dashboard für Mandatsstatus Fristen und Risiken.
- Insolvenzverwalter übernimmt Airline; braucht sofort strukturierten Überblick über alle relevanten Daten.
- Investor führt Due Diligence durch; Dashboard als Instrument für strukturierte Datenzusammenführung.

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

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-finanzielle-leistungsfaehigkei`

_LBA prueft finanzielle Leistungsfaehigkeit nach EU-VO 1008/2008 Art. 5 oder Mandant bewertet Insolvenzrisiko einer Fluggesellschaft. Prueft Nachweispflichten Eigenkapital Versicherung Businessplan LBA-Auflagenpraxis und Fruehwarnindikatoren und liefert Leistungsfaehigkeits-Bewertungs-Vermerk im L..._

# Airline – Finanzielle Leistungsfähigkeit prüfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Startup-Airline beantragt Betriebsgenehmigung; LBA fordert Nachweis finanzieller Leistungsfähigkeit nach EU-VO 1008/2008 Art. 5; Mandant fragt welche Unterlagen ausreichen.
- Bestehende Airline erhält LBA-Schreiben über Zweifel an fortlaufender Leistungsfähigkeit nach Art. 9; Mandant hat einen Monat zur Stellungnahme.
- Investor prüft Beteiligung an einer Regionalairline; Due-Diligence-Check der Betriebsgenehmigung und Liquiditätslage.

## Erste Schritte

1. Genehmigungstyp bestimmen: Neugenehmigung (Art. 5) oder laufende Überwachung (Art. 9).
2. Nachweisunterlagen zusammenstellen: Jahresabschluss (geprüft) Eigenkapitalnachweis Versicherungspolice Businessplan inkl. Liquiditätsplanung für mindestens 3 Monate.
3. Mindestkapital prüfen: Art. 5 Abs. 2 gibt Richtwerte; LBA kann höhere Anforderungen stellen je nach Flottengröße und Streckennetz.
4. LBA-Prüfstruktur verstehen: Trigger für Überprüfung sind Verluste Kapitalherabsetzung Lohnrückstände Steuerschulden.
5. Gegenmaßnahmen bei LBA-Zweifeln: sofortige schriftliche Stellungnahme aktualisierter Businessplan Bankbestätigung über Kreditlinie.
6. Insolvenzfrühwarnung dokumentieren: Z-Score-Analyse oder Creditreform-Bericht beifügen.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 5**: Finanzielle Leistungsfähigkeit als Genehmigungsvoraussetzung.
- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung; LBA kann Genehmigung aussetzen oder widerrufen.
- **EU-VO 1008/2008 Art. 9 Abs. 1**: Mitteilungspflicht der Airline bei finanziellen Schwierigkeiten.
- **LuftVG § 20 Abs. 1**: Betriebsgenehmigung als nationale Umsetzungsnorm.
- **InsO §§ 15a 17-18**: Insolvenzantragspflicht; Zahlungsunfähigkeit und drohende Zahlungsunfähigkeit.
- **LuftBO § 9**: Haftpflichtversicherungspflicht; Mindestdeckungssummen.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Erfüllt Jahresabschluss die LBA-Mindestanforderungen (geprüft aktuell)?
2. Ist Eigenkapital ausreichend gemäß Art. 5 Abs. 2?
3. Besteht Haftpflichtversicherung in vorgeschriebener Höhe?
4. Gibt es Steuerschulden Lohnrückstände oder offene Sozialversicherungsbeiträge?
5. Ist Mitteilungspflicht nach Art. 9 Abs. 1 ausgelöst?
6. Sind Frühwarnindikatoren (negativer Cashflow Kreditkündigung) dokumentiert?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Ungeprüfter Jahresabschluss reicht nicht; LBA besteht auf Wirtschaftsprüfer-Testat.
- Eigenkapital-Mindestbetrag als Einmalnachweis missverstanden; LBA überwacht fortlaufend.
- Mitteilungspflicht nach Art. 9 Abs. 1 übersehen; LBA legt Untätigkeit als Verschleierung aus.
- Businessplan zu optimistisch; LBA lehnt ab und Mandant muss nachlegen.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LBA Betriebsgenehmigung: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-genehmigung-pruefen`

_Airline-Genehmigungsstand ist unklar: Betriebsgenehmigung AOC Streckengenehmigung oder Sonderflugerlaubnis fehlt oder laeuft ab. Prueft EU-VO 1008/2008 LuftVG § 20 EASA EU-VO 965/2012 Part-OPS und Bilateralabkommen und liefert Genehmigungsstatus-Vermerk mit Handlungsbedarf und Fristen im Luftrech..._

# Airline – Genehmigung prüfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Airline-Geschäftsführer fragt vor Saisonstart ob alle Genehmigungen vorliegen und keine abgelaufen sind.
- Neue Streckeneröffnung nach Nordamerika; Frage ob bestehende Betriebsgenehmigung abdeckt oder Bilateralabkommen nötig.
- Betriebsgenehmigung erlischt durch Nichterfüllung von Auflagen; was ist zu tun?

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

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-insolvenzrisiko-markieren`

_Mandant will Insolvenzrisiko einer Airline fruehzeitig erkennen: sinkende Liquiditaet schlechte Ratings Zahlungsrueckstaende. Prueft EU-VO 1008/2008 Art. 9 Fruehwarnindikatoren InsO §§ 15a 17-19 Antragspflicht und Haftungsrisiken Geschaeftsfuehrer und liefert Risikoampel-Bewertung und Geschaeftsf..._

# Airline – Insolvenzrisiko markieren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Leasinggeber beobachtet dass Airline Leasingraten verzögert zahlt und Medien über Liquiditätsprobleme berichten; möchte Risikobewertung.
- Airline-Geschäftsführer fragt ab wann Insolvenzantragspflicht entsteht und wie er persönliche Haftung vermeidet.
- Gläubiger-Ausschuss prüft rückwirkend ob Geschäftsführer zu spät Insolvenz angemeldet hat.

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

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-local-dashboard-bauen`

_Deutsches Kanzleiteam muss auslaendischen Anwalt für Airline-Mandat briefen: Arrest Insolvenz Cape-Town oder Betriebsgenehmigung. Skill erstellt strukturiertes englisches Briefing-Memo mit Sachverhalt deutschem Rechtsrahmen Cape-Town-Status IDERA und konkreten Fragen an Local Counsel im Luftrecht..._

# Airline – Local Counsel briefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Deutsche Kanzlei soll Arrest auf Flugzeug einer deutschen Airline in Dubai beantragen; lokaler Anwalt braucht Briefing zu deutschem Pfandrecht und Cape-Town-Status.
- Irischer Leasinggeber gibt deutschem Anwalt Auftrag Local Counsel zu briefen für Herausgabeklage gegen insolvente Airline.
- Insolvenzverwalter beauftragt Kanzlei in London zur Rückholung von Flugzeugen; Briefing zu deutschem Insolvenzrecht und Cape Town nötig.

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

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-mandantenmemo-schreiben`

_Anwalt schreibt Mandantenmemo für Airline zu komplexem Luftrechtsfall: Genehmigungsrisiko Sicherheitsauflage Slot-Verlust oder Insolvenznaehe. Skill strukturiert Memo nach Sachverhalt Rechtslage Handlungsoptionen Risikobewertung und Empfehlung und liefert fertigen Memo-Baustein mit Nächste-Schrit..._

# Airline – Mandantenmemo schreiben

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Airline-Vorstand braucht Memo nach LBA-Schreiben zu finanzieller Leistungsfähigkeit; Entscheidungsgrundlage für Vorstandssitzung.
- Airline soll Insolvenz beantragen; Memo an Gesellschafter über Rechtslage Ablauf und Alternativen.
- Audit-Finding Level 1; Memo an Airline-Compliance-Abteilung über sofortigen Handlungsbedarf.

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

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

