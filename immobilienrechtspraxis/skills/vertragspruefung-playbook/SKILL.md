---
name: vertragspruefung-playbook
description: "Immobilienrechtliche Vertraege nach standardisiertem Playbook pruefen: Kaufvertrag, Grundschuld, WEG. Normen: §§ 433 ff. 873 ff. BGB, WEG, GrEStG, GBO. Pruefraster: Playbook-Checkliste, Risikoklauseln, Notar- und Formerfordernisse. Output: Vertragspruefergebnis mit Markierungen. Abgrenzung: nicht Vertragserstellung."
---

# Vertragsprüfung gegen Playbook

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

## Output

- `Pruefbericht_<Vertragsname>.md` mit Ampelmatrix in Tabellenform
- `<Vertragsname>_redlined.docx` mit Tracked Changes auf Klauselbasis
- `Memo_Business.md` — eine Seite, in Klartext, für Geschäftsleitung

## Typische Prüfthemen im Immobilienrecht

- Schriftform Gewerbemiete § 550 BGB inklusive aller Nachtraege
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

## Aktuelle Rechtsprechung — Leitsaetze fuer Playbook-Pruefung

- BGH, Urt. v. 07.03.2018 — XII ZR 129/16, NJW 2018, 1875 Rn. 22: Das Schriftformerfordernis des § 550 BGB bei Gewerbemietvertraegen gilt auch fuer saemtliche Nachtraege; fehlt die Schriftform eines Nachtrags, kann jede Partei ordentlich kuendigen trotz vereinbarten Kuendigungsausschlusses.
- BGH, Urt. v. 21.11.2018 — VIII ZR 255/17, NJW 2019, 601 Rn. 28: AGB-Klauseln zu Schoenheitsreparaturen sind unwirksam, wenn sie den Mieter zur Renovierung unabhaengig vom tatsaechlichen Renovierungsbedarf verpflichten; der Startbedingungsansatz ist der korrekte Massstab.
- BGH, Urt. v. 29.04.2020 — VIII ZR 315/18, NJW 2020, 2406 Rn. 19: Endrenovierungsklauseln in Formularmietvertraegen sind unwirksam, wenn sie keine Ruecksicht auf den Abnutzungszustand nehmen; Individualvereinbarung moeglich aber AGB-Kontrolle streng.
- BGH, Urt. v. 11.12.2019 — XII ZR 26/19, NJW 2020, 460 Rn. 31: Gewerbemietvertrag ist wirksam, wenn Mietgegenstand und Mietzins hinreichend bestimmbar; unklare Mietzinsindexierungsklausel fuehrt nicht zur Nichtigkeit sondern zur ergaenzenden Vertragsauslegung.

## Paragrafenkette Immobilienvertraege

- Kaufvertrag: §§ 433 ff. BGB, § 311b BGB (Formzwang Notar), §§ 437 ff. BGB (Maengelrechte), § 442 BGB (Ausschluss Arglist)
- Gewerbemiete: §§ 535 ff. BGB, § 550 BGB (Schriftform langfristig), § 557b BGB (Indexmiete), §§ 579, 580 BGB (Sonderregeln)
- Wohnraummiete: §§ 549 ff. BGB, § 558 BGB (Kappungsgrenze), §§ 555b ff. BGB (Modernisierung), §§ 573 ff. BGB (Kuendigung)
- WEG-Verwaltervertrag: §§ 26 ff. WEG, § 19 Abs. 2 Nr. 6 WEG

## Kommentarliteratur

- Schmidt-Futterer, Mietrecht, 15. Aufl. — § 550 BGB Rn. 1 ff. Schriftform
- BeckOK Mietrecht — § 557b BGB Indexmiete
- Staudinger, BGB §§ 535 ff. — Gewerberaummiete
- Grueenberg, BGB, 83. Aufl. — §§ 437 ff. Sachmangelhaftung Grundstueck

## Integration mit Projekten und Agenten

Der Skill ist so gebaut, dass er in einem Projekt-Ordner mit fixiertem
Playbook und Vertragstyp laeuft. Ein Agent kann auf eingehende Vertraege
auf einem Watch-Ordner reagieren und automatisch die Pruefung anstossen.
Siehe Skill `projekt-arbeitsweise`.
