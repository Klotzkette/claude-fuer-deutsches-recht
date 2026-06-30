# Krypto-Multisig-Wallet — Technisches und rechtliches Dossier

**Az.:** KlKette 025/0422-ERB-EDE
**Stand:** 09.05.2025
**Bearbeitung:** RAin Steinkamp, technische Zuarbeit: IT-Sachverständige Petra Wandke (beratend)

---

## 1. Wallet-Grundstruktur

Der Erblasser verwaltete seinen Kryptovermögensbestand in einem sogenannten **3-of-5-Multisig-Wallet**. Bei einem Multisig-Wallet (Multi-Signature-Wallet) werden Transaktionen erst dann auf der Blockchain ausgeführt, wenn eine Mindestanzahl von vordefinierten privaten Schlüsseln (hier: 3 von 5) die Transaktion digital unterzeichnet haben.

Ein Zugriff oder eine Übertragung aus dem Wallet ist technisch also nur möglich, wenn mindestens 3 der 5 Schlüsselinhaber kooperieren. Kein einzelner Schlüsselinhaber kann einseitig auf die Wallet zugreifen.

---

## 2. Wallet-Adressen (syntaxgeprüft, intern verifiziert)

### 2.1 Bitcoin-Adressen (bech32 P2WSH)

Die Bitcoin-Wallet ist als native SegWit P2WSH-Adresse (bc1q…) implementiert, was für Multisig-Wallets auf dem Bitcoin-Netzwerk üblich ist:

```
bc1qmje7v4h8rfzpd4e3tnz6xpq9nk2wv9g0a7rkqwjfhcx2m4lsdqkfzppw8
```

*(Anmerkung Akte: Adresse ist ein Nachlassbestand; alle On-Chain-Guthaben dieser Adresse sind Nachlass.)*

### 2.2 Ethereum-Adresse

Die Ethereum-Bestände sind in einem Gnosis Safe Multisig-Contract (Ethereum Mainnet) gespeichert:

```
0x3dF9e2A4C8b1F74E6035aD7B9c2f1E8dF042cA7b
```

*(Contract-Adresse des Gnosis Safe; Contract-Owner: 5 Schlüssel, Threshold: 3)*

---

## 3. Schlüsselverteilung (laut Angaben Constantin, nicht vollständig verifiziert)

| Schlüssel | Inhaber | Verwahrungsort | Status |
|---|---|---|---|
| #1 (Erblasser) | Prof. Dr. Edelmann | Hardware-Wallet-Stick (Ledger Nano X) im Haustresoor Sonnenbergstraße 38a | Gefunden; liegt bei Marlies |
| #2 (Constantin) | Constantin Edelmann | Eigene Hardware-Wallet (Trezor Model T), Berlin | Vorhanden und zugänglich |
| #3 (Marlies) | Marlies Edelmann-Praun | Unbekannt; Marlies bestreitet, je einen Schlüssel erhalten zu haben | Streitig |
| #4 (RA Trotz) | RA Dr. Friedrich Trotz (†) | Kanzleinachlass? Hinterlegt bei Anwaltskammer? | Trotz verstorben Okt. 2023; Verbleib unklar |
| #5 (Backup) | — | Bankschließfach Nr. 441, Volksbank Esslingen, Plochinger Straße 33, 73728 Esslingen | Schließfach nur mit Erbschein zugänglich; Bank verlangt einstimmige Erbenanweisung |

---

## 4. Transaktionshistorie (Auszug, On-Chain verifiziert)

Die On-Chain-Daten sind öffentlich zugänglich; Transaktionsbeträge in EUR zum jeweiligen Transaktionskurs (Quelle: CoinGecko-Tageskurs):

### 4.1 Bitcoin-Wallet

| Datum | Typ | BTC | Kurs EUR | EUR-Wert | Gegenseite |
|---|---|---|---|---|---|
| 15.04.2019 | Einzahlung | +12,50 BTC | 4.280 EUR | 53.500 EUR | Kauf über Börse (Coinbase Pro) |
| 18.11.2020 | Einzahlung | +3,20 BTC | 13.150 EUR | 42.080 EUR | Kauf, Quelle unklar |
| 07.02.2021 | Auszahlung | −0,80 BTC | 38.600 EUR | 30.880 EUR | Empfängeradresse: bc1q7v…9r3 (= Constantin-Wallet?) |
| 12.12.2022 | Auszahlung | −1,20 BTC | 16.200 EUR | 19.440 EUR | Empfängeradresse: bc1q3n…4kp (= Constantin-Wallet?) |
| 22.03.2024 | Einzahlung | +0,50 BTC | 62.400 EUR | 31.200 EUR | Kauf |
| **Stand 12.03.2025** | | **14,20 BTC** | 60.850 EUR | **864.070 EUR** | |

### 4.2 Ethereum-Wallet (Gnosis Safe)

| Datum | Typ | ETH | Kurs EUR | EUR-Wert | Gegenseite |
|---|---|---|---|---|---|
| 08.09.2020 | Einzahlung | +80,00 ETH | 310 EUR | 24.800 EUR | Kauf |
| 14.02.2021 | Einzahlung | +40,00 ETH | 1.210 EUR | 48.400 EUR | Kauf |
| 23.12.2022 | Auszahlung | −8,00 ETH | 1.180 EUR | 9.440 EUR | Empfänger: 0x9aF7…2bC1 (= Constantin?) |
| 15.03.2024 | Auszahlung | −2,00 ETH | 3.120 EUR | 6.240 EUR | Empfänger: 0x9aF7…2bC1 |
| 04.07.2024 | Einzahlung | +35,50 ETH | 2.890 EUR | 102.595 EUR | Kauf, Herkunft unklar |
| **Stand 12.03.2025** | | **145,50 ETH** | 1.620 EUR | **235.710 EUR** | |

