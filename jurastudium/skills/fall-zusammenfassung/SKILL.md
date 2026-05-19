---
name: fall-zusammenfassung
description: >
  Fallbearbeitung im deutschen Gutachtenstil (Obersatz – Definition –
  Subsumtion – Ergebnis). Lade diesen Skill bei Anfragen wie „bearbeite diesen
  Fall", „schreibe ein Gutachten", „löse den Sachverhalt", „Fallbearbeitung",
  „Klausuraufbau" oder wenn ein Sachverhalt zur Bearbeitung eingegeben wird.
language: de
argument-hint: "[Sachverhalt einfügen oder Fallname nennen]"
triggers:
  - "fallbearbeitung"
  - "gutachten"
  - "sachverhalt"
  - "klausuraufbau"
  - "löse den fall"
  - "anspruch prüfen"
---

# Fallbearbeitung im Gutachtenstil

## Zweck

Dieser Skill begleitet die Bearbeitung juristischer Übungsfälle, Klausuren und Hausarbeitssachverhalte im deutschen **Gutachtenstil**. Er gibt keine fertige Lösung vor – er stellt das Gerüst bereit, hakt bei Ungenauigkeiten nach und bewertet Schritt für Schritt die Struktur, die Definitionen und die Subsumtion.

Einsatzbereiche:
- Große und kleine BGB-Übungen (AT, SchuldR, SachenR, FamR, ErbR)
- Anfänger- und Fortgeschrittenenklausuren
- Examsklausuren (1. StEx, Bundesland nach JAG)
- Hausarbeiten und Seminararbeiten
- Anwaltsklausur / 2. StEx

## Eingaben

1. **Sachverhalt** – als Text eingefügt, Pfad oder mündlich formuliert
2. **Aufgabenstellung** – „Prüfe alle Ansprüche" / „Ist die Klage begründet?" / „Prüfe die Strafbarkeit von A"
3. **Rechtsgebiet** (optional, wird aus Sachverhalt abgeleitet)
4. **Lernprofil** aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` → Lernstil (Drill / Erklärung), Semester, Schwächebereiche

## Das deutsche Gutachtenstil-Schema

Das Plugin verwendet **ausschließlich** das deutsche Vier-Schritte-Schema. IRAC ist die US-amerikanische Variante und hat im deutschen Jurastudium keine eigenständige Verwendung.

```
1. OBERSATZ
   Formulierung: „[Person] könnte gegen [Person] einen Anspruch auf
   [Rechtsfolge] gemäß § X BGB/StGB/VwGO haben."
   Pflicht: hypothetisch, nicht assertorisch. „A hat …" ist Urteilsstil → falsch
   für Klausuren.

2. DEFINITION
   Abstrakte Tatbestandsmerkmale der Norm (wörtlich oder paraphrasiert).
   Pflicht: Kommentarzitat oder Lehrbuchbeleg einfügen.
   Beispiel: „Besitz i. S. d. § 854 BGB ist die tatsächliche Sachherrschaft,
   Grüneberg/Herrler, BGB, 84. Aufl. 2025, § 854 Rn. 1."

3. SUBSUMTION
   Anwendung der abstrakten Merkmale auf die konkreten Sachverhaltsfakten.
   Pflicht: jeden Sachverhaltsaspekt explizit subsumieren, keine stillschweigen-
   de Übernahme. Streitstände auflösen (h.M. mit Beleg, Gegenauffassung benennen).

4. ERGEBNIS
   Kurze, eindeutige Aussage: „Damit hat A gegen B einen Anspruch auf X
   gemäß § Y BGB. / Der Anspruch besteht nicht."
