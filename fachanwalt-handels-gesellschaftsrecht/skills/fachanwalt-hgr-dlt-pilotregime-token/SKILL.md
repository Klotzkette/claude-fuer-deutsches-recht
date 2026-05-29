---
name: fachanwalt-hgr-dlt-pilotregime-token
description: "EU-DLT-Pilotregime VO 2022/858 (anwendbar 23.3.2023, verlängert voraussichtlich bis 23.3.2029) für DLT-basierte Wertpapierinfrastruktur. Tokenisierte Aktien und elektronische Wertpapiere (eWpG). Plattformtypen DLT-MTF (500 Mio. EUR) / DLT-TSS (6 Mrd. EUR) / DLT-SS. BaFin-Lizenzverfahren. Krypto-Wertpapierregister § 16 eWpG. Schwellenwerte, Compliance-Workflow, Risikomatrix, DORA-Schnittstelle, MiCA-Abgrenzung. Schriftsatzvorlagen BaFin-Antrag, Smart-Contract-Checkliste."
---

## Mandantenfragen beim Kaltstart

1. Welcher Wertpapiertyp soll tokenisiert werden — Inhaberaktie (§ 10 AktG), Namensaktie (§ 67 AktG), Schuldverschreibung oder Investmentanteil?
2. Welches Zielvolumen / welche Marktkapitalisierung ist geplant (relevant für Schwellenwerte DLT-MTF: 500 Mio. EUR; DLT-TSS: 6 Mrd. EUR)?
3. Welcher Plattformtyp ist vorgesehen — nur Handel (DLT-MTF), nur Abwicklung (DLT-SS) oder kombiniert (DLT-TSS)?
4. Ist ein bestehender BaFin-lizenzierter Anbieter als Register-Führer vorgesehen, oder wird eine eigene Lizenz beantragt?
5. Welche DLT-Plattform / Blockchain ist vorgesehen (Permissioned, Permissionless; Ethereum, Polygon, Stellar, dedizierte EU-Chain)?
6. Ist die Satzung der Aktiengesellschaft auf "elektronische Wertpapiere als Krypto-Wertpapiere" ausgerichtet?
7. Sind DORA-Anforderungen (seit 17.1.2025) bereits in der IT-Governance abgebildet?
8. Besteht ein Zeitplan für den Übergang nach Ablauf des Pilotregimes (voraussichtlich verlängert bis 23.3.2029)?

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| VO (EU) 2022/858 Art. 4 | DLT-MTF (Multilateral Trading Facility): Handel mit DLT-Wertpapieren; Schwelle 500 Mio. EUR Marktkapitalisierung |
| VO (EU) 2022/858 Art. 5 | DLT-SS (Settlement System): Abwicklung; ohne separate Handelsschwelle |
| VO (EU) 2022/858 Art. 6 | DLT-TSS (Trading and Settlement System): Kombination; Schwelle 6 Mrd. EUR Gesamtvolumen |
| VO (EU) 2022/858 Art. 7–9 | Voraussetzungen + Befreiungen von MiFID II / CSDR-Anforderungen |
| VO (EU) 2022/858 Art. 14 | Marktransparenzpflichten auf DLT-Plattformen |
| VO (EU) 2022/858 Art. 16 | Halbjährliche Berichtspflicht an ESMA |
| § 1 eWpG | Elektronisches Wertpapier: Begriffsbestimmung; Krypto-Wertpapier als Unterform |
| § 4 eWpG | Begründung durch Eintragung im Register statt Urkundenausgabe |
| § 11 eWpG | Krypto-Wertpapierregister: DLT-basiertes Register; Pflicht-Inhalte |
| § 16 eWpG | Pflichten des Register-Führers: Integrität, Verfügbarkeit, Vertraulichkeit |
| § 17 eWpG | Übertragung durch Umbuchung im Register; Gutglaubensschutz |
| § 1 Abs. 11 S. 1 Nr. 10 KWG | Krypto-Wertpapier als Finanzinstrument |
| § 1 Abs. 1a Nr. 8 KWG | Kryptoverwahrgeschäft als erlaubnispflichtiges Finanzdienstleistungsgeschäft |
| § 67c AktG | Digitales Aktienregister: Anforderungen bei Namensaktien |
| § 118a AktG | Online-Hauptversammlung mit digitaler Stimmrechtsausübung (DiRUG) |
| VO (EU) 2022/2554 (DORA) | Digital Operational Resilience Act: seit 17.1.2025 für Finanzdienstleister; auch für DLT-Plattformen anwendbar |
| VO (EU) 2023/1114 (MiCA) | Markets in Crypto Assets: ARTs und EMTs; Abgrenzung zu eWpG-Krypto-Wertpapieren wichtig |

