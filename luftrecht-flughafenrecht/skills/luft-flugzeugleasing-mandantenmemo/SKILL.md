---
name: luft-flugzeugleasing-mandantenmemo
description: "Luft Flugzeugleasing Mandantenmemo: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Flugzeugleasing Mandantenmemo

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Flugzeugleasing Mandantenmemo** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-050-flugzeugleasing-mandantenmemo-schreibe` | Anwalt schreibt Mandantenmemo fuer Leasinggeber oder Leasingnehmer zu komplexem Flugzeugleasing-Fall: IDERA-Entregistrierung Insolvenz Cape-Town-Remedies oder Wet-Lease-Genehmigung. Skill strukturiert Memo mit Sachverhalt Rechtslage Handlungsoptionen und Empfehlung. |
| `luft-052-registerpfandrecht-register-auswerten` | Mandant will Pfandrechtsregister AG Braunschweig und ICAO-Cape-Town-Register auswerten. Prueft LuftFzgG §§ 1-12 AG-Braunschweig-Registerauszug Cape-Town-Convention Art. 16 ICAO-Registerabfrage und liefert Ranganalyse-Bericht mit allen eingetragenen Belastungen. |
| `luft-053-registerpfandrecht-pfandrecht-vorberei` | Glaeubigerbank will Pfandrecht an Luftfahrzeug bestellen und gleichzeitig Cape-Town-Sicherungsinteresse eintragen. Prueft LuftFzgG §§ 1-12 Notarerfordernis Rangordnung AG-Braunschweig-Antrag Cape-Town-Prioritaet und liefert Bestellungs-Checkliste und Antragsentwurf. |
| `luft-054-registerpfandrecht-pfaendung-planen` | Pfandglaeubiger will aus eingetragenem Pfandrecht vollstrecken oder Neuglaeubigers will Pfandrecht pfaenden. Prueft LuftFzgG §§ 22-28 Zwangsversteigerungsrecht ZPO §§ 864-871 Cape-Town-Remedies Art. 8 InsO § 50 Absonderungsrecht und liefert Vollstreckungs-Plan. |
| `luft-055-registerpfandrecht-genehmigung-pruefen` | Pfandrecht an Luftfahrzeug soll bestellt werden; Prüfung ob Genehmigungen der Luftfahrtbehörde nötig sind. Prueft LuftFzgG LuftVG § 64 Cape-Town-Voraussetzungen und liefert Genehmigungs-Checkliste fuer Pfandrechtsbestellung an Luftfahrzeugen. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Flugzeugleasing Mandantenmemo**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-050-flugzeugleasing-mandantenmemo-schreibe`

**Fokus:** Anwalt schreibt Mandantenmemo fuer Leasinggeber oder Leasingnehmer zu komplexem Flugzeugleasing-Fall: IDERA-Entregistrierung Insolvenz Cape-Town-Remedies oder Wet-Lease-Genehmigung. Skill strukturiert Memo mit Sachverhalt Rechtslage Handlungsoptionen und Empfehlung.

# Flugzeugleasing – Mandantenmemo schreiben

## Mandantenfall

- Leasinggeber-Vorstand braucht Memo nach Insolvenzantrag des Leasingnehmers; IDERA hinterlegt; Alternative A unklar.
- Leasingnehmer erhält Kündigung des Leasingvertrags; Memo über Rechtslage und Abwehrmöglichkeiten.
- Refinanzierungsbank fragt nach Auswirkungen eines Leasingnehmer-Defaults auf Sicherheiten-Struktur.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: Cape Town Convention InsO EU-VO 1008/2008 LuftFzgG.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

Cape Town Convention InsO EU-VO 1008/2008 LuftFzgG – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Output

