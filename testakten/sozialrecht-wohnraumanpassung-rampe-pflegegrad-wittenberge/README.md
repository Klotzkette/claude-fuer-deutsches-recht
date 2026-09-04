# Sozialrecht: Wohnraumanpassung und Rampe in Wittenberge

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge_gesamt.pdf`](gesamt-pdf/sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

Arbeitsakte zu den Plugins `fachanwalt-sozialrecht`, `selbstvertreter-sozialgericht` und `richter-sozialgericht`.

## Kurzbild

Irmgard Pahl, 84, Pflegegrad 3, lebt in einem Reihenhaus in Wittenberge. Sie geht mit Gehstock, kommt aber wegen drei Außenstufen und einer hohen Türschwelle nicht mehr sicher aus dem Haus; seit Januar 2026 gab es Stürze auf der Eingangstreppe. Die PrignitzCare Pflegekasse bewilligt nur 1.180 EUR für ein mobiles Schienensystem; die Tochter will die fest montierte, wintertaugliche Rampe mit Handlauf für 7.920 EUR durchsetzen. Streit besteht über Notwendigkeit, Wirtschaftlichkeit, bauliche Eignung, Zuschusshöhe und die mögliche Beteiligung des Sozialhilfeträgers.

## Aktenstruktur

```
sozialrecht-wohnraumanpassung-rampe-pflegegrad-wittenberge/
├── README.md                              <- diese Übersicht
├── rubric.yaml                            <- Prüfkriterien für die Bearbeitung
├── 01_erstgespraech_tochter.docx            <- Erstberatung, Wohnsituation, Frist, Ziel
├── 02a_pflegegradbescheid_2024-09-18.docx   <- Eigenständiger Pflegegradbescheid
├── 02b_md_pflegegutachten_2024-09-11.docx   <- Gesondertes MD-Gutachten mit Mobilitätsmodul
├── 02c_hausaerztliche_stellungnahme_rampe_2026-06-15.docx <- Eigenständige ärztliche Stellungnahme
├── 03_bauangebot_rampe.docx                 <- Angebot der Fachfirma mit Maßen und Alternativen
├── 04a_pflegekassenbescheid_rampe_2026-06-24.docx <- Eigenständiger Teilbewilligungsbescheid
├── 04b_telefonnotiz_tochter_pflegekasse_2026-06-28.docx <- Gesonderte Telefonnotiz der Tochter
├── 05a_widerspruch_feste_rampe_2026-07-06.docx <- Eigenständiger anwaltlicher Widerspruch
├── 05b_pruefvermerk_ergaenzende_kostentraeger.docx <- Getrennter Prüfvermerk zu weiteren Kostenträgern
├── 06_wohnumfeld_fotos_beschreibung.docx    <- Eingang, Maße, Fotobeschreibungen, Winterrisiko
├── 07_kosten_traeger_matrix.csv           <- Datenkern: Kostenpositionen, Höchstzuschuss, Eigenanteil, Finanzierungslücke
├── 08a_kanzleivermerk_eilbeduerftigkeit_rampe.docx <- Getrennter Eilbedürftigkeits- und Belegvermerk
├── 08b_anregung_ortstermin_pflegekasse.docx <- Eigenständiges Schreiben zur Anregung eines Ortstermins
├── 09_bauamt_ortstermin_und_skizzenmass.docx <- Protokoll des Ortstermins mit dem Bauamt
├── 10_email_nachbarin_zugang.eml          <- Nachbarin zu Stürzen, Winter und Rampenakzeptanz
├── 11_pflegetagebuch_sturzliste.txt       <- Sturzliste und Pflegetagebuch der Tochter
├── 12_sozialamt_prignitz_zwischennachricht.docx <- Sozialamt zu Nachrang, Höchstzuschuss und Nachweisen
├── 13_einkommen_vermoegen_nachweisliste.csv <- Von der Tochter zusammengestellte Einkommens- und Vermögensliste für das Sozialamt
├── eml/
│   ├── 01_pflegekasse_eingang_widerspruch.eml <- Pflegekasse bestätigt Widerspruch, nennt Höchstbetrag 4000 EUR
│   ├── 02_teschner_angebotsklarstellung.eml    <- Fachfirma schlüsselt die 7920 EUR auf, mobile nicht selbst nutzbar
│   ├── 03_md_stellungnahme_selbstnutzbarkeit.eml <- Medizinischer Dienst zur Selbstnutzbarkeit der mobilen Rampe
│   └── 04_pflegekasse_terminvorschlag_ortstermin.eml <- Pflegekasse schlägt Ortstermin am 22.07.2026 vor und stellt das Widerspruchsverfahren zurück
└── gesamt-pdf/                            <- konsolidierte Lesefassung als PDF
```

## Bearbeitungsziel

Die Akte eignet sich für Pflegekassenverfahren und Sozialgerichtsarbeit: Pflegegrad, wohnumfeldverbessernde Maßnahme, Erleichterung der häuslichen Pflege, selbstständige Lebensführung, Zumutbarkeit mobiler Alternativen, Zuschussgrenze, Mehrkostenträger und Eilbedürftigkeit müssen konkret abgearbeitet werden. Die Angaben zur Zahl der Stürze sind in den Unterlagen nicht völlig deckungsgleich; das gehört zur Beweiswürdigung.
