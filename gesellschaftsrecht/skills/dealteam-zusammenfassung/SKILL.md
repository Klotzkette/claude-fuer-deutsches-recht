---
name: dealteam-zusammenfassung
description: >
  Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und
  Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: „Deal-Briefing",
  „Deal-Zusammenfassung", „Status für Geschäftsführung", „Team-Update",
  „Deal-Team-Summary".
language: de
triggers:
  - "Deal-Briefing"
  - "Deal-Zusammenfassung"
  - "Team-Update"
  - "Vorstandsbriefing"
  - "Deal-Summary"
---

# Deal-Team-Zusammenfassung

## Zweck

M&A-Teams brauchen je nach Ebene unterschiedliche Informationstiefe: Die Geschäftsführung will drei Sätze und eine Risikobewertung. Der Deal-Lead will kritischen Pfad und offene Punkte. Das Arbeitsteam will alle Findings mit Quellen. Dieser Skill erstellt alle drei Ebenen aus denselben DD-Quellen.

## Eingaben

- DD-Issue-Extraktions-Findings aus dem laufenden Mandat
- Vollzugscheckliste (aktueller Status)
- Wesentliche-Verträge-Anlage (wenn vorhanden)
- Deal-Kontext: Parteien, Transaktionsstruktur, Kaufpreis, Zieldatum Vollzug
- Praxisprofil: `## M&A → Deal-Team-Briefing` (Rhythmus, Format, Adressat)

## Ablauf

### Schritt 1: Quellen zusammenführen

Aus dem Mandatsordner lesen:
- `mandate/[code]/dd-issues-[kategorie].md` (alle Kategorien)
- `mandate/[code]/vollzugs-checkliste.yaml`
- `mandate/[code]/wesentliche-vertraege-anlage.md` (falls vorhanden)
- `mandate/[code]/deal-kontext.md`

Gesamtbild: Anzahl Findings je Schweregrad; blockierende Vollzugspunkte; kritischer Pfad.

### Schritt 2: Drei Briefing-Ebenen erstellen

**Ebene 1 – Geschäftsführungs-Kurzfassung (½–1 Seite)**

```markdown
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

## [Deal-Code] – Statusbericht – [Datum]

**Transaktion:** Erwerb [Zielgesellschaft] durch [Käufer]; Kaufpreis: [X] EUR; Vollzug geplant: [Datum].

**Gesamteinschätzung:** [🔴 Erhebliche offene Punkte / 🟠 Klärungsbedarf / 🟢 Auf Kurs]

**Kernrisiken (max. 3):**
1. [Risiko] — [eine Zeile Implikation]
2. [Risiko] — [eine Zeile Implikation]
3. [Risiko] — [eine Zeile Implikation]

**Vollzugsstatus:** [N] von [N] VB erfüllt. Kritischer Pfad: [Punkt + Datum].

**Empfehlung:** [Fortsetzen / Preis anpassen / Klärung einholen / Abbruch erwägen]
```

**Ebene 2 – Deal-Lead-Briefing (2–4 Seiten)**

```markdown
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

## [Deal-Code] – Deal-Lead-Briefing – [Datum]

### Transaktionsübersicht
[Parteien, Struktur, Preis, Timeline]

### DD-Ergebnisse nach Kategorie

| Kategorie | 🔴 | 🟠 | 🟡 | 🟢 | Top-Finding |
|---|---|---|---|---|---|
| Gesellschaftsrecht | N | N | N | N | [Kurzbeschreibung] |
| Wesentliche Verträge | N | N | N | N | [Kurzbeschreibung] |
| IP / Technologie | N | N | N | N | [Kurzbeschreibung] |
| Arbeitsrecht | N | N | N | N | [Kurzbeschreibung] |
| Umwelt / Regulatorisch | N | N | N | N | [Kurzbeschreibung] |

### Vollzugsblockaden (🔴 Blocking)
[Jeder blockierende Punkt mit Verantwortlichem und Fälligkeit]

### Kritischer Pfad
[Zeitstrahldarstellung oder Liste mit Fälligkeiten]

### Offene Fragen für Entscheidung
1. [Frage] — Entscheidung bis [Datum] benötigt
2. [Frage]

### Preisanpassung / Risikoreservierung
[Falls 🔴-Findings preisrelevant sind: quantifizierte oder qualifizierte Risikoschätzung]
```

**Ebene 3 – Arbeitsteam-Vollständigkeitsbericht**

Vollständige DD-Findings aus allen Kategorien nach Schweregrad sortiert, mit Quellen, Empfehlungen und Status. Feeds direkt aus `dd-findings-extraktion`-Output. Keine zusätzliche Zusammenfassung – Vollständigkeit ist das Ziel.

### Schritt 3: Vollzugs-Handlungs-Abgleich

Nach Erstellung der Zusammenfassung: prüfen, ob dealteam-zusammenfassung neue Vollzugspunkte aufdeckt, die in der Vollzugscheckliste fehlen. Falls ja: diese als Übergabe-Items für den `vollzugs-checkliste`-Skill markieren.

## Quellen und Zitierweise

Normen-Basis je nach DD-Findings. Zitierweise nach `../../references/zitierweise.md`.

Kommentarliteratur (als Hintergrund für Risikoeinschätzungen):
- MüKoGmbHG/Fleischer, 4. Aufl. 2022.
- Roth/Altmeppen, GmbHG, 10. Aufl. 2021.
- BGH, Urt. v. 01.03.2010 – II ZR 213/08, NJW 2010, 1808 (Risikoverteilung beim Unternehmenskauf).

## Ausgabeformat

Drei separate Abschnitte (oder drei Dokumente auf Anfrage):
1. Geschäftsführungs-Kurzfassung (½–1 Seite)
2. Deal-Lead-Briefing (2–4 Seiten)
3. Arbeitsteam-Vollständigkeitsbericht (vollständig)

## Beispiel

**Eingabe:** DD abgeschlossen; 4 🔴-Findings (davon 1 Change-of-Control Zustimmung ausstehend, 1 IP-Eigentumslücke); 2 Vollzugsbedingungen offen (Kartell 6 Wochen + CoC-Zustimmung 3 Wochen).

**GF-Kurzfassung:**
> Gesamteinschätzung: 🟠 Klärungsbedarf. Zwei Punkte blockieren den Vollzug: kartellrechtliche Freigabe (ca. 6 Wochen, Monat) und Zustimmung Acme GmbH zum Eigentümerwechsel (3 Wochen, risikobehaftet – Verhandlungen noch nicht aufgenommen). IP-Eigentumslücke bei drei Kernpatenten erfordert Rückwärtsabtretung; ohne diese Reduktion des Kaufpreises um ca. 800 TEUR empfohlen.

## Risiken / typische Fehler

- **Ebenenverwirrung:** GF-Kurzfassung niemals mit Arbeitsteam-Vollständigkeitsbericht mischen. Separate Dokumente erstellen.
- **Preisanpassung ohne Quantifizierung:** 🔴-Findings ohne Risikowert lassen die GF ohne Entscheidungsgrundlage. Zumindest Bandbreite angeben.
- **Vollzugspunkte nicht an Checkliste übergeben:** Diese Zusammenfassung ist der letzte Filter vor dem Vollzug. Wenn sie neue Punkte aufdeckt, müssen diese in die Vollzugscheckliste.
- **Verteilungskreis:** Ebene 1 häufig an GF weitergegeben; Ebene 3 bleibt im Privilegierungskreis. Nie Ebene 3 an Gegenpartei senden.
