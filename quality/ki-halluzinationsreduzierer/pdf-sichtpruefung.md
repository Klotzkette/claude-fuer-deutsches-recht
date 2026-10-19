# PDF-Sichtprüfung KI-Halluzinationsreduzierer

## 1. Prüfgegenstand und Methode

Am 18.10.2026 wurden sämtliche 16 Seiten der drei erzeugten Prompt-Lesefassungen aus `/tmp/halluzination-release-1.0.0` mit Poppler `pdftoppm` bei 100 dpi als PNG gerendert und tatsächlich visuell angesehen. Acht Kontaktbögen mit jeweils zwei vollständigen Seiten zeigten jede Seite einschließlich Seitenrändern, Überschriften, Tabellen und Fußzeile. Die Prüfbilder liegen außerhalb des Repositorys unter `/tmp/halluzination-pdf-sichtpruefung`.

Die Sichtprüfung umfasste die Werkstatt auf den Seiten 1 bis 11, den Mini-Prompt auf den Seiten 1 bis 3 und den Hauptproblem-Prompt auf den Seiten 1 und 2. Zusätzlich wurden Seitenzahl, SHA-256 und eingebettete Schriftbezeichnungen unmittelbar aus den geprüften PDF-Dateien ermittelt. Diese Runde hat keine PDF-Datei verändert oder neu gebaut.

## 2. Tatsächlich gesehene Ergebnisse

| Lesefassung | Gesehene Seiten | Sichtbefund |
| --- | --- | --- |
| Werkstatt-Prompt | 1 bis 11 | Titel, 27 dezimale Kapitel, Fließtext, Tabelle auf Seite 9 und Seitenzahlen vollständig sichtbar. Keine abgeschnittenen Zeilen, überdeckten Texte, unlesbaren Glyphen oder über den Seitenrand laufenden Inhalte festgestellt. |
| Mini-Prompt | 1 bis 3 | Titel, sechs Hauptabschnitte und fünf untergeordnete Prüfblöcke lesbar; Überschriften stehen mit nachfolgendem Text. Fußzeilen und Seitenzahlen sichtbar und getrennt vom Haupttext. |
| Hauptproblem-Prompt | 1 bis 2 | Der zweizeilige Titel ist vollständig sichtbar; Hierarchie, Absätze und Seitenübergang sind lesbar. Keine Überlagerung oder abgeschnittene Unterzeile festgestellt. |

Die vier Spalten der Werkstatt-Tabelle auf Seite 9 sind voneinander abgegrenzt. Kopfzeile und beide Datenzeilen sind vollständig lesbar; die Tabelle steht innerhalb der Satzbreite. Ihr Einleitungssatz steht am Ende der vorangehenden Seite. Der Seitenwechsel verdeckt keine Tabelleninformation.

Die Schlussseiten sind unterschiedlich gefüllt: Die Werkstatt endet auf Seite 11 mit zwei Absätzen, der Mini-Prompt auf Seite 3 mit seinem abschließenden Format- und Ausführungshinweis. Diese kurzen Schlussseiten enthalten vollständigen Text; der größere Weißraum ist sichtbar und wird nicht als fehlender Inhalt behandelt. Die Prüfung ergab keinen erforderlichen Layoutreparaturschritt.

## 3. Schrift und Fußzeilen

Alle drei PDFs enthalten die eingebetteten Schriften `TimesNewRomanPSMT` und `TimesNewRomanPS-BoldMT`. Die aus den Textobjekten gelesenen Schriftgrößen sind 11 pt für den Fließtext, 14 und 18 pt für abgestufte Überschriften sowie 7.5 pt für die Fußzeilen. Ein Ersatzfont wurde bei diesen lokal geprüften Fassungen nicht verwendet.

Die Fußzeile benennt auf allen gesehenen Seiten die Komponente, Version 1.0.0 und Times New Roman 11 pt. Die jeweils rechts stehende Seitenzahl ist erkennbar. Zwischen Fußzeile und Haupttext besteht ein sichtbarer Abstand; Überschneidungen wurden nicht festgestellt.

## 4. Identität der geprüften PDF-Dateien

