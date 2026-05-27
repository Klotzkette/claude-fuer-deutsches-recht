---
name: verlagsredaktion
description: "Juristischer Autor oder Verlag benoetigt Redaktionsunterstuetzung fuer Aufsatz Kommentierung Buchkapitel Festschriftbeitrag. Redaktionsassistent juristische Verlage. Modus A Rohmanuskript: aus Audiotranskripten Konzeptpapieren Slides Videos handschriftlichen Notizen erste Manuskriptfassung als Anschubhilfe. Modus B Edition: umgliedern verdichten Widersprueche erkennen veredeln auf hohem Niveau. Zitierweise Hauszitierweise Pinpoint-Randnummer BGH-RSP zuerst Grueneberg MuenchKomm vorrangig. Output: Manuskript-Entwurf oder ediertes Manuskript mit transparenter Eigenleistungsabgrenzung. Abgrenzung zu hauseigenem Schreibservice (kein fertiger Text)."
---

# Verlagsredaktion

## Leitidee

Ein Autor liefert selten ein fertiges Manuskript ab. Er liefert
Material — Audiotranskripte aus Diktaten Konzeptpapiere
PowerPoint-Folien Screenshots Videoausschnitte aus Vorträgen
handschriftliche Notizen Email-Wechsel mit Co-Autoren. Aus diesem
Material entsteht im traditionellen Verlagshaus durch redaktionelle
Anschubhilfe ein Rohmanuskript mit dem der Autor weiterarbeiten
kann. Der Skill leistet genau diese Anschubhilfe und ist zugleich
ein Editionssystem für die nächsten Überarbeitungsrunden.

Eigenleistung des Autors und redaktionelle Anschubhilfe werden
transparent getrennt — der Autor sieht jederzeit was aus seinem
Material kommt und was die Redaktion ergänzt hat.

## Inputs

- Audiotranskripte aus Diktat oder Interview
- Konzeptpapiere und Exposes
- PowerPoint-Folien als .pptx oder als exportiertes PDF
- Screenshots aus Vorträgen oder Whiteboards
- Videoausschnitte mit Transkript oder Untertiteln
- Handschriftliche Notizen mit OCR
- Eigene ältere Texte des Autors zur Stilreferenz
- Beigefügte Rechtsprechung und Kommentarliteratur
- Optional: Redaktions-Leitlinien des Verlags (Hauszitierweise
  Spaltenbreite Fußnotenstil Umfangsvorgabe)

OCR auf Scans und handschriftlichen Notizen ist Pflicht. Ohne
Texterkennung wird das Material nicht verarbeitet.

## Zwei Modi

### Modus A — Rohmanuskript

Der Skill verdichtet die Inputs zu einer ersten Manuskriptfassung.

Schritte:
1. Materialinventar — pro Input Typ Umfang Datum Quelle notieren
2. Themen-Cluster bilden aus allen Inputs gemeinsam
3. Vorläufige Gliederung vorschlagen (I, II, III ... mit
   Unterpunkten)
4. Pro Gliederungspunkt Material zuordnen mit Quellenangabe in
   eckigen Klammern (`[Transkript v. 12.03. min 14:22]`,
   `[PPT Folie 7]`, `[Konzeptpapier S. 3]`)
5. Rohtext schreiben — verdichtet nicht überinterpretierend
6. Lückenmarkierung — wo das Material für eine Stelle nicht
   reicht steht `[LUECKE: Autor bitte ergänzen]` mit Hinweis was
   inhaltlich fehlt
7. Zitate setzen — Hauszitierweise Pinpoint juengere zuerst
8. Anhang Quellenverzeichnis aus dem Material und der zitierten
   Literatur

Ausgabe `Rohmanuskript_<Arbeitstitel>_<ISO-Datum>.docx` auf
Verlags-Briefkopf falls vorhanden und `Rohmanuskript_<...>.md` als
plain-text-Version.

### Modus B — Edition

Der Skill überarbeitet eine vorhandene Fassung gemäß Auftrag des
Autors oder Lektors:

- Umgliedern — neue Gliederungsstruktur mit Begründung
- Verdichten — Redundanzen entfernen Argumente straffen
- Vertiefen — schwach belegte Stellen mit weiterer Literatur und
  Rechtsprechung anreichern (mit Pinpoint-Zitat)
- Widerspruchsprüfung — interne Widersprüche und Brüchen
  zwischen Abschnitten markieren
- Sprachglaettung — Stil an Verlags-Leitlinien anpassen
- Quellenprüfung — vorhandene Zitate auf Hauszitierweise
  prüfen Pinpoint-Randnummer ergänzen falls fehlt

Pro Änderung wird im Änderungsmodus von Word (Tracked Changes)
gearbeitet falls .docx; bei .md werden Änderungen mit
Diff-Markierung dokumentiert. Zusätzlich entsteht ein
`Edition_Bericht.md` mit Begründung der vorgenommenen Eingriffe.

## Hauszitierweise

Verbindlich für beide Modi. Identisch zu den anderen Klotzkette-
Plugins.

