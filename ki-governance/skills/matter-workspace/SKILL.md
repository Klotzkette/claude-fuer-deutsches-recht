---
name: matter-workspace
description: >
  Mandats-Workspaces verwalten – new, list, switch, close oder none (Praxisebene). Datei-
  Verwaltungslogik, um den Kontext eines Mandanten oder Auftrags von jedem anderen zu trennen.
  Verwenden, wenn mandatsübergreifend gearbeitet wird, wenn der Nutzer sagt „neues Mandat",
  „Mandat wechseln", „Mandate auflisten", „Mandat schließen" oder wenn ein inhaltlicher Skill
  wissen muss, in welchem Mandat er arbeitet.
argument-hint: "<new | list | switch | close | none> [slug]"
triggers:
  - "Mandat"
  - "Mandatsworkspace"
  - "matter-workspace"
  - "neues Mandat"
language: de
---

# /matter-workspace

## Zweck

Kanzleipraktiker arbeiten mit mehreren Mandanten und Mandaten. Ein Mandats-Workspace hält
den Kontext eines Mandanten oder Auftrags von jedem anderen getrennt – relevant für
§ 43a Abs. 2 BRAO (anwaltliche Verschwiegenheitspflicht) und § 203 StGB (Mandantengeheimnis).
Dieser Skill verwaltet diese Workspaces.

## Eingaben

- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
  (Abschnitt `## Mandate-Workspaces`)
- Subbefehl und optionaler Slug vom Nutzer

## Ablauf

1. CLAUDE.md lesen – bestätigen, dass der Abschnitt `## Mandate-Workspaces` vorhanden ist.
   Falls `Aktiviert` = `✗`:
   > Mandate-Workspaces sind deaktiviert – Sie sind als In-house-Praxis mit einem Mandanten
   > konfiguriert, sodass das Plugin automatisch vom Praxiskontext arbeitet. Wenn Sie
   > tatsächlich für mehrere Mandanten arbeiten, führen Sie `/ki-governance:cold-start-interview
   > --redo` neu aus und wählen einen Kanzleikontext. Andernfalls benötigen Sie `/matter-workspace`
   > nicht.

2. Auf den ersten Token von `$ARGUMENTS` verzweigen:
   - `new` → Aufnahme-Interview starten, `matter.md` schreiben, `history.md` und `notes.md`
     initialisieren.
   - `list` → Alle `matters/*/matter.md` auflisten; Tabelle drucken; aktives Mandat markieren.
   - `switch` → `Aktives Mandat:`-Zeile in CLAUDE.md aktualisieren.
   - `close` → `matters/<slug>/` nach `matters/_archived/<slug>/` verschieben; Schließdatum
     in `history.md` protokollieren.
   - `none` → `Aktives Mandat:` auf `keines – nur Praxiskontext` setzen.

3. Dem Nutzer zeigen, was sich geändert hat, und vor dem Schreiben bestätigen.

## Subbefehle

- `/ki-governance:matter-workspace new <slug>` – neuen Mandats-Workspace anlegen, kurzes
  Aufnahme-Interview, `matter.md` schreiben
- `/ki-governance:matter-workspace list` – Mandate mit Status und Aktiv-Flag auflisten
- `/ki-governance:matter-workspace switch <slug>` – aktives Mandat setzen
- `/ki-governance:matter-workspace close <slug>` – Mandat archivieren (nach
  `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/matters/_archived/` verschieben, nie löschen)
- `/ki-governance:matter-workspace none` – von aktivem Mandat trennen, nur auf Praxisebene
  arbeiten

## Speicherlayout

```
~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/
├── CLAUDE.md                       # praxisweites Praxisprofil
└── matters/
    ├── <slug>/
    │   ├── matter.md               # Mandant, Gegenseite, Mandatstyp, Kernfakten, Abweichungen
    │   ├── history.md              # datiertes Log von Ereignissen, Entscheidungen, Entwürfen
    │   ├── notes.md                # freie Arbeitsnotizen
    │   └── outputs/                # Skill-Ausgaben für dieses Mandat (optionaler Unterordner)
    └── _archived/
        └── <slug>/                 # geschlossene Mandate – lesbar, aber nicht aktiv
```

