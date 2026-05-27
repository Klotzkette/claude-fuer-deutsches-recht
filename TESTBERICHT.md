# Testbericht — Klotzkette German Legal Skills

**Erstellt:** 2026-05-20  
**Stand des Repos:** Commit `7f7bdf5` (v2.0.3)  
**Plugins gesamt:** 52  
**Skills gesamt:** 361  
**Validatoren:** `validate-plugin-structure` OK, `validate-release-zips` OK (52 Plugin-ZIPs)

## Macro-Zustand

| Kennzahl | Wert |
|---|---|
| Plugin-Manifests gültig (JSON, Semver, ≤ 300 Zeichen Description) | 52 / 52 |
| SKILL.md-Frontmatter gültig (nur `name` + `description`) | 361 / 361 |
| Description ≤ 1024 Zeichen | 361 / 361 |
| Keine Zahl-Komma-Zahl-Sequenz in Description | 361 / 361 |
| Keine XML-Klammern in Description | 361 / 361 |
| `name` matched Verzeichnis | 361 / 361 |
| Code-Blöcke alle geschlossen | 361 / 361 |
| README erwähnt alle Plugins | 52 / 52 |
| ZIP-Größen unter 10-MB-Limit | 52 / 52 (Max 1016 KB) |
| Intra-Plugin-Skill-Refs aufgelöst | 133 / 133 |
| Skill-Body-Median | 6140 Bytes |
| Skill-Body-Streuung | 1488 – 24933 Bytes (Faktor 17) |
| Unique Keywords | 483 |
| Unique EuGH-Aktenzeichen | 20+ in Skills |

**Macro-Befund:** Alle Validatoren grün, keine Upload-Blocker. Beanstandungen unten sind **inhaltlich/qualitativ**, keine Cowork-Blocker.

---

## Die 20 schlimmsten Befunde

### Rang 1 — 32 Verweise auf nicht-mitgelieferte Reference-Dateien

`references/zitierweise.md` wird aus **30+ Skills** in 10+ Plugins referenziert (`vertragsrecht`, `datenschutzrecht`, `gewerblicher-rechtsschutz`, `regulatorisches-recht`, `kanzlei-builder-hub`, weitere). Die Datei existiert **nur im Repo-Root**, nicht in den einzelnen Plugin-ZIPs. Bei Solo-Installation eines Plugins in Cowork ist der Verweis **broken**. Workaround durch User: zusätzlich `zitierweise-deutsches-recht` installieren — aber das ist nicht dokumentiert.

### Rang 2 — 12 Plugins ohne `license`-Feld

Inkonsistente Lizenzierung. 40 Plugins haben `"license": "Apache-2.0 OR MIT"`, **12 haben kein license-Feld**:
- `kanzlei-builder-hub`, `regulatorisches-recht`, `rechtsberatungsstelle`, `datenschutzrecht`, `jurastudium`, `gewerblicher-rechtsschutz`, `arbeitsrecht`, `produktrecht`, `gesellschaftsrecht`, `ki-governance`, `vertragsrecht`, `prozessrecht`.

Für Drittnutzer rechtsunsicher (keine explizite Lizenzgewährung).

### Rang 3 — 9 Skills referenzieren Output-Dateien mit Umlauten (beA-Konflikt)

