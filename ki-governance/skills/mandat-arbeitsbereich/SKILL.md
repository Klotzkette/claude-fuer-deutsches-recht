---
name: mandat-arbeitsbereich
description: "Mandats-Arbeitsbereiche verwalten – neu, liste, wechseln, schließen oder keines (Praxisebene). Datei- Verwaltungslogik, um den Kontext eines Mandanten oder Auftrags von jedem anderen zu trennen. Verwenden, wenn mandatsübergreifend gearbeitet wird, wenn der Nutzer sagt neues Mandat, Mandat wechsel..."
---

# /mandat-arbeitsbereich

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
 > tatsächlich für mehrere Mandanten arbeiten, führen Sie `/ki-governance:ki-governance-kaltstart-interview
 > --redo` neu aus und wählen einen Kanzleikontext. Andernfalls benötigen Sie `/mandat-arbeitsbereich`
 > nicht.

2. Auf den ersten Token von `$ARGUMENTS` verzweigen:
 - `new` → Aufnahme-Interview starten, `mandat.md` schreiben, `verlauf.md` und `notizen.md`
 initialisieren.
 - `list` → Alle `mandate/*/mandat.md` auflisten; Tabelle drucken; aktives Mandat markieren.
 - `switch` → `Aktives Mandat:`-Zeile in CLAUDE.md aktualisieren.
 - `close` → `mandate/<slug>/` nach `mandate/_archiv/<slug>/` verschieben; Schließdatum
 in `verlauf.md` protokollieren.
 - `none` → `Aktives Mandat:` auf `keines – nur Praxiskontext` setzen.

3. Dem Nutzer zeigen, was sich geändert hat, und vor dem Schreiben bestätigen.

## Subbefehle

- `/ki-governance:ki-governance-mandat-arbeitsbereich new <slug>` – neuen Mandats-Workspace anlegen, kurzes
 Aufnahme-Interview, `mandat.md` schreiben
- `/ki-governance:ki-governance-mandat-arbeitsbereich list` – Mandate mit Status und Aktiv-Flag auflisten
- `/ki-governance:ki-governance-mandat-arbeitsbereich switch <slug>` – aktives Mandat setzen
- `/ki-governance:ki-governance-mandat-arbeitsbereich close <slug>` – Mandat archivieren (nach
 `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/mandate/_archiv/` verschieben, nie löschen)
- `/ki-governance:ki-governance-mandat-arbeitsbereich none` – von aktivem Mandat trennen, nur auf Praxisebene
 arbeiten

## Speicherlayout

```
~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/
├── CLAUDE.md # praxisweites Praxisprofil
└── mandate/
 ├── <slug>/
 │ ├── mandat.md # Mandant, Gegenseite, Mandatstyp, Kernfakten, Abweichungen
 │ ├── verlauf.md # datiertes Log von Ereignissen, Entscheidungen, Entwürfen
 │ ├── notizen.md # freie Arbeitsnotizen
 │ └── outputs/ # Skill-Ausgaben für dieses Mandat (optionaler Unterordner)
 └── _archiv/
 └── <slug>/ # geschlossene Mandate – lesbar, aber nicht aktiv
```

Slugs sind kleingeschrieben mit Bindestrichen. Beispiele: `mueller-ki-review-2026`,
`xyz-gmbh-aia`, `vendor-openai-avv`.

## Subbefehl-Logik

### `new <slug>`

1. Bestätigen, dass der Slug nicht bereits in `mandate/<slug>/` oder `mandate/_archiv/<slug>/`
 vorhanden ist. Bei Wiederverwendung anderen Slug wählen.
