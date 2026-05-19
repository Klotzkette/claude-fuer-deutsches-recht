---
name: automatischer-aktualisierer
description: >
  Prüft installierte Community-Skills auf Updates. Zeigt einen vollständigen Diff und erfordert
  eine explizite Genehmigung vor der Anwendung. Einsetzen, wenn der Nutzer sagt:
  „Updates prüfen", „Skills aktualisieren", „Gibt es Neuigkeiten für meine installierten Skills",
  oder wenn der Registry-Sync-Agent den Skill aufruft.
argument-hint: "[--apply zum Aktualisieren aller, sonst nur Benachrichtigen]"
language: de
triggers:
  - "updates prüfen"
  - "skills aktualisieren"
  - "automatischer-aktualisierer"
  - "skill-updates"
  - "neue version skill"
  - "verzeichnis-synchronisierung"
  - "skill auf aktualität prüfen"
---

# /automatischer-aktualisierer — Automatische Aktualisierung mit Diff-Review

## Zweck

Community-Skills verbessern sich. Dieser Skill bemerkt, wenn eine neue Version vorliegt, zeigt genau, was sich geändert hat, und wendet Updates ausschließlich mit Ihrer expliziten Genehmigung an. Kein Update wird jemals ohne menschliche Sichtung des Diffs durchgeführt.

**Vertrauenshaltung:** Installierte Skills laufen in Ihrer privilegierten Kanzleiumgebung mit Zugriff auf Mandantendaten. Ein vorgelagertes Repository kann kompromittiert, an einen neuen Eigentümer übertragen oder einfach so geändert werden, dass Sie das nicht möchten. Dieser Skill ist so konzipiert, dass **kein Update jemals ohne Lesen des Diffs und explizite Genehmigung angewendet wird.** Das ist kein Präferenz — es ist das Design.

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

- BGH, Urt. v. 10.02.2011 – IX ZR 49/10, NJW 2011, 1594 Rn. 9 — Haftung bei Verletzung von Organisationspflichten in der Kanzlei; sorgfaltsgemäße Einrichtung und Überwachung technischer Systeme ist geschuldeter Anwaltspflichtstandard.
- BGH, Urt. v. 26.09.2002 – IX ZR 399/99, NJW 2003, 211 — Rechtsanwalt haftet für unzureichende Überprüfung eingesetzter Software in der Mandatsbearbeitung, wenn dadurch Datenverlust entsteht.

### Kommentar- und Aufsatzbelege

- Henssler/Prütting, in: Henssler/Prütting, BRAO, 5. Aufl. 2023, § 43a Rn. 55 — Verschwiegenheitspflicht und technische Schutzmaßnahmen beim Einsatz von KI-Werkzeugen in der Kanzlei.
- Hähnchen, NJW 2024, 1137 (1141) — KI-gestützte Rechtsdienstleistung: Anforderungen an Qualitätssicherung; einschlägig zu Update-Kontrolle als Bestandteil des Qualitätsmanagements.

## Ablauf

### Schritt 1: Jeden installierten Skill prüfen

Für jeden Skill in der Installationsliste:

- Aktuellen Commit-SHA von der Quellregistry abrufen (exakter Commit, nicht ein Tag oder Branch-Head — Tags sind veränderbar und können nachträglich vom Publisher überschrieben werden; nur Commit-SHAs sind unveränderlich).
- Mit dem beim Installationszeitpunkt gespeicherten SHA vergleichen.
- Bei Abweichung: Update verfügbar.

### Schritt 2: Diff und Vertrauensprüfung

Für jedes Update den vollständigen Diff anzeigen:

