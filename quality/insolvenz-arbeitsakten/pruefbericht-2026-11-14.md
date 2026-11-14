# 1 Prüfbericht Insolvenz-Arbeitsakten 1.0.0

Prüfdatum: 14. November 2026. Umfang: drei Insolvenzreifeakten, Weserfunken, vier weitere Anfechtungsakten und die Hamburger Backstube. Kein Anspruch auf eine neue fachliche Freigabe sämtlicher Testakten oder Rechtsprechungsanker des Repositorys.

## 1.1 Originale und Trennung

Der tatsächlich erzeugte Bestand steht in `v1.0.0-bestand.json`. Die neun Original-ZIPs enthalten 532 Arbeitsdateien, davon 440 unter `Grundakte`. Die drei Insolvenzreife-Grundakten umfassen 298 Dateien. Verfahren, Lösungen und Gesamt-PDFs werden nicht in die Grundakte aufgenommen. Vorlagen und das gesonderte Vergleichsmaterial bleiben entsprechend der bestehenden Exportregeln getrennt.

Die ursprünglichen Bankbuchungen und Kontrollrechnungen bleiben unverändert. Die ergänzten Verträge konkretisieren die vorhandenen Finanzierungen; das Rotor-Darlehen und die bereits gezogene Linie ergeben gemeinsam 620.000 EUR. Die Hamburger Rechnungen ergeben 34.545,22 EUR, die Zahlungen 13.012,75 EUR und die geltend gemachte Hauptforderung 21.532,47 EUR. 274 Ereigniszeilen dienen dem eigenständigen Abgleich der Zuordnungen; eine fertige korrigierte Forderungsabrechnung wird nicht beigelegt.

## 1.2 Satz und Belegtreue

Weserfunken: 18 Seiten Klage und 14 Seiten Erwiderung bei erhaltener Argumentation. Die Migration dokumentiert 97 Klage- und 80 Erwiderungsabsätze; 37 von 42 geschützten historischen Originalen bleiben bytegleich. Fünf weitere Word-Schreiben und Schriftsätze erhalten Kanzleibriefköpfe, Anschrift, Aktenbezug, Anträge und dezimale Überschriften. Die E-Mail mit Klageanlage enthält die neu erzeugte Word-Datei bytegleich.

Die fünf ergänzend gesetzten Word-Dokumente wurden vollständig gerendert und auf allen zwölf Seiten visuell geprüft. Die 40 Vertrags-PDFs mit 78 Seiten, die geänderten Weser-Dokumente und die Hamburger Original-PDFs und Word-Dateien wurden durch die zuständigen Bearbeiter gerendert und gesichtet. Tabellen und Portalansichten sind gesondert geprüft. Times New Roman stammt aus den rechtmäßig auf diesem Rechner vorhandenen Systemschriften. Keine Schrift wurde umbenannt und kein Fontguard abgeschaltet.

Die bestehenden Vergleichsgutachten und Word-Vorlagen der fünf betroffenen Anfechtungsakten wurden fachlich mit den neuen Satzfassungen abgeglichen. Es ändern sich nur fünf nach tatsächlicher Inspektion erzeugte Aktenstand-Hashes. Material- und Quellenhashes bleiben unverändert; Einzelheiten im gesonderten Vergleichsmaterial-Prüfvermerk.

## 1.3 Tatsächlich ausgeführte Prüfungen

- Drei Releaseprüfungen einschließlich Quellabgleich und zwei Manipulationsproben: eine falsche Seite bei unveränderter Gesamtseitenzahl sowie eine byteveränderte Original-PDF unter dem Grundakte-Präfix werden abgewiesen.
- Weser: 14 Bestands-/Pakettests, fünf Ergänzungstests, sieben Satztests; außerdem sechs echte Tests im CI-Modus ohne Neugenerierung.
- Fünf Vertragsaktentests, fünf Grundaktentests und zwölf Anfechtungs-/Exporttests für die Insolvenzreifeakten. Der exportabhängige Test wurde mit dem tatsächlichen Releaseverzeichnis ausgeführt.
- 26 Rechner- und Falltests; sechs Hamburger Falltests; zwei Kanzleisatztests, die auch den vorherigen Briefkopfzustand als unzureichend erkennen.
- Neun Prüfungen für Insolvenzanfechtung; eine dortige Prüfung des gesonderten alten Plugin-Komponentenreleases ist im lokalen Lauf ohne dessen Dist-Verzeichnis ausgenommen. Das neue Aktenrelease wird durch seinen eigenen vollständigen Prüfer geprüft.
- 30 Akten und 70 Vergleichsmaterialdateien über den bestehenden Materialprüfer.
- Marketplace, YAML, Pluginstruktur, Gesamt-PDFs, Downloadhinweise, zentrale Übersicht, Release-Routen und Quellenrelease-Kandidaten geprüft.
- Qualitätsaudit mit Editorial- und Workflow-Anforderung: strukturell bestanden. Bereits vorhandene, nicht freigegebene Ergebnisstände bei anwaltschaft-generell, corporate-contract-law, gesellschafterstreit und wirtschaftsanwalt bleiben als needs_review erhalten; keine Ergebnisfreigabe dieser fachfremden Bereiche.

## 1.4 Paketprüfung und Veröffentlichung

Genau 32 Release-Dateien: neun Original-ZIPs, neun Einzel-PDF-ZIPs, neun Gesamt-PDFs, drei Sammelpakete, Inventar und Prüfsummenverzeichnis. Jede Original-PDF bleibt auch nach Verschiebung unter Grundakte bytegleich zur entsprechenden Einzel-PDF. Die Seitenfolge und der normalisierte Text der Gesamt-PDFs werden mit allen Einzel-PDFs abgeglichen; Weserfunken besitzt zusätzlich drei Registerseiten.

Die Sammelpakete werden byteweise mit ihren Einzelakten abgeglichen. Der reine Grundakten-Download enthält ausschließlich die 298 ausgewählten Dateien sowie README.txt. Alle ZIPs enthalten den vorgeschriebenen deutschen und englischen Hinweis; keine PDF enthält den Warntext. Der Builder verifiziert SHA-256 und tatsächlichen Inhalt. Der öffentliche Download ist nach dem Hochladen separat erneut mit `--verify --offline` zu prüfen; dieser Bericht allein behauptet noch keine Veröffentlichung.
