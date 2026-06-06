---
name: schriftsatz-abschnitt
description: "Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in Klageschrift oder Erwiderung. Abgrenzung: nicht vollständige Klageschrift im Prozessrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Schriftsatzabschnitt-Entwurf

## Arbeitsbereich

Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in Klageschrift oder Erwiderung. Abgrenzung: nicht vollständige Klageschrift. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Entwurf einzelner Abschnitte eines Schriftsatzes – Klageschrift, Klageerwiderung, Replik, Duplik, Berufungsbegründung (§ 520 ZPO), Revisionsbegründung (§ 551 ZPO), Beschwerdeerwiderung oder anderer Schriftsätze – im Urteilsstil nach deutschem Prozessrecht. Der Skill arbeitet mandatsspezifisch auf Basis der mandat.md und verlauf.md des aktiven Mandats und hält den Kanzleistil aus CLAUDE.md ein.

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

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

Schriftsatzformat im deutschen Standard:
1. **Rubrum** (Gericht, Parteien, Az., Datum) – sofern vollständiger Schriftsatz
2. **Abschnittsüberschrift** (z. B. "I. Sachverhaltsdarstellung", "III. Zum Berufungsangriff")
3. **Fließtext im Urteilsstil** mit Randnummern (fakultativ)
4. **Beweisangebote** am Ende jedes bestrittenen Tatsachenblocks
5. **Lücken-Notizen** in Klammern: `[LÜCKE: Beleg für Fristversäumnis fehlt]`
6. **Fristenliste** am Ende des Outputs

## Beispiel

> **III. Zur Berufungsbegründung – Verletzung des § 286 ZPO**
>
> Das Landgericht hat das Beweisangebot der Klägerin auf Vernehmung des Zeugen Müller (Schriftsatz v. 14.03.2023, S. 7) übergangen, ohne dies in den Entscheidungsgründen zu begründen. Dies verletzt Art. 103 Abs. 1 GG und § 286 Abs. 1 ZPO.
>
> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
>
> *Beweis: Zeugnis des Herrn Max Müller, [Anschrift] – Beweis-Nr. 5.*

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Berufungsbegründungsfrist:** § 520 Abs. 2 ZPO: 2 Monate ab Urteilszustellung; verlängerbar auf Antrag, aber nur mit gegnerischer Zustimmung oder wichtigem Grund.
- **Neue Tatsachen in der Berufung:** § 531 Abs. 2 ZPO begrenzt neues Vorbringen; stets prüfen, ob Nachlässigkeit im ersten Rechtszug vorlag.
- **Revisionsanforderungen:** § 543 Abs. 2 ZPO – Grundsatzbedeutung oder Sicherung einheitlicher Rechtsprechung; ohne NZB-Begründung keine Revision (§ 544 ZPO).
- **Verstoß gegen § 138 ZPO:** Wahrheitspflicht; keine Behauptung ins Blaue hinein; Darlegungs- und Beweislast nicht verwechseln.
- **Berufsrechtliche Hinweispflicht:** Bei überraschenden Rechtswendungen ist der Mandant nach § 43 BRAO zu informieren; kein Schriftsatz ohne Rücksprache versenden.

---

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 73/20, NJW 2021, 1886 Rn. 15 (" neue Angriffsmittel § 531 ZPO ") – Zitatfehler (WRONG_TOPIC). Das Urteil behandelt Verletzung des allgemeinen Persönlichkeitsrechts / Bestimmtheit Klageantrags bei Erstbegehungsgefahr (NJW 2021, 1756), nicht neue Angriffsmittel nach § 531 ZPO (dejure.org/2021,4358). Eintrag ersatzlos gelöscht; kein verifizierbarer Ersatz mit identischem NJW-Fundstelle ermittelt.
Quelle : https://dejure.org/2021,4358
Aktion : Zeile entfernt
-->
