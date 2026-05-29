---
name: verzeichnis-durchsuchen
description: "Skill-Verzeichnis nach Rechtsgebiet, Norm oder Mandantentyp durchsuchen. Normen: technisch/intern. Prüfraster: Suchbegriff, Kategoriefilter, Ergebnispriorisierung. Output: Suchergebnisliste Skills. Abgrenzung: nicht Skill-Installation oder -verwaltung."
---

# /verzeichnis-durchsuchen — Skill-Registry-Browser


## Triage zu Beginn
1. Nach welchem Skill oder welchem Rechtsgebiet wird gesucht (Stichwort oder freie Suche)?
2. Welche Registries sind in der Watchlist — und sind sie aktuell (Cache aelter als 7 Tage)?
3. Soll eine neue Registry zur Watchlist hinzugefuegt werden (URL-Validierung und Sicherheitshinweis erforderlich)?
4. Ist der Positivliste-Modus 'restrictive' (neue Registry muss auch in positivliste.yaml eingetragen werden)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 32 DSGVO — TOM: Sicherheitsprueung jeder neuen Registry vor Aufnahme in Watchlist
- Art. 28 DSGVO — AVV: Registry-Betreiber kann Auftragsverarbeiter sein, wenn Skills Mandantendaten verarbeiten
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht: Registry-Skills duerfen keine Mandantengeheimnisse an externe Anbieter uebermitteln
- § 203 StGB — Verletzung von Privatgeheimnissen: Community-Skills muessen mandatsgeheimnisskonform sein

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Skills in den beobachteten Registries finden. Suchen, Vorschau anzeigen, entscheiden. Dieser Skill installiert nichts — er zeigt, was verfügbar ist. Das Installieren übernimmt `/kanzlei-builder-hub:skill-installierer`.

## Eingaben

- Suchbegriff (optional — ohne Argument werden alle Skills aller Registries aufgelistet)
- Kanzleiprofil: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` → beobachtete Registries
- Optional: URL einer neuen Registry, die hinzugefügt werden soll

## Ablauf

### Schritt 1: Kanzleiprofil laden

Beobachtete Registries aus dem Config-Pfad lesen. Wenn keine Registries konfiguriert sind, hinweisen: "Keine beobachteten Registries konfiguriert. Führen Sie `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview` aus oder geben Sie eine Registry-URL an."

Praxisprofil lesen (Rechtsgebiet, Kanzleityp) um Suchergebnisse zu gewichten und unpassende Skills als solche zu kennzeichnen.

### Schritt 2: Registry-Indexes abrufen

Für jede beobachtete Registry:

- GitHub-Repos: `skills/`-Verzeichnislisting und Frontmatter (Name + Beschreibung) jeder `SKILL.md` abrufen.
- Marketplace-artige Registries: Index abrufen.

Index lokal cachen (`references/registry-cache.json`) für schnelles Browsen. Cache aktualisieren wenn >7 Tage alt oder auf Anforderung.

### Schritt 3: Suche

Anfrage gegen Skill-Namen und Beschreibungen abgleichen. Einfacher Schlüsselwortabgleich — keine Fuzzy-Suche nötig.

Zusätzlich: nach Kategorie browsen, falls die Registry so organisiert ist.

**Profil-Filterung:** Suchergebnisse nach Kanzleiprofil gewichten:
- Skills, die genau zum Rechtsgebiet passen: zuerst anzeigen
- Skills aus dem Rechtsgebiet des Nutzers: mit ✅ markieren
- Skills aus anderen Rechtsgebieten: anzeigen, aber als "ggf. nicht relevant für Ihr Profil" kennzeichnen
- Bereits installierte Skills: als "bereits installiert" markieren und nicht doppelt vorschlagen

### Schritt 4: Treffer präsentieren

```markdown
## Suche: "[Suchbegriff]"

**[N] Skills in [M] Registries gefunden:**

### [skill-name]
**Aus:** [Registry-Name]
**Rechtsgebiet:** [Rechtsgebiet-Tag, falls vorhanden]
**Beschreibung:** [aus dem Frontmatter]
**Zuletzt verifiziert:** [Datum, falls angegeben]
[Vollständige SKILL.md anzeigen] [Installieren]

