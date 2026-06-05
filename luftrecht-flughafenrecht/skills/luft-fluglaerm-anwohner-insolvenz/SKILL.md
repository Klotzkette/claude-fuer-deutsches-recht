---
name: luft-fluglaerm-anwohner-insolvenz
description: "Luft Fluglaerm Anwohner Insolvenz: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Fluglaerm Anwohner Insolvenz

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Fluglaerm Anwohner Insolvenz** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-017-fluglaerm-und-anwohner` | Anwohner klagt gegen Fluglaerm oder Flughafen baut Schallschutzprogramm auf. Prueft FluglaermG §§ 1-9 Laermschutzbereiche Tagschutzzone 65-60 dB Nachtschutzzone 55 dB BImSchG § 41 und Schallschutzansprueche und liefert Klagebaustein und Schallschutzanspruchs-Checkliste mit Fristen. |
| `luft-018-insolvenz-fluggesellschaft` | Airline-Insolvenz: Passagier Glaeubiger Leasinggeber oder Slot-Halter fragt nach Anspruechen. Prueft InsO §§ 21 47 50 103 Absonderungsrecht Leasingvertrag Slot-Nicht-Uebertragbarkeit EuGH Cape-Town-Insolvenzschutz Art. XI Aircraft Protocol und liefert Glaeubiger-Strategie-Vermerk und Anmeldeformular-Baustein. |
| `luft-019-leasing-und-cape-town-bezuege` | Wet-Lease Dry-Lease oder Finance-Lease eines Flugzeugs mit Cape-Town-Registrierung. Prueft Cape Town Convention Art. 2-9 Internationale Interests LuftFzgG nationales Pfandrecht IDERA Aircraft Protocol Art. XI Alternative A/B und liefert Leasing-Sicherungsstrategie und Vertrags-Pruef-Checkliste. |
| `luft-020-aviation-dashboard` | Mandant braucht Echtzeit-Lageueberblick ueber eine Airline: Betriebsgenehmigung AOC Flotte Slots Sicherheitsstatus Insolvenzrisiko. Skill erstellt Dashboard-Matrix aus LBA-Register EU-VO 1008/2008 Art. 9 Indikatoren FluglaermG-Zonen und Cape-Town-Register und liefert einseitige Lagebewertung mit Ampel-Rating. |
| `luft-022-airline-register-auswerten` | Mandant will Luftfahrzeugrolle Pfandrechtsregister und Cape-Town-Register einer Airline auswerten. Skill fuehrt strukturierte Registerabfrage LBA LuftVG § 64 AG Braunschweig LuftFzgG und ICAO-Register durch und liefert Registerauszugs-Auswertungs-Bericht mit Eigentuemerstruktur und Belastungen. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Fluglaerm Anwohner Insolvenz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-017-fluglaerm-und-anwohner`

**Fokus:** Anwohner klagt gegen Fluglaerm oder Flughafen baut Schallschutzprogramm auf. Prueft FluglaermG §§ 1-9 Laermschutzbereiche Tagschutzzone 65-60 dB Nachtschutzzone 55 dB BImSchG § 41 und Schallschutzansprueche und liefert Klagebaustein und Schallschutzanspruchs-Checkliste mit Fristen.

# Fluglärm und Anwohner – Lärmschutzbereiche und Schallschutzansprüche

## Mandantenfall

- Hausbesitzer im Lärmschutzbereich eines Großflughafens beantragt Schallschutzmaßnahmen; Flughafen lehnt ab mit der Begründung das Haus liege außerhalb der Nacht-Schutzzone.
- Anwohnerinitiative klagt gegen Planfeststellungsbeschluss wegen unzureichender Lärmschutzauflagen bei Flughafenerweiterung.
- Gemeinde prüft Widerspruch gegen Nachtflug-Genehmigung die über Flughafenbetriebsgenehmigung hinausgeht.

## Erste Schritte

