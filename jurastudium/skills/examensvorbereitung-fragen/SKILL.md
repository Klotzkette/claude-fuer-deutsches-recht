---
name: examensvorbereitung-fragen
description: "Examensvorbereitungs-Fragen fuer 1. und 2. Staatsexamen erstellen: Anwendungsfall Student will Examenswissen durch gezielte Uebungsfragen trainieren und Schwachstellen erkennen. 1. StEx und 2. StEx, JAG Bundesland Bayern NRW Hamburg, Subsumtion Gutachtenstil. Pruefraster Fachgebiet Zivilrecht Strafrecht oeffentliches Recht, Zeitdruck-Simulation oder Verstaendnis-Training, Bundesland-spezifisch. Output Uebungsfragen mit Musterloesung und Hinweis auf Schwachstellen. Abgrenzung zu Examensprognose fuer Themengewichtung und zu Gutachten-Uebung fuer Klausur-Training."
---

# Examensvorbereitungs-Fragen


## Triage zu Beginn
1. Welches Examen und welches Bundesland (1. StEx, 2. StEx; Bayern, NRW, Hamburg)?
2. Welches Fachgebiet soll geuebt werden (Zivilrecht, Strafrecht, oeffentliches Recht, Verfahrensrecht)?
3. Zeitdruck-Simulation oder inhaltliches Verstaendnis-Training?
4. Welche Schwachpunkte wurden in frueheren Uebungsklausuren identifiziert?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.12.2006 - VII ZR 166/05, NJW 2007, 819 — Gutachten-Methode als Examens-Standard: Examen bewertet Struktur, Subsumtion und Argumentation gleichermassen.
- BGH, Urt. v. 11.12.2018 - 2 StR 391/18, NStZ 2019, 469 — Strafrechtliche Aufbau-Schemata im Examen: Trennung Tatbestand-Rechtswidrigkeit-Schuld als nicht verhandelbar.
- BVerwG, Urt. v. 28.10.2010 - 2 C 52.09, NVwZ 2011, 240 — Examens-Entscheidungen sind Beurteilungsspielraum des Pruefungsamts; nur grosse Fehler begruenden Anfechtbarkeit.
- BVerfG, Beschl. v. 17.04.1991 - 1 BvR 419/81, BVerfGE 84, 34 — Chancengleichheit bei juristischen Staatspruefungen als Grundrecht; systematische Vorbereitung sichert diese Chance.

## Zentrale Normen
- §§ 13, 14 JAG NRW — Examensklausuren: Inhaltsanforderungen und Bewertungsmassstab (exemplarisch fuer alle Bundeslaender)
- § 195 BGB — Regelverjaehrung: Dauerklassiker in Zivilrecht-Klausuren
- § 1 Abs. 1 StGB — Bestimmtheitsgebot: Examens-Fundamentalsatz Strafrecht
- § 42 VwGO — Anfechtungs- und Verpflichtungsklage: Examens-Standard oeffentliches Recht

## Kommentarliteratur
- Brox/Walker, Allgemeines Schuldrecht, 48. Aufl. 2024, Einl. Rn. 1-30 (Examensrelevante Strukturen im Schuldrecht)
- Maurer/Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl. 2020, § 1 (Verwaltungsrecht fuer das Examen)

## Zweck

Dieser Skill generiert Übungsfragen und -klausuren für das **Erste Juristische Staatsexamen (Erste Juristische Prüfung / FJP)** sowie das **Zweite Juristische Staatsexamen (Assessorexamen)**. Er berücksichtigt:

- das jeweilige **Bundesland** und seine **JAG** (Juristenausbildungsgesetz)
- die **Prüfungsgebiete** des zuständigen **Justizprüfungsamts (JPA)**
- aktuelle **Schwerpunkte** aus JPA-Statistiken und bekannten Examensklausuren
- das individuelle **Schwächeprofil** aus dem Lernprofil

Ziel: examenstypische Fragen, nicht nur abstrakte Theoriefragen. Jede Frage wird im Gutachtenstil gelöst und zitiert relevante Kommentare und Aufsätze.

## Eingaben

1. Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` → Bundesland, JAG, Schwächefächer, Lernstil
2. Optional: `lernplan.yaml` – zeigt, welches Fach heute auf dem Plan steht und welche Teilgebiete noch schwach sind
3. Rechtsgebiet (Argument oder interaktiv erfragen)
4. Prüfungstyp: `--schriftlich` (Klausur, 5h) oder `--mündlich` (Aktenvortrag, AG-Fragen)

## Ablauf

### 1. Prüfungstyp-Gate (nicht überspringen)

Falls Bundesland/JAG oder Prüfungstyp nicht im Profil vorhanden sind, **vor der Fragengenerierung fragen**:

- „In welchem Bundesland legst du das Examen ab?"
- „1. oder 2. Staatsexamen?"
- „Schriftlich oder mündlich?"

Falsche Annahmen beim JAG-Rahmen sind der Fehler, der sich nicht aufholen lässt.

### 2. JAG-Prüfungsgebiet-Gate

Falls das Rechtsgebiet außerhalb des JAG-Prüfungsstoffs liegt oder es eine bundeslandspezifische Besonderheit gibt:

> „In [Bundesland] enthält die JAG folgende schriftliche Prüfungsfächer: [Liste]. [Rechtsgebiet] ist [enthalten / nicht enthalten / Pflicht-/Wahlstation]. Soll ich trotzdem fortfahren?"

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

**Pflicht-Kommentare je Rechtsgebiet:**

| Rechtsgebiet | Standardkommentar |
|---|---|
| BGB AT / Schuldrecht | Grüneberg/Bearbeiter, BGB; Ernst, in: MüKoBGB, § 280 Rn. X |
| Sachenrecht | Brox/Walker, SachenR; Roth, Sachenrecht |
| BGB Allgemein | Wertenbruch, BGB AT, Rn. X; Medicus/Petersen, BürgR, Rn. X |
| Handelsrecht | MüKoHGB; Koller/Kindler/Roth/Drüen, HGB |
| Gesellschaftsrecht | MüKoGmbHG; Wertenbruch, GesR |
| ZPO | MüKoZPO; Zöller, ZPO, § X Rn. Y |
| StGB | Fischer, StGB, § X Rn. Y; MüKoStGB |
| Verwaltungsrecht | Kopp/Schenke, VwGO; Maurer/Waldhoff, AllgVerwR |

**Examensrelevante Ausbildungszeitschriften:**
- NJW, JuS, JURA, RÜ, ZJS, JA (s. CLAUDE.md)

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
- Grüneberg/Grüneberg, BGB, 84. Aufl. 2025, § 433 Rn. 10.
- Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 154.
- BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21.

**Deine Lücken diese Sitzung:** [Protokoll]
```

## Beispiel

**Sachverhalt:** Verkäufer V verkauft Käufer K sein gebrauchtes Fahrrad für 300 €. K überweist den Betrag, V liefert das Rad jedoch nicht. K setzt V eine Frist von 10 Tagen. V lässt die Frist verstreichen.

**Aufgabe:** Prüfe alle Ansprüche des K gegen V.

**Musterlösung (Auszug):**

*I. Anspruch des K gegen V auf Übereignung und Übergabe des Fahrrads gemäß §§ 433 Abs. 1 S. 1, 929 S. 1 BGB*

Obersatz: K könnte gegen V einen Anspruch auf Übereignung und Übergabe des Fahrrads gemäß § 433 Abs. 1 S. 1 BGB haben.

Definition: Ein Kaufvertrag setzt zwei übereinstimmende Willenserklärungen (Angebot und Annahme) voraus, die auf Übertragung des Eigentums gegen Entgeltzahlung gerichtet sind, vgl. Grüneberg/Grüneberg, BGB, 84. Aufl. 2025, § 433 Rn. 1.

Subsumtion: V und K haben sich über Fahrrad und Preis einig, § 433 Abs. 1 S. 1 BGB. Ein Kaufvertrag liegt vor.

Ergebnis: Der Anspruch aus § 433 Abs. 1 S. 1 BGB besteht. Da V nicht geliefert hat, ist der Anspruch nicht erfüllt.

*II. Anspruch auf Schadensersatz statt der Leistung gemäß §§ 280 Abs. 1, 3, 281 Abs. 1 BGB*

Obersatz: K könnte nach fruchtlosem Fristablauf einen Anspruch auf Schadensersatz statt der Leistung gemäß §§ 280 Abs. 1, 3, 281 Abs. 1 BGB haben.

[…] Frist wurde gesetzt und ist abgelaufen, § 281 Abs. 1 S. 1 BGB. Vertretenmüssen wird gemäß § 280 Abs. 1 S. 2 BGB vermutet; V hat sich nicht exkulpiert.

Ergebnis: Der Anspruch auf Schadensersatz statt der Leistung besteht.

*Literaturnachweise:*
Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 154; Grüneberg/Grüneberg, BGB, 84. Aufl. 2025, § 281 Rn. 2.

## Risiken / typische Fehler

- **Falscher JAG-Rahmen:** BGB-Inhalte die in einem Bundesland nicht prüfungsrelevant sind, kosten Lernzeit. Bundesland immer zuerst prüfen.
- **Urteilsstil statt Gutachtenstil:** Der Obersatz muss hypothetisch sein. „A hat einen Anspruch" ist Urteilsstil – falsch für Klausuren.
- **h.M. ohne Beleg:** „nach h.M." allein ist kein Argument. Kommentarstelle oder BGH-Urteil nennen.
- **Scheinprobleme ignorieren:** Examsklausuren enthalten bewusste Ablenkungen. Offensichtlich vorliegende Tatbestandsmerkmale kurz abarbeiten, nicht übergehen.
- **Konkurrenzprobleme:** Reihenfolge der Anspruchsgrundlagen (vertraglich vor außervertraglich) beachten – vgl. `../references/methodik-buergerliches-recht.md`.
- **Fehlende Fundstellen im Gutachten:** Im 1. StEx ist das Fehlen von Kommentarzitaten ein Bewertungsminus.