2. Aufnahme-Interview starten:
 - **Mandant** (die von uns vertretene Partei oder die interne Geschäftseinheit bei In-house)
 - **Gegenseite** (die andere Seite – kann mehrere sein)
 - **Mandatstyp** (für ki-governance: KI-Anwendungsfall intern | Vendor-AI-Review | Folgenabschätzung | Regulierungsänderung | Richtlinienprojekt | Sonstiges)
 - **Vertraulichkeitsstufe** (standard | erhöht | Clean-Team – erhöht erfordert besondere
 Vorsicht in mandatsübergreifenden Einstellungen)
 - **Kernfakten** (2–5 Sätze: Worum geht es in diesem Mandat, wer sind die Stakeholder,
 was steht auf dem Spiel)
 - **Mandatsspezifische Abweichungen vom Playbook** (z. B. "Mandant verlangt 24-monatigen
 Haftungshöchstbetrag statt 12", "Gegenseite ist strategischer Partner – beziehungserhaltender
 Ton", "§ 203 StGB: besondere Schutzmechanismen erforderlich")
 - **Verbundene Mandate** (Slugs anderer zusammenhängender Mandate)
3. `mandate/<slug>/mandat.md` mit der nachstehenden Vorlage schreiben.
4. `mandate/<slug>/verlauf.md` mit einem einzigen "Eröffnet"-Eintrag initialisieren.
5. Leere `mandate/<slug>/notizen.md` anlegen.
6. **Nicht** automatisch auf das neue Mandat wechseln. Fragen: "Möchten Sie jetzt zu
 `<slug>` wechseln? (`/ki-governance:ki-governance-mandat-arbeitsbereich switch <slug>`)"

### `list`

`mandate/*/mandat.md` auflisten. Tabelle:

| Slug | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. `_archiv/*` unter separater "Archiviert"-Überschrift,
falls vorhanden.

### `switch <slug>`

1. Bestätigen, dass `mandate/<slug>/mandat.md` existiert. Falls nicht, `/mandat-arbeitsbereich
 new <slug>` anbieten.
2. `Aktives Mandat:`-Zeile in CLAUDE.md auf `Aktives Mandat: <slug>` setzen.
3. Nutzern die mandat.md-Zusammenfassung zeigen, damit sie bestätigen können, dass sie
 beim richtigen Mandat sind.

### `close <slug>`

1. Bestätigen, dass `mandate/<slug>/` existiert.
2. "Geschlossen"-Eintrag mit heutigem Datum an `mandate/<slug>/verlauf.md` anhängen.
3. `mandate/<slug>/` → `mandate/_archiv/<slug>/` verschieben.
4. Falls das geschlossene Mandat das aktive war, `Aktives Mandat:` auf
 `keines – nur Praxiskontext` setzen.

### `none`

`Aktives Mandat:` in CLAUDE.md auf `keines – nur Praxiskontext` setzen. Mit Nutzer bestätigen.

## `mandat.md`-Vorlage

```markdown
[ARBEITSPRODUKT-HEADER – gemäß Plugin-Konfiguration; Vertraulichkeitsmarkierung beachten]

### Mandat: [Mandant] – [Kurzbeschreibung]

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

- [z. B. "Haftungshöchstbetrag: Mandant verlangt 24 Monate, nicht Hausstandard 12."]
- [z. B. "Ton: beziehungserhaltend – Gegenseite ist strategischer Partner."]
- [z. B. "Rechtswahl: muss deutsches Recht sein."]
- [z. B. "§ 203 StGB: nur On-Premise-Verarbeitung, kein Drittanbieter-KI-System ohne AVV."]

## Verbundene Mandate

- [slug – ein Satz, warum verbunden]

## Vertraulichkeitshinweise

[Falls erhöht oder clean-team, erläutern warum. Wer Mandatsdateien einsehen darf. Ob
mandatsübergreifender Kontext trotz globaler Aktivierung zulässig ist.]
```

## `verlauf.md`-Initialisierung

```markdown
### Verlauf: [Mandant] – [Kurzbeschreibung]

Nur-Anhänge-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] – Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Anfangskontext über mandat.md hinaus – z. B. "Eröffnet als Reaktion auf eingehenden
Vendor-KI-Vertrag von [Gegenseite]."]
```

## Mandatsübergreifender Kontext

CLAUDE.md hat ein `Mandatsübergreifender Kontext:`-Flag. Bei `aus` (Standard) liest ein Skill
in Mandat A **niemals** Dateien in `mandate/B/`. Das ist die Vertraulichkeitsgarantie für
die Anforderungen aus § 43a Abs. 2 BRAO und § 203 StGB.

Bei `an` darf ein Skill Dateien mandatsübergreifend nur lesen, wenn der Nutzer explizit
darum bittet (z. B. "Vergleichen Sie unsere Haftungshöchstbetragsposition über die letzten
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

- **§ 203 StGB bei KI-Einsatz.** Wenn Mandantendaten in ein Drittanbieter-KI-System eingegeben
 werden, AVV nach Art. 28 DSGVO und Vereinbarkeit mit § 203 StGB prüfen. Im mandat.md
 dokumentieren.
- **Slug-Wiederverwendung.** Führt zu Kontext-Vermischung. Immer neu prüfen, ob Slug frei ist.
- **Schließen vs. Löschen.** Archivierte Mandate für Konflikts- und Aufbewahrungszwecke
 niemals löschen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des Anwalts
- § 203 StGB — Mandantengeheimnis
- § 50 BRAO — Handakten-Pflicht (fuenf Jahre)
- Art. 28 DSGVO — Auftragsverarbeitung bei externen Dienstleistern

## Triage zu Beginn
1. Handelt es sich um eine Kanzlei (mehrere Mandanten) oder eine In-house-Situation (ein Mandant)?
2. Ist das gesuchte Mandat bereits angelegt oder muss es neu erstellt werden?
3. Bestehen Interessenkonflikte — wurde der Konflikt-Check (§ 43a BRAO) durchgefuehrt?
4. Soll ein abgeschlossenes Mandat archiviert oder reaktiviert werden?
5. Welcher Skill soll anschliessend im Mandatskontext ausgefuehrt werden?

## Output-Template — Mandats-Workspace-Anlage
**Adressat:** Kanzlei intern — Tonfall: knapp, strukturiert
```
MANDATS-WORKSPACE
Slug: [SLUG]
Angelegt: [DATUM] — Letzte Aktivitaet: [DATUM]
Status: [AKTIV / ARCHIVIERT]

Mandant: [NAME MANDANT]
Gegenseite: [NAME GEGNER]
Mandatstyp: [IT-Recht / KI-Governance / Datenschutz / ...]
Sachgebiet: [KURZBEZEICHNUNG]

Aktenzeichen: [AKTENZEICHEN]
Zustaendige RA/RAin: [NAME]
Konflikt-Check: [DURCHGEFUEHRT AM DATUM — KEIN KONFLIKT / KONFLIKT: BESCHREIBUNG]

Kernfakten: [KURZBEZEICHNUNG 1-3 SAETZE]
Naechste Frist: [DATUM — ART DER FRIST]
Aktiver Skill: [SKILL-NAME]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