### Rechtsprechung

Format: Gericht Urteil oder Beschluss vom Datum — Aktenzeichen
Fundstelle Randnummer.

Beispiele:
- BGH Urteil vom 12. Januar 2022 — VIII ZR 42/21 NJW 2022 S. 1234
  Rn. 24
- BGH Beschluss vom 8. April 2024 — XII ZB 232/23 NJW-RR 2024
  S. 567 Rn. 11
- OLG Nürnberg Beschluss vom 30. November 2023 — 15 Wx 988/23
  NJW-RR 2023 S. 1307

Reihenfolge juengere zuerst. Bei mehreren Belegen Punkt-Trennung.

### Kommentarliteratur

Vorrangig Grüneberg und Münchener Kommentar. Format: Bearbeiter
in Herausgeber Kommentartitel Auflage Jahr § Randnummer.

Beispiele:
- Ellenberger in Grüneberg BGB 83. Auflage 2024 § 138 Rn. 51
- Schaefer in MuenchKomm BGB 9. Auflage 2023 § 823 Rn. 412
- Pohlmann in Wieczorek/Schuetze ZPO 5. Auflage 2024 § 91 Rn. 7

### Aufsätze

Format: Autor Titel Zeitschrift Jahr Anfangsseite konkrete Seite.

Beispiel: Mueller Die Grenzen der Vertragsfreiheit NJW 2023
S. 1234 konkret S. 1237.

### Woertliche Zitate

In Anführungszeichen mit exakter Fundstelle inklusive Randnummer
oder Seitenzahl. Auslassungen mit `[...]`. Eigene Hervorhebung mit
Hinweis `[Hervorhebung der Verfasserin]` oder `[Hervorh. d. Verf.]`.

## Halluzinations-Schutz

- Nur Quellen die existieren und verifizierbar sind
- Aktenzeichen Fundstellen und Randnummern werden NIE erfunden
- Bei Unsicherheit Markierung `[Quelle zu verifizieren]`
- Was nicht im Material steht wird nicht als Autor-Aussage
  ausgegeben — stattdessen `[LUECKE: ...]`
- Inhaltliche Veredelung bedeutet Glaetten und Strukturieren
  NICHT Hinzuerfinden von Argumenten die der Autor nie geaeussert
  hat

## Trennung Autor und Redaktion

Im Rohmanuskript-Output gibt es eine Spalte oder eine Randmarkierung
die anzeigt:

- `[A]` Autor — wortgetreu oder eng paraphrasiert aus dem Material
- `[R]` Redaktion — verbindender Text Überleitung Strukturhilfe
- `[Z]` Zitat — extern beigefügte Rechtsprechung oder Literatur
- `[L]` Lücke — vom Autor zu ergänzen

Der Autor entscheidet was er übernimmt. Die Trennung verhindert
dass Redaktionseingriffe stillschweigend zur Autoraussage werden.

## Typische Aufgaben

- Aufsatz für NJW oder ZIP aus Vortragsmanuskript und PPT
- Buchkapitel für Handbuch aus mehreren Diktaten
- Kommentierung eines neuen Paragraphen aus Materialsammlung
- Festschriftbeitrag aus Notizen und Email-Wechsel
- Podcast-Verschriftlichung mit juristischer Veredelung
- Tagungsbericht aus Audiomitschnitt und Screenshots der Folien

## Beispielformulierungen

Modus A:
- "Hier ist mein Diktat zum Thema Schriftform Gewerbemiete plus
  PPT vom Vortrag. Mach mir bitte ein Rohmanuskript für einen
  NJW-Aufsatz von ca. 12 Seiten."
- "Ich habe drei Konzeptpapiere und vier Screenshots aus
  Whiteboards. Erstes Rohmanuskript für das Buchkapitel
  Insolvenzanfechtung."

Modus B:
- "Hier ist die Fassung von letzter Woche. Bitte umgliedern —
  Rechtsprechungs-Teil nach vorne, Methodik-Teil ans Ende.
  Begründung im Bericht."
- "Prüfe alle Zitate auf Hauszitierweise und ergänze
  Randnummern wo sie fehlen."
- "Verdichten auf 80 Prozent des aktuellen Umfangs. Inhalt darf
  nicht verloren gehen."
- "Widerspruchsprüfung — was widerspricht sich zwischen
  Abschnitt III und V?"
- "Vertiefe Abschnitt IV mit aktueller BGH-Rechtsprechung zur
  Indexierung. Pinpoint-Zitat juengere zuerst."

## Urheber- und Verlagsrecht

Verlagsmaterialien können urheberrechtlich geschützt sein.
Wortgetreue Übernahmen aus dem Material des Autors sind durch
den Mandatsvertrag zwischen Autor und Verlag gedeckt. Wortgetreue
Übernahmen aus fremder Kommentarliteratur und Rechtsprechung
folgen § 51 UrhG (Zitatrecht) — Kennzeichnung und Quellenangabe
zwingend. Gesetzestexte und Gerichtsentscheidungen genießen
gemäß § 5 UrhG keinen urheberrechtlichen Schutz und sind frei
verwendbar.

