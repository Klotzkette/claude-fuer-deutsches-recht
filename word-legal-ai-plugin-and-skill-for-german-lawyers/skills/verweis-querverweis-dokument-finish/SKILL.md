---
name: verweis-querverweis-dokument-finish
description: "Verweis Querverweis Dokument Finish: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verweis Querverweis Dokument Finish

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Verweis Querverweis Dokument Finish** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verweis-und-querverweis-technik` | Verweis- und Querverweistechnik in juristischen Dokumenten. Interne Verweise auf Klauseln und Anlagen, externe Verweise auf Gesetze und Urteile. Anlagenverwaltung: jede Anlage einmal benannt, einmal definiert, einmal eingeführt. Vorstehender vs. nachstehender Verweis, Vermeidung der Klausel-Spinne, konsolidierter Verweisapparat. |
| `word-dokument-finish-und-layout` | Finalisiert juristische Word-Dokumente vor Versand. Prüft Formatvorlagen, Nummerierung, Inhaltsverzeichnis, Querverweise, Anlagen, Track Changes, Kommentare, Metadaten, PDF/beA-Tauglichkeit, Unterschriftenblock, Tabellen, Seitenumbrüche und optische Konsistenz. Liefert eine Versand-Checkliste und konkrete Reparaturanweisungen. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Verweis Querverweis Dokument Finish**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verweis-und-querverweis-technik`

**Fokus:** Verweis- und Querverweistechnik in juristischen Dokumenten. Interne Verweise auf Klauseln und Anlagen, externe Verweise auf Gesetze und Urteile. Anlagenverwaltung: jede Anlage einmal benannt, einmal definiert, einmal eingeführt. Vorstehender vs. nachstehender Verweis, Vermeidung der Klausel-Spinne, konsolidierter Verweisapparat.

# Verweis- und Querverweis-Technik

## Zweck

Verweise machen einen Vertrag oder Schriftsatz lesbar oder zerstoeren ihn. Wer "im Sinne der vorstehenden Klausel" schreibt, hat keine Klausel benannt. Wer "Anlage 7" referenziert, ohne sie zu definieren, schafft eine Klausel-Spinne, die kein Reviewer mehr entwirrt.

Dieser Skill liefert die Verweistechnik: interne Verweise auf Klauseln und Anlagen, externe Verweise auf Gesetze, Verordnungen und Urteile. Er zeigt die Anlagenverwaltung mit dem Drei-Punkte-Prinzip: einmal benannt, einmal definiert, einmal eingeführt. Es geht um saubere juristische Verweislogik, nicht um Word-Makros, VBA oder Office-Automatisierung.

## Eingaben

- Vertrag oder Schriftsatz mit Verweisstruktur
- Anlagenliste
- Verwendete Gesetze und Verordnungen
- Optional: Versionsstand zur Konsistenzpruefung

## Rechtlicher und methodischer Rahmen

- § 305 Abs. 2 BGB: Einbeziehung von AGB. Verweis auf AGB muss klar und auffindbar sein.
- §§ 133, 157 BGB: Auslegung. Defekte Verweise werden gegen den Verwender ausgelegt (§ 305c Abs. 2 BGB).
- Zitierweise nach `references/zitierweise.md` fuer externe Verweise auf Rechtsprechung und Literatur.
- Technische Umsetzung: Wenn Word genutzt wird, reichen normale Querverweise oder eine bewusste manuelle Endkontrolle. Keine Makros, kein VBA, keine Automatisierungslogik.

## Ablauf / Checkliste

1. **Interne Verweise inventarisieren.** Welche Klauseln verweisen aufeinander?
2. **Anlagen inventarisieren.** Welche Anlagen werden zitiert? Sind sie alle vorhanden?
3. **Externe Verweise pruefen.** Sind Gesetzesangaben aktuell? Sind Rspr.-Zitate verifiziert?
4. **Verweisform pruefen.** Klauselnummer und Klauselueberschrift nennen ("§ 7 Abs. 2 (Haftung)").
5. **Verweise nach Renumbering kontrollieren.** Keine toten Verweise nach Verschiebung von Klauseln oder Anlagen.
6. **Konsistenzpruefung.** Volltextsuche nach "siehe oben", "vorstehend", "nachstehend".
7. **Anlagenverzeichnis erstellen.** Anlage 1 bis Anlage n.

### Interne Verweise: Drei Regeln

1. **Klauselnummer plus Ueberschrift.** "§ 7 Abs. 2 (Haftung)" statt "vorstehender Absatz".
2. **Richtung explizit.** "siehe § 5" oder "wie in § 5 geregelt", nicht "siehe oben".
3. **Voll qualifiziert.** "Anlage 3 (Leistungsbeschreibung)", nicht "Anlage".

