# Weserfunken: Form und Satz der Schriftsätze

Prüfstand: 14. November 2026. Fiktiver Aktenstand weiterhin 28. September 2026.

## 1. Umfang und Bestandsschutz

Die Klage besitzt jetzt einen vollständigen Kanzleikopf, die postalische Anschrift des Landgerichts Bremen, ein ausformuliertes Rubrum und vorangestellte Haupt-, Hilfs-, Auskunfts- und Nebenanträge. Die Begründung verwendet eine echte Dezimalhierarchie. Die Klageerwiderung und die Verteidigungsanzeige erhalten dazu passende eigene Kanzleibögen. Eine Übermittlungsart wird nicht aus Kanzlei oder Empfänger abgeleitet.

Die Ausführungen wurden nicht gekürzt oder im Sinne einer Musterlösung umgeschrieben. Die bewusst streitige Zuordnung des Zahlungsempfängers und die Auseinandersetzung um Vertragsübernahme und Abtretung bleiben erhalten. In der Klage sind 97 Sach- und Begründungsabsätze erhalten (87 wörtlich, 10 mit angepassten Verweisnummern), in der Erwiderung 80 (70 wörtlich, 10 mit angepassten Verweisnummern). Doppelte Antragswiederholungen wurden in einen geordneten Eingangsabschnitt überführt.

Von den 42 historisch geschützten Originalen ändern sich genau fünf: Klage, Erwiderung, Verteidigungsanzeige sowie die Seitenangaben in gerichtlicher Verfügung und Posteingangsvermerk. Die übrigen 37 Dateien sind bytegleich. Die historischen SHA-Dateien bleiben unverändert. Die zusätzliche Datei `scripts/fixtures/fintech-bremen/satz-migration-2026-11.json` dokumentiert alte und neu erzeugte Hashes, Gründe und Absatznachweise. Sie ersetzt keine fehlende Neugenerierung.

## 2. Satz und Sichtkontrolle

Die ursprünglichen künstlichen Seitenblöcke wurden durch fließenden Satz ersetzt. Die Klage umfasst 18 Seiten, die native Word-Erwiderung nach LibreOffice-Konvertierung 14 Seiten. Das ist ein anderer Umbruch bei erhaltenem Begründungsumfang. Hauptschrift ist echtes Times New Roman 11 Punkt. Der PDF-Renderer verlangt die regulären, fetten, kursiven und fett-kursiven TTF-Dateien. Eine Ersatzschrift wird nicht zugelassen.

Alle Seiten der geänderten Klage, Erwiderung, Verteidigungsanzeige, Verfügung und des Posteingangsvermerks wurden gerendert und visuell angesehen. Kopf, Anschrift, Rubrum, Nummerierung, Seitenzählung, Unterschriftszeilen und Seitenübergänge wurden kontrolliert. Ein zunächst isolierter Signaturabsatz der Erwiderung wurde mit dem vorhergehenden Anlagenabsatz zusammengehalten. Der aktualisierte Registeranfang wurde ebenfalls angesehen. Eine neue Sichtprüfung sämtlicher unveränderter Anlagen ist damit nicht behauptet.

## 3. Formbezogene Quellenprüfung

- Die Anschrift Domsheide 16, 28195 Bremen wurde an der [Kontaktseite des Landgerichts Bremen](https://www.landgericht.bremen.de/kontakt/verkehrsanbindung-gerichtshaus-1998) geprüft.
- Die Benennung von Gericht und Parteien sowie der bestimmte Antrag wurden an [§ 253 ZPO](https://www.gesetze-im-internet.de/zpo/__253.html) ausgerichtet.

Diese Änderung enthält keine neue allgemeine Freigabe sämtlicher materiell-rechtlicher Aussagen der Lernakte. Parteivortrag bleibt Parteivortrag.

## 4. Ausgeführte Prüfungen

- `python scripts/test-fintech-bremen-schriftsatzsatz.py`: 7 erfolgreich, einschließlich tatsächlicher bitgleicher PDF-Neugenerierung.
- `python scripts/test-fintech-bremen-schriftsatzsatz.py --read-only`: 6 erfolgreich; prüft auch die tatsächlich verwendeten und eingebetteten TNR-Schriften, ohne lokale Schriftdateien für einen Neubau zu benötigen.
- `python scripts/test-fintech-bremen.py --assets <lokaler Paketordner>`: 14 erfolgreich, ohne übersprungene Tests.
- `python scripts/test-fintech-bremen-anfechtung-ergaenzung.py`: 5 erfolgreich.
- Python-Kompilierung der geänderten Module und `git diff --check`: erfolgreich.

Der Regressionstest verwendet den aus der früheren PDF extrahierten Empfängerbereich und deren alte flache Überschriften. Er weist das frühere Dokument wegen fehlender Gerichtsanschrift, fehlender Untergliederung und fehlendem vorangestellten Antragsabschnitt zurück. Die neuen Originale werden dagegen tatsächlich ausgelesen, nicht nur anhand ihrer Dateinamen akzeptiert.

## 5. Lokale Pakete

Die bestehende Originalakten- und Einzel-PDF-Pipeline wurde ausgeführt. Das Originalarchiv enthält 62 Arbeitsdateien sowie den vorgeschriebenen README-Hinweis, darunter 41 Dateien im Ordner `Grundakte/`. Es enthält kein Gesamt-PDF. Die Formate sind PDF, DOCX, EML, XLSX, CSV und TXT.

Das Einzel-PDF-Archiv enthält 62 PDFs mit 226 Seiten sowie den README-Hinweis. Die vollständige Lesefassung besitzt zusätzlich drei Registerseiten, insgesamt 229 Seiten. Dateien, Anlagenbezeichnungen und paketierte Originalbytes wurden mit dem Quellbestand abgeglichen. Die lokalen Paketprüfungen belegen noch keine Veröffentlichung; diese erfolgt im übergreifenden Releaseverfahren.
