# Kanzleiprofil und Hausstil

Die Schrift eines Enddokuments ist eine Eigenschaft der Kanzlei, nicht dieses Repositorys. Deshalb nennt kein Skill, Prompt oder Referenztext in diesem Repository eine konkrete Hausschrift. Stattdessen gilt überall dieselbe Formulierung: „Hausschrift laut Kanzleiprofil, ohne Profil Times New Roman 11 pt". Der neutrale Standard dahinter steht an genau einer Stelle, in `hausstil.json` im Repository-Root.

## 1 Kanzleiprofil anlegen

Jede Kanzlei setzt ihre Hausschrift in ihrer eigenen `CLAUDE.md`, in der Regel in der benutzerweiten Datei `~/.claude/CLAUDE.md`, die Claude Code in jeder Sitzung lädt. Der Abschnitt heißt „Kanzleiprofil" und hat Vorrang vor dem neutralen Standard:

```markdown
## Kanzleiprofil ([Name der Kanzlei])

- Hausschrift für Enddokumente: [Hausschrift], 11 pt. Dieses Profil geht dem neutralen Standard aus hausstil.json vor.
- Fehlt die Hausschrift auf dem System, wird die tatsächlich verwendete Ersatzschrift im Exporthinweis genannt.
```

Mehr ist nicht nötig. Alle Skills lesen die Hausschrift aus diesem Abschnitt; der Standard aus `hausstil.json` greift nur, wenn kein Profil vorliegt.

## 2 Standard ändern

Der neutrale Standard wird ausschließlich in `hausstil.json` geändert. Danach werden die Texte einmal nachgezogen:

```bash
python3 scripts/inject-ausformulierungspflicht.py        # Formatblock in den Skills
python3 scripts/apply-hausstil.py                        # Freitext in Skills, Prompts, References, Eval-Rubriken
python3 scripts/refresh-pruefhashes-nach-hausstil.py     # Prüfhashes in quality/evals nachziehen, nur für rein mechanische Änderungen
python3 scripts/audit-hausstil.py                        # meldet jede Schriftnennung außerhalb der Phrase und der Ausnahmen
```

`apply-hausstil.py --check` und `refresh-pruefhashes-nach-hausstil.py --check` zeigen die anstehenden Änderungen, ohne zu schreiben. Alle Skripte sind idempotent.

Die Prüfprofile unter `quality/evals` halten SHA-256-Hashes der geprüften Prompts und Skills fest; `quality-lab.py audit` und der Werkstatt-Generator brechen ab, wenn ein Hash nicht mehr zur Datei passt. Das Nachzieh-Skript vergleicht jede geprüfte Datei mit ihrem Stand im letzten Commit und aktualisiert den Hash nur, wenn sich die Datei allein durch die Hausstil-Phrase und den Formatblock unterscheidet; der Prüfvermerk bekommt dann einen datierten Eintrag in seiner Änderungsliste. Fachlich geänderte Dateien und Hashes, die schon vorher nicht passten, bleiben stehen und werden mit Pfad gemeldet. Deshalb läuft das Skript vor dem Commit, solange der letzte Commit noch den geprüften Stand enthält.

## 3 Ausnahmen

Wo ein Text bewusst eine andere Schrift nennt, steht der Pfad mit Grund unter `ausnahmen` in `hausstil.json`: Testakten-Builder, die fremde Kanzleiakten nachbilden, das amtliche Layout der Bundestags-Drucksache, Laienhilfen mit gerichtsüblicher Schrift, aufgezeichnete Prüfprotokolle und die Historie. Fremdvorgaben, die als wörtliche Textstelle überall zulässig sind, stehen unter `fremdvorgaben` (zum Beispiel der amtliche Hausstil der Ministerien für Referentenentwürfe oder der Anlagenstempel auf Beweisanlagen). `hausstil.json` selbst ist immer ausgenommen. Schnellstart- und Hauptproblem-Prompts (`*-schnellstart.md`, `*-hauptproblem.md` und ihre byteidentischen TXT-Kopien) haben eine Bytegrenze von 7500 Bytes (`scripts/prompt-limits.json`, `scripts/test-schwerpunkt-coverage.py`) und tragen deshalb statt der langen Phrase nur die Kurzform „Kanzleihausschrift“; `apply-hausstil.py` setzt sie automatisch. Der Validator meldet jede andere Schriftnennung mit Datei und Zeile; er prüft Markdown, Text, JSON, Python, JavaScript, YAML und Shell, nicht aber HTML und CSS von Web-Oberflächen.

Die DOCX- und ODT-Builder außerhalb der Testakten-Nachbildungen (`scripts/generate-formatvorlagen.py`, `scripts/build-bauwirtschaft-werkstatt-handbuch.py`, `scripts/render-startup-gruender-werkstatt.py`, `scripts/render-registerwerkstaetten.py`, `scripts/build-ki-verordnung-hochrisiko-pruefer.py`) lesen Schrift und Grundgröße aus `hausstil.json` (`hausstil.lade_hausstil()`, `hausstil.groesse_in_punkt()`); ein Test wacht darüber. Die übrigen Builder unter `scripts/` bilden fremde Kanzleiakten nach und bleiben Ausnahme.
