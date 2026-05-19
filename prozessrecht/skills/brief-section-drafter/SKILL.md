---
name: schriftsatzabschnitt
description: Entwurf eines Schriftsatzabschnitts im Kanzleistil, konsistent mit der Mandatstheorie – jede Tatsache belegt, jede Norm geprüft, jedes Argument an der Theorie verankert. Verwenden, wenn der Nutzer sagt „Entwurf [Abschnitt]", „schreib den Klagevortrag", „Berufungsbegründung zu [Punkt]" oder einen Ersterst-Entwurf eines Schriftsatzabschnitts benötigt.
language: de
triggers:
  - "schriftsatzabschnitt"
  - "klageschrift"
  - "klageerwiderung"
  - "berufungsbegründung"
  - "revisionsbegründung"
  - "schriftsatz entwerfen"
  - "abschnitt entwerfen"
---

# Schriftsatzabschnitt-Entwurf

## Zweck

Entwurf einzelner Abschnitte eines Schriftsatzes – Klageschrift, Klageerwiderung, Replik, Duplik, Berufungsbegründung (§ 520 ZPO), Revisionsbegründung (§ 551 ZPO), Beschwerdeerwiderung oder anderer Schriftsätze – im Urteilsstil nach deutschem Prozessrecht. Der Skill arbeitet mandatsspezifisch auf Basis der matter.md und history.md des aktiven Mandats und hält den Kanzleistil aus CLAUDE.md ein.

## Eingaben

