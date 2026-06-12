---
name: examensvorbereitung-fragen
description: "Examensvorbereitungs-Fragen für 1. und 2. Staatsexamen erstellen: Anwendungsfall Student will Examenswissen durch gezielte Uebungsfragen trainieren und Schwachstellen erkennen. 1. StEx und 2. StEx, JAG Bundesland Bayern NRW Hamburg, Subsumtion Gutachtenstil. Prüfraster Fachgebiet Zivilrecht Straf..."
---

# Examensvorbereitungs-Fragen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DRiG § 5a Studiendauer 9 Semester (Regelstudienzeit), Freischuss-Frist (i.d.R. 8 Semester nach JAG), Wiederholungsfrist, Hausarbeit 4-6 Wochen.
- Tragende Normen verifizieren: DRiG §§ 5, 5a, 5b (Erste Prüfung), JAG der Länder, JAPO Bayern, JAG NRW, BBesG (Referendariat), Hochschulgesetze, Studienordnungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Studierende, Justizprüfungsamt (Landesjustizverwaltung), Universität, Repetitorium, Klausurleiter, Mündliche-Prüfungs-Kommission.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Klausurgutachten (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis), Hausarbeit, Aktenvortrag (Referendar), Probeklausur, Prüfungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welches Examen und welches Bundesland (1. StEx, 2. StEx; Bayern, NRW, Hamburg)?
2. Welches Fachgebiet soll geuebt werden (Zivilrecht, Strafrecht, öffentliches Recht, Verfahrensrecht)?
3. Zeitdruck-Simulation oder inhaltliches Verstaendnis-Training?
4. Welche Schwachpunkte wurden in frueheren Uebungsklausuren identifiziert?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 13, 14 JAG NRW — Examensklausuren: Inhaltsanforderungen und Bewertungsmaßstab (exemplarisch für alle Bundeslaender)
- § 195 BGB — Regelverjaehrung: Dauerklassiker in Zivilrecht-Klausuren
- § 1 Abs. 1 StGB — Bestimmtheitsgebot: Examens-Fundamentalsatz Strafrecht
- § 42 VwGO — Anfechtungs- und Verpflichtungsklage: Examens-Standard öffentliches Recht

## Eingaben

1. Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` → Bundesland, JAG, Schwächefächer, Lernstil
2. Optional: `lernplan.yaml` – zeigt, welches Fach heute auf dem Plan steht und welche Teilgebiete noch schwach sind
3. Rechtsgebiet (Argument oder interaktiv erfragen)
4. Prüfungstyp: `--schriftlich` (Klausur, 5h) oder `--mündlich` (Aktenvortrag, AG-Fragen)

## Ablauf

### 1. Prüfungstyp-Gate (nicht überspringen)

Falls Bundesland/JAG oder Prüfungstyp nicht im Profil vorhanden sind, **vor der Fragengenerierung fragen**:

- "In welchem Bundesland legst du das Examen ab?"
- "1. oder 2. Staatsexamen?"
- "Schriftlich oder mündlich?"

Falsche Annahmen beim JAG-Rahmen sind der Fehler, der sich nicht aufholen lässt.

### 2. JAG-Prüfungsgebiet-Gate

Falls das Rechtsgebiet außerhalb des JAG-Prüfungsstoffs liegt oder es eine bundeslandspezifische Besonderheit gibt:

> "In [Bundesland] enthält die JAG folgende schriftliche Prüfungsfächer: [Liste]. [Rechtsgebiet] ist [enthalten / nicht enthalten / Pflicht-/Wahlstation]. Soll ich trotzdem fortfahren?"

### 3. Fragengenerierung

- Fragen gewichtet nach **Schwächeprofil** aus dem Lernprofil
- **Examenstypische Sachverhalte** (Falllösung, nicht Theoriefragen): kurze Sachverhalte mit mehreren Anspruchsgrundlagen, Streitständen und bewusstem Ablenkungspotenzial
- **Schwierigkeitsmarkierung:** `[Grundniveau]` / `[Examensniveau]` / `[Schwerpunkt]`
- **JAG-Markierung:** kennzeichnet, ob eine Regel bundeseinheitlich oder länderspezifisch ist

### 4. Auswertung

Nach jeder Antwort:
1. Struktur prüfen: War der Obersatz klar hypothetisch formuliert? Wurde die Definition zitiert?
2. Subsumtion prüfen: Wurden alle Tatbestandsmerkmale geprüft?
3. Streitstände: Wurden h.M. und Mindermeinung mit Belegen genannt?
4. Zitierweise: Entsprechen die Literaturzitate dem Standard aus `../references/zitierweise.md`?
5. Ergebnis festhalten, Muster in Fehlern protokollieren

`--session <n>` läuft N Fragen durch und schreibt anschließend eine Zusammenfassung der Fehlermuster.

## Quellen und Zitierweise

→ `../references/zitierweise.md` (maßgeblich für alle Zitate)

**Quellenregel je Rechtsgebiet:**

| Rechtsgebiet | Standardkommentar |
|---|---|
| BGB AT / Schuldrecht | Normtext, bereitgestellte Materialien, verifizierte Rechtsprechung |
| Sachenrecht | Normtext, bereitgestellte Materialien, verifizierte Rechtsprechung |
| BGB Allgemein | Normtext, bereitgestellte Materialien, verifizierte Rechtsprechung |
| Handelsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| Gesellschaftsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| ZPO | Normtext, amtliche Hinweise, verifizierte Rechtsprechung |
| StGB | Normtext, verifizierte Rechtsprechung, bereitgestellte Materialien |
| Verwaltungsrecht | Normtext, amtliche Materialien, verifizierte Rechtsprechung |

**Ausbildungszeitschriften:**
Nur verwenden, wenn der Nutzer den konkreten Aufsatz bereitstellt oder ein lizenzierter Live-Zugriff die Fundstelle verifiziert.

## Ausgabeformat

### Sachverhalts-Aufgabe (Klausurstil)

```
**Sachverhalt:**
[3–8 Sätze, examenstypische Verdichtung mit Ablenkungsmanövern]

