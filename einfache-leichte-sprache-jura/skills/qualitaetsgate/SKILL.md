---
name: qualitaetsgate
description: "Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 Netzwerk Leichte Sprache. Prüfraster Verstaendlichkeits-Score"
---

# Qualitätsgate

Dieses Fachmodul vor jeder Herausgabe.

## Triage zu Beginn
1. In welchem Modus wurde der Text erstellt: Einfache Sprache oder Leichte Sprache?
2. Für welche Zielgruppe und welches Medium ist der Text bestimmt?
3. Gibt es bekannte Risikostellen (Fristen, Wahlrechte, Ausnahmen), die besonders geprueft werden müssen?
4. Liegt ein Prüfgruppen-Protokoll vor oder soll das Gate nur einen Entwurfs-Check durchfuehren?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Prüfpflicht der öffentlichen Hand für barrierefreie Kommunikation
- § 58 VwGO — Fehlerhafte Rechtsbehelfsbelehrung fuehrt zur Fristverlaengerung
- BITV 2.0 Anhang 1 — Prüfanforderungen für digitale Barrierefreiheit
- DIN 33430 — Qualitaetsanforderungen an Testverfahren (analog heranziehbar für Verstaendlichkeitspruefungen)

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Output-Template: Qualitaetsgate-Ergebnis

```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

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
