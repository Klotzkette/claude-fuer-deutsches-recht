---
name: jurastudium-juristisches-schreiben-jus
description: "Juristisches Schreiben JUS: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Juristisches Schreiben JUS

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Juristisches Schreiben JUS** im Plugin Jurastudium (Klausur, AG, Examen). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jurastudium-anpassen` | Lernprofil im Jurastudium anpassen und aktualisieren: Anwendungsfall Student wechselt Lernstil, aendert Studienschwerpunkte, wechselt Bundesland oder aktualisiert Prüfungsziel von Zwischenprüfung auf Examen. 1. und 2. Staatsexamen, JAG Bundesland. Prüfraster Lernstil-Typ, Faecher-Auswahl, Bundesland-Spezifika, Prüfungsziel, verfuegbare Ressourcen amtliche/freie Quellen und lizenzierte Datenbanken nur bei vorhandenem Zugang Bibliothek. Output aktualisiertes Lernprofil mit neuer Schwerpunktsetzung. Abgrenzung zu Jurastudium-Kaltstart für Erst-Konfiguration und zu Lernplan. |
| `juristisches-schreiben` | Juristisches Schreiben trainieren für Klausur und Seminararbeit: Anwendungsfall Student will Schreibstil verbessern und benoetigt Feedback zu Formulierungen Argumentationsstruktur und Praegnanz. Gutachtenstil, Lösungsschemata, Subsumtion Methodenlehre Buergerliches Recht. Prüfraster Satzstruktur juristisch korrekt, Definitionen prazise, Subsumtion vollständig, Praegnanz ohne Weitschweifigkeit, Zitierweise korrekt. Output kommentierter Text mit Verbesserungsvorschlaegen zu Stil und Struktur. Abgrenzung zu Gutachten-Uebung für inhaltliche Prüfung und zu Subsumtionslehre. |
| `jus-klausurtraining-leitfaden` | Leitfaden Klausurtraining: Sachverhaltsanalyse, Aufbau, Zeitmanagement, typische Fehler. Pruefraster fuer Klausurenkurs Z1 / Z2 / Examen. |

## Arbeitsweg

Im Plugin Jurastudium (Klausur, AG, Examen) gilt für **Juristisches Schreiben JUS**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jurastudium-anpassen`

**Fokus:** Lernprofil im Jurastudium anpassen und aktualisieren: Anwendungsfall Student wechselt Lernstil, aendert Studienschwerpunkte, wechselt Bundesland oder aktualisiert Prüfungsziel von Zwischenprüfung auf Examen. 1. und 2. Staatsexamen, JAG Bundesland. Prüfraster Lernstil-Typ, Faecher-Auswahl, Bundesland-Spezifika, Prüfungsziel, verfuegbare Ressourcen amtliche/freie Quellen und lizenzierte Datenbanken nur bei vorhandenem Zugang Bibliothek. Output aktualisiertes Lernprofil mit neuer Schwerpunktsetzung. Abgrenzung zu Jurastudium-Kaltstart für Erst-Konfiguration und zu Lernplan.

# Lernprofil anpassen


## Triage zu Beginn
1. Welches Element des Lernprofils soll angepasst werden: Lernstil, Faecher, Bundesland, Prüfungsziel?
2. Gibt es einen konkreten Anlass (neue Pruefung, Schwachstelle erkannt, Semesterwechsel)?
3. Welches Prüfungsziel gilt jetzt (Zwischenpruefung, 1. StEx, 2. StEx, Schwerpunktbereich)?
4. Welche Ressourcen stehen zur Verfuegung (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang, Bibliothek, Lerngruppe)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 13 JAG NRW — Pruefungsinhalte 1. Staatsexamen (exemplarisch); andere Laender aequivalent
- Art. 3 GG — Chancengleichheit: Grundlage fuer bundeslandspezifische Lernprofile
- §§ 133, 157 BGB — Auslegungsmethoden: unveraendert kernelementig in allen Profilen
- § 195 BGB — Verjaehrung als Dauerklassiker: bleibt in jedem Profil

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ändert einzelne oder mehrere Einträge im Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`, ohne das gesamte Kaltstart-Interview erneut zu durchlaufen.

Einsatzbereiche:
- Semesterwechsel (neue Lehrveranstaltungen, neues Prüfungsziel)
- Lernstil wechseln (Drill → Erklärung oder umgekehrt)
- Bundesland / JAG aktualisieren (z. B. nach Hochschulwechsel)
- Neues Material hinzufügen (Klausuren, Gliederungen)
- Schwächen- und Stärkenprofil nach Prüfungsergebnissen anpassen
- `--reset`: vollständiges Löschen des Profils (vor neuem Kaltstart)

## Eingaben

1. **Flag** (optional): `--lernstil`, `--bundesland`, `--fach`, `--material`, `--examen`, `--reset`
2. Ohne Flag: interaktives Menü mit allen anpassbaren Feldern
3. Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`