### Externe Verweise: Zitiermuster

- Gesetz: "§ 433 Abs. 1 Satz 1 BGB"
- EU-Recht: "Art. 6 Abs. 1 lit. f DSGVO"
- Rspr.: "BGH, Urt. v. TT.MM.JJJJ - Az. ..., [freie Quelle] Rn. ..."
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

- **Tote Verweise nach Renumbering.** Klauselnummern wurden verschoben, aber die Verweise im Text nicht nachgezogen.
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

- `dokumentarchitektur-vertrag-und-schriftsatz`
- `definitionen-klauseln-stringent`
- `word-dokument-finish-und-layout`
- `drafting-prinzipien-klarheit-bestimmtheit-praezision`

## Quellen (Stand 05/2026)

- § 305 Abs. 2 BGB, § 305c Abs. 2 BGB, §§ 133, 157 BGB. gesetze-im-internet.de.
- `references/zitierweise.md` fuer externe Verweise.
- Normale Word-Querverweise können helfen; Makros, VBA und Office-Automatisierung sind für diesen Skill bewusst ausgeschlossen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `word-dokument-finish-und-layout`

**Fokus:** Finalisiert juristische Word-Dokumente vor Versand. Prüft Formatvorlagen, Nummerierung, Inhaltsverzeichnis, Querverweise, Anlagen, Track Changes, Kommentare, Metadaten, PDF/beA-Tauglichkeit, Unterschriftenblock, Tabellen, Seitenumbrüche und optische Konsistenz. Liefert eine Versand-Checkliste und konkrete Reparaturanweisungen.

# Word-Dokument Finish und Layout

## Zweck

Dieser Skill ist die letzte Werkbank vor Versand. Er behandelt das Dokument als echtes Kanzlei-Artefakt: Es muss nicht nur rechtlich stimmen, sondern in Word sauber, stabil und versandfähig sein.

## Prüfblöcke

| Block | Prüffrage |
|---|---|
| Formatvorlagen | Sind Überschriften, Standardtext, Zitate, Definitionen und Anlagen über Styles gebaut? |
| Nummerierung | Läuft die Nummerierung stabil und ohne manuelle Brüche? |
| Querverweise | Sind Verweise als Felder oder wenigstens konsistent aktualisiert? |
| Inhaltsverzeichnis | Ist es vorhanden und aktualisiert, wenn das Dokument länger ist? |
| Track Changes | Ist klar, ob Markup sichtbar versendet wird oder eine Clean Version? |
| Kommentare | Sind interne Kommentare entfernt oder bewusst sichtbar? |
| Metadaten | Sind Autor, Pfade, Vorversionen und versteckte Inhalte geprüft? |
| Anlagen | Stimmen Anlagenbezeichnung, Anlagenverzeichnis und Textverweise überein? |
| Versandform | Word, PDF, PDF/A, beA, E-Mail oder Signing-Plattform? |

## Ablauf

1. Dokumenttyp und Versandweg bestimmen.
2. Word-Hygiene prüfen: Formatvorlagen, Nummerierung, Tabellen, Seitenumbrüche.
3. Juristische Versandhygiene prüfen: Anlagen, Vollmacht, Signaturblock, Fristen.
4. Markup-Status prüfen: Clean, Redline, Vergleichsdokument oder kommentierte Fassung.
5. Metadaten- und Vertraulichkeitscheck durchführen.
6. Versandfassung benennen.

## Dateinamenskonvention

Empfohlen:

```text
2026-05-30_Mandant_Gegner_Dokumenttyp_v03_clean.docx
2026-05-30_Mandant_Gegner_Dokumenttyp_v03_redline.docx
2026-05-30_Mandant_Gegner_Dokumenttyp_v03_signed.pdf
```

## Versand-Checkliste

- Felder aktualisiert.
- Inhaltsverzeichnis aktualisiert.
- Keine leeren Überschriften.
- Keine sichtbaren Platzhalter.
- Keine versehentlichen Kommentare.
- Markup-Status bewusst gewählt.
- Metadaten geprüft.
- Anlagen vollständig.
- Signaturblock korrekt.
- PDF geöffnet und visuell geprüft.

## Output

- Ampel pro Prüfblock.
- Reparaturliste in Reihenfolge der Dringlichkeit.
- Versand-Checkliste.
- Optional: kurze manuelle Reparaturanweisung für die Versandfassung.

## Querverweise

- `revisions-prozess-redlines-comparison`
- `finaler-writing-quality-gate`
- `verweis-und-querverweis-technik`


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
