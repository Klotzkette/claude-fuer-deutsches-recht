---
name: akzg-zeitstrahl-anlagenverzeichnis-extrakt
description: "Akzg Zeitstrahl Anlagenverzeichnis Extrakt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Akzg Zeitstrahl Anlagenverzeichnis Extrakt

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Akzg Zeitstrahl Anlagenverzeichnis Extrakt** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `akzg-zeitstrahl-checkliste` | Checkliste Zeitstrahl in Aktenauszug: Eingang Klage, Klageerwiderung, Beweisbeschluss, mundliche Verhandlung, Urteil. Pruefraster fuer Rechtsmittelinstanz. |
| `anlagenverzeichnis-extrakt` | Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der Akte und will Anlagenverzeichnis erstellen. Anlagenbezeichnung Kurzbeschreibung Schriftsatz Blattangabe je Partei. Normen §§ 130 131 ZPO Schriftsatz-Anlagen. Prüfraster Vollständigkeit Fundstellen-Praezision Parteizuordnung. Output vollständiges Anlagenverzeichnis je Partei. Abgrenzung zu aktenauszug-erstellen (Gesamtauszug) und beweismittel-gegenüberstellung (Beweisuebersicht). |
| `anwaltsschriftsatz-stilrichtlinie` | Stilrichtlinie für den juristisch sauberen neutralen und für Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklatur Abkuerzungskonventionen Tabellengestaltung und Markdown-Formatierung. Verbindliche Stilregeln für alle Bausteine des Aktenauszugs. Massstab §§ 130 131 ZPO. |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Akzg Zeitstrahl Anlagenverzeichnis Extrakt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `akzg-zeitstrahl-checkliste`

**Fokus:** Checkliste Zeitstrahl in Aktenauszug: Eingang Klage, Klageerwiderung, Beweisbeschluss, mundliche Verhandlung, Urteil. Pruefraster fuer Rechtsmittelinstanz.

# AkzG: Zeitstrahl-Checkliste

## Spezialwissen: AkzG: Zeitstrahl-Checkliste
- **Spezialgegenstand:** AkzG: Zeitstrahl-Checkliste / akzg zeitstrahl checkliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AkzG.
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

## 2. `anlagenverzeichnis-extrakt`

**Fokus:** Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der Akte und will Anlagenverzeichnis erstellen. Anlagenbezeichnung Kurzbeschreibung Schriftsatz Blattangabe je Partei. Normen §§ 130 131 ZPO Schriftsatz-Anlagen. Prüfraster Vollständigkeit Fundstellen-Praezision Parteizuordnung. Output vollständiges Anlagenverzeichnis je Partei. Abgrenzung zu aktenauszug-erstellen (Gesamtauszug) und beweismittel-gegenüberstellung (Beweisuebersicht).

# Anlagenverzeichnis-Extrakt

## Zweck

Umfangreiche Gerichtsakten enthalten oft Hunderte von Anlagen, die über verschiedene Schriftsätze verteilt sind. Dieser Skill erstellt ein geordnetes Anlagenverzeichnis, das alle Anlagen mit Bezeichnung, Inhalt und Fundstelle erfasst.

## Triage — kläre vor Erstellung

1. Liegt ein vollständiges Inhaltsverzeichnis der Akte vor?
2. Sind alle Schriftsätze in der Akte? Welche fehlen?
3. Besteht Streit über Übergabe oder Vollständigkeit bestimmter Anlagen?
4. Ist ein Anlageregister fuer Gericht oder fuer Mandant gedacht?

## Zentrale Normen

- § 130 Nr. 5 ZPO — Inhalt des Schriftsatzes: Anlagen müssen bezeichnet werden
- § 131 ZPO — Bezugnahme auf beigefügte Schriftstücke als Anlagen; Verlesen bei Bedarf
- § 141 ZPO — Persönliches Erscheinen; Vorlage von Unterlagen durch Partei
- § 142 ZPO — Anordnung der Urkundenvorlage durch Gericht (richterliche Vorlageanordnung)
- § 422 ZPO — Vorlegungspflicht für Urkunden (Parteibesitz)
- § 432 ZPO — Anforderung von Urkunden durch das Gericht bei Behörden

## Rechtsprechung zu Anlagen und Schriftsatz-Bezugnahmen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anlagenbezeichnungen

### Klägerseite

- K 1, K 2, K 3 ... (K = Kläger)
- AST 1, AST 2 ... (Antragsteller in Eilverfahren)

### Beklagtenseite

- B 1, B 2, B 3 ... (B = Beklagter)
- AG 1, AG 2 ... (Antragsgegner in Eilverfahren)

### Sonstige

- GA 1, GA 2 ... (Gericht, z. B. Sachverständigengutachten)
- SV 1, SV 2 ... (Sachverständiger)

## Tabellenstruktur

