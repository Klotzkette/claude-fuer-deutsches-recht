# gesellschaftsgruender — Gruendungsassistent fuer deutsche Gesellschaften

Freistehendes Plugin, das durch die Gruendung einer deutschen Gesellschaft fuehrt — von der Rechtsformwahl ueber den Notarsitz, das Handelsregister, Behoerdenanmeldungen bis hin zu den ersten 100 Tagen Geschaeftsfuehrer-Pflichten.

## Mandatsperspektive

**Du als Anwalt, Steuerberater, Gruender oder Notarberater.** Das Plugin

- klaert die **Rechtsformwahl** (GmbH, UG, GbR, OHG, KG, GmbH & Co. KG, AG, PartG, gGmbH, eK),
- bereitet die **Notarsitzung** vor,
- begleitet die **Handelsregister-Anmeldung**,
- koordiniert die **Behoerden-Anmeldungen** (Gewerbeamt, Finanzamt, IHK, Berufsgenossenschaft, Transparenzregister),
- liefert eine **erste 100-Tage-Checkliste** fuer den Geschaeftsfuehrer.

Berueksichtigt aktuelle Gesetzeslage Stand 2026 inkl. **MoPeG** (Modernisierung Personengesellschaftsrecht, Januar 2024) und **DiRUG** (Online-Gruendung per Videokonferenz, August 2022).

## Aufbau

Der Lebenszyklus einer Gruendung laeuft in fuenf Phasen:

```
Phase 0 — Rechtsformwahl (Woche 1)
  └─ GmbH vs. UG vs. GbR vs. KG vs. AG vs. ... — Entscheidung mit Begruendung

Phase A — Vorbereitung (Woche 2-3)
  └─ Gesellschafterstruktur, Firmenname, Sitz, Gegenstand, Stammkapital

Phase B — Vertraege (Woche 3-4)
  └─ Gesellschaftsvertrag/Satzung
     Gesellschaftervereinbarung (SHA mit Vesting, Drag/Tag, Liquidation Preference)
     Geschaeftsfuehrer-Anstellungsvertrag

Phase C — Notar + Handelsregister (Woche 4-6)
  └─ Beurkundung (physisch oder online nach DiRUG)
     Stammkapital-Einzahlung
     Anmeldung beim Handelsregister
     Eintragung

Phase D — Behoerden und operativer Start (Woche 6-8)
  └─ Gewerbeamt, Finanzamt-Erfassung, IHK, BG, Transparenzregister
     Geschaeftskonto, Buchhaltung, Compliance-Aufbau
     Erste 100 Tage Geschaeftsfuehrer-Pflichten
```

## Enthaltene Skills (17)

### Phase 0 — Rechtsformwahl (2 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-kommandocenter` | Master-Workflow mit Fristen Beteiligten Kosten |
| `gesellschaftsgruender-rechtsformwahl` | Entscheidungsmatrix GmbH/UG/GbR/OHG/KG/AG/PartG/gGmbH/eK |

### Phase A — Vorbereitung (4 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gmbh-vorbereitung` | Sieben Bausteine: Firma, Sitz, Gegenstand, Stammkapital, Gesellschafter, GF, Satzung |
| `gesellschaftsgruender-ug-vorbereitung` | UG-Spezifika, Thesaurierungspflicht Paragraf 5a III GmbHG |
| `gesellschaftsgruender-egbr-mopeg` | GbR nach MoPeG 2024, Gesellschaftsregister, Pflichteintragung bei Grundstuecksgeschaeften |
| `gesellschaftsgruender-kg-und-gmbhcokg` | KG und GmbH & Co. KG, Komplementaer/Kommanditist, Hafteinlage |

### Phase B — Vertraege (3 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gesellschaftsvertrag-gmbh` | Satzung mit Pflicht- und Standard-Klauseln, Musterprotokoll vs. individuell |
| `gesellschaftsgruender-gesellschaftervereinbarung` | SHA: Vesting, Leaver, Drag/Tag, Liquidation Preference, Anti-Dilution |
| `gesellschaftsgruender-geschaeftsfuehrervertrag` | GF-Anstellung: Vergueutung, Wettbewerbsverbot, D&O, SV-Status, vGA-Risiken |

