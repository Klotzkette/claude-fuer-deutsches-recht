---
name: luft-flughafen-dashboard-mandantenmemo
description: "Luft Flughafen Dashboard Mandantenmemo: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Flughafen Dashboard Mandantenmemo

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Flughafen Dashboard Mandantenmemo** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-039-flughafen-dashboard-bauen` | Kanzlei oder Mandant braucht Dashboard fuer Flughafen-Mandat: Genehmigungsstatus LuftSiG-Findings Passagierzahlen Finanzlage Grundbuch. Skill strukturiert Datenquellen LuftVG-Genehmigungsregister LuftSiG Grundbuch Fluko und liefert befuellbares Dashboard-Template. |
| `luft-040-flughafen-mandantenmemo-schreiben` | Anwalt schreibt Mandantenmemo fuer Flughafen-Betreiber oder Investor zu komplexem Luftrechtsfall: Planfeststellungsklage Sicherheitsauflage Insolvenznaehe oder Entgeltstreit. Skill strukturiert Memo nach Sachverhalt Rechtslage Handlungsoptionen Risikobewertung und Empfehlung. |
| `luft-042-flugzeugleasing-register-auswerten` | Mandant will Register zu einem geleasten Flugzeug auswerten: Luftfahrzeugrolle Cape-Town-ICAO-Register Pfandrechtsregister AG Braunschweig und IDERA-Status. Prueft LuftVG § 64 LuftFzgG Cape-Town-Art. 16 und liefert Registerauszugs-Auswertung mit vollstaendiger Belastungsanalyse. |
| `luft-043-flugzeugleasing-pfandrecht-vorbereiten` | Leasinggeber will internationales Sicherungsinteresse Cape-Town und nationales Pfandrecht an geleasetem Flugzeug koordinieren. Prueft Cape-Town-Convention Art. 2 ICAO-Register-Eintragung LuftFzgG §§ 1-12 AG-Braunschweig und IDERA-Bestellung und liefert Sicherungsstruktur-Vermerk. |
| `luft-044-flugzeugleasing-pfaendung-planen` | Leasinggeber will nach Zahlungsausfall das Flugzeug zuruecknehmen oder Glaeubiger will in geleaste Flugzeuge vollstrecken. Prueft Cape-Town-Convention Art. 8-10 Remedies IDERA LuftFzgG ZPO-Vollstreckungsrecht und InsO § 89 Vollstreckungssperre und liefert Ruecknahme-Strategie. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Flughafen Dashboard Mandantenmemo**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-039-flughafen-dashboard-bauen`

**Fokus:** Kanzlei oder Mandant braucht Dashboard fuer Flughafen-Mandat: Genehmigungsstatus LuftSiG-Findings Passagierzahlen Finanzlage Grundbuch. Skill strukturiert Datenquellen LuftVG-Genehmigungsregister LuftSiG Grundbuch Fluko und liefert befuellbares Dashboard-Template.

# Flughafen – Dashboard bauen

## Mandantenfall

- Kanzlei betreut Flughafenbetreiber dauerhaft; Dashboard soll alle mandatsrelevanten Daten bündeln.
- Investoren-Konsortium führt Due Diligence durch; Dashboard für strukturierte Datenzusammenführung.
- Insolvenzverwalter hat Flughafen übernommen; sofortiger Überblick über Betrieb und Verbindlichkeiten nötig.

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

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Output

Vermerk zu Flughafen – Dashboard bauen mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-040-flughafen-mandantenmemo-schreiben`

**Fokus:** Anwalt schreibt Mandantenmemo fuer Flughafen-Betreiber oder Investor zu komplexem Luftrechtsfall: Planfeststellungsklage Sicherheitsauflage Insolvenznaehe oder Entgeltstreit. Skill strukturiert Memo nach Sachverhalt Rechtslage Handlungsoptionen Risikobewertung und Empfehlung.

# Flughafen – Mandantenmemo schreiben

## Mandantenfall

- Flughafen-Vorstand braucht Memo nach Klageandrohung einer Anwohner-Initiative gegen Nachtflugbetrieb.
- Gesellschafter-Meeting zum Insolvenzrisiko; Memo über Rechtslage Haftung und Optionen.
- EASA-Audit-Ergebnis muss binnen 48 Stunden an Aufsichtsbehörde kommuniziert werden.

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

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Output

Vermerk zu Flughafen – Mandantenmemo schreiben mit Rechtslagenanalyse Handlungsoptionen und Fristen. Planfeststellungs-Checkliste. Lärmschutzbereichs-Karte als Anhang.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- FluglärmG: https://www.gesetze-im-internet.de/fluglaermg/
- UVPG: https://www.gesetze-im-internet.de/uvpg/
- BVerwG Planfeststellung: https://www.bverwg.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flughafenbetrieb und Planfeststellung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Flughafenbetrieb und Planfeststellung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-042-flugzeugleasing-register-auswerten`

