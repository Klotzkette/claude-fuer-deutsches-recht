# 1. Betrieb und Prüfung

## 1.1. Ausführungsmodell

Die Anwendung benötigt Python ab Version 3.10, die Abhängigkeiten aus `app/requirements.txt` und einen Browser mit JavaScript. Sie bindet ausschließlich an `127.0.0.1`. Der Browser muss diesen lokalen Server erreichen können. Ein Plugin-Menü allein stellt weder einen Python-Prozess noch einen eingebetteten Browser bereit. Eine entfernte Arbeitsumgebung benötigt eine ausdrücklich freigegebene Vorschaufunktion; das Öffnen des Servers im öffentlichen Netz ist nicht vorgesehen.

Die mitgelieferten Skills begleiten Start und Dokumentenvorbereitung. Ein vollständiger Vorgang ist auch ohne Sprachmodell direkt in der Anwendung bearbeitbar. Es gibt keine API-Schlüssel, kein Modellabonnement und keinen externen Dokumentenversand durch den Programmcode.

Daneben steht ein Website-Export zur Verfügung. Das erzeugte ZIP enthält `index.html`, lokale Karten- und Dokumentenbibliotheken sowie eine Browserlaufzeit. Nach vollständigem Entpacken öffnet sich die Website per Doppelklick ohne Python. Die Dokumentvorlagen werden beim Verpacken aus denselben freigegebenen Vorlagen wie in der App übernommen; es gibt keinen externen Textgenerator. Browser und App erzeugen aus denselben Angaben inhaltlich gleiche Schreiben. Paritätstests vergleichen die HTML-Ausgaben beider Wege.

Das Website-ZIP enthält standardmäßig keine Vorgangsdaten. Eine ausdrückliche Auswahl kann den aktuellen Vorgang einschließen; dann sind die Angaben in `portable-bundle.js` für jeden Empfänger lesbar. Die Website öffnet solche Daten erst auf Anforderung. JSON bleibt der verlässliche Sicherungs- und Übertragungsweg, wenn ein Browser die lokale Speicherung für `file://` nicht dauerhaft unterstützt.

Die portable Website verwendet nur ausdrücklich unterstützte öffentliche Direktabrufe. Ein erreichbares Kartenbild ist keine erneute amtliche Quellenprüfung. Neue Katalog- und Zuständigkeitsrecherche erfordert die App mit Python-Laufzeit. Externe Dienste können direkte Browserabrufe blockieren oder ausfallen; vorhandene oder importierte Vorgänge und lokale Dokumentenerzeugung bleiben verfügbar. Keine Browser-Sicherheitsoption abschalten und keinen öffentlichen Ausweichproxy verwenden. Das ZIP enthält keine Offline-Kartenkacheln.

## 1.2. Datenquellen und Grenzen

Die Ortssuche liest die Verwaltungsgebiete VG250 des Bundesamts für Kartographie und Geodäsie. Der Gemeindeschlüssel kommt unverändert als achtstellige Zeichenkette aus dieser Quelle. Gemeindegrenzen und ihr Mittelpunkt sind generalisiert; sie ersetzen keine amtliche Grenzfeststellung und keinen Katasterauszug. Gleichnamige Gemeinden werden nach Bundesland und Kreis getrennt angeboten.

Anschließend erfolgen begrenzte Kataloganfragen an Geodatenkatalog.de. Kuratierte regionale Dienstadressen ergänzen diese Laufzeitsuche, ersetzen sie aber nicht. Ein Katalogausfall wird angezeigt. Gefundene Dienste werden weder durch ihren Namen noch durch eine erfolgreiche HTTP-Verbindung automatisch zu verwendbaren Quellen. Ein WMS muss zusätzlich ein gültiges Kartenbild am Ort liefern. Ein Flurstück-WFS muss sein Schema und zuordenbare reale Geometrien liefern.

Stand der Liveprüfung am 6. Oktober 2026:

| Ort | Geprüftes Ergebnis | Grenze |
| --- | --- | --- |
| Münster, NRW | Amtlicher Gemeindeschlüssel, Kreis, ABK, Luftbild, vereinfachter ALKIS-Flurstückdienst sowie Kataster- und Grundbuchkontakte. | Kein Eigentümernachweis; Interesse und Einreichungsweg bleiben gesondert zu prüfen. |
| Leipzig, Sachsen | Amtlicher Gemeindeschlüssel, Kreis, WebAtlas, Luftbild und bundesweite Basiskarte. | Der Flurstückabruf antwortete mit HTTP 400; deshalb keine Freigabe der Vektorauswahl. |
| Berlin | Amtlicher Gemeindeschlüssel, Kreis und bundesweite Basiskarte. | Der Flurstückdienst war nicht zuverlässig abrufbar; manuelle Erfassung oder Import bleibt erforderlich. |