1. Lärmschutzbereich bestimmen: Flughafen muss Lärmschutzbereich nach FluglärmG § 2 festgesetzt haben; Tag-Schutzzone 1 (65 dB) Tag-Schutzzone 2 (60 dB) Nacht-Schutzzone (55 dB Mittelungspegel).
2. Schallschutzanspruch prüfen: FluglärmG §§ 7-9; bauliche Schallschutzmaßnahmen auf Kosten des Flughafenbetreibers.
3. Eigentümer/Mieter-Frage klären: § 7 Abs. 1 FluglärmG Anspruch des Eigentümers.
4. Antrag beim Flughafenbetreiber stellen: fristgebunden; Anspruchsverlust bei Fristversäumnis.
5. Planfeststellungsklage: Abwägungsfehler bei Lärmschutzauflagen angreifen.
6. Nachtflugbeschränkungen: BVerwG hat Nachtfluggenehmigungen an restriktive Bedingungen geknüpft.

## Rechtsrahmen

- **FluglärmG § 1**: Zweck und Anwendungsbereich.
- **FluglärmG § 2**: Festsetzung des Lärmschutzbereichs mit Tag- und Nacht-Schutzzonen.
- **FluglärmG §§ 7-9**: Schallschutzansprüche; bauliche Maßnahmen auf Kosten des Betreibers.
- **BImSchG § 41**: Schutz vor schädlichen Umwelteinwirkungen bei Verkehrswegen.
- **BImSchG § 42**: Entschädigungsansprüche bei Überschreitung von Immissionsgrenzwerten.
- **LuftVG § 29b**: Gebot der gegenseitigen Rücksichtnahme.
- **BVerwG 4 A 1001.04**: Nachtflugregelung FRA; Leitentscheidung für Verhältnismäßigkeit.

## Prüfraster

1. Liegt das Anwesen innerhalb eines Lärmschutzbereichs nach FluglärmG § 2?
2. Welche Schutzzone ist einschlägig?
3. Wurde Antrag auf Schallschutz fristgerecht gestellt?
4. Überschreiten Lärmwerte die Schwellenwerte des FluglärmG?
5. Bestehen Fehler in der UVP oder Abwägung des Planfeststellungsbeschlusses?
6. Ist Nachtflug über genehmigte Zeiten hinaus rechtswidrig?

## Typische Fallstricke

- Anwesen knapp außerhalb Lärmschutzbereich; kein gesetzlicher Anspruch.
- Schallschutzantrag zu spät gestellt; Frist abgelaufen Anspruch erloschen.
- Planfeststellungsklage ohne Einwendung im Verfahren; Präklusion.
- Nachtflugregelung als Planfeststellungsbestandteil angreifen statt als separate Genehmigung.

## Output

Schallschutzanspruchs-Checkliste mit Fristen. Klagebaustein gegen Planfeststellungsbeschluss (Lärmschutzfehler). Muster-Antrag an Flughafenbetreiber.

## Quellen

- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- BImSchG: https://www.gesetze-im-internet.de/bimschg/
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- BVerwG: https://www.bverwg.de

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

## 2. `luft-018-insolvenz-fluggesellschaft`

**Fokus:** Airline-Insolvenz: Passagier Glaeubiger Leasinggeber oder Slot-Halter fragt nach Anspruechen. Prueft InsO §§ 21 47 50 103 Absonderungsrecht Leasingvertrag Slot-Nicht-Uebertragbarkeit EuGH Cape-Town-Insolvenzschutz Art. XI Aircraft Protocol und liefert Glaeubiger-Strategie-Vermerk und Anmeldeformular-Baustein.

# Insolvenz Fluggesellschaft – Gläubigerrechte und Masseschutz

## Mandantenfall

- Leasinggesellschaft hat 3 Flugzeuge an insolvente Airline vermietet; Insolvenzverwalter verweigert Herausgabe; IDERA hinterlegt.
- Passagier hat bereits bezahlte Tickets; Airline insolvent; fragt ob Insolvenzforderung oder Masseforderung.
- Zulieferer (Catering) hat offene Rechnungen; fragt nach Rang in Insolvenz.

