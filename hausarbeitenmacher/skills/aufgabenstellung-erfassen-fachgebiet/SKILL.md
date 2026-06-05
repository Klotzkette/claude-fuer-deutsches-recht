---
name: aufgabenstellung-erfassen-fachgebiet
description: "Aufgabenstellung Erfassen Fachgebiet: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Aufgabenstellung Erfassen Fachgebiet

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Aufgabenstellung Erfassen Fachgebiet** im Plugin Hausarbeitenmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aufgabenstellung-erfassen` | Student erhaelt Hausarbeit-Aufgabenstellung und will den Sachverhalt strukturiert erfassen. Drei-Lese-Methode zerlegt Sachverhalt in wesentliche Tatsachen Beteiligte Zeitschiene. Bearbeitungsvermerk identifizieren wer fragt was wird geprüft. Normen §§ 133 157 BGB Auslegungsmethodik. Prüfraster Sachverhalts-Zerlegung Bearbeitungsvermerk-Analyse Schwerpunkt-Erkennung. Output strukturierte Sachverhaltskarte Bearbeitungshinweise. Abgrenzung zu bearbeitungsplan-erstellen (Zeitplan) und hausarbeit-workflow-start (Master-Workflow). |
| `fachgebiet-routing-zivil-oeffentlich-straf` | Student weiss nicht in welches Fachgebiet die Hausarbeit faellt: Zivilrecht öffentliches Recht Strafrecht oder Mix. Routing-Skill klaert Fachgebiet anhand Indikatoren. Normen allgemein BGB HGB VwGO StGB je nach Gebiet. Prüfraster Fachgebiet-Indikatoren Mix-Konstellationen Anspruchsgrundlagen-Typ. Output Fachgebiet-Zuordnung Routing-Empfehlung Erlaeuterung. Abgrenzung zu öffentliches-recht-statthaft (Schema) strafrecht-tatbestand (Schema) zivilrecht-anspruchsgrundlagen (Schema). |
| `gliederung-mit-tiefenstruktur` | Student erstellt Gliederung für juristische Hausarbeit mit korrekter Tiefenstruktur A Roemisch Arabisch Kleinbuchstaben. Anspruchsgrundlagen-Reihenfolge Zivilrecht öffentlich-rechtlicher Aufbau Strafrecht Drei-Stufen. Normen §§ 133 157 BGB Methodenlehre. Prüfraster Gliederungs-Logik Hierarchie Prüfungsschema-Sichtbarkeit Vollständigkeit. Output Gliederungs-Entwurf Tiefenstruktur-Template. Abgrenzung zu gutachtenstil-vs-urteilsstil (Stil) und subsumtion-schritt-fuer-schritt (Inhalt). |

## Arbeitsweg

Im Plugin Hausarbeitenmacher gilt für **Aufgabenstellung Erfassen Fachgebiet**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aufgabenstellung-erfassen`

**Fokus:** Student erhaelt Hausarbeit-Aufgabenstellung und will den Sachverhalt strukturiert erfassen. Drei-Lese-Methode zerlegt Sachverhalt in wesentliche Tatsachen Beteiligte Zeitschiene. Bearbeitungsvermerk identifizieren wer fragt was wird geprüft. Normen §§ 133 157 BGB Auslegungsmethodik. Prüfraster Sachverhalts-Zerlegung Bearbeitungsvermerk-Analyse Schwerpunkt-Erkennung. Output strukturierte Sachverhaltskarte Bearbeitungshinweise. Abgrenzung zu bearbeitungsplan-erstellen (Zeitplan) und hausarbeit-workflow-start (Master-Workflow).

# Aufgabenstellung erfassen


## Triage zu Beginn
1. Hausarbeit oder Seminararbeit — und von welchem Lehrstuhl/Fachgebiet?
2. Welches Rechtsgebiet ist nach erster Lektuere des Sachverhalts erkennbar?
3. Gibt es im Bearbeitungsvermerk explizite Einschraenkungen ("Verjährung ist nicht zu prüfen")?
4. Wie viel Zeit bleibt bis zur Abgabe?

