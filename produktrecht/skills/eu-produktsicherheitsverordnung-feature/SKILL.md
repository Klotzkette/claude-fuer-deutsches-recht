---
name: eu-produktsicherheitsverordnung-feature
description: "EU Produktsicherheitsverordnung Feature: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# EU Produktsicherheitsverordnung Feature

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **EU Produktsicherheitsverordnung Feature** im Plugin Produktrecht (ProdSG/GPSR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `eu-produktsicherheitsverordnung-gpsr` | EU-Produktsicherheitsverordnung GPSR (VO (EU) 2023/988) in der Praxis: Geltung seit 13.12.2024, Pflichten fuer Hersteller, Importeure, Haendler und Online-Marktplaetze, Rueckverfolgbarkeit, Unfallmeldungen und Safety Business Gateway. |
| `feature-risikobewertung` | Tiefgehende Risikobewertung für ein einzelnes Feature oder einen Produktbereich wenn der Launch-Review etwas gefunden hat das mehr als eine Tabellenzeile braucht. Strukturierte Analyse: was könnte schiefgehen, wie wahrscheinlich, wie schlimm, was mildert es. Verwenden wenn der Nutzer sagt "tiefer Einblick in dieses Risiko", "Risikobewertung für [Feature]", "was könnte schiefgehen mit", oder wenn launch-prüfung eine neuartige Frage flaggt. Besonders einschlägig bei: UWG-Verstoßrisiken, DSGVO-Verletzung, DSA-Pflichten, KI-VO-Anforderungen, Verbraucherschutz nach BGB. |
| `impressum-pflicht` | Prüft die Impressumspflicht für Websites, Apps und Social-Media-Profile nach §§ 5 und 6 DDG und § 18 MStV, erstellt konforme Impressumstexte und identifiziert typische Abmahnrisiken nach UWG. Lädt bei Fragen zu Anbieterkennzeichnung, Impressum-Vollständigkeit und Bußgeldrisiken. |

## Arbeitsweg

Im Plugin Produktrecht (ProdSG/GPSR) gilt für **EU Produktsicherheitsverordnung Feature**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `eu-produktsicherheitsverordnung-gpsr`

**Fokus:** EU-Produktsicherheitsverordnung GPSR (VO (EU) 2023/988) in der Praxis: Geltung seit 13.12.2024, Pflichten fuer Hersteller, Importeure, Haendler und Online-Marktplaetze, Rueckverfolgbarkeit, Unfallmeldungen und Safety Business Gateway.

# GPSR in der Praxis

## Spezialwissen: GPSR in der Praxis
- **Spezialgegenstand:** GPSR in der Praxis / eu produktsicherheitsverordnung gpsr. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, GPSR, VO.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `feature-risikobewertung`

**Fokus:** Tiefgehende Risikobewertung für ein einzelnes Feature oder einen Produktbereich wenn der Launch-Review etwas gefunden hat das mehr als eine Tabellenzeile braucht. Strukturierte Analyse: was könnte schiefgehen, wie wahrscheinlich, wie schlimm, was mildert es. Verwenden wenn der Nutzer sagt "tiefer Einblick in dieses Risiko", "Risikobewertung für [Feature]", "was könnte schiefgehen mit", oder wenn launch-prüfung eine neuartige Frage flaggt. Besonders einschlägig bei: UWG-Verstoßrisiken, DSGVO-Verletzung, DSA-Pflichten, KI-VO-Anforderungen, Verbraucherschutz nach BGB.

# Feature-Risikobewertung

## Mandat-Kontext

**Mandat-Kontext.** `## Mandate-Workspaces` in der praxisseitigen CLAUDE.md prüfen. Wenn `Aktiviert` `✗` ist (Standard für In-House-Nutzer), diesen Absatz überspringen. Wenn aktiviert und kein aktives Mandat, fragen: "Für welches Mandat ist das? `/produktrecht:produktrecht-mandat-arbeitsbereich switch <kürzel>` ausführen oder 'Praxisebene' sagen." Das aktive `mandat.md` für mandatsspezifischen Kontext laden. Ausgaben in den Mandat-Ordner schreiben. Niemals Dateien eines anderen Mandats lesen außer `Mandats-übergreifender Kontext` ist `ein`.

---

## Zweck

Der Launch-Review ist breit. Dies ist tief. Wenn eine einzelne Frage mehr als eine Tabellenzeile braucht – ein neuartiges KI-Feature, ein Produkt für Minderjährige, etwas das ein Behörde aktiv beobachtet – erstellt dieser Skill eine eigenständige Bewertung.

Nicht jeder Launch braucht eine. Die meisten nicht. Dies ist für die 10% wo "DSFA fertig, geshippt" nicht das richtige Prüfungsniveau ist.

## Eingaben

- Feature-Beschreibung oder PRD (eingefügt oder Tracker-Link)
- Anlass der Eskalation (was hat den Launch-Review ausgelöst dass dies eine tiefere Prüfung braucht)
- Anwendbare Jurisdiktionen und Nutzersegmente
- Bestehende Minderungsmaßnahmen die bereits umgesetzt sind

## Wann dies ausführen

- Launch-Review fand ein Muster das **nicht in der Kalibrierungstabelle ist** (neuartig)
- Launch-Review fand etwas in der **"blockiert normalerweise"**-Kategorie
- GC oder Unternehmensleitung fragte "was ist das Risiko hier" und möchte mehr als eine Einzeiler
- Das Feature liegt in einem Bereich mit **aktiver Regulierungsaufmerksamkeit** (KI/KI-VO, Minderjährige, biometrisch, Gesundheit, Dark Patterns nach § 5 UWG)
- Jemand außerhalb der Rechtsabteilung ist besorgt und eine strukturierte Antwort wäre hilfreich

Wenn keines davon zutrifft, reicht der Launch-Review. Keine Dokumente um der Dokumente willen erstellen.

## Ablauf

### 1. Was wird bewertet

Ein Absatz. Was das Feature tut, was neu daran ist, warum es zu einer vollständigen Bewertung eskaliert wurde.

### 2. Die Risiken

Für jedes einzelne Risiko (2–5, nicht 15):

```markdown
### Risiko [N]: [Kurzname]

**Szenario:** [Was eintreten müsste damit dies schiefgeht. Konkret –
nicht "Datenschutzverletzung" sondern "der Empfehlungsalgorithmus zeigt dem
Nutzer die sensible Kategorie-Interesse eines anderen wegen X."]

**Wer wird geschädigt:** [Nutzer? Das Unternehmen? Ein Dritter? Konkret.]

**Wie wahrscheinlich:** [Gering / Mittel / Hoch – mit Begründung. "Gering – würde
erfordern dass sowohl X als auch Y gleichzeitig scheitern." Nicht nur ein
Bauchgefühl.]

**Wie schlimm wenn es passiert:** [Gering / Mittel / Hoch – mit Begründung.
"Hoch – behördliches Bußgeld (bis 4% Jahresumsatz, Art. 83 DSGVO) + Abmahnwelle
+ Presseschaden" vs. "Gering – eine Verbraucherbeschwerde, kein tatsächlicher
Schaden."]

**Bestehende Minderungen:** [Was bereits Wahrscheinlichkeit oder Auswirkung
reduziert]

**Lücke:** [Was fehlt, falls vorhanden]

**Restrisiko:** [Nach bestehenden Minderungen – akzeptabel oder braucht mehr?]
```

### 3. Regulierungslandschaft (falls relevant)

Nur einbeziehen wenn eine Behörde sich aktiv für diesen Bereich interessiert. Falls ja:

- Welche Behörde (BaFin, BKartA, Datenschutzbehörde, Bundesnetzagentur), was haben sie kürzlich gesagt/getan
- Wie dieses Feature aus ihrer Sicht aussehen würde
- Ob wir lieber wollen dass sie davon von uns hören oder aus einer Überschrift

**Relevante deutsche Behörden und jüngste Prioritäten:**
- **BKartA:** Dark Patterns nach § 19a GWB, Daten-Tying, Marktbeherrschungsmissbrauch digitaler Unternehmen; vgl. Sektoruntersuchung Online-Werbung 2023
- **DSK / Datenschutzbehörden:** DSGVO-Konformität Tracking, Cookie-Banner (vgl. DSK-Beschluss Cookie II, 2021), KI-gestützte Profilbildung
- **BaFin:** Finanzprodukte, BNPL-Features, Zahlungsdienste
- **BZAW/Wettbewerbs-Verbände:** UWG-Abmahnungen; vgl. Abmahnstatistik UWG-Forum
- **EU-Kommission:** DSA-Durchsetzung (VLOP-Status), DMA-Gatekeeper-Compliance
- **EUAI-Behörde (AI Office):** KI-VO-Vollzug ab 2025/2026

### 4. Präzedenz (falls vorhanden)

Hat ein anderes Unternehmen etwas Ähnliches gemacht? Was passierte?

**Relevante Präzedenzfälle im deutschen Produktrecht:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Vorrang nicht überschätzen. Regulierungsbehörden ändern Prioritäten; dass ein Unternehmen damit durchgekommen ist bedeutet nicht dass das nächste es auch tut.

### 5. Optionen

2–3 realistische Wege präsentieren:

```markdown
| Option | Beschreibung | Risikoreduzierung | Kosten |
|---|---|---|---|
| A: Wie geplant shippen | [aktueller Plan] | Keine | Keine |
| B: Mit [Minderung] shippen | [Änderung] | [wie viel] | [Entwicklungsaufwand, Timeline, UX] |
| C: [Komponente] nicht shippen | [Umfangskürzung] | [wie viel] | [Produktauswirkung] |
```

### 6. Empfehlung

Eine wählen. Erklären warum. Anerkennen was abgewogen wird.

```markdown
**Empfohlen: Option [X]**

[Warum. Welches Risiko verbleibt. Warum das akzeptabel ist. Wer es akzeptiert.]

**Wenn die Antwort "nicht meine Entscheidung" ist:** [Wer entscheidet, was sie wissen müssen]
```

## Kalibrierungscheck

Vor der Fertigstellung gegen `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` → Risikokalibrierung prüfen:

- Ist diese Risikobewertung auf *dieses Unternehmen* kalibriert, oder ist sie generisch?
- Ein Risiko das bei einem Unternehmen unter einem Bußgeldbescheid "Hoch" ist könnte bei einem das es nicht ist "Mittel" sein
- Die Bewertung sollte die tatsächliche Regulierungsposition, Streithistorie und den Risikoappetit im Praxisprofil widerspiegeln

## Besondere Prüfrahmen nach Rechtsgebiet

### UWG-Risiko (§§ 3, 5, 5a, 5b, 7 UWG)

Prüfen:
- Könnte das Feature Verbraucher über wesentliche Merkmale irren? (§ 5 UWG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Werden wesentliche Informationen verschwiegen? (§ 5a UWG)
- Werden Verbraucher unzumutbar belästigt? (§ 7 UWG: unerwünschte E-Mail, Telefonwerbung, Push-Nachrichten)
- Vergleichende Werbung: objektiv, kein Anschwärzen, Vergleich wesentlicher Merkmale? (§ 6 UWG)

Leitkommentare: Köhler/Bornkamm/Feddersen UWG, 42. Aufl. 2024, § 5 Rn. 1 ff.; Harte-Bavendamm/Henning-Bodewig UWG, 5. Aufl. 2021.

### DSGVO/TDDDG-Risiko

Prüfen:
- Neue Datenerhebung: Welche Rechtsgrundlage (Art. 6 DSGVO)? Einwilligung oder berechtigtes Interesse?
- Besondere Kategorien (Art. 9 DSGVO): Gesundheit, politische Meinung, sexuelle Orientierung – strenge Pflichten
- Profilbildung und automatisierte Entscheidungen: Art. 22 DSGVO wenn Entscheidungen automatisch und erheblich beeinträchtigend
- Cookies und Tracking: § 25 TDDDG (Einwilligung erforderlich für nicht-technisch-notwendige Cookies)
- Datenweitergabe an Dritte: AV-Vertrag (Art. 28 DSGVO), Drittlandtransfer (Art. 44 ff. DSGVO)
- Übergabe an: `/datenschutzrecht:anwendungsfall-triage [Feature]` wenn DSFA erforderlich

### DSA-Risiko (VO (EU) 2022/2065)

Relevant für Plattformen, Marktplätze, sehr große Online-Plattformen (VLOP):
- Art. 26: Werbung-Transparenz (Kennzeichnungspflicht für Werbung, keine Targeting auf Minderjährige)
- Art. 27: Empfehlungssysteme (transparente Parameter, Opt-out-Option)
- Art. 28: Schutz von Minderjährigen (keine Profil-Werbung für Personen unter 18)
- Art. 17–18: Beschwerde- und Abhilfemechanismen für illegale Inhalte

Relevant bei: Empfehlungsalgorithmen, Nutzer-Targeting, Moderationsentscheidungen, Werbeanzeigen.

### KI-VO-Risiko (VO (EU) 2024/1689)

**Risikoklassifizierung zuerst:**

| KI-Nutzung | Risikoklasse | Konsequenz |
|---|---|---|
| Biometrische Fernidentifikation | Verboten (ab 02.02.2025) | Nicht erlaubt |
| Social Scoring durch Behörden | Verboten | Nicht erlaubt |
| Emotionserkennung am Arbeitsplatz | Hochrisiko | Art. 9–15: DSFA, Register, CE |
| KI in kritischer Infrastruktur | Hochrisiko | Strenges Konformitätsregime |
| KI-Empfehlungssystem (nicht VLOP) | Begrenzt | Art. 50: Transparenzpflichten |
| Generative KI (GPAI) | GPAI-spezifisch | Art. 53: Urheberrechtsschutz, Transparenz |
| KI-Chatbot für Verbraucher | Begrenzt | Art. 50: Kennzeichnung als KI |

**Übergabe an:** `/ki-governance:anwendungsfall-triage [Feature]` wenn KI-Komponente erkannt.

### Verbraucherschutz BGB/BGB §§ 305 ff.

Prüfen:
- AGB-Klauseln: Einbeziehungsanforderungen (§§ 305, 305c BGB), überraschende Klauseln, Inhaltskontrolle (§§ 307–309 BGB)
- Fernabsatz: Widerrufsrecht (§§ 312g, 355 BGB), Widerrufsbelehrung (Muster-Widerrufsformular)
- Verbraucherverträge: wesentliche Informationen (Art. 246a EGBGB), Buttonlösung (§ 312j BGB)
 - **Button-Beschriftung isoliert prüfen** — maßgeblich sind nur die Worte auf dem Button, nicht Kontext oder Begleitumstände (EuGH C-249/21 "Fuhrmann-2"). Verstoß = endgültige Unwirksamkeit (§ 312j Abs. 4 BGB) plus Rückabwicklung nach § 812 BGB; gilt branchenübergreifend, auch für regulierte Bereiche wie Online-Glücksspiel (LG Aachen, Urteil vom 27.05.2026, 10 O 306/25 – "Wette abgeben" unzureichend; Quelle: Pressehinweis Gamesright/rightmart, 28.05.2026, Volltext bei Aufnahme noch nicht veröffentlicht).
- Gewährleistung: § 434 BGB (Produktmangel, Übereinstimmung mit öffentlichen Äußerungen inkl. Werbeaussagen)

## Übergaben

- **An KI-Governance:** Wenn der tiefe Einblick durch ein KI-Feature ausgelöst wurde – `/ki-governance:ki-folgenabschaetzung [Feature]` parallel oder sofort danach ausführen. Die Feature-Risikobewertung rahmt die Entscheidung; die KI-Folgenabschätzung dokumentiert das KI-System spezifisch. Sie sind keine Duplikate.
- **An Datenschutzrecht:** Wenn das Feature neue Datenerhebung oder -verarbeitung beinhaltet, `/datenschutzrecht:dsfa-erstellung [Feature]` ausführen.
- **An KI-Governance-Lieferantenprüfung:** Wenn das Feature einen neuen KI-Anbieter verwendet, `/ki-governance:ki-anbieter-prüfung [Lieferantenvertrag]` ausführen.

## Ausgabeformat

Eigenständiges Dokument, 2–4 Seiten. Arbeitsvermerk aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` `## Ausgaben` voranstellen.

Kein Foliensatz, kein Memo zur Akte – ein Entscheidungsdokument das jemand liest und dann entscheidet.

Speichern wo `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` → Launch-Review-Prozess sagt wohin Review-Dokumente gehen.

## Quellen und Zitierweise

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Pflicht-Beispielzitate für häufige Konstellationen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Köhler, in: Köhler/Bornkamm/Feddersen UWG, 42. Aufl. 2024, § 5 Rn. 1.50 ff.

## Zitierprüfung

Wenn die Bewertung Fälle, Normen, Verordnungen oder Vollzugsmaßnahmen zitiert – insbesondere in der Regulierungslandschaft und Präzedenz-Abschnitten – wurden diese Zitate von einem KI-Modell generiert und wurden nicht gegen eine Primärquelle verifiziert. Vor Verwendung des Entscheidungsdokuments für Entscheidungsträger jeden Verweis gegen amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang oder die BGH-Website auf Richtigkeit, Status als geltendes Recht und aktuellen Vollzugsstand prüfen. Eine Risikobewertung die auf einem erfundenen Bußgeldbescheid aufbaut ist schlimmer als keine Bewertung.

## Risiken / typische Fehler

- **Überprüfung nicht ersetzen.** Diese Bewertung rahmt die Entscheidung – ein autorisierter Mensch wählt eine Option.
- **Kalibrierung vergessen.** Ein generisch "hohes" Risiko kann bei Ihrem Unternehmen "mittel" sein. Immer mit der Kalibrierungstabelle abgleichen.
- **Regulierungslandschaft ohne Forschung.** Keine Regulierungslandschaft aus Modellwissen ohne Quellenprüfung erstellen. Behörden-Positionen ändern sich.
- **DSGVO-Vollzugsfristen.** Meldepflicht Datenpanne nach Art. 33 DSGVO: 72 Stunden an zuständige Behörde. Diese Frist ist absolute Grenze.
- **Beweislast UWG.** Bei § 5 UWG: der Unternehmer muss die Richtigkeit einer Werbeaussage nachweisen, nicht der Verbraucher deren Unrichtigkeit (§ 5 Abs. 4 UWG für nachprüfbare Tatsachen).

---

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 721/15 ("Nutzerdaten") – Zitatfehler (WRONG_TOPIC). Das Urteil behandelt unzulässige E-Mail-Werbung / § 7 UWG, nicht Datenhaftung bei Plattform-Nutzerdaten (dejure.org/2017,9951). Eintrag ersatzlos gelöscht.
Quelle : https://dejure.org/2017,9951
Aktion : Zeile entfernt
-->

## 3. `impressum-pflicht`

**Fokus:** Prüft die Impressumspflicht für Websites, Apps und Social-Media-Profile nach §§ 5 und 6 DDG und § 18 MStV, erstellt konforme Impressumstexte und identifiziert typische Abmahnrisiken nach UWG. Lädt bei Fragen zu Anbieterkennzeichnung, Impressum-Vollständigkeit und Bußgeldrisiken.

# Impressumspflicht (§§ 5, 6 DDG, § 18 MStV)

## Zweck

Dieser Skill prüft, ob eine Impressumspflicht nach dem Digitale-Dienste-Gesetz (DDG, in Kraft seit 14.05.2024, vormals TMG) und dem Medienstaatsvertrag (MStV) besteht, welche Pflichtangaben erforderlich sind und wie das Impressum korrekt zu gestalten ist. Er identifiziert Abmahnrisiken nach UWG und Bußgeldrisiken nach DDG. Anwendungsfälle: Unternehmenswebsite, Online-Shop, Blog, Social-Media-Profil (Instagram, LinkedIn, YouTube), App-Store-Listing, Newsletter.

## Eingaben

Das Modell benötigt:

- **Art des Dienstes**: Website, App, Social-Media-Profil, Newsletter?
- **Anbieter**: Natürliche Person (privat/gewerblich), GmbH, AG, Einzelunternehmen, Verein, öffentliche Stelle?
- **Geschäftsmäßigkeit**: Wird der Dienst geschäftsmäßig betrieben (also dauerhaft und mit Einnahmeabsicht) oder rein privat?
- **Redaktionell-journalistischer Inhalt**: Werden regelmäßig Inhalte mit gesellschaftlicher Relevanz veröffentlicht (Meinungsäußerungen, Nachrichten) → § 18 MStV relevant?
- **Bereits vorhandenes Impressum**: Vollständiger Text zur Prüfung?
- **Rechtsform und Sitz**: Handelsregisternummer, USt-IdNr., zuständige Aufsichtsbehörde, Kammerzugehörigkeit (bei Freiberuflern)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 5 Abs. 1 DDG** (vormals § 5 TMG): Pflichtangaben für Anbieter von Telemedien, die geschäftsmäßig betrieben werden (auch unentgeltlich, wenn mit wirtschaftlichem Hintergrund): Name, Anschrift, E-Mail, Telefon/Fax oder anderes schnelles elektronisches Kommunikationsmittel, ggf. Umsatzsteuer-ID, ggf. Handelsregisternummer, ggf. zuständige Aufsichtsbehörde, ggf. Berufsbezeichnung und Kammer (Freiberufler), ggf. berufsrechtliche Regelungen.
- **§ 5 Abs. 2 DDG**: Für juristische Personen: Vertretungsberechtigte(r) namentlich.
- **§ 6 DDG** (vormals § 6 TMG): Besondere Kennzeichnungspflichten für kommerzielle Kommunikation (Werbung).
- **§ 18 Abs. 2 MStV** (vormals § 55 Abs. 2 RStV): Für journalistisch-redaktionell gestaltete Angebote: Verantwortlicher i.S.d. Presserechts (v.i.S.d.P.) mit vollständigem Namen, Anschrift; muss natürliche Person sein, die unbeschränkt geschäftsfähig und in Deutschland ansässig ist.
- **§ 16 Abs. 1 Nr. 1 DDG**: Bußgeld bis 50.000 EUR bei fehlenden oder unvollständigen Pflichtangaben.
- **§ 5a Abs. 4 UWG**: Vorenthalten wesentlicher Informationen (einschließlich Impressumsangaben) als unlautere Geschäftspraxis; Grundlage für Abmahnungen durch Mitbewerber und Verbände.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

**Schritt 1 – Impressumspflicht dem Grunde nach**
- Geschäftsmäßiger Telemediendienst? → § 5 DDG anwendbar.
- Rein private Nutzung ohne kommerziellen Bezug → keine Impressumspflicht (Achtung: schon ein Affiliate-Link oder gesponserte Post begründet Gewerblichkeit).
- Redaktionell-journalistisches Angebot? → zusätzlich § 18 MStV prüfen.

**Schritt 2 – Pflichtangaben nach § 5 Abs. 1 DDG zusammenstellen**
- Vollständiger Name (Firmenname wie im Handelsregister) und Rechtsform.
- Ladungsfähige Anschrift (kein Postfach).
- E-Mail-Adresse.
- Telefonnummer oder anderes schnelles elektronisches Kommunikationsmittel.
- Bei GmbH, AG, KGaA: Handelsregisternummer, Registergericht, alle vertretungsberechtigten Geschäftsführer/Vorstände (§ 5 Abs. 2 DDG).
- USt-IdNr. (§ 27a UStG) oder Wirtschafts-IdNr., sofern vorhanden.
- Bei Freiberuflern: Berufsbezeichnung, verleihender Staat, Kammerzugehörigkeit, berufsrechtliche Vorschriften.
- Zuständige Aufsichtsbehörde bei erlaubnispflichtigem Gewerbe (z.B. Finanzdienstleistung, Gastronomie).

**Schritt 3 – v.i.S.d.P. nach § 18 Abs. 2 MStV**
- Gilt für journalistisch-redaktionell gestaltete Angebote (Meinungsblogs, Online-Zeitungen, Podcasts mit politischem/gesellschaftlichem Inhalt, YouTube-Kanäle mit regelmäßigem redaktionellem Programm).
- Verantwortliche Person: natürliche Person, volljährig, nicht vorbestraft (§ 18 Abs. 2 Satz 3 MStV), in Deutschland ansässig.
- Angabe: vollständiger Name, vollständige Anschrift im Impressum.

**Schritt 4 – Platzierung und Zugänglichkeit**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Erreichbarkeit: maximal zwei Klicks von jeder Seite aus.
- Ständige Verfügbarkeit: kein Login erforderlich, keine Paywall.
- Bei Social-Media-Profilen: Impressum im Profilbereich (Bio/Info) oder direkt verlinkt.

**Schritt 5 – Bußgeld- und Abmahnrisiko bewerten**
- § 16 DDG: Bußgeld bis 50.000 EUR bei fehlenden Angaben.
- § 5a Abs. 4 UWG: Abmahnfähigkeit durch Mitbewerber oder qualifizierte Einrichtungen (§ 8 Abs. 3 UWG).
- Häufige Abmahnfallen: fehlende Telefonnummer, fehlende Handelsregisternummer, keine v.i.S.d.P.-Angabe bei Blog.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabeformat

- **Impressumstext** (fertig formuliert, vollständig, einfügebereit).
- **Prüfliste** (Tabelle): Pflichtangabe × vorhanden/fehlend × Fundstelle.
- **Risikomemo** (kurz): Fehlende Angaben, Bußgeld- und Abmahnrisiko, Empfehlung.

## Beispiel

**Sachverhalt**: GmbH G betreibt einen Online-Shop mit integriertem Unternehmensblog, auf dem regelmäßig Meinungsbeiträge zu Branchenthemen erscheinen. Bisheriges Impressum enthält keine Handelsregisternummer und keine v.i.S.d.P.-Angabe.

**Gutachtenstil**:

*Impressumspflicht*: G betreibt einen geschäftsmäßigen Telemediendienst i.S.d. § 5 Abs. 1 DDG (Online-Shop + Blog mit Werbebezug). Impressumspflicht besteht unzweifelhaft.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*v.i.S.d.P.*: Der Blog mit Meinungsbeiträgen ist ein journalistisch-redaktionell gestaltetes Angebot i.S.d. § 18 Abs. 2 MStV. Eine verantwortliche Person mit vollständigem Namen und Anschrift ist zu benennen. Fehlt die Angabe, droht Bußgeld nach § 49 MStV bis 500.000 EUR.

*Empfehlung*: Impressum unverzüglich um HRB-Nummer, Registergericht und v.i.S.d.P.-Angabe ergänzen.

## Risiken und typische Fehler

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Social Media vergessen**: Instagram-, LinkedIn-, TikTok-Profile sind eigenständige Telemedien; kein gesondertes Impressum erforderlich, wenn eines eindeutig verlinkt ist.
- **TMG-Altlinks**: Nach DDG-Inkrafttreten (14.05.2024) sind Verweise auf "§ 5 TMG" veraltet; aktuell § 5 DDG angeben.
- **v.i.S.d.P. durch juristische Person**: Unzulässig nach § 18 Abs. 2 Satz 2 MStV; muss natürliche Person sein.
- **Abmahnmissbrauch-Schranke**: Seit UWG-Reform 2021 begrenzt § 8c UWG missbräuchliche Abmahnungen; qualifizierte Einrichtungen und Mitbewerber mit echtem Wettbewerbsverhältnis bleiben abmahnberechtigt.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- AUDIT 27.05.2026 bundle_040
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->
