---
name: rueckausnahme-art-6-abs-3
description: "Prueft nach positiver Anhang-III-Zuordnung, ob ein KI-System ausnahmsweise nicht Hochrisiko ist. Art. 6 Abs. 3 KI-VO: kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte, vier enge Fallgruppen, Profiling-Sperre, Begruendungs- und Dokumentationspflicht nach Art. 6 Abs. 4. Besonders wichtig für allgemeine Assistenzsysteme, Chatbots und vorbereitende Tools in Personal, Justiz, Bildung, Kredit und Verwaltung. Output: begruendeter Rueckausnahme-Vermerk mit Risikobegruendung und Folge-Skills."
---

# Rückausnahme vom Hochrisiko — Art. 6 Abs. 3 KI-VO

## Zweck

Dieser Skill wird nur genutzt, wenn zuvor ein Anhang-III-Tatbestand nach Art. 6 Abs. 2 KI-VO möglich oder wahrscheinlich ist. Er prüft, ob das System ausnahmsweise nicht als Hochrisiko-KI-System gilt, weil es kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte darstellt und in eine der eng auszulegenden Fallgruppen fällt.

Der Skill ist besonders wichtig bei allgemeinen Assistenzsystemen, LLM-Tools, Chatbots und Dokumentationshilfen, die in sensiblen Bereichen eingesetzt werden, aber nur vorbereitende oder eng begrenzte Aufgaben erfüllen sollen.

## Prüfungsreihenfolge

1. Anhang-III-Treffer konkret benennen.
2. Profiling natürlicher Personen ausschließen.
3. Erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte bewerten.
4. Eine der vier Fallgruppen prüfen.
5. Tatsächliche Nutzung und vorhersehbaren Fehlgebrauch gegen die behauptete Rückausnahme halten.
6. Dokumentationspflicht nach Art. 6 Abs. 4 vorbereiten.

## Sperre: Profiling natürlicher Personen

Wenn das System Profiling natürlicher Personen vornimmt, greift die Rückausnahme nicht.

Prüfe:
- Werden personenbezogene Daten automatisiert verarbeitet?
- Werden persönliche Aspekte bewertet, analysiert oder vorhergesagt?
- Geht es um Leistung, wirtschaftliche Lage, Gesundheit, Präferenzen, Interessen, Zuverlässigkeit, Verhalten, Aufenthaltsort oder Bewegung?
- Hat der Output individualisierende Wirkung?

Bei Bewerberranking, Beschäftigtenbewertung, Kredit-Scoring, individueller Risikobewertung, Eignungsbewertung oder personalisiertem Leistungsmonitoring ist die Profiling-Sperre besonders sorgfältig zu prüfen.

## Erhebliches Risiko

Die Rückausnahme setzt voraus, dass das System kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte darstellt. Nicht nur technische Sicherheit zählt, sondern auch Gleichbehandlung, Datenschutz, Menschenwürde, Zugang zu Leistungen, Bildung, Arbeit, Rechtsschutz und effektiver menschlicher Kontrolle.

Risikofaktoren:
- Output beeinflusst Zugang, Ablehnung, Priorität, Score, Ranking oder Sanktion.
- Betroffene können Output kaum erkennen, bestreiten oder korrigieren.
- Menschliche Kontrolle ist nur formal oder faktisch überfordert.
- Datenqualität, Bias, Halluzinationen oder Fehlklassifikationen können Personen treffen.
- Nutzung erfolgt in Machtasymmetrie: Arbeitgeber, Schule, Behörde, Bank, Versicherung, Gericht.
- Off-label-Nutzung ist naheliegend und nicht wirksam abgesichert.

## Vier Fallgruppen

### 1. Enge Verfahrensaufgabe

Das System führt eine eng begrenzte Verfahrensaufgabe aus und hat keinen wesentlichen Einfluss auf das Ergebnis der Entscheidung.

Beispiele:
- Vollständigkeitsprüfung eines Formulars
- Erkennung fehlender Anlagen
- Termin- oder Fristenhinweis ohne Bewertung des Anspruchs

Nicht ausreichend:
- "nur Vorprüfung", wenn die Vorprüfung praktisch über Weiterleitung, Ablehnung oder Ranking entscheidet
- automatische Priorisierung von Personenfällen mit realer Entscheidungswirkung

### 2. Verbesserung einer bereits abgeschlossenen menschlichen Tätigkeit

Das System verbessert das Ergebnis einer zuvor von einem Menschen erbrachten Tätigkeit, ohne dieses Ergebnis wesentlich zu verändern oder zu ersetzen.

Beispiele:
- sprachliche Glättung eines bereits entschiedenen Bescheids
- Barrierefreiheits- oder Lesbarkeitsverbesserung ohne Inhaltsänderung
- Formatierung, Übersetzung oder Zusammenfassung zur Nachvollziehbarkeit

Nicht ausreichend:
- das System schreibt die eigentliche Bewertung, Begründung oder Entscheidung
- der Mensch übernimmt die KI-Ausgabe regelmäßig ungeprüft

### 3. Mustererkennung ohne Ersetzung oder Beeinflussung menschlicher Bewertung