## Leitentscheidungen und Regulatorische Quellen

| Quelle | Datum | Kernaussage |
|--------|-------|-------------|
| ESMA Final Report on DLT Pilot Regime | 2022 | Technische Standards; Plattformtypen; Berichtspflichten |
| BaFin-Merkblatt zum DLT-Pilotregime-Antrag | 2023 | Anforderungen BaFin-Antrag; Verfahrensdauer 6 Monate |
| BMF-Schreiben vom 17.11.2022 | 17.11.2022 | Steuerliche Behandlung Krypto-Wertpapiere; KapESt auf Token-Dividenden |
| ESMA Opinion on Review of DLT Pilot | 2024 | Empfehlung zur Verlängerung; Anpassungen für Phase 2 |
| BaFin-Schreiben zu DORA-Umsetzung | 2025 | DORA-Anforderungen für Register-Führer und DLT-Plattformbetreiber |

## DLT-Plattformtypen im Überblick

| Typ | Funktion | Schwelle | MiFID II / CSDR-Befreiung | Typische Nutzung |
|-----|---------|---------|--------------------------|-----------------|
| DLT-MTF | Nur Handel | 500 Mio. EUR Marktkapitalisierung | MiFID II-Lockerungen möglich | Sekundärmarkt für Token-Aktien |
| DLT-SS | Nur Abwicklung | Keine Schwelle | CSDR-Lockerungen | Clearing und Settlement für DLT-Wertpapiere |
| DLT-TSS | Handel + Abwicklung | 6 Mrd. EUR Gesamtvolumen | MiFID II + CSDR kombiniert | Vollständiger DLT-Marktplatz |

## Workflow Tokenisierung einer Aktiengesellschaft

### Phase 1 — Strukturentscheidung und Satzungsänderung

```
1. Rechtsformprüfung: AG, SE oder GmbH?
   - AG bevorzugt (§ 67c AktG digitales Aktienregister)
   - GmbH: Krypto-Wertpapier-Regelung über § 4 eWpG möglich

2. Satzungsanpassung (HV-Beschluss):
   - Aufnahme Klausel: "Die Gesellschaft kann Aktien als elektronische
     Wertpapiere gemäß eWpG begeben."
   - Namens- oder Inhaberaktie: Entscheidung dokumentieren
   - Form der HV-Einberufung und Stimmrechtsausübung digital (§ 118a AktG)

3. Notarielle Beurkundung der Satzungsänderung (§ 130 AktG)
4. Eintragung im Handelsregister
```

### Phase 2 — Krypto-Wertpapierregister einrichten

```
1. Wahl Register-Führer:
   - Bank mit § 1 KWG-Lizenz oder FinTech mit
     Kryptoverwahrerlaubnis (§ 1 Abs. 1a Nr. 8 KWG)
   - Due Diligence: DORA-Compliance, IT-Sicherheitszertifizierung,
     BaFin-Aufsicht aktiv

2. DLT-Plattform:
   - Permissioned (Ethereum Enterprise, Polygon, Stellar, Hyperledger):
     bevorzugt für regulierte Emissionen
   - Permissionless: KYC/AML-Anforderungen schwerer einhaltbar

3. Krypto-Wertpapierregister § 11 eWpG-Anforderungen:
   - Identifier der Token (ISIN digital)
   - Stückelung und Gesamtzahl
   - Inhaber-Verzeichnis (für Namensaktien)
   - Übertragungshistorie (unveränderlich / immutable)

4. Smart Contract-Pflichtfelder:
   - Transferrestriktionen (Whitelist KYC-verifizierter Adressen)
   - Compliance-Layer (AML/CFT nach GwG)
   - Dividendenausschüttungs-Funktion
   - Voting-Integration (§ 118a AktG)
```

