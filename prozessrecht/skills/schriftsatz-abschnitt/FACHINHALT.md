---
name: schriftsatz-abschnitt
description: "Für Schriftsatzabschnitt-Entwurf: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik."
---

# Schriftsatzabschnitt-Entwurf

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Aktives Mandat (Slug) mit mandat.md und verlauf.md
- Bezeichnung des gewünschten Abschnitts (z. B. "Sachverhaltsdarstellung", "Rechtliche Ausführungen zu Klageantrag 1", "Berufungsangriff I: Übergangener Beweisantrag")
- Anspruchstabelle (falls vorhanden, aus `/anspruchstabelle`)
- Chronologie (falls vorhanden, aus `/chronologie`)
- Beizufügende Dokumente / Anlagen (Vertrag, Schriftverkehr, Sachverständigengutachten)
- Gewünschte Schriftsatzart und verfahrensrechtliche Situation

## Ablauf

1. **Mandatsdaten laden:** mandat.md, verlauf.md, ggf. Chronologie und Anspruchstabelle einlesen. Mandatstheorie und Kanzleistil aus CLAUDE.md laden.

2. **Abschnittstyp bestimmen:**
 - **Klageschrift** (Paragrafen 253, 261 ZPO): Rubrum, Anträge, Sachverhaltsdarstellung, Rechtliche Ausführungen, Beweisangebote.
 - **Klageerwiderung** (Paragraf 277 ZPO): Bestreiten (erheblich/unerheblich), Gegendarstellung, Rechtsausführungen, eigene Anträge, Hilfsaufrechnung/Widerklage.
 - **Berufungsbegründung** (Paragraf 520 Abs. 3 ZPO): Darlegung der Berufungsangriffe, Bezifferung von Rechtsverletzungen (Paragraf 546 ZPO), neue Tatsachen und Beweise (Paragraf 531 Abs. 2 ZPO), Berufungsanträge.
 - **Revisionsbegründung** (Paragraf 551 Abs. 3 ZPO): Revisionsgründe (Paragraf 545 ZPO), absolute Revisionsgründe (Paragraf 547 ZPO), Rüge der Nichtzulassung (Paragraf 544 ZPO), Grundsatzrevision (Paragraf 543 Abs. 2 ZPO).
 - **Beschwerde** (Paragrafen 567 ff., 574 ff. ZPO): Statthaftigkeit, Frist, Begründung.

3. **Urteilsstil anwenden:** Tatsachenvortrag in indirekter Rede oder Behauptungsform, normative Subsumtion knapp, Beweisangebote vollständig.

4. **Normen und Rechtsprechung einarbeiten:** Jede Behauptung rechtlicher Art mit Norm und – soweit verfügbar – BGH-Rechtsprechung nach Zitierweise (../references/zitierweise.md) belegen.

5. **Beweisangebote formulieren:** Für jeden bestrittenen Tatsachenbehauptung ein konkretes Beweisangebot (Zeugnis, Sachverständiger, Urkunde, Augenschein, Parteivernehmung Paragraf 447 ZPO, Geständnisfiktion Paragraf 138 Abs. 3 ZPO).

6. **Lückenprüfung:** Fehlende Tatsachenbehauptungen, unklare Beweisangebote, ungeklärte Passivlegitimation, fehlende Kausalität und Schaden als **[LÜCKE: …]** markieren.

7. **Entwurf ausgeben:** Urteilsstil, kanzleispezifisches Format, Fristen am Ende der Ausgabe.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

Einschlägige Kommentare und Rechtsprechung:

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispiel

> **III. Zur Berufungsbegründung – Verletzung des Paragraf 286 ZPO**
>
> Das Landgericht hat das Beweisangebot der Klägerin auf Vernehmung des Zeugen Müller (Schriftsatz v. 14.03.2023, S. 7) übergangen, ohne dies in den Entscheidungsgründen zu begründen. Dies verletzt Art. 103 Abs. 1 GG und Paragraf 286 Abs. 1 ZPO.
>
>
> *Beweis: Zeugnis des Herrn Max Müller, [Anschrift] – Beweis-Nr. 5.*

## Risiken / typische Fehler

- **Berufungsbegründungsfrist:** Paragraf 520 Abs. 2 ZPO: 2 Monate ab Urteilszustellung; verlängerbar auf Antrag, aber nur mit gegnerischer Zustimmung oder wichtigem Grund.
- **Neue Tatsachen in der Berufung:** Paragraf 531 Abs. 2 ZPO begrenzt neues Vorbringen; stets prüfen, ob Nachlässigkeit im ersten Rechtszug vorlag.
- **Revisionsanforderungen:** Paragraf 543 Abs. 2 ZPO – Grundsatzbedeutung oder Sicherung einheitlicher Rechtsprechung; ohne NZB-Begründung keine Revision (Paragraf 544 ZPO).
- **Verstoß gegen Paragraf 138 ZPO:** Wahrheitspflicht; keine Behauptung ins Blaue hinein; Darlegungs- und Beweislast nicht verwechseln.
- **Berufsrechtliche Hinweispflicht:** Bei überraschenden Rechtswendungen ist der Mandant nach Paragraf 43 BRAO zu informieren; kein Schriftsatz ohne Rücksprache versenden.

---

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
