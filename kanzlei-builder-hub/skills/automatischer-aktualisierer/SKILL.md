---
name: automatischer-aktualisierer
description: "Plugins und Skills in der KI-Anwaltskanzlei automatisch aktualisieren: neue Norm-Versionen, Rechtsprechungsaenderungen. Normen: technisch/intern. Prüfraster: aeltere Versionen identifizieren, Update-Prioritaet, Rollback-Option. Output: Aktualisierungsprotokoll. Abgrenzung: nicht manuelle Skill-Verwaltung im Kanzlei Builder Hub."
---

# /automatischer-aktualisierer — Automatische Aktualisierung mit Diff-Review

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 51 Mindestversicherung sofort, FAO § 4 Fachanwalt-Antrag 3-Jahres-Frist (10 % Mindestumfang), GwG-Risikoanalyse jährlich, beA Pflichtnutzung seit 01.01.2022.
- Tragende Normen verifizieren: BRAO §§ 5, 7, 14, 27, 43 ff., 49b, 51 (Berufshaftpflicht), BORA, FAO, RVG §§ 1 ff., GwG §§ 2, 10, 11, 43 (Kanzlei als Verpflichteter), DSGVO, beA-Bedingungen, Steuerrecht (EStG, UStG, GewStG) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Kanzleigründer, Kammer, BRAK, Versicherer (Berufshaftpflicht), Mandant, Steuerberater, IT-Dienstleister (beA, RA-MICRO/AnNoText).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Kanzleihandbuch, Datenschutz-Konzept, Geldwäsche-Risikoanalyse, Mandatsvertrag, Honorarvereinbarung, Versicherungspolice, Sozietätsvertrag, beA-Konfiguration — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Laufende Konfiguration: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` → installierte Skills (mit Versionsnummer/Commit-SHA), Update-Einstellungen (benachrichtigen / manuell).
- Optional: `--apply` um alle genehmigten Updates zu installieren; `--rollback [skill]` um auf die vorherige Version zurückzusetzen.

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht; unkontrollierte Skill-Updates können Mandatsdaten gefährden.
- **Art. 32 DSGVO** — Pflicht zu technisch-organisatorischen Maßnahmen; Aktualisierungen von in Mandatsprozessen eingesetzten Werkzeugen sind sicherheitstechnisch zu überwachen.
- **§ 50 BRAO** — Pflicht zur Aktenführung; das Installationsprotokoll dokumentiert alle Versionsänderungen als Teil der Kanzleiorganisation.
- **AI Act Art. 26** — Deployer-Pflichten bei Hochrisiko-KI: Änderungen am KI-System sind zu überwachen und zu dokumentieren.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Ablauf

### Schritt 1: Jeden installierten Skill prüfen

Für jeden Skill in der Installationsliste:

- Aktuellen Commit-SHA von der Quellregistry abrufen (exakter Commit, nicht ein Tag oder Branch-Head — Tags sind veränderbar und können nachträglich vom Publisher überschrieben werden; nur Commit-SHAs sind unveränderlich).
- Mit dem beim Installationszeitpunkt gespeicherten SHA vergleichen.
- Bei Abweichung: Update verfügbar.

### Schritt 2: Diff und Vertrauensprüfung

Für jedes Update den vollständigen Diff anzeigen:

```diff
### [skill-name] — [installierter SHA] → [neuester SHA]

## Änderungen in SKILL.md
[Unified Diff]

## Änderungen in ausloeser/ausloeser.json
[Unified Diff — ACHTUNG: Automatische Auslöser können beliebigen Code ausführen]

## Änderungen in .mcp.json
[Unified Diff — ACHTUNG: MCP-Server laufen mit Ihren Anmeldedaten]

