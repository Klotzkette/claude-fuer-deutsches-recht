---
name: kig-konformitaetsbewertung-risikobewertung
description: "KIG Konformitaetsbewertung Risikobewertung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KIG Konformitaetsbewertung Risikobewertung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **KIG Konformitaetsbewertung Risikobewertung** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kig-konformitaetsbewertung-spezial` | Spezialfall Konformitaetsbewertungsverfahren Hochrisiko-KI Art. 43 AI Act: interne Kontrolle, benannte Stelle, EU-Konformitaetserklaerung, CE-Kennzeichnung. Pruefraster fuer Anbieter. |
| `kig-risikobewertung-hochrisiko-leitfaden` | Leitfaden Risikobewertung Hochrisiko-KI Anhang III AI Act: Bereiche Bildung / Beschaeftigung / Kreditscoring / Migration. Pruefraster fuer Klassifizierung und Ausnahme. |
| `regulierungs-luecken-analyse` | Gleicht eine neue KI-Regulierung oder Behördenleitlinie mit der aktuellen Governance-Position ab — identifiziert Lücken, Prioritäten und einen Maßnahmenplan mit Verantwortlichen und Fristen. Lädt, wenn der Nutzer "Lückenanalyse AI Act", "gilt der AI Act für uns", "Compliance-Prüfung KI", "neue KI-Verordnung prüfen" oder Regelungstext eingibt. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **KIG Konformitaetsbewertung Risikobewertung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kig-konformitaetsbewertung-spezial`

**Fokus:** Spezialfall Konformitaetsbewertungsverfahren Hochrisiko-KI Art. 43 AI Act: interne Kontrolle, benannte Stelle, EU-Konformitaetserklaerung, CE-Kennzeichnung. Pruefraster fuer Anbieter.

# KIG: Konformitaetsbewertung

## Spezialwissen: KIG: Konformitaetsbewertung
- **Spezialgegenstand:** KIG: Konformitaetsbewertung / kig konformitaetsbewertung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, Art. 43, AI, EU, CE, KIG, BGH.
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

## 2. `kig-risikobewertung-hochrisiko-leitfaden`

**Fokus:** Leitfaden Risikobewertung Hochrisiko-KI Anhang III AI Act: Bereiche Bildung / Beschaeftigung / Kreditscoring / Migration. Pruefraster fuer Klassifizierung und Ausnahme.

# KIG: Risikobewertung Hochrisiko

## Spezialwissen: KIG: Risikobewertung Hochrisiko
- **Spezialgegenstand:** KIG: Risikobewertung Hochrisiko / kig risikobewertung hochrisiko leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, III, AI, KIG.
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

## 3. `regulierungs-luecken-analyse`

**Fokus:** Gleicht eine neue KI-Regulierung oder Behördenleitlinie mit der aktuellen Governance-Position ab — identifiziert Lücken, Prioritäten und einen Maßnahmenplan mit Verantwortlichen und Fristen. Lädt, wenn der Nutzer "Lückenanalyse AI Act", "gilt der AI Act für uns", "Compliance-Prüfung KI", "neue KI-Verordnung prüfen" oder Regelungstext eingibt.

# KI-Regulierungs-Lückenanalyse

## Zweck

Der AI Act ist seit 01.08.2024 in Kraft — mit gestaffelter Anwendbarkeit.
Die Datenschutzaufsichtsbehörden präzisieren DSGVO Art. 22. Die neue
Produkthaftungs-RL (RL 2024/2853) erfasst KI-Systeme. Etwas bewegt sich —
und nun muss bekannt sein, was sich, wenn überhaupt, ändern muss.

Dieser Skill gleicht neue Anforderungen mit der aktuellen KI-Governance
ab (gem. `CLAUDE.md`) und produziert eine priorisierte Lückenliste mit
Maßnahmenplan. Wo Regelungstext tatsächlich mehrdeutig ist: klar sagen,
konservative Lesart nennen, bei Materialität externe Beratung empfehlen.

## Eingaben

- Regulierungs-Name oder Regelungstext (AI Act Hochrisiko, DSGVO Art. 22,
 DSA, DMA, RL 2024/2853, BSIG, Sektoren)
- Praxisprofil aus `CLAUDE.md` (regulatorischer Fußabdruck, Anwendungsfall-
 Register, KI-Richtlinien-Verpflichtungen, Anbieter-Positionen,
 Folgenabschätzungspraxis)

## Rechtlicher Rahmen

**Kernvorschriften (Referenzrahmen)**

- **AI Act (VO (EU) 2024/1689)**: Gestaffelte Anwendbarkeit: Art. 5 (verbotene
 Praktiken) ab 02.02.2025; Art. 53 ff. (Allgemeinzweck-KI) ab 02.08.2025;
 Hochrisiko-Pflichten Art. 9–15 (Anbieter), Art. 26/29 (Betreiber) ab
 02.08.2026. Hochrisiko: Art. 6 i.V.m. Anhang III. Bußgeld: Art. 99 bis
 35 Mio. € oder 7 % weltweiter Jahresumsatz bei Art. 5-Verstößen.
- **DSGVO Art. 22**: Automatisierte Einzelentscheidungen; Rechtsgrundlagen
 Art. 22 Abs. 2 lit. a–c.
- **DSA Art. 27, 38 (VO (EU) 2022/2065)**: Transparenz für Empfehlungs-
 systeme sehr großer Plattformen.
- **DMA Art. 6 (VO (EU) 2022/1925)**: KI-bezogene Pflichten für Torwächter.
- **Produkthaftungs-RL 2024/2853/EU** (ersetzt RL 85/374/EWG): KI-Systeme
 als Produkte; Beweislasterleichterungen.
- **GeschGehG, UrhG § 44b**: Trainingsdaten-Schutz; Text-und-Data-Mining.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kommentare**

- Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Rn. 5 (Hochrisiko-Klassifikation; Anhang-III-Kategorien).
- Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 115 ff.
 (regulatorische Lücken im KI-Recht).
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 110 (Compliance-Anforderungen AI Act).
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 20

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Regulierung abgrenzen**

Bevor Lücken analysiert werden: Anwendbar? Jurisdiktion, Schwellenwert,
Sektor-Ausnahmen, Anbieter-/Betreiber-Unterscheidung (Art. 3 KI-VO).
Wann? Inkrafttreten; Durchsetzungsdatum; Phase-in-Fristen.
Was ist tatsächlich neu? Delta zum Status quo ermitteln, nicht Volltext
wiedergeben.
→ Bei eindeutiger Nichtanwendbarkeit: "Nicht anwendbar. Begründung: [Grund].
Kein Handlungsbedarf."

**Schritt 2 — Anforderungen extrahieren**

Jede substanzielle Anforderung auflisten:

| Nr. | Anforderung | Fundstelle | Kategorie |
|---|---|---|---|

Kategorien: Transparenz / Folgenabschätzung / Menschliche Aufsicht /
Genauigkeit+Prüfung / Governance / Vertrags-Weitergabepflichten /
Verbotene Praktiken / Betroffenenrechte.

**Schritt 3 — Abgleich mit dem Ist-Zustand**

Für jede Anforderung (Kurzformat):

```
### [Nr.]: [Kurzbezeichnung]
Verordnung verlangt: [Anforderung]
Unser Ist-Zustand: [aus CLAUDE.md]
Lücke: [Keine | Teilweise | Vollständig]
Was fehlt: [konkret]
Aufwand: [Richtlinienänderung | Prozess | System | Folgenabschätzung |
 Anbieter-Nachverhandlung | Registrierung]