## Aktuelle Rechtsprechung und Methodik
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 133, 157 BGB — Auslegung von Willenserklärungen und Vertraegen: Massstab fuer Sachverhaltswuerdigung
- § 195 BGB — Regelverjaehrung 3 Jahre: Zeitstrahl-Relevanz bei Klage/Mahnung/Verjährungsbeginn
- § 199 BGB — Verjährungsbeginn: Kenntnis und grob fahrlässige Unkenntnis
- § 204 BGB — Hemmung der Verjährung durch Rechtsverfolgung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Der erste Schritt jeder Hausarbeit: den Sachverhalt verstehen, **bevor** Du anfängst zu prüfen. Ohne sauberes Sachverhaltsbild ist jede Subsumtion willkürlich.

## Bevor Du anfängst

Lege bereit:

- den vollständigen Sachverhalt (Aufgabentext)
- den Bearbeitungs-Vermerk (am Ende des Sachverhalts)
- einen leeren Notizbogen für Deine Skizze
- ggf. Hinweise der Lehrkraft, in welchem Semester und Modul die Aufgabe steht

## Schritt 1 — Drei-Lese-Methode

### Erste Lesung: Überblick

Lies den Sachverhalt **ohne Notizen** durch. Lass die Geschichte wirken. Frage Dich am Ende:

- Was ist hier eigentlich los?
- Wer sind die handelnden Personen?
- Welches Rechtsgebiet ist offensichtlich? (BGB-Schuldrecht? StGB-Körperverletzung? Verwaltungsbescheid?)

### Zweite Lesung: Detail

Lies langsam und unterstreiche / markiere:

- **Personen / Beteiligte** (vergib Kennbuchstaben — A, B, C, K für Kläger, B für Beklagter, T für Täter, O für Opfer)
- **Daten** (jedes Datum, das im Sachverhalt erwähnt wird)
- **Orte** (zur Bestimmung der örtlichen Zuständigkeit)
- **Beträge** (zur Bestimmung von Streitwert / Schaden)
- **Verträge / Rechtsgeschäfte** (was wurde wann geschlossen?)

### Dritte Lesung: Skizze

Zeichne ein **Beziehungs-Diagramm**:

- Wer steht in welcher Beziehung zu wem?
- Welche Verträge zwischen welchen Personen?
- Wer hat wem was geschuldet / geleistet / verweigert?
- Welche Personen haben sich wann wo getroffen?

## Schritt 2 — Wesentliche und unwesentliche Tatsachen

### Wesentlich

- Erklärungen, Vereinbarungen, Handlungen, die rechtliche Folgen haben
- Daten von Erklärungen (Vertragsabschluss, Mahnung, Kündigung, Tatzeit)
- Beträge, die rechtlich relevant sind
- Identifizierbare Personen mit Rollen

### Unwesentlich (häufig)

- Beschreibende Adjektive (sympathisch, ärgerlich) ohne rechtlichen Anker
- Hintergrund-Geschichte (Was die Person im Beruf macht), außer es ist relevant
- Wetterangaben, außer bei Verkehrsdelikt
- Daten ohne rechtlichen Bezug

### Hilfsfrage

> "Wenn ich diese Tatsache weglasse — ändert sich dann das rechtliche Ergebnis?"

Wenn **nein**: vermutlich unwesentlich.
Wenn **ja oder eventuell**: wesentlich.

## Schritt 3 — Bearbeitungsvermerk verstehen

Der Bearbeitungs-Vermerk steht typisch am Ende des Sachverhalts. Lies ihn besonders sorgfältig:

### Standard-Formulierungen