## Erste Schritte

1. Insolvenzantrag und Verfahrensstand prüfen: vorläufige Insolvenzverwaltung (§ 21 InsO) oder eröffnetes Verfahren (§ 27 InsO)?
2. Leasingvertrag qualifizieren: echtes Leasing (Eigentum beim Leasinggeber) oder Finanzierungsleasing? Insolvenzverwalter kann nach §§ 103 108 InsO erfüllen oder ablehnen.
3. Cape Town Convention: IDERA hinterlegt? Entregistrierung und Herausgabe auch in Insolvenz möglich (Art. XI Aircraft Protocol Alternative A).
4. Passagierticket: Insolvenzforderung (§ 38 InsO) oder Masseforderung (§ 55 InsO) wenn Flug nach Insolvenzeröffnung angeboten.
5. Slot-Frage: Slots nicht Massebestandteil; Flughafenkoordinator zieht Slots ein.
6. Forderungsanmeldung: beim Insolvenzverwalter innerhalb gesetzter Frist; Formular Forderungsbetrag Rang.

## Rechtsrahmen

- **InsO § 21 Abs. 2**: Vorläufige Insolvenzverwaltung; Verfügungsverbot.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber).
- **InsO § 50**: Absonderungsrecht des Pfandgläubigers.
- **InsO §§ 103 108**: Wahlrecht bei gegenseitigen Verträgen; Dauerschuldverhältnisse.
- **InsO § 55**: Masseverbindlichkeiten; Vorrang vor Insolvenzforderungen.
- **Aircraft Protocol Art. XI Alternative A**: Automatische Herausgabepflicht in Insolvenz nach 60 Tagen.
- **EuGH C-272/06**: Slots keine übertragbaren Vermögenswerte.

## Prüfraster

1. Ist Insolvenzverfahren eröffnet oder noch vorläufige Verwaltung?
2. Hat Leasinggeber Eigentumsrecht (§ 47 InsO Aussonderungsrecht)?
3. Ist IDERA korrekt beim ICAO-Register hinterlegt?
4. Hat Deutschland Alternative A des Aircraft Protocols erklärt?
5. Ist Passagieranspruch Insolvenz- oder Masseforderung?
6. Wurden Slot-Rückgabe und Betriebsgenehmigungsende an LBA gemeldet?

## Typische Fallstricke

- Leasinggeber meldet Forderung als Insolvenzgläubiger statt Aussonderung zu betreiben.
- IDERA nicht hinterlegt; Cape-Town-Herausgaberecht entfällt.
- Passagier meldet Forderung zu spät; Fristversäumnis.
- Slot-Übertragung an Käufer versucht; scheitert nach EuGH C-272/06.

## Output

Gläubiger-Strategie-Vermerk nach Rang und Anspruchstyp. Forderungsanmeldungs-Baustein. Cape-Town-IDERA-Checkliste.

## Quellen

