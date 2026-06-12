---
name: qualitaetsgate-rechtsnormen-einfach
description: "Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 Netzwerk Leichte Sprache. Prüfraster Verstaendlichkeits-Score"
---

# Qualitätsgate

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BFSG ab 28.06.2025, BITV § 4 Verständlichkeit, BGG § 11 Pflicht zur einfachen Sprache bei Bescheiden auf Antrag.
- Tragende Normen verifizieren: BGG §§ 11, 12a, BITV 2.0 § 4, BFSG, UN-Behindertenrechtskonvention Art. 9 (Zugänglichkeit), EU-RL 2016/2102, DIN SPEC 33429 (Leichte Sprache), Hurraki-/Inclusion Europe-Regeln — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Behörde, Verwaltungsstelle, Übersetzer Leichte Sprache, Prüfgruppe (Selbstvertreter), Sozialverbände (Lebenshilfe, BAGSO), Behindertenbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Bescheid in Leichter Sprache, Erklärfilm-Skript, Antragsformular mit Erläuterung, Mandanteninfo, Prozessunterlagen in einfacher Sprache — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

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
