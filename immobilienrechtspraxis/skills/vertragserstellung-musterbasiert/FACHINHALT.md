---
name: vertragserstellung-musterbasiert
description: "Für Vertragserstellung musterbasiert: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Vertragserstellung musterbasiert

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
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

## Typische manuelle Prüfpunkte bei Immobilienverträgen

- Vorkaufsrechte der Gemeinde §§ 24 ff. BauGB
- Genehmigung nach § 1365 BGB bei Verfügung über das Vermögen im Ganzen
- Grundstücksverkehrsgenehmigung GrdstVG
- Sanierungsvermerk § 144 BauGB, Erhaltungssatzung § 172 BauGB
- Wohnungseigentumsumwandlung § 250 BauGB (Genehmigungspflicht)
- WEG-Beschlüsse als Anlage (Beschlussfähigkeit, Anfechtungsfristen)
- Erbbauzins-Anpassungsklauseln und Heimfallrecht
- Mietpreisbremse §§ 556d ff. BGB, qualifizierter Mietspiegel
- Textform langfristiger Gewerberaummietvertrag nach Paragraf 578 Absatz 1 und 550 BGB; Vertragskette und Nachträge beweissicher führen
- Betriebskostenkatalog Verordnung 2003, Umlagevereinbarung
- Indexmiete §§ 557b BGB versus Staffelmiete § 557a BGB

## Beispielformulierungen

- "Erstelle aus Mustervertrag und Term Sheet einen Gewerberaummietvertrag. Dokumentiere Hauptvertrag, Anlagen und Nachträge in Textform nach Paragraf 578 Absatz 1 und 550 BGB."
- "Befuelle den Wohnraummietvertrag-Muster mit den Eckpunkten aus dem
 Eckpunktepapier. Prüfe ob Mietpreisbremse greift und markiere."
- "Erstelle WEG-Verwaltervertrag aus Muster, Term Sheet anbei,
 Bestellungsbeschluss als Anlage einfügen."

## Paragrafenkette

- Form: Paragraf 578 Absatz 1 in Verbindung mit Paragraf 550 BGB sowie Paragraf 311b BGB, soweit ein Grundstücksgeschäft betroffen ist
- Mietpreisbremse: §§ 556d ff. BGB
- Modernisierung: §§ 555a ff. BGB
- WEG-Verwaltervertrag: §§ 26 ff. WEG

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
