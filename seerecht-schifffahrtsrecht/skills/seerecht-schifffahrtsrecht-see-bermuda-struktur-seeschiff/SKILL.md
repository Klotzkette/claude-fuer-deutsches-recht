---
name: seerecht-schifffahrtsrecht-see-bermuda-struktur-seeschiff
description: "SEE Bermuda Struktur Seeschiff: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Bermuda Struktur Seeschiff

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Bermuda Struktur Seeschiff** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-013-bermuda-struktur-pruefen` | Reederei nutzt Bermuda-Holding-Struktur (SPV; Cayman/BVI-Holding): steuerliche und haftungsrechtliche Analyse. Abgrenzung Reeder vs. Ausruester (HGB §§ 476/477); Durchgriffshaftung; BEPS-Konformitaet (AStG §§ 7-14); BFH-Rechtsprechung; ISM-Code-Verantwortung. Output: Strukturanalyse-Vermerk und Haftungsrisiko-Karte. |
| `see-002-seeschiff-oder-binnenschiff` | Mandant klaert ob sein Fahrzeug Seeschiff oder Binnenschiff ist: entscheidend fuer Register; Hypothekenrecht und Haftungsregime. Abgrenzung nach HGB § 476 (Seegewaesser) vs. BinSchG § 1 (Binnengewaesser); SchRegO § 3 (Seeschiffsregister) vs. BinSchRegO (Binnenschiffsregister). BSH-Fahrterlaubnis; Klasseregime. Output: Klassifizierungsvermerk mit Normpfad und Folgeregime. |
| `see-003-schiffsregister-und-eigentum` | Mandant kauft Schiff und klaert Eigentumslage: Pruefung des Schiffsregisters auf Hypotheken; Vormerkungen; Arreste nach SchRG §§ 8-74 und SchRegO §§ 3-19. Eigentumsuebergang (SchRG § 2 Eintragungsprinzip); Rangfolge; Loeschungsvoraussetzungen. Output: Registerpruefprotokoll und Due-Diligence-Vermerk fuer Schiffskauf. |
| `see-004-schiffshypothek-pruefen` | Mandant (Bank oder Kaeufer) prueft bestehende Schiffshypothek: Valutierung; Rang; Sicherungsvertrag nach SchRG §§ 8-74. Hoechstbetragshypothek (SchRG § 75); Sicherungsabrede; Mithaftung Zubehoer (SchRG § 31); Kreditkuendigungsvoraussetzungen. Schiffsglaeubigerrecht-Vorrang (HGB §§ 596-601). Output: Hypothekenpruefvermerk und Freigabestrategie. |
| `see-006-schiffsverkauf-closing` | Mandant schliesst Schiffsveraeusserung ab: MOA (Norwegian Saleform/Nipponsale) prufen; Closing-Bedingungen; Eigentumsuebergang (SchRG § 2); Flaggenwechsel; Loeschung alter Hypotheken (SchRG § 19); P&I-Abrechnung; Zertifikats-Ummeldung. FlaggRG §§ 3-5. Output: Closing-Checkliste und Uebergabe-Protokoll. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Bermuda Struktur Seeschiff**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-013-bermuda-struktur-pruefen`

**Fokus:** Reederei nutzt Bermuda-Holding-Struktur (SPV; Cayman/BVI-Holding): steuerliche und haftungsrechtliche Analyse. Abgrenzung Reeder vs. Ausruester (HGB §§ 476/477); Durchgriffshaftung; BEPS-Konformitaet (AStG §§ 7-14); BFH-Rechtsprechung; ISM-Code-Verantwortung. Output: Strukturanalyse-Vermerk und Haftungsrisiko-Karte.

# Bermuda-Struktur prüfen – Holding-Struktur und Haftungsrisiken

## Mandantenfall
Ein Schiffsfonds hält seine Schiffe über Cayman-SPVs; nach einem Totalverlust fragt der Insolvenzverwalter wer wirklich Reeder und haftbar ist. Eine Bank finanziert ein Schiff das einer BVI-Gesellschaft gehört; der Reeder operiert aus Deutschland. Die Steuerbehörde prüft ob die Bermuda-Struktur BEPS-konform ist.

