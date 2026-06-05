---
name: lease-flugzeugleasing-register-schiffsleasing
description: "Lease Flugzeugleasing Register Schiffsleasing: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Flugzeugleasing Register Schiffsleasing

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Flugzeugleasing Register Schiffsleasing** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-025-flugzeugleasing-register-pfand-und-wartung` | Flugzeug-Leasing: Luftfahrtregister, Kapstadt-Übereinkommen, Internationales Interesse, Wartung nach EASA, Rückgabe-Condition und Leasingstruktur. |
| `lease-026-schiffsleasing-schiffshypothek-und-flagge` | Schiffsleasing: Schiffsregister, Schiffshypothek, Flaggenrecht, internationale Leasingstruktur und Insolvenzbesonderheiten. |
| `lease-028-refinanzierung-forderungsabtretung-und-servicing` | Leasingrefinanzierung: Forderungsabtretung, ABS-Strukturen, True Sale, Servicing, stille Abtretung und Schuldnerschutz nach § 407 BGB. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Flugzeugleasing Register Schiffsleasing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-025-flugzeugleasing-register-pfand-und-wartung`

**Fokus:** Flugzeug-Leasing: Luftfahrtregister, Kapstadt-Übereinkommen, Internationales Interesse, Wartung nach EASA, Rückgabe-Condition und Leasingstruktur.

# Flugzeug-Leasing: Register, Pfand und Wartung

## Zweck

Flugzeug-Leasing ist ein hochspezialisiertes Segment mit eigenen Registern, internationalem Recht (Kapstadt-Übereinkommen) und strikten Wartungsanforderungen (EASA). Dieser Skill analysiert die relevanten Strukturen, Sicherungsrechte und typischen Vertragsklauseln.

## Rechtlicher Rahmen

- **Cape Town Convention (Kapstadt-Übereinkommen, 2001)**: Internationales Übereinkommen über mobile Ausrüstungen; Protokoll Luftfahrzeuge (2001); Deutschland ratifiziert 2015
- **LuftVG, LuftVZO**: Deutsches Luftfahrzeugrecht; Eintragungspflicht im Luftfahrzeugregister
- **EASA-VO (EG) 2018/1139**: Lufttüchtigkeit und Wartung
- **ICAO Annex 7**: Nationalitätskennzeichen; Eigentumsnachweis
- §§ 101 ff. LuftVG: Luftfahrzeugpfandrecht

## Luftfahrzeugregister

### Nationales Register (LBA / Luftfahrt-Bundesamt)
- Eintragung der Luftfahrzeuge nach Nationalitätskennzeichen (§ 3 LuftVZO)
- Eintragung des Eigentümers (oder Leasinggebers) und Betreibers (Leasingnehmer/Airline)
- Keine automatische Sicherungsrechts-Transparenz

### Kapstadt-Register: Internationales Interesse
- Kapstadt-Protokoll schafft internationales Interesse an Luftfahrzeugen
- Registrierung im International Registry (IR, Dublin): Priorität nach Registrierungsdatum
- Schutz des registrierten Gläubigers (LG / Refinanzierer) vor späteren Rechten Dritter

### Priorität der Sicherungsrechte
- First registered, first protected: Kapstadt-Prinzip
- LG muss „prospective international interest" anmelden, bevor LN das Luftfahrzeug erhält
- Ohne Registrierung: Kein Schutz nach Kapstadt-Übereinkommen

## Wartung nach EASA

### Kontinuierliche Lufttüchtigkeit (CAMO)
- EASA Part-M/Part-CAMO: Halter und/oder Betreiber müssen CAMO-Organisation aufbauen
- CAMO verantwortlich für: Wartungsplanung, AD/SB-Compliance, Gewichts- und Schwerpunktdokumentation
- Im Leasingvertrag: Wer ist CAMO-Verantwortlicher? LN als Betreiber

### Maintenance Reserve (MR)
- Leasingverträge enthalten oft Maintenance-Reserve-Klauseln: LN zahlt monatlich MR in Treuhandkonto
- MR deckt: Triebwerksüberholung, Fahrwerk-Overhaul, C-Check
- Bei Vertragsende: MR wird für Reparaturen verwendet; verbleibend zurück an LN

