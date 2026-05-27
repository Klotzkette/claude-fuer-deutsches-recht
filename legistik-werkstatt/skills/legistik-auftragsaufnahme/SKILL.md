---
name: legistik-auftragsaufnahme
description: "Legistischen Auftrag strukturiert aufnehmen und in operationale Regelungsziele umwandeln. Anwendungsfall Erstkontakt zu einem neuen legistischen Vorhaben Koalitionsvertrag Beschluss Kabinett Landtag Aufsichtsweisung liegt vor. Klaert Adressaten Eingriffstiefe deklaratorisch oder konstitutiv Dringlichkeit Eckpunktepapier Referentenentwurf Formulierungshilfe Kabinettsentwurf Norm-Ebene Verfassungs- und EU-Bezug Zeitplan Beteiligte. Output Auftragsblatt mit zehn Fragen. Anschluss normhierarchie-routing. Abgrenzung zu normenkartierung bestehende Normen kartieren."
---

# Legistik-Auftragsaufnahme

> Erster Skill bei jedem neuen legistischen Vorhaben. Vor Normwahl, vor Entwurf, vor allem.

## Eingaben

- politische Vorgabe (Koalitionsvertrag, Kabinettsbeschluss, Landtagsantrag, Bürgermeisterbeschluss, Aufsichtsweisung)
- Auftraggeber (Hausleitung, Fachreferat, Land, Kommune)
- Adressat der Vorgabe (Bundestag, Bundesrat, Landtag, Stadtrat, Kammer-Vollversammlung)

## Vorgehen

### Schritt 1 - Was ist das politische Ziel?

Wer soll wozu verpflichtet oder ermaechtigt werden? Was soll verboten, was erlaubt werden?

### Schritt 2 - Wer ist Adressat der neuen Regel?

- Bürger (Grundrechtseingriff bedacht?)
- Unternehmen (Erfüllungsaufwand bedacht?)
- Verwaltung (Vollzugsaufwand bedacht?)
- Gerichte (gerichtliche Pruefbarkeit klar?)

### Schritt 3 - Wie tief greift die Regel ein?

- deklaratorisch (nur klarstellend, keine neuen Pflichten)
- konstitutiv (begründet neue Rechte oder Pflichten)
- modifizierend (aendert bestehende Pflichten)

### Schritt 4 - Wie eilig ist die Vorgabe?

- Eckpunktepapier (Phase 1) - politische Klärung
- Referentenentwurf (Phase 2) - mit Begründung, Verbändeanhörung
- Kabinettsentwurf (Phase 3) - nach Ressortabstimmung
- Formulierungshilfe (Phase 4) - aus der Mitte des Bundestages/Landtags (umgeht Ressortabstimmung und NKR-Prüfung)
- Eilgesetzgebung (Phase 5) - Fristverkürzungen

### Schritt 5 - Was ist die Norm-Ebene? Vorab-Routing

Welche Stufe ist plausibel? Bundesgesetz, Landesgesetz, Rechtsverordnung Bund, Rechtsverordnung Land, Satzung. Endgültige Antwort gibt Skill `normhierarchie-routing`.

### Schritt 6 - Auftragsblatt

| Feld | Inhalt |
|---|---|
| Aktenzeichen | (intern) |
| Bezeichnung des Vorhabens | |
| Politisches Ziel in einem Satz | |
| Adressat der Regelung | |
| Eingriffstiefe | |
| Norm-Ebene erste Einschätzung | |
| EU-Bezug ja/nein/unsicher | |
| Verfassungsbezug ja/nein/unsicher | |
| Folgen Bürger/Wirtschaft/Verwaltung | |
| Beteiligte Stellen | |
| Zeitplan | |

## Aktuelle Rechtsprechung & Leitsätze

- BVerfG, Beschl. v. 14.01.2015 — 1 BvR 931/12, BVerfGE 138, 261 Rn. 30 — Gesetzgebungsauftrag und Bestimmtheitsgrundsatz: Auftragsaufnahme muss Regelungszweck, Adressaten-Kreis und Grundrechtsbezug klaeren; unklarer Auftrag fuehrt regelmaessig zu normativer Unschaerfe im Entwurf
- BVerfG, Urt. v. 09.07.2007 — 2 BvF 1/04, BVerfGE 119, 59 Rn. 60 — Gesetzgeber muss bei Auftragsannahme die Kompetenz-Frage vorab klaeren; spaetere Ueberarbeitung eines inkompetenten Entwurfs nicht moeglich ohne erneutes Auftragsverfahren
- BGH, Urt. v. 22.10.2015 — III ZR 24/15, NJW 2016, 319 — Auftrag zur Rechtsetzung zwischen Auftraggeber und Rechtsberatung; Auftragsaufnahme-Protokoll ist Grundlage des Mandatsverhaeltnisses; unklare Auftragsabgrenzung kann Honoraranspruch gefahrden

## Zentrale Normen (Paragrafenkette)

§§ 14-20 GGO (Auftragsannahme ministerieller Rechtsetzungsauftrag) — Art. 76 Abs. 1 GG (Initiativrecht Bundesregierung) — §§ 611-630 BGB (Dienstvertrag, Mandatsrecht) — § 62 GGO (Checkliste Gesetzgebungsauftrag)

## Kommentarliteratur

- Schneider, Gesetzgebung, 3. Aufl. 2002, §§ 1-2 Rn. 1 ff. (Gesetzgebungsauftrag, Auftragsaufnahme-Systematik)
- Maurer/Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl. 2020, § 4 Rn. 1 ff. (Normgebungsauftrag und -programme)

## Ausgabe

Strukturiertes Auftragsblatt als Markdown, das durch alle weiteren Skills mitgeführt wird.

## Anschluss

- `normhierarchie-routing` - welche Norm-Ebene ist richtig
- `gesetzgebungskompetenz-pruefen` falls Gesetz
- `verordnungsermaechtigung-art80` falls VO
- `satzungskompetenz-pruefen` falls Satzung

## Stolperfallen

1. Politische Vorgaben sind oft unscharf - Legist muss klären, nicht erfinden, sondern beim Auftraggeber nachfragen
2. Politik will manchmal nicht eine Norm, sondern eine Geste - dann ist ein Schreiben oder Erlass besser als ein Gesetz
3. Zeitvorgabe prüfen - oft ist eine Formulierungshilfe schneller als ein Referentenentwurf
