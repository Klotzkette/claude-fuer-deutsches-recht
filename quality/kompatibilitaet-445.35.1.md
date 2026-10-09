# 1. Kompatibilitätsreparatur 445.35.1

Prüfstand: 9. Oktober 2026. Gegenstand sind die vier Befundklassen des Import- und Paketabgleichs. Die fachlichen Skills, Prompttexte und Testakten werden nicht pauschal überarbeitet. Die zwischenzeitlich auf main veröffentlichte Fachrunde aus PR 559 wurde vollständig übernommen; ihr Bestand wird mitgeprüft.

## 1.1. Reparaturen

| Befund | Änderung | Nachweis |
| --- | --- | --- |
| Grundstücksrecherche ohne erreichbare Plugin- und Website-Downloads | Beide Archive erhalten einen expliziten Komponententag; Startskill, README und Indizes verwenden dieselben Ziele. | Paketbau prüft Einstieg, Quelldateien und leeren Vorgang im Website-ZIP. |
| Fremdes Anzeigefeld in zwei Bauvergabe-Manifesten | Anzeigemetadaten bleiben nur im dafür vorgesehenen alternativen Manifest. | Strikte Herstellerprüfung und negativer Regressionstest. |
| Sechs Plugin-ZIPs mit älteren Skill-Fassungen | Neue Paketversionen; Bytevergleich aller Skill-Dateien und vollständiger Quellenabgleich der neun Reparaturpakete. | Paketprüfer verwirft auch abweichende Inhalte bei unveränderter Versionsnummer. |
| Fehlende Qualitätsprofile und starres Katalogbudget | Individuelle Profile für AGB-Werkstatt und Kanzlei-Website-Redaktion; jeweils drei Fälle mit neun Ergebniskriterien. Kataloggrenze wächst mit der Pluginzahl. | Profil-, Start-, Fortsetzungs- und Budgettests. |

## 1.2. Technische Prüfungen

- Marketplace und Plugin-Manifeste werden mit Prüfprogrammversion 2.1.168 strikt geprüft; nach Integration umfasst der Katalog 296 Plugins.
- Struktur, Marketplace-Import und YAML-Frontmatter: bestanden; 23238 Skills, keine Frontmatter-Fehler oder Warnungen.
- Qualitätskatalog: 296 vollständige Einzelprofile einschließlich redaktioneller und Workflow-Prüfung. Das ist noch kein bestandener Modelllauf.
- Neue Paketregressionen: neun Tests bestanden; darunter bytegleicher Wiederholungsbau, veraltete Skills, zusätzliche Dateien, Manifestfeld, Versionszuordnung, Schreibschutz, Lizenzmitnahme und Symlink-Abweisung.
- Katalogbudget: fünf Tests bestanden. Die bisherige Basis von 287 Plugins, 23000 Skills und 3630000 Beschreibungszeichen bleibt bestehen. Für 296 Plugins ergeben sich proportional 23721 Skills und 3743832 Beschreibungszeichen. Tatsächlich vorhanden: 23238 und 3697127. Einzelplugin-, Dateigrößen- und Zeilengrenzen bleiben unverändert.
- App-Integration: 16 Tests bestanden; Start- und Fortsetzungsregressionen: elf bestanden; Komponentenrouting: sechs bestanden.
- Bauvergabe: zehn Tests bestanden; Immobilien-Rechtsabteilung und Versandwerkstatt: acht Tests bestanden. Beide Suiten prüfen Komponentenversionen gegen den jeweiligen Marketplace-Eintrag und dessen explizite Release-Zuordnung. Bereits auf main vorhandene Auswahlbeschreibungen bleiben durch eigene Dateihashes geschützt; die unveränderte ursprüngliche Lieferung bleibt zusätzlich erhalten.
- Grundstücksrecherche: 109 Anwendungstests bestanden; ein ausdrücklich zu aktivierender Liveabruf nicht ausgeführt. Browserprüfungen laufen zusätzlich im bestehenden Anwendungsworkflow.
- Hauptverzeichnis und Fachgebietsübersicht: Bestandszahlen, Sortierung und Paketversionen abgeglichen. Keine Änderungen an Testakten.

## 1.3. Veröffentlichung

Das Komponentenrelease `kompatibilitaet-v445.35.1` umfasst neun installierbare Plugin-ZIPs, ein Website-ZIP, `quellenabgleich.json` und `checksums-sha256.txt`. Die ZIPs werden deterministisch aus versionierten Dateien erstellt. Unversionierte lokale Vorgänge werden nicht übernommen. Lizenzdateien bleiben enthalten. Eigenständige Werkstatt-, Schnellstart- und Hauptproblemdateien werden nicht automatisch installiert.

Der Veröffentlichungsworkflow prüft Tag, Zugehörigkeit zu main und Quellencommit. Vor Veröffentlichung werden die hochgeladenen Dateien erneut heruntergeladen und ihre Prüfsummen kontrolliert. Bereits öffentliche Releases werden nicht überschrieben. Alte Tags, Gesamtsammelarchive und die Latest-Zuordnung bleiben unverändert.

## 1.4. Grenzen und abgegrenzte Altbefunde

Die Strukturprüfung ersetzt keinen Live-Lauf in jeder Oberfläche und keine juristische Richtigkeitsgarantie. Lokale Dateierzeugung, Recherchezugang und Veröffentlichungsrechte hängen von der jeweiligen Umgebung ab. Die Budgetanpassung ist eine Korrektur des Katalogmaßstabs, kein behaupteter Geschwindigkeitsgewinn.

Zwei zusätzliche globale Altprüfungen sind außerhalb dieses Reparaturumfangs weiterhin nicht vollständig grün: Die Navigationsprüfung meldet einen lokalen Pfad in einer gespeicherten Qualitätsprobe und sechs Vorschauverweise auf Markdown-Dateien anderer Komponenten. Der ältere Readiness-Audit verlangt außerdem Generator-Marker in acht bewusst individuell gepflegten READMEs und beanstandet eine Dateigrößenangabe sowie eine Wortform im Prüfsystem der experimentellen Vorlagensammlung. Diese Befunde werden nicht als neue Importfehler ausgegeben oder durch Löschen der Prüfungen verdeckt.
