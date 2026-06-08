# Skill-Gesamtuebersicht

Automatisch generierte Gesamtuebersicht aller **18549 Skills** in **212 Plugins**.

Stand: `v239.0.0`.

## ⬇️ Alle Skills auf einmal herunterladen

| Paket | Inhalt | Download |
| --- | --- | --- |
| **Alle Skills (kompakt)** | Alle 212 Plugin-ZIPs in einem Archiv (ca. 11 MB) | [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) |
| **Komplettpaket (alles)** | Plugins + Testakten + Uebersichten (ca. 80 MB) | [`alles-komplettpaket.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alles-komplettpaket.zip) |

Das erste Paket reicht, wenn man nur die Prompts (Skills) braucht. Das zweite enthaelt zusaetzlich die Testakten und alle Repo-Uebersichten.

Wer nur **ein bestimmtes Plugin** will: weiter unten in der Plugin-Tabelle pro Plugin ein eigener `[Download]`-Link.

## Worum es hier geht: alles nur grosse Prompts

Diese Skills sind am Ende **nichts weiter als grosse, sehr sorgfaeltig formulierte System-Prompts in Markdown**. Sie wurden fuer das Claude-Code-Plugin-System geschrieben, **funktionieren aber in jedem anderen Chatbot genauso**.

So benutzt man einen Skill ausserhalb von Claude Code:

1. Unten in der Plugin-Tabelle auf das gewuenschte Plugin klicken — die Detailseite mit allen Skills oeffnet sich.
2. Auf der Detailseite den gewuenschten Skill suchen und `[Markdown]` klicken — die Datei `SKILL.md` oeffnet sich im Browser.
3. **Entweder** den kompletten Text mit `Strg+A` / `Cmd+A` kopieren und in den Chat einfuegen (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, ...).
4. **Oder** auf `[Raw .md]` klicken und die Datei direkt herunterladen, dann als Anhang in den Chatbot ziehen oder den Inhalt einfuegen.
5. Danach die eigene Frage / das eigene Dokument hinterherschicken — der Chatbot uebernimmt die Rolle aus dem Skill.

So bekommt man die komplette Sammlung als ZIP:

- In der Plugin-Tabelle unten in der Spalte **ZIP** auf den Download-Link klicken. Das laedt eine ZIP-Datei mit **allen** Skills dieses Plugins (mitsamt Hilfsdateien, Pruefrastern und Vorlagen).
- Wer Claude Code nutzt, kann das ZIP direkt als Plugin installieren. Alle anderen koennen die enthaltenen `SKILL.md`-Dateien einzeln in jeden Chatbot kopieren.

**Wichtig:** Wenn irgendwo im Repo ein neuer Skill angelegt wird (also ein neuer Ordner `<plugin>/skills/<skill>/SKILL.md`), erscheint er beim naechsten Lauf von `scripts/generate-skills-md.py` automatisch -- sowohl in dieser Liste als auch auf der jeweiligen Plugin-Detailseite. Es kann also nichts fehlen.

Die Detailseiten liegen unter [`skills-index/`](skills-index/) -- eine eigene `.md`-Datei pro Plugin. So bleibt diese Hauptseite klein und laedt schnell, statt mit 18549 Tabellenzeilen den Browser-Renderer von GitHub zu ueberfordern.

## Alle Plugins

Pro Plugin: Klick auf den Namen oeffnet die Detailseite mit allen Skills, Beschreibungen und Einzel-Downloads. **ZIP** laedt die komplette Plugin-Sammlung direkt.

| Plugin | Skills | Detailseite | ZIP |
| --- | ---: | --- | --- |
| **agb-recht-pruefer** | 302 | [Skills ansehen](skills-index/agb-recht-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/agb-recht-pruefer.zip) |
| **aktenaufbereiter-strafrecht** | 54 | [Skills ansehen](skills-index/aktenaufbereiter-strafrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenaufbereiter-strafrecht.zip) |
| **aktenauszug-gerichtsverfahren** | 54 | [Skills ansehen](skills-index/aktenauszug-gerichtsverfahren.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |
| **aktienrecht-hauptversammlung-ag-se** | 100 | [Skills ansehen](skills-index/aktienrecht-hauptversammlung-ag-se.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktienrecht-hauptversammlung-ag-se.zip) |
| **anlagen-zu-schriftsaetzen** | 115 | [Skills ansehen](skills-index/anlagen-zu-schriftsaetzen.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |
| **apothekenrecht** | 65 | [Skills ansehen](skills-index/apothekenrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/apothekenrecht.zip) |
| **arbeitsrecht** | 26 | [Skills ansehen](skills-index/arbeitsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitsrecht.zip) |
| **arbeitszeugnis-analyse** | 50 | [Skills ansehen](skills-index/arbeitszeugnis-analyse.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |
| **aufsichtsrat-ag-se-praxis** | 100 | [Skills ansehen](skills-index/aufsichtsrat-ag-se-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aufsichtsrat-ag-se-praxis.zip) |
| **aussenwirtschaft-zoll-sanktionen** | 100 | [Skills ansehen](skills-index/aussenwirtschaft-zoll-sanktionen.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aussenwirtschaft-zoll-sanktionen.zip) |
| **bank-rechtsabteilung** | 119 | [Skills ansehen](skills-index/bank-rechtsabteilung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bank-rechtsabteilung.zip) |
| **barrierefreiheit-web-checker** | 54 | [Skills ansehen](skills-index/barrierefreiheit-web-checker.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/barrierefreiheit-web-checker.zip) |
| **bav-strategie-konzern** | 54 | [Skills ansehen](skills-index/bav-strategie-konzern.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bav-strategie-konzern.zip) |
| **beamtenrecht** | 157 | [Skills ansehen](skills-index/beamtenrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/beamtenrecht.zip) |
| **bereicherungs-und-anfechtungsrecht-pruefer** | 139 | [Skills ansehen](skills-index/bereicherungs-und-anfechtungsrecht-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bereicherungs-und-anfechtungsrecht-pruefer.zip) |
| **berichtspflichten-erlediger** | 57 | [Skills ansehen](skills-index/berichtspflichten-erlediger.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berichtspflichten-erlediger.zip) |
| **berufsgerichtliche-verfahren-freie-berufe** | 95 | [Skills ansehen](skills-index/berufsgerichtliche-verfahren-freie-berufe.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsgerichtliche-verfahren-freie-berufe.zip) |
| **berufsrecht-anwaelte** | 201 | [Skills ansehen](skills-index/berufsrecht-anwaelte.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-anwaelte.zip) |
| **berufsrecht-ki-vertragspruefung** | 93 | [Skills ansehen](skills-index/berufsrecht-ki-vertragspruefung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-ki-vertragspruefung.zip) |
| **berufsrecht-notare** | 196 | [Skills ansehen](skills-index/berufsrecht-notare.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-notare.zip) |
| **berufsrecht-patentanwaelte** | 197 | [Skills ansehen](skills-index/berufsrecht-patentanwaelte.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-patentanwaelte.zip) |
| **berufsrecht-steuerberater** | 200 | [Skills ansehen](skills-index/berufsrecht-steuerberater.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-steuerberater.zip) |
| **berufsrecht-wirtschaftspruefer** | 200 | [Skills ansehen](skills-index/berufsrecht-wirtschaftspruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-wirtschaftspruefer.zip) |
| **betaeubungsmittelrecht** | 100 | [Skills ansehen](skills-index/betaeubungsmittelrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betaeubungsmittelrecht.zip) |
| **betreuungsrecht** | 116 | [Skills ansehen](skills-index/betreuungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betreuungsrecht.zip) |
| **bgb-at-pruefer** | 84 | [Skills ansehen](skills-index/bgb-at-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-at-pruefer.zip) |
| **bgb-bt-pruefer** | 101 | [Skills ansehen](skills-index/bgb-bt-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-bt-pruefer.zip) |
| **buerokratieversteher-entbuerokratisierer** | 100 | [Skills ansehen](skills-index/buerokratieversteher-entbuerokratisierer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/buerokratieversteher-entbuerokratisierer.zip) |
| **bundesnetzagentur-verfahren** | 221 | [Skills ansehen](skills-index/bundesnetzagentur-verfahren.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bundesnetzagentur-verfahren.zip) |
| **bundeswehrrecht-wehrrecht** | 82 | [Skills ansehen](skills-index/bundeswehrrecht-wehrrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bundeswehrrecht-wehrrecht.zip) |
| **commercial-courts-deutschland** | 57 | [Skills ansehen](skills-index/commercial-courts-deutschland.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/commercial-courts-deutschland.zip) |
| **common-law-kompass** | 54 | [Skills ansehen](skills-index/common-law-kompass.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/common-law-kompass.zip) |
| **corporate-kanzlei** | 84 | [Skills ansehen](skills-index/corporate-kanzlei.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/corporate-kanzlei.zip) |
| **datenbankrecht** | 65 | [Skills ansehen](skills-index/datenbankrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenbankrecht.zip) |
| **datenschutz-sanktionsverfahren-verteidigung** | 27 | [Skills ansehen](skills-index/datenschutz-sanktionsverfahren-verteidigung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutz-sanktionsverfahren-verteidigung.zip) |
| **datenschutzrecht** | 260 | [Skills ansehen](skills-index/datenschutzrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutzrecht.zip) |
| **designrecht-geschmacksmusterrecht** | 50 | [Skills ansehen](skills-index/designrecht-geschmacksmusterrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/designrecht-geschmacksmusterrecht.zip) |
| **deutsche-rechtsgeschichte** | 132 | [Skills ansehen](skills-index/deutsche-rechtsgeschichte.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/deutsche-rechtsgeschichte.zip) |
| **dfg-foerderantrag** | 85 | [Skills ansehen](skills-index/dfg-foerderantrag.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dfg-foerderantrag.zip) |
| **dsa-dma-digitalregulierung** | 53 | [Skills ansehen](skills-index/dsa-dma-digitalregulierung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dsa-dma-digitalregulierung.zip) |
| **ecommerce-recht** | 72 | [Skills ansehen](skills-index/ecommerce-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ecommerce-recht.zip) |
| **einfache-leichte-sprache-jura** | 83 | [Skills ansehen](skills-index/einfache-leichte-sprache-jura.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip) |
| **einigungsvertrag-vermoegensrecht** | 100 | [Skills ansehen](skills-index/einigungsvertrag-vermoegensrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einigungsvertrag-vermoegensrecht.zip) |
| **email-umformulierer-berufsrecht** | 83 | [Skills ansehen](skills-index/email-umformulierer-berufsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/email-umformulierer-berufsrecht.zip) |
| **energierecht** | 92 | [Skills ansehen](skills-index/energierecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/energierecht.zip) |
| **erbbaurecht-praxis** | 50 | [Skills ansehen](skills-index/erbbaurecht-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/erbbaurecht-praxis.zip) |
| **europarecht-kompass** | 54 | [Skills ansehen](skills-index/europarecht-kompass.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/europarecht-kompass.zip) |
| **fachanwalt-agrarrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-agrarrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-agrarrecht.zip) |
| **fachanwalt-arbeitsrecht** | 38 | [Skills ansehen](skills-index/fachanwalt-arbeitsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-arbeitsrecht.zip) |
| **fachanwalt-bank-kapitalmarktrecht** | 36 | [Skills ansehen](skills-index/fachanwalt-bank-kapitalmarktrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-bank-kapitalmarktrecht.zip) |
| **fachanwalt-bau-architektenrecht** | 40 | [Skills ansehen](skills-index/fachanwalt-bau-architektenrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-bau-architektenrecht.zip) |
| **fachanwalt-erbrecht** | 36 | [Skills ansehen](skills-index/fachanwalt-erbrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-erbrecht.zip) |
| **fachanwalt-familienrecht** | 40 | [Skills ansehen](skills-index/fachanwalt-familienrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-familienrecht.zip) |
| **fachanwalt-gewerblicher-rechtsschutz** | 36 | [Skills ansehen](skills-index/fachanwalt-gewerblicher-rechtsschutz.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-gewerblicher-rechtsschutz.zip) |
| **fachanwalt-handels-gesellschaftsrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-handels-gesellschaftsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-handels-gesellschaftsrecht.zip) |
| **fachanwalt-insolvenz-sanierungsrecht** | 55 | [Skills ansehen](skills-index/fachanwalt-insolvenz-sanierungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-insolvenz-sanierungsrecht.zip) |
| **fachanwalt-internationales-wirtschaftsrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-internationales-wirtschaftsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-internationales-wirtschaftsrecht.zip) |
| **fachanwalt-it-recht** | 40 | [Skills ansehen](skills-index/fachanwalt-it-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-it-recht.zip) |
| **fachanwalt-medizinrecht** | 56 | [Skills ansehen](skills-index/fachanwalt-medizinrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-medizinrecht.zip) |
| **fachanwalt-miet-wohnungseigentumsrecht** | 59 | [Skills ansehen](skills-index/fachanwalt-miet-wohnungseigentumsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-miet-wohnungseigentumsrecht.zip) |
| **fachanwalt-migrationsrecht** | 68 | [Skills ansehen](skills-index/fachanwalt-migrationsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-migrationsrecht.zip) |
| **fachanwalt-sozialrecht** | 37 | [Skills ansehen](skills-index/fachanwalt-sozialrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-sozialrecht.zip) |
| **fachanwalt-sportrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-sportrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-sportrecht.zip) |
| **fachanwalt-strafrecht** | 47 | [Skills ansehen](skills-index/fachanwalt-strafrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-strafrecht.zip) |
| **fachanwalt-transport-speditionsrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-transport-speditionsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-transport-speditionsrecht.zip) |
| **fachanwalt-urheber-medienrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-urheber-medienrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-urheber-medienrecht.zip) |
| **fachanwalt-vergaberecht** | 37 | [Skills ansehen](skills-index/fachanwalt-vergaberecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-vergaberecht.zip) |
| **fachanwalt-verkehrsrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-verkehrsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |
| **fachanwalt-versicherungsrecht** | 38 | [Skills ansehen](skills-index/fachanwalt-versicherungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-versicherungsrecht.zip) |
| **fachanwalt-verwaltungsrecht** | 34 | [Skills ansehen](skills-index/fachanwalt-verwaltungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verwaltungsrecht.zip) |
| **factoring-recht** | 62 | [Skills ansehen](skills-index/factoring-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/factoring-recht.zip) |
| **fahrgastrechte** | 13 | [Skills ansehen](skills-index/fahrgastrechte.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fahrgastrechte.zip) |
| **fashion-law-moderecht** | 50 | [Skills ansehen](skills-index/fashion-law-moderecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fashion-law-moderecht.zip) |
| **festlandchina-wirtschaftsverkehr** | 101 | [Skills ansehen](skills-index/festlandchina-wirtschaftsverkehr.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/festlandchina-wirtschaftsverkehr.zip) |
| **fluggastrechte** | 84 | [Skills ansehen](skills-index/fluggastrechte.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |
| **forderungsmanagement-klagewerkstatt** | 47 | [Skills ansehen](skills-index/forderungsmanagement-klagewerkstatt.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| **forschungszulage-antragstellung** | 85 | [Skills ansehen](skills-index/forschungszulage-antragstellung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forschungszulage-antragstellung.zip) |
| **fortbestehensprognose** | 54 | [Skills ansehen](skills-index/fortbestehensprognose.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |
| **franchiserecht-praxis** | 78 | [Skills ansehen](skills-index/franchiserecht-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/franchiserecht-praxis.zip) |
| **gebrauchsmusterrecht** | 50 | [Skills ansehen](skills-index/gebrauchsmusterrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gebrauchsmusterrecht.zip) |
| **geldwaeschepraevention-aml-kyc** | 53 | [Skills ansehen](skills-index/geldwaeschepraevention-aml-kyc.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/geldwaeschepraevention-aml-kyc.zip) |
| **gesellschaftsgruender** | 99 | [Skills ansehen](skills-index/gesellschaftsgruender.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsgruender.zip) |
| **gesellschaftsrecht** | 100 | [Skills ansehen](skills-index/gesellschaftsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht.zip) |
| **gesellschaftsrecht-legal-english** | 50 | [Skills ansehen](skills-index/gesellschaftsrecht-legal-english.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht-legal-english.zip) |
| **gesellschaftsrechtliche-treuepflicht** | 99 | [Skills ansehen](skills-index/gesellschaftsrechtliche-treuepflicht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrechtliche-treuepflicht.zip) |
| **gewerblicher-rechtsschutz** | 62 | [Skills ansehen](skills-index/gewerblicher-rechtsschutz.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gewerblicher-rechtsschutz.zip) |
| **goae-gebuehrenordnung-aerzte** | 65 | [Skills ansehen](skills-index/goae-gebuehrenordnung-aerzte.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/goae-gebuehrenordnung-aerzte.zip) |
| **grosskanzlei-corporate-ma** | 196 | [Skills ansehen](skills-index/grosskanzlei-corporate-ma.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grosskanzlei-corporate-ma.zip) |
| **grundbuchamt-praxis** | 64 | [Skills ansehen](skills-index/grundbuchamt-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundbuchamt-praxis.zip) |
| **handelsrecht-hgb** | 56 | [Skills ansehen](skills-index/handelsrecht-hgb.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsrecht-hgb.zip) |
| **handelsregister-praxis** | 76 | [Skills ansehen](skills-index/handelsregister-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-praxis.zip) |
| **handelsvertreterrecht** | 104 | [Skills ansehen](skills-index/handelsvertreterrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsvertreterrecht.zip) |
| **hausarbeitenmacher** | 54 | [Skills ansehen](skills-index/hausarbeitenmacher.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |
| **haushaltsrecht-bho-bund-laender** | 300 | [Skills ansehen](skills-index/haushaltsrecht-bho-bund-laender.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/haushaltsrecht-bho-bund-laender.zip) |
| **hinweisgeberschutz-compliance** | 100 | [Skills ansehen](skills-index/hinweisgeberschutz-compliance.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hinweisgeberschutz-compliance.zip) |
| **hoai-leistungsphasen-praxis** | 386 | [Skills ansehen](skills-index/hoai-leistungsphasen-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hoai-leistungsphasen-praxis.zip) |
| **hochschulrecht-laender** | 99 | [Skills ansehen](skills-index/hochschulrecht-laender.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hochschulrecht-laender.zip) |
| **immobilienrechtspraxis** | 57 | [Skills ansehen](skills-index/immobilienrechtspraxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/immobilienrechtspraxis.zip) |
| **influencer-recht** | 69 | [Skills ansehen](skills-index/influencer-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/influencer-recht.zip) |
| **informationsfreiheit-presseauskunft** | 100 | [Skills ansehen](skills-index/informationsfreiheit-presseauskunft.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/informationsfreiheit-presseauskunft.zip) |
| **insiderrecht-compliance** | 56 | [Skills ansehen](skills-index/insiderrecht-compliance.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insiderrecht-compliance.zip) |
| **insolvenzforderungsanmeldungspruefung** | 54 | [Skills ansehen](skills-index/insolvenzforderungsanmeldungspruefung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzforderungsanmeldungspruefung.zip) |
| **insolvenzplan-starug-planwerkstatt** | 54 | [Skills ansehen](skills-index/insolvenzplan-starug-planwerkstatt.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzplan-starug-planwerkstatt.zip) |
| **insolvenzrecht** | 89 | [Skills ansehen](skills-index/insolvenzrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzrecht.zip) |
| **insolvenzverwaltung** | 51 | [Skills ansehen](skills-index/insolvenzverwaltung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzverwaltung.zip) |
| **internal-investigations-praxis** | 55 | [Skills ansehen](skills-index/internal-investigations-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/internal-investigations-praxis.zip) |
| **internationales-handelsrecht-lex-mercatoria** | 100 | [Skills ansehen](skills-index/internationales-handelsrecht-lex-mercatoria.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/internationales-handelsrecht-lex-mercatoria.zip) |
| **jurastudium** | 54 | [Skills ansehen](skills-index/jurastudium.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jurastudium.zip) |
| **juristische-sprache-deutsch-als-zweitsprache** | 50 | [Skills ansehen](skills-index/juristische-sprache-deutsch-als-zweitsprache.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/juristische-sprache-deutsch-als-zweitsprache.zip) |
| **jveg-kostenpruefer** | 53 | [Skills ansehen](skills-index/jveg-kostenpruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jveg-kostenpruefer.zip) |
| **kanzlei-allgemein** | 50 | [Skills ansehen](skills-index/kanzlei-allgemein.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-allgemein.zip) |
| **kanzlei-builder-hub** | 54 | [Skills ansehen](skills-index/kanzlei-builder-hub.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-builder-hub.zip) |
| **kanzlei-management** | 100 | [Skills ansehen](skills-index/kanzlei-management.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-management.zip) |
| **kanzlei-mandant-lifecycle** | 115 | [Skills ansehen](skills-index/kanzlei-mandant-lifecycle.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-mandant-lifecycle.zip) |
| **kartellrecht-marktabgrenzung-pruefung** | 305 | [Skills ansehen](skills-index/kartellrecht-marktabgrenzung-pruefung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kartellrecht-marktabgrenzung-pruefung.zip) |
| **ki-governance** | 53 | [Skills ansehen](skills-index/ki-governance.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-governance.zip) |
| **ki-richtlinie-kanzleien** | 55 | [Skills ansehen](skills-index/ki-richtlinie-kanzleien.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-richtlinie-kanzleien.zip) |
| **ki-vo-ai-act-pruefer** | 122 | [Skills ansehen](skills-index/ki-vo-ai-act-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-vo-ai-act-pruefer.zip) |
| **kommunalrecht-laender** | 160 | [Skills ansehen](skills-index/kommunalrecht-laender.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kommunalrecht-laender.zip) |
| **krankenhausrecht** | 67 | [Skills ansehen](skills-index/krankenhausrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krankenhausrecht.zip) |
| **krankenkassenrecht-krankenversicherung** | 81 | [Skills ansehen](skills-index/krankenkassenrecht-krankenversicherung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krankenkassenrecht-krankenversicherung.zip) |
| **kriegsdienstverweigerung-wehrdienst** | 133 | [Skills ansehen](skills-index/kriegsdienstverweigerung-wehrdienst.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kriegsdienstverweigerung-wehrdienst.zip) |
| **krisenfrueherkennung-starug** | 54 | [Skills ansehen](skills-index/krisenfrueherkennung-starug.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |
| **leasingrecht-praxis** | 59 | [Skills ansehen](skills-index/leasingrecht-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/leasingrecht-praxis.zip) |
| **legistik-werkstatt** | 246 | [Skills ansehen](skills-index/legistik-werkstatt.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |
| **liquiditaetsplanung** | 68 | [Skills ansehen](skills-index/liquiditaetsplanung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |
| **lobbyregister-bundestag** | 51 | [Skills ansehen](skills-index/lobbyregister-bundestag.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lobbyregister-bundestag.zip) |
| **luftrecht-flughafenrecht** | 120 | [Skills ansehen](skills-index/luftrecht-flughafenrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/luftrecht-flughafenrecht.zip) |
| **mandantenanfragen-assistent** | 54 | [Skills ansehen](skills-index/mandantenanfragen-assistent.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mandantenanfragen-assistent.zip) |
| **markenrecht-fashion-luxus** | 79 | [Skills ansehen](skills-index/markenrecht-fashion-luxus.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/markenrecht-fashion-luxus.zip) |
| **meinungspruefer** | 50 | [Skills ansehen](skills-index/meinungspruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/meinungspruefer.zip) |
| **memorandums-ersteller** | 54 | [Skills ansehen](skills-index/memorandums-ersteller.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |
| **methodenlehre-buergerliches-recht** | 125 | [Skills ansehen](skills-index/methodenlehre-buergerliches-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/methodenlehre-buergerliches-recht.zip) |
| **mietrecht** | 56 | [Skills ansehen](skills-index/mietrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mietrecht.zip) |
| **mittelstand-corporate-ma** | 100 | [Skills ansehen](skills-index/mittelstand-corporate-ma.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mittelstand-corporate-ma.zip) |
| **nachbarschaftsstreit-pruefer** | 54 | [Skills ansehen](skills-index/nachbarschaftsstreit-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |
| **nda-abgleich** | 85 | [Skills ansehen](skills-index/nda-abgleich.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-abgleich.zip) |
| **nda-verschwiegenheit-generator-checker** | 100 | [Skills ansehen](skills-index/nda-verschwiegenheit-generator-checker.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-verschwiegenheit-generator-checker.zip) |
| **nis2-cybersecurity-compliance** | 101 | [Skills ansehen](skills-index/nis2-cybersecurity-compliance.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nis2-cybersecurity-compliance.zip) |
| **normenkontrolle-bauleitplanung** | 91 | [Skills ansehen](skills-index/normenkontrolle-bauleitplanung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrolle-bauleitplanung.zip) |
| **normenkontrollrat-nkr** | 59 | [Skills ansehen](skills-index/normenkontrollrat-nkr.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrollrat-nkr.zip) |
| **notariat-alltag** | 66 | [Skills ansehen](skills-index/notariat-alltag.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/notariat-alltag.zip) |
| **oeffentliches-wirtschaftsrecht** | 100 | [Skills ansehen](skills-index/oeffentliches-wirtschaftsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/oeffentliches-wirtschaftsrecht.zip) |
| **ordnungswidrigkeitenrecht** | 100 | [Skills ansehen](skills-index/ordnungswidrigkeitenrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ordnungswidrigkeitenrecht.zip) |
| **parteienrecht-parteiorganisation** | 110 | [Skills ansehen](skills-index/parteienrecht-parteiorganisation.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/parteienrecht-parteiorganisation.zip) |
| **patentrecherche** | 54 | [Skills ansehen](skills-index/patentrecherche.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecherche.zip) |
| **patentrecht** | 59 | [Skills ansehen](skills-index/patentrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecht.zip) |
| **phishing-vorfall-pruefer** | 54 | [Skills ansehen](skills-index/phishing-vorfall-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |
| **preussisches-allgemeines-landrecht-pralr** | 199 | [Skills ansehen](skills-index/preussisches-allgemeines-landrecht-pralr.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/preussisches-allgemeines-landrecht-pralr.zip) |
| **private-equity-praxis** | 108 | [Skills ansehen](skills-index/private-equity-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/private-equity-praxis.zip) |
| **produktrecht** | 65 | [Skills ansehen](skills-index/produktrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/produktrecht.zip) |
| **prozessrecht** | 56 | [Skills ansehen](skills-index/prozessrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |
| **pruefungsrecht-hochschule** | 100 | [Skills ansehen](skills-index/pruefungsrecht-hochschule.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/pruefungsrecht-hochschule.zip) |
| **rechtsberatungsstelle** | 54 | [Skills ansehen](skills-index/rechtsberatungsstelle.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle.zip) |
| **rechtstheorie-rechtsphilosophie** | 70 | [Skills ansehen](skills-index/rechtstheorie-rechtsphilosophie.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtstheorie-rechtsphilosophie.zip) |
| **regulatorisches-recht** | 54 | [Skills ansehen](skills-index/regulatorisches-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/regulatorisches-recht.zip) |
| **rentenpruefer** | 50 | [Skills ansehen](skills-index/rentenpruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rentenpruefer.zip) |
| **robotik-recht** | 211 | [Skills ansehen](skills-index/robotik-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/robotik-recht.zip) |
| **roemisch-katholisches-kirchenrecht** | 100 | [Skills ansehen](skills-index/roemisch-katholisches-kirchenrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/roemisch-katholisches-kirchenrecht.zip) |
| **roemisches-recht** | 255 | [Skills ansehen](skills-index/roemisches-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/roemisches-recht.zip) |
| **schoeffen-handelsrichter-praxis** | 79 | [Skills ansehen](skills-index/schoeffen-handelsrichter-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schoeffen-handelsrichter-praxis.zip) |
| **schriftform-und-textform-bgb** | 53 | [Skills ansehen](skills-index/schriftform-und-textform-bgb.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftform-und-textform-bgb.zip) |
| **schulrecht-laender** | 100 | [Skills ansehen](skills-index/schulrecht-laender.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schulrecht-laender.zip) |
| **seerecht-schifffahrtsrecht** | 120 | [Skills ansehen](skills-index/seerecht-schifffahrtsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/seerecht-schifffahrtsrecht.zip) |
| **selbstvertreter-amtsgericht** | 115 | [Skills ansehen](skills-index/selbstvertreter-amtsgericht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/selbstvertreter-amtsgericht.zip) |
| **selbstvertreter-sozialgericht** | 155 | [Skills ansehen](skills-index/selbstvertreter-sozialgericht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/selbstvertreter-sozialgericht.zip) |
| **softwarerecht-de-eu-us** | 105 | [Skills ansehen](skills-index/softwarerecht-de-eu-us.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/softwarerecht-de-eu-us.zip) |
| **solo-selbststaendige-praxis** | 200 | [Skills ansehen](skills-index/solo-selbststaendige-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/solo-selbststaendige-praxis.zip) |
| **sozialversicherungsstatus-pruefer** | 101 | [Skills ansehen](skills-index/sozialversicherungsstatus-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/sozialversicherungsstatus-pruefer.zip) |
| **staatsanwaltschaft-praxis-einstieg** | 142 | [Skills ansehen](skills-index/staatsanwaltschaft-praxis-einstieg.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-praxis-einstieg.zip) |
| **startup-hr-personalabteilung-berlin** | 110 | [Skills ansehen](skills-index/startup-hr-personalabteilung-berlin.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/startup-hr-personalabteilung-berlin.zip) |
| **status-navigator-step-plan** | 35 | [Skills ansehen](skills-index/status-navigator-step-plan.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/status-navigator-step-plan.zip) |
| **steuerrecht-anwalt-und-berater** | 355 | [Skills ansehen](skills-index/steuerrecht-anwalt-und-berater.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/steuerrecht-anwalt-und-berater.zip) |
| **strafanzeige-vorbereiter** | 56 | [Skills ansehen](skills-index/strafanzeige-vorbereiter.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafanzeige-vorbereiter.zip) |
| **strafbefehl-verteidiger** | 55 | [Skills ansehen](skills-index/strafbefehl-verteidiger.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafbefehl-verteidiger.zip) |
| **strafzumessung** | 54 | [Skills ansehen](skills-index/strafzumessung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafzumessung.zip) |
| **strassenrecht-infrastruktur** | 100 | [Skills ansehen](skills-index/strassenrecht-infrastruktur.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenrecht-infrastruktur.zip) |
| **strassenverkehrsrecht-stvo** | 100 | [Skills ansehen](skills-index/strassenverkehrsrecht-stvo.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenverkehrsrecht-stvo.zip) |
| **subsumtions-pruefer** | 53 | [Skills ansehen](skills-index/subsumtions-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/subsumtions-pruefer.zip) |
| **tabellenreview-3d** | 84 | [Skills ansehen](skills-index/tabellenreview-3d.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tabellenreview-3d.zip) |
| **telekommunikationsrecht** | 57 | [Skills ansehen](skills-index/telekommunikationsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/telekommunikationsrecht.zip) |
| **tierschutzrecht** | 100 | [Skills ansehen](skills-index/tierschutzrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tierschutzrecht.zip) |
| **umweltrecht** | 54 | [Skills ansehen](skills-index/umweltrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht.zip) |
| **umweltschutzverband-verbandsklage** | 100 | [Skills ansehen](skills-index/umweltschutzverband-verbandsklage.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltschutzverband-verbandsklage.zip) |
| **urheberrecht-de-eu** | 63 | [Skills ansehen](skills-index/urheberrecht-de-eu.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/urheberrecht-de-eu.zip) |
| **urteilsbauer-relationsmacher** | 80 | [Skills ansehen](skills-index/urteilsbauer-relationsmacher.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/urteilsbauer-relationsmacher.zip) |
| **us-bankruptcy-code** | 100 | [Skills ansehen](skills-index/us-bankruptcy-code.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/us-bankruptcy-code.zip) |
| **us-copyright-registrierung-verlag** | 100 | [Skills ansehen](skills-index/us-copyright-registrierung-verlag.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/us-copyright-registrierung-verlag.zip) |
| **venture-capital-geber** | 105 | [Skills ansehen](skills-index/venture-capital-geber.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/venture-capital-geber.zip) |
| **verbraucher-rechtsstaat-alltag** | 66 | [Skills ansehen](skills-index/verbraucher-rechtsstaat-alltag.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucher-rechtsstaat-alltag.zip) |
| **verbraucherinsolvenz-schuldenbereinigung** | 26 | [Skills ansehen](skills-index/verbraucherinsolvenz-schuldenbereinigung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherinsolvenz-schuldenbereinigung.zip) |
| **verbraucherschutzrecht-pruefer** | 112 | [Skills ansehen](skills-index/verbraucherschutzrecht-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherschutzrecht-pruefer.zip) |
| **verbraucherschutzverband-durchsetzung** | 106 | [Skills ansehen](skills-index/verbraucherschutzverband-durchsetzung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherschutzverband-durchsetzung.zip) |
| **vereinsrecht-vereinsmanager** | 58 | [Skills ansehen](skills-index/vereinsrecht-vereinsmanager.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vereinsrecht-vereinsmanager.zip) |
| **verfassungsrecht** | 54 | [Skills ansehen](skills-index/verfassungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verfassungsrecht.zip) |
| **verhaeltnismaessigkeitspruefer** | 44 | [Skills ansehen](skills-index/verhaeltnismaessigkeitspruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verhaeltnismaessigkeitspruefer.zip) |
| **verkehr-infrastrukturrecht** | 54 | [Skills ansehen](skills-index/verkehr-infrastrukturrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehr-infrastrukturrecht.zip) |
| **verkehrsowi-verteidiger** | 54 | [Skills ansehen](skills-index/verkehrsowi-verteidiger.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip) |
| **verlagsrecht-buchpreisbindung** | 51 | [Skills ansehen](skills-index/verlagsrecht-buchpreisbindung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verlagsrecht-buchpreisbindung.zip) |
| **verlagsredaktion** | 104 | [Skills ansehen](skills-index/verlagsredaktion.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verlagsredaktion.zip) |
| **versammlungsrecht** | 55 | [Skills ansehen](skills-index/versammlungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versammlungsrecht.zip) |
| **versicherungsrecht** | 64 | [Skills ansehen](skills-index/versicherungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |
| **vertragsausfueller** | 54 | [Skills ansehen](skills-index/vertragsausfueller.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |
| **vertragsrecht** | 54 | [Skills ansehen](skills-index/vertragsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsrecht.zip) |
| **wahlkampfrecht-praxis** | 118 | [Skills ansehen](skills-index/wahlkampfrecht-praxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wahlkampfrecht-praxis.zip) |
| **wandeldarlehen-lebenszyklus** | 50 | [Skills ansehen](skills-index/wandeldarlehen-lebenszyklus.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wandeldarlehen-lebenszyklus.zip) |
| **weg-hausverwaltung** | 87 | [Skills ansehen](skills-index/weg-hausverwaltung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/weg-hausverwaltung.zip) |
| **weltraumrecht** | 102 | [Skills ansehen](skills-index/weltraumrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/weltraumrecht.zip) |
| **word-legal-ai-plugin-and-skill-for-german-lawyers** | 50 | [Skills ansehen](skills-index/word-legal-ai-plugin-and-skill-for-german-lawyers.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/word-legal-ai-plugin-and-skill-for-german-lawyers.zip) |
| **zitierweise-deutsches-recht** | 84 | [Skills ansehen](skills-index/zitierweise-deutsches-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zitierweise-deutsches-recht.zip) |
| **zwangsverwaltung-zvg** | 54 | [Skills ansehen](skills-index/zwangsverwaltung-zvg.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg.zip) |
| **zwangsvollstreckung** | 54 | [Skills ansehen](skills-index/zwangsvollstreckung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsvollstreckung.zip) |
