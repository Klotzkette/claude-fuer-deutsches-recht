---
name: nachtragsverwaltung
description: Verfolgt, wie sich ein Vertrag über Basisvertrag und alle Nachträge hinweg verändert hat – entweder als Gesamtüberblick aller Änderungen oder als Klausel-Rückverfolgung für eine bestimmte Bestimmung. Laden, wenn der Nutzer fragt „was hat sich in diesem Vertrag geändert", „zeig mir die Nachtragshistorie", „wo steht die aktuelle [Klausel]" oder mehrere Vertragsversionen hochlädt.
language: de
triggers:
  - "nachtrag"
  - "vertragsänderung"
  - "nachtragshistorie"
  - "klausel verfolgen"
  - "amendment"
---

# Nachtragsverwaltung

## Zweck

Verträge sammeln über die Zeit Nachträge an. Spätestens beim dritten Nachtrag erinnert sich niemand mehr, was im Ursprungsvertrag stand oder welche Fassung einer Klausel gilt. Dieser Skill liest den Basisvertrag und alle Nachträge in chronologischer Reihenfolge und erstellt entweder eine Gesamtübersicht aller Änderungen oder verfolgt eine bestimmte Klausel durch jede Fassung bis zur aktuell geltenden Regelung.

## Eingaben

- Basisvertrag und alle Nachträge (Datei-Upload, CLM-Referenz oder Direkteingabe)
- Optional: Name der zu verfolgenden Klausel (bei Modus 2)
- Optional: `--tage N` zur Änderung des Beobachtungszeitraums im Verlängerungstracker

## Akten-Kontext

Falls Akten-Arbeitsbereiche aktiviert sind (Kanzleibetrieb), die aktive Akte prüfen. Wenn keine aktive Akte vorhanden: „Für welche Akte ist das? `/vertragsrecht:akte wechsel <kürzel>` ausführen oder `praxisebene` angeben." Ausgaben in den Akten-Ordner schreiben. Nie eine andere Akte lesen, solange der aktenübergreifende Kontext nicht eingeschaltet ist.

## Ablauf

### Schritt 1: Dokumente laden und ordnen

Dokumente aus folgenden Quellen akzeptieren:

