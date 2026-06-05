---
name: see-werftvertrag-closing-klagepfad-waehlen
description: "SEE Werftvertrag Closing Klagepfad Waehlen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Werftvertrag Closing Klagepfad Waehlen

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Werftvertrag Closing Klagepfad Waehlen** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-048-werftvertrag-closing-planen` | Werftvertrag: Closing eines Neubauprojekt unter Werftvertrag-Kaufs oder einer Finanzierung planen: Eigentumsuebergang (SchRG § 2); Hypothekenloesung (SchRG § 19); simultane Zahlung und Eintragung; Zertifikats-Ummeldung. Output: Closing-Checkliste und Zeitplan. |
| `see-049-werftvertrag-klagepfad-waehlen` | Werftvertrag: Glaeubiger oder Reeder waehlt Klagepfad bei Streit um Neubauprojekt unter Werftvertrag: Zwangsversteigerung (ZPO §§ 864-871); Arrest; einvernehmlicher Verkauf; Insolvenzantrag. Rangfolge und Erloesprognose. Output: Klagepfad-Analyse und Erloesprognose. |
| `see-050-werftvertrag-risiko-memo-schreiben` | Werftvertrag: Gesamtrisikobewertung fuer Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel bei Neubauprojekt unter Werftvertrag: Kreditausfall; Hypothekenrang; Schiffsglaeubigerrechte; Wrackpflicht; Insolvenzrisiko; Handlungsoptionen. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Output: Risiko-Memo und Empfehlungsmatrix. |
| `see-053-yachtkauf-kaufvertrag-scopen` | Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus scopet Kaufvertrag fuer Segel- oder Motorjacht: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-063-containerschiff-kaufvertrag-scopen` | Containerschiff: Reederei; Linienoperator; Slot-Charter oder Leasinggesellschaft scopet Kaufvertrag fuer Containerlinienfrachtschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 481-526 Stueckgutfracht; SchRG §§ 8-75; ISPS-Code; SOLAS Kap. XI-2. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Werftvertrag Closing Klagepfad Waehlen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-048-werftvertrag-closing-planen`

**Fokus:** Werftvertrag: Closing eines Neubauprojekt unter Werftvertrag-Kaufs oder einer Finanzierung planen: Eigentumsuebergang (SchRG § 2); Hypothekenloesung (SchRG § 19); simultane Zahlung und Eintragung; Zertifikats-Ummeldung. Output: Closing-Checkliste und Zeitplan.

# Werftvertrag – Closing planen

## Mandantenfall
Der Kauf eines Neubauprojekt unter Werftvertrag soll abgeschlossen werden; Hypotheken sind abzulösen. Ein Käufer besteht auf lastenfreier Lieferung mit gültiger Klasse und MLC-Zertifikat. Eine Bank koordiniert das Closing bei syndizierten Finanzierungen.

## Erste Schritte
1. Ablosebetraege aller Hypothekenglaeubiger anfordern; Stichtag abstimmen.
2. Loeschungsbewilligungen (SchRG § 19) beschaffen; zeitlich koordinieren.
3. Escrow-Konto einrichten: Kaufpreis gegen Loeschungsbestaetigung.
4. Eigentumsuebergang (SchRG § 2) und Hypothekenloesung gleichzeitig fuer Neubauprojekt unter Werftvertrag.
5. Zertifikate (Klasse; ISM; MLC; ISPS) auf neuen Eigentuemer ummelden.
6. Registerauszug nach Closing beschaffen; Closing-Memo erstellen.

## Rechtsrahmen
- SchRG §§ 2/19; SchRegO §§ 13-19; FlaggRG §§ 3-5; ISM-Code Kap. 3 SMC-Neuzertifizierung.

## Prüfraster
- Sind alle Loeschungsbewilligungen zeitlich koordiniert?
- Ist der Escrow-Mechanismus wasserdicht gegen Insolvenz des Verkaeufers?
- Sind alle Zertifikate fuer Neubauprojekt unter Werftvertrag auf neuen Eigentuemer vorbereitet?
- Ist der Flaggenwechsel (wenn vorgesehen) vorbereitet?
- Ist die Vollmacht fuer den Registerantrag aktuell?

## Typische Fallstricke
- Zahlung ohne simultane Loeschung: Hypothek bleibt trotz Zahlung eingetragen.
- ISM-/MLC-Luecke nach Eigentumsuebergang; Port-State-Detention droht.
- Nachranghypotheken blockieren Closing wenn Erstrangglaeubigerbank nicht kooperiert.

## Output
Closing-Checkliste und Zeitplan mit Abhängigkeiten für Neubauprojekt unter Werftvertrag.


## Vertiefung: Closing-Mechanismus im Schiffskauf
Das Closing eines Schiffskaufs ist der Moment wo Eigentum und Risiko auf den Käufer übergehen. Technisch besteht das Closing aus: (1) Zahlung des Kaufpreises (oder freigabe aus Escrow); (2) Übergabe der Delivery Documents; (3) Eintragung des Eigentumsübergangs im Schiffsregister (SchRG § 2). Alle drei Schritte sollen simultan erfolgen; in der Praxis nutzt man Softclose-Mechanismen.

## Delivery Documents Checkliste
Folgende Originalunterlagen müssen beim Closing übergeben werden: Klasse-Zertifikat; Delivery and Acceptance Certificate; Protokoll zur Übergabe von Bunker und Schmieröl; alle Schiffszertifikate (IOPP; IAPP; MLC; ISSC; BSH-Fahrterlaubnis); Logbücher; technische Handbücher. Kopien werden bei der abgebenden Reederei archiviert.

## Nachsorge nach dem Closing
Nach dem Closing: Neuanmeldung beim Flaggenregister; Beantragung neuer DOC beim ISM-Code-Unternehmen; MLC-Erneuerung; P&I-Club-Eintritt des Käufers; Benachrichtigung aller Charterer und Hafenbehörden über den Eigentümerwechsel. Closing-Memo erstellen mit Datum; Kaufpreis; alle übergebenen Dokumente; Beteiligten.


## Checkliste Closing-Vorbereitung
- [ ] Ablösebeträge aller Hypothekengläubiger angefordert; Stichtag fixiert
- [ ] Löschungsbewilligungen (SchRG § 19) von allen Gläubigern vorliegend
- [ ] Escrow-Konto eingerichtet; Escrow-Agent benannt
- [ ] Eigentumsübergang (SchRG § 2) und Hypothekenlöschung zeitlich koordiniert
- [ ] Alle Zertifikate (Klasse; ISM/DOC/SMC; MLC/DMLC; ISSC; BSH) auf neuen Eigentümer vorbereitet
- [ ] P&I-Club-Eintritt des Käufers bestätigt
- [ ] Delivery and Acceptance Certificate vorbereitet
- [ ] Registerauszug nach Closing beauftragt
- [ ] Closing-Memo-Vorlage bereitgestellt

## Relevante Rechtsprechung
- BGH zur Wirksamkeit des Eigentumsübergangs an Schiffen; Einigung und Eintragung als konstitutive Voraussetzungen.
- OLG Hamburg zur Auslegung von Closing-Conditions in MOA-Verträgen; Delivery-Condition-Klauseln.
- BGH zur Haftung des Verkäufers für nach Closing entstehende Schiffsgläubigerrechte; Freistellungspflicht.

## Normen im Überblick
- SchRG § 2: Eigentumsübergang durch Einigung und Eintragung; nicht durch Besitzübergabe.
- SchRG § 19: Löschung der Hypothek; Form; Zeitpunkt; Wirkung.
- SchRegO §§ 13-19: Eintragungsverfahren; Antragsteller; Fristen.
- FlaggRG §§ 3-5: Berechtigung zur Flagge; Pflichten bei Eigentumsübergang.
- ISM-Code Kap. 3: SMC-Gültigkeit und Neuausstellung nach Eigentümerwechsel.
- MLC 2006 Reg. 5.1.3: Neuausstellung MLC-Zertifikat nach Eigentumsübergang und Flaggenwechsel.


## Vertiefung Closing

### Simultaneous Closing
Das "simultaneous closing" (Zug-um-Zug-Abwicklung) ist bei Schiffsverkäufen mit Kreditfinanzierung Standard. Ablöse der Altfinanzierung; Neuhypothek für den Käufer; Eigentumsumschreibung; Kaufpreiszahlung — alles erfolgt zeitgleich über ein Escrow-Konto.

### Zertifikatsübergang
Klasse- und ISM-Zertifikate bleiben nicht automatisch mit dem Schiff verbunden; sie sind personengebunden (SMC an den Reeder; DOC an den Betreiber). Der Käufer muss rechtzeitig seine eigene ISM-Zulassung (DOC) und das SMC für das Schiff beantragen.

## Normen-Synopse Closing
| Norm | Inhalt |
|------|--------|
| SchRG § 2 | Eigentumsübergang |
| SchRG § 19 | Hypothekenlöschung |
| FlaggRG § 3 | Flagge bei Eigentümerwechsel |
| MLC Reg. 5.1.3 | MLC-Zertifikat |

## Quellen
- SchRG §§ 2/19: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- FlaggRG: https://www.gesetze-im-internet.de/flaggrg/
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- SchRegO: https://dejure.org/gesetze/SchRegO

## 2. `see-049-werftvertrag-klagepfad-waehlen`

**Fokus:** Werftvertrag: Glaeubiger oder Reeder waehlt Klagepfad bei Streit um Neubauprojekt unter Werftvertrag: Zwangsversteigerung (ZPO §§ 864-871); Arrest; einvernehmlicher Verkauf; Insolvenzantrag. Rangfolge und Erloesprognose. Output: Klagepfad-Analyse und Erloesprognose.

# Werftvertrag – Klagepfad wählen

## Mandantenfall
Eine Bank will nach Kreditausfall aus der Hypothek am Neubauprojekt unter Werftvertrag vollstrecken. Mehrere Gläubiger streiten um den Versteigerungserlös des Neubauprojekt unter Werftvertrag. Ein Reeder prüft, ob ein freiwilliger Verkauf günstiger ist als die Zwangsversteigerung.

## Erste Schritte
1. Schiffswert des Neubauprojekt unter Werftvertrag ermitteln: aktuelles Schätzgutachten beschaffen.
2. Glaeubigerrangfolge aufstellen: gesetzliche Vorrechte dann Hypotheken nach Rang.
3. ZPO §§ 864-871 Zwangsversteigerung: Zeitaufwand; Kosten; erwarteter Erloes.
4. Einvernehmlichen Verkauf pruefen: schneller und guenstiger wenn Reeder kooperiert.
5. Insolvenzantrag als taktisches Mittel: Arrests anderer Glaeubiger stoppen.
6. Schiedsklausel im Kreditvertrag pruefen: London Arbitration oder deutsches Gericht?

## Rechtsrahmen
- ZPO §§ 864-871 Zwangsversteigerung; InsO §§ 49-51 Absonderung; HGB §§ 596-601 Vorrangrechte; SchRG §§ 59-74 Rang.

## Prüfraster
- Uebersteigt Schiffswert des Neubauprojekt unter Werftvertrag die Kreditvaluta?
- Gibt es erstrangige Vorrechte die den Erloes aufzehren?
- Ist einvernehmlicher Verkauf moeglich?
- Droht auslaendische Vollstreckung das deutsche Verfahren zu unterlaufen?
- Ist Insolvenzantrag taktisch sinnvoll?

## Typische Fallstricke
- Gesetzliche Schiffsglaeubigerrechte (Crew-Loehne/Hafen) fressen Erloes vor Hypotheken.
- Zwangsversteigerung dauert; Schiffswert sinkt durch Stillstand im Hafen.
- Auslaendische Arrests parallel zum deutschen Verfahren.

## Output
Klagepfad-Analyse und Erlösprognose (Tabelle Kosten vs. Erlös) für Neubauprojekt unter Werftvertrag.


## Vertiefung: Gerichtsstand und Schiedsklauseln im Seerecht
Im deutschen Seerecht gilt für Schiffsarrest die ZPO § 919 (Gericht am Liegeplatz). Für streitige Klagen über Schiffshypotheken gilt ZPO § 29c (besonderer Gerichtsstand) oder der allgemeine Gerichtsstand. International ist London Arbitration (LMAA-Schiedsordnung) der Marktstandard für Charterparty-Streitigkeiten; Hamburg Arbitration (DIS-Regeln) ist eine deutsche Alternative.

## Vollstreckung ausländischer Urteile und Schiedssprüche
Ausländische Urteile aus EU-Staaten werden nach EuGVVO 2012 automatisch anerkannt; Vollstreckbarerklärung durch deutsches Gericht nötig. Ausländische Schiedssprüche werden nach dem New Yorker Übereinkommen 1958 (NYÜ) anerkannt; Deutschland ist Vertragsstaat. Einwendungen gegen Anerkennung: ordre public; fehlende Schiedsvereinbarung; Verletzung des rechtlichen Gehörs.

## Kostenabwägung Klage vs. Schiedsverfahren
Schiedsverfahren (London/Hamburg): höhere Kosten (Schiedsrichter-Honorare); aber schneller; vertraulicher; international vollstreckbarer. Ordentliches Gericht: günstigere RVG-Gebühren; aber Öffentlichkeit; Instanzenzug; schlechtere internationale Vollstreckbarkeit. Priorität: kurzfristige Sicherungsmaßnahmen (Arrest) immer vor ordentlichem Gericht; Hauptsacheverfahren nach Klausel.


## Checkliste Klagepfad-Entscheidung
- [ ] Aktueller Schiffswert gutachterlich ermittelt
- [ ] Gläubigerrangfolge aufgestellt (gesetzliche Vorrechte; Hypotheken; ungesicherte Gläubiger)
- [ ] Insolvenzwahrscheinlichkeit des Reeders bewertet
- [ ] Optionen verglichen: Zwangsversteigerung; einvernehmlicher Verkauf; Insolvenzantrag
- [ ] Schiedsklausel geprüft; Schiedsort und Schiedsregeln identifiziert
- [ ] Zeitlinie je Option: Wochen bis zur Verwertung; Kosten; Erlösprognose
- [ ] Entscheidung dokumentiert und von Entscheidungsträger genehmigt

## Relevante Rechtsprechung
- BGH zur Zwangsversteigerung von Seeschiffen; ZPO §§ 864-871; Verteilung des Erlöses.
- BGH zur Wirkung des Insolvenzantrags auf laufende Arrests und Pfändungen; InsO § 21.
- BGH zur LMAA-Schiedsklausel; Wirksamkeit in Deutschland; Vollstreckbarerklärung nach NYÜ.

## Normen im Überblick
- ZPO §§ 864-871: Zwangsversteigerung und Zwangsverwaltung eingetragener Schiffe.
- ZPO § 864: Gegenstand der Zwangsvollstreckung; Seeschiffe als unbewegliche Gegenstände.
- ZPO § 865: Beschlagnahme; Verfügungsverbot; Wirkung auf Charter-Zahlungen.
- InsO § 103: Wahlrecht des Insolvenzverwalters bei gegenseitigen Verträgen (Charter).
- InsO §§ 129-147: Insolvenzanfechtung; Tilgungen in der Krise rückforderbar.
- New Yorker Übereinkommen 1958: Anerkennung und Vollstreckung ausländischer Schiedssprüche.


## Vertiefung Klagepfad

### Zwangsversteigerung vs. Insolvenz
Die Zwangsversteigerung (ZPO §§ 864-871) ist effizienter, wenn das Schiff noch betrieben wird und einen Marktwert über den Hypotheken hat. Der Insolvenzantrag ist sinnvoller, wenn mehrere Schiffe betroffen sind oder der Reeder persönlich in die Haftung genommen werden soll.

### Schiedsgerichtsbarkeit
Schifffahrtssachen werden häufig vor dem LMAA (London Maritime Arbitrators Association) oder dem GMAA (German Maritime Arbitration Association) ausgetragen. LMAA-Schiedssprüche sind nach NYÜ 1958 in Deutschland vollstreckbar.

## Normen-Synopse Klagepfad
| Norm | Inhalt |
|------|--------|
| ZPO § 864 | Zwangsversteigerung |
| InsO § 103 | Charter-Wahlrecht |
| InsO § 49 | Absonderungsrecht |
| NYÜ 1958 | Schiedssprüche |

## Quellen
- ZPO §§ 864-871: https://dejure.org/gesetze/ZPO/864.html
- InsO §§ 49-51: https://www.gesetze-im-internet.de/inso/__49.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- BGH Zwangsversteigerung Schiff: https://www.bgh.de

## 3. `see-050-werftvertrag-risiko-memo-schreiben`

**Fokus:** Werftvertrag: Gesamtrisikobewertung fuer Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel bei Neubauprojekt unter Werftvertrag: Kreditausfall; Hypothekenrang; Schiffsglaeubigerrechte; Wrackpflicht; Insolvenzrisiko; Handlungsoptionen. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Output: Risiko-Memo und Empfehlungsmatrix.

# Werftvertrag – Risiko-Memo schreiben

## Mandantenfall
Eine Bank bereitet den Vorstand auf potenzielle Kreditausfälle in der Werftvertrag-Flotte vor. Ein Finanzinvestor prüft den Kauf eines Kreditportfolios mit Werftvertrag-Hypotheken. Ein Syndikat benötigt ein gemeinsames Risikodokument für alle Banken.

## Erste Schritte
1. Werftvertrag-Daten zusammenfassen: IMO-Nummer; Flagge; Alter; Schiffswert; Kreditvaluta.
2. Hypothekenrang und Konkurrenzrechte darstellen.
3. Hauptrisiken identifizieren: Wertverfall; Reeder-Insolvenz; Vorrangglaeubigerrechte; Wrackpflicht.
4. Handlungsoptionen mit Kosten-Nutzen-Analyse formulieren.
5. Zeitkritische Massnahmen priorisieren: Arrest; Versicherungspruefung; ISM-Status.
6. Empfehlungsmatrix fuer Entscheidungstraeger erstellen.

## Rechtsrahmen
- BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen; InsO §§ 49-51 Absonderung; WSG §§ 1-12 Wrackpflicht; ZPO §§ 864-871 Zwangsversteigerung.

## Prüfraster
- Ist aktueller Schiffswert fuer Neubauprojekt unter Werftvertrag dokumentiert?
- Sind alle Vorrangglaeubigerrechte (gesetzliche Schiffsglaeubigerrechte) bekannt?
- Ist Wrackbeseitigungs-Versicherungsdeckung bestaetigt?
- Ist Insolvenzwahrscheinlichkeit des Reeders bewertet?
- Sind Handlungsoptionen mit Zeitplan und Kosten aufgelistet?

## Typische Fallstricke
- Schiffswertgutachten fuer Neubauprojekt unter Werftvertrag veraltet; Marktpreise schwanken stark.
- Memo ohne Priorisierung zeitkritischer Massnahmen fuehrt zu Untaetigkeit.
- Vorrangglaeubigerrechte (Besatzungsloehne/Hafengebuehren) werden unterschaetzt.

## Output
Risiko-Memo (Exekutivfassung) und Empfehlungsmatrix für Neubauprojekt unter Werftvertrag.


## Vertiefung: Struktur des Risiko-Memos
Ein hochwertiges Risiko-Memo enthält: (1) Zusammenfassung und Handlungsempfehlung (Executive Summary; max. 1 Seite); (2) Schiffsdaten und aktueller Schiffswert (mit Gutachterquelle und -datum); (3) Kreditstatus (Valutastand; Zinsen; Fälligkeiten; Default-Events); (4) Sicherheitenanalyse (Hypothekenrang; Verwertungserlös-Prognose); (5) Gläubigerrangfolge (gesetzliche Vorrechte; Hypotheken; ungesicherte Forderungen); (6) Risikoszenarien (Best Case; Base Case; Worst Case); (7) Maßnahmenplan mit Zeitlinie und Verantwortlichen.

## Schiffswertermittlung
Schiffswerte werden bestimmt durch: Chartermarkt (aktueller T/C-Äquivalent-Erlös); Vergleichsverkäufe (comparable sales aus Baltic Exchange oder SSY); Gutachten von Shipbrokers (Clarkson; Braemar; Gibson). In der Insolvenz kann ein Notverkauf (forced sale) 10-30% unter dem Schätzwert liegen.

## Eskalationsweg und Zeitkritikalität
Zeitkritische Maßnahmen müssen sofort eingeleitet werden: Arrest bei Fluchtgefahr (sofort); Versicherungsmeldung (binnen 24 Stunden); P&I-Kündigung verhindern (laufende Prämien beobachten); ISM-DOC-Ablauf prüfen (ohne DOC kein Hafenanlauf). Das Risiko-Memo soll diese Zeitlinie explizit darstellen damit Entscheidungsträger die Prioritäten erkennen.


## Checkliste Risiko-Memo
- [ ] Schiffsdaten vollständig: IMO-Nummer; Flagge; Alter; BRZ; Schiffstyp; Klasse
- [ ] Schiffswert: Gutachterquelle; Datum; Methode (Charter-Equivalent; Comparable Sales)
- [ ] Kreditstatus: Valutastand; Zinsen; letzte Zahlung; Default-Events
- [ ] Hypothekenrang: alle Gläubiger; Beträge; Rangstellen
- [ ] Gesetzliche Vorrechte (HGB §§ 596-601): aktuelle Crew-Löhne; Hafengebühren; PSC-Bußgelder
- [ ] Versicherungsdeckung: P&I-Club-Mitgliedschaft; H&M-Police; MII; Laufzeit
- [ ] ISM-/MLC-Zertifikatsstatus: Ablaufdaten; bekannte Mängel
- [ ] Drei Szenarien: Best Case (einvernehmlicher Verkauf); Base Case (Zwangsversteigerung); Worst Case (Insolvenz + Verschrottung)
- [ ] Maßnahmenplan mit Zeitlinie und Verantwortlichen
- [ ] Executive Summary: Gesamtrisiko; Handlungsempfehlung; Nächste Schritte

## Relevante Rechtsprechung
- BGH zur Absonderung des Hypothekengläubigers in der Reederei-Insolvenz; InsO §§ 49-51.
- BGH zur Insolvenzanfechtung von Hypothekentilgungen in der Krise (InsO §§ 130-133).
- OLG Hamburg zu Schiffswertgutachten in Verwertungsverfahren; Anforderungen an die Sachverständigenqualifikation.

## Normen im Überblick
- InsO §§ 49-51: Absonderungsrecht; Hypothekengläubiger befriedigt sich vor der Insolvenzmasse.
- InsO §§ 80-92: Verwaltungs- und Verfügungsbefugnis des Insolvenzverwalters über Schiffe.
- HGB §§ 611-617: Summenhaftung; Haftungsbeschränkung des Reeders; Limits nach LLMC 1976/1996.
- ZPO §§ 864-871: Zwangsversteigerung; Mindestgebot; Erlösverteilung.
- SchRG §§ 59-74: Rangfolge bei der Erlösverteilung nach Zwangsversteigerung.


## Vertiefung Risiko-Memo

### Drei-Szenarien-Analyse
Ein gutes Risiko-Memo enthält immer drei Szenarien: (1) Best Case: freiwilliger Verkauf zum Marktwert; vollständige Schuldenablösung; (2) Base Case: Zwangsversteigerung mit 15-20% Abschlag; teilweise Restschuld; (3) Worst Case: Insolvenz des Reeders; Schiff liegt fest; Erlös nach Kosten nur Teilbefriedigung.

### Zeitlinie
Die Dauer eines Seearrests bis zur Zwangsversteigerung beträgt in Deutschland typischerweise 3-6 Monate; in anderen Jurisdiktionen kürzer (Singapore: 4-6 Wochen; Panama: 2-3 Monate).

## Normen-Synopse Risiko-Memo
| Norm | Inhalt |
|------|--------|
| HGB § 596 | Gesetzliche Vorrechte |
| InsO § 49 | Absonderungsrecht |
| ZPO § 864 | Zwangsversteigerung |
| SchRG § 59 | Rangfolge |

## Quellen
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- InsO §§ 49-51: https://www.gesetze-im-internet.de/inso/__49.html
- BSH: https://www.bsh.de

## 4. `see-053-yachtkauf-kaufvertrag-scopen`

**Fokus:** Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus scopet Kaufvertrag fuer Segel- oder Motorjacht: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Yachtkauf – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Segel- oder Motorjacht; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Segel- oder Motorjacht unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Segel- oder Motorjacht.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. CE-Kennzeichnung; Fahrterlaubnis BSH; VAT-Status EU; MCA Cat..

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Segel- oder Motorjacht fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Segel- oder Motorjacht.


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de

## 5. `see-063-containerschiff-kaufvertrag-scopen`

**Fokus:** Containerschiff: Reederei; Linienoperator; Slot-Charter oder Leasinggesellschaft scopet Kaufvertrag fuer Containerlinienfrachtschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 481-526 Stueckgutfracht; SchRG §§ 8-75; ISPS-Code; SOLAS Kap. XI-2. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Containerschiff – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Containerlinienfrachtschiff; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Containerlinienfrachtschiff unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Containerlinienfrachtschiff.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- HGB §§ 481-526 Stueckgutfracht; SchRG §§ 8-75; ISPS-Code; SOLAS Kap. XI-2; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. SOLAS Chapter VI Gefahrgut; IMO DG-Code; Container-Gewichtsverifikation VGM.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Containerlinienfrachtschiff fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Containerlinienfrachtschiff.


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de