**Fokus:** Mandant will Register zu einem geleasten Flugzeug auswerten: Luftfahrzeugrolle Cape-Town-ICAO-Register Pfandrechtsregister AG Braunschweig und IDERA-Status. Prueft LuftVG § 64 LuftFzgG Cape-Town-Art. 16 und liefert Registerauszugs-Auswertung mit vollstaendiger Belastungsanalyse.

# Flugzeugleasing – Register auswerten

## Mandantenfall

- Leasinggeber prüft vor Vertragsabschluss ob Flugzeug belastungsfrei und korrekt im ICAO-Register eingetragen ist.
- Leasingnehmer will nach Insolvenz des Leasinggebers prüfen ob Belastungen den Weiterbetrieb gefährden.
- Käufer will Flugzeug aus Leasing-Pool erwerben; Registerprüfung vor Kaufvertrag.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftVG § 64 LuftFzgG Cape Town Convention Art. 16 ICAO-Register.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftVG § 64 LuftFzgG Cape Town Convention Art. 16 ICAO-Register – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Output

Registerauszugs-Auswertungs-Bericht je Flugzeug (Tabelle). Inkonsistenz-Markierungsliste. IDERA-Status-Vermerk. Cape-Town-Registrierungs-Checkliste. Aussonderungsvermerk bei Insolvenz.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- ICAO International Registry: https://www.internationalregistry.aero

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flugzeug-Leasing und Cape Town Convention ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Flugzeug-Leasing und Cape Town Convention sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-043-flugzeugleasing-pfandrecht-vorbereiten`

**Fokus:** Leasinggeber will internationales Sicherungsinteresse Cape-Town und nationales Pfandrecht an geleasetem Flugzeug koordinieren. Prueft Cape-Town-Convention Art. 2 ICAO-Register-Eintragung LuftFzgG §§ 1-12 AG-Braunschweig und IDERA-Bestellung und liefert Sicherungsstruktur-Vermerk.

# Flugzeugleasing – Pfandrecht vorbereiten

## Mandantenfall

- Leasinggesellschaft will erstmalig internationales Sicherungsinteresse für neue Flugzeugflotte im ICAO-Register eintragen.
- Refinanzierung einer Leasingflotte erfordert Umstrukturierung der Sicherheiten; altes Pfandrecht zu löschen.
- Leasingnehmer will Sublease eingehen; Leasinggeber muss Sicherheiten-Struktur anpassen.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: Cape Town Convention Art. 2 ICAO-Register LuftFzgG §§ 1-12 AG Braunschweig.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen). IDERA bestellen: notarielle Erklärung des Luftfahrzeugeigentümers; beim ICAO-Register hinterlegen.
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

Cape Town Convention Art. 2 ICAO-Register LuftFzgG §§ 1-12 AG Braunschweig – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Output

Sicherungsstruktur-Vermerk. IDERA-Hinterlegungs-Ablauf. Pfandrechts-Bestellungs-Checkliste. Cape-Town-Registrierungs-Checkliste. Aussonderungsvermerk bei Insolvenz.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- ICAO International Registry: https://www.internationalregistry.aero

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flugzeug-Leasing und Cape Town Convention ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Flugzeug-Leasing und Cape Town Convention sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-044-flugzeugleasing-pfaendung-planen`

**Fokus:** Leasinggeber will nach Zahlungsausfall das Flugzeug zuruecknehmen oder Glaeubiger will in geleaste Flugzeuge vollstrecken. Prueft Cape-Town-Convention Art. 8-10 Remedies IDERA LuftFzgG ZPO-Vollstreckungsrecht und InsO § 89 Vollstreckungssperre und liefert Ruecknahme-Strategie.

# Flugzeugleasing – Pfändung planen

## Mandantenfall

- Leasinggeber will nach ausstehenden Raten Flugzeug zurücknehmen; IDERA hinterlegt; Leasingnehmer verweigert Herausgabe.
- Pfandgläubiger will in geleaste Flugzeuge vollstrecken; Eigentümer (Leasinggeber) hat vorrangige Rechte.
- Insolvenz des Leasingnehmers: Insolvenzverwalter will Leasingvertrag fortführen; Leasinggeber will Herausgabe.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: Cape Town Convention Art. 8-10 Aircraft Protocol Art. IX IDERA LuftFzgG ZPO InsO §§ 47 89.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

Cape Town Convention Art. 8-10 Aircraft Protocol Art. IX IDERA LuftFzgG ZPO InsO §§ 47 89 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Output

Rücknahme-Strategie-Vermerk. IDERA-Entregistrierungsablauf. Insolvenz-Reaktions-Checkliste. Cape-Town-Registrierungs-Checkliste. Aussonderungsvermerk bei Insolvenz.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- ICAO International Registry: https://www.internationalregistry.aero

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flugzeug-Leasing und Cape Town Convention ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Flugzeug-Leasing und Cape Town Convention sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
