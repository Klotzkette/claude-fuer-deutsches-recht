# gesellschaftsgründer — Gründungsassistent für deutsche Gesellschaften

Freistehendes Plugin, das durch die Gründung einer deutschen Gesellschaft führt — von der Rechtsformwahl über Cap Table, Class-Shares, Notar, Handelsregister, Behördenanmeldungen bis hin zu den ersten 100 Tagen Geschäftsführer-Pflichten und Streit-Eskalationen.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| gesellschaftsgründer | [gesellschaftsgruender.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsgruender.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **"Roeschen Tech GmbH" — Gesellschaftsgründung mit B-Shares und Streit-Eskalation** ([`testakten/gesellschaftsgruender-streit-roeschen-tech/`](../testakten/gesellschaftsgruender-streit-roeschen-tech/)).

Direkt-Download als ZIP: [testakte-gesellschaftsgruender-streit-roeschen-tech.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `gesellschaftsgruender.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte die Gesellschaftsgruendung. Rechtsform: GmbH. Drei Gruender, zwei davon im Ausland.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install gesellschaftsgruender@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und das Verzeichnis `skills/` enthalten.

## Arbeitsakte (Direkt-Download)

- **Streit Roeschen Tech GmbH i.Gr.** (Drei-Gründer-Streit mit Vesting/SHA/Class-Shares): [testakten/gesellschaftsgruender-streit-roeschen-tech/](../testakten/gesellschaftsgruender-streit-roeschen-tech/) -> [testakte-gesellschaftsgruender-streit-roeschen-tech.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip)

Details zur Arbeitsakte stehen weiter unten.

## Mandatsperspektive

**Du als Anwalt, Steuerberater, Gründer oder Notarberater.** Das Plugin

- erfasst die **Gründer-Eckdaten** strukturiert,
- klärt die **Rechtsformwahl** (GmbH, UG, GbR, OHG, KG, GmbH & Co. KG, AG, PartG, gGmbH, eK),
- entwickelt **Cap Table** mit Pre/Post-Money und Verwässerungs-Simulation,
- liefert **Class-Shares** (A/B/C/Common) mit Liquidation Preference,
- erstellt **Gesellschaftervereinbarung (SHA)** mit Vesting, Drag/Tag, Stimmverpflichtungen,
- bereitet die **Notarsitzung** vor (auch DiRUG-online),
- begleitet die **Handelsregister-Anmeldung**,
- koordiniert die **Behörden-Anmeldungen** (Gewerbe, Finanzamt, IHK, BG, TraFinG),
- liefert eine **Geschäftsordnung der Geschäftsführung** und Meeting-Templates,
- erstellt **Gesellschafterversammlungs-Einladungen** und **Protokolle**,
- vermittelt **bilinguale Dokumente** Deutsch/Englisch,
- klärt den **Sozialversicherungs-Status** des Geschäftsführers,
- begleitet **Gesellschafterstreit** mit Eilanträgen LG und Registergericht,
- prüft den **Firmennamen** (HR, IHK, DPMA, EUIPO),
- liefert eine **erste 100-Tage-Checkliste** für den Geschäftsführer.

Berücksichtigt aktuelle Gesetzeslage Stand 2026 inkl. **MoPeG** (Modernisierung Personengesellschaftsrecht, Januar 2024) und **DiRUG** (Online-Gründung per Videokonferenz, August 2022).

## Aufbau

Der Lebenszyklus einer Gründung läuft in fünf Phasen:

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

## Enthaltene Skills (37)

### Phase 0 — Intake und Rechtsformwahl (5 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-kommandocenter` | Master-Workflow mit Fristen Beteiligten Kosten |
| `gesellschaftsgruender-gruender-intake` | Strukturierte Eingangs-Abfrage Gründer Anteile Class-Shares Geschäftsmodell |
| `gesellschaftsgruender-rechtsformwahl` | Entscheidungsmatrix GmbH/UG/GbR/OHG/KG/AG/PartG/gGmbH/eK |
| `gesellschaftsgruender-firmenname-pruefung` | HR DPMA EUIPO Domain Verwechslungsgefahr Irreführungsverbot |
| `gesellschaftsgruender-cap-table` | Capitalization Table Pre/Post-Money Verwässerung Liquidation-Waterfall |

### Phase A — Strukturen und Sondervetorechte (4 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gmbh-vorbereitung` | Sieben Bausteine: Firma Sitz Gegenstand Stammkapital Anteile GF Satzungswahl |
| `gesellschaftsgruender-ug-vorbereitung` | UG-Spezifika Thesaurierungspflicht Paragraf 5a III GmbHG |
| `gesellschaftsgruender-egbr-mopeg` | GbR nach MoPeG 2024 Gesellschaftsregister Pflichteintragung Grundstücksgeschäfte |
| `gesellschaftsgruender-kg-und-gmbhcokg` | KG und GmbH und Co KG Komplementär Kommanditist Hafteinlage |
| `gesellschaftsgruender-share-classes-a-b-c` | Anteilsklassen A/B/C Common Liquidation Preference Anti-Dilution |
| `gesellschaftsgruender-golden-share-und-vetorechte` | Golden Share Sperrminorität Vetorechte Restrukturierung |

### Phase B — Verträge und Geschäftsordnung (8 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gesellschaftsvertrag-gmbh` | Satzung mit Pflicht-/Standard-Klauseln Musterprotokoll vs individuell |
| `gesellschaftsgruender-gesellschaftervereinbarung` | SHA: Vesting Leaver Drag Tag Liquidation Anti-Dilution Pönalen |
| `gesellschaftsgruender-sha-satzung-stimmverpflichtung` | Stimmverpflichtung Innenverhältnis Joinder Agreement Pönalen |
| `gesellschaftsgruender-geschaeftsfuehrervertrag` | GF-Anstellung Vergütung Wettbewerb D&O SV-Status vGA |
| `gesellschaftsgruender-gf-sozialversicherungs-status` | Fremd-GF Mehrheits-/Minderheits-GF Statusfeststellung Paragraf 7a SGB IV |
| `gesellschaftsgruender-geschaeftsordnung-gf` | Geschäftsordnung der Geschäftsführung Zustimmungs-Kataloge |
| `gesellschaftsgruender-gf-meeting-templates` | Tagesordnung Einladung Protokoll Umlauf-Beschluss bilingual |
| `gesellschaftsgruender-beirat-advisory-board` | Beirat Advisory Board Beiratsordnung Schlichtungs-Funktion |
| `gesellschaftsgruender-bilinguale-dokumente` | Deutsch und Englisch parallel Vorrang-Klausel Übersetzungs-Fallen |
| `gesellschaftsgruender-klauselkatalog-bilingual` | Volltextliche DE/EN-Klauseln Stimmbindung Golden-Share-StaRUG-Veto BSG-feste Sperrminorität Drag Tag Liquidation Preference Anti-Dilution Vesting Bad-Leaver Koppelung Wettbewerbsverbot |
| `gesellschaftsgruender-intake-decision-tree` | Mermaid-Decision-Tree für Intake conditional logic Knoten Trigger-Events Workflow-Engine-Architektur |

### Phase C — Notar und Handelsregister (3 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-notar-vorbereitung` | Notarsitzung Unterlagen GNotKG-Kosten Sacheinlage |
| `gesellschaftsgruender-online-gruendung-dirug` | DiRUG-Online-Gründung Videokonferenz seit August 2022 |
| `gesellschaftsgruender-handelsregister-anmeldung` | Anmeldung Versicherungen Paragraf 8 II GmbHG Vor-GmbH |

### Phase D — Behörden und Start (5 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gewerbeanmeldung-finanzamt` | Gewerbeamt Paragraf 14 GewO ELSTER USt-Wahl Kleinunternehmer |
| `gesellschaftsgruender-transparenzregister` | TraFinG wirtschaftlich Berechtigter Bußgeld bis 150000 EUR |
| `gesellschaftsgruender-ihk-und-berufsgenossenschaft` | IHK HwK BG binnen 1 Woche Freiberufler-Spezifika |
| `gesellschaftsgruender-stammkapital-einzahlung` | Bareinlage freie Verfügung Paragraf 7 II 2 GmbHG Hin-und-Herzahlen verboten |
| `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` | Erste 100 Tage Buchhaltung Steuern SV Compliance Haftung Paragraf 43 GmbHG |

### Phase E — GV und Konflikt-Mass nahmen (5 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gv-einladung-tagesordnung` | Einladung Paragraf 51 GmbHG Frist Form Tagesordnung Beschluss-Vorlage |
| `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` | Protokoll Versammlungsleiter Wahl Streit notarielle Beurkundung |
| `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` | Pflichtversammlung bei Verlust Hälfte Stammkapital |
| `gesellschaftsgruender-genehmigtes-kapital` | Vorratsbeschluss Paragraf 55a GmbHG bis 50% des Stammkapitals 5 Jahre |
| `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` | Kapitalerhöhung Bezugsrecht Bezugsrechtsausschluss BGH-Linie Kali-Salz |
| `gesellschaftsgruender-gesellschafterstreit-eilantraege` | Einstweilige Verfügung LG Anmeldungs-Sperre Registergericht Anfechtungsklage |

## Arbeitsakte

Im Verzeichnis `testakten/gesellschaftsgruender-streit-roeschen-tech/` befindet sich eine **vollständige Arbeitsakte** zum Gesellschafterstreit der Roeschen Tech GmbH:

- Gründung mit drei Gründern und Stammkapital 30.000 EUR
- Series-A-Aufnahme von Stahlauge Ventures AG mit B-Shares
- 2. Kapitalerhöhung mit Bezugsrechtsausschluss zugunsten Pi Mu Holding GmbH
- **Streit** der Minderheits-Gesellschafterin Christine Linnenbach mit Anfechtungsklage, Eilantrag LG, Anmeldungs-Sperre Registergericht
- Schlichtung durch Beirat

Enthält:

- Vollständige Satzung
- Shareholder Agreement
- Cap Table (Stand 1-4)
- Einladung und Protokoll der streitigen GV
- Anfechtungsklage und Eilanträge
- Beirat-Schlichtungs-Empfehlung
- Prüfvermerk mit Lernzielen und Aufgaben

## Pluginscope und Stoppschilder

### Was das Plugin macht

- Strukturen und Schemata vermitteln
- Pflicht- und Soll-Inhalte erklären
- Fristen und Beteiligte aufstellen
- Typische Fallstricke benennen
- Praktische Schritt-für-Schritt-Anleitungen
- Bilinguale Vorlagen (Deutsch/Englisch)
- Konflikt-Werkzeuge (Eilanträge, Anfechtungsklagen)

### Was nicht

- **Keine Notar-Beurkundung** (muss vor Notar erfolgen)
- **Keine Steuerberatung** (Steuerberater zwingend bei Mandaten)
- **Keine Vertretung im Streit** (Anwalt bei Konflikt-Mandaten)
- **Kein Mandanten-Vertretungs-Vertrag** mit Pflichten zur Schweigepflicht

### Wann zwingend Anwalt / Notar / Steuerberater

- Bei Sacheinlagen mit Werthaltigkeits-Risiko (Differenzhaftung Paragraf 9 GmbHG)
- Bei Beteiligung von Auslandsgesellschaftern (Sanktionsrecht, Investitionsprüfung)
- Bei gemeinnützigen Zwecken
- Bei Konzern- und Holding-Strukturen
- Bei Family-Buy-In / Buy-Out
- Bei wirtschaftlicher Krise (Insolvenzantragspflicht Paragraf 15a InsO)
- Bei Gesellschafterstreit mit Klage-Vorbereitung

## Zitierweise

Sämtliche Zitierweise-Vorgaben folgen `references/zitierweise.md` des übergeordneten Repositories `claude-fuer-deutsches-recht`. Jede juristische Aussage wird belegt.

## Aktualität (Stand 2026)

Berücksichtigt:

- **MoPeG** (Modernisierung Personengesellschaftsrecht, 1.1.2024) — eGbR-Eintragung, Pflicht bei Grundstücksgeschäften
- **DiRUG** (Digitalisierungsrichtlinie-Umsetzungsgesetz, 1.8.2022) — Online-Gründung
- **TraFinG** (2021) — Transparenzregister als Vollregister
- **GwG**-Novellen — wirtschaftlich Berechtigter, Bußgeld bis 150.000 EUR
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Tipps für die Bearbeitung

1. **Zeit einplanen**: Eine GmbH-Gründung dauert 4-8 Wochen, eine GmbH & Co. KG 6-10 Wochen, eine AG 8-12 Wochen.

2. **Rechtsform-Beratung vor Notar**: Wer falsch wählt, korrigiert später teuer per Umwandlungsverfahren.

3. **Steuerberater früh einbinden**: insbesondere für Vorauszahlungs-Schätzung und USt-Wahl.

4. **TraFinG nicht vergessen**: bei Konto-Eröffnung wird die Bank prüfen.

5. **D&O-Versicherung von Anfang an**: GF-Haftung Paragraf 43 GmbHG ist real.

6. **Vesting für Gründer**: Vermeidet Frust, wenn ein Gründer nach 6 Monaten ausscheidet.

7. **Bezugsrechte ernst nehmen**: Bei Kapitalerhöhung **immer** Bezugsrechte anbieten — sonst Anfechtungs-Risiko.

8. **Beirat als Schlichter**: Vor Klage anrufen, wenn vorgesehen.

9. **Bilinguale Dokumente**: Deutsche Fassung geht vor.

10. **Fristen sind unverzeihlich**: Insolvenzantrag binnen 3 Wochen, Anfechtungsklage binnen 1 Monat, BG binnen 1 Woche.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 37 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Gesellschaftsgruender-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `gesellschaftsgruender-beirat-advisory-board` | Beirat oder Advisory Board für GmbH oder UG einrichten: Satzungsregelung, Bestellungsverfahren, Beratungsvertrag. Normen: §§ 45 52 GmbHG, §§ 95 ff. AktG analog. Prüfraster: Kompetenzen, Verguetung, Haftung, Abberufung, Datenschutz. Outpu... |
| `gesellschaftsgruender-bilinguale-dokumente` | Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen: zweisprachige Satzung, Gesellschafterbeschluss, SHA. Normen: §§ 2 3 GmbHG, HGB. Prüfraster: rechtliche Verbindlichkeit der deutschen Fassung, Abweichungsregelung, Notar... |
| `gesellschaftsgruender-cap-table` | Cap-Table für GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Prüfraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output: Cap-Table-Tabelle m... |
| `gesellschaftsgruender-egbr-mopeg` | GbR nach MoPeG 2024 und Eintragung ins Gesellschaftsregister als eGbR vorbereiten. Normen: §§ 705 ff. BGB n.F. MoPeG, §§ 707 ff. BGB Gesellschaftsregister. Prüfraster: Eintragungsvoraussetzungen, Gesellschafterverzeichnis, Vertretungsreg... |
| `gesellschaftsgruender-firmenname-pruefung` | Firmenname auf Zulässigkeit und Verwechslungsgefahr prüfen: Differenzierungsgebot, Irreführungsverbot. Normen: §§ 17 18 HGB, § 4 GmbHG. Prüfraster: Unterscheidungskraft, Irreführungsverbot, Handelsregisterfähigkeit, Markenrecherche-Empfe... |
| `gesellschaftsgruender-genehmigtes-kapital` | Genehmigtes Kapital für GmbH oder AG in Satzung aufnehmen: Ermaechtigungsbeschluss, Hoechstbetrag, Bezugsrechtsausschluss. Normen: §§ 55a GmbHG, §§ 202 ff. AktG. Prüfraster: Ermaechtigungsrahmen, Fristen, Bezugsrechte, Eintragungserforde... |
| `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` | Pflichten des GmbH-Geschäftsführers in Gründungs- und Startphase: Stammkapitaleinzahlung, Insolvenzantragspflicht, Buchführung. Normen: §§ 35 43 64 GmbHG, § 15a InsO. Prüfraster: Handlungspflichten, Haftungsrisiken, Compliance-Checkliste... |
| `gesellschaftsgruender-geschaeftsfuehrervertrag` | Geschäftsführervertrag für GmbH-Geschäftsführer aufsetzen: Verguetung, Wettbewerbsverbot, Abberufung, Kündigungsfristen. Normen: §§ 35 38 GmbHG, BGB Dienstvertrag. Prüfraster: Verguetungsstruktur, Tantieme, Freistellung, Geheimhaltung, P... |
| `gesellschaftsgruender-geschaeftsordnung-gf` | Geschäftsordnung für GmbH-Geschäftsführung entwerfen: Ressortzuteilung, Zustimmungsvorbehalte, Berichtspflichten. Normen: §§ 35 37 GmbHG. Prüfraster: Kompetenzbereiche, interne Beschraenkungen, Zustimmungskataloge. Output: Geschäftsordnu... |
| `gesellschaftsgruender-gesellschafterstreit-eilantraege` | Eilmassnahmen im Gesellschafterstreit der GmbH: einstweilige Verfuegung gegen Mitgesellschafter oder Geschäftsführer. Normen: §§ 935 940 ZPO, §§ 37 38 GmbHG. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Arrest vs. einstweilige Verf... |
| `gesellschaftsgruender-gesellschaftervereinbarung` | Gesellschaftervereinbarung (SHA) neben dem Gesellschaftsvertrag entwerfen: Vorkaufsrechte, Drag-Along, Tag-Along. Normen: §§ 705 ff. BGB, GmbHG. Prüfraster: schuldrechtliche Bindung, Satzungsrang, Durchsetzbarkeit, Vertragsstrafe. Output... |
| `gesellschaftsgruender-gesellschaftsvertrag-gmbh` | GmbH-Gesellschaftsvertrag aufsetzen: Mindestinhalt, Stammkapital, Beschlussfassung, Gewinnverteilung. Normen: §§ 2 3 5 GmbHG. Prüfraster: Notarerfordernis, Pflichtinhalte, Optionalklauseln, Sonderrechte. Output: GmbH-Gesellschaftsvertrag... |
| `gesellschaftsgruender-gewerbeanmeldung-finanzamt` | Gewerbeanmeldung und steuerliche Ersterfassung nach GmbH-Gründung vorbereiten: Fragebogen Finanzamt, Gewerbeamt. Normen: § 14 GewO, AO, UStG. Prüfraster: Steuerklassen, USt-Voranmeldung, Betriebsstaette, Umsatzsteuer-ID. Output: Ausfuell... |
| `gesellschaftsgruender-gf-meeting-templates` | Vorlagen für Geschäftsführersitzungen und Protokolle erstellen: Tagesordnung, Beschlussprotokoll, Aktionsliste. Normen: §§ 35 ff. GmbHG. Prüfraster: Beschlussfähigkeit, Umlaufverfahren, Dokumentationspflichten. Output: Meeting-Templates... |
| `gesellschaftsgruender-gf-sozialversicherungs-status` | Sozialversicherungsrechtlichen Status des GmbH-Geschäftsführers klaeren: Pflichtversicherung vs. Befreiung bei beherrschendem Gesellschafter-GF. Normen: § 7 SGB IV, §§ 1 ff. SGB VI. Prüfraster: Beteiligungshoehe, Weisungsabhaengigkeit, B... |
| `gesellschaftsgruender-gmbh-vorbereitung` | GmbH-Gründung vorbereiten: Gründerprüfung, Kapitalplanung, Notar-Auftrag, Gesellschafterliste. Normen: §§ 2 3 5 7 GmbHG. Prüfraster: Mindestkapital 25000 Euro, Einzahlungsnachweis, Gesellschafterkreis, Geschäftsführereignung. Output: Vor... |
| `gesellschaftsgruender-golden-share-und-vetorechte` | Golden Shares und Vetorechte in GmbH oder AG satzungsmäßig absichern: Sonderrechte, Sperrminoritaeten. Normen: §§ 35 45 GmbHG, §§ 23 ff. AktG. Prüfraster: Satzungsgestaltung, Grenzen der Satzungsautonomie, Bestandsschutz, Vinkulierung. O... |
| `gesellschaftsgruender-gruender-intake` | Ersterfassung des Gründungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschäftszweck. Normen: GmbHG, AktG, HGB. Prüfraster: Intake-Fragen Rechtsformwahl, Haftung, steuerliche Aspekte, Zeitplan. Output: Gründungsintake-Bogen. Ab... |
| `gesellschaftsgruender-gv-einladung-tagesordnung` | Gesellschafterversammlungs-Einladung und Tagesordnung nach GmbHG erstellen: Fristen, Formen, Mindestinhalt. Normen: §§ 49 51 GmbHG. Prüfraster: Ladungsfrist, Schriftform, Tagesordnungspunkte, Beschlussfähigkeit. Output: GV-Einladungsschr... |
| `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` | Gesellschafterversammlungs-Protokoll anfertigen und Versammlungsleitung durchführen. Normen: §§ 48 ff. GmbHG. Prüfraster: Protokollierungspflicht, Abstimmungsergebnis, Unterschriften, Formfehler. Output: GV-Protokoll-Vorlage. Abgrenzung:... |
| `gesellschaftsgruender-handelsregister-anmeldung` | Erstanmeldung der GmbH zum Handelsregister vorbereiten: Notarauftrag, Eintragungsvoraussetzungen, Gründungsunterlagen. Normen: §§ 7 ff. GmbHG, §§ 12 ff. HGB. Prüfraster: Einzahlungsnachweis, Notarbeglaubigung, Gesellschafterliste, HR-For... |
| `gesellschaftsgruender-ihk-und-berufsgenossenschaft` | IHK-Pflichtmitgliedschaft und Berufsgenossenschafts-Anmeldung nach GmbH-Gründung erledigen. Normen: §§ 2 ff. IHKG, §§ 150 ff. SGB VII. Prüfraster: Branchenzuordnung BG, IHK-Beitragspflicht, Fristen. Output: Checkliste IHK-Anmeldung und B... |
| `gesellschaftsgruender-intake-decision-tree` | Entscheidungsbaum für GmbH-Gründung: Rechtsformwahl, Gründungsweg, Kapitalausstattung. Normen: GmbHG, AktG, PartGG, HGB. Prüfraster: Haftung, Steuer, Kapital, Gesellschafteranzahl. Output: Entscheidungsmatrix Rechtsformwahl. Abgrenzung:... |
| `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` | Kapitalerhöhung der GmbH mit und ohne Bezugsrecht der Gesellschafter durchführen. Normen: §§ 55 56 56a GmbHG. Prüfraster: Gesellschafterbeschluss, Bezugsrechtsausschluss, Einlageverpflichtung, Handelsregisteranmeldung. Output: Beschlussv... |
| `gesellschaftsgruender-kg-und-gmbhcokg` | KG und GmbH und Co. KG gründen: Gesellschaftsvertrag, Haftungsstruktur, steuerliche Transparenz. Normen: §§ 161 ff. HGB, GmbHG. Prüfraster: Komplementaer-GmbH, Kommanditistenstellung, steuerliche Behandlung. Output: KG-Gesellschaftsvertr... |
| `gesellschaftsgruender-klauselkatalog-bilingual` | Klauselkatalog für GmbH-Satzung und SHA in Deutsch und Englisch: Standardklauseln für internationale Investoren. Normen: GmbHG, BGB. Prüfraster: Drag-Along, Tag-Along, Liquidationspräferenzen, Leaver-Klauseln. Output: Klauselkatalog bili... |
| `gesellschaftsgruender-kommandocenter` | Navigationszentrum für alle Gründungs-Skills: Fortschrittsanzeige, Delegierung an Fachinhalte, Status. Normen: GmbHG, AktG, HGB. Prüfraster: aktueller Gründungsstand, offene Schritte, Notartermin, Eintragungsstatus. Output: Statusuebersi... |
| `gesellschaftsgruender-notar-vorbereitung` | Notartermin für GmbH-Gründung vorbereiten: Unterlagencheck, Vollmachten, Ausweisanforderungen. Normen: §§ 2 7 GmbHG, BeurkG. Prüfraster: Gesellschafterliste, Musterprotokoll vs. individueller Gesellschaftsvertrag, Vollmachten. Output: No... |
| `gesellschaftsgruender-online-gruendung-dirug` | Online-Gründung der GmbH nach DiRUG ohne persoenlichen Notartermin: Voraussetzungen, Verfahren, Grenzen. Normen: § 2 Abs. 3 GmbHG, DiRUG. Prüfraster: Musterprotokoll-Pflicht, Videoidentifikation, Beschraenkungen. Output: Checkliste Onlin... |
| `gesellschaftsgruender-rechtsformwahl` | Rechtsformwahl für Unternehmen: GmbH, UG, AG, GbR, PartG, KG, SE im Vergleich. Normen: GmbHG, AktG, PartGG, HGB, SE-VO. Prüfraster: Haftung, Steuern, Kapital, Mitbestimmung, Borsenreife. Output: Rechtsformvergleich-Matrix mit Empfehlung.... |
| `gesellschaftsgruender-sha-satzung-stimmverpflichtung` | Stimmbindungsvereinbarung und SHA-Regelungen zu Abstimmungspflichten in GmbH aufsetzen. Normen: §§ 47 48 GmbHG, BGB. Prüfraster: zulässige Stimmbindung, Durchsetzbarkeit, Vertragsstrafe, Grenze Satzungsautonomie. Output: SHA-Klausel Stim... |
| `gesellschaftsgruender-share-classes-a-b-c` | Anteilsklassen A, B, C in GmbH oder AG gestalten: unterschiedliche Gewinn-, Stimm- und Liquidationsrechte. Normen: §§ 29 47 GmbHG, §§ 11 12 AktG. Prüfraster: Satzungsgestaltung, steuerliche Wirkung, Investorenerwartungen. Output: Satzung... |
| `gesellschaftsgruender-stammkapital-einzahlung` | Stammkapitaleinzahlung bei GmbH-Gründung nachweisen: Mindesteinzahlung, Bankbescheinigung, Sacheinlage. Normen: §§ 7 Abs. 2 und 19 GmbHG. Prüfraster: Mindesteinzahlung 50 Prozent, Bankbescheinigung, Sacheinlageprüfung, verdeckte Sacheinl... |
| `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` | Hälftiger Stammkapitalverlust nach § 49 Abs. 3 GmbHG: Einberufungspflicht und Insolvenzprüfung. Normen: §§ 49 Abs. 3 64 GmbHG, § 15a InsO. Prüfraster: Bilanzkennzahlen, Einberufungspflicht, Haftungsrisiken GF. Output: Stellungnahme Stamm... |
| `gesellschaftsgruender-transparenzregister` | Transparenzregister-Meldung für GmbH oder UG: wirtschaftlich Berechtigte, Fristen, Bußgelder. Normen: §§ 18 ff. GwG, GeldwäscheG. Prüfraster: Identifikation wirtschaftlich Berechtigter, Meldepflicht, Meldefristen, Aktualisierungen. Outpu... |
| `gesellschaftsgruender-ug-vorbereitung` | UG haftungsbeschraenkt gründen: Musterprotokoll, Mindestkapital 1 Euro, Thesaurierungspflicht. Normen: § 5a GmbHG, §§ 2 3 GmbHG. Prüfraster: Stammkapital 1 Euro bis unter 25000 Euro, Musterprotokoll-Pflicht, Rücklagenbildung 25 Prozent J... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
