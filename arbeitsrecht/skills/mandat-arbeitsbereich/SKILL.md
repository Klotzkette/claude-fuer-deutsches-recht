---
name: mandat-arbeitsbereich
description: "Für Mandat Arbeitsbereich: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Mandatsakten verwalten – neu anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Mandatsakten verwalten – neu anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen. Verhindert, dass Kontext von einem Mandat in ein anderes übergeht. Relevant für Kanzleien mit mehreren Mandanten; für Syndikusrechtsanwälte deaktiviert.

### /arbeitsrecht:mandat-arbeitsbereich

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:mandat-arbeitsbereich` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

Anwälte und Kanzleien arbeiten für mehrere Mandanten gleichzeitig. Eine Mandatsakte hält den Kontext eines Mandanten strikt von allen anderen getrennt. Dieser Skill verwaltet diese Akten.

## Eingaben

- Befehl: `neu`, `auflisten`, `wechseln`, `schließen` oder `keine`
- Kürzel der Akte (Slug), z.B. `mueller-ksg-2024`
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` – Abschnitt `## Mandantenakten`

## Ablauf

### Vorabprüfung

`~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` lesen, Abschnitt `## Mandantenakten` prüfen.

Falls `Aktiviert: ✗` (Syndikus / in-house):
> Mandantenakten sind deaktiviert – Sie sind als [Kanzlei/in-house] konfiguriert und arbeiten mit einem einzigen Mandantenkontext. Falls Sie tatsächlich mehrere Mandanten betreuen, führen Sie `/arbeitsrecht:kaltstart-interview --redo` aus und wählen Sie Kanzleibetrieb. Andernfalls benötigen Sie `/arbeitsrecht:mandat-arbeitsbereich` nicht.

### Befehle

**`neu <kürzel>`** – Neue Mandatsakte anlegen.
1. Kürzel in Kleinbuchstaben, Bindestriche erlaubt (z.B. `mueller-ksg-2024`).
2. Kurzes Intake-Interview:
 > - Mandantenname (intern, nicht für Ausgaben)
 > - Sachverhalt in einem Satz (Kündigung / Untersuchung / Entsendung / Tarifstreit)
 > - Zuständiger Anwalt
 > - Aktenstatus: offen / ruhend / geschlossen
 > - Besondere Vertraulichkeitsstufe?
3. `mandat.md`, `verlauf.md` und `notizen.md` anlegen unter:
 `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/akten/<kürzel>/`

**`auflisten`** – Alle Akten tabellarisch mit Status und aktive-Akte-Flag anzeigen.

**`wechseln <kürzel>`** – Aktive Akte setzen. Alle folgenden Skill-Aufrufe arbeiten im Kontext dieser Akte.

**`schließen <kürzel>`** – Akte archivieren (in `_archiv/` verschieben, nie löschen). Keine Daten vernichten.

**`keine`** – Vom aktiven Mandat lösen; auf Kanzlei-Ebene-Kontext zurücksetzen.

### Aktenübergreifender Kontext

Bei `Aktenübergreifender Kontext: deaktiviert` (Standard): Ein Skill, der in Akte A arbeitet, liest niemals Dateien aus Akte B. Dies ist datenschutzrechtlich geboten (Paragraf 43a Abs. 2 BRAO, Paragraf 26 BDSG): Personalakte eines Arbeitnehmers darf nicht in die Analyse eines anderen einfließen.

Lerneffekte, die mehrere Mandate betreffen, werden in die Kanzlei-CLAUDE.md geschrieben, nicht in eine Akten-Datei.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

- Paragraf 43a Abs. 2 BRAO (Verschwiegenheitspflicht des Rechtsanwalts)
- Paragraf 203 StGB (Verletzung von Privatgeheimnissen)
- Paragraf 26 BDSG (Beschäftigtendatenschutz; gilt auch für anwaltlich bearbeitete Personaldaten)
- Paragraf 53 StPO (Zeugnisverweigerungsrecht des Rechtsanwalts)

## Beispiele

```
/arbeitsrecht:mandat-arbeitsbereich neu mueller-ksg-2024
Kündigung wegen betriebsbedingter Restrukturierung, Sozialauswahl streitig.
```