**Direkter Upload:** Nutzer stellt Dateien direkt bereit. In den meisten Fällen ergibt sich die Reihenfolge aus Dokumenttiteln (z. B. „Nachtrag Nr. 1", „Zweiter Nachtrag", „Nachtrag A") oder Daten im Dateinamen oder Dokumentkopf.

**Reihenfolge nur fragen, wenn:**
- Dateinamen keinen Hinweis auf Reihenfolge geben
- Kein Datum in Dateinamen oder Dokumentkopf
- Zwei Dokumente offenbar dieselbe Nachtragsfassung sind

Wenn Reihenfolge erschlossen wurde statt bestätigt:
> „Reihenfolge aus Dokumenttiteln erschlossen – bei [spezifischem Dokument] war ich weniger sicher. Bitte bestätigen, falls dies Ihre Prüfung betrifft."

**Ordnungsregeln:**
- Immer chronologische Reihenfolge festlegen, bevor Inhalt gelesen wird.
- Unterfertigungsdaten aus Metadaten nutzen, falls vorhanden.
- Sonst Daten im Dokumentkopf oder in Präambeln suchen.
- Nachträge verweisen oft auf den Vertrag, den sie ändern – zur Bestätigung der Kette nutzen.

### Schritt 2: Modus erkennen

Anhand der Anfrage bestimmen, welcher Modus zu nutzen ist. Nur bei echter Mehrdeutigkeit fragen.

**Modus 1 – Gesamtübersicht** (keine bestimmte Klausel genannt)
Auslöse-Formulierungen: „was hat sich geändert", „Nachtragshistorie", „Änderungen im Zeitverlauf", „Nachträge zusammenfassen", „wie sieht der Vertrag jetzt aus"

**Modus 2 – Klausel-Rückverfolgung** (bestimmte Klausel oder Thema genannt)
Auslöse-Formulierungen: „wo steht die [Klausel]", „aktuelle [Bestimmung]", „wie hat sich [Begriff] geändert", „finde die Haftungsklausel", „was steht jetzt zu [Thema]"

Häufige Klausel-Zuordnungen:
- „Haftung" / „Haftungsbegrenzung" → Haftungsbeschränkungsklausel
- „Freistellung" / „Indemnity" → Freistellungsklausel
- „Kündigung" → Laufzeit und Kündigung
- „Daten" / „Datenschutz" / „AVV" → Datenschutzbestimmungen
- „IP" / „geistiges Eigentum" / „Nutzungsrechte" → IP-Bestimmungen
- „Preis" / „Vergütung" / „Zahlung" → Vergütungsregelungen
- „Verlängerung" / „Laufzeit" → Verlängerungsmechanismus
- „Vertragsstrafe" → § 339 BGB-Klausel

Bei echter Mehrdeutigkeit eine Frage stellen:
> „Gesamtübersicht aller Änderungen, oder eine bestimmte Klausel verfolgen – z. B. Haftung, Kündigung oder Vergütung?"

### Schritt 3: Lesen und indexieren

Jedes Dokument in chronologischer Reihenfolge lesen. Für jedes Dokument entnehmen:
- Dokumenttyp (Basisvertrag, Nachtrag Nr. X, Ergänzungsvereinbarung usw.)
- Unterfertigungsdatum
- Parteien (auf Übereinstimmung quer prüfen – kennzeichnen, wenn neue Partei hinzugekommen oder Parteibezeichnung geändert wurde)
- Liste der ausdrücklich geänderten, hinzugefügten oder gestrichenen Bestimmungen

Einen internen Arbeitsindex aufbauen, bevor eine Ausgabe erstellt wird. Intern nutzen – nicht dem Nutzer zeigen.

## Modus 1: Gesamtübersicht aller Änderungen

### Abschnittsverweis-Regel

Jeder Befund muss einen Inline-Abschnittsverweis enthalten, damit der Leser die Quelle prüfen kann, ohne zu suchen:

  „Ordentliche Kündigung (§ 12 Abs. 3): Neu eingefügt. Auftraggeber kann mit 3 Monaten Frist kündigen, keine Vergütungsnachzahlung nach Ablauf der Erstlaufzeit."

Falls eine Bestimmung mehrere Abschnitte überspannt oder die Abschnittsnummer über Nachträge geändert wurde, alle Verweise zitieren:
  „Haftungsbegrenzung (§ 9 Abs. 1 Basisvertrag; § 9 Abs. 1 neu gefasst in Nachtrag 3)"

### Ausgabeformat

```markdown
# Nachtragsübersicht: [Vertragspartner] – [Vertragstyp]

**Basisvertrag:** [Datum]
**Nachträge:** [Anzahl] ([Datum erster] → [Datum letzter])
**Zuletzt geändert:** [Datum]

---

## Was geändert wurde – chronologisch

### Nachtrag 1 – [Datum]
**Zweck:** [ein Satz – warum dieser Nachtrag, aus Präambel oder aus Kontext erkennbar. Falls nicht ersichtlich, weglassen.]

**Wesentliche Änderungen:**
- [Bestimmung] (§ [X.X]): [was vorher stand → was jetzt steht, in Klartext]
- [Neue Bestimmung eingefügt] (§ [X.X]): [was sie regelt]
- [Bestimmung gestrichen] (§ [X.X]): [was entfernt wurde und warum das relevant ist]

### Nachtrag 2 – [Datum]
[dieselbe Struktur]

[für jeden Nachtrag wiederholen]

---

## Aktueller Gesamtstand

| Bestimmung | Aktuelle Regelung | §-Verweis | Zuletzt geändert |
|---|---|---|---|
| [Klausel] | [Klartext-Zusammenfassung] | §[X.X] | Nachtrag N, [Datum] |
| [Klausel] | [unverändert seit Basisvertrag] | §[X.X] | Basisvertrag |

---

## Hinweise
[Alles kennzeichnen, das inkonsistent erscheint – z. B. ein Nachtrag, der eine bereits gestrichene Bestimmung ändert; widersprüchliche Formulierungen zwischen Nachträgen; eine Parteibezeichnung, die ohne förmliche Abtretung geändert wurde; eine Bestimmung, bei der die Abschnittsnummer über Dokumente hinweg verschoben ist. Jeden Hinweis mit Abschnittsverweis versehen.]
```

---

## Modus 2: Klausel-Rückverfolgung

Nur änderungen zeigen. Nachträge, in denen die Bestimmung unberührt blieb, vollständig weglassen.

```markdown
# Klausel-Rückverfolgung: [Bestimmungsname]
## [Vertragspartner] – [Vertragstyp]

---

### Ursprung – Basisvertrag [Datum], §[X.X]
> „[wörtliches Zitat]"

*Klartext:* [ein Satz]

---

### Nachtrag [N] – [Datum], §[X.X]

**Vorher:**
> „[wörtliches Zitat der vorherigen Fassung]"

**Jetzt:**
> „[wörtliches Zitat der Ersatzformulierung]"

*Was sich geändert hat:* [ein Satz – praktische Auswirkung auf die Parteien]

---

[Nur nachfolgende Nachträge erscheinen hier, die diese Bestimmung berührt haben. Alle anderen werden weggelassen.]

---

## Aktuell geltende Formulierung

**§[X.X] – [Quelle, Datum]**
> „[wörtliches Zitat]"

*Klartext:* [ein Satz]

---

## Hinweise
[Kennzeichnungen, Inkonsistenzen, offene Fragen – mit Abschnittsverweis. Typische Prüfpunkte: Ob die Bestimmung dem Haftungsdeckel unterliegt oder davon ausgenommen ist; ob die Abschnittsnummer über Nachträge verschoben ist; ob die Formulierung in einem anderen § widersprochen wird.]
```

Falls die Bestimmung nach dem Basisvertrag nie geändert wurde:
> „Diese Bestimmung wurde durch keinen Nachtrag geändert. Die ursprüngliche Formulierung gilt. §[X.X], Basisvertrag, [Datum]."

## Ausgabeformat

Memo-Format. Kein Schriftsatz-Stil. Klarer Prüf-Hinweis (⚠️ Prüfer-Hinweis) über dem Dokument gemäß CLAUDE.md.

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Relevante Normen:
- § 311 BGB – Vertragsänderungen; Schriftformerfordernis prüfen (§ 126 BGB)
- §§ 133, 157 BGB – Auslegung; bei Widersprüchen zwischen Basisvertrag und Nachtrag gilt der jüngere Nachtrag (lex posterior-Prinzip), sofern kein expliziter Vorrang)
- § 154 BGB – Fehlen der Einigung über einzelne Punkte
- BGH, Urt. v. 07.02.2002 – I ZR 304/99, NJW 2002, 2710 – Auslegung von Vertragsänderungen

