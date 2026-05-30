---
name: verweis-und-querverweis-technik
description: "Verweis- und Querverweistechnik in juristischen Dokumenten. Interne Verweise auf Klauseln und Anlagen externe Verweise auf Gesetze und Urteile. Anlagenverwaltung jede Anlage einmal benannt einmal definiert einmal eingefuehrt. Word-Querverweise (siehe Skill word-formatvorlagen-querverweise-track-changes). vorstehender vs nachstehender. Vermeidung der Klausel-Spinne. Mit Beispiel konsolidierter Verweisapparat."
---

# Verweis- und Querverweis-Technik

## Zweck

Verweise machen einen Vertrag oder Schriftsatz lesbar oder zerstoeren ihn. Wer "im Sinne der vorstehenden Klausel" schreibt, hat keine Klausel benannt. Wer "Anlage 7" referenziert, ohne sie zu definieren, schafft eine Klausel-Spinne, die kein Reviewer mehr entwirrt.

Dieser Skill liefert die Verweistechnik: interne Verweise auf Klauseln und Anlagen, externe Verweise auf Gesetze, Verordnungen und Urteile. Er zeigt die Anlagenverwaltung mit dem Drei-Punkte-Prinzip: einmal benannt, einmal definiert, einmal eingefuehrt. Er verweist auf den Word-Skill fuer die technische Umsetzung der Querverweise.

## Eingaben

- Vertrag oder Schriftsatz mit Verweisstruktur
- Anlagenliste
- Verwendete Gesetze und Verordnungen
- Optional: Versionsstand zur Konsistenzpruefung

## Rechtlicher und methodischer Rahmen

- § 305 Abs. 2 BGB: Einbeziehung von AGB. Verweis auf AGB muss klar und auffindbar sein.
- §§ 133, 157 BGB: Auslegung. Defekte Verweise werden gegen den Verwender ausgelegt (§ 305c Abs. 2 BGB).
- Zitierweise nach `references/zitierweise.md` fuer externe Verweise auf Rechtsprechung und Literatur.
- Word-Funktion: automatische Querverweise mit Aktualisierung beim Druck. Siehe `word-formatvorlagen-querverweise-track-changes`.

## Ablauf / Checkliste

1. **Interne Verweise inventarisieren.** Welche Klauseln verweisen aufeinander?
2. **Anlagen inventarisieren.** Welche Anlagen werden zitiert? Sind sie alle vorhanden?
3. **Externe Verweise pruefen.** Sind Gesetzesangaben aktuell? Sind Rspr.-Zitate verifiziert?
4. **Verweisform pruefen.** Klauselnummer und Klauselueberschrift nennen ("§ 7 Abs. 2 (Haftung)").
5. **Querverweise als Word-Felder.** Bei Renumbering keine toten Verweise.
6. **Konsistenzpruefung.** Volltextsuche nach "siehe oben", "vorstehend", "nachstehend".
7. **Anlagenverzeichnis erstellen.** Anlage 1 bis Anlage n.

### Interne Verweise: Drei Regeln

1. **Klauselnummer plus Ueberschrift.** "§ 7 Abs. 2 (Haftung)" statt "vorstehender Absatz".
2. **Richtung explizit.** "siehe § 5" oder "wie in § 5 geregelt", nicht "siehe oben".
3. **Voll qualifiziert.** "Anlage 3 (Leistungsbeschreibung)", nicht "Anlage".

### Externe Verweise: Zitiermuster

- Gesetz: "§ 433 Abs. 1 Satz 1 BGB"
- EU-Recht: "Art. 6 Abs. 1 lit. f DSGVO"
- Rspr.: "BGH, Urt. v. TT.MM.JJJJ - Az. ... , [freie Quelle] Rn. ..."
- Mehrere Normen: "§§ 280 Abs. 1, 281 Abs. 1 und Abs. 2 BGB"

Externe Rspr.- und Literaturverweise nur, wenn verifiziert. Siehe `references/zitierweise.md`.

### Anlagenverwaltung: Drei-Punkte-Prinzip

| Schritt | Beispiel |
|---|---|
| 1. Benennen | "Anlage 3 (Leistungsbeschreibung)" im Anlagenverzeichnis |
| 2. Definieren | "Anlage 3 bezeichnet die in Anlage 3 zu diesem Vertrag enthaltene Leistungsbeschreibung." im Definitionen-Abschnitt |
| 3. Einfuehren | "Der Lieferant erbringt die in Anlage 3 (Leistungsbeschreibung) beschriebenen Leistungen." in der operativen Klausel |

### Beispiel: konsolidierter Verweisapparat

