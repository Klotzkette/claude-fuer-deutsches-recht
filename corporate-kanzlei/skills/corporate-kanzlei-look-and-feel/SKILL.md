---
name: corporate-kanzlei-look-and-feel
description: "Corporate-Cowork-Design: Definiert die visuelle Oberflaeche für Partner, Counsel und Associates. Ruhig, edel, blaeulich-silbern; Orange für Entscheidungspunkte. Statuskarten, Ampeln und dichte Deal-Information statt Marketing. Keine Spielerei, keine Dekoration."
---

# Corporate-Cowork-Look — Design und Ausgabestandard

## Triage — kläre vor der Ausgabegestaltung

1. Wer ist der Adressat — Partner/Counsel intern, Mandant, Gegenpartei, Aufsichtsrat oder Gericht?
2. Welches Ausgabeformat ist gefordert — Deal-Karte, Statusbericht, Präsentation, Protokoll, Schriftsatz?
3. Vertraulichkeitsstufe — intern, mandantenvertraulich, nur Partner?
4. Enthält die Ausgabe rote Schwellen oder Risiken, die optisch hervorgehoben werden müssen?
5. Ist die Ausgabe für ein Board Meeting oder Gremium bestimmt, das besonders klare Struktur braucht?

## Designprinzipien

### Farbpalette

