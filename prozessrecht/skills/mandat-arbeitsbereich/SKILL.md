---
name: mandat-arbeitsbereich
description: "Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: nicht Kanzlei-Builder-Hub-Skill im Prozessrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Mandatsarbeitsbereich

## Arbeitsbereich

Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: nicht Kanzlei-Builder-Hub-Skill. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Schritt 1: Konfiguration prüfen

Lies `CLAUDE.md` → Abschnitt `## Mandatsarbeitsbereiche`. Ist `Aktiviert: ✗`:

> "Mandatsarbeitsbereiche sind deaktiviert — die Kanzlei ist als Einmandat-Kanzlei (z. B. Syndikusrechtsanwalt nach § 46 BRAO) konfiguriert und arbeitet automatisch auf Kanzleiebene. Falls tatsächlich mehrere Mandate geführt werden, bitte `/prozessrecht:prozessrecht-kaltstart-interview --neu` ausführen und eine Mehrmandat-Kanzlei auswählen. Andernfalls wird `/mandat-arbeitsbereich` nicht benötigt."

### Schritt 2: Unterbefehl ausführen

#### `neu <slug>`

1. Prüfen, ob der Slug noch nicht in `mandate/<slug>/` oder `mandate/_archiviert/<slug>/` existiert. Bei Kollision: anderen Slug wählen lassen.
2. Aufnahmeinterview:
 - **Mandant** (zu vertretende Partei oder interne Abteilung bei Syndikusanwalt)
 - **Gegenseite** (eine oder mehrere)
 - **Mandatstyp**: Zivilstreitigkeit | Arbeitsrechtssache | Verwaltungsverfahren | Strafverteidigung | Steuerrechtsstreit (FGO) | Sozialrechtsstreit (SGG) | IP-Streit | sonstiges
 - **Vertraulichkeitsstufe**: Standard | erhöht | Clean-Team
 - **Sachverhalt** (2–5 Sätze: Gegenstand, Beteiligte, Streitwert/Risiko, Besonderheiten)
 - **Mandatsspezifische Abweichungen vom Kanzleistandard** (z. B. "Mandant verlangt wöchentliche Statusberichte", "Gegenseite ist Geschäftspartner — deeskalierender Ton")
 - **Verwandte Mandate** (Slugs verbundener Sachen)
3. `mandate/<slug>/akte.md` nach Vorlage unten schreiben.
4. `mandate/<slug>/verlauf.md` mit Eröffnungseintrag seeden.
5. Leere `mandate/<slug>/notizen.md` anlegen.
6. Nicht automatisch wechseln — fragen: "Soll auf `<slug>` gewechselt werden? (`/prozessrecht:prozessrecht-mandat-arbeitsbereich wechseln <slug>`)"

#### `liste`

`mandate/*/akte.md` auflisten. Tabelle ausgeben:

| Slug | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. Archivierte Mandate unter separater Überschrift "Archiviert".

#### `wechseln <slug>`

1. Bestätigen, dass `mandate/<slug>/akte.md` existiert.
2. `Aktives Mandat:`-Zeile in der Kanzlei-`CLAUDE.md` auf `<slug>` setzen.
3. Zusammenfassung der `akte.md` anzeigen zur Bestätigung.

#### `schließen <slug>`

1. Bestätigen, dass `mandate/<slug>/` existiert.
2. Eintrag "Mandat abgeschlossen" in `mandate/<slug>/verlauf.md` mit heutigem Datum anhängen.
3. `mandate/<slug>/` nach `mandate/_archiviert/<slug>/` verschieben (nicht löschen — § 50 Abs. 2 BRAO).
4. War das geschlossene Mandat das aktive, `Aktives Mandat:` auf `keins — nur Kanzleiebene` setzen.

#### `keins`

`Aktives Mandat:` in der Kanzlei-`CLAUDE.md` auf `keins — nur Kanzleiebene` setzen. Bestätigung anzeigen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Prozessrechtlichen Mandats-Workspace aufbauen | Arbeitsbereich nach Schema; Template unten |
| Variante A — Mandat nur beratend kein Klageauftrag | Beratungsmandat; Prozess-Template weglassen |
| Variante B — Mehrere Instanzen parallel | Instanzübergreifende Workspace-Struktur; separate Aktenteile |
| Variante C — Internationales Verfahren Schiedsgericht | Schiedsverfahrens-Workspace; anderen Skill parallel einsetzen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Ausgabeformat

### Vorlage `akte.md`

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

### Mandat: [Mandant] — [Kurzbeschreibung]

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

- [z. B. "Prozesskostenfondlimit: Mandant besteht auf max. 50.000 EUR, nicht Standard 100.000 EUR."]
- [z. B. "Ton: deeskalierend — Gegenseite ist Geschäftspartner."]
- [z. B. "Gerichtsstand: Hamburg; abweichend vom Standardsitz München."]

## Verwandte Mandate

- [slug — ein Satz zur Verbindung]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer darf die Mandatsakte einsehen. Ob mandatsübergreifender Kontext trotz globaler Aktivierung untersagt ist.]
```

### Seed `verlauf.md`

```markdown
### Verlauf: [Mandant] — [Kurzbeschreibung]

Chronologisches Ereignisprotokoll. Jüngster Eintrag oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Weiterer Anfangskontext — z. B. "Eröffnet nach Zustellung Klageschrift durch [Gegenseite] am [Datum]."]
```

## Beispiel

**Anfrage:** "Neues Mandat anlegen: Berufungsverfahren Müller GmbH gegen Bauer AG, OLG München, Streitwert 250.000 EUR."

**Unterbefehl:** `neu muellerGmbH-bauer-berufung-2025`

**Ergebnis:** `akte.md` wird angelegt mit Mandatstyp "Zivilstreitigkeit", Vertraulichkeit "standard", Sachverhalt aus den Angaben. `verlauf.md` mit Eröffnungseintrag vom heutigen Tag geseeded. Frage: "Auf `muellerGmbH-bauer-berufung-2025` wechseln?"

## Risiken und typische Fehler

- **Mandatsübergreifende Informationsweitergabe:** Ohne strikte Trennung können Informationen aus Mandat A bei der Bearbeitung von Mandat B sichtbar werden — Verstoß gegen § 43a Abs. 2 BRAO. Das Flag `Mandatsübergreifender Kontext: aus` (Standard) verhindert dies.
- **Löschung statt Archivierung:** Archivierte Mandate dürfen nicht gelöscht werden (§ 50 Abs. 2 BRAO: 5 Jahre Aufbewahrung). `schließen` verschiebt nur.
- **Konfliktkontrolle nicht Aufgabe dieses Skills:** Die Aufnahme erfasst die Angaben des Anwalts; eine eigenständige Konfliktkontrolle kann das Plugin nicht ersetzen.
- **Slug-Kollision mit archivierten Mandaten:** Wird ein Slug wiederverwendet, der in `_archiviert/` liegt, ist das archivierte Mandat unter `_archiviert/<slug>/` weiter lesbar.
- **Retention/Aufbewahrung:** Das Schließen archiviert; Löschfristen nach § 50 BRAO und DSGVO Art. 17 sind Sache der Kanzlei.

## Quellenpflicht

- Gesetzestexte: §§ 43a, 45, 46, 50 BRAO; § 3 BORA; Art. 32 DSGVO; § 1 BDSG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
