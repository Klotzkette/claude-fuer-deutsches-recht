---
name: case-management
description: "Fallmanagement für Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Überblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Prüfraster: Fristenliste, offene Anträge, Dokumentenstruktur. Output: Case-Management-Übersicht Immobilienrecht. Abgrenzung: nicht Einzelvertragsprüfung."
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 45 WEG: Anfechtungsklage muss innerhalb eines Monats ab Beschlussfassung erhoben und innerhalb zweier Monate ab Beschlussfassung begruendet werden; beide Fristen sind materiell-rechtliche Ausschlussfristen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Relevante Fristen im Immobilienrecht

| Frist | Norm | Dauer |
|-------|------|-------|
| WEG-Beschlussanfechtung | § 45 WEG | 1 Monat ab Beschlussfassung |
| Betriebskosten-Einwendung | § 556 Abs. 3 Satz 5 BGB | 12 Monate nach Zugang |
| Vorkaufsrecht Gemeinde | §§ 24 ff. BauGB | 2 Monate nach Mitteilung |
| Mietkaution-Abrechnung | § 551 Abs. 3 BGB | Ca. 6 Monate nach Auszug |
| Verjaehrung Mietforderung | §§ 195, 199 BGB | 3 Jahre ab Jahresende |

<!-- AUDIT 27.05.2026 — Bundle 033 —
  Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->
