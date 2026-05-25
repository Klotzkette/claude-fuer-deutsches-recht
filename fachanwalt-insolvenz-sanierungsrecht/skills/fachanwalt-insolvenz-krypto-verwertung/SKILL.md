---
name: fachanwalt-insolvenz-krypto-verwertung
description: "Verwertung Krypto-Assets im Insolvenzverfahren durch Insolvenzverwalter. Massezugehoerigkeit § 35 InsO bei Wallet ohne Seed-Phrase. Multi-Sig-Wallets Mit-Signer-Anspruechen. Aussonderung § 47 InsO Custodial-Exchanges (Bitvavo Coinbase). Verwertungsstrategie Stueckweise-Verkauf vs. Auktion vs. OTC. Forensische Wallet-Rekonstruktion BfJ-Insolvenz-Forensik. BMF 22.11.2024 zur insolvenz-steuerlichen Behandlung."
---

# Krypto-Assets im Insolvenzverfahren — Verwertung

## Zweck

Insolvenzverwalter (oder anwaltliche Berater) bei der Sicherung, Aussonderung und Verwertung von Krypto-Vermögen im Insolvenzverfahren. Drei typische Konstellationen: (a) Insolvenzschuldner hat eigene Wallet, (b) Krypto-Custodial-Exchange ist insolvent, (c) Multi-Sig-Konstellation mit Mit-Signern.

## Eingaben

- Wallet-Typ: Hardware, Software, Custodial Exchange
- Seed-Phrase / Recovery-Schlüssel auffindbar?
- Multi-Sig-Konstellation mit identifizierbaren Mit-Signern?
- Bestand (BTC, ETH, ERC-20, NFTs, Stablecoins)
- Stichtagswert (Eröffnungsdatum)
- Erwartete Massehöhe vor Krypto-Berücksichtigung
- Forderungen Dritter (Custodial Exchange-Kunden bei FTX-ähnlichem Szenario)

## Rechtlicher Rahmen

### Insolvenzrecht

- **§ 35 InsO** — Massebegriff: Krypto-Vermögen gehört regelmäßig zur Masse (BFH IX R 3/22 zur "Wirtschaftsgut"-Qualität; KOMM-Insolvenzverwalter zu § 35)
- **§ 47 InsO** — Aussonderung: bei Custodial-Konstruktion (Insolvenzverwalter ≠ Eigentümer)
- **§ 80 InsO** — Verwaltungs- und Verfügungsbefugnis des Verwalters
- **§ 159 InsO** — Verwertungsplan
- **§ 161 InsO** — Freihändige Verwertung
- **§ 166 InsO** — Verwertung bei Sicherungsrechten

### Steuerrecht

- **BMF-Schreiben vom 22.11.2024** — steuerliche Behandlung Krypto bei Insolvenz: Verwertungserlös als Einkunft des Verwalters; Spekulationsfrist § 23 EStG durchläuft Insolvenz
- **§ 55 InsO** — Masseverbindlichkeiten (Steuer auf Krypto-Veräußerung)

### Leitentscheidungen

- BFH, Urt. v. 14.2.2023 — **IX R 3/22** (Krypto als Wirtschaftsgut § 23 EStG)
- AG Stuttgart, Beschl. v. 12.6.2023 — 5 IN 248/22 (Wallet-Zugang bei Insolvenzschuldner)
- LG Köln, Urt. v. 12.3.2024 — 22 O 25/23 (Aussonderungsanspruch Krypto-Exchange-Kunde)
- US-Bankruptcy Court SDNY (FTX, Celsius) — Vergleichswert für Custodial-Insolvenz

## Konstellationen

### A — Insolvenzschuldner hat eigene Wallet

- Wallet gehört zur Masse (§ 35 InsO)
- Verwalter benötigt Zugang: Seed-Phrase, PIN, Recovery-Karte
- Schuldnerpflicht zur **Mitwirkung § 97 InsO** (mit Strafbewehrung § 156 InsO)
- Bei Verweigerung: Eidesstattliche Versicherung § 98 InsO + Erzwingungshaft

### B — Krypto-Exchange ist insolvent (z. B. Custodial-Wallet)

- Kunden haben **Aussonderungsanspruch § 47 InsO**, wenn vertraglich Custody (nicht Darlehen) vereinbart
- AGB-Prüfung entscheidend: "Treuhand-Verwahrung" vs. "Krypto-Darlehen"
- FTX-Linie: Custodial gilt als Sondervermögen → Aussonderung möglich
- Celsius-Linie: Lend-Programs sind Darlehen → Insolvenzgläubiger
- BaFin-Lizenz § 1 Abs. 1a Nr. 8 KWG-Kryptoverwahrung relevant