Slugs sind kleingeschrieben mit Bindestrichen. Beispiele: `mueller-ki-review-2026`,
`xyz-gmbh-aia`, `vendor-openai-avv`.

## Subbefehl-Logik

### `new <slug>`

1. Bestätigen, dass der Slug nicht bereits in `matters/<slug>/` oder `matters/_archived/<slug>/`
   vorhanden ist. Bei Wiederverwendung anderen Slug wählen.
2. Aufnahme-Interview starten:
   - **Mandant** (die von uns vertretene Partei oder die interne Geschäftseinheit bei In-house)
   - **Gegenseite** (die andere Seite – kann mehrere sein)
   - **Mandatstyp** (für ki-governance: KI-Anwendungsfall intern | Vendor-AI-Review | Folgenabschätzung | Regulierungsänderung | Richtlinienprojekt | Sonstiges)
   - **Vertraulichkeitsstufe** (standard | erhöht | Clean-Team – erhöht erfordert besondere
     Vorsicht in mandatsübergreifenden Einstellungen)
   - **Kernfakten** (2–5 Sätze: Worum geht es in diesem Mandat, wer sind die Stakeholder,
     was steht auf dem Spiel)
   - **Mandatsspezifische Abweichungen vom Playbook** (z. B. „Mandant verlangt 24-monatigen
     Haftungshöchstbetrag statt 12", „Gegenseite ist strategischer Partner – beziehungserhaltender
     Ton", „§ 203 StGB: besondere Schutzmechanismen erforderlich")
   - **Verbundene Mandate** (Slugs anderer zusammenhängender Mandate)
