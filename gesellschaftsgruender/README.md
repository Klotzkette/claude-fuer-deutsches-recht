# gesellschaftsgruender — Gruendungsassistent fuer deutsche Gesellschaften

Freistehendes Plugin, das durch die Gruendung einer deutschen Gesellschaft fuehrt — von der Rechtsformwahl ueber Cap Table, Class-Shares, Notar, Handelsregister, Behoerdenanmeldungen bis hin zu den ersten 100 Tagen Geschaeftsfuehrer-Pflichten und Streit-Eskalationen.

## Mandatsperspektive

**Du als Anwalt, Steuerberater, Gruender oder Notarberater.** Das Plugin

- erfasst die **Gruender-Eckdaten** strukturiert,
- klaert die **Rechtsformwahl** (GmbH, UG, GbR, OHG, KG, GmbH & Co. KG, AG, PartG, gGmbH, eK),
- entwickelt **Cap Table** mit Pre/Post-Money und Verwaesserungs-Simulation,
- liefert **Class-Shares** (A/B/C/Common) mit Liquidation Preference,
- erstellt **Gesellschaftervereinbarung (SHA)** mit Vesting, Drag/Tag, Stimmverpflichtungen,
- bereitet die **Notarsitzung** vor (auch DiRUG-online),
- begleitet die **Handelsregister-Anmeldung**,
- koordiniert die **Behoerden-Anmeldungen** (Gewerbe, Finanzamt, IHK, BG, TraFinG),
- liefert eine **Geschaeftsordnung der Geschaeftsfuehrung** und Meeting-Templates,
- erstellt **Gesellschafterversammlungs-Einladungen** und **Protokolle**,
- vermittelt **bilinguale Dokumente** Deutsch/Englisch,
- klaert den **Sozialversicherungs-Status** des Geschaeftsfuehrers,
- begleitet **Gesellschafterstreit** mit Eilantraegen LG und Registergericht,
- prueft den **Firmennamen** (HR, IHK, DPMA, EUIPO),
- liefert eine **erste 100-Tage-Checkliste** fuer den Geschaeftsfuehrer.

Beruecksichtigt aktuelle Gesetzeslage Stand 2026 inkl. **MoPeG** (Modernisierung Personengesellschaftsrecht, Januar 2024) und **DiRUG** (Online-Gruendung per Videokonferenz, August 2022).

## Aufbau

Der Lebenszyklus einer Gruendung laeuft in fuenf Phasen:

```
Phase 0 — Intake und Rechtsformwahl (Woche 1)
  └─ Gruender-Intake → Rechtsformwahl → Firmenname-Pruefung
     → Cap Table initial

Phase A — Vorbereitung (Woche 2-3)
  └─ Gesellschafterstruktur, Class-Shares, Stammkapital
     Beirat / Advisory Board einplanen

Phase B — Vertraege (Woche 3-4)
  └─ Gesellschaftsvertrag/Satzung mit B-Shares Vetorechten
     Gesellschaftervereinbarung mit Vesting Drag Tag
     Geschaeftsfuehrer-Anstellungsvertrag mit SV-Status
     Geschaeftsordnung der Geschaeftsfuehrung
     Beiratsordnung
     Stimmverpflichtungs-Vereinbarungen SHA-Satzung
     Bilinguale Fassungen Deutsch / Englisch

Phase C — Notar + Handelsregister (Woche 4-6)
  └─ Beurkundung (physisch oder online nach DiRUG)
     Stammkapital-Einzahlung
     Anmeldung beim Handelsregister
     Eintragung

Phase D — Behoerden und operativer Start (Woche 6-8)
  └─ Gewerbeamt, Finanzamt-Erfassung, IHK, BG, Transparenzregister
     Geschaeftskonto, Buchhaltung, Compliance-Aufbau
     Erste 100 Tage Geschaeftsfuehrer-Pflichten
     Gesellschafterversammlungen Einladungen Protokolle

Phase E — Laufender Betrieb und Konflikt-Mass nahmen
  └─ Kapitalerhoehungen (genehmigtes Kapital, Bezugsrecht)
     Pflichtversammlung bei Stammkapital-Verlust Paragraf 49 III GmbHG
     Gesellschafterstreit Eilantraege LG Registergericht
     Schlichtung durch Beirat
```

## Enthaltene Skills (36)

### Phase 0 — Intake und Rechtsformwahl (5 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-kommandocenter` | Master-Workflow mit Fristen Beteiligten Kosten |
| `gesellschaftsgruender-gruender-intake` | Strukturierte Eingangs-Abfrage Gruender Anteile Class-Shares Geschaeftsmodell |
| `gesellschaftsgruender-rechtsformwahl` | Entscheidungsmatrix GmbH/UG/GbR/OHG/KG/AG/PartG/gGmbH/eK |
| `gesellschaftsgruender-firmenname-pruefung` | HR DPMA EUIPO Domain Verwechslungsgefahr Irrefuehrungsverbot |
| `gesellschaftsgruender-cap-table` | Capitalization Table Pre/Post-Money Verwaesserung Liquidation-Waterfall |

