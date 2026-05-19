---
name: mandat-arbeitsbereich
description: "Verwaltet Mandatsarbeitsbereiche für Mehrmandat-Kanzleien — anlegen, auflisten, wechseln, abschließen oder vom aktiven Mandat lösen. Lädt, wenn der Nutzer einen neuen Mandatsarbeitsbereich anlegen, das aktive Mandat wechseln, Mandate auflisten, ein Mandat archivieren oder nur auf Kanzleiebene arbeiten möchte."
---

# Mandatsarbeitsbereich

## Zweck

Anwälte mit mehreren Mandanten und Verfahren arbeiten parallel an verschiedenen Prozessmandaten. Ein Mandatsarbeitsbereich hält den Kontext eines Mandats strikt von allen anderen getrennt. Dieser Skill verwaltet diese Arbeitsbereiche. Lädt bei Anfragen zur Mandatsverwaltung: Anlegen, Auflisten, Wechseln, Schließen und Archivieren von Prozessmandaten.

**Standardzustand ist deaktiviert für Syndikusrechtsanwälte** (§ 46 BRAO) und Einmandat-Kanzleien. Für diese läuft das Plugin automatisch auf Kanzleiebene. Ist `Aktiviert: ✗` in der Kanzleikonfiguration, erklärt dieser Skill den deaktivierten Zustand und schlägt eine Neukonfiguration vor.

## Eingaben

- **Unterbefehl** (erforderlich): `neu`, `liste`, `wechseln`, `schließen` oder `keins`
- **Mandatsbezeichnung (Slug)**: Kleinschreibung mit Bindestrichen (z. B. `schmidt-gmbh-berufung-2025`)
- **Mandantendaten** (bei `neu`): Mandant, Gegenseite, Mandatstyp, Vertraulichkeitsstufe, Sachverhalt, mandatsspezifische Abweichungen vom Kanzleistandard, verwandte Mandate

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht des Rechtsanwalts; absolute Mandandenvertraulichkeit; keine Datenweitergabe zwischen Mandaten ohne Einwilligung.
- **§ 50 BRAO** — Handakten des Rechtsanwalts; Aufbewahrungspflicht von mindestens fünf Jahren nach Mandatsende (§ 50 Abs. 2 BRAO).
- **§ 3 BORA** — Mandatsniederlegung; die Aktenführungspflicht bleibt bis zur ordnungsgemäßen Übergabe bestehen.
- **§ 45 BRAO** — Tätigkeitsverbote bei Interessenkonflikten; vor Mandatsanlage ist die Konfliktkontrolle unerlässlich.
- **§ 2 Abs. 1 DSGVO i.V.m. § 1 BDSG** — Personenbezogene Daten in Mandatsakten unterliegen dem Datenschutzrecht; organisatorische Trennung ist technisch-organisatorische Maßnahme i.S.d. Art. 32 DSGVO.

### Leitentscheidungen

- **BGH, Urt. v. 05.11.2009 – IX ZR 214/08, NJW 2010, 73 Rn. 16** — Anwaltliche Verschwiegenheitspflicht und Haftung bei unzulässiger mandatsübergreifender Nutzung von Informationen; strikte Trennung der Mandate als Berufspflicht.
- **BGH, Urt. v. 14.07.2016 – IX ZR 291/14, NJW 2016, 3235 Rn. 22 ff.** — Aufbewahrung von Handakten; Herausgabepflicht nach § 50 BRAO; Haftung bei vorzeitiger Vernichtung.
- **BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, NJW 2005, 1917** — Schutz der Mandatsunterlagen vor staatlichem Zugriff; anwaltliche Verschwiegenheit als Verfassungsposition.

### Kommentarliteratur