Das Plugin `anlagen-zu-schriftsaetzen` fordert explizit „**Datei-Benennung beA-tauglich: keine Umlaute**". Mehrere Skills produzieren aber Output-Dateinamen mit Umlauten:
- `kanzlei-allgemein/skills/mandantenakte-anlegen/SKILL.md`: Standardordner `03_schriftsätze/`
- `kanzlei-allgemein/skills/versand-vor-check/SKILL.md`, `bea-versand-pruefen`, `posteingang-ausgang`: Pfad `mandate/<az>/03_schriftsätze/`
- `fluggastrechte/skills/ticket-und-fluginformationen-erfassen/SKILL.md`: `nächste-schritte.md`
- `fluggastrechte/skills/ausnahmen-aussergewoehnliche-umstaende-pruefen/SKILL.md`: `außergewöhnlich-prüfung.md`
- `fortbestehensprognose/skills/ausloesendes-ereignis-erfassen/SKILL.md`: `auslösendes-ereignis.yaml`
- `fortbestehensprognose/skills/patronatserklaerung-extern-hart-erzeugen/SKILL.md`: `patronatserklärung-extern-hart.docx`
- `fortbestehensprognose/skills/stundungsanfrage-glaeubiger/SKILL.md`: `stundungsanfrage-<gläubiger>.docx`
- `liquiditaetsplanung/skills/liquiditaetsvorschau-3-6-12-monate/SKILL.md`: `liquiditäts-artefakt-<Firma>-KW<t>.md`
- `liquiditaetsplanung/skills/liquiditaetsvorschau-3wochen/SKILL.md`: gleiches Template
- `kanzlei-allgemein/skills/fristenbuch-fuehren/SKILL.md`: `fristen-übersicht.md`
- `kanzlei-builder-hub/skills/playbook-aus-eigenen-daten/SKILL.md`: `kündigungsschutz-arbeitnehmer.playbook.md` / `.fristen.yaml`
- `immobilienrechtspraxis/skills/vertragserstellung-musterbasiert/SKILL.md`: `Manuelle_Prüfung.md`

### Rang 4 — Cross-Plugin-Abhängigkeiten nicht dokumentiert

`sozialrecht-kanzlei` referenziert `kanzlei-allgemein/versand-vor-check`. `fortbestehensprognose` referenziert `liquiditaetsplanung/liquiditaetsvorschau-3-6-12-monate`. **Plugin-Manifests** enthalten kein `dependencies`-Feld. User installiert Solo-Plugin und wundert sich, dass Skill-Verweis ins Leere geht.

### Rang 5 — `fundstellenglattzieher` (kanzlei-builder-hub) hat 6× Verweis auf nicht existente `references/zitierweise.md`

Der Skill validiert Zitierweise gegen ein Reference-Dokument, das im Plugin-ZIP nicht enthalten ist. Lauffähig nur wenn `zitierweise-deutsches-recht` parallel installiert ist. Ohne dies nutzt der Skill ein imaginäres Dokument als Grundlage.

### Rang 6 — Skill-Längen-Streuung Faktor 17

Median 6140 Bytes. Kürzester Skill 1488 Bytes (`mietrecht/mietspiegel-quellen` — nur Trampolin zur Referenz), längster 24933 Bytes (`arbeitsrecht/interne-untersuchung`). Bei stark schwankender Qualität: kurze Skills fehlen oft an Konkretheit (z. B. die 17 `fachanwalt-*`-Plugin fuer Fachanwaltschaft-Skills mit je ~2000 Bytes).

### Rang 7 — Inkonsistente Versionsnummern in plugin.json vs Repo-Tag

Repo-Tag ist v2.0.x. Plugin-Manifests stehen aber bei 0.1.0 für die meisten neuen Plugins, 0.2.1 für `liquiditaetsplanung`. Keine erkennbare Strategie. Bei Update über `release-plugin-zips.yml` springt der Repo-Tag, die einzelnen Plugin-Versionen bleiben rückständig.

### Rang 8 — 17 nahezu identische `fachanwalt-*`-Plugin fuer Fachanwaltschaft-Plugins

Familienrecht, Strafrecht, Verkehrsrecht, Versicherungsrecht, Verwaltungsrecht, Bau-Architektenrecht, Erbrecht, Medizinrecht, Urheber-Medienrecht, IT-Recht, Bank-Kapitalmarktrecht, Internationales Wirtschaftsrecht, Migrationsrecht, Vergaberecht, Transport-Speditionsrecht, Agrarrecht, Sportrecht — alle mit einem einzigen Skill `fachanwalt-orientierung` (~2000 Bytes). 17 Marketplace-Einträge für wenig differenzierten Inhalt. Marketplace-Rauschen.