**Aufgabe:**
Prüfe alle in Betracht kommenden Ansprüche des A gegen B.
[Bundesland: Bayern / JAG-Prüfungsgebiet: Schuldrecht / Niveau: Examensniveau]
```

### Musterlösung (nach Nutzerantwort)

```
**Lösungsskizze – Gutachtenstil**

A. Ansprüche des A gegen B

I. Anspruch aus § 433 Abs. 2 BGB
 Obersatz: A könnte gegen B einen Anspruch auf Kaufpreiszahlung
 gemäß § 433 Abs. 2 BGB haben.
 Voraussetzungen: wirksamer Kaufvertrag, Fälligkeit, kein Einrederecht.
 Definition Kaufvertrag: …
 Subsumtion: …
 Ergebnis: Der Anspruch besteht / besteht nicht.

II. Anspruch aus § 280 Abs. 1 BGB
 Obersatz: …

**Literaturnachweise:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Deine Lücken diese Sitzung:** [Protokoll]
```

## Beispiel

**Sachverhalt:** Verkäufer V verkauft Käufer K sein gebrauchtes Fahrrad für 300 €. K überweist den Betrag, V liefert das Rad jedoch nicht. K setzt V eine Frist von 10 Tagen. V lässt die Frist verstreichen.

**Aufgabe:** Prüfe alle Ansprüche des K gegen V.

**Musterlösung (Auszug):**

*I. Anspruch des K gegen V auf Übereignung und Übergabe des Fahrrads gemäß §§ 433 Abs. 1 S. 1, 929 S. 1 BGB*

Obersatz: K könnte gegen V einen Anspruch auf Übereignung und Übergabe des Fahrrads gemäß § 433 Abs. 1 S. 1 BGB haben.

Definition: Ein Kaufvertrag setzt zwei übereinstimmende Willenserklärungen (Angebot und Annahme) voraus, die auf Übertragung des Eigentums gegen Entgeltzahlung gerichtet sind.

Subsumtion: V und K haben sich über Fahrrad und Preis einig, § 433 Abs. 1 S. 1 BGB. Ein Kaufvertrag liegt vor.

Ergebnis: Der Anspruch aus § 433 Abs. 1 S. 1 BGB besteht. Da V nicht geliefert hat, ist der Anspruch nicht erfüllt.

*II. Anspruch auf Schadensersatz statt der Leistung gemäß §§ 280 Abs. 1, 3, 281 Abs. 1 BGB*

Obersatz: K könnte nach fruchtlosem Fristablauf einen Anspruch auf Schadensersatz statt der Leistung gemäß §§ 280 Abs. 1, 3, 281 Abs. 1 BGB haben.

[…] Frist wurde gesetzt und ist abgelaufen, § 281 Abs. 1 S. 1 BGB. Vertretenmüssen wird gemäß § 280 Abs. 1 S. 2 BGB vermutet; V hat sich nicht exkulpiert.

Ergebnis: Der Anspruch auf Schadensersatz statt der Leistung besteht.

*Quellenhinweis:*
Literaturfundstellen nur ergänzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff die Fundstelle verifiziert.

## Risiken / typische Fehler

- **Falscher JAG-Rahmen:** BGB-Inhalte die in einem Bundesland nicht prüfungsrelevant sind, kosten Lernzeit. Bundesland immer zuerst prüfen.
- **Urteilsstil statt Gutachtenstil:** Der Obersatz muss hypothetisch sein. "A hat einen Anspruch" ist Urteilsstil – falsch für Klausuren.
- **h.M. ohne Beleg:** "nach h.M." allein ist kein Argument. Kommentarstelle oder BGH-Urteil nennen.
- **Scheinprobleme ignorieren:** Examsklausuren enthalten bewusste Ablenkungen. Offensichtlich vorliegende Tatbestandsmerkmale kurz abarbeiten, nicht übergehen.
- **Konkurrenzprobleme:** Reihenfolge der Anspruchsgrundlagen (vertraglich vor außervertraglich) beachten – vgl. `../references/methodik-buergerliches-recht.md`.
- **Fehlende Fundstellen im Gutachten:** Im 1. StEx ist das Fehlen von Kommentarzitaten ein Bewertungsminus.