## Ablauf

### Ohne Flag: Interaktives Menü

```
Was möchtest du anpassen?
1. Lernstil (aktuell: [Drill / Erklärung])
2. Bundesland / JAG (aktuell: [X])
3. Ziel-Examen und Prüfungstermin (aktuell: [X])
4. Aktuelle Lehrveranstaltungen
5. Schwächen / Stärken
6. Material hinzufügen
7. Repetitorium wechseln
8. Profil vollständig zurücksetzen (--reset)
```

### `--lernstil`

Wechsel zwischen:
- **Drill-Modus:** Sokratisch, kein Vorwegnehmen der Antwort, Nachbohren
- **Erklärungs-Modus:** Erst Erklärung, dann Selbsttest, mehr Gerüst

Gilt sofort für alle nachfolgenden Skills in dieser Sitzung und wird in `CLAUDE.md` gespeichert.

### `--bundesland`

Fragt nach neuem Bundesland und JAG, prüft Konsistenz:
> "Nach dem Wechsel von NRW nach Bayern unterscheiden sich die Prüfungsfächer im 1. StEx. Ich aktualisiere das Profil. Bitte bestätige: [neue Fächerliste nach JAG Bayern]."

### `--fach`

Fügt eine Lehrveranstaltung hinzu oder entfernt sie:
- Name der Veranstaltung
- Prüfungsformat (Klausur / Hausarbeit / mündlich)
- Semesterwoche

### `--material`

Nimmt neues Lernmaterial auf:
- Dateipfad oder Textinhalt (benotete Klausur, Gliederung, JPA-Klausur)
- Aktualisiert den Materialzähler im Profil
- Entfernt `WENIG MATERIAL`-Flag, sobald ≥ 10 Positionen vorhanden

### `--examen`

Aktualisiert Prüfungsziel, Prüfungstermin und Repetitorium.

### `--reset`

Sicherheitsabfrage:
> "Du löschst das gesamte Lernprofil. Diese Aktion ist nicht rückgängig zu machen. Danach musst du kaltstart-interview erneut durchlaufen. Fortfahren? (ja / nein)"

## Quellen und Zitierweise

Dieser Skill ändert nur Konfigurationsdaten. Keine juristischen Inhalte. Zitierregeln → `../references/zitierweise.md` gelten in den inhaltlichen Skills.

## Ausgabeformat

Nach jeder Änderung:

```
**Profil aktualisiert**

Geändert:
- [Feld]: [alter Wert] → [neuer Wert]

Nicht geändert:
- [Feld]: [aktueller Wert] (unverändert)

Gespeichert in: ~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md

**Auswirkungen auf laufende Skills:**
- lernplan: [wird beim nächsten Aufruf mit neuen Daten neu berechnet]
- examens-prognose: [aktualisiert Prüfungsgebietsliste nach neuer JAG]
- examensvorbereitung-fragen: [neue Bundesland-Filterung aktiv]
```

## Beispiel

**Anfrage:** "Ich habe jetzt auch VwGO als Pflichtfach und möchte auf Drill-Modus wechseln."

**Ausgabe:**

```
Profil aktualisiert:
- Lernstil: Erklärung → Drill
- Lehrveranstaltungen: VwGO-Klausur (Klausur, Woche 1) hinzugefügt

Auswirkungen:
- pruefungsgespraech-ag, ag-vorbereitung, gutachten-übung: ab sofort Drill-Modus
- examensvorbereitung-fragen: VwGO jetzt in der Fächerliste
- lernplan: wird beim nächsten Aufruf mit VwGO ergänzt
```

## Risiken / typische Fehler

