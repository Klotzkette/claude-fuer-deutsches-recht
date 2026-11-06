# Prüfbestand der E-Rechnung-Werkstatt

Dieser Bestand dokumentiert die tatsächlich ausgeführte lokale Rechnungserzeugung. Der Fall ist vollständig fiktiv. Das [Eingabebeispiel](../../e-rechnung-werkstatt/beispiele/rechnungsdaten.json) enthält den bestätigten Datenstand und die feldbezogenen Fundstellen in der [Quelle](../../e-rechnung-werkstatt/beispiele/rechnungsquelle.txt).

## 1 Ausgeführte Prüfung

Am 6. November 2026 wurden beide Formate mit Python, pypdf 6.10.0, Temurin 17.0.21, Mustangproject 2.26.0 und dem amtlichen KoSIT-Validator 1.6.3 samt Konfiguration vom 31. August 2026 tatsächlich erzeugt und geprüft. Die endgültige Ausgabe liegt unverändert unter `ausgabe/`; ihr [Generatorbericht](ausgabe/Pruefbericht.json) bindet Eingabe, Generator, Layout, Laufzeitdefinition und Ausgabedateien an ihre tatsächlichen SHA-256-Werte.

Die XRechnung wurde mit XML-Schema und Schematron akzeptiert. Die ZUGFeRD-Datei verwendet Factur-X 1.09.2 im Profil EN 16931 und wurde als PDF/A-3u geprüft; das eingebettete XML ist bytegleich mit dem separat geprüften XML. Der nicht einschlägige Mustang-Hinweis BR-DE-21 zur abweichenden XRechnung-Profilkennung bleibt im Originalbericht erkennbar. Ein solches EN-16931-Profil wird hier nicht als XRechnung ausgegeben.

Die abschließende Hybriddatei wurde gerendert und visuell geprüft. Die Beispielrechnung hat eine Seite mit lesbarem Briefkopf, Empfängeranschrift, Positionstabelle, getrennten Steuergruppen und Zahlungsdaten. Es waren keine Überlagerungen, abgeschnittenen Texte oder Rendererwarnungen sichtbar beziehungsweise protokolliert.

## 2 Regressionen und Gegenproben

Das [unveränderte Testprotokoll](regressionen.log) dokumentiert zehn bestandene Tests. Die echten Prüfwerkzeuge verwerfen einen manipulierten XML-Zahlbetrag und manipulierte PDF/A-Metadaten. Weitere Gegenproben betreffen doppelte JSON-Schlüssel, falsche Summen, nicht unterstützte Steuer- und Abrechnungsfelder, fehlende Quellenzuordnung, veränderte Quellenhashes, die Änderung des Eingabestands während der Erzeugung, vorhandene Ausgabeziele, Rendererwarnungen sowie Preispräzision und numerische Steuergruppierung.

Die endgültige Einrichtung wurde zusätzlich in einem neuen Ordner mit tatsächlichen Downloads geprüft. Das amtliche KoSIT-Bundle, die inneren Archive und alle 98 installierten Dateien stimmen mit dem gepinnten Bestand überein. Die großen Fremdwerkzeuge werden nicht im Plugin ausgeliefert.

## 3 Aussagegrenzen

Dies sind technische Ausführungsnachweise und redaktionelle Prüfungen. Sie belegen keine automatische Auswahl des Plugins in einem fremden Client, keine allgemeine Qualität der Extraktion aus beliebigen Dateien und keine tatsächliche Annahme durch ein Empfängerportal. Es wurde keine Rechnung versandt. Steuerliche Tatsachen sind vom jeweiligen Bearbeiter anhand der Quellen zu prüfen. Das [Qualitätsprofil](../evals/e-rechnung-werkstatt.json) enthält getrennte synthetische Bewertungsaufgaben.