Die zusätzliche Ortssuche wurde für Hannover und Freiburg im Breisgau geprüft. Das ist keine Zusage flächendeckender Katasterdaten. WMS und das vereinfachte ALKIS-WFS-Schema sind aktiv unterstützt. Andere Schemata, WMTS und OGC-API-Angebote werden nicht ungeprüft aktiviert. Nicht unterstützte Geometrien führen zu einer nachvollziehbaren Fehlermeldung. GeoJSON-Importe verlangen WGS84; GML muss sein Koordinatenreferenzsystem eindeutig bezeichnen. Manuelle Importe werden nicht zu amtlich bestätigten Flurstücken erklärt.

Der landesweite NRW-Dienst nennt bei der Prüfung die Datenlizenz Deutschland Zero 2.0. Die unveränderte ältere Münster-Referenz kann einen anderen Lizenzstand nennen. Maßgeblich für neue Abrufe sind die aktuellen Dienstmetadaten. Quellenangaben bleiben in den Exporten erhalten.

## 1.3. Begrenzungen und Sicherheit

Ausgehende Abrufe sind auf die Hostnamen und Pfade in `app/catalogs.json` begrenzt. DNS-Ergebnisse werden auf öffentliche Adressen geprüft; die geprüfte Adresse wird für die TLS-Verbindung festgehalten. Jede Weiterleitung wird erneut geprüft. Zugangsdaten in URLs, lokale Netze und ein frei verwendbarer URL-Proxy sind ausgeschlossen. Neue Katalogtreffer erweitern die Freigabeliste nicht selbstständig.

Der Transport begrenzt Zeit, Antwortgröße, parallele Abrufe und Cachegröße. Die Quellenrecherche hat ein eigenes Zeitbudget. Kartenbewegungen lösen verzögerte Abrufe aus; überholte Browserantworten werden verworfen. Eine Flurstückseite enthält höchstens 400 Datensätze, ein Ausschnitt höchstens fünf Seiten. Unvollständige Ergebnisse werden angezeigt. Die gespeicherte Auswahl bleibt von neu geladenen Kartenflächen getrennt.

JSON-Importe sind auf 2 MiB und 200 ausgewählte Flurstücke begrenzt. Geometrien haben zusätzliche Punkt- und Größenbudgets. XML-Entitäten und externe XML-Referenzen sind gesperrt. Externe Texte werden nicht als Anweisungen ausgeführt und in Dokumenten maskiert. Die Weboberfläche schützt lokale Schreibanfragen mit Sitzungstoken, Host- und Herkunftsprüfung.

Ortsnamen, Adresssuchen und Kartenausschnitte werden an die benannten öffentlichen Dienste übertragen. Absender, Interessenbegründung, Kontaktangaben und Dokumententexte verlassen den lokalen Prozess dabei nicht. Eine lokale Speicherung erfolgt ausdrücklich im Browserprofil; auf gemeinsam genutzten Geräten sollte sie anschließend gelöscht werden. JSON und ZIP enthalten die eingegebenen Vorgangsangaben und sind entsprechend aufzubewahren.

## 1.4. Reproduzierbare Prüfungen

Führen Sie nach Installation der Python-Abhängigkeiten im Repository aus:

```sh
python3 -m unittest discover -s grundstuecksrecherche/tests -v
python3 scripts/test-app-only-integration.py
node scripts/validate-plugin-structure.mjs
node scripts/validate-marketplace-import.mjs
python3 scripts/validate-yaml-frontmatter.py
```

Die Browserprüfung benötigt Playwright und dessen Chromium-Installation. `PLAYWRIGHT_MODULE` kann auf das installierte `playwright/index.mjs` zeigen; `PLAYWRIGHT_CHANNEL=chromium` wählt den mitgelieferten Browser. Ohne `--live` verwendet sie kontrollierte Dienstantworten und prüft auch Fehlerfälle. Mit `--live` verwendet sie den laufenden Server auf `UI_BASE_URL`, standardmäßig `http://127.0.0.1:8765`.

```sh
node grundstuecksrecherche/tests/test-ui.mjs
node grundstuecksrecherche/tests/test-ui.mjs --live
node grundstuecksrecherche/tests/test-portable-documents.mjs
node grundstuecksrecherche/tests/test-portable-runtime.mjs
node grundstuecksrecherche/tests/test-website-file.mjs
RUN_LIVE_DISCOVERY=1 python3 -m unittest discover -s grundstuecksrecherche/tests -p test_discovery.py -v
```

Die Prüfsumme jeder Datei der ursprünglichen Münster-Referenz wird separat kontrolliert. Diese Referenz bleibt unverändert. Sie ist kein Trainingsfall und kein vorausgefüllter Vorgang der neuen App. Ein Live-Test in einer anderen Plugin-Oberfläche wird durch diese technischen Prüfungen nicht ersetzt.
