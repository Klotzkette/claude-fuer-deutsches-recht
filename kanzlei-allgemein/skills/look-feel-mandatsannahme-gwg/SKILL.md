---
name: look-feel-mandatsannahme-gwg
description: "Für Look and Feel: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Look and Feel

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Für welchen Kanzlei-soll die Ausgabe gestaltet werden: Schriftsatz, Rechnung, Dashboard, Mandantenbrief?
2. Wird die Ausgabe in Claude Cowork oder in einem anderen System angezeigt (Markdown-Grenzen beachten)?
3. Sollen Ampelstatus, Statuskarten oder Tabellenansichten eingesetzt werden?
4. Ist der Empfaenger der Ausgabe ein Anwalt, ein Sekretariat oder ein Mandant?

## Zentrale Normen
- § 43 BRAO — Sorgfaltspflicht: umfasst auch klare und verstaendliche Kommunikation
- § 2 BORA — Gewissenhaftigkeit: Kanzlei-Ausgaben müssen korrekt und klar sein
- § 133 BGB — Auslegung: Unklarheiten in Kanzleischreiben gehen zu Lasten des Verfassers
- Art. 5 Abs. 1 DSGVO — Transparenz: Informationen an Mandanten müssen klar und verstaendlich sein

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
### Kanzlei-Allgemein-Plugin

## Kommandocenter

| Akte | Ampel | Frist | Nächste Aktion |
| --- | --- | --- | --- |
| | | | |

## Jetzt

1. Sofortmaßnahme mit Verantwortlichem
2. Fehlende Unterlage oder Entscheidung
3. Abschlusskontrolle mit Frist
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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
