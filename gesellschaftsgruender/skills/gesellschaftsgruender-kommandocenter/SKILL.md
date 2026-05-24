---
name: gesellschaftsgruender-kommandocenter
description: "Master-Workflow fuer die Gesellschaftsgruendung. Fuehrt von der Rechtsformwahl ueber Gesellschaftsvertrag Notar Handelsregister Gewerbeamt Finanzamt Transparenzregister bis zu den ersten Geschaeftsfuehrer-Pflichten. Synchronisiert Fristen Beteiligte Dokumente. Liefert Checkliste und Ablaufplan fuer GmbH UG GbR OHG KG GmbH und Co KG PartG mbB gGmbH eK."
---

# Kommandocenter Gesellschaftsgründung

## Zweck

Master-Workflow für die Begleitung einer Gesellschaftsgründung von der ersten Beratung bis zur betriebsbereiten Gesellschaft. Verbindet die spezifischen Skills zu einem Ablauf und synchronisiert Fristen, Beteiligte, Dokumente.

## Phasen

### Phase 0 — Rechtsformwahl (Woche 1)

Vor allem anderen: Welche Rechtsform passt? Haftung, Steuern, Kosten, Komplexitaet, Struktur, Reputation, Investorenfähigkeit.

→ `gesellschaftsgruender-rechtsformwahl`

### Phase A — Vorbereitung (Woche 2-3)

- Gesellschafterstruktur klären (Stimmrechte, Gewinnverteilung, Mehrheits-/Minderheits-Schutz)
- Firmenname prüfen (IHK-Vorprüfung, Verwechslungsfrage Paragraf 30 HGB, Domain)
- Sitz und Gegenstand des Unternehmens festlegen
- Stammkapital und Sacheinlagen klären (Werthaltigkeit, Sachgründungsbericht)

### Phase B — Verträge (Woche 3-4)

- Gesellschaftsvertrag / Satzung
- Gesellschaftervereinbarung (Shareholder Agreement)
- Geschäftsführeranstellungsvertrag
- Bei KG: Beirat / Aufsichtsrat optional

→ `gesellschaftsgruender-gesellschaftsvertrag-gmbh`
→ `gesellschaftsgruender-gesellschaftervereinbarung`
→ `gesellschaftsgruender-geschaeftsfuehrervertrag`

### Phase C — Notar (Woche 4-5)

GmbH / UG / AG: Beurkundung erforderlich. Vorbereitung der Notarsitzung, Prüfung von Vertretungen, Sacheinlage-Belegen, Gesellschafterliste.

Alternative seit DiRUG 2022: Online-Gründung per Videokonferenz beim Notar (nur Bargründung).

→ `gesellschaftsgruender-notar-vorbereitung`
→ `gesellschaftsgruender-online-gruendung-dirug`

### Phase D — Handelsregister und Behörden (Woche 5-6)

- Anmeldung Handelsregister durch Notar
- Gewerbeanmeldung (lokales Gewerbeamt)
- Fragebogen zur steuerlichen Erfassung (Finanzamt, elektronisch über ELSTER)
- Transparenzregister (TraFinG, Pflicht Paragraf 19 GwG)
- IHK-Mitgliedschaft (Pflicht, mit Beitrag)
- Berufsgenossenschaft (Pflicht binnen einer Woche)

→ `gesellschaftsgruender-handelsregister-anmeldung`
→ `gesellschaftsgruender-gewerbeanmeldung-finanzamt`
→ `gesellschaftsgruender-transparenzregister`
→ `gesellschaftsgruender-ihk-und-berufsgenossenschaft`

### Phase E — Operativer Start (Woche 6-8)

- Geschäftskonto eröffnen (GwG-Identifikation, gegebenenfalls Online-Banking)
- Stammkapital einzahlen (Mindesthöhen pro Rechtsform)
- Buchhaltung aufsetzen (Kontenrahmen SKR03/SKR04)
- Rechnungslegung beginnen
- Steuer-Vorauszahlungen anmelden

→ `gesellschaftsgruender-stammkapital-einzahlung`
→ `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase`

## Beteiligte