```

## Anspruchsgrundlagen-Reihenfolge

Die Reihenfolge ist nicht beliebig – vgl. `../references/methodik-deutsches-recht.md`:

1. Vertragliche Ansprüche (§§ 433, 535, 611 ff. BGB etc.)
2. Vertragsähnliche Ansprüche (c.i.c., §§ 311 Abs. 2, 241 Abs. 2, 280 Abs. 1 BGB)
3. Quasivertragliche Ansprüche (GoA, §§ 677 ff. BGB)
4. Dingliche Ansprüche (§§ 985, 1004 BGB)
5. Deliktische Ansprüche (§§ 823 Abs. 1, 823 Abs. 2, 826 BGB; ProdHaftG; StVG)
6. Bereicherungsansprüche (§§ 812 ff. BGB)

Strafrecht: Täterschaft vor Teilnahme, vollendetes Delikt vor Versuch, schwerer vor minder schwerer Fall.

Verwaltungsrecht: Zulässigkeit vor Begründetheit, Ermächtigungsgrundlage zuerst.

## Ablauf

### Schritt 1: Sachverhaltsanalyse

Das Plugin liest den Sachverhalt und:
- Identifiziert beteiligte Parteien und ihre Rollen
- Markiert Schlüsselfakten (fett)
- Benennt mögliche Ansprüche / Tatbestände ohne Lösung vorwegzunehmen
- Stellt gezielte Fragen zur Sachverhaltsambiguität

### Schritt 2: Lösungsgliederung (Gerüst)

Das Plugin gibt:
- Eine **Gliederung** der zu prüfenden Anspruchsgrundlagen in der richtigen Reihenfolge
- **Leere Slots** für Obersatz, Definition, Subsumtion, Ergebnis
- Hinweise auf relevante Streitstände (mit Kommentarstellen, ohne die Lösung vorwegzunehmen)

Im **Drill-Modus**: Fragen statt Hinweise. „Was ist der erste Anspruch, den du prüfst?"

### Schritt 3: Begleitendes Feedback

Pro Prüfungspunkt, den der Nutzer erarbeitet:
- Ist der Obersatz korrekt formuliert (hypothetisch)?
- Ist die Definition belegt?
- Subsumiert die Antwort alle Sachverhaltselemente?
- Ist der Streitstand korrekt aufgelöst?

Das Plugin **schreibt den Abschnitt nicht um**. Es zeigt genau, was fehlt oder unscharf ist.

### Schritt 4: Zitierprüfung

Alle genannten Kommentare und Urteile werden auf Formatkonformität mit `../references/zitierweise.md` geprüft.

Beispiel-Korrektur:
> „Du hast zitiert: `MüKo § 280 Rn. 154`. Korrekte Form: `Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 154.` – Bearbeiter vor Kommentartitel."

## Quellen und Zitierweise

→ `../references/zitierweise.md` (verbindlich)

**Standardzitate für häufige BGB-Normen:**

- Anspruchsgrundlage § 433 BGB: `Grüneberg/Grüneberg, BGB, 84. Aufl. 2025, § 433 Rn. 1.`
- Schadensersatz § 280 Abs. 1 BGB: `Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 100 ff.`
- Deliktsrecht § 823 Abs. 1 BGB: `Sprau, in: Grüneberg, BGB, 84. Aufl. 2025, § 823 Rn. 1.`
- Ungerechtfertigte Bereicherung § 812 BGB: `Sprau, in: Grüneberg, BGB, 84. Aufl. 2025, § 812 Rn. 1.`
- Allgemeines Schuldrecht: `Brox/Walker, Allg. Schuldrecht, 47. Aufl. 2023, § X Rn. Y.`
- BGB Allgemeiner Teil: `Wertenbruch, BGB AT, 5. Aufl. 2023, § X Rn. Y.`

**Leitentscheidungen (Beispiele für häufige Streitstände):**
- BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 (Schadensersatz Verzug)
- BGH, Urt. v. 26.01.2021 – VI ZR 405/19, NJW 2021, 1006 (Verkehrspflichten)

## Ausgabeformat

### Lösungsgliederung (Gerüst-Modus)

```
**Sachverhalt:** [Schlüsselfakten fett]

**Lösungsskizze – Gliederung**

A. Ansprüche des A gegen B
   I.   § X BGB – [Kurzbezeichnung]
        Obersatz: [leer – deine Formulierung]
        Definition: [Hinweis auf Tatbestandsmerkmale; Kommentarstelle]
        Subsumtion: [leer – deine Subsumtion]
        Ergebnis: [leer]
   II.  § Y BGB – [Kurzbezeichnung]
        [...]

B. Ansprüche des B gegen A
   [...]