## Weitere Dateien
[Liste hinzugefügter/entfernter/geänderter Dateien mit Diffs]
```

Dann die Vertrauensprüfung durchführen:
- **Hat sich `ausloeser/ausloeser.json` (hooks/hooks.json) geändert?** Automatische Auslöser können beliebige Shell-Befehle auf Ereignisse ausführen. Diff prominent anzeigen und Nutzer bestätigen lassen, dass er versteht, was die neuen Auslöser tun.
- **Hat sich `.mcp.json` geändert?** Neue oder geänderte MCP-Server können auf die Umgebung zugreifen.
- **Hat sich `allowed-tools` oder `tools` im Frontmatter erweitert?** Neuer Werkzeugzugriff ist eine Berechtigungseskalation.
- **Gibt es neue Netzwerkaufrufe, Dateischreibvorgänge außerhalb des Skill-Verzeichnisses oder Code-Ausführung in der SKILL.md?** Diese kennzeichnen.
- **Hat sich die `description` des Skills oder sein angegebener Zweck geändert?** Ein Skill, der behauptete, "NDAs zu prüfen", und jetzt behauptet, "Verträge zu senden", hat sich umprogrammiert.

### Schritt 2.5: Erneuter Scan der neuen Version (GlassWorm-Sperre)

Den vollständigen `skills-qualitaetspruefung`-Scan gegen die NEUE Version durchführen, bevor das Update angewendet wird. Ein Skill, der bei v1.0 sauber war, kann ein vergiftetes v1.1 ausliefern — das GlassWorm-Muster (ein vertrauenswürdiger Publisher, ein etablierter Skill, ein kleinerer Versions-Bump, der die Nutzlast trägt). Vertrauen aus der Installationszeit überträgt sich nicht auf Updates.

**Regeln:**

1. **Bei Regression schließen.** Wenn die neue Version Befunde erzeugt, wo die alte keine hatte — in einer beliebigen `skills-qualitaetspruefung`-Kategorie — Update standardmäßig verweigern und erklären warum.
2. **Sicherheitsrelevante Diffs erfordern menschliche Genehmigung unabhängig vom Urteil.** Jede Änderung an `ausloeser/ausloeser.json`, `.mcp.json`, `allowed-tools`/`tools`-Frontmatter, neuer `Bash`/`WebFetch`/`WebSearch`-Zugriff, neue externe URLs, neue Dateischreibpfade außerhalb des Skill-Verzeichnisses oder das `description`-Frontmatter erzwingt einen menschlichen Genehmigungsprompt.
3. **Leseschutz-Scan-Kontext.** Der Scan liest angreiferkontrollierten Text (die neue SKILL.md). Im Leseschutz-Subagenten mit Read + WebFetch + Glob ausführen (kein Write, kein Bash, kein MCP), wenn verfügbar.
4. **Update verweigern, wenn Scan jetzt fehlschlägt.** Kein "trotzdem anwenden"-Option. REFUSE-Ausgabe und Stopp.

### Schritt 2.6: Aktualitätsbedingte Neu-Verifikation

Nicht nur auf neue Commits prüfen. Auch prüfen, ob installierte Skills ihr Aktualitätsfenster überschritten haben.

Für jeden installierten Skill aus dem Installationsprotokoll `last_verified`, `freshness_window` und `freshness_category` lesen. Aktives Fenster als `min(freshness_window, Nutzer-Schwellenwert für freshness_category)` berechnen.

**Wenn aktives Fenster abgelaufen ist UND es keinen neueren Commit gibt:**

> "Dieser Skill wurde seit [Datum] nicht aktualisiert und sein Referenzmaterial wurde zuletzt am [Datum] verifiziert — das Aktualitätsfenster von [N Monaten] ist überschritten. Optionen:
> (a) [verified_against-URLs] selbst prüfen,
> (b) beim Registry-Maintainer melden,
> (c) Skill bis zur erneuten Verifikation deaktivieren."

**Wenn aktives Fenster abgelaufen ist UND es einen neueren Commit gibt:**

Immer bei Update neu verifizieren, nicht still anwenden. Ein neuer Commit beweist nicht von sich aus, dass der Autor die gebearbeiteten Referenzen neu verifiziert hat.

### Schritt 3: Gemäß Einstellung verarbeiten

**Benachrichtigen (Standard):** Vollständigen Diff und Vertrauensprüfung anzeigen. "Update verfügbar. Den obigen Diff prüfen. Anwenden? [ja/nein]"

**Manuell:** Nur auflisten, was Updates hat. Nutzer führt `/kanzlei-builder-hub:automatischer-aktualisierer --apply [skill]` aus, wenn bereit.

Es gibt keinen "automatischen" Modus. Updates für Code in der Kanzleiumgebung erfordern immer, dass ein Mensch den Diff liest.

### Schritt 4: Anwenden (nach expliziter Genehmigung)

Installierte Skill-Dateien durch neue Version ersetzen. `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` mit neuem Commit-SHA aktualisieren. Alte Version vorher sichern (nach `~/.claude/skills/.backups/[skill]-[alter-sha]/`) für Rollback.

## Beispiel

```

## Update-Prüfung — 3 installierte Skills geprüft

### nda-prüfung — Update verfügbar
Installierter SHA: a1b2c3d → Neuester SHA: e4f5g6h

## Änderungen in SKILL.md
+ ## Neue DSGVO-Checkliste
+ 1. Art. 28 DSGVO Auftragsverarbeitung prüfen
- ## Alte NDA-Checkliste

Vertrauensprüfung: ✅ Keine Änderungen an ausloeser.json, .mcp.json oder allowed-tools.
skills-qualitaetspruefung: BEREIT — kein Rückschritt gegenüber v1.0.

Diff anzeigen (ja) oder Update zurückstellen (nein)?
```

## Risiken und typische Fehler

- **GlassWorm-Muster:** Vertrauenswürdiger Publisher, kleiner Versions-Bump, versteckte Nutzlast — deshalb scannt Schritt 2.5 jede neue Version.
- **Veränderliche Tags:** Niemals auf Tags pinnen — nur auf Commit-SHAs. Ein Tag `v1.0` kann retroaktiv auf einen anderen Commit zeigen.
- **Aktualitätsdrift:** Ein Skill kann ohne Commit-Änderung veralten, wenn Gesetze oder Rechtsprechung sich ändern. Schritt 2.6 erkennt dies.
- **Erster automatischer Update-Fallstrick:** Es gibt keinen automatischen Modus. Keine Ausnahme. Jedes Update erfordert menschliche Genehmigung.

## Was dieser Skill nicht tut

- Updates automatisch anwenden. Niemals. Jedes Update erhält einen Diff und eine Genehmigung.
- Skills aktualisieren, die nicht über den Hub installiert wurden.
- Tags, Branches oder Versionsnummern vertrauen. Nur Commit-SHAs werden gepinnt.

## Quellenpflicht

Bei der Ausführung dieses Skills sind folgende Quellen zu berücksichtigen:

- § 43a Abs. 2 BRAO (Verschwiegenheit; Sicherheit eingesetzter Werkzeuge)
- Art. 32 DSGVO (technisch-organisatorische Maßnahmen)
- § 50 BRAO (Aktenführung; Versionsprotokollierung)
- AI Act Art. 26 (Deployer-Pflichten; Überwachung von KI-Systemänderungen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 32 DSGVO
- § 203 StGB
- Art. 28 DSGVO
- Art. 30 DSGVO
- Art. 35 DSGVO
- § 4 KSchG
- Art. 25 DSGVO
- Art. 17 DSGVO
- § 5 KSchG
- § 29 VwVfG
- § 102 BetrVG
- § 17 MuSchG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