- **Falsches Bundesland nach Hochschulwechsel nicht aktualisieren:** Alle Examensprognosen und Lernpläne arbeiten mit dem gespeicherten Bundesland. Bei Wechsel immer sofort `--bundesland` ausführen.
- **Veraltete Lehrveranstaltungen nicht entfernen:** Beendete Fächer im Profil lassen laufen, führt zu Studienplan-Verzerrungen.
- **`--reset` versehentlich ausführen:** Das Plugin fragt zur Sicherheit nach. Antwort "nein" bricht ab. Vor dem Reset eigene Gliederungen sichern.
- **Material nicht hochladen nach neuen Klausurergebnissen:** `examens-prognose` und `gutachten-uebung` werden genauer, wenn benotete Klausuren im Profil sind. Nach jeder Prüfungsrückgabe `--material` ausführen.

## 2. `juristisches-schreiben`

**Fokus:** Juristisches Schreiben trainieren für Klausur und Seminararbeit: Anwendungsfall Student will Schreibstil verbessern und benoetigt Feedback zu Formulierungen Argumentationsstruktur und Praegnanz. Gutachtenstil, Lösungsschemata, Subsumtion Methodenlehre Buergerliches Recht. Prüfraster Satzstruktur juristisch korrekt, Definitionen prazise, Subsumtion vollständig, Praegnanz ohne Weitschweifigkeit, Zitierweise korrekt. Output kommentierter Text mit Verbesserungsvorschlaegen zu Stil und Struktur. Abgrenzung zu Gutachten-Uebung für inhaltliche Prüfung und zu Subsumtionslehre.

# Juristische Schreibberatung

## Zweck

Juristische Schreibkompetenz entsteht durch eigenes Schreiben, Feedback und Überarbeitung — nicht dadurch, dass jemand anders den Text schreibt. Diese Skill liest den eingereichten Entwurf, benennt strukturelle und sprachliche Defizite mit Belegen aus dem Text, zeigt Techniken — und überlässt die Überarbeitung dem Studierenden.

**Hardregel: Kein Umschreiben. Nie.** Strukturelles Feedback ist das Produkt. Maximal ein bis zwei markierte Formulierungsbeispiele zur Demonstration einer Technik, mit explizitem Hinweis "eigene Variante formulieren, nicht übernehmen." Wenn das Feedback in "so sollte der Absatz lauten" übergeht, hat die Skill ihren Zweck verfehlt.

## Eingaben

- **Entwurf** (als Text einfügen oder Pfad angeben)
- **Textsorte** (Hausarbeit, Seminararbeit, Dissertation, Aufsatz, Klausur im Urteilsstil)
- **Rechtsgebiet und Problemstellung** (kurze Angabe)
- **Prüfungsmaßstab** (Examensarbeit / Seminarnote / Einreichung bei JuS, JA, NJW-etc.)
- Optional: **Aufgabenstellung** oder Bewertungsrichtlinien des Betreuers

## Rechtlicher Rahmen

Wissenschaftlicher juristischer Stil folgt Konventionen, die in Stil- und Methodenhandbüchern sowie in den Zitierregeln der großen Fachzeitschriften kodifiziert sind.

**Maßgebliche Stilquellen:**
- Byrd/Lehmann, Zitierfibel für Juristen, 3. Aufl. 2022 — deutsche Zitierregeln
- Möllers, Juristische Arbeitstechnik und wissenschaftliches Arbeiten, 10. Aufl. 2021
- Schimmel, Juristische Klausuren und Hausarbeiten richtig formulieren, 13. Aufl. 2022
- Wissenschaftliche Schreibweise gemäß Hinweisen der Deutschen Vereinigung für Internationales Recht (DVIR) und Zeitschriftenrichtlinien JuS/NJW

**Leitentscheidungen für Zitiergenauigkeit:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kommentare und Formatnachweise:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Creifelds, Rechtswörterbuch, 24. Aufl. 2023 — Begriffsdefinitionen

## Ablauf

### Schritt 1: Entwurf vollständig lesen

Vor der Kommentierung den gesamten Text lesen. Keine Reaktion auf den ersten Fehler. Holistische Gesamtschau vor Detailkritik — sonst wird eine Liste von Kleinstfixes erzeugt, die das strukturelle Hauptproblem übersieht.

### Schritt 2: Textsorte bestimmen

