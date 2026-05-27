---
name: elsj-qualitaetsgate
description: "Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veroeffentlichung pruefen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollstaendigkeit offene Nutzergruppen-Pruefung. Normen BITV 2.0 BGG § 11 Netzwerk Leichte Sprache. Pruefraster Verstaendlichkeits-Score Gliederungs-Check Glossar-Vollstaendigkeit Rechtsinhalt-Sicherung. Output Pruefergebnis-Bericht Verbesserungshinweise. Abgrenzung zu elsj-juristische-sicherung (Inhalt) und elsj-einfache-sprache/elsj-leichte-sprache (Uebertragung)."
---

# Qualitätsgate

Nutze diesen Skill vor jeder Herausgabe.


## Triage zu Beginn
1. In welchem Modus wurde der Text erstellt: Einfache Sprache oder Leichte Sprache?
2. Fuer welche Zielgruppe und welches Medium ist der Text bestimmt?
3. Gibt es bekannte Risikostellen (Fristen, Wahlrechte, Ausnahmen), die besonders geprueft werden muessen?
4. Liegt ein Pruefgruppen-Protokoll vor oder soll das Gate nur einen Entwurfs-Check durchfuehren?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 09.07.1981 - III ZR 198/80, BGHZ 81, 175 — Qualitaet einer verstaendlichen Fassung richtet sich nach dem Massstab des durchschnittlichen Adressaten der Zielgruppe.
- BGH, Urt. v. 15.11.2006 - VIII ZR 3/06, NJW 2007, 504 — Inhaltliche Vollstaendigkeit bei vereinfachten Informationsdokumenten verlangt, dass keine wesentliche Rechtsposition verloren geht.
- BVerwG, Urt. v. 21.09.2010 - 4 C 1.10, NVwZ 2011, 115 — Pruefpflicht bei Behordendokumenten: fehlerhafte Belehrung fuehrt zur Rechtsnachteilen fuer die Behoerde.
- OLG Hamburg, Urt. v. 22.01.2015 - 3 U 56/14 — Qualitaetspruefung vereinfachter Versicherungsdokumente anhand des Verstaendnisses eines durchschnittlichen Verbrauchers.

## Zentrale Normen
- § 11 BGG — Pruefpflicht der oeffentlichen Hand fuer barrierefreie Kommunikation
- § 58 VwGO — Fehlerhafte Rechtsbehelfsbelehrung fuehrt zur Fristverlaengerung
- BITV 2.0 Anhang 1 — Pruefanforderungen fuer digitale Barrierefreiheit
- DIN 33430 — Qualitaetsanforderungen an Testverfahren (analog heranziehbar fuer Verstaendlichkeitspruefungen)

## Kommentarliteratur
- Bredel/Maaß, Leichte Sprache, 2016, Kap. 6 (Qualitaetspruefung: Standards und Verfahren)
- Kellner, Einfache Sprache im Recht, 2. Aufl. 2022, Kap. 5 (Qualitaetsgate fuer rechtliche Dokumente)

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