- **"Beurteilen Sie die Rechtslage"**: vollständiges Gutachten, alle Ansprüche prüfen
- **"Prüfen Sie die Ansprüche des A gegen B"**: nur diese Richtung, nicht umgekehrt
- **"Bestehen Schadensersatz-Ansprüche?"**: nur Schadensersatz, nicht Erfüllung etc.
- **"Wie ist die Rechtslage in einem Schriftsatz an das Gericht zu vertreten?"**: parteiischer Standpunkt
- **"Hilfsweise / Hilfsgutachten"**: Wenn der Haupt-Ergebnis-Pfad zu einem bestimmten Ergebnis kommt, ist hilfsweise auch das andere Ergebnis zu prüfen

### Frage-Vermerke

- **"§ XYZ ist nicht zu prüfen"**: aussparen
- **"Die örtliche Zuständigkeit ist nicht zu prüfen"**: nicht subsumieren
- **"Gehen Sie davon aus, dass..."**: als feststehend annehmen

## Schritt 4 — Zeitstrahl erstellen

Bei Sachverhalten mit mehreren Zeit-Punkten:

```
T-30 Tage: Vertragsschluss A-B
T-20 Tage: Lieferung
T-15 Tage: Mängelanzeige A
T-10 Tage: Nacherfüllungs-Frist
T-7 Tage: Rücktrittserklärung A
T-0: Klage
```

Wozu? Bei Schuldrechts-Sachverhalten (Verzug, Verjährung, Fristen) hilft der Zeitstrahl enorm.

## Schritt 5 — Skizziere die rechtlichen Fragen

**Nicht** subsumieren, sondern **identifizieren**:

- Welche Anspruchs-Konstellationen gibt es?
- Welche Tatbestände kommen in Frage?
- Welche Mehrheits-Meinungen sind hier zu erwarten?
- Welche Methoden-Probleme (Auslegung, Analogie)?

## Schritt 6 — Vor-Recherche

Bevor Du anfängst zu schreiben:

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Welche aktuellen Aufsätze in NJW, JuS, JA, JURA?

## Hilfsfragen für Deine eigene Reflexion

- Habe ich den Sachverhalt **dreimal** gelesen?
- Habe ich eine **Skizze** der Beteiligten?
- Habe ich den **Bearbeitungs-Vermerk** wortgenau verstanden?
- Habe ich einen **Zeitstrahl** (bei zeitkritischen Sachverhalten)?
- Habe ich die **rechtlichen Fragen** identifiziert (nicht gelöst)?
- Habe ich eine **Vor-Recherche** durchgeführt?

## Häufige Anfänger-Fehler

1. **Sofort subsumieren** ohne Sachverhalt zu verstehen — führt zu falschen Anspruchs-Grundlagen
2. **Bearbeitungs-Vermerk übersehen** — Stoff falsch abgegrenzt
3. **Personen-Buchstaben verwechseln** — Verwirrung beim Schreiben
4. **Datum übersehen** — Verjährungs-, Verzugs-, Fristen-Fragen falsch
5. **"Hilfsweise"-Hinweis übersehen** — wesentlicher Teil der Aufgabe nicht geprüft

## Übergang zu

Wenn Du die Aufgabenstellung erfasst hast, gehe weiter zu

- `fachgebiet-routing-zivil-oeffentlich-straf` — Welches Fachgebiet?
- `bearbeitungsplan-erstellen` — Zeitplan und Stoff-Aufteilung

## 2. `fachgebiet-routing-zivil-oeffentlich-straf`

**Fokus:** Student weiss nicht in welches Fachgebiet die Hausarbeit faellt: Zivilrecht öffentliches Recht Strafrecht oder Mix. Routing-Skill klaert Fachgebiet anhand Indikatoren. Normen allgemein BGB HGB VwGO StGB je nach Gebiet. Prüfraster Fachgebiet-Indikatoren Mix-Konstellationen Anspruchsgrundlagen-Typ. Output Fachgebiet-Zuordnung Routing-Empfehlung Erlaeuterung. Abgrenzung zu öffentliches-recht-statthaft (Schema) strafrecht-tatbestand (Schema) zivilrecht-anspruchsgrundlagen (Schema).

