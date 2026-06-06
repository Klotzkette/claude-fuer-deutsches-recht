---
name: fall-zusammenfassung-gliederungs-baukasten
description: "Juristischen Fall zusammenfassen und strukturieren: Anwendungsfall Student oder Referendar muss langen Sachverhalt oder Urteil in praegnante Fallzusammenfassung fassen und Kernprobleme herausarbeiten. Gutachtenstil, Tatbestandsmerkmale, Subsumtion Methodenlehre. Prüfraster Sachverhalt komprimieren, Kern-Rechtsfragen extrahieren, Obersatz und Subsumtion trennen, Relevantes von Irrelevantem trennen. Output strukturierte Fallzusammenfassung mit Rechtsfragen-Übersicht und Lösungshinweisen. Abgrenzung zu Gutachten-Uebung für vollständige Bearbeitung und zu Lösungsschemata im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Fallbearbeitung im Gutachtenstil

## Arbeitsbereich

Juristischen Fall zusammenfassen und strukturieren: Anwendungsfall Student oder Referendar muss langen Sachverhalt oder Urteil in praegnante Fallzusammenfassung fassen und Kernprobleme herausarbeiten. Gutachtenstil, Tatbestandsmerkmale, Subsumtion Methodenlehre. Prüfraster Sachverhalt komprimieren, Kern-Rechtsfragen extrahieren, Obersatz und Subsumtion trennen, Relevantes von Irrelevantem trennen. Output strukturierte Fallzusammenfassung mit Rechtsfragen-Übersicht und Lösungshinweisen. Abgrenzung zu Gutachten-Uebung für vollständige Bearbeitung und zu Lösungsschemata. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DRiG § 5a Studiendauer 9 Semester (Regelstudienzeit), Freischuss-Frist (i.d.R. 8 Semester nach JAG), Wiederholungsfrist, Hausarbeit 4-6 Wochen.
- Tragende Normen verifizieren: DRiG §§ 5, 5a, 5b (Erste Prüfung), JAG der Länder, JAPO Bayern, JAG NRW, BBesG (Referendariat), Hochschulgesetze, Studienordnungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Studierende, Justizprüfungsamt (Landesjustizverwaltung), Universität, Repetitorium, Klausurleiter, Mündliche-Prüfungs-Kommission.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Klausurgutachten (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis), Hausarbeit, Aktenvortrag (Referendar), Probeklausur, Prüfungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welches Fachgebiet und welches Prüfungsniveau (Hausarbeit, AG, Klausur, Examen)?
2. Soll das Gutachten vollstaendig oder nur schwerpunktmaessig erstellt werden?
3. Gibt es spezifische Anspruchsgrundlagen oder Streitstaende, die besonders durchgearbeitet werden sollen?
4. Soll das Ergebnis als Lernuebung (mit Rueckfragen) oder als fertiges Gutachten ausgegeben werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 433-453 BGB — Kaufrecht: Standardkomplex fuer Zivilrecht-Gutachten
- §§ 241-304 BGB — Leistungsstoerungsrecht: Kern-Anspruchsgrundlagen
- §§ 823-853 BGB — Deliktsrecht: zweite Pruefungssaule
- §§ 242, 263 StGB — Strafrecht-Standardtatbestaende fuer Klausur

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
2. **Aufgabenstellung** – "Prüfe alle Ansprüche" / "Ist die Klage begründet?" / "Prüfe die Strafbarkeit von A"
3. **Rechtsgebiet** (optional, wird aus Sachverhalt abgeleitet)
4. **Lernprofil** aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` → Lernstil (Drill / Erklärung), Semester, Schwächebereiche

## Das deutsche Gutachtenstil-Schema

Das Plugin verwendet **ausschließlich** das deutsche Vier-Schritte-Schema. IRAC ist die US-amerikanische Variante und hat im deutschen Jurastudium keine eigenständige Verwendung.

```
1. OBERSATZ
 Formulierung: "[Person] könnte gegen [Person] einen Anspruch auf
 [Rechtsfolge] gemäß § X BGB/StGB/VwGO haben."
 Pflicht: hypothetisch, nicht assertorisch. "A hat …" ist Urteilsstil → falsch
 für Klausuren.

2. DEFINITION
 Abstrakte Tatbestandsmerkmale der Norm (wörtlich oder paraphrasiert).
 Pflicht: Kommentarzitat oder Lehrbuchbeleg einfügen.
 Beispiel: "Besitz i. S. d. § 854 BGB ist die tatsächliche Sachherrschaft,
 lizenzpflichtige Literaturquelle/Herrler, BGB, 84. Aufl. 2025, § 854 Rn. 1."

3. SUBSUMTION
 Anwendung der abstrakten Merkmale auf die konkreten Sachverhaltsfakten.
 Pflicht: jeden Sachverhaltsaspekt explizit subsumieren, keine stillschweigen-
 de Übernahme. Streitstände auflösen (h.M. mit Beleg, Gegenauffassung benennen).

4. ERGEBNIS
 Kurze, eindeutige Aussage: "Damit hat A gegen B einen Anspruch auf X
 gemäß § Y BGB. / Der Anspruch besteht nicht."
