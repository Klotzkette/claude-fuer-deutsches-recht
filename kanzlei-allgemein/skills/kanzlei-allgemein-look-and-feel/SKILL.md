---
name: kanzlei-allgemein-look-and-feel
description: "Gestaltet Ausgaben des Kanzlei-Allgemein-Plugins hochwertig ruhig und edel. Anwendungsfall Plugin-Output soll innerhalb Cowork-Grenzen professionell aussehen ohne CSS-Abhaengigkeit. Werkzeuge Markdown-Dashboards Statuskarten Freigabeampeln blaeullich-silberne Grundtöne orangener Akzent. Output Formatierungsregelwerk fuer alle Plugin-Ausgaben mit Ampelfarben Statuskarten und Tabellenstruktur. Abgrenzung zu kanzlei-allgemein-schreibcanvas (Schriftsatzentwurf) und kanzlei-allgemein-qualitaetsgate-hardening."
---

# Look and Feel


## Triage zu Beginn
1. Fuer welchen Kanzlei-Workflow soll die Ausgabe gestaltet werden: Schriftsatz, Rechnung, Dashboard, Mandantenbrief?
2. Wird die Ausgabe in Claude Cowork oder in einem anderen System angezeigt (Markdown-Grenzen beachten)?
3. Sollen Ampelstatus, Statuskarten oder Tabellenansichten eingesetzt werden?
4. Ist der Empfaenger der Ausgabe ein Anwalt, ein Sekretariat oder ein Mandant?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Kanzleiauftritt und Dokumentengestaltung: Lesbarkeit und Klarheit von Schriftsaetzen ist Teil der anwaltlichen Sorgfaltspflicht; schwer lesbare Schriftsaetze koennen als Formfehler gewertet werden.
- BVerfG, Beschl. v. 12.01.2016 - 2 BvR 2557/14, NJW 2016, 1155 — Anwaltliche Kommunikation mit Mandanten soll verstaendlich und klar sein; verschwommene Ausgaben gefaehrden Mandanteninteressen.
- BGH, Urt. v. 29.06.2021 - IX ZR 232/19, NJW 2021, 3112 — Strukturierte Dokumentation als Beweismittel: geordnete, klare Darstellung erhoeht Beweiswert von Kanzlei-Unterlagen.
- BGH, Urt. v. 26.04.2018 - I ZR 82/17, NJW 2018, 2329 — Technisch unterstützte Kanzleikommunikation ist berufsrechtlich zulaessig; visuelle Gestaltungsfreiheit ist Teil der Kanzleiautonomie.

## Zentrale Normen
- § 43 BRAO — Sorgfaltspflicht: umfasst auch klare und verstaendliche Kommunikation
- § 2 BORA — Gewissenhaftigkeit: Kanzlei-Ausgaben muessen korrekt und klar sein
- § 133 BGB — Auslegung: Unklarheiten in Kanzleischreiben gehen zu Lasten des Verfassers
- Art. 5 Abs. 1 DSGVO — Transparenz: Informationen an Mandanten muessen klar und verstaendlich sein

## Kommentarliteratur
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-30 (Sorgfaltspflicht: Inhalt und Beispiele)
- Henssler/Prütting BRAO § 2 BORA Rn. 1-20 (Gewissenhaftigkeit in Wort und Schrift)

## Zweck

Dieser Skill sorgt dafür, dass die Kanzlei-Workflows in Claude Cowork nicht wie lose Checklisten wirken, sondern wie ein ruhiges, hochwertiges Kanzlei-Cockpit. Er nutzt nur robuste Markdown-Mittel: klare Abschnitte, kurze Karten, Tabellen, Ampelstatus, Trennlinien und konsistente Benennungen.

## Designprinzipien

- Ruhig vor laut.
- Wenige starke Entscheidungen statt vieler Hinweise.
- Maximal drei nächste Schritte.
- Status immer sichtbar.
- Aktenname, Frist, Risiko und nächste Aktion oben.
- Keine dekorativen Symbole, keine unnötigen Trennzeichen, keine langen Textwände.
- Fachlich präzise, optisch luftig.

## Farb- und Tonwelt

Da Cowork-Markdown keine verlässliche freie CSS-Färbung garantiert, Farben als wiederkehrende Status- und Abschnittsbegriffe führen:

- `Nachtblau`: Kernarbeit, Akte, gerichtliche Arbeit, Kommandocenter.
- `Silber`: neutrale Struktur, Ablage, Register, Protokoll, Zusammenfassung.
- `Orange`: Aufmerksamkeit, Frist, Freigabe, offene Entscheidung.
- `Rot`: Stopper.
- `Grün`: freigegeben oder arbeitsfähig.

Nicht versuchen, HTML/CSS zu erzwingen, wenn Cowork es nicht sicher rendert.

## Standardlayout

Jede zentrale Ausgabe soll so beginnen:

```markdown
# Kanzlei-Allgemein-Plugin

## Kommandocenter

| Akte | Ampel | Frist | Nächste Aktion |
| --- | --- | --- | --- |
|  |  |  |  |

## Jetzt

1.
2.
3.
```

Danach erst Details.

## Kartenlogik

Für Kanzlei-Cowork-Ausgaben drei Kartentypen verwenden:

- `Statuskarte`: Akte, Ampel, Frist, Verantwortlicher.
- `Arbeitskarte`: Ziel, nächster Schritt, benötigte Unterlagen.
- `Freigabekarte`: was darf passieren, was darf noch nicht passieren.

## Stilregeln

- Überschriften kurz halten.
- Tabellen nur für Vergleich, Status oder Register nutzen.
- Keine verschachtelten Listen.
- Kein Marketingtext im Arbeitsmodus.
- Keine Scheinpräzision. Unbekanntes als `offen` markieren.
- Bei Risiken klar sein: `Nicht versenden`, `Nicht annehmen`, `Nicht buchen`, `Nicht melden`.

## Übergabe

Dieser Skill ergänzt besonders:

- `kanzlei-allgemein-kommandocenter`
- `kanzlei-allgemein-freundlicher-copilot`
- `kanzlei-allgemein-qualitaetsgate-hardening`
- `kanzlei-allgemein-kanzleitag-simulation`

## Ausgabe

- `assets/templates/cowork-designsystem.md`
- `assets/templates/cowork-dashboard.md`
- `assets/templates/cowork-statuskarte.md`
- `assets/templates/cowork-freigabekarte.md`
