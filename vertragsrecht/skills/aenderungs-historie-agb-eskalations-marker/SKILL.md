---
name: aenderungs-historie-agb-eskalations-marker
description: "Aenderungs Historie AGB Eskalations Marker: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Aenderungs Historie AGB Eskalations Marker

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Aenderungs Historie AGB Eskalations Marker** im Plugin Vertragsrecht (BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aenderungs-historie` | Verfolgt, wie sich ein Vertrag über Basisvertrag und alle Nachträge hinweg verändert hat – entweder als Gesamtüberblick aller Änderungen oder als Klausel-Rückverfolgung für eine bestimmte Bestimmung. Laden, wenn der Nutzer fragt "was hat sich in diesem Vertrag geändert", "zeig mir die Nachtragshistorie", "wo steht die aktuelle [Klausel]" oder mehrere Vertragsversionen hochlädt. |
| `agb-pruefung` | Unterstützt bei der rechtlichen Prüfung von Allgemeinen Geschäftsbedingungen (AGB) auf Einbeziehung, Inhaltskontrolle und Transparenzgebot nach §§ 305–310 BGB. Lädt, wenn ein Mandat die Prüfung, Erstellung oder Verteidigung von AGB im B2C- oder B2B-Bereich zum Gegenstand hat. |
| `eskalations-marker` | Ordnet ein Vertragsproblem dem richtigen Genehmiger per Eskalationsmatrix aus dem Praxisprofil zu und erstellt die Genehmigungsanfrage. Laden, wenn der Nutzer fragt "wer muss das genehmigen", "eskalieren", "braucht das GC-Freigabe", "Genehmigung einholen" oder ein anderer Skill ein Problem identifiziert, das die Kompetenz des Prüfers übersteigt. |

## Arbeitsweg

Im Plugin Vertragsrecht (BGB) gilt für **Aenderungs Historie AGB Eskalations Marker**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aenderungs-historie`

**Fokus:** Verfolgt, wie sich ein Vertrag über Basisvertrag und alle Nachträge hinweg verändert hat – entweder als Gesamtüberblick aller Änderungen oder als Klausel-Rückverfolgung für eine bestimmte Bestimmung. Laden, wenn der Nutzer fragt "was hat sich in diesem Vertrag geändert", "zeig mir die Nachtragshistorie", "wo steht die aktuelle [Klausel]" oder mehrere Vertragsversionen hochlädt.

# Nachtragsverwaltung


## Triage zu Beginn

1. Liegen alle Vertragsversionen (Basisvertrag + alle Nachträge) vollständig vor?
2. Ist die chronologische Reihenfolge der Nachträge eindeutig — anhand von Datum oder Nummerierung?
3. Soll eine Gesamtübersicht (Modus 1) oder eine Klausel-Rückverfolgung (Modus 2) erstellt werden?
4. Gibt es Widersprüche zwischen Nachträgen die auf Auslegung nach § 157 BGB (lex posterior) hinweisen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- §§ 133, 157 BGB — Vertragsauslegung (lex posterior-Prinzip bei widersprüchlichen Klauseln)
- § 125, 126 BGB — Schriftformmängel (Nachtrag ohne Schriftform kann Gesamtvertrag kündbar machen)
- § 311 BGB — Vertragsänderungen und Ergänzungsvereinbarungen
- § 550 BGB — Schriftformerfordernis bei langfristiger Miete (mehr als 1 Jahr)
- § 154 BGB — fehlendes Einvernehmen über einzelne Punkte

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Verträge sammeln über die Zeit Nachträge an. Spätestens beim dritten Nachtrag erinnert sich niemand mehr, was im Ursprungsvertrag stand oder welche Fassung einer Klausel gilt. Dieser Skill liest den Basisvertrag und alle Nachträge in chronologischer Reihenfolge und erstellt entweder eine Gesamtübersicht aller Änderungen oder verfolgt eine bestimmte Klausel durch jede Fassung bis zur aktuell geltenden Regelung.

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

## Ausgabeformat

Memo-Format. Kein Schriftsatz-Stil. Klarer Prüf-Hinweis (⚠️ Prüfer-Hinweis) über dem Dokument gemäß CLAUDE.md.

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Relevante Normen:
- § 311 BGB – Vertragsänderungen; Schriftformerfordernis prüfen (§ 126 BGB)
- §§ 133, 157 BGB – Auslegung; bei Widersprüchen zwischen Basisvertrag und Nachtrag gilt der jüngere Nachtrag (lex posterior-Prinzip), sofern kein expliziter Vorrang)
- § 154 BGB – Fehlen der Einigung über einzelne Punkte
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

