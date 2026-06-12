---
name: handelsregister-elektronische-zustellung
description: "Fachmodul für Vorhaben mit Handelsregister-Bezug und elektronischer Zustellung. Beschreibt die Schnittstellen HRG ZPO beA beBPO De-Mail eIDAS-Wallet und die typischen NKR-Prüfpunkte bei Handelsregister-Vorhaben (Fallzahlen rund 1.8 Mio Gesellschaften zentrale vs dezentrale Architektur Once-Only"
---

# NKR-Handelsregister und elektronische Zustellung

## Worum geht es konkret

Vorhaben mit Bezug auf das Handelsregister und elektronische Zustellungswege gehoeren zu den methodisch komplexesten NKR-Prüfungen. Sie verbinden Gesellschaftsrecht, ZPO, OZG, eIDAS-VO, beA und die dezentrale Registerstruktur in Deutschland. Dieser Skill ist auch die methodische Grundlage für die Testakte des Plugins (ElErrHandRegG).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Vorhaben ändert HGB / Handelsregister-Vorschriften
- Vorhaben sieht elektronische Zustellung an Gesellschaften vor
- Vorhaben adressiert ausländische Gesellschaften mit deutscher Zweigniederlassung
- Fallzahlen-Prüfung mit Bezug auf Anzahl Gesellschaften

Rueckfrage nur wenn unklar: *"Welche Rechtsformen sind adressiert — alle eingetragenen Gesellschaften, nur Kapitalgesellschaften, nur GmbH?"*

## Rechtlicher und methodischer Rahmen

- **HGB**, insbesondere §§ 1 ff., 8 ff., 33 ff.
- **HRV (Handelsregisterverordnung)** in der jeweils geltenden Fassung
- **ZPO**, insbesondere §§ 166-195a (Zustellungsrecht)
- **ERVV** (Elektronischer Rechtsverkehr in Zivilsachen)
- **BRAO §§ 31a, 31b** (beA / beBPO)
- **De-Mail-Gesetz**
- **eIDAS-Verordnung (EU) 910/2014** in der jeweils geltenden Fassung
- **OZG** in der jeweils geltenden Fassung
- **NKRG** § 4, **GGO** §§ 44, 45

## Fallzahlen-Orientierung (Stand 06/2026, vom Anwender zu prüfen)

- Eingetragene Gesellschaften gesamt: rund 1,8 Mio (Statistisches Bundesamt, Unternehmensregister; vom Anwender mit aktueller Zahl zu prüfen)
- GmbH: dominantes Segment (groesste Einzelmenge)
- AG, KGaA, OHG, KG, e.K.: jeweils kleinere Segmente
- Ausländische Gesellschaften mit deutscher Zweigniederlassung: kleinere Teilmenge

## Prüfraster / Schritt für Schritt

### 1. Adressatenkreis

- Welche Rechtsformen?
- Aktive vs. ruhende Gesellschaften?
- Ausländische Gesellschaften?
- Konzerne — Konsolidierung oder einzeln?

### 2. Architektur (zentral vs. dezentral)

- Wer fuehrt die elektronische Adresse?
 - **Zentral**: einheitliches Register beim BfJ / zentrale Stelle
 - **Dezentral**: bei jedem Amtsgericht (Registergericht)
- Schnittstellen
- Datenkonsistenz

### 3. Standards

- beA / beBPO / De-Mail / EUDI-Wallet / qualifizierter eIDAS-Mailbox-Dienst
- Single Sign-On
- Once-Only
- XOEV / FIM

### 4. Fortlaufende Erreichbarkeit

- "Lebensbescheid" / Erreichbarkeitsbestaetigung
- Frequenz (monatlich / quartalsweise / jaehrlich / event-driven)
- Konsequenzen bei Verstoss (Zwangsgeld, Loeschung)

### 5. Ausländische Gesellschaften

- Inlandsvertreter (analog § 184 ZPO)
- Direktanschluss EU-weiter Systeme (BRIS Business Registers Interconnection System)
- Schnittstelle zu nationalen Registern anderer Mitgliedstaaten

### 6. Erfuellungsaufwand

- Aufwand pro Gesellschaft × Fallzahl
- Aufwand Verwaltung (Registergerichte, BfJ)
- Sanktionsaufwand (Verfahren, Zwangsgeld)

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Dezentrale Loesung trotz hoher Skaleneffekte einer zentralen
- Hoche Frequenz Lebensbescheid (monatlich) ohne Sachgrund
- Parallele Standards ohne Once-Only
- Ausländische Gesellschaften ungeklaert
- Sanktionsmechanik zu pauschal (z.B. Loeschungsdrohung ohne Stufung)
- KMU nicht differenziert (Kleinst-Gesellschaften gleich behandelt wie Konzerne)