Risiko: [Bußgeldrahmen; Durchsetzungswahrscheinlichkeit]
```

**Schritt 4 — Priorisieren**

1. Harte Frist + Sanktionen (Art. 99 KI-VO; Art. 83 DSGVO)
2. Verbotene Praktiken (Art. 5 KI-VO): erste Priorität unabhängig
 vom Durchsetzungsdatum
3. Aufwand-Wirkung-Verhältnis
4. Anwendungsfall-Überschneidung

**Schritt 5 — Maßnahmenplan**

```markdown
## Maßnahmenplan: [Regulierungsname]
Anwendungsdatum: [Datum] | Betrifft uns als: [Anbieter/Betreiber/beides]

### Muss-Maßnahmen vor Durchsetzungsbeginn
| Lücke | Maßnahme | Verantwortlich | Frist | Status |

### Soll-Maßnahmen
[gleiche Tabelle]

### Bereits compliant [Liste]
### Akzeptierte Lücken [mit Begründung und Akzeptant]
```

## Ausgabeformat

Datiertes Markdown-Dokument; Maßnahmenplan-Tabelle wird zum Tracker.
Auch bei "keine Lücken" dokumentieren — nützlicher Compliance-Nachweis.

**Quellen-Tagging:**
- `[gesichert]` — stabile Normen (z. B. DSGVO Art. 22, VO (EU) 2024/1689).
- `[prüfen]` — Durchführungsrechtsakte, Leitlinien, Schwellenwerte.
- **Pinpoint-Pflicht** — konkrete Artikelnummern, Anhang-Referenzen und Erwägungsgründe immer gegen die Primärquelle (ABl./EUR-Lex, amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang) verifizieren. AI-Act-Artikelnummern haben sich während der Konsolidierung verschoben; im Output keine ungeprüften Pinpoint-Tags stehen lassen.

## Beispiel

**Anfrage:** "Gilt der AI Act für unsere interne Bewerbungs-Screening-KI?"

**Ablauf:** Betreiberrolle; Hochrisiko nach Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO, wenn das System zweckbestimmt für Auswahl, Filterung oder Bewertung von Bewerbungen eingesetzt wird. Betreiber-Pflichten aus Art. 26 KI-VO und ggf. Grundrechte-Folgenabschätzung nach Art. 27 KI-VO; bei eigener Anbieterrolle zusätzlich Anbieterpflichten, insbesondere Risikomanagement nach Art. 9 KI-VO. Maßnahme: Rollen sauber trennen, Human-in-the-Loop dokumentieren, Betriebsrat einbeziehen und Umsetzungsfrist im Maßnahmenplan führen.

## Risiken und typische Fehler

- Mehrdeutigkeit übergehen: bei echten Auslegungsfragen konservative Lesart
 nennen, nicht überdecken.
- Maßnahmen nicht implementieren: dieser Skill plant nur.
- Sektorspezifische Expertise nicht ersetzen (Medizinprodukte MDR/IVDR,
 Finanzdienstleistungen MaRisk-KI).

## Quellenpflicht

- **AI Act Art. 5, Art. 6 i.V.m. Anhang III, Art. 9–15, Art. 26/29, Art. 99.**
- **DSGVO Art. 22** bei automatisierten Entscheidungsverfahren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **RL 2024/2853/EU** (Produkthaftung) bei Haftungslücken.
- **DSGVO Art. 35** bei Folgenabschätzungspflicht.
- **Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Rn. 5.**
- **Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 115.**

## Triage zu Beginn
1. Welches Regulierungsregime ist Gegenstand — KI-VO, DSGVO Art. 22, DSA, DMA, ProdHaft-RL?
2. Ist das Regime bereits in Kraft oder nur angekuendigt — welches Anwendungsdatum?
3. Betrifft das Regime die Rolle als Anbieter oder Betreiber (Art. 3 KI-VO-Unterscheidung)?
4. Welche Anwendungsfaelle aus dem Register sind potenziell lueckenhaft?
5. Gibt es bereits Massnahmen oder laufende Compliance-Projekte — Delta zum Status quo ermitteln?

## Output-Template — Lueckenanalyse KI-Regulierung
**Adressat:** Compliance- / Rechts-Team — Tonfall: sachlich, priorisiert
```
LUECKENANALYSE KI-REGULIERUNG
[DATUM] — Regime: [REGULIERUNGSNAME] — Anwendungsbereich: [JA/NEIN/TEILWEISE]

ANWENDBARES REGIME: [BEGRUENDUNG IN 1-2 SAETZEN]
Inkrafttreten: [DATUM] — Durchsetzung ab: [DATUM]

LUECKENTABELLE:
| Nr. | Anforderung | Fundstelle | Status | Luecke | Prioritaet | Verantwortlicher | Frist |
|---|---|---|---|---|---|---|---|
| 1 | [ANFORDERUNG] | Art. X KI-VO | [BESTEHT/FEHLT/LUECKE] | [BESCHREIBUNG] | HOCH/MITTEL/NIEDRIG | [PERSON] | [DATUM] |

GESAMTBEWERTUNG: [N] kritische Luecken / [N] material / [N] gering

NICHT-ANWENDBAR-POSTEN:
- [ANFORDERUNG]: nicht anwendbar wegen [BEGRUENDUNG]

NAECHSTE SCHRITTE:
1. [MASSNAHME — Verantwortlicher: NAME — bis: DATUM]

Erstellt: [NAME], [DATUM]
```