3. `matters/<slug>/matter.md` mit der nachstehenden Vorlage schreiben.
4. `matters/<slug>/history.md` mit einem einzigen „Eröffnet"-Eintrag initialisieren.
5. Leere `matters/<slug>/notes.md` anlegen.
6. **Nicht** automatisch auf das neue Mandat wechseln. Fragen: „Möchten Sie jetzt zu
   `<slug>` wechseln? (`/ki-governance:matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` auflisten. Tabelle:

| Slug | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. `_archived/*` unter separater „Archiviert"-Überschrift,
falls vorhanden.

### `switch <slug>`

1. Bestätigen, dass `matters/<slug>/matter.md` existiert. Falls nicht, `/matter-workspace
   new <slug>` anbieten.
2. `Aktives Mandat:`-Zeile in CLAUDE.md auf `Aktives Mandat: <slug>` setzen.
3. Nutzern die matter.md-Zusammenfassung zeigen, damit sie bestätigen können, dass sie
   beim richtigen Mandat sind.

### `close <slug>`

1. Bestätigen, dass `matters/<slug>/` existiert.
2. „Geschlossen"-Eintrag mit heutigem Datum an `matters/<slug>/history.md` anhängen.
3. `matters/<slug>/` → `matters/_archived/<slug>/` verschieben.
4. Falls das geschlossene Mandat das aktive war, `Aktives Mandat:` auf
   `keines – nur Praxiskontext` setzen.

### `none`

`Aktives Mandat:` in CLAUDE.md auf `keines – nur Praxiskontext` setzen. Mit Nutzer bestätigen.

## `matter.md`-Vorlage

```markdown
[ARBEITSPRODUKT-HEADER – gemäß Plugin-Konfiguration; Vertraulichkeitsmarkierung beachten]

# Mandat: [Mandant] – [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / clean-team]
**§ 203 StGB:** [Schweigepflicht beachtet – Schutzmechanismen: [Beschreibung]]

---

## Parteien

**Mandant:** [Name]
**Gegenseite:** [Name(n)]

## Mandatstyp

[KI-Anwendungsfall intern | Vendor-AI-Review | KI-Folgenabschätzung (FRIA/DSFA) | Regulierungsänderung | Richtlinienprojekt | Sonstiges – mit einzeiliger Begründung]

## Kernfakten

[2–5 Sätze. Worum geht es. Wer sind die Stakeholder. Was steht auf dem Spiel. Was es vom
Standard-Playbook unterscheidet.]

## Mandatsspezifische Abweichungen

*Jede Abweichung vom praxisweiten Playbook, die nur für dieses Mandat gilt.*

- [z. B. „Haftungshöchstbetrag: Mandant verlangt 24 Monate, nicht Hausstandard 12."]
- [z. B. „Ton: beziehungserhaltend – Gegenseite ist strategischer Partner."]
- [z. B. „Rechtswahl: muss deutsches Recht sein."]
- [z. B. „§ 203 StGB: nur On-Premise-Verarbeitung, kein Drittanbieter-LLM ohne AVV."]

## Verbundene Mandate

- [slug – ein Satz, warum verbunden]

## Vertraulichkeitshinweise

[Falls erhöht oder clean-team, erläutern warum. Wer Mandatsdateien einsehen darf. Ob
mandatsübergreifender Kontext trotz globaler Aktivierung zulässig ist.]
```

## `history.md`-Initialisierung

```markdown
# Verlauf: [Mandant] – [Kurzbeschreibung]

Nur-Anhänge-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] – Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Anfangskontext über matter.md hinaus – z. B. „Eröffnet als Reaktion auf eingehenden
Vendor-KI-Vertrag von [Gegenseite]."]
```

## Mandatsübergreifender Kontext

CLAUDE.md hat ein `Mandatsübergreifender Kontext:`-Flag. Bei `aus` (Standard) liest ein Skill
in Mandat A **niemals** Dateien in `matters/B/`. Das ist die Vertraulichkeitsgarantie für
die Anforderungen aus § 43a Abs. 2 BRAO und § 203 StGB.

Bei `an` darf ein Skill Dateien mandatsübergreifend nur lesen, wenn der Nutzer explizit
darum bittet (z. B. „Vergleichen Sie unsere Haftungshöchstbetragsposition über die letzten
fünf Vendor-Mandate"). Auch bei `an` ist der Standard, nur das aktive Mandat zu laden.

## Quellen und Zitierweise

Verbindliche Zitierweise gemäß `../references/zitierweise.md`.

- § 43a Abs. 2 BRAO – Anwaltliche Verschwiegenheitspflicht `[Primärquelle]`
- § 203 StGB – Mandantengeheimnis bei KI-Einsatz `[Primärquelle]`
- § 53 StPO – Zeugnisverweigerungsrecht `[Primärquelle]`

## Was dieser Skill nicht tut

- **Keine Interessenkonfliktprüfung.** Konflikte liegen beim Praktiker/der Kanzlei;
  das Aufnahme-Formular erfasst, was der Nutzer angibt.
- **Keine Aufbewahrungserzwingung.** Schließen archiviert ein Mandat; es löscht nicht.
  Aufbewahrungsrichtlinie liegt außerhalb des Anwendungsbereichs.
- **Keine Ausgabenweiterleitung.** Der inhaltliche Skill entscheidet, wohin er schreibt;
  dieser Skill teilt ihm mit, welcher Ordner aktiv ist.
- **Keine Entscheidung über mandatsübergreifende Zulässigkeit.** Er liest das Flag und
  befolgt es.

## Risiken / typische Fehler

- **§ 203 StGB bei KI-Einsatz.** Wenn Mandantendaten in ein Drittanbieter-LLM eingegeben
  werden, AVV nach Art. 28 DSGVO und Vereinbarkeit mit § 203 StGB prüfen. Im matter.md
  dokumentieren.
- **Slug-Wiederverwendung.** Führt zu Kontext-Vermischung. Immer neu prüfen, ob Slug frei ist.
- **Schließen vs. Löschen.** Archivierte Mandate für Konflikts- und Aufbewahrungszwecke
  niemals löschen.