## 2. `agb-pruefung`

**Fokus:** Unterstützt bei der rechtlichen Prüfung von Allgemeinen Geschäftsbedingungen (AGB) auf Einbeziehung, Inhaltskontrolle und Transparenzgebot nach §§ 305–310 BGB. Lädt, wenn ein Mandat die Prüfung, Erstellung oder Verteidigung von AGB im B2C- oder B2B-Bereich zum Gegenstand hat.

# AGB-Prüfung – Einbeziehung und Inhaltskontrolle

## Zweck

Dieser Skill begleitet die vollständige AGB-rechtliche Prüfung nach §§ 305–310 BGB. Er deckt
drei Prüfungsebenen ab: (1) wirksame Einbeziehung (§§ 305–305c BGB), (2) Auslegung
(§§ 305b, 305c Abs. 2 BGB) und (3) Inhaltskontrolle (§§ 307–309 BGB). Typische Mandate:
Gestaltung oder Revision von Online-AGB (B2C/E-Commerce), Lieferanten- und Einkaufsbedingungen
(B2B), Prüfung fremder AGB im Rahmen einer Vertragsverhandlung.

## Eingaben

Das Modell benötigt:

1. **AGB-Text**: vollständiger Wortlaut der zu prüfenden Klauseln oder des gesamten Klauselwerks
2. **Vertragstyp**: Kauf-, Werk-, Dienst-, Miet- oder sonstiger Vertrag
3. **Vertragsparteien**: B2C (Verbraucher i. S. v. § 13 BGB) oder B2B (Unternehmer § 14 BGB);
 ggf. gemischte Konstellationen
4. **Einbeziehungsmodalitäten**: Wie werden AGB einbezogen (Webshop, Bestellformular,
 Rahmenvertrag)? Liegen Hinweis und Möglichkeit zur Kenntnisnahme vor?
5. **Besondere Branchen**: Energieversorgung, Banken, Versicherungen (Sonderregelungen)

## Rechtlicher Rahmen

### Normen

- **§ 305 Abs. 1–3 BGB** – AGB-Begriff, Einbeziehungsvoraussetzungen
- **§ 305a BGB** – Einbeziehung durch besondere Umstände (Fernkommunikation etc.)
- **§ 305b BGB** – Vorrang der Individualabrede
- **§ 305c BGB** – überraschende und mehrdeutige Klauseln; Unklarheitenregel Abs. 2
- **§ 306 BGB** – Rechtsfolge der Unwirksamkeit (Restgültigkeit des Vertrags, dispositivem Recht)
- **§ 307 BGB** – Inhaltskontrolle; Abs. 1 S. 2 Transparenzgebot; Abs. 2 Nr. 1 (Abweichung
 von Grundgedanken), Nr. 2 (Gefährdung des Vertragszwecks)
- **§ 308 BGB** – Klauselverbote mit Wertungsmöglichkeit
- **§ 309 BGB** – Klauselverbote ohne Wertungsmöglichkeit (absolute Verbote)
- **§ 310 Abs. 1 BGB** – eingeschränkte Anwendung §§ 308, 309 im B2B-Verkehr; nur § 307 BGB
 vollanwendbar

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 von AGB im Onlinehandel; der bloße Verweis auf "unsere AGB" genügt, wenn die Klauseln vor
 Vertragsschluss klar zugänglich sind; kein Erfordernis, dass der Verbraucher die AGB
 tatsächlich liest.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 § 307 Abs. 1 S. 2 BGB; eine Preisanpassungsklausel ist unwirksam, wenn sie dem Verwender
 die einseitige Anpassung ermöglicht, ohne dass der Vertragspartner die Höhe vorhersehen kann.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Laufzeitklauseln im B2B-Bereich; auch im B2B gilt § 307 BGB; eine übermäßig lange
 Bindungsfrist kann den Vertragspartner unangemessen benachteiligen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 § 305c Abs. 2 BGB; bei zwei vertretbaren Auslegungen ist die für den Verwender ungünstigere
 maßgeblich.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Qualifikation als AGB** (§ 305 Abs. 1 BGB): Sind die Klauseln vorformuliert für eine
 Vielzahl von Verträgen? Wurde der Inhalt vom Verwender gestellt? Cave: 3-Verträge-Regel
 der Rspr.
