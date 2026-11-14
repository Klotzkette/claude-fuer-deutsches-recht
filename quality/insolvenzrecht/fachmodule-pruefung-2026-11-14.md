# Insolvenzrecht: Prüfung der integrierten Fachmodule

## 1. Umfang und Herkunft

Das Hauptplugin `insolvenzrecht` enthält die Facharbeit aus `fachanwalt-insolvenz-sanierungsrecht`, `insolvenzverwaltung`, `insolvenzsachbearbeitung` und `insolvenzverwaltung-berichtsersteller` als paketlokale Referenzen. Die bisherigen 99 auswählbaren Hauptplugin-Skills bleiben erhalten. Es werden weder weitere `SKILL.md`-Dateien noch zusätzliche Plugin-Manifeste in den Fachmodulen angelegt. Die Einzelausgaben bleiben als kompatible Quellen bestehen.

Die explizite Registry `scripts/data/insolvenzrecht-fachmodule.json` ordnet alle 159 Quellskills einer fachlichen Produktgruppe und einem Auswahlgrund zu. Der gezielte Builder `scripts/build-insolvenzrecht-fachmodule.py` erzeugt 308 Dateien unter `insolvenzrecht/references/fachmodule/`. Die `SOURCE_MAP.json` enthält 302 Quelldateizuordnungen einschließlich gemeinsamer Quellenregeln, Quellhashes, Übernahmeart, Ziel und Hash der erzeugten Datei. Der aktuelle gemeinsame Hauptworkflow ist zusätzlich durch einen eigenen SHA-256 gebunden. Die Registry und die tatsächlich erzeugten Paketdateien sind ebenfalls über Hashes nachprüfbar.

## 2. Auswahl und Bewahrung der Materialien

Vier Modulindizes erschließen anwaltliche Mandatsarbeit, Verwaltung, Sachbearbeitung sowie Berichte und Rechnungslegung. Darunter stehen konkrete Produktgruppen mit Anlass, Arbeitsprodukt und passenden Fachreferenzen. Die Anweisung ist, eine führende Referenz zu laden und weitere Texte nur für eine benannte offene Frage hinzuzunehmen. Die Normbibliothek bleibt mit ihrem vorhandenen gezielten Bereichsindex erhalten.

17 bisherige Intake- und Steuerungsskills sind ausdrücklich der bestehenden Hauptroute `skills/einstieg-routing/SKILL.md` zugeordnet. Besondere Kontext-, Produktkennungs- und Übergaberegeln bleiben nachschlagbar, starten aber keinen zweiten Intake. Drei frühere Chat-Kurzbefehle führen ebenfalls zur gemeinsamen Hauptroute. Die Vorschauseite des alten Verwaltungspakets bleibt als dokumentierter externer Verweis erhalten; sie wird nicht als benötigtes Arbeitsmaterial kopiert.

34 vollständige Arbeitsvorlagen sind paketlokal enthalten: 25 aus der Verwaltung und neun aus dem Berichtsersteller. Es handelt sich um 32 Markdown-Dateien und zwei CSV-Dateien. 22 weitere Planvorlagen sind nachweislich byteidentisch mit den Vorlagen der eigenständigen Insolvenzplan- und StaRUG-Planwerkstatt. Sie werden nicht nochmals verteilt; SourceMap und Prüfung binden die jeweilige kanonische Datei und ihren Hash. Die 33 zugehörigen Plan-Fachtexte bleiben nur als Kontext für die Übergabe erhalten. Die vollständige Planarbeit ist weiterhin dem eigenständigen Spezialplugin zugewiesen.

Gemeinsame Quellenregeln werden bei nachgewiesener Byteidentität auf eine lokale Datei zusammengeführt. Ein bestehender Dateinamensfehler (`vorläufige-verwaltung-checkliste.md` statt der tatsächlich vorhandenen Datei `vorlaeufige-verwaltung-checkliste.md`) ist als ausdrücklicher Linkalias in der Registry und als Korrektur in der SourceMap dokumentiert.

## 3. Technische Prüfungen

Die gezielte Prüfung erfolgt mit:

```text
python3 scripts/build-insolvenzrecht-fachmodule.py --check
python3 scripts/test-insolvenzrecht-fachmodule.py
python3 scripts/test-insolvenzrecht-fachmodule.py --dist <Release-Verzeichnis>
```

Die Tests prüfen vollständige Quellabdeckung, stabile Zuordnungen, die 22 getrennten identischen Planvorlagen, die 34 lokalen Arbeitsvorlagen, unverändert 99 Runtime-Skills, deterministische Erzeugung und bytegenaue Übereinstimmung des erzeugten Bestands. Ein allein entpacktes Hauptplugin wird ohne Repository-Geschwister auf auflösbare lokale Markdown-Verweise und ausdrücklich genannte Vorlagenpfade geprüft. Der optionale `--dist`-Lauf prüft zusätzlich das tatsächlich gebaute `insolvenzrecht.zip`.

Negativprüfungen zeigen, dass geänderte Fachquellen, ein veränderter Hauptworkflow, eine nicht zugeordnete neue Quelle, fehlende lokale Dateien und aus dem Paket herausführende lokale Verweise erkannt werden. Veraltete Dateien werden nicht durch manuell angepasste Hashes akzeptiert. Der Builder entfernt keine unerwarteten Altdateien stillschweigend.

Der lokale Lauf umfasst zehn Tests. Ohne `--dist` wird ausschließlich der zusätzliche Test eines extern gebauten Release-Archivs übersprungen; der unabhängige temporäre Pakettest läuft bereits dabei. Die endgültige Releaseprüfung muss das tatsächlich gebaute Archiv mit `--dist` einbeziehen.

## 4. Aussagegrenzen

Geprüft wurden Auswahlzuordnung, Vollständigkeit, Quellenherkunft, reproduzierbarer Bau und lokale Verwendbarkeit des Paketinhalts. Eine interaktive Funktionsprobe in Claude Cowork, ChatGPT oder einer anderen Oberfläche wurde nicht durchgeführt. Die Integration ist keine erneute vollständige Live-Prüfung sämtlicher übernommenen Norm- und Rechtsprechungsaussagen. Die im Rahmen der Integration gezielt korrigierte Fachanwalt-Orientierung wird als aktueller Quellstand übernommen; weitergehende rechtliche Verifikation richtet sich nach dem konkreten Auftrag und den Quellenregeln des Hauptplugins. Dieser Vermerk bestätigt weder eine Veröffentlichung noch die tatsächliche Ausführung einer Außenhandlung.
