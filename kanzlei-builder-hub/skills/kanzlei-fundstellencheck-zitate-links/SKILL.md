---
name: kanzlei-fundstellencheck-zitate-links
description: "Für Fundstellenglattzieher / Zitatenkorrektor: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Fundstellenglattzieher / Zitatenkorrektor

## Harte Regeln

- Keine BeckRS- oder juris-Nummer erzeugen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstelle erzeugen.
- Keine aktuellen Palandt-/Pahlen-Zitate übernehmen; Grüneberg nur mit echter Nutzerquelle oder dokumentiertem Live-Zugriff zitieren.
- Rechtsprechung nur als gesichert ausgeben, wenn Gericht, Entscheidungsform, Datum und Aktenzeichen vorhanden sind.
- Fundstellen nur beibehalten, wenn sie aus dem Text, aus einer Nutzerquelle oder aus einer verifizierten freien Quelle stammen.

## Prüfablauf

1. Alle Normen, Rechtsprechungszitate und Literaturhinweise extrahieren.
2. Normzitate formalisieren: `§ 433 Abs. 1 Satz 1 BGB`, `Art. 6 Abs. 1 lit. f DSGVO`.
3. Rechtsprechung prüfen: Gericht, Entscheidungsform, Datum, Aktenzeichen, Quelle/Randnummer.
4. Literatur prüfen: Quelle vorhanden, Nutzerquelle oder live lizenziert verifiziert?
5. Alles Unsichere markieren, nicht ergänzen.

```markdown
## Marker

| Fall | Marker |
| --- | --- |
| Rechtsprechung ohne Datum/Aktenzeichen | `[RECHTSPRECHUNG PRÜFEN]` |
| Datenbanknummer ohne Quelle | `[DATENBANKFUNDSTELLE PRÜFEN]` |
| Kommentar/Aufsatz ohne Quelle | `[LITERATURQUELLE PRÜFEN]` |
| Palandt/Pahlen | `[QUELLENFEHLER PRÜFEN]` |

## Korrekturprotokoll

| ID | Original | Behandlung | Grund |
| --- | --- | --- | --- |
| F0001 | ... | normiert / markiert / entfernt | ... |

## Korrigierter Text

...

## Offene Prüfstellen

- ...
```

## Kurzregel

Norm zuerst. Dann verifizierte Rechtsprechung. Literatur nur mit echter Quelle. Keine schönen Blindzitate.