## Erste Schritte
1. Gesellschafts-Kaskade aufzeichnen: Eigentümer (BVI/Cayman-SPV); Reeder (HGB § 476); Ausrüster (HGB § 477).
2. Substanzprüfung der Offshore-Einheiten: Sitz; Mitarbeiter; Geschäftsführung; BEPS Action 6/13 Anforderungen.
3. ISM-Code-Verantwortung klären: ISM § 1.1.2 – Unternehmen = wer betriebliche Kontrolle hat; nicht zwingend Registereigentümer.
4. Steuerliche Analyse: AStG §§ 7-14 Hinzurechnungsbesteuerung; § 49 EStG; § 8b KStG.
5. Durchgriffshaftungsrisiko bewerten: Konzernhaftung nur in Ausnahmefällen; UNCLOS Art. 94 kann wirtschaftlichen Eigentümer identifizieren.
6. Restrukturierungsoptionen aufzeigen: BEPS-konforme Substanzschaffung.

## Rechtsrahmen
- HGB § 476: Reeder = Betreiber auf eigene Rechnung; auch Offshore-Eigentümer kann Reeder sein.
- HGB § 477: Ausrüster = wer fremdes Schiff auf eigene Rechnung betreibt; haftet wie Reeder.
- AStG §§ 7-14: Hinzurechnungsbesteuerung für passive Offshore-Einkünfte.
- KStG § 8 Abs. 2: Ort der Geschäftsleitung als Anknüpfungspunkt.
- UNCLOS Art. 94: Flaggenstaat verpflichtet zur Kontrolle; darf nicht an formale Eigentumsstruktur anknüpfen.
- ISM-Code Kap. 1.1.2: Unternehmensdefinition; betriebliche Kontrolle entscheidend.

## Prüfraster
- Hat jede Gesellschaft in der Kaskade echte wirtschaftliche Substanz?
- Ist klar wer ISM-Code-Unternehmen ist?
- Greift die Hinzurechnungsbesteuerung (AStG § 7) für Schifffahrtseinkünfte?
- Gibt es Haftungsdurchgriff auf die Holding-Ebene?
- Sind alle Gesellschaften im UBO-Register offengelegt?

## Typische Fallstricke
- Irrige Annahme der Offshore-SPV isoliere vollständig von Haftungsrisiken.
- Fehlende Substanz der Bermuda-Gesellschaft; BFH bejaht Hinzurechnung.
- ISM-DOC ausgestellt auf Managementfirma aber wirtschaftlicher Betreiber ist anders.
- KYC/AML-Anforderungen verlangen zunehmend UBO-Transparenz.

## Output
- Strukturanalyse-Vermerk: Gesellschaftskaskade; Haftungsfluss; Steuerrisiken
- Haftungsrisiko-Karte
- Restrukturierungs-Empfehlung


## Erweiterte Normengrundlage

### Gesellschaftsrecht
- BGB §§ 705-740: Gesellschaft bürgerlichen Rechts; Grundstruktur von SPV-Strukturen.
- GmbHG §§ 1-88: GmbH als Einschiffgesellschaft; Haftungsbegrenzung.
- Companies Act 1981 (Bermuda): Bermuda-Gesellschaftsrecht; Exempted Companies.

### Steuerrecht
- AO §§ 12-13: Betriebsstätte; Beschränkte Steuerpflicht.
- UmwStG: Einbringung in Kapitalgesellschaft; Entstrickungsbesteuerung.
- DBA Deutschland-Bermuda: kein vollständiges DBA; Anwendung nationalen Steuerrechts.

## Checkliste Bermuda-Struktur
- [ ] Gesellschaftsstruktur vollständig aufgenommen (Organogramm)
- [ ] Beneficial Owner identifiziert; UBO-Transparenz geprüft (GwG)
- [ ] Steuerliche Ansässigkeit jeder Gesellschaft bestimmt
- [ ] Substanz-Anforderungen der Bermuda-Gesellschaft geprüft
- [ ] Bankkonten und Cash-Flow-Struktur aufgenommen
- [ ] Compliance mit FATF/FATCA/CRS dokumentiert

