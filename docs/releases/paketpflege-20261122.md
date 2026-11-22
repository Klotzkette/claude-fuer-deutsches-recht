# Plugin-Pakete mit aktuellen Anleitungen

Die Plugin-ZIPs dieser Ausgabe enthalten die überarbeiteten README-Dateien und die zum jeweiligen Paket gehörenden Downloadziele der interaktiven Vorschauen. Die Dateinamen und Fachpaketversionen bleiben für die Installation gleich. Jeder dieser vier GitHub-Releases enthält die Pakete seiner Version sowie einen Bestandsnachweis und SHA-256-Prüfsummen.

| Version im Plugin-Manifest | Native ZIPs | Portable ZIPs |
| --- | ---: | ---: |
| 445.36.9 | 308 | 27 |
| 445.36.10 | 2 | 0 |
| 445.36.11 | 2 | 0 |
| 1.0.0 | 1 | 0 |

Die Ausgabe umfasst die von der Dokumentationspflege betroffenen Pakete. Die bereits aktuellen ZIPs für Aktenanleger und Umwandlungssteuerrecht stehen weiter im Fachaufnahme-Release. Das Notariatspaket führt vom Installationsarchiv zur Kursmappe und zur aktuellen Neuralis-Akte. Der [Ausgabeplan](../../scripts/data/paketpflege-20261122.json) bezeichnet die Vorgängerausgaben und die vorgesehene Aufteilung. Die öffentlichen Verweise im [Download-Index](../../ASSET_INDEX.md) wechseln erst, wenn alle vier Nachauflagen bereitstehen.

Der Workflow [Paketpflege](../../.github/workflows/paketpflege.yml) baut jede Gruppe aus dem freigegebenen Commit. Er vergleicht Namen und Inhalt aller Archivmitglieder mit dem Checkout, kontrolliert die Paket-Manifeste und lädt die bereitgestellten ZIPs zur Gegenprüfung vollständig zurück. Der Bestandsnachweis im Release enthält den Quellcommit sowie die Prüfsummen der mitgelieferten Dateien. Die früheren Komponenten- und Sammelausgaben bleiben unter ihren ursprünglichen Tags abrufbar.