Das System erkennt Entscheidungsmuster oder Abweichungen von früheren Entscheidungsmustern, ohne eine bereits abgeschlossene menschliche Bewertung zu ersetzen oder zu beeinflussen.

Beispiele:
- Qualitätskontrolle, die auffällige Abweichungen für interne Audit-Zwecke markiert
- statistische Konsistenzprüfung ohne Einfluss auf Einzelfallentscheidung

Nicht ausreichend:
- Anomaliehinweis löst faktisch Ablehnung, Eskalation oder Benachteiligung aus
- System gibt einen Risikoscore aus, der die menschliche Bewertung prägt

### 4. Vorbereitende Aufgabe

Das System bereitet eine Bewertung vor, die für einen Anhang-III-Zweck relevant ist, ohne selbst die bewertungsrelevanten Aspekte zu beurteilen.

Beispiele:
- Dokumente sortieren, OCR, Dubletten erkennen
- Akten chronologisch strukturieren
- Lebenslaufdaten in Felder übertragen, ohne Eignung zu bewerten

Nicht ausreichend:
- das System extrahiert nicht nur, sondern bewertet Eignung, Glaubhaftigkeit, Risiko, Bedürftigkeit, Leistung oder Rechtsfolge
- die vorbereitende Ausgabe wird als Empfehlung oder Entscheidungsvorschlag genutzt

## Allgemeiner Chatbot im sensiblen Bereich

Bei ChatGPT-ähnlichen oder GPAI-basierten Tools:

- Reine Textentwürfe, Zusammenfassungen oder Übersetzungen können unter die Rückausnahme fallen, wenn sie keine individuelle Bewertung steuern.
- Prompt-Vorlagen wie "bewerte die Eignung", "ranke Bewerber", "prognostiziere Prozessrisiko für Richter", "entscheide Leistungsanspruch" sprechen gegen die Rückausnahme.
- Wenn die Fachabteilung das Tool faktisch für Bewertungen nutzt, reicht eine schöne Richtlinie allein nicht. Prüfe Nutzung, Logs, Schulung, Freigabe und Kontrollen.

## Dokumentationspflicht nach Art. 6 Abs. 4

Wenn ein Anbieter ein Anhang-III-System wegen Art. 6 Abs. 3 nicht als Hochrisiko einstuft, ist die Bewertung vor dem Inverkehrbringen oder der Inbetriebnahme zu dokumentieren. Die Dokumentation muss belastbar genug sein, um sie zuständigen Behörden auf Anfrage vorzulegen.

Dokumentieren:
- Anhang-III-Tatbestand
- konkrete Zweckbestimmung
- warum kein erhebliches Risiko besteht
- welche Fallgruppe greift
- warum kein Profiling natürlicher Personen vorliegt
- welche Kontrollen Fehlgebrauch verhindern
- Re-Evaluation-Trigger

## Ergebnis und Routing

- **Rückausnahme greift wahrscheinlich:** `nicht-hochrisiko-bestaetigt-end-to-end-roadmap`, zusätzlich Art. 50, GPAI und Art. 4 prüfen.
- **Rückausnahme greift nicht:** `hochrisiko-bestaetigt-end-to-end-roadmap`.
- **Fehlgebrauch oder Zweckänderung unklar:** `betreiber-deployer-pflichten-art-26`, `anbieter-werden-art-25`, ggf. `mandatsabbruch-empfehlung-komplexe-faelle`.

## Output-Template — Rückausnahme-Vermerk

```text
RUECKAUSNAHME-VERMERK — ART. 6 ABS. 3 KI-VO
Datum: [DATUM]
System: [NAME]
Anhang-III-Treffer: [NR. / BEREICH / KONKRETER TATBESTAND]

1. Profiling-Sperre
[Profiling natürlicher Personen: JA/NEIN/UNKLAR]
[Begründung]

2. Erhebliches Risiko
[Gesundheit/Sicherheit/Grundrechte betroffen?]
[Wirkpfad, betroffene Personen, Entscheidungseinfluss, Kontrollen]

3. Fallgruppe
[enge Verfahrensaufgabe / Verbesserung menschlicher Tätigkeit / Mustererkennung / vorbereitende Aufgabe / keine]

4. Tatsächliche Nutzung und Fehlgebrauch
[Zweckbestimmung, Richtlinie, Logs, Schulung, technische Sperren, bekannte Abweichungen]

5. Ergebnis
[Rückausnahme greift wahrscheinlich / greift nicht / offen]

6. Dokumentations- und Re-Evaluation-Punkte
[Was muss in der Art. 6 Abs. 4-Dokumentation stehen? Wann neu prüfen?]

7. Nächster Skill
[nicht-hochrisiko-bestaetigt-end-to-end-roadmap / hochrisiko-bestaetigt-end-to-end-roadmap / betreiber-deployer-pflichten-art-26 / anbieter-werden-art-25]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 6 Abs. 3 und 4 KI-VO, Art. 3 Nr. 12/13/23 KI-VO und Anhang III. Keine Rechtsberatung; die Rückausnahme ist eng und tatsachenabhängig.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