### Phase 3 — BaFin-Lizenzantrag (für Plattformbetreiber)

```
Antrag an BaFin für DLT-MTF / DLT-SS / DLT-TSS:

Pflichtinhalte nach VO (EU) 2022/858 Art. 7:

1. Beschreibung der DLT-Infrastruktur:
   - Blockchain-Typ, Konsens-Mechanismus, Nodes
   - Governance-Struktur der Plattform

2. Cybersecurity-Konzept (BaFin BAIT/MaRisk):
   - Penetrationstest-Berichte (monatlich / jährlich)
   - Business Continuity Plan (BCP)
   - DORA-Konformitätsbescheinigung (seit 17.1.2025 Pflicht)

3. Marktintegrität:
   - MAR-Compliance (Insiderhandel, Marktmanipulation)
   - Ad-hoc-Mitteilungspflicht § 17 MAR

4. Transparenzberichte:
   - Halbjährlich an ESMA (Art. 16 VO 2022/858)

5. Übergangsplan nach Ende Pilotregime:
   - Roadmap Übergang zu vollem MiFID II / CSDR oder Schließung

Verfahrensdauer: 6 Monate (BaFin) + ggf. Verlängerung
```

### Phase 4 — Emittenten-Pflichten

```
1. Prospektpflicht (§ 6 WpPG):
   - Bei öffentlichem Angebot > EUR 8 Mio. in 12 Monaten: Prospektpflicht
   - Ausnahmen: nicht-öffentliche Platzierung, qualifizierte Anleger

2. KYC/AML der Token-Inhaber (GwG):
   - Identifizierungspflicht bei Erwerb
   - Whitelist im Smart Contract

3. Kapitalmarktrecht:
   - Insider-Liste § 26 MAR
   - Ad-hoc-Mitteilung § 17 MAR bei kursrelevanten Informationen
   - Stimmrechtsmitteilungen §§ 33 ff. WpHG bei Schwellenüberschreitung

4. Steuer:
   - Kapitalertragsteuer § 43 EStG auf Token-Dividenden
   - Veräußerungsgewinn: § 17 EStG (> 1 % Beteiligung) oder § 23 EStG
   - BMF-Schreiben 17.11.2022
```

### Phase 5 — Übertragung und Stimmrecht

```
1. Übertragung § 17 eWpG:
   - Umbuchung im Krypto-Wertpapierregister = Eigentumsübergang
   - Gutglaubensschutz für Erwerber

2. Hauptversammlung:
   - Token-Identifikation für Online-HV (§ 118a AktG)
   - Stimmenzählung via Smart Contract
   - Stimmrechtsnachweis per Blockchain-Snapshot zum Stichtag

3. Dividende:
   - Snapshot zum Ausschüttungsstichtag
   - Auszahlung an Token-Adressen (automatisch oder manuell)
   - KapESt-Einbehalt obligatorisch
```

## Risikomatrix

| Konstellation | Risiko | Norm | Maßnahme |
|--------------|--------|------|---------|
| Register-Führer ohne KWG-Lizenz | SEHR HOCH | § 32 KWG; § 1 Abs. 1a Nr. 8 KWG | Lizenzkontrolle vor Vertragsschluss |
| Smart Contract ohne Transfer-Restriktionen | HOCH | GwG; FATF-Standards | Whitelist-Layer einbauen; AML-Compliance |
| Schwelle DLT-MTF überschritten (> 500 Mio. EUR) | HOCH | Art. 4 VO 2022/858 | Übergang zu vollem MiFID II erforderlich oder Volumen reduzieren |
| DORA nicht eingehalten (seit 17.1.2025) | MITTEL-HOCH | VO 2022/2554 Art. 16–20 | ICT-Risikomanagement implementieren; Penetrationstest |
| Pilotregime läuft aus (3/2026 bzw. 3/2029) | MITTEL | VO 2022/858 Art. 18 | Übergangsstrategie 18 Monate vorher definieren |
| Prospektpflicht missachtet | SEHR HOCH | § 6 WpPG | Schwelle EUR 8 Mio. überwachen; Ausnahmen dokumentieren |
| MiCA-ART-Einstufung des Tokens | MITTEL | VO 2023/1114 | Abgrenzung Krypto-Wertpapier (eWpG) vs. Asset-Referenced Token (MiCA) |

