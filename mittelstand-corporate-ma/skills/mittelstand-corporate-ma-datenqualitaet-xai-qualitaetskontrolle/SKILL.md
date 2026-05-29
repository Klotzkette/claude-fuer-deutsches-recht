---
name: mittelstand-corporate-ma-datenqualitaet-xai-qualitaetskontrolle
description: "Datenqualität und XAI-Qualitätskontrolle: Sichert KI-gestuetzte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab."
---

# Datenqualität und XAI-Qualitätskontrolle

## Zweck

Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab.

## Arbeitsmodus

- Datenqualität, Quellenstatus, Stichprobe und Plausibilisierung festhalten.
- Explainability-Anforderungen für jedes Ergebnis markieren.
- Human-in-the-loop und Senior Review dokumentieren.
- Fehler, Annahmen und nicht geprüfte Bereiche offenlegen.

## Rote Schwellen

- Keine Belegkette.
- Nicht erklärbares Ergebnis bei hohem Risiko.
- Bias oder Datenlücke wird nicht benannt.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/data-quality-gate.md
- assets/templates/xai-quality-control-log.md

## Triage

1. Welche Datenquellen wurden fuer die M&A-Analyse genutzt — Datenraum, Handelsregister, Pressemitteilungen, Expert Calls?
2. Welche Ergebnisse basieren auf automatisierter Verarbeitung — DD-Analyse, Vertragsmarkup, Risikobewertung?
3. Gibt es Bereiche, die nicht geprueft wurden — fehlende Daten, eingeschraenkter Datenraum, nicht zugaengliche Unterlagen?
4. Welche Ergebnisse haben hohes Risiko und erfordern Senior Review?

## Zentrale Rechtsgrundlagen

- Art. 22 DSGVO — automatisierte Einzelentscheidungen: bei rechtlich bedeutsamen Entscheidungen darf keine vollautomatische Entscheidung ohne menschliche Ueberpruefung getroffen werden
- Art. 13, 14 EU-KI-Verordnung (in Kraft ab 2024/2025) — KI-Systeme mit hohem Risiko muessen transparent, pruefbar und erklaerbar sein; Dokumentationspflichten
- §§ 675, 280 BGB — Beraterhaftung: Ergebnisse, die auf unzuverlaessigen Daten basieren, koennen Schadensersatz ausloesen; Anwalt muss Datenbasis offenlegen
- § 43a BRAO — Unabhaengigkeit: Anwalt darf sich nicht auf Ergebnisse verlassen, die er nicht nachpruefen kann

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Datenquellen dokumentieren:** alle verwendeten Quellen mit Datum, Version, Zugaenglichkeit; Luecken explizit benennen
2. **Stichprobe und Plausibilisierung:** 10-20 % der Ergebnisse manuell querprufen
3. **Explainability-Flag setzen:** je Ergebnis mit hohem Risiko: Human muss Ergebnis nachvollziehen koennen
4. **Halluzinations-Check:** Leitsatz-Zitate, Normen, Aktenzeichen — alle Faktenangaben verifizieren
5. **Human-in-the-loop-Protokoll:** wer hat geprueft, wann, Ergebnis der Pruefung

## Rote Schwellen

- Keine Belegkette fuer wesentliche Ergebnisse: Haftungsrisiko
- Nicht erklaerbares Ergebnis bei hohem Risiko: sofortige Senior Review; kein Versand
- Bias oder Datenlücke nicht benannt: moeglicherweise fehlerhafte Mandatsberatung