### Return Conditions (Rückgabebedingungen)
Typische Rückgabezustand-Anforderungen:
- Mindest-Triebwerkszeit bis nächstem Shop-Visit (z.B. 4.000 Flight Hours)
- Mindest-Airframe-Zeit
- No open MEL items (Minimum Equipment List)
- Vollständige technische Dokumentation (Log Books, AD Status)
- Exterieur: Keine Dellen/Risse über bestimmten Toleranzen

### Lease Return Compensation
- Wenn LN Rückgabebedingungen nicht erfüllt: Compensation Payment (vertraglich pauschaliert oder nach Gutachten)
- Andersherum: Übererfüllung → LN erhält Gutschrift aus MR-Rückstand

## Steuern: Dry-Lease vs. Wet-Lease

- **Dry Lease**: Nur Flugzeug geleast; Besatzung und Betrieb durch LN
- **Wet Lease** (ACMI): Flugzeug + Crew + Maintenance + Insurance; kurzfristig, hohe Rates
- Steuerliche Unterschiede: Wet-Lease kann als Dienstleistung (USt auf Gesamtleistung) eingestuft werden

## Insolvenz einer Airline

- Cape Town Convention Art. XI (Alternative A/B): Schutz des LG bei Insolvenz LN (Airline)
- Alternative A: LG kann Flugzeug innerhalb von 60 Tagen nach Insolvenzeröffnung zurückholen, sofern keine Zahlung durch Insolvenzverwalter
- Deutschland: Alternative A umgesetzt (§ 108a InsO)

## Prüfprogramm

1. Kapstadt-Registrierung: Internationales Interesse angemeldet?
2. Wartungsorganisation: Wer ist CAMO? LN verantwortlich?
3. Maintenance Reserve: Korrekte Einzahlungen, Treuhänder, Verwendung?
4. Rückgabebedingungen: Vertragsklauseln klar? Gutachtenverfahren vereinbart?
5. Insolvenz: Cape Town Alternative A aktiv? 60-Tage-Frist bekannt?
6. USt: Dry vs. Wet-Lease? Welcher USt-Satz/Leistungsort?

## Typische Fallen

- Kapstadt-Registrierung versäumt → kein Prioritätsschutz gegenüber Gläubigern
- MR-Konten nicht ordnungsgemäß geführt → Rückgabe-Dispute
- Rückgabebedingungen unklar → Langwieriger technischer Streit
- Insolvenz Airline: 60-Tage-Frist nach Alternative A verpasst → Masse behält Flugzeug länger

## Normen und Quellen

- Kapstadt-Übereinkommen / Cape Town Convention: https://www.unidroit.org
- LuftVG §§ 101 ff. (Luftfahrzeugpfandrecht): https://www.gesetze-im-internet.de/luftvg/
- EASA-VO (EG) 2018/1139: https://eur-lex.europa.eu
- § 108a InsO (Cape Town, Insolvenz Airline): https://www.gesetze-im-internet.de/inso/__108a.html
- ICAO Annex 7: https://www.icao.int
- LuftVZO: https://www.gesetze-im-internet.de/luftvzo/

## Output-Formate

- **Kapstadt-Registrierungsablauf**: Schritt-für-Schritt zum International Registry
- **Return-Conditions-Checkliste**: Technische Anforderungen bei Rückgabe
- **MR-Berechnung**: Monatliche Reserve nach Flight Hours und Cycle
- **Insolvenz-Airline-Plan**: Sofortmaßnahmen für LG nach Insolvenzantrag

## 2. `lease-026-schiffsleasing-schiffshypothek-und-flagge`

**Fokus:** Schiffsleasing: Schiffsregister, Schiffshypothek, Flaggenrecht, internationale Leasingstruktur und Insolvenzbesonderheiten.

# Schiffsleasing: Schiffsregister, Schiffshypothek und Flagge

