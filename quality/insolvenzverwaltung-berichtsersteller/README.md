# Qualitätsnachweis Insolvenzverwaltung Berichtsersteller

Stand: 22. Oktober 2026

## 1. Gegenstand

Geprüft wurden das Plugin `insolvenzverwaltung-berichtsersteller`, seine elf Skills, Werkstatt- und Schnellstart-Prompt, die drei Referenzdateien, acht neutralen Berichtsvorlagen sowie die Testakten Mainbogen Laborsoftware GmbH, Nordlicht Handels GmbH und Möbelwerk Havelberg GmbH.

Das Plugin trennt Zwischenbericht, Schlussbericht, Schlussrechnung, Schlussverzeichnis, Freigabe, Verteilungsvollzug und Nachtragsverteilung als eigene Produkte. Jeder Arbeitslauf führt Stichtag, Berichtszeitraum, führende Fassung, Belegstatus und offene Gates. Ein Entwurf oder eine fachliche Prüfung wird nicht als gerichtliche Einreichung, Zustimmung oder Zahlung ausgegeben.

## 2. Skill- und Promptprüfung

Das Paket enthält zehn Fachskills und den Hauptskill `berichtserstellung-steuern`. Alle Skills haben die sechs vorgesehenen Abschnitte, konkret benannte Eingaben und Produkte, nachvollziehbare Übergaben und eine Quellenbegrenzung mit `Trägt` und `Trägt nicht`. Die Skilltexte umfassen jeweils 1.547 bis 1.679 Wörter.

Werkstatt- und Schnellstartfassung verwenden dieselben Produktkennungen und Gates. Die Markdown- und TXT-Fassungen sind jeweils byteidentisch. Der Schnellstart bleibt unter 7.500 UTF-8-Bytes. Die Norm- und Entscheidungsanker stehen mit amtlichen Links und Aussagegrenzen in `references/rechtsquellen.md`.

## 3. Testakten und Rechenkontrolle

| Testakte | Schwerpunkt | Rechenstand |
| --- | --- | --- |
| Mainbogen Laborsoftware GmbH | vier Zwischenberichte, Arbeits- und Referenzfassung des Schlussberichts, neutrale Word-Vorlagen, E-Mail-Anlagen und Nachtragsfall | 425.430,00 EUR Verteilungsmasse; 1.685.971,56 EUR Forderungen; 25,2335 Prozent Quote |
| Nordlicht Handels GmbH | langer Berichtsverlauf bis Verteilungsvollzug und tatsächlichem späterem Steuerzins | 120.462,00 EUR Teilungsmasse; 509.842,00 EUR Forderungen; 23,627320 Prozent Quote |
| Möbelwerk Havelberg GmbH | Sicherheiten- und Freimassepfad, Abschlussgates und nur möglicher späterer Zufluss | 289.790,00 EUR Teilungsmasse; 862.900,00 EUR Forderungen; 33,583266 Prozent Quote |

Die Arbeitsmappen schließen rechnerisch ohne Differenz. Nordlicht und Havelberg wurden zusätzlich mit LibreOffice neu berechnet und unabhängig gegengeprüft. Der gesonderte Nachweis steht in `testakten-nordlicht-havelberg-2026-10-22.md`.

## 4. Dokument- und Sichtprüfung

Die Mainbogen-Akte enthält 37 Quelldokumente und ein 56-seitiges Gesamt-PDF. Sämtliche Seiten wurden als fünf Kontaktbögen gerendert und visuell kontrolliert. Überschriften, Tabellen und Kernwerte sind lesbar; Überlagerungen und abgeschnittene Inhalte wurden nicht festgestellt. DOCX-, XLSX-, CSV-, EML- und PDF-Dateien lassen sich mit den vorgesehenen Parsern öffnen. Die sechs E-Mails enthalten ihre angekündigten Anhänge tatsächlich als MIME-Anlagen.

Die aus der Nutzervorlage entnommene abstrakte Gliederungslogik wurde mit vollständig neuen Personen, Daten, Beträgen und Vorgängen umgesetzt. Der angehängte Altbericht ist weder Bestandteil des Repositorys noch eines Releasepakets. Eine zusätzliche Sperrwortprüfung kontrolliert, dass die bekannten Falldaten der Vorlage nicht in die neue Akte übernommen wurden.

## 5. Releaseprüfung

Der Komponentenbuilder erzeugt das installierbare Plugin, das portable Paket, beide Prompts als Markdown, TXT und PDF, je Testakte ein Originalformat-ZIP, ein Einzel-PDF-ZIP und das Gesamt-PDF sowie Prüfsummen und Quellenbericht. Der Paketselbsttest prüft Struktur, Hashes, ZIP-Inhalte, Warnhinweise, Dateilesbarkeit, Quellenanker und zentrale Rechenwerte.

