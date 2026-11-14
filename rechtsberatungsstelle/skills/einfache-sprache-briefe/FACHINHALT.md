---
name: einfache-sprache-briefe
description: "Für [VERALTET] Verständliche Mandantenbriefe → siehe `/mandantenbrief` und `/status mandant`: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik."
---

# [VERALTET] Verständliche Mandantenbriefe → siehe `/mandantenbrief` und `/status mandant`

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Mandantenbriefe: `/mandantenbrief [typ]` oder `/status mandant`.

## Rechtlicher Rahmen

### Hintergrund der Aufteilung

Verständliche Mandantenkommunikation sichert eine ordnungsgemäße Beratung. Inhalt, Folgen, Fristen und nächste Handlungen müssen so erklärt werden, dass der Empfänger sie erfassen und eine informierte Entscheidung treffen kann. Die Nachfolge-Skills trennen deshalb kurze Routinekorrespondenz von einer inhaltlichen Statusmitteilung.

### Relevante Normen für die Nachfolge-Skills

- **Paragraf 6 Absatz 2 RDG** — Unentgeltliche Rechtsdienstleistungen außerhalb enger persönlicher Beziehungen müssen durch eine befugte Person, eine Person mit Befähigung zum Richteramt oder unter deren Anleitung erbracht werden. Anleitung umfasst Einweisung, Fortbildung und die im Einzelfall erforderliche Mitwirkung.
- **Paragraf 43a Absatz 3 BRAO** — Für den anleitenden Rechtsanwalt gilt das Sachlichkeitsgebot; bewusste Unwahrheiten und anlasslose herabsetzende Äußerungen sind unzulässig.
- **Paragraf 11 BORA sowie Paragrafen 675 und 666 BGB** — Für anwaltlich geführte Mandate tragen angemessene Unterrichtung und Auskunftspflicht die klare Statuskommunikation.
- **Paragrafen 2 und 3 BerHG** — Bei Beratungshilfe sind Gegenstand und Reichweite der bewilligten Beratung zu beachten.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

**Stattdessen verwenden:**

Für einfache Korrespondenz (Terminbestätigung, Unterlagenbitte, Eingangsbestätigung):
```
/mandantenbrief terminbestätigung
/mandantenbrief unterlagenbitte
/mandantenbrief eingangsbestätigung
```

Für inhaltliche Statusmitteilungen:
```
/status mandant
```

Vollständiger Ablauf in den jeweiligen SKILL.md-Dateien:

1. Zielgruppe festlegen (Bildungshintergrund, Sprache, besondere Umstände des Mandanten)
2. Verständlichkeitsstandards der Klinik anwenden (Klinik-Konfiguration → plain-language-standard)
3. Kein Fachjargon ohne Erläuterung; kurze Sätze; konkrete Handlungsanweisungen
4. Anleitung und erforderliche Mitwirkung nach Paragraf 6 Absatz 2 RDG vor Versand sichern

## Beispiel

Statt `/einfache-sprache-briefe`:

```
/status mandant
```

Dieser Befehl erstellt ein verständliches Statusschreiben (Zielgruppe: Mandant/-in) nach dem Hauptschulniveau-Standard, ohne Fachjargon, mit konkreten nächsten Schritten: "Was ist passiert / Was passiert als nächstes / Was müssen Sie tun / So erreichen Sie uns."

Oder für Routine-Korrespondenz:
```
/mandantenbrief terminbestätigung
```

Ergebnis: Eine klare Terminbestätigung mit Ort, Zeit, Mitnahme-Unterlagen und Kontaktdaten — ohne juristische Formulierungen.

## Risiken und typische Fehler

- **Verweis auf diese Skill in älteren Materialien:** Semesterskripte und Tutorenmaterialien auf die neuen Skills umschreiben.
- **Verständlichkeitsstandards als optional behandeln:** Frist, Folge und Handlungsauftrag müssen für den konkreten Empfänger erfassbar sein; im anwaltlich geführten Mandat tragen Paragraf 11 BORA sowie Paragrafen 675 und 666 BGB die Unterrichtung.
- **Fachbegriffe ohne Erläuterung:** Begriffe wie "Widerspruchsfrist", "Vollstreckungstitel" oder "Klagefrist" sind für viele Mandanten unverständlich. Immer in Klammern oder mit einfachem Folgesatz erläutern.
- **Versand ohne erforderliche Anleitung:** Vor einem rechtlich inhaltlichen Schreiben ist die nach Paragraf 6 Absatz 2 RDG im Einzelfall erforderliche Mitwirkung der anleitenden Person zu dokumentieren.

## Quellenpflicht

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben zu Mandantenbriefen: `skills/status/SKILL.md`, Sektion "Quellenpflicht", und `skills/mandantenbrief/SKILL.md`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
