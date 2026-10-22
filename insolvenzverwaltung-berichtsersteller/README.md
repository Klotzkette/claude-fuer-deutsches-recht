# Insolvenzverwaltung Zwischen- und Schlussbericht-Ersteller

Dieses Plugin erstellt und aktualisiert gerichtstaugliche Zwischenberichte und Schlussberichte in deutschen Insolvenzverfahren. Es führt die Verfahrensakte, die fachlichen Berichtsmodule, Schlussrechnung, Schlussverzeichnis und Freigaben über gemeinsame Stichtage und Versionen zusammen. Zielgruppe sind Insolvenzverwalterinnen und Insolvenzverwalter, Sachbearbeitende, Rechtsanwältinnen und Rechtsanwälte sowie andere fachlich verantwortliche Personen in der Insolvenzverwaltung.

## 1. Benutzung

Übergeben Sie die vorhandene Verfahrensakte oder den für den Auftrag relevanten Ausschnitt und benennen Sie, soweit bekannt, Gericht, Aktenzeichen, Berichtsanlass, Berichtszeitraum, Stichtag und Abgabefrist. Das Plugin liest zuerst die Unterlagen, legt die Verfahrens- und Berichtskarte `BER-INT` an und erstellt anschließend das bestellte Produkt. Fehlende entscheidende Angaben werden gezielt erfragt; bereits bearbeitbare Teile werden nicht zurückgehalten.

Ein kurzer Startauftrag lautet beispielsweise:

> Erstellen Sie zum 30.09.2026 den turnusmäßigen Zwischenbericht. Lesen Sie zuerst den letzten Bericht, die neue Finanzbuchhaltung, die Kontoauszüge und die Verwertungskorrespondenz. Stellen Sie alle Veränderungen seit dem letzten Bericht dar und kennzeichnen Sie offene Belege.

Für einen vollständigen Abschlusslauf lautet der Auftrag beispielsweise:

> Prüfen Sie die Abschlussreife und erstellen Sie Schlussbericht, Schlussrechnung, Schlussverzeichnis und das gerichtliche Begleitschreiben als getrennte, aufeinander abgestimmte Produkte. Stoppen Sie die Quotenfreigabe bei jeder ungeklärten Kontendifferenz.

## 2. Arbeitslogik

Jedes Produkt erhält eine Kennung, einen Stichtag und eine Versionsnummer. Text, Zahlen und Anlagen müssen dieselbe führende Fassung verwenden. Der Hauptskill `berichtserstellung-steuern` zeigt offene Gates, Fragen, Fristen und die nächste Fachroute. Er unterscheidet Entwurf, fachliche Freigabe, Freigabe zur konkreten Außenhandlung sowie tatsächlichen Vollzug.

Eine natürliche Person muss jede gerichtliche Einreichung, rechtsverbindliche Erklärung, Zahlung und Hinterlegung freigeben. Das Plugin bereitet diese Handlungen vor, führt sie aber nicht allein aufgrund eines erzeugten Dokuments aus. Eine Schlussberichtsfassung ersetzt weder die Schlussrechnung noch das Schlussverzeichnis, einen Vergütungsbeschluss oder die gerichtliche Zustimmung zur Schlussverteilung.

## 3. Skills

