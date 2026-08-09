# Installation in einfach

Der robusteste Weg für einen einzelnen Nutzer ist: **ein Plugin-ZIP laden, in der Pluginverwaltung hochladen, neue Aufgabe öffnen**. Der Marketplace ist die bessere Wahl, wenn eine Organisation viele Plugins zentral verteilen und aktualisieren will.

## 1. Einzelnes Plugin installieren

1. Den [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) öffnen.
2. Das gewünschte Einzel-ZIP laden, beispielsweise `fachanwalt-sozialrecht.zip`, `rentenpruefer.zip` oder `schriftsatz-versandwerkstatt.zip`.
3. In der Anwendung **Customize → Plugins** öffnen.
4. **Plugin hochladen**, **Upload plugin** oder den entsprechenden Plus-Schalter wählen und das ZIP auswählen.
5. Nach erfolgreichem Upload eine neue Aufgabe öffnen und den Skill über `/` oder `+` auswählen.

Die Schalterbezeichnung kann je nach Oberfläche abweichen. Entscheidend ist der Dialog für ein eigenes Plugin-ZIP, nicht der Dialog für einen Repository- oder Marketplace-Pfad.

## 2. Diese Dateien haben einen anderen Zweck

| Datei | Richtige Verwendung |
| --- | --- |
| `<plugin>.zip` | als einzelnes Plugin hochladen |
| `<plugin>-schnellstart.md` | ohne Installation zusammen mit den Unterlagen öffnen |
| `<plugin>-werkstatt.md` | ohne Installation für umfangreiche Vorgänge öffnen |
| `testakte-<name>.zip` | als Arbeitsunterlagen öffnen, nicht als Plugin installieren |
| `alle-plugins-megazip.zip` | zuerst entpacken; darin liegende Einzel-ZIPs verwenden |
| `marketplace.json` | Marketplace-Manifest, kein installierbares Plugin |
| Repository-ZIP aus **Code → Download ZIP** | Quellbestand, kein installierbares Einzel-Plugin |

Ein korrektes Plugin-ZIP enthält `.claude-plugin/plugin.json` und `skills/` direkt auf der Wurzelebene. Es enthält nicht noch einen zusätzlichen äußeren Repository-Ordner.

## 3. Wenn der Mac das ZIP nicht annimmt

1. Prüfen, ob der Browser das ZIP nach dem Download automatisch entpackt hat. Für den Upload wird die ZIP-Datei gebraucht, nicht der entstandene Ordner.
2. Prüfen, ob die Datei vollständig lokal liegt. Bei einem Cloud-Platzhalter zuerst den Download abschließen.
3. Sicherstellen, dass der Dateiname nicht versehentlich auf `.zip.zip` endet.
4. Das Einzel-ZIP statt `alle-plugins-megazip.zip` auswählen.
5. Die Datei gegebenenfalls erneut aus dem [Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) laden.

Wer den Inhalt technisch prüfen möchte, kann ausführen:

```bash
file ~/Downloads/liquiditaetsplanung.zip
unzip -l ~/Downloads/liquiditaetsplanung.zip | head
```

Die Auflistung muss `.claude-plugin/plugin.json` und einen `skills/`-Ordner zeigen.

## 4. Marketplace für eine Organisation

Der Organisations-Marketplace ist für Team und Enterprise vorgesehen und wird von einem Owner unter **Organization settings → Plugins** eingerichtet. Vorher müssen Cowork und Skills für die Organisation aktiviert sein.

Die GitHub-Synchronisierung akzeptiert derzeit nur private oder interne Repositorys. Deshalb den aktuellen Inhalt dieses öffentlichen Projekts zuerst in ein privates oder internes Spiegelrepository der Organisation übernehmen. Anschließend **Add plugin → GitHub** wählen, das Spiegelrepository als `owner/repo` eintragen und den ersten Sync abwarten. Die relative Plugin-Struktur und die Datei [`marketplace.json`](./.claude-plugin/marketplace.json) bleiben dabei unverändert.

