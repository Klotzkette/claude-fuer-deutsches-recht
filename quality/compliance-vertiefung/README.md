# Prüfung der Hamelner Compliance-Vertiefung

## 1 Gegenstand und Grenzen

Die Prüfung erfasst die Überarbeitung der fünf Skills, der drei eigenständigen Prompts, der 35 Word-Vorlagen und der 70 ergänzenden Aktenstücke in den 35 Hamelner Compliance-Fällen. Der Ausgangsbestand umfasst 338 unveränderte Originaldateien. Die Falltexte bleiben fiktiv. Die Prüfung ist keine rechtliche Endfreigabe und keine umfassende Leistungsmessung eines bestimmten Modells oder einer bestimmten Zieloberfläche.

## 2 Reproduzierbarer Bau

`scripts/build-compliance-hameln-vertiefung.py --output-root <Ziel>` erzeugt die zusätzlichen Originaldateien und Word-Vorlagen aus `scripts/data/compliance-hameln-vertiefung.json`. Der Builder erhält bestehende Aktenstücke. `scripts/build-compliance-hameln-release.py --dist <leeres Ziel> --rebuild-pdfs` baut Einzel-PDFs, identische Lesefassungen im Repo und in den Originalformat-ZIPs, das Workshop-Paket und den vollständigen Release-Bestand. Ohne `--rebuild-pdfs` weist er veraltete Lesefassungen zurück.

Die Office-Konvertierung benötigt LibreOffice. Für layoutgetreue Ausgabe müssen die im DOCX bezeichneten Schriften verfügbar sein; in dieser Prüfung werden die legitim vorhandenen Times-New-Roman-Dateien der macOS-Systeminstallation verwendet. Die neuen Word-Dokumente verwenden Times New Roman 11 pt und dezimale Gliederung. Screenshots, Tabellen und bestehende Originale behalten ihre unterschiedlichen Erscheinungsbilder.

## 3 Nachweise

`ursprungsbestand-445.35.4.json` enthält die vor der Überarbeitung erfassten SHA-256-Werte sämtlicher 338 Originaldateien. `scripts/test-compliance-hameln.py` vergleicht diese Originale byteweise mit dem Ausgangsbestand, liest beide ergänzenden Dokumente je Fall und prüft ihre vollständigen Texte in den tatsächlich gebauten PDF-Lesefassungen. Negative Proben weisen Textverlust und einen vertauschten Fall zurück.

Mit `--dist <Releaseverzeichnis>` prüft dasselbe Werkzeug sämtliche äußeren Prüfsummen, Archivmitglieder, PDF-Seitenzahlen, Originaldateien im ZIP und die Übereinstimmung der Gesamt-PDFs in Repo, Einzel-Download und Originalformat-ZIP. Die zentralen ZIP- und Hinweisprüfungen bleiben unverändert in Kraft. Die 35 bisherigen Nachbesprechungsblätter bleiben getrennt und werden nicht als neue Musterlösungen der ergänzenden Unterlagen ausgegeben.

Redaktionelle Quellen- und Verfahrensprüfung stehen im Profil `quality/evals/compliance-abteilung-grosskonzern.json`. Praktische Agentenproben werden gesondert dokumentiert; aus ihnen folgt kein angeblich erfolgreich ausgeführter Gesamtlauf aller 35 Fälle.