# Fachgebiet-Routing: Zivilrecht — Öffentliches Recht — Strafrecht

## Zweck

Ohne klares Fachgebiet kein klares Prüfungsschema. Die Hausarbeit hat einen Schwerpunkt — manchmal mit Mit-Aspekten anderer Fachgebiete.

## Schritt 1 — Erste Indikatoren je Fachgebiet

### Zivilrecht

- Zwei (oder mehr) **Privatpersonen** stehen sich gegenüber
- Es geht um **Verträge, Eigentum, Schadensersatz, Familie, Erbschaft**
- Stichworte: kaufen, verkaufen, mieten, leihen, schenken, heiraten, vererben, Hund beißt
- Anspruchsgrundlagen aus **BGB, HGB, GmbHG, WEG, ProdHaftG** etc.
- Gerichtsweg: Amtsgericht / Landgericht / Oberlandesgericht / BGH
- Beteiligte häufig: K (Kläger), B (Beklagter)

### Öffentliches Recht

- Eine **Behörde / der Staat** ist auf einer Seite
- Es geht um **Verwaltungsakt, Genehmigung, Erlaubnis, Polizeirecht, Steuerrecht, Baurecht, Sozialleistungen**
- Stichworte: Bescheid, Bauantrag, Polizei, Versammlung, Sozialleistung, Asyl, Hund-Halten-Verboten
- Anspruchsgrundlagen aus **VwGO, VwVfG, Spezial-Gesetze** (BImSchG, BBauG, BPolG, SGB)
- Gerichtsweg: Verwaltungsgericht / Oberverwaltungsgericht / BVerwG; oder: BVerfG
- Beteiligte häufig: K (Kläger Bürger), Beklagte Behörde (Stadt, Land, Bund)

### Strafrecht

- Es geht um eine **Tat** (Körperverletzung, Diebstahl, Betrug, Tötung, Sexualdelikt, Verkehrsdelikt)
- Eine **Person** soll bestraft werden
- Anspruchsgrundlagen aus **StGB, JGG, BtMG, WaffG** etc.
- Verfahren: StPO; Ermittlungs-Behörde StA + Polizei; Gericht: Amtsgericht / Landgericht / BGH
- Beteiligte häufig: T (Täter), O (Opfer), ggf. Mittäter

## Schritt 2 — Mix-Konstellationen

Hausarbeiten haben oft Schwerpunkte mit Neben-Aspekten:

### Zivilrecht mit Verfassungsbezug

- Z.B. Mietrecht und Grundrechte (Eigentum, Wohnungsfreiheit)
- Strafrecht und Grundrechte (Persönlichkeitsrecht)
- Schwerpunkt bleibt Zivil-/Strafrecht; Verfassung wird verfassungs-konform ausgelegt

### Zivilrecht mit EU-Bezug

- Verbraucherschutz-Richtlinie, AGB-Richtlinie, Datenschutz-Grundverordnung
- Schwerpunkt bleibt BGB / nationales Recht, mit EU-konformer Auslegung

### Zivilrecht und Arbeitsrecht

- Arbeitsrecht ist im Kern Zivilrecht (Arbeitsvertrag) + Spezial-Gesetze (KSchG, BGB, BetrVG)
- Hauptzugang über BGB-Anspruchsgrundlagen + spezifische Arbeitsrechts-Normen

### Öffentliches Recht und Strafrecht (parallel)

- Z.B. Polizei-Maßnahme + Strafverfahren
- Trennung: ÖR für die Polizei-Befugnis, Strafrecht für die Strafbarkeit der Beteiligten

### Zivilrecht und Verfassungsrecht (Drittwirkung)

- Mittelbare Grundrechts-Wirkung im Zivilrecht
- Z.B. AGG-Diskriminierung im Mietverhältnis
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 3 — Hilfsfragen

### Bei Unklarheit, ob Zivilrecht oder ÖR

> "Steht eine Behörde / der Staat auf einer Seite?"

