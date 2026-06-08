---
name: definitionen-klauseln-stringent
description: "Defined Terms in Vertraegen sauber bauen. Hierarchie und Konsistenz: einmal definieren, im gesamten Dokument einheitlich verwenden, mit Grossschreibung sichtbar machen. Trennung zwischen zentralem Definitionen-Abschnitt (alphabetisch) und Inline-Definitionen ('im Folgenden Vertrag'). Mit Beispielklauseln, Konsistenzpruefung per Suchen-Ersetzen-Logik und einem Katalog typischer Anti-Pattern wie verschachtelte Definitionen oder Definitionsdoppel im Word Legal Ai Plugin And Skill For German Lawyers."
---

# Definitionen-Klauseln stringent

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Vertragsentwurf oder Term Sheet
- Liste der zu definierenden Begriffe (oder Auftrag, sie zu identifizieren)
- Position im Vertrag: zentraler Abschnitt vs. Inline

## Rechtlicher und methodischer Rahmen

- § 305c Abs. 2 BGB: Unklarheitenregel zulasten des Verwenders. Inkonsistente Begriffe gehen zulasten des AGB-Verwenders.
- § 307 Abs. 1 Satz 2 BGB: Transparenzgebot. Defined Terms muessen klar verstaendlich definiert sein.
- §§ 133, 157 BGB: Vertragsauslegung. Defined Terms binden die Auslegung.
- Konvention: Defined Terms grossschreiben oder kursiv setzen, damit sie im Text sichtbar sind.

## Ablauf / Checkliste

1. **Begriffe identifizieren.** Welche Konzepte tauchen mehr als einmal auf? Welche tragen Rechtsfolgen?
2. **Zentral oder inline?** Faustregel: mehr als zehn Begriffe oder Verwendung in mehreren Klauseln, dann zentraler Definitionen-Abschnitt.
3. **Definitionsstruktur waehlen.** Alphabetisch (Default) oder thematisch (bei sehr grossen Vertraegen).
4. **Defined Term auszeichnen.** Grossschreibung des Anfangs ("Vertrag", "Vertragspartei", "Closing", "Long Stop Date") oder kursiv ("Vertrag").
5. **Definition formulieren.** Knapp, eindeutig, ohne andere Defined Terms zu verschachteln, wo unnoetig.
6. **Konsistenzpruefung durchfuehren.** Volltextsuche, jeder Defined Term im Dokument identisch geschrieben.
7. **Anti-Pattern checken.** Siehe unten.

### Beispielklauseln

**Zentraler Definitionen-Abschnitt:**

```
§ 1 Definitionen

In diesem Vertrag haben die folgenden Begriffe die nachstehende Bedeutung:

"Anlage" bezeichnet jede mit diesem Vertrag verbundene Anlage gemaess Anlagenverzeichnis.

"Bestellt" bezeichnet die Bestellung der Ware durch den Besteller gemaess § 3.

"Besteller" bezeichnet die [Besteller AG, Anschrift, HRB ...], die Partei dieses Vertrages ist.

"Closing" bezeichnet den Vollzug dieses Vertrages gemaess § 8.

"Lieferant" bezeichnet die [Lieferant GmbH, Anschrift, HRB ...], die Partei dieses Vertrages ist.

"Parteien" bezeichnet den Besteller und den Lieferanten gemeinsam; "Partei" bezeichnet jede der beiden.

"Vertrag" bezeichnet diese Vereinbarung einschliesslich aller Anlagen.

"Vertraulichkeitszeitraum" bezeichnet den in § 7 Abs. 3 definierten Zeitraum.
```

**Inline-Definition (Kurzvertrag):**

```
Zwischen der A-GmbH, Musterstrasse 1, 10115 Berlin (im Folgenden "Lieferant"),
und der B-AG, Beispielstrasse 2, 20095 Hamburg (im Folgenden "Besteller"),
wird folgender Liefervertrag (im Folgenden "Vertrag") geschlossen.
```

### Konsistenzpruefung

| Schritt | Suche | Erwartet |
|---|---|---|
| 1 | "Vertragspartei" | nicht vorhanden, wenn "Partei" definiert ist |
| 2 | "Vereinbarung" | nicht vorhanden im operativen Text, wenn "Vertrag" definiert ist |
| 3 | "vorliegender Kontrakt" | streichen |
| 4 | "Liefergegenstand" und "Ware" | nur einer als Defined Term zulaessig |
| 5 | "Besteller" und "Auftraggeber" | nur einer |

### Anti-Pattern

- **Verschachtelte Definitionen.** "Vertrag bezeichnet diese Vereinbarung einschliesslich aller Anlagen, soweit nichts anderes bestimmt ist." Streichen Sie den Soweit-Zusatz oder definieren Sie ihn explizit.
- **Definitionsdoppel.** "Lieferant" im Vorspann und nochmal in § 1.
- **Wechselnde Schreibweise.** "Closing" und "closing" sind unterschiedliche Begriffe in der Volltextsuche.
- **Zirkulaere Definitionen.** "Lieferung" bezeichnet die Lieferung der Ware. Streichen oder funktional definieren.
- **Ungenutzte Defined Terms.** Wer definiert, soll auch verwenden. Sonst streichen.

## Typische Drafting-Fehler

- Zentrale Definitionen ohne Auszeichnung. Defined Terms verschwinden im Fliesstext.
- Falsche Reihenfolge. Begriffe werden verwendet, bevor sie definiert sind. Loesung: vorne definieren oder Defined Term mit Verweis "(siehe § 12)" einfuehren.
- Klein- statt Grossschreibung im Defined Term. "Vertrag" und "vertrag" sind nicht dasselbe.
- Definitionen, die selbst Rechtsfolgen anordnen. Definitionen definieren, sie regeln nicht. "Lieferzeit bezeichnet vier Wochen; bei Verzug schuldet der Lieferant Schadensersatz." Die Schadensersatzregelung gehoert in die operative Klausel.
- Defined Terms in der Praeambel. Praeambel ist Kontext, nicht Regelung.

## Beispiel

**Aufgabe:** "Bauen Sie aus folgendem Term Sheet einen Definitionen-Abschnitt: Lieferant ist eine GmbH, Besteller eine AG, Liefergegenstand sind Industrieventile, Closing erfolgt am Long Stop Date oder spaeter, Anlage 1 enthaelt die technische Spezifikation."

**Loesung:**

```
§ 1 Definitionen

"Anlage 1" bezeichnet die technische Spezifikation des Liefergegenstandes.

"Besteller" bezeichnet die [Besteller AG, Anschrift, HRB ...].

"Closing" bezeichnet den Vollzug dieses Vertrages gemaess § 8.

"Liefergegenstand" bezeichnet die in Anlage 1 spezifizierten Industrieventile.

"Lieferant" bezeichnet die [Lieferant GmbH, Anschrift, HRB ...].

"Long Stop Date" bezeichnet den 31. Dezember 2026.

"Parteien" bezeichnet den Besteller und den Lieferanten gemeinsam.

"Vertrag" bezeichnet diese Vereinbarung einschliesslich aller Anlagen.
```

## Quellen (Stand 05/2026)

- § 305c Abs. 2 BGB, § 307 Abs. 1 Satz 2 BGB, §§ 133, 157 BGB. gesetze-im-internet.de.
- Konvention zur Defined-Terms-Auszeichnung folgt internationaler M&A-Praxis und ist in deutscher Wirtschaftsvertragsgestaltung etabliert. Konkretes Hauskonvention je Kanzlei pruefen.

