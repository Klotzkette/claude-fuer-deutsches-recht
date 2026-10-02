# 1. Prüfung der einfachen Testakte Kleinhausen

Stand: 2. Oktober 2026. Geprüft wurden alle **31 Originaldateien**: 23 Word-Dokumente, sechs E-Mails, eine Textdatei und eine Excel-Arbeitsmappe mit drei Blättern. Die 30 Textoriginale und alle drei Tabellenblätter wurden vollständig gelesen.

## 1.1 Ergebnis

Die Akte bleibt bei fünf selbst nutzenden Eigentümern mit je 200/1000 Miteigentumsanteilen. Die unabhängige Nachrechnung der acht Belege und aller 116 Bankbewegungen ergibt 5.660 EUR Kosten. 60 vollständig und rechtzeitig gezahlte Monatsraten ergeben 7.500 EUR; davon betreffen 6.000 EUR die Kosten und 1.500 EUR die Rücklage.

Die Kontenbrücke stimmt: 1.000 + 7.500 − 5.660 − 1.500 = 1.340 EUR auf dem Betriebskonto; 5.000 + 1.500 = 6.500 EUR auf dem Rücklagenkonto. Zusammen sind es 7.840 EUR. Jeder Einheit sind 1.132 EUR tatsächliche Kosten zuzuordnen; gegenüber 1.200 EUR Kostenvorschüssen ergeben sich 68 EUR Anpassungsbetrag.

Zwei kleine Abweichungen sind gewollt: Der Abrechnungsentwurf enthält 260 statt 240 EUR Allgemeinstrom und weist dadurch durchgängig 64 statt 68 EUR Guthaben je Einheit aus. Bei der sonst betragsmäßig richtigen Reinigung ist R-2025-71 statt R-2025-17 eingetragen. Die Folgewerte desselben Betragsfehlers sind keine zusätzlichen Fallstricke.

Die Beschlussvorlage betrifft konkret die Anpassung der Kostenvorschüsse. Sie ist noch nicht beschlossen; die Auszahlung folgt erst nach Beschlussfassung. Rücklagenbeiträge werden weder als verbrauchte Kosten noch doppelt als Vermögen angesetzt. Der Vermögensbericht ist als eigenes Aktenstück vorhanden. Es gibt keine versteckte Miet-, Heizkosten-, Zahlungsrückstands- oder Haftungsfrage.

## 1.2 Nachweise

- [Redaktionelle Gegenprüfung mit konkreten Ergebnissen und Grenzen](redaktionelle-pruefung.json).
- [Geprüfter Originalbestand mit 31 SHA-256-Werten](originalbestand.json).
- [Sechs bestandene Regressionstests](regression.log), darunter jede Bankbewegung, fünf Eigentümerkonten und vier bytegleiche E-Mail-Anhänge.
- [Gezielte amtliche Normprüfung](quellenbericht.md) und [strukturierte Quellen](normen.json).
- [Wiederholbarer Regressionstest](../../../scripts/test-weg-kleinhausen.py).

Die vor dem Freeze festgestellten Banktags- und Stichtagsdarstellungen wurden berichtigt und im finalen Bestand erneut geprüft. Das Hashinventar stimmt mit dem finalen Autorenfreeze überein.

## 1.3 Prüfungsgrenze

Dies ist eine redaktionelle Gegenlese mit deterministischen Datei-, MIME- und Rechenprüfungen, **kein neuer Modelltest**. Die Aussage über zwei beabsichtigte Abweichungen ist keine allgemeine Fehlerfreiheitsgarantie. Visuelle Word-/Excel-/PDF-Prüfungen und die Prüfung veröffentlichter Downloads werden getrennt dokumentiert. Es wurden keine neuen Gerichtsentscheidungen oder Literaturfundstellen erfunden und nicht sämtliche 93 Skills erneut geprüft. Die Prüfunterlagen liegen außerhalb der exportierten Arbeitsakte.

## 1.4 Visuelle und technische Abschlussprüfung

Alle 23 Word-Seiten und alle drei Excel-Blätter wurden vollständig visuell angesehen. Die Excel-Datei wurde mit LibreOffice tatsächlich neu berechnet; zwei veränderte Eingaben prüften die Formelreaktion. Die E-Mail-Anlagen wurden gegen die Originaldateien abgeglichen. Nachweise: [Word](word-visual-review.json), [Excel](spreadsheet-visual-review.json) und [Neuberechnung und Anlagen](native-recalculation-mime-checks.json).

Die 31 Einzel-PDFs haben zusammen 38 Seiten; das Gesamt-PDF umfasst mit den Trennblättern 62 Seiten. Von den insgesamt 100 gerenderten Seiten wurden alle 69 unterschiedlichen Seiten einzeln vollständig angesehen. Die übrigen 31 Seiten stimmen pixelgenau mit bereits geprüften Seiten überein. Nachweise: [Gesamtergebnis](pdf-final-visual-review.json), [Seiten 0–34](pdf-visual-part-1.json) und [Seiten 35–68](pdf-visual-part-2.json). Pfade unter `build-evidence/` sowie `qa/` bezeichnen temporäre Rendernachweise; die SHA-256-Werte dokumentieren den geprüften Stand.

Die [24 technischen Prüfungen](check-results.json) bestanden nach einer Versionskorrektur: Beim ersten Durchlauf standen 15 gerichtliche Plugin-Manifeste noch auf der Vorversion. Der [erneute Marketplace-Importcheck](marketplace-import-retry.json) besteht nach deren Anpassung. Der ursprüngliche Fehlerlauf bleibt sichtbar. Die [Bestandsprüfung](preserved-existing-content.json) bestätigt unveränderte bisherige WEG-Unterlagen, Skills und eigenständige Prompts. Diese technischen und visuellen Prüfungen ersetzen keinen Modelltest; veröffentlichte Downloads werden erst nach dem Release gesondert abgeglichen.
