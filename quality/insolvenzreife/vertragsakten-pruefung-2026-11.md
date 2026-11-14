# 1. Vertragsgrundlagen der drei Insolvenzreifeakten

Die Ergänzung stellt 40 vollständige Vertrags- und Abrechnungsunterlagen auf 78 PDF-Seiten bereit: 13 für Cottbus, elf für Zehlendorf und 16 für Prenzlau. Hinzu kommen drei CSV-Dateiverzeichnisse und drei E-Mails mit jeweils drei identischen Vertragsanlagen. Die Unterlagen werden vom Hauptbuilder über `scripts/insolvenzreife_vertragsakten.py` reproduzierbar erzeugt. Sie gehören vollständig zur Grundakte; fertige Kredit- oder Sicherheitenspiegel werden nicht vorgegeben.

## 1.1 Unveränderte Rechenbasis

`scripts/data/zu-insolvenzfaelle.json`, die historischen Bankauszüge, Buchungsjournale, OP-Listen und Kontrolldaten bleiben unverändert. Die Ergänzung führt keine neue Girozahlung ein. Bestehende Zahlungen werden in Abrechnungsanlagen nur aufgegliedert. Die drei bestehenden Erstbefunde für Zahlungsunfähigkeit und die getrennten Überschuldungsbefunde bleiben unverändert.

Die Vollverträge konkretisieren die zuvor nur in Bestätigungen bezeichneten Finanzierungen. Die ursprünglichen Valutierungen der Laufzeitdarlehen erfolgten vor Beginn des historischen Giroexports unmittelbar an Verkäufer. Die Vorausentgeltperiode bis Juni 2026 ist durch eigene Auszahlungsabrechnungen belegt, sodass keine bislang fehlenden laufenden Bankzinsen in den historischen Girobestand hineinerfunden werden. Die ausdrücklich vereinbarten zukünftigen Zins- und Tilgungstermine sind von tatsächlichen Zahlungen zu trennen.

## 1.2 Fallbezogene Abgrenzung

- Cottbus: OF-109 über 1.040.000 EUR einschließlich der gesondert gestundeten Rate von 58.000 EUR; Grundschuld und bestimmte Brennöfen; getrennte Zwischenlinie; Gesellschafterdarlehen mit bloßer Fälligkeitsverschiebung; vollständiger Außenlagermietvertrag mit Abfindung sowie Anschluss- und Rückbauvereinbarung. Die historischen Buchungstexte „Werkhallenmiete“ betreffen das Außenlager und werden nicht in eine Belastung der eigenen Halle umgedeutet.
- Zehlendorf: Hallendarlehen von 640.000 EUR, Grundschuld, eigenständige freie Linie, Gesellschafterforderung von insgesamt 185.000 EUR einschließlich 5.000 EUR bereits aufgelaufener Zinsen sowie die unterschriebene Rang- und Durchsetzungsvereinbarung. Maschinenpacht und Rückbau werden von Halleneigentum und anderen Werkaufträgen getrennt.
- Prenzlau: Fluggerätedarlehen von 545.000 EUR und bereits vollständig ausgereichte Linie von 75.000 EUR ergeben zusammen die unveränderte Bankverbindlichkeit von 620.000 EUR. Kauf und Sicherungsübereignung betreffen U-01 und U-02. Vier vollständige Leasingeinzelverträge betreffen U-03 bis U-06; ihre historischen Objektabrechnungen stimmen centgenau mit den Sammelzahlungen überein. Mai-Rate, Ablöse künftiger Leasingperioden, Gesellschafterdarlehen, befristete Ausstattung und Kartenreserve bleiben getrennte Vorgänge.

## 1.3 Rechtsquellen und Aussagegrenze

Die Unterschiede zwischen Nachrang, bloßer Stundung und Durchsetzungssperre wurden mit [§ 19 InsO](https://www.gesetze-im-internet.de/inso/__19.html) und [§ 39 InsO](https://www.gesetze-im-internet.de/inso/__39.html) abgeglichen. Die Akten enthalten vereinbarte Klauseln und Erklärungen der Beteiligten, keine Rechtsgutachten zur Wirksamkeit. Der Quellenabgleich ist keine vollständige Aktualitätsprüfung sämtlicher insolvenzrechtlicher Rechtsprechung.

## 1.4 Technische und visuelle Kontrolle

- Fünf ergänzende Vertragsaktentests prüfen Volltext, Vertragsparteien, A4, dezimale Gliederung, Dokumentenauswahl, Vertragsbeträge, Tilgungssummen, Monatsabrechnungen, unterscheidbare Finanzierungsbedingungen und identische MIME-Anlagen.
- Fünf bestehende Grundaktentests bestanden.
- Zwölf bestehende Anfechtungstests: elf bestanden, eine nur bei übergebenem Exportverzeichnis aktive Prüfung nicht ausgeführt.
- Vier bestehende Rechenfalltests bestanden; einschließlich der Vergleichstage, Quellenketten und Umschaltung von Patronat, Nachrang und Verwertung.
- Alle 78 Seiten gerendert und in Kontaktübersichten kontrolliert; Darlehensvertrag, Rangvereinbarung und Leasingabrechnung zusätzlich in großer Darstellung geprüft. Kein Wort außerhalb der definierten Seitenränder; keine sichtbaren Überlagerungen. Times New Roman ist in den PDF-Verträgen eingebettet. Kopf- und Fußzeilen, Anschriften, Seitenzahlen und fortgesetzte Tabellen sind vorhanden.

Der Hauptbuilder berührt bei vorhandenen DOCX- und EML-Dateien teilweise nur ZIP-Zeitstempel und MIME-Grenzen. Diese sachlich unveränderten Altdateien wurden vor der Übergabe bytegleich zum vorherigen Repository-Bestand wiederhergestellt. Die neuen Ausfertigungen besitzen deterministische PDF-Metadaten und feste MIME-Grenzen. Gesamt-PDF und Release-Archive sind durch die übergeordnete Integration separat neu zu bauen und zu prüfen.