- **Gründer**: Treffen die wesentlichen Entscheidungen, unterzeichnen
- **Notar**: Beurkundet GmbH/AG, meldet beim Handelsregister an
- **Steuerberater**: ELSTER-Anmeldung, laufende Buchhaltung
- **Bank**: Geschäftskonto, GwG-Identifikation
- **Anwalt** (oft erste Gründer-Beratung, dieses Plugin)
- **IHK** (Vor-Prüfung Firmenname, Mitgliedschaft)
- **Gewerbeamt** (lokale Anmeldung)
- **Finanzamt** (Erfassung, Steuernummer)
- **Berufsgenossenschaft** (BG-Mitgliedschaft)

## Fristen-Übersicht

| Aktion | Frist | Konsequenz |
|---|---|---|
| Gewerbeanmeldung | unverzueglich nach Geschäftsaufnahme | Bußgeld Paragraf 146 GewO |
| Fragebogen Finanzamt | innerhalb eines Monats nach Aufnahme | Schätzung, Saeumniszuschlag |
| Anmeldung Berufsgenossenschaft | binnen einer Woche | Bußgeld |
| Transparenzregister-Meldung | unverzueglich bei wirtschaftlich Berechtigtem | bis 150.000 EUR Bußgeld Paragraf 56 GwG |
| Handelsregister-Anmeldung (GmbH) | nach Beurkundung | Verzug schadet Geschäftsführerhaftung |
| IHK-Anmeldung | mit der Gewerbeanmeldung (automatisch) | - |
| Erste Lohnabrechnung | bei Beschaeftigung Lohnsteuer-Anmeldung | Saeumnis Paragraf 240 AO |

## Kosten-Rahmen (Stand 2026)

| Rechtsform | Notar | Handelsregister | Sonstige | Gesamt |
|---|---|---|---|---|
| eK | - | ca. 70 EUR | - | < 200 EUR |
| GbR (eGbR seit MoPeG) | nur bei Wahl der Eintragung | ca. 80-150 EUR | ggf. IHK | < 300 EUR |
| UG | ca. 250-450 EUR (Musterprotokoll) | ca. 150 EUR | IHK | < 800 EUR |
| GmbH (Musterprotokoll) | ca. 400-600 EUR | ca. 150 EUR | IHK | ca. 800-1.000 EUR |
| GmbH (individuelle Satzung) | ca. 800-1.500 EUR | ca. 150 EUR | IHK + Steuerberater | 1.500-3.000 EUR |
| GmbH und Co KG | ca. 1.500-3.000 EUR (zwei Gesellschaften) | ca. 300 EUR | IHK + Steuerberater | 3.000-5.000 EUR |
| AG | ca. 3.000-8.000 EUR | ca. 300 EUR | Hauptversammlung-Vorbereitung | > 10.000 EUR |

## Stoppschilder — Wann Anwalt zwingend

- Bei Sacheinlagen (Werthaltigkeit Paragraf 7 III GmbHG, Differenzhaftung Paragraf 9 GmbHG)
- Bei Beteiligung von Gesellschaftern aus Drittstaaten (Sanktionsrecht, ggf. Investitionsprüfung)
- Bei gemeinnützigen Zwecken (gGmbH, Voraussetzungen Paragraf 52 AO)
- Bei Konzernstrukturen (Beherrschungs-/Gewinnabführungsvertrag)
- Bei Family-Office-Strukturen
- Bei Holding-Strukturen (steuerliche Vorprüfung)
- Bei Family-Buy-In / Buy-Out

## Plugin-Eigeneinschraenkung

Dieses Plugin ist Begleiter, nicht Ersatz für Notar oder Anwalt. Beurkundungen erfolgen ausschließlich beim Notar. Steuerliche Strukturberatung gehört zum Steuerberater. Bei zweifelhaften Konstellationen: anwaltliche Prüfung anstrahlen.

## Anschluss

- `gesellschaftsgruender-rechtsformwahl` — wenn Rechtsform noch offen
- `gesellschaftsrecht` — für laufende Mandate nach Gründung
- `fachanwalt-handels-gesellschaftsrecht` — für fachanwaltschaftliche Vertiefung
- `kanzlei-allgemein-mandatsannahme-gwg` — bei eigener Mandatsannahme