- `Dittmann, in: Henssler/Prütting, BRAO, 5. Aufl. 2023, § 43a Rn. 55` — Verschwiegenheitspflicht; Reichweite und Grenzen; mandatsübergreifende Nutzung.
- `Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 84 Rn. 3` — Vollmacht und Aktenführung im Prozess; Wechsel des Prozessbevollmächtigten.
- `Römermann, in: BeckOK BRAO, 21. Ed. (Stand 01.03.2024), § 50 Rn. 12` — Handaktenpflicht, Aufbewahrung, Vernichtung.

## Ablauf

### Schritt 1: Konfiguration prüfen

Lies `CLAUDE.md` → Abschnitt `## Mandatsarbeitsbereiche`. Ist `Aktiviert: ✗`:

> „Mandatsarbeitsbereiche sind deaktiviert — die Kanzlei ist als Einmandat-Kanzlei (z. B. Syndikusrechtsanwalt nach § 46 BRAO) konfiguriert und arbeitet automatisch auf Kanzleiebene. Falls tatsächlich mehrere Mandate geführt werden, bitte `/prozessrecht:erstkonfiguration --neu` ausführen und eine Mehrmandat-Kanzlei auswählen. Andernfalls wird `/mandat-arbeitsbereich` nicht benötigt."

### Schritt 2: Unterbefehl ausführen

#### `neu <slug>`

1. Prüfen, ob der Slug noch nicht in `mandate/<slug>/` oder `mandate/_archiviert/<slug>/` existiert. Bei Kollision: anderen Slug wählen lassen.
2. Aufnahmeinterview:
   - **Mandant** (zu vertretende Partei oder interne Abteilung bei Syndikusanwalt)
   - **Gegenseite** (eine oder mehrere)
   - **Mandatstyp**: Zivilstreitigkeit | Arbeitsrechtssache | Verwaltungsverfahren | Strafverteidigung | Steuerrechtsstreit (FGO) | Sozialrechtsstreit (SGG) | IP-Streit | sonstiges
   - **Vertraulichkeitsstufe**: Standard | erhöht | Clean-Team
   - **Sachverhalt** (2–5 Sätze: Gegenstand, Beteiligte, Streitwert/Risiko, Besonderheiten)
   - **Mandatsspezifische Abweichungen vom Kanzleistandard** (z. B. „Mandant verlangt wöchentliche Statusberichte", „Gegenseite ist Geschäftspartner — deeskalierender Ton")
   - **Verwandte Mandate** (Slugs verbundener Sachen)
3. `mandate/<slug>/akte.md` nach Vorlage unten schreiben.
4. `mandate/<slug>/verlauf.md` mit Eröffnungseintrag seeden.
5. Leere `mandate/<slug>/notizen.md` anlegen.
6. Nicht automatisch wechseln — fragen: „Soll auf `<slug>` gewechselt werden? (`/prozessrecht:mandatsarbeitsbereich wechseln <slug>`)"

#### `liste`

`mandate/*/akte.md` auflisten. Tabelle ausgeben:

| Slug | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. Archivierte Mandate unter separater Überschrift „Archiviert".

#### `wechseln <slug>`

1. Bestätigen, dass `mandate/<slug>/akte.md` existiert.
2. `Aktives Mandat:`-Zeile in der Kanzlei-`CLAUDE.md` auf `<slug>` setzen.
3. Zusammenfassung der `akte.md` anzeigen zur Bestätigung.

#### `schließen <slug>`

1. Bestätigen, dass `mandate/<slug>/` existiert.
2. Eintrag „Mandat abgeschlossen" in `mandate/<slug>/verlauf.md` mit heutigem Datum anhängen.
3. `mandate/<slug>/` nach `mandate/_archiviert/<slug>/` verschieben (nicht löschen — § 50 Abs. 2 BRAO).
4. War das geschlossene Mandat das aktive, `Aktives Mandat:` auf `keins — nur Kanzleiebene` setzen.

#### `keins`

`Aktives Mandat:` in der Kanzlei-`CLAUDE.md` auf `keins — nur Kanzleiebene` setzen. Bestätigung anzeigen.

