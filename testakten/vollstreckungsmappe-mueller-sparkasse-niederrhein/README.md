# Akte: Vollstreckungsmappe Sparkasse Niederrhein gegen Müller

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/vollstreckungsmappe-mueller-sparkasse-niederrhein_gesamt.pdf`](gesamt-pdf/vollstreckungsmappe-mueller-sparkasse-niederrhein_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein` (Akte) | [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.

## Mandantenkonstellation

- **Gläubigerin:** Sparkasse Niederrhein AOeR, Krefeld, vertreten durch Rechtsanwältin Dr. Henrike Boehringer, Krefeld (Mandantin des Plugins).
- **Schuldner 1:** Bernd Müller, geb. 14.3.1968, Eigentümer des Einfamilienhauses Beethovenstrasse 12, 47800 Krefeld. Haupt-Sicherungsgeber, vertritt zugleich die Müller Küchen GmbH.
- **Schuldnerin 2 (Mitschuldnerin):** Dorothea Müller, geb. 7.9.1971, Ehefrau, Miteigentümerin Beethovenstrasse 12.
- **Schuldnerin 3 (Drittschuldnerin gegen Kundin Müller):** Müller Küchen GmbH, AG Krefeld HRB 14 432, Geschäftsführer Bernd Müller. Hier nicht Schuldnerin der Sparkasse, sondern Drittschuldnerin in einer separaten Mietzinspfändung.

## Drei Vorgänge in einer Mappe

### 01 - Vollstreckung aus notarieller Grundschuld

Dingliche Vollstreckung in das selbstgenutzte Einfamilienhaus Beethovenstrasse 12. Sicherungsgrundschuld 380.000 EUR aus 2017, Notar Dr. Berghoff, URNr 882/2017. Forderung valutiert per 31.3.2026 mit 261.480,73 EUR offen aus Privatdarlehen 4717-8821 zur Sanierung. Bernd und Dorothea Müller sind drei Monate im Rückstand, Kündigung mit Schreiben vom 5.4.2026 erklärt, Kündigung der Grundschuld nach Paragraf 1193 BGB am 12.4.2026.

Skills: `notarielle-urkunde-grundschuld`, `zvg-antrag-glaeubiger`, gegebenenfalls `pfueb-bank` für die parallele persönliche Vollstreckung.

### 02 - Einfache Kontopfändung

Aus demselben Privatdarlehen (Restforderung 261.480,73 EUR) wird parallel der Lohnzufluss des Schuldners gepfändet. Bernd Müller bezieht Geschäftsführervergehalt der Müller Küchen GmbH (Drittschuldner) über das Geschäftskonto bei der Postbank, IBAN DE89 1001 0010 0987 6543 21. Dorothea Müller führt ihr Privatkonto bei der DKB, IBAN DE12 1203 0000 5511 2233 00. Beide Konten werden gepfändet, P-Konto-Schutz wird voraussichtlich beantragt.

Skills: `pfueb-bank`, `pfueb-arbeitsentgelt`, `pfaendungstabelle-pfueb-arbeitsentgelt`, `elektronische-zustellung-eu`.

### 03 - Verpfändung Bitcoin- und Stablecoin-Wallets

Bei der Vermögensauskunft am 22.4.2026 hat Bernd Müller offengelegt, dass er über zwei Wallets verfügt:

- **Wallet A (self-hosted):** Hardware-Wallet Ledger Nano X mit Seed-Phrase und Software-Wallet auf seinem MacBook. Bestand laut Selbstauskunft 0,42 BTC und 11.500 USDT zum Stichtag.
- **Wallet B (custodial):** Konto bei der Bitpanda GmbH (Wien) als Krypto-Verwahrstelle nach Paragraf 1 Abs. 1a Satz 2 Nr. 6 KWG, Bestand 0,18 BTC, 4.300 USDC und 22.000 EUR Fiat-Guthaben.

Beide Vermögensgegenstände werden vollstreckt - mit unterschiedlichen Mechaniken, die diese Akte gegenüberstellt.

Skills: `mobiliar-gv-auftrag` für die selbst verwahrte Wallet, `pfueb-802l-arbeit` für den verwahrenden Drittschuldner, `vermoegensauskunft-gv` sowie `abwehr-schuldner` für die Schuldnerseite und mögliche Auskunftsgrenzen.

## Verzeichnisstruktur

```
vollstreckungsmappe-mueller-sparkasse-niederrhein/
- 00_aktenuebersicht.md
- 01_grundschuld_mueller/
- 02_kontopfaendung_kuechen-mueller-gmbh/
  - 04_drittschuldnererklaerung_postbank.md (Erklärung der Postbank nach Paragraf 840 ZPO mit P-Konto-Angaben und Handvermerk)
- 03_kryptowallets_mueller/
  - 05_gv_protokoll_ledger_termin_12_06_2026.md (Abschrift des GV-Protokolls zum Pfändungsversuch: Ledger verwahrt, PIN verweigert, Seed-Kapsel angeblich beim Bruder)
- 04_email_lemm_an_boehringer_ratenangebot.eml (Sparkassen-Mail zu Ratenangebot Müller, Anruf der Ehefrau und Stand der Drittschuldnererklärungen)
- originale/ (gescannte Schriftstuecke - in dieser Akte nur als Text beschrieben)
- README.md
```

## Hinweis

IBANs, BICs, Aktenzeichen und Wallet-Adressen sind anonymisierte Beispielwerte für die Aktenarbeit. Die wirtschaftliche und rechtliche Analyse folgt der zum Stand 25.5.2026 geltenden Rechtslage einschliesslich des ZVollstrDigitG (BT-Drs. 21/4815) und der Pfändungsfreigrenzenbekanntmachung 1.7.2025.