2. **Einbeziehungsprüfung** (§§ 305 Abs. 2, 305a BGB):
 - Deutlicher Hinweis vor Vertragsschluss?
 - Zumutbare Möglichkeit der Kenntnisnahme (Link oder Aushang)?
 - Bei B2B: § 305 Abs. 2 BGB gilt nicht; konkludente Einbeziehung durch Handelsbrauch
 möglich (§ 346 HGB).
3. **Individualabrede** (§ 305b BGB): Vorrang prüfen; Individualabrede muss ernsthaft
 ausgehandelt sein (BGH: blo­ßes Textmarkieren im Formular ≠ Aushandeln).
4. **Überraschungsklauseln** (§ 305c Abs. 1 BGB): Ungewöhnlich und nicht zu erwarten?
 Klausel wird nicht Vertragsbestandteil.
5. **Auslegung** (§ 305c Abs. 2 BGB): Bei Unklarheit → kundenfreundlichste Auslegung.
6. **Inhaltskontrolle** §§ 307–309 BGB in der Prüfreihenfolge:
 a. § 309 BGB (Verbote ohne Wertungsmöglichkeit) – abschließende schwarze Liste
 b. § 308 BGB (Verbote mit Wertungsmöglichkeit) – graue Liste
 c. § 307 BGB (Generalklausel) – unangemessene Benachteiligung; Transparenzgebot
 Im B2B-Verkehr: §§ 308, 309 BGB gelten nur als Indizien für § 307 BGB
 (§ 310 Abs. 1 S. 2 BGB).
7. **Rechtsfolge** (§ 306 BGB): Unwirksame Klausel entfällt; Vertrag bleibt im Übrigen
 wirksam; dispositives Recht tritt an die Stelle (Lückenfüllung).
8. **Empfehlung**: Klausel-für-Klausel-Tabelle mit Ampelsystem (grün/gelb/rot) und
 Überarbeitungsvorschlägen.

## Ausgabeformat

- **Prüftabelle** (Klausel | Prüfungsmaßstab | Ergebnis | Überarbeitungsvorschlag)
- **Rechtliches Memo** (Gutachtenstil) für kritische Klauseln mit ausführlicher Subsumtion
- Auf Wunsch: **überarbeiteter AGB-Entwurf** mit nachverfolgbaren Änderungen

## Beispiel

**Sachverhalt**: Eine Online-Plattform (B2C) verwendet folgende Klausel: "Änderungen an den
AGB werden dem Kunden per E-Mail mitgeteilt. Widerspricht der Kunde nicht binnen 6 Wochen,
gilt seine Zustimmung als erteilt."

**Prüfung (Gutachtenstil)**:

*§ 308 Nr. 5 BGB*: Die Klausel fingiert eine Willenserklärung (Zustimmung) durch Schweigen.
Nach § 308 Nr. 5 lit. b BGB müsste der Verwender den Kunden auf die Bedeutung seines
Schweigens hinweisen. Ob ein ausreichender Hinweis in der E-Mail liegt, ist im Einzelfall zu
prüfen. Fehlt er, ist die Klausel nach § 308 Nr. 5 BGB unwirksam.

*Zusätzlich § 307 Abs. 1 S. 2 BGB (Transparenzgebot)*: Die Frist von 6 Wochen ist nach
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Verbraucher nicht erkennen kann, welche konkreten Änderungen gelten sollen.

**Ergebnis**: Klausel ist unwirksam. Empfohlen: Opt-in-Lösung mit aktiver Bestätigung.

## Risiken und typische Fehler

- **Einbeziehungsfehler**: AGB werden erst nach Vertragsschluss übermittelt → nicht wirksam
 einbezogen (§ 305 Abs. 2 BGB); besonders kritisch bei E-Commerce.
- **Überraschungsklauseln** (§ 305c BGB): Klauseln an unerwarteter Stelle (z. B. Haftungsaus-
 schluss in Lieferbedingungen) → unwirksam ohne Hinweis.
- **Unterschätzung des B2B-Risikos**: Auch B2B-AGB unterliegen § 307 BGB; übermäßige
 Haftungsfreizeichnungen und einseitige Preisänderungsrechte werden vom BGH kassiert.
- **Transparenzgebot** § 307 Abs. 1 S. 2 BGB: Preis­nachberechnungsklauseln ohne
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Geltungserhaltende Reduktion**: Im deutschen AGB-Recht grundsätzlich nicht zulässig
 (BGH st. Rspr.); unwirksame Klausel entfällt ersatzlos oder wird durch dispositives Recht
 ersetzt.
