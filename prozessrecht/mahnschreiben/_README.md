# mahnschreiben/ — vorprozessuale Mahnkorrespondenz

Dieses Verzeichnis enthält die Arbeitsergebnisse für jedes Mahnschreiben, das die Sozietät versendet: Zahlungsaufforderungen (§ 286 BGB), Mängelrügen mit Abhilfefrist, Abmahnungen, Trennungsforderungen aus dem Arbeitsverhältnis sowie Aufforderungen zur Beweissicherung.

Getrennt von `mandate/`, weil:

- Nicht jedes Mahnschreiben wird zu einem erfassten Mandat. Geringfügige Zahlungsaufforderungen und Routinemahnungen erfordern keinen Mandatseintrag.
- Jedes Mahnschreiben folgt derselben Arbeitsstruktur (Sachverhaltsaufnahme → Entwurf → Versand → Checkliste), unabhängig davon, ob es später zu einem Mandat wird.
- Wird aus einem Mahnschreiben ein Mandat, verweist `mandate/[mandat-slug]/mandat.md` zurück auf diesen Ordner — die Entstehungsgeschichte des Schreibens verbleibt beim Schreiben.

## Verzeichnisstruktur

```
mahnschreiben/
├── _README.md                     # diese Datei
└── [slug]/
    ├── sachverhalt.md             # Sachverhaltsaufnahme, Strategie, Druckmittel, Verschwiegenheitsfilter
    ├── entwurf-v1.docx            # das Schreiben (v2, v3 bei Überarbeitungen)
    └── checkliste.md              # Checkliste nach Versand — Zustellungsnachweis, Abschriften, vorgemerkte Fristen, Wiedervorlage
```

## Slug-Konventionen

`[art]-[gegenseite]-[jjjj-mm]`. Beispiele:

- `zahlung-mustermann-gmbh-2026-04`
- `abmahnung-wettbewerber-x-2026-04`
- `maengelruege-lieferant-2026-04`
- `trennung-schmidt-2026-04`
- `beweissicherung-auftragnehmer-2026-04`

## Ablauf

1. `/prozessrecht:mahnung-aufnahme [titel]` → führt adaptive Sachverhaltsaufnahme durch, schreibt `sachverhalt.md`
2. `/prozessrecht:mahnung-entwurf [slug]` → prüft Privilegien und Verzichtsrisiken (§ 203 BGB analog; anwaltliche Verschwiegenheit), erstellt `.docx`, schreibt `checkliste.md`, bietet Mandatsanlage an

## Verhältnis zu Mandaten

Nach Erstellung des Mahnschreibens prüft `mahnung-entwurf` die rechtliche und wirtschaftliche Erheblichkeit (Heuristik aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/prozessrecht/CLAUDE.md`) und bietet die Anlage eines Mandats an. Bei Bejahung wird ein Eintrag in `mandate/_log.yaml` mit `quelle: mahnschreiben` erstellt, und `mandate/[mandat-slug]/mandat.md` verweist zurück auf diesen Mahnschreiben-Ordner.

Unerhebliche Mahnschreiben verbleiben nur hier. Sie sind gleichwohl ein Arbeitsergebnis — werden aber nicht im Portfolio erfasst.

## Korrekturen und Versionen

Einen versandten Entwurf nie überschreiben. Muss ein Schreiben nach Versand ergänzt werden (z. B. ergänzende Mahnung), ist `entwurf-v2.docx` anzulegen. Der Versionsverlauf ist selbst ein wichtiger Nachweis.
