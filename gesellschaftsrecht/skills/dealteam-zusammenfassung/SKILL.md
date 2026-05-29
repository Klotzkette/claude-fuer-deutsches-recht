---
name: dealteam-zusammenfassung
description: "Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status für Geschäftsführung, Team-Update, Deal-Team-Summary."
---

# Deal-Team-Zusammenfassung

## Triage zu Beginn

Vor der Erstellung des Briefings klären:

1. **Ebene bestimmen:** Welche Ebene wird zuerst benötigt — GF-Kurzfassung, Deal-Lead-Briefing oder Arbeitsteam-Vollständigkeit?
2. **DD-Stand:** Sind alle DD-Kategorien abgeschlossen oder nur Teilbereiche?
3. **Vollzugsstatus:** Ist die Vollzugscheckliste aktuell gepflegt?
4. **Adressat:** Wer erhält welche Ebene? (GF-Kurzfassung häufig nach außen; Ebene 3 bleibt im Privilegierungskreis)
5. **Zeitdruck:** Ist Signing in weniger als 48 Stunden (dann Ebene 1 und 2 prioritär)?
6. **Preisrelevanz:** Gibt es blockierende Findings, die eine Kaufpreisanpassung erfordern?

## Zentrale Normen

§§ 311 Abs. 2, 241 Abs. 2 BGB (vorvertragliche Aufklärungspflichten) — §§ 443, 444 BGB (Garantien, Haftungsausschluss) — § 442 BGB (Kenntnis des Käufers) — §§ 35 ff. GWB (Fusionskontrolle) — §§ 55 ff. AWV, § 5 AWG (FDI-Investitionsprüfung) — § 15 GmbHG (Abtretung) — § 613a BGB (Betriebsübergang)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

M&A-Teams brauchen je nach Ebene unterschiedliche Informationstiefe: Die Geschäftsführung will drei Sätze und eine Risikobewertung. Der Deal-Lead will kritischen Pfad und offene Punkte. Das Arbeitsteam will alle Findings mit Quellen. Dieser Skill erstellt alle drei Ebenen aus denselben DD-Quellen.

## Eingaben

- DD-Issue-Extraktions-Findings aus dem laufenden Mandat
- Vollzugscheckliste (aktueller Status)
- Wesentliche-Verträge-Anlage (wenn vorhanden)
- Deal-Kontext: Parteien, Transaktionsstruktur, Kaufpreis, Zieldatum Vollzug
- Praxisprofil: `## M&A → Deal-Team-Briefing` (Rhythmus, Format, Adressat)

## Schritt-fuer-Schritt-Workflow

### Schritt 1: Quellen zusammenführen

Aus dem Mandatsordner lesen:
- `mandate/[code]/dd-issues-[kategorie].md` (alle Kategorien)
- `mandate/[code]/vollzugs-checkliste.yaml`
- `mandate/[code]/wesentliche-vertraege-anlage.md` (falls vorhanden)
- `mandate/[code]/deal-kontext.md`

Gesamtbild: Anzahl Findings je Schweregrad; blockierende Vollzugspunkte; kritischer Pfad.

### Schritt 2: Drei Briefing-Ebenen erstellen

**Ebene 1 – GF-Kurzfassung (max. 1 Seite):** Kernrisiken, Vollzugsstatus, Handlungsempfehlung.

**Ebene 2 – Deal-Lead-Briefing (2-4 Seiten):** Alle Kategorien mit Findings-Tabelle, kritischer Pfad, offene Fragen.

**Ebene 3 – Arbeitsteam-Vollständigkeit:** Alle Findings mit Quellen, sortiert nach Schweregrad.

### Schritt 3: Vollzugs-Handlungs-Abgleich

Nach Erstellung: prüfen, ob neue Vollzugspunkte aufgedeckt wurden, die in der Vollzugscheckliste fehlen. Falls ja: als Übergabe-Items für den Vollzugscheckliste-Skill markieren.

## Output-Template

**Adressat je Ebene; Tonfall:** Ebene 1 verständlich-entscheidungsorientiert; Ebene 2+3 sachlich-juristisch

### Ebene 1 — GF-Kurzfassung

```
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

# [DEAL-CODE] — Statusbericht — [DATUM]

Transaktion: Erwerb [ZIELGESELLSCHAFT] durch [KAEUFER]; Kaufpreis: [X] EUR;
Vollzug geplant: [DATUM].

Gesamteinschätzung: [Erhebliche offene Punkte / Klärungsbedarf / Auf Kurs]

Kernrisiken:
1. [RISIKO] — [Implikation in einem Satz]
2. [RISIKO] — [Implikation in einem Satz]
3. [RISIKO] — [Implikation in einem Satz]

Vollzugsstatus: [N] von [N] VB erfüllt. Kritischer Pfad: [PUNKT + DATUM].

Empfehlung: [Fortsetzen / Preis anpassen / Klärung einholen / Abbruch erwägen]
```

### Ebene 2 — Deal-Lead-Briefing

```
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

# [DEAL-CODE] — Deal-Lead-Briefing — [DATUM]

## Transaktionsübersicht
[Parteien, Struktur, Preis, Timeline]

## DD-Ergebnisse nach Kategorie

| Kategorie | Rot | Orange | Gelb | Gruen | Top-Finding |
|---|---|---|---|---|---|
| Gesellschaftsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| Wesentliche Verträge | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |
| IP / Technologie | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |
| Arbeitsrecht | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |
| Umwelt / Regulatorisch | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |

## Vollzugsblockaden (Blockierend)
[Jeder blockierende Punkt mit Verantwortlichem und Fälligkeit]

## Kritischer Pfad
[Liste mit Fälligkeiten; gefährdete Punkte hervorgehoben]

## Offene Fragen für Entscheidung
1. [FRAGE] — Entscheidung bis [DATUM] benötigt

## Preisanpassung / Risikoreservierung
[Falls blockierende Findings preisrelevant sind: quantifizierte Risikoschätzung]
```

## Rote Schwellen

- Blockierende Findings ohne Vollzugsplan → sofortige Eskalation an GF/Investoren
- Kritischer Pfad-Punkt mit weniger als 14 Tagen Restzeit → tägliches Tracking
- Neue Vollzugsbedingungen nach Signing entdeckt → SPA-Parteien informieren
- Ebene 3 an Gegenseite gesandt → Mandatsgeheimnis (§ 43a Abs. 2 BRAO) gefährdet

## Quellen und Zitierweise

Normen-Basis je nach DD-Findings. Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Risiken / typische Fehler

- **Ebenenverwirrung:** GF-Kurzfassung niemals mit Arbeitsteam-Vollständigkeit mischen.
- **Preisanpassung ohne Quantifizierung:** Blockierende Findings ohne Risikowert lassen die GF ohne Entscheidungsgrundlage.
- **Vollzugspunkte nicht an Checkliste übergeben:** Diese Zusammenfassung ist der letzte Filter vor dem Vollzug.
- **Verteilungskreis:** Ebene 3 bleibt im Privilegierungskreis; nie an Gegenpartei senden.

---
## Audit-Hinweis (27.05.2026)

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: WRONG_TOPIC — das Urteil betrifft Prospekthaftung wegen falscher Darstellung eines Vorgängerfonds (Medienfonds ApolloProMedia, NJW-RR 2010, 911), nicht Aufklaerungspflicht beim Unternehmenskauf.
Maßnahme: Beide Nennungen entfernt (Rechtsprechungsabschnitt und Quellenabschnitt). Kein Ersatz eingefuegt; die verbleibenden drei Urteile decken Due Diligence und Vollzugsverbot zutreffend ab.
