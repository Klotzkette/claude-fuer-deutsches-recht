# Gegenueberstellung self-hosted vs. custodial Krypto-Wallet

## Kernunterschied auf einen Blick

| Kriterium | Wallet A self-hosted (Ledger Nano X) | Wallet B custodial (Bitpanda) |
| --- | --- | --- |
| Verwahrform | privater Schluessel beim Schuldner | privater Schluessel beim Verwahrer |
| Anspruch gegen Dritten | nein | ja, schuldrechtlich gegen Bitpanda |
| Vollstreckungsart | Sachpfaendung Paragrafen 808 ff. ZPO | Forderungspfaendung Paragrafen 829, 835 ZPO |
| Vollstreckungsorgan | Gerichtsvollzieher (mit Durchsuchungsanordnung Paragraf 758a) | Vollstreckungsgericht (PfUEB) |
| Drittschuldner | keiner | Bitpanda GmbH Wien |
| Mitwirkung des Schuldners | zwingend (PIN, Seed) | nicht erforderlich |
| Zwangsmittel bei Verweigerung | Paragraf 802g (VA) plus Paragraf 888 (Mitwirkung) | nicht erforderlich |
| Geografisches Risiko | gering (Geraet in DE) | hoch (Drittschuldnerin in AT) |
| Zustellungsregime | GV-Termin vor Ort | EU-Zustellungs-VO 2020/1784 |
| Eilrechtsschutz | Durchsuchungsanordnung | oest. Sicherheitsverfuegung Paragraf 379 EO |
| Verwertungsrisiko | Verlustgefahr (Selbstverwertung Wallet) | gering (Bitpanda zahlt EUR aus oder verwertet selbst) |
| Volatilitaetsrisiko | hoch | hoch |
| Zeithorizont bis EUR-Erloes | 4-6 Wochen | 8-14 Wochen |
| Skills (zwangsvollstreckung) | zv-mobiliar-gv-auftrag, zv-vermoegensauskunft-gv | zv-pfueb-mieter-finanzamt, zv-elektronische-zustellung-2027 |

## Konsequenzen fuer die Beratung

### Glaeubigerseite

- Self-hosted-Wallets sind nur greifbar, wenn der Schuldner kooperiert oder das Geraet **vor Ort** beim Gerichtsvollzieher zugaenglich ist. Ohne PIN ist das Geraet wertlos.
- Custodial-Wallets sind genauso pfaendbar wie ein Bankkonto, aber bei auslaendischem Verwahrer ist die Zustellung deutlich aufwendiger.
- Bei einer Mischlage Wallet A + Wallet B ist beides parallel zu betreiben, damit der Schuldner nicht in den Zustellungszeitraum hinein abziehen kann.
- Skill `zv-elektronische-zustellung-2027` weist bei deutschen Krypto-Verwahrern (Bitpanda Asset Management GmbH Frankfurt) auf die eBO-Pflicht ab 1.10.2027 hin - die Wiener Mutter ist davon **nicht** erfasst, dort gilt oest. ERV.

### Schuldnerseite

- Verweigerung der PIN ist KEIN Schweigerecht im Vollstreckungsverfahren; sie kann Paragraf 888 ZPO ausloesen. Anders, soweit ein **Strafverfahren** im Hintergrund stehen koennte (Steuerhinterziehung etc.) - dann greift das Selbstbelastungsverbot Art. 6 EMRK.
- Bei Bitpanda kann der Schuldner versuchen, vor Zustellung das Guthaben abzuziehen; das kann Anfechtung Paragrafen 129 ff. InsO bei spaeterer Insolvenz oder Paragrafen 1, 4 AnfG (Glaeubigeranfechtung) ausloesen. Beratung zwingend.
- P-Konto-Regeln Paragraf 850k ZPO gelten **nicht** fuer Krypto-Konten.

### Schnittstellen Plugin-Architektur

- `zwangsvollstreckung/zv-mobiliar-gv-auftrag` ist Hauptansatz fuer Wallet A.
- `zwangsvollstreckung/zv-pfueb-mieter-finanzamt` ist Hauptansatz fuer Wallet B.
- `prozessrecht/elektronischer-rechtsverkehr` (anderes Plugin) fuer eBO-Themen.
- `insolvenzforderungsanmeldungspruefung` fuer das Szenario, dass der Schuldner Verbraucherinsolvenz beantragt.

## Praxisempfehlung Sparkasse Niederrhein

1. **Sofort** Sachpfaendungsantrag fuer Wallet A einreichen (`zv-mobiliar-gv-auftrag`).
2. **Sofort** PfUEB fuer Wallet B einreichen, Zustellung nach EU-Zustellungs-VO.
3. **Parallel** oesterreichischen Korrespondenzanwalt mit Eilantrag Paragraf 379 oest. EO beauftragen.
4. **Wiedervorlage** GV-Termin 12.6.2026.
5. **Wiedervorlage** Drittschuldnererklaerung Bitpanda 24.7.2026.
6. **Hauptweg** bleibt dingliche Vollstreckung Beethovenstrasse 12 ab 14.10.2026.