- **Ja**: ÖR (Anfechtungsklage, Verpflichtungsklage, Eilantrag)
- **Nein, beide Seiten Privat**: Zivilrecht

> "Wird ein Verwaltungsakt erlassen oder abgewehrt?"

- **Ja**: ÖR
- **Nein**: Zivilrecht / Strafrecht

### Bei Unklarheit, ob Strafrecht oder Zivilrecht

> "Geht es darum, dass jemand bestraft werden soll?"

- **Ja**: Strafrecht
- **Nein, Schadensersatz?**: Zivilrecht
- **Beides**: Zwei separate Gutachten

### Bei Mehrebenen-Konstellation

> "Welches ist das Schwerpunkt-Problem im Sachverhalt?"

- Schwerpunkt ist meist im Bearbeitungs-Vermerk erkennbar
- Bei "Beurteilen Sie die strafrechtliche Verantwortlichkeit" → klares Strafrecht
- Bei "Welche Klagemöglichkeit besteht?" mit Behörden-Beteiligung → ÖR

## Schritt 4 — Reihenfolge bei Mix

Bei mehreren Fachgebieten ist die Reihenfolge wichtig:

### Reihenfolge typisch

1. Zivilrecht (wenn schwerpunkt)
2. Öffentliches Recht (wenn parallel oder Vorfrage)
3. Strafrecht (wenn parallel)

### Bei reinem Schwerpunkt-Fach

Nur das Schwerpunkt-Fach prüfen; Andere als Vorfrage oder Anmerkung.

### Bei parallelem Mix (z.B. zivilrechtliche + strafrechtliche Verantwortlichkeit)

Beide gleichwertig prüfen, Gliederung typisch:

```
A. Zivilrechtliche Ansprüche
 I. ...
B. Strafrechtliche Verantwortlichkeit
 I. ...
```

## Schritt 5 — Schwerpunkt-Identifikation

### Indikatoren im Sachverhalt

- Was nimmt Raum-Anteil ein? (Häufig: 60-70 % Schwerpunkt)
- Welches Detail wird im Sachverhalt ungewöhnlich detailliert ausgeführt? (Hinweis auf Streit-Punkt)
- Welche Personen-Konstellation ist im Mittelpunkt?

### Indikatoren im Bearbeitungs-Vermerk

- Genaue Wort-Wahl: "Ansprüche" → Zivilrecht; "Klage" → ÖR; "Strafbarkeit" → Strafrecht
- "Im Schriftsatz an das Gericht XYZ" → Gerichtsname verrät Fachgebiet (Verwaltungsgericht → ÖR; Strafgericht → StR; Zivilgericht → Zivilrecht)

## Schritt 6 — Bei Unsicherheit

- Frage Lehrkraft / Tutor
- Vergleich mit dem Modul-Titel (im Sommersemester oft Schwerpunkt-Hinweis)
- Schau in Modul-Handbuch

## Hilfsfragen für Deine Reflexion

- Ist mein **Schwerpunkt** klar?
- Habe ich **Mit-Aspekte** erkannt?
- Habe ich die **Reihenfolge** bei Mix-Konstellation bestimmt?
- Bin ich mit dem **Bearbeitungs-Vermerk** kompatibel?

## Übergang zu

- Zivilrecht-Schwerpunkt: `zivilrecht-anspruchsgrundlagen-pruefung`
- ÖR-Schwerpunkt: `oeffentliches-recht-statthaft-zulaessig-begruendet` oder `verfassungsrecht-grundrechtspruefung`
- Strafrecht-Schwerpunkt: `strafrecht-tatbestand-rechtswidrigkeit-schuld`
- EU-Bezug: `europarecht-anwendbarkeit-vorrang-vorabentscheidung`
- Rechtstheorie / -philosophie: `rechtstheorie-rechtsphilosophie-anbindung`

## 3. `gliederung-mit-tiefenstruktur`