### [skill-name]
[...]
```

### Schritt 5: Vorschau

Auf "Vollständige SKILL.md anzeigen": Die gesamte Datei abrufen und anzeigen. Nutzer liest sie, bevor er sich zur Installation entscheidet. Keine Überraschungen.

### Schritt 6: Registry hinzufügen

Wenn der Nutzer eine URL zu einer Registry hat, die nicht in der Watchlist ist:

1. URL abrufen, validieren dass es sich um ein Skills-Repo handelt (hat `skills/` oder `.claude-plugin/`)
2. Anzeigen, was darin enthalten ist (Vorschau)
3. Zur Watchlist hinzufügen: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` → beobachtete Registries — nur nach Bestätigung

**Sicherheitshinweis beim Hinzufügen einer Registry:**
> "Eine neue Registry hinzuzufügen bedeutet, dass deren Skills für die Installation verfügbar werden. Prüfen Sie, wer die Registry betreibt und welche Skills sie enthält, bevor Sie sie als vertrauenswürdig einstufen. Für Kanzleibetrieb mit Mandantendaten sollten nur Registries vertrauenswürdiger Quellen hinzugefügt werden."

Wenn der Positivliste-Modus `restrictive` ist: darauf hinweisen, dass die neue Registry auch in `positivliste.yaml` unter `registries` eingetragen werden muss, bevor der Installer Skills daraus installiert.

## Standard-Registries

- **kanzlei-skills** — Skills für deutsche Kanzleien und Rechtsabteilungen — Kanzlei-Community auf GitHub

## Quellen und Zitierweise

Keine direkten Rechtsnormen-Zitate. Bei Fragen zu vertrauenswürdigen Drittanbieter-Registries:
- Art. 32 DSGVO (Sicherheit der Verarbeitung — Grundlage für Registry-Vertrauensprüfung)
- § 43a Abs. 2 BRAO (Verschwiegenheit — Grundlage für Prüfung, ob Registry-Skills Mandantendaten gefährden könnten)
- Zitierweise nach `../references/zitierweise.md`

## Ausgabeformat

Strukturierte Trefferliste mit:
- Skill-Name, Registry-Herkunft, Rechtsgebiet-Tag
- Kurzbeschreibung (aus Frontmatter)
- Aktualitätsdatum (falls angegeben)
- Links: "Vollständige SKILL.md anzeigen" / "Installieren"
- Kennzeichnung bereits installierter Skills
- Am Ende: "[N] weitere Skills nicht angezeigt. Filter anpassen?"

## Beispiel

```
## Suche: "NDA"

3 Skills in 2 Registries gefunden:

### nda-prüfung ✅
Aus: kanzlei-skills
Rechtsgebiet: Vertragsrecht, Gesellschaftsrecht
Beschreibung: Prüft Geheimhaltungsvereinbarungen (NDA) auf typische Risikopunkte nach deutschem
Recht — Laufzeit, Vertragsstrafe, Rückgabepflichten, Wettbewerbsklauseln.
Zuletzt verifiziert: 2025-01-10

[Vollständige SKILL.md anzeigen] [Installieren]

### geheimhaltungsvereinbarung-generator
Aus: kanzlei-skills
Rechtsgebiet: Vertragsrecht
Beschreibung: Generiert NDA-Entwürfe für bilaterale Geheimhaltungsvereinbarungen nach deutschem Recht.
Zuletzt verifiziert: 2024-09-01 ⚠️ Aktualität prüfen (>6 Monate)

[Vollständige SKILL.md anzeigen] [Installieren]
```

## Risiken / typische Fehler

- **Aktualitätsdrift:** Ein Skill ohne `last_verified`-Datum kann veraltete Rechtsnormen oder Rechtsprechung enthalten. Bei Skills ohne Aktualitätsangabe besonders sorgfältig prüfen.
- **Registry-Impersonation:** Eine URL die wie `kanzlei-skills` aussieht, könnte auf ein kompromittiertes Repo zeigen. Immer den vollständigen Repository-Pfad prüfen.
- **Profilübereinstimmung als Sicherheitsgarantie missverstehen:** Ein als "✅ passend zum Profil" markierter Skill ist noch kein geprüfter Skill — das `skills-qualitaetspruefung` und die Berufsrechtsprüfung folgen erst beim Installieren.

## Was dieser Skill nicht tut

- Skills installieren. Das macht `skill-installierer`.
- Skills bewerten oder Empfehlungen geben (nur Profil-Passung-Filterung). Den Rohtext prüfen; Sie urteilen.
- Das gesamte Internet durchsuchen. Nur beobachtete Registries.
