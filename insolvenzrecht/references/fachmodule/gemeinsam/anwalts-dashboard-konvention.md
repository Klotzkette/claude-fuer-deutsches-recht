# Anwalts-Dashboard-Konvention für Einstiegs-Skills

> Diese Konvention gilt für `allgemein`/`einstieg-routing`/`kaltstart-triage`-Skills der **Anwalts-Plugins**. Ergänzt `https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/references/dashboard-template.md` (das die Output-Form behandelt) um die **Einstiegs-Form**: Was sieht ein Anwalt im ersten Bildschirm, der durch den Fall führt, ohne ihn zu entmündigen.

## Leitprinzipien

1. **Geschwindigkeit vor Höflichkeit.** Kein Vorgeplänkel, keine Plugin-Selbstvorstellung. Erste sichtbare Zeile zeigt die Triage-Tabelle.
2. **Tabelle vor Prosa.** Strukturen werden als Tabellen, Ampeln und Routenkarten gerendert, nicht als Fließtext. Tabellen sind scanbar, Fließtext nicht.
3. **Eine Rückfrage maximal.** Wenn die Akte 80 % der Triage trägt, wird der Rest mit `[noch zu klären: …]`-Platzhaltern markiert und sofort gearbeitet, nicht abgefragt.
4. **Human lawyers stay in charge.** Jede Empfehlung ist als Empfehlung markiert, nicht als Auto-Antwort. Entscheidungen treffen Menschen.
5. **Anschluss-Skills offen benannt.** Der Einstiegs-Skill ist nur eine Tür — der nächste Skill mit Slug, Aufgabe und Erwartung muss klar genannt sein.

## Standardaufbau (von oben nach unten)

### Visueller Anker (optional, vor Block 1)

Wenn der Fall typischerweise einen mehrstufigen Verfahrensablauf hat, darf am Anfang eine kompakte **Routenkarte als ASCII-Block** stehen — eine Zeile pro Phase, mit Pfeilen, ohne Lehrbuch. Beispiel Insolvenzrecht:

```
Antragsphase  -->  Eroeffnung 27/28 InsO  -->  Berichtstermin 156 InsO
     |                     |                          |
     |                     v                          v
Paragraf 15a InsO       VVB Paragraf 80 InsO              Verwertung 159 ff. InsO
3 Wochen         Treuhandkonten              Glaeubigerausschuss 160 InsO
```

