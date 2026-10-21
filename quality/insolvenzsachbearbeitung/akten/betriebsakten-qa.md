# 1. Qualitätsbericht zu den drei Betriebsakten

## 1.1. Ergebnis und Umfang

Die drei Betriebsakten wurden am 21.10.2026 erstellt, aus den tatsächlichen Originaldateien paketiert und erneut paketiert. Alle nachstehenden Prüfungen sind ausgeführt. Der Prüfbericht behandelt ausschließlich diese drei Akten; die Verbraucherakte und das Komponentenrelease werden gesondert geprüft.

| Akte | Originale / PDF-Seiten | Formate | Echte MIME-Anlagen |
| --- | ---: | --- | ---: |
| Kaufhaus Katzenbogen, München | 41 / 41 | 24 PDF, 7 DOCX, 8 EML, 2 XLSX | 8 |
| Werkzeugkiste, Augsburg | 22 / 22 | 12 PDF, 5 DOCX, 4 EML, 1 XLSX | 7 |
| Café Abendrot, Regensburg | 24 / 24 | 11 PDF, 8 DOCX, 4 EML, 1 XLSX | 5 |

Insgesamt liegen 87 Originalunterlagen und 87 PDF-Seiten vor. Jede Unterlage erhält eine eigene PDF-Abbildung. Alle zwanzig E-Mail-Anlagen stimmen bytegenau mit den separat vorhandenen Originaldateien überein. Die EML-Dateien besitzen echte MIME-Strukturen, Absender, Adressat, Datum, Betreff und Message-ID.

## 1.2. Tatsächliche Sichtprüfung

Alle zwanzig DOCX-Dateien wurden mit dem Dokumentenrenderer des geladenen Skills in Seitenbilder gerendert und geöffnet. Alle vier XLSX-Dateien wurden mit `@oai/artifact-tool` erstellt, berechnet, als Arbeitsblattbilder gerendert und geöffnet. Zusätzlich wurden die vier nativen Office-PDF-Abbildungen geöffnet; die endgültigen deutschen Zahlenformate, Spaltenabstände und einseitigen Druckbereiche wurden kontrolliert. Die Office-Konvertierung verwendet die gebündelte `soffice`-Override-Datei des Codex-Runtimes.

Zwanzig ausgewählte PDF-Abbildungen wurden als Bilder geöffnet, darunter alle fünf Forderungsanmeldungen, der vorläufige Beschluss, das Urteil, Lieferantenrechnung und Herausgabeverlangen, Gutscheinbeleg, Gutscheinkarte, Mehllieferschein sowie E-Mail- und Excel-Abbildungen. Es wird keine manuelle Sichtprüfung sämtlicher 87 PDF-Seiten behauptet. Automatisch wurden sämtliche 87 Abbildungen auf lesbaren Text, A4-Format, gültige PDF-Struktur und fehlenden Warntext geprüft. Die ausgewählten Ansichten zeigten keine abgeschnittenen Texte oder überlagerte Tabellen.

Die Rendernachweise liegen unter `/tmp/insolvenzsachbearbeitung-20261021/qa-betriebsakten/`. `docx-render-checks.json` führt die zwanzig DOCX-Seitenbilder auf, `pdf-sample-images.json` die zwanzig PDF-Stichproben. Die Excel-Renderings und Auswertungen stehen im Unterordner `xlsx`; die endgültigen nativen Ansichten heißen `claims-final.png`, `inventory-final.png`, `ledger-final.png` und `cafe-final-1.png`.

## 1.3. Rechen- und Belegkontrollen

| Arbeitsmappe | Kontrollwert | Tatsächliche Prüfung | Aussagegrenze |
| --- | ---: | --- | --- |
| Katzenbogen, Forderungsliste | 23.957,33 EUR | Neun Formeln; Gläubigerkorrekturen von 595,00 EUR und 67,67 EUR nachvollzogen. | Arbeitsstand ohne Feststellung oder Verteilung. |
| Katzenbogen, Warenbestand | 25.000,00 EUR | Vier Formeln; 200 × 60,00 + 200 × 35,00 + 300 × 20,00. | Brutto-Einkaufswert; Eigentum und Herausgabe bleiben streitig. |
| Werkzeugkiste, Belegliste | 2.380,00 EUR | Vier Formeln; 1.071,00 + 357,00 + 1.428,00 − 476,00. | Summe der bezeichneten Belege ohne einheitlichen Rang. |
| Café, Gutscheine und Bestand | 900,00 / 2.500,00 EUR | Sechs Formeln; 36 offene Gutscheine sowie bereinigte Standortbestände. | Unverkaufte Karten begründen keinen Verkaufsumsatz. |

In jeder Arbeitsmappe wurde während des Erstelllaufs eine Eingabe verändert, das veränderte Formelergebnis kontrolliert und die Eingabe vor Export wiederhergestellt. Nach Export wurden die tatsächlichen Formelzellen und gespeicherten Ergebnisse aus dem XLSX-Paket gelesen. Die 23 Formeln und vier Eingabeänderungstests sind in `xlsx/xlsx-checks.json` protokolliert. Die unabhängigen Betragskontrollen sind Bestandteil des Testskripts. Es wurde keine zweite Berechnungsbibliothek zur Erstellung der Arbeitsmappen verwendet.

