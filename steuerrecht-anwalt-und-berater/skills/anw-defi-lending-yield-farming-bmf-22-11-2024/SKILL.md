---
name: anw-defi-lending-yield-farming-bmf-22-11-2024
description: "Steuerliche Behandlung DeFi-Lending Yield Farming Liquidity Mining nach BMF-Schreiben vom 22.11.2024 (Folge zum BMF-Krypto-Schreiben 10.5.2022). Einkuenfte § 22 Nr. 3 EStG bzw. § 20 EStG. Token-Tausch als Veraeusserung § 23 EStG mit Spekulationsfrist. Wrapped Tokens Yield Tokens LP-Tokens. Steuererklaerungs-Pflicht inkl. DAC8. Workflow Wallet-Analyse Cointracking Erklaerung."
---

# DeFi-Lending / Yield Farming — Steuerliche Behandlung BMF 22.11.2024

## Zweck

Spezial-Mandat: Mandant nutzt DeFi-Protokolle (Aave, Compound, Curve, Yearn, Uniswap V3, Lido, EigenLayer) für Lending, Yield Farming, Liquidity Mining, Staking. Anwaltliche Beratung zur **steuerlichen Erklärung** nach **BMF-Schreiben vom 22.11.2024** (Folge zum BMF-Krypto-Schreiben 10.5.2022). DeFi-Komplexität: jeder Token-Tausch ist potenziell Veräußerung; LP-Token-Einlage = Tausch; Rewards = Einnahmen.

## Eingaben

- Genutzte Protokolle (Aave, Compound, Uniswap, Lido, EigenLayer)
- Aktivitäten (Lending, Borrowing, LP, Staking, Restaking)
- Bestand Wallets (Adressen für Blockchain-Analyse)
- Tax-Tool im Einsatz? (Cointracking, Accointing, Koinly, Crypto Tax)
- Veranlagungszeitraum
- Einkünfte-Höhe (Steuersatz-Relevanz)

## Rechtlicher Rahmen

- **BMF-Schreiben vom 10.5.2022** — Grundlinien Krypto-Besteuerung
- **BMF-Schreiben vom 22.11.2024** — Konkretisierung DeFi-Tatbestände
- **§ 22 Nr. 3 EStG** — Sonstige Einkünfte (Staking-Rewards, Lending-Zinsen, soweit nicht § 20)
- **§ 20 Abs. 1 Nr. 7 EStG** — Kapitalvermögen (Zinsähnliche Rewards)
- **§ 23 EStG** — Privates Veräußerungsgeschäft (Spekulationsfrist 1 Jahr; bei Lending-Token argumentativ erweitert auf 10 Jahre nach altem BMF 2022, durch JStG 2022 abgeschwächt)
- **§ 15 EStG** — Gewerbliche Einkünfte bei Daytrading-Charakter
- **§ 256 HGB / EStG-AfA-Liste** — Bei betrieblichem DeFi
- **DAC8 (KryptoStG 2026)** — Meldepflicht der CASP

### Leitentscheidungen

- BFH, Urt. v. 14.2.2023 — **IX R 3/22** (Krypto als Wirtschaftsgut)
- BFH-anhängig zu DeFi-Spezifika (2025/2026)
- FG Münster, Urt. v. 25.5.2023 — 9 K 26/23 (Staking-Rewards § 22 Nr. 3 EStG)
- FG Baden-Württemberg-anhängig zu Liquidity-Mining-Token-Tausch

## Steuerliche Behandlung pro Aktivität

### A — Lending (Aave, Compound)

- Einzahlung in Lending-Pool: kein Steuer-Tatbestand (gleicher Token; BMF 22.11.2024 anders sieht es bei Wrapped Tokens aWETH ≠ ETH)
- **Wrapped Token (aWETH, cUSDC)**: BMF 22.11.2024 sieht Tausch ETH→aWETH als steuerbar an (Veräußerung § 23 EStG)
- **Lending-Zinsen** (variabel): § 20 Abs. 1 Nr. 7 EStG (Kapitalvermögen) — KapitalErtragsteuer 25 % + Soli + KiSt
- **Rückzug aWETH→ETH**: erneut steuerbar (Tausch zurück)

### B — Liquidity Mining (Uniswap V3, Curve, Balancer)

- Einzahlung Token-Paar in Pool gegen LP-Token: **Tausch § 23 EStG**
- Rewards (UNI, CRV, BAL): **§ 22 Nr. 3 EStG**
- Impermanent Loss: nicht steuerlich abzugsfähig (BMF-Linie)
- LP-Auflösung: erneut Tausch