- InsO: https://www.gesetze-im-internet.de/inso/
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- EuGH Urteile: https://eur-lex.europa.eu
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-019-leasing-und-cape-town-bezuege`

**Fokus:** Wet-Lease Dry-Lease oder Finance-Lease eines Flugzeugs mit Cape-Town-Registrierung. Prueft Cape Town Convention Art. 2-9 Internationale Interests LuftFzgG nationales Pfandrecht IDERA Aircraft Protocol Art. XI Alternative A/B und liefert Leasing-Sicherungsstrategie und Vertrags-Pruef-Checkliste.

# Leasing und Cape Town – Flugzeugsicherung im internationalen Leasing

## Mandantenfall

- Irischer Leasinggeber verleast Boeing an deutsche Regionalairline (Dry-Lease); Vertrag nach englischem Recht; Sicherungsinteresse soll im ICAO-Register eingetragen werden.
- Wet-Lease-Arrangement: ausländische Airline stellt deutschem Carrier Flugzeug mit Crew zur Verfügung; AOC-Fragen und Betriebsgenehmigung unklar.
- Finance-Lease läuft aus; Airline will Kaufoption ausüben; Umschreibung in Luftfahrzeugrolle nötig.

## Erste Schritte

1. Leasingtyp bestimmen: Dry-Lease (Flugzeug ohne Crew Leasingnehmer nutzt eigenes AOC) Wet-Lease (Flugzeug mit Crew und AOC des Leasinggebers) Finance-Lease (wirtschaftliches Eigentum beim Leasingnehmer).
2. Cape Town Registration: internationales Sicherungsinteresse des Leasinggebers im ICAO-Register eintragen; IDERA hinterlegen.
3. IDERA-Prüfung: ermöglicht Entregistrierung bei Vertragsbruch ohne Gerichtsverfahren.
4. Wet-Lease: LBA-Genehmigung nach LuftVG § 21a; EU-intern EU-VO 1008/2008 Art. 13; AOC bleibt beim Verleasenden.
5. Nationales Pfandrecht: Falls Deutschland als Registrierungsstaat Pfandrecht beim AG Braunschweig eintragen.
6. Insolvenzschutz: Aircraft Protocol Alternative A in Deutschland prüfen.

## Rechtsrahmen

- **Cape Town Convention Art. 2**: Internationale Sicherungsinteressen; Entstehung durch Vertrag und ICAO-Registrierung.
- **Cape Town Convention Art. 9**: Schutz des gesicherten Gläubigers; Remedies bei Default.
- **Aircraft Protocol Art. IV**: Dry-Lease-Gleichstellung; Recht des Registrierungsstaats auf IDERA.
- **Aircraft Protocol Art. XI**: Insolvenzschutz Alternative A/B.
- **EU-VO 1008/2008 Art. 13**: Wet-Lease innerhalb der EU; Genehmigungspflicht.
- **LuftVG § 21a**: Wet-Lease mit Drittlands-Carrier; Sondergenehmigung LBA.
- **LuftFzgG §§ 1-5**: Nationales Pfandrecht; Eintragung AG Braunschweig.

## Prüfraster

1. Welcher Leasingtyp liegt vor (Dry/Wet/Finance)?
2. Ist internationales Sicherungsinteresse im ICAO-Register eingetragen?
3. Ist IDERA korrekt hinterlegt?
4. Gilt EU-VO 1008/2008 Art. 13 für Wet-Lease?
5. Hat Deutschland Alternative A des Aircraft Protocols erklärt?
6. Ist Cape-Town-Eintrag zeitlich vor nationalem Pfandrecht?

## Typische Fallstricke

- IDERA nicht hinterlegt; Entregistrierungsrecht fehlt bei Vertragsbruch.
- Wet-Lease ohne LBA-Genehmigung; Betrieb illegal.
- Finance-Lease als Dry-Lease deklariert; steuerliche und rechtliche Konsequenzen.
- Aircraft-Protocol-Alternative ignoriert; Insolvenzschutz schwächer als erwartet.

## Output

Leasing-Sicherungsstrategie je Leasingtyp. Vertrags-Prüf-Checkliste Cape Town compliance. IDERA-Hinterlegungsablauf.

## Quellen

- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- ICAO Register: https://www.internationalregistry.aero
- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/

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

## 4. `luft-020-aviation-dashboard`

**Fokus:** Mandant braucht Echtzeit-Lageueberblick ueber eine Airline: Betriebsgenehmigung AOC Flotte Slots Sicherheitsstatus Insolvenzrisiko. Skill erstellt Dashboard-Matrix aus LBA-Register EU-VO 1008/2008 Art. 9 Indikatoren FluglaermG-Zonen und Cape-Town-Register und liefert einseitige Lagebewertung mit Ampel-Rating.

# Aviation Dashboard – Lageüberblick Airline und Flughafen

## Mandantenfall

- Rechtsanwalt übernimmt Airline-Mandat und braucht in 30 Minuten strukturierten Überblick über Genehmigungsstand Flottenregistrierung und Risiken.
- Investor prüft Beteiligung an Regionalairline; Due-Diligence-Dashboard als Entscheidungsgrundlage.
- Insolvenzverwalter muss nach Antragsstellung sofort Betriebsmittel (Flotte Slots AOC) erfassen.

## Erste Schritte

1. Grunddaten zusammenstellen: ICAO-Code IATA-Code Hauptgeschäftssitz Flottengröße bediente Strecken.
2. Genehmigungsstatus: Betriebsgenehmigung AOC-Status EU-VO 1008/2008 Art. 9 Überwachungsstatus.
3. Registercheck: Luftfahrzeugrolle LBA Pfandrechtsregister AG Braunschweig ICAO Cape-Town-Register.
4. Slot-Bestand: Fluko-Daten koordinierte Flughäfen Saison Nutzungsquote.
5. Sicherheitsstatus: LuftSiG-Sicherheitsprogramm aktuell aktuelle Findings.
6. Finanzlage: letzter Jahresabschluss Kreditratings Pressemitteilungen zu Liquidität.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung finanzielle Leistungsfähigkeit durch LBA.
- **LuftVG § 64**: Luftfahrzeugrolle; Eigentümer- und Halternachweis.
- **LuftFzgG §§ 1-5**: Pfandrechtsregister beim AG Braunschweig.
- **Cape Town Convention Art. 16**: ICAO-Register für internationale Sicherungsinteressen.
- **VO EWG 95/93 Art. 10**: Use-it-or-lose-it Slot-Quote.
- **LuftSiG §§ 8-9**: Sicherheitsprogramme.
## Prüfraster

1. Ist Betriebsgenehmigung aktuell?
2. Stimmen Flugzeuge in Rolle mit tatsächlicher Flotte überein?
3. Sind Pfandrechte und Cape-Town-Einträge konsistent?
4. Ist Slot-Bestand aktuell?
5. Gibt es LuftSiG-Findings?
6. Zeigen Finanzkennzahlen Insolvenzfrühzeichen?

## Typische Fallstricke

- Luftfahrzeugrolle veraltet; geleaste Flugzeuge unter fremdem Eintrag.
- Cape-Town-Register ignoriert; Sicherungsinteressen Dritter unerkannt.
- Slot-Verluste durch Use-it-or-lose-it nicht erfasst.
- Finanzdaten 18 Monate alt; Insolvenzrisiko unterschätzt.


## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Einseitige Lage-Matrix mit Ampel-Rating: Genehmigung/Flotte/Slots/Sicherheit/Finanzen. Offene-Punkte-Liste. Risiko-Kurzbewertung.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Luftfahrzeugrolle/luftfahrzeugrolle_node.html
- Cape Town Register: https://www.internationalregistry.aero
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-022-airline-register-auswerten`

**Fokus:** Mandant will Luftfahrzeugrolle Pfandrechtsregister und Cape-Town-Register einer Airline auswerten. Skill fuehrt strukturierte Registerabfrage LBA LuftVG § 64 AG Braunschweig LuftFzgG und ICAO-Register durch und liefert Registerauszugs-Auswertungs-Bericht mit Eigentuemerstruktur und Belastungen.

# Airline – Register auswerten

## Mandantenfall

- Finanzierer prüft vor Flugzeugfinanzierung ob auf der gesamten Flotte einer Airline Pfandrechte oder internationale Sicherungsinteressen lasten.
- Rechtsanwalt übernimmt Mandat nach Airline-Insolvenz; braucht vollständige Übersicht Flotte und Belastungen.
- Käufer will Airline erwerben; Due-Diligence verlangt vollständigen Registercheck.

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

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Vermerk zu Airline – Register auswerten mit Ampel-Rating Fristenstand und nächsten Schritten. Checkliste offener Punkte. Zuständigkeitsmatrix Behörde/Register. Fristenkalender mit Ampelstatus.
## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
