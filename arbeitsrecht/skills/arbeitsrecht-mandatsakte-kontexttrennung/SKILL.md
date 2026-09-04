---
name: arbeitsrecht-mandatsakte-kontexttrennung
description: "Für Arbeitsrechtliche Mandatsakte und Kontexttrennung: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Arbeitsrechtliche Mandatsakte und Kontexttrennung

Anwälte und Kanzleien arbeiten für mehrere Mandanten gleichzeitig. Eine Mandatsakte hält den Kontext eines Mandanten strikt von allen anderen getrennt. Dieser Skill verwaltet diese Akten.

## Zweck

Für Kanzleien mit mehreren Mandanten (Einzelkanzlei, Mittelkanzlei, Großkanzlei). Für Syndikusrechtsanwälte mit einem Arbeitgeber ist diese Funktion standardmäßig **deaktiviert** – alle Skills nutzen automatisch den Kanzlei-/Unternehmenskontext.

Im Arbeitsrecht entspricht eine "Akte" typischerweise einem bestimmten Mandanten-Sachverhalt:
- Eine konkrete Kündigung oder Kündigungsschutzklage
- Eine interne Untersuchung
- Ein Entsendungsprojekt
- Ein Tarifvertragsstreit
- Eine Massenentlassung / Betriebsänderung

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

## Ausgabeformat

**Neu:**
```
Mandatsakte angelegt: mueller-ksg-2024
========================================
Mandant:    [intern anonymisiert]
Sachverhalt: Kündigungsschutzklage nach betriebsbedingter Kündigung
Anwalt:     [Name]
Status:     offen
Ablage:     ~/.../akten/mueller-ksg-2024/

Dateien erstellt:
  mandat.md    – Akten-Stammdaten und Kontext
  verlauf.md   – Chronologisches Protokoll
  notizen.md   – Freie Notizen, entwürfe, Recherche-Ergebnisse
```

**Auflisten:**
```
Mandantenakten – Arbeitsrecht
=================================
● mueller-ksg-2024     [offen]    Kündigungsschutzklage      geändert: heute
  bayer-betriebsrat    [ruhend]   BR-Streitigkeit Paragraf 87 BetrVG   geändert: vor 3 Wo.
  huber-entsendung     [offen]    Entsendung Frankreich          geändert: gestern

● = aktive Akte
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

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


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