Vollständiger Mandanten-Memo-Baustein (1-3 Seiten). Executive Summary. Nächste-Schritte-Tabelle. Cape-Town-Registrierungs-Checkliste. Aussonderungsvermerk bei Insolvenz.
## Quellen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- InsO: https://www.gesetze-im-internet.de/inso/
- ICAO International Registry: https://www.internationalregistry.aero

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Flugzeug-Leasing und Cape Town Convention ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Flugzeug-Leasing und Cape Town Convention sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-052-registerpfandrecht-register-auswerten`

**Fokus:** Mandant will Pfandrechtsregister AG Braunschweig und ICAO-Cape-Town-Register auswerten. Prueft LuftFzgG §§ 1-12 AG-Braunschweig-Registerauszug Cape-Town-Convention Art. 16 ICAO-Registerabfrage und liefert Ranganalyse-Bericht mit allen eingetragenen Belastungen.

# Registerpfandrecht – Register auswerten

## Mandantenfall

- Finanzierer prüft vor Kreditvergabe ob auf Flugzeug Vorbelastungen aus nationalen und internationalen Registern bestehen.
- Käufer will Flugzeug kaufen; vollständige Belastungsfreiheit muss vor Kaufpreis-Zahlung festgestellt werden.
- Insolvenzverwalter braucht Übersicht aller Pfandgläubiger für Gläubigerversammlung.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG §§ 1-12 Cape Town Convention Art. 16 29 AG Braunschweig ICAO-Register.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG §§ 1-12 Cape Town Convention Art. 16 29 AG Braunschweig ICAO-Register – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

Strukturierter Vermerk zu Registerpfandrecht – Register auswerten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
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

## 3. `luft-053-registerpfandrecht-pfandrecht-vorberei`

**Fokus:** Glaeubigerbank will Pfandrecht an Luftfahrzeug bestellen und gleichzeitig Cape-Town-Sicherungsinteresse eintragen. Prueft LuftFzgG §§ 1-12 Notarerfordernis Rangordnung AG-Braunschweig-Antrag Cape-Town-Prioritaet und liefert Bestellungs-Checkliste und Antragsentwurf.

# Registerpfandrecht – Pfandrecht vorbereiten

## Mandantenfall

- Bank gibt Kredit für Flugzeugkauf; erstrangiges Pfandrecht im AG Braunschweig und Cape-Town-Eintrag gleichzeitig nötig.
- Zweiter Gläubiger tritt bei; nachrangiges Pfandrecht muss mit erstem Gläubiger koordiniert werden.
- Auslands-Pfandrecht soll in deutschen Register überführt werden; alte Eintragung zu löschen.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG §§ 1-12 Cape Town Convention Art. 16 19 29 AG Braunschweig Notar ZPO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG §§ 1-12 Cape Town Convention Art. 16 19 29 AG Braunschweig Notar ZPO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

Strukturierter Vermerk zu Registerpfandrecht – Pfandrecht vorbereiten mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
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

## 4. `luft-054-registerpfandrecht-pfaendung-planen`

**Fokus:** Pfandglaeubiger will aus eingetragenem Pfandrecht vollstrecken oder Neuglaeubigers will Pfandrecht pfaenden. Prueft LuftFzgG §§ 22-28 Zwangsversteigerungsrecht ZPO §§ 864-871 Cape-Town-Remedies Art. 8 InsO § 50 Absonderungsrecht und liefert Vollstreckungs-Plan.

# Registerpfandrecht – Pfändung planen

## Mandantenfall

- Pfandgläubiger hat vollstreckbaren Titel; will aus eingetragenem Pfandrecht vorgehen; Flugzeug steht auf Frankfurter Flughafen.
- Neuglaeubiger versucht Pfändung in Luftfahrzeug auf das bereits Pfandrecht eingetragen ist; Rang-Konflikt.
- Insolvenz: Pfandgläubiger will Absonderungsrecht geltend machen; Insolvenzverwalter verweigert Herausgabe.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG §§ 22-28 ZPO §§ 864-871 Cape Town Convention Art. 8-10 InsO §§ 50 89.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG §§ 22-28 ZPO §§ 864-871 Cape Town Convention Art. 8-10 InsO §§ 50 89 – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

Strukturierter Vermerk zu Registerpfandrecht – Pfändung planen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
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

## 5. `luft-055-registerpfandrecht-genehmigung-pruefen`

**Fokus:** Pfandrecht an Luftfahrzeug soll bestellt werden; Prüfung ob Genehmigungen der Luftfahrtbehörde nötig sind. Prueft LuftFzgG LuftVG § 64 Cape-Town-Voraussetzungen und liefert Genehmigungs-Checkliste fuer Pfandrechtsbestellung an Luftfahrzeugen.

# Registerpfandrecht – Genehmigung prüfen

## Mandantenfall

- Bank fragt ob Betriebsgenehmigung der Airline Voraussetzung für Pfandrechtsbestellung ist.
- Ausländischer Gläubiger fragt ob er in Deutschland ein Pfandrecht an deutschem Flugzeug bestellen darf.
- Pfandrechtsbestellung geplant; Frage ob LBA-Genehmigung oder Notar ausreichend.

## Erste Schritte

1. Sachverhalt strukturieren: Parteien betroffene Luftfahrzeuge/Einrichtungen beteiligte Behörden und laufende Fristen.
2. Einschlägige Normen identifizieren: LuftFzgG §§ 1-5 LuftVG § 64 Cape Town Convention Art. 19 Notar GBO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Cape-Town-Register je nach Fallrelevanz.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. EASA vs. Verwaltungsgericht.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Handlungsbedarf dokumentieren: Ampel-Vermerk mit konkreten nächsten Schritten.

## Rechtsrahmen

LuftFzgG §§ 1-5 LuftVG § 64 Cape Town Convention Art. 19 Notar GBO – die einschlägigen Normen werden je nach Sachverhaltsebene (nationaler Betrieb EU-Recht internationales Recht) herangezogen und zu jedem Normzitat kurz erläutert.

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

Strukturierter Vermerk zu Registerpfandrecht – Genehmigung prüfen mit Rechtslage Handlungsoptionen Risikobewertung und nächsten Schritten. Checkliste offener Punkte mit Fristen. Registerauszug-Analyse mit Rangfolge. Vollstreckungsfahrplan.
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
