# Testakte: juristischer Mandantenbrief in Einfacher und Leichter Sprache

Diese fiktive Testakte gehört zum Plugin `einfache-leichte-sprache-jura`.
Sie enthält einen kurzen juristischen Ausgangstext und zwei Ziel-Fassungen:
Einfache Sprache und Leichte Sprache.

## Dateien

| Datei | Zweck |
| --- | --- |
| `01_original_juristischer_text.md` | Ausgangstext im üblichen juristischen Stil |
| `02_einfache_sprache.md` | Ziel-Fassung in Einfacher Sprache |
| `03_leichte_sprache.md` | Ziel-Fassung in Leichter Sprache |
| `04_glossar.md` | schwere Wörter kurz erklärt |
| `05_qualitaetscheck_einfache.json` | Skript-Prüfung Einfache Sprache |
| `06_qualitaetscheck_leichte.json` | Skript-Prüfung Leichte Sprache |

## Testlauf

```bash
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py \
  testakten/einfache-leichte-sprache-jura-mandantenbrief/02_einfache_sprache.md \
  --mode einfache
```

```bash
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py \
  testakten/einfache-leichte-sprache-jura-mandantenbrief/03_leichte_sprache.md \
  --mode leichte
```

Erwartung: Beide Checks dürfen Warnungen ausgeben. Das ist kein Fehler.
Warnungen zeigen, wo ein Mensch noch prüfen soll.