## Trade-off-Matrix

| Aspekt | Plus | Minus |
|---|---|---|
| Architektur zentral | Skalierung, Once-Only | Implementierungsaufwand initial |
| Architektur dezentral | Bestandssystem nutzbar | hoher Vollzugsaufwand, Datenfragmentierung |
| Frequenz monatlich | rasche Erreichbarkeit | sehr hoher Erfuellungsaufwand |
| Frequenz jaehrlich + Event | gleicher Effekt, geringer Aufwand | etwas hoeheres Aktualitaetsrisiko |
| Mehrere Standards | technische Wahlfreiheit | keine Once-Only |
| Einheitlicher Standard | Once-Only, Effizienz | weniger Flexibilitaet |

## Mustertexte / Stellungnahme-Bausteine

- "Das Vorhaben betrifft alle im Handelsregister eingetragenen Gesellschaften (rund 1,8 Mio nach Unternehmensregister Statistisches Bundesamt) sowie ausländische Gesellschaften mit deutscher Zweigniederlassung."
- "Der NKR begruesst die Zielsetzung, die elektronische Erreichbarkeit von im Handelsregister eingetragenen Gesellschaften zu verbessern und damit Verfahren zu beschleunigen."
- "Der NKR weist darauf hin, dass die vorgesehene dezentrale Architektur einen erheblichen Mehraufwand für die Wirtschaft und die Verwaltung verursacht. Eine zentrale Loesung über das Handelsregistergericht im Sinne des Once-Only-Prinzips waere praktikabler."
- "Die vorgesehene monatliche Lebensbescheid-Pflicht ist aus Sicht des NKR unverhaeltnismaessig. Eine jaehrliche Bestaetigung mit ereignisorientierter Nachmeldepflicht erreicht das Regelungsziel mit deutlich geringerem Erfuellungsaufwand."
- "Der NKR empfiehlt, das vorgesehene Verfahren mit dem OZG-Portalverbund, dem beA-System und der EUDI-Wallet zu verknuepfen und die Standards XOEV und FIM anzuwenden."
- "Der NKR empfiehlt, für ausländische Gesellschaften mit deutscher Zweigniederlassung den Anschluss an das Business Registers Interconnection System (BRIS) zu prüfen, anstatt einen separaten Inlandsvertreter zu fordern."

### Spezielle Aufwandsberechnung (Beispiel ElErrHandRegG)

- Adressaten: rund 1,8 Mio Gesellschaften
- Pflicht: monatliche Lebensbescheid-Bestaetigung
- Aufwand pro Fall: ca. 15 min pro Bestaetigung × 12 = 180 min = 3 h pro Jahr
- Lohnsatz Wirtschaft (Verwaltungstaetigkeit): ca. 45 EUR/h
- Aufwand pro Gesellschaft p.a.: 3 × 45 = 135 EUR
- Plus Sachkosten / IT-Anteil: ca. 45 EUR p.a.
- Gesamtaufwand pro Gesellschaft p.a.: ca. 180 EUR
- **Hochrechnung**: 1,8 Mio × 180 EUR = **324 Mio EUR jaehrlich**

Alternativ: jaehrliche Bestaetigung
- 15 min × 1 = 15 min × 45 EUR/h = ca. 11 EUR Zeit
- Sachkosten: ca. 35 EUR
- Gesamt pro Gesellschaft p.a.: ca. 46 EUR
- **Hochrechnung**: 1,8 Mio × 46 EUR = **ca. 83 Mio EUR jaehrlich**

Ersparnis: rund **240 Mio EUR jaehrlich**.

## Typische Fehler in Ressort-Entwuerfen

- Fallzahlen ohne Quelle (Mikrozensus statt Unternehmensregister)
- "Geringer Mehraufwand für die Wirtschaft" trotz monatlicher Pflicht
- Ausländische Gesellschaften nicht adressiert
- Mehrere Standards parallel ohne Schnittstellen-Spezifikation
- Konsequenz Loeschung aus Handelsregister ohne Abstufung

## Quellen Stand 06/2026

- HGB; HRV in der jeweils geltenden Fassung
- ZPO §§ 166-195a; ERVV
- BRAO §§ 31a, 31b
- De-Mail-Gesetz
- eIDAS-Verordnung (EU) 910/2014 in der jeweils geltenden Fassung
- OZG in der jeweils geltenden Fassung
- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4
- Statistisches Bundesamt — Unternehmensregister
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren über [www.destatis.de](https://www.destatis.de), [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de) und [www.bundesjustizportal.de](https://www.handelsregister.de)