Der Kaufhausfall trennt bestätigten Kaufauftrag, unterschriebenes Lieferantenblatt, unbestätigte spätere AGB und nicht unterzeichneten Kommissionsentwurf. Inventur und alte Verkaufscodes werden nicht als Beweis eines Verkaufs derselben Charge gleichgesetzt. Die fünf Anmeldungen FAA01–05 sind eigene Original-PDFs. Die GmbH und ihre Geschäftsführerin bleiben rechtlich unterschiedliche Anspruchsgegner; der Schuldnerwiderspruch wird nicht mit einem Verwalterwiderspruch gleichgesetzt.

Die ausgeführte [Anwendungsprobe](../anwendungsprobe-fuenf-anmeldungen.md) enthält fünf begründete Prüfentwürfe, eine Betragsübersicht und einen vollständigen Nachforderungsbrief. Sie dokumentiert ihren bekannten Bearbeitungskontext und ist ausdrücklich kein Blindtest. Die Pluginbeispiele wurden gegen die tatsächlichen Anmeldungen, Warenbelege und Caféunterlagen gelesen; Abweichungen wurden dem Pluginbearbeiter mitgeteilt und korrigierte Passagen nachgelesen.

## 1.4. Pakete und Reproduzierbarkeit

Die Original-ZIPs enthalten die unveränderten Originaldateien und die zweisprachige `README.txt` als ersten Eintrag. Die Einzel-PDF-ZIPs enthalten genau die 87 PDF-Abbildungen und je eine README. Alle Archive sind flach, unverschlüsselt, lesbar und ohne Markdown oder Gesamt-PDF im Original-ZIP. Die Pflichtwarnung steht ausschließlich in den Fall-READMEs und ZIP-READMEs. Die Testakten-PDFs enthalten weder Warnseite noch Warntext.

Der abschließende Paketmodus hat die vorhandenen Originale verwendet. SHA-256-Abgleiche vor und nach dem Paketieren bestätigen ihre Unverändertheit. Zwei unabhängige Paketläufe lieferten für alle neun Exportdateien identische Bytes. Die gemeinsamen ZIP- und A4-Prüffunktionen des Repositories wurden auf die drei Komponentenakten angewandt. Die allgemeinen Validator-Hauptprogramme verlangen zusätzlich repo-weite Sammelarchive und ein Gesamt-PDF im allgemeinen Arbeitsdateien-ZIP; diese globalen Veröffentlichungsprodukte waren nicht Gegenstand dieses Komponentenauftrags.

Die Ergebnisse stehen in [betriebsakten-pruefung.json](betriebsakten-pruefung.json). Die drei fallbezogenen JSON-Manifeste im selben Ordner enthalten pro Original Dateiname, SHA-256-Wert, Seitenzahl und Anfangsseite. Alle Fall-READMEs enthalten die vier Navigationslinks, reservierte Kontaktmarkierung, Downloadmarkierungen und Tabellen mit höchstens drei Spalten.

## 1.5. Wiederholung und Dateien

Der [Builder](../../../scripts/build-insolvenzsachbearbeitung-betriebsakten.py) verwendet die [Fixturedatei](../../../scripts/data/insolvenzsachbearbeitung-betriebsakten.json) und den [XLSX-Builder](../../../scripts/build-insolvenzsachbearbeitung-betriebsakten-xlsx.mjs). Er liest vorhandene gemeinsame Hilfsfunktionen; bestehende globale Builder wurden durch diese Teilaufgabe nicht geändert.

Mit dem gebündelten Python wurden diese Befehle erfolgreich ausgeführt:

```sh
python scripts/build-insolvenzsachbearbeitung-betriebsakten.py
python scripts/build-insolvenzsachbearbeitung-betriebsakten.py --package-only
python scripts/build-insolvenzsachbearbeitung-betriebsakten.py --package-only --dist /tmp/insolvenzsachbearbeitung-20261021/repro-betriebsakten --qa /tmp/insolvenzsachbearbeitung-20261021/qa-betriebsakten-repro
python scripts/test-insolvenzsachbearbeitung-betriebsakten.py --repro /tmp/insolvenzsachbearbeitung-20261021/repro-betriebsakten
```

Die neun endgültigen Exportdateien liegen in `/tmp/insolvenzsachbearbeitung-20261021/dist-akten/`. Je Fall sind `<Fallslug>_gesamt.pdf`, `testakte-<Fallslug>.zip` und `testakte-<Fallslug>-einzelpdfs.zip` vorhanden. Die Dateinamen beziehen sich auf das Komponentenrelease `insolvenzsachbearbeitung-v1.0.0`; dieser Bericht behauptet keine Veröffentlichung oder Übertragung.