**Fokus:** Student erstellt Gliederung für juristische Hausarbeit mit korrekter Tiefenstruktur A Roemisch Arabisch Kleinbuchstaben. Anspruchsgrundlagen-Reihenfolge Zivilrecht öffentlich-rechtlicher Aufbau Strafrecht Drei-Stufen. Normen §§ 133 157 BGB Methodenlehre. Prüfraster Gliederungs-Logik Hierarchie Prüfungsschema-Sichtbarkeit Vollständigkeit. Output Gliederungs-Entwurf Tiefenstruktur-Template. Abgrenzung zu gutachtenstil-vs-urteilsstil (Stil) und subsumtion-schritt-fuer-schritt (Inhalt).

# Gliederung mit Tiefen-Struktur


## Triage zu Beginn
1. Welches Fachgebiet und wie viele Anspruchsgrundlagen/Pruefungspunkte sind zu erwarten?
2. Wie ist die gewuenschte Tiefe der Gliederung (Anfaenger: A.I.1.a), Examen: tiefer)?
3. Gibt es Konkurrenzen zwischen Anspruchsgrundlagen, die in der Gliederung sichtbar sein muessen?
4. Sollen Hilfsweise-Pruefungen als eigene Gliederungspunkte oder als Unterpunkte erscheinen?

## Aktuelle Rechtsprechung und Methodik
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 242 BGB — Treu und Glauben: Gliederung muss die rechtlichen Beziehungen vollstaendig abbilden
- § 308 ZPO — Bindung an Antraege: Gliederung darf nicht ueber den Bearbeitungsvermerk hinausgehen
- §§ 195 ff. BGB — Verjährung als eigener Gliederungspunkt bei Anspruchs-Erloesung
- § 362 BGB — Erfuellung als erster Erloeschungsgrund in Gliederungs-Unterebene

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Eine gute Gliederung zeigt schon im Inhaltsverzeichnis, ob Du das Problem verstanden hast. Sie ist die Schiene, auf der die Argumentation läuft.

## Schritt 1 — Standard-Tiefenstruktur

```
A. Erster Hauptpunkt
 I. Erster Unter-Hauptpunkt
 1. Erste Voraussetzung
 a) Erste Teilvoraussetzung
 aa) Erste Teil-Teil-Voraussetzung
 bb) Zweite Teil-Teil-Voraussetzung
 b) Zweite Teilvoraussetzung
 2. Zweite Voraussetzung
 II. Zweiter Unter-Hauptpunkt
B. Zweiter Hauptpunkt
```

**Reihenfolge**: A — B — C; I — II — III; 1 — 2 — 3; a) — b) — c); aa — bb — cc.

## Schritt 2 — Reihenfolge je Fachgebiet

### Zivilrecht

```
A. Anspruch K gegen B aus § 433 II BGB (Kaufpreiszahlung)
 I. Wirksamer Kaufvertrag
 1. Angebot
 2. Annahme
 3. Wirksamkeit (Geschäftsfähigkeit, Form, AGB)
 II. Anspruch nicht erloschen
 1. Erfüllung § 362 I BGB
 2. Aufrechnung § 387 BGB
 3. Verjährung
 III. Anspruch durchsetzbar
 1. Einreden (z.B. § 320 BGB)

B. Anspruch K gegen B aus § 280 I BGB iVm § 433 BGB (Schadensersatz statt der Leistung)
 I. Schuldverhältnis
 II. Pflichtverletzung
 III. Vertretenmüssen
 IV. Schaden
```

### Öffentliches Recht (Verwaltungsklage)

```
A. Zulässigkeit
 I. Verwaltungsrechtsweg § 40 VwGO
 II. Statthafte Klageart § 42 I VwGO
 III. Klagebefugnis § 42 II VwGO
 IV. Vorverfahren §§ 68 ff. VwGO
 V. Klagefrist § 74 VwGO
 VI. Zuständigkeit (sachlich, örtlich)

B. Begründetheit
 I. Anspruchsgrundlage / Rechtsgrundlage
 II. Formelle Rechtmäßigkeit (Zuständigkeit, Verfahren, Form)
 III. Materielle Rechtmäßigkeit
 1. Tatbestand
 2. Rechtsfolge / Ermessen
 IV. Rechtsverletzung Kläger
```

