# Insolvenzrecht 445.35.4

## 1. Gemeinsamer Einstieg

Der Oberordner [Insolvenzrecht](../../insolvenzrecht-plugins/README.md) ordnet die Insolvenzarbeit in vier Haupteinstiege: das gemeinsame Hauptplugin, den Forderungsanmelder, den Zahlungsunfähigkeits- und Überschuldungsprüfer sowie die Insolvenzplan- und StaRUG-Planwerkstatt. Weitere Spezialangebote stehen darunter. Die bisherigen allgemeinen Einzelpakete bleiben für bestehende Installationen erreichbar.

Das Hauptplugin verbindet anwaltliche Mandatsführung, Insolvenzverwaltung, operative Sachbearbeitung und Berichte. Ein gemeinsamer Arbeitsstand hält Rolle, Verfahren, Auftrag, Belege, Fristen und Entwurf zusammen. Der passende Fachtext wird erst für die konkrete Aufgabe geladen. Forderungsanmeldung, vertiefte Insolvenzreifeprüfung und Planerstellung können mit diesem Arbeitsstand an die eigenständigen Werkzeuge übergeben werden.

## 2. Vollständigkeit und Abgrenzung

Die 159 Quellskills aus den vier allgemeinen Einzelausgaben werden über ausdrücklich zugeordnete lokale Fachmodule erschlossen. Die vorhandenen 99 auswählbaren Skills des Hauptplugins bleiben erhalten. Die Module enthalten die zugehörigen Arbeitsvorlagen und Referenzen; eine zusätzliche Installation der vier Einzelausgaben ist nicht nötig. Die 22 byteidentischen Planvorlagen bleiben bei der eigenständigen Planwerkstatt.

Die Registry und die erzeugte `SOURCE_MAP.json` halten Quelle, Ziel, Zuordnungsgrund und SHA-256 fest. Die Driftprüfung verhindert, dass später veränderte Quellen unbemerkt neben veralteten Paketkopien stehen. Eingebundene alte Intake-Routen führen zum gemeinsamen Einstieg; sie beginnen keine zweite Aufnahme.

Werkstatt-, Mini- und Schwerpunktprompt sind separate Markdown-Downloads. Sie sind nicht Bestandteil des installierbaren ZIP. Bestehende Testakten, deren Veröffentlichungen und alle bisherigen Tags bleiben unverändert.

## 3. Gezielte fachliche Korrekturen

Der frühere fachanwaltliche Orientierungstext wird an konkret erkannten Stellen berichtigt, unter anderem zu Insolvenzgericht, Beschwerde, Antrags- und Anfechtungsfristen, Schutzschirm, Insolvenzgeld und Fachanwaltsanforderungen. Die amtlichen Quellen und Aussagegrenzen stehen im [Prüfvermerk](../../quality/insolvenzrecht/konsolidierung-pruefvermerk-2026-11-14.md). Diese Organisationsänderung ist keine erneute rechtliche Vollprüfung sämtlicher importierter Fachtexte.

## 4. Paket und Prüfung

Das Release enthält genau sechs Dateien: `insolvenzrecht.zip`, drei eigenständige Markdown-Prompts, `quellenabgleich.json` und `checksums-sha256.txt`. Das Quelleninventar erfasst jede Datei des Plugins mit Größe und Prüfsumme. Der Paketprüfer gleicht die tatsächlichen ZIP-Inhalte byteweise mit dem Checkout ab; neu berechnete Prüfsummen allein lassen ein veraltetes Paket nicht bestehen.

Die automatisierte Prüfung umfasst Quellzuordnung, lokale Modulverweise, getrennte Spezialwerkzeuge, reproduzierbaren Paketbau, manipulierte Releaseinhalte, Navigation, Skillstruktur, Laufzeitbudgets, Qualitätsprofile und Versionsrouting. Der Veröffentlichungsworkflow prüft den freien Tag, lädt alle Assets vor der Veröffentlichung erneut herunter und wiederholt den Downloadvergleich danach. Diese Prüfungen belegen Paketinhalt und Anweisungsintegration; sie ersetzen keinen Live-Anwendungstest in jeder KI-Oberfläche.