Kommentare:
- Busche, in: MüKoBGB, 9. Aufl. 2021, § 133 Rn. 10 ff. (Auslegung)
- Ellenberger, in: Grüneberg, BGB, 83. Aufl. 2024, § 157 Rn. 3 ff.

## Beispiel

**Anfrage:** „Nachtrag 2 zum Softwarepflegevertrag mit Acme GmbH – was hat sich bei der Haftungsklausel geändert?"

**Klausel-Rückverfolgung – Haftungsbegrenzung (§ 8)**

*Basisvertrag, 01.03.2021, § 8 Abs. 1:*
> „Die Haftung des Auftragnehmers ist der Höhe nach auf die im letzten Vertragsjahr gezahlte Jahresvergütung begrenzt."

*Nachtrag 1, 15.11.2022, § 8 Abs. 1 (neu gefasst):*
Vorher: s. o. | Jetzt:
> „Die Haftung des Auftragnehmers ist auf das Zweifache der im letzten Vertragsjahr gezahlten Jahresvergütung begrenzt. Hiervon ausgenommen ist die Haftung für Vorsatz und grobe Fahrlässigkeit sowie für Schäden aus der Verletzung von Leben, Körper oder Gesundheit."

*Was sich geändert hat:* Haftungsdeckel wurde von einfacher auf doppelte Jahresvergütung angehoben; Kardinalpflichten-/Verletzung von Leben/Körper/Gesundheit-Ausnahmen normkonform (§ 309 Nr. 7 BGB) ergänzt. `[Trainingswissen – prüfen]`

## Risiken / typische Fehler

- **Reihenfolge-Fehler:** Falsches Datum eines Nachtrags führt zu falscher Ergebnisfassung. Immer Unterfertigungsdaten aus Dokumentkopf oder Präambel entnehmen.
- **Stiller Widerspruch:** Nachtrag N ändert eine Bestimmung, ohne Nachtrag N-1 ausdrücklich aufzuheben. lex-posterior-Grundsatz anwenden und als Hinweis markieren.
- **Schriftformklausel:** Mündliche Nebenabsprachen können durch eine Schriftformklausel (§ 125 BGB i. V. m. Vertragsklausel) unwirksam sein. Prüfen, ob eine solche Klausel im Basisvertrag oder einem Nachtrag steht.
- **Skill-Grenzen:** Dieser Skill stellt nicht fest, welches Dokument bei Widersprüchen vorgeht – das ist eine Auslegungsfrage. Er kennzeichnet Widersprüche und leitet an die Rechtsabteilung weiter. Er entwirft keine neuen Nachträge. Er prüft nicht gegen das Playbook – das ist Aufgabe des Lieferantenvertrag-Prüfungs-Skills.