### Strafrecht

```
A. Strafbarkeit T wegen Diebstahl gemäß § 242 StGB
 I. Tatbestand
 1. Objektiver Tatbestand
 a) Fremde bewegliche Sache
 b) Wegnahme
 aa) Bruch fremden Gewahrsams
 bb) Begründung neuen Gewahrsams
 2. Subjektiver Tatbestand
 a) Vorsatz
 b) Zueignungsabsicht
 aa) Aneignungs-Element
 bb) Enteignungs-Element
 II. Rechtswidrigkeit
 III. Schuld
 1. Schuldfähigkeit
 2. Schuldformen / Unrechtsbewusstsein
 3. Entschuldigungsgründe
 IV. Strafzumessungs-Erwägungen (ggf.)
 V. Ergebnis
```

## Schritt 3 — Anspruchsgrundlagen-Reihenfolge im Zivilrecht (V-C-G-D-D-B)

| Rang | Anspruchs-Grundlage | Norm |
|---|---|---|
| **V** ertrag | Erfüllungsanspruch | § 433 II BGB usw. |
| **C** ulpa in contrahendo | Vorvertragliches Verschulden | § 280 I iVm § 311 II BGB |
| **G** eschäftsführung ohne Auftrag | echte / unechte GoA | §§ 677 ff. BGB |
| **D** inglich | Eigentums-/Besitzansprüche | §§ 985 und 1004 BGB |
| **D** elikt | Unerlaubte Handlung | §§ 823 ff. BGB |
| **B** ereicherung | Leistungs-/Eingriffskondiktion | §§ 812 ff. BGB |

### Warum diese Reihenfolge?

- **Vertraglich** vor **gesetzlich**: Vertrags-Anspruch ist regelmäßig spezieller
- **Vorvertraglich** vor **dinglich**: c.i.c. wird oft als "neben-vertraglich" gerechnet
- **Vor Bereicherung**: weil bei Vorliegen eines Vertrags Bereicherung typisch ausgeschlossen ist (Bestandsschutz Leistungs-Anspruch)

## Schritt 4 — Tiefe der Gliederung

### Anfänger-Hausarbeit (20-30 Seiten)

- Hauptpunkte: 3-5
- Maximal-Tiefe: aa) / bb)
- Mehr Tiefe verzettelt

### Fortgeschrittenen-Hausarbeit (30-40 Seiten)

- Hauptpunkte: 4-7
- Maximal-Tiefe: aaa) / bbb)
- Bei sehr komplexen Anspruchs-Konkurrenzen tiefere Strukturierung

### Examens-Hausarbeit (50-80 Seiten)

- Hauptpunkte: 5-10
- Maximal-Tiefe: ααα) / βββ) (gr. Buchstaben für Tiefen-Tiefe)

## Schritt 5 — Konkretes Gliederungs-Beispiel — gemischter Fall

**Sachverhalt**: A verkauft B ein gebrauchtes Auto. B zahlt nicht. Später entwickelt A Bedenken wegen einer Mängel-Anzeige B's, dass das Auto nicht funktioniere.

