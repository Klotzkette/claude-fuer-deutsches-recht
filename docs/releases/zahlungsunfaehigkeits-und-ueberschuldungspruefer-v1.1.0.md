# Zahlungsunfähigkeits- und Überschuldungsprüfer 1.1.0

Elf Skills, Werkstatt-Prompt und Mini-Prompt führen von den übergebenen Geschäftsunterlagen zur getrennten Prüfung nach §§ 17 und 19 InsO. Die Überarbeitung berücksichtigt amtlich geprüfte BGH-Entscheidungen aus 2026 zur Zahlungseinstellung, zur Realisierbarkeit von Gesellschafterforderungen und zur historischen Vermögensbewertung. Quellen, Aussagegrenzen und Prüfstand stehen im [Quellenverzeichnis](../../zahlungsunfaehigkeits-und-ueberschuldungspruefer/references/insolvenzreife-quellen.md).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

Die drei Unternehmen aus Cottbus, Berlin-Zehlendorf und Prenzlau sind mit weiteren Rechnungen, betrieblichen Belegen, Finanzierungs- und Vermögensunterlagen sowie Korrespondenz ausgearbeitet. Das Originalformat-ZIP jeder Akte enthält die Eingangsunterlagen in `Grundakte` und den Verfahrensbestand gesondert in `10_Verfahren`. Gesamt-PDF und Einzel-PDF-ZIP dienen der vollständigen Durchsicht. Das zusätzliche `Insolvenzreife_Drei_Grundakten.zip` enthält ausschließlich die drei Grundakten. Die Stichtagskontrolle für die Nachbesprechung bleibt ein eigenes Archiv.

Der lokale Rechner verarbeitet aufbereitete und belegte Eingaben. Ein rechnerischer Befund ersetzt weder die Vollständigkeitsprüfung der Originalunterlagen noch die rechtliche Würdigung von Zahlungseinstellung, Fortbestehensprognose oder Kenntnis eines Anfechtungsgegners. Die Funktionsprüfung umfasst Rechenfälle und Regressionen. Sie behauptet keine Live-Ausführung des Plugins in ChatGPT oder Claude.

Die Grundakten enthalten zusammen 216 Originaldateien. Mit den 15 getrennten Verfahrensdokumenten umfassen die vollständigen Akten 231 Originaldateien. Die dokumentweise zusammengestellten Gesamt-PDFs umfassen 711 Seiten (Cottbus 240, Berlin 233, Prenzlau 238). Alle 72 Monatsauszüge und 822 Bankbewegungen bleiben erhalten. Bei der Berliner Halle behandelt die Nachbesprechung ausdrücklich die mögliche frühere objektive Wertminderung trotz späterer Erkenntnis.

Geprüft wurden 26 Rechen- und Falltests, fünf Belegkettenprüfungen sowie die Browserausführung der 18 Kontrollstichtage. Die Paketprüfung vergleicht Originale und Mailanlagen, kontrolliert die Grundaktenauswahl und prüft die heruntergeladenen Release-Dateien gegen ihre Prüfsummen.

Für den reproduzierbaren Aktenbau verwendet `scripts/build-insolvenzreife-akten.py` vier echte Times-New-Roman-TTFs. Falls sie nicht in den unterstützten Systemverzeichnissen liegen, setzt `INSOLVENZREIFE_FONT_DIR` das Schriftverzeichnis. Ohne Regular, Bold, Italic und Bold Italic bricht der Aktenbau ab. Der Release-Builder nutzt die gespeicherten Original-PDFs und benötigt dafür keinen erneuten Schriftaufbau. Bank- und Rechnungslayouts verwenden ihre eigenen Hausschriften.
