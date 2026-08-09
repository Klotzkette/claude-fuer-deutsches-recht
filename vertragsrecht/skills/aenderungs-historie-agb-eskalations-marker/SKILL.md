---
name: aenderungs-historie-agb-eskalations-marker
description: "Wenn es um Nachtragsverwaltung in Vertragsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen."
---

# Nachtragsverwaltung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Liegen alle Vertragsversionen (Basisvertrag + alle Nachträge) vollständig vor?
2. Ist die chronologische Reihenfolge der Nachträge eindeutig — anhand von Datum oder Nummerierung?
3. Soll eine Gesamtübersicht (Modus 1) oder eine Klausel-Rückverfolgung (Modus 2) erstellt werden?
4. Gibt es Widersprüche zwischen Nachträgen die auf Auslegung nach § 157 BGB (lex posterior) hinweisen?

## Zentrale Normen

- §§ 133, 157 BGB — Vertragsauslegung (lex posterior-Prinzip bei widersprüchlichen Klauseln)
- Paragrafen 125 und 126 BGB — gesetzliche Schriftform und Rechtsfolgen
- Paragraf 126b BGB — Textform
- Paragraf 311 BGB — Vertragsänderungen und Ergänzungsvereinbarungen
- Paragraf 578 Absatz 1 in Verbindung mit Paragraf 550 BGB — Textform bei langfristiger Grundstücks- und Gewerberaummiete; Artikel 229 Paragraf 70 EGBGB bei älteren Vertragsketten
- Paragraf 154 BGB — fehlendes Einvernehmen über einzelne Punkte

## Eingaben

- Basisvertrag und alle Nachträge (Datei-Upload, CLM-Referenz oder Direkteingabe)
- Optional: Name der zu verfolgenden Klausel (bei Modus 2)
- Optional: `--tage N` zur Änderung des Beobachtungszeitraums im Verlängerungstracker

## Akten-Kontext

Falls Akten-Arbeitsbereiche aktiviert sind (Kanzleibetrieb), die aktive Akte prüfen. Wenn keine aktive Akte vorhanden: "Für welche Akte ist das? `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich wechsel <kürzel>` ausführen oder `praxisebene` angeben." Ausgaben in den Akten-Ordner schreiben. Nie eine andere Akte lesen, solange der aktenübergreifende Kontext nicht eingeschaltet ist.

## Ablauf

### Schritt 1: Dokumente laden und ordnen

Dokumente aus folgenden Quellen akzeptieren:

**Direkter Upload:** Nutzer stellt Dateien direkt bereit. In den meisten Fällen ergibt sich die Reihenfolge aus Dokumenttiteln (z. B. "Nachtrag Nr. 1", "Zweiter Nachtrag", "Nachtrag A") oder Daten im Dateinamen oder Dokumentkopf.

**Reihenfolge nur fragen, wenn:**
- Dateinamen keinen Hinweis auf Reihenfolge geben
- Kein Datum in Dateinamen oder Dokumentkopf
- Zwei Dokumente offenbar dieselbe Nachtragsfassung sind

Wenn Reihenfolge erschlossen wurde statt bestätigt:
> "Reihenfolge aus Dokumenttiteln erschlossen – bei [spezifischem Dokument] war ich weniger sicher. Bitte bestätigen, falls dies Ihre Prüfung betrifft."

**Ordnungsregeln:**
- Immer chronologische Reihenfolge festlegen, bevor Inhalt gelesen wird.
- Unterfertigungsdaten aus Metadaten nutzen, falls vorhanden.
- Sonst Daten im Dokumentkopf oder in Präambeln suchen.
- Nachträge verweisen oft auf den Vertrag, den sie ändern – zur Bestätigung der Kette nutzen.

### Schritt 2: Modus erkennen

Anhand der Anfrage bestimmen, welcher Modus zu nutzen ist. Nur bei echter Mehrdeutigkeit fragen.

**Modus 1 – Gesamtübersicht** (keine bestimmte Klausel genannt)
Auslöse-Formulierungen: "was hat sich geändert", "Nachtragshistorie", "Änderungen im Zeitverlauf", "Nachträge zusammenfassen", "wie sieht der Vertrag jetzt aus"

**Modus 2 – Klausel-Rückverfolgung** (bestimmte Klausel oder Thema genannt)
Auslöse-Formulierungen: "wo steht die [Klausel]", "aktuelle [Bestimmung]", "wie hat sich [Begriff] geändert", "finde die Haftungsklausel", "was steht jetzt zu [Thema]"

Häufige Klausel-Zuordnungen:
- "Haftung" / "Haftungsbegrenzung" → Haftungsbeschränkungsklausel
- "Freistellung" / "Indemnity" → Freistellungsklausel
- "Kündigung" → Laufzeit und Kündigung
- "Daten" / "Datenschutz" / "AVV" → Datenschutzbestimmungen
- "IP" / "geistiges Eigentum" / "Nutzungsrechte" → IP-Bestimmungen
- "Preis" / "Vergütung" / "Zahlung" → Vergütungsregelungen
- "Verlängerung" / "Laufzeit" → Verlängerungsmechanismus
- "Vertragsstrafe" → § 339 BGB-Klausel

