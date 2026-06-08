---
name: verweis-querverweis-dokument-finish
description: "Verweis- und Querverweistechnik in juristischen Dokumenten. Interne Verweise auf Klauseln und Anlagen, externe Verweise auf Gesetze und Urteile. Anlagenverwaltung: jede Anlage einmal benannt, einmal definiert, einmal eingeführt. Vorstehender vs. nachstehender Verweis, Vermeidung der Klausel-Spinne, konsolidierter Verweisapparat im Word Legal Ai Plugin And Skill For German Lawyers: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Verweis- und Querverweis-Technik

## Arbeitsbereich

Verweis- und Querverweistechnik in juristischen Dokumenten. Interne Verweise auf Klauseln und Anlagen, externe Verweise auf Gesetze und Urteile. Anlagenverwaltung: jede Anlage einmal benannt, einmal definiert, einmal eingeführt. Vorstehender vs. nachstehender Verweis, Vermeidung der Klausel-Spinne, konsolidierter Verweisapparat. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
- Zitierweise nach `references/zitierweise.md` für externe Verweise auf Rechtsprechung und Literatur.
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
(2) Die Haftung für Geheimhaltungsverstoesse richtet sich nach § 8
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
- `references/zitierweise.md` für externe Verweise.
- Normale Word-Querverweise können helfen; Makros, VBA und Office-Automatisierung sind für diesen Skill bewusst ausgeschlossen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
