---
name: fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht
description: "Cyber-Versicherung bei Ransomware mit Sanktions-Risiko OFAC EU-VO 833/2014 VO 269/2014 Russland-Sanktionen. Deckungs-Abwehr Versicherer bei Loesegeld-Zahlung. § 261 StGB Geldwaesche. OFAC-Advisory Anti-Money-Laundering. BaFin-Aufsicht. § 16 OWiG Sanktionsbruch. Workflow Schadensanalyse Sanktions-Pruefung Versicherungsanspruch."
---

# Cyber-Lösegeld bei Ransomware mit Sanktions-Risiko

## Zweck

Spezial-Mandat: Mandant hat Cyber-Versicherung, wurde Opfer Ransomware-Angriff. Lösegeld-Zahlung wird erwogen oder bereits geleistet. Versicherer verweigert Deckung mit Verweis auf Sanktions-Risiko (OFAC Specially Designated Nationals List, EU-Russland-Sanktionen, Lazarus Group Nordkorea). Anwaltliche Deckungs-Klage.

## Eingaben

- Versicherungsvertrag Cyber-Police (GDV-Bedingungen + Individualklauseln)
- Identität / Indizien zum Erpresser (typisch Crypto-Wallet, Tor-Adresse)
- Bisheriger Verlauf (Verhandlung, Probe-Entschlüsselung, Forderung)
- Sanktions-Screening durchgeführt? (Chainalysis Sanctions Screening, OFAC SDN)
- Versicherer-Abwehrschreiben
- Datum der Zahlung (falls bereits erfolgt)

## Rechtlicher Rahmen

### Sanktionsrecht

- **VO (EU) 833/2014** Russland-Wirtschaftssanktionen (mit zahlreichen Erweiterungen 2022-2025)
- **VO (EU) 269/2014** Russland-Personensanktionen (Vermögenseinfrierungen)
- **OFAC SDN List** USA (50 % Rule für indirekte Sanktionierte)
- **§§ 17, 18 AWG** Embargo-Verordnung Verstoß (Freiheitsstrafe bis 10 Jahre)
- **§ 81 AWV** Buß-/Strafvorschriften
- **OFAC Advisory** vom 1.10.2020 und 21.9.2021 zu Ransomware-Zahlungen

### Versicherungsrecht

- **VVG § 81** — Herbeiführung Versicherungsfall (Versicherte-Eigenverschulden)
- **VVG § 28** — Obliegenheitsverletzung
- **Sanctions Limitation Clauses** in Cyber-Policen (Standard-Wording)
- **GDV-Cyber-AVB**

### Strafrecht

- **§ 261 StGB** — Geldwäsche (auch Vorfeld-Zahlungen, wenn herkunfts-strittig)
- **§ 89c StGB** — Terrorismus-Finanzierung (bei Lazarus Group / Hamas etc.)

### Leitentscheidungen

- LG Bonn, Urt. v. 14.6.2024 — 22 O 51/23 (Cyber-Deckung bei Lösegeld; Sanktions-Klausel-Wirksamkeit)
- OLG Düsseldorf, Urt. v. 22.11.2023 — I-4 U 80/22 (Versicherungsfall Ransomware)
- US Federal Court (Travelers Ins. v. Universal Health Services 2023) — Sanctions Exclusion

## Konstellationen

### A — Erpresser auf OFAC SDN-Liste (z. B. Lazarus Group, Conti-Nachfolger)

- **OFAC**: Lösegeld-Zahlung **strikt verboten** (Direct + Indirect)
- **OFAC Advisory 2021**: Lösegeld-Zahlung kann eigene Sanktions-Verletzung sein
- US-Sanktionen wirken auch auf nicht-US-Unternehmen mit US-Geschäftsbezug
- Strafrechtliche Folge USA: bis 1 Mio. USD Buße + Haft
- Strafrechtliche Folge DE: § 18 AWG Verstoß bis 10 Jahre Haft

### B — Erpresser nicht direkt sanktioniert (kein klarer SDN-Match)

- Sanktions-Klausel der Versicherung greift dennoch oft restriktiv
- Compliance: Sorgfaltspflichten zur Identifikation des Empfängers
- Chainalysis Reactor-Analyse vor Zahlung
- Bei nicht-sanktionierter Adresse: Versicherer-Deckung möglich

### C — Erpresser möglicherweise sanktioniert (Grauzone)

- Cyber-Versicherer fordert Compliance-Memo
- Bei Zweifel: Zahlung untersagt
- BSI-Empfehlung: keine Zahlung
- Alternative: Daten-Wiederherstellung aus Backup

## Workflow

### Phase 1 — Sofortmaßnahmen nach Angriff

- BSI-Meldung (KRITIS) / Polizei-LKA Cybercrime
- Versicherer-Anzeige binnen 24-48 Stunden
- Forensik-Beauftragung
- Backup-Prüfung (vorrangig vor Lösegeld)

### Phase 2 — Sanktions-Screening vor Zahlung

- Wallet-Adresse forensisch zurückverfolgen (Chainalysis, Elliptic)
- OFAC SDN-Match-Check
- EU-Sanktionslisten (VO 269/2014, VO 833/2014)
- UN-Sanktionsliste
- **Wenn Match**: Zahlung **darf nicht erfolgen** (Strafbarkeit)
- **Memo** für Akten und Versicherer

### Phase 3 — Versicherer-Verhandlung

- Schadensanzeige mit Forensik-Bericht
- Versicherer prüft Sanktions-Klausel + Verschulden § 81 VVG
- Bei Deckungs-Abwehr: schriftliche Begründung verlangen

### Phase 4 — Deckungs-Klage

- LG-Sitz Versicherer
- Klage auf Versicherungsleistung
- Argumentation: Sanktions-Klausel zu weit / unverständlich / unwirksam (§ 305c BGB / Transparenz)
- Bei abgelehnter Klausel: AVB-Auslegung

### Phase 5 — Bei Sanktions-Verstoß-Verdacht

- Strafverteidigung parallel zur Deckungs-Klage
- Selbstanzeige bei Lieferchain-Versehen prüfen (§ 22 OWiG)
- BAFA-Kommunikation

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Zahlung an SDN-Wallet | § 18 AWG-Verstoß + Versicherungs-Ausschluss | Pre-Zahlungs-Klärung | klare Compliance-Kette |
| Versicherer-Sanktions-Klausel undurchsichtig | § 305c BGB-Unwirksamkeit prüfen | Klärung läuft | klar formuliert |
| OFAC-Verstoß durch DE-Mandant | US-Sanktionen mit Extraterritorialität | klare US-Geschäftsabsicht-Check | kein US-Bezug |
| Daten-Backup nicht versucht | Versicherer rügt Obliegenheitsverletzung | Backup-Versuch dokumentiert | Backup geprüft |

## Querverweise

- `fachanwalt-versicherungsrecht-orientierung` — Triage
- `fachanwalt-versicherungsrecht-do-deckungsabwehr` — D&O-Variante
- `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` — Sofortmaßnahmen
- `aussenwirtschaft-zoll-sanktionen` — Sanktions-Compliance
- `fachanwalt-strafrecht-orientierung` — Strafverteidigung

## Quellen und Updates

Stand: 05/2026. OFAC Advisory 2021. EU-VO 833/2014, 269/2014 mit laufenden Erweiterungen. LG Bonn 22 O 51/23. Bei OFAC-Listen-Update / EU-Sanktionsrunde aktualisieren.