**Offene Streitstände:** [Liste mit Kommentarstellen, ohne Lösung]
**Zitierhinweise:** [Formatvorgaben für die in der Lösung benötigten Quellen]
```

### Feedback nach Nutzerantwort

```
**⚠️ Feedback**
- Obersatz: [korrekt hypothetisch / nicht hypothetisch → Formulierungsvorschlag-Struktur]
- Definition: [belegt / unbelegt → benötigte Quelle]
- Subsumtion: [vollständig / Sachverhaltselement X fehlt]
- Streitstand: [h.M. belegt / Gegenmeinung fehlt / Meinungsstreit nicht erkannt]
- Zitat: [konform / Abweichung von zitierweise.md]
```

## Beispiel

**Sachverhalt:** A verkauft B sein Motorrad für 4.000 €. B zahlt, A übergibt das Motorrad. Drei Wochen später bricht das Vorderrad aus mangelhafter Schweißnaht, B stürzt und verletzt sich. A wusste von dem Defekt.

**Aufgabe:** Prüfe alle Ansprüche des B gegen A.

**Lösungsskizze (Auszug):**

*A. Ansprüche des B gegen A*

*I. Anspruch auf Schadensersatz gemäß §§ 437 Nr. 3, 280 Abs. 1, 3, 281 BGB*

Obersatz: B könnte gegen A einen Anspruch auf Schadensersatz statt der Leistung gemäß §§ 437 Nr. 3, 280 Abs. 1, 3, 281 BGB haben.

Definition: §§ 437 Nr. 3, 280 Abs. 1, 3, 281 BGB setzen einen Kaufvertrag mit mangelhafter Sache und Vertretenmüssen voraus. Ein Sachmangel liegt vor, wenn die Sache bei Gefahrübergang nicht die vereinbarte Beschaffenheit hat (§ 434 Abs. 1 BGB), vgl. Grüneberg/Weidenkaff, BGB, 84. Aufl. 2025, § 434 Rn. 1.

Subsumtion: Kaufvertrag liegt vor. Das Motorrad hatte eine mangelhafte Schweißnaht, die bereits bei Übergabe vorhanden war (§ 446 BGB: Gefahrübergang bei Übergabe). A kannte den Defekt → grob fahrlässige, jedenfalls vorsätzliche Pflichtverletzung. § 276 Abs. 1 S. 1 BGB: Vorsatz und Fahrlässigkeit werden vertreten. Fristsetzung (§ 281 Abs. 1 BGB): ggf. entbehrlich nach § 281 Abs. 2 BGB, weil A arglistig gehandelt hat, vgl. Ernst, in: MüKoBGB, 9. Aufl. 2022, § 281 Rn. 64.

Ergebnis: B hat einen Anspruch auf Schadensersatz statt der Leistung gemäß §§ 437 Nr. 3, 280 Abs. 1, 3, 281 Abs. 2 BGB.

*II. Deliktischer Anspruch gemäß § 823 Abs. 1 BGB*

Obersatz: B könnte auch einen deliktischen Anspruch auf Schadensersatz wegen Verletzung seiner Gesundheit gemäß § 823 Abs. 1 BGB haben.

[…] Verletzungserfolg (Körperverletzung), Kausalität, Rechtswidrigkeit (indiziert durch Tatbestand), Vorsatz des A (kannte Defekt). Haftungsbegründende und haftungsausfüllende Kausalität liegen vor, Sprau, in: Grüneberg, BGB, 84. Aufl. 2025, § 823 Rn. 6.

Ergebnis: Anspruch besteht.

*Literaturnachweise:*  
Grüneberg/Weidenkaff, BGB, 84. Aufl. 2025, § 434 Rn. 1; Ernst, in: MüKoBGB, 9. Aufl. 2022, § 281 Rn. 64; BGH, Urt. v. 26.01.2021 – VI ZR 405/19, NJW 2021, 1006.

## Risiken / typische Fehler

- **Assertorischer Obersatz:** „A hat einen Anspruch auf …" ist Urteilsstil und in Klausuren ein Aufbaufehler.
- **Subsumtion als Behauptung:** „Das Tatbestandsmerkmal liegt vor." ohne Sachverhaltsbezug ist keine Subsumtion.
- **Streitstand übergehen:** Leitentscheidungen und Kommentarstreitstände sind im 1. StEx Bewertungsbestandteil.
- **Konkurrenzfragen nicht lösen:** Wenn § 823 Abs. 1 BGB und §§ 437, 280 BGB nebeneinander bestehen, dies kurz konstatieren (kumulative Anspruchskonkurrenz).
- **Zu lange Obersätze:** Der Obersatz soll die Rechtsfolge benennen, nicht die gesamte Prüfung vorwegnehmen.
- **Zitate ohne Bearbeiter:** `MüKo § 280` ist kein korrektes Zitat. Immer: `Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. X.`