```
A. Anspruch A gegen B auf Kaufpreis aus § 433 II BGB
 I. Wirksamer Kaufvertrag
 1. Angebot
 2. Annahme
 3. Wirksamkeit (AGB-Kontrolle? Sittenwidrigkeit?)
 II. Anspruch nicht erloschen
 1. Erfüllung
 2. Rücktritt B (§ 437 Nr. 2 sowie §§ 323 und 326 BGB)
 a) Mangel
 aa) Vereinbarte Beschaffenheit
 bb) Übliche Beschaffenheit
 b) Nacherfüllungs-Frist gesetzt?
 c) Folge: Rücktritt durchgreifend?
 3. Aufrechnung (Schadensersatz B)
 III. Anspruch durchsetzbar
 1. Verjährung
 2. § 320 BGB Einrede

B. Anspruch A gegen B auf Schadensersatz aus §§ 280 I, 437 Nr. 3 BGB
 I. Schuldverhältnis (Kaufvertrag)
 II. Pflichtverletzung
 III. Vertretenmüssen
 IV. Schaden

C. Gegenanspruch B gegen A auf Lieferung mangelfreier Sache aus § 437 Nr. 1 BGB
 I. Mangel
 II. Frist
 III. Anspruch nicht ausgeschlossen
```

## Schritt 6 — Probleme bei der Gliederung

### Problem 1: Doppelung von Voraussetzungen

Wenn dieselbe Voraussetzung in zwei Anspruchs-Grundlagen geprüft wird:

✅ Beim ersten Mal vollständig prüfen.
✅ Beim zweiten Mal verweisen: "Auf die Ausführungen unter A. I. wird verwiesen."

### Problem 2: Tief-Verschachtelung

Wenn die Tiefe `aa) → aaa)` benötigt wird, prüfe:
- Lässt sich strukturell anders gliedern?
- Sind die untersten Punkte wirklich getrennt zu behandeln?

### Problem 3: Hilfsweise-Prüfung

Wenn ein Punkt am Ergebnis nicht entscheidet, aber zur Vollständigkeit zu prüfen ist:

```
III. Hilfsweise: Annahme der Wirksamkeit des Vertrags
 1. ...
 2. ...
```

### Problem 4: Mehrere Anspruchssteller

Bei mehreren Klägern: pro Kläger eigenen Hauptpunkt.

```
A. Ansprüche des A
 I. Anspruch gegen B
 II. Anspruch gegen C
B. Ansprüche des K
 I. Anspruch gegen B
 II. Anspruch gegen C
```

## Schritt 7 — Inhaltsverzeichnis

### Format

```
INHALTSVERZEICHNIS

A. Ansprüche des A gegen B........................................ 5
 I. Anspruch aus § 433 II BGB................................... 5
 1. Wirksamer Kaufvertrag.................................... 5
 a) Angebot............................................... 5
 b) Annahme............................................... 6
 c) Wirksamkeit........................................... 7
 2. Anspruch nicht erloschen.................................. 9
 II. Anspruch aus § 823 I BGB................................... 12
B. Ansprüche des B gegen A....................................... 15
...
```

### Tipps

- Seitenzahlen genau angeben
- Tiefen-Struktur visuell durch Einrückung
- Bei elektronisch generiertem Inhaltsverzeichnis Verlinkungen verwenden

## Schritt 8 — Selbst-Test

- Liest sich Deine Gliederung wie eine Geschichte?
- Folgen die Anspruchs-Grundlagen der V-C-G-D-D-B-Regel (Zivilrecht)?
- Sind alle Tatbestandsmerkmale erfasst?
- Sind keine Strukturen über-tief?
- Sind alle Hilfsweise-Punkte gekennzeichnet?

## Hilfsfragen für Deine Reflexion

- Habe ich die **Reihenfolge** der Anspruchsgrundlagen richtig?
- Ist meine **Tiefe** angemessen für die Hausarbeit-Art?
- Habe ich alle **Tatbestandsmerkmale** erfasst?
- Habe ich die **Konkurrenzen** strukturell abgebildet?
- Habe ich **Hilfsweise-Prüfungen** als solche markiert?

## Übergang zu

- `gutachtenstil-vs-urteilsstil` — Schreib-Stil
- `zivilrecht-anspruchsgrundlagen-pruefung` — Detail Zivilrecht-Schema
- `oeffentliches-recht-statthaft-zulaessig-begruendet` — ÖR-Schema
- `strafrecht-tatbestand-rechtswidrigkeit-schuld` — Strafrecht-Schema