```
§ 1 Definitionen

"Anlage 1" bezeichnet die in Anlage 1 zu diesem Vertrag enthaltene
Leistungsbeschreibung.

"Anlage 2" bezeichnet die in Anlage 2 zu diesem Vertrag enthaltene
Preisliste.

§ 3 Leistung
Der Lieferant erbringt die in Anlage 1 (Leistungsbeschreibung) im
Einzelnen beschriebenen Leistungen.

§ 4 Verguetung
Die Verguetung richtet sich nach Anlage 2 (Preisliste).

§ 6 Maengelhaftung
(1) ...
(2) Bei Verzug gilt zusaetzlich § 4 Abs. 3 (Verzug).
(3) ...

§ 7 Haftung
(1) ...
(2) ...
Schadensersatzansprueche aus § 6 Abs. 2 (Maengelhaftung) und aus § 8
(Geheimhaltung) sind in der Hoehe nach diesem § 7 begrenzt.

Anlagenverzeichnis
Anlage 1 - Leistungsbeschreibung
Anlage 2 - Preisliste
Anlage 3 - Lieferplan
```

### Klausel-Spinne vermeiden

Eine Klausel-Spinne entsteht, wenn ein Begriff durch mehrere Klauseln laeuft, die sich gegenseitig verweisen, ohne dass die Hauptregel klar ist.

**Anti-Pattern:**

```
§ 3 ... soweit nicht in § 5 anders geregelt ...
§ 5 ... vorbehaltlich § 3 und § 7 ...
§ 7 ... unter Bezugnahme auf § 5 und § 3 ...
```

**Loesung:** Hauptregel in einer Klausel. Andere Klauseln verweisen nur in eine Richtung. Tabelle Verweis-Graph zeichnen.

### vorstehender und nachstehender

Vermeiden Sie diese Begriffe in operativen Klauseln. Sie sind Auslegungsmuell. Wenn unausweichlich, ergaenzen Sie die Klauselnummer:

- Statt "vorstehender Absatz" schreiben Sie "Abs. 1".
- Statt "vorstehender Paragraph" schreiben Sie "§ 6".
- Statt "nachstehender Absatz" schreiben Sie "Abs. 3".

## Typische Drafting-Fehler

- **Tote Verweise nach Renumbering.** Manuelle Klauselnummern statt Word-Querverweisfelder.
- **"Siehe oben" ohne Bezugsstelle.** Kein Reviewer findet die Stelle.
- **Anlage zitiert, aber nicht vorhanden.** Anlagenverzeichnis pruefen.
- **Externe Verweise auf veraltete Normen.** § Nummern haben sich geaendert (z.B. nach Schuldrechtsmodernisierung 2002, AGB-Reform 2002, BDSG-DSGVO-Umstellung 2018).
- **Rspr.-Zitate aus Modellwissen.** Verifikationspflicht nach `references/zitierweise.md`.
- **Klausel-Spinne.** Mehrfach kreisende Verweise. Hauptregel konsolidieren.

## Ausgabeformat

- Verweisapparat mit Tabelle Verweis-Quelle zu Verweis-Ziel.
- Konsistenzbericht (welche Verweise sind tot, welche doppelt).
- Empfehlung zur Konsolidierung.

## Beispiel

**Aufgabe:** Pruefen Sie den Verweisapparat folgender Klausel:

```
§ 7 Haftung
Soweit nicht im Vorstehenden anders bestimmt, haftet der Lieferant nur,
soweit dies in den nachstehenden Bestimmungen vorgesehen ist, wobei die
Regelungen in § 5 (Maengelhaftung) und in den dort genannten Anlagen
zu beachten sind, vorbehaltlich der Sonderregelungen in den Anlagen
zur Geheimhaltung.
```

**Pruefbericht:**

- "im Vorstehenden": ohne Bezug. Streichen.
- "in den nachstehenden Bestimmungen": keine Klauselnummer. Konkretisieren.
- "in den dort genannten Anlagen": Verweis zweiter Stufe. Direkt auf die Anlage zeigen.
- "Anlagen zur Geheimhaltung": ist eine Anlage gemeint oder mehrere? Nummerieren.

**Loesung:**

```
§ 7 Haftung
(1) Der Lieferant haftet nach Massgabe dieses § 7 in Verbindung mit
    § 6 (Maengelhaftung).
(2) Die Haftung fuer Geheimhaltungsverstoesse richtet sich nach § 8
    (Geheimhaltung) und Anlage 8 (Geheimhaltungsregeln).
(3) Im Uebrigen ist die Haftung ausgeschlossen.
```

## Querverweise

- `dokumentstruktur-makroebene-vertrag-und-schriftsatz`
- `definitionen-klauseln-stringent`
- `word-formatvorlagen-querverweise-track-changes`
- `drafting-prinzipien-klarheit-bestimmtheit-praezision`

## Quellen (Stand 05/2026)

- § 305 Abs. 2 BGB, § 305c Abs. 2 BGB, §§ 133, 157 BGB. gesetze-im-internet.de.
- `references/zitierweise.md` fuer externe Verweise.
- Word-Querverweistechnik: Microsoft-Dokumentation; konkrete Umsetzung in `word-formatvorlagen-querverweise-track-changes`.
