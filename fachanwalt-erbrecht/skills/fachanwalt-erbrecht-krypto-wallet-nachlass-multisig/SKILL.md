---
name: fachanwalt-erbrecht-krypto-wallet-nachlass-multisig
description: "Sonderfall Nachlass Krypto-Vermoegen mit Multi-Sig-Wallet oder Hardware-Wallet ohne Seed-Phrase. Erblasser hat Wallet nicht eroeffnungsbereit hinterlassen. Erbenstellung § 1922 BGB plus technische Verwertbarkeit. Beweisfuehrung Eigentum am Krypto-Vermoegen. Steuerliche Bewertung § 23 EStG / ErbStG zum Todeszeitpunkt. Auseinandersetzung bei Erbengemeinschaft. Workflow Asset-Identifikation Wallet-Zugang Bewertung."
---

# Krypto-Nachlass — Multi-Sig-Wallet ohne Seed-Phrase

## Zweck

Spezial-Mandat: Erblasser hinterlässt Krypto-Vermögen, aber Erben kommen nicht an die Wallet. Hardware-Wallet ohne Seed-Phrase, Multi-Sig-Wallet mit Mit-Signern (Verstorbenem + Dritten), Custodial Account ohne Zugangsdaten — alle drei Konstellationen verlangen eigenes Vorgehen. Bewertung zum Todesstichtag für Pflichtteil + ErbSt nicht trivial.

## Eingaben

- Wallet-Typ (Hardware-Wallet Ledger/Trezor, Software-Wallet, Custodial Exchange, Multi-Sig)
- Vorhandene Anhaltspunkte (Briefverkehr, USB-Sticks, Notizen mit Seed-Wörtern, Recovery-Cards)
- Mit-Signer bei Multi-Sig bekannt?
- Token-/Coin-Bestand (Bitcoin, Ethereum, ERC-20, NFTs)
- Bewertung am Todestag (€)
- Erbengemeinschaft oder Alleinerbe
- Steuerwerte für ErbSt-Erklärung

## Rechtlicher Rahmen

### Erbrecht

- **§ 1922 BGB** — Gesamtrechtsnachfolge: Krypto als digitales Vermögensgut erfasst (BGH-Linie zu digitalen Inhalten: III ZR 183/17 "Facebook-Erbe")
- **§ 2032 BGB** — Erbengemeinschaft: Bruchteilsgemeinschaft am Krypto-Vermögen bis Auseinandersetzung
- **§ 2042 BGB** — Auseinandersetzung; bei Krypto regelmäßig durch Verkauf + Aufteilung Erlös
- **§ 2314 BGB** — Auskunftsanspruch Pflichtteilsberechtigter
- **§ 2050 BGB** — Ausgleichung bei Schenkung Wallet-Zugang zu Lebzeiten

### Steuerrecht

- **§ 12 ErbStG i.V.m. § 9 BewG** — Bewertung zum Todesstichtag (gemeiner Wert = Marktwert)
- **§ 23 EStG** — Bei Veräußerung durch Erben: Spekulationsfrist 1 Jahr, Übernahme der AK (BFH IX R 3/22)
- **BMF-Schreiben vom 10.5.2022** und **Folgeschreiben 22.11.2024** zur steuerlichen Behandlung Krypto

### Leitentscheidungen

- BGH, Urt. v. 12.7.2018 — **III ZR 183/17** "Facebook-Erbe" (Digitale Inhalte erbbar)
- BFH, Urt. v. 14.2.2023 — **IX R 3/22** (Krypto-Veräußerung § 23 EStG steuerpflichtig)
- BFH-anhängig (2025) zu Krypto-Bewertung bei Erbschaft mit illiquiden Token

## Konstellationen

### A — Hardware-Wallet ohne Seed-Phrase

- Wallet (Ledger/Trezor) physisch vorhanden, PIN unbekannt
- Bei 3 Fehlversuchen: Reset → Vermögen verloren wenn Seed nicht extern
- **Lösung**: forensische Datenwiederherstellung (selten erfolgreich) oder Trezor-Bruteforce-Tools (rechtlich grau)
- Bei Totalverlust: Bewertungsfrage — ErbSt auf nicht-zugängliches Vermögen?

### B — Multi-Sig-Wallet (2-of-3 / 3-of-5)

- Erblasser war einer von mehreren Signern
- Bei 2-of-3: zwei verbleibende Signer können verfügen (auch ohne Erblasser-Key)
- Bei 3-of-3: Erbe braucht Erblasser-Key zwingend
- **Rechtlich**: Mit-Signer haben Treuhand-/Fremdgeldverwahrungs-Pflichten (§ 667 BGB analog)

