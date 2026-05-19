---
name: verwandte-skills-vorschlag
description: "Verwandte Community-Skills basierend auf aktueller Tätigkeit in anderen Plugins empfehlen. Prüft, ob die Community etwas Relevantes für eine Aufgabe gebaut hat, und erwähnt es einmal, nicht aufdringlich. Einsetzen, wenn der Nutzer sagt: „Gibt es einen Community-Skill dafür\", „Was gibt es sonst noch\", oder wenn Skill-Empfehlungen gewünscht werden; läuft auch passiv am Ende von Abläufe anderer Plugins."
---

# /verwandte-skills-vorschlag — Verwandte-Skills-Empfehlung

## Zweck

Die Community könnte etwas gebaut haben, das Sie gerade selbst erstellen oder gesucht haben. Dieser Skill bemerkt dies und erwähnt es — einmal, kurz, nicht nervig. Keine Unterbrechung laufender Arbeit. Nur am Ende einer Aufgabe.

## Eingaben

- Aufgabenbeschreibung (was der Nutzer gerade getan hat) — aus dem Kontext oder direkt
- Kanzleiprofil: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` → Praxisprofil, installierte Skills (bereits installierte nicht vorschlagen), Benachrichtigungseinstellungen
- Registry-Cache aus `verzeichnis-durchsuchen`

## Ablauf

### Schritt 1: Kanzleiprofil und Registry-Cache laden

Praxisprofil lesen:
- Benachrichtigungseinstellung: `alle` / `passend zum Profil` / `keine`
- Wenn `keine`: still beenden (kein Output)

Registry-Cache lesen (aus `verzeichnis-durchsuchen`-Skill). Falls Cache nicht vorhanden oder >7 Tage alt: registries im Hintergrund aktualisieren. Falls keine Registries konfiguriert: nichts empfehlen.

### Schritt 2: Abgleich

Basierend auf der Aufgabenbeschreibung passende Skills in den Registries suchen:

**Abgleichskriterien:**
- Schlüsselwortüberschneidung zwischen der Aufgabe und Skill-Beschreibungen
- Praxisprofil-Passung (keine Strafrecht-Skills für einen Vertragsrechtler empfehlen)
- Noch nicht installiert

**Rechtsgebietsspezifische Erkennung:**
- Aufgaben mit Bezug zu §§ 622, 626 BGB, KSchG → Arbeitsrecht-Skills
- Aufgaben mit Bezug zu DSGVO, BDSG, AVV, DSE → Datenschutz-Skills
- Aufgaben mit Bezug zu NDA, LOI, Term Sheet, M&A → Gesellschaftsrecht/Vertragsrecht-Skills
- Aufgaben mit Bezug zu § 43a BRAO, Berufsrecht, BRAK → Kanzleiorganisation-Skills
- Aufgaben mit Bezug zu Schriftsatz, ZPO, Klage, Berufung → Prozessrecht-Skills

**Schwellenwert:** Nur anzeigen, wenn die Übereinstimmung stark ist. Schwache Übereinstimmungen sind Lärm. Lieber nichts anzeigen als zu nerven.

### Schritt 3: Ausgabe

**Bei starker Übereinstimmung:**
> 💡 Die Community hat einen Skill dafür: **[Name]** aus [Registry] — „[Beschreibung]". `/kanzlei-builder-hub:skill-installierer [name]` zum Ausprobieren.

**Bei keiner starken Übereinstimmung:** Keine Ausgabe. Nicht ankündigen „Ich habe nichts gefunden."

### Schritt 4: Häufigkeitsbegrenzung

Denselben Skill nicht zweimal empfehlen. Wenn der Nutzer ihn beim ersten Mal nicht installiert hat, hat er ihn gesehen und nein entschieden. Abweisungen in `references/surfaced.json` tracken.

### Nutzersteuerung

Gemäß `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` → neue Skill-Benachrichtigungen:
- **Alle:** Jede Übereinstimmung anzeigen
- **Passend zum Profil:** Nach Profil filtern (Standard)
- **Keine:** Dieser Skill ist deaktiviert — bei Aufruf sofort beenden

### Kanzlei-spezifische Hinweise im Surfacing

Wenn ein vorgeschlagener Skill Mandantendaten verarbeiten könnte, folgenden Hinweis ergänzen:
> „Vor der Installation: Prüfen Sie, ob dieser Skill Mandantendaten verarbeitet. Falls ja, ist eine Auftragsverarbeitung nach Art. 28 DSGVO sowie eine TOM-Prüfung nach Art. 32 DSGVO erforderlich."

## Quellen und Zitierweise

Keine direkten Rechtsnormen in diesem Skill. Bei Empfehlungen datenschutzrelevanter Skills:
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Datensicherheit)
- § 43a Abs. 2 BRAO (Verschwiegenheit)
- Zitierweise nach `../references/zitierweise.md`

## Ausgabeformat

Maximal ein kurzer einzeiliger Hinweis nach einer Aufgabe. Nie mehr als zwei Skills gleichzeitig empfehlen — wenn mehrere passen, den am besten passenden auswählen.

Format:
> 💡 Die Community hat einen Skill dafür: **[Name]** aus [Registry] — „[Kurzbeschreibung in einem Satz]". `/kanzlei-builder-hub:skill-installierer [name]` zum Ansehen.

## Entscheidungsbaum am Ende

Mit dem Nächste-Schritte-Entscheidungsbaum gemäß `CLAUDE.md` → `## Ausgaben` abschließen. Optionen auf das anpassen, was dieser Skill gerade produziert hat:

> **Wie weiter? Wählen Sie:**
> 1. **Skill ansehen** — Ich zeige die vollständige SKILL.md des empfohlenen Skills.
> 2. **Skill installieren** — Ich starte `/kanzlei-builder-hub:skill-installierer [name]` mit dem vollständigen Sicherheits- und Berufsrechtsprüfungs-Ablauf.
> 3. **Ähnliche Skills suchen** — Ich durchsuche die Registries nach weiteren Skills im gleichen Bereich.
> 4. **Nicht interessiert** — Ich merke mir das und empfehle diesen Skill nicht mehr.
> 5. **Sonstiges** — Was möchten Sie mit dieser Empfehlung tun?

## Beispiel

```
[Nach Vertragsreview mit NDAs]

💡 Die Community hat einen Skill dafür: **nda-pruefung** aus kanzlei-skills —
„Prüft Geheimhaltungsvereinbarungen auf typische Risikopunkte nach deutschem Recht."
/kanzlei-builder-hub:skill-installierer nda-pruefung zum Ansehen.
```

```
[Nach DSGVO-Aufgabe]

💡 Die Community hat einen Skill dafür: **avv-generator** aus kanzlei-datenschutz-skills —
„Generiert Auftragsverarbeitungsverträge nach Art. 28 DSGVO."
/kanzlei-builder-hub:skill-installierer avv-generator zum Ansehen.

Hinweis: Vor der Installation — dieser Skill verarbeitet Mandantendaten. TOM-Prüfung nach
Art. 32 DSGVO und ggf. AVV mit dem Infrastrukturanbieter erforderlich.
```

## Risiken / typische Fehler

- **Überempfehlung:** Lieber keine Empfehlung als eine schwache. Mehr als zwei aufeinanderfolgende Empfehlungen ohne Installation durch den Nutzer sind ein Signal, dass die Schwelle zu niedrig ist.
- **Bereits-installiert-Vergessen:** Immer die Installationsliste prüfen, bevor ein Skill empfohlen wird.
- **Datenschutzkontextfehlen:** Bei Empfehlungen, die Mandantendaten betreffen könnten, immer den DSGVO/BRAO-Hinweis ergänzen.
- **Unterbrechung laufender Arbeit:** Empfehlungen nur am Ende einer Aufgabe, nie während.

## Was dieser Skill nicht tut

- Skills installieren.
- Laufende Aufgaben unterbrechen. Empfehlungen erscheinen am *Ende* einer Aufgabe, nicht mittendrin.
- Nerven. Ein Hinweis pro Skill, nie.
- Benachrichtigungen anzeigen, wenn die Einstellung auf `keine` steht.
