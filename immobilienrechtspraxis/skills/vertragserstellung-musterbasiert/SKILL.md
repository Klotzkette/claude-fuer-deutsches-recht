---
name: vertragserstellung-musterbasiert
description: "Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Pruefraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis. Output: Vertragsentwurf auf Musterbasis. Abgrenzung: nicht individuelle Vertragspruefung."
---

# Vertragserstellung musterbasiert

## Leitidee

Vertragserstellung ist NICHT voll an die KI delegierbar. Die KI ist ein
disziplinierter Schreibtisch, der vorgegebene Klauseln einsetzt, Platzhalter
befüllt und Querverweise konsistent haelt. Sie ist KEIN Drafter und schreibt
keine eigenen Klauseln in tragenden Punkten.

## Inputs

- Mustervertrag (.docx) der Kanzlei oder Rechtsabteilung
- Term Sheet oder Eckpunktepapier (.docx, .md, .pdf, freier Text)
- Optional: vorhandene Vorgängerverträge zur Stilreferenz
- Optional: Anlagenliste (Lageplan, Baubeschreibung, Hausordnung,
  Betriebskostenaufstellung)

## Klauselschutz — die zentrale Regel

Jede Klausel im Muster, die NICHT als Platzhalter markiert ist, ist tabu.
Markierungen die der Skill respektiert:

- `[[...]]` doppelte eckige Klammern für freie Eingaben
- `{{...}}` doppelte geschweifte Klammern für typisierte Variablen
- `__________` Unterstrich-Strecken für Daten und Betraege
- Gelb hinterlegte Felder im Word-Dokument
- Kommentare am Rand mit Praefix `KI:`

Findet die KI an einer NICHT-markierten Stelle einen logischen Widerspruch
zum Term Sheet (zB Term Sheet sagt befristet, Muster ist unbefristet),
DARF sie die Klausel nicht selbst ändern. Sie protokolliert den Konflikt
und gibt das Dokument unverändert zurück mit Hinweis.

## Methodik

1. Mustervertrag laden und alle Platzhalter inventarisieren
2. Term Sheet parsen — Parteien, Objekt, wirtschaftliche Eckpunkte,
   Sondervereinbarungen
3. Mapping Term-Sheet-Position auf Musterplatzhalter erstellen
4. Platzhalter befuellen, Querverweise (§-Verweise, Anlagen) anpassen
5. Konsistenzprüfung: Daten, Betraege ohne Komma in der Beschreibung,
   Parteiennennungen, Pluralformen
6. Änderungsprotokoll erzeugen — welche Platzhalter befüllt, welche offen,
   welche Konflikte
7. Roter Block oben im Dokument: was zwingend manuell zu prüfen ist

## Output

- `Vertrag_<Objekt>_<Datum>.docx` auf Muster-Layout, Platzhalter befüllt
- `Aenderungsprotokoll.md` mit Tabelle Platzhalter — Wert — Quelle im Term Sheet
- `Manuelle_Pruefung.md` mit Liste der Punkte die nur ein Jurist
  entscheiden kann (zB GenehmigungspflichtigerVerkauf §§ 1365 BGB,
  Vorkaufsrechte §§ 24 ff. BauGB, Denkmalschutz, Erbbauzins-Anpassung)

## Typische manuelle Pruefpunkte bei Immobilienverträgen

- Vorkaufsrechte der Gemeinde §§ 24 ff. BauGB
- Genehmigung nach § 1365 BGB bei Verfügung über das Vermögen im Ganzen
- Grundstücksverkehrsgenehmigung GrdstVG
- Sanierungsvermerk § 144 BauGB, Erhaltungssatzung § 172 BauGB
- Wohnungseigentumsumwandlung § 250 BauGB (Genehmigungspflicht)
- WEG-Beschlüsse als Anlage (Beschlussfähigkeit, Anfechtungsfristen)
- Erbbauzins-Anpassungsklauseln und Heimfallrecht
- Mietpreisbremse §§ 556d ff. BGB, qualifizierter Mietspiegel
- Schriftform Gewerbemietvertrag § 550 BGB (Heilung schwierig)
- Betriebskostenkatalog Verordnung 2003, Umlagevereinbarung
- Indexmiete §§ 557b BGB versus Staffelmiete § 557a BGB

## Beispielformulierungen

- "Erstelle aus Mustervertrag Gewerbemiete und beigefügtem Term Sheet
  einen Entwurf. Achte auf Schriftform § 550 BGB."
- "Befuelle den Wohnraummietvertrag-Muster mit den Eckpunkten aus dem
  Eckpunktepapier. Prüfe ob Mietpreisbremse greift und markiere."
- "Erstelle WEG-Verwaltervertrag aus Muster, Term Sheet anbei,
  Bestellungsbeschluss als Anlage einfügen."

## Aktuelle Rechtsprechung — Leitsaetze

- BGH, Urt. v. 07.03.2018 — XII ZR 129/16, NJW 2018, 1875 Rn. 22: Schriftformerfordernis § 550 BGB gilt fuer alle Aenderungen des Gewerbemietvertrags; Nachtraege ohne Schriftform koennen zur ordentlichen Kuendigung fuhren trotz vereinbarten Kuendigungsausschlusses.
- BGH, Urt. v. 25.07.2018 — VIII ZR 220/17, NJW 2018, 2564 Rn. 18: Mietvertrag-AGB-Klauseln zu Schoenheitsreparaturen sind wirksam nur bei Uebergabe in unrenoviertem Zustand mit entsprechender Minderung; Musterklauseln pruefen.
- BGH, Urt. v. 13.09.2023 — VIII ZR 117/22, NJW 2023, 3235 Rn. 15: Mietpreisbremse-Pflicht besteht ab dem ersten Mietvertrag nach Erlass der Landesverordnung; Mustervertrag muss Mietpreisbremseregelung und Ausnahmepruefung integrieren.

## Paragrafenkette

- Schriftform: § 550 BGB, § 311b BGB
- Mietpreisbremse: §§ 556d ff. BGB
- Modernisierung: §§ 555a ff. BGB
- WEG-Verwaltervertrag: §§ 26 ff. WEG

## Kommentarliteratur

- Schmidt-Futterer, Mietrecht, 15. Aufl. — Vertragsgestaltung
- BeckOK BGB — §§ 535 ff. Mietvertrag-Gestaltung
- Baermann, WEG, 15. Aufl. — §§ 26 ff. Verwaltervertrag