---

## 5. Technische Analyseergebnisse (vorläufig, SV Wandke)

- Die Auszahlungs-Transaktion vom 07.02.2021 (−0,80 BTC) trägt **zwei Signaturen**: Schlüssel #1 (Erblasser-Stick) und Schlüssel #2 (Constantin). Die dritte Signatur konnte nicht aus dem On-Chain-Datensatz ermittelt werden (Signaturmetadaten bei P2WSH nicht vollständig im Blockchain-Explorer sichtbar); es könnte Schlüssel #3 oder #5 gewesen sein.
- Dasselbe gilt für die Transaktion 12.12.2022 (−1,20 BTC) und 23.12.2022 (−8 ETH).
- Diese Transaktionen belegen, dass zu Lebzeiten Edelmanns Auszahlungen aus der Wallet stattgefunden haben; ob es sich um Schenkungen an Constantin oder um interne Walletbereinigungen handelt, ist rechtlich streitig.
- Die Einzahlung 04.07.2024 (35,50 ETH) ist herkunftsmäßig noch nicht geklärt. Sie erfolgte, als Edelmanns Gesundheitszustand bereits schlechter war. Ein Kauf ist möglich, eine Rückführung bereits abgehobener Mittel ebenso.

---

## 6. Rechtliche Qualifikation des Multisig-Problems

### 6.1 Kryptowährung als Nachlassmasse

Nach der deutschen Rechtslage sind Kryptowährungen als Eigentum im erbrechtlichen Sinne zu behandeln. Das Eigentumsrecht an BTC und ETH geht mit dem Tod auf die Erbengemeinschaft über (§§ 1922, 2032 BGB). Das Testament bestätigt dies ausdrücklich.

### 6.2 Technische Kontrolle vs. rechtliche Eigentümerstellung

Das Recht an den Kryptowährungen (als Erbengemeinschaft) ist strikt zu trennen von der faktischen Möglichkeit, auf die Wallet zuzugreifen. Constantin hält Schlüssel #2; damit allein kann er technisch nicht auf die Wallet zugreifen (3-of-5-Quorum). Wenn er jedoch Schlüssel #1 (Erblasser-Stick, bei Marlies) unbefugt nutzt und/oder den Backup-Schlüssel #5 eigenständig verschafft, könnte er faktisch Zugriff erlangen, ohne rechtlich dazu berechtigt zu sein.

### 6.3 Constantins Ausschlagung und Wallet

Constantin hat die Erbschaft ausgeschlagen. Damit ist er kein Erbe. Er hat keinerlei Verwaltungs- oder Verfügungsbefugnis über den Nachlass (§§ 1953, 2038 BGB e contrario). Sein Schlüssel #2 ist sein persönliches Eigentum; aber das Recht, ihn zur Freischaltung der Wallet zu benutzen und Gelder zu verschieben, hat er nicht. Jeder entsprechende Zugriff wäre:
- Zivilrechtlich: Eingriff in das Gesamthandseigentum der Erbengemeinschaft (§ 2032 BGB), Bereicherungsanspruch (§ 812 BGB), Schadensersatz (§ 823 BGB).
- Strafrechtlich: Je nach Konstruktion — Untreue (§ 266 StGB) scheidet mangels Treueverhältnis aus; möglicherweise Unterschlagung (§ 246 StGB) oder Computerbetrug (§ 263a StGB), wenn technische Systeme manipuliert werden.

### 6.4 Schlüssel #1 bei Marlies

Der Erblasser-Stick liegt bei Marlies. Sie ist Miterbin (1/4) und damit Mitglied der Erbengemeinschaft. Die Übergabe des Sticks an Constantin oder die gemeinsame Benutzung durch Marlies und Constantin ohne Zustimmung der anderen Erben (Henrike, Marie-Theres) wäre ebenfalls ein Eingriff in die Gesamthandsrechte.

### 6.5 Bankschließfach Volksbank Esslingen

Das Schließfach (Nr. 441) war auf Edelmann allein eröffnet. Nach dem Tod ist ein Zugang durch Vorlage eines Erbscheins möglich. Die Bank verlangt darüber hinaus eine einstimmige Weisung der Erbengemeinschaft, wenn kein Testamentsvollstrecker bestellt ist. Da die Erbengemeinschaft derzeit dreiköpfig ist (Marlies, Henrike, Marie-Theres nach Constantins Ausschlagung), müssen alle drei gemeinsam handeln. Dies blockiert die Situation, solange keine Einigkeit besteht.

---

## 7. Offene Punkte

- Schlüssel #4 (Trotz-Kanzleinachlass): Anfrage bei Anwaltskammer BW läuft (→ Aktenstück 15).
- Schlüssel #3 (Marlies): Sie bestreitet, je einen Schlüssel erhalten zu haben. Ob das stimmt, ist unklar. Constantin behauptet das Gegenteil. Beweis? → Aktenstück 22.
- Herkunft der Einzahlung vom 04.07.2024 (35,50 ETH): noch ungeklärt.

Diagramm zur Schlüsselverteilung: `jpg/multisig_diagramm_5_schluessel.jpg`.
Tresor-Inventar: `jpg/tresor_inhalt_inventarisierung.jpg` und `pdfs/multisig_protokoll_tresor_inventar.pdf`.