### C — Multi-Sig mit Mit-Signern

- Mit-Signer haben Treuhand-/Fremdgeldverwahrungs-Pflichten (§ 667 BGB analog)
- Insolvenzverwalter tritt in Position des Insolvenzschuldners
- Bei 2-of-3 mit Verwalter + 1 Mit-Signer = Verfügung möglich
- Bei 3-of-3: Verwalter braucht Kooperation aller verbleibenden Signer

## Workflow Verwertung

### Phase 1 — Sicherung der Wallet

- Sofortige Suchverfügung Wohnung Schuldner (§ 99 InsO)
- Sicherstellung Hardware-Wallets, USB-Sticks, Papier-Backups
- Sichtung E-Mail-Inbox (Exchange-Benachrichtigungen)
- Beschlagnahme-Anordnung bei Verdacht auf Verbergung

### Phase 2 — Bewertung Eröffnung-Stichtag

- Kurs am Eröffnungstag (12:00 Uhr UTC) — wichtig für Insolvenz-Quote
- Mehrere Kurse zum Median (Coinbase, Kraken, Bitstamp)
- Bei illiquiden Token: Sachverständigen-Gutachten

### Phase 3 — Forensische Wallet-Rekonstruktion (bei verlorenem Zugang)

- Hardware-Wallet ohne PIN: Bruteforce-Tools (rechtlich grau; Verwalter darf bei eigener Verwahrung)
- Forensische Datenwiederherstellung Software-Wallet (Festplattensicherung)
- Blockchain-Analyse für Wallet-Adresse-Identifikation (Chainalysis, Elliptic)

### Phase 4 — Verwertungs-Entscheidung

| Strategie | Vorteil | Nachteil |
|---|---|---|
| **Stückweise an Börse** | einfach, transparent | Preisbewegung; bei großem Bestand Market Impact |
| **OTC-Verkauf** | besserer Preis bei Größe | KYC/AML-Risiko bei Gegenpartei |
| **Auktion** | klare Verwertung | Verwaltungsaufwand |
| **Sachausschüttung an Gläubiger** | Erhalt für Gläubiger | Steuer-Komplexität |

### Phase 5 — Verteilung Erlös

- Versteuerung Erlös: § 55 InsO Masseverbindlichkeit
- Berücksichtigung BMF 22.11.2024 zur Steuerpflicht
- Verteilung an Gläubiger nach Insolvenzplan

## Sonderprobleme

### Verloren-geglaubte Wallets (Hardware ohne Seed)

- Bewertung als "wirtschaftlich wertlos" möglich (mit Gutachten)
- Aufnahme in Inventar mit Vermerk "unzugänglich"
- Bei späterer Auffindbarkeit Nachtragsverwertung

### Crypto-Lending mit Schuldner als Geldgeber

- Insolvenzschuldner hat Krypto verliehen (Compound, Aave); Rückforderung möglich
- Smart-Contract-Auflösung erforderlich

### NFTs als Sonderfall

- Bewertungs-Komplexität (Sachverständige PR Sotheby's, OpenSea-Floor)
- Manchmal nur OTC-Verwertbar
- Kunst-Steuer-Implikationen

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Schuldner verweigert Wallet-Zugang | § 98 InsO Erzwingung; Strafanzeige § 283 StGB | Kooperation kommt | volle Mitwirkung |
| Custodial-Exchange in EU-Drittland (FTX-Bahamas-Modell) | Aussonderungsanspruch unklar; teurer Prozess | Klärung läuft | EU-Custodial mit MiCA |
| Steuerliche Veräußerungsfrist § 23 EStG übersehen | unnötige Steuerbelastung | Klärung läuft | Strategie BMF-konform |
| Schwarzgeld-Indikatoren (StA-Beteiligung) | Strafrechtliche Beschlagnahme + Insolvenz-Konflikt | Klärung läuft | sauber dokumentiert |

## Querverweise

- `fachanwalt-insolvenz-sanierungsrecht-orientierung` — Triage
- `fachanwalt-insolvenz-sanierungsrecht-anfechtungsklage-verwalter` — Anfechtungsmöglichkeit Krypto-Übertragungen
- `fachanwalt-erbrecht-krypto-wallet-nachlass-multisig` — Krypto-Erbschaft (analog Konstellation)
- `anw-dac7-dac8-plattformen-krypto` — DAC8-Meldepflichten Plattformen

## Quellen und Updates

Stand: 05/2026. BFH IX R 3/22, BMF-Schreiben 22.11.2024. AG Stuttgart 5 IN 248/22 als frühe Praxis. FTX/Celsius US-Verfahren als Vergleichsmaterial. Bei BGH-Linie zu Krypto-Aussonderung aktualisieren.
