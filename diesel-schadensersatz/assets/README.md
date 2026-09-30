# Aktenstart-, E-Akte- und beA-Assets

[Plugin-README](../README.md) | [Repository-Start](../../README.md) | [Download-Index](../../ASSET_INDEX.md) | [Skill 20](../skills/20-eakte-export-kanzleisoftware/SKILL.md) | [Skill 21](../skills/21-bea-versandfertig-schriftsatz-anlagen/SKILL.md) | [Plugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/diesel-schadensersatz.zip)

Die Dateien sind neutrale, versionierte Verträge und Vorlagen für den sicheren Aktenstart, Kanzleisoftware-/DMS-Übergaben und beA-Versandkontrollen. Eine konkrete Importfähigkeit oder tatsächliche Gerichtseinreichung wird erst nach Zielsystem-, Anwalts- und Eingangskontrolle behauptet.

## Schemas

| Datei | Zweck |
|---|---|
| [aktenstart-manifest.schema.json](./schemas/aktenstart-manifest.schema.json) | strikter Übergabevertrag vom deterministischen Dateiinventar an Skill 01 |
| [arbeitsstand-basis.schema.json](./schemas/arbeitsstand-basis.schema.json) | gemeinsamer struktureller V2-Basisvertrag für die beiden folgenden Lifecycle-Verträge |
| [arbeitsstand.schema.json](./schemas/arbeitsstand.schema.json) | verbindlicher Finalvertrag; freigegebener Versand immer mit deterministischer `action_id` |
| [arbeitsstand-skill21-candidate.schema.json](./schemas/arbeitsstand-skill21-candidate.schema.json) | eng begrenzter Pre-Append-Vertrag für Skill 21, in dem `action_id` noch `null` sein darf |
| [fallakte.schema.json](./schemas/fallakte.schema.json) | JSON-Schema für die strukturierte Fallakte |
| [dms-register.schema.json](./schemas/dms-register.schema.json) | Spalten- und Feldvertrag für das DMS-Register |
| [bea-paketauftrag.schema.json](./schemas/bea-paketauftrag.schema.json) | Strikter Inputvertrag für Endfassung, Vorgang, Anlagen, Fundstellen und erwartete Hashes |
| [bea-paket-manifest.schema.json](./schemas/bea-paket-manifest.schema.json) | Manifest `1.1.0` mit Produktionszeit, tatsächlichen Namen, Größen, Seitenzahlen, Hashes und vollständigem Paket-Fingerprint |
| [bea-freigabe.schema.json](./schemas/bea-freigabe.schema.json) | Hashgebundene anwaltliche Inhalts-, Zuordnungs- und Sichtfreigabe |
| [bea-paket.schema.json](./schemas/bea-paket.schema.json) | JSON-Schema für den finalen beA-Paketprüfbericht und seine drei Statusstufen |

Für Speicherung und Skill-Übergaben gilt ausschließlich `arbeitsstand.schema.json`. Das Candidate-Schema ist nur für den ausdrücklich als Skill-21-Pre-Append gekennzeichneten Zwischenzustand bestimmt; vor der Persistenz muss der hostseitig finalisierte Zustand gegen den Finalvertrag validieren.

## Beispiele

| Datei | Zweck |
|---|---|
| [aktenstart-manifest-beispiel.json](./examples/aktenstart-manifest-beispiel.json) | minimales Startinventar mit zwei Kernunterlagen und ohne absolute Quellpfade |
| [arbeitsstand-beispiel.json](./examples/arbeitsstand-beispiel.json) | verlustfreie Schnelllauf-Übergabe mit Fakten-IDs, Gates, Delta und genau einem nächsten Skill |
| [fallakte-beispiel.json](./examples/fallakte-beispiel.json) | anonymisierte Beispiel-Fallakte |
| [dms-register-beispiel.csv](./examples/dms-register-beispiel.csv) | anonymisiertes Beispielregister |
| [bea-paketauftrag-beispiel.json](./examples/bea-paketauftrag-beispiel.json) | anonymisierter Beispielauftrag für Replik und zwei neue Anlagen |

## Vorlagen

| Datei | Zweck |
|---|---|
| [dms-register-vorlage.csv](./templates/dms-register-vorlage.csv) | leere Kopfzeile für neue Registerexporte |
| [kontrollbericht-vorlage.md](./templates/kontrollbericht-vorlage.md) | Prüfbericht für Mapping, Rechte, Konflikte und Testimport |
| [bea-paketauftrag-vorlage.json](./templates/bea-paketauftrag-vorlage.json) | auszufüllender Startvertrag für einen neuen beA-Paketbau |
| [bea-anlagenverzeichnis-vorlage.csv](./templates/bea-anlagenverzeichnis-vorlage.csv) | Abgleich von Bezugnahme, Original, Versandkopie, Stempel und Hash je Anlage |
| [bea-versandkontrolle-vorlage.md](./templates/bea-versandkontrolle-vorlage.md) | Paket-, Fingerprint-, Signatur-, Versand- und Eingangskontrolle mit ausstehender Freigabe |
| [kanzlei-arbeitskopf.md](./templates/kanzlei-arbeitskopf.md) | kompakte Status-, Frist-, Quellen- und Übergabeansicht vor jedem Arbeitsprodukt; nie Teil des Dokuments |
