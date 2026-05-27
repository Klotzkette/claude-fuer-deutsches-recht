---
name: dealteam-zusammenfassung
description: "Erstellt gestaffelte Deal-Briefings fuer Geschaeftsfuehrung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status fuer Geschaeftsfuehrung, Team-Update, Deal-Team-Summary."
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

- BGH, Urt. v. 01.03.2010 – II ZR 213/08, NJW 2010, 1808 Rn. 14 — Beim Unternehmenskauf trägt der Käufer grundsätzlich das Risiko nicht offenbarter Mängel; Aufklärungspflicht des Verkäufers bei objektiv wesentlichen, wertbestimmenden Umständen, die der Käufer nicht selbst erkennen kann.
- BGH, Urt. v. 27.03.2009 – V ZR 30/08, NJW 2009, 2064 Rn. 25 — Due-Diligence-Pflicht des Käufers; Kenntnis von im Datenraum offengelegten Mängeln schließt Gewährleistung regelmäßig aus (§ 442 BGB).
- OLG Frankfurt, Urt. v. 10.09.2020 – 26 U 35/19 — Unzureichende Offenlegung im Datenraum heilte die Aufklärungspflichtverletzung nicht; späterer Hinweis auf versteckte Dokumente kann Sorgfaltspflicht nicht erfüllen.
- BGH, Urt. v. 08.01.2019 – KVZ 57/17, NJW 2019, 1067 — Vollzugsverbot nach § 41 GWB; rechtswidriger Vollzug vor Kartellfreigabe führt zu Bußgeld und Unwirksamkeit.

## Kommentarliteratur

- Westermann, in: MüKoBGB, 9. Aufl. 2022, § 453 Rn. 12 ff. (Unternehmenskauf, Gewährleistung und Due Diligence).
- MüKoGmbHG/Fleischer, 4. Aufl. 2022, § 15 Rn. 90 ff. (Abtretungsform GmbH-Anteile).
- Mestmäcker/Veelken, in: Immenga/Mestmäcker, GWB, 6. Aufl. 2021, § 35 Rn. 1 ff. (Fusionskontrolle; Vollzugsverbot).

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
| Gesellschaftsrecht | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |
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

Kommentarliteratur:
- MüKoGmbHG/Fleischer, 4. Aufl. 2022.
- Roth/Altmeppen, GmbHG, 11. Aufl. 2023.
- BGH, Urt. v. 01.03.2010 – II ZR 213/08, NJW 2010, 1808 (Risikoverteilung beim Unternehmenskauf).

## Risiken / typische Fehler

- **Ebenenverwirrung:** GF-Kurzfassung niemals mit Arbeitsteam-Vollständigkeit mischen.
- **Preisanpassung ohne Quantifizierung:** Blockierende Findings ohne Risikowert lassen die GF ohne Entscheidungsgrundlage.
- **Vollzugspunkte nicht an Checkliste übergeben:** Diese Zusammenfassung ist der letzte Filter vor dem Vollzug.
- **Verteilungskreis:** Ebene 3 bleibt im Privilegierungskreis; nie an Gegenpartei senden.
