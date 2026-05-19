# mandate/ — Mandatsportfolio

Dieses Verzeichnis enthält das Mandatsportfolio. Es gliedert sich in zwei Ebenen:

- **`_log.yaml`** — das Mandatsregister. Ein Eintrag pro Mandat. Maschinenlesbar für Skills. Maßgebliche Quelle für Auswertungen.
- **`[slug]/`** — mandatsbezogene Details. Darstellung und Verlauf. Für die menschliche Lektüre und Bearbeitung.

## Verzeichnisstruktur

```
mandate/
├── _log.yaml                  # Register (alle Mandate einschließlich abgeschlossener)
├── _README.md                 # diese Datei
└── [mandat-slug]/
    ├── mandat.md              # Sachverhaltsaufnahme, Rechtstheorie, Verfahrensstand
    └── verlauf.md             # fortlaufendes Ereignisprotokoll (nur Ergänzungen)
```

## Slug-Konventionen

Kleinschreibung, Bindestriche, Jahr am Ende. Beispiele:
- `mustermann-gmbh-v-lieferant-2026`
- `bundeskartellamt-anfrage-2026`
- `arbeitsrecht-schmidt-2026`

Das Jahr stabilisiert den Slug, auch wenn ein ähnliches Mandat später entsteht. Der Ordnername entspricht dem Slug.

## Wer schreibt was

| Datei | Erstellt durch | Direkt bearbeitbar? |
|---|---|---|
| `_log.yaml` | `/mandat-aufnahme`, `/mandat-aktualisierung`, `/mandat-abschluss` | Ja, aber Änderungen in `verlauf.md` des Mandats nachführen |
| `mandat.md` | `/mandat-aufnahme` bei Mandatsannahme; ergänzt durch `/mandat-abschluss` | Ja, für Fortentwicklung von Rechtstheorie und Verfahrensstand |
| `verlauf.md` | `/mandat-aufnahme` legt Grundlage; `/mandat-aktualisierung` und `/mandat-abschluss` ergänzen | In der Praxis nur Ergänzungen — frühere Einträge sind Protokoll |

## Abgeschlossene Mandate

Verbleiben im Verzeichnis. Nicht löschen. `/portfolio-status` blendet sie bei Standardauswertungen aus; `/portfolio-status --alle` schließt sie ein. Abgeschlossene Mandate sind die Grundlage für die Beurteilung des Gesamtportfolios.

## Korrekturen

Ist ein früherer Verlaufseintrag unrichtig, nicht bearbeiten. Einen neuen Eintrag ergänzen, der auf den fehlerhaften Eintrag Bezug nimmt und ihn korrigiert. Der Nachweis der Korrektur ist ebenso wichtig wie die Korrektur selbst.
