# 1. Qualitätsnachweis Schlussbericht, Schlussrechnung und Verteilung

Dieser Nachweis betrifft die Skills `insolvenzverwaltung/skills/verteilung-iv-vorlaeufige` und `insolvenzsachbearbeitung/skills/berichte-fristen-und-verteilung` sowie die beiden Arbeitsvorlagen für Schlussbericht, Schlussrechnung und Schlussverzeichnis. Der Bearbeitungsstand ist der 22.10.2026.

## 1.1. Fachlicher Ausbau

Beide Skills wurden von knappen oder teilweise generischen Abläufen zu durchgängigen Abschlussworkflows ausgebaut. Sie trennen nun Zwischenbericht, Schlussbericht, Schlussrechnung, Schlussverzeichnis, Quotenrechnung, Zahlungslauf, Vollzugsnachweis, Aufhebung und Nachtragsverteilung. Stichtage, führende Fassungen, Rollen und Freigaben sind je Produkt benannt. Eine ungeklärte Kontendifferenz, eine offene Masseposition oder eine unklare Forderungsbasis sperrt die davon abhängige Freigabe, ohne unabhängige Arbeiten anzuhalten.

Der Sachbearbeitungsskill verwendet stabile Produktkennungen von `BER-ZW` bis `BER-NV` und acht Qualitätsgates. Der Verwaltungsskill erzeugt ein internes Kontrollpaket, ein Gerichtspaket und ein getrenntes Verteilungs- oder Nachtragspaket. Beide Skills unterscheiden fachliche Prüfung, gerichtliche Entscheidung, menschliche Freigabe, technische Ausführung und belegten Vollzug.

## 1.2. Rechen- und Beleglogik

Die Schlussrechnung wird aus Einzelbuchungen, Kontoauszügen, Kasse, Hauptbuch und Belegen aufgebaut. Interne Umbuchungen werden neutralisiert. Ein Abschluss ist erst freigabefähig, wenn Bank- und Kassenbestand, Buchhaltung und Schlussrechnung centgenau übereinstimmen. Erwartete Steuererstattungen werden nicht als vorhandene Masse behandelt. Rückstellungen und Rückbehalte benötigen Betrag, Rechtsgrund, Auslöser, Verwahrweg und Beleg.

Die Forderungsbasis wird mit dem gerichtlichen Stand abgestimmt. Gesicherte Gläubiger nehmen nur nach Maßgabe des belegten Ausfalls an der Verteilung teil; eine volle Anmeldung wird nicht als Verzicht auf das Absonderungsrecht behandelt. Für bestrittene Forderungen werden Nachweis, Ausschlussfrist, Rückbehalt und Hinterlegung getrennt geprüft. Die neue Rechenprobe verarbeitet 250.000,00 Euro Geldbestand, 115.000,00 Euro konkret bezeichnete Abzüge, 700.000,00 Euro sichere Forderungsbasis und 100.000,00 Euro rechtzeitig nachgewiesene bestrittene Forderung. Sie führt reproduzierbar zu 135.000,00 Euro Teilungsmasse, 16,875 Prozent Quote, 118.125,00 Euro Auszahlung und 16.875,00 Euro Rückbehalt.

## 1.3. Amtliche Quellenprüfung

Die einschlägigen Vorschriften der Insolvenzordnung und Insolvenzrechtlichen Vergütungsverordnung wurden am 22.10.2026 in der amtlichen Fassung gelesen. Besonders geprüft wurden Paragraf 66, Paragrafen 187 bis 200, Paragrafen 203 bis 205 und Paragrafen 207 bis 211 InsO sowie Paragrafen 1, 6, 8 und 9 InsVV.

Die Skills verwenden amtlich gelesene Entscheidungen mit konkreten Randnummern und Aussagegrenzen. Dazu gehören BGH IX ZB 8/05 und IX ZB 143/11 zur konkreten Schlussverteilung, IX ZR 177/15 zur Ausfallteilnahme gesicherter Gläubiger, IX ZB 19/20 zur Abschlussreife und Vergütungsfälligkeit, IX ZB 35/21 zur gesonderten Abschlussroute nach Masseunzulänglichkeit, IX ZB 5/24, IX ZB 13/25 und IX ZB 45/25 zur Nachtragsverteilung sowie IX ZB 16/14 und IX ZB 36/25 zur eng begrenzten Rückstellung für Kosten der Wohlverhaltensperiode. Die vollständige Link- und Aussageübersicht steht in `insolvenzverwaltung/references/amtliche-quellen.md`.

## 1.4. Arbeitsvorlagen

Die frühere Kurzvorlage für Schlussbericht und Schlussrechnung wurde durch eine ausfüllbare Arbeitsstruktur mit fünfzehn Abschnitten ersetzt. Sie umfasst Verfahrensgang, Buchführung, Betrieb, Verwertung, Drittrechte, Prozesse, Steuern, Forderungstabelle, Kosten, Schlussrechnung, Quote, Nachtragspositionen, Anträge und Anlagenkontrolle. Die Schlussverzeichnisvorlage führt zusätzlich bestrittene, gesicherte, bedingte und nachträglich geänderte Positionen, Rückbehalte, Hinterlegungen, Summenprüfung und Vollzug.

## 1.5. Ausgeführte Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| `scripts/test-insolvenzsachbearbeitung.py` mit dem gebündelten Python | Sieben Tests ausgeführt, sechs bestanden und eine optionale Paketprüfung mangels übergebenem Releaseordner ausgelassen. |
| `scripts/validate-yaml-frontmatter.py` | Bestanden; keine Fehler oder Warnungen. |
| `scripts/audit-skill-activation.py` | Bestanden; beide Beschreibungen enthalten hinreichende Aktivierungssignale. |
| `scripts/validate-markdown-structure.py` | Bestanden. |
| Gezielte Validierung der beiden Qualitätsprofile samt redaktioneller und Workflow-Prüfung | Bestanden. |
| Relative Links in den beiden Skills | Sämtliche lokalen Ziele vorhanden. |
| `git diff --check` | Bestanden. |

Die technischen Prüfungen belegen Struktur und Reproduzierbarkeit. Die rechtliche Verantwortung für eine konkrete Einreichung, Zahlung, Hinterlegung oder Verfahrensbeendigung verbleibt bei der namentlich freigebenden Person.