## Zweck

Schiffsleasing verbindet Seerecht, Registerrecht und allgemeines Leasingrecht. Schiffe haben eigene Register und Sicherungsrechte (Schiffshypothek). Die Flagge des Schiffes bestimmt das anwendbare Recht für viele Fragen. Dieser Skill klärt die relevanten Strukturen.

## Rechtlicher Rahmen

- SchiffRG (Gesetz über Rechte an eingetragenen Schiffen und Schiffsbauwerken): §§ 1–107 SchiffRG
- SchiffsRegO (Schiffsregisterordnung)
- HGB §§ 476 ff. (Seehandelsrecht, Schiffsüberlassung)
- ISM-Code (International Safety Management): Betreiberverantwortung
- STCW (Standards of Training, Certification and Watchkeeping): Besatzungsanforderungen
- § 108 InsO: Leasingvertrag über unbewegliche Sachen (Schiff ≈ beweglich)

## Schiffsregister und Eigentum

### Eintragungspflicht
- Kauffahrteischiffe über 15 BRZ: Eintragungspflicht im Schiffsregister (§ 3 SchiffsRegO)
- Eintragung des Eigentümers (§ 3 SchiffsRegO)
- Publizitätswirkung: Gutgläubiger Erwerb nach Registerstand möglich (§§ 16, 17 SchiffRG)

### Eigentumsübertragung
- Einigung + Eintragung im Schiffsregister (§ 3 SchiffRG analog § 873 BGB für Immobilien)
- Sicherungsübereignung von Schiffen: Eintragung der Schiffshypothek

### Schiffshypothek
- §§ 8 ff. SchiffRG: Schiffshypothek als dingliches Sicherungsrecht
- Eintragung im Schiffsregister
- Rang nach Eintragungszeitpunkt
- Bei Insolvenz: Absonderungsrecht (§ 49 InsO)

## Flaggenrecht

### Bedeutung der Flagge
- Flagge = Nationalität des Schiffes; bestimmt anwendbares Recht an Bord
- Flaggenstaat-Kontrolle: Besatzungsvorschriften, Sicherheitsstandards, Zollrecht
- Open-Register-Staaten (Liberia, Panama, Marshall Islands): Günstige Registrierungsbedingungen, niedrige Steuern

### Bareboat Charter und Flaggenwechsel
- Bareboat Charter (ähnlich Dry Lease Schiff): LN (Charter) übernimmt volle Betriebsverantwortung
- Flaggenwechsel möglich: Bareboat Registration im Flaggenstaat des LN
- Doppelregistrierung: Eigentumsregister im Flaggenstaat des LG + Betriebsregistrierung im Flaggenstaat des LN

## Leasingstruktur für Schiffe

### Typische Struktur
1. Schifffahrtsgesellschaft (LN/Reederei) wählt Schiff
2. LG (Bank, Leasinggesellschaft) kauft Schiff vom Werftenlieferant
3. LG verleast Schiff an Reederei; Reederei betreibt das Schiff
4. LG finanziert über Schiffshypothek bei Bank

### KG-Modell (historisch)
Viele Schiffe in Deutschland: KG-Struktur (Kommanditgesellschaft als Schiffs-Eigentümer; Kommanditisten = Anleger). Leasingvertrag zwischen KG (LG) und Reederei (LN). Steuervorteile durch Tonnagesteuer (§ 5a EStG).

### Tonnagesteuer (§ 5a EStG)
- Pauschalbesteuerung nach Schiffsgröße (BRZ), nicht nach Gewinn
- Vorteil: Steuerersparnis bei profitablen Schiffen
- Nachteil: Keine Verlustverrechnung in Verlustjahren

## Insolvenz: Besonderheiten bei Schiffen

- § 108 InsO: Mietvertrag über unbewegliche Sachen → Schiffe sind beweglich; § 103 InsO gilt
- Insolvenzverwalter: Wahlrecht (Fortführung oder Ablehnung)
- LG: Aussonderungsrecht (Eigentumsrecht) nach § 47 InsO
- Schiffshypothek-Gläubiger: Absonderungsrecht (§ 49 InsO)