### Phase C — Notar und Handelsregister (3 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-notar-vorbereitung` | Notarsitzung: Unterlagen, Kosten GNotKG, Sacheinlage-Vorbereitung |
| `gesellschaftsgruender-online-gruendung-dirug` | DiRUG-Online-Gruendung per Videokonferenz seit August 2022 |
| `gesellschaftsgruender-handelsregister-anmeldung` | Anmeldung, Versicherungen Paragraf 8 II GmbHG, Vor-GmbH, Gesellschafterliste |

### Phase D — Behoerden und Start (5 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschaftsgruender-gewerbeanmeldung-finanzamt` | Gewerbeamt Paragraf 14 GewO, Fragebogen ELSTER, USt-Wahl, Kleinunternehmer |
| `gesellschaftsgruender-transparenzregister` | TraFinG-Meldung, wirtschaftlich Berechtigter, Sonderkonstellationen |
| `gesellschaftsgruender-ihk-und-berufsgenossenschaft` | IHK/HwK-Pflicht, BG binnen 1 Woche, Freiberufler-Spezifika |
| `gesellschaftsgruender-stammkapital-einzahlung` | Bareinlage, freie Verfuegung Paragraf 7 II 2 GmbHG, Hin- und Herzahlen verboten |
| `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` | Erste 100 Tage: Buchhaltung, Steuern, SV, Compliance, Haftung Paragraf 43 GmbHG |

## Pluginscope und Stoppschilder

### Was das Plugin macht

- Strukturen und Schemata vermitteln
- Pflicht- und Soll-Inhalte erklaeren
- Fristen und Beteiligte aufstellen
- Typische Fallstricke benennen
- Praktische Schritt-fuer-Schritt-Anleitungen

### Was das Plugin NICHT macht

- **Keine Notar-Beurkundung**: muss vor Notar erfolgen
- **Keine Steuerberatung**: Steuerberater fuer Mandate erforderlich
- **Keine Vertretung im Streit**: Anwalt fuer Konflikt-Mandate

### Wann zwingend Anwalt / Notar / Steuerberater

- Bei Sacheinlagen mit Werthaltigkeits-Risiko (Differenzhaftung Paragraf 9 GmbHG)
- Bei Beteiligung von Auslandsgesellschaftern (Sanktionsrecht, Investitionspruefung)
- Bei gemeinnuetzigen Zwecken (Voraussetzungen Paragrafen 52-68 AO)
- Bei Konzern- und Holding-Strukturen
- Bei Family-Buy-In / Buy-Out
- Bei wirtschaftlicher Krise (Insolvenzantragspflicht Paragraf 15a InsO)

## Zitierweise

Sämtliche Zitierweise-Vorgaben folgen `references/zitierweise.md` des übergeordneten Repositories `claude-fuer-deutsches-recht`. Jede juristische Aussage wird belegt.

## Aktualitaet (Stand 2026)

Beruecksichtigt:

- **MoPeG** (Modernisierung Personengesellschaftsrecht, 1.1.2024) — eGbR-Eintragung, Pflicht bei Grundstuecksgeschaeften
- **DiRUG** (Digitalisierungsrichtlinie-Umsetzungsgesetz, 1.8.2022) — Online-Gruendung GmbH/UG
- **TraFinG** (2021) — Transparenzregister als Vollregister
- **GWG**-Novellen — wirtschaftlich Berechtigter, Bussgeldrahmen bis 150.000 EUR
- **Geldwaesche-Strafrecht** Paragraf 261 StGB

## Tipps fuer die Bearbeitung

1. **Zeit einplanen**: Eine GmbH-Gruendung dauert 4-8 Wochen, eine GmbH & Co. KG 6-10 Wochen, eine AG 8-12 Wochen.

2. **Rechtsform-Beratung vor Notar**: Wer falsch waehlt, korrigiert spaeter teuer per Umwandlungsverfahren.

3. **Steuerberater frueh einbinden**: insbesondere fuer Vorauszahlungs-Schaetzung und USt-Wahl.

4. **TraFinG nicht vergessen**: bei Konto-Eroeffnung wird die Bank pruefen.

5. **D&O-Versicherung von Anfang an**: GF-Haftung Paragraf 43 GmbHG ist real.

6. **Fristen sind unverzeihlich**: Insolvenzantrag binnen 3 Wochen, BG binnen 1 Woche, Fragebogen Finanzamt binnen 1 Monat.
