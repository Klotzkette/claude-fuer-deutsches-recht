---
name: elsj-qualitaetsgate
description: "Prüft Fassungen in Einfacher Sprache oder Leichter Sprache auf Verständlichkeit, Gliederung, Glossar, Zielgruppenpassung, juristische Vollständigkeit und offene Nutzerprüfung."
---

# Qualitätsgate

Nutze diesen Skill vor jeder Herausgabe.

## Pflichtprüfung

| Prüffeld | Frage |
| --- | --- |
| Zielgruppe | Ist klar, für wen der Text geschrieben ist? |
| Zielhandlung | Ist klar, was die Person tun soll oder tun kann? |
| Struktur | Sind Überschriften aussagekräftig? |
| Fristen | Sind alle Fristen sichtbar und richtig? |
| Rechtsfolgen | Sind Risiken und Folgen klar genannt? |
| Wörter | Sind Fachwörter erklärt? |
| Satzbau | Sind Sätze kurz und eindeutig? |
| Ton | Ist der Text respektvoll? |
| Recht | Wurde nichts rechtlich Wichtiges weggelassen? |
| Prüfung | Ist eine Nutzerprüfung erforderlich oder offen? |

## Automatischer Vorcheck

Optional:

```bash
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py <datei> --mode einfache
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py <datei> --mode leichte
```

Bewerte das Skript nur als Warnsystem. Ein kurzer Text kann trotzdem schlecht
sein. Ein längerer Satz kann ausnahmsweise nötig sein.

## Ergebnisformat

```markdown
## Qualitätsgate

Status: freigabereif / überarbeiten / Nutzerprüfung offen

### Stärken

- ...

### Risiken

- ...

### Muss vor Herausgabe korrigiert werden

- ...

### Kann verbessert werden

- ...
```

## Harte Stopps

Stoppe die Herausgabe, wenn:

- Frist oder Rechtsfolge fehlt.
- eine Pflicht als bloße Empfehlung dargestellt wird.
- ein Rechtsmittel falsch bezeichnet ist.
- bei Leichter Sprache fälschlich behauptet wird, es habe eine Prüfung durch
  Zielgruppenpersonen gegeben.
- der Text herablassend wirkt.
