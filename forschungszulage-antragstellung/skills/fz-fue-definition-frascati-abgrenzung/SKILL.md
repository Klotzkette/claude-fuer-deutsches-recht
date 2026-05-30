---
name: fz-fue-definition-frascati-abgrenzung
description: "FuE-Definition für die Forschungszulage praxisnah prüfen: Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung, Frascati-Kriterien (Neuheit, Schöpferisch, Ungewissheit, Systematik, Reproduzierbarkeit), AGVO-Definitionen, Abgrenzung zu Routineentwicklung, Customizing, Bugfixing und Serienpflege. Mit Mustersätzen für die BSFZ-Projektbeschreibung."
---

# FuE-Definition und Abgrenzung nach Frascati

## Worum geht es

Die BSFZ entscheidet, ob ein Vorhaben Forschung und Entwicklung im Sinne des FZulG ist. Sie wendet die Definitionen der AGVO (Art. 2 Nr. 84 bis 86) an, die wiederum auf dem OECD-Frascati-Handbuch beruhen. Dieser Skill liefert die Frascati-Kriterien praxisnah, Abgrenzungsfälle, Software-Spezifika und Mustersätze für die Projektbeschreibung.

## Wann brauchen Sie diesen Skill

- Vor dem Schreiben einer BSFZ-Projektbeschreibung, wenn unklar ist, ob das Vorhaben förderfähig ist.
- Bei Streit Auftraggeber-Auftragnehmer: was darf als FuE-Anteil angesetzt werden?
- Bei BSFZ-Rückfrage zur FuE-Eigenschaft.
- Bei Software-Vorhaben, weil Abgrenzung dort am schwierigsten ist.

## Die fünf Frascati-Kriterien

Ein Vorhaben gilt als FuE, wenn es kumulativ:

1. **Neuartig (novel)** ist — neuer Erkenntnisgewinn, keine bloße Anwendung bekannten Wissens.
2. **Schöpferisch (creative)** ist — nicht-triviale konzeptionelle Eigenleistung.
3. **Ungewiss (uncertain)** im Ergebnis ist — technisches Scheitern ist denkbar, Lösungsweg nicht determiniert.
4. **Systematisch (systematic)** durchgeführt wird — geplant, dokumentiert, mit Arbeitspaketen.
5. **Übertragbar/Reproduzierbar (transferable, reproducible)** ist — andere Fachleute könnten die Ergebnisse nachvollziehen.

Die BSFZ verlangt nicht jedes Kriterium gleich stark, aber die Trias **Neuheit + Ungewissheit + Systematik** muss klar erkennbar sein.

## Sachrahmen: drei FuE-Kategorien

- **Grundlagenforschung (Art. 2 Nr. 84 AGVO):** Erkenntnisgewinn ohne unmittelbare praktische Anwendung. Selten in der mittelständischen Praxis.
- **Industrielle Forschung (Art. 2 Nr. 85 AGVO):** Erkenntnisgewinn für neue Produkte, Verfahren oder Dienstleistungen.
- **Experimentelle Entwicklung (Art. 2 Nr. 86 AGVO):** Anwendung von Erkenntnissen für Prototypen, Demonstratoren, Pilotprodukte — ohne kommerzielle Serienreife.

In der Mittelstandspraxis dominieren Punkt 2 und Punkt 3.

## Praxisleitfaden — die Abgrenzungsfälle der alten Hasen

### Was schnell durchgeht

- **Algorithmus erreicht Zielgenauigkeit nicht mit bekannten Verfahren.** Konkret: Erkennungsrate, Latenz, Energiebudget. Beispiel: "Stand der Technik liefert 87 Prozent Erkennungsrate bei [Klasse], Zielwert 95 Prozent ist mit bestehenden Verfahren nicht erreichbar."
- **Material-/Prozessparameter sind unklar.** Beispiel: neue Legierung, neuer Sinterprozess, unklare Festigkeit unter Wärmebelastung.
- **Prototyp scheitert an Skalierung.** Beispiel: Laborprozess funktioniert bei 5 Liter, bei 5000 Liter unklar.
- **Konstruktion mit echter Funktionsneuheit.** Nicht: ein Bauteil größer dimensionieren. Doch: ein Bauteil mit Funktion XY, die so nicht existiert.

### Was die BSFZ-Prüfer triggert (rote Flaggen)

- **"Innovative Plattform"** ohne erklärten technischen Inhalt.
- **"KI-basiert"** ohne ML-Konzept, ohne Datenmenge, ohne Trainingsproblem.
- **"Industrie 4.0"** als Schlagwort, statt konkret zu beschreiben, welche Steuerungs- oder Sensorprobleme gelöst werden.
- **Fehlende Abgrenzung zu Routine.** Wenn die Projektbeschreibung das Serienpflege-/Wartungs-Konzept und das FuE-Vorhaben vermischt, hagelt es Rückfragen.
- **Lastenheft mit Anforderungs-Liste** statt FuE-Vorgehen. "Soll X können, soll Y unterstützen" ist Kundenmanagement, keine Forschung.
- **Marketing-Sprache.** "Disruptive Lösung", "smart", "next-generation" — sofort streichen.

### Rote Flaggen — Anti-Pattern, die wir oft sehen

