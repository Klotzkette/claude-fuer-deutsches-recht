---
name: fachanwalt-bank-kapitalmarktrecht-mica-stablecoin-art-16-bafin
description: "MiCA-Verordnung VO (EU) 2023/1114 Art. 16-21 Lizenzierung von Stablecoin-Emittenten (Asset-Referenced Tokens ART und Electronic Money Tokens EMT) bei BaFin. Whitepaper-Pflicht Art. 19. Eigenmittel-Anforderung Art. 35. Reserveaktiva Verwahrungspflichten Art. 36-38. BaFin-Antrag und Pruefverfahren 180 Tage Art. 17. Workflow Emittenten-Lizenz Whitepaper Notifizierung."
---

# MiCA-Stablecoin-Emittenten — Art. 16-21 Lizenzierung (BaFin)

## Zweck

Beratung von FinTechs und Banken bei der Lizenzierung als Emittent von Asset-Referenced Tokens (ART) oder E-Money Tokens (EMT) nach MiCA-VO (EU) 2023/1114, Titel III/IV. MiCA ist seit 30.6.2024 (ART/EMT-Teil) bzw. 30.12.2024 (CASP-Teil) anwendbar; die BaFin ist die zuständige nationale Behörde.

## Eingaben

- Geplanter Token-Typ (ART = mehrere Werte-Referenz / EMT = 1:1 Fiat-Anbindung)
- Geplantes Emissionsvolumen (für „significant"-Schwelle Art. 43-58)
- Vorhandene Bank-/Zahlungs-Lizenzen (CRD-Kreditinstitut, ZAG-Zahlungsinstitut, E-Geld-Institut)
- Verwahrungsstruktur Reserveaktiva (Custodian, Banken-Diversifikation)
- Whitepaper-Entwurf
- Sitz der emittierenden Gesellschaft

## Rechtlicher Rahmen

### MiCA-VO (EU) 2023/1114

- **Art. 16-17** — Zulassung als ART-Emittent (180-Tage-Verfahren bei BaFin)
- **Art. 19** — Whitepaper-Pflichten (Inhalt, Notifizierung, Vorabprüfung BaFin)
- **Art. 25** — Marketing-Mitteilungen
- **Art. 31-34** — Pflichten Emittent (Reserve-Aktiva, Trennung)
- **Art. 35** — Eigenmittel: 2 % der durchschnittlichen Reserve oder 350.000 EUR (höherer Wert)
- **Art. 36-38** — Verwahrung der Reserve (≥ 30 % bei verschiedenen Kreditinstituten)
- **Art. 43-58** — Erhöhte Pflichten für "signifikante" ART (Schwelle 10 Mio. Token oder 5 Mio. EUR Marktwert)
- **Art. 48-58** — EMT-spezifisch (1:1-Bindung, kein eigener Whitepaper-Genehmigungsprozess wenn CRD/E-Geld)

### Nationaler Rahmen

- **KWG / ZAG** für Bank-/E-Geld-Aspekte
- **WpHG / WpIG** falls Wertpapier-Charakteristika
- **GwG** Geldwäscheprävention
- **§ 32 BaFin-Aufsicht**

### Leitentscheidungen / Auslegung

- **ESMA Q&A** zu MiCA (laufend, 2024-2026)
- **BaFin-Merkblatt** zur Antragsstellung Art. 16 (2024)
- **EBA/ESMA Joint Guidelines** zu signifikanten ART (2024)

## Workflow Lizenzierung

### Phase 1 — Token-Klassifikation

- ART (Asset-Referenced Token) — Wert mehrerer Werte
- EMT (E-Money Token) — 1:1 Fiat-Bindung
- Utility Token (außerhalb MiCA, aber Whitepaper Art. 4-6)
- Token-Klassifikations-Memo erstellen (FAQ-Stil)

### Phase 2 — Antragsvoraussetzungen Art. 16 MiCA

| Voraussetzung | Inhalt |
|---|---|
| Gesellschaftsrechtl. Sitz | EU-Mitgliedstaat |
| Mindest-Eigenmittel | 350.000 EUR oder 2 % Reserve |
| Geschäftsplan | 3-Jahres-Plan |
| Governance | Geeignete Geschäftsführer, Vier-Augen-Prinzip |
| Risikomanagement | Schriftlich, BaFin-konform |
| Reserve-Politik | Diversifikation, Verwahrung bei Kreditinstituten |

### Phase 3 — Whitepaper Art. 19 MiCA

Pflichtinhalte:
- Identität Emittent / Geschäftsführer
- Token-Beschreibung
- Rechte und Pflichten Inhaber
- Risikofaktoren
- Reserve-Aktiva-Beschreibung
- Rückkaufrecht (für ART)
- Technologie und Konsensmechanismus
- Klimaauswirkungen

### Phase 4 — BaFin-Antrag

- Einreichung digital über BaFin-Portal
- **180 Tage**-Entscheidungsfrist Art. 17 (verlängerbar)
- BaFin-Konsultation mit EBA bei signifikanten ART
- BaFin-Rückfragen typisch innerhalb 60 Tagen

### Phase 5 — Bei Lizenz

- Notifizierung an ESMA-Register
- Whitepaper-Veröffentlichung
- Marketing-Mitteilungen Art. 25 konform
- Laufende Berichts-Pflichten (vierteljährlich)

## Eigenmittel + Reserve-Struktur

```
Eigenmittel-Pflicht Art. 35 MiCA
= max(350.000 EUR; 2 % × Ø Reserve-Aktiva)

Reserve-Aktiva Art. 36-37
- 100 % der Token-Verbindlichkeit
- Hochliquide, geringes Risiko
- Verwahrung bei ≥ 3 Kreditinstituten (Diversifikation)
- Mindestens 30 % bei Kreditinstituten zu jedem Zeitpunkt

Signifikante ART (Art. 43+):
- Erhöhte Eigenmittel 3 %
- Stresstest-Pflicht
- EBA als zusätzliche Aufsicht
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Reserve nicht bei Kreditinstituten | Lizenz-Verweigerung | Vertragsverhandlungen | Diversifizierte Verwahrung |
| Whitepaper unvollständig | Rückfrage-Loop; Verzögerung | Nachbesserung läuft | komplettes Set |
| Token mit Wertpapier-Charakteristika | WpHG/Prospekt-Pflicht parallel | Klassifikation strittig | klar Utility/ART/EMT |
| Drittstaaten-Emittent | Nicht-MiCA-konform; Verbot | Equivalence-Prüfung | EU-Sitz |
| Vermarktung vor Lizenz | § 32 BaFin-Sanktion | Marketing zurückgehalten | erst nach Lizenz |

## Querverweise

- `fachanwalt-bank-kapitalmarktrecht-orientierung` — Triage
- `fachanwalt-bank-kapitalmarktrecht-cybertrading-anlagebetrug` — bei Token-Betrug
- `aussenwirtschaft-zoll-sanktionen` — bei Drittland-Sanktionen
- `geldwaeschepraevention-aml-kyc` — KYC/AML für Token-Emittent

## Quellen und Updates

Stand: 05/2026. MiCA-VO 2023/1114 (ART/EMT ab 30.6.2024; CASP ab 30.12.2024). EBA Final Guidelines zu Art. 35 und Art. 43 verabschiedet 2024. ESMA Q&A laufend. Bei MiCA 2 (in Planung) aktualisieren.
