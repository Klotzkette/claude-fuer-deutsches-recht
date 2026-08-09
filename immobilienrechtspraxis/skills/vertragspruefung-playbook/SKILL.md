---
name: vertragspruefung-playbook
description: "Wenn es um Vertragsprüfung gegen Playbook in Immobilienrechtspraxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

# Vertragsprüfung gegen Playbook

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Vertragsprüfung gegen Playbook
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.

## Leitidee

Externe Verträge werden nicht freihändig geprüft, sondern gegen ein
hauseigenes Playbook. Das Playbook ist die institutionalisierte
Verhandlungserfahrung der Abteilung. Der Skill liefert Prüfergebnis,
Redline-Empfehlung und Business-Memo in einem Lauf.

## Inputs

- Externer Vertrag (.docx oder .pdf)
- Playbook (`playbook.md` oder `playbook.json`) mit Klauselkatalog
- Optional: interne Richtlinien (zB Mindest-Indexschwelle Maximalmietzeit)
- Optional: Vorvertrag oder LOI als Auslegungshilfe

## Playbook-Schema

```json
{
 "klausel_id": "indexmiete",
 "soll": "VPI mit Schwelle 5 Prozent und Mindestabstand zwölf Monate",
 "toleranz": "Schwelle drei bis sieben Prozent",
 "rot": "Vollindexierung ohne Schwelle oder Mindestabstand",
 "eskalation": "Asset-Management bei Abweichung",
 "fundstelle": "§ 557b BGB"
}
```

## Methodik

1. Vertrag in Klauseln segmentieren
2. Jede Klausel einem Playbook-Eintrag zuordnen (Klassifikation per
 Schlüsselwort und Semantik)
3. Ampel setzen — GRUEN entspricht Soll, GELB innerhalb Toleranz, ROT
 außerhalb Toleranz
4. Fehlende Klauseln als WEISS markieren (Schutzlücke)
5. Redline-Vorschlag in Tracked Changes erzeugen wo ROT oder WEISS
6. Business-Memo mit drei bis fünf Punkten was wirklich wirtschaftlich
 relevant ist

## Typische Prüfthemen im Immobilienrecht

- Textform langfristiger Gewerbemiete nach Paragraf 578 Absatz 1 und 550 BGB einschließlich vollständiger Nachtrags- und Kommunikationskette
- Indexmiete § 557b BGB versus Staffelmiete § 557a BGB
- Konkurrenzschutz und Sortimentsschutz bei Gewerberaum
- Untervermietung und Nutzungsänderung
- Betriebskostenkatalog Verordnung 2003 und Umlagevereinbarung
- Schönheitsreparaturen-Klauseln (BGH-Rechtsprechung Quotenklausel)
- Endrenovierungsklauseln (unwirksam wenn formularmaessig)
- Mietpreisbremse §§ 556d ff. BGB bei Wohnraum
- Kappungsgrenze § 558 Abs. 3 BGB
- Kündigungsausschluss und Mindestlaufzeit
- Gewährleistungsausschluss beim Grundstückskaufvertrag und Arglist
- Erschliessungskosten und Anliegerbeitraege
- Altlasten und Baulastenverzeichnis
- Belastung mit Grunddienstbarkeiten und Wegerechten

## Beispielformulierungen

- "Prüfe diesen Gewerbemietvertrag gegen unser Playbook. Schwerpunkt
 Schriftform Indexierung und Konkurrenzschutz."
- "Externer Kaufvertrag liegt vor. Vergleiche mit Playbook und liefere
 Ampelmatrix plus Redline."
- "Property-Management-Vertrag ist gekommen. Was muss vor Unterschrift
 geändert werden, gemessen an unseren Mindeststandards?"

## Aktuelle Rechtsprechung — Leitsaetze für Playbook-Prüfung (Stand 05/2026, verifiziert dejure.org)

- BGH, Urteil vom 4. November 2020, XII ZR 104/19: Nach damaligem Schriftformrecht musste bei ausgelagerten wesentlichen Bedingungen die Zusammengehörigkeit der Dokumente zweifelsfrei erkennbar sein; eine körperliche Verbindung war nicht zwingend. Für heutige Gewerberaumfälle nur mit Hinweis auf die seit 2025 geltende Textform und nach Prüfung der Übertragbarkeit verwenden.
- **BVerfG 25.03.2021, 2 BvF 1/20** (Berliner Mietendeckel): Landesgesetzliche Mietpreisregelung verfassungswidrig; für Neuvermietung bleiben deshalb die bundesrechtlichen Regeln der §§ 556d ff. BGB und die jeweils wirksame Landesverordnung zur Mietpreisbremse getrennt zu prüfen. Quelle: bundesverfassungsgericht.de.
- **BVerfG 25.03.2021, 2 BvF 1/20** (Berliner Mietendeckel-Beschluss): Landesgesetzliche Mietpreisregelung verfassungswidrig (Bundesrecht abschliessend). Quelle: bundesverfassungsgericht.de.
- **BGH 18.03.2020, VIII ZR 64/19** — Maengel bei Wohnraummiete als Mietminderungsgrund. Quelle: dejure.org/2020,4895.
- **BGH 27.06.2024, I ZR 98/23** (Katjes „klimaneutral"): Greenwashing in Mietvertraegen mit ESG-Bezug; Substantiierungspflicht. Quelle: bundesgerichtshof.de PM 144/2024.

Konkrete weitere Entscheidungen vor Ausgabe per dejure.org / bundesgerichtshof.de mit Datum verifizieren.

## Paragrafenkette Immobilienvertraege

- Kaufvertrag: §§ 433 ff. BGB, § 311b BGB (Formzwang Notar), §§ 437 ff. BGB (Maengelrechte), § 442 BGB (Ausschluss Arglist)
- Gewerbemiete: Paragraf 535 folgende BGB, Paragraf 578 Absatz 1 in Verbindung mit Paragraf 550 BGB für die Textform langfristiger Verträge, Paragrafen 579 und 580 BGB; Indexklauseln nicht unbesehen nach wohnraummietrechtlichem Paragraf 557b BGB beurteilen
- Wohnraummiete: §§ 549 ff. BGB, § 558 BGB (Kappungsgrenze), §§ 555b ff. BGB (Modernisierung), §§ 573 ff. BGB (Kuendigung)
- WEG-Verwaltervertrag: §§ 26 ff. WEG, § 19 Abs. 2 Nr. 6 WEG

## Integration mit Projekten und Agenten

Der Skill ist so gebaut, dass er in einem Projekt-Ordner mit fixiertem
Playbook und Vertragstyp laeuft. Ein Agent kann auf eingehende Verträge
auf einem Watch-Ordner reagieren und automatisch die Prüfung anstossen.
Siehe Skill `projekt-arbeitsweise`.
