---
name: caching-und-teil-rerun
description: "Zwischenergebnisse des 3D-Tabellenreviews cachen und Teilbereiche erneut ausführen ohne Vollneustart. Normen: technisch. Prüfraster: Cache-Status, verarbeitete Zeilen, Fehlerpunkte. Output: Rerun-Bericht mit gecachten und neu verarbeiteten Zeilen. Abgrenzung: nicht vollständiger Neustart."
---

# /tabellenreview-3d:caching-und-teil-rerun


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Ein 25.000-Zellen-Würfel komplett neu zu berechnen weil ein einziger Spaltenprompt um drei Worte präziser wurde ist verschwenderisch. Dieser Skill macht den Würfel inkrementell.

## Cache-Key

Pro Zelle ein deterministischer Hash:

```
sha256(spaltenprompt-version + zeilenprompt-version + dokument-hash + arbeitsblatt-perspektive + modell-version)
```

Wenn irgendeine dieser Komponenten sich ändert wird der Cache-Eintrag invalidiert.

## Invalidierungsregeln

- **Patch-Änderung am Spaltenprompt:** Cache bleibt gültig (siehe `prompt-versionierung`)
- **Minor-Änderung am Spaltenprompt:** Cache wird auf `nachprüfen` gesetzt — Prüfer entscheidet ob neu rechnen
- **Major-Änderung am Spaltenprompt:** Cache invalidiert, betroffene Zellen müssen neu berechnet werden
- **Zeilenprompt geändert:** nur die betroffene Zeile invalidiert, über alle Arbeitsblätter
- **Arbeitsblatt-Perspektive geändert:** alle Zellen dieses Arbeitsblatts invalidiert
- **Dokument-Hash geändert (z. B. neue Version):** alle Zellen dieser Zeile invalidiert
- **Modell-Version geändert:** Vorgehen wählbar — komplett neu / Stichprobe prüfen / Cache übernehmen mit Hinweis

## Quasi-Duplikate

Ein Vertrag-Cousin (sehr ähnlich) kann Cache-Treffer vom geprüften Originalvertrag übernehmen — als VORSCHLAG nicht als Befund. Schwelle: Cosine-Ähnlichkeit über 95 Prozent UND derselbe Dokumenttyp UND derselbe Vertragspartner-Stamm. Prüfer-Flag automatisch. Prüfer bestätigt oder verwirft.

## Kostenschätzung

Vor jedem Teil-Rerun schaetzt der Skill:
- Anzahl zu berechnender Zellen
- erwartete Laufzeit
- erwartete Token-/Kosten-Aufnahme
- Auswirkung auf Audit-Trail

Prüfer kann Rerun beauftragen / ablehnen / nur Stichprobe rechnen lassen.

## Ausgabe

- `cache.parquet` — alle Zellen mit Cache-Key Antwort Belegkette Ampel
- `rerun-vorschlag.md` — pro Änderung welche Zellen invalidiert sind und Kostenschätzung
- Eintrag in `audit-trail-protokoll`

## Grenzen

Caching ist ein Effizienzwerkzeug nicht ein Beweismittel. Wer auf gerichtsfeste Reproduzierbarkeit angewiesen ist (z. B. Verfahrenseingabe) sollte einen kompletten Lauf ohne Cache machen und das Ergebnis hashen.
