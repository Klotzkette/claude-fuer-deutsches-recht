---
name: case-management
description: "Fallmanagement fuer Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Ueberblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Pruefraster: Fristenliste, offene Antraege, Dokumentenstruktur. Output: Case-Management-Uebersicht Immobilienrecht. Abgrenzung: nicht Einzelvertragspruefung."
---

# Case Management Immobilienrecht

## Leitidee

Eine Rechtsabteilung verliert mehr Zeit mit Suchen und
Status-Reproduktion als mit der eigentlichen rechtlichen Arbeit. Der
Skill konsolidiert pro Fall den aktuellen Stand auf einer Seite,
führt einen Fristenkalender und eine Ereignistabelle und schreibt
beides bei jedem neuen Eingang fort.

## Inputs

- Aktenbestandteile in beliebiger Form: Verträge Schriftsätze
  Korrespondenz Gutachten Fotos Hausverwaltungs-Berichte
- Optional: bestehende Fallübersicht zur Fortschreibung
- Optional: Recherche-Auftrag für aktuelle Rechtsprechung

## Output je Fall

- `Fall_<Aktenzeichen>.md` — eine Seite Fallübersicht mit
  - Beteiligte (Mandant Gegenseite Vertreter Gericht)
  - Streitgegenstand und Streitwert
  - Aktueller Verfahrensstand
  - Nächste Schritte mit Verantwortlichem
  - Risiko-Ampel
- `Fristen_<Aktenzeichen>.md` — Tabelle Frist — Datum —
  Rechtsgrundlage — Status
- `Ereignisse_<Aktenzeichen>.md` — chronologische Tabelle aller
  Vorgänge mit Quellenverweis auf Aktenstelle
- Optional `Rechtsprechung_<Aktenzeichen>.md` — kuratierte
  BGH-Entscheidungen zum Fall mit Pinpoint-Zitat und
  Risiko-Einordnung

## Methodik

1. Eingangsdokument klassifizieren (Schreiben Vertrag Schriftsatz
   Urteil Gutachten Foto)
2. Tatsachen extrahieren mit Quellenangabe in eckigen Klammern
3. Fristen und Termine berechnen — gesetzliche Fristen aus
   Vorschrift abgeleitet, gerichtliche aus Verfügung
4. Risiko-Ampel pro Fall: GRUEN beherrschbar, GELB beobachten,
   ROT Eskalation
5. Bei Nachlieferung: bestehende Markdown-Dateien werden ergänzt,
   neue Einträge mit `[NEU]` markiert
6. Auf Wunsch: aktuelle Rechtsprechung recherchieren und mit
   Pinpoint-Zitierung anhängen (juengere zuerst Randnummer)

## Zusammenfassung umfangreicher Dokumente

Der Skill kann lange Schriftsätze Gutachten und Urteile
zusammenfassen. Format pro Dokument:

- Kernaussage in zwei Sätzen
- Relevante Tatsachen mit Quellenangabe (Randnummer Seite)
- Rechtliche Würdigung in Stichpunkten
- Bezug zum eigenen Fall mit Ampel

Bei Urteilen wird die Pinpoint-Zitierung sauber gesetzt — Gericht
Datum Aktenzeichen Fundstelle Randnummer.

## Rechtsprechungs-Recherche mit Risiko-Einordnung

Auf Anfrage sucht der Skill aktuelle Rechtsprechung zum
Streitgegenstand. Format pro Entscheidung:

- BGH oder OLG mit Datum Aktenzeichen Fundstelle Randnummer
- Sachverhalts-Kern in zwei Sätzen
- Rechtssatz wortgetreu mit Anführungszeichen und Randnummer
- Bezug zum eigenen Fall — staerkt oder schwaecht die eigene
  Position
- Ampel ROT GELB GRUEN aus Sicht des Mandanten

Halluzinations-Regel: nur Entscheidungen die existieren und mit
verifizierbarer Fundstelle vorliegen. Bei Unsicherheit Markierung
`[Quelle zu verifizieren]`.

## Typische Fristen im Immobilienrecht

- Widerspruch Eigenbedarfskündigung § 574b BGB — spätestens zwei
  Monate vor Beendigung
- Mieterhöhungsverlangen § 558b BGB — Zustimmungsfrist zwei
  Monate
- Schönheitsreparaturen-Endabrechnung — Abrechnung der
  Betriebskosten § 556 Abs. 3 BGB binnen zwölf Monaten
- Mietkautionsrückforderung — angemessene Prüfungsfrist nach
  Auszug
- Anfechtung WEG-Beschluss § 45 WEG — ein Monat ab Beschlussfassung
- Schriftform Gewerbemietvertrag § 550 BGB bei Nachtraegen
- Verjährung Mietminderung § 548 BGB — sechs Monate nach
  Rückgabe der Mietsache
- Auskunftsverlangen Mietpreisbremse § 556g Abs. 3 BGB

## Beispielformulierungen

- "Lege Fall Mueller gegen Hausverwaltung Berlin an. Hier sind
  alle Unterlagen."
- "Schreibe Fall ABC GmbH gegen XY fort. Hier ist die neue
  Klageerwiderung."
- "Recherchiere aktuelle BGH-Rechtsprechung zu Schimmel und
  Beweislast. Ordne jede Entscheidung mit Ampel ein."
- "Fasse das 80-Seiten-Gutachten in einer Seite zusammen mit
  Bezug zum Fall."

## Aktuelle Rechtsprechung — Leitsaetze fuer Case-Management

- BGH, Urt. v. 12.10.2022 — VIII ZR 221/21, NJW 2023, 150 Rn. 18: Fristen im Mietrecht sind starre Ausschlussfristen; Versaeumung der Einwendungsfrist gegen Betriebskostenabrechnung (§ 556 Abs. 3 Satz 5 BGB — 12 Monate nach Zugang) fuehrt zum Anspruchsverlust.
- BGH, Urt. v. 13.01.2021 — VIII ZR 66/19, NJW 2021, 1021 Rn. 25: WEG-Beschlussanfechtungsklage muss innerhalb eines Monats ab Beschlussfassung erhoben und innerhalb zwei weiterer Monate begruendet werden (§ 45 WEG); keine Wiedereinsetzung bei anwaltlicher Versaeumung.
- BGH, Urt. v. 22.03.2024 — V ZR 81/22, NJW 2024, 1876: Gemeindliches Vorkaufsrecht bei Kaufvertraegen muss innerhalb von zwei Monaten nach Mitteilung ausgeubt werden; Fristen-Tracking im Case-Management ist kritisch.

## Relevante Fristen im Immobilienrecht

| Frist | Norm | Dauer |
|-------|------|-------|
| WEG-Beschlussanfechtung | § 45 WEG | 1 Monat ab Beschlussfassung |
| Betriebskosten-Einwendung | § 556 Abs. 3 Satz 5 BGB | 12 Monate nach Zugang |
| Vorkaufsrecht Gemeinde | §§ 24 ff. BauGB | 2 Monate nach Mitteilung |
| Mietkaution-Abrechnung | § 551 Abs. 3 BGB | Ca. 6 Monate nach Auszug |
| Verjaehrung Mietforderung | §§ 195, 199 BGB | 3 Jahre ab Jahresende |