## Smart-Contract-Checkliste § 16 eWpG

```
Pflicht-Felder im Krypto-Wertpapierregister:

[ ] Eindeutiger Identifier (ISIN digital oder nationale Kennung)
[ ] Wertpapierart (Aktie/Schuldverschreibung)
[ ] Emittent (Name, LEI-Nummer)
[ ] Gesamtstückelung und Nennwert
[ ] Ausstellungsdatum
[ ] Inhaber-Mapping (für Namensaktien: Adresse → Identität)
[ ] Unveränderlichkeit der Buchungshistorie (Audit Trail)
[ ] Transferrestriktionen (Whitelist / Blacklist)
[ ] Dividendenausschüttungs-Funktion
[ ] Voting-Integration (HV-Stimmrecht § 118a AktG)
[ ] Emergency-Freeze-Funktion (regulatorische Anforderung)
[ ] Interoperabilität mit anderen Registern (§ 17 eWpG Übertragung)
```

## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Eigentumsübergang durch Umbuchung | Erwerber | Blockchain-Protokoll; Register-Auszug § 11 eWpG |
| BaFin-Lizenz des Register-Führers | Emittent bei Haftungsklage | BaFin-Lizenzurkunde; öffentliches BaFin-Register |
| Prospektpflicht-Ausnahme | Emittent | Anleger-Protokoll (qualifizierter Anleger); Platzierungsdokumentation |
| DORA-Compliance | Plattformbetreiber | ICT-Risikomanagement-Bericht; Audit-Protokoll |
| Eigentumsstellung für Stimmrecht HV | Aktionär | Snapshot-Zertifikat der Blockchain zum Stichtag |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 6 Monate | BaFin-Lizenzverfahren (ca.) | BaFin-Merkblatt 2023 |
| Halbjährlich | ESMA-Transparenzbericht | Art. 16 VO 2022/858 |
| 17.1.2025 | DORA vollständig anwendbar | VO 2022/2554 |
| 23.3.2029 | Voraussichtliches Ende Pilotregime (verlängert) | VO 2022/858; ESMA-Empfehlung |
| 10 Tage | Meldepflicht bei IT-Vorfällen nach DORA | VO 2022/2554 Art. 19 |

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Startup will Token-Aktien begeben | DLT-TSS oder DLT-SS mit lizenziertem Register-Führer; eigene BaFin-Lizenz nur bei Volumen > EUR 100 Mio. | Kosten-Nutzen; Lizenz-Outsourcing kostengünstiger |
| Bestehendes Unternehmen will Kapitalerhöhung digital | Satzungsänderung + Krypto-Wertpapierregister + Prospekt-Prüfung | Digitale Emission erhöht Liquidität; Prospektpflicht beachten |
| Pilotregime läuft aus | 18 Monate vorher Übergangsplan: MiFID II-Compliance, CSDR oder Plattformschließung | ESMA-Empfehlung: Übergangsfrist beachten |
| Stimmrechtsausübung digital | Online-HV § 118a AktG + Smart-Contract-Voting + Datenschutz | Effizienzgewinn; Satzungsklausel erforderlich |

## Anschluss-Skills

- `fachanwalt-bank-kapitalmarktrecht-mica-stablecoin-art-16-bafin` — MiCA-Abgrenzung zu Krypto-Wertpapieren
- `fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung` — Holding-Struktur bei Token-Unternehmen
- `sanktions-compliance-pruefung` — Exportkontrolle bei DLT-Plattformen mit Auslandsbezug
- `gerichtsstand-und-rechtswahl-pruefen` — Grenzüberschreitende Token-Angebote

## Quellen

- EU-DLT-Pilotregime VO 2022/858: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R0858
- eWpG: https://www.gesetze-im-internet.de/ewpg/
- BaFin DLT-Pilotregime: https://www.bafin.de/DE/Aufsicht/FinTech/DLT-Pilotregime/dlt_pilotregime_node.html
- DORA VO 2022/2554: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2554
- MiCA VO 2023/1114: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R1114
- BMF-Schreiben 17.11.2022: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Ertragsteuern/2022-11-17-einzelfragen-zur-ertragsteuerrechtlichen-behandlung-von-elektronischen-wertpapieren.pdf
