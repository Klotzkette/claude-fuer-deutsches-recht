---
name: kommandocenter
description: "Für Kommandocenter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Kanzlei-Allgemein."
---

# Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Grundregel

Erst Tempo, dann Tiefe:

1. Ziel erkennen.
2. Risiko erkennen.
3. maximal drei Rückfragen stellen.
4. sofort eine Arbeitskarte erzeugen.
5. `kanzlei-allgemein-look-and-feel` anwenden, wenn eine sichtbare Dashboard-, Status- oder Startausgabe entsteht.
6. an den passenden Fachmodul übergeben.

Nicht alle Checklisten auf einmal öffnen. Nur die Checkliste verwenden, die den nächsten Arbeitsschritt wirklich freischaltet.

## Schnellbefehle

| Nutzer sagt | Route |
| --- | --- |
| `Neue Sache` | Intake, Akte, Mandatsannahme/GwG, Aktenzeichen, Kontoblatt |
| `Mach Klage` | Schriftsatz-Turbo, Anlagen, Rechtsprechung, Qualitätsgate, Versand |
| `Mach Replik` | Replikmatrix, Anlagen, Rechtsprechung, Qualitätsgate, Versand |
| `Mach Vertrag` | Vertragsentwurf, Handelsregister, Datenschutz, Qualitätsgate |
| `Post machen` | Postlauf, beA-Journal, Fristen, EB, Aktenablage |
| `Rechnung machen` | Zeitnarrative, Rechnung, E-Rechnung, GoBD, offene Posten |
| `GwG prüfen` | Mandatsannahme/GwG, KYC, PEP, wirtschaftlich Berechtigte, Verdachtslogik |
| `Recherche machen` | Rechtsprechungsrecherche, Fundstellenregister, Verwertungsnotiz |
| `Kanzleitag simulieren` | Integrationen, Simulation, Kalender, Postlauf, Mandatsannahme, Output |
| `Was ist offen?` | Fristen, Action-Items, Rechnungen, GwG-Reminder, Post, HR, UStVA |

## Freigabeampel

Immer eine Ampel ausgeben:

- `GRÜN`: Weiterarbeiten möglich. Keine bekannte Stoppschwelle.
- `GELB`: Nutzbarer Entwurf, aber offene Punkte.
- `ROT`: Nicht versenden, nicht annehmen, nicht buchen oder nicht melden, bevor ein Mensch freigibt.

Typische rote Schwellen:

- Frist unklar.
- beA-Versand oder EB ohne Einzelbestätigung.
- Mandatsannahme ohne Konfliktcheck oder GwG-Status.
- Verdachtsfall, PEP-/Hochrisiko- oder Mittelherkunftsproblem ungeklärt.
- Rechnung ohne Freigabe oder E-Rechnungsvalidierung.
- Rechtsprechung nicht verifiziert.
- Handelsregister, Partei oder Vertretung ungeprüft.

## Arbeitskarte

Immer mit dieser Struktur starten:

```markdown
### Kanzlei-Allgemein-Plugin

## Kommandocenter

| Akte | Ampel | Frist | Nächste Aktion |
| --- | --- | --- | --- |
| | | | |

## Jetzt

1. Sofortmaßnahme mit Verantwortlichem
2. Folgeschritt mit Frist
3. Abschlusskontrolle mit Freigabestatus
```

## Anfängerfreundlichkeit

- Fachworte kurz übersetzen.
- Nicht mit 20 Fragen beginnen.
- Fehlendes als `TODO` markieren.
- Unsichere Nutzer mit einem konkreten Vorschlag führen.
- Bei Profis knapper werden und direkt an die Fachmodule übergeben.

## Übergabe

- Neue Sache oder Dokumenteneingang: `kanzlei-allgemein-intake`, danach `kanzlei-allgemein-akte` und bei Bedarf `kanzlei-allgemein-mandatsannahme-gwg`.
- Klage/Replik/Antrag: `kanzlei-allgemein-schriftsatz-turbo`, `kanzlei-allgemein-rechtsprechungsrecherche`, `kanzlei-allgemein-qualitaetsgate-hardening`.
- Vertrag: `kanzlei-allgemein-vertragsentwurf`, `kanzlei-allgemein-handelsregisterabruf`, `kanzlei-allgemein-qualitaetsgate-hardening`.
- beA/Post: `kanzlei-allgemein-postlauf`, `kanzlei-allgemein-bea-journal`, `kanzlei-allgemein-fristen-monitor`.
- Rechnung/Buchhaltung: `kanzlei-allgemein-zeitnarrative`, `kanzlei-allgemein-rechnung`, `kanzlei-allgemein-erechnung`, `kanzlei-allgemein-buchhaltung-konten`.
- Kanzleibetrieb: `kanzlei-allgemein-kanzleikalender`, `kanzlei-allgemein-automationen`, HR-/Payroll-Skills.

## Ausgabe

- `assets/templates/workflow-kommandocenter.md`
- `assets/templates/workflow-schnellstartkarte.md`
- `assets/templates/workflow-freigabeampel.md`
- optional `assets/templates/workflow-naechste-beste-aktion.md`
- für hochwertige Cowork-Ausgaben zusätzlich `assets/templates/cowork-dashboard.md`, `assets/templates/cowork-statuskarte.md` und `assets/templates/cowork-freigabekarte.md`.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->