| Textsorte | Erwartete Struktur |
|---|---|
| **Hausarbeit / Seminararbeit** | Titelblatt, Gliederung, Einleitung (Problemaufriss), Hauptteil mit Gliederungsebenen, Schluss (Zusammenfassung/Stellungnahme), Literaturverzeichnis, Selbständigkeitserklärung |
| **Dissertation** | Umfassende Gliederung, Forschungsstand, eigene These, Methode, Durchführung, Ergebnis, Zusammenfassung |
| **JuS/JA-Aufsatz** | Straffes Format: Einleitung (ein Absatz), Problemdarstellung, Lösungsweg, ggf. Stellungnahme, kurze Zusammenfassung; Zitate im Fußnotenapparat |
| **Klausur im Urteilsstil** | Ergebnis vorangestellt (Tenor), dann Begründung strukturiert nach Tatbestand / Rechtsfragen |

Textsorte explizit benennen. Eine Hausarbeit, die wie ein Aufsatz ohne Gliederung strukturiert ist, ist keine gute Hausarbeit.

### Schritt 3: Strukturiertes Feedback (kein Umschreiben)

Feedback von oben nach unten: Struktur zuerst, dann Absatzebene, dann Satzebene. Nicht auf Tippfehler springen, wenn die Gliederung fehlt.

```markdown
# Schreib-Feedback — [Aufgabe / Datum]

**Textsorte:** [Hausarbeit / Seminararbeit / Aufsatz / Klausur]
**Länge:** [N Wörter / N Seiten] [ggf. Vergleich mit Vorgabe]
**Gesamtbild:** [Ein Satz.]

---

## Struktur (zuerst beheben, wenn fehlerhaft)

**Gliederungskonformität:** [Entspricht die Gliederung der Textsorte? Sind Gliederungsebenen konsistent nummeriert — z. B. A. I. 1. a)?]

**These / Problemaufriss:** [Vorhanden? In der Einleitung klar formuliert? Vom Schlussteil beantwortet?]

**Argumentation:** [Behauptung + Begründung + Beleg in jedem Hauptargument vorhanden? Oder Behauptungen ohne Begründung?]

**Übergänge:** [Verbinden die Abschnitte, oder wirkt jeder Abschnitt wie ein eigenständiger Aufsatz?]

**Wichtigste strukturelle Korrektur (falls nötig):** [Eine konkrete Maßnahme.]

## Argumentationstiefe

**Rechtsnormdarstellung:** [Normen genannt und inhaltlich entfaltet? Oder nur zitiert ohne Auslegung?]

**Subsumtion / Rechtsanwendung:** [Wird die Norm auf den konkreten Sachverhalt oder die Rechtsfrage angewendet? Oder wird die Norm referiert und dann die Schlussfolgerung behauptet?]

**Gegenpositionen:** [Auseinandersetzung mit Gegenansichten? Oder werden abweichende Meinungen nur erwähnt ohne Erwiderung?]

**Konkretes Defizit:** [z. B. "Im dritten Abschnitt wird die h.M. zu § 138 BGB dargestellt, aber nicht begründet, warum die Gegenansicht abzulehnen ist."]

## Sprachlicher Stil

**Konklusivformulierungen:** [Stellen, an denen das Ergebnis ohne Herleitung steht — in der Regel ein Zeichen, dass der Absatz umzukehren ist.]

**Passiv-Übermaß:** [Spezifische Beispiele — nicht die allgemeine Empfehlung "Aktiv verwenden".]

**Redundanz:** [Passagen, die auf die Hälfte gekürzt werden könnten, ohne Substanzverlust.]

**Zitierweise:** [Häufige Fehler — Fußnoten-Ebene, Kurzform nach Erstnennung, id./a.a.O.-Verwendung, Seitenzahl/Randnummernangabe, Herausgeber bei Kommentaren.] PRÜFEN bei Zweifelsfällen gegen Byrd/Lehmann.

## Top 3 Korrekturen (nach Priorität)

1. [Strukturell, falls zutreffend]
2. [Argumentationstiefe, falls zutreffend]
3. [Stilistisch, falls zutreffend]

## Demonstrationsbeispiel — nicht übernehmen

*Nur wenn eine konkrete Schreibtechnik zu zeigen ist. Maximal ein Beispiel, deutlich markiert.*

> Demonstrationsformulierung (eigene Variante formulieren, nicht kopieren):
> "[Abstraktes Beispiel der Technik — z. B. Behauptung-Begründung-Beleg-Struktur — ohne den konkreten Inhalt der Arbeit des Studierenden]"

---

**Nicht umgeschrieben. Kein Muster-Entwurf. Der Text bleibt Ihrer.**
```

