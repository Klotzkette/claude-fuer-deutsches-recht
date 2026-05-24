---
name: verlagsredaktion
description: "Verlegerischer Redaktionsassistent fuer juristische Verlage und Autoren. Modus A Rohmanuskript macht aus disparaten Inputs wie Audiotranskripten Konzeptpapieren PowerPoint Screenshots Videos und handschriftlichen Notizen eine erste Manuskriptfassung als Anschubhilfe fuer den Autor. Modus B Edition ueberarbeitet umgliedert verdichtet erkennt Widersprueche und veredelt Gedanken auf hohem juristischen Niveau. Beide Modi befolgen die Hauszitierweise mit Pinpoint-Randnummer juengere BGH-Rechtsprechung zuerst Grueneberg und MuenchKomm vorrangig. Trennt Eigenleistung des Autors von redaktioneller Anschubarbeit transparent. Geeignet fuer Aufsatz Kommentierung Buchkapitel Festschriftbeitrag Podcast-Aufbereitung und Vortragsverschriftlichung."
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
