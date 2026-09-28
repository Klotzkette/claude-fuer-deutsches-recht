# 1. Abschlussprüfung der erweiterten Hildesheimer Projektakte

Prüfstand: 28. September 2026. Gegenstand ist die Erweiterung für v445.8.0; dieser Vermerk ist kein Beleg einer bereits abgeschlossenen Veröffentlichung. Die Release-Prüfung und der öffentliche Download werden zusätzlich anhand des tatsächlichen GitHub-Laufs kontrolliert.

## 1.1. Bestand und Auftragsgrenzen

366 Originaldateien werden ohne Exportverlust bereitgestellt: 175 DOCX, 101 PDF, 49 EML, 28 XML, sieben CSV, drei XLSX, zwei PNG und eine TXT-Datei. Alle 198 Ausgangsdateien sind bytegleich übernommen. Der neue Bestand ergänzt 168 Originale. Die Gesamtakte umfasst in der geprüften lokalen Release-Fassung 1.171 Seiten: elf Registerseiten und 1.160 Seiten mit Akteninhalt. Jeder Originaldatei ist ein navigierbares Lesezeichen und ein gedruckter Seitenverweis zugeordnet.

Das Hauptprojekt bleibt Vermietung. Der Bauträgerverkauf ist ausschließlich eine unbeschlossene Variante vom 1. November 2027; weder Kaufabschlüsse noch Einnahmen werden fingiert. Der angefragte tägliche Band ist ein Bautagebuch mit 304 Kalendertagen, kein Fotobuch. Die vorhandenen 29 Skills bleiben bestehen. Die zusätzliche Werkstatt umfasst genau 100 inhaltliche Stationen und 100 Word-/PDF-Seiten.

## 1.2. Dokumente, Layout und Bearbeitbarkeit

Die 136 neu hinzugekommenen Worddateien umfassen 568 Seiten. Alle wurden nativ gerendert und vollständig visuell geprüft: 95 Bau-Dokumente mit 459 Seiten, 36 Dokumente der Verkaufsoption mit 104 Seiten sowie fünf Dokumente für Projektorganisation und kaufmännische Bearbeitung mit fünf Seiten. Die 304 Tagesseiten wurden zusätzlich unabhängig auf Zeitfolge, Personal, Mengen und Kenntnisstand geprüft. Änderungen wurden auf den betroffenen Seiten erneut angesehen; die übrigen Seiten wurden per Hashvergleich zugeordnet.

Die 28 zusätzlichen E-Mail-Lesefassungen, 217 Seiten der vier neuen CSV-Register und alle elf Registerseiten der Gesamtakte wurden vollständig visuell kontrolliert. Die Prüfung der 100-seitigen Werkstatt und ihrer 1.192 Textblöcke ist separat dokumentiert. Für den tatsächlichen zentralen Release-Build werden abweichende Leseseiten erneut geprüft; der abschließende Nachtrag liegt unter `bau/native-release-sichtpruefung.md`.

Die vier kaufmännischen Wordvorlagen wurden zusätzlich mit Testwerten vollständig befüllt, gespeichert, erneut geöffnet und gerendert. Alle 16, 16, 15 beziehungsweise 21 nativen Inhaltssteuerelemente übernahmen die vorgesehenen Werte; alle vier ausgefüllten einseitigen Fassungen wurden visuell angesehen. Diese Testbefüllungen sind keine Aktenoriginale und werden nicht mitgeliefert. Die übrigen 14 Vorlagen bleiben bearbeitbare, ausformulierte Wordmuster mit sichtbaren Eingabestellen.

## 1.3. Inhaltliche und rechnerische Nachweise

Die Quellen der 28 Rechnungseingangs-E-Mails sind echte MIME-Dateien mit den bytegleichen zugehörigen PDF- und XML-Anlagen. Datierung, Absender und Rechnungsidentität wurden geprüft. Die E-Mails erzeugen keine weiteren Forderungen. Die 38 Kostenbelege, 28 XRechnungen und drei Excel-Arbeitsmappen bleiben unverändert; ihre frühere Validierung wird durch diese Erweiterung nicht als neuer Prüfungslauf ausgegeben.