### Phase A — Strukturen und Sondervetorechte (4 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gmbh-vorbereitung` | Sieben Bausteine: Firma Sitz Gegenstand Stammkapital Anteile GF Satzungswahl |
| `gesellschaftsgruender-ug-vorbereitung` | UG-Spezifika Thesaurierungspflicht Paragraf 5a III GmbHG |
| `gesellschaftsgruender-egbr-mopeg` | GbR nach MoPeG 2024 Gesellschaftsregister Pflichteintragung Grundstuecksgeschaefte |
| `gesellschaftsgruender-kg-und-gmbhcokg` | KG und GmbH und Co KG Komplementaer Kommanditist Hafteinlage |
| `gesellschaftsgruender-share-classes-a-b-c` | Anteilsklassen A/B/C Common Liquidation Preference Anti-Dilution |
| `gesellschaftsgruender-golden-share-und-vetorechte` | Golden Share Sperrminoritaet Vetorechte Restrukturierung |

### Phase B — Vertraege und Geschaeftsordnung (8 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gesellschaftsvertrag-gmbh` | Satzung mit Pflicht-/Standard-Klauseln Musterprotokoll vs individuell |
| `gesellschaftsgruender-gesellschaftervereinbarung` | SHA: Vesting Leaver Drag Tag Liquidation Anti-Dilution Pönalen |
| `gesellschaftsgruender-sha-satzung-stimmverpflichtung` | Stimmverpflichtung Innenverhaeltnis Joinder Agreement Pönalen |
| `gesellschaftsgruender-geschaeftsfuehrervertrag` | GF-Anstellung Vergueutung Wettbewerb D&O SV-Status vGA |
| `gesellschaftsgruender-gf-sozialversicherungs-status` | Fremd-GF Mehrheits-/Minderheits-GF Statusfeststellung Paragraf 7a SGB IV |
| `gesellschaftsgruender-geschaeftsordnung-gf` | Geschaeftsordnung der Geschaeftsfuehrung Zustimmungs-Kataloge |
| `gesellschaftsgruender-gf-meeting-templates` | Tagesordnung Einladung Protokoll Umlauf-Beschluss bilingual |
| `gesellschaftsgruender-beirat-advisory-board` | Beirat Advisory Board Beiratsordnung Schlichtungs-Funktion |
| `gesellschaftsgruender-bilinguale-dokumente` | Deutsch und Englisch parallel Vorrang-Klausel Uebersetzungs-Fallen |
| `gesellschaftsgruender-klauselkatalog-bilingual` | Volltextliche DE/EN-Klauseln Stimmbindung Golden-Share-StaRUG-Veto BSG-feste Sperrminoritaet Drag Tag Liquidation Preference Anti-Dilution Vesting Bad-Leaver Koppelung Wettbewerbsverbot |
| `gesellschaftsgruender-intake-decision-tree` | Mermaid-Decision-Tree fuer Intake conditional logic Knoten Trigger-Events Workflow-Engine-Architektur |

### Phase C — Notar und Handelsregister (3 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-notar-vorbereitung` | Notarsitzung Unterlagen GNotKG-Kosten Sacheinlage |
| `gesellschaftsgruender-online-gruendung-dirug` | DiRUG-Online-Gruendung Videokonferenz seit August 2022 |
| `gesellschaftsgruender-handelsregister-anmeldung` | Anmeldung Versicherungen Paragraf 8 II GmbHG Vor-GmbH |

### Phase D — Behoerden und Start (5 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gewerbeanmeldung-finanzamt` | Gewerbeamt Paragraf 14 GewO ELSTER USt-Wahl Kleinunternehmer |
| `gesellschaftsgruender-transparenzregister` | TraFinG wirtschaftlich Berechtigter Bussgeld bis 150000 EUR |
| `gesellschaftsgruender-ihk-und-berufsgenossenschaft` | IHK HwK BG binnen 1 Woche Freiberufler-Spezifika |
| `gesellschaftsgruender-stammkapital-einzahlung` | Bareinlage freie Verfuegung Paragraf 7 II 2 GmbHG Hin-und-Herzahlen verboten |
| `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` | Erste 100 Tage Buchhaltung Steuern SV Compliance Haftung Paragraf 43 GmbHG |

### Phase E — GV und Konflikt-Mass nahmen (5 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gv-einladung-tagesordnung` | Einladung Paragraf 51 GmbHG Frist Form Tagesordnung Beschluss-Vorlage |
| `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` | Protokoll Versammlungsleiter Wahl Streit notarielle Beurkundung |
| `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` | Pflichtversammlung bei Verlust Haelfte Stammkapital |
| `gesellschaftsgruender-genehmigtes-kapital` | Vorratsbeschluss Paragraf 55a GmbHG bis 50% des Stammkapitals 5 Jahre |
| `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` | Kapitalerhoehung Bezugsrecht Bezugsrechtsausschluss BGH-Linie Kali-Salz |
| `gesellschaftsgruender-gesellschafterstreit-eilantraege` | Einstweilige Verfuegung LG Anmeldungs-Sperre Registergericht Anfechtungsklage |