- **Berufsrecht**: Keine Klauseln entwerfen, die § 43a BRAO oder berufsrechtliche Verbote
 umgehen; Verschwiegenheit § 203 StGB beachten.

## Quellenpflicht

Jede AGB-Bewertung ist nach `references/zitierweise.md` zu belegen. Für jede als unwirksam
eingestufte Klausel ist die einschlägige BGH-Entscheidung oder die herrschende Kommentarmeinung
zu zitieren (Bearbeiter, Werk, Aufl., §, Rn.). Bei abweichender Instanzrechtsprechung ist auf
den Streitstand hinzuweisen. "Die Klausel ist unwirksam" ohne Beleg ist kein ausreichendes
Ergebnis.

## 3. `eskalations-marker`

**Fokus:** Ordnet ein Vertragsproblem dem richtigen Genehmiger per Eskalationsmatrix aus dem Praxisprofil zu und erstellt die Genehmigungsanfrage. Laden, wenn der Nutzer fragt "wer muss das genehmigen", "eskalieren", "braucht das GC-Freigabe", "Genehmigung einholen" oder ein anderer Skill ein Problem identifiziert, das die Kompetenz des Prüfers übersteigt.

# Eskalationsregeln


## Triage zu Beginn

1. Welcher Eskalationsauslöser liegt vor — Betrags-Schwelle, Klausel-Abweichung oder automatischer Auslöser?
2. Auf welcher Seite steht das Unternehmen (Käufer oder Verkäufer) — welches Playbook gilt?
3. Wer ist der konkrete Genehmiger laut Eskalationsmatrix (CLAUDE.md)?
4. Bis wann muss eine Entscheidung vorliegen (Verhandlungsdeadline)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 164 ff. BGB — Vertretung; Vollmacht; Vertretungsmacht
- § 177 BGB — Genehmigung vollmachtlosen Handelns
- § 311 Abs. 2 BGB — culpa in contrahendo (Vorvertragspflichten)
- §§ 5-8 LkSG — Sorgfaltspflichten (Eskalationsauslöser bei Lieferkettenverstößen)
- Art. 33, 34 DSGVO — Meldepflichten bei Datenpannen (Eskalationsauslöser)
- § 43a Abs. 2 BRAO — anwaltliche Verschwiegenheitspflicht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Jede Rechtsabteilung hat eine Eskalationsmatrix – geschrieben oder ungeschrieben. Dieser Skill liest die geschriebene (in `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md`), ordnet ein Vertragsproblem darin ein, nennt den Genehmiger beim Namen und entwirft die Anfrage – damit der Jurist nicht abends schnell eine "hast du kurz?"-E-Mail schreibt.

## Eingaben

- Beschreibung des Problems (direkt oder Verweis auf Prüfvermerk)
- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## Eskalation`
- Jahreswert/ACV des Vertrags (für Betrags-Schwellenwerte)

## Akten-Kontext

Falls Akten-Arbeitsbereiche aktiviert, aktive Akte prüfen. Ausgaben im Akten-Ordner speichern.

## Ablauf

### Schritt 1: Matrix laden

`~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## Eskalation` lesen. Falls fehlend oder vage: Hinweis, dass das Praxisprofil ergänzt werden muss.

**Welche Seite?** Käufer- oder Verkäufer-Playbook bestimmt, ob ein Begriff innerhalb der Fallback-Positionen liegt oder eine automatische Eskalation auslöst. Seite im Entwurf vermerken.

### Schritt 2: Problem einordnen

Was wird eskaliert?

- **Betrags-Schwelle:** Vertragswert übersteigt Genehmigungskompetenz
- **Klausel-Abweichung:** Ein Begriff liegt außerhalb der Playbook-Fallback-Positionen; eine erfahrenere Person muss entscheiden, ob Akzeptanz gerechtfertigt ist
- **Automatischer Eskalationsauslöser:** Immer-Eskalieren-Liste (z. B. unbegrenzte Haftung, IP-Abtretung, Datenschutzverstoß ohne Remediation, LkSG-Pflichtverletzung)
- **Geschäftliche Entscheidung:** Keine Rechtsfrage, sondern ein Thema für den Business-Owner

Dinge nicht eskalieren, die eigentlich in Ordnung sind. Wenn der Begriff innerhalb der Fallback-Positionen liegt, braucht er keine Eskalation.

