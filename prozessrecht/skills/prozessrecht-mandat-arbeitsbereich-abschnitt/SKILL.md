---
name: prozessrecht-mandat-arbeitsbereich-abschnitt
description: "Mandat Arbeitsbereich Abschnitt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandat Arbeitsbereich Abschnitt

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandat Arbeitsbereich Abschnitt** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `prozessrecht-anpassen` | Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: §§ 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten. Output: Strategieanpassungs-Vermerk. Abgrenzung: nicht Berufungs-Skill. |
| `prozessrecht-mandat-arbeitsbereich` | Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: nicht Kanzlei-Builder-Hub-Skill. |
| `schriftsatz-abschnitt` | Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in Klageschrift oder Erwiderung. Abgrenzung: nicht vollständige Klageschrift. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Mandat Arbeitsbereich Abschnitt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `prozessrecht-anpassen`

**Fokus:** Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: §§ 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten. Output: Strategieanpassungs-Vermerk. Abgrenzung: nicht Berufungs-Skill.

# Praxisprofil anpassen

## Triage — kläre vor der Anpassung

1. **Welches Feld?** Welches Profilfeld soll geändert werden (Rolle, Schwerpunkt, Risikostrategie, Integration)?
2. **Einzeln oder vollständig?** Sollen nur bestimmte Felder geändert oder das gesamte Profil neu aufgesetzt werden (dann Kaltstart-Interview)?
3. **Berufsrechtliche Relevanz:** Hat die geänderte Einstellung berufsrechtliche Folgen (Rollenwechsel, Vergütungsart)?
4. **Integrationscheck:** Muss nach der Änderung `--check-integrations` ausgeführt werden?
5. **Vorher-Nachher-Bestätigung:** Soll der Vergleich der geänderten Felder vor dem Speichern bestätigt werden?

## Zentrale Normen
- § 43a BRAO (Grundpflichten des Rechtsanwalts — Verschwiegenheit, sachlich unabhängige Beratung)
- § 46a BRAO (Syndikusrechtsanwalt — besondere Rollenpflichten)
- § 46c BRAO (Vertretungsverbote des Syndikusrechtsanwalts)
- § 3a RVG (Vergütungsvereinbarung — Textformerfordernis)
- § 4a RVG (Erfolgshonorar — Voraussetzungen)
- BORA §§ 2, 3 (Sachlichkeit und Grundpflichten)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Gezielte Änderung einzelner Felder des Praxisprofils in CLAUDE.md, ohne den gesamten Kaltstart-Prozess zu wiederholen. Geeignet für Wechsel des Praxisschwerpunkts, Anpassung der Risikostrategie, Aktivierung neuer Integrationen oder Korrektur falscher Angaben.

## Eingaben

- Eines oder mehrere zu ändernde Felder (z. B. "Schwerpunkt auf Strafrecht hinzufügen", "Outlook MCP aktivieren")
- Optional: `--alle` – zeigt alle aktuellen Einstellungen zur Auswahl

## Ablauf

1. **Aktuelle CLAUDE.md einlesen:** Alle bestehenden Profilwerte anzeigen.
2. **Änderungswunsch präzisieren:** Falls unklar, welches Feld geändert werden soll, Auswahl anbieten.
3. **Neuen Wert erfassen:** Validierung gegen zulässige Werte (z. B. Praxisschwerpunkte-Liste).
4. **CLAUDE.md aktualisieren:** Nur das geänderte Feld überschreiben.
5. **Bestätigung:** Vorher-Nachher-Vergleich der geänderten Felder ausgeben.
6. **Integrations-Check (optional):** Bei Aktivierung einer neuen Integration automatisch `--check-integrations` ausführen.

## Quellen und Zitierweise

Keine gesonderten Normen. Allgemein: §§ 43a BRAO, 3a RVG bei rollenbezogenen Änderungen.

## Ausgabeformat