## Schulungsakte

Im Verzeichnis `testakten/gesellschaftsgruender-streit-roeschen-tech/` befindet sich eine **vollstaendige Schulungsakte** mit dem Szenario einer fiktiven Roeschen Tech GmbH:

- Gruendung mit drei Gruendern und Stammkapital 30.000 EUR
- Series-A-Aufnahme von Stahlauge Ventures AG mit B-Shares
- 2. Kapitalerhoehung mit Bezugsrechtsausschluss zugunsten Pi Mu Holding GmbH
- **Streit** der Minderheits-Gesellschafterin Christine Linnenbach mit Anfechtungsklage, Eilantrag LG, Anmeldungs-Sperre Registergericht
- Schlichtung durch Beirat

Enthaelt:

- Vollstaendige Satzung
- Shareholder Agreement
- Cap Table (Stand 1-4)
- Einladung und Protokoll der streitigen GV
- Anfechtungsklage und Eilantraege
- Beirat-Schlichtungs-Empfehlung
- Schulungsbegleiter mit Lernzielen und Aufgaben

## Pluginscope und Stoppschilder

### Was das Plugin macht

- Strukturen und Schemata vermitteln
- Pflicht- und Soll-Inhalte erklaeren
- Fristen und Beteiligte aufstellen
- Typische Fallstricke benennen
- Praktische Schritt-fuer-Schritt-Anleitungen
- Bilinguale Vorlagen (Deutsch/Englisch)
- Konflikt-Werkzeuge (Eilantraege, Anfechtungsklagen)

### Was nicht

- **Keine Notar-Beurkundung** (muss vor Notar erfolgen)
- **Keine Steuerberatung** (Steuerberater zwingend bei Mandaten)
- **Keine Vertretung im Streit** (Anwalt bei Konflikt-Mandaten)
- **Kein Mandanten-Vertretungs-Vertrag** mit Pflichten zur Schweigepflicht

### Wann zwingend Anwalt / Notar / Steuerberater

- Bei Sacheinlagen mit Werthaltigkeits-Risiko (Differenzhaftung Paragraf 9 GmbHG)
- Bei Beteiligung von Auslandsgesellschaftern (Sanktionsrecht, Investitionspruefung)
- Bei gemeinnuetzigen Zwecken
- Bei Konzern- und Holding-Strukturen
- Bei Family-Buy-In / Buy-Out
- Bei wirtschaftlicher Krise (Insolvenzantragspflicht Paragraf 15a InsO)
- Bei Gesellschafterstreit mit Klage-Vorbereitung

## Zitierweise

Sämtliche Zitierweise-Vorgaben folgen `references/zitierweise.md` des übergeordneten Repositories `claude-fuer-deutsches-recht`. Jede juristische Aussage wird belegt.

## Aktualitaet (Stand 2026)

Beruecksichtigt:

- **MoPeG** (Modernisierung Personengesellschaftsrecht, 1.1.2024) — eGbR-Eintragung, Pflicht bei Grundstuecksgeschaeften
- **DiRUG** (Digitalisierungsrichtlinie-Umsetzungsgesetz, 1.8.2022) — Online-Gruendung
- **TraFinG** (2021) — Transparenzregister als Vollregister
- **GwG**-Novellen — wirtschaftlich Berechtigter, Bussgeld bis 150.000 EUR
- **BGH Kali+Salz** (BGHZ 71, 40) — Bezugsrechtsausschluss-Linie
- **BGH Macrotron** (BGH NJW 2005, 985) — Bezugsrecht-Schutz
- **BGH NJW 2007, 917 / 2018, 1233** — Treuepflicht in Kapitalgesellschaften

## Tipps fuer die Bearbeitung

1. **Zeit einplanen**: Eine GmbH-Gruendung dauert 4-8 Wochen, eine GmbH & Co. KG 6-10 Wochen, eine AG 8-12 Wochen.

2. **Rechtsform-Beratung vor Notar**: Wer falsch waehlt, korrigiert spaeter teuer per Umwandlungsverfahren.

3. **Steuerberater frueh einbinden**: insbesondere fuer Vorauszahlungs-Schaetzung und USt-Wahl.

4. **TraFinG nicht vergessen**: bei Konto-Eroeffnung wird die Bank pruefen.

5. **D&O-Versicherung von Anfang an**: GF-Haftung Paragraf 43 GmbHG ist real.

6. **Vesting fuer Gruender**: Vermeidet Frust, wenn ein Gruender nach 6 Monaten ausscheidet.

7. **Bezugsrechte ernst nehmen**: Bei Kapitalerhoehung **immer** Bezugsrechte anbieten — sonst Anfechtungs-Risiko.

8. **Beirat als Schlichter**: Vor Klage anrufen, wenn vorgesehen.

9. **Bilinguale Dokumente**: Deutsche Fassung geht vor.

10. **Fristen sind unverzeihlich**: Insolvenzantrag binnen 3 Wochen, Anfechtungsklage binnen 1 Monat, BG binnen 1 Woche.