- Aktives Mandat (Slug) mit matter.md und history.md
- Bezeichnung des gewünschten Abschnitts (z. B. „Sachverhaltsdarstellung", „Rechtliche Ausführungen zu Klageantrag 1", „Berufungsangriff I: Übergangener Beweisantrag")
- Anspruchstabelle (falls vorhanden, aus `/anspruchstabelle`)
- Chronologie (falls vorhanden, aus `/chronologie`)
- Beizufügende Dokumente / Anlagen (Vertrag, Schriftverkehr, Sachverständigengutachten)
- Gewünschte Schriftsatzart und verfahrensrechtliche Situation

## Ablauf

1. **Mandatsdaten laden:** matter.md, history.md, ggf. Chronologie und Anspruchstabelle einlesen. Mandatstheorie und Kanzleistil aus CLAUDE.md laden.

2. **Abschnittstyp bestimmen:**
   - **Klageschrift** (§§ 253, 261 ZPO): Rubrum, Anträge, Sachverhaltsdarstellung, Rechtliche Ausführungen, Beweisangebote.
   - **Klageerwiderung** (§ 277 ZPO): Bestreiten (erheblich/unerheblich), Gegendarstellung, Rechtsausführungen, eigene Anträge, Hilfsaufrechnung/Widerklage.
   - **Berufungsbegründung** (§ 520 Abs. 3 ZPO): Darlegung der Berufungsangriffe, Bezifferung von Rechtsverletzungen (§ 546 ZPO), neue Tatsachen und Beweise (§ 531 Abs. 2 ZPO), Berufungsanträge.
   - **Revisionsbegründung** (§ 551 Abs. 3 ZPO): Revisionsgründe (§ 545 ZPO), absolute Revisionsgründe (§ 547 ZPO), Rüge der Nichtzulassung (§ 544 ZPO), Grundsatzrevision (§ 543 Abs. 2 ZPO).
   - **Beschwerde** (§§ 567 ff., 574 ff. ZPO): Statthaftigkeit, Frist, Begründung.

3. **Urteilsstil anwenden:** Tatsachenvortrag in indirekter Rede oder Behauptungsform, normative Subsumtion knapp, Beweisangebote vollständig.

4. **Normen und Rechtsprechung einarbeiten:** Jede Behauptung rechtlicher Art mit Norm und – soweit verfügbar – BGH-Rechtsprechung nach Zitierweise (../references/zitierweise.md) belegen.

5. **Beweisangebote formulieren:** Für jeden bestrittenen Tatsachenbehauptung ein konkretes Beweisangebot (Zeugnis, Sachverständiger, Urkunde, Augenschein, Parteivernehmung § 447 ZPO, Geständnisfiktion § 138 Abs. 3 ZPO).

6. **Lückenprüfung:** Fehlende Tatsachenbehauptungen, unklare Beweisangebote, ungeklärte Passivlegitimation, fehlende Kausalität und Schaden als **[LÜCKE: …]** markieren.

7. **Entwurf ausgeben:** Urteilsstil, kanzleispezifisches Format, Fristen am Ende der Ausgabe.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

Einschlägige Kommentare und Rechtsprechung:

- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 253 Rn. 12 ff. (Klageschrift, Bestimmtheit der Anträge).
- Gruber, in: MüKoZPO, 6. Aufl. 2020, § 520 Rn. 30 ff. (Berufungsbegründung, Berufungsangriffe).
- Wulf, in: BeckOK ZPO, 52. Ed. (Stand 01.03.2024), § 520 Rn. 20 ff.
- BGH, Urt. v. 26.04.2023 – VIII ZR 121/22, NJW 2023, 2253 Rn. 18 (Schlüssigkeit der Klageschrift).
- BGH, Urt. v. 19.01.2022 – IV ZR 295/19, NJW 2022, 1097 Rn. 22 (Berufungsangriff, § 520 Abs. 3 Nr. 2 ZPO).
- BGH, Urt. v. 09.03.2021 – VI ZR 73/20, NJW 2021, 1886 Rn. 15 (neue Angriffsmittel § 531 ZPO).
- BGH, Beschl. v. 21.02.2017 – VIII ZB 74/16, NJW 2017, 2273 Rn. 14 (Anforderungen § 551 Abs. 3 ZPO).
- Heßler, in: Zöller, ZPO, 35. Aufl. 2024, § 520 Rn. 28 ff.
- Steinmetz, in: Musielak/Voit, ZPO, 21. Aufl. 2024, § 520 Rn. 15 ff.

## Ausgabeformat

Schriftsatzformat im deutschen Standard:
1. **Rubrum** (Gericht, Parteien, Az., Datum) – sofern vollständiger Schriftsatz
2. **Abschnittsüberschrift** (z. B. „I. Sachverhaltsdarstellung", „III. Zum Berufungsangriff")
3. **Fließtext im Urteilsstil** mit Randnummern (fakultativ)
4. **Beweisangebote** am Ende jedes bestrittenen Tatsachenblocks
5. **Lücken-Notizen** in Klammern: `[LÜCKE: Beleg für Fristversäumnis fehlt]`
6. **Fristenliste** am Ende des Outputs

## Beispiel

> **III. Zur Berufungsbegründung – Verletzung des § 286 ZPO**
>
> Das Landgericht hat das Beweisangebot der Klägerin auf Vernehmung des Zeugen Müller (Schriftsatz v. 14.03.2023, S. 7) übergangen, ohne dies in den Entscheidungsgründen zu begründen. Dies verletzt Art. 103 Abs. 1 GG und § 286 Abs. 1 ZPO.
>
> Nach ständiger Rechtsprechung des BGH ist ein Beweisangebot nur dann ohne Fehler übergehen, wenn es entweder unerheblich, unzulässig oder eindeutig untauglich ist (BGH, Urt. v. 29.03.2023 – IV ZR 28/22, NJW 2023, 1891 Rn. 23; Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 286 Rn. 14). Keine dieser Voraussetzungen liegt hier vor.
>
> *Beweis: Zeugnis des Herrn Max Müller, [Anschrift] – Beweis-Nr. 5.*

## Risiken / typische Fehler

- **Unbestimmter Antrag** (§ 253 Abs. 2 Nr. 2 ZPO): Der Klageantrag muss vollstreckbar formuliert sein; das Gericht darf nicht selbst nach billigem Ermessen ergänzen (BGH, Urt. v. 26.04.2023 – VIII ZR 121/22, NJW 2023, 2253 Rn. 18).
- **Berufungsbegründungsfrist:** § 520 Abs. 2 ZPO: 2 Monate ab Urteilszustellung; verlängerbar auf Antrag, aber nur mit gegnerischer Zustimmung oder wichtigem Grund.
- **Neue Tatsachen in der Berufung:** § 531 Abs. 2 ZPO begrenzt neues Vorbringen; stets prüfen, ob Nachlässigkeit im ersten Rechtszug vorlag.
- **Revisionsanforderungen:** § 543 Abs. 2 ZPO – Grundsatzbedeutung oder Sicherung einheitlicher Rechtsprechung; ohne NZB-Begründung keine Revision (§ 544 ZPO).
- **Verstoß gegen § 138 ZPO:** Wahrheitspflicht; keine Behauptung ins Blaue hinein; Darlegungs- und Beweislast nicht verwechseln.
- **Berufsrechtliche Hinweispflicht:** Bei überraschenden Rechtswendungen ist der Mandant nach § 43 BRAO zu informieren; kein Schriftsatz ohne Rücksprache versenden.