| Skill | Aufgabe | Leitprodukt |
| --- | --- | --- |
| `akte-und-berichtsanlass-steuern` | Verfahren, Rolle, Zeitraum, Stichtag, Frist und Unterlagen bestimmen | `BER-INT` |
| `zwischenbericht-erstellen` | Entwicklungen seit dem letzten Bericht belegt und entscheidungsorientiert darstellen | `BER-ZW` |
| `schlussbericht-erstellen` | Verfahrensverlauf, Ergebnis, Restpunkte und Schlussvorschlag ausformulieren | `BER-SB` |
| `schlussrechnung-konten-abgleichen` | Bank, Kasse, Buchhaltung, Belege und Schlussrechnung abstimmen | `BER-SR` |
| `masse-verwertung-betrieb-darstellen` | Masse, Aussonderung, Verwertung, Betrieb, Verträge und Personal abbilden | `BER-MV` |
| `forderungen-sicherheiten-quote-darstellen` | Tabelle, Rang, Sicherheiten, Ausfall, Rückbehalte und Quote rechnen | `BER-FQ` |
| `steuern-kosten-verguetung-darstellen` | Steuern, Verfahrenskosten, Masseverbindlichkeiten und Vergütung abgrenzen | `BER-SKV` |
| `prozesse-anfechtung-haftung-darstellen` | Prozesse, Anfechtungs- und Haftungsansprüche samt Risiko und Erlösstatus führen | `BER-PAH` |
| `schlussverteilung-aufhebung-vorbereiten` | Zustimmung, Schlusstermin, Auszahlung, Hinterlegung und Aufhebung vorbereiten | `BER-SVA` |
| `nachtragsverteilung-bearbeiten` | spätere Massegegenstände rechtlich und rechnerisch bis zur Rechnungslegung bearbeiten | `BER-NV` |
| `berichtserstellung-steuern` | Gesamtworkflow, Gates, Fassungen und Übergaben steuern | `BER-CTRL` |

## 4. Prompts und Vorlagen

- [Werkstatt-Prompt](./insolvenzverwaltung-berichtsersteller-werkstatt.md): vollständiger Berichtslauf mit Fachmodulen, Kontrollen und Freigaben.
- [Schnellstart-Prompt (Mini-Prompt)](./insolvenzverwaltung-berichtsersteller-schnellstart.md): kompakter Arbeitsauftrag für ChatGPT, Codex oder Claude.
- [Arbeitsweise](./references/arbeitsweise.md): Tatsachenstatus, Fassungen, Rechenkontrolle und Außenwirkung.
- [Produkte, Gates und Übergaben](./references/produkte-gates-und-uebergaben.md): verbindliche Workflow-Schnittstellen.
- [Amtliche Quellen](./references/rechtsquellen.md): im Repository bereits volltextgeprüfte Norm- und Entscheidungsanker mit Aussagegrenzen.
- [Neutrale Arbeitsvorlagen](./assets/templates/README.md): leere, ausfüllbare Strukturen ohne Falldaten.

## 5. Testakten

Die Testakten dienen dazu, Zwischenbericht, Schlussbericht, Schlussrechnung, Schlussverzeichnis und Nachtragsfragen in einem vollständig fiktiven Aktenbestand zu erproben. Öffnen Sie zuerst die jeweilige Akten-README, bestimmen Sie einen Berichtsauftrag und lassen Sie das Plugin ausschließlich aus den dort vorhandenen Unterlagen arbeiten. Fehlende oder widersprüchliche Belege sind Teil der Übung und dürfen nicht durch erfundene Tatsachen ersetzt werden.

- [Testakte Nordlicht Handels GmbH, Kiel](../testakten/insolvenzverwaltung-nordlicht-handels-kiel/README.md)
- [Testakte Möbelwerk Havelberg, Regelverfahren](../testakten/insolvenzverwaltung-moebelwerk-havelberg-regelverfahren/README.md)
- [Testakte Mainbogen Laborsoftware GmbH, Würzburg](../testakten/insolvenzverwaltung-mainbogen-laborsoftware-wuerzburg/README.md): vier Zwischenberichte, Schlussbericht als Arbeits- und Referenzfassung, Schlussrechnung, Schlussverzeichnis, Quotenrechnung, neutrale Word-Vorlagen und eingebettete E-Mail-Anlagen.

Die konkreten Downloadlinks stehen bei den jeweiligen Testakten. Für jede Downloadgruppe gilt der dort unmittelbar wiedergegebene zweisprachige KI-Hinweis.

## 6. Fachliche Grenzen

Der Berichtsersteller arbeitet nur aus der konkreten Akte und verifizierten Quellen. Er erfindet keine Kontostände, Forderungsfeststellungen, Erlöse, gerichtlichen Entscheidungen oder Freigaben. Lokale Gerichtsformulare und gerichtliche Einzelverfügungen werden nur für das betroffene Verfahren verwendet. Das Plugin ersetzt nicht die fachliche Verantwortung der bestellten Insolvenzverwalterin oder des bestellten Insolvenzverwalters.

## 7. Version

Version 1.0.0. Änderungen werden im [Changelog](./CHANGELOG.md) dokumentiert.
