---
name: gegenseite-status-mahnbescheid-mahnschreiben
description: "Wenn es um Statusabfrage Externe Bevollmächtigte in Prozessrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik."
---

# Statusabfrage Externe Bevollmächtigte

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Mandatsprotokoll `_log.yaml`**: Filterquelle und Feldquelle
- **`akte.md` und `verlauf.md`** je Mandat: Mandatskontext und aktuelle Entwicklungen
- **Kanzleikonfiguration `CLAUDE.md`**: Direktive für externe Bevollmächtigte (Tonvorgabe), Unterzeichner, Budgethaltung
- **Flags** (optional): `--alle`, `--slug=[bezeichnung]`, `--kein-outlook`

## Rechtlicher Rahmen

### Kernvorschriften

- **Paragraf 11 BORA** — Mandatsbearbeitung und Unterrichtung: Der Rechtsanwalt unterrichtet den Mandanten angemessen über wesentliche Vorgänge und gibt auf Anfrage Auskunft über den Stand des Mandats.
- **Paragrafen 675 und 666 BGB** — Auskunft und Rechenschaft aus dem anwaltlichen Geschäftsbesorgungsvertrag; der externe Bevollmächtigte teilt erforderliche Nachrichten mit und gibt auf Verlangen Auskunft über den Bearbeitungsstand.
- **Paragraf 43a Absatz 4 BRAO** — Verbot der Vertretung widerstreitender Interessen; vor einer Statusweitergabe ist zu prüfen, ob Mandate, Beteiligte oder Informationsräume kollidieren.
- **Paragraf 43a Abs. 2 BRAO** — Vertraulichkeit; die Statuskorrespondenz mit externen Bevollmächtigten ist durch die gemeinsame Verschwiegenheitspflicht geschützt.
- **Paragraf 49b BRAO; Paragrafen 2 ff. RVG** — Vergütung; Budgetanfragen und Kostenkontrollen im Statusschreiben orientieren sich am vereinbarten Honorar und etwaigen Vergütungsrahmen.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Schritt 1: Mandate filtern

**Standardfilter:**

- `status != geschlossen`
- `externe_bevollmaechtigte.sozietaet != null` UND `externe_bevollmaechtigte.partner != null`
- Entweder: letzte Aktualisierung vor mehr als 10 Tagen ODER `nächste_frist` innerhalb von 21 Tagen

Übersprungen werden: Mandate mit Update in den letzten 10 Tagen (kein erneutes Anschreiben erforderlich) sowie Mandate ohne hinterlegte E-Mail-Adresse des externen Bevollmächtigten (Markdown-Entwurf wird trotzdem erstellt; Outlook-Entwurf nicht).

**Flags:**
- `--alle` → Entwurf für alle aktiven Mandate, unabhängig von der Aktualität
- `--slug=[bezeichnung]` → Entwurf nur für ein Mandat (Ad-hoc-Anfrage)
- `--kein-outlook` → kein Outlook-Entwurf, auch wenn MCP verfügbar

### Schritt 2: Je Mandat — E-Mail-Entwurf erstellen

Jede E-Mail folgt demselben Grundgerüst; Inhalt ist mandatsspezifisch.

**Betreff:** gemäß Kanzleidirektive (Fallback: `[Mandat: [Bezeichnung]] — Wöchentlicher Sachstand`)

**Rumpf-Gerüst:**