| Datei | Seiten | SHA-256 |
| --- | --- | --- |
| `ki-halluzinationsreduzierer-werkstatt.pdf` | 11 | `db62461805ed2a92113f432ab29923abd300ae8677164d23eea4f280ceefe3ad` |
| `ki-halluzinationsreduzierer-schnellstart.pdf` | 3 | `a1ced8edaa12921a21d8b9d0e405e7bb4a5f765953a3ee64e5486d8710bed5f3` |
| `ki-halluzinationsreduzierer-hauptproblem.pdf` | 2 | `ff80e8aeeb1fcbe862ef184b6df01dcf64e7db72080b823127b3603facaaa1e4` |

## 5. Reichweite des Befunds

Die Sichtprüfung ergänzt den automatischen Abgleich von Wortbestand, Quellenbytes, Glyphen und Seitenbegrenzungen. Sie bestätigt das tatsächlich gesehene Layout der oben durch Prüfsummen bezeichneten Dateien. Sie ist keine zusätzliche rechtliche Quellenverifikation und keine Aussage über abweichend gerenderte spätere Fassungen. Ein erneuter Build mit Liberation Serif benötigt eine eigene Sichtprüfung, soweit die erzeugten PDFs ausgeliefert werden sollen.

## 6. Nachtrag zur Komponentenfassung 1.1.0 vom 19.10.2026

Die drei finalen Lesefassungen enthalten 23 Seiten: Werkstatt 17, Mini drei und Hauptproblem drei. Alle Seiten wurden als PNG gerendert und tatsächlich visuell geprüft. Nach der letzten Änderung wurden die betroffenen Werkstattseiten 11 bis 17 nochmals in Originalauflösung angesehen; die vorhergehenden Seiten und beiden kompakten PDFs blieben unverändert. Die Sichtprüfung erfolgte arbeitsteilig mit redaktioneller Gegenkontrolle. Sie ist eine Modellprüfung, keine menschliche Einreichungsfreigabe.

Der erste Textabgleich beanstandete die engen Normen-URLs in einer Tabelle. Der Block wurde in Absätze überführt. Bei der Sichtprüfung gefundene nicht interpretierte Unterüberschriften wurden als unterstützte Markdown-Überschriften mit gleichbleibender dezimaler Nummerierung gesetzt. Die abschließende Sichtprüfung zeigt keine Markdownreste, abgeschnittenen Zeilen, überlagerten Texte oder fehlenden Glyphen. Die Tabelle in Abschnitt 28.3 steht vollständig auf Seite 15; der davor verbleibende Weißraum enthält keinen ausgelassenen Text. Der Schlussabsatz setzt sich vollständig und lesbar auf Seite 17 fort.

Alle drei Fassungen verwenden eingebettete Times-New-Roman-Schriften mit 11 pt Grundschrift. Der automatische Wortbestandsabgleich meldet null fehlende Wörter; Glyphen- und Seitenbegrenzungsprüfungen sind bestanden. Die Werkstatt enthält 30 Kapitel. Die Titel, dezimalen Unterüberschriften, Fettpräfixe, Fußzeilen und Seitenzahlen sind lesbar. Die endgültigen Dateien liegen außerhalb des Repositorys im Ausgabeordner und werden mit identischen Bytes veröffentlicht.

| Datei | Seiten | SHA-256 |
| --- | --- | --- |
| `ki-halluzinationsreduzierer-werkstatt.pdf` | 17 | `7f1d51234261aeb904935f472d632a48376374edc306a058975da325d7840e4d` |
| `ki-halluzinationsreduzierer-schnellstart.pdf` | 3 | `6e944421e3042ca9d5121a1ecd968bd2ad4e58e57f28157702d36488f48ecc67` |
| `ki-halluzinationsreduzierer-hauptproblem.pdf` | 3 | `8661ba2a62f7a982840d0ddcb38d1c1fd555411d2c13103c116c3df26b1015fe` |

Dieser Nachtrag gilt nur für die genannten Prüfsummen. Ein abweichender Build erfordert eine neue Sichtprüfung der veränderten Seiten. Die Paketidentität und die juristische Quellenprüfung sind eigenständige Nachweise.