```
/arbeitsrecht:mandat-arbeitsbereich wechseln bayer-betriebsrat
```

```
/arbeitsrecht:mandat-arbeitsbereich auflisten
```

## Risiken / typische Fehler

- **Akten nicht schließen, wenn das Mandat endet.** Archivieren statt löschen – BRAO Paragraf 50 Abs. 2 schreibt 5 Jahre Aufbewahrung vor.
- **Mandant nicht anonymisieren.** Kürzel und interne Bezeichnung sollten nicht von Unbefugten identifiziert werden können.
- **Aktenübergreifende Suche ungewollt aktivieren.** Standardmäßig deaktiviert aus datenschutzrechtlichen Gründen.

## Aktuelle BAG-Linie 2025/2026 (live verifizieren vor Schriftsatzverwendung)

Drei aktuelle Leitentscheidungen, die über das Arbeitsrecht in den letzten zwoelf Monaten besonders weit ausstrahlen:

| Entscheidung | Tragende Aussage | Skill-Vertiefung |
| --- | --- | --- |
| **BAG, Urt. v. 23.10.2025 - 8 AZR 300/24** | **Equal Pay - Paarvergleich genuegt.** Eine einzige besser bezahlte Vergleichsperson des anderen Geschlechts mit gleicher oder gleichwertiger Arbeit reicht, um die Vermutung des Paragraf 22 AGG auszuloesen. Der Arbeitgeber muss konkret darlegen, dass die Differenz ausschließlich auf objektiven, geschlechtsneutralen Gruenden beruht. Pauschale Hinweise auf Medianwerte, Durchschnittsbetrachtungen oder Verhandlungsgeschick reichen nicht. Art. 157 AEUV bekommt damit Schaerfe. | `bag-equal-pay-paarvergleich` (fachanwalt-arbeitsrecht) / `bag-equal-pay-paarvergleich-8azr30024` (arbeitsrecht) |
| **BAG, Urt. v. 03.06.2025 - 9 AZR 104/24** | **Kein Verzicht auf gesetzlichen Mindesturlaub.** Im bestehenden Arbeitsverhaeltnis können Arbeitnehmer:innen auf den gesetzlichen Mindesturlaub nicht wirksam verzichten - auch nicht durch gerichtlichen Vergleich. Gilt selbst dann, wenn die Beendigung bereits feststeht und absehbar ist, dass der Urlaub krankheitsbedingt nicht mehr genommen werden kann. Ausgleichs-/Erledigungs-/Abgeltungsklauseln müssen sauber zwischen gesetzlichem Mindesturlaub, vertraglichem Mehrurlaub und bereits entstandener Urlaubsabgeltung unterscheiden. | `bag-mindesturlaub-kein-verzicht` (fachanwalt-arbeitsrecht) / `bag-mindesturlaub-kein-verzicht-9azr10424` (arbeitsrecht) |
| **BAG, Urt. v. 25.03.2026 - 5 AZR 108/25** | **Pauschale Freistellungsklauseln in Arbeitsvertragsformularen unwirksam.** Eine formularmaessige Freistellungsklausel, die dem Arbeitgeber das einseitige Recht gibt, Beschäftigte nach Kuendigung unter Fortzahlung der Vergütung freizustellen, ist nach AGB-Kontrolle unwirksam, wenn sie Arbeitnehmer:innen unangemessen benachteiligt. Freistellung bleibt im konkreten Fall möglich - braucht aber einen tragfaehigen Grund (ueberwiegende schutzwuerdige Arbeitgeberinteressen). Die pauschale Vorratsklausel reicht nicht. | `bag-freistellungsklausel-unwirksam` (fachanwalt-arbeitsrecht) / `bag-freistellungsklausel-unwirksam-5azr10825` (arbeitsrecht) |

> Diese drei Aktenzeichen sind Sucheinstieg. Vor Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (bundesarbeitsgericht.de, dejure.org) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung. Spezial-Skills oben enthalten Prüfschemata, Klagebausteine und Verteidigungsmuster.
