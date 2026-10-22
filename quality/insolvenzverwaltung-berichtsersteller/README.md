# Qualitätsnachweis Insolvenzverwaltung Berichtsersteller

Stand: 22. Oktober 2026

## 1. Gegenstand

Geprüft wurden das Plugin `insolvenzverwaltung-berichtsersteller`, seine elf Skills, Werkstatt- und Schnellstart-Prompt, die drei Referenzdateien, acht neutralen Berichtsvorlagen sowie die vier Testakten Klangbogen Buehnen- und Probenraumtechnik GmbH, Mainbogen Laborsoftware GmbH, Nordlicht Handels GmbH und Möbelwerk Havelberg GmbH.

Das Plugin trennt Zwischenbericht, Schlussbericht, Schlussrechnung, Schlussverzeichnis, Freigabe, Verteilungsvollzug und Nachtragsverteilung als eigene Produkte. Jeder Arbeitslauf führt Stichtag, Berichtszeitraum, führende Fassung, Belegstatus und offene Gates. Ein Entwurf oder eine fachliche Prüfung wird nicht als gerichtliche Einreichung, Zustimmung oder Zahlung ausgegeben.

## 2. Skill- und Promptprüfung

Das Paket enthält zehn Fachskills und den Hauptskill `berichtserstellung-steuern`. Alle Skills haben die sechs vorgesehenen Abschnitte, konkret benannte Eingaben und Produkte, nachvollziehbare Übergaben und eine Quellenbegrenzung mit `Trägt` und `Trägt nicht`. Die Skilltexte umfassen jeweils 1.547 bis 1.679 Wörter.

Werkstatt- und Schnellstartfassung verwenden dieselben Produktkennungen und Gates. Die Markdown- und TXT-Fassungen sind jeweils byteidentisch. Der Schnellstart bleibt unter 7.500 UTF-8-Bytes. Die Norm- und Entscheidungsanker stehen mit amtlichen Links und Aussagegrenzen in `references/rechtsquellen.md`.

## 3. Testakten und Rechenkontrolle

| Testakte | Schwerpunkt | Rechenstand |
| --- | --- | --- |
| Klangbogen Buehnen- und Probenraumtechnik GmbH | 22 turnusmäßige Zwischenberichte über 3.836 Tage, umfangreicher Nachweislauf und aus den fortgeschriebenen Berichten zu entwickelnder Schlussbericht | 419.000,07 EUR vorläufige Verteilungsmasse; 1.764.825,62 EUR festgestellte Forderungen; 23,741726 Prozent vorläufige Quote |
| Mainbogen Laborsoftware GmbH | vier Zwischenberichte, Arbeits- und Referenzfassung des Schlussberichts, neutrale Word-Vorlagen, E-Mail-Anlagen und Nachtragsfall | 425.430,00 EUR Verteilungsmasse; 1.685.971,56 EUR Forderungen; 25,2335 Prozent Quote |
| Nordlicht Handels GmbH | langer Berichtsverlauf bis Verteilungsvollzug und tatsächlichem späterem Steuerzins | 120.462,00 EUR Teilungsmasse; 509.842,00 EUR Forderungen; 23,627320 Prozent Quote |
| Möbelwerk Havelberg GmbH | Sicherheiten- und Freimassepfad, Abschlussgates und nur möglicher späterer Zufluss | 289.790,00 EUR Teilungsmasse; 862.900,00 EUR Forderungen; 33,583266 Prozent Quote |

Die Arbeitsmappen schließen rechnerisch ohne Differenz. Nordlicht und Havelberg wurden zusätzlich mit LibreOffice neu berechnet und unabhängig gegengeprüft. Der gesonderte Nachweis steht in `testakten-nordlicht-havelberg-2026-10-22.md`. Für Klangbogen hält `testakte-klangbogen-zwischenberichte-2026-10-22.md` die feste Berichtsfolge, das Dateiprofil und die Abnahmekriterien fest.

## 4. Dokument- und Sichtprüfung

Die Mainbogen-Akte enthält 37 Quelldokumente und ein 56-seitiges Gesamt-PDF. Sämtliche Seiten wurden als fünf Kontaktbögen gerendert und visuell kontrolliert. Überschriften, Tabellen und Kernwerte sind lesbar; Überlagerungen und abgeschnittene Inhalte wurden nicht festgestellt. DOCX-, XLSX-, CSV-, EML- und PDF-Dateien lassen sich mit den vorgesehenen Parsern öffnen. Die sechs E-Mails enthalten ihre angekündigten Anhänge tatsächlich als MIME-Anlagen.

Die Klangbogen-Akte ist ein vollständig fiktiver, eigenständiger Langzeitfall. Ihr Prüfprofil umfasst 22 einzelne Zwischenbericht-PDFs mit zusammen 233 Berichtsseiten, 15 Beleg-PDFs mit 30 Seiten, acht EML-Dateien mit tatsächlichen Anlagen, eine XLSX-Rechenmappe und drei TXT-Arbeitsnotizen. Die 37 Quell-PDFs werden zu einem 263-seitigen Gesamt-PDF zusammengeführt; einschließlich README, Rubrik und Gesamt-PDF enthält der Aktenordner 52 Dateien. Bericht 13 enthält den umfangreichen Nachweislauf; Bericht 22 endet bei der dokumentierten Schlussreife, ohne einen fertigen Schlussbericht vorwegzunehmen.

## 5. Releaseprüfung

Der Komponentenbuilder erzeugt das installierbare Plugin, das portable Paket, beide Prompts als Markdown, TXT und PDF, je Testakte ein Originalformat-ZIP, ein Einzel-PDF-ZIP und das Gesamt-PDF sowie Prüfsummen und Quellenbericht. Der Paketselbsttest prüft Struktur, Hashes, ZIP-Inhalte, Warnhinweise, Dateilesbarkeit, Quellenanker und zentrale Rechenwerte.
