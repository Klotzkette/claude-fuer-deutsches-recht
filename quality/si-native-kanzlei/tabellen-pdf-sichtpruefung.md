# 1. Sichtprüfung der 24 Excel-Druckansichten

Prüfdatum: 7. Oktober 2026. Alle 24 endgültigen Arbeitsmappen `08_Zeiten_und_Honorar.xlsx` wurden mit LibreOffice Calc nativ als PDF exportiert und anschließend als vollständige, einzeln angezeigte PNG-Seiten visuell geprüft. Jede Druckansicht umfasst genau eine A4-Querformatseite. Kein Text ist abgeschnitten oder überlagert; die Eingabefelder, vier Zeitzeilen, Zwischenergebnisse und erklärenden Hinweise bleiben lesbar.

## 1.1. Umfang und Beleg

Die Eingangskopien stammen aus den aktuellen Repository-Dateien. Der nach Abschluss durchgeführte SHA-256-Abgleich bestätigt für alle 24 Arbeitsmappen die Identität mit den gerenderten Quellen. Die [maschinelle Prüfliste](tabellen-pdf-sichtpruefung.json) enthält Quellen- und PDF-Hashes, Seitenzahl, Seitengröße und den Sichtstatus jeder Datei. Temporäre Renderbelege liegen unter `/tmp/si-native-kanzlei-20261007/tabellen/pdf-sichtpruefung-final`.

Geprüft wurden Titel und Aktenzuordnung, Honorarart und Vereinbarungsstatus, editierbare Felder, Datums-/Personenspalten, Tätigkeitstext, Minuten, Abrechenbarkeit, Bestätigung, Zeitwert, Quellenhinweise, Ergebnisbereich sowie Erläuterungen zu Festpreis, Schätzung, Deckel und noch ungeklärtem RVG-Honorar. Die fehlende Dauer der dritten Zeile bleibt sichtbar offen; die vierte Zeile ist nicht als bereits abrechenbar dargestellt. Die Sichtprüfung bezieht sich auf die native Calc-Druckansicht, nicht auf die Oberfläche von Microsoft Excel. Die gesonderten Rechen- und Mutationstests werden hier nicht als Sichtprüfung ausgegeben.

## 1.2. Behobener Befund

Im ersten Durchlauf standen rechtsbündige Minuten-/Geldwerte unmittelbar am linksbündigen Text der nächsten Spalte. Die Tabellen wurden im Erzeuger nachgebessert: Datum sowie Minuten, Ja/Nein-Status, Wert und Quelle sind nun zentriert. Alle 24 endgültigen Dateien wurden danach erneut exportiert und vollständig visuell geprüft. Die Abstände sind jetzt klar erkennbar; es verblieb kein Layoutbefund.

## 1.3. Ergebnis nach Akte

| Akte | Seiten | Sichtprüfung |
|---|---:|---|
| si-kanzlei-agrarrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-arbeitsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-bank-kapitalmarktrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-bau-architektenrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-erbrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-familienrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-gewerblicher-rechtsschutz | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-handels-gesellschaftsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-insolvenz-sanierungsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-internationales-wirtschaftsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-it-recht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-medizinrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-miet-wohnungseigentumsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-migrationsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-sozialrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-sportrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-steuerrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-strafrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-transport-speditionsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-urheber-medienrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-vergaberecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-verkehrsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-versicherungsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
| si-kanzlei-verwaltungsrecht | 1 | Vollständig angesehen; kein verbleibender Layoutbefund. |
