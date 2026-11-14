# 1 Hamburger Entsorgungsakte

Prüfstand: 14. November 2026. Diese redaktionelle Datei steht außerhalb der exportierten Arbeitsakte. Die Parteien, Beschäftigten, Datensätze und der konkrete Rechtsstreit sind erfunden. Das Gericht ist eine wirkliche Institution; die Fallaktennummer bezeichnet kein behauptetes wirkliches Verfahren.

## 1.1 Fallaufbau und Arbeitsstände

Die Backbord Backstube GmbH wird von der privaten Elbmarsch Wertstofflogistik GmbH auf 21.532,47 EUR verklagt. Neun Rechnungen ergeben 34.545,22 EUR; auf die ersten beiden Rechnungen entfielen vollständige Zahlungen, auf die sieben weiteren jeweils 800 EUR. Die Zahlungen ergeben 13.012,75 EUR. Keine Mahnpauschale und keine vorgerichtlichen Anwaltskosten werden zusätzlich eingeklagt.

Die Grundakte enthält keine gerichtlichen Dokumente und keine ausgearbeitete Verteidigung. Sie zeigt eine zunächst widersprüchliche Menge, die Reklamationen, das originale Übergabeprotokoll, die Rechnungen und die tatsächlichen Überweisungen. Der andere Identifikator auf Rechnung und Übergabeprotokoll ist ein auffindbarer Widerspruch, beweist aber allein weder die Ursache noch sämtliche tatsächlich ausgeführten Leistungen. Die Mandantin hat am Anfang eine Nummer von der Rechnung vorgelesen, ohne den Behälter zu kontrollieren; sie berichtigt dies ausdrücklich in ihrer späteren E-Mail.

Die Nachlieferung enthält den gesicherten Importverlauf, das IT-Ticket, die Betriebsunterlagen des anderen Kunden und 274 Fahrzeugereignisse: 196 Ereignisse am Klinikum und 78 am Hof der Backstube. Das klinische Material betrifft ausschließlich nicht gefährlichen Gewerberestabfall aus Verwaltung, Kantine und öffentlichen Bereichen. Medizinische Abfallströme bleiben ausdrücklich außerhalb der Verträge. Das Klinikmaterial enthält keine Patientendaten.

Die Tabellen bilden Originaldaten ab; sie enthalten keine fertige korrigierte Forderungsabrechnung und keine Musterlösung. Die Zahlungen sind rechnungsbezogen erfolgt. Die Wirkung möglicher Überzahlungen, ein möglicher Gegenanspruch und die prozessualen Folgen der nachträglichen Aufklärung bleiben zu bearbeiten. Eine Klagerücknahme oder gerichtliche Fristverlängerung ist nicht fingiert.

## 1.2 Überprüfte Primärquellen

- [§ 253 ZPO](https://www.gesetze-im-internet.de/zpo/__253.html): bestimmter Antrag, Gericht und Parteien; Angaben zu außergerichtlicher Streitbeilegung, Einzelrichter und Videoverhandlung. Die Klage enthält diese Angaben.
- [§ 276 ZPO](https://www.gesetze-im-internet.de/zpo/__276.html): zweiwöchige Notfrist zur Verteidigungsanzeige und mindestens zwei weitere Wochen zur Klageerwiderung; Belehrung über Kosten und Vollstreckbarkeit. Die Verfügung trennt die Fristen und nennt die Folgen nach §§ 91, 708 Nr. 2 ZPO.
- [§ 78 ZPO](https://www.gesetze-im-internet.de/zpo/__78.html) und [§ 331 ZPO](https://www.gesetze-im-internet.de/zpo/__331.html): Anwaltszwang und Voraussetzungen eines Versäumnisurteils im schriftlichen Vorverfahren. Kein automatisches Obsiegen wegen fehlender Verteidigungsanzeige wird behauptet.
- [§ 631 BGB](https://www.gesetze-im-internet.de/bgb/__631.html): die Klage legt den konkret vereinbarten Entsorgungserfolg und die geschuldete Vergütung dar; die Behältergestellung wird gesondert angesprochen. Der Vertrag ersetzt nicht den Nachweis der konkreten Leistung.
- [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html) und [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html): behaupteter Verzug nach Zugang der Mahnung und Fristablauf; neun Prozentpunkte bei der hier beiderseits unternehmerischen Entgeltforderung. Der Zinsantrag ist Parteivorbringen, kein festgestellter Anspruch.
- [§ 23 GVG](https://www.gesetze-im-internet.de/gvg/__23.html) und [§ 71 GVG](https://www.gesetze-im-internet.de/gvg/__71.html): Der Streitwert liegt auch oberhalb der aktuellen amtsgerichtlichen Wertgrenze von 10.000 EUR.
- [Landgericht Hamburg, Kontakt](https://justiz.hamburg.de/gerichte/landgericht-hamburg/kontakt): Sievekingplatz 1, 20355 Hamburg.
- [Geschäftsverteilungsplan 2026, Stand 4. Mai 2026](https://justiz.hamburg.de/resource/blob/1171340/469329c8af395768da85c4301678d250/gvp-2026-stand-04-05-2026-data.pdf), Seite 57 des PDF: Zivilkammer 16 nimmt am Hauptturnus erstinstanzlicher Sachen teil. Die fiktive Akte verwendet daher 316 O 287/26. Eine tatsächliche Zuteilung des erfundenen Vorgangs wird damit nicht behauptet.

Es werden keine unüberprüften Rechtsprechungs- oder Literaturfundstellen als tragende Nachweise eingesetzt. Für den Fallaufbau reichen die geprüften gesetzlichen Anforderungen; eine materiell abschließende Bewertung wird bewusst nicht in die Akte geschrieben.

## 1.3 Technische Prüfung

`scripts/test-hamburg-baeckerei-akte.py` prüft sechs Gruppen: Phasentrennung und native Formate, unabhängige Rechnung aus den CSV-Einzelereignissen, formelle Mindestbestandteile der Klage und Verfügung, bytegenaue MIME-Anhänge, XLSX-Rücklesung sowie abgeschlossene Dokumente ohne Platzhalter oder Warntexte im PDF. Die Warntexte stehen auf der README-Seite vor den Downloads und werden vom zentralen ZIP-Builder auf die ZIP-Wurzel gelegt.

Die 55 Originaldateien umfassen PDF, DOCX, XLSX, EML, CSV und PNG. Die Original-PDFs haben 49 Seiten; hinzu kommen zwei einseitige Word-Dokumente und die Lesefassungen der übrigen Originalformate. Alle 49 Original-PDF-Seiten und beide Word-Seiten wurden gerendert und auf sichtbare Überläufe und Seitenaufbau geprüft; Klage, Vertrag und Rechnungsbeispiel zusätzlich einzeln angesehen. Beide nativen Arbeitsmappen wurden mit Artifact Tool erzeugt, zurückgelesen und ihre Ansichten gerendert. Die Word-Titel wurden nach der ersten Renderprüfung von geerbter Theme-Schrift und Absatzrand bereinigt. Der Umschlag ist als Umschlagvorderseite gestaltet.

Die technische Prüfung ist keine Behauptung, dass ein Gericht den Anspruch bejaht oder dass die Unterlagen eine vollständig automatische Rechtsberatung ermöglichen.
