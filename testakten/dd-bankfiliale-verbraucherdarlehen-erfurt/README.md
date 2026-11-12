# Due Diligence einer Erfurter Bankfiliale

[Alle Testakten](../README.md) · [Hauptübersicht](../../README.md) · [Download-Index](../../ASSET_INDEX.md)

Die Akte begleitet den beabsichtigten Erwerb von 1.000 Verbraucherdarlehensforderungen einer fiktiven englischen Bank. Sie eignet sich für Käuferprüfung, Verkäuferaufbereitung, Kaufpreisabgleich und die Bearbeitung des Forderungskaufvertrags. Ausgangspunkt ist ein Forderungskauf mit gesonderter Serviceüberleitung; Einlagen, vollständige Kundenverträge und Betriebsteile sind keine stillschweigend mitverkauften Gegenstände.

## 1 Benutzung

Beginnen Sie mit `00_Auftrag_Due_Diligence.docx`, der Arbeitsmappe und dem Verkäuferentwurf. Bearbeitungsdatum ist der 10.10.2026, wirtschaftlicher Stichtag der 30.09.2026. Prüfen Sie aus Käufer- oder Verkäufersicht und verlangen Sie einen belegten Befund mit nächstem Arbeitsschritt. Eine fertige DD-Musterlösung ist nicht enthalten.

Die 20 Detailfälle wurden bewusst problemorientiert ausgewählt. Sie bilden keine repräsentative Stichprobe der 1.000 Forderungen. Für weitere 980 Nummern existieren nur knappe Verkäuferdaten; deren Einzelakten müssen nachgefordert werden. Alle Zahlen und Personennamen sind erfunden. Anschriften sind fiktiv; E-Mail-Adressen verwenden die nicht zustellbare Domain `example.invalid`. Es werden keine echten Bankkennzeichen, Kontoverbindungen oder Registereintragungen behauptet.

## 2 Unterlagen

- 20 ausformulierte Verbraucherdarlehensverträge in Word.
- 20 PDF-Kontojournale mit je zwölf Monatsbuchungen und ausdrücklich bezeichneten Anfangssalden.
- 20 konkrete Briefe in PDF und 20 E-Mails; fünf enthalten das zugehörige Schreiben als echten PDF-Anhang.
- Prüfauftrag, Absichtserklärung und bearbeitbarer Forderungskaufvertrag in Word.
- Hauptbuchüberleitung, Urkundeninventar und sechs Transaktions-E-Mails.
- Interne Filialergebnisrechnung mit Buchwertüberleitung sowie konkrete Insolvenz- und Vollstreckungsbelege.
- Excel mit 1.000 Forderungen, 240 Detailbuchungen, Stichtagsbrücke, Preisannahmen und Erläuterung der Belege.

Die PDF-Briefe verwenden die PDF-Standardschrift Times. Word ist auf Times New Roman 11 pt eingestellt; der verfügbare PDF-Renderer ersetzt die nicht installierte Schrift durch Liberation Serif. Die technische Darstellung eines Buchungssaldos bestätigt weder Fälligkeit noch Durchsetzbarkeit. Kosten, Zinsen, Insolvenzereignisse und kundenseitige Einwendungen bleiben sichtbar. Verkäuferfaktoren sind ausdrücklich keine Erwerberbewertung.

## 3 Downloads

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Entpacken Sie das Akten-ZIP und laden Sie für den ersten Arbeitsauftrag nur den Ordner `Grundakte`. Dort stehen die ausgewählten Eingangsunterlagen und Belege. Falls ein Rechtsbehelf vorzubereiten ist, kann der zugrunde liegende Ausgangsbescheid dazugehören. Die weiteren Aktenstücke liegen außerhalb der Grundakte. Die vollständige Lesefassung ist separat abrufbar. Das Einzel-PDF-ZIP dient der Durchsicht der vollständigen Akte.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/dd-bankfiliale-verbraucherdarlehen-erfurt_gesamt.pdf`](gesamt-pdf/dd-bankfiliale-verbraucherdarlehen-erfurt_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-dd-bankfiliale-verbraucherdarlehen-erfurt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-dd-bankfiliale-verbraucherdarlehen-erfurt.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-dd-bankfiliale-verbraucherdarlehen-erfurt-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/due-diligence-v1.0.1/testakte-dd-bankfiliale-verbraucherdarlehen-erfurt-einzelpdfs.zip) |

Die ZIP-Links führen zu den veröffentlichten Aktenfassungen. Die Gesamt-PDF steht für die Nachbesprechung getrennt bereit.

English: Start with the `Grundakte` folder in the original-format ZIP. It contains the selected intake records. Later procedural documents are outside that folder. Choose the combined PDF for reading; it is deliberately excluded from the original-format ZIP. Choose the individual-PDF ZIP to review each document separately.

<!-- END gesamt-pdf-section (autogen) -->

## 4 Herkunft und Reproduktion

Die Unterlagen werden mit `scripts/build-dd-bankakte.py` und `scripts/build-dd-bankakte-excel.mjs` aus dem deterministischen Fallmodell reproduziert. Das Modell enthält Buchungsdaten, ausdrücklich getrennte Vorannahmen und die Bestandsüberleitung. Die Darstellung behauptet keine tatsächliche Banklizenz und ersetzt keine aufsichtsrechtliche Prüfung des Erwerbers oder Servicers.
