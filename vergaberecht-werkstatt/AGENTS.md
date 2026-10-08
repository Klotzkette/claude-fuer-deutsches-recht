# AGENTS.md – Repository-Regeln für alle Agenten

Dieses Repository enthält die Vergaberecht-Werkstatt mit drei Plugins: `vergabestelle-behoerden` (öffentliche Auftraggeber), `bieter-unternehmen` (Bieter, Bewerber und Kanzleien auf Bieterseite) und `konkurrenten-rechtsschutz` (unterlegene Bieter, Konkurrenten und Zuschlagsgegner). Diese Datei gilt für jedes Werkzeug, das hier arbeitet — Codex, Perplexity, Cloud, Claude und jedes weitere Modell. Der vollständige Leitfaden steht in [`CLAUDE.md`](./CLAUDE.md).

## Repo-Spezifika

- Marktrolle zuerst klären: Vergabestelle, Bieter/Bewerber oder Konkurrent/Zuschlagsgegner? Davon hängt jede Antwort ab.
- Schwellenwerte und Rechtsregime trennen: oberhalb EU-Schwellenwert GWB Teil 4 plus passendes Spezialregime und Nachprüfung vor VK/OLG; unterhalb Haushalts-, UVgO-/VOB/A- und Landesrecht. Rechtsweg und Primärrechtsschutz im Unterschwellenbereich fall- und landesbezogen bestimmen.
- Bei Bauleistungen VOB/A Abschnitt 1, VOB/A-EU und VOB/A-VS trennscharf zuordnen.
- EU-Schwellenwerte ändern sich alle zwei Jahre und werden vor tragender Verwendung über [EUR-Lex](https://eur-lex.europa.eu/) oder die EU-Kommission verifiziert.
- Vergabesprache: nüchtern, klar, normgenau. Bei Bieter-Schriftsätzen präzise, ohne unnötige Schärfe.

## Gliederung und Nummerierung (verbindlich)

Diese Regel gilt dauerhaft und für jedes Werkzeug. Sie ist nicht verhandelbar.

- Ausschließlich dezimale Gliederung: `1`, dann `1.1`, dann `1.1.1`, dann `1.1.1.1` und so weiter, beliebig tief.
- Niemals römische Ziffern (`I`, `II`), Großbuchstaben (`A`, `B`, `C`), Kleinbuchstaben (`a`, `b`) oder gemischte Verlags-Gliederungen (`A. I. 1. a) aa)`).
- Leerzeile zwischen Gliederungspunkt und Inhalt sowie zwischen Gliederungsebenen.
- Einrückung sparsam.

Gilt für alle Vorlagen, Verträge, Memos, Schriftsätze und sonstigen Dokumente.

## Validatoren (vor jedem Commit)

- `python3 -m pip install -r requirements-dev.txt` — einmalig für Build- und Artefaktabhängigkeiten; die reinen Rechtsvalidatoren lesen OOXML ohne Pflichtpakete.
- `node scripts/validate-plugin-structure.mjs` — Plugin-Struktur, Slug-Regeln, plugin.json description maximal 300 Zeichen, marketplace.json description pro Plugin maximal 300 Zeichen, Testakten-Tabelle.
- `python3 scripts/validate-yaml-frontmatter.py` — Skill-Frontmatter, description maximal 1024 Zeichen, keine Komma-Zahlen nach Muster `\d,\d`, keine spitzen Klammern, keine doppelten Anführungszeichen, keine Symbolzeichen wie Paragraphenzeichen, Haken, Stern oder Pfeil.
- `python3 scripts/validate-skill-discovery.py` — Skill-Beschreibungen eindeutig halten, Import-Boilerplate ausschließen und Sichtbarkeit in Plugin-README und Skill-Index sichern.
- `python3 scripts/sync-references.py --check` — identische gemeinsame Referenzen in allen drei Plugin-ZIPs sichern.
- `python3 scripts/validate-rechtsstand-2026.py` — aktuellen VK-/OLG-Rechtsstand, richtige Normzuordnung und geprüfte Fallanker sichern.
- `python3 scripts/validate-system-integration.py` — Feldautorität, Angebotsfreeze, Beweiskette und aktuelle System-/Formatrechtsprechung in allen drei Rollen sichern.
- `python3 scripts/validate-doc-links.py` und `python3 scripts/validate-navigation.py` — lokale Links, globale Menüs, Einzeldateizugriff und vollständige Release-Download-Abdeckung sichern.
- `python3 scripts/run-smoke-tests.py --quick` — konsolidierter schneller Lauf ohne Release-ZIP- und Git-Metadatenprüfung.

Description-Felder dürfen keine Abruf-/Auslese-Wörter aus der verbotenen Wortfamilie enthalten. Bei Platzhaltern eckige Klammern verwenden, nicht spitze Klammern. Plugin-Slugs maximal 64 Zeichen, nur `a-z`, `0-9` und Bindestrich.

## Oeffentliche Einbettung

- Root-Dateien und `source-import.json` werden durch die uebergeordnete Integration gepflegt; hier nicht veraendern.
- Technische Ziele zentral in `scripts/public_release.py`; Installation ueber `@klotzkette-german-legal-skills`, lokale Marketplace-Quellen bleiben relativ.
- Vor Abschluss zusaetzlich `python3 scripts/sync-public-entrypoints.py --check` und `python3 scripts/validate-public-integration.py` ausfuehren.
- Schnellstarts und Unified-Mini-Prompts: maximal 7500 UTF-8-Bytes, nicht nur Zeichen.
- Standalone-Prompts einzeln als Markdown, nicht im Plugin- oder Skills-ZIP; weitere Regeln und Umbenennungen stehen in `PUBLIC-INTEGRATION.md`.
- Vor jeder Testakten-PDF-/ZIP-Downloadgruppe steht der unveraenderte deutsche und englische Warnhinweis aus `testakten/README.txt`. Beide Akten-ZIP-Varianten und Sammelpakete mit Testakten enthalten diese Datei auf ZIP-Wurzelebene. Keine Warnhinweise in PDFs einbauen.

## Autorenkontakt

- Name: `Klotzkette`
- E-Mail: `39582916+Klotzkette@users.noreply.github.com`
- Niemals Modell-, Werkzeug- oder Assistenz-Erwähnung in Commits.
