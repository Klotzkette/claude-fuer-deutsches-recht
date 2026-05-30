# Skill-Gesamtuebersicht

Automatisch generierte Gesamtuebersicht aller **2655 Skills** in **108 Plugins**.

Stand: `v50.9.1`.

## ⬇️ Alle Skills auf einmal herunterladen

| Paket | Inhalt | Download |
| --- | --- | --- |
| **Alle Skills (kompakt)** | Alle 108 Plugin-ZIPs in einem Archiv (ca. 11 MB) | [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) |
| **Komplettpaket (alles)** | Plugins + Testakten + Uebersichten (ca. 80 MB) | [`alles-komplettpaket.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alles-komplettpaket.zip) |

Das erste Paket reicht, wenn man nur die Prompts (Skills) braucht. Das zweite enthaelt zusaetzlich die 63 Testakten und alle Repo-Uebersichten.

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

Die Detailseiten liegen unter [`skills-index/`](skills-index/) -- eine eigene `.md`-Datei pro Plugin. So bleibt diese Hauptseite klein und laedt schnell, statt mit 2655 Tabellenzeilen den Browser-Renderer von GitHub zu ueberfordern.

## Alle Plugins

Pro Plugin: Klick auf den Namen oeffnet die Detailseite mit allen Skills, Beschreibungen und Einzel-Downloads. **ZIP** laedt die komplette Plugin-Sammlung direkt.

| Plugin | Skills | Detailseite | ZIP |
| --- | ---: | --- | --- |
| **aktenaufbereiter-strafrecht** | 2 | [Skills ansehen](skills-index/aktenaufbereiter-strafrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenaufbereiter-strafrecht.zip) |
| **aktenauszug-gerichtsverfahren** | 21 | [Skills ansehen](skills-index/aktenauszug-gerichtsverfahren.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |
| **anlagen-zu-schriftsaetzen** | 2 | [Skills ansehen](skills-index/anlagen-zu-schriftsaetzen.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |
| **arbeitsrecht** | 80 | [Skills ansehen](skills-index/arbeitsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitsrecht.zip) |
| **arbeitszeugnis-analyse** | 32 | [Skills ansehen](skills-index/arbeitszeugnis-analyse.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |
| **aussenwirtschaft-zoll-sanktionen** | 20 | [Skills ansehen](skills-index/aussenwirtschaft-zoll-sanktionen.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aussenwirtschaft-zoll-sanktionen.zip) |
| **barrierefreiheit-web-checker** | 12 | [Skills ansehen](skills-index/barrierefreiheit-web-checker.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/barrierefreiheit-web-checker.zip) |
| **bav-strategie-konzern** | 18 | [Skills ansehen](skills-index/bav-strategie-konzern.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bav-strategie-konzern.zip) |
| **bereicherungs-und-anfechtungsrecht-pruefer** | 98 | [Skills ansehen](skills-index/bereicherungs-und-anfechtungsrecht-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bereicherungs-und-anfechtungsrecht-pruefer.zip) |
| **berufsrecht-ki-vertragspruefung** | 14 | [Skills ansehen](skills-index/berufsrecht-ki-vertragspruefung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-ki-vertragspruefung.zip) |
| **betreuungsrecht** | 8 | [Skills ansehen](skills-index/betreuungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betreuungsrecht.zip) |
| **bgb-at-pruefer** | 53 | [Skills ansehen](skills-index/bgb-at-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-at-pruefer.zip) |
| **common-law-kompass** | 19 | [Skills ansehen](skills-index/common-law-kompass.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/common-law-kompass.zip) |
| **corporate-kanzlei** | 48 | [Skills ansehen](skills-index/corporate-kanzlei.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/corporate-kanzlei.zip) |
| **datenschutzrecht** | 21 | [Skills ansehen](skills-index/datenschutzrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutzrecht.zip) |
| **dsa-dma-digitalregulierung** | 10 | [Skills ansehen](skills-index/dsa-dma-digitalregulierung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dsa-dma-digitalregulierung.zip) |
| **einfache-leichte-sprache-jura** | 6 | [Skills ansehen](skills-index/einfache-leichte-sprache-jura.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip) |
| **email-umformulierer-berufsrecht** | 21 | [Skills ansehen](skills-index/email-umformulierer-berufsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/email-umformulierer-berufsrecht.zip) |
| **energierecht** | 14 | [Skills ansehen](skills-index/energierecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/energierecht.zip) |
| **europarecht-kompass** | 19 | [Skills ansehen](skills-index/europarecht-kompass.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/europarecht-kompass.zip) |
| **fachanwalt-agrarrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-agrarrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-agrarrecht.zip) |
| **fachanwalt-arbeitsrecht** | 17 | [Skills ansehen](skills-index/fachanwalt-arbeitsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-arbeitsrecht.zip) |
| **fachanwalt-bank-kapitalmarktrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-bank-kapitalmarktrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-bank-kapitalmarktrecht.zip) |
| **fachanwalt-bau-architektenrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-bau-architektenrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-bau-architektenrecht.zip) |
| **fachanwalt-erbrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-erbrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-erbrecht.zip) |
| **fachanwalt-familienrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-familienrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-familienrecht.zip) |
| **fachanwalt-gewerblicher-rechtsschutz** | 14 | [Skills ansehen](skills-index/fachanwalt-gewerblicher-rechtsschutz.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-gewerblicher-rechtsschutz.zip) |
| **fachanwalt-handels-gesellschaftsrecht** | 13 | [Skills ansehen](skills-index/fachanwalt-handels-gesellschaftsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-handels-gesellschaftsrecht.zip) |
| **fachanwalt-insolvenz-sanierungsrecht** | 13 | [Skills ansehen](skills-index/fachanwalt-insolvenz-sanierungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-insolvenz-sanierungsrecht.zip) |
| **fachanwalt-internationales-wirtschaftsrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-internationales-wirtschaftsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-internationales-wirtschaftsrecht.zip) |
| **fachanwalt-it-recht** | 16 | [Skills ansehen](skills-index/fachanwalt-it-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-it-recht.zip) |
| **fachanwalt-medizinrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-medizinrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-medizinrecht.zip) |
| **fachanwalt-miet-wohnungseigentumsrecht** | 13 | [Skills ansehen](skills-index/fachanwalt-miet-wohnungseigentumsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-miet-wohnungseigentumsrecht.zip) |
| **fachanwalt-migrationsrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-migrationsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-migrationsrecht.zip) |
| **fachanwalt-sozialrecht** | 33 | [Skills ansehen](skills-index/fachanwalt-sozialrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-sozialrecht.zip) |
| **fachanwalt-sportrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-sportrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-sportrecht.zip) |
| **fachanwalt-strafrecht** | 20 | [Skills ansehen](skills-index/fachanwalt-strafrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-strafrecht.zip) |
| **fachanwalt-transport-speditionsrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-transport-speditionsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-transport-speditionsrecht.zip) |
| **fachanwalt-urheber-medienrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-urheber-medienrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-urheber-medienrecht.zip) |
| **fachanwalt-vergaberecht** | 16 | [Skills ansehen](skills-index/fachanwalt-vergaberecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-vergaberecht.zip) |
| **fachanwalt-verkehrsrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-verkehrsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |
| **fachanwalt-versicherungsrecht** | 16 | [Skills ansehen](skills-index/fachanwalt-versicherungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-versicherungsrecht.zip) |
| **fachanwalt-verwaltungsrecht** | 19 | [Skills ansehen](skills-index/fachanwalt-verwaltungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verwaltungsrecht.zip) |
| **fluggastrechte** | 13 | [Skills ansehen](skills-index/fluggastrechte.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |
| **forderungsmanagement-klagewerkstatt** | 4 | [Skills ansehen](skills-index/forderungsmanagement-klagewerkstatt.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| **fortbestehensprognose** | 16 | [Skills ansehen](skills-index/fortbestehensprognose.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |
| **geldwaeschepraevention-aml-kyc** | 22 | [Skills ansehen](skills-index/geldwaeschepraevention-aml-kyc.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/geldwaeschepraevention-aml-kyc.zip) |
| **gesellschaftsgruender** | 37 | [Skills ansehen](skills-index/gesellschaftsgruender.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsgruender.zip) |
| **gesellschaftsrecht** | 21 | [Skills ansehen](skills-index/gesellschaftsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht.zip) |
| **gesellschaftsrecht-legal-english** | 32 | [Skills ansehen](skills-index/gesellschaftsrecht-legal-english.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht-legal-english.zip) |
| **gewerblicher-rechtsschutz** | 18 | [Skills ansehen](skills-index/gewerblicher-rechtsschutz.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gewerblicher-rechtsschutz.zip) |
| **grosskanzlei-corporate-ma** | 56 | [Skills ansehen](skills-index/grosskanzlei-corporate-ma.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grosskanzlei-corporate-ma.zip) |
| **hausarbeitenmacher** | 23 | [Skills ansehen](skills-index/hausarbeitenmacher.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |
| **immobilienrechtspraxis** | 8 | [Skills ansehen](skills-index/immobilienrechtspraxis.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/immobilienrechtspraxis.zip) |
| **weg-hausverwaltung** | 28 | [Skills ansehen](skills-index/weg-hausverwaltung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/weg-hausverwaltung.zip) |
| **insolvenzforderungsanmeldungspruefung** | 21 | [Skills ansehen](skills-index/insolvenzforderungsanmeldungspruefung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzforderungsanmeldungspruefung.zip) |
| **insolvenzplan-starug-planwerkstatt** | 27 | [Skills ansehen](skills-index/insolvenzplan-starug-planwerkstatt.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzplan-starug-planwerkstatt.zip) |
| **insolvenzrecht** | 16 | [Skills ansehen](skills-index/insolvenzrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzrecht.zip) |
| **insolvenzverwaltung** | 45 | [Skills ansehen](skills-index/insolvenzverwaltung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzverwaltung.zip) |
| **jurastudium** | 23 | [Skills ansehen](skills-index/jurastudium.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jurastudium.zip) |
| **word-legal-ai-plugin-and-skill-for-german-lawyers** | 38 | [Skills ansehen](skills-index/word-legal-ai-plugin-and-skill-for-german-lawyers.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/word-legal-ai-plugin-and-skill-for-german-lawyers.zip) |
| **jveg-kostenpruefer** | 20 | [Skills ansehen](skills-index/jveg-kostenpruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jveg-kostenpruefer.zip) |
| **kanzlei-allgemein** | 48 | [Skills ansehen](skills-index/kanzlei-allgemein.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-allgemein.zip) |
| **kanzlei-builder-hub** | 13 | [Skills ansehen](skills-index/kanzlei-builder-hub.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-builder-hub.zip) |
| **kartellrecht-marktabgrenzung-pruefung** | 25 | [Skills ansehen](skills-index/kartellrecht-marktabgrenzung-pruefung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kartellrecht-marktabgrenzung-pruefung.zip) |
| **ki-governance** | 11 | [Skills ansehen](skills-index/ki-governance.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-governance.zip) |
| **ki-richtlinie-kanzleien** | 27 | [Skills ansehen](skills-index/ki-richtlinie-kanzleien.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-richtlinie-kanzleien.zip) |
| **ki-vo-ai-act-pruefer** | 48 | [Skills ansehen](skills-index/ki-vo-ai-act-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-vo-ai-act-pruefer.zip) |
| **krisenfrueherkennung-starug** | 20 | [Skills ansehen](skills-index/krisenfrueherkennung-starug.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |
| **legistik-werkstatt** | 26 | [Skills ansehen](skills-index/legistik-werkstatt.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |
| **liquiditaetsplanung** | 4 | [Skills ansehen](skills-index/liquiditaetsplanung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |
| **lobbyregister-bundestag** | 51 | [Skills ansehen](skills-index/lobbyregister-bundestag.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lobbyregister-bundestag.zip) |
| **mandantenanfragen-assistent** | 15 | [Skills ansehen](skills-index/mandantenanfragen-assistent.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mandantenanfragen-assistent.zip) |
| **markenrecht-fashion-luxus** | 32 | [Skills ansehen](skills-index/markenrecht-fashion-luxus.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/markenrecht-fashion-luxus.zip) |
| **meinungspruefer** | 36 | [Skills ansehen](skills-index/meinungspruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/meinungspruefer.zip) |
| **memorandums-ersteller** | 2 | [Skills ansehen](skills-index/memorandums-ersteller.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |
| **methodenlehre-buergerliches-recht** | 20 | [Skills ansehen](skills-index/methodenlehre-buergerliches-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/methodenlehre-buergerliches-recht.zip) |
| **mietrecht** | 16 | [Skills ansehen](skills-index/mietrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mietrecht.zip) |
| **nachbarschaftsstreit-pruefer** | 20 | [Skills ansehen](skills-index/nachbarschaftsstreit-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |
| **mittelstand-corporate-ma** | 54 | [Skills ansehen](skills-index/mittelstand-corporate-ma.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mittelstand-corporate-ma.zip) |
| **nda-abgleich** | 2 | [Skills ansehen](skills-index/nda-abgleich.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-abgleich.zip) |
| **normenkontrolle-bauleitplanung** | 22 | [Skills ansehen](skills-index/normenkontrolle-bauleitplanung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrolle-bauleitplanung.zip) |
| **patentrecherche** | 14 | [Skills ansehen](skills-index/patentrecherche.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecherche.zip) |
| **phishing-vorfall-pruefer** | 2 | [Skills ansehen](skills-index/phishing-vorfall-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |
| **produktrecht** | 10 | [Skills ansehen](skills-index/produktrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/produktrecht.zip) |
| **prozessrecht** | 26 | [Skills ansehen](skills-index/prozessrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |
| **rechtsberatungsstelle** | 17 | [Skills ansehen](skills-index/rechtsberatungsstelle.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle.zip) |
| **regulatorisches-recht** | 13 | [Skills ansehen](skills-index/regulatorisches-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/regulatorisches-recht.zip) |
| **schriftform-und-textform-bgb** | 23 | [Skills ansehen](skills-index/schriftform-und-textform-bgb.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftform-und-textform-bgb.zip) |
| **selbstvertreter-amtsgericht** | 86 | [Skills ansehen](skills-index/selbstvertreter-amtsgericht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/selbstvertreter-amtsgericht.zip) |
| **selbstvertreter-sozialgericht** | 80 | [Skills ansehen](skills-index/selbstvertreter-sozialgericht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/selbstvertreter-sozialgericht.zip) |
| **steuerrecht-anwalt-und-berater** | 203 | [Skills ansehen](skills-index/steuerrecht-anwalt-und-berater.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/steuerrecht-anwalt-und-berater.zip) |
| **strafbefehl-verteidiger** | 21 | [Skills ansehen](skills-index/strafbefehl-verteidiger.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafbefehl-verteidiger.zip) |
| **strafzumessung** | 25 | [Skills ansehen](skills-index/strafzumessung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafzumessung.zip) |
| **subsumtions-pruefer** | 31 | [Skills ansehen](skills-index/subsumtions-pruefer.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/subsumtions-pruefer.zip) |
| **tabellenreview-3d** | 21 | [Skills ansehen](skills-index/tabellenreview-3d.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tabellenreview-3d.zip) |
| **umweltrecht** | 16 | [Skills ansehen](skills-index/umweltrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht.zip) |
| **urteilsbauer-relationsmacher** | 25 | [Skills ansehen](skills-index/urteilsbauer-relationsmacher.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/urteilsbauer-relationsmacher.zip) |
| **verfassungsrecht** | 9 | [Skills ansehen](skills-index/verfassungsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verfassungsrecht.zip) |
| **verkehr-infrastrukturrecht** | 13 | [Skills ansehen](skills-index/verkehr-infrastrukturrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehr-infrastrukturrecht.zip) |
| **verkehrsowi-verteidiger** | 21 | [Skills ansehen](skills-index/verkehrsowi-verteidiger.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip) |
| **verlagsredaktion** | 28 | [Skills ansehen](skills-index/verlagsredaktion.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verlagsredaktion.zip) |
| **vertragsausfueller** | 15 | [Skills ansehen](skills-index/vertragsausfueller.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |
| **vertragsrecht** | 17 | [Skills ansehen](skills-index/vertragsrecht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsrecht.zip) |
| **wandeldarlehen-lebenszyklus** | 33 | [Skills ansehen](skills-index/wandeldarlehen-lebenszyklus.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wandeldarlehen-lebenszyklus.zip) |
| **zitierweise-deutsches-recht** | 2 | [Skills ansehen](skills-index/zitierweise-deutsches-recht.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zitierweise-deutsches-recht.zip) |
| **zwangsverwaltung-zvg** | 24 | [Skills ansehen](skills-index/zwangsverwaltung-zvg.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg.zip) |
| **zwangsvollstreckung** | 20 | [Skills ansehen](skills-index/zwangsvollstreckung.md) | [Download](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsvollstreckung.zip) |