## Prüfprogramm

1. Schiff im Register eingetragen? LG als Eigentümer?
2. Schiffshypothek: Höhe, Rang, Gläubiger?
3. Flagge: Welches Recht gilt an Bord? Bareboat-Registration?
4. ISM-Code: Betreiber (LN) als Document of Compliance-Inhaber?
5. Insolvenz: Wahlrecht Verwalter; Aussonderungs- vs. Absonderungsrecht?
6. Tonnagesteuer: Anwendung auf Leasingverhältnis?

## Typische Fallen

- Eigentümer nicht im Schiffsregister eingetragen → kein gutgläubiger Schutz
- Flaggenwechsel ohne Genehmigung des Schiffshypothek-Gläubigers → Vertragsbruch
- ISM-Code: Betreiber ohne gültiges DOC → Hafenstaatkontrolle (PSC) hält Schiff auf
- KG-Modell: Anleger verlieren Einlage bei Insolvenz; Reederei kann nicht zahlen

## Normen und Quellen

- SchiffRG §§ 1–107: https://www.gesetze-im-internet.de/schiffreg/
- SchiffsRegO: https://www.gesetze-im-internet.de/schiffsrego/
- HGB §§ 476 ff.: https://www.gesetze-im-internet.de/hgb/__476.html
- § 5a EStG (Tonnagesteuer): https://www.gesetze-im-internet.de/estg/__5a.html
- ISM-Code (IMO): https://www.imo.org
- §§ 47, 49 InsO: https://www.gesetze-im-internet.de/inso/__47.html

## Output-Formate

- **Schiffsregister-Auszug-Analyse**: Eigentümer, Hypotheken, Lasten
- **Bareboat-Charter-Checkliste**: Flagge, ISM, Crew, Versicherung
- **Insolvenz-Sofortplan**: LG bei Insolvenz der Reederei
- **Tonnagesteuer-Memo**: Voraussetzungen und Berechnung

## 3. `lease-028-refinanzierung-forderungsabtretung-und-servicing`

**Fokus:** Leasingrefinanzierung: Forderungsabtretung, ABS-Strukturen, True Sale, Servicing, stille Abtretung und Schuldnerschutz nach § 407 BGB.

# Refinanzierung: Forderungsabtretung und Servicing

## Zweck

Leasinggesellschaften refinanzieren ihre Portfolios durch Forderungsabtretung (echtes Factoring, ABS) oder durch besicherte Darlehen (Sicherungsübereignung der Objekte). Dieser Skill analysiert die Abtretungsstruktur, ABS-Konstruktionen, Servicing-Pflichten und Schuldnerschutz.

## Refinanzierungsmethoden

### 1. Direkte Bankfinanzierung
- LG nimmt Bankdarlehen auf; Leasingforderungen als Sicherheit (stille Zession)
- Einfache Struktur; LG bleibt Kreditnehmer

### 2. Echtes Factoring (True Sale)
- LG verkauft Leasingforderungen an Finanzierungsvehikel (SPV)
- Keine Rückkaufpflicht des LG → „True Sale" → Off-Balance für LG
- Forderungen aus LN-Leasingraten sind das Assets des SPV

### 3. Asset-Backed Securities (ABS)
- SPV emittiert Wertpapiere besichert durch Leasingforderungen
- Tranchenstruktur: Senior (AAA), Mezzanine, Junior (LG hält oft Junior-Tranche)
- Ratingagentur bewertet Pool-Qualität

### 4. Sicherungsübereignung der Objekte
- LG übereignet Leasingobjekte sicherungshalber an Refinanzierer (Bank)
- Bei Ausfall: Bank kann Objekte verwerten

## True Sale: Voraussetzungen

### Echte Forderungsübertragung (§ 398 BGB)
- Abtretung: LG überträgt Leasingforderungen an SPV
- Stille Abtretung: LN erfährt nichts; zahlt weiter an LG (als Servicer)
- Offene Abtretung: LN wird informiert; zahlt direkt an SPV