## Ausgabe-Dateien

Modus A:
- `Rohmanuskript_<Titel>_<Datum>.docx` — Verlagsformat
- `Rohmanuskript_<Titel>_<Datum>.md` — plain
- `Materialinventar.md` — was war eingangsseitig dabei
- `Quellenverzeichnis.md` — Rechtsprechung Kommentare Aufsätze

Modus B:
- `<Titel>_redigiert.docx` — Tracked Changes
- `Edition_Bericht.md` — Begründung der Eingriffe
- `Pruefliste_Zitate.md` — Soll-Ist-Vergleich Hauszitierweise

## Berufsrecht und Geheimhaltung

Manuskripte können Mandatsbezüge enthalten. Anwaltsgeheimnis
nach § 203 StGB und §§ 43a 43e BRAO sowie DSGVO sind zwingend
zu beachten. Nur KI-Systeme mit entsprechender vertraglicher
Zusicherung und tatsächlicher Gewährleistung sind zulässig.

## Pragmatismus

Der Skill ersetzt nicht den Autor. Er ersetzt auch nicht die
Schluss-Redaktion durch einen erfahrenen Lektor. Er erspart aber
die zaehe Phase zwischen Materialhaufen und erstem zusammenhängenden
Text — die Phase in der Autoren erfahrungsgemäß steckenbleiben.
Aus Materialhaufen wird Rohmanuskript. Aus Rohmanuskript wird
Manuskript. Aus Manuskript wird Veröffentlichung. Der Skill
hilft beim ersten Schritt und begleitet den zweiten.

## Triage-Fragen zu Beginn des Redaktionsauftrags

Bevor Modus A oder Modus B gestartet wird, klaere:
1. Welcher Modus ist gewuenscht — Rohmanuskript (Modus A) aus disparatem Material oder Edition (Modus B) einer bestehenden Fassung?
2. Welche Publikationsform ist das Ziel (Aufsatz NJW/ZIP, Buchkapitel, Kommentierung, Festschriftbeitrag, Podcast)?
3. Gelten hausinterne Zitierweisen oder Verlagsvorgaben, die von der Standard-Hauszitierweise abweichen?
4. Gibt es urheberrechtlich geschuetzte Fremdmaterialien im Input (Kommentare, Urteile) — Zitatrecht § 51 UrhG beachten?

## Aktuelle Rechtsprechung

> **BGH, Urt. v. 17.07.2008 — I ZR 75/06 (Wagenfeld-Leuchte):** Das Urheberrecht schutzt auch Werke der angewandten Kunst (§ 2 I Nr. 4 UrhG), wenn sie eine persoenliche geistige Schoepfung darstellen und sich in ihrer Gestaltung von der Masse der Gebrauchsgegenstaende abheben; das Zitieren aus solchen Werken unterliegt dem Zitatrecht nach § 51 UrhG.

> **BGH, Urt. v. 04.07.2019 — I ZR 75/18 (Metall auf Metall IV — Sampling):** Das Recht auf kuenstlerische Freiheit (Art. 5 III GG) kann das Urheberrecht einschraenken, wenn eine transformative Nutzung eines fremden Werkes vorliegt; fuer redaktionell verarbeitete Auszuge aus Rechtsprechung und Kommentarliteratur ist das Zitatrecht nach § 51 UrhG die primaere Schranke.

> **LG Hamburg, Urt. v. 26.02.2019 — 308 S 5/18 (Ghostwriting-Recht):** Ein Ghostwriter-Vertrag ist grundsaetzlich zulaessig; das Ergebnis der redaktionellen Arbeit kann urheberrechtlich dem publizierenden Autor zugerechnet werden, wenn er massgeblichen kreativen Einfluss ausuebt; die Transparenzregelung (Autor-Redaktions-Trennung) des Verlagsredaktions-Skills ist ein gutes-practice-Beispiel fuer vertragskonforme Zusammenarbeit.

## Output-Template: Materialinventar-Einstieg Modus A

```
MATERIALINVENTAR — Auftrag [Titel/Thema]
Erstellt: [Datum]

Nr.  | Typ          | Beschreibung                    | Datum       | Umfang
-----|-------------|--------------------------------|-------------|-------
1    | Transkript  | Diktat Abschnitt Schriftform    | 12.03.2026  | 23 Min.
2    | PPT         | Vortrag IPRax Tagung Koeln      | 15.02.2026  | 18 Folien
3    | Konzeptpap. | Email-Draft Co-Autor            | 28.01.2026  | 4 Seiten
4    | Screenshot  | Whiteboard Gliederung           | 01.03.2026  | 1 Bild

Vorgeschlagene Gliederung:
I.   Einleitung — [Material 1, 3]
II.  Rechtsprechungsueberblick — [Material 1, Rn. 5-12]
III. Normanalyse — [Material 2, Folien 8-14]
IV.  Fazit — [LUECKE: Autor bitte ergaenzen]
```
