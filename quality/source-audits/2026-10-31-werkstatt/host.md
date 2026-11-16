# Marketplace und Hostprüfung

Geprüft am 16. November 2026. Ausgangspunkt war der veröffentlichte Repository-Stand [`b6f3df2149`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/commit/b6f3df21493250508646a385354447a9893c72ab). Nach der Korrektur des Schema-Links wurde der aktuelle Katalog erneut geladen. Die folgenden technischen Ergebnisse beziehen sich auf den Marketplace und seine Pakete.

| Prüfweg | Ergebnis |
| --- | --- |
| Claude Code, strikte Herstellerprüfung | Marketplace und 311 Plugin-Manifeste bestanden in Version 2.1.168 und 2.1.325. Beide Versionen erkannten den lokalen Marketplace. |
| Claude Code, Installation | In einem separaten Profil installierte Version 2.1.168 alle 311 Plugins aus dem lokalen Marketplace. Die installierten Paketversionen entsprachen dem Katalog, und alle 3.153 installierten `SKILL.md` stimmten mit den Quelldateien überein. Version 2.1.325 konnte den vollständigen Installationsbestand auslesen. |
| Claude Code, veröffentlichte Paketstichprobe | Vier native Plugin-ZIPs aus [Release 445.36.5](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/qualitaetsrunde-v445.36.5) wurden entpackt, strikt validiert und in einem separaten lokalen Marketplace installiert. Claude Code erkannte die enthaltenen Arbeitsabläufe der vier Pakete für Bauträgerverträge, Arbeitszeugnisse, Sozialversicherungsstatus und Einkauf im Bauunternehmen. |
| ChatGPT-Desktop-Laufzeit für Work und Codex | Der App-Server `Codex Desktop/0.166.0-alpha.5.1` unter macOS 26.5.2 lieferte auf `plugin/list` den Repository-Marketplace mit genau 311 verfügbaren Einträgen. `plugin/read` bestätigte für jeden Eintrag die richtige lokale Quelle und Version sowie zusammen 3.153 aktive Skills mit den erwarteten Pfaden. |

Der Schema-Verweis im [Marketplace](../../../.claude-plugin/marketplace.json) führte zu HTTP 404. Der erreichbare Ersatz bei SchemaStore validiert den gesamten Katalog. Claude Code und die ChatGPT-Desktop-Laufzeit erkennen weiterhin dieselben relativen Paketpfade. [Marketplace-Schema](https://json.schemastore.org/claude-code-marketplace.json)

Claude Code kann den öffentlichen Marketplace verwenden. Für den Organisations-Sync auf github.com verlangt Anthropic ein privates oder internes Spiegelrepository. Die separate ZIP-Installation hängt von Oberfläche, Tarif und Organisationsvorgaben ab. [Claude-Marketplace](https://code.claude.com/docs/en/plugin-marketplaces) · [Claude-Organisationsimport](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) · [Plugins verwenden](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)

OpenAI dokumentiert den Repository-Katalog für lokal geöffnete Projekte in der Desktop-App und für den Import öffentlicher GitHub-Repositories durch ChatGPT-Workspace-Administratoren. Für diesen Workspace-Import wird das Repository als Quelle angegeben. Zum Nachführen von Updates bleibt die Referenz auf `main`. Für einen festen Stand kann ein Commit oder Tag gewählt werden. [Lokaler Marketplace](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work) · [ChatGPT-Workspace-Import](https://learn.chatgpt.com/docs/enterprise/plugin-management)

Die Prüfungen decken Erkennung, Paketidentität, Installation in Claude Code und Laden der Skill-Metadaten ab. Offen bleiben der tatsächliche Organisationsimport in Cowork oder im ChatGPT-Workspace und die vollständige Modellbearbeitung in den jeweiligen Oberflächen. Insbesondere hängen Recherche, Zugriff auf Arbeitsdateien und Dokumentexport von den dort verfügbaren Werkzeugen ab.

Die Ladeprüfung lässt sich aus dem Repository mit den installierten Herstellerprogrammen wiederholen:

```sh
python3 scripts/validate-manufacturer-plugins.py
python3 scripts/validate-with-codex-app-server.py
```

Beide Programme akzeptieren `--executable` für eine bestimmte Herstellerversion. Die Codex-Prüfung liest den lokalen Katalog und die sichtbaren Skill-Dateien. Dazu sind keine Plugin-Installation und kein Modellaufruf erforderlich.
