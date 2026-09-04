# Rentenrecht: Hinterbliebenenrente, KVdR und Pflegezeiten in Bremen

Akte einer Witwe mit Witwenrentenbescheid, eigener kleiner Rente, Unterstützungskasse, Einkommensanrechnung, Krankenversicherung der Rentner und ungeklärten Pflegezeiten des verstorbenen Ehemanns.

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen_gesamt.pdf`](gesamt-pdf/rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zum Plugin `rentenpruefer`.

## Kurzbild

Helga Bruns, 68, ist seit dem 21.04.2026 verwitwet. Die DRV Oldenburg-Bremen bewilligt eine große Witwenrente, rechnet ab August 2026 aber ein Nettoeinkommen von 1.236,20 EUR an, das sich aus den vorliegenden Unterlagen nicht ergibt. Parallel verbeitragt die Weser Krankenkasse die Unterstützungskassenleistung als Versorgungsbezug und kündigt eine Nachberechnung ab Mai 2023 an. Die Pflegekasse hat für die zweijährige häusliche Pflege des Ehemanns nur lückenhaft Rentenbeiträge gezahlt — und zwar in das Konto der Mandantin, die fest davon ausgeht, die Pflege müsse die Rente ihres Mannes erhöht haben.

Die Akte verlangt die saubere Trennung von Sterbevierteljahr und Einkommensanrechnung, die beitragsrechtliche Einordnung dreier Zahlungsströme in der KVdR und die Aufklärung der Pflegebeitragslücken samt Zuordnungsfrage.

Neu hinzugekommen ist ein vierter Streitpunkt: Die Weser Krankenkasse stellt nach dem Tod des Ehemannes die KVdR-Pflichtmitgliedschaft der Mandantin selbst in Frage und droht mit dem Wechsel in die deutlich teurere freiwillige Versicherung. Sie zählt für die Vorversicherungszeit nur die gesetzlich belegten Monate und übergeht die Kindererziehung der drei Kinder Anke, Torben und Wiebke. Ob die Neun-Zehntel-Belegung erfüllt ist, entscheidet sich rechnerisch an dieser Anrechnung.

## Aktenstruktur

```
rentenrecht-hinterbliebene-kvdr-pflegezeiten-bremen/
├── README.md                                  ← diese Datei
├── 02_drv_bescheid_witwenrente.docx             ← Bewilligungsbescheid mit Sterbevierteljahr, Anrechnung, Rechtsbehelfsbelehrung
├── 03_unterstuetzungskasse_leistungsmitteilung.docx ← Zahlstelle erklärt Beitragsabzug ab Juni 2026
├── 04_krankenkasse_beitragsmitteilung.docx      ← KVdR-Einordnung, Beitragssätze, angekündigte Nachberechnung
├── 05_pflegekasse_bescheinigung.docx            ← Pflegegrad, gemeldete Pflegeperson, lückenhafte Beitragszeiträume
├── 06_pflegedienst_leistungsnachweis.docx       ← Dokumentationsauszug zum Pflegeumfang der Ehefrau
├── 07_versicherungsverlauf_auszug_mandantin.docx ← Kontoauszug DRV mit Pflegebeiträgen und Speicherlücke
├── 08_widerspruch_kanzlei.docx                  ← fristwahrender Widerspruch mit Auskunftsanträgen
├── 09_drv_eingangsbestaetigung.docx             ← Eingangsbestätigung, Begründungsfrist, Fachreferats-Abgabe
├── 10_kontoauszug_zahlungseingaenge.txt         ← Zahlungseingänge Juni 2026 mit Notiz der Mandantin
├── 11_email_nachfragen_tochter.eml              ← Fragen der Tochter, Zeugin für den Erhebungsbogen 2023
├── 12_kvdr_vorversicherung_datenkern.csv        ← Datenkern: Rahmenfrist, Belegungszeiten, Kindererziehung; Neun-Zehntel-Belegung nachrechenbar
├── 13_anwaltliche_stellungnahme_kvdr_2026-07-03.docx ← Stellungnahme an die Krankenkasse: Kindererziehung führt über die Schwelle
├── 14_drv_bescheinigung_kindererziehungszeiten_2026-06-29.docx ← DRV-Bescheinigung der drei Kindererziehungszeiten
├── 15_telefonvermerk_drv_widerspruch_2026-07-10.docx ← Telefonat mit dem Fachreferat: Anlage zur Anrechnung folgt, Verläufe getrennt, Zahlung läuft weiter
├── rubric.yaml                                  ← Prüfkriterien für die Bearbeitung
├── eml/
    ├── 01_weser_kk_kvdr_ueberpruefung.eml       ← Krankenkasse: Vorversicherungszeit angeblich nicht erfüllt (172 von 252)
    ├── 02_kanzlei_an_weser_kk_kindererziehung.eml ← Kanzlei: drei Kinder mal drei Jahre erfüllen die Schwelle
    ├── 03_pflegekasse_erhebungsbogen.eml        ← Pflegekasse zur Beitragslücke 07/2023 bis 11/2023 und zur Zeugin
    ├── 04_weser_kk_geburtsurkunden_nachforderung.eml ← Krankenkasse fordert Geburtsurkunden nach und verlangt Nachweis der PKV-Zeit 2004 bis 2012
    └── chatverlauf_geschwister_bruns.txt        ← WhatsApp-Export der drei Kinder zur Suche der Geburtsurkunden
```

Der Datenkern in `12_kvdr_vorversicherung_datenkern.csv` macht den KVdR-Streit rechnerisch nachvollziehbar: Zweite Rahmenfristhälfte 280 Monate, Schwelle 252 Monate, belegt 172 Monate, Kindererziehung 108 Monate, zusammen 280 Monate. Die Krankenkasse kommt nur deshalb auf ein Fehlen der Vorversicherungszeit, weil sie die 108 Monate Kindererziehung nicht mitzählt.

## Bearbeitungsziel

Die Akte soll eine Rentenberatung zwingen, den Anrechnungsbetrag nicht hinzunehmen, sondern die Herkunft des angesetzten Nettoeinkommens aufzuklären, die Verbeitragung der drei Zahlungsströme einzeln zu prüfen (einschließlich Freibetragsfragen beim Versorgungsbezug) und die Pflegebeitragslücken Juli bis November 2023 sowie das Beitragsende März 2024 rechtlich einzuordnen, ohne die Erwartung der Mandantin ungeprüft zu übernehmen.