## Relevante Rechtsprechung
- BGH zur Durchgriffshaftung bei Einschiff-SPV-Strukturen; Unterkapitalisierung.
- BFH zur Besteuerung von Bermuda-Schiffen; beschränkte Steuerpflicht inländischer Einkünfte.
- BVerwG zum Geldwäschegesetz; Transparenzregister-Pflicht für Schiffs-SPV.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB §§ 476/477: https://dejure.org/gesetze/HGB/476.html
- AStG §§ 7-14: https://www.gesetze-im-internet.de/astg/__7.html
- UNCLOS Art. 94: https://www.un.org/Depts/los/convention_agreements/texts/unclos/unclos_e.pdf
- ISM-Code: https://www.bsh.de/DE/THEMEN/Schifffahrt/ISM_Code/ism_code_node.html
- BFH: https://www.bfh.de

## 2. `see-002-seeschiff-oder-binnenschiff`

**Fokus:** Mandant klaert ob sein Fahrzeug Seeschiff oder Binnenschiff ist: entscheidend fuer Register; Hypothekenrecht und Haftungsregime. Abgrenzung nach HGB § 476 (Seegewaesser) vs. BinSchG § 1 (Binnengewaesser); SchRegO § 3 (Seeschiffsregister) vs. BinSchRegO (Binnenschiffsregister). BSH-Fahrterlaubnis; Klasseregime. Output: Klassifizierungsvermerk mit Normpfad und Folgeregime.

# Seeschiff oder Binnenschiff – Klassifizierungsprüfung

## Mandantenfall
Ein Reeder betreibt eine Fähre zwischen Rügen und dem Festland und fragt, ob sie im Seeschiffs- oder Binnenschiffsregister einzutragen ist. Eine Bank fragt, ob ein auf dem Rhein eingesetzter seetüchtiger Frachter als Seeschiffshypothek oder Binnenschiffshypothek zu besichern ist. Ein Charterer fragt, welches Haftungsregime für eine Küstenfahrt in der Nordsee gilt.

## Erste Schritte
1. Fahrtbereich ermitteln: ausschließlich Binnengewässer (BinSchG § 1) oder Seegewässer (HGB § 476) oder gemischt?
2. Registerstatus prüfen: Eintragung im Seeschiffsregister (SchRegO § 3) oder Binnenschiffsregister (BinSchRegO §§ 1-4).
3. Seetüchtigkeitsklasse der Klassifikationsgesellschaft auswerten: Klasse A/B/C/D für Fahrtgebiete.
4. BSH-Fahrterlaubnis prüfen: nur Seeschiffe benötigen BSH-Flaggenzertifikat und SafeSeaNet-Meldepflicht.
5. Haftungsregime ableiten: HGB §§ 476 ff. für Seeschiff; BinSchG §§ 1-6 für Binnenschiff.
6. Klassifizierungsvermerk erstellen und an Registerbehörde übermitteln.

## Rechtsrahmen
- HGB § 476: Reeder = Person die Schiff auf eigene Rechnung zur Seefahrt betreibt; Seegewässer als Abgrenzungsmerkmal.
- BinSchG § 1 Abs. 1: Schiffseigner = Betreiber auf Binnengewässern; eigenes Haftungsregime.
- SchRegO §§ 3-5: Seeschiffsregister-Zuständigkeit bei Registergerichten Hamburg; Bremen; Lübeck; Rostock; Emden.
- BinSchRegO §§ 1-4: Binnenschiffsregister beim AG Duisburg-Ruhrort und regionalen Gerichten.
- SchRG §§ 1-7: nur eingetragene Schiffe können Schiffshypothek nach SchRG tragen.
- FlaggRG §§ 1-3: Flaggenführungsrecht für Seeschiffe unter deutschem Recht.
- BinSchG §§ 92-101: Bergung auf Binnengewässern; abweichend von HGB §§ 574 ff. Seebergung.