### Abgrenzung True Sale vs. Sicherungsübereignung
- True Sale: Endgültiger Eigentumsübergang der Forderung; kein Rückkauf
- Sicherungsübereignung: Treuhänderisch; Rückkauf bei Tilgung des Darlehens
- Bilanzierung: True Sale → Off-Balance für LG; Sicherungsübereignung → On-Balance

## Schuldnerschutz (§§ 406–408 BGB)

### § 406 BGB: Aufrechnung
- LN kann nach Abtretung mit Gegenforderung gegen LG aufrechnen, wenn Gegenforderung vor Abtretung entstanden

### § 407 BGB: Leistung an bisherigen Gläubiger
- LN zahlt gutgläubig an LG (obwohl Forderung abgetreten): schuldbefreiend
- SPV kann LN nicht nochmals in Anspruch nehmen
- Schutz endet, wenn LN von Abtretung weiß (Anzeige nach § 409 BGB)

### Abtretungsanzeige (§ 409 BGB)
- Nach Anzeige der Abtretung: LN muss an neuen Gläubiger (SPV) zahlen
- Bis zur Anzeige: Gutgläubige Zahlung an LG schuldbefreiend

## Servicing-Vereinbarung

### Typischer Servicing-Vertrag
- LG bleibt Servicer: Einzug der Forderungen, Kundenkommunikation, Mahnwesen
- Servicer-Fee: Vergütung für LG als Servicer
- Kündigungsrecht des SPV bei Servicer-Ausfall (Successor Servicer-Klausel)

### Backup Servicer
- ABS-Strukturen erfordern oft Backup Servicer: übernimmt bei Insolvenz des LG
- Wichtig für ABS-Rating

## Insolvenz des LG als Servicer

- LG insolvent → kann keine Forderungen mehr einziehen
- Backup Servicer übernimmt
- Forderungen im SPV sind insolvenzfest (True Sale): nicht in Masse des LG

## Prüfprogramm

1. Refinanzierungsart: Direktdarlehen, True Sale oder ABS?
2. True Sale: Echte Forderungsübertragung? Off-Balance für LG?
3. Schuldnerschutz: § 407 BGB – zahlt LN noch an LG?
4. Abtretungsanzeige: Wann wird LN informiert?
5. Servicer-Vertrag: LG als Servicer; Backup Servicer?
6. Insolvenz LG: Forderungen im SPV insolvenzfest?

## Typische Fallen

- Stille Abtretung: LN zahlt weiter an LG (insolvent) → SPV leer; schuldbefreiende Zahlung nach § 407 BGB
- True Sale nicht vollständig → On-Balance → Bilanzverkürzung scheitert
- Kein Backup Servicer → Bei Insolvenz LG keine Forderungseinziehung → ABS-Ausfall
- § 406 BGB Aufrechnung: LN rechnet mit Schadensersatz gegen Leasingrate auf → SPV erhält weniger

## Normen und Quellen

- §§ 398–413 BGB (Abtretung): https://dejure.org/gesetze/BGB/398.html
- § 406 BGB (Aufrechnung nach Abtretung): https://dejure.org/gesetze/BGB/406.html
- § 407 BGB (Leistung an bisherigen Gläubiger): https://dejure.org/gesetze/BGB/407.html
- § 409 BGB (Abtretungsanzeige): https://dejure.org/gesetze/BGB/409.html
- KWG § 1 II Nr. 10 (Finanzierungsleasing als Finanzdienstleistung): https://www.gesetze-im-internet.de/kredwg/__1.html
- IFRS 9 (Finanzinstrumente): https://eur-lex.europa.eu

## Output-Formate

- **Refinanzierungsstruktur-Diagramm**: LG, SPV, Investoren, LN, Zahlungsflüsse
- **True-Sale-Checkliste**: Kriterien für echte Forderungsübertragung
- **Servicer-Vertrag-Muster**: Pflichten, Vergütung, Kündigung
- **§ 407-Memo**: Schuldnerschutz bei stiller Abtretung
