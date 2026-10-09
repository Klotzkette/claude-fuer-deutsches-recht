# Skill-Gesamtübersicht

[Repo-Start](README.md) | [Dateikatalog](README.md#dateikatalog) | [Sofort-Downloads](README.md#sofort-downloads) | [Vergabestelle](vergabestelle-behoerden/README.md) | [Bieter](bieter-unternehmen/README.md) | [Konkurrent](konkurrenten-rechtsschutz/README.md) | [Plugin-Detailseiten](skills-index/README.md) | [Testakten](testakten/README.md) | [Rechtsprechung](references/leitentscheidungen-anker.md)

Automatisch generierte Gesamtübersicht aller 255 Skills in 3 Plugins.

Stand: `v445.33.1`.

## Alle Skills auf einmal herunterladen

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Paket | Inhalt | Download |
| --- | --- | --- |
| Alle Skills als Markdown | Reine `SKILL.md`-Dateien aller 3 Plugins — als echte Datei-Downloads | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alle-skills-markdown.zip) |
| Unified Mini Prompts | Pro Marktrolle ein kompakter Ein-Datei-Prompt | [Einzelne Markdown-Dateien](unified-mini-prompts/README.md) |
| Alle Plugins (installierbar) | Alle 3 Plugin-ZIPs in einem Archiv (für Claude Code) | [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alle-plugins-megazip.zip) |
| Vollständiges Quellarchiv (nicht installierbar) | Alle Komponentenquellen unter `vergaberecht-werkstatt/` und README.txt mit Warnhinweis | [`alles-komplettpaket.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alles-komplettpaket.zip) |

Das Markdown-Paket reicht, wenn man die vollständigen Skills in ChatGPT, Gemini, Mistral, Le Chat oder Perplexity nutzen will. Die Unified Mini Prompts sind die Sparvariante: ein kurzer Workflow pro Plugin, wenn man nur eine einzige Markdown-Datei verwenden möchte. Das Plugin-Paket ist für Claude-Code-/Cowork-Nutzer. Das Komplettpaket enthält zusätzlich Testakten und alle Repo-Übersichten.

Wer nur ein bestimmtes Plugin will: weiter unten in der Plugin-Tabelle pro Plugin eigene Download-Links (Plugin-ZIP, Markdown-ZIP und Unified Mini Prompt).

## Welche Datei nehme ich?

| Bedarf | Beste Wahl | Warum |
| --- | --- | --- |
| Plugin in Claude Code nutzen | Plugin-ZIP der Marktrolle | Enthält Skills, Hilfsdateien, Vorlagen und Referenzen als installierbares Paket. |
| Ohne Plugin schnell starten | Unified Mini Prompt | Eine Markdown-Datei pro Marktrolle, autark und kurz genug für normale Chatfenster. |
| Ohne Plugin tief arbeiten | Markdown-ZIP der Marktrolle | Enthält alle `SKILL.md`-Dateien dieser Marktrolle. |
| Einzelnen Spezialfall lösen | Detailseite des Plugins öffnen und passende `SKILL.md` wählen | Jede Zeile enthält Beschreibung, Browser-Ansicht und Raw-Link. |
| Alles lokal prüfen oder weiterbauen | Komplettpaket oder Repo-Checkout | Enthält Plugins, Testakten, Übersichten, Validatoren und Release-Struktur. |

## Ohne Skillauswahl starten

Wenn ein Aktenordner, ZIP, Portalexport, DMS-Export oder Projektordner vorliegt, zuerst die Marktrolle wählen und den Ordner mit einem Satz wie `Hier ist der neue Fall, bitte vorbereiten` übergeben. Das passende Plugin startet über Orchestrator und Kaltstart selbst mit Fallkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Output-Weiche, Lückenliste und erstem Arbeitsauftrag. Die technischen Skill-Slugs bleiben stabile Links; die sprechenden Arbeitsnamen stehen in den Detailseiten in einer eigenen Spalte und stammen direkt aus der H1 der jeweiligen `SKILL.md`.

## Worum es hier geht: alles nur große Prompts

Diese Skills sind am Ende nichts weiter als große, sehr sorgfältig formulierte System-Prompts in Markdown. Sie wurden für das Claude-Code-Plugin-System geschrieben, funktionieren aber in jedem anderen Chatbot genauso.

So benutzt man einen Skill außerhalb von Claude Code:

1. Unten in der Plugin-Tabelle auf das gewünschte Plugin klicken — die Detailseite mit allen Skills öffnet sich.
2. Auf der Detailseite oben auf Markdown-ZIP klicken — die `<plugin>-skills-markdown.zip` landet direkt im Download-Ordner. Entpacken, gewünschte `SKILL.md` öffnen.
3. Entweder den kompletten Text mit `Strg+A` / `Cmd+A` kopieren und in den Chat einfügen (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat oder andere Chatbots).
4. Oder die einzelne `SKILL.md` als Anhang in den Chatbot ziehen.
5. Danach die eigene Frage / das eigene Dokument hinterherschicken — der Chatbot übernimmt die Rolle aus dem Skill.

Hinweis zu Browser-Links: `[Markdown]` zeigt die Datei im Browser an (zum Lesen oder Kopieren). `[Raw .md]` öffnet den Rohtext — GitHub liefert ihn als `text/plain` aus, manche Browser zeigen ihn deshalb als Text statt als Download. Wenn ein echter Datei-Download gewünscht ist, immer das Plugin-Markdown-ZIP nehmen.

So bekommt man die komplette Sammlung als installierbares ZIP:

- In der Plugin-Tabelle unten in der Spalte Plugin-ZIP auf den Download-Link klicken. Das lädt eine ZIP-Datei mit allen Skills dieses Plugins inkl. Hilfsdateien, Prüfrastern und Vorlagen — direkt in Claude Code installierbar.
- Wer kein Claude Code nutzt, nimmt stattdessen Markdown-ZIP — das enthält nur die `SKILL.md` als reine Markdown-Dateien zum Einlesen in beliebige Chatbots.
- Wer nur schnell eine einzige Datei ausprobieren will, nimmt Unified Mini Prompt. Das ist bewusst nicht die volle Skilltiefe, sondern der verdichtete Arbeitsmodus des jeweiligen Plugins.

Wichtig: Wenn irgendwo im Repo ein neuer Skill angelegt wird (also ein neuer Ordner `<plugin>/skills/<skill>/SKILL.md`), erscheint er beim nächsten Lauf von `scripts/generate-skills-md.py` automatisch -- sowohl in dieser Liste als auch auf der jeweiligen Plugin-Detailseite. Es kann also nichts fehlen.

Die Detailseiten liegen unter [`skills-index/`](skills-index/) -- eine eigene `.md`-Datei pro Plugin. So bleibt diese Hauptseite klein und lädt schnell, statt mit 255 Tabellenzeilen den Browser-Renderer von GitHub zu überfordern.

## Alle Plugins

Pro Plugin: Klick auf die Detailseite öffnet alle Skills, Beschreibungen und Einzel-Downloads. Plugin-ZIP lädt die installierbare Claude-Code-/Cowork-Sammlung. Markdown-ZIP lädt die reinen `SKILL.md`-Dateien. Mini-Prompt ist eine einzelne Markdown-Datei bis 7.500 Zeichen für ChatGPT, Gemini, Mistral oder andere Chatbots.

| Plugin | Rolle | Wofür | Skills | README | Detailseite | Plugin-ZIP | Markdown-ZIP | Mini-Prompt |
| --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| vergabestelle-behoerden | Vergabestelle | Vergabe planen, Unterlagen bauen, Bestangebot werten, Rüge/VK/OLG verteidigen | 122 | [README](vergabestelle-behoerden/README.md) | [Skills ansehen](skills-index/vergabestelle-behoerden.md) | [Plugin](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/vergabestelle-behoerden.zip) | [Markdown](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden-skills-markdown.zip) | [Mini](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden-unified-mini-prompt.md) |
| bieter-unternehmen | Bieter | Unterlagen prüfen, Angebot liefern, Qualitätsvorsprung belegen, Rüge/VK/OLG führen | 113 | [README](bieter-unternehmen/README.md) | [Skills ansehen](skills-index/bieter-unternehmen.md) | [Plugin](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/bieter-unternehmen.zip) | [Markdown](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen-skills-markdown.zip) | [Mini](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen-unified-mini-prompt.md) |
| konkurrenten-rechtsschutz | Konkurrent | Billigzuschlag, Produktvorgabe, Wertung, Eignung und De-facto-Lage angreifen | 20 | [README](konkurrenten-rechtsschutz/README.md) | [Skills ansehen](skills-index/konkurrenten-rechtsschutz.md) | [Plugin](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz.zip) | [Markdown](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz-skills-markdown.zip) | [Mini](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz-unified-mini-prompt.md) |