```diff
# [skill-name] — [installierter SHA] → [neuester SHA]

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
- **Hat sich die `description` des Skills oder sein angegebener Zweck geändert?** Ein Skill, der behauptete, „NDAs zu prüfen", und jetzt behauptet, „Verträge zu senden", hat sich umprogrammiert.

### Schritt 2.5: Erneuter Scan der neuen Version (GlassWorm-Sperre)

Den vollständigen `skills-qualitaetspruefung`-Scan gegen die NEUE Version durchführen, bevor das Update angewendet wird. Ein Skill, der bei v1.0 sauber war, kann ein vergiftetes v1.1 ausliefern — das GlassWorm-Muster (ein vertrauenswürdiger Publisher, ein etablierter Skill, ein kleinerer Versions-Bump, der die Nutzlast trägt). Vertrauen aus der Installationszeit überträgt sich nicht auf Updates.

**Regeln:**

1. **Bei Regression schließen.** Wenn die neue Version Befunde erzeugt, wo die alte keine hatte — in einer beliebigen `skills-qualitaetspruefung`-Kategorie — Update standardmäßig verweigern und erklären warum.
2. **Sicherheitsrelevante Diffs erfordern menschliche Genehmigung unabhängig vom Urteil.** Jede Änderung an `ausloeser/ausloeser.json`, `.mcp.json`, `allowed-tools`/`tools`-Frontmatter, neuer `Bash`/`WebFetch`/`WebSearch`-Zugriff, neue externe URLs, neue Dateischreibpfade außerhalb des Skill-Verzeichnisses oder das `description`-Frontmatter erzwingt einen menschlichen Genehmigungsprompt.
3. **Leseschutz-Scan-Kontext.** Der Scan liest angreiferkontrollierten Text (die neue SKILL.md). Im Leseschutz-Subagenten mit Read + WebFetch + Glob ausführen (kein Write, kein Bash, kein MCP), wenn verfügbar.
4. **Update verweigern, wenn Scan jetzt fehlschlägt.** Kein „trotzdem anwenden"-Option. REFUSE-Ausgabe und Stopp.

### Schritt 2.6: Aktualitätsbedingte Neu-Verifikation

Nicht nur auf neue Commits prüfen. Auch prüfen, ob installierte Skills ihr Aktualitätsfenster überschritten haben.

Für jeden installierten Skill aus dem Installationsprotokoll `last_verified`, `freshness_window` und `freshness_category` lesen. Aktives Fenster als `min(freshness_window, Nutzer-Schwellenwert für freshness_category)` berechnen.

**Wenn aktives Fenster abgelaufen ist UND es keinen neueren Commit gibt:**

> „Dieser Skill wurde seit [Datum] nicht aktualisiert und sein Referenzmaterial wurde zuletzt am [Datum] verifiziert — das Aktualitätsfenster von [N Monaten] ist überschritten. Optionen:
> (a) [verified_against-URLs] selbst prüfen,
> (b) beim Registry-Maintainer melden,
> (c) Skill bis zur erneuten Verifikation deaktivieren."

**Wenn aktives Fenster abgelaufen ist UND es einen neueren Commit gibt:**

Immer bei Update neu verifizieren, nicht still anwenden. Ein neuer Commit beweist nicht von sich aus, dass der Autor die gebündelten Referenzen neu verifiziert hat.

### Schritt 3: Gemäß Einstellung verarbeiten

**Benachrichtigen (Standard):** Vollständigen Diff und Vertrauensprüfung anzeigen. „Update verfügbar. Den obigen Diff prüfen. Anwenden? [ja/nein]"

**Manuell:** Nur auflisten, was Updates hat. Nutzer führt `/kanzlei-builder-hub:automatischer-aktualisierer --apply [skill]` aus, wenn bereit.

Es gibt keinen „automatischen" Modus. Updates für Code in der Kanzleiumgebung erfordern immer, dass ein Mensch den Diff liest.

### Schritt 4: Anwenden (nach expliziter Genehmigung)

Installierte Skill-Dateien durch neue Version ersetzen. `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` mit neuem Commit-SHA aktualisieren. Alte Version vorher sichern (nach `~/.claude/skills/.backups/[skill]-[alter-sha]/`) für Rollback.

## Ausgabeformat

Für jedes Update:
- Skill-Name und SHA-Übergang
- Vollständiger Diff aller geänderten Dateien
- Vertrauensprüfungs-Ergebnisse (Automatische Auslöser, MCP, Werkzeugberechtigungen, Netzwerkaufrufe)
- skills-qualitaetspruefung-Scan-Ergebnis für neue Version
- Genehmigungsprompt: „Anwenden? (ja / nein)"

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
- BGH, Urt. v. 10.02.2011 – IX ZR 49/10, NJW 2011, 1594 Rn. 9
- BGH, Urt. v. 26.09.2002 – IX ZR 399/99, NJW 2003, 211
- Henssler/Prütting, in: Henssler/Prütting, BRAO, 5. Aufl. 2023, § 43a Rn. 55
- Hähnchen, NJW 2024, 1137 (1141)

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
