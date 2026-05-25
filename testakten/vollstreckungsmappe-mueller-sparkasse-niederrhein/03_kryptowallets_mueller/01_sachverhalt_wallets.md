# Krypto-Wallets - Sachverhalt aus der Vermoegensauskunft

## Quelle

Vermoegensauskunft Bernd Mueller vor GV Olaf Wendt, AG Krefeld, am 22.4.2026, 10:30 Uhr. Schuldner gab unaufgefordert an, ueber Kryptowerte zu verfuegen. Belege wurden zur Akte gereicht (Anlage K 5 und K 6, siehe `originale/`).

## Wallet A - self-hosted (Hardware-Wallet Ledger Nano X)

| Position | Inhalt |
| --- | --- |
| Geraet | Ledger Nano X, Seriennummer S/N nicht angegeben |
| Aufbewahrung | Heimsafe Beethovenstrasse 12; Seed-Phrase 24 Woerter auf Stahlblech "Cryptosteel Capsule" im selben Safe |
| Backup | digitale Kopie auf MacBook Pro 14 Zoll des Schuldners (verschluesselt) |
| Software | Ledger Live, Sparrow Wallet, BlueWallet auf iPhone |
| Adressen (Stichproben) | bc1qz0u4fhk7qa9c... (BTC), 0xA9F12dE4BCb78a... (ETH/USDT ERC-20) |
| Bestand laut VA | 0,42 BTC, 11.500 USDT (ERC-20) |
| Marktwert per 22.4.2026 | 0,42 BTC zu ca. 95.000 USD = 39.900 USD; 11.500 USDT = 11.500 USD; Summe ca. 47.000 USD bzw. rd. 43.000 EUR |
| Rechtsnatur Wallet | reines technisches Werkzeug; **keine** Forderung gegen einen Dritten; der Schuldner ist allein verfuegungsberechtigt durch Besitz der privaten Schluessel |
| Drittschuldner | **keiner** - es gibt schlicht keinen Anspruch eines Dritten, gegen den vollstreckt werden koennte |

## Wallet B - custodial (Bitpanda GmbH, Wien)

| Position | Inhalt |
| --- | --- |
| Anbieter | Bitpanda GmbH, Stella-Klein-Loew-Weg 17, 1020 Wien |
| Erlaubnis | Krypto-Verwahrer nach Paragraf 1 Abs. 1a Satz 2 Nr. 6 KWG durch BaFin (deutsche Tochter Bitpanda Asset Management GmbH; ggf. zusaetzlich oesterreichische FMA-Aufsicht) |
| Konto-Nr. | 5598-77821-MUE |
| Login | uebliche 2FA mit Email + TOTP |
| Bestand laut VA | 0,18 BTC, 4.300 USDC, 22.000 EUR Fiat |
| Marktwert per 22.4.2026 | 0,18 BTC = ca. 17.100 USD; 4.300 USDC = 4.300 USD; 22.000 EUR = 22.000 EUR; Summe rd. 42.000 EUR |
| Rechtsnatur Wallet | schuldrechtlicher Herausgabe- bzw. Auszahlungsanspruch des Schuldners gegen Bitpanda als Krypto-Verwahrerin; Bitpanda haelt die privaten Schluessel und ist treuhaenderische Verwahrerin |
| Drittschuldnerin | Bitpanda GmbH, Wien |

## Konsequenz fuer die Vollstreckung

Aus dem Unterschied folgt die ganz unterschiedliche Vollstreckungsmechanik:

- **Wallet A self-hosted** ist eine **Sachpfaendung** im Sinne der Paragrafen 808 ff. ZPO mit Eigentuemlichkeiten: gepfaendet wird das Geraet (Ledger), zugaenglich werden die Krypto-Bestaende erst ueber die Seed-Phrase, die als verkoerperte Information eigenstaendig gepfaendet wird (BGH-Linie bislang nicht abschliessend; obergerichtlich AG Heidelberg 21.6.2022 - 5 M 1124/22, LG Stuttgart 31.5.2023 - 19 T 22/23 zu Krypto-Sachpfaendungen).
- **Wallet B custodial** ist eine **Forderungspfaendung** Paragrafen 829, 835 ZPO gegen Bitpanda als Drittschuldnerin. Auslandsbezug (Sitz Wien): EuKtPVO oder Zustellung nach EU-Zustellungs-VO 2020/1784.

Die folgenden beiden Dateien (`02_wallet_a_selfhosted.md`, `03_wallet_b_custodial.md`) bauen die jeweilige Mechanik aus. `04_gegenueberstellung.md` fasst zusammen.