```

## Anspruchsgrundlagen-Reihenfolge

Die Reihenfolge ist nicht beliebig – vgl. `../references/methodik-buergerliches-recht.md`:

1. Vertragliche Ansprüche (§§ 433, 535, 611 ff. BGB; Vertrag mit Schutzwirkung zugunsten Dritter)
2. Vorvertragliche Ansprüche aus c.i.c. (§§ 311 Abs. 2, 311 Abs. 3, 241 Abs. 2, 280 Abs. 1 BGB)
3. Geschäftsführung ohne Auftrag (§§ 677 ff. BGB)
4. Dingliche Ansprüche (§§ 985, 1004, 894, 1007 BGB)
5. Deliktische Ansprüche im engeren Sinne, verschuldensabhängig (§§ 823 Abs. 1, 823 Abs. 2, 824, 826, 831 BGB)
6. Gefährdungshaftung, verschuldensunabhängig (§ 7 StVG; § 1 ProdHaftG; § 1 HaftpflG; § 33 LuftVG; § 25 AtG; § 89 II WHG; § 84 AMG; § 32 GenTG; § 1 UmweltHG; § 833 S. 1 BGB)
7. Bereicherungsansprüche (§§ 812 ff. BGB)

Die Sammelbegriffe "vertragsähnlich" und "quasivertraglich" werden bewusst vermieden — sie sind in der Lehre uneinheitlich besetzt. Die Gefährdungshaftung ist eigenständige verschuldensunabhängige Haftungsspur, **kein** Unterfall des § 823 BGB; in Klausuren gern übersehen.

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

Im **Drill-Modus**: Fragen statt Hinweise. "Was ist der erste Anspruch, den du prüfst?"

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
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Quellen und Zitierweise

→ `../references/zitierweise.md` (verbindlich)

**Quellenregel für häufige BGB-Normen:**

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Leitentscheidungen (Beispiele für häufige Streitstände):**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

### Lösungsgliederung (Gerüst-Modus)

```
**Sachverhalt:** [Schlüsselfakten fett]

**Lösungsskizze – Gliederung**

A. Ansprüche des A gegen B
 I. § X BGB – [Kurzbezeichnung]
 Obersatz: [leer – deine Formulierung]
 Definition: [Hinweis auf Tatbestandsmerkmale; Kommentarstelle]
 Subsumtion: [leer – deine Subsumtion]
 Ergebnis: [leer]
 II. § Y BGB – [Kurzbezeichnung]
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

Definition: §§ 437 Nr. 3, 280 Abs. 1, 3, 281 BGB setzen einen Kaufvertrag mit mangelhafter Sache und Vertretenmüssen voraus. Ein Sachmangel liegt vor, wenn die Sache bei Gefahrübergang nicht die vereinbarte Beschaffenheit hat (§ 434 Abs. 1 BGB).

Subsumtion: Kaufvertrag liegt vor. Das Motorrad hatte eine mangelhafte Schweißnaht, die bereits bei Übergabe vorhanden war (§ 446 BGB: Gefahrübergang bei Übergabe). A kannte den Defekt → grob fahrlässige, jedenfalls vorsätzliche Pflichtverletzung. § 276 Abs. 1 S. 1 BGB: Vorsatz und Fahrlässigkeit werden vertreten. Fristsetzung (§ 281 Abs. 1 BGB): ggf. entbehrlich nach § 281 Abs. 2 BGB, weil A arglistig gehandelt hat.

Ergebnis: B hat einen Anspruch auf Schadensersatz statt der Leistung gemäß §§ 437 Nr. 3, 280 Abs. 1, 3, 281 Abs. 2 BGB.

*II. Deliktischer Anspruch gemäß § 823 Abs. 1 BGB*

Obersatz: B könnte auch einen deliktischen Anspruch auf Schadensersatz wegen Verletzung seiner Gesundheit gemäß § 823 Abs. 1 BGB haben.

[…] Verletzungserfolg (Körperverletzung), Kausalität, Rechtswidrigkeit (indiziert durch Tatbestand), Vorsatz des A (kannte Defekt). Haftungsbegründende und haftungsausfüllende Kausalität sind im Gutachten eigenständig zu begründen.

Ergebnis: Anspruch besteht.

*Literaturnachweise:*
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Risiken / typische Fehler

- **Assertorischer Obersatz:** "A hat einen Anspruch auf …" ist Urteilsstil und in Klausuren ein Aufbaufehler.
- **Subsumtion als Behauptung:** "Das Tatbestandsmerkmal liegt vor." ohne Sachverhaltsbezug ist keine Subsumtion.
- **Streitstand übergehen:** Leitentscheidungen und Kommentarstreitstände sind im 1. StEx Bewertungsbestandteil.
- **Konkurrenzfragen nicht lösen:** Wenn § 823 Abs. 1 BGB und §§ 437, 280 BGB nebeneinander bestehen, dies kurz konstatieren (kumulative Anspruchskonkurrenz).
- **Zu lange Obersätze:** Der Obersatz soll die Rechtsfolge benennen, nicht die gesamte Prüfung vorwegnehmen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