Ein manueller Marketplace wird dagegen mit einzelnen Plugin-ZIPs befüllt. `marketplace.json` ist kein Upload für diesen Dialog. Jedes ZIP muss kleiner als 50 MB sein; ein manueller Marketplace nimmt höchstens 100 Plugins auf. Für alle 235 Plugins ist daher das private oder interne Spiegelrepository zweckmäßiger, für eine gezielte Auswahl der manuelle Upload.

Automatischer Sync setzt einen in den Standardbranch gemergten Pull Request mit Versionsanhebung voraus. Ein direkter Push löst ihn nicht aus; dann in der Marketplace-Verwaltung **Update** wählen. Der Sync kann bis zu 30 Minuten dauern.

Nur im Kommandozeilen-Client kann das öffentliche Repository unmittelbar verwendet werden:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install liquiditaetsplanung@klotzkette-german-legal-skills
```

Der Marketplace lädt den Stand des verbundenen Spiegelrepositorys. Einzelne Plugin-ZIPs stammen dagegen aus dem getaggten Release und sind für einen gezielten, reproduzierbaren Stand meist einfacher.

Aktuelle Oberflächen- und Planvorgaben: [Plugins verwenden](https://support.claude.com/en/articles/13837440-use-plugins-in-claude), [Organisations-Marketplaces verwalten](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) und [Skills verwenden](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## 5. Ohne Installation anfangen

Jede Plugin-README beginnt mit einem Abschnitt **In 30 Sekunden starten**. Dort stehen:

1. der direkte Schnellstart-Download,
2. der ausführliche Werkstatt-Download,
3. ein fertiger Startsatz für den Arbeitsordner,
4. die zum Fachgebiet gehörenden Testakten.

Der [Plugin-Katalog](./README.md#was-ist-drin) führt zu allen 235 Startseiten. Der [Download-Index](./ASSET_INDEX.md) enthält zusätzlich sämtliche Einzeldateien.

## 6. Nach der Installation prüfen

1. Neue Aufgabe öffnen.
2. Plugin in der Pluginverwaltung als aktiv kontrollieren.
3. Einen Fachskill über `/` oder `+` wählen.
4. Zwei oder drei Unterlagen bereitstellen und einen konkreten Auftrag stellen.

Ein geeigneter Funktionstest lautet:

> Lies zuerst alle vorhandenen Dateien. Prüfe die laufende Frist und liefere unmittelbar das nächste fachlich passende Schreiben. Frage nur gebündelt nach, wenn die Unterlagen die entscheidende Weiche nicht beantworten.

Die Antwort soll die Unterlagen verwerten und nicht mit einem allgemeinen Fragenkatalog beginnen.

## 7. Häufige Fehler

| Symptom | Ursache | Lösung |
| --- | --- | --- |
| Upload wird sofort abgelehnt | falsches ZIP oder Repository-ZIP | Einzel-ZIP aus dem Release laden |
| Im Auswahldialog liegt nur ein Ordner | ZIP wurde automatisch entpackt | ZIP erneut laden und automatisches Öffnen ausschalten |
| Plugin ist installiert, Skill fehlt | alte Aufgabe oder Plugin nicht aktiv | neue Aufgabe öffnen und Aktivierung prüfen |
| Öffentliches Repository wird abgelehnt | Organisations-Sync verlangt ein privates oder internes Repository | privaten oder internen Spiegel verbinden |
| Marketplace zeigt nichts | Repository-Angabe, App-Zugriff oder Sync unvollständig | Spiegelrepository und Zugriff prüfen, dann **Update** wählen |
| Erster Start dauert zu lange | kompletter Marketplace statt Einzel-Plugin | zunächst Einzel-ZIP oder Schnellstart-Markdown verwenden |
| Prompt fragt bekannte Daten erneut ab | Arbeitsordner nicht ausgewählt oder Auftrag zu abstrakt | Dateien bereitstellen und den Funktionstest aus Abschnitt 6 verwenden |

Die kompakte Gesamtanleitung steht in [Schnellstart](./QUICKSTART.md). Fehler können mit Screenshot und gewähltem Dateinamen als [Issue](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/new) gemeldet werden.
