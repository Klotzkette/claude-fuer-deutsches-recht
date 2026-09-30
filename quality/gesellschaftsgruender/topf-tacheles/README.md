# 1. Qualitätsnachweis: Topf & Tacheles

Prüfung am 30.09.2026 für die einfache Gründungsakte. Die Nachweise liegen außerhalb der Arbeitsakte und werden nicht in deren ZIPs oder Gesamt-PDF aufgenommen.

## 1.1. Inhalt und gewünschter Entwurfsstand

Die Akte enthält genau 15 native Originale: drei DOCX, vier EML, einen TXT-Chat und sieben JPG-Datenkarten. Alle Arbeitsinhalte sind deutschsprachig. Die beiden Vertragsentwürfe enthalten keine Vor- oder Nachnamen der sieben Personen; die Prüfung erfasst sämtliche XML-Bestandteile der DOCX-Container. P01 bis P07 bleiben erhalten. Nennbeträge und Quoten ergeben 25.000 EUR und 100 Prozent. Der [Dateinachweis](inhalt-pruefung.json) hält die geprüften Originalhashes fest.

Die Namensfelder und offenen Entscheidungen sind ausdrücklich vom Nutzer bestellt. Sie dürfen hier sichtbar bleiben. Die sieben JPGs sind ebenso ausdrücklich als fiktive Datenblätter gekennzeichnet; sie sind keine amtlichen Ausweisnachbildungen. Diese beiden Eigenschaften sind keine Mängel der Dokumentvollständigkeit und keine Aufforderung, fehlende Entscheidungen zu erfinden.

## 1.2. Fachliche Prüfung

Der [Quellenvermerk](rechtspruefung.md) dokumentiert die tatsächlich gelesenen amtlichen Normen. Das [Vertragsreview](vertragsreview.md) trennt den ursprünglichen Befund von der nachgelesenen Korrektur. Die Abgrenzung zwischen Satzungsänderung, internem Gesellschafterbeschluss und vertraglicher Pflicht wurde präzisiert. Die irrtümliche 25-Prozent-Vorstellung bleibt als zu prüfende Behauptung eines Gründers im Fall erhalten. Die Prüfung belegt keine Beurkundungsreife; die beauftragten Entscheidungen sind weiterhin offen.

## 1.3. Tatsächliche Sichtprüfungen

Alle sieben Word-Seiten wurden mit der gebündelten Office-Laufzeit gerendert und vom Dokumentautor einzeln betrachtet: Vorüberlegungen zwei Seiten, Satzung drei Seiten und Gesellschaftervereinbarung zwei Seiten. Sämtliche sieben nativen JPGs wurden zusätzlich einzeln betrachtet.

Eine unabhängige Sichtprüfung erfasste alle 22 Seiten des Gesamt-PDFs. Der [Seitenbericht](sichtpruefung.md) und der [Hashnachweis](sichtpruefung.json) dokumentieren den geprüften Umfang. Keine abgeschnittenen Felder, kollidierenden Zeilen oder unleserlichen Datenkarten festgestellt. Das Gesamt-PDF enthält 19 Inhaltsseiten und drei vom zentralen Builder erzeugte Word-Trennblätter.

Zusätzlich wurden die Einzel-PDFs der vier E-Mails, des Chats und der Karte P01 vollständig betrachtet. Alle sieben Karten-PDFs betten die unveränderten originalen JPEG-Datenströme ein; der [Bildvergleich](einzelpdf-bilder.json) prüft die tatsächlichen PDF-Bildobjekte. Die Karten sind Bildinhalt, keine nachgewiesene OCR-Textebene.

## 1.4. Archive und automatische Prüfungen

Der [Archivnachweis](archives.json) bestätigt die zentrale Verpackung: Original-ZIP mit 15 Originalen, Gesamt-PDF und README.txt; Einzel-PDF-ZIP mit 15 Einzel-PDFs und README.txt. Die erwarteten Dateinamen und Herkunftshinweise wurden mit den bestehenden zentralen Validatorfunktionen abgeglichen.

Die [Prüfliste](checks.json) dokumentiert bestandene Dokumentqualität, lösungsfreie Arbeitsakte, Downloadhinweise, Verzeichnisse, Navigation, Release-Routing, bestehende Startup-Regressionen, Aktenstruktur und redaktionelle Qualitätsprofile. Diese technischen Prüfungen werden nicht als Modelltest ausgegeben. Ein neuer interaktiver Modelllauf wurde für diese reine Akten-Ergänzung nicht durchgeführt. Die bereits vorhandenen Skills wurden nicht geändert.

## 1.5. Wiederherstellung

Die beiden Builder `scripts/build-topf-tacheles-akten.py` und `scripts/build-topf-tacheles-personenkarten.py` nutzen denselben Faktensatz `scripts/data/topf-tacheles/fakten.json`. Gesamt-PDF und Archive entstehen mit den vorhandenen zentralen Akten-Buildern. Versionsstände und öffentliche Downloads werden getrennt im Release geprüft; dieser Nachweis behauptet keinen bereits erfolgten öffentlichen Downloadabgleich.