## Prüfraster
- Liegt ein Eintragungsantrag im See- oder Binnenschiffsregister vor?
- Welchen Fahrtbereich deckt das BSH-Zertifikat ab?
- Ist die Hypothekenurkunde als Seeschiffshypothek oder Binnenhypothek qualifiziert?
- Welcher Versicherungsvertrag liegt vor: See-P&I oder Binnenschiffs-Haftpflicht?
- Gelten SOLAS/ISM-Code oder BinSchUO als Sicherheitsstandard?

## Typische Fallstricke
- Wattenmeer und Bodden sind trotz Küstennähe Seegewässer; BinSchG greift nicht.
- Im Binnenschiffsregister eingetragenes Schiff kann keine Seeschiffshypothek nach SchRG erwerben.
- Fehlerhafte Registrierung führt zu Nichtigkeit der Hypothek.
- Haftungsgrenzen (HGB §§ 611-617 vs. BinSchG §§ 92 ff.) weichen erheblich voneinander ab.

## Output
- Klassifizierungsvermerk mit Normpfad
- Empfehlung Register-/Hypothekenweg
- Checkliste Registereintragung


## Erweiterte Normengrundlage

### Abgrenzungsnormen
- BinSchG § 1: Definition Binnenschiff; Abgrenzung zu Seeschiffen; maßgebliche Fahrtroute.
- FlaggRG § 1: Seeschiff im Sinne des FlaggRG; internationale Fahrt als Merkmal.
- UNCLOS Art. 8-12: Basislinie; innere Gewässer; Küstenmeer; Abgrenzung für Rechtsanwendung.

### Konsequenzen der Einordnung
- BinSchG §§ 77-119: Haftungsrecht für Binnenschiffe; Unterschiede zu HGB §§ 611-617.
- HGB § 476: Anwendungsbereich des Seehandelsrechts; nur bei Fahrt auf See.
- SeeArbG § 3: Seearbeitsrecht gilt für Seeschiffe; ArbZG gilt für Binnenschiffe.

## Checkliste Schiffseinordnung
- [ ] Fahrtgebiet aus letzten 12 Monaten ermittelt; überwiegende Nutzung Binnen oder See
- [ ] Schiffszeugnis (Binnenschiff) oder Klassenzertifikat (Seeschiff) vorliegend
- [ ] Registerart bestimmt: Schiffsregister (See) vs. Binnenschiffsregister
- [ ] Anwendbares Seearbeitsrecht geprüft: SeeArbG vs. ArbZG
- [ ] Flagge / Nationalitätspapiere angepasst an Fahrtgebiet

## Relevante Rechtsprechung
- BGH zur Abgrenzung Seeschiff/Binnenschiff bei gemischter Fahrt; maßgeblich ist geplante Nutzung.
- OLG Karlsruhe zur Haftungsdivergenz zwischen BinSchG und HGB bei Grenzgewässern.
- BVerwG zur Zuständigkeit von BSH vs. Wasserstraßen- und Schifffahrtsamt.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB § 476: https://www.gesetze-im-internet.de/hgb/__476.html
- BinSchG: https://www.gesetze-im-internet.de/binschprg/
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- dejure SchRegO: https://dejure.org/gesetze/SchRegO

## 3. `see-003-schiffsregister-und-eigentum`

**Fokus:** Mandant kauft Schiff und klaert Eigentumslage: Pruefung des Schiffsregisters auf Hypotheken; Vormerkungen; Arreste nach SchRG §§ 8-74 und SchRegO §§ 3-19. Eigentumsuebergang (SchRG § 2 Eintragungsprinzip); Rangfolge; Loeschungsvoraussetzungen. Output: Registerpruefprotokoll und Due-Diligence-Vermerk fuer Schiffskauf.

# Schiffsregister und Eigentum – Due-Diligence-Prüfung

## Mandantenfall
Eine Investmentgesellschaft kauft einen gebrauchten Containerfrachter und benötigt Gewissheit über lastenfreies Eigentum vor Kaufpreiszahlung. Eine Bank prüft, ob ihr Grundpfandrecht an einem Schiff erstrangig eingetragen ist. Ein Insolvenzverwalter stellt fest, welche Schiffe der Insolvenzmasse gehören und welche Belastungen darauf ruhen.