```
[Vorname des Partneranwalts],

[Ein einleitender Satz — natürlich, entspricht dem Kanzleiston.]

Kurze Rückmeldung zu [Mandatsbezeichnung] erbeten. Einige Punkte:

1. **Sachstand seit [Datum der letzten Aktualisierung aus verlauf.md]** — Was hat sich bewegt, was ist noch offen? Gab es Schriftsätze, Termine, Korrespondenz oder Telefonate seit unserem letzten Austausch?

2. **Bevorstehende Fristen** — Ich vermerke [nächste_frist aus Protokoll + etwaige Fristen aus akte.md]. Bitte Abdeckungsplan bestätigen und ggf. weitere Termine mitteilen.

3. **Ausstehende Entscheidungen** — [offene Fragen aus akte.md, die externen Input erfordern; entfällt, falls keine vorhanden — umnummerieren]

4. **Budget** — [monatlich / quartalsweise / auf Anfrage gemäß Kanzleikonfiguration]. Wo stehen wir gegenüber [Budgetrahmen aus akte.md]? Gibt es Abweichungen?

[Falls wesentlich und relevant: 5. Konkrete Bitte — z. B. "Bitte Entwurf des Schriftsatzes vor [Datum] übersenden" — aus offenen Punkten in akte.md.]

[Grußformel — Name, Funktion, Kontakt. Aus Kanzleikonfiguration.]
```

Ton wird der Kanzleidirektive angepasst — einige Kanzleien schreiben förmlich, andere per Vorname und Stichpunkte. Die Direktive hat Vorrang.

### Schritt 3: Ausgabe erstellen

### Schritt 4: Abschicken-Schranke

Jedem Entwurf wird folgender Hinweis angefügt (vor dem Versenden entfernen):

> Dies ist ein Entwurf zur anwaltlichen Prüfung vor dem Versand an externe Bevollmächtigte. Prüfen Sie auf privilegierte Inhalte, die nicht aus dem Mandatsverhältnis herausgegeben werden sollten, sachliche Richtigkeit, Ton und Budgethaltung. Auch routinemäßige Wochenanfragen können Strategie, Positionierungen oder unbeabsichtigte Zugeständnisse enthalten.

```markdown
## Entwurf erstellt für

| Mandat | Externer Partner | Zuletzt aktualisiert | Grund der Aufnahme |
|---|---|---|---|
| [slug] | [Partner] | [Datum] | [veraltet / bevorstehende Frist / --alle / --slug] |

## Übersprungen

| Mandat | Grund |
|---|---|
| [slug] | aktuelles Update (zuletzt bearbeitet [Datum]) |
| [slug] | keine E-Mail des externen Bevollmächtigten im Protokoll — nachtragen mit `/mandat-update [slug]` |

## Auffälligkeiten

- Mandate ohne externe Bevollmächtigte: [Liste — bei hohem/kritischem Risiko gesondert markiert]
- Mandate mit externen Bevollmächtigten, aber ohne E-Mail-Adresse: [Liste]
```

## Beispiel

**Sachverhalt:** Mandat `bauer-ag-berufung-2025`, OLG Hamburg. Letztes Update vor 14 Tagen. Nächste Frist: Berufungserwiderung in 18 Tagen. Externer Partner: RA Dr. Schneider, Schneider & Partner.

**Ergebnis:** Entwurf mit Statusanfrage zu eingereichten Schriftsätzen seit letztem Austausch, Bestätigung der Berufungserwiderungsfrist, Budget-Abfrage gemäß Quartals-Direktive. Gespeichert unter `gegenseite-status/2025-05-12/bauer-ag-berufung-2025.md`.

## Risiken und typische Fehler

- **Vertraulichkeit:** Die Statuskorrespondenz mit externen Bevollmächtigten ist durch Paragraf 43a Abs. 2 BRAO geschützt; Entwürfe nicht an Personen außerhalb des Mandatskreises weitergeben.
- **Nicht geprüfte Entwürfe versenden:** Auch kurze Statusanfragen können strategische Hinweise, Budgetkonzessionen oder unbeabsichtigte Zugaben enthalten.
- **Veraltete Kontaktdaten:** Falls die E-Mail des externen Partners nicht im Protokoll hinterlegt ist, wird kein Outlook-Entwurf angelegt; der Nutzer erhält einen Hinweis, die Daten nachzupflegen.
- **Mandatsübergreifende Abfrage:** Nur bei aktivem `Mandatsübergreifender Kontext: an` in der Kanzleikonfiguration darf das System mandatsübergreifend lesen.

## Quellenpflicht

- Gesetzestexte: Paragrafen 43a, 49b BRAO; Paragrafen 2 ff. RVG; Paragraf 667 BGB
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
