# Akte: Vollstreckungsmappe Sparkasse Niederrhein gegen Mueller


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Diese Arbeitsakte gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 68 KB) | PDF | [`gesamt-pdf/vollstreckungsmappe-mueller-sparkasse-niederrhein_gesamt.pdf`](gesamt-pdf/vollstreckungsmappe-mueller-sparkasse-niederrhein_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein` (Akte) | [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.


## Mandantenkonstellation

- **Gläubigerin:** Sparkasse Niederrhein AOeR, Krefeld, vertreten durch Rechtsanwältin Dr. Henrike Boehringer, Krefeld (Mandantin des Plugins).
- **Schuldner 1:** Bernd Mueller, geb. 14.3.1968, Eigentümer des Einfamilienhauses Beethovenstrasse 12, 47800 Krefeld. Haupt-Sicherungsgeber, vertritt zugleich die Mueller Küchen GmbH.
- **Schuldnerin 2 (Mitschuldnerin):** Dorothea Mueller, geb. 7.9.1971, Ehefrau, Miteigentümerin Beethovenstrasse 12.
- **Schuldnerin 3 (Drittschuldnerin gegen Kundin Mueller):** Mueller Küchen GmbH, AG Krefeld HRB 14 432, Geschäftsführer Bernd Mueller. Hier nicht Schuldnerin der Sparkasse, sondern Drittschuldnerin in einer separaten Mietzinspfändung.

## Drei Vorgänge in einer Mappe

### 01 - Vollstreckung aus notarieller Grundschuld

Dingliche Vollstreckung in das selbstgenutzte Einfamilienhaus Beethovenstrasse 12. Sicherungsgrundschuld 380.000 EUR aus 2017, Notar Dr. Berghoff, URNr 882/2017. Forderung valutiert per 31.3.2026 mit 261.480,73 EUR offen aus Privatdarlehen 4717-8821 zur Sanierung. Bernd und Dorothea Mueller sind drei Monate im Rückstand, Kündigung mit Schreiben vom 5.4.2026 erklärt, Kündigung der Grundschuld nach Paragraf 1193 BGB am 12.4.2026.

Skills: `zv-notarielle-urkunde-grundschuld`, `zv-zvg-antrag-glaeubiger`, ggf. `zv-pfueb-bank` (persönliche Vollstreckung parallel).

### 02 - Einfache Kontopfändung

Aus demselben Privatdarlehen (Restforderung 261.480,73 EUR) wird parallel der Lohnzufluss des Schuldners gepfändet. Bernd Mueller bezieht Geschaeftsfuehrervergehalt der Mueller Küchen GmbH (Drittschuldner) über das Geschäftskonto bei der Postbank, IBAN DE89 1001 0010 0987 6543 21. Dorothea Mueller führt ihr Privatkonto bei der DKB, IBAN DE12 1203 0000 5511 2233 00. Beide Konten werden gepfändet, P-Konto-Schutz wird voraussichtlich beantragt.

Skills: `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`, `zv-pfaendungstabelle-2025`, `zv-elektronische-zustellung-2027`.

### 03 - Verpfändung Bitcoin- und Stablecoin-Wallets

Bei der Vermögensauskunft am 22.4.2026 hat Bernd Mueller offengelegt, dass er über zwei Wallets verfügt:

- **Wallet A (self-hosted):** Hardware-Wallet Ledger Nano X mit Seed-Phrase und Software-Wallet auf seinem MacBook. Bestand laut Selbstauskunft 0,42 BTC und 11.500 USDT zum Stichtag.
- **Wallet B (custodial):** Konto bei der Bitpanda GmbH (Wien) als Krypto-Verwahrstelle nach Paragraf 1 Abs. 1a Satz 2 Nr. 6 KWG, Bestand 0,18 BTC, 4.300 USDC und 22.000 EUR Fiat-Guthaben.

Beide Vermögensgegenstände werden vollstreckt - mit unterschiedlichen Mechaniken, die diese Akte gegenüberstellt.

Skills: `zv-mobiliar-gv-auftrag` (self-hosted), `zv-pfueb-mieter-finanzamt` (custodial Drittschuldner), `zv-vermoegensauskunft-gv`, `zv-abwehr-schuldner` (Schuldnerseite Selbstbelastungsverweigerung).

## Verzeichnisstruktur

```
vollstreckungsmappe-mueller-sparkasse-niederrhein/
- 00_aktenuebersicht.md
- 01_grundschuld_mueller/
- 02_kontopfaendung_kuechen-mueller-gmbh/
- 03_kryptowallets_mueller/
- originale/ (gescannte Schriftstuecke - in dieser Akte nur als Text beschrieben)
- README.md
```

## Hinweis

IBANs, BICs, Aktenzeichen und Wallet-Adressen sind anonymisierte Beispielwerte für die Aktenarbeit. Die wirtschaftliche und rechtliche Analyse folgt der zum Stand 25.5.2026 geltenden Rechtslage einschliesslich des ZVollstrDigitG (BT-Drs. 21/4815) und der Pfaendungsfreigrenzenbekanntmachung 1.7.2025.