```markdown
| Anlage | Inhalt (kurz) | Datum des Dokuments | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag vom TT.MM.JJJJ | TT.MM.JJJJ | Klageschrift | 12-18 |
| K 2 | Abnahmeprotokoll | TT.MM.JJJJ | Klageschrift | 19-21 |
| K 3 | Mängelrüge (Schreiben) | TT.MM.JJJJ | Klageschrift | 22 |
```

## Schritt-für-Schritt-Workflow

1. **Jeden Schriftsatz** auf Anlagenverweise (K 1, B 1 etc.) durchsuchen
2. **Anlage mit Inhalt und Datum** erfassen; Originalbezeichnung übernehmen
3. **Schriftsatz und Blattangabe** notieren
4. **Alle Anlagen** nach Partei getrennt tabellarisch listen
5. **Lücken prüfen** — fehlende Nummern als [nicht in vorliegender Akte] markieren
6. **Doppelreferenzen** prüfen — gleiche Anlage in mehreren Schriftsätzen vermerken
7. **Vorlageanordnung prüfen** — falls § 142 ZPO-Beschluss in Akte: erfasste Anlagen abgleichen

## Entscheidungsbaum — Anlage fehlt in Akte

```
Anlage ist im Schriftsatz bezeichnet aber fehlt körperlich in Akte?
 → Handelt es sich um beweiserhebliche Urkunde? (§ 422 ZPO)
 → Ja: Schriftsatz an Gericht: Vorlage anfordern; Eintrag: [angefordert TT.MM.JJJJ]
 → Nein: Vermerk: [nicht in vorliegender Akte]
 → War Anlage Gegenstand einer Vorlageanordnung (§ 142 ZPO)?
 → Ja: Nachverfolgung ob Vorlage erfolgt — ggf. Antrag auf Ungehorsamssanktion
```

## Beispiel (vollständig)

### Klägeranlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag | 15.03.2021 | Klageschrift 08.02.2023 | 12-18 |
| K 2 | Abnahmeprotokoll | 02.09.2021 | Klageschrift 08.02.2023 | 19-21 |
| K 3 | Mängelrüge | 14.10.2021 | Klageschrift 08.02.2023 | 22 |
| K 4 | Nachbesserungsprotokoll | 08.11.2021 | Klageschrift 08.02.2023 | 23-24 |
| K 5 | Rücktrittsandrohung | 03.01.2022 | Klageschrift 08.02.2023 | 25 |
| K 6 | Rücktrittserklärung | 15.02.2022 | Klageschrift 08.02.2023 | 26 |

### Beklagtenanlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| B 1 | E-Mail-Korrespondenz | versch. | Klageerwiderung 14.04.2023 | 40-44 |
| B 2 | Wartungsprotokoll | 05.09.2021 | Klageerwiderung 14.04.2023 | 45-47 |

## Qualitätscheck

- [ ] Alle Anlagenbezeichnungen aus allen Schriftsätzen erfasst?
- [ ] Lücken in der Nummerierung als fehlend markiert?
- [ ] Inhalt kurz aber aussagekräftig beschrieben?
- [ ] Fundstelle (Schriftsatz und Blatt) angegeben?
- [ ] Vorlageanordnungen nach § 142 ZPO berücksichtigt?

<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 396/18 (claimed: Fehlende Anlage kann nachgereicht werden, NJW 2020, 404): WRONG_TOPIC. Urteil existiert (dejure.org/2019,38295), behandelt aber Kfz-Unfall Beilackierungskosten/§287 ZPO Schaetzungsermessen, NJW 2020, 236. Kein Bezug zu ZPO-Anlagenrecht. Eintrag geloescht. -->

## 3. `anwaltsschriftsatz-stilrichtlinie`

**Fokus:** Stilrichtlinie für den juristisch sauberen neutralen und für Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklatur Abkuerzungskonventionen Tabellengestaltung und Markdown-Formatierung. Verbindliche Stilregeln für alle Bausteine des Aktenauszugs. Massstab §§ 130 131 ZPO.

# Anwaltsschriftsatz-Stilrichtlinie

## Zweck

Diese Stilrichtlinie legt verbindliche Regeln für Sprache, Gliederung und Formatierung des Aktenauszugs fest. Sie sichert, dass der Aktenauszug dem professionellen Standard entspricht, den Rechtsanwältinnen und Rechtsanwälte in ihrer täglichen Arbeit erwarten.

## Normhintergrund — Schriftsatz-Anforderungen

- § 130 ZPO — Pflichtinhalt anwaltlicher Schriftsätze (Bezeichnung der Partei, Antraege, Tatsachen, Beweismittel)
- § 131 ZPO — Beizufügende Schriftstücke und Anlagen
- § 253 Abs. 2 ZPO — Klageschrift: bestimmter Antrag, Sachverhalt, Benennung Gericht
- § 520 Abs. 3 ZPO — Berufungsbegründung: Bezeichnung der Angriffspunkte, neues Vorbringen
- § 551 Abs. 3 ZPO — Revisionsbegründung: Angabe der Revisionsgründe