```
Änderung gespeichert:
 Feld: praxis_schwerpunkte
 Alt: ["ZPO", "ArbGG"]
 Neu: ["ZPO", "ArbGG", "StPO"]

CLAUDE.md aktualisiert. Alle Skills verwenden ab sofort das neue Profil.
```

## Risiken / typische Fehler

- **Rollenwechsel mit Rechtsfolgen:** Wechsel von Rechtsanwalt zu Syndikusrechtsanwalt (§ 46a BRAO) hat berufsrechtliche Konsequenzen; das Plugin dokumentiert den Wechsel, ersetzt aber keine standesrechtliche Beratung.
- **Überschreiben statt Ergänzen:** Bei Praxisschwerpunkten immer prüfen, ob bestehende Einträge erhalten bleiben sollen; Default ist Ergänzung, nicht Überschreiben.

## 2. `prozessrecht-mandat-arbeitsbereich`

**Fokus:** Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: nicht Kanzlei-Builder-Hub-Skill.

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
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


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
# Verlauf: [Mandant] — [Kurzbeschreibung]

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

## 3. `schriftsatz-abschnitt`

**Fokus:** Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in Klageschrift oder Erwiderung. Abgrenzung: nicht vollständige Klageschrift.

# Schriftsatzabschnitt-Entwurf

## Zweck

Entwurf einzelner Abschnitte eines Schriftsatzes – Klageschrift, Klageerwiderung, Replik, Duplik, Berufungsbegründung (§ 520 ZPO), Revisionsbegründung (§ 551 ZPO), Beschwerdeerwiderung oder anderer Schriftsätze – im Urteilsstil nach deutschem Prozessrecht. Der Skill arbeitet mandatsspezifisch auf Basis der mandat.md und verlauf.md des aktiven Mandats und hält den Kanzleistil aus CLAUDE.md ein.

## Eingaben

- Aktives Mandat (Slug) mit mandat.md und verlauf.md
- Bezeichnung des gewünschten Abschnitts (z. B. "Sachverhaltsdarstellung", "Rechtliche Ausführungen zu Klageantrag 1", "Berufungsangriff I: Übergangener Beweisantrag")
- Anspruchstabelle (falls vorhanden, aus `/anspruchstabelle`)
- Chronologie (falls vorhanden, aus `/chronologie`)
- Beizufügende Dokumente / Anlagen (Vertrag, Schriftverkehr, Sachverständigengutachten)
- Gewünschte Schriftsatzart und verfahrensrechtliche Situation

## Ablauf

1. **Mandatsdaten laden:** mandat.md, verlauf.md, ggf. Chronologie und Anspruchstabelle einlesen. Mandatstheorie und Kanzleistil aus CLAUDE.md laden.

2. **Abschnittstyp bestimmen:**
 - **Klageschrift** (§§ 253, 261 ZPO): Rubrum, Anträge, Sachverhaltsdarstellung, Rechtliche Ausführungen, Beweisangebote.
 - **Klageerwiderung** (§ 277 ZPO): Bestreiten (erheblich/unerheblich), Gegendarstellung, Rechtsausführungen, eigene Anträge, Hilfsaufrechnung/Widerklage.
 - **Berufungsbegründung** (§ 520 Abs. 3 ZPO): Darlegung der Berufungsangriffe, Bezifferung von Rechtsverletzungen (§ 546 ZPO), neue Tatsachen und Beweise (§ 531 Abs. 2 ZPO), Berufungsanträge.
 - **Revisionsbegründung** (§ 551 Abs. 3 ZPO): Revisionsgründe (§ 545 ZPO), absolute Revisionsgründe (§ 547 ZPO), Rüge der Nichtzulassung (§ 544 ZPO), Grundsatzrevision (§ 543 Abs. 2 ZPO).
 - **Beschwerde** (§§ 567 ff., 574 ff. ZPO): Statthaftigkeit, Frist, Begründung.

3. **Urteilsstil anwenden:** Tatsachenvortrag in indirekter Rede oder Behauptungsform, normative Subsumtion knapp, Beweisangebote vollständig.