### Rang 9 — `liquiditaetsplanung` Plugin-Description nur 112 Zeichen

Andere Plugin-Descriptions sind 270–300 Zeichen. `liquiditaetsplanung` ist das größte Power-Plugin (1 MB ZIP, 5 Pflichtassets, 3 Skills) — die kurze Description liefert nicht genug Trigger-Worte.

### Rang 10 — Reference-Sync-Risiko (mehrere identische Kopien)

`references/zitierweise.md` existiert in **drei** Versionen:
- `references/zitierweise.md` (Repo-Root)
- `zitierweise-deutsches-recht/references/zitierweise.md`
- (Plus impliziert in `methodenlehre-buergerliches-recht/references/methodik-buergerliches-recht.md` mit Kreuzverweisen)

Ohne automatischen Sync-Hook (es gibt `scripts/sync-references.py`, aber kein CI-Pre-Commit) divergieren die Versionen schleichend.

### Rang 11 — Mietspiegel-Skill ist reines Trampolin (1488 Bytes)

`mietrecht/skills/mietspiegel-quellen/SKILL.md` ist der **kürzeste Skill im Repo**. Er sagt im Wesentlichen "siehe references/mietspiegel-quellen.md". Aber die Reference selbst ist 828 Zeilen — der Skill könnte intelligenter sein (z. B. konkretes Heraussuchen für eine Adresse).

### Rang 12 — Inkonsistente Slash-Command-Verweise

Manche Skills sagen `/<plugin>:kaltstart-interview`, andere `Skill \`kaltstart-interview\``, andere `den Skill kaltstart-interview`. Cowork-Slash-Resolution funktioniert nur mit `/<plugin>:<skill>` Schreibweise. Cross-Plugin-Verweise im Backtick-Format fühlen sich kaputt an.

### Rang 13 — Plugin-Manifest ohne `homepage` bei einigen Plugins

Stichprobe zeigt 49/52 mit `https://github.com/Klotzkette/claude-fuer-deutsches-recht`, einige ohne — bei Marketplace-Anzeige fehlt der Klick-Link.

### Rang 14 — 29 Plugins ohne `kaltstart-interview`

Bei 17 Plugin fuer Fachanwaltschaft-`fachanwalt-*` macht das Sinn (nur 1 Orientierungs-Skill). Aber **12 weitere Plugins** mit mehreren Skills haben keinen Kaltstart-Interview-Setup-Skill:
- `liquiditaetsplanung` (3 Skills)
- `fortbestehensprognose` (15 Skills) — **hat tatsaechlich einen**, aber `kanzlei-allgemein`, `mietrecht`, `verfassungsrecht`, `immobilienrechtspraxis`, `tabellenreview-3d`... — Inkonsistenz.

### Rang 15 — `prozessrecht/skills/anpassen/SKILL.md` mit 1794 Bytes verdächtig kurz

Erscheint im "kürzeste Skills"-Set. Möglicherweise Stub, der nie vervollständigt wurde.

### Rang 16 — Plugin-Description Trigger-Worte nicht systematisch

Manche Plugin-Descriptions sind Liste von Hauptgesetzen ("BGB §§ 558d ff."), andere Marketing-Stil ("Vollassistenz fuer ..."). Trigger-Suche durch Claude ist daher inkonsistent.

### Rang 17 — Konvention "Pflichtanlage zur Mandatsuebergabe" nicht standardisiert

Mehrere Skills erzeugen "Beleganhang" / "Audit-Trail" / "Pruefer-Paket" — aber jeder mit eigenem Schema. Plugin-übergreifende Standardisierung wäre Mehrwert.

### Rang 18 — `Praeambel` (5 Mal in fortbestehensprognose-Mustervorlagen) statt `Präambel`

Inkonsistenz mit dem Umlaut-Restoration-Sweep — die Mustervorlagen für Patronatserklärung, Forderungsverzicht, Rangrücktritt haben "Praeambel" als ASCII.

### Rang 19 — Anrede-Inkonsistenz Sie/Du innerhalb von Skills