## Erste Schritte
1. Registerauszug beim zuständigen Registergericht anfordern: Hamburg; Bremen; Lübeck; Rostock; Emden oder Duisburg-Ruhrort für Binnenschiffe.
2. Abteilung I (Eigentumsrecht): Eingetragener Eigentümer; Eigentümerwechsel; Eigentümer-Vormerkungen.
3. Abteilung II (Lasten): Schiffshypotheken nach SchRG §§ 8-74; Pfändungsvermerke; Arreste; Nießbrauch.
4. Gesetzliche Schiffsgläubigerrechte (HGB §§ 596-601) ermitteln; gehen Hypotheken vor.
5. Eigentumsübergang: SchRG § 2 – Einigung und Eintragung nötig; bloßer Kaufvertrag überträgt kein Eigentum.
6. Löschungsvoraussetzungen für Altlasten ermitteln: Löschungsbewilligung oder Gerichtsbeschluss nötig.

## Rechtsrahmen
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; Konstitutivprinzip.
- SchRG §§ 8-74: Schiffshypothek; Entstehung; Rang; Übertragung; Erlöschen.
- HGB §§ 596-601: gesetzliche Schiffsgläubiger mit Vorrang vor Hypotheken.
- SchRegO §§ 3-19: Registerführung; Zuständigkeit; Eintragungsverfahren.
- BGB §§ 892-893: Gutglaubensschutz im Register; gilt analog für Schiffsregister.
- ZPO §§ 864-871: Zwangsvollstreckung in eingetragene Schiffe.

## Prüfraster
- Stimmt eingetragener Eigentümer mit dem Veräußerer im Kaufvertrag überein?
- Welche Hypotheken lasten auf dem Schiff: Betrag; Rang; Fälligkeit; Gläubiger?
- Sind gesetzliche Schiffsgläubigerrechte (HGB §§ 596 ff.) entstanden?
- Bestehen Pfändungs- oder Arrestvermerke, die den Eigentumsübergang gefährden?
- Sind alle Löschungsbewilligungen der Hypothekengläubiger vorhanden?

## Typische Fallstricke
- Gesetzliche Schiffsgläubigerrechte (HGB § 597: Kapitäns-/Besatzungslöhne; Hafengebühren; Bergungskosten) entstehen ohne Registereintragung und gehen Hypotheken vor.
- Eigentumsübertragung setzt Voreintragung des Verkäufers voraus.
- Auslandshypotheken bei Bare-Boat-Registrierung können parallel existieren.
- Arreste kurz vor Closing können den Eigentumsübergang verzögern.

## Output
- Registerprüfprotokoll (Abteilungen I/II/III)
- Due-Diligence-Vermerk: Eigentumsklarheit; Lasten; offene Fragen
- Checkliste Löschungsvoraussetzungen


## Erweiterte Normengrundlage

### Registerrecht
- SchRegO §§ 8-30: Eintragungsverfahren; Antragsteller; Unterlagen; Fristen; Eintragungswirkung.
- SchRegO §§ 31-50: Änderungen; Löschungen; Berichtigungen im Schiffsregister.
- SchRG § 3: Eigentumsvermutung durch Eintragung; gutgläubiger Erwerb.

### Eigentumsübergang
- SchRG § 2: Übereignung eines eingetragenen Seeschiffes durch Einigung und Eintragung.
- BGB § 929 ff.: Grundsatz Übereignung beweglicher Sachen; verdrängt durch SchRG § 2 für eingetragene Schiffe.
- SchRG §§ 60-68: Wirkung der Eintragung gegen Dritte; Gutglaubensschutz.

## Checkliste Registerprüfung
- [ ] Registerauszug Abt. I: Eigentümereintragung; Name; IMO; Flagge; BRZ
- [ ] Registerauszug Abt. II: alle Hypotheken; Beträge; Gläubiger; Rang
- [ ] Registerauszug Abt. III: Arreste; Vormerkungen; Veräußerungsverbote
- [ ] Richtigkeit der Eintragung mit tatsächlichen Verhältnissen verglichen
- [ ] Negativattest beim Registergericht beantragt