## Rechtsprechung zum Schriftsatzstil und Schriftsatz-Anforderungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Sprache

### Allgemeine Grundsätze

- **Sachlich und präzise:** Jeder Satz transportiert eine Information. Füllphrasen vermeiden.
- **Juristisch korrekt:** Rechtsbegriffe werden in ihrer gesetzlichen oder gefestigten dogmatischen Bedeutung verwendet.
- **Neutral:** Keine Wertungen, keine Erfolgsprognosen (→ Skill `neutralitaetspruefung`).
- **Aktiv bevorzugen:** "Die Klägerin macht geltend" — nicht "Es wird geltend gemacht".

### Verbotene Begriffe

Keine Begriffe aus dem Bereich kommerzieller Textverarbeitungssoftware oder Assistenzsysteme. Keine Formulierungen wie "basierend auf meiner Analyse" oder "nach meiner Einschätzung". Keine Ich-Form.

### Parteibezeichnungen

- Konsistente Verwendung im gesamten Aktenauszug
- Zulässig: vollständiger Name, Kurzname, Parteibezeichnung (die Klägerin)
- Nicht mischen: nicht "Klägerin" in einem Abschnitt und "Frau Müller" im nächsten
- Abkürzungen (Kl., Bekl.) nur in Tabellen, nicht in Fließtext

### Normen und Paragraphen

- Vollständige Angabe bei erster Nennung: § 634 Nr. 4 i.V.m. § 280 Abs. 1 BGB
- Abkürzung bei Wiederholung möglich: § 634a Abs. 1 Nr. 1 BGB (Verjährung)
- Gesetze stets mit Kurzbezeichnung: BGB, ZPO, StPO, VwGO, ArbGG, SGG, KSchG, GKG

## Gliederung

### Überschriften-Hierarchie

```
# Aktenauszug — [Aktenzeichen] (H1 — nur einmal)
## Verfahrensidentifikation (H2 — Bausteine)
### Parteien (H3 — Unterabschnitte)
#### Klägerseite (H4 — bei Bedarf)
```

### Abschnittstrennungen

Jeder Baustein beginnt auf einer neuen Hierarchieebene. Zwischen Bausteinen eine Leerzeile.

## Tabellen

### Formatierung

- Markdown-Tabellen mit Pipes und Trennzeile
- Spaltenbreite nicht fixieren (Markdown passt sich an)
- Spaltenköpfe fett oder als Header-Zeile

### Tabellenstil

| Gut | Nicht gut |
|---|---|
| Klägerin / Beklagte als Spaltenköpfe | Kl. / Bekl. |
| Kurze präzise Zellinhalte | Lange Fließtextabsätze in Zellen |
| Fundstellen in separater Spalte | Fundstellen ohne Quelle |

## Datumsformat

- Vollständig: TT.MM.JJJJ (z. B. 15.03.2021)
- Kein ISO-Format (2021-03-15) im Aktenauszug-Body
- Monats-/Jahresangaben: März 2021 (nicht 03/2021)

## Beträge

- Immer mit EUR-Präfix: EUR 45.000
- Keine Tausenderpunkte in Zahlen: EUR 45000 oder EUR 45.000 (Punkt als Tausendertrenner ist im Deutschen üblich)
- Keine Abkürzung T€ oder TEUR im Aktenauszug (ausgeschrieben)

## Aktenzeichen

Format: [Gericht-Kürzel] [Senats-/Kammernummer] [Verfahrensart] [Laufnummer]/[Jahr]

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Markdown-Besonderheiten

- Fettdruck (`**Text**`) für Daten in Chronologien
- Kursiv (`*Text*`) sparsam — für Gesetzesbegriffe oder Fremdwörter
- Code-Blöcke (` ``` `) für Musterformulierungen und Vorlagen
- Fristenboxen hervorheben (Tabelle oder Blockquote mit ⚠️)

## Qualitätscheck Stil

- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteibezeichnungen konsistent?
- [ ] Normen vollständig angegeben?
- [ ] Datumsformat einheitlich TT.MM.JJJJ?
- [ ] Beträge mit EUR-Präfix?
- [ ] Überschriften-Hierarchie korrekt?
- [ ] Schriftsatz erfüllt Mindestanforderungen §§ 130-131 ZPO?

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- VII ZR 248/12 (BGH): ersatzlos entfernt (NOT_FOUND auf dejure.org; kein Urteil vom 06.11.2013 nachweisbar)
- VII ZR 126/02 (BGH): ersatzlos entfernt (WRONG_TOPIC: tatsaechliches Thema ist Werkvertragsrecht/Verputzungsfehler/§ 421 BGB, nicht Prozessrecht; Quelle: https://dejure.org/2003,299)
- Aktenzeichen-Formatbeispiele sind frei erfunden und duerfen nicht als Rechtsprechungszitate verwendet werden.