### Schritt 3: Genehmiger bestimmen

Zutreffende Matrixzeile auswählen. Konkrete Person oder Rolle nennen – keine abstrakte "Führungsebene".

### Schritt 4: Anfrage entwerfen

Vorlage (immer verwenden):

```markdown
Betreff: Genehmigung erforderlich – [Vertrag] mit [Vertragspartner] – [Problembezeichnung]

[Name],

ich bitte um Genehmigung zu folgendem Vertragspunkt:

**Vertrag:** [Bezeichnung und Vertragspartner]
**ACV:** [Jahreswert]
**Klausel / Problem:** [§ X – Kurzbezeichnung]

**Was der Vertrag sagt:**
> "[wörtliches Zitat der betroffenen Klausel]"

**Was unser Playbook sagt:**
[Standard-Position aus CLAUDE.md] / [Fallback-Position aus CLAUDE.md]

**Warum das eskaliert:**
[Ein Satz: Betrags-Schwelle / Abweichung außerhalb Fallback / automatischer Auslöser / Geschäftsentscheidung]

**Risiko bei Akzeptanz ohne Änderung:**
🔴/🟠/🟡 [Rechtliches Risiko] | 🔴/🟠/🟡 [Geschäftliche Reibung]
[Konkrete Folge: z. B. "Unbegrenzte Haftung für Datenpannen; typischer Schaden bei mittelgroßem Verstoß XXX EUR"]

**Optionen:**

1. **Akzeptieren** – [Bedingung oder unkonditioniert]
 Konsequenz: [was das bedeutet, z. B. "unbegrenzte Haftung bleibt bestehen; kein Deckungsschutz D&O"]

2. **Verhandeln** – Redline: [konkrete Formulierung]
 Verhandlungsspielraum: [einschätzen, ob Markt-Standard / Gegenseite wird wahrscheinlich...]

3. **Ablehnen** – [Begründung gegenüber Gegenseite]

**Empfehlung:** Option [N] – [ein Satz Begründung]

**Entscheidung bis:** [Datum] (Verhandlungsdeadline oder Vertragsabschluss-Termin)

Bei Rückfragen stehe ich gerne zur Verfügung.

[Absender]
```

### Schritt 5: Nicht versenden

Entwurf anzeigen, Anwalt sendet. Niemals ohne ausdrückliche Bestätigung absenden.

## Ausgabeformat

```markdown
VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS (§ 43a II BRAO)

## Eskalation: [Vertrag] mit [Vertragspartner] – [Klausel]

**Eskalationsgrund:** [Betrags-Schwelle / Klausel-Abweichung / Automatischer Auslöser / Geschäftsentscheidung]
**Genehmiger:** [Person/Rolle aus CLAUDE.md]
**Kontaktweg:** [Slack / E-Mail / Meeting]
**Seite:** [Käufer/Verkäufer – welches Playbook wurde angewendet]

---

[Entwurf der Genehmigungsanfrage gemäß Vorlage oben]

---

⚠️ Prüfer-Hinweis: Vor dem Versand prüfen, ob der Entwurf die Sachlage korrekt wiedergibt und keine privilegierten Informationen unbeabsichtigt preisgibt.
```

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Relevante Normen:
- § 164 ff. BGB – Vertretungsmacht; Vollmacht
- § 177 BGB – Genehmigung vollmachtlosen Handelns
- § 43a Abs. 2 BRAO – anwaltliche Verschwiegenheitspflicht
- Bei LkSG-Eskalation: §§ 5–8 LkSG – Sorgfaltspflichten, Risikoanalyse, Präventionsmaßnahmen
- Bei DSGVO-Eskalation: Art. 33, 34 DSGVO – Melde- und Benachrichtigungspflichten

## Risiken / typische Fehler

- **Zu viel eskalieren:** Wenn alles eskaliert wird, verliert die Matrix ihre Wirkung. Nur wirkliche Überschreitungen eskalieren.
- **Entscheidung vorwegnehmen:** Der Entwurf bietet Optionen – er trifft keine Entscheidung. Der Genehmiger entscheidet.
- **Frist vergessen:** Ohne Entscheidungs-Datum läuft die Verhandlung. Immer ein Datum nennen.
- **Privilegierter Inhalt außerhalb des Kreises:** Genehmigungsanfragen intern halten; § 43a Abs. 2 BRAO, § 203 StGB beachten.