4. **Normen und Rechtsprechung einarbeiten:** Jede Behauptung rechtlicher Art mit Norm und – soweit verfügbar – BGH-Rechtsprechung nach Zitierweise (../references/zitierweise.md) belegen.

5. **Beweisangebote formulieren:** Für jeden bestrittenen Tatsachenbehauptung ein konkretes Beweisangebot (Zeugnis, Sachverständiger, Urkunde, Augenschein, Parteivernehmung § 447 ZPO, Geständnisfiktion § 138 Abs. 3 ZPO).

6. **Lückenprüfung:** Fehlende Tatsachenbehauptungen, unklare Beweisangebote, ungeklärte Passivlegitimation, fehlende Kausalität und Schaden als **[LÜCKE: …]** markieren.

7. **Entwurf ausgeben:** Urteilsstil, kanzleispezifisches Format, Fristen am Ende der Ausgabe.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

Einschlägige Kommentare und Rechtsprechung:

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

Schriftsatzformat im deutschen Standard:
1. **Rubrum** (Gericht, Parteien, Az., Datum) – sofern vollständiger Schriftsatz
2. **Abschnittsüberschrift** (z. B. "I. Sachverhaltsdarstellung", "III. Zum Berufungsangriff")
3. **Fließtext im Urteilsstil** mit Randnummern (fakultativ)
4. **Beweisangebote** am Ende jedes bestrittenen Tatsachenblocks
5. **Lücken-Notizen** in Klammern: `[LÜCKE: Beleg für Fristversäumnis fehlt]`
6. **Fristenliste** am Ende des Outputs

## Beispiel

> **III. Zur Berufungsbegründung – Verletzung des § 286 ZPO**
>
> Das Landgericht hat das Beweisangebot der Klägerin auf Vernehmung des Zeugen Müller (Schriftsatz v. 14.03.2023, S. 7) übergangen, ohne dies in den Entscheidungsgründen zu begründen. Dies verletzt Art. 103 Abs. 1 GG und § 286 Abs. 1 ZPO.
>
> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
>
> *Beweis: Zeugnis des Herrn Max Müller, [Anschrift] – Beweis-Nr. 5.*

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Berufungsbegründungsfrist:** § 520 Abs. 2 ZPO: 2 Monate ab Urteilszustellung; verlängerbar auf Antrag, aber nur mit gegnerischer Zustimmung oder wichtigem Grund.
- **Neue Tatsachen in der Berufung:** § 531 Abs. 2 ZPO begrenzt neues Vorbringen; stets prüfen, ob Nachlässigkeit im ersten Rechtszug vorlag.
- **Revisionsanforderungen:** § 543 Abs. 2 ZPO – Grundsatzbedeutung oder Sicherung einheitlicher Rechtsprechung; ohne NZB-Begründung keine Revision (§ 544 ZPO).
- **Verstoß gegen § 138 ZPO:** Wahrheitspflicht; keine Behauptung ins Blaue hinein; Darlegungs- und Beweislast nicht verwechseln.
- **Berufsrechtliche Hinweispflicht:** Bei überraschenden Rechtswendungen ist der Mandant nach § 43 BRAO zu informieren; kein Schriftsatz ohne Rücksprache versenden.

---

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 73/20, NJW 2021, 1886 Rn. 15 (" neue Angriffsmittel § 531 ZPO ") – Zitatfehler (WRONG_TOPIC). Das Urteil behandelt Verletzung des allgemeinen Persönlichkeitsrechts / Bestimmtheit Klageantrags bei Erstbegehungsgefahr (NJW 2021, 1756), nicht neue Angriffsmittel nach § 531 ZPO (dejure.org/2021,4358). Eintrag ersatzlos gelöscht; kein verifizierbarer Ersatz mit identischem NJW-Fundstelle ermittelt.
Quelle : https://dejure.org/2021,4358
Aktion : Zeile entfernt
-->
