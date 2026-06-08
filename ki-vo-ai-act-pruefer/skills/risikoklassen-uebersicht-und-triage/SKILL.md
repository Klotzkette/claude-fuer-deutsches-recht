---
name: risikoklassen-uebersicht-und-triage
description: "Schnelle Risikoklassen-Triage nach KI-VO mit Fokus auf Art. 6 Abs. 2 und Anhang III. Prueft verboten, Hochrisiko nach Art. 6 Abs. 1/2, Rueckausnahme Art. 6 Abs. 3, begrenztes Risiko Art. 50, GPAI und minimales Risiko. Behandelt allgemeine Chatbots/GPAI: nicht automatisch Hochrisiko, sondern zweck- und einsatzbezogen. Output: Risikoklassen-Erstdiagnose mit passenden Folge-Skills und Dokumentationshinweisen."
---

# Risikoklassen-Übersicht und Triage — KI-VO

## Zweck

Dieser Skill gibt eine schnelle, aber dokumentierbare Ersteinschätzung der KI-VO-Risikoklasse. Der Schwerpunkt liegt auf der richtigen Abzweigung zwischen allgemeinem KI-System/GPAI, begrenztem Risiko und Hochrisiko nach Art. 6 Abs. 2 i.V.m. Anhang III.

## Vorfrage: Ist es ein KI-System?

Wenn das nicht sicher ist, zuerst:
- `liegt-ki-system-vor-art-3-nr-1`
- bei Grenzfällen `abgrenzung-konventionelle-software-vs-ki-system`

## Reihenfolge der Risikoprüfung

### 1. Verbotene Praktiken nach Art. 5

Nur kurz screenen. Wenn ein Treffer möglich ist, in `verbotene-praktiken-art-5` vertiefen. Der Nutzer hat den Schwerpunkt hier nicht gesetzt, aber Art. 5 darf nicht übersehen werden.

### 2. Hochrisiko nach Art. 6 Abs. 1

Prüfe, ob das KI-System Sicherheitsbauteil eines Produkts ist oder selbst ein Produkt, das unter Anhang-I-Sektorrecht fällt und einer Dritt-Konformitätsbewertung unterliegt.

Weiter: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

### 3. Hochrisiko nach Art. 6 Abs. 2 i.V.m. Anhang III

Das ist der zentrale Praxisschritt.

Immer prüfen:
- konkrete Zweckbestimmung
- Betreiberzweck und tatsächlicher Organisationsgebrauch
- natürliche Personen oder kritische Infrastruktur betroffen?
- Entscheidungseinfluss: Zugang, Bewertung, Ranking, Priorisierung, Rechtsanwendung, Risiko, Leistung
- allgemeiner Chatbot/GPAI nur theoretisch nutzbar oder tatsächlich eingebettet?

Weiter: `hochrisiko-art-6-abs-2-anhang-iii`

### 4. Rückausnahme Art. 6 Abs. 3

Wenn Anhang III passt, nicht sofort stoppen. Prüfe eng:
- Profiling natürlicher Personen?
- erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte?
- eine der vier Fallgruppen?
- Dokumentation nach Art. 6 Abs. 4?

Weiter: `rueckausnahme-art-6-abs-3`

### 5. Begrenztes Risiko nach Art. 50

Prüfe insbesondere:
- Interaktion natürlicher Personen mit KI-System
- KI-generierte oder manipulierte Inhalte
- Deepfake-Kennzeichnung
- Emotionserkennung oder biometrische Kategorisierung, soweit nicht verboten/hochrisikorelevant

Weiter: `begrenztes-risiko-art-50-transparenzpflichten`

### 6. GPAI

Bei LLMs, Foundation Models, APIs und allgemeinen Chatbots:
- GPAI-Modell oder GPAI-System prüfen
- systemisches Risiko prüfen, falls Modellanbieter betroffen
- Hochrisiko nur bei konkreter Anhang-III-Zweckbestimmung

Weiter: `gpai-vorliegen-art-3-nr-63`

### 7. Minimales Risiko

Wenn keine der obigen Kategorien greift:
- KI-VO-Restpflichten prüfen, insbesondere Art. 4 KI-Kompetenz, interne Governance, Datenschutz, Berufsrecht, Urheberrecht, Produktsicherheit.
- Negativdiagnose dokumentieren.

Weiter: `nicht-hochrisiko-bestaetigt-end-to-end-roadmap`

## Chatbot-/GPAI-Leitsatz

Ein allgemeiner Chatbot ist nicht deshalb Hochrisiko, weil er technisch in Hochrisiko-Bereichen einsetzbar wäre. Entscheidend ist, ob Anbieter oder Betreiber ihn für einen Anhang-III-Zweck bestimmen, integrieren, erlauben, systematisch dulden oder durch fehlende Kontrollen naheliegenden Hochrisiko-Fehlgebrauch nicht beherrschen.

## Output-Template — Risikoklassen-Erstdiagnose

```text
RISIKOKLASSEN-ERSTDIAGNOSE KI-VO
Datum: [DATUM]
System: [NAME]

1. KI-System-Status
[Ja/Nein/Unklar] — [Begründung oder Verweis]

2. Zweck und Nutzung
[Anbieter-Zweck, Betreiber-Zweck, tatsächliche Nutzung, Off-label-Risiken]

3. Risiko-Screening
- Art. 5 Verbot: [Treffer/kein Treffer/unklar]
- Art. 6 Abs. 1: [Treffer/kein Treffer/unklar]
- Art. 6 Abs. 2/Anhang III: [Treffer/kein Treffer/unklar]
- Art. 6 Abs. 3 Rückausnahme: [prüfen/nicht einschlägig]
- Art. 50 begrenztes Risiko: [Treffer/kein Treffer/unklar]
- GPAI: [Modell/System/nein/unklar]

4. Vorläufiges Ergebnis
[verboten / Hochrisiko / nicht Hochrisiko wegen Rückausnahme / begrenztes Risiko / GPAI-Pflichten / minimales Risiko / offen]

5. Nächste Skills
[konkrete Skill-Reihenfolge]

6. Dokumentation
[Welche Tatsachen und Unterlagen fehlen? Welche Annahmen müssen belegt werden?]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3, 5, 6, 50, 51 bis 55 und Anhang III KI-VO. Keine Rechtsberatung.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
