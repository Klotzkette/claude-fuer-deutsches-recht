# Installation in einfach

[Startseite und fünf Verzeichnisse](./README.md#alle-vollständigen-listen-von-a-bis-z) · [Plugin-Katalog](./README.md#was-ist-drin) · [Downloads](./ASSET_INDEX.md) · [Kurzanleitung](./QUICKSTART.md)

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

Der Organisations-Marketplace ist für Team und Enterprise vorgesehen und wird von einem Owner unter **Organization settings → Plugins & skills → Marketplaces** eingerichtet. Vorher müssen Cowork und Skills für die Organisation aktiviert sein. Die folgenden Menübezeichnungen wurden am 25. September 2026 mit der unten verlinkten Anbieterdokumentation abgeglichen.

Die GitHub-Synchronisierung akzeptiert derzeit nur private oder interne Repositorys. Deshalb den aktuellen Inhalt dieses öffentlichen Projekts zuerst in ein privates oder internes Spiegelrepository der Organisation übernehmen. Anschließend **Add → Sync from GitHub** wählen, das Spiegelrepository als `owner/repo` eintragen und den ersten Sync abwarten. Die Claude GitHub App muss auf dieses Repository zugreifen können. Die relative Plugin-Struktur und die Datei [`marketplace.json`](./.claude-plugin/marketplace.json) bleiben dabei unverändert.

Ein manueller Marketplace wird unter **Add → Upload a plugin** mit einzelnen Plugin-ZIPs befüllt. `marketplace.json` ist kein Upload für diesen Dialog. Jedes ZIP muss kleiner als 50 MB sein; ein manueller Marketplace nimmt höchstens 100 Plugins auf. Für den gesamten [Plugin-Bestand](./README.md#was-ist-drin) ist daher das private oder interne Spiegelrepository zweckmäßiger, für eine gezielte Auswahl der manuelle Upload.

Weitere automatische Updates müssen beim Marketplace über **Sync automatically** aktiviert sein und setzen einen in den Standardbranch gemergten Pull Request mit Versionsanhebung voraus. Ein direkter Push löst sie nicht aus; dann in der Marketplace-Verwaltung **Update** wählen. Der Sync kann bis zu 30 Minuten dauern.

Nur im Kommandozeilen-Client kann das öffentliche Repository unmittelbar verwendet werden:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install liquiditaetsplanung@klotzkette-german-legal-skills
```

Der Marketplace lädt den Stand des verbundenen Spiegelrepositorys. Einzelne Plugin-ZIPs stammen dagegen aus dem getaggten Release und sind für einen gezielten, reproduzierbaren Stand meist einfacher.

Aktuelle Oberflächen- und Planvorgaben: [Plugins verwenden](https://support.claude.com/en/articles/13837440-use-plugins-in-claude), [Organisations-Marketplaces verwalten](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) und [Skills verwenden](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## 5. Ohne Installation anfangen

Jede Plugin-README erklärt zuerst die Bestandteile und verlinkt den Abschnitt „In 30 Sekunden starten“. Im oberen Bereich findest du:

1. der direkte Schnellstart-Download,
2. der ausführliche Werkstatt-Download,
3. ein fertiger Startsatz für den Arbeitsordner,
4. zugeordnete Testakten oder den Verweis auf die zentrale Sammlung.

Der [Plugin-Katalog](./README.md#was-ist-drin) führt zu allen Plugin-Startseiten. Der [Download-Index](./ASSET_INDEX.md) enthält zusätzlich sämtliche Einzeldateien.

## 6. Nach der Installation prüfen

1. Neue Aufgabe öffnen.
2. Plugin in der Pluginverwaltung als aktiv kontrollieren.
3. Einen Fachskill über `/` oder `+` wählen.
4. Zwei oder drei Unterlagen bereitstellen und einen konkreten Auftrag stellen.

Ein geeigneter Funktionstest lautet:

> Erfasse zuerst alle Dateien nach Name, Datum und Typ. Öffne höchstens fünf tragende Unterlagen, prüfe die laufende Frist und liefere unmittelbar das nächste fachlich passende Schreiben. Erweitere die Lektüre nur für eine konkrete Beleglücke und frage nur gebündelt nach, wenn die Unterlagen die entscheidende Weiche nicht beantworten.

Die Antwort soll die Unterlagen verwerten und nicht mit einem allgemeinen Fragenkatalog beginnen.

## 7. Laufzeit bei großen Ablagen verbessern

Aktiviere für einen konkreten Vorgang nur das tatsächlich benötigte Plugin und öffne nach Installation, Aktivierung oder Update eine neue Aufgabe. Wenn der Sachskill feststeht, wähle ihn unmittelbar über `/` oder `+`. Bei Leistungsphasen, Länder-, Behörden-, Lohn-, BWA-, Sanierungsgewinn-, Beirats- und BHO-Fragen öffnet der jeweilige Fachrouter nur die einschlägige Referenz; mehrere Vertiefungen werden nur bei einer echten Schnittstelle geladen. Bei Microsoft 365 wird die Suche schneller und genauer, wenn Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und ein prägnanter Suchbegriff vorgegeben sind. Der erste Durchgang soll höchstens 20 Treffer erfassen und höchstens fünf tragende Dokumente öffnen; erweitert wird nur für eine konkret benannte Beleglücke.

Bereits gelesene Word- und PDF-Dateien werden nicht erneut geöffnet. Bei Tabellen genügt zunächst das einschlägige Blatt mit dem relevanten Zellbereich, bei E-Mails der genaue Gesprächsverlauf. Für einen einzelnen Fall bleibt der Schnellstart oder das Einzel-Plugin der schnellste Weg.

## 8. Häufige Fehler

| Symptom | Ursache | Lösung |
| --- | --- | --- |
| Upload wird sofort abgelehnt | falsches ZIP oder Repository-ZIP | Einzel-ZIP aus dem Release laden |
| Im Auswahldialog liegt nur ein Ordner | ZIP wurde automatisch entpackt | ZIP erneut laden und automatisches Öffnen ausschalten |
| Plugin ist installiert, Skill fehlt | alte Aufgabe oder Plugin nicht aktiv | neue Aufgabe öffnen und Aktivierung prüfen |
| Öffentliches Repository wird abgelehnt | Organisations-Sync verlangt ein privates oder internes Repository | privaten oder internen Spiegel verbinden |
| Marketplace zeigt nichts | Repository-Angabe, App-Zugriff oder Sync unvollständig | Spiegelrepository und Zugriff prüfen, dann **Update** wählen |
| „Marketplace sync failed“ mit „validation errors“ | mindestens ein Paket oder der synchronisierte Stand wird abgelehnt | Abschnitt 8.1 durcharbeiten und den genauen Prüfbericht festhalten |
| Erster Start dauert zu lange | kompletter Marketplace statt Einzel-Plugin | zunächst Einzel-ZIP oder Schnellstart-Markdown verwenden |
| Microsoft-365-Suche läuft zu breit | Ablage und Suchziel nicht eingegrenzt | Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und Suchbegriff nennen; zunächst höchstens fünf Kerndokumente öffnen |
| Spätere Antworten werden langsam | zu langer Aufgabenverlauf oder wiederholte Dateilektüre | neue Aufgabe mit kompaktem Ergebnisstand öffnen; bereits gewonnene Extrakte weiterverwenden |
| Prompt fragt bekannte Daten erneut ab | Arbeitsordner nicht ausgewählt oder Auftrag zu abstrakt | Dateien bereitstellen und den Funktionstest aus Abschnitt 6 verwenden |

### 8.1 Marketplace meldet Validierungsfehler

Zuerst den tatsächlich verbundenen Repository-Stand und die verwendete Oberfläche festhalten. Ein Organisations-Spiegel und ein bereits heruntergeladenes Release-ZIP können unterschiedliche Versionen enthalten. Die Meldung allein nennt weder das betroffene Plugin noch dessen Fehler.

Wer das Repository lokal prüft, führt aus dessen Wurzelverzeichnis aus:

```bash
node scripts/validate-plugin-structure.mjs
node scripts/validate-marketplace-import.mjs
claude plugin validate --strict .claude-plugin/marketplace.json
```

Die letzte Prüfung benötigt die installierte Claude-Code-CLI. Für einzelne Pakete kann zusätzlich `claude plugin validate --strict ./liquiditaetsplanung` verwendet werden; für alle Pakete steht [validate-with-claude-cli.sh](./scripts/validate-with-claude-cli.sh) bereit. Diese Prüfungen melden Dateifehler, ersetzen aber keinen erfolgreichen Import in der betroffenen Anwendung. Der Unterschied ist auch in der [offiziellen Marketplace-Dokumentation](https://code.claude.com/docs/en/plugin-marketplaces#validate-and-test) beschrieben.

Bei einem Fehler den gemeldeten Pfad korrigieren und den aktualisierten Stand erneut synchronisieren. Sind die Prüfungen erfolgreich, den Sync in der Organisationsverwaltung über **Update** wiederholen oder als Eingrenzung ein einzelnes Plugin-ZIP aus dem aktuellen Release hochladen. Nach erfolgreichem Sync die Installationseinstellungen kontrollieren, weil ein fehlgeschlagener Sync sie zurücksetzen kann.

Bleibt der Fehler bestehen, bitte im [Issue](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/new) App-Version, Betriebssystem, persönlichen Upload oder Organisations-Sync, Repository-Commit beziehungsweise Release-Version, Plugin-Dateiname, vollständigen Fehlertext und die Prüfergebnisse nennen. Zugangsschlüssel und Mandatsunterlagen gehören nicht in den Bericht. Ein lokal gültiger Stand belegt nicht, dass der Fehler in einem anderen Benutzerkonto bereits behoben ist.

Die kompakte Gesamtanleitung steht in [Schnellstart](./QUICKSTART.md).