## Relevante Rechtsprechung
- BGH zur Konstitutivwirkung der Eintragung bei Schiffseigentum; kein Eigentumsübergang ohne Eintragung.
- OLG Hamburg zur Berichtigungsklage nach SchRG § 3 bei unrichtiger Registereintragung.
- LG Hamburg zur Vormerkung im Schiffsregister; Schutz des Käufers vor Zwischeneintragungen.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- SchRegO: https://dejure.org/gesetze/SchRegO
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- BGH Schiffsregister: https://www.bgh.de

## 4. `see-004-schiffshypothek-pruefen`

**Fokus:** Mandant (Bank oder Kaeufer) prueft bestehende Schiffshypothek: Valutierung; Rang; Sicherungsvertrag nach SchRG §§ 8-74. Hoechstbetragshypothek (SchRG § 75); Sicherungsabrede; Mithaftung Zubehoer (SchRG § 31); Kreditkuendigungsvoraussetzungen. Schiffsglaeubigerrecht-Vorrang (HGB §§ 596-601). Output: Hypothekenpruefvermerk und Freigabestrategie.

# Schiffshypothek prüfen

## Mandantenfall
Eine Schiffsfinanzierungsbank prüft, ob ihre erstrangige Schiffshypothek noch valutiert und durchsetzbar ist, nachdem der Reeder in Zahlungsschwierigkeiten geraten ist. Ein Käufer möchte wissen, welchen Wert eine eingetragene Höchstbetragshypothek in der Zwangsvollstreckung hat. Ein Insolvenzverwalter prüft, welche Schiffshypotheken absonderungsberechtigt sind.

## Erste Schritte
1. Registerauszug Abteilung II: Hypothekennennbetrag; Rang; Bestelldatum; Gläubiger.
2. Sicherungsvertrag beschaffen und prüfen: gesicherte Forderungen; Fälligkeitsbedingungen; Kündigungsrechte.
3. Valutierung feststellen: Kreditkontostand beim Gläubiger anfordern.
4. Höchstbetragshypothek (SchRG § 75) von Verkehrshypothek unterscheiden.
5. Mithaftung des Zubehörs prüfen: SchRG § 31 – Schiffsmaschinen; Zubehör; Schiffsdokumente.
6. Zwangsvollstreckungsrisiko bewerten: ZPO §§ 864-871; Rangstreit mit anderen Gläubigern.

## Rechtsrahmen
- SchRG §§ 8-30: Bestellung und Übertragung der Schiffshypothek; Eintragungserfordernis.
- SchRG § 31: Mithaftung des Zubehörs; Schiffsmaschinen und Ausrüstung als Haftungsgegenstand.
- SchRG §§ 59-74: Rang der Schiffshypothek gegenüber anderen Hypotheken und Schiffsgläubigern.
- SchRG § 75: Höchstbetragshypothek zur Sicherung wechselnder Forderungen.
- HGB §§ 596-601: vorrangige gesetzliche Schiffsgläubigerrechte.
- InsO §§ 49-51: Absonderungsrecht des Hypothekengläubigers in der Insolvenz.
- ZPO §§ 864-871: Zwangsvollstreckung in eingetragene Schiffe durch Versteigerung.

## Prüfraster
- Ist die Hypothek erstrangig eingetragen; bestehen Vorlasten?
- Besteht die gesicherte Forderung noch und ist sie valutiert?
- Enthält der Sicherungsvertrag Cross-Default-Klauseln?
- Werden Schiffsgläubigerprivilegien (HGB §§ 596-601) die Hypothek im Rang überholen?
- Ist das Zubehör durch Mithaftungsklausel (SchRG § 31) erfasst?
- Liegt ein aktuelles Gutachten über den Schiffswert vor?