Höchstens 10 Zeilen, klar lesbar in Monospace. Keine ASCII-Kunst um ihrer selbst willen — die Karte muss eine Frage beantworten, die die Tabelle nicht beantwortet (typischerweise: „wo stehe ich im Verfahrenslauf?").

### Block 1 — Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| Rolle | Wen vertrete ich? (Mandant / Gegenseite / Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual / Außergerichtlich / Klage / Rechtsmittel / Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | Welche Frist läuft heute, in 7, in 30 Tagen? | Frist berechnen aus Zugangsdatum |
| Hauptanspruch | Welche Anspruchsgrundlage(n) tragen den Fall? | Plugin-spezifisch (siehe Norm-Radar unten) |
| Zuständigkeit | Welches Gericht / welche Behörde? | Gesetzliche Zuständigkeit, vertragliche Gerichtsstandsklausel |

### Block 2 — Risiko-Ampel

Drei Achsen, je drei Stufen 🔴/🟠/🟢:

- **Frist:** 🔴 ≤ 7 Tage · 🟠 8-30 Tage · 🟢 > 30 Tage oder ohne harte Frist
- **Beweislage:** 🔴 Beweisnot · 🟠 lückenhaft, aber heilbar · 🟢 Beweisstand belastbar
- **Wirtschaftlich:** 🔴 existentiell · 🟠 erheblich · 🟢 überschaubar

Pro Ampel ein Satz Begründung, kein Lehrbuch.

### Block 3 — Anschluss-Skill-Router

Tabelle mit den 3-5 passendsten Spezial-Skills aus demselben Plugin:

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| Konkretes Sachverhaltsmerkmal | `slug-des-spezial-skills` | Welcher Output / welche Frist / welcher Beweisbedarf |

Höchstens fünf Zeilen. Eine vorrangige Empfehlung wird mit Fettung markiert; alternative Pfade darunter.

### Block 4 — Norm-Radar (eine Zeile pro Norm)

Maximal sechs tragende Normen mit kurzer Funktionsangabe. Beispiel: `§ 4 KSchG — 3-Wochen-Frist Kündigungsschutzklage`. Keine Kommentierung, kein Lehrbuch. Diese Zeilen sind Anker für die Spezial-Skills.

### Block 5 — Genau eine Rückfrage (nur wenn nötig)

Wenn die Akte 80 % der Triage trägt: keine Rückfrage, stattdessen sofort ein erster Entwurf mit klar gesetzten `[noch zu klären: …]`-Platzhaltern. Wenn doch eine Frage nötig ist: **eine** Frage, die die nächste Weiche tatsächlich umstellt. Keine Liste von zehn Punkten.

### Block 6 — Leitentscheidungs-Anker (Such-Wegweiser, kein Zitat)

Maximal 3-4 Themen-Anker aus `leitentscheidungen-anker.md`. Format pro Zeile: *Thema/Linie — wahrscheinlicher Spruchkörper — freie Quelle*. **Keine vollständigen Aktenzeichen behaupten**, sondern auf live-zu-verifizierende Quellen verweisen (BVerfG/BGH/BAG/BSG/BFH/BVerwG/EuGH-Homepage, dejure.org, openjur.de, curia.europa.eu). Damit hat der Anwalt die Rspr-Linien sofort sichtbar, ohne dass das Dashboard ein Halluzinationsrisiko schafft.

### Block 7 — Driver-Seat-Reminder

Genau ein Satz, am Ende des Dashboards: *„Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte."*

## Was bewusst weggelassen wird

- **Keine Plugin-Selbstvorstellung am Anfang.** Wer den Skill startet, weiß welches Plugin.
- **Keine Quellenhygiene-Predigt.** Die zentrale Quellenhygiene steht in `quellenhygiene.md`. Im Dashboard genügt ein Verweis am Ende.
- **Keine Lehrbuchpassagen.** Wer Dogmatik braucht, ruft den Spezial-Skill auf.
- **Keine sechs-Punkte-Pflichtfragen.** Eine.

## Beispiel-Skelett (für jedes Anwalts-Plugin gleich gegliedert)

```markdown
# Einstieg <Plugin> — Anwalts-Dashboard

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle |
| --- | --- | --- |
| Rolle | … | … |
| Verfahrensstand | … | … |
| Eilfrist | <Plugin-spezifische Frist> | … |
| Hauptanspruch | <plugin-spezifisch> | … |
| Zuständigkeit | <plugin-spezifisch> | … |

## Risiko-Ampel

- 🔴/🟠/🟢 Frist — <Satz>
- 🔴/🟠/🟢 Beweis — <Satz>
- 🔴/🟠/🟢 Wirtschaftlich — <Satz>

## Anschluss-Skills

| Wenn … | dann | Erwartung |
| --- | --- | --- |
| <Sachverhaltsmerkmal> | `<slug>` | <Output/Frist/Beweis> |

## Norm-Radar

- `<Norm>` — <Funktion>
- …

## Genau eine Rückfrage (falls nötig)

> [Eine konkrete Frage, die die nächste Weiche umstellt]

## Hinweis

Diese Triage ist Vorbereitung, nicht Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `quellenhygiene.md`, Zitierform nach `../../zitierweise.md`.
```

## Self-Test vor Freigabe

Bevor ein Einstiegs-Skill ausgeliefert wird, wird gegen diese sechs Fragen geprüft:

1. Sieht der Anwalt in den ersten 15 Zeilen die Triage-Tabelle?
2. Steht die Risiko-Ampel auf einer Seite mit der Triage?
3. Ist mindestens ein Anschluss-Skill konkret mit Slug benannt — und existiert dieser Slug real im Plugin-Verzeichnis?
4. Wird höchstens **eine** Rückfrage gestellt?
5. Sind 3-4 Leitentscheidungs-Anker mit *Thema, Spruchkörper, freier Quelle* (ohne erfundene Aktenzeichen) gesetzt?
6. Steht der Driver-Seat-Hinweis sichtbar am Ende?

Wenn ein Punkt fehlt, ist der Skill nicht freigegeben.
