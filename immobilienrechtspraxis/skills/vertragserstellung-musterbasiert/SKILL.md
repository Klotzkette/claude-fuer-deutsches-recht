---
name: vertragserstellung-musterbasiert
description: "Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis. Output: Vertragsentwurf auf Musterbasis. Abgrenzung: nicht individuelle Vertragsprüfung im Immobilienrechtspraxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Vertragserstellung musterbasiert

## Arbeitsbereich

Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis. Output: Vertragsentwurf auf Musterbasis. Abgrenzung: nicht individuelle Vertragsprüfung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Vertragserstellung musterbasiert
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Schriftform: § 550 BGB, § 311b BGB
- Mietpreisbremse: §§ 556d ff. BGB
- Modernisierung: §§ 555a ff. BGB
- WEG-Verwaltervertrag: §§ 26 ff. WEG

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