## Ausgabeformat

### Vorlage `akte.md`

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / clean-team]

---

## Parteien

**Mandant:** [Name]
**Gegenseite:** [Name(n)]

## Mandatstyp

[Zivilstreitigkeit | Arbeitsrechtssache | Verwaltungsverfahren | Strafverteidigung | FGO | SGG | IP | sonstiges — mit einzeiliger Begründung]

## Sachverhalt

[2–5 Sätze: Gegenstand, Beteiligte, Streitwert/Risiko, Besonderheiten gegenüber dem Kanzleistandard.]

## Mandatsspezifische Abweichungen

*Abweichungen vom Kanzleistandard, die nur für dieses Mandat gelten.*

- [z. B. „Prozesskostenfondlimit: Mandant besteht auf max. 50.000 EUR, nicht Standard 100.000 EUR."]
- [z. B. „Ton: deeskalierend — Gegenseite ist Geschäftspartner."]
- [z. B. „Gerichtsstand: Hamburg; abweichend vom Standardsitz München."]

## Verwandte Mandate

- [slug — ein Satz zur Verbindung]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer darf die Mandatsakte einsehen. Ob mandatsübergreifender Kontext trotz globaler Aktivierung untersagt ist.]
```

### Seed `verlauf.md`

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Chronologisches Ereignisprotokoll. Jüngster Eintrag oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Weiterer Anfangskontext — z. B. „Eröffnet nach Zustellung Klageschrift durch [Gegenseite] am [Datum]."]
```

## Beispiel

**Anfrage:** „Neues Mandat anlegen: Berufungsverfahren Müller GmbH gegen Bauer AG, OLG München, Streitwert 250.000 EUR."

**Unterbefehl:** `neu muellerGmbH-bauer-berufung-2025`

**Ergebnis:** `akte.md` wird angelegt mit Mandatstyp „Zivilstreitigkeit", Vertraulichkeit „standard", Sachverhalt aus den Angaben. `verlauf.md` mit Eröffnungseintrag vom heutigen Tag geseeded. Frage: „Auf `muellerGmbH-bauer-berufung-2025` wechseln?"

## Risiken und typische Fehler

- **Mandatsübergreifende Informationsweitergabe:** Ohne strikte Trennung können Informationen aus Mandat A bei der Bearbeitung von Mandat B sichtbar werden — Verstoß gegen § 43a Abs. 2 BRAO. Das Flag `Mandatsübergreifender Kontext: aus` (Standard) verhindert dies.
- **Löschung statt Archivierung:** Archivierte Mandate dürfen nicht gelöscht werden (§ 50 Abs. 2 BRAO: 5 Jahre Aufbewahrung). `schließen` verschiebt nur.
- **Konfliktkontrolle nicht Aufgabe dieses Skills:** Die Aufnahme erfasst die Angaben des Anwalts; eine eigenständige Konfliktkontrolle kann das Plugin nicht ersetzen.
- **Slug-Kollision mit archivierten Mandaten:** Wird ein Slug wiederverwendet, der in `_archiviert/` liegt, ist das archivierte Mandat unter `_archiviert/<slug>/` weiter lesbar.
- **Retention/Aufbewahrung:** Das Schließen archiviert; Löschfristen nach § 50 BRAO und DSGVO Art. 17 sind Sache der Kanzlei.

## Quellenpflicht

- Gesetzestexte: §§ 43a, 45, 46, 50 BRAO; § 3 BORA; Art. 32 DSGVO; § 1 BDSG
- Rechtsprechung: BGH, Urt. v. 05.11.2009 – IX ZR 214/08, NJW 2010, 73; BGH, Urt. v. 14.07.2016 – IX ZR 291/14, NJW 2016, 3235
- Kommentare: Dittmann, in: Henssler/Prütting, BRAO, 5. Aufl. 2023, § 43a; Römermann, in: BeckOK BRAO, 21. Ed. 2024, § 50

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