## Typische Fallstricke
- Gesetzliche Schiffsgläubiger entstehen ohne Eintragung und verdrängen Hypotheken im Rang.
- Höchstbetragshypothek: Zinsen über das Maximum hinaus sind ungesichert.
- Bei Flaggenwechsel unter Bare-Boat bleibt Heimatregister-Hypothek erhalten; ausländisches Registerpfandrecht kann konkurrieren.
- Löschung setzt vollständige Valutierungsfreiheit voraus.

## Output
- Hypothekenprüfvermerk: Rang; Valuta; Sicherungsumfang; Risiken
- Freigabestrategie-Empfehlung (Ablösung; Umschuldung; Vollstreckung)
- Checkliste Kreditkündigungsvoraussetzungen


## Erweiterte Normengrundlage

### Hypothekenrecht
- SchRG §§ 8-30: Entstehung; Inhalt; Umfang der Schiffshypothek.
- SchRG §§ 59-74: Rang mehrerer Hypotheken; Verschiebung; Verzicht.
- SchRG § 75: Höchstbetragshypothek für revolvierende Kreditlinien.

### Vollstreckung
- ZPO §§ 864-871: Zwangsversteigerung eingetragener Schiffe; Mindestgebot; Erlösverteilung.
- ZVG §§ 162-170: ergänzende Regeln zur Versteigerung beweglicher Sachen.
- InsO §§ 49-51: Absonderungsrecht des Hypothekengläubigers; Rang vor ungesicherten Gläubigern.

## Checkliste Hypothekenprüfung
- [ ] Alle Hypothekeneintragungen aus Registerauszug Abt. II erfasst
- [ ] Valutierungsstand von jedem Gläubiger bestätigt (Valutierungsauszug)
- [ ] Rang und Gesamtbelastung berechnet
- [ ] Verhältnis Schiffswert zu Gesamtbelastung (LTV) ermittelt
- [ ] Eventuelle Höchstbetragshypotheken (§ 75) auf tatsächliche Inanspruchnahme geprüft
- [ ] Löschungsbewilligungen für freie Ränge vorliegend

## Relevante Rechtsprechung
- BGH zur Valutierung der Schiffshypothek; Nachweis gegenüber Drittgläubigern.
- OLG Hamburg zur Rangverschiebung (SchRG § 59) bei simultanen Anträgen.
- BGH zur Absonderung in der Reederei-Insolvenz; InsO §§ 49-51.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- SchRG §§ 8-75: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- InsO § 49: https://www.gesetze-im-internet.de/inso/__49.html
- ZPO §§ 864 ff.: https://dejure.org/gesetze/ZPO/864.html
- BGH Schiffshypothek: https://www.bgh.de

## 5. `see-006-schiffsverkauf-closing`

**Fokus:** Mandant schliesst Schiffsveraeusserung ab: MOA (Norwegian Saleform/Nipponsale) prufen; Closing-Bedingungen; Eigentumsuebergang (SchRG § 2); Flaggenwechsel; Loeschung alter Hypotheken (SchRG § 19); P&I-Abrechnung; Zertifikats-Ummeldung. FlaggRG §§ 3-5. Output: Closing-Checkliste und Uebergabe-Protokoll.

# Schiffsverkauf Closing – Durchführung und Übergabe

## Mandantenfall
Ein norddeutscher Schiffskapitalfonds veräußert einen Bulkcarrier an einen griechischen Käufer; das Closing soll in Piräus stattfinden; zwei Hypotheken sind abzulösen. Ein Verkäufer möchte die norwegische Saleform-MOA anwenden; deutsche Registerpflichten bestehen parallel. Ein Käufer besteht auf Lieferung mit frischer Klasse und gültigem MLC-Zertifikat.

## Erste Schritte
1. MOA-Text analysieren: Kaufpreis-Zahlungsplan; Delivery Conditions (clean class; no outstanding recommendations); Lieferort und -zeitfenster.
2. Löschungsplan für Hypotheken erstellen: Ablösungsbeträge bei Gläubigerbanken anfordern; Löschungsbewilligungen vorbereiten (SchRG § 19).
3. Eigentumsübergang im Register sicherstellen: Auflassung (SchRG § 2); Vollmachten des Eigentümers prüfen.
4. Flaggenwechsel koordinieren: FlaggRG §§ 3-5; Abmeldung beim deutschen Register; BSH-Abmeldebescheinigung.
5. P&I-Übergabe: laufende Deckung endet mit Closing; Käufer muss eigenen Club-Eintritt nachweisen.
6. Übergabe-Protokoll erstellen: Treibstoffmengen; Bunker-Abrechnung; offene Crew-Löhne; Reparaturliste.