Bei echter Mehrdeutigkeit eine Frage stellen:
> "Gesamtübersicht aller Änderungen, oder eine bestimmte Klausel verfolgen – z. B. Haftung, Kündigung oder Vergütung?"

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

 "Ordentliche Kündigung (§ 12 Abs. 3): Neu eingefügt. Auftraggeber kann mit 3 Monaten Frist kündigen, keine Vergütungsnachzahlung nach Ablauf der Erstlaufzeit."

Falls eine Bestimmung mehrere Abschnitte überspannt oder die Abschnittsnummer über Nachträge geändert wurde, alle Verweise zitieren:
 "Haftungsbegrenzung (§ 9 Abs. 1 Basisvertrag; § 9 Abs. 1 neu gefasst in Nachtrag 3)"

### Ausgabeformat

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

```markdown
### Nachtragsübersicht: [Vertragspartner] – [Vertragstyp]

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
### Klausel-Rückverfolgung: [Bestimmungsname]

## [Vertragspartner] – [Vertragstyp]

---

### Ursprung – Basisvertrag [Datum], §[X.X]
> "[wörtliches Zitat]"

*Klartext:* [ein Satz]

---

### Nachtrag [N] – [Datum], §[X.X]

**Vorher:**
> "[wörtliches Zitat der vorherigen Fassung]"

**Jetzt:**
> "[wörtliches Zitat der Ersatzformulierung]"

*Was sich geändert hat:* [ein Satz – praktische Auswirkung auf die Parteien]

---

[Nur nachfolgende Nachträge erscheinen hier, die diese Bestimmung berührt haben. Alle anderen werden weggelassen.]

---

## Aktuell geltende Formulierung

**§[X.X] – [Quelle, Datum]**
> "[wörtliches Zitat]"

*Klartext:* [ein Satz]

---

## Hinweise
[Kennzeichnungen, Inkonsistenzen, offene Fragen – mit Abschnittsverweis. Typische Prüfpunkte: Ob die Bestimmung dem Haftungsdeckel unterliegt oder davon ausgenommen ist; ob die Abschnittsnummer über Nachträge verschoben ist; ob die Formulierung in einem anderen § widersprochen wird.]
```

Falls die Bestimmung nach dem Basisvertrag nie geändert wurde:
> "Diese Bestimmung wurde durch keinen Nachtrag geändert. Die ursprüngliche Formulierung gilt. §[X.X], Basisvertrag, [Datum]."

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Relevante Normen:
- § 311 BGB – Vertragsänderungen; Schriftformerfordernis prüfen (§ 126 BGB)
- §§ 133, 157 BGB – Auslegung; bei Widersprüchen zwischen Basisvertrag und Nachtrag gilt der jüngere Nachtrag (lex posterior-Prinzip), sofern kein expliziter Vorrang)
- § 154 BGB – Fehlen der Einigung über einzelne Punkte

Kommentare:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispiel

**Anfrage:** "Nachtrag 2 zum Softwarepflegevertrag mit Acme GmbH – was hat sich bei der Haftungsklausel geändert?"

**Klausel-Rückverfolgung – Haftungsbegrenzung (§ 8)**

*Basisvertrag, 01.03.2021, § 8 Abs. 1:*
> "Die Haftung des Auftragnehmers ist der Höhe nach auf die im letzten Vertragsjahr gezahlte Jahresvergütung begrenzt."

*Nachtrag 1, 15.11.2022, § 8 Abs. 1 (neu gefasst):*
Vorher: s. o. | Jetzt:
> "Die Haftung des Auftragnehmers ist auf das Zweifache der im letzten Vertragsjahr gezahlten Jahresvergütung begrenzt. Hiervon ausgenommen ist die Haftung für Vorsatz und grobe Fahrlässigkeit sowie für Schäden aus der Verletzung von Leben, Körper oder Gesundheit."

*Was sich geändert hat:* Haftungsdeckel wurde von einfacher auf doppelte Jahresvergütung angehoben; Kardinalpflichten-/Verletzung von Leben/Körper/Gesundheit-Ausnahmen normkonform (§ 309 Nr. 7 BGB) ergänzt. `[Trainingswissen – prüfen]`

## Risiken / typische Fehler

- **Reihenfolge-Fehler:** Falsches Datum eines Nachtrags führt zu falscher Ergebnisfassung. Immer Unterfertigungsdaten aus Dokumentkopf oder Präambel entnehmen.
- **Stiller Widerspruch:** Nachtrag N ändert eine Bestimmung, ohne Nachtrag N-1 ausdrücklich aufzuheben. lex-posterior-Grundsatz anwenden und als Hinweis markieren.
- **Schriftformklausel:** Mündliche Nebenabsprachen können durch eine Schriftformklausel (§ 125 BGB i. V. m. Vertragsklausel) unwirksam sein. Prüfen, ob eine solche Klausel im Basisvertrag oder einem Nachtrag steht.
- **Skill-Grenzen:** Dieser Skill stellt nicht fest, welches Dokument bei Widersprüchen vorgeht – das ist eine Auslegungsfrage. Er kennzeichnet Widersprüche und leitet an die Rechtsabteilung weiter. Er entwirft keine neuen Nachträge. Er prüft nicht gegen das Playbook – das ist Aufgabe des Lieferantenvertrag-Prüfungs-Skills.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
