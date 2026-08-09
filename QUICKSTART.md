# Schnellstart

Diese Anleitung führt ohne Umweg zum ersten verwertbaren Arbeitsprodukt. Für einen einzelnen Vorgang genügt meistens ein Plugin oder sogar nur dessen Schnellstart-Markdown; der gesamte Marketplace ist nur sinnvoll, wenn viele Rechtsgebiete dauerhaft gebraucht werden.

## 1. Den passenden Weg wählen

| Bedarf | Weg | Zeit bis zum Start |
| --- | --- | --- |
| Ein Rechtsgebiet, dauerhaft nutzbar | einzelnes Plugin-ZIP aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) | wenige Minuten |
| Viele Rechtsgebiete in einer Organisation | Marketplace aus einer privaten oder internen Spiegelung dieses Repositorys synchronisieren | einmalige Einrichtung |
| Sofort arbeiten, nichts installieren | Schnellstart-Markdown aus der README des gewünschten Plugins laden | sofort |
| Umfangreicher oder mehrstufiger Vorgang | Werkstatt-Markdown des gewünschten Plugins laden | sofort |

Der [Plugin-Katalog](./README.md#was-ist-drin) führt zu jeder Plugin-README. Dort stehen oben der Plugin-Download, der Schnellstart, die Werkstatt, ein fertiger Startsatz und gegebenenfalls passende Testakten.

## 2. Sofort ohne Installation arbeiten

1. Im [Plugin-Katalog](./README.md#was-ist-drin) das Rechtsgebiet öffnen.
2. Oben in der Plugin-README bei **Kompakter Prompt (Schnellstart)** auf den Markdown-Download klicken.
3. Die Markdown-Datei zusammen mit dem Arbeitsordner oder den relevanten Unterlagen öffnen.
4. Diesen Startsatz verwenden:

> Lies zuerst alle Dateien im ausgewählten Ordner. Beginne unmittelbar mit dem verlangten Arbeitsprodukt. Wenn nur der Prompt gestartet wurde, bestimme aus den Unterlagen selbst die passende Fachroute und liefere einen ersten belastbaren Stand. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Für einen Folgewunsch genügt die gewünschte Änderung, etwa „Rechne zusätzlich die Gegenvariante“, „Formuliere daraus die Klage“ oder „Kürze den Mandantenbrief“. Der bereits erarbeitete Aktenstand soll fortgeführt und nicht neu abgefragt werden.

## 3. Ein einzelnes Plugin installieren

1. Den [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) öffnen.
2. Das gewünschte `<plugin>.zip` laden, beispielsweise `liquiditaetsplanung.zip`.
3. In der Anwendung **Customize → Plugins** öffnen und das eigene Plugin-ZIP hochladen. In Cowork zuerst den Cowork-Bereich öffnen. Die Bezeichnung des Upload-Schalters kann je nach Oberfläche leicht abweichen.
4. Eine neue Aufgabe öffnen. Den passenden Skill über `/` oder `+` auswählen oder den Auftrag unmittelbar mit dem Arbeitsordner stellen.

Nicht das Repository-ZIP aus **Code → Download ZIP** verwenden. Das installierbare Einzel-ZIP enthält `.claude-plugin/plugin.json` und `skills/` unmittelbar auf seiner Wurzelebene.

## 4. Den Marketplace einbinden

Der organisationsweite Marketplace steht Team- und Enterprise-Organisationen zur Verfügung. Cowork und Skills müssen freigeschaltet sein; die Einrichtung erfolgt durch einen Owner unter **Organization settings → Plugins**.

Für die GitHub-Synchronisierung muss das verbundene Repository derzeit **privat oder intern** sein. Das öffentliche Original kann daher nicht unmittelbar als Organisations-Marketplace verbunden werden. Für den vollständigen Katalog wird sein Inhalt in ein privates oder internes Spiegelrepository übernommen; dort bleibt die relative Struktur aus [`marketplace.json`](./.claude-plugin/marketplace.json) unverändert. Danach: **Add plugin → GitHub**, Spiegelrepository im Format `owner/repo` angeben und den ersten Sync abwarten.

Der manuelle Organisationsweg lädt einzelne Plugin-ZIPs hoch, nicht `marketplace.json`. Pro ZIP gelten höchstens 50 MB, pro manuellem Marketplace höchstens 100 Plugins. Für alle 235 Plugins ist deshalb die GitHub-Synchronisierung aus dem privaten oder internen Spiegelrepository der klare Hauptweg; für eine kleine Auswahl genügt der manuelle Upload.

Automatische Aktualisierung wird nur durch einen in den Standardbranch gemergten Pull Request mit Versionsanhebung ausgelöst. Nach einem direkten Push muss ein Owner in der Marketplace-Verwaltung **Update** wählen. Ein Sync kann bei diesem Umfang bis zu 30 Minuten dauern.

Nur im Kommandozeilen-Client kann das öffentliche Repository unmittelbar als Marketplace hinzugefügt werden:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install <plugin-name>@klotzkette-german-legal-skills
```

Der erste Repository-Sync ist deutlich größer als die Installation eines einzelnen Plugin-ZIPs. Bei nur einem Rechtsgebiet ist deshalb das Einzel-ZIP schneller.

Aktuelle Oberflächen- und Planvorgaben: [Plugins verwenden](https://support.claude.com/en/articles/13837440-use-plugins-in-claude), [Organisations-Marketplaces verwalten](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) und [Skills verwenden](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## 5. Was der erste Lauf leisten soll

| Eingangslage | Erwartetes Verhalten |
| --- | --- |
| Dateien oder Ordner vorhanden | Unterlagen zuerst lesen; Fundstellen und Fristen sichern; erstes Arbeitsprodukt liefern |
| Konkretes Dokument verlangt | Mit diesem Dokument beginnen; kein allgemeines Lagebild voranstellen |
| Nur Skill oder Prompt gestartet | Fachroute aus Dateinamen und Inhalt bestimmen; nicht nach dem Auftrag fragen |
| Keine verwertbaren Unterlagen | genau eine gebündelte Frage zu den entscheidenden Angaben stellen |
| Großer Ordner | nach den ersten entscheidungserheblichen Dateien einen Teilstand liefern und offene Dateien nennen |
| Folgewunsch | Tatsachen, Berechnungen und Quellen beibehalten; nur die gewünschte Dimension ändern |

## 6. Kurzer Funktionstest

1. Ein Plugin aktivieren oder seinen Schnellstart öffnen.
2. Zwei bis fünf zusammengehörige Dokumente bereitstellen.
3. Einen konkreten Auftrag stellen, beispielsweise: „Prüfe die laufende Frist und entwirf das nächste Schreiben.“

Der erste Antwortblock soll bereits Ergebnisrichtung, Fundstelle, Frist oder Risiko und das nächste Arbeitsprodukt enthalten. Ein vorgeschalteter Fragenkatalog ist nur zulässig, wenn die Unterlagen die entscheidende Weiche tatsächlich nicht beantworten.

## 7. Fehler schnell eingrenzen

| Problem | Nächster Schritt |
| --- | --- |
| Plugin erscheint nach dem Upload nicht | neue Aufgabe öffnen, Pluginverwaltung neu laden und prüfen, ob wirklich das Einzel-ZIP gewählt wurde |
| ZIP wurde automatisch entpackt | die ZIP erneut laden und das automatische Öffnen von Downloads vorübergehend ausschalten |
| Skill wird nicht vorgeschlagen | Plugin aktivieren und den Skill einmal über `/` oder `+` wählen |
| Öffentliches Repository wird beim Organisations-Sync abgelehnt | privates oder internes Spiegelrepository verbinden; das öffentliche Original ist nur der Quellstand |
| Marketplace-Sync dauert lange | bis zu 30 Minuten abwarten; für den sofortigen Start ein einzelnes Plugin-ZIP oder den Schnellstart verwenden |
| Antwort fragt vorhandene Angaben erneut ab | auf den Arbeitsordner verweisen und „Dateien zuerst, dann Erstprodukt“ ergänzen |
| Markdown wird nur im Browser angezeigt | den HTML-Download in der Plugin-README oder den [Download-Index](./ASSET_INDEX.md) verwenden |

Ausführliche Hinweise zu ZIP-Auswahl, Mac-Downloads und Organisations-Marketplaces stehen in [Installation in einfach](./INSTALLATION_EINFACH.md).