- Reines Customizing einer Standard-Software (SAP, Salesforce, AX).
- Routine-Bugfixing, auch wenn es lange dauert.
- Lieferantenwechsel ohne technischen Erkenntnisgewinn.
- Serienpflege, Dokumentation, Schulung, Vertriebsmaterial.
- "Wir haben das noch nie gemacht" als einzige Begründung für Neuheit (Maßstab ist objektiver Stand der Technik, nicht der hauseigene).
- Migration einer Anwendung auf eine andere Datenbank/Cloud.
- UI-Refactor, Style-Update, neue Frontend-Library.

### Software-Spezifika (häufiges Streitfeld)

- **Förderfähig:** neuer Algorithmus, neues Datenmodell, neuartige Optimierungstechnik, neues ML-Verfahren mit eigenem Trainings- oder Architekturkonzept, eigene Inferenz-Beschleunigung.
- **Nicht förderfähig:** Wechsel auf eine neue UI-Bibliothek (React/Vue/Angular), Migration der Build-Pipeline, Refactoring zur Wartbarkeit, Standard-Cloud-Migration.
- **Grenzfall:** neues Architekturkonzept (z. B. Event-Sourcing, CQRS) — nur förderfähig, wenn dadurch ein konkretes technisches Problem gelöst wird, das mit klassischer Architektur nicht lösbar wäre.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Gesamtprojekt vs. FuE-Anteil | gesamtes Projekt einreichen | nur FuE-Anteile separieren | nur FuE-Anteile, sauber abgegrenzt |
| Routine + FuE in einem Antrag | gemeinsam | getrennt | getrennt, sonst gefährdet Routine die ganze BSFZ |
| Konservative Beschreibung vs. großzügig | kleinere Förderung, sichere BSFZ | mehr Förderung, höheres Ablehnungsrisiko | konservativ beim Erstantrag |

## Schritt für Schritt — FuE-Memo erstellen

1. Vorhaben in einem Satz beschreiben (nicht Produkt, sondern Problem).
2. Stand der Technik mit zwei oder drei konkreten Quellen benennen (Norm, Publikation, Patent, Wettbewerbsprodukt).
3. Neuheit gegenüber Stand der Technik herausarbeiten.
4. Technische Unsicherheit nennen: was kann scheitern, woran erkennen Sie das?
5. Systematischen Lösungsweg in Arbeitspaketen.
6. Routine-Anteile offen benennen und herausrechnen.
7. Frascati-Kriterien einzeln durchgehen und je Kriterium ein bis zwei Sätze formulieren.

## Mustertexte für die BSFZ-Projektbeschreibung

**Ausgangsproblem:**

"Im Bereich [Domäne] erreicht der bestehende Stand der Technik (siehe [Quelle 1, Quelle 2]) eine [Messgröße] von [Wert]. Für [Zielanwendung] ist ein Wert von mindestens [Zielwert] erforderlich. Mit bekannten Verfahren ist diese Schwelle nach unseren Voruntersuchungen nicht erreichbar."

**Neuheit:**

"Wir untersuchen [konkretes Verfahren / konkrete Architektur]. Im Unterschied zum Stand der Technik kombinieren wir [A] mit [B] — diese Kombination ist nach unserem Kenntnisstand bislang nicht veröffentlicht."

**Technische Unsicherheit:**

"Es ist offen, ob [Bedingung X] unter [Randbedingung Y] erreicht werden kann. Insbesondere [konkrete Hürde, z. B. Konvergenz, Festigkeit, Latenz] kann zum Scheitern führen. Vergleichbare Vorhaben in der Literatur scheiterten an [Bezug]."

**Systematisches Vorgehen:**

"Das Vorhaben gliedert sich in Arbeitspakete (siehe Tabelle). Jedes Arbeitspaket schließt mit einem definierten Meilenstein und Erfolgskriterium. Negative Ergebnisse werden dokumentiert; bei Abbruchkriterien wird ein Decision-Gate ausgelöst."

## Typische Fehler

- "Wir entwickeln eine moderne Plattform für ..." — Marketing, keine FuE.
- "Wir verwenden KI, um ..." — was ist das ML-Konzept? Trainingsdaten? Erfolgsmaß?
- "Innovativ" als Adjektiv, nirgends operationalisiert.
- Stand der Technik nicht zitiert.
- Risiko nur generisch ("Risiken bestehen").

## Output

FuE-Memo mit:

- Kategorie (Grundlagenforschung / industrielle Forschung / experimentelle Entwicklung).
- tragenden Tatsachen pro Frascati-Kriterium.
- Nicht-FuE-Anteilen.
- Belegbedarf.
- BSFZ-tauglichen Formulierungen für Ausgangsproblem, Neuheit, Unsicherheit, Systematik.

## Querverweise

- `fz-bsfz-bescheinigung-projektbeschreibung` für die volle Projektbeschreibung.
- `fz-foerdercheck-kaltstart` für die schnelle Erstabschätzung.
- `fz-ablehnung-nachbesserung-einspruch` wenn BSFZ Nachfragen zur FuE-Eigenschaft stellt.

## Quellen Stand 05/2026

- AGVO Verordnung (EU) 651/2014, Art. 2 Nr. 84 bis 86 (vom Antragsteller mit konsolidierter Fassung zu prüfen).
- OECD Frascati-Handbuch (Frascati Manual 2015).
- BSFZ-Hilfen zur Antragstellung: https://www.bescheinigung-forschungszulage.de/hilfen-zur-antragstellung
- FZulG: https://www.gesetze-im-internet.de/fzulg/
