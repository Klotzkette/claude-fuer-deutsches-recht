---
name: qualitaetsgate
description: "Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 Netzwerk Leichte Sprache. Prüfraster Verstaendlichkeits-Score Gliederungs-Check Glossar-Vollständigkeit Rechtsinhalt-Sicherung. Output Prüfergebnis-Bericht Verbesserungshinweise. Abgrenzung zu elsj-juristische-sicherung (Inhalt) und elsj-einfache-sprache/elsj-leichte-sprache (Übertragung)."
---

# Qualitätsgate

Dieses Fachmodul vor jeder Herausgabe.

## Triage zu Beginn
1. In welchem Modus wurde der Text erstellt: Einfache Sprache oder Leichte Sprache?
2. Fuer welche Zielgruppe und welches Medium ist der Text bestimmt?
3. Gibt es bekannte Risikostellen (Fristen, Wahlrechte, Ausnahmen), die besonders geprueft werden muessen?
4. Liegt ein Pruefgruppen-Protokoll vor oder soll das Gate nur einen Entwurfs-Check durchfuehren?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Pruefpflicht der oeffentlichen Hand fuer barrierefreie Kommunikation
- § 58 VwGO — Fehlerhafte Rechtsbehelfsbelehrung fuehrt zur Fristverlaengerung
- BITV 2.0 Anhang 1 — Pruefanforderungen fuer digitale Barrierefreiheit
- DIN 33430 — Qualitaetsanforderungen an Testverfahren (analog heranziehbar fuer Verstaendlichkeitspruefungen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Qualitaetsgate-Ergebnis

```
## Qualitaetsgate

Geprueft am: [DATUM]
Modus: Einfache Sprache / Leichte Sprache
Zielgruppe: [Bezeichnung]

Status: freigabereif / ueberarbeiten / Nutzergruppe-Pruefung offen

### Staerken
- [...]

### Risiken
- [...]

### Muss vor Herausgabe korrigiert werden
- [...]

### Kann verbessert werden
- [...]

### Harte Stopps (falls zutreffend)
- [ ] Frist oder Rechtsfolge fehlt
- [ ] Pflicht als bloss Empfehlung dargestellt
- [ ] Rechtsmittel falsch bezeichnet
- [ ] Leichte Sprache: Pruefung durch Zielgruppe faelschlich behauptet
- [ ] Text wirkt herablassend
```
## Pflichtprüfung

| Prüfungslinie | Frage |
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