Die Bauprüfung gleicht 134 Detailpositionen gegen 26 ursprüngliche Pauschalgruppen und sieben Vertragssummen von insgesamt 2.080.000 EUR netto ab. Liefermengen, Ruhetage, Nachtragsstunden, Personaleinsatz und zeitlicher Kenntnisstand werden gesondert geprüft. Datierte Korrekturen erläutern widersprüchliche Kurzvermerke, ohne die Ausgangsbelege umzuschreiben. Die acht optionalen Erwerbsentwürfe und ihre Anlagen werden auf Flächen, Miteigentumsanteile, Preise, Raten und Sicherungsmechanik abgeglichen. Fachliche Quellen und Anwendungsgrenzen stehen in den jeweiligen Prüfberichten.

## 1.4. Exporte und technische Regression

Die Original-ZIP enthält 368 Einträge einschließlich README und Gesamt-PDF; die Einzel-PDF-ZIP enthält 367 Einträge einschließlich README. Für diese eine Projektakte bleiben Unterordner erhalten. Die Zuordnungen aller 365 übrigen vorhandenen Testaktenverzeichnisse wurden gegen die vorherige Exportlogik verglichen: keine Änderung der Archivnamen. Beide neuen Einzelarchive wurden mit den tatsächlichen Validatorfunktionen auf CRC, sichere Pfade, genaue Exportmenge, PDF-Inhalte und Herkunftshinweise geprüft. Die vollständigen Sammelarchive werden im Release-Workflow gebaut und geprüft.

Die unabhängigen Tests lesen die fertigen Dateien und Archive. Sie prüfen unter anderem Ausgangsdatei-Hashes, Kalenderfolge, LV-Rechnung, MIME-Anlagen, Verkaufsstatus, Vorlagenabgrenzung, PDF-Inhaltsabdeckung, Lesezeichen und gedruckte Registerverweise. Pfadtests erfassen Traversal, Windows-Sonderzeichen, Kollisionen, alte Flachstruktur und den ausdrücklich bestellten Bautagebuch-Teilband. Weitere Prüfungen betreffen bestehende HOAI-Akten, Prompt-Erhaltung, Navigation, Herkunftshinweise, Dokumentqualität, Pluginstruktur, Frontmatter, Marketplace und Prüfprofile. Der unabhängige Exportreview und die behobenen Befunde sind in `export-review.md` dokumentiert.

## 1.5. Tatsächliche Verhaltensprüfung und Grenzen

`verhaltenstest.md` enthält zwei manuell ausgeführte Fälle mit jeweils Erst- und Folgeantwort. Im Zahlungsfall führt eine später bestätigte Erstattung zur geschlossenen Rückforderung und zum Wegfall des überholten Briefs. Im Vertragsfall trennt die Erstbearbeitung technische Zuarbeit von unbefugter Individualgestaltung; nach Bestätigung eines unmittelbaren Anwaltsmandats entsteht eine konkret begrenzte Klausel mit nur der noch entscheidenden Produktfrage. Erwartungshorizonte wurden vor diesen Bearbeitungen nicht gelesen.

Diese zwei Fälle sind kein automatischer Aktivierungsnachweis und keine vollständige Modellbewertung aller 29 Skills. Technische Prüfungen und die Sichtung der simulierten Akte begründen keine allgemeine rechtliche oder bautechnische Fehlerfreiheitsgarantie. Quellenstand ist der 28. September 2026; das Projekt bis 2033 ist simuliert. Unbekanntes künftiges Recht wird nicht als verifiziert behandelt. DIN-/VDE-Volltexte und sämtliche denkbaren kommunalen oder steuerlichen Besonderheiten wurden nicht vollständig geprüft.