### C — Staking (Lido, EigenLayer)

- Einzahlung in Staking-Vertrag (z. B. ETH→stETH): **Tausch § 23 EStG** (BMF 22.11.2024 hält stETH ≠ ETH)
- Rewards: § 22 Nr. 3 EStG
- Spekulationsfrist 1 Jahr (JStG 2022 hat 10-Jahres-Frist aus BMF 2022 wieder zurückgenommen)

### D — Restaking (EigenLayer)

- Doppel-Tausch: ETH→stETH→reSt-Token; jeder Schritt steuerbar
- Rewards aus Restaking: § 22 Nr. 3 EStG
- Slashing-Verlust: steuerlich abzugsfähig (Verlust-Verrechnung mit § 22 Nr. 3 EStG-Einkünften)

### E — Bridging (zwischen Chains)

- BMF 22.11.2024 differenziert: Funktional gleicher Token = kein Tausch; technisch Wrapped Token = Tausch
- Beispiel: ETH→WETH (Ethereum) = nicht-tauschbar (Liquidator/User-Identität); ETH→cbETH = Tausch
- Polygon-, Optimism-, Arbitrum-Bridges typisch nicht steuerbar (User-Identität bleibt)

## Workflow

### Phase 1 — Wallet- und Protokoll-Inventur

- Alle genutzten Wallet-Adressen sammeln (MetaMask, Ledger, Argent)
- Blockchain-Analyse (Etherscan, Arbiscan, Polygonscan)
- Protokoll-Liste mit Beträgen

### Phase 2 — Datenaufbereitung Tax-Tool

- Cointracking / Accointing / Koinly Import via API
- Manuelle Korrekturen (LP-Token-Tausch, Slashing-Verlust)
- BMF-Schreiben-konforme Bewertung (Tageskurs bei Tausch)

### Phase 3 — Steuererklärung

- **Anlage SO** für § 22 Nr. 3 EStG (Staking, Lending-Rewards bei nicht-Kapitalvermögen-Auslegung)
- **Anlage KAP** für § 20 EStG (Kapitalvermögen Lending-Zinsen)
- **Anlage V** für § 23 EStG (Veräußerungsgeschäfte)
- DAC8-konforme Mitwirkung mit CASP-Daten

### Phase 4 — Bei Selbstanzeige § 371 AO

- Bei nicht erklärtem DeFi-Vermögen aus Vorjahren: Selbstanzeige sinnvoll
- Vor DAC8-Erstmeldung 31.1.2027 dringend (Sperrwirkung droht)
- Vollständigkeit zwingend (10 Jahre rückwärts)

### Phase 5 — Bei Außenprüfung

- Steuerberater + Anwalt parallel
- BMF-Schreiben-Konformität nachweisen
- Beweissicherung Blockchain-Daten (Off-Chain-Logs schwer reproduzierbar)

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Nicht erklärtes DeFi-Vermögen ab 2024 | DAC8 deckt es 2027 auf; § 371 AO-Selbstanzeige vor Tatentdeckung | Selbstanzeige läuft | rechtzeitig erklärt |
| Wrapped-Token-Tausch nicht erfasst | Steuerverkürzung bei jedem aWETH→ETH-Move | Korrektur § 153 AO | volle Erfassung |
| Daytrading-Niveau | § 15 EStG (Gewerblich) statt § 23 — höherer Steuersatz | Klärung Gewinn-/Volumen-Schwelle | klar privat |
| Liquidity-Mining-Rewards in nicht-€ | Kursbewertung Tageskurs Pflicht | Tool-Bewertung | korrekt bewertet |

## Querverweise

- `anw-selbstanzeige-371` — bei nachträglicher Erklärung
- `anw-dac7-dac8-plattformen-krypto` — DAC8-Meldepflichten
- `anw-steuerbescheid-analyse` — Bescheid-Auswertung
- `anw-aussenpruefung-strategien` — bei BP
- `fachanwalt-erbrecht-krypto-wallet-nachlass-multisig` — bei Krypto-Erbschaft

## Quellen und Updates

Stand: 05/2026. BMF-Schreiben 22.11.2024. BFH IX R 3/22. FG Münster 9 K 26/23. KryptoStG 1.1.2026. DAC8 Erstmeldung 31.1.2027. Bei BFH-Linie zu DeFi-Tausch aktualisieren.
