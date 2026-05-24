# Liquiditätsplanung — Power-Plugin

**Eigenständiges Power-Plugin** für wochenaktuelle Liquiditätsvorschauen nach deutschem Recht (§§ 17, 18, 19 InsO; § 1 StaRUG; BGH-Schema Passiva II). Funktioniert allein. Ergänzt sich optional mit `insolvenzrecht` und `steuerberater-werkzeuge`, hängt aber nicht von ihnen ab.

---

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| **Liquiditätsplanung** (`liquiditaetsplanung`, dieses Plugin) | [liquiditaetsplanung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |
| insolvenzrecht | [insolvenzrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzrecht.zip) |
| steuerberater-werkzeuge | [steuerberater-werkzeuge.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/steuerberater-werkzeuge.zip) |

Die URLs sind **stabil** und zeigen immer auf die neueste Version. Alle weiteren Plugins (Vertragsrecht, Datenschutz, Arbeitsrecht, …) sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

Hinweis: Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus **Code → Download ZIP** verwenden.

### Lokale Voraussetzungen für Excel-Export

Das Werkzeug `skills/liquiditaetsvorschau-3-6-12-monate/werkzeuge/build_liquiditaetsplan.py` erzeugt die gerichtsfeste `.xlsx`-Datei mit Formeln und bedingter Formatierung. Es braucht zwei Python-Module:

```bash
pip install openpyxl   # zwingend für den Excel-Export
pip install pyyaml     # optional, sonst Mini-YAML-Parser-Fallback
```

Ohne `openpyxl` beendet sich das Skript mit klarem Hinweis statt einer ImportError-Stacktrace. Skills, die nur die Liquiditätsplanung als Markdown/HTML-Output produzieren, brauchen die Pakete nicht.

### Zum Ausprobieren: Beispielakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

[testakte-beispielakte-edelholz-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beispielakte-edelholz-berlin.zip)

Enthält Firmenstammblatt, BWA, SuSa, OPOS, Bankauszüge, Steuer-/SV-Lage und einen fertigen Liquiditätsplan der fiktiven Edelholz Manufaktur Berlin GmbH.

Alternativ als ganzes Marketplace:

```bash
# Marketplace-Manifest aus dem Release ziehen
curl -L -O https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/marketplace.json
```

---

## Was ist drin

Drei Skills, alle fachlich autark:

| Skill | Zweck | Horizont |
| --- | --- | --- |
| `liquiditaetsvorschau-3wochen` | Wochenaktuelle Vorprüfung § 17 InsO (Freitag-Stichtag), Verhältnis zu offenen Forderungen, Ampel. | 3 Wochen |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Planung mit Sensitivität (Best/Base/Worst), Fortführungsprognose nach § 19 InsO. | 13 / 26 / 52 Wochen |
| `liquiditaetsvorschau-insolvenzrechtlich` | Gerichtsfeste Liquiditätsbilanz nach BGH-Schema (Passiva II zwingend, Volumeneffekt der Quote, titulierte Forderungen mit Nennwert). | Stichtagsbezogen |

## Ergebnisformate

Jeder Skill liefert standardmäßig eine **Excel-Tabelle** nach der hinterlegten Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`, KW-Spalten × Kategorien-Zeilen, Freitag als Wochenstichtag). Zusätzlich auf Wahl:

- **Interaktives HTML-Padlet** (`assets/padlet/liquiditaets-padlet.html`) — single-file, autark, rechnet die Ampel live nach BGH-Schema, speichert in `localStorage`, exportiert/importiert JSON.
- **Markdown-Artefakt** (`assets/markdown/liquiditaets-artefakt-vorlage.md`) — Tabellen, Indizienliste, Kurzfazit; wird bei jeder Folgemeldung neu geschrieben.
- **Memo** im Gutachtenstil (DOCX oder Markdown) — **nur auf ausdrückliche Anfrage**.

Die Skills fragen einmal am Anfang nach Format und merken sich die Antwort.

## Banking

Jeder Skill fragt einmal nach der Datenquelle:

1. **Manuell** im Padlet/Artefakt/Chat.
2. **Datei-Import** — CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS.
3. **Connector** — PSD2/FinTS oder verfügbare Anbieter (per `list_external_tools`).

Mandatsgeheimnis (§§ 203/204 StGB, § 43e BRAO) und Drittlandtransfer (DSGVO Art. 44 ff.) werden adressiert.

## BGH-Schema (Passiva II)

```
Aktiva I   = Bank + Kasse + freier zugesagter Kontokorrent (Stichtag)
Aktiva II  = Σ Einzahlungen KW t..t+2
Passiva I  = am Stichtag fällig, eingefordert, nicht echt gestundet
Passiva II = binnen 3 Wochen fällig (KW t+1 + KW t+2)

Lücke abs. = max(0, (Passiva I + Passiva II) − (Aktiva I + Aktiva II))
Quote      = Lücke abs. ÷ (Passiva I + Passiva II)   (Volumeneffekt
             BGH 19.12.2017 – II ZR 88/16, BGHZ 217, 129 Rn. 25 ff.)
```

**Ampel**: 🟢 Quote < 10 % und Liquidität KW t+2 ≥ 0 und < 2 Indizien. 🟡 Quote ≥ 10 %, KW t+2 ≥ 0, < 2 Indizien (schließbar). 🔴 sonst — § 17 InsO indiziert.

## Leitentscheidungen (Volltexte: `references/rechtsprechung/`)

1. BGH, 19.12.2017 – **II ZR 88/16**, BGHZ 217, 129 (Passiva II; Volumeneffekt)
2. BGH, 28.06.2022 – **II ZR 112/21**, ZIP 2022, 1606 (Bugwellenrspr.)
3. BGH, 28.04.2022 – **IX ZR 48/21**, ZIP 2022, 1341 (10-%-Schwelle)
4. BGH, 23.01.2025 – **IX ZR 229/22**, DB 2025, 381 (titulierte Forderungen)
5. BGH, 11.03.2025 – **II ZR 139/23** (objektive Umstände)
6. BGH, 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 (Grundsatzentscheidung)
7. BGH, 12.10.2006 – IX ZR 228/03, NJW 2007, 78 (Indizienkatalog)

Berufsständischer Hintergrund: IDW S 11 (12.08.2021), IDW S 6 — nicht im Vordergrund zitieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Alle Aussagen beruhen auf der im Plugin hinterlegten BGH-Rechtsprechung (`references/rechtsprechung/`) und genannter Kommentarliteratur. Die Skills ersetzen keine eigene anwaltliche oder steuerberatende Prüfung im Einzelfall.