Manche Skills mischen "Sie" (formell zum Mandanten) und "Du" (direkt zu Claude) im selben Body — verwirrend.

### Rang 20 — Keine README-Pflege je Plugin

Manche Plugins (`liquiditaetsplanung`, `forderungsmanagement-klagewerkstatt`) haben ein eigenes README.md, die meisten nicht. Inkonsistent.

---

## Die 20 besten Verbesserungsvorschläge

### 1. License-Feld nachziehen (Aufwand: 5 min)
12 Plugin-Manifests um `"license": "Apache-2.0 OR MIT"` ergänzen.

### 2. Output-Dateinamen konsequent ASCII (Aufwand: 30 min)
Ein einmaliger Sweep über Skills mit Umlauten in Backtick-Filenamen: `03_schriftsätze/` → `03_schriftsaetze/`, `nächste-schritte.md` → `naechste-schritte.md`, `auslösendes-ereignis.yaml` → `ausloesendes-ereignis.yaml`. Damit ist die im `anlagen-zu-schriftsaetzen`-Plugin selbst proklamierte beA-Konvention konsequent.

### 3. Repo-Root-Reference-Verweise durch Plugin-Hinweis ersetzen (Aufwand: 1 h)
In Skills die `references/zitierweise.md` aufrufen: ersetzen durch "Hauszitierweise: nach den Vorgaben des Plugins `zitierweise-deutsches-recht` (gesondert empfohlen)" — dann ist der Skill auch in Solo-Installation kohärent.

### 4. `dependencies`-Liste in Plugin-Manifests einführen (Aufwand: 2 h)
Erweitern um Feld `recommended_companions: ["kanzlei-allgemein", "zitierweise-deutsches-recht"]`. Cowork ignoriert das Feld, aber Mensch-Reader sieht die Abhängigkeiten.

### 5. CI-Hook gegen broken Pfad-Verweise (Aufwand: 1 h)
`scripts/validate-plugin-structure.mjs` um Check erweitern, der jeden Backtick-Pfad gegen tatsächlich existierende Dateien prüft. Verhindert Wiederkehr der bisher gefixten Bugs.

### 6. `liquiditaetsplanung` Plugin-Description erweitern (Aufwand: 10 min)
Von 112 auf ~280 Zeichen ausbauen — BGH-Schema, Padlet, Excel-Export erwähnen.

### 7. CI-Sync für identische Reference-Dateien (Aufwand: 30 min)
`scripts/sync-references.py` als Pre-Commit-Hook konfigurieren, damit Divergenzen zwischen `references/zitierweise.md` (Root) und `zitierweise-deutsches-recht/references/zitierweise.md` (Plugin-Kopie) immer aufgelöst werden.

### 8. Plugin-Versionen synchron zum Repo-Tag (Aufwand: 30 min)
Bei jedem Release-Tag (z. B. v2.1.0) alle 52 `plugin.json` automatisch auf dieselbe Version setzen. Konsistenz für Marketplace-Anzeige.

### 9. 17 `fachanwalt-*`-Plugins zu einem konsolidieren (Aufwand: 4 h)
Ein einziges `fachanwaltschaften-orientierung`-Plugin mit 17 Sub-Skills (`fachanwalt-orientierung-familienrecht`, …). Marketplace-Last drastisch reduziert, Maintenance einfacher.

### 10. Kaltstart-Interview-Skill für Mehr-Skill-Plugins nachziehen (Aufwand: 2 h)
`kanzlei-allgemein`, `mietrecht`, `verfassungsrecht`, `tabellenreview-3d`, `immobilienrechtspraxis` haben mehrere Skills, aber keinen Setup-Skill. Standardvorlage existiert (z. B. aus `sozialrecht-kanzlei`).

### 11. Plugin-Bundles im Marketplace einführen (Aufwand: 1 h)
Marketplace-Eintrag pro thematisches Bundle: "Sozialrechtskanzlei-Komplett" = `sozialrecht-kanzlei + kanzlei-allgemein + zitierweise-deutsches-recht + methodenlehre-buergerliches-recht`. Solo-Installation eines Bundles statt vier einzelner Plugins.

