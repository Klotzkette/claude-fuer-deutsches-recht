---
name: kostenentscheidung-bauen
description: "Kostenentscheidung nach §§ 91 ff. ZPO erstellen: Richter muss Kostenquote und -grundentscheidung formulieren. Normen: § 91 ZPO (vollständiges Obsiegen), § 92 ZPO (teilweises Obsiegen), § 100 ZPO (mehrere Beklagte), § 101 ZPO (Streitgenossenschaft/Nebenintervenient), § 93 ZPO (sofortiges Anerkennt..."
---

# Kostenentscheidung

## Triage zu Beginn

1. Wer hat in der Hauptsache gewonnen — vollständig oder teilweise?
2. Bei teilweisem Obsiegen: wie hoch sind die Streitwertanteile beider Parteien?
3. Sind mehrere Beklagte vorhanden — Gesamtschuldner (§ 100 Abs. 4 ZPO) oder anteilig (§ 100 Abs. 1 ZPO)?
4. Liegt sofortiges Anerkenntnis ohne Veranlassung vor (§ 93 ZPO — Kostenfolge für Kläger)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 91 ZPO — vollständige Kostentragung durch Unterliegenden
- § 92 ZPO — Quotelung bei teilweisem Obsiegen
- § 93 ZPO — sofortiges Anerkenntnis (Kosten für Kläger)
- § 100 ZPO — mehrere Beklagte (anteilig oder gesamtschuldnerisch)
- § 101 ZPO — Kosten bei Nebenintervention
- § 3 ZPO — Streitwertschätzung

## Schritt-für-Schritt-Workflow

1. **Obsiegen/Unterliegen feststellen:** Welche Klageanträge wurden zugesprochen, welche abgewiesen?
2. **Streitwertanteile berechnen:** Zugesprochener Betrag / Gesamtstreitwert = Obsiegensquote Kläger.
3. **Regelfall § 91 ZPO:** Voller Sieg → Beklagter trägt alle Kosten.
4. **Teilsieg § 92 ZPO:** Quote berechnen und Kostenverteilung quotalisch.
5. **Sonderfälle prüfen:** § 93 ZPO (sofortiges Anerkenntnis), § 96 ZPO (Vergleich), § 101 ZPO (Nebenintervention).
6. **Formulierung wählen** (s. Beispiele oben).

## Output-Template

**Adressat:** Urteil → Tenor (Ziff. 2) und Entscheidungsgründe — Tonfall: sachlich-juristisch

```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Kostenentscheidung

**Tenor Ziff. 2:**
"Die Kosten des Rechtsstreits trägt die Beklagte." [Volles Obsiegen]
"Von den Kosten des Rechtsstreits trägt der Kläger [X] von hundert, die Beklagte [Y] von hundert." [Quotelung]

**Begründung in Entscheidungsgründen:**
Die Kostenentscheidung beruht auf § [91 / 92 Abs. 1] ZPO. Der Kläger hat in Höhe von
[BETRAG] EUR obsiegt (zugesprochene Forderung) und ist in Höhe von [BETRAG] EUR unterlegen.
Dies ergibt eine Obsiegensquote von [X] Prozent.
```

## Grundregeln

- Paragraf 91 ZPO - die unterlegene Partei traegt alle Kosten
- Paragraf 92 ZPO - bei teilweisem Obsiegen Quote nach Streitwertverhältnis und Erfolg
- Paragraf 93 ZPO - sofortiges Anerkenntnis ohne Veranlassung - Kläger traegt Kosten
- Paragraf 96 ZPO - Vergleichsspezial
- Paragraf 100 ZPO - mehrere unterlegene Streitgenossen
- Paragraf 101 ZPO - Nebenintervention

## Quotenberechnung

1. Ausgangsstreitwert ermitteln
2. Tatsächliches Obsiegen / Unterliegen jeder Partei beziffern
3. Quoten bilden: Obsiegen Kläger / Streitwert = Verurteilungsquote Beklagter
4. Gegenrechnung: gegenseitige Anteile bei Widerklage / Drittwiderklage

## Formulierung

- "Die Kosten des Rechtsstreits traegt die Beklagte."
- "Von den Kosten des Rechtsstreits tragen der Kläger einhundertacht von hundert und die Beklagte zweiundneunzig von hundert."
- Bei mehreren Beklagten: "Die Kosten des Rechtsstreits tragen die Beklagten als Gesamtschuldner."
- Bei Widerklage: getrennte Quoten für Klage und Widerklage möglich

## Streitwert

Streitwertbeschluss separat oder im Tenor. Pflicht zur Begründung bei Abweichung vom Klagantrag.

<!-- AUDIT 27.05.2026
-->
