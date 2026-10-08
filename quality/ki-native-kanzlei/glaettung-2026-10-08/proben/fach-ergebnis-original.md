Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

# 1. Ergebnis des unabhängigen Fachprobelaufs

Die beiden bestellten Fachprodukte sind auf Grundlage der übermittelten Tatsachen vollständig formuliert. Es wurden keine Repository-Dateien geändert, keine quality-Dateien, fremden Resultate oder Git-Diffs gelesen. Es fand keine Außenhandlung statt. Die Ergebnisse sind Entwürfe, keine menschlich freigegebenen Fassungen.

## 1.1. Fall 1

Der [Prüfvermerk](Fall1/01_Bearbeitung/Pruefvermerk.md) trennt Herausgabeanspruch, Mandatsübergang, Empfangsbefugnis, Geheimnisschutz, Cloudrollen, Datenschutz und Zurückbehaltung. Das [Antwortschreiben](Fall1/01_Bearbeitung/Antwortschreiben.md) ist ausformuliert. Die Akte wird nicht übertragen. Die tatsächlich fehlenden Unterlagen und sichere Alternativen sind benannt; die offene Honorarnote ersetzt keine Prüfung der Unangemessenheit einer Zurückbehaltung.

Im [Mandatslauf](Fall1/00_Mandat/mandatslauf.json) steht Stufe 2, Phase sacharbeit und Nebenlauf kommunikation. G1, G3 und G6 sind offen und an Produkte mit Hash gebunden. Verantwortlich ist RAin Ada Ahrens. Die übrigen Gates sind mit Grund als derzeit nicht erforderlich dokumentiert. Dies bestätigt keine Kalenderprüfung oder Mandatsbeendigung. Der [nächste Schritt](Fall1/00_Mandat/naechster_schritt.txt) verweist tatsächlich auf den Berufsrechtsskill, das Produkt berufsrechtsvermerk und RAin Ahrens.

## 1.2. Fall 2

Der [Prüfvermerk](Fall2/01_Bearbeitung/Pruefvermerk.md) prüft den begrenzten Anwendungsbereich und die Monatsklausel anhand der gelesenen amtlichen BGH-Entscheidungen IX ZR 226/22 und IX ZR 227/22 vom 19.02.2026. Der neue Lizenzvertragsentwurf fällt nach den gegebenen Tatsachen nicht unter die bisherige Honorargrundlage. Die Anerkenntnisfiktion ist bei AGB-Verwendung auch gegenüber der GmbH unwirksam; die übrige Abrede bleibt grundsätzlich erhalten.

Die [Honorarergänzung](Fall2/01_Bearbeitung/Honorarergaenzung.md) enthält vollständige Regelungen zu Umfang, 260 EUR netto je tatsächlicher Stunde, minutengenauer Abrechnung, Auslagen, Kostenerstattung und Annahme in Textform. Sie beginnt erst nach Annahme und erweitert den alten Auftrag nicht rückwirkend. Fehlende Parteien- und Gegenstandsdaten sind als Platzhalter sichtbar.

Im [Mandatslauf](Fall2/00_Mandat/mandatslauf.json) steht Stufe 2, Phase sacharbeit und Nebenlauf abrechnung. G1 und G3 sind offen, verantwortlich ist RA Bertram Brecht. Der [nächste Schritt](Fall2/00_Mandat/naechster_schritt.txt) verweist tatsächlich auf honorar-budget-vereinbaren, honorarstand und RA Brecht. Eine Parteienannahme oder anwaltliche Freigabe wurde nicht fingiert.

## 1.3. Honorar, Zeiten und Helferausführung

Je Fall wurde mit kanzlei.py ein echtes lokales Mandatsjournal angelegt und ein Rechnungsentwurf erzeugt. Es erfolgten keine terms-, time-, manual-fee- oder payment-Buchungen: Die alte Honorargrundlage betrifft nur die beschriebene Forderungsabwehr, die neue Vereinbarung ist offen, und tatsächliche anwaltliche Dauer und Abrechenbarkeit fehlen. Auch der steuerliche Sachverhalt ist nicht bestätigt. Diese offenen Angaben sind in den Prüfvermerken und Lauf-Fragen dokumentiert.

Beobachtung zur erzeugten Honoraransicht: kanzlei.py zeigt bei leerem Journal einen bekannten Teilbetrag von 0,00 EUR und 19 Prozent Umsatzsteuer an, obwohl keine Honorarposition eingegeben wurde. Der Helfer nennt zugleich „Honorargrundlage fehlt“ und schließt einen vollständigen Rechnungsstand aus. Diese Nullanzeige ist keine festgestellte Gesamtforderung, kein bestätigter Steuersatz des Mandats und keine Aussage über tatsächliche Minuten.

Es wurden 46 Helferaufrufe erfolgreich ausgeführt: mandatslauf.py init zweimal, phase viermal, product viermal, gate sechzehnmal, question zehnmal, status zweimal und next zweimal; kanzlei.py init, draft und status jeweils zweimal. Exakte Argumentlisten, Rückgabecodes und Ausgaben stehen in [helferaufrufe.json](helferaufrufe.json). Das aufgerufene interne Steuerungsskript steht in [lauf_ausfuehren.py](lauf_ausfuehren.py); es ist wegen geschützter Initialisierung nicht als erneut ausführbare Fortsetzung gedacht.

## 1.4. Form und Quellenstand

Die Arbeitsprodukte sind Markdown-Dateien; es wurden keine DOCX- oder PDF-Dateien und keine tatsächliche Schriftformatierung erzeugt. Für einen späteren Export gelten Times New Roman, 11 pt und dezimale Gliederung. Empfängertexte enthalten keine technischen Abrufprotokolle; diese stehen in den getrennten Prüfvermerken.

Die BGH-Rohtexte wurden selbst gelesen. IX ZR 227/22 war beim direkten Webabruf mit HTTP 403 blockiert; der zugelassene amtliche Rohcache wurde daraufhin verwendet. Weitere fehlgeschlagene Normabrufe wurden durch den amtlichen Rohcache oder direkten Serverabruf ersetzt und im Quellenvermerk eingegrenzt. Es wurde keine spätere Rechtsprechung als geprüft behauptet.