### C — Custodial Exchange ohne Zugangsdaten

- Bitvavo, Binance, Coinbase, Bitpanda — KYC-Konto
- Identitätsnachweis Erbe + Erbschein + Todesurkunde
- Plattformen haben Erbschafts-Prozesse (Coinbase: Estate, Bitvavo: Inheritance)
- Frist regelmäßig 12 Wochen

## Workflow

### Phase 1 — Asset-Identifikation

- Sichtung der Erblasserwohnung (USB, Backup-Karten, Schlüsselsymbole)
- E-Mail-Inbox-Durchsicht (Krypto-Exchange-Benachrichtigungen, Steuerbescheide)
- Bank-Auszüge auf Krypto-Käufe (Exchange-Überweisungen)
- Tax-Tools (Cointracking, Accointing) Login-Daten?

### Phase 2 — Wallet-Zugang

- Bei Hardware-Wallet: Notar-Versicherung Inventur + forensische Wiederherstellungsfirma
- Bei Multi-Sig: Mit-Signer kontaktieren, Erbschein vorzeigen
- Bei Custodial: Plattform-Erbschafts-Antrag (Erbschein, Todesurkunde, Identitätsnachweis Erbe)

### Phase 3 — Bewertung Todesstichtag

- Coinbase/Kraken-Kurs am Todestag (12:00 Uhr UTC oder lokale Schlusskurs)
- Bei illiquiden Token: Bewertungs-Stellungnahme Sachverständiger
- Mehrere Kurse zum Median (BMF-Schreiben 22.11.2024)

### Phase 4 — Steuererklärung ErbSt

- Anlage Vermögen ErbSt-Erklärung
- Krypto unter "übrige Wirtschaftsgüter"
- Bei nicht zugänglichem Krypto: Antrag § 33 ErbStG-Steuerstundung wegen Härte

### Phase 5 — Auseinandersetzung Erbengemeinschaft

- Wenn Erbengemeinschaft: gemeinsamer Verkauf > Aufteilung Erlös
- Oder Auflassungsverfahren bei NFTs (besonderer Wert für einzelne Erben)
- § 23 EStG-Folge: Spekulationsfrist beginnt mit Tod, AK übernommen

## Bewertungsbeispiel

```
Todesstichtag 15.5.2026, 12:00 UTC
Bestand:
  - 0,5 BTC × 65.000 EUR = 32.500 EUR
  - 4 ETH × 2.800 EUR    = 11.200 EUR
  - NFT Bored Ape #1234  = 5.000 EUR (Sachverständigen-Gutachten)
  - 1.000 USDT × 0,92    = 920 EUR
Total Krypto-Vermögen: 49.620 EUR (ErbSt-relevant)

Spekulationsfrist § 23 EStG (Verkauf durch Erben):
- Mit Erblasser-Erwerb < 1 Jahr: steuerpflichtig
- Mit Erblasser-Erwerb > 1 Jahr: steuerfrei
- Erbe übernimmt Anschaffungskosten + Anschaffungsdatum
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Seed-Phrase nicht auffindbar | Vermögen verloren; ErbSt-Härtefall | forensische Versuche | dokumentierte Seed-Aufbewahrung |
| Multi-Sig ohne Mit-Signer-Kooperation | Patt; ggf. § 894 ZPO | Verhandlung läuft | Mit-Signer mit Treuhand-Verpflichtung |
| ErbSt-Erklärung verzögert | Säumniszuschläge + § 30 ErbStG-Anzeigepflicht | Antrag § 33 ErbStG läuft | rechtzeitige Erklärung |
| Verkauf vor Wertermittlung | Falsche Bewertung; § 23 EStG-Risiko | nachträgliche Bewertung | Erst Bewertung dann Verkauf |
| Pflichtteils-Auskunft § 2314 unzulänglich | Pflichtteilsergänzung; Strafanzeige Erbschleicherei | Auskunft unvollständig | komplette Inventur |

## Querverweise

- `fachanwalt-erbrecht-orientierung` — Triage
- `fachanwalt-erbrecht-pflichtteilsergaenzung-2325` — bei Pflichtteilsstreit
- `fachanwalt-erbrecht-testamentsvollstreckung` — bei TV-Mandat
- `anw-dac7-dac8-plattformen-krypto` (steuerrecht-anwalt-und-berater) — DAC8-Meldepflichten

## Quellen und Updates

Stand: 05/2026. BGH III ZR 183/17 stehende Rspr. BFH IX R 3/22 zu Krypto-Veräußerung. BMF-Schreiben 22.11.2024 zur Krypto-Bewertung. DAC8 ab 1.1.2026. Bei BFH-Linie zu Bewertung bei Erbschaft aktualisieren.
