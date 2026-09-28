# 1. Sichtprüfung des nativen Release-PDF

Stand: 2026-09-28T02:20:07+02:00. Geprüft wurde das durch den zentralen Builder erzeugte Gesamt-PDF `testakten/bauwirtschaft-hildesheim-lebensakte/gesamt-pdf/bauwirtschaft-hildesheim-lebensakte_gesamt.pdf` gegen die zuvor gesichtete Fassung `/tmp/hildesheim-lebensakte/qa/gesamt-visuell-geprueft.pdf`.

Beide Fassungen haben **1.171 Seiten**. Der unabhängige Vergleich aller Seiten mit pypdf bestätigt **144 Seiten mit verändertem Inhaltsstream bzw. extrahiertem Text** und **1.027 unveränderte Seiten**. Die Zuordnung berücksichtigt die elf Registerseiten vor den 1.160 Dokumentseiten aus 366 Originalen. Dieser Nachtrag betrifft ausschließlich die 144 abweichenden Seiten; für die unveränderten Seiten gilt die bereits dokumentierte Sichtprüfung.

# 2. Tatsächlich angesehener Umfang

Alle **144 abweichenden Seiten** der neuen Fassung wurden vollständig visuell mit `view_image` angesehen:

- Finanzprüfung: **111 Seiten, Gesamtseiten 905–1015**, sämtliche 28 XML-Lesefassungen der Originale 080–106 und 119. Geprüft anhand 37 Kontaktbögen mit je drei unskaliert eingefügten Seitenrastern; jede Seite wurde mit 1.415 × 2.000 Pixeln gerendert.
- Planungsprüfung: **33 Seiten**, Gesamtseiten 30, 47, 50, 55, 279, 728, 757, 758, 759, 760, 761, 763, 765, 769, 775, 776, 777, 778, 782, 783, 785, 872, 873, 874, 875, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047. Alle Seiten wurden vollständig anhand der neu erzeugten Raster angesehen; zusätzlich erfolgte ein Vergleich der Alt-/Neu-Pixel.

Kontrolliert wurden insbesondere Dateipfadzeilen, Zeilenenden, Seitenübergänge, kurze XML-Schlussseiten, Tabellen, Bilder, Kopf-/Fußzeilen und sichtbare Lesbarkeit. **Keine abgeschnittenen Zeilen, Überlagerungen oder sonstigen offenen Layoutbefunde im geprüften Umfang.**

# 3. Ursachen und Vollständigkeit

Die Abweichungen entstehen durch den neuen Aktennamen `bauwirtschaft-hildesheim-lebensakte` in den Fußzeilen und die ergänzten relativen Quellpfade in den Dateizeilen. Die Dokumentinhalte wurden dadurch nicht geändert.

Bei allen 33 Nicht-XML-Seiten ist der Textkörper nach Entfernung ausschließlich der Akten-/Dateizeilen exakt identisch. Außerhalb der zugehörigen Kopf-/Fußzeilenbereiche sind ihre Alt-/Neu-Raster pixelidentisch; es gibt dort keine Umbruchänderung.

Bei sämtlichen 28 XML-Dokumenten ist der über alle jeweiligen Seiten zusammengesetzte Dokumentkörper nach Entfernung der Akten-/Pfadzeilen und Normalisierung der Umbruch-Leerzeichen identisch. Lediglich beim langen Dateipfad des Originals 119 entsteht eine zweite Dateizeile: Auf Gesamtseiten 1013–1015 wandern `</ns2:Contact>` und die `TaxExclusiveAmount`-Zeile jeweils auf die Folgeseite. Beide Zeilen sind vollständig vorhanden; sämtliche drei Seiten wurden angesehen und bleiben sauber lesbar. Auch die bereits vorher vorhandenen kurzen XML-Schlussseiten enthalten ihre vollständigen End-Tags.

# 4. Prüffassung und Nachweise

SHA-256 der zuvor gesichteten Gesamtfassung:

`82f58d328735485aead6a84e8bc21709a43e69cc99df5b1dfdd4a6efa73cf3c0`

SHA-256 der finalen nativen Gesamtfassung, bei Abschluss erneut bestätigt:

`fabf8520e552868ce0e5b6bc40099e709f28deb3a32e3b2e924535e42cddd990`

Die maschinenlesbare vollständige Seiten-/Quellzuordnung und der Textvergleich liegen in `/tmp/hildesheim-lebensakte/native-release-qa/comparison.json`. Raster, Seitenliste und XML-Körperabgleich liegen unter `xml/manifest.json`; der ergänzende Bericht und Pixelvergleich unter `planung.md` und `planung-compare.json` desselben QA-Verzeichnisses. Der verwendete Quellen-/Renderindex ist `/tmp/hildesheim-lebensakte/release-qa/index.json`.

Die Prüfung erfolgte ausschließlich lesend an Originalen und PDFs. Dieser Vermerk bestätigt den beschriebenen Rendervergleich und die tatsächliche Sichtprüfung; er ist keine erneute rechtliche oder finanzmathematische Modellprüfung.
