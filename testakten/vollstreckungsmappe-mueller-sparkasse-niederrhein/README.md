# Testakte: Vollstreckungsmappe Sparkasse Niederrhein gegen Mueller

## ⬇️ Direkt-Download

| Testakte | Direkt-Download |
| --- | --- |
| `testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein` (diese Akte) | [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip) |

Die Testakte ist **kein Teil des Plugins** und wird separat als ZIP-Datei aus dem GitHub-Release geladen. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.


Sammelakte fuer drei parallele Vollstreckungsvorgaenge der Sparkasse Niederrhein (Glaeubigerin) gegen die Familie Mueller. Alle Personen, Konten, Adressen, Aktenzeichen, Wallet-Adressen und Beraternamen sind frei erfunden. IBANs sind keine echten Bankverbindungen, BICs sind Beispielwerte.

## Mandantenkonstellation

- **Glaeubigerin:** Sparkasse Niederrhein AOeR, Krefeld, vertreten durch Rechtsanwaeltin Dr. Henrike Boehringer, Krefeld (Mandantin des Plugins).
- **Schuldner 1:** Bernd Mueller, geb. 14.3.1968, Eigentuemer des Einfamilienhauses Beethovenstrasse 12, 47800 Krefeld. Haupt-Sicherungsgeber, vertritt zugleich die Mueller Kuechen GmbH.
- **Schuldnerin 2 (Mitschuldnerin):** Dorothea Mueller, geb. 7.9.1971, Ehefrau, Miteigentuemerin Beethovenstrasse 12.
- **Schuldnerin 3 (Drittschuldnerin gegen Kundin Mueller):** Mueller Kuechen GmbH, AG Krefeld HRB 14 432, Geschaeftsfuehrer Bernd Mueller. Hier nicht Schuldnerin der Sparkasse, sondern Drittschuldnerin in einer separaten Mietzinspfaendung.

## Drei Vorgaenge in einer Mappe

### 01 - Vollstreckung aus notarieller Grundschuld

Dingliche Vollstreckung in das selbstgenutzte Einfamilienhaus Beethovenstrasse 12. Sicherungsgrundschuld 380.000 EUR aus 2017, Notar Dr. Berghoff, URNr 882/2017. Forderung valutiert per 31.3.2026 mit 261.480,73 EUR offen aus Privatdarlehen 4717-8821 zur Sanierung. Bernd und Dorothea Mueller sind drei Monate im Rueckstand, Kuendigung mit Schreiben vom 5.4.2026 erklaert, Kuendigung der Grundschuld nach Paragraf 1193 BGB am 12.4.2026.

Skills: `zv-notarielle-urkunde-grundschuld`, `zv-zvg-antrag-glaeubiger`, ggf. `zv-pfueb-bank` (persoenliche Vollstreckung parallel).

### 02 - Einfache Kontopfaendung

Aus demselben Privatdarlehen (Restforderung 261.480,73 EUR) wird parallel der Lohnzufluss des Schuldners gepfaendet. Bernd Mueller bezieht Geschaeftsfuehrervergehalt der Mueller Kuechen GmbH (Drittschuldner) ueber das Geschaeftskonto bei der Postbank, IBAN DE89 1001 0010 0987 6543 21. Dorothea Mueller fuehrt ihr Privatkonto bei der DKB, IBAN DE12 1203 0000 5511 2233 00. Beide Konten werden gepfaendet, P-Konto-Schutz wird voraussichtlich beantragt.

Skills: `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`, `zv-pfaendungstabelle-2025`, `zv-elektronische-zustellung-2027`.

### 03 - Verpfaendung Bitcoin- und Stablecoin-Wallets

Bei der Vermoegensauskunft am 22.4.2026 hat Bernd Mueller offengelegt, dass er ueber zwei Wallets verfuegt:

- **Wallet A (self-hosted):** Hardware-Wallet Ledger Nano X mit Seed-Phrase und Software-Wallet auf seinem MacBook. Bestand laut Selbstauskunft 0,42 BTC und 11.500 USDT zum Stichtag.
- **Wallet B (custodial):** Konto bei der Bitpanda GmbH (Wien) als Krypto-Verwahrstelle nach Paragraf 1 Abs. 1a Satz 2 Nr. 6 KWG, Bestand 0,18 BTC, 4.300 USDC und 22.000 EUR Fiat-Guthaben.

Beide Vermoegensgegenstaende werden vollstreckt - mit unterschiedlichen Mechaniken, die diese Akte gegenueberstellt.

Skills: `zv-mobiliar-gv-auftrag` (self-hosted), `zv-pfueb-mieter-finanzamt` (custodial Drittschuldner), `zv-vermoegensauskunft-gv`, `zv-abwehr-schuldner` (Schuldnerseite Selbstbelastungsverweigerung).

## Verzeichnisstruktur

```
vollstreckungsmappe-mueller-sparkasse-niederrhein/
- 00_aktenuebersicht.md
- 01_grundschuld_mueller/
- 02_kontopfaendung_kuechen-mueller-gmbh/
- 03_kryptowallets_mueller/
- originale/ (gescannte Schriftstuecke - in dieser Testakte nur als Text beschrieben)
- README.md
```

## Hinweis

Diese Testakte ist eine **fiktive** Schulungsakte. Sie ist erkennbar nicht zur Verwendung in einem realen Mandat geeignet. IBANs, BICs, Aktenzeichen und Wallet-Adressen sind Beispielwerte. Die wirtschaftliche und rechtliche Analyse folgt der zum Stand 25.5.2026 geltenden Rechtslage einschliesslich des ZVollstrDigitG (BT-Drs. 21/4815) und der Pfaendungsfreigrenzenbekanntmachung 1.7.2025.