### 12. Mietspiegel-Skill konkret aufwerten (Aufwand: 2 h)
Statt nur Verweis-Trampolin: konkrete Schritt-für-Schritt-Anleitung "Adresse eingeben → richtigen Mietspiegel finden → Spanne ablesen → ortsuebliche Vergleichsmiete bestimmen". Der Reference-Inhalt liegt schon vor.

### 13. Plugin-Description-Stil standardisieren (Aufwand: 3 h)
Drei-Teile-Schema: (1) Was tut das Plugin, (2) Hauptgesetze/Standards, (3) Trigger-Worte. Pro Plugin ~280 Zeichen. Verbessert sowohl Marketplace-Anzeige als auch Claude-Trigger-Treffsicherheit.

### 14. Slash-Command-Konvention durchgängig nutzen (Aufwand: 1 h)
Cross-Plugin-Verweise nur als `/<plugin>:<skill>` schreiben. Intra-Plugin-Verweise nur als `\`skill-name\``. Damit ist die Resolution maschinell prüfbar.

### 15. Testakten verlinken in Skill-Bodies (Aufwand: 1 h)
`testakten/sozialrecht-rollstuhl-tannenberg/`, `testakten/fluggastrechte-familie-braeutigam/` etc. Skills könnten in einer „Beispiel"-Sektion auf die jeweilige Testakte verweisen — sofortige Anschauung.

### 16. CHANGELOG je Plugin (Aufwand: 2 h einmal, dann Pflege)
Statt Repo-CHANGELOG: ein kurzer Eintrag in jedem Plugin-Verzeichnis als `CHANGELOG.md` mit Datum + was sich geändert hat. Wichtiger Audit-Beleg bei Mandantsplanung.

### 17. Reference-Datum-Header in allen Referenzen (Aufwand: 30 min)
Jede `references/*.md` bekommt Header: "Stand: 2026-05, naechste Pruefung: 2026-08". Bei rollenden Gesetzesaenderungen prüfbarer Audit-Trigger.

### 18. `homepage`-Feld in allen Manifests einheitlich setzen (Aufwand: 10 min)
GitHub-URL bei jedem Plugin-Manifest gleich. Marketplace-Anzeige mit Klick-Link auf Repo.

### 19. Inkonsistenz „Praeambel/Präambel" und vergleichbare Restwoerter bereinigen (Aufwand: 30 min)
Letzter feiner Sweep nach dem Umlaut-Sweep — die fünf "Praeambel"-Vorkommen in fortbestehensprognose-Vertragstemplates zu "Präambel" konvertieren. Hauptanwendung ist Fließtext.

### 20. Skill-Längen-Korridor (Aufwand: kontinuierlich)
Soft-Konvention: kein Skill kürzer als 3000 Bytes, keiner länger als 15000 Bytes. Zu kurze Skills (Stubs) vertiefen, zu lange (Monolithen) splitten. Konsistenz für User-Erwartung.

---

## Zusammenfassung

**Hartes Befundbild:** 52 Plugins, 361 Skills, alle Validatoren grün — **kein Upload-Blocker**.

**Weiches Befundbild:** Die Plugin-Sammlung ist breit aufgestellt, mit klarer Plugin-Granularität (außer den 17 `fachanwalt-*`-Plugin fuer Fachanwaltschaft-Klonen, die konsolidierungsreif sind). Die größten Qualitätshebel liegen in Konsistenz (License-Felder, Slash-Command-Schreibweise, Output-Dateinamen-Konvention) und in der Sichtbarmachung von Cross-Plugin-Abhängigkeiten.

**Top-3-Priorität für die nächste Iteration:**
1. License-Feld nachziehen (Rang 2 → Vorschlag 1)
2. Output-Dateinamen ASCII (Rang 3 → Vorschlag 2)
3. Repo-Root-Reference-Verweise abkoppeln (Rang 1 + 5 → Vorschlag 3)