### Schritt 4: Bei Umschreibungswunsch

Abgelehnt. Sachlich, ohne Moralisieren:

> "Umschreiben ist nicht das Angebot dieser Skill. Das Schreiben selbst ist der Lernprozess. Spezifischeres Feedback zu einem bestimmten Abschnitt gebe ich gern — welchen Absatz soll ich genauer analysieren? Oder ein sokrates-artiges Gespräch über die Argumentation, die Sie treffen wollen."

### Schritt 5: Muster festhalten

Nach 3+ Sitzungen: Wiederkehrende Schwächen benennen:
- "Sie setzen bei drei Hausarbeiten Normen voraus, ohne sie auszulegen."
- "Die Gliederung ist stets durchdacht; das Defizit liegt bei der Auseinandersetzung mit Gegenmeinungen."

## Ausgabeformat

Strukturiertes Feedback nach dem Schema in Schritt 3. Einschätzung nach Notentendenz (mit Vorbehalt: Betreuer kennen Aufgabenspezifika, die diese Skill nicht kennt). Keine Endnoten, kein Gesamtpunktwert.

## Beispiel

**Textsorte:** Seminararbeit Schuldrecht BT (Kaufrecht), 15 Seiten

**Typischer Befund:** Gliederungsebene springt von "A. Einleitung" zu "1. Problematik" ohne konsistente Hierarchie. Im Hauptteil wird § 434 BGB (Sachmangel) in zwei Sätzen dargestellt ohne Auslegung der Tatbestandsmerkmale. Die Gegenansicht zum Fehlerbegriff (subjektiver vs. objektiver Fehlerbegriff nach Kaufrechtsreform 2022) wird erwähnt, aber nicht inhaltlich auseinandergesetzt. Schlussabsatz beginnt mit Ergebnis ohne Herleitung.

**Feedback-Schwerpunkte:** Gliederungskonsistenz, Normauslegung § 434 BGB n.F., Meinungsstreit-Darstellung, Schlussstruktur.

## Risiken und typische Fehler

- **Normen nur zitieren, nicht auslegen**: "Gemäß § 280 Abs. 1 BGB ist Schadensersatz zu leisten" ist keine juristische Argumentation. Die Norm muss auf die Rechtsfrage ausgelegt und angewendet werden.
- **Literaturverzeichnis als Legitimation**: Viele Fußnoten ersetzen keine Argumentation. Jede Quellenangabe muss einer inhaltlichen Aussage im Text entsprechen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- **Kein Forschungsstand in Seminar- und Dissertationsarbeiten**: Wissenschaftliche Arbeiten müssen den Stand der Diskussion aufnehmen — Monografien, Aufsätze in NJW, JZ, AcP, ZHR, DÖV — nicht nur Kommentare.
- **These ≠ Fragestellung**: Eine Hausarbeit, die nur referiert, ist kein wissenschaftlicher Text. Eine eigene Stellungnahme ist strukturell erforderlich.

## Quellenpflicht

Zitierhinweise in diesem Feedback folgen den gängigen deutschen Zitierkonventionen (Byrd/Lehmann, Zitierfibel für Juristen, 3. Aufl. 2022). Inhaltliche Angaben zu Rechtsnormen und Rechtsprechung sind mit `[PRÜFEN]` markiert, wenn keine Quellenverifikation möglich ist. Vor Einreichung alle Nachweise gegen aktuelle Quellen abgleichen.

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

<!-- AUDIT 27.05.2026: BGH VI ZR 116/12 (WRONG_TOPIC: echtes Thema Straßenverkehrsunfall NJW 2013, 1679, nicht Schriftsatzanforderungen NJW 2013, 1682 Rn. 12) korrigiert; Fundstelle auf NJW 2013, 1679 berichtigt und Beschreibung an echten Urteilsinhalt angepasst. -->

## 3. `jus-klausurtraining-leitfaden`

**Fokus:** Leitfaden Klausurtraining: Sachverhaltsanalyse, Aufbau, Zeitmanagement, typische Fehler. Pruefraster fuer Klausurenkurs Z1 / Z2 / Examen.

# JuS: Klausurtraining

## Spezialwissen: JuS: Klausurtraining
- **Spezialgegenstand:** JuS: Klausurtraining / jus klausurtraining leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH, BVerfG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