| Element | Farbe / Stil | Verwendung |
|---|---|---|
| Hintergrund Hauptfläche | Sehr helles Blaugrau (#F0F4F8) | Standardhintergrund aller Ausgaben |
| Primärtext | Tiefdunkelblau (#1A2B4A) | Fließtext, Tabelleninhalt, Überschriften |
| Akzent — Entscheidungspunkte | Warmes Orange (#E87722) | Rote Schwellen, TODO, Deadlines, Freigabe |
| Akzent — Navigation / Links | Mittelblau (#2B6CB0) | Skill-Links, Anker, Querverweise |
| Tabellenhintergrund (gerade Zeilen) | Sehr helles Blau (#EBF4FF) | Lesbarkeit bei dichten Tabellen |
| Statusampel Grün | #38A169 | Workstream auf Kurs |
| Statusampel Gelb | #D69E2E | Verzögerung, Klärungsbedarf |
| Statusampel Rot | #E53E3E | Kritisch, rote Schwelle ausgelöst |
| Vertraulich-Markierung | Orange auf Dunkelblau | Deckblatt, Kopfzeile |

### Typografie

- **Überschriften (H1-H3):** Serifenlos, Gewicht Bold/SemiBold; keine kursiven Überschriften.
- **Fließtext:** Serifenlos, Regular; Zeilenlänge max. 90 Zeichen.
- **Tabellenkopf:** Bold, Kleinschrift ODER Normalschrift mit Unterstreichung.
- **Hervorhebungen:** Fett für Norm-/Aktenzeichen und Entscheidungspunkte; kursiv nur für Zitate.
- **Zahlen / Beträge:** Tausenderpunkt (`1.000`), Dezimalkomma (`12,82 EUR`), kein Apostroph.

### Struktur und Layout

- Statuskarten bevorzugen: kompakte Tabelle mit Phase / Owner / Deadline / Risiko / Aktion.
- Kein Fließtext-Wust: maximal 3 Sätze pro Absatz; dann Tabelle oder Liste.
- Aufzählungen mit genau einem Gedanken pro Zeile; keine Schachtelsätze.
- Jeder Ausgabeblock hat eine sichtbare Überschrift (H2 oder H3).
- Deal-Karten immer mit Ampelstatus; Risikostatus immer explizit.

## Ausgabestandards nach Adressat

| Adressat | Tonfall | Länge | Besonderheit |
|---|---|---|---|
| Partner / Counsel intern | Sachlich-juristisch, präzise | Kurz bis mittel | Deal-Karte + offene Punkte; keine Erklärungen |
| Associate intern | Anleitend, strukturiert | Mittel | Workflow-Schritte; Hinweise auf Normen und Muster |
| Mandant | Verständlich-erklärend | Mittel bis lang | Kein Fachjargon ohne Erläuterung; Handlungsempfehlung klar |
| Aufsichtsrat / Gremium | Sachlich, executive | Kurz | Executive Summary zuerst; Details in Anlage |
| Gegenpartei | Sachlich oder scharf-fristsetzend | Kurz bis mittel | Keine Konzessionen außer explizit gewünscht |
| Gericht | Formal-juristisch | Variabel | Schriftsatz-Format; Anträge zuerst |

## Schritt-für-Schritt-Workflow

1. **Adressat und Format bestimmen** — Ausgabe auf Tabelle oben anpassen.
2. **Vertraulichkeitsstufe prüfen** — Deckblatt oder Kopfzeile mit Vertraulichkeitsmarkierung.
3. **Risikoelemente identifizieren** — rote Schwellen und TODO farblich abheben (Orange).
4. **Struktur aufbauen:** Executive Summary → Statusampel → Hauptinhalt → Offene Punkte → Freigabegrad.
5. **Tabellen bevorzugen** — überall wo mehr als 3 Items verglichen werden.
6. **Qualitätscheck:** Text ohne Fließtextblöcke > 5 Zeilen? Ampelstatus sichtbar? Freigabegrad angegeben?
7. **Ausgabe finalisieren** — Version, Datum, Ersteller, Freigabestatus im Footer.

## Output-Template Standardausgabe Deal-Dokument

**Adressat:** Deal-Team / Mandant (anpassen) — Tonfall sachlich-präzise
```
[VERTRAULICH — NUR FÜR INTERNE VERWENDUNG / MANDANTENVERTRAULICH]

TITEL: [Bezeichnung des Dokuments]
Mandat: [Mandatsname / Kürzel]
Datum: [TT.MM.JJJJ]
Version: [Nr.]
Ersteller: [Name, Funktion]
Freigabe: [Name, Funktion, Datum oder "ausstehend"]

─────────────────────────────────────────────────────────────
EXECUTIVE SUMMARY
[2-3 Sätze: Kernbotschaft, wichtigste Risiken, empfohlene Aktion]
─────────────────────────────────────────────────────────────

STATUSÜBERSICHT
| Workstream | Status | Owner | Nächste Aktion | Deadline |
|-----------|--------|-------|----------------|---------|
| [WS 1]    | GRÜN   | [Name]| [Aktion]        | [Datum] |
| [WS 2]    | GELB   | [Name]| [Aktion]        | [Datum] |
| [WS 3]    | ROT    | [Name]| [Aktion — DRINGEND] | [Datum] |

─────────────────────────────────────────────────────────────
HAUPTINHALT
[Abschnitte mit H2-Überschriften; Tabellen bevorzugen]
─────────────────────────────────────────────────────────────

ROTE SCHWELLEN / ENTSCHEIDUNGSPUNKTE
[ ] [Schwelle 1: Beschreibung — Owner, Frist]
[ ] [Schwelle 2: Beschreibung — Owner, Frist]

OFFENE PUNKTE (TODO)
| Nr. | Punkt | Owner | Frist | Eskalation |
|----|-------|-------|-------|------------|
| 1  | [Punkt] | [Name] | [Datum] | [Stufe] |

─────────────────────────────────────────────────────────────
Freigabegrad: [Entwurf / Freigegeben / Vertraulich]
Nächste Review: [Datum]
```

## Rote Schwellen (Design)

- Text überlappt Tabellen oder Karten → Struktur korrigieren; Tabelle in eigenem Block.
- Ampel- oder Freigabestatus fehlt → Deal-Karte unvollständig; Ampelzeile ergänzen.
- Unerklärte Farben oder dekorative Flächen ohne Informationsgehalt → entfernen; Farbe hat semantische Bedeutung.
- Fließtextblock > 5 Zeilen ohne Strukturierung → in Tabelle oder nummerierte Liste umwandeln.
- Vertraulichkeitskennzeichnung fehlt bei mandantenvertraulichem Dokument → sofort ergänzen.

## Übergabe an andere Skills

- `corporate-kanzlei-kommandocenter` — Deal-Karte im Corporate-Cowork-Format
- `corporate-kanzlei-board-paper-business-judgment` — Board Paper in diesem Design-Standard
- `corporate-kanzlei-billing-narratives` — Billing-Output gemäß Design-Standard
- `corporate-kanzlei-output-versand-signing` — Versandpaket im Corporate-Cowork-Format

## Quellen und Vertiefung

- Keine spezifischen Rechtsnormen; Design-Standard ist prozessual, nicht materiell-rechtlich.
- Referenz: Corporate-Cowork-Designsystem (`assets/templates/cowork-ma-designsystem.md`)
- Vorlagen: `assets/templates/cowork-ma-dashboard.md`, `assets/templates/workflow-statuskarte.md`