## Rechtsrahmen
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung.
- SchRG § 19: Löschung der Hypothek durch Bewilligung des Gläubigers.
- FlaggRG §§ 3-5: Recht zur Führung der Bundesflagge; Pflicht zur Abmeldung bei Eigentümerwechsel.
- SchRegO §§ 13-19: Eintragungsverfahren für Eigentumsübergang und Hypothekenlöschung.
- MLC 2006 Titel 5 Reg. 5.1.3: MLC-Zertifikat bleibt beim Schiff; Neuausstellung nach Flaggenwechsel nötig.
- ISM-Code Kapitel 3: SMC-Gültigkeit endet mit Eigentümerwechsel; neues DOC des Käufers erforderlich.

## Prüfraster
- Sind alle Hypotheken ablösungsbereit und Löschungsbewilligungen vorhanden?
- Liegt das Delivery-Conditions-Zertifikat des Klassifikators vor?
- Hat der Käufer gültigen P&I-Deckungsnachweis für erste Reise nach Übergabe?
- Ist die Bunker-Menge gemessen und der Abrechnung zugrunde gelegt?
- Gibt es offene Arrestvermerke im Register?

## Typische Fallstricke
- Closing ohne gleichzeitige Registereintragung: Schiff ist rechtlich noch beim Verkäufer.
- P&I-Lücke zwischen Closing und Club-Aufnahme des Käufers.
- Bunker-Streit nach Übergabe mangels Protokollierung.
- ISM-/MLC-Zertifikate nicht rechtzeitig neu ausgestellt; Detention droht.

## Output
- Closing-Checkliste (Dokumente; Register; Versicherung; Zertifikate)
- Übergabe-Protokoll-Baustein (Delivery and Acceptance Certificate)
- Ablösungsrechnung-Vorlage für Hypothekenbanken


## Erweiterte Normengrundlage

### Kaufrecht
- BGB §§ 433-453: Kaufvertrag; Übergabe; Eigentumsübertragung; Gewährleistung.
- SchRG § 2: Eigentumsübergang am Seeschiff nur durch Einigung und Eintragung.
- SchRG § 19: Löschung der Hypothek; Bewilligung; notarielle Form.

### Abwicklung
- SchRegO §§ 13-19: Eintragungsverfahren; Antragsteller; Unterlagen.
- FlaggRG §§ 3-9: Pflicht zur Führung der deutschen Flagge; Entziehung; Ausnahmen.
- MLC 2006 Reg. 5.1.3: Neuausstellung MLC-Zertifikat nach Eigentümerwechsel.

## Checkliste Closing Schiffsverkauf
- [ ] MOA/NSF-Kaufvertrag unterzeichnet; Conditions Precedent erfüllt
- [ ] Escrow-Konto eingerichtet; Kaufpreis hinterlegt
- [ ] Alle Hypothekenlöschungsbewilligungen vorliegend
- [ ] Delivery and Acceptance Certificate vorbereitet
- [ ] Eigentumsumschreibung beim Registergericht beantragt
- [ ] P&I-Club-Membership des Käufers bestätigt
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) auf neuen Eigentümer umgestellt

## Relevante Rechtsprechung
- BGH zur Wirksamkeit der NSF-Saleform-Klauseln nach deutschem Recht.
- OLG Hamburg zur Simultanabwicklung (simultaneous closing) bei Schiffen.
- BGH zur Haftung des Verkäufers nach Closing für gesetzliche Schiffsgläubigerrechte.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- SchRG §§ 2/19: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- FlaggRG: https://www.gesetze-im-internet.de/flaggrg/
- SchRegO: https://dejure.org/gesetze/SchRegO
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- MLC ILO: https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C186
